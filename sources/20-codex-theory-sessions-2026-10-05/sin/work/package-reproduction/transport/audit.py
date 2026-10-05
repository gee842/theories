"""Predeclared, independently coded finite-case and invariant audit."""
from itertools import product
import json
from pathlib import Path
import service
import queue_model

def run():
    n=0
    for r in service.REGIMES:
        for backlog,bursts,dd,dl in product((0,1,3),product((False,True),repeat=5),(1,2,4),(2,4)):
            for f,a in product((0,1),repeat=2):
                shock=dict(backlog=backlog,bursts=bursts,diag_duration=dd,deploy_duration=dl,correct=True,effective=True)
                observed=service.run(r,shock,f,a)
                predicted=queue_model.predict_path(r,backlog,bursts,dd,dl,f,a)
                assert observed['recovered']==predicted['recovered'],(r,shock,f,a,observed,predicted)
                assert observed['valid_gate']==predicted['gate'],(r,shock,f,a,observed,predicted)
                if observed['recovered']: assert observed['recovery_time']==predicted['recovery_time']
                gate0=service.run(r,shock,f,0,mode='diag')
                gate1=service.run(r,shock,f,1,mode='diag')
                assert gate0['valid_gate']==gate1['valid_gate']
                assert gate0['proposal_time']==gate1['proposal_time']
                assert observed['spent'] in (3,6)
                n+=1
            for t,a in product(range(1,6),(0,1)):
                shock=dict(backlog=backlog,bursts=bursts,diag_duration=dd,deploy_duration=dl,correct=True,effective=True)
                observed=service.run(r,shock,authority=a,mode='enact',inject_time=t)
                predicted=queue_model.predict_path(r,backlog,bursts,dd,dl,0,a,mode='enact',inject_time=t)
                assert observed['recovered']==predicted['recovered']
                n+=1
    # Strict control oracle: p0=.85*.75; p1=.85; q0=.95*.5; q1=.95.
    control=service.REGIMES[0]
    for dd in (1,2,4):
        for dl in (2,4):
            s=dict(backlog=3,bursts=(True,)*5,diag_duration=dd,deploy_duration=dl,correct=True,effective=True)
            for f,a in product((0,1),repeat=2):
                got=service.run(control,s,f,a)
                expected=(dd+(0 if f else 3)<=5) and ((5 if a else 7)+dl<=9)
                assert got['recovered']==expected
                for field in ('correct','effective'):
                    failed=dict(s);failed[field]=False
                    assert not service.run(control,failed,f,a)['recovered']
    oracles=[]
    for r in service.REGIMES:
        p=dict(queue_model.TRUE_PARAMS,arrival=r['arrival_p'])
        mass=sum(case[-1] for case in queue_model.primitive_cases(p))
        assert abs(mass-1)<1e-12
        actual=queue_model.integrated_rates(r,p)
        local=queue_model.oracle_local(r,p)
        if r['name']=='reserved_control':
            for got,want in zip(local['p'],[.6375,.85]): assert abs(got-want)<1e-12
            for got,want in zip(local['q'],[.475,.95]): assert abs(got-want)<1e-12
            assert max(abs(x-y) for x,y in zip(actual,local['predictions']))<1e-12
        oracles.append(dict(regime=r['name'],integrated=actual,local=local,
                            residual=[x-y for x,y in zip(actual,local['predictions'])],
                            max_factorization_error=max(abs(x-y) for x,y in zip(actual,local['predictions']))))
    result=dict(status='passed',path_checks=n,oracle=oracles,
                numerical_tolerance=1e-12,scope='all finite backlog/burst/duration combinations, all four intervention cells, and forced recommendation times 1..5; technical and diagnosis failure controls')
    Path(__file__).with_name('audit-results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('Independent path checks passed:',n,flush=True)
