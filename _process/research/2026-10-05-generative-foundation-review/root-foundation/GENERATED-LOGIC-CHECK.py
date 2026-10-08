#!/usr/bin/env python3
"""Check this study's evidence bindings and owned documentary integration.

This does not rerun Lean or stamp unrelated source reviews. The Lean checker
is separate; its frozen source, output and dependency receipt are checked here.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEAN = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/deeper"
THEORY = ROOT / "theories/becoming/chapters/GENERATED-LOGIC.md"
SOURCE = ROOT / "sources/15-codex-theory-conversations/2026-10-08-generative-logic-investigation.md"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    proof = LEAN / "generated-contraction-checks/20261008T101759.536385Z/receipt.json"
    receipt = json.loads(proof.read_text())
    assert receipt["passed"]
    assert sha((LEAN / "check_generated_contraction.py").read_bytes()) == receipt["checker_sha256"]
    totals = {"all": 0, "empty": 0, "new": 0, "new_empty": 0}
    for item in receipt["modules"]:
        p = ROOT / item["source"]
        frozen = proof.parent / "sources" / p.name
        assert item["passed"] and item["source_unchanged_during_check"]
        assert sha(p.read_bytes()) == sha(frozen.read_bytes()) == item["sha256"]
        audits = item["axiom_audits"]
        names = re.findall(r"^#print axioms (\S+)$", p.read_text(), re.M)
        assert set(names) == set(audits) and len(names) == len(audits)
        log = (proof.parent / (p.stem + ".log")).read_text()
        parsed = {n: [] for n in re.findall(r"'([^']+)' does not depend on any axioms", log)}
        parsed.update({n: [x.strip() for x in xs.split(",")]
                       for n, xs in re.findall(r"'([^']+)' depends on axioms: \[(.*?)\]", log, re.S)})
        assert parsed == audits
        assert all(set(xs) <= {"propext", "Quot.sound"} for xs in audits.values())
        count = len(audits)
        empty = sum(not xs for xs in audits.values())
        totals["all"] += count
        totals["empty"] += empty
        if p.name in {"GeneratedContraction.lean", "ContractionMechanisms.lean"}:
            assert len(re.findall(r"^theorem ", p.read_text(), re.M)) == count
            totals["new"] += count
            totals["new_empty"] += empty
    assert totals == {"all": 65, "empty": 51, "new": 38, "new_empty": 24}

    spec = importlib.util.spec_from_file_location("chain", HERE / "build_generative_chain.py")
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    data = chain.read_data()
    edits = json.loads((HERE / "GENERATED-LOGIC-INDEX-EDITS.json").read_text())
    entry = next(e for s in data["sections"] for e in s["entries"] if e["id"] == "F01")
    assert entry == edits["entry_after"]
    expected = next(x for x in chain.render(data).splitlines() if x.startswith("| F01 |"))
    current = next(x for x in chain.OUTPUT.read_text().splitlines() if x.startswith("| F01 |"))
    assert current == expected
    assert edits["other_entries_preserved"] and edits["other_rendered_lines_preserved"]
    for name, digest in edits["authored_fingerprints"].items():
        assert data["reviewed_sources"][name] == sha((ROOT / name).read_bytes()) == digest
    for fragment in edits["shared_fragments"]:
        assert (ROOT / fragment["path"]).read_text().count(fragment["text"]) == 1
    assert all(p in data["known_discovery_paths"] for p in edits["owned_discovery_paths"])

    links = []
    documents = [THEORY, HERE / "GENERATED-LOGIC-INTEGRATION.md", SOURCE]
    for doc in documents:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", doc.read_text()):
            if target.startswith(("https://", "http://")):
                continue
            name, _, anchor = unquote(target).partition("#")
            p = (doc.parent / name).resolve() if name else doc
            assert p.is_relative_to(ROOT) and p.exists(), (doc, target)
            if anchor and p.suffix == ".md":
                assert anchor in chain.heading_ids(p), (doc, target)
            links.append({"document": str(doc.relative_to(ROOT)), "target": target})

    global_errors = chain.validate(data)
    pending = chain.changes(data)
    combined = {}
    # The renderer refuses unrelated pending source reviews. Preserve that
    # outcome rather than falsely refreshing sources that were not reviewed.
    if pending["modified_sources"] or pending["missing_sources"]:
        original = chain.OUTPUT.read_bytes()
        for mode in ("--render", "--check"):
            result = subprocess.run([sys.executable, str(HERE / "build_generative_chain.py"), mode],
                                    cwd=ROOT, text=True, capture_output=True)
            assert result.returncode == 2
            combined[mode] = json.loads(result.stdout)
        assert chain.OUTPUT.read_bytes() == original
    report = {
        "passed_owned_scope": True,
        "scope": "Frozen proof bindings, new documents, owned insertions and canonical F01 row only",
        "proof_receipt": str(proof.relative_to(ROOT)),
        "proof_receipt_sha256": sha(proof.read_bytes()),
        "audit_totals": totals,
        "documents": {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in documents},
        "local_links": links,
        "paired_entry": "F01",
        "owned_edits_preserved": True,
        "global_link_validation_errors": global_errors,
        "pending_shared_reviews": pending,
        "combined_renderer_checks": combined,
        "whole_table_certified": False,
        "independent_agent_review": False,
    }
    (HERE / "GENERATED-LOGIC-CHECKS.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"passed_owned_scope": True, "new_theorems": totals["new"],
                      "total_audits": totals["all"], "local_links": len(links),
                      "pending_shared_sources": len(pending["modified_sources"]),
                      "whole_table_certified": False}))


if __name__ == "__main__":
    main()
