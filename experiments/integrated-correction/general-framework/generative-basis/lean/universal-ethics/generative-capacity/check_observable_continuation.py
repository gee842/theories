#!/usr/bin/env python3
"""Checks observable funded continuation using the existing contingent selector."""
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
    retained = HERE / "observable-continuation-checks" / stamp
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
        "scope": "Four new results reuse the unchanged finite contingent selector and chance bridge. Selected actual execution, actual-candidate coverage and a separately supplied task-effect correspondence imply pointwise continuation and common-positive-total numerator bounds. In a fixed two-mode resource law, blind one-unit maintenance remains feasible while the full old-or-candidate extension has no listed single-route plan. Two units allow a charged current-mode observation followed by a single route, or a genuinely available parallel route without observation; both actually consume their budget and improve event mass from one to two. Stable faithful observation, permission, finite model coverage and resource law are supplied. This does not re-prove general observation-class criteria, prove ethical authority, bound search cost or model arbitrary noise/drift. The imported AlignmentInquiry and ChanceAdequacy declarations are rebuilt and audited separately as inherited."
    }
    try:
        registry = {name: declarations(data.decode(), {"AlignmentInquiry": ["Std"], "ChanceAdequacy": ["Std"], "ObservableContinuation": ["AlignmentInquiry", "ChanceAdequacy"]}[name])
                    for name, data in sources.items()}
        lean = Path.home() / ".elan/bin/lean"
        binary = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
        receipt["lean_binary_sha256"] = audit_support.digest(binary.read_bytes())
        command = [str(lean), "+" + audit_support.TOOLCHAIN]
        records = []
        with tempfile.TemporaryDirectory(prefix="generative-observable-continuation-lean-") as scratch:
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
            controls = """import ObservableContinuation
open ObservableContinuation

-- Paying for a reading with the only unit leaves no unit for the response.
example : AlignmentInquiry.run (interface extension) inspect (initial 1 false) = none := by rfl

-- Instantiate the generic bridge with independently checked actual support.
example : ChanceAdequacy.mass [false, true] (fun _ => 1)
      (ChanceAdequacy.target (fun _ => true) oldWorks) ≤
    ChanceAdequacy.mass [false, true] (fun _ => 1) (support inspect 2) := by
  have joined := selected_execution_gives_continuation_bound
    [false, true] (fun _ => 1) (fun _ => true) oldWorks (support inspect 2)
    (initial 2) (interface extension) (states 2) singlePlans inspect
    funded_observation_realizes_extension.1
    (by intro mode _; cases mode <;> simp [states])
    (by
      intro mode _ _ final _ _
      have actual := (funded_observation_realizes_extension.2.1 mode).2
      simp [support, actual])
    (by decide)
  exact joined.2.2.1
"""
            (work / "Controls.lean").write_text(controls)
            (retained / "Controls.lean").write_text(controls)
            run(["Controls.lean"], "Controls.log")
            receipt["checked_application_examples"] = [
                {"claim": "with one budget unit the sensing plan cannot execute its subsequent response",
                 "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "the generic selected-execution chance bridge instantiates to the funded sensing route using its actual output theorem",
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
        (HERE / "observable-continuation-verification.json").write_text(serialized)
    model = next(r for r in records if r["module"] == "ObservableContinuation")
    print(json.dumps({"status": receipt["status"], "new_theorems": model["theorems"],
                      "new_declaration_audits": len(model["declarations"]),
                      "axioms": sorted({a for r in records for aa in r["axiom_dependencies"].values() for a in aa}),
                      "receipt": str(HERE / "observable-continuation-verification.json")}))


if __name__ == "__main__":
    main()
