#!/usr/bin/env python3
"""Write the P62 record target-capture (B5) into a checkout, and extend evolution-on-descent.

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
CAPTURE = f'{D}/Becoming/Capture.lean'
EVOLUTION = f'{D}/Becoming/Evolution.lean'
FLOWL = f'{D}/Becoming/Flow.lean'
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
N_MODULE = next(m for m in receipt['modules'] if m['module'] == 'Becoming.Capture')['theorems']
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


DECLS = B('mul_assoc_nat', 'offspringCount', 'le_offspringCount', 'offspringCount_le', 'share_not_lower', 'share_rises',
          'Flow.descent_needs_unrun', 'Flow.descent_exhausted', 'Law.reform_reabsorbed', 'Captured.next',
          'Captured.byRule', 'Captured.state_reform_returns', 'Captured.rule_reform_changes')

record = {
    'schema_version': 1,
    'id': 'target-capture',
    'title': zh_en(
        '目标的捕获：带着目标的亲代留下更多后代时目标的份额上升；所立者衰减不断则选择停止；下一配置取决于规则时只改状态被重新吸收',
        'The capture of a target: a target\'s share rises where its carriers leave more offspring; running down stops the '
        'selection; where the next configuration depends on the rule, reforming the state alone is re-absorbed'),
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': 'F04',
    'reviewed_at_utc': REVIEWED,
    'claim': zh_en(
        '一个亲代家族的后代计数（offspringCount）在每个亲代至少（至多）留下若干后代时有相应的界（le_offspringCount、offspringCount_le）。'
        '带着目标的亲代 ms 各留下至少 a 个后代、其他亲代 es 各至多 b 个、b ≤ a 时，|ms|·（es 的后代）≤（ms 的后代）·|es|'
        '（share_not_lower）；b < a 且两类都在时严格小于（share_rises）。后代带着亲代的目标时，这就是目标在后代中的份额不低于、高于它在亲代中的'
        '份额。世系是一次开始而立，即一次上升；所立者每步被列出（Web.StandingCensus）时，任意晚的世系需要任意晚处所立者不衰减的步'
        '（Flow.descent_needs_unrun）；所立者从某步起每步衰减时世系不再复现（Flow.descent_exhausted）。在状态与规则的配置上，下一配置取决于规则'
        '而不取决于状态时，规则相同的两个配置从下一步起轨道相同（Law.reform_reabsorbed）；Captured 中状态随规则、规则保持自身，改过的状态立即'
        '回来，改过的规则改变结果（Captured.state_reform_returns、Captured.rule_reform_changes）。乘法结合律以递归证明（mul_assoc_nat），因为'
        '前导的 Nat.mul_assoc 用 propext。不用 Lean 公理。',
        'The offspring of a family of parents, counted (offspringCount), are bounded where each parent leaves at least or '
        'at most so many (le_offspringCount, offspringCount_le). Carriers of a target ms each leaving at least a offspring '
        'and the other parents es each at most b, with b ≤ a, |ms|·(es\'s offspring) ≤ (ms\'s offspring)·|es| '
        '(share_not_lower), strictly where b < a and both kinds are present (share_rises). Where the offspring carry their '
        'parents\' target, this is the target\'s share among the offspring not below, or above, its share among the '
        'parents. A descent is a coming to stand, so a rise; where what stands is listed at each step '
        '(Web.StandingCensus), descent at arbitrarily late steps needs steps at arbitrarily late times across which what '
        'stands does not run down (Flow.descent_needs_unrun), and where it runs down at every step from some step on, '
        'descent does not recur (Flow.descent_exhausted). On configurations of a state and a rule, where the next '
        'configuration depends on the rule and not on the state, two configurations with the same rule have the same '
        'orbit from the next step on (Law.reform_reabsorbed); in Captured the state follows the rule and the rule keeps '
        'itself, a reformed state returns at once and a reformed rule changes the outcome (Captured.state_reform_returns, '
        'Captured.rule_reform_changes). Associativity is proved by recursion (mul_assoc_nat), since the prelude\'s '
        'Nat.mul_assoc uses propext. No Lean axiom is used.'),
    'hypotheses': [
        zh_en('份额定理只设后代计数的界；后代带着亲代的目标（传递）是读作份额所需的前提，如 Becoming.Evolution 中的 TransmitsWithin。',
              'The share theorems assume only bounds on offspring numbers; that offspring carry their parents\' target '
              '(transmission) is the premise needed to read them as shares, as with TransmitsWithin in Becoming.Evolution.'),
        zh_en('世系的定理设所立者每步被列出，这是写在定理中的局部条件；reform_reabsorbed 设下一配置不取决于状态。',
              'The descent theorems assume what stands is listed at each step, a local condition written into them; '
              'reform_reabsorbed assumes the next configuration does not depend on the state.'),
        zh_en('离散的步；自然数的量。', 'Discrete steps; natural-number amounts.'),
    ],
    'correspondence': zh_en(
        'Ren 10 月 10 日把劫持说成“a part of the nature got hijacked by what they "got nurtured"”，10 月 11 日答“b5”。无明边界计划的 B5：'
        '在赢得更多以赢之处，不能静止的目标被多取并多传递，直到被围住；胜者写下判断寻求的规则。这里陈述三个部分：份额（元吸引子对心智之选择的'
        '计数核心，差异的延续与复利），世系停止之处，规则握住结果（“胜者重写考题”与杠杆点论证）。读法（AI 的，待 Ren）：劫持是奖赏不能静止者的'
        '选择所形成、由胜者所写之规则保持的目标；Ren 的“even rationality is self-interest”读作规则伸及理性本身的标准。'
        f'见整合文档 §{SEC}。',
        'Ren on 10 October spoke of nature hijacked “by what they "got nurtured"”, and on 11 October answered “b5”. B5 of '
        'the 无明 boundary plan: where winning buys more power to win, targets that cannot rest are taken more and passed '
        'on more until enclosure binds, and the winners write the rule by which seeking is judged. Three parts are stated '
        'here: the share (the counting core of the meta-attractor\'s selection of minds, differential persistence and '
        'compounding), where descent stops, and the rule holding the outcome (“the winner rewrites the test” and the '
        'leverage-point argument). Readings (the AI\'s, pending Ren): hijacking is a target formed and passed on by a '
        'selection that rewards what cannot rest, held in place by a rule its winners write; Ren\'s “even rationality is '
        f'self-interest” reads as the rule reaching the standard of reason itself. See §{SEC} of the integration note.'),
    'canonical_source': CAPTURE,
    'aliases': [*B('share_not_lower', 'share_rises', 'Flow.descent_needs_unrun', 'Flow.descent_exhausted',
                   'Law.reform_reabsorbed'),
                'hijacking', '劫持', 'capture', '捕获', 'selection of minds', 'winner rewrites the test'],
    'dependencies': [
        dep('evolution-on-descent',
            zh_en('推进它：它陈述 Price 方程的计数形式，未陈述选择项；这里给出二值目标的选择项（share_not_lower、share_rises），并复用 '
                  'Flow.DescendsAt 与 Web.ComesToStand.rises。',
                  'Advances it: it states the counting form of Price\'s equation and leaves the selection term unstated; '
                  'here the selection term for a two-valued target is given (share_not_lower, share_rises), and '
                  'Flow.DescendsAt and Web.ComesToStand.rises are reused.'),
            zh_en('世系与 Price 方程的计数形式。', 'Descent and the counting form of Price\'s equation.'),
            zh_en('目标的份额；世系停止之处。', 'A target\'s share; where descent stops.'),
            zh_en('无。', 'None.'), EVOLUTION),
        dep('laws-of-one-step',
            zh_en('复用 Web.StandingCensus、Flow.RunsDown 与 Flow.change_recurs_iff。',
                  'Reuses Web.StandingCensus, Flow.RunsDown and Flow.change_recurs_iff.'),
            zh_en('持续的变化需要开放。', 'Continued change needs openness.'), zh_en('选择停止之处。', 'Where the selection stops.'),
            zh_en('所立者每步被列出。', 'What stands is listed at each step.'), LOCALITY),
        dep('recurrence-without-premise',
            zh_en('复用 Law.orbit 与 orbit_shift。', 'Reuses Law.orbit and orbit_shift.'),
            zh_en('律的轨道。', 'The orbit of a law.'), zh_en('规则握住结果。', 'The rule holding the outcome.'),
            zh_en('无。', 'None.'), RECURRENCE),
    ],
    'related': [
        related('seeking-boundary', zh_en('B1、B2：寻求何处能静止；这里是 B5：不能静止的目标怎样被选择、选择握在哪里。',
                                          'B1 and B2: where seeking can rest; here B5: how a target that cannot rest is '
                                          'selected and where the selection is held.')),
    ],
    'counterexamples': [],
    'limitations': zh_en(
        '多取者留下更多后代、后代带着亲代的目标、胜者塑造规则，都是给出的，不推出；份额定理是二值目标的计数；reform_reabsorbed 的条件（下一配置'
        '不取决于状态）是强的，规则怎样被胜者改写而仍握住结果没有一般地陈述；Captured 是最小的见证；读法是 AI 的，待 Ren；不含伦理谓词。',
        'That taking more yields more offspring, that offspring carry their parents\' target and that winners shape the rule '
        'are supplied, not derived; the share theorems are the counting for a two-valued target; the condition of '
        'reform_reabsorbed (the next configuration not depending on the state) is strong, and how a rule rewritten by its '
        'winners still holds the outcome is not stated in general; Captured is a minimal witness; the readings are the '
        'AI\'s, pending Ren; contains no ethical predicate.'),
    'validation_scope': zh_en(
        f'Lean 4.29.1 合并检查器成功实查（{RUN}）：Becoming.Capture 的 {N_MODULE} 项定理全部空依赖，其中含 share_not_lower、share_rises、'
        'Flow.descent_exhausted 与 Law.reform_reabsorbed；同一回执覆盖包内 '
        f'{N_PKG} 个模块（含只作导入的根模块与桥接），共 {N_THM} 项定理／{N_DECL} 项声明审计，{N_INH} 个继承模块的当前字节与已通过回执一致；'
        f'外围回执 {PERI_RUN} 通过。检查器另核对核心纯净：核心（GenerativeCore、InquirySufficiency、RelationalRenewal、L1–L4 与根模块 '
        f'Becoming）的导入闭包恰为这 {N_CORE} 个模块，其中每条源声明的公理报告为空（Lean 生成的常量中，只有带字段构造子的单射引理 injEq '
        '依赖 propext，没有源声明使用它们，检查器逐一列出），并且只用 Lean 内置前导即可编译（基础模块的 import Std 在该次编译中去掉）。'
        f'作者反审见整合文档 §{SEC}；未作独立审查，是否需要交 Ren。',
        f'Successful Lean 4.29.1 consolidated check ({RUN}): the {N_MODULE} theorems of Becoming.Capture all have empty axiom '
        'reports, among them share_not_lower, share_rises, Flow.descent_exhausted and Law.reform_reabsorbed; the same receipt '
        f"covers the package's {N_PKG} modules (including the import-only root and the bridge) with {N_THM} "
        f'theorems/{N_DECL} declaration audits, and {N_INH} inherited modules whose current bytes match passed receipts; '
        f'periphery receipt {PERI_RUN} passed. The checker also verifies core purity: the import closure of the core '
        '(GenerativeCore, InquirySufficiency, RelationalRenewal, L1–L4 and the root module Becoming) is exactly these '
        f'{N_CORE} modules, every source declaration in it has an empty axiom report (of the constants Lean generates, '
        'only the injectivity lemmas of constructors with fields, injEq, depend on propext; no source declaration uses '
        "them, and the checker lists them), and it compiles from Lean's prelude alone (the foundation's import Std removed "
        "for that run). The author's counterreview is in "
        f'§{SEC} of the integration note; not independently reviewed, whether it needs a review is Ren\'s call.'),
    'references': [
        ref(CAPTURE, 'proof', DECLS),
        ref(EVOLUTION, 'proof', B('Flow.DescendsAt', 'offspring', 'price')),
        ref(FLOWL, 'proof', B('Web.ComesToStand.rises')),
        ref(LOCALITY, 'proof', B('Web.StandingCensus', 'Flow.RunsDown', 'Flow.change_recurs_iff')),
        ref(RECURRENCE, 'proof', B('Law.orbit', 'Law.orbit_shift')),
        ref(RECEIPT, 'receipt'),
        ref(STUDY, 'integration'),
        ref(CHAPTER, 'statement'),
        ref(PLANW, 'integration'),
        ref(SOURCE10, 'provenance'),
        ref(SOURCE, 'provenance'),
    ],
    'proof_bindings': [binding(CAPTURE, 'Becoming.Capture'), binding(EVOLUTION, 'Becoming.Evolution'),
                       binding(FLOWL, 'Becoming.Flow'), binding(LOCALITY, 'Becoming.Locality'),
                       binding(RECURRENCE, 'Becoming.Recurrence')],
    'next_delta': zh_en(
        '多取者留下更多后代的条件由流推出（取用、支持与给予）；规则被胜者改写（规则依赖于状态）而仍握住结果的一般形式；多值目标的选择项。',
        'The condition that taking more yields more offspring, derived from the flow (taking, support and giving); the '
        'general form in which a rule rewritten by its winners (the rule depending on the state) still holds the outcome; '
        'the selection term for many-valued targets.'),
    'history': [zh_en(
        f'2026-10-11 P62：新增，按 Ren 10-11“b5”；无明边界计划的 B5；见整合文档 §{SEC}。',
        f'2026-10-11 P62: added, following Ren\'s ‘b5’ (11 October); B5 of the 无明 boundary plan; see §{SEC} of the '
        'integration note.')],
}

path = ROOT / 'theories/becoming/results/records' / f'{record["id"]}.json'
path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print('wrote', path.relative_to(ROOT))

path = ROOT / 'theories/becoming/results/records/evolution-on-descent.json'
r = json.loads(path.read_text())
if not any(x.get('id') == 'target-capture' for x in r.get('related', [])):
    r.setdefault('related', []).append(related('target-capture', zh_en(
        '推进本记录：这里未陈述的选择项，对二值目标在 target-capture 中给出（share_not_lower、share_rises）。',
        'Advances this record: the selection term left unstated here is given for a two-valued target in target-capture '
        '(share_not_lower, share_rises).')))
    r['history'].append(zh_en(
        f'2026-10-11 P62：由 target-capture 推进（二值目标的选择项）；本记录的断言不变；见整合文档 §{SEC}。',
        f'2026-10-11 P62: advanced by target-capture (the selection term for a two-valued target); this record\'s claim is '
        f'unchanged; see §{SEC} of the integration note.'))
    path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('extended evolution-on-descent')
