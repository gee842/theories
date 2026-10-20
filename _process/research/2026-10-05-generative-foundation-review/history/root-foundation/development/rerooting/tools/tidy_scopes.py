"""Tidy the scope commands a move leaves behind in Lean modules of the Becoming package.

usage: tidy_scopes.py PACKAGE MODULE ...

For each named module, by the imports now in its file and those of the modules it imports:
* where neither `GenerativeCore` nor `InquirySufficiency` is in its import closure, `open` drops the
  namespaces `Generative` and `Generative.…`; where only `InquirySufficiency` is, it keeps those
  under `Generative.InquirySufficiency` and `Generative` itself;
* where neither `GenerativeCore` nor `Becoming.Frame` is in its import closure, `variable` drops
  the binder groups whose type names `Process`, `Frame`, `Run` or `Trace`;
* an `open` or `variable` left empty is removed, then a section or namespace holding no
  declaration (only scope commands, headings and blank lines) is removed with one blank line
  around it, and blank lines at the top of the file are removed.
Declarations are not touched.
"""
import re
import sys
from pathlib import Path

package = Path(sys.argv[1])
FOUND = {"GenerativeCore", "InquirySufficiency", "RelationalRenewal"}


def path_of(m):
    return package / (m.replace(".", "/") + ".lean")


def imports(m):
    p = path_of(m)
    if not p.exists():
        return []
    return [line.split()[1] for line in p.read_text().splitlines() if line.startswith("import ")]


def closure(m):
    seen, stack = set(), [m]
    while stack:
        for i in imports(stack.pop()):
            if i not in seen:
                seen.add(i)
                stack.append(i)
    return seen


LTS_TYPE = re.compile(r"\b(Process|Frame|Run|Trace)\b")


def binder_groups(text):
    """Split the binders of a `variable` command into top-level bracket groups."""
    groups, depth, start = [], 0, None
    for i, ch in enumerate(text):
        if ch in "({[⦃":
            if depth == 0:
                start = i
            depth += 1
        elif ch in ")}]⦄":
            depth -= 1
            if depth == 0:
                groups.append(text[start:i + 1])
    return groups


def tidy(m):
    c = closure(m)
    gen = "GenerativeCore" in c
    inq = "InquirySufficiency" in c
    frame = gen or "Becoming.Frame" in c
    lines = Path(path_of(m)).read_text().splitlines(keepends=True)
    out = []
    for line in lines:
        if line.startswith("open ") and not gen:
            words = line.split()[1:]
            keep = [w for w in words if not (w == "Generative" or w.startswith("Generative."))
                    or (inq and (w == "Generative" or w.startswith("Generative.InquirySufficiency")))]
            if keep != words:
                if not keep:
                    out.append(None)
                    continue
                line = "open " + " ".join(keep) + "\n"
        if line.startswith("variable ") and not frame and LTS_TYPE.search(line):
            groups = binder_groups(line[len("variable "):])
            keep = [g for g in groups if not LTS_TYPE.search(g)]
            if not keep:
                out.append(None)
                continue
            line = "variable " + " ".join(keep) + "\n"
        out.append(line)
    # A removed line leaves one blank line where it stood between two.
    out = [line for k, line in enumerate(out) if line is not None and not (
        not line.strip() and k > 0 and out[k - 1] is None and k > 1 and out[k - 2] is not None
        and not out[k - 2].strip())]
    # Remove sections and namespaces that hold no declaration, innermost first.
    scope = re.compile(r"^(namespace|section)\b ?(\S*)")
    filler = re.compile(r"^(variable|open|universe)\b|^\s*$|^/-! .* -/\s*$")
    changed = True
    while changed:
        changed = False
        for i, line in enumerate(out):
            mo = scope.match(line)
            if not mo:
                continue
            name = mo.group(2)
            j = i + 1
            while j < len(out) and filler.match(out[j]):
                j += 1
            if j < len(out) and out[j].rstrip() == ("end " + name if name else "end"):
                k = j + 1
                if k < len(out) and not out[k].strip() and (i == 0 or not out[i - 1].strip()):
                    k += 1
                del out[i:k]
                changed = True
                break
    # A heading directly before an `end` heads nothing.
    text = "".join(out)
    text = re.sub(r"\n/-! [^\n]* -/\n(\s*\n)*(?=end\b)", "\n", text)
    text = text.lstrip("\n")
    path_of(m).write_text(text)


for m in sys.argv[2:]:
    tidy(m)
print("tidied:", len(sys.argv) - 2)
