#!/usr/bin/env python3
"""Check saved attainable-question proof evidence and owned document links."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
CORE = REPO / "experiments/integrated-correction/general-framework/generative-basis/lean"
S = CORE / "inquiry-root/sufficiency"
RUN = S / "question-runs/1791281585451526000"
OUTPUT = HERE / "ATTAINABLE-QUESTIONS-LEAN-CHECKS.json"
hashes = []


def check_hash(path, expected):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    assert digest == expected, path
    hashes.append({"path": str(path.relative_to(REPO)), "sha256": digest})


def headings(text):
    out, seen = set(), {}
    for title in re.findall(r"^#{1,6}\s+(.+)$", text, re.M):
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        index = seen.get(slug, 0)
        seen[slug] = index + 1
        out.add(slug + (f"-{index}" if index else ""))
    return out


def main():
    receipt_hash = "57a5d6532e98ad281c8e8f982127a21563307ff07813e3ffe39d245cbd710006"
    check_hash(S / "questions-verification.json", receipt_hash)
    check_hash(RUN / "receipt.json", receipt_hash)
    receipt = json.loads((RUN / "receipt.json").read_text())
    assert receipt["status"] == "passed" and receipt["inputs_unchanged"]
    assert receipt["audits"] == 307 and receipt["new_audits"] == 80 and len(receipt["modules"]) == 23
    assert receipt["all_previous227_audit_names_retained"] and receipt["whole_current_audited_closure_empty"]
    check_hash(S / "check_questions.py", receipt["checker_sha256"])
    check_hash(RUN / "check_questions.py", receipt["checker_sha256"])
    check_hash(CORE / "lean-toolchain", receipt["toolchain_sha256"])
    check_hash(RUN / "lean-toolchain", receipt["toolchain_sha256"])
    compiler = Path(receipt["compiler"])
    assert hashlib.sha256(compiler.read_bytes()).hexdigest() == receipt["compiler_sha256"]
    check_hash(REPO / receipt["baseline"], receipt["baseline_sha256"])
    check_hash(S / receipt["baseline_snapshot"], receipt["baseline_sha256"])
    baseline = json.loads((REPO / receipt["baseline"]).read_text())
    previous = {m["module"]: m["axioms_by_declaration"] for m in baseline["modules"]}
    for module in receipt["modules"]:
        assert module["passed"] and module["audit_complete"] and module["exact_dependency_contract"]
        assert all(not d for d in module["axioms_by_declaration"].values())
        if module["module"] in previous:
            assert module["axioms_by_declaration"] == previous[module["module"]]
        check_hash(REPO / module["source"], module["source_sha256"])
        check_hash(S / module["source_snapshot"], module["source_sha256"])
        check_hash(S / module["log"], module["log_sha256"])
    check_hash(S / "attainable-inputs.json", receipt["evidence_manifest_sha256"])
    check_hash(RUN / "attainable-inputs.json", receipt["evidence_manifest_sha256"])
    evidence = json.loads((RUN / "attainable-inputs.json").read_text())
    assert len(evidence["files"]) == 16
    for item in evidence["files"]:
        check_hash(REPO / item["path"], item["sha256"])
        check_hash(RUN / "evidence" / item["path"], item["sha256"])
    comparison = json.loads((S / receipt["saved_evidence_record"]).read_text())
    assert comparison["passed"] and comparison["complete_unique_coverage"]
    assert len(comparison["rows"]) == comparison["saved_decisions_compared"] == 60
    assert not comparison["producer_or_native_model_executed"]
    check_hash(HERE / "ATTAINABLE-QUESTIONS-LEAN-REVIEW.md",
               "fca62af0c768d3ada95ae50b02e107f6f4c569e558ce7cb45472ba2489217a34")

    edits = json.loads((HERE / "ATTAINABLE-QUESTIONS-LEAN-EDITS.json").read_text())["edits"]
    fragments = []
    for edit in edits:
        path = REPO / edit["path"]
        fragment = edit["new"]
        if re.fullmatch(r"# [^\n]+\n\n", edit["old"]) and fragment.startswith(edit["old"]):
            fragment = fragment[len(edit["old"]):]
        assert fragment in path.read_text(), (path, "Owned fragment changed")
        fragments.append((path, fragment))
    for name in ("ATTAINABLE-QUESTIONS-LEAN-INTEGRATION.md", "ATTAINABLE-QUESTIONS-LEAN-REVIEW.md"):
        path = HERE / name
        fragments.append((path, path.read_text()))
    links = []
    for path, text in fragments:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"[a-zA-Z]+:", target):
                continue
            file, _, anchor = unquote(target).partition("#")
            actual = (path.parent / file).resolve() if file else path
            # This receipt is created below only after all checks succeed.
            assert actual.exists() or (actual == OUTPUT and not anchor), (path, target)
            if anchor and actual.suffix == ".md":
                assert anchor in headings(actual.read_text()), (path, target)
            links.append({"from": str(path.relative_to(REPO)), "target": target})
    result = {"status": "passed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "scope": "Saved proof/evidence and document reconciliation only; no Lean or scientific rerun.",
              "modules": 23, "audits": 307, "new_theorems": 47, "new_definitions_and_abbreviations": 33,
              "all_audited_dependencies_empty": True, "saved_comparison_cases": 60,
              "owned_files": len({e["path"] for e in edits}), "owned_fragments": len(edits),
              "links_checked": len(links), "hash_comparisons": len(hashes),
              "compiler_hash_verified": True, "hashes": hashes, "links": links}
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k not in {"hashes", "links"}}))


if __name__ == "__main__":
    main()
