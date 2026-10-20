#!/usr/bin/env python3
"""R37: bring the apart register to the run after lens B.

* `CrossSituational.distinct_iff` is gone: with one `Distinct` (B6) its statement was `Distinct l ↔ Distinct l`,
  so it was removed with no replacement. Its entry moves to this kit's apart-retired.json with its bytes.
* `Frequency.count_from` becomes an apart root: `Frequency.SelfLoop.onset_amount`, the only theorem that used it,
  was removed as the same statement as `Closing.Onset.amount_after` (B6). It is a counting lemma of the module's
  own `count`, registered as support.

usage: python3 -B apart.py   (once)"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTER = HERE.parents[1] / 'THEOREM-CONNECTIVITY-APART.json'
RETIRED = HERE / 'apart-retired.json'

register = json.loads(REGISTER.read_text())
GONE = ['Becoming.CrossSituational.distinct_iff']
retired = {
    'about': 'Apart-register entries retired by R37 (20 October 2026): each names a theorem removed by lens B of the '
             'twentieth review (B6), whose statement became trivial once the definition twins were stated once. '
             'Bytes as they stood in THEOREM-CONNECTIVITY-APART.json.',
    'roots': {}}
for name in GONE:
    retired['roots'][name] = register['roots'].pop(name)
register['roots']['Becoming.Frequency.count_from'] = {
    'module': 'Becoming.Frequency',
    'category': 'support',
    'reason': "a counting lemma of the module's own `count`: marking the steps from `T`, `r` are counted by `T + r`; "
              "since R37 the onset's doubling is stated once, by `Closing.Onset.amount_after`, which does not use it"}
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=1) + '\n')
RETIRED.write_text(json.dumps(retired, ensure_ascii=False, indent=1) + '\n')
print('retired', len(GONE), 'added 1')
