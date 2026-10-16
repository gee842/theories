#!/usr/bin/env python3
"""Check this reconstruction's evidence and links, without running a model."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = ROOT / "sources/38-participation-consequence-2026-10-06"
EVIDENCE = HERE / "development/participation-consequence"
MODEL = ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/coupling/architecture/learning"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def identity(path):
    return {"path": str(path.relative_to(ROOT)), "sha256": sha(path)}


def main():
    manifest = json.loads((SOURCE / "manifest.json").read_text())
    for relative, item in manifest["files"].items():
        path = SOURCE / relative
        assert sha(path) == item["sha256"] and path.stat().st_size == item["bytes"]

    evidence = json.loads((EVIDENCE / "EXTRACTED-EVIDENCE.json").read_text())
    assert evidence["status"] == "passed"
    assert sha(EVIDENCE / "extract_evidence.py") == evidence["extractor_sha256"]
    for path, expected in evidence["inspected_artifact_sha256"].items():
        assert sha(ROOT / path) == expected
    counts = {}
    for filename, key in [("witness.json", "source_sha256"),
                          ("results.json", "source_sha256"),
                          ("independent-check.json", "source_hashes"),
                          ("handoff-check.json", "source_sha256")]:
        data = json.loads((MODEL / filename).read_text())
        for path, expected in data[key].items():
            assert sha(ROOT / path) == expected, (filename, path)
        counts[filename] = len(data[key])
    results = json.loads((MODEL / "results.json").read_text())
    for arm, extracted in evidence["matched_saved_outcomes"].items():
        rows = [x for x in results["cases"]["primary"]["arms"][arm]["terminal_rows"]
                if x["entry"] == evidence["learning_entry"] and x["regime"] == 1]
        assert len(rows) == 1
        state = rows[0]["state"]
        assert all(state["parent"][k] == v for k, v in extracted["parent"].items())
        assert all(state[k] == v for k, v in extracted["learning"].items())
    assert len(evidence["actual_learning_trace"]) == 30
    assert not evidence["inherited_prior_motor_revision"]

    documents = [HERE / ("PARTICIPATION-CONSEQUENCE-" + name + ".md")
                 for name in ["MECHANISM", "IDENTIFICATION", "COMPARATORS", "REVIEW", "INTEGRATION"]]
    documents.append(SOURCE / "README.md")
    link_inputs = [(p, p.read_text()) for p in documents]
    edits = json.loads((HERE / "PARTICIPATION-CONSEQUENCE-CANONICAL-EDITS.json").read_text())
    edit_states = []
    for item in edits["edits"]:
        path = ROOT / item["path"]
        own = item["after_fragment"]
        if own.startswith(item["before_fragment"]):
            own = own[len(item["before_fragment"]):]
        assert own in path.read_text(), item["path"]
        edit_states.append({**identity(path), "own_fragment_present": True,
                           "whole_file_matches_immediate_post_edit": sha(path) == item["after_sha256"]})
        link_inputs.append((path, own))
    links = []
    for owner, text in link_inputs:
        for raw in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            target = urlsplit(raw.strip("<>"))
            if target.scheme or target.netloc:
                continue
            path = (owner.parent / unquote(target.path)).resolve() if target.path else owner
            assert path.exists(), (str(owner), raw)
            if target.fragment and path.suffix == ".md":
                headings = re.findall(r"^#{1,6}\s+(.+)$", path.read_text(), re.M)
                anchors = {re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-") for h in headings}
                assert unquote(target.fragment) in anchors, (str(owner), raw)
            links.append({"owner": str(owner.relative_to(ROOT)), "target": raw})

    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(), "status": "passed",
        "scope": "Evidence bindings, saved-result extraction and scoped link check only; no new scientific validation.",
        "source_package_files_verified": len(manifest["files"]),
        "original_model_source_bindings_verified": counts,
        "matched_saved_arms": len(evidence["matched_saved_outcomes"]),
        "saved_trace_events": len(evidence["actual_learning_trace"]),
        "new_theorems": 0, "original_model_modified": False, "simulation_rerun": False,
        "new_empirical_data": False, "assumption_free_foundation_established": False,
        "next_connection": "Consequence-sensitive formation/revision of relevant access, target differentiation and acquisition practices, with affected organizational continuation identified where claimed.",
        "documents": [identity(p) for p in documents], "canonical_edits": edit_states,
        "local_links": links,
        "evidence": [identity(p) for p in [SOURCE / "manifest.json",
                     EVIDENCE / "extract_evidence.py", EVIDENCE / "EXTRACTED-EVIDENCE.json",
                     HERE / "PARTICIPATION-CONSEQUENCE-CANONICAL-EDITS.json", Path(__file__)]],
    }
    (HERE / "PARTICIPATION-CONSEQUENCE-CHECKS.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": "passed", "source_package_files": len(manifest["files"]),
                      "matched_saved_arms": record["matched_saved_arms"], "local_links": len(links)}))


if __name__ == "__main__":
    main()
