#!/usr/bin/env python3
"""Check saved evidence and integration links; do not rerun formal/scientific work."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BUILD = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/connected/applicability"
CANON = ROOT / "theories/shengsheng-buxi-generative-existence/unified-2026-10-05"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def identity(path):
    return {"path": str(path.relative_to(ROOT)), "sha256": sha(path)}


def main():
    receipt = json.loads((BUILD / "verification.json").read_text())
    manifest = json.loads((BUILD / "INPUTS.json").read_text())
    assert receipt["build_status"] == "passed"
    assert receipt["manifest_sha256"] == sha(BUILD / "INPUTS.json")
    assert receipt["checker_sha256"] == sha(BUILD / "check.py")
    assert receipt["compiler_sha256"] == sha(Path(receipt["compiler"]))
    sources = {x["module"]: x for x in manifest["sources"]}
    assert len(sources) == len(receipt["modules"]) == 51
    for item in receipt["modules"]:
        assert item["checked"] and item["exit_code"] == 0
        assert sha(ROOT / item["source"]) == item["source_sha256"]
        assert sha(BUILD / sources[item["module"]]["snapshot"]) == item["source_sha256"]
        assert sha(BUILD / item["log"]) == item["log_sha256"]
    for item in manifest["receipt_sources"]:
        assert sha(BUILD / item["saved"]) == item["sha256"]

    added = {"CompletionApplicability", "GenerativeApplicabilityModel"}
    reports = [x for x in receipt["modules"] if x["module"] in added]
    count = sum(len(x["axioms_by_declaration"]) for x in reports)
    empty = sum(not a for x in reports for a in x["axioms_by_declaration"].values())
    assert (count, empty) == (21, 5)
    assert receipt["named_axiom_dependencies"] == ["Classical.choice", "Quot.sound", "propext"]
    assert receipt["whole_closure_has_empty_axiom_dependencies"] is False
    assert receipt["assumption_free_foundation_established"] is False

    edits = json.loads((HERE / "COMPLETION-APPLICABILITY-INTEGRATION-EDITS.json").read_text())
    edit_states = []
    link_inputs = []
    for item in edits["files"]:
        before = ROOT / item["before_snapshot"]
        current = ROOT / item["path"]
        assert sha(before) == item["before_sha256"]
        added_lines = [s[1:] for s in item["patch"].splitlines()
                       if s.startswith("+") and not s.startswith("+++")]
        removed_lines = [s for s in item["patch"].splitlines()
                         if s.startswith("-") and not s.startswith("---")]
        assert not removed_lines, item["path"]
        assert all(s in current.read_text() for s in added_lines if s)
        edit_states.append({**identity(current), "before_snapshot_verified": True,
                            "own_additions_present": True,
                            "matches_immediate_post_edit": sha(current) == item["after_sha256"]})
        link_inputs.append((current, "\n".join(added_lines)))

    documents = [CANON / "CONNECTED-GENERATIVE-MODEL.md", BUILD / "README.md",
                 HERE / "COMPLETION-APPLICABILITY-MECHANISM.md",
                 HERE / "COMPLETION-APPLICABILITY-REVIEW.md",
                 HERE / "COMPLETION-APPLICABILITY-IDENTIFICATION.md"]
    link_inputs.extend((p, p.read_text()) for p in documents)
    checked_links = []
    for owner, content in link_inputs:
        for raw in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            target = urlsplit(raw.strip("<>"))
            if target.scheme or target.netloc:
                continue
            path = (owner.parent / unquote(target.path)).resolve() if target.path else owner
            assert path.exists(), (str(owner), raw)
            anchor_checked = False
            if target.fragment and path.suffix == ".md":
                headings = re.findall(r"^#{1,6}\s+(.+)$", path.read_text(), re.M)
                anchors = {re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-") for h in headings}
                assert unquote(target.fragment) in anchors, (str(owner), raw)
                anchor_checked = True
            checked_links.append({"document": str(owner.relative_to(ROOT)), "target": raw,
                                  "exists": True, "anchor_checked": anchor_checked})

    evidence = [BUILD / "check.py", BUILD / "INPUTS.json", BUILD / "verification.json",
                HERE / "COMPLETION-APPLICABILITY-INTEGRATION-EDITS.json", Path(__file__)]
    for directory in [HERE / "development/completion-applicability"]:
        evidence.extend(p for p in sorted(directory.rglob("*")) if p.is_file())
    evidence.extend(ROOT / x["source"] for x in reports)
    prototype = HERE / "development/completion-applicability/root/attempt-01-GenerativeApplicabilityModel.lean"
    current_entry = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeApplicabilityModel.lean"
    revised_comment = prototype.read_text().replace(
        "ledger while the same physical learner retains its old help assessment forever.",
        "ledger while the same physical learner retains its old help assessment through\nevery admitted finite continuation.")
    assert revised_comment == current_entry.read_text()
    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed",
        "scope": "Integrity and local-link check of the completed bounded connection; no proof or empirical rerun.",
        "combined_build_modules": 51,
        "new_audited_declarations": count,
        "new_empty_named_axiom_reports": empty,
        "all_current_sources_snapshots_logs_and_compiler_match_receipt": True,
        "ancestor_receipt_snapshots_verified": True,
        "inherited_claim_ledger_audits_not_counted_as_new": 21,
        "physical_law_changed": False,
        "runtime_completion_selector_installed": False,
        "proof_level_ledger_only": True,
        "whole_closure_named_axioms": receipt["named_axiom_dependencies"],
        "whole_closure_has_empty_axiom_dependencies": False,
        "assumption_free_foundation_established": False,
        "empirical_experiment_rerun": False,
        "review": "Independent source review accepted both new modules, actual-certificate scope and final canonical claims. The mechanism author and root entry author are distinct from the reviewer; the reviewer checked final source/manifest/log bindings.",
        "next_connection": "Form and use a justified, paid applicability-sensitive selection path from the actual learned predecessor. Preserve acquired means, separate addressed claims, current permission and actual resource/ancestry handoffs; equivalent refactoring alone cannot create the missing behavior.",
        "upstream_open": ["Origin of supplied event laws and formation recipes", "Sensing, interpretation and calibration", "Independent ethical grounding and legitimate authority"],
        "integration_edits": edit_states,
        "local_links": checked_links,
        "documents": [identity(p) for p in documents],
        "evidence": [identity(p) for p in evidence],
    }
    (HERE / "COMPLETION-APPLICABILITY-INTEGRATION.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": "passed", "modules": 51, "new_audits": count,
                      "new_empty_reports": empty, "local_links": len(checked_links),
                      "preserved_evidence_files": len(evidence),
                      "index_files_changed_since_integration": [x["path"] for x in edit_states
                                                                if not x["matches_immediate_post_edit"]]}))


if __name__ == "__main__":
    main()
