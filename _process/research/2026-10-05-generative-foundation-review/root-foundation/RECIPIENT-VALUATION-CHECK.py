#!/usr/bin/env python3
"""Bind accepted recipient-harm artifacts; no scientific analysis or network calls."""
from collections import Counter
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote, urlsplit


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
EXPERIMENT = ROOT / "experiments/recipient-harm-valuation"
SOURCES = ROOT / "sources/30-recipient-harm-valuation-2026-10-06"
NEURAL_SOURCES = ROOT / "sources/32-shared-affect-action-2026-10-06"
CANONICAL = ROOT / "theories/shengsheng-buxi-generative-existence/unified-2026-10-05/RECIPIENT-HARM-AND-ACTION.md"
OUTPUT = HERE / "RECIPIENT-VALUATION-INTEGRATION.json"
# Earlier behavioral-only acceptance is preserved in the canonical review and git 113a956.
ACCEPTED_CANONICAL = "309ececbbb21e184e99d73249504736c672b589a472977efd8380912333e7ca8"
NEURAL_MANIFEST = "1978b0aad933511daaad4d61dd6e4bb4aaba8658c86124847d4ef6f48f467996"
NEURAL_CONTRACT = "fcdd52b271e52c24e080a0877a8480f1a80c354d57fdde32747a115272abf082"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read(path):
    return json.loads(path.read_text())


def digest(path, algorithm="sha256"):
    return hashlib.new(algorithm, path.read_bytes()).hexdigest()


def relative(path):
    return str(path.resolve().relative_to(ROOT))


def main():
    bindings = []
    bound_files = set()

    def bind(path, expected, claim, size=None):
        path = path.resolve()
        require(path.is_file(), f"Missing file: {path}")
        actual = digest(path)
        require(actual == expected, f"Digest mismatch: {claim}: {relative(path)}")
        if size is not None:
            require(path.stat().st_size == size, f"Size mismatch: {relative(path)}")
        bindings.append({"claim": claim, "path": relative(path), "sha256": actual})
        bound_files.add(path)

    def bind_map(mapping, base, claim):
        for name, expected in mapping.items():
            bind(base / name, expected, claim)

    manifest = read(SOURCES / "manifest.json")
    require(len(manifest["files"]) == 20, "Source manifest coverage changed")
    paths = [entry["path"] for entry in manifest["files"]]
    require(len(set(paths)) == 20, "Duplicate source manifest entry")
    for entry in manifest["files"]:
        bind(SOURCES / entry["path"], entry["sha256"], "source_manifest", entry["bytes"])

    bind(NEURAL_SOURCES / "manifest.json", NEURAL_MANIFEST, "neural_source_manifest_identity")
    neural_manifest = read(NEURAL_SOURCES / "manifest.json")
    neural_paths = {entry["path"] for entry in neural_manifest["files"]}
    require(len(neural_paths) == len(neural_manifest["files"]) == 12,
            "Neural source manifest coverage changed")
    actual_neural_paths = {str(p.relative_to(NEURAL_SOURCES))
                           for p in NEURAL_SOURCES.rglob("*") if p.is_file()}
    require(actual_neural_paths == neural_paths | {"manifest.json"},
            "Neural source package contains unbound or missing files")
    for entry in neural_manifest["files"]:
        bind(NEURAL_SOURCES / entry["path"], entry["sha256"],
             "neural_source_manifest", entry["bytes"])

    originals = manifest["original_osf_files"]
    require(len(originals) == 4 and len({x["path"] for x in originals}) == 4,
            "OSF-original coverage changed")
    osf_checks = []
    for entry in originals:
        path = SOURCES / entry["path"]
        bind(path, entry["sha256"], "osf_original_manifest", entry["bytes"])
        metadata = read(SOURCES / entry["metadata_path"])["data"]
        attrs = metadata["attributes"]
        hashes = attrs["extra"]["hashes"]
        bind(path, hashes["sha256"], "preserved_osf_api_sha256", attrs["size"])
        require(digest(path, "md5") == hashes["md5"], f"OSF MD5 mismatch: {path}")
        require(metadata["id"] == entry["osf_id"] and attrs["guid"] == entry["guid"],
                f"OSF identity mismatch: {path}")
        require(attrs["name"] == path.name and attrs["current_version"] == entry["osf_version"],
                f"OSF name/version mismatch: {path}")
        require(metadata["relationships"]["node"]["data"]["id"] == manifest["osf_node"],
                f"OSF project mismatch: {path}")
        require(metadata["links"]["download"] == entry["download_url"],
                f"OSF download identity mismatch: {path}")
        versions = read(SOURCES / f"metadata/versions-{entry['osf_id']}.json")["data"]
        matched = [v for v in versions if v["id"] == str(entry["osf_version"])]
        require(len(matched) == 1 and matched[0]["attributes"]["size"] == entry["bytes"],
                f"Preserved OSF version size mismatch: {path}")
        require(entry["upstream_hash_match"] is True, "Contradictory upstream-match record")
        osf_checks.append({"path": relative(path), "osf_id": entry["osf_id"],
                           "version": entry["osf_version"], "sha256": hashes["sha256"],
                           "md5": hashes["md5"], "bytes": entry["bytes"]})
    validation = manifest["read_only_validation"]
    require(validation == {"osf_original_hashes_match": True,
                           "trial_workbook_cached_cells_compared": 7128,
                           "trial_workbook_cached_cell_mismatches": 0,
                           "trial_identity_join_count": 78, "summary_identity_count": 142},
            "Saved source-validation scope changed")

    freeze = read(EXPERIMENT / "protocol-freeze.json")
    require(freeze["status"] == "frozen_before_new_local_aggregates", "Protocol freeze status")
    bind(EXPERIMENT / "PROTOCOL.md", freeze["protocol_sha256"], "protocol_freeze")
    bind_map(freeze["source_sha256"], ROOT, "protocol_frozen_sources")
    clarification = read(EXPERIMENT / "schema-clarification-freeze.json")
    require(clarification["status"] == "clarification_frozen_before_first_aggregate",
            "Clarification freeze status")
    bind_map(clarification["files"], EXPERIMENT, "schema_clarification_freeze")

    results = read(EXPERIMENT / "results.json")
    producer = read(EXPERIMENT / "analysis-receipt.json")
    require(producer["status"] == "computed", "Producer receipt status")
    for field, filename in [("code_sha256", "analysis.py"), ("results_sha256", "results.json"),
                            ("protocol_sha256", "PROTOCOL.md"),
                            ("clarification_sha256", "SCHEMA-CLARIFICATION.md")]:
        bind(EXPERIMENT / filename, producer[field], "producer_receipt")
    for field, filename in [("analysis_sha256", "analysis.py"), ("protocol_sha256", "PROTOCOL.md"),
                            ("clarification_sha256", "SCHEMA-CLARIFICATION.md")]:
        bind(EXPERIMENT / filename, results[field], "results_input")
    require(results["source_sha256"] == freeze["source_sha256"], "Frozen source-set mismatch")
    bind_map(results["source_sha256"], ROOT, "results_sources")

    independent = read(EXPERIMENT / "independent-verification.json")
    require(independent["status"] == "passed" and independent["producer_imported"] is False,
            "Independent verification not accepted")
    for field, filename in [("checker_sha256", "check_analysis.py"),
                            ("producer_results_sha256", "results.json"),
                            ("independent_reconstruction_sha256", "independent-reconstruction.json"),
                            ("independent_detail_sha256", "independent-detail.json"),
                            ("protocol_sha256", "PROTOCOL.md"),
                            ("clarification_sha256", "SCHEMA-CLARIFICATION.md")]:
        bind(EXPERIMENT / filename, independent[field], "independent_verification")
    for filename, source_key in [("independent-reconstruction.json", "source_sha256"),
                                 ("independent-detail.json", "source_hashes")]:
        saved = read(EXPERIMENT / filename)
        source_base = SOURCES / "original" if filename == "independent-detail.json" else ROOT
        normalized_sources = {relative(source_base / name): value
                              for name, value in saved[source_key].items()}
        require(normalized_sources == freeze["source_sha256"], f"Independent source set: {filename}")
        bind_map(saved[source_key], source_base, filename)
        bind(EXPERIMENT / "PROTOCOL.md", saved["protocol_sha256"], filename)
        bind(EXPERIMENT / "SCHEMA-CLARIFICATION.md", saved["clarification_sha256"], filename)
    counts = {"comparison_count": 21581, "actors": 78, "raw_trial_slots": 6240,
              "groups": 7, "contrasts": 6, "leave_one_actor": 26, "leave_one_sbl_label": 4,
              "hypothetical_completions": 3, "source_audit_comparisons": 780,
              "source_audit_flags": 39}
    require(all(independent[k] == v for k, v in counts.items()), "Independent receipt scope changed")
    faults = independent["fault_checks"]
    require(len(faults) == 12 and len({x["name"] for x in faults}) == 12
            and all(x["rejected"] is True for x in faults), "Fault-check record incomplete")
    require(len(results["actors"]) == 78 and len(results["groups"]) == 7
            and len(results["contrasts"]) == 6, "Result coverage changed")
    require(len(results["primary_leave_one_actor_out"]) == 26
            and len(results["primary_leave_one_sbl_label_out"]) == 4
            and len(results["actor70_unknown_completion_sensitivity"]) == 3,
            "Saved sensitivity coverage changed")
    require(results["new_animal_experiments"] == 0, "Unexpected new animal experiment")
    primary = results["contrasts"]["primary_harm_minus_no_harm"]
    require(primary["left_actors"] == freeze["primary_actors"]["male_contingent_harm"]
            and primary["right_actors"] == freeze["primary_actors"]["male_no_harm"],
            "Primary actor selection differs from freeze")
    require(primary["change_differences"]["shock_all"] == {
        "preferred_offered": "-841/5040", "alternative_offered": "827/5040",
        "nonresponse_offered": "1/360", "unknown_offered": "0",
        "preferred_completed": "-5451/33040"}, "Accepted primary result changed")

    audit = read(EXPERIMENT / "source-summary-audit.json")
    require(audit["status"] == "pass" and audit["discrepancies_classified"] == 39,
            "Summary audit status/coverage changed")
    bind_map(audit["input_sha256"], ROOT, "source_summary_audit_inputs")
    require(audit["categories"] == {"spreadsheet_average_ignores_undefined_session": 1,
                                    "omitted_total_summary": 32,
                                    "scheduled_versus_completed_response_denominator": 6},
            "Summary-audit classification changed")
    require(dict(Counter(x["category"] for x in audit["findings"])) == audit["categories"],
            "Summary-audit category coverage mismatch")
    require([x["original_discrepancy"] for x in audit["findings"]]
            == results["source_summary_audit"]["discrepancies"],
            "Summary audit does not classify the actual result discrepancies")
    history = EXPERIMENT / "review-history/summary-nan"
    failure = read(history / "preservation.json")
    bind(history / failure["file"], failure["sha256"], "preserved_initial_parser_failure", failure["bytes"])
    require(failure["sha256"] != producer["code_sha256"], "Initial failure replaced by final code")
    require("NaN" in failure["reason"] and "No result file was written" in
            (EXPERIMENT / "ANALYSIS-REPAIRS.md").read_text(), "Parser-failure explanation missing")

    bind(CANONICAL, ACCEPTED_CANONICAL, "accepted_canonical_identity")
    review = (HERE / "RECIPIENT-VALUATION-CANONICAL-REVIEW.md").read_text()
    for path in [CANONICAL, EXPERIMENT / "results.json", EXPERIMENT / "independent-verification.json",
                 EXPERIMENT / "source-summary-audit.json"]:
        require(digest(path) in review, f"Review does not bind current {relative(path)}")
    require("Final verdict: accepted within the stated scope; no outstanding correction" in review,
            "Final canonical acceptance absent")
    neural_review = (HERE / "SHARED-AFFECT-ACTION-REVIEW.md").read_text()
    bind(HERE / "SHARED-AFFECT-ACTION-CONTRACT.md", NEURAL_CONTRACT,
         "accepted_neural_identification_contract")
    require(ACCEPTED_CANONICAL in neural_review and NEURAL_CONTRACT in neural_review,
            "Neural review does not bind current canonical and contract")

    docs = [CANONICAL, SOURCES / "README.md", NEURAL_SOURCES / "README.md"]
    docs += [HERE / f"SHARED-AFFECT-ACTION-{suffix}.md"
             for suffix in ("EVIDENCE", "CONTRACT", "REVIEW")]
    docs += [HERE / f"RECIPIENT-VALUATION-{suffix}.md"
             for suffix in ("EVIDENCE", "IDENTIFICATION", "REVIEW", "CANONICAL-REVIEW")]
    docs += [EXPERIMENT / name for name in
             ("README.md", "PROTOCOL.md", "SCHEMA-CLARIFICATION.md", "ANALYSIS-REPAIRS.md")]
    indexes = [ROOT / "RESEARCH.md", CANONICAL.parent.parent / "README.md", HERE / "README.md",
               ROOT / "experiments/README.md", ROOT / "sources/SOURCES.md"]
    indexes += [CANONICAL.parent / name for name in
                ("GENERATIVE-GROUNDING.md", "ALIGNMENT-COMPLETION.md", "ALIGNMENT-AND-GOVERNANCE.md")]
    index_excerpts = []
    links = []
    for doc in docs + indexes:
        content = doc.read_text()
        if doc in indexes:
            content = "\n".join(line for line in content.splitlines()
                                if re.search(r"recipient-harm|RECIPIENT-HARM|RECIPIENT-VALUATION", line))
            require(bool(content), f"Missing study integration entry: {relative(doc)}")
            index_excerpts.append({"path": relative(doc), "matching_lines": content.splitlines(),
                                   "excerpt_sha256": hashlib.sha256(content.encode()).hexdigest()})
        destinations = re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)', content)
        destinations += re.findall(r'^\[[^]\n]+\]:\s*(\S+)', content, re.M)
        for destination in destinations:
            destination = destination.strip("<>")
            url = urlsplit(destination)
            if url.scheme or url.netloc or not url.path:
                continue
            target = (doc.parent / unquote(url.path)).resolve()
            require(target.exists() or target == OUTPUT, f"Broken local link: {doc}: {destination}")
            links.append({"from": relative(doc), "destination": destination,
                          "target": relative(target)})

    files = bound_files | set(docs) | {Path(__file__).resolve(), SOURCES / "manifest.json"}
    files |= {EXPERIMENT / name for name in ("protocol-freeze.json", "schema-clarification-freeze.json",
               "analysis-receipt.json", "independent-verification.json", "source-summary-audit.json")}
    files.add(history / "preservation.json")
    receipt = {
        "schema_version": 1,
        "status": "pass: accepted descriptive recipient-harm study identities and integration verified",
        "named_connection": "Recipient-linked physical consequences to changing action under unchanged offered food.",
        "scope": "Checks saved byte identities, receipt consistency, accepted canonical identity and local file-link targets. No scientific calculation or checker rerun; no network verification or new data collection.",
        "source_manifest_files_checked": len(manifest["files"]),
        "neural_source_manifest_files_checked": len(neural_manifest["files"]),
        "neural_extension_scope": "Reviewed primary-source comparison and conditional identification contract only; no neural-data analysis or new behavioral calculation.",
        "osf_originals_checked": len(osf_checks), "osf_original_checks": osf_checks,
        "source_workbook_validation": {"mode": "saved manifest claim, not recomputed", **validation},
        "saved_independent_verification_counts": counts,
        "saved_fault_checks_rejected": len(faults),
        "primary_change": primary["change_differences"]["shock_all"],
        "source_audit_categories": audit["categories"],
        "preserved_parser_failure": {"path": relative(history / failure["file"]),
                                      "sha256": failure["sha256"], "bytes": failure["bytes"]},
        "accepted_canonical_sha256": ACCEPTED_CANONICAL,
        "markdown_files_checked": len(docs), "local_file_links_checked": len(links),
        "local_file_links": links, "fragment_anchors_checked": False,
        "shared_index_excerpts_checked": len(index_excerpts),
        "shared_index_excerpts": index_excerpts,
        "shared_index_scope": "Only matching study-integration lines checked and excerpt-hashed; unrelated concurrent edits are outside this receipt.",
        "hash_claims_checked": len(bindings), "hash_claims": bindings,
        "bound_file_count": len(files),
        "file_hashes": {relative(p): digest(p) for p in sorted(files)},
        "checker_sha256": digest(Path(__file__)),
        "shared_indexes_edited": False, "scientific_reruns": 0,
        "new_animal_experiments": 0, "unified_foundation_complete": False,
        "remaining_scope": ["assignment and dependence identification", "separate value/correspondence acquisition",
                            "recipient outcome versus actor cue relief", "ethical standing and justified action"]}
    OUTPUT.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({k: receipt[k] for k in ["status", "source_manifest_files_checked", "osf_originals_checked",
                     "markdown_files_checked", "local_file_links_checked", "hash_claims_checked", "bound_file_count"]}))


if __name__ == "__main__":
    main()
