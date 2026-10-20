#!/usr/bin/env python3
"""Join U5's modules to the core package: copy the three new modules (WitnessRefinementRuns, NarrowingRuns,
HistoryIdealsTraces) and the edited FrontierWorlds in, import each new module after the module it reads, add its root
doc bullet after that module's, its CORE entry and scope text in check_becoming.py, and its README row.
usage: python3 -B integrate.py   (U5_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['U5_ROOT']).resolve() if os.environ.get('U5_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
NEW = {'WitnessRefinementRuns': 'WitnessRefinement', 'NarrowingRuns': 'Narrowing',
       'HistoryIdealsTraces': 'HistoryIdeals'}
EDITED = ['FrontierWorlds']


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


for m in list(NEW) + EDITED:
    shutil.copyfile(HERE / 'Becoming' / f'{m}.lean', PKG / 'Becoming' / f'{m}.lean')

DOC = {
    'WitnessRefinementRuns': (
        '* `Becoming.WitnessRefinementRuns` (L4): inspection by fallible witnesses as a process for every\n'
        '  roster, fault sets and answers (`inspection`), and testing (`testing`); the audit and the\n'
        '  inquiry move their candidates by them. A silent transcript keeps exactly the candidates\n'
        '  admitting a fault set, a certificate after a step needs a candidate; after a complete\n'
        '  transcript candidates with cross-separated envelopes agree, at every later state; two\n'
        '  candidates are told apart by every complete step exactly where their envelopes are\n'
        '  cross-separated; covering fault sets keep both and certify nothing; listing the roster twice\n'
        '  changes nothing; a candidate admitting every failure is kept and blocks every later\n'
        '  certificate; a test leaving no candidate certifies nothing, and a separated pool after a\n'
        '  faithful test completes.\n'),
    'NarrowingRuns': (
        '* `Becoming.NarrowingRuns` (L4): narrowing along the runs of the pure observation. What the\n'
        '  belief `After` narrows settles is what the learned list answers; the answer is safe for it\n'
        '  and, where it holds a rule, its greatest safe answer, the only one; along every run observing\n'
        '  a candidate rule the answer from the record is the greatest safe answer and asserts the\n'
        '  observed rule\'s values; re-encoding transports what the belief settles.\n'),
    'HistoryIdealsTraces': (
        '* `Becoming.HistoryIdealsTraces` (L3): the word half of `Becoming.HistoryIdeals` on the courses a\n'
        '  process can take (no premise): an ideal of feasible courses that settles, or goes on with its\n'
        '  courses picked, is a history of the process, a feasible course settles, and a run\'s moves go\n'
        '  on; a history of feasible courses need not be a run\'s moves (`history_without_run`).\n'),
}
FRONTIER_OLD = ('* `Becoming.FrontierWorlds` (L4): what a formation requires of a condition in a world, served\n'
                '  across a handover from one giver to another (`Served`): withdrawn giving needs the successor,\n'
                '  a handover with no gap serves, and a gap refutes service.\n')
FRONTIER_NEW = ('* `Becoming.FrontierWorlds` (L4): what a formation requires of a condition in a world, served\n'
                '  across a handover from one giver to another (`Served`): withdrawn giving needs the successor,\n'
                '  a handover with no gap serves, and a gap refutes service. Joint plans and undertakings on the\n'
                '  world\'s moves: a sole giver to what a formation requires is required, and active where only\n'
                '  active formations give; a discharged undertaking leaves no residual step.\n')
SCOPE = (
    '    "FrontierWorlds (U5): on the world\'s moves, a sole giver to what a formation requires is "\n'
    '    "required and, where only active formations give, active; a discharged undertaking leaves no "\n'
    '    "residual step and an unmet one is residual. "\n'
    '    "WitnessRefinementRuns: inspection by fallible witnesses and testing as processes for every "\n'
    '    "roster, fault sets and answers, the audit and the inquiry their instances: silence keeps the "\n'
    '    "candidates admitting a fault set; after a complete transcript cross-separated candidates "\n'
    '    "agree at every later state; complete steps tell two candidates apart exactly where their "\n'
    '    "envelopes are cross-separated; covering fault sets keep both and certify nothing; a doubled "\n'
    '    "roster changes nothing; a candidate admitting every failure blocks every later certificate; "\n'
    '    "a test leaving no candidate certifies nothing, a separated pool after a faithful test completes. "\n'
    '    "NarrowingRuns: the answer is the greatest safe answer of the belief narrowed by After on the "\n'
    '    "pure observation, the only one; along every run observing a candidate rule it asserts the "\n'
    '    "observed rule\'s values; re-encoding transports what the belief settles. "\n'
    '    "HistoryIdealsTraces: an ideal of the courses a process can take that settles, or goes on with "\n'
    '    "its courses picked, is a history of the process; a run\'s moves go on; a history of feasible "\n'
    '    "courses need not be a run\'s moves. "\n')
README = {
    'WitnessRefinementRuns': (
        '| L4 | [`Becoming.WitnessRefinementRuns`](Becoming/WitnessRefinementRuns.lean) | inspection by fallible '
        'witnesses as a process for every roster (no premise): `inspection` and `testing`, with the audit and the inquiry '
        'as instances (`audit_step_inspection`, `inquiry_step_testing`); silence (`silent_step`), a certificate needs a '
        'candidate (`step_certificate_candidate`), agreement after a complete transcript (`complete_step_agrees`, '
        '`complete_run_agrees`), diagnosability (`diagnosable_iff`), covering fault sets (`covering_step_keeps_both`), '
        'the doubled roster (`doubled_roster_same`), a candidate admitting every failure (`total_fault_blocks`), testing '
        '(`test_emptied`, `test_step_completes`) |'),
    'NarrowingRuns': (
        '| L4 | [`Becoming.NarrowingRuns`](Becoming/NarrowingRuns.lean) | narrowing along the runs of the pure '
        'observation (no premise; function extensionality named where used): the greatest safe answer of the narrowed '
        'belief (`narrowed_answer_greatest`, `narrowed_answer_unique`), along a run (`run_answer_greatest`, '
        '`run_answer_correct`), re-encoding (`transport_settles_iff`) |'),
    'HistoryIdealsTraces': (
        '| L3 | [`Becoming.HistoryIdealsTraces`](Becoming/HistoryIdealsTraces.lean) | the word half of '
        '`Becoming.HistoryIdeals` on a process\'s feasible courses (no premise): `classification`, `course_settles`, '
        '`run_goesOn`, and a history of feasible courses that is no run\'s moves (`history_without_run`) |'),
}
README_FRONTIER_OLD = ('| L4 | [`Becoming.FrontierWorlds`](Becoming/FrontierWorlds.lean) | what a formation requires of a '
                       'condition in a world, served across a handover between givers (`Served`, `Served.successor`, '
                       '`served_of_handover`, `Served.not_of_gap`) |')
README_FRONTIER_NEW = ('| L4 | [`Becoming.FrontierWorlds`](Becoming/FrontierWorlds.lean) | what a formation requires of a '
                       'condition in a world, served across a handover between givers (`Served`, `Served.successor`, '
                       '`served_of_handover`, `Served.not_of_gap`); joint plans and undertakings on the world\'s moves '
                       '(`sole_giver_required`, `sole_giver_active`, `Discharged.no_residual`, '
                       '`residual_of_unfulfilled`) |')

root = (PKG / 'Becoming.lean').read_text()
for new, base in NEW.items():
    root = once(root, f'import Becoming.{base}\n', f'import Becoming.{base}\nimport Becoming.{new}\n')
    start = root.index(f'* `Becoming.{base}` (')
    end = root.index('\n* `', start) + 1
    root = root[:end] + DOC[new] + root[end:]
root = once(root, FRONTIER_OLD, FRONTIER_NEW)
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
for new, base in NEW.items():
    chk = once(chk, f'"Becoming.{base}",', f'"Becoming.{base}", "Becoming.{new}",')
chk = once(chk, '    "Hexagrams: six two-valued lines give sixty-four configurations, equality and membership told "\n',
           SCOPE + '    "Hexagrams: six two-valued lines give sixty-four configurations, equality and membership told "\n')
(PKG / 'check_becoming.py').write_text(chk)

rd = (PKG / 'README.md').read_text()
lines = rd.split('\n')
for new, base in NEW.items():
    layer = README[new][:7]
    idx = [i for i, l in enumerate(lines) if l.startswith(f'{layer}[`Becoming.{base}`](Becoming/{base}.lean) |')]
    assert len(idx) == 1, (new, idx)
    lines.insert(idx[0] + 1, README[new])
rd = '\n'.join(lines)
rd = once(rd, README_FRONTIER_OLD, README_FRONTIER_NEW)
(PKG / 'README.md').write_text(rd)
print('integrated')
