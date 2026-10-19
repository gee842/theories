#!/usr/bin/env python3
"""Check the peripheral instances of the Becoming core's laws in constructed machines.

`MachineInstances` imports the core's `Becoming.Assurance`, `Segmentation`, `Readout` and `Gated`, the
periphery modules the pure bridge `Becoming.Instances` gave it (`WisdomResponseStructure`,
`RelationalReduction`, `OrganizationalRuleInheritance`, `AcquiredSegmentation`; the bridge is in
`lean/history/becoming/` since the F3 sweep), the core's
`Becoming.CrossSituational` and four peripheral machine modules (`EncounterChoice`, `RetrospectiveBinding`, `GoalFormationRevision`,
`JointPracticeContinuation`). Their definitions use standard axioms through library
instances, so these instances are stated here rather than in the core, and their
declarations may depend on `propext`, `Quot.sound` and `Classical.choice` only. The
module is compiled with Lean 4.29.1 and no Mathlib, as the core is. Module resolution,
declaration scanning, passed-receipt matching and the Lean step cache are those of the
core checker; every other module in the closure must match a passed receipt, so the core
checker runs first. The core does not import this module. `BECOMING_FRESH=1` runs every
step. The run folder keeps the receipt, the drivers and logs of the steps that ran, and a
copy of each file `main` does not hold byte for byte.
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
LEAN_ROOT = HERE.parents[1]
sys.path.insert(0, str(LEAN_ROOT / "becoming"))
import check_becoming as core  # noqa: E402

TARGET = "MachineInstances"
RECEIPT = HERE / "machine-instances-verification.json"
RETAINED = HERE / "machine-instances-checks"
TOOLCHAIN = "leanprover/lean4:v4.29.1"
LEAN = Path.home() / ".elan/bin/lean"
BINARY = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
EXTERNAL = {"Init", "Std", "Lean"}
STANDARD_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}
# Seconds allowed for each Lean run; a heavily loaded machine may need more.
TIMEOUT = int(os.environ.get("LEAN_TIMEOUT", "900"))

SCOPE = (
    "Instances of the Becoming core's laws in constructed peripheral machines. Reading acquired "
    "words: for every lexicon whose transition record groups the two-word encoding, every encoded "
    "sequence is interpreted as the assembly of its atoms exactly when each word form resolves to its "
    "atom (from Segmentation.reads_every_iff); the histories learned 32, coordinated 37, acquired 51, "
    "retrospective 36 and the fixed decoder of experienced 28 are instances, and the peripheral bond "
    "is the core's majority bond. Readout: the four-integer summary of the two-qubit fragment carries "
    "a law and is exact after every course of moves. Formed goal revision: a practice runs n cycles "
    "from an account exactly as the work covers the cycles the reserve does not support; every "
    "operation of the learning goal keeps the goal and selector and adds the transition loss if any; "
    "revision completes exactly under access loss with kept maintenance, after which n operations run "
    "exactly when n <= 5 (n <= 2 without reform) and the earlier loss is retained; the harmful headline "
    "is an instance. Gated change: the practice machine's traces are its completed runs, only "
    "revision changes the recorded methods and only an organizational adoption changes the rule. "
    "Cross-situational binding: for every lexicon whose repertoire has no repeats, a word resolves to "
    "its atom exactly when its admitted records separate the atom (CrossSituational.resolves_iff); "
    "after every history of an enacted scene every sequence is read exactly when the earlier records "
    "and those heard, each offering what was accessible where the learner stood, separate every atom "
    "(coordinated 37 is an instance; stationary 37 fails separation, mistimed 37 coverage); cooperative "
    "naming narrows exactly the words whose atoms are accessible; for every memory whose packets of a "
    "form are produced by learned worlds with the target, the binding view resolves the form to the "
    "target exactly when every other meaning is ruled out by a packet no learned world with it "
    "produces (retrospective 36 is an instance, and after a real route change the target is not "
    "produced). Learning is better than attendance exactly under access loss with kept maintenance, "
    "and revision completes exactly there. A practice round completes exactly when the worker is "
    "present and the reviewer is a present roster member other than the worker whose method answers "
    "as the context does, and then only records the review, trains the worker and completes the "
    "trial; the three rounds of the complete history are instances. "
    "Correspondence of these machines to actual learners, quantum systems, people or organizations "
    "is not checked."
)


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
    for path in LEAN_ROOT.rglob("*.json"):
        if path == RECEIPT or RETAINED in path.parents:
            continue
        text = path.read_text(errors="replace")
        if '"passed"' in text:
            receipts.append((str(path.relative_to(LEAN_ROOT)), text))
    return receipts


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    retained = RETAINED / stamp
    retained.mkdir(parents=True, exist_ok=False)
    index = core.module_index()
    order = closure(index)
    paths = {name: index[name][0] for name in order}
    sources = {name: paths[name].read_bytes() for name in order}
    helper_paths = [Path(__file__).resolve(), LEAN_ROOT / "becoming/check_becoming.py", HERE / "check.py"]
    helpers = {p.name: p.read_bytes() for p in helper_paths}
    commit, held = core.held_in_main({**{p: helpers[p.name] for p in helper_paths},
                                      **{paths[name]: sources[name] for name in order}})
    copied = {p.name: helpers[p.name] for p in helper_paths if p not in held}
    copied.update({name + ".lean": sources[name] for name in order if paths[name] not in held})
    for name, data in copied.items():
        (retained / name).write_bytes(data)
    digest = core.audit_support.digest
    receipt = {
        "status": "checking", "utc": stamp, "toolchain": TOOLCHAIN,
        "retained_run": str(retained.relative_to(HERE)),
        "instance_module": TARGET, "compile_order": order,
        "source_paths": {name: str(paths[name].relative_to(LEAN_ROOT)) for name in order},
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
        assert TARGET not in core.closure(index, core.CORE), "the core imports the instance module"
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
        with tempfile.TemporaryDirectory(prefix="machine-instances-") as scratch:
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
