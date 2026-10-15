#!/usr/bin/env python3
"""P113: classify Becoming.Sensitivity's uses of decidedness in DECIDABILITY-INVENTORY.py.

usage: python3 -B apply_inventory.py W

`vanishIndicator` and `tailLaw` are constructions taking the decision of vanishing (`indicate`): the
tail law exchanges the indicator of whether levels vanish from some condition on. The theorems of
the least registration with any number of conditions use the equality of conditions only in their
proofs, mixing one history into another condition by condition (`same`), as in
`Becoming.Counterfactual`; their forms with no decision are the same as there. `lpo_of_vanish_decided`
uses the decision of vanishing only in its proof, taking both its cases (`split`). The theorems
whose results are the weak limited principle or a decided sequence (`WLPO.of_lpo`, `mixed_decides`,
`wlpo_of_insensitive_differs`, `wlpo_of_not_through_sensitive`) are rows proving decidedness and need
no classification. The entries go at the end of FORMS, CONSTRUCTIONS and PROOF_KIND; a second run
fails.
"""
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
path = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/DECIDABILITY-INVENTORY.py'
t = path.read_text()
assert "'tailLaw'" not in t, 'already classified'


def before(text, anchor, insert):
    assert text.count(anchor) == 1, (anchor, text.count(anchor))
    return text.replace(anchor, insert + anchor)


FORM = ("'`ExchangeLaw.ReadsFinitely.nonanticipating` 与 `ExchangeLaw.Nonanticipating.through_all`（经识一切，不判定 / "
        "through registering everything, no decision, P113）；逆向 `ExchangeLaw.Through.registers_of_sensitive`（不判定 / the "
        "converse, no decision）'")
t = before(t, '}\n\n# Why a statement depends on decidedness',
           '    # 2026-10-15, P113 the least registration with any number of conditions (Becoming.Sensitivity)\n'
           + ''.join(f"    '{n}': {FORM},\n" for n in [
               'alike_of_sensitive_agree_within', 'ExchangeLaw.ReadsFinitely.through_of_observed',
               'ExchangeLaw.ReadsFinitely.through_sensitive', 'ExchangeLaw.ReadsFinitely.least_registration',
               'ExchangeLaw.Nonanticipating.through_sensitive_of_every'])
           + "    'comparison_through_sensitivity_of_readsFinitely': '`comparison_of_courses`（经律所经的识，不判定 / through a "
             "registration the law reads through, no decision, P113）',\n")
t = before(t, '}\nMENT_REASON = {',
           '    # 2026-10-15, P113 the least registration with any number of conditions (Becoming.Sensitivity): the tail law\n'
           '    # exchanges the indicator of whether levels vanish from some condition on, given its decision\n'
           "    'vanishIndicator': 'indicate', 'tailLaw': 'indicate',\n")
t = before(t, '}\n# Proved to need decidedness where asked of every world',
           '    # 2026-10-15, P113 the least registration with any number of conditions (Becoming.Sensitivity): one history is\n'
           '    # mixed into another condition by condition, as in Becoming.Counterfactual; the decision of vanishing gives LPO\n'
           '    # by both its cases\n'
           "    **{n: 'same' for n in [\n"
           "        'alike_of_sensitive_agree_within', 'ExchangeLaw.ReadsFinitely.through_of_observed',\n"
           "        'ExchangeLaw.ReadsFinitely.through_sensitive', 'ExchangeLaw.ReadsFinitely.least_registration',\n"
           "        'ExchangeLaw.Nonanticipating.through_sensitive_of_every', 'comparison_through_sensitivity_of_readsFinitely',\n"
           "        'alike_of_insensitiveAt_within', 'ExchangeLaw.ReadsFinitely.alike_of_insensitive']},\n"
           "    'lpo_of_vanish_decided': 'split',\n")
path.write_text(t)
print('classified vanishIndicator, tailLaw, eight proof-only theorems of the least registration, lpo_of_vanish_decided')
