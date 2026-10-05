"""Delivery integrity for the 慧根 continuation; not a scientific revalidation."""

from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CAN = ROOT / "theories/shengsheng-buxi-generative-existence/unified-2026-10-05"
LEAN = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root"
SYM = LEAN.parent.parent / "necessity-symmetry"
RECIPIENT = ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction"
SOURCE = ROOT / "sources/15-codex-theory-conversations/2026-10-06-huigen-entire-theory-necessity.md"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def anchors(path):
    counts = {}
    result = set()
    for match in re.finditer(r"^#{1,6}\s+(.+)$", path.read_text(), re.M):
        heading = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", match.group(1))
        slug = re.sub(r"[^\w\-\s]", "", heading.lower()).replace(" ", "-")
        number = counts.get(slug, 0)
        counts[slug] = number + 1
        result.add(slug if number == 0 else f"{slug}-{number}")
    return result


def main():
    docs = [CAN / "HUIGEN.md", SOURCE, LEAN / "README.md", SYM / "README.md"]
    docs += [HERE / name for name in (
        "HUIGEN-GENERATIVE-CLOSURE.md", "HUIGEN-FULL-THEORY-AUDIT.md",
        "HUIGEN-NECESSITY-ARGUMENTS.md", "HUIGEN-REVIEW.md",
        "HUIGEN-REASON-TRANSPORT.md", "HUIGEN-PRACTICAL-NECESSITY-AUDIT.md",
        "HUIGEN-PRACTICAL-NECESSITY-SOURCES.md", "HUIGEN-SELF-GROUND-AUDIT.md",
        "HUIGEN-GENERATIVE-IDENTITY.md", "HUIGEN-SELF-GROUND-SOURCES.md",
        "HUIGEN-HARM-IDENTIFICATION.md")]
    indexed = [
        (ROOT / "RESEARCH.md", "**慧根 and necessity of the entire theory,"),
        (CAN.parent / "README.md", "**慧根 and the entire necessary foundation,"),
        (CAN / "GENERATIVE-GROUNDING.md", "**Necessary inquiry → entire generative closure"),
        (HERE / "README.md", "**慧根 and whole-theory necessity,"),
        (ROOT / "sources/SOURCES.md", "Recorded 2026-10-06: [慧根 and necessity"),
        (ROOT / "RESEARCH.md", "**Patient significance → shared practical reasons,"),
        (CAN.parent / "README.md", "**From a patient's significance to another actor's reason,"),
        (CAN / "GENERATIVE-GROUNDING.md", "**Patient-ground → cross-deliberator reason"),
        (HERE / "README.md", "**Patient-ground and deliberator scope,"),
        (ROOT / "sources/SOURCES.md", "Research extension recorded 2026-10-06: the [practical-necessity")]
    texts = [(path, path.read_text()) for path in docs]
    for path, prefix in indexed:
        selected = [p for p in path.read_text().split("\n\n") if p.startswith(prefix)]
        assert len(selected) == 1, (path, "missing or duplicate integration paragraph")
        texts.append((path, selected[0]))
    links = []
    for source, content in texts:
        for target in re.findall(r"\[[^\]\n]+\]\(([^\n)]+)\)", content):
            if re.match(r"[a-zA-Z]+:", target):
                continue
            target = unquote(target.strip("<>"))
            filename, _, fragment = target.partition("#")
            path = (source.parent / filename).resolve() if filename else source
            # This report is the output of the check, so its self-link is checked
            # by construction rather than requiring a prior report to exist.
            assert path.exists() or path == HERE / "HUIGEN-CHECKS.json", (source, target)
            if fragment:
                assert fragment in anchors(path), (source, target, "missing anchor")
            links.append({"source": str(source.relative_to(ROOT)), "target": target})

    coverage = json.loads((HERE / "HUIGEN-CLAIM-COVERAGE.json").read_text())
    assert digest(ROOT / coverage["source"]) == coverage["source_sha256"]
    assert coverage["row_count"] == len(coverage["claims"]) == 55
    assert sum(coverage["classes"].values()) == 55
    assert all(row["newly_reverified_proof"] is False for row in coverage["claims"])

    proof = json.loads((LEAN / "verification.json").read_text())
    assert proof["status"] == "passed" and proof["fresh_temporary_build"]
    assert proof["source_unchanged_during_check"]
    assert digest(LEAN / "check.py") == proof["checker_sha256"]
    assert digest(LEAN / "lean-toolchain") == proof["toolchain_sha256"]
    for module in proof["modules"]:
        assert module["exit_code"] == 0 and module["clean_dependency_audit"]
        assert digest(LEAN / module["source"]) == module["source_sha256"]
        assert digest(LEAN / module["output"]) == module["output_sha256"]
        assert set(module["axioms"]) <= {"propext", "Classical.choice", "Quot.sound"}
    new_count = sum(len(m["audited_declarations"]) for m in proof["modules"] if not m["inherited"])
    inherited_count = sum(len(m["audited_declarations"]) for m in proof["modules"] if m["inherited"])
    assert new_count == proof["new_audited_declarations"] == 27
    assert inherited_count == proof["inherited_audited_declarations"] == 23

    symmetry = json.loads((SYM / "verification.json").read_text())
    assert symmetry["status"] == "pass" and digest(SYM / "check.py") == symmetry["source_sha256"]
    assert symmetry["total_matrices_enumerated"] == 66066
    assert [r["jointly_invariant_count"] for r in symmetry["results"]] == [2, 4, 4, 4]
    assert [r["positive_self_count"] for r in symmetry["results"]] == [1, 2, 2, 2]
    assert [r["positive_self_and_actor_independent_count"] for r in symmetry["results"]] == [1, 1, 1, 1]

    # Read the inherited fixture and its receipts; do not rerun the model.
    recipient = json.loads((RECIPIENT / "results.json").read_text())
    recipient_review = json.loads((RECIPIENT / "independent-check.json").read_text())
    assert recipient_review["status"] == "passed"
    for receipt, count in ((recipient, 8), (recipient_review, 11)):
        assert len(receipt["source_sha256"]) == count
        for name, expected in receipt["source_sha256"].items():
            assert digest(ROOT / name) == expected, (name, "changed inherited recipient source")
    arms = recipient["cases"]["primary"]["producers"]["variable"]
    for arm in ("indexed", "private_only"):
        metrics = arms[arm]["metrics"]
        assert metrics["final_actor"] == "25/18"
        assert metrics["actor_captures"] == "2/9"
        assert metrics["spent"] == "25/6"
    assert arms["indexed"]["metrics"]["final_recipient"] == "10/9"
    assert arms["private_only"]["metrics"]["final_recipient"] == "0"

    artifacts = docs + [Path(__file__), HERE / "HUIGEN-CLAIM-COVERAGE.json"]
    artifacts += [LEAN / name for name in ("GenerativeClosure.lean", "InquiryFamilies.lean", "check.py", "lean-toolchain", "verification.json")]
    artifacts += sorted((LEAN / "verification").glob("*.txt"))
    artifacts += [SYM / name for name in ("check.py", "verification.json")]
    report = {
        "date": "2026-10-06", "status": "pass",
        "scope": "Local document links and anchors, owned artifact hashes, claim inventory, existing proof/enumeration receipt consistency and stated inherited recipient metrics/source receipts. No rerun of science, empirical validation or completed philosophical foundation.",
        "local_links_checked": len(links),
        "anchors_checked": sum("#" in link["target"] for link in links),
        "claim_rows_inventoried": 55, "new_lean_audits": new_count,
        "inherited_lean_audits": inherited_count, "finite_matrices_enumerated": 66066,
        "practical_necessity_follow_up": {
            "previous_goal_turn": "progress",
            "new_companions": 3,
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "evidence": "Displayed hand proofs, primary-source argument inspection and internal cross-review; no claim that propagation justifies the supplied normative inputs.",
            "inspected_reason_interface": "experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/reason-replay/formal/ReasonReplay.lean",
            "inspected_reason_interface_sha256": digest(ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/reason-replay/formal/ReasonReplay.lean"),
        },
        "self_ground_follow_up": {
            "previous_goal_turn": "progress",
            "new_companions": 4,
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "primary_philosophical_works_examined": 2,
            "primary_empirical_reports_examined": 3,
            "empirical_reports_abstract_only": 1,
            "evidence": "Displayed conditional branching and fixed-constituency succession arguments; exact scoped-inheritance condition; selective primary readings and internal cross-review. Does not establish practical congruency, universal standing or whole-root necessity.",
        },
        "practical_congruency_follow_up": {
            "previous_goal_turn": "progress",
            "existing_companions_extended_or_corrected": 5,
            "new_companion_files": 0,
            "new_primary_philosophical_works_examined": 1,
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "inherited_model_reruns": 0,
            "evidence": "Matched-case normative adjudication, typed assignment/oracle analysis, Williams primary comparison, corrected countermodel capacity scope, and inherited operational evidence. Positive warrant remains distinct from universal necessity.",
            "recipient_receipt_source_hash_counts": [8, 11],
            "recipient_receipt_sha256": {
                name: digest(RECIPIENT / name)
                for name in ("results.json", "independent-check.json")
            },
            "recipient_metric_scope": "Saved primary variable-producer expected values; no inference from equal means alone to equal nonlinear or risk-sensitive evaluations.",
        },
        "perspective_uptake_follow_up": {
            "previous_goal_turn": "progress",
            "existing_companions_extended": 4,
            "new_companion_files": 0,
            "new_primary_philosophical_works_examined": 1,
            "new_primary_empirical_reports_examined": 3,
            "empirical_reports_abstract_or_preview_only": 2,
            "empirical_reports_selected_full_text": 1,
            "new_lean_audits": 0,
            "new_empirical_studies": 0,
            "inherited_model_reruns": 0,
            "proposed_discrimination_tests_executed": False,
            "evidence": "Exact typed-frame hand argument, conditional retention of warranted actual-actor reasons, calibrated acquisition route, scoped Sidgwick and empirical readings, and internal cross-review. Recognition and practical grounding remain distinct; full necessity is not established.",
        },
        "artifacts": {str(p.relative_to(ROOT)): digest(p) for p in artifacts},
        "shared_index_paragraphs": [str(p.relative_to(ROOT)) for p, _ in indexed],
        "links": links,
    }
    (HERE / "HUIGEN-CHECKS.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ("status", "local_links_checked", "anchors_checked", "claim_rows_inventoried", "new_lean_audits", "finite_matrices_enumerated")}, indent=2))


if __name__ == "__main__":
    main()
