#!/usr/bin/env python3
"""P120: classify Becoming.Remainder's use of decidedness in DECIDABILITY-INVENTORY.py.

usage: python3 -B apply_inventory.py W

One theorem takes the equality of conditions and uses it only in its proof (`same`):
`gap_within_order_iff`, through `most_difference_arrives` of `Becoming.Propagation`, whose carrying
law splits on whether a level is the one that differs. Nothing else in the module takes a decision.
The entry goes at the end of PROOF_KIND; a second run fails.
"""
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
path = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/DECIDABILITY-INVENTORY.py'
t = path.read_text()
assert "'gap_within_order_iff'" not in t, 'already classified'


def before(text, anchor, insert):
    assert text.count(anchor) == 1, (anchor, text.count(anchor))
    return text.replace(anchor, insert + anchor)


t = before(t, '}\n# Proved to need decidedness where asked of every world',
           '    # 2026-10-16, P120 what a cut loses (Becoming.Remainder): the equivalence for every law reads the\n'
           '    # equality of conditions in its proof, through most_difference_arrives\n'
           "    'gap_within_order_iff': 'same',\n")
path.write_text(t)
print('classified one proof-only theorem of Becoming.Remainder')
