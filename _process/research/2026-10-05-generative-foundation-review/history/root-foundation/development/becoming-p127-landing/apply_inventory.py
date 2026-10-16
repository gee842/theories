#!/usr/bin/env python3
"""P127: classify Becoming.Onward's use of decidedness in DECIDABILITY-INVENTORY.py.

usage: python3 -B apply_inventory.py W

One definition takes decisions: the test of each enumerated move (`Onward.decidedTest`), true
exactly where the step is taken and its target is in the family, an indicator of a decided
proposition (`indicate`). The statement mentioning it (`Onward.decidedTest_finds`) is classified
through it. `Onward.run_decided` proves a proposition decided and needs no classification. The
entry goes at the end of CONSTRUCTIONS; a second run fails.
"""
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
path = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/DECIDABILITY-INVENTORY.py'
t = path.read_text()
assert "'Onward.decidedTest'" not in t, 'already classified'
anchor = '}\nMENT_REASON = {'
assert t.count(anchor) == 1
t = t.replace(anchor,
              '    # 2026-10-16, P127 where a run goes on (Becoming.Onward): the test of each enumerated move, true where\n'
              '    # the step is taken and its target is in the family\n'
              "    'Onward.decidedTest': 'indicate',\n" + anchor)
path.write_text(t)
print('classified one definition of Becoming.Onward')
