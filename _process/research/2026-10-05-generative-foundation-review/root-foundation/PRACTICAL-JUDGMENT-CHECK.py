#!/usr/bin/env python3
"""Check this study's document links and retained proof binding; no Lean rerun."""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

sys.dont_write_bytecode = True
import build_generative_chain as chain

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
THEORY = ROOT / "theories/shengsheng-buxi-generative-existence/unified-2026-10-05/PRACTICAL-JUDGMENT.md"
FORMAL = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    docs = [THEORY, HERE / "PRACTICAL-JUDGMENT-INTEGRATION.md", HERE / "PRACTICAL-JUDGMENT-REVIEW.md"]
    links = []
    for doc in docs:
        for ref in re.findall(r"\[[^\]]*\]\(([^)]+)\)", doc.read_text()):
            if "://" in ref:
                continue
            name, _, fragment = unquote(ref).partition("#")
            target = (doc.parent / name).resolve() if name else doc
            assert target.is_relative_to(ROOT), (doc, ref)
            assert target.exists(), (doc, ref)
            if fragment and target.suffix == ".md":
                assert fragment in chain.heading_ids(target), (doc, ref)
            links.append({"document": str(doc.relative_to(ROOT)), "target": ref})
    receipt_path = FORMAL / "practical-judgment-verification.json"
    receipt = json.loads(receipt_path.read_text())
    assert receipt["status"] == "passed"
    run = FORMAL / receipt["retained_run"]
    assert receipt_path.read_bytes() == (run / "verification.json").read_bytes()
    for name, h in receipt["artifact_sha256"].items():
        assert digest(run / name) == h, name
    assert digest(FORMAL / "PracticalJudgment.lean") == receipt["source_sha256"]["PracticalJudgment"]
    for name, h in receipt["checker_sha256"].items():
        assert digest(FORMAL / name) == h, name
    module, = receipt["modules"]
    assert module["theorems"] == 30 and len(module["declarations"]) == 46
    for axioms in module["axiom_dependencies"].values():
        assert set(axioms) <= {"propext", "Quot.sound", "Classical.choice"}
    data = chain.read_data()
    assert not chain.validate(data), chain.validate(data)
    assert (chain.OUTPUT).read_text() == chain.render(data)
    tracked = docs + [FORMAL / "PracticalJudgment.lean", FORMAL / "check_practical_judgment.py",
                      receipt_path, Path(__file__)]
    report = {
        "status": "passed", "date": "2026-10-08 Asia/Bangkok",
        "scope": "Document links and exact successful Lean receipt binding, not a new proof or empirical run.",
        "local_links_checked": len(links), "retained_artifacts_checked": len(receipt["artifact_sha256"]),
        "theorems": module["theorems"], "explicit_declarations": len(module["declarations"]),
        "sha256": {str(p.relative_to(ROOT)): digest(p) for p in tracked},
        "bilingual_entries": sum(len(s["entries"]) for s in data["sections"]),
        "links": links,
    }
    (HERE / "PRACTICAL-JUDGMENT-CHECKS.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k not in {"sha256", "links"}}, ensure_ascii=False))


if __name__ == "__main__":
    main()
