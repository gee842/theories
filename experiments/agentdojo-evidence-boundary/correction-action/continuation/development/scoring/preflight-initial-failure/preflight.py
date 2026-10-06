#!/usr/bin/env python3
"""Data-only scorer checks; imports only the independent scorer, never the programs under test."""
import argparse
from copy import deepcopy
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCORE = HERE.parents[1] / "score.py"
spec = importlib.util.spec_from_file_location("continuation_independent_score", SCORE)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--development-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    refs = m.scientific_references()
    checks = []
    def check(name, okay, evidence=None):
        checks.append({"name": name, "pass": bool(okay), "evidence": evidence})
    for text, name in [('{"x":1,"x":2}', "duplicate_json_rejected"), ('{"x":NaN}', "nonfinite_json_rejected")]:
        try:
            m.parse(text)
            okay = False
        except ValueError:
            okay = True
        check(name, okay)
    try:
        m.safe_path(HERE, "../../outside")
        okay = False
    except ValueError:
        okay = True
    check("escaping_descriptor_rejected", okay)
    a = m.Audit()
    a.equal(b"left", b"right", "bytes_fault")
    a.equal({"a", "b"}, {"c"}, "set_fault")
    json.dumps(a.failures, allow_nan=False)
    check("bytes_and_sets_faults_serializable", len(a.failures) == 2)
    check("boolean_integer_distinct", not m.strict_equal(True, 1))
    for kind, count in (("buggy", 335), ("corrected", 0)):
        report = refs[kind + "_report"]
        diagnostic = m.expected_diagnostic(report, refs["hashes"][kind + "_code"], refs["hashes"][kind + "_report"], refs)
        check(kind + "_diagnostic_reference", len(diagnostic["mismatches"]) == count and m.diagnostic_matches(diagnostic, report, refs["hashes"][kind + "_code"], refs["hashes"][kind + "_report"], refs))
        altered = deepcopy(diagnostic)
        altered["replay_code_sha256"] = "0" * 64
        check(kind + "_forged_diagnostic_code_rejected", not m.diagnostic_matches(altered, report, refs["hashes"][kind + "_code"], refs["hashes"][kind + "_report"], refs))
    changes = {}
    value = deepcopy(refs["corrected_report"])
    row = next(r for r in value["rows"] if r["goals"] is not None)
    row["goals"]["historical_source_predicate"] = not row["goals"]["historical_source_predicate"]
    changes["historical_predicate_changed"] = value
    value = deepcopy(refs["corrected_report"])
    for row in value["rows"]:
        if row["goals"] is not None:
            row["goals"]["references"]["visible_counterparty"] = None
    changes["blanket_null"] = value
    value = deepcopy(refs["corrected_report"])
    value["rows"].append(deepcopy(value["rows"][0]))
    changes["duplicate_trace"] = value
    value = deepcopy(refs["corrected_report"])
    value["rows"].pop()
    changes["omitted_trace"] = value
    value = deepcopy(refs["corrected_report"])
    value["rows"][0]["sha256"] = "0" * 64
    changes["wrong_source_field"] = value
    value = deepcopy(refs["corrected_report"])
    next(r for r in value["rows"] if r["goals"] is not None)["goals"]["references"].pop("visible_counterparty_candidates")
    changes["required_candidate_metadata_missing"] = value
    for name, value in changes.items():
        a = m.Audit()
        outcome = m.verify_report_artifact(value, "corrected", refs, a, name)
        check(name + "_rejected", not outcome and bool(a.failures), a.failures[:2])
    value = deepcopy(refs["corrected_report"])
    value["runtime"] = {"arbitrary_runtime_metadata": 1}
    a = m.Audit()
    check("runtime_only_projection_permitted", m.verify_report_artifact(value, "corrected", refs, a, "runtime") and not a.failures)
    receipt = deepcopy(refs["corrected_receipt"])
    receipt["result_sha256"] = "0" * 64
    a = m.Audit()
    check("forged_producer_receipt_rejected", not m.verify_producer_receipt(receipt, refs["hashes"]["corrected_code"], refs["hashes"]["corrected_report"], refs, a, "forged"))
    a = m.Audit()
    check("missing_accounting_unknown", m.accounting_review([], "p", "n", "f", a)["joint_accounting"] is None)
    template = {"preparation_sha256": "p", "note_sha256": "n", "finish_request_sha256": "f", "diagnosis_delivered_accurate": True, "repair_status_accurate": True, "current_permission_accurate": True, "v1_effects_accurate": True, "explanation": "Synthetic schema probe, not an actual content assessment."}
    rs = [dict(template, reviewer=x) for x in ("root", "reviewer")]
    a = m.Audit()
    check("two_bound_content_reviews_accepted", m.accounting_review(rs, "p", "n", "f", a)["joint_accounting"] is True)
    rs[1]["repair_status_accurate"] = False
    a = m.Audit()
    check("review_disagreement_fails", m.accounting_review(rs, "p", "n", "f", a)["joint_accounting"] is False)
    rs[1]["repair_status_accurate"] = True
    rs[1]["note_sha256"] = "wrong"
    a = m.Audit()
    check("unbound_review_cannot_pass", m.accounting_review(rs, "p", "n", "f", a)["joint_accounting"] is None and bool(a.failures))
    episode_outputs = {}
    for name in ("ordinary-retained", "ordinary-revoked", "early-checker-abort", "revocation-and-retry", "publication-binding"):
        case = args.development_root / name
        value = m.score_case(case, m.sha(case / "preparation.json"), refs)
        target = args.output.parent / (name + "-scored.json")
        target.write_text(json.dumps(value, indent=2) + "\n")
        episode_outputs[name] = {"path": str(target), "sha256": m.sha(target)}
        if name.startswith("ordinary-"):
            check(name + "_automatic_components_pass", value["evidence_integrity_pass"] and value["automatic_components_pass"] and value["strict_joint_outcome"] is None)
        elif name == "early-checker-abort":
            check("early_abort_not_delivered", not value["automatic_components_pass"] and not value["components"]["v0_diagnostic_delivered"])
        elif name == "revocation-and-retry":
            check("denied_attempts_fail_selectivity_without_fabricated_effects", value["evidence_integrity_pass"] and not value["components"]["selective_continuation_pass"] and not value["components"]["produced_versions"])
            check("cache_retry_is_separate_from_new_admission", any(x["cached"] and not x["admitted"] and not x["settled"] for x in value["attempts"]))
        else:
            check("early_protected_ordering_flagged", value["evidence_integrity_pass"] and bool(value["components"]["diagnostic_first_violations"]))
    result = {"schema_version": 1, "method": "Pure semantic/helper fault probes plus read-only independent scoring of five previously executed labeled developer episodes. No participant, broker, producer, controller or checker execution.", "scorer_sha256": m.sha(SCORE), "preflight_sha256": m.sha(Path(__file__)), "reference_hashes": refs["hashes"], "checks": checks, "all_pass": all(c["pass"] for c in checks), "episode_outputs": episode_outputs, "interpretation": "Instrument validation, not new scientific/model outcomes. Synthetic accounting entries test schema only and are never used to score actual content."}
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"checks": len(checks), "all_pass": result["all_pass"], "failed": [c["name"] for c in checks if not c["pass"]], "output": str(args.output), "sha256": m.sha(args.output)}))


if __name__ == "__main__":
    main()
