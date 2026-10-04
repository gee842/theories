"""Independent boundary/scope checks for REVIEW-v6.1-codex.md.

Standard library only. These test specific manuscript statements; they neither
certify the full theory nor estimate any real-world parameter.
"""

import json
import math


def emit(case, **values):
    print(json.dumps(dict(case=case, **values), sort_keys=True))


def gains(r, decay, diffusion, discount=0.9, won_share=1.0):
    G = r * won_share * decay / (decay + diffusion)
    Gd = r * won_share * discount * decay / (
        1 - discount * (1 - decay - diffusion)
    )
    return G, Gd


def stock_step(stocks, r, decay, diffusion=0.0, cap=None):
    strengths = [x ** r for x in stocks]
    mean = sum(stocks) / len(stocks)
    new = [(1 - decay) * x + strength / sum(strengths)
           + diffusion * (mean - x)
           for x, strength in zip(stocks, strengths)]
    return new if cap is None else [min(cap, x) for x in new]


# 1. Outside convergence, the displayed rational expression turns negative,
# but a positive relative-capacity perturbation raises future winnings.
G, Gd = gains(2, 0.2, 0)
printed_multiplier = Gd / (1 - Gd)
stocks = [2.50001, 2.49999]
pv = 0.0
for t in range(1000):
    p = stocks[0] ** 2 / sum(x ** 2 for x in stocks)
    pv += 0.9 ** (t + 1) * (p - 0.5)
    stocks = stock_step(stocks, 2, 0.2)
assert Gd > 1 and printed_multiplier < 0 < pv
emit('price_outside_convergence', Gamma=G, Gamma_discounted=Gd,
     printed_multiplier=printed_multiplier, nonlinear_positive_pv=pv)


# 2. The allowed log-strength stock gives the opposite decay comparative static.
before = gains(1.8, 0.1, 0.1)
after = gains(1.8, 0.2, 0.1)
assert before[0] < 1 < after[0] and before[1] < after[1] < 1
emit('decay_raises_loop_gain', before=before, after=after)


# 3a. A cap equal to the symmetric steady capacity is not always locally stable.
stocks = [2.499, 2.5]
first = stock_step(stocks, 3, 0.2, cap=2.5)
assert first[0] < stocks[0]
for _ in range(400):
    stocks = stock_step(stocks, 3, 0.2, cap=2.5)
assert stocks[0] < 1e-20 and stocks[1] == 2.5
emit('cap_equality_unstable', first=first, after_400=stocks)


# 3b. Diffusion supplies a restoring flow with no sharing or outside provision.
# Check the exact laggard inflow with the other actor at the cap, then evolve
# both stocks (including the leader's own diffusion loss).
smallest_inflow = math.inf
for k in range(1, 10000):
    s = k / 10000
    direct = s * s / (1 + s * s) - 0.5 * s + 0.75 * (1 - s)
    factored = (1 - s) * (1.25 * s * s - 0.5 * s + 0.75) / (1 + s * s)
    assert direct > 0 and math.isclose(direct, factored, abs_tol=1e-14)
    smallest_inflow = min(smallest_inflow, direct)
stocks = [0.01, 2.5]
for _ in range(1000):
    stocks = stock_step(stocks, 2, 0.2, 0.6, 2.5)
assert all(abs(x - 2.5) < 1e-10 for x in stocks)
emit('diffusion_restores_without_provision', smallest_grid_inflow=smallest_inflow,
     after_1000=stocks)


# 4. Falling fixed marginal cost can shut cultivation off despite correction
# growing more slowly than the manuscript's zero-fixed-cost threshold.
def cultivated(t):
    gamma = math.exp(-0.2 * t)
    d = 2 * math.exp(0.05 * t)
    f = 0.49 * math.exp(-0.01 * t)
    q = max(0.0, (1 / d - f) / gamma)
    return q, q / d


cutoff = math.log(0.5 / 0.49) / 0.04
rows = [(t, *cultivated(t)) for t in [0, 0.25, 0.5, 1, 10, 100]]
assert 0.01 < 0.05 < 0.2 / 2
assert all(cultivated(t / 1000)[1] <= 0.005 + 1e-12 for t in range(1000))
assert cultivated(1) == (0.0, 0.0)
emit('falling_fixed_cost_preserves_certificate', cutoff=cutoff, rows=rows)


# 5. Unequal compliance costs do not prevent selection for universal compliance.
payoffs = [0.9, 0.0, 0.8, 0.0]  # A comply/evade, B comply/evade
weights = [math.exp(20 * x) for x in payoffs]
shares = [x / sum(weights) for x in weights]
safe_share = shares[0] + shares[2]
assert safe_share > 0.9999999
emit('unequal_costs_safe_selection', payoffs=payoffs, shares_at_20=shares,
     compliant_share=safe_share)


# 6. A targeted stochastic continuation defeats the stage-only imitation bound.
# In punishment DD is credible: it maximizes both actors' current relative
# payoff, and actions cannot change the transition. Solve its target value by
# independent value iteration, then evaluate a deviation at cooperation.
discount, q, terminal = 0.9, 0.5, -10.0
punishment_value = 0.0
for _ in range(1000):
    punishment_value = discount * (
        q * terminal / (1 - discount) + (1 - q) * punishment_value
    )
deviation_value = 4 + discount * punishment_value
assert punishment_value < 0 and deviation_value < 0
emit('stage_imitation_not_continuation_imitation',
     normalized_punishment=(1 - discount) * punishment_value,
     cooperation_value=0, deviation_value=deviation_value)


# 7. The general delegation survival function admits an interior pure profile.
n, speed, p, lock, psi0, psi1 = 3, 1, 0.1, 0, 0, 0.015


def survival(delegate, other_delegators):
    count = other_delegators + int(delegate)
    Q = (1 - psi1) ** count * (1 - psi0) ** (n - count)
    w = (1 + speed * int(delegate)) / (n + speed * count)
    return (1 - lock * int(delegate)) * Q * (w + (1 - w) * (1 - p))


ratios = [survival(True, k) / survival(False, k) for k in range(n)]
assert ratios[0] > 1 and ratios[1] > 1 > ratios[2]
emit('delegation_needs_p_equal_one', ratios=ratios, equilibrium_delegators=2)


# 8. Nonlinear monotone fitness does not preserve the sign of both grouping
# terms, although total selection still opposes this costly global trait.
groups = [[0.0, 1.0], [0.4, 0.4]]
mean = lambda seq: sum(seq) / len(seq)


def covariance(a, b):
    return mean([x * y for x, y in zip(a, b)]) - mean(a) * mean(b)


fitness = [[math.exp(-5 * z) for z in group] for group in groups]
between = covariance([mean(g) for g in groups], [mean(w) for w in fitness])
within = mean([covariance(g, w) for g, w in zip(groups, fitness)])
total = covariance([z for g in groups for z in g], [w for g in fitness for w in g])
assert between > 0 > total and math.isclose(total, between + within)
emit('nonlinear_fitness_price_partition', between=between, within=within, total=total)


# 9. Provision increases the normalized common-channel weight. Raw conduct
# elasticity requires its own definition and need not share a global sign.
def theta_effective(Gd, n=4, theta0=0):
    return (n * theta0 - (n - 1) * (1 + theta0) * Gd) / (n - (1 + theta0) * Gd)


no_provision = gains(1, 0.2, 0.1, won_share=1)[1]
with_provision = gains(1, 0.2, 0.1, won_share=0.5)[1]
common_before = 1 + theta_effective(no_provision)
common_after = 1 + theta_effective(with_provision)
assert common_after > common_before
emit('provision_common_channel_sign', before=common_before, after=common_after)

print('All independent counterexample checks passed.')
