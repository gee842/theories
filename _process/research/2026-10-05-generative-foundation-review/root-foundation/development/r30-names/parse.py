import os
#!/usr/bin/env python3
"""Parse declarations of the Becoming core (read-only). Output decls.json (not kept in the repository: it is this
script's output on R29's core, 19 MB; set R30_CORE to an export of 4cc010fb0's Becoming folder to regenerate it)."""
import json, re, os, sys

ROOT = os.environ.get("R30_CORE") or os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), *[".."]*6)) + "/experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "decls.json")

def strip_comments(src):
    """Replace comments with spaces, keep line structure."""
    out = []
    i, n = 0, len(src)
    depth = 0
    in_str = False
    while i < n:
        c = src[i]
        if depth == 0 and not in_str and src.startswith("--", i):
            j = src.find("\n", i)
            if j < 0: j = n
            out.append(" " * (j - i)); i = j; continue
        if not in_str and src.startswith("/-", i):
            depth += 1; out.append("  "); i += 2; continue
        if depth > 0:
            if src.startswith("-/", i):
                depth -= 1; out.append("  "); i += 2; continue
            out.append("\n" if c == "\n" else " "); i += 1; continue
        if c == '"' and (i == 0 or src[i-1] != "\\") and not (i > 0 and src[i-1] == "'"):
            in_str = not in_str
        out.append(c); i += 1
    return "".join(out)

KW = r"(theorem|lemma|def|abbrev|structure|inductive|class|instance|opaque|axiom)"
DECL_RE = re.compile(r"^(?P<mods>(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|partial|nonrec|unsafe)\s+)*)" + KW + r"\b\s*(?P<name>[^\s:({\[]*)", re.M)

def parse(path):
    raw = open(path, encoding="utf-8").read()
    src = strip_comments(raw)
    lines = src.split("\n")
    mod = "Becoming." + os.path.basename(path)[:-5]
    ns_stack = []  # list of (kind, name)
    decls = []
    cur = None
    offs = []
    for ln, line in enumerate(lines, 1):
        s = line.strip()
        m = re.match(r"^namespace\s+(\S+)", s)
        if m and not line.startswith(" "):
            ns_stack.append(("ns", m.group(1))); continue
        m = re.match(r"^section\b\s*(\S*)", s)
        if m and not line.startswith(" "):
            ns_stack.append(("sec", m.group(1))); continue
        m = re.match(r"^end\b\s*(\S*)", s)
        if m and not line.startswith(" "):
            if ns_stack: ns_stack.pop()
            continue
        m = DECL_RE.match(line)
        if m:
            kind = m.group(2)
            name = m.group("name")
            ns = ".".join(x[1] for x in ns_stack if x[0] == "ns" and x[1])
            full = (ns + "." + name) if (ns and name) else (name or ns)
            if name.startswith("_root_."): full = name[len("_root_."):]
            cur = {"module": mod, "kind": kind, "name": name, "full": full, "ns": ns,
                   "line": ln, "text": [line], "private": "private" in m.group("mods")}
            decls.append(cur); continue
        if re.match(r"^(open|variable|universe|set_option|attribute|#|import|noncomputable section|mutual|deriving)\b", s) and not line.startswith(" "):
            cur = None; continue
        if cur is not None:
            cur["text"].append(line)
    for d in decls:
        t = "\n".join(d["text"])
        d["text"] = t
        stmt, body = split_stmt(t, d["kind"])
        d["stmt"] = stmt
        d["body"] = body
        d["nlines"] = t.strip().count("\n") + 1
    return decls, raw.count("\n") + 1

def split_stmt(t, kind):
    # find first top-level ':=' or ' where' or a line starting with '|'
    depth = 0
    i = 0
    n = len(t)
    while i < n:
        c = t[i]
        if c in "([{⟨": depth += 1
        elif c in ")]}⟩": depth -= 1
        elif depth <= 0:
            if t.startswith(":=", i):
                return t[:i], t[i+2:]
            if re.match(r"\swhere\b", t[i:i+7]) and kind in ("structure", "class", "inductive", "def", "instance", "abbrev", "theorem"):
                return t[:i], t[i:]
            if t[i] == "\n" and re.match(r"\n\s*\|", t[i:]):
                return t[:i], t[i:]
        i += 1
    return t, ""

if __name__ == "__main__":
    allds = []
    sizes = {}
    for f in sorted(os.listdir(ROOT)):
        if f.endswith(".lean"):
            ds, nl = parse(os.path.join(ROOT, f))
            allds.extend(ds); sizes["Becoming." + f[:-5]] = nl
    json.dump({"decls": allds, "sizes": sizes}, open(OUT, "w"))
    from collections import Counter
    print(len(allds), Counter(d["kind"] for d in allds))
