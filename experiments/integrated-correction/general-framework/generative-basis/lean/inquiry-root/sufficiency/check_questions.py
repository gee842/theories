#!/usr/bin/env python3
"""Fresh attainable-question closure with empty audits and saved-evidence checks."""

from datetime import datetime, timezone
import hashlib
from itertools import product
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
BASELINE = HERE / "finite-runs/1791274808194068000/receipt.json"
BASELINE_SHA256 = "b7cd95e327f86e712c3367f3458a3b8e8d3eadc042e0c59a48ef74a8f9a66450"
EVIDENCE = HERE / "attainable-inputs.json"
EVIDENCE_SHA256 = "a1ce0e30d8443f3f6f4560689d33ad66a40549c8f5829a3fce69f390300b52e2"
CRITERIA = CORE.parent / "mathematical-abstraction/acquisition/access/inquiry/criteria"
NEW = {
    "AttainableQuestions": HERE / "AttainableQuestions.lean",
    "OnePacketQuestions": HERE / "OnePacketQuestions.lean",
    "GenerativeAttainableQuestionsModel": CORE / "GenerativeAttainableQuestionsModel.lean",
}
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def evidence_check():
    manifest_bytes = EVIDENCE.read_bytes()
    assert sha(manifest_bytes) == EVIDENCE_SHA256
    manifest = json.loads(manifest_bytes)
    frozen = {row["path"]: (REPO / row["path"]).read_bytes() for row in manifest["files"]}
    assert len(frozen) == 16
    for row in manifest["files"]:
        assert sha(frozen[row["path"]]) == row["sha256"], row["path"]
    data = json.loads(frozen[str((CRITERIA / "results.json").relative_to(REPO))])
    review = json.loads(frozen[str((CRITERIA / "review-check.json").relative_to(REPO))])
    assert review["checked_decisions"] == data["decision_count"] == len(data["decisions"]) == 8100
    assert review["producer_results_sha256"] == sha((CRITERIA / "results.json").read_bytes())
    assert review["review_checker_sha256"] == sha((CRITERIA / "review_check.py").read_bytes())
    assert data["checker_sha256"] == sha((CRITERIA / "check.py").read_bytes())
    assert data["protocol_sha256"] == sha((CRITERIA / "PROTOCOL.md").read_bytes())
    assert len(data["source_bindings"]) == 11
    for path, digest in data["source_bindings"].items():
        assert sha(frozen[path]) == digest, path
    # The formal comparison keeps A/B/C behavioral targets. Splitting the two
    # blocked parameterizations is outside this three-target representation.
    partitions = {tuple(p) for p in data["partitions"] if p[2] == p[3]}
    assert partitions == {(0, 0, 0, 0), (0, 0, 1, 1), (0, 1, 0, 0),
                          (0, 1, 1, 1), (0, 1, 2, 2)}
    expected = set(product(partitions, range(3), range(2), range(2)))
    rows, seen = [], set()
    for row in data["decisions"]:
        p = tuple(row["partition"])
        if row["labels"] != data["labels"] or row["packets"] != 1 or p not in partitions:
            continue
        key = (p, row["phase"], row["parity"], row["broken_reset"])
        assert key not in seen
        seen.add(key)
        criterion = p[1] == p[2] or p[0] == p[2]
        recorded = row["native_depth"] is not None
        assert criterion == recorded, row
        rows.append({"partition": p, "phase": row["phase"], "parity": row["parity"],
                     "broken_reset": row["broken_reset"], "attainable": recorded})
    assert seen == expected and len(rows) == 60
    return manifest_bytes, frozen, {
        "passed": True, "source_bindings": len(frozen), "ancestor_bindings": 11,
        "saved_decisions_compared": 60, "complete_unique_coverage": True,
        "comparison": "f(B)=f(C) or f(A)=f(C), on every saved full-belief one-packet row for the five A/B/C partitions",
        "original_decisions_preserved": 8100, "producer_or_native_model_executed": False,
        "scope": "Represented-interface correspondence only; no full native trace refinement or installed-controller affordability claim.",
        "rows": rows,
    }


def main():
    baseline_bytes = BASELINE.read_bytes()
    assert sha(baseline_bytes) == BASELINE_SHA256
    baseline = json.loads(baseline_bytes)
    assert baseline["status"] == "passed" and len(baseline["modules"]) == 20 and baseline["audits"] == 227
    assert baseline["whole_current_audited_closure_empty"]
    original = {m["module"]: m for m in baseline["modules"]}
    paths = {name: REPO / row["source"] for name, row in original.items()}
    paths.update(NEW)
    frozen = {name: path.read_bytes() for name, path in paths.items()}
    for name, row in original.items():
        assert sha(frozen[name]) == row["source_sha256"], name
    evidence_bytes, evidence_frozen, evidence = evidence_check()
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
        assert set(imports[name]) <= {"Std", *paths}, (name, imports[name])
        requests[name] = re.findall(r"^#print axioms (\S+)\s*$", source, re.M)
        assert len(requests[name]) == len(set(requests[name])), name
        if name in {"AttainableQuestions", "OnePacketQuestions"}:
            declared = set(re.findall(r"^(?:private\s+)?(?:theorem|def|abbrev)\s+(\w+)\b", source, re.M))
            audited = {n.rsplit(".", 1)[-1] for n in requests[name]}
            assert declared == audited, (name, "Audit every theorem and definition", declared - audited, audited - declared)
            assert declared
    assert imports["AttainableQuestions"] == ["InquirySufficiency"]
    assert imports["OnePacketQuestions"] == ["AttainableQuestions"]
    assert imports["GenerativeAttainableQuestionsModel"] == ["GenerativeFiniteInquiryModel", "AttainableQuestions", "OnePacketQuestions"]
    entry = re.sub(r"/\-.*?\-/", "", frozen["GenerativeAttainableQuestionsModel"].decode(), flags=re.S)
    assert all(re.fullmatch(r"import\s+\w+", line.strip()) for line in entry.splitlines() if line.strip())
    order, done = [], {"Std"}
    while len(order) < len(paths):
        ready = [n for n in paths if n not in done and set(imports[n]) <= done]
        assert ready, "Incomplete or cyclic source closure"
        order.extend(ready)
        done.update(ready)
    attempt = HERE / "question-runs" / str(time.time_ns())
    (attempt / "sources").mkdir(parents=True)
    (attempt / "baseline-verification.json").write_bytes(baseline_bytes)
    (attempt / "check_questions.py").write_bytes(checker_bytes)
    (attempt / "lean-toolchain").write_bytes(toolchain_bytes)
    (attempt / "attainable-inputs.json").write_bytes(evidence_bytes)
    (attempt / "saved-evidence-comparison.json").write_text(json.dumps(evidence, indent=2) + "\n")
    for name, data in frozen.items():
        (attempt / "sources" / (name + ".lean")).write_bytes(data)
    for name, data in evidence_frozen.items():
        dest = attempt / "evidence" / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
    rows = []
    with tempfile.TemporaryDirectory(prefix="attainable-questions-fresh-") as temporary:
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
                 (CORE / "lean-toolchain").read_bytes() == toolchain_bytes and EVIDENCE.read_bytes() == evidence_bytes and
                 all((REPO / name).read_bytes() == data for name, data in evidence_frozen.items()))
    old_names = {n for row in original.values() for n in row["axioms_by_declaration"]}
    names = {n for row in rows for n in row["axioms_by_declaration"]}
    passed = len(rows) == 23 and unchanged and old_names <= names and all(row["passed"] for row in rows)
    record = {"status": "passed" if passed else "failed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "compiler": str(compiler), "compiler_sha256": baseline["compiler_sha256"], "lean_version": version,
              "toolchain_sha256": sha(toolchain_bytes), "checker_sha256": sha(checker_bytes),
              "baseline": str(BASELINE.relative_to(REPO)), "baseline_sha256": sha(baseline_bytes),
              "baseline_snapshot": str((attempt / "baseline-verification.json").relative_to(HERE)),
              "fresh_temporary_build": True, "local_precompiled_imports_used": False,
              "inputs_unchanged": unchanged, "inherited_modules": 20,
              "all_previous227_audit_names_retained": old_names <= names,
              "whole_current_audited_closure_empty": passed and all(not d for row in rows for d in row["axioms_by_declaration"].values()),
              "axiom_policy": "Every inherited and new audited declaration must be empty. Every new theorem and definition is audited.",
              "audits": sum(len(row["axioms_by_declaration"]) for row in rows),
              "new_audits": sum(len(row["axioms_by_declaration"]) for row in rows if row["new_module"]),
              "modules": rows, "evidence_manifest_sha256": sha(evidence_bytes),
              "saved_evidence": {k: v for k, v in evidence.items() if k != "rows"},
              "saved_evidence_record": str((attempt / "saved-evidence-comparison.json").relative_to(HERE)),
              "scope": "Constructive attainable-question laws over native effectful inquiry, and the permissive one-packet comparison interface. No full Python refinement, funded controller, acquired criterion, universal ethical conclusion or assumption-free foundation is established."}
    (attempt / "receipt.json").write_text(json.dumps(record, indent=2) + "\n")
    if passed:
        (HERE / "questions-verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "modules": len(rows), "audits": record["audits"],
                      "new_audits": record["new_audits"], "receipt": str((attempt / "receipt.json").relative_to(HERE))}), flush=True)
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
