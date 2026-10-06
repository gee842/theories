"""Independent finite reconstruction; no producer or native-model import.

The transition relation below was written from the unchanged FormedSelection
source. Complete graph discovery and bottom-up reachable endpoint calculation
are distinct from the producer's native-channel import and recursive profile.
"""
from collections import deque
from itertools import product
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[7]
RESULT = HERE / 'results.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def population(s):
    return s[0] + s[1] + int(s[2] != 0)


def counts(s):
    return s[0] + int(s[2] == 1), s[1] + int(s[2] == 2)


def energy(s):
    return sum(s[4:7])


def rank(s):
    return 4*s[6] + 2*s[5] + 2*s[4] + s[3] + population(s)


def successors(material, s):
    a, h, r, c, local, f, source = s
    assert min(a, h, f, source) >= 0 and r in (0, 1, 2)
    assert c in (0, 1) and local in (0, 1) and population(s) <= material
    room = population(s) < material
    answer = []

    def add(label, enabled, **changes):
        if enabled:
            target = list(s)
            positions = {'a': 0, 'h': 1, 'r': 2, 'c': 3,
                         'local': 4, 'f': 5, 'source': 6}
            for key, value in changes.items():
                target[positions[key]] = value
            target = tuple(target)
            assert min(target) >= 0 and population(target) <= material
            assert target[5] <= f and target[6] <= source
            assert rank(target) < rank(s)
            answer.append((label, target))

    add('form_a', not c and room and f > 0, a=a+1, f=f-1)
    add('form_h', not c and room and f > 0, h=h+1, f=f-1)
    add('bind_a', a > 0 and r == 0 and f > 0, a=a-1, r=1, f=f-1)
    add('bind_h', h > 0 and r == 0 and f > 0, h=h-1, r=2, f=f-1)
    add('repair', r == 1 and not c and f > 0, c=1, f=f-1)
    add('capture', c == 1 and not local and source > 0, local=1, source=source-1)
    add('copy_a', r == 1 and local == 1 and room, a=a+1, local=0)
    add('copy_h', r == 2 and local == 1 and room, h=h+1, local=0)
    add('bulk_a', counts(s)[0] > 0 and room and f > 0, a=a+1, f=f-1)
    add('bulk_h', counts(s)[1] > 0 and room and f > 0, h=h+1, f=f-1)
    add('wear_a', a > 0, a=a-1)
    add('wear_h', h > 0, h=h-1)
    add('wear_res_a' if r == 1 else 'wear_res_h', r != 0, r=0)
    add('damage', c == 1, c=0)
    add('leak_common', f > 0, f=f-1)
    add('leak_local', local == 1, local=0)
    return tuple(answer)


def graph_from(roots):
    graph, pending = {}, deque(roots)
    while pending:
        key = pending.popleft()
        if key in graph:
            continue
        material, state = key
        graph[key] = successors(material, state)
        pending.extend((material, target) for _, target in graph[key])
    return graph


def endpoint_profiles(graph):
    result = {}
    for (material, state), edges in sorted(graph.items(), key=lambda item: rank(item[0][1])):
        profile = [-1] * (material+1)
        if state[2] == 1:
            a, h = counts(state)
            profile[h] = a
        for _, target in edges:
            following = result[material, target]
            profile = [max(a, b) for a, b in zip(profile, following)]
        result[material, state] = tuple(profile)
    return result


def allocation_minimum(c, local, source, n):
    """Enumerate copy-route allocations, rather than repeat the closed formula."""
    alternatives = []
    for repair in range(2 if not c else 1):
        accessible = local + (source if c or repair else 0)
        for local_copies in range(n+1):
            if local_copies <= accessible:
                alternatives.append(repair + n-local_copies)
    return min(alternatives)


def replay(material, initial, word):
    state, spent, trace = tuple(initial), 0, []
    for event in word:
        matches = [target for label, target in successors(material, state) if label == event]
        assert len(matches) == 1, (state, event, matches)
        target = matches[0]
        expense = energy(state)-energy(target)
        assert expense == int(event not in ('capture', 'wear_a', 'wear_h',
                                           'wear_res_a', 'wear_res_h', 'damage'))
        trace.append({'event': event, 'before': list(state),
                      'after': list(target), 'spent': expense})
        spent += expense
        state = target
    assert energy(state)+spent == energy(initial)
    return state, spent, trace


def ledger(s):
    return dict(free_A=s[0], free_H=s[1], resident=s[2], intact=s[3],
                local=s[4], common=s[5], source=s[6],
                total_A=counts(s)[0], total_H=counts(s)[1], energy=energy(s))


def preparation_word(bound_paths):
    # Fail on a changed native definition instead of silently trusting the
    # producer's expanded list. These are the complete four word definitions.
    definitions = {
        'ActionPreparation.lean': '''List.replicate 16 .formH ++
          [.formA,.formA,.formA,.associateA,.repair] ++
          (List.replicate 13 [.capture,.localCopyA]).flatten ++ [.capture]''',
        'RevisionPreparation.lean': '''List.replicate 5 .formA ++
          List.replicate 5 .formH ++ ActionPreparation.word''',
        'EvaluationPreparation.lean': '''List.replicate 9 .formA ++
          List.replicate 9 .formH ++ RevisionPreparation.word''',
        'SuccessionPreparation.lean': '''List.replicate 9 .formA ++
          List.replicate 9 .formH ++ EvaluationPreparation.word''',
    }
    found = {}
    for path in bound_paths:
        if path.name in definitions:
            body = re.search(r'def word\s*:.*?:=\s*(.*?)\n\ndef ',
                             path.read_text(), re.DOTALL).group(1)
            assert ''.join(body.split()) == ''.join(definitions[path.name].split())
            found[path.name] = body
    assert set(found) == set(definitions)
    word = ['form_h']*16 + ['form_a']*3 + ['bind_a', 'repair']
    word += ['capture', 'copy_a']*13 + ['capture']
    for count in (5, 9, 9):
        word = ['form_a']*count + ['form_h']*count + word
    return word


def main():
    data = json.loads(RESULT.read_text())
    bindings = {path: sha(ROOT/path) for path in data['source_hashes']}
    assert bindings == data['source_hashes']
    assert len(bindings) == 9
    cases = data['cases']
    settings = list(product(range(2), range(2), range(5), range(2),
                            range(2), range(2), range(6), range(5)))
    assert len(cases) == len(settings) == 4800
    roots = []
    for row, (a, h, n, extra, c, local, f, source) in zip(cases, settings):
        start = (a, h, 1, c, local, f, source)
        material = a+h+1+n+extra
        assert tuple(row['initial']) == start and row['material'] == material
        assert row['deficit'] == n and row['extra_places'] == extra
        roots.append((material, start))
    graph = graph_from(roots)
    profiles = endpoint_profiles(graph)
    positive = events = 0
    for row, (_, _, n, _, c, local, f, source), (material, state) in zip(cases, settings, roots):
        minimum = allocation_minimum(c, local, source, n)
        assert row['minimum_common'] == minimum
        maximum = profiles[material, state][state[1]]
        reachable = maximum >= state[0]+1+n
        assert row['max_reachable_A'] == maximum
        assert row['reachable'] == reachable == (f >= minimum)
        if reachable:
            final, _, _ = replay(material, state, row['witness_word'])
            assert counts(final) == (state[0]+1+n, state[1]) and final[2] == 1
            positive += 1
            events += len(row['witness_word'])
        else:
            assert row['witness_word'] is None
    grid_counts = dict(states=len(graph), edges=sum(map(len, graph.values())),
                       positive_witnesses=positive, witness_events=events)
    assert grid_counts == data['grid_counts']

    histories = data['histories']
    initial = (0, 0, 0, 0, 0, 360, 230)
    ancestor_word = preparation_word([ROOT/path for path in bindings])
    ancestor, _, _ = replay(78, initial, ancestor_word)
    assert len(ancestor_word) == 94 and ancestor == (38, 39, 1, 1, 1, 293, 216)
    disturbance_word = ['leak_common']*292 + ['leak_local', 'wear_a']
    base, _, _ = replay(78, ancestor, disturbance_word)
    assert base == (37, 39, 1, 1, 0, 1, 216)
    local_word, bulk_word = ['capture', 'copy_a'], ['bulk_a']
    local_state, _, _ = replay(78, base, local_word)
    bulk_state, _, _ = replay(78, base, bulk_word)
    local_damage, _, _ = replay(78, local_state, ['damage'])
    bulk_damage, _, _ = replay(78, bulk_state, ['damage'])
    rich_wear, _, _ = replay(78, ancestor, ['wear_a'])
    expected_histories = {
        'ancestor': (initial, ancestor_word),
        'disturbance': (ancestor, disturbance_word),
        'local_reconstruction': (base, local_word),
        'bulk_reconstruction': (base, bulk_word),
        'local_after_damage': (local_state, ['damage']),
        'bulk_after_damage': (bulk_state, ['damage']),
        'local_repair': (local_damage, ['repair']),
        'full_local_continuation': (initial, ancestor_word+disturbance_word+local_word+['damage', 'repair']),
        'full_bulk_continuation': (initial, ancestor_word+disturbance_word+bulk_word+['damage']),
        'rich_wear': (ancestor, ['wear_a']),
        'rich_bulk': (rich_wear, ['bulk_a']),
        'rich_local': (rich_wear, ['copy_a']),
        'no_need': (ancestor, []),
    }
    assert set(histories) == set(expected_histories) | {'bulk_next_events'}
    actual_events = 0
    for name, (start, word) in expected_histories.items():
        record = histories[name]
        final, expense, trace = replay(78, start, word)
        assert record == dict(initial=list(start), word=word, final=list(final),
                              expenditure=expense, trace=trace,
                              initial_ledger=ledger(start), final_ledger=ledger(final)), name
        actual_events += len(word)
    assert local_state[:5] == bulk_state[:5] == (38, 39, 1, 1, 0)
    assert energy(local_state) == energy(bulk_state) == 216
    assert local_state[5:] == (1, 215) and bulk_state[5:] == (0, 216)
    assert histories['bulk_next_events'] == [event for event, _ in successors(78, bulk_damage)]
    blocked_graph = graph_from([(78, bulk_damage)])
    assert all(state[3] == 0 and state[5] == 0 for _, state in blocked_graph)
    assert all(event != 'repair' for edges in blocked_graph.values() for event, _ in edges)
    receipt = dict(
        status='passed', producer_imported=False, native_model_imported=False,
        method='Independent native transitions, complete graph discovery and bottom-up endpoint profiles; source-bound ancestry replay',
        configurations=len(cases), grid_counts=grid_counts,
        source_binding_count=len(bindings), source_hashes=bindings,
        producer_result_sha256=sha(RESULT), checker_sha256=sha(Path(__file__)),
        actual_history_records=len(expected_histories), actual_event_occurrences=actual_events,
        ancestor_events=len(ancestor_word), shared_prefix_events=len(ancestor_word+disturbance_word),
        full_local_events=len(expected_histories['full_local_continuation'][1]),
        full_bulk_events=len(expected_histories['full_bulk_continuation'][1]),
        equal_energy=216, support_compositions=[list(local_state[5:]), list(bulk_state[5:])],
        blocked_continuation_states=len(blocked_graph),
        blocked_continuation_edges=sum(map(len, blocked_graph.values())),
        proof_scope='Finite reconstruction plus independently reviewed general hand argument; no new Lean build or acquisition mechanism certified here')
    (HERE/'independent-check.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps({key: value for key, value in receipt.items() if key != 'source_hashes'}, indent=2))


if __name__ == '__main__':
    main()
