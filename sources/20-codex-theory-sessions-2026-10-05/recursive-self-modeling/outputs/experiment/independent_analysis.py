"""Read frozen raw results, recompute summaries; no simulator imports or edits."""
from pathlib import Path
import math, json, statistics
import numpy as np

HERE=Path(__file__).resolve().parent
z=np.load(HERE/'results/all-results.npz')
v=z['values']; metrics=list(z['metrics']); policies=list(z['policies'])
worlds=list(z['worlds']); stages=list(z['stages']); seeds=z['seeds']
selected=json.loads((HERE/'results/selected.json').read_text())
summary=json.loads((HERE/'results/summary.json').read_text())
normal=statistics.NormalDist(); crit=normal.inv_cdf(1-.05/16)
lines=[];checks=[]
def emit(s=''): lines.append(s)
def check(name,condition):
    checks.append((name,bool(condition)))
    if not condition: raise AssertionError(name)
def vals(stage,world,policy,metric):
    return v[stages.index(stage),worlds.index(world),policies.index(policy),:,metrics.index(metric)]
def mean(a):
    a=np.asarray(a);a=a[np.isfinite(a)]
    return float(a.mean()) if len(a) else math.nan
def ci(d,c=1.959963984540054):
    m=mean(d);se=float(np.std(d,ddof=1)/math.sqrt(len(d)))
    return m,se,m-c*se,m+c*se
def price(stage,world,policy,p):
    return vals(stage,world,policy,'control_loss')+vals(stage,world,policy,'sense_cost')+p*vals(stage,world,policy,'work_units')

check('dimensions',v.shape==(2,5,8,1000,20))
check('seed sequence',np.array_equal(seeds,np.arange(1000,2000)))
for r in summary['rows']:
    for m in metrics:
        actual=mean(vals(r['stage'],r['world'],r['policy'],m))
        expected=r[m]
        check('summary mean '+str((r['stage'],r['world'],r['policy'],m)),
              (expected is None and math.isnan(actual)) or (expected is not None and np.isclose(expected,actual,atol=1e-13,rtol=1e-13)))
for r in summary['contrasts']:
    d=vals(r['stage'],r['world'],r['left'],'total_loss')-vals(r['stage'],r['world'],r['right'],'total_loss')
    actual=ci(d,crit if r['kind']=='primary' else normal.inv_cdf(.975))
    for key,a in zip(['mean_difference','se','lower','upper'],actual):
        check('contrast '+str((r['stage'],r['world'],r['left'],r['right'],key)),np.isclose(a,r[key],atol=1e-13,rtol=1e-13))

emit('Independent analysis of raw held-out arrays, 5 October 2026')
emit('All numerical means and contrasts below are recomputed from all-results.npz without importing the simulator. Arrays comprise 80 cases × 1000 paired seed trajectories = 80,000 recorded policy episodes; per-case inference n=1000, not time steps. Extra exact-equivalence reruns are not independent data.')
emit('Initial hypotheses were conditional: retained calibration might improve a simple method, auditing might help bias switches, biased references might create shared failure, and nested/flat equivalence should defeat claims from labels. These hypotheses must be distinguished from the observed comparisons below.')
emit()
emit('PRIMARY contrasts: retained minus development-selected joint_y_only; negative favors retained.')
emit(f'Bonferroni normal critical value {crit:.12f}, 99.375% individual two-sided intervals; eight prespecified tests. Margin .02.')
for stage in stages:
    for world in worlds[:4]:
        baseline=selected['baselines'][stage]['selected']
        d=vals(stage,world,'retained','total_loss')-vals(stage,world,baseline,'total_loss')
        m,se,lo,hi=ci(d,crit)
        classification='benefit beyond margin' if hi<-.02 else 'harm beyond margin' if lo>.02 else 'within margin' if lo>=-.02 and hi<=.02 else 'unresolved relative to margin'
        emit(f'{stage:8s} {world:14s} delta={m:+.9f} SE={se:.9f} CI=[{lo:+.9f},{hi:+.9f}] {classification}')
emit()
emit('DESCRIPTIVE contrasts: 95% paired intervals; no multiplicity-controlled claims.')
for stage in stages:
    for world in worlds:
        for left,right in [('audit','retained'),('retained','direct'),('joint','retained'),('joint_y_only','joint')]:
            d=vals(stage,world,left,'total_loss')-vals(stage,world,right,'total_loss')
            m,se,lo,hi=ci(d)
            emit(f'{stage:8s} {world:14s} {left:12s}-{right:9s} delta={m:+.6f} CI=[{lo:+.6f},{hi:+.6f}]')
emit()
emit('PER-CASE COMPONENTS: means across seed clusters. Coverage target is .90. NPE target of 1 requires correctly specified conditional mean/variance; approximate forecasts need not satisfy it.')
emit('stage world policy | total control state effort senses work | estimateMSE forecastMSE Brier coverage90 width90 NPE eventrate biasMSE')
for stage in stages:
    for world in worlds:
        for policy in ['raw','direct','retained','audit','joint','joint_y_only']:
            names=['total_loss','control_loss','state_loss','action_effort','sense_count','work_units','estimate_mse','forecast_mse','brier','coverage90','interval90_width','normalized_forecast_error','event_rate','bias_mse']
            emit(f'{stage} {world} {policy} | '+' '.join(f'{mean(vals(stage,world,policy,m)):.6f}' for m in names))
emit()
emit('TARGETED EXPLORATORY CHECK: matched reference_bias joint minus joint_y_only, paired95% intervals. This post-observation focus is descriptive.')
for metric in ['control_loss','estimate_mse','forecast_mse','coverage90','brier','normalized_forecast_error','interval90_width']:
    d=vals('matched','reference_bias','joint',metric)-vals('matched','reference_bias','joint_y_only',metric)
    m,se,lo,hi=ci(d)
    emit(f'{metric}: delta={m:+.9f},95%CI=[{lo:+.9f},{hi:+.9f}]')
emit('The small positive MSE differences are unresolved, while the control improvement and severe interval-undercoverage difference are clearly separated in these paired data. Brier loss improves despite interval undercoverage; these assess different properties and are also affected by control-induced event rates.')
emit()
emit('ACQUISITION COUNTS: per-seed minimum/maximum and histogram (all offered time points remain the same).')
for stage in stages:
    for world in worlds:
        for policy in ['raw','direct','retained','audit','joint','joint_y_only']:
            a=vals(stage,world,policy,'sense_count');u,n=np.unique(a,return_counts=True)
            check('sense cap '+str((stage,world,policy)),np.all(a<= (12 if stage=='matched' else 6)))
            if stage=='matched':check('fixed access '+str((world,policy)),np.all(a==12))
            emit(f'{stage} {world} {policy}: '+str(dict(zip(u.astype(int).tolist(),n.tolist()))))
emit()
emit('ACQUISITION TIMING AUDIT: independently reconstruct scalar policies from b-d+eps-eta (x cancels); no simulator import. Counts checked against every raw NPZ episode, seed1000 timing against saved full trace.')
for world in worlds:
    for policy in ['retained','audit']:
        buys=np.zeros((1000,60),dtype=bool);fasts=np.zeros_like(buys);eligible=np.zeros(1000,dtype=bool)
        for j,seed in enumerate(seeds):
            rng=np.random.default_rng(int(seed));rng.normal();b0=int(rng.choice([-1,0,1]))
            eps=rng.normal(0,.25,60);eta=rng.normal(0,.05,60)
            if world=='no_bias':b0=0
            eligible[j]=abs(b0)==1
            d=.25 if world=='reference_bias' else 0.
            switch=30 if world=='switch30' else 32 if world=='switch32' else 61
            h,ph=0.,2/3;count=0
            for t in range(60):
                if t:ph+=.0025
                if t%5 or count>=6:continue
                alpha=.2 if policy=='audit' else .5
                variance=.0625+ph
                delta=variance-(1-alpha)**2*variance-alpha**2*.0025
                cost=.02+.0001*(4 if policy=='audit' else 2)
                if .25*delta<=cost:continue
                b=-b0 if t>=switch else b0
                residual=b-d+eps[t]-eta[t]-h
                if policy=='audit' and abs(residual)>2*math.sqrt(ph+.0625+.0025):
                    alpha=1.;fasts[j,t]=True
                buys[j,t]=True;count+=1
                h=(1-alpha)*h+alpha*(b-d+eps[t]-eta[t])
                ph=(1-alpha)**2*ph+alpha**2*(.0625+.0025)
        check('reconstructed counts '+str((world,policy)),np.array_equal(buys.sum(axis=1),vals('adaptive',world,policy,'sense_count')))
        tr=np.load(HERE/f'results/trace-adaptive-{world}-{policy}.npy')
        check('reconstructed seed1000 schedule '+str((world,policy)),np.array_equal(buys[0],tr[:,-1].astype(bool)))
        times=np.arange(0,60,5)
        emit(f'{world} {policy}: purchase counts at t={times.tolist()}: {buys[:,times].sum(axis=0).tolist()}')
        if world in ['switch30','switch32']:
            emit(f'  actual-switch subset n={eligible.sum()}: purchase counts={buys[eligible][:,times].sum(axis=0).tolist()}, fast update counts={fasts[eligible][:,times].sum(axis=0).tolist()}')
emit('The retained schedule is deterministic under its covariance-only gate. Audit surprise is examined only on purchased reference packets; ordinary observations do not trigger purchase through their values. The timing sensitivity exposes a gate-observation dependency, not a general result that reflection fails at a given depth.')
emit()
emit('PRICE SENSITIVITY: fixed trajectories/policies repriced; no policy adaptation or retuning. Columns computeprice=0,.0001,.001,.01.')
for stage in stages:
    for world in worlds:
        for left,right in [('retained','joint_y_only'),('audit','retained'),('joint','retained')]:
            prices=[0.,.0001,.001,.01]
            ds=[mean(price(stage,world,left,p)-price(stage,world,right,p)) for p in prices]
            dw=mean(vals(stage,world,left,'work_units')-vals(stage,world,right,'work_units'))
            intercept=ds[0]
            be=-intercept/dw if dw else math.nan
            emit(f'{stage} {world} {left}-{right}: '+', '.join(f'{x:+.6f}' for x in ds)+f'; compute break-even={be:.9f} (nonnegative only meaningful)')
emit()
emit('RECOVERY: five consecutive post-action states within ±.2; confirm at j+5, capped at remaining horizon; transient and right-censored, not permanent recovery.')
for stage in stages:
    for world in ['switch30','switch32']:
        for policy in ['raw','direct','retained','audit','joint','joint_y_only']:
            eligible=vals(stage,world,policy,'switch_eligible').astype(bool)
            delay=vals(stage,world,policy,'recovery_delay')[eligible]
            rec=vals(stage,world,policy,'recovered')[eligible]
            emit(f'{stage} {world} {policy}: eligible={eligible.sum()}, capped_mean_delay={mean(delay):.6f}, recovered={rec.sum():.0f}/{len(rec)} ({mean(rec):.6f})')
emit()
emit('NEGATIVE CONTROL AND ACCOUNTING CHECKS')
for stage in stages:
    for world in worlds:
        base=v[stages.index(stage),worlds.index(world)]
        check('flat exact aggregate '+str((stage,world)),np.array_equal(base[policies.index('retained')],base[policies.index('flat')],equal_nan=True))
        for metric in metrics:
            if metric not in ['total_loss','work_units','work_cost']:
                check('repeat preserves '+str((stage,world,metric)),np.array_equal(vals(stage,world,'repeat',metric),vals(stage,world,'retained',metric),equal_nan=True))
        check('repeat180 '+str((stage,world)),np.all(vals(stage,world,'repeat','work_units')-vals(stage,world,'retained','work_units')==180))
        check('repeat .018 '+str((stage,world)),np.allclose(vals(stage,world,'repeat','total_loss')-vals(stage,world,'retained','total_loss'),.018,rtol=0,atol=1e-12))
for ix,metric in enumerate(metrics):
    if metric not in ['recovery_delay','recovered']:check('finite '+metric,np.isfinite(v[...,ix]).all())
check('control accounting',np.allclose(v[...,metrics.index('control_loss')],v[...,metrics.index('state_loss')]+.05*v[...,metrics.index('action_effort')],atol=1e-12,rtol=0))
check('total accounting',np.allclose(v[...,metrics.index('total_loss')],v[...,metrics.index('control_loss')]+v[...,metrics.index('sense_cost')]+v[...,metrics.index('work_cost')],atol=1e-12,rtol=0))
check('sense accounting',np.allclose(v[...,metrics.index('sense_cost')],.02*v[...,metrics.index('sense_count')],atol=1e-12,rtol=0))
check('work accounting',np.allclose(v[...,metrics.index('work_cost')],.0001*v[...,metrics.index('work_units')],atol=1e-12,rtol=0))
emit('All raw arrays retained=flat including seed-level metrics, with identical documented budget/cost. Per-step equality for all seeds is in evaluator assertion; independently checked saved seed1000 traces below.')
for stage in stages:
    for world in worlds:
        r=np.load(HERE/f'results/trace-{stage}-{world}-retained.npy')
        f=np.load(HERE/f'results/trace-{stage}-{world}-flat.npy')
        check('saved trace equality '+str((stage,world)),np.array_equal(r,f,equal_nan=True))
emit('Repeat behavior equals retained, adds exactly 180 work units and .018 net loss per episode at the chosen price.')
emit(f'{len(checks)} independent numerical assertions passed, including {len(summary["rows"])} rows, {len(summary["contrasts"])} paired contrasts, component accounting, caps and negative controls. These are software checks, not independent experiments.')
emit()
emit('Interpretation limits: matched means equal paid opportunities, including forced reference packets discarded by joint_y_only. Adaptive stage changes acquisition choices and actual spending. Brier comparisons can reflect control-induced event frequencies, so pair them with pre-action estimate MSE, interval coverage/width, and NPE. Repricing cannot establish performance of retrained or price-aware policies. Monte Carlo uncertainty does not quantify model adequacy for minds or real systems. No evidence here establishes unique hierarchy, consciousness, wisdom, or ethical legitimacy.')
emit()
emit('INTERPRETIVE FINDINGS (observed after freeze)')
emit('1. Retention beats the immediate-reference controller in biased worlds, yet loses every prespecified primary comparison with joint_y_only. The original claim of conditional usefulness relative to a weak immediate comparator survives; a stronger claim that retention was the best frozen approach is rejected. joint_y_only retains its own joint state and bias, so it is not a no-memory or necessarily non-meta comparator.')
emit('2. Faster transient recovery does not imply lower full-horizon loss. With forced references, audit switch30 recovers in capped mean13.407 steps versus22.035 for retained, but has total loss4.721 versus4.555; its exploratory paired difference is +.166 [+.098,+.234].')
emit('3. The adaptive switch30 audit advantage is timing-sensitive: audit7.182 versusretained16.566, but the switch32 control produces audit27.523 versusretained13.985. These were two prespecified timing cases, not representative samples from a timing distribution. The mechanism includes unavailable residual checks between purchases and long gaps caused by the covariance-only gate.')
emit('4. Biased-reference joint filtering achieves better control than joint_y_only (1.020496 versus1.162361) while state-estimation MSE is similar (.024795 versus.024304; paired95% difference interval[-.000873,.001856]) and nominal90% coverage is much worse (.532433 versus.899283). Width shrinks to.238035 from.357634 and normalized error rises to3.873828 from1.000579. Thus low control loss does not demonstrate well-calibrated uncertainty. The small positive observed MSE difference does not establish worse estimation.')
emit('5. Costs matter without becoming empirical resource measurements. At frozen workprice0 and.001 retained still loses all eight primary mean comparisons; at.01 it beats joint_y_only in seven of eight, with adaptive switch30 still worse. This is repricing of fixed policies under a declared weighted-block convention, not proof of robustness or optimal behavior at a new price.')
(HERE/'independent-analysis.txt').write_text('\n'.join(lines)+'\n')
print('\n'.join(lines[:15]));print(f'\nAssertions passed: {len(checks)}')
