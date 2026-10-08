#!/usr/bin/env python3
"""Checks for PhasePeriodUniversal.lean: source lint (no sorry, admit,
native_decide, axiom declarations; one axiom audit per declaration) and, when
Lean 4.29.1 is available as `lean +leanprover/lean4:v4.29.1` on PATH, a fresh
build of the import closure with the axiom audit of every declaration of the new
module. Writes phase-universal-verification.json next to this file.

The module proves reduction lemmas toward the unbounded period lower bound; it
does not prove that bound. See PHASE-PERIOD-ASSUMPTIONS.md.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
CORE = HERE.parents[1]
REPO = CORE.parents[4]
MODULES = [HERE / "PhasePeriodUniversal.lean"]
SEARCH = [CORE, CORE / "inquiry-root", HERE]
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def lint(text):
    assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", text)
    assert not re.search(r"^\s*(axiom|constant)\s", text, re.M)
    namespace = re.search(r"^namespace (\S+)", text, re.M).group(1)
    declared = re.findall(r"^(?:theorem|def|abbrev|inductive|structure)\s+(\w+)", text, re.M)
    audited = re.findall(r"^#print axioms (\S+)", text, re.M)
    assert sorted(namespace + "." + d for d in declared) == sorted(audited), "audit mismatch"
    return namespace, declared


# ---- optional Lean build ----------------------------------------------------

def closure():
    index = {}
    for root in SEARCH:
        for path in root.glob("*.lean"):
            index.setdefault(path.stem, path)
    order, visiting = [], set()

    def visit(name):
        if name in order or name.split(".")[0] in ("Std", "Init", "Lean"):
            return
        assert name not in visiting
        visiting.add(name)
        for item in re.findall(r"^import\s+(\S+)", index[name].read_text(), re.M):
            visit(item)
        order.append(name)
    for module in MODULES:
        visit(module.stem)
    return [(name, index[name]) for name in order]


def lean_build(expected):
    toolchain = (CORE / "lean-toolchain").read_text().strip()
    lean = shutil.which("lean")
    if lean is None:
        return dict(status="lean_unavailable", toolchain=toolchain)
    try:
        version = subprocess.run([lean, "+" + toolchain, "--version"], text=True,
                                 capture_output=True, timeout=600)
    except Exception as error:  # elan cannot fetch the toolchain, for example
        return dict(status="lean_unavailable", toolchain=toolchain, error=str(error))
    if version.returncode != 0 or "4.29.1" not in version.stdout:
        return dict(status="lean_unavailable", toolchain=toolchain,
                    error=(version.stdout + version.stderr)[-2000:])
    modules, audits = [], {}
    with tempfile.TemporaryDirectory(prefix="phase-universal-lean-") as temporary:
        build = Path(temporary)
        for name, path in closure():
            source = path.read_bytes()
            (build / (name + ".lean")).write_bytes(source)
            run = subprocess.run([lean, "+" + toolchain, "-o", name + ".olean", name + ".lean"],
                                 cwd=build, text=True, capture_output=True, timeout=1800,
                                 env={"LEAN_PATH": str(build), "PATH": "/usr/bin:/bin"})
            output = run.stdout + run.stderr
            warning = re.search(r"warning|error", output)
            modules.append(dict(module=name, source=str(path.relative_to(REPO)),
                                source_sha256=sha(source), exit_code=run.returncode,
                                clean=run.returncode == 0 and not warning))
            if name in [module.stem for module in MODULES]:
                for declaration, axioms in AUDIT.findall(output):
                    audits[declaration] = [a.strip() for a in axioms.split(",") if a.strip()]
            if run.returncode != 0:
                return dict(status="failed", modules=modules, failing_output=output[-4000:])
    passed = (all(m["clean"] for m in modules) and sorted(audits) == sorted(expected)
              and all(not v for v in audits.values()))
    return dict(status="passed" if passed else "failed", toolchain=toolchain,
                version=version.stdout.strip(), modules=modules,
                audits=len(audits), empty_audits=sum(1 for v in audits.values() if not v),
                nonempty=[k for k, v in audits.items() if v])


def main():
    expected, sources = [], {}
    for module in MODULES:
        source = module.read_bytes()
        namespace, declared = lint(source.decode())
        expected += [namespace + "." + d for d in declared]
        sources[str(module.relative_to(REPO))] = sha(source)
    report = dict(
        checked_at_utc=datetime.now(timezone.utc).isoformat(),
        modules=sources, checker_sha256=sha(Path(__file__).read_bytes()),
        declared=len(expected), lint="passed", lean=lean_build(expected),
        scope=("Reduction lemmas only: sub-belief monotonicity, transfer between paired "
               "beliefs, propext-free arithmetic of the advance, and stretches read forward. "
               "The unbounded period lower bound itself is not claimed. Lean statements "
               "count as verified only when lean.status is passed. No existing module is "
               "changed."))
    (HERE / "phase-universal-verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(dict(lint=report["lint"], declared=report["declared"],
                          lean=report["lean"]["status"],
                          modules=len(report["lean"].get("modules", [])),
                          audits=report["lean"].get("audits")), indent=2))


if __name__ == "__main__":
    main()
