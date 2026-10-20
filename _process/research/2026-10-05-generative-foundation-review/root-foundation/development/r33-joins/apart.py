#!/usr/bin/env python3
"""R33: bring the apart register to the run with the joins.

* `Naturals.add_le_of_le_sub` is no longer an apart root: G7's `Tolerance.allBut_sub_iff`, on the base
  through the tolerating law's run, uses it. Its entry moves to this kit's apart-retired.json with its bytes.
* `Interleavings.LocalLaw.standings_of_interleavings` (G10) is an apart root: the course of standings of a
  local law, on any state type, is stated in the module's own vocabulary; what of it the World reads is
  on the base (`world_final`, `world_swap`, `world_swap_between`).

usage: python3 -B apart.py   (once)"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTER = HERE.parents[1] / 'THEOREM-CONNECTIVITY-APART.json'
RETIRED = HERE / 'apart-retired.json'

register = json.loads(REGISTER.read_text())
GONE = ['Becoming.Naturals.add_le_of_le_sub']
retired = {
    'about': 'Apart-register entries retired by R33 (20 October 2026): each names a theorem that is no longer an '
             'apart root, because a theorem on the base now uses it. Bytes as they stood in '
             'THEOREM-CONNECTIVITY-APART.json.',
    'roots': {}}
for name in GONE:
    retired['roots'][name] = register['roots'].pop(name)
NEW = {
    'Becoming.Interleavings.LocalLaw.standings_of_interleavings': {
        'module': 'Becoming.Interleavings',
        'category': 'general-structure',
        'reason': "two interleavings of the same own courses give each relatum the same course of standings, for a "
                  "local law on any state type: the per-relatum course is the module's own vocabulary, which the "
                  "step-indexed World does not index; what the World reads of it is on the base (`world_final`, "
                  "`world_swap`, `world_swap_between`)"},
}
for name, entry in NEW.items():
    assert name not in register['roots'], name
    register['roots'][name] = entry
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=1) + '\n')
RETIRED.write_text(json.dumps(retired, ensure_ascii=False, indent=1) + '\n')
print('retired', len(GONE), 'added', len(NEW))
