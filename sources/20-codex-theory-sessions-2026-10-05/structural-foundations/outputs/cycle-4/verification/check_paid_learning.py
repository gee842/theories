#!/usr/bin/env python3
"""Exact finite paid learning and adoption. Python standard library only.

Only a physical final register reaches the supplied Bayesian selector. Fixed
public cohort size, memory mode, and fees cannot encode the hidden observations.
The learned object is a latent regime, not its supplied likelihood family.
"""

from dataclasses import dataclass, replace
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import csv
import json


@dataclass(frozen=True)
class Config:
    name: str
    prior_high: F = F(1, 5)
    p_high: F = F(1, 2)
    p_low: F = F(0)
    probe_fee: F = F(2, 25)
    memory_cell_fee: F = F(1, 50)
    maintenance_fee: F = F(1)
    maintained_repair: F = F(6)
    substitute_repair: F = F(14)
    failure_loss: F = F(14)  # imputed consequence, never debited as cash
    cash: F = F(15)
    max_probes: int = 8


MODES = ("or", "count", "last", "erased", "or_lost")


def cells(n, mode):
    if n == 0 or mode == "erased":
        return 0
    if mode == "count":
        return n.bit_length()  # ceil(log2(n+1)) physical data bits
    return 1


def learning_cost(n, mode, c):
    holding_intervals = 1 if mode == "last" and n else n
    return n * c.probe_fee + holding_intervals * cells(n, mode) * c.memory_cell_fee


def final_register(observations, mode):
    # No observation history is passed to the selector. These are the actual
    # allowed finite-register update mechanisms used by the probe apparatus.
    register = 0 if mode in ("or", "count", "or_lost") else None
    for index, observed in enumerate(observations):
        if mode in ("or", "or_lost"):
            register = int(bool(register or observed))
        elif mode == "count":
            register += observed
        elif mode == "last":
            # Earlier reports are immediately discarded; only the final one
            # occupies the charged holding interval before selection.
            register = observed if index == len(observations) - 1 else None
        elif mode == "erased":
            register = None
        else:
            raise AssertionError(mode)
    if mode == "or_lost":
        register = None
    return register


def select_action(p_fault, cash, c):
    # Scores use actual available cash. If a fault response cannot be prepaid,
    # the declared objective incurs failure loss, rather than spending money
    # that does not exist. Ties favor no maintenance.
    absent_fault_consequence = c.substitute_repair if cash >= c.substitute_repair else c.failure_loss
    choices = [(p_fault * absent_fault_consequence, "no_maintenance")]
    if cash >= c.maintenance_fee:
        remaining = cash - c.maintenance_fee
        maintained_consequence = c.maintained_repair if remaining >= c.maintained_repair else c.failure_loss
        choices.append((c.maintenance_fee + p_fault * maintained_consequence, "maintain"))
    return min(choices, key=lambda x: (x[0], x[1] == "maintain"))[1]


def evaluate(c, n, mode):
    assert 0 <= n <= c.max_probes
    cost = learning_cost(n, mode, c)
    if cost > c.cash:
        return {"n": n, "mode": mode, "feasible": False, "learning_cost": cost}
    remaining = c.cash - cost
    regime_mass = {"H": c.prior_high, "L": 1 - c.prior_high}
    regime_probability = {"H": c.p_high, "L": c.p_low}
    joint = {}
    histories = 0
    for observations in product((0, 1), repeat=n):
        r = final_register(observations, mode)
        masses = joint.setdefault(r, {"H": F(0), "L": F(0)})
        for regime in ("H", "L"):
            p = regime_probability[regime]
            probability = regime_mass[regime]
            for y in observations:
                probability *= p if y else 1 - p
            masses[regime] += probability
        histories += 1
    assert sum(sum(v.values()) for v in joint.values()) == 1

    policy = []
    score = cash_expense = cost
    failure_probability = F(0)
    adoption_joint = {"H": F(0), "L": F(0)}
    min_cash_end = remaining
    branch_count = 0
    for r, masses in sorted(joint.items(), key=lambda x: str(x[0])):
        mass = sum(masses.values())
        if not mass:
            continue
        posterior = masses["H"] / mass
        fault_probability = posterior * c.p_high + (1 - posterior) * c.p_low
        action = select_action(fault_probability, remaining, c)
        policy.append({"register": r, "mass": mass, "posterior_high": posterior,
                       "predicted_fault_probability": fault_probability, "action": action})
        for regime in ("H", "L"):
            if action == "maintain":
                adoption_joint[regime] += masses[regime]
            for fault in (False, True):
                p = regime_probability[regime]
                probability = masses[regime] * (p if fault else 1 - p)
                if not probability:
                    continue
                branch_count += 1
                cash = remaining
                expense = F(0)
                if action == "maintain":
                    assert cash >= c.maintenance_fee
                    cash -= c.maintenance_fee
                    expense += c.maintenance_fee
                failure = False
                if fault:
                    bill = c.maintained_repair if action == "maintain" else c.substitute_repair
                    if cash >= bill:
                        cash -= bill
                        expense += bill
                    else:
                        failure = True
                assert cash >= 0 and cash + expense + cost == c.cash
                min_cash_end = min(min_cash_end, cash)
                cash_expense += probability * expense
                score += probability * (expense + (c.failure_loss if failure else 0))
                failure_probability += probability * failure
    adoption = {z: adoption_joint[z] / regime_mass[z] if regime_mass[z] else None for z in ("H", "L")}
    # Independent policy-score check from register-conditioned action values.
    independent = cost
    for row in policy:
        p, action = row["predicted_fault_probability"], row["action"]
        if action == "maintain":
            consequence = c.maintained_repair if remaining - c.maintenance_fee >= c.maintained_repair else c.failure_loss
            independent += row["mass"] * (c.maintenance_fee + p * consequence)
        else:
            consequence = c.substitute_repair if remaining >= c.substitute_repair else c.failure_loss
            independent += row["mass"] * p * consequence
    assert independent == score
    return {"n": n, "mode": mode, "feasible": True, "learning_cost": cost,
            "cash_after_learning": remaining, "memory_cells": cells(n, mode),
            "expected_score": score, "expected_cash_expense": cash_expense,
            "failure_probability": failure_probability, "adoption_by_regime": adoption,
            "policy": policy, "minimum_cash_after_duty": min_cash_end,
            "histories_enumerated": histories, "positive_branches_checked": branch_count}


def run_case(c):
    rows = [evaluate(c, n, mode) for n in range(c.max_probes + 1) for mode in MODES]
    winner = min((r for r in rows if r["feasible"]),
                 key=lambda r: (r["expected_score"], r["n"], r["memory_cells"], MODES.index(r["mode"])))
    return {"config": c.__dict__, "selected_protocol": winner,
            "all_admitted_fixed_cohort_protocols": rows}


def primitive(x):
    if isinstance(x, F):
        return {"exact": str(x), "decimal": float(x)}
    if isinstance(x, dict):
        return {str(k): primitive(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [primitive(v) for v in x]
    return x


def main():
    base = Config("base_funded_substitute")
    cases = [base,
             replace(base, name="limited_cash", cash=F(8)),
             replace(base, name="learning_eats_margin", cash=F(71, 10)),
             replace(base, name="no_hazard", p_high=F(0), p_low=F(0)),
             replace(base, name="high_memory_price", memory_cell_fee=F(3, 10)),
             replace(base, name="high_probe_price", probe_fee=F(2, 5)),
             replace(base, name="overlap_regimes", p_low=F(1, 10), maintenance_fee=F(2),
                     probe_fee=F(1, 200), memory_cell_fee=F(1, 200)),
             replace(base, name="deadline_one_probe", max_probes=1),
             replace(base, name="known_high_regime", prior_high=F(1)),
             replace(base, name="known_low_regime", prior_high=F(0)),
             replace(base, name="cheap_substitute", substitute_repair=F(7)),
             replace(base, name="free_retention", memory_cell_fee=F(0))]
    results = [run_case(c) for c in cases]
    indexed = {r["config"]["name"]: r for r in results}
    winner = indexed[base.name]["selected_protocol"]
    assert (winner["n"], winner["mode"], winner["expected_score"]) == (2, "or", F(23, 20))
    assert winner["adoption_by_regime"] == {"H": F(3, 4), "L": F(0)}
    assert winner["failure_probability"] == 0
    constrained = indexed["limited_cash"]["selected_protocol"]
    assert (constrained["n"], constrained["mode"], constrained["expected_score"]) == (2, "or", F(23, 20))
    assert constrained["failure_probability"] == F(1, 40)
    # Capacity comparison: unconditional maintenance is affordable before any
    # probes from cash8, and repairs every admitted fault at total bill<=7.
    assert F(8) >= base.maintenance_fee + base.maintained_repair
    margin = indexed["learning_eats_margin"]["selected_protocol"]
    assert (margin["n"], margin["expected_score"]) == (1, F(6, 5))
    margin_case = next(c for c in cases if c.name == "learning_eats_margin")
    paid_too_much = evaluate(margin_case, 2, "or")
    assert paid_too_much["cash_after_learning"] == F(69, 10)
    assert paid_too_much["cash_after_learning"] < base.maintenance_fee + base.maintained_repair
    assert paid_too_much["failure_probability"] == F(1, 10)

    closed_form_checks = 0
    for n in range(9):
        r = evaluate(base, n, "or")
        assert r["expected_score"] == F(4, 5) + F(3, 5) * F(1, 2) ** n + F(n, 10)
        assert r["adoption_by_regime"]["H"] == 1 - F(1, 2) ** n
        assert r["adoption_by_regime"]["L"] == 0
        zero = next(row for row in r["policy"] if row["register"] == 0)
        assert zero["posterior_high"] == F(1, 1 + 4 * 2**n)
        closed_form_checks += 1
        lost = evaluate(base, n, "or_lost")
        assert all(row["posterior_high"] == base.prior_high for row in lost["policy"])
        assert lost["expected_score"] == F(7, 5) + F(n, 10)

    for label in ("no_hazard", "high_memory_price", "high_probe_price",
                  "known_high_regime", "known_low_regime", "cheap_substitute"):
        assert indexed[label]["selected_protocol"]["n"] == 0
    assert indexed["no_hazard"]["selected_protocol"]["expected_score"] == 0
    assert indexed["deadline_one_probe"]["selected_protocol"]["expected_score"] == F(6, 5)

    overlap = next(c for c in cases if c.name == "overlap_regimes")
    or3, count3 = evaluate(overlap, 3, "or"), evaluate(overlap, 3, "count")
    assert or3["expected_score"] == F("2.46016")
    assert count3["expected_score"] == F("2.39188")
    assert next(x for x in count3["policy"] if x["register"] == 1)["action"] == "no_maintenance"
    assert next(x for x in count3["policy"] if x["register"] == 2)["action"] == "maintain"
    assert next(x for x in or3["policy"] if x["register"] == 1)["action"] == "maintain"

    all_rows = [r for case in results for r in case["all_admitted_fixed_cohort_protocols"] if r["feasible"]]
    out = {"status": "all assertions passed", "date": "2026-10-05", "cases": results,
           "protocols_evaluated": len(all_rows),
           "histories_enumerated": sum(r["histories_enumerated"] for r in all_rows),
           "positive_cash_branches_checked": sum(r["positive_branches_checked"] for r in all_rows),
           "base_closed_form_checks": closed_form_checks,
           "matched_cohort_overlap_comparison": {"or": or3, "count": count3},
           "forced_learning_consumes_guarantee": paid_too_much,
           "limits": ["Finite deployment episode; no endogenous recurrent financing claim",
                      "Regime likelihoods, prior, candidate menu, and score are supplied",
                      "Only final physical register reaches the actual selector",
                      "Fixed public cohorts exclude adaptive stopping and its communication channels",
                      "Failure loss is imputed; actual cash is never made negative",
                      "Expected-score optimum is not a robust-safety optimum"]}
    directory = Path(__file__).parent
    (directory / "paid-learning-results.json").write_text(json.dumps(primitive(out), indent=2) + "\n")
    with (directory / "paid-learning-frontier.csv").open("w", newline="") as f:
        cols = ("case", "n", "mode", "learning_cost", "score", "cash_expense", "failure_probability",
                "adoption_high", "adoption_low")
        writer = csv.DictWriter(f, fieldnames=cols)
        writer.writeheader()
        for result in results:
            for r in result["all_admitted_fixed_cohort_protocols"]:
                if r["feasible"]:
                    writer.writerow({"case": result["config"]["name"], "n": r["n"], "mode": r["mode"],
                                     "learning_cost": float(r["learning_cost"]), "score": float(r["expected_score"]),
                                     "cash_expense": float(r["expected_cash_expense"]),
                                     "failure_probability": float(r["failure_probability"]),
                                     "adoption_high": None if r["adoption_by_regime"]["H"] is None else float(r["adoption_by_regime"]["H"]),
                                     "adoption_low": None if r["adoption_by_regime"]["L"] is None else float(r["adoption_by_regime"]["L"])})
    print(json.dumps({"status": out["status"], "protocols_evaluated": out["protocols_evaluated"],
                      "histories_enumerated": out["histories_enumerated"],
                      "cash_branches_checked": out["positive_cash_branches_checked"],
                      "selected": [{"case": r["config"]["name"], "n": r["selected_protocol"]["n"],
                                    "memory": r["selected_protocol"]["mode"],
                                    "score": float(r["selected_protocol"]["expected_score"]),
                                    "failure_probability": float(r["selected_protocol"]["failure_probability"])} for r in results]}, indent=2))


if __name__ == "__main__":
    main()
