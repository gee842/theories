"""Freeze -> local calibration -> freeze predictions -> held-out execution -> audit.

Usage: python experiment.py freeze|calibrate|evaluate|audit|report
Requires numpy. Run from this directory. No network or external services are used.
"""
import csv
import hashlib
import json
import pathlib
import sys
import time
from datetime import datetime, timezone
import numpy as np
import service
import queue_model

ROOT = pathlib.Path(__file__).resolve().parent
N_CAL = 65536
N_TARGET = 1024
N_BOOT = 20000
TOLERANCE = .075
CODE_FILES = ('protocol.md','service.py','queue_model.py','experiment.py','audit.py')

def now(): return datetime.now(timezone.utc).isoformat()
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def write(name, data): (ROOT/name).write_text(json.dumps(data, indent=2, sort_keys=True)+'\n')
def read(name): return json.loads((ROOT/name).read_text())
def rng(namespace, regime, arm=0): return np.random.default_rng(np.random.SeedSequence([namespace,regime,arm]))
def manifest(): return {name:digest(ROOT/name) for name in CODE_FILES}
def integrity():
    saved = read('freeze.json')
    assert saved['files'] == manifest(), 'Frozen source changed. Preserve evidence and declare amendment.'
    return saved

def freeze():
    assert not (ROOT/'freeze.json').exists(), 'Do not overwrite the first freeze.'
    write('freeze.json',dict(utc=now(),files=manifest(),state='before calibration and integrated target execution'))
    print('Source and protocol frozen.',flush=True)

def calibrate():
    integrity()
    assert not (ROOT/'calibration.json').exists()
    all_results=[]
    for i,r in enumerate(service.REGIMES):
        start=time.monotonic()
        primitive=list(service.sample_shocks(rng(11001,i),r,N_CAL))
        params=dict(backlog=[sum(s['backlog']==v for s in primitive)/N_CAL for v in service.BACKLOG],
                    arrival=sum(sum(s['bursts']) for s in primitive)/(N_CAL*5),
                    diag=[sum(s['diag_duration']==v for s in primitive)/N_CAL for v in service.DIAG],
                    correct=sum(s['correct'] for s in primitive)/N_CAL,
                    deploy=[sum(s['deploy_duration']==v for s in primitive)/N_CAL for v in service.DEPLOY],
                    effective=sum(s['effective'] for s in primitive)/N_CAL)
        p=[]; p_counts=[]; hist=[]
        for f in (0,1):
            counts={}
            for s in service.sample_shocks(rng(22002,i,f),r,N_CAL):
                result=service.run(r,s,finance=f,mode='diag')
                if result['valid_gate']:
                    t=result['proposal_time']
                    counts[t]=counts.get(t,0)+1
            successes=sum(counts.values())
            assert successes>0, 'Undefined proposal timing calibration.'
            p_counts.append(successes); p.append(successes/N_CAL); hist.append(counts)
        timing={}
        for f in (0,1):
            for t,c in hist[f].items(): timing[t]=timing.get(t,0)+.5*c/p_counts[f]
        times=sorted(timing)
        q=[];q_counts=[]
        for a in (0,1):
            local_rng=rng(33003,i,a)
            inject_times=local_rng.choice(times,size=N_CAL,p=[timing[t] for t in times])
            count=0
            for j,s in enumerate(service.sample_shocks(local_rng,r,N_CAL)):
                count+=service.run(r,s,authority=a,mode='enact',inject_time=int(inject_times[j]))['recovered']
            q_counts.append(count);q.append(count/N_CAL)
        transported=[p[f]*q[a] for f in (0,1) for a in (0,1)]
        domain=queue_model.integrated_rates(r,params)
        all_results.append(dict(regime=r['name'],p=p,q=q,p_counts=p_counts,q_counts=q_counts,
                                proposal_histograms=hist,timing=timing,primitive_params=params,
                                transported=transported,domain=domain,
                                aggregate=[sum(transported)/4]*4,
                                fixed_diagnostic=[p[0]*q[a] for f in (0,1) for a in (0,1)],
                                seconds=time.monotonic()-start))
        print('Completed independent local calibration:',r['name'],flush=True)
    write('calibration.json',dict(utc=now(),n_per_local_arm=N_CAL,cell_order=['f0a0','f0a1','f1a0','f1a1'],regimes=all_results))
    write('prediction-freeze.json',dict(utc=now(),source_freeze_sha256=digest(ROOT/'freeze.json'),
                                      calibration_sha256=digest(ROOT/'calibration.json'),
                                      state='predictions frozen before target evaluation'))
    print('All predictions frozen; target integrated run has not started.',flush=True)

def evaluate():
    integrity()
    pred_freeze=read('prediction-freeze.json')
    assert pred_freeze['calibration_sha256']==digest(ROOT/'calibration.json')
    assert not (ROOT/'target.json').exists()
    records=[]
    for i,r in enumerate(service.REGIMES):
        seeds=[]
        for seed,s in enumerate(service.sample_shocks(rng(44004,i),r,N_TARGET)):
            outcomes=[service.run(r,s,finance=f,authority=a) for f in (0,1) for a in (0,1)]
            seeds.append(dict(cluster=seed,shock=s,outcomes=outcomes))
        records.append(dict(regime=r['name'],seeds=seeds))
        print('Completed 1,024 paired target clusters:',r['name'],flush=True)
    write('target.json',dict(utc=now(),prediction_freeze_sha256=digest(ROOT/'prediction-freeze.json'),
                            n_clusters_per_regime=N_TARGET,regimes=records))

def parameters_to_vector(p):
    return np.array([p['backlog'][0],p['backlog'][1],p['arrival'],p['diag'][0],p['diag'][1],p['correct'],p['deploy'][0],p['effective']])

def vector_to_parameters(x):
    return dict(backlog=[x[0],x[1],1-x[0]-x[1]],arrival=x[2],diag=[x[3],x[4],1-x[3]-x[4]],correct=x[5],deploy=[x[6],1-x[6]],effective=x[7])

def domain_covariance(r,p):
    x=parameters_to_vector(p)
    cov=np.zeros((8,8))
    for indices,values in (([0,1],x[[0,1]]),([3,4],x[[3,4]])):
        block=(np.diag(values)-np.outer(values,values))/N_CAL
        cov[np.ix_(indices,indices)]=block
    for j in (2,5,6,7): cov[j,j]=x[j]*(1-x[j])/(N_CAL*5 if j==2 else N_CAL)
    jac=np.zeros((4,8));epsilon=1e-5
    for j in range(8):
        upper=x.copy();lower=x.copy();upper[j]+=epsilon;lower[j]-=epsilon
        jac[:,j]=(np.array(queue_model.integrated_rates(r,vector_to_parameters(upper)))-np.array(queue_model.integrated_rates(r,vector_to_parameters(lower))))/(2*epsilon)
    return jac@cov@jac.T

def bootstrap_target(outcomes,generator):
    y=np.array(outcomes,dtype=float)
    codes=(y.astype(int)*np.array([1,2,4,8])).sum(axis=1)
    counts=np.bincount(codes,minlength=16)
    patterns=np.array([[(j>>k)&1 for k in range(4)] for j in range(16)])
    sample=generator.multinomial(N_TARGET,counts/N_TARGET,size=N_BOOT)
    return sample@patterns/N_TARGET

def classify(residuals,halfwidth):
    lo=np.array(residuals)-halfwidth;hi=np.array(residuals)+halfwidth
    equivalent=bool(np.all(lo>=-TOLERANCE) and np.all(hi<=TOLERANCE))
    rejected=bool(np.any(lo>TOLERANCE) or np.any(hi<-TOLERANCE))
    return dict(status='equivalent' if equivalent else 'rejected' if rejected else 'inconclusive',
                intervals=[[float(a),float(b)] for a,b in zip(lo,hi)],
                exact_agreement_rejected=bool(np.any(lo>0) or np.any(hi<0)))

def report():
    integrity()
    cal=read('calibration.json');target=read('target.json');audit_data=read('audit-results.json')
    simulations=[];domain_simulations=[];interaction_simulations=[];partial=[]
    contrast=np.array([1,-1,-1,1])
    for i,(r,c,t) in enumerate(zip(service.REGIMES,cal['regimes'],target['regimes'])):
        y=np.array([[o['recovered'] for o in s['outcomes']] for s in t['seeds']],float)
        observed=y.mean(axis=0)
        random=rng(55005,i)
        outcome_boot=bootstrap_target(y,random)
        ps=np.column_stack([random.binomial(N_CAL,p,size=N_BOOT)/N_CAL for p in c['p']])
        qs=np.column_stack([random.binomial(N_CAL,q,size=N_BOOT)/N_CAL for q in c['q']])
        pred_boot=np.column_stack([ps[:,f]*qs[:,a] for f in (0,1) for a in (0,1)])
        residual=observed-np.array(c['transported'])
        simulations.append(outcome_boot-pred_boot-residual)
        dnoise=random.multivariate_normal(np.zeros(4),domain_covariance(r,c['primitive_params']),size=N_BOOT,check_valid='raise')
        domain_simulations.append(outcome_boot-observed-dnoise)
        interaction_simulations.append((outcome_boot-pred_boot-residual)@contrast)
        secondary=[]
        for j in range(4):
            outs=[s['outcomes'][j] for s in t['seeds']]
            times=[o['recovery_time'] for o in outs if o['recovered']]
            secondary.append(dict(mean_spending=sum(o['spent'] for o in outs)/N_TARGET,
                                  mean_good_responses=sum(o['good_responses'] for o in outs)/N_TARGET,
                                  mean_deadline_misses=sum(o['deadline_misses'] for o in outs)/N_TARGET,
                                  mean_recovery_time_conditional=float(np.mean(times)) if times else None))
        partial.append(dict(regime=r['name'],observed=observed.tolist(),
                            observed_interaction=float(observed@contrast),
                            predicted_interaction=float(np.array(c['transported'])@contrast),
                            conditional_repair_by_finance=[float(y[:,2*f+1].sum()/sum(s['outcomes'][2*f+1]['valid_gate'] for s in t['seeds'])) for f in (0,1)],
                            secondary=secondary))
    primary_hw=float(np.quantile(np.max(np.abs(np.concatenate(simulations,axis=1)),axis=1),.95,method='higher'))
    domain_hw=float(np.quantile(np.max(np.abs(np.concatenate(domain_simulations,axis=1)),axis=1),.95,method='higher'))
    interaction_hw=float(np.quantile(np.max(np.abs(np.column_stack(interaction_simulations)),axis=1),.95,method='higher'))
    rows=[]
    for i,(p,c) in enumerate(zip(partial,cal['regimes'])):
        p['models']={}
        for model in ('transported','domain','aggregate','fixed_diagnostic'):
            pred=np.array(c[model]);obs=np.array(p['observed']);resid=obs-pred
            item=dict(prediction=pred.tolist(),residual=resid.tolist(),max_absolute_error=float(np.max(np.abs(resid))),mean_squared_error=float(np.mean(resid**2)))
            if model in ('transported','domain'): item.update(classify(resid,primary_hw if model=='transported' else domain_hw))
            p['models'][model]=item
        delta=p['observed_interaction']-p['predicted_interaction']
        p['interaction_residual']=delta
        p['interaction_residual_interval']=[delta-interaction_hw,delta+interaction_hw]
        rows.append(p)
    result=dict(utc=now(),n_target=N_TARGET,n_cal=N_CAL,n_boot=N_BOOT,practical_tolerance=TOLERANCE,
                simultaneous_halfwidth=primary_hw,domain_halfwidth=domain_hw,interaction_halfwidth=interaction_hw,
                uncertainty='Nominal cluster-bootstrap bands, conditional on calibrated proposal mixing distribution; domain component calibration uses first-order Gaussian delta propagation.',
                source_freeze_sha256=digest(ROOT/'freeze.json'),prediction_freeze_sha256=digest(ROOT/'prediction-freeze.json'),
                target_sha256=digest(ROOT/'target.json'),regimes=rows,audit=audit_data)
    write('results.json',result)
    lines=['# Frozen transfer test: queued software service','',
           'Constructed runnable software/simulator evidence; no people or observed production system. All source, mapping and decisions were frozen before calibration, and all predictions were frozen before 1,024 paired held-out seed clusters per regime.','',
           'The transported predictor remains exactly `R[f,a] = p[f] * q[a]`. The serious comparison is an independently implemented FIFO departure-time model, using separately measured primitive component distributions. Both receive local calibration, neither sees held-out integrated recovery before its prediction freeze.','',
           '| Regime | Transport max error | Transport decision | Queue model max error | Queue model decision |','|---|---:|---|---:|---|']
    for row in rows:
        m=row['models'];lines.append(f"| {row['regime']} | {m['transported']['max_absolute_error']:.4f} | {m['transported']['status']} | {m['domain']['max_absolute_error']:.4f} | {m['domain']['status']} |")
    lines+=['',f'Practical tolerance: ±{TOLERANCE:.3f}. Simultaneous nominal 95% band half-width over all 12 primary cell residuals: {primary_hw:.4f}; domain model: {domain_hw:.4f}. Exact-agreement rejection and full intervals are in results.json. Equivalence requires every interval to fit inside the tolerance; rejection requires an interval wholly outside it.','',
            '| Regime/cell | Frozen p×q | Frozen queue model | Observed recovery | p×q residual |','|---|---:|---:|---:|---:|']
    for row in rows:
        for j,label in enumerate(cal['cell_order']):
            lines.append(f"| {row['regime']} / {label} | {row['models']['transported']['prediction'][j]:.4f} | {row['models']['domain']['prediction'][j]:.4f} | {row['observed'][j]:.4f} | {row['models']['transported']['residual'][j]:+.4f} |")
    lines+=['','| Regime | Predicted interaction | Observed interaction | Residual simultaneous interval |','|---|---:|---:|---|']
    for row in rows:
        lo,hi=row['interaction_residual_interval'];lines.append(f"| {row['regime']} | {row['predicted_interaction']:.4f} | {row['observed_interaction']:.4f} | [{lo:+.4f}, {hi:+.4f}] |")
    lines+=['','## Interpretation','',
            'The reserved/batched control satisfies the source factorization assumptions by construction; its agreement is a sanity check, not discovery. The shared-worker regimes probe the candidate bridge: diagnosis timing and its correlation with backlog change which deployment can finish before the deadline. A pooled scalar q measured on standardized local recommendations can discard those distinctions. Failure rejects this registered transport application. It does not refute the conditional probability identity, and adding queue state afterward would be a new model. The original predictions are retained unmodified.','',
            'The domain model has eight fitted primitive probabilities per regime plus explicit queue/clock rules. The transported predictor has four displayed gate probabilities but also needs proposal-timing histograms for calibration; those histograms and supplied scheduling rules are not free information. No explanatory compression or new fundamental law is established by this experiment.','',
            'p used diagnosis-only trials. q used enactment-only trials with a forced correct recommendation at a release time from the balanced pooled p-trial timing distribution, and a fresh independently generated workload. There is no diagnostic job in q calibration. This deliberately frozen bridge preserves timing marginals but discards diagnosis-induced backlog and time/backlog dependence. Consequently the confidence analysis conditions on that measured mixing distribution.','',
            'The bootstrap treats each four-cell outcome vector as one cluster. Bands are nominal, not an exact finite-sample coverage theorem; domain calibration uses a first-order delta approximation. Exhaustive finite-law checking below independently resolves structural discrepancies without relying on those sampling approximations.','',
            '## Independent checks','',
            f"The object/worker target and independent FIFO-time recurrence agreed on {audit_data['path_checks']:,} enumerated paths. Audit status: {audit_data['status']}. The audit also checks accounting, inclusive deadlines, authority exclusion from diagnosis, and exact primitive probability mass. It was run after held-out evaluation. No source edits occurred after freeze.",'',
            '| Regime | Oracle p×q max discrepancy from true integrated software law |','|---|---:|']
    for row in audit_data['oracle']:
        lines.append(f"| {row['regime']} | {row['max_factorization_error']:.10f} |")
    lines+=['','These oracle calculations are predeclared checks of the constructed program, not fitted replacements for the frozen predictions. The deadline-miss, good-response, spending, and conditional recovery-time outcomes are recorded separately in results.json.','',
            '## Reproduce','',
            'Use Python 3 with numpy. In a fresh copy containing only protocol.md, service.py, queue_model.py, experiment.py and audit.py, run:', '',
            '```text','python experiment.py freeze','python experiment.py calibrate','python experiment.py evaluate','python experiment.py audit','python experiment.py report','```','',
            'SHA-256 records: freeze.json and prediction-freeze.json. Raw independent local estimates: calibration.json. Per-cluster primitive shocks and all intervention outcomes: target.json. Audit details: audit-results.json. All numerical summaries: results.json. Source protocol paths and their assumptions are recorded in protocol.md.']
    (ROOT/'RESULTS.md').write_text('\n'.join(lines)+'\n')
    print('Results and all uncertainty bands saved.',flush=True)

if __name__=='__main__':
    command=sys.argv[1]
    if command=='audit':
        integrity()
        assert (ROOT/'target.json').exists(), 'Oracle audit is post-evaluation only.'
        import audit
        audit.run()
    else:
        {'freeze':freeze,'calibrate':calibrate,'evaluate':evaluate,'report':report}[command]()
