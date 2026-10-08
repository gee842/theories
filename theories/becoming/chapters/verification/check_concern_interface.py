"""Exact decision-interface checks, independent of the concern branch's code."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

count=0
for r,c,chi,v,H,z in product(range(1,5),range(1,5),range(1,5),[F(i,2) for i in range(11)], [F(1),F(2)],[F(0),F(1,4),F(1,2),F(3,4),F(1)]):
    # Primitive money and patient-harm ledger for each realized action.
    cash={'S':r-c,'B':r-chi,'H':0}
    harm={'S':(1-z)*H,'B':H,'H':F(0)}
    values={a:cash[a]-v*harm[a] for a in cash}
    best=max(values.values())
    choices={a for a in values if values[a]==best}
    threshold=(c<chi+z*v*H and c+(1-z)*v*H<r)
    assert (choices=={'S'})==threshold
    inactive={'S':r-c-v*(1-z)*H,'B':r-chi-v*H,'H':r-v*H}
    best=max(inactive.values())
    choices={a for a in inactive if inactive[a]==best}
    assert (choices=={'S'})==(z*v*H>c)
    count+=1
result={'status':'passed','active_and_inactive_parameter_cases':count,'scope':'Exact finite rational decision checks. Not dynamic closure or empirical evidence.'}
Path(__file__).with_name('concern-interface-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
