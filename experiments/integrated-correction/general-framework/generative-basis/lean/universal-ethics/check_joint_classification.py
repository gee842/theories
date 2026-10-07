#!/usr/bin/env python3
"""Fresh source-bound Lean check for joint continuation classification.

Uses the established declaration scanner, preserved in every run. Audits explicit
named declarations, not a separate enumeration of generated constructors. Empty
axiom dependencies are not a claim of zero philosophical/model assumptions.
"""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
MODULE = "JointContinuationClassification"
TOOLCHAIN = "leanprover/lean4:v4.29.1"
SCANNER = HERE / "generative-capacity/check.py"
if not SCANNER.exists():
    SCANNER = HERE / "joint_classification_audit_support.py"
spec = importlib.util.spec_from_file_location("joint_classification_support", SCANNER)
support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    retained = HERE / "joint-classification-checks" / stamp
    retained.mkdir(parents=True, exist_ok=False)
    paths = {
        MODULE + ".lean": HERE / (MODULE + ".lean"),
        Path(__file__).name: Path(__file__),
        "joint_classification_audit_support.py": SCANNER,
    }
    snapshots = {name: path.read_bytes() for name, path in paths.items()}
    for name, data in snapshots.items():
        (retained / name).write_bytes(data)
    receipt = {
        "status": "checking", "utc": stamp, "toolchain": TOOLCHAIN,
        "retained_run": str(retained.relative_to(HERE)),
        "source_sha256": {MODULE: digest(snapshots[MODULE + ".lean"])},
        "checker_sha256": {name: digest(data) for name, data in snapshots.items()
                           if name.endswith(".py")},
        "scope": "Conditional joint-profile representation audit and one supplied common-history event law; no ethical ranking or first ethical warrant.",
        "audit_scope": "Every explicit named top-level declaration; generated constructors and projections are kernel checked with the module, not separately inventoried.",
    }
    records = []
    try:
        registry = support.declarations(snapshots[MODULE + ".lean"].decode())
        lean = Path.home() / ".elan/bin/lean"
        binary = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
        receipt["lean_binary_sha256"] = digest(binary.read_bytes())
        prefix = [str(lean), "+" + TOOLCHAIN]
        with tempfile.TemporaryDirectory(prefix="joint-classification-lean-") as scratch:
            work = Path(scratch)
            env = {**os.environ, "LEAN_PATH": str(work)}

            def run(arguments, log):
                command = prefix + arguments
                result = subprocess.run(command, cwd=work, env=env, text=True,
                                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                        timeout=120)
                (retained / log).write_text(result.stdout)
                records.append({"command": command, "returncode": result.returncode,
                                "log": log})
                assert result.returncode == 0, result.stdout
                assert not re.search(r"\b(?:error|warning):", result.stdout), result.stdout
                return result.stdout

            receipt["lean_version"] = run(["--version"], "version.log").strip()
            assert "version 4.29.1" in receipt["lean_version"]
            (work / (MODULE + ".lean")).write_bytes(snapshots[MODULE + ".lean"])
            run(["-o", MODULE + ".olean", MODULE + ".lean"], "compiler.log")
            audit = "import " + MODULE + "\n" + "\n".join(
                "#print axioms " + item["name"] for item in registry) + "\n"
            (work / "AxiomAudit.lean").write_text(audit)
            (retained / "AxiomAudit.lean").write_text(audit)
            output = run(["AxiomAudit.lean"], "axioms.log")
            signatures = "import " + MODULE + "\n" + "\n".join(
                "#check " + item["name"] for item in registry
                if item["kind"] == "theorem") + "\n"
            (work / "Signatures.lean").write_text(signatures)
            (retained / "Signatures.lean").write_text(signatures)
            run(["Signatures.lean"], "signatures.log")
            dependencies = {}
            for item in registry:
                name = item["name"]
                if "'" + name + "' does not depend on any axioms" in output:
                    axioms = []
                else:
                    match = re.search(r"'" + re.escape(name) +
                                      r"' depends on axioms:\s*\[([^]]*)\]", output)
                    assert match, (name, output)
                    axioms = [entry.strip() for entry in match[1].split(",") if entry.strip()]
                assert not axioms, ("Final joint-classification module requires empty axiom dependencies", name, axioms)
                dependencies[name] = axioms
            receipt["declarations"] = registry
            receipt["theorems"] = sum(item["kind"] == "theorem" for item in registry)
            receipt["axiom_dependencies"] = dependencies
            receipt["kernel_checked"] = True
        receipt["sources_unchanged_during_check"] = all(
            paths[name].read_bytes() == data for name, data in snapshots.items())
        assert receipt["sources_unchanged_during_check"]
        receipt["status"] = "passed"
    except Exception as error:
        receipt["status"] = "failed"
        receipt["error"] = repr(error)
        raise
    finally:
        receipt["commands"] = records
        receipt["artifact_sha256"] = {
            path.name: digest(path.read_bytes()) for path in sorted(retained.iterdir())
            if path.is_file()
        }
        encoded = json.dumps(receipt, indent=2) + "\n"
        (retained / "verification.json").write_text(encoded)
        (HERE / "joint-classification-verification.json").write_text(encoded)
    print(json.dumps({"status": receipt["status"], "theorems": receipt["theorems"],
                      "explicit_declarations": len(receipt["declarations"]),
                      "axioms": sorted({axiom for entries in receipt["axiom_dependencies"].values()
                                        for axiom in entries}),
                      "receipt": str(HERE / "joint-classification-verification.json")}))


if __name__ == "__main__":
    main()
