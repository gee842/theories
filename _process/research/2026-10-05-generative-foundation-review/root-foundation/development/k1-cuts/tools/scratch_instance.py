#!/usr/bin/env python3
"""Scratch-build PreparationCorrespondence with K1's workspace overlay (Becoming.Cuts and the
instance module), using check_preparation_correspondence's toolchain, Mathlib path and step cache.
A working build, not a receipt.

usage: python3 -B scratch_instance.py
"""
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
K1 = Path(__file__).resolve().parents[1]
LEAN_ROOT = Path(__file__).resolve().parents[7] / "experiments/integrated-correction/general-framework/generative-basis/lean"
sys.path.insert(0, str(LEAN_ROOT / "universal-ethics"))
import check_preparation_correspondence as cp  # noqa: E402

core = cp.core
OVERLAY = {"Becoming.Cuts": K1 / "Becoming/Cuts.lean",
           "PreparationCorrespondence": K1 / "PreparationCorrespondence.lean"}


def main():
    index = core.module_index()
    for name, path in OVERLAY.items():
        index[name] = [path]
    order = cp.closure(index)
    sources = {name: index[name][0].read_bytes() for name in order}
    lean_sha = core.audit_support.digest(cp.LEAN.read_bytes())
    context = [cp.TOOLCHAIN, lean_sha, cp.MATHLIB_REVISION]
    keys = core.module_keys(context, sources, order)
    ran, reused = [], 0
    with tempfile.TemporaryDirectory(prefix="k1-instance-") as scratch:
        work = Path(scratch)
        env = {**os.environ, "LEAN_PATH": ":".join([str(work)] + [str(p) for p in cp.mathlib_path()])}
        for name, data in sources.items():
            target = work / core.source_file(name)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)

        def run(args, key, outputs):
            nonlocal reused
            outs = [work / o for o in outputs]
            found = core.reuse(key, outs) if key else None
            if found:
                reused += 1
                return found[0]
            p = subprocess.run([str(cp.LEAN)] + args, cwd=work, env=env, text=True,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=cp.TIMEOUT)
            if p.returncode != 0 or re.search(r"\b(?:error|warning):", p.stdout):
                print(p.stdout)
                sys.exit(1)
            if key:
                core.store(key, outs, p.stdout, {"utc": "scratch", "retained": "k1 scratch"})
            ran.append(args[-1])
            return p.stdout

        for name in order:
            olean = core.source_file(name)[:-5] + ".olean"
            run(["-o", olean, core.source_file(name)], keys[name], [olean])
        registry = core.declarations(sources[cp.TARGET])
        audit = f"import {cp.TARGET}\n" + "".join(f"#print axioms {d['name']}\n" for d in registry)
        (work / "Audit.lean").write_text(audit)
        output = run(["Audit.lean"], None, [])
    audited = dict(cp.AUDIT.findall(output))
    new = [d["name"] for d in registry]
    print("ran", ran, "reused", reused)
    print("theorems", sum(d["kind"] == "theorem" for d in registry))
    for name in new:
        print(name, "|", audited.get(name, "MISSING") or "none")


if __name__ == "__main__":
    main()
