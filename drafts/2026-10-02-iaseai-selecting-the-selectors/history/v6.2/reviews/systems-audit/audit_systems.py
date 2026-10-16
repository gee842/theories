#!/usr/bin/env python3
"""Independent boundary checks for V6.2 systems review; standard library only.
No manuscript functions or existing tests are imported.
"""
import json
import math
import random
from pathlib import Path


def rk4(f, y, t, h):
    a = f(t, y)
    b = f(t + h / 2, [v + h * k / 2 for v, k in zip(y, a)])
    c = f(t + h / 2, [v + h * k / 2 for v, k in zip(y, b)])
    d = f(t + h, [v + h * k for v, k in zip(y, c)])
    return [v + h * (ka + 2 * kb + 2 * kc + kd) / 6
            for v, ka, kb, kc, kd in zip(y, a, b, c, d)]


def sigmoid(u):
    return 1 / (1 + math.exp(-u)) if u >= 0 else math.exp(u) / (1 + math.exp(u))


def participation(initial=(0.5, 0.4), masses=(0.1, 0.9), h=0.02, T=500):
    def rhs(t, u):
        x = sum(m * sigmoid(v) for m, v in zip(masses, u))
        return [0.3 - 0.48 * (1 - x), 0.3 - (0.6 - 0.4 * x)]
    u = [math.log(x / (1 - x)) for x in initial]
    x_initial = sum(m * x for m, x in zip(masses, initial))
    initial_du = rhs(0, u)
    initial_dx = sum(m * x * (1 - x) * du for m, x, du in zip(masses, initial, initial_du))
    t_cross = None
    for step in range(int(T / h)):
        t = step * h
        u = rk4(rhs, u, t, h)
        total = sum(m * sigmoid(v) for m, v in zip(masses, u))
        if t_cross is None and total < 0.375:
            t_cross = t + h
    return dict(initial_total=x_initial, initial_total_derivative=initial_dx,
                time_below_first_threshold=t_cross, final_types=[sigmoid(v) for v in u],
                final_total=total, h=h, T=T)


def boundary_field(h=0.02, T=3000):
    # a=b=c=d=epsilon=zeta=1 => G=1; core pruning removes nothing.
    def rhs(t, y):
        u, z = y
        return [z - 1, sigmoid(u) - z]
    u0 = math.log(0.99 / 0.01)
    y = [u0, 0.99]
    for k in range(int(T / h)):
        y = rk4(rhs, y, k * h, h)
    return dict(gain=1, core_nonempty=True, initial=[0.99, 0.99],
                final_share=sigmoid(y[0]), final_support=y[1], T=T)


def host_path(kind, h=0.02, T=500):
    # Host parameters are manuscript HO's; integrate logit racing share and V.
    def delta(t):
        return 0.08 if kind == 'constant' else 0.08 + 0.92 * (1 - math.exp(-t))
    def rhs(t, y):
        u, v = y
        return [-delta(t), v * (0.05 * (1 - v) - 0.08 * sigmoid(u))]
    y = [math.log(99), 1.0]
    v_min, t_min = 1.0, 0
    for k in range(int(T / h)):
        y = rk4(rhs, y, k * h, h)
        if y[1] < v_min:
            v_min, t_min = y[1], (k + 1) * h
    return dict(initial_margin=delta(0), minimum_host=v_min, minimum_time=t_min,
                final_host=y[1], floor=0.3, h=h)


def sprt(mu, sigma=1, runs=20000, seed=17):
    # Exact iid Gaussian LLR for H0:mu=0 vs H1:mu=1, matching the manuscript's tested endpoints.
    # Policy threshold is 0.5; values 0.49/0.51 are outside the endpoints but on either side of that threshold.
    a, b = 0.01, 0.05 / 7
    upper = math.log((1 - b) / a)
    lower = math.log(b / (1 - a))
    rng = random.Random(seed)
    met, total_n = 0, 0
    for _ in range(runs):
        llr = 0.0
        n = 0
        while lower < llr < upper:
            llr += (rng.gauss(mu, sigma) - 0.5) / sigma**2
            n += 1
        met += llr >= upper
        total_n += n
    return dict(mean=mu, probability_declared_met=met / runs,
                mean_observations=total_n / runs, runs=runs,
                false_met_bound_at_H0=a / (1 - b), false_unmet_bound_at_H1=b / (1 - a))


def closed_form_checks():
    # The direct sanction game includes true removal despite p_det=0.
    # Safe option costs .3; unsafe sanction detection is zero. A common subsidy can support safe.
    tax, det, fine, subsidy = 0.3, 0.0, 1.0, 0.4
    # Second-order payoff rents R_i/d: a common d increase is not keyed to a carrier.
    old_rents, new_rents = [2.0, 4.0], [1.0, 2.0]
    own_change = new_rents[0] - old_rents[0]
    rival_change = new_rents[1] - old_rents[1]
    return dict(
        test_B=dict(own_absolute_change=own_change, rival_absolute_change=rival_change,
                    own_relative_change=own_change-rival_change),
        detection_vs_removal=dict(safe_net_payoff=-tax, unsafe_net_payoff=-det*fine,
                                 safe_after_auditable_intervention_subsidy=-tax+subsidy),
        oversight=dict(p_each=0.9, layers=6, iid_serial=0.9**6,
                       perfectly_correlated_serial=0.9,
                       disjoint_failure_events_serial=0.4),
    )


if __name__ == '__main__':
    output = {
        'participation': [participation(h=h) for h in (0.02, 0.01)],
        'field_equality': boundary_field(),
        'liability_margin': {kind: [host_path(kind, h=h) for h in (0.02, 0.01)]
                             for kind in ('constant', 'growing')},
        'readiness_simple_vs_threshold': [sprt(mu) for mu in (0, 0.49, 0.51, 1)],
        'closed_form': closed_form_checks(),
    }
    assert all(r['initial_total'] > .375 and r['final_total'] < 1e-12
               for r in output['participation'])
    assert output['field_equality']['final_share'] < 1e-10
    assert output['liability_margin']['constant'][0]['minimum_host'] < .3
    assert output['liability_margin']['growing'][0]['minimum_host'] > .3
    assert output['readiness_simple_vs_threshold'][1]['probability_declared_met'] > .3
    assert output['readiness_simple_vs_threshold'][2]['probability_declared_met'] < .7
    path = Path(__file__).with_name('results.json')
    path.write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output, indent=2))
    print('All independent boundary assertions passed.')
