#!/usr/bin/env python3
"""P123: classify Becoming.Frequency's use of decidedness in DECIDABILITY-INVENTORY.py.

usage: python3 -B apply_inventory.py W

One theorem takes the equality of conditions and uses it only in its proof (`same`): `gap_le_count`,
through `gap_le_carried` of `Becoming.Propagation`, whose carrying law splits on whether a level is
the one that differs. Nothing else in the module takes a decision: the schedules and the families of
the dichotomy are Boolean-valued functions, not decisions taken of a proposition. The entry goes at
the end of PROOF_KIND; a second run fails.
"""
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
path = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/DECIDABILITY-INVENTORY.py'
t = path.read_text()
assert "'gap_le_count'" not in t, 'already classified'


def before(text, anchor, insert):
    assert text.count(anchor) == 1, (anchor, text.count(anchor))
    return text.replace(anchor, insert + anchor)


t = before(t, '}\n# Proved to need decidedness where asked of every world',
           '    # 2026-10-16, P123 how often couplings act (Becoming.Frequency): the rate for every law reads the\n'
           '    # equality of conditions in its proof, through gap_le_carried\n'
           "    'gap_le_count': 'same',\n")
path.write_text(t)
print('classified one proof-only theorem of Becoming.Frequency')
