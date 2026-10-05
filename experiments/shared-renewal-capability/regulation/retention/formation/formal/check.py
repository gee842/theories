#!/usr/bin/env python3
"""Compile frozen Lean sources in a fresh build and audit every new theorem."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[5]
CORE = REPO / "experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean"
SOURCES = {
    "GenerativeCore": CORE,
    "FormedSelection": ROOT / "FormedSelection.lean",
    "FormationRoot": ROOT / "FormationRoot.lean",
}
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
    command_prefix = ["lean", "+" + toolchain]
    version = run(command_prefix + ["--version"], ROOT)
    version.check_returncode()
    assert "version 4.29.1," in version.stdout
    prefix = run(command_prefix + ["--print-prefix"], ROOT)
    prefix.check_returncode()
    compiler = Path(prefix.stdout.strip()) / "bin/lean"
    frozen = {name: path.read_bytes() for name, path in SOURCES.items()}
    declared = {}
    requested_audits = {}
    for name, source in frozen.items():
        source_text = source.decode()
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", source_text), name
        assert not re.search(r"^\s*(axiom|constant)\s", source_text, re.M), name
        imports = re.findall(r"^import\s+(.+)$", source_text, re.M)
        assert set(imports).issubset({"Std", "GenerativeCore", "FormedSelection"}), imports
        declared[name] = set(re.findall(r"^theorem\s+(\w+)", source_text, re.M))
        requested = {qualified.rsplit(".", 1)[-1] for qualified in
                     re.findall(r"^#print axioms\s+([\w.]+)\s*$", source_text, re.M)}
        requested_audits[name] = requested
        if name == "GenerativeCore":
            assert requested and requested.issubset(declared[name])
        else:
            assert declared[name] == requested, (name, declared[name] ^ requested)

    results = []
    logs = ROOT / "verification"
    logs.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="formed-variant-selection-lean-") as temporary:
        build = Path(temporary)
        for name, source in frozen.items():
            (build / (name + ".lean")).write_bytes(source)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name, path in SOURCES.items():
            command = [str(compiler), "-o", name + ".olean", name + ".lean"]
            result = run(command, build, env)
            log = logs / (name + ".txt")
            log.write_text(result.stdout)
            audits = re.findall(
                r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
                result.stdout)
            audited_short = {name.rsplit(".", 1)[-1] for name, _ in audits}
            dependencies = sorted({axiom.strip() for _, group in audits
                                   for axiom in group.split(",") if axiom.strip()})
            clean = (result.returncode == 0 and "warning:" not in result.stdout
                     and "sorryAx" not in result.stdout
                     and audited_short == requested_audits[name]
                     and len(audits) == len(requested_audits[name])
                     and set(dependencies).issubset(ALLOWED_AXIOMS))
            results.append({
                "module": name,
                "source": str(path.relative_to(REPO)),
                "source_sha256": sha(frozen[name]),
                "role": "existing root dependency" if name == "GenerativeCore" else "new formalization",
                "command": command,
                "exit_code": result.returncode,
                "clean_dependency_audit": clean,
                "audited_declarations": [qualified for qualified, _ in audits],
                "dependency_audits": len(audits),
                "axioms": dependencies,
                "output": str(log.relative_to(ROOT)),
                "output_sha256": sha(log.read_bytes()),
            })
            if not clean:
                break

    unchanged = all(path.read_bytes() == frozen[name] for name, path in SOURCES.items())
    passed = (len(results) == len(SOURCES) and unchanged
              and all(item["clean_dependency_audit"] for item in results))
    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if passed else "failed",
        "toolchain": toolchain,
        "toolchain_sha256": sha(toolchain_bytes),
        "lean_version": version.stdout.strip(),
        "compiler_binary": str(compiler),
        "compiler_sha256": sha(compiler.read_bytes()),
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "source_unchanged_during_check": unchanged,
        "fresh_temporary_build": True,
        "project_objects_only_from_frozen_sources": True,
        "modules": results,
        "new_audited_declarations": sum(item["dependency_audits"] for item in results
                                        if item["role"] == "new formalization"),
        "scope": "Sixteen enabled discrete events with formed A/H variants, one paid resident "
                 "site and shared/local fuel; arbitrary-path material validity, total and common "
                 "fuel ledgers, copy and event budgets, three-unit and mixed four-unit bootstrap bounds, "
                 "type-specific formation ancestry, paid witness and repaired-site inheritance "
                 "counterexample; no-H-local-copy invariant before resident wear; exact trace "
                 "transport into the original relational generative core. No stochastic rates, "
                 "numerical probabilities, selection expectation, CTMC-to-Lean refinement, "
                 "empirical chemistry, learning or universal explanatory sufficiency.",
    }
    (ROOT / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "modules": len(results),
                      "new_audited_declarations": record["new_audited_declarations"],
                      "record": str(ROOT / "verification.json")}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
