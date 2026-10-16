"""Independent finite-control checks of the continuous establishment frontier.

Uses exact rational reachable-state dynamic programming, then separately checks
random admissible piecewise-constant controls against the proved upper bound.
The numerical checks support implementation and arithmetic, not universality.
"""

from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import random


def frontier(alpha, delta, floor, initial, beta, horizon):
    p = delta * floor / alpha
    reserve_time = math.log(initial / floor) / delta
    return beta * (min(horizon, reserve_time)
                   + (1 - p) * max(0, horizon - reserve_time))


def exact_reachability(p, initial_multiple, steps=8):
    # A time step log(2)/delta gives decay exactly 1/2. Normalize floor=1.
    # With delta=1, alpha=1/p, exact capacity update is c/2 + u/(2p).
    # Work is measured in beta*step units, making all arithmetic rational.
    controls = [F(i, 4) for i in range(5)]
    states = {F(initial_multiple): F(0)}
    reserve_steps = {1: 0, 2: 1, 4: 2}[initial_multiple]
    records = []
    for step in range(1, steps + 1):
        successors = {}
        for capacity, work in states.items():
            for control in controls:
                next_capacity = capacity / 2 + control / (2 * p)
                if next_capacity < 1:
                    continue
                # Capacity is monotone within each constant-control interval,
                # so endpoint feasibility ensures continuous service there.
                next_work = work + 1 - control
                if next_work > successors.get(next_capacity, F(-1)):
                    successors[next_capacity] = next_work
        states = successors
        observed = max(states.values())
        expected = min(step, reserve_steps) + (1 - p) * max(0, step-reserve_steps)
        assert observed == expected, (p, initial_multiple, step, observed, expected)
        records.append({"steps": step, "reachable_capacities": len(states),
                        "maximum_normalized_work": str(observed)})
    return {"maintenance_fraction": str(p), "initial_multiple": initial_multiple,
            "exact_matches": len(records), "horizons": records}


def sampled_controls(seed=5102026, count=1000):
    rng = random.Random(seed)
    closest_gap = math.inf
    for _ in range(count):
        delta = rng.uniform(.15, 2.5)
        floor = rng.uniform(.2, 3)
        p = rng.uniform(.12, 1)
        alpha = delta * floor / p
        initial = floor * rng.uniform(1, 5)
        beta = rng.uniform(.2, 3)
        horizon = rng.uniform(.1, 8)
        interval = horizon / 20
        decay = math.exp(-delta * interval)
        gain = alpha / delta * (1-decay)
        capacity, progress = initial, 0.0
        for _ in range(20):
            minimum = max(0.0, (floor-decay*capacity) / gain)
            assert minimum <= 1 + 1e-12
            control = rng.uniform(minimum, 1)
            capacity = decay*capacity + gain*control
            progress += beta*interval*(1-control)
            assert capacity >= floor - 1e-11
        bound = frontier(alpha, delta, floor, initial, beta, horizon)
        gap = bound-progress
        assert gap >= -1e-10, (bound, progress)
        closest_gap = min(closest_gap, gap)
    return {"seed": seed, "admissible_schedules": count,
            "bound_violations": 0, "smallest_bound_gap": closest_gap}


def main():
    exact = [exact_reachability(p, r)
             for p in [F(1), F(3, 4), F(1, 2), F(1, 4)]
             for r in [1, 2, 4]]
    witnesses = {
        "perpetual_operation_without_establishment": frontier(1, 1, 1, 1, 1, 100),
        "ongoing_margin_at_deadline_four": frontier(2, 1, 1, 1, 1, 4),
        "reserve_plus_margin_at_deadline_three": frontier(2, 1, 1, math.e, 1, 3),
        "insufficient_deadline": frontier(2, 1, 1, math.e, 1, 2.5),
        "finite_reserve_no_margin": frontier(1, 1, 1, math.e, 1, 100),
    }
    assert list(witnesses.values()) == [0, 2, 2, 1.75, 1]
    result = {
        "status": "pass",
        "scope": "Internal mathematical checks; no empirical validation or universal health theorem.",
        "method": "Exact rational reachable-state enumeration over five admissible effort levels, plus sampled feasible controls.",
        "exact_horizon_comparisons": sum(r["exact_matches"] for r in exact),
        "exact_cases": exact,
        "random_control_checks": sampled_controls(),
        "numerical_witnesses": witnesses,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    target = Path(__file__).with_name("VERIFICATION.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ["status", "exact_horizon_comparisons", "random_control_checks", "numerical_witnesses"]}, indent=2))


if __name__ == "__main__":
    main()
