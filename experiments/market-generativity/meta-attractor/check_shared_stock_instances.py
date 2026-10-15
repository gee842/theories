#!/usr/bin/env python3
"""Check the peripheral instance of the Becoming core's law of listed masses in the draws on one
shared stock of `CorrectionDependence`.

`SharedStockInstances` imports `Becoming.Weighted` and `CorrectionDependence` (which uses Lean's
standard library and its tactics). It is compiled with Lean 4.30.0-rc2, as the other instance
modules of this directory are, with the installed Mathlib on the path (`SYSTEMS_MATHLIB_PROJECT`,
default `~/repos/生生不息`), though it imports none. This checker follows
`check_versioned_task_instances.py`: module resolution, declaration scanning and passed-receipt
matching are those of the core checker, with this directory's modules added to its index by file
name, and every other module in the closure must match a passed receipt (the core's or this
directory's). Each declaration's axiom report is recorded and must be empty (EMPTY). Neither the core nor any module of this directory imports
this one. Lean steps are reused as in the core checker, keyed also by the Mathlib revision;
`BECOMING_FRESH=1` runs every step. The run folder keeps the receipt, the drivers and logs of the
steps that ran, and a copy of each file `main` does not hold byte for byte.
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

TARGET = "SharedStockInstances"
RECEIPT = HERE / "shared-stock-instances-verification.json"
RETAINED = HERE / "shared-stock-instances-checks"
TOOLCHAIN = "leanprover/lean4:v4.30.0-rc2"
LEAN = Path.home() / ".elan/toolchains/leanprover--lean4---v4.30.0-rc2/bin/lean"
MATHLIB_REVISION = "ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa"
EXTERNAL = {"Init", "Std", "Lean", "Mathlib"}
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
# The instance adds no axiom: every declaration here must have an empty report.
EMPTY = {"SharedStockInstances." + n for n in
         ["firstDraws", "selectedTotal_eq_mass", "total_eq_mass",
          "every_selection_within_iff_total_within", "each_within_alone_not_together"]}
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")
# Seconds allowed for each Lean run; a heavily loaded machine may need more.
TIMEOUT = int(os.environ.get("LEAN_TIMEOUT", "900"))

SCOPE = (
    "An instance of the Becoming core's law of listed masses in CorrectionDependence's draws on one "
    "shared stock. The first n draws listed latest first are a domain, a selection is an event on it "
    "and the draws are its weighting: the selected total is the selection's mass and the total the "
    "whole domain's. So every selection fits within the stock exactly when the total does "
    "(every_selection_within_iff_total_within, from every_event_within_iff), and two draws of two "
    "each fitting a stock of two do not fit it together (each_within_alone_not_together, the "
    "whole domain's mass four). What a draw and the stock stand for keeps CorrectionDependence's "
    "scope; correspondence to actual activities and stocks is not checked."
)


def module_index():
    index = core.module_index()
    for path in sorted(HERE.glob("*.lean")):
        assert path.stem not in index, ("module name already in the core index", path.stem)
        index[path.stem] = [path]
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


def mathlib_path():
    project = Path(os.environ.get("SYSTEMS_MATHLIB_PROJECT", str(Path.home() / "repos/生生不息")))
    manifest = json.loads((project / "lake-manifest.json").read_text())
    packages = project / manifest.get("packagesDir", ".lake/packages")
    assert next(p for p in manifest["packages"] if p["name"] == "mathlib")["rev"] == MATHLIB_REVISION
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=packages / "mathlib",
                                   text=True).strip() == MATHLIB_REVISION
    assert (packages / "mathlib/lean-toolchain").read_text().strip() == TOOLCHAIN
    return [p / ".lake/build/lib/lean" for p in sorted(packages.iterdir())
            if (p / ".lake/build/lib/lean").is_dir()]


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    retained = RETAINED / stamp
    retained.mkdir(parents=True, exist_ok=False)
    index = module_index()
    order = closure(index)
    paths = {name: index[name][0] for name in order}
    sources = {name: paths[name].read_bytes() for name in order}
    helper_paths = [Path(__file__).resolve(), LEAN_ROOT / "becoming/check_becoming.py"]
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
        "mathlib_revision": MATHLIB_REVISION,
        "retained_run": str(retained.relative_to(HERE)),
        "instance_module": TARGET, "compile_order": order,
        "source_paths": {name: str(paths[name].relative_to(HERE.parents[1])) for name in order},
        "source_sha256": {name: digest(data) for name, data in sources.items()},
        "checker_sha256": {name: digest(data) for name, data in helpers.items()},
        # Files main holds byte for byte are named by this commit; the rest are copied here.
        "source_commit": {"main": commit, "copied": sorted(copied)},
        "scope": SCOPE,
    }
    # A reused step passed in the named run with the same binary and identical inputs; its log
    # stays in the cache under its key. Drivers and logs of the steps that ran are kept here.
    steps = receipt["lean_steps"] = {"cache": str(core.CACHE), "fresh": core.FRESH, "ran": [], "reused": {}, "keys": {}}
    try:
        assert TARGET not in core.closure(core.module_index(), core.CORE), "the core imports the instances"
        assert all(TARGET not in core.imports_of(path.read_bytes())
                   for path in HERE.glob("*.lean") if path.stem != TARGET), "a module here imports the instances"
        receipts = passed_receipts()
        matches = {}
        for name in order[:-1]:
            found = sorted(path for path, text in receipts if receipt["source_sha256"][name] in text)
            assert found, ("module has no passed receipt for its current bytes", name)
            matches[name] = found
        receipt["inherited_receipts"] = matches
        registry = core.declarations(sources[TARGET])
        receipt["lean_binary_sha256"] = digest(LEAN.read_bytes())
        context = [TOOLCHAIN, receipt["lean_binary_sha256"], MATHLIB_REVISION]
        keys = core.module_keys(context, sources, order)
        origin = {"utc": stamp, "retained": str(retained)}
        with tempfile.TemporaryDirectory(prefix="shared-stock-instances-") as scratch:
            work = Path(scratch)
            env = {**os.environ, "LEAN_PATH": ":".join([str(work)] + [str(p) for p in mathlib_path()])}

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
                p = subprocess.run([str(LEAN)] + args, cwd=work, env=env, text=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=TIMEOUT)
                (retained / log).write_text(p.stdout)
                assert p.returncode == 0, p.stdout
                assert not re.search(r"\b(?:error|warning):", p.stdout), p.stdout
                steps["ran"].append(log)
                if key:
                    core.store(key, outputs, p.stdout, origin)
                return p.stdout

            receipt["lean_version"] = run(["--version"], "version.log").strip()
            assert "version 4.30.0-rc2" in receipt["lean_version"]
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
        audited = {name: [a.strip() for a in values.split(",") if a.strip()]
                   for name, values in AUDIT.findall(output)}
        dependencies = {}
        for item in registry:
            assert item["name"] in audited, ("missing axiom audit", item["name"], output)
            found = audited[item["name"]]
            assert set(found) <= ALLOWED, (item["name"], found)
            assert not (item["name"] in EMPTY and found), ("must not depend on axioms", item["name"], found)
            dependencies[item["name"]] = found
        assert EMPTY <= set(dependencies), sorted(EMPTY - set(dependencies))
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
    print(json.dumps({"status": receipt["status"], "theorems": receipt["modules"][0]["theorems"],
                      "declaration_audits": len(registry),
                      "nonempty_audits": {k: v for k, v in dependencies.items() if v},
                      "inherited_modules": len(order) - 1,
                      "lean_steps_run": len(steps["ran"]), "lean_steps_reused": len(steps["reused"]),
                      "receipt": str(RECEIPT)}))


if __name__ == "__main__":
    main()
