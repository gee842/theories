#!/usr/bin/env python3
"""Check renewing and consuming as a relation to participated conditions, and what the
comparison principle C decides once G0's generation is read relationally; no axioms."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
import importlib.util
SUPPORT_PATH = Path(__file__).resolve().parent.parent / "universal-ethics/generative-capacity/check.py"
spec = importlib.util.spec_from_file_location("relational_renewal_audit_support", SUPPORT_PATH)
audit_support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit_support)


HERE = Path(__file__).resolve().parent
SOURCES = {
    "RelationalRenewal": HERE / "RelationalRenewal.lean",
    "RenewalComparison": HERE / "RenewalComparison.lean",
}
IMPORTS = {
    "RelationalRenewal": [],
    "RenewalComparison": ["GenerativeComparison", "RelationalRenewal"],
}
# Compiled as a dependency and hashed; audited by its own checker, not here.
DEPENDENCIES = {
    "GenerativeComparison": HERE.parent / "universal-ethics/generative-capacity/GenerativeComparison.lean",
}


def declarations(source, expected_import):
    code = audit_support.code_only(source)
    imports = re.findall(r"^import\s+(.+)$", code, re.M)
    assert imports == expected_import, imports
    return audit_support.declarations(source)


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    retained = HERE / "relational-renewal-checks" / stamp
    retained.mkdir(parents=True, exist_ok=False)
    sources = {name: path.read_bytes() for name, path in SOURCES.items()}
    dependencies_src = {name: path.read_bytes() for name, path in DEPENDENCIES.items()}
    helpers = {p.name: p.read_bytes() for p in [Path(__file__), SUPPORT_PATH]}
    for name, data in helpers.items():
        (retained / name).write_bytes(data)
    for name, data in {**dependencies_src, **sources}.items():
        (retained / (name + ".lean")).write_bytes(data)
    receipt = {
        "status": "checking", "utc": stamp, "toolchain": audit_support.TOOLCHAIN,
        "retained_run": str(retained.relative_to(HERE)),
        "source_sha256": {name: audit_support.digest(data) for name, data in sources.items()},
        "dependency_sha256": {name: audit_support.digest(data) for name, data in dependencies_src.items()},
        "checker_sha256": {name: audit_support.digest(data) for name, data in helpers.items()},
        "scope": "A formation is classified by its relation to the conditions of the relations it participates in (dependence or drawing): renewing when each such condition keeps supporting every formation depending on it, consuming when it draws on a condition some dependent formation permanently loses. Exclusive, not exhaustive. Unrenewed drawdown admits finitely many active steps. In a law where the renewing formation depends on the condition it renews: within renewal, continuation and unbounded formation; beyond renewal, permanent loss of the renewer's support, self-ending with bounded formation for a dependent focal formation, and unbounded persistence for an independent one. Neither formation at each active step nor the focal formation's own trajectory decides the class; joint drawing can consume when each alone is within renewal; escalation beginning within renewal consumes. No ethical predicate; every declaration is required to have an empty axiom set. Levels, needs and rates are local representations whose real correspondence is not established. RenewalComparison connects this to GenerativeComparison's G0 and C as hypotheses only: under the relational reading (active events of non-consuming formations as grounds), G0 credits exactly non-consuming formation events, and C ranks a malignant formation's unfolding below the same unfolding without it, which the broad event reading leaves incomparable and lets a strict C-respecting comparison invert; sharing extends winning by consumption under both readings. The comparisons use C, not G0; the relational reading of G0's generation and C's defense are philosophical, outside this audit; mixed cases are not decided."
    }
    try:
        registry = {name: declarations(data.decode(), IMPORTS[name]) for name, data in sources.items()}
        lean = Path.home() / ".elan/bin/lean"
        binary = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
        receipt["lean_binary_sha256"] = audit_support.digest(binary.read_bytes())
        command = [str(lean), "+" + audit_support.TOOLCHAIN]
        records = []
        with tempfile.TemporaryDirectory(prefix="generative-relational-renewal-lean-") as scratch:
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
            for name, data in {**dependencies_src, **sources}.items():
                (work / (name + ".lean")).write_bytes(data)
            for name in dependencies_src:
                run(["-o", name + ".olean", name + ".lean"], name + ".log")
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
                    assert axioms == [], (full, axioms)
                    dependencies[full] = axioms
                records.append({
                    "module": name, "theorems": sum(x["kind"] == "theorem" for x in registry[name]),
                    "declarations": registry[name], "axiom_dependencies": dependencies,
                    "kernel_checked": True,
                })
            controls = """import RelationalRenewal
open RelationalRenewal RelationalRenewal.Law
example : ¬ RenewingIn fluctuating () ∧ ¬ ConsumingIn fluctuating () := fluctuating_neither
example : ¬ ConsumingIn cultivation.unfolding .focal :=
  renewing_not_consuming formation_does_not_decide.2.1.1
example : ¬ RenewingIn winning.unfolding .focal := fun renewing =>
  renewing_not_consuming renewing own_trajectory_does_not_decide.2.2.2
example : ∀ t, winning.formed t = t :=
  (independent_overdraw_persists winning rfl (Nat.succ_pos 0) (T0 := 0)
    (fun _ _ => Nat.lt_succ_self 1)).2.1
"""
            bridge_controls = """import RenewalComparison
open GenerativeComparison RenewalComparison
example (Better : Growth → Growth → Prop)
    (c : ComparisonPrinciple (relationalInventory tumor) Better) : Better .occurs .absent :=
  (relational_comparison_ranks Better c).1
example : ¬ GenerativeExtension (broadInventory tumor) .occurs .absent :=
  fun ext => tumor_broad_incomparable.1 ext.1
example : ∃ Better : Growth → Growth → Prop,
    ComparisonPrinciple (broadInventory tumor) Better ∧ Better .absent .occurs :=
  ⟨preferMalignant, broad_comparison_admits_malignant.1, broad_comparison_admits_malignant.2.1⟩
example (PositiveRelevant : Contest → RelationalRenewal.Law.Part × Nat → Prop)
    (g0 : G0 (relationalInventory contest) PositiveRelevant) (t : Nat) :
    PositiveRelevant .shares (.sustaining, t) :=
  g0 _ _ trivial (sharing_grounds _)
"""
            (work / "Controls.lean").write_text(controls)
            (retained / "Controls.lean").write_text(controls)
            run(["Controls.lean"], "Controls.log")
            (work / "BridgeControls.lean").write_text(bridge_controls)
            (retained / "BridgeControls.lean").write_text(bridge_controls)
            run(["BridgeControls.lean"], "BridgeControls.log")
            receipt["checked_application_examples"] = 8
        receipt["source_unchanged_during_check"] = all(
            SOURCES[name].read_bytes() == data for name, data in sources.items()) and all(
            DEPENDENCIES[name].read_bytes() == data for name, data in dependencies_src.items())
        assert receipt["source_unchanged_during_check"], "Source changed; only snapshot checked"
        assert all((SUPPORT_PATH if name == "check.py" else Path(__file__)).read_bytes() == data for name, data in helpers.items()), "Checker changed"
        receipt["modules"] = records
        receipt["all_axiom_dependencies_empty"] = all(
            not deps for r in records for deps in r["axiom_dependencies"].values())
        assert receipt["all_axiom_dependencies_empty"]
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
        (HERE / "relational-renewal-verification.json").write_text(serialized)
    print(json.dumps({"status": receipt["status"],
                      "new_theorems": {r["module"]: r["theorems"] for r in records},
                      "new_declaration_audits": sum(len(r["declarations"]) for r in records),
                      "axioms": sorted({a for r in records for aa in r["axiom_dependencies"].values() for a in aa}),
                      "receipt": str(HERE / "relational-renewal-verification.json")}))


if __name__ == "__main__":
    main()
