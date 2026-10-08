#!/usr/bin/env python3
"""Owned documentary/receipt checks; neither ethical warrant nor new Lean run."""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
THEORY = ROOT / "theories/shengsheng-buxi-generative-existence/unified-2026-10-05/ALIGNMENT-DIRECTION.md"
PROOF = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity"
SOURCE = ROOT / "sources/15-codex-theory-conversations/2026-10-08-alignment-direction-completion.md"
DOCS = [THEORY, SOURCE, HERE / "ALIGNMENT-DIRECTION-INTEGRATION.md"]
if (HERE / "ALIGNMENT-DIRECTION-REVIEW.md").exists():
    DOCS.append(HERE / "ALIGNMENT-DIRECTION-REVIEW.md")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location("chain", HERE / "build_generative_chain.py")
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    links = 0
    for doc in DOCS:
        for ref in re.findall(r"\[[^\]]*\]\(([^)]+)\)", doc.read_text()):
            if re.match(r"[a-zA-Z]+://", ref):
                continue
            name, _, anchor = ref.partition("#")
            target = (doc.parent / unquote(name)).resolve() if name else doc
            assert target.exists(), (doc, ref)
            if anchor and target.suffix == ".md":
                assert unquote(anchor) in chain.heading_ids(target), (doc, ref)
            links += 1
    receipt_path = PROOF / "alignment-direction-verification.json"
    r = json.loads(receipt_path.read_text())
    assert r["status"] == "passed"
    frozen = PROOF / r["retained_run"]
    assert receipt_path.read_bytes() == (frozen / "verification.json").read_bytes()
    for name, h in r["source_sha256"].items():
        assert digest(PROOF / (name + ".lean")) == h
        assert digest(frozen / (name + ".lean")) == h
    for name, h in r["checker_sha256"].items():
        assert digest(PROOF / name) == h
        assert digest(frozen / name) == h
    for name, h in r["artifact_sha256"].items():
        assert digest(frozen / name) == h
    counts = {m["module"]: [m["theorems"], len(m["declarations"])] for m in r["modules"]}
    assert counts == {"PracticalJudgment": [30, 46], "AlignmentDirection": [9, 16]}
    independent = HERE / "development/alignment-direction-review"
    reviewed = json.loads((independent / "verification.json").read_text())
    assert reviewed["status"] == "passed_independent_source_binding_and_isolated_recompilation"
    assert reviewed["author_receipt_sha256"] == digest(receipt_path)
    assert reviewed["source_sha256"] == r["source_sha256"]
    assert reviewed["document_sha256"][str(THEORY.relative_to(ROOT))] == digest(THEORY)
    accepted = HERE / "development/alignment-direction-accepted/ALIGNMENT-DIRECTION-INTEGRATION.md"
    integration_name = str((HERE / "ALIGNMENT-DIRECTION-INTEGRATION.md").relative_to(ROOT))
    assert reviewed["document_sha256"][integration_name] == digest(accepted)
    assert reviewed["review_script_sha256"] == digest(independent / "verify.py")
    for name, h in reviewed["review_log_sha256"].items():
        assert digest(independent / name) == h
    data = chain.read_data()
    entry = next(e for s in data["sections"] for e in s["entries"] if e["id"] == "M20")
    generated = next(line for line in chain.render(data).splitlines() if line.startswith("| M20 |"))
    actual = next(line for line in chain.OUTPUT.read_text().splitlines() if line.startswith("| M20 |"))
    assert actual == generated
    owned_sources = []
    for item in entry["links"]:
        path, anchor = chain.local_target(item["path"])
        assert path.exists()
        if anchor and path.suffix == ".md":
            assert anchor in chain.heading_ids(path)
        name = str(path.relative_to(ROOT))
        assert data["reviewed_sources"][name] == digest(path), name
        owned_sources.append(name)
    result = {
        "status": "passed_owned_document_and_proof_bindings",
        "utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Links, frozen actual Lean run, current proof bytes and owned bilingual M20 row. No empirical, ethical-premise or entire-table certification.",
        "local_links": links,
        "proof_counts": counts,
        "proof_receipt_sha256": digest(receipt_path),
        "retained_artifacts_checked": len(r["artifact_sha256"]),
        "document_sha256": {str(p.relative_to(ROOT)): digest(p) for p in DOCS},
        "owned_chain_sources": owned_sources,
        "shared_table_changes": chain.changes(data),
        "independent_review_file_present": (HERE / "ALIGNMENT-DIRECTION-REVIEW.md").exists(),
        "independent_recompilation_and_accepted_documents_bound": True,
        "independent_receipt_sha256": digest(independent / "verification.json"),
    }
    (HERE / "ALIGNMENT-DIRECTION-CHECKS.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "links": links, "proof_counts": counts,
                      "shared_table_pending": result["shared_table_changes"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
