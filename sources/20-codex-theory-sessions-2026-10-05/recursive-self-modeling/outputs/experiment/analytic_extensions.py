"""Post-evaluation analytic diagnostics, kept separate from primary results."""
from fractions import Fraction as F
from pathlib import Path
import json,math,sys
import numpy as np
from experiment import data

out=Path(__file__).resolve().parent/'results'
# Exact observational symmetry with unknown constant forcing.
records=[]
for a in [F(4,5),F(1)]:
    for c in [F(-2),F(1,3),F(3)]:
        x,b,d,g=F(2,3),F(-1,2),F(1,4),F(1,10)
        xp,bp,dp,gp=x+c,b-c,d-c,g+(1-a)*c
        for t in range(20):
            eps=F((t%3)-1,20);eta=F((t%5)-2,50);w=F((t%7)-3,100)
            y,z=x+b+eps,x+d+eta
            yp,zp=xp+bp+eps,xp+dp+eta
            assert y==yp and z==zp and xp==x+c
            # Observation-based control; same output under same transcript.
            u=-y/2 if t%2 else -z/2
            up=-yp/2 if t%2 else -zp/2
            assert u==up
            x=a*x+u+g+w;xp=a*xp+up+gp+w
        records.append({'a':str(a),'shift':str(c),'steps':20,'identical_observations_actions':True})

# Passive zero-action benchmark added after the primary evaluation; no parameter fit.
losses=[]
for seed in range(1000,2000):
    x,_,_,_,w=data(seed)
    total=0.
    for noise in w:x=.8*x+noise;total+=x*x
    losses.append(total)
variance=1.;expectation=0.
for t in range(60):variance=.8**2*variance+.05**2;expectation+=variance
se=float(np.std(losses,ddof=1)/math.sqrt(len(losses)))
r={'status':'Post-evaluation analytic extension; not part of the frozen primary comparison family.',
   'symmetry_exact_checks':records,'symmetry_note':'Requires shift-closed parameter/initial-state class; fixed known priors or fixed forcing can break it.',
   'passive_control':{'mean_control_loss':float(np.mean(losses)),'standard_error':se,
      'descriptive_95_interval':[float(np.mean(losses))-1.96*se,float(np.mean(losses))+1.96*se],
      'exact_model_expectation':expectation,'sensing_count':0,'note':'State-only zero-action benchmark, no algorithm work price assigned. Lower bound on its priced total; same in all five worlds.'}}
(out/'analytic-extension-checks.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r))
