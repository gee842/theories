#!/usr/bin/env python3
"""Finite paid revision: exact Bayes DP, physical memory, and policy enumeration."""

from dataclasses import dataclass, replace, asdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import lcm
from pathlib import Path
import csv
import json


@dataclass(frozen=True)
class Config:
    reserve: int = 14
    deadline: int = 4
    prior_b: F = F(1, 2)
    signal_a: F = F(1, 4)
    signal_b: F = F(3, 4)
    probe_fee: int = 1
    memory_fee: int = 1
    revision_fee: int = 2
    revision_time: int = 1
    child_requirement: int = 6
    max_probes: int = 3

    @property
    def observation_fee(self):
        return self.probe_fee + self.memory_fee


def posterior(c, n, k):
    wb = c.prior_b * c.signal_b**k * (1-c.signal_b)**(n-k)
    wa = (1-c.prior_b) * c.signal_a**k * (1-c.signal_a)**(n-k)
    return wb / (wa+wb) if wa+wb else None


def signal_probability(c, theta, bits):
    p = c.signal_b if theta == "B" else c.signal_a
    prior = c.prior_b if theta == "B" else 1-c.prior_b
    return prior * p**sum(bits) * (1-p)**(len(bits)-sum(bits))


def terminal(c, theta, recommendation, cash, time):
    """No fallback after an infeasible B recommendation."""
    if recommendation == "B":
        if time + c.revision_time > c.deadline:
            return {"success": False, "status": "revision_misses_deadline",
                    "committed_rule": None, "child_cash": None,
                    "untransferred_cash": cash, "revision_expense": 0}
        if cash < c.revision_fee:
            return {"success": False, "status": "revision_bill_unpayable",
                    "committed_rule": None, "child_cash": None,
                    "untransferred_cash": cash, "revision_expense": 0}
        cash -= c.revision_fee
        time += c.revision_time
        expense = c.revision_fee
    else:
        expense = 0
    if time > c.deadline:
        return {"success": False, "status": "launch_misses_deadline",
                "committed_rule": recommendation, "child_cash": None,
                "untransferred_cash": cash, "revision_expense": expense}
    if cash < c.child_requirement:
        return {"success": False, "status": "child_underfunded",
                "committed_rule": recommendation, "child_cash": None,
                "untransferred_cash": cash, "revision_expense": expense}
    return {"success": recommendation == theta,
            "status": "success" if recommendation == theta else "wrong_rule",
            "committed_rule": recommendation, "child_cash": cash,
            "untransferred_cash": 0, "revision_expense": expense}


def dynamic_program(c):
    policy = {}
    certificate = {}

    @lru_cache(None)
    def value(n, k, cash):
        p = posterior(c, n, k)
        if p is None:
            return F(0)
        options = {}
        if n <= c.deadline and cash >= c.child_requirement:
            options["A"] = 1-p
        if (n+c.revision_time <= c.deadline and
                cash >= c.revision_fee+c.child_requirement):
            options["B"] = p
        if (n < c.max_probes and n+1 <= c.deadline and
                cash >= c.observation_fee):
            prob1 = p*c.signal_b + (1-p)*c.signal_a
            total = F(0)
            for bit, prob in ((0, 1-prob1), (1, prob1)):
                if prob:
                    total += prob*value(n+1, k+bit, cash-c.observation_fee)
            options["probe"] = total
        options["abort"] = F(0)
        # Stop before probing when values tie; A before B on posterior ties.
        selected = max(options, key=lambda a: options[a])
        policy[n, k, cash] = selected
        certificate[n, k, cash] = {
            "posterior_B": p, "actions": options,
            "chosen": selected, "value": options[selected]}
        return options[selected]

    optimum = value(0, 0, c.reserve)
    return optimum, policy, certificate


def rollout(c, theta, bits, mode, dp_policy=None, table=None):
    n = k = 0
    cash = c.reserve
    ledger = []
    if mode in ("majority", "erased", "last"):
        # Fixed cohort, prices and timing; no payload-dependent public channel.
        register = 0 if mode == "majority" else None
        for bit in bits:
            if n+1 > c.deadline or cash < c.observation_fee:
                return {"success": False, "recommendation": None,
                        "status": "cohort_unfinished", "observations": n,
                        "probe_and_memory_expense": c.reserve-cash,
                        "revision_expense": 0, "child_cash": None,
                        "untransferred_cash": cash, "payment_ledger": ledger}
            cash -= c.observation_fee
            n += 1
            if mode == "majority":
                register += bit
            elif mode == "last":
                register = bit
            # Erased mode destroys each payload before the next decision.
            ledger.append({"observation": n, "expense": c.observation_fee,
                           "cash": cash, "physical_register": register})
        recommendation = ("B" if register >= 2 else "A") if mode == "majority" else (
            "B" if register == 1 else "A") if mode == "last" else "A"
    elif mode == "fixed":
        recommendation = "A"
    elif mode == "oracle":
        recommendation = theta
    else:
        while True:
            if mode == "dp":
                decision = dp_policy[n, k, cash]
            elif mode == "table":
                decision = table[n, k]
            else:
                raise AssertionError(mode)
            if decision in ("A", "B"):
                recommendation = decision
                break
            if (decision == "abort" or n == c.max_probes or
                    n+1 > c.deadline or cash < c.observation_fee):
                return {"success": False, "recommendation": None,
                        "status": "abort", "observations": n,
                        "probe_and_memory_expense": c.reserve-cash,
                        "revision_expense": 0, "child_cash": None,
                        "untransferred_cash": cash, "payment_ledger": ledger}
            cash -= c.observation_fee
            k += bits[n]
            n += 1
            ledger.append({"observation": n, "expense": c.observation_fee,
                           "cash": cash, "physical_register": k})
    outcome = terminal(c, theta, recommendation, cash, n)
    outcome.update({"recommendation": recommendation, "observations": n,
                    "probe_and_memory_expense": c.reserve-cash,
                    "payment_ledger": ledger})
    return outcome


def distribution(c, mode, policy=None):
    success = correct = complete = adopted_correct = F(0)
    expected_n = expense = F(0)
    statuses = {}
    cases = []
    for theta, bits in product(("A", "B"), product((0, 1), repeat=c.max_probes)):
        prob = signal_probability(c, theta, bits)
        if not prob:
            continue
        r = rollout(c, theta, bits, mode, dp_policy=policy)
        correct += prob*(r["recommendation"] == theta)
        complete += prob*(r["recommendation"] is not None)
        adopted_correct += prob*(r.get("committed_rule") == theta)
        success += prob*r["success"]
        expected_n += prob*r["observations"]
        paid = r["probe_and_memory_expense"]+r["revision_expense"]
        expense += prob*paid
        assert paid + (r["child_cash"] or 0) + r["untransferred_cash"] == c.reserve
        statuses[r["status"]] = statuses.get(r["status"], F(0))+prob
        cases.append({"regime": theta, "potential_probe_bits": bits,
                      "probability": prob, **r})
    assert sum(statuses.values()) == 1
    return {"probability_recommendation_completed": complete,
            "probability_recommendation_correct": correct,
            "conditional_recommendation_accuracy": correct/complete if complete else None,
            "probability_committed_rule_correct": adopted_correct,
            "probability_usable_successor": success,
            "expected_probe_count": expected_n, "expected_actual_expense": expense,
            "outcome_probabilities": statuses, "branches": cases}


def exhaustive_policy_check(c):
    """Every deterministic table on the ten (n,count) states; no oracle."""
    internal = [(n, k) for n in range(3) for k in range(n+1)]
    leaves = [(3, k) for k in range(4)]
    weighted = [(theta, bits, signal_probability(c, theta, bits))
                for theta, bits in product(("A", "B"), product((0, 1), repeat=3))]
    denominator = lcm(*(p.denominator for _, _, p in weighted))
    weighted = [(theta, bits, int(p*denominator)) for theta, bits, p in weighted]
    best = -1
    count = 0
    for early, final in product(product(("A", "B", "probe"), repeat=6),
                                product(("A", "B"), repeat=4)):
        table = dict(zip(internal+leaves, early+final))
        score = sum(weight*rollout(c, theta, bits, "table", table=table)["success"]
                    for theta, bits, weight in weighted)
        best = max(best, score)
        count += 1
    assert count == 11664
    return F(best, denominator), count, count*len(weighted)


def primitive(x):
    if isinstance(x, F):
        return {"exact": str(x), "decimal": float(x)}
    if isinstance(x, dict):
        return {str(k): primitive(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [primitive(v) for v in x]
    return x


def main():
    base = Config()
    cases = [
        ("ample_budget", base),
        ("revision_bridge_consumed", replace(base, reserve=12)),
        ("revision_time_consumed", replace(base, deadline=3)),
        ("one_probe_affordable", replace(base, reserve=10)),
        ("oracle_affordable_learning_not_useful", replace(base, reserve=8)),
        ("unchanged_regime", replace(base, reserve=6, prior_b=F(0))),
        ("perfectly_separating_probe", replace(base, reserve=10,
             signal_a=F(0), signal_b=F(1))),
        ("free_observation_control", replace(base, reserve=8, probe_fee=0, memory_fee=0)),
    ]
    expected = {
        "ample_budget": (F(27,32), F(27,32)),
        "revision_bridge_consumed": (F(27,64), F(3,4)),
        "revision_time_consumed": (F(27,64), F(3,4)),
        "one_probe_affordable": (F(0), F(3,4)),
        "oracle_affordable_learning_not_useful": (F(0), F(1,2)),
        "unchanged_regime": (F(0), F(1)),
        "perfectly_separating_probe": (F(0), F(1)),
        "free_observation_control": (F(27,32), F(27,32)),
    }
    results = []
    policy_checks = rollouts = 0
    for name, c in cases:
        optimum, policy, certificate = dynamic_program(c)
        modes = {mode: distribution(c, mode, policy)
                 for mode in ("majority", "dp", "fixed", "oracle", "erased", "last")}
        assert modes["dp"]["probability_usable_successor"] == optimum
        assert (modes["majority"]["probability_usable_successor"], optimum) == expected[name]
        assert modes["oracle"]["probability_usable_successor"] >= optimum
        assert optimum >= modes["fixed"]["probability_usable_successor"]
        if name in ("ample_budget", "revision_bridge_consumed",
                    "revision_time_consumed", "oracle_affordable_learning_not_useful"):
            enumerated, count, trials = exhaustive_policy_check(c)
            assert enumerated == optimum
            policy_checks += count
            rollouts += trials
        results.append({"name": name, "config": asdict(c), "modes": modes,
                        "dp_optimum": optimum, "dp_certificate": [
                            {"probes": n, "count": k, "cash": cash, **info}
                            for (n,k,cash), info in sorted(certificate.items())]})
    assert results[0]["modes"]["dp"]["expected_probe_count"] == F(19,8)
    assert results[0]["modes"]["dp"]["expected_actual_expense"] == F(23,4)
    assert results[1]["modes"]["dp"]["expected_probe_count"] == 1
    frontier = []
    for reserve, deadline in product(range(6,17), range(5)):
        c = replace(base, reserve=reserve, deadline=deadline)
        optimum, policy, certificate = dynamic_program(c)
        actual = distribution(c, "majority")
        oracle = distribution(c, "oracle")
        fixed = distribution(c, "fixed")
        assert oracle["probability_usable_successor"] >= optimum >= fixed["probability_usable_successor"]
        assert optimum >= actual["probability_usable_successor"]
        if deadline >= 3:
            assert actual["probability_recommendation_correct"] == F(27,32)
        formula = (F(27,32) if reserve >= 14 and deadline >= 4 else
                   F(3,4) if reserve >= 10 and deadline >= 2 else F(1,2))
        assert optimum == formula
        frontier.append({"reserve": reserve, "deadline": deadline,
                         "actual_majority_success": str(actual["probability_usable_successor"]),
                         "best_paid_success": str(optimum),
                         "free_information_bound": str(oracle["probability_usable_successor"]),
                         "fixed_A_success": str(fixed["probability_usable_successor"])})
    directory = Path(__file__).parent
    out = {"status": "all assertions passed", "selected_cases": results,
           "frontier_rows": len(frontier), "exhaustive_policy_tables": policy_checks,
           "exhaustive_potential_history_rollouts": rollouts,
           "limits": ["Finite successor delivery with supplied two-regime duty interface",
                      "Known prior/likelihood family, conditionally independent paid probes",
                      "Count register is the only report-dependent controller payload",
                      "No interim income or endogenous recurrence financing",
                      "Oracle information is deliberately free, but revision remains paid/timed",
                      "Erased/last controls use a fixed cohort, so clock/cash cannot encode reports"]}
    (directory/"paid-revision-results.json").write_text(json.dumps(primitive(out),indent=2)+"\n")
    with (directory/"paid-revision-frontier.csv").open("w",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=list(frontier[0]))
        writer.writeheader();writer.writerows(frontier)
    print(json.dumps({"status":out["status"],"frontier_rows":len(frontier),
         "exhaustive_policy_tables":policy_checks,"potential_history_rollouts":rollouts,
         "selected":[{"case":r["name"],"actual":str(r["modes"]["majority"]["probability_usable_successor"]),
                     "paid_optimum":str(r["dp_optimum"]),
                     "oracle":str(r["modes"]["oracle"]["probability_usable_successor"])}
                     for r in results]},indent=2))


if __name__ == "__main__":
    main()
