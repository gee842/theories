"""Post-run accounting, uncertainty summaries, and scientific figures."""
from pathlib import Path
import json
import hashlib
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import experiment as ex

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results-evaluation'
report=json.loads((OUT/'summary.json').read_text())
records=[json.loads(line) for line in (OUT/'runs.jsonl').read_text().splitlines()]
assert len(records)==256*2*14
for name,digest in json.loads((ROOT/'evaluation-inputs/manifest.json').read_text()).items():
    assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
for row in records:
    if row['false_acceptance']:
        assert row['true_selected_policy_gain']<=0
    for test in row['tests']:
        assert test['n_a']==test['n_b']==128
        assert test['complete_block']>=test['start_block']+2
    assert sum(t['alpha'] for t in row['tests'])<=.05+1e-12

stats={(row['hazard'],row['arm']):row for row in report['summary']}
names=['protected','return_funded','short_records','frozen_model',
       'no_standing','no_authority','no_inquiry','temporary_rescue']
labels=['Protected inquiry','Fast funding withdrawal','Lost linking records','Fixed global model',
        'Evidence denied standing','Deployment veto','No inquiry','Temporary rescue']

funding_cost=640*.01+73*.01+256*.015+128*.25
def scheduled_funds(rho,last_block=22):
    return sum(max(.125,8*rho**b) for b in range(last_block+1))
rho_bound=brentq(lambda rho:scheduled_funds(rho)-funding_cost,.81,.82,xtol=1e-14)
renewal=[]
for rate in [.8,.81,.815,.816,.82,.9]:
    name=f'renewal_{rate:.3f}'
    rr=[r for r in records if r['hazard'] and r['arm']==name]
    times=[r['validated_block'] for r in rr if r['validated_block'] is not None]
    renewal.append({'rho':rate,'funding_by_block22':scheduled_funds(rate),
                    'ever_validated':len(times),'timely':sum(r['timely_validation'] for r in rr),
                    'validation_min':None if not times else min(times),
                    'validation_max':None if not times else max(times),
                    'validation_mean':None if not times else float(np.mean(times))})

plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(2,2,figsize=(13,9.8),layout='constrained')
ax=axs[0,0]
matrix=[]
for name in names:
    rr=[r for r in records if r['hazard'] and r['arm']==name]
    matrix.append([np.mean([r[field] is not None and r[field]<=24 for r in rr])
                   for field in ['validated_block','admitted_block','enacted_block']])
matrix=np.array(matrix)
ax.imshow(matrix,cmap='Blues',vmin=0,vmax=1,aspect='auto')
ax.set_yticks(range(len(labels)),labels)
ax.set_xticks(range(3),['Validated','Admitted','Deployed'])
for i in range(len(labels)):
    for j in range(3):
        ax.text(j,i,f'{matrix[i,j]:.0%}',ha='center',va='center',
                color='white' if matrix[i,j]>.5 else '#253449')
ax.set_title('A. Distinct stages by the declared deadline\nHazard present, 256 paired evaluation seeds')

ax=axs[0,1]
for i,row in enumerate(renewal):
    mean=row['validation_mean']
    ax.errorbar(i,mean,yerr=[[mean-row['validation_min']],[row['validation_max']-mean]],
                fmt='o',capsize=5,color='#2c7c7b',ms=7)
ax.axhline(24,color='#c45145',ls='--',label='Deadline: block 24')
ax.set_xticks(range(len(renewal)),[f'{r["rho"]:.3f}' for r in renewal])
ax.set(xlabel='Fraction of inquiry allocation retained per block',
       ylabel='Block of first validation',title='B. Valid evidence can arrive too late')
ax.legend(frameon=False,loc='upper right')
ax.text(.98,.45,'Points: mean\nBars: observed min–max\nAll six eventually validated',
        transform=ax.transAxes,ha='right',fontsize=9)

ax=axs[1,0]
subset=['protected','return_funded','frozen_model','no_authority','temporary_rescue']
display=['Protected','Fast withdrawal','Fixed model','Deployment veto','Rescue']
ix=np.arange(len(subset))
for h,offset,color,label in [(True,-.18,'#2c7c7b','Hazard present'),
                            (False,.18,'#c45145','Hazard absent')]:
    mean=np.array([stats[h,n]['loss_reduction_vs_no_inquiry']['mean'] for n in subset])
    ci=np.array([1.96*stats[h,n]['loss_reduction_vs_no_inquiry']['se'] for n in subset])
    ax.barh(ix+offset,mean,height=.34,color=color,label=label)
    ax.errorbar(mean,ix+offset,xerr=ci,fmt='none',ecolor='#253449',capsize=2,lw=1)
ax.axvline(0,color='#888888',lw=1)
ax.set_yticks(ix,display)
ax.invert_yaxis()
ax.set(xlabel='Loss reduction versus no inquiry; all declared costs included',
       title='C. Discovery can pay here, and cost in the control world')
ax.legend(frameon=False,loc='lower right',fontsize=9)

ax=axs[1,1]
for h,color,label in [(False,'#c45145','Hazard absent'),(True,'#2c7c7b','Hazard present')]:
    rr=[r for r in records if r['hazard']==h and r['arm']=='protected' and r['tests']]
    ax.scatter([r['tests'][0]['search_score'] for r in rr],
               [r['tests'][0]['net_lower_bound'] for r in rr],s=14,alpha=.35,color=color,label=label)
ax.axhline(0,color='#888888',ls='--',label='Acceptance threshold')
ax.set(xlabel='Exploratory failure-rate contrast of nominated feature',
       ylabel='Fresh causal lower bound after action cost',
       title='D. A promising association still requires a new trial')
ax.legend(frameon=False,loc='lower right',fontsize=9)
fig.suptitle('From generated candidates to effective institutional change',fontsize=16)
fig.savefig(OUT/'discovery-results.png',dpi=180)
fig.savefig(OUT/'discovery-results.svg')
plt.close(fig)

compact={'status':'passed','n_independent_seeds':256,'arms':14,'conditions':2,
         'total_trajectories':len(records),'first_full_test_cost':funding_cost,
         'severe_funding_total':sum(max(.125,8*.5**b) for b in range(64)),
         'necessary_funding_rho_boundary_at_deadline':rho_bound,
         'renewal_sweep':renewal,
         'protected_hazard':stats[True,'protected'],
         'protected_absent':stats[False,'protected'],
         'all_false_acceptances':sum(r['false_acceptance'] for r in records),
         'note':'Arms and hazard conditions are paired, not 7168 independent replications. The confidence guarantee is conditional on the protocol assumptions.'}
(OUT/'analysis.json').write_text(json.dumps(compact,indent=2)+'\n')
print(json.dumps({k:v for k,v in compact.items() if not k.startswith('protected_')},indent=2))
