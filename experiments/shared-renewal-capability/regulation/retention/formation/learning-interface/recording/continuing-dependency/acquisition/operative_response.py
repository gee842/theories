"""Source-derived native response witnesses; no new controller or event law."""
from copy import deepcopy
from fractions import Fraction
from pathlib import Path
import importlib.util
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('_operative_acquisition', HERE/'model.py')
acq = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = acq
spec.loader.exec_module(acq)

APPARATUS = ('cells', 'cell_count', 'reader', 'pending', 'escrow',
             'reader_phase', 'read_values', 'selected')


def apparatus(s):
    return {k: deepcopy(s[k]) for k in APPARATUS}


def guards(s):
    """Eligibility of apparatus-changing admitted operations, not failed calls.

    Unrecorded physical macros are native words and preserve apparatus. A
    recorded macro's completion requires a bound contact; phase/contact
    requirements below are the stable blockers at the installed checkpoint.
    """
    a, h, _, _, _, f, _ = s['plant']
    pending = s['pending']
    assembly = min(a, h, f) >= 1 and pending is None
    reading = s['reader'] and pending is None and f >= 1
    phase = s['reader_phase']
    return {
        'assemble_cell': assembly and s['cell_count'] < 2,
        'assemble_reader': assembly and not s['reader'],
        'bind_contact0': pending is None and s['cell_count'] > 0
                         and s['cells'][0] is None and f >= 2,
        'bind_contact1': pending is None and s['cell_count'] > 1
                         and s['cells'][1] is None and f >= 2,
        'recorded_macro_completion': pending is not None
                                     and pending['stage'] == 'bound',
        'contact_latched_or_lost': pending is not None
                                   and pending['stage'] == 'completed',
        'record_committed': pending is not None and pending['stage'] == 'latched'
                            and s['escrow'] == 1,
        'reader_activate': reading and phase == 'cold',
        'reader_read0': reading and phase == 'active' and len(s['read_values']) == 0,
        'reader_read1': reading and phase == 'read0' and len(s['read_values']) == 1,
        'reader_install': reading and phase == 'read1',
    }


def observe(s):
    acq.valid(s)
    pop = list(acq.native.counts(s['plant']))
    return dict(state=deepcopy(s), type_counts=pop,
                native_population=sum(pop), occupied_parts=acq.occupied(s),
                precursor=acq.capacity(s)-sum(pop), energy=acq.energy(s),
                propensities={e: str(q) for e, _, q in acq.native.channels(
                    acq.native.Law(material=acq.capacity(s)), tuple(s['plant']))},
                apparatus_guards=guards(s))


def rate(observation, name):
    return Fraction(observation['propensities'].get(name, '0'))


def prefix(previous):
    saved = next(c for c in previous['cases'] if c['case'] == 'ordinary_w0')
    s = deepcopy(previous['ancestry']['initial'])
    trace = []
    for e in previous['ancestry']['events']:
        assert acq.native_step(s, e['detail']['native_event'], trace,
                               role='existing_ancestry')
    assert trace == previous['ancestry']['events'] and len(trace) == 94
    for kind in ('cell', 'cell', 'reader'):
        acq.assemble(s, kind, trace)
    assembled = deepcopy(s)
    assert assembled == saved['checkpoints']['assembled']
    assert acq.native_step(s, 'leak_local', trace, role='external_initial_loss')
    for port in (0, 1):
        assert acq.native_step(s, 'wear_a', trace, role='external_training_wear')
        acq.bind(s, port, trace)
        assert acq.physical_macro(s, port, 0, trace, role='training', record=True)
        assert acq.contact(s, 'ordinary', trace)
        assert acq.commit(s, 'ordinary', trace)
    acq.reader_operation(s, 'reader_activate', trace)
    acq.reader_operation(s, 'reader_read', trace, port=0)
    acq.reader_operation(s, 'reader_read', trace, port=1)
    acq.reader_operation(s, 'reader_install', trace)
    assert s == saved['checkpoints']['reader_completed']
    assert trace[94:] == saved['events'][:21] and len(trace) == 115
    return dict(initial=deepcopy(previous['ancestry']['initial']), events=trace,
                cuts=dict(assembled=dict(index=97, state=assembled),
                          installed=dict(index=115, state=deepcopy(s))))


def run_case(name, cut, word, inherited):
    s = deepcopy(inherited)
    trace, observations = [], [observe(s)]
    fixed = apparatus(s)
    for event in word:
        assert acq.native_step(s, event, trace, role='operative_source_witness')
        assert apparatus(s) == fixed
        observations.append(observe(s))
    return dict(case=name, cut=cut, word=word, events=trace,
                observations=observations, final=deepcopy(s))


def main():
    old = json.loads((HERE/'results.json').read_text())
    for name, digest in old['source_hashes'].items():
        assert acq.sha(acq.ROOT/name) == digest
    ancestry = prefix(old)
    specifications = [
        ('a_vacancy', 'assembled', ['wear_a', 'copy_a']),
        ('h_vacancy', 'assembled', ['wear_h', 'copy_a']),
        ('source_present_repair', 'assembled', ['leak_local', 'damage', 'repair']),
        ('store_response', 'assembled', ['leak_local', 'capture']),
        ('source_depleted_repair', 'assembled',
         ['leak_local'] + ['capture', 'leak_local']*216 + ['damage', 'repair']),
        ('installed_continuation', 'installed',
         ['capture', 'wear_h', 'copy_a', 'damage', 'repair']),
    ]
    rows = [run_case(n, c, w, ancestry['cuts'][c]['state'])
            for n, c, w in specifications]
    endpoints = [([35,36,1,1,0,290,216],84), ([36,35,1,1,0,290,216],84),
                 ([35,36,1,1,0,289,216],85), ([35,36,1,1,1,290,215],84),
                 ([35,36,1,1,0,289,0],301), ([36,35,1,1,0,280,214],96)]
    for row, (plant, spent) in zip(rows, endpoints):
        assert row['final']['plant'] == plant and row['final']['spent'] == spent
    for row in rows[:2]:
        obs = row['observations']
        assert [o['precursor'] for o in obs] == [0,1,0]
        assert [rate(o, 'copy_a') for o in obs] == [0,1,0]
    assert rows[0]['observations'][-1]['type_counts'] == [36,36]
    assert rows[1]['observations'][-1]['type_counts'] == [37,35]
    present, depleted = rows[2]['observations'], rows[4]['observations']
    assert rate(present[-2], 'repair') == rate(depleted[-2], 'repair') == 290
    assert present[-2]['state']['plant'][:-1] == depleted[-2]['state']['plant'][:-1]
    assert rate(present[-1], 'capture') == 216
    assert rate(depleted[-1], 'capture') == 0
    assert [rate(o, 'capture') for o in rows[3]['observations']] == [0,216,0]
    assert all(not any(o['apparatus_guards'].values())
               for o in rows[5]['observations'])
    paths = [Path(__file__), HERE/'OPERATIVE-PROTOCOL.md', HERE/'results.json',
             HERE/'independent-check.json', HERE/'independent_check.py']
    bindings = dict(old['source_hashes'])
    bindings.update({str(p.relative_to(acq.ROOT)): acq.sha(p) for p in paths})
    counts = dict(cases=len(rows), shared_prefix_events=len(ancestry['events']),
                  suffix_native_events=sum(len(r['events']) for r in rows))
    assert counts == dict(cases=6, shared_prefix_events=115, suffix_native_events=449)
    counts['stored_event_occurrences'] = counts['shared_prefix_events']+counts['suffix_native_events']
    result = dict(scope='Six possible native continuations; source-derived response and apparatus scope',
                  source_hashes=bindings, counts=counts, prefix=ancestry, cases=rows,
                  universal_apparatus_closure='Source/induction argument in accompanying review; traces alone are finite witnesses')
    (HERE/'operative-results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(counts=counts, endpoints=[dict(case=r['case'], plant=r['final']['plant'],
                     spent=r['final']['spent']) for r in rows]), indent=2))


if __name__ == '__main__':
    main()
