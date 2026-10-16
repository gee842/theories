"""Declared finite comparisons; deterministic, no sampling or hidden fit."""
import argparse, json, hashlib, shutil, platform, gc
from dataclasses import asdict, replace
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from model import Params, BeliefMDP, constrained, summarize


def execute(cfg,mode,budgets,details=False):
    mdp=BeliefMDP(cfg,mode)
    rows=[]
    for budget in budgets:
        result=summarize(mdp,constrained(mdp,budget),details and budget==.02)
        result['budget']=budget;rows.append(result)
    print(mode,asdict(cfg),'nodes',len(mdp.nodes),'done',flush=True)
    return {'config':asdict(cfg),'mode':mode,'results':rows}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True)
    args=parser.parse_args();base=Path(__file__).resolve().parent;out=base/args.output
    out.mkdir(exist_ok=False);(out/'inputs').mkdir()
    manifest={}
    for name in ('model.py','analyze.py','config.json','PROTOCOL.md','test_model.py'):
        data=(base/name).read_bytes();(out/'inputs'/name).write_bytes(data)
        manifest[name]=hashlib.sha256(data).hexdigest()
    (out/'manifest.json').write_text(json.dumps({'sha256':manifest,'python':platform.python_version(),'numpy':np.__version__},indent=2))
    raw=json.loads((base/'config.json').read_text());raw.pop('burden_budget');cfg=Params(**raw)
    budgets=[0,.01,.02,.03,.05,.1,.2,.4,.6];main_cfg=replace(cfg,horizon=8)
    bundle={'main':[],'controls':{}}
    def checkpoint(): (out/'results.json').write_text(json.dumps(bundle,indent=2))
    for mode in ('adaptive','no_test','continuous'):
        bundle['main'].append(execute(main_cfg,mode,budgets,True));checkpoint();gc.collect()
    controls={
        'original_short_horizon':(cfg,.6),
        'known_absent_fault':(replace(main_cfg,onset='0'),.02),
        'uninformative_test':(replace(main_cfg,sensitivity='.5',specificity='.5'),.02),
        'low_initial_cash':(replace(main_cfg,initial_cash=2),.02),
        'low_initial_stock':(replace(main_cfg,initial_stock=1),.02),
        'low_output':(replace(main_cfg,output_per_stock=1),.02),
        'initially_dormant':(replace(main_cfg,initial_ready=0),.02),
    }
    for name,(control,budget) in controls.items():
        bundle['controls'][name]=execute(control,'adaptive',[budget]);checkpoint();gc.collect()
    # Every feasible evaluated policy must balance cash and decompose cost.
    max_gap=0.;max_residual=0.;cases=0
    for series in bundle['main']+list(bundle['controls'].values()):
        c=series['config']
        for row in series['results']:
            cases+=1
            if not row['feasible']:continue
            m=row['metrics'];max_gap=max(max_gap,row['optimality_gap'])
            residual=m['terminal_cash']-c['initial_cash']+m['treasury']+m['expense']-m['output']
            max_residual=max(max_residual,abs(residual));assert abs(residual)<1e-9
            assert m['burden']<=row['budget']+1e-10
            assert abs(m['cost']-(m['expense']-m['output']-c['terminal_stock_value']*m['terminal_stock']+c['failure_cost']*m['failure']))<1e-9
            assert abs(m['burden']-m['target_absent_repairs']-c['test_burden']*m['tests'])<1e-10
    summary={'case_count':cases,'maximum_primal_dual_gap':max_gap,'maximum_conservation_residual':max_residual}
    (out/'checks.json').write_text(json.dumps(summary,indent=2));print(summary,flush=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10})
    fig,axs=plt.subplots(1,2,figsize=(11.8,4.6),layout='constrained')
    colors={'adaptive':'#246a73','no_test':'#ba6243','continuous':'#807589'}
    labels={'adaptive':'Adaptive inquiry','no_test':'Ordinary evidence only','continuous':'Compulsory service'}
    for series in bundle['main']:
        rr=[r for r in series['results'] if r['feasible']]
        x=[r['budget'] for r in rr];color=colors[series['mode']]
        axs[0].plot(x,[-r['metrics']['cost'] for r in rr],'o-',color=color,label=labels[series['mode']],ms=4)
        axs[1].plot(x,[r['metrics']['failure'] for r in rr],'o-',color=color,ms=4)
    axs[0].set_ylabel('Expected objective value (−cost; higher is better)')
    axs[1].set_ylabel('Probability of stock collapse by period 8')
    for ax in axs:
        ax.set_xlabel('Allowed expected cumulative burden');ax.grid(alpha=.2);ax.set_xlim(-.01,.61)
    axs[0].legend(fontsize=9,loc='lower right')
    axs[1].text(.98,.98,'Missing compulsory-service points are infeasible.\nExpected burden is not a pathwise harm cap.',ha='right',va='top',transform=axs[1].transAxes,fontsize=8)
    fig.suptitle('Recoverable inquiry under earned revenue and a burden limit',fontsize=14)
    fig.savefig(out/'frontier.png',dpi=180);fig.savefig(out/'frontier.svg');plt.close(fig)

if __name__=='__main__':main()
