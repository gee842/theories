#!/usr/bin/env python3
"""Check conditional-law modules in a fresh directory from frozen source bytes."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
MODULES = ["GenerativeCore", "ResourceContinuation", "RenewalExamples", "SupportNecessity"]
SOURCES = {name: (ROOT.parent if name == "GenerativeCore" else ROOT) /
           (name + ".lean") for name in MODULES}
ALLOWED_AXIOMS = set()  # every audit must be empty (Ren, 6 October 2026: no axioms)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=180)


def main():
    toolchain = (ROOT / "lean-toolchain").read_text().strip()
    assert toolchain == "leanprover/lean4:v4.29.1"
    prefix = ["lean", "+" + toolchain]
    try:
        version = run(prefix + ["--version"], ROOT)
    except FileNotFoundError:
        version = None
    if version is None or version.returncode:
        # Without elan, accept a Lean 4.29.1 on PATH; the version is asserted below.
        prefix = ["lean"]
        version = run(prefix + ["--version"], ROOT)
    version.check_returncode()
    assert "version 4.29.1," in version.stdout
    compiler_prefix = run(prefix + ["--print-prefix"], ROOT)
    compiler_prefix.check_returncode()
    compiler = Path(compiler_prefix.stdout.strip()) / "bin" / "lean"
    frozen = {name: path.read_bytes() for name, path in SOURCES.items()}
    for name, source in frozen.items():
        text = source.decode()
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", text), name
        assert not re.search(r"^\s*(axiom|constant)\s", text, re.M), name
        imports = re.findall(r"^import\s+(.+)$", text, re.M)
        assert all(item in {"Std", "GenerativeCore", "ResourceContinuation"}
                   for item in imports), imports
        requested = re.findall(r"^#print axioms (\S+)", text, re.M)
        theorems = re.findall(r"^theorem\s+(\w+)", text, re.M)
        # The inherited core retains its earlier selected audit contract; every
        # newly introduced theorem must appear in this package's audit list.
        if name != "GenerativeCore":
            assert set(theorems) == {item.rsplit(".", 1)[-1] for item in requested}, name
    results = []
    output_dir = ROOT / "verification"
    output_dir.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="generative-conditional-lean-") as temporary:
        build = Path(temporary)
        for name, source in frozen.items():
            (build / (name + ".lean")).write_bytes(source)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in MODULES:
            result = run([str(compiler), "-o", name + ".olean", name + ".lean"], build, env)
            log = output_dir / (name + ".txt")
            log.write_text(result.stdout)
            audits = re.findall(
                r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
                result.stdout)
            requested = re.findall(r"^#print axioms (\S+)", frozen[name].decode(), re.M)
            names = [theorem for theorem, _ in audits]
            matched = len(names) == len(requested) and all(
                actual == wanted or actual.endswith("." + wanted)
                for actual, wanted in zip(names, requested))
            axioms = sorted({a.strip() for _, group in audits
                             for a in group.split(",") if a.strip()})
            clean = ("sorryAx" not in result.stdout and "warning:" not in result.stdout
                     and matched and bool(audits) and set(axioms) <= ALLOWED_AXIOMS)
            results.append({
                "module": name, "source": os.path.relpath(SOURCES[name], ROOT),
                "source_sha256": digest(frozen[name]), "exit_code": result.returncode,
                "dependency_audits": len(audits), "audited_declarations": names,
                "requested_audits": requested, "axioms": axioms,
                "empty_axiom_audits": sum(not group.strip() for _, group in audits),
                "clean_dependency_audit": clean,
                "output": "verification/" + log.name,
                "output_sha256": digest(log.read_bytes()),
            })
            if result.returncode or not clean:
                break
    unchanged = all(path.read_bytes() == frozen[name] for name, path in SOURCES.items())
    passed = (len(results) == len(MODULES) and unchanged and
              all(r["exit_code"] == 0 and r["clean_dependency_audit"] for r in results))
    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if passed else "failed", "lean_version": version.stdout.strip(),
        "compiler_binary": str(compiler), "compiler_sha256": digest(compiler.read_bytes()),
        "toolchain": toolchain, "toolchain_sha256": digest((ROOT / "lean-toolchain").read_bytes()),
        "checker_sha256": digest(Path(__file__).read_bytes()),
        "source_unchanged_during_check": unchanged, "fresh_temporary_build": True,
        "allowed_standard_axioms": sorted(ALLOWED_AXIOMS), "modules": results,
        "audited_declarations": sum(r["dependency_audits"] for r in results),
        "new_audited_declarations": sum(r["dependency_audits"] for r in results
                                        if r["module"] != "GenerativeCore"),
        "new_empty_axiom_audits": sum(r["empty_axiom_audits"] for r in results
                                      if r["module"] != "GenerativeCore"),
        "scope": "Universal conditional statements over supplied discrete process laws: "
                 "actual-history nonnegative support accounting, finite reserve and cost bounds, "
                 "unbounded demand implies unbounded credit, positive-unit credit recurrence, "
                 "bounded-credit event frequency, transfer by forward simulation, componentwise "
                 "accounts, and conditional lifetime/dependency constraints. Constructive "
                 "realizations and countermodels delimit sufficiency and missing hypotheses. "
                 "No identification of a real-world account, universal welfare scalar, inevitable "
                 "renewal, learning, concern, or uniquely necessary ontology is asserted.",
    }
    (ROOT / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "modules": len(results),
                      "new_audited_declarations": record["new_audited_declarations"],
                      "new_empty_axiom_audits": record["new_empty_axiom_audits"],
                      "record": str(ROOT / "verification.json")}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
