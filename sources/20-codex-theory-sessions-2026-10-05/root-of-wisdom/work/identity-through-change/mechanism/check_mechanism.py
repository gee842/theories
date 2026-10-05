"""Exact rational checks for a deliberately specified turnover model.

These verify algebraic identities and boundary cases, not empirical adequacy.
Only the Python standard library is used.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial
from pathlib import Path
import json


class Dual:
    def __init__(self, v, d=0):
        self.v, self.d = F(v), F(d)
    def __add__(self, other):
        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.v + other.v, self.d + other.d)
    __radd__ = __add__
    def __neg__(self):
        return Dual(-self.v, -self.d)
    def __sub__(self, other):
        return self + (-other if isinstance(other, Dual) else -F(other))
    def __rsub__(self, other):
        return -self + other
    def __mul__(self, other):
        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.v * other.v, self.d * other.v + self.v * other.d)
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.v / other.v,
                    (self.d * other.v - self.v * other.d) / other.v**2)
    def __rtruediv__(self, other):
        return Dual(other) / self


rates = [F(1, 2), F(1), F(2)]
counts = dict(parameter_sets=0, positive_equilibria=0, critical_sets=0,
              below_threshold_sets=0, mass_balance_states=0,
              exact_logistic_residuals=0, exact_critical_residuals=0,
              original_cohort_ratio_checks=0, inherited_lineage_ratio_checks=0,
              stochastic_projection_states=0, detailed_balance_pairs=0)
for k, D, ain in product(rates, repeat=3):
    counts['parameter_sets'] += 1
    r = k * ain - D
    if r > 0:
        counts['positive_equilibria'] += 1
        a, x = D/k, ain-D/k
        assert x > 0 and a > 0
        assert D*(ain-a)-k*a*x == 0
        assert k*a*x-D*x == 0
        # Characteristic polynomial of the actual two-variable Jacobian.
        j11, j12, j21, j22 = -D-k*x, -k*a, k*x, k*a-D
        assert -(j11+j22) == D+r
        assert j11*j22-j12*j21 == D*r
        assert k*a*x == D*x
    elif r == 0:
        counts['critical_sets'] += 1
    else:
        counts['below_threshold_sets'] += 1
    # Washout exists in every regime, with eigenvalues -D and r.
    a, x = ain, F(0)
    j11, j12, j21, j22 = -D-k*x, -k*a, k*x, k*a-D
    assert j11+j22 == r-D
    assert j11*j22-j12*j21 == -D*r
    for a, x in product([F(0), F(1, 3), F(2)], repeat=2):
        da = D*(ain-a)-k*a*x
        dx = k*a*x-D*x
        assert da+dx == D*(ain-a-x)
        if a == 0:
            assert da > 0
        if x == 0:
            assert dx == 0
        counts['mass_balance_states'] += 1
    for x0 in [ain/8, ain/2, ain]:
        if r:
            for z in ([F(1), F(3, 2), F(2), F(10)] if r > 0
                      else [F(1), F(2, 3), F(1, 2), F(1, 10)]):
                # z=exp(r t) and dz/dt=r z. Dual numbers differentiate
                # the claimed closed solution, then compare the ODE.
                zz = Dual(z, r*z)
                xx = x0*zz/(1+k*x0*(zz-1)/r)
                assert 0 < xx.v <= ain
                assert xx.d == r*xx.v-k*xx.v**2
                counts['exact_logistic_residuals'] += 1
        else:
            for t in [F(0), F(1, 3), F(1), F(10)]:
                tt = Dual(t, 1)
                xx = x0/(1+k*x0*tt)
                assert xx.d == -k*xx.v**2
                counts['exact_critical_residuals'] += 1
    for a, x, fraction in product(rates, rates, [F(0), F(1, 4), F(1)]):
        ell = fraction*x
        dx = (k*a-D)*x
        dell = -D*ell
        dfraction = (dell*x-ell*dx)/x**2
        assert dfraction == -k*a*fraction
        counts['original_cohort_ratio_checks'] += 1
        x1, x2 = fraction*x, (1-fraction)*x
        dx1, dx2 = (k*a-D)*x1, (k*a-D)*x2
        assert dx1+dx2 == dx
        assert (dx1*x-x1*dx)/x**2 == 0
        counts['inherited_lineage_ratio_checks'] += 1

# The molecule model has substrate immigration, dilution of each molecule,
# and A+X -> 2X. Check projection onto total molecule count.
V, k, D, ain = F(3), F(1, 2), F(2, 3), F(5, 2)
arrival = D*V*ain
for na, nx in product(range(11), repeat=2):
    events = [(na+1, nx, arrival),
              (na-1, nx, D*na),
              (na, nx-1, D*nx),
              (na-1, nx+1, k*na*nx/V)]
    events = [(a, x, rate) for a, x, rate in events if rate]
    assert all(a >= 0 and x >= 0 for a, x, rate in events)
    n = na+nx
    assert sum(rate for a, x, rate in events if a+x == n+1) == arrival
    assert sum(rate for a, x, rate in events if a+x == n-1) == D*n
    if nx == 0:
        assert all(x == 0 for a, x, rate in events)
    counts['stochastic_projection_states'] += 1
m = V*ain
for n in range(31):
    # The common exp(-m) factor cancels in detailed balance.
    pi_n = m**n/F(factorial(n))
    pi_next = m**(n+1)/F(factorial(n+1))
    assert pi_n*arrival == pi_next*D*(n+1)
    counts['detailed_balance_pairs'] += 1

result = {
    'status': 'all assertions passed',
    'checks': counts,
    'scope': 'Exact algebraic checks of a constructed model. No physical measurements or stochastic simulation.',
    'analytic_results_not_replaced_by_grid': [
        'Global convergence for all positive finite parameters and nonnegative initial concentrations',
        'Original material cohort decays as exp(-D t)',
        'Finite-volume molecule model eventually loses every X almost surely because total count is a recurrent immigration-death process',
    ],
}
Path(__file__).with_name('mechanism-checks.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
