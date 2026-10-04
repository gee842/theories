"""Independent counterexamples for REVIEW-v6-codex.md (standard library only).

These check specific overgeneralizations in V6. They do not validate the full
manuscript, estimate real-world parameters, or establish institutional safety.
Run: python3 counterexamples_codex.py
"""

import json
import math


def emit(name, **values):
    print(json.dumps({"case": name, **values}, sort_keys=True))


# Direct discounted values, not a definition of sustainability using the
# manuscript's disputed inequality. Punishment v is stipulated credible, as in
# the proposition; these are one-step incentive comparisons at cooperation.
C, v, gain, discount = 3.0, 1.0, 1.0, 0.9
cooperate = C / (1 - discount)
for pd, decisive in [(1.0, 2.0), (0.5, 3.0)]:
    deviate = C + gain + discount * (
        pd * decisive + (1 - pd) * v
    ) / (1 - discount)
    printed_bound = discount * (1 - pd) * (C - v) / (1 - discount)
    actual_bound = discount * (
        (1 - pd) * (C - v) + pd * (C - decisive)
    ) / (1 - discount)
    assert gain > 0 and cooperate > deviate
    assert gain <= actual_bound
    if pd == 1:
        assert decisive <= C and gain > printed_bound
    emit("decisive_continuation", pd=pd, decisive=decisive,
         cooperative_value=round(cooperate, 10),
         deviation_value=round(deviate, 10),
         printed_bound=round(printed_bound, 10),
         actual_bound=round(actual_bound, 10))


# A universally applicable rule can have heterogeneous incidence.
baseline, costs = [1.0, 1.0], [0.3, 0.1]
after = [p - c for p, c in zip(baseline, costs)]
mean = sum(after) / 2
relative_growth = [p - mean for p in after]
assert relative_growth[0] < 0 < relative_growth[1]
unsafe_payoff = 1 - 0.20
safe_payoff = 1 - 0.01 - 0.01
assert safe_payoff > unsafe_payoff
emit("common_rule_and_unilateral_safety", after_rule_payoffs=after,
     relative_growth=relative_growth, unsafe_payoff=unsafe_payoff,
     safe_payoff=safe_payoff)


# Three-player relative objectives need not oppose the communicating pair.
def objectives(state, guess):
    good = float(state == guess)
    payoffs = [good, good, 0.0]
    return [payoffs[i] - sum(payoffs[j] for j in range(3) if j != i) / 2
            for i in range(3)]


for state in [0, 1]:
    honest, lie = objectives(state, state), objectives(state, 1 - state)
    assert abs(sum(honest)) < 1e-12
    assert honest[0] > lie[0] and honest[1] > lie[1]
without_talk = sum(objectives(t, 0)[1] for t in [0, 1]) / 2
with_talk = sum(objectives(t, t)[1] for t in [0, 1]) / 2
assert with_talk == 0.5 and without_talk == 0.25
emit("informative_relative_cheap_talk", receiver_no_talk=without_talk,
     receiver_truthful_talk=with_talk)


# R1: finite-horizon safety does not entail all-time viability. With load <=1,
# the full-load logistic solution is a lower bound on the host state.
H, floor = 50, 0.2
host_lower_bound = 1 / (2 * math.exp(0.01 * H) - 1)
crossing = math.log(3) / 0.01
assert 0.02 > 0.01 * (1 - floor)  # H0 holds; floor eventually reachable.
assert host_lower_bound > floor and crossing > H
emit("finite_horizon_zero_liability", horizon=H, floor=floor,
     host_lower_bound=host_lower_bound, full_load_crossing=crossing)


# R3: R=2, but a low initial state converges to no capture. The invariant
# rectangle [0,.1] x [0,.2] supplies the analytic argument; RK4 illustrates it.
def field(x, z):
    return x * (1 - x) * (z - 1), 2 * x - z


x, z, step, max_z = 0.1, 0.1, 0.001, 0.1
for _ in range(20000):
    k1 = field(x, z)
    k2 = field(x + step * k1[0] / 2, z + step * k1[1] / 2)
    k3 = field(x + step * k2[0] / 2, z + step * k2[1] / 2)
    k4 = field(x + step * k3[0], z + step * k3[1])
    x += step * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
    z += step * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
    max_z = max(max_z, z)
    assert 0 <= x <= 0.1 and 0 <= z <= 0.2
assert x < 1e-8 and z < 1e-7
emit("uncaptured_basin_above_row_threshold", R=2, time=20,
     x=x, z=z, maximum_z=max_z)


# One population can have non-selection transmission. A costly trait with
# mutation/transmission obeys zdot=(1-z)(mu-c*z); z*=mu/c is stable.
c, mu = 1.0, 0.2
equilibrium = mu / c
flow = lambda q: (1 - q) * (mu - c * q)
assert flow(equilibrium - 0.01) > 0 > flow(equilibrium + 0.01)
emit("one_group_with_transmission", costly_trait_equilibrium=equilibrium)


# Prop6.1(5) needs a condition on the exponent of cost, not only b versus d.
def theta_threshold(eps):
    b, d, c = eps, 1.0, eps ** 3
    return (eps * (b - d) - c) / (eps * (b / 3 + d))


thresholds = {str(eps): theta_threshold(eps) for eps in [10, 100, 1000]}
assert thresholds["1000"] < thresholds["100"] < thresholds["10"] < -1
emit("cost_exponent_counterexample", n=4, beta_b=1, beta_d=0,
     beta_c=3, thresholds=thresholds)


# Prop6.4(2): at least one of all/no delegation must be an equilibrium.
draws = 0
for n in range(2, 11):
    for A in [0.01, 0.1, 0.5, 1.0]:
        for speed in [0.0, 0.1, 1.0, 10.0, 1000.0]:
            g0 = A * n * (1 + speed) / (n + speed)
            gall = A * (n + (n - 1) * speed) / n
            difference = A * (n - 1) * speed ** 2 / (n * (n + speed))
            assert math.isclose(gall - g0, difference, abs_tol=1e-10)
            assert g0 <= 1 or gall >= 1
            draws += 1
emit("delegation_neither_is_impossible", cases=draws)
print("All independent counterexample checks passed.")
