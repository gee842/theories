#!/usr/bin/env python3
"""One-line restatements: theorems whose proof is a single application of another theorem."""
import json, re, os
from collections import defaultdict, Counter
H = os.path.dirname(os.path.abspath(__file__))
ROOT = "/Users/ren/theories/experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming"
D = json.load(open(os.path.join(H, "decls.json")))
ds = D["decls"]
th = [d for d in ds if d["kind"] == "theorem"]
# name resolution by suffix
by_last = defaultdict(list)
for d in ds:
    parts = d["full"].split(".")
    for i in range(len(parts)):
        by_last[".".join(parts[i:])].append(d)
raw = {}
def docstring(d):
    f = os.path.join(ROOT, d["module"].split(".", 1)[1] + ".lean")
    if f not in raw: raw[f] = open(f, encoding="utf-8").read().split("\n")
    L = raw[f]
    i = d["line"] - 2
    buf = []
    while i >= 0 and L[i].strip() and not L[i].startswith(("theorem", "def", "end", "namespace")):
        buf.append(L[i]); i -= 1
        if L[i + 1].lstrip().startswith("/--"): break
    return "\n".join(reversed(buf))
ID = re.compile(r"[A-Za-z_α-ω][A-Za-z0-9_'!?₀-₉.]*")
KEYW = set("fun by exact simpa using at rfl _ mp mpr le lt symm trans elim intro left right inl inr fst snd show from have this".split())
res = []
for d in th:
    body = d["body"].strip()
    flat = " ".join(body.split())
    refs = []
    for t in ID.findall(flat):
        t2 = t.rstrip(".")
        cands = by_last.get(t2) or by_last.get(t2.rsplit(".", 1)[0] if "." in t2 else "", [])
        thm = [c for c in (cands or []) if c["kind"] == "theorem" and c["full"] != d["full"]]
        if thm: refs.append((t2, thm))
    short = len(flat) <= 140 and "match" not in flat and "induction" not in flat and "cases" not in flat and " | " not in flat
    head = re.match(r"^(?:by\s+(?:exact|simpa\s+using)\s+)?\(?\s*([A-Za-z_][\w'.]*)", flat)
    headthm = None
    if head:
        h = head.group(1)
        for k in (h, h.rsplit(".", 1)[0]):
            c = [x for x in by_last.get(k, []) if x["kind"] == "theorem" and x["full"] != d["full"]]
            if c: headthm = c; break
    distinct = set(r[0] for r in refs)
    kind = None
    if short and headthm and len(distinct) <= 2:
        tgt_mods = set(x["module"] for x in headthm)
        kind = "alias-same-module" if d["module"] in tgt_mods else "alias-other-module"
    elif short and flat.startswith("⟨") and 2 <= len(distinct) <= 4 and len(flat) <= 140:
        kind = "pair-of-theorems"
    doc = docstring(d) if kind else ""
    restated = bool(re.search(r"restat|as an instance|is the instance|the instance of|instance\b|read as|named case", doc))
    res.append({"full": d["full"], "module": d["module"], "line": d["line"], "kind": kind, "body": flat[:140],
                "target": [x["full"] for x in headthm][:2] if headthm else None, "doc_restated": restated})
json.dump(res, open(os.path.join(H, "wrappers.json"), "w"), indent=0, ensure_ascii=False)
c = Counter(r["kind"] for r in res)
print(c, "of", len(res))
print("doc says restated/instance among short:", sum(1 for r in res if r["kind"] and r["doc_restated"]))
per = defaultdict(Counter)
for r in res:
    per[r["module"]][r["kind"] or "proof"] += 1
rows = []
for m, cc in per.items():
    tot = sum(cc.values())
    w = cc["alias-other-module"] + cc["alias-same-module"] + cc["pair-of-theorems"]
    rows.append((w / tot, tot, w, cc["alias-other-module"], m))
rows.sort(reverse=True)
print("modules by share of one-line restatements (share, theorems, short, cross-module, module):")
for r in rows[:45]:
    print("  %.2f %4d %4d %4d %s" % r)
json.dump(rows, open(os.path.join(H, "wrapper_modules.json"), "w"))
