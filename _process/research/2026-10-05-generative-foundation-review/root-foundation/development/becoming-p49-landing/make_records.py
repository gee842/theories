#!/usr/bin/env python3
"""Write the P49 records into a checkout: testing-within-registration and subthreshold-registration,
and extend becoming-finite-horizon with its two corollaries in Becoming.Testing.

Usage: python3 -B make_records.py ROOT REVIEWED_AT_UTC SECTION REVIEW_ORDINAL_ZH REVIEW_ORDINAL_EN

SECTION is the study section number of P49 (its review handling is SECTION.2, the author's
counterreview SECTION.3); REVIEW_ORDINAL_ZH/EN are e.g. 第十七次 / seventeenth.
Reference hashes are the current bytes of ROOT; the receipt's stamp and counts are read from its
becoming-verification.json. Rerun after any edit to a referenced file, after reading that edit:
it rewrites the two P49 records and adds to becoming-finite-horizon only what is not yet there.
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
REVIEWED, SEC, ORD_ZH, ORD_EN = sys.argv[2:6]
D = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
TESTING = f'{D}/Becoming/Testing.lean'
LOCALITY = f'{D}/Becoming/Locality.lean'
FEEDBACK = f'{D}/Becoming/Feedback.lean'
ADMISSION = f'{D}/Becoming/Admission.lean'
INQUIRY = f'{D}/Becoming/Inquiry.lean'
ROLES = f'{D}/Becoming/Roles.lean'
HORIZON = f'{D}/Becoming/Horizon.lean'
REGIONS = f'{D}/Becoming/Regions.lean'
RECEIPT = f'{D}/becoming-verification.json'
STUDY = f'{RF}/BECOMING-RENEWAL-READING.md'
PLAN = f'{RF}/REGISTRATION-AND-TESTING-PLAN.md'
REVIEW = f'{RF}/BECOMING-P49-REVIEW.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-11-wisdom-from-registration.md'
RECORDS = ROOT / 'theories/becoming/results/records'

receipt = json.loads((ROOT / RECEIPT).read_text())
assert receipt['status'] == 'passed'
RUN = receipt['utc']
spine = [m for m in receipt['modules'] if m['spine']]
N_TESTING = next(m for m in receipt['modules'] if m['module'] == 'Becoming.Testing')['theorems']
N_THM = sum(m['theorems'] for m in spine)
N_DECL = sum(len(m['declarations']) for m in spine)
N_PKG = len(spine)
N_CORE = len(receipt['core_closure'])
N_INH = len(receipt['inherited_receipts'])
PERI_RECEIPT = 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/correction-inquiry-verification.json'
peri = json.loads((ROOT / PERI_RECEIPT).read_text())
assert peri['status'] == 'passed'
PERI_RUN = peri['utc']
for path in (TESTING, LOCALITY, REVIEW, SOURCE, PLAN):
    assert (ROOT / path).exists(), path


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


def scope(names_zh, names_en):
    return zh_en(
        f'Lean 4.29.1 合并检查器成功实查（{RUN}）：Becoming.Testing 的 {N_TESTING} 项定理全部空依赖，其中含{names_zh}；同一回执覆盖包内 '
        f'{N_PKG} 个模块（含只作导入的根模块与桥接），共 {N_THM} 项定理／{N_DECL} 项声明审计，{N_INH} 个继承模块的当前字节与已通过回执一致；'
        f'外围回执 {PERI_RUN} 通过。检查器另核对核心纯净：核心（GenerativeCore、InquirySufficiency、RelationalRenewal、L1–L4 与根模块 '
        f'Becoming）的导入闭包恰为这 {N_CORE} 个模块，其中每条源声明的公理报告为空（Lean 生成的常量中，只有带字段构造子的单射引理 injEq '
        '依赖 propext，没有源声明使用它们，检查器逐一列出），并且只用 Lean 内置前导即可编译（基础模块的 import Std 在该次编译中去掉）。'
        f'作者反审见整合文档 §{SEC}.3；整合之前经{ORD_ZH}独立审查（BECOMING-P49-REVIEW.md，起草时称 P47），其处理见 §{SEC}.2；'
        '处理之后的文本尚未经独立审查。',
        f'Successful Lean 4.29.1 consolidated check ({RUN}): the {N_TESTING} theorems of Becoming.Testing all have empty '
        f"axiom reports, among them {names_en}; the same receipt covers the package's {N_PKG} modules (including the "
        f'import-only root and the bridge) with {N_THM} theorems/{N_DECL} declaration audits, and {N_INH} inherited '
        f'modules whose current bytes match passed receipts; periphery receipt {PERI_RUN} passed. The checker also '
        'verifies core purity: the import closure of the core (GenerativeCore, InquirySufficiency, RelationalRenewal, '
        f'L1–L4 and the root module Becoming) is exactly these {N_CORE} modules, every source declaration in it has an '
        'empty axiom report (of the constants Lean generates, only the injectivity lemmas of constructors with fields, '
        'injEq, depend on propext; no source declaration uses them, and the checker lists them), and it compiles from '
        "Lean's prelude alone (the foundation's import Std removed for that run). The author's counterreview is in "
        f'§{SEC}.3 of the integration note; reviewed before integration by the {ORD_EN} independent review '
        f'(BECOMING-P49-REVIEW.md, titled P47), whose treatment is in §{SEC}.2; the text after that treatment is not yet '
        'independently reviewed.')


CORRESPONDENCE = zh_en(
    'Ren 的提议：“can becoming provide wisdoms to avoid run away feedbacks and the identification of knowledge, learning, and '
    'scientific principles like falsifiability”，“I think all the wisdoms about wisdoms, how to think, learn, update, are all '
    'explained within what we have, if not not proved yet”。AI 的回答提出反馈的三种不见、失控是在其一之中运行的回路、跨过它们的方式、'
    '可否证性是被展开纠正的条件，以及 理 的读法；Ren 答：“agree with you, great job, start now. for 4, you can explore which option '
    'is better, then make decision”。独立审查收窄了这些读法：三种不见各有其范围（阈下在交换随反映之处，视界之外在延续开放之处，反映闭包'
    '之外在成员只经自己的反映回应之处）；失控的读法是启发，不是陈述；理 读作对反映负责的模型。所以记录中的读法是 AI 收窄之后的，待 Ren，'
    '不是 Ren 所接受的原文。第 4 问（形成自身的立着是否算作被反映）由 AI 探索后决定：基础只反映支持（supportOnly），一类读法中自身的立着'
    f'经承担自身（Web.SelfBearing）作为阈值反映，量度自身（ownStanding）是观察前提；理由见整合文档 §{SEC}.1。“反映”（registers）原作“计入”，与 P42 '
    '一致；Ren 认为“计入 is apparently weird, need better word”，改为“反映”，取差别在形成的状态中显出之义（见整合文档 §{SEC}.2）。',
    'Ren\'s proposal: “can becoming provide wisdoms to avoid run away feedbacks and the identification of knowledge, '
    'learning, and scientific principles like falsifiability”, and “I think all the wisdoms about wisdoms, how to think, '
    'learn, update, are all explained within what we have, if not not proved yet”. The AI\'s answer proposed three '
    'blindnesses of feedback, a runaway as a loop running inside one of them, the ways across them, falsifiability as the '
    'condition of being corrected by the unfolding, and a reading of 理; Ren answered “agree with you, great job, start '
    'now. for 4, you can explore which option is better, then make decision”. The independent review narrowed the '
    'readings: each blindness has its scope (below a threshold where the exchange follows registration, beyond the '
    'horizon where the continuation is open, beyond the registration closure where the members respond only through '
    'their own registration); the runaway reading is a heuristic, not a statement; and 理 is read as a model answerable '
    'to registration. So the readings recorded here are the AI\'s narrowed ones, pending Ren, not the wording Ren '
    'accepted. Question 4, whether a formation\'s own standing counts as registered, was decided by the AI after '
    'exploring the options: the base registers support only (supportOnly); in the one-kind reading own standing '
    'registers through self-bearing (Web.SelfBearing) as a threshold; and a gauge of oneself (ownStanding) is an '
    f'observation premise. The reasons are in §{SEC}.1 of the integration note. The Chinese for “registers” was 计入, '
    'as in P42; Ren found it “apparently weird” and asked for a better word, so it is 反映, a difference showing in the '
    f'formation\'s state (§{SEC}.2 of the integration note).')

DISCRETE = zh_en('离散的步（从第 0 步计）；自然数的水平、所需与数量；条件上的判定相等（DecidableEq）只在按条件分情形处使用，不用经典推理。',
                 'Discrete steps, counted from step 0; natural-number levels, needs and amounts; decidable equality of '
                 'conditions (DecidableEq) is used only to split cases on conditions, and no classical reasoning is used.')
LOCAL_BALANCE = zh_en(
    '平衡只在被反映的条件上逐步假设（Flow.BalancesOn，单元素家族，不需要有限性）；整体的平衡经 Flow.Balances.on 给出它。',
    'Balance is assumed only on the conditions registered, at each step (Flow.BalancesOn, singleton families, needing '
    'no finiteness); global balance gives it through Flow.Balances.on.')
HISTORY = [zh_en(
    '2026-10-11 P49：新增，按 Ren“agree with you, great job, start now. for 4, you can explore which option is better, then make '
    f'decision”；起草时编为 P47，因 P47 已是 Becoming.Standing 而改为 P49；统一计划 P49；见整合文档 §{SEC}；整合之前经{ORD_ZH}独立'
    f'审查，处理见 §{SEC}.2。',
    '2026-10-11 P49: added, following Ren\'s ‘agree with you, great job, start now. for 4, you can explore which option is '
    'better, then make decision’; drafted as P47 and renumbered because P47 is Becoming.Standing; unification plan P49; see '
    f'§{SEC} of the integration note; reviewed before integration by the {ORD_EN} independent review, handled in §{SEC}.2.')]
SHARED_REFS = [ref(RECEIPT, 'receipt'), ref(STUDY, 'integration'), ref(CHAPTER, 'statement'), ref(PLAN, 'integration'),
               ref(REVIEW, 'review'), ref(SOURCE, 'provenance')]

# ---------------------------------------------------------------- subthreshold-registration

S_DECLS = B('Web.LevelsAtLeast', 'Web.registersAlike_iff_of_levelsAtLeast', 'Web.admits_iff_supported_of_agree',
            'le_of_add_eq_of_le', 'eq_of_add_eq_of_eq', 'Flow.ExchangeFollows', 'Flow.difference_kept',
            'Flow.levelsAtLeast_while_alike', 'Flow.alike_while_supported', 'Flow.difference_changes_after_divergence',
            'Flow.subthreshold_alike', 'Flow.subthreshold_alike_always', 'Gauged.flow', 'Gauged.web', 'Gauged.stock',
            'Gauged.gauge_changes_difference', 'Gauged.own_is_stock', 'SupportDrawn.flow', 'SupportDrawn.web',
            'SupportDrawn.follows', 'SupportDrawn.difference_waits', 'JointFailure.flow', 'JointFailure.web',
            'JointFailure.difference_kept', 'Attracting.lowerFlow', 'Attracting.higherFlow', 'Attracting.web',
            'Attracting.higher_breaks_first', 'SelfPrey.flow', 'SelfPrey.web', 'SelfPrey.selfBearing',
            'SelfPrey.within_influence', 'SelfPrey.threshold_on_oneself', 'ownStanding', 'supportOnly')

subthreshold = {
    'schema_version': 1,
    'id': 'subthreshold-registration',
    'title': zh_en(
        '阈下的差别：交换随反映时，形成依存而不观察的储量上的差别保持到两网的支持分岔；观察储量解除它，他者回应储量本身时则不然',
        'Differences below the threshold: where the exchange follows registration, a difference in a stock a formation '
        'depends on and does not observe stays until the two webs\' support diverges; observing the stock lifts it, '
        'and others responding to the stock itself break it'),
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': 'F04',
    'reviewed_at_utc': REVIEWED,
    'claim': zh_en(
        '设两个流在形成 g 所反映（依存或观察）的每个条件上逐步平衡，并且 g 周围的交换随其反映：凡 g 直到某步反映相同，两个流跨过该步在 g '
        '所反映的每个条件上，对在场的全部形成，取用与给予的总量相同（Flow.ExchangeFollows）。那么 g 反映相同期间，它所反映条件上的每个差别'
        '都保持起始的样子（Flow.difference_kept）。第二个网在 g 所反映的条件上起始不低、在其观察的条件上相同时，在第一个网此前每步都支持 g '
        '的每一步，g 都反映相同（Flow.alike_while_supported），可以有任意多个条件不同；差别在某步之前已改变，必有更早的一步，第二个网的水平'
        '接纳 g 而第一个网不支持它，活动需要支持时 g 在第一个网中并非此前每步都活跃（Flow.difference_changes_after_divergence）。起始只在 g '
        '依存而不观察的一个储量上不同、第二个网中高 d 时，在第一个网此前每步都支持 g 的每一步，储量恰好高 d，g 所反映的其余条件相同，g 此前'
        '每步都反映相同（Flow.subthreshold_alike）；第一个网每步都支持 g 时每步都如此（Flow.subthreshold_alike_always）。见证：SupportDrawn '
        '中形成需要一个单位、在每个被支持的步取一个单位，交换只随支持，差别保持到第三步，较低的网在第三步不支持它而较高的网支持，第四步差别'
        '已变（SupportDrawn.difference_waits）；JointFailure 中两网从第二步起都不支持形成，差别每步都保持（JointFailure.difference_kept）；'
        'Gauged 中观察储量的形成在第一步取尽需要之上的全部，在较高的网中动用了差别，交换随其反映而不约束任何东西，只反映支持时交换不随其反映'
        '（Gauged.gauge_changes_difference）；储量划作自身的立着时，量度自身就是量度储量（Gauged.own_is_stock）；Attracting 中被较高的储量'
        '招来的取用者使较高的网在第二步就不支持依存者，交换不随其反映（Attracting.higher_breaks_first）；SelfPrey 中以所需一依存于自身的猎物，'
        '咬一个单位经支持每步都反映相同，量度自身在第二步反映它，咬两个单位经支持在第二步就被反映（SelfPrey.threshold_on_oneself）。'
        '不用 Lean 公理。',
        'Let two flows balance at each step on every condition a formation g registers (depends on or observes), and let '
        'the exchange around g follow its registration: wherever g has registered alike up to a step, the two flows take '
        'from and give to every condition g registers alike across that step, in total over every formation present '
        '(Flow.ExchangeFollows). Then while g registers alike every difference on a condition it registers stays as it '
        'was at the start (Flow.difference_kept). Where the second web starts at least as high on what g registers and '
        'alike on what it observes, g registers alike at every step before which the first web supported it '
        '(Flow.alike_while_supported), any number of conditions differing; where a difference has changed by a step, at '
        'some earlier step the second web\'s levels admitted g and the first web did not support it, and where activity '
        'needs support g was not active in the first web at every earlier step '
        '(Flow.difference_changes_after_divergence). Where the starts differ only in one stock g depends on and does not '
        'observe, d higher in the second web, at every step before which the first web supported g at every step the '
        'stock stands exactly d higher, every other condition g registers stands alike and g has registered alike '
        '(Flow.subthreshold_alike), and at every step where the first web supports g at every step '
        '(Flow.subthreshold_alike_always). Witnesses: in SupportDrawn a formation needing one unit draws one unit at each '
        'supported step, the exchange following its support only; the difference stands through the third step, where '
        'the lower web fails to support it and the higher supports it, and has changed by the fourth '
        '(SupportDrawn.difference_waits); in JointFailure both webs fail the formation from the second step and the '
        'difference stands at every step (JointFailure.difference_kept); in Gauged a formation observing its stock draws '
        'all of it above its need at the first step and draws on the difference in the higher web, the exchange '
        'following its registration constraining nothing, while through support only the exchange does not follow its '
        'registration (Gauged.gauge_changes_difference); carving the stock as its own standing, a gauge of oneself is the '
        'gauge of the stock (Gauged.own_is_stock); in Attracting a taker drawn by the higher stock makes the higher web '
        'fail the dependent at the second step, the exchange not following its registration '
        '(Attracting.higher_breaks_first); in SelfPrey, with the prey depending on its own standing at need one, a bite of '
        'one registers alike through support at every step and through a gauge of oneself at the second, and a bite of '
        'two registers through support at the second step (SelfPrey.threshold_on_oneself). No Lean axiom is used.'),
    'hypotheses': [
        LOCAL_BALANCE,
        zh_en('交换随反映（Flow.ExchangeFollows）是给出的假设，不由动力学推出：它是关于 g 周围全部交换的，排除他者对 g 所不反映者作出回应；'
              'Attracting 是它不成立时的反例。',
              'The exchange following registration (Flow.ExchangeFollows) is a supplied hypothesis, not derived from the '
              'dynamics: it concerns the whole exchange around g and excludes others responding to what g does not '
              'register; Attracting is the counterexample where it fails.'),
        zh_en('反映：形成反映它的支持（水平是否接纳它）与它所观察之条件的水平（obs，参数，基础是 supportOnly）。活动由表示给出，不算作被反映；'
              '在 Web.Dependent 之下它不能超出支持。',
              'Registration: a formation registers its support (whether the levels admit it) and the levels of the '
              'conditions it observes (obs, a parameter, with supportOnly the base). Activity is supplied by the '
              'representation and is not counted as registered; under Web.Dependent it cannot outrun support.'),
        zh_en('见证的结论：各见证的流与网（SupportDrawn、JointFailure、Gauged、Attracting、SelfPrey）。',
              'For the witnesses: their flows and webs (SupportDrawn, JointFailure, Gauged, Attracting, SelfPrey).'),
        DISCRETE,
    ],
    'correspondence': CORRESPONDENCE,
    'canonical_source': TESTING,
    'aliases': [*B('Flow.ExchangeFollows', 'Flow.difference_kept', 'Flow.alike_while_supported',
                   'Flow.difference_changes_after_divergence', 'Flow.subthreshold_alike',
                   'Flow.subthreshold_alike_always', 'SupportDrawn.difference_waits', 'JointFailure.difference_kept',
                   'Gauged.gauge_changes_difference', 'Attracting.higher_breaks_first',
                   'SelfPrey.threshold_on_oneself'),
                'threshold blindness', '阈下不见', 'subthreshold registration', '阈下的差别'],
    'dependencies': [
        dep('testing-within-registration',
            zh_en('复用 Web.Registers、Web.RegistersAlike、Web.RegistersAlikeUpTo、supportOnly 与 ownStanding。',
                  'Reuses Web.Registers, Web.RegistersAlike, Web.RegistersAlikeUpTo, supportOnly and ownStanding.'),
            zh_en('一个形成反映什么，两个水平历史何时对它反映相同。',
                  'What a formation registers, and when two level histories register alike for it.'),
            zh_en('交换随反映的假设与阈下差别的规律。', 'The hypothesis of the exchange following registration, and the '
                  'laws of differences below the threshold.'),
            zh_en('无。', 'None.'), TESTING),
        dep('closing-needs-net-draw',
            zh_en('复用 Web.Admits：支持就是所需条件的水平接纳形成。', 'Reuses Web.Admits: support is admission by the '
                  'levels of the conditions required.'),
            zh_en('接纳。', 'Admission.'),
            zh_en('第二个网的水平在第一个网支持 g 处接纳 g，所以 g 反映相同。', 'The second web\'s levels admit g wherever '
                  'the first web supports it, so g registers alike.'),
            zh_en('无。', 'None.'), ADMISSION),
        dep('levels-of-closure',
            zh_en('复用 Web.DependsOn：g 依存于储量。', 'Reuses Web.DependsOn: g depends on the stock.'),
            zh_en('依存。', 'Dependence.'), zh_en('被反映的条件。', 'The conditions registered.'),
            zh_en('无。', 'None.'), FEEDBACK),
    ],
    'related': [
        related('reserve-defers-ending', zh_en('那里储备推迟终结而不逃脱它；这里交换随反映时，储量上的差别在支持分岔之前不被反映。',
                                               'There a reserve defers the end and does not escape it; here, where the '
                                               'exchange follows registration, a difference in a stock registers only '
                                               'once support diverges.')),
        related('consumption-ends-with-feeders', zh_en('那里只由不被支持的供给者供给的消耗至多持续其所消耗的水平那么多步；这里支持在分岔之前'
                                                       '不反映储量的差别。',
                                                       'There consumption fed only by unsupported feeders lasts at most as '
                                                       'many steps as the level it consumes; here support registers a '
                                                       'difference in a stock only once it diverges.')),
        related('becoming-finite-horizon', zh_en('那里有限的前缀不决定更新还是消耗；这里是阈值处的反映。',
                                                 'There no finite prefix decides renewal or consumption; here registration '
                                                 'at a threshold.')),
    ],
    'counterexamples': [
        {'path': TESTING, 'detail': zh_en(
            '他者回应储量本身时，交换不随反映，较高的储量可以先终结依存者：Attracting 中被三个单位的储量招来的取用者使较高的网在第二步就不'
            '支持依存者，较低的网仍支持（Attracting.higher_breaks_first）。未加限定的读法“损失直到断裂才被反映”对此不成立。',
            'Where others respond to the stock itself the exchange does not follow registration, and a higher stock can end '
            'the dependent first: in Attracting a taker drawn by a stock of three makes the higher web fail the dependent at '
            'the second step while the lower web still supports it (Attracting.higher_breaks_first). The unqualified '
            'reading that losses register only at the break fails here.')},
        {'path': TESTING, 'detail': zh_en(
            '观察储量解除阈下的差别：Gauged 中观察储量的形成在两个网中每步都被支持，并在较高的网中动用差别（Gauged.gauge_changes_difference）。',
            'Observing the stock lifts the blindness below the threshold: in Gauged a formation observing its stock is '
            'supported at every step in both webs and draws on the difference in the higher one '
            '(Gauged.gauge_changes_difference).')},
    ],
    'limitations': zh_en(
        '形成观察支持之外的任何东西、量度自身的立着或想要避免失控都不推出；交换随反映是给出的假设，哪些展开满足它是经验问题；回路、增益与'
        '失控没有定义，失控的读法是启发；观察是精确的，带误差的量度（校准）没有建模；读法是 AI 的，经审查收窄，待 Ren；不含伦理谓词。',
        'That a formation observes anything beyond its support, gauges its own standing or wants to avoid a runaway is '
        'not derived; the exchange following registration is a supplied hypothesis, and which unfoldings meet it is '
        'empirical; loops, gain and runaway are not defined, and the runaway reading is a heuristic; observation is '
        'exact, and measurement with error (calibration) is not modelled; the readings are the AI\'s, narrowed by the '
        'review, pending Ren; contains no ethical predicate.'),
    'validation_scope': scope('Flow.difference_kept、alike_while_supported、difference_changes_after_divergence、subthreshold_alike、'
                              'SupportDrawn.difference_waits 与 Attracting.higher_breaks_first',
                              'Flow.difference_kept, alike_while_supported, difference_changes_after_divergence, '
                              'subthreshold_alike, SupportDrawn.difference_waits and Attracting.higher_breaks_first'),
    'references': [
        ref(TESTING, 'proof', S_DECLS),
        ref(LOCALITY, 'proof', B('Flow.BalancesOn', 'Flow.Balances.on')),
        ref(ADMISSION, 'proof', B('Web.Admits')),
        ref(FEEDBACK, 'proof', B('Web.DependsOn')),
        ref(ROLES, 'proof', B('Web.SelfBearing')),
        *SHARED_REFS,
    ],
    'proof_bindings': [binding(TESTING, 'Becoming.Testing'), binding(LOCALITY, 'Becoming.Locality'),
                       binding(ADMISSION, 'Becoming.Admission'), binding(FEEDBACK, 'Becoming.Feedback'),
                       binding(ROLES, 'Becoming.Roles')],
    'next_delta': zh_en(
        '定义回路（水平影响取用、取用又影响水平的闭合）并把失控陈述为定理；由动力学给出交换随反映，而不是假设它；带误差的观察（校准）。',
        'Define a loop (levels affecting taking, and taking the levels) and state a runaway as a theorem; give the exchange '
        'following registration from the dynamics rather than assume it; observation with error (calibration).'),
    'history': HISTORY,
}

# ---------------------------------------------------------------- testing-within-registration

R_DECLS = B('supportOnly', 'ownStanding', 'ownStanding_other', 'sees_narrow', 'recordThen',
            'Web.RegistersAlike', 'Web.RegistersAlikeUpTo', 'Web.Refutes', 'Web.RefutesWithin', 'Web.Registers',
            'Web.Belief', 'Web.RegistersAlikeAll', 'Web.RefutesBy',
            'Web.RegistersAlike.refl', 'Web.RegistersAlike.symm', 'Web.RegistersAlikeUpTo.symm',
            'Web.RegistersAlikeUpTo.earlier', 'Web.RegistersAlikeUpTo.of_obs', 'Web.registersAlikeUpTo_of_agree',
            'Web.alike_of_threshold', 'Web.observed_level_registers', 'Web.Refutes.not_of_alike',
            'Web.Refutes.not_meets', 'Web.Refutes.later', 'Web.Refutes.widen', 'Web.Refutes.not_of_extension',
            'Web.tail_unrefuted', 'Web.refutes_iff_refutesWithin_all', 'Web.refutesWithin_iff_conjunction',
            'Web.RefutesWithin.narrow', 'Web.RefutesWithin.not_meets', 'Web.RefutesBy.of_member',
            'Web.belief_refutes_iff', 'Web.belief_judge_iff', 'Web.belief_judge_later', 'Web.belief_judge_widen',
            'Flow.RegisteredFrom', 'Flow.WithinRegistration', 'Flow.RegisteredFromEither', 'Flow.BalancedHistory',
            'Flow.balancedHistory_iff', 'Flow.BalancedHistory.agree', 'Flow.refutes_tail_within',
            'Flow.withinRegistration_of_withinInfluence', 'Flow.withinRegistration_supportOnly',
            'Flow.withinRegistration_mono_obs', 'Flow.withinRegistration_mono_flow', 'Flow.beyond_registration',
            'Flow.exchange_agrees_within', 'Flow.alike_within_closed', 'Flow.alike_within_registration',
            'Flow.withhold_exchanges', 'Flow.unregistered_beyond_registration', 'Flow.unrefuted_beyond_registration',
            'Flow.beyond_needs_model', 'Flow.belief_judge_beyond', 'Prey.flow', 'Prey.web', 'Prey.spared',
            'Prey.predatorPart', 'Prey.preyAlone_closed', 'Prey.registers_taking', 'Prey.omits', 'Stationary.still',
            'Stationary.actual', 'Stationary.model_error', 'Stationary.model_refuted', 'Clearing.clearerSide',
            'Clearing.clearerSide_closed', 'Clearing.alike_for_clearer', 'Clearing.DwellerEnded',
            'Clearing.tested_by_dweller', 'Clearing.EitherEnded', 'Clearing.pooled', 'Clearing.FixedStartAndExchange',
            'Clearing.model_idles_registration')

testing_rec = {
    'schema_version': 1,
    'id': 'testing-within-registration',
    'title': zh_en(
        '检验在反映之内：主张只经反映的差别被否证，相对于模型的否证是对模型与主张一起的否证；成员只经自己的反映回应时，反映闭包之外的在其中'
        '不被反映；检验是关系的',
        'Testing lies within registration: a claim is refuted only through a difference in what registers, and refutation '
        'relative to a model is refutation of the model and the claim together; where the members respond only through '
        'their own registration, nothing beyond the registration closure registers within it; testing is relational'),
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': 'F04',
    'reviewed_at_utc': REVIEWED,
    'claim': zh_en(
        '形成反映它的支持（水平是否接纳它）与它所观察之条件的水平（obs；基础是只反映支持，supportOnly）。在两个水平历史之下，在某步水平同样'
        '接纳它、所观察的条件同样立着，就是反映相同（Web.RegistersAlike），直到某步每步如此就是直到该步反映相同（Web.RegistersAlikeUpTo）。'
        '依存而不观察的条件只反映它是否满足所需（Web.alike_of_threshold），观察的条件反映其水平（Web.observed_level_registers），观察得更多'
        '分辨得更多（Web.RegistersAlikeUpTo.of_obs）。关于水平历史的主张在某步被否证，是指满足它的历史没有一个直到该步与实际反映相同'
        '（Web.Refutes）：主张只经反映的差别被否证（Web.Refutes.not_of_alike），成立的永不被否证，否证此后一直成立，观察得更多否证得更多；'
        '没有模型时，对任何有限的记录，“某条件将归于无”与“它此后一直在无之上”都不被否证（Web.tail_unrefuted）。相对于模型（可容许历史的类）'
        '的否证（Web.RefutesWithin）恰是对模型与主张一起的否证（Web.refutesWithin_iff_conjunction）；相对于流的水平历史，观察储量的形成在'
        '第一步否证一切“它将归于无”的假主张（Flow.refutes_tail_within）；错的模型否证成立的，反映否证模型（Stationary.model_error、'
        'model_refuted）。形成的信念是与实际反映相同的历史（Web.Belief）；否证是主张与信念不交；由反映作出的判断恰是 Becoming.Inquiry 中'
        '判断过程在信念上的共同回应，更晚的步与更多的观察都保持它（Web.belief_judge_iff、belief_judge_later、belief_judge_widen）。形成依存于'
        '或观察一个条件就反映它（Web.Registers）；反映闭包是对经所反映者受影响的闭包（Flow.WithinRegistration），含影响闭包，只反映支持时就是'
        '它，随观察与交换增大。两个流在相同的形成在场、在一个区域的成员所反映的每个条件上逐步平衡，区域在两个流中都对经所反映者受影响封闭，'
        '水平起始在成员所反映的条件上相同，每个成员在自己反映相同之处对成员所反映的条件同样取用与给予时，每个成员每步都反映相同'
        '（Flow.alike_within_closed）。其余交换固定时，这给出：成员都在反映闭包之外的部分，闭包之内每步有与无它都反映相同'
        '（Flow.unregistered_beyond_registration，推广 P42 的 unregistered_beyond_influence），无部分的水平所满足的主张在闭包之内不被否证，'
        '相对于模型的否证靠模型对部分之交换的排除，闭包之内的判断在有与无部分时都可容许（Flow.unrefuted_beyond_registration、'
        'beyond_needs_model、belief_judge_beyond）。Clearing 中清除者每步都反映相同，无论清除是否终结栖居者（Clearing.alike_for_clearer）；'
        '在不清除的世界中，“栖居者已被终结”被清除者在任何一步都不否证，被栖居者在第三步否证（Clearing.tested_by_dweller）；“第三步栖居者或'
        '清除者不被接纳”，两者各自都不否证，合起来否证（Clearing.pooled）；以固定起始与交换的模型，清除者在第一步否证它不反映的（'
        'Clearing.model_idles_registration）。Prey 中不依存于自身的猎物，捕食者在其影响闭包之外、量度自身时的反映闭包之内，经支持每步反映'
        '相同、量度自身则反映其取用（Prey.registers_taking），这靠被省略的关系（Prey.omits）。不用 Lean 公理。',
        'A formation registers its support (whether the levels admit it) and the levels of the conditions it observes '
        '(obs; the base registers support only, supportOnly). Under two level histories it registers alike at a step '
        'when the levels admit it alike and its observed conditions stand alike (Web.RegistersAlike), and alike up to a '
        'step when it does so at every step up to it (Web.RegistersAlikeUpTo). A condition depended on and not observed '
        'registers only whether it meets the need (Web.alike_of_threshold), an observed one registers its level '
        '(Web.observed_level_registers), and observing more distinguishes more (Web.RegistersAlikeUpTo.of_obs). A claim '
        'about level histories is refuted at a step when no history meeting it registers alike with the actual one up to '
        'that step (Web.Refutes): a claim is refuted only through a difference in what registers '
        '(Web.Refutes.not_of_alike), what holds is never refuted, a refutation stands, and observing more refutes more; '
        'without a model, for any finite record, neither the claim that a condition comes to nothing nor the claim that '
        'it stays above nothing afterwards is refuted (Web.tail_unrefuted). Refutation relative to a model, a class of '
        'admissible histories (Web.RefutesWithin), is exactly refutation of the model and the claim together '
        '(Web.refutesWithin_iff_conjunction); relative to the level histories of a flow a formation observing a stock '
        'refutes at the first step every false claim that it comes to nothing (Flow.refutes_tail_within); a wrong model '
        'refutes what holds, and registration refutes the model (Stationary.model_error, model_refuted). A formation\'s '
        'belief is the histories registering alike with the actual one (Web.Belief); refutation is a claim disjoint from '
        'the belief; a judgment from registration is exactly a common response of the judging process of '
        'Becoming.Inquiry over the belief, kept as later steps and more observation narrow it (Web.belief_judge_iff, '
        'belief_judge_later, belief_judge_widen). A formation registers a condition when it depends on it or observes it '
        '(Web.Registers); the registration closure is the closure under being affected through what is registered '
        '(Flow.WithinRegistration), holding the influence closure, equal to it registering support only, and growing '
        'with observation and exchange. For two flows with the same formations present, balancing at each step on every '
        'condition a member of a region registers, the region closed in both under being affected through what is '
        'registered, the levels starting alike on what members register, and each member taking from and giving to '
        'what members register alike wherever it has registered alike, every member registers alike at every step '
        '(Flow.alike_within_closed). With the rest of the exchange fixed this gives that a part whose members all lie '
        'beyond the registration closure is registered alike with and without it at every step within the closure '
        '(Flow.unregistered_beyond_registration, extending P42\'s unregistered_beyond_influence), that no claim met by the '
        'levels without the part is refuted within it, that a refutation there relative to a model rests on the model '
        'excluding the part\'s exchange, and that a judgment there is admissible with and without the part '
        '(Flow.unrefuted_beyond_registration, beyond_needs_model, belief_judge_beyond). In Clearing the clearer registers '
        'alike at every step whether or not its clearing ends the dweller (Clearing.alike_for_clearer); in the world with '
        'the habitat spared, the claim that the dweller is ended is refuted by the clearer at no step and by the dweller '
        'at the third step (Clearing.tested_by_dweller); the claim that the dweller or the clearer is not admitted at the '
        'third step is refuted by neither alone and by the two together (Clearing.pooled); with a model fixing the start '
        'and the exchange the clearer refutes at the first step what it does not register '
        '(Clearing.model_idles_registration). In Prey, the prey not depending on itself, the predator lies beyond its '
        'influence closure and within its registration closure under a gauge of itself, registering alike through '
        'support at every step and through the gauge after the bite (Prey.registers_taking), which rests on omitted '
        'relations (Prey.omits). No Lean axiom is used.'),
    'hypotheses': [
        zh_en('反映与否证的定义不设前提；模型是给出的可容许历史类。',
              'The definitions of registration and refutation assume nothing; a model is a supplied class of admissible '
              'histories.'),
        LOCAL_BALANCE,
        zh_en('Flow.alike_within_closed 另设区域在两个流中封闭、起始相同与成员只经自己的反映回应，都是给出的假设；有与无部分的比较用扣留水平'
              '（Flow.WithheldLevels，其余交换不变，是表示上的选择）；部分是判定的形成家族。',
              'Flow.alike_within_closed further assumes the region closed in both flows, the starts alike, and the members '
              'responding only through their own registration, all supplied hypotheses; the comparison with and without a '
              'part uses withheld levels (Flow.WithheldLevels, the rest of the exchange unchanged, a choice of the '
              'representation); a part is a decided family of formations.'),
        zh_en('反映：支持与所观察条件的水平（obs，参数）；活动由表示给出，不算作被反映。否证是对一个形成、在一步、在一个水平历史之下的；主张是'
              '关于水平历史的任何命题。',
              'Registration: support and the levels of the conditions observed (obs, a parameter); activity is supplied by '
              'the representation and is not counted as registered. Refutation is by one formation, at a step, under one '
              'level history; a claim is any proposition about level histories.'),
        zh_en('见证的结论：各见证的流、网与模型（Clearing、Prey、Stationary）。',
              'For the witnesses: their flows, webs and models (Clearing, Prey, Stationary).'),
        DISCRETE,
    ],
    'correspondence': CORRESPONDENCE,
    'canonical_source': TESTING,
    'aliases': [*B('Web.RegistersAlike', 'Web.RegistersAlikeUpTo', 'Web.Refutes', 'Web.RefutesWithin', 'Web.Registers',
                   'Web.Belief', 'Web.alike_of_threshold', 'Web.tail_unrefuted', 'Web.refutesWithin_iff_conjunction',
                   'Web.belief_judge_iff', 'Flow.WithinRegistration', 'Flow.refutes_tail_within',
                   'Flow.alike_within_closed', 'Flow.unregistered_beyond_registration',
                   'Flow.unrefuted_beyond_registration', 'Flow.beyond_needs_model', 'Clearing.tested_by_dweller',
                   'Clearing.pooled', 'Stationary.model_error'),
                'registration closure', '反映闭包', 'reach blindness', 'falsifiability', '可否证性',
                'refutation relative to a model', '相对于模型的否证'],
    'dependencies': [
        dep('feedback-and-reach',
            zh_en('推广 P42 的 Flow.Balances.unregistered_beyond_influence（加入观察，并以成员有回应的形式 Flow.alike_within_closed 为其根据；'
                  '只反映支持时 Flow.unregistered_beyond_registration 就是它），复用 Flow.Exchanges、Flow.WithinInfluence、'
                  'Clearing.sparedFlow、sparedWeb、spared_balances 与 spared_dependent；这里的实质增量是 alike_within_closed，不是'
                  '固定其余交换的形式。',
                  'Extends P42\'s Flow.Balances.unregistered_beyond_influence (adding observation, and grounding it in the '
                  'form where the members respond, Flow.alike_within_closed; registering support only, '
                  'Flow.unregistered_beyond_registration is it), and reuses Flow.Exchanges, Flow.WithinInfluence, '
                  'Clearing.sparedFlow, sparedWeb, spared_balances and spared_dependent; the substantive delta here is '
                  'alike_within_closed, not the fixed-rest form.'),
            zh_en('交换、影响闭包与不清除的世界。', 'Exchange, the influence closure and the world with the habitat spared.'),
            zh_en('反映闭包及其不见；清除者不检验栖居者被终结。', 'The registration closure and its blindness; the clearer does '
                  'not test whether the dweller is ended.'),
            zh_en('平衡；扣留水平。', 'Balance; withheld levels.'), FEEDBACK),
        dep('levels-of-closure',
            zh_en('复用 ClosedUnder、WithinClosure（mono、not_rel、of_rel、refl、trans）、closedUnder_withinClosure 与 Web.DependsOn。',
                  'Reuses ClosedUnder, WithinClosure (mono, not_rel, of_rel, refl, trans), closedUnder_withinClosure and '
                  'Web.DependsOn.'),
            zh_en('对一个关系的闭包。', 'Closure under a relation.'),
            zh_en('反映闭包及其封闭。', 'The registration closure and its closedness.'),
            zh_en('无。', 'None.'), FEEDBACK),
        dep('closing-needs-net-draw',
            zh_en('复用 Web.Admits、Flow.withhold 与 Flow.WithheldLevels。', 'Reuses Web.Admits, Flow.withhold and '
                  'Flow.WithheldLevels.'),
            zh_en('接纳与扣留水平。', 'Admission and withheld levels.'),
            zh_en('反映相同的第一项；有与无部分的比较。', 'The first clause of registering alike; the comparison with and '
                  'without a part.'),
            zh_en('无。', 'None.'), ADMISSION),
        dep('four-cases-of-a-part',
            zh_en('复用 Clearing.unsupported_with：清除时栖居者从第三步起不被支持。', 'Reuses Clearing.unsupported_with: with '
                  'the clearing the dweller is unsupported from the third step on.'),
            zh_en('栖居者被终结。', 'The dweller is ended.'),
            zh_en('Clearing.DwellerEnded 在清除的世界中成立。', 'Clearing.DwellerEnded holds in the world with the clearing.'),
            zh_en('无。', 'None.'), REGIONS),
    ],
    'related': [
        related('subthreshold-registration', zh_en('那里是阈值处的反映与交换随反映时阈下差别的规律；这里是反映、否证、所及与检验的关系性。',
                                                   'There registration at a threshold and the laws of differences below '
                                                   'it where the exchange follows registration; here registration, '
                                                   'refutation, reach and the relational character of testing.')),
        related('becoming-finite-horizon', zh_en('那里有限的前缀不决定更新还是消耗，其两个推论 no_exact_finite_reading 与 '
                                                 'finite_reading_withholds_renewal 也在 Becoming.Testing 中；这里没有模型时有限的记录不否证关于其后的'
                                                 '主张，相对于模型则可以。',
                                                 'There no finite prefix decides renewal or consumption, and its two '
                                                 'corollaries no_exact_finite_reading and finite_reading_withholds_renewal '
                                                 'are also in Becoming.Testing; here without a model no finite record '
                                                 'refutes a claim about what follows it, while relative to a model one '
                                                 'can.')),
        related('finite-fallible-inquiry-necessity', zh_en('外围的信息界：保持同样读数的适应关系不能同时满足更强的覆盖；这里在脊柱上，'
                                                           '同样的反映不分辨，主张只经反映的差别被否证。',
                                                           'The periphery\'s information bound: adaptive relations preserving '
                                                           'the same readouts cannot also meet stronger coverage; here on the '
                                                           'spine, the same registration does not distinguish, and a claim is '
                                                           'refuted only through a difference in what registers.')),
        related('prefix-observation-loss', zh_en('那里一切前缀问题都可以漏掉中间的损失；这里没有模型时有限的记录不否证关于其后的主张。',
                                                 'There every prefix question can omit an intermediate loss; here without a '
                                                 'model no finite record refutes a claim about what follows it.')),
        related('scientific-inquiry-foundation', zh_en('这一开放目标的一个部分：在脊柱上陈述被展开否证的条件与相对于模型的否证；不确立整个目标。',
                                                       'One part of this open target: the condition of being refuted by the '
                                                       'unfolding, and refutation relative to a model, stated on the spine; '
                                                       'it does not establish the whole target.')),
    ],
    'counterexamples': [
        {'path': TESTING, 'detail': zh_en(
            '相对于模型的否证可以出错：Stationary 中模型说没有取用与给予，相对于它，量度储量的形成在第一步否证“储量将归于无”，而这在实际中成立'
            '（Stationary.model_error）。',
            'Refutation relative to a model can err: in Stationary the model says nothing takes or gives, and relative to '
            'it a formation gauging the stock refutes at the first step the claim that the stock comes to nothing, which '
            'holds of the actual history (Stationary.model_error).')},
        {'path': TESTING, 'detail': zh_en(
            '反映闭包可以严格大于影响闭包：Prey 中捕食者在猎物的影响闭包之外，量度自身时在其反映闭包之内（Prey.registers_taking）；所反映的'
            '差别对猎物不起作用，猎物不承担自身（Prey.omits），所以这一见证靠被省略的关系。',
            'The registration closure can be strictly larger than the influence closure: in Prey the predator lies beyond '
            'the prey\'s influence closure and, under a gauge of itself, within its registration closure '
            '(Prey.registers_taking); the registered difference does nothing to the prey, which does not bear on itself '
            '(Prey.omits), so the witness rests on omitted relations.')},
    ],
    'limitations': zh_en(
        '形成观察支持之外的任何东西、形成模型、想要检验或知道其反映闭包都不推出；反映相同界定能分辨的，不说一个差别关于什么；一个动作造成什么'
        '是对两段历史的比较，只相对于无此动作之历史的模型才可检验，变动自己的动作并反映差别（实验）没有陈述；他者怎样回应是给出的；多步 '
        'Scope 的桥仍开放；读法是 AI 的，经审查收窄，待 Ren；不含伦理谓词。',
        'That a formation observes anything beyond its support, forms a model, wants to test or knows its registration '
        'closure is not derived; registering alike bounds what can be told apart and says nothing of what a difference is '
        'about; what an act does compares two histories and is testable only relative to a model of the history without '
        'it, and varying one\'s own act and registering the difference (experiment) is not stated; how others respond is '
        'supplied; the multi-step Scope bridge remains open; the readings are the AI\'s, narrowed by the review, pending '
        'Ren; contains no ethical predicate.'),
    'validation_scope': scope('Web.Refutes.not_of_alike、Web.tail_unrefuted、Web.refutesWithin_iff_conjunction、Flow.refutes_tail_within、'
                              'Web.belief_judge_iff、Flow.alike_within_closed、Clearing.tested_by_dweller 与 Clearing.pooled',
                              'Web.Refutes.not_of_alike, Web.tail_unrefuted, Web.refutesWithin_iff_conjunction, '
                              'Flow.refutes_tail_within, Web.belief_judge_iff, Flow.alike_within_closed, '
                              'Clearing.tested_by_dweller and Clearing.pooled'),
    'references': [
        ref(TESTING, 'proof', R_DECLS),
        ref(LOCALITY, 'proof', B('Flow.BalancesOn', 'Flow.Balances.on')),
        ref(FEEDBACK, 'proof', B('Flow.Balances.unregistered_beyond_influence', 'Clearing.sparedFlow',
                                 'Clearing.sparedWeb', 'Clearing.spared_balances', 'Clearing.spared_dependent',
                                 'WithinClosure', 'ClosedUnder', 'closedUnder_withinClosure', 'Web.DependsOn',
                                 'Flow.Exchanges', 'Flow.WithinInfluence')),
        ref(ADMISSION, 'proof', B('Web.Admits', 'Flow.withhold', 'Flow.WithheldLevels')),
        ref(INQUIRY, 'proof', B('commonResponse_judge_iff', 'commonResponse_antitone', 'judgeProcess', 'sees')),
        ref(REGIONS, 'proof', B('Clearing.unsupported_with')),
        ref(ROLES, 'proof', B('Web.SelfBearing', 'Web.Embodied')),
        *SHARED_REFS,
    ],
    'proof_bindings': [binding(TESTING, 'Becoming.Testing'), binding(LOCALITY, 'Becoming.Locality'),
                       binding(FEEDBACK, 'Becoming.Feedback'), binding(ADMISSION, 'Becoming.Admission'),
                       binding(INQUIRY, 'Becoming.Inquiry'), binding(REGIONS, 'Becoming.Regions'),
                       binding(ROLES, 'Becoming.Roles')],
    'next_delta': zh_en(
        '多步 Scope 的桥：感知只经反映的策略在反映相同的流上有同样的所见范围；实验：变动自己的动作并反映差别；模型从哪里来；由动力学给出回应，'
        '而不是假设它；反映关于什么（校准）。',
        'The multi-step Scope bridge: a policy sensing only through registration has the same visible scope on flows '
        'registered alike; experiment: varying one\'s own act and registering the difference; where a model comes from; '
        'responses given by the dynamics rather than assumed; what a registration is about (calibration).'),
    'history': HISTORY,
}

for r in (subthreshold, testing_rec):
    path = RECORDS / f'{r["id"]}.json'
    path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('wrote', path.relative_to(ROOT))

# ---------------------------------------------------------------- becoming-finite-horizon: two corollaries

path = RECORDS / 'becoming-finite-horizon.json'
h = json.loads(path.read_text())
COROLLARIES = B('Renewable.no_exact_finite_reading', 'Renewable.finite_reading_withholds_renewal')
if COROLLARIES[0] not in h['aliases']:
    h['aliases'] += COROLLARIES
    h['claim']['zh'] += ('推论（P49，Becoming.Testing）：没有由前 h 步决定的读法恰是整段的分类（Renewable.no_exact_finite_reading）；'
                         '不认可任何消耗的运行的这种读法，不认可某个更新的运行（Renewable.finite_reading_withholds_renewal）。')
    h['claim']['en'] += (' Corollaries (P49, Becoming.Testing): no reading decided by the first h steps is the whole-run '
                         'classification (Renewable.no_exact_finite_reading); such a reading crediting no consuming run '
                         'withholds credit from some renewing run (Renewable.finite_reading_withholds_renewal).')
    h['references'].insert(0, ref(TESTING, 'proof', COROLLARIES))
    h['proof_bindings'].append(binding(TESTING, 'Becoming.Testing'))
    h['validation_scope']['zh'] += (f'两个推论在 Becoming.Testing 中（同一回执 {RUN}，{N_TESTING} 项定理全部空依赖），经{ORD_ZH}独立审查'
                                    f'（F9）记作本记录的推论。')
    h['validation_scope']['en'] += (f' The two corollaries are in Becoming.Testing (the same receipt {RUN}, all '
                                    f'{N_TESTING} theorems with empty axiom reports), recorded as corollaries of this '
                                    f'record following the {ORD_EN} independent review (F9).')
    h['history'].append(zh_en(
        f'2026-10-11 P49：加入两个推论 Renewable.no_exact_finite_reading 与 finite_reading_withholds_renewal（Becoming.Testing），按{ORD_ZH}'
        f'独立审查 F9 记作本记录的推论，不是另一项成果；原有断言与证明不变；见整合文档 §{SEC}。',
        f'2026-10-11 P49: added the two corollaries Renewable.no_exact_finite_reading and finite_reading_withholds_renewal '
        f'(Becoming.Testing), recorded as corollaries of this record and not as another result, following the {ORD_EN} '
        f'independent review F9; the original claim and proofs are unchanged; see §{SEC} of the integration note.'))
else:
    for r in h['references']:
        if r['path'] == TESTING:
            r['sha256'] = sha(TESTING)
path.write_text(json.dumps(h, ensure_ascii=False, indent=2) + '\n')
print('extended', path.relative_to(ROOT))
