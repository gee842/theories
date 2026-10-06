#!/usr/bin/env python3
"""Read-only fault injection against the delivery consumer; never runs Lean.

Each case calls the actual consumer main() with only digest() faulted in memory.
Its report write is intercepted, so no historical, live, or archived proof file
is altered. Only this check's own result file is written after all cases finish.
"""

from contextlib import redirect_stdout
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
from unittest.mock import patch


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CONSUMER = HERE / "HUIGEN-CHECK.py"
CONSUMER_REPORT = HERE / "HUIGEN-CHECKS.json"
LEAN = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root"
REVALIDATION = LEAN / "revalidation"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    consumer_bytes = CONSUMER.read_bytes()
    namespace = {"__name__": "huigen_receipt_fault_review", "__file__": str(CONSUMER)}
    exec(compile(consumer_bytes, str(CONSUMER), "exec"), namespace)
    original_digest = namespace["digest"]
    current_path = REVALIDATION / "verification.json"
    current = json.loads(current_path.read_text())
    historical_path = LEAN / "verification.json"
    run_record = REVALIDATION / current["run_record"]
    bindings = [CONSUMER, historical_path, current_path, run_record,
                run_record.parent / "original-checker-verification.json",
                REVALIDATION / "check.py"]
    source = LEAN.parent / "Depletion.lean"
    source_key = str(source.relative_to(ROOT))
    module = next(m for m in current["modules"] if m["module"] == "Depletion")
    cases = [
        ("baseline", None),
        ("current_source_digest", source),
        ("historical_log_digest", LEAN / "verification/Depletion.txt"),
        ("archived_source_digest", REVALIDATION / current["snapshots"][source_key]),
        ("archived_log_digest", REVALIDATION / module["output"]),
        ("historical_receipt_digest", historical_path),
    ]
    watched = set(bindings + [CONSUMER_REPORT, Path(__file__)])
    watched.update(ROOT / key for key in current["inputs"])
    watched.update(ROOT / key for key in current["preserved_historical"])
    watched.update(REVALIDATION / key for key in current["artifacts"])
    before = {path: digest(path) for path in watched}
    results = []

    for name, fault in cases:
        captured = {}
        fault_hits = [0]

        def faulted_digest(path):
            if fault is not None and Path(path).resolve() == fault.resolve():
                fault_hits[0] += 1
                return "0" * 64
            return original_digest(path)

        def intercept_write(path, data, *args, **kwargs):
            if Path(path).resolve() != CONSUMER_REPORT.resolve():
                raise RuntimeError("Unexpected consumer write: " + str(path))
            captured["report"] = json.loads(data)
            return len(data)

        namespace["digest"] = faulted_digest
        exit_code = 0
        exception = None
        with patch.object(Path, "write_text", intercept_write), redirect_stdout(io.StringIO()):
            try:
                namespace["main"]()
            except SystemExit as exc:
                exit_code = exc.code
            except Exception as exc:
                exit_code = 1
                exception = {"type": type(exc).__name__, "message": str(exc)}
        report = captured.get("report")
        status = report["status"] if report else None
        current_status = report["current_proof_receipt_consistency"]["status"] if report else None
        mismatches = report["current_proof_receipt_consistency"]["mismatches"] if report else None
        if name == "baseline":
            expected = (exit_code == 0 and exception is None and status == "pass"
                        and current_status == "matches" and mismatches == [])
        elif name == "current_source_digest":
            expected = (exit_code == 1 and exception is None and status == "partial"
                        and current_status == "stale" and len(mismatches or []) == 1
                        and mismatches[0]["path"] == source_key)
        else:
            expected = (exit_code == 1 and exception is not None
                        and exception["type"] == "AssertionError" and report is None)
        expected = expected and (fault is None or fault_hits[0] > 0)
        results.append({
            "case": name,
            "expected_behavior_observed": expected,
            "faulted_digest_calls": fault_hits[0],
            "consumer_exit_code": exit_code,
            "intercepted_report_status": status,
            "current_proof_status": current_status,
            "current_source_mismatch_count": len(mismatches) if mismatches is not None else None,
            "exception": exception,
        })

    namespace["digest"] = original_digest
    unchanged = before == {path: digest(path) for path in watched}
    passed = unchanged and all(case["expected_behavior_observed"] for case in results)
    result = {
        "schema_version": 1,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if passed else "failed",
        "checker_sha256": digest(Path(__file__)),
        "bound_artifacts": {str(path.relative_to(ROOT)): before[path] for path in bindings},
        "tests": results,
        "watched_files_unchanged": unchanged,
        "watched_file_count": len(watched),
        "proof_compilations": 0,
        "proof_or_consumer_report_writes": 0,
        "scope": "Consumer integrity and failure behavior under in-memory digest faults. "
                 "Historical and archived corruption must be rejected; a later live source "
                 "change must produce a stale current receipt, partial report and exit 1. "
                 "No proof compilation, physical file corruption, adversarial security claim, "
                 "new theorem or philosophical necessity result.",
    }
    (HERE / "HUIGEN-RECEIPT-CHECKS.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "cases": len(results),
                      "expected": sum(case["expected_behavior_observed"] for case in results),
                      "watched_files_unchanged": unchanged, "proof_compilations": 0}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
