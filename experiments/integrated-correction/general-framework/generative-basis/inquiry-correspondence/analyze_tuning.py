#!/usr/bin/env python3
"""Finite numerical tuning and held-out residual-transfer checks.
The objective correction is explicit. All candidate temperatures are model
outputs, never relabeled physical observations. No hardware or upstream execution.
"""
from pathlib import Path
import csv,hashlib,json,math,sys
import numpy as np
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(path):
    with path.open() as f:return [{k:float(v) for k,v in r.items()} for r in csv.DictReader(f)]
def describe(errors):
    e=np.asarray(errors);return {'rmse_celsius':float(np.sqrt(np.mean(e*e))),'mae_celsius':float(np.mean(np.abs(e))),'max_abs_celsius':float(np.max(np.abs(e)))}

def plant_inputs(rows,a,b,c,gamma=1.0):
    # Same first two measured states as sysid. Subsequent states use only the
    # input record and recursion, never later measured temperatures.
    x=[rows[0]['T1'],rows[1]['T1']]
    for k in range(2,len(rows)):
        x.append(a[0]*x[k-1]+a[1]*x[k-2]+gamma*(b[0]*rows[k-1]['Q1']+b[1]*rows[k-2]['Q1'])+c)
    return np.asarray(x)

def simulate(rows,a,b,c,residual,kc,ti,gamma=1.0,actual_intervals=False):
    n=len(rows);latent=c/(1-a[0]-a[1]);prior=latent;prior_q=0.0
    reading=rows[0]['T1'];integral=0.0;temperature=[];commands=[];memories=[]
    for k,row in enumerate(rows):
        dt=rows[k]['Time']-rows[k-1]['Time'] if actual_intervals and k else 1.0
        error=row['TSP1']-reading;addition=(kc/ti)*error*dt
        integral+=addition;raw=kc*error+integral;command=max(0.0,min(100.0,raw))
        if raw<0 or raw>100:integral-=addition
        temperature.append(reading);commands.append(command);memories.append(integral)
        next_latent=a[0]*latent+a[1]*prior+gamma*(b[0]*command+b[1]*prior_q)+c
        if k+1<n:reading=next_latent+residual[k+1]
        prior,latent,prior_q=latent,next_latent,command
    assert all(math.isfinite(x) for x in temperature+commands+memories)
    tracking=sum(abs(r['TSP1']-v) for r,v in zip(rows,temperature))
    signed=sum(v-u for u,v in zip(commands,commands[1:]));absolute=sum(abs(v-u) for u,v in zip(commands,commands[1:]))
    return {'Kc':kc,'tauI_seconds':ti,'signed_objective':(tracking+.5*signed)/n,
      'absolute_objective':(tracking+.5*absolute)/n,'mean_absolute_tracking':tracking/n,'mean_absolute_movement':absolute/n,
      'temperature':temperature,'commands':commands,'integral':memories}

def main():
    path=HERE/'tuning-model.json';fit=json.loads(path.read_text())
    assert fit['status']=='passed' and fit['producer_sha256']==sha(HERE/'fit_tuning_model.py')
    rows=load(ROOT/fit['training_source']);assert sha(ROOT/fit['training_source'])==fit['training_sha256']
    a=[r[0] for r in fit['parameters']['a']];b=[r[0] for r in fit['parameters']['b'][0]];c=fit['parameters']['c'][0]
    observed=np.array([r['T1'] for r in rows]);residual=np.array(fit['training_output_residual'])[:,0]
    forward=plant_inputs(rows,a,b,c)
    equivalence=describe(forward-np.array(fit['predicted_training'])[:,0])
    specs=[('archived_contract',1.0,residual,False),('recorded_intervals',1.0,residual,True),('no_residual_transfer',1.0,np.zeros(len(rows)),False)]
    for gamma in [.8,1.0,1.2]:
        specs.append((f'compensated_gain_{gamma:g}',gamma,observed-plant_inputs(rows,a,b,c,gamma),False))
    scenarios=[]
    grid=[(float(kc),float(ti)) for ti in range(5,81,5) for kc in range(5,81,5)]
    for label,gamma,offset,actual_intervals in specs:
        runs=[simulate(rows,a,b,c,offset,kc,ti,gamma,actual_intervals) for kc,ti in grid]
        # The archived loop updates on <=, hence uses the last tied grid point.
        winner=lambda metric:min(enumerate(runs),key=lambda ir:(ir[1][metric],-ir[0]))[0]
        isigned=winner('signed_objective');iabs=winner('absolute_objective')
        selected_indices=sorted({isigned,iabs,grid.index((10.,55.))})
        scores=[{k:v for k,v in r.items() if k not in ['temperature','commands','integral']} for r in runs]
        metrics=['signed_objective','absolute_objective']
        best={m:{'index':winner(m),'Kc':runs[winner(m)]['Kc'],'tauI_seconds':runs[winner(m)]['tauI_seconds'],'value':runs[winner(m)][m],
                 'runner_up_gap':sorted(r[m] for r in runs)[1]-min(r[m] for r in runs)} for m in metrics}
        ranking=0;strictpairs=0
        for j in range(len(runs)):
            for k in range(j):
                ds=runs[j]['signed_objective']-runs[k]['signed_objective'];da=runs[j]['absolute_objective']-runs[k]['absolute_objective']
                if ds and da:strictpairs+=1;ranking+=int(ds*da<0)
        scenarios.append({'label':label,'gain_multiplier':gamma,'actual_recorded_intervals_in_PI':actual_intervals,
          'residual':offset.tolist(),'candidate_count':len(runs),'best':best,
          'absolute_cost_of_signed_winner':runs[isigned]['absolute_objective'],
          'absolute_excess_from_wrong_objective':runs[isigned]['absolute_objective']-runs[iabs]['absolute_objective'],
          'pairwise_ranking_reversals':ranking,'strict_pairs':strictpairs,'scores':scores,
          'selected_trajectories':[{**runs[i],'grid_index':i} for i in selected_indices],
          'training_reconstruction_max_abs_error':float(np.max(np.abs(plant_inputs(rows,a,b,c,gamma)+offset-observed)))})
    validation=[]
    originals=json.loads((HERE/'tclab-results.json').read_text())
    for run in originals['physical_runs'][1:]:
        p=ROOT/run['path'];valid=load(p);truth=np.array([r['T1'] for r in valid]);pred=plant_inputs(valid,a,b,c)
        assert len(pred)==len(residual)
        validation.append({'label':run['label'],'source':run['path'],'sha256':sha(p),'evaluated_indices':'2 through 598 inclusive; first two measured values initialize recurrence',
          'without_transferred_residual':describe((pred-truth)[2:]),'with_initial_run_residual':describe((pred+residual-truth)[2:]),
          'predicted_temperature':pred.tolist(),'observed_temperature':truth.tolist(),
          'scope':'Uses the actually recorded validation commands and first two temperatures. No validation coefficient fitting, no altered-command physical experiment, no prospective input availability claim. Absolute model intercept retained; differing initial/ambient conditions may contribute to error.'})
    result={'status':'passed','producer_sha256':sha(Path(__file__)),'fit_sha256':sha(path),'python':sys.version,'numpy':np.__version__,
      'fit_recurrence_numerical_agreement':equivalence,'scenarios':scenarios,'validation':validation,
      'scope':'Finite numerical model comparisons over the authors 256-point gain grid. Local output-error fit, residual transfer and nominal timing are disclosed contracts. Compensated gain domains are sensitivity constructions, not calibrated physical alternatives. Corrected model minimum is not a proved real-world optimum or an ethical ordering.'}
    (HERE/'tuning-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','fit_recurrence_agreement':equivalence,
      'scenarios':[{k:s[k] for k in ['label','best','absolute_excess_from_wrong_objective','pairwise_ranking_reversals','training_reconstruction_max_abs_error']} for s in scenarios],
      'validation':[{k:v[k] for k in ['label','without_transferred_residual','with_initial_run_residual']} for v in validation]},indent=2))
if __name__=='__main__':main()
