#!/usr/bin/env python3
"""Join SG's three modules to the core package: copy each in, import it after Becoming.JointKeeping, add its
root doc bullet before Contacts', its CORE entry and scope text in check_becoming.py, and its README row.
usage: python3 -B integrate.py   (SG_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['SG_ROOT']).resolve() if os.environ.get('SG_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
MODS = ['Undecided', 'Junctures', 'Commuting']


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


for m in MODS:   # the kit's scratch copies, where present; at a reland the modules are already in the package
    kit = HERE / 'lean' / 'Becoming' / f'{m}.lean'
    if kit.exists():
        shutil.copyfile(kit, PKG / 'Becoming' / f'{m}.lean')
    assert (PKG / 'Becoming' / f'{m}.lean').exists(), m

DOC = (
    '* `Becoming.Undecided` (L2): the third value and revision, with no premise. With values true,\n'
    '  undecided and false, undecided below the decided ones in information, a term with no constant\n'
    '  is undecided where every sentence is, so a system with no constant stays wholly undecided, and\n'
    '  evaluation is monotone in information. Revision of `N` sentences that speak only of one another,\n'
    '  run from every sentence undecided, rises at every step and settles within `N` steps at the least\n'
    '  fixed point, a bound the chain of denials shows exact; readings on a list that only rise, and once\n'
    '  steady stay steady, are steady by the list\'s length. The liar rests undecided, and a run of its\n'
    '  revision rests exactly where it is undecided. Where the two-valued revision has no fixed point,\n'
    '  as for the liar (`Diagonal.revision_never_rests`), every fixed point, and every run of revision\n'
    '  that rests, leaves a sentence undecided: the gap reappears as undecidedness. The run of a\n'
    '  monotone map from the undecided value rests from its first step, so the gap of\n'
    '  `Diagonal.gap_unsaid` needs a map that is not monotone.\n'
    '* `Becoming.Junctures` (L3): where a configuration can still be had again and where it is lost.\n'
    '  A juncture for `s` has a step after which `s` can still be had and one after which it cannot.\n'
    '  Every loss of a returning `s` passes a juncture on its course, up to double negation; where it\n'
    '  is decided along the course whether `s` can still be had, and for configurations a list holds\n'
    '  with decided steps, the juncture is found; finding it for every loss of every process is the\n'
    '  limited principle of omniscience. Keeping the steps after which `s` can still be had keeps `s`\n'
    '  and is the greatest sub-process that does; on its course it removes exactly the losing steps\n'
    '  at junctures; losing never returns. Many options make no juncture.\n'
    '* `Becoming.Commuting` (L4): what a commuting law keeps apart. Where a law commutes with a map\n'
    '  that moves every configuration, its runs from a configuration and from its image are never at\n'
    '  one configuration at the same step: to merge what a symmetry tells apart a law must break it.\n'
    '  No such law is constant; what the map fixes stays fixed along the run; rests\n'
    '  and returns come in pairs; under an exchange a course holding a pair holds it halfway round a\n'
    '  return; the law goes alike across the pairs; `Diagonal.revision_never_rests` is the case of a\n'
    '  map commuting with itself. Symmetric processes carry reach, returning and junctures, and each\n'
    '  run has a mirror run never at the same configuration. In the Changes, waxing and waning never\n'
    '  merges a hexagram with its complement, and the waning into 坤 breaks the symmetry.\n')
SCOPE = (
    '    "Undecided: with values t, u and f, u below in information, constant-free terms are undecided "\n'
    '    "where every sentence is and a constant-free system stays undecided; evaluation is monotone; "\n'
    '    "revision of N closed sentences run from all undecided settles within N steps, a bound the "\n'
    '    "chain shows exact, at the least fixed point; a run of the liar rests exactly where it is "\n'
    '    "undecided; where two-valued revision has no fixed point every fixed point and every resting "\n'
    '    "run leave a sentence undecided; a monotone map\'s run from u rests, so no monotone map moves "\n'
    '    "every value. "\n'
    '    "Junctures: every loss of a returning configuration passes a juncture on its course, up to "\n'
    '    "double negation, found where reach is decided and for listed configurations with decided "\n'
    '    "steps; finding it for every process is LPO; keeping the steps that can still return keeps "\n'
    '    "the configuration, is the greatest such sub-process and removes the losing steps at "\n'
    '    "junctures; many options make no juncture. "\n'
    '    "Commuting: the runs of a law commuting with a map that moves every configuration, from a "\n'
    '    "configuration and from its image, are never at one configuration at the same step; what the "\n'
    '    "map fixes stays fixed; rests, returns and junctures come in pairs; under an exchange a "\n'
    '    "pair is held halfway round a return; Diagonal.revision_never_rests is the case of a map "\n'
    '    "commuting with itself; waxWane never merges complements and wane breaks the symmetry. "\n')
README_ROWS = [
    '| L2 | [`Becoming.Undecided`](Becoming/Undecided.lean) | the third value and revision (no premise): constant-free '
    'terms are undecided where every sentence is (`eval_undecided`), so constant-free systems stay undecided '
    '(`stays_undecided`); evaluation is monotone in information (`eval_mono`); revision of `N` closed sentences, run '
    'from all undecided, settles within `N` steps (`settles`, from `settles_within`), exactly (`chain_exact`), at the '
    'least fixed point (`least_fixed`); the liar rests undecided (`liar_rests`, `liar_rests_iff`); where two-valued '
    'revision has no fixed point every fixed point and every resting run leave a sentence undecided '
    '(`undecided_of_moves`, `rest_undecided`, `liar_undecided`, `liar_both_sides`); a monotone map\'s run from the '
    'undecided value rests (`monotone_run_rests`), so the gap needs a map that is not monotone (`moves_not_monotone`) |',
    '| L3 | [`Becoming.Junctures`](Becoming/Junctures.lean) | where a configuration is lost (no premise): every loss of '
    'a returning configuration passes a juncture, up to double negation (`loss_passes_juncture`), found where reach is '
    'decided (`loss_passes_juncture_decided`) and for listed configurations with decided steps '
    '(`loss_passes_juncture_listed`); finding it for every process is LPO (`lpo_of_junctures_found`); keeping keeps '
    '`s` (`keeping_keeps`), is the greatest (`keeping_greatest`) and removes the losing steps at junctures '
    '(`keeping_removes_at_juncture`); many options make no juncture (`Many.no_juncture`) |',
    '| L4 | [`Becoming.Commuting`](Becoming/Commuting.lean) | what a commuting law keeps apart (no premise): with a map '
    'moving every configuration, the runs from a configuration and its image never meet at a step (`Law.Commutes.apart`), so '
    'merging needs breaking the symmetry (`Law.Commutes.breaks`); rests, returns and junctures in pairs; pairs held '
    'halfway (`Law.Commutes.paired_halfway`); `Diagonal.revision_never_rests` as `Law.Commutes.self_apart`; mirror '
    'runs (`Branching.mirror_apart`); waxWane and the complement (`Hexagram.waxWane_apart`, '
    '`Hexagram.waxWane_halfway`), wane breaks it (`Hexagram.wane_breaks`) |',
]

root = (PKG / 'Becoming.lean').read_text()
root = once(root, 'import Becoming.JointKeeping\n',
            'import Becoming.JointKeeping\n' + ''.join(f'import Becoming.{m}\n' for m in MODS))
root = once(root, '* `Becoming.Contacts` (L4): registration through addressed contacts.',
            DOC + '* `Becoming.Contacts` (L4): registration through addressed contacts.')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.JointKeeping",',
           '"Becoming.JointKeeping", ' + ' '.join(f'"Becoming.{m}",' for m in MODS))
chk = once(chk, '    "Description: describing the parts separately gives back a whole of two parts exactly where it "\n',
           SCOPE + '    "Description: describing the parts separately gives back a whole of two parts exactly where it "\n')
(PKG / 'check_becoming.py').write_text(chk)

rd = (PKG / 'README.md').read_text()
lines = rd.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| L4 | [`Becoming.JointKeeping`](Becoming/JointKeeping.lean) |')]
assert len(idx) == 1, idx
lines[idx[0] + 1:idx[0] + 1] = README_ROWS
(PKG / 'README.md').write_text('\n'.join(lines))
print('integrated')
