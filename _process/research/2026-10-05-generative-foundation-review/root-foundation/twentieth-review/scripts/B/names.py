#!/usr/bin/env python3
"""Namespace collisions and duplicated definitions."""
import json, re, os
from collections import defaultdict, Counter
H = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(H, "decls.json")))
ds = D["decls"]
fulls = defaultdict(list)
for d in ds:
    fulls[d["full"]].append(d)

# 0. same full name declared in two modules (would fail to compile if both imported; possible if never co-imported)
same = {k: v for k, v in fulls.items() if len(set(x["module"] for x in v)) > 1}
print("same full name in >1 module:", len(same))
for k, v in list(same.items())[:40]:
    print("  ", k, [(x["module"], x["line"], x["kind"]) for x in v])

# 1. namespaces used in several modules
nsmods = defaultdict(lambda: defaultdict(list))
for d in ds:
    # every prefix that is a namespace
    if d["ns"]:
        nsmods[d["ns"]][d["module"]].append(d)
TYPES = ("structure", "inductive", "def", "abbrev", "class")
rows = []
for ns, mods in nsmods.items():
    if len(mods) < 2: continue
    owner = fulls.get(ns)
    # modules that define fresh types/defs inside ns
    fresh = {m: [x["name"] for x in v if x["kind"] in ("structure", "inductive")] for m, v in mods.items()}
    defs = {m: [x["name"] for x in v if x["kind"] in TYPES] for m, v in mods.items()}
    nfresh = sum(1 for m in fresh if fresh[m])
    rows.append((ns, bool(owner), owner[0]["module"] if owner else None, {m: len(v) for m, v in mods.items()}, nfresh, fresh, defs))
coll = [r for r in rows if not r[1]]
print("\nnamespaces in >=2 modules:", len(rows), " of which with no declaration of that name:", len(coll))
coll2 = [r for r in coll if r[4] >= 2]
print("  ... and with fresh structure/inductive in >=2 modules:", len(coll2))
for r in sorted(coll2, key=lambda r: -r[4]):
    print("  ", r[0], r[3], {m: f for m, f in r[5].items() if f})
coll3 = [r for r in coll if r[4] < 2 and sum(1 for m in r[6] if r[6][m]) >= 2]
print("\n  ... fresh defs (def/abbrev) in >=2 modules:", len(coll3))
for r in coll3:
    print("  ", r[0], r[3], {m: f[:6] for m, f in r[6].items() if f})
json.dump([list(r[:5]) for r in rows], open(os.path.join(H, "ns_rows.json"), "w"))
