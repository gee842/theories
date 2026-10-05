"""Exact analytic checks only; does not rerun or alter frozen evaluation."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

a, k = F(4, 5), F(1, 2)
rho = a-k
trajectory_steps = 0
for g, x0, b, d in product([F(-3, 20), F(3, 20)], [F(-1), F(0), F(1)],
                           [F(-1), F(1)], [F(-1, 4), F(0), F(1, 4)]):
    r = g/(1-a)
    x, xt = x0, x0-r
    bt, dt = b+r, d+r
    for t in range(20):
        eps, eta, w = F(t % 3 - 1, 20), F(t % 5 - 2, 50), F(t % 7 - 3, 100)
        assert x+b+eps == xt+bt+eps
        assert x+d+eta == xt+dt+eta
        assert bt-dt == b-d
        u = -k*xt
        x = a*x+u+g+w
        xt = a*xt+u+w
        assert x == xt+r
        trajectory_steps += 1
    assert a*r+g == r  # equilibrium u=0

equilibria = []
for g, d in product([F(-3, 20), F(0), F(3, 20)], [F(-1, 4), F(0), F(1, 4)]):
    fixed = (g-k*d)/(1-a+k)
    assert a*fixed-k*(fixed+d)+g == fixed
    assert abs(k*(fixed+d)) <= 2
    equilibria.append({'g':float(g), 'd':float(d), 'scalar_equilibrium':float(fixed)})

r = F(3, 4)
horizon = 60
formula = horizon*r*r - 2*r*r*sum(rho**t for t in range(1,horizon+1))
formula += (r*r+1)*sum(rho**(2*t) for t in range(1,horizon+1))
mean, variance, recurrence = F(0), F(1), F(0)
for _ in range(horizon):
    mean = rho*mean+(1-rho)*r
    variance *= rho*rho
    recurrence += mean*mean+variance
assert recurrence == formula
assert horizon*r*r == F(135,4)

result = {
    'status':'All exact algebraic checks pass; no new simulation evaluation.',
    'shifted_coordinate_trajectory_steps':trajectory_steps,
    'transformed_bias_sign':'b_tilde=b+r, d_tilde=d+r, x_tilde=x-r',
    'anchor_equilibrium_magnitude':float(r),
    'sixty_steps_already_at_equilibrium_state_loss':float(horizon*r*r),
    'ideal_noiseless_perfect_coordinate_expected_state_loss_from_N01':float(formula),
    'scalar_equilibria':equilibria,
}
Path(__file__).with_name('anchor-mechanism-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='scalar_equilibria'},indent=2))
