#!/usr/bin/env python3
"""Freeze, compile and audit the Std-only rational market formalization.

Uses an already installed compiler. Does not install dependencies or toolchains.
Set MARKET_LEAN to a Lean 4.29.1 binary if it is not in the normal elan directory.
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
SOURCE = ROOT / "MarketGenerativity.lean"
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
    default = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
    compiler = Path(os.environ.get("MARKET_LEAN", str(default))).resolve()
    if not compiler.is_file():
        raise SystemExit("Lean 4.29.1 is not installed at the default path. "
                         "Set MARKET_LEAN to its binary; no installation was attempted.")
    version = run([str(compiler), "--version"], ROOT)
    version.check_returncode()
    assert "version 4.29.1," in version.stdout, version.stdout
    source_bytes = SOURCE.read_bytes()
    source = source_bytes.decode()
    assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", source)
    assert not re.search(r"^\s*(axiom|constant)\s", source, re.M)
    assert re.findall(r"^import\s+(.+)$", source, re.M) == ["Std"]
    declared = re.findall(r"^theorem\s+(\w+)", source, re.M)
    requested = re.findall(r"^#print axioms MarketGenerativity\.([\w]+)\s*$", source, re.M)
    assert len(set(declared)) == len(declared)
    assert set(declared) == set(requested) and len(declared) == len(requested)
    with tempfile.TemporaryDirectory(prefix="market-generativity-lean-") as temporary:
        build = Path(temporary)
        (build / SOURCE.name).write_bytes(source_bytes)
        env = dict(os.environ, LEAN_PATH=str(build))
        command = [str(compiler), "-o", "MarketGenerativity.olean", SOURCE.name]
        result = run(command, build, env)
    logs = ROOT / "verification"
    logs.mkdir(exist_ok=True)
    log = logs / "MarketGenerativity.txt"
    log.write_text(result.stdout)
    audits = re.findall(
        r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
        result.stdout)
    audited = [qualified.rsplit(".", 1)[-1] for qualified, _ in audits]
    dependencies = sorted({axiom.strip() for _, group in audits
                           for axiom in group.split(",") if axiom.strip()})
    unchanged = SOURCE.read_bytes() == source_bytes
    clean = (result.returncode == 0 and "warning:" not in result.stdout
             and "sorryAx" not in result.stdout and unchanged
             and set(audited) == set(declared) and len(audited) == len(declared)
             and set(dependencies).issubset(ALLOWED_AXIOMS))
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
        "source_sha256": sha(source_bytes),
        "source_unchanged_during_check": unchanged,
        "fresh_temporary_build": True,
        "imports": ["Std"],
        "command": command,
        "exit_code": result.returncode,
        "clean_dependency_audit": clean,
        "audited_declarations": [qualified for qualified, _ in audits],
        "new_audited_declarations": len(audits),
        "axioms": dependencies,
        "output": str(log.relative_to(ROOT)),
        "output_sha256": sha(log.read_bytes()),
        "scope": (
            "Rational profit-gap and full uses-of-revenue identities; pre-receipt "
            "correction payment, capped reserve/overflow accounting; derived one-step "
            "share, accountability, paid-influence and componentwise support bounds; "
            "generic finite-support rectangle closure and arbitrary-time invariant "
            "for any upper-bounded disturbance history; essential-support guard, "
            "absorbing failure and safe-history nonfailure; exact numerical certificate "
            "and interval recovery collar; finite degeneration, capture, liquidity, "
            "excluded-recipient and zero-entry witnesses. The authorized policy, "
            "charges, causal parameters, support identities/floors and error bounds "
            "are premises. No real convergence, low-basin attractor, empirical "
            "validation, origin of institutions or Python-to-Lean refinement theorem."
        ),
    }
    (ROOT / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"],
                      "new_audited_declarations": len(audits),
                      "record": str(ROOT / "verification.json")}, indent=2))
    if not clean:
        print(result.stdout)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
