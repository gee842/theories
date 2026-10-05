"""Fresh experiment on access to correction. See protocol.json for frozen design."""
from pathlib import Path
import argparse, hashlib, json, math, statistics, time
import numpy as np
from anchor_filter import AnchorFilter

HERE=Path(__file__).resolve().parent
H=60; A=.8; K=.5; RY=.25**2; RZ=.05**2; QX=.05**2; QH=.0025
PERIODIC=(0,10,20,35,45,55); PROTECTED=(0,25,55)
POLICIES=['confidence','innovation','periodic','hybrid','anchor_filter']
WORLDS=[f'{change}_g{g}_d{d}' for change in ['constant','change'] for g in [0,1] for d in [0,1]]+['no_bias']
METRICS=['total_loss','control_loss','state_loss','action_effort','sense_count','sense_cost',
'estimate_mse','relative_bias_mse','absolute_bias_mse','ref_bias_mse','coverage90','interval_width90',
'normalized_forecast_error','access_delay','sample_found','recovery_delay','recovered',
'alarm_steps','monitor_steps','fast_updates','prechange_purchases','postchange_purchases']
TRACE_COLS=['t','x','b','g','d','y','z','xhat','variance','h','dhat','u','x_next','buy','fast','alarm','score','ph']

def data(seed):
    rng=np.random.default_rng(seed)
    return (float(rng.normal()),int(rng.choice([-1,1])),int(rng.choice([-1,1])),
            int(rng.choice([-1,1])),int(rng.integers(8,48)),
            rng.normal(0,.25,H),rng.normal(0,.05,H),rng.normal(0,.05,H))

class ScalarPolicy:
    """All four gates share correction and control. No hidden truth enters this API."""
    def __init__(self,name,threshold=2.):
        self.name=name;self.threshold=threshold;self.h=0.;self.ph=1.
        self.last_y=None;self.last_u=0.;self.purchases=0;self.discretionary=0
        self.latch=0.;self.monitor_steps=0;self.alarm_steps=0;self.fast_updates=0
    def begin(self,t,y):
        self.t=t;self.y=y
        if t:self.ph+=QH
        self.score=0.;self.alarm=False
        if self.name in ['innovation','hybrid'] and t:
            r=y-A*self.last_y-self.last_u-(1-A)*self.h
            # A heuristic scale: correlations and model misspecification are not integrated out.
            self.score=abs(r)/math.sqrt(QX+(1+A*A)*RY+(1-A)**2*self.ph)
            self.latch=max(self.latch,self.score)
            self.alarm=self.score>self.threshold
            self.monitor_steps+=1;self.alarm_steps+=int(self.alarm)
        self.last_y=y
    def wants_reference(self):
        if self.t%5:return False
        if self.name=='confidence':
            v=self.ph+RY;delta=v-((1-.2)**2*v+.2**2*RZ)
            buy=self.purchases<6 and K*K*delta>.02
        elif self.name=='periodic':buy=self.t in PERIODIC
        elif self.name=='innovation':buy=self.purchases<6 and (self.t==0 or self.latch>self.threshold)
        elif self.name=='hybrid':
            buy=self.t in PROTECTED or (self.discretionary<3 and self.latch>self.threshold)
        else:raise ValueError(self.name)
        self.latch=0.  # Each opportunity closes the preceding monitoring interval, even on a decline.
        return buy
    def finish(self,z):
        self.fast=False
        if z is not None:
            self.purchases+=1
            if self.name=='hybrid' and self.t not in PROTECTED:self.discretionary+=1
            residual=self.y-z-self.h
            self.fast=abs(residual)>2*math.sqrt(self.ph+RY+RZ)
            alpha=1. if self.fast else .2
            v=(1-alpha)**2*(self.ph+RY)+alpha*alpha*RZ
            self.h=(1-alpha)*self.h+alpha*(self.y-z)
            self.ph=(1-alpha)**2*self.ph+alpha*alpha*(RY+RZ)
            self.fast_updates+=int(self.fast)
        else:v=self.ph+RY
        xhat=self.y-self.h;u=float(np.clip(-K*xhat,-2,2));self.last_u=u
        return xhat,v,self.h,0.,u

class AnchorPolicy:
    def __init__(self,q_b):
        self.f=AnchorFilter(q_b=q_b);self.last_u=0.;self.purchases=0
        self.alarm_steps=0;self.monitor_steps=0;self.fast_updates=0
        self.fast=False;self.alarm=False;self.score=0.;self.ph=math.nan
    def begin(self,t,y):
        self.t=t
        if t:self.f.predict(self.last_u)
        self.f.update_y(y)
    def wants_reference(self):return self.t in PERIODIC
    def finish(self,z):
        if z is not None:self.f.update_z(z);self.purchases+=1
        u=float(np.clip(-K*self.f.x_mean,-2,2));self.last_u=u
        return self.f.x_mean,self.f.x_variance,self.f.bias_mean,self.f.ref_bias_mean,u

def run(seed,world,name,params,trace=False,override=None):
    x,b0,sg,sd,tau,eps,eta,w=data(seed)
    if override:
        x=override.get('x0',x);b0=override.get('b0',b0);tau=override.get('tau',tau)
        eps=override.get('eps',eps);eta=override.get('eta',eta);w=override.get('w',w)
    changed=world.startswith('change')
    g=.15*sg if '_g1_' in world else 0.;d=.25*sd if world.endswith('_d1') else 0.
    if world=='no_bias':b0=0
    if override:g=override.get('g',g);d=override.get('d',d)
    p=AnchorPolicy(params['q_b']) if name=='anchor_filter' else ScalarPolicy(name,params.get('threshold',2.))
    purchases=np.zeros(H,dtype=bool);alarms=np.zeros(H,dtype=bool);fast=np.zeros(H,dtype=bool)
    sums=dict.fromkeys(METRICS,0.);rows=[];after=[]
    for t in range(H):
        b=-b0 if changed and t>=tau else b0
        y=x+b+eps[t];p.begin(t,y);buy=p.wants_reference()
        z=x+d+eta[t] if buy else None
        xhat,v,h,dhat,u=p.finish(z)
        xn=A*x+u+g+w[t];mu=A*xhat+u;pv=max(1e-15,A*A*v+QX)
        sums['state_loss']+=xn*xn;sums['action_effort']+=u*u
        sums['estimate_mse']+=(xhat-x)**2
        sums['relative_bias_mse']+=((h-dhat)-(b-d))**2
        sums['absolute_bias_mse']+=(h-b)**2;sums['ref_bias_mse']+=(dhat-d)**2
        sums['coverage90']+=abs(xn-mu)<=1.6448536269514722*math.sqrt(pv)
        sums['interval_width90']+=2*1.6448536269514722*math.sqrt(pv)
        sums['normalized_forecast_error']+=(xn-mu)**2/pv
        purchases[t]=buy;alarms[t]=p.alarm;fast[t]=p.fast
        if changed and t>=tau:after.append(abs(xn)<=.2)
        if trace:rows.append([t,x,b,g,d,y,z,xhat,v,h,dhat,u,xn,buy,p.fast,p.alarm,p.score,p.ph])
        x=xn
    for k in ['estimate_mse','relative_bias_mse','absolute_bias_mse','ref_bias_mse','coverage90','interval_width90','normalized_forecast_error']:sums[k]/=H
    sums['control_loss']=sums['state_loss']+.05*sums['action_effort']
    sums['sense_count']=p.purchases;sums['sense_cost']=.02*p.purchases
    sums['total_loss']=sums['control_loss']+sums['sense_cost']
    sums['alarm_steps']=p.alarm_steps;sums['monitor_steps']=p.monitor_steps;sums['fast_updates']=p.fast_updates
    for k in ['access_delay','sample_found','recovery_delay','recovered','prechange_purchases','postchange_purchases']:sums[k]=math.nan
    if changed:
        later=np.flatnonzero(purchases[tau:])
        sums['access_delay']=int(later[0]) if len(later) else H-tau
        sums['sample_found']=int(bool(len(later)))
        sums['prechange_purchases']=int(purchases[:tau].sum());sums['postchange_purchases']=int(purchases[tau:].sum())
        delay=H-tau;recovered=0
        for j in range(len(after)-4):
            if all(after[j:j+5]):delay=j+5;recovered=1;break
        sums['recovery_delay']=delay;sums['recovered']=recovered
    return np.array([sums[k] for k in METRICS]),np.array(rows,dtype=float) if trace else None,purchases,alarms,fast

def dump(path,obj):path.write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n')
def fhash(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def development(folder):
    folder.mkdir(parents=True,exist_ok=True)
    selected={'confidence':{},'periodic':{}};scores={}
    grids={n:[{'threshold':v} for v in [1.5,2,2.5,3,3.5]] for n in ['innovation','hybrid']}
    grids['anchor_filter']=[{'q_b':v} for v in [0,.0025,.04]]
    for n,grid in grids.items():
        scores[n]=[]
        for par in grid:
            vals=[run(seed,world,n,par)[0][0] for seed in range(20000,20200) for world in WORLDS[:8]]
            score={'params':par,'mean_total_loss':float(np.mean(vals))};scores[n].append(score)
            print(json.dumps({'development':n,**score}),flush=True)
        selected[n]=min(scores[n],key=lambda r:r['mean_total_loss'])['params']
    dump(folder/'development.json',scores);dump(folder/'selected.json',selected)

def frozen_paths(folder):return [HERE/'experiment.py',HERE/'anchor_filter.py',HERE/'protocol.json',folder/'selected.json']
def freeze(folder):
    dump(folder/'freeze.json',{'created_unix':time.time(),'files':{p.name:fhash(p) for p in frozen_paths(folder)},'evaluation_seeds':[30000,31999]})
def check_freeze(folder):
    hashes=json.loads((folder/'freeze.json').read_text())['files']
    for p in frozen_paths(folder):assert fhash(p)==hashes[p.name],f'Frozen source changed: {p}'

def evaluate(folder):
    check_freeze(folder);params=json.loads((folder/'selected.json').read_text())
    result=np.empty((9,5,2000,len(METRICS)));buy=np.empty((9,5,2000,H),dtype=bool)
    alarm=np.empty_like(buy);fast=np.empty_like(buy);timing={}
    for wi,world in enumerate(WORLDS):
        for pi,name in enumerate(POLICIES):
            start=time.perf_counter()
            for j,seed in enumerate(range(30000,32000)):
                vals,tr,b,a,f=run(seed,world,name,params[name],trace=seed==30000)
                result[wi,pi,j]=vals;buy[wi,pi,j]=b;alarm[wi,pi,j]=a;fast[wi,pi,j]=f
                if tr is not None:np.save(folder/f'trace-{world}-{name}.npy',tr)
            timing[f'{world}/{name}']=time.perf_counter()-start
            print(json.dumps({'evaluated':world,'policy':name,'mean_loss':float(result[wi,pi,:,0].mean())}),flush=True)
    meta=np.array([data(seed)[:5] for seed in range(30000,32000)])
    np.savez_compressed(folder/'all-results.npz',values=result,buy=buy,alarm=alarm,fast=fast,metadata=meta,
                        worlds=np.array(WORLDS),policies=np.array(POLICIES),metrics=np.array(METRICS),trace_columns=np.array(TRACE_COLS),seeds=np.arange(30000,32000))
    dump(folder/'execution.json',{'end_to_end_seconds_per_2000_episodes':timing,'episodes':90000,'seed_clusters':2000})

def interval(vals,z=1.959963984540054):
    vals=np.asarray(vals);vals=vals[np.isfinite(vals)]
    if not len(vals):return None
    m=float(vals.mean());se=float(vals.std(ddof=1)/math.sqrt(len(vals)))
    return {'mean':m,'se':se,'lo':m-z*se,'hi':m+z*se,'n':len(vals)}
def summarize(folder):
    f=np.load(folder/'all-results.npz');v=f['values'];rows=[];desc=[];primary=[]
    for wi,w in enumerate(WORLDS):
        for pi,p in enumerate(POLICIES):
            rows.append({'world':w,'policy':p,'metrics':{m:interval(v[wi,pi,:,mi]) for mi,m in enumerate(METRICS)}})
        for pi,p in enumerate(POLICIES[1:],1):
            desc.append({'world':w,'contrast':p+' minus confidence','total_loss':interval(v[wi,pi,:,0]-v[wi,0,:,0])})
    z=statistics.NormalDist().inv_cdf(1-.05/(2*6))
    for label,ix in [('constant',range(4)),('change',range(4,8))]:
        for pi,p in [(1,'innovation'),(2,'periodic'),(3,'hybrid')]:
            diffs=(v[list(ix),pi,:,0]-v[list(ix),0,:,0]).mean(axis=0)
            ci=interval(diffs,z)
            primary.append({'stratum':label,'contrast':p+' minus confidence','interval':ci,'improves_margin_02':ci['hi']<-.02,'worse_margin_02':ci['lo']>.02})
    dump(folder/'summary.json',{'means':rows,'primary':primary,'descriptive':desc,'primary_z':z})
    print(json.dumps({'primary':primary},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('command',choices=['development','freeze','evaluate','summarize']);parser.add_argument('--folder',type=Path,default=HERE/'results')
    args=parser.parse_args();globals()[args.command](args.folder)
