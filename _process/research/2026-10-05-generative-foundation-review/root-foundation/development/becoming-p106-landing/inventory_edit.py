#!/usr/bin/env python3
"""Classify Becoming.Learnable's proof-only uses of decidedness in DECIDABILITY-INVENTORY.py.

    python3 -B inventory_edit.py W

Run before regenerating the inventory on the checked bytes; then `zero_count.py W` (landing kit). Read off the module:
- statements depending on decidedness need no entry: `rests_through` and `Pair.whole_rests` mention the learner
  (`refute`), `firstFit_congr` mentions `Identification.firstFit` (`first`); `Pair.whole_rests` has no binder, Bool's
  equality is a proved instance (counted under decidedness proved);
- `withWorldAt`, `withWorld` take `DecidableEq R` and no theorem statement mentions them;
- proof only: `refuted_on_one` splits on whether the claim is the target's value (`same`); `learnable_iff` finds the first
  configuration of the list whose record is the one read, and `learnable_of_lumped` and `still_learnable_iff_lumped`
  go through it (`find`).
Entries go inside the dictionaries, before entries other packages anchor on at their ends."""
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
p = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/DECIDABILITY-INVENTORY.py'
s = p.read_text()
pairs = [
    ("    'Learning.determines_lumped_iff': '`Learning.lumped_determines`（无前提的一个方向 / one direction, no premise, P73）',\n",
     "    'Learning.determines_lumped_iff': '`Learning.lumped_determines`（无前提的一个方向 / one direction, no premise, P73）',\n"
     "    'Learnable.refuted_on_one': '`Learnable.claim_not_right_on_both`（无前提：主张不在两者上都对 / no premise: the '\n"
     "                                'claim is not right on both）',\n"
     "    'Learnable.learnable_iff': '`Learnable.agree_of_rests_both`（必要一侧，对每个学习者，不判定 / the necessary side, of '\n"
     "                               'every learner, no decision）',\n"
     "    'Learnable.still_learnable_iff_lumped': '`Learnable.still_lumped_of_rests`（必要一侧，不判定 / the necessary side, '\n"
     "                                            'no decision）',\n"),
    ("        'Learning.determines_lumped_iff']},",
     "        'Learning.determines_lumped_iff', 'Learnable.learnable_iff', 'Learnable.learnable_of_lumped',\n"
     "        'Learnable.still_learnable_iff_lumped']},"),
    ("        'Learning.every_determines_nothing',\n",
     "        'Learning.every_determines_nothing', 'Learnable.refuted_on_one',\n"),
]
for a, b in pairs:
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)
p.write_text(s)
print('edited', p.relative_to(W))
