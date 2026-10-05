"""Exact algebra checks for the constructed organization/turnover model.

These checks do not simulate organisms or establish a theory of consciousness.
The accompanying audit gives the general proof.
"""
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path

counts = {"parameter_tuples": 0, "positive_equilibria": 0,
          "below_threshold": 0, "at_threshold": 0,
          "lyapunov_point_checks": 0}
values = (Q(1, 2), Q(1), Q(2))
for a, b, f, delta, mu, c in product(values, values, (Q(0), *values), values, values, values):
    counts["parameter_tuples"] += 1
    gap = a*b*f - delta*mu
    if gap <= 0:
        counts["at_threshold" if gap == 0 else "below_threshold"] += 1
        assert delta*mu - a*b*f >= 0
        continue
    counts["positive_equilibria"] += 1
    R = a*b*f/mu
    C = R-delta
    xs = C/c
    ys = b*xs/mu
    assert xs > 0 and ys > 0
    assert a*f*ys-delta*xs-c*xs*xs == 0
    assert b*xs-mu*ys == 0
    trace = -delta - 2*c*xs - mu
    determinant = mu*(delta+2*c*xs)-a*b*f
    assert trace < 0 and determinant == mu*c*xs > 0
    assert delta+c*xs == R
    for u, v in product((Q(1, 4), Q(1, 2), Q(1), Q(2), Q(4)), repeat=2):
        du = R*(v-u)-C*u*(u-1)
        dv = mu*(u-v)
        direct = (1-1/u)*du+(R/mu)*(1-1/v)*dv
        formula = -R*(u-v)**2/(u*v)-C*(u-1)**2
        assert direct == formula
        assert (direct == 0) == (u == 1 and v == 1)
        counts["lyapunov_point_checks"] += 1

result = {"status": "all exact checks passed", "counts": counts,
          "scope": "constructed deterministic two-species maintenance model; general proof in self-audit.md",
          "limits": ["original label tends to zero, never zero at finite time in this continuum model",
                     "constant resource supply and rates are assumed",
                     "no empirical or metaphysical no-self claim was tested"]}
out = Path(__file__).with_name("self-maintenance-checks.json")
out.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
