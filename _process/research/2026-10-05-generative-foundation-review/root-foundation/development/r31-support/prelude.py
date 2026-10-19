#!/usr/bin/env python3
"""R31, item 3 (one-shot): one prelude, one name per prelude-only statement.

`Becoming.Prelude` (imports only Init) states, once each:
* the arithmetic of the root namespace (Dependence's section and the root lemmas the table keeps);
* the whole of Becoming.Naturals and Becoming.ListTests, whose files are removed;
* the names the table gives new (`how: new`), with the proof of one of the copies;
* the list lemmas of OneStep, Population and Listing that read no world (`mem_cons_cases`,
  `mem_append_cases`, `length_map`, `map_comp_eq`, `map_eq_of`, `map_eq_singleton`, `mem_middle`),
  and the root Boolean and list lemmas the table keeps.
Every kept name keeps its full name and statement. Each name the table deletes is removed, and each
use of it in the package (code, and qualified mentions in comments) is rewritten to the kept name,
written relative to `Becoming` where that resolves to it and in full otherwise; `--dry` prints the
rewrites without writing. Frame and Integers import the prelude; imports of Naturals and ListTests
become imports of the prelude.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import decltext  # noqa: E402
import dups  # noqa: E402

PKG = dups.ROOT  # .../becoming/Becoming
DRY = "--dry" in sys.argv
TABLE = json.load(open(HERE / "dedup-table.json"))
DS = decltext.decls()
FULL = {d["full"] for d in DS}

DELETE = {}
for g in TABLE["groups"]:
    for x in g["delete"]:
        assert x in FULL, x
        DELETE[x] = g["keep"]
    if g["how"] in ("moved", "kept"):
        assert g["keep"] in FULL, g["keep"]
    else:
        assert g["keep"] not in FULL, g["keep"]
MOVED = [g["keep"] for g in TABLE["groups"] if g["how"] == "moved"
         and not g["keep"].startswith(("Becoming.Naturals.", "Becoming.ListTests."))]
NEW = {g["keep"] for g in TABLE["groups"] if g["how"] == "new"}
AFTER = (FULL - set(DELETE)) | NEW

# ---------------------------------------------------------------- the prelude's text
ROOT_NAT = ["Becoming.le_dest", "Becoming.le_of_add_le_add_right", "Becoming.add_right_cancel",
            "Becoming.add_sub_turn", "Becoming.add_sub_turn_add", "Becoming.add_sub_of_le",
            "Becoming.sub_eq_zero_of_le", "Becoming.succ_sub_self", "Becoming.exists_add_of_le",
            "Becoming.mul_assoc_nat", "Becoming.mul_turn", "Becoming.add_mul_split", "Becoming.beq_self"]
ROOT_LIST = ["Becoming.bool_eq_of_iff", "Becoming.bool_and_true", "Becoming.bool_of_and_true",
             "Becoming.mem_cons_cases", "Becoming.mem_append_cases", "Becoming.mem_append_of_left",
             "Becoming.mem_append_of_right", "Becoming.mem_middle", "Becoming.length_map", "Becoming.map_comp_eq",
             "Becoming.map_eq_of", "Becoming.map_eq_singleton", "Becoming.preimage_of_mem_map"]
assert sorted(ROOT_NAT + ROOT_LIST) == sorted(MOVED), sorted(set(MOVED) ^ set(ROOT_NAT + ROOT_LIST))

NEW_NAT = '''
/-- No successor is zero (the prelude's `Nat.succ_ne_zero` depends on `propext`). -/
theorem succ_ne_zero (n : Nat) : n + 1 ≠ 0 :=
  fun same => Nat.noConfusion same

/-- Twice a number is the number added to itself. -/
theorem two_mul (n : Nat) : 2 * n = n + n :=
  (Nat.succ_mul 1 n).trans (congrArg (· + n) (Nat.one_mul n))

/-- A power of a sum of exponents is the product of the powers. -/
theorem pow_add (b x : Nat) : ∀ y, b ^ (x + y) = b ^ x * b ^ y
  | 0 => (Nat.mul_one _).symm
  | y + 1 => (congrArg (· * b) (pow_add b x y)).trans (mul_assoc_nat _ _ _)

/-- The last two factors of a product exchange. -/
theorem mul_right_comm (a b c : Nat) : a * b * c = a * c * b :=
  (mul_assoc_nat a b c).trans ((congrArg (a * ·) (Nat.mul_comm b c)).trans (mul_assoc_nat a c b).symm)

/-- The middle factors of two products exchange. -/
theorem mul_mul_mul_comm (a b c d : Nat) : a * b * (c * d) = a * c * (b * d) :=
  (mul_assoc_nat a b (c * d)).trans ((congrArg (a * ·) (mul_turn b c d)).trans
    (mul_assoc_nat a c (b * d)).symm)

/-- Two equal summands give equal sums. -/
theorem add_congr {a b c d : Nat} (ab : a = b) (cd : c = d) : a + c = b + d :=
  (congrArg (· + c) ab).trans (congrArg (b + ·) cd)

/-- Below a number, the test of being at most another fails. -/
theorem ble_false_of_lt : ∀ {a b : Nat}, b < a → Nat.ble a b = false
  | 0, _, lt => absurd lt (Nat.not_lt_zero _)
  | _ + 1, 0, _ => rfl
  | a + 1, b + 1, lt => @ble_false_of_lt a b (Nat.lt_of_succ_lt_succ lt)
'''

NEW_LIST = '''
/-! ## Negation, disjunction and the two truth values -/

/-- No truth value is its negation. -/
theorem not_ne_self : ∀ b : Bool, (!b) ≠ b
  | true => fun same => Bool.noConfusion same
  | false => fun same => Bool.noConfusion same

/-- No truth value is its negation, read the other way. -/
theorem ne_not : ∀ b : Bool, b ≠ !b
  | false => fun same => nomatch same
  | true => fun same => nomatch same

theorem not_not : ∀ b : Bool, (!!b) = b
  | false => rfl
  | true => rfl

theorem false_of_not : ∀ {b : Bool}, (!b) = true → b = false
  | false, _ => rfl
  | true, yes => Bool.noConfusion yes

theorem false_of_not_true : ∀ {b : Bool}, ¬ b = true → b = false
  | false, _ => rfl
  | true, no => absurd rfl no

theorem not_eq_true_of_false : ∀ {b : Bool}, b = false → (!b) = true
  | false, _ => rfl
  | true, no => Bool.noConfusion no

theorem or_cases : ∀ {a b : Bool}, (a || b) = true → a = true ∨ b = true
  | true, _, _ => .inl rfl
  | false, _, yes => .inr yes

theorem or_left : ∀ {a : Bool} (b : Bool), a = true → (a || b) = true
  | true, _, _ => rfl
  | false, _, no => nomatch no

theorem or_right : ∀ (a : Bool) {b : Bool}, b = true → (a || b) = true
  | true, _, _ => rfl
  | false, _, yes => yes

/-- Each truth value is listed in `[true, false]`. -/
theorem mem_bools : ∀ b : Bool, b ∈ [true, false]
  | true => .head _
  | false => .tail _ (.head _)

/-! ## Joining lists -/

theorem append_nil : ∀ l : List α, l ++ [] = l
  | [] => rfl
  | x :: xs => congrArg (x :: ·) (append_nil xs)

theorem append_assoc : ∀ l m n : List α, l ++ m ++ n = l ++ (m ++ n)
  | [], _, _ => rfl
  | a :: l, m, n => congrArg (List.cons a) (append_assoc l m n)
'''

DOC = '''/-!
# Prelude: numbers, truth values, lists and options

The lemmas on Lean's own types that the layers use, each stated once and each with an empty axiom
report; several of the prelude's own versions use `propext`. Nothing here reads a world, a frame
or a law: the module imports only Init, and every module of the core reaches it through
`Becoming.Frame`.

* **Natural numbers.** Cancellation, subtraction and the order (`add_right_cancel`,
  `add_sub_of_le`, `le_dest`, `exists_add_of_le`, `sub_eq_zero_of_le`, `add_sub_turn`), products
  (`mul_assoc_nat`, `mul_turn`, `add_mul_split`) and equality tests (`beq_self`) in the root
  namespace, and the lemmas of `Naturals`.
* **Truth values, lists and options** (`ListTests`): how `&&`, `||`, `!`, `==`, `all`, `any`,
  `contains`, `filter`, `map`, `flatMap`, `find?` and the operations on options evaluate, as
  statements about membership and truth.
* **Lists** in the root namespace: membership in a joined list and a cons
  (`mem_append_cases`, `mem_cons_cases`, `mem_append_of_left`, `mem_append_of_right`,
  `mem_middle`), the length and members of a mapped list (`length_map`, `preimage_of_mem_map`,
  `map_comp_eq`, `map_eq_of`, `map_eq_singleton`), and equal truth values (`bool_eq_of_iff`).

Each statement here was proved in the modules that used it, often more than once; R31 (20 October
2026) states each once (the table and the copies it replaced are in the R31 kit,
`development/r31-support/dedup-table.json`).
-/
'''


def span_text(full):
    path, a, b = decltext.span(full, DS)
    return path, a, b, "\n".join(path.read_text().split("\n")[a - 1:b])


removals = {}  # path -> list of (a, b)


def take(full):
    path, a, b, text = span_text(full)
    removals.setdefault(path, []).append((a, b))
    return text


nat_src = (PKG / "Naturals.lean").read_text().split("\n")
assert nat_src[22] == "namespace Naturals" and nat_src[85] == "end Naturals", (nat_src[22], nat_src[85])
lt_src = (PKG / "ListTests.lean").read_text().split("\n")
assert lt_src[29] == "namespace ListTests" and lt_src[246] == "end ListTests"
assert lt_src[31] == "universe u v" and lt_src[33] == "variable {α : Type u} {β : Type v}"

out = [DOC, "namespace Becoming", "", "universe u v", "",
       "/-! ## Natural numbers -/", ""]
for x in ROOT_NAT:
    out += [take(x), ""]
out += ["namespace Naturals", ""] + nat_src[24:85] + [NEW_NAT.strip("\n"), "", "end Naturals", "",
        "/-! ## Truth values, lists and options -/", "", "namespace ListTests", "",
        "variable {α : Type u} {β : Type v}", ""]
out += lt_src[35:246] + [NEW_LIST.strip("\n"), "", "end ListTests", "",
                         "/-! ## Lists in the root namespace -/", "", "section Lists", "",
                         "variable {α β γ : Type}", ""]
for x in ROOT_LIST:
    out += [take(x), ""]
out += ["end Lists", "", "end Becoming", ""]
prelude = "\n".join(out)

for x in DELETE:
    take(x)

# ---------------------------------------------------------------- removing the spans
texts = {p: p.read_text() for p in PKG.glob("*.lean")}
for path, spans in removals.items():
    lines = texts[path].split("\n")
    gone = set()
    for a, b in spans:
        gone.update(range(a - 1, b))
        k = b
        while k < len(lines) and lines[k].strip() == "" and (k == b):
            gone.add(k)
            k += 1
    texts[path] = "\n".join(l for i, l in enumerate(lines) if i not in gone)
texts[PKG / "Prelude.lean"] = prelude
del texts[PKG / "Naturals.lean"], texts[PKG / "ListTests.lean"]

# ---------------------------------------------------------------- imports
for path in list(texts):
    s = texts[path]
    if re.search(r"^import Becoming\.(Naturals|ListTests)\s*$", s, re.M):
        lines = s.split("\n")
        new, seen = [], False
        for l in lines:
            if re.fullmatch(r"import Becoming\.(Naturals|ListTests|Prelude)\s*", l):
                if not seen:
                    new.append("import Becoming.Prelude")
                    seen = True
                continue
            new.append(l)
        texts[path] = "\n".join(new)
for name in ("Frame", "Integers"):
    path = PKG / f"{name}.lean"
    if "import Becoming.Prelude" not in texts[path]:
        texts[path] = "import Becoming.Prelude\n" + texts[path]

# ---------------------------------------------------------------- rewriting the uses
IDENT = re.compile(r"(?<![\w.'?!])(@?)([A-Za-z_α-ω][\w'?!]*(?:\.[A-Za-z_][\w'?!]*)*)")
NAMESPACES = set()
for f in AFTER | FULL:
    parts = f.split(".")
    for i in range(1, len(parts)):
        NAMESPACES.add(".".join(parts[:i]))


def resolve(tok, ns, opens, names):
    parts = ns.split(".") if ns else []
    for i in range(len(parts), -1, -1):
        cand = ".".join(parts[:i] + [tok])
        if cand in names:
            return cand
    for o in opens:
        if o + "." + tok in names:
            return o + "." + tok
    return None


def written(keep, ns, opens):
    if ns.startswith("Becoming"):
        rel = keep[len("Becoming."):]
        if resolve(rel, ns, opens, AFTER) == keep:
            return rel
    return keep


rewrites = []


def rewrite(path, s):
    lines = s.split("\n")
    stack = []  # (kind, name, opens added)
    opens = []
    in_block = 0
    out = []
    for n, line in enumerate(lines):
        code = line
        m = re.match(r"\s*namespace\s+(\S+)", line)
        if m and not in_block:
            stack.append(("ns", m.group(1), []))
        m2 = re.match(r"\s*section\b\s*(\S*)", line)
        if m2 and not in_block:
            stack.append(("sec", m2.group(1), []))
        m3 = re.match(r"\s*end\b\s*(\S*)\s*$", line)
        m4 = re.match(r"\s*open\s+(.*?)(\s+in)?\s*$", line)
        ns = ".".join(x[1] for x in stack if x[0] == "ns")
        if m4 and not in_block and not line.lstrip().startswith("open scoped"):
            for o in m4.group(1).split():
                if o.startswith("("):
                    break
                full = resolve(o, ns, [], NAMESPACES) or o
                opens.append(full)
                if stack:
                    stack[-1][2].append(full)
        # tokens: rewrite in code; in comments only qualified tokens
        res, pos = [], 0
        i = 0
        segs = []
        # split the line into (text, is_comment) by tracking block comments and `--`
        cur, comment = "", bool(in_block)
        while i < len(line):
            if not in_block and line.startswith("--", i):
                segs.append((cur, comment))
                segs.append((line[i:], True))
                cur, i = "", len(line)
                break
            if line.startswith("/-", i):
                if not in_block:
                    segs.append((cur, False))
                    cur = ""
                in_block += 1
                cur += "/-"
                i += 2
                continue
            if in_block and line.startswith("-/", i):
                in_block -= 1
                cur += "-/"
                i += 2
                if not in_block:
                    segs.append((cur, True))
                    cur = ""
                continue
            cur += line[i]
            i += 1
        segs.append((cur, bool(in_block)))
        newline = ""
        for text, is_comment in segs:
            def rep(mt):
                at, tok = mt.group(1), mt.group(2)
                if is_comment and "." not in tok:
                    return mt.group(0)
                target = resolve(tok, ns, opens, FULL)
                if target not in DELETE:
                    if is_comment:
                        t2 = tok if tok.startswith("Becoming.") else None
                        if t2 in DELETE:
                            target = t2
                        else:
                            return mt.group(0)
                    else:
                        return mt.group(0)
                keep = DELETE[target]
                w = written(keep, ns, opens)
                rewrites.append((path.name, n + 1, tok, w, "comment" if is_comment else "code", line.strip()[:160]))
                return at + w
            newline += IDENT.sub(rep, text)
        out.append(newline)
        if m3 and not in_block and stack:
            kind, name, added = stack.pop()
            for o in added:
                opens.remove(o)
    return "\n".join(out)


for path in sorted(texts):
    texts[path] = rewrite(path, texts[path])

for r in rewrites:
    print(*r, sep="\t")
print(len(rewrites), "rewrites", file=sys.stderr)
if not DRY:
    for path, s in texts.items():
        if not path.exists() or path.read_text() != s:
            path.write_text(s)
    for name in ("Naturals", "ListTests"):
        (PKG / f"{name}.lean").unlink()
    print("written", file=sys.stderr)
