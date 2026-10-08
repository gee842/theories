"""Independent local-only GEKKO refit and one runtime candidate. No author imports."""
from pathlib import Path
import contextlib,csv,hashlib,io,json,sys,time
import numpy as np
OUT=Path(__file__).resolve().parent;ROOT=next(p for p in OUT.parents if (p/'RESEARCH.md').is_file());EXP=ROOT/'experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence'
DEP=Path('/var/folders/h6/tw6bmgcs5txbtn4swlpkpm4w0000gn/T/tclab-tuning-deps-nyp4v3dm');sys.path.insert(0,str(DEP))
import gekko
from gekko import GEKKO
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
f=json.loads((EXP/'tuning-model.json').read_text());assert gekko.__version__=='1.3.2';assert sha(DEP/'gekko/gekko.py')==f['package_source_sha256'];assert sha(DEP/'gekko/bin/apm_mac')==f['local_solver_sha256']
with (ROOT/f['training_source']).open() as stream:rows=[{k:float(v) for k,v in r.items()} for r in csv.DictReader(stream)]
assert sha(ROOT/f['training_source'])==f['training_sha256']
t=np.array([r['Time'] for r in rows]);u=np.array([[r['Q1'],r['Q2']] for r in rows]);y=np.array([[r['T1'],r['T2']] for r in rows]);log=io.StringIO();start=time.monotonic();model=GEKKO(remote=False)
try:
 with contextlib.redirect_stdout(log),contextlib.redirect_stderr(log):
  predictions,params,gains=model.sysid(t,u,y,na=2,nb=2,objf=10000,shift='init',scale=False,diaglevel=1,pred='model')
finally:model.cleanup()
(OUT/'fit-log.txt').write_text(log.getvalue());fit_time=time.monotonic()-start
diffs={k:float(np.max(np.abs(np.asarray(v)-np.asarray(f['parameters'][k])))) for k,v in params.items()};assert max(diffs.values())<1e-8
pdiff=float(np.max(np.abs(predictions-np.array(f['predicted_training']))));assert pdiff<1e-6
fit_record={'parameters':{k:np.asarray(v).tolist() for k,v in params.items()},'predictions':predictions.tolist(),'gains':np.asarray(gains).tolist(),'max_parameter_differences':diffs,'max_training_prediction_difference':pdiff,'elapsed_seconds':fit_time}
# Runtime uses frozen author coefficients to isolate ARX realization from refitting.
m=GEKKO(remote=False);runtime_log=io.StringIO();start=time.monotonic();kc=10.;ti=55.;acc=0.;readings=[rows[0]['T1']];commands=[]
try:
 with contextlib.redirect_stdout(runtime_log),contextlib.redirect_stderr(runtime_log):
  output,input_=m.arx({k:np.array(v) for k,v in f['parameters'].items()});m.time=[0,1];m.options.IMODE=1;m.solve(disp=False);m.options.IMODE=4;m.solve(disp=False)
  for k,row in enumerate(rows):
   err=row['TSP1']-readings[-1];trial=acc+err;raw=kc*err+(kc/ti)*trial;q=min(100.,max(0.,raw))
   if 0<=raw<=100:acc=trial
   commands.append(q);input_[0].value=q;m.solve(disp=False)
   if k+1<len(rows):readings.append(float(output[0].value[-1])+f['training_output_residual'][k+1][0])
finally:m.cleanup()
(OUT/'runtime-log.txt').write_text(runtime_log.getvalue());duration=time.monotonic()-start
result=json.loads((EXP/'tuning-results.json').read_text());direct=next(v for v in result['scenarios'][0]['selected_trajectories'] if v['Kc']==kc and v['tauI_seconds']==ti)
tracking=sum(abs(row['TSP1']-x) for row,x in zip(rows,readings));moves=[b-a for a,b in zip(commands,commands[1:])];obj=(tracking+.5*sum(map(abs,moves)))/len(rows);signed=(tracking+.5*(commands[-1]-commands[0]))/len(rows)
tdiff=max(abs(a-b) for a,b in zip(readings,direct['temperature']));qdiff=max(abs(a-b) for a,b in zip(commands,direct['commands']));assert tdiff<1e-5 and qdiff<1e-4
record={'status':'passed','review_script_sha256':sha(Path(__file__)),'fit_sha256':sha(EXP/'tuning-model.json'),'results_sha256':sha(EXP/'tuning-results.json'),'gekko':gekko.__version__,'package_sha256':sha(DEP/'gekko/gekko.py'),'solver_sha256':sha(DEP/'gekko/bin/apm_mac'),'remote':False,'independent_refit':fit_record,'runtime':{'candidate':[kc,ti],'iterations':len(rows),'elapsed_seconds':duration,'absolute_objective':obj,'signed_objective':signed,'max_temperature_difference':tdiff,'max_command_difference':qdiff,'temperature':readings,'commands':commands},'log_sha256':{p.name:sha(p) for p in OUT.glob('*-log.txt')},'scope':'Independent modern local refit and one 599-iteration ARX runtime candidate plus initialization. Same pinned solver, not an independent solver algorithm, full256 runtime replay, historical binary recovery or physical experiment.'}
(OUT/'solver-verification.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'status':'passed','refit_diffs':diffs,'prediction_diff':pdiff,'runtime_metrics':{k:v for k,v in record['runtime'].items() if not isinstance(v,list)}},indent=2))
