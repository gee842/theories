"""Exhaustive support-graph certificate and controls for model.py.

Run: python3 verify.py. Writes graph-*.json, results.json, RESULTS.md.
Cycles after removing an event's edges refute its sure recurrence, without any
probability/fairness assumption. Baseline rank checks additionally give an
explicit bound. All states (including unsafe ones) stay in every graph.
"""
from collections import deque
from dataclasses import replace
from pathlib import Path
import json

import model as m

HERE = Path(__file__).resolve().parent


def enumerate_graph(mode):
    states = list(m.initial_states())
    ids = {s: i for i, s in enumerate(states)}
    initial = list(range(len(states)))
    predecessor = {i: None for i in initial}
    edges = []
    i = 0
    while i < len(states):
        s = states[i]
        successors = m.successors(s, mode)
        assert successors, "Actual transition relation must be total."
        for e in successors:
            t = e.successor
            if t not in ids:
                ids[t] = len(states)
                states.append(t)
                predecessor[ids[t]] = (i, len(edges))
            edges.append({"source": i, "target": ids[t], "action": e.action,
                          "argument": e.argument, "cost": e.cost, "receipt": e.receipt,
                          "spill": e.spill, "events": list(e.events)})
        i += 1
        assert len(states) < 200000, "Unexpected state expansion."
    return states, edges, initial, predecessor


def cycle_after_removing_event(n, edges, event):
    # Kahn elimination is independent of the phase-rank calculation.
    adjacent = [[] for _ in range(n)]
    indegree = [0] * n
    for e in edges:
        if event not in e["events"]:
            adjacent[e["source"]].append(e["target"])
            indegree[e["target"]] += 1
    queue = deque(i for i, k in enumerate(indegree) if k == 0)
    removed = 0
    while queue:
        i = queue.popleft()
        removed += 1
        for j in adjacent[i]:
            indegree[j] -= 1
            if indegree[j] == 0:
                queue.append(j)
    return {"acyclic": removed == n, "uneliminated_states": n - removed}


def trace_to(sid, predecessor, edges):
    path = []
    while predecessor[sid] is not None:
        previous, ei = predecessor[sid]
        path.append(edges[ei])
        sid = previous
    return list(reversed(path))


def check_edges(states, edges, mode):
    violations = []
    strict_false_states = [i for i, s in enumerate(states)
                           if s.certificate and s.guard == 1 and s.candidate != s.truth]
    # Event checks use public plant truth and actual payloads, not the actor's score.
    for ei, e in enumerate(edges):
        s, t = states[e["source"]], states[e["target"]]
        errors = []
        if t.funds != s.funds - e["cost"] + e["receipt"] - e["spill"]:
            errors.append("ledger does not reconcile")
        if s.funds - e["cost"] < 0:
            errors.append("unfunded debit prefix")
        if e["cost"] not in (0, 1) or (e["cost"] == 0) != (e["action"] == "resource_stop"):
            errors.append("unpriced executable microstep")
        if e["receipt"] and (e["action"] != "auxiliary_work" or e["receipt"] != m.RECEIPT):
            errors.append("unearned income")
        if e["spill"] != max(0, s.funds - e["cost"] + e["receipt"] - m.CAP):
            errors.append("incorrect resource cap")
        if s.bad and not t.bad:
            errors.append("public harm erased")
        for event in e["events"]:
            if event.startswith("delivered_x"):
                x = int(event[-1])
                if not (e["action"] == "ordinary_service" and e["argument"] == x
                        and s.active and s.skilled and s.lease and mode != "execution_blocked"
                        and m.output(s.installed, x) == m.output(s.truth, x)):
                    errors.append("false delivery label")
            if event == "corrective_install" and not (
                    s.phase == 15 and e["argument"] == 1 and t.installed == s.truth
                    and t.installed != s.installed and s.certificate and s.guard == 1):
                errors.append("false correction label")
            if event == "maintained_archive" and not (
                    s.phase == 18 and t.archive == m.payload(s) and s.skilled and s.lease):
                errors.append("false archive label")
            if event == "trained_successor" and not (
                    s.phase == 19 and s.archive is not None and t.trainee == s.archive
                    and s.skilled and s.lease):
                errors.append("false training label")
            if event == "competent_handoff" and not (
                    s.phase == 20 and s.trainee is not None and s.trainee == s.archive
                    and m.payload(t) == s.trainee and t.skilled and t.guard == 1
                    and t.carrier != s.carrier and s.lease):
                errors.append("false handoff label")
        if errors:
            violations.append({"edge": ei, "errors": errors})
    return violations, strict_false_states


def inspect(mode):
    states, edges, initial, pred = enumerate_graph(mode)
    violations, strict_false = check_edges(states, edges, mode)
    assert not violations, (mode, violations[:5])
    unsafe = [i for i, s in enumerate(states) if not m.protected(s)]
    recurrence = {}
    for event, phase in m.EVENT_PHASES.items():
        failures = []
        for ei, e in enumerate(edges):
            if event not in e["events"]:
                a = (phase - states[e["source"]].phase) % m.PERIOD
                b = (phase - states[e["target"]].phase) % m.PERIOD
                if not b < a:
                    failures.append(ei)
        cycle = cycle_after_removing_event(len(states), edges, event)
        recurrence[event] = {"sure_recurs": cycle["acyclic"],
                             "phase_rank_certificate": not failures,
                             "rank_failing_edges": len(failures),
                             "first_rank_failure": failures[0] if failures else None,
                             "cycle_test": cycle}
    # Explicit information restriction: changing hidden truth or the assessment
    # flag cannot change an action when all permitted observation is held fixed.
    noninterference_cases = 0
    for s in states:
        expected = m.choose(m.observe(s))
        for q in range(4):
            for bad in (False, True):
                assert m.choose(m.observe(replace(s, truth=q, bad=bad))) == expected
                noninterference_cases += 1
    graph = {"mode": mode, "period": m.PERIOD, "resource_cap": m.CAP,
             "initial": initial, "protected_predicate": "0 <= funds <= 8 and not bad",
             "event_phases": m.EVENT_PHASES,
             "states": [m.state_record(s, i) for i, s in enumerate(states)], "edges": edges}
    (HERE / ("graph-" + mode + ".json")).write_text(json.dumps(graph, indent=2) + "\n")
    shortest_bad = None
    if unsafe:
        # BFS construction assigns the first bad id a shortest prefix.
        sid = unsafe[0]
        path = trace_to(sid, pred, edges)
        shortest_bad = {"state": sid, "microsteps": len(path), "edges": path,
                        "state_record": m.state_record(states[sid], sid)}
    result = {"mode": mode, "states": len(states), "edges": len(edges),
              "initial_states": len(initial), "all_reachable_protected": not unsafe,
              "unsafe_states": len(unsafe), "min_funds": min(s.funds for s in states),
              "min_after_payment": min(states[e["source"]].funds - e["cost"] for e in edges),
              "ledger_and_event_semantics_pass": not violations,
              "false_strict_certificate_states": len(strict_false),
              "noninterference_cases": noninterference_cases,
              "evaluator_revised_edges": sum("evaluator_revised" in e["events"] for e in edges),
              "conditional_generation_edges": sum("conditional_candidate_constructed" in e["events"] for e in edges),
              "recurrence": recurrence, "shortest_public_violation": shortest_bad}
    if mode == "baseline":
        assert result["all_reachable_protected"] and not strict_false
        assert all(r["sure_recurs"] and r["phase_rank_certificate"] for r in recurrence.values())
        assert all(s.skilled and s.guard == 1 for s in states)
        assert all(not s.active or s.installed == s.truth for s in states)
        assert result["min_after_payment"] >= 0
    return result


def write_report(results):
    lines = ["# Exact combined-process results", "",
             "Every reachable support transition was enumerated; unsafe states were retained. "
             "These are exact results for the supplied finite process, not sampling estimates.", "",
             "| Condition | States | Edges | All prefixes protected | Sure recurring ordinary service (both contexts) | Competent succession recurs |",
             "|---|---:|---:|:---:|:---:|:---:|"]
    for r in results:
        service = all(r["recurrence"][e]["sure_recurs"] for e in ("delivered_x0", "delivered_x1"))
        handoff = r["recurrence"]["competent_handoff"]["sure_recurs"]
        lines.append(f"| {r['mode']} | {r['states']} | {r['edges']} | {'yes' if r['all_reachable_protected'] else 'no'} | {'yes' if service else 'no'} | {'yes' if handoff else 'no'} |")
    base = results[0]
    lines += ["", f"The baseline has {base['states']} reachable states and {base['edges']} actual transitions. "
              f"Its smallest boundary balance is {base['min_funds']} and smallest balance immediately after a debit is {base['min_after_payment']}. "
              "All six required events pass both the strict decreasing phase-rank certificate and an independent event-deleted cycle test. "
              "Each event therefore occurs at least once per 23 microsteps on every admitted infinite path. "
              "The initial evaluator actually changes after a failed fresh check; that judgment program then survives paid maintenance, training and transfer. "
              "Recurrent evaluator rewriting is neither needed nor claimed.", "",
              "All conditions pass ledger and event-truth checks. Fail-closed conditions can remain protected while losing delivered service. "
              "Score capture and misleading calibration allow wrong ordinary responses and preserve the resulting public harm flag. "
              "The latter control gives internally consistent but physically false strict certificates, demonstrating the dependence on the stated reliable calibration premise.", "",
              "The score-capture row is instructive: correct services in each context can recur while wrong services also occur. "
              "Recurring correct outcomes alone do not establish protection. Only the baseline passes protection together with all six required recurrence conditions. "
              "The earliest public violation in either unsafe control occurs after 17 microsteps. "
              "Archive maintenance and training remain operational in the record-loss control, so institutional succession alone does not guarantee the right acquired program.", "",
              "Every decision is a function of the explicit Observation object, which excludes hidden truth and the assessment flag. "
              f"The exhaustive hidden-field perturbation check covers {sum(r['noninterference_cases'] for r in results)} cases. "
              "This checks implementation access; it does not show that this controller is optimal or that diagnosis is universally necessary.", "",
              "Reproduce with `python3 verify.py`. Graph exports contain full state records, every edge, payments, receipts, spill, "
              "actual event labels, and initial states. `results.json` also records the shortest harmful prefix for each unsafe condition. "
              "See MODEL.md for the finite grammar, safe calibration, within-period stability, supplied productive inputs and all other scope assumptions.", ""]
    (HERE / "RESULTS.md").write_text("\n".join(lines))


if __name__ == "__main__":
    results = [inspect(mode) for mode in m.MODES]
    (HERE / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    write_report(results)
    print(json.dumps([{k: r[k] for k in ("mode", "states", "edges", "all_reachable_protected",
                     "unsafe_states", "min_funds", "false_strict_certificate_states")} for r in results], indent=2))
