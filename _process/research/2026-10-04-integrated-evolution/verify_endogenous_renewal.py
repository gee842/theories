"""Check an illustrative paid-renewal model. This is not empirical validation."""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
a, delta, eta, mu, K = 9., 1., 1., 1., 1.
E_min = 1.
m = mu / eta
A = a / m
u_min = delta / (K * (np.sqrt(A) - 1)**2)
u_max = m / E_min

def rhs(z, u):
    E, C = z
    return np.array([a*C/(1+C/K)-delta*E-u*E*C,
                     eta*u*E*C-mu*C])

def positive_equilibria(u):
    d = delta / (u*K)
    if not A > (1+np.sqrt(d))**2:
        return []
    discriminant = (A-1-d)**2-4*d
    return [(m/u, K*((A-1-d)+s*np.sqrt(discriminant))/2)
            for s in (-1, 1)]

def jacobian(z, u):
    E, C = z
    return np.array([[-delta-u*C, a/(1+C/K)**2-u*E],
                     [eta*u*C, eta*u*E-mu]])

def simulate(u, initial, tolerance=1e-9):
    # Log coordinates preserve positivity without clipping or artificial floors.
    def log_rhs(t, z):
        E, C = np.exp(z)
        return [a*np.exp(z[1]-z[0])/(1+C/K)-delta-u*C,
                eta*u*E-mu]
    time = np.linspace(0, 200, 4001)
    sol = solve_ivp(log_rhs, [0, 200], np.log(initial), t_eval=time,
                    rtol=tolerance, atol=tolerance*1e-2, max_step=.1)
    assert sol.success
    values = np.exp(sol.y)
    assert np.all(values > 0)
    # V=E+C/eta obeys Vdot <= aK-min(delta,mu)V.
    bound = max(initial[0]+initial[1]/eta, a*K/min(delta, mu))
    assert np.max(values[0]+values[1]/eta) <= bound+1e-7
    return time, values

equilibria = []
for u in [.2, .5, 1., 1.5]:
    roots = positive_equilibria(u)
    checks = []
    for i, z in enumerate(roots):
        residual = float(np.max(np.abs(rhs(z, u))))
        eigenvalues = np.linalg.eigvals(jacobian(z, u))
        assert residual < 1e-12
        if i == 0:
            assert np.sum(np.real(eigenvalues) > 0) == 1
        else:
            assert np.all(np.real(eigenvalues) < 0)
        checks.append({'E':z[0], 'C':z[1], 'residual':residual,
                       'eigenvalues_real':np.real(eigenvalues).tolist(),
                       'eigenvalues_imaginary':np.imag(eigenvalues).tolist()})
    equilibria.append({'u':u, 'positive_equilibria':checks})
assert u_min == .25 and u_max == 1.
assert positive_equilibria(u_min) == []  # No two distinct roots at tangency.
assert np.max(np.abs(rhs((m/u_min, K*(np.sqrt(A)-1)), u_min))) < 1e-12
assert all(np.all(np.real(np.linalg.eigvals(jacobian((0., 0.), u))) < 0)
           for u in [.2, .5, 1.5])

cases = [
    ('Insufficient fixed effort', .2, (2., 4.)),
    ('Maintained correction with reserve', .5, (2., 4.)),
    ('Stable correction below support floor', 1.5, (2., 4.)),
    ('Depleted repair capacity', .5, (.05, .001)),
]
trajectories = []
for name, u, initial in cases:
    time, values = simulate(u, initial)
    _, refined = simulate(u, initial, 1e-11)
    discrepancy = float(np.max(np.abs(values-refined)))
    assert discrepancy < 1e-6
    trajectories.append({'case':name, 'u':u, 'initial':initial,
                         'final_t200':values[:, -1].tolist(),
                         'minimum_E_over_sampled_times':float(np.min(values[0])),
                         'tolerance_refinement_error':discrepancy})
assert max(trajectories[0]['final_t200']) < 1e-6
assert np.max(np.abs(np.array(trajectories[1]['final_t200']) -
                     positive_equilibria(.5)[1])) < 1e-6
assert trajectories[2]['final_t200'][0] < E_min
assert trajectories[2]['final_t200'][1] > trajectories[1]['final_t200'][1]
assert max(trajectories[3]['final_t200']) < 1e-6

# An invariant rectangle certifies the depleted start analytically at u=.5.
E_box, C_box, u_box = .1, .001, .5
E_boundary_bound = a*C_box-delta*E_box  # Omit negative paid-renewal cost.
C_growth_bound = eta*u_box*E_box-mu
assert E_boundary_bound < 0 and C_growth_bound < 0

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,
                     'axes.spines.top':False,'axes.spines.right':False,
                     'text.color':'#22323F','axes.labelcolor':'#22323F'})
fig, axes = plt.subplots(1, 2, figsize=(11.8, 4.7), facecolor='#FCFCFA')
efforts = np.linspace(u_min+1e-5, 1.8, 900)
roots = np.array([positive_equilibria(u)[1] for u in efforts])
for j, ax in enumerate(axes):
    ax.set_facecolor('#FCFCFA')
    ax.axvspan(u_min, u_max, color='#087F83', alpha=.10)
    ax.axvspan(0, u_min, color='#65737D', alpha=.09)
    ax.axvspan(u_max, 1.8, color='#BD4E36', alpha=.09)
    ax.axvline(u_min, color='#65737D', ls=':', lw=1)
    ax.axvline(u_max, color='#BD4E36', ls=':', lw=1)
    ax.plot(efforts, roots[:,j], color='#087F83', lw=2.5)
    ax.set_xlim(0, 1.8)
    ax.set_ylim(bottom=0)
    ax.set_xlabel('Fixed renewal effort u')
    ax.grid(alpha=.16)
axes[0].axhline(E_min, color='#BD4E36', ls='--', lw=1.4)
axes[0].text(1.1, 1.14, 'Protected support floor', fontsize=9, color='#BD4E36')
axes[0].set_ylabel('Support at the stable positive equilibrium E*')
axes[1].set_ylabel('Repair capacity at that equilibrium C*')
axes[0].set_title('Support reserve falls', fontsize=12, fontweight='bold', pad=10)
axes[1].set_title('Repair capacity rises', fontsize=12, fontweight='bold', pad=10)
fig.suptitle('Maintaining correction also consumes support', x=.07, ha='left',
             y=.97, fontsize=16, fontweight='bold')
fig.text(.07, .085, 'Green: a stable positive equilibrium meets E*>1. '
         'Gray: no positive equilibrium below u=0.25. '
         'Red: its support is below the floor.', fontsize=9)
fig.text(.07, .035, 'Illustrative model, not fitted data. Equilibrium feasibility does not '
         'guarantee safe transients. a=9; decay, conversion, saturation scales=1.',
         fontsize=9, color='#65737D')
fig.subplots_adjust(left=.07, right=.975, bottom=.25, top=.79, wspace=.25)
fig.savefig(OUT/'endogenous-renewal-tradeoff.png', dpi=180, facecolor=fig.get_facecolor())
fig.savefig(OUT/'endogenous-renewal-tradeoff.svg', facecolor=fig.get_facecolor())

record = {'status':'passed', 'scope':'analytic model verification, not empirical validation',
          'parameters':dict(a=a,delta=delta,eta=eta,mu=mu,K=K,E_min=E_min),
          'strict_equilibrium_effort_interval':[u_min, u_max],
          'equilibria':equilibria, 'trajectories':trajectories,
          'depleted_box_certificate':{'E_upper':E_box,'C_upper':C_box,'u':u_box,
              'E_upper_boundary_derivative_bound':E_boundary_bound,
              'C_per_capita_growth_upper':C_growth_bound},
          'limitations':['No empirical fit or universal social parameter claim.',
                        'Fixed u does not explain selection over renewal effort.',
                        'Finite trajectories are illustrations; analytic proofs are separate.',
                        'External feedstock for production is a declared boundary condition.']}
(OUT/'endogenous-renewal-checks.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
