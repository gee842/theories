#!/usr/bin/env python3
"""R46: bring the apart register to the run after one renumbering of interleavings.

One new apart root, with its category and reason:
* `Interleavings.Pair.idle_unmatched`: two lists of the pair with the same own courses, one with an exchange the
  other has at no step (a model witness: the premise `Touching` is needed).

One entry leaves the register, being no longer an apart root: `Interleavings.LocalLaw.firstAt_least`, which
`firstAt_after` now uses on the way to the renumbering's laws on the World.

usage: python3 -B apart.py   (once)"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTER = HERE.parents[1] / 'THEOREM-CONNECTIVITY-APART.json'
register = json.loads(REGISTER.read_text())
NEW = {
    'Becoming.Interleavings.Pair.idle_unmatched': ('Becoming.Interleavings', 'model-witness',
        'the lists [2] and [] of the pair give every relatum the same own course, while [2] has at step 0 an '
        'exchange that [] has at no step: a fact about one constructed model, showing the premise `Touching` of the '
        'renumbering is needed'),
}
GONE = ['Becoming.Interleavings.LocalLaw.firstAt_least']
for name, (module, category, reason) in NEW.items():
    assert name not in register['roots'], name
    register['roots'][name] = {'module': module, 'category': category, 'reason': reason}
for name in GONE:
    assert name in register['roots'], name
    del register['roots'][name]
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=1) + '\n')
print('registered', sorted(NEW), 'removed', GONE)
