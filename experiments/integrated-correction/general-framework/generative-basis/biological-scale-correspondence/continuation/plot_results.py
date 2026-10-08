#!/usr/bin/env python3
"""Scientific figure from the preserved analysis; no new fits."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
r=json.loads((P/'results.json').read_text())
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,2,figsize=(14,5.6))
fig.subplots_adjust(left=.255,right=.98,bottom=.25,top=.80,wspace=.40)
names=['constant','current_density','density_satiety','nonlinear_no_density_history','history']
labels=['Constant','Current density','Density + time off food','Nonlinear density + time','Density + time + prior densities']
vals=[r['cross_validation_scores'][n]['soft_cross_entropy'] for n in names]
axes[0].barh(labels,vals,color=['#B7C4CC']*4+['#237C82'])
axes[0].invert_yaxis();axes[0].set_xlim(0,.76)
for y,v in enumerate(vals):axes[0].text(v+.007,y,f'{v:.3f}',va='center')
axes[0].set_xlabel('Held-out soft cross entropy (lower is better)')
axes[0].set_title('A   Foraging: 198 worms, grouped five-fold test',loc='left',pad=15,fontsize=11)
rng=np.random.default_rng(20261008)
for i,key in enumerate(['standard_plate','full_plate']):
    v=np.array(r['pathogen_fluorescence'][key]['values'])
    axes[1].scatter(i+rng.uniform(-.14,.14,len(v)),v,s=24,alpha=.7,color=['#237C82','#AF6953'][i])
    axes[1].plot([i-.22,i+.22],[v.mean()]*2,color='#182D3A',lw=2.5)
    axes[1].text(i,v.max()+200,f'n={len(v)}',ha='center')
axes[1].set_xticks([0,1],['Avoidance available\nstandard lawn','Avoidance restricted\nfull lawn'])
axes[1].set_ylabel('Rectal SYTO13 fluorescence (arbitrary units)')
axes[1].set_xlim(-.6,1.6)
axes[1].set_title('B   Separate pathogen experiment',loc='left',pad=15,fontsize=11)
fig.suptitle('History improves prediction; changed access changes later microbial burden',fontsize=14,y=.97)
fig.text(.03,.055,'A: fixed behavioral classifiers and imputations; conditional prediction test.  B: individual measurements; no plate-level error bars.\nSources: Haley et al. (2025), eLife 103191; Anderson & McMullan (2018), doi:10.1098/rstb.2017.0255.',fontsize=9,color='#43535B')
fig.savefig(P/'continuation-results.png',dpi=180)
fig.savefig(P/'continuation-results.svg')
