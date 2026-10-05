from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

ROOT=Path(__file__).resolve().parent
results=json.loads((ROOT/'results/summary.json').read_text())
rows=results['rows']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
policies=['direct','retained','audit','joint_y_only','joint']
labels=['Use current reference only','Retain a bias correction','Audit the correction','Joint estimate, ordinary data','Joint estimate, optional reference']
worlds=['constant','switch30','reference_bias','no_bias','switch32']
world_labels=['Constant\nbias','Change at\nstep 30','Biased\nreference','No\nbias','Change at\nstep 32*']
fig,axs=plt.subplots(1,2,figsize=(14,5.6))
fig.subplots_adjust(left=.255,right=.95,top=.80,bottom=.20,wspace=.07)
for ax,stage,title in zip(axs,['matched','adaptive'],['Same 12 reference packets','Optional reference, at most 6 purchases']):
    data=np.array([[next(r['total_loss'] for r in rows if r['stage']==stage and r['world']==w and r['policy']==p) for w in worlds] for p in policies])
    im=ax.imshow(data,cmap='YlOrRd',norm=LogNorm(vmin=.5,vmax=30),aspect='auto')
    ax.set_xticks(range(5),world_labels)
    ax.set_yticks(range(5),labels if stage=='matched' else [])
    ax.set_title(title,fontsize=13,fontweight='bold',pad=14)
    for i in range(5):
        for j in range(5):ax.text(j,i,f'{data[i,j]:.2f}',ha='center',va='center',fontsize=11,color='white' if data[i,j]>8 else '#181818')
fig.colorbar(im,ax=axs,shrink=.85,label='Mean total loss · lower is better')
fig.suptitle('How the model uses evidence matters more than its level label',fontsize=16,fontweight='bold',y=.98)
fig.text(.02,.035,'Synthetic results: 1,000 paired seeds per cell. Loss includes state, action, sensing and declared work costs. Color scale is logarithmic.\n*Timing control was not used for tuning.',fontsize=9,color='#555555')
fig.savefig(ROOT/'results-overview.png',dpi=180,bbox_inches='tight')
fig.savefig(ROOT/'results-overview.svg',bbox_inches='tight')

fig,axs=plt.subplots(1,2,figsize=(13,5.1))
colors={'switch30':'#168775','switch32':'#C65336'}
for world in ['switch30','switch32']:
    trace=np.load(ROOT/f'results/trace-adaptive-{world}-audit.npy')
    label='Change at '+('30' if world=='switch30' else '32')
    axs[0].plot(trace[:,0],trace[:,7],color=colors[world],label=label,lw=2)
    mask=trace[:,13]>0
    axs[0].scatter(trace[mask,0],trace[mask,7],s=45,color=colors[world],edgecolor='white',zorder=3)
    axs[0].plot(trace[:,0],trace[:,1],ls=':',color=colors[world],alpha=.55,lw=1)
axs[0].axhline(-1,ls='--',color='#777777',lw=1)
axs[0].annotate('New true bias = −1',xy=(41,-1),xytext=(32,-1.45),fontsize=9)
axs[0].set(title='A  A two-step timing change delays correction',xlabel='Time step',ylabel='Bias estimate (solid); state (dotted)')
axs[0].legend(frameon=False,loc='lower left',fontsize=9)
axs[0].set_ylim(-1.75,1.65)
axs[0].text(.02,.94,'Dots mark paid checks; illustrative seed 1000',transform=axs[0].transAxes,fontsize=9)
coverage=[];width=[]
for p in ['retained','audit','joint_y_only','joint']:
    r=next(r for r in rows if r['stage']=='matched' and r['world']=='reference_bias' and r['policy']==p)
    coverage.append(100*r['coverage90']);width.append(r['interval90_width'])
axs[1].bar(range(4),coverage,color=['#5C7BA6','#7C699A','#B48C3A','#168775'],width=.62)
axs[1].axhline(90,ls='--',color='#333333',lw=1)
axs[1].set_xticks(range(4),['Retained','Audit','Joint\nordinary','Joint with\nreference'])
axs[1].set(title='B  Good control can coexist with overconfidence',ylabel='Coverage of nominal 90% forecast interval (%)',ylim=(0,105))
for i,(c,w) in enumerate(zip(coverage,width)):
    axs[1].text(i,c+2,f'{c:.1f}%',ha='center',fontsize=10)
    axs[1].text(i,6,f'width\n{w:.2f}',ha='center',fontsize=9,color='white')
fig.suptitle('When a correction mechanism misses its own changed conditions',fontsize=15,fontweight='bold',y=.99)
fig.tight_layout(rect=(0,.12,1,.88))
fig.text(.02,.012,'A: adaptive sensing, one prespecified trace. B: biased reference, matched sensing, 1,000 seed trajectories. Interval widths are in state units.',fontsize=9,color='#555555')
fig.savefig(ROOT/'timing-and-calibration.png',dpi=180,bbox_inches='tight')
fig.savefig(ROOT/'timing-and-calibration.svg',bbox_inches='tight')
print('Saved two figures.')
