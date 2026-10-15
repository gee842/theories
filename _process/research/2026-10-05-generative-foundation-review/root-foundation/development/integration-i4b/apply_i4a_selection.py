#!/usr/bin/env python3
"""I4b-2: the I4a classification rows for the Selection join (run from the repository root, then rerun the I4a pipeline,
RUBRIC.md "Reproducing the table").

PluralRecords and TieBreaking become joined, with the spine laws they instantiate; SelectionRelabelCorrespondence gets
a joined row in the same family file; the theme `symmetry` (“Symmetry and ties”), which held only these two, is
removed, since a joined row takes no theme. Rows are matched by stem, so the script applies on any base holding them;
it asserts each edit once."""
import json
from pathlib import Path

A = Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/development/integration-i4a')
ROWS = A / 'rows/D-models.jsonl'
THEMES = A / 'themes.json'
FORMAL = ('experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/'
          'feedback/remaining-dependency/formal/')
JOINED = {
    'PluralRecords': {
        'spine': ['Becoming.Relabel.singled_iff_untied', 'Becoming.Relabel.EquivariantChoice.untied',
                  'Becoming.Relabel.EquivariantChoice.withholds_of_full_tie'],
        'reason_en': "Its tie laws are instances of Becoming.Selection's laws of selection by the record alone (I4b, 16 "
                     'October 2026): SelectionRelabelCorrespondence restates tied_not_served, '
                     'all_tied_forces_withholding and servable_iff_untied by core, with `PluralRecords.pick` the search.',
        'reason_zh': '其平局律是 Becoming.Selection 只读记录之选择律的实例（I4b，2026-10-16）：SelectionRelabelCorrespondence 由核心'
                     '重述 tied_not_served、all_tied_forces_withholding 与 servable_iff_untied，搜索由 `PluralRecords.pick` 完成。'},
    'TieBreaking': {
        'spine': ['Becoming.Relabel.EquivariantValue.tied', 'Becoming.Relabel.EquivariantValue.full_tie',
                  'Becoming.Relabel.Equivariant.none_of_full_tie'],
        'reason_en': "Its weight laws are instances of Becoming.Selection's laws of selection by the record alone (I4b, "
                     "16 October 2026): a lottery's weights are a valuation reading the record alone, and "
                     'SelectionRelabelCorrespondence restates tied_equal_weight, full_tie_equal_weights, uniform_alike '
                     'and point_mass_not_alike_at_tie by core.',
        'reason_zh': '其权重律是 Becoming.Selection 只读记录之选择律的实例（I4b，2026-10-16）：抽签的权重是只读记录的取值，'
                     'SelectionRelabelCorrespondence 由核心重述 tied_equal_weight、full_tie_equal_weights、uniform_alike 与 '
                     'point_mass_not_alike_at_tie。'},
}
INSTANCE = {
    'stem': 'SelectionRelabelCorrespondence', 'path': FORMAL + 'SelectionRelabelCorrespondence.lean',
    'category': 'joined',
    'spine': ['Becoming.Relabel.Equivariant', 'Becoming.Relabel.EquivariantChoice', 'Becoming.Relabel.EquivariantValue'],
    'relation': '', 'basis': 'statements read',
    'reason_en': "The periphery instance module of I4b item 2: a record is the core's record of entries over `Fin n`, a "
                 "rule treating the centers alike is a choice reading the record alone and a lottery's weights a "
                 'valuation reading it; the core laws give the tie laws, every axiom report empty.',
    'reason_zh': 'I4b 第二项的外围实例模块：记录即 `Fin n` 上的条目记录，同等对待中心的规则即只读记录的选取，抽签的权重即只读记录的取值；'
                 '核心律给出各平局律，公理报告皆空。'}

rows = [json.loads(line) for line in ROWS.read_text().splitlines() if line.strip()]
for stem, change in JOINED.items():
    matched = [r for r in rows if r['stem'] == stem]
    assert len(matched) == 1 and matched[0]['category'] == 'join-candidate', stem
    matched[0].update(category='joined', relation='', **change)
assert not any(r['stem'] == INSTANCE['stem'] for r in rows)
at = max(i for i, r in enumerate(rows) if r['stem'] in JOINED) + 1
rows.insert(at, INSTANCE)
ROWS.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows))

text = THEMES.read_text()
themes = json.loads(text)
# themes.json is written with one-space indentation and no final newline; keep that form.
assert json.dumps(themes, ensure_ascii=False, indent=1) == text
assert sorted(themes['themes']['symmetry']['stems']) == sorted(JOINED)
del themes['themes']['symmetry']
THEMES.write_text(json.dumps(themes, ensure_ascii=False, indent=1))
print('joined', ', '.join(JOINED), '; row', INSTANCE['stem'], '; theme symmetry removed')
