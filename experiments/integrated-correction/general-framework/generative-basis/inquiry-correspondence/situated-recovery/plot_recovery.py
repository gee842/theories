#!/usr/bin/env python3
"""Plot measured terminal histories, individual endpoints and held-out errors."""
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
r=json.loads((P/'results.json').read_text());rows=json.loads((P/'observations.json').read_text())
s=json.loads((P/'sensitivity-results.json').read_text())
groups=['spontaneous_recovery','evoked_recovery'];colors=['#306B91','#A8532E']
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none'})
fig,axs=plt.subplots(2,2,figsize=(11,7.3),layout='constrained')
for i,(g,color) in enumerate(zip(groups,colors)):
 ax=axs[0,i]; t=np.arange(191,341);ys=[]
 for p in range(1,9):
  z={o['trial']:o['adaptation'] for o in rows if o['group']==g and o['participant']==p and o['adaptation'] is not None}
  y=np.array([z.get(int(k),np.nan) for k in t]);ys.append(y);ax.plot(t,y,color=color,alpha=.13,lw=.8)
 ys=np.array(ys);valid=~np.all(np.isnan(ys),axis=0)
 mean=np.full(150,np.nan);se=mean.copy();mean[valid]=np.mean(ys[:,valid],axis=0);se[valid]=np.std(ys[:,valid],axis=0,ddof=1)/np.sqrt(8)
 ax.plot(t,mean,color=color,lw=2.2);ax.fill_between(t,mean-se,mean+se,color=color,alpha=.17)
 ax.axhline(0,color='#666666',lw=.8);ax.axvspan(290.5,340,color='#E5DCC6',alpha=.35)
 ax.set(xlim=(190,341),ylim=(-.6,1.2),xlabel='Actual trial number',ylabel='Adaptation (original signed scale)',title=('Spontaneous recovery' if i==0 else 'Evoked recovery')+' | 8 participants')
 ax.text(.98,.96,'Held out: trials 291–340',ha='right',va='top',transform=ax.transAxes,fontsize=9)
ax=axs[1,0]
for i,(g,color) in enumerate(zip(groups,colors)):
 y=np.array([p['late_baseline_corrected'] for p in r['participants'] if p['group']==g]);jitter=np.linspace(-.12,.12,8)
 ax.scatter(i+jitter,y,color=color,s=28,zorder=3)
 stat=r['groups'][g]['late_baseline_corrected'];lo,hi=stat['ci95'];m=stat['mean']
 ax.errorbar(i+.23,m,yerr=[[m-lo],[hi-m]],fmt='D',color=color,capsize=4)
ax.axhline(0,color='#777777',lw=.8);ax.set(xticks=[0,1],xticklabels=['Spontaneous','Evoked'],ylabel='Final 50-trial mean minus baseline',title='Individual retained responses')
ax.text(.02,.98,'Dots: participants; diamonds: group means\nBars: participant-bootstrap 95% intervals',va='top',transform=ax.transAxes,fontsize=9)
ax=axs[1,1]
models=['zero_level_decay','fitted_level_relaxation','constant_calibration_mean','last_observation']
labels=['Zero-level\ndecay','Fitted\nlevel','Constant\nmean','Last\nobservation']
x=np.arange(4)
for i,(g,color) in enumerate(zip(groups,colors)):
 vals=[r['groups'][g]['forecast_raw'][m]['mean_participant_rmse'] for m in models]
 ax.bar(x+(i-.5)*.32,vals,.3,color=color,label='Spontaneous' if i==0 else 'Evoked')
ax.set(xticks=x,xticklabels=labels,ylabel='Mean participant RMSE on held-out trials',title='More parameters do not always predict better',ylim=(0,.21));ax.legend(frameon=False,fontsize=9)
fig.suptitle('Published human recovery data: finite retention and forecast limits',fontsize=15)
fig.savefig(P/'recovery-results.png',dpi=180)
fig.savefig(P/'recovery-results.svg')
