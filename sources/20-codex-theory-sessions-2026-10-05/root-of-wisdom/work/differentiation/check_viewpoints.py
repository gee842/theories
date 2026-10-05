"""Exact finite checks for viewpoint-audit.md; no external dependencies."""
from itertools import product
from fractions import Fraction
import json
from pathlib import Path

# State: phase, mode, disturbances, records, messages, viability, body errors.
# Two identical circuits. Mode 0 requires local compensation; mode 1 adds
# the other site's disturbance. The message link is controlled by link.
def step(s, link):
    phase, mode, h, r, q, v, b = s
    if phase == 0:
        r = tuple(h[i] if v[i] else r[i] for i in range(2))
    elif phase == 1 and link:
        q = tuple(r[1-i] if v[i] and v[1-i] else q[i] for i in range(2))
    elif phase == 2:
        a = tuple(v[i] * (r[i] ^ (mode * q[i])) for i in range(2))
        b = tuple(a[i] ^ h[i] ^ (mode * h[1-i]) for i in range(2))
        v = tuple(v[i] * (1-b[i]) for i in range(2))
    return ((phase+1) % 3, mode, h, r, q, v, b)

def swap(s):
    phase, mode, *pairs = s
    return (phase, mode, *(tuple(reversed(p)) for p in pairs))

bits = tuple(product((0, 1), repeat=2))
states = tuple((p, mode, h, r, q, v, b)
               for p in range(3) for mode in (0, 1)
               for h, r, q, v, b in product(bits, repeat=5))
symmetry_checks = 0
for s in states:
    for link in (False, True):
        assert step(swap(s), link) == swap(step(s, link))
        symmetry_checks += 1

local_trials = message_trials = turnover_trials = 0
for h, r0, b0 in product(bits, repeat=3):
    s = (0, 0, h, r0, (0, 0), (1, 1), b0)
    for _ in range(3):
        s = step(s, False)
    assert s[-2] == (1, 1) and s[-1] == (0, 0)
    local_trials += 1
    s = (0, 1, h, r0, (0, 0), (1, 1), b0)
    for _ in range(3):
        s = step(s, True)
    assert s[-2] == (1, 1) and s[-1] == (0, 0)
    message_trials += 1

# Local state has an actually copied record and a currently blank sensor.
history_cases = []
for h in bits:
    s = step((0, 0, h, (0, 0), (0, 0), (1, 1), (0, 0)), False)
    assert s[0] == 1 and s[3] == h
    history_cases.append({"field": h, "records": s[3], "current_sensors": (0, 0)})

# Exhaust all deterministic policies based only on one local bit.
policies = bits  # a = policy[local_record]
policy_results = []
for i in range(2):
    for mode in (0, 1):
        for policy in policies:
            correct = sum(policy[h[i]] == (h[i] ^ (mode*h[1-i])) for h in bits)
            policy_results.append({"site": i, "mode": mode, "policy": policy,
                                   "accuracy": str(Fraction(correct, 4))})
        best = max(sum(policy[h[i]] == (h[i] ^ (mode*h[1-i])) for h in bits)
                   for policy in policies)
        assert best == (4 if mode == 0 else 2)

constant_success = [sum(a == h[0] for h in bits) for a in (0, 1)]
assert constant_success == [2, 2]

# Intervene on each stored record after sensing, with messages disabled and
# local mode. The targeted circuit fails; the other remains viable.
record_interventions = 0
for h in bits:
    for i in range(2):
        r = list(h)
        r[i] ^= 1
        s = step((2, 0, h, tuple(r), (0, 0), (1, 1), (0, 0)), False)
        assert s[-2][i] == 0 and s[-2][1-i] == 1
        record_interventions += 1

# All binary target functions on four field states: exact regulation iff
# target is constant on every record fiber. Check every deterministic policy.
sufficiency_checks = 0
for target in product((0, 1), repeat=4):
    for i in range(2):
        fiber_constant = all(target[a] == target[b]
                             for a, ha in enumerate(bits)
                             for b, hb in enumerate(bits) if ha[i] == hb[i])
        feasible = any(all(policy[h[i]] == target[k] for k, h in enumerate(bits))
                       for policy in policies)
        assert fiber_constant == feasible
        sufficiency_checks += 1

report = {
    "arithmetic": "Finite Boolean enumeration and exact rational accuracies",
    "global_states": len(states),
    "site_swap_equivariance_checks": symmetry_checks,
    "local_regulation_trials": local_trials,
    "coupled_regulation_with_message_trials": message_trials,
    "record_intervention_checks": record_interventions,
    "all_binary_target_sufficiency_checks": sufficiency_checks,
    "history_cases": history_cases,
    "exhaustive_local_policy_results": policy_results,
    "private_view_classes": {
        "A": [[[0, 0], [0, 1]], [[1, 0], [1, 1]]],
        "B": [[[0, 0], [1, 0]], [[0, 1], [1, 1]]],
        "parity_required_classes": [[[0, 0], [1, 1]], [[0, 1], [1, 0]]]
    },
    "proved_not_measured": [
        "Claims are conditional on supplied copying, retention, actuator, timing and viability mechanisms.",
        "No claim about phenomenal experience or the historical origin of these mechanisms.",
        "Uniform disturbance ensemble is used for accuracy comparisons; deterministic regulation is all-state."
    ]
}
Path(__file__).with_name("viewpoint-checks.json").write_text(json.dumps(report, indent=2)+"\n")
print(json.dumps({k: report[k] for k in list(report)[:7]}, indent=2))
