"""Independent joint-latent Markov calculation for zero-output control."""
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import json

# With barred cash zero/one, unready equipment and output zero, no action
# except drop/no-test/no-repair can ever be afforded. Thus no optimizer or
# belief filter is needed: propagate the true joint physical/fault law.
law={(2,1):Q(1)}
rows=[]
for t in range(4):
    successor=defaultdict(Q)
    for (x,h),mass in law.items():
        if x==0:
            successor[(0,0)]+=mass
            continue
        risk=Q(4,5) if h else Q(1,10)
        for damage,pd in ((0,1-risk),(1,risk)):
            xp=max(0,min(3,x+1-2*damage))
            if xp==0:
                successor[(0,0)]+=mass*pd
            else:
                next_h=Q(19,20) if h else Q(1,10)
                successor[(xp,1)]+=mass*pd*next_h
                successor[(xp,0)]+=mass*pd*(1-next_h)
    law=successor
    assert sum(law.values())==1
    rows.append({'round':t+1,'failure_exact':str(law[(0,0)])})
failure=law[(0,0)]
assert failure==Q('0.7918345')
out={'status':'passed','method':'direct exact propagation of joint stock/true fault, no candidate-module import',
     'initial_stock':2,'initial_fault':1,'horizon':4,
     'barred_cash_zero_and_one_same_failure':str(failure),
     'failure_decimal':float(failure),'rounds':rows,
     'scope':'zero-output, inaccessible treasury, no initially affordable action beyond doing nothing'}
Path(__file__).with_name('audit_no_output_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
