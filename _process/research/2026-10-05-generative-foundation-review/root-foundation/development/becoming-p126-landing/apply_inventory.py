#!/usr/bin/env python3
"""P126: classify Becoming.Tail's use of decidedness in DECIDABILITY-INVENTORY.py.

usage: python3 -B apply_inventory.py W

Four definitions taking a rule are indicators of a decided proposition (`indicate`), as the tail
law and the indicator of vanishing already are: whether levels vanish from a condition on
(`vanishesFrom`) and whether some level from it on is above zero (`raisedFrom`), each a Boolean
decided by the rule, the indicator of never vanishing (`neverIndicator`) and its law (`neverLaw`).
Statements mentioning them are classified through them. Two theorems use their rule only in their
proofs, splitting on its two cases (`split`), as `lpo_of_vanish_decided` does: `WLPO.of_rule` and
`LPO.of_rule`. The definitions building rules (`mixedDecision` and the others) are rows of
decidedness proved and need no classification. The entries go at the end of CONSTRUCTIONS and of
PROOF_KIND; a second run fails.
"""
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
path = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/DECIDABILITY-INVENTORY.py'
t = path.read_text()
assert "'neverIndicator'" not in t and "'WLPO.of_rule'" not in t, 'already classified'


def before(text, anchor, insert):
    assert text.count(anchor) == 1, (anchor, text.count(anchor))
    return text.replace(anchor, insert + anchor)


t = before(t, '}\nMENT_REASON = {',
           '    # 2026-10-16, P126 what a law of the whole and no part takes (Becoming.Tail): whether levels vanish\n'
           '    # from a condition on, or some level from it on is above zero, decided by a rule, the indicator of\n'
           '    # never vanishing and its law\n'
           "    **{n: 'indicate' for n in ['vanishesFrom', 'raisedFrom', 'neverIndicator', 'neverLaw']},\n")
t = before(t, '}\n# Proved to need decidedness where asked of every world',
           '    # 2026-10-16, P126 what a law of the whole and no part takes (Becoming.Tail): a rule gives the\n'
           '    # principle by both its cases\n'
           "    **{n: 'split' for n in ['WLPO.of_rule', 'LPO.of_rule']},\n")
path.write_text(t)
print('classified four definitions and two proof-only theorems of Becoming.Tail')
