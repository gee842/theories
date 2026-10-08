#!/usr/bin/env python3
"""Check the generated-contraction pilot in isolation.

Only this document's scope is rechecked. Existing project build artifacts and
other sessions' receipts are not used or rewritten. Keep immutable source/log
snapshots and a receipt; disposable compiler products stay outside the repo.
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
MODULES = [
    (LEAN_ROOT / "GenerativeCore.lean", 18),
    (HERE / "GeneratedPaths.lean", 9),
    (HERE / "GeneratedContraction.lean", 14),
    (HERE / "ContractionMechanisms.lean", 24),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    out = HERE / "generated-contraction-checks" / stamp
    (out / "sources").mkdir(parents=True)
    toolchain = (LEAN_ROOT / "lean-toolchain").read_text().strip()
    env = dict(os.environ, ELAN_TOOLCHAIN=toolchain)
    lean = shutil.which("lean")
    if lean is None:
        raise SystemExit("Lean is required; no installation is performed.")
    version = subprocess.check_output([lean, "--version"], env=env, text=True).strip()
    receipt = {"checked_at_utc": stamp, "toolchain": toolchain,
               "compiler": version, "checker_sha256": sha(Path(__file__).read_bytes()),
               "scope": "four modules for GENERATED-LOGIC.md; no repository-wide validation",
               "modules": [], "passed": False}
    with tempfile.TemporaryDirectory(prefix="ren-generated-contraction-") as scratch:
        build = Path(scratch)
        env["LEAN_PATH"] = str(build)
        for source, expected in MODULES:
            raw = source.read_bytes()
            (out / "sources" / source.name).write_bytes(raw)
            copied = build / source.name
            copied.write_bytes(raw)
            if re.search(r"\b(sorry|admit|axiom)\b", raw.decode()):
                raise RuntimeError(f"Unexpected proof-hole/axiom token in {source.name}")
            proc = subprocess.run([lean, "-o", str(copied.with_suffix(".olean")), str(copied)],
                                  cwd=build, env=env, text=True, capture_output=True)
            log = proc.stdout + proc.stderr
            (out / (source.stem + ".log")).write_text(log)
            empty = re.findall(r"'([^']+)' does not depend on any axioms", log)
            dependent = re.findall(r"'([^']+)' depends on axioms: \[(.*?)\]", log, re.S)
            audits = {name: [] for name in empty}
            audits.update({name: [a.strip() for a in xs.split(",")] for name, xs in dependent})
            allowed = {"propext", "Quot.sound", "Classical.choice"}
            ok = (proc.returncode == 0 and len(audits) == expected
                  and "warning:" not in log and all(set(xs) <= allowed for xs in audits.values()))
            receipt["modules"].append({"source": str(source.relative_to(ROOT)),
                "sha256": sha(raw), "expected_audits": expected,
                "axiom_audits": audits, "empty_count": len(empty), "exit_code": proc.returncode,
                "source_unchanged_during_check": source.read_bytes() == raw,
                "passed": ok})
            if not ok:
                (out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
                raise SystemExit(log + f"\nCheck failed: {source.name}")
    receipt["passed"] = all(m["passed"] and m["source_unchanged_during_check"]
                            for m in receipt["modules"])
    receipt["total_empty_axiom_audits"] = sum(m["empty_count"]
                                              for m in receipt["modules"])
    (out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    (HERE / "generated-contraction-verification.json").write_text(json.dumps({
        "receipt": str((out / "receipt.json").relative_to(ROOT)),
        "passed": receipt["passed"],
        "total_empty_axiom_audits": receipt["total_empty_axiom_audits"],
    }, indent=2) + "\n")
    print(json.dumps({"passed": receipt["passed"], "modules": len(MODULES),
                      "empty_audits": receipt["total_empty_axiom_audits"], "total_audits": sum(len(m["axiom_audits"]) for m in receipt["modules"]),
                      "receipt": str(out / "receipt.json")}))
    if not receipt["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
