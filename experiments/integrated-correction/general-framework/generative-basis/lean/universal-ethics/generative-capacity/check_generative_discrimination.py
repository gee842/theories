#!/usr/bin/env python3
"""Checks renewing/consuming formation dynamics and basic-condition priority against score rivals."""
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

-- Joint consumption: two parts each at the full rate 2 jointly draw 4; together they form
-- only the budget 3 and then nothing, whereas either part alone forms 2 at every step.
example : cumulative unitWear ⟨0, 2⟩ (fun _ => 4) 5 = 3 ∧ formed unitWear ⟨0, 2⟩ (fun _ => 4) 5 = 0 ∧
    cumulative unitWear ⟨0, 2⟩ (fun _ => 2) 5 = 10 := by decide

-- Sign-neutrality control: any predicate in the G0 position covers both continuations'
-- events, and the Ceaseless distinction takes no valence argument. Which side a reading
-- favors is therefore not supplied by these theorems.
example (V : (Nat → Nat) → Nat × Nat → Prop)
    (anySign : G0 (eventInventory unitWear ⟨3, 2⟩) V) :
    V (fun _ => 5) (0, 2) ∧ V (fun _ => 2) (0, 1) ∧
    Ceaseless unitWear ⟨3, 2⟩ (fun _ => 2) ∧ ¬ Ceaseless unitWear ⟨3, 2⟩ (fun _ => 5) := by
  have beyond := beyond_initial_implies_current unitWear ⟨3, 2⟩ (fun _ => 5)
    (fun _ => show 2 < 5 by decide)
  refine ⟨(event_reading_recognizes_both unitWear ⟨3, 2⟩ (by decide) (by decide) V anySign).1,
    (event_reading_recognizes_both unitWear ⟨3, 2⟩ (by decide) (by decide) V anySign).2.2 0 1 (by decide),
    (ceaseless_separates unitWear ⟨3, 2⟩ (by decide) (fun _ => 5) beyond).1,
    (ceaseless_separates unitWear ⟨3, 2⟩ (by decide) (fun _ => 5) beyond).2⟩

-- A natural-number rival trades where basic-condition priority does not; the bounded
-- ratio score does not trade and ranks six gains above three.
example : weighted 5 0 < weighted 5 6 ∧ ¬ PracticalJudgment.Better protect gain 6 0 ∧
    ¬ (num 0 * den 6 < num 6 * den 0) ∧ (num 3 * den 6 < num 6 * den 3) :=
  ⟨weighted_trades 5, priority_never_trades 6 (by decide), by decide, by decide⟩
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
        "scope": "RenewingFormation: under a supplied no-recovery wear law, formation within renewal is ceaseless and keeps renewal capacity; formation whose pressure persistently exceeds the current renewal rate has a whole-unfolding total bounded by stock plus the triangular renewal budget and ceases by that budget time; shared formation under any allocation ceases under joint excess, including when each part is within renewal; KeepsCapacity holds exactly when no pressure exceeds the initial rate (positive rate) and differs from Ceaseless on rest and on one-off wear; a one-step count favors consuming formation while every within-renewal continuation exceeds every beyond-current one after the budget. Part A uses no normative predicate. Part B shows that G0 read over every formation event covers both continuations and that the no-loss comparison does not apply between them; any valence attached to the distinction is an interpretive premise. ProtectionPriorityRival: in one protection-versus-gains situation, G0, C and J2 hold together and J2 never trades; G0 leaves the ordering open and a natural-number ordering satisfying C trades; every natural-number score satisfying C trades; a bounded rational score agrees with J2 on every pair. Correspondence of real processes to the law, the basic classification and separation of J2 from bounded-sensitivity rivals remain outside the check."
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
                {"claim": "unitWear joint instance: two parts at rate 2 jointly form the budget 3 and then nothing; one part alone forms 10 by step 5", "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "sign-neutrality: any predicate in the G0 position covers both continuations; the Ceaseless distinction takes no valence argument", "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "natural-number rival trades at six gains while basic-condition priority and the bounded ratio score do not", "kernel_checked": True, "counted_as_new_theorem": False},
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
