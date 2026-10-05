"""Exact recurrence, full declared grid, controls, and scientific figure."""
from dataclasses import fields
import hashlib
import json
from pathlib import Path
import platform

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import scipy

from model import Procedure,episode_kernel,run_chain,mean_matched_constant,expected_shutdown,reserve_kernel

HERE=Path(__file__).resolve().parent
OUT=HERE/"results"


def figure(result):
    base=result['base']
    def get(world,ledger,floor):
        return next(r for r in base if r['world']==world and r['ledger']==ledger and r['floor']==floor)
    fig,axes=plt.subplots(2,2,figsize=(13.5,9.5),layout='constrained')
    ax=axes[0,0]
    for ledger,color,label in [('both','#176e80','Both contexts credited'),('A','#b45c36','Only context A credited')]:
        item=get('distributed',ledger,0)
        ax.plot([t['round'] for t in item['trace']], [t['active_probability'] for t in item['trace']],
                color=color,label=label,lw=2)
    ax.axhline(1,color='#508346',ls='--',label='Paid floor / mean-matched smoothing*',lw=1.7)
    ax.set(title='Positive mean income does not prevent shutdown',xlabel='Fresh projects elapsed',ylabel='Probability inquiry remains active',ylim=(-.02,1.06),xlim=(0,1000))
    ax.legend(fontsize=8,loc='upper right')
    ax=axes[0,1]
    selected=[r for r in result['grid'] if r['world']=='distributed' and r['ledger']=='both' and r['diversion']==0 and r['floor']==0]
    ax.plot([r['cap'] for r in selected],[r['shutdown']['expected_active_rounds'] for r in selected],marker='o',color='#176e80')
    ax.set_yscale('log')
    ax.set(title='A larger reserve changes the practical timescale',xlabel='Accessible reserve cap (rounds of expense)',ylabel='Expected active rounds before shutdown')
    ax=axes[1,0]
    names=['Distributed\nuseful proposals','No useful\nchange (.20)','Near-null\nchange (.39)']
    x=np.arange(3)
    for shift,floor,label,color in [(-.18,0,'Credit-funded','#176e80'),(.18,1,'Paid floor','#508346')]:
        vals=[get(w,'both',floor)['incremental_social_loss'] for w in ('distributed','absent','near_null')]
        ax.bar(x+shift,vals,.36,label=label,color=color)
    ax.axhline(0,color='#777777',lw=.8)
    ax.set(xticks=x,xticklabels=names,title='Continuing inquiry can help or waste resources',ylabel='Extra social loss over 1,000 projects\n(lower is better)')
    ax.legend(fontsize=9)
    ax=axes[1,1]
    selected=[r for r in result['grid'] if r['world']=='distributed' and r['ledger']=='both' and r['cap']==8 and r['floor']==0]
    ax.plot([r['diversion'] for r in selected],[r['flows']['active'] for r in selected],marker='o',color='#176e80',label='Expected active rounds')
    ax.plot([r['diversion'] for r in selected],[r['expected_useful_adoptions'] for r in selected],marker='s',color='#b45c36',label='Expected useful adoptions')
    ax.set(title='Diverting the agenda consumes correction capacity',xlabel='Probability slot is redirected to context A',ylabel='Expected count over 1,000 projects')
    ax.legend(fontsize=9)
    for ax in axes.flat:
        ax.grid(axis='y',alpha=.15)
        ax.spines[['top','right']].set_visible(False)
    fig.suptitle('Inquiry renewal depends on cash flow, recognition, and continued access',fontsize=16)
    fig.supxlabel('Exact finite calculations; independent project-specific proposals and fresh tests; output and response efficacy supplied\n*Mean-matched smoothing applies to both-context credit in the useful world; funding transfers are paid and are not counted twice.',fontsize=10)
    fig.savefig(OUT/'inquiry-renewal.png',dpi=170)
    fig.savefig(OUT/'inquiry-renewal.svg')
    plt.close(fig)


def main():
    if OUT.exists():raise SystemExit('Refusing to overwrite results; use a fresh copy for reproduction.')
    OUT.mkdir()
    cfg=json.loads((HERE/'config.json').read_text())
    proc=Procedure(**{f.name:cfg[f.name] for f in fields(Procedure)})
    base=[];grid=[];mean=[]
    for name,mix in cfg['worlds'].items():
        world=tuple(tuple(x) for x in mix)
        for ledger in ('both','A'):
            for diversion in cfg['capture_grid']:
                episode=episode_kernel(world,ledger,diversion,proc)
                for cap in cfg['reserve_grid']:
                    for floor in cfg['floors']:
                        row=run_chain(episode,cap,cap,floor,cfg['horizon'],cfg['inquiry_cost'],cfg['grant'],cfg['productive_output'],
                                      trace=diversion==0 and cap==cfg['reserve_cap'])
                        row.update(world=name,ledger=ledger,diversion=diversion)
                        if 'trace' in row:base.append(row)
                        grid.append({k:v for k,v in row.items() if k!='trace'})
                if diversion==0:
                    item=mean_matched_constant(episode,cfg['reserve_cap'],cfg['initial_reserve'],cfg['horizon'],
                                              cfg['inquiry_cost'],cfg['grant'],cfg['productive_output'])
                    item.update(world=name,ledger=ledger)
                    mean.append(item)
    e=episode_kernel(tuple(tuple(x) for x in cfg['worlds']['distributed']))
    controls={'positive_return_toy':expected_shutdown(.5,2,2,grant=3),
              'certain_credit':expected_shutdown(1.,8,8),
              'no_credit':expected_shutdown(0.,8,8),
              'zero_initial_performance':run_chain(e,initial=0,horizon=100),
              'zero_initial_floor':run_chain(e,initial=0,floor=1,horizon=100)}
    transition,flows=reserve_kernel(0.,4,cost=2,grant=5,floor=1)
    state=np.eye(5)[0];active=0.;balances=[]
    for t in range(100):
        active+=float(state@flows['active']);balances.append(float(state@np.arange(5)));state=state@transition
    controls['subcost_restart']={'cost':2,'floor':1,'initial':0,'horizon':100,'active_rounds':active,'opening_balances':balances}
    result={'status':'exploratory exact finite calculation; no empirical data or random simulation',
            'runtime':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'matplotlib':matplotlib.__version__},
            'base':base,'grid':grid,'constant_mean_benchmarks':mean,'controls':controls}
    (OUT/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    inputs=OUT/'inputs';inputs.mkdir()
    manifest={}
    for name in ('model.py','test_model.py','analyze.py','config.json','PROTOCOL.md'):
        data=(HERE/name).read_bytes();(inputs/name).write_bytes(data);manifest[name]=hashlib.sha256(data).hexdigest()
    (OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    summary=[]
    for row in base:
        summary.append({k:row[k] for k in ('world','ledger','floor','active_probability_next_round','incremental_social_loss','expected_useful_adoptions','expected_false_adoptions')} |
                       {'credit_probability':row['episode']['credit_probability'],
                        'social_value_per_active_round':-row['episode']['incremental_social_loss_per_active_round'],
                        'uncapped_net_income_per_active':row['performance_uncapped_mean_net_income'],
                        'active_rounds':row['flows']['active'],'shutdown':row.get('shutdown'),
                        'snapshots':row['snapshots']})
    (OUT/'summary.json').write_text(json.dumps({'base':summary,'constant_mean_benchmarks':mean},indent=2)+'\n')
    figure(result)
    print(json.dumps(summary,indent=2))
    print('Grid:',len(grid),'Conservation max:',max(abs(r['conservation_residual']) for r in grid),
          'Mass max:',max(r['probability_mass_residual'] for r in grid),
          'Linear residual max:',max(r.get('shutdown',{}).get('linear_residual',0) for r in grid))


if __name__=='__main__':main()
