#!/usr/bin/env python3
"""Join U3's modules to the core package: copy the four new modules (FrontierFrames, FrontierWorlds,
AcceptanceFrames, PresentationFrames) and the two edited ones (Hexagrams, Listing) in, import each new module after the
module it reads, add its root doc bullet after that module's, its CORE entry and scope text in
check_becoming.py, and its README row.
usage: python3 -B integrate.py   (U3_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['U3_ROOT']).resolve() if os.environ.get('U3_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
NEW = ['FrontierFrames', 'FrontierWorlds', 'AcceptanceFrames', 'PresentationFrames']
EDITED = ['Hexagrams', 'Listing']


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


for m in NEW + EDITED:
    shutil.copyfile(HERE / 'Becoming' / f'{m}.lean', PKG / 'Becoming' / f'{m}.lean')

DOC_FRONTIER = (
    '* `Becoming.FrontierFrames` (L4): the practical commitments on a frame. J1/J2 as a condition on\n'
    '  the configurations of a frame, compared by the basic, then the living claims they realize\n'
    '  (`Priority`): irreflexive and transitive, anchored by a kept basic claim, no trade of a basic\n'
    '  claim for living ones, a generative extension never refuted to be better, C wherever it is\n'
    '  decided whether an extension adds a basic claim, and every two-tier condition that of its\n'
    '  tier frame. The options at a configuration are what one move of the process reaches\n'
    '  (`Options`): an option bettered by another is not chosen, J1/J2 leave one chosen where the\n'
    '  options are listed and the comparison weakly decided, a required task is performed by any\n'
    '  chosen option, nothing is required where no move is possible, and a basic claim kept by an\n'
    '  option keeping every basic claim of the options is never refuted at a chosen option and is\n'
    '  required where decided. Fresh contents under every classification on a frame of two kinds.\n'
    '* `Becoming.FrontierWorlds` (L4): what a formation requires of a condition in a world, served\n'
    '  across a handover from one giver to another (`Served`): withdrawn giving needs the successor,\n'
    '  a handover with no gap serves, and a gap refutes service.\n'
    '* `Becoming.AcceptanceFrames` (L4): scores over the options of a step. Every option best by the\n'
    '  score with acceptance keeps access exactly where every option best by the base score does;\n'
    '  restricting to the options loses score, least among them; an option best by an estimate\n'
    '  within `err` is within `2 * err` of every option.\n')
DOC_PRESENTATIONS = (
    '* `Becoming.PresentationFrames` (L3): presentations of a frame. Exact reduced presentations of a\n'
    '  frame\'s branching tests correspond one to one; the canonical presentation reads every test,\n'
    '  gives one code exactly to configurations passing the same tests where predicates are\n'
    '  extensional, and every exact presentation factors through it; the joint relation of a joint\n'
    '  frame descends to the codes exactly where it is the same for configurations passing the same\n'
    '  tests; the frame realizing every predicate tells every two configurations apart and every\n'
    '  relation descends to its codes.\n')
SCOPE = (
    '    "FrontierFrames: J1/J2 as a condition on the configurations of a frame compared by what they "\n'
    '    "realize, irreflexive and transitive, anchored by a kept basic claim, no trade for living "\n'
    '    "claims, C where decided, every two-tier condition that of its tier frame; the options of a "\n'
    '    "step are what one move reaches; a bettered option is not chosen, J1/J2 leave one chosen "\n'
    '    "where listed and weakly decided, a required task is performed by any chosen option, "\n'
    '    "nothing is required where no move is possible, a basic claim kept by an option keeping "\n'
    '    "every basic claim of the options is never refuted at a chosen option and required where "\n'
    '    "decided; fresh contents under every classification on a frame of two kinds. "\n'
    '    "FrontierWorlds: what a formation requires of a condition, served across a handover between "\n'
    '    "givers to it: withdrawn giving needs the successor, no gap serves, a gap refutes service. "\n'
    '    "AcceptanceFrames: on the options of a step, every option best with acceptance keeps access "\n'
    '    "exactly where every best base option does, restricting to the options loses score least "\n'
    '    "among them, and an option best by an estimate within err is within 2 err of every option. "\n'
    '    "PresentationFrames: exact reduced presentations of a frame\'s branching tests correspond one "\n'
    '    "to one, the canonical presentation reads every test and every exact one factors through "\n'
    '    "it, the joint relation of a joint frame descends exactly where saturated, and the frame "\n'
    '    "realizing every predicate tells every two configurations apart. "\n')
README_FRONTIER = [
    '| L4 | [`Becoming.FrontierFrames`](Becoming/FrontierFrames.lean) | the practical commitments on a frame (no '
    'premise beyond what each theorem names): J1/J2 as a condition on configurations compared by what they realize '
    '(`Priority`, `Priority.anchor`, `Priority.no_trade`, `Priority.comparison`, `basicPriority_iff_priority`); the '
    'options of a step are what one move reaches (`Options`); J1/J2 leave one chosen where listed and weakly decided '
    '(`Priority.choice_exists`); nothing is required where no move is possible (`nothing_required`); a kept basic '
    'claim is never refuted at a chosen option and required where decided (`Priority.kept_unrefuted`, '
    '`Priority.kept_required`); fresh contents under every classification (`classifiedOn_robust_iff_of_decided`, '
    '`classifiedOn_required`) |',
    '| L4 | [`Becoming.FrontierWorlds`](Becoming/FrontierWorlds.lean) | what a formation requires of a condition in a '
    'world, served across a handover between givers (`Served`, `Served.successor`, `served_of_handover`, '
    '`Served.not_of_gap`) |',
    '| L4 | [`Becoming.AcceptanceFrames`](Becoming/AcceptanceFrames.lean) | scores over the options of a step (no '
    'premise): acceptance protects only what the best options keep (`access_iff`, `no_access`), restricting to the '
    'options loses score exactly (`restriction_loss`), estimates within `err` fall short by at most `2 * err` '
    '(`estimate_bound`) |',
]
README_PRESENTATIONS = [
    '| L3 | [`Becoming.PresentationFrames`](Becoming/PresentationFrames.lean) | presentations of a frame (no premise; '
    'extensionality of predicates named where used): codes of its branching tests correspond one to one '
    '(`correspondence`), the canonical presentation (`canonical_kernel`, `canonical_factor`), the joint relation of a '
    'joint frame descends exactly where saturated (`joint_descends_iff`, `joint_blocked`), and the frame realizing every '
    'predicate tells every two configurations apart (`everyPredicate_separate`, `everyPredicate_correspondence`) |',
]

root = (PKG / 'Becoming.lean').read_text()
root = once(root, 'import Becoming.Frontier\n',
            'import Becoming.Frontier\nimport Becoming.FrontierFrames\nimport Becoming.FrontierWorlds\n'
            'import Becoming.AcceptanceFrames\n')
root = once(root, 'import Becoming.Presentations\n', 'import Becoming.Presentations\nimport Becoming.PresentationFrames\n')
root = once(root, '* `Becoming.ScoreRepresentation` (L4):', DOC_FRONTIER + '* `Becoming.ScoreRepresentation` (L4):')
root = once(root, '* `Becoming.Carriers` (L3):', DOC_PRESENTATIONS + '* `Becoming.Carriers` (L3):')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.Lexical", "Becoming.Frontier",', '"Becoming.Lexical", "Becoming.Frontier", "Becoming.FrontierFrames", "Becoming.FrontierWorlds", '
           '"Becoming.AcceptanceFrames",')
chk = once(chk, '"Becoming.Presentations",', '"Becoming.Presentations", "Becoming.PresentationFrames",')
chk = once(chk, '    "Hexagrams: six two-valued lines give sixty-four configurations, equality and membership told "\n',
           SCOPE + '    "Hexagrams: six two-valued lines give sixty-four configurations, equality and membership told "\n')
chk = once(chk, '"where turning over gives the same hexagram, changed in every line; the change of one line "',
           '"where turning over gives the same hexagram, changed in every line, which is six steps of the "\n'
           '    "law of waxing and waning; the change of one line "')
(PKG / 'check_becoming.py').write_text(chk)

rd = (PKG / 'README.md').read_text()
lines = rd.split('\n')
for prefix, rows in (('| L4 | [`Becoming.Frontier`](Becoming/Frontier.lean) |', README_FRONTIER),
                     ('| L3 | [`Becoming.Presentations`](Becoming/Presentations.lean) |', README_PRESENTATIONS)):
    idx = [i for i, l in enumerate(lines) if l.startswith(prefix)]
    assert len(idx) == 1, (prefix, idx)
    lines[idx[0] + 1:idx[0] + 1] = rows
rd = '\n'.join(lines)
rd = once(rd, 'paired by turning over or changing every line (`mem_order`, `order_paired`)',
          'paired by turning over or by six steps of the law of waxing and waning (`mem_order`, `order_paired`, '
          '`order_paired_by_law`)')
(PKG / 'README.md').write_text(rd)
print('integrated')
