from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent
data = json.loads((root/'results/analysis.json').read_text())['arms']
curves = np.load(root/'results/curves.npz')
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                     'axes.spines.top': False, 'axes.spines.right': False})
fig, axes = plt.subplots(2, 2, figsize=(12.6, 8.8))
colors = {'protected': '#247b5e', 'rare_adverse': '#6e55a5',
          'endogenous': '#226b9e', 'reentry': '#c07c24',
          'no_admission': '#b8535c', 'volume_only': '#737b83',
          'fixed_criterion': '#6095a5', 'perfect_inquiry': '#67a191'}
labels = {'protected': 'Protected succession', 'rare_adverse': 'Rare adverse succession',
          'endogenous': 'Endogenous succession', 'reentry': 'Outside re-entry',
          'no_admission': 'Evidence not admitted', 'volume_only': 'Volume-only successors',
          'fixed_criterion': 'Criterion feedback removed', 'perfect_inquiry': 'Perfect inquiry'}

ax = axes[0, 0]
for name in ('protected', 'rare_adverse', 'endogenous', 'no_admission'):
    ax.plot(curves[name+'_survival'], label=labels[name], color=colors[name], lw=2)
ax.set_yscale('log'); ax.set_ylim(1e-6, 1.2); ax.set_xlim(0, 2000)
ax.set_title('A  Probability of uninterrupted skill retention', loc='left', fontweight='bold')
ax.set_xlabel('Periods'); ax.set_ylabel('Probability (log scale)')
ax.legend(frameon=False, fontsize=8.5)
ax.grid(alpha=.15)

ax = axes[0, 1]
names = ['protected', 'rare_adverse', 'perfect_inquiry', 'endogenous',
         'no_admission', 'fixed_criterion']
values = [100*data[n]['checkpoints']['200']['never_lost_capacity'] for n in names]
y = np.arange(len(names))
ax.barh(y, values, color=[colors[n] for n in names], height=.65)
ax.set_yticks(y, [labels[n] for n in names], fontsize=9)
ax.invert_yaxis(); ax.set_xlim(0, 117)
for pos, value in zip(y, values):
    ax.text(value+1, pos, f'{value:.2f}%', va='center', fontsize=9)
ax.set_xticks([0, 25, 50, 75, 100]); ax.set_xlabel('Never reached zero skill by period 200 (%)')
ax.set_title('B  Skill retained through 200 periods', loc='left', fontweight='bold')

ax = axes[1, 0]
ax.plot(curves['reentry_capacity_occupancy'], color=colors['reentry'], lw=2,
        label='Capacity currently present, with re-entry')
ax.plot(curves['reentry_survival'], color=colors['endogenous'], lw=2, ls='--',
        label='Capacity never lost, with re-entry')
limit = data['reentry']['limiting']['positive_capacity_fraction']
ax.axhline(limit, color=colors['reentry'], lw=1, alpha=.5)
ax.text(1060, limit+.035, f'Long-run occupancy {limit:.1%}', color=colors['reentry'])
ax.set_xlim(0, 2000); ax.set_ylim(0, 1.04)
ax.set_title('C  Repeated recovery and uninterrupted preservation', loc='left', fontweight='bold')
ax.set_xlabel('Periods'); ax.set_ylabel('Probability')
ax.legend(frameon=False, fontsize=8.5, loc='upper right')
ax.grid(alpha=.15)

ax = axes[1, 1]
for name in ('protected', 'endogenous', 'reentry', 'no_admission', 'volume_only'):
    ev = data[name]['checkpoints']['200']['average_events']
    x, y = ev['completed_cases'], ev['adequate']
    ax.scatter([x], [y], s=65, color=colors[name], zorder=3)
    dx, dy = (.025, .022) if name == 'protected' else (-.025, .025)
    ax.annotate(labels[name], (x, y), xytext=(x+dx, y+dy),
                ha='left' if name == 'protected' else 'right', fontsize=8.5)
ax.set_xlim(.78, 2.04); ax.set_ylim(.47, 1.04)
ax.set_title('D  Different outcomes remain separate', loc='left', fontweight='bold')
ax.set_xlabel('Completed cases per period, first 200 periods')
ax.set_ylabel('Probability routine fits context')
ax.grid(alpha=.15)

fig.suptitle('Succession, renewal and recovery in a finite nonfinancial model',
             fontsize=16, fontweight='bold', y=.985)
fig.text(.5, .015,
         'Synthetic stipulated mechanisms; no empirical fit. Protected succession assumes zero adverse appointments.\n'
         'Every finite adverse appointment weight retains an eventual depletion path without outside restoration.',
         ha='center', fontsize=9, color='#42484e')
fig.tight_layout(rect=[0, .055, 1, .95], h_pad=3, w_pad=2.5)
fig.savefig(root/'results/closure-study.png', dpi=160)
fig.savefig(root/'results/closure-study.svg')
