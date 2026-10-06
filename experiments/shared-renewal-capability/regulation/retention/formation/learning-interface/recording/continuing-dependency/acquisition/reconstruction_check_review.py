"""Independent reconstruction of native template-retention continuations.

Only bound independent interpreters/rate formulas are imported. No acquisition,
operative or reconstruction producer, or native process module, is imported.
The four words and endpoints are fixed independently from the protocol. Earlier
scientific sweeps are not rerun. Exact local race and projection checks follow
from the complete independently derived native relation and rational rates.
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
ROOT = next(p for p in HERE.parents if (p/'AGENTS.md').exists())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
HELPERS = {
    HERE/'operative_check_review.py':
        'bbe629da4557a86523153d9f082a8850d118d4fbef21a4fd2dde9f1e98c23703',
    HERE/'independent_check.py':
        'fc66a8377d36fb66a5f07370ac004ff3394bab8d79499444cb6c8ebb991c4aa9',
    HERE.parent/'independent_check.py':
        'c9ff5611ac3248b02db951bb2edcf7bf23e77d559f6e7da438c67047791a9250',
}
for path,digest in HELPERS.items():
    assert sha(path) == digest
spec = importlib.util.spec_from_file_location('_reviewed_operative_independent',
                                              HERE/'operative_check_review.py')
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)
review = prior.review
CASES = (
    ('copy_then_a', True, 'a', [35,36,1,1,0,279,213],98),
    ('copy_then_h', True, 'h', [35,36,2,0,0,280,213],97),
    ('loss_then_a', False, 'a', [34,36,1,1,0,279,213],98),
    ('loss_then_h', False, 'h', [34,36,2,0,0,280,213],97),
)


def formation_distribution(state):
    rates = {k:Q(v) for k,v in prior.rates(state).items()}
    a,h,r,c,local,f,e = state['plant']
    assert r == 0 and c == 1 and local == 0 and f > 0
    n = a+h
    precursor = 78-review.occupied(state)-n
    direct_total = Q(f*n+e) + Q(f*n*precursor+n+1+f,1000000)
    assert sum(rates.values(),Q(0)) == direct_total
    assert rates['bind_a'] == a*f and rates['bind_h'] == h*f
    return dict(bind_a_rate=str(Q(a*f)), bind_h_rate=str(Q(h*f)),
                exit_rate=str(direct_total),
                conditional_a_given_next_event_association=str(Q(a,n)),
                next_event_a_probability=str(Q(a*f)/direct_total),
                next_event_h_probability=str(Q(h*f)/direct_total))


def project(state):
    p = state['plant']
    return dict(type_counts=list(review.base.counts(p)), intact=p[3], local=p[4],
                common=p[5], source=p[6], spent=state['spent'],
                native_capacity=78-review.occupied(state),
                apparatus=prior.apparatus(state))


def rate_to_projected_class(state, target):
    rates = {name:Q(value) for name,value in prior.rates(state).items()}
    total = Q(0)
    contributors = []
    for name,plant in review.base.successors(78-review.occupied(state),
                                             tuple(state['plant'])):
        successor = deepcopy(state)
        successor['plant'] = list(plant)
        successor['spent'] += review.base.energy(state['plant'])-review.base.energy(plant)
        review.check_state(successor)
        if project(successor) == target:
            total += rates[name]
            contributors.append(name)
    return total,contributors


def main():
    path = HERE/'reconstruction-results.json'
    data = json.loads(path.read_text())
    result_sha = sha(path)
    bindings = {p:sha(ROOT/p) for p in data['source_hashes']}
    assert bindings == data['source_hashes'] and len(bindings) == 25
    older = json.loads((HERE/'operative-results.json').read_text())
    assert all(bindings[p] == digest for p,digest in older['source_hashes'].items())
    saved_acquisition = json.loads((HERE/'results.json').read_text())
    prefix = prior.reconstruct_prefix(bindings, saved_acquisition)
    assert prefix == data['prefix'] == older['prefix']
    inherited = prefix['cuts']['installed']['state']
    expected=[]
    for name,retained,kind,endpoint,spent in CASES:
        word = ['wear_a','capture', 'copy_a' if retained else 'leak_local',
                'wear_res_a',f'bind_{kind}','capture',f'copy_{kind}','damage','repair']
        run = review.Replay(inherited)
        original_apparatus = prior.apparatus(run.state)
        observations = [prior.observation(run.state)]
        for i,native in enumerate(word):
            enabled = run.step('native', native_event=native,
                               role='native_carrier_reconstruction')
            assert enabled == (kind == 'a' or i < 8)
            assert prior.apparatus(run.state) == original_apparatus
            assert not any(prior.apparatus_guards(run.state).values())
            observations.append(prior.observation(run.state))
        assert run.state['plant'] == endpoint and run.state['spent'] == spent
        fork = observations[4]['state']
        expected.append(dict(case=name,retained_copy=retained,chosen_resident=kind,
                             requests=word,events=run.events,observations=observations,
                             association_fork=deepcopy(fork),
                             formation_distribution=formation_distribution(fork),
                             final=deepcopy(run.state)))
    assert expected == data['cases']
    counts = dict(cases=4,shared_prefix_events=115,suffix_records=36,
                  suffix_native_events=34,suffix_unavailable_requests=2,
                  stored_event_occurrences=151)
    assert counts == data['counts']
    assert sum(e['event']=='native' for r in expected for e in r['events']) == 34
    assert sum(e['event']=='native_unavailable' for r in expected for e in r['events']) == 2
    copied,lost = expected[0]['formation_distribution'],expected[2]['formation_distribution']
    cond = Q(copied['conditional_a_given_next_event_association'])-Q(lost['conditional_a_given_next_event_association'])
    assert cond == Q(18,2485) == Q(36,70*71)
    whole = Q(copied['next_event_a_probability'])-Q(lost['next_event_a_probability'])
    assert whole == Q(4123474980687500,569548386526593617) > 0
    assert str(cond) == data['conditional_association_difference']
    assert str(whole) == data['next_event_a_probability_difference']
    assert Q(copied['exit_rate']) == Q(1260313769,62500)
    assert Q(lost['exit_rate']) == Q(4971009923,250000)
    pairs=[]
    for arow,hrow in (expected[:2],expected[2:]):
        astate = arow['observations'][6]['state']
        hstate = hrow['observations'][6]['state']
        assert project(astate) == project(hstate)
        assert astate['plant'][2] == 1 and hstate['plant'][2] == 2
        target = project(arow['observations'][7]['state'])
        a_rate,a_names = rate_to_projected_class(astate,target)
        h_rate,h_names = rate_to_projected_class(hstate,target)
        assert a_names == ['copy_a'] and h_names == []
        assert a_rate == (1 if arow['retained_copy'] else 2) and h_rate == 0
        pairs.append(dict(retained_copy=arow['retained_copy'],
                          shared_projected_source=project(astate),
                          a_copy_projected_target=target,
                          rate_from_a_resident=str(a_rate),rate_from_h_resident=str(h_rate)))
    assert pairs == data['insufficient_projection_pairs']
    assert data['unchanged_learned_apparatus'] is True
    for p,digest in bindings.items():
        assert sha(ROOT/p) == digest
    for p,digest in HELPERS.items():
        assert sha(p) == digest
    assert sha(path) == result_sha
    report = dict(
        status='passed',scope='Four fixed native continuations; exact immediate formation probabilities and failure of the specified strong Markov projection',
        producer_imported=False,native_process_imported=False,
        independent_helpers={str(p.relative_to(ROOT)):d for p,d in HELPERS.items()},
        source_hashes=bindings,producer_bound_files=25,
        unique_bound_inputs_including_helpers=len(set(bindings)|{str(p.relative_to(ROOT)) for p in HELPERS}),
        checker_sha256=sha(Path(__file__)),result_sha256=result_sha,counts=counts,
        full_state_observation_tables=40,complete_rational_rate_tables=40,
        apparatus_guard_tables=40,guards_per_table=11,
        conserved_original_energy_including_spent=590,global_material=78,
        occupied_apparatus_parts=6,effective_native_material=72,
        conditional_association_difference=str(cond),
        next_event_a_probability_difference=str(whole),
        projection_pairs=2,projected_class_rates=[['1','0'],['2','0']],
        projection_scope='Unequal total instantaneous rates to the same projected target at two reached full states with identical projection; no claim against history-conditioned or weak distribution-specific abstractions',
        learned_apparatus_unchanged=True,
        denied_repair_scope='Immediate request with H resident; not permanent inability to reorganize and repair',
        no_prior_sweep_rerun=True,
    )
    (HERE/'reconstruction-independent-check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='source_hashes'},indent=2))


if __name__ == '__main__':
    main()
