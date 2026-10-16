#!/usr/bin/env python3
"""Scoped documentary preservation, links and receipt bindings; not new proof checking."""
from pathlib import Path
import copy
import hashlib
import json
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from tools.research import generative_chain as chain


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    output = HERE / "CLASSIFICATION-ROBUSTNESS-CHECKS.json"
    output.write_text(json.dumps({"status": "checking"}) + "\n")
    edit = json.loads((HERE / "CLASSIFICATION-ROBUSTNESS-INDEX-EDITS.json").read_text())
    passages = []
    for name, previous in edit["appends"].items():
        raw = (ROOT / name).read_bytes()
        assert digest(raw[:previous["bytes"]]) == previous["sha256"], name
        passages.append((ROOT / name, raw[previous["bytes"]:].decode()))
    inserted = edit["insertion"]
    raw = (ROOT / inserted["path"]).read_bytes()
    content = inserted["text"].encode()
    at = inserted["offset"]
    assert raw[at:at + len(content)] == content
    inverse = raw[:at] + raw[at + len(content):]
    assert len(inverse) == inserted["baseline"]["bytes"]
    assert digest(inverse) == inserted["baseline"]["sha256"]
    passages.append((ROOT / inserted["path"], inserted["text"]))

    linked = set()
    for source, passage in passages:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", passage):
            if "://" in target:
                continue
            name, _, fragment = target.partition("#")
            path = (source.parent / unquote(name)).resolve() if name else source
            assert path.is_relative_to(ROOT) and path.exists(), (source, target)
            if fragment and path.suffix == ".md":
                assert unquote(fragment) in chain.heading_ids(path), (source, target)
            linked.add((str(source.relative_to(ROOT)), target))

    c = edit["chain"]
    data = json.loads((ROOT / c["data"]).read_text())
    entry = next(e for s in data["sections"] for e in s["entries"] if e["id"] == c["id"])
    row = next(x for x in chain.render(data).splitlines() if x.startswith("| M20 |"))
    assert digest(row.encode()) == c["after_row_sha256"]
    table = (ROOT / c["table"]).read_text()
    assert table.count(row) == 1
    assert digest(table.replace(row, "__OWNED_M20__", 1).encode()) == c["table_except_owned_row_sha256"]
    reverse = copy.deepcopy(data)
    entry = next(e for s in reverse["sections"] for e in s["entries"] if e["id"] == c["id"])
    for key, suffix in c["suffixes"].items():
        assert entry[key].endswith(suffix), key
        entry[key] = entry[key][:-len(suffix)]
    assert entry["links"][-len(c["links"]):] == c["links"]
    del entry["links"][-len(c["links"]):]
    for name, previous in c["previous_reviewed_sources"].items():
        assert data["reviewed_sources"][name] == chain.digest(ROOT / name), name
        if previous is None:
            del reverse["reviewed_sources"][name]
        else:
            reverse["reviewed_sources"][name] = previous
    assert digest(json.dumps(reverse, sort_keys=True, ensure_ascii=False).encode()) == c["before_semantic_sha256"]

    proof_dir = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity"
    receipt = json.loads((proof_dir / "classification-robust-judgment-verification.json").read_text())
    assert receipt["status"] == "passed" and receipt["source_unchanged_during_check"]
    for name, expected in receipt["source_sha256"].items():
        path = (proof_dir.parent if name == "JointContinuationClassification" else proof_dir) / (name + ".lean")
        assert chain.digest(path) == expected, name
    for name, expected in receipt["checker_sha256"].items():
        assert chain.digest(proof_dir / name) == expected, name
    run = proof_dir / receipt["retained_run"]
    for name, expected in receipt["artifact_sha256"].items():
        assert chain.digest(run / name) == expected, name
    new = next(m for m in receipt["modules"] if m["module"] == "ClassificationRobustJudgment")
    assert new["theorems"] == 13 and len(new["declarations"]) == 25
    result = {"status": "passed", "scope": "Owned source preservation, local added links, bilingual M20 additions and existing proof-receipt consistency only; no whole-table freshness, new Lean run or independent scientific acceptance.",
              "preserved_appends": len(edit["appends"]), "shared_source_inverse_preserved": True,
              "local_added_links": len(linked), "unrelated_chain_data_and_rows_preserved": True,
              "bound_proof_sources": len(receipt["source_sha256"]),
              "proof_retained_run": receipt["retained_run"],
              "checker_sha256": chain.digest(Path(__file__)),
              "edit_record_sha256": chain.digest(HERE / "CLASSIFICATION-ROBUSTNESS-INDEX-EDITS.json")}
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
