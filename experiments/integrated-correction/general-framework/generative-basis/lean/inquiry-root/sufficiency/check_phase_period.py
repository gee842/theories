#!/usr/bin/env python3
"""Checks for PhasePeriodSelection.lean and FormedContactCycle.lean: source lint,
an independent finite reconstruction of the knowing-arrival game, source binding
to the original apparatus, and (when the pinned Lean toolchain is available) a
fresh build of the import closure with axiom audits of both new modules. Writes
phase-period-verification.json next to this file.

The Python game solver is an independent reconstruction (memoized, on sets); it
is not a substitute for the Lean kernel check.
"""
from datetime import datetime, timezone
from functools import lru_cache
from itertools import product
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
MODULES = [HERE / "PhasePeriodSelection.lean", HERE / "FormedContactCycle.lean"]
SEARCH = [CORE, CORE / "inquiry-root", HERE]
DIAGNOSIS = CORE.parent / "mathematical-abstraction/acquisition/access/diagnosis.py"
MODEL = CORE.parent / "mathematical-abstraction/acquisition/model.py"
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


# ---- independent reconstruction of the knowing-arrival game -----------------

def least_commands(p, value, cap=12):
    """Least worst-case number of advance/read commands, from unknown phase and
    unknown reading inversion, after which the current contact value is known."""
    n = len(p)

    @lru_cache(None)
    def solve(belief, depth):
        if all(p[q] == value for q, _ in belief):
            return 0
        if depth == 0:
            return None
        options = []
        moved = solve(frozenset(((q + 1) % n, i) for q, i in belief), depth - 1)
        if moved is not None:
            options.append(moved + 1)
        parts = [frozenset(x for x in belief if (p[x[0]] ^ x[1]) == o) for o in (0, 1)]
        if all(parts):
            values = [solve(part, depth - 1) for part in parts]
            if None not in values:
                options.append(max(values) + 1)
        return min(options) if options else None

    return solve(frozenset((q, i) for q in range(n) for i in (0, 1)), cap)


def enumeration():
    table = {}
    for n in range(1, 9):
        best = None
        sevens = []
        for p in product((0, 1), repeat=n):
            if not 0 < sum(p) < n:
                continue
            values = [least_commands(p, v) for v in (0, 1)]
            worst = None if None in values else max(values)
            if worst is not None and (best is None or worst < best):
                best = worst
            if worst is not None and worst <= 7:
                sevens.append("".join(map(str, p)))
        table[str(n)] = dict(least_worst_case=best, patterns_within_seven=sevens)
        assert best is None or best >= 7
        assert all(n % 3 == 0 and all(s[i] == s[(i + 3) % n] for i in range(n)) for s in sevens)
    assert table["3"]["least_worst_case"] == 7 and len(table["3"]["patterns_within_seven"]) == 6
    assert least_commands((0, 0, 1), 0) == 4 and least_commands((0, 0, 1), 1) == 7
    assert least_commands((0, 0, 0, 0, 1), 0) == 4
    waits = lambda p: sum(next(s for s in range(len(p)) if p[(q + s) % len(p)] == v)
                          for q in range(len(p)) for v in (0, 1))
    assert waits((0, 0, 1)) == 4 and waits((0, 0, 1, 0, 1)) == 6
    return dict(by_period=table, native_per_value=[4, 7],
                total_known_phase_waits={"001": 4, "00101": 6})


def source_binding():
    diagnosis = DIAGNOSIS.read_bytes()
    model = MODEL.read_bytes()
    assert "a.pay('native_'+command, extra=a.tariff.interface, temporary=2)" in diagnosis.decode()
    assert "for c in ('read','a','read','a','read'):" in diagnosis.decode()
    assert "return 1 + len(self.outputs)*(1+len(self.alphabet))" in model.decode()
    return {str(DIAGNOSIS.relative_to(REPO)): sha(diagnosis),
            str(MODEL.relative_to(REPO)): sha(model)}


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
    with tempfile.TemporaryDirectory(prefix="phase-period-lean-") as temporary:
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
        declared=len(expected), lint="passed",
        enumeration=enumeration(), source_binding=source_binding(),
        lean=lean_build(expected),
        scope=("Python game solving is an independent finite reconstruction, not a kernel "
               "proof. Lean statements count as verified only when lean.status is passed. "
               "ContactFormation.lean is imported unchanged from the contact-formation thread."))
    (HERE / "phase-period-verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(dict(lint=report["lint"], declared=report["declared"],
                          lean=report["lean"]["status"],
                          modules=len(report["lean"].get("modules", [])),
                          audits=report["lean"].get("audits")), indent=2))


if __name__ == "__main__":
    main()
