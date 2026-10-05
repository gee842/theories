#!/usr/bin/env python3
"""Exact, finite verification of the declared paid-revision toy model.

Standard library only. Run from any directory. Writes results beside this file.
All pre-revision moves consume >=1 reserve; the graph is therefore acyclic.
No claim of empirical validity, novelty, or proof by simulation is intended.
"""

from dataclasses import dataclass, asdict
from functools import lru_cache
from itertools import product
from pathlib import Path
import json


@dataclass(frozen=True, order=True)
class State:
    theta: int
    reserve: int
    archive: bool = True
    service: bool = True
    known: bool = False
    permit: bool = False
    mode: str = "old"


ACTIONS = ("inspect", "test", "authorize", "rebuild", "apply0", "apply1", "routine")
COSTS = {"inspect": 1, "test": 2, "authorize": 1, "rebuild": 2,
         "apply0": 1, "apply1": 1, "routine": 1}


def observe(s):
    # Perfect recall is allowed; once acquired, diagnosis is never erased.
    return (s.reserve, s.archive, s.service, s.known,
            s.theta if s.known else None, s.permit, s.mode)


def step(s, a, authorized=True):
    """None means unavailable. Failed repairs are terminal, not recoverable."""
    if s.mode != "old" or s.reserve < COSTS[a]:
        return None
    if a == "inspect" and not s.archive:
        return None
    if a == "authorize" and not s.service:
        return None
    if a.startswith("apply") and authorized and not s.permit:
        return None
    d = asdict(s)
    d["reserve"] -= COSTS[a]
    if a in ("inspect", "test"):
        d["known"] = True
    elif a in ("authorize", "rebuild"):
        d["permit"] = True
    elif a.startswith("apply"):
        d["mode"] = "renewed" if int(a[-1]) == s.theta else "failed"
    elif a == "routine":
        d["archive"] = False
        d["service"] = False
        d["permit"] = False
    return State(**d)


def canonical(states):
    return tuple(sorted(set(states)))


def initial(b, r=True, u=True):
    return canonical(State(theta, b, r, u) for theta in (0, 1))


@lru_cache(None)
def winning(belief, authorized=True):
    """Universal hidden-state safety and eventual renewed-mode reachability."""
    if all(s.mode == "renewed" for s in belief):
        return True
    if any(s.mode != "old" for s in belief):
        return False
    for a in ACTIONS:
        successors = [step(s, a, authorized) for s in belief]
        if any(s is None or s.mode == "failed" for s in successors):
            continue
        branches = {}
        for s in successors:
            branches.setdefault(observe(s), []).append(s)
        if all(winning(canonical(ss), authorized) for ss in branches.values()):
            return True
    return False


def witness(belief, authorized=True):
    if all(s.mode == "renewed" for s in belief):
        return {"goal": True}
    if not winning(belief, authorized):
        return None
    for a in ACTIONS:
        successors = [step(s, a, authorized) for s in belief]
        if any(s is None or s.mode == "failed" for s in successors):
            continue
        branches = {}
        for s in successors:
            branches.setdefault(observe(s), []).append(s)
        if all(winning(canonical(ss), authorized) for ss in branches.values()):
            return {"action": a, "branches": [
                {"observation": obs, "then": witness(canonical(ss), authorized)}
                for obs, ss in branches.items()]}
    raise AssertionError("Winning state lacks a witness")


def brute_force_tree(belief, authorized=True):
    """Independent un-memoized policy-tree enumeration on bounded small cases.

    Enumerates all candidate first actions, recursively each observation branch,
    without consulting the dynamic-programming results or witness routine.
    """
    if all(s.mode == "renewed" for s in belief):
        return True
    if any(s.mode != "old" for s in belief):
        return False
    for a in ACTIONS:
        by_observation = {}
        usable = True
        for s in belief:
            ns = step(s, a, authorized)
            if ns is None or ns.mode == "failed":
                usable = False
                break
            by_observation.setdefault(observe(ns), set()).add(ns)
        if usable and all(brute_force_tree(tuple(ss), authorized)
                          for ss in by_observation.values()):
            return True
    return False


def all_reachable(belief, authorized=True):
    """Concrete-state enumeration, used to test pathwise stock accounting."""
    seen = set(belief)
    pending = list(belief)
    count = 0
    while pending:
        s = pending.pop()
        for a in ACTIONS:
            t = step(s, a, authorized)
            if t is None:
                continue
            count += 1
            assert t.reserve == s.reserve - COSTS[a]
            assert t.reserve >= 0
            if s.known:
                assert t.known
            if t not in seen:
                seen.add(t)
                pending.append(t)
    return len(seen), count


def finite_resource_checks():
    # Independent pure-ledger microstep check. Every sequence of length <=5
    # using deltas -2,-1,0,1,2 is checked against all initial stocks 0..3.
    ledger_cases = 0
    final_balance_false_positives = 0
    for n in range(6):
        for deltas in product(range(-2, 3), repeat=n):
            for b0 in range(4):
                b = b0
                legal = True
                for delta in deltas:
                    b += delta
                    legal = legal and b >= 0
                prefix = all(b0 + sum(deltas[:k]) >= 0 for k in range(1, n + 1))
                assert legal == prefix
                ledger_cases += 1
                final_balance_false_positives += int(b >= 0 and not legal)

    # A Petri-style two-conversion state equation permits a nonzero firing
    # vector at zero marking but the first transition is not enabled.
    conversions = (((1, 0), (0, 1)), ((0, 1), (1, 0)))
    b0 = (0, 0)
    combined_net = tuple(sum(v[j] - u[j] for u, v in conversions) for j in range(2))
    enabled = [all(b0[j] >= u[j] for j in range(2)) for u, v in conversions]
    assert combined_net == (0, 0) and not any(enabled)

    # Separately attainable D and P compete for one unit; neither completion
    # nor even joint possession is reachable.
    reach = {(1, False, False)}
    pending = list(reach)
    while pending:
        b, d, p = pending.pop()
        successors = [] if b == 0 else [(b - 1, True, p), (b - 1, d, True)]
        for q in successors:
            if q not in reach:
                reach.add(q)
                pending.append(q)
    assert any(q[1] for q in reach) and any(q[2] for q in reach)
    assert not any(q[1] and q[2] for q in reach)
    return {
        "ledger_sequences_checked": ledger_cases,
        "final_balance_false_positives": final_balance_false_positives,
        "conversion_zero_marking": {"combined_net": combined_net, "enabled": enabled},
        "prerequisite_competition_reachable_states": sorted(reach),
    }


def main():
    rows = []
    checked = 0
    for r, u, b in product((False, True), (False, True), range(8)):
        B = initial(b, r, u)
        expected = b >= (1 if r else 2) + (1 if u else 2) + 1
        result = winning(B)
        assert result == expected
        full_information = all(winning((s,)) for s in B)
        assert full_information == (b >= (1 if u else 2) + 1)
        physical = all(winning((s,), False) for s in B)
        assert physical == (b >= 1)
        # Only b<=5 for independent brute force keeps verification quick.
        if b <= 5:
            assert brute_force_tree(B) == result
            checked += 1
        rows.append({"archive": r, "service": u, "initial_reserve": b,
                     "observation_robust_authorized": result,
                     "full_information_authorized": full_information,
                     "full_information_physical": physical})

    routine_rows = []
    for b in range(1, 9):
        B = canonical(step(s, "routine") for s in initial(b))
        result = winning(B)
        assert result == (b >= 6)
        routine_rows.append({"initial_reserve": b, "residual_reserve": b - 1,
                             "robust_after_initial_routine": result})

    # Diagnosis acquired before record destruction remains available.
    before = State(0, 6, known=False)
    after = step(step(before, "inspect"), "routine")
    assert after.known and observe(after)[4] == 0
    assert not after.archive

    # Enumerate all concrete states and edges for eight initial reserve levels
    # under each authority interpretation; all satisfy prefix stock accounting.
    reach_checks = []
    for b, auth in product(range(8), (False, True)):
        nstates, nedges = all_reachable(initial(b), auth)
        reach_checks.append({"reserve": b, "authorized": auth,
                             "reachable_states": nstates, "edges": nedges})

    # Myopic routine output is an imposed objective, not welfare.
    myopic = initial(3)
    myopic_trace = []
    while all(s.mode == "old" and s.reserve >= 1 for s in myopic):
        myopic = canonical(step(s, "routine") for s in myopic)
        myopic_trace.append({"reserve": myopic[0].reserve,
                             "archive": myopic[0].archive,
                             "service": myopic[0].service})
    assert not winning(myopic)

    report = {
        "status": "all assertions passed",
        "model": "declared deterministic paid-revision toy model, perfect recall",
        "threshold_cases_checked": len(rows),
        "independent_policy_tree_cases_checked": checked,
        "capacity_table": rows,
        "initial_routine_cases": routine_rows,
        "optimal_three_unit_witness": witness(initial(3)),
        "post_routine_six_unit_witness": witness(canonical(step(s, "routine") for s in initial(6))),
        "recall_control": {"archive_destroyed": not after.archive, "diagnosis_retained": after.known},
        "concrete_reachability_checks": reach_checks,
        "myopic_routine_trace": myopic_trace,
        "resource_countermodels": finite_resource_checks(),
        "cached_beliefs_evaluated": winning.cache_info().currsize,
        "limits": ["Small synthetic state space, fixed action grammar and dynamics",
                   "No empirical validation or unrestricted concept generation",
                   "Brute force shares the transition function, so proofs remain necessary",
                   "The post-revision renewing loop assumes explicitly supplied external input"],
    }
    out = Path(__file__).with_name("revision-model-results.json")
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "threshold_cases": len(rows),
                      "independent_tree_cases": checked,
                      "ledger_cases": report["resource_countermodels"]["ledger_sequences_checked"],
                      "result_path": str(out)}, indent=2))


if __name__ == "__main__":
    main()
