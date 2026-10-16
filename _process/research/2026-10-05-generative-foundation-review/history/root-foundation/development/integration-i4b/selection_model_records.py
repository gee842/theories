#!/usr/bin/env python3
"""I4b-2 follow-up (Ren, 16 October 2026: “go ahead with the reframing, first title, keep names, (a)”): the records,
run from the repository root at landing.

usage: python3 -B selection_model_records.py SECTION

Run after the core receipt holding this branch's Selection.lean and Learning.lean exists, after
check_selection_relabel_correspondence.py has passed against it, and after `selection_model_docs.py study --section
SECTION` has inserted the study section.

1. selection-by-the-record-alone becomes selection-through-a-model-of-the-options (`git mv`, the old identifier kept as
   an alias, as draws-on-a-shared-stock kept aggregate-exit-funding). Title, statement, laws, hypotheses,
   correspondence and next steps name the model; the withdrawn reading leaves the correspondence and the former wording
   stays in study section 151. A law with Learning's eight new theorems is added. Selection.lean and Learning.lean bind
   the retained core receipt; the instance and the two originals bind the retained instance receipt.
2. The other records citing Selection.lean or Learning.lean take the new hashes, their bindings move to the retained core
   receipt, and the declarations they cite are asserted unchanged. selection-through-registration's link follows the new
   identifier; generalization-through-lumping links the new record.
Each changed record gains one paired, dated history note. Every hash refreshed here is of a file this follow-up changed
and whose change was read; any other reference of the renamed record must still match.
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()
REC = ROOT / 'theories/becoming/results/records'
BASE = 'experiments/integrated-correction/general-framework/generative-basis/'
SELECTION = BASE + 'lean/becoming/Becoming/Selection.lean'
LEARNING = BASE + 'lean/becoming/Becoming/Learning.lean'
FORMAL = BASE + 'mathematical-abstraction/acquisition/feedback/remaining-dependency/formal/'
INSTANCE = FORMAL + 'SelectionRelabelCorrespondence.lean'
PLURAL = FORMAL + 'PluralRecords.lean'
TIES = FORMAL + 'TieBreaking.lean'
CORE_POINTER = BASE + 'lean/becoming/becoming-verification.json'
INSTANCE_POINTER = FORMAL + 'selection-relabel-correspondence-verification.json'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-16-selection-through-a-model.md'
OLD, NEW = 'selection-by-the-record-alone', 'selection-through-a-model-of-the-options'
MARKER, UNTIL = '/-! ## Selection through a model of the options', '/-! ## Witnesses'
# Files this follow-up changed; their hashes are refreshed in the renamed record.
CHANGED = {SELECTION, LEARNING, INSTANCE, STUDY, CHAPTER}
CAPS = {'title': (100, 40), 'statement': (300, 150), 'validation_scope': (600, 260), 'next_delta': (400, 180)}
DRY = '--dry' in sys.argv  # a test run without the new receipts: the receipt checks are skipped
SECTION = int([a for a in sys.argv[1:] if a != '--dry'][0])


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def pair(zh, en):
    return {'zh': zh, 'en': en}


def declared(path, after=None, until=None):
    """The fully qualified declarations of a module from its namespaces; with `after`, only those following the line
    that starts with it, and with `until`, only those before the line that starts with that."""
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


def passed(pointer, module, source):
    """The retained copy of the receipt `pointer` names, checked to have passed for the current bytes of `source`."""
    top = json.loads((ROOT / pointer).read_text())
    if 'retained_run' in top:
        path = str(Path(pointer).parent / top['retained_run'] / 'verification.json')
    else:
        path = BASE + f'lean/becoming/becoming-checks/{top["utc"]}/verification.json'
    receipt = json.loads((ROOT / path).read_text())
    if not DRY:
        assert receipt['status'] == 'passed', path
        assert receipt['source_sha256'][module] == sha(source), ('receipt predates the source', path, source)
    return path


def binding(source, receipt, module):
    return {'source': source, 'receipt': receipt, 'sha256_pointer': f'/source_sha256/{module}',
            'success_pointer': '/status', 'success_value': 'passed'}


def move_receipt(r, source, receipt, module):
    """Point `source`'s binding at `receipt`, reference it, and drop an earlier receipt no binding reads any more."""
    found = [b for b in r['proof_bindings'] if b['source'] == source]
    assert len(found) == 1, (r['id'], source)
    old = found[0]['receipt']
    found[0].update(binding(source, receipt, module))
    if not any(x['path'] == receipt for x in r['references']):
        r['references'].append({'path': receipt, 'role': 'receipt', 'sha256': sha(receipt)})
    if old != receipt and not any(b['receipt'] == old for b in r['proof_bindings']):
        r['references'] = [x for x in r['references'] if x['path'] != old]


def write(r, path):
    path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print(path.relative_to(ROOT))


def renamed(core, instance):
    if (REC / f'{OLD}.json').exists():
        assert not (REC / f'{NEW}.json').exists()
        for ext in ('json', 'md'):
            if (REC / f'{OLD}.{ext}').exists():
                subprocess.run(['git', 'mv', str(REC / f'{OLD}.{ext}'), str(REC / f'{NEW}.{ext}')], check=True)
    path = REC / f'{NEW}.json' if (REC / f'{NEW}.json').exists() else REC / f'{OLD}.json'
    r = json.loads(path.read_text())
    assert r['id'] in (OLD, NEW) and len(r['laws']) == 6, (r['id'], len(r['laws']))
    learning = declared(LEARNING, MARKER, UNTIL)
    assert len(learning) == 8 and all(n.startswith('Becoming.Learning.') for n in learning), learning
    selection = r['references'][0]['declarations']
    assert r['references'][0]['path'] == SELECTION and set(selection) <= set(declared(SELECTION)), 'Selection unchanged'
    texts = [
        ('交换两个选项（swap）是对合。选择、取值与选取经模型：交换两个选项的条目，即交换所选者、所取的值或所选取者。'
         '交换两个并列的选项，模型不变。',
         "Exchanging two options (swap) is an involution. A selection, a valuation and a choice are through the model "
         "when exchanging two options' entries exchanges what is selected, the values or the choice. Exchanging two "
         "tied options leaves the model as it was."),
        ('并列的选项被选得相同；两个选项被每个经模型的选择选得相同，恰当模型使二者并列。见证是选出条目等于给定值的选项。',
         'Tied options are selected alike, and two options are selected alike by every selection through the model '
         'exactly when the model ties them. The witness selects the options whose entry equals a given value.'),
        ('至多选一个的经模型的选择不选并列的选项，两个以上选项全并列时不选。单独持有一个条目（Alone）是这样的选择，'
         '所以一个选项能被单独选出，恰当没有别的选项的条目与它相同。',
         "A selection through the model that selects at most one option selects no tied option, and none at a full tie "
         "of two or more. Holding an entry alone (Alone) is such a selection, so an option can be singled out exactly "
         "when no other option's entry ties it."),
        ('经模型的取值（如权重）给并列的选项相同的值，全并列时处处相同；取某值的选项是经模型的选择；常值经模型；'
         '两个选项被每个这样的取值取得相同，恰当二者并列。',
         'A valuation through the model, such as a weight on each option, gives tied options equal values, and every '
         'option the same at a full tie; the options taking a value form a selection through the model; a constant '
         'valuation is one; two options are valued alike by every such valuation exactly when tied.'),
        ('经模型、至多选取一个选项的选取，其所选取者是经模型的选择；它不选取并列的选项，全并列时不选取。',
         'A choice of at most one option through the model selects, through the model, the option it chooses; it '
         'chooses no tied option and withholds at a full tie.'),
    ]
    laws = [dict(law, zh=zh, en=en) for law, (zh, en) in zip(r['laws'][:5], texts)]
    laws.append({'zh': '模型是一个归并（Learning.Lumped）：经模型的选择是经其归并的选择，对要紧者（谓词 p 或取值 f）正确，只在要紧者'
                       '经归并同去之处；要紧者分开模型所并的两个选项时，无一正确；要紧者从模型读出时，经模型读出即正确。',
                 'en': 'The model is a lumping (Learning.Lumped): a selection through it is a selection through its '
                       'lumping, right about what matters (a predicate p or values f) only where what matters goes '
                       'alike across the lumping; where what matters separates two options the model lumps, none is '
                       'right; where it is read off the model, reading it through the model is right.',
                 'declarations': learning})
    instance_law = r['laws'][5]
    laws.append(dict(instance_law,
                     zh='实例（外围，自有检查器，亦编译审计原文件）：PluralRecords 的记录即 Fin n 上的选项模型，同等对待中心的规则'
                        '即经模型的选取，TieBreaking 同等对待的抽签其权重经模型；七条定理由核心律给出，PluralRecords.pick '
                        '找出单独持有者，公理报告皆空。',
                     en="Instance (periphery, own checker, which also compiles and audits the originals): PluralRecords' "
                        'records are models of the options Fin n, a rule treating the centers alike is a choice through '
                        'the model, and a lottery treating them alike in TieBreaking has weights through it; seven '
                        'theorems follow from the core, PluralRecords.pick finding the holder, every axiom report empty.'))
    assert set(instance_law['declarations']) == set(declared(INSTANCE)), 'instance declarations unchanged'
    r.update({
        'id': NEW,
        'title': pair('经选项模型的选择', 'Selection through a model of the options'),
        'statement': pair('对相同已定的选项与给每个选项任何种类条目的模型：两个选项被每个经模型的选择选得相同，恰当模型使二者并列；'
                          '至多选一个选项的这种选择能选出 k，恰当没有别的选项的条目等于 k 的。',
                          'For options with decided equality and a model giving each an entry of any kind: two options '
                          'are selected alike by every selection through the model exactly when the model ties them, '
                          "and such a selection selecting at most one option can select k exactly when no other "
                          "option's entry equals k's."),
        'laws': laws,
        'hypotheses': [pair('不加公理。选项的相同已定（交换两个选项需要它）；条目任意种类；选择、取值或选取经模型是假设；'
                            '要紧者（p、f）是给出的。',
                            'No axiom. The options\' equality is decided (exchanging two options needs it); entries are '
                            'of any kind; that a selection, valuation or choice is through the model is a hypothesis, '
                            'and what matters (p, f) is given.')],
        'validation_scope': pair(
            f'Lean 4.29.1 合并检查器实查：Becoming.Selection 共 67 项定理，该节 29 项声明（24 项定理）公理报告为空；'
            f'Becoming.Learning 共 {sum(1 for x in (ROOT / LEARNING).read_text().splitlines() if x.startswith("theorem "))} '
            f'项定理，新增 8 项公理报告为空。外围实例 SelectionRelabelCorrespondence 由其检查器实查（Lean 4.30.0-rc2），'
            f'也编译并审计 PluralRecords 与 TieBreaking，每项公理报告为空。未经独立审查。',
            'Machine-checked by the consolidated Lean 4.29.1 checker: Becoming.Selection has 67 theorems, the 29 '
            'declarations of its section (24 theorems) with empty axiom reports, and Becoming.Learning '
            f'{sum(1 for x in (ROOT / LEARNING).read_text().splitlines() if x.startswith("theorem "))}, its 8 new '
            'theorems with empty axiom reports. The periphery instance SelectionRelabelCorrespondence is checked by its '
            'own checker (Lean 4.30.0-rc2), which also compiles and audits PluralRecords and TieBreaking; every axiom '
            'report is empty. Not independently reviewed.'),
        'next_delta': pair('独立审查；模型的条目为选项之间关系时的同一律。',
                           "An independent review; the same law where the model's entries are relations between options."),
        'correspondence': pair(
            'Ren 2026-10-16 对 I4 归类表选择“Closest gaps first”；PluralRecords 与 TieBreaking 读作待接入的律，名依 Ren '
            '同日的接入命名规则。结果初名“只读记录的选择”；Ren 同日更正：“it is about the cognitive model, not just '
            'record, which feels as long as we remember all pasts we can move forward without wisdom”，并认可重新框定。'
            '读法（AI 对 Ren 的更正的读法，Ren 认可）：模型所并者，经它的选择分不开；要分开需要更细的模型，那个模型是否正确'
            '在于它对要紧者的拟合，记得更多并不提供。原读法“需另一被记录的关系，如到达的次序”撤回。',
            'Ren, 16 October 2026, chose “Closest gaps first” on the I4 classification table; PluralRecords and '
            "TieBreaking were read as join candidates, and the names follow Ren's rule of the same day for joined "
            'modules. The result was first titled “Selection by the record alone”. Ren corrected it the same day: '
            '“it is about the cognitive model, not just record, which feels as long as we remember all pasts we can '
            'move forward without wisdom”, and approved the reframing. Reading (the AI\'s reading of Ren\'s correction, '
            'approved by Ren): what a model lumps, no selection through it can separate; separating them takes a finer '
            'model, and whether that model is right is its fit to what matters, which remembering more does not '
            'supply. The earlier reading, that a further recorded relation such as an order of arrival parts a tie, is '
            'withdrawn.'),
        'aliases': [a for a in r['aliases'] if a not in (OLD, NEW)] + [
            OLD, 'selection through a model of the options', '经选项模型的选择',
            'Becoming.Learning.selects_right_through', 'Becoming.Learning.selects_not_right_of_parted'],
    })
    r['does_not_show'].append({'zh': '哪个模型对、什么要紧：p 与 f 是给出的；更细的模型从哪里来属于学习。',
                               'en': 'Which model is right, or what matters: p and f are given; where a finer model '
                                     'comes from belongs to learning.',
                               'kind': 'scope'})
    related = [x for x in r['related'] if x['id'] != 'generalization-through-lumping']
    for x in related:
        if x['id'] == 'selection-through-registration':
            x['detail'] = pair('同一形式的律：经识的选择恰及所识（Web.selects_alike_iff），经模型的选择恰分开模型所分开者。',
                               'A law of the same form: selection through registration reaches exactly what registers '
                               '(Web.selects_alike_iff), and selection through a model separates exactly what the model '
                               'separates.')
    related.append({'id': 'generalization-through-lumping', 'detail': pair(
        '模型是一个归并：经它的选择只在要紧者经归并同去之处正确，与 lumped_right_iff 同形。',
        'The model is a lumping: a selection through it is right only where what matters goes alike across the '
        'lumping, the form of lumped_right_iff.')})
    r['related'] = related
    # References: refresh the hashes of the files this follow-up changed; every other one must still match.
    refs = []
    for x in r['references']:
        if x['role'] == 'receipt':
            continue
        if x['path'] in CHANGED:
            x['sha256'] = sha(x['path'])
        else:
            assert x['sha256'] == sha(x['path']), ('unexpected drift', x['path'])
        refs.append(x)
        if x['path'] == SELECTION:
            refs.append({'path': LEARNING, 'role': 'proof', 'sha256': sha(LEARNING), 'declarations': learning})
    refs.insert(next(i for i, x in enumerate(refs) if x['path'] == TIES) + 1,
                {'path': core, 'role': 'receipt', 'sha256': sha(core)})
    refs.insert(next(i for i, x in enumerate(refs) if x['path'] == core) + 1,
                {'path': instance, 'role': 'receipt', 'sha256': sha(instance)})
    refs.append({'path': SOURCE, 'role': 'provenance', 'sha256': sha(SOURCE)})
    r['references'] = refs
    r['proof_bindings'] = [binding(SELECTION, core, 'Becoming.Selection'), binding(LEARNING, core, 'Becoming.Learning'),
                           binding(INSTANCE, instance, 'SelectionRelabelCorrespondence'),
                           binding(PLURAL, instance, 'PluralRecords'), binding(TIES, instance, 'TieBreaking')]
    r['history'].append(pair(
        f'2026-10-16：依 Ren 的更正（“it is about the cognitive model, not just record”）与认可（“go ahead with the '
        f'reframing, first title, keep names, (a)”）重新框定：ID 由 {OLD} 改为 {NEW}（旧 ID 留作别名），标题“只读记录的选择”'
        f'改为“经选项模型的选择”；陈述、定律、假设与对应改称模型；“需另一被记录的关系，如到达的次序”一读撤回，next_delta '
        f'去掉 Ren 对读法的判断；加一条定律：Becoming.Learning 中连接模型与其归并的 8 项定理；Selection.lean 与 '
        f'SelectionRelabelCorrespondence.lean 只改注释。研究第{SECTION}节；原标题、陈述与读法见研究第151节。',
        f'16 October 2026: reframed at Ren\'s correction (“it is about the cognitive model, not just record”) and '
        f'approval (“go ahead with the reframing, first title, keep names, (a)”). The id {OLD} became {NEW}, the old id '
        f'kept as an alias; the title “Selection by the record alone” became “Selection through a model of the '
        f'options”; statement, laws, hypotheses and correspondence name the model; the reading that a further recorded '
        f'relation such as an order of arrival parts a tie is withdrawn, and Ren\'s judgment of the reading leaves '
        f'next_delta. A law adds Becoming.Learning\'s eight theorems linking the model to its lumping; Selection.lean '
        f'and SelectionRelabelCorrespondence.lean change only in comments. Study section {SECTION}; the former title, '
        f'statement and reading are in study section 151.'))
    for key, (en, zh) in CAPS.items():
        assert len(r[key]['en']) <= en and len(r[key]['zh']) <= zh, (key, len(r[key]['en']), len(r[key]['zh']))
    write(r, REC / f'{NEW}.json')


def rebound(core):
    stamp = core.split('/')[-2]
    others = []
    for path in sorted(REC.glob('*.json')):
        r = json.loads(path.read_text())
        if r['id'] in (OLD, NEW):
            continue
        cited = [x for x in r.get('references', []) if x['path'] in (SELECTION, LEARNING)]
        if not cited:
            continue
        for x in cited:
            assert set(x.get('declarations', [])) <= set(declared(x['path'])), (r['id'], x['path'])
            x['sha256'] = sha(x['path'])
            module = 'Becoming.Selection' if x['path'] == SELECTION else 'Becoming.Learning'
            move_receipt(r, x['path'], core, module)
        linked = ''
        for x in r.get('related', []):
            if x['id'] == OLD:
                x['id'] = NEW
                x['detail'] = pair('同一形式的律：经识的选择恰及所识，经模型的选择恰分开模型所分开者；模型使两个选项并列时，'
                                   '每个经模型的选择都选得相同。',
                                   'A law of the same form: selection through registration reaches exactly what '
                                   'registers, and selection through a model separates exactly what the model '
                                   'separates; where the model ties two options, every selection through it selects '
                                   'them alike.')
                linked = 'follows'
        if r['id'] == 'generalization-through-lumping' and not any(x['id'] == NEW for x in r.get('related', [])):
            r.setdefault('related', []).append({'id': NEW, 'detail': pair(
                '经选项模型的选择：模型是一个归并，经它的选择只在要紧者经归并同去之处正确。',
                'Selection through a model of the options: the model is a lumping, and a selection through it is right '
                'only where what matters goes alike across the lumping.')})
            linked = 'links'
        files = ' and '.join(sorted({Path(x['path']).name for x in cited}))
        r['history'].append(pair(
            f'2026-10-16，整合 I4b 第二项的后续（研究第{SECTION}节）：Selection.lean 只改注释（“只读记录的选择”一节改称“经选项'
            f'模型的选择”），Learning.lean 加一节，8 项定理连接选项的模型与其归并；本记录所引的声明不变。{files} 改用新哈希，'
            f'证明绑定移到核心回执 {stamp}'
            + {'': '。', 'follows': f'；关联改指新 ID {NEW}。', 'links': f'；关联新记录 {NEW}。'}[linked],
            f'16 October 2026, I4b item 2 follow-up (study section {SECTION}): Selection.lean changes only in comments '
            f'(the section “Selection by the record alone” renamed “Selection through a model of the options”), and '
            f'Learning.lean gains a section of eight theorems linking a model of the options to its lumping; the '
            f'declarations this record cites are unchanged. {files} take the new hashes, and the proof bindings move to '
            f'core receipt {stamp}'
            + {'': '.', 'follows': f'; the link follows the new id {NEW}.',
               'links': f'; the record {NEW} is linked.'}[linked]))
        write(r, path)
        others.append(r['id'])
    return others


def main():
    core = passed(CORE_POINTER, 'Becoming.Selection', SELECTION)
    assert core == passed(CORE_POINTER, 'Becoming.Learning', LEARNING)
    instance = passed(INSTANCE_POINTER, 'SelectionRelabelCorrespondence', INSTANCE)
    for module, source in [('PluralRecords', PLURAL), ('TieBreaking', TIES)]:
        assert passed(INSTANCE_POINTER, module, source) == instance
    if not DRY:
        checked = json.loads((ROOT / instance).read_text())
        assert checked['checked_here'] == ['PluralRecords', 'TieBreaking', 'SelectionRelabelCorrespondence']
        assert all(not v for m in checked['modules'] for v in m['axiom_dependencies'].values()), 'nonempty report'
        assert f'\n## {SECTION}. 经选项模型的选择' in (ROOT / STUDY).read_text(), 'insert the study section first'
    renamed(core, instance)
    print('rebound:', ', '.join(rebound(core)))


if __name__ == '__main__':
    main()
