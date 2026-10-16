#!/usr/bin/env python3
"""Fresh compilation and explicit-declaration audits for developmental learning recovery.

Uses the pinned installed Mathlib revision and rebuilds this repository module in
a fresh temporary directory. Actual source and compiler hashes bind the receipt.
Theorems do not establish population convergence, empirical correspondence or
normative validity. Adapted from the existing observation-repair checker.
"""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
CORE = HERE.parent.parent
REPO = next(p for p in HERE.parents if (p / "RESEARCH.md").is_file())
TARGETS = ["CalibratedUpdater"]
LEAN = Path(os.environ.get("LEAN", str(Path.home() / ".elan/toolchains/leanprover--lean4---v4.30.0-rc2/bin/lean")))
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")
ALLOWED = {"propext", "Quot.sound", "Classical.choice"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def code_without_comments(source):
    # These modules have no string literals containing comment delimiters.
    result, depth, i = [], 0, 0
    while i < len(source):
        if source.startswith("/-", i):
            depth += 1
            result.append("  ")
            i += 2
        elif depth and source.startswith("-/", i):
            depth -= 1
            result.append("  ")
            i += 2
        elif not depth and source.startswith("--", i):
            stop = source.find("\n", i)
            stop = len(source) if stop < 0 else stop
            result.append(" " * (stop - i))
            i = stop
        else:
            result.append(source[i] if not depth or source[i] == "\n" else " ")
            i += 1
    assert depth == 0, "unterminated comment"
    return "".join(result)


def closure():
    ordered, seen = [], set()

    def visit(module):
        if module in seen or module.split(".")[0] in {"Init", "Std", "Lean", "Mathlib"}:
            return
        matches = [p / (module.replace(".", "/") + ".lean") for p in [HERE, HERE.parent, CORE, CORE / "universal-ethics/generative-capacity", CORE.parent / "mathematical-abstraction/acquisition/feedback/remaining-dependency/formal"]
                   if (p / (module.replace(".", "/") + ".lean")).is_file()]
        matches = list(dict.fromkeys(matches))
        assert len(matches) == 1, (module, matches)
        path = matches[0]
        data = path.read_bytes()
        code = code_without_comments(data.decode())
        seen.add(module)
        for line in re.findall(r"^import (.+)$", code, re.M):
            for dependency in line.split():
                visit(dependency)
        namespaces = re.findall(r"^namespace (\S+)\s*$", code, re.M)
        assert len(namespaces) == 1, (module, namespaces)
        declarations = re.findall(r"^(def|theorem|lemma|structure|inductive|abbrev|instance)\s+([\w.]+)", code, re.M)
        assert declarations, module
        assert not re.search(r"\b(?:sorry|admit|axiom|opaque|unsafe|native_decide|implemented_by|skipKernelTC)\b", code), module
        ordered.append({"module": module, "path": path, "data": data,
                        "declarations": [{"kind": k, "name": namespaces[0] + "." + n}
                                         for k, n in declarations]})

    for module in TARGETS:
        visit(module)
    return ordered


def main():
    sources = closure()
    checker = Path(__file__).read_bytes()
    compiler = LEAN.resolve().read_bytes()
    version = subprocess.check_output([str(LEAN), "--version"], text=True).strip()
    assert "version 4.30.0-rc2," in version, version
    run = HERE / "calibrated-updater-checks" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    (run / "sources").mkdir(parents=True)
    (run / Path(__file__).name).write_bytes(checker)
    (run / "lean-toolchain").write_text("leanprover/lean4:v4.30.0-rc2\n")
    for entry in sources:
        (run / "sources" / (entry["module"] + ".lean")).write_bytes(entry["data"])
    names = [d["name"] for s in sources for d in s["declarations"]]
    assert len(names) == len(set(names)), "duplicate explicit declaration"
    audit_source = "\n".join("import " + target for target in TARGETS) + "\n\n"
    audit_source += "\n".join("#print axioms " + name for name in names) + "\n"
    (run / "CalibratedUpdaterAudit.lean").write_text(audit_source)
    commands, outputs = [], {}
    import_fingerprints = {}
    with tempfile.TemporaryDirectory(prefix="calibrated-updater-") as temporary:
        stage = Path(temporary)
        project = Path(os.environ.get("SYSTEMS_MATHLIB_PROJECT", str(Path.home() / "repos/生生不息")))
        manifest = (project / "lake-manifest.json").read_bytes()
        packages = project / json.loads(manifest).get("packagesDir", ".lake/packages")
        revision = "ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa"
        assert next(x for x in json.loads(manifest)["packages"] if x["name"] == "mathlib")["rev"] == revision
        assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=packages / "mathlib", text=True).strip() == revision
        assert (packages / "mathlib/lean-toolchain").read_text().strip() == "leanprover/lean4:v4.30.0-rc2"
        libraries = sorted(p / ".lake/build/lib/lean" for p in packages.iterdir() if (p / ".lake/build/lib/lean").is_dir())
        environment = dict(os.environ, LEAN_PATH=":".join([str(stage)] + [str(p) for p in libraries]))
        (run / "lake-manifest.json").write_bytes(manifest)
        for entry in sources:
            (stage / (entry["module"] + ".lean")).write_bytes(entry["data"])
        (stage / "CalibratedUpdaterAudit.lean").write_text(audit_source)

        def execute(args, label):
            command = [str(LEAN)] + args
            commands.append(command)
            result = subprocess.run(command, cwd=stage, env=environment,
                                    capture_output=True, text=True, timeout=300)
            output = result.stdout + result.stderr
            outputs[label] = output
            (run / label).write_text(output)
            assert result.returncode == 0, output
            assert "warning:" not in output and "error:" not in output, output
            return output

        for entry in sources:
            module = entry["module"]
            execute(["-o", module + ".olean", module + ".lean"], module + ".txt")
            print(json.dumps({"module": module, "compiled": True}), flush=True)
        audit_output = execute(["CalibratedUpdaterAudit.lean"], "axioms.txt")
        for entry in sources:
            result = subprocess.run([str(LEAN), "--deps", entry["module"] + ".lean"], cwd=stage, env=environment, capture_output=True, text=True, timeout=60)
            assert result.returncode == 0, result.stdout + result.stderr
            for line in result.stdout.splitlines():
                path = Path(line.strip())
                if path.is_file():
                    label = path.name if path.is_relative_to(stage) else str(path)
                    import_fingerprints[label] = sha(path.read_bytes())
    audited = AUDIT.findall(audit_output)
    assert [n for n, _ in audited] == names, "missing or reordered audit"
    dependencies = {n: [a.strip() for a in values.split(",") if a.strip()] for n, values in audited}
    assert all(set(a) <= ALLOWED for a in dependencies.values()), dependencies
    changed = [str(s["path"].relative_to(REPO)) for s in sources if s["path"].read_bytes() != s["data"]]
    assert not changed, changed
    assert Path(__file__).read_bytes() == checker and LEAN.resolve().read_bytes() == compiler
    assert (project / "lake-manifest.json").read_bytes() == manifest
    rows = [{"module": s["module"], "source": str(s["path"].relative_to(REPO)),
             "source_sha256": sha(s["data"]), "declarations": s["declarations"],
             "audits": len(s["declarations"]),
             "theorems": sum(d["kind"] in {"theorem", "lemma"} for d in s["declarations"]),
             "nonempty_audits": {d["name"]: dependencies[d["name"]] for d in s["declarations"]
                                 if dependencies[d["name"]]}} for s in sources]
    record = {"checked_at_utc": datetime.now(timezone.utc).isoformat(), "status": "passed",
              "lean_version": version, "compiler_sha256": sha(compiler),
              "targets": TARGETS, "snapshot": str(run.relative_to(REPO)),
              "modules": rows, "total_audits": len(audited),
              "new_audits": sum(s["audits"] for s in rows if s["module"] in TARGETS),
              "new_theorems": sum(s["theorems"] for s in rows if s["module"] in TARGETS),
              "nonempty_audits": {n: a for n, a in dependencies.items() if a},
              "checker_sha256": sha(checker), "commands": commands,
              "log_sha256": {k: sha(v.encode()) for k, v in outputs.items()},
              "source_changed_during_run": changed,
              "direct_import_sha256": import_fingerprints,
              "mathlib_revision": revision, "manifest_sha256": sha(manifest),
              "upstream_scope": "Pinned existing Mathlib cache; repository import closure rebuilt. Mathlib not rebuilt.",
              "scope": "Acquired affine-channel calibration, local report composition, paid gate formation and network-rule correspondence; "
                       "explicit declarations audited, generated declarations kernel-checked. "
                       "Supplied affine channels, bound zero/one references, local component laws, assembly plan, construction stock and operational support. Exact correspondence under stable nonzero gain; constant-channel, missing-contact, underfunding and changed-channel limits. No empirical, metrological, population or ethical certification."}
    (run / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    (HERE / "calibrated-updater-verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({k: record[k] for k in ["status", "total_audits", "new_audits", "new_theorems", "snapshot"]}))


if __name__ == "__main__":
    main()
