#!/usr/bin/env python3
"""R29: bring the apart register to the compressed spine.

* The entries of the two whole-number restatements R29 removed (`whole_falls_not_recurring`,
  `whole_falls_stop_unrefuted`) move to this kit's apart-retired.json with their bytes.
* Four theorems whose only user was a removed second name are now apart roots; each gets a reason.
  Their statements are unchanged.

usage: python3 -B apart.py   (from the checkout root; once)
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTER = HERE.parents[1] / 'THEOREM-CONNECTIVITY-APART.json'
RETIRED = HERE / 'apart-retired.json'

register = json.loads(REGISTER.read_text())
retired = {
    'about': 'Apart-register entries retired by R29 (20 October 2026): the theorems were removed as second names of '
             'statements proved once (falls_not_recurring in Becoming.Renewal, falls_stop_unrefuted in Becoming.Space, '
             'now proved as the whole-number instance of Becoming.Amounts). Bytes as they stood in '
             'THEOREM-CONNECTIVITY-APART.json.',
    'roots': {}}
for name in ('Becoming.whole_falls_not_recurring', 'Becoming.whole_falls_stop_unrefuted'):
    retired['roots'][name] = register['roots'].pop(name)
NEW = {
    'Becoming.Dependence.level_registers': {
        'module': 'Becoming.Likeness', 'category': 'support',
        'reason': 'a one-line lemma: the claims reading a condition\'s level tell its levels apart. With it determinacy '
                  'is the case of Dependence.dichotomy_of_determinedAt that Joint\'s Dependence.determined_dichotomy '
                  'states; R29 removed the second name that used it, and determinacy-up-to-likeness cites it'},
    'Becoming.ExchangeLaw.Nonanticipating.readsFinitely_of_every': {
        'module': 'Becoming.Sensitivity', 'category': 'general-structure',
        'reason': 'with finitely many conditions every law of what has stood reads finitely many: a law of every law of '
                  'exchange, on the base once instantiated; through it Counterfactual\'s '
                  'ExchangeLaw.Nonanticipating.through_sensitive is a case of ExchangeLaw.ReadsFinitely.through_sensitive '
                  '(R29 removed the second name that stated so)'},
    'Becoming.no_chain_of_no_loop_listed': {
        'module': 'Becoming.Remainder', 'category': 'general-structure',
        'reason': 'with every condition listed and no loop upstream, no chain in time order of as many couplings as '
                  'there are conditions ends at a condition: a law of every coupling schedule, in its own vocabulary; it '
                  'is why carriedWithin_exact_of_no_loop of Becoming.Loops holds (R29 removed Remainder\'s second name '
                  'for that statement)'},
    'Becoming.unrefuted_falls_exceed': {
        'module': 'Becoming.Space', 'category': 'support',
        'reason': 'the counting step of the whole-number descent: an amount not rising whose later falls are not refuted '
                  'exceeds every bound. Since R29 falls_stop_unrefuted is proved as the whole-number instance of '
                  'Amounts.rests_unrefuted, so nothing on the base uses it; space-and-its-parts cites it'},
}
for name, entry in NEW.items():
    assert name not in register['roots'], name
    register['roots'][name] = entry
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=1) + '\n')
RETIRED.write_text(json.dumps(retired, ensure_ascii=False, indent=1) + '\n')
print('retired', len(retired['roots']), 'added', len(NEW))
