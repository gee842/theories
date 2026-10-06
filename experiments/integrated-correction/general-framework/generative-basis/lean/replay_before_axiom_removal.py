#!/usr/bin/env python3
"""Replay a pinned historical Lean check without modifying current artifacts.

The whole Lean subtree is copied. Outside sources are read through a temporary
repository view. Only whitelisted, inspected Lean checkers are accepted; their
output paths are inside that private copy. Original source pins are not relaxed.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time


CORE = Path(__file__).resolve().parent
REPO = CORE.parents[4]
CORE_REL = CORE.relative_to(REPO)
ARCHIVE = CORE / "verification-history/2026-10-06-before-axiom-removal"
MANIFEST_SHA256 = "269635cef5f1fab71dd4d375c4a4fa93bc9b33a41bbffc1656fca00b9a6d5764"
CHECKS = {
    "core": ("check.py", "verification.json"),
    "sufficiency": ("inquiry-root/sufficiency/check.py", "inquiry-root/sufficiency/verification.json"),
    "core-tree": ("inquiry-root/check_core_tree.py", "inquiry-root/core-tree-verification.json"),
    "receipts": ("learning/construction/prediction/check_receipt_lean.py",
                 "learning/construction/prediction/receipt-identification-verification.json"),
    "acquisition": ("acquired-perspective/check.py", "acquired-perspective/verification.json"),
    "connected": ("connected/check.py", "connected/verification.json"),
    "applicability": ("connected/applicability/check.py", "connected/applicability/verification.json"),
    "nondual": ("connected/nondual/check.py", "connected/nondual/verification.json"),
    "pretraining": ("connected/pretraining/check.py", "connected/pretraining/verification.json"),
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def copied_core_view(target):
    """Materialize the path to CORE, copy CORE, and link read-only siblings."""
    original, view = REPO, target
    view.mkdir()
    for part in CORE_REL.parts:
        for child in original.iterdir():
            if child.name != part and child.name != ".git":
                (view / child.name).symlink_to(child, target_is_directory=child.is_dir())
        original = original / part
        view = view / part
        if original == CORE:
            shutil.copytree(original, view, symlinks=False,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.olean",
                                                          "*.ilean", "legacy-replays"))
        else:
            view.mkdir()
    return view


def protected_hashes():
    return {str(p.relative_to(CORE)): sha(p.read_bytes())
            for p in CORE.rglob("*")
            if p.is_file() and p.suffix in {".lean", ".py", ".json", ".txt"}
            and "legacy-replays" not in p.relative_to(CORE).parts
            and "__pycache__" not in p.relative_to(CORE).parts}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("check", choices=CHECKS)
    args = parser.parse_args()
    manifest_bytes = (ARCHIVE / "manifest.json").read_bytes()
    assert sha(manifest_bytes) == MANIFEST_SHA256
    manifest = json.loads(manifest_bytes)
    for item in manifest["files"]:
        assert sha((ARCHIVE / item["snapshot"]).read_bytes()) == item["sha256"], item
    before = protected_hashes()
    run_dir = CORE / "legacy-replays" / (str(time.time_ns()) + "-" + args.check)
    run_dir.mkdir(parents=True)
    restored = []
    checker_name, receipt_name = CHECKS[args.check]
    with tempfile.TemporaryDirectory(prefix="generative-historical-replay-") as tmp:
        root = Path(tmp) / "repository"
        copied = copied_core_view(root)
        for item in manifest["files"]:
            origin = Path(item["origin"])
            if not origin.is_relative_to(CORE_REL):
                continue
            destination = root / origin
            assert destination.is_relative_to(copied)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes((ARCHIVE / item["snapshot"]).read_bytes())
            restored.append(item["origin"])
        checker = copied / checker_name
        (run_dir / "checker.py").write_bytes(checker.read_bytes())
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        command = [sys.executable, str(checker)]
        result = subprocess.run(command, cwd=root, env=env, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=900)
        (run_dir / "output.txt").write_text(result.stdout)
        produced = copied / receipt_name
        receipt = json.loads(produced.read_text()) if produced.is_file() else {}
        if produced.is_file():
            (run_dir / "receipt.json").write_bytes(produced.read_bytes())
        # Retain the actual compiler logs referenced by this replay's receipt.
        log_copies = []
        for module in receipt.get("modules", []):
            log = module.get("output") or module.get("log")
            if not log:
                continue
            path = produced.parent / log
            if path.is_file() and path.resolve().is_relative_to(copied.resolve()):
                dest = run_dir / "logs" / path.name
                dest.parent.mkdir(exist_ok=True)
                dest.write_bytes(path.read_bytes())
                expected_hash = module.get("output_sha256") or module.get("log_sha256")
                assert expected_hash and sha(dest.read_bytes()) == expected_hash, module.get("module")
                log_copies.append({"module": module.get("module"), "file": str(dest.relative_to(run_dir)),
                                   "sha256": sha(dest.read_bytes())})
    after = protected_hashes()
    unchanged = all(after.get(path) == digest for path, digest in before.items())
    logs_complete = (bool(receipt.get("modules")) and len(log_copies) == len(receipt["modules"]))
    passed = result.returncode == 0 and receipt.get("status") == "passed" and unchanged and logs_complete
    record = {"status": "passed" if passed else "failed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "historical_check": args.check, "archive_manifest_sha256": MANIFEST_SHA256,
              "restored_files": restored, "checker_sha256": sha((run_dir / "checker.py").read_bytes()),
              "exit_code": result.returncode, "historical_receipt_status": receipt.get("status"),
              "original_artifacts_unchanged": unchanged, "all_compiler_logs_preserved": logs_complete,
              "logs": log_copies,
              "scope": "Historical source replay only; current constructive receipts remain untouched. "
                       "Historical axioms remain recorded, and this is not a migration of the sibling theory."}
    (run_dir / "replay.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "historical_check": args.check,
                      "original_artifacts_unchanged": unchanged,
                      "record": str((run_dir / "replay.json").relative_to(REPO))}), flush=True)
    if not passed:
        print(result.stdout[-6000:])
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
