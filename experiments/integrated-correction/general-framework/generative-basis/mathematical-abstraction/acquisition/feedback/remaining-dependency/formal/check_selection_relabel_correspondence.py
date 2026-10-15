#!/usr/bin/env python3
"""Check the peripheral instance of the Becoming core's laws of selection by the record alone in PluralRecords and
TieBreaking.

`SelectionRelabelCorrespondence` imports `Becoming.Selection` and `TieBreaking`, which imports `PluralRecords`;
the two originals import only Lean's prelude and have no machine receipt (their build record is
`inquiry-warrant/BUILD.md`), so this checker compiles and audits them as well: every declaration of the
originals and of the instance must have an empty axiom report. It is compiled with Lean 4.30.0-rc2, as the other
instance modules are, with the installed Mathlib on the path (`SYSTEMS_MATHLIB_PROJECT`, default
`~/repos/生生不息`), though it imports none. This checker follows `check_continuation_correspondence.py`:
module resolution, declaration scanning and passed-receipt matching are those of the core checker, and every core
module in the closure must match a passed receipt. The core's module index covers its Lean root only, so the
originals and this module are added from this folder. The originals keep their bytes; the one warning they print,
the unused hypothesis `noWithhold` of `TieBreaking.full_tie_open_uniform`, kept as stated, is the only output
allowed beyond the audits. The core does not import this module. Lean steps are reused as in the core checker,
keyed also by the Mathlib revision; `BECOMING_FRESH=1` runs every step. The run folder keeps the receipt, the
drivers and logs of the steps that ran, and a copy of each file `main` does not hold byte for byte.
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
LEAN_ROOT = HERE.parents[4] / "lean"
sys.path.insert(0, str(LEAN_ROOT / "becoming"))
import check_becoming as core  # noqa: E402

TARGET = "SelectionRelabelCorrespondence"
RECEIPT = HERE / "selection-relabel-correspondence-verification.json"
RETAINED = HERE / "selection-relabel-correspondence-checks"
TOOLCHAIN = "leanprover/lean4:v4.30.0-rc2"
LEAN = Path.home() / ".elan/toolchains/leanprover--lean4---v4.30.0-rc2/bin/lean"
MATHLIB_REVISION = "ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa"
EXTERNAL = {"Init", "Std", "Lean", "Mathlib"}
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
# Every declaration of the instance adds no axiom: the originals' proofs were rewritten on 7 October 2026
# without classical reasoning, and the core laws they instantiate have empty reports. Each report must be empty.
EMPTY = {"Becoming.SelectionRelabelCorrespondence." + n for n in
         ["transpose_eq_swap", "treatsAlike_iff", "lotteryAlike_iff", "alone_iff", "tied_not_served_by_core", "first_lt", "all_tied_forces_withholding_by_core", "servable_iff_untied_by_core", "tied_equal_weight_by_core", "full_tie_equal_weights_by_core", "uniform_alike_by_core", "pointMass_one", "point_mass_not_alike_at_tie_by_core"]}
# Read anchored at the line's start, so a name ending in a prime is read whole.
AUDIT = re.compile(r"^'(.+?)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", re.M)
# The originals instantiated here: they import only the prelude and have no machine receipt, so this checker
# compiles and audits them, and every report must be empty.
ORIGINALS = ("PluralRecords", "TieBreaking")
# The one warning the originals print, kept as stated.
ALLOWED_WARNINGS = {"TieBreaking": "TieBreaking.lean:63:46: warning: unused variable `noWithhold`"}
# Seconds allowed for each Lean run; a heavily loaded machine may need more.
TIMEOUT = int(os.environ.get("LEAN_TIMEOUT", "900"))

SCOPE = (
    "On the Becoming core's laws of selection by the record alone (Becoming.Selection, Relabel): "
    "PluralRecords' records are the core's records of entries over the options Fin n, exchanging two "
    "centers is Relabel.swap, a rule treating the centers alike is a choice reading the record alone, "
    "a lottery treating them alike has weights reading the record alone, and holding an entry alone "
    "is Relabel.Alone. The core's laws give tied_not_served, all_tied_forces_withholding, "
    "servable_iff_untied (with PluralRecords.pick finding the center holding the entry alone), "
    "tied_equal_weight, full_tie_equal_weights, uniform_alike and point_mass_not_alike_at_tie, each "
    "with an empty axiom report. Whether an equal chance legitimately breaks a tie, and priority by "
    "claim size or by turn, keep the originals' scope."
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


def original_declarations(data):
    """The core scanner's rules, with `?`, `!` and `'` admitted in names, as the originals use them."""
    code = core.audit_support.code_only(data.decode())
    assert not re.search(r"\b(sorry|admit|axiom|unsafe|native_decide|implemented_by)\b|debug\.skipKernelTC", code), \
        "Proof escape in source"
    scopes, result = [], []
    for line in code.splitlines():
        scope = re.match(r"^(namespace|section)\b\s*(\S*)", line)
        if scope:
            scopes.append((scope[1], scope[2]))
            continue
        if re.match(r"^end(?:\s|$)", line):
            assert scopes, line
            scopes.pop()
            continue
        declaration = re.match(r"^(theorem|def|abbrev|structure|inductive|instance)\s+([\w.'?!]+)", line)
        if declaration:
            prefix = ".".join(n for kind, n in scopes if kind == "namespace")
            result.append({"kind": declaration[1],
                           "name": prefix + "." + declaration[2] if prefix else declaration[2]})
    assert not scopes and result
    assert len({item["name"] for item in result}) == len(result)
    return result


def passed_receipts():
    receipts = []
    for path in LEAN_ROOT.rglob("*.json"):
        if path == RECEIPT or RETAINED in path.parents:
            continue
        text = path.read_text(errors="replace")
        if '"passed"' in text:
            receipts.append((str(path.relative_to(LEAN_ROOT)), text))
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
    # The core indexes its Lean root only; the originals and this module sit in the remaining-dependency package.
    for name in ORIGINALS + (TARGET,):
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
        "checked_here": list(ORIGINALS) + [TARGET], "allowed_warnings": ALLOWED_WARNINGS,
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
            if name in ORIGINALS:
                continue
            found = sorted(path for path, text in receipts if receipt["source_sha256"][name] in text)
            assert found, ("module has no passed receipt for its current bytes", name)
            matches[name] = found
        receipt["inherited_receipts"] = matches
        registry = core.declarations(sources[TARGET])
        originals = {name: original_declarations(sources[name]) for name in ORIGINALS}
        audited_registry = registry + [d for name in ORIGINALS for d in originals[name]]
        empty = EMPTY | {d["name"] for name in ORIGINALS for d in originals[name]}
        receipt["lean_binary_sha256"] = digest(LEAN.read_bytes())
        context = [TOOLCHAIN, receipt["lean_binary_sha256"], MATHLIB_REVISION]
        keys = core.module_keys(context, sources, order)
        origin = {"utc": stamp, "retained": str(retained)}
        with tempfile.TemporaryDirectory(prefix="selection-relabel-correspondence-") as scratch:
            work = Path(scratch)
            env = {**os.environ, "LEAN_PATH": ":".join([str(work)] + [str(p) for p in mathlib_path()])}

            def run(args, log, key=None, outputs=(), driver=None, allowed=""):
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
                assert not re.search(r"\b(?:error|warning):", p.stdout.replace(allowed, "") if allowed else p.stdout), \
                    p.stdout
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
                run(["-o", olean, core.source_file(name)], name + ".log", key=keys[name], outputs=[olean],
                    allowed=ALLOWED_WARNINGS.get(name, ""))
            audit = f"import {TARGET}\n" + "".join(f"#print axioms {d['name']}\n" for d in audited_registry)
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
        for item in audited_registry:
            assert item["name"] in audited, ("missing axiom audit", item["name"], output)
            found = audited[item["name"]]
            assert set(found) <= ALLOWED, (item["name"], found)
            assert not (item["name"] in empty and found), ("must not depend on axioms", item["name"], found)
            dependencies[item["name"]] = found
        assert empty <= set(dependencies), sorted(empty - set(dependencies))
        receipt["source_unchanged_during_check"] = all(
            paths[name].read_bytes() == data for name, data in sources.items())
        assert receipt["source_unchanged_during_check"], "Source changed; only snapshot checked"
        receipt["modules"] = [{
            "module": TARGET, "layer": "periphery bridge",
            "theorems": sum(d["kind"] == "theorem" for d in registry),
            "declarations": registry,
            "axiom_dependencies": {d["name"]: dependencies[d["name"]] for d in registry}, "kernel_checked": True,
        }] + [{
            "module": name, "layer": "periphery original, checked here",
            "theorems": sum(d["kind"] == "theorem" for d in originals[name]),
            "declarations": originals[name],
            "axiom_dependencies": {d["name"]: dependencies[d["name"]] for d in originals[name]},
            "kernel_checked": True,
        } for name in ORIGINALS]
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
                      "declaration_audits": len(audited_registry),
                      "nonempty_audits": {k: v for k, v in dependencies.items() if v},
                      "inherited_modules": len(order) - 1,
                      "lean_steps_run": len(steps["ran"]), "lean_steps_reused": len(steps["reused"]),
                      "receipt": str(RECEIPT)}))


if __name__ == "__main__":
    main()
