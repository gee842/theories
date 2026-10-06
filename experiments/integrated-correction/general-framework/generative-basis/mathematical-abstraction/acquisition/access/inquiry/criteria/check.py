"""Question partitions of the unchanged, permissive effectful inquiry graph."""
from hashlib import sha256
import importlib.util
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
ROOT = next(p for p in HERE.parents if (p / 'AGENTS.md').exists())
spec = importlib.util.spec_from_file_location('inquiry_graph', PARENT / 'check.py')
graph = importlib.util.module_from_spec(spec)
spec.loader.exec_module(graph)  # Definitions only: no experiment or main invocation.
LABELS = graph.LABELS
INDEX = {label: i for i, label in enumerate(LABELS)}


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def partitions(prefix=(0,)):
    if len(prefix) == len(LABELS):
        yield prefix
    else:
        for value in range(max(prefix) + 2):
            yield from partitions(prefix + (value,))


PARTITIONS = tuple(partitions())


def coarser(p, q):
    """p <= q: each q block is contained in a p block."""
    return all(q[i] != q[j] or p[i] == p[j]
               for i in range(4) for j in range(4))


def join(p, q):
    pairs = list(zip(p, q))
    return tuple(list(dict.fromkeys(pairs)).index(x) for x in pairs)


def terminal(labels, partition):
    return len({partition[INDEX[x]] for x in labels}) == 1


def fixed_point(partition, parity, broken):
    winning = {s: 0 for s in graph.STATES if terminal(s[0], partition)}
    policy = {}
    while True:
        additions = {}
        for state in graph.STATES:
            if state in winning:
                continue
            choices = []
            for action in ('a', 'reset', 'read', 'probe'):
                children = graph.successors(state, action, parity, broken)
                if children and all(c in winning for c in children.values()):
                    choices.append((1 + max(winning[c] for c in children.values()), action))
            if choices:
                depth, action = min(choices)
                additions[state], policy[state] = depth, action
        if not additions:
            return winning, policy
        winning.update(additions)


def main():
    parent = json.loads((PARENT / 'results.json').read_text())
    parent_review = json.loads((PARENT / 'review-check.json').read_text())
    assert parent['checker_sha256'] == digest(PARENT / 'check.py')
    assert parent_review['producer_results_sha256'] == digest(PARENT / 'results.json')
    bindings = dict(parent['source_bindings'])
    for name in ('check.py', 'PROTOCOL.md', 'results.json', 'review-check.json'):
        bindings[str((PARENT / name).relative_to(ROOT))] = digest(PARENT / name)
    for name, expected in bindings.items():
        assert digest(ROOT / name) == expected, name
    inherited = {(tuple(d['labels']), d['phase'], d['packets'], d['parity'],
                  d['broken_reset'], d['target']): d['native_depth']
                 for d in parent['decisions']}
    records, families = [], []
    saved = {}
    comparisons = 0
    for partition, parity, broken in product(PARTITIONS, range(2), range(2)):
        winning, policy = fixed_point(partition, parity, broken)
        saved[partition, parity, broken] = winning
        for state in graph.STATES:
            labels, phase, packets = state
            record = dict(partition=partition, labels=labels, phase=phase,
                          packets=packets, parity=parity, broken_reset=broken,
                          native_depth=winning.get(state), first_action=policy.get(state))
            records.append(record)
            target = {(0, 1, 2, 3): 'four_causes',
                      (0, 1, 2, 2): 'three_behaviors'}.get(partition)
            if target is not None:
                assert inherited[labels, phase, packets, parity, broken, target] == winning.get(state)
                comparisons += 1
    expected = {
        0: {(0, 0, 0, 0)},
        1: {(0, 0, 0, 0), (0, 1, 1, 1), (0, 1, 0, 0)},
        2: {p for p in PARTITIONS if p[2] == p[3]},
    }
    for phase, packets, parity, broken in product(range(3), range(3), range(2), range(2)):
        state = LABELS, phase, packets
        attainable = {p for p in PARTITIONS if state in saved[p, parity, broken]}
        assert attainable == expected[packets]
        assert all(q in attainable for p in attainable for q in PARTITIONS if coarser(q, p))
        maximal = sorted(p for p in attainable if not any(p != q and coarser(p, q) for q in attainable))
        greatest = [p for p in attainable if all(coarser(q, p) for q in attainable)]
        missing_joins = [(p, q, join(p, q)) for p in sorted(attainable)
                         for q in sorted(attainable) if p < q and join(p, q) not in attainable]
        families.append(dict(phase=phase, packets=packets, parity=parity,
                             broken_reset=broken, attainable=sorted(attainable),
                             maximal=maximal, greatest=greatest, missing_joins=missing_joins))
    assert len(PARTITIONS) == 15 and len(records) == 8100 and comparisons == 1080
    report = dict(
        scope='Finite mathematical extension; no new physical execution or learned criterion',
        original_experiments_executed=False, source_bindings=bindings,
        labels=LABELS, partitions=PARTITIONS, decisions=records, families=families,
        decision_count=len(records), parent_decisions_preserved=comparisons,
        inherited_retained_probes=parent_review['retained_original_probe_records'],
        inherited_retention_failures=parent_review['original_probe_retention_failures'],
        delayed_demand_witnesses=[
            dict(first_probe_output=1, observed_arrival=0,
                 surviving_labels=['B', 'C0', 'C1'], later_question='initial B?',
                 conflicting_labels=['B', 'C0'], packets_remaining=0),
            dict(first_probe_output=0, observed_arrival=0,
                 surviving_labels=['A', 'C0', 'C1'], later_question='initial A?',
                 conflicting_labels=['A', 'C0'], packets_remaining=0)],
        protocol_sha256=digest(HERE / 'PROTOCOL.md'), checker_sha256=digest(Path(__file__)))
    (HERE / 'results.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(dict(partitions=15, checked_decisions=len(records),
                         inherited_comparisons=comparisons,
                         full_belief_attainable_counts={k: len(v) for k, v in expected.items()},
                         source_bindings=len(bindings))))


if __name__ == '__main__':
    main()
