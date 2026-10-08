#!/usr/bin/env python3
"""Exact model comparison; exhaustive-sequence reference independent of DP.

No model API, learned policy, empirical AI measurement or statistical inference.
Protocol fixes the family before execution. Receipt hashes bind exact inputs.
"""
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "RESEARCH.md").is_file())
PROTOCOL = ROOT / "_process/research/2026-10-05-generative-foundation-review/root-foundation/CORRECTION-INFRASTRUCTURE-PROTOCOL.md"


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def run():
    results = []
    totals = {"models": 0, "cases": 0, "feasible": 0, "infeasible": 0}
    names = ("acceptance_only", "stale_filter", "recomputed")
    metrics = {name: {"unsafe_on_feasible": 0, "suboptimal_on_feasible": 0,
                      "maximum_regret": 0, "executed_decisions": 0,
                      "accepting_decisions": 0} for name in names}
    witnesses = {}
    for flat_next in product(range(3), repeat=4):
        nxt = [flat_next[:2], flat_next[2:], (2, 2)]
        for flat_reward in product((0, 2), repeat=4):
            rewards = [flat_reward[:2], flat_reward[2:], (0, 0)]
            model = totals["models"]
            totals["models"] += 1

            @lru_cache(None)
            def unrestricted(n, s):
                if n == 0:
                    return 0
                return max(rewards[s][a] + unrestricted(n - 1, nxt[s][a]) for a in (0, 1))

            @lru_cache(None)
            def constrained(n, s):
                if s == 2:
                    return None
                if n == 0:
                    return 0
                values = [rewards[s][a] + v for a in (0, 1)
                          if (v := constrained(n - 1, nxt[s][a])) is not None]
                return max(values) if values else None

            def execute(n, initial, policy):
                s, value, trace, decisions = initial, 0, [initial], []
                for remaining in range(n, 0, -1):
                    choices = []
                    for a in (0, 1):
                        cv = constrained(remaining - 1, nxt[s][a])
                        if policy != "acceptance_only" and (s == 2 or cv is None):
                            continue
                        tail = cv if policy == "recomputed" else unrestricted(remaining - 1, nxt[s][a])
                        for accept in (False, True):
                            choices.append((rewards[s][a] + tail + int(accept), a, accept))
                    if not choices:
                        return {"blocked": True, "trace": trace, "return": value, "decisions": decisions}
                    # Highest transformed score, then lowest base action.
                    _, a, accept = max(choices, key=lambda x: (x[0], -x[1], x[2]))
                    assert accept
                    decisions.append([a, accept])
                    value += rewards[s][a]
                    s = nxt[s][a]
                    trace.append(s)
                return {"blocked": False, "trace": trace, "return": value, "decisions": decisions}

            # Independent oracle: explicitly enumerate entire action strings.
            def exhaustive(n, initial):
                best = None
                best_sequence = None
                for seq in product((0, 1), repeat=n):
                    s, total, safe = initial, 0, initial != 2
                    for a in seq:
                        total += rewards[s][a]
                        s = nxt[s][a]
                        safe = safe and s != 2
                    if safe and (best is None or total > best):
                        best, best_sequence = total, seq
                return best, best_sequence

            for n in range(1, 6):
                for initial in (0, 1):
                    totals["cases"] += 1
                    reference, sequence = exhaustive(n, initial)
                    assert reference == constrained(n, initial)
                    feasible = reference is not None
                    totals["feasible" if feasible else "infeasible"] += 1
                    row = {"model": model, "horizon": n, "initial": initial,
                           "feasible": feasible, "reference": reference, "policies": {}}
                    for name in names:
                        outcome = execute(n, initial, name)
                        safe = not outcome["blocked"] and all(s != 2 for s in outcome["trace"])
                        regret = reference - outcome["return"] if feasible and safe else None
                        count = metrics[name]
                        count["executed_decisions"] += len(outcome["decisions"])
                        count["accepting_decisions"] += sum(accept for _, accept in outcome["decisions"])
                        row["policies"][name] = {"safe": safe, "return": outcome["return"],
                                                  "blocked": outcome["blocked"], "regret": regret}
                        if feasible:
                            count["unsafe_on_feasible"] += not safe
                            count["suboptimal_on_feasible"] += bool(safe and regret > 0)
                            if regret is not None:
                                count["maximum_regret"] = max(count["maximum_regret"], regret)
                            failure = not safe or regret > 0
                            if failure and name not in witnesses:
                                witnesses[name] = {"next": nxt, "rewards": rewards, "row": row,
                                                   "outcome": outcome, "reference_sequence": sequence}
                            if name == "recomputed":
                                assert safe and regret == 0
                            if name == "stale_filter":
                                assert safe
                        elif name != "acceptance_only":
                            assert outcome["blocked"]
                    results.append(row)

    maintenance = []
    for cost, bonus, weight in product((0, 1, 2, 4, 8, 16), (1, 3, 17), (0, 1, 4, 16)):
        scores = {(divert, accept): cost * divert + bonus * accept
                  for divert, accept in product((False, True), repeat=2)}
        optimal = [list(a) for a, v in scores.items() if v == max(scores.values())]
        assert all(a[1] for a in optimal)
        assert all(a[0] for a in optimal) if cost > 0 else len(optimal) == 2
        augmented = {(divert, accept): value + (0 if divert else weight)
                     for (divert, accept), value in scores.items()}
        augmented_opt = [list(a) for a, v in augmented.items() if v == max(augmented.values())]
        assert all(not a[0] for a in augmented_opt) == (cost < weight)
        maintenance.append({"cost": cost, "acceptance_bonus": bonus, "access_bonus": weight,
                            "acceptance_optima": optimal, "augmented_optima": augmented_opt})

    traps = []
    for temptation in (3, 5, 9):
        branches = [[2, 2], [1, temptation]]
        unres = [max(r) for r in branches]
        restricted = [2, 1]
        stale_branch = max(range(2), key=lambda b: unres[b])
        good_branch = max(range(2), key=lambda b: restricted[b])
        assert stale_branch == 1 and good_branch == 0
        traps.append({"temptation": temptation, "stale_return": restricted[stale_branch],
                      "recomputed_return": restricted[good_branch]})
    hidden_policies = [(a, a) for a in (False, True)]
    informed_policies = list(product((False, True), repeat=2))
    usable = lambda policy: all(policy[int(s)] == s for s in (False, True))
    assert not any(map(usable, hidden_policies))
    assert sum(map(usable, informed_policies)) == 1
    gap = [(True, False), (False, False), (False, True)]
    overlap = [(True, False), (True, True), (False, True)]
    assert not all(any(s) for s in gap) and all(any(s) for s in overlap)
    records = HERE / "correction-infrastructure-model-records.jsonl"
    records.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in results))
    summary = {"status": "passed", "scope": "Exact finite-model execution; not learned-AI evidence",
               "protocol_sha256": digest(PROTOCOL), "runner_sha256": digest(Path(__file__)),
               "lean_source_sha256": digest(HERE / "CorrectionInfrastructure.lean"),
               "records_sha256": digest(records), "totals": totals, "metrics": metrics,
               "first_counterexamples": witnesses, "maintenance_cases": maintenance,
               "two_stage_controls": traps, "observation_control": "statewise yes, hidden no, disclosed yes",
               "handoff_control": "endpoints yes, gap fails, overlap passes"}
    (HERE / "correction-infrastructure-model-checks.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({"status": "passed", "totals": totals, "metrics": metrics}, indent=2))


if __name__ == "__main__":
    run()
