"""Independent replay of six native witnesses and their rational rates.

Reuses the previously accepted independent acquisition-prefix interpreter and
its independent native relation. Imports neither acquisition producer, native
process nor operative producer. Re-derives the rate table and apparatus guards
here from the inspected declared laws. No original twenty-case sweep is run.
"""
from copy import deepcopy
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'AGENTS.md').exists())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
HELPERS = {
    HERE / 'independent_check.py':
        'fc66a8377d36fb66a5f07370ac004ff3394bab8d79499444cb6c8ebb991c4aa9',
    HERE.parent / 'independent_check.py':
        'c9ff5611ac3248b02db951bb2edcf7bf23e77d559f6e7da438c67047791a9250',
}
for path, digest in HELPERS.items():
    assert sha(path) == digest
spec = importlib.util.spec_from_file_location('_accepted_independent_acquisition',
                                              HERE / 'independent_check.py')
review = importlib.util.module_from_spec(spec)
spec.loader.exec_module(review)

CASES = (
    ('a_vacancy', 'assembled', ('wear_a', 'copy_a'), [35,36,1,1,0,290,216], 84),
    ('h_vacancy', 'assembled', ('wear_h', 'copy_a'), [36,35,1,1,0,290,216], 84),
    ('source_present_repair', 'assembled', ('leak_local', 'damage', 'repair'),
     [35,36,1,1,0,289,216], 85),
    ('store_response', 'assembled', ('leak_local', 'capture'),
     [35,36,1,1,1,290,215], 84),
    ('source_depleted_repair', 'assembled',
     ('leak_local',) + ('capture', 'leak_local') * 216 + ('damage', 'repair'),
     [35,36,1,1,0,289,0], 301),
    ('installed_continuation', 'installed',
     ('capture', 'wear_h', 'copy_a', 'damage', 'repair'),
     [36,35,1,1,0,280,214], 96),
)


def apparatus(state):
    return {k: deepcopy(v) for k, v in state.items() if k not in ('plant', 'spent')}


def rates(state):
    """Default active source rates, independently evaluated with rationals."""
    a, h, r, c, local, common, source = state['plant']
    total_a, total_h = a + (r == 1), h + (r == 2)
    p = 78 - review.occupied(state) - total_a - total_h
    slow = Q(1, 1000000)
    raw = {
        'form_a': (1-c)*p*common,
        'form_h': (1-c)*p*common,
        'bind_a': a*common*(r == 0),
        'bind_h': h*common*(r == 0),
        'repair': common*(r == 1)*(1-c),
        'capture': source*c*(1-local),
        'copy_a': p*local*(r == 1),
        'copy_h': p*local*(r == 2),
        'bulk_a': slow*total_a*p*common,
        'bulk_h': slow*total_h*p*common,
        'wear_a': slow*a,
        'wear_h': slow*h,
        'wear_res_a': slow*(r == 1),
        'wear_res_h': slow*(r == 2),
        'damage': slow*c,
        'leak_common': slow*common,
        'leak_local': slow*local,
    }
    positive = {name: str(Q(value)) for name, value in raw.items() if value > 0}
    enabled = {name for name, _ in review.base.successors(78-review.occupied(state),
                                                         tuple(state['plant']))}
    assert set(positive) == enabled
    return positive


def apparatus_guards(state):
    """Preconditions for successful declared operations; never invoke failures."""
    a, h, _, _, _, common, _ = state['plant']
    pending = state['pending']
    idle = pending is None
    stage = pending['stage'] if pending else None
    phase = state['reader_phase']
    n = len(state['read_values'])
    formed = state['reader'] and idle and common >= 1
    return {
        'assemble_cell': idle and a >= 1 and h >= 1 and common >= 1
                         and state['cell_count'] < 2,
        'assemble_reader': idle and a >= 1 and h >= 1 and common >= 1
                           and not state['reader'],
        'bind_contact0': idle and state['cell_count'] >= 1
                         and state['cells'][0] is None and common >= 2,
        'bind_contact1': idle and state['cell_count'] >= 2
                         and state['cells'][1] is None and common >= 2,
        'recorded_macro_completion': stage == 'bound',
        'contact_latched_or_lost': stage == 'completed',
        'record_committed': stage == 'latched' and state['escrow'] == 1,
        'reader_activate': formed and phase == 'cold',
        'reader_read0': formed and phase == 'active' and n == 0,
        'reader_read1': formed and phase == 'read0' and n == 1,
        'reader_install': formed and phase == 'read1',
    }


def observation(state):
    review.check_state(state)
    types = list(review.base.counts(state['plant']))
    population = sum(types)
    occupation = review.occupied(state)
    return dict(state=deepcopy(state), type_counts=types,
                native_population=population, occupied_parts=occupation,
                precursor=78-occupation-population, energy=review.energy(state),
                propensities=rates(state), apparatus_guards=apparatus_guards(state))


def reconstruct_prefix(bindings, saved):
    word = review.base.preparation_word([ROOT / p for p in bindings])
    assert len(word) == 94
    start = review.fresh((0,0,0,0,0,360,230))
    run = review.Replay(start)
    for name in word:
        assert run.step('native', native_event=name, role='existing_ancestry')
    assert saved['ancestry'] == dict(initial=start, final=run.state,
                                    events=run.events,
                                    original_saved_history='histories.ancestor')
    for kind in ('assemble_cell', 'assemble_cell', 'assemble_reader'):
        run.step(kind)
    assembled = deepcopy(run.state)
    assert len(run.events) == 97
    assert assembled['plant'] == [35,36,1,1,1,290,216] and assembled['spent'] == 83
    run.step('native', native_event='leak_local', role='external_initial_loss')
    for port in (0,1):
        run.step('native', native_event='wear_a', role='external_training_wear')
        run.step('bind_contact', port=port)
        run.macro(port, 0, 'training', record=True)
        run.step('contact_latched')
        run.step('record_committed')
    run.step('reader_activate')
    run.step('reader_read', port=0)
    run.step('reader_read', port=1)
    run.step('reader_install')
    old = next(row for row in saved['cases'] if row['case'] == 'ordinary_w0')
    assert run.events[94:] == old['events'][:21]
    assert run.state == old['checkpoints']['reader_completed']
    assert assembled == old['checkpoints']['assembled']
    assert len(run.events) == 115
    return dict(initial=start, events=run.events,
                cuts=dict(assembled=dict(index=97, state=assembled),
                          installed=dict(index=115, state=deepcopy(run.state))))


def main():
    result_path = HERE / 'operative-results.json'
    data = json.loads(result_path.read_text())
    bindings = {path: sha(ROOT/path) for path in data['source_hashes']}
    assert bindings == data['source_hashes'] and len(bindings) == 20
    old = json.loads((HERE/'results.json').read_text())
    assert all(bindings[k] == v for k,v in old['source_hashes'].items())
    initial_result_sha = sha(result_path)
    prefix = reconstruct_prefix(bindings, old)
    assert prefix == data['prefix']
    expected = []
    for name, cut, word, endpoint, spent in CASES:
        run = review.Replay(prefix['cuts'][cut]['state'])
        frozen = apparatus(run.state)
        obs = [observation(run.state)]
        for event in word:
            assert run.step('native', native_event=event, role='operative_source_witness')
            assert apparatus(run.state) == frozen
            obs.append(observation(run.state))
        assert run.state['plant'] == endpoint and run.state['spent'] == spent
        expected.append(dict(case=name, cut=cut, word=list(word), events=run.events,
                             observations=obs, final=deepcopy(run.state)))
    assert expected == data['cases']
    counts = dict(cases=6, shared_prefix_events=115, suffix_native_events=449,
                  stored_event_occurrences=564)
    assert data['counts'] == counts
    assert sum(len(row['events']) for row in expected) == 449
    assert sum(len(row['observations']) for row in expected) == 455
    get_rate = lambda o, n: Q(o['propensities'].get(n, '0'))
    for row in expected[:2]:
        assert [o['precursor'] for o in row['observations']] == [0,1,0]
        assert [get_rate(o,'copy_a') for o in row['observations']] == [0,1,0]
    assert expected[0]['observations'][-1]['type_counts'] == [36,36]
    assert expected[1]['observations'][-1]['type_counts'] == [37,35]
    present = expected[2]['observations']
    depleted = expected[4]['observations']
    assert get_rate(present[-2], 'repair') == get_rate(depleted[-2], 'repair') == 290
    assert present[-2]['state']['plant'][:-1] == depleted[-2]['state']['plant'][:-1]
    assert get_rate(present[-1], 'capture') == 216
    assert get_rate(depleted[-1], 'capture') == 0
    assert [get_rate(o, 'capture') for o in expected[3]['observations']] == [0,216,0]
    assert all(not any(o['apparatus_guards'].values())
               for o in expected[-1]['observations'])
    for path,digest in bindings.items():
        assert sha(ROOT/path) == digest
    assert sha(result_path) == initial_result_sha
    report = dict(
        status='passed', scope='Six admitted native histories, rational propensities and guard inspection; no stochastic typicality or new law',
        producer_imported=False, native_process_imported=False,
        independent_helpers={str(p.relative_to(ROOT)): d for p,d in HELPERS.items()},
        source_hashes=bindings, producer_bound_files=20,
        unique_bound_inputs_including_helpers=len(set(bindings) | {str(p.relative_to(ROOT)) for p in HELPERS}),
        checker_sha256=sha(Path(__file__)), result_sha256=initial_result_sha,
        counts=counts, observation_tables=455, rational_propensity_tables=455,
        apparatus_guard_tables=455, declared_guards_per_table=11,
        global_material=78, occupied_apparatus_parts=6, effective_native_material=72,
        exact_energy_including_escrow=590,
        prefix_reuse='Reconstructs94nativeevents and21existing acquisition events with two bound independent helpers; does not run earlier20-case sweep',
        installed_closure_scope='Source/induction for successful admitted operations: structural guards exclude every apparatus change and native steps preserve apparatus; finite replay checks six installed states only',
        invalid_helpers_invoked=False,
        outputs=[dict(case=row['case'], final_plant=row['final']['plant'],
                      spent=row['final']['spent']) for row in expected],
    )
    (HERE/'operative-independent-check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items()
                      if k not in ('source_hashes','outputs')},indent=2))


if __name__ == '__main__':
    main()
