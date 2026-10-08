#!/usr/bin/env python3
"""Check contact-level reconstruction, actual partitions and coarse-graining limits."""
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
    with tempfile.TemporaryDirectory(prefix="contact-reconstruction-") as tmp:
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
    new = audits["ContactReconstruction"]
    receipt = {
        "status": "passed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "version": version, "toolchain": TOOLCHAIN, "fresh_temporary_build": True,
        "commands": commands, "source_unchanged_during_check": True,
        "source_sha256": {name: sha(data) for name, data in sources.items()},
        "log_sha256": {name: sha(log.encode()) for name, log in logs.items()},
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "source_locations": {module + ".lean": str(path.relative_to(PACKAGE.parent)) for module, (path, _, _) in MODULES.items()},
        "new_theorem_count": len(theorems["ContactReconstruction"]),
        "new_audit_count": len(new), "total_audit_count": sum(map(len, audits.values())),
        "new_empty_axiom_count": sum(not v for v in new.values()), "axiom_dependencies": audits,
        "scope": "Actual transmitted components and retained contact opportunities determine encounter success. Uniform sampling with replacement projects exactly to the finite assembly process; each seed reconstructs its own bond. Checked partitions conserve components yet yield different reconstruction at equal mean contact rate and expected encounter cost. Variation invalidates a generic single-P return coefficient. A typed three-stage operator derives finite cycle returns and a valid aggregation under its balanced mixture law. Compatibility, contact geometry, partition formation, stocks and repeated mature-stage preparation remain supplied. No origin of replication, empirical calibration or superiority over an equally informed spatial model.",
    }
    (HERE / "verification.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({key: receipt[key] for key in ["status", "new_theorem_count", "new_audit_count", "total_audit_count", "new_empty_axiom_count"]}, indent=2))


if __name__ == "__main__":
    main()
