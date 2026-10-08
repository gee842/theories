#!/usr/bin/env python3
"""Cross-check four leading direct-recurrence candidates through local GEKKO ARX.
This is a numerical runtime comparison, not a formal floating implementation proof.
"""
from pathlib import Path
import argparse,contextlib,csv,hashlib,io,json,sys,time
import numpy as np
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[4]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--gekko-path',required=True);args=ap.parse_args()
    dep=Path(args.gekko_path);sys.path.insert(0,str(dep))
    import gekko
    from gekko import GEKKO
    assert gekko.__version__=='1.3.2'
    fit=json.loads((HERE/'tuning-model.json').read_text());result=json.loads((HERE/'tuning-results.json').read_text())
    assert sha(dep/'gekko/gekko.py')==fit['package_source_sha256']
    assert sha(dep/'gekko/bin/apm_mac')==fit['local_solver_sha256']
    with (ROOT/fit['training_source']).open() as f:rows=[{k:float(v) for k,v in r.items()} for r in csv.DictReader(f)]
    p={k:np.array(v) for k,v in fit['parameters'].items()};residual=np.array(fit['training_output_residual'])[:,0]
    scenario=result['scenarios'][0]
    import analyze_tuning
    reports=[];logs=io.StringIO()
    for kc,ti in [(10.,55.),(10.,60.),(10.,50.),(10.,65.)]:
        start=time.monotonic();m=GEKKO(remote=False)
        with contextlib.redirect_stdout(logs),contextlib.redirect_stderr(logs):
            ys,us=m.arx(p);m.options.IMODE=1;m.time=[0,1];m.solve(disp=False)
            m.options.IMODE=4;m.solve(disp=False)
            readings=[rows[0]['T1']];commands=[];integ=0.0
            for i,row in enumerate(rows):
                e=row['TSP1']-readings[i];addition=kc/ti*e;integ+=addition;raw=kc*e+integ
                q=max(0.,min(100.,raw))
                if raw<0 or raw>100:integ-=addition
                commands.append(q);us[0].value=q;m.solve(disp=False)
                if i<len(rows)-1:readings.append(ys[0].value[1]+residual[i+1])
            m.cleanup()
        a=[v[0] for v in fit['parameters']['a']];b=[v[0] for v in fit['parameters']['b'][0]];c=fit['parameters']['c'][0]
        direct=analyze_tuning.simulate(rows,a,b,c,residual,kc,ti)
        n=len(rows);tracking=sum(abs(r['TSP1']-y) for r,y in zip(rows,readings));motion=sum(abs(v-u) for u,v in zip(commands,commands[1:]));signed=commands[-1]-commands[0]
        report={'Kc':kc,'tauI_seconds':ti,'steps':n,'elapsed_seconds':time.monotonic()-start,
          'max_temperature_difference_celsius':max(abs(x-y) for x,y in zip(readings,direct['temperature'])),
          'max_command_difference_percent':max(abs(x-y) for x,y in zip(commands,direct['commands'])),
          'runtime_signed_objective':(tracking+.5*signed)/n,'runtime_absolute_objective':(tracking+.5*motion)/n,
          'direct_signed_objective':direct['signed_objective'],'direct_absolute_objective':direct['absolute_objective'],
          'runtime_temperature':readings,'runtime_commands':commands}
        reports.append(report);print(json.dumps({k:v for k,v in report.items() if not isinstance(v,list)}),flush=True)
    (HERE/'tuning-runtime-log.txt').write_text(logs.getvalue())
    output={'status':'passed','checker_sha256':sha(Path(__file__)),'producer_sha256':sha(HERE/'analyze_tuning.py'),
      'fit_sha256':sha(HERE/'tuning-model.json'),'results_sha256':sha(HERE/'tuning-results.json'),'log_sha256':sha(HERE/'tuning-runtime-log.txt'),
      'gekko':gekko.__version__,'python':sys.version,'cases':reports,
      'scope':'Four leading source-contract grid candidates independently advanced through GEKKO ARX runtime for all 599 loop iterations. The remaining grid points use the disclosed direct recurrence, not a claimed full GEKKO-grid replication or verified floating implementation.'}
    assert all(r['max_temperature_difference_celsius']<0.001 and r['max_command_difference_percent']<0.01 for r in reports)
    assert min(reports,key=lambda r:r['runtime_absolute_objective'])['tauI_seconds']==55.
    assert min(reports,key=lambda r:r['runtime_signed_objective'])['tauI_seconds']==55.
    (HERE/'tuning-runtime-checks.json').write_text(json.dumps(output,indent=2)+'\n')
if __name__=='__main__':main()
