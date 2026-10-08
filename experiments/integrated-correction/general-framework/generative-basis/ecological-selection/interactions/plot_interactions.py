"""Descriptive figure: all original video means and technical-replicate means."""
import csv
from collections import defaultdict
from pathlib import Path
import statistics

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
data = defaultdict(lambda: defaultdict(list))
for r in csv.DictReader((HERE/'video-means.csv').open()):
    data[(r['species'],r['medium'],int(r['density_percent']))][int(r['technical_replicate'])].append(float(r['mean_velocity_mm_min']))
fig, axes = plt.subplots(1,2,figsize=(11.8,5),gridspec_kw={'width_ratios':[2,1]})
panels = [[('K. lactis','YPD',5),('K. lactis','YPD',100),('S. cerevisiae','YPD',5),('S. cerevisiae','YPD',100)],
          [('K. lactis','Galactose',100),('K. lactis','Dextrose',100)]]
labels = [['K. lactis\n5%','K. lactis\n100%','S. cerevisiae\n5%','S. cerevisiae\n100%'],
          ['Galactose\nblocked','Dextrose\nunblocked']]
for ax, groups, ticks in zip(axes,panels,labels):
    for x,key in enumerate(groups):
        color = '#146D85' if key[0]=='K. lactis' else '#A6611A'
        for rep,values in sorted(data[key].items()):
            center = x+(rep-2)*.19
            ax.scatter([center-.025,center,center+.025],values,color=color,alpha=.3,s=24)
            ax.scatter(center,statistics.mean(values),color=color,marker='D',s=45,zorder=3)
        avg = statistics.mean([statistics.mean(v) for v in data[key].values()])
        ax.hlines(avg,x-.38,x+.38,color='#222222',linewidth=1.5)
    ax.set_xticks(range(len(groups)),ticks,fontsize=10)
    ax.set_ylim(0,29)
    ax.set_ylabel('Settling velocity (mm/min)')
    ax.grid(axis='y',alpha=.2)
    ax.spines[['top','right']].set_visible(False)
axes[0].set_title('Density response in growth medium (YPD)')
axes[1].set_title('K. lactis: flocculation intervention')
fig.suptitle('Temporary association changes measured settling',fontsize=16,y=.99)
fig.text(.5,.025,'Faint dots: video means • Diamonds: technical-replicate means • Bars: condition means\n3 videos per technical replicate; 3 technical replicates per condition. No biological population confidence intervals.',ha='center',fontsize=10)
fig.tight_layout(rect=[0,.11,1,.95])
fig.savefig(HERE/'interaction-correspondence.png',dpi=180)
