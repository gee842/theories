#!/usr/bin/env python3
"""Check integrated links and preserved evidence; do not rerun the experiments or Lean."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
THEORY = REPO / "theories/shengsheng-buxi-generative-existence/unified-2026-10-05"
NATIVE = REPO / "experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/feedback"
FORMAL = NATIVE / "remaining-dependency/formal"
OUTPUT = HERE / "REMAINING-DEPENDENCY-CHECKS.json"
DOCS = [
    HERE / "REMAINING-DEPENDENCY-INTEGRATION.md",
    HERE / "REMAINING-DEPENDENCY-REVIEW.md",
    HERE / "SYSTEMS-HIGHER-DYNAMICS.md",
    NATIVE / "REMAINING-DEPENDENCY-PROTOCOL.md",
    NATIVE / "REMAINING-DEPENDENCY-MECHANISM.md",
    NATIVE / "REMAINING-DEPENDENCY-ERRATUM.md",
    FORMAL / "FORMAL-NOTES.md",
    REPO / "sources/15-codex-theory-conversations/2026-10-06-remaining-dependency-continuation.md",
]
INDEXES = {
    REPO / "RESEARCH.md": "**Acquired continuing dependency now changes later activity,",
    REPO / "theories/shengsheng-buxi-generative-existence/README.md": "**Learning what must continue after success,",
    THEORY / "GENERATIVE-GROUNDING.md": "**Acquired continuing dependency → maintained relation → further activity,",
    HERE / "README.md": "**Acquired continuing dependency completed locally,",
    NATIVE / "README.md": "**Further continuation, 6 October 2026:**",
}
CANONICAL = THEORY / "CONNECTED-GENERATIVE-MODEL.md"
SECTION = "## Acquired dependency changes what must remain organized"
FROZEN = {
    NATIVE / "REMAINING-DEPENDENCY-PROTOCOL.md": "d56551ba5d025e51d0b19a8e463e69b32fcd79746403120d25786be91cea1532",
    NATIVE / "remaining_dependency.py": "75e715f1a7a0af499a39887e3fc9b38d88b66125d313361de851c421d9197127",
    NATIVE / "remaining-dependency-results.json": "424540b7688e836b8357b86adf1ae7f3382349c7581abe83df37d36ccbae72b2",
    NATIVE / "remaining_dependency_check_review.py": "d46972459e2680839a4092bd226f1a5da9401b748377d5c2b15089f3ccad1cdb",
    NATIVE / "remaining-dependency-independent-check.json": "e9adb2a52c661054cd18bb60ca057bf716a33646474076ff13366e0369cd99f1",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def anchors(path):
    result = set()
    for heading in re.findall(r"^#{1,6}\s+(.+)$", path.read_text(), re.M):
        heading = re.sub(r"[^\w\s-]", "", heading.lower())
        result.add(re.sub(r"\s", "-", heading))
    return result


def main():
    failures = []
    hash_checks = 0
    links = 0
    pieces = {}

    def require(condition, message):
        if not condition:
            failures.append(message)

    def check_hash(path, expected):
        nonlocal hash_checks
        hash_checks += 1
        require(path.exists() and sha(path) == expected, f"Hash mismatch: {path}")

    for path in DOCS:
        pieces[path] = path.read_text()
    for path, prefix in INDEXES.items():
        matches = [line for line in path.read_text().splitlines() if line.startswith(prefix)]
        require(len(matches) == 1, f"Missing or duplicate new index entry: {path}")
        pieces[path] = "\n".join(matches)
    canonical = CANONICAL.read_text()
    require(canonical.count(SECTION) == 1, "Missing or duplicate canonical section")
    pieces[CANONICAL] = SECTION + canonical.split(SECTION, 1)[1].split("\n## ", 1)[0]
    for path, source in pieces.items():
        for raw in re.findall(r"\]\(([^)]+)\)", source):
            if raw.startswith(("https://", "http://", "mailto:")):
                continue
            raw = unquote(raw.strip("<>"))
            target, _, anchor = raw.partition("#")
            resolved = (path.parent / target).resolve() if target else path
            links += 1
            # The receipt is created below; recognize only this exact output.
            require(resolved == OUTPUT or resolved.exists(), f"Missing target in {path}: {raw}")
            if anchor and resolved.exists() and resolved.suffix == ".md":
                require(anchor in anchors(resolved), f"Missing anchor in {path}: {raw}")

    for path, expected in FROZEN.items():
        check_hash(path, expected)
    native = json.loads((NATIVE / "remaining-dependency-independent-check.json").read_text())
    require(native["status"] == "passed", "Native independent receipt did not pass")
    for key, expected in [("case_count", 28), ("continuation_state_points", 362),
                          ("successful_charged_events", 325), ("ancestry_admissible_cases", 27),
                          ("unique_source_bindings", 19)]:
        require(native[key] == expected, f"Unexpected native count: {key}")
    rejected = native["conditional_suffix_only_cases"]
    require(len(rejected) == 1 and rejected[0]["name"] == "capacity_forty"
            and rejected[0]["actual_inherited_peak"] == 114
            and not rejected[0]["whole_history_capacity_admissible"],
            "Rejected capacity ancestry must remain rejected")
    require(len(native["rejected_mutations"]) == 7, "Unexpected mutation-check count")
    for relative, expected in native["source_bindings"].items():
        check_hash(REPO / relative, expected)
    for name, key in [("remaining-dependency-results.json", "results_sha256"),
                      ("remaining_dependency_check_review.py", "check_source_sha256"),
                      ("REMAINING-DEPENDENCY-PROTOCOL.md", "prospective_protocol_sha256")]:
        check_hash(NATIVE / name, native[key])

    receipt_path = FORMAL / "verification.json"
    receipt = json.loads(receipt_path.read_text())
    require(receipt["status"] == "passed" and receipt["source_hashes_stable"],
            "Formal verification must pass with unchanged sources")
    for key, expected in [("mathematical_theorem_count", 43),
                          ("saved_correspondence_theorem_count", 446),
                          ("inherited_audit_count", 18), ("total_audit_count", 507)]:
        require(receipt[key] == expected, f"Unexpected formal count: {key}")
    require(not receipt["custom_axioms"] and not receipt["proof_holes"]
            and not receipt["native_decide_used"], "Formal escape or custom axiom reported")
    require(set(receipt["standard_axioms"]) <= {"propext", "Quot.sound"},
            "Unexpected proof dependency")
    fixture = REPO / receipt["generated_fixture"]
    run = fixture.parent
    require(len(receipt["source_hashes"]) == 25, "Unexpected bound source count")
    for relative, expected in receipt["source_hashes"].items():
        check_hash(REPO / relative, expected)
        check_hash(run / "snapshots" / relative, expected)
    check_hash(fixture, receipt["generated_fixture_sha256"])
    check_hash(REPO / receipt["independent_runtime_receipt"], receipt["independent_runtime_receipt_sha256"])
    check_hash(Path(receipt["compiler"]["path"]), receipt["compiler"]["sha256"])
    check_hash(run / "verification.json", sha(receipt_path))
    require(sum(m["audit_count"] for m in receipt["modules"]) == 507,
            "Module audit totals do not agree")
    for module in receipt["modules"]:
        check_hash(REPO / module["log"], module["log_sha256"])
        require(len(module["theorem_audits"]) == module["audit_count"],
                f"Audit list length differs: {module['module']}")
    coverage = receipt["coverage"]
    for key, expected in [("state_count", 362), ("event_attempts", 333),
                          ("denied_events", 8), ("charged_events", 325),
                          ("case_count", 28), ("ancestry_admissible_cases", 27)]:
        require(coverage[key] == expected, f"Unexpected saved correspondence count: {key}")
    require(coverage["conditional_suffix_only_cases"] == ["capacity_forty"],
            "Formal capacity fixture scope changed")

    output = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if not failures else "failed",
        "scope": "Local links/anchors and owned index/canonical sections; preserved native and Lean sources, snapshots, receipts, logs and compiler. No scientific rerun, proof rebuild or external-link verification.",
        "local_links_checked": links,
        "preservation_hash_checks": hash_checks,
        "native_ancestry_admissible_cases": 27,
        "rejected_ancestry_conditional_fixtures": ["capacity_forty"],
        "new_substantive_theorem_audits": 43,
        "saved_correspondence_audits": 446,
        "replayed_core_audits": 18,
        "formal_receipt_sha256": sha(receipt_path),
        "review_sha256": sha(HERE / "REMAINING-DEPENDENCY-REVIEW.md"),
        "checked_document_or_section_sha256": {
            str(path.relative_to(REPO)): hashlib.sha256(source.encode()).hexdigest()
            for path, source in pieces.items()
        },
        "checker_sha256": sha(Path(__file__)),
        "final_edit_record_sha256": sha(HERE / "REMAINING-DEPENDENCY-DOC-EDITS.json"),
        "failures": failures,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({k: output[k] for k in
                      ["status", "local_links_checked", "preservation_hash_checks", "failures"]}))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
