#!/usr/bin/env python3
"""R28: drop the parentheses the construction-site rewrite put around single names.

`rewrite_world.py` and `rewrite_world2.py` (S4's scripts, kept here) rewrite `⟨R, L, W⟩ : World` to
`World.of (R) (L) (W)`. Where an argument is one name (`World.of (C) (Flow.still) (W)`), the
parentheses are dropped: `World.of C Flow.still W`. Nothing else changes.

usage: python3 -B tidy_of.py PACKAGE_DIR
"""
import re
import sys
from pathlib import Path

NAME = re.compile(r"[A-Za-z_][\w.'₀-₉]*\Z")
OPEN, CLOSE = "([{⟨", ")]}⟩"


def closing(text, start):
    depth = 0
    for k in range(start, len(text)):
        if text[k] in OPEN:
            depth += 1
        elif text[k] in CLOSE:
            depth -= 1
            if depth == 0:
                return k
    return None


def tidy(text):
    out, i = [], 0
    while True:
        k = text.find("World.of (", i)
        if k < 0:
            out.append(text[i:])
            return "".join(out)
        j = k + len("World.of")
        out.append(text[i:j])
        for _ in range(3):
            if not text.startswith(" (", j):
                break
            e = closing(text, j + 1)
            inner = text[j + 2:e]
            out.append(" " + inner if NAME.match(inner) else text[j:e + 1])
            j = e + 1
        i = j


def main():
    pkg = Path(sys.argv[1]) / "Becoming"
    for path in sorted(pkg.glob("*.lean")):
        text = path.read_text()
        new = tidy(text)
        if new != text:
            path.write_text(new)
            print("tidied", path.name)


if __name__ == "__main__":
    main()
