#!/usr/bin/env python3
"""Write the P73–P75 records into a checkout, and the history entries of the records they advance.

Usage: python3 -B make_records.py ROOT REVIEWED_AT_UTC S   (REVIEWED_AT_UTC as 2026-10-12T12:00:00+00:00)

S is the first of the two study sections, as for apply_docs.py: S for P73 with P74 (learning), S+1 for
P75 (the root of wisdom). The text of the three new records is in docs/records/<id>.json; this script
adds what depends on the checkout: the receipts' stamps and counts, reference hashes of ROOT's current
bytes, and the history. Two records are theorems bound to the consolidated receipt (and, for the
periphery instances, the learning-bridge receipt); wisdom-root-part-one is an argument, reviewed-scoped
on the author's counterreview, with every module it cites bound to its receipt. Each advanced record
gets one history entry, a revised next_delta and its listed replacements; its current next_delta and
each replaced passage must be the ones read when this package was written, or the script stops so
the change can be read and reconciled. Rerun after any edit to a referenced file, after reading that
edit; a rerun does not repeat a history entry.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve()
REVIEWED = sys.argv[2]
assert REVIEWED.endswith('+00:00') and 'T' in REVIEWED, 'REVIEWED_AT_UTC as 2026-10-12T12:00:00+00:00'
S_LEARNING, S_WISDOM = (str(int(sys.argv[3]) + i) for i in range(2))
L = 'experiments/integrated-correction/general-framework/generative-basis/lean'
D = f'{L}/becoming'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
RECEIPT = f'{D}/becoming-verification.json'
BRIDGE_SOURCE = f'{L}/universal-ethics/evolution-connectionism/LearningCorrespondence.lean'
BRIDGE_RECEIPT = f'{L}/universal-ethics/evolution-connectionism/learning-correspondence-verification.json'
STUDY = f'{RF}/BECOMING-RENEWAL-READING.md'
WISDOM_STUDY = f'{RF}/CORE-CONSTRAINT-AND-WISDOM.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-12-learning-wisdom-root-and-induction.md'
RECORDS = ROOT / 'theories/becoming/results/records'


def lean(module):
    return f'{D}/Becoming/{module}.lean'


receipt = json.loads((ROOT / RECEIPT).read_text())
bridge = json.loads((ROOT / BRIDGE_RECEIPT).read_text())
assert receipt['status'] == bridge['status'] == 'passed'
RUN, BRIDGE_RUN = receipt['utc'], bridge['utc']
MODULES = {m['module']: m for m in receipt['modules']}
assert 'Becoming.Learning' in MODULES, 'Becoming.Learning is not in the receipt'
spine = [m for m in receipt['modules'] if m['spine']]
N_THM = sum(m['theorems'] for m in spine)
N_DECL = sum(len(m['declarations']) for m in spine)
N_PKG = len(spine)
N_CORE = len(receipt['core_closure'])
N_INH = len(receipt['inherited_receipts'])
N_LEARNING = MODULES['Becoming.Learning']['theorems']
BM = bridge['modules'][0]
assert BM['module'] == 'LearningCorrespondence'
N_BRIDGE, N_BRIDGE_DECL = BM['theorems'], len(BM['declarations'])
BRIDGE_EMPTY = sorted(n for n, v in BM['axiom_dependencies'].items() if not v)
assert all(set(v) <= {'propext', 'Classical.choice', 'Quot.sound'} for v in BM['axiom_dependencies'].values())


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def zh_en(zh, en):
    return {'zh': zh, 'en': en}


def ref(path, role, declarations=None):
    return {'path': path, 'role': role, 'sha256': sha(path), 'declarations': declarations or []}


def binding(module):
    return {'source': lean(module), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{module}',
            'success_pointer': '/status', 'success_value': 'passed'}


BRIDGE_BINDING = {'source': BRIDGE_SOURCE, 'receipt': BRIDGE_RECEIPT, 'sha256_pointer': '/source_sha256/LearningCorrespondence',
                  'success_pointer': '/status', 'success_value': 'passed'}


def B(*names):
    return ['Becoming.' + n for n in names]


def P(*names):
    return ['Becoming.LearningCorrespondence.' + n for n in names]


def declarations(module):
    """The declarations the receipt lists for a module, instances left out (references name only those
    the registry can find by keyword)."""
    entries = BM['declarations'] if module == 'LearningCorrespondence' else MODULES[f'Becoming.{module}']['declarations']
    return [d['name'] for d in entries if d['kind'] != 'instance']


LEARNING = declarations('Learning')
# The generalization part of Becoming.Learning starts at Determines; Alternate, the witness of learning by
# refutation, is at the end of the module.
START = LEARNING.index('Becoming.Learning.Determines')
GENERALIZATION = [n for n in LEARNING[START:] if not n.startswith('Becoming.Learning.Alternate.')]
REFUTATION = [n for n in LEARNING if n not in GENERALIZATION]

# id: (section, own module references as (module, declarations), theorems named in the validation scope,
#      references to the modules it builds on as (module, declarations))
SPEC = {
    'learning-by-refutation': (
        S_LEARNING,
        [('Learning', REFUTATION)],
        B('Learning.no_record_fixes_next', 'Learning.claim_refuted_on_one', 'Learning.diagonal_refutes',
          'Learning.diagonal_open', 'Learning.index_le_of_holds', 'Learning.refutations_not_recurring',
          'Learning.held_learner_bounded', 'Learning.held_rest_unrefuted', 'Learning.merged_unrested'),
        [('Recurrence', B('Law.orbit', 'Law.orbit_add', 'revisits_within')),
         ('Testing', B('Web.tail_unrefuted'))]),
    'generalization-through-lumping': (
        S_LEARNING,
        [('Learning', GENERALIZATION), ('LearningCorrespondence', declarations('LearningCorrespondence'))],
        B('Learning.determines_lumped_iff', 'Learning.lumped_right_iff', 'Learning.every_determines_nothing',
          'Learning.goAlike_iff_lumped', 'Learning.transfer_right_iff', 'Learning.Training.loss_through',
          'Learning.Training.fit_right_iff'),
        [('Mechanism', B('GoAlike', 'carries_law_iff')),
         ('Selection', B('Web.SelectsThrough')),
         ('Recurrence', B('Law.process'))]),
}

# The modules wisdom-root-part-one cites, with the declarations it names.
WISDOM = [
    ('Testing', B('Web.Refutes.not_of_alike', 'Web.tail_unrefuted', 'Web.refutesWithin_iff_conjunction',
                  'Clearing.tested_by_dweller', 'Clearing.pooled', 'Web.belief_judge_iff')),
    ('Inquiry', B('commonResponse_judge_iff')),
    ('Experiment', B('Run.not_fixes_of_untaken', 'Run.fixes_on_return', 'Run.generalizes')),
    ('Selection', B('Web.selects_alike_iff', 'Flow.unselected_beyond_registration', 'Clearing.selected_pooled',
                    'Diversion.favours')),
    ('Seeking', B('Law.rests_iff', 'more_needs_open', 'Law.aboveAll_never_rests')),
    ('Runaway', B('Web.break_not_bounded', 'Web.observed_raise_registers')),
    ('Mechanism', B('carries_law_iff', 'adaptive_state_law_iff')),
    ('Learning', B('Learning.no_record_fixes_next', 'Learning.every_determines_nothing',
                   'Learning.determines_lumped_iff', 'Learning.lumped_right_iff', 'Learning.goAlike_iff_lumped',
                   'Learning.held_learner_bounded', 'Learning.held_rest_unrefuted', 'Learning.no_record_fixes_next_finite',
                   'Learning.diagonal_refutes', 'Learning.diagonal_open', 'Learning.Training.loss_through',
                   'Learning.Training.unselected_beyond_data', 'Learning.merged_bound', 'Learning.merged_unrested')),
    ('LearningCorrespondence', P('uniform_determines', 'hebbian_activity_law_iff', 'updating_network_law_iff',
                                 'responsive_learns')),
]


def source(module):
    return BRIDGE_SOURCE if module == 'LearningCorrespondence' else lean(module)


def bind(module):
    return BRIDGE_BINDING if module == 'LearningCorrespondence' else binding(module)


for record_id, (_, own, named, builds_on) in SPEC.items():
    assert all(n in LEARNING for n in named), (record_id, [n for n in named if n not in LEARNING])
    for module, names in builds_on:
        missing = [n for n in names if n not in declarations(module)]
        assert not missing, (record_id, module, missing)
for module, names in WISDOM:
    missing = [n for n in names if n not in declarations(module)]
    assert not missing, ('wisdom-root-part-one', module, missing)


def short(names):
    return [n.removeprefix('Becoming.').removeprefix('Learning.').removeprefix('LearningCorrespondence.') for n in names]


def core_scope(named):
    s = short(named)
    return (
        f'Lean 4.29.1 合并检查器成功实查（{RUN}）：Becoming.Learning 的 {N_LEARNING} 项定理全部空依赖，其中含 {"、".join(s[:-1])}'
        f'与 {s[-1]}；同一回执覆盖包内 {N_PKG} 个模块（含只作导入的根模块与桥接），共 {N_THM} 项定理／{N_DECL} 项声明审计，'
        f'{N_INH} 个继承模块的当前字节与已通过回执一致。检查器另核对核心纯净：核心（GenerativeCore、InquirySufficiency、'
        f'RelationalRenewal、L1–L4 与根模块 Becoming）的导入闭包恰为这 {N_CORE} 个模块，其中每条源声明的公理报告为空（Lean 生成'
        '的常量中，只有带字段构造子的单射引理 injEq 依赖 propext，没有源声明使用它们，检查器逐一列出），并且只用 Lean 内置前导即可'
        '编译（基础模块的 import Std 在该次编译中去掉）。',
        f'Successful Lean 4.29.1 consolidated check ({RUN}): the {N_LEARNING} theorems of Becoming.Learning all have empty '
        f'axiom reports, among them {", ".join(s[:-1])} and {s[-1]}; the same receipt covers the package\'s {N_PKG} '
        f'modules (including the import-only root and the bridge) with {N_THM} theorems/{N_DECL} declaration audits, and '
        f'{N_INH} inherited modules whose current bytes match passed receipts. The checker also verifies core purity: the '
        'import closure of the core (GenerativeCore, InquirySufficiency, RelationalRenewal, L1–L4 and the root module '
        f'Becoming) is exactly these {N_CORE} modules, every source declaration in it has an empty axiom report (of the '
        'constants Lean generates, only the injectivity lemmas of constructors with fields, injEq, depend on propext; no '
        "source declaration uses them, and the checker lists them), and it compiles from Lean's prelude alone (the "
        "foundation's import Std removed for that run).")


BRIDGE_SCOPE = (
    f'外围学习桥接以 Lean 4.30.0-rc2 与 Mathlib ea11ccc0 成功实查（{BRIDGE_RUN}）：LearningCorrespondence 的 {N_BRIDGE} 项定理／'
    f'{N_BRIDGE_DECL} 项声明审计，其中习得部分 {len(BRIDGE_EMPTY)} 项声明公理报告为空，其余只报告 Mathlib 的标准公理（propext、'
    'Classical.choice、Quot.sound）；导入闭包中的每个其他模块与已通过回执一致；核心不导入它。',
    f'Successful periphery learning-bridge check with Lean 4.30.0-rc2 and Mathlib ea11ccc0 ({BRIDGE_RUN}): the '
    f'{N_BRIDGE} theorems/{N_BRIDGE_DECL} declaration audits of LearningCorrespondence, the {len(BRIDGE_EMPTY)} '
    "acquisition declarations with empty axiom reports and the rest reporting only Mathlib's standard axioms (propext, "
    'Classical.choice, Quot.sound); every other module in its import closure matches a passed receipt; the core does not '
    'import it.')


def scope(record_id):
    sec, own, named, _ = SPEC[record_id]
    zh, en = core_scope(named)
    if any(m == 'LearningCorrespondence' for m, _ in own):
        zh, en = zh + BRIDGE_SCOPE[0], en + ' ' + BRIDGE_SCOPE[1]
    return zh_en(zh + f'作者反审见整合文档 §{sec}；尚无独立审查。',
                 en + f' The author\'s counterreview is in §{sec} of the integration note; there is no independent review yet.')


ORDER = ['schema_version', 'id', 'title', 'kind', 'status', 'family', 'reviewed_at_utc', 'claim', 'hypotheses',
         'correspondence', 'canonical_source', 'aliases', 'dependencies', 'related', 'counterexamples', 'limitations',
         'validation_scope', 'references', 'proof_bindings', 'next_delta', 'history']
HISTORY = {
    'P73': zh_en(
        '2026-10-12 P73、P74：新增，按 Ren“please, fully complete, 我觉得理更像是对结构和变化的规律的建模 finish wisdom root, and '
        f'resolve the undissolved”；来自 AI 对元层次、神经网络、认知与学习之完整性的回答与三步提议（工作板 P73、P74）；见整合文档 §{S_LEARNING}。',
        '2026-10-12 P73, P74: added, following Ren\'s ‘please, fully complete, 我觉得理更像是对结构和变化的规律的建模 finish wisdom root, '
        'and resolve the undissolved’; from the AI\'s answer on how complete the account of the meta level, networks, '
        f'cognition and learning is, and its three proposed steps (work board P73, P74); see §{S_LEARNING} of the integration note.'),
    'P75': zh_en(
        '2026-10-12 P75：新增，按 Ren“finish wisdom root”（同一消息）；把第一部分已检查的规律逐条对到目标 wisdom-root 的四条连接，不新增 '
        f'Lean（工作板 P75）；见整合文档 §{S_WISDOM}。',
        '2026-10-12 P75: added, following Ren\'s ‘finish wisdom root’ (same message); matches Part I\'s checked laws to the '
        f'four connections of the target wisdom-root, adding no Lean (work board P75); see §{S_WISDOM} of the integration note.'),
}


def fill(value):
    if isinstance(value, str):
        return value.replace('{S_LEARNING}', S_LEARNING).replace('{S_WISDOM}', S_WISDOM)
    if isinstance(value, list):
        return [fill(v) for v in value]
    if isinstance(value, dict):
        return {k: fill(v) for k, v in value.items()}
    return value


def draft(record_id):
    d = fill(json.loads((HERE / 'docs/records' / f'{record_id}.json').read_text()))
    assert d['id'] == record_id
    left = re.findall(r'\{[A-Z_]+\}', json.dumps(d, ensure_ascii=False))
    assert not left, (record_id, left)
    return d


def write(record):
    missing = [k for k in ORDER if k not in record]
    assert not missing, (record['id'], missing)
    extra = [k for k in record if k not in ORDER]
    assert not extra, (record['id'], extra)
    for d in record['dependencies'] + record['related']:
        assert d['id'] in NEW or (RECORDS / f'{d["id"]}.json').exists(), (record['id'], d['id'])
    paths = [r['path'] for r in record['references']]
    assert len(paths) == len(set(paths)), (record['id'], paths)
    assert record['canonical_source'] in paths, record['id']
    record = {k: record[k] for k in ORDER}
    (RECORDS / f'{record["id"]}.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print('wrote', record['id'])


NEW = [*SPEC, 'wisdom-root-part-one']

for record_id, (sec, own, named, builds_on) in SPEC.items():
    d = draft(record_id)
    own_paths = {source(m) for m, _ in own}
    built = {lean(m) for m, _ in builds_on}
    write({
        **d,
        'schema_version': 1,
        'kind': 'theorem',
        'status': 'recorded-checked',
        'reviewed_at_utc': REVIEWED,
        'canonical_source': lean('Learning'),
        'validation_scope': scope(record_id),
        'references': [
            *[ref(source(m), 'proof', names) for m, names in own],
            *[ref(lean(m), 'proof', names) for m, names in builds_on],
            *[ref(path, 'proof') for path in sorted({e['interface']['evidence'] for e in d['dependencies']})
              if path not in own_paths | built],
            ref(RECEIPT, 'receipt'),
            *([ref(BRIDGE_RECEIPT, 'receipt')] if BRIDGE_SOURCE in own_paths else []),
            ref(STUDY, 'integration'),
            ref(CHAPTER, 'statement'),
            ref(SOURCE, 'provenance'),
        ],
        'proof_bindings': [*[bind(m) for m, _ in own], *[binding(m) for m, _ in builds_on]],
        'history': [HISTORY['P73']],
    })

d = draft('wisdom-root-part-one')
cited = {source(m) for m, _ in WISDOM}
write({
    **d,
    'schema_version': 1,
    'kind': 'argument',
    'status': 'reviewed-scoped',
    'reviewed_at_utc': REVIEWED,
    'canonical_source': STUDY,
    'validation_scope': zh_en(
        f'作者反审见整合文档 §{S_WISDOM}（本记录的 review 引用即该文档）；尚无独立审查。本记录不新增 Lean：它所引的每条定理都在其模块的已通过'
        f'回执中（合并检查器 {RUN}，Lean 4.29.1，公理报告为空；外围学习桥接 {BRIDGE_RUN}，Lean 4.30.0-rc2 与 Mathlib，习得部分报告为空，'
        '网络部分只报告 Mathlib 的标准公理），每个模块以源哈希绑定其回执。被核对的是这些定理的陈述与它们对目标 wisdom-root 四条连接的'
        '对照；对照本身（哪条规律构成智慧的哪一面）是论证，不是定理，理依 Ren，其余读法是 AI 的，待 Ren。',
        f'The author\'s counterreview is in §{S_WISDOM} of the integration note (the review reference of this record); there '
        f'is no independent review yet. This record adds no Lean: every theorem it cites is in its module\'s passed receipt '
        f'(consolidated checker {RUN}, Lean 4.29.1, empty axiom reports; periphery learning bridge {BRIDGE_RUN}, Lean '
        "4.30.0-rc2 and Mathlib, the acquisition part with empty reports and the network part reporting only Mathlib's "
        'standard axioms), each module bound to its receipt by source hash. What is checked is the statements of these '
        'theorems and their matching to the four connections of the target wisdom-root; the matching itself (which law '
        'constitutes which aspect of wisdom) is an argument, not a theorem; 理 is read as Ren reads it, the other readings '
        'are the AI\'s, pending Ren.'),
    'references': [
        ref(STUDY, 'review'),
        ref(CHAPTER, 'statement'),
        *[ref(source(m), 'proof', names) for m, names in WISDOM],
        *[ref(path, 'proof') for path in sorted({e['interface']['evidence'] for e in d['dependencies']}) if path not in cited],
        ref(RECEIPT, 'receipt'),
        ref(BRIDGE_RECEIPT, 'receipt'),
        ref(WISDOM_STUDY, 'integration'),
        ref(SOURCE, 'provenance'),
    ],
    'proof_bindings': [bind(m) for m, _ in WISDOM],
    'history': [HISTORY['P75']],
})


# The records these results advance, each with its next_delta as read and the revised next_delta (both null
# for a history entry alone), passages to replace as [field, language, read, revised], related records to
# add, and the history entry (section placeholders {S_LEARNING}, {S_WISDOM}).
ADVANCES = json.loads((HERE / 'docs/advances.json').read_text())
for item in ADVANCES:
    path = RECORDS / f'{item["id"]}.json'
    record = json.loads(path.read_text())
    entry = fill(item['history'])
    if entry in record['history']:
        print('already advanced', item['id'])
        continue
    if item.get('next_delta_read') is not None:
        if record['next_delta'] != item['next_delta_read']:
            sys.exit(f'{item["id"]}: next_delta changed since this package was written; read and reconcile it first')
        record['next_delta'] = fill(item['next_delta'])
    for field, lang, read, revised in item.get('replace', []):
        if record[field][lang].count(read) != 1:
            sys.exit(f'{item["id"]}: {field}.{lang} changed since this package was written; read and reconcile it first')
        record[field][lang] = record[field][lang].replace(read, fill(revised))
    for edge in item.get('add_related', []):
        if all(r['id'] != edge['id'] for r in record['related']):
            record['related'].append(fill(edge))
    record['history'].append(entry)
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print('advanced', item['id'])
