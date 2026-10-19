#!/usr/bin/env python3
"""Duplicate and near-duplicate statements across the core."""
import json, re, os
from collections import defaultdict, Counter
H = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(H, "decls.json")))
ds = D["decls"]

TOK = re.compile(r"[A-Za-z_α-ωΑ-Ω][A-Za-z0-9_'!?₀-₉α-ω.]*|\d+|:=|->|→|↔|∀|∃|∧|∨|¬|≤|<|≥|>|=|≠|\S")
PRELUDE = set("""Nat List Prop Type Sort Bool True False Option Fin Int String Unit PUnit Subtype Exists And Or Not Iff Eq Ne
fun λ let have show by at with from in if then else match do Decidable DecidableEq DecidablePred Function some none
nil cons length map filter sum succ zero ite id comp Prod fst snd Sigma PSigma Empty True.intro inl inr Sum
""".split())
global_last = Counter()
for d in ds:
    if d["name"]:
        global_last[d["name"].split(".")[-1]] += 1
GLOBALS = set(global_last)

def binder_split(stmt, name):
    # remove "theorem name"
    s = stmt
    m = re.match(r"^(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable)\s+)*\w+\s+\S+", s)
    if m: s = s[m.end():]
    return s

def norm(stmt, name, mode):
    s = binder_split(stmt, name)
    toks = TOK.findall(s)
    ren = {}
    out = []
    for t in toks:
        if re.match(r"[A-Za-z_α-ωΑ-Ω]", t):
            last = t.split(".")[-1] if "." in t else t
            if t in PRELUDE or last in PRELUDE:
                out.append(last); continue
            is_global = ("." in t) or (t in GLOBALS)
            if mode == "exact":
                if is_global:
                    out.append(last); continue
                key = t
            else:  # shape: rename everything non-prelude
                key = last
            if key not in ren: ren[key] = "v%d" % len(ren)
            out.append(ren[key])
        else:
            out.append(t)
    return " ".join(out)

th = [d for d in ds if d["kind"] == "theorem"]
res = {}
for mode in ("exact", "shape"):
    groups = defaultdict(list)
    for d in th:
        k = norm(d["stmt"], d["name"], mode)
        d["n_" + mode] = k
        groups[k].append(d)
    multi = {k: v for k, v in groups.items() if len(v) > 1}
    cross = {k: v for k, v in multi.items() if len(set(x["module"] for x in v)) > 1}
    res[mode] = (multi, cross)
    ntoks = lambda k: len(k.split())
    print("==", mode, "groups>1:", len(multi), "decls in them:", sum(len(v) for v in multi.values()),
          "cross-module groups:", len(cross), "decls:", sum(len(v) for v in cross.values()))
    big = {k: v for k, v in cross.items() if ntoks(k) >= 25}
    print("   cross-module groups with >=25 tokens:", len(big), "decls:", sum(len(v) for v in big.values()),
          "removable (decls - groups):", sum(len(v) - 1 for v in big.values()))

json.dump({mode: [[{"full": x["full"], "module": x["module"], "line": x["line"]} for x in v] + [k]
                  for k, v in sorted(res[mode][1].items(), key=lambda kv: -len(kv[0].split()))]
           for mode in res}, open(os.path.join(H, "dup_groups.json"), "w"), ensure_ascii=False, indent=0)
