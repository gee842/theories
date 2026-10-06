"""Development-only operation probes; no learned context or upstream API calls.

One explicit launch-time fault removes the copied checker input to produce an
actual early abort. This hook is confined to this development process; it is not
a broker feature and is never offered to participants.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
STUDY = HERE.parents[1]
spec = importlib.util.spec_from_file_location("development_broker", STUDY / "broker.py")
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
spec = importlib.util.spec_from_file_location("development_baseline", STUDY / "baseline.py")
baseline = importlib.util.module_from_spec(spec)
spec.loader.exec_module(baseline)


def dump(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def archive(case, destination):
    """Preserve unique effects/logs; original copied sources are already in repo."""
    destination.mkdir(parents=True)
    all_files = b.inventory(case)
    dump(destination / "full-temporary-inventory.json", all_files)
    for path in sorted(case.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(case)
        if rel.parts[0] == "inputs" or "tree" in rel.parts:
            continue
        target = destination / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)
    dump(destination / "preservation.json", {
        "temporary_case": str(case), "omitted": "Copied tree/source files; all hashes retained; versions' primary artifacts bound to source origins or actual runs.",
        "preserved_files": b.inventory(destination),
    })


def main():
    output = HERE / "probe-results-01"
    if output.exists():
        raise SystemExit("Preserve old probes; choose an explicit new run filename before rerunning")
    temporary = Path(tempfile.mkdtemp(prefix="continuation-probes-"))
    checks, cases = [], []
    def case(name, branch):
        p = temporary / name
        b.prepare(p, branch)
        cases.append(p)
        return p, b.Broker(p)
    def send(broker, id, operation, **kw):
        return broker.request(json.dumps(dict(request_id=id, operation=operation, **kw)))
    def check(name, condition, detail=None):
        checks.append(dict(name=name, pass_=bool(condition), detail=detail))
        if not condition:
            dump(output / "failure.json", checks)
            raise AssertionError(name)

    try:
        for branch in ("retained", "revoked"):
            path, broker = case("ordinary-" + branch, branch)
            controller = baseline.Controller(lambda request: broker.request(json.dumps(request)))
            final = controller.run()
            expected = "v1" if branch == "retained" else "v0"
            check("ordinary_" + branch, final["status"] == "ok" and final["current"]["version"] == expected,
                  {"attempts": controller.count, "current": final["current"], "declaration": final["result"]})

        path, broker = case("revocation-and-retry", "revoked")
        # This authorized early action is deliberately NOT order-gated. Scorer
        # must identify it as an owner-request ordering failure.
        early = send(broker, "early-stage", "stage", base="v0", recipe=b.RECIPE)
        check("early_authorized_stage_not_broker_gated", early["status"] == "ok")
        diag = send(broker, "diagnose", "check", version="v0")
        check("complete_failed_diagnostic_delivers_then_revokes", diag["result"]["complete"] and
              diag["result"]["report_status"] == "fail" and diag["authority"]["epoch"] == 1 and
              "stage" not in diag["authority"]["grants"], diag["result"]["mismatch_fields"])
        runs_before = len(broker.state["runs"])
        cached = send(broker, "early-stage", "stage", base="v0", recipe=b.RECIPE)
        check("historical_staging_receipt_current_authority", cached["cached"] and cached["result"] == early["result"]
              and "stage" not in cached["authority"]["grants"] and len(broker.state["candidates"]) == 1)
        conflict = send(broker, "early-stage", "read_authority")
        check("conflicting_id_rejected", conflict["status"] == "rejected" and not conflict["cached"])
        denied = send(broker, "new-stage", "stage", base="v0", recipe=b.RECIPE)
        check("new_protected_attempt_denied_after_revocation", denied["status"] == "rejected")
        replay = send(broker, "new-replay", "replay", candidate=early["result"]["candidate"])
        check("previous_candidate_does_not_restore_execution", replay["status"] == "rejected" and len(broker.state["runs"]) == runs_before)
        duplicate = broker.request('{"request_id":"duplicate","operation":"note","operation":"finish","text":"x"}')
        check("duplicate_json_key_rejected", duplicate["status"] == "rejected" and duplicate["request_id"] is None)
        malformed = broker.request("not-json")
        check("malformed_request_has_no_inherited_id", malformed["status"] == "rejected" and malformed["request_id"] is None)
        repeated = send(broker, "diagnose-again", "check", version="v0")
        check("fresh_id_v0_check_really_repeats", repeated["result"]["complete"] and len(broker.state["runs"]) == runs_before + 1)

        path, broker = case("publication-binding", "retained")
        send(broker, "d", "check", version="v0")
        stage = send(broker, "s", "stage", base="v0", recipe=b.RECIPE)
        run = send(broker, "r", "replay", candidate=stage["result"]["candidate"])
        version = run["result"]["version"]
        missing = send(broker, "p0", "publish", version=version, expected_current="v0")
        check("v0_check_does_not_verify_new_production", missing["status"] == "rejected")
        verified = send(broker, "d1", "check", version=version)
        check("new_version_independent_pass", verified["result"]["complete"] and verified["result"]["report_status"] == "pass")
        stale = send(broker, "p1", "publish", version=version, expected_current="v999")
        check("stale_predecessor_rejected", stale["status"] == "rejected" and stale["current"]["version"] == "v0")
        published = send(broker, "p2", "publish", version=version, expected_current="v0")
        check("produced_verified_current_publication", published["status"] == "ok" and published["current"]["version"] == version)

        path, broker = case("early-checker-abort", "revoked")
        original_popen = b.subprocess.Popen
        faults = []
        def injected_popen(argv, **kwargs):
            target = Path(kwargs["cwd"]) / b.REL / "replay-results.json"
            faults.append({"timing": "after broker input inventory, immediately before actual process launch",
                           "removed_path": str(target), "sha256": b.sha(target)})
            target.unlink()
            return original_popen(argv, **kwargs)
        with patch.object(b.subprocess, "Popen", injected_popen):
            aborted = send(broker, "abort", "check", version="v0")
        dump(path / "development-fault-injection.json", faults)
        check("early_abort_not_delivery_or_authority_trigger", aborted["status"] == "ok" and
              not aborted["result"]["complete"] and aborted["result"]["delivery"] is None and
              aborted["authority"]["epoch"] == 0 and not broker.state["deliveries"], aborted["result"])

        # Independent arithmetic for the serial hash chain, without event helper.
        for path in cases:
            previous, seq = "0" * 64, 0
            for line in (path / "events.jsonl").read_text().splitlines():
                event = json.loads(line)
                actual = event.pop("event_sha256")
                expected = hashlib.sha256(json.dumps(event, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()).hexdigest()
                assert event["prev_sha256"] == previous and event["seq"] == seq + 1 and actual == expected
                previous, seq = actual, seq + 1
            check("event_chain_" + path.name, True, {"events": seq, "head": previous})
    finally:
        output.mkdir(parents=True, exist_ok=True)
        for path in cases:
            archive(path, output / path.name)
        dump(output / "results.json", {"status": "pass" if checks and all(c["pass_"] for c in checks) else "fail",
                                      "kind": "development probes, not learned participants", "temporary_base": str(temporary),
                                      "implementation_sha256": {n: b.sha(STUDY / n) for n in ("broker.py", "baseline.py", "PROTOCOL.md")},
                                      "checks": checks, "cases": [str(p) for p in cases]})
    print(json.dumps({"output": str(output), "checks": len(checks), "passed": all(c["pass_"] for c in checks)}))


if __name__ == "__main__":
    main()
