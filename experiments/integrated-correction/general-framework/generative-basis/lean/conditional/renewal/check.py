#!/usr/bin/env python3
"""Fresh build of the renewal–closure modules from frozen source bytes.

Inherited modules must keep the source hashes recorded by their own receipts.
New declarations may use only Lean's standard propext and Quot.sound; every new
theorem must be audited, and sorry, custom axioms and warnings are rejected.
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
LEAN = ROOT.parents[1]
SOURCES = {
    "GenerativeCore": LEAN / "GenerativeCore.lean",
    "Depletion": LEAN / "Depletion.lean",
    "SupportNecessity": LEAN / "conditional/SupportNecessity.lean",
    "RenewalClosure": ROOT / "RenewalClosure.lean",
    "RenewalAccounting": ROOT / "RenewalAccounting.lean",
    "RenewalSufficiency": ROOT / "RenewalSufficiency.lean",
    "RenewalLink": ROOT / "RenewalLink.lean",
}
INHERITED_SHA256 = {
    "GenerativeCore": "e3daca1b729118fc309585a5d3ba1af60ac99cd80bab41e477aed204177069e8",
    "Depletion": "324021e3f315d7f06f2ae28624aa4468f1029a77347a6f3952c5313c2641aa3e",
    "SupportNecessity": "d55d4e960e7d95f0c17e8f915b5b46b85c9c04fbf34c036b17c725cf98b66aa0",
}
NEW = ["RenewalClosure", "RenewalAccounting", "RenewalSufficiency", "RenewalLink"]
ALLOWED_AXIOMS = {"propext", "Quot.sound"}


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
        requested = set(re.findall(r"^#print axioms (\S+)", text, re.M))
        assert theorems == requested, (name, theorems ^ requested)
    results = []
    output_dir = ROOT / "verification"
    output_dir.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="renewal-closure-lean-") as temporary:
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
        "scope": "Conditional statements over supplied kinds, support edges, spans, formation "
                 "demands and arrival rates: late occurrence descends from a realized closure "
                 "of kinds; acyclic support has a deadline without a supplied rank; when every "
                 "kind brings in less than its formation demands, a combined potential strictly "
                 "decreases on every live tick, so renewal ends by an explicit deadline; a "
                 "support-closed population that is balanced, or that supports an excess kind, "
                 "has a steady configuration fixed by one tick and so renews forever; and on "
                 "one execution of the constraint-flow process, endless liveness needs both a "
                 "realized closure of supporters that outlast the tick and a kind that brings in "
                 "at least its formation demand. The exact mixed-case condition is not yet "
                 "proved. No physical identification or ethical appraisal is asserted.",
    }
    (ROOT / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "modules": len(results),
                      "new_audited_declarations": record["new_audited_declarations"],
                      "new_empty_axiom_audits": record["new_empty_axiom_audits"]}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
