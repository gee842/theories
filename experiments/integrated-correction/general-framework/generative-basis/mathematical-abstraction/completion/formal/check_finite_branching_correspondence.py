#!/usr/bin/env python3
"""Check the peripheral instance of the Becoming core's laws of lasting some course in the completion package's
finite-branching lifting.

`FiniteBranchingCorrespondence` imports `Becoming.Lasting` and `FiniteBranching`, the completion package's lifting
module (it imports `Std`; `check.py` in this folder checks the package under Lean 4.29.1). It is compiled with
Lean 4.30.0-rc2, as the other instance modules are, with the installed Mathlib on the path
(`SYSTEMS_MATHLIB_PROJECT`, default `~/repos/生生不息`), though it imports none. This checker follows
`check_continuation_correspondence.py`: module resolution, declaration scanning and passed-receipt matching are
those of the core checker, and every other module in the closure must match a passed receipt. The core's module
index covers its Lean root only, so `FiniteBranching` and this module are added from this folder, and
`FiniteBranching` matches the package receipt `verification.json`, which `check.py` writes only after every module
compiled fresh and every audit passed. Each declaration's axiom report is recorded: it may name only the standard
axioms (propext, Classical.choice, Quot.sound). The core does not import this module. Lean steps are reused as in
the core checker, keyed also by the Mathlib revision; `BECOMING_FRESH=1` runs every step. The run folder keeps the
receipt, the drivers and logs of the steps that ran, and a copy of each file `main` does not hold byte for byte.
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
LEAN_ROOT = HERE.parents[2] / "lean"
sys.path.insert(0, str(LEAN_ROOT / "becoming"))
import check_becoming as core  # noqa: E402

TARGET = "FiniteBranchingCorrespondence"
RECEIPT = HERE / "finite-branching-correspondence-verification.json"
RETAINED = HERE / "finite-branching-correspondence-checks"
TOOLCHAIN = "leanprover/lean4:v4.30.0-rc2"
LEAN = Path.home() / ".elan/toolchains/leanprover--lean4---v4.30.0-rc2/bin/lean"
MATHLIB_REVISION = "ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa"
EXTERNAL = {"Init", "Std", "Lean", "Mathlib"}
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
# The relation as a process and the correspondences of reaching, unboundedness and listed children must have empty
# reports. The other six take the classical steps FiniteBranching's statements need (excluded middle for
# `EitherThroughout`, Lean's choice for the selection); the core laws they instantiate have empty reports.
EMPTY = {"Becoming.FiniteBranchingCorrespondence." + n for n in
         ["process", "reach_iff_continues", "unbounded_iff", "finitelyBranching"]}
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")
# The completion package's receipt; see passed_receipts.
PACKAGE_RECEIPT = HERE / "verification.json"
# Seconds allowed for each Lean run; a heavily loaded machine may need more.
TIMEOUT = int(os.environ.get("LEAN_TIMEOUT", "900"))

SCOPE = (
    "On the Becoming core's laws of lasting some course: a relation is the process with one move "
    "whose steps are its pairs, and there FiniteBranching's Reach is the core's Lasting.Continues and "
    "its Unbounded the core's Lasting.Unbounded (reach_iff_continues, unbounded_iff), listed children "
    "making the process finitely branching (finitelyBranching). With Lean's classical reasoning "
    "supplying EitherThroughout (either_classical), the core's EitherThroughout.list and "
    "Lasting.Unbounded.step_of_either give finite_unbounded and unbounded_child; with Lean's choice "
    "selecting an unbounded successor, the core's Lasting.lifting and "
    "Lasting.unbounded_start_of_either give infinite_from_unbounded, finite_initial_lifting and "
    "labelled_lifting. The core shows that the unbounded successor, asked of every finitely branching "
    "process, is exactly EitherThroughout (Lasting.step_iff_either). FiniteBranching's statements "
    "keep their scope: a path's existence, not its effective selection or a physical infinity."
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
    # check.py in this folder writes its receipt only after every module compiled fresh and every audit passed;
    # it has no status field, so the receipt counts as passed when it says so.
    text = PACKAGE_RECEIPT.read_text()
    package = json.loads(text)
    if package["fresh_build"] is True and package["custom_axioms"] == [] and package["proof_holes"] is False:
        receipts.append((os.path.relpath(PACKAGE_RECEIPT, LEAN_ROOT), text))
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
    index = core.module_index()
    # The core indexes its Lean root only; FiniteBranching and this module sit in the completion package.
    for name in ("FiniteBranching", TARGET):
        assert name not in index, name
        index[name] = [HERE / (name + ".lean")]
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
    receipt = {
        "status": "checking", "utc": stamp, "toolchain": TOOLCHAIN,
        "mathlib_revision": MATHLIB_REVISION,
        "retained_run": str(retained.relative_to(HERE)),
        "bridge_module": TARGET, "compile_order": order,
        "source_paths": {name: os.path.relpath(paths[name], LEAN_ROOT) for name in order},
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
        assert TARGET not in core.closure(index, core.CORE), "the core imports the bridge"
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
        with tempfile.TemporaryDirectory(prefix="finite-branching-correspondence-") as scratch:
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
            "module": TARGET, "layer": "periphery bridge",
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
