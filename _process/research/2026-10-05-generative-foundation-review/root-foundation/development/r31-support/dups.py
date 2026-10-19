#!/usr/bin/env python3
"""R31: theorems whose statements use only Lean's prelude, and the statements proved more than once.

Parses the core's declarations (R30's parser, `development/r30-names/parse.py`, on this checkout),
keeps the theorems whose statement names only prelude types and their usual operations (the strict
test of the twentieth review's `scripts/A/arith2.py`), renames bound names in order, and groups equal
statements. Prints the groups proved in more than one place; `--json` writes them to stdout.
"""
import collections
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("r30parse", HERE.parent / "r30-names" / "parse.py")
parse = importlib.util.module_from_spec(spec)
spec.loader.exec_module(parse)
ROOT = Path(parse.ROOT)

OK = {"Nat", "Int", "List", "Bool", "Prop", "Option", "Type", "True", "False", "Unit", "Iff", "Eq", "Or",
      "And", "Not", "Exists", "Decidable", "DecidableEq"}
LM = {"map", "length", "sum", "filter", "all", "any", "append", "reverse", "foldl", "foldr", "head", "tail",
      "contains", "succ", "beq", "ble", "find?", "bind", "some", "none", "inl", "inr", "mem", "zero", "one",
      "sub", "add", "mul", "isSome", "isEmpty", "flatten", "flatMap", "getD", "get?", "replicate", "range",
      "take", "drop", "zip", "pow", "div", "mod", "max", "min", "true", "false", "decide", "not", "and", "or"}
KW = {"fun", "by", "rfl", "at", "with", "match", "if", "then", "else", "let", "in", "have", "show", "from",
      "exact", "intro", "theorem", "decide"}


def declarations():
    out = []
    for path in sorted(ROOT.glob("*.lean")):
        ds, _ = parse.parse(str(path))
        out.extend(ds)
    return out


def body(d):
    st = re.sub(r"^\s*(@\[[^\]]*\]\s*)?((private|protected)\s+)*theorem\s+\S+", "", d["stmt"])
    return re.sub(r"\s+", " ", st).strip()


CONST = {"true", "false", "id", "min", "max"}
IDENT = re.compile(r"(?<![\w.'])([A-Za-zα-ωΑ-Ω_][\w']*(?:\.[\w?']+)*)")


def bound(b):
    """Names bound in the statement: binder groups and the variables after ∀, ∃, fun."""
    names = set()
    for group in re.findall(r"[({\[]\s*([^(){}\[\]:]+?)\s*:", b):
        names.update(w for w in group.split() if re.fullmatch(r"[\w']+", w))
    for group in re.findall(r"(?:∀|∃|fun|λ)\s+([^,:=]+?)\s*(?:,|:|=>)", b):
        names.update(w for w in re.findall(r"[\w']+", group))
    return names


def prelude_only(d):
    b = body(d)
    bnd = bound(b)
    for tok in IDENT.findall(b):
        head, _, rest = tok.partition(".")
        if head in KW or head in CONST:
            continue
        if head in OK:
            continue
        if head in bnd:
            if rest and rest.split(".")[0] not in LM:
                return False
            continue
        if head.isupper() or head[0].isupper():
            return False
        return False  # an unbound lower-case word is a module's constant
    return True


def norm(d):
    b = body(d)
    bnd = bound(b)
    names = {}

    def rep(m):
        tok = m.group(1)
        head, dot, rest = tok.partition(".")
        if head not in bnd:
            return tok
        names.setdefault(head, "v%d" % len(names))
        return names[head] + dot + rest

    return IDENT.sub(rep, b)


def groups(ds=None):
    ds = ds if ds is not None else declarations()
    th = [d for d in ds if d["kind"] == "theorem" and not d.get("private") and prelude_only(d)]
    g = collections.defaultdict(list)
    for d in th:
        g[norm(d)].append(d)
    multi = {k: v for k, v in g.items() if len(v) > 1}
    return th, multi


def main():
    th, multi = groups()
    rows = sorted(multi.items(), key=lambda kv: (-len(kv[1]), kv[1][0]["full"]))
    if "--json" in sys.argv:
        print(json.dumps([{"statement": k, "copies": [{"full": d["full"], "module": d["module"],
                                                       "line": d["line"]} for d in v]} for k, v in rows],
                         indent=1, ensure_ascii=False))
        return
    print(f"prelude-only theorems {len(th)}; statements proved more than once {len(rows)}, "
          f"{sum(len(v) for _, v in rows)} theorems, {sum(len(v) - 1 for _, v in rows)} copies beyond one")
    for k, v in rows:
        print(len(v), " ".join(f"{d['full']}@{d['module'][9:]}:{d['line']}" for d in v), "|", k[:120])


if __name__ == "__main__":
    main()
