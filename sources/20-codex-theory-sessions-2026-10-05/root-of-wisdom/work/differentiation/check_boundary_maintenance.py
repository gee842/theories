"""Exact local stability and converged illustrative trajectories; constructed model."""
from fractions import Fraction as Q
import json
from pathlib import Path

A, ell, q, beta, mu = Q(3), Q(15, 4), Q(1), Q(1), Q(1)
fixed = []
for c, b in [(Q(1, 2), Q(1, 2)), (Q(3, 2), Q(3, 2))]:
    assert (A-ell/(1+b))*c-q*c*c == 0
    assert beta*c-mu*b == 0
    trace = -q*c-mu
    determinant = mu*q*c-beta*ell*c/(1+b)**2
    assert trace < 0
    assert (determinant < 0) == (c == Q(1, 2))
    fixed.append({'c': str(c), 'b': str(b), 'trace': str(trace),
                  'determinant': str(determinant),
                  'type': 'saddle' if determinant < 0 else 'stable'})


def rhs(z, production=1, clamp=False):
    c, b = z
    return ((3-3.75/(1+b))*c-c*c, 0 if clamp else production*c-b)


def trajectory(initial, duration, dt, production=1, clamp=False):
    z = tuple(map(float, initial))
    selected = [{'time': 0.0, 'c': z[0], 'b': z[1]}]
    steps = round(duration/dt)
    for n in range(steps):
        k1 = rhs(z, production, clamp)
        k2 = rhs(tuple(z[i]+dt*k1[i]/2 for i in (0, 1)), production, clamp)
        k3 = rhs(tuple(z[i]+dt*k2[i]/2 for i in (0, 1)), production, clamp)
        k4 = rhs(tuple(z[i]+dt*k3[i] for i in (0, 1)), production, clamp)
        z = tuple(z[i]+dt*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6 for i in (0, 1))
        assert min(z) >= 0 and max(z) <= 3.0000001
        if (n+1) % round(1/dt) == 0:
            selected.append({'time': round((n+1)*dt, 8), 'c': z[0], 'b': z[1]})
    return z, selected


cases = [
    ('established', (2, 2), 1, False),
    ('insufficient_seed', (.1, .1), 1, False),
    ('barrier_production_disabled', (1.5, 1.5), 0, False),
    ('externally_maintained_barrier', (.1, 1.5), 0, True),
]
numeric = {}
for name, initial, production, clamp in cases:
    coarse, _ = trajectory(initial, 80, .02, production, clamp)
    fine, points = trajectory(initial, 80, .01, production, clamp)
    error = max(abs(x-y) for x, y in zip(coarse, fine))
    assert error < 1e-8
    target = (1.5, 1.5) if name in ('established', 'externally_maintained_barrier') else (0, 0)
    assert max(abs(x-y) for x, y in zip(fine, target)) < 1e-7
    numeric[name] = {'initial': initial, 'final': fine, 'step_difference': error,
                     'trajectory': points}

result = {'status': 'all checks passed', 'exact_fixed_points': fixed,
          'origin_eigenvalues': ['-3/4', '-1'], 'numerical_cases': numeric,
          'method': 'RK4 at steps 0.02 and 0.01, t=80; proofs supply general claims',
          'scope': 'Boundary function and maintenance conditional on fixed patch geometry, supplied growth mechanism and external precursors; no organism or origin-of-life experiment.'}
destination = Path(__file__).with_name('boundary-maintenance-checks.json')
destination.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'status': result['status'], 'exact_fixed_points': fixed,
                  'numerical_cases': {name: {key: value for key, value in data.items() if key != 'trajectory'} for name, data in numeric.items()}}, indent=2))
