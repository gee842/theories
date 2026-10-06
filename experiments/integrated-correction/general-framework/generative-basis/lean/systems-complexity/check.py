#!/usr/bin/env python3
"""Build the frozen systems/complexity package in a fresh Lean 4.29.1 directory.

No inherited checker, receipt or compiled object is used or rewritten. The
source screen is a conservative check for this package's declaration style,
not a general Lean parser. Kernel compilation and explicit dependency audits
provide the independent checks of successful proof elaboration.
"""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parent
MODULES = ["GenerativeCore", "SystemsOrganization", "FeedbackDynamics", "SymbolicDynamics",
           "SystemsComplexity"]
SOURCES = {
    name: (ROOT.parent if name == "GenerativeCore" else ROOT) / (name + ".lean")
    for name in MODULES
}
STANDARD_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
TOOLCHAIN = "leanprover/lean4:v4.29.1"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=180)


def code_only(source):
    """Blank nested comments and string contents while preserving line breaks."""
    out = []
    pos = 0
    depth = 0
    in_string = False
    while pos < len(source):
        pair = source[pos:pos + 2]
        char = source[pos]
        if depth:
            if pair == "/-":
                depth += 1
                out.extend("  ")
                pos += 2
            elif pair == "-/":
                depth -= 1
                out.extend("  ")
                pos += 2
            else:
                out.append("\n" if char == "\n" else " ")
                pos += 1
        elif in_string:
            if char == "\\" and pos + 1 < len(source):
                out.extend("  ")
                pos += 2
            else:
                in_string = char != '"'
                out.append("\n" if char == "\n" else " ")
                pos += 1
        elif pair == "/-":
            depth = 1
            out.extend("  ")
            pos += 2
        elif pair == "--":
            end = source.find("\n", pos)
            end = len(source) if end == -1 else end
            out.extend(" " * (end - pos))
            pos = end
        elif char == '"':
            in_string = True
            out.append(" ")
            pos += 1
        else:
            out.append(char)
            pos += 1
    if depth or in_string:
        raise ValueError("Unclosed comment or string in source screen")
    return "".join(out)


def inspect_source(name, source):
    code = code_only(source.decode("utf-8"))
    forbidden = re.search(r"\b(sorry|admit|native_decide|unsafe)\b", code)
    if forbidden:
        raise ValueError(f"{name}: forbidden proof/code token {forbidden.group()}")
    if re.search(r"^\s*(?:(?:private|protected)\s+)*(?:axiom|constant)\s", code, re.M):
        raise ValueError(f"{name}: explicit axiom/constant declaration")
    imports = re.findall(r"^import\s+([^\n]+)", code, re.M)
    allowed = {"Std"} | set(MODULES[:MODULES.index(name)])
    imported_names = [module for line in imports for module in line.split()]
    if not set(imported_names) <= allowed:
        raise ValueError(f"{name}: unrecognized or forward imports {imported_names}")
    requested = re.findall(r"^#print\s+axioms\s+(\S+)", code, re.M)
    declarations = []
    namespaces = []
    for line in code.splitlines():
        match = re.match(r"^namespace\s+(\S+)\s*$", line)
        if match:
            namespaces.append(match.group(1))
        elif re.match(r"^end(?:\s+\S+)?\s*$", line):
            if namespaces:
                namespaces.pop()
        else:
            match = re.match(r"^(?:theorem|lemma)\s+([^\s(:]+)(?:\s|$)", line)
            if match:
                declarations.append(".".join(namespaces + [match.group(1)]))
    lexical_count = len(re.findall(r"\b(?:theorem|lemma)\s+", code))
    if len(declarations) != lexical_count:
        raise ValueError(f"{name}: unsupported declaration style in audit screen")
    if len(requested) != len(set(requested)):
        raise ValueError(f"{name}: duplicate requested dependency audit")
    if name != "GenerativeCore" and (
        len(declarations) != len(requested) or set(declarations) != set(requested)
    ):
        raise ValueError(f"{name}: theorem/audit coverage differs: "
                         f"missing={set(declarations)-set(requested)}, "
                         f"extra={set(requested)-set(declarations)}")
    return {"imports": imported_names, "theorems": declarations,
            "requested_audits": requested,
            "coverage_scope": "selected inherited audits" if name == "GenerativeCore"
                              else "every declared theorem/lemma exactly once"}


def main():
    frozen = {name: path.read_bytes() for name, path in SOURCES.items()}
    checker_bytes = Path(__file__).read_bytes()
    toolchain_bytes = (ROOT / "lean-toolchain").read_bytes()
    if toolchain_bytes.decode().strip() != TOOLCHAIN:
        raise ValueError("Unexpected toolchain")
    inspections = {name: inspect_source(name, data) for name, data in frozen.items()}
    compiler = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
    version = run([str(compiler), "--version"], ROOT)
    version.check_returncode()
    if "version 4.29.1," not in version.stdout:
        raise ValueError("Compiler version does not match frozen toolchain")
    compiler_hash = digest(compiler.read_bytes())
    output_dir = ROOT / "verification"
    snapshot_dir = output_dir / "sources"
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    for name, data in frozen.items():
        (snapshot_dir / (name + ".lean")).write_bytes(data)
    (snapshot_dir / "lean-toolchain").write_bytes(toolchain_bytes)
    (snapshot_dir / "check.py").write_bytes(checker_bytes)
    results = []
    with tempfile.TemporaryDirectory(prefix="systems-complexity-lean-") as temporary:
        build = Path(temporary)
        for name, data in frozen.items():
            (build / (name + ".lean")).write_bytes(data)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in MODULES:
            result = run([str(compiler), "-o", name + ".olean", name + ".lean"], build, env)
            log = output_dir / (name + ".txt")
            log.write_text(result.stdout)
            matched_audits = re.findall(
                r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
                result.stdout,
            )
            requested = inspections[name]["requested_audits"]
            audits = [{"declaration": decl,
                       "dependencies": [a.strip() for a in group.split(",") if a.strip()]}
                      for decl, group in matched_audits]
            names = [audit["declaration"] for audit in audits]
            axioms = sorted({a for audit in audits for a in audit["dependencies"]})
            clean = (names == requested and bool(audits)
                     and set(axioms) <= STANDARD_AXIOMS
                     and "sorryAx" not in result.stdout
                     and "warning:" not in result.stdout and "error:" not in result.stdout)
            results.append({
                "module": name,
                "source": os.path.relpath(SOURCES[name], ROOT),
                "source_sha256": digest(frozen[name]),
                "snapshot": "verification/sources/" + name + ".lean",
                "exit_code": result.returncode,
                **inspections[name],
                "dependency_audits": len(audits),
                "audits": audits,
                "axioms": axioms,
                "empty_axiom_audits": sum(not audit["dependencies"] for audit in audits),
                "clean_dependency_audit": clean,
                "output": "verification/" + log.name,
                "output_sha256": digest(log.read_bytes()),
            })
            if result.returncode or not clean:
                break
    unchanged = (all(path.read_bytes() == frozen[name] for name, path in SOURCES.items())
                 and Path(__file__).read_bytes() == checker_bytes
                 and (ROOT / "lean-toolchain").read_bytes() == toolchain_bytes
                 and digest(compiler.read_bytes()) == compiler_hash)
    passed = (len(results) == len(MODULES) and unchanged and
              all(r["exit_code"] == 0 and r["clean_dependency_audit"] for r in results))
    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if passed else "failed",
        "lean_version": version.stdout.strip(),
        "compiler_binary": str(compiler), "compiler_sha256": compiler_hash,
        "toolchain": TOOLCHAIN, "toolchain_sha256": digest(toolchain_bytes),
        "checker_sha256": digest(checker_bytes),
        "source_unchanged_during_check": unchanged,
        "fresh_temporary_build": True,
        "input_source_hashes": {name: digest(data) for name, data in frozen.items()},
        "allowed_standard_axioms": sorted(STANDARD_AXIOMS),
        "axiom_interpretation": "Standard logical dependencies are reported per theorem; "
            "they are not custom physical axioms. An empty list does not remove supplied "
            "model definitions, theorem hypotheses, mathematical background or the need "
            "for an independently justified real-system correspondence.",
        "modules": results,
        "audited_declarations": sum(r["dependency_audits"] for r in results),
        "new_audited_declarations": sum(r["dependency_audits"] for r in results
                                        if r["module"] != "GenerativeCore"),
        "new_empty_axiom_audits": sum(r["empty_axiom_audits"] for r in results
                                      if r["module"] != "GenerativeCore"),
        "scope": "Actual generative-core trace correspondence for iteration, the binary "
            "shift and rational delayed feedback. Conditional structural organization/projection, exact rational feedback "
            "dynamics, finite autonomous recurrence and an infinite binary-symbolic chaos "
            "witness. This receipt is not an empirical identification, a physical chaos "
            "claim for the finite learner, ethical grounding or a universal ontology proof. "
            "The separate Mathlib real-analysis package is outside this receipt.",
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
