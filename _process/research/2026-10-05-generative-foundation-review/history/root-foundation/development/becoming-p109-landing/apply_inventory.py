#!/usr/bin/env python3
"""P109: classify Becoming.Coupling's uses of decidedness in DECIDABILITY-INVENTORY.py.

usage: python3 -B apply_inventory.py W

`policyUpto` is a construction that tells configurations apart; `lumped_upto_iff` uses decidedness only
in its proof, to tell configurations apart; `no_policy_upto_iff` and `throughout_or_fails` use it only
in their proofs, to find a step. The entries go at the end of CONSTRUCTIONS and PROOF_KIND; a second
run fails.
"""
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
path = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/DECIDABILITY-INVENTORY.py'
t = path.read_text()
assert "'policyUpto'" not in t, 'already classified'


def before(text, anchor, insert):
    assert text.count(anchor) == 1, (anchor, text.count(anchor))
    return text.replace(anchor, insert + anchor)


t = before(t, '}\nMENT_REASON = {',
           '    # 2026-10-15, P109 where a move is formed (Becoming.Coupling): the policy read off a finite stretch compares\n'
           '    # configurations\n'
           "    'policyUpto': 'same',\n")
t = before(t, '}\n# Proved to need decidedness where asked of every world',
           '    # 2026-10-15, P109 where a move is formed (Becoming.Coupling): the policy on a finite stretch is built by comparing\n'
           '    # configurations; where none exists, a configuration recurring with the move varied is found\n'
           "    'lumped_upto_iff': 'same', 'no_policy_upto_iff': 'find', 'throughout_or_fails': 'find',\n")
path.write_text(t)
print('classified policyUpto, lumped_upto_iff, no_policy_upto_iff, throughout_or_fails')
