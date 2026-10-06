#!/usr/bin/env python3
"""Verify the integrated model from frozen sources without new axiom dependencies."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
HISTORY = ROOT / "verification-history/2026-10-06-before-model-integration"
MODULE_PATHS = {
    "GenerativeCore": "GenerativeCore.lean",
    "BoundaryModels": "BoundaryModels.lean",
    "Depletion": "Depletion.lean",
    "RootRealization": "RootRealization.lean",
    "ProductTower": "deeper/ProductTower.lean",
    "DynamicUnderdetermination": "deeper/DynamicUnderdetermination.lean",
    "GeneratedPaths": "deeper/GeneratedPaths.lean",
    "HistoryRealization": "deeper/HistoryRealization.lean",
    "DynamicSymmetry": "deeper/DynamicSymmetry.lean",
    "DynamicConsequences": "deeper/DynamicConsequences.lean",
    "DynamicClassification": "deeper/DynamicClassification.lean",
    "GenerativeModel": "GenerativeModel.lean",
}
NEW_MODULES = {"DynamicConsequences", "DynamicClassification", "GenerativeModel"}
AUDIT_PATTERN = re.compile(
    r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])"
)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=180)


def parse_audits(output):
    return [(name, sorted(a.strip() for a in group.split(",") if a.strip()))
            for name, group in AUDIT_PATTERN.findall(output)]


def main():
    checker_bytes = Path(__file__).read_bytes()
    toolchain_bytes = (ROOT / "lean-toolchain").read_bytes()
    toolchain = toolchain_bytes.decode().strip()
    assert toolchain == "leanprover/lean4:v4.29.1"
    prefix = ["lean", "+" + toolchain]
    version = run(prefix + ["--version"], ROOT)
    version.check_returncode()
    assert "version 4.29.1," in version.stdout
    compiler_prefix = run(prefix + ["--print-prefix"], ROOT)
    compiler_prefix.check_returncode()
    compiler = Path(compiler_prefix.stdout.strip()) / "bin" / "lean"

    # Only the exact original declarations may retain their recorded dependencies.
    history_manifest = json.loads((HISTORY / "manifest.json").read_text())
    for path, item in history_manifest["files"].items():
        assert digest((HISTORY / path).read_bytes()) == item["sha256"], path
    baseline = json.loads((HISTORY / "verification.json").read_text())
    allowed = {}
    for module in baseline["modules"]:
        log = HISTORY / module["output"]
        assert digest(log.read_bytes()) == module["output_sha256"], log
        for name, dependencies in parse_audits(log.read_text()):
            allowed[name] = set(dependencies)

    sources = {name: ROOT / path for name, path in MODULE_PATHS.items()}
    frozen = {name: path.read_bytes() for name, path in sources.items()}
    for module in baseline["modules"]:
        assert digest(frozen[module["module"]]) == module["source_sha256"], module["module"]

    seen = set()
    for name, source in frozen.items():
        text = source.decode()
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", text), name
        assert not re.search(r"^\s*(axiom|constant|opaque)\s", text, re.M), name
        imports = re.findall(r"^import\s+(.+)$", text, re.M)
        assert all(item == "Std" or item in seen for item in imports), (name, imports)
        seen.add(name)
        if name in NEW_MODULES:
            declarations = re.findall(r"^theorem\s+(\w+)", text, re.M)
            requested = re.findall(r"^#print axioms (\S+)", text, re.M)
            assert len(declarations) == len(set(declarations)), name
            assert [x.rsplit(".", 1)[-1] for x in requested] == declarations, name

    results = []
    output_dir = ROOT / "verification"
    output_dir.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="generative-model-lean-") as temporary:
        build = Path(temporary)
        for name, source in frozen.items():
            (build / (name + ".lean")).write_bytes(source)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in MODULE_PATHS:
            command = [str(compiler), "-o", name + ".olean", name + ".lean"]
            result = run(command, build, env)
            log = output_dir / (name + ".txt")
            log.write_text(result.stdout)
            audits = parse_audits(result.stdout)
            requested = re.findall(r"^#print axioms (\S+)", frozen[name].decode(), re.M)
            matches = (len(audits) == len(requested) and bool(audits) and
                       all(actual == expected or actual.endswith("." + expected)
                           for (actual, _), expected in zip(audits, requested)))
            additions = {declaration: sorted(set(deps) - allowed.get(declaration, set()))
                         for declaration, deps in audits
                         if set(deps) - allowed.get(declaration, set())}
            clean = (result.returncode == 0 and "sorryAx" not in result.stdout
                     and "warning:" not in result.stdout and matches and not additions)
            results.append({
                "module": name, "source": MODULE_PATHS[name],
                "source_sha256": digest(frozen[name]), "command": command,
                "exit_code": result.returncode, "dependency_audits": len(audits),
                "audited_declarations": [declaration for declaration, _ in audits],
                "axioms": sorted({a for _, deps in audits for a in deps}),
                "axioms_by_declaration": dict(audits),
                "added_axiom_dependencies": additions,
                "clean_dependency_audit": clean,
                "output": "verification/" + log.name,
                "output_sha256": digest(log.read_bytes()),
            })
            if not clean:
                print(result.stdout)
                break

    unchanged = all(path.read_bytes() == frozen[name] for name, path in sources.items())
    checker_unchanged = Path(__file__).read_bytes() == checker_bytes
    history_unchanged = all(digest((HISTORY / path).read_bytes()) == item["sha256"]
                            for path, item in history_manifest["files"].items())
    passed = (len(results) == len(MODULE_PATHS) and unchanged and checker_unchanged
              and history_unchanged and
              all(r["clean_dependency_audit"] for r in results))
    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if passed else "failed",
        "lean_version": version.stdout.strip(),
        "compiler_binary": str(compiler), "compiler_sha256": digest(compiler.read_bytes()),
        "toolchain": toolchain, "toolchain_sha256": digest(toolchain_bytes),
        "checker_sha256": digest(checker_bytes),
        "checker_unchanged_during_check": checker_unchanged,
        "historical_evidence_hashes_match": history_unchanged,
        "source_unchanged_during_check": unchanged, "fresh_temporary_build": True,
        "local_precompiled_imports_used": False,
        "axiom_policy": "No new declared axiom dependencies; every new/deeper audit empty. "
                        "Only exact original declarations may retain recorded dependencies.",
        "original_verification": str((HISTORY / "verification.json").relative_to(ROOT)),
        "modules": results,
        "audited_declarations": sum(r["dependency_audits"] for r in results),
        "new_audited_declarations": sum(r["dependency_audits"] for r in results
                                        if r["module"] in NEW_MODULES),
        "new_axiom_dependencies": sorted({a for r in results
                                          for deps in r["added_axiom_dependencies"].values()
                                          for a in deps}),
        "scope": "Existing Process/Trace core and historical realizations, deeper closure/history "
                 "results, exact Boolean classification, endpoint-history identification and "
                 "feasible-word counterexample under synchronous composition. No added primitive "
                 "event law or asserted physical/ethical premise. Not complete V7.3 dynamics "
                 "or assumption-free foundations.",
    }
    (ROOT / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "modules": len(results),
                      "audited_declarations": record["audited_declarations"],
                      "new_audited_declarations": record["new_audited_declarations"],
                      "new_axiom_dependencies": record["new_axiom_dependencies"],
                      "record": str(ROOT / "verification.json")}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
