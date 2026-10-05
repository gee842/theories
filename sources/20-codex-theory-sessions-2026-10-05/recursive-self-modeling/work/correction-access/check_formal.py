"""Independent elementary checks for formal-note.md; no evaluation data used."""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
from statistics import NormalDist
import json
import math

checked_schedules = 0
for n in range(1, 13):
    for budget in range(1, n + 1):
        best = n
        for early in combinations(range(1, n), budget - 1):
            schedule = (0,) + early + (n,)
            gap = max(right - left for left, right in zip(schedule, schedule[1:]))
            best = min(best, gap)
            checked_schedules += 1
        assert best == math.ceil(n / budget)

def delays(schedule, changes):
    return {tau: min(t for t in schedule if t >= tau) - tau for tau in changes}

changes = range(8, 48)
periodic = (0, 10, 20, 35, 45, 55)
protected = (0, 25, 55)
periodic_delays = delays(periodic, changes)
protected_delays = delays(protected, changes)
assert max(periodic_delays.values()) == 14
assert max(protected_delays.values()) == 29
hybrid_schedules = 0
optional = [t for t in range(0, 60, 5) if t not in protected]
for size in range(4):
    for selected in combinations(optional, size):
        schedule = sorted(protected + selected)
        assert len(schedule) <= 6
        assert max(delays(schedule, changes).values()) <= 29
        hybrid_schedules += 1
assert not any(t >= 56 for t in range(0, 60, 5))

# Perfect information does not stabilize a badly chosen clipped controller.
x = F(10, 9)
for t in range(20):
    u = max(F(-2), min(F(2), -2 * x))
    x = F(4, 5) * x + u
    assert x == (F(-10, 9) if t % 2 == 0 else F(10, 9))

# Pairwise squared-error identity behind the identification lower bound.
square_checks = 0
for h, x, c in product([F(-3, 2), F(0), F(7, 3)],
                       [F(0), F(1, 4)], [F(-2), F(1, 3), F(3)]):
    assert (h-x)**2 + (h-x-c)**2 == 2*(h-x-c/2)**2 + c*c/2
    square_checks += 1

# Uniform bounded-noise separation, including baseline-error extremes.
sigma, baseline_error, magnitude = F(1, 10), F(1, 20), F(1, 2)
threshold = sigma + baseline_error
for error, noise in product([-baseline_error, baseline_error], [-sigma, sigma]):
    assert abs(noise - error) <= threshold
    for change in [-magnitude, magnitude]:
        assert abs(change + noise - error) > threshold

# A Gaussian sufficient condition is a probability statement, not certainty.
normal = NormalDist()
alpha, beta, sigma, m, tests = .05, .1, .25, 4, 12
sd = sigma / math.sqrt(m)
h = sd * normal.inv_cdf(1 - alpha / (2 * tests))
delta = h + sd * normal.inv_cdf(1 - beta)
miss_probability = normal.cdf((h-delta)/sd) - normal.cdf((-h-delta)/sd)
false_alarm_union_bound = tests * 2 * (1-normal.cdf(h/sd))
assert miss_probability <= beta + 1e-12
assert false_alarm_union_bound <= alpha + 1e-12

# Stable-update bound under all extreme noise sequences of five steps.
a, k, epsilon, disturbance = F(4, 5), F(1, 2), F(1, 10), F(1, 20)
rho = abs(a-k)
forcing = abs(k)*epsilon+disturbance
control_checks = 0
noise_pairs = list(product([-epsilon, epsilon], [-disturbance, disturbance]))
for sequence in product(noise_pairs, repeat=5):
    x = F(1)
    for step, (nu, w) in enumerate(sequence, start=1):
        u = -k*(x+nu)
        assert abs(u) <= 2
        x = a*x+u+w
        upper = rho**step + forcing*(1-rho**step)/(1-rho)
        assert abs(x) <= upper
        control_checks += 1

result = {
    "status": "All checks pass; independent mathematical examples, no development or evaluation dataset used.",
    "exhaustive_terminal_schedules_N_1_through_12": checked_schedules,
    "periodic_integer_acquisition_delay_bound_tau_8_to_47": 14,
    "hybrid_protected_integer_acquisition_delay_bound_tau_8_to_47": 29,
    "hybrid_optional_schedules_checked": hybrid_schedules,
    "clipped_exact_cycle_steps": 20,
    "squared_error_identities": square_checks,
    "gaussian_example": {
        "familywise_false_alarm_bound": false_alarm_union_bound,
        "miss_probability": miss_probability,
        "maximum_miss_probability": beta,
        "minimum_shift_sufficient": delta,
        "postchange_samples_required": m,
        "tested_windows": tests,
    },
    "stable_control_extreme_noise_steps": control_checks,
}
path = Path(__file__).with_name("formal-checks.json")
path.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
