"""Finite countermodels for the fundamental-theory audit; standard library only.

These are different fully specified dynamics sharing the proposed schema,
observation interface, controller implementation, and resource law.
"""
from itertools import product
import json
from pathlib import Path


def feasible(z, action):
    x, cash, controller, memory, threshold = z
    return action == 0 or (x > 0 and cash == 1)


def observe(z):
    return z[0], z[1]


def execute(z):
    x, cash = observe(z)
    controller = z[2]
    return int(controller == 1 and x > 0 and cash == 1)


def step(z, action, efficacy):
    assert feasible(z, action)
    x, cash, controller, memory, threshold = z
    next_x = max(0, min(2, x + efficacy * action))
    return (next_x, cash - action,
            0 if action else controller, next_x, threshold)


states = list(product(range(3), range(2), range(2), range(3), (1, 2)))
states_set = set(states)
checks = 0
for efficacy in (-1, 0, 1):
    for z in states:
        for action in (0, 1):
            if not feasible(z, action):
                continue
            out = step(z, action, efficacy)
            assert out in states_set
            assert out[1] == z[1] - action
            assert out[3] == out[0]
            assert out[4] == z[4]
            if z[0] == 0:
                assert out[0] == 0
            checks += 1

initial = (1, 1, 1, 1, 1)
assert execute(initial) == 1
witness = {}
for name, efficacy in (("beneficial", 1), ("ineffective", 0), ("harmful", -1)):
    after = step(initial, execute(initial), efficacy)
    witness[name] = {
        "initial_observation": observe(initial),
        "action": "repair", "expense": 1,
        "next_capacity": after[0], "next_cash": after[1],
        "failure": int(after[0] == 0),
        "target_capacity_2_met": int(after[0] == 2),
    }
assert [witness[k]["next_capacity"] for k in witness] == [2, 1, 0]

# Every 2-state, 2-action deterministic plant admits a nontrivial carrier
# extension with the original plant as an exact projection.
embedding_checks = 0
kernel_count = 0
for entries in product(range(2), repeat=4):
    kernel_count += 1
    plant = dict(zip(product(range(2), repeat=2), entries))
    for x, carrier, action in product(range(2), repeat=3):
        next_x = plant[x, action]
        extended = (next_x, carrier ^ action ^ next_x)
        assert extended[0] == plant[x, action]
        embedding_checks += 1

# Distinguishability does not entail a possible strict state change.
frozen = {0: 0, 1: 1}
assert 0 != 1 and frozen[0] == 0 and frozen[1] == 1

result = {
    "states_per_repair_model": len(states),
    "valid_transition_checks": checks,
    "repair_witness": witness,
    "deterministic_plant_kernels": kernel_count,
    "carrier_projection_checks": embedding_checks,
    "frozen_distinguishable_model_checked": True,
    "scope": "Finite constructed countermodels; not empirical data or a Lean build.",
}
out_path = Path(__file__).with_name("formal_countermodels.json")
out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(result, ensure_ascii=False, indent=2))
