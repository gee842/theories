#!/usr/bin/env python3
"""Write the P62 record (seeking-boundary) into a checkout.

Usage: python3 -B make_records.py ROOT REVIEWED_AT_UTC SECTION P49_SECTION

Reference hashes are the current bytes of ROOT; the receipts' stamps and counts are read from
them. Rerun after any edit to a referenced file, after reading that edit.
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
REVIEWED, SEC, P49SEC = sys.argv[2:5]
L = 'experiments/integrated-correction/general-framework/generative-basis/lean'
D = f'{L}/becoming'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
SEEKING = f'{D}/Becoming/Seeking.lean'
LOCALITY = f'{D}/Becoming/Locality.lean'
RECURRENCE = f'{D}/Becoming/Recurrence.lean'
PLANW = f'{RF}/WUMING-BOUNDARY-PLAN.md'
SOURCE10 = 'sources/15-codex-theory-conversations/2026-10-10-truth-exists-opening.md'
RECEIPT = f'{D}/becoming-verification.json'
PERI_RECEIPT = f'{L}/universal-ethics/generative-capacity/correction-inquiry-verification.json'
STUDY = f'{RF}/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-11-wisdom-from-registration.md'

receipt = json.loads((ROOT / RECEIPT).read_text())
peri = json.loads((ROOT / PERI_RECEIPT).read_text())
assert receipt['status'] == peri['status'] == 'passed'
RUN, PERI_RUN = receipt['utc'], peri['utc']
spine = [m for m in receipt['modules'] if m['spine']]
N_MODULE = next(m for m in receipt['modules'] if m['module'] == 'Becoming.Seeking')['theorems']
N_THM = sum(m['theorems'] for m in spine)
N_DECL = sum(len(m['declarations']) for m in spine)
N_PKG = len(spine)
N_CORE = len(receipt['core_closure'])
N_INH = len(receipt['inherited_receipts'])


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def zh_en(zh, en):
    return {'zh': zh, 'en': en}


def ref(path, role, declarations=None):
    return {'path': path, 'role': role, 'sha256': sha(path), 'declarations': declarations or []}


def binding(path, module):
    return {'source': path, 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/{module}',
            'success_pointer': '/status', 'success_value': 'passed'}


def dep(ident, detail, output, inp, conditions, evidence):
    return {'id': ident, 'relation': 'formal-reuse', 'detail': detail,
            'interface': {'output': output, 'input': inp, 'conditions': conditions, 'evidence': evidence}}


def related(ident, detail):
    return {'id': ident, 'detail': detail}


def B(*names):
    return ['Becoming.' + n for n in names]


DECLS = B('MoreThanNow', 'RestsAt', 'more_not_at_rest', 'more_rises', 'more_new', 'more_needs_open', 'succ_more',
          'AboveAll', 'aboveAll_unique', 'aboveAll_not_two', 'Law.fixed_rests', 'Law.rests_iff', 'Law.more_never_rests',
          'Law.aboveAll_never_rests', 'Flow.more_needs_unrun', 'Flow.more_exhausted')

record = {
    'schema_version': 1,
    'id': 'seeking-boundary',
    'title': zh_en(
        '无明的边界条件：寻求恰在目标于展开所不变的状态被满足之处静止；“比现在更多”需要开放的世界，“高于一切他者”不同时满足两个；不断上升需要'
        '不衰减的步，衰减不断则上升停止',
        'The boundary condition for 无明: seeking rests exactly where its target is met at a state the unfolding leaves '
        'unchanged; more than now needs an open world and above all others never holds of two; rising without end needs '
        'steps that do not run down, and running down stops it'),
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': 'F04',
    'reviewed_at_utc': REVIEWED,
    'claim': zh_en(
        '在确定的律 next 之下，从 s 出发的轨道从某步起带着满足的目标静止，恰当它到达一个 next 不变、满足目标的状态（Law.rests_iff）；'
        '在这样的状态满足的目标此后每步都满足（Law.fixed_rests）。“比现在更多”，即自身的一个量 q 跨过一步上升（MoreThanNow），只由变化满足'
        '（more_not_at_rest、Law.more_never_rests）；每步都满足时任意两个较晚的步之间 q 都上升（more_rises），所以每个配置都是新的'
        '（more_new），没有列表容纳它们（more_needs_open，unlisted_of_new 的实例）；往上数满足它（succ_more）。“高于一切他者”，即其他每个'
        '寻求者的量都低于自己的（AboveAll），在一个状态至多被一个寻求者满足（aboveAll_unique、aboveAll_not_two），所以在任何律之下，没有'
        '律所不变的状态对两个寻求者都满足它（Law.aboveAll_never_rests）。所立者每步被列出（Web.StandingCensus）时，在任意晚处上升的条件，'
        '需要在任意晚处有所立者不衰减的步（Flow.more_needs_unrun，由 Flow.change_recurs_iff）；所立者从某步起每步衰减时，没有条件在任意晚处'
        '上升（Flow.more_exhausted）。不用 Lean 公理。',
        'Under a determined law next, the orbit from s comes to rest with its target met from some step on exactly when it '
        'reaches a state next leaves unchanged that meets the target (Law.rests_iff); a target met at such a state is met at '
        'every later step (Law.fixed_rests). More than now, a quantity q of one\'s own rising across the step '
        '(MoreThanNow), is met only by change (more_not_at_rest, Law.more_never_rests); met at every step, q rises between '
        'any two later steps (more_rises), so every configuration is new (more_new) and no list holds them '
        '(more_needs_open, an instance of unlisted_of_new); counting on meets it (succ_more). Above all others, every other '
        'seeker\'s quantity below one\'s own (AboveAll), is met at a state by at most one seeker (aboveAll_unique, '
        'aboveAll_not_two), so under any law no state left unchanged meets it for two seekers (Law.aboveAll_never_rests). '
        'Where what stands is listed at each step (Web.StandingCensus), a condition rising at arbitrarily late steps needs, '
        'at arbitrarily late steps, steps across which what stands does not run down (Flow.more_needs_unrun, from '
        'Flow.change_recurs_iff); where what stands runs down at every step from some step on, no condition rises at '
        'arbitrarily late steps (Flow.more_exhausted). No Lean axiom is used.'),
    'hypotheses': [
        zh_en('目标是配置上的任一条件；目标怎样形成没有建模。rests_iff 设律确定；B2 设所立者每步被列出，这是写在定理中的局部条件。',
              'A target is any condition on the configuration; how a target forms is not modelled. rests_iff assumes a '
              'determined law; B2 assumes what stands is listed at each step, a local condition written into the theorems.'),
        zh_en('离散的步（从第 0 步计）；自然数的量。', 'Discrete steps, counted from step 0; natural-number quantities.'),
    ],
    'correspondence': zh_en(
        'Ren 10 月 10 日：“the seeking system got locked in, what they are pursuing is illusion(in south asia and Buddhism)”，'
        '“find the boundary condition for 无明”；10 月 11 日：“yes let\'s do 无明”。无明边界计划的 B1（够）与 B2（扩张或耗尽）在这里陈述；'
        'B3（反馈）与 B4（明）是 P49、P53、P55 的定理读到寻求上，不重述；B5（劫持）没有陈述。读法（AI 的，待 Ren）：无明是使寻求锁定在不能'
        '于静止中满足之目标上的不见，其边界是 B1；明是识及支持所不标记者的识；知足、知止是边界之内的目标；支配本身不在所排除者之内。'
        f'见整合文档 §{SEC}。',
        'Ren on 10 October: “the seeking system got locked in, what they are pursuing is illusion(in south asia and '
        'Buddhism)” and “find the boundary condition for 无明”; on 11 October: “yes let\'s do 无明”. B1 (enough) and B2 '
        '(expansion or exhaustion) of the 无明 boundary plan are stated here; B3 (feedback) and B4 (明) are the theorems of '
        'P49, P53 and P55 read for seeking, not restated; B5 (hijacking) is not stated. Readings (the AI\'s, pending Ren): '
        '无明 is the not-seeing that keeps seeking locked onto a target that cannot be met at rest, and its boundary is B1; '
        '明 is registration reaching what support does not mark; 知足 and 知止 are targets within the boundary; dominance as '
        f'such is not the target ruled out. See §{SEC} of the integration note.'),
    'canonical_source': SEEKING,
    'aliases': [*B('Law.rests_iff', 'more_needs_open', 'aboveAll_unique', 'Law.aboveAll_never_rests',
                   'Flow.more_needs_unrun', 'Flow.more_exhausted'),
                '无明', 'boundary condition for 无明', '够', 'enough', 'seeking', '寻求'],
    'dependencies': [
        dep('recurrence-without-premise',
            zh_en('复用 Law.orbit、orbit_add、gap_of_lt、gap_of_le、unlisted_of_new 与 Law.succ_open。',
                  'Reuses Law.orbit, orbit_add, gap_of_lt, gap_of_le, unlisted_of_new and Law.succ_open.'),
            zh_en('永不重访需要开放；律的轨道。', 'Never revisiting needs openness; the orbit of a law.'),
            zh_en('“比现在更多”需要开放的世界；够的边界。', 'More than now needs an open world; the boundary of enough.'),
            zh_en('无。', 'None.'), RECURRENCE),
        dep('laws-of-one-step',
            zh_en('复用 Web.StandingCensus、Flow.RunsDown 与 Flow.change_recurs_iff：持续的变化需要开放。',
                  'Reuses Web.StandingCensus, Flow.RunsDown and Flow.change_recurs_iff: continued change needs openness.'),
            zh_en('持续的变化需要所立者不衰减的步。', 'Continued change needs steps at which what stands does not run down.'),
            zh_en('扩张或耗尽。', 'Expansion or exhaustion.'),
            zh_en('所立者每步被列出。', 'What stands is listed at each step.'), LOCALITY),
    ],
    'related': [
        related('testing-within-registration', zh_en('B3、B4 的一部分：主张只经所识的差别被否证；识闭包之外的不被识。',
                                                     'Part of B3 and B4: a claim is refuted only through a difference in what '
                                                     'registers; nothing beyond the registration closure registers.')),
        related('runaway-distance-unregistered', zh_en('B3：断裂之前，断裂还有多远不被识。',
                                                       'B3: before the break, how far off it is does not register.')),
        related('experiment-needs-return', zh_en('B4：自己的动作造成什么，只在配置返回之处、在关于何者无关的模型之下被固定。',
                                                 'B4: what one\'s own act does is fixed only where the configuration returns, '
                                                 'under a model of what is irrelevant.')),
        related('continuing-self-fed-from-beyond', zh_en('那里不断取用的有限家族被围住时不能由其外供给；这里不断上升需要所立者不衰减的步。',
                                                         'There a finite family that keeps taking cannot, enclosed, go on fed '
                                                         'from beyond; here rising without end needs steps at which what '
                                                         'stands does not run down.')),
    ],
    'counterexamples': [],
    'limitations': zh_en(
        '目标怎样形成、怎样修正，寻求者追求其目标，实际形成持有哪些目标，都不推出；劫持（B5）没有陈述；rests_iff 只对确定的律；B2 只说上升不再'
        '复现，耗尽终结寻求者自身没有陈述；B1 的计数是初等的，实质在于把它们陈述为展开之中的目标；读法是 AI 的，待 Ren；不含伦理谓词。',
        'How a target forms or is revised, that a seeker pursues it, and which targets actual formations hold are not '
        'derived; hijacking (B5) is not stated; rests_iff is for determined laws only; B2 says only that the rises stop '
        'recurring, not that exhaustion ends the seekers themselves; the counting of B1 is elementary, and the substance is '
        'in stating it of targets within the unfolding; the readings are the AI\'s, pending Ren; contains no ethical '
        'predicate.'),
    'validation_scope': zh_en(
        f'Lean 4.29.1 合并检查器成功实查（{RUN}）：Becoming.Seeking 的 {N_MODULE} 项定理全部空依赖，其中含 Law.rests_iff、more_needs_open、'
        'aboveAll_unique、Flow.more_needs_unrun 与 Flow.more_exhausted；同一回执覆盖包内 '
        f'{N_PKG} 个模块（含只作导入的根模块与桥接），共 {N_THM} 项定理／{N_DECL} 项声明审计，{N_INH} 个继承模块的当前字节与已通过回执一致；'
        f'外围回执 {PERI_RUN} 通过。检查器另核对核心纯净：核心（GenerativeCore、InquirySufficiency、RelationalRenewal、L1–L4 与根模块 '
        f'Becoming）的导入闭包恰为这 {N_CORE} 个模块，其中每条源声明的公理报告为空（Lean 生成的常量中，只有带字段构造子的单射引理 injEq '
        '依赖 propext，没有源声明使用它们，检查器逐一列出），并且只用 Lean 内置前导即可编译（基础模块的 import Std 在该次编译中去掉）。'
        f'作者反审见整合文档 §{SEC}；未作独立审查，是否需要交 Ren。',
        f'Successful Lean 4.29.1 consolidated check ({RUN}): the {N_MODULE} theorems of Becoming.Seeking all have empty axiom '
        'reports, among them Law.rests_iff, more_needs_open, aboveAll_unique, Flow.more_needs_unrun and '
        f"Flow.more_exhausted; the same receipt covers the package's {N_PKG} modules (including the import-only root and "
        f'the bridge) with {N_THM} theorems/{N_DECL} declaration audits, and {N_INH} inherited modules whose current bytes '
        f'match passed receipts; periphery receipt {PERI_RUN} passed. The checker also verifies core purity: the import '
        'closure of the core (GenerativeCore, InquirySufficiency, RelationalRenewal, L1–L4 and the root module Becoming) '
        f'is exactly these {N_CORE} modules, every source declaration in it has an empty axiom report (of the constants '
        'Lean generates, only the injectivity lemmas of constructors with fields, injEq, depend on propext; no source '
        "declaration uses them, and the checker lists them), and it compiles from Lean's prelude alone (the foundation's "
        "import Std removed for that run). The author's counterreview is in "
        f'§{SEC} of the integration note; not independently reviewed, whether it needs a review is Ren\'s call.'),
    'references': [
        ref(SEEKING, 'proof', DECLS),
        ref(LOCALITY, 'proof', B('Web.StandingCensus', 'Flow.RunsDown', 'Flow.change_recurs_iff')),
        ref(RECURRENCE, 'proof', B('Law.orbit', 'unlisted_of_new', 'gap_of_lt', 'gap_of_le')),
        ref(RECEIPT, 'receipt'),
        ref(STUDY, 'integration'),
        ref(CHAPTER, 'statement'),
        ref(PLANW, 'integration'),
        ref(SOURCE10, 'provenance'),
        ref(SOURCE, 'provenance'),
    ],
    'proof_bindings': [binding(SEEKING, 'Becoming.Seeking'), binding(LOCALITY, 'Becoming.Locality'),
                       binding(RECURRENCE, 'Becoming.Recurrence')],
    'next_delta': zh_en(
        'B5，劫持：目标怎样形成与传递，赢得更多以赢者怎样选择不能静止的目标，接上元吸引子的结果；耗尽在活动需要支持之处终结寻求者自身；'
        '不确定的律中够的边界。',
        'B5, hijacking: how targets form and are transmitted, and how winning that buys more power to win selects targets '
        'that cannot rest, joined to the meta-attractor\'s results; exhaustion ending the seekers themselves where activity '
        'needs support; the boundary of enough under undetermined laws.'),
    'history': [zh_en(
        '2026-10-11 P62：新增，按 Ren 10-10“find the boundary condition for 无明”与 10-11“yes let\'s do 无明”；统一计划 P62；无明边界计划'
        f'的 B1、B2；见整合文档 §{SEC}。',
        '2026-10-11 P62: added, following Ren\'s ‘find the boundary condition for 无明’ (10 October) and ‘yes let\'s do 无明’ '
        f'(11 October); unification plan P62; B1 and B2 of the 无明 boundary plan; see §{SEC} of the integration note.')],
}

path = ROOT / 'theories/becoming/results/records' / f'{record["id"]}.json'
path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print('wrote', path.relative_to(ROOT))
