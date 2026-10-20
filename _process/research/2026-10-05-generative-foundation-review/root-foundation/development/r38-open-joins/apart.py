#!/usr/bin/env python3
"""R38: bring the apart register to the run after the open joins (G6, G10).

Three new apart roots, each with its category and reason:
* `Interleavings.LocalLaw.index_matches`: where a relatum takes an exchange at a step of one list, the index map
  sends the next step to the step after the same exchange in the other list. A law of the lists of exchanges for a
  local law on any state type; the World an interleaving builds records amounts, not which exchange stands at a
  step, so the base supplies no reading of the matching (general structure, as `standings_of_interleavings` was).
* `Interleavings.LocalLaw.firstAt_least`: the step `firstAt` finds is the least with the count (support: an
  unpacking of the module's own definition).
* `LoopReturn.Ring.givesExactly`: the ring meets the premise of the exact turn (a model witness).

Two entries leave the register, being no longer apart roots: `standings_of_interleavings`, which the index
laws read on the base through `standingAfter_of_interleavings` and `world_index`, and `Naturals.add_left_cancel`,
which the cycle laws of LoopReturn now use.

usage: python3 -B apart.py   (once)"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTER = HERE.parents[1] / 'THEOREM-CONNECTIVITY-APART.json'
register = json.loads(REGISTER.read_text())
NEW = {
    'Becoming.Interleavings.LocalLaw.index_matches': ('Becoming.Interleavings', 'general-structure',
        'where a relatum takes an exchange at a step of one interleaving, the index map sends the next step to the '
        'step after the same exchange in the other, for a local law on any state type: which exchange stands at a step '
        'is the module\'s own vocabulary (lists of exchanges), which the World an interleaving builds does not record; '
        'what the World reads of the index map is on the base (`world_index`, `world_reads_alike`)'),
    'Becoming.Interleavings.LocalLaw.firstAt_least': ('Becoming.Interleavings', 'support',
        'the step `firstAt` finds is the least at which the relatum has taken the given number of its own exchanges: '
        'an unpacking of the module\'s own definition, used by `index_matches`'),
    'Becoming.LoopReturn.Ring.givesExactly': ('Becoming.LoopReturn', 'model-witness',
        'the ring of m + 2 conditions meets the premise of the exact turn (`GivesExactly`), so `carried_around_exact` '
        'applies to it: a fact about one constructed model'),
}
GONE = ['Becoming.Interleavings.LocalLaw.standings_of_interleavings', 'Becoming.Naturals.add_left_cancel']
for name, (module, category, reason) in NEW.items():
    assert name not in register['roots'], name
    register['roots'][name] = {'module': module, 'category': category, 'reason': reason}
for name in GONE:
    assert name in register['roots'], name
    del register['roots'][name]
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=1) + '\n')
print('registered', sorted(NEW), 'removed', GONE)
