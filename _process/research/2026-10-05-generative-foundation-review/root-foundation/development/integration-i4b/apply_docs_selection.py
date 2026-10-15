#!/usr/bin/env python3
"""I4b-2: the documents naming Becoming.Selection's laws of selection by the record alone and the instance
SelectionRelabelCorrespondence (run from the repository root): python3 -B apply_docs_selection.py [PART ...]

PART is any of `module`, `chapter`, `package`, `notes` (default all):
* module: the docstring of Selection.lean, a bullet for the new section and the line on what is not derived;
* chapter: the theory chapter's §9 row for Becoming.Selection, now bilingual, with its theorem count; a §9 periphery row
  for SelectionRelabelCorrespondence after the last periphery row; its name in the chapter's lists of peripheral
  instance modules, zh and en (the lists with or without I4b-4's FiniteBranchingCorrespondence);
* package: the module bullet in Becoming.lean;
* notes: a paragraph in the remaining-dependency package's FORMAL-NOTES.md.
Each edit asserts the text it replaces, so a second run of a part fails. After a merge that conflicts in the chapter,
take the merged chapter without this branch's edits and run `chapter` again."""
import re
import sys
from pathlib import Path

LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
PACKAGE = ('experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/'
           'feedback/remaining-dependency/formal/')
SELECTION = Path(LEAN + 'becoming/Becoming/Selection.lean')
INSTANCE = Path(PACKAGE + 'SelectionRelabelCorrespondence.lean')
PARTS = sys.argv[1:] or ['module', 'chapter', 'package', 'notes']


def count(path):
    return sum(1 for line in path.read_text().splitlines() if re.match(r'^theorem ', line))


def change(s, old, new, what):
    assert s.count(old) == 1, what
    return s.replace(old, new)


if 'module' in PARTS:
    s = SELECTION.read_text()
    s = change(s, """
**Readings (the AI's, adopted on Ren's delegation of 15 October 2026, DELEGATED-CHOICES D25).**""", """* **By the record alone.** Options are told apart only by what a record holds of each. A
  selection reads the record alone when exchanging two options' entries exchanges what it
  selects (`Relabel.Equivariant`). Two options are selected alike by every such selection exactly
  when the record ties them (`Relabel.selected_alike_iff`), as a selection through registration
  reaches exactly what registers. One selecting at most one option singles out exactly the
  options whose entry no other option shares (`Relabel.singled_iff_untied`, the selection
  `Relabel.Alone`), and at a full tie of two or more options it selects none
  (`Relabel.Equivariant.none_of_full_tie`). A valuation reading the record alone, such as a
  weight on each option, gives tied options equal values (`Relabel.EquivariantValue.tied`,
  `Relabel.valued_alike_iff`), and a choice of one option chooses no tied option and withholds at
  a full tie (`Relabel.EquivariantChoice.untied`, `Relabel.EquivariantChoice.withholds_of_full_tie`).
  Exchanging two options tells them apart: their equality is decided, a condition each statement
  names. Reading (the AI's, pending Ren): which option is which is not part of the record's
  relations; to part what the record ties takes a further recorded relation, such as an order of
  arrival or an agreement.

**Readings (the AI's, adopted on Ren's delegation of 15 October 2026, DELEGATED-CHOICES D25).**""",
               'Selection docstring bullet')
    s = change(s, """registration at all (supplied as `Web.SelectsThrough`), that offspring follow the selection, and
that reaching beyond is chosen.""", """registration at all (supplied as `Web.SelectsThrough`), that offspring follow the selection,
that reaching beyond is chosen, that a selection reads the record alone, and how an option it
singles out is found (a search over listed options).""", 'Selection not derived')
    SELECTION.write_text(s)

if 'chapter' in PARTS:
    chapter = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md')
    s = chapter.read_text()
    s = change(s, '选择给出携带者时后代中的份额上升（`share_rises` 的应用） | 43 |',
               '选择给出携带者时后代中的份额上升（`share_rises` 的应用）。只读记录的选择（不加前提，选项的相同已定）：两个选项被每个只读记录的'
               '选择选得相同，恰当记录使二者并列；至多选一个者能单独选出一个选项，恰当没有别的选项的条目与它相同；并列的选项得到相同的值，'
               '如权重，全并列时至多选一个者不选。'
               '/ Selection through registration (no premise): two histories are selected alike by every selection '
               "through a selector's registration exactly when it registers them alike, a pooled registration "
               'likewise; with the rest of the exchange fixed, selections and scores are blind beyond the registration '
               'closure, also pooled with formations within it; the gap is the reach closure less the registration '
               "closure: the clearer's selection does not see the dweller's end, which the dweller's registration and "
               'the pooled one select; a flow reaching beyond the registration closure to raise what registers is '
               'selected, and selected alike with raising it without reaching beyond; where a selection supplies the '
               'carriers their share rises among descendants (`share_rises` applied). Selection by the record alone (no '
               "premise; the options' equality decided): two options are selected alike by every selection reading the "
               'record alone exactly when the record ties them; one selecting at most one singles out an option exactly '
               "when no other option's entry ties it; tied options take equal values, such as weights, and at a full tie "
               f'one selecting at most one selects none. | {count(SELECTION)} |', 'chapter Selection row')
    rows = [line for line in s.split('\n') if line.startswith('| 外围实例 / Peripheral instances |')]
    last = rows[-1] + '\n'
    s = change(s, last, last +
               '| 外围实例 / Peripheral instances | [SelectionRelabelCorrespondence](../../../' + PACKAGE +
               'SelectionRelabelCorrespondence.lean) | 只读记录的选择的实例，用 Lean 4.30.0-rc2，由 '
               'check_selection_relabel_correspondence.py 另行检查，它也编译与审计未有回执的原文件 PluralRecords 与 '
               'TieBreaking，每项公理报告为空：记录即 `Fin n` 上的条目记录，交换两个中心即 `Relabel.swap`，同等对待中心的规则即只读记录的'
               '选取，同等对待的抽签其权重只读记录，单独持有一个条目即 `Relabel.Alone`（`transpose_eq_swap`、`treatsAlike_iff`、'
               '`lotteryAlike_iff`、`alone_iff`）；核心律给出 `tied_not_served`、`all_tied_forces_withholding`、`servable_iff_untied`'
               '（`PluralRecords.pick` 找出单独持有者）、`tied_equal_weight`、`full_tie_equal_weights`、`uniform_alike` 与 '
               '`point_mass_not_alike_at_tie`（各为 `_by_core`）。'
               '/ The instance of selection by the record alone, with Lean 4.30.0-rc2, checked separately by '
               'check_selection_relabel_correspondence.py, which also compiles and audits the unreceipted originals '
               'PluralRecords and TieBreaking, every axiom report empty: a record is the core\'s record of entries over '
               '`Fin n`, exchanging two centers is `Relabel.swap`, a rule treating the centers alike is a choice reading '
               'the record alone, a lottery treating them alike has weights reading the record alone, and holding an '
               'entry alone is `Relabel.Alone` (`transpose_eq_swap`, `treatsAlike_iff`, `lotteryAlike_iff`, '
               '`alone_iff`); the core\'s laws give `tied_not_served`, `all_tied_forces_withholding`, '
               '`servable_iff_untied` (`PluralRecords.pick` finding the holder), `tied_equal_weight`, '
               '`full_tie_equal_weights`, `uniform_alike` and `point_mass_not_alike_at_tie` (each `_by_core`). '
               f'| {count(INSTANCE)} |\n', 'chapter periphery row')
    if '、无穷迹的前缀序及有限分支的提升同样经' in s:
        s = change(s, '、无穷迹的前缀序及有限分支的提升同样经', '、无穷迹的前缀序、有限分支的提升及只读记录的选择同样经', 'zh list words')
        s = change(s, 'the prefix order of infinite traces and finite-branching lifting connect',
                   'the prefix order of infinite traces, finite-branching lifting and selection by the record alone connect',
                   'en list words')
    else:
        s = change(s, '组织中池的起源及无穷迹的前缀序同样经', '组织中池的起源、无穷迹的前缀序及只读记录的选择同样经', 'zh list words')
        s = change(s, "the origin of an organization's pools and the prefix order of infinite traces connect",
                   "the origin of an organization's pools, the prefix order of infinite traces and selection by the "
                   "record alone connect", 'en list words')
    s, n = re.subn(r'(PrefixSafetyCorrespondence(?:、FiniteBranchingCorrespondence)?)）',
                   r'\1、SelectionRelabelCorrespondence）', s)
    assert n == 1, 'zh list'
    s, n = re.subn(r'(PrefixSafetyCorrespondence(?:, FiniteBranchingCorrespondence)?)\)',
                   r'\1, SelectionRelabelCorrespondence)', s)
    assert n == 1, 'en list'
    chapter.write_text(s)

if 'package' in PARTS:
    package = Path(LEAN + 'becoming/Becoming.lean')
    s = package.read_text()
    s = change(s, """15 October 2026.
* `Becoming.Learning`""", """15 October 2026. By the record alone: two options are selected alike by every
  selection reading only a record exactly when the record ties them, one is singled out exactly
  where the record parts it from every other, and tied options are valued alike.
* `Becoming.Learning`""", 'package bullet')
    package.write_text(s)

if 'notes' in PARTS:
    notes = Path(PACKAGE + 'FORMAL-NOTES.md')
    s = notes.read_text()
    assert s.endswith('\n')
    s += """
## Selection by the record alone (16 October 2026)

[SelectionRelabelCorrespondence.lean](SelectionRelabelCorrespondence.lean) reads `PluralRecords` and `TieBreaking` as instances of the Becoming core's laws of selection by the record alone (`Becoming.Selection`, namespace `Relabel`). A record is the core's record of entries over `Fin n`. A rule that treats the centers alike is a choice reading the record alone, and a lottery that treats them alike has weights reading the record alone. `tied_not_served`, `all_tied_forces_withholding`, `servable_iff_untied`, `tied_equal_weight`, `full_tie_equal_weights`, `uniform_alike` and `point_mass_not_alike_at_tie` follow from the core's laws, each with an empty axiom report. The core states these laws for any options with decided equality and entries of any kind, as relations, with no search.

It imports the core, so it is compiled by [check_selection_relabel_correspondence.py](check_selection_relabel_correspondence.py) with Lean 4.30.0-rc2. That checker also compiles and audits `PluralRecords` and `TieBreaking`, whose build record is [inquiry-warrant/BUILD.md](inquiry-warrant/BUILD.md) and which had no machine receipt. Every declaration of the three modules must have an empty axiom report. The one warning the originals print, the unused hypothesis `noWithhold` of `TieBreaking.full_tie_open_uniform`, is the only output allowed beyond the audits, and the receipt records it. `PluralRecords` and `TieBreaking` are unchanged.
"""
    notes.write_text(s)

print('parts', PARTS, '; Selection', count(SELECTION), 'theorems; instance', count(INSTANCE))
