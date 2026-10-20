#!/usr/bin/env python3
"""R34 (20 October 2026), one evaluative chain: the records (run once, before rebind.py).

* D2(a)/F13: new record the-run-classes-and-widening (Becoming.Retaining).
* D2(b): comparison-by-widening states Web.paths_one_object (the condition, significance and C read one
  object, admission).
* D3/F7: held-lives-g0-is-centering gains the law of standpoints as formations with own a closure
  (Web.selfValuation, Becoming.Boundaries).
* D7: alignment-direction-g0-j is rebound to the core schema Becoming.Direction: hypotheses without the retired
  label, a structural title, laws on the spine; the periphery module stays bound as an instance.
* F9: ranking-under-readings and relational-reading-comparison note the restated declarations (worlds read as
  webs).
Hashes of the chapter and the study are set by rebind.py after those are written."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
REC = ROOT / 'theories/becoming/results/records'
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
B = LEAN + 'becoming/Becoming/'
RID = '20261020T005554.047169Z'
RECEIPT = LEAN + f'becoming/becoming-checks/{RID}/verification.json'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
REVIEW = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-TWENTIETH-REVIEW.md'
NOW = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
BOUNDS = ['discrete-steps', 'no-evaluation', 'formal-not-empirical', 'names-provisional', 'omission-not-refutation']
HIST = '20 October 2026, R34 (one evaluative chain: the run classes and widening, one object of admission, standpoints as formations, the direction on a web\'s moves, worlds read as webs):'
HIST_ZH = '2026年10月20日，R34（一条评价之链：整段的类与扩大，接纳这一个对象，以形成为立场，网之动作上的方向，世界读作网）：'


def h(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


def load(i):
    return json.loads((REC / f'{i}.json').read_text())


def save(d):
    (REC / f"{d['id']}.json").write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print('wrote', d['id'])


def binding(src, module):
    return {'source': src, 'receipt': RECEIPT, 'sha256_pointer': '/source_sha256/' + module,
            'success_pointer': '/status', 'success_value': 'passed'}


def ref(path, role, decls=()):
    return {'path': path, 'role': role, 'sha256': h(path), 'declarations': list(decls)}


def t(en, zh):
    return {'en': en, 'zh': zh}


def dep(i, en, zh, out, inp, cond, evidence):
    return {'id': i, 'relation': 'formal-reuse', 'detail': {'en': en, 'zh': zh},
            'interface': {'output': out, 'input': inp, 'conditions': cond, 'evidence': evidence}}


def add_ref(d, path, role, decls, module=None):
    refs = d['references']
    for r in refs:
        if r['path'] == path:
            for x in decls:
                if x not in r['declarations']:
                    r['declarations'].append(x)
            r['sha256'] = h(path)
            break
    else:
        refs.insert(0, ref(path, role, decls))
    if module and d.get('proof_bindings') is not None and not any(b['source'] == path for b in d['proof_bindings']):
        d['proof_bindings'].append(binding(path, module))
    if not any(r['path'] == RECEIPT for r in refs):
        refs.append(ref(RECEIPT, 'receipt'))


def note(d, en, zh):
    d.setdefault('history', []).append({'en': HIST + ' ' + en, 'zh': HIST_ZH + zh})


def check_caps(d):
    for k, (ce, cz) in {'title': (100, 40), 'statement': (300, 150), 'validation_scope': (600, 260),
                        'next_delta': (400, 180)}.items():
        if k in d:
            assert len(d[k]['en']) <= ce and len(d[k]['zh']) <= cz, (d['id'], k, len(d[k]['en']), len(d[k]['zh']))
    for k, (ce, cz) in {'laws': (420, 190), 'hypotheses': (420, 190), 'does_not_show': (240, 110)}.items():
        for x in d.get(k, []):
            if len(x['en']) > ce or len(x['zh']) > cz:  # list caps only warn (style.HARD_CAPS)
                print('warn: over the cap', d['id'], k, x['en'][:50], len(x['en']), len(x['zh']))


# ---------------------------------------------------------------- D2(a): the run classes and widening
RET = B + 'Retaining.lean'
fl = lambda *xs: ['Becoming.Flow.Balances.' + x for x in xs]
RUN = {
    'schema_version': 2,
    'id': 'the-run-classes-and-widening',
    'title': t('The run classes and widening', '整段的类与扩大'),
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': NOW,
    'statement': t(
        "Where only active formations take, a part whose draws fall on conditions renewed over the run does not "
        "narrow what can form, and a consumed dependence the levels without a part meet makes a part that opens "
        "nothing narrow. Neither class decides alone.",
        '只有活跃的形成取用时，汲取都落在整段上被更新之条件上的部分不缩小能形成者；无此部分的水平所满足的被消耗依存，使不打开什么的部分缩小。两个类单独都不决定。'),
    'laws': [
        {**t("In a balanced flow where only active formations take, and only from what they draw on, let every "
             "condition a member of a part draws on at some step be renewed over the run (every dependence on it "
             "kept at every step). Then the levels with the part include those without it, so the part does not "
             "narrow; a part of formations renewing over the run is a case.",
             '在平衡的流中，只有活跃的形成取用，且只从它所汲取者取用；设部分的成员在某步所汲取的每个条件都在整段上被更新（对它的每个依存在每步都被满足）。则有此部分的水平包含无它的水平，部分不缩小；整段上更新的形成所成的部分是一个情形。'),
         'declarations': fl('includes_of_renewed', 'not_narrows_of_renewed', 'includes_of_renewingIn')},
        {**t("Let a dependence held at T be met at no step after it, let the part give each condition at every step "
             "no more than it takes, and let the levels without the part admit at a later step the formation whose "
             "dependence it was, held there at no smaller need. Then the levels without the part widen those with it.",
             '设一个在 T 被持有的依存此后在任何一步都不被满足，部分在每步对每个条件所给不多于所取，无此部分的水平在后来某步接纳其依存所属的形成、该依存在那里以不小的所需被持有。则无此部分的水平扩大有它的水平。'),
         'declarations': fl('narrows_of_consumed')},
        {**t("The stepwise class does not decide: in Preemption the drawer's event at the first step is within "
             "renewal, the drawer is consuming over the run and does not renew over it, and the levels without its "
             "part widen those with it.",
             '逐步的类不决定：Preemption 中汲取者在第一步的事件在更新之内，汲取者在整段上是消耗的、不更新，无其部分的水平扩大有它的水平。'),
         'declarations': ['Becoming.Preemption.renewingAt_consuming_narrows', 'Becoming.Preemption.within_renewal_yet_loses']},
        {**t("The consuming class alone does not narrow: in Untaken a formation draws on a condition that stays at "
             "zero below its need, so it is consuming over the run, yet nothing is taken or given, the flow balances, "
             "and the levels with and without its part keep what can form the same.",
             '单是消耗的类不缩小：Untaken 中一个形成汲取一个始终为零、低于其所需的条件，所以它在整段上是消耗的；但没有取用与给予，流平衡，有无其部分的水平保持能形成者相同。'),
         'declarations': ['Becoming.Untaken.flow', 'Becoming.Untaken.web', 'Becoming.Untaken.part',
                          'Becoming.Untaken.consuming_keeps']},
    ],
    'hypotheses': [
        t("Balance (Flow.Balances); only active formations take, and only from what they draw on (Flow.Taking); the "
          "levels without the part (WithheldLevels). The consuming law needs no Taking but needs the part to give no "
          "more than it takes and the levels without it to meet the consumed dependence later.",
          '平衡（Flow.Balances）；只有活跃的形成取用，且只从它所汲取者取用（Flow.Taking）；无此部分的水平（WithheldLevels）。消耗之律不需 Taking，但需部分所给不多于所取，且无它的水平后来满足被消耗的依存。'),
        t("Discrete steps from step zero; natural-number levels, needs and amounts; a part is a decided family "
          "(part : F → Bool); a formation's class over a run is read with identity fixed by naming.",
          '离散的步，从第零步起；自然数的水平、所需与量；部分是可判定的族（part : F → Bool）；形成在整段上的类以命名所定的同一来读。'),
    ],
    'does_not_show': [
        {**t("That renewing widens: keeping what can form is not widening; whether a part opens anything is its net give.",
             '更新即扩大：保持能形成者不是扩大；部分是否打开什么在于它的净给予。'), 'kind': 'non-implication'},
        {**t("That consuming alone narrows: Untaken is consuming and keeps what can form.",
             '单是消耗就缩小：Untaken 是消耗的，却保持能形成者。'), 'kind': 'non-implication',
         'witness': 'Becoming.Untaken.consuming_keeps'},
        {**t("That being within renewal at a step keeps what can form: Preemption's drawer is, and its part narrows.",
             '一步上在更新之内就保持能形成者：Preemption 的汲取者如此，其部分却缩小。'), 'kind': 'non-implication',
         'witness': 'Becoming.Preemption.renewingAt_consuming_narrows'},
        {**t('The class of arising over a run and the order; a valuation of either class.',
             '整段上生起的类与次序；对任一类的评价。'), 'kind': 'scope'},
    ],
    'counterexamples': [
        {'path': RET, 'detail': t('Within renewal at a step, consuming over the run, narrowing: Preemption (renewingAt_consuming_narrows).',
                                  '一步上在更新之内、整段上消耗、缩小：Preemption（renewingAt_consuming_narrows）。')},
        {'path': RET, 'detail': t('Consuming over the run and keeping what can form: Untaken (consuming_keeps).',
                                  '整段上消耗而保持能形成者：Untaken（consuming_keeps）。')},
    ],
    'standard_boundaries': BOUNDS,
    'validation_scope': t(
        f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {RID}): the cited declarations of '
        'Becoming.Retaining have empty axiom reports; the checker verifies core purity. Author self-review in study '
        'section 225; not independently reviewed.',
        f'Lean 4.29.1 合并检查器实查（回执 {RID}）：所引 Becoming.Retaining 的声明公理报告为空；检查器并核对核心纯净。作者自审见研究第 225 节；未经独立审查。'),
    'next_delta': t(
        'The class of arising over a run and the order; identity from continuity rather than naming, on which a '
        'class over a run depends; an independent review.',
        '整段上生起的类与次序；由延续而非命名的同一（整段上的类依赖它）；独立审查。'),
    'correspondence': t(
        "The twentieth review's D2 and F13 asked how a part's class over a run relates to its widening, under named "
        "premises with Preemption as the boundary. The answer is one direction each: renewal over the run closes "
        "nothing where only active formations take, and a consumed dependence narrows where the levels without the "
        "part meet it; the stepwise class and the consuming class alone each have a witness against them. Reading "
        "(the AI's, D2 revised): renewing and consuming are classes of a formation over a run, related to the order "
        "by these laws, not the formation-level meaning of generative and degenerative.",
        '第二十次审查的 D2 与 F13 问：在写明的前提下、以 Preemption 为界，部分在整段上的类与它的扩大怎样相关。答案是各一个方向：只有活跃的形成取用时，整段上的更新不关闭什么；无此部分的水平满足被消耗的依存时，它缩小；逐步的类与单是消耗的类各有反例。读法（AI 的，D2 修订）：更新与消耗是形成在整段上的类，经这些规律与次序相关，不是生成的与退化的在形成层次上的含义。'),
    'canonical_source': RET,
    'aliases': ['the run classes and widening', '整段的类与扩大',
                'Becoming.Flow.Balances.not_narrows_of_renewed', 'Becoming.Flow.Balances.narrows_of_consumed'],
    'dependencies': [
        dep('four-cases-of-a-part',
            'Reuses the four cases (Web.Widens, Web.Includes) and Flow.Balances.opens_nothing, the withheld levels and their balance.',
            '复用四种情形（Web.Widens、Web.Includes）与 Flow.Balances.opens_nothing、被扣下的水平及其平衡。',
            t('The order on what can form and when a part opens nothing.', '能形成者上的次序，及部分何时不打开什么。'),
            t('What the run classes are related to.', '整段的类与之相关者。'),
            t('Balance; the levels without the part.', '平衡；无此部分的水平。'), RET),
        dep('significance-retained-within-margin',
            'Reuses Preemption and within_renewal_yet_loses, the witness that renewal at a step is no sign of keeping.',
            '复用 Preemption 与 within_renewal_yet_loses，即一步上的更新不是保持之标志的见证。',
            t('The preempting drawer within renewal whose part loses.', '在更新之内而其部分失去的先占汲取者。'),
            t('The boundary of the run-class law: the stepwise class overlaps the run class there.', '整段类之律的边界：逐步的类在那里与整段的类重叠。'),
            t('None beyond the witness.', '见证之外无。'), RET),
        dep('life-as-condition-of-life',
            'Reuses the run classes of a web: Web.Renewed, Web.Consumed, Web.ConsumingIn and Web.RenewingIn.',
            '复用网的整段之类：Web.Renewed、Web.Consumed、Web.ConsumingIn 与 Web.RenewingIn。',
            t("A formation's class over a run.", '形成在整段上的类。'),
            t('What a part whose members renew or whose dependence is consumed does to what can form.', '成员更新或依存被消耗的部分对能形成者做什么。'),
            t('Identity fixed by naming.', '同一由命名所定。'), RET),
    ],
    'related': [{'id': 'comparison-by-widening', 'detail': t(
        'On level paths the condition, significance and C read one object, admission; the run classes are related to that order here.',
        '在水平路径上，条件、意义与 C 读同一个对象，即接纳；这里整段的类与这一次序相关。')}],
    'references': [
        ref(RET, 'proof', fl('includes_of_renewed', 'not_narrows_of_renewed', 'includes_of_renewingIn', 'narrows_of_consumed')
            + ['Becoming.Preemption.renewingAt_consuming_narrows', 'Becoming.Preemption.within_renewal_yet_loses',
               'Becoming.Untaken.flow', 'Becoming.Untaken.web', 'Becoming.Untaken.part', 'Becoming.Untaken.consuming_keeps']),
        ref(RECEIPT, 'receipt'), ref(STUDY, 'integration'), ref(CHAPTER, 'statement'), ref(REVIEW, 'provenance'),
    ],
    'proof_bindings': [binding(RET, 'Becoming.Retaining')],
    'history': [t(
        '20 October 2026: added (R34, D2 and F13 of the twentieth review): the run classes related to widening under '
        'named premises, with Preemption and Untaken as boundaries; study section 225.',
        '2026年10月20日：新增（R34，第二十次审查 D2 与 F13）：整段的类在写明的前提下与扩大相关，以 Preemption 与 Untaken 为界；研究第 225 节。')],
}
check_caps(RUN)
save(RUN)

# ---------------------------------------------------------------- D2(b): one object, admission
REL = B + 'Relevance.lean'
C = load('comparison-by-widening')
C['claim']['en'] = C['claim']['en'].rstrip() + (
    " The three are one object, admission (Web.paths_one_object): the continuation condition is living significance "
    "on level paths with every claim living and significance from every standpoint as the relevance, C's extension "
    "there with every claim counted is widening, and under the condition widening is retaining and adding what has "
    "significance from any standpoint. The condition fixes which admissions count; C read as widening orders them.")
C['claim']['zh'] = C['claim']['zh'].rstrip() + (
    '三者是同一个对象，即接纳（Web.paths_one_object）：延续条件是水平路径上以每个主张为活、以从每个立场的意义为相关的生命意义；C 在那里计入每个主张的延伸就是扩大；'
    '在条件之下，扩大就是从任一立场保留并增加有意义者。条件定哪些接纳计入；读作扩大的 C 为它们定次序。')
assert len(C['claim']['en']) <= 1500 and len(C['claim']['zh']) <= 700, (len(C['claim']['en']), len(C['claim']['zh']))
C['aliases'].append('Becoming.Web.paths_one_object')
add_ref(C, REL, 'proof', ['Becoming.Web.paths_one_object'], 'Becoming.Relevance')
note(C, 'Web.paths_one_object added to the claim (D2(b) of the twentieth review: the condition, significance and C read one object, admission); its proof binding to Relevance.lean is at the R34 receipt. The earlier claim is unchanged.',
     '主张中加入 Web.paths_one_object（第二十次审查 D2(b)：条件、意义与 C 读同一个对象，即接纳）；它在 Relevance.lean 的证明绑定在 R34 的回执上。原有主张不变。')
save(C)

# ---------------------------------------------------------------- D3/F7: standpoints as formations
BND = B + 'Boundaries.lean'
H = load('held-lives-g0-is-centering')
sv = lambda *xs: ['Becoming.Web.' + x for x in xs]
H['laws'].append({**t(
    "With the formations as standpoints, each one's own region its closure under any relation of the unfolding and "
    "living and related the stepwise reading, sig is the only evaluative parameter supplied. The own region is the "
    "least boundary; every event is held, so living significance is self-significance with standpoint neutrality; "
    "the empty relation gives the case above, feeding the feeding closure.",
    '以形成为立场，各自的自身区域取它在展开的任一关系下的闭包，living 与 related 取逐步读法，则 sig 是唯一给出的评价参数。自身区域是最小边界；每个事件都被持有，所以生命意义是自身意义加立场中立；空关系给出上面的情形，供给给出供给闭包。'),
    'declarations': sv('selfValuation', 'selfValuation_own_least', 'selfValuation_held', 'selfValuation_significant_iff',
                       'selfValuation_empty_own', 'selfValuation_feeding_own', 'selfValuation_of_unrestricted')})
H['hypotheses'].append(t(
    "Standpoints as formations: the laws on valuations hold for any type of standpoints, and this is the instance "
    "Pos := F; which relation a center's region is drawn along is supplied, read off the unfolding, not derived.",
    '以形成为立场：评价之律对任何类型的立场成立，这是实例 Pos := F；中心的区域沿哪个关系划出是给出的，从展开读出，不是推出的。'))
add_ref(H, BND, 'proof', sv('selfValuation', 'selfValuation_own_least', 'selfValuation_held', 'selfValuation_significant_iff',
                            'selfValuation_empty_own', 'selfValuation_feeding_own', 'selfValuation_of_unrestricted'),
        'Becoming.Boundaries')
check_caps(H)
note(H, "A law added (D3 and F7 of the twentieth review): standpoints as formations with each one's own region its closure under a relation of the unfolding (Web.selfValuation and its laws, Boundaries.lean), so that sig is the only supplied evaluative parameter; with a premise naming the instance. The earlier laws are unchanged.",
     '新增一条规律（第二十次审查 D3 与 F7）：以形成为立场，各自的自身区域取它在展开的某个关系下的闭包（Web.selfValuation 及其规律，Boundaries.lean），使 sig 是唯一给出的评价参数；另加一条写明该实例的前提。原有规律不变。')
save(H)

# ---------------------------------------------------------------- D7: the direction on a web's moves
DIR = B + 'Direction.lean'
dr = lambda *xs: ['Becoming.Direction.' + x for x in xs]
A = load('alignment-direction-g0-j')
A['title'] = t('AI alignment direction under widening and the practical commitments', '扩大与实践承诺之下的 AI 对齐方向')
A['hypotheses'] = [
    t("The continuation condition fixes scope: every admission compared is a continuation with significance from every "
      "standpoint (Web.paths_one_object). C read as widening orders. J1–J4: J1/J2 as Priority on the moves' frame; for "
      "J3/J4 the moves listed, the comparison weakly decided and the admission decided. The core schema does not use "
      "the condition.",
      '延续条件定范围：所比较的每个接纳都是从每个立场有意义的延续（Web.paths_one_object）。读作扩大的 C 定次序。J1–J4：J1/J2 是动作之框架上的 Priority；J3/J4 需动作列出、比较弱可判定、接纳可判定。核心模式不用条件。'),
    t("The pool part takes the premises of Flow.act_selected_by_pool: balance, the rest following one law of exchange "
      "reading through coupling, the part acting alike within its group's coupling closure. Reading a move by the levels "
      "it leads to is the AI's. E includes warrant for basic classifications, actual protection, valid undertakings and "
      "authority.",
      '合起来之耦合的部分取 Flow.act_selected_by_pool 的前提：平衡，其余依循一条经耦合读取的交换之律，部分在其组的耦合闭包内同样行动。以所导向的水平读动作是 AI 的。E 包括基本分类、实际保护、有效承担及权限的根据。'),
]
A['laws'] = [
    {**t("On a web, moves are read by the levels they lead to and a claim is a formation at a step, realized where those "
         "levels admit it. One move's outcome extends another's, with every admission counted, exactly where it widens it.",
         '在网上，动作以其所导向的水平来读，主张是某步上的形成，在这些水平接纳它之处实现。一个动作的结果延伸另一个的（计入每个接纳），恰在它扩大后者之处。'),
     'declarations': dr('frame', 'options_iff', 'extension_iff_widens')},
    {**t("Under J1/J2 on the moves' frame, a chosen move keeps the basic admissions some move keeps, and with the moves "
         "listed, the comparison weakly decided and the admission decided, that admission is required of the choice.",
         '在动作框架上的 J1/J2 之下，被选的动作保持某个动作所保持的基本接纳；动作列出、比较弱可判定、接纳可判定时，这一接纳是选择所要求的。'),
     'declarations': dr('chosen_keeps_basic', 'kept_required')},
    {**t("Under J1/J2, a move whose outcome another move's outcome widens is not chosen, wherever it is decided whether "
         "the widening adds a basic admission; with no decision, the widening move is never refuted to be better.",
         '在 J1/J2 之下，一个动作的结果被另一个的结果扩大时，凡扩大是否增加基本接纳可判定之处，它不被选；无此判定时，扩大者更好从不被否定。'),
     'declarations': dr('narrowed_not_chosen', 'widening_not_not_better')},
    {**t("With the rest following one law of exchange reading through coupling, the admission that tells two moves apart "
         "lies beyond the acting group's coupling closure and is selected through the pooled coupling of every group "
         "holding that formation, and of no group within the closure.",
         '其余依循一条经耦合读取的交换之律时，区分两个动作的接纳在行动组的耦合闭包之外，经持有该形成的每个组的合起来的耦合被选择，而不经闭包之内任何组的。'),
     'declarations': dr('widening_selected_by_pool')},
    {**t("In Clearing, sparing the habitat widens clearing; under J1/J2 with no basic admission clearing is not chosen, and "
         "the dweller's admission is selected through every pool holding the dweller and through no pool within the "
         "clearer's coupling closure.",
         'Clearing 中，保留栖地扩大清除；在无基本接纳的 J1/J2 之下清除不被选，栖居者的接纳经持有栖居者的每个组被选择，而不经清除者耦合闭包之内的任何组。'),
     'declarations': ['Becoming.Clearing.spareOutcome', 'Becoming.Clearing.spared_widens', 'Becoming.Clearing.direction']},
]
add_ref(A, DIR, 'proof', dr('frame', 'options_iff', 'extension_iff_widens', 'chosen_keeps_basic', 'kept_required',
                            'narrowed_not_chosen', 'widening_not_not_better', 'widening_selected_by_pool')
        + ['Becoming.Clearing.spareOutcome', 'Becoming.Clearing.spared_widens', 'Becoming.Clearing.direction'],
        'Becoming.Direction')
add_ref(A, REL, 'proof', ['Becoming.Web.paths_one_object'], 'Becoming.Relevance')
A['aliases'] += ['Becoming.Direction.narrowed_not_chosen', 'Becoming.Direction.widening_selected_by_pool']
A['does_not_show'] = A['does_not_show'] + [
    {**t("That a system chooses so: the schema says what any comparison meeting J1/J2 chooses on a web's moves.",
         '某个系统如此选择：这一模式说的是任何满足 J1/J2 的比较在网的动作上选什么。'), 'kind': 'non-implication'},
    {**t("A World's exchanges read as the family of moves, or the periphery case as a formal core instance.",
         'World 的交换读作这一族动作，或外围案例作为核心中的形式实例。'), 'kind': 'scope'},
]
A['does_not_show'][2] = {**t('It does not prove axiom-free necessity of the continuation condition or of C.',
                             '不证明延续条件或 C 的无公理必然性。'), 'kind': 'scope'}
A['dependencies'][0]['interface']['output'] = t('Comparison and bounded practical principles under the practical commitments J.',
                                                '实践承诺 J 下的比较与有界实践原则。')
A['dependencies'] += [
    dep('comparison-by-widening', 'Reuses C read as widening on level paths and the one object of admission (Web.paths_one_object).',
        '复用水平路径上读作扩大的 C 与接纳这一个对象（Web.paths_one_object）。',
        t('C read as widening; under the condition, every admission a continuation with significance.', '读作扩大的 C；在条件之下，每个接纳都是有意义的延续。'),
        t("The order on a web's moves.", '网之动作上的次序。'),
        t('The reading that better is widening, an open warrant.', '“更好”即扩大的读法，其根据开放。'), DIR),
    dep('what-pooled-coupling-reaches', 'Reuses Flow.act_selected_by_pool: what a selection through a pool reaches beyond the actor.',
        '复用 Flow.act_selected_by_pool：经组的选择在行动者之外及于什么。',
        t("Selection through pooled coupling of an act's difference beyond the actor's closure.", '行动者闭包之外动作差别经合起来的耦合的选择。'),
        t('Where the admission that tells two moves apart is selected.', '区分两个动作的接纳在何处被选择。'),
        t('The law of exchange reads through coupling; balance.', '交换之律经耦合读取；平衡。'), DIR),
]
A['progress'].append({**t(
    "Core schema: on a web's moves, under C read as widening and J1/J2, a narrowed move is not chosen, and the "
    "admission that tells it apart is selected only through a pool coupled into it; Clearing is the instance.",
    '核心模式：在网的动作上，于读作扩大的 C 与 J1/J2 之下，被缩小的动作不被选，区分它的接纳只经耦合入它的组被选择；Clearing 是实例。'),
    'source': STUDY + '#225-one-evaluative-chain-r34'})
A['overview']['evidence']['en'] += (" On the spine, a core schema states the direction on a web's moves under C read as "
                                    "widening and the practical commitments, with what tells two moves apart selected "
                                    "only through a pool coupled into it.")
A['overview']['evidence']['zh'] += '在脊柱上，一个核心模式在读作扩大的 C 与实践承诺之下陈述网之动作上的方向，区分两个动作者只经耦合入它的组被选择。'
A['validation_scope'] = t(
    A['validation_scope']['en'].rstrip() + f' The core schema (Becoming.Direction) is machine-checked with empty axiom reports (receipt {RID}); not independently reviewed.',
    A['validation_scope']['zh'].rstrip() + f'核心模式（Becoming.Direction）经实查，公理报告为空（回执 {RID}）；未经独立审查。')
for r in A['references']:
    if r['path'] == CHAPTER or r['path'] == STUDY:
        break
else:
    A['references'].append(ref(STUDY, 'integration'))
check_caps(A)
note(A, "Rebound to the core (D7 of the twentieth review): the direction is a core schema on a web's moves under C read as widening and J1–J4, with its pool part and the Clearing instance (Direction.lean, bound to the R34 receipt), stated as laws; the hypotheses name the continuation condition for scope and C for order in place of the retired label G0; title restated structurally (was \"AI alignment direction from living significance and the practical commitments\"). The periphery module AlignmentDirection.lean stays bound as an instance by reading (its comparison is BasicPriority, which on a frame is Priority). The argument's claim and scope are unchanged.",
     '改绑到核心（第二十次审查 D7）：方向是网之动作上的核心模式，在读作扩大的 C 与 J1–J4 之下，连同合起来之耦合的部分与 Clearing 实例（Direction.lean，绑定 R34 回执），写作规律；前提以延续条件定范围、以 C 定次序，取代退役的标签 G0；标题改为结构性的（原为“生生之意义与实践承诺下的 AI 对齐方向应用”）。外围模块 AlignmentDirection.lean 按读法仍作为实例绑定（其比较是 BasicPriority，在框架上即 Priority）。论证的主张与范围不变。')
save(A)

# ---------------------------------------------------------------- F9: restatements
R = load('ranking-under-readings')
R['dependencies'][1]['detail'] = t(
    'stepwise is exactly the living of Web.valuation (Ranking.stepwise_iff, now in Becoming.Relevance), on the web each world is; a foundation law\'s unfolding is read as a web through Web.static where a course is built from it.',
    'stepwise 恰是 Web.valuation 的 living（Ranking.stepwise_iff，现在 Becoming.Relevance 中），在每个世界所是的网上；由基础定律构造进程时，其展开经 Web.static 读作网。')
note(R, "F9 of the twentieth review: the readings' worlds are webs (W → Web F C) in place of foundation unfoldings, so the declarations it cites from Ranking and Relevance state Web.Renewed, Web.Dependent and Web.ConsumingIn where they stated RelationalRenewal's (restatements listed old → new in study section 225); the courses built from the foundation's laws read them through Web.static. Ranking now imports neither Metaethics nor ValuationFrames, and Ranking.stepwise_iff moved to Relevance. The claim is unchanged.",
     '第二十次审查 F9：各读法的世界是网（W → Web F C），不再是基础的展开，所以所引 Ranking 与 Relevance 的声明陈述 Web.Renewed、Web.Dependent 与 Web.ConsumingIn，取代 RelationalRenewal 的（重述逐条列于研究第 225 节）；由基础定律构造的进程经 Web.static 读取。Ranking 不再导入 Metaethics 与 ValuationFrames，Ranking.stepwise_iff 移到 Relevance。论断不变。')
save(R)
Q = load('relational-reading-comparison')
note(Q, "F9 of the twentieth review: Ranking's and ActiveReading's worlds are webs, so the cited Ranking.wholeRun_of_renewed, renewed_extends_iff, renewed_active_extends_iff and ActiveReading.livingSignificance_wholeRun_iff state Web.Renewed and Web.ConsumingIn in place of RelationalRenewal's (study section 225); ActiveReading.livingSignificance_wholeRun_web_iff, the same statement once the world is a web, was removed (development/r34-evaluative-chain/RENAME-TABLE.json). The claim is unchanged.",
     '第二十次审查 F9：Ranking 与 ActiveReading 的世界是网，所以所引 Ranking.wholeRun_of_renewed、renewed_extends_iff、renewed_active_extends_iff 与 ActiveReading.livingSignificance_wholeRun_iff 陈述 Web.Renewed 与 Web.ConsumingIn，取代 RelationalRenewal 的（研究第 225 节）；ActiveReading.livingSignificance_wholeRun_web_iff 在世界是网之后是同一陈述，已删去（development/r34-evaluative-chain/RENAME-TABLE.json）。论断不变。')
save(Q)
