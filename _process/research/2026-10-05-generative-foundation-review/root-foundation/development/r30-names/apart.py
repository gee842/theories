#!/usr/bin/env python3
"""R30: the apart register follows the rename table. An entry whose theorem was renamed is keyed by the new name, with
its category unchanged, its module renamed where the module was, and the names in its reason renamed by text.py's rule
for records; the reason's words do not change. Statements are unchanged, so no theorem changes class.

usage: python3 -B apart.py   (from the checkout root; once, on main before R30's register)"""
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTER = HERE.parents[1] / 'THEOREM-CONNECTIVITY-APART.json'
spec = importlib.util.spec_from_file_location('r30text', HERE / 'text.py')
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)
TABLE = json.loads((HERE / 'RENAME-TABLE.json').read_text())
REN, MODS = TABLE['declarations'], TABLE['modules']

register = json.loads(REGISTER.read_text())
roots, renamed, edited = {}, 0, 0
for name, entry in register['roots'].items():
    new = REN.get(name, name)
    renamed += new != name
    e = dict(entry)
    e['module'] = MODS.get(e['module'], e['module'])
    e['reason'] = T.rewrite_text(e['reason'], True)
    edited += e != entry
    assert new not in roots, new
    roots[new] = e
register['roots'] = roots
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=1) + '\n')
print('renamed', renamed, 'entries changed', edited)
