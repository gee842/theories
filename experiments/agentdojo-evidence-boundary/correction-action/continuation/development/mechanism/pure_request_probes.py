"""Parser, terminal-retry and request-limit tests; no producer/checker execution."""
import importlib.util
import json
from pathlib import Path
import tempfile

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("development_helpers", HERE / "run_probes.py")
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
b = h.b


def main():
    output = HERE / "pure-request-results-01"
    if output.exists():
        raise SystemExit("Refusing to overwrite preserved pure probes")
    temporary = Path(tempfile.mkdtemp(prefix="continuation-pure-probes-"))
    checks, cases = [], []
    def record(name, condition, result):
        checks.append({"name": name, "pass": bool(condition), "observed": result})
        assert condition, name
    def send(broker, **request):
        return broker.request(json.dumps(request))
    try:
        p = temporary / "budget"
        b.prepare(p, "retained")
        cases.append(p)
        broker = b.Broker(p)
        for i in range(1, 17):
            r = send(broker, request_id="first" if i == 1 else f"read-{i}", operation="read_authority")
            assert r["status"] == "ok"
        r = send(broker, request_id="first", operation="read_authority")
        record("seventeenth_cached_attempt_rejects", r["status"] == "rejected" and not r["cached"] and
               r["error"] == "Request budget exhausted" and broker.state["attempts"] == 17, r)

        p = temporary / "terminal-and-malformed"
        b.prepare(p, "revoked")
        cases.append(p)
        broker = b.Broker(p)
        r = send(broker, request_id="bad-operation", operation=[])
        record("unhashable_operation_explicit_rejection", r["status"] == "rejected" and r["error"] == "Operation must be a string", r)
        r = broker.request('{"request_id":"bad-duplicate","operation":"read","operation":"note"}')
        record("duplicate_key_rejected", r["status"] == "rejected" and r["request_id"] is None, r)
        r = send(broker, request_id="valid", operation="read_authority")
        r = broker.request("malformed")
        record("malformed_does_not_inherit_request_id", r["status"] == "rejected" and r["request_id"] is None, r)
        finish = dict(request_id="end", operation="finish", diagnosis="unresolved", repair="unresolved", explanation="Parser test only; no diagnostic or repair effect claimed.")
        first = send(broker, **finish)
        second = send(broker, **finish)
        record("terminal_identical_retry_receipt_only", first["status"] == second["status"] == "ok" and second["cached"] and
               first["result"] == second["result"] and broker.state["finished"], second)
        r = send(broker, request_id="new-after-end", operation="read_authority")
        record("terminal_new_request_rejected", r["status"] == "rejected" and r["error"] == "Episode already finished", r)
        record("no_scientific_program_executed", all(not json.loads((p / "state.json").read_text())["runs"] for p in cases), {})
    finally:
        output.mkdir(parents=True, exist_ok=True)
        for p in cases:
            h.archive(p, output / p.name)
        h.dump(output / "results.json", {"status": "pass" if len(checks) == 7 and all(c["pass"] for c in checks) else "fail",
                                        "checks": checks, "cases": [str(p) for p in cases],
                                        "broker_sha256": b.sha(h.STUDY / "broker.py"),
                                        "baseline_sha256": b.sha(h.STUDY / "baseline.py"),
                                        "producer_or_checker_executions": 0, "learned_contexts": 0})
    print(json.dumps({"status": "pass", "checks": len(checks), "output": str(output)}))


if __name__ == "__main__":
    main()
