#!/usr/bin/env python3
"""Verify this integration's links and preserved evidence, without scientific reruns."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
THEORY = REPO / "theories/becoming/chapters"
NATIVE = REPO / "experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/feedback"
FORMAL = NATIVE / "calibration-revision/formal"
OUTPUT = HERE / "CALIBRATION-REVISION-CHECKS.json"
DOCS = [
    HERE / "CALIBRATION-REVISION-INTEGRATION.md",
    HERE / "CALIBRATION-REVISION-REVIEW.md",
    HERE / "SYSTEMS-HIGHER-DYNAMICS.md",
    HERE / "REMAINING-DEPENDENCY-INTEGRATION.md",
    NATIVE / "CALIBRATION-REVISION-PROTOCOL.md",
    NATIVE / "CALIBRATION-REVISION-MECHANISM.md",
    FORMAL / "FORMAL-NOTES.md",
    REPO / "sources/15-codex-theory-conversations/2026-10-06-calibration-revision-continuation.md",
]
INDEXES = {
    REPO / "RESEARCH.md": "**Later consequences now revise diagnostic reliance and inquiry,",
    REPO / "theories/becoming/README.md": "**Failure now changes what the learner investigates,",
    THEORY / "GENERATIVE-GROUNDING.md": "**Actual later effect → qualified reliance → further inquiry,",
    HERE / "README.md": "**Consequences revise diagnostic reliance,",
    NATIVE / "README.md": "**Final effects now enter further inquiry,",
}
CANONICAL = THEORY / "CONNECTED-GENERATIVE-MODEL.md"
SECTION = "## When consequences challenge the diagnostic relation"
FROZEN = {
    NATIVE / "CALIBRATION-REVISION-PROTOCOL.md": "3223b6e2e0b4a65ba3f419deb7373c6f30f88d9d7b2a0e01df6b39ab5f60f085",
    NATIVE / "calibration_revision.py": "732d855ae20f4be322442dfce767fd839759cc5181ce5a8c33571ddab23efe1b",
    NATIVE / "calibration-revision-results.json": "04e0b604172d2042fc8418af54e549a586bbaefc60e43cebe980a56fd164eca1",
    NATIVE / "calibration_revision_check_review.py": "c3b92cf690490ab5d3e0cefbb59b4d37d980bd0f81955920531951c28a97ff02",
    NATIVE / "calibration-revision-independent-check.json": "f5e0104d85fd981c5e94b506837593b376798c7a1b2534a2bd80434b5fd7a7db",
    FORMAL / "verification.json": "c28247f5465a0f70bf8c507bbf36e65ec5c6e4f6de53958141336f129000c4ce",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def anchors(path):
    result = set()
    for heading in re.findall(r"^#{1,6}\s+(.+)$", path.read_text(), re.M):
        result.add(re.sub(r"\s", "-", re.sub(r"[^\w\s-]", "", heading.lower())))
    return result


def main():
    failures = []
    hash_checks = links = 0

    def require(condition, message):
        if not condition:
            failures.append(message)

    def check_hash(path, expected):
        nonlocal hash_checks
        hash_checks += 1
        require(path.exists() and sha(path) == expected, f"Hash mismatch: {path}")

    pieces = {path: path.read_text() for path in DOCS}
    for path, prefix in INDEXES.items():
        matches = [line for line in path.read_text().splitlines() if line.startswith(prefix)]
        require(len(matches) == 1, f"Missing or duplicate index entry: {path}")
        pieces[path] = "\n".join(matches)
    canonical = CANONICAL.read_text()
    require(canonical.count(SECTION) == 1, "Missing or duplicate canonical section")
    pieces[CANONICAL] = SECTION + canonical.split(SECTION, 1)[1].split("\n## ", 1)[0]
    for path, source in pieces.items():
        for raw in re.findall(r"\]\(([^)]+)\)", source):
            if raw.startswith(("https://", "http://", "mailto:")):
                continue
            target, _, anchor = unquote(raw.strip("<>")).partition("#")
            resolved = (path.parent / target).resolve() if target else path
            links += 1
            require(resolved == OUTPUT or resolved.exists(), f"Missing target in {path}: {raw}")
            if anchor and resolved.exists() and resolved.suffix == ".md":
                require(anchor in anchors(resolved), f"Missing anchor in {path}: {raw}")

    for path, expected in FROZEN.items():
        check_hash(path, expected)
    native = json.loads((NATIVE / "calibration-revision-independent-check.json").read_text())
    require(native["status"] == "passed", "Independent native receipt must pass")
    for key, expected in [("case_count", 25), ("parent_count", 8),
                          ("continuation_state_points", 288), ("successful_charged_events", 257),
                          ("recorded_denials", 6), ("unique_source_bindings", 24)]:
        require(native[key] == expected, f"Unexpected native count: {key}")
    require(len(native["rejected_mutations"]) == 9, "Unexpected corruption-check count")
    for relative, expected in native["source_bindings"].items():
        check_hash(REPO / relative, expected)
    for filename, key in [("calibration-revision-results.json", "results_sha256"),
                          ("calibration_revision_check_review.py", "check_source_sha256"),
                          ("CALIBRATION-REVISION-PROTOCOL.md", "prospective_protocol_sha256")]:
        check_hash(NATIVE / filename, native[key])

    receipt_path = FORMAL / "verification.json"
    receipt = json.loads(receipt_path.read_text())
    require(receipt["status"] == "passed" and receipt["source_hashes_stable"],
            "Formal receipt must pass with stable source bindings")
    for key, expected in [("mathematical_theorem_count", 32),
                          ("saved_correspondence_theorem_count", 399),
                          ("inherited_audit_count", 61), ("total_audit_count", 492)]:
        require(receipt[key] == expected, f"Unexpected formal count: {key}")
    require(not receipt["custom_axioms"] and not receipt["proof_holes"]
            and not receipt["native_decide_used"], "Unexpected formal proof escape")
    require(set(receipt["standard_axioms"]) <= {"propext", "Quot.sound"},
            "Unexpected named proof dependency")
    fixture = REPO / receipt["generated_fixture"]
    run = fixture.parent
    require(len(receipt["source_hashes"]) == 33, "Unexpected formal binding count")
    for relative, expected in receipt["source_hashes"].items():
        check_hash(REPO / relative, expected)
        check_hash(run / "snapshots" / relative, expected)
    check_hash(fixture, receipt["generated_fixture_sha256"])
    check_hash(REPO / receipt["independent_runtime_receipt"], receipt["independent_runtime_receipt_sha256"])
    check_hash(Path(receipt["compiler"]["path"]), receipt["compiler"]["sha256"])
    check_hash(run / "verification.json", sha(receipt_path))
    require(sum(module["audit_count"] for module in receipt["modules"]) == 492,
            "Module audit totals differ")
    for module in receipt["modules"]:
        check_hash(REPO / module["log"], module["log_sha256"])
        require(len(module["theorem_audits"]) == module["audit_count"],
                f"Module audit list differs: {module['module']}")
    for key, expected in [("case_count", 25), ("state_count", 288),
                          ("saved_edges", 263), ("event_attempts", 262),
                          ("charged_events", 257), ("denied_events", 6),
                          ("parent_construction_equalities", 3), ("mask_encoding_equalities", 8)]:
        require(receipt["coverage"][key] == expected, f"Unexpected correspondence count: {key}")
    # Preserve the previously accepted proof/source package independently of
    # the new checker's subset of inherited dependencies.
    previous = json.loads((NATIVE / "remaining-dependency/formal/verification.json").read_text())
    require(previous["status"] == "passed", "Preceding formal receipt must retain its pass")
    for relative, expected in previous["source_hashes"].items():
        check_hash(REPO / relative, expected)

    result = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if not failures else "failed",
        "scope": "Local targets/anchors and owned index/canonical sections; source, snapshot, receipt, log, compiler and inherited-source preservation. No scientific rerun, proof rebuild or external-link verification.",
        "local_links_checked": links,
        "preservation_hash_checks": hash_checks,
        "native_cases": 25,
        "native_states": 288,
        "new_substantive_theorem_audits": 32,
        "saved_correspondence_audits": 399,
        "replayed_inherited_audits": 61,
        "formal_receipt_sha256": sha(receipt_path),
        "review_sha256": sha(HERE / "CALIBRATION-REVISION-REVIEW.md"),
        "checked_document_or_section_sha256": {
            str(path.relative_to(REPO)): hashlib.sha256(source.encode()).hexdigest()
            for path, source in pieces.items()
        },
        "checker_sha256": sha(Path(__file__)),
        "final_edit_record_sha256": sha(HERE / "CALIBRATION-REVISION-DOC-EDITS.json"),
        "failures": failures,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({key: result[key] for key in
                      ["status", "local_links_checked", "preservation_hash_checks", "failures"]}))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
