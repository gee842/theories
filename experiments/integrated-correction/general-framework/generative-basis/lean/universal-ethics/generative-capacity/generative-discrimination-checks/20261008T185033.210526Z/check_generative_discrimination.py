#!/usr/bin/env python3
"""Checks renewing/consuming formation dynamics and basic-condition priority against scalar rivals."""
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
    "GenerativeComparison": HERE / "GenerativeComparison.lean",
    "PracticalJudgment": HERE / "PracticalJudgment.lean",
    "RenewingFormation": HERE / "RenewingFormation.lean",
    "ProtectionPriorityRival": HERE / "ProtectionPriorityRival.lean",
}
EXPECTED_IMPORTS = {
    "GenerativeComparison": ["Std"],
    "PracticalJudgment": ["Std"],
    "RenewingFormation": ["GenerativeComparison"],
    "ProtectionPriorityRival": ["GenerativeComparison", "PracticalJudgment"],
}
NEW_MODULES = ["RenewingFormation", "ProtectionPriorityRival"]


def declarations(source, expected_import):
    # Validate the exact import closure before using the inherited declaration scanner.
    # Only the scanner input substitutes local imports; compilation uses unchanged bytes.
    code = audit_support.code_only(source)
    imports = re.findall(r"^import\s+(.+)$", code, re.M)
    assert imports == expected_import, imports
    return audit_support.declarations(re.sub(r"^import .+$", "import Std", source, flags=re.M))


CONTROLS = """import RenewingFormation
import ProtectionPriorityRival
open RenewingFormation ProtectionPriorityRival GenerativeComparison

-- A concrete instance of the law class: consuming forms more first, then stops at its budget.
example : cumulative unitWear ⟨3, 2⟩ (fun _ => 2) 1 < cumulative unitWear ⟨3, 2⟩ (fun _ => 5) 1 ∧
    cumulative unitWear ⟨3, 2⟩ (fun _ => 5) 7 = 6 ∧
    cumulative unitWear ⟨3, 2⟩ (fun _ => 2) 7 = 14 := by decide

-- Valence control: any predicate in the G0 position covers both continuations' events;
-- the separation is the ceaseless/non-ceaseless dynamics, which takes no valence argument.
example (V : (Nat → Nat) → Nat × Nat → Prop)
    (anySign : G0 (eventInventory unitWear ⟨3, 2⟩) V) :
    V (fun _ => 5) (0, 2) ∧ V (fun _ => 2) (0, 1) ∧
    Ceaseless unitWear ⟨3, 2⟩ (fun _ => 2) ∧ ¬ Ceaseless unitWear ⟨3, 2⟩ (fun _ => 5) := by
  refine ⟨(event_reading_favors_both unitWear ⟨3, 2⟩ (by decide) (by decide) V anySign).1,
    (event_reading_favors_both unitWear ⟨3, 2⟩ (by decide) (by decide) V anySign).2.2 0 1 (by decide),
    (whole_direction_separates unitWear ⟨3, 2⟩ (by decide) (fun _ => 5) (fun _ => show 2 < 5 by decide)).1,
    (whole_direction_separates unitWear ⟨3, 2⟩ (by decide) (fun _ => 5) (fun _ => show 2 < 5 by decide)).2⟩

-- A concrete scalar rival trades where the basic-condition priority does not.
example : weighted 5 0 < weighted 5 6 ∧ ¬ PracticalJudgment.Better protect gain 6 0 :=
  ⟨weighted_trades 5, priority_never_trades 6 (by decide)⟩
"""


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    retained = HERE / "generative-discrimination-checks" / stamp
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
        "scope": "RenewingFormation: under a supplied wear law, formation within renewal is ceaseless; formation persistently beyond renewal has a whole-unfolding total bounded by stock plus the triangular renewal budget and ceases by that budget time; co-dependent formation under any allocation ceases with it; consuming formation can form more at first while sustained formation exceeds every consuming continuation after the budget. Part A uses no normative predicate. Part B shows that G0 read over every formation event covers both continuations, so separation comes from the dynamics. ProtectionPriorityRival: in one protection-versus-gains situation, J2's ordering satisfies C and never trades; a scalar ordering satisfies C and trades; every natural-number score satisfying C trades. Correspondence of real processes to the law, the basic classification and bounded-sensitivity rivals remain outside the check."
    }
    records = []
    try:
        registry = {name: declarations(data.decode(), EXPECTED_IMPORTS[name])
                    for name, data in sources.items()}
        lean = Path.home() / ".elan/bin/lean"
        binary = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
        receipt["lean_binary_sha256"] = audit_support.digest(binary.read_bytes())
        command = [str(lean), "+" + audit_support.TOOLCHAIN]
        with tempfile.TemporaryDirectory(prefix="generative-discrimination-lean-") as scratch:
            work = Path(scratch)
            env = {**os.environ, "LEAN_PATH": str(work)}

            def run(args, log):
                p = subprocess.run(command + args, cwd=work, env=env, text=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=300)
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
                    assert set(axioms) <= audit_support.STANDARD_AXIOMS, (full, axioms)
                    dependencies[full] = axioms
                records.append({
                    "module": name, "new": name in NEW_MODULES,
                    "theorems": sum(x["kind"] == "theorem" for x in registry[name]),
                    "declarations": registry[name], "axiom_dependencies": dependencies,
                    "kernel_checked": True,
                })
            (work / "Controls.lean").write_text(CONTROLS)
            (retained / "Controls.lean").write_text(CONTROLS)
            run(["Controls.lean"], "Controls.log")
            receipt["checked_application_examples"] = [
                {"claim": "unitWear instance: consuming forms more at step 1, total stops at budget 6, sustained reaches 14 by step 7", "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "any predicate in the G0 position covers both continuations; ceaseless separation takes no valence argument", "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "weighted scalar rival trades at six gains while basic-condition priority does not", "kernel_checked": True, "counted_as_new_theorem": False},
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
        (HERE / "generative-discrimination-verification.json").write_text(serialized)
    summary = {}
    for r in records:
        if r["new"]:
            counts = {}
            for axioms in r["axiom_dependencies"].values():
                key = "+".join(axioms) or "none"
                counts[key] = counts.get(key, 0) + 1
            summary[r["module"]] = {"theorems": r["theorems"], "declarations": len(r["declarations"]),
                                    "dependency_profile": counts}
    print(json.dumps({"status": receipt["status"], "new_modules": summary,
                      "receipt": str(HERE / "generative-discrimination-verification.json")}, indent=1))


if __name__ == "__main__":
    main()
