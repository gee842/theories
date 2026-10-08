#!/usr/bin/env python3
"""Compile the formation-profile-gap audit in isolation; retain exact sources/logs.

Empty reported axiom dependencies concern the checked Lean declarations, not
their logical foundation, hypotheses, definitions or application to reality.
"""
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
LEAN_ROOT = HERE.parent
ROOT = next(p for p in HERE.parents if (p / "RESEARCH.md").is_file())
MODULES = [(LEAN_ROOT / "GenerativeCore.lean", 18),
           (HERE / "HistoryRealization.lean", 7),
           (HERE / "ContinuationConditions.lean", 18),
           (HERE / "SystemIndividuation.lean", 0),
           (HERE / "RelationalFormation.lean", 31),
           (HERE / "FormationProfileGap.lean", 13)]


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    out = HERE / "formation-profile-gap-checks" / stamp
    (out / "sources").mkdir(parents=True)
    env = dict(os.environ, ELAN_TOOLCHAIN=(LEAN_ROOT / "lean-toolchain").read_text().strip())
    lean = shutil.which("lean")
    if lean is None:
        raise SystemExit("Lean is required; no installation is performed.")
    compiler = subprocess.check_output([lean, "--version"], env=env, text=True).strip()
    receipt = {"checked_at_utc": stamp, "toolchain": env["ELAN_TOOLCHAIN"],
               "compiler": compiler, "checker_sha256": sha(Path(__file__).read_bytes()),
               "scope": "FormationProfileGap; 9 new theorem audits, 43 inherited core/history/continuation audits, 31 inherited relational-formation audits and 4 selected native declarations. SystemIndividuation is compiled unchanged; its other declarations are not separately audited here.",
               "modules": [], "passed": False}
    with tempfile.TemporaryDirectory(prefix="ren-formation-profile-gap-") as scratch:
        build = Path(scratch)
        env["LEAN_PATH"] = str(build)
        for source, expected in MODULES:
            raw = source.read_bytes()
            snapshot = out / "sources" / source.name
            snapshot.write_bytes(raw)
            copied = build / source.name
            copied.write_bytes(raw)
            code = re.sub(r"/\*.*?\*/", "", raw.decode(), flags=re.S)
            code = re.sub(r"/-.*?-/", "", code, flags=re.S)
            code = re.sub(r"--[^\n]*", "", code)
            if re.search(r"\b(sorry|admit|axiom)\b", code):
                raise RuntimeError(f"Unexpected proof-hole/axiom token in {source.name}")
            proc = subprocess.run([lean, "-o", str(copied.with_suffix(".olean")), str(copied)],
                                  cwd=build, env=env, text=True, capture_output=True)
            log = proc.stdout + proc.stderr
            logpath = out / (source.stem + ".log")
            logpath.write_text(log)
            audits = re.findall(r"'([^']+)' does not depend on any axioms", log)
            ok = (proc.returncode == 0 and len(audits) == expected
                  and "warning:" not in log and "depends on axioms" not in log)
            receipt["modules"].append({"source": str(source.relative_to(ROOT)),
                "sha256": sha(raw), "snapshot": str(snapshot.relative_to(ROOT)),
                "log": str(logpath.relative_to(ROOT)), "log_sha256": sha(log.encode()),
                "expected_audits": expected, "empty_axiom_audits": audits,
                "exit_code": proc.returncode,
                "source_unchanged_during_check": source.read_bytes() == raw, "passed": ok})
            if not ok:
                (out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
                raise SystemExit(log + f"\nCheck failed: {source.name}")
    receipt["passed"] = all(m["passed"] and m["source_unchanged_during_check"]
                            for m in receipt["modules"])
    receipt["total_empty_axiom_audits"] = sum(len(m["empty_axiom_audits"])
                                              for m in receipt["modules"])
    (out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    pointer = {"receipt": str((out / "receipt.json").relative_to(ROOT)),
               "passed": receipt["passed"],
               "total_empty_axiom_audits": receipt["total_empty_axiom_audits"]}
    (HERE / "formation-profile-gap-verification.json").write_text(json.dumps(pointer, indent=2) + "\n")
    print(json.dumps(pointer))
    if not receipt["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
