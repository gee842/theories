#!/usr/bin/env python3
"""R28: move the apart-register entries that are no longer apart roots to this kit's apart-retired.json.

With `Law.Lossless`, `Law.Returns`, `Law.Reachable` and the others abbreviations at `Law.process next`, the
orbit forms of the recurrence laws reach the Process family by definition, so `THEOREM-CONNECTIVITY.py --check`
reports their register entries as no longer apart roots. Their statements are unchanged; the entries move here
with their bytes, as the F3 sweep kept its retired entries.

usage: python3 -B retire_apart.py NAME ...   (from the checkout root)
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTER = HERE.parents[1] / 'THEOREM-CONNECTIVITY-APART.json'
RETIRED = HERE / 'apart-retired.json'

register = json.loads(REGISTER.read_text())
retired = json.loads(RETIRED.read_text()) if RETIRED.exists() else {
    'about': 'Apart-register entries retired by R28 (20 October 2026): with Law.* abbreviations at Law.process, '
             'these theorems reach the Process family by definition and are no longer apart roots. Bytes as they '
             'stood in THEOREM-CONNECTIVITY-APART.json.',
    'roots': {}}
for name in sys.argv[1:]:
    retired['roots'][name] = register['roots'].pop(name)
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=1) + '\n')
RETIRED.write_text(json.dumps(retired, ensure_ascii=False, indent=1) + '\n')
print(len(sys.argv) - 1, 'retired')
