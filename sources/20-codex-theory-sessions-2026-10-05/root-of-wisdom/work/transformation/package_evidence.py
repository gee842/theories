"""Package existing proofs, executed checks, and provenance without rerunning them."""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / "work/transformation"
REPORT = ROOT / "outputs/changing-the-interface.md"
TARGET = ROOT / "outputs/changing-the-interface-evidence.json"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def snapshot(name):
    path = WORK / name
    body = path.read_text()
    return {
        "path": str(path.relative_to(ROOT)),
        "sha256": digest(path),
        "content": json.loads(body) if path.suffix == ".json" else body,
    }


def main():
    baseline = json.loads((WORK / "preservation-manifest.json").read_text())
    preservation = [
        {"path": path, "before_sha256": old,
         "after_sha256": digest(ROOT / path),
         "unchanged": old == digest(ROOT / path)}
        for path, old in baseline.items()
    ]
    assert len(preservation) == 28
    assert all(item["unchanged"] for item in preservation)

    links = []
    for href in re.findall(r"\]\(([^)]+)\)", REPORT.read_text()):
        if href.startswith(("https://", "http://", "#")):
            continue
        path = (REPORT.parent / href).resolve()
        exists = path.is_file() or path == TARGET
        links.append({"target": href, "resolved": str(path),
                      "exists_or_current_package": exists})
    assert all(link["exists_or_current_package"] for link in links)

    sources = snapshot("integration-sources.json")
    source_status = []
    for source in sources["content"]["sources"]:
        path = Path(source["path"])
        current_hash = digest(path) if path.is_file() else None
        source_status.append({
            "path": str(path),
            "sha256_at_read": source["sha256"],
            "sha256_at_packaging": current_hash,
            "unchanged_since_read": current_hash == source["sha256"],
        })

    evidence = {
        "title": "Changing the interface: model, proof, and provenance",
        "packaged_utc": datetime.now(timezone.utc).isoformat(),
        "report": {
            "path": str(REPORT.relative_to(ROOT)),
            "sha256": digest(REPORT),
            "word_count_whitespace": len(REPORT.read_text().split()),
        },
        "status": "conditional mathematical construction; checks passed",
        "scope": {
            "repertoire": "Two supplied resource-specific interfaces and a two-tick rebuilding primitive.",
            "sufficient_contract": "Capacity and initial reserve 3; either coherent interface fully fitted and ready, with no rebuild underway; start at phase beginning; each constant-availability phase lasts at least 4 ticks; arbitrary processing bits read only by matching sensor.",
            "necessary_capacity": "Below 3, any two-tick rebuild exhausts reserve before completion while alive.",
            "necessary_dwell_at_capacity_3": "Alternating pure-resource phases of length 3 defeat all controllers, even with perfect future knowledge. Counting proof gives death by 21; exhaustive full-information action-history propagation gives no survivor after tick 14.",
            "comparison": "Every permanently fitted receptor/transporter/converter choice under the same one-slot-per-module physical budget; not every fixed algorithm.",
            "dwell3_check_scope": "The joint-model graph checks the implemented reactive policy only. The independent limits audit and all-history enumeration establish impossibility for every allowed controller.",
            "general_theorem": "Finite known-model partial-information indefinite safety, with nonempty transitions and unavailable actions entering absorbing failure.",
            "tests": "Exact finite enumeration and reachable-state analysis. No physical, biological, human-subject, or other-session experiment was rerun.",
            "claim_limit": "No scientific priority, derivation of monism, subjective experience, ethical criterion, new purpose, or unforeseen capability is established.",
        },
        "proofs": [snapshot("joint-model-notes.md"), snapshot("limits-audit.md")],
        "executable_checks": [snapshot("check_joint_model.py"), snapshot("check_limits.py")],
        "check_results": [snapshot("joint-model-checks.json"), snapshot("limits-checks.json")],
        "peer_reviews": [snapshot("review-model.md"), snapshot("review-limits.md"), snapshot("review-sources.md")],
        "review_incorporation": {
            "final_author_check": "Parent inspected proofs, result files, source scopes, and final reviews. Both mathematical reviewers requested an explicit initially ready interface with no rebuild underway; this was added to both sufficient entry conditions in the final report. Source reviewer passed without required corrections; its optional checks-versus-experiments wording was adopted.",
            "corrections_during_construction": [
                "Independent resource processing bits make the changed observation substantive.",
                "Storage cap applies after the combined maintenance and intake update.",
                "Old sensor is available when rebuilding starts; next tick completes without a new reading.",
                "Phase-start or initially matched full-reserve initialization is explicit.",
                "Final review correction: both sufficient entry conditions require a ready coherent interface with no rebuild underway.",
                "The separate all-controller timing proof is distinguished from a policy-specific reachability failure.",
                "The fixed-point operator explicitly ranges over safe observation-coherent beliefs.",
                "Changing selective exchange does not derive the initial enclosure or rebuilding machinery.",
            ],
        },
        "source_manifest": sources,
        "integration_audit": {
            "path": "work/transformation/integration-audit.md",
            "sha256": digest(WORK / "integration-audit.md"),
            "scope": "Read-only integration; full audit retained locally. Existing other-session results acknowledged, not rerun or presented as newly discovered.",
        },
        "source_status_at_packaging": source_status,
        "preservation": {
            "pre_existing_outputs": len(preservation),
            "all_unchanged": True,
            "files": preservation,
        },
        "report_local_links": links,
    }
    TARGET.write_text(json.dumps(evidence, indent=2, ensure_ascii=False) + "\n")
    assert json.loads(TARGET.read_text())["report"]["sha256"] == digest(REPORT)
    print(json.dumps({"report": str(REPORT), "report_words": evidence["report"]["word_count_whitespace"],
                      "evidence": str(TARGET), "evidence_bytes": TARGET.stat().st_size,
                      "preserved_outputs": 28, "valid_local_links": len(links),
                      "sources_unchanged_since_read": sum(x["unchanged_since_read"] for x in source_status),
                      "source_count": len(source_status)}, indent=2))


if __name__ == "__main__":
    main()
