#!/usr/bin/env python3
"""Verify evidence provenance, owned integration and unchanged prior proof bindings.

This documentary check neither evaluates experimental truth nor runs Lean.
"""
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
RESULT = HERE / "SITUATED-EXPERIMENTAL-EVIDENCE-CHECKS.json"
LEAN = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(data):
    return json.dumps(data, ensure_ascii=False, sort_keys=True).encode()


def main():
    RESULT.write_text('{"status":"checking"}\n')
    spec = importlib.util.spec_from_file_location("chain", HERE / "build_generative_chain.py")
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    edits = json.loads((HERE / "SITUATED-EXPERIMENTAL-EVIDENCE-INDEX-EDITS.json").read_text())
    data = chain.read_data()
    entry = next(e for s in data["sections"] for e in s["entries"] if e["id"] == "M20")
    for key, suffix in edits["owned_suffixes"].items():
        assert entry[key].count(suffix) == 1, key
        assert edits["entry_before"][key] + suffix == edits["entry_after"][key]
    for link in edits["entry_before"]["links"] + edits["added_links"]:
        assert link in entry["links"], link
    expected = next(x for x in chain.render(data).splitlines() if x.startswith("| M20 |"))
    actual = next(x for x in chain.OUTPUT.read_text().splitlines() if x.startswith("| M20 |"))
    assert actual == expected
    passages = []
    for name, fingerprint in edits["owned_reviewed_sources"].items():
        p = ROOT / name
        assert digest(p.read_bytes()) == fingerprint == data["reviewed_sources"][name], name
        if name in edits["prior_content"]:
            info = edits["prior_content"][name]
            assert digest(p.read_bytes()[:info["prior_length"]]) == info["prior_sha256"]
            assert p.read_bytes()[info["prior_length"]:].decode() == info["addition"]
            assert info["prior_bytes_preserved"]
            passages.append((p, info["addition"]))
        elif p.suffix == ".md":
            passages.append((p, p.read_text()))
    for name, info in edits["shared_fragments"].items():
        p = ROOT / name
        assert p.read_text().count(info["fragment"]) == 1, name
        assert info["other_bytes_preserved"]
        passages.append((p, info["fragment"]))
    for name in edits["added_discovery_paths"]:
        assert name in data["known_discovery_paths"] and (ROOT / name).exists()
    links = []
    for p, passage in passages:
        for reference in re.findall(r"\]\(([^\s)]+)\)", passage):
            if re.match(r"[a-zA-Z]+:", reference):
                continue
            name, _, fragment = reference.partition("#")
            target = (p.parent / unquote(name)).resolve() if name else p
            assert target.is_relative_to(ROOT) and target.exists(), (p, reference)
            if fragment:
                assert unquote(fragment) in chain.heading_ids(target), (p, reference)
            links.append({"from": str(p.relative_to(ROOT)), "reference": reference})
    for link in edits["added_links"]:
        p, fragment = chain.local_target(link["path"])
        assert p.exists() and (not fragment or fragment in chain.heading_ids(p)), link

    evidence = json.loads((HERE / "SITUATED-RECOVERY-EXPERIMENTAL-EVIDENCE.json").read_text())
    narrative = (HERE / "SITUATED-RECOVERY-EXPERIMENTAL-EVIDENCE.md").read_text()
    studies = evidence["primary_studies"]
    assert [s["id"] for s in studies] == ["E1", "E2", "E3", "E4", "E5", "E6"]
    assert len({s["doi"] for s in studies}) == 6
    for s in studies:
        assert s["primary_url"] in narrative and s["primary_url"].startswith("https://")
        assert s["inspected"] and s["supports"] and s["limitations"]
        assert s["physical_observations_in_source"]
        if "temporary_reading_copy" in s:
            c = s["temporary_reading_copy"]
            assert not c["repository_imported"] and c["bytes"] > 0
            assert re.fullmatch("[a-f0-9]{64}", c["sha256"])
    for name in evidence["reuse_without_new_replication"] + [evidence["stronger_joint_target"]]:
        assert (HERE / name).exists()
    for key in ("new_theorems", "new_laboratory_experiments", "new_raw_data_reanalyses"):
        assert evidence[key] == 0
    for key in ("evidence_establishes_exact_bilinear_model", "evidence_establishes_universal_goal_convergence",
                "complete_biological_joint_validation", "independent_review", "source_bytes_imported"):
        assert evidence[key] is False

    receipt = json.loads((LEAN / "diagnostic-tracking-verification.json").read_text())
    assert receipt["status"] == "passed" and receipt["source_unchanged_during_check"]
    retained = LEAN / receipt["retained_run"]
    assert set(receipt["source_sha256"]) == {"SituatedTracking", "ActionAwareTracking", "DiagnosticTracking"}
    for name, fingerprint in receipt["source_sha256"].items():
        assert digest((LEAN / (name + ".lean")).read_bytes()) == fingerprint
        assert digest((retained / (name + ".lean")).read_bytes()) == fingerprint
    for name, fingerprint in receipt["artifact_sha256"].items():
        assert digest((retained / name).read_bytes()) == fingerprint, name
    assert (retained / "verification.json").read_bytes() == (LEAN / "diagnostic-tracking-verification.json").read_bytes()
    others = [e for s in data["sections"] for e in s["entries"] if e["id"] != "M20"]
    other_lines = "".join(x for x in chain.OUTPUT.read_text().splitlines(keepends=True)
                          if not x.startswith("| M20 |"))
    result = {
        "status": "passed", "scope": edits["scope"], "primary_studies_assessed": len(studies),
        "new_theorems": 0, "new_laboratory_experiments": 0, "new_raw_data_reanalyses": 0,
        "prior_documents_preserved": len(edits["prior_content"]),
        "owned_M20_additions_and_renderer_match": True,
        "other_entries_preserved_at_mutation": edits["other_entries_preserved_at_mutation"],
        "unrelated_entries_match_edit_baseline": digest(canonical(others)) == edits["unrelated_entries_sha256"],
        "other_table_lines_match_edit_baseline": digest(other_lines.encode()) == edits["other_table_lines_sha256"],
        "local_links_checked": len(links), "links": links,
        "source_sha256": edits["owned_reviewed_sources"],
        "checker_sha256": digest(Path(__file__).read_bytes()),
        "prior_proof_scope_unchanged": True, "proof_recompiled": False,
        "prior_proof_source_sha256": receipt["source_sha256"],
        "retained_proof_artifacts_bound": len(receipt["artifact_sha256"]),
        "pending_global_review": chain.changes(data),
        "scientific_truth_certified_by_this_script": False,
        "new_independent_review": False, "exact_observer_empirically_certified": False,
        "complete_biological_joint_validation": False, "whole_table_certified": False,
    }
    RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("status", "primary_studies_assessed", "new_theorems",
                                           "prior_documents_preserved", "local_links_checked",
                                           "retained_proof_artifacts_bound")}))


if __name__ == "__main__":
    main()
