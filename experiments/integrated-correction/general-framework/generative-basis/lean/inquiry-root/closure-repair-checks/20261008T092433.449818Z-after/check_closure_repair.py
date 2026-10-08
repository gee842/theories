#!/usr/bin/env python3
"""Freeze and compare the actual affected closure before/after a proof repair.

The older integration receipt supplies source locations, not current validity.
Both runs compile current frozen sources with no repository olean reuse.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[5]
TARGETS = {"GenerativeClosure", "CoreTreeRearticulation", "WholeTheoryDischarge"}
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")
OLD = """    cases List.mem_cons.mp hr with
    | inl heq => exact heq ▸ hp
    | inr ht => exact hc r ht"""
NEW = """    cases hr with
    | head => exact hp
    | tail _ ht => exact hc r ht"""


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    result = subprocess.run(command, cwd=cwd, env=env, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            timeout=60)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", type=Path)
    args = parser.parse_args()
    stage = "after" if args.baseline else "before"
    old_receipt = json.loads((HERE / "core-tree-verification.json").read_text())
    paths = [(m["module"], REPO / m["source"]) for m in old_receipt["modules"]]
    paths.append(("WholeTheoryDischarge", HERE / "WholeTheoryDischarge.lean"))
    assert len(paths) == 32 and len({m for m, _ in paths}) == 32
    frozen = {m: p.read_bytes() for m, p in paths}
    baseline = json.loads(args.baseline.read_text()) if args.baseline else None
    if baseline:
        assert baseline["stage"] == "before" and baseline["passed"]
        before_dir = args.baseline.resolve().parent
        for module, _ in paths:
            previous = (before_dir / (module + ".lean")).read_bytes()
            assert sha(previous) == baseline["sources"][module]["sha256"]
            if module == "GenerativeClosure":
                assert previous.decode().count(OLD) == 1
                assert frozen[module].decode() == previous.decode().replace(OLD, NEW)
            else:
                assert frozen[module] == previous, "Concurrent source change: " + module
    else:
        assert frozen["GenerativeClosure"].decode().count(OLD) == 1

    toolchain = (HERE.parent / "lean-toolchain").read_text().strip()
    command = ["lean", "+" + toolchain]
    version = run(command + ["--version"], HERE)
    assert version.returncode == 0 and "version 4.29.1," in version.stdout
    prefix = run(command + ["--print-prefix"], HERE)
    assert prefix.returncode == 0
    compiler = Path(prefix.stdout.strip()) / "bin/lean"
    build = HERE / "closure-repair-checks" / (datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ") + "-" + stage)
    build.mkdir(parents=True)
    (build / "lean-toolchain").write_text(toolchain + "\n")
    (build / Path(__file__).name).write_bytes(Path(__file__).read_bytes())
    for module, _ in paths:
        (build / (module + ".lean")).write_bytes(frozen[module])
    results = {}
    for module, _ in paths:
        code = frozen[module].decode()
        result = run([str(compiler), "-o", module + ".olean", module + ".lean"],
                     build, dict(os.environ, LEAN_PATH=str(build)))
        (build / (module + ".log")).write_text(result.stdout)
        assert result.returncode == 0, module + "\n" + result.stdout
        assert "warning:" not in result.stdout, module + "\n" + result.stdout
        requests = re.findall(r"^#print axioms (\S+)", code, re.M)
        audits = {name: [x.strip() for x in raw.split(",") if x.strip()]
                  for name, raw in AUDIT.findall(result.stdout)}
        # Some historical requests use names relative to their namespace.
        assert len(audits) == len(requests), (module, len(audits), len(requests))
        for requested, actual in zip(requests, audits):
            assert actual == requested or actual.endswith("." + requested), (requested, actual)
        assert all(set(a) <= {"propext", "Quot.sound", "Classical.choice"} for a in audits.values())
        if baseline:
            before_audits = baseline["modules"][module]["audits"]
            assert audits.keys() == before_audits.keys(), module
            assert all(set(a) <= set(before_audits[n]) for n, a in audits.items()), module
            if module in TARGETS:
                assert all(not a for a in audits.values()), (module, audits)
        results[module] = {"audits": audits, "log_sha256": sha(result.stdout.encode())}
        print(module + ": " + str(len(audits)) + " audits", flush=True)
    assert all(p.read_bytes() == frozen[m] for m, p in paths), "Source changed during build"
    all_audits = [a for m in results.values() for a in m["audits"].values()]
    target_audits = [a for m in TARGETS for a in results[m]["audits"].values()]
    reductions = []
    if baseline:
        for module in results:
            for name, deps in results[module]["audits"].items():
                prior = baseline["modules"][module]["audits"][name]
                if prior != deps:
                    reductions.append({"module": module, "declaration": name,
                                       "before": prior, "after": deps})
        assert len(reductions) == 9
        assert all(r["before"] == ["propext"] and not r["after"] for r in reductions)
        assert len(target_audits) == 24 and all(not a for a in target_audits)
    receipt = {"passed": True, "stage": stage, "checked_at_utc": datetime.now(timezone.utc).isoformat(),
               "lean_version": version.stdout.strip(), "compiler_sha256": sha(compiler.read_bytes()),
               "checker_sha256": sha(Path(__file__).read_bytes()),
               "sources": {m: {"path": str(p.relative_to(REPO)), "sha256": sha(frozen[m])} for m, p in paths},
               "modules": results, "module_count": len(results), "audit_count": len(all_audits),
               "empty_audits": sum(not a for a in all_audits),
               "standard_dependency_audits": sum(bool(a) for a in all_audits),
               "target_audits": len(target_audits), "target_empty_audits": sum(not a for a in target_audits),
               "new_theorems": 0, "dependency_reductions": reductions,
               "baseline_receipt": str(args.baseline.resolve().relative_to(REPO)) if baseline else None,
               "baseline_receipt_sha256": sha(args.baseline.read_bytes()) if baseline else None,
               "scope": "One proof-body repair; unchanged statements, definitions, rules and premises. No proof of actual foundational process law.",
               "logical_basis": "Lean 4.29.1 type theory remains the checking framework; non-target standard dependencies are reported separately.",
               "run_directory": str(build.relative_to(REPO))}
    serialized = json.dumps(receipt, indent=2) + "\n"
    (build / "receipt.json").write_text(serialized)
    (HERE / ("closure-repair-" + stage + ".json")).write_text(serialized)
    print(json.dumps({k: receipt[k] for k in ("passed", "stage", "module_count", "audit_count", "empty_audits", "standard_dependency_audits", "target_empty_audits", "run_directory")}))


if __name__ == "__main__":
    main()
