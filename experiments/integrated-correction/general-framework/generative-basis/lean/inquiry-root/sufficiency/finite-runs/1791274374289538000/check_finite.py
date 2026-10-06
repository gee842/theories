#!/usr/bin/env python3
"""Fresh, scoped finite-classification proof check; no default receipt mutation."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time

HERE = Path(__file__).resolve().parent
CORE = HERE.parents[1]
REPO = next(p for p in HERE.parents if (p / "AGENTS.md").is_file())
COMPILER = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
COMPILER_SHA256 = "b48bc5ab229bd8b320a224b87e20fc428dba6fa8a1c054bd4fa6def846e19997"
TOOLCHAIN_SHA256 = "7dc000621e0046d1aada809e2b7177e64454645cf4c741e9daaf79c99ec2e7a2"
SOURCES = {
    "GenerativeCore": CORE / "GenerativeCore.lean",
    "InquirySufficiency": HERE / "InquirySufficiency.lean",
    "FiniteInquiryClassification": HERE / "FiniteInquiryClassification.lean",
}
ANCESTOR_SHA256 = {
    "GenerativeCore": "e3daca1b729118fc309585a5d3ba1af60ac99cd80bab41e477aed204177069e8",
    "InquirySufficiency": "d4a95ca842f46ffa9c23eea92d04cdb45027dc6842148d3d0bdc17cd65ad18f2",
}
IMPORTS = {"GenerativeCore": ["Std"], "InquirySufficiency": ["GenerativeCore"],
           "FiniteInquiryClassification": ["InquirySufficiency"]}
COUNTS = {"GenerativeCore": 18, "InquirySufficiency": 17, "FiniteInquiryClassification": 13}
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    checker = Path(__file__).read_bytes()
    toolchain = (CORE / "lean-toolchain").read_bytes()
    frozen = {name: path.read_bytes() for name, path in SOURCES.items()}
    assert sha(COMPILER.read_bytes()) == COMPILER_SHA256
    assert sha(toolchain) == TOOLCHAIN_SHA256
    for name, expected in ANCESTOR_SHA256.items():
        assert sha(frozen[name]) == expected, f"Review changed inherited source: {name}"
    requests = {}
    for name, data in frozen.items():
        source = data.decode()
        assert re.findall(r"^import\s+(\S+)\s*$", source, re.M) == IMPORTS[name]
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", source)
        assert not re.search(r"^\s*(axiom|constant|opaque)\s", source, re.M)
        requests[name] = re.findall(r"^#print axioms (\S+)\s*$", source, re.M)
        assert len(requests[name]) == len(set(requests[name])) == COUNTS[name]
    new_source = frozen["FiniteInquiryClassification"].decode()
    theorem_names = set(re.findall(r"^theorem\s+(\w+)", new_source, re.M))
    audited_names = {decl.rsplit(".", 1)[-1] for decl in requests["FiniteInquiryClassification"]}
    assert len(theorem_names) == 11
    assert audited_names == theorem_names | {"beliefDecision", "afterMembership"}
    version = subprocess.check_output([str(COMPILER), "--version"], text=True).strip()
    attempt = HERE / "finite-runs" / str(time.time_ns())
    (attempt / "sources").mkdir(parents=True)
    (attempt / "check_finite.py").write_bytes(checker)
    (attempt / "lean-toolchain").write_bytes(toolchain)
    for name, data in frozen.items():
        (attempt / "sources" / f"{name}.lean").write_bytes(data)
    rows = []
    with tempfile.TemporaryDirectory(prefix="finite-inquiry-fresh-") as temporary:
        build = Path(temporary)
        for name, data in frozen.items():
            (build / f"{name}.lean").write_bytes(data)
        for name in SOURCES:
            command = [str(COMPILER), "-o", f"{name}.olean", f"{name}.lean"]
            result = subprocess.run(command, cwd=build, env=dict(os.environ, LEAN_PATH=str(build)),
                                    text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)
            log = attempt / f"{name}.txt"
            log.write_text(result.stdout)
            audits = [(decl, sorted(a.strip() for a in deps.split(",") if a.strip()))
                      for decl, deps in AUDIT.findall(result.stdout)]
            complete = [decl for decl, _ in audits] == requests[name]
            passed = (result.returncode == 0 and "warning:" not in result.stdout and complete
                      and all(not deps for _, deps in audits))
            rows.append({"module": name, "source": str(SOURCES[name].relative_to(REPO)),
                         "source_sha256": sha(frozen[name]),
                         "source_snapshot": str((attempt / "sources" / f"{name}.lean").relative_to(HERE)),
                         "command": command, "exit_code": result.returncode,
                         "audit_complete": complete, "axioms_by_declaration": dict(audits),
                         "log": str(log.relative_to(HERE)), "log_sha256": sha(log.read_bytes()),
                         "passed": passed})
            print(json.dumps({"module": name, "passed": passed, "audits": len(audits)}), flush=True)
            if not passed:
                print(result.stdout, flush=True)
                break
    unchanged = (all(path.read_bytes() == frozen[name] for name, path in SOURCES.items()) and
                 Path(__file__).read_bytes() == checker and (CORE / "lean-toolchain").read_bytes() == toolchain)
    passed = len(rows) == 3 and unchanged and all(row["passed"] for row in rows)
    record = {
        "status": "passed" if passed else "failed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "lean_version": version, "compiler": str(COMPILER), "compiler_sha256": COMPILER_SHA256,
        "toolchain_sha256": TOOLCHAIN_SHA256, "checker_sha256": sha(checker),
        "fresh_temporary_build": True, "local_precompiled_imports_used": False,
        "default_receipt_overwritten": False, "inputs_unchanged": unchanged,
        "modules": rows, "audits": sum(len(row["axioms_by_declaration"]) for row in rows),
        "new_audits": len(rows[-1]["axioms_by_declaration"]) if len(rows) == 3 else 0,
        "axiom_dependencies": sorted({a for row in rows for deps in row["axioms_by_declaration"].values() for a in deps}),
        "scope": "Exact successor enumeration and branch classification for an unchanged Process on Fin N "
                 "with executable transition and membership decisions. The Boolean-initial policy theorem "
                 "requires neither a classification certificate nor a supplied exact enumeration. "
                 "No new event law, action search, installed planner, or full-model foundation completion. "
                 "This three-module receipt is not the separate public-model dependency audit."
    }
    (attempt / "receipt.json").write_text(json.dumps(record, indent=2) + "\n")
    if passed:
        (HERE / "finite-verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "modules": len(rows), "audits": record["audits"],
                      "new_audits": record["new_audits"], "receipt": str(attempt.relative_to(REPO))}), flush=True)
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
