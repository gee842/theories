"""Reproduce the constructed renewal model and independent arithmetic checks."""
from pathlib import Path
import hashlib
import itertools
import json
import os
from fractions import Fraction as F

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / 'work/endogenous-renewal'
OUT = ROOT / 'outputs'
os.environ['MPLCONFIGDIR'] = str(WORK / 'mpl-cache')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def field(y, a=1, b=1, k=1):
    r, c, d = y
    return (k*c*d-a*r, a*r-b*c, b*c-k*c*d)

exact_count = 0
for a, b, k in itertools.product((F(1, 2), F(1), F(2)), repeat=3):
    for r, c, d in itertools.product((F(0), F(1, 3), F(2)), repeat=3):
        f = field((r, c, d), a, b, k)
        assert sum(f) == 0
        assert f[2] == -k*c*(d-b/k)
        assert all(f[i] >= 0 for i, v in enumerate((r, c, d)) if v == 0)
        exact_count += 1
    m = b/k+F(3)
    equilibrium = (b/(a+b)*(m-b/k), a/(a+b)*(m-b/k), b/k)
    assert field(equilibrium, a, b, k) == (0, 0, 0)
    assert sum(equilibrium) == m

def integrate(m, step, horizon=40):
    steps = round(horizon/step)
    times = np.linspace(0, horizon, steps+1)
    states = np.empty((steps+1, 3))
    states[0] = (m, 0, 0)
    def f(y):
        return np.asarray(field(y), dtype=float)
    for i in range(steps):
        y = states[i]
        k1 = f(y)
        k2 = f(y+step*k1/2)
        k3 = f(y+step*k2/2)
        k4 = f(y+step*k3)
        states[i+1] = y+step*(k1+2*k2+2*k3+k4)/6
    return times, states

trajectories = []
comparison = []
for m in (.6, 1., 3.):
    time, state = integrate(m, .01)
    time_fine, fine = integrate(m, .005)
    error = float(np.max(np.abs(state-fine[::2])))
    conservation_error = float(np.max(np.abs(state.sum(axis=1)-m)))
    assert error < 1e-8
    assert conservation_error < 1e-11
    assert state.min() >= -1e-12
    trajectories.append((m, time, state))
    comparison.append({'M': m, 'initial_R_C_D': [m, 0, 0],
                       'final_at_t40': state[-1].tolist(),
                       'maximum_step_halving_difference': error,
                       'maximum_mass_error': conservation_error,
                       'predicted_limit': [0, 0, m] if m <= 1 else [(m-1)/2, (m-1)/2, 1]})

# The feedback result is checked by an independent full 4x4 matrix calculation.
p_plus = np.array([[1, 1], [1, 1]], dtype=float)/2
p_minus = np.array([[1, -1], [-1, 1]], dtype=float)/2
feedback = []
for h in (0., .5):
    matrix = np.block([[np.eye(2), -np.eye(2)],
                       [6*(p_plus+h*p_minus), -2*np.eye(2)]])
    eigenvalues = np.linalg.eigvals(matrix)
    expected = list(np.roots([1, 1, 4]))+list(np.roots([1, 1, 6*h-2]))
    remaining = list(eigenvalues)
    for value in expected:
        idx = min(range(len(remaining)), key=lambda i: abs(remaining[i]-value))
        assert abs(remaining.pop(idx)-value) < 1e-10
    assert (max(eigenvalues.real) < 0) == (h == .5)
    feedback.append({'h': h, 'eigenvalues': [[float(z.real), float(z.imag)] for z in eigenvalues],
                     'all_real_parts_negative': bool(max(eigenvalues.real) < 0)})

# Independent finite-state graph check: all states can reach all-degraded.
n = 8
states = [(r, c, n-r-c) for r in range(n+1) for c in range(n-r+1)]
reverse = {s: [] for s in states}
for r, c, d in states:
    successors = []
    if r: successors.append((r-1, c+1, d))
    if c: successors.append((r, c-1, d+1))
    if c and d: successors.append((r+1, c, d-1))
    for t in successors: reverse[t].append((r, c, d))
reached = {(0, 0, n)}
frontier = [(0, 0, n)]
while frontier:
    for s in reverse[frontier.pop()]:
        if s not in reached:
            reached.add(s)
            frontier.append(s)
assert len(reached) == len(states)

plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':11,
                     'axes.spines.top':False,'axes.spines.right':False,
                     'axes.titleweight':'bold','figure.facecolor':'white'})
fig, axes = plt.subplots(1, 2, figsize=(11.8, 4.6))
colors = ['#ae6138', '#78649d', '#137d84']
labels = ['Below threshold: M = 0.6', 'At threshold: M = 1', 'Above threshold: M = 3']
for (m, times, values), color, label in zip(trajectories, colors, labels):
    axes[0].plot(times, values[:,1], color=color, lw=2.3, label=label)
axes[0].axhline(1, color=colors[2], lw=1, ls=':', alpha=.7)
axes[0].set(xlim=(0,40), ylim=(0,1.35), xlabel='Time', ylabel='Renewal machinery C',
            title='Machinery forms from an initial amount of zero')
axes[0].legend(frameon=False, loc='upper right', fontsize=9)
axes[0].grid(axis='y', alpha=.14)
masses = np.linspace(0,3.5,400)
axes[1].plot(masses, np.maximum(0,(masses-1)/2), color='#137d84', lw=2.6)
axes[1].axvline(1, color='#676d72', lw=1.2, ls='--')
axes[1].text(1.08, 1.12, 'Renewal threshold\nM = b/k = 1', va='top', color='#454c52')
for m in (.6,1,3):
    axes[1].plot(m, max(0,(m-1)/2), 'o', color=colors[(.6,1,3).index(m)], ms=6)
axes[1].set(xlim=(0,3.5), ylim=(-.055,1.35), xlabel='Total material M',
            ylabel='Long-run machinery amount C*', title='A lasting regime requires sufficient renewal')
axes[1].grid(axis='y', alpha=.14)
fig.text(.02,.02,'Constructed deterministic model; a = b = k = 1. Maintained energy supply. Initial (R, C, D) = (M, 0, 0).',
         fontsize=9,color='#515960')
fig.tight_layout(rect=(0,.06,1,1),w_pad=3)
png = OUT/'endogenous-renewal.png'
svg = OUT/'endogenous-renewal.svg'
fig.savefig(png,dpi=170)
fig.savefig(svg)
plt.close(fig)

checks = {'exact_state_and_parameter_checks':exact_count,
          'numerical_method':'Fixed-step classical fourth-order Runge-Kutta; plotted runs repeated at half step.',
          'trajectories':comparison, 'feedback_matrix_checks':feedback,
          'finite_population_graph_check':{'N':n,'states':len(states),'states_reaching_all_degraded':len(reached)},
          'scope':'Analytic proofs establish results; finite tests check arithmetic and implementation. Plots are model illustrations, not empirical observations.',
          'figures':[str(png),str(svg)],'all_checks_passed':True}
(WORK/'checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
