"""Exploratory diagnostic witness, independently enumerated after main study.

Changes: H1, ready equipment, accessible cash6, prior1/2, and a new scalar
probe or expected expense/burden constraints. Base technology/costs unchanged.
Only writes within followup-audit/. Does not alter frozen results or inputs.
"""
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
from hashlib import sha256
import json

HERE=Path(__file__).resolve().parent
PARENT=HERE.parent
sys.path.insert(0,str(PARENT))
import audit_oracle as oracle

protected=[PARENT/'model.py',PARENT/'PROTOCOL.md',PARENT/'results/main.json']
before={str(p.name):sha256(p.read_bytes()).hexdigest() for p in protected}
s=oracle.State(1,1,6,0,1,Q(1,2))
rows=[]
for i,a in enumerate(oracle.choices(s,'barred')):
    tr=oracle.transition(s,a,'barred')
    v=[Q(0),tr['expense'],tr['burden'],Q(0)]
    for _,pr,ch in tr['branches']:
        v[0]+=pr*(ch.x==0);v[3]+=pr*(ch.x<2)
    rows.append({'id':i,'action':a,'vector':tuple(v),
                 'score':20*v[0]+v[1]+10*v[2]})
assert len(rows)==8
best=min(rows,key=lambda r:r['score'])
assert best['action'].test and dict(best['action'].repair_rule)=={'positive':1,'negative':0}
assert best['vector']==(Q(17,200),Q(9,2),Q(1,10),Q(27,200))
assert best['score']==Q(36,5)
assert sum(r['score']==best['score'] for r in rows)==1

def linear_solve(A,b):
    aug=[list(row)+[rhs] for row,rhs in zip(A,b)]
    n=len(b)
    for col in range(n):
        piv=next((j for j in range(col,n) if aug[j][col]),None)
        if piv is None:return None
        aug[col],aug[piv]=aug[piv],aug[col]
        scale=aug[col][col];aug[col]=[x/scale for x in aug[col]]
        for j in range(n):
            if j!=col:
                scale=aug[j][col]
                aug[j]=[x-scale*y for x,y in zip(aug[j],aug[col])]
    return tuple(row[-1] for row in aug)

def exact_constrained_lp(allowed):
    """Enumerate vertices: ≤3 positive weights for normalization +2 caps."""
    candidates=[]
    for k in (1,2,3):
        for subset in combinations(allowed,k):
            for active in combinations((1,2),k-1):
                A=[[Q(1)]*k]+[[r['vector'][j] for r in subset] for j in active]
                b=[Q(1)]+[{1:Q(9,2),2:Q(1,10)}[j] for j in active]
                weights=linear_solve(A,b)
                if weights is None or any(w<0 for w in weights):continue
                v=tuple(sum(w*r['vector'][j] for w,r in zip(weights,subset)) for j in range(4))
                if v[1]>Q(9,2) or v[2]>Q(1,10):continue
                candidates.append((v[0],v,tuple((r['id'],w) for r,w in zip(subset,weights))))
    return min(candidates,key=lambda x:x[0])

all_best=exact_constrained_lp(rows)
no_test_best=exact_constrained_lp([r for r in rows if not r['action'].test])
assert all_best[0]==Q(17,200)
assert no_test_best[0]==Q(9,25)

registered={
    'failure':(1,0,0,0),'recovery':(0,0,0,1),'expense':(0,1,0,0),
    'burden':(0,0,1,0),'failure_expense':(12,1,0,0),
    'failure_expense_burden':(12,1,4,0),'mixed':(4,1,1,4)}
registered_rows={}
for name,w in registered.items():
    chosen=min(rows,key=lambda r:(sum(x*y for x,y in zip(w,r['vector'])),
                                  r['vector'][1],r['vector'][2],r['vector'][3],
                                  r['vector'][0],r['action'].test,r['id']))
    assert not chosen['action'].test
    registered_rows[name]={'action_id':chosen['id'],'score':str(sum(x*y for x,y in zip(w,chosen['vector'])))}

assert before=={str(p.name):sha256(p.read_bytes()).hexdigest() for p in protected}
def serial(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,oracle.Choice):return {'support':x.support,'test':x.test,'repair_rule':dict(x.repair_rule)}
    if isinstance(x,(list,tuple)):return [serial(v) for v in x]
    if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
    return x
out={'status':'passed','status_of_analysis':'exploratory followup, outside frozen main design',
     'state':{'horizon':1,'stock':1,'cash':6,'treasury':0,'ready':1,'fault_prior':'1/2'},
     'unchanged':'all physical transition, diagnostic reliability, payment and burden costs',
     'metric_order':['failure','expense','burden','unrecovered'],
     'all_eight_legal_prescriptions':rows,
     'new_weight':[20,1,10,0],'unique_scalar_winner':best,
     'constraint':{'expense_at_most':'9/2','burden_at_most':'1/10'},
     'all_policy_constrained_minimum':all_best,
     'no_test_randomized_constrained_minimum':no_test_best,
     'original_seven_probe_optima_at_new_state':registered_rows,
     'protected_file_hashes_unchanged':before,
     'method':'independent latent-event oracle; exact Fraction vertex enumeration over randomized prescriptions'}
(HERE/'diagnostic_mechanism_results.json').write_text(json.dumps(serial(out),indent=2)+'\n')
print(json.dumps({'status':'passed','actions':len(rows),'scalar_minimum':str(best['score']),
                  'with_test_constrained_failure':str(all_best[0]),
                  'no_test_constrained_failure':str(no_test_best[0]),
                  'seven_original_probes_select_test':False},indent=2))
