#!/usr/bin/env python3
"""Check the rational market's instances of the Becoming core's laws.

`MarketInstances` imports pure core modules of the Becoming spine and the rational market
modules of this directory. The market's definitions are rational arithmetic with standard
axioms, so its instances of the core's laws are stated here rather than in the pure bridge, and
their declarations may depend on `propext`, `Quot.sound` and `Classical.choice` only. The module
is compiled with Lean 4.29.1 and no Mathlib, as the core is. Module resolution, declaration
scanning, passed-receipt matching and the Lean step cache are those of the core checker
(`check_becoming.py`); the market modules of this directory are added to its index by file name.
Every other module in the closure must match a passed receipt (the core's, or this directory's
market receipts), so the core checker runs first. Neither the core nor any market module imports
this one. `BECOMING_FRESH=1` runs every step. The run folder keeps the receipt, the drivers and
logs of the steps that ran, and a copy of each file `main` does not hold byte for byte.
"""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
LEAN_ROOT = HERE.parents[1] / "integrated-correction" / "general-framework" / "generative-basis" / "lean"
sys.path.insert(0, str(LEAN_ROOT / "becoming"))
import check_becoming as core  # noqa: E402

TARGET = "MarketInstances"
RECEIPT = HERE / "market-instances-verification.json"
RETAINED = HERE / "market-instances-checks"
TOOLCHAIN = "leanprover/lean4:v4.29.1"
LEAN = Path.home() / ".elan/bin/lean"
BINARY = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
EXTERNAL = {"Init", "Std", "Lean"}
STANDARD_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}
# Seconds allowed for each Lean run; a heavily loaded machine may need more.
TIMEOUT = int(os.environ.get("LEAN_TIMEOUT", "900"))

SCOPE = (
    "Instances of the Becoming core's laws in the rational market of MarketGenerativity and its "
    "regime modules. Protected continuation (Becoming.Viability): the operating map is a law of "
    "change driven by disturbances and the guarded market is the core's guarded law with the "
    "essential floors as guard; some disturbance is admissible for every bound, so for every "
    "parameter set, bound set and start, no admissible history ever fails the essential guard "
    "exactly when some set of states containing the start lies within the essential floors and is "
    "closed under every admissible disturbance; under Certificate p b the safe rectangle is one, so "
    "safe_history_never_fails is an instance. Finite support obstruction (Becoming.Lasting, "
    "exhaustion): with a correction strength chosen at each step, the share's orbit under growth "
    "3/2 bounds it, and while that orbit stays at or below 1/6 a step with a nonnegative shock costs "
    "the stock one unit above the floor 5, so finite_support_forces_failure is an instance, and so "
    "is every_finite_stock_has_obstructed_positive_seeds. "
    "Supported finite transition (Becoming.Lasting, ladders): the cover recurrence is a ladder for "
    "every correction schedule and every shock at most the cost, so the prefixes of the supported "
    "transitions are instances, and at the worst share the cover is exact. Partial correction "
    "boundary (Becoming.Lasting, never reaching): some positive seed never lands exactly when a set "
    "closed under the regime law and avoiding landing contains one; for 0 <= b <= 3/4 every positive "
    "seed lands exactly when the quality margin at 3/8 under influence 1 is nonnegative, and exactly "
    "when no such set contains a positive seed; above 5/12 the fixed configuration is one. "
    "Landing side (Becoming.Lasting, reaching): every positive seed lands exactly when every "
    "positive seed is held by some funnel into landing; a quantity raised by a fixed gain up to a "
    "bound gives a funnel for every determined rational law; for 0 <= b <= 5/12 the market's gain "
    "estimates (share, then influence, then quality) supply such funnels from a settled region "
    "the law keeps, which a positive seed enters by the old seed retention estimates, so the "
    "landing side, its case b = 0 (the rescue's finite horizon) and the 5/12 boundary follow "
    "from the core's reaching law. "
    "Correspondence of the market law to actual markets, its parameters and its protected floors is "
    "not checked."
)


def market_modules():
    """The Lean modules of this directory, by file name."""
    return {path.stem: path for path in sorted(HERE.glob("*.lean"))}


def module_index():
    index = core.module_index()
    for name, path in market_modules().items():
        assert name not in index, ("market module name already in the core index", name)
        index[name] = [path]
    return index


def closure(index):
    order, seen = [], set()

    def visit(name):
        if name in seen or name.split(".")[0] in EXTERNAL:
            return
        paths = index.get(name, [])
        assert len(paths) == 1, (name, [str(p) for p in paths])
        for dependency in core.imports_of(paths[0].read_bytes()):
            visit(dependency)
        seen.add(name)
        order.append(name)

    visit(TARGET)
    return order


def passed_receipts():
    receipts = []
    for root, paths in [(LEAN_ROOT, LEAN_ROOT.rglob("*.json")), (HERE, HERE.glob("*.json"))]:
        for path in paths:
            if path == RECEIPT or RETAINED in path.parents:
                continue
            text = path.read_text(errors="replace")
            if '"passed"' in text:
                receipts.append((str(path.relative_to(root.parent)), text))
    return receipts


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    retained = RETAINED / stamp
    retained.mkdir(parents=True, exist_ok=False)
    index = module_index()
    order = closure(index)
    paths = {name: index[name][0] for name in order}
    sources = {name: paths[name].read_bytes() for name in order}
    helper_paths = [Path(__file__).resolve(), LEAN_ROOT / "becoming/check_becoming.py",
                    LEAN_ROOT / "universal-ethics/generative-capacity/check.py"]
    helpers = {p.name: p.read_bytes() for p in helper_paths}
    commit, held = core.held_in_main({**{p: helpers[p.name] for p in helper_paths},
                                      **{paths[name]: sources[name] for name in order}})
    copied = {p.name: helpers[p.name] for p in helper_paths if p not in held}
    copied.update({name + ".lean": sources[name] for name in order if paths[name] not in held})
    for name, data in copied.items():
        (retained / name).write_bytes(data)
    digest = core.audit_support.digest
    top = HERE.parents[1]
    receipt = {
        "status": "checking", "utc": stamp, "toolchain": TOOLCHAIN,
        "retained_run": str(retained.relative_to(HERE)),
        "instance_module": TARGET, "compile_order": order,
        "source_paths": {name: str(paths[name].relative_to(top)) for name in order},
        "source_sha256": {name: digest(data) for name, data in sources.items()},
        "checker_sha256": {name: digest(data) for name, data in helpers.items()},
        # Files main holds byte for byte are named by this commit; the rest are copied here.
        "source_commit": {"main": commit, "copied": sorted(copied)},
        "scope": SCOPE,
    }
    # A reused step passed in the named run with the same binary and identical inputs; its log
    # stays in the cache under its key. Drivers and logs of the steps that ran are kept here.
    steps = receipt["lean_steps"] = {"cache": str(core.CACHE), "fresh": core.FRESH, "ran": [], "reused": {}, "keys": {}}
    registry = []
    try:
        assert TARGET not in core.closure(core.module_index(), core.CORE), "the core imports the instance module"
        assert all(TARGET not in core.imports_of(path.read_bytes())
                   for name, path in market_modules().items() if name != TARGET), "a market module imports the instances"
        receipts = passed_receipts()
        matches = {}
        for name in order[:-1]:
            found = sorted(path for path, text in receipts if receipt["source_sha256"][name] in text)
            assert found, ("module has no passed receipt for its current bytes", name)
            matches[name] = found
        receipt["inherited_receipts"] = matches
        registry = core.declarations(sources[TARGET])
        receipt["lean_binary_sha256"] = digest(BINARY.read_bytes())
        command = [str(LEAN), "+" + TOOLCHAIN]
        context = [TOOLCHAIN, receipt["lean_binary_sha256"]]
        keys = core.module_keys(context, sources, order)
        origin = {"utc": stamp, "retained": str(retained)}
        with tempfile.TemporaryDirectory(prefix="market-instances-") as scratch:
            work = Path(scratch)
            env = {**os.environ, "LEAN_PATH": str(work)}

            def run(args, log, key=None, outputs=(), driver=None):
                outputs = [work / output for output in outputs]
                if key:
                    steps["keys"][log] = key
                found = core.reuse(key, outputs) if key else None
                if found:
                    output, steps["reused"][log] = found
                    return output
                if driver:
                    (retained / driver).write_bytes((work / driver).read_bytes())
                p = subprocess.run(command + args, cwd=work, env=env, text=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=TIMEOUT)
                (retained / log).write_text(p.stdout)
                assert p.returncode == 0, p.stdout
                assert not re.search(r"\b(?:error|warning):", p.stdout), p.stdout
                steps["ran"].append(log)
                if key:
                    core.store(key, outputs, p.stdout, origin)
                return p.stdout

            receipt["lean_version"] = run(["--version"], "version.log").strip()
            assert "version 4.29.1" in receipt["lean_version"]
            for name, data in sources.items():
                target = work / core.source_file(name)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
            for name in order:
                olean = core.source_file(name)[:-5] + ".olean"
                run(["-o", olean, core.source_file(name)], name + ".log", key=keys[name], outputs=[olean])
            audit = f"import {TARGET}\n" + "".join(f"#print axioms {d['name']}\n" for d in registry)
            signatures = f"import {TARGET}\n" + "".join(
                f"#check @{d['name']}\n" for d in registry if d["kind"] == "theorem")
            for label, text in [("AxiomAudit", audit), ("Signatures", signatures)]:
                (work / (TARGET + label + ".lean")).write_text(text)
            output = run([TARGET + "AxiomAudit.lean"], TARGET + "AxiomAudit.log",
                         key=core.step_key(context, TARGET + "AxiomAudit.lean", audit.encode(), keys),
                         driver=TARGET + "AxiomAudit.lean")
            run([TARGET + "Signatures.lean"], TARGET + "Signatures.log",
                key=core.step_key(context, TARGET + "Signatures.lean", signatures.encode(), keys),
                driver=TARGET + "Signatures.lean")
        dependencies = {}
        for item in registry:
            full = item["name"]
            if f"'{full}' does not depend on any axioms" in output:
                axioms = []
            else:
                match = re.search(r"'" + re.escape(full) + r"' depends on axioms:\s*\[([^]]*)\]", output)
                assert match, (full, output)
                axioms = [a.strip() for a in match[1].split(",") if a.strip()]
            assert set(axioms) <= STANDARD_AXIOMS, (full, axioms)
            dependencies[full] = axioms
        receipt["source_unchanged_during_check"] = all(
            paths[name].read_bytes() == data for name, data in sources.items())
        assert receipt["source_unchanged_during_check"], "Source changed; only snapshot checked"
        receipt["modules"] = [{
            "module": TARGET, "layer": "periphery instances",
            "theorems": sum(d["kind"] == "theorem" for d in registry),
            "declarations": registry, "axiom_dependencies": dependencies, "kernel_checked": True,
        }]
        receipt["artifact_sha256"] = {
            p.name: digest(p.read_bytes()) for p in sorted(retained.iterdir()) if p.is_file()}
        receipt["status"] = "passed"
    except Exception as error:
        receipt["status"] = "failed"
        receipt["error"] = str(error)
        raise
    finally:
        serialized = json.dumps(receipt, indent=2, ensure_ascii=False) + "\n"
        (retained / "verification.json").write_text(serialized)
        RECEIPT.write_text(serialized)
    used = sorted({a for axioms in receipt["modules"][0]["axiom_dependencies"].values() for a in axioms})
    print(json.dumps({"status": receipt["status"], "theorems": receipt["modules"][0]["theorems"],
                      "declaration_audits": len(registry), "axioms": used,
                      "inherited_modules": len(order) - 1,
                      "lean_steps_run": len(steps["ran"]), "lean_steps_reused": len(steps["reused"]),
                      "receipt": str(RECEIPT)}))


if __name__ == "__main__":
    main()
