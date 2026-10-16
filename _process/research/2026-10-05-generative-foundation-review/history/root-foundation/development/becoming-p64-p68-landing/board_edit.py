#!/usr/bin/env python3
"""Mark P64–P68 landed on the work board. Usage: python3 -B board_edit.py ROOT COMMIT CORE_UTC PERI_UTC"""
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
COMMIT, CORE, PERI = sys.argv[2:5]
board = ROOT / '_process/BECOMING-WORKBOARD.md'
s = board.read_text()
PKG = ('`_process/research/2026-10-05-generative-foundation-review/root-foundation/development/becoming-p64-p68-landing/` '
       '(package); scratch `/private/tmp/claude-501/-Users-ren-theories/6114a5b7-5805-4fa7-9783-383dfbc218ce/scratchpad/causal/`')
STATUS = {
    'P64': ('verified in scratch against main ae17922a', f'landed `{COMMIT}` (10-12) with P65–P68, one run (study §86; receipts core {CORE}, periphery {PERI}): '),
    'P65': ('verified in scratch against main ae17922a', f'landed `{COMMIT}` (10-12) with P64, P66–P68 (study §87; same receipts): '),
    'P66': ('verified in scratch against main ae17922a', f'landed `{COMMIT}` (10-12) with P64, P65, P67, P68 (study §88, with P68; same receipts): '),
    'P67': ('verified in scratch against main ae17922a', f'landed `{COMMIT}` (10-12) with P64–P66, P68 (study §89; same receipts): '),
    'P68': ('verified in scratch with P66 in `Becoming.Mechanism`', f'landed `{COMMIT}` (10-12) with P66 in `Becoming.Mechanism` (study §88; same receipts): '),
}
lines = s.split('\n')
for key, (old, new) in STATUS.items():
    idx = [i for i, l in enumerate(lines) if l.startswith(f'| **{key} ')]
    assert len(idx) == 1, key
    cells = lines[idx[0]].split(' | ')
    k = next(j for j, c in enumerate(cells) if c.startswith(old))
    c = cells[k]
    c = c[len(old):]
    c = re.sub(r'^ \(P62 landed, c3f6829f\), Capture patched', '', c)
    c = c.lstrip(':, ')
    c = re.sub(r'\. Handed to the integrator with the landing package( \(rebased onto ae17922a\))?$', '', c)
    cells[k] = new + c
    lines[idx[0]] = ' | '.join(cells)
s = '\n'.join(lines)
old_q = next(l for l in s.split('\n') if l.startswith('- P64–P68 `Becoming.Attraction`'))
new_q = ('- ~~P64–P68 `Becoming.Attraction`, `Becoming.Mechanism`, `Becoming.Response`, `Becoming.Selection` '
         '(Cause–effect comparison [31d5b6])~~ landed `' + COMMIT + '` by its owner (§86–§89; receipt ' + CORE +
         ', periphery ' + PERI + '), with Capture\'s `Law.reform_reabsorbed` re-proved as the instance of Mechanism\'s '
         '`Law.reabsorbed` (name and statement kept).')
s = s.replace(old_q, new_q)
board.write_text(s)
for l in s.split('\n'):
    if l.startswith('| **P6') and any(l.startswith(f'| **{k} ') for k in STATUS):
        cells = l.split(' | ')
        print(cells[0][:40], '|', cells[2][:260])
print(new_q)
