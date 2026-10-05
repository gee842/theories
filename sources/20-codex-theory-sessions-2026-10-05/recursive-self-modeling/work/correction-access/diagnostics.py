"""Post-evaluation descriptive summaries; no policy retuning or new evaluation data."""
from pathlib import Path
import json,math
import numpy as np
P=Path(__file__).resolve().parent
f=np.load(P/'results/all-results.npz');v=f['values'];m=list(f['metrics']);names=list(f['policies'])
def ci(x):
 x=np.asarray(x);x=x[np.isfinite(x)];mean=float(x.mean());se=float(x.std(ddof=1)/math.sqrt(len(x)))
 return {'mean':mean,'lo':mean-1.95996398454*se,'hi':mean+1.95996398454*se}
r={'note':'Post-evaluation descriptive diagnostics, derived from frozen raw trajectories. No retuning.', 'strata':{},'mixture_reweighting':{},'anchor_vs_periodic':{}}
for label,ix in [('constant',list(range(4))),('change',list(range(4,8))),('no_bias',[8])]:
 r['strata'][label]={}
 for pi,p in enumerate(names):
  wanted=['total_loss','control_loss','sense_count','alarm_steps','access_delay','sample_found','recovered','relative_bias_mse','absolute_bias_mse','coverage90','estimate_mse','monitor_steps']
  if label!='change':wanted=[k for k in wanted if k not in ['access_delay','sample_found','recovered']]
  r['strata'][label][p]={k:ci(v[ix,pi,:,m.index(k)].mean(axis=0)) for k in wanted}
  if label=='change':
   r['strata'][label][p]['max_observed_access_delay']=float(v[ix,pi,:,m.index('access_delay')][v[ix,pi,:,m.index('sample_found')]==1].max())
for pi,p in enumerate(names[1:4],1):
 c=(v[:4,pi,:,0]-v[:4,0,:,0]).mean(axis=0)
 d=(v[4:8,pi,:,0]-v[4:8,0,:,0]).mean(axis=0)
 r['mixture_reweighting'][p]={'constant_minus_confidence':ci(c),'change_minus_confidence':ci(d),
 'point_crossover_change_probability':float(c.mean()/(c.mean()-d.mean())),
 'differences_at_probability':{str(p0):ci((1-p0)*c+p0*d) for p0 in [0,.1,.25,.5,.75,1]}}
for wi,w in enumerate(f['worlds'][:8]):
 r['anchor_vs_periodic'][w]={k:ci(v[wi,4,:,m.index(k)]-v[wi,2,:,m.index(k)]) for k in ['total_loss','estimate_mse','coverage90','relative_bias_mse','absolute_bias_mse','ref_bias_mse']}
(P/'results/diagnostics.json').write_text(json.dumps(r,indent=2)+'\n')
for label,ps in r['strata'].items():
 print(label)
 for p,mm in ps.items():print(p,{k:round(vv['mean'],4) if isinstance(vv,dict) else vv for k,vv in mm.items()})
print('REWEIGHTING',json.dumps(r['mixture_reweighting'],indent=2))
print('ANCHOR',json.dumps(r['anchor_vs_periodic'],indent=2))
