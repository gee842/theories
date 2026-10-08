#!/usr/bin/env python3
"""Scientific figure: published observations beside an explicitly supplied model."""
from pathlib import Path
import csv
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
rows = list(csv.DictReader((HERE/'pellicle-cohorts.csv').open()))
result = json.loads((HERE/'results.json').read_text())
fig, axes = plt.subplots(1,2,figsize=(11,4.4),layout='constrained')
colors = ['#2364AA','#E07A16','#648D42','#AA4076']
dates = sorted({r['date'] for r in rows})
for i,date in enumerate(dates):
    cohort=[r for r in rows if r['date']==date]
    axes[0].scatter([float(r['log10_dilution_factor'])+(i-1.5)*.025 for r in cohort],
                    [int(r['success'])/int(r['total']) for r in cohort],s=48,color=colors[i],label=date)
p=result['pellicle_pooled']
axes[0].plot([r['log10_dilution_factor'] for r in p],
             [r['success']/r['total'] for r in p],color='black',marker='x',linestyle='--',label='Pooled counts')
axes[0].set(title='Observed mat formation at 24 hours',xlabel='log10 dilution factor (higher = fewer initial cells)',ylabel='Recorded successes / cultures',ylim=(-.06,1.09))
axes[0].legend(fontsize=8,loc='center left')
labels={'source':'Source dispersal rates','equal_dispersal':'Equal dispersal rates',
        'neutral_retention_slice':'Neutral retention contrast; mutation retained'}
for (name,runs),color in zip(result['event_model_scenarios'].items(),colors):
    series=runs[-1]['records'][1:]
    axes[1].plot([r['source_nominal_days'] for r in series],
                 [r['surface_WS_fraction'] for r in series],marker='o',markersize=3,label=labels[name],color=color)
axes[1].set(title='Illustrative conventional model; no fitted rates',xlabel='Nominal days in source model',ylabel='WS fraction at the surface',yscale='log',ylim=(1e-9,2))
axes[1].legend(fontsize=7,loc='center right')
for ax in axes:ax.grid(alpha=.18)
fig.suptitle('Establishment depends on conditions; later representation depends on retention',fontsize=12)
fig.savefig(HERE/'establishment-and-retention.png',dpi=180)
fig.savefig(HERE/'establishment-and-retention.svg')
