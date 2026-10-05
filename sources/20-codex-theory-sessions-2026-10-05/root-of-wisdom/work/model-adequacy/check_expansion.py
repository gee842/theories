"""Independent exact check of scheduled representational expansion, not noisy discovery performance."""
from itertools import combinations,product
from fractions import Fraction as F
from pathlib import Path
import json

worlds=list(product((0,1),repeat=6))
def risk(x,a):
    hazardous=all(x[i]==1 for i in range(4))
    return F(1,20)+(F(3,4) if hazardous and a==0 else 0)+(F(1,4) if a==1 else 0)
base=sum(risk(x,0) for x in worlds)/64
assert base==F(31,320)
records=[]
all_predicates=[]
for depth in range(7):
    # Generation uses only feature indices, binary values and the current depth.
    # It does not consult the hazard definition or any benefit value.
    new=[tuple(zip(indices,values)) for indices in combinations(range(6),depth)
         for values in product((0,1),repeat=depth)]
    gains=[]
    for terms in new:
        value=sum(risk(x,int(all(x[i]==v for i,v in terms))) for x in worlds)/64
        gains.append(base-value)
    all_predicates.extend(new)
    records.append({'depth':depth,'new_candidates':len(new),'cumulative_candidates':len(all_predicates),
                    'best_at_exact_depth_gain':str(max(gains)),'positive_candidates':sum(g>0 for g in gains)})
assert [r['new_candidates'] for r in records]==[1,12,60,160,240,192,64]
assert len(all_predicates)==len(set(all_predicates))==729
assert [r['best_at_exact_depth_gain'] for r in records][2:5]==['-1/64','1/64','1/32']
result={'status':'passed','scope':'Exact candidate coverage and operating gains, not finite-sample ranking or confirmation performance.',
 'reference_loss_always_A':str(base),'schedule':'Generate every conjunction at successive depths regardless of previous values. Nomination/test allocation is an additional requirement, not simulated here.',
 'depths':records,'best_through_depth_two_including_no_change':'0','best_through_depth_three_gain':'1/64','best_through_depth_four_gain':'1/32',
 'costs_excluded':['candidate generation','recording','testing','delay','any ongoing feature-use costs'],
 'limits':['All six binary attributes and two actions are supplied.','Generation is complete only for conjunctions over those variables.','Existing validation samples may have low power and deeper subgroups are rare.','No performance claim about noisy discovery follows from policy coverage.']}
out=Path(__file__).with_name('expansion-check-results.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
