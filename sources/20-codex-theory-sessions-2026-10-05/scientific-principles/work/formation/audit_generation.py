"""Independent audit: integer enumeration, no import from original generator."""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import json

contexts = list(product((0,1), repeat=3))
target = [x[0]^x[1] for x in contexts]
assignments = list(product((0,1), repeat=8))

def tablefit(fields, outcomes):
    estimates = []
    for x in contexts:
        indices = [i for i,z in enumerate(contexts) if all(z[j]==x[j] for j in fields)]
        estimates.append(int(sum(outcomes[i] for i in indices)*2 > len(indices)))
    wrong = sum(a!=b for a,b in zip(estimates,outcomes))
    return (4*wrong + 2**len(fields)-1, fields, tuple(estimates))

def independent_selection(outcomes, proc):
    baseline = tablefit((),outcomes)
    singles = [tablefit((j,),outcomes) for j in range(3)]
    leading = min(singles)
    cost_quarters=35
    if proc=='greedy' and leading[0]>=baseline[0]:
        return None,F(cost_quarters,4)
    pairs = [p for p in combinations(range(3),2) if proc!='greedy' or leading[1][0] in p]
    cost_quarters+=len(pairs)
    best=min([baseline]+singles+[tablefit(p,outcomes) for p in pairs])
    if best[0]>=baseline[0]:
        return None,F(cost_quarters,4)
    return best,F(cost_quarters+32,4)

def weights(eps):
    p,q=eps.numerator,eps.denominator
    return [p**sum(y!=z for y,z in zip(ys,target))*(q-p)**sum(y==z for y,z in zip(ys,target)) for ys in assignments]

expected=json.loads(Path('work/formation/generation-results.json').read_text())
checks=[]
for row in expected['results']:
    eps=F(row['noise']['exact']);proc=row['procedure'];den=eps.denominator**8
    ws=weights(eps)
    proposal=adoption=gain=cost=F(0)
    bad_adoption=F(0)
    for ys,w in zip(assignments,ws):
        if not w: continue
        candidate,charge=independent_selection(ys,proc)
        cost+=F(w,den)*charge
        if candidate is None: continue
        proposal+=F(w,den)
        _,fields,preds=candidate
        acceptance_mass=sum(vw for vals,vw in zip(assignments,ws) if sum(a==b for a,b in zip(preds,vals))>=7)
        adoption_weight=F(w*acceptance_mass,den**2)
        adoption+=adoption_weight
        # Direct expected deployment error over context and both outcome values.
        risk=sum((eps if pred==true else 1-eps) for pred,true in zip(preds,target))/8
        improvement=F(1,2)-risk-F(len(fields),50)
        gain+=adoption_weight*improvement
        if improvement<=0:
            bad_adoption+=adoption_weight
    actual={'proposal_probability':proposal,'adoption_probability':adoption,'expected_inquiry_cost':cost,'expected_net_gain_per_future_decision':gain,'extra_expected_loss_100_future_decisions':cost-100*gain}
    for k,v in actual.items():
        assert v==F(row[k]['exact']),(eps,proc,k,v,row[k])
    checks.append({'noise':str(eps),'procedure':proc,'all_five_reported_metrics_exactly_matched':True,'probability_of_adopting_nonpositive_deployment_gain':str(bad_adoption)})
result={'independent_integer_enumeration':checks,'training_full_grid_balanced_labels_under_noiseless_XOR':'1','training_full_grid_balanced_labels_under_fair_independent_noise':'35/128','full_grid_balanced_labels_note':'Different transcript statistics despite zero individual-feature mutual information under IID uniform deployment.'}
Path('work/formation/generation-audit-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
