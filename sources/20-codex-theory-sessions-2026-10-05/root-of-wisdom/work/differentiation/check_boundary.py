"""Exact finite audits of the four-site phase-domain construction.

These checks are not a proof of unrestricted dynamics; the accompanying audit
contains the analytic proofs. No external dependencies or empirical data.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
import math

HERE = Path(__file__).resolve().parent
EDGES = ((0, 1), (1, 2), (2, 3), (3, 0))


def lap(x):
    return tuple(2*x[i] - x[(i-1) % 4] - x[(i+1) % 4] for i in range(4))


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def energy(x, k):
    return sum((z*z-1)**2 for z in x)/4 + k*dot(x, lap(x))/2


def potential(x, k):
    lx = lap(x)
    return tuple(z**3-z+k*v for z, v in zip(x, lx))


def rhs(x, k):
    return tuple(-v for v in lap(potential(x, k)))


def transform(x, offset, reverse=False):
    step = -1 if reverse else 1
    return tuple(x[(offset+step*i) % 4] for i in range(4))


values = tuple(map(Q, (-2, -1, 0, 1, 2))) + (Q(-1, 2), Q(1, 2))
states = [(*u, -sum(u)) for u in product(values, repeat=3)]
ks = (Q(0), Q(1, 10), Q(1, 5), Q(1, 4), Q(1, 3), Q(1, 2), Q(3, 4), Q(1))
counts = dict(states=len(states), parameters=len(ks), conservation_dissipation=0,
              energy_remainders=0, high_parameter_norm_bounds=0,
              ring_equivariance=0, invariant_mode_equations=0,
              balanced_sign_minimum_checks=0, exact_minimum_linear_rates=0)

for k in ks:
    for x in states:
        f = rhs(x, k)
        mu = potential(x, k)
        assert sum(f) == 0
        dissipation = sum((mu[i]-mu[j])**2 for i, j in EDGES)
        assert dot(mu, f) == -dissipation
        counts['conservation_dissipation'] += 1
        r2 = dot(x, x)
        r4 = r2*r2
        gap4 = sum(z**4 for z in x)-r4/4
        gapL = dot(x, lap(x))-2*r2
        assert gap4 >= 0 and gapL >= 0
        q = 1-2*k
        remainder = (r2-4*q)**2/16 + gap4/4 + k*gapL/2
        assert energy(x, k)-(1-q*q) == remainder
        assert remainder >= 0
        counts['energy_remainders'] += 1
        if k >= Q(1, 2):
            assert dot(x, f) <= -2*(2*k-1)*r2
            counts['high_parameter_norm_bounds'] += 1
        for offset in range(4):
            for reverse in (False, True):
                gx = transform(x, offset, reverse)
                assert rhs(gx, k) == transform(f, offset, reverse)
                counts['ring_equivariance'] += 1

patterns = ((1,1,-1,-1), (-1,1,1,-1), (-1,-1,1,1), (1,-1,-1,1))
for k in ks:
    for a in (Q(-2), Q(-1, 100), Q(0), Q(1, 100), Q(1, 2), Q(1), Q(2)):
        for signs in patterns:
            x = tuple(a*s for s in signs)
            amplitude_rhs = 2*a*(1-2*k-a*a)
            assert rhs(x, k) == tuple(amplitude_rhs*s for s in signs)
            counts['invariant_mode_equations'] += 1

for a in (Q(1, 4), Q(1, 2), Q(3, 4)):
    k = (1-a*a)/2
    minimizing = []
    for signs in product((-1, 1), repeat=4):
        if sum(signs):
            continue
        x = tuple(a*s for s in signs)
        if energy(x, k) == 1-(1-2*k)**2:
            minimizing.append(signs)
            assert all(z == 0 for z in rhs(x, k))
        counts['balanced_sign_minimum_checks'] += 1
    assert set(minimizing) == set(patterns)
    for lam in (Q(2), Q(2), Q(4)):
        hessian_rate = 3*a*a-1+k*lam
        dynamical_rate = -lam*hessian_rate
        assert hessian_rate > 0 and dynamical_rate < 0
        assert dynamical_rate == (-4+8*k if lam == 2 else -8+8*k)
        counts['exact_minimum_linear_rates'] += 1

# The k=0 endpoint has six, rather than four, balanced sign minima.
zero_coupling_minima = [s for s in product((-1, 1), repeat=4)
                        if sum(s) == 0 and energy(tuple(map(Q, s)), Q(0)) == 0]
assert len(zero_coupling_minima) == 6

trajectory = []
for t in (0, 1, 2, 3, 4, 5, 10):
    amplitude = math.sqrt(0.5/(1+4999*math.exp(-2*t)))
    trajectory.append(dict(t=t, amplitude=amplitude))

result = dict(status='passed', arithmetic='fractions.Fraction except labeled decimal illustration',
              counts=counts, zero_coupling_balanced_minima=len(zero_coupling_minima),
              trajectory_illustration=dict(kappa='1/4', initial_amplitude='1/100',
                  exact_formula='sqrt((1/2)/(1+4999*exp(-2*t)))', values=trajectory),
              coverage_limit='Finite checks catch algebraic errors; audit proofs establish general claims. No generic convergence or physical-data claim.')
(HERE/'boundary-checks.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
