#!/usr/bin/env python3
"""Independent fresh Lean build and declaration audit for SystemIndividuation.

The inventory scanner is deliberately limited to the inspected single-namespace
source layout. Generated constructors/projections are not separately counted.
No empirical or universal foundational certification is produced.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "RESEARCH.md").is_file())
LEAN = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean"
SOURCE = LEAN / "deeper/SystemIndividuation.lean"
CORE = LEAN / "GenerativeCore.lean"
AUTHOR = LEAN / "deeper/system-individuation-checks/20261007T233431.104249Z/receipt.json"
COMMAND = [str(Path.home() / ".elan/bin/lean"), "+leanprover/lean4:v4.29.1"]


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def code_only(text):
    # The inspected module contains nested-capable block comments, no strings.
    out, pos, depth = [], 0, 0
    while pos < len(text):
        if text[pos:pos + 2] == "/-":
            depth += 1
            pos += 2
        elif depth and text[pos:pos + 2] == "-/":
            depth -= 1
            pos += 2
        elif depth:
            out.append("\n" if text[pos] == "\n" else " ")
            pos += 1
        elif text[pos:pos + 2] == "--":
            end = text.find("\n", pos)
            pos = len(text) if end < 0 else end
        else:
            out.append(text[pos])
            pos += 1
    assert depth == 0
    return "".join(out)


def main():
    raw = SOURCE.read_bytes()
    core = CORE.read_bytes()
    code = code_only(raw.decode())
    assert re.findall(r"^namespace (\w+)$", code, re.M) == ["SystemIndividuation"]
    assert re.findall(r"^import (\w+)$", code, re.M) == ["GenerativeCore"]
    assert not re.search(r'\b(?:axiom|sorry|admit|unsafe|native_decide|implemented_by)\b|debug\.skipKernelTC', code)
    declarations = [{"kind": kind, "name": "SystemIndividuation." + name}
                    for kind, name in re.findall(r"^(def|theorem|inductive|structure|abbrev) (\w+)", code, re.M)]
    names = [d["name"] for d in declarations]
    assert len(names) == len(set(names)) == 41
    assert sum(d["kind"] == "theorem" for d in declarations) == 27
    author_bytes = AUTHOR.read_bytes()
    author = json.loads(author_bytes)
    assert author["status"] == "passed"
    assert author["source_sha256"] == {"GenerativeCore": sha(core), "SystemIndividuation": sha(raw)}
    authored = next(m for m in author["modules"] if m["module"] == "SystemIndividuation")
    assert authored["declarations"] == declarations
    for name, expected in author["artifact_sha256"].items():
        assert sha((AUTHOR.parent / name).read_bytes()) == expected, name

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    retained = HERE / stamp
    retained.mkdir()
    (retained / "SystemIndividuation.lean").write_bytes(raw)
    (retained / "GenerativeCore.lean").write_bytes(core)
    (retained / "check.py").write_bytes(Path(__file__).read_bytes())
    receipt = {"status": "checking", "utc": stamp, "source_sha256": author["source_sha256"],
               "author_receipt": str(AUTHOR.relative_to(ROOT)), "author_receipt_sha256": sha(author_bytes),
               "declarations": declarations, "new_theorems": 27, "new_declarations": 41,
               "scope": "Independent fresh compilation of both source modules and audit of all 41 explicit new declarations; inherited science not rerun; no assumption-free completion claim."}
    try:
        with tempfile.TemporaryDirectory(prefix="system-individuation-independent-") as temporary:
            work = Path(temporary)
            for filename in ["GenerativeCore.lean", "SystemIndividuation.lean"]:
                (work / filename).write_bytes((retained / filename).read_bytes())
            env = dict(os.environ, LEAN_PATH=str(work))
            def run(args, log):
                p = subprocess.run(COMMAND + args, cwd=work, env=env, capture_output=True, text=True, timeout=60)
                output = p.stdout + p.stderr
                (retained / log).write_text(output)
                assert p.returncode == 0 and not re.search(r"\b(?:error|warning):", output), output
                return output
            receipt["lean_version"] = run(["--version"], "version.log").strip()
            for module in ["GenerativeCore", "SystemIndividuation"]:
                run(["-o", module + ".olean", module + ".lean"], module + ".log")
            audit = "import SystemIndividuation\n" + "\n".join("#print axioms " + n for n in names) + "\n"
            signatures = "import SystemIndividuation\n" + "\n".join("#check " + d["name"] for d in declarations if d["kind"] == "theorem") + "\n"
            for filename, content in [("Audit.lean", audit), ("Signatures.lean", signatures)]:
                (work / filename).write_text(content)
                (retained / filename).write_text(content)
                output = run([filename], filename + ".log")
                if filename == "Audit.lean":
                    empty = re.findall(r"'([^']+)' does not depend on any axioms", output)
                    assert empty == names
                    assert "depends on axioms:" not in output
                    receipt["axiom_dependencies"] = {n: [] for n in empty}
        assert SOURCE.read_bytes() == raw and CORE.read_bytes() == core
        receipt["source_unchanged_during_check"] = True
        receipt["status"] = "passed"
    except Exception as e:
        receipt["status"] = "failed"
        receipt["error"] = str(e)
        raise
    finally:
        receipt["artifact_sha256"] = {p.name: sha(p.read_bytes()) for p in sorted(retained.iterdir()) if p.is_file()}
        (retained / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"status": receipt["status"], "receipt": str((retained / "receipt.json").relative_to(ROOT)), "theorems": 27, "declarations": 41}))


if __name__ == "__main__":
    main()
