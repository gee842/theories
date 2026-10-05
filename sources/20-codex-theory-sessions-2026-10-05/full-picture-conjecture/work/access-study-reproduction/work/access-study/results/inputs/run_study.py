"""Run the frozen four-period access study and save every declared case."""
from pathlib import Path
import json,time,hashlib,datetime
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product
from model import Config,Engine,WEIGHTS,make_state

HERE=Path(__file__).resolve().parent
RESULTS=HERE/'results'

def case(engine,label,stock,cash,belief,access,ready=0,horizon=4):
    state=make_state(horizon=horizon,stock=stock,cash=cash,belief=belief,access=access,ready=ready)
    data={'label':label,'initial':{'horizon':horizon,'stock':stock,'cash':cash,'treasury':5-cash,
                                'ready':ready,'belief':belief,'access':access},'probes':{}}
    for name,w in WEIGHTS.items():data['probes'][name]=engine.result(state,w)
    return data

def main():
    RESULTS.mkdir(exist_ok=True)
    inputs=RESULTS/'inputs';inputs.mkdir(exist_ok=True)
    for name in ('PROTOCOL.md','protocol-freeze.json','model.py','run_study.py'):
        (inputs/name).write_bytes((HERE/name).read_bytes())
    manifest={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs.iterdir()}}
    (RESULTS/'input-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    start=time.monotonic();groups={};stats={}
    eng=Engine()
    rows=[]
    for stock,belief,access in product((1,2,3),('0','1/2','1'),('barred','immediate','delayed')):
        for cash in range(6):rows.append(case(eng,'main',stock,cash,belief,access))
    groups['main']=rows
    stats['main']={'states_solved_per_weight':eng.solve.cache_info().currsize,
                   'action_states':eng.actions.cache_info().currsize,'branch_checks':eng.branch_checks}
    print('Main grid completed:',len(rows),'initial states;',round(time.monotonic()-start,2),'seconds',flush=True)
    (RESULTS/'main.json').write_text(json.dumps(rows,indent=2)+'\n')
    # Fixed controls are separate models, not adjusted after observing main results.
    definitions=[
        ('no_output',replace(Config(),output_rate=0),2,'1',0,('barred','immediate')),
        ('known_safe',replace(Config(),onset=Q(0),damage_healthy=Q(0)),2,'0',0,('barred','immediate','delayed')),
        ('initially_ready',Config(),1,'1/2',1,('barred','immediate','delayed')),
        ('uninformative_test',replace(Config(),sensitivity=Q(1,2),specificity=Q(1,2)),2,'1',0,('barred','immediate')),
    ]
    for label,cfg,x,p,r,modes in definitions:
        e=Engine(cfg);cr=[]
        for access,cash in product(modes,(0,1,5)):cr.append(case(e,label,x,cash,p,access,r))
        groups[label]=cr
        stats[label]={'states_solved_per_weight':e.solve.cache_info().currsize,
                      'action_states':e.actions.cache_info().currsize,'branch_checks':e.branch_checks}
        print('Control completed:',label,round(time.monotonic()-start,2),'seconds',flush=True)
    (RESULTS/'controls.json').write_text(json.dumps({k:v for k,v in groups.items() if k!='main'},indent=2)+'\n')
    # Predetermined group-level projection checks.
    sensitive={a:0 for a in ('barred','immediate','delayed')}
    ranges=[]
    for stock,belief,access,probe in product((1,2,3),('0','1/2','1'),sensitive,WEIGHTS):
        subset=[r for r in rows if r['initial']['stock']==stock and r['initial']['belief']==belief and r['initial']['access']==access]
        vals=[Q(r['probes'][probe]['support_value']) for r in subset]
        if len(set(vals))>1:sensitive[access]+=1
        ranges.append({'stock':stock,'belief':belief,'access':access,'probe':probe,
                       'minimum':str(min(vals)),'maximum':str(max(vals)),'different':len(set(vals))>1})
        if access=='immediate':
            assert len(set(vals))==1
            assert len({json.dumps(r['probes'][probe]['metrics_exact'],sort_keys=True) for r in subset})==1
    # Every relaxed support optimum weakly improves; this concerns scores, not each vector coordinate.
    access_comparisons=0
    for stock,belief,cash,probe in product((1,2,3),('0','1/2','1'),range(6),WEIGHTS):
        selected={r['initial']['access']:r for r in rows if r['initial']['stock']==stock and r['initial']['belief']==belief and r['initial']['cash']==cash}
        value=lambda mode:Q(selected[mode]['probes'][probe]['support_value'])
        assert value('immediate')<=value('delayed')<=value('barred')
        access_comparisons+=1
    paid_test_cases=sum(r['probes'][p]['metrics']['tests']>0 for r in rows for p in WEIGHTS)
    chosen=[r for r in rows if r['initial']['stock']==2 and r['initial']['belief']=='1' and r['initial']['cash'] in (0,1,5)]
    controls_summary={}
    for label,cr in groups.items():
        if label=='main':continue
        controls_summary[label]=[{'initial':r['initial'],'failure_probe':r['probes']['failure']['metrics_exact'],
                                 'mixed_probe':r['probes']['mixed']['metrics_exact']} for r in cr]
    summary={'status':'all completed','main_initial_states':len(rows),'probes':len(WEIGHTS),
             'main_optimizations':len(rows)*len(WEIGHTS),'control_initial_states':sum(len(r) for k,r in groups.items() if k!='main'),
             'partition_sensitive_groups_out_of_63_per_access':sensitive,
             'nested_access_comparisons':access_comparisons,'main_probe_optima_using_paid_tests':paid_test_cases,
             'selected_stock2_known_fault_cases':chosen,'controls':controls_summary,
             'graph_stats':stats,'elapsed_seconds':time.monotonic()-start,
             'meaning':'Exact finite-model support probes. Unequal minima refute equality; seven equal minima alone do not prove attainable-set equality.'}
    (RESULTS/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    (RESULTS/'partition-checks.json').write_text(json.dumps(ranges,indent=2)+'\n')
    witnesses={}
    for access,cash in product(('barred','immediate','delayed'),(0,1)):
        s=make_state(horizon=2,cash=cash)
        s=s._replace(unlock={'barred':-1,'immediate':0,'delayed':1}[access])
        witnesses[f'{access}_cash{cash}']={'result':eng.result(s,WEIGHTS['failure']),
                                        'policy':eng.reachable_policy(s,WEIGHTS['failure'])}
    (RESULTS/'two-period-witnesses.json').write_text(json.dumps(witnesses,indent=2)+'\n')
    compact={k:summary[k] for k in ('status','main_initial_states','probes','main_optimizations','control_initial_states',
                                  'partition_sensitive_groups_out_of_63_per_access','nested_access_comparisons','main_probe_optima_using_paid_tests','elapsed_seconds')}
    print(json.dumps(compact,indent=2))

if __name__=='__main__':main()
