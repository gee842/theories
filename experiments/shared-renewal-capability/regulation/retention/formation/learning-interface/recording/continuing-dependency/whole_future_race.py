"""Exploratory exact comparison of two inherited continuation arrangements.

No new law or ethical score. Success is uninterrupted restoration of one lost A
while preserving H. Capture is allowed; a further wear, damage, leak, or H copy
ends this episode unsuccessfully. This is not unrestricted eventual restoration.
The comparison was selected after inspecting the inherited law and endpoints.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[7]
PROCESS = HERE.parents[2] / 'process.py'
spec = importlib.util.spec_from_file_location('_whole_future_native', PROCESS)
native = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = native
spec.loader.exec_module(native)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact(q):
    return dict(numerator=q.numerator, denominator=q.denominator,
                decimal=float(q))


def race(law, state):
    rows = native.channels(law, state)
    total = sum((rate for _, _, rate in rows), Q(0))
    assert total > 0
    success = Q(0)
    failures = {}
    visited = [dict(state=list(state), rates={e: str(q) for e, _, q in rows})]
    for event, target, rate in rows:
        weight = rate / total
        if event in ('copy_a', 'bulk_a'):
            assert native.counts(target) == (39, 39) and target[2] == 1
            success += weight
        elif event == 'capture':
            assert not state[4] and target[4]
            child, losses, records = race(law, target)
            success += weight * child
            for label, probability in losses.items():
                failures[label] = failures.get(label, Q(0)) + weight * probability
            visited.extend(records)
        else:
            assert event in ('bulk_h', 'wear_a', 'wear_h', 'wear_res_a',
                             'damage', 'leak_common', 'leak_local')
            failures[event] = failures.get(event, Q(0)) + weight
    assert success + sum(failures.values(), Q(0)) == 1
    return success, failures, visited


def main():
    inherited_path = HERE / 'results.json'
    inherited = json.loads(inherited_path.read_text())
    assert sha(PROCESS) == inherited['source_hashes'][str(PROCESS.relative_to(ROOT))]
    law = native.Law(material=78)
    report = {}
    probabilities = {}
    for label, key, expected in (
        ('local', 'local_reconstruction', (38, 39, 1, 1, 0, 1, 215)),
        ('bulk', 'bulk_reconstruction', (38, 39, 1, 1, 0, 0, 216)),
    ):
        endpoint = tuple(inherited['histories'][key]['final'])
        assert endpoint == expected
        worn = [t for e, t, _ in native.channels(law, endpoint) if e == 'wear_a']
        assert len(worn) == 1
        probability, losses, records = race(law, worn[0])
        assert len(records) == 2
        probabilities[label] = probability
        report[label] = dict(inherited_endpoint=list(endpoint), after_wear=list(worn[0]),
                             success=exact(probability),
                             failures={k: exact(v) for k, v in losses.items()},
                             transient_states=records)

    # Independently written hand equations from the inspected channel table,
    # with each rate scaled by 1,000,000. These are not fitted to output values.
    local_hand = Q(38, 215000156) + Q(215000000, 215000156)*Q(1000038, 1000157)
    bulk_hand = Q(216000000, 216000078)*Q(1000000, 1000079)
    assert probabilities['local'] == local_hand
    assert probabilities['bulk'] == bulk_hand
    difference = probabilities['bulk'] - probabilities['local']
    assert difference > 0
    output = dict(
        scope='Exact uninterrupted restoration race; no eventual-reachability or ethical ranking',
        selection='Exploratory comparison of previously reached endpoints; not preregistered',
        law=law.record(), results=report, bulk_minus_local=exact(difference),
        hand_equations_match=True, outcomes_sum_to_one=True,
        source_hashes={str(p.relative_to(ROOT)): sha(p) for p in
                       (Path(__file__), PROCESS, Path(native.arithmetic.__file__), inherited_path)},
    )
    (HERE / 'whole-future-race.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k: v['success'] for k, v in report.items()} |
                     {'bulk_minus_local': exact(difference)}, indent=2))


if __name__ == '__main__':
    main()
