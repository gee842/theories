"""Exercise existing contact operations beyond the original fixed scheduler.

This is a request-word extension, not a new event law or autonomous scheduler.
Original ancestry is retained by artifact bindings and the prior review.
"""
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[6]
sys.path.insert(0, str(HERE))
import remaining_dependency as native

PROTOCOL_HASH = '47b25788e20a10c8aa074091fa1447f5eb03f08a136eb01d8c7bffb02357d301'
NAMES = ('law_01_learned', 'calibration_break', 'false_dependence')


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def projection(event):
    """Richer than the reader, retaining all its demonstrated inputs."""
    return {key: deepcopy(event[key]) for key in ('kind', 'detail', 'charge')} | {
        'state': {key: deepcopy(event['state'][key])
                  for key in ('account', 'inherited', 'controller')}}


def bindings(original):
    result = dict(original['source_hashes'])
    for path, expected in result.items():
        assert digest(ROOT/path) == expected, path
    additions = [
        'remaining-dependency-results.json',
        'remaining-dependency-independent-check.json',
        'remaining_dependency_check_review.py',
        'remaining-dependency/formal/RemainingDependency.lean',
        'remaining-dependency/formal/FORMAL-NOTES.md',
        'remaining-dependency/formal/verification.json',
        'CORRECTION-LOCALIZATION-PROTOCOL.md',
        'correction_localization.py',
    ]
    for name in additions:
        path = HERE/name
        result[str(path.relative_to(ROOT))] = digest(path)
    assert digest(HERE/'CORRECTION-LOCALIZATION-PROTOCOL.md') == PROTOCOL_HASH
    receipt = json.loads((HERE/'remaining-dependency-independent-check.json').read_text())
    assert receipt['results_sha256'] == digest(HERE/'remaining-dependency-results.json')
    return result


def extend(original, source_case, selector):
    p = source_case['parameters']
    parent = deepcopy(original['parents'][p['parent']])
    run = native.Continuation(parent, p['law'], p['full_law'], p['policy'],
                              p['fault'], p['capacity'])
    status, retained = run.execute(wait=p['wait'], context_change=p['context_change'])
    assert status == source_case['status'] and retained == source_case['retention_status']
    assert run.trace == source_case['trace']
    assert run.snapshot() == source_case['final']
    start = run.snapshot()
    cut = len(run.trace)
    run.port.command(1)
    run.port.challenge()
    run.port.contact(selector)
    run.controller.write(1)
    run.controller.read()
    run.controller.commit()
    run.controller.retain()
    suffix = deepcopy(run.trace[cut:])
    final = run.snapshot()
    assert len(suffix) == 7
    assert Q(start['account']['fuel']) - Q(final['account']['fuel']) == Q(95732, 65536)
    assert final['account']['fuel'] == '166143/32768'
    for event in suffix:
        state = event['state']
        assert state['inherited'] == start['inherited']
        assert state['whole_account'] == '145'
        assert all(state['native'][key] == start['native'][key]
                   for key in ('source', 'load', 'waste', 'test_law', 'full_law'))
    expected = [0, 0] if source_case['name'] == 'false_dependence' and selector == 0 else [0, 1]
    assert final['controller']['values'] == expected
    assert final['controller']['selected'] == (None if expected == [0, 0] else 1)
    return dict(name=f"{source_case['name']}_contact_{selector}",
                source_case=source_case['name'], contact_selector=selector,
                inherited_consumption=source_case['inherited_consumption'],
                old_endpoint=start, original_prefix_verified=True,
                original_prefix_records=cut, trace=suffix, final=final)


def main():
    original = json.loads((HERE/'remaining-dependency-results.json').read_text())
    source_bindings = bindings(original)
    selected = {name: next(c for c in original['cases'] if c['name'] == name)
                for name in NAMES}
    projected = {name: [projection(e) for e in case['trace']]
                 for name, case in selected.items()}
    assert all(len(p) == 16 for p in projected.values())
    assert projected[NAMES[0]] == projected[NAMES[1]] == projected[NAMES[2]]
    cases = [extend(original, selected[name], selector)
             for name in NAMES for selector in (1, 0)]
    same = [[projection(e) for e in c['trace']] for c in cases if c['contact_selector'] == 1]
    assert same[0] == same[1] == same[2]
    alternate = [[projection(e) for e in c['trace']] for c in cases if c['contact_selector'] == 0]
    assert alternate[0] == alternate[1] and alternate[1] != alternate[2]
    assert bindings(original) == source_bindings
    result = dict(
        scope='Existing source-interface request words; not autonomous or physically derived channel selection',
        protocol_sha256=PROTOCOL_HASH, source_bindings=source_bindings,
        ancestry_scope='Bound to previous independent reconstruction; small original continuation replayed here',
        old_projection=dict(source_cases=list(NAMES), records_per_case=16,
                            fields=['kind', 'detail', 'charge', 'account', 'inherited', 'controller'],
                            identical=True),
        case_count=len(cases), suffix_event_count=sum(len(c['trace']) for c in cases),
        cases=cases,
        limitations=[
            'No final full-load receipt is acquired.',
            'Contact selector interpretation and faithfulness are supplied source semantics.',
            'The fixed executor does not choose these new request words.',
            'No new source, fuel, apparatus or inherited completion is provided.',
            'Full-load service is not restored and ethical warrant is not derived.',
            'No new Lean build or universal scheduling theorem is claimed.',
        ])
    target = HERE/'correction-localization-results.json'
    target.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps(dict(status='pass', cases=len(cases), suffix_events=42,
                          bindings=len(source_bindings), results_sha256=digest(target))))


if __name__ == '__main__':
    main()
