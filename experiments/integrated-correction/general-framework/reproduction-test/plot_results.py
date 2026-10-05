"""Render declared synthetic comparisons from saved results, without refitting."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

ROOT = Path(__file__).resolve().parent
disc = json.loads((ROOT/'discrimination/analysis.json').read_text())
evidence = json.loads((ROOT/'adaptive-evidence/analysis.json').read_text())
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10, 'axes.spines.top': False,
                     'axes.spines.right': False, 'svg.fonttype': 'none'})
fig, axes = plt.subplots(1, 3, figsize=(15, 5.3))
colors = ['#8b6a3e', '#2162a0', '#237d68']

ax = axes[0]
names = {'feedback_enabled': ('Execution enabled; feedback', colors[2]),
         'feedback_blocked': ('Execution blocked (both models)\nand enabled constant-turnover rival', colors[1])}
for name, (label, color) in names.items():
    rows = disc['arms'][name]['curve']
    ax.plot([r['round'] for r in rows], [r['skill_positive'] for r in rows], lw=2.3, label=label, color=color)
ax.set(title='A  Corrective action affects continuation', xlabel='Round', ylabel='Probability that skill remains', ylim=(0, 1.03))
ax.text(.06, .16, 'Effect at round 25 of enabling execution:\nfeedback +9.99 percentage points\nrival 0 points', transform=ax.transAxes)
ax.legend(loc='lower left', bbox_to_anchor=(-.03, 1.03), frameon=False, fontsize=9)

labels = ['Latest five cases', 'All evidence; always replace', 'All evidence; certificate']
procedures = ['latest_replacement', 'cumulative_replacement', 'cumulative_certificate']
for ax, scenario, title in zip(axes[1:], ['stationary', 'changed'], ['B  Stable physical relation', 'C  Unannounced reversal after case 30']):
    for procedure, label, color in zip(procedures, labels, colors):
        run = evidence['scenarios'][scenario][procedure]
        xs, ys = [], []
        for row in run['curve']:
            xs.append(row['cases']); ys.append(row['correct'])
            if scenario == 'changed' and row['cases'] == 30:
                xs.append(30); ys.append(run['immediately_after_unannounced_shift']['correct'])
        ax.plot(xs, ys, label=label, color=color, lw=2, marker='o', ms=3)
    if scenario == 'changed':
        ax.axvline(30, color='#626872', ls=':', lw=1, zorder=0)
    ax.set(title=title, xlabel='Inquiry cases observed', ylabel='Probability held declaration is currently correct', ylim=(0, 1.03), xlim=(3, 62))
    ax.set_xticks([5, 15, 30, 45, 60])
    if scenario == 'stationary':
        ax.legend(loc='lower left', bbox_to_anchor=(-.03, 1.03), frameon=False, fontsize=9)
for ax in axes:
    ax.yaxis.set_major_formatter(PercentFormatter(1))
    ax.grid(axis='y', color='#e4e6e9', lw=.7)
    ax.set_axisbelow(True)
    ax.set_title(ax.get_title(), fontsize=10, pad=58)
fig.subplots_adjust(left=.06, right=.985, bottom=.21, top=.71, wspace=.36)
fig.suptitle('Persistence, useful memory, and confident error are different outcomes', y=.98, fontsize=16)
fig.text(.06, .085, 'Conditional synthetic results; no empirical effect sizes shown. Panels B–C use identical budgets: 60 inquiry cases + 60 record-work slots.', fontsize=10)
fig.text(.06, .035, 'A declaration can be withheld without making the physical action safe. The stationary certificate guarantee does not apply after the reversal.', fontsize=10, color='#424851')
fig.savefig(ROOT/'results.png', dpi=180)
fig.savefig(ROOT/'results.svg')
