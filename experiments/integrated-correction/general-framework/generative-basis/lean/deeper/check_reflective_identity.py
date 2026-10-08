#!/usr/bin/env python3
"""Isolated, source-bound check of the reflective identity audit."""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "RESEARCH.md").is_file())


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    out = HERE / "reflective-identity-checks" / stamp
    out.mkdir(parents=True)
    source = HERE / "ReflectiveIdentity.lean"
    raw = source.read_bytes()
    assert not re.search(r"\b(sorry|admit|axiom)\b", raw.decode())
    snapshot = out / source.name
    snapshot.write_bytes(raw)
    toolchain = (HERE.parent / "lean-toolchain").read_text().strip()
    env = dict(os.environ, ELAN_TOOLCHAIN=toolchain)
    lean = shutil.which("lean")
    if lean is None:
        raise SystemExit("Lean is required; no installation is performed.")
    version = subprocess.check_output([lean, "--version"], env=env, text=True).strip()
    with tempfile.TemporaryDirectory(prefix="ren-reflective-identity-") as scratch:
        build = Path(scratch)
        copied = build / source.name
        copied.write_bytes(raw)
        env["LEAN_PATH"] = str(build)
        result = subprocess.run([lean, "-o", str(copied.with_suffix(".olean")), str(copied)],
                                cwd=build, env=env, text=True, capture_output=True)
    log = result.stdout + result.stderr
    logpath = out / "ReflectiveIdentity.log"
    logpath.write_text(log)
    audits = re.findall(r"'([^']+)' does not depend on any axioms", log)
    passed = (result.returncode == 0 and len(audits) == 11 and
              "warning:" not in log and "depends on axioms" not in log and
              source.read_bytes() == raw)
    receipt = {"passed": passed, "checked_at_utc": stamp, "toolchain": toolchain,
               "compiler": version, "source": str(source.relative_to(ROOT)),
               "source_sha256": sha(raw), "snapshot": str(snapshot.relative_to(ROOT)),
               "log": str(logpath.relative_to(ROOT)), "log_sha256": sha(log.encode()),
               "checker": str(Path(__file__).relative_to(ROOT)),
               "checker_sha256": sha(Path(__file__).read_bytes()),
               "source_unchanged_during_check": source.read_bytes() == raw,
               "exit_code": result.returncode, "new_theorems": 11,
               "empty_axiom_audits": audits,
               "scope": "One new module, Std only; eleven theorems audited. No ultimate grounding claim."}
    receipt_path = out / "receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    if not passed:
        raise SystemExit(log + "\nReflective identity check failed.")
    pointer = {"passed": passed, "receipt": str(receipt_path.relative_to(ROOT)),
               "new_theorems": 11, "empty_axiom_audits": 11}
    (HERE / "reflective-identity-verification.json").write_text(json.dumps(pointer, indent=2) + "\n")
    print(json.dumps(pointer))


if __name__ == "__main__":
    main()
