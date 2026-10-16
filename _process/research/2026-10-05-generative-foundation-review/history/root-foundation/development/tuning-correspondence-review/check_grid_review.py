"""Independent stdlib search/replay. No author-module import, no hardware/solver."""
from pathlib import Path
import csv,hashlib,json,math,datetime
OUT=Path(__file__).resolve().parent;ROOT=next(p for p in OUT.parents if (p/'RESEARCH.md').is_file());EXP=ROOT/'experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
f=json.loads((EXP/'tuning-model.json').read_text());expected=json.loads((EXP/'tuning-results.json').read_text());reference=json.loads((EXP/'tuning-reference-check.json').read_text());physical=json.loads((EXP/'tclab-results.json').read_text())
assert expected['fit_sha256']==sha(EXP/'tuning-model.json');assert expected['producer_sha256']==sha(EXP/'analyze_tuning.py');assert f['producer_sha256']==sha(EXP/'fit_tuning_model.py');assert f['solver_log_sha256']==sha(EXP/'tuning-fit-log.txt')
a0,a1=(r[0] for r in f['parameters']['a']);b0,b1=(r[0] for r in f['parameters']['b'][0]);c=f['parameters']['c'][0]
def load(path):
 with (ROOT/path).open() as stream:return [{k:float(v) for k,v in row.items()} for row in csv.DictReader(stream)]
rows=load(f['training_source']);n=len(rows);assert n==599

def open_loop(rows,gamma=1.,intercept=c):
 states=[rows[0]['T1'],rows[1]['T1']]
 for k in range(2,len(rows)):
  states.append(a0*states[-1]+a1*states[-2]+gamma*(b0*rows[k-1]['Q1']+b1*rows[k-2]['Q1'])+intercept)
 return states

def simulate(offset,kp,tau,gamma,recorded):
 # Independently retain unweighted integrated error. Residual affects readout only.
 old=new=c/(1-a0-a1);previous_q=0.;reading=rows[0]['T1'];sum_error=0.;ys=[];qs=[];mem=[]
 for k,row in enumerate(rows):
  dt=row['Time']-rows[k-1]['Time'] if recorded and k>0 else 1.
  e=row['TSP1']-reading;proposed=sum_error+e*dt;raw=kp*e+(kp/tau)*proposed
  q=sorted([0.,raw,100.])[1]
  if 0<=raw<=100:sum_error=proposed
  ys.append(reading);qs.append(q);mem.append((kp/tau)*sum_error)
  next_=a0*new+a1*old+gamma*(b0*q+b1*previous_q)+c;old,new,previous_q=new,next_,q
  if k+1<n:reading=next_+offset[k+1]
 track=math.fsum(abs(row['TSP1']-value) for row,value in zip(rows,ys));motion=math.fsum(abs(qs[k]-qs[k-1]) for k in range(1,n));signed=qs[-1]-qs[0]
 return {'Kc':float(kp),'tauI_seconds':float(tau),'signed_objective':(track+signed/2)/n,'absolute_objective':(track+motion/2)/n,'mean_absolute_tracking':track/n,'mean_absolute_movement':motion/n,'temperature':ys,'commands':qs,'integral':mem}

def close(a,b,tol=2e-7):assert abs(a-b)<tol,(a,b,tol)
def compare_metrics(actual,want):
 for k,v in actual.items():close(v,want[k])
def describe(es):
 return {'rmse_celsius':math.sqrt(math.fsum(e*e for e in es)/len(es)),'mae_celsius':math.fsum(abs(e) for e in es)/len(es),'max_abs_celsius':max(abs(e) for e in es)}
base_res=[row[0] for row in f['training_output_residual']];obs=[r['T1'] for r in rows]
specs=[('archived_contract',1.,base_res,False),('recorded_intervals',1.,base_res,True),('no_residual_transfer',1.,[0.]*n,False)]
for gamma in (.8,1.,1.2):specs.append((f'compensated_gain_{gamma:g}',gamma,[o-p for o,p in zip(obs,open_loop(rows,gamma))],False))
comparisons=[];trajectory_diffs=[];grid=[(kp,tau) for tau in range(5,81,5) for kp in range(5,81,5)]
for (label,gamma,offset,recorded),want in zip(specs,expected['scenarios']):
 assert label==want['label'];assert len(want['scores'])==256
 assert max(abs(a-b) for a,b in zip(offset,want['residual']))<1e-10
 runs=[simulate(offset,kp,tau,gamma,recorded) for kp,tau in grid]
 for actual,score in zip(runs,want['scores']):
  for key,value in score.items():close(actual[key],value)
 def winner(metric):
  best=None
  for index,r in enumerate(runs):
   if best is None or r[metric]<=runs[best][metric]:best=index
  return best
 best={}
 for metric in ['signed_objective','absolute_objective']:
  ix=winner(metric);assert ix==want['best'][metric]['index'];gap=sorted(r[metric] for r in runs)[1]-runs[ix][metric];close(gap,want['best'][metric]['runner_up_gap']);best[metric]={'index':ix,'gains':grid[ix],'value':runs[ix][metric],'runner_up_gap':gap}
 reverse=0;strict=0
 for i in range(256):
  for j in range(i):
   first=runs[i]['signed_objective']-runs[j]['signed_objective'];second=runs[i]['absolute_objective']-runs[j]['absolute_objective']
   if first!=0 and second!=0:strict+=1;reverse+=int(first*second<0)
 assert reverse==want['pairwise_ranking_reversals'] and strict==want['strict_pairs']
 chosen=[]
 for target in want['selected_trajectories']:
  actual=runs[target['grid_index']];diffs={key:max(abs(a-b) for a,b in zip(actual[key],target[key])) for key in ['temperature','commands','integral']};assert max(diffs.values())<2e-6,diffs
  chosen.append(dict(actual,grid_index=target['grid_index']));trajectory_diffs.append({'label':label,'grid_index':target['grid_index'],'max_differences':diffs})
 training_error=max(abs(p+d-o) for p,d,o in zip(open_loop(rows,gamma),offset,obs));close(training_error,want['training_reconstruction_max_abs_error'])
 excess=runs[winner('signed_objective')]['absolute_objective']-runs[winner('absolute_objective')]['absolute_objective'];close(excess,want['absolute_excess_from_wrong_objective'])
 comparisons.append({'label':label,'best':best,'reversals':reverse,'strict_pairs':strict,'training_reconstruction_error':training_error,'wrong_objective_excess':excess,'scores':[{k:v for k,v in r.items() if not isinstance(v,list)} for r in runs],'selected_trajectories':chosen})
validation=[];diagnostics=[]
for source,want,diag in zip(physical['physical_runs'][1:],expected['validation'],reference['runs']):
 data=load(source['path']);assert sha(ROOT/source['path'])==want['sha256'];truth=[r['T1'] for r in data];prediction=open_loop(data);assert max(abs(a-b) for a,b in zip(prediction,want['predicted_temperature']))<1e-10
 bare=describe([p-y for p,y in zip(prediction[2:],truth[2:])]);transferred=describe([p+d-y for p,d,y in zip(prediction[2:],base_res[2:],truth[2:])]);compare_metrics(bare,want['without_transferred_residual']);compare_metrics(transferred,want['with_initial_run_residual'])
 delta=data[0]['T1']-rows[0]['T1'];changed=c+delta*(1-a0-a1);shifted=open_loop(data,intercept=changed)
 bare_shift=describe([p-y for p,y in zip(shifted[2:],truth[2:])]);transfer_shift=describe([p+d-y for p,d,y in zip(shifted[2:],base_res[2:],truth[2:])]);compare_metrics(bare_shift,diag['without_transferred_residual']);compare_metrics(transfer_shift,diag['with_initial_run_residual']);close(changed,diag['adjusted_intercept'])
 validation.append({'label':source['label'],'without':bare,'with':transferred});diagnostics.append({'label':source['label'],'without':bare_shift,'with':transfer_shift,'adjusted_intercept':changed})
agreement=describe([p-y[0] for p,y in zip(open_loop(rows),f['predicted_training'])]);compare_metrics(agreement,expected['fit_recurrence_numerical_agreement'])
receipt={'status':'passed','checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'script_sha256':sha(Path(__file__)),'fit_sha256':sha(EXP/'tuning-model.json'),'results_sha256':sha(EXP/'tuning-results.json'),'reference_sha256':sha(EXP/'tuning-reference-check.json'),'producer_sha256':sha(EXP/'analyze_tuning.py'),'candidate_count':1536,'fit_prediction_agreement':agreement,'initialization':{'stationary_latent':c/(1-a0-a1),'training_first_two':[rows[0]['T1'],rows[1]['T1']],'first_target':rows[0]['TSP1'],'first_recorded_command':rows[0]['Q1']},'scenarios':comparisons,'selected_trajectory_differences':trajectory_diffs,'validation':validation,'posthoc_initial_reference':diagnostics,'scope':'Independent stdlib reconstruction of all6x256 model candidates, all retained selected trajectories, actual-input validation and posthoc diagnostic. Unweighted PI error memory, fsum metrics. No physical counterfactual or future calibration claimed.'}
(OUT/'grid-verification.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'status':'passed','candidates':1536,'scenarios':[{k:s[k] for k in ['label','best','reversals','strict_pairs','wrong_objective_excess']} for s in comparisons],'max_selected_trajectory_difference':max(max(r['max_differences'].values()) for r in trajectory_diffs),'validation':validation,'diagnostics':diagnostics},indent=2))
