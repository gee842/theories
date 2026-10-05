#!/usr/bin/env python3
"""Compile the frozen finite interface afresh and audit every theorem."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "RecipientCorrection.lean"
ALLOWED_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=180)


def main():
    toolchain_bytes = (ROOT / "lean-toolchain").read_bytes()
    toolchain = toolchain_bytes.decode().strip()
    assert toolchain == "leanprover/lean4:v4.29.1"
    prefix_command = ["lean", "+" + toolchain]
    version = run(prefix_command + ["--version"], ROOT)
    version.check_returncode()
    assert "version 4.29.1," in version.stdout
    prefix = run(prefix_command + ["--print-prefix"], ROOT)
    prefix.check_returncode()
    compiler = Path(prefix.stdout.strip()) / "bin/lean"
    frozen = SOURCE.read_bytes()
    source = frozen.decode()
    assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", source)
    assert not re.search(r"^\s*(axiom|constant)\s", source, re.M)
    assert re.findall(r"^import\s+(.+)$", source, re.M) == ["Std"]
    declared = set(re.findall(r"^theorem\s+(\w+)", source, re.M))
    requested = re.findall(r"^#print axioms\s+([\w.]+)\s*$", source, re.M)
    requested_short = {name.rsplit(".", 1)[-1] for name in requested}
    assert declared == requested_short and len(declared) == len(requested)
    logs = ROOT / "verification"
    logs.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="recipient-correction-lean-") as temporary:
        build = Path(temporary)
        (build / SOURCE.name).write_bytes(frozen)
        env = dict(os.environ, LEAN_PATH=str(build))
        command = [str(compiler), "-o", "RecipientCorrection.olean", SOURCE.name]
        result = run(command, build, env)
    log = logs / "RecipientCorrection.txt"
    log.write_text(result.stdout)
    audits = re.findall(
        r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
        result.stdout)
    dependencies = sorted({axiom.strip() for _, group in audits
                           for axiom in group.split(",") if axiom.strip()})
    unchanged = SOURCE.read_bytes() == frozen
    clean = (result.returncode == 0 and "warning:" not in result.stdout
             and "sorryAx" not in result.stdout
             and [name for name, _ in audits] == requested
             and set(dependencies).issubset(ALLOWED_AXIOMS) and unchanged)
    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if clean else "failed",
        "toolchain": toolchain,
        "toolchain_sha256": sha(toolchain_bytes),
        "lean_version": version.stdout.strip(),
        "compiler_binary": str(compiler),
        "compiler_sha256": sha(compiler.read_bytes()),
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "source": SOURCE.name,
        "source_sha256": sha(frozen),
        "source_unchanged_during_check": unchanged,
        "fresh_temporary_build": True,
        "imports": ["Std"],
        "project_dependencies": [],
        "command": command,
        "exit_code": result.returncode,
        "clean_dependency_audit": clean,
        "audited_declarations": [name for name, _ in audits],
        "dependency_audits": len(audits),
        "axioms": dependencies,
        "output": str(log.relative_to(ROOT)),
        "output_sha256": sha(log.read_bytes()),
        "scope": "Independent deterministic finite information/payment interface: "
                 "four distinguishable exact controller states for two independent binary "
                 "target laws without new probes; packed context memory with noninterfering "
                 "writes; actual recipient receipt decoding versus private-credit alias; "
                 "paid observation/write feasibility, ledger, and sunk observation costs. "
                 "No stochastic producer refinement, inherited resource trace, full phase "
                 "budget, physical recipe derivation or ethical selection theorem.",
    }
    (ROOT / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"],
                      "audited_declarations": len(audits),
                      "axioms": dependencies,
                      "record": str(ROOT / "verification.json")}, indent=2))
    if not clean:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
