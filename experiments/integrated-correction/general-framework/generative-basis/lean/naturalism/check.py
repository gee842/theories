#!/usr/bin/env python3
"""Fresh build of the ethical-naturalism modules from frozen source bytes.

Inherited modules must keep the source hashes recorded by the main generative-basis
receipt. New declarations may use only Lean's standard propext and Quot.sound; every
new theorem must be audited, and sorry, custom axioms and warnings are rejected.
Uses `lean +<toolchain>` through elan when available, else `lean` on PATH;
either way the reported version must be 4.29.1.
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
LEAN = ROOT.parent
SOURCES = {
    "GenerativeCore": LEAN / "GenerativeCore.lean",
    "DynamicUnderdetermination": LEAN / "deeper/DynamicUnderdetermination.lean",
    "DynamicSymmetry": LEAN / "deeper/DynamicSymmetry.lean",
    "DynamicConsequences": LEAN / "deeper/DynamicConsequences.lean",
    "EthicalOrientation": LEAN / "EthicalOrientation.lean",
    "WholeQualityNaturalism": ROOT / "WholeQualityNaturalism.lean",
    "NaturalismIdentity": ROOT / "NaturalismIdentity.lean",
    "NaturalismReview": ROOT / "NaturalismReview.lean",
    "ProtectedScope": ROOT / "ProtectedScope.lean",
    "ProtectedScopeLimits": ROOT / "ProtectedScopeLimits.lean",
    "PremiseNecessity": ROOT / "PremiseNecessity.lean",
    "EmbeddedEvaluation": ROOT / "EmbeddedEvaluation.lean",
}
# Equal to the source_sha256 values in ../verification.json.
INHERITED_SHA256 = {
    "GenerativeCore": "e3daca1b729118fc309585a5d3ba1af60ac99cd80bab41e477aed204177069e8",
    "DynamicUnderdetermination": "0b5e930ba0a91306e73746c811b71e74fb9ccbc9e152c2e1116c4d19c4147f6c",
    "DynamicSymmetry": "5f71b9cc6c69070b5033852a0809ad795ad5dd18a44eb2ca068d1915d744673b",
    "DynamicConsequences": "d4a0dfc019fd1009d0230b0aa88ea4d940d42b6394ff44f59568e95edbd27692",
    "EthicalOrientation": "00bcc4a7542d4b81f1e924207d1d5b82e1ae032c4e26d7031d2779914fd56cc4",
}
NEW = ["WholeQualityNaturalism", "NaturalismIdentity", "NaturalismReview", "ProtectedScope", "ProtectedScopeLimits", "PremiseNecessity", "EmbeddedEvaluation"]
ALLOWED_AXIOMS = set()  # Ren, 6 October 2026: no axioms in new declarations


def digest(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=600)


def compiler():
    toolchain = (ROOT / "lean-toolchain").read_text().strip()
    for prefix in (["lean", "+" + toolchain], ["lean"]):
        try:
            version = run(prefix + ["--version"], ROOT)
        except FileNotFoundError:
            continue
        if version.returncode == 0 and "version 4.29.1," in version.stdout:
            where = run(prefix + ["--print-prefix"], ROOT)
            return toolchain, version.stdout.strip(), Path(where.stdout.strip()) / "bin" / "lean"
    raise SystemExit("Lean 4.29.1 not found")


def main():
    toolchain, version, lean = compiler()
    frozen = {name: path.read_bytes() for name, path in SOURCES.items()}
    for name, expected in INHERITED_SHA256.items():
        assert digest(frozen[name]) == expected, f"{name} changed since its own receipt"
    for name in NEW:
        text = frozen[name].decode()
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", text), name
        assert not re.search(r"^\s*(axiom|constant)\s", text, re.M), name
        theorems = set(re.findall(r"^theorem\s+(\S+)", text, re.M))
        requested = {x.rsplit(".", 1)[-1] for x in re.findall(r"^#print axioms (\S+)", text, re.M)}
        assert theorems == requested, (name, theorems ^ requested)
    results = []
    output_dir = ROOT / "verification"
    output_dir.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="naturalism-lean-") as temporary:
        build = Path(temporary)
        for name, source in frozen.items():
            (build / (name + ".lean")).write_bytes(source)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in SOURCES:
            result = run([str(lean), "-o", name + ".olean", name + ".lean"], build, env)
            log = output_dir / (name + ".txt")
            log.write_text(result.stdout)
            audits = re.findall(
                r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
                result.stdout, re.S)
            axioms = sorted({a.strip() for _, group in audits
                             for a in group.split(",") if a.strip()})
            clean = (result.returncode == 0 and "sorryAx" not in result.stdout
                     and "warning:" not in result.stdout and "error" not in result.stdout)
            if name in NEW:
                requested = re.findall(r"^#print axioms (\S+)", frozen[name].decode(), re.M)
                clean = clean and len(audits) == len(requested) and set(axioms) <= ALLOWED_AXIOMS
            results.append({
                "module": name, "source": os.path.relpath(SOURCES[name], ROOT),
                "source_sha256": digest(frozen[name]), "exit_code": result.returncode,
                "new": name in NEW, "dependency_audits": len(audits), "axioms": axioms,
                "empty_axiom_audits": sum(not group.strip() for _, group in audits),
                "clean": clean, "output": "verification/" + log.name,
                "output_sha256": digest(log.read_bytes()),
            })
            if not clean:
                break
    unchanged = all(path.read_bytes() == frozen[name] for name, path in SOURCES.items())
    passed = len(results) == len(SOURCES) and unchanged and all(r["clean"] for r in results)
    new_results = [r for r in results if r["new"]]
    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if passed else "failed", "lean_version": version,
        "compiler_sha256": digest(lean.read_bytes()), "toolchain": toolchain,
        "checker_sha256": digest(Path(__file__).read_bytes()),
        "source_unchanged_during_check": unchanged, "fresh_temporary_build": True,
        "allowed_standard_axioms": sorted(ALLOWED_AXIOMS), "modules": results,
        "new_audited_declarations": sum(r["dependency_audits"] for r in new_results),
        "new_empty_axiom_audits": sum(r["empty_axiom_audits"] for r in new_results),
        "scope": "Supervenience is factorization through base-identity classes; a step "
                 "quality along a history is a function of its visited states, composes through "
                 "the shared boundary, is invariant under exact re-representation, and is not "
                 "fixed by endpoints and action word; damage-free histories keep every initially "
                 "realizable activity realizable throughout, and every loss is located at an "
                 "actual transition. These credentials hold equally for the converse orientation. "
                 "Under the stated non-undermining premise over the whole scope of activities, "
                 "admissible orientations are exactly sub-relations of continuation inclusion; "
                 "fixed scopes and complete (including scalar) rankings fail it in finite "
                 "examples, including over actual transitions. The structural credentials hold "
                 "for every step relation; continuation inclusion registers restraint, every "
                 "exclusive choice and every recovered dip as damage. A scope derived from the "
                 "process (ongoing activities that remove no other ongoing activity, with "
                 "eventual realizability) separates restraint from harm only with every activity "
                 "in scope and only in a process where the victim removes nothing, and separates "
                 "untaken from carried courses only with the exercised scope; no single scope does "
                 "both, symmetric rivals stay unprotected, and unrecovered falls are not damage. "
                 "The orientation input and the whole-scope input are proved necessary: the "
                 "credentials do not determine the verdict, and unprivileged scopes include both "
                 "the empty and the whole scope, and the action vocabulary is necessary. Evaluation "
                 "is also modelled as a record inside the same process: the record equals the "
                 "whole-history relation, shares the process's continuation, and which recording "
                 "relation forms is not fixed by the law. No separate moral predicate is "
                 "formalized: the premise, the supervenience of moral properties, property "
                 "identity and any ethical verdict are not asserted.",
    }
    (ROOT / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "modules": len(results),
                      "new_audited_declarations": record["new_audited_declarations"],
                      "new_empty_axiom_audits": record["new_empty_axiom_audits"]}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
