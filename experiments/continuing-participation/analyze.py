"""Declared finite participation comparisons; no sampling or empirical fit."""
from pathlib import Path
from dataclasses import replace
from itertools import product
import json,hashlib,platform,argparse,gc
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from model import PublicTree,ParticipationParams


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    base=Path(__file__).resolve().parent;out=base/args.output;out.mkdir(exist_ok=False);(out/'inputs').mkdir()
    manifest={}
    for name in ['model.py','upstream_model.py','analyze.py','config.json','PROTOCOL.md','test_model.py']:
        data=(base/name).read_bytes();(out/'inputs'/name).write_bytes(data);manifest[name]=hashlib.sha256(data).hexdigest()
    (out/'manifest.json').write_text(json.dumps({'sha256':manifest,'python':platform.python_version(),'numpy':np.__version__},indent=2))
    cfg=json.loads((base/'config.json').read_text());results=[]
    def run(p,group,details=False):
        m=PublicTree(p)
        for mode in cfg['modes']:
            r=m.solve(mode,details);r['group']=group;results.append(r)
        print(group,p.horizon,p.initial_cash,p.compensation_grid,'nodes',len(m.nodes),'done',flush=True)
        (out/'results.json').write_text(json.dumps(results,indent=2));gc.collect()
    for h,cash,grid in product(cfg['horizons'],cfg['initial_cash'],cfg['compensation_grids']):
        p=ParticipationParams(horizon=h,initial_cash=cash,compensation_grid=tuple(grid))
        run(p,'base',h==1 and cash in (3,4))
    for burden,cash,grid in product(cfg['burden_controls'],cfg['burden_control_cash'],cfg['compensation_grids']):
        p=ParticipationParams(horizon=1,initial_cash=cash,compensation_grid=tuple(grid),repair_burden=burden)
        run(p,'burden_control')
    for cash,grid in product(cfg['high_loss_cash'],cfg['compensation_grids']):
        p=ParticipationParams(horizon=2,initial_cash=cash,compensation_grid=tuple(grid),collapse_loss=cfg['high_collapse_loss'])
        run(p,'high_collapse_loss',cash in (4,5))
    checks={'result_count':len(results),'max_flow_residual':max(r['flow_residual'] for r in results),
       'max_policy_evaluation_residual':max(r['policy_evaluation_residual'] for r in results),
       'max_absolute_primary_duality_gap':max(abs(r['duality_gap']) for r in results),
       'max_cash_conservation_residual':max(abs(r['cash_conservation_residual']) for r in results),
       'max_loss_sum_residual':max(abs(r['loss_sum_residual']) for r in results),
       'max_continuing_conditional_refusal_gain':max(r['maximum_conditional_refusal_gain'] for r in results if r['mode']=='continuing'),
       'max_continuing_replay_discrepancy':max(abs(r['metrics'][k]-r['veto_replay_metrics'][k]) for r in results if r['mode']=='continuing' for k in r['metrics'])}
    for key,value in checks.items():
        if key!='result_count':assert value<1e-7,(key,value)
    assert len(results)==92
    (out/'checks.json').write_text(json.dumps(checks,indent=2));print(checks,flush=True)
    def select(group,h,transfer,mode):
        return sorted([r for r in results if r['group']==group and r['config']['horizon']==h and (len(r['config']['compensation_grid'])>1)==transfer and r['mode']==mode],key=lambda r:r['config']['initial_cash'])
    fig,axs=plt.subplots(1,2,figsize=(11.8,4.8));colors=['#807589','#ba6243','#246a73']
    for ax,group,h,title in zip(axs,['base','high_collapse_loss'],[1,2],['One period; collapse loss 1 per owner','Two periods; collapse loss 6 per owner']):
        for (transfer,mode,label),color in zip([(True,'ex_ante','Initial agreement benchmark'),(False,'continuing','Continuing veto; no payments'),(True,'continuing','Continuing veto; funded payments')],colors):
            rows=select(group,h,transfer,mode)
            ax.plot([r['config']['initial_cash'] for r in rows],[100*r['metrics']['failure'] for r in rows],marker='o',ms=4,label=label,color=color)
        ax.set_xlabel('Initial joint liquid reserve');ax.set_ylabel('Best attainable collapse probability (%)');ax.set_title(title,fontsize=11);ax.grid(alpha=.2)
    fig.suptitle('An initially acceptable repair can require funded compensation later',fontsize=14)
    fig.legend(*axs[0].get_legend_handles_labels(),loc='lower center',ncol=3,bbox_to_anchor=(.5,.06),frameon=False,fontsize=9)
    fig.text(.5,.025,'Initial-agreement values assume execution. Full results separately replay actual vetoes. No borrowing or deferred compensation.',ha='center',fontsize=8)
    fig.subplots_adjust(left=.07,right=.98,top=.81,bottom=.24,wspace=.23)
    fig.savefig(out/'participation.png',dpi=180);fig.savefig(out/'participation.svg')

if __name__=='__main__':main()
