#!/usr/bin/env python3
"""P58c: docstrings of the not-recurring theorems say what they state. Usage: docs_lean_p58c.py TREE"""
import sys
from pathlib import Path
B = Path(sys.argv[1]) / 'Becoming'
EDITS = {
 'Renewal.lean': [('from some step on falls only finitely often.', 'from some step on does not fall at arbitrarily late steps.'),
                  ('condition at each active step is active only finitely often.', 'condition at each active step is not active at arbitrarily late steps.'),
                  ('from step `T` on falls only finitely often. -/', 'from step `T` on does not fall at arbitrarily late steps. -/'),
                  ('is active only finitely often. -/', 'is not active at arbitrarily late steps. -/')],
 'Change.lean': [('never rising from some step on falls only\n  finitely often', 'never rising from some step on does not\n  fall at arbitrarily late steps'),
                 ('never rises from some step on falls only finitely often. -/', 'never rises from some step on does not fall at arbitrarily late steps. -/')],
 'Generation.lean': [('  is active only finitely often, however', '  is not active at arbitrarily late steps, however'),
                     ('consume it, and arising stops (`Growth.ceases`).', 'consume it, and arising does not recur (`Growth.ceases`).'),
                     ('active only finitely often. -/', 'not active at arbitrarily late steps. -/'),
                     ('\nstops. -/', '\ndoes not recur. -/')],
 'Recurrence.lean': [('* **A marked change stops.**', '* **A marked change does not recur.**'),
                     ('and a marked change stops.', 'and a marked change does not recur.'),
                     ('**A marked change ends within finitely many configurations.**', '**Within finitely many configurations, a marked change does not recur.**')],
 'Reserve.lean': [('  step on is active only finitely often (`Carries.active_not_recurring`)', '  step on is not active at arbitrarily late steps (`Carries.active_not_recurring`)'),
                  ('unsupported, a formation arises only finitely often\n', 'unsupported, a formation does not arise at arbitrarily late steps\n'),
                  ('a formation is active only finitely often:', 'a formation is not active at arbitrarily late steps:'),
                  ('from step `T` on, a formation is active only finitely often. -/', 'from step `T` on, a formation is not active at arbitrarily late steps. -/'),
                  ('a formation arises only finitely often. -/', 'a formation does not arise at arbitrarily late steps. -/'),
                  ('a formation arises only finitely often: dormancy', 'a formation does not arise at arbitrarily late steps: dormancy')],
}
for name, pairs in EDITS.items():
    p = B / name; t = p.read_text()
    for old, new in pairs:
        assert t.count(old) == 1, (name, t.count(old), old)
        t = t.replace(old, new)
    p.write_text(t)
print('ok')
p = B / 'Reserve.lean'; t = p.read_text()
for old, new in [('with a reserve is active only finitely often, at most as often as its reserve after the\nloss (`Carries.lasts`).',
                  'with a reserve is not active at arbitrarily late steps, and over any stretch at most as often\nas its reserve after the loss (`Carries.lasts`).'),
                 ('positive need, with a reserve, is active only finitely often, at most as often as its\nreserve when the relatum ended (`Carries.lasts`).',
                  'positive need, with a reserve, is not active at arbitrarily late steps, and over any stretch at\nmost as often as its reserve when the relatum ended (`Carries.lasts`).')]:
    assert t.count(old) == 1, old
    t = t.replace(old, new)
p.write_text(t)
print('reserve ok')
