#!/usr/bin/env python3
"""Fresh Lean 4.29.1 kernel/dependency check of the formative-capacity model.

The scanner covers this source's explicit declarations (including its named instance)
at any indentation and with any attributes or modifiers, not Lean-generated
constructor/projection/deriving declarations; private declarations and unnamed
instances are listed apart (`scan`), since they cannot be audited by name.
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


# A scope opens with `namespace`/`section` (also `noncomputable section`) or `mutual`, at
# any indentation, and closes with `end`.
SCOPE_OPEN = re.compile(r"^\s*(?:noncomputable\s+)?(namespace|section)\b\s*(\S*)")
MUTUAL_OPEN = re.compile(r"^\s*mutual\s*$")
SCOPE_END = re.compile(r"^\s*end(?:\s+\S+)?\s*$")
# A declaration at any indentation, after `open … in`, attributes (`@[simp]`) and modifiers.
DECLARATION = re.compile(
    r"^\s*(?:open\b.*?\bin\s+)?"
    r"((?:(?:@\[[^\]]*\]|private|protected|noncomputable|partial|nonrec|unsafe|scoped|local)\s*)*)"
    r"(theorem|def|abbrev|structure|inductive|instance)\b(.*)$")
# A declared name runs to the first space, colon or bracket (primes and `!`/`?` included).
DECLARED_NAME = re.compile(r"[^\s:()\[\]{}⦃⦄,]+")


def scan(source):
    """The declarations of a source, read from its code with comments, docstrings and
    strings blanked (`code_only`), at any indentation and with any attributes or modifiers.

    `declarations`: those an importing file can audit by name (`#print axioms`), in order.
    `private`: private declarations, whose names an importing file cannot resolve.
    `unnamed_instances`: line numbers of `instance` declarations without a name (Lean names
    them itself). Neither of the last two can be audited by name; an environment-wide audit
    of the module's constants covers them. Constants Lean generates (constructors,
    projections, `injEq`, deriving) are not source declarations and are not listed."""
    code = code_only(source)
    assert not re.search(
        r"\b(sorry|admit|axiom|unsafe|native_decide|implemented_by)\b|debug\.skipKernelTC", code
    ), "Proof escape in source"
    imports = re.findall(r"^import\s+(.+)$", code, re.M)
    assert all(item.strip() in {"Std", "GenerativeCore"} for item in imports), imports
    scopes, named, private, unnamed = [], [], [], []
    for number, line in enumerate(code.splitlines(), 1):
        scope = SCOPE_OPEN.match(line)
        if scope:
            scopes.append((scope[1], scope[2]))
            continue
        if MUTUAL_OPEN.match(line):
            scopes.append(("mutual", ""))
            continue
        if SCOPE_END.match(line):
            assert scopes, (number, line)
            scopes.pop()
            continue
        declaration = DECLARATION.match(line)
        if not declaration:
            continue
        modifiers, kind, rest = declaration[1], declaration[2], declaration[3].strip()
        if kind == "instance":
            rest = re.sub(r"^\(priority\s*:=[^)]*\)\s*", "", rest)
        name = DECLARED_NAME.match(rest)
        if not name:
            assert kind == "instance", (number, line)
            unnamed.append(number)
            continue
        name = name[0].split(".{")[0].rstrip(".")
        if name.startswith("_root_."):
            full = name[len("_root_."):]
        else:
            prefix = ".".join(n for k, n in scopes if k == "namespace" and n)
            full = prefix + "." + name if prefix else name
        (private if re.search(r"\bprivate\b", modifiers) else named).append({"kind": kind, "name": full})
    # A section may stay open to the end of the file; a namespace may not.
    assert not [s for s in scopes if s[0] != "section"], scopes
    assert named
    assert len({item["name"] for item in named}) == len(named)
    return {"declarations": named, "private": private, "unnamed_instances": unnamed}


def declarations(source):
    """The declarations of a source that can be audited by name (see `scan`)."""
    return scan(source)["declarations"]


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
