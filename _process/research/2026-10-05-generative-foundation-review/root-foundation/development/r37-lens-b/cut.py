#!/usr/bin/env python3
"""R37b: cut declarations, with their doc comments, from one module, by their names as written there.

usage: python3 -B cut.py MODULE.lean NAME ...   (NAME as declared in the file, e.g. `CountsOf.tally`)

A declaration runs from its doc comment (or attributes) to the line before the next top-level item;
one blank line after it goes with it. Used where a declaration moved to a lower module under the same
full name (so the package-wide remove.py, which needs one declaration per name, does not apply)."""
import re
import sys
from pathlib import Path

path = Path(sys.argv[1])
lines = path.read_text().split('\n')
TOP = re.compile(r'^(/--|/-!|theorem |def |abbrev |instance |structure |inductive |namespace |end |section |variable |open |@\[|private |protected |noncomputable |universe )')
gone = set()
for name in sys.argv[2:]:
    hits = [k for k, l in enumerate(lines)
            if re.match(r'^(?:private |protected )?(theorem|def|abbrev|instance) ' + re.escape(name) + r'(?:\s|$)', l)]
    assert len(hits) == 1, (name, hits)
    a = hits[0]
    while a > 0 and lines[a - 1].startswith('@['):
        a -= 1
    if a > 0 and lines[a - 1].rstrip().endswith('-/') and not lines[a - 1].startswith('/-!'):
        j = a - 1
        while not lines[j].startswith('/--'):
            j -= 1
        a = j
    b = hits[0] + 1
    while b < len(lines) and not (lines[b].strip() == '' and b + 1 < len(lines) and TOP.match(lines[b + 1])) \
            and not TOP.match(lines[b]):
        b += 1
    if b < len(lines) and lines[b].strip() == '':
        b += 1
    gone.update(range(a, b))
    print(name, a + 1, b)
path.write_text('\n'.join(l for k, l in enumerate(lines) if k not in gone))
