#!/usr/bin/env python3
"""Plot checked stationary branches; do not label them as basin boundaries."""
import hashlib
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent


def main():
    receipt = HERE/'attraction-verification.json'
    assert json.loads(receipt.read_text())['status'] == 'passed'
    out = HERE/'figures'
    out.mkdir(exist_ok=True)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                         'axes.spines.top': False, 'axes.spines.right': False})
    fig, ax = plt.subplots(figsize=(10, 6.4))
    fig.subplots_adjust(left=.10, right=.96, bottom=.30, top=.82)
    beta = np.linspace(.035, .75, 400)
    admitted = np.linspace(5/12, .75, 250)
    ax.plot(beta, np.ones_like(beta), color='#66717e', linewidth=2)
    ax.plot(beta, np.zeros_like(beta), color='#66717e', linewidth=2)
    ax.plot(admitted, 1-5/(12*admitted), color='#9b5b28', linewidth=2.5)
    ax.axvline(5/12, color='#8b9299', linestyle='--', linewidth=1)
    ax.axvline(.5, color='#2167a3', alpha=.15, linewidth=12)
    ax.scatter([.5, .5], [0, 1], color='#2167a3', s=95, zorder=5)
    ax.scatter([.5], [1/6], color='#bc3b3b', marker='X', s=110, zorder=6)
    ax.scatter([5/12], [0], facecolors='white', edgecolors='#9b5b28', s=70, zorder=5)
    ax.text(.055, 1.035, 'H: maintenance share = 1', color='#48515a')
    ax.text(.055, -.09, 'L: maintenance share = 0', color='#48515a')
    ax.annotate('Interior branch: 1 - 5/(12β)', xy=(.70, 1-5/(12*.70)),
                xytext=(.46,.63), arrowprops={'arrowstyle': '-', 'color': '#9b5b28'},
                color='#814a20')
    ax.annotate('Branch collision\nβ = 5/12', xy=(5/12,0), xytext=(.20,.25),
                arrowprops={'arrowstyle': '->', 'color': '#767d85'}, color='#48515a')
    ax.annotate('Unstable at β = 1/2', xy=(.5,1/6), xytext=(.55,.10),
                arrowprops={'arrowstyle': '->', 'color': '#bc3b3b'}, color='#9c2929')
    ax.text(.54,.82, 'Local attraction proved\nat both blue points', color='#2167a3')
    ax.set(xlim=(.02,.77), ylim=(-.12,1.12), xlabel='Erosion strength β',
           ylabel='Stationary maintenance share x*')
    ax.set_xticks([.1,.2,.3,5/12,.5,.6,.75],
                  ['0.1','0.2','0.3','5/12','1/2','0.6','3/4'])
    ax.set_yticks([0,1/6,.5,1], ['0','1/6','1/2','1'])
    ax.grid(axis='y', alpha=.15)
    fig.suptitle('Two local attractors and an unstable interior state', x=.10, ha='left',
                 y=.96, fontsize=18, fontweight='bold')
    fig.text(.10,.88, 'Existing paid operating model: α = 1/4, λ = 1, θ = 3/8, μ = 1/4, ηf = 4/5.',
             fontsize=11, color='#48515a')
    fig.text(.10,.085,
             'Curves classify fixed states, not basin boundaries. Local behavior is certified at β = 1/2 only.\n'
             'The low attractor describes the selection projection: coupling its essential support causes finite failure.\n'
             'No empirical parameter calibration or complete bifurcation classification is represented.',
             fontsize=10, color='#48515a', linespacing=1.5)
    files = []
    for suffix in ['png','svg']:
        path = out/('regime-fixed-states.'+suffix)
        fig.savefig(path, dpi=180, facecolor='white')
        files.append(path)
    plt.close(fig)
    record = {
        'scope': 'Illustration of checked rational stationary formulas and beta=1/2 local behavior; no simulated trajectories.',
        'matplotlib_version': matplotlib.__version__,
        'proof_receipt_sha256': hashlib.sha256(receipt.read_bytes()).hexdigest(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'outputs': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
    (out/'regime-fixed-states.json').write_text(json.dumps(record, indent=2)+'\n')
    print('Created fixed-state figure; no basin or empirical threshold inferred.')


if __name__ == '__main__':
    main()
