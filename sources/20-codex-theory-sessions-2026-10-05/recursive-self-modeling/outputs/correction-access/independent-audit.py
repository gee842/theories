"""Independent array, scalar-replay, and selective API audit. Never alters frozen inputs."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, math, statistics, sys
import numpy as np

HERE=Path(__file__).resolve().parent
PARSER=argparse.ArgumentParser()
PARSER.add_argument('--folder',type=Path,default=HERE/'results')
PARSER.add_argument('--skip-api',action='store_true')
ARGS=PARSER.parse_args();FOLDER=ARGS.folder
if not (FOLDER/'all-results.npz').exists():
    raise SystemExit('Raw results not yet available. Run this audit after evaluation completes.')

z=np.load(FOLDER/'all-results.npz')
v=z['values'];buy=z['buy'];alarm=z['alarm'];fast=z['fast'];meta=z['metadata']
worlds=list(z['worlds']);policies=list(z['policies']);metrics=list(z['metrics'])
seeds=z['seeds'];N=len(seeds);H=60
normal=statistics.NormalDist();critical=normal.inv_cdf(1-.05/12)
selected=json.loads((FOLDER/'selected.json').read_text())
summary=json.loads((FOLDER/'summary.json').read_text())
lines=[];checks=[]
def out(s=''):lines.append(s)
def check(label,ok):
    checks.append(label)
    if not bool(ok):raise AssertionError(label)
def near(label,left,right,tol=1e-10):
    check(label,np.allclose(left,right,rtol=1e-10,atol=tol,equal_nan=True))
def vector(world,policy,metric):return v[worlds.index(world),policies.index(policy),:,metrics.index(metric)]
def ci(a,c=1.959963984540054):
    a=np.asarray(a);a=a[np.isfinite(a)]
    if not len(a):return None
    mean=float(a.mean());se=float(a.std(ddof=1)/np.sqrt(len(a)))
    return {'mean':mean,'se':se,'lo':mean-c*se,'hi':mean+c*se,'n':len(a)}
def compare_ci(label,observed,expected):
    if expected is None:check(label,observed is None);return
    for key in expected:near(label+'/'+key,observed[key],expected[key],1e-12)

check('dimensions',v.shape==(9,5,2000,22))
check('acquisition shape',buy.shape==alarm.shape==fast.shape==(9,5,2000,60))
check('fresh evaluation seeds',np.array_equal(seeds,np.arange(30000,32000)))
check('metadata shape',meta.shape==(2000,5))
check('no purchase off grid',not buy[...,np.arange(H)%5!=0].any())
check('hard sensing cap',np.all(buy.sum(axis=-1)<=6))
check('fast only after purchase',not np.any(fast & ~buy))
for wi,world in enumerate(worlds):
    for pi,policy in enumerate(policies):
        a=v[wi,pi]
        near('purchase count/'+world+'/'+policy,a[:,metrics.index('sense_count')],buy[wi,pi].sum(axis=-1),0)
        near('alarm count/'+world+'/'+policy,a[:,metrics.index('alarm_steps')],alarm[wi,pi].sum(axis=-1),0)
        near('fast count/'+world+'/'+policy,a[:,metrics.index('fast_updates')],fast[wi,pi].sum(axis=-1),0)
        near('sensing price/'+world+'/'+policy,a[:,metrics.index('sense_cost')],.02*buy[wi,pi].sum(axis=-1))
        near('control accounting/'+world+'/'+policy,a[:,metrics.index('control_loss')],a[:,metrics.index('state_loss')]+.05*a[:,metrics.index('action_effort')])
        near('total accounting/'+world+'/'+policy,a[:,0],a[:,metrics.index('control_loss')]+a[:,metrics.index('sense_cost')])
        if policy in ['innovation','hybrid']:
            check('monitor count/'+world+'/'+policy,np.all(a[:,metrics.index('monitor_steps')]==59))
        else:
            check('no alarm monitor/'+world+'/'+policy,not alarm[wi,pi].any() and np.all(a[:,metrics.index('monitor_steps')]==0))
        if policy in ['periodic','anchor_filter']:
            expect=np.zeros((N,H),bool);expect[:,[0,10,20,35,45,55]]=True
            check('periodic guarantee/'+world+'/'+policy,np.array_equal(buy[wi,pi],expect))
        if policy=='hybrid':
            check('protected guarantee/'+world,np.all(buy[wi,pi][:,[0,25,55]]))
            check('discretionary cap/'+world,np.all(buy[wi,pi].sum(axis=-1)-3<=3))
        if world.startswith('change'):
            tau=meta[:,4].astype(int);post=np.arange(H)[None,:]>=tau[:,None]
            count=(buy[wi,pi]&post).sum(axis=-1);found=count>0
            delay=np.where(found,np.where(buy[wi,pi]&post,np.arange(H)[None,:]-tau[:,None],H).min(axis=-1),H-tau)
            near('access delay/'+world+'/'+policy,a[:,metrics.index('access_delay')],delay,0)
            near('found/'+world+'/'+policy,a[:,metrics.index('sample_found')],found,0)
            near('post count/'+world+'/'+policy,a[:,metrics.index('postchange_purchases')],count,0)
            near('pre count/'+world+'/'+policy,a[:,metrics.index('prechange_purchases')],(buy[wi,pi]&~post).sum(axis=-1),0)

for row in summary['means']:
    for metric,expected in row['metrics'].items():
        compare_ci('summary mean/'+row['world']+'/'+row['policy']+'/'+metric,ci(vector(row['world'],row['policy'],metric)),expected)
for row in summary['descriptive']:
    left=row['contrast'].split(' minus ')[0]
    compare_ci('descriptive/'+row['world']+'/'+left,ci(vector(row['world'],left,'total_loss')-vector(row['world'],'confidence','total_loss')),row['total_loss'])
for row in summary['primary']:
    ix=[i for i,w in enumerate(worlds) if w.startswith(row['stratum']+'_')]
    left=row['contrast'].split(' minus ')[0];pi=policies.index(left)
    d=(v[ix,pi,:,0]-v[ix,policies.index('confidence'),:,0]).mean(axis=0)
    actual=ci(d,critical)
    compare_ci('primary/'+row['stratum']+'/'+left,actual,row['interval'])
    check('primary benefit/'+row['stratum']+'/'+left,row['improves_margin_02']==(actual['hi']<-.02))
    check('primary harm/'+row['stratum']+'/'+left,row['worse_margin_02']==(actual['lo']>.02))

# Reconstruct the random tape independently, matching its declared consumption order.
tapes=[]
for seed in seeds:
    r=np.random.default_rng(int(seed))
    header=(r.normal(),r.choice([-1,1]),r.choice([-1,1]),r.choice([-1,1]),r.integers(8,48))
    tapes.append((header,r.normal(0,.25,H),r.normal(0,.05,H),r.normal(0,.05,H)))
near('metadata regenerated',np.asarray([t[0] for t in tapes]),meta,0)
eps=np.asarray([t[1] for t in tapes]);eta=np.asarray([t[2] for t in tapes]);noise=np.asarray([t[3] for t in tapes])

def replay_scalar(world,policy):
    """All seeds vectorized; innovation derived by cancelling physical state, independently of the runner."""
    A=.8;RY=.25**2;RZ=.05**2;QX=.05**2;QH=.0025
    x=meta[:,0].copy();initial_b=meta[:,1].copy();tau=meta[:,4].astype(int)
    if world=='no_bias':initial_b[:]=0
    g=.15*meta[:,2] if '_g1_' in world else np.zeros(N)
    d=.25*meta[:,3] if world.endswith('_d1') else np.zeros(N)
    threshold=selected[policy].get('threshold',2.)
    changed=world.startswith('change');h=np.zeros(N);ph=np.ones(N);latch=np.zeros(N)
    purchases=np.zeros(N,int);discretionary=np.zeros(N,int)
    B=np.zeros((N,H),bool);Al=np.zeros_like(B);Fa=np.zeros_like(B);states=np.empty((N,H));trace=[]
    accum={k:np.zeros(N) for k in metrics};previous_b=initial_b.copy()
    for t in range(H):
        if t:ph+=QH
        b=np.where(t>=tau,-initial_b,initial_b) if changed else initial_b
        y=x+b+eps[:,t];score=np.zeros(N);al=np.zeros(N,bool)
        if policy in ['innovation','hybrid'] and t:
            residual=g+b-A*previous_b-(1-A)*h+noise[:,t-1]+eps[:,t]-A*eps[:,t-1]
            score=np.abs(residual)/np.sqrt(QX+(1+A*A)*RY+(1-A)**2*ph)
            latch=np.maximum(latch,score);al=score>threshold
            accum['monitor_steps']+=1
        bought=np.zeros(N,bool)
        if t%5==0:
            if policy=='confidence':
                V=ph+RY;delta=V-((1-.2)**2*V+.2**2*RZ)
                bought=(purchases<6)&(.5*.5*delta>.02)
            elif policy=='innovation':bought=(purchases<6)&((t==0)|(latch>threshold))
            elif policy=='periodic':bought[:]=t in [0,10,20,35,45,55]
            elif policy=='hybrid':bought=(t in [0,25,55])|((discretionary<3)&(latch>threshold))
            latch[:]=0
        # Calibration difference is independent of the controlled physical state.
        calibration=b-d+eps[:,t]-eta[:,t]
        f=bought&(np.abs(calibration-h)>2*np.sqrt(ph+RY+RZ))
        alpha=np.where(f,1.,.2);variance=ph+RY
        variance=np.where(bought,(1-alpha)**2*(ph+RY)+alpha**2*RZ,variance)
        h=np.where(bought,(1-alpha)*h+alpha*calibration,h)
        ph=np.where(bought,(1-alpha)**2*ph+alpha**2*(RY+RZ),ph)
        purchases+=bought
        if policy=='hybrid' and t not in [0,25,55]:discretionary+=bought
        estimate=y-h;u=np.maximum(-2,np.minimum(2,-.5*estimate));next_x=A*x+u+g+noise[:,t]
        mu=A*estimate+u;pv=np.maximum(1e-15,A*A*variance+QX)
        accum['state_loss']+=next_x**2;accum['action_effort']+=u**2
        accum['estimate_mse']+=(estimate-x)**2
        accum['relative_bias_mse']+=(h-(b-d))**2;accum['absolute_bias_mse']+=(h-b)**2;accum['ref_bias_mse']+=d**2
        accum['coverage90']+=np.abs(next_x-mu)<=1.6448536269514722*np.sqrt(pv)
        accum['interval_width90']+=2*1.6448536269514722*np.sqrt(pv)
        accum['normalized_forecast_error']+=(next_x-mu)**2/pv
        accum['alarm_steps']+=al;accum['fast_updates']+=f
        B[:,t]=bought;Al[:,t]=al;Fa[:,t]=f;states[:,t]=next_x
        j=0;trace.append([t,x[j],b[j],g[j],d[j],y[j],x[j]+d[j]+eta[j,t] if bought[j] else np.nan,estimate[j],variance[j],h[j],0.,u[j],next_x[j],bought[j],f[j],al[j],score[j],ph[j]])
        x=next_x;previous_b=b.copy()
    for key in ['estimate_mse','relative_bias_mse','absolute_bias_mse','ref_bias_mse','coverage90','interval_width90','normalized_forecast_error']:accum[key]/=H
    accum['sense_count']=purchases;accum['sense_cost']=.02*purchases
    accum['control_loss']=accum['state_loss']+.05*accum['action_effort']
    accum['total_loss']=accum['control_loss']+accum['sense_cost']
    for key in ['access_delay','sample_found','recovery_delay','recovered','prechange_purchases','postchange_purchases']:accum[key]=np.full(N,np.nan)
    if changed:
        post=np.arange(H)[None,:]>=tau[:,None];found=(B&post).any(axis=-1)
        accum['access_delay']=np.where(found,np.where(B&post,np.arange(H)[None,:]-tau[:,None],H).min(axis=-1),H-tau)
        accum['sample_found']=found.astype(float)
        accum['prechange_purchases']=(B&~post).sum(axis=-1);accum['postchange_purchases']=(B&post).sum(axis=-1)
        rec=np.zeros(N,bool);delay=H-tau
        for end in range(4,H):
            new=(~rec)&(end-4>=tau)&(np.abs(states[:,end-4:end+1])<=.2).all(axis=-1)
            delay=np.where(new,end-tau+1,delay);rec|=new
        accum['recovery_delay']=delay;accum['recovered']=rec.astype(float)
    return np.column_stack([accum[k] for k in metrics]),B,Al,Fa,np.asarray(trace)

for wi,world in enumerate(worlds):
    for pi,policy in enumerate(policies[:4]):
        values,B,Al,Fa,tr=replay_scalar(world,policy)
        near('all scalar metrics independently replayed/'+world+'/'+policy,values,v[wi,pi],1e-9)
        check('full acquisitions independently replayed/'+world+'/'+policy,np.array_equal(B,buy[wi,pi]))
        check('full alarms independently replayed/'+world+'/'+policy,np.array_equal(Al,alarm[wi,pi]))
        check('full fast updates independently replayed/'+world+'/'+policy,np.array_equal(Fa,fast[wi,pi]))
        near('seed30000 full scalar trace/'+world+'/'+policy,tr,np.load(FOLDER/f'trace-{world}-{policy}.npy'),1e-9)

# Verify each saved example's outcome/forecast math, including the independent anchor family.
columns=list(z['trace_columns']);col={k:i for i,k in enumerate(columns)}
for wi,world in enumerate(worlds):
    for pi,policy in enumerate(policies):
        t=np.load(FOLDER/f'trace-{world}-{policy}.npy')
        mu=.8*t[:,col['xhat']]+t[:,col['u']]
        pv=.8*.8*t[:,col['variance']]+.05**2
        near('saved example estimateMSE/'+world+'/'+policy,np.mean((t[:,col['xhat']]-t[:,col['x']])**2),v[wi,pi,0,metrics.index('estimate_mse')])
        near('saved example coverage/'+world+'/'+policy,np.mean(np.abs(t[:,col['x_next']]-mu)<=1.6448536269514722*np.sqrt(pv)),v[wi,pi,0,metrics.index('coverage90')])
        near('saved example NPE/'+world+'/'+policy,np.mean((t[:,col['x_next']]-mu)**2/pv),v[wi,pi,0,metrics.index('normalized_forecast_error')])

# A selective API noninterference test is separate from the independent replay above.
if not ARGS.skip_api:
    sys.path.insert(0,str(HERE))
    spec=importlib.util.spec_from_file_location('correction_access_runner_for_audit',HERE/'experiment.py')
    runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)
    for policy in policies:
        original=runner.run(40000,'change_g1_d1',policy,selected[policy],trace=True)
        eta_test=runner.data(40000)[6].copy();eta_test[~original[2]]=1e8
        modified=runner.run(40000,'change_g1_d1',policy,selected[policy],trace=True,override={'eta':eta_test})
        for ix in range(5):
            check('unacquired reference noninterference/'+policy+'/'+str(ix),np.array_equal(original[ix],modified[ix],equal_nan=True))

manifest=json.loads((FOLDER/'freeze.json').read_text())
for name,digest in manifest['files'].items():
    path=FOLDER/name if name=='selected.json' else HERE/name
    check('freeze hash/'+name,hashlib.sha256(path.read_bytes()).hexdigest()==digest)

out('## Independent numerical audit after evaluation')
out('')
out(f'{len(checks)} assertions passed. Read raw episode arrays and recomputed all summary intervals. Independently regenerated all random tapes and replayed every scalar episode from a separately written vectorized implementation, deriving the innovation by cancellation of physical state. Scalar results and all acquisition/alarm/fast-update arrays match. A separate selective API test changes only unacquired reference values and verifies identical behavior for all five policies on test seed40000; this test imports the runner, unlike the independent replay.')
out('')
out('The data contain 90,000 episodes (nine worlds × five policies × 2,000 seeds). Primary uncertainty uses 2,000 paired seed averages across four worlds, not 8,000 independent world episodes. All six primary intervals, every summary mean/interval, sensing caps, protected checks, purchase delays, scalar recovery, and frozen source hashes were verified. The anchor benchmark is independently checked through aggregate consistency and its saved example forecast math; this audit does not independently replay every anchor episode.')
out('')
out('### Six primary comparisons')
out('')
out('| Stratum | Alternative minus confidence | Mean | Adjusted lower | Adjusted upper | Decision at .02 margin |')
out('|---|---|---:|---:|---:|---|')
for row in summary['primary']:
    r=row['interval'];status='benefit' if r['hi']<-.02 else 'harm' if r['lo']>.02 else 'within margin' if r['lo']>=-.02 and r['hi']<=.02 else 'unresolved'
    out(f"| {row['stratum']} | {row['contrast']} | {r['mean']:+.6f} | {r['lo']:+.6f} | {r['hi']:+.6f} | {status} |")
out('')
out(f'Critical normal value: {critical:.12f}; 99.1667% individual two-sided intervals, Bonferroni family of six.')
out('')
out('### World-specific effects and access')
out('')
out('| World | Policy | Total loss | Control loss | Purchases | Alarms | Coverage90 | Width90 | NPE | Access delay | Post-change sample fraction | Recovery fraction |')
out('|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|')
for world in worlds:
    for policy in policies:
        names=['total_loss','control_loss','sense_count','alarm_steps','coverage90','interval_width90','normalized_forecast_error','access_delay','sample_found','recovered']
        means=[]
        for name in names:
            r=ci(vector(world,policy,name));means.append('—' if r is None else f"{r['mean']:.6f}")
        out('| '+world+' | '+policy+' | '+' | '.join(means)+' |')
out('')
out('All primary results describe the frozen equal-weight mixture and free-computation assumptions. Individual cells are descriptive, not additional multiplicity-controlled discoveries. Access delay measures arrival of a purchased sample, not successful diagnosis or trustworthy correction. Forecast interval coverage is an empirical check of model assumptions; low control loss does not establish calibrated uncertainty. No-change alarms are not automatically false discoveries.')
out('')
out('### Mechanism checks and interpretation')
out('')
out('The constant-bias control is not initially calibrated: h starts at zero while b is ±1. With noiseless clean calibration and no fast update, the residual bias after n slow updates is .8^n times its initial error. Postponing early observations can therefore prolong initial error even without a later change. This is a mechanism explanation under the shared rule, not a randomized mediation estimate.')
out('')
out('| Policy in constant_g0_d0 | Mean purchases through15 | Through25 | Through55 |')
out('|---|---:|---:|---:|')
for policy in policies[:4]:
    b=buy[worlds.index('constant_g0_d0'),policies.index(policy)]
    out(f'| {policy} | {b[:,:16].sum(axis=1).mean():.6f} | {b[:,:26].sum(axis=1).mean():.6f} | {b.sum(axis=1).mean():.6f} |')
out('')
out('Periodic and hybrid have a guaranteed post-change purchase because both protect step55 and all changes occur by47. Their 100% sample-arrival fraction is therefore a design guarantee, not successful learned diagnosis. The six-purchase cap trades earlier calibration against later access; hybrid reserves fewer closely spaced checks than periodic and can still leave long delays.')
out('')
out('The anchor estimator uses the same periodic six measurements but can fail badly when its known-zero-forcing assumption is false. The previously derived shift explains a candidate mechanism: true g=.15 can be represented in a nominal g=0 model by shifting x by−.75 and both biases by+.75. The prespecified seed30000 constant_g1_d0 example ends with true x=.6834, estimated x=.01247, b=1 versus estimated1.7954, and d=0 versus estimated.7458. These finite-run values illustrate, rather than prove exact convergence to, that explanation. Across forcing worlds its very low interval coverage and high normalized error contradict calibrated uncertainty. More reliable access cannot alone correct a false physical anchor.')
(HERE/'independent-audit.txt').write_text('\n'.join(lines)+'\n')
print(f'PASS: {len(checks)} assertions; 72,000 scalar episodes independently replayed; all 45 case summaries checked.')
print('\n'.join(lines[8:22]))
