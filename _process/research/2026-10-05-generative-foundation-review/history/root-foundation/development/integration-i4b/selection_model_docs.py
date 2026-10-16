#!/usr/bin/env python3
"""I4b-2 follow-up (Ren, 16 October 2026: “go ahead with the reframing, first title, keep names, (a)”): the documents
around Becoming.Selection's section “Selection through a model of the options” and Becoming.Learning's new section of
that name, and IdealWarrant's place with the general mathematical line.

usage (from the repository root): python3 -B selection_model_docs.py PART [PART ...] [--section N]

Parts:
* learning   Becoming/Learning.lean: the header bullet and reading for the new section (comments only);
* root       Becoming.lean: the Selection and Learning bullets (comments only);
* readme     the Lean package README: the Selection and Learning rows;
* chapter    THE-THEORY-OF-BECOMING.md: §9's Selection and Learning rows (Learning 75 → 83 theorems), the periphery row
             and the zh and en instance lists;
* notes      the remaining-dependency package's FORMAL-NOTES.md;
* periphery  SelectionRelabelCorrespondence.lean (comments only) and relabel.json, the checker's spec; then run
             make_relabel_checker.py to regenerate the checker;
* inventory  DECIDABILITY-INVENTORY.py's comment on Relabel;
* i4a        the I4a rows of PluralRecords, TieBreaking, SelectionRelabelCorrespondence and IdealWarrant, and
             IdealWarrant's theme (reach → mathematics); then rerun the I4a pipeline;
* study      (needs --section N) the study section from s_i4b2b_zh.md and s_i4b2b_en.md, inserted after the last
             numbered section and at the end of the English summary, and a forward note on section 151.

Every replacement is asserted to apply once; Lean files are asserted to keep their code outside comments. After a merge
that conflicts in a file, take the merged file without this branch's edits and run its part again.
"""
import json
import os
import re
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent
BASE = Path('experiments/integrated-correction/general-framework/generative-basis')
LEAN = BASE / 'lean/becoming'
FORMAL = BASE / 'mathematical-abstraction/acquisition/feedback/remaining-dependency/formal'
STUDY_DIR = Path('_process/research/2026-10-05-generative-foundation-review/root-foundation')
I4A = STUDY_DIR / 'development/integration-i4a'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-16-selection-through-a-model.md'


def code(text):
    """The text outside comments: nested block comments and line comments removed, whitespace collapsed."""
    out, i, depth = [], 0, 0
    while i < len(text):
        if text.startswith('/-', i):
            depth, i = depth + 1, i + 2
        elif depth and text.startswith('-/', i):
            depth, i = depth - 1, i + 2
        elif depth:
            i += 1
        elif text.startswith('--', i):
            i = text.find('\n', i)
            i = len(text) if i < 0 else i
        else:
            out.append(text[i])
            i += 1
    return re.sub(r'\s+', ' ', ''.join(out))


def edit(path, pairs, lean=False):
    path = Path(path)
    before = path.read_text()
    after = before
    for old, new in pairs:
        assert after.count(old) == 1, (str(path), old[:100])
        after = after.replace(old, new)
    if lean:
        assert code(after) == code(before), (str(path), 'code outside comments changed')
        long = lambda text: {line for line in text.splitlines() if len(line) > 100}
        assert long(after) <= long(before), long(after) - long(before)
    path.write_text(after)
    print(path)


def learning():
    edit(LEAN / 'Becoming/Learning.lean', [
        ("""exactly where the class determines it (`Training.fit_right_iff`).

**Readings.**""",
         """exactly where the class determines it (`Training.fit_right_iff`).
* **Selection through a model of the options.** A selection or valuation through a model of the
  options (`Relabel.Equivariant`, `Relabel.EquivariantValue` of `Becoming.Selection`) is a
  selection through the model's lumping (`selects_through_lumping`, `values_lumped`). It is right
  about what matters only where what matters goes alike across that lumping
  (`selects_right_through`, `values_right_lumped`): where what matters separates two options the
  model lumps, none is right (`selects_not_right_of_parted`, `values_not_right_of_parted`); where
  what matters is read off the model, reading it through the model is right
  (`selects_right_of_reads`, `values_right_of_reads`).

**Readings.**"""),
        ("""  the lumping. This reading of the formal terms is the AI's.
""",
         """  the lumping. This reading of the formal terms is the AI's.
- (The AI's reading of Ren's correction of 16 October 2026, which Ren approved the same day.) A
  selection is as good as the model it goes through. What a model lumps, no selection through it
  separates; separating them takes a finer model, and whether that model is right is its fit to
  what matters, which a longer record does not supply: the record gives distinctions, not their
  relevance.
"""),
    ], lean=True)


def root():
    edit(LEAN / 'Becoming.lean', [
        ("""  AI's, adopted on Ren's delegation of 15 October 2026. By the record alone: two options are selected alike by every
  selection reading only a record exactly when the record ties them, one is singled out exactly
  where the record parts it from every other, and tied options are valued alike.
""",
         """  AI's, adopted on Ren's delegation of 15 October 2026. Through a model of the options: two
  options are selected alike by every selection through the model exactly when the model ties
  them, one is singled out exactly where the model separates it from every other, and tied
  options are valued alike.
"""),
        ("""  where the class is determined there. 理 is read as Ren reads it, the modeling of the laws of
  structure and of change; the other readings are the AI's, adopted on Ren's delegation of 15
  October 2026.
""",
         """  where the class is determined there; a selection through a model of the options is right about
  what matters only where what matters goes alike across the model's lumping. 理 is read as Ren
  reads it, the modeling of the laws of structure and of change; the other readings are the AI's,
  adopted on Ren's delegation of 15 October 2026 or, for selection through a model, approved by
  Ren on 16 October 2026.
"""),
    ], lean=True)


def readme():
    path = LEAN / 'README.md'
    lines = path.read_text().split('\n')
    selection = [n for n, line in enumerate(lines) if line.startswith('| L4 | [`Becoming.Selection`]')]
    learning_ = [n for n, line in enumerate(lines) if line.startswith('| L4 | [`Becoming.Learning`]')]
    assert len(selection) == 1 and len(learning_) == 1
    row = lines[selection[0]]
    pairs = [
        ('；读法是 AI 的，依 Ren 的交托采用 / ',
         '；经选项模型的选择（不加前提，选项的相同已定）：两个选项被每个经模型的选择选得相同，恰当模型使二者并列'
         '（`Relabel.selected_alike_iff`）；至多选一个者单独选出一个选项，恰当没有别的选项的条目与它相同'
         '（`Relabel.singled_iff_untied`）；并列的选项取值相同，全并列时选取不选（`Relabel.valued_alike_iff`、'
         '`Relabel.EquivariantChoice.withholds_of_full_tie`）；读法是 AI 的，依 Ren 的交托采用，经模型的选择的读法 Ren '
         '2026-10-16 认可 / '),
        ("; the readings are the AI's, adopted on Ren's delegation |",
         "; selection through a model of the options (no premise; the options' equality decided): two options are "
         "selected alike by every selection through the model exactly when the model ties them "
         "(`Relabel.selected_alike_iff`), one selecting at most one singles out an option exactly when no other "
         "option's entry ties it (`Relabel.singled_iff_untied`), and tied options are valued alike, a choice "
         "withholding at a full tie (`Relabel.valued_alike_iff`, `Relabel.EquivariantChoice.withholds_of_full_tie`); "
         "the readings are the AI's, adopted on Ren's delegation, and that of selection through a model approved by "
         "Ren on 16 October 2026 |"),
    ]
    for old, new in pairs:
        assert row.count(old) == 1, old
        row = row.replace(old, new)
    lines[selection[0]] = row
    row = lines[learning_[0]]
    pairs = [
        ('；理依 Ren 读作',
         '；经选项模型的选择是经其归并的选择（`selects_through_lumping`），对要紧者正确只在要紧者经归并同去之处'
         '（`selects_right_through`、`values_right_lumped`），模型所并者无一经它的选择可分开'
         '（`selects_not_right_of_parted`）；理依 Ren 读作'),
        ('; 理 is read as Ren reads it',
         '; a selection through a model of the options is a selection through its lumping '
         '(`selects_through_lumping`), right about what matters only where what matters goes alike across the '
         'lumping (`selects_right_through`, `values_right_lumped`), so what the model lumps no selection through it '
         'separates (`selects_not_right_of_parted`); 理 is read as Ren reads it'),
    ]
    for old, new in pairs:
        assert row.count(old) == 1, old
        row = row.replace(old, new)
    lines[learning_[0]] = row
    path.write_text('\n'.join(lines))
    print(path)


def chapter():
    path = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md')
    lines = path.read_text().split('\n')
    learning_ = [n for n, line in enumerate(lines) if line.startswith('| L4 | [Becoming.Learning](')]
    assert len(learning_) == 1
    row = lines[learning_[0]]
    old = '，拟合在数据之外正确恰当类在那里决定 | 75 |'
    assert row.endswith(old), row[-80:]
    lines[learning_[0]] = row[:-len(old)] + (
        '，拟合在数据之外正确恰当类在那里决定；经选项模型的选择是经其归并的选择，对要紧者正确只在要紧者经归并同去之处，'
        '模型所并者无一经它的选择可分开 | 83 |')
    path.write_text('\n'.join(lines))
    edit(path, [
        ('只读记录的选择（不加前提，选项的相同已定）：两个选项被每个只读记录的选择选得相同，恰当记录使二者并列；'
         '至多选一个者能单独选出一个选项，恰当没有别的选项的条目与它相同；并列的选项得到相同的值，如权重，'
         '全并列时至多选一个者不选。',
         '经选项模型的选择（不加前提，选项的相同已定）：两个选项被每个经模型的选择选得相同，恰当模型使二者并列；'
         '至多选一个者能单独选出一个选项，恰当没有别的选项的条目与它相同；并列的选项得到相同的值，如权重，'
         '全并列时至多选一个者不选；模型是一个归并，经它的选择对要紧者正确，只在要紧者经此归并同去之处'
         '（`Learning.selects_right_through`）。'),
        ("Selection by the record alone (no premise; the options' equality decided): two options are selected alike by "
         "every selection reading the record alone exactly when the record ties them; one selecting at most one singles "
         "out an option exactly when no other option's entry ties it; tied options take equal values, such as weights, "
         "and at a full tie one selecting at most one selects none.",
         "Selection through a model of the options (no premise; the options' equality decided): two options are "
         "selected alike by every selection through the model exactly when the model ties them; one selecting at most "
         "one singles out an option exactly when no other option's entry ties it; tied options take equal values, such "
         "as weights, and at a full tie one selecting at most one selects none; the model is a lumping, and a selection "
         "through it is right about what matters only where what matters goes alike across the lumping "
         "(`Learning.selects_right_through`)."),
        ('只读记录的选择的实例，', '经选项模型的选择的实例，'),
        ('记录即 `Fin n` 上的条目记录，交换两个中心即 `Relabel.swap`，同等对待中心的规则即只读记录的选取，'
         '同等对待的抽签其权重只读记录，',
         '记录即 `Fin n` 上的选项模型，交换两个中心即 `Relabel.swap`，同等对待中心的规则即经模型的选取，'
         '同等对待的抽签其权重经模型，'),
        ('The instance of selection by the record alone,', 'The instance of selection through a model of the options,'),
        ("a record is the core's record of entries over `Fin n`, exchanging two centers is `Relabel.swap`, a rule "
         "treating the centers alike is a choice reading the record alone, a lottery treating them alike has weights "
         "reading the record alone,",
         "a record is the core's model of the options over `Fin n`, exchanging two centers is `Relabel.swap`, a rule "
         "treating the centers alike is a choice through the model, a lottery treating them alike has weights through "
         "the model,"),
        ('有限分支的提升及只读记录的选择同样', '有限分支的提升及经选项模型的选择同样'),
        ('finite-branching lifting and selection by the record alone connect',
         'finite-branching lifting and selection through a model of the options connect'),
    ])


def notes():
    edit(FORMAL / 'FORMAL-NOTES.md', [
        ('## Selection by the record alone (16 October 2026)\n',
         '## Selection through a model of the options (16 October 2026)\n'),
        ("reads `PluralRecords` and `TieBreaking` as instances of the Becoming core's laws of selection by the record "
         "alone (`Becoming.Selection`, namespace `Relabel`). A record is the core's record of entries over `Fin n`. A "
         "rule that treats the centers alike is a choice reading the record alone, and a lottery that treats them alike "
         "has weights reading the record alone.",
         "reads `PluralRecords` and `TieBreaking` as instances of the Becoming core's laws of selection through a model "
         "of the options (`Becoming.Selection`, namespace `Relabel`; first written as “selection by the record alone” "
         f"and renamed the same day at Ren's correction, [source]({os.path.relpath(SOURCE, FORMAL)})). A record "
         "(`Record n`) is the core's model of the options `Fin n`, an entry for each. A rule that treats the centers "
         "alike is a choice through the model, and a lottery that treats them alike has weights through the model."),
    ])


def periphery():
    edit(FORMAL / 'SelectionRelabelCorrespondence.lean', [
        ('# Plural records and equal chances as instances of selection by the record alone\n',
         '# Plural records and equal chances as instances of selection through a model of the options\n'),
        ("""`TieBreaking` which weights a lottery may give them. A record is the core's record of entries over
the options `Fin n`, and there:""",
         """`TieBreaking` which weights a lottery may give them. A record (`Record n`) is the core's model of
the options `Fin n`, an entry for each, and there:"""),
        ("""  centers alike exactly when it is a choice reading the record alone (`treatsAlike_iff`), a
  lottery exactly when its weights are a valuation reading the record alone and its withholding""",
         """  centers alike exactly when it is a choice through the model (`treatsAlike_iff`), a lottery
  exactly when its weights are a valuation through the model and its withholding"""),
        ("""relations: a selection reading the record alone singles out exactly the options the record parts""",
         """relations: a selection through the model singles out exactly the options the model separates"""),
        ('/-- A rule treats the centers alike exactly when it is a choice reading the record alone. -/',
         '/-- A rule treats the centers alike exactly when it is a choice through the model. -/'),
        ('/-- A lottery treats the centers alike exactly when its weights read the record alone and its\n',
         '/-- A lottery treats the centers alike exactly when its weights are through the model and its\n'),
        ('reading the record alone that selects at most one, so at a full tie it selects none. -/',
         'through the model that selects at most one, so at a full tie it selects none. -/'),
    ], lean=True)
    spec_path = KIT / 'relabel.json'
    raw = spec_path.read_text()
    spec = json.loads(raw)
    for key, pairs in {
        'doc': [("Check the peripheral instance of the Becoming core's laws of selection by the record alone in "
                 "PluralRecords and\nTieBreaking.",
                 "Check the peripheral instance of the Becoming core's laws of selection through a model of the options "
                 "in\nPluralRecords and TieBreaking.")],
        'scope': [("On the Becoming core's laws of selection by the record alone (Becoming.Selection, Relabel): "
                   "PluralRecords' records are the core's records of entries over the options Fin n, exchanging two "
                   "centers is Relabel.swap, a rule treating the centers alike is a choice reading the record alone, a "
                   "lottery treating them alike has weights reading the record alone,",
                   "On the Becoming core's laws of selection through a model of the options (Becoming.Selection, "
                   "Relabel): PluralRecords' records are the core's models of the options Fin n, exchanging two centers "
                   "is Relabel.swap, a rule treating the centers alike is a choice through the model, a lottery treating "
                   "them alike has weights through the model,")],
    }.items():
        for old, new in pairs:
            assert spec[key].count(old) == 1, (key, old[:80])
            spec[key] = spec[key].replace(old, new)
    indent = 2 if raw.startswith('{\n  "') else None
    out = json.dumps(spec, ensure_ascii=False, indent=indent) + ('\n' if raw.endswith('\n') else '')
    assert json.loads(out) == spec
    spec_path.write_text(out)
    print(spec_path)


def inventory():
    edit(STUDY_DIR / 'DECIDABILITY-INVENTORY.py', [
        ("# integration I4b (2026-10-16): a selection by the record alone exchanges two options' entries",
         "# integration I4b (2026-10-16): a selection through a model of the options exchanges two options' entries"),
    ])


def i4a():
    rows_path = I4A / 'rows/D-models.jsonl'
    rows = [json.loads(line) for line in rows_path.read_text().splitlines()]
    edits = {
        'PluralRecords': [("Becoming.Selection's laws of selection by the record alone",
                           "Becoming.Selection's laws of selection through a model of the options"),
                          ('Becoming.Selection 只读记录之选择律', 'Becoming.Selection 经选项模型之选择律')],
        'TieBreaking': [("Becoming.Selection's laws of selection by the record alone",
                         "Becoming.Selection's laws of selection through a model of the options"),
                        ("a lottery's weights are a valuation reading the record alone",
                         "a lottery's weights are a valuation through the model"),
                        ('Becoming.Selection 只读记录之选择律', 'Becoming.Selection 经选项模型之选择律'),
                        ('抽签的权重是只读记录的取值', '抽签的权重是经模型的取值')],
        'SelectionRelabelCorrespondence': [
            ("a record is the core's record of entries over `Fin n`, a rule treating the centers alike is a choice "
             "reading the record alone and a lottery's weights a valuation reading it",
             "a record is the core's model of the options over `Fin n`, a rule treating the centers alike is a choice "
             "through the model and a lottery's weights a valuation through it"),
            ('记录即 `Fin n` 上的条目记录，同等对待中心的规则即只读记录的选取，抽签的权重即只读记录的取值',
             '记录即 `Fin n` 上的选项模型，同等对待中心的规则即经模型的选取，抽签的权重即经模型的取值')],
        'IdealWarrant': [
            ('Its run-level case is now on the spine (`Becoming.Refutable.adheres_iff`, `Becoming.refutable_passes`, '
             'through PrefixSafety); the poset form needs the ideal vocabulary of CompletionRole and HistoryIdeals.',
             'Its run-level case is on the spine (`Becoming.Refutable.adheres_iff`, `Becoming.refutable_passes`, '
             'through PrefixSafety). It defines the posets and ideals CompletionRole and HistoryIdeals build on, and '
             'stays with that line (Ren, 16 October 2026).'),
            ('；偏序形式需要 CompletionRole 与 HistoryIdeals 的理想词汇。',
             '；它定义 CompletionRole 与 HistoryIdeals 所依的偏序与理想，与这条线留在一起（Ren，2026-10-16）。')],
    }
    seen = set()
    for row in rows:
        for old, new in edits.get(row['stem'], []):
            field = 'reason_zh' if re.search(r'[一-鿿]', old) else 'reason_en'
            assert row[field].count(old) == 1, (row['stem'], old[:60])
            row[field] = row[field].replace(old, new)
            seen.add((row['stem'], old))
    assert len(seen) == sum(len(v) for v in edits.values()), 'every row edit applied once'
    rows_path.write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in rows))
    print(rows_path)
    themes_path = I4A / 'themes.json'
    raw = themes_path.read_text()
    themes = json.loads(raw)
    assert json.dumps(themes, ensure_ascii=False, indent=1) == raw, 'themes.json format'
    reach, maths = themes['themes']['reach']['stems'], themes['themes']['mathematics']['stems']
    assert 'IdealWarrant' in reach and 'IdealWarrant' not in maths
    reach.remove('IdealWarrant')
    maths.insert(maths.index('CompletionRole'), 'IdealWarrant')
    themes_path.write_text(json.dumps(themes, ensure_ascii=False, indent=1))
    print(themes_path)


def study(section):
    path = STUDY_DIR / 'BECOMING-RENEWAL-READING.md'
    zh = (KIT / 's_i4b2b_zh.md').read_text().replace('SECTION', str(section))
    en = (KIT / 's_i4b2b_en.md').read_text().replace('SECTION', str(section))
    text = path.read_text()
    assert f'\n## {section}. ' not in text, 'section number taken'
    numbered = [int(m.group(1)) for m in re.finditer(r'^## (\d+)\. ', text, re.M)]
    assert max(numbered) == section - 1, (max(numbered), section)
    summary = '\n## English summary\n'
    assert text.count(summary) == 1
    text = text.replace(summary, '\n' + zh.rstrip('\n') + '\n' + summary)
    text = text.rstrip('\n') + '\n\n' + en.rstrip('\n') + '\n'
    path.write_text(text)
    edit(path, [
        ('## 151. 只读记录的选择（整合 I4b 第二项）：PluralRecords 与 TieBreaking 接入\n\n',
         '## 151. 只读记录的选择（整合 I4b 第二项）：PluralRecords 与 TieBreaking 接入\n\n'
         f'（同日后记：依 Ren 的更正，本节结果改称“经选项模型的选择”，读法撤回，见第{section}节；以下文字作为证据保留。）\n\n'),
        ('**Selection by the record alone, integration I4b item 2 (16 October 2026).** ',
         '**Selection by the record alone, integration I4b item 2 (16 October 2026).** (Reframed the same day in '
         f'section {section} at Ren\'s correction, as selection through a model of the options, its reading withdrawn; '
         'the text below is kept as evidence.) '),
    ])


PARTS = {'learning': learning, 'root': root, 'readme': readme, 'chapter': chapter, 'notes': notes,
         'periphery': periphery, 'inventory': inventory, 'i4a': i4a}


def main():
    args = sys.argv[1:]
    section = None
    if '--section' in args:
        at = args.index('--section')
        section = int(args[at + 1])
        del args[at:at + 2]
    assert args, __doc__
    for part in args:
        if part == 'study':
            assert section, 'study needs --section N'
            study(section)
        else:
            PARTS[part]()


if __name__ == '__main__':
    main()
