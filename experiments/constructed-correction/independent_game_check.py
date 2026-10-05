"""Independent tree semantics for the constructed-correction game.

Reference code is defined before importing the production module.  It does not call
production choices(), operator_moves(), Game, or Result. Exact arithmetic throughout.
Run as a script; findings are saved beside this file.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib
import importlib.util
import json
import random
import sys


def reference(parameters, cash0, owned0=False, persistent=False,
              policy="optimal", reverse=False, allocation_long_view=None):
    p = parameters
    horizon = p["T"]
    gamma = F(p["discount"])
    long_allocation = policy == "optimal" if allocation_long_view is None else allocation_long_view

    def budgets(t, cash, owned):
        # name, real current payment, delivered ownership, active this period
        obligations = []
        ell = p["ell"]
        if owned and t in p["handoff_at"]:
            obligations.append(("lapse", ell, False, False))
            for means, expenditure in (("transfer", p["J"]), ("rebuild", p["K"])):
                for operates in (False, True):
                    obligations.append((means + ("_active" if operates else "_dormant"),
                                        ell + expenditure + (p["m"] if operates else 0), True, operates))
        elif owned:
            obligations = [("idle", ell, True, False), ("activate", ell + p["m"], True, True)]
        else:
            obligations = [("idle", ell, False, False)]
            for operates in (False, True):
                obligations.append(("build_active" if operates else "build_dormant",
                                    ell + p["K"] + (p["m"] if operates else 0), True, operates))
        feasible = sorted((z for z in obligations if z[1] <= cash),
                          key=lambda z: (z[1], not z[2], z[0]))
        if policy == "never":
            feasible = [z for z in feasible if z[0] in ("idle", "lapse")]
        if policy == "always":
            activated = [z for z in feasible if z[3]]
            feasible = [activated[0] if activated else feasible[0]]
        return feasible

    def select(items, evaluate):
        # Explicit first-in-order maximizer implements the stated tie convention.
        best = None
        best_key = None
        for candidate in items:
            key = evaluate(candidate)
            if best is None or key > best_key:
                best, best_key = candidate, key
        return best

    @lru_cache(None)
    def tree(stage, t, cash, owned, action=None, operation=None):
        if t == horizon:
            return F(0), F(0), (), F(0), F(0)
        if stage == "budget":
            moves = budgets(t, cash, owned)
            if not moves:
                raise ValueError("unfunded initial decision")
            candidates = [tree("operator", t, cash, owned, move) for move in moves]
            return select(candidates, lambda z: z[3] if policy == "myopic" else z[0])
        if stage == "operator":
            chi = p["successor_chi"] if p["successor_at"] >= 0 and t >= p["successor_at"] else p["chi"]
            operations = [("harm", F(0)), ("block", F(chi)), ("safeguard", F(p["c"]))]
            if not action[3]:
                operations = [z for z in operations if z[0] != "block"]
            if reverse:
                operations = list(reversed(operations))
            candidates = [tree("allocate", t, cash, owned, action, move) for move in operations]
            return select(candidates, lambda z: z[1] if persistent else z[4])
        if stage != "allocate":
            raise AssertionError(stage)
        name, bill, delivered, enabled = action
        op, cost = operation
        choices = []
        for shared in (True, False):
            if shared:
                receipt = p["b"] if op == "safeguard" else p["x"]
            else:
                receipt = p["o"] if enabled and op != "block" else p["o0"]
            remainder = cash - bill + receipt
            stops = t < horizon - 1 and remainder < p["ell"]
            if stops:
                after_p, after_o, later = F(0), F(0), ()
            else:
                after_p, after_o, later, _, _ = tree("budget", t + 1, remainder, delivered)
            payoff_p, payoff_o = F(receipt - bill), F(p["r"] if shared else 0) - cost
            trace = (t + 1, cash, owned, name, bill, enabled, op, str(cost), shared,
                     receipt, remainder, delivered, stops)
            choices.append((payoff_p + gamma * after_p, payoff_o + gamma * after_o,
                            (trace,) + later, payoff_p, payoff_o))
        return select(choices, lambda z: z[0] if long_allocation else z[3])

    return tree("budget", 0, cash0, owned0)


def independent_static(p, active=True):
    # Enumerate every pure response map directly; collect sequentially rational outcomes.
    actions = ("harm", "block", "safeguard") if active else ("harm", "safeguard")
    costs = {"harm": F(0), "block": F(p["chi"]), "safeguard": F(p["c"])}
    outcomes = set()
    for responses in product((True, False), repeat=len(actions)):
        payoffs = []
        valid = True
        for op, stay in zip(actions, responses):
            inside = p["b"] if op == "safeguard" else p["x"]
            outside = p["o"] if active and op != "block" else p["o0"]
            if (inside if stay else outside) < max(inside, outside):
                valid = False
                break
            payoffs.append((F(p["r"]) if stay else F(0)) - costs[op])
        if valid:
            best = max(payoffs)
            for op, stay, value in zip(actions, responses, payoffs):
                if value == best:
                    income = (p["b"] if op == "safeguard" else p["x"]) if stay else (p["o"] if active and op != "block" else p["o0"])
                    outcomes.add((op, stay, income, str(value)))
    return sorted(outcomes)


def signature(row):
    return tuple(row[key] for key in ("period", "cash_before", "owned_before", "participant_action", "bill",
                 "active", "operator_action", "operator_cost", "participates", "income", "cash_after",
                 "owned_after", "terminated"))


def validate_ledger(result, p, initial_cash, initial_owned):
    previous_cash, previous_owned = initial_cash, initial_owned
    total_p = total_o = F(0)
    terminated = False
    for t, row in enumerate(result.path):
        assert row["period"] == t + 1
        assert row["cash_before"] == previous_cash
        assert row["owned_before"] == previous_owned
        assert row["bill"] <= previous_cash
        assert row["bill"] >= p.ell
        expected = (p.b if row["operator_action"] == "safeguard" else p.x) if row["participates"] else (p.o if row["active"] and row["operator_action"] != "block" else p.o0)
        assert row["income"] == expected
        assert row["cash_after"] == previous_cash - row["bill"] + expected
        assert not (row["active"] and not row["owned_after"])
        op_payoff = (p.r if row["participates"] else F(0)) - F(row["operator_cost"])
        total_p += p.discount ** t * (expected - row["bill"])
        total_o += p.discount ** t * op_payoff
        assert not terminated
        terminated = row["terminated"]
        previous_cash, previous_owned = row["cash_after"], row["owned_after"]
    assert total_p == result.vp and total_o == result.vo
    if p.discount == 1:
        assert result.vp == previous_cash - initial_cash
    return terminated


def main():
    # Import production implementation only after defining the independent reference.
    location = Path(__file__).resolve().with_name("model.py")
    spec = importlib.util.spec_from_file_location("constructed_correction_review_target", location)
    target = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = target
    spec.loader.exec_module(target)
    from dataclasses import asdict, replace
    base = target.Model()
    mismatches = []
    counts = {"dynamic_comparisons": 0, "static_correspondences": 0, "strict_regime_checks": 0,
              "on_path_cessations": 0, "long_allocation_sensitivity_comparisons": 0,
              "long_allocation_sensitivity_differences": 0}
    tie_examples = []

    def check(p, cash, owned=False, persistent=False, policy="optimal", reverse=False):
        expected = reference(asdict(p), cash, owned, persistent, policy, reverse)
        result = target.Game(p, persistent, policy, reverse).solve(0, cash, owned)
        measured = (result.vp, result.vo, tuple(signature(row) for row in result.path))
        if measured != expected[:3]:
            mismatches.append({"p": asdict(p), "cash": cash, "owned": owned,
                               "persistent": persistent, "policy": policy, "reverse": reverse,
                               "measured": measured, "reference": expected[:3]})
        counts["dynamic_comparisons"] += 1
        if validate_ledger(result, p, cash, owned):
            counts["on_path_cessations"] += 1
        return result

    for c, r, chi in product((F(1, 2), F(1), F(2), F(3)), repeat=3):
        p = replace(base, T=1, c=c, r=r, chi=chi)
        for active in (False, True):
            actual = target.static_outcomes(p, active)
            expected = independent_static(asdict(p), active)
            assert actual == expected
            counts["static_correspondences"] += 1
            if active and c < min(r, chi):
                assert {z[0] for z in actual} == {"safeguard"}
                counts["strict_regime_checks"] += 1
            if active and chi < min(r, c):
                assert {z[0] for z in actual} == {"block"}
                counts["strict_regime_checks"] += 1
            if active and r < min(c, chi):
                assert {z[0] for z in actual} == {"harm"} and all(not z[1] for z in actual)
                counts["strict_regime_checks"] += 1
        if len(expected) > 1 and len(tie_examples) < 5:
            tie_examples.append({"c": str(c), "r": str(r), "chi": str(chi), "outcomes": expected})

    configurations = []
    for horizon, cash, K, m, chi, persistent in product((1, 2, 3), (2, 4, 6), (1, 3), (1, 2), (F(1, 2), F(3, 2), F(6)), (False, True)):
        configurations.append((replace(base, T=horizon, K=K, m=m, chi=chi), cash, False, persistent))
    for p, cash, owned, persistent in configurations:
        for policy in ("optimal", "never", "myopic", "always"):
            check(p, cash, owned, persistent, policy)

    # Handoffs include affordable transfer, cheaper rebuild, lapse, and immediate operation.
    successor_rows = []
    for J, K, cash, persistent in product((0, 1, 3, 6), (1, 4), (2, 3, 5, 8), (False, True)):
        p = replace(base, T=3, J=J, K=K, handoff_at=(0, 1), successor_at=1, successor_chi=F(1, 2))
        for policy in ("optimal", "never", "myopic", "always"):
            result = check(p, cash, True, persistent, policy)
            if policy == "optimal":
                successor_rows.append((J, K, cash, persistent, result.vp, [z["participant_action"] for z in result.path]))

    # Reversal of operator ties plus discount and unusually strong/weak alternatives.
    for T, o, r, discount, persistent in product((1, 2, 3), (2, 4, 5, 6), (F(0), F(1), F(4)), (F(1), F(3, 4)), (False, True)):
        p = replace(base, T=T, o=o, r=r, discount=discount)
        check(p, 6, False, persistent, reverse=True)

    # Does the baseline's myopic allocation add a material restriction on this finite core grid?
    sensitivity_examples = []
    for p, cash, owned, persistent in configurations:
        for policy in ("never", "always"):
            short = reference(asdict(p), cash, owned, persistent, policy)
            long = reference(asdict(p), cash, owned, persistent, policy, allocation_long_view=True)
            counts["long_allocation_sensitivity_comparisons"] += 1
            if short[:3] != long[:3]:
                counts["long_allocation_sensitivity_differences"] += 1
                if len(sensitivity_examples) < 5:
                    sensitivity_examples.append({"p": asdict(p), "cash": cash, "persistent": persistent,
                                                 "policy": policy, "short": short, "long": long})

    witness_fresh = check(base, 4, persistent=False)
    witness_persistent = check(base, 4, persistent=True)
    forced_build = check(replace(base, T=2), 4, persistent=True, policy="always")
    assert witness_fresh.vp == 3
    assert witness_persistent.vp == 1
    assert witness_fresh.path[0]["participant_action"] == "build_active"
    assert witness_persistent.path[0]["participant_action"] == "idle"
    assert forced_build.path[0]["operator_action"] == "block"
    assert forced_build.path[0]["cash_after"] == 2
    assert forced_build.vp == -2
    for persistent, expected_result in ((False, witness_fresh), (True, witness_persistent)):
        reversed_result = check(base, 4, persistent=persistent, reverse=True)
        assert (reversed_result.vp, reversed_result.vo, reversed_result.path) == (expected_result.vp, expected_result.vo, expected_result.path)
    assert counts["on_path_cessations"] == 0
    assert not mismatches

    report = {
        "status": "PASS",
        "production_sha256": hashlib.sha256(location.read_bytes()).hexdigest(),
        "reference_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "counts": counts,
        "witness": {"fresh": target.trace_summary(witness_fresh, 4),
                    "persistent": target.trace_summary(witness_persistent, 4),
                    "forced_activation_persistent": target.trace_summary(forced_build, 4)},
        "tie_examples": tie_examples,
        "handoff_witnesses": successor_rows,
        "allocation_sensitivity_examples": sensitivity_examples,
        "limits": ["Independent executable reference, not a proof assistant or empirical validation.",
                   "Exact deterministic tie selection is reproduced; it does not establish all-equilibrium dynamic claims.",
                   "never and always use current-period input allocation in the production implementation.",
                   "Fresh-operator vo sums receipts of different one-period operators.",
                   "Explicit cessation sets future modeled payoffs to zero; no simulated path reaches it in these cases."]}
    output = Path(__file__).with_name("independent-game-check-results.json")
    output.write_text(json.dumps(report, indent=2, default=str) + "\n")
    print(json.dumps({"status": report["status"], "counts": counts, "output": str(output)}, indent=2))


if __name__ == "__main__":
    main()
