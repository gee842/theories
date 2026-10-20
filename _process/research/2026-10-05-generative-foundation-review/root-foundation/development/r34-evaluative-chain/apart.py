#!/usr/bin/env python3
"""R34: bring the apart register to the run with Ranking and ActiveReading read on webs (F9).

`Ranking.active_of_renewed` and `ActiveReading.absent_included` are no longer apart roots: once a world of
the readings is a web (`W → Web F C`), their statements use `Web.Renewed` and the web's activity, on the
World/Flow/Web family, where before they used the foundation's `RelationalRenewal.Unfolding`. Their entries
move to this kit's apart-retired.json with their bytes. No root is added.

usage: python3 -B apart.py   (once)"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTER = HERE.parents[1] / 'THEOREM-CONNECTIVITY-APART.json'
RETIRED = HERE / 'apart-retired.json'

register = json.loads(REGISTER.read_text())
GONE = ['Becoming.Ranking.active_of_renewed', 'Becoming.ActiveReading.absent_included']
retired = {
    'about': 'Apart-register entries retired by R34 (20 October 2026): each names a theorem that is no longer an '
             'apart root, because its statement now reads a web (F9 of the twentieth review). Bytes as they stood in '
             'THEOREM-CONNECTIVITY-APART.json.',
    'roots': {}}
for name in GONE:
    retired['roots'][name] = register['roots'].pop(name)
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=1) + '\n')
RETIRED.write_text(json.dumps(retired, ensure_ascii=False, indent=1) + '\n')
print('retired', len(GONE))
