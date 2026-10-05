"""Render the declared named cases as a scientific figure (matplotlib required)."""
from pathlib import Path
import json
from fractions import Fraction
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out=Path(__file__).resolve().parent/'results'
data=json.loads((out/'named-cases.json').read_text())
fig,axes=plt.subplots(1,2,figsize=(12,5.5))
cases=[('positive','Paid reconstruction','#217c79'),
       ('free_identity_filter','Free identity filter','#924265'),
       ('cheap_reserve_raid','Cheap recurring raid','#bd6a28')]
for name,label,color in cases:
    d=data[name]; path=d['path']
    xs=list(range(len(path)+1))
    cash=[d['opening_cash']]+[float(Fraction(r['closing_cash'])) for r in path]
    harms=[0]
    for r in path:
        harms.append(harms[-1]+float(Fraction(r['patient_harm'])))
    style='o--' if name=='free_identity_filter' else 'o-'
    layer=3 if name=='free_identity_filter' else 2
    axes[0].plot(xs,cash,style,label=label,color=color,lw=2.3,zorder=layer)
    axes[1].plot(xs,harms,style,label=label,color=color,lw=2.3,zorder=layer)
axes[0].set_ylabel('Shared account after each episode')
axes[1].set_ylabel('Cumulative actual patient harm')
axes[0].set_title('More money need not mean more concern')
axes[1].set_title('Renewal can protect or reproduce exclusion')
axes[1].text(.97,.46,'The two failure curves coincide',transform=axes[1].transAxes,ha='right',fontsize=9)
axes[0].legend(frameon=False,loc='upper left')
axes[1].legend(frameon=False,loc='upper left')
for ax in axes:
    ax.set_xlabel('Completed episodes')
    ax.spines[['top','right']].set_visible(False)
    ax.grid(axis='y',alpha=.15)
    ax.set_xticks(range(7))
fig.suptitle('Joint formation has a protected cycle and explicit failure cycles',fontsize=15,y=.97)
fig.text(.5,.02,'Exact constructed game; each controller starts with zero learned concern. Model outcomes, not empirical data.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.045,1,.91))
fig.savefig(out/'joint-formation-and-failure.png',dpi=180)
fig.savefig(out/'joint-formation-and-failure.svg')
