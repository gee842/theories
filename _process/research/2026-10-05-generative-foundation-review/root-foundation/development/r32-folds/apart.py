#!/usr/bin/env python3
"""R32: bring the apart register to the run without forwarders, copies and reading modules.

* Seven entries name theorems R32 removed (six pure forwarders, one copy stated once in the prelude); they
  move to this kit's apart-retired.json with their bytes.
* Three laws the removed forwarders restated are now apart roots in their place; each takes the
  category and reason of the forwarder's entry, said of the law itself.
* Every entry's module is the module that now holds it (the folds moved some).

usage: python3 -B apart.py   (once; the instance entries are instances.py's)"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'r31-support'))
import decltext  # noqa: E402

REGISTER = HERE.parents[1] / 'THEOREM-CONNECTIVITY-APART.json'
RETIRED = HERE / 'apart-retired.json'
home = {d['full']: d['module'] for d in decltext.decls()}

register = json.loads(REGISTER.read_text())
GONE = ['Becoming.Copying.le_of_add_le_add', 'Becoming.Ideals.hull_hull', 'Becoming.Ideals.hull_not_interior_compl',
        'Becoming.Ideals.interior_sub', 'Becoming.PartialReadout.parity_exact',
        'Becoming.Requirement.Handover.crossed_unranked', 'Becoming.Weights.truncation']
retired = {
    'about': 'Apart-register entries retired by R32 (20 October 2026): each names a theorem R32 removed, a pure '
             'forwarder (B10) or a copy of a statement now stated once in Becoming.Prelude (B9). Bytes as they stood '
             'in THEOREM-CONNECTIVITY-APART.json.',
    'roots': {}}
for name in GONE:
    assert name not in home, name
    retired['roots'][name] = register['roots'].pop(name)
NEW = {
    'Becoming.Ideals.AdheresBy.adheres': {
        'category': 'restates',
        'reason': "the hull's idempotence for any family of ideals (what adheres to the classes adhering to a "
                  "class adheres to it); its case of runs is Horizon's `Adheres.adheres`, on the base. It took the "
                  "entry of `Ideals.hull_hull`, the forwarder R32 removed"},
    'Becoming.Lexical.Crossed.incomparable': {
        'category': 'model-witness',
        'reason': 'crossed tiers leave the two alternatives unranked; read in the constructed handover model of '
                  '`Becoming.Frontier` (AlignmentDirection, ported by F3J). It took the entry of '
                  '`Requirement.Handover.crossed_unranked`, the forwarder R32 removed'},
    'Becoming.PartialReadout.paired_exact': {
        'category': 'model-witness',
        'reason': 'a fact about the constructed channel model (exactness surviving compression); the general law '
                  'is read on runs as `Runs.retained_exact`. It took the entry of `PartialReadout.parity_exact`, the '
                  'forwarder R32 removed'},
}
for name, entry in NEW.items():
    assert name not in register['roots'] and name in home, name
    register['roots'][name] = {'module': home[name], **entry}
moved = 0
for name, entry in register['roots'].items():
    if name in home and entry['module'] != home[name]:
        entry['module'] = home[name]
        moved += 1
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=1) + '\n')
RETIRED.write_text(json.dumps(retired, ensure_ascii=False, indent=1) + '\n')
print('retired', len(retired['roots']), 'added', len(NEW), 'module updated', moved)
