"""Unchanged native reactions: retained templates alter carrier reconstruction."""
from copy import deepcopy
from fractions import Fraction as Q
from pathlib import Path
import importlib.util
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('_native_operative_witness',
                                              HERE/'operative_response.py')
operative = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = operative
spec.loader.exec_module(operative)
acq = operative.acq


def distribution(state):
    rates = {name: q for name, _, q in acq.native.channels(
        acq.native.Law(material=acq.capacity(state)), tuple(state['plant']))}
    qa, qh = rates.get('bind_a', Q(0)), rates.get('bind_h', Q(0))
    total = sum(rates.values(), Q(0))
    assert total > 0 and qa+qh > 0
    return dict(bind_a_rate=str(qa), bind_h_rate=str(qh), exit_rate=str(total),
                conditional_a_given_next_event_association=str(qa/(qa+qh)),
                next_event_a_probability=str(qa/total),
                next_event_h_probability=str(qh/total))


def project(state):
    """Omit only template placement, retaining totals, accounts and apparatus."""
    _, _, _, intact, local, common, source = state['plant']
    return dict(type_counts=list(acq.native.counts(state['plant'])), intact=intact,
                local=local, common=common, source=source, spent=state['spent'],
                native_capacity=acq.capacity(state), apparatus=operative.apparatus(state))


def projected_rate_to(state, target):
    answer = Q(0)
    for _, plant, rate in acq.native.channels(
            acq.native.Law(material=acq.capacity(state)), tuple(state['plant'])):
        successor = deepcopy(state)
        successor['plant'] = list(plant)
        successor['spent'] += acq.native.fuel(state['plant'])-acq.native.fuel(plant)
        acq.valid(successor)
        if project(successor) == target:
            answer += rate
    return answer


def run_case(inherited, retained, kind):
    state = deepcopy(inherited)
    records = []
    observations = [operative.observe(state)]
    word = ['wear_a', 'capture', 'copy_a' if retained else 'leak_local',
            'wear_res_a', 'bind_'+kind, 'capture', 'copy_'+kind, 'damage', 'repair']
    for index, event in enumerate(word):
        admitted = acq.native_step(state, event, records, role='native_carrier_reconstruction')
        assert admitted == (kind == 'a' or index != 8)
        assert operative.apparatus(state) == operative.apparatus(inherited)
        observations.append(operative.observe(state))
    fork = observations[4]['state']
    return dict(case=('copy' if retained else 'loss')+'_then_'+kind,
                retained_copy=retained, chosen_resident=kind, requests=word,
                events=records, observations=observations,
                association_fork=deepcopy(fork), formation_distribution=distribution(fork),
                final=deepcopy(state))


def main():
    previous = json.loads((HERE/'results.json').read_text())
    recent = json.loads((HERE/'operative-results.json').read_text())
    for path, digest in recent['source_hashes'].items():
        assert acq.sha(acq.ROOT/path) == digest
    ancestry = operative.prefix(previous)
    assert ancestry == recent['prefix']
    installed = ancestry['cuts']['installed']['state']
    rows = [run_case(installed, retained, kind)
            for retained in (True, False) for kind in ('a', 'h')]
    expected = [([35,36,1,1,0,279,213],98), ([35,36,2,0,0,280,213],97),
                ([34,36,1,1,0,279,213],98), ([34,36,2,0,0,280,213],97)]
    for row, (plant, spent) in zip(rows, expected):
        assert row['final']['plant'] == plant and row['final']['spent'] == spent
    copy_fork, loss_fork = rows[0]['association_fork'], rows[2]['association_fork']
    assert copy_fork['plant'] == [35,36,0,1,0,281,214]
    assert loss_fork['plant'] == [34,36,0,1,0,281,214]
    assert copy_fork['spent'] == loss_fork['spent'] == 95
    copied, lost = rows[0]['formation_distribution'], rows[2]['formation_distribution']
    conditional_difference = Q(copied['conditional_a_given_next_event_association'])-Q(lost['conditional_a_given_next_event_association'])
    assert conditional_difference == Q(18,2485) == Q(36,70*71)
    next_difference = Q(copied['next_event_a_probability'])-Q(lost['next_event_a_probability'])
    assert next_difference > 0
    pairs = []
    for arow, hrow in (rows[:2], rows[2:]):
        astate, hstate = arow['observations'][6]['state'], hrow['observations'][6]['state']
        assert project(astate) == project(hstate) and astate['plant'][2] != hstate['plant'][2]
        target = project(arow['observations'][7]['state'])
        qa, qh = projected_rate_to(astate, target), projected_rate_to(hstate, target)
        assert qa == (1 if arow['retained_copy'] else 2) and qh == 0
        pairs.append(dict(retained_copy=arow['retained_copy'],
                          shared_projected_source=project(astate),
                          a_copy_projected_target=target,
                          rate_from_a_resident=str(qa), rate_from_h_resident=str(qh)))
    paths = [Path(__file__), HERE/'RECONSTRUCTION-PROTOCOL.md',
             HERE/'operative-results.json', HERE/'operative-independent-check.json',
             HERE/'operative_check_review.py']
    bindings = dict(recent['source_hashes'])
    bindings.update({str(p.relative_to(acq.ROOT)): acq.sha(p) for p in paths})
    counts = dict(cases=len(rows), shared_prefix_events=len(ancestry['events']),
                  suffix_records=sum(len(r['events']) for r in rows),
                  suffix_native_events=sum(e['event']=='native' for r in rows for e in r['events']),
                  suffix_unavailable_requests=sum(e['event']=='native_unavailable' for r in rows for e in r['events']))
    assert counts == dict(cases=4, shared_prefix_events=115, suffix_records=36,
                          suffix_native_events=34, suffix_unavailable_requests=2)
    counts['stored_event_occurrences'] = counts['shared_prefix_events']+counts['suffix_records']
    result = dict(scope='Native template retention changes association probabilities; four possible formed-carrier continuations',
                  source_hashes=bindings, counts=counts, prefix=ancestry, cases=rows,
                  conditional_association_difference=str(conditional_difference),
                  next_event_a_probability_difference=str(next_difference),
                  insufficient_projection_pairs=pairs,
                  unchanged_learned_apparatus=True,
                  general_proof_scope='Hand algebra and source argument; finite replay is not a new Lean theorem')
    (HERE/'reconstruction-results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(counts=counts, conditional_difference=str(conditional_difference),
                         next_event_a_difference=str(next_difference),
                         forks=dict(copy=copied, loss=lost),
                         projection_rate_pairs=[(p['rate_from_a_resident'],p['rate_from_h_resident']) for p in pairs]),indent=2))


if __name__ == '__main__':
    main()
