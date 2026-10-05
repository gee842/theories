"""Run exact illustrative calculations and save all parameters and outputs."""
from pathlib import Path
from dataclasses import asdict,replace
from itertools import product
import hashlib,json,platform
import numpy as np
import scipy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from model import *


def main():
    root=Path(__file__).resolve().parent
    out=root/'results'
    out.mkdir(exist_ok=True)
    rows=[]
    for h,m,K in product([.05,.15],[.015,.06],[.08,.3]):
        p=Parameters(h=h,upkeep=m,rebuild=K)
        s=Planner(p);v=s.solve(8,UNKNOWN,1)
        stats,trace=evaluate(s,8)
        assert abs(v-stats['total_loss'])<1e-10
        fixed=calendar_lp(p,8)
        matched=calendar_lp(p,8,budget=stats['inquiry_cost'])
        assert stats['total_loss']<=fixed['total_loss']+1e-8
        assert stats['operating_loss']<=matched['operating_loss']+1e-8
        rows.append(dict(parameters=asdict(p),horizon=8,initial=list(UNKNOWN),
                         adaptive=stats,fixed_calendar=fixed,matched_expenditure=matched,
                         adaptive_trace=trace))
    cert=Parameters(h=.2,loss=10,treatment=4,diagnostic=1,success=1,
                    upkeep=.1,rebuild=2,cap=3)
    certstats,certtrace=evaluate(Planner(cert),2,(0,0))
    certificate=dict(parameters=asdict(cert),horizon=2,initial=[0,0],
                     adaptive=certstats,trace=certtrace,
                     absent_initially=Planner(cert).solve(2,(0,0),0),
                     expensive_upkeep=Planner(replace(cert,upkeep=.3)).solve(2,(0,0),1))
    capscan=[]
    for cap in [.04,.08,.1,.14,.38,.65]:
        p=Parameters(cap=cap,h=.05,upkeep=.06,rebuild=.08)
        stats,_=evaluate(Planner(p),8)
        capscan.append(dict(cap=cap,stats=stats))
    controls=[]
    for label,p in [('stationary',Parameters(h=0)),('unpredictable',Parameters(h=.5)),
                    ('uninformative_diagnostic',Parameters(success=0)),
                    ('prohibitive_upkeep',Parameters(upkeep=1.,rebuild=1.))]:
        stats,_=evaluate(Planner(p),8)
        fixed=calendar_lp(p,8)
        controls.append(dict(label=label,parameters=asdict(p),adaptive=stats,fixed_calendar=fixed))
    aging=[]
    for age,accuracy,delivery in product(range(13),[.5,.8,1.],[1.,.8,0.]):
        settings=dict(age=age,cue_accuracy=accuracy,delivery=delivery)
        aging.append(dict(settings=settings,result=handoff(**settings)))
    actual=Parameters(h=.1)
    stale=Planner(replace(actual,h=0))
    stale_stats,stale_trace=evaluate(stale,12,(0,0),world=actual)
    updated_stats,updated_trace=evaluate(Planner(actual),12,(0,0))
    stale_case=dict(world_parameters=asdict(actual),assumed_h=0,horizon=12,
                    stale=stale_stats,updated=updated_stats,
                    stale_trace=stale_trace,updated_trace=updated_trace)
    hashes={name:hashlib.sha256((root/name).read_bytes()).hexdigest()
            for name in ['PROTOCOL.md','model.py','test_model.py','analyze.py']}
    results=dict(status='exploratory exact finite-model calculations; no sampled trials',
                 versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
                 input_sha256=hashes,certificate=certificate,parameter_grid=rows,
                 resource_caps=capscan,controls=controls,handoffs=aging,stale_case=stale_case)
    (out/'analysis.json').write_text(json.dumps(results,indent=2)+'\n')
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    fig,ax=plt.subplots(2,2,figsize=(12.6,8.5),layout='constrained')
    labels=[f"h={r['parameters']['h']}, m={r['parameters']['upkeep']}, K={r['parameters']['rebuild']}" for r in rows]
    y=np.arange(len(rows))
    ax[0,0].barh(y-.15,[r['adaptive']['operating_loss'] for r in rows],height=.28,label='Adaptive capacity')
    ax[0,0].barh(y+.15,[r['matched_expenditure']['operating_loss'] for r in rows],height=.28,label='Best calendar lottery')
    ax[0,0].set_yticks(y,labels,fontsize=8)
    ax[0,0].invert_yaxis();ax[0,0].set_xlabel('Expected operating loss over 8 periods')
    ax[0,0].set_title('A. Matched expected inquiry expenditure',loc='left')
    ax[0,0].legend(fontsize=8)
    ages=np.arange(13);p0=.5*(1-.8**ages)
    ax[0,1].plot(ages,p0,'o-',label='Current need after an old negative')
    ax[0,1].axhline(.4,color='#c4682d',linestyle='--',label='Treatment threshold')
    ax[0,1].axhline(0,color='gray',linestyle=':',label='Unrevised “no need” instruction')
    ax[0,1].set(xlabel='Periods since diagnosis',ylabel='Probability of need',ylim=(-.015,.55))
    ax[0,1].set_title('B. Historical truth and current relevance differ',loc='left')
    ax[0,1].legend(fontsize=8)
    for accuracy,delivery,label in [(.5,1.,'No cue; reliable delivery'),(.5,.8,'No cue; 80% delivery'),
                                    (1.,1.,'Fully informative public cue')]:
        series=[next(x['result'] for x in aging if x['settings']==dict(age=int(a),cue_accuracy=accuracy,delivery=delivery)) for a in ages]
        ax[1,0].plot(ages,[s['communication_cost'] for s in series],'o-',label=label)
    ax[1,0].set(xlabel='Periods since recorded state',ylabel='Expected handoff expenditure',ylim=(-.003,.085))
    ax[1,0].set_title('C. Pay for evidence only when it changes a decision',loc='left')
    ax[1,0].legend(fontsize=8)
    ax[1,1].plot([r['cap'] for r in capscan],[r['stats']['total_loss'] for r in capscan],'o-',color='#4a7864')
    ax[1,1].set(xlabel='Per-period inquiry procurement cap',ylabel='Minimum total expected loss over 8 periods')
    ax[1,1].set_title('D. Availability constraints and paid allocation',loc='left')
    fig.suptitle('Maintaining inquiry and transmitting evidence\nTwo separate exact decision models; fixed purposes and known dynamics',fontsize=15)
    fig.savefig(out/'recurrent-inquiry.png',dpi=180)
    fig.savefig(out/'recurrent-inquiry.svg')
    brief=dict(certificate=certificate['adaptive'],grid=[dict(parameters=r['parameters'],
               adaptive=r['adaptive'],fixed=r['fixed_calendar']['total_loss'],
               matched=r['matched_expenditure']) for r in rows],controls=controls,
               stale={k:v for k,v in stale_case.items() if 'trace' not in k})
    print(json.dumps(brief,indent=2))


if __name__=='__main__':main()
