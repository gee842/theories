#!/usr/bin/env python3
"""Kernel, statement and dependency checks of retrospective source-to-binding composition.

Reuses the existing explicit-declaration scanner, snapshots original sources,
and audits all named declarations. Lean-generated declarations are compiled
but not separately counted. No empirical or cognitive-sufficiency certificate.
"""
from datetime import datetime, timezone
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
SUPPORT = HERE.parent / "universal-ethics/generative-capacity/check.py"
spec = importlib.util.spec_from_file_location("audit_support", SUPPORT)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
GROUND = HERE.parent / "universal-ethics/generative-capacity"
IMPORTS = {
    "KnowledgeCorrespondence": ["Std"],
    "NormativeActivity": ["KnowledgeCorrespondence"],
    "StandardsBridge": ["Std"],
    "FormedGrounds": ["NormativeActivity", "StandardsBridge"],
    "SelectiveRevision": ["FormedGrounds"],
    "SourceReliance": ["SelectiveRevision"],
    "CompositionalAcquisition": ["KnowledgeCorrespondence"],
    "CompositionalFormation": ["CompositionalAcquisition"],
    "CompositionalTransmission": ["CompositionalFormation"],
    "AcquiredSegmentation": ["CompositionalTransmission"],
    "AcquiredBinding": ["AcquiredSegmentation"],
    "RetrospectiveBinding": ["SourceReliance", "AcquiredBinding"],
}
SOURCES = {name: (GROUND if name in ["NormativeActivity", "StandardsBridge", "FormedGrounds"] else HERE) / (name+".lean") for name in IMPORTS}


def inventory(name, data):
    code = audit.code_only(data.decode())
    imports = re.findall(r"^import\s+(.+)$", code, re.M)
    assert imports == IMPORTS[name], (name, imports)
    normalized = re.sub(r"^import\s+[^\n]+", "import Std", code, flags=re.M)
    normalized = re.sub(r"^noncomputable def\b", "def", normalized, flags=re.M)
    return audit.declarations(normalized)


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    retained = HERE / "retrospective-binding-checks" / stamp
    retained.mkdir(parents=True, exist_ok=False)
    sources = {name: p.read_bytes() for name,p in SOURCES.items()}
    helpers = {"check_retrospective_binding.py": Path(__file__).read_bytes(),
               "audit_support.py": SUPPORT.read_bytes()}
    for name,data in sources.items():
        (retained / (name + ".lean")).write_bytes(data)
    for name,data in helpers.items():
        (retained / name).write_bytes(data)
    receipt = {"status": "checking", "utc": stamp, "toolchain": audit.TOOLCHAIN,
        "retained_run": str(retained.relative_to(HERE)),
        "source_sha256": {name: audit.digest(data) for name,data in sources.items()},
        "checker_sha256": {name: audit.digest(data) for name,data in helpers.items()},
        "scope": "Acquired source-route distinctions reinterpret earlier retained naming packets and supply binding candidates, then enter all-sequence compositional interpretation and finite response. Route family, channel identity, calibration fidelity, stable transfer, fault envelope and elementary repertoire remain supplied. No full developmental or evolutionary explanation."}
    try:
        registry = {name: inventory(name,data) for name,data in sources.items()}
        binary = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
        receipt["lean_binary_sha256"] = audit.digest(binary.read_bytes())
        command = [str(Path.home() / ".elan/bin/lean"), "+" + audit.TOOLCHAIN]
        records = []
        with tempfile.TemporaryDirectory(prefix="retrospective-binding-") as tmp:
            work = Path(tmp)
            env = {**os.environ, "LEAN_PATH": str(work)}
            def run(args, log):
                p = subprocess.run(command + args, cwd=work, env=env, text=True,
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
                (retained / log).write_text(p.stdout)
                assert p.returncode == 0 and not re.search(r"\b(error|warning):", p.stdout), p.stdout
                return p.stdout
            receipt["lean_version"] = run(["--version"], "version.log").strip()
            for name,data in sources.items():
                (work / (name + ".lean")).write_bytes(data)
            for name in sources:
                run(["-o", name + ".olean", name + ".lean"], name + ".log")
                declarations = registry[name]
                commands = "import " + name + "\n" + "\n".join(
                    "#print axioms " + x["name"] for x in declarations) + "\n"
                signatures = "import " + name + "\n" + "\n".join(
                    "#check " + x["name"] for x in declarations if x["kind"] == "theorem") + "\n"
                for suffix,content in [("Audit",commands),("Signatures",signatures)]:
                    filename = name + suffix + ".lean"
                    (work / filename).write_text(content)
                    (retained / filename).write_text(content)
                    output = run([filename], name + suffix + ".log")
                    if suffix == "Audit":
                        dependencies = {}
                        for x in declarations:
                            full = x["name"]
                            if "'" + full + "' does not depend on any axioms" in output:
                                deps = []
                            else:
                                match = re.search(r"'" + re.escape(full) + r"' depends on axioms:\s*\[([^]]*)\]", output)
                                assert match, full
                                deps = [a.strip() for a in match[1].split(",") if a.strip()]
                            assert set(deps) <= audit.STANDARD_AXIOMS, (full,deps)
                            dependencies[full] = deps
                records.append({"module": name, "theorems": sum(x["kind"] == "theorem" for x in declarations),
                    "declarations": declarations, "axiom_dependencies": dependencies, "kernel_checked": True})
        assert all(SOURCES[name].read_bytes() == data for name,data in sources.items())
        assert Path(__file__).read_bytes() == helpers["check_retrospective_binding.py"]
        assert SUPPORT.read_bytes() == helpers["audit_support.py"]
        receipt["source_unchanged_during_check"] = True
        receipt["modules"] = records
        receipt["artifact_sha256"] = {p.name: audit.digest(p.read_bytes()) for p in sorted(retained.iterdir()) if p.is_file()}
        receipt["status"] = "passed"
    except Exception as exc:
        receipt["status"] = "failed"
        receipt["error"] = str(exc)
        raise
    finally:
        saved = json.dumps(receipt, indent=2) + "\n"
        (retained / "verification.json").write_text(saved)
        (HERE / "retrospective-binding-verification.json").write_text(saved)
    own = records[-1]
    print(json.dumps({"status": receipt["status"], "new_theorems": own["theorems"],
        "new_declaration_audits": len(own["declarations"]),
        "inherited_declaration_audits": sum(len(r["declarations"]) for r in records[:-1]),
        "receipt": str(HERE / "retrospective-binding-verification.json")}))


if __name__ == "__main__":
    main()
