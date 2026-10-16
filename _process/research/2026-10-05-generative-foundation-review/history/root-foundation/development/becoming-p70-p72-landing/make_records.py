#!/usr/bin/env python3
"""Write the P70–P72 records into a checkout.

Usage: python3 -B make_records.py ROOT REVIEWED_AT_UTC S   (REVIEWED_AT_UTC as 2026-10-12T12:00:00+00:00)

S is the study section of P70, as for apply_docs.py; P71 and P72 take S + 1 and S + 2. The text of
the four new records is in docs/records/<id>.json; this script adds what depends on the checkout: the
receipts' stamps and counts, reference hashes of ROOT's current bytes, and the history. Where the
receipt's Becoming.Description declares lasso_iff_sameAhead (P73 landed first and learning_patch.py
was applied), the-split-that-makes-sense states the identities with Becoming.Learning and names
P73's records as related; otherwise it leaves them to P73. P70–P72 advance no existing record's
next_delta. Rerun after any edit to a referenced file, after reading that edit.
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve()
REVIEWED = sys.argv[2]
assert REVIEWED.endswith('+00:00') and 'T' in REVIEWED, 'REVIEWED_AT_UTC as 2026-10-12T12:00:00+00:00'
S = int(sys.argv[3])
SECTION = {'Description': str(S), 'Diagonal': str(S + 1), 'Context': str(S + 2)}
L = 'experiments/integrated-correction/general-framework/generative-basis/lean'
D = f'{L}/becoming'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
RECEIPT = f'{D}/becoming-verification.json'
PERI_RECEIPT = f'{L}/universal-ethics/generative-capacity/correction-inquiry-verification.json'
STUDY = f'{RF}/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCES = ['sources/15-codex-theory-conversations/2026-10-12-framing-and-pairs.md']
EVIDENCE = f'{RF}/development/becoming-framing-evidence/README.md'
QUANTUM_EVIDENCE = f'{RF}/development/becoming-p72q-quantum/README.md'
RECORDS = ROOT / 'theories/becoming/results/records'


def lean(module):
    return f'{D}/Becoming/{module}.lean'


receipt = json.loads((ROOT / RECEIPT).read_text())
peri = json.loads((ROOT / PERI_RECEIPT).read_text())
assert receipt['status'] == peri['status'] == 'passed'
RUN, PERI_RUN = receipt['utc'], peri['utc']
MODULES = {m['module']: m for m in receipt['modules']}
spine = [m for m in receipt['modules'] if m['spine']]
N_THM = sum(m['theorems'] for m in spine)
N_DECL = sum(len(m['declarations']) for m in spine)
N_PKG = len(spine)
N_CORE = len(receipt['core_closure'])
N_INH = len(receipt['inherited_receipts'])
for module in ('Description', 'Diagonal', 'Context', 'Quantum'):
    assert f'Becoming.{module}' in MODULES, f'Becoming.{module} is not in the receipt'
    assert f'Becoming.{module}' in receipt['core_closure'], f'Becoming.{module} is not in the core'


def declared(full):
    return [d['name'] if isinstance(d, dict) else d for d in MODULES[full]['declarations']]


def names(module):
    return declared(f'Becoming.{module}')


OWNER = {n: m.removeprefix('Becoming.') for m in MODULES for n in declared(m)}


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def zh_en(zh, en):
    return {'zh': zh, 'en': en}


def ref(path, role, declarations=None):
    return {'path': path, 'role': role, 'sha256': sha(path), 'declarations': declarations or []}


def binding(module):
    return {'source': lean(module), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{module}',
            'success_pointer': '/status', 'success_value': 'passed'}


def B(*xs):
    return ['Becoming.' + x for x in xs]


# Description's first section, "Separation": the record separation-loses-the-relation; the rest of the
# module is the-split-that-makes-sense.
SEPARATION = set(B('Rectangular', 'Separated', 'separated_of_whole', 'separation_faithful_iff', 'separation_surplus',
                   'flipIf', 'EvenThree', 'whole_not_in_pairs', 'evenBoxes', 'flipIf_self', 'even_first', 'even_third',
                   'evenBoxes_glued', 'evenBoxes_not_determined', 'imageOf', 'Rectangular.image_of_separate',
                   'copy_relates', 'Rectangular.of_image_injective', 'relation_persists', 'forgetting_unrelates',
                   'couple', 'couple_couple', 'coupling_relates_and_unrelates'))
assert SEPARATION <= set(names('Description')), SEPARATION - set(names('Description'))

# id: (module of the record, theorems named in the validation scope, declarations of other modules it
# builds on, own part of its module, further modules of this landing wholly in the record)
SPEC = {
    'separation-loses-the-relation': (
        'Description',
        B('separation_faithful_iff', 'separation_surplus', 'whole_not_in_pairs', 'evenBoxes_glued',
          'evenBoxes_not_determined', 'Rectangular.image_of_separate', 'copy_relates', 'relation_persists',
          'forgetting_unrelates', 'coupling_relates_and_unrelates'),
        B('restrict', 'Glued', 'PartsDetermine', 'Specker.Box', 'Specker.within'),
        lambda n: n in SEPARATION, []),
    'the-split-that-makes-sense': (
        'Description',
        B('Law.kernel_bisimulation', 'Law.makesSense_of_law', 'Law.const_makesSense_iff', 'Law.now_makesSense_iff_goAlike',
          'Law.part_makesSense_iff_step', 'Law.adaptive_makesSense_iff', 'Motion.neither_alone',
          'Motion.still_makes_sense', 'alike_moments_iff', 'shared_below', 'finitely_many_states_iff',
          'Law.Returns.states', 'Denial.two_states'),
        B('Alike', 'Alike.refl', 'Bisimulation', 'MakesSense', 'makesSense_iff', 'makesSense_id_iff', 'Law.registered',
          'Law.SameFuture', 'Law.alike_iff_sameFuture', 'Law.MakesSense.carries', 'GoAlike', 'adaptive',
          'adaptive_state_law_iff', 'carries_law_iff', 'Law.orbit', 'Law.orbit_add', 'Law.succ_orbit', 'Law.process',
          'Law.Returns', 'skipAt', 'skipAt_le', 'skipAt_lt', 'skipAt_ne', 'le_succ_cases',
          'Diagonal.revision_never_rests', 'Diagonal.flip_moves'),
        lambda n: n not in SEPARATION, []),
    'registration-within-what-it-registers': (
        'Diagonal',
        B('Diagonal.gap_unsaid', 'Diagonal.fixed_of_complete', 'Diagonal.claims_incomplete', 'Frame.self_incomplete',
          'Diagonal.complete_iff_alike', 'Diagonal.Unfolds.incomplete', 'Diagonal.Unfolds.gaps_differ',
          'Diagonal.Unfolds.never_returns', 'Diagonal.Unfolds.unheld', 'Diagonal.unfolding_open',
          'Diagonal.revision_never_rests', 'Diagonal.denial_returns'),
        B('Frame', 'Law.orbit', 'Law.Returns', 'gap_of_lt'),
        lambda n: True, []),
    'contextual-registration': (
        'Context',
        B('Contextual.glues_iff_agree', 'Contextual.fitsFree_iff', 'Contextual.indexed_fits', 'Contextual.not_glues',
          'Contextual.no_free_frame', 'glued_of_whole', 'no_whole', 'Specker.noGlobal', 'Specker.not_glues',
          'Specker.no_whole', 'Square.noGlobal', 'Square.no_whole'),
        B('Frame'),
        lambda n: True, ['Quantum']),
}
LEARNING = 'Becoming.lasso_iff_sameAhead' in names('Description')
if LEARNING:
    split = SPEC['the-split-that-makes-sense']
    SPEC['the-split-that-makes-sense'] = (
        split[0], split[1] + B('lasso_iff_sameAhead', 'finitely_many_states_iff_lasso'),
        split[2] + B('Learning.goAlike_iff_lumped', 'Learning.Lasso'), split[3], split[4])

QUANTUM_NAMED = B('Square.obs_sq', 'Square.line_commute', 'Square.line_product', 'Square.line_parity',
                  'Square.shows_support', 'Square.support_shown', 'Square.no_context_free_values')
assert set(QUANTUM_NAMED) <= set(names('Quantum')), set(QUANTUM_NAMED) - set(names('Quantum'))

for record_id, (module, named, builds_on, own, _) in SPEC.items():
    for name in named:
        assert name in names(module), (record_id, name)
    missing = [n for n in builds_on if n not in OWNER]
    assert not missing, (record_id, missing)
    assert all(OWNER[n] != module for n in builds_on), record_id


def grouped(declarations):
    by = {}
    for n in declarations:
        by.setdefault(OWNER[n], []).append(n)
    return by


def scope(record_id):
    module, named, _, _, more = SPEC[record_id]
    n_module = MODULES[f'Becoming.{module}']['theorems']
    short = [n.removeprefix('Becoming.') for n in named]
    zh_more = en_more = ''
    if more:
        q = [n.removeprefix('Becoming.') for n in QUANTUM_NAMED]
        n_q = MODULES['Becoming.Quantum']['theorems']
        zh_more = f'Becoming.Quantum 的 {n_q} 项定理全部空依赖，其中含 {"、".join(q[:-1])}与 {q[-1]}；'
        en_more = f'the {n_q} theorems of Becoming.Quantum all have empty axiom reports, among them {", ".join(q[:-1])} and {q[-1]}. '
    sec = SECTION[module]
    return zh_en(
        f'Lean 4.29.1 合并检查器成功实查（{RUN}）：Becoming.{module} 的 {n_module} 项定理全部空依赖，其中含 {"、".join(short[:-1])}'
        f'与 {short[-1]}；{zh_more}同一回执覆盖包内 {N_PKG} 个模块（含只作导入的根模块与桥接），共 {N_THM} 项定理／{N_DECL} 项声明审计，'
        f'{N_INH} 个继承模块的当前字节与已通过回执一致；外围回执 {PERI_RUN} 通过。检查器另核对核心纯净：核心（GenerativeCore、'
        'InquirySufficiency、RelationalRenewal、L1–L4 与根模块 Becoming）的导入闭包恰为这 '
        f'{N_CORE} 个模块，其中每条源声明的公理报告为空（Lean 生成的常量中，只有带字段构造子的单射引理 injEq 依赖 propext，没有源声明'
        '使用它们，检查器逐一列出），并且只用 Lean 内置前导即可编译（基础模块的 import Std 在该次编译中去掉）。'
        f'作者反审见整合文档 §{sec}；独立审查的范围见同节。',
        f'Successful Lean 4.29.1 consolidated check ({RUN}): the {n_module} theorems of Becoming.{module} all have empty '
        f'axiom reports, among them {", ".join(short[:-1])} and {short[-1]}; {en_more}the same receipt covers the package\'s '
        f'{N_PKG} modules (including the import-only root and the bridge) with {N_THM} theorems/{N_DECL} declaration '
        f'audits, and {N_INH} inherited modules whose current bytes match passed receipts; periphery receipt {PERI_RUN} '
        'passed. The checker also verifies core purity: the import closure of the core (GenerativeCore, '
        'InquirySufficiency, RelationalRenewal, L1–L4 and the root module Becoming) is exactly these '
        f'{N_CORE} modules, every source declaration in it has an empty axiom report (of the constants Lean generates, '
        'only the injectivity lemmas of constructors with fields, injEq, depend on propext; no source declaration uses '
        "them, and the checker lists them), and it compiles from Lean's prelude alone (the foundation's import Std "
        f'removed for that run). The author\'s counterreview is in §{sec} of the integration note, with the scope of the '
        'independent review.')


ORDER = ['schema_version', 'id', 'title', 'kind', 'status', 'family', 'reviewed_at_utc', 'claim', 'hypotheses',
         'correspondence', 'canonical_source', 'aliases', 'dependencies', 'related', 'counterexamples', 'limitations',
         'validation_scope', 'references', 'proof_bindings', 'next_delta', 'history']


def fill(value, sec):
    if isinstance(value, str):
        return value.replace('{S}', sec)
    if isinstance(value, list):
        return [fill(v, sec) for v in value]
    if isinstance(value, dict):
        return {k: fill(v, sec) for k, v in value.items()}
    return value


for record_id, (module, _, builds_on, own, more) in SPEC.items():
    sec = SECTION[module]
    draft = fill(json.loads((HERE / 'docs/records' / f'{record_id}.json').read_text()), sec)
    assert draft['id'] == record_id
    if record_id == 'the-split-that-makes-sense':
        old_zh = '与 P73 的 Lasso（Learning.Lasso o i q 即 SameAhead o i (i + q + 1)）由后落地者给出实例定理。'
        old_en = ("The instance theorem to P73's Lasso (Learning.Lasso o i q is SameAhead o i (i + q + 1)) goes to "
                  "whichever lands second.")
        assert old_zh in draft['correspondence']['zh'] and old_en in draft['correspondence']['en']
        if LEARNING:
            new_zh = ('P73 先落地，所以这里写出同一：Law.goAlike_process_iff 是 Becoming.Learning 的 goAlike_iff_lumped 的实例'
                      '（两者各自写成，证明相同），状态有限就是 P73 的 Lasso。')
            new_en = ("P73 landed first, so the identities are stated here: Law.goAlike_process_iff is the instance of "
                      "Becoming.Learning's goAlike_iff_lumped (written independently, with the same proof), and finitely many "
                      "states is P73's lasso.")
            for lang, add in (('zh', 'Law.goAlike_process_iff 是 Becoming.Learning 的 goAlike_iff_lumped 的实例；'
                                     'Learning.Lasso o i q 恰当 SameAhead o i (i + (q + 1))（lasso_iff_sameAhead），'
                                     '所以状态有限恰当有 Lasso（finitely_many_states_iff_lasso）。'),
                              ('en', "Law.goAlike_process_iff is the instance of Becoming.Learning's goAlike_iff_lumped; "
                                     'Learning.Lasso o i q holds exactly where SameAhead o i (i + (q + 1)) '
                                     '(lasso_iff_sameAhead), so there are finitely many states exactly where there is a '
                                     'lasso (finitely_many_states_iff_lasso).')):
                end = '不用 Lean 公理。' if lang == 'zh' else 'No Lean axiom is used.'
                assert draft['claim'][lang].endswith(end), lang
                draft['claim'][lang] = draft['claim'][lang][:-len(end)] + add + ('' if lang == 'zh' else ' ') + end
            draft['aliases'] += B('lasso_iff_sameAhead', 'finitely_many_states_iff_lasso')
            for lang, old in (('zh', '与 P73 Lasso 的实例定理；'), ('en', "the instance theorem to P73's Lasso; ")):
                assert old in draft['next_delta'][lang], lang
                draft['next_delta'][lang] = draft['next_delta'][lang].replace(old, '')
            draft['related'] += [
                {'id': 'generalization-through-lumping', 'detail': zh_en(
                    'Law.goAlike_process_iff 是其 goAlike_iff_lumped 的实例。',
                    'Law.goAlike_process_iff is the instance of its goAlike_iff_lumped.')},
                {'id': 'learning-by-refutation', 'detail': zh_en(
                    '它的 Lasso 就是两个时刻是同一状态（lasso_iff_sameAhead）。',
                    'Its Lasso is two moments being one state (lasso_iff_sameAhead).')}]
        else:
            new_zh = ('与 P73 的 Lasso 的实例定理（Learning.Lasso o i q 即 SameAhead o i (i + (q + 1))）由 P73 写出；它的 '
                      'goAlike_iff_lumped 与 Law.goAlike_process_iff 是同一定律，各自写成。')
            new_en = ("The instance theorem to P73's Lasso (Learning.Lasso o i q is SameAhead o i (i + (q + 1))) is P73's to "
                      'write; its goAlike_iff_lumped and Law.goAlike_process_iff are one law, written independently.')
        draft['correspondence']['zh'] = draft['correspondence']['zh'].replace(old_zh, new_zh)
        draft['correspondence']['en'] = draft['correspondence']['en'].replace(old_en, new_en)
    if record_id == 'registration-within-what-it-registers' and LEARNING:
        draft['related'].append({'id': 'learning-by-refutation', 'detail': zh_en(
            '它的 diagonal_refutes 与 diagonal_unrested 是学习者的形式，与 gap_unsaid、revision_never_rests 同形而对象不同，各自写成。',
            "Its diagonal_refutes and diagonal_unrested are the learner's form, of the same form as gap_unsaid and "
            'revision_never_rests and a different object, written independently.')})
    by_module = grouped(builds_on)
    own_names = [n for n in names(module) if own(n)]
    proof_paths = {lean(module), *(lean(m) for m in more), *(lean(m) for m in by_module)}
    record = {
        **draft,
        'schema_version': 1,
        'kind': 'theorem',
        'status': 'recorded-checked',
        'reviewed_at_utc': REVIEWED,
        'canonical_source': lean(module),
        'validation_scope': scope(record_id),
        'references': [
            ref(lean(module), 'proof', own_names),
            *[ref(lean(m), 'proof', names(m)) for m in more],
            *[ref(lean(m), 'proof', ns) for m, ns in by_module.items()],
            *[ref(path, 'proof') for path in sorted({d['interface']['evidence'] for d in draft['dependencies']})
              if path not in proof_paths],
            ref(RECEIPT, 'receipt'),
            ref(STUDY, 'integration'),
            ref(CHAPTER, 'statement'),
            *[ref(path, 'provenance') for path in SOURCES],
            ref(EVIDENCE, 'provenance'),
            *([ref(QUANTUM_EVIDENCE, 'provenance')] if more else []),
        ],
        'proof_bindings': [binding(module), *[binding(m) for m in more], *[binding(m) for m in by_module]],
        'history': [zh_en(
            f'2026-10-12 {"P72、P72q" if more else {"Description": "P70", "Diagonal": "P71"}[module]}：新增，按 Ren'
            f'“push the frontier, as far as possible”（对框架失去什么、什么使一对成为一对的回答之后），'
            f'及其后“keep prove to the deepest, i agree with your last reply”；见整合文档 §{sec}。',
            f'2026-10-12 {"P72 and P72q" if more else {"Description": "P70", "Diagonal": "P71"}[module]}: added, following '
            f'Ren\'s ‘push the frontier, as far as possible’ (after the answer on what the framing loses and what makes a '
            f'pair a pair) and the later ‘keep prove to the deepest, i agree with your last reply’; see §{sec} of the '
            f'integration note.')],
    }
    missing = [k for k in ORDER if k not in record]
    assert not missing, (record_id, missing)
    extra = [k for k in record if k not in ORDER]
    assert not extra, (record_id, extra)
    for d in record['dependencies'] + record['related']:
        assert d['id'] in SPEC or (RECORDS / f'{d["id"]}.json').exists(), (record_id, d['id'])
    record = {k: record[k] for k in ORDER}
    (RECORDS / f'{record_id}.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print('wrote', record_id)
