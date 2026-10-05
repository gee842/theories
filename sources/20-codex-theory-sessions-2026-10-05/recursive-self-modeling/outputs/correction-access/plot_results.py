"""Create static scientific summaries from frozen held-out raw results.

This script does no simulation, model selection, or result-file mutation.
Mean-loss intervals use a descriptive normal 95% interval with independent seeds
as units. For mixtures, each seed is averaged across its four paired worlds
before estimating uncertainty. These are not the multiplicity-adjusted primary
contrast intervals. Access curves count actual acquisitions only, divide by all
episodes, and are not Kaplan-Meier estimates; their missing mass stays explicit.
"""
from pathlib import Path
import argparse
import json

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, PercentFormatter


HERE = Path(__file__).resolve().parent
PALETTE = {'confidence': '#586777', 'innovation': '#1878ad',
           'periodic': '#da792d', 'hybrid': '#168778', 'anchor_filter': '#845cb6'}
LABELS = {'confidence': 'Confidence', 'innovation': 'Innovation',
          'periodic': 'Periodic', 'hybrid': 'Hybrid', 'anchor_filter': 'Anchor filter'}
SCALAR = ['confidence', 'innovation', 'periodic', 'hybrid']


def theme():
    plt.rcParams.update({
        'font.family': 'DejaVu Sans', 'font.size': 10, 'axes.titlesize': 12,
        'axes.labelsize': 10, 'xtick.labelsize': 9, 'ytick.labelsize': 9,
        'axes.spines.top': False, 'axes.spines.right': False,
        'axes.edgecolor': '#bbc1c8', 'axes.labelcolor': '#303946',
        'text.color': '#24303e', 'xtick.color': '#4f5d6b', 'ytick.color': '#4f5d6b',
        'axes.axisbelow': True, 'grid.color': '#e3e7eb', 'grid.linewidth': .7,
        'legend.frameon': False, 'figure.facecolor': 'white',
        'savefig.facecolor': 'white', 'svg.fonttype': 'none',
    })


def mean_ci(seed_values):
    values = np.asarray(seed_values)
    assert values.ndim == 1 and np.all(np.isfinite(values))
    return float(values.mean()), float(1.959963984540054*values.std(ddof=1)/np.sqrt(len(values)))


def validate(raw):
    values = raw['values']
    worlds, policies, metrics = (list(raw[k].astype(str)) for k in ['worlds', 'policies', 'metrics'])
    assert values.shape == (len(worlds), len(policies), len(raw['seeds']), len(metrics))
    assert len(np.unique(raw['seeds'])) == len(raw['seeds'])
    for name in SCALAR+['anchor_filter']:
        assert name in policies
    assert all(f'{stratum}_g{g}_d{d}' in worlds for stratum in ['constant','change'] for g in [0,1] for d in [0,1])
    return values, worlds, policies, metrics


def save(fig, out, basename):
    paths = []
    for ext in ['png', 'svg']:
        path = out / f'{basename}.{ext}'
        fig.savefig(path, dpi=220, bbox_inches='tight', pad_inches=.15)
        paths.append(str(path))
    plt.close(fig)
    return paths


def access_figure(values, worlds, policies, metrics, seeds, out):
    pidx = {name: policies.index(name) for name in policies}
    midx = {name: metrics.index(name) for name in metrics}
    strata = [[worlds.index(f'{label}_g{g}_d{d}') for g in [0,1] for d in [0,1]]
              for label in ['constant', 'change']]
    fig, (left, right) = plt.subplots(1, 2, figsize=(12.4, 5.6),
                                     gridspec_kw={'width_ratios': [1, 1.15]})
    fig.subplots_adjust(top=.73, bottom=.26, left=.07, right=.975, wspace=.27)
    fig.text(.07, .95, 'Access schedules and control outcomes', fontsize=18, weight='bold')
    fig.text(.07, .89, 'Four gates share the same correction rule, controller, and six-reference limit.', fontsize=11)
    left.set_title('A   Mean total loss', loc='left', pad=12, weight='bold')
    right.set_title('B   Reference acquired after the change', loc='left', pad=12, weight='bold')
    positions = np.arange(2)
    width = .18
    means, records, max_y = {}, {}, 0.
    for j, policy in enumerate(SCALAR):
        mean, error = [], []
        for wi in strata:
            # Averaging four paired worlds BEFORE seed-level SE is essential.
            by_seed = values[wi, pidx[policy], :, midx['total_loss']].mean(axis=0)
            m, c = mean_ci(by_seed)
            mean.append(m); error.append(c)
        means[policy] = mean
        x = positions + (j-1.5)*width
        bars = left.bar(x, mean, width=width*.93, color=PALETTE[policy], label=LABELS[policy],
                        yerr=error, error_kw={'ecolor':'#334153','elinewidth':1.,'capsize':2.4})
        for bar, value, err in zip(bars, mean, error):
            left.annotate(f'{value:.2f}', (bar.get_x()+bar.get_width()/2., value+err),
                          xytext=(0, 4), textcoords='offset points', ha='center', fontsize=8.4)
        max_y = max(max_y, max(np.array(mean)+error))
        records[policy] = {'mean_loss_constant':mean[0], 'mean_loss_change':mean[1]}
    left.set_xticks(positions, ['Constant ordinary bias', 'One bias reversal'])
    left.set_ylim(0, max_y*1.20)
    left.set_ylabel('Total loss per 60-step episode · lower is better')
    left.yaxis.set_major_locator(MaxNLocator(5))
    left.grid(axis='y')
    handles, legend_labels = left.get_legend_handles_labels()
    fig.legend(handles, legend_labels, ncol=4, loc='upper left', bbox_to_anchor=(.065, .86),
               handlelength=1.1, columnspacing=1.4, fontsize=9)

    grid = np.arange(0, 53)
    for policy in SCALAR:
        found = values[strata[1], pidx[policy], :, midx['sample_found']].astype(bool).ravel()
        delays = values[strata[1], pidx[policy], :, midx['access_delay']].ravel()
        # This is a subdistribution of observed events, never a naive ECDF of
        # recorded censoring times. Denominator includes episodes without events.
        fraction = np.array([np.mean(found & (delays <= d)) for d in grid])
        missing = 1.-float(found.mean())
        assert np.all(np.diff(fraction) >= -1e-15)
        assert abs(fraction[-1]-float(found.mean())) < 1e-12
        records[policy]['no_postchange_reference_fraction'] = missing
        records[policy]['max_observed_postchange_reference_delay'] = float(delays[found].max())
        records[policy]['mean_delay_among_observed_references_only'] = float(delays[found].mean())
        right.step(grid, fraction, where='post', color=PALETTE[policy], linewidth=2.2,
                   label=f'{LABELS[policy]} · {missing:.1%} no later reference')
    right.set_xlim(0, 52)
    right.set_ylim(0, 1.025)
    right.set_xticks([0, 10, 20, 30, 40, 50])
    right.set_xlabel('Steps since the bias reversal')
    right.set_ylabel('Fraction of all change-world episodes')
    right.yaxis.set_major_formatter(PercentFormatter(1.))
    right.grid(axis='y')
    right.legend(loc='lower right', fontsize=8.6, handlelength=2., labelspacing=.7)
    fig.text(.07, .14, f'{len(seeds):,} independent held-out seeds; each stratum equally weights four forcing/reference-bias worlds.', fontsize=9.2)
    fig.text(.07, .10, 'A: descriptive 95% intervals use per-seed world averages. Total loss includes sensing; computation has no price.', fontsize=9.2)
    fig.text(.07, .06, 'B: actual acquisitions only; missing events remain outside the curve. Pooled paired worlds; no confidence bands or survival extrapolation.', fontsize=9.2)
    return save(fig, out, 'gate-access-summary'), records


def anchor_figure(values, worlds, policies, metrics, seeds, out):
    pidx = {name: policies.index(name) for name in policies}
    midx = {name: metrics.index(name) for name in metrics}
    fig, axes = plt.subplots(2, 2, figsize=(12.4, 8.1))
    fig.subplots_adjust(top=.80, bottom=.22, left=.07, right=.975, hspace=.47, wspace=.20)
    fig.text(.07, .955, 'A different estimator under the same periodic access', fontsize=18, weight='bold')
    fig.text(.07, .907, 'Descriptive benchmark: the anchor filter estimates state, ordinary bias, and reference bias; both receive six references.', fontsize=10.6)
    labels = ['No forcing\nClean reference', 'No forcing\nBiased reference',
              'Hidden forcing\nClean reference', 'Hidden forcing\nBiased reference']
    positions = np.arange(4)
    records = {}
    max_loss = 0.
    for col, stratum in enumerate(['constant', 'change']):
        wi = [worlds.index(f'{stratum}_g{g}_d{d}') for g in [0,1] for d in [0,1]]
        for row, metric in enumerate(['total_loss', 'coverage90']):
            ax = axes[row, col]
            for j, policy in enumerate(['periodic', 'anchor_filter']):
                mean, error = zip(*(mean_ci(values[w, pidx[policy], :, midx[metric]]) for w in wi))
                mean, error = np.array(mean), np.array(error)
                color = PALETTE[policy]
                x = positions+(j-.5)*.31
                bars = ax.bar(x, mean, width=.29, color=color, label=LABELS[policy], yerr=error,
                              error_kw={'ecolor':'#334153', 'elinewidth':.9, 'capsize':2.})
                for bar, value, err in zip(bars, mean, error):
                    label = f'{value:.2f}' if row == 0 else f'{value:.1%}'
                    ax.annotate(label, (bar.get_x()+bar.get_width()/2, value+err),
                                xytext=(0, 3), textcoords='offset points', ha='center', fontsize=8.1)
                if row == 0:
                    max_loss = max(max_loss, max(mean+error))
                for w, m in zip(wi, mean):
                    records.setdefault(worlds[w], {}).setdefault(policy, {})[metric] = float(m)
            ax.grid(axis='y')
            ax.set_xticks(positions, labels)
            ax.tick_params(axis='x', labelsize=8.5)
            if row == 0:
                ax.set_title(('A   Constant ordinary bias' if col == 0 else 'B   One bias reversal'),
                             loc='left', pad=12, weight='bold')
                ax.yaxis.set_major_locator(MaxNLocator(5))
                if col == 0:
                    ax.set_ylabel('Mean total loss · lower is better')
            else:
                ax.axhline(.9, color='#45505d', linestyle=(0,(4,3)), linewidth=1.1, zorder=1)
                ax.set_ylim(0, 1.09)
                ax.set_yticks([0, .25, .5, .75, 1.])
                ax.yaxis.set_major_formatter(PercentFormatter(1.))
                if col == 0:
                    ax.set_ylabel('Coverage of nominal 90% forecast intervals')
    for ax in axes[0]:
        ax.set_ylim(0, max_loss*1.20)
    handles, legend_labels = axes[0,0].get_legend_handles_labels()
    fig.legend(handles, ['Periodic · shared scalar correction', 'Anchor filter · Gaussian moment model'],
               ncol=2, loc='upper left', bbox_to_anchor=(.063,.88), columnspacing=2.2, fontsize=10)
    fig.text(.07, .135, f'Each world: {len(seeds):,} held-out seeds. Whiskers: descriptive 95% intervals. Dashed line: nominal 90% coverage.', fontsize=9.2)
    fig.text(.07, .098, 'Hidden forcing is a constant ±0.15 input; reference bias is a constant ±0.25 offset. All estimators assume zero forcing.', fontsize=9.2)
    fig.text(.07, .061, 'Estimator and uncertainty model both change here. Differences cannot be attributed solely to when references are acquired.', fontsize=9.2)
    return save(fig, out, 'anchor-benchmark-summary'), records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default=HERE/'results'/'all-results.npz')
    parser.add_argument('--output', type=Path, default=HERE)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    theme()
    with np.load(args.input, allow_pickle=False) as raw:
        values, worlds, policies, metrics = validate(raw)
        first_paths, first_records = access_figure(values, worlds, policies, metrics, raw['seeds'], args.output)
        second_paths, second_records = anchor_figure(values, worlds, policies, metrics, raw['seeds'], args.output)
    metadata = {'input':str(args.input), 'figures': first_paths+second_paths,
                'scalar_gate_summary':first_records, 'descriptive_anchor_summary':second_records}
    (args.output/'figure-values.json').write_text(json.dumps(metadata, indent=2)+'\n')
    print(json.dumps(metadata, indent=2))


if __name__ == '__main__':
    main()
