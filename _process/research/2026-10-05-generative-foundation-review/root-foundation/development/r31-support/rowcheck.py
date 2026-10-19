#!/usr/bin/env python3
"""R31: which module-table rows cite a declaration that R31 moved out of the row's module.

For each row of a module table (the Lean READMEs, the Chinese chapter's §9 table) naming a core module
`Becoming.M`, each backticked name is resolved against two receipts: a name that resolved to a
declaration of M in the base receipt and to none of M in R31's is printed with the module that now
holds it. usage: python3 -B rowcheck.py BASE_RID NEW_RID FILE..."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
CHECKS = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-checks'


def homes(rid):
    r = json.load(open(CHECKS / rid / 'verification.json'))
    out = {}
    for m in r['modules']:
        if m.get('layer') != 'core':
            continue
        for x in m.get('declarations', []):
            out[x['name'] if isinstance(x, dict) else x] = m['module']
    return out


old, new = homes(sys.argv[1]), homes(sys.argv[2])


def index(h):
    by = {}
    for full, mod in h.items():
        parts = full.split('.')
        for i in range(1, len(parts)):
            by.setdefault('.'.join(parts[i:]), set()).add((full, mod))
    return by


oi, ni = index(old), index(new)
ROWMOD = re.compile(r"Becoming/(\w+)\.lean\)")
for f in sys.argv[3:]:
    for n, line in enumerate(Path(f).read_text().split('\n'), 1):
        if not line.startswith('| '):
            continue
        m = ROWMOD.search(line)
        if not m:
            continue
        mod = 'Becoming.' + m.group(1)
        for tok in re.findall(r"`([^`\s]+)`", line):
            tok = tok.strip('`')
            if tok.startswith('Becoming.') and tok.count('.') == 1:
                continue
            before = {x for x, mm in oi.get(tok, ()) if mm == mod}
            after = {x for x, mm in ni.get(tok, ()) if mm == mod}
            if before and not after:
                now = sorted({mm for x, mm in ni.get(tok, ()) if x in before}) or ['removed']
                print(f'{Path(f).name}:{n} {mod} `{tok}` -> {", ".join(now)}')
