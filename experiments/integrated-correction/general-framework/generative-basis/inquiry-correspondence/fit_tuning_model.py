#!/usr/bin/env python3
"""Reproduce archived sysid options with a pinned modern GEKKO, local solver only.
No hardware and no execution of the original optimizer. This does not recover an
unspecified historical software environment or establish a global fit optimum.
"""
from pathlib import Path
import argparse,contextlib,csv,hashlib,io,json,sys,time
import numpy as np
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--gekko-path',required=True);args=ap.parse_args()
    dep=Path(args.gekko_path);sys.path.insert(0,str(dep))
    import gekko
    from gekko import GEKKO
    assert gekko.__version__=='1.3.2'
    p=ROOT/'sources/tclab-benchmark/extracted/2_PID/0_initial_PID/data.txt'
    with p.open() as f:data=[{k:float(v) for k,v in r.items()} for r in csv.DictReader(f)]
    t=np.array([r['Time'] for r in data]);u=np.array([[r['Q1'],r['Q2']] for r in data]);y=np.array([[r['T1'],r['T2']] for r in data])
    assert len(data)==599 and np.all(u[:,1]==0)
    log=io.StringIO();start=time.monotonic()
    m=GEKKO(remote=False)
    try:
        with contextlib.redirect_stdout(log),contextlib.redirect_stderr(log):
            yp,parameters,gain=m.sysid(t.copy(),u.copy(),y.copy(),na=2,nb=2,objf=10000,shift='init',scale=False,diaglevel=1,pred='model')
    except Exception:
        (HERE/'tuning-fit-log.txt').write_text(log.getvalue());raise
    finally:m.cleanup()
    (HERE/'tuning-fit-log.txt').write_text(log.getvalue())
    result={'status':'passed','producer_sha256':sha(Path(__file__)),'training_source':str(p.relative_to(ROOT)),'training_sha256':sha(p),
      'python':sys.version,'numpy':np.__version__,'gekko':gekko.__version__,
      'package_source_sha256':sha(dep/'gekko/gekko.py'),'local_solver_sha256':sha(dep/'gekko/bin/apm_mac'),
      'options':{'na':2,'nb':2,'objf':10000,'shift':'init','scale':False,'diaglevel':1,'pred':'model','remote':False},
      'elapsed_seconds':time.monotonic()-start,'parameters':{k:np.asarray(v).tolist() for k,v in parameters.items()},
      'gains':np.asarray(gain).tolist(),'predicted_training':np.asarray(yp).tolist(),
      'training_output_residual':(y-np.asarray(yp)).tolist(),'solver_log_sha256':sha(HERE/'tuning-fit-log.txt'),
      'scope':'Pinned modern GEKKO 1.3.2 local numerical output-error fit using the archived options and original initial data. Not the unspecified historical binary/environment, independent physical replication, global-optimum proof or future-error certificate.'}
    (HERE/'tuning-model.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','gekko','elapsed_seconds','parameters','gains','scope']},indent=2))
if __name__=='__main__':main()
