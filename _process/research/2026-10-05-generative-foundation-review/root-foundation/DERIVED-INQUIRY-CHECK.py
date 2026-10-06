#!/usr/bin/env python3
"""Reconcile immutable proof evidence and owned integration fragments."""
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
RUN = S / "derived-inquiry-runs/1791286286937536000"
OUTPUT = HERE / "DERIVED-INQUIRY-CHECKS.json"
RECEIPT_SHA = "01fad790e1436e72ab967cf8163240452b360ea2ed8972000ce1caedf93b51ee"
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")
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
    check_hash(S / "derived-inquiry-verification.json", RECEIPT_SHA)
    check_hash(RUN / "receipt.json", RECEIPT_SHA)
    receipt = json.loads((RUN / "receipt.json").read_text())
    assert receipt["status"] == "passed" and receipt["inputs_unchanged"]
    assert len(receipt["modules"]) == 28 and receipt["audits"] == 409 and receipt["new_audits"] == 102
    assert receipt["all_previous307_audit_names_retained"] and receipt["whole_current_audited_closure_empty"]
    assert not receipt["scientific_producer_executed"]
    check_hash(S / "check_derived_inquiry.py", receipt["checker_sha256"])
    check_hash(RUN / "check_derived_inquiry.py", receipt["checker_sha256"])
    check_hash(CORE / "lean-toolchain", receipt["toolchain_sha256"])
    check_hash(RUN / "lean-toolchain", receipt["toolchain_sha256"])
    assert hashlib.sha256(Path(receipt["compiler"]).read_bytes()).hexdigest() == receipt["compiler_sha256"]
    baseline_path = REPO / receipt["baseline"]
    check_hash(baseline_path, receipt["baseline_sha256"])
    check_hash(S / receipt["baseline_snapshot"], receipt["baseline_sha256"])
    baseline = json.loads(baseline_path.read_text())
    old = {m["module"]: m for m in baseline["modules"]}
    total = 0
    for module in receipt["modules"]:
        assert module["passed"] and module["audit_complete"] and module["exact_dependency_contract"]
        assert all(not d for d in module["axioms_by_declaration"].values())
        check_hash(REPO / module["source"], module["source_sha256"])
        check_hash(S / module["source_snapshot"], module["source_sha256"])
        check_hash(S / module["log"], module["log_sha256"])
        source = (S / module["source_snapshot"]).read_text()
        requests = re.findall(r"^#print axioms (\S+)\s*$", source, re.M)
        audited = [(name, [d.strip() for d in ds.split(",") if d.strip()])
                   for name, ds in AUDIT.findall((S / module["log"]).read_text())]
        assert len(audited) == len(requests) == len(module["axioms_by_declaration"])
        assert dict(audited) == module["axioms_by_declaration"]
        assert all(actual == requested or actual.endswith("." + requested)
                   for (actual, _), requested in zip(audited, requests))
        total += len(audited)
        if module["module"] in old:
            prior = old[module["module"]]
            assert module["source_sha256"] == prior["source_sha256"]
            assert module["axioms_by_declaration"] == prior["axioms_by_declaration"]
        else:
            declared = set(re.findall(r"^(?:private\s+)?(?:theorem|def|abbrev|inductive|structure)\s+(\w+)\b", source, re.M))
            assert declared == {name.rsplit(".", 1)[-1] for name in requests}
    assert total == 409
    counts = {kind: sum(row[kind] for row in receipt["new_declarations"].values())
              for kind in ("theorem", "def", "abbrev", "inductive", "structure")}
    assert counts == {"theorem": 55, "def": 42, "abbrev": 4, "inductive": 1, "structure": 0}
    check_hash(RUN / "attainable-inputs.json", receipt["evidence_manifest_sha256"])
    check_hash(baseline_path.parent / "attainable-inputs.json", receipt["evidence_manifest_sha256"])
    evidence = json.loads((RUN / "attainable-inputs.json").read_text())["files"]
    assert len(evidence) == 16
    for row in evidence:
        check_hash(REPO / row["path"], row["sha256"])
        check_hash(baseline_path.parent / "evidence" / row["path"], row["sha256"])
    edits = json.loads((HERE / "DERIVED-INQUIRY-EDITS.json").read_text())["edits"]
    fragments = []
    for edit in edits:
        path = REPO / edit["path"]
        assert edit["fragment"] in path.read_text(), (path, "Owned fragment missing")
        fragments.append((path, edit["fragment"]))
    for name in ("DERIVED-INQUIRY-PREMISES.md", "DERIVED-INQUIRY-REVIEW.md"):
        path = HERE / name
        fragments.append((path, path.read_text()))
    links = []
    for path, content in fragments:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            if re.match(r"[a-zA-Z]+:", target):
                continue
            file, _, anchor = unquote(target).partition("#")
            actual = (path.parent / file).resolve() if file else path
            # The sole forward reference is this checker's own output.
            assert actual.exists() or (actual == OUTPUT and not anchor), (path, target)
            if anchor and actual.suffix == ".md":
                assert anchor in headings(actual.read_text()), (path, target)
            links.append({"from": str(path.relative_to(REPO)), "target": target})
    document_hashes = {str(path.relative_to(REPO)): hashlib.sha256(path.read_bytes()).hexdigest()
                       for path, _ in fragments}
    result = {"status": "passed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Saved proof/evidence and owned document reconciliation only; no Lean or scientific rerun.",
        "modules": 28, "audits": 409, "new_audits": 102, "new_declarations": counts,
        "all_audited_dependencies_empty": True, "all_previous307_audits_retained": True,
        "owned_fragments": len(edits), "owned_files": len({e["path"] for e in edits}),
        "links_checked": len(links), "hash_comparisons": len(hashes),
        "compiler_hash_verified": True, "assumption_free_foundation_established": False,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "document_hashes_at_check": document_hashes, "hashes": hashes, "links": links}
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items()
                      if k not in {"document_hashes_at_check", "hashes", "links"}}))


if __name__ == "__main__":
    main()
