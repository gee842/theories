#!/usr/bin/env python3
"""I4b-2: write the schema-2 record selection-by-the-record-alone (run from the repository root at landing).

usage: python3 -B make_record_selection.py SECTION

Run after the core receipt holding the I4b-2 edits of Becoming.Selection exists and the periphery checker
check_selection_relabel_correspondence.py has passed against it. It binds Selection.lean to the retained core receipt,
and SelectionRelabelCorrespondence.lean, PluralRecords.lean and TieBreaking.lean to the retained instance receipt, which
compiled and audited the two originals (they have no receipt of their own; their build record is
inquiry-warrant/BUILD.md). The declarations listed in the laws are checked against the new section of Selection.lean
and the instance module, and the statement, title, validation scope and next delta against the research check's hard
length caps. Names follow board rule 8 (Ren, 16 October 2026): the core law, the instance module and the title state
the structure in the core's vocabulary.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
REC = ROOT / 'theories/becoming/results/records'
BASE = 'experiments/integrated-correction/general-framework/generative-basis/'
SELECTION = BASE + 'lean/becoming/Becoming/Selection.lean'
FORMAL = BASE + 'mathematical-abstraction/acquisition/feedback/remaining-dependency/formal/'
INSTANCE = FORMAL + 'SelectionRelabelCorrespondence.lean'
PLURAL = FORMAL + 'PluralRecords.lean'
TIES = FORMAL + 'TieBreaking.lean'
BUILD = FORMAL + 'inquiry-warrant/BUILD.md'
CORE_POINTER = BASE + 'lean/becoming/becoming-verification.json'
INSTANCE_POINTER = FORMAL + 'selection-relabel-correspondence-verification.json'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
EARLIER = '_process/research/2026-10-05-generative-foundation-review/root-foundation/PLURAL-CLAIMS-INTEGRATION.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCES = ['sources/15-codex-theory-conversations/2026-10-16-i4-decisions.md',
           'sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md',
           'sources/15-codex-theory-conversations/2026-10-16-joined-module-names.md']
REVIEWED = '2026-10-16T00:00:00+00:00'
SECTION = int(sys.argv[1])
# The new section of Selection.lean runs from here to the witnesses; the rest stays with selection-through-registration.
MARKER = '/-! ## Selection by the record alone'
UNTIL = '/-! ## Witnesses'
# The research check's hard caps (tools/research/style.py): (en, zh).
CAPS = {'title': (100, 40), 'statement': (300, 150), 'validation_scope': (600, 260), 'next_delta': (400, 180)}


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def pair(zh, en):
    return {'zh': zh, 'en': en}


def declared(path, after=None, until=None):
    """The fully qualified declarations of a module, read from its namespaces; with `after`, only those following the
    line that starts with it, and with `until`, only those before the line that starts with that."""
    names, spaces, on, done = [], [], after is None, False
    for line in (ROOT / path).read_text().splitlines():
        if not on and line.startswith(after):
            on = True
        if on and until and line.startswith(until):
            done = True
        m = re.match(r'^namespace (\S+)', line)
        if m:
            spaces.append(m.group(1))
            continue
        m = re.match(r'^end (\S+)', line)
        if m and spaces and spaces[-1] == m.group(1):
            spaces.pop()
            continue
        m = re.match(r'^(?:theorem|def|abbrev|structure|inductive|instance)\s+(\S+)', line)
        if m and on and not done:
            names.append('.'.join(spaces + [m.group(1)]))
    assert on and (until is None or done), (after, until)
    return names


def law(zh, en, names):
    return {'zh': zh, 'en': en, 'declarations': names}


def c(*names):
    return ['Becoming.Relabel.' + n for n in names]


def i(*names):
    return ['Becoming.SelectionRelabelCorrespondence.' + n for n in names]


LAWS = [
    law('交换两个选项（swap）是对合。选择、取值与选取只读记录：交换两个选项的条目，即交换所选者、所取的值或所选取者。交换两个并列的选项，'
        '记录不变。',
        'Exchanging two options (swap) is an involution. A selection, a valuation and a choice read the record alone when '
        "exchanging two options' entries exchanges what is selected, the values or the choice. Exchanging two tied "
        'options leaves the record as it was.',
        c('swap', 'swap_left', 'swap_right', 'swap_other', 'swap_swap', 'swap_inj', 'Equivariant', 'EquivariantValue',
          'EquivariantChoice', 'fixed_of_tied')),
    law('并列的选项被选得相同；两个选项被每个只读记录的选择选得相同，恰当记录使二者并列。见证是选出条目等于给定值的选项。',
        'Tied options are selected alike, and two options are selected alike by every selection reading the record '
        'alone exactly when the record ties them. The witness selects the options whose entry equals a given value.',
        c('Equivariant.tied', 'selected_alike_iff')),
    law('至多选一个的只读记录的选择不选并列的选项，两个以上选项全并列时不选。单独持有一个条目（Alone）是这样的选择，所以一个选项能被单独'
        '选出，恰当没有别的选项的条目与它相同。',
        'A selection reading the record alone that selects at most one option selects no tied option, and none at a full '
        'tie of two or more. Holding an entry alone (Alone) is such a selection, so an option can be singled out exactly '
        "when no other option's entry ties it.",
        c('Equivariant.untied', 'Equivariant.none_of_full_tie', 'Alone', 'alone_equivariant', 'alone_single',
          'singled_iff_untied')),
    law('只读记录的取值（如权重）给并列的选项相同的值，全并列时处处相同；取某值的选项是只读记录的选择；常值只读记录；两个选项被每个这样的'
        '取值取得相同，恰当二者并列。',
        'A valuation reading the record alone, such as a weight on each option, gives tied options equal values, and '
        'every option the same at a full tie; the options taking a value form a selection reading the record alone; a '
        'constant valuation reads it; two options are valued alike by every such valuation exactly when tied.',
        c('EquivariantValue.tied', 'EquivariantValue.full_tie', 'EquivariantValue.level', 'EquivariantValue.const',
          'entry_equivariant', 'valued_alike_iff')),
    law('只读记录、至多选取一个选项的选取，其所选取者是只读记录的选择；它不选取并列的选项，全并列时不选取。',
        'A choice of at most one option reading the record alone selects, reading the record alone, the option it '
        'chooses; it chooses no tied option and withholds at a full tie.',
        c('map_swap_eq_some', 'EquivariantChoice.selects', 'EquivariantChoice.single', 'EquivariantChoice.untied',
          'EquivariantChoice.withholds_of_full_tie')),
    law('实例（外围，自有检查器，亦编译审计原文件）：PluralRecords 的记录即 Fin n 上的条目记录，同等对待中心的规则即只读记录的选取，'
        'TieBreaking 同等对待的抽签其权重只读记录；七条定理由核心律给出，PluralRecords.pick 找出单独持有者，公理报告皆空。',
        "Instance (periphery, own checker, which also compiles and audits the originals): PluralRecords' records are "
        'records over Fin n, a rule treating the centers alike is a choice reading the record alone, and a lottery '
        'treating them alike in TieBreaking has weights reading it; seven theorems follow from the core, '
        'PluralRecords.pick finding the holder, every axiom report empty.',
        i('transpose_eq_swap', 'treatsAlike_iff', 'lotteryAlike_iff', 'alone_iff', 'tied_not_served_by_core',
          'first_lt', 'all_tied_forces_withholding_by_core', 'servable_iff_untied_by_core', 'tied_equal_weight_by_core',
          'full_tie_equal_weights_by_core', 'uniform_alike_by_core', 'pointMass_one',
          'point_mass_not_alike_at_tie_by_core')),
]


def passed(pointer, module, source):
    # The top-level receipt is overwritten by the next run; bind its retained copy.
    top = json.loads((ROOT / pointer).read_text())
    if 'retained_run' in top:
        path = str(Path(pointer).parent / top['retained_run'] / 'verification.json')
    else:
        path = BASE + f'lean/becoming/becoming-checks/{top["utc"]}/verification.json'
    receipt = json.loads((ROOT / path).read_text())
    assert receipt['status'] == 'passed', path
    assert receipt['source_sha256'][module] == sha(source), ('receipt predates the source', path, source)
    return path


def record():
    new = declared(SELECTION, MARKER, UNTIL)
    instance = declared(INSTANCE)
    listed = [d for x in LAWS for d in x['declarations']]
    assert sorted(listed) == sorted(new + instance), set(listed) ^ set(new + instance)
    core_receipt = passed(CORE_POINTER, 'Becoming.Selection', SELECTION)
    instance_receipt = passed(INSTANCE_POINTER, 'SelectionRelabelCorrespondence', INSTANCE)
    for module, source in [('PluralRecords', PLURAL), ('TieBreaking', TIES)]:
        assert passed(INSTANCE_POINTER, module, source) == instance_receipt
    checked = json.loads((ROOT / instance_receipt).read_text())
    assert checked['checked_here'] == ['PluralRecords', 'TieBreaking', 'SelectionRelabelCorrespondence']
    assert all(not v for m in checked['modules'] for v in m['axiom_dependencies'].values()), 'nonempty report'
    theorems = sum(1 for line in (ROOT / SELECTION).read_text().splitlines() if line.startswith('theorem '))
    section = (ROOT / SELECTION).read_text().split(MARKER, 1)[1].split(UNTIL, 1)[0]
    added = sum(1 for line in section.splitlines() if line.startswith('theorem '))
    bindings = [
        {'source': SELECTION, 'receipt': core_receipt, 'sha256_pointer': '/source_sha256/Becoming.Selection',
         'success_pointer': '/status', 'success_value': 'passed'},
        {'source': INSTANCE, 'receipt': instance_receipt,
         'sha256_pointer': '/source_sha256/SelectionRelabelCorrespondence',
         'success_pointer': '/status', 'success_value': 'passed'},
        # The instance checker compiled and audited the originals, which have no receipt of their own.
        {'source': PLURAL, 'receipt': instance_receipt, 'sha256_pointer': '/source_sha256/PluralRecords',
         'success_pointer': '/status', 'success_value': 'passed'},
        {'source': TIES, 'receipt': instance_receipt, 'sha256_pointer': '/source_sha256/TieBreaking',
         'success_pointer': '/status', 'success_value': 'passed'},
    ]
    r = {
        'schema_version': 2,
        'id': 'selection-by-the-record-alone',
        'title': pair('只读记录的选择', 'Selection by the record alone'),
        'kind': 'theorem',
        'status': 'recorded-checked',
        'family': 'F04',
        'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '对相同已定的选项与任何种类条目的记录：两个选项被每个只读记录的选择选得相同，恰当记录使二者并列；至多选一个选项的这种选择能选出 '
            'k，恰当没有别的选项的条目等于 k 的。',
            'For options with decided equality and a record of entries of any kind: two options are selected alike by '
            'every selection reading the record alone exactly when the record ties them, and such a selection selecting '
            "at most one option can select k exactly when no other option's entry equals k's."),
        'laws': LAWS,
        'hypotheses': [pair(
            '不加公理。选项的相同已定（交换两个选项需要它）；条目任意种类；选择、取值或选取只读记录是假设。',
            'No axiom. The options\' equality is decided (exchanging two options needs it); entries are of any kind; '
            'that a selection, valuation or choice reads the record alone is a hypothesis.')],
        'does_not_show': [
            {**pair('单独选出的选项由一个选取函数找到：这需在列出的选项中搜索，外围用 PluralRecords.pick。',
                    'That an option singled out is found by a choice function: that needs a search over listed '
                    "options, the periphery's PluralRecords.pick."), 'kind': 'scope'},
            {**pair('平局中等概率的抽签是否正当，按条目大小或按轮次的优先：保持原文件的范围。',
                    'Whether an equal chance legitimately breaks a tie, or priority by size or by turn: these keep the '
                    "originals' scope."), 'kind': 'scope'},
            {**pair('选项的相同不判定时的形式：交换两个选项需要判定。',
                    "A form without the options' equality decided: exchanging two options needs it."),
             'kind': 'scope'},
        ],
        'counterexamples': [],
        'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'formal-not-empirical', 'names-provisional',
                                'omission-not-refutation'],
        'validation_scope': pair(
            f'Lean 4.29.1 合并检查器实查：Becoming.Selection 共 {theorems} 项定理，新增 {len(new)} 项声明（{added} 项定理）公理报告'
            f'为空。外围实例 SelectionRelabelCorrespondence 由其检查器实查（Lean 4.30.0-rc2），它也编译并审计未有回执的 PluralRecords 与 '
            f'TieBreaking，每项公理报告为空。作者反审见研究 §{SECTION}；未经独立审查。',
            f'Machine-checked by the consolidated Lean 4.29.1 checker: Becoming.Selection has {theorems} theorems, and '
            f'the {len(new)} new declarations ({added} theorems) have empty axiom reports. The periphery instance '
            f'SelectionRelabelCorrespondence is checked by its own checker (Lean 4.30.0-rc2), which also compiles and '
            f'audits PluralRecords and TieBreaking, unreceipted before; every axiom report is empty. Author '
            f'counterreview in study section {SECTION}; not independently reviewed.'),
        'next_delta': pair(
            '独立审查；Ren 对读法的判断；两两关系之记录上的同一律。',
            "An independent review; Ren's judgment of the reading; the same law over records of pairwise relations."),
        'correspondence': pair(
            'Ren 2026-10-16 对 I4 归类表选择“Closest gaps first”。归类表把 PluralRecords 与 TieBreaking 读作待接入的律：Selection 陈述了'
            '经识的选择恰及所识，未陈述只读记录的选择。名依 Ren 同日的接入命名规则。读法（AI 的，待 Ren）：哪个选项是哪个不在记录的关系之中；'
            '要分开记录所并列者，需另一被记录的关系，如到达的次序或约定，正如经识选择的缺口只经关系而合。',
            'Ren, 16 October 2026, chose “Closest gaps first” on the I4 classification table. The table read PluralRecords '
            'and TieBreaking as join candidates: Selection stated that selection through registration reaches exactly '
            'what registers, not selection by the record alone. The names follow Ren\'s rule of the same day for joined '
            'modules. Reading (the AI\'s, pending Ren): which option is which is not among the record\'s relations; to '
            'part what the record ties takes a further recorded relation, such as an order of arrival or an agreement, '
            'as the gap of selection through registration closes only through relations.'),
        'canonical_source': SELECTION,
        'aliases': ['Becoming.Relabel.selected_alike_iff', 'Becoming.Relabel.singled_iff_untied',
                    'Becoming.Relabel.Equivariant', 'Becoming.Relabel.EquivariantValue.tied',
                    'Becoming.Relabel.EquivariantChoice.withholds_of_full_tie', 'selection by the record alone',
                    '只读记录的选择', 'exchange-invariant selection', 'equivariant selection'],
        'dependencies': [],
        'related': [{'id': 'selection-through-registration', 'detail': pair(
            '同一形式的律：经识的选择恰及所识（Web.selects_alike_iff），只读记录的选择恰分开记录所分开者。',
            'A law of the same form: selection through registration reaches exactly what registers '
            '(Web.selects_alike_iff), and selection by the record alone parts exactly what the record parts.')}],
        'references': [
            {'path': SELECTION, 'role': 'proof', 'sha256': sha(SELECTION), 'declarations': new},
            {'path': INSTANCE, 'role': 'proof', 'sha256': sha(INSTANCE), 'declarations': instance},
            {'path': PLURAL, 'role': 'proof', 'sha256': sha(PLURAL),
             'declarations': ['PluralRecords.TreatsAlike', 'PluralRecords.Alone', 'PluralRecords.pick',
                              'PluralRecords.tied_not_served', 'PluralRecords.all_tied_forces_withholding',
                              'PluralRecords.servable_iff_untied']},
            {'path': TIES, 'role': 'proof', 'sha256': sha(TIES),
             'declarations': ['TieBreaking.LotteryAlike', 'TieBreaking.tied_equal_weight',
                              'TieBreaking.full_tie_equal_weights', 'TieBreaking.uniform_alike', 'TieBreaking.pointMass',
                              'TieBreaking.point_mass_not_alike_at_tie']},
            {'path': core_receipt, 'role': 'receipt', 'sha256': sha(core_receipt)},
            {'path': instance_receipt, 'role': 'receipt', 'sha256': sha(instance_receipt)},
            {'path': BUILD, 'role': 'provenance', 'sha256': sha(BUILD)},
            {'path': EARLIER, 'role': 'integration', 'sha256': sha(EARLIER)},
            {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
            {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
        ] + [{'path': s, 'role': 'provenance', 'sha256': sha(s)} for s in SOURCES],
        'proof_bindings': bindings,
        'history': [pair(
            f'2026-10-16：新增，整合 I4b 第二项（Ren 选择“Closest gaps first”）；研究 §{SECTION}。',
            f'16 October 2026: added, integration I4b item 2 (Ren chose “Closest gaps first”); study section {SECTION}.')],
        'text_versions': [],
    }
    for key, (en, zh) in CAPS.items():
        assert len(r[key]['en']) <= en and len(r[key]['zh']) <= zh, (key, len(r[key]['en']), len(r[key]['zh']))
    return r


def main():
    r = record()
    (REC / f'{r["id"]}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('wrote', r['id'], len(r['references'][0]['declarations']), '+', len(r['references'][1]['declarations']),
          'declarations; statement', len(r['statement']['en']), '/', len(r['statement']['zh']), 'chars')


if __name__ == '__main__':
    main()
