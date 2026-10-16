#!/usr/bin/env python3
"""Fresh Lean 4.29.1 kernel/dependency check of the formative-capacity model.

The scanner covers this source's explicit top-level declarations (including its
named instance), not Lean-generated constructor/projection/deriving declarations.
Kernel success does not establish physical or ethical correspondence.
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
CORE = HERE.parents[1] / "GenerativeCore.lean"
TOOLCHAIN = "leanprover/lean4:v4.29.1"
SOURCES = {"GenerativeCore": CORE, "FormativeCapacity": HERE / "FormativeCapacity.lean"}
STANDARD_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def code_only(source):
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
        r"\b(sorry|admit|axiom|unsafe|native_decide|implemented_by)\b|debug\.skipKernelTC", code
    ), "Proof escape in source"
    imports = re.findall(r"^import\s+(.+)$", code, re.M)
    assert all(item.strip() in {"Std", "GenerativeCore"} for item in imports), imports
    scopes, result = [], []
    for line in code.splitlines():
        scope = re.match(r"^(namespace|section)\b\s*(\S*)", line)
        if scope:
            scopes.append((scope[1], scope[2]))
            continue
        if re.match(r"^end(?:\s|$)", line):
            assert scopes, line
            scopes.pop()
            continue
        declaration = re.match(
            r"^(theorem|def|abbrev|structure|inductive|instance)\s+([\w.]+)", line
        )
        if declaration:
            prefix = ".".join(n for kind, n in scopes if kind == "namespace")
            name = prefix + "." + declaration[2] if prefix else declaration[2]
            result.append({"kind": declaration[1], "name": name})
    assert not scopes and result
    assert len({item["name"] for item in result}) == len(result)
    return result


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    retained = HERE / "checks" / stamp
    retained.mkdir(parents=True, exist_ok=False)
    sources = {name: path.read_bytes() for name, path in SOURCES.items()}
    checker = Path(__file__).read_bytes()
    (retained / "check.py").write_bytes(checker)
    for name, data in sources.items():
        (retained / (name + ".lean")).write_bytes(data)
    receipt = {
        "status": "checking", "utc": stamp, "toolchain": TOOLCHAIN,
        "checker_sha256": digest(checker), "retained_run": str(retained.relative_to(HERE)),
        "source_sha256": {name: digest(data) for name, data in sources.items()},
        "scope": "Checked mathematical implications of the stated assembly law; no ethical verdict or empirical validation.",
    }
    try:
        registry = {name: declarations(data.decode()) for name, data in sources.items()}
        lean = Path.home() / ".elan/bin/lean"
        command = [str(lean), "+" + TOOLCHAIN]
        binary = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
        receipt["lean_binary_sha256"] = digest(binary.read_bytes())
        records = []
        with tempfile.TemporaryDirectory(prefix="formative-capacity-lean-") as scratch:
            work = Path(scratch)
            env = {**os.environ, "LEAN_PATH": str(work)}

            def run(args, log):
                p = subprocess.run(command + args, cwd=work, env=env, text=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
                (retained / log).write_text(p.stdout)
                assert p.returncode == 0, p.stdout
                assert not re.search(r"\b(?:error|warning):", p.stdout), p.stdout
                return p.stdout

            receipt["lean_version"] = run(["--version"], "version.log").strip()
            assert "version 4.29.1" in receipt["lean_version"]
            for name, data in sources.items():
                (work / (name + ".lean")).write_bytes(data)
            for name in sources:
                run(["-o", name + ".olean", name + ".lean"], name + ".log")
                audit = "import " + name + "\n" + "\n".join(
                    "#print axioms " + item["name"] for item in registry[name]) + "\n"
                audit_name = name + "AxiomAudit.lean"
                (work / audit_name).write_text(audit)
                (retained / audit_name).write_text(audit)
                output = run([audit_name], name + "AxiomAudit.log")
                dependencies = {}
                for item in registry[name]:
                    full = item["name"]
                    if "'" + full + "' does not depend on any axioms" in output:
                        axioms = []
                    else:
                        match = re.search(r"'" + re.escape(full) + r"' depends on axioms:\s*\[([^]]*)\]", output)
                        assert match, (full, output)
                        axioms = [a.strip() for a in match[1].split(",") if a.strip()]
                    assert set(axioms) <= STANDARD_AXIOMS, (full, axioms)
                    dependencies[full] = axioms
                records.append({
                    "module": name, "theorems": sum(x["kind"] == "theorem" for x in registry[name]),
                    "declarations": registry[name], "axiom_dependencies": dependencies,
                    "kernel_checked": True,
                })
        receipt["source_unchanged_during_check"] = all(
            SOURCES[name].read_bytes() == data for name, data in sources.items())
        assert receipt["source_unchanged_during_check"], "Source changed; only snapshot checked"
        assert Path(__file__).read_bytes() == checker, "Checker changed during run"
        receipt["modules"] = records
        receipt["artifact_sha256"] = {
            p.name: digest(p.read_bytes()) for p in sorted(retained.iterdir()) if p.is_file()
        }
        receipt["status"] = "passed"
    except Exception as error:
        receipt["status"] = "failed"
        receipt["error"] = str(error)
        raise
    finally:
        serialized = json.dumps(receipt, indent=2) + "\n"
        (retained / "verification.json").write_text(serialized)
        (HERE / "verification.json").write_text(serialized)
    model = next(r for r in records if r["module"] == "FormativeCapacity")
    print(json.dumps({"status": receipt["status"], "new_theorems": model["theorems"],
                      "new_declaration_audits": len(model["declarations"]),
                      "axioms": sorted({a for r in records for aa in r["axiom_dependencies"].values() for a in aa}),
                      "receipt": str(HERE / "verification.json")}))


if __name__ == "__main__":
    main()
