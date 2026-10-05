#!/usr/bin/env python3
"""Finite checks of protocol-transport obligations and counterexamples.

Standard library only. These examples test concrete proof obligations; they
do not constitute a machine proof of the general transport theorems.
Perfect recall of each listed interface and own actions is explicitly free
within these three-slot protocols. No hidden plant state is in that interface.
"""
from dataclasses import dataclass
from itertools import product
from pathlib import Path
import json


@dataclass(frozen=True)
class Plant:
    theta: int
    cash: int = 3
    tick: int = 0
    report: int | None = None
    permit: bool = False
    mode: str = "fault"


def observe(q, redacted):
    report = None if redacted else q.report
    return (q.cash, q.tick, report, q.permit, q.mode)


def step(q, action):
    """Plant action remains physical when unauthorized; certificate rejects it."""
    cost = 0 if action == "wait" else 1
    cash = q.cash - cost
    report, permit, mode = q.report, q.permit, q.mode
    authorized = True
    if action == "inspect":
        report = q.theta
    elif action == "authorize":
        permit = True
    elif action.startswith("apply"):
        authorized = q.permit
        mode = "goal" if int(action[-1]) == q.theta else "failure"
    else:
        assert action == "wait"
    if q.mode == "failure":
        mode = "failure"
    return Plant(q.theta, cash, q.tick + 1, report, permit, mode), authorized


def check_protocol(selector, *, redacted=False):
    choices = {}
    uniform = solvent = authorized = safe = target = deadline = True
    runs = []
    for theta in (0, 1):
        q = Plant(theta)
        history = (observe(q, redacted),)
        states, actions = [q], []
        for index in range(3):
            action = selector(index, history, theta)
            if history in choices and choices[history] != action:
                uniform = False
            choices[history] = action
            q, allowed = step(q, action)
            solvent &= q.cash >= 0
            authorized &= allowed
            safe &= q.mode != "failure"
            states.append(q)
            actions.append(action)
            history += (action, observe(q, redacted))
        target &= q.mode == "goal"
        deadline &= q.tick <= 3
        runs.append({"hidden_bit": theta, "actions": actions,
                     "cash_prefixes": [s.cash for s in states],
                     "final_mode": q.mode})
    flags = {"information_uniform": uniform, "all_prefixes_solvent": solvent,
             "authorized": authorized, "all_prefixes_safe": safe,
             "all_worlds_target": target, "deadline": deadline}
    return {**flags, "certificate_valid": all(flags.values()), "runs": runs}


def feedback(index, history, _theta):
    if index < 2:
        return ("inspect", "authorize")[index]
    return f"apply{history[-1][2]}"


def oracle(index, history, theta):
    return ("inspect", "authorize", f"apply{theta}")[index]


def unauthorized_feedback(index, history, _theta):
    if index < 2:
        return ("inspect", "wait")[index]
    return f"apply{history[-1][2]}"


def main():
    positive = check_protocol(feedback)
    assert positive["certificate_valid"]
    oracle_bad = check_protocol(oracle, redacted=True)
    assert oracle_bad["all_worlds_target"] and not oracle_bad["information_uniform"]
    authority_bad = check_protocol(unauthorized_feedback)
    assert authority_bad["all_worlds_target"] and not authority_bad["authorized"]

    # Exhaust ALL primitive three-command words. Physical successful words
    # exist separately in both worlds, but no common word guarantees repair.
    alphabet = ("inspect", "authorize", "apply0", "apply1", "wait")
    batch_count = 0
    best_batch_successes = 0
    separate_success = {0: False, 1: False}
    for word in product(alphabet, repeat=3):
        successes = 0
        for theta in (0, 1):
            q = Plant(theta)
            valid = True
            for action in word:
                q, allowed = step(q, action)
                # Failure is irreversible: a word cannot undo a wrong guess.
                valid &= allowed and q.cash >= 0 and q.mode != "failure"
            succeeded = valid and q.mode == "goal"
            separate_success[theta] |= succeeded
            successes += succeeded
        best_batch_successes = max(best_batch_successes, successes)
        assert successes < 2
        batch_count += 1
    assert all(separate_success.values()) and best_batch_successes == 1

    # Zero endpoint net expenditure cannot finance a negative balance prefix.
    balance = 0
    ledger = [balance]
    for delta in (-1, 1):
        balance += delta
        ledger.append(balance)
    assert balance == 0 and min(ledger) == -1

    protected = {"source", "goal"}
    path = ("source", "unsafe", "goal")
    assert path[0] in protected and path[-1] in protected
    assert not all(s in protected for s in path)

    # A conservative abstract environment can add adverse choices. Its
    # failure cannot establish failure of the simpler concrete implementation.
    abstract_outcomes, concrete_outcomes = {"goal", "unsafe"}, {"goal"}
    assert concrete_outcomes <= abstract_outcomes
    assert not abstract_outcomes <= {"goal"} and concrete_outcomes <= {"goal"}

    # Two individually feasible jobs contend for one slot/channel. Explicit
    # schedules at two slots restore feasibility without altering each job.
    schedules_one = list(product((0, 1, None), repeat=1))
    schedules_two = list(product((0, 1, None), repeat=2))
    both_done = lambda schedule: {0, 1} <= set(schedule)
    assert not any(map(both_done, schedules_one))
    assert any(map(both_done, schedules_two))

    # A certificate-composition bound realized at equality by two middle
    # actions. Resource units match and every physical prefix is financed.
    h_time, h_cost = 1, 2
    middle_times, middle_costs = (1, 2), (3, 4)
    lam1, delay1, factor1, overhead1 = 2, 1, 3, 1
    lam2, delay2, factor2, overhead2 = 2, 1, 2, 3
    m = len(middle_times)
    assert sum(middle_times) == lam1*h_time + delay1
    assert sum(middle_costs) == factor1*h_cost + overhead1
    low_times = [lam2*t + delay2 for t in middle_times]
    low_costs = [factor2*c + overhead2 for c in middle_costs]
    composed_time = lam2*lam1*h_time + lam2*delay1 + m*delay2
    composed_cost = factor2*factor1*h_cost + factor2*overhead1 + m*overhead2
    assert sum(low_times) == composed_time == 8
    assert sum(low_costs) == composed_cost == 20
    cash = composed_cost
    cash_prefixes = [cash]
    for expense in low_costs:
        cash -= expense
        cash_prefixes.append(cash)
    assert min(cash_prefixes) >= 0

    # Separate mode invariants are insufficient without a certified handoff.
    joint_safe = {(0, 0), (1, 1)}
    before, after_rule_only = (0, 0), (1, 0)
    assert before in joint_safe and after_rule_only not in joint_safe
    assert (1, 1) in joint_safe

    result = {
        "status": "all assertions passed",
        "feedback_protocol": positive,
        "hidden_oracle_counterexample": oracle_bad,
        "authority_counterexample": authority_bad,
        "precommitted_words_exhausted": batch_count,
        "best_precommitted_successes_out_of_two_worlds": best_batch_successes,
        "separately_successful_physical_paths": separate_success,
        "net_zero_unpayable_ledger": ledger,
        "unsafe_intermediate_path": path,
        "directionality": {"abstract_wins": False, "concrete_wins": True},
        "shared_channel": {"one_slot_feasible": False, "two_slots_feasible": True},
        "nested_protocol": {"duration": composed_time, "gross_cost": composed_cost,
                            "cash_prefixes": cash_prefixes},
        "rule_handoff": {"before_safe": True, "rule_only_change_safe": False},
        "limits": ["Finite examples are not a machine proof of CT1 or CT2",
                   "No finite truncation proves the unbounded-delay example",
                   "Perfect recall of the explicitly listed protocol interface is supplied",
                   "No empirical data or cross-domain universality claim"]
    }
    destination = Path(__file__).with_name("constraint-transport-results.json")
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"],
                      "precommitted_words_exhausted": batch_count,
                      "nested_protocol": result["nested_protocol"]}, indent=2))


if __name__ == "__main__":
    main()
