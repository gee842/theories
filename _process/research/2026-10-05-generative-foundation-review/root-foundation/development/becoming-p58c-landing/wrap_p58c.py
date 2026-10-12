#!/usr/bin/env python3
"""P58c: rewrap the comment lines this change made longer than 100 characters, carrying words into the
next line of the same paragraph. Lines already long on main are left. Usage: wrap_p58c.py TREE CORE"""
import os
import sys
from pathlib import Path
T, C = Path(sys.argv[1]) / 'Becoming', Path(sys.argv[2])
W = 100


def comment_mask(lines):
    inside, mask = False, []
    for l in lines:
        s = l.strip()
        starts = s.startswith('/-')
        mask.append(inside or starts)
        if starts:
            inside = True
        if s.endswith('-/'):
            inside = False
    return mask


for f in sorted(T.glob('*.lean')):
    old = set(l for l in (C / f.name).read_text().split('\n') if len(l) > W)
    lines = f.read_text().split('\n')
    changed = True
    while changed:
        changed = False
        mask = comment_mask(lines)
        for i, l in enumerate(lines):
            if len(l) <= W or l in old or not mask[i]:
                continue
            cut = l.rfind(' ', 0, W + 1)
            head, tail = l[:cut], l[cut + 1:]
            nxt = lines[i + 1] if i + 1 < len(lines) else ''
            ns = nxt.strip()
            cont = (mask[i + 1] and ns and not ns.startswith('* ') and not ns.startswith('/-') and ns != '-/'
                    and not l.rstrip().endswith('-/') and not ns.startswith('#'))
            if cont:
                indent = nxt[:len(nxt) - len(nxt.lstrip())]
                lines[i], lines[i + 1] = head, indent + tail + ' ' + ns
            else:
                lead = l[:len(l) - len(l.lstrip())]
                if l.lstrip().startswith('* '):
                    lead += '  '
                lines[i:i + 1] = [head, lead + tail]
            changed = True
            break
    f.write_text('\n'.join(lines))
print('ok')
