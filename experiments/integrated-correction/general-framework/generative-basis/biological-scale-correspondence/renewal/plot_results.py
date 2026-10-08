#!/usr/bin/env python3
"""Static research figure; distinct datasets are separate panels, not one trajectory."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

P=Path(__file__).resolve().parent
r=json.loads((P/'results.json').read_text())
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,3,figsize=(14,5.4))
fig.subplots_adjust(left=.07,right=.985,bottom=.27,top=.79,wspace=.40)
fig.suptitle('Measured memory, calibration and later microbial conditions',fontsize=16,fontweight='bold',y=.95)
a=axes[0]
v=r['memory']['panels']['choice_generations']['trained_minus_control']
a.bar(list(v),list(v.values()),color=['#287d8e']*5+['#c25b45'])
a.axhline(0,color='#333333',linewidth=.8)
a.set(title='A · Pv1 study: retained response',ylabel='Mean choice index: trained − control',ylim=(-.05,.47))
a.text(.02,.97,'Descriptive plate means\nDifferent cohorts at each generation',va='top',transform=a.transAxes,fontsize=8)
a.set_xlabel('P0 trained; descendants raised on OP50')
a=axes[1]
cal=r['calibration']
for condition,color in [('CM100','#287d8e'),('CM250','#4661a3'),('CM500','#ba8a31'),('CM25','#c25b45')]:
    rows=[v for v in cal['test'] if v['condition']==condition]
    a.scatter([v['log10_cfu'] for v in rows],[v['predictions']['inverse_tanh'] for v in rows],
              s=22,alpha=.75,color=color,label=condition+(' (new)' if condition=='CM25' else ''))
a.plot([0,7],[0,7],color='#444444',linestyle='--',linewidth=1)
a.set(title='B · Matched fluorescence → viable count',xlabel='Observed log₁₀ CFU / worm',ylabel='Predicted log₁₀ CFU / worm',xlim=(0,7),ylim=(0,7))
a.legend(loc='upper left',fontsize=8,frameon=False)
a.text(.97,.04,'Train: 70 positive-count T48 worms\nTest: 96 T72 worms\nRMSE 0.663; bias −0.197',ha='right',va='bottom',transform=a.transAxes,fontsize=8)
a=axes[2]
conditions=['High +','High -','Low +','Low -']
colors=['#287d8e','#4661a3','#ba8a31','#c25b45']
for run,marker,offset in [(1,'o',-.09),(2,'s',.09)]:
    for i,(cond,color) in enumerate(zip(conditions,colors)):
        g=next(v for v in r['migration'][run-1]['groups'] if v['time']=='T48' and v['condition']==cond)
        s=g['log10_green'];a.errorbar(i+offset,s['median'],yerr=[[s['median']-s['q25']],[s['q75']-s['median']]],
                                   fmt=marker,color=color,capsize=3,label=f'Run {run}' if i==0 else None)
        a.annotate(str(s['n']),(i+offset,s['q75']),xytext=(0,5 if run==1 else 16),textcoords='offset points',ha='center',fontsize=7)
a.set(title='C · Later sorted-cohort distributions',xticks=range(4),xticklabels=['High\n+','High\n−','Low\n+','Low\n−'],ylabel='T48 log₁₀ fluorescence: median and IQR',ylim=(1.3,4.4))
a.legend(loc='upper left',fontsize=8,frameon=False)
a.set_xlabel('Initial load / migration (+ or −); labels: n')
for axis in axes:
    axis.title.set_fontsize(10)
fig.text(.5,.015,'Separate preparations; no individual joins across panels. Neuronal signal, learned motion and ecological reproduction have not been jointly calibrated.\nCFU zeros remain in the source audit; calibration is conditional on positive counts. No new biological experiment or uniform error bound.',ha='center',va='bottom',fontsize=9)
for suffix in ['png','svg']:
    fig.savefig(P/('renewal-results.'+suffix),dpi=170)
