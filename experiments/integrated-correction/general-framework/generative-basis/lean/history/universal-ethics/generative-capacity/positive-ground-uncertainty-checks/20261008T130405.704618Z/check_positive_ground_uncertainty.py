#!/usr/bin/env python3
"""Checks positive generative ground with open future forms and revisable evidence, without strict whole comparison."""
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
    "JointContinuationClassification": HERE.parent / "JointContinuationClassification.lean",
    "GenerativeComparison": HERE / "GenerativeComparison.lean",
    "PracticalJudgment": HERE / "PracticalJudgment.lean",
    "StandardsBridge": HERE / "StandardsBridge.lean",
    "PositiveGroundUncertainty": HERE / "PositiveGroundUncertainty.lean",
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
    retained = HERE / "positive-ground-uncertainty-checks" / stamp
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
        "scope": "Positive ground and contributory reason under explicit G0 and direct articulation, without C, global no-loss or a strict whole ordering. The same response can secure some new generative realization in each admitted future while no fixed form is secured across all branches. A finite signed integral finds a positive relational occurrence with supplied generative correspondence; a represented adverse burden remains. Old joint positive possibilities and query access are retained. Acquired evidence distinguishes two live productive hypotheses from a barren one, while branch form remains open and further evidence can discriminate or retract the certificate. The finite visible scope, local law, meaning, units and direct normative articulation remain explicit; no infinite integral, final action permission or universal behavioral convergence is inferred."
    }
    try:
        registry = {name: declarations(data.decode(), {
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
        with tempfile.TemporaryDirectory(prefix="generative-positive-ground-uncertainty-lean-") as scratch:
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
            controls = """import PositiveGroundUncertainty
open PositiveGroundUncertainty GenerativeComparison Generative.StandardsBridge

-- The concrete new formation feeds G0 directly without requiring C or no loss.
example (m : FormationModel) (productive : 0 < magnitude m)
    (positive : Bool → LivingClaim → Prop)
    (g0 : G0 (generatedInventory m) positive) :
    ∀ branch, ∃ q, positive branch q ∧ ¬ prior branch q := by
  apply contingent_generation_has_positive_ground (fun _ => True)
    prior (generatedInventory m) positive g0
  intro branch _
  exact (same_response_secures_generation_without_fixed_form m productive).1 branch

-- Existing truth retention applies to the same acquired evidence mechanism.
example (m : FormationModel) (included : rule m ∈ repertoire) :
    rule m ∈ learn repertoire (acquire (rule m) 1 [true]) :=
  actual_rule_retained (rule m) repertoire _ included
    (acquired_evidence_faithful (rule m) 1 [true])

-- Existing robust scope-to-actual transport needs actual coverage only here.
example (m : FormationModel) (covered : live m) (branch : Bool) :
    0 < finiteIntegral positiveDomain (contribution (respond initial) m branch) := by
  apply PracticalJudgment.robust_at_actual (w := m) (a := branch) covered
  intro model admitted
  exact acquired_evidence_secures_good_and_leaves_both_opennesses.2.2.2.2.2.1 model admitted branch

-- Represented physical realization is independent of merely changing evidence.
example (m : FormationModel) (branch : Bool) :
    finiteIntegral positiveDomain (contribution initial m branch) = 0 := by
  cases m <;> cases branch <;> rfl
"""
            (work / "Controls.lean").write_text(controls)
            (retained / "Controls.lean").write_text(controls)
            run(["Controls.lean"], "Controls.log")
            receipt["checked_application_examples"] = [
                {"claim": "same-response new generation feeds G0 directly", "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "existing acquired-evidence truth retention applies", "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "existing robust-at-actual transport applies with coverage", "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "before response no fresh positive contribution is realized", "kernel_checked": True, "counted_as_new_theorem": False},
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
        (HERE / "positive-ground-uncertainty-verification.json").write_text(serialized)
    model = next(r for r in records if r["module"] == "PositiveGroundUncertainty")
    print(json.dumps({"status": receipt["status"], "new_theorems": model["theorems"],
                      "new_declaration_audits": len(model["declarations"]),
                      "axioms": sorted({a for r in records for aa in r["axiom_dependencies"].values() for a in aa}),
                      "receipt": str(HERE / "positive-ground-uncertainty-verification.json")}))


if __name__ == "__main__":
    main()
