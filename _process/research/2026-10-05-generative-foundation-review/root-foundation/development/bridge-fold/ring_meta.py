#!/usr/bin/env python3
"""F3 sweep planner on Lean's constant graph: what leaves the package when periphery modules retire.

Usage (from the repository root):
  ring_meta.py build OUT            build every BRIDGE and PERIPHERY_JOINS module in scratch (OUT/tree,
                                    steps from the shared cache) and write OUT/ring-meta.json: every
                                    constant of those modules, the constants its type and value use, and
                                    the module of each
  ring_meta.py plan OUT MODULE ...  read OUT/ring-meta.json and print the plan for retiring MODULE ...
                                    (with the checker's SUPERSEDED register); changes nothing

A ring constant's reach is the set of periphery modules whose constants its type or value uses, directly
or through other ring constants. A source declaration of the ring goes when its reach is not empty and
lies inside the retired set. A ring constant that reaches no periphery module goes when it was used by a
constant that goes and no constant that stays uses it. A ring file goes whole when none of its source
declarations stays; files importing it drop the import. The plan reports, for each retired module, the
ring files that still import it (each must drop the import or the module stays in the run), the
periphery modules in the run that import it, and the records and chapter lines naming a declaration that
goes. The core checker decides whether the plan holds.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()
LEAN = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean"
PKG = LEAN / "becoming"
CHECKER = PKG / "check_becoming.py"
TOOLS = Path(__file__).resolve().parent / "tools"
FOUNDATION = {"GenerativeCore", "InquirySufficiency", "RelationalRenewal"}


def lists():
    src = CHECKER.read_text()
    out = {}
    for name in ("CORE", "BRIDGE", "PERIPHERY_JOINS"):
        m = re.search(r"^" + name + r"\s*=\s*\[(.*?)\]", src, re.M | re.S)
        out[name] = re.findall(r'"([^"]+)"', m.group(1))
    m = re.search(r"^SUPERSEDED\s*=\s*\{(.*?)^\}", src, re.M | re.S)
    out["SUPERSEDED"] = re.findall(r'^\s*"([^"]+)"\s*:', m.group(1), re.M) if m else []
    return out


def build(out):
    out = Path(out).resolve()
    tree = out / "tree"
    tree.mkdir(parents=True, exist_ok=True)
    L = lists()
    ring = L["BRIDGE"] + L["PERIPHERY_JOINS"]
    (tree / "RingImports.lean").write_text("".join("import " + m + "\n" for m in ring))
    meta = (TOOLS / "BridgeMeta.lean").read_text()
    meta = meta.replace("import BridgeInventoryImports", "import RingImports")
    meta = meta.replace('"BridgeInventoryImports.lean"', '"RingImports.lean"').replace('"bridge-meta.json"', '"ring-meta.json"')
    subprocess.run([sys.executable, "-B", str(PKG / "scratch_build.py"), str(tree), "RingImports"], check=True)
    build_dir = tree / ".build"
    (build_dir / "RingImports.lean").write_text((tree / "RingImports.lean").read_text())
    (build_dir / "RingMeta.lean").write_text(meta)
    lean = subprocess.run(["elan", "which", "lean"], cwd=PKG, text=True, capture_output=True, check=True).stdout.strip()
    subprocess.run([lean, "RingMeta.lean"], cwd=build_dir, env={"LEAN_PATH": str(build_dir), "PATH": "/usr/bin:/bin"}, check=True)
    (out / "ring-meta.json").write_bytes((build_dir / "ring-meta.json").read_bytes())
    print("wrote", out / "ring-meta.json")


def source_names(module):
    """Full names of the declarations written in a ring module's source (namespaces followed)."""
    text = (PKG / (module.replace(".", "/") + ".lean")).read_text()
    names, stack = set(), []
    for line in text.split("\n"):
        ns = re.match(r"^namespace\s+(\S+)", line)
        if ns:
            stack.extend(ns.group(1).split("."))
            continue
        en = re.match(r"^end\s+(\S+)", line)
        if en:
            parts = en.group(1).split(".")
            if stack[-len(parts):] == parts:
                del stack[-len(parts):]
            continue
        m = re.match(r"^(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable)\s+)*"
                     r"(?:theorem|lemma|def|abbrev|structure|inductive|instance|class)\s+([^\s:({\[]+)", line)
        if m:
            names.add(".".join(stack + [m.group(1)]))
    return names


def plan(out, named):
    L = lists()
    ring = L["BRIDGE"] + L["PERIPHERY_JOINS"]
    core = set(L["CORE"])
    retired = set(L["SUPERSEDED"]) | set(named)
    data = json.loads((Path(out) / "ring-meta.json").read_text())
    mods = data["modules"]
    info = {d["name"]: d for d in data["decls"]}
    for n, d in info.items():
        mods.setdefault(n, d["module"])

    def layer(mod):
        top = mod.split(".")[0]
        if top in ("Init", "Std", "Lean"):
            return "prelude"
        if mod in FOUNDATION:
            return "foundation"
        if mod in core:
            return "core"
        if mod in ring:
            return "ring"
        return "periphery"

    uses = {n: set(d["type"]) | set(d["value"]) for n, d in info.items()}
    memo = {n: {mods[c] for c in uses[n] if layer(mods.get(c, "?")) == "periphery"} for n in info}
    ring_uses = {n: {c for c in uses[n] if c in info and c != n and layer(mods.get(c, "?")) == "ring"} for n in info}
    changed = True
    while changed:
        changed = False
        for n in info:
            new = memo[n].union(*(memo[c] for c in ring_uses[n])) if ring_uses[n] else memo[n]
            if new != memo[n]:
                memo[n] = new
                changed = True
    sources = {m: source_names(m) for m in ring}
    source_of = {n: m for m, ns in sources.items() for n in ns}
    users = {}
    for n, cs in uses.items():
        for c in cs:
            if c in info:
                users.setdefault(c, set()).add(n)
    going = {n for n in info if memo[n] and memo[n] <= retired}
    changed = True
    while changed:
        changed = False
        for n in info:
            if n in going or memo[n]:
                continue
            us = users.get(n, set()) - {n}
            if us and us <= going:
                going.add(n)
                changed = True
    staying = set(info) - going
    blocked = sorted((u, n) for n in going for u in users.get(n, set()) if u in staying)
    src_going = {m: sorted(n for n in sources[m] if n in going) for m in ring}
    src_unmatched = {m: sorted(n for n in sources[m] if n not in info) for m in ring}
    whole = sorted(m for m in ring if sources[m] and all(n in going for n in sources[m] if n in info))
    importers = {}
    for f in LEAN.rglob("*.lean"):
        if any(p.endswith("-checks") or p == "history" or p.startswith(".") for p in f.relative_to(LEAN).parts[:-1]):
            continue
        name = ".".join(f.relative_to(PKG).with_suffix("").parts) if PKG in f.parents else f.stem
        for imp in re.findall(r"^import\s+(\S+)", f.read_text(errors="ignore"), re.M):
            importers.setdefault(imp, set()).add(name)
    pinned = {}
    for r in sorted(retired):
        ring_imp = sorted(m for m in importers.get(r, ()) if m in ring and m not in whole)
        if ring_imp:
            pinned[r] = ring_imp
    still_reached = sorted({p for n in staying if n in source_of for p in memo[n]} & retired)
    named_going = {n for n in going if n in source_of}
    records = {}
    for rec in sorted((ROOT / "theories/becoming/results/records").glob("*.json")):
        live = json.dumps({k: v for k, v in json.loads(rec.read_text()).items() if k != "history"}, ensure_ascii=False)
        hit = sorted(n for n in named_going if n in live)
        if hit:
            records[rec.stem] = hit
    result = {
        "retired": sorted(retired),
        "source_declarations_going": {m: v for m, v in src_going.items() if v},
        "source_declarations_not_found_in_lean_data": {m: v for m, v in src_unmatched.items() if v},
        "whole_files": whole,
        "ring_files_importing_a_retired_module": pinned,
        "retired_modules_reached_by_staying_declarations": still_reached,
        "blocked": blocked[:200],
        "records_naming_going": records,
        "counts": {"constants_going": len(going), "source_declarations_going": len(named_going),
                   "theorems_going": sum(1 for n in named_going if info[n]["kind"] == "theorem")},
    }
    print(json.dumps(result, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    if sys.argv[1] == "build":
        build(sys.argv[2])
    else:
        plan(sys.argv[2], sys.argv[3:])
