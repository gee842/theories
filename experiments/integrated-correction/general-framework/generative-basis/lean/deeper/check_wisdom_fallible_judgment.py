#!/usr/bin/env python3
"""Check the fallible-wisdom companion and direct imports in isolation.

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
    (HERE / "CorePredication.lean", 12),
    (HERE / "ContextualWisdom.lean", 11),
    (HERE / "WisdomResponseStructure.lean", 9),
    (HERE / "WisdomFallibleJudgment.lean", 5),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    out = HERE / "wisdom-fallible-judgment-checks" / stamp
    (out / "sources").mkdir(parents=True)
    (out / "sources" / Path(__file__).name).write_bytes(Path(__file__).read_bytes())
    toolchain = (LEAN_ROOT / "lean-toolchain").read_text().strip()
    env = dict(os.environ, ELAN_TOOLCHAIN=toolchain)
    lean = shutil.which("lean")
    if lean is None:
        raise SystemExit("Lean is required; no installation is performed.")
    version = subprocess.check_output([lean, "--version"], env=env, text=True).strip()
    receipt = {"checked_at_utc": stamp, "toolchain": toolchain,
               "compiler": version, "checker_sha256": sha(Path(__file__).read_bytes()),
               "scope": "five claim-relative risk/application theorems and 59 inherited import audits; no repository-wide validation",
               "modules": [], "passed": False}
    with tempfile.TemporaryDirectory(prefix="ren-wisdom-fallible-judgment-") as scratch:
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
            audits = re.findall(r"'([^']+)' does not depend on any axioms", log)
            dependencies = {name: [x.strip() for x in body.split(',') if x.strip()]
                            for name, body in re.findall(
                                r"'([^']+)' depends on axioms: \[([^\]]*)\]", log)}
            declared = re.findall(r"^#print axioms (\S+)", raw.decode(), re.M)
            reported = audits + list(dependencies)
            standard = {"propext", "Quot.sound", "Classical.choice"}
            ok = (proc.returncode == 0 and len(reported) == expected
                  and sorted(reported) == sorted(declared)
                  and all(set(ds) <= standard for ds in dependencies.values())
                  and "warning:" not in log and "sorryAx" not in log)
            receipt["modules"].append({"source": str(source.relative_to(ROOT)),
                "sha256": sha(raw), "expected_audits": expected,
                "empty_axiom_audits": audits, "standard_dependency_audits": dependencies,
                "exit_code": proc.returncode,
                "source_unchanged_during_check": source.read_bytes() == raw,
                "passed": ok})
            if not ok:
                (out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
                raise SystemExit(log + f"\nCheck failed: {source.name}")
    receipt["passed"] = all(m["passed"] and m["source_unchanged_during_check"]
                            for m in receipt["modules"])
    receipt["total_empty_axiom_audits"] = sum(len(m["empty_axiom_audits"])
                                              for m in receipt["modules"])
    receipt["total_audits"] = sum(m["expected_audits"] for m in receipt["modules"])
    receipt["total_standard_dependency_audits"] = sum(
        len(m["standard_dependency_audits"]) for m in receipt["modules"])
    (out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    (HERE / "wisdom-fallible-judgment-verification.json").write_text(json.dumps({
        "receipt": str((out / "receipt.json").relative_to(ROOT)),
        "passed": receipt["passed"],
        "total_audits": receipt["total_audits"],
        "total_empty_axiom_audits": receipt["total_empty_axiom_audits"],
    }, indent=2) + "\n")
    print(json.dumps({"passed": receipt["passed"], "modules": len(MODULES),
                      "audits": receipt["total_audits"],
                      "empty": receipt["total_empty_axiom_audits"],
                      "receipt": str(out / "receipt.json")}))
    if not receipt["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
