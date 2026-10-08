#!/usr/bin/env python3
"""Check explanatory-resumption claims and their explicit import closure in isolation.

Only this document's scope is rechecked. Existing project build artifacts and
other sessions' receipts are not used or rewritten. Keep immutable source/log
snapshots and a receipt; disposable compiler products stay outside the repo.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
LEAN_ROOT = HERE.parent
ROOT = next(p for p in HERE.parents if (p / "RESEARCH.md").is_file())
MODULES = [
    (LEAN_ROOT / "GenerativeCore.lean", 18),
    (HERE / "HistoryRealization.lean", 7),
    (HERE / "ExplanatoryNecessity.lean", 17),
    (HERE / "ExplanatoryStructure.lean", 17),
    (HERE / "ExplanatoryUniqueness.lean", 15),
    (HERE / "DynamicUnderdetermination.lean", 9),
    (HERE / "RelationalDynamics.lean", 13),
    (HERE / "ExplanatoryBranching.lean", 18),
    (HERE / "ExplanatoryUniversality.lean", 13),
    (HERE / "ExplanatoryJoining.lean", 23),
    (HERE / "ExplanatoryLocalUnits.lean", 31),
    (HERE / "ExplanatoryJoiningContexts.lean", 16),
    (HERE / "ExplanatoryJoiningBranches.lean", 16),
    (HERE / "ExplanatoryJoiningIncidence.lean", 9),
    (HERE / "ExplanatoryJoiningRefinement.lean", 11),
    (HERE / "ExplanatoryJoiningAnchors.lean", 12),
    (HERE / "ExplanatoryJoiningRegisters.lean", 11),
    (HERE / "ExplanatoryGranularity.lean", 10),
    (HERE / "ExplanatoryGranularityBoundary.lean", 13),
    (HERE / "ExplanatoryGuardedPrograms.lean", 11),
    (HERE / "ExplanatoryResiduals.lean", 13),
    (HERE / "ExplanatoryResumptionCases.lean", 11),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    out = HERE / "explanatory-resumption-checks" / stamp
    (out / "sources").mkdir(parents=True)
    toolchain = (LEAN_ROOT / "lean-toolchain").read_text().strip()
    env = dict(os.environ, ELAN_TOOLCHAIN=toolchain)
    lean = shutil.which("lean")
    if lean is None:
        raise SystemExit("Lean is required; no installation is performed.")
    version = subprocess.check_output([lean, "--version"], env=env, text=True).strip()
    receipt = {"checked_at_utc": stamp, "toolchain": toolchain,
               "compiler": version, "checker_sha256": sha(Path(__file__).read_bytes()),
               "scope": "Guarded finite recipes, coherent residuals and interruption boundaries; 279 inherited audits separate. All new formal claims checked; semantic guards do not imply acquired sensors or physical control.",
               "modules": [], "passed": False}
    with tempfile.TemporaryDirectory(prefix="ren-explanatory-resumption-") as scratch:
        build = Path(scratch)
        env["LEAN_PATH"] = str(build)
        for source, expected in MODULES:
            raw = source.read_bytes()
            (out / "sources" / source.name).write_bytes(raw)
            copied = build / source.name
            copied.write_bytes(raw)
            if (re.search(r"\b(sorry|admit|native_decide|unsafe)\b", raw.decode())
                    or re.search(r"^\s*(axiom|constant)\s", raw.decode(), re.M)):
                raise RuntimeError(f"Unexpected proof-hole/axiom token in {source.name}")
            proc = subprocess.run([lean, "-o", str(copied.with_suffix(".olean")), str(copied)],
                                  cwd=build, env=env, text=True, capture_output=True)
            log = proc.stdout + proc.stderr
            (out / (source.stem + ".log")).write_text(log)
            audits = re.findall(r"'([^']+)' does not depend on any axioms", log)
            dependencies = {name: [a.strip() for a in deps.split(",")]
                            for name, deps in re.findall(r"'([^']+)' depends on axioms: \[([^\]]+)\]", log)}
            allowed = {"propext", "Quot.sound", "Classical.choice"}
            ok = (proc.returncode == 0 and len(audits) + len(dependencies) == expected
                  and "warning:" not in log
                  and all(set(deps) <= allowed for deps in dependencies.values()))
            receipt["modules"].append({"source": str(source.relative_to(ROOT)),
                "sha256": sha(raw), "log_sha256": sha(log.encode()), "expected_audits": expected,
                "empty_axiom_audits": audits, "standard_axiom_audits": dependencies, "exit_code": proc.returncode,
                "source_unchanged_during_check": source.read_bytes() == raw,
                "passed": ok})
            if not ok:
                (out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
                raise SystemExit(log + f"\nCheck failed: {source.name}")
    receipt["passed"] = all(m["passed"] and m["source_unchanged_during_check"]
                            for m in receipt["modules"])
    receipt["total_empty_axiom_audits"] = sum(len(m["empty_axiom_audits"])
                                              for m in receipt["modules"])
    receipt["total_declaration_audits"] = sum(m["expected_audits"] for m in receipt["modules"])
    receipt["total_standard_axiom_audits"] = sum(len(m["standard_axiom_audits"]) for m in receipt["modules"])
    (out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    (HERE / "explanatory-resumption-verification.json").write_text(json.dumps({
        "receipt": str((out / "receipt.json").relative_to(ROOT)),
        "passed": receipt["passed"],
        "total_empty_axiom_audits": receipt["total_empty_axiom_audits"],
        "total_declaration_audits": receipt["total_declaration_audits"],
        "total_standard_axiom_audits": receipt["total_standard_axiom_audits"],
    }, indent=2) + "\n")
    print(json.dumps({"passed": receipt["passed"], "modules": len(MODULES),
                      "audits": receipt["total_declaration_audits"],
                      "empty_audits": receipt["total_empty_axiom_audits"],
                      "standard_dependency_audits": receipt["total_standard_axiom_audits"],
                      "receipt": str(out / "receipt.json")}))
    if not receipt["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
