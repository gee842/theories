#!/usr/bin/env python3
"""Reconcile this round's saved proofs, preservation evidence and owned links.

This does not recompile Lean or rerun a scientific experiment. Compilation is
recorded in the separately preserved fresh-build receipts.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
CORE = REPO / "experiments/integrated-correction/general-framework/generative-basis/lean"
SUFF = CORE / "inquiry-root/sufficiency"
checks = []


def hashed(path, expected):
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    assert actual == expected, path
    checks.append({"path": str(path), "sha256": actual})


def anchors(text):
    result, used = set(), {}
    for title in re.findall(r"^#{1,6}\s+(.+)$", text, re.M):
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        index = used.get(slug, 0)
        used[slug] = index + 1
        result.add(slug + (f"-{index}" if index else ""))
    return result


def main():
    for receipt_path, checker, source_root, module_count, audit_count in [
        (CORE / "verification.json", CORE / "check.py", CORE, 16, 195),
        (SUFF / "verification.json", SUFF / "check.py", REPO, 18, 212),
        (SUFF / "finite-verification.json", SUFF / "check_finite.py", REPO, 20, 227),
    ]:
        receipt = json.loads(receipt_path.read_text())
        assert receipt["status"] == "passed" and receipt["whole_current_audited_closure_empty"]
        assert len(receipt["modules"]) == module_count
        assert sum(len(m["axioms_by_declaration"]) for m in receipt["modules"]) == audit_count
        hashed(checker, receipt["checker_sha256"])
        for module in receipt["modules"]:
            assert all(not deps for deps in module["axioms_by_declaration"].values())
            hashed(source_root / module["source"], module["source_sha256"])
            hashed(receipt_path.parent / module["source_snapshot"], module["source_sha256"])
            log = module.get("output") or module["log"]
            hashed(receipt_path.parent / log, module.get("output_sha256") or module["log_sha256"])
        if "baseline" in receipt:
            assert "/runs/" in receipt["baseline"] or "/verification-runs/" in receipt["baseline"]
            hashed(REPO / receipt["baseline"], receipt["baseline_sha256"])
            hashed(receipt_path.parent / receipt["baseline_snapshot"], receipt["baseline_sha256"])
    archive = CORE / "verification-history/2026-10-06-before-axiom-removal"
    hashed(archive / "manifest.json", "269635cef5f1fab71dd4d375c4a4fa93bc9b33a41bbffc1656fca00b9a6d5764")
    manifest = json.loads((archive / "manifest.json").read_text())
    assert len(manifest["files"]) == 60
    for entry in manifest["files"]:
        hashed(archive / entry["snapshot"], entry["sha256"])

    replay_dir = CORE / "legacy-replays/1791275071482105000-core-tree"
    replay = json.loads((replay_dir / "replay.json").read_text())
    assert replay["status"] == "passed" and replay["original_artifacts_unchanged"]
    assert replay["all_compiler_logs_preserved"] and len(replay["logs"]) == 31
    historical = json.loads((replay_dir / "receipt.json").read_text())
    assert historical["status"] == "passed" and historical["audits"] == 400
    assert len(historical["modules"]) == 31
    for item in replay["logs"]:
        hashed(replay_dir / item["file"], item["sha256"])

    edits = json.loads((HERE / "CONSTRUCTIVE-DEPENDENCY-REMOVAL-EDITS.json").read_text())["edits"]
    fragments = []
    for edit in edits:
        path = REPO / edit["path"]
        fragment = edit["new"]
        # Concurrent studies may insert their own lead after the shared title.
        # Check our whole substantive insertion independently of that anchor.
        if re.fullmatch(r"# [^\n]+\n\n", edit["old"]) and fragment.startswith(edit["old"]):
            fragment = fragment[len(edit["old"]):]
        assert fragment in path.read_text(), (path, "Owned fragment changed")
        fragments.append((path, fragment))
    for name in ["CONSTRUCTIVE-DEPENDENCY-REMOVAL-INTEGRATION.md", "CONSTRUCTIVE-DEPENDENCY-REMOVAL-REVIEW.md"]:
        path = HERE / name
        fragments.append((path, path.read_text()))
    links = []
    for path, text in fragments:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"[a-zA-Z]+:", target):
                continue
            file, _, anchor = unquote(target).partition("#")
            resolved = (path.parent / file).resolve() if file else path
            assert resolved.exists(), (path, target)
            if anchor and resolved.suffix == ".md":
                assert anchor in anchors(resolved.read_text()), (path, target, "Missing anchor")
            links.append({"from": str(path.relative_to(REPO)), "target": target})
    result = {"status": "passed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "scope": "Saved-evidence and owned-document reconciliation, not a new compiler or scientific run.",
              "current_builds": [[16, 195], [18, 212], [20, 227]],
              "every_current_audited_dependency_empty": True, "archive_files": 60,
              "historical_replay": {"modules": 31, "audits": 400, "logs_preserved": 31},
              "owned_fragments": len(edits), "links_checked": len(links),
              "hash_comparisons": len(checks), "hashes": checks, "links": links}
    (HERE / "CONSTRUCTIVE-DEPENDENCY-REMOVAL-CHECKS.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k not in {"hashes", "links"}}))


if __name__ == "__main__":
    main()
