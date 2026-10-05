"""Controlled synthetic comparison. Development and held-out evaluation separate.

See protocol.json for frozen assumptions. No human/brain data are used.
"""
from __future__ import annotations
from pathlib import Path
from collections import Counter
import argparse, csv, hashlib, json, math, statistics, time
import numpy as np
from filter_model import KalmanBiasFilter

HERE=Path(__file__).resolve().parent
A,K,RY,RZ,QX,QH=.8,.5,.25**2,.05**2,.05**2,.0025
HORIZON=60
SENSE_PRICE,WORK_PRICE,CONTROL_PRICE=.02,.0001,.05
WORLD_NAMES=['constant','switch30','reference_bias','no_bias','switch32']
POLICIES=['raw','direct','retained','flat','audit','joint','joint_y_only','repeat']
STAGES=['matched','adaptive']
# Named model blocks are NOT equal FLOPs. The weights are a disclosed price model.
WEIGHTS={'estimate':1,'variance':1,'bias_predict':1,'bias_update':2,'audit':2,
         'control':1,'forecast':1,'gate':1,'reference_value':1,
         'joint_predict':4,'joint_update_y':6,'joint_update_z':6}
PERSISTENT_SCALARS={'raw':0,'direct':0,'retained':2,'flat':2,'audit':2,
                    'joint':5,'joint_y_only':5,'repeat':2}
METRICS=['control_loss','state_loss','action_effort','total_loss','estimate_mse',
         'forecast_mse','brier','coverage90','sense_count','sense_cost','work_units',
         'work_cost','max_abs_x','recovery_delay','recovered','switch_eligible',
         'interval90_width','normalized_forecast_error','event_rate','bias_mse']

def data(seed):
    rng=np.random.default_rng(seed)
    x0=float(rng.normal())
    b0=int(rng.choice([-1,0,1]))
    return x0,b0,rng.normal(0,.25,HORIZON),rng.normal(0,.05,HORIZON),rng.normal(0,.05,HORIZON)

def normal_cdf(x):return .5*(1+math.erf(x/math.sqrt(2)))

class Policy:
    """Only observations, time and own past actions enter the policy."""
    def __init__(self,name,params):
        self.name=name;self.params=params;self.blocks=Counter();self.purchases=0
        self.model={'bias':{'mean':0.,'variance':2/3}}
        self.flat=np.array([0.,2/3])
        self.f=KalmanBiasFilter(q_b=params.get('q_b',0.)) if name.startswith('joint') else None
        self.last_u=0.

    def get_hv(self):
        if self.name=='flat':return float(self.flat[0]),float(self.flat[1])
        return self.model['bias']['mean'],self.model['bias']['variance']

    def set_hv(self,h,v):
        if self.name=='flat':self.flat[:]=h,v
        else:self.model['bias']['mean']=h;self.model['bias']['variance']=v

    def begin(self,t,y):
        self.t=t;self.y=y
        if self.f:
            if t:self.f.predict(self.last_u);self.blocks['joint_predict']+=1
            self.f.update_y(y);self.blocks['joint_update_y']+=1
        elif self.name not in ['raw','direct'] and t:
            h,v=self.get_hv();self.set_hv(h,v+QH);self.blocks['bias_predict']+=1

    def wants_reference(self,stage):
        if self.t%5:return False
        if stage=='matched':return True  # matched packets paid even when ignored
        self.blocks['gate']+=1
        if self.name in ['raw','joint_y_only'] or self.purchases>=6:return False
        if self.f:
            delta=self.f.expected_reference_x_variance_reduction();cost=WEIGHTS['joint_update_z']
        elif self.name=='direct':
            delta=RY+2/3-RZ;cost=0
        else:
            _,v=self.get_hv()
            alpha=self.params['slow'] if self.name=='audit' else self.params['alpha']
            variance=RY+v
            delta=variance-((1-alpha)**2*variance+alpha**2*RZ)
            cost=WEIGHTS['bias_update']+(WEIGHTS['audit'] if self.name=='audit' else 0)
        self.blocks['reference_value']+=1
        # A myopic variance heuristic, not exact value of control or optimal sensing.
        return K*K*delta>SENSE_PRICE+WORK_PRICE*cost

    def finish(self,z):
        y=self.y
        if z is not None:self.purchases+=1
        if self.f:
            if z is not None and self.name!='joint_y_only':
                self.f.update_z(z);self.blocks['joint_update_z']+=1
            xhat,v=self.f.x_mean,self.f.x_variance
            h=self.f.bias_mean
        elif self.name in ['raw','direct']:
            if self.name=='direct' and z is not None:xhat,v=z,RZ
            else:xhat,v=y,RY+2/3
            h=0.;self.blocks['estimate']+=1;self.blocks['variance']+=1
        else:
            h,ph=self.get_hv()
            if z is not None:
                alpha=self.params.get('alpha',0.)
                if self.name=='audit':
                    residual=y-z-h
                    surprise=abs(residual)>self.params['threshold']*math.sqrt(ph+RY+RZ)
                    alpha=self.params['fast'] if surprise else self.params['slow']
                    self.blocks['audit']+=1
                new_h=(1-alpha)*h+alpha*(y-z)
                v=(1-alpha)**2*(ph+RY)+alpha**2*RZ
                new_ph=(1-alpha)**2*ph+alpha**2*(RY+RZ)
                h=new_h;self.set_hv(h,new_ph);self.blocks['bias_update']+=1
            else:v=RY+ph
            # In repeat, repeated computation uses the same frozen h; no double update.
            repeats=4 if self.name=='repeat' else 1
            for _ in range(repeats):xhat=y-h;self.blocks['estimate']+=1
            self.blocks['variance']+=1
        u=max(-2.,min(2.,-K*xhat));self.last_u=u;self.blocks['control']+=1
        mu=A*xhat+u;pv=max(1e-15,A*A*v+QX)
        p=normal_cdf((-.5-mu)/math.sqrt(pv))+1-normal_cdf((.5-mu)/math.sqrt(pv))
        self.blocks['forecast']+=1
        return xhat,v,h,u,mu,pv,min(1.,max(0.,p))

def run(seed,world,name,params,stage,trace=False,eta_override=None):
    x,b0,eps,eta,w=data(seed)
    if eta_override is not None:eta=np.asarray(eta_override)
    if world=='no_bias':b0=0
    d=.25 if world=='reference_bias' else 0.
    switch=30 if world=='switch30' else 32 if world=='switch32' else None
    p=Policy(name,params)
    totals=Counter();max_x=abs(x);rows=[];after=[]
    for t in range(HORIZON):
        b=-b0 if switch is not None and t>=switch else b0
        y=x+b+eps[t]
        p.begin(t,y)
        buy=p.wants_reference(stage)
        z=x+d+eta[t] if buy else None
        xhat,v,h,u,mu,pv,prob=p.finish(z)
        xn=A*x+u+w[t]
        totals['state_loss']+=xn*xn;totals['action_effort']+=u*u
        totals['estimate_mse']+=(xhat-x)**2;totals['forecast_mse']+=(mu-xn)**2
        totals['brier']+=(prob-float(abs(xn)>.5))**2
        totals['coverage90']+=float(abs(xn-mu)<=1.6448536269514722*math.sqrt(pv))
        totals['interval90_width']+=2*1.6448536269514722*math.sqrt(pv)
        totals['normalized_forecast_error']+=(xn-mu)**2/pv
        totals['event_rate']+=float(abs(xn)>.5)
        totals['bias_mse']+=(h-b)**2
        max_x=max(max_x,abs(xn))
        if switch is not None and t>=switch:after.append(abs(xn)<=.2)
        if trace:rows.append([t,x,b,y,z,xhat,v,h,u,xn,mu,pv,prob,int(buy)])
        x=xn
    work=sum(WEIGHTS[key]*n for key,n in p.blocks.items())
    totals['control_loss']=totals['state_loss']+CONTROL_PRICE*totals['action_effort']
    totals['sense_count']=p.purchases;totals['sense_cost']=SENSE_PRICE*p.purchases
    totals['work_units']=work;totals['work_cost']=WORK_PRICE*work
    totals['total_loss']=totals['control_loss']+totals['sense_cost']+totals['work_cost']
    for key in ['estimate_mse','forecast_mse','brier','coverage90','interval90_width',
                'normalized_forecast_error','event_rate','bias_mse']:totals[key]/=HORIZON
    totals['max_abs_x']=max_x
    eligible=switch is not None and abs(b0)==1
    totals['switch_eligible']=int(eligible)
    delay=HORIZON-switch if switch is not None else HORIZON
    recovered=False
    if eligible:
        for j in range(len(after)-4):
            if all(after[j:j+5]):delay=j+5;recovered=True;break
    totals['recovery_delay']=delay if eligible else math.nan
    totals['recovered']=int(recovered) if eligible else math.nan
    vals=np.array([totals[k] for k in METRICS],float)
    return vals,np.array(rows,dtype=float) if trace else None,dict(p.blocks)

def dev(folder):
    folder.mkdir(parents=True,exist_ok=True)
    candidates={'retained':[{'alpha':a} for a in [.2,.5,.8]],
      'audit':[{'slow':s,'fast':f,'threshold':t} for s in [.1,.2] for f in [.8,1.] for t in [2.,3.]],
      'joint':[{'q_b':q} for q in [0.,.0025,.04]],
      'joint_y_only':[{'q_b':q} for q in [0.,.0025,.04]]}
    results={};selected={'raw':{},'direct':{}}
    # Select global parameters across matched and adaptive stages and all four primary worlds.
    for policy,grid in candidates.items():
        scores=[]
        for par in grid:
            vals=[run(seed,world,policy,par,stage)[0][3] for seed in range(100)
                  for world in WORLD_NAMES[:4] for stage in STAGES]
            scores.append({'params':par,'mean_total_loss':float(np.mean(vals))})
        best=min(scores,key=lambda r:r['mean_total_loss'])
        selected[policy]=best['params'];results[policy]=scores
        print(json.dumps({'development_policy':policy,'selected':best}),flush=True)
    for alias in ['flat','repeat']:selected[alias]=dict(selected['retained'])
    baselines={}
    for stage in STAGES:
        scores={name:float(np.mean([run(seed,world,name,selected[name],stage)[0][3]
                                  for seed in range(100) for world in WORLD_NAMES[:4]]))
                for name in ['raw','direct','joint_y_only']}
        baselines[stage]={'selected':min(scores,key=scores.get),'scores':scores}
    (folder/'development.json').write_text(json.dumps({'candidate_scores':results,'baseline_selection':baselines},indent=2)+'\n')
    (folder/'selected.json').write_text(json.dumps({'parameters':selected,'baselines':baselines},indent=2)+'\n')
    print(json.dumps({'frozen_selection':selected,'baselines':baselines}),flush=True)

def filehash(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def freeze(folder):
    paths=[HERE/'experiment.py',HERE/'filter_model.py',HERE/'protocol.json',folder/'selected.json']
    r={'files':{p.name:filehash(p) for p in paths},'evaluation_seeds':[1000,1999],
       'created_unix':time.time(),'note':'Frozen before held-out evaluation; current code checks hashes.'}
    (folder/'freeze.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r),flush=True)

def check_freeze(folder):
    r=json.loads((folder/'freeze.json').read_text())
    for p in [HERE/'experiment.py',HERE/'filter_model.py',HERE/'protocol.json',folder/'selected.json']:
        assert filehash(p)==r['files'][p.name],f'Frozen file changed: {p}'

def evaluate(folder):
    check_freeze(folder)
    selected=json.loads((folder/'selected.json').read_text())['parameters']
    result=np.empty((len(STAGES),len(WORLD_NAMES),len(POLICIES),1000,len(METRICS)))
    timing={};equivalence=[];blocks={}
    for si,stage in enumerate(STAGES):
        for wi,world in enumerate(WORLD_NAMES):
            for pi,name in enumerate(POLICIES):
                start=time.perf_counter()
                for j,seed in enumerate(range(1000,2000)):
                    value,tr,b=run(seed,world,name,selected[name],stage,trace=seed==1000)
                    result[si,wi,pi,j]=value
                    if seed==1000:
                        np.save(folder/f'trace-{stage}-{world}-{name}.npy',tr)
                        blocks[f'{stage}/{world}/{name}']=b
                timing[f'{stage}/{world}/{name}']=time.perf_counter()-start
            retained=result[si,wi,POLICIES.index('retained')]
            flat=result[si,wi,POLICIES.index('flat')]
            assert np.array_equal(retained,flat,equal_nan=True)
            # check complete per-step behavior for all evaluation seeds; the two paths store state differently
            discrepancy=0.
            for seed in range(1000,2000):
                _,r,_=run(seed,world,'retained',selected['retained'],stage,trace=True)
                _,f,_=run(seed,world,'flat',selected['flat'],stage,trace=True)
                assert np.array_equal(r,f,equal_nan=True)
            equivalence.append({'stage':stage,'world':world,'seeds':1000,'max_discrepancy':discrepancy})
            print(json.dumps({'evaluated_stage':stage,'world':world,'seeds':1000}),flush=True)
    np.savez_compressed(folder/'all-results.npz',values=result,metrics=METRICS,policies=POLICIES,
                        worlds=WORLD_NAMES,stages=STAGES,seeds=np.arange(1000,2000))
    (folder/'execution.json').write_text(json.dumps({'end_to_end_simulation_seconds':timing,'equivalence':equivalence,
       'example_blocks':blocks,'persistent_belief_scalars':PERSISTENT_SCALARS},indent=2)+'\n')
    summarize(folder)

def summarize(folder):
    z=np.load(folder/'all-results.npz');v=z['values']
    selected=json.loads((folder/'selected.json').read_text())
    rows=[];contrasts=[];normal=statistics.NormalDist()
    critical=normal.inv_cdf(1-.05/(2*8))
    for si,stage in enumerate(STAGES):
        for wi,world in enumerate(WORLD_NAMES):
            for pi,policy in enumerate(POLICIES):
                row={'stage':stage,'world':world,'policy':policy}
                for mi,name in enumerate(METRICS):
                    vals=v[si,wi,pi,:,mi];valid=vals[np.isfinite(vals)]
                    row[name]=float(np.mean(valid)) if len(valid) else None
                for price in [0.,.0001,.001,.01]:
                    row[f'total_work_price_{price}']=row['control_loss']+row['sense_cost']+price*row['work_units']
                rows.append(row)
            baseline=selected['baselines'][stage]['selected']
            for left,right,kind in [('retained',baseline,'primary'),('retained','direct','descriptive'),
                 ('audit','retained','descriptive'),('joint','retained','descriptive'),
                 ('joint_y_only','joint','descriptive'),('repeat','retained','descriptive')]:
                if wi>=4:kind='descriptive'
                diff=v[si,wi,POLICIES.index(left),:,3]-v[si,wi,POLICIES.index(right),:,3]
                mean=float(np.mean(diff));se=float(np.std(diff,ddof=1)/math.sqrt(len(diff)))
                crit=critical if kind=='primary' and wi<4 else normal.inv_cdf(.975)
                contrasts.append({'stage':stage,'world':world,'left':left,'right':right,'kind':kind,
                    'mean_difference':mean,'se':se,'lower':mean-crit*se,'upper':mean+crit*se,
                    'n_seed_clusters':1000,'critical_value':crit,'practical_margin':.02,
                    'improvement_beyond_margin':bool(mean+crit*se<-.02)})
    (folder/'summary.json').write_text(json.dumps({'rows':rows,'contrasts':contrasts},indent=2,allow_nan=False)+'\n')
    with (folder/'summary.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    print(json.dumps({'summary_rows':len(rows),'contrasts':len(contrasts)}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['dev','freeze','evaluate','summarize'])
    p.add_argument('--folder',type=Path,default=HERE/'results');args=p.parse_args()
    {'dev':dev,'freeze':freeze,'evaluate':evaluate,'summarize':summarize}[args.mode](args.folder)
