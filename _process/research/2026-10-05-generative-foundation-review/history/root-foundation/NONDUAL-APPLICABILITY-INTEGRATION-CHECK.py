#!/usr/bin/env python3
"""Verify preserved evidence and integration links without rerunning the proofs."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BUILD = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/connected/nondual"
CANON = ROOT / "theories/becoming/chapters"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def identity(path):
    return {"path": str(path.relative_to(ROOT)), "sha256": sha(path)}


def main():
    receipt = json.loads((BUILD / "verification.json").read_text())
    manifest = json.loads((BUILD / "INPUTS.json").read_text())
    assert receipt["build_status"] == "passed" and receipt["inputs_unchanged"]
    assert receipt["manifest_sha256"] == sha(BUILD / "INPUTS.json")
    assert receipt["checker_sha256"] == sha(BUILD / "check.py")
    assert receipt["compiler_sha256"] == sha(Path(receipt["compiler"]))
    assert receipt["fresh_temporary_build"] and not receipt["local_precompiled_imports_used"]
    sources = {x["module"]: x for x in manifest["sources"]}
    assert len(sources) == len(receipt["modules"]) == 55
    for item in receipt["modules"]:
        assert item["checked"] and item["exit_code"] == 0
        assert sha(ROOT / item["source"]) == item["source_sha256"]
        assert sha(BUILD / sources[item["module"]]["snapshot"]) == item["source_sha256"]
        assert sha(BUILD / item["log"]) == item["log_sha256"]
    for item in manifest["receipt_sources"]:
        assert sha(BUILD / item["saved"]) == item["sha256"]
    development = json.loads((HERE / "development/nondual-applicability/DEVELOPMENT-ATTEMPTS.json").read_text())
    for item in development["sources"] + development["files"]:
        assert sha(ROOT / item["path"]) == item["sha256"]

    added = {"GenerativeRepairApplicability", "RecipientContinuationProjection"}
    reports = [x for x in receipt["modules"] if x["module"] in added]
    count = sum(len(x["axioms_by_declaration"]) for x in reports)
    empty = sum(not a for x in reports for a in x["axioms_by_declaration"].values())
    assert (count, empty) == (27, 3)
    entry = next(x for x in receipt["modules"] if x["module"] == "GenerativeNondualApplicabilityModel")
    assert entry["import_only"] and not entry["axioms_by_declaration"]
    assert receipt["named_axiom_dependencies"] == ["Classical.choice", "Quot.sound", "propext"]
    assert not receipt["whole_closure_has_empty_axiom_dependencies"]
    assert not receipt["assumption_free_foundation_established"]

    edits = json.loads((HERE / "NONDUAL-APPLICABILITY-CANONICAL-EDITS.json").read_text())
    link_inputs = []
    edit_states = []
    for item in edits["edits"]:
        current = ROOT / item["path"]
        own = item["after_fragment"]
        # Later concurrent entries may sit between a title and our paragraph.
        if own.startswith(item["before_fragment"]):
            own = own[len(item["before_fragment"]):]
        assert own in current.read_text(), item["path"]
        edit_states.append({**identity(current), "own_fragment_present": True,
                            "matches_immediate_post_edit": sha(current) == item["after_sha256"]})
        link_inputs.append((current, item["after_fragment"]))
    documents = [HERE / ("NONDUAL-APPLICABILITY-" + name + ".md")
                 for name in ["QUESTION", "MECHANISM", "REVIEW", "COMPARATORS", "INTEGRATION"]]
    documents += [CANON / "CONNECTED-GENERATIVE-MODEL.md", BUILD / "README.md"]
    link_inputs.extend((p, p.read_text()) for p in documents)
    checked_links = []
    for owner, content in link_inputs:
        for raw in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            target = urlsplit(raw.strip("<>"))
            if target.scheme or target.netloc:
                continue
            path = (owner.parent / unquote(target.path)).resolve() if target.path else owner
            assert path.exists(), (str(owner), raw)
            if target.fragment and path.suffix == ".md":
                headings = re.findall(r"^#{1,6}\s+(.+)$", path.read_text(), re.M)
                anchors = {re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-") for h in headings}
                assert unquote(target.fragment) in anchors, (str(owner), raw)
            checked_links.append({"document": str(owner.relative_to(ROOT)), "target": raw})

    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(), "status": "passed",
        "scope": "Preserved-source, receipt and local-link verification; no proof or empirical rerun.",
        "combined_build_modules": 55, "new_audited_declarations": count,
        "new_empty_named_axiom_reports": empty, "import_entry_audits": 0,
        "all_current_sources_snapshots_logs_and_compiler_match_receipt": True,
        "ancestor_receipt_and_development_hashes_verified": True,
        "physical_law_changed": False, "separate_process_histories_physically_spliced": False,
        "whole_closure_named_axioms": receipt["named_axiom_dependencies"],
        "assumption_free_foundation_established": False, "empirical_experiment_rerun": False,
        "next_connection": "Formed and revisable participation, internally acquired consequence distinctions, and changes in affected continuation within one history.",
        "integration_edits": edit_states, "local_links": checked_links,
        "documents": [identity(p) for p in documents],
        "evidence": [identity(p) for p in [BUILD / "check.py", BUILD / "INPUTS.json",
                     BUILD / "verification.json", HERE / "NONDUAL-APPLICABILITY-CANONICAL-EDITS.json",
                     HERE / "development/nondual-applicability/DEVELOPMENT-ATTEMPTS.json", Path(__file__)]],
    }
    (HERE / "NONDUAL-APPLICABILITY-INTEGRATION.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": "passed", "modules": 55, "new_audits": count,
                      "new_empty_reports": empty, "local_links": len(checked_links)}))


if __name__ == "__main__":
    main()
