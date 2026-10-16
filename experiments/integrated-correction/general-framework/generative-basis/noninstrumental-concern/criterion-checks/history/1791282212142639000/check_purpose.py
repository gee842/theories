#!/usr/bin/env python3
"""Fresh, source-bound build of continuation correction and its actual adapter.

This checks formal statements under their explicit process/contract inputs.
It is not certification of experience, moral necessity, or rule formation.
"""
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
REPO = next(p for p in HERE.parents if (p / "AGENTS.md").exists())
INQUIRY = REPO / (
    "experiments/shared-renewal-capability/regulation/retention/formation/selectors/"
    "updaters/prediction/recipient-correction/identification/recording/reason-consumer/"
    "action/revision/evaluation/plasticity/formal/inquiry-revision"
)
NEW = ("PurposeCorrection", "PurposeCorrectionHistory")
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def code_without_comments(source):
    """Retain code positions while excluding Lean comments and string contents."""
    out = []
    i, depth, string = 0, 0, False
    while i < len(source):
        c = source[i]
        pair = source[i:i + 2]
        if depth:
            if pair == "/-":
                depth += 1
                out.extend("  ")
                i += 2
            elif pair == "-/":
                depth -= 1
                out.extend("  ")
                i += 2
            else:
                out.append("\n" if c == "\n" else " ")
                i += 1
        elif string:
            if c == "\\" and i + 1 < len(source):
                out.extend("  ")
                i += 2
            else:
                string = c != '"'
                out.append("\n" if c == "\n" else " ")
                i += 1
        elif pair == "/-":
            depth = 1
            out.extend("  ")
            i += 2
        elif pair == "--":
            end = source.find("\n", i)
            end = len(source) if end < 0 else end
            out.extend(" " * (end - i))
            i = end
        elif c == '"':
            string = True
            out.append(" ")
            i += 1
        else:
            out.append(c)
            i += 1
    assert depth == 0 and not string, "unterminated comment or string"
    return "".join(out)


def main():
    inherited_bytes = (INQUIRY / "verification.json").read_bytes()
    inherited = json.loads(inherited_bytes)
    assert inherited["status"] == "passed"
    compiler_record_bytes = (HERE / "coformation-verification.json").read_bytes()
    compiler_record = json.loads(compiler_record_bytes)
    compiler = Path(compiler_record["compiler"])
    assert sha(compiler.read_bytes()) == compiler_record["compiler_sha256"]
    version = subprocess.check_output([str(compiler), "--version"], text=True).strip()
    assert "version 4.29.1," in version
    paths = {row["module"]: REPO / row["source"] for row in inherited["modules"]}
    occurrence_record = next(row for row in compiler_record["modules"]
                             if row["module"] == "CoupledOccurrence")
    paths["CoupledOccurrence"] = REPO / occurrence_record["source"]
    for name in NEW:
        paths[name] = HERE / (name + ".lean")
    frozen = {name: p.read_bytes() for name, p in paths.items()}
    for row in inherited["modules"]:
        assert sha(frozen[row["module"]]) == row["sha256"], row["module"]
    assert sha(frozen["CoupledOccurrence"]) == occurrence_record["sha256"]
    requested = {}
    dependencies = {}
    for name, data in frozen.items():
        source = code_without_comments(data.decode())
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", source), name
        assert not re.search(r"^\s*(axiom|constant|opaque)\s", source, re.M), name
        imports = set(re.findall(r"^import\s+(\S+)", source, re.M))
        assert imports <= set(paths) | {"Std"}, (name, imports - set(paths))
        dependencies[name] = imports - {"Std"}
        requested[name] = re.findall(r"^#print axioms (\S+)$", source, re.M)
        if name in NEW:
            theorems = set(re.findall(r"^\s*(?:theorem|lemma) (\w+)", source, re.M))
            assert theorems == {x.rsplit(".", 1)[-1] for x in requested[name]}, name
    order = []
    pending = set(paths)
    while pending:
        ready = [n for n in paths if n in pending and dependencies[n] <= set(order)]
        assert ready, "cyclic import closure"
        order.extend(ready)
        pending.difference_update(ready)
    checker = Path(__file__).read_bytes()
    attempt = HERE / "purpose-checks" / str(time.time_ns())
    attempt.mkdir(parents=True)
    (attempt / "check_purpose.py").write_bytes(checker)
    for name in NEW:
        (attempt / (name + ".lean")).write_bytes(frozen[name])
    bindings = {
        name: {"source": str(paths[name].relative_to(REPO)), "sha256": sha(data)}
        for name, data in frozen.items()
    }
    (attempt / "inputs.json").write_text(json.dumps(bindings, indent=2) + "\n")
    rows = []
    with tempfile.TemporaryDirectory(prefix="purpose-correction-lean-") as temporary:
        build = Path(temporary)
        for name, data in frozen.items():
            (build / (name + ".lean")).write_bytes(data)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in order:
            try:
                result = subprocess.run(
                    [str(compiler), "-o", name + ".olean", name + ".lean"],
                    cwd=build, env=env, text=True, stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT, timeout=300,
                )
            except subprocess.TimeoutExpired as error:
                output = error.stdout or ""
                if isinstance(output, bytes):
                    output = output.decode(errors="replace")
                result = subprocess.CompletedProcess([], 124, output + "\nTIMEOUT after 300s\n")
            log = attempt / (name + ".txt")
            log.write_text(result.stdout)
            audits = {
                name: sorted(a.strip() for a in deps.split(",") if a.strip())
                for name, deps in AUDIT.findall(result.stdout)
            }
            names_match = len(audits) == len(requested[name]) and all(
                actual == expected or actual.endswith("." + expected)
                for actual, expected in zip(audits, requested[name])
            )
            allowed = all(set(a) <= {"propext", "Quot.sound", "Classical.choice"}
                          for a in audits.values())
            passed = result.returncode == 0 and "warning:" not in result.stdout and names_match and allowed
            rows.append(dict(
                module=name, **bindings[name], new=name in NEW, passed=passed,
                exit_code=result.returncode, axioms_by_declaration=audits,
                log=str(log.relative_to(HERE)), log_sha256=sha(log.read_bytes()),
            ))
            print(json.dumps(dict(module=name, passed=passed, audits=len(audits))), flush=True)
            if not passed:
                print(result.stdout, flush=True)
                break
    stable = all(p.read_bytes() == frozen[n] for n, p in paths.items())
    stable = stable and Path(__file__).read_bytes() == checker
    stable = stable and (INQUIRY / "verification.json").read_bytes() == inherited_bytes
    passed = len(rows) == len(paths) and all(r["passed"] for r in rows) and stable
    record = dict(
        status="passed" if passed else "failed",
        checked_at_utc=datetime.now(timezone.utc).isoformat(),
        compiler=str(compiler), compiler_sha256=sha(compiler.read_bytes()), version=version,
        checker_sha256=sha(checker), inherited_receipt_sha256=sha(inherited_bytes),
        compiler_record_sha256=sha(compiler_record_bytes), fresh_temporary_build=True,
        inputs_unchanged=stable, modules=rows,
        new_audits=sum(len(r["axioms_by_declaration"]) for r in rows if r["new"]),
        scope="Supplied continuation contracts, actual generative histories and correction "
              "of an arrangement. No identification of a stock with experience, learned origin "
              "of the contract, universal ethical necessity or assumption-free foundation.",
    )
    (attempt / "receipt.json").write_text(json.dumps(record, indent=2) + "\n")
    if passed:
        (HERE / "purpose-verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print("RECEIPT " + str(attempt / "receipt.json"), flush=True)
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
