#!/usr/bin/env python3
"""Check the peripheral instances of the Becoming core's copying laws in the copy machines.

`CopyingInstances` imports the core module `Becoming.Copying` and the four peripheral copy
machines (`RecurrentAssembly`, `StructuralCopying`, `CopyingRegistration`, `CopyingCorrection`,
the last importing the others). Their definitions use standard axioms through library
instances, so these instances are stated here rather than in the pure core, and their
declarations may depend on `propext`, `Quot.sound` and `Classical.choice` only. The module is
compiled with Lean 4.29.1 and no Mathlib, as the core is. Module resolution, declaration
scanning, passed-receipt matching and the Lean step cache are those of the core checker; every
other module in the closure must match a passed receipt, so the core checker runs first. The
core does not import this module. `BECOMING_FRESH=1` runs every step. The run folder keeps the
receipt, the drivers and logs of the steps that ran, and a copy of each file `main` does not
hold byte for byte.
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

TARGET = "CopyingInstances"
RECEIPT = HERE / "copying-instances-verification.json"
RETAINED = HERE / "copying-instances-checks"
TOOLCHAIN = "leanprover/lean4:v4.29.1"
LEAN = Path.home() / ".elan/bin/lean"
BINARY = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
EXTERNAL = {"Init", "Std", "Lean"}
STANDARD_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}
# Seconds allowed for each Lean run; a heavily loaded machine may need more.
TIMEOUT = int(os.environ.get("LEAN_TIMEOUT", "900"))

SCOPE = (
    "Instances of the Becoming core's copying laws in the constructed copy machines. Structural "
    "copying: one machine move is one core move with first draw 1 and local draws; a template "
    "strand is copied exactly when the pool holds each token as often as the strand uses it and the "
    "support covers the draws, and released exactly when it also covers one unit, for every pool; "
    "the old support law is the instance with the template's tokens in the pool; every strand of a "
    "batch from one pool is released exactly when the pool supplies them together and the support "
    "covers all draws and releases, kept under adjacent exchange; every reproduction of a lineage of "
    "n is released exactly when the pool holds each token n times as often as the strand uses it and "
    "the support covers n times its draws and release, exactly when the support used is n times "
    "that, the converse of finite_lineage_inherits (on the strands alone it is false); the ranking and the third-strand "
    "constraint are instances of the local-draw laws. Chain growth: end attachment is the core copy "
    "of the alternating word with unit draws; the mature chain forms exactly when the pool holds at least "
    "four of each kind and eight units are free; attachment keeps the bonds the path on the tokens, "
    "so both hold bonds included; n rounds from k mature chains reach k * 2 ^ n exactly when "
    "the support covers 9 * required n k, exactly when the core doubling process with draw 9 runs. "
    "Registration: operating extends the product by a word exactly when each site reads its token "
    "through the actual contacts, the pool supplies it and the support covers what it draws; complete "
    "registration is the instance; every course keeps the product's bonds the path on its tokens, so "
    "complete registration copies the template, bonds included, exactly when its bonds are that path; "
    "the product only grows; only copy moves change it; the totals are "
    "kept. Correction: inspection never increases the defects for any copy exactly when the reference "
    "agrees with the template at the site; scans of such sites never increase them; the single-site "
    "criterion is an instance; the old wrong reference is unfaithful at the inspected site. "
    "Correspondence of these machines to molecular copying, proofreading or growth is not checked."
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
        with tempfile.TemporaryDirectory(prefix="copying-instances-") as scratch:
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
