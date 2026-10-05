#!/usr/bin/env python3
"""Compile the frozen ledger and typed refinement without repository build caches.

Run from any directory with the pinned Lean 4.29.1 toolchain installed.
Only typed-* execution records beside this script are written.
"""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parent
EXPECTED_LEDGER = "1c78c6dae53bc9b7c15ae3a24a63d83558d585fa07a4c402c25c571229514e74"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(args, env=None):
    return subprocess.run(args, cwd=ROOT, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def main():
    assert sha(ROOT / "RenewalLedger.lean") == EXPECTED_LEDGER, "Frozen ledger changed"
    version = run(["lean", "--version"])
    version.check_returncode()
    prefix = run(["lean", "--print-prefix"])
    prefix.check_returncode()
    compiler = Path(prefix.stdout.strip()) / "bin" / "lean"
    assert "version 4.29.1," in version.stdout, "Wrong Lean version"
    source_text = (ROOT / "TypedRenewal.lean").read_text()
    checked_at = datetime.now(timezone.utc).isoformat()
    with tempfile.TemporaryDirectory(prefix="typed-renewal-lean-") as tmp:
        dependency = Path(tmp) / "RenewalLedger.olean"
        dependency_command = ["lean", "-o", str(dependency), "RenewalLedger.lean"]
        dep = run(dependency_command)
        (ROOT / "typed-dependency-output.txt").write_text(dep.stdout)
        dep.check_returncode()
        env = dict(os.environ, LEAN_PATH=tmp)
        typed_command = ["lean", "TypedRenewal.lean"]
        result = run(typed_command, env)
        (ROOT / "typed-lean-output.txt").write_text(result.stdout)
        record = {
            "checked_at_utc": checked_at,
            "working_directory": str(ROOT),
            "dependency_command": dependency_command,
            "dependency_exit_code": dep.returncode,
            "command": typed_command,
            "environment_override": {"LEAN_PATH": tmp},
            "lean_version": version.stdout.strip(),
            "compiler_binary": str(compiler),
            "compiler_binary_sha256": sha(compiler),
            "exit_code": result.returncode,
            "source_sha256": sha(ROOT / "TypedRenewal.lean"),
            "ledger_source_sha256": sha(ROOT / "RenewalLedger.lean"),
            "imported_olean_sha256": sha(dependency),
            "toolchain_sha256": sha(ROOT / "lean-toolchain"),
            "checker_sha256": sha(__file__),
            "protocol_sha256": sha(ROOT.parent / "paid-access" / "PROTOCOL.md"),
            "dependency_output_sha256": sha(ROOT / "typed-dependency-output.txt"),
            "output_sha256": sha(ROOT / "typed-lean-output.txt"),
            "contains_sorry_token": bool(re.search(r"\bsorry\b", source_text)),
            "contains_custom_axiom_declaration": bool(re.search(r"^\s*axiom\s", source_text, re.M)),
            "contains_native_decide": bool(re.search(r"\bnative_decide\b", source_text)),
            "output_contains_sorryAx": "sorryAx" in result.stdout,
            "scope": (
                "Concrete two-type reaction stoichiometry, enabled steps and traces; "
                "proved one-way projection to the frozen pooled ledger; bare obstruction, "
                "conditional six-capture turnover bound and exact loss-budget consequence. "
                "No original-carrier tags, typed positive path, kinetic lumping, CTMC "
                "enumerator equivalence, probability certification or physical calibration."
            ),
            "temporary_dependency_removed_after_check": True,
        }
        (ROOT / "typed-lean-verification.json").write_text(json.dumps(record, indent=2) + "\n")
        result.check_returncode()
        assert not record["contains_sorry_token"]
        assert not record["contains_custom_axiom_declaration"]
        assert not record["contains_native_decide"]
        assert not record["output_contains_sorryAx"]
        print(json.dumps({"exit_code": result.returncode,
                          "source_sha256": record["source_sha256"],
                          "compiler_binary_sha256": record["compiler_binary_sha256"],
                          "record": str(ROOT / "typed-lean-verification.json")}, indent=2))


if __name__ == "__main__":
    main()
