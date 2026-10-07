#!/usr/bin/env python3
"""Checks for RecoveryQuantum.lean, FormationDraw.lean and StartingStock.lean:
source lint, an independent Python reconstruction of the closure history (rate
countercases and least starting stock), source binding of the conversion unit to
the original apparatus, and (when Lean 4.29.1 is available) a fresh build of the
import closure with axiom audits of the three new modules. Writes
stock-derivation-verification.json next to this file.

The Python reconstruction is independent of the Lean sources; it is not a
substitute for the Lean kernel check.
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
MODULES = [HERE / "RecoveryQuantum.lean", HERE / "FormationDraw.lean", HERE / "StartingStock.lean"]
SEARCH = [CORE, CORE / "inquiry-root", HERE]
DIAGNOSIS = CORE.parent / "mathematical-abstraction/acquisition/access/diagnosis.py"
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


# ---- independent reconstruction of the closure history ----------------------

BILL = 16384 + 0 + 0 + 2  # live = workspace = 0, two temporary cells


def run(history, fuel, source, rate=10, blocked=True, tau=False, phase=0, spare=0):
    """Returns the final state or None. Output table (0,0,1); arrival when
    output xor tau and not blocked; a conversion moves ten source units."""
    st = dict(fuel=fuel, source=source, wasted=0, transferred=0, spare=spare,
              recovered=0, blocked=blocked, phase=phase, spent=0)

    def draw():
        if st["fuel"] < BILL:
            return False
        st["fuel"] -= BILL
        st["spent"] += BILL
        return True
    for event in history:
        if not draw():
            return None
        if event == "a":
            st["phase"] = (st["phase"] + 1) % 3
        elif event == "probe":
            if st["source"] < 10:
                return None
            st["source"] -= 10
            arrived = ((st["phase"] == 2) != tau) and not st["blocked"]
            if arrived:
                st["transferred"] += 10
                st["fuel"] += 655360
            else:
                st["wasted"] += 10
            if not draw():
                return None
        elif event == "recover":
            if rate * (st["recovered"] + 1) > st["wasted"]:
                return None
            st["spare"] += 1
            st["recovered"] += 1
        elif event == "form":
            if st["spare"] < 1:
                return None
            st["spare"] -= 1
            st["blocked"] = False
    return st


def reconstruction():
    history = ["a", "a", "probe", "recover", "form", "probe"]
    least_fuel = next(f for f in range(0, 300000) if run(history, f, 20) is not None)
    least_source = next(s for s in range(0, 100) if run(history, 10 ** 6, s) is not None)
    assert least_fuel == 7 * BILL == 114702 and least_source == 20
    final = run(history, 114702, 20)
    assert final["transferred"] == 10 and final["fuel"] == 638974
    assert run(history, 114701, 20) is None and run(history, 114702, 19) is None
    assert run(history, 200000, 20, rate=11) is None
    nine = ["probe"] * 9 + ["recover"] * 10
    over = run(nine, 10 ** 6, 90, rate=9)
    assert over["wasted"] == 90 and over["recovered"] == 10
    assert run(nine, 10 ** 6, 90, rate=10) is None
    # one-pair-per-failure holds only at rate 10, checked on small ledgers
    rates = [r for r in range(0, 30)
             if all((r * (n + 1) <= 10 * k) == (n + 1 <= k)
                    for k in range(0, 40) for n in range(0, 40))]
    assert rates == [10]
    assert run(["form"], 100000, 0, spare=1)["wasted"] == 0
    return dict(least_fuel=least_fuel, least_source=least_source,
                final_fuel_at_least=final["fuel"], rate_eleven_closure="stopped",
                rate_nine_pairs_from_nine_failures=over["recovered"],
                rates_with_one_pair_per_failure=rates)


def source_binding():
    diagnosis = DIAGNOSIS.read_bytes()
    text = diagnosis.decode()
    for needle in ("if self._source < 10:", "self._source -= 10", "self.wasted += 10",
                   "self.transferred += 10",
                   "a.pay('native_'+command, extra=a.tariff.interface, temporary=2)",
                   "a.pay('arrival_receipt', extra=a.tariff.receipt, temporary=2)"):
        assert needle in text, needle
    return {str(DIAGNOSIS.relative_to(REPO)): sha(diagnosis)}


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
    with tempfile.TemporaryDirectory(prefix="stock-derivation-lean-") as temporary:
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
        reconstruction=reconstruction(), source_binding=source_binding(),
        lean=lean_build(expected),
        scope=("The Python reconstruction is independent of the Lean sources and is not a "
               "kernel proof. Lean statements count as verified only when lean.status is "
               "passed. No existing module is changed."))
    (HERE / "stock-derivation-verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(dict(lint=report["lint"], declared=report["declared"],
                          lean=report["lean"]["status"],
                          modules=len(report["lean"].get("modules", [])),
                          audits=report["lean"].get("audits")), indent=2))


if __name__ == "__main__":
    main()
