#!/usr/bin/env python3
"""Paid parent evaluation and a real handoff reserve, exact finite checking.

Reimplements the declared cycle-4 plant and actual one/two-cycle planners.
Infinite descendant behavior is decided on their finite functional graphs,
not extrapolated from a trace. Evaluator labels/addresses are distinct from
the physical channels that may or may not be transferred at parental retirement.
"""

from collections import defaultdict, deque
from dataclasses import dataclass, replace
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import csv
import json


CAP = 240
STATES = tuple(product(range(CAP + 1), range(9)))


def cycle(cash, old, new, hazard=True):
    purchase = 30 * max(new - old, 0)
    if cash < purchase:
        return None
    cash -= purchase
    if not hazard:
        for _ in range(8):
            cash = min(CAP, cash + 32 - 2 * new)
        return cash
    if new == 0:
        return None
    duration = (8 + new - 1) // new + 2
    if duration > 6:
        return None
    expense = 24 + (8 + 2 * new) * duration
    if cash < expense:
        return None
    cash -= expense
    for _ in range(8 - duration):
        cash = min(CAP, cash + 32 - 2 * new)
    return cash


@lru_cache(None)
def plan(cash, old, depth, hazard=True):
    if depth == 0:
        return cash, ()
    best = None
    menu = range(1, 9) if hazard else range(9)
    for new in menu:
        target = cycle(cash, old, new, hazard)
        if target is None:
            continue
        tail = plan(target, new, depth - 1, hazard)
        if tail is None:
            continue
        candidate = tail[0], (new,) + tail[1]
        if best is None or candidate[0] > best[0] or (candidate[0] == best[0] and candidate[1] < best[1]):
            best = candidate
    return best


@lru_cache(None)
def actual_next(cash, old, rule, hazard=True):
    horizon = 1 if rule == "S" else 2
    for depth in range(horizon, 0, -1):
        p = plan(cash, old, depth, hazard)
        if p is not None:
            new = p[1][0]
            return cycle(cash, old, new, hazard), new
    return None


def infinite_actual(rule, hazard=True):
    successors = {s: actual_next(*s, rule, hazard) for s in STATES}
    parents = defaultdict(list)
    lost = {s for s, t in successors.items() if t is None}
    queue = deque(lost)
    ranks = {s: 1 for s in lost}
    for s, t in successors.items():
        if t is not None:
            parents[t].append(s)
    while queue:
        bad = queue.popleft()
        for q in parents[bad]:
            if q not in lost:
                lost.add(q)
                ranks[q] = ranks[bad] + 1
                queue.append(q)
    win = set(STATES) - lost
    assert all(successors[q] in win for q in win)
    assert all(successors[q] is None or ranks[successors[q]] < ranks[q] for q in lost)
    return win, successors, ranks


@lru_cache(None)
def parent_profile(rule, checkpoint, hazard=True):
    state = (240, 0)
    trace = []
    for t in range(1, checkpoint + 1):
        nxt = actual_next(*state, rule, hazard)
        if nxt is None:
            return {"cash": state[0], "channels": state[1], "completed": False,
                    "failure_cycle": t, "trace": trace}
        trace.append({"cycle": t, "cash_before": state[0], "channels_before": state[1],
                      "cash_after": nxt[0], "channels_after": nxt[1]})
        state = nxt
    return {"cash": state[0], "channels": state[1], "completed": True, "trace": trace}


@dataclass(frozen=True)
class Evaluation:
    name: str
    checkpoint: int = 1
    scoring: str = "cash_rank"
    reserve: int = 240
    transfer: str = "program_only"  # donor_bundle, existing_four
    retain_address: bool = True
    waiting_per_cycle: int = 10
    audit_fee: int = 2
    address_retention: int = 1
    copy_fee: int = 2
    bundle_fee: int = 3
    hazard: bool = True


def observe_and_select(address_rules, c):
    profiles = {address: parent_profile(rule, c.checkpoint, c.hazard)
                for address, rule in address_rules.items()}
    if c.scoring == "cash_rank":
        payload = {a: p["cash"] for a, p in profiles.items()}
        chosen = max(("A", "B"), key=lambda a: (payload[a], a == "A"))
    elif c.scoring == "pass_rank":
        payload = {a: p["completed"] for a, p in profiles.items()}
        chosen = max(("A", "B"), key=lambda a: (payload[a], a == "A"))
    elif c.scoring == "calibrated":
        # Uses only observed cash/status and the supplied profile table. It
        # never consults address_rules to identify which letter contains L.
        payload = {a: (p["cash"], p["completed"]) for a, p in profiles.items()}
        reference = parent_profile("L", c.checkpoint, c.hazard)
        matches = [a for a in ("A", "B") if payload[a] == (reference["cash"], reference["completed"])]
        chosen = matches[0] if len(matches) == 1 else "A"
    else:
        raise AssertionError(c.scoring)
    # The copier starts after the audit controller has retired. Its sole
    # payload input is this paid physical address register, not past audit data.
    copied_register = chosen if c.retain_address else None
    copied_address = copied_register if copied_register is not None else "A"
    return profiles, payload, chosen, copied_register, copied_address


def evaluate(c, wins):
    costs = [("waiting", c.waiting_per_cycle)] * c.checkpoint
    costs += [("audit", c.audit_fee)]
    if c.retain_address:
        costs += [("address_memory", c.address_retention)]
    costs += [("copy", c.copy_fee)]
    if c.transfer == "donor_bundle":
        costs += [("one_to_one_asset_transfer", c.bundle_fee)]
    cash = c.reserve
    ledger = []
    for phase, fee in costs:
        if cash < fee:
            return {"config": c.__dict__, "affordable": False, "failed_payment": phase,
                    "spent_before_failure": c.reserve - cash, "handoff_success": F(0)}
        cash -= fee
        ledger.append({"phase": phase, "expense": fee, "remaining": cash})
    spill = max(0, cash - CAP)
    child_cash = cash - spill
    assert child_cash + spill + sum(f for _, f in costs) == c.reserve
    rows = []
    for rules in ({"A": "S", "B": "L"}, {"A": "L", "B": "S"}):
        profiles, payload, selected, register, address = observe_and_select(rules, c)
        rule = rules[address]
        channels = (profiles[address]["channels"] if c.transfer == "donor_bundle"
                    else 4 if c.transfer == "existing_four" else 0)
        success = (child_cash, channels) in wins[(rule, c.hazard)]
        rows.append({"address_rules": rules, "observed_payload": payload,
                     "audit_selection": selected, "register_at_copy": register,
                     "copied_address": address, "copied_rule": rule,
                     "donor_channels_before": profiles[address]["channels"],
                     "donor_channels_after": 0 if c.transfer == "donor_bundle" else profiles[address]["channels"],
                     "child_channels": channels, "child_cash": child_cash,
                     "indefinite_actual_child_success": success})
    return {"config": c.__dict__, "affordable": True, "total_evaluator_expense": sum(f for _, f in costs),
            "cash_spill_at_child_cap": spill, "payment_ledger": ledger,
            "probability_copy_L": F(sum(r["copied_rule"] == "L" for r in rows), 2),
            "handoff_success": F(sum(r["indefinite_actual_child_success"] for r in rows), 2),
            "guarantees_child_continuation_for_both_assignments": all(r["indefinite_actual_child_success"] for r in rows),
            "assignment_cases": rows}


def primitive(x):
    if isinstance(x, F):
        return {"exact": str(x), "decimal": float(x)}
    if isinstance(x, dict):
        return {str(k): primitive(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [primitive(v) for v in x]
    return x


def main():
    wins = {}
    graphs = {}
    for rule, hazard in product(("S", "L"), (False, True)):
        win, successors, ranks = infinite_actual(rule, hazard)
        wins[rule, hazard] = win
        graphs[rule, hazard] = successors, ranks
    for b in range(241):
        assert ((b, 0) in wins["L", True]) == (b >= 208)
        assert (b, 0) not in wins["S", True]
        assert (b, 2) not in wins["S", True]
        for rule in ("S", "L"):
            assert ((b, 4) in wins[rule, True]) == (b >= 88)
            assert (b, 0) in wins[rule, False]

    profiles = {rule: [parent_profile(rule, t) for t in range(1, 5)] for rule in ("S", "L")}
    assert [p["cash"] for p in profiles["S"]] == [140, 100, 60, 60]
    assert [p["cash"] for p in profiles["L"]] == [128, 136, 144, 152]
    assert not profiles["S"][3]["completed"]

    configs = [
        Evaluation("early_cash_proxy"),
        Evaluation("delayed_cash_rank", checkpoint=2),
        Evaluation("calibrated_early", scoring="calibrated"),
        Evaluation("coarse_early_pass", scoring="pass_rank"),
        Evaluation("coarse_late_duty", scoring="pass_rank", checkpoint=4, reserve=270),
        Evaluation("lost_delayed_address", checkpoint=2, retain_address=False),
        Evaluation("delay_consumes_bridge", checkpoint=2, reserve=230),
        Evaluation("early_same_reserve", scoring="calibrated", reserve=230),
        Evaluation("late_program_only", checkpoint=2, reserve=120),
        Evaluation("late_donor_bundle", checkpoint=2, reserve=120, transfer="donor_bundle"),
        Evaluation("warm_early_unnecessary_evaluation", reserve=103, transfer="existing_four"),
        Evaluation("warm_delayed_evaluation_harms", reserve=103, checkpoint=2, transfer="existing_four"),
        Evaluation("wait_bill_unaffordable", reserve=19, checkpoint=2),
        Evaluation("no_hazard_early", reserve=15, hazard=False),
        Evaluation("no_hazard_delayed", reserve=25, checkpoint=2, hazard=False),
    ]
    results = [evaluate(c, wins) for c in configs]
    expected = {"early_cash_proxy": F(0), "delayed_cash_rank": F(1), "calibrated_early": F(1),
                "coarse_early_pass": F(1, 2), "coarse_late_duty": F(1), "lost_delayed_address": F(1, 2),
                "delay_consumes_bridge": F(0), "early_same_reserve": F(1), "late_program_only": F(0),
                "late_donor_bundle": F(1), "warm_early_unnecessary_evaluation": F(1),
                "warm_delayed_evaluation_harms": F(0), "wait_bill_unaffordable": F(0),
                "no_hazard_early": F(1), "no_hazard_delayed": F(1)}
    for r in results:
        assert r["handoff_success"] == expected[r["config"]["name"]]

    frontier = []
    for checkpoint, scoring, transfer, retain in product(range(1, 5),
            ("cash_rank", "pass_rank", "calibrated"),
            ("program_only", "donor_bundle", "existing_four"), (False, True)):
        minimum = None
        for reserve in range(301):
            c = Evaluation("frontier", checkpoint, scoring, reserve, transfer, retain)
            result = evaluate(c, wins)
            if result.get("guarantees_child_continuation_for_both_assignments", False):
                minimum = reserve
                break
        frontier.append({"checkpoint": checkpoint, "scoring": scoring, "transfer": transfer,
                         "retain_address": retain, "minimum_reserve_for_sure_actual_success": minimum})
    def threshold(checkpoint, scoring, transfer="program_only", retain=True):
        return next(r["minimum_reserve_for_sure_actual_success"] for r in frontier
                    if (r["checkpoint"], r["scoring"], r["transfer"], r["retain_address"])
                    == (checkpoint, scoring, transfer, retain))
    assert threshold(1, "calibrated") == 223
    assert threshold(2, "cash_rank") == 233
    assert threshold(2, "cash_rank", "donor_bundle") == 116
    assert threshold(1, "calibrated", "donor_bundle") == 106
    assert threshold(1, "cash_rank", "existing_four") == 103
    assert threshold(2, "cash_rank", "existing_four") == 113

    directory = Path(__file__).parent
    certificates = {}
    for rule, hazard in product(("S", "L"), (False, True)):
        successors, ranks = graphs[rule, hazard]
        certificates[f"{rule}-hazard-{hazard}"] = {
            "winning_state_count": len(wins[rule, hazard]),
            "winning_invariant": [{"cash": s[0], "channels": s[1],
                                   "successor": successors[s]} for s in sorted(wins[rule, hazard])],
            "losing_rank": [{"cash": s[0], "channels": s[1], "rank": rank,
                             "successor": successors[s]} for s, rank in sorted(ranks.items())]}
    (directory / "paid-evaluation-controller-certificates.json").write_text(json.dumps(certificates, indent=2) + "\n")
    out = {"status": "all assertions passed", "date": "2026-10-05", "source_trial_capital": 480,
           "actual_controller_graphs": 4, "states_per_graph": len(STATES), "frontier_rows": len(frontier),
           "parent_profiles": profiles, "selected_cases": results, "frontier": frontier,
           "limits": ["Deterministic periodic faults; exact supplied plant and rule family",
                      "Two candidate trial plants each receive endowed capital240",
                      "Basic source and child plant bodies are endowed; their construction is outside this module",
                      "Evaluator/child reserve is separate; parental remainingcash is inaccessible",
                      "Donor assets move to one child and donor retires; no free copying of hardware",
                      "Hidden candidate assignment is uniform only for reported probabilities",
                      "No population-frequency or endogenous evaluator-financing theorem is claimed"]}
    (directory / "paid-evaluation-results.json").write_text(json.dumps(primitive(out), indent=2) + "\n")
    with (directory / "paid-evaluation-frontier.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(frontier[0]))
        writer.writeheader(); writer.writerows(frontier)
    print(json.dumps({"status": out["status"], "states_checked": len(STATES) * 4,
                      "frontier_rows": len(frontier), "selected": [
                          {"case": r["config"]["name"], "handoff_success": str(r["handoff_success"]),
                           "copy_L": str(r.get("probability_copy_L", "unfunded"))} for r in results]}, indent=2))


if __name__ == "__main__":
    main()
