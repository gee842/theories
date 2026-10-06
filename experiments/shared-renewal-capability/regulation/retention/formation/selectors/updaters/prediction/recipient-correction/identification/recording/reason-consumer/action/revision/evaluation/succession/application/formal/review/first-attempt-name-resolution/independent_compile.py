#!/usr/bin/env python3
"""Independent fresh compilation of the frozen application-evidence source map."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
FORMAL = HERE.parent
REPO = next(p for p in FORMAL.parents if (p / "AGENTS.md").exists())
PARENT = "dc4a16cf97d3af8bd88bffbef2500b6bb5381e32"
EXPECTED_RECEIPT = "ca0cda4100c9308588612a87952fe6f2beac4394b9520c64915eb60a1ecf385e"
EXPECTED_NEW = "dcbf17d1c8e4d57798f7c7d4208e80f6c3ea318ae9202868cf9b83d8e7700fe6"
ALLOWED = {"propext", "Quot.sound", "Classical.choice"}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def main():
    receipt_bytes = (FORMAL / "verification.json").read_bytes()
    assert digest(receipt_bytes) == EXPECTED_RECEIPT
    receipt = json.loads(receipt_bytes)
    frozen = {}
    modules = receipt["modules"]
    assert len(modules) == 30
    for module in modules:
        source = (REPO / module["source"]).read_bytes()
        assert digest(source) == module["source_sha256"]
        frozen[module["module"]] = source
        if module["module"] != "ApplicationEvidence":
            old = subprocess.run(
                ["git", "show", PARENT + ":" + module["source"]],
                cwd=REPO, capture_output=True, check=True).stdout
            assert old == source
    assert digest(frozen["ApplicationEvidence"]) == EXPECTED_NEW
    contracts = {name: (FORMAL / name).read_bytes()
                 for name in ["PROOF-CONTRACT.md", "check.py", "lean-toolchain"]}
    toolchain = contracts["lean-toolchain"].decode().strip()
    assert toolchain == "leanprover/lean4:v4.29.1"
    prefix = subprocess.run(["lean", "+" + toolchain, "--print-prefix"],
                            cwd=FORMAL, capture_output=True, text=True, check=True).stdout.strip()
    compiler = Path(prefix) / "bin" / "lean"
    version = subprocess.run([str(compiler), "--version"], capture_output=True,
                             text=True, check=True).stdout.strip()
    before = {
        "reviewer": "material_updater_model",
        "author_receipt_sha256": digest(receipt_bytes),
        "parent_commit": PARENT,
        "all_29_inherited_sources_match_commit": True,
        "source_sha256": {m["source"]: digest(frozen[m["module"]]) for m in modules},
        "contract_sha256": {name: digest(data) for name, data in contracts.items()},
        "compiler_sha256": digest(compiler.read_bytes()),
        "compiler_version": version,
        "checker_sha256": digest(Path(__file__).read_bytes()),
        "started_at_utc": datetime.now(timezone.utc).isoformat(),
        "fresh_build": True,
        "numerical_model_rerun": False,
    }
    (HERE / "before.json").write_text(json.dumps(before, indent=2) + "\n")
    results = []
    logs = HERE / "logs"
    logs.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="application-evidence-independent-") as temp:
        build = Path(temp)
        for name, source in frozen.items():
            (build / (name + ".lean")).write_bytes(source)
        env = dict(os.environ, LEAN_PATH=str(build))
        for module in modules:
            name = module["module"]
            text = frozen[name].decode()
            assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", text), name
            assert not re.search(r"^\s*(axiom|constant)\s", text, re.M), name
            requested = re.findall(r"^#print axioms\s+([\w.]+)\s*$", text, re.M)
            declarations = set(re.findall(r"^theorem\s+(\w+)", text, re.M))
            if name != "GenerativeCore":
                assert {x.rsplit(".", 1)[-1] for x in requested} == declarations
            started = datetime.now(timezone.utc)
            completed = subprocess.run(
                [str(compiler), "-o", name + ".olean", name + ".lean"],
                cwd=build, env=env, capture_output=True, text=True, timeout=300)
            output = completed.stdout + completed.stderr
            log = logs / (name + ".txt")
            log.write_text(output)
            audit = re.findall(
                r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
                output)
            dependencies = {item.strip() for _, group in audit
                            for item in group.split(",") if item.strip()}
            clean = (completed.returncode == 0 and "warning:" not in output
                     and "error:" not in output and "sorryAx" not in output
                     and len(audit) == len(requested)
                     and {x for x, _ in audit} == set(requested)
                     and dependencies <= ALLOWED)
            results.append({
                "module": name, "source_sha256": digest(frozen[name]),
                "exit_code": completed.returncode, "passed": clean,
                "audit_count": len(audit), "axioms": sorted(dependencies),
                "empty_audits": sum(not group for _, group in audit),
                "log": str(log.relative_to(HERE)), "log_sha256": digest(log.read_bytes()),
                "seconds": (datetime.now(timezone.utc) - started).total_seconds(),
            })
            print(name, "passed" if clean else "FAILED", len(audit), flush=True)
            if not clean:
                break
    unchanged = (
        (FORMAL / "verification.json").read_bytes() == receipt_bytes
        and all((REPO / m["source"]).read_bytes() == frozen[m["module"]] for m in modules)
        and all((FORMAL / name).read_bytes() == data for name, data in contracts.items()))
    passed = len(results) == 30 and unchanged and all(r["passed"] for r in results)
    record = dict(before, status="passed" if passed else "failed",
                  finished_at_utc=datetime.now(timezone.utc).isoformat(),
                  unchanged_during_review=unchanged, modules=results,
                  total_audits=sum(r["audit_count"] for r in results),
                  new_audits=next((r["audit_count"] for r in results
                                   if r["module"] == "ApplicationEvidence"), 0),
                  scope="Independent fresh compilation and complete requested dependency audit; "
                        "statement/provenance/application review is reported separately. "
                        "No model execution and no new empirical result.")
    (HERE / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    if not passed:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
