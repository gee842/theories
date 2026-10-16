#!/usr/bin/env python3
"""Add P73's module to the root module, the checker and the Lean READMEs, and P74's bridge to the
evolution-connectionism README.

Usage: python3 -B root_edits.py ROOT core      (before the consolidated checker's landing run)
       python3 -B root_edits.py ROOT readmes   (after both receipts pass)

`core` adds `import Becoming.Learning` and its docstring bullet to `Becoming.lean`, and the module
to `CORE` with its scope sentence in `check_becoming.py`. `readmes` adds the spine row, the import
note and the periphery ring entry to `becoming/README.md`, and the bridge paragraph to the
evolution-connectionism README, with the counts from ROOT's receipts. Every anchor must occur
exactly once; rerunning on an edited checkout fails.
"""
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
STAGE = sys.argv[2]
assert STAGE in {'core', 'readmes'}, STAGE
L = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean'
B = L / 'becoming'
EC = L / 'universal-ethics/evolution-connectionism'


def edit(path, pairs):
    s = path.read_text()
    for anchor, new in pairs:
        assert s.count(anchor) == 1, (path.name, anchor[:80], s.count(anchor))
        s = s.replace(anchor, new)
    path.write_text(s)
    print('edited', path.relative_to(ROOT))


BULLET = """* `Becoming.Learning` (L4): no record fixes the next value: two courses share any record and
  differ at its next step, also among worlds held by a list, and for every learner a course
  refutes each of its claims, the registration of a law keeping its record, so open. Learning by
  refutation never passes a hypothesis that holds; where a list holds the world the lasso learner
  is refuted a bounded number of times, its coming to rest is unrefuted, and when it rests is not
  registered; learning over classes is the same learning over a merged enumeration. A lumping
  determines exactly the inputs it lumps with the data and is right exactly where the world goes
  alike across it; structure and change are one lumping; the class of every function fixes no
  untried value; training selects through the data, and its fit is right beyond them exactly
  where the class is determined there. 理 is read as Ren reads it, the modeling of the laws of
  structure and of change; the other readings are the AI's, pending Ren.
"""

SCOPE = (
    '    "Learning: given two values, two courses share the record before any step and differ at it, also "\n'
    '    "among worlds held by a list, so a claim from the record is not right on both and, with values "\n'
    '    "decided, is refuted on one; for every learner and every map moving each value the diagonal "\n'
    '    "course refutes each of its claims, is the registration of a law keeping its record and has no "\n'
    '    "list holding that law\'s configurations; learning by refutation over hypotheses in order never "\n'
    '    "passes one that holds, is then not refuted at arbitrarily late steps, and passes only refuted "\n'
    '    "hypotheses; every registration of an orbit held by a list l is a lasso within l.length, on it "\n'
    '    "the learner over the lassos in diagonal order is refuted fewer than tri l.length times and "\n'
    '    "claims at every step from step l.length on, its coming to rest unrefuted, and its diagonal "\n'
    '    "course is no lasso; over classes merged along the pairs the index is bounded where a member "\n'
    '    "of a class holds, and every merging is unrested on its diagonal course; the class of functions "\n'
    '    "going alike across a lumping is determined at an input lumped with an observed one, and with "\n'
    '    "two values, listed data and decided equality exactly there; a member fitting the world on the "\n'
    '    "data is right at an input lumped with an observed one exactly where the world takes one value "\n'
    '    "at the two; the class of every function fixes no unobserved value; a determined law goes alike "\n'
    '    "under a projection exactly when the projection of its step goes alike across it, and an "\n'
    '    "observed outcome transfers exactly where the configurations go alike; a loss computed on the "\n'
    '    "data selects through agreement on the data, within a class free at an input every selection "\n'
    '    "through the data leaves every value there selected, and every member fitting a world of the "\n'
    '    "class is right at an input exactly where the data determine it. "\n'
)

ROW_ZH = ('学习（不加前提）：给出两个值，两个序列在任一步之前记录相同、在该步不同，被列表所持的世界中亦然，所以从记录作出的主张不在两者上都对，'
          '值可判定时在其一被否证（`no_record_fixes_next`、`claim_refuted_on_one`、`no_record_fixes_next_finite`）；每个学习者都有在每个主张处否证它的对角序列，'
          '那是保留记录之律的识，开放（`diagonal_refutes`、`diagonal_open`）；按否证学习从不越过成立的假设（`index_le_of_holds`、`refutations_not_recurring`）；'
          '被列表 l 所持的世界中，套索学习者否证少于 `tri l.length` 次、从第 l.length 步起每步主张，静止不能被否证（`held_learner_bounded`、`held_rest_unrefuted`）；'
          '对类的学习是合并枚举上的同一学习（`merged_bound`、`merged_unrested`）；经归并同去之类恰在与数据归并之处被决定，正确恰在世界在那里取同一值之处'
          '（`determines_lumped_iff`、`lumped_right_iff`）；确定律经投影同去恰当投影后的步经它同去，结构与变化是同一个归并（`goAlike_iff_lumped`）；'
          '一切函数之类不固定任何未试之值（`every_determines_nothing`）；训练经数据选择，拟合在数据之外正确恰当类在那里决定（`Training.loss_through`、'
          '`Training.fit_right_iff`）；理依 Ren 读作对结构与变化之规律的建模，其余读法是 AI 的，待 Ren')
ROW_EN = ('learning (no premise): given two values, two courses share the record before any step and differ at it, also among worlds held by a '
          'list, so a claim from the record is not right on both and, with values decided, is refuted on one (`no_record_fixes_next`, '
          '`claim_refuted_on_one`, `no_record_fixes_next_finite`); every learner has a diagonal course refuting each of its claims, the '
          'registration of a law keeping its record, so open (`diagonal_refutes`, `diagonal_open`); learning by refutation never passes a '
          'hypothesis that holds (`index_le_of_holds`, `refutations_not_recurring`); where a list l holds the world the lasso learner is refuted '
          'fewer than `tri l.length` times and claims at every step from step l.length on, its coming to rest unrefuted (`held_learner_bounded`, '
          '`held_rest_unrefuted`); learning over classes is the same learning over a merged enumeration (`merged_bound`, `merged_unrested`); '
          'the class going alike across a lumping is determined exactly where an input is lumped with the data, and right exactly where the '
          'world takes one value there (`determines_lumped_iff`, `lumped_right_iff`); a determined law goes alike under a projection exactly when '
          'the projection of its step goes alike across it, so structure and change are one lumping (`goAlike_iff_lumped`); the class of every '
          'function fixes no untried value (`every_determines_nothing`); training selects through the data, and its fit is right beyond them '
          'exactly where the class is determined there (`Training.loss_through`, `Training.fit_right_iff`); 理 is read as Ren reads it, the '
          'modeling of the laws of structure and of change; the other readings are the AI\'s, pending Ren')

if STAGE == 'core':
    edit(B / 'Becoming.lean', [
        ('import Becoming.Selection\n', 'import Becoming.Selection\nimport Becoming.Learning\n'),
        ('* `Becoming.Boundaries` (L4):', BULLET + '* `Becoming.Boundaries` (L4):'),
    ])
    edit(B / 'check_becoming.py', [
        ('"Becoming.Selection", "Becoming.Boundaries"', '"Becoming.Selection", "Becoming.Learning", "Becoming.Boundaries"'),
        ('    "Boundaries: along a relation a boundary of a formation is a region holding it that is closed "\n',
         SCOPE + '    "Boundaries: along a relation a boundary of a formation is a region holding it that is closed "\n'),
    ])
    sys.exit()

core = json.loads((B / 'becoming-verification.json').read_text())
bridge = json.loads((EC / 'learning-correspondence-verification.json').read_text())
assert core['status'] == bridge['status'] == 'passed'
assert any(m['module'] == 'Becoming.Learning' for m in core['modules'])
bm = bridge['modules'][0]
n_bridge, n_audits = bm['theorems'], len(bm['declarations'])
n_empty = sum(not v for v in bm['axiom_dependencies'].values())

readme = (B / 'README.md').read_text()
selection_row = next(line for line in readme.split('\n') if line.startswith('| L4 | [`Becoming.Selection`]'))
row = f'| L4 | [`Becoming.Learning`](Becoming/Learning.lean) | {ROW_ZH} / {ROW_EN} |'
assert selection_row.count('|') == row.count('|'), (selection_row.count('|'), row.count('|'))
edit(B / 'README.md', [
    (selection_row + '\n', selection_row + '\n' + row + '\n'),
    ('`Selection` 导入 `Testing` 与 `Capture`；', '`Selection` 导入 `Testing` 与 `Capture`；`Learning` 导入 `Mechanism` 与 `Selection`；'),
    ('`Selection` imports `Testing` and `Capture`;', '`Selection` imports `Testing` and `Capture`; `Learning` imports `Mechanism` and `Selection`;'),
    ('及其桥接 [`CorrectionInquiry`](../universal-ethics/generative-capacity/CorrectionInquiry.lean)',
     '及其桥接 [`CorrectionInquiry`](../universal-ethics/generative-capacity/CorrectionInquiry.lean)、'
     '[`LearningCorrespondence`](../universal-ethics/evolution-connectionism/LearningCorrespondence.lean)'),
])

STUDY = ('../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/'
         'BECOMING-RENEWAL-READING.md')
PARAGRAPH = (
    f'**The learning correspondence.** [LearningCorrespondence.lean](LearningCorrespondence.lean) states this package\'s '
    'central relationships, with the acquisition chain, as instances of the Becoming core\'s laws of learning '
    f'(`Becoming.Learning`; [study]({STUDY})). A network\'s development under fixed weights is the orbit of its step; '
    'Hebbian development and the network going on under a route of updating are one determined process on the joint '
    'configuration, activity or the network having a law of its own exactly where the weights or the route make no '
    'difference, and in the three-unit memory and at the starting network they do; the responsive route learns exactly '
    'where the task fails. Within the uniform law family with distinguishable primitive effects the three encounters of '
    '`CompositionalAcquisition` determine every expression, and admitting its nonuniform law they determine nothing at '
    f'the novel one. **{n_bridge} theorems / {n_audits} audits**; the {n_empty} acquisition declarations have empty '
    'axiom reports and the rest report Mathlib\'s standard axioms. [Receipt](learning-correspondence-verification.json); '
    'run `python3 check_learning_correspondence.py`. Profiles, constants, routes, the grammar and the probes keep the '
    'earlier modules\' scope; correspondence to an actual learner or network is not checked.\n\n')
edit(EC / 'README.md', [('# Developmental connectionist recovery\n\n', '# Developmental connectionist recovery\n\n' + PARAGRAPH)])
