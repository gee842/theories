#!/usr/bin/env python3
"""Checks the monist evaluator-grounding route: self-good, formed relations and the reach of G0."""
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
    "EvaluatorGrounding": HERE / "EvaluatorGrounding.lean",
}
IMPORTS = {
    "GenerativeComparison": ["Std"],
    "EvaluatorGrounding": ["GenerativeComparison"],
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
    retained = HERE / "evaluator-grounding-checks" / stamp
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
        "scope": "Monist evaluator grounding. From a standpoint's reason-giving self-good (S0) over its own living and further generation, with significance determined by formed relations rather than a primitive owner: (1) unrestricted monotonicity (over own and other occurrences) in the relations grounding self-good extends significance to any living occurrence at least as connected as a valued own occurrence, and a strictly own-only rival is inconsistent once its further generation differentiates into such an occurrence; (2) supervenience, tolerance (no positive-to-none flip across one small relational step) and graded connection extend significance to every reachable living occurrence, which is exactly G0 for the reachable inventory with this standpoint's significance as positive relevance. Countermodels keep consistent a threshold rival without tolerance, a present-aim evaluator without self-good, a closed self without graded connection, and a persistence-grounded rival escaping the tolerance-free step. The derived G0 is a standpoint-indexed single-history instance, not the unindexed G0 over continuations. S0, tolerance, unrestricted monotonicity (equivalently supervenience, a profile-monotone valuation and boundary irrelevance), differentiation and graded-connection correspondence are supplied; no theorem proves them, assigns weights, permission or duty, or binds an evaluator without self-good."
    }
    try:
        registry = {name: declarations(data.decode(), IMPORTS[name]) for name, data in sources.items()}
        lean = Path.home() / ".elan/bin/lean"
        binary = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
        receipt["lean_binary_sha256"] = audit_support.digest(binary.read_bytes())
        command = [str(lean), "+" + audit_support.TOOLCHAIN]
        records = []
        with tempfile.TemporaryDirectory(prefix="generative-evaluator-grounding-lean-") as scratch:
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
            controls = """import EvaluatorGrounding
open EvaluatorGrounding GenerativeComparison

-- With tolerance, the finite standpoint's self-good yields G0 for its reachable inventory.
example (val : Nat → Prop) (self : SelfGood (standpoint val)) (tol : Tolerant val adjacent)
    (chain : ∀ g', (standpoint val).reach g' → (standpoint val).living g' →
      ∃ g, (standpoint val).own g ∧ (standpoint val).living g ∧
        Chain adjacent ((standpoint val).prof g) ((standpoint val).prof g')) :
    G0 (reachableInventory (standpoint val)) (fun _ g => (standpoint val).sig g) :=
  self_good_derives_reachable_g0 (standpoint val) val adjacent (fun _ _ => Iff.rfl) self tol chain

-- The threshold rival is exactly where the tolerance-free step stops: formed other yes, stranger no.
example : (standpoint (4 ≤ ·)).sig .formedOther ∧ ¬ (standpoint (4 ≤ ·)).sig .stranger :=
  ⟨threshold_rival_is_consistent_without_tolerance.2.2.2.1,
   threshold_rival_is_consistent_without_tolerance.2.2.2.2.1⟩

-- The strictly own-only rival fails in the finite unfolding once self-good and monotonicity hold.
example (val : Nat → Prop) (self : SelfGood (standpoint val))
    (mono : Monotone (standpoint val) (· ≤ ·))
    (onlyOwn : ∀ g, (standpoint val).sig g → (standpoint val).own g) : False :=
  strict_indexed_rival_inconsistent (standpoint val) (· ≤ ·) self mono onlyOwn
    ⟨.changedSelf, .formedOther, trivial, trivial, trivial, id, show 4 ≤ 5 by decide⟩
"""
            (work / "Controls.lean").write_text(controls)
            (retained / "Controls.lean").write_text(controls)
            run(["Controls.lean"], "Controls.log")
            receipt["checked_application_examples"] = [
                {"claim": "finite standpoint with tolerance yields G0 for its reachable inventory", "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "threshold rival reaches the formed other but not the stranger", "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "own-only rival with self-good and monotonicity is inconsistent in the finite unfolding", "kernel_checked": True, "counted_as_new_theorem": False},
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
        (HERE / "evaluator-grounding-verification.json").write_text(serialized)
    model = next(r for r in records if r["module"] == "EvaluatorGrounding")
    print(json.dumps({"status": receipt["status"], "new_theorems": model["theorems"],
                      "new_declaration_audits": len(model["declarations"]),
                      "axioms": sorted({a for r in records for aa in r["axiom_dependencies"].values() for a in aa}),
                      "receipt": str(HERE / "evaluator-grounding-verification.json")}))


if __name__ == "__main__":
    main()
