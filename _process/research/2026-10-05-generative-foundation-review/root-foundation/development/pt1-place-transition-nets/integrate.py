#!/usr/bin/env python3
"""Join PT1's module to the core package: import Becoming.PlaceTransitionNets after Becoming.Reading,
add its root doc bullet after Reading's, its CORE entry and scope text in check_becoming.py, and its
README row after Reading's. The module itself is already at its package path.
usage: python3 -B integrate.py   (PT1_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['PT1_ROOT']).resolve() if os.environ.get('PT1_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
assert (PKG / 'Becoming' / 'PlaceTransitionNets.lean').exists()


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


DOC = (
    '* `Becoming.PlaceTransitionNets` (L4): place/transition nets (Petri nets; reaction networks with\n'
    '  whole-number counts), a formalism defined outside the theory by its own rules, read on the\n'
    '  spine. The net is a law of exchange reading nothing, its course along a schedule is its flow,\n'
    '  and along a firing sequence the levels the law generates are its markings. The flow balances\n'
    '  the markings exactly where the schedule is a firing sequence; enabling gives feasibility, which\n'
    '  is enabling exactly for pure nets fired one transition at a time (a catalyst and a concurrent\n'
    '  step are feasible and do not fire). For finitely many places the flow is dissipative exactly\n'
    '  where every fired transition loses weighted tokens (a strict P-subinvariant), and every step\n'
    '  is enclosed. So rising with falling, the bound of the consuming firings by the initial\n'
    '  weighted tokens, rest unrefuted (flow and world forms) and, for a place every producer of\n'
    '  which consumes it, the joint-excess law as the siphon law hold of every such net; the\n'
    '  conservative cycle and the fed place keep each premise needed.\n')
SCOPE = (
    '    "PlaceTransitionNets: a place/transition net, defined by its own rules (pre and post "\n'
    '    "multiplicities, enabling, firing, firing sequences), is a law of exchange reading nothing "\n'
    '    "whose course is its flow and whose levels along a firing sequence are its markings; the flow "\n'
    '    "balances the markings exactly on firing sequences, enabling gives feasibility, and "\n'
    '    "feasibility is enabling exactly for pure sequential nets; with finitely many places the flow "\n'
    '    "is dissipative exactly where every fired transition loses weighted tokens, and every step is "\n'
    '    "enclosed; rising with falling, the bound of consuming firings by the initial weighted "\n'
    '    "tokens, rest unrefuted in the flow and world forms, and the siphon law as joint excess "\n'
    '    "hold of such nets; the conservative cycle and the fed place keep dissipation and gating "\n'
    '    "needed. "\n')
README_ROW = (
    '| L4 | [`Becoming.PlaceTransitionNets`](Becoming/PlaceTransitionNets.lean) | place/transition nets '
    '(Petri nets) defined by their own rules, read on the spine (no premise beyond the net\'s named '
    'properties): the net is a law of exchange (`Net.law`, `Net.law_nonanticipating`) whose course is its flow '
    '(`Net.course_eq`) and whose levels are its markings (`Net.Fires.levels_eq`); balance exactly on firing '
    'sequences (`Net.balances_iff`), feasibility from enabling (`Net.Fires.feasible`) and exactly for pure '
    'sequential nets (`Net.fires_iff_feasible`; `Net.catalyst_feasible_not_fires`, `Net.relay_feasible_not_fires`); '
    'dissipation exactly where fired transitions lose (`Net.dissipative_iff`, a strict P-subinvariant); '
    '`Net.rise_with_fall`, `Net.takers_within`, `Net.change_stops_unrefuted`, `Net.rests_unrefuted` (world form), '
    'the siphon law `Net.gated_ends` and `Net.siphon_empty` from `Flow.joint_excess_ends`; counterexamples '
    '`Net.cycle_never_rests`, `Net.fed_refills` |')

root = (PKG / 'Becoming.lean').read_text()
root = once(root, 'import Becoming.Reading\n', 'import Becoming.Reading\nimport Becoming.PlaceTransitionNets\n')
root = once(root, '* `Becoming.Readings` (L4): one unfolding, read in context, with no premise.',
            DOC + '* `Becoming.Readings` (L4): one unfolding, read in context, with no premise.')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.Reading", ', '"Becoming.Reading", "Becoming.PlaceTransitionNets", ')
chk = once(chk, '    "Description: describing the parts separately gives back a whole of two parts exactly where it "\n',
           SCOPE + '    "Description: describing the parts separately gives back a whole of two parts exactly where it "\n')
(PKG / 'check_becoming.py').write_text(chk)

rd = (PKG / 'README.md').read_text()
lines = rd.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| L4 | [`Becoming.Reading`](Becoming/Reading.lean) |')]
assert len(idx) == 1, idx
lines[idx[0] + 1:idx[0] + 1] = [README_ROW]
(PKG / 'README.md').write_text('\n'.join(lines))
print('integrated')
