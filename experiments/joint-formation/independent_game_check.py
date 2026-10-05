"""Independent exact reconstruction of joint-formation game stages.

The reference uses generic decision-node evaluation and independently constructed
physical transitions. Production code is imported only in the bottom comparison
adapter, after all reference and accounting functions have been defined.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import hashlib
import importlib.util
import json
import random
import sys


def reference(p, opening_cash, reverse=False):
    """Return operator value and a complete independently derived path."""
    delta = F(p["discount"])
    D = p["evidence_cost"] + p["control_cost"]

    def ordered(choices):
        return choices[::-1] if reverse else choices

    def resolve(choices, owner, concern=F(0)):
        def score(z):
            value, trajectory = z
            if owner == "operator":
                return value
            cash = F(trajectory[0]["closing_cash"])
            return cash if owner == "cold" else cash-concern*F(trajectory[0]["patient_harm"])
        selected, selected_score = None, None
        for choice in choices:
            current = score(choice)
            if selected is None or current > selected_score:
                selected, selected_score = choice, current
        assert selected is not None
        return selected

    @lru_cache(None)
    def episode(t, opening):
        if t >= p["T"]:
            return F(0), ()
        options = ["none", "alignment_capture"]
        if p["raid_enabled"]:
            options.append("reserve_raid")
        continuations = []
        for attack in ordered(options):
            pre_cost = (p["teaching_attack_cost"] if attack == "alignment_capture" else
                        p["raid_cost"] if attack == "reserve_raid" else F(0))
            removed = min(opening, p["raid_amount"]) if attack == "reserve_raid" else F(0)
            funds = opening-removed
            record = {"episode": t+1, "opening_cash": str(opening), "pre_attack": attack,
                      "operator_pre_cost": str(pre_cost), "destroyed_cash": str(removed)}
            if funds < p["ell"]:
                future, following = episode(t+1, funds)
                record.update(status="cannot_operate", closing_cash=str(funds), patient_harm="0",
                              operator_current=str(-pre_cost))
                continuations.append((-pre_cost+delta*future, (record,)+following))
            else:
                record["status"] = "operated"
                record["after_subsistence"] = str(funds-p["ell"])
                continuations.append(cold(t, funds, record))
        return resolve(continuations, "operator")

    def cold(t, funds, record):
        reserve = funds-p["ell"]
        candidates = ["none"]
        if reserve >= p["a"]:
            candidates.append("shared")
            if p["identity_enabled"] and reserve-p["a"]+p["R"] >= p["identity_cost"]:
                candidates.append("identity_gated")
        outcomes = []
        for architecture in ordered(candidates):
            bill = p["a"] if architecture != "none" else F(0)
            receipt = p["R"] if architecture != "none" else F(0)
            filter_bill = p["identity_cost"] if architecture == "identity_gated" else F(0)
            after_bill = reserve-bill
            after_receipt = after_bill+receipt
            w = p["eta"]*p["beta"] if architecture != "none" else F(0)
            g = p["kappa"]*p["G"] if architecture == "shared" and record["pre_attack"] != "alignment_capture" else F(0)
            row = dict(record, learning=architecture, lesson_bill=str(bill), after_lesson_bill=str(after_bill),
                       private_receipt=str(receipt), after_lesson_receipt=str(after_receipt), identity_bill=str(filter_bill),
                       after_filter=str(after_receipt-filter_bill), learned_w=str(w), learned_g=str(g), learned_v=str(w*g))
            outcomes.append(warm(t, funds, row, w*g))
        return resolve(outcomes, "cold")

    def warm(t, funds, record, v):
        reserve = F(record["after_filter"])
        alternatives = [("open", F(0)), ("withdraw", F(0))]
        if p["control_enabled"] and p["control_cost"]+p["cue_cost"] <= reserve:
            alternatives.append(("cue_gate", p["control_cost"]+p["cue_cost"]))
        if p["control_enabled"] and p["verification_enabled"] and D <= reserve:
            alternatives.append(("verified_gate", D))
        outcomes = []
        for policy, bill in ordered(alternatives):
            row = dict(record, profile=policy, gate_bill=str(bill), after_gate=str(reserve-bill))
            outcomes.append(operator_action(t, funds, row))
        return resolve(outcomes, "warm", v)

    def operator_action(t, funds, record):
        policy = record["profile"]
        reserve = F(record["after_gate"])
        actions = ["no_trade"] if policy == "withdraw" else ["harm", "mask", "bypass", "safeguard", "decline"]
        outcomes = []
        for action in ordered(actions):
            price = {"harm": F(0), "mask": p["mask_cost"], "bypass": p["bypass_cost"],
                     "safeguard": p["c"], "decline": F(0), "no_trade": F(0)}[action]
            if action == "safeguard":
                admitted, harm = True, F(0)
            elif action == "bypass":
                admitted, harm = True, p["H"]
            elif action == "mask":
                admitted = policy in ("open", "cue_gate")
                harm = p["H"] if admitted else F(0)
            elif action == "harm":
                admitted = policy == "open"
                harm = p["H"] if admitted else F(0)
            else:
                admitted, harm = False, F(0)
            receipt = p["b"] if admitted else p["o"]
            closing = reserve+receipt
            current = (p["r"] if admitted else F(0))-price-F(record["operator_pre_cost"])
            future, following = episode(t+1, closing)
            row = dict(record, operator_action=action, operator_action_cost=str(price), admitted=admitted,
                       production_receipt=str(receipt), patient_harm=str(harm), probe_harm="0", closing_cash=str(closing),
                       controller_net_cash=str(closing-funds), operator_current=str(current))
            outcomes.append((current+delta*future, (row,)+following))
        return resolve(outcomes, "operator")

    return episode(0, F(opening_cash))


def ledger(p, opening, value, rows):
    assert len(rows) == p["T"]
    total = F(0)
    for t, row in enumerate(rows):
        assert F(row["opening_cash"]) == opening
        removal = min(opening, p["raid_amount"]) if row["pre_attack"] == "reserve_raid" else F(0)
        assert F(row["destroyed_cash"]) == removal
        available = opening-removal
        if row["status"] == "cannot_operate":
            assert available < p["ell"]
            assert F(row["closing_cash"]) == available
            assert F(row["patient_harm"]) == 0
        else:
            assert available >= p["ell"]
            assert F(row["after_subsistence"]) == available-p["ell"]
            cash = available-p["ell"]
            bill = F(row["lesson_bill"])
            assert 0 <= bill <= cash
            cash -= bill
            assert cash == F(row["after_lesson_bill"])
            cash += F(row["private_receipt"])
            assert cash == F(row["after_lesson_receipt"])
            assert 0 <= F(row["identity_bill"]) <= cash
            cash -= F(row["identity_bill"])
            assert cash == F(row["after_filter"])
            assert 0 <= F(row["gate_bill"]) <= cash
            cash -= F(row["gate_bill"])
            assert cash == F(row["after_gate"])
            income = p["b"] if row["admitted"] else p["o"]
            assert F(row["production_receipt"]) == income
            cash += income
            assert cash == F(row["closing_cash"])
            assert F(row["controller_net_cash"]) == cash-available
            assert F(row["probe_harm"]) == 0
            assert F(row["learned_v"]) == F(row["learned_w"])*F(row["learned_g"])
        total += p["discount"]**t*F(row["operator_current"])
        opening = F(row["closing_cash"])
    assert total == value


def main():
    # Adapter begins here. The independent reference above is already defined.
    target_path = Path(__file__).with_name("model.py")
    spec = importlib.util.spec_from_file_location("joint_formation_audit_target", target_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    from dataclasses import asdict, replace
    original = module.Parameters()
    cases = []
    named = [
        ("positive", {}, F(5)),
        ("cheap_raid", {"raid_enabled": True, "raid_cost": F(1, 4)}, F(5)),
        ("expensive_raid", {"raid_enabled": True, "raid_cost": F(3)}, F(5)),
        ("zero_value", {"beta": F(0)}, F(5)),
        ("no_alignment", {"G": F(0)}, F(5)),
        ("high_concern", {"beta": F(6)}, F(5)),
        ("no_learning_return", {"R": F(0)}, F(5)),
        ("free_identity", {"identity_cost": F(0)}, F(5)),
        ("cheap_capture", {"teaching_attack_cost": F(1, 2)}, F(5)),
        ("cheap_bypass", {"bypass_cost": F(1, 2)}, F(5)),
        ("cue_only", {"verification_enabled": False}, F(5)),
        ("no_control", {"control_enabled": False}, F(5)),
        ("poor_start", {}, F(3)),
        ("bootstrap_trap", {"b": F(3)}, F(3)),
        ("resource_failure", {"b": F(1), "o": F(0), "R": F(0)}, F(3)),
        ("gate_then_failure", {"ell": F(10), "R": F(6), "o": F(1), "beta": F(7, 2)}, F(12)),
        ("identity_after_return", {"identity_cost": F(6)}, F(5)),
        ("partial_learning", {"eta": F(1, 2), "kappa": F(1, 2), "beta": F(14)}, F(5)),
        ("zero_operator_rent", {"r": F(0)}, F(5)),
    ]
    for name, overrides, cash in named:
        for horizon in (1, 2, 3, 6):
            for discount in (F(0), F(1, 2)):
                for reverse in (False, True):
                    p = replace(original, T=horizon, discount=discount, **overrides)
                    cases.append((name, p, cash, reverse))
    rng = random.Random(205005)
    for i in range(180):
        D = rng.choice((2, 3, 5))
        p = replace(original, T=rng.choice((1, 2, 3)), R=F(rng.choice((4, 8))),
                    evidence_cost=F(D-1), control_cost=F(1), beta=rng.choice((F(0), F(7, 2), F(6))),
                    identity_cost=F(rng.choice((0, 4, 8))), teaching_attack_cost=rng.choice((F(1, 2), F(2))),
                    bypass_cost=rng.choice((F(1, 2), F(2))), discount=rng.choice((F(0), F(1, 2))))
        cases.append((f"sample_{i}", p, F(rng.choice((3, 5, 7))), bool(rng.randrange(2))))
    reports = []
    counts = {"comparisons": 0, "realized_episodes": 0, "cannot_operate_episodes": 0,
              "fresh_cases": 0, "persistent_cases": 0, "reversed_tie_cases": 0}
    differences = []
    for name, p, cash, reverse in cases:
        params = asdict(p)
        expected_value, expected_rows = reference(params, cash, reverse)
        actual = module.Game(p, reverse).solve(0, cash)
        if (actual.vo, actual.path) != (expected_value, expected_rows):
            differences.append({"name": name, "parameters": params, "cash": cash, "reverse": reverse,
                                "actual_value": actual.vo, "reference_value": expected_value,
                                "actual": actual.path, "reference": expected_rows})
        ledger(params, cash, actual.vo, actual.path)
        counts["comparisons"] += 1
        counts["realized_episodes"] += len(actual.path)
        counts["cannot_operate_episodes"] += sum(row["status"] == "cannot_operate" for row in actual.path)
        counts["fresh_cases" if p.discount == 0 else "persistent_cases"] += 1
        counts["reversed_tie_cases"] += reverse
        if not name.startswith("sample") and p.T == 3 and p.discount == F(1, 2) and not reverse:
            reports.append({"name": name, "parameters": params, "opening_cash": cash,
                            "summary": module.summarize(actual), "path": actual.path})
    assert not differences, differences[:1]
    primary = module.Game(original).solve(0, F(5))
    assert all(z["learning"] == "shared" and z["profile"] == "verified_gate" and z["operator_action"] == "safeguard" and z["pre_attack"] == "none" for z in primary.path)
    assert [F(z["closing_cash"]) for z in primary.path] == [10, 15, 20, 25]
    assert primary.vo == F(45, 8)
    result = {"status": "PASS", "production_sha256": hashlib.sha256(target_path.read_bytes()).hexdigest(),
              "reference_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "counts": counts, "named_reports": reports,
              "limits": ["Exact finite-game consistency, not empirical validation or indefinite-proof certification.",
                         "Reproduces the declared dated selfish cold/learned warm objectives and equilibrium tie selection.",
                         "Cannot-operate freezes residual cash and records zero modeled harm; this is not a welfare verdict."]}
    output = Path(__file__).with_name("independent-game-check-results.json")
    output.write_text(json.dumps(result, indent=2, default=str)+"\n")
    print(json.dumps({"status": result["status"], "counts": counts, "output": str(output)}, indent=2))


if __name__ == "__main__":
    main()
