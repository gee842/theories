"""Audit phase carry, cash totals, bounds, and enacted rules without source edits."""
from fractions import Fraction as F
from pathlib import Path
from dataclasses import asdict
import importlib.util,sys,json,math,hashlib
folder=Path(__file__).parent
sys.path.insert(0,str(folder))
import repeated_revision as r
import revise_standard as m
saved=json.loads((folder/'repeated-revision-results.json').read_text())
assert saved['source_sha256']==hashlib.sha256((folder/'repeated_revision.py').read_bytes()).hexdigest()
current=m.Rule(); replay=[]
# Instrument deployed rule identities to verify actual use before and after decisions.
real_run=m.run_policy
calls=[]
def traced_run(rule,task,cfg,rng):
    calls.append(rule.require_improving_prefix)
    return real_run(rule,task,cfg,rng)
m.run_policy=traced_run
try:
    for phase,(profile,n,budget) in enumerate(r.SCHEDULE,1):
        entering=current.require_improving_prefix
        calls.clear()
        current,observed=r.phase_run(current,profile,n,budget,phase)
        assert observed==saved['records'][phase-1]
        expected_pairs=observed['discovery_pairs']+observed.get('fresh_outer_check',{}).get('pairs',0)
        assert calls[:2*expected_pairs]==[entering,not entering]*expected_pairs
        assert calls[2*expected_pairs:]==[current.require_improving_prefix]*r.POST_TASKS
        assert observed['initial_rule']['require_improving_prefix']==entering
        assert observed['post_decision_execution']['actual_rule']==asdict(current)
        # Reconstruct cash from independently aggregated record parts.
        cash=sum(F(observed[key][arm]['expense']['exact']) for key in ('discovery','checking') for arm in ('incumbent','edited'))+F(observed['post_decision_execution']['expense']['exact'])
        assert cash==F(observed['expense']['exact'])
        reserve=F(1003,50)*(2*(128+n)+32)
        assert reserve==F(observed['required_worst_case_reserve_including_post_tasks']['exact'])
        radius=float(F(7531,100))*math.sqrt(2*math.log(60)/n)
        assert abs(radius-observed['fresh_outer_check']['one_sided_Hoeffding_radius'])<1e-12
        replay.append({'phase':phase,'exact_replay':True,'current_rule_carried_and_enacted':True,'paired_protocol_identity_trace_checked':True,'cash_ledger_exact':str(cash),'reserve_exact':str(reserve),'confidence_radius':radius})
finally:
    m.run_policy=real_run
assert asdict(current)==saved['final_rule']
assert sum(F(x['expense']['exact']) for x in saved['records'])==F(6403151,25)
# Verify no outcomes can be acquired by an underfunded phase.
real_observe=m.observe
observations=[]
def counted_observe(task,indices,rng):
    observations.append(1)
    return real_observe(task,indices,rng)
m.observe=counted_observe
try:
    unchanged,empty=r.phase_run(m.Rule(),'interaction',256,F(0),1)
    assert empty['status']=='unfunded' and not observations and unchanged==m.Rule()
finally:
    m.observe=real_observe
out={'phase_audits':replay,'underfunded_phase_observe_calls':len(observations),'conditional_union_bound_alpha_exact':'1/60 + 1/60 + 1/60 = 1/20','total_expense_exact':'6403151/25','interpretation':'Three scheduled conditional checks only; no drift-detection or universal norm-generation guarantee.'}
(folder/'repeated-revision-audit-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
