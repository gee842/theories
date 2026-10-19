#!/usr/bin/env python3
"""Classify namespaces opened in several modules: extension (later content uses earlier) or collision."""
import json, re, os
from collections import defaultdict
H = os.path.dirname(os.path.abspath(__file__))
ROOT = "/Users/ren/theories/experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming"
D = json.load(open(os.path.join(H, "decls.json")))
ds = D["decls"]
imports = {}
for f in os.listdir(ROOT):
    if f.endswith(".lean"):
        m = "Becoming." + f[:-5]
        imports[m] = re.findall(r"^import\s+(\S+)", open(os.path.join(ROOT, f)).read(), re.M)
closure = {}
def clo(m):
    if m in closure: return closure[m]
    closure[m] = set()
    s = set()
    for i in imports.get(m, []):
        s.add(i); s |= clo(i)
    closure[m] = s
    return s
for m in imports: clo(m)
json.dump({m: sorted(v) for m, v in closure.items()}, open(os.path.join(H, "closure.json"), "w"))

fulls = set(d["full"] for d in ds)
byns = defaultdict(lambda: defaultdict(list))
for d in ds:
    if d["ns"]:
        byns[d["ns"]][d["module"]].append(d)
out = []
for ns, mods in byns.items():
    if len(mods) < 2 or ns in fulls: continue
    ms = list(mods)
    # names defined in ns per module (types/defs)
    defined = {m: set(x["name"] for x in mods[m] if x["kind"] in ("def", "abbrev", "structure", "inductive", "class")) for m in ms}
    pairs = []
    for a in ms:
        for b in ms:
            if a == b: continue
            if a in closure[b]:  # b imports a
                txt = " ".join(x["text"] for x in mods[b])
                uses = [n for n in defined[a] | set(x["name"] for x in mods[a]) if n and re.search(r"(?<![\w.])" + re.escape(n) + r"(?![\w'])", txt)]
                pairs.append((a, b, "imports", len(uses)))
    unrelated = [m for m in ms if not any(p[1] == m and p[3] > 0 for p in pairs) and not any(p[0] == m and p[3] > 0 for p in pairs)]
    indep = [(a, b) for i, a in enumerate(ms) for b in ms[i+1:] if a not in closure[b] and b not in closure[a]]
    out.append({"ns": ns, "mods": {m: len(v) for m, v in mods.items()}, "pairs": pairs, "not_co_imported": indep,
                "modules_sharing_nothing": unrelated})
coll = [o for o in out if o["modules_sharing_nothing"] and len(o["modules_sharing_nothing"]) >= 1 and (o["not_co_imported"] or any(p[3] == 0 for p in o["pairs"]))]
print("multi-module namespaces without an owning declaration:", len(out))
print("with at least one module whose content in it neither uses nor is used by another's:", len(coll))
for o in sorted(coll, key=lambda o: -len(o["mods"])):
    print(o["ns"], o["mods"], "| unrelated:", [m.replace("Becoming.", "") for m in o["modules_sharing_nothing"]])
json.dump(out, open(os.path.join(H, "ns_collisions.json"), "w"), indent=0)
