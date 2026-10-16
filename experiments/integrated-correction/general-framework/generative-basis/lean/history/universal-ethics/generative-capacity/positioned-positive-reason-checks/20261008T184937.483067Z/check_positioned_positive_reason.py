#!/usr/bin/env python3
"""Checks positive ground addressed to every situated position, with endorsement independence located in the positioned articulation premise."""
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
    "PositionedPositiveReason": HERE / "PositionedPositiveReason.lean",
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
    retained = HERE / "positioned-positive-reason-checks" / stamp
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
        "scope": "Positions are differentiated response positions formed within one unfolding. Under explicit G0, formation correspondence E and a positioned direct articulation D that mentions only access and secured positive ground, every position with access to a response has a contributory reason for it. The least D-reason is fixed by access alone, so positions alike in access are alike in this reason whatever their endorsement, substrate or other labels. A position without access receives no reason from this route, which does not show it has no reason at all. On the existing positive-ground construction, a non-endorsing artificial position with access has the reason, while an endorsement-conditional articulation is compatible with the same G0 and formation facts and withholds it; endorsement independence is therefore the content of D, not a consequence of G0. No permission, duty, ranking, recognition or compliance is inferred."
    }
    try:
        registry = {name: declarations(data.decode(), {
            "JointContinuationClassification": ["Std"],
            "GenerativeComparison": ["Std"],
            "PracticalJudgment": ["Std"],
            "StandardsBridge": ["Std"],
            "PositiveGroundUncertainty": ["GenerativeComparison", "PracticalJudgment", "JointContinuationClassification", "StandardsBridge"],
            "PositionedPositiveReason": ["GenerativeComparison", "PositiveGroundUncertainty"],
        }[name]) for name, data in sources.items()}
        lean = Path.home() / ".elan/bin/lean"
        binary = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
        receipt["lean_binary_sha256"] = audit_support.digest(binary.read_bytes())
        command = [str(lean), "+" + audit_support.TOOLCHAIN]
        records = []
        with tempfile.TemporaryDirectory(prefix="generative-positioned-positive-reason-lean-") as scratch:
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
            controls = """import PositionedPositiveReason
open PositionedPositiveReason GenerativeComparison

-- Any position with access, of either substrate and either endorsement value, has the reason.
example (s : Substrate) (e : Bool) :
    RouteReason access admittedAfter priorIn g0Relevant ⟨s, e, true⟩ .respond :=
  every_situated_position_has_reason access admittedAfter priorIn wholeInventory g0Relevant
    (RouteReason access admittedAfter priorIn g0Relevant) g0_holds
    (route_reason_is_least access admittedAfter priorIn g0Relevant).1
    .respond respond_formation ⟨s, e, true⟩ rfl

-- Changing only endorsement and substrate leaves the route reason unchanged.
example :
    RouteReason access admittedAfter priorIn g0Relevant ⟨.human, true, true⟩ .respond ↔
      RouteReason access admittedAfter priorIn g0Relevant ⟨.artificial, false, true⟩ .respond :=
  route_reason_depends_only_on_access access admittedAfter priorIn g0Relevant _ _
    (fun a => by cases a <;> exact Iff.rfl) .respond
"""
            (work / "Controls.lean").write_text(controls)
            (retained / "Controls.lean").write_text(controls)
            run(["Controls.lean"], "Controls.log")
            receipt["checked_application_examples"] = [
                {"claim": "every position with access has the reason for both substrates and endorsement values", "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "changing only endorsement and substrate preserves the route reason", "kernel_checked": True, "counted_as_new_theorem": False},
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
        (HERE / "positioned-positive-reason-verification.json").write_text(serialized)
    model = next(r for r in records if r["module"] == "PositionedPositiveReason")
    print(json.dumps({"status": receipt["status"], "new_theorems": model["theorems"],
                      "new_declaration_audits": len(model["declarations"]),
                      "axioms": sorted({a for r in records for aa in r["axiom_dependencies"].values() for a in aa}),
                      "receipt": str(HERE / "positioned-positive-reason-verification.json")}))


if __name__ == "__main__":
    main()
