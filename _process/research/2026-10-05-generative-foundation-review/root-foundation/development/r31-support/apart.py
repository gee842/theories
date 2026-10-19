#!/usr/bin/env python3
"""R31: bring the apart register to the spine with one prelude.

* Two entries are no longer apart roots: `ListTests.length_append` and `Naturals.add_sub_cancel_left`, now in
  Becoming.Prelude, are used on the base since the copies whose users they took were removed. Their entries
  move to this kit's apart-retired.json with their bytes.
* `Copying.le_of_add_le_add` is now an apart root: its only user, `Copying.le_sub_of_add`, was removed as a copy
  of `Naturals.le_sub_of_add_le`. It gets a reason; its statement is unchanged.
* Every entry's module is its module in R31's receipt (ListTests, Naturals and Order are gone; the conditional
  split moved some theorems); categories and reasons are unchanged.

usage: python3 -B apart.py RECEIPT_ID   (from the checkout root; once)
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTER = HERE.parents[1] / 'THEOREM-CONNECTIVITY-APART.json'
RETIRED = HERE / 'apart-retired.json'
CHECKS = HERE.parents[5] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-checks'
r = json.load(open(CHECKS / sys.argv[1] / 'verification.json'))
home = {}
for m in r['modules']:
    for x in m.get('declarations', []):
        home[x['name'] if isinstance(x, dict) else x] = m['module']

register = json.loads(REGISTER.read_text())
retired = {
    'about': 'Apart-register entries retired by R31 (20 October 2026): the lemmas, now in Becoming.Prelude, are used on '
             'the base since R31 removed the copies whose users now read them (one name per statement). Bytes as they '
             'stood in THEOREM-CONNECTIVITY-APART.json.',
    'roots': {}}
for name in ('Becoming.ListTests.length_append', 'Becoming.Naturals.add_sub_cancel_left'):
    retired['roots'][name] = register['roots'].pop(name)
NEW = {
    'Becoming.Copying.le_of_add_le_add': {
        'module': 'Becoming.Copying', 'category': 'support',
        'reason': 'an arithmetic lemma of `Nat` proved without `propext`: adding the same amount on the left keeps no '
                  'more than the order. Its only user, Copying.le_sub_of_add, was removed by R31 as a copy of '
                  'Naturals.le_sub_of_add_le in Becoming.Prelude, so nothing uses it'},
}
for name, entry in NEW.items():
    assert name not in register['roots'], name
    register['roots'][name] = entry
moved = 0
for name, entry in register['roots'].items():
    assert name in home, name
    if entry['module'] != home[name]:
        entry['module'] = home[name]
        moved += 1
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=1) + '\n')
RETIRED.write_text(json.dumps(retired, ensure_ascii=False, indent=1) + '\n')
print('retired', len(retired['roots']), 'added', len(NEW), 'module updated', moved)
