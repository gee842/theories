#!/usr/bin/env python3
"""Fresh build and all-declaration axiom audit for RecursiveGenerativeSelection.

Run from any directory. This imports no project checker and does not rebuild or
claim fresh validation of the older shared-support or transmission packages.
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
PACKAGE = HERE.parent
TOOLCHAIN = "leanprover/lean4:v4.29.1"
NAMES = ["RecursiveGenerativeSelection.lean", "RecursiveGenerativeSelectionAudit.lean", "lean-toolchain"]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    sources = {name: (PACKAGE / name).read_bytes() for name in NAMES}
    assert sources["lean-toolchain"].decode().strip() == TOOLCHAIN
    source = sources["RecursiveGenerativeSelection.lean"].decode()
    names = re.findall(r"^(?:theorem|def|instance)\s+(\w+)", source, re.M)
    code = re.sub(r"/-.*?-/|--[^\n]*", "", source, flags=re.S)
    assert not re.search(r"\b(sorry|admit|axiom|unsafe|native_decide|implemented_by)\b", code)
    assert not re.search(r"\bimport\b|skipKernelTC", code)
    expected_audit = "import RecursiveGenerativeSelection\n\n" + "\n".join(
        "#print axioms RecursiveGenerativeSelection." + name for name in names
    ) + "\n"
    assert sources["RecursiveGenerativeSelectionAudit.lean"].decode() == expected_audit
    commands, logs = [], {}
    lean = str(Path.home() / ".elan/bin/lean")
    with tempfile.TemporaryDirectory(prefix="recursive-generative-selection-") as tmp:
        stage = Path(tmp)
        for name, data in sources.items():
            (stage / name).write_bytes(data)
        environment = os.environ.copy()
        environment["LEAN_PATH"] = str(stage)

        def run(arguments, name):
            command = [lean, "+" + TOOLCHAIN] + arguments
            commands.append(command)
            result = subprocess.run(command, cwd=stage, env=environment, text=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                    timeout=120)
            logs[name] = result.stdout
            assert result.returncode == 0, result.stdout
            assert "warning:" not in result.stdout and "error:" not in result.stdout
            return result.stdout

        version = run(["--version"], "version.txt").strip()
        run(["-o", "RecursiveGenerativeSelection.olean", "RecursiveGenerativeSelection.lean"], "compiler.txt")
        audit = run(["RecursiveGenerativeSelectionAudit.lean"], "axioms.txt")
    entries = re.findall(r"'([^']+)' does not depend on any axioms", audit)
    assert entries == ["RecursiveGenerativeSelection." + name for name in names], audit
    assert "depends on axioms" not in audit
    snapshot = HERE / "sources"
    snapshot.mkdir(exist_ok=True)
    for name, data in sources.items():
        (snapshot / name).write_bytes(data)
    for name, data in logs.items():
        (HERE / name).write_text(data)
    receipt = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "toolchain": TOOLCHAIN,
        "version": version,
        "fresh_temporary_directory": True,
        "LEAN_PATH": "fresh temporary directory only",
        "commands": commands,
        "audited_declarations": entries,
        "audit_count": len(entries),
        "all_axiom_dependencies_empty": True,
        "source_sha256": {name: sha(data) for name, data in sources.items()},
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "log_sha256": {name: sha(data.encode()) for name, data in logs.items()},
        "scope": "Formal implications under stated hypotheses; no empirical or normative validation.",
    }
    (HERE / "verification.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"audits": len(entries), "all_axioms_empty": True,
                      "receipt": str(HERE / "verification.json")}, indent=2))


if __name__ == "__main__":
    main()
