#!/usr/bin/env python3
"""Exact infinite safety games for a declared recurrent paid-repair model.

The finite deadline makes every uncompleted fault a safety violation. The
greatest fixed point quantifies over ALL admitted observable event histories,
not sampled paths or stationary disturbance schedules. Python stdlib only.
"""

from collections import deque, defaultdict
from dataclasses import dataclass, asdict, replace
from itertools import product
from pathlib import Path
import csv
import json


@dataclass(frozen=True)
class Config:
    name: str
    cap: int = 24
    gross: int = 5
    operating: int = 1
    maintenance: int = 1
    rebuild_cost: int = 2
    rebuild_delay: int = 2
    diagnostic: int = 1
    authority: int = 1
    implementation: int = 1
    spacing: int = 5
    deadline: int = 5
    hazard: bool = True
    full_information: bool = False
    fixed_fault: bool = False
    authority_supplied: bool = False
    alternative_premium: int | None = None

    def __post_init__(self):
        for value in (self.cap, self.gross, self.operating, self.maintenance,
                      self.rebuild_cost, self.rebuild_delay, self.diagnostic,
                      self.authority, self.implementation, self.spacing):
            assert isinstance(value, int) and value >= 0
        assert isinstance(self.deadline, int) and self.deadline >= 1
        assert self.operating >= 1
        assert self.alternative_premium is None or (
            isinstance(self.alternative_premium, int) and self.alternative_premium >= 0)


@dataclass(frozen=True, order=True)
class State:
    cash: int
    clock: int
    phase: str = "healthy"
    age: int = 0
    apparatus: int = 0  # -1 absent, 0 ready, k>0 build slots remaining
    remembered: bool = False  # symmetry quotient of a retained known fixed bit


def first_phase(c, remembered=False):
    informed = c.full_information or (c.fixed_fault and remembered)
    return "authorize" if informed and not c.authority_supplied else (
        "execute" if informed else "diagnose")


def after_diagnosis(c):
    return "execute" if c.authority_supplied else "authorize"


def apparatus_progress(a):
    return max(0, a - 1) if a > 0 else a


def event_states(q, c):
    if q.phase != "healthy":
        return [("existing_fault", q)]
    events = [("quiet", q)]
    if c.hazard and q.clock >= c.spacing:
        events.append(("fault_onset", replace(q, clock=0, phase=first_phase(c, q.remembered), age=0)))
    return events


def settle(q, c, *, phase, apparatus, fee, gross=0):
    cost = c.operating + fee
    working_cash = q.cash + gross  # receipts precede this slot's expense
    if working_cash < cost:
        return None, {"reason": "unaffordable", "cash": q.cash, "gross": gross, "cost": cost}
    remainder = working_cash - cost
    spill = max(0, remainder - c.cap)
    cash = remainder - spill
    age = 0 if phase == "healthy" else q.age + 1
    flow = {"cash_before": q.cash, "gross": gross, "operating": c.operating,
            "fee": fee, "spill": spill, "cash_after": cash}
    assert cash + cost + spill == q.cash + gross
    if phase != "healthy" and age >= c.deadline:
        return None, {**flow, "reason": "missed_deadline", "age_after": age}
    remembered = q.remembered or (c.fixed_fault and q.phase == "diagnose" and phase != "diagnose")
    return State(cash, min(c.spacing, q.clock + 1), phase, age, apparatus, remembered), flow


def controller_actions(q, c, policy_class):
    """Actions follow the observed fault/quiet event; hidden diagnosis is not an oracle.

    The two possible diagnostic reports have isomorphic continuation games.
    apply_reported is the concrete rule apply(report), AFTER a paid diagnosis
    (or the full-information control). Incorrect guesses are terminal failures
    and cannot improve a sure-winning controller, so are omitted.
    """
    moves = []

    def add(label, phase, app, fee, gross=0):
        target, flow = settle(q, c, phase=phase, apparatus=app, fee=fee, gross=gross)
        moves.append((label, target, flow))

    a = q.apparatus
    if q.phase == "healthy":
        if policy_class == "on_demand":
            add("suspend_or_remain_absent", "healthy", -1, 0, c.gross)
        elif a == 0:
            add("standby", "healthy", 0, c.maintenance, c.gross)
            if policy_class == "all":
                add("suspend", "healthy", -1, 0, c.gross)
        elif a == -1:
            if policy_class == "all":
                add("remain_absent", "healthy", -1, 0, c.gross)
            next_a = max(0, c.rebuild_delay - 1)
            fee = c.rebuild_cost + (c.maintenance if next_a == 0 else 0)
            add("start_proactive_rebuild", "healthy", next_a, fee, c.gross)
        else:
            next_a = apparatus_progress(a)
            add("continue_rebuild", "healthy", next_a,
                c.maintenance if next_a == 0 else 0, c.gross)
            if policy_class == "all":
                add("cancel_rebuild", "healthy", -1, 0, c.gross)
    elif q.phase == "diagnose":
        if a == 0:
            add("inspect", after_diagnosis(c), 0, c.diagnostic)
        elif a == -1 and c.rebuild_delay == 0:
            add("rebuild_and_inspect", after_diagnosis(c), 0,
                c.rebuild_cost + c.diagnostic)
        elif a == -1:
            add("start_fault_rebuild", "diagnose", c.rebuild_delay - 1, c.rebuild_cost)
        else:
            add("continue_fault_rebuild", "diagnose", apparatus_progress(a), 0)
        if c.alternative_premium is not None:
            add("inspect_via_alternative", after_diagnosis(c), apparatus_progress(a),
                c.diagnostic + c.alternative_premium)
    elif q.phase == "authorize":
        add("authorize", "execute", apparatus_progress(a), c.authority)
    elif q.phase == "execute":
        if policy_class != "on_demand":
            add("apply_reported_keep", "healthy", apparatus_progress(a), c.implementation)
        if policy_class != "standby":
            add("apply_reported_suspend", "healthy", -1, c.implementation)
    else:
        raise AssertionError(q)
    assert moves
    return moves


def graph(c, policy_class):
    roots = [State(b, c.spacing, apparatus=a, remembered=remembered)
             for b in range(c.cap + 1) for a in (0, -1)
             for remembered in ((False, True) if c.fixed_fault else (False,))]
    seen = set(roots)
    pending = deque(roots)
    branches = {}
    edge_count = 0
    while pending:
        q = pending.popleft()
        result = []
        for event, intermediate in event_states(q, c):
            actions = controller_actions(intermediate, c, policy_class)
            edge_count += len(actions)
            result.append((event, actions))
            for _, target, _ in actions:
                if target is not None and target not in seen:
                    seen.add(target)
                    pending.append(target)
        branches[q] = result
    return roots, seen, branches, edge_count


def solve(c, policy_class="all", export=False):
    roots, states, branches, edge_count = graph(c, policy_class)
    # An environment branch is safe iff at least one control successor survives.
    counts = {}
    reverse = defaultdict(list)
    losing = set()
    queue = deque()
    losing_rank = {}
    for q, events in branches.items():
        for event, actions in events:
            key = (q, event)
            targets = {target for _, target, _ in actions if target is not None}
            counts[key] = len(targets)
            for target in targets:
                reverse[target].append(key)
            if not targets and q not in losing:
                losing.add(q)
                losing_rank[q] = 1
                queue.append(q)
    while queue:
        bad = queue.popleft()
        for q, event in reverse[bad]:
            key = (q, event)
            counts[key] -= 1
            if counts[key] == 0 and q not in losing:
                losing.add(q)
                losing_rank[q] = 1 + max(
                    [losing_rank.get(t, 0) for _, t, _ in dict(branches[q])[event]
                     if t is not None] or [0])
                queue.append(q)
    winning = states - losing

    # Check the greatest-fixed-point equation on EVERY graph state.
    for q in states:
        pred = all(any(t in winning for _, t, _ in acts if t is not None)
                   for _, acts in branches[q])
        assert (q in winning) == pred

    minima = {}
    for label, a in (("ready", 0), ("cold", -1)):
        credits = [b for b in range(c.cap + 1) if State(b, c.spacing, apparatus=a) in winning]
        assert not credits or credits == list(range(min(credits), c.cap + 1))
        minima[label] = min(credits) if credits else None
    if c.fixed_fault:
        for label, a in (("remembered_ready", 0), ("remembered_cold", -1)):
            credits = [b for b in range(c.cap + 1)
                       if State(b, c.spacing, apparatus=a, remembered=True) in winning]
            minima[label] = min(credits) if credits else None

    report = {"config": asdict(c), "policy_class": policy_class,
              "minimum_initial_credit": minima, "states": len(states),
              "winning_states": len(winning), "controller_edges": edge_count,
              "maximum_loss_rank": max(losing_rank.values(), default=0)}
    if export:
        outdir = Path(__file__).parent / "witnesses"
        outdir.mkdir(exist_ok=True)
        records = []
        # Preserve the entire winning invariant and one action for EACH event.
        for q in sorted(winning):
            for event, actions in branches[q]:
                candidates = [(a, t, f) for a, t, f in actions if t in winning]
                # Low current fee first; this is only a witness tie break, not
                # a long-run burden optimum. It demonstrates optional suspension.
                action, target, flow = min(candidates, key=lambda x: (x[2]["fee"], x[0]))
                records.append({**asdict(q), "event": event, "action": action,
                                "successor": asdict(target), "flow": flow})
        counterstrategy = []
        for q in sorted(losing):
            # Rank strictly descends under EVERY controller reply to the
            # selected event; therefore this forces a finite-time violation.
            for event, actions in branches[q]:
                if all(t is None or (t in losing and losing_rank[t] < losing_rank[q])
                       for _, t, _ in actions):
                    counterstrategy.append({"state": asdict(q), "rank": losing_rank[q],
                        "event": event, "all_controller_replies": [
                            {"action": a, "successor": None if t is None else asdict(t),
                             "successor_rank": 0 if t is None else losing_rank[t], "flow": f}
                            for a, t, f in actions]})
                    break
            else:
                raise AssertionError("Losing state lacks a decreasing-rank certificate")
        fname = outdir / f"{c.name}-{policy_class}.json"
        fname.write_text(json.dumps({"model": asdict(c), "policy_class": policy_class,
                                    "winning_invariant_and_policy": records,
                                    "losing_counterstrategy": counterstrategy}, indent=2) + "\n")
        report["witness_file"] = str(fname.relative_to(Path(__file__).parent))
        report["witness_rows"] = len(records)
    return report, (states, branches, winning)


def independent_finite_horizon_check(game):
    states, branches, winning = game
    current = set(states)
    counts = [len(current)]
    # A second implementation of bounded safety recursion. It shares the
    # transition table; this checks the solver, not independent model validity.
    for _ in range(len(states) + 1):
        next_set = {q for q in current if all(
            any(t in current for _, t, _ in actions if t is not None)
            for _, actions in branches[q])}
        assert winning <= next_set
        if next_set == current:
            assert next_set == winning
            break
        current = next_set
        counts.append(len(current))
    else:
        raise AssertionError("Finite descending fixed point did not stabilize")
    return counts


def exhaustive_tree_check(game, c, max_horizon=4):
    states, branches, _ = game

    def tree(q, horizon):
        if horizon == 0:
            return True
        return all(any(t is not None and tree(t, horizon - 1) for _, t, _ in acts)
                   for _, acts in branches[q])

    bounded = set(states)
    checked = 0
    roots = [State(b, c.spacing, apparatus=a) for b in range(min(10, c.cap) + 1)
             for a in (0, -1)]
    for h in range(max_horizon + 1):
        for q in roots:
            assert tree(q, h) == (q in bounded)
            checked += 1
        bounded = {q for q in bounded if all(
            any(t in bounded for _, t, _ in acts if t is not None)
            for _, acts in branches[q])}
    return checked


def analytic(c):
    # Exact prescribed-route theorem only for local diagnosis every episode.
    # Full information, a remembered fixed bit, and an alternative supplier
    # have different route definitions and are solved by the game instead.
    assert c.hazard and not c.full_information and not c.fixed_fault
    assert c.alternative_premium is None
    base_slots = 1 + (not c.full_information) + (not c.authority_supplied)
    fees = c.implementation + (0 if c.full_information else c.diagnostic) + (
        0 if c.authority_supplied else c.authority)
    tau_s = int(base_slots)
    cost_s = tau_s * c.operating + fees
    tau_r = tau_s + (0 if c.full_information else c.rebuild_delay)
    cost_r = tau_r * c.operating + fees + (0 if c.full_information else c.rebuild_cost)
    assert cost_s > 0 and cost_r > 0
    p = c.gross - c.operating
    gap_s = max(0, c.spacing - tau_s)
    gap_r = max(0, c.spacing - tau_r)
    maintain = c.maintenance
    sufficient_s = (c.cap >= cost_s and tau_s <= c.deadline and p - maintain >= 0 and
                    gap_s * (p - maintain) >= cost_s)
    sufficient_r = (c.cap >= cost_r and tau_r <= c.deadline and p >= 0 and gap_r * p >= cost_r)
    return {"spacing": c.spacing, "rebuild_delay": c.rebuild_delay,
            "standby_duration": tau_s, "standby_episode_cost": cost_s,
            "standby_healthy_gap": gap_s, "standby_net_cycle": gap_s * (p - maintain) - cost_s,
            "standby_ready_infinite_feasible": sufficient_s,
            "standby_ready_min_credit": cost_s if sufficient_s else None,
            "on_demand_duration": tau_r, "on_demand_episode_cost": cost_r,
            "on_demand_healthy_gap": gap_r, "on_demand_net_cycle": gap_r * p - cost_r,
            "on_demand_cold_infinite_feasible": sufficient_r,
            "on_demand_cold_min_credit": cost_r if sufficient_r else None}


def trace_witness(c, game, credit, initial_app, max_slots=40):
    """Illustrative earliest-onset trajectory; infinite proof is the invariant."""
    states, branches, winning = game
    q = State(credit, c.spacing, apparatus=initial_app)
    assert q in winning
    trace = []
    for t in range(max_slots):
        events = branches[q]
        event, actions = next(((e, a) for e, a in events if e == "fault_onset"), events[0])
        candidates = [(a, n, f) for a, n, f in actions if n in winning]
        a, n, flow = min(candidates, key=lambda x: (x[2]["fee"], x[0]))
        trace.append({"slot": t, "before": asdict(q), "event": event,
                      "action": a, "flow": flow, "after": asdict(n)})
        q = n
    return trace


def main():
    base = Config("standby_advantage")
    configs = [
        base,
        replace(base, name="suspension_advantage", gross=4, maintenance=4,
                rebuild_cost=1, rebuild_delay=1, spacing=7, deadline=4),
        replace(base, name="cheap_instant_rebuild", rebuild_cost=0, rebuild_delay=0),
        replace(base, name="no_hazard", hazard=False),
        replace(base, name="full_information", full_information=True),
        replace(base, name="fixed_fault_retained_bit", fixed_fault=True),
        replace(base, name="authority_supplied", authority_supplied=True),
        replace(base, name="alternative_provider", alternative_premium=2),
        replace(base, name="outside_spacing_class", spacing=4),
        replace(base, name="feedstock_removed", gross=0),
        replace(base, name="long_spacing", spacing=9),
    ]
    reports = []
    traces = {}
    for c in configs:
        for policy_class in ("all", "standby", "on_demand"):
            report, game = solve(c, policy_class, export=policy_class == "all")
            report["bounded_safety_counts"] = independent_finite_horizon_check(game)
            report["bounded_tree_cases_checked"] = exhaustive_tree_check(game, c)
            reports.append(report)
            if policy_class == "all":
                for label, app in (("ready", 0), ("cold", -1)):
                    credit = report["minimum_initial_credit"][label]
                    if credit is not None:
                        traces[f"{c.name}-{label}"] = trace_witness(c, game, credit, app)

        # Closed-form frontier is exact for the two prescribed routes under
        # their stated start assets. Here test ordinary hazard/local-info cases.
        if c.hazard and not c.full_information and not c.fixed_fault and c.alternative_premium is None:
            a = analytic(c)
            standby = next(r for r in reports if r["config"]["name"] == c.name and r["policy_class"] == "standby")
            cold = next(r for r in reports if r["config"]["name"] == c.name and r["policy_class"] == "on_demand")
            expected_s = a["standby_ready_min_credit"]
            expected_r = a["on_demand_cold_min_credit"]
            assert standby["minimum_initial_credit"]["ready"] == expected_s
            assert cold["minimum_initial_credit"]["cold"] == expected_r

    # Detailed Δ×L frontier: analytic route proofs, separately checked against
    # exact finite games for every grid point, from matched cap and start state.
    frontier = []
    for spacing, delay in product(range(3, 11), range(5)):
        c = replace(base, name=f"grid_s{spacing}_l{delay}", spacing=spacing, rebuild_delay=delay)
        row = analytic(c)
        for pc, field, asset in (("standby", "standby_ready_min_credit", "ready"),
                                 ("on_demand", "on_demand_cold_min_credit", "cold")):
            report, _ = solve(c, pc)
            assert report["minimum_initial_credit"][asset] == row[field]
        frontier.append(row)

    cap_checks = []
    suspension = next(c for c in configs if c.name == "suspension_advantage")
    for c0, caps in ((base, (6, 15, 16)), (suspension, (6, 7, 8))):
        for cap in caps:
            c = replace(c0, name=f"{c0.name}_cap{cap}", cap=cap)
            r, g = solve(c, "all", export=True)
            r["bounded_safety_counts"] = independent_finite_horizon_check(g)
            cap_checks.append(r)
    expected_caps = {
        "standby_advantage_cap6": {"ready": 6, "cold": None},
        "standby_advantage_cap15": {"ready": 6, "cold": None},
        "standby_advantage_cap16": {"ready": 6, "cold": 16},
        "suspension_advantage_cap6": {"ready": None, "cold": None},
        "suspension_advantage_cap7": {"ready": None, "cold": None},
        "suspension_advantage_cap8": {"ready": 6, "cold": 8},
    }
    for r in cap_checks:
        assert r["minimum_initial_credit"] == expected_caps[r["config"]["name"]]

    report = {"status": "all assertions passed", "date": "2026-10-05",
              "method": "exact greatest fixed point of finite deadline safety games",
              "selected_cases": reports, "analytic_frontier": frontier,
              "frontier_base_config": asdict(base),
              "cap_credit_checks": cap_checks,
              "illustrative_witness_traces": traces,
              "limitations": ["Fixed grammar, error-free fresh diagnosis, perfect recall",
                              "Deadline and minimum onset spacing are supplied assumptions",
                              "External feedstock supports every healthy slot's gross output",
                              "Cap bounds carried reserve after receipts, payment, and spill",
                              "Witness tie break is not long-run burden optimal",
                              "Finite-horizon cross-check shares the transition table"]}
    directory = Path(__file__).parent
    (directory / "recurrent-repair-results.json").write_text(json.dumps(report, indent=2) + "\n")
    with (directory / "route-frontier.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(frontier[0]))
        writer.writeheader()
        writer.writerows(frontier)
    summary = [{"case": r["config"]["name"], "class": r["policy_class"],
                **r["minimum_initial_credit"], "states": r["states"]} for r in reports]
    print(json.dumps({"status": report["status"], "frontier_points": len(frontier),
                      "selected_results": summary, "cap_checks": [
                          {"case": r["config"]["name"], **r["minimum_initial_credit"]}
                          for r in cap_checks]}, indent=2))


if __name__ == "__main__":
    main()
