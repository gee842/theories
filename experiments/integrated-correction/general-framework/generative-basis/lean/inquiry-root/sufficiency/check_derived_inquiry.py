#!/usr/bin/env python3
"""Fresh proof closure for derived inquiry certificates; no scientific rerun."""
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
REPO = CORE.parents[4]
BASELINE = HERE / "question-runs/1791281585451526000/receipt.json"
BASELINE_SHA256 = "57a5d6532e98ad281c8e8f982127a21563307ff07813e3ffe39d245cbd710006"
NEW = {name: HERE / (name + ".lean") for name in (
    "DerivedInquiryCertificates", "ReachedInquiryComposition",
    "OnePacketAdmissibility", "OnePacketInquirySynthesis")}
NEW["GenerativeDerivedInquiryModel"] = CORE / "GenerativeDerivedInquiryModel.lean"
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    baseline_bytes = BASELINE.read_bytes()
    assert sha(baseline_bytes) == BASELINE_SHA256
    baseline = json.loads(baseline_bytes)
    assert baseline["status"] == "passed" and len(baseline["modules"]) == 23
    assert baseline["audits"] == 307 and baseline["whole_current_audited_closure_empty"]
    original = {row["module"]: row for row in baseline["modules"]}
    paths = {name: REPO / row["source"] for name, row in original.items()}
    paths.update(NEW)
    frozen = {name: path.read_bytes() for name, path in paths.items()}
    for name, row in original.items():
        assert sha(frozen[name]) == row["source_sha256"], name
        assert (HERE / row["source_snapshot"]).read_bytes() == frozen[name], name
        assert sha((HERE / row["log"]).read_bytes()) == row["log_sha256"], name
    # Preserve the prior scientific bindings. This round is a proof extension,
    # not a new execution of the native apparatus or its scientific producer.
    evidence_path = BASELINE.parent / "attainable-inputs.json"
    evidence_bytes = evidence_path.read_bytes()
    assert sha(evidence_bytes) == baseline["evidence_manifest_sha256"]
    evidence_files = json.loads(evidence_bytes)["files"]
    for item in evidence_files:
        assert sha((REPO / item["path"]).read_bytes()) == item["sha256"], item["path"]
        assert sha((BASELINE.parent / "evidence" / item["path"]).read_bytes()) == item["sha256"]
    checker_bytes = Path(__file__).read_bytes()
    toolchain_bytes = (CORE / "lean-toolchain").read_bytes()
    assert sha(toolchain_bytes) == baseline["toolchain_sha256"]
    compiler = Path(baseline["compiler"])
    assert sha(compiler.read_bytes()) == baseline["compiler_sha256"]
    version = subprocess.check_output([str(compiler), "--version"], text=True).strip()
    assert version == baseline["lean_version"]
    imports, requests, declarations = {}, {}, {}
    for name, data in frozen.items():
        source = data.decode()
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", source), name
        assert not re.search(r"^\s*(axiom|constant|opaque)\s", source, re.M), name
        imports[name] = re.findall(r"^import\s+(\S+)\s*$", source, re.M)
        assert set(imports[name]) <= {"Std", *paths}, (name, imports[name])
        requests[name] = re.findall(r"^#print axioms (\S+)\s*$", source, re.M)
        assert len(requests[name]) == len(set(requests[name])), name
        if name in NEW:
            ds = re.findall(r"^(?:private\s+)?(theorem|def|abbrev|inductive|structure)\s+(\w+)\b", source, re.M)
            declarations[name] = {kind: sum(k == kind for k, _ in ds) for kind in ("theorem", "def", "abbrev", "inductive", "structure")}
            declared = {n for _, n in ds}
            audited = {n.rsplit(".", 1)[-1] for n in requests[name]}
            assert declared == audited, (name, declared - audited, audited - declared)
    entry = re.sub(r"/\-.*?\-/", "", frozen["GenerativeDerivedInquiryModel"].decode(), flags=re.S)
    assert all(re.fullmatch(r"import\s+\w+", line.strip()) for line in entry.splitlines() if line.strip())
    assert imports["GenerativeDerivedInquiryModel"] == ["GenerativeAttainableQuestionsModel", *list(NEW)[:-1]]
    order, done = [], {"Std"}
    while len(order) < len(paths):
        ready = [n for n in paths if n not in done and set(imports[n]) <= done]
        assert ready, "Incomplete or cyclic source closure"
        order.extend(ready)
        done.update(ready)
    attempt = HERE / "derived-inquiry-runs" / str(time.time_ns())
    (attempt / "sources").mkdir(parents=True)
    (attempt / "baseline-verification.json").write_bytes(baseline_bytes)
    (attempt / "check_derived_inquiry.py").write_bytes(checker_bytes)
    (attempt / "lean-toolchain").write_bytes(toolchain_bytes)
    (attempt / "attainable-inputs.json").write_bytes(evidence_bytes)
    for name, data in frozen.items():
        (attempt / "sources" / (name + ".lean")).write_bytes(data)
    rows = []
    with tempfile.TemporaryDirectory(prefix="derived-inquiry-fresh-") as temporary:
        build = Path(temporary)
        for name, data in frozen.items():
            (build / (name + ".lean")).write_bytes(data)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in order:
            command = [str(compiler), "-o", name + ".olean", name + ".lean"]
            result = subprocess.run(command, cwd=build, env=env, text=True,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=240)
            log = attempt / (name + ".txt")
            log.write_text(result.stdout)
            audits = [(decl, sorted(a.strip() for a in deps.split(",") if a.strip()))
                      for decl, deps in AUDIT.findall(result.stdout)]
            audit_map = dict(audits)
            complete = len(audits) == len(audit_map) == len(requests[name]) and all(
                actual == expected or actual.endswith("." + expected)
                for (actual, _), expected in zip(audits, requests[name]))
            contract = all(not deps for _, deps in audits) and (
                name not in original or audit_map == original[name]["axioms_by_declaration"])
            passed = result.returncode == 0 and "warning:" not in result.stdout and complete and contract
            rows.append({"module": name, "source": str(paths[name].relative_to(REPO)),
                "source_sha256": sha(frozen[name]), "new_module": name in NEW,
                "command": command, "exit_code": result.returncode,
                "axioms_by_declaration": audit_map, "audit_complete": complete,
                "exact_dependency_contract": contract, "passed": passed,
                "source_snapshot": str((attempt / "sources" / (name + ".lean")).relative_to(HERE)),
                "log": str(log.relative_to(HERE)), "log_sha256": sha(log.read_bytes())})
            print(json.dumps({"module": name, "passed": passed, "audits": len(audits)}), flush=True)
            if not passed:
                print(result.stdout, flush=True)
                break
    unchanged = (all(path.read_bytes() == frozen[n] for n, path in paths.items()) and
        BASELINE.read_bytes() == baseline_bytes and Path(__file__).read_bytes() == checker_bytes and
        (CORE / "lean-toolchain").read_bytes() == toolchain_bytes and
        evidence_path.read_bytes() == evidence_bytes and all(
            sha((REPO / item["path"]).read_bytes()) == item["sha256"] for item in evidence_files))
    old_names = {n for row in original.values() for n in row["axioms_by_declaration"]}
    names = {n for row in rows for n in row["axioms_by_declaration"]}
    passed = len(rows) == len(paths) and unchanged and old_names <= names and all(row["passed"] for row in rows)
    record = {"status": "passed" if passed else "failed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "compiler": str(compiler), "compiler_sha256": baseline["compiler_sha256"], "lean_version": version,
        "toolchain_sha256": sha(toolchain_bytes), "checker_sha256": sha(checker_bytes),
        "baseline": str(BASELINE.relative_to(REPO)), "baseline_sha256": sha(baseline_bytes),
        "baseline_snapshot": str((attempt / "baseline-verification.json").relative_to(HERE)),
        "fresh_temporary_build": True, "local_precompiled_imports_used": False,
        "inputs_unchanged": unchanged, "inherited_modules": 23,
        "all_previous307_audit_names_retained": old_names <= names,
        "whole_current_audited_closure_empty": passed and all(not d for row in rows for d in row["axioms_by_declaration"].values()),
        "axiom_policy": "Every inherited audit is retained exactly; every new named theorem, definition, abbreviation and inductive/structure declaration must have an empty dependency report.",
        "audits": sum(len(row["axioms_by_declaration"]) for row in rows),
        "new_audits": sum(len(row["axioms_by_declaration"]) for row in rows if row["new_module"]),
        "new_declarations": declarations, "modules": rows,
        "evidence_manifest_sha256": sha(evidence_bytes), "preserved_evidence_files": len(evidence_files),
        "scientific_producer_executed": False,
        "scope": "Derived finite inquiry certificates, reached-leaf composition, nonvacuous packet availability and concrete synthesis. Supplied dynamics, interpretation and ethical grounding are not declared assumption-free."}
    data = (json.dumps(record, indent=2) + "\n").encode()
    (attempt / "receipt.json").write_bytes(data)
    if passed:
        (HERE / "derived-inquiry-verification.json").write_bytes(data)
    print(json.dumps({"status": record["status"], "modules": len(rows), "audits": record["audits"],
        "new_audits": record["new_audits"], "receipt": str((attempt / "receipt.json").relative_to(HERE))}), flush=True)
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
