#!/usr/bin/env python3
"""Fresh-build the inquiry closure and its recorded root dependencies."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
MODULES = ["GenerativeCore", "Depletion", "GenerativeClosure", "InquiryFamilies"]
INHERITED = {"GenerativeCore", "Depletion"}
SOURCES = {name: (ROOT.parent if name in INHERITED else ROOT) / (name + ".lean")
           for name in MODULES}
ALLOWED_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)


def main():
    toolchain = (ROOT / "lean-toolchain").read_text().strip()
    assert toolchain == "leanprover/lean4:v4.29.1"
    prefix = ["lean", "+" + toolchain]
    version = run(prefix + ["--version"], ROOT)
    version.check_returncode()
    assert "version 4.29.1," in version.stdout
    located = run(prefix + ["--print-prefix"], ROOT)
    located.check_returncode()
    compiler = Path(located.stdout.strip()) / "bin" / "lean"
    frozen = {name: path.read_bytes() for name, path in SOURCES.items()}
    for name, source in frozen.items():
        text = source.decode()
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", text), name
        assert not re.search(r"^\s*(axiom|constant)\s", text, re.M), name
        imports = re.findall(r"^import\s+(.+)$", text, re.M)
        assert all(item in {"Std", *MODULES} for item in imports), imports
    results = []
    output = ROOT / "verification"
    output.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="inquiry-root-lean-") as temporary:
        build = Path(temporary)
        for name, source in frozen.items():
            (build / (name + ".lean")).write_bytes(source)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in MODULES:
            result = run([str(compiler), "-o", name + ".olean", name + ".lean"], build, env)
            log = output / (name + ".txt")
            log.write_text(result.stdout)
            audits = re.findall(
                r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
                result.stdout)
            declared = re.findall(r"^#print axioms (\S+)", frozen[name].decode(), re.M)
            axioms = sorted({a.strip() for _, group in audits for a in group.split(",")
                             if a.strip()})
            names_match = ([x.rsplit(".", 1)[-1] for x, _ in audits] ==
                           [x.rsplit(".", 1)[-1] for x in declared])
            clean = ("warning:" not in result.stdout and bool(audits) and names_match
                     and set(axioms) <= ALLOWED_AXIOMS)
            results.append({
                "module": name, "inherited": name in INHERITED,
                "source": os.path.relpath(SOURCES[name], ROOT),
                "source_sha256": digest(frozen[name]), "exit_code": result.returncode,
                "audited_declarations": [x for x, _ in audits], "axioms": axioms,
                "clean_dependency_audit": clean,
                "output": "verification/" + log.name,
                "output_sha256": digest(log.read_bytes())})
            if result.returncode or not clean:
                break
    unchanged = all(path.read_bytes() == frozen[name] for name, path in SOURCES.items())
    passed = len(results) == len(MODULES) and unchanged and all(
        r["exit_code"] == 0 and r["clean_dependency_audit"] for r in results)
    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if passed else "failed", "lean_version": version.stdout.strip(),
        "compiler_binary": str(compiler), "compiler_sha256": digest(compiler.read_bytes()),
        "toolchain": toolchain, "toolchain_sha256": digest((ROOT / "lean-toolchain").read_bytes()),
        "checker_sha256": digest(Path(__file__).read_bytes()),
        "fresh_temporary_build": True, "source_unchanged_during_check": unchanged,
        "modules": results,
        "new_audited_declarations": sum(len(r["audited_declarations"]) for r in results
                                        if not r["inherited"]),
        "inherited_audited_declarations": sum(len(r["audited_declarations"]) for r in results
                                              if r["inherited"]),
        "scope": "Necessity preservation for all finite premise-tracked derivations; "
                 "exact clipped-observation threshold family; actual inherited spending "
                 "traces and finite reserve exclusions; concrete local-basis composition. "
                 "No proof of necessity of the full proposed ontology or of empirical or "
                 "ethical premises, physical infinite computation, or complete wisdom."}
    (ROOT / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "new": record["new_audited_declarations"],
                      "inherited": record["inherited_audited_declarations"],
                      "last_module": results[-1]["module"]}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
