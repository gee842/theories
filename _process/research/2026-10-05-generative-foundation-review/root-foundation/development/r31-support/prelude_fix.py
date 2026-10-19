#!/usr/bin/env python3
"""R31, item 3, second pass: uses of a removed name followed by a field (`and_eq_true.mp`).

prelude.py rewrote tokens naming a removed declaration; a token naming one with a projection or
a generalized field after it (`band_true_iff.trans`) was left. This pass rewrites the longest
prefix of each such token that resolves, in its namespace, to a name the table removes and to no
declaration now present, keeping the rest of the token.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import dups  # noqa: E402

PKG = dups.ROOT
TABLE = json.load(open(HERE / "dedup-table.json"))
DELETE = {x: g["keep"] for g in TABLE["groups"] for x in g["delete"]}
NOW = {d["full"] for d in dups.declarations()}
assert not (set(DELETE) & NOW), sorted(set(DELETE) & NOW)
IDENT = re.compile(r"(?<![\w.'?!])(@?)([A-Za-z_][\w'?!]*(?:\.[A-Za-z_][\w'?!]*)+)")


def resolve(tok, ns, names):
    parts = ns.split(".") if ns else []
    for i in range(len(parts), -1, -1):
        cand = ".".join(parts[:i] + [tok])
        if cand in names:
            return cand
    return None


def written(keep, ns):
    rel = keep[len("Becoming."):]
    return rel if ns.startswith("Becoming") and resolve(rel, ns, NOW) == keep else keep


DRY = "--dry" in sys.argv
for path in sorted(PKG.glob("*.lean")):
    lines = path.read_text().split("\n")
    stack, in_block, changed = [], 0, False
    for n, line in enumerate(lines):
        if not in_block:
            m = re.match(r"\s*namespace\s+(\S+)", line)
            if m:
                stack.append(m.group(1))
            if re.match(r"\s*section\b", line):
                stack.append(None)
        ns = ".".join(x for x in stack if x)
        code_start = in_block
        in_block += line.count("/-") - line.count("-/")
        if code_start:
            continue
        code = line.split("--")[0]

        def rep(mt):
            at, tok = mt.group(1), mt.group(2)
            parts = tok.split(".")
            for k in range(len(parts) - 1, 0, -1):
                head = ".".join(parts[:k])
                if resolve(head, ns, NOW):
                    return mt.group(0)
                parts_ns = ns.split(".") if ns else []
                for i in range(len(parts_ns), -1, -1):
                    cand = ".".join(parts_ns[:i] + [head])
                    if cand in DELETE:
                        new = written(DELETE[cand], ns) + "." + ".".join(parts[k:])
                        print(f"{path.name}:{n + 1}\t{tok}\t{new}")
                        return at + new
            return mt.group(0)

        new = IDENT.sub(rep, code) + line[len(code):]
        if new != line:
            lines[n] = new
            changed = True
        if re.match(r"\s*end\b", line) and stack:
            stack.pop()
    if changed and not DRY:
        path.write_text("\n".join(lines))
