#!/usr/bin/env python3
"""Fresh pinned build of actual prediction protocol and its independently authored observation bridge.

Only prediction-protocol-audit.txt is written. Other saved package records
and concurrent research are left unchanged.
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
NEW_MODULES = {"PredictionProtocolBridge", "PredictionProtocolObservation"}
REPO = ROOT.parents[5]
FORMATION = REPO / "experiments/shared-renewal-capability/regulation/retention/formation"
SOURCES = {
    "GenerativeCore": ROOT.parent / "GenerativeCore.lean",
    "Depletion": ROOT.parent / "Depletion.lean",
    "ResourceContinuation": ROOT.parent / "conditional/ResourceContinuation.lean",
    "ControllerRevision": ROOT / "ControllerRevision.lean",
    "ControlledRefinement": ROOT / "ControlledRefinement.lean",
    "ProtocolComposition": ROOT / "ProtocolComposition.lean",
    "FormedSelection": FORMATION / "formal/FormedSelection.lean",
    "SelectorRevision": FORMATION / "selectors/formal/SelectorRevision.lean",
    "UpdaterFormation": FORMATION / "selectors/updaters/formal/UpdaterFormation.lean",
    "PredictionAction": FORMATION / "selectors/updaters/prediction/formal/PredictionAction.lean",
    "PredictionProtocolBridge": ROOT / "PredictionProtocolBridge.lean",
    "PredictionProtocolObservation": ROOT / "PredictionProtocolObservation.lean",
}
ALLOWED_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=180)


def main():
    toolchain_bytes = (ROOT / "lean-toolchain").read_bytes()
    toolchain = toolchain_bytes.decode().strip()
    assert toolchain == "leanprover/lean4:v4.29.1"
    prefix = ["lean", "+" + toolchain]
    version = run(prefix + ["--version"], ROOT)
    version.check_returncode()
    assert "version 4.29.1," in version.stdout
    location = run(prefix + ["--print-prefix"], ROOT)
    location.check_returncode()
    compiler = Path(location.stdout.strip()) / "bin/lean"
    frozen = {name: source.read_bytes() for name, source in SOURCES.items()}
    for name, source in frozen.items():
        text = source.decode()
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", text), name
        assert not re.search(r"^\s*(axiom|constant)\s", text, re.M), name
        assert all(item in {"Std", *SOURCES}
                   for item in re.findall(r"^import\s+(.+)$", text, re.M)), name
        if name in NEW_MODULES:
            declarations = re.findall(r"^theorem\s+(\w+)", text, re.M)
            requested = re.findall(r"^#print axioms (\S+)", text, re.M)
            assert len(declarations) == len(set(declarations)), name
            assert len(requested) == len(declarations), name
            assert set(declarations) == {r.rsplit(".", 1)[-1] for r in requested}, name
    results = []
    with tempfile.TemporaryDirectory(prefix="prediction-protocol-lean-") as directory:
        build = Path(directory)
        for name, data in frozen.items():
            (build / (name + ".lean")).write_bytes(data)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in SOURCES:
            outcome = run([str(compiler), "-o", name + ".olean", name + ".lean"], build, env)
            audits = re.findall(
                r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
                outcome.stdout)
            requested = re.findall(r"^#print axioms (\S+)", frozen[name].decode(), re.M)
            names = [theorem for theorem, _ in audits]
            matched = len(names) == len(requested) and all(
                actual == wanted or actual.endswith("." + wanted)
                for actual, wanted in zip(names, requested))
            axioms = sorted({a.strip() for _, group in audits
                             for a in group.split(",") if a.strip()})
            clean = (bool(audits) and matched and set(axioms) <= ALLOWED_AXIOMS
                     and "sorryAx" not in outcome.stdout and "warning:" not in outcome.stdout)
            results.append({
                "module": name,
                "source": os.path.relpath(SOURCES[name], ROOT),
                "source_sha256": digest(frozen[name]),
                "exit_code": outcome.returncode,
                "audited_declarations": names,
                "dependency_audits": len(audits),
                "empty_axiom_audits": sum(not group.strip() for _, group in audits),
                "axioms": axioms,
                "clean_dependency_audit": clean,
                "compiler_output": outcome.stdout,
            })
            if outcome.returncode or not clean:
                break
    unchanged = all(path.read_bytes() == frozen[name] for name, path in SOURCES.items())
    passed = (len(results) == len(SOURCES) and unchanged
              and all(r["exit_code"] == 0 and r["clean_dependency_audit"] for r in results))
    new = [r for r in results if r["module"] in NEW_MODULES]
    report = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if passed else "failed",
        "lean_version": version.stdout.strip(),
        "compiler_binary": str(compiler),
        "compiler_sha256": digest(compiler.read_bytes()),
        "toolchain": toolchain,
        "toolchain_sha256": digest(toolchain_bytes),
        "checker_sha256": digest(Path(__file__).read_bytes()),
        "source_unchanged_during_check": unchanged,
        "fresh_temporary_build": True,
        "new_theorem_audits": sum(r["dependency_audits"] for r in new),
        "new_empty_axiom_audits": sum(r["empty_axiom_audits"] for r in new),
        "allowed_standard_axioms": sorted(ALLOWED_AXIOMS),
        "modules": results,
        "scope": "Concrete paid prediction trial protocol: independently stated macro "
                 "guards and arithmetic updates are equivalent to actual nonempty "
                 "first-return rent/work/write/finish blocks, retaining bounded actual "
                 "memory and whole/prefix resource ledgers. The endpoint-derived receipt "
                 "is proved equal to the consumed transient record, not a hidden truth "
                 "teacher or newly installed free sensor. Paid aborts remain outside "
                 "completed histories. Only deterministic-capture payable-write trials; "
                 "no full stochastic executable, skipped-write, reconstruction, "
                 "reversal/formation history, scheduling, probability or empirical claim.",
    }
    output = ROOT / "prediction-protocol-audit.txt"
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "new_theorem_audits": report["new_theorem_audits"],
                      "new_empty_axiom_audits": report["new_empty_axiom_audits"],
                      "output": str(output)}, indent=2))
    if not passed:
        for result in results:
            if result["exit_code"] or not result["clean_dependency_audit"]:
                print(result["compiler_output"])
        raise SystemExit(1)


if __name__ == "__main__":
    main()
