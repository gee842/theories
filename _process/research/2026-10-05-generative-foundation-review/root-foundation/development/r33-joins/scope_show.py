#!/usr/bin/env python3
"""Print the checker's SCOPE sentences and Becoming.lean's notes for the named modules (inspection)."""
import re
import sys
from pathlib import Path

PKG = Path(__file__).resolve().parents[6] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def scope_blocks(text):
    out, cur, buf = {}, None, []
    for line in text.split('\n'):
        m = re.match(r'^    "([A-Z][A-Za-z]*): ', line)
        if m:
            if cur:
                out[cur] = '\n'.join(buf)
            cur, buf = m.group(1), [line]
        elif cur and line.startswith('    "'):
            buf.append(line)
        elif cur:
            out[cur] = '\n'.join(buf)
            cur, buf = None, []
    return out


def notes(text):
    out, cur, buf = {}, None, []
    for line in text.split('\n'):
        m = re.match(r'^\* `Becoming\.([A-Za-z]+)`', line)
        if m:
            if cur:
                out[cur] = '\n'.join(buf)
            cur, buf = m.group(1), [line]
        elif cur and line.startswith('  '):
            buf.append(line)
        elif cur:
            out[cur] = '\n'.join(buf)
            cur, buf = None, []
    return out


S = scope_blocks((PKG / 'check_becoming.py').read_text())
N = notes((PKG / 'Becoming.lean').read_text())
for k in sys.argv[1:]:
    print('== SCOPE', k)
    print(S.get(k, '(none)'))
    print('== NOTE', k)
    print(N.get(k, '(none)'))
