"""Layout revision and local zoom; reads saved results without recalculating policies."""
from pathlib import Path
import json, hashlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
base=Path(__file__).resolve().parent
source=base/'results-v1/results.json';out=base/'figures-v2';out.mkdir(exist_ok=False)
data=json.loads(source.read_text())
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10})
fig,axs=plt.subplots(1,2,figsize=(11.8,4.8))
colors={'adaptive':'#246a73','no_test':'#ba6243','continuous':'#807589'}
labels={'adaptive':'Adaptive inquiry','no_test':'Ordinary evidence only','continuous':'Compulsory service'}
for series in data['main']:
    rr=[r for r in series['results'] if r['feasible']];mode=series['mode']
    axs[0].plot([r['budget'] for r in rr],[-r['metrics']['cost'] for r in rr],'o-',color=colors[mode],label=labels[mode],ms=4)
    if mode!='continuous':
        zoom=[r for r in rr if r['budget']<=.05]
        axs[1].plot([r['budget'] for r in zoom],[100*r['metrics']['failure'] for r in zoom],'o-',color=colors[mode],ms=4)
axs[0].set_ylabel('Expected objective value (−cost)');axs[0].set_title('Full declared budget range')
axs[1].set_ylabel('Probability of stock collapse (%)');axs[1].set_title('Detail: tight burden limits')
axs[1].annotate('17.52%',(.02,17.5176),xytext=(.025,20),arrowprops={'arrowstyle':'-','color':'#ba6243'},color='#994a30')
axs[1].annotate('12.44%',(.02,12.4389),xytext=(.025,9),arrowprops={'arrowstyle':'-','color':'#246a73'},color='#246a73')
for ax in axs:
    ax.set_xlabel('Allowed expected cumulative burden');ax.grid(alpha=.2)
axs[0].set_xlim(-.01,.61);axs[1].set_xlim(-.001,.051)
fig.suptitle('Recoverable inquiry with production-funded diagnosis and repair',fontsize=14)
fig.legend(*axs[0].get_legend_handles_labels(),loc='lower center',ncol=3,bbox_to_anchor=(.5,.055),frameon=False)
fig.text(.5,.025,'Eight periods. Compulsory service is infeasible below 0.371175 expected burden. This is not a pathwise harm guarantee.',ha='center',fontsize=8)
fig.subplots_adjust(top=.81,bottom=.24,wspace=.24,left=.07,right=.98)
fig.savefig(out/'frontier.png',dpi=180);fig.savefig(out/'frontier.svg')
(out/'manifest.json').write_text(json.dumps({'results_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'plot_code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))
