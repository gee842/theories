#!/usr/bin/env python3
"""Checks the inherited-to-new composition for open-form realization under revision."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
import check as audit_support


HERE = Path(__file__).resolve().parent
SOURCES = {
    "ContinuationRenewal": HERE.parent / "ContinuationRenewal.lean",
    "JointContinuationClassification": HERE.parent / "JointContinuationClassification.lean",
    "GenerativeComparison": HERE / "GenerativeComparison.lean",
    "PracticalJudgment": HERE / "PracticalJudgment.lean",
    "StandardsBridge": HERE / "StandardsBridge.lean",
    "PositiveGroundUncertainty": HERE / "PositiveGroundUncertainty.lean",
    "OpenFutureRevision": HERE / "OpenFutureRevision.lean",
}


def declarations(source, expected_import):
    # Validate the exact import closure before using the inherited declaration scanner.
    # Only the scanner input substitutes local imports; compilation uses unchanged bytes.
    code = audit_support.code_only(source)
    imports = re.findall(r"^import\s+(.+)$", code, re.M)
    assert imports == expected_import, imports
    return audit_support.declarations(re.sub(r"^import .+$", "import Std", source, flags=re.M))


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    retained = HERE / "open-future-revision-checks" / stamp
    retained.mkdir(parents=True, exist_ok=False)
    sources = {name: path.read_bytes() for name, path in SOURCES.items()}
    helpers = {p.name: p.read_bytes() for p in [Path(__file__), HERE / "check.py"]}
    for name, data in helpers.items():
        (retained / name).write_bytes(data)
    for name, data in sources.items():
        (retained / (name + ".lean")).write_bytes(data)
    receipt = {
        "status": "checking", "utc": stamp, "toolchain": audit_support.TOOLCHAIN,
        "retained_run": str(retained.relative_to(HERE)),
        "source_sha256": {name: audit_support.digest(data) for name, data in sources.items()},
        "checker_sha256": {name: audit_support.digest(data) for name, data in helpers.items()},
        "scope": "One formal composition: current-rule progress plus non-increasing certificate handoff supplies the inherited finite realization bound, whose actual generative witnesses feed inherited G0 positive-ground inference. Two individually finishing rules can fail under perpetual revision; a valid handoff can change the formed outcome. No ethical scalar, authority, duty, unconditional success or universal productive deadline is inferred. Inherited modules are compiled for this import composition, counted separately.",
    }
    try:
        registry = {name: declarations(data.decode(), {
            "ContinuationRenewal": [],
            "OpenFutureRevision": ["ContinuationRenewal", "PositiveGroundUncertainty"],
            "JointContinuationClassification": ["Std"],
            "GenerativeComparison": ["Std"],
            "PracticalJudgment": ["Std"],
            "StandardsBridge": ["Std"],
            "PositiveGroundUncertainty": ["GenerativeComparison", "PracticalJudgment", "JointContinuationClassification", "StandardsBridge"],
        }[name]) for name, data in sources.items()}
        lean = Path.home() / ".elan/bin/lean"
        binary = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
        receipt["lean_binary_sha256"] = audit_support.digest(binary.read_bytes())
        command = [str(lean), "+" + audit_support.TOOLCHAIN]
        records = []
        with tempfile.TemporaryDirectory(prefix="open-future-revision-lean-") as scratch:
            work = Path(scratch)
            env = {**os.environ, "LEAN_PATH": str(work)}

            def run(args, log):
                p = subprocess.run(command + args, cwd=work, env=env, text=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
                (retained / log).write_text(p.stdout)
                assert p.returncode == 0, p.stdout
                assert not re.search(r"\b(?:error|warning):", p.stdout), p.stdout
                return p.stdout

            receipt["lean_version"] = run(["--version"], "version.log").strip()
            assert "version 4.29.1" in receipt["lean_version"]
            for name, data in sources.items():
                (work / (name + ".lean")).write_bytes(data)
            for name in sources:
                run(["-o", name + ".olean", name + ".lean"], name + ".log")
                audit = "import " + name + "\n" + "\n".join(
                    "#print axioms " + item["name"] for item in registry[name]) + "\n"
                audit_name = name + "AxiomAudit.lean"
                (work / audit_name).write_text(audit)
                (retained / audit_name).write_text(audit)
                output = run([audit_name], name + "AxiomAudit.log")
                signatures = "import " + name + "\n" + "\n".join(
                    "#check " + item["name"] for item in registry[name]
                    if item["kind"] == "theorem") + "\n"
                signature_name = name + "Signatures.lean"
                (work / signature_name).write_text(signatures)
                (retained / signature_name).write_text(signatures)
                run([signature_name], name + "Signatures.log")
                dependencies = {}
                for item in registry[name]:
                    full = item["name"]
                    if "'" + full + "' does not depend on any axioms" in output:
                        axioms = []
                    else:
                        match = re.search(r"'" + re.escape(full) + r"' depends on axioms:\s*\[([^]]*)\]", output)
                        assert match, (full, output)
                        axioms = [a.strip() for a in match[1].split(",") if a.strip()]
                    assert set(axioms) <= {"propext", "Quot.sound", "Classical.choice"}, (full, axioms)
                    dependencies[full] = axioms
                records.append({
                    "module": name, "theorems": sum(x["kind"] == "theorem" for x in registry[name]),
                    "declarations": registry[name], "axiom_dependencies": dependencies,
                    "kernel_checked": True,
                })
            controls = """import OpenFutureRevision
open OpenFutureRevision GenerativeComparison

-- Exact producer-consumer adapter, with all operational and G0 premises visible.
example {H S Q : Type}
    (admitted : H → Prop) (states : H → Nat → S)
    (rank : H → Nat → S → Nat) (completed : H → Nat → Prop)
    (decideEvent : ∀ h, DecidablePred (completed h))
    (appears : H → Nat → Q → Prop) (generative : Q → Prop)
    (before : H → Q → Prop) (bound : Nat)
    (initial : ∀ h, admitted h → rank h 0 (states h 0) ≤ bound)
    (localStep : ∀ h, admitted h → ∀ n, ¬ completed h n →
      rank h n (states h (n+1)) < rank h n (states h n))
    (handoff : ∀ h, admitted h → ∀ n, ¬ completed h n →
      rank h (n+1) (states h (n+1)) ≤ rank h n (states h (n+1)))
    (correspondence : ∀ h, admitted h → ∀ n, completed h n →
      ∃ q, generative q ∧ appears h n q ∧ ¬ before h q)
    (positive : H → Q → Prop)
    (g0 : G0 (boundedInventory appears generative bound) positive) :
    ∀ h, admitted h → ∃ q, positive h q ∧ ¬ before h q :=
  positive_ground_by_bound admitted appears generative before bound positive g0
    (generation_by_bound admitted states rank completed decideEvent appears
      generative before bound initial localStep handoff correspondence)
"""
            (work / "Controls.lean").write_text(controls)
            (retained / "Controls.lean").write_text(controls)
            run(["Controls.lean"], "Controls.log")
            receipt["checked_application_examples"] = [
                {"claim": "Complete rank-handoff to timed formation to G0 positive-ground adapter", "kernel_checked": True, "counted_as_new_theorem": False}
            ]
        receipt["source_unchanged_during_check"] = all(
            SOURCES[name].read_bytes() == data for name, data in sources.items())
        assert receipt["source_unchanged_during_check"], "Source changed; only snapshot checked"
        assert all((HERE / name).read_bytes() == data for name, data in helpers.items()), "Checker changed"
        receipt["modules"] = records
        receipt["artifact_sha256"] = {
            p.name: audit_support.digest(p.read_bytes()) for p in sorted(retained.iterdir()) if p.is_file()
        }
        receipt["status"] = "passed"
    except Exception as error:
        receipt["status"] = "failed"
        receipt["error"] = str(error)
        raise
    finally:
        serialized = json.dumps(receipt, indent=2) + "\n"
        (retained / "verification.json").write_text(serialized)
        (HERE / "open-future-revision-verification.json").write_text(serialized)
    model = next(r for r in records if r["module"] == "OpenFutureRevision")
    print(json.dumps({"status": receipt["status"], "new_theorems": model["theorems"],
                      "new_declaration_audits": len(model["declarations"]),
                      "axioms": sorted({a for r in records for aa in r["axiom_dependencies"].values() for a in aa}),
                      "receipt": str(HERE / "open-future-revision-verification.json")}))


if __name__ == "__main__":
    main()
