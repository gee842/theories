#!/usr/bin/env python3
"""Compile a frozen copy of the four modules and record proof dependencies."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
MODULES = ["GenerativeCore", "BoundaryModels", "Depletion", "RootRealization"]
ALLOWED_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=180)


def main():
    toolchain = (ROOT / "lean-toolchain").read_text().strip()
    assert toolchain == "leanprover/lean4:v4.29.1"
    command_prefix = ["lean", "+" + toolchain]
    version = run(command_prefix + ["--version"], ROOT)
    version.check_returncode()
    assert "version 4.29.1," in version.stdout
    prefix = run(command_prefix + ["--print-prefix"], ROOT)
    prefix.check_returncode()
    compiler = Path(prefix.stdout.strip()) / "bin" / "lean"
    frozen = {name: (ROOT / (name + ".lean")).read_bytes() for name in MODULES}
    for name, source in frozen.items():
        text = source.decode()
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", text), name
        assert not re.search(r"^\s*(axiom|constant)\s", text, re.M), name
        imports = re.findall(r"^import\s+(.+)$", text, re.M)
        assert all(item in {"Std", "GenerativeCore"} for item in imports), imports

    results = []
    output_dir = ROOT / "verification"
    output_dir.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="generative-core-lean-") as temporary:
        build = Path(temporary)
        for name, source in frozen.items():
            (build / (name + ".lean")).write_bytes(source)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in MODULES:
            # Object files exist only in this temporary build; no stale local
            # object can stand in for the recorded source.
            command = [str(compiler), "-o", name + ".olean", name + ".lean"]
            result = run(command, build, env)
            log = output_dir / (name + ".txt")
            log.write_text(result.stdout)
            clean = "sorryAx" not in result.stdout and "warning:" not in result.stdout
            audits = re.findall(
                r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
                result.stdout)
            declared_audits = len(re.findall(r"^#print axioms ", frozen[name].decode(), re.M))
            axioms = sorted({a.strip() for _, group in audits
                             for a in group.split(",") if a.strip()})
            clean = clean and len(audits) == declared_audits and bool(audits)
            clean = clean and set(axioms).issubset(ALLOWED_AXIOMS)
            results.append({
                "module": name, "source_sha256": digest(frozen[name]),
                "command": ["lean", "-o", name + ".olean", name + ".lean"],
                "exit_code": result.returncode, "dependency_audits": len(audits),
                "audited_declarations": [theorem for theorem, _ in audits],
                "axioms": axioms, "clean_dependency_audit": clean,
                "output": "verification/" + log.name,
                "output_sha256": digest(log.read_bytes()),
            })
            if result.returncode or not clean:
                break

    unchanged = all((ROOT / (name + ".lean")).read_bytes() == frozen[name]
                    for name in MODULES)
    passed = (len(results) == len(MODULES) and unchanged and
              all(r["exit_code"] == 0 and r["clean_dependency_audit"] for r in results))
    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if passed else "failed", "lean_version": version.stdout.strip(),
        "compiler_binary": str(compiler), "compiler_sha256": digest(compiler.read_bytes()),
        "toolchain": toolchain, "toolchain_sha256": digest((ROOT / "lean-toolchain").read_bytes()),
        "checker_sha256": digest(Path(__file__).read_bytes()),
        "source_unchanged_during_check": unchanged,
        "fresh_temporary_build": True, "modules": results,
        "audited_declarations": sum(r["dependency_audits"] for r in results),
        "scope": "Discrete labelled relations; exact finite existential traces and their "
                 "representations; conditional natural-reserve obstruction; authored supported "
                 "feedback witness and finite countermodels. No probability, physical law, "
                 "observational policy, emergent learning, ethical or universal-reality validation.",
    }
    (ROOT / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "modules": len(results),
                      "audited_declarations": record["audited_declarations"],
                      "record": str(ROOT / "verification.json")}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
