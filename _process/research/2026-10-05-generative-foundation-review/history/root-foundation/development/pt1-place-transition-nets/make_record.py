#!/usr/bin/env python3
"""Write PT1's record: python3 -B make_record.py CORE_RECEIPT   (from the checkout root, after apply_text.py)

Every declaration cited is resolved against the receipt's audited declarations of the module (a short name must match
exactly one declaration by suffix), and the receipt must bind the module's current bytes."""
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
PROVENANCE = 'drafts/2026-10-10-opening/history/OPENING-V7-PROPOSAL.md'
RECORDS = ROOT / 'theories/becoming/results/records'
MOD = 'PlaceTransitionNets'
RID = 'place-transition-nets-on-the-spine'
core_id = sys.argv[1]
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
section = re.search(r'^## (\d+)\. Place/transition nets on the spine \(PT1\)$', (ROOT / STUDY).read_text(), re.M)
assert section, 'study section missing'
N = section.group(1)


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def src(mod):
    return f'{PKG}/Becoming/{mod}.lean'


m = next(m for m in core['modules'] if m['module'] == f'Becoming.{MOD}')
assert core['source_sha256'][f'Becoming.{MOD}'] == sha(src(MOD)), 'receipt does not bind the module'
assert not any(m['axiom_dependencies'].values())
FULL = [d['name'] for d in m['declarations']]
n_decl, n_thm = len(FULL), m['theorems']


def resolve(names):
    out = []
    for n in names:
        hits = [f for f in FULL if f == 'Becoming.' + n or f.endswith('.' + n)]
        assert len(hits) == 1, (n, hits)
        out.append(hits[0])
    return out


def dep(rid, en, zh, out_en, out_zh, in_en, in_zh, cond_en, cond_zh, evidence):
    return {'id': rid, 'relation': 'formal-reuse', 'detail': {'en': en, 'zh': zh},
            'interface': {'output': {'en': out_en, 'zh': out_zh}, 'input': {'en': in_en, 'zh': in_zh},
                          'conditions': {'en': cond_en, 'zh': cond_zh}, 'evidence': evidence}}


STATEMENT = {
    'en': 'Place/transition nets, defined by their own rules, are an instance of the spine: the flow balances the '
          'markings exactly on firing sequences, and dissipation is exactly a strict P-subinvariant on what fires; so '
          'rising with falling, bounded taking, rest and the siphon law hold of such nets.',
    'zh': '按自身规则定义的库所/变迁网是脊柱的一个实例：其流恰在发生序列上与标识平衡，耗散恰是所发生变迁上的严格 P-子不变量；'
          '于是此类网上有涨落同在、取用有界、静止与虹吸律。'}
assert len(STATEMENT['en']) <= 300, len(STATEMENT['en'])

LAWS = [
    ('The net is a law of exchange reading nothing, whose course along a schedule is the net\'s flow and whose levels '
     'along a firing sequence are its markings in units.',
     '网是什么也不读的交换律，它沿一个调度生成的进程就是网的流，沿发生序列它生成的水平就是按单位计的标识。',
     ['Net.law', 'Net.flow', 'Net.web', 'Net.law_nonanticipating', 'Net.course_eq', 'Net.Fires.levels_eq',
      'Net.levels_eq_of_enabled']),
    ('Balance is the firing rule: along a firing sequence the flow balances the markings in any units, and with every '
     'weight positive it balances exactly where the schedule is a firing sequence.',
     '平衡就是发生规则：沿发生序列，流在任何单位下与标识平衡；各权为正时，恰在调度是发生序列之处平衡。',
     ['Net.Fires.balances', 'Net.balances_iff', 'Net.balance_at_iff']),
    ('Enabling gives the law\'s feasibility, so course_balances_iff applies; feasibility is enabling exactly for pure '
     'nets fired one transition at a time, and a catalyst and a concurrent step are feasible and do not fire.',
     '使能推出该律的可行性，因而 course_balances_iff 适用；可行性恰在纯网逐个发生变迁时等于使能，催化剂与并发一步可行而不发生。',
     ['Net.Fires.feasible', 'Net.Fires.course_balances', 'Net.fires_iff_feasible', 'Net.catalyst_feasible_not_fires',
      'Net.relay_feasible_not_fires']),
    ('Only active transitions give and take, and only from what they draw on; along a firing sequence activity needs '
     'support.',
     '只有活动的变迁给出与取用，且只取其所汲取者；沿发生序列，活动需要支撑。',
     ['Net.acting', 'Net.taking', 'Net.Fires.dependent']),
    ('With finitely many places listed once, the flow is dissipative exactly where every fired transition loses '
     'weighted tokens, which a strict P-subinvariant gives; every step is enclosed.',
     '有限多个库所各列一次时，流恰在每个所发生变迁都损失加权令牌之处耗散，严格 P-子不变量给出这一点；每一步都被包围。',
     ['Net.Loses', 'Net.StrictSubinvariant', 'Net.Loses.of_lt', 'Net.dissipative_iff',
      'Net.StrictSubinvariant.dissipative', 'Net.enclosed', 'Net.total_eq_closed']),
    ('Along such a firing sequence a place rises only as another falls, the consuming firings number at most the '
     'initial weighted tokens and do not recur, and that the marking stops changing cannot be refuted.',
     '沿这样的发生序列，一个库所只随另一库所下降而上升，取用的发生次数不超过初始加权令牌且不复现，标识停止变化不可被驳倒。',
     ['Net.rise_with_fall', 'Net.rise_with_fall_tokens', 'Net.takers_within', 'Net.taking_not_recurring',
      'Net.change_stops_unrefuted', 'Net.marking_stops_unrefuted']),
    ('Read as a world of places and transitions with finitely many transitions, every premise of '
     'World.rests_unrefuted_enclosed holds, so that the world rests from some step on cannot be refuted.',
     '读作库所与变迁的世界、变迁有限时，World.rests_unrefuted_enclosed 的每个前提都成立，因而世界从某步起静止不可被驳倒。',
     ['Net.world', 'Net.Fires.world_balanced', 'Net.world_embodied', 'Net.world_counted', 'Net.world_dissipative',
      'Net.world_enclosed', 'Net.rests_unrefuted']),
    ('The siphon law is the joint-excess law: where every producer of a place consumes at least m from it, joint excess '
     'starting below n + m leaves every transition consuming m from it dead; an empty such place stays empty.',
     '虹吸律就是共同过量律：一个库所的每个生产者都从它取至少 m 时，起于 n + m 之下的共同过量使每个从它取 m 的变迁此后不再发生；'
     '这样的空库所保持为空。',
     ['Net.Gated', 'Net.Gated.gates', 'Net.gated_ends', 'Net.siphon_empty']),
]

COUNTER = [
    {'path': src(MOD), 'detail': {
        'en': 'The conservative cycle (Net.cycle): one token moved back and forth between two places fires forever; every '
              'premise of the rest law holds but dissipation (cycle_premises, cycle_not_dissipative), its marking changes '
              'at every step (cycle_changes) and its world never rests (cycle_never_rests).',
        'zh': '守恒循环（Net.cycle）：一个令牌在两个库所之间来回移动，永远发生；静止律除耗散外的每个前提都成立（cycle_premises、'
              'cycle_not_dissipative），其标识每步变化（cycle_changes），其世界永不静止（cycle_never_rests）。'}},
    {'path': src(MOD), 'detail': {
        'en': 'The fed place (Net.fed): refilled by a transition that does not consume it, it is not gated; its flow '
              'balances and one step of joint excess starts below 1 + 1, yet a transition requiring it is active two '
              'steps later, so the conclusion of Flow.joint_excess_ends fails (fed_fires, fed_refills).',
        'zh': '被供给的库所（Net.fed）：被一个不从它取用的变迁补充，因而不受门控；其流平衡，一步共同过量起于 1 + 1 之下，而两步后一个'
              '需要它的变迁仍活动，所以 Flow.joint_excess_ends 的结论不成立（fed_fires、fed_refills）。'}},
]
resolve(['Net.cycle', 'Net.cycle_premises', 'Net.cycle_not_dissipative', 'Net.cycle_changes', 'Net.cycle_never_rests',
         'Net.fed', 'Net.fed_fires', 'Net.fed_refills'])

BOUNDS = ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical', 'names-provisional',
          'omission-not-refutation']

DEPS = [
    dep('counterfactual-is-the-course',
        'Uses ExchangeLaw.course, levels_succ, Feasible and course_balances_iff for the net\'s law.',
        '对网的律使用 ExchangeLaw.course、levels_succ、Feasible 与 course_balances_iff。',
        'The course a law of what has stood generates balances exactly where it is feasible.',
        '读已成者之律所生成的进程恰在可行处平衡。',
        'The net\'s course along a firing sequence balances on the levels it generates.',
        '网沿发生序列的进程在其生成的水平上平衡。',
        'The net\'s law reads what has stood (it reads nothing); the schedule is a firing sequence.',
        '网的律读已成者（它什么也不读）；调度是发生序列。', src('Counterfactual')),
    dep('rising-and-falling-in-one-exchange',
        'Instantiates Flow.rise_with_fall on the net\'s flow and web.',
        '在网的流与网络上实例化 Flow.rise_with_fall。',
        'In a balanced flow, a member of a family dissipated on that rises has another that falls.',
        '在平衡的流中，被耗散之族的一个成员上升，则另一成员下降。',
        'A place rising across a step of a firing sequence whose fired transitions lose has another falling.',
        '在所发生变迁皆损失的发生序列的一步上，一个库所上升则另一个下降。',
        'Fires (balance); every fired transition loses over the places (dissipated on).',
        '发生（平衡）；每个所发生变迁在诸库所上损失（被耗散）。', src('Dissipation')),
    dep('no-finite-part-bears-taking',
        'Instantiates Flow.Balances.takers_within and Flow.Dissipative.finite_taking_not_recurring.',
        '实例化 Flow.Balances.takers_within 与 Flow.Dissipative.finite_taking_not_recurring。',
        'Dissipated on from a step, the takers over a stretch number at most the stock; with finitely many '
        'conditions taking does not recur.',
        '自某步起被耗散，一段中的取用者不多于存量；条件有限时取用不复现。',
        'The consuming firings are bounded by the initial weighted tokens and do not recur.',
        '取用的发生次数以初始加权令牌为界且不复现。',
        'Fires; every fired transition loses; finitely many places listed once.',
        '发生；每个所发生变迁损失；有限多个库所各列一次。', src('Dissipation')),
    dep('continued-change-needs-openness',
        'Instantiates Flow.change_stops_unrefuted_around and World.rests_unrefuted_enclosed.',
        '实例化 Flow.change_stops_unrefuted_around 与 World.rests_unrefuted_enclosed。',
        'Under balance, dissipation, a census and enclosure, that change stops (the world rests) cannot be refuted.',
        '在平衡、耗散、普查与包围之下，变化停止（世界静止）不可被驳倒。',
        'That a net\'s marking stops changing, and that its world rests, cannot be refuted.',
        '网的标识停止变化、其世界静止，皆不可被驳倒。',
        'Fires; fired transitions lose; finitely many places, and for the world finitely many transitions; equality '
        'decided.',
        '发生；所发生变迁损失；库所有限，世界形式还要求变迁有限；相等可判定。', src('Openness')),
    dep('own-count-misses-joint-excess',
        'Instantiates Flow.joint_excess_ends and Flow.stays_below as the siphon law.',
        '把 Flow.joint_excess_ends 与 Flow.stays_below 实例化为虹吸律。',
        'Joint excess ends gated renewal and every formation depending on the condition at the gating need.',
        '共同过量结束受门控的更新，以及在门控需要处依赖该条件的每个形成。',
        'Every transition consuming at least m from a gated place is dead after joint excess; an empty gated place '
        'stays empty.',
        '共同过量之后，每个从受门控库所取至少 m 的变迁不再发生；空的受门控库所保持为空。',
        'Fires (balance, acting, dependence); the place is gated at m; unit weights.',
        '发生（平衡、给出者活动、依赖）；库所在 m 处受门控；单位权。', src('Continuation')),
]

RELATED = [
    {'id': 'premises-read-off-the-exchange',
     'detail': {'en': 'Read off a law of exchange, the tying premises hold and dissipation is a state of the law; for a '
                      'net\'s law that state is exactly a strict P-subinvariant on what fires.',
                'zh': '从交换律读出时，捆绑前提成立，耗散是律的一种状态；对网的律，这种状态恰是所发生变迁上的严格 P-子不变量。'}},
]

record = {
    'schema_version': 2, 'id': RID,
    'title': {'en': 'Place/transition nets on the spine', 'zh': '脊柱上的库所/变迁网'},
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': NOW,
    'statement': STATEMENT,
    'laws': [{'en': en, 'zh': zh, 'declarations': resolve(names)} for en, zh, names in LAWS],
    'hypotheses': [
        {'en': 'No axiom. The net, its schedule, its starting marking and its weights are given; every other premise is '
               'a named property of the net stated where it is used: a firing sequence; finitely many places listed '
               'once with equality decided; fired transitions that lose weighted tokens; a gated place; finitely many '
               'transitions for the world form.',
         'zh': '不加公理。网、调度、初始标识与权是给定的；其余每个前提都是网的一个具名性质，在用到之处陈述：发生序列；有限多个库所各列一次且'
               '相等可判定；所发生变迁损失加权令牌；受门控的库所；世界形式还要求变迁有限。'}],
    'does_not_show': [
        {'en': 'That a given chemical, biological or computing system is a given net, with which places, transitions '
               'and weights: a modelling correspondence outside the Lean.',
         'zh': '某个化学、生物或计算系统是某个给定的网，有哪些库所、变迁与权：这是 Lean 之外的建模对应。', 'kind': 'scope'},
        {'en': 'Inhibitor arcs, capacities, timed, stochastic or continuous nets; siphons of more than one place; nets '
               'with infinitely many places; deciding reachability.',
         'zh': '抑制弧、容量、时间网、随机网或连续网；多于一个库所的虹吸；无限多个库所的网；可达性的判定。', 'kind': 'scope'},
        {'en': 'That every system in our universe loses at each step; dissipation is a property a net has or lacks, as '
               'the conservative cycle shows.',
         'zh': '我们宇宙中的每个系统每步都有损失；耗散是网具有或缺乏的性质，守恒循环即是一例。', 'kind': 'non-implication'}],
    'counterexamples': COUNTER,
    'standard_boundaries': BOUNDS,
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {n_decl} declarations of '
              f'Becoming.{MOD}, {n_thm} of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'Author review in study section {N}; not independently reviewed by a person.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.{MOD} 的 {n_decl} 项声明（{n_thm} 项定理）公理报告为空；'
              f'检查器并核对核心纯净。作者审查见研究第 {N} 节；未经人的独立审查。'},
    'next_delta': {
        'en': 'Stochastic reaction networks pathwise and in expectation; siphons of several places; finite Markov kernels '
              'on counts; an independent review.',
        'zh': '随机反应网络的逐路径与期望形式；多库所的虹吸；计数上的有限马尔可夫核；独立审查。'},
    'correspondence': {
        'en': 'An outside critique of the opening said the theory proves the rules of its own invented universe and '
              'assumes ours runs the same way; the opening proposal\'s second review ranked an instance theorem for a '
              'formalism defined outside the theory as the direct answer. Place/transition nets are such a formalism; '
              'the map onto the spine is the identity on what each states.',
        'zh': '一则对开篇的外部批评说，理论证明了它自己所发明之宇宙的规则，又假定我们的宇宙也如此运行；开篇提案的第二次审查把一个关于理论之外'
              '所定义形式体系的实例定理列为直接回应。库所/变迁网就是这样的形式体系；到脊柱的映射在两者各自所述之上是恒等的。'},
    'canonical_source': src(MOD),
    'aliases': [
        'place/transition nets on the spine', 'Petri nets on the spine', '脊柱上的库所/变迁网', 'siphon law',
        'Becoming.Net.balances_iff', 'Becoming.Net.dissipative_iff', 'Becoming.Net.rests_unrefuted',
        'Becoming.Net.siphon_empty'],
    'dependencies': DEPS,
    'related': RELATED,
}
cited = {src(MOD)}
extra = []
for d in DEPS:
    e = d['interface']['evidence']
    if e not in cited:
        cited.add(e)
        extra.append(e)
record['references'] = (
    [{'path': src(MOD), 'role': 'proof', 'declarations': sorted(FULL), 'sha256': sha(src(MOD))}]
    + [{'path': p, 'role': 'proof', 'sha256': sha(p)} for p in extra]
    + [{'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
       {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
       {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
       {'path': PROVENANCE, 'role': 'provenance', 'sha256': sha(PROVENANCE)}])
record['proof_bindings'] = [{'source': src(MOD), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{MOD}',
                             'success_pointer': '/status', 'success_value': 'passed'}]
record['history'] = [{
    'en': f'19 October 2026: added (PT1), the instance theorem the opening proposal\'s second review ranked second; '
          f'study section {N}.',
    'zh': f'2026年10月19日：新增（PT1），即开篇提案第二次审查列在第二位的实例定理；研究第 {N} 节。'}]
path = RECORDS / f'{RID}.json'
assert not path.exists(), 'record exists'
path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print('written', RID, n_thm, n_decl)
