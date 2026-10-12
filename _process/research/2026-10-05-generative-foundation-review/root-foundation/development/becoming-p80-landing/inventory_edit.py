#!/usr/bin/env python3
"""P80's decidability uses, classified in the inventory tool (`DECIDABILITY-INVENTORY.py`) before it is rerun:
python3 -B inventory_edit.py W

`Becoming.Counterfactual`'s sensitivity section takes `[DecidableEq C]`. `mixIn` (a history with another mixed in on
the conditions of a list) is a decidability-taking definition, so the statements mentioning it depend on decidedness;
its reason is new: it tells conditions apart. The theorems using decidedness only in their proofs split on whether two
conditions are the same ("tells same from different"); each has a form with no decision procedure. Every anchor must
occur exactly once."""
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
INV = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/DECIDABILITY-INVENTORY.py'
s = INV.read_text()
assert "'mixIn'" not in s, 'already classified'

PROOF_ONLY = ['alike_of_sensitive_agree', 'ExchangeLaw.Nonanticipating.through_of_observed',
              'ExchangeLaw.Nonanticipating.through_sensitive', 'comparison_through_sensitivity']
FORMS = {
    'alike_of_sensitive_agree': '`ExchangeLaw.Nonanticipating.through_all`（经识一切，不判定 / through registering '
                                'everything, no decision, P80）',
    'ExchangeLaw.Nonanticipating.through_of_observed': '`ExchangeLaw.Nonanticipating.through_all`（不判定 / no decision, '
                                                       'P80）；逆向 `ExchangeLaw.Through.registers_of_sensitive`（不判定 / '
                                                       'the converse, no decision）',
    'ExchangeLaw.Nonanticipating.through_sensitive': '`ExchangeLaw.Nonanticipating.through_all`（不判定 / no decision, '
                                                     'P80）；逆向 `ExchangeLaw.Through.registers_of_sensitive`（不判定 / '
                                                     'the converse, no decision）',
    'comparison_through_sensitivity': '`comparison_of_courses`（经律所经的识，不判定 / through a registration the law '
                                      'reads through, no decision, P80）',
}


def once(s, old, new):
    assert s.count(old) == 1, (old[:60], s.count(old))
    return s.replace(old, new)


s = once(s, "    'adjoin': 'once',\n}", "    'adjoin': 'once', 'mixIn': 'mix',\n}")
s = once(s, "    'once': '不重复的列表：成员关系已定 / a list without repetition: membership decided',\n}",
         "    'once': '不重复的列表：成员关系已定 / a list without repetition: membership decided',\n"
         "    'mix': '逐个条件换入另一段历史：需分辨条件的相同 / another history mixed in condition by condition: tells '\n"
         "           'conditions apart',\n}")
s = once(s, "    'indicate': '造出指示 / builds an indicator',\n}",
         "    'indicate': '造出指示 / builds an indicator', 'mix': '逐个条件换入 / mixed in condition by condition',\n}")
s = once(s, "        'Law.none_drawn_lossless', 'Law.lossless_iff_none_drawn']},",
         "        'Law.none_drawn_lossless', 'Law.lossless_iff_none_drawn',\n        "
         + ', '.join(f"'{n}'" for n in PROOF_ONLY) + "]},")
forms = ''.join(f"    '{k}': '{v}',\n" for k, v in FORMS.items())
anchor = "    'Web.scores_alike_iff': "
i = s.index(anchor)
j = s.index('\n}\n', i) + 1
assert s.count(anchor) == 1
s = s[:j] + forms + s[j:]
INV.write_text(s)
print('classified mixIn and', len(PROOF_ONLY), 'proof-only theorems')
