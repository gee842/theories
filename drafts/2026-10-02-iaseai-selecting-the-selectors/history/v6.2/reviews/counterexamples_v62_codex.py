"""Reproduce the new V6.2 review counterexamples with Python's standard library.

Run from any directory: python3 /path/to/reviews/counterexamples_v62_codex.py
The two independent numerical audits import no manuscript model functions.
The reporting audit executes a deliberately changed checker in memory only.
No manuscript, register, or existing checker is edited.
"""
from pathlib import Path
import json
import math
import subprocess
import sys


def main():
    here = Path(__file__).resolve().parent
    results = {}
    for name, relative in (
        ("formal", "formal-audit/independent_audit.py"),
        ("systems", "systems-audit/audit_systems.py"),
    ):
        script = here / relative
        completed = subprocess.run(
            [sys.executable, str(script)], cwd=script.parent,
            text=True, capture_output=True,
        )
        (here / f"{name}-independent-run.log").write_text(
            completed.stdout + completed.stderr
        )
        if completed.returncode:
            raise RuntimeError(f"{name} audit failed; see its log")
        results[name] = {"exit_code": completed.returncode, "script": relative}
        print(f"{name}: independent counterexample assertions passed", flush=True)

    risk_examples = []
    for horizon in (100, 10000, 100000):
        log_survival = math.fsum(
            math.log1p(-0.5 / (t + 1)) for t in range(horizon)
        )
        risk_examples.append({"periods": horizon, "survival": math.exp(log_survival)})
    assert all(b["survival"] < a["survival"] for a, b in zip(risk_examples, risk_examples[1:]))
    results["falling_nonsummable_hazard"] = {
        "hazard": "h_t = 1/(2(t+1)), t >= 0",
        "proof": "sum h_t diverges and log(1-h_t) <= -h_t, so survival tends to zero",
        "finite_examples": risk_examples,
    }

    source = (here.parent / "checks_v62.py").read_text()
    original = "agree += ((rad < 1) == (a * b < mu * de))"
    if source.count(original) == 1:
        changed = source.replace(original, "agree += False")
        injected = subprocess.run(
            [sys.executable, "-c", changed, "FB"],
            text=True, capture_output=True,
        )
        assert "agreement 0/200000" in injected.stdout
        assert injected.returncode == 0
        (here / "harness-audit/injected-failure.log").write_text(
            injected.stdout + injected.stderr
        )
        results["failure_reporting"] = {
            "injected_agreements": 0, "comparisons": 200000,
            "exit_code": injected.returncode,
            "interpretation": "FB is diagnostic only; its displayed disagreement does not fail the runner",
        }
    else:
        results["failure_reporting"] = {
            "status": "skipped: checker has changed since the reviewed snapshot"
        }
    (here / "counterexamples-summary.json").write_text(json.dumps(results, indent=2) + "\n")
    print("Review counterexamples reproduced; see counterexamples-summary.json.")


if __name__ == "__main__":
    main()
