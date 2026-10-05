"""Focused semantic audit; full graph/rank certification is performed separately."""
import json
import hashlib
from pathlib import Path
import sys
from dataclasses import replace

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "implementation"))
import model


def decoded(rule):
    """Independent arithmetic spelling of the four response tables."""
    return [rule % 2, rule // 2]


def run_two_rounds(mode, initial_truth):
    state = model.State(truth=initial_truth)
    transcript = []
    for step in range(46):
        edges = model.successors(state, mode)
        # Choose the first different physical law from a declared deterministic
        # cycle. This tests selected paths, not all environmental branches.
        desired = (state.truth + 1) % 4
        edge = next((e for e in edges if e.successor.truth == desired), edges[0])
        assert edge.successor.funds == state.funds - edge.cost + edge.receipt - edge.spill
        assert not state.bad or edge.successor.bad
        if state.funds == 0:
            assert edge.action == "resource_stop" and edge.cost == 0 and edge.successor == state
        else:
            assert edge.cost == 1
        # Invariance of action under every hidden truth and public-harm value,
        # with all actor-observable inputs held identical.
        expected_action = model.choose(model.observe(state))
        for truth in range(4):
            for bad in (False, True):
                hidden_variant = replace(state, truth=truth, bad=bad)
                assert model.choose(model.observe(hidden_variant)) == expected_action
        if edge.action == "ordinary_service" and edge.argument >= 0 and mode != "execution_blocked":
            correct = decoded(state.installed)[edge.argument] == decoded(state.truth)[edge.argument]
            assert ("wrong_service" in edge.events) == (not correct)
            assert (f"delivered_x{edge.argument}" in edge.events) == correct
        transcript.append({"step": step, "phase": state.phase, "truth": state.truth,
                           "action": edge.action, "argument": edge.argument,
                           "events": list(edge.events), "evaluator_before": state.evaluator,
                           "evaluator_after": edge.successor.evaluator,
                           "candidate_after": edge.successor.candidate,
                           "bad_after": edge.successor.bad,
                           "skilled_after": edge.successor.skilled,
                           "guard_after": edge.successor.guard})
        state = edge.successor
    return transcript


results = {}
for mode in model.MODES:
    paths = [run_two_rounds(mode, truth) for truth in (1, 2)]
    results[mode] = {
        "paths_checked": len(paths),
        "steps_checked": sum(map(len, paths)),
        "first_wrong_service_step": [next((r["step"] for r in p if "wrong_service" in r["events"]), None) for p in paths],
        "first_skill_loss_step": [next((r["step"] for r in p if not r["skilled_after"]), None) for p in paths],
        "delivered_ordinary_events": [sum(sum(e in ("delivered_x0", "delivered_x1") for e in r["events"]) for r in p) for p in paths],
    }
    if mode == "baseline":
        for truth, path in zip((1, 2), paths):
            assert path[4]["candidate_after"] == 0
            assert path[9]["evaluator_before"] == 0 and path[9]["evaluator_after"] == 1
            assert path[10]["candidate_after"] == truth
            assert all(not r["bad_after"] for r in path)
            for event in model.EVENT_PHASES:
                assert sum(event in r["events"] for r in path) == 2
    if mode == "record_loss":
        assert all(p[10]["candidate_after"] in (0, 3) for p in paths)
        assert all(not r["bad_after"] for p in paths for r in p)
    if mode in ("no_maintenance", "no_training"):
        assert all(not p[20]["skilled_after"] and p[20]["guard_after"] == 0 for p in paths)
        assert all(not r["events"] or "auxiliary_service" in r["events"]
                   for p in paths for r in p[23:])
    if mode in ("score_capture", "misleading_calibration"):
        assert all(any(r["bad_after"] for r in p) for p in paths)

# Check that the installed data generator does not secretly use fresh-check
# answers as a replacement discovery record in the missing-record control.
for truth in range(4):
    o = model.observe(model.State(phase=10, lease=True, evaluator=1,
                    data0=-1, data1=-1, check0=decoded(truth)[0], check1=decoded(truth)[1]))
    assert model.nominate(o) == 0

# Transfer deliberately varied payloads: no defaults are substituted for the
# actual archived programme/evaluator/verifier/linked records.
payload_checks = 0
for program in range(4):
    for evaluator in range(2):
        for guard in (1, 2):
            payload = (program, evaluator, guard, 1, 0)
            source = model.State(phase=19, lease=True, archive=payload)
            trained = model.successors(source, "baseline")[0].successor
            assert trained.trainee == payload
            handed = model.successors(trained, "baseline")[0].successor
            assert (handed.installed, handed.evaluator, handed.guard, handed.data0, handed.data1) == payload
            payload_checks += 1

report = {
    "scope": "Selected semantic replays and payload checks; not exhaustive graph certification or empirical validation.",
    "implementation_sha256": hashlib.sha256((HERE / "implementation" / "model.py").read_bytes()).hexdigest(),
    "modes": results,
    "total_path_steps": sum(r["steps_checked"] for r in results.values()),
    "hidden_field_action_comparisons": 8 * sum(r["steps_checked"] for r in results.values()),
    "payload_transfers_checked": payload_checks,
    "missing_record_check_answers_not_used": True,
    "all_passed": True,
}
(HERE / "cognitive-scope-audit.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
