#!/usr/bin/env python3
"""Fresh pinned Lean check of the rational offered-choice identification bound."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
MODULES = ["OfferedChoiceBounds"]
ALLOWED_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def without_comments(text):
    """Remove nested Lean comments while preserving line boundaries and strings."""
    output, index, depth, quoted = [], 0, 0, False
    while index < len(text):
        pair = text[index:index + 2]
        char = text[index]
        if depth:
            if pair == "/-":
                depth += 1
                index += 2
            elif pair == "-/":
                depth -= 1
                index += 2
            else:
                output.append("\n" if char == "\n" else " ")
                index += 1
        elif quoted:
            output.append(char)
            index += 1
            if char == "\\" and index < len(text):
                output.append(text[index])
                index += 1
            elif char == '"':
                quoted = False
        elif pair == "/-":
            output.append(" ")
            depth = 1
            index += 2
        elif pair == "--":
            end = text.find("\n", index)
            index = len(text) if end < 0 else end
        else:
            output.append(char)
            quoted = char == '"'
            index += 1
    assert depth == 0 and not quoted, "Unclosed Lean comment/string"
    return "".join(output)


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)

def main():
    toolchain_bytes = (ROOT / "lean-toolchain").read_bytes()
    toolchain = toolchain_bytes.decode().strip()
    assert toolchain == "leanprover/lean4:v4.29.1"
    prefix = ["lean", "+" + toolchain]
    version = run(prefix + ["--version"], ROOT)
    version.check_returncode()
    assert "version 4.29.1," in version.stdout
    location = run(prefix + ["--print-prefix"], ROOT)
    location.check_returncode()
    compiler = Path(location.stdout.strip()) / "bin/lean"
    frozen = {name: (ROOT / (name + ".lean")).read_bytes() for name in MODULES}
    checker_bytes = Path(__file__).read_bytes()
    contract_bytes = (ROOT / "development/contract.json").read_bytes()
    attempt = ROOT / "development" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    attempt.mkdir()
    (attempt / "checker.py").write_bytes(checker_bytes)
    for name, data in frozen.items():
        (attempt / (name + ".lean")).write_bytes(data)
    results = []
    with tempfile.TemporaryDirectory(prefix="offered-choice-lean-") as directory:
        build = Path(directory)
        for name, data in frozen.items():
            (build / (name + ".lean")).write_bytes(data)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name, data in frozen.items():
            text = without_comments(data.decode())
            assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", text), name
            assert not re.search(r"^\s*(axiom|constant)\s", text, re.M), name
            assert all(item in {"Std", *MODULES}
                       for item in re.findall(r"^import\s+(.+)$", text, re.M)), name
            declarations = re.findall(r"^theorem\s+(\w+)", text, re.M)
            requested = re.findall(r"^#print axioms (\S+)", text, re.M)
            assert len(declarations) == len(set(declarations)), name
            assert len(requested) == len(declarations), name
            assert set(declarations) == {r.rsplit(".", 1)[-1] for r in requested}, name
            command = [str(compiler), "-o", name + ".olean", name + ".lean"]
            outcome = run(command, build, env)
            log = attempt / (name + ".txt")
            log.write_text(outcome.stdout)
            audits = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", outcome.stdout)
            names = [n for n, _ in audits]
            axioms = sorted({a.strip() for _, group in audits for a in group.split(",") if a.strip()})
            clean = (outcome.returncode == 0 and names == requested and bool(audits)
                     and set(axioms) <= ALLOWED_AXIOMS and "sorryAx" not in outcome.stdout
                     and "warning:" not in outcome.stdout)
            results.append({"module":name, "source_sha256":digest(data), "exit_code":outcome.returncode,
                "audited_declarations": names, "axioms": axioms, "empty_axiom_audits":sum(not g.strip() for _,g in audits),
                "clean_dependency_audit":clean, "log":log.relative_to(ROOT).as_posix(),
                "log_sha256":digest(log.read_bytes()), "command":command})
            if not clean:
                break
    unchanged = all((ROOT / (name + ".lean")).read_bytes() == data for name, data in frozen.items())
    unchanged = unchanged and Path(__file__).read_bytes() == checker_bytes
    passed = len(results) == len(MODULES) and unchanged and all(r["clean_dependency_audit"] for r in results)
    report = {"checked_at_utc":datetime.now(timezone.utc).isoformat(), "status":"passed" if passed else "failed",
        "lean_version":version.stdout.strip(), "compiler_binary":str(compiler), "compiler_sha256":digest(compiler.read_bytes()),
        "toolchain":toolchain, "toolchain_sha256":digest(toolchain_bytes), "checker_sha256":digest(checker_bytes),
        "prospective_contract_sha256":digest(contract_bytes), "fresh_temporary_build":True,
        "source_unchanged_during_check":unchanged, "new_theorem_audits":sum(len(r["audited_declarations"]) for r in results),
        "empty_axiom_audits":sum(r["empty_axiom_audits"] for r in results),
        "allowed_standard_axioms":sorted(ALLOWED_AXIOMS), "modules":results,
        "scope":"Finite rational paired population, conditional probability-gap and coverage premises, exact signed offered-choice frontier. Real logistic interpretation, empirical calibration and ethical conclusions are separate.",
        "preserved_attempt":attempt.relative_to(ROOT).as_posix()}
    (attempt / "audit.json").write_text(json.dumps(report,indent=2)+"\n")
    (ROOT / "verification.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({"status":report["status"],"new_theorem_audits":report["new_theorem_audits"],"attempt":report["preserved_attempt"]},indent=2))
    if not passed:
        for r in results:
            if not r["clean_dependency_audit"]:
                print((ROOT / r["log"]).read_text())
        raise SystemExit(1)

if __name__ == "__main__":
    main()
