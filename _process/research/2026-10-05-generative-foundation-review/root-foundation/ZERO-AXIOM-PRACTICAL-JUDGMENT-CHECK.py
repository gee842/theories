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
THEORY = ROOT / "theories/shengsheng-buxi-generative-existence/unified-2026-10-05/ZERO-AXIOM-PRACTICAL-JUDGMENT.md"
FORMAL = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    docs = [THEORY, HERE / "ZERO-AXIOM-PRACTICAL-JUDGMENT-INTEGRATION.md"]
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
    packages = [
        ("priority-identification-verification.json",
         {"PracticalPriorityIdentification": (FORMAL / "PracticalPriorityIdentification.lean", 14, 21)}),
        ("normative-activity-verification.json",
         {"KnowledgeCorrespondence": (FORMAL.parent.parent / "inquiry-root/KnowledgeCorrespondence.lean", 20, 34),
          "NormativeActivity": (FORMAL / "NormativeActivity.lean", 34, 56)}),
        ("standards-bridge-verification.json",
         {"StandardsBridge": (FORMAL / "StandardsBridge.lean", 26, 39)}),
        ("formed-grounds-verification.json",
         {"KnowledgeCorrespondence": (FORMAL.parent.parent / "inquiry-root/KnowledgeCorrespondence.lean", 20, 34),
          "NormativeActivity": (FORMAL / "NormativeActivity.lean", 34, 56),
          "StandardsBridge": (FORMAL / "StandardsBridge.lean", 26, 39),
          "FormedGrounds": (FORMAL / "FormedGrounds.lean", 27, 45)}),
        ("practical-reach-verification.json",
         {"PracticalReach": (FORMAL / "PracticalReach.lean", 24, 35)}),
    ]
    tracked = docs + [Path(__file__), ROOT / "sources/15-codex-theory-conversations/2026-10-08-normative-force-and-informational-generation.md"]
    package_records = []
    for receipt_name, expected in packages:
        receipt_path = FORMAL / receipt_name
        receipt = json.loads(receipt_path.read_text())
        assert receipt["status"] == "passed"
        run = FORMAL / receipt["retained_run"]
        assert receipt_path.read_bytes() == (run / "verification.json").read_bytes()
        for name, h in receipt["artifact_sha256"].items():
            assert digest(run / name) == h, name
        assert set(receipt["source_sha256"]) == set(expected)
        for module_name, (source, _, _) in expected.items():
            assert digest(source) == receipt["source_sha256"][module_name]
            assert source.read_bytes() == (run / (module_name + ".lean")).read_bytes()
            tracked.append(source)
        for name, h in receipt["checker_sha256"].items():
            assert digest(FORMAL / name) == h, name
            tracked.append(FORMAL / name)
        assert {m["module"] for m in receipt["modules"]} == set(expected)
        for module in receipt["modules"]:
            _, theorems, declarations = expected[module["module"]]
            assert module["theorems"] == theorems and len(module["declarations"]) == declarations
            assert module["kernel_checked"]
            assert set(module["axiom_dependencies"]) == {d["name"] for d in module["declarations"]}
            allowed = {"propext", "Quot.sound"}
            if module["module"] in {"KnowledgeCorrespondence", "StandardsBridge", "FormedGrounds", "PracticalReach"}:
                allowed.add("Classical.choice")
            for axioms in module["axiom_dependencies"].values():
                assert set(axioms) <= allowed
        tracked.append(receipt_path)
        package_records.append({"receipt": str(receipt_path.relative_to(ROOT)),
            "retained_artifacts_checked": len(receipt["artifact_sha256"]),
            "modules": [{"name": m["module"], "theorems": m["theorems"],
                         "explicit_declarations": len(m["declarations"]),
                         "inherited_in_this_package": m["module"] != next(reversed(expected))}
                        for m in receipt["modules"]]})
    data = chain.read_data()
    # Keep this study's link/proof binding independent of concurrent index edits.
    # Report every shared-index issue explicitly instead of certifying that index.
    # Match this study's exact generated rows without claiming review of other
    # sessions' concurrently changing sources. This follows the index workflow's
    # earlier scoped-row maintenance for the knowledge study.
    generated_lines = chain.render(data).splitlines()
    actual_lines = chain.OUTPUT.read_text().splitlines()
    for identity in ("C26", "F23", "F26", "F27", "F28"):
        tag = "| " + identity + " |"
        wanted = [line for line in generated_lines if line.startswith(tag)]
        actual = [line for line in actual_lines if line.startswith(tag)]
        assert len(wanted) == 1 and actual == wanted, identity
        entry = next(e for section in data["sections"] for e in section["entries"] if e["id"] == identity)
        for link in entry["links"]:
            path, _ = chain.local_target(link["path"])
            assert digest(path) == data["reviewed_sources"][str(path.relative_to(ROOT))]
    chain_errors = chain.validate(data)
    delta = chain.changes(data)
    if delta["modified_sources"] or delta["missing_sources"]:
        chain_errors.append({"source_changes": delta})
    if chain.OUTPUT.read_text() != chain.render(data):
        chain_errors.append("Shared table differs from current paired data")
    report = {
        "status": "passed", "date": "2026-10-08 Asia/Bangkok",
        "scope": "Document links and exact successful Lean receipt binding, not a new proof or empirical run.",
        "scoped_index_rows": {"C26": "passed", "F23": "passed", "F26": "passed", "F27": "passed", "F28": "passed"},
        "shared_index_status": "needs-review" if chain_errors else "passed",
        "shared_index_issues": chain_errors,
        "local_links_checked": len(links), "formal_packages": package_records,
        "sha256": {str(p.relative_to(ROOT)): digest(p) for p in tracked},
        "bilingual_entries": sum(len(s["entries"]) for s in data["sections"]),
        "links": links,
    }
    (HERE / "ZERO-AXIOM-PRACTICAL-JUDGMENT-CHECKS.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k not in {"sha256", "links"}}, ensure_ascii=False))


if __name__ == "__main__":
    main()
