#!/usr/bin/env python3
"""Fresh finite-classification public closure; every inherited and new audit empty."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time

HERE = Path(__file__).resolve().parent
CORE = HERE.parents[1]
REPO = next(p for p in HERE.parents if (p / "AGENTS.md").is_file())
BASELINE = HERE / "verification.json"
BASELINE_SHA256 = "1195e65f32790bc5d0df6e97bcb586f3b6e79f66e60aacf2aac7dbee6c6fb632"
NEW = {
    "FiniteInquiryClassification": HERE / "FiniteInquiryClassification.lean",
    "GenerativeFiniteInquiryModel": CORE / "GenerativeFiniteInquiryModel.lean",
}
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    baseline_bytes = BASELINE.read_bytes()
    assert sha(baseline_bytes) == BASELINE_SHA256, "Default receipt changed; review the new baseline."
    baseline = json.loads(baseline_bytes)
    assert baseline["status"] == "passed" and len(baseline["modules"]) == 18 and baseline["audits"] == 212
    assert baseline["whole_current_audited_closure_empty"] and baseline["all_previous196_audit_names_retained"]
    archive = CORE / "verification-history/2026-10-06-before-axiom-removal"
    manifest_bytes = (archive / "manifest.json").read_bytes()
    assert sha(manifest_bytes) == "269635cef5f1fab71dd4d375c4a4fa93bc9b33a41bbffc1656fca00b9a6d5764"
    manifest = json.loads(manifest_bytes)
    for item in manifest["files"]:
        assert sha((archive / item["snapshot"]).read_bytes()) == item["sha256"]
    old_names = {n for m in baseline["modules"] for n in m["axioms_by_declaration"]}
    assert len(old_names) == 212
    originals = {m["module"]: m for m in baseline["modules"]}
    paths = {name: REPO / m["source"] for name, m in originals.items()}
    paths.update(NEW)
    frozen = {name: path.read_bytes() for name, path in paths.items()}
    for name, original in originals.items():
        assert sha(frozen[name]) == original["source_sha256"], name
    checker_bytes = Path(__file__).read_bytes()
    toolchain_bytes = (CORE / "lean-toolchain").read_bytes()
    assert sha(toolchain_bytes) == baseline["toolchain_sha256"]
    compiler = Path(baseline["compiler"])
    assert sha(compiler.read_bytes()) == baseline["compiler_sha256"]
    version = subprocess.check_output([str(compiler), "--version"], text=True).strip()
    assert version == baseline["lean_version"]

    imports, requests = {}, {}
    for name, data in frozen.items():
        source = data.decode()
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", source), name
        assert not re.search(r"^\s*(axiom|constant|opaque)\s", source, re.M), name
        imports[name] = re.findall(r"^import\s+(\S+)\s*$", source, re.M)
        assert set(imports[name]) <= {"Std", *paths}, name
        requests[name] = re.findall(r"^#print axioms (\S+)\s*$", source, re.M)
        assert len(requests[name]) == len(set(requests[name])), name
    assert imports["FiniteInquiryClassification"] == ["InquirySufficiency"]
    assert imports["GenerativeFiniteInquiryModel"] == ["GenerativeInquirySufficiencyModel", "FiniteInquiryClassification"]
    mechanism = frozen["FiniteInquiryClassification"].decode()
    theorem_names = re.findall(r"^theorem\s+(\w+)", mechanism, re.M)
    audited_short = [x.rsplit(".", 1)[-1] for x in requests["FiniteInquiryClassification"]]
    assert set(theorem_names) == set(audited_short) - {"beliefDecision", "afterMembership"}
    assert len(theorem_names) == 11 and len(audited_short) == 13
    entry = re.sub(r"/\-.*?\-/", "", frozen["GenerativeFiniteInquiryModel"].decode(), flags=re.S)
    assert all(re.fullmatch(r"import\s+\w+", line.strip())
               for line in entry.splitlines() if line.strip())
    assert requests["GenerativeFiniteInquiryModel"] == []

    order, done = [], {"Std"}
    while len(order) < len(paths):
        ready = [name for name in paths if name not in done and set(imports[name]) <= done]
        assert ready, "Cyclic or incomplete imports"
        order.extend(ready)
        done.update(ready)

    attempt = HERE / "finite-runs" / str(time.time_ns())
    attempt.mkdir(parents=True)
    (attempt / "sources").mkdir()
    (attempt / "baseline-verification.json").write_bytes(baseline_bytes)
    (attempt / "check_finite.py").write_bytes(checker_bytes)
    (attempt / "lean-toolchain").write_bytes(toolchain_bytes)
    for name, data in frozen.items():
        (attempt / "sources" / (name + ".lean")).write_bytes(data)
    rows = []
    with tempfile.TemporaryDirectory(prefix="finite-inquiry-public-fresh-") as temporary:
        build = Path(temporary)
        for name, data in frozen.items():
            (build / (name + ".lean")).write_bytes(data)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in order:
            command = [str(compiler), "-o", name + ".olean", name + ".lean"]
            result = subprocess.run(command, cwd=build, env=env, text=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)
            log = attempt / (name + ".txt")
            log.write_text(result.stdout)
            audits = [(decl, sorted(a.strip() for a in deps.split(",") if a.strip()))
                      for decl, deps in AUDIT.findall(result.stdout)]
            audit_map = dict(audits)
            complete = len(audits) == len(audit_map) == len(requests[name]) and all(
                actual == wanted or actual.endswith("." + wanted)
                for (actual, _), wanted in zip(audits, requests[name]))
            contract = (all(not deps for _, deps in audits) and
                        (name not in originals or audit_map == originals[name]["axioms_by_declaration"]))
            passed = result.returncode == 0 and "warning:" not in result.stdout and complete and contract
            rows.append({"module": name, "source": str(paths[name].relative_to(REPO)),
                         "source_sha256": sha(frozen[name]), "new_module": name in NEW,
                         "command": command, "exit_code": result.returncode,
                         "import_only": name == "GenerativeFiniteInquiryModel",
                         "axioms_by_declaration": audit_map, "audit_complete": complete,
                         "exact_dependency_contract": contract, "passed": passed,
                         "log": str(log.relative_to(HERE)), "log_sha256": sha(log.read_bytes()),
                         "source_snapshot": str((attempt / "sources" / (name + ".lean")).relative_to(HERE))})
            print(json.dumps({"module": name, "passed": passed, "audits": len(audits)}), flush=True)
            if not passed:
                print(result.stdout, flush=True)
                break

    unchanged = (all(path.read_bytes() == frozen[name] for name, path in paths.items()) and
                 BASELINE.read_bytes() == baseline_bytes and Path(__file__).read_bytes() == checker_bytes and
                 (CORE / "lean-toolchain").read_bytes() == toolchain_bytes and
                 (archive / "manifest.json").read_bytes() == manifest_bytes and
                 all(sha((archive / x["snapshot"]).read_bytes()) == x["sha256"] for x in manifest["files"]))
    names = {n for row in rows for n in row["axioms_by_declaration"]}
    passed = (len(rows) == len(paths) == 20 and unchanged and old_names <= names and
              sum(len(row["axioms_by_declaration"]) for row in rows) == 225 and
              all(row["passed"] for row in rows))
    record = {
        "status": "passed" if passed else "failed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "compiler": str(compiler), "compiler_sha256": baseline["compiler_sha256"], "lean_version": version,
        "checker_sha256": sha(checker_bytes), "toolchain_sha256": sha(toolchain_bytes),
        "baseline": str(BASELINE.relative_to(REPO)), "baseline_sha256": sha(baseline_bytes),
        "baseline_snapshot": str((attempt / "baseline-verification.json").relative_to(HERE)),
        "default_receipt_overwritten": False, "fresh_temporary_build": True,
        "local_precompiled_imports_used": False, "inputs_unchanged": unchanged,
        "modules": rows, "inherited_modules": len(originals),
        "all_previous212_audit_names_retained": old_names <= names,
        "preservation_archive": str(archive.relative_to(REPO)), "preservation_manifest_sha256": sha(manifest_bytes),
        "whole_current_audited_closure_empty": len(rows) == len(paths) and all(
            not deps for row in rows for deps in row["axioms_by_declaration"].values()),
        "axiom_policy": "Every current inherited or extension audit must be empty; no grandfathered exceptions.",
        "audits": sum(len(row["axioms_by_declaration"]) for row in rows),
        "new_audits": sum(len(row["axioms_by_declaration"]) for row in rows if row["new_module"]),
        "new_axiom_dependencies": sorted({a for row in rows if row["new_module"]
                                           for deps in row["axioms_by_declaration"].values() for a in deps}),
        "scope": "Exact finite successor enumeration derives ClassifiedThrough at every finite depth "
                 "from executable membership and native transition decisions on Fin N. The Boolean-initial "
                 "policy theorem requires no supplied classification or exact enumeration certificate. "
                 "Every audit in the complete public closure is empty; all previous212 audit names and "
                 "their exact maps are retained. No new event law, policy-search algorithm, installed "
                 "planner, acquired criterion, or assumption-free foundation is claimed."
    }
    (attempt / "receipt.json").write_text(json.dumps(record, indent=2) + "\n")
    if passed:
        (HERE / "finite-verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "modules": len(rows),
                      "audits": record["audits"], "new_audits": record["new_audits"],
                      "receipt": str((attempt / "receipt.json").relative_to(REPO))}), flush=True)
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
