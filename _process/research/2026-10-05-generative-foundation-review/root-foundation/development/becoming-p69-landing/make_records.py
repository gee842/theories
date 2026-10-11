#!/usr/bin/env python3
"""Write the P69 records into a checkout.

Usage: python3 -B make_records.py ROOT REVIEWED_AT_UTC S   (REVIEWED_AT_UTC as 2026-10-12T12:00:00+00:00)

S is the study section of P69, as for apply_docs.py. The text of the two new records is in
docs/records/<id>.json; this script adds what depends on the checkout: the receipts' stamps and
counts, reference hashes of ROOT's current bytes, and the history. Where the receipt's
Becoming.Bridge declares the bridge section (deeper_bisimulation_iff), configurations-alike-by-relation
gains its bridge sentence, the dependency on branching-tests-bisimulation and the bridge's references;
otherwise that record names branching-tests-bisimulation as related only. P69 advances no existing
record's next_delta. Rerun after any edit to a referenced file, after reading that edit.
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve()
REVIEWED = sys.argv[2]
assert REVIEWED.endswith('+00:00') and 'T' in REVIEWED, 'REVIEWED_AT_UTC as 2026-10-12T12:00:00+00:00'
SEC = str(int(sys.argv[3]))
L = 'experiments/integrated-correction/general-framework/generative-basis/lean'
D = f'{L}/becoming'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
RECEIPT = f'{D}/becoming-verification.json'
PERI_RECEIPT = f'{L}/universal-ethics/generative-capacity/correction-inquiry-verification.json'
STUDY = f'{RF}/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCES = ['sources/15-codex-theory-conversations/2026-10-12-relational-starting-point.md',
           'sources/15-codex-theory-conversations/2026-10-12-no-two-realities.md']
EVIDENCE = f'{RF}/development/becoming-p69-shape-evidence/Shape.lean'
FRAMING = f'{RF}/development/becoming-framing-evidence/Saying.lean'
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
assert 'Becoming.Unfolding' in MODULES, 'Becoming.Unfolding is not in the receipt'


def names(module):
    return [d['name'] if isinstance(d, dict) else d for d in MODULES[module]['declarations']]


OWNER = {n: m for m in MODULES for n in names(m)}
BRIDGE = 'Becoming.deeper_bisimulation_iff' in names('Becoming.Bridge')


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


# The likeness half of the module: its sections "Configurations alike in their relations" and "Standings alike".
LIKENESS = {n for n in names('Becoming.Unfolding')
            if n.startswith(('Becoming.Bisimulation', 'Becoming.Alike', 'Becoming.DeterminedAt', 'Becoming.Twins.',
                             'Becoming.MakesSense', 'Becoming.makesSense', 'Becoming.Law.'))
            or n in B('Determined.at', 'exchangeFrame', 'exchange_pointwise_bisimulation', 'exchange_alike_of_pointwise',
                      'exchange_pointwise_of_alike', 'exchange_alike_iff', 'exchange_determinedAt')}

# id: (theorems named in the validation scope, declarations of other modules it builds on, own part)
SPEC = {
    'process-and-frame-as-readings': (
        B('withMove_determined_iff', 'closedBy_runs_agree', 'Fork.label_couples', 'World.balances_iff_exchange',
          'exchange_runs_agree', 'exists_law_iff', 'Shown.runs_of_new', 'Splice.spliced', 'DeadEnd.no_history',
          'Frame.novel_iff_arises', 'Frame.world_fixes_run'),
        B('World', 'Flow.Balances', 'Flow.BalancesOn', 'Web.Arises', 'carries_law_iff', 'goAlike_id_iff',
          'GoAlike.runs_agree', 'keepHistory', 'keepHistory_new', 'Run.not_fixes_of_untaken', 'Determined',
          'ComesToBe', 'CeasesToBe', 'Recurs', 'coming_recurs_iff', 'Run', 'Novel', 'total', 'add_right_cancel'),
        lambda n: n not in LIKENESS),
    'configurations-alike-by-relation': (
        B('Alike.trans', 'Alike.tests', 'DeterminedAt.transfer', 'DeterminedAt.goAlike', 'Twins.alike_one',
          'makesSense_iff', 'MakesSense.carries', 'makesSense_id_iff', 'Law.alike_iff_sameFuture', 'Law.MakesSense.carries',
          'exchange_alike_iff', 'exchange_determinedAt'),
        B('Determined', 'Frame', 'Run', 'carries_law_iff', 'FactorsThrough', 'Law.orbit', 'Law.orbit_shift', 'Law.process'),
        lambda n: n in LIKENESS),
}

for record_id, (named, builds_on, _) in SPEC.items():
    for name in named:
        assert name in names('Becoming.Unfolding'), (record_id, name)
    missing = [n for n in builds_on if n not in OWNER]
    assert not missing, (record_id, missing)


def grouped(declarations):
    by = {}
    for n in declarations:
        by.setdefault(OWNER[n].removeprefix('Becoming.'), []).append(n)
    return by


def scope(record_id):
    named = SPEC[record_id][0]
    n_module = MODULES['Becoming.Unfolding']['theorems']
    short = [n.removeprefix('Becoming.') for n in named]
    zh_bridge = en_bridge = ''
    if BRIDGE and record_id == 'configurations-alike-by-relation':
        zh_bridge = ('同一回执中，外围桥接 Becoming.Bridge 的 deeper_bisimulation_iff、static_toggle_alike、'
                     'branching_bisimulation_iff 与 Alike.same 空依赖；')
        en_bridge = ('In the same receipt the periphery bridge Becoming.Bridge\'s deeper_bisimulation_iff, '
                     'static_toggle_alike, branching_bisimulation_iff and Alike.same have empty axiom reports. ')
    return zh_en(
        f'Lean 4.29.1 合并检查器成功实查（{RUN}）：Becoming.Unfolding 的 {n_module} 项定理全部空依赖，其中含 {"、".join(short[:-1])}'
        f'与 {short[-1]}；{zh_bridge}同一回执覆盖包内 {N_PKG} 个模块（含只作导入的根模块与桥接），共 {N_THM} 项定理／{N_DECL} 项声明审计，'
        f'{N_INH} 个继承模块的当前字节与已通过回执一致；外围回执 {PERI_RUN} 通过。检查器另核对核心纯净：核心（GenerativeCore、'
        'InquirySufficiency、RelationalRenewal、L1–L4 与根模块 Becoming）的导入闭包恰为这 '
        f'{N_CORE} 个模块，其中每条源声明的公理报告为空（Lean 生成的常量中，只有带字段构造子的单射引理 injEq 依赖 propext，没有源声明'
        '使用它们，检查器逐一列出），并且只用 Lean 内置前导即可编译（基础模块的 import Std 在该次编译中去掉）。'
        f'作者反审见整合文档 §{SEC}；尚无独立审查。',
        f'Successful Lean 4.29.1 consolidated check ({RUN}): the {n_module} theorems of Becoming.Unfolding all have empty '
        f'axiom reports, among them {", ".join(short[:-1])} and {short[-1]}. {en_bridge}The same receipt covers the package\'s '
        f'{N_PKG} modules (including the import-only root and the bridge) with {N_THM} theorems/{N_DECL} declaration '
        f'audits, and {N_INH} inherited modules whose current bytes match passed receipts; periphery receipt {PERI_RUN} '
        'passed. The checker also verifies core purity: the import closure of the core (GenerativeCore, '
        'InquirySufficiency, RelationalRenewal, L1–L4 and the root module Becoming) is exactly these '
        f'{N_CORE} modules, every source declaration in it has an empty axiom report (of the constants Lean generates, '
        'only the injectivity lemmas of constructors with fields, injEq, depend on propext; no source declaration uses '
        "them, and the checker lists them), and it compiles from Lean's prelude alone (the foundation's import Std "
        f'removed for that run). The author\'s counterreview is in §{SEC} of the integration note; there is no '
        'independent review yet.')


ORDER = ['schema_version', 'id', 'title', 'kind', 'status', 'family', 'reviewed_at_utc', 'claim', 'hypotheses',
         'correspondence', 'canonical_source', 'aliases', 'dependencies', 'related', 'counterexamples', 'limitations',
         'validation_scope', 'references', 'proof_bindings', 'next_delta', 'history']


def fill(value):
    if isinstance(value, str):
        return value.replace('{S}', SEC)
    if isinstance(value, list):
        return [fill(v) for v in value]
    if isinstance(value, dict):
        return {k: fill(v) for k, v in value.items()}
    return value


for record_id, (_, builds_on, own) in SPEC.items():
    draft = fill(json.loads((HERE / 'docs/records' / f'{record_id}.json').read_text()))
    assert draft['id'] == record_id
    bridge = draft.pop('bridge', None)
    by_module = grouped(builds_on)
    extra_refs, extra_bindings = [], []
    if bridge:
        if BRIDGE:
            missing = [n for n in bridge['declarations'] if n not in names('Becoming.Bridge')]
            assert not missing, missing
            for lang, end in (('zh', '不用 Lean 公理。'), ('en', 'No Lean axiom is used.')):
                assert draft['claim'][lang].endswith(end), lang
                draft['claim'][lang] = (draft['claim'][lang][:-len(end)] + bridge['claim'][lang]
                                        + ('' if lang == 'zh' else ' ') + end)
            draft['dependencies'].append(bridge['dependency'])
            extra_refs.append(ref(lean('Bridge'), 'proof', bridge['declarations']))
            extra_bindings.append(binding('Bridge'))
        else:
            draft['related'].append({'id': bridge['dependency']['id'], 'detail': zh_en(
                '外围的分支检验与互模拟；桥接一节没有落地，所以它与核心互模拟的等同没有陈述。',
                'The periphery\'s branching tests and bisimulation; the bridge section has not landed, so its '
                'identity with the core\'s bisimulation is not stated.')})
    own_names = [n for n in names('Becoming.Unfolding') if own(n)]
    record = {
        **draft,
        'schema_version': 1,
        'kind': 'theorem',
        'status': 'recorded-checked',
        'reviewed_at_utc': REVIEWED,
        'canonical_source': lean('Unfolding'),
        'validation_scope': scope(record_id),
        'references': [
            ref(lean('Unfolding'), 'proof', own_names),
            *[ref(lean(m), 'proof', ns) for m, ns in by_module.items()],
            *extra_refs,
            *[ref(path, 'proof') for path in sorted({d['interface']['evidence'] for d in draft['dependencies']})
              if path not in {lean('Unfolding'), *(lean(m) for m in by_module), lean('Bridge')}],
            ref(RECEIPT, 'receipt'),
            ref(STUDY, 'integration'),
            ref(CHAPTER, 'statement'),
            *[ref(path, 'provenance') for path in SOURCES],
            *([ref(EVIDENCE, 'provenance')] if record_id == 'process-and-frame-as-readings' else [ref(FRAMING, 'provenance')]),
        ],
        'proof_bindings': [binding('Unfolding'), *[binding(m) for m in by_module], *extra_bindings],
        'history': [zh_en(
            f'2026-10-12 P69：新增，按 Ren“yes, put it on the board and start”（对“is this dualistic?”的回答所附的提议）；'
            f'律与历史的读法经 Ren 确认（“yes, i do agree with your reading, there are no two realities”）；见整合文档 §{SEC}。',
            f'2026-10-12 P69: added, following Ren\'s ‘yes, put it on the board and start’ (to the proposal answering ‘is '
            f'this dualistic?’); the reading of law and history confirmed by Ren (‘yes, i do agree with your reading, '
            f'there are no two realities’); see §{SEC} of the integration note.')],
    }
    missing = [k for k in ORDER if k not in record]
    assert not missing, (record_id, missing)
    extra = [k for k in record if k not in ORDER]
    assert not extra, (record_id, extra)
    for d in record['dependencies'] + record['related']:
        assert d['id'] in SPEC or (RECORDS / f'{d["id"]}.json').exists(), (record_id, d['id'])
    record = {k: record[k] for k in ORDER}
    (RECORDS / f'{record_id}.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print('wrote', record_id, '(bridge)' if bridge and BRIDGE else '')
