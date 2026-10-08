#!/usr/bin/env python3
"""Check this study's links, source-bound Lean evidence and owned index entry.

Documentary validation only: does not rerun Lean or certify philosophical warrant.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "RESEARCH.md").is_file())
REPORT = HERE / "ENACTED-FOUNDATION-CHECKS.json"
DOCS = [ROOT / "theories/becoming/chapters/ASSUMPTION-FREE-FOUNDATION.md",
        HERE / "ENACTED-FOUNDATION-INTEGRATION.md",
        HERE / "GROUNDING-INFERENCE-AND-PRESENTATION.md",
        ROOT / "sources/15-codex-theory-conversations/2026-10-08-assumption-free-shengsheng-foundation.md"]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location("chain", HERE / "build_generative_chain.py")
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    errors, links = [], []
    for source in DOCS:
        for ref in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", source.read_text()):
            if re.match(r"[a-z]+://", ref):
                continue
            pathpart, _, fragment = ref.partition("#")
            target = (source.parent / unquote(pathpart)).resolve() if pathpart else source
            if target != REPORT and not target.is_file():
                errors.append("Missing target: " + str(target))
            elif fragment and target.suffix == ".md" and unquote(fragment) not in chain.heading_ids(target):
                errors.append("Missing anchor: " + ref)
            links.append({"source": str(source.relative_to(ROOT)), "reference": ref})
    pointer_path = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/deeper/enacted-foundation-verification.json"
    pointer = json.loads(pointer_path.read_text())
    receipt_path = ROOT / pointer["receipt"]
    receipt = json.loads(receipt_path.read_text())
    assert pointer["passed"] and receipt["passed"]
    assert receipt["total_empty_axiom_audits"] == 29
    assert len(receipt["modules"]) == 2
    checker = pointer_path.parent / "check_enacted_foundation.py"
    assert digest(checker) == receipt["checker_sha256"]
    for module in receipt["modules"]:
        assert digest(ROOT / module["source"]) == module["sha256"]
        assert digest(ROOT / module["snapshot"]) == module["sha256"]
        assert digest(ROOT / module["log"]) == module["log_sha256"]
        assert module["passed"] and module["exit_code"] == 0
        assert module["source_unchanged_during_check"]
        assert len(module["empty_axiom_audits"]) == module["expected_audits"]
    inference_pointer = json.loads((pointer_path.parent / "inferential-grounds-verification.json").read_text())
    inference_receipt_path = ROOT / inference_pointer["receipt"]
    inference_receipt = json.loads(inference_receipt_path.read_text())
    assert inference_pointer["passed"] and inference_receipt["passed"]
    assert inference_receipt["exit_code"] == 0
    assert inference_receipt["source_unchanged_during_check"]
    assert inference_receipt["new_theorems"] == 8
    assert len(inference_receipt["empty_axiom_audits"]) == 10
    assert digest(ROOT / inference_receipt["source"]) == inference_receipt["source_sha256"]
    assert digest(ROOT / inference_receipt["snapshot"]) == inference_receipt["source_sha256"]
    assert digest(ROOT / inference_receipt["log"]) == inference_receipt["log_sha256"]
    assert digest(ROOT / inference_receipt["checker"]) == inference_receipt["checker_sha256"]
    mutual_pointer = json.loads((pointer_path.parent / "mutual-grounding-verification.json").read_text())
    mutual_receipt_path = ROOT / mutual_pointer["receipt"]
    mutual_receipt = json.loads(mutual_receipt_path.read_text())
    assert mutual_pointer["passed"] and mutual_receipt["passed"]
    assert mutual_receipt["exit_code"] == 0 and mutual_receipt["source_unchanged_during_check"]
    assert mutual_receipt["new_theorems"] == 10 and len(mutual_receipt["empty_axiom_audits"]) == 10
    assert digest(ROOT / mutual_receipt["source"]) == mutual_receipt["source_sha256"]
    assert digest(ROOT / mutual_receipt["snapshot"]) == mutual_receipt["source_sha256"]
    assert digest(ROOT / mutual_receipt["log"]) == mutual_receipt["log_sha256"]
    assert digest(ROOT / mutual_receipt["checker"]) == mutual_receipt["checker_sha256"]
    dependence_pointer = json.loads((pointer_path.parent / "dependence-warrant-verification.json").read_text())
    dependence_receipt_path = ROOT / dependence_pointer["receipt"]
    dependence_receipt = json.loads(dependence_receipt_path.read_text())
    assert dependence_pointer["passed"] and dependence_receipt["passed"]
    assert dependence_receipt["exit_code"] == 0 and dependence_receipt["source_unchanged_during_check"]
    assert dependence_receipt["new_theorems"] == 3 and len(dependence_receipt["empty_axiom_audits"]) == 3
    assert digest(ROOT / dependence_receipt["source"]) == dependence_receipt["source_sha256"]
    assert digest(ROOT / dependence_receipt["snapshot"]) == dependence_receipt["source_sha256"]
    assert digest(ROOT / dependence_receipt["log"]) == dependence_receipt["log_sha256"]
    assert digest(ROOT / dependence_receipt["checker"]) == dependence_receipt["checker_sha256"]
    transport_pointer_path = pointer_path.parent / "ground-relation-transport-verification.json"
    transport_pointer = json.loads(transport_pointer_path.read_text())
    transport_receipt_path = ROOT / transport_pointer["receipt"]
    transport_receipt = json.loads(transport_receipt_path.read_text())
    assert transport_pointer["passed"] and transport_receipt["passed"]
    assert transport_receipt["total_empty_axiom_audits"] == 14
    assert len(transport_receipt["modules"]) == 2
    assert digest(pointer_path.parent / "check_ground_relation_transport.py") == transport_receipt["checker_sha256"]
    for module in transport_receipt["modules"]:
        assert digest(ROOT / module["source"]) == module["sha256"]
        assert digest(ROOT / module["snapshot"]) == module["sha256"]
        assert digest(ROOT / module["log"]) == module["log_sha256"]
        assert module["passed"] and module["exit_code"] == 0 and module["source_unchanged_during_check"]
        assert len(module["empty_axiom_audits"]) == module["expected_audits"]
    assert transport_receipt["modules"][1]["expected_audits"] == 4
    continuation_pointer_path = pointer_path.parent / "continuation-conditions-verification.json"
    continuation_pointer = json.loads(continuation_pointer_path.read_text())
    continuation_receipt_path = ROOT / continuation_pointer["receipt"]
    continuation_receipt = json.loads(continuation_receipt_path.read_text())
    assert continuation_pointer["passed"] and continuation_receipt["passed"]
    assert continuation_receipt["total_empty_axiom_audits"] == 43
    assert len(continuation_receipt["modules"]) == 3
    assert digest(pointer_path.parent / "check_continuation_conditions.py") == continuation_receipt["checker_sha256"]
    for module in continuation_receipt["modules"]:
        assert digest(ROOT / module["source"]) == module["sha256"]
        assert digest(ROOT / module["snapshot"]) == module["sha256"]
        assert digest(ROOT / module["log"]) == module["log_sha256"]
        assert module["passed"] and module["exit_code"] == 0 and module["source_unchanged_during_check"]
        assert len(module["empty_axiom_audits"]) == module["expected_audits"]
    assert continuation_receipt["modules"][2]["expected_audits"] == 18
    formation_pointer_path = pointer_path.parent / "formation-profile-gap-verification.json"
    formation_pointer = json.loads(formation_pointer_path.read_text())
    formation_receipt_path = ROOT / formation_pointer["receipt"]
    formation_receipt = json.loads(formation_receipt_path.read_text())
    assert formation_pointer["passed"] and formation_receipt["passed"]
    assert formation_receipt["total_empty_axiom_audits"] == 87
    assert len(formation_receipt["modules"]) == 6
    assert digest(pointer_path.parent / "check_formation_profile_gap.py") == formation_receipt["checker_sha256"]
    for module in formation_receipt["modules"]:
        assert digest(ROOT / module["source"]) == module["sha256"]
        assert digest(ROOT / module["snapshot"]) == module["sha256"]
        assert digest(ROOT / module["log"]) == module["log_sha256"]
        assert module["passed"] and module["exit_code"] == 0 and module["source_unchanged_during_check"]
        assert len(module["empty_axiom_audits"]) == module["expected_audits"]
    assert formation_receipt["modules"][-1]["expected_audits"] == 13
    return_pointer = json.loads((pointer_path.parent / "return-conditions-verification.json").read_text())
    return_receipt_path = ROOT / return_pointer["receipt"]
    return_receipt = json.loads(return_receipt_path.read_text())
    assert return_pointer["passed"] and return_receipt["passed"]
    assert return_receipt["total_empty_axiom_audits"] == 115
    assert len(return_receipt["modules"]) == 7
    assert digest(pointer_path.parent / "check_return_conditions.py") == return_receipt["checker_sha256"]
    for module in return_receipt["modules"]:
        assert digest(ROOT / module["source"]) == module["sha256"]
        assert digest(ROOT / module["snapshot"]) == module["sha256"]
        assert digest(ROOT / module["log"]) == module["log_sha256"]
        assert module["passed"] and module["exit_code"] == 0 and module["source_unchanged_during_check"]
        assert len(module["empty_axiom_audits"]) == module["expected_audits"]
    assert return_receipt["modules"][-1]["expected_audits"] == 28
    reused_pointer = json.loads((pointer_path.parent / "unfolding-preservation-verification.json").read_text())
    reused_receipt_path = ROOT / reused_pointer["receipt"]
    reused_receipt = json.loads(reused_receipt_path.read_text())
    assert reused_receipt["status"] == "passed"
    assert digest(pointer_path.parent / "UnfoldingPreservation.lean") == reused_receipt["source_sha256"]["UnfoldingPreservation"]
    data = chain.read_data()
    entry = next(e for s in data["sections"] for e in s["entries"] if e["id"] == "C01")
    for link in entry["links"]:
        path, fragment = chain.local_target(link["path"])
        assert digest(path) == data["reviewed_sources"][str(path.relative_to(ROOT))]
        if fragment:
            assert fragment in chain.heading_ids(path)
    expected = next(x for x in chain.render(data).splitlines() if x.startswith("| C01 |"))
    actual = next(x for x in chain.OUTPUT.read_text().splitlines() if x.startswith("| C01 |"))
    assert actual == expected
    result = {"passed": not errors, "scope": "Owned documents, existing proof evidence and C01 only",
              "errors": errors, "local_link_count": len(links), "links": links,
              "documents": {str(p.relative_to(ROOT)): digest(p) for p in DOCS},
              "proof_receipt": str(receipt_path.relative_to(ROOT)),
              "proof_receipt_sha256": digest(receipt_path), "new_theorems": 11,
              "full_closure_audits": 29, "proof_recompiled_by_this_check": False,
              "inference_receipt": str(inference_receipt_path.relative_to(ROOT)),
              "inference_receipt_sha256": digest(inference_receipt_path),
              "inference_new_theorems": 8, "inference_declaration_audits": 10,
              "mutual_grounding_receipt": str(mutual_receipt_path.relative_to(ROOT)),
              "mutual_grounding_receipt_sha256": digest(mutual_receipt_path),
              "mutual_grounding_new_theorems": 10,
              "dependence_receipt": str(dependence_receipt_path.relative_to(ROOT)),
              "dependence_receipt_sha256": digest(dependence_receipt_path),
              "dependence_new_theorems": 3,
              "transport_receipt": str(transport_receipt_path.relative_to(ROOT)),
              "transport_receipt_sha256": digest(transport_receipt_path),
              "transport_new_theorems": 4, "transport_total_declaration_audits": 14,
              "continuation_receipt": str(continuation_receipt_path.relative_to(ROOT)),
              "continuation_receipt_sha256": digest(continuation_receipt_path),
              "continuation_new_theorems": 18, "continuation_total_declaration_audits": 43,
              "formation_profile_receipt": str(formation_receipt_path.relative_to(ROOT)),
              "formation_profile_receipt_sha256": digest(formation_receipt_path),
              "formation_profile_new_theorems": 9, "formation_profile_inherited_selected_audits": 78,
              "formation_profile_total_audits": 87,
              "return_conditions_receipt": str(return_receipt_path.relative_to(ROOT)),
              "return_conditions_receipt_sha256": digest(return_receipt_path),
              "return_conditions_new_theorems": 23,
              "return_conditions_new_declaration_audits": 28,
              "return_conditions_inherited_selected_audits": 87,
              "return_conditions_total_audits": 115,
              "reused_unfolding_receipt": str(reused_receipt_path.relative_to(ROOT)),
              "reused_unfolding_source_matches": True,
              "owned_chain_entry_passed": True,
              "combined_table_pending_changes": chain.changes(data)}
    REPORT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ["passed", "errors", "local_link_count",
                       "new_theorems", "full_closure_audits", "inference_new_theorems",
                       "inference_declaration_audits", "mutual_grounding_new_theorems", "dependence_new_theorems",
                       "transport_new_theorems", "transport_total_declaration_audits",
                       "continuation_new_theorems", "continuation_total_declaration_audits",
                       "formation_profile_new_theorems", "formation_profile_total_audits",
                       "return_conditions_new_theorems", "return_conditions_total_audits",
                       "owned_chain_entry_passed"]}))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
