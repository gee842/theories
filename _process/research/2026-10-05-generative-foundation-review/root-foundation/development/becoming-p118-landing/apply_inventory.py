#!/usr/bin/env python3
"""P118: classify Becoming.Loops's uses of decidedness in DECIDABILITY-INVENTORY.py.

usage: python3 -B apply_inventory.py W

Three theorems take the equality of conditions and use it only in their proofs (`same`), through
`Becoming.Propagation`: `gap_le_polynomial` through `gap_le_carried`, and `most_difference_within`
and `gap_polynomial_iff_no_loop` through `most_difference_arrives`, whose carrying law splits on
whether a level is the one that differs. Nothing else in the module takes a decision. The entries
go at the end of PROOF_KIND; a second run fails.
"""
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
path = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/DECIDABILITY-INVENTORY.py'
t = path.read_text()
assert "'gap_polynomial_iff_no_loop'" not in t, 'already classified'


def before(text, anchor, insert):
    assert text.count(anchor) == 1, (anchor, text.count(anchor))
    return text.replace(anchor, insert + anchor)


t = before(t, '}\n# Proved to need decidedness where asked of every world',
           '    # 2026-10-16, P118 how a carried difference grows (Becoming.Loops): the gap bounds of Propagation,\n'
           '    # gap_le_carried and most_difference_arrives, read the equality of conditions in their proofs\n'
           "    **{n: 'same' for n in ['most_difference_within', 'gap_le_polynomial', 'gap_polynomial_iff_no_loop']},\n")
path.write_text(t)
print('classified three proof-only theorems of Becoming.Loops')
