#!/usr/bin/env python3
"""Post hoc nonnegative-level sensitivity; preserve planned analysis unchanged."""
import json
from pathlib import Path
import numpy as np
from scipy.optimize import minimize_scalar
from analyze_recovery import HERE, GROUPS, sha, save
rows=json.loads((HERE/'observations.json').read_text())
primary=json.loads((HERE/'results.json').read_text())
output=[]
for p in primary['participants']:
 start=191 if p['group']==GROUPS[0] else 195
 y=np.array([r['adaptation'] for r in rows if r['group']==p['group'] and r['participant']==p['participant'] and r['trial']>=start])
 for centered in [False,True]:
  v=y-p['baseline'] if centered else y
  train=v[:-50]; t=np.arange(len(train));tf=np.arange(len(train),len(v))
  def evaluate(q):
   b=q**t;x=np.column_stack([np.ones(len(t)),b]);c=np.linalg.lstsq(x,train,rcond=None)[0]
   if c[0]<0:c=np.array([0.,np.dot(b,train)/np.dot(b,b)])
   return float(np.sum((x@c-train)**2)),c
  grid=np.unique(np.r_[np.linspace(0,1,1001),1-np.logspace(-8,-3,40)])
  loss=np.array([evaluate(q)[0] for q in grid]); candidates=list(zip(grid,loss))
  for i in range(1,len(grid)-1):
   if loss[i]<=loss[i-1] and loss[i]<=loss[i+1]:
    o=minimize_scalar(lambda q:evaluate(q)[0],bounds=(grid[i-1],grid[i+1]),method='bounded',options={'xatol':1e-12});candidates.append((o.x,o.fun))
  q,_=min(candidates,key=lambda z:z[1]);sse,c=evaluate(q);pred=c[0]+c[1]*q**tf
  output.append({'group':p['group'],'participant':p['participant'],'baseline_corrected':centered,'q':float(q),'coefficients':c.tolist(),'calibration_sse':sse,'rmse':float(np.sqrt(np.mean((pred-v[-50:])**2))),'predictions':pred.tolist()})
summary={}
for g in GROUPS:
 summary[g]={}
 for center in [False,True]:
  selected=[p for p in output if p['group']==g and p['baseline_corrected']==center]
  scale='forecast_baseline_corrected' if center else 'forecast_raw'
  delta=[p['rmse']-next(s for s in primary['participants'] if s['group']==g and s['participant']==p['participant'])[scale]['zero_level_decay']['rmse'] for p in selected]
  summary[g][scale]={'mean_participant_rmse':float(np.mean([p['rmse'] for p in selected])),'better_than_zero_count':sum(d<0 for d in delta),'rmse_difference':float(np.mean(delta))}
save('sensitivity-results.json',{'status':'completed','post_hoc':True,'level_constraint':'c >= 0','participants':output,'summary':summary,'source_sha256':{'analysis':sha(Path(__file__)),'note':sha(HERE/'SENSITIVITY-NOTE.md'),'observations':sha(HERE/'observations.json'),'primary_results':sha(HERE/'results.json')}})
print(json.dumps(summary,indent=2))
