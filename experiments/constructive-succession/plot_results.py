from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
main = json.loads((HERE/'results/summary.json').read_text())['groups']
access = json.loads((HERE/'results-access/summary.json').read_text())['groups']
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':11,
                     'axes.spines.top':False, 'axes.spines.right':False})
fig, axes = plt.subplots(1, 2, figsize=(13, 7), gridspec_kw={'width_ratios':[1, 1.22]})
fig.subplots_adjust(left=.14, right=.975, bottom=.30, top=.78, wspace=.65)
fig.suptitle('Inherited material can help retrieval and hinder construction',
             fontsize=19, fontweight='bold', x=.06, ha='left', y=.96)
fig.text(.06,.895,'Paid Boolean-program synthesis; bounded, exploratory computational study',
         fontsize=12,color='#555555')

policies = ['solution','closest','diverse','recent']
labels = ['Source only','+ Similar','+ Diverse','+ Recent']
rows = [next(g for g in main if g['regime']=='local' and g['flow']==1200
             and g['archive_price']==2 and g['reserve_quarters']==1 and g['policy']==p)
        for p in policies]
y = np.arange(4)
reuse = [r['direct_reuses'] for r in rows]
new = [r['new_compositions'] for r in rows]
axes[0].barh(y,reuse,color='#7896ac',label='Inherited exact answer')
axes[0].barh(y,new,left=reuse,color='#19685a',label='New composition')
for i,r in enumerate(rows):
    axes[0].text(r['successes']+1,i,str(r['successes']),va='center',fontsize=11)
axes[0].set_yticks(y,labels)
axes[0].invert_yaxis()
axes[0].set_xlim(0,75)
axes[0].set_xlabel('Correct installations (256 successor tasks)', fontsize=10)
axes[0].set_title('Four successive handoffs\nRelated targets, fixed cost and reserve rule',
                  loc='left',fontsize=12,pad=16)
fig.legend(*axes[0].get_legend_handles_labels(),loc='lower left',
           bbox_to_anchor=(.135,.17),frameon=False,fontsize=10,ncol=2)

group = next(g for g in access if g['policy']=='diverse' and g['flow']==1200
             and g['reserve_quarters']==0)
both = group['all_active_successes']-len(group['active_only_successes'])
neither = 256-both-len(group['active_only_successes'])-len(group['dormant_only_successes'])
cells = [both,len(group['active_only_successes']),len(group['dormant_only_successes']),neither]
names = ['Both succeed','Active extras only','Dormant extras only','Neither succeeds']
colors = ['#7896ac','#19685a','#d49547','#d7dce0']
axes[1].barh(y,cells,color=colors)
for i,c in enumerate(cells):
    axes[1].text(c+3,i,str(c),va='center')
axes[1].set_yticks(y,names)
axes[1].invert_yaxis()
axes[1].set_xlim(0,195)
axes[1].set_xlabel('Number of targets out of all 256 functions')
axes[1].set_title('Same inherited package and resources\nOnly its use in search changes',
                  loc='left',fontsize=12,pad=16)
fig.text(.06,.055,'Left: 64 paired task sequences, four tasks each; these are not 256 independent trials.\n'
         'Right: exhaustive one-step comparison. Dormant material remains available for exact retrieval.\n'
         'Neither access rule dominates: they make different constructions reachable within the same budget.',
         fontsize=10,color='#444444',linespacing=1.5)
fig.savefig(HERE/'results/constructive-succession.png',dpi=170)
fig.savefig(HERE/'results/constructive-succession.svg')
