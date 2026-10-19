#!/usr/bin/env python3
"""R31: the source span of declarations, with their doc comments (used by prelude.py).

`span(full)` gives (module path, first line, last line) of the declaration named `full`, its doc
comment and attributes included, its trailing blank lines excluded; `python3 decltext.py NAME ...`
prints each span.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import dups  # noqa: E402

_DECLS = None


def decls(refresh=False):
    global _DECLS
    if _DECLS is None or refresh:
        _DECLS = dups.declarations()
    return _DECLS


def span(full, ds=None):
    ds = ds if ds is not None else decls()
    hits = [d for d in ds if d["full"] == full]
    assert len(hits) == 1, (full, len(hits))
    d = hits[0]
    path = dups.ROOT / (d["module"][len("Becoming."):] + ".lean")
    lines = path.read_text().split("\n")
    a = d["line"] - 1
    # attributes and the doc comment directly above
    while a > 0 and lines[a - 1].strip().startswith("@["):
        a -= 1
    if a > 0 and lines[a - 1].rstrip().endswith("-/") and not lines[a - 1].lstrip().startswith("/-!"):
        j = a - 1
        while not lines[j].lstrip().startswith("/--"):
            j -= 1
            assert j >= 0
        a = j
    n = d["text"].count("\n") + 1
    b = d["line"] - 1 + n - 1
    while b > d["line"] - 1 and lines[b].strip() == "":
        b -= 1
    # the parser may run into a following section comment: stop at a `/-!` line
    for k in range(d["line"], b + 1):
        if lines[k].lstrip().startswith(("/-!", "/--")) or re.match(
                r"(end|namespace|section|variable|open|universe|theorem|def|@\[|private|protected|instance|abbrev|structure|inductive)\b", lines[k]):
            b = k - 1
            while lines[b].strip() == "":
                b -= 1
            break
    return path, a + 1, b + 1


if __name__ == "__main__":
    for name in sys.argv[1:]:
        path, a, b = span(name)
        lines = path.read_text().split("\n")
        print(f"== {name} {path.name}:{a}-{b}")
        print("\n".join(lines[a - 1:b]))
