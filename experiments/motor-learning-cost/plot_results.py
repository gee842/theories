#!/usr/bin/env python3
"""Plot every fixed contrast, with primary status and literal series meanings."""
from pathlib import Path
import hashlib
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

HERE=Path(__file__).resolve().parent
x=json.loads((HERE/'independent-results.json').read_text())
check=json.loads((HERE/'independent-verification.json').read_text())
assert check['status']=='passed'
assert hashlib.sha256((HERE/'independent-results.json').read_bytes()).hexdigest()==check['files_sha256']['independent-results.json']
rows=[('EXP2 early — primary',x['aggregate']['EXP2']['early']['opposed']),
      ('EXP2 late — secondary',x['aggregate']['EXP2']['late']['opposed']),
      ('EXP1 early — secondary',x['aggregate']['EXP1']['early']['opposed']),
      ('EXP1 late — secondary',x['aggregate']['EXP1']['late']['opposed']),
      ('EXP2 − EXP1 early — secondary',x['between_cohort']['early']),
      ('EXP2 − EXP1 late — secondary',x['between_cohort']['late'])]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,
                     'axes.spines.right':False,'axes.labelcolor':'#263645','text.color':'#263645'})
fig,(ax,scatter)=plt.subplots(1,2,figsize=(12.6,7.2),gridspec_kw={'width_ratios':[1.25,1]})
fig.subplots_adjust(left=.245,right=.97,top=.79,bottom=.31,wspace=.36)
fig.suptitle('Cost-switch data: paired behavior and identification limits',x=.04,ha='left',y=.97,fontsize=17,fontweight='bold')
fig.text(.04,.9,'Retrospective analysis of public binned saccade data • 20 participants per cohort',fontsize=11)
for n,(label,s) in enumerate(rows):
    color='#1b6580' if n==0 else '#657987'
    mean=s['mean'];lo,hi=s['ci95']
    ax.errorbar(mean,n,xerr=[[mean-lo],[hi-mean]],fmt='o',color=color,
                ecolor=color,markersize=7 if n==0 else 5,capsize=4,lw=2 if n==0 else 1.4)
ax.axvline(0,color='#a6b2bb',ls='--',lw=1)
ax.axhline(3.5,color='#d9e0e5',lw=1)
ax.set_yticks(range(len(rows)),[r[0] for r in rows])
ax.invert_yaxis();ax.set_xlim(-1.06,.65)
ax.set_title('All fixed contrasts and marginal 95% intervals',loc='left',fontsize=11,pad=17)
ax.set_xlabel('Source-series contrast (degrees)',labelpad=12)
ax.spines['left'].set_visible(False);ax.tick_params(axis='y',length=0,pad=9)
ax.get_yticklabels()[0].set_fontweight('bold')
a=[p['deltas']['LARGE COST']['early'] for p in x['participants']['EXP2']]
b=[p['deltas']['SMALL COST']['early'] for p in x['participants']['EXP2']]
scatter.scatter(a,b,s=34,color='#1b6580',alpha=.85,edgecolor='white',linewidth=.5)
limits=(min(a+b)-.1,max(a+b)+.1)
scatter.plot(limits,limits,color='#a6b2bb',ls='--',lw=1)
scatter.set_xlim(limits);scatter.set_ylim(limits);scatter.set_aspect('equal')
scatter.set_title('EXP2 early: the paired participant changes',loc='left',fontsize=11,pad=17)
scatter.set_xlabel('“LARGE COST” series: post − pre (°)')
scatter.set_ylabel('“SMALL COST” series: post − pre (°)')
fig.text(.04,.155,'Contrast = change in the source “SMALL COST” series minus change in “LARGE COST”.',fontsize=10)
fig.text(.04,.115,'Primary interval crosses zero. Secondary intervals do not replace the primary or identify an updater mechanism.',fontsize=10)
fig.text(.04,.075,'Windows use mean trial coordinates with a guard around 951. Opposed physical-side interpretation assumes retained initial-side labels.',fontsize=9)
fig.text(.04,.038,'Source: Sedaghat-Nejad & Shadmehr (2021), OSF H24J8. Original bin membership and trial-level teaching signals are unavailable here.',fontsize=9,color='#526572')
for suffix in ('png','svg'):
    fig.savefig(HERE/f'paired-contrasts.{suffix}',dpi=180,facecolor='white')
plt.close(fig)
(HERE/'figure-verification.json').write_text(json.dumps({'status':'generated; visual review separate','source_result_sha256':hashlib.sha256((HERE/'independent-results.json').read_bytes()).hexdigest(),'plot_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'matplotlib':matplotlib.__version__,'numpy':np.__version__,'files':{f'paired-contrasts.{s}':hashlib.sha256((HERE/f'paired-contrasts.{s}').read_bytes()).hexdigest() for s in ('png','svg')}},indent=2)+'\n')
print('Generated paired-contrasts.png and .svg from independently matched results.')
