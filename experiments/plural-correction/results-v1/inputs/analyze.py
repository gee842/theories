"""Deterministic queries of attainable expected consequence vectors."""
import argparse,json,hashlib,platform
from pathlib import Path
from dataclasses import replace,asdict
from itertools import product
import numpy as np
from scipy.optimize import linprog
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from model import Params,BeliefMDP,Access,ConsequenceGraph,NAMES


def curve(graph,caps,net_cap):
    rows=[]
    for cap in caps:
        fit=linprog(graph.metrics[1],A_eq=graph.flow,b_eq=graph.rhs,
                    A_ub=graph.metrics[[0,2]],b_ub=[cap,net_cap],bounds=(0,None),method='highs',options=graph.options)
        r={'failure_cap':float(cap),'net_expense_cap':net_cap,'feasible':bool(fit.success)}
        if fit.success:r.update(dict(zip(NAMES,map(float,graph.metrics@fit.x))))
        else:r['solver_status']=fit.status
        rows.append(r)
    return rows


def examples():
    pairwise={}
    for pair in [(0,1),(0,2),(1,2)]:
        omitted=({0,1,2}-set(pair)).pop();pairwise[str(pair)]=np.eye(3)[omitted].tolist()
    return {'three_way_conflict':{'policy_vectors':np.eye(3).tolist(),'bounds':[.3]*3,
               'pairwise_witnesses':pairwise,'separator':[1/3]*3,'minimum_weighted_loss':1/3,
               'weighted_bound':.3,'margin':1/30},
            'lottery_and_continuation':{'outcomes':[[0,2],[2,0]],'probabilities':[.5,.5],
               'expected_vector':[1,1],'fallback':[1.1,1.1],'ex_ante_gain_each':.1,
               'loss_for_exposed_participant_after_revelation':2.,'veto_gain_if_fallback_available':.9,
               'scope':'Separate constructed decision example; no integrated strategic game or compensation mechanism.'}}


def main():
    args=argparse.ArgumentParser();args.add_argument('--output',required=True);a=args.parse_args()
    base=Path(__file__).resolve().parent;out=base/a.output;out.mkdir(exist_ok=False);(out/'inputs').mkdir()
    names=['model.py','upstream_model.py','analyze.py','config.json','PROTOCOL.md','test_model.py']
    manifest={}
    for name in names:
        data=(base/name).read_bytes();(out/'inputs'/name).write_bytes(data);manifest[name]=hashlib.sha256(data).hexdigest()
    (out/'manifest.json').write_text(json.dumps({'sha256':manifest,'python':platform.python_version(),'numpy':np.__version__},indent=2))
    cfg=json.loads((base/'config.json').read_text());p=Params(horizon=cfg['main_horizon'])
    mdp=BeliefMDP(p);one=BeliefMDP(replace(p,horizon=1,initial_stock=1,initial_fault_probability='1/2'))
    result={'main_config':asdict(p),'one_period_config':asdict(one.cfg),'grid':[],'highlights':[],
            'one_period':[],'complementarity':[],'curves':{},'examples':examples()}
    def save(): (out/'results.json').write_text(json.dumps(result,indent=2))
    for access in [Access(),Access('no_diagnostic',diagnostics=False),Access('no_repair',repairs=False)]:
        graph=ConsequenceGraph(mdp,access)
        for f,h,c in product(cfg['failure_caps'],cfg['burden_caps'],cfg['expense_caps']):
            result['grid'].append(graph.feasibility([f,h,c],cfg['main_scales']))
        for b in cfg['highlighted_bounds']:result['highlights'].append(graph.feasibility(b,cfg['main_scales'],True))
        if access.name!='no_repair':result['curves']['six_'+access.name]=curve(graph,np.linspace(0,.18,21),-30)
        print('main',access.name,'complete',flush=True);save()
    accesses=[Access(),Access('no_diagnostic',diagnostics=False),Access('no_repair',repairs=False),
              Access('opening_75',repair_posterior_floor=.75),Access('response_75',response_posterior_floor=.75),
              Access('response_95',response_posterior_floor=.95)]
    for access in accesses:
        graph=ConsequenceGraph(one,access)
        result['one_period'].append(graph.feasibility(cfg['analytic_bounds'],cfg['analytic_scales'],True))
        if access.name in ['full','no_diagnostic']:result['curves']['one_'+access.name]=curve(graph,np.linspace(0,.45,21),.05)
    for cash,permission in product([2,8],[False,True]):
        graph=ConsequenceGraph(BeliefMDP(replace(one.cfg,initial_cash=cash)),Access('repair_allowed' if permission else 'repair_denied',repairs=permission))
        result['complementarity'].append({'cash':cash,'repair_permission':permission,
            **graph.feasibility(cfg['analytic_bounds'],cfg['analytic_scales'],True)})
    save()
    rows=result['grid']+result['highlights']+result['one_period']+result['complementarity']
    checks={'grid_cases':len(result['grid']),'detailed_cases':len(result['highlights'])+len(result['one_period'])+len(result['complementarity']),
            'curve_points':sum(map(len,result['curves'].values())),
            'max_flow_residual':max(r['flow_residual'] for r in rows),
            'max_policy_evaluation_residual':max(r['policy_evaluation_residual'] for r in rows),
            'max_absolute_primal_dual_gap':max(abs(r['certificate']['primal_dual_gap']) for r in rows),
            'unresolved':sum(r['status']=='numerically_unresolved' for r in rows),
            'grid_status_counts':{mode:{status:sum(r['authority']==mode and r['status']==status for r in result['grid'])
                    for status in ['feasible','infeasible']} for mode in ['full','no_diagnostic','no_repair']}}
    assert checks['unresolved']==0
    assert checks['max_policy_evaluation_residual']<1e-7
    assert checks['max_absolute_primal_dual_gap']<1e-7
    (out/'checks.json').write_text(json.dumps(checks,indent=2));print(checks,flush=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10})
    fig,axs=plt.subplots(1,2,figsize=(11.6,4.8))
    colors={'full':'#246a73','no_diagnostic':'#ba6243'}
    for ax,prefix,target,title in zip(axs,['one','six'],[(.1,.1),(.02,.02)],['One-period response; net expense ≤ 0.05','Six-period production; net expense ≤ −30']):
        for mode in ['full','no_diagnostic']:
            rr=result['curves'][prefix+'_'+mode]
            # NaN breaks the line at any infeasible query.
            ax.plot([r['failure_cap'] for r in rr],[r['burden'] if r['feasible'] else np.nan for r in rr],
                    'o-',ms=3,color=colors[mode],label='Diagnostic permitted' if mode=='full' else 'No paid diagnostic')
        ax.axvline(target[0],color='#66717a',lw=1,ls=':');ax.axhline(target[1],color='#66717a',lw=1,ls=':')
        ax.plot(*target,'*',color='#202932',ms=12,label='Declared requirement')
        ax.set_title(title,fontsize=11);ax.set_xlabel('Maximum allowed probability of collapse');ax.grid(alpha=.15)
        ax.set_ylabel('Minimum expected intervention/testing burden')
    fig.suptitle('Joint requirements can be feasible with one decision right and infeasible without it',fontsize=13)
    fig.legend(*axs[0].get_legend_handles_labels(),loc='lower center',bbox_to_anchor=(.5,.06),ncol=3,frameon=False)
    fig.text(.5,.025,'Finite expected constraints under a supplied model. Curves are threshold tradeoffs, not agreed social utility or individual safety guarantees.',ha='center',fontsize=8)
    fig.subplots_adjust(left=.07,right=.98,top=.81,bottom=.25,wspace=.25)
    fig.savefig(out/'frontiers.png',dpi=180);fig.savefig(out/'frontiers.svg')

if __name__=='__main__':main()
