#!/usr/bin/env python3
"""Checks intervention-dependent target erosion against an original finite maintenance task."""
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
    "AlignmentInquiry": HERE / "AlignmentInquiry.lean",
    "ChanceAdequacy": HERE / "ChanceAdequacy.lean",
    "ObservableContinuation": HERE / "ObservableContinuation.lean",
    "MaintenanceBaseline": HERE / "MaintenanceBaseline.lean",
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
    retained = HERE / "maintenance-baseline-checks" / stamp
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
        "scope": "Four new results audit the comparison origin of a finite one-delivery maintenance task. An original target may be transported through faithful actual completion records or preserved current requirements; fulfillment then yields the inherited natural event-mass bound. A physical retirement disables the old left line and parallel execution, so recomputing demand-and-old-capability after intervention can certify an empty target while original delivery remains absent. Actual funded parallel delivery before retirement fulfills the original task; actual single left delivery also permits finite completion and retirement. Delivery records are formed by enabled inherited response effects, not an arbitrary release flag. The local mechanism does not build new hardware, prove continuous service, establish moral authority or excuse unmet needs outside the original finite undertaking. ObservableContinuation, AlignmentInquiry and ChanceAdequacy are imported unchanged and audited as inherited."
    }
    try:
        registry = {name: declarations(data.decode(), {"AlignmentInquiry": ["Std"], "ChanceAdequacy": ["Std"], "ObservableContinuation": ["AlignmentInquiry", "ChanceAdequacy"], "MaintenanceBaseline": ["ObservableContinuation"]}[name])
                    for name, data in sources.items()}
        lean = Path.home() / ".elan/bin/lean"
        binary = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
        receipt["lean_binary_sha256"] = audit_support.digest(binary.read_bytes())
        command = [str(lean), "+" + audit_support.TOOLCHAIN]
        records = []
        with tempfile.TemporaryDirectory(prefix="generative-maintenance-baseline-lean-") as scratch:
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
            controls = """import MaintenanceBaseline
open MaintenanceBaseline

-- Retirement actually disables the old dependent routes.
example : deliver .left (retire (initial 2 false)) = none ∧
    deliver .parallel (retire (initial 2 false)) = none := by
  exact ⟨rfl, rfl⟩

-- The independent right route remains executable where its physical mode works.
example : deliver .right (retire (initial 2 true)) =
    some ⟨⟨true, 1, true⟩, false, true⟩ := by rfl

-- Completed task records suffice even when the retired current target is empty.
example : ChanceAdequacy.Fulfilled [false, true] (fun _ => true)
    ObservableContinuation.oldWorks (actualDelivery .left 1) := by
  have joined := target_transport_with_completion_gives_bound [false, true]
    (fun _ => 1) (fun _ => true) ObservableContinuation.oldWorks
    (fun mode => !(actualDelivery .left 1 mode)) (fun _ => false)
    (actualDelivery .left 1) (actualDelivery .left 1)
    (by
      intro mode member needed
      exact Or.inl (completed_single_delivery_allows_retirement.2.1 mode member needed))
    (by intro mode member done; exact done)
    (by intro mode member needed; simp [ChanceAdequacy.target] at needed)
    (by decide)
  exact joined.1
"""
            (work / "Controls.lean").write_text(controls)
            (retained / "Controls.lean").write_text(controls)
            run(["Controls.lean"], "Controls.log")
            receipt["checked_application_examples"] = [
                {"claim": "retirement disables actual left and parallel execution",
                 "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "the independent right route remains executable in its working mode after retirement",
                 "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "the generic original-target transport accepts independently checked completion despite an empty retired current target",
                 "kernel_checked": True, "counted_as_new_theorem": False},
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
        (HERE / "maintenance-baseline-verification.json").write_text(serialized)
    model = next(r for r in records if r["module"] == "MaintenanceBaseline")
    print(json.dumps({"status": receipt["status"], "new_theorems": model["theorems"],
                      "new_declaration_audits": len(model["declarations"]),
                      "axioms": sorted({a for r in records for aa in r["axiom_dependencies"].values() for a in aa}),
                      "receipt": str(HERE / "maintenance-baseline-verification.json")}))


if __name__ == "__main__":
    main()
