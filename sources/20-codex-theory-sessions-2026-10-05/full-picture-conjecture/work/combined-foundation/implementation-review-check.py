"""Independent source/graph replay; does not import the author's verifier.

Run from any directory with Python 3. Reads model and graph exports, and writes
only implementation-review-check.json beside this file. No reference builds.
"""
import hashlib
import importlib.util
import json
import sys
from collections import deque
from dataclasses import asdict, replace
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
IMPL = HERE / "implementation"
spec = importlib.util.spec_from_file_location("combined_model_review", IMPL / "model.py")
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def state_from_record(record):
    fields = {k: record[k] for k in m.State.__dataclass_fields__}
    for key in ("archive", "trainee"):
        if fields[key] is not None:
            fields[key] = tuple(fields[key])
    return m.State(**fields)


def edge_key(s, t, action, argument, cost, receipt, spill, events):
    return (s, t, action, argument, cost, receipt, spill, tuple(events))


def independently_enumerate(mode):
    seen = set(m.initial_states())
    queue = deque(m.initial_states())
    edge_set = set()
    while queue:
        s = queue.popleft()
        successors = m.successors(s, mode)
        assert successors
        for edge in successors:
            t = edge.successor
            edge_set.add(edge_key(s, t, edge.action, edge.argument, edge.cost,
                                  edge.receipt, edge.spill, edge.events))
            if t not in seen:
                seen.add(t)
                queue.append(t)
    return seen, edge_set


def check(mode):
    graph = json.loads((IMPL / ("graph-" + mode + ".json")).read_text())
    by_id = {r["id"]: state_from_record(r) for r in graph["states"]}
    exported = {
        edge_key(by_id[e["source"]], by_id[e["target"]], e["action"], e["argument"],
                 e["cost"], e["receipt"], e["spill"], e["events"])
        for e in graph["edges"]
    }
    states, edges = independently_enumerate(mode)
    assert states == set(by_id.values())
    assert edges == exported
    assert {by_id[i] for i in graph["initial"]} == set(m.initial_states())
    assert len(edges) == len(graph["edges"]), "Export has duplicate edges"
    assert len(states) == len(graph["states"]), "Export has duplicate states"

    false_certificates = sum(s.certificate and s.guard == 1 and s.candidate != s.truth for s in states)
    events_count = {event: 0 for event in m.EVENT_PHASES}
    ranks_fail = {event: 0 for event in m.EVENT_PHASES}
    min_debit = m.CAP
    for s, t, action, argument, cost, receipt, spill, events in edges:
        assert 0 <= s.funds <= m.CAP and 0 <= t.funds <= m.CAP
        assert s.funds - cost >= 0
        min_debit = min(min_debit, s.funds - cost)
        assert t.funds == s.funds - cost + receipt - spill
        assert cost == (0 if action == "resource_stop" else 1)
        assert receipt == (m.RECEIPT if action == "auxiliary_work" and mode != "no_renewal" else 0)
        assert spill == max(0, s.funds - cost + receipt - m.CAP)
        assert not s.bad or t.bad
        assert (action == "resource_stop") == (s.funds < 1)
        if action != "resource_stop":
            assert t.phase == (s.phase + 1) % m.PERIOD
        if action == "period_close":
            assert t.truth != s.truth
        else:
            assert t.truth == s.truth

        if "corrective_install" in events:
            assert s.phase == 15 and action == "admit" and argument == 1
            assert t.installed == s.truth and t.installed != s.installed
            assert s.certificate and s.guard == 1 and t.active
        for x in (0, 1):
            if "delivered_x" + str(x) in events:
                assert action == "ordinary_service" and argument == x
                assert s.skilled and s.lease and s.active
                assert ((s.installed >> x) & 1) == ((s.truth >> x) & 1)
                assert mode != "execution_blocked"
        if "maintained_archive" in events:
            assert cost == 1 and action == "maintain_archive"
            assert t.archive == (s.installed, s.evaluator, s.guard, s.data0, s.data1)
        if "trained_successor" in events:
            assert cost == 1 and action == "train_successor"
            assert s.archive is not None and t.trainee == s.archive
        if "competent_handoff" in events:
            assert cost == 1 and action == "handoff" and s.trainee == s.archive
            assert s.trainee == (t.installed, t.evaluator, t.guard, t.data0, t.data1)
            assert t.guard == 1 and t.skilled and t.carrier == 1 - s.carrier
        if action == "handoff" and s.trainee is None:
            assert not t.skilled and t.guard == 0

        if mode == "baseline":
            assert not s.bad and s.skilled and s.guard == 1
            assert not s.active or s.installed == s.truth
            if s.phase in (14, 15):
                assert s.certificate and s.candidate == s.truth and s.installed != s.truth
            if action == "observe" or action == "check":
                key = ("data" if action == "observe" else "check") + str(argument)
                assert getattr(t, key) == ((s.truth >> argument) & 1)
            if s.phase in (18, 19, 20, 21, 22):
                assert s.evaluator == 1 and s.installed == s.truth
        for event, phase in m.EVENT_PHASES.items():
            if event in events:
                events_count[event] += 1
                assert s.phase == phase
            elif (phase - t.phase) % m.PERIOD >= (phase - s.phase) % m.PERIOD:
                ranks_fail[event] += 1
    if mode == "baseline":
        assert false_certificates == 0 and not any(ranks_fail.values())
        assert all(events_count.values())

    # Distinct hidden truths/assessment flags cannot directly alter a choice.
    for s in states:
        chosen = m.choose(m.observe(s))
        for truth in range(4):
            for bad in (False, True):
                assert m.choose(m.observe(replace(s, truth=truth, bad=bad))) == chosen
    return {"mode": mode, "states": len(states), "edges": len(edges),
            "export_matches_actual_reachable_model": True,
            "ledger_event_payload_checks": True,
            "all_reachable_protected": all(not s.bad for s in states),
            "min_funds": min(s.funds for s in states), "min_after_debit": min_debit,
            "false_strict_certificates": false_certificates,
            "event_edges": events_count, "phase_rank_failure_edges": ranks_fail}


results = [check(mode) for mode in m.MODES]
output = {
    "method": "Independent BFS replay and microstep semantic assertions; no author verify.py import",
    "source_sha256": {
        name: hashlib.sha256((IMPL / name).read_bytes()).hexdigest()
        for name in ("model.py", "verify.py", "MODEL.md", "RESULTS.md", "results.json")
    },
    "results": results,
}
(HERE / "implementation-review-check.json").write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps(results, indent=2))
