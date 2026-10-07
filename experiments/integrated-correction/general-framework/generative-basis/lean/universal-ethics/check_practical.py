#!/usr/bin/env python3
"""Check the whole-comparison restriction interface in a fresh Lean 4.29.1 directory.

Kernel checks establish the declared mathematical implications, not their
normative premises or correspondence to every intelligence. The source scanner
supports these modules' simple namespace style; it is not a Lean parser.
"""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile


HERE = Path(__file__).resolve().parent
TOOLCHAIN = "leanprover/lean4:v4.29.1"
MODULES = ["WholePracticalRestriction"]
RUN_LOG = None
RUN_COUNTER = 0
SOURCE_BINDINGS = {}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def code_only(source):
    # Preserve newlines while removing nested comments and quoted strings.
    output, i, depth, quoted = [], 0, 0, False
    while i < len(source):
        pair, char = source[i:i + 2], source[i]
        if depth:
            if pair == "/-":
                depth += 1
                output.append("  ")
                i += 2
            elif pair == "-/":
                depth -= 1
                output.append("  ")
                i += 2
            else:
                output.append("\n" if char == "\n" else " ")
                i += 1
        elif quoted:
            if char == "\\" and i + 1 < len(source):
                output.append("  ")
                i += 2
            else:
                quoted = char != '"'
                output.append("\n" if char == "\n" else " ")
                i += 1
        elif pair == "/-":
            depth = 1
            output.append("  ")
            i += 2
        elif pair == "--":
            end = source.find("\n", i)
            end = len(source) if end == -1 else end
            output.append(" " * (end - i))
            i = end
        elif char == '"':
            quoted = True
            output.append(" ")
            i += 1
        else:
            output.append(char)
            i += 1
    assert not depth and not quoted, "Unclosed source comment/string"
    return "".join(output)


def declarations(source):
    code = code_only(source)
    assert not re.search(
        r"\b(sorry|admit|axiom|unsafe|native_decide|implemented_by)\b|debug\.skipKernelTC",
        code,
    ), "Unsupported proof escape in source"
    imports = re.findall(r"^import\s+(.+)$", code, re.M)
    assert all(item.strip() in {"Init", "Std"} for item in imports), imports
    scopes, result = [], []
    for line in code.splitlines():
        scope = re.match(r"^\s*(namespace|section)\b\s*(\S*)", line)
        if scope:
            scopes.append((scope[1], scope[2]))
            continue
        if re.match(r"^end(?:\s|$)", line):
            assert scopes, line
            scopes.pop()
            continue
        declaration = re.match(
            r"^(?:(?:noncomputable|protected)\s+)?"
            r"(theorem|def|abbrev|structure|inductive)\s+([\w.]+)", line,
        )
        if declaration:
            prefix = ".".join(n for kind, n in scopes if kind == "namespace")
            name = prefix + "." + declaration[2] if prefix else declaration[2]
            result.append({"kind": declaration[1], "name": name})
    assert not scopes, scopes
    assert result and len({item["name"] for item in result}) == len(result)
    return result


def run(command, cwd, environment):
    global RUN_COUNTER
    RUN_COUNTER += 1
    outcome = subprocess.run(command, cwd=cwd, env=environment, text=True,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                             timeout=120)
    record = {"command": command, "returncode": outcome.returncode,
              "output": outcome.stdout}
    (RUN_LOG / (str(RUN_COUNTER).zfill(2) + "-command.json")).write_text(
        json.dumps(record, indent=2) + "\n")
    if outcome.returncode != 0 or "declaration uses 'sorry'" in outcome.stdout:
        (RUN_LOG / "failure.json").write_text(json.dumps({
            "status": "failed", "command": command, "sources": SOURCE_BINDINGS,
            "checker_sha256": digest(Path(__file__).read_bytes()),
            "output": outcome.stdout,
        }, indent=2) + "\n")
        raise AssertionError(outcome.stdout)
    return outcome.stdout


def main():
    global RUN_LOG, SOURCE_BINDINGS
    # Copy bytes first: concurrently changing sources cannot silently change a run.
    sources = {name: (HERE / (name + ".lean")).read_bytes() for name in MODULES}
    registry = {name: declarations(data.decode()) for name, data in sources.items()}
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    retained = HERE / "practical-verification" / stamp
    retained.mkdir(parents=True, exist_ok=False)
    RUN_LOG = retained
    (retained / "check_practical.py").write_bytes(Path(__file__).read_bytes())
    SOURCE_BINDINGS = {name: digest(data) for name, data in sources.items()}
    lean = Path.home() / ".elan/bin/lean"
    command = [str(lean), "+" + TOOLCHAIN]
    records = []
    with tempfile.TemporaryDirectory(prefix="whole-practical-restriction-") as scratch:
        work = Path(scratch)
        environment = os.environ.copy()
        environment["LEAN_PATH"] = str(work)
        version = run(command + ["--version"], work, environment).strip()
        assert "4.29.1" in version, version
        for name, data in sources.items():
            (work / (name + ".lean")).write_bytes(data)
            (retained / (name + ".lean")).write_bytes(data)
        for name in MODULES:
            output = run(command + ["-o", name + ".olean", name + ".lean"],
                         work, environment)
            (retained / (name + ".log")).write_text(output)
            audit = "import " + name + "\n" + "\n".join(
                "#print axioms " + item["name"] for item in registry[name]) + "\n"
            audit_name = name + "AxiomAudit.lean"
            (work / audit_name).write_text(audit)
            audited = run(command + [audit_name], work, environment)
            (retained / audit_name).write_text(audit)
            (retained / (name + "AxiomAudit.log")).write_text(audited)
            for item in registry[name]:
                assert "'" + item["name"] + "' does not depend on any axioms" in audited, (
                    item["name"], audited)
            records.append({
                "module": name, "sha256": digest(sources[name]),
                "declarations": registry[name],
                "theorems": sum(d["kind"] == "theorem" for d in registry[name]),
                "axioms": [], "kernel_checked": True,
            })
    unchanged = all((HERE / (name + ".lean")).read_bytes() == data
                    for name, data in sources.items())
    receipt = {
        "status": "passed", "utc": stamp, "lean": version,
        "source_unchanged_during_check": unchanged,
        "checker_sha256": digest(Path(__file__).read_bytes()),
        "retained_run": str(retained.relative_to(HERE)), "modules": records,
        "scope": "Declared mathematical implications only; universal ethical warrant unresolved.",
    }
    (retained / "verification.json").write_text(json.dumps(receipt, indent=2) + "\n")
    assert unchanged, "Source changed during check; retained snapshot passed, current source unverified"
    (HERE / "practical-verification.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"status": "passed", "lean": version,
                      "theorems": sum(r["theorems"] for r in records),
                      "audits": sum(len(r["declarations"]) for r in records),
                      "all_axiom_sets_empty": True,
                      "receipt": str(HERE / "practical-verification.json")}))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        if RUN_LOG is not None and not (RUN_LOG / "failure.json").exists():
            (RUN_LOG / "failure.json").write_text(json.dumps({
                "status": "failed", "error": str(error), "sources": SOURCE_BINDINGS,
                "checker_sha256": digest(Path(__file__).read_bytes()),
            }, indent=2) + "\n")
        raise
