#!/usr/bin/env python3
"""Plot fixed held-out comparisons; values below one favor the numerator."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
H=Path(__file__).resolve().parent
result=json.loads((H/'predictive-calibration-results.json').read_text())
S={(s['run'],s['fit_run'],s['channel'],s['model'],s['lag']):s for s in result['summary']}
fig,axes=plt.subplots(1,2,figsize=(12,3.8),layout='constrained')
for ax,top,bottom,title in zip(axes,['local6','coupled6'],['persistence','local6'],['Local history / retained reading','Coupled channels / local history (equal size)']):
    ratio=np.asarray([[S[r,r,c,top,h]['rmse_C']/S[r,r,c,bottom,h]['rmse_C'] for c in [1,2] for h in [1,2,5]] for r in ['physics','arx','ann']])
    ax.imshow(np.log2(ratio),cmap='RdBu_r',norm=TwoSlopeNorm(vmin=-2,vcenter=0,vmax=2),aspect='auto')
    for i in range(3):
        for j in range(6):ax.text(j,i,f'{ratio[i,j]:.2f}',ha='center',va='center',color='white' if abs(np.log2(ratio[i,j]))>1.3 else '#171717',fontsize=11)
    ax.set_xticks(range(6),['T1: 1','T1: 2','T1: 5','T2: 1','T2: 2','T2: 5']);ax.set_yticks(range(3),['Physics','ARX','ANN']);ax.set_title(title,fontsize=12);ax.set_xlabel('Channel: forecast horizon in observation steps')
fig.suptitle('Held-out RMSE ratios — below 1 means lower error',fontsize=15)
fig.supxlabel('Exploratory archived-run analysis. Overlapping forecasts; no causal or future-coverage guarantee.',fontsize=10)
fig.savefig(H/'predictive-calibration-comparison.png',dpi=170)
fig.savefig(H/'predictive-calibration-comparison.svg')
print('Saved PNG and SVG')
