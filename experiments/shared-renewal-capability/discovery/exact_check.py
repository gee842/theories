#!/usr/bin/env python3
"""Exact finite checks for CONSEQUENTIAL-DISCOVERY.md; no empirical data.

This verifies a declared deterministic experiment grammar and resource ledger,
not the statistical theorem or physical adequacy of the toy process. All
arithmetic used for assertions is integer/Fraction arithmetic.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
STATES = ("a", "b", "c", "d")
NEXT = {"a": "c", "b": "a", "c": "d", "d": "d"}


def outcome(s, length):
    for _ in range(length):
        s = NEXT[s]
    return int(s == "d")


def profile(s, horizon):
    return tuple(outcome(s, length) for length in range(horizon + 1))


def partition(horizon):
    blocks = {}
    for s in STATES:
        blocks.setdefault(profile(s, horizon), []).append(s)
    return list(blocks.values())


def fr(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main():
    profiles = {s: list(profile(s, 3)) for s in STATES}
    assert profile("a", 1) == profile("b", 1)
    assert outcome("a", 2) == 1 and outcome("b", 2) == 0
    assert len(partition(1)) == 3 and len(partition(2)) == 4

    # The primitive is unchanged. The extra test is its length-two composition.
    # Charge every length-0..3 experiment afresh for all four preparations.
    budget = 100
    spent = 0
    jobs = []
    for length in range(4):
        spent += 1  # construct/compile this finite experimental program
        jobs.append({"job": f"construct length-{length} program", "cost": 1,
                     "cumulative_cost": spent})
        for s in STATES:
            cost = 2 + length + 1 + 1  # preparation/reset, moves, readout, record
            spent += cost
            jobs.append({"job": f"prepare {s}, execute {length} moves",
                         "cost": cost, "cumulative_cost": spent})
            assert spent + 4 <= budget  # reserve representation installation
    spent += 4
    jobs.append({"job": "install refined response table", "cost": 4,
                 "cumulative_cost": spent})
    assert spent == 96 and budget - spent == 4

    # Supplied deterministic loss table: the relevant distinctions are already
    # independently specified as losses, not inferred ethical standing.
    weights = (F(1, 3), F(2, 3))
    losses = ((F(0), F(1, 2)), (F(1, 2), F(0)))
    eta = F(1, 2)
    coarse_losses = [sum(weights[i] * losses[i][a] for i in range(2))
                     for a in range(2)]
    minimum_regret = min(coarse_losses)
    assert minimum_regret == eta * min(weights) == F(1, 6)
    # A randomized context-blind rule is affine in its mixing probability,
    # so its minimum is one of these two endpoints.
    per_use_cost, error_bound = F(1, 30), F(1, 60)
    net_per_use_lower = minimum_regret - per_use_cost - error_bound
    assert net_per_use_lower == F(7, 60)
    deployment_uses, sunk_inquiry_cost = 900, F(96)
    # This last illustration expressly converts the paid inquiry bill into
    # declared loss units at rate 1; that conversion is not a physical law.
    net_horizon_lower = deployment_uses * net_per_use_lower - sunk_inquiry_cost
    assert net_horizon_lower == 9

    # Exact finite checks of the summable statistical error allocation.
    delta = F(1, 20)
    error_prefix = {}
    for M in (1, 2, 10, 100):
        assigned = sum((delta / (k*(k+1)*m*(m+1))
                        for m in range(1, M+1) for k in range(1, m+1)), F(0))
        rectangle_bound = delta * F(M, M+1)**2
        assert assigned <= rectangle_bound < delta
        error_prefix[str(M)] = {"assigned": fr(assigned),
                               "rectangle_bound": fr(rectangle_bound)}

    # Exact support work at the already-derived two-support model's floors:
    # p1=p2=1/4, so B(T)=T/2. This pays the illustrative 96 work units.
    work_time = 192
    work_capacity = F(work_time) * (1-F(1,4)-F(1,4))
    assert work_capacity == spent

    sources = [
        "theories/becoming/chapters/FORMAL-SPECIFICATION.md",
        "theories/becoming/chapters/FORMAL-CORE.md",
        "_process/research/2026-10-05-causal-foundations/outputs/formal-results.md",
        "_process/research/2026-10-04-integrated-evolution/prospective-revision-math.md",
        "_process/research/2026-10-04-integrated-evolution/candidate-discovery-math.md",
        "_process/research/2026-10-05-generative-health/discovery/DISCOVERY-MATH.md",
        "_process/research/2026-10-05-revisable-concern/settlement/formal/FEATURE-CONSTRUCTION.md",
    ]
    result = {
        "status": "all exact assertions passed",
        "git_head_at_check": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "scope": "Exact arithmetic for a supplied deterministic finite model; no empirical, noisy-sample, universal-discovery, or autonomous-formation validation.",
        "arithmetic": "Python integers and fractions.Fraction; no floating arithmetic in checks",
        "state_transition": NEXT,
        "outcome_profiles_length_0_to_3": profiles,
        "partitions": {str(h): partition(h) for h in range(4)},
        "new_separating_program": {"primitive": "u", "composition": "u;u",
                                   "same_old_profile": ["a", "b"],
                                   "expanded_outcomes": {"a": 1, "b": 0}},
        "paid_jobs": jobs,
        "budget": budget, "spent": spent, "remaining": budget-spent,
        "declared_loss_example": {
            "context_weights": list(map(fr, weights)),
            "losses": [list(map(fr, row)) for row in losses],
            "coarse_minimum_regret": fr(minimum_regret),
            "per_use_access_cost": fr(per_use_cost),
            "feature_error_bound": fr(error_bound),
            "per_use_net_gain_lower": fr(net_per_use_lower),
            "uses": deployment_uses,
            "inquiry_cost_in_declared_loss_units": fr(sunk_inquiry_cost),
            "net_gain_lower": fr(net_horizon_lower)},
        "statistical_allocation_finite_checks": error_prefix,
        "support_clock_check": {"deadline": work_time, "work_capacity": fr(work_capacity),
                                "assumed_p1": "1/4", "assumed_p2": "1/4"},
        "input_sha256": {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (HERE / "exact-check.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "spent": spent,
                      "net_gain_lower": fr(net_horizon_lower)}))


if __name__ == "__main__":
    main()
