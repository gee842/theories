"""Inventory of the 39 bridge modules' declarations with a first-pass kind."""
import json, re, sys, pathlib, subprocess

# The repository root, from this script's location.
ROOT = pathlib.Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                                          cwd=pathlib.Path(__file__).resolve().parent, text=True).strip())
LEAN = ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/becoming"
src = (LEAN / "check_becoming.py").read_text()
bridge = re.search(r"^BRIDGE = \[(.*?)\]", src, re.S | re.M).group(1)
MODULES = re.findall(r'"(Becoming\.[A-Za-z]+)"', bridge)
assert len(MODULES) == 39, len(MODULES)

DECL = re.compile(r"^(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|nonrec|partial|unsafe)\s+)*"
                  r"(theorem|lemma|def|abbrev|structure|inductive|instance|class|opaque)\s+([^\s:({\[]+)?")


def strip_comments(text):
    out, i, depth = [], 0, 0
    while i < len(text):
        if text.startswith("/-", i):
            depth += 1; i += 2; continue
        if depth and text.startswith("-/", i):
            depth -= 1; i += 2; continue
        if depth:
            out.append("\n" if text[i] == "\n" else ""); i += 1; continue
        if text.startswith("--", i):
            j = text.find("\n", i); i = len(text) if j < 0 else j; continue
        out.append(text[i]); i += 1
    return "".join(out)


def parse(mod):
    path = LEAN / (mod.replace(".", "/") + ".lean")
    raw = path.read_text()
    imports = re.findall(r"^import (\S+)", raw, re.M)
    lines = strip_comments(raw).split("\n")
    ns, decls, cur = [], [], None
    for n, line in enumerate(lines, 1):
        m = re.match(r"^namespace (\S+)", line)
        if m:
            ns.append(m.group(1)); cur = None; continue
        m = re.match(r"^end (\S+)\s*$", line)
        if m and ns and ns[-1] == m.group(1):
            ns.pop(); cur = None; continue
        m = DECL.match(line)
        if m:
            kind, name = m.group(1), m.group(2) or "(anon)"
            full = ".".join(ns + [name]) if not name.startswith("_root_.") else name[7:]
            cur = {"module": mod, "kind": kind, "name": full, "line": n, "text": line + "\n"}
            decls.append(cur); continue
        if re.match(r"^(section|end|open|variable|universe|set_option|attribute|#)", line):
            if not re.match(r"^(open|variable|universe)", line):
                cur = None
            continue
        if cur is not None:
            cur["text"] += line + "\n"
    return imports, decls


def body(text):
    t = text.strip()
    # split statement from proof at the first top-level ':=' or the start of match arms
    m = re.search(r":=", t)
    if not m:
        return t, ""
    return t[:m.start()], t[m.end():].strip()


TRIVIAL = re.compile(r"^(Iff\.rfl|rfl|\.rfl|id|by rfl|by exact Iff\.rfl|⟨id, id⟩|⟨fun h => h, fun h => h⟩|"
                     r"fun _ => rfl|fun _ _ => rfl|fun _ => Iff\.rfl|fun _ _ => Iff\.rfl|by intro[^\n]*; rfl|"
                     r"by funext[^\n]*;? ?rfl|by simp only \[[^\]]*\]|by unfold [^\n]*|"
                     r"by constructor <;> intro h <;> exact h|Iff\.rfl\s*)$", re.S)

rows, mods = [], {}
for mod in MODULES:
    imports, decls = parse(mod)
    mods[mod] = imports
    for d in decls:
        stmt, proof = body(d["text"])
        oneline = " ".join(proof.split())
        d["proof"] = oneline[:400]
        d["proof_len"] = len(oneline)
        d["stmt"] = " ".join(stmt.split())[:500]
        d["trivial"] = bool(TRIVIAL.match(oneline)) or (d["kind"] in ("theorem", "lemma") and len(oneline) <= 25 and "rfl" in oneline)
        del d["text"]
        rows.append(d)
json.dump({"modules": mods, "decls": rows}, open(sys.argv[1], "w"), indent=1, ensure_ascii=False)
from collections import Counter
print(len(rows), Counter(r["kind"] for r in rows))
print("trivial theorems", sum(1 for r in rows if r["trivial"] and r["kind"] in ("theorem", "lemma")))
for mod in MODULES:
    rs = [r for r in rows if r["module"] == mod]
    print(f"{mod:45} thm={sum(r['kind'] in ('theorem','lemma') for r in rs):4} def={sum(r['kind'] not in ('theorem','lemma') for r in rs):3} triv={sum(r['trivial'] and r['kind'] in ('theorem','lemma') for r in rs):3}")
