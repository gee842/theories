"""Plot the first predeclared evaluation seed, never a selected success.

Optional figure reproduction requires matplotlib; the model and evaluation
themselves use only Python's standard library.
"""
import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--records', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    records = json.loads(args.records.read_text())
    assert {r['seed'] for r in records} == {800001}
    scenarios = [('emerging', 'Lasting opportunity'),
                 ('material_stress', 'Facility cost shock'),
                 ('poor_income', 'Falling income')]
    styles = [('full', 'Integrated community', '#176b8a', '-'),
              ('fixed_mandate', 'Fixed mandate', '#6b7280', '--'),
              ('no_renewal', 'No facility renewal', '#d26926', '-')]
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'axes.titleweight': 'bold'})
    fig, axes = plt.subplots(2, 3, figsize=(14, 8), sharex=True)
    for j, (scenario, label) in enumerate(scenarios):
        for arm, name, color, linestyle in styles:
            r = next(r for r in records if r['scenario'] == scenario and r['arm'] == arm)
            rows = r['timeline']
            t = [0] + [p['round'] for p in rows]
            failures = [0] + [p['errors_B'] + p['round'] - p['served_B'] for p in rows]
            cash = [r['initial_cash'] / 1000] + [p['cash'] / 1000 for p in rows]
            axes[0, j].plot(t, failures, color=color, linestyle=linestyle, lw=2.3, label=name)
            axes[1, j].plot(t, cash, color=color, linestyle=linestyle, lw=2.3)
        axes[0, j].set_title(label, pad=12)
        axes[1, j].set_xlabel('Service round')
        for ax in axes[:, j]:
            ax.grid(axis='y', color='#e4e7eb', lw=.8)
            ax.set_xlim(0, 700)
            ax.set_ylim(bottom=0)
        full = next(r for r in records if r['scenario'] == scenario and r['arm'] == 'full')
        edits = [e['round'] for e in full['events'] if e['kind'] == 'review_finished' and e['rule_changed']]
        for t in edits:
            for ax in axes[:, j]:
                ax.axvline(t, color='#176b8a', alpha=.23, lw=1.1, linestyle=':')
    axes[0, 0].set_ylabel('B: wrong or unserved requests\n(cumulative)')
    axes[1, 0].set_ylabel('Cash balance\n(contract currency units)')
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', ncol=3, frameon=False, bbox_to_anchor=(.51, .936))
    fig.suptitle('The same inquiry loop can improve service or exhaust its funding',
                 x=.5, y=.989, fontsize=18, fontweight='bold')
    fig.text(.06, .025,
             'First predeclared held-out seed: 800001. Dotted lines: integrated community installs a method.\n'
             'Each group receives 700 requests. All five arms and all 64 seeds are reported separately; this trace was not selected by outcome.',
             fontsize=10, color='#4b5563')
    fig.subplots_adjust(top=.84, bottom=.14, left=.08, right=.98, wspace=.25, hspace=.18)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output.with_suffix('.png'), dpi=170, facecolor='white')
    fig.savefig(args.output.with_suffix('.svg'), facecolor='white')


if __name__ == '__main__':
    main()
