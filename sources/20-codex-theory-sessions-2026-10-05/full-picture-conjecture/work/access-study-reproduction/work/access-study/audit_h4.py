"""Targeted independent H4 support checks for the main account-access result."""
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
import time
import model as m
import audit_oracle as oracle

HERE=Path(__file__).resolve().parent
assert Path(m.__file__).resolve()==HERE/'model.py'
engine=m.Engine();rows=[];started=time.perf_counter()
for cash in (0,1,5):
    for access in ('barred','immediate','delayed'):
        state=m.make_state(4,2,cash,5,0,'1',access)
        os=oracle.State(4,2,cash,5-cash,0,Q(1),state.unlock)
        mode='barred' if access=='barred' else 'delayed'
        for name in ('failure','mixed'):
            weights=m.WEIGHTS[name]
            actual=engine.result(state,weights)
            expected,metrics,_=oracle.solve(os,weights,mode)
            assert Q(actual['support_value'])==expected,(cash,access,name,actual,expected)
            rows.append({'cash':cash,'treasury':5-cash,'access':access,'probe':name,
                         'support_exact':str(expected),
                         'independent_selected_metrics':list(map(str,metrics)),
                         'candidate_selected_metrics':{n:actual['metrics_exact'][n] for n in ('failure','expense','burden','unrecovered')}})
failure={(r['cash'],r['access']):Q(r['support_exact']) for r in rows if r['probe']=='failure'}
assert failure[(0,'barred')]==Q(153,250)
assert failure[(1,'barred')]==Q(17,1250)
assert failure[(5,'barred')]==0
assert all(failure[(b,access)]==0 for b in (0,1,5) for access in ('immediate','delayed'))
out={'status':'passed','runtime_seconds':time.perf_counter()-started,
     'independent_H4_optima_compared':len(rows),'results':rows,
     'scope':'stock2, certain initial fault, unready, total5; splits0/1/5; all3access modes; failure and mixed probes',
     'model_sha256':sha256((HERE/'model.py').read_bytes()).hexdigest(),
     'oracle_sha256':sha256((HERE/'audit_oracle.py').read_bytes()).hexdigest(),
     'independent_cache':str(oracle.solve.cache_info())}
(HERE/'audit_h4_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
