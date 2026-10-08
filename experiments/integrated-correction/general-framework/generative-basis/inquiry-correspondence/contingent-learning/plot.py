"""Scientific plot from the preserved computed results; no new analysis."""
import csv
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

HERE=Path(__file__).resolve().parent
r=json.loads((HERE/'results.json').read_text())['primary']
with (HERE/'participant-summaries.csv').open() as f: rows=list(csv.DictReader(f))
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,(ax,bx)=plt.subplots(1,2,figsize=(11.5,4.8),gridspec_kw={'width_ratios':[1.2,1]})
colors=['#137E85','#637DB0','#B37636']
for i,(name,color) in enumerate(zip(['curiosity','yoked','random'],colors)):
    xs=np.array([float(x['mean'])*100 for x in rows if x['condition']==name])
    jitter=np.random.default_rng(43+i).uniform(-.16,.16,len(xs))
    ax.scatter(i+jitter,xs,s=23,color=color,alpha=.6,zorder=2)
    g=r['groups'][name]; mean=g['mean']*100;lo,hi=np.array(g['ci95'])*100
    ax.errorbar(i+.25,mean,yerr=[[mean-lo],[hi-mean]],fmt='s',color='#202D3B',capsize=4,zorder=3)
ax.axhline(0,color='#8A9099',lw=1,ls='--');ax.set_xticks(range(3),['Curiosity','Yoked','Random'])
ax.set_ylabel('Change in target looking (percentage points)')
ax.set_title('Participant outcomes · 25 per condition',loc='left',fontweight='bold')
ax.set_xlim(-.4,2.5)
for i,key in enumerate(['curiosity_minus_yoked','curiosity_minus_random']):
    g=r['contrasts'][key];d=g['difference']*100;lo,hi=np.array(g['ci95'])*100
    bx.errorbar(d,i,xerr=[[d-lo],[hi-d]],fmt='o',color='#137E85',capsize=5,lw=2)
    bx.text(d,i+.17,f'{d:+.1f}  [{lo:+.1f}, {hi:+.1f}]',ha='center',fontsize=10)
bx.axvline(0,color='#8A9099',lw=1,ls='--');bx.set_yticks([0,1],['Curiosity − Yoked','Curiosity − Random']);bx.set_ylim(-.45,1.6)
bx.set_xlabel('Difference in change (percentage points)')
bx.set_xlim(-13,12);bx.set_title('Unadjusted 95% Welch intervals',loc='left',fontweight='bold')
fig.suptitle('Encounter control does not establish a retention advantage here',x=.055,ha='left',fontsize=15,fontweight='bold')
fig.text(.055,.03,'Secondary analysis of CuriGaze public summaries. Intervals assume independent participants;\nyoking dependence and sequential-design coverage are not resolved. Zero within an interval does not establish equivalence.',fontsize=9,color='#46505E')
fig.subplots_adjust(left=.08,right=.98,bottom=.24,top=.81,wspace=.53)
for suffix in ['png','svg']:fig.savefig(HERE/('control-retention.'+suffix),dpi=180,facecolor='white')
