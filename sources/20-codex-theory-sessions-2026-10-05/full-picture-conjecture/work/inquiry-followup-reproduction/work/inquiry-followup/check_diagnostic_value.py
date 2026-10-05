"""Exploratory follow-up, separate from the frozen four-round access study."""
from pathlib import Path
import sys,json,hashlib
from fractions import Fraction as Q
from dataclasses import replace
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'work/access-study'))
from model import Config,Engine,State
import audit_oracle as oracle
weights=(20,1,10,0)
s=State(1,1,6,0,1,Q(1,2),-1)

def evaluate(engine,action):
    v=list(action.stage)
    for br in action.branches:
        terminal=engine.terminal(br.child)
        for j,value in enumerate(terminal):v[j]+=br.probability*value
    return tuple(v)

rows=[]
for label,cfg in [('informative',Config()),('uninformative',replace(Config(),sensitivity=Q(1,2),specificity=Q(1,2)))]:
    e=Engine(cfg);ss=e.normalize(s)
    chosen=next(a for a in e.actions(ss) if a.test and dict(a.repair_rule)=={'positive':1,'negative':0})
    v=evaluate(e,chosen)
    rows.append({'sensor':label,'F_E_B_U':list(map(str,v[:4])),'expected_tests':str(v[4]),'expected_repairs':str(v[5]),'optimal_weighted_policy':e.result(ss,weights)})
assert rows[0]['F_E_B_U']==['17/200','9/2','1/10','27/200']
assert rows[1]['F_E_B_U']==['9/40','9/2','3/10','11/40']
assert all(row['expected_repairs']=='1/2' for row in rows)
# No-test policies can only repair with a probability q independent of fault.
q=Q(1,5)
assert Q(1,2)*q==Q(1,10)
assert Q(9,20)*(1-q)==Q(9,25)
# Check all eight original-technology action vectors against separate latent oracle.
os=oracle.State(1,1,6,0,1,Q(1,2),-1)
eng=Engine();actual=[]
for a in eng.actions(eng.normalize(s)):
    v=evaluate(eng,a)
    oa=oracle.Choice(a.support,a.test,a.repair_rule)
    tr=oracle.transition(os,oa,'barred')
    ov=(sum(pr*Q(child.x==0) for _,pr,child in tr['branches']),tr['expense'],tr['burden'],sum(pr*Q(child.x<2) for _,pr,child in tr['branches']))
    assert tuple(v[:4])==ov
    actual.append({'support':a.support,'test':a.test,'repair_rule':dict(a.repair_rule),'F_E_B_U':list(map(str,v[:4])),'score':str(eng.score(v,weights))})
result={'status':'passed','study_type':'exploratory post-main counterexample; changed start, horizon and evaluation; original physical dynamics/prices unchanged',
        'state':{'horizon':1,'stock':1,'cash':6,'treasury':0,'ready':1,'fault_prior':'1/2','access':'barred'},
        'burden_definition':'expected absent-target repairs plus 1/20 per test; not total harm',
        'sensors_same_test_then_repair_positive_rule':rows,'all_eight_original_sensor_actions':actual,
        'constrained_no_test_bound':{'expected_expense_cap':'9/2','burden_cap':'1/10','initial_cash':6,'maximum_repair_probability':'1/5','minimum_failure':'9/25','expense_at_bound':'3/5','randomized_policies_allowed':True},
        'weighted_objective':{'weights_F_E_B_U':list(weights),'meaning':'illustrative tradeoff, not a normative recommendation','informative_optimum':'36/5','best_no_test':'8','uninformative_optimum':'8'},
        'independent_latent_oracle_actions_matched':len(actual),
        'model_sha256':hashlib.sha256((ROOT/'work/access-study/model.py').read_bytes()).hexdigest()}
out=ROOT/'outputs/diagnostic-value-check.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'sensors':[{'sensor':r['sensor'],'F_E_B_U':r['F_E_B_U']} for r in rows],'file':str(out)},indent=2))
