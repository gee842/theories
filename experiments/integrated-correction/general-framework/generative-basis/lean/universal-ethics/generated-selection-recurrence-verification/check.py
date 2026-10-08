#!/usr/bin/env python3
"""Fresh source-bound build of generated reconstruction and its inherited modules."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent
TOOLCHAIN = "leanprover/lean4:v4.29.1"
MODULES = ["RecursiveGenerativeSelection", "RecursiveSelectionInheritance", "GeneratedSelectionRecurrence"]
ALLOWED = {"propext", "Quot.sound", "Classical.choice"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    filenames = [name + suffix for name in MODULES for suffix in [".lean", "Audit.lean"]]
    filenames.append("lean-toolchain")
    sources = {name: (PACKAGE / name).read_bytes() for name in filenames}
    assert sources["lean-toolchain"].decode().strip() == TOOLCHAIN
    registry = {}
    for module in MODULES:
        source = sources[module + ".lean"].decode()
        code = re.sub(r"/-.*?-/|--[^\n]*", "", source, flags=re.S)
        assert not re.search(r"\b(sorry|admit|axiom|unsafe|native_decide|implemented_by)\b|skipKernelTC", code)
        imports = re.findall(r"^import\s+(\S+)", code, re.M)
        assert imports == ([] if module == MODULES[0] else [MODULES[MODULES.index(module) - 1]])
        names = re.findall(r"^(?:theorem|def|instance|structure|inductive)\s+(\w+)", code, re.M)
        registry[module] = [module + "." + name for name in names]
        expected = "import " + module + "\n\n" + "\n".join(
            "#print axioms " + name for name in registry[module]) + "\n"
        assert sources[module + "Audit.lean"].decode() == expected
    commands, logs, audits = [], {}, {}
    lean = str(Path.home() / ".elan/bin/lean")
    with tempfile.TemporaryDirectory(prefix="generated-selection-recurrence-") as tmp:
        stage = Path(tmp)
        for name, data in sources.items():
            (stage / name).write_bytes(data)
        environment = os.environ.copy()
        environment["LEAN_PATH"] = str(stage)

        def run(arguments, log):
            command = [lean, "+" + TOOLCHAIN] + arguments
            commands.append(command)
            result = subprocess.run(command, cwd=stage, env=environment, text=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                    timeout=120)
            logs[log] = result.stdout
            assert result.returncode == 0, result.stdout
            assert "warning:" not in result.stdout and "error:" not in result.stdout
            return result.stdout

        version = run(["--version"], "version.txt").strip()
        for module in MODULES:
            run(["-o", module + ".olean", module + ".lean"], module + "-compiler.txt")
            text = run([module + "Audit.lean"], module + "-axioms.txt")
            parsed = re.findall(
                r"'([^']+)' (?:does not depend on any axioms|depends on axioms:\s*\[([^\]]*)\])",
                text, flags=re.S)
            assert [name for name, _ in parsed] == registry[module], text
            audits[module] = {}
            for name, raw in parsed:
                dependencies = [part.strip() for part in raw.split(",") if part.strip()]
                assert set(dependencies) <= ALLOWED, (name, dependencies)
                audits[module][name] = dependencies
    snapshots = HERE / "sources"
    snapshots.mkdir(exist_ok=True)
    for name, data in sources.items():
        (snapshots / name).write_bytes(data)
        assert (PACKAGE / name).read_bytes() == data, "Source changed during the check: " + name
    for name, text in logs.items():
        (HERE / name).write_text(text)
    new_audits = audits[MODULES[-1]]
    receipt = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed", "toolchain": TOOLCHAIN, "version": version,
        "fresh_temporary_build": True, "source_unchanged_during_check": True,
        "LEAN_PATH": "fresh temporary directory only", "commands": commands,
        "allowed_standard_axioms": sorted(ALLOWED),
        "audit_count": sum(len(items) for items in audits.values()),
        "new_audit_count": len(new_audits),
        "new_empty_axiom_audits": sum(not deps for deps in new_audits.values()),
        "axiom_dependencies": audits,
        "source_sha256": {name: sha(data) for name, data in sources.items()},
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "log_sha256": {name: sha(text.encode()) for name, text in logs.items()},
        "scope": "Generated transfer entries, supported reconfiguration, arbitrary finite history accounting and exact witness histories under supplied operational laws; no selected reconstruction recipe or evolutionary universality.",
    }
    (HERE / "verification.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"audits": receipt["audit_count"],
                      "new_audits": receipt["new_audit_count"],
                      "new_empty_axiom_audits": receipt["new_empty_axiom_audits"],
                      "receipt": str(HERE / "verification.json")}, indent=2))


if __name__ == "__main__":
    main()
