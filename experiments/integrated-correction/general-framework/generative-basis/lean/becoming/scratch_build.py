#!/usr/bin/env python3
"""Build changed or new modules in scratch, sharing the checker's cache.

usage: python3 -B scratch_build.py TREE [MODULE ...]

TREE holds the modules a session changed or added, at their package paths
(`Becoming/Foo.lean` for `Becoming.Foo`; a module the checker finds by file name, such as
`GenerativeCore`, at TREE's top level). Every other module comes from this checkout.
MODULE names the modules to build and audit; by default every module in TREE.

The import closure is compiled in dependency order with the checker's Lean (`LEAN`, else
`elan which lean` in the package folder, else elan's default path), toolchain
and step keys (`check_becoming.step_key`), steps running concurrently as in the checker
(`BECOMING_JOBS`). A step whose inputs match a step that passed is restored from the
shared cache instead of run; a step that passes (exit 0, no error or warning) is stored
there, so the landing run and other sessions reuse it. Each named module's declarations
are audited, once it is compiled, with the checker's own `#print axioms` driver, cached
the same way; loading `import Lean` for an audit is left to the checker's environment
audit. This is a working build, not a receipt: nothing is retained, and the environment
audit, the controls and the prelude-only compile of the core run only in the checker.
Writes only into TREE/.build and the cache.
"""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import threading

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_becoming as cb  # noqa: E402

# Seconds allowed for each Lean run; a heavily loaded machine may need more.
TIMEOUT = int(os.environ.get("LEAN_TIMEOUT", "1800"))


def overlay(tree):
    """The modules in TREE by name, read from their paths below it."""
    found = {}
    for path in sorted(tree.rglob("*.lean")):
        relative = path.relative_to(tree)
        if not any(part.startswith(".") for part in relative.parts):
            found[".".join(relative.with_suffix("").parts)] = path
    return found


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        return 2
    tree = Path(sys.argv[1]).resolve()
    mine = overlay(tree)
    targets = sys.argv[2:] or sorted(mine)
    assert targets, ("no modules to build in", str(tree))
    index = cb.module_index()
    for name, path in mine.items():
        index[name] = [path]
    order = cb.closure(index, targets)
    sources = {name: index[name][0].read_bytes() for name in order}
    # The checker's Lean: `LEAN`, `elan which lean` in the package folder, or the default path.
    command, binary, _ = cb.resolve_lean()
    context = [cb.audit_support.TOOLCHAIN, cb.audit_support.digest(binary.read_bytes())]
    keys = cb.module_keys(context, sources, order)
    build = tree / ".build"
    origin = {"utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ"),
              "retained": "scratch build, not retained: " + str(tree)}
    report = {"tree": str(tree), "modules": len(order), "ran": [], "reused": 0, "unclean": [], "audits": {}}

    lock = threading.Lock()

    def step(args, label, key, outputs=()):
        """Restore a passed step or run it; store it when it passes. Returns the log, or
        None where Lean failed."""
        found = cb.reuse(key, [build / output for output in outputs])
        if found:
            with lock:
                report["reused"] += 1
            return found[0]
        p = subprocess.run(command + args, cwd=build, env={**os.environ, "LEAN_PATH": str(build)},
                           text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=TIMEOUT)
        with lock:
            report["ran"].append(label)
        if p.returncode != 0:
            with lock:
                print(p.stdout[-8000:], file=sys.stderr)
            return None
        if re.search(r"\b(?:error|warning):", p.stdout):
            with lock:
                report["unclean"].append(label)
                print(p.stdout[-8000:], file=sys.stderr)
        else:
            cb.store(key, [build / output for output in outputs], p.stdout, origin)
        return p.stdout

    class Failed(Exception):
        pass

    def checked(args, label, key, outputs=()):
        def action():
            output = step(args, label, key, outputs)
            if output is None:
                raise Failed(label)
            return output
        return action

    for name, data in sources.items():
        target = build / cb.source_file(name)
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.is_file() or target.read_bytes() != data:
            target.write_bytes(data)
    # Steps run concurrently as in the checker (`BECOMING_JOBS`), each once the compiles of
    # the modules it imports have passed; an audit waits for its module's compile.
    tasks, labels, registries = {}, [], {}
    for name in order:
        olean = cb.source_file(name)[:-5] + ".olean"
        tasks["compile " + name] = (["compile " + m for m in cb.imports_of(sources[name]) if m in keys],
                                    checked(["-o", olean, cb.source_file(name)], name, keys[name], [olean]))
        labels.append(name)
    for name in targets:
        flat = name.replace(".", "")
        registries[name] = cb.declarations(sources[name])
        audit = "import " + name + "\n" + "\n".join(
            "#print axioms " + item["name"] for item in registries[name]) + "\n"
        (build / (flat + "AxiomAudit.lean")).write_text(audit)
        tasks["audit " + name] = (["compile " + name],
                                  checked([flat + "AxiomAudit.lean"], flat + "AxiomAudit",
                                          cb.step_key(context, flat + "AxiomAudit.lean", audit.encode(), keys)))
        labels.append(flat + "AxiomAudit")
    try:
        outputs = cb.run_graph(tasks)
    except Failed as failure:
        report["failed"] = str(failure)
    report["ran"].sort(key=labels.index)
    report["unclean"].sort(key=labels.index)
    if "failed" in report:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 1
    for name in targets:
        registry, output = registries[name], outputs["audit " + name]
        axioms = {}
        for item in registry:
            full = item["name"]
            if "'" + full + "' does not depend on any axioms" in output:
                continue
            match = re.search(r"'" + re.escape(full) + r"' depends on axioms:\s*\[([^]]*)\]", output)
            axioms[full] = [a.strip() for a in match[1].split(",") if a.strip()] if match else ["not reported"]
        report["audits"][name] = {
            "theorems": sum(item["kind"] == "theorem" for item in registry),
            "declarations": len(registry), "with_axioms": axioms}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
