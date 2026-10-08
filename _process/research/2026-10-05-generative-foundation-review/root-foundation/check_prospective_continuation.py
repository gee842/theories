#!/usr/bin/env python3
"""Check the owned conceptual correction and old proof bindings, without rerunning proofs."""
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
RESULT = HERE / "PROSPECTIVE-CONTINUATION-CHECKS.json"
LEAN = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity"


def digest(b):
    return hashlib.sha256(b).hexdigest()


def canonical(d):
    return json.dumps(d, ensure_ascii=False, sort_keys=True).encode()


def main():
    RESULT.write_text('{"status":"checking"}\n')
    spec = importlib.util.spec_from_file_location("chain", HERE / "build_generative_chain.py")
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    edits = json.loads((HERE / "PROSPECTIVE-CONTINUATION-INDEX-EDITS.json").read_text())
    data = chain.read_data()
    entry = next(e for s in data["sections"] for e in s["entries"] if e["id"] == "M20")
    for key, change in edits["owned_replacements"].items():
        assert entry[key].count(change["after"]) == 1, key
        assert change["before"] not in entry[key], key
        assert edits["entry_before"][key].replace(change["before"], change["after"], 1) == edits["entry_after"][key]
    for link in edits["entry_after"]["links"]:
        assert link in entry["links"], link
    expected = next(x for x in chain.render(data).splitlines() if x.startswith("| M20 |"))
    actual = next(x for x in chain.OUTPUT.read_text().splitlines() if x.startswith("| M20 |"))
    assert actual == expected

    passages = []
    for name, expected_hash in edits["owned_reviewed_sources"].items():
        p = ROOT / name
        assert digest(p.read_bytes()) == expected_hash, name
        assert data["reviewed_sources"][name] == expected_hash, name
        passages.append((p, p.read_text()))
        preservation = edits["prior_content"][name]
        before = p.read_text().split(preservation["new_heading"], 1)[0]
        notice = preservation["inserted_notice"]
        if notice:
            assert before.count(notice) == 1
            before = before.replace(notice, "", 1)
        assert digest(before.encode()) == preservation["prior_sha256"], name
    for name, info in edits["shared_fragments"].items():
        p = ROOT / name
        assert p.read_text().count(info["fragment"]) == 1, name
        assert info["other_bytes_preserved"]
        passages.append((p, info["fragment"]))

    links = []
    for p, text in passages:
        for reference in re.findall(r"\]\(([^\s)]+)\)", text):
            if re.match(r"[a-zA-Z]+:", reference):
                continue
            name, _, fragment = reference.partition("#")
            target = (p.parent / unquote(name)).resolve() if name else p
            assert target.is_relative_to(ROOT) and target.exists(), (p, reference)
            if fragment:
                assert unquote(fragment) in chain.heading_ids(target), (p, reference)
            links.append({"from": str(p.relative_to(ROOT)), "reference": reference})
    for link in entry["links"]:
        p, fragment = chain.local_target(link["path"])
        assert p.exists() and (not fragment or fragment in chain.heading_ids(p)), link

    receipt = json.loads((LEAN / "formative-assessment-verification.json").read_text())
    assert receipt["status"] == "passed" and receipt["source_unchanged_during_check"]
    retained = LEAN / receipt["retained_run"]
    for name, expected_hash in receipt["source_sha256"].items():
        assert digest((LEAN / (name + ".lean")).read_bytes()) == expected_hash
        assert digest((retained / (name + ".lean")).read_bytes()) == expected_hash
    for name, expected_hash in receipt["artifact_sha256"].items():
        assert digest((retained / name).read_bytes()) == expected_hash
    model = next(m for m in receipt["modules"] if m["module"] == "FormativeAssessment")
    assert model["theorems"] == 18 and len(model["declarations"]) == 34
    for theorem in ["formation_then_unprompted_probe_succeeds", "one_credit_forms_but_cannot_fund_assessment"]:
        assert any(d["name"] == "FormativeAssessment." + theorem for d in model["declarations"])

    others = [e for s in data["sections"] for e in s["entries"] if e["id"] != "M20"]
    other_lines = "".join(x for x in chain.OUTPUT.read_text().splitlines(keepends=True) if not x.startswith("| M20 |"))
    result = {
        "status": "passed", "scope": edits["scope"], "new_theorems": 0,
        "scientific_checks_rerun": False, "existing_formative_theorems": 18,
        "existing_formative_audits": 34, "retained_proof_artifacts_bound": len(receipt["artifact_sha256"]),
        "prior_documents_preserved": len(edits["prior_content"]),
        "owned_M20_correction_and_renderer_match": True,
        "unrelated_entries_match_edit_baseline": digest(canonical(others)) == edits["unrelated_entries_sha256"],
        "other_table_lines_match_edit_baseline": digest(other_lines.encode()) == edits["other_table_lines_sha256"],
        "local_links_checked": len(links), "links": links,
        "source_sha256": edits["owned_reviewed_sources"],
        "checker_sha256": digest(Path(__file__).read_bytes()),
        "pending_global_review": chain.changes(data), "new_independent_review": False,
    }
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ["status", "new_theorems", "prior_documents_preserved", "local_links_checked", "retained_proof_artifacts_bound"]}))


if __name__ == "__main__":
    main()
