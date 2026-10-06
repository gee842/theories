#!/usr/bin/env python3
"""Checks for PhaseCycleDerivation.lean: source lint, independent finite
enumeration, source binding to the original apparatus, and (when the pinned
Lean toolchain is available) a fresh build of the import closure with axiom
audits. Writes phase-cycle-verification.json next to this file.

The finite enumeration is an independent Python reconstruction; it is not a
substitute for the Lean kernel check. When Lean is unavailable the receipt says
so and the Lean statements remain unverified.
"""
from datetime import datetime, timezone
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
MODULE = HERE / "PhaseCycleDerivation.lean"
SEARCH = [CORE, CORE / "inquiry-root", HERE]
DIAGNOSIS = CORE.parent / "mathematical-abstraction/acquisition/access/diagnosis.py"
ACQUISITION_CHECK = CORE.parent / "mathematical-abstraction/acquisition/check.py"
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


# ---- independent finite reconstruction -------------------------------------

def phase_recoverable(p):
    n, seen = len(p), {}
    for q in range(n):
        for inv in (0, 1):
            readings = tuple(p[(q + k) % n] ^ inv for k in range(n))
            if seen.setdefault(readings, q) != q:
                return False
    return True


def both_within(p, bound):
    n = len(p)
    return all(any(p[(q + j) % n] == v for j in range(bound + 1))
               for q in range(n) for v in (0, 1))


def two_valued(p):
    return 0 < sum(p) < len(p)


def rotation_of(p, base):
    n = len(p)
    return any(all(p[(i + s) % n] == base[i] for i in range(n)) for s in range(n))


def enumeration():
    counts = {}
    for bound in (1, 2, 3):
        counts[str(bound)] = {str(n): sum(1 for p in product((0, 1), repeat=n)
                                          if two_valued(p) and phase_recoverable(p) and both_within(p, bound))
                              for n in range(1, 15)}
    recover_only = {str(n): sum(1 for p in product((0, 1), repeat=n)
                                if two_valued(p) and phase_recoverable(p)) for n in range(1, 11)}
    three = [p for p in product((0, 1), repeat=3) if two_valued(p)]
    assert all(phase_recoverable(p) and both_within(p, 2) for p in three)
    assert all(rotation_of(p, (0, 0, 1)) or rotation_of(tuple(1 - x for x in p), (0, 0, 1)) for p in three)
    assert counts["2"]["1"] == counts["2"]["2"] == counts["2"]["4"] == 0 and counts["2"]["3"] == 6
    assert all(v == 0 for v in counts["1"].values())
    assert recover_only["1"] == recover_only["2"] == 0 and recover_only["3"] == 6
    assert phase_recoverable((0, 0, 0, 1)) and not both_within((0, 0, 0, 1), 2)
    p5 = (0, 0, 1, 0, 1)
    assert two_valued(p5) and phase_recoverable(p5) and both_within(p5, 2)
    # Orbits of every change table on carriers of one through six.
    orbit = {}
    for n in range(1, 7):
        injective = merging_with_transient = 0
        for f in product(range(n), repeat=n):
            if len(set(f)) == n:
                injective += 1
                for x in range(n):
                    y, back = x, False
                    for _ in range(n):
                        y = f[y]
                        back = back or y == x
                    assert back
            else:
                transient = False
                for x in range(n):
                    y, back = x, False
                    for _ in range(n):
                        y = f[y]
                        back = back or y == x
                    transient = transient or not back
                assert transient  # every merging change leaves some configuration unrevisited
                merging_with_transient += 1
        orbit[str(n)] = dict(injective=injective, merging_all_with_transient=merging_with_transient)
    return dict(admitted_by_bound=counts, admitted_without_reach_bound=recover_only,
                period_five_witness=list(p5), period_four_reach_failure=[0, 0, 0, 1], orbits=orbit)


# ---- binding to the original apparatus -------------------------------------

def source_binding():
    diagnosis = DIAGNOSIS.read_bytes()
    acquisition = ACQUISITION_CHECK.read_bytes()
    text = diagnosis.decode()
    assert "assert self.H.alphabet == ('a',) and len(self.H.outputs) == 3" in text
    assert "assert tuple(self.H.outputs[q] for q in walk) == (0,0,1)" in text
    assert "raise Halt('phase_unresolved')" in text
    assert "unary = m.Machine(('a',),(0,0,1),((1,),(2,),(0,)))" in acquisition.decode()
    return {str(DIAGNOSIS.relative_to(REPO)): sha(diagnosis),
            str(ACQUISITION_CHECK.relative_to(REPO)): sha(acquisition)}


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
    visit("PhaseCycleDerivation")
    return [(name, index[name]) for name in order]


def lean_build(namespace, declared):
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
    with tempfile.TemporaryDirectory(prefix="phase-cycle-lean-") as temporary:
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
            if name == "PhaseCycleDerivation":
                for declaration, axioms in AUDIT.findall(output):
                    audits[declaration] = [a.strip() for a in axioms.split(",") if a.strip()]
            if run.returncode != 0:
                return dict(status="failed", modules=modules, failing_output=output[-4000:])
    expected = sorted(namespace + "." + d for d in declared)
    passed = (all(m["clean"] for m in modules) and sorted(audits) == expected
              and all(not v for v in audits.values()))
    return dict(status="passed" if passed else "failed", toolchain=toolchain,
                version=version.stdout.strip(), modules=modules,
                audits=len(audits), empty_audits=sum(1 for v in audits.values() if not v),
                nonempty=[k for k, v in audits.items() if v])


def main():
    source = MODULE.read_bytes()
    namespace, declared = lint(source.decode())
    report = dict(
        checked_at_utc=datetime.now(timezone.utc).isoformat(),
        module=str(MODULE.relative_to(REPO)), module_sha256=sha(source),
        checker_sha256=sha(Path(__file__).read_bytes()),
        declared=len(declared), lint="passed",
        enumeration=enumeration(), source_binding=source_binding(),
        lean=lean_build(namespace, declared),
        scope=("Python enumeration is an independent finite reconstruction, not a kernel "
               "proof. Lean statements count as verified only when lean.status is passed."))
    (HERE / "phase-cycle-verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(dict(lint=report["lint"], declared=report["declared"],
                          lean=report["lean"]["status"]), indent=2))


if __name__ == "__main__":
    main()
