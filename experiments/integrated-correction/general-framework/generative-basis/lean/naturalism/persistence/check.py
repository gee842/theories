#!/usr/bin/env python3
"""Fresh build of the evaluation-persistence bridge from frozen source bytes.

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
LEAN = ROOT.parents[1]
VAL = ROOT.parents[5] / "valuation-development/lean"
SOURCES = {
    "GenerativeCore": LEAN / "GenerativeCore.lean",
    "Depletion": LEAN / "Depletion.lean",
    "SupportNecessity": LEAN / "conditional/SupportNecessity.lean",
    "ResourceContinuation": LEAN / "conditional/ResourceContinuation.lean",
    "RenewalAccounting": LEAN / "conditional/renewal/RenewalAccounting.lean",
    "RenewalClosure": LEAN / "conditional/renewal/RenewalClosure.lean",
    "RenewalSufficiency": LEAN / "conditional/renewal/RenewalSufficiency.lean",
    "RenewalLink": LEAN / "conditional/renewal/RenewalLink.lean",
    "RenewalCharacterization": LEAN / "conditional/renewal/RenewalCharacterization.lean",
    "ValuationDevelopment": VAL / "ValuationDevelopment.lean",
    "ClosedLoopValuation": VAL / "ClosedLoopValuation.lean",
    "ExplorationCoverage": VAL / "ExplorationCoverage.lean",
    "ValuationCompletion": VAL / "ValuationCompletion.lean",
    "ValuationBridges": VAL / "ValuationBridges.lean",
    "LineageInProcess": VAL / "LineageInProcess.lean",
    "ValuationRenewal": VAL / "ValuationRenewal.lean",
    "EvaluationPersistence": ROOT / "EvaluationPersistence.lean"
}
# Hashes of the imported sources as they stand on main (6 October 2026).
INHERITED_SHA256 = {
    "GenerativeCore": "e3daca1b729118fc309585a5d3ba1af60ac99cd80bab41e477aed204177069e8",
    "Depletion": "324021e3f315d7f06f2ae28624aa4468f1029a77347a6f3952c5313c2641aa3e",
    "SupportNecessity": "d55d4e960e7d95f0c17e8f915b5b46b85c9c04fbf34c036b17c725cf98b66aa0",
    "ResourceContinuation": "4c423a74c7c5b197374b652c420fdc682834fbbf5122aac277a828e193cc7c6e",
    "RenewalAccounting": "b593f8c58d7a302506deff75f36fe01ca53db7df59d701ee509f31d7585e0927",
    "RenewalClosure": "2e8a923cf90c3113c88afbaf107f9057ac3123f5f259ca759bab7741e66bada7",
    "RenewalSufficiency": "51788ffa220bae4493958fab5f63d2a6a8c2714ce2e5f9c56f4cc8f5c30e90a3",
    "RenewalLink": "1abc38a98588f33d3d2cf31fe0bf3f7026b936116500da2d2bbfa7d53404fa18",
    "RenewalCharacterization": "b972ae4ec4e640568672ce29356647f93bf7928e23c669fa6318fda47bbee0a0",
    "ValuationDevelopment": "646fe738830cf9da7037f9ef554aa455af0dd85b32ae1ba3591ba7e6dbb3b9d2",
    "ClosedLoopValuation": "ba21df526dae8fdf0b4f5e1f1947ab12391572e083d9f521e3b0284fbf2c43d3",
    "ExplorationCoverage": "c6f0f9c8ac71310b2f1f7511f4347ace50c285eb712cb4335bf63f5f159abd8e",
    "ValuationCompletion": "7af08fa21c4c12d7eb53e525394303d168b1be4df20d6132451d1ddc3118c35f",
    "ValuationBridges": "9e2557f07597903c5d54ace4645e8267b2c769dde90a861d12a9e07e0eae0248",
    "LineageInProcess": "605e5ba655d7f81665dec19936f82f0afd416d83085f3fb14d86c65926c62d70",
    "ValuationRenewal": "e64e02644405dc228fd641f6e974bbb49d558177275922c1f245929bfc20e8a6"
}
NEW = ["EvaluationPersistence"]
ALLOWED_AXIOMS = {"propext", "Quot.sound"}  # inherited from the valuation study's modules; reported to Ren


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
    with tempfile.TemporaryDirectory(prefix="naturalism-persistence-lean-") as temporary:
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
        "scope": "An evaluating kind of the shared renewal process persists under some "
                 "valuation exactly when it belongs to a self-renewing population, which is "
                 "closed under support and opens what it demands; valuing the correction kind "
                 "of lapsingCorrection does not keep it. Read from the valuation study's "
                 "theorems; their propext and Quot.sound dependencies are inherited.",
    }
    (ROOT / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "modules": len(results),
                      "new_audited_declarations": record["new_audited_declarations"],
                      "new_empty_axiom_audits": record["new_empty_axiom_audits"]}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
