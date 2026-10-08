#!/usr/bin/env python3
"""Scientific figure from measured participant summaries, not simulated data."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

P = Path(__file__).resolve().parent
r = json.loads((P / 'memory-updating-results.json').read_text())
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                     'axes.spines.top': False, 'axes.spines.right': False})
fig, axes = plt.subplots(1, 3, figsize=(13.8, 4.8), gridspec_kw={'width_ratios': [1.1, 1.2, 1]})
colors = ['#637085', '#146e75']
for phase, offset, color in [('pre', -.08, colors[0]), ('post', .08, colors[1])]:
    stats = [r['phase_means'][phase][k] for k in r['conditions']]
    y = np.array([v['mean'] for v in stats]); ci = np.array([v['bootstrap_ci95'] for v in stats]).T
    axes[0].errorbar(np.arange(4) + offset, y, yerr=np.abs(ci - y), fmt='o-',
                     color=color, capsize=3, label=phase.capitalize() + '-training')
axes[0].set(xticks=range(4), xticklabels=['P+\nCue 1', 'P+\nCue 2', 'P−\nCue 1', 'P−\nCue 2'],
            ylabel='Perturbation-aligned update', title='A  Measured update by condition')
axes[0].legend(frameon=False, fontsize=9)
axes[0].axhline(0, color='#afb4bc', lw=.7)
for i, name in enumerate(['cue', 'perturbation', 'interaction']):
    v = r['contrasts'][name]['change']; x = v['mean']; lo, hi = v['bootstrap_ci95']
    w = np.array(r['contrast_weights'][name])
    values = [(np.array(p['post']) - np.array(p['pre'])) @ w for p in r['participant_means']]
    axes[1].scatter(values, np.full(24, i) + np.linspace(-.13, .13, 24), s=12, alpha=.3, color='#637085')
    axes[1].errorbar(x, i, xerr=[[x-lo], [hi-x]], color='#146e75', fmt='o', capsize=4, lw=2)
axes[1].set(yticks=range(3), yticklabels=['Cue', 'Perturbation', 'Interaction'],
            xlabel='Post minus pre contrast', title='B  Change across training')
axes[1].invert_yaxis(); axes[1].axvline(0, color='#afb4bc', lw=.9)
for name, color, offset in [('cue', '#b66533', -.035), ('perturbation', '#146e75', .035)]:
    stats = [r['post_half_sensitivity'][name][k] for k in ['first_half', 'second_half']]
    y = np.array([v['mean'] for v in stats]); ci = np.array([v['bootstrap_ci95'] for v in stats]).T
    axes[2].errorbar(np.arange(2) + offset, y, yerr=np.abs(ci-y), fmt='o-',
                     color=color, capsize=4, label=name.capitalize())
axes[2].set(xticks=[0, 1], xticklabels=['Earlier 4', 'Later 4'], xlim=(-.25, 1.25),
            xlabel='Post-training triplets per condition', ylabel='Contrast in measured update',
            title='C  Effects need not persist equally')
axes[2].axhline(0, color='#afb4bc', lw=.9); axes[2].legend(frameon=False, fontsize=9)
fig.suptitle('Acquired history changes expressed updating — unevenly', x=.055, ha='left', fontsize=16, weight='bold')
fig.text(.055, .02, '24 participants • 2,304 triplets retained • Bars: 95% participant-bootstrap intervals (exploratory, unadjusted)\n'
         'Public-data reanalysis of Heald et al. (2021); a finite behavioral comparison, not a latent-state or convergence certificate.', fontsize=9, color='#4b5563')
fig.tight_layout(rect=[.02, .1, .99, .9], w_pad=2)
fig.savefig(P / 'memory-updating-results.png', dpi=170)
fig.savefig(P / 'memory-updating-results.svg', metadata={'Date': None})
