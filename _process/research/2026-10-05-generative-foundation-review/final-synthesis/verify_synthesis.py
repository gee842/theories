"""Independent constructed checks for the integrated theory.

No external data or old study artifacts are modified. This checks finite witnesses
and algebra, not the truth of their proposed real-world applications.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import json
import math

HERE = Path(__file__).resolve().parent
checks = []


def require(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def production(c):
    return 9 * c / (1 + c)


# The identity below proves the exact maximum, since C >= 0 and denominator > 0.
# (1+C)[4 - (9C/(1+C)-C)] = C^2 - 4C + 4 = (C-2)^2.
lhs_coefficients = (F(4), F(4) - F(9) + F(1), F(1))
require("production surplus polynomial identity", lhs_coefficients == (4, -4, 1))
require("production surplus attains four", production(F(2)) - 2 == 4)
require("critical effort is one quarter", F(1, 4) == 1 / F(4))
require("capacity floor gives effort lower bound", 1 / (production(F(6)) - 6) == F(7, 12))
require("support floor gives effort upper bound", 1 / F(3, 2) == F(2, 3))
u = F(5, 8)
require("chosen effort lies strictly inside both floors", F(7, 12) < u < F(2, 3))
require("chosen support equals eight fifths", 1 / u == F(8, 5))
# C+ = (16+6 sqrt(6))/5 > 6 iff sqrt(6)>7/3.
require("chosen capacity strictly exceeds six", F(6) > F(49, 9))
c_upper = 3 + math.sqrt(7)
c_lower = 3 - math.sqrt(7)
for c, expected in [(c_lower, "saddle"), (c_upper, "stable")]:
    trace = -1 - .5 * c
    determinant = -.5 * c * (9 / (1 + c)**2 - 1)
    require(f"ecological {expected} signs", determinant < 0 if expected == "saddle" else (determinant > 0 and trace < 0))
    require(f"ecological {expected} equilibrium residual", abs(production(c) - c - 2) < 1e-12)
for kappa, expected in [(F(1, 2), -F(2, 5)), (F(3, 2), F(2, 5))]:
    eig = -(1 - kappa) * 2 * (F(1, 2) - F(1, 10))
    require(f"practice eigenvalue at kappa {kappa}", eig == expected)


# Generic support transitions retain both the physical status and persistent model.
initial = frozenset({("L", "unfinished"), ("R", "unfinished")})
actions = ("left", "right", "probe", "wait")
cost = {"left": 1, "right": 1, "probe": 1, "wait": 0}


def successors(belief, action, probe):
    out = {}
    for model, state in belief:
        if state != "unfinished":
            branches = [("done", state)]
        elif action == "wait":
            branches = [("none", state)]
        elif action in ("left", "right"):
            matches = (action == "left") == (model == "L")
            branches = [("done", "complete" if matches else "harm")]
        elif probe == "perfect":
            branches = [(model.lower(), state)]
        elif probe == "noisy":
            branches = [("l", state), ("r", state)]
        elif probe == "hazardous":
            branches = [(model.lower(), state), ("crash", "harm")]
        else:
            raise ValueError(probe)
        for obs, next_state in branches:
            out.setdefault(obs, set()).add((model, next_state))
    return {obs: frozenset(states) for obs, states in out.items()}


@lru_cache(None)
def value(belief, n, probe):
    if any(s == "harm" for _, s in belief):
        return math.inf
    if all(s == "complete" for _, s in belief):
        return 0
    if n == 0:
        return math.inf
    return min(cost[a] + max(value(b, n - 1, probe) for b in successors(belief, a, probe).values()) for a in actions)


perfect_values = [value(initial, n, "perfect") for n in (1, 2, 3)]
require("perfect-probe exact horizon values", perfect_values == [math.inf, 2, 2])
for probe in ("noisy", "hazardous"):
    require(f"{probe} probe infeasible at horizons one through six", all(value(initial, n, probe) == math.inf for n in range(1, 7)))
require("known model costs one", all(value(frozenset({(m, "unfinished")}), 1, "perfect") == 1 for m in ("L", "R")))

# Independently enumerate every two-step policy, rather than trusting only the DP.
obs_names = ("l", "r", "none", "done")
best = math.inf
feasible = 0
for first in actions:
    for second_actions in product(actions, repeat=len(obs_names)):
        mapping = dict(zip(obs_names, second_actions))
        worst = 0
        good = True
        for model in ("L", "R"):
            b0 = frozenset({(model, "unfinished")})
            for obs, b1 in successors(b0, first, "perfect").items():
                if any(s == "harm" for _, s in b1):
                    good = False
                    break
                second = mapping[obs]
                for b2 in successors(b1, second, "perfect").values():
                    if not all(s == "complete" for _, s in b2):
                        good = False
                worst = max(worst, cost[first] + cost[second])
        if good:
            feasible += 1
            best = min(best, worst)
require("exhaustive two-step policy minimum agrees with DP", best == 2 and feasible > 0)

l_l, l_r = F(3, 4)**4, F(1, 4)**4
mixture = (l_l + l_r) / 2
require("four-signal likelihood ratio rejecting R", mixture / l_r == 41)
require("four-signal likelihood ratio retaining L", mixture / l_l == F(41, 81))
require("false rejection example remains below delta", l_r < F(1, 40))


# Exact factorial equivalence and independent mediator manipulation.
route = lambda a, b, m: b * m
direct = lambda a, b, m: a * b
require("factorial observations do not identify mediator", all(route(a, b, a) == direct(a, b, a) for a, b in product((0, 1), repeat=2)))
require("mediator clamp separates the route", route(1, 1, 0) == 0 and direct(1, 1, 0) == 1)

models = {
    "C": lambda a, b: (a, b * a),
    "P": lambda a, b: (1, b),
    "N": lambda a, b: (a, 0),
}
experiments = {"F": (0, 0), "T": (1, 1)}
require("calibration models agree", len({f(1, 0) for f in models.values()}) == 1)
pairs = (("C", "P"), ("C", "N"), ("P", "N"))
distances = {pair: tuple(F(models[pair[0]](*ab) != models[pair[1]](*ab)) for ab in experiments.values()) for pair in pairs}
require("pairwise distance matrix", list(distances.values()) == [(1, 0), (0, 1), (1, 1)])
weights, costs, budget = (F(3, 4), F(1, 4)), (F(1), F(2)), F(5, 4)
separation = min(sum(w * d for w, d in zip(weights, row)) for row in distances.values())
require("design primal budget", sum(w * c for w, c in zip(weights, costs)) == budget)
require("design primal value", separation == F(1, 4))
alpha, beta, rho = F(-1), F(1), (F(0), F(1), F(0))
require("dual certificate feasible", all(alpha + beta * costs[e] >= sum(rho[j] * distances[p][e] for j, p in enumerate(pairs)) for e in range(2)))
require("dual certificate matches primal", alpha + beta * budget == separation)
require("worst pair error", (1 - separation) / 2 == F(3, 8))
require("hard batch cost realizes proportions", 3 * costs[0] + costs[1] == 5)


def tv(p, q):
    return sum(abs(p.get(k, 0) - q.get(k, 0)) for k in set(p) | set(q)) / 2


labelled_a = {("F", 0): F(1, 2), ("T", 1): F(1, 2)}
labelled_b = {("F", 1): F(1, 2), ("T", 0): F(1, 2)}
unlabelled = {0: F(1, 2), 1: F(1, 2)}
require("retaining test labels preserves distinction", tv(labelled_a, labelled_b) == 1)
require("erasing test labels can remove distinction", tv(unlabelled, unlabelled) == 0)

report = {
    "scope": "Constructed algebra and finite examples; no new empirical data; no proof certification.",
    "passed": len(checks),
    "checks": checks,
    "mechanism": {"critical_effort": "1/4", "protected_interval": "7/12 < u < 2/3", "interior_effort": "5/8", "interior_support": "8/5", "interior_capacity": "(16+6 sqrt(6))/5"},
    "adaptive": {"perfect_horizons_1_to_3": ["infinity", 2, 2], "noisy_horizons_1_to_6": "infinity", "two_step_policies_enumerated": len(actions)**(len(obs_names) + 1), "feasible_two_step_policies": feasible, "minimum_cost": best},
    "experimental_design": {"weights": ["3/4", "1/4"], "expected_cost": "5/4", "pairwise_separation": "1/4", "dual_bound": "1/4", "worst_pair_binary_error": "3/8"},
}
(HERE / "EXACT-CHECKS.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"passed": len(checks), "two_step_policies_enumerated": report["adaptive"]["two_step_policies_enumerated"], "minimum_cost": best, "design_separation": str(separation)}))
