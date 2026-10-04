"""Numerical checks of an illustrative model; no empirical calibration."""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
a, m, c, gamma, rho, delta, K = 5., .8, .2, 1., 1., 1., 1.
M, H = m+c, delta*K/rho
discriminant = (a*K-M-gamma*H)**2-4*gamma*H*M
roots = [(a*K-M-gamma*H+s*np.sqrt(discriminant))/(2*gamma) for s in [-1, 1]]

def original_rhs(state, theta):
    x, N, E = state
    return np.array([x*(1-x)*(theta-c),
                     N*(a*E-m-gamma*N-c*x),
                     rho*N*x*(1-E/K)-delta*E])

def logistic(t, theta, x0=.9):
    return 1/(1+(1-x0)/x0*np.exp(-(theta-c)*t))

def simulate(theta, initial, tol=1e-9):
    x0, N0, E0 = initial
    def rhs(t, logs):
        N, E = np.exp(logs)
        x = logistic(t, theta, x0)
        return [a*E-m-gamma*N-c*x,
                rho*np.exp(logs[0]-logs[1])*x*(1-E/K)-delta]
    time = np.linspace(0, 120, 2401)
    sol = solve_ivp(rhs, [0, 120], np.log([N0, E0]), t_eval=time,
                    rtol=tol, atol=tol*1e-2, max_step=.1)
    assert sol.success
    result = np.vstack([logistic(time, theta, x0), np.exp(sol.y)])
    assert np.all(result > 0)
    assert np.max(result[0]) <= 1+1e-12
    assert np.max(result[2]) <= K+1e-9
    return time, result

equilibria = []
for N in roots:
    E = K*N/(H+N)
    jac = np.array([[-(.4-c), 0, 0],
                    [-c*N, -gamma*N, a*N],
                    [rho*N*(1-E/K), rho*(1-E/K), -rho*N/K-delta]])
    eig = np.linalg.eigvals(jac)
    residual = float(np.max(np.abs(original_rhs([1., N, E], .4))))
    assert residual < 1e-12
    equilibria.append({'N':N, 'E':E, 'eigenvalues':eig.tolist(), 'residual':residual})
assert sum(np.array(equilibria[0]['eigenvalues']) > 0) == 1
assert all(np.array(equilibria[1]['eigenvalues']) < 0)

# Analytic trapping-box certificate for the depleted initial state.
# These bounds hold for every x in [0, 1] in the specified box.
N_box, E_box = .05, .05
growth_bound = a*E_box-m
support_boundary_bound = rho*N_box*(1-E_box/K)-delta*E_box
assert 0 < E_box <= K
assert growth_bound < 0 and support_boundary_bound < 0
depleted_box = {'N_upper':N_box, 'E_upper':E_box,
                'per_capita_growth_upper':growth_bound,
                'support_upper_boundary_derivative_bound':support_boundary_bound,
                'conclusion':'forward invariant; N decays exponentially and E tends to zero'}

cases = [
    ('Maintenance loses; stocked start', .1, [.9, 2.5, .7], '#BD4E36', '-'),
    ('Maintenance spreads; stocked start', .4, [.9, 2.5, .7], '#087F83', '-'),
    ('Maintenance spreads; depleted start', .4, [.9, .05, .05], '#7661A8', '--'),
]
results = []
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':10,
                     'axes.spines.top':False, 'axes.spines.right':False,
                     'axes.labelcolor':'#22323F', 'text.color':'#22323F'})
fig, axes = plt.subplots(1, 3, figsize=(13.6, 4.8), facecolor='#FCFCFA')
for name, theta, initial, color, style in cases:
    time, values = simulate(theta, initial)
    _, refined = simulate(theta, initial, 1e-11)
    error = float(np.max(np.abs(values-refined)))
    assert error < 1e-6
    results.append({'case':name, 'theta':theta, 'initial':initial,
                    'final_t120':values[:,-1].tolist(), 'tolerance_refinement_error':error})
    for j, ax in enumerate(axes):
        ax.plot(time, values[j], color=color, ls=style, lw=2.3, label=name)
        ax.set_xlim(0, 120)
        ax.set_facecolor('#FCFCFA')
        ax.set_xlabel('Time (model units)')
        ax.grid(alpha=.18)
for ax, title, label in zip(axes, ['What spreads', 'How much remains', 'What supports renewal'],
                           ['Maintainer share x', 'Total abundance N', 'Maintained support E']):
    ax.set_title(title, fontsize=12, fontweight='bold', pad=11)
    ax.set_ylabel(label)
    ax.set_ylim(bottom=0)
axes[0].set_ylim(0, 1.05)
axes[2].set_ylim(0, .82)
axes[0].annotate('These two cases have\nthe same share trajectory', xy=(27,.994),
                 xytext=(29,.56), arrowprops={'arrowstyle':'->','color':'#7661A8'},
                 fontsize=9, color='#7661A8')
fig.suptitle('Spreading maintenance does not guarantee recovery', x=.07, ha='left',
             y=.985, fontsize=16, fontweight='bold')
fig.legend(*axes[1].get_legend_handles_labels(), loc='lower center',
           bbox_to_anchor=(.5,.075), ncol=3, frameon=False, fontsize=9)
fig.text(.07, .015, 'Illustrative deterministic model, not a fit to data. '
         'a=5, m=0.8, c=0.2; other rate and scale parameters=1. '
         'Decay toward zero is asymptotic.', fontsize=9, color='#65737D')
fig.subplots_adjust(left=.07,right=.98,bottom=.24,top=.82,wspace=.30)
fig.savefig(OUT/'regeneration-regimes.png', dpi=180, facecolor=fig.get_facecolor())
fig.savefig(OUT/'regeneration-regimes.svg', facecolor=fig.get_facecolor())

assert results[0]['final_t120'][1] < 1e-6
assert results[0]['final_t120'][2] < 1e-6
assert abs(results[1]['final_t120'][1]-roots[1]) < 1e-6
assert results[2]['final_t120'][0] > .99999
assert results[2]['final_t120'][1] < 1e-6
assert results[2]['final_t120'][2] < 1e-6
checks = {'status':'passed', 'scope':'illustrative analytic model; not empirical validation',
          'parameters':dict(a=a,m=m,c=c,gamma=gamma,rho=rho,delta=delta,K=K),
          'positive_equilibrium_threshold':float((np.sqrt(M)+np.sqrt(gamma*H))**2),
          'a_times_K':a*K, 'equilibria':equilibria, 'cases':results,
          'depleted_trapping_box':depleted_box}
(OUT/'regeneration-model-checks.json').write_text(json.dumps(checks, indent=2)+'\n')
print(json.dumps(checks, indent=2))
