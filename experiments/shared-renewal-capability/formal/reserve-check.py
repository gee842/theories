#!/usr/bin/env python3
"""Check the reserve-sensitive turnover lemma, preserving frozen inputs."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
FROZEN = {
    "RenewalLedger.lean": "1c78c6dae53bc9b7c15ae3a24a63d83558d585fa07a4c402c25c571229514e74",
    "TypedRenewal.lean": "73d0fea4f9fbf2a51560b850d608d2cc83a6ac8db80a8b7b2981f5f76a5a193c",
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(args, env=None):
    return subprocess.run(args, cwd=ROOT, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def main():
    for name, expected in FROZEN.items():
        assert sha(ROOT / name) == expected, f"Frozen source changed: {name}"
    version = run(["lean", "--version"])
    version.check_returncode()
    prefix = run(["lean", "--print-prefix"])
    prefix.check_returncode()
    compiler = Path(prefix.stdout.strip()) / "bin" / "lean"
    assert "version 4.29.1," in version.stdout
    source = ROOT / "ReserveTurnover.lean"
    text = source.read_text()
    with tempfile.TemporaryDirectory(prefix="reserve-turnover-lean-") as tmp:
        env = dict(os.environ, LEAN_PATH=tmp)
        deps = []
        for name, label in (("RenewalLedger", "ledger"), ("TypedRenewal", "typed")):
            obj = Path(tmp) / (name + ".olean")
            command = ["lean", "-o", str(obj), name + ".lean"]
            result = run(command, env)
            output = ROOT / ("reserve-" + label + "-dependency-output.txt")
            output.write_text(result.stdout)
            result.check_returncode()
            deps.append({"command": command, "exit_code": result.returncode,
                         "source_sha256": sha(ROOT / (name + ".lean")),
                         "imported_olean_sha256": sha(obj),
                         "output_file": output.name, "output_sha256": sha(output)})
        command = ["lean", "ReserveTurnover.lean"]
        result = run(command, env)
        output = ROOT / "reserve-lean-output.txt"
        output.write_text(result.stdout)
        record = {
            "checked_at_utc": datetime.now(timezone.utc).isoformat(),
            "working_directory": str(ROOT), "command": command,
            "environment_override": {"LEAN_PATH": tmp}, "dependencies": deps,
            "lean_version": version.stdout.strip(),
            "compiler_binary": str(compiler), "compiler_binary_sha256": sha(compiler),
            "exit_code": result.returncode, "source_sha256": sha(source),
            "toolchain_sha256": sha(ROOT / "lean-toolchain"),
            "checker_sha256": sha(__file__), "output_sha256": sha(output),
            "contains_sorry_token": bool(re.search(r"\bsorry\b", text)),
            "contains_custom_axiom_declaration": bool(re.search(r"^\s*axiom\s", text, re.M)),
            "contains_native_decide": bool(re.search(r"\bnative_decide\b", text)),
            "output_contains_sorryAx": "sorryAx" in result.stdout,
            "scope": "Typed enabled trace bound captures >= 6n + final work - initial work, "
                     "assuming restored total A and gates and at least n wears per role; "
                     "specialized to organizations with inherited reserve m and final reserve m'. "
                     "No original tags, positive path, stochastic rates or probability claim.",
            "temporary_dependencies_removed_after_check": True,
        }
        (ROOT / "reserve-lean-verification.json").write_text(json.dumps(record, indent=2) + "\n")
        result.check_returncode()
        for key in ("contains_sorry_token", "contains_custom_axiom_declaration",
                    "contains_native_decide", "output_contains_sorryAx"):
            assert not record[key], key
        print(json.dumps({"exit_code": result.returncode,
                          "source_sha256": record["source_sha256"],
                          "record": str(ROOT / "reserve-lean-verification.json")}, indent=2))


if __name__ == "__main__":
    main()
