#!/usr/bin/env python3
"""Check formed corrective routes, actual component exchange and inherited repair."""
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
MODULES = {
    "GenerativeCore": (PACKAGE.parent / "GenerativeCore.lean", "Generative", ["Std"]),
    "DevelopmentalAssociation": (PACKAGE / "DevelopmentalAssociation.lean", "DevelopmentalAssociation", ["GenerativeCore"]),
    "ReconstructiveSelection": (PACKAGE / "ReconstructiveSelection.lean", "ReconstructiveSelection", ["Std"]),
    "AssemblyDerivedSelection": (PACKAGE / "AssemblyDerivedSelection.lean", "AssemblyDerivedSelection", ["ReconstructiveSelection", "DevelopmentalAssociation"]),
    "ContactReconstruction": (PACKAGE / "ContactReconstruction.lean", "ContactReconstruction", ["AssemblyDerivedSelection"]),
    "MaterialMaturation": (PACKAGE / "MaterialMaturation.lean", "MaterialMaturation", ["ContactReconstruction"]),
    "GrownFragmentation": (PACKAGE / "GrownFragmentation.lean", "GrownFragmentation", ["MaterialMaturation"]),
    "RecurrentAssembly": (PACKAGE / "RecurrentAssembly.lean", "RecurrentAssembly", ["GrownFragmentation"]),
    "StructuralCopying": (PACKAGE / "StructuralCopying.lean", "StructuralCopying", ["RecurrentAssembly"]),
    "CopyingRegistration": (PACKAGE / "CopyingRegistration.lean", "CopyingRegistration", ["StructuralCopying"]),
    "CopyingCorrection": (PACKAGE / "CopyingCorrection.lean", "CopyingCorrection", ["CopyingRegistration"]),
}
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    sources = {name + ".lean": path.read_bytes() for name, (path, _, _) in MODULES.items()}
    sources["lean-toolchain"] = (PACKAGE / "lean-toolchain").read_bytes()
    assert sources["lean-toolchain"].decode().strip() == TOOLCHAIN
    registry, theorems = {}, {}
    for module, (_, namespace, imports) in MODULES.items():
        code = re.sub(r"/-.*?-/|--[^\n]*", "", sources[module + ".lean"].decode(), flags=re.S)
        assert not re.search(r"\b(sorry|admit|axiom|unsafe|native_decide|implemented_by)\b|skipKernelTC", code)
        assert re.findall(r"^import\s+(\S+)", code, re.M) == imports
        registry[module] = [namespace + "." + name for name in re.findall(
            r"^(?:theorem|def|abbrev|structure|inductive)\s+(\w+)", code, re.M)]
        theorems[module] = re.findall(r"^theorem\s+(\w+)", code, re.M)
        sources[module + "Audit.lean"] = ("import " + module + "\n\n" + "\n".join(
            "#print axioms " + name for name in registry[module]) + "\n").encode()
    logs, commands, audits = {}, [], {}
    lean = str(Path.home() / ".elan/bin/lean")
    with tempfile.TemporaryDirectory(prefix="copying-correction-") as tmp:
        stage = Path(tmp)
        for name, data in sources.items():
            (stage / name).write_bytes(data)
        env = dict(os.environ, LEAN_PATH=str(stage))

        def run(args, log):
            command = [lean, "+" + TOOLCHAIN] + args
            commands.append(command)
            result = subprocess.run(command, cwd=stage, env=env, text=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
            logs[log] = result.stdout
            assert result.returncode == 0, result.stdout
            assert "warning:" not in result.stdout and "error:" not in result.stdout
            return result.stdout

        version = run(["--version"], "version.txt").strip()
        for module in MODULES:
            run(["-o", module + ".olean", module + ".lean"], module + "-compiler.txt")
            audit = run([module + "Audit.lean"], module + "-axioms.txt")
            parsed = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms:\s*\[([^\]]*)\])", audit, re.S)
            assert [name for name, _ in parsed] == registry[module]
            audits[module] = {}
            for name, raw in parsed:
                dependencies = [p.strip() for p in raw.split(",") if p.strip()]
                assert set(dependencies) <= ALLOWED, (name, dependencies)
                audits[module][name] = dependencies
    for module, (path, _, _) in MODULES.items():
        assert path.read_bytes() == sources[module + ".lean"], "Source changed during checking"
    snapshots = HERE / "sources"
    snapshots.mkdir(exist_ok=True)
    for name, data in sources.items():
        (snapshots / name).write_bytes(data)
    for name, log in logs.items():
        (HERE / name).write_text(log)
    new = audits["CopyingCorrection"]
    receipt = {
        "status": "passed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "version": version, "toolchain": TOOLCHAIN, "fresh_temporary_build": True,
        "commands": commands, "source_unchanged_during_check": True,
        "source_sha256": {name: sha(data) for name, data in sources.items()},
        "log_sha256": {name: sha(log.encode()) for name, log in logs.items()},
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "source_locations": {module + ".lean": str(path.relative_to(PACKAGE.parent)) for module, (path, _, _) in MODULES.items()},
        "new_theorem_count": len(theorems["CopyingCorrection"]),
        "new_audit_count": len(new), "total_audit_count": sum(map(len, audits.values())),
        "new_empty_axiom_count": sum(not v for v in new.values()), "axiom_dependencies": audits,
        "scope": "A connector reclaimed from actual copying forms a source-to-product checking/editing route. Inspection consumes support and any enabled mismatch response exchanges actual available material. Exact single-site repair requires matching stock and two operational support units after formation. Faithful references make finite inspection scans non-increasing in positional defects, without guaranteeing completion. Shared wrong references can hide errors or damage correct products; exhausted support can prevent editing or release. Copying-origin, microscopic comparison/editing, fault distribution, plan discovery, reference renewal, autonomous feed and population selection remain outside this conditional composition.",
    }
    (HERE / "verification.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({key: receipt[key] for key in ["status", "new_theorem_count", "new_audit_count", "total_audit_count", "new_empty_axiom_count"]}, indent=2))


if __name__ == "__main__":
    main()
