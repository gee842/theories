"""Static scientific figure from the exact game; plotting needs matplotlib."""
import json
from pathlib import Path
from fractions import Fraction as Q
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from model import Model, Game, trace_summary

root=Path(__file__).resolve().parent
out=root/'results'
witness=json.loads((out/'witnesses.json').read_text())
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig=plt.figure(figsize=(12,7),layout='constrained')
gs=fig.add_gridspec(2,2,height_ratios=[1.8,1])
ax=fig.add_subplot(gs[0,0])
ws=list(range(2,9))
for persistent,color,marker,label in [(False,'#2b7a78','o','A fresh operator each period'),(True,'#8b3d62','s','One persistent operator')]:
    vals=[trace_summary(Game(Model(),persistent).solve(0,w),w)['safeguarded_participations'] for w in ws]
    ax.step(ws,vals,where='post',marker=marker,color=color,lw=2,label=label)
ax.axvspan(2,4,alpha=.09,color='#666666');ax.axvspan(4,5,alpha=.12,color='#df9d35');ax.axvspan(5,8,alpha=.08,color='#2b7a78')
ax.axvline(4,ls=':',color='#888888');ax.axvline(5,ls=':',color='#888888')
ax.set(xlabel='Initial participant reserve (at least 2)',ylabel='Protected periods out of two',yticks=[0,1,2],xticks=ws,ylim=(-.1,2.3),title='A  Affordability and strategic resilience differ')
ax.legend(loc='lower right',fontsize=8,frameon=False)

ax=fig.add_subplot(gs[0,1])
labels=['Fresh\nreserve 4','Persistent\nreserve 4','Persistent\nreserve 5','Forced upkeep\nreserve 4']
seqs=[witness['affordable_but_vulnerable']['fresh']['optimal'],witness['affordable_but_vulnerable']['persistent']['optimal'],witness['one_more_unit_of_reserve']['persistent']['optimal'],witness['affordable_but_vulnerable']['persistent']['always']]
for idx,s in enumerate(seqs):
    values=[s['path'][0]['cash_before']]+[z['cash_after'] for z in s['path']]
    color=['#2b7a78','#8b3d62','#386cb0','#bb6f27'][idx]
    ax.plot(range(3),values,marker='o',label=labels[idx].replace('\n',' '),color=color,lw=2)
ax.set(xlabel='Completed periods',ylabel='Cash after receipts',xticks=[0,1,2],title='B  A blockade can remove the next upkeep budget')
ax.legend(frameon=False,fontsize=8,loc='upper left')

ax=fig.add_subplot(gs[1,:]);ax.axis('off')
rows=[['Below 4','No active alternative','Startup and the first operating bill cannot be funded.'],['4 to below 5','Activation deferred','A prospective block would remove next-period operating funds.'],['5 or more','Protection in both periods','Even after a prospective block, next upkeep remains affordable.']]
tab=ax.table(cellText=rows,colLabels=['Initial reserve','Persistent-operator outcome','Mechanism in this exact two-period class'],cellLoc='left',colLoc='left',loc='upper center',colWidths=[.14,.22,.64])
tab.auto_set_font_size(False);tab.set_fontsize(9);tab.scale(1,1.8)
for (r,c),cell in tab.get_celld().items():
    cell.set_edgecolor('#dddddd')
    if r==0:cell.set_facecolor('#edf1f5');cell.set_text_props(weight='bold')
fig.suptitle('Correction must remain affordable after another actor responds',fontsize=17,fontweight='bold')
fig.supxlabel('Exact constructed game: b=5, x=ell=2, o=4, K=m=c=1, r=4, chi=1.5. These are model results, not measured institutions.',fontsize=9)
fig.savefig(out/'formation-and-strategic-reserve.png',dpi=170)
fig.savefig(out/'formation-and-strategic-reserve.svg')
print(out/'formation-and-strategic-reserve.png')
