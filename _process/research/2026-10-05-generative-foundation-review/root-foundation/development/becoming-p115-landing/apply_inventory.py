#!/usr/bin/env python3
"""P115: classify Becoming.Propagation's uses of decidedness in DECIDABILITY-INVENTORY.py.

usage: python3 -B apply_inventory.py W

`mixCells` mixes one history into another at listed levels, each a step with a condition, telling
conditions apart as `mixIn` does (`mix`); `mixCells_either`, `mixCells_listed` and
`ExchangeLaw.exchangeGap_le_mixCells` name it in their statements. The other theorems use the
equality of conditions only in their proofs (`same`): the strengths add up by mixing the other
history in level by level (`ExchangeLaw.exchangeGap_le_strengths` and what is proved from it), and
the carrying law's strengths split on whether a level is the one that differs
(`ExchangeLaw.carrying_respondsWithin`, `most_difference_arrives`). No statement takes a decision
of anything beyond the equality of conditions. The entries go at the end of CONSTRUCTIONS and
PROOF_KIND; a second run fails.
"""
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
path = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/DECIDABILITY-INVENTORY.py'
t = path.read_text()
assert "'mixCells'" not in t, 'already classified'


def before(text, anchor, insert):
    assert text.count(anchor) == 1, (anchor, text.count(anchor))
    return text.replace(anchor, insert + anchor)


t = before(t, '}\nMENT_REASON = {',
           '    # 2026-10-16, P115 how much difference arrives (Becoming.Propagation): one history mixed into another at\n'
           '    # listed levels, each a step with a condition, as mixIn mixes condition by condition\n'
           "    'mixCells': 'mix',\n")
t = before(t, '}\n# Proved to need decidedness where asked of every world',
           '    # 2026-10-16, P115 how much difference arrives (Becoming.Propagation): the strengths add up by mixing the\n'
           '    # other history in level by level, and the carrying law splits on whether a level is the one that differs\n'
           "    **{n: 'same' for n in [\n"
           "        'ExchangeLaw.exchangeGap_le_strengths', 'ExchangeLaw.exchangeGap_le_strengths_listed',\n"
           "        'ExchangeLaw.exchangeGap_le_shares', 'ExchangeLaw.insensitiveAt_iff_strength_zero',\n"
           "        'ExchangeLaw.sensitive_iff_strength', 'gap_le_carried', 'ExchangeLaw.carrying_respondsWithin',\n"
           "        'most_difference_arrives', 'levels_alike_of_not_conveyed']},\n")
path.write_text(t)
print('classified mixCells and nine proof-only theorems of Becoming.Propagation')
