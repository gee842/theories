"""Render the frozen main result using Matplotlib; no data fitting."""
from pathlib import Path
import sys,json
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'plot-libraries'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

rows=json.loads((HERE/'results/main.json').read_text())
out=HERE.parent.parent/'outputs'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,
                    'axes.spines.right':False,'axes.titleweight':'bold'})
fig,axes=plt.subplots(1,3,figsize=(13,4.9),sharey=True)
styles={
    'barred':dict(color='#243b6b',marker='o',linestyle='-',linewidth=2.2,markersize=6,label='Treasury barred'),
    'delayed':dict(color='#dc8836',marker='s',linestyle='--',linewidth=2.1,markersize=7,markerfacecolor='none',label='Access from round 2'),
    'immediate':dict(color='#168878',marker='x',linestyle=':',linewidth=2.2,markersize=7,label='Immediate access'),
}
for x,ax in zip((1,2,3),axes):
    for mode in ('barred','delayed','immediate'):
        relevant=sorted((r for r in rows if r['initial']['stock']==x and r['initial']['belief']=='1'
                         and r['initial']['access']==mode),key=lambda r:r['initial']['cash'])
        ax.plot([r['initial']['cash'] for r in relevant],
                [r['probes']['failure']['metrics']['failure'] for r in relevant],**styles[mode])
    ax.set_title(f'Initial productive stock {x}',pad=13)
    ax.set_xlabel('Initially spendable funds')
    ax.set_xticks(range(6));ax.set_xlim(-.15,5.15);ax.set_ylim(-.025,.9)
    ax.grid(axis='y',alpha=.18)
axes[0].set_ylabel('Minimum collapse probability by round 4')
axes[0].yaxis.set_major_formatter(PercentFormatter(1,decimals=0))
axes[1].annotate('61.2%',(0,.612),xytext=(.6,.65),fontsize=11,color='#243b6b',
                 arrowprops={'arrowstyle':'-','color':'#243b6b'})
axes[1].annotate('1.36%',(1,.0136),xytext=(1.3,.2),fontsize=11,color='#243b6b',
                 arrowprops={'arrowstyle':'-','color':'#243b6b'})
axes[2].text(.5,.47,'All three access modes\nattain zero collapse here',transform=axes[2].transAxes,
             ha='center',va='center',color='#46505c',fontsize=11)
fig.suptitle('Equal total funds do not always give equal recovery possibilities',x=.06,ha='left',fontsize=17,y=.98)
fig.text(.06,.90,'Five total units in every case · current fault known · diagnostic initially unready',fontsize=11,color='#46505c')
handles,labels=axes[0].get_legend_handles_labels()
fig.legend(handles,labels,loc='lower center',bbox_to_anchor=(.52,.075),ncol=3,frameon=False)
fig.text(.06,.025,'Exact constructed model. These optima use direct repair, with no paid diagnostic tests.',fontsize=10,color='#46505c')
fig.subplots_adjust(left=.07,right=.98,top=.78,bottom=.25,wspace=.16)
fig.savefig(out/'access-outcomes.png',dpi=180,facecolor='white')
fig.savefig(out/'access-outcomes.svg',facecolor='white')
print(str(out/'access-outcomes.png'))
