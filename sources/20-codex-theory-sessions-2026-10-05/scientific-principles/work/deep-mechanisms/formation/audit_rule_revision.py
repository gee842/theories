"""Independent arithmetic, replay, budget boundary, and data-interface audit."""
from fractions import Fraction as F
import importlib.util
from pathlib import Path
import json, sys, math

folder=Path(__file__).parent
spec=importlib.util.spec_from_file_location('formation_rule_revision_audit_target', folder/'revise_standard.py')
m=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=m
spec.loader.exec_module(m)
record=json.loads((folder/'standard-revision-results.json').read_text())
cfg=m.Config()
old_price=F(8)+3*F(1,4)
new_price=F(16)+6*F(1,4)+2*64*F(1,50)
expected_gain=64*F(1,2)+old_price-new_price
expected_spending=(old_price+new_price)*(32+256)
independent_bound=F(64)+new_price-old_price
reserve=2*(32+256)*new_price
radius=2*float(independent_bound)*math.sqrt(math.log(20)/(2*256))
assert expected_gain==F(2069,100)
assert expected_spending==F(207432,25)
assert independent_bound==F(7531,100)
assert reserve==F(288864,25)
first=record['records'][0]
assert F(first['spent']['exact'])==expected_spending
assert F(first['fresh_outer_check']['mean_observed_gain']['exact'])==expected_gain
assert abs(first['fresh_outer_check']['one_sided_Hoeffding_radius']-radius)<1e-12
replays=[]
for index,saved in enumerate(record['records']):
    thiscfg=m.replace(cfg,field_cost=F(3,10)) if index==8 else (m.replace(cfg,checking_pairs=1024) if index==9 else cfg)
    observed=m.run_study(saved['profile'],saved['opening'],F(saved['starting_budget']['exact']),saved['seed'],thiscfg)
    assert observed==saved, (index,'seeded result did not replay')
    replays.append({'record':index,'status':observed['status'],'exact_replay_matches':True})
# Count acquired labels: outer task outcomes are not shared for free between arms.
orig_observe=m.observe
calls=[]
def counted_observe(task, indices, rng):
    indices=tuple(indices)
    calls.append(len(indices))
    return orig_observe(task,indices,rng)
m.observe=counted_observe
try:
    pure=m.run_study('interaction','protected_probe',F(12000),20261005,cfg)
    expected_counts={'eight_label_calls':3*(32+256),'deployment_calls':2*(32+256)}
    assert calls.count(8)==expected_counts['eight_label_calls']
    assert calls.count(64)==expected_counts['deployment_calls']
    assert len(calls)==sum(expected_counts.values())
    calls.clear()
    unfunded=m.run_study('interaction','incumbent_gate',F(0),20261005,cfg)
    underfunded_observations=len(calls)
    assert underfunded_observations==0, 'Underfunded pilot acquired evidence before payment check.'
finally:
    m.observe=orig_observe

# Exact relay proposed independently in the architecture memo.
def relay(capacity,funding):
    return int((capacity==1 and funding>=1) or (capacity==0 and funding>=3))
state=1
states=[state]
for funding in (0,2,3,2):
    state=relay(state,funding)
    states.append(state)
assert states==[1,0,0,1,1]
assert relay(1,2)==1 and relay(0,2)==0
service=first['study_service_accounting']
assert F(service['total_observed_loss_including_priced_expense']['exact'])==F(437832,25)
assert F(service['matched_two_incumbent_streams_loss_estimate']['exact'])==F(23472)
assert F(service['incremental_observed_loss_estimate']['exact'])==F(-148968,25)
transfer=json.loads((folder/'standard-transfer-results.json').read_text())
assert m.run_transfer(first['final_rule'],cfg)==transfer
exact=json.loads((folder/'exact-transfer-results.json').read_text())
prior=json.loads(Path('work/formation/generation-results.json').read_text())['results']
for profile,eps in [('interaction','0'),('null','1/2'),('noisy_interaction','1/4')]:
    values=[]
    for proc in ('greedy','compositional'):
        row=next(r for r in prior if r['noise']['exact']==eps and r['procedure']==proc)
        values.append(F(32)+F(row['expected_inquiry_cost']['exact'])-64*F(row['expected_net_gain_per_future_decision']['exact']))
    target=next(r for r in exact['rows'] if r['profile']==profile)
    assert values[0]-values[1]==F(target['true_expected_gain']['exact'])
assert F(next(r for r in exact['rows'] if r['profile']=='mixed')['true_expected_gain']['exact'])==(F(2069,100)+F(-38401,12800))/2
result={'exact_transfer_matches_prior_independent_enumeration':True,'transfer_seeded_replay_matches':True,'matched_service_arithmetic_checked':True,'independent_arithmetic':{'deterministic_gain':str(expected_gain),'study_expense':str(expected_spending),'difference_bound':str(independent_bound),'reserve':str(reserve),'Hoeffding_radius':radius},'seeded_replays':replays,'outcome_acquisition_counts':expected_counts,'underfunded_pilot':{'status':unfunded['status'],'observe_calls':underfunded_observations,'observed_before_payment_check':underfunded_observations>0},'relay_check':{'maintenance':1,'reconstruction':3,'initial_capacity':1,'funding_sequence':[0,2,3,2],'capacity_states':states}}
(folder/'rule-revision-audit-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
