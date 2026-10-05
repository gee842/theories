"""Scientific summary figure from saved calculations; no model fitting."""
from pathlib import Path
import hashlib
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

ROOT = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                     'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.titleweight': 'bold'})
fig, ax = plt.subplots(2,2, figsize=(13.4,9.4), layout='constrained')
fig.suptitle('Alignment as the Reproduction of Its Conditions\n'
             'Bounded models (A–C) and public experimental evidence (D)', fontsize=17)

a = ax[0,0]
b = np.linspace(0,.5,301)
nu=.1
blind=1-nu-(1-2*nu)*b
conditional=np.maximum(nu,1-nu-2*(1-2*nu)*b)
a.fill_between(b,conditional,.94,color='#c8e9e3',alpha=.65)
a.plot(b,blind,color='#8793a1',lw=2.3,label='Best blind response')
a.plot(b,conditional,color='#007f73',lw=2.5,label='Correct conditional response')
a.scatter([.40,.45],[.20,.20],c=['#b94432','#007f73'],s=52,zorder=5)
a.annotate('Infeasible',(.40,.20),xytext=(.26,.13),arrowprops={'arrowstyle':'-','color':'#b94432'},color='#9a3728')
a.annotate('Feasible',(.45,.20),xytext=(.35,.33),arrowprops={'arrowstyle':'-','color':'#007f73'},color='#007f73')
a.axhline(.2,color='#5d6570',ls=':',lw=1)
a.set(xlim=(0,.5),ylim=(.08,.94),xlabel='Allowed action burden',ylabel='Allowed harm in every context',
      title='A  New representation changes feasibility')
a.legend(loc='upper right',frameon=False,fontsize=9)
a.text(.02,.98,'Shading: conditional feasibility\nFixed physical noise = 0.10',
       transform=a.transAxes,va='top',fontsize=9)

c=json.loads((ROOT/'causal-results.json').read_text())
a=ax[0,1]
arms=c['accuracy_factorial']['0.95']['arms']
values=np.array([[arms[f'{i}{j}']['survival'] for j in (0,1)] for i in (0,1)])
a.imshow(values,cmap='YlGnBu',vmin=0,vmax=.1,aspect='auto')
for i in (0,1):
 for j in (0,1):
  a.text(j,i,f'{values[i,j]*100:.2f}%',ha='center',va='center',fontsize=20,
         color='white' if values[i,j]>.05 else '#25323c',fontweight='bold')
a.set(xticks=[0,1],xticklabels=['Blocked','Enabled'],yticks=[0,1],yticklabels=['Blocked','Enabled'],
      xlabel='Execution',ylabel='Evidence admission',title='B  Two repairs can require each other')
a.text(.5,-.26,'Chance of retaining skill through 200 periods\nSupplied gates; evidence accuracy = 0.95',
       transform=a.transAxes,ha='center',fontsize=9)

j=json.loads((ROOT/'formation-coupled'/'analysis.json').read_text())
a=ax[1,0]
lines=[('linked','Linked evidence','#007f73','-'),
       ('aggregate','Aggregate archive','#b47722','-'),
       ('training_blocked','Training unavailable','#b94432','-'),
       ('protected_succession','Protected benchmark','#5270ab','--')]
for key,label,color,ls in lines:
 curve=j['arms'][key]['curve']
 a.plot([x['round'] for x in curve],[x['plural_success'] for x in curve],lw=2.2,color=color,ls=ls,label=label)
a.set(xlim=(0,25),ylim=(0,1),xlabel='Round',ylabel='Probability of a compliant retained service policy',
      title='C  Discovery, training and turnover interact')
a.yaxis.set_major_formatter(PercentFormatter(1))
a.legend(loc='upper left',frameon=False,fontsize=9)
a.text(.02,.04,'Execution blocked or infeasible commitments: 0\nOrdinary service policy; inquiry harms separate',
       transform=a.transAxes,fontsize=9)

e=json.loads((ROOT/'empirical/results/analysis.json').read_text())['results']
lag=json.loads((ROOT/'empirical/results/succession_analysis.json').read_text())['result']
a=ax[1,1]
rs=[e['primary_information'],lag,e['boundary_authority_beneficiary']]
labels=['Accuracy → current\ncontribution (6 sessions)',
        'Accuracy → next-round\ninvestment (6 sessions)',
        'Authority benefits →\ncontribution (7 sessions)']
for y,(r,color) in enumerate(zip(rs,['#007f73','#b47722','#727b89'])):
 mean=100*r['equal_session_estimate'];lo,hi=[100*x for x in r['approximate_t95_interval']]
 a.errorbar(mean,y,xerr=[[mean-lo],[hi-mean]],fmt='o',color=color,lw=2,capsize=4,markersize=7)
a.axvline(0,color='#7f8994',lw=1,ls=':')
a.set(yticks=range(3),yticklabels=labels,ylim=(2.6,-.65),xlim=(-15,22),
      xlabel='Estimated effect (percentage points)',title='D  Separate tests of action and reinvestment')
a.text(.02,.02,'Approximate session-based 95% intervals\nPublic human experiments; different endpoints',
       transform=a.transAxes,fontsize=9,va='bottom')

fig.savefig(ROOT/'research-summary.png',dpi=180)
fig.savefig(ROOT/'research-summary.svg')
inputs=['render.py','causal-results.json','formation-coupled/analysis.json',
        'empirical/results/analysis.json','empirical/results/succession_analysis.json']
(ROOT/'figure-manifest.json').write_text(json.dumps({
    'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
    'description':'Figure panels use separate supplied models and distinct experimental endpoints; no pooled effect.'
},indent=2)+'\n')
print(ROOT/'research-summary.png')
