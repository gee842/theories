#!/usr/bin/env python3
"""R33: the records of the joins (run once, before rebind.py).

* G4: a-law-through-a-projection-along-one-run becomes the one record "A law along one run, under a
  relation": the law up to an equivalence with its three readings (projection, changing coupling, fixed
  conditions) and exactness; the laws, aliases, witnesses, premises and links of
  a-law-through-coupling-along-one-run and a-law-through-changing-coupling-along-one-run join it, and those
  two are superseded by it (their evidence kept as it was).
* G5: new record learning-through-a-map-is-tracking-in-the-limit.
* G6: whether-a-loop-closes-a-difference: factor in place of strength, and the join with Loops.
* G7: thresholds-of-waiting: the tolerance law as a web's run.
* G10: new record the-world-an-interleaving-builds.
Hashes of the chapter and the study are set by rebind.py after those are committed."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
REC = ROOT / 'theories/becoming/results/records'
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
B = LEAN + 'becoming/Becoming/'
RID = '20261019T235844.485705Z'
RECEIPT = LEAN + f'becoming/becoming-checks/{RID}/verification.json'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
FRONTIER = '_process/research/2026-10-05-generative-foundation-review/root-foundation/twentieth-review/G-FRONTIER.md'
NOW = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
BOUNDS = ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical', 'names-provisional',
          'omission-not-refutation']


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


def dep(i, en, zh, out, inp, cond, evidence):
    return {'id': i, 'relation': 'formal-reuse', 'detail': {'en': en, 'zh': zh},
            'interface': {'output': out, 'input': inp, 'conditions': cond, 'evidence': evidence}}


def t(en, zh):
    return {'en': en, 'zh': zh}


# ---------------------------------------------------------------- G4
P, C, X = (load('a-law-through-a-projection-along-one-run'), load('a-law-through-coupling-along-one-run'),
           load('a-law-through-changing-coupling-along-one-run'))
SUP = {C['id'], X['id']}
pl, cl, xl = P['laws'], C['laws'], X['laws']
P['title'] = t('A law along one run, under a relation', '沿一个运行、在一个关系之下的规律')
P['statement'] = t(
    "Under an equivalence, a law admits a run's steps up to a step exactly where steps alike under it, by the same "
    "move, end alike, and failure persists. Projection, changing coupling and fixed conditions are its readings; the "
    "image is exact exactly where alike configurations match steps.",
    '在一个等价关系之下，规律容许一个运行到某步为止的各步，恰在经它相同、动作相同的步终于相同之处，失败持续。投影、改变的耦合与固定条件是其读法；'
    '像恰在相同的配置相互匹配步之处精确。')
P['claim'] = t(
    "One law along a run, up to an equivalence: some process going alike under it admits a run's steps before a step "
    "exactly where any two of them alike under it, by the same move, end alike (Run.law_under_iff), with the record "
    "read under it as witness and failure persisting. Its readings are corollaries: through a projection, the "
    "relation of equal images (Run.ConsistentThrough is consistency under that relation, and Run.law_through_iff is "
    "proved from Run.law_under_iff), where the record is the least candidate and the identity gives the history law; "
    "through coupling that changes along the run, with dependences read off the configuration; and through fixed "
    "conditions, the instance whose dependences do not change, matching Web.AlikeThrough. Exactness of the image is a "
    "law of the whole process, kept beside them.",
    '沿一个运行、到等价关系为止的一条规律：某个在其下同去的过程容许一个运行在某步之前的各步，恰在其中任两步经它相同、以相同动作终于相同之处'
    '（Run.law_under_iff），见证是在其下读出的记录，失败持续。其读法都是推论：经投影，即像相等的关系（Run.ConsistentThrough 是此关系下的一致，'
    'Run.law_through_iff 由 Run.law_under_iff 证出），记录是最小候选，恒等给出历史之律；经沿运行改变的耦合，依赖从配置读出；经固定条件，'
    '即依赖不变的实例，与 Web.AlikeThrough 相合。像的精确是整个过程的规律，并列保留。')
P['laws'] = [cl[0], cl[1], pl[0], pl[1], pl[2], xl[0], xl[1], xl[2], cl[2], cl[3], xl[3], pl[3]]
P['hypotheses'] = P['hypotheses'] + C['hypotheses'] + X['hypotheses']
P['does_not_show'] = [P['does_not_show'][0], P['does_not_show'][1], C['does_not_show'][0], X['does_not_show'][0],
                      X['does_not_show'][1], C['does_not_show'][1],
                      {'en': "The criterion along one run is near-definitional: what it adds is the least candidate, "
                             "the persistence of failure, the identity instance, the bridges to coupling and the "
                             "comparison of fixed and changing coupling.",
                       'zh': '沿一个运行的判据近于定义：增量在于最小候选、失败的持续、恒等实例、通往耦合的桥，以及固定与改变的耦合之比较。',
                       'kind': 'scope'}]
for cx in C['counterexamples'] + X['counterexamples']:
    P['counterexamples'].append({'path': B + 'LawAlongRun.lean', 'detail': cx['detail']})
P['next_delta'] = t(
    'How many steps of a run settle whether a law through a finite description or coupling holds (with '
    'Becoming.Recurrence); observation that changes along the run; an independent review.',
    '一个运行要多少步才定下经有限描述或耦合的规律是否成立（与 Becoming.Recurrence 一起）；沿运行改变的观察；独立审查。')
P['correspondence'] = t(
    "The chapter's open programme (section 8.2) named a constructive criterion along one run for a projection "
    "carrying a law, the bridge to GenerativeCore's exact projection, the instance with a formation's coupling as the "
    "relation, and the criterion through coupling that changes along the run; this record holds all four as one law "
    "under a relation with its readings, as the twentieth review's G4 asked. Coupling (Web.AlikeThrough) is a "
    "relation, not a projection, and an equality of what is coupled would need propext, so the law is stated up to an "
    "equivalence. Reading (the AI's): a run is evidence of a law under a relation exactly as far as its own steps "
    "agree; what it never visits it does not test; where what a formation does not couple into decides its next "
    "coupling, it meets no law at its coupling, only a record; a law at a description is not yet a faithful model of "
    "finite paths.",
    '本章开放纲领（第 8.2 节）列出沿一个运行、投影承载规律的构造性判据，通往 GenerativeCore 精确投影的桥，以形成的耦合为关系的实例，以及经沿运行'
    '改变的耦合的判据；本记录把四者作为关系之下的一条规律及其读法收在一起，如第二十次审查 G4 所求。耦合（Web.AlikeThrough）是关系而非投影，所耦合者的'
    '相等需要 propext，所以规律到等价关系为止陈述。读法（AI 的）：一个运行在多大程度上自身各步一致，就在多大程度上是关系之下规律的证据；它未到过的，'
    '它不检验；形成不耦合者决定其下一步耦合之处，它在其耦合上遇不到规律，只有记录；描述上的规律还不是有限路径的忠实模型。')
P['aliases'] = P['aliases'] + C['aliases'] + X['aliases']
deps = {d['id']: d for d in P['dependencies']}
for d in C['dependencies']:
    if d['id'] not in deps and d['id'] != P['id']:
        deps[d['id']] = d
for d in X['dependencies']:
    if d['id'] == 'becoming-dependence-dynamics':
        deps[d['id']] = d
P['dependencies'] = list(deps.values())
P['related'] = [r for r in P['related'] if r['id'] not in SUP] + [r for r in C['related'] if r['id'] not in SUP]
refs = {r['path']: r for r in P['references']}
order = [r['path'] for r in P['references']]
lawalong = refs[B + 'LawAlongRun.lean']
for src in (C, X):
    for r in src['references']:
        p = r['path']
        if p.startswith(LEAN + 'history/'):
            for x in r.get('declarations', []):
                if x not in lawalong['declarations']:
                    lawalong['declarations'].append(x)
            continue
        if p not in refs:
            refs[p] = dict(r)
            order.append(p)
        else:
            for x in r.get('declarations', []):
                if x not in refs[p].setdefault('declarations', []):
                    refs[p]['declarations'].append(x)
            if refs[p].get('sha256') != h(p) and r.get('sha256') == h(p):
                refs[p]['sha256'] = r['sha256']
P['references'] = [refs[p] for p in order]
bound = {b['source']: b for b in P['proof_bindings']}
for src in (C, X):
    for b in src['proof_bindings']:
        if b['source'].startswith(LEAN + 'history/'):
            continue
        if b['source'] not in bound or b['receipt'] > bound[b['source']]['receipt']:
            bound[b['source']] = b
P['proof_bindings'] = list(bound.values())
for b in P['proof_bindings']:
    assert any(r['path'] == b['receipt'] for r in P['references']), b['receipt']
P['reviewed_at_utc'] = NOW
P['history'].append(t(
    '20 October 2026, R33 (G4, one law along a run): Becoming.LawThroughCoupling and Becoming.LawThroughChangingCoupling '
    'were joined into Becoming.LawAlongRun, their declarations kept under their names, and Run.ConsistentThrough became '
    'consistency under the relation of equal images, with Run.law_through_iff proved from Run.law_under_iff. This record '
    'became the one record of the join: its title, statement and claim now state the law under a relation with its three '
    'readings; the laws, premises, non-implications, witnesses (Unseen, Changing), aliases, dependencies and related link '
    'of a-law-through-coupling-along-one-run and a-law-through-changing-coupling-along-one-run joined it, and those two '
    'are superseded by it. Study section 224.',
    '2026年10月20日，R33（G4，沿运行的一条规律）：Becoming.LawThroughCoupling 与 Becoming.LawThroughChangingCoupling 并入 '
    'Becoming.LawAlongRun，声明以原名保留；Run.ConsistentThrough 成为像相等之关系下的一致，Run.law_through_iff 由 Run.law_under_iff 证出。'
    '本记录成为此并合的唯一记录：标题、陈述与论断现在陈述关系之下的规律及其三种读法；a-law-through-coupling-along-one-run 与 '
    'a-law-through-changing-coupling-along-one-run 的规律、前提、不蕴含、见证（Unseen、Changing）、别名、依赖与相关链接并入本记录，'
    '那两条记录由本记录取代。研究第 224 节。'))
save(P)
for S in (C, X):
    S['status'] = 'superseded'
    S['superseded_by'] = P['id']
    S['aliases'] = []
    S['reviewed_at_utc'] = NOW
    S['history'].append(t(
        f"20 October 2026, R33 (G4): superseded by {P['id']}, the one record of a law along one run under a relation; "
        "its laws, premises, non-implications, witness, aliases and links are there, its declarations in "
        "Becoming.LawAlongRun under their names. The evidence here is kept as it was: the module's bytes in the Lean "
        "history folder, bound to the receipts that checked them.",
        f"2026年10月20日，R33（G4）：由 {P['id']} 取代，即沿一个运行、在关系之下之规律的唯一记录；本记录的规律、前提、不蕴含、见证、别名与链接都在那里，"
        "其声明以原名在 Becoming.LawAlongRun 中。此处证据照旧保留：模块字节在 Lean 历史目录中，绑定到检查过它们的回执。"))
    save(S)

# ---------------------------------------------------------------- G5
LR, LV = B + 'LearnableRuns.lean', B + 'LimitVerification.lean'
lr = lambda *xs: ['Becoming.LearnableRuns.' + x for x in xs]
lv = lambda *xs: ['Becoming.Limit.' + x for x in xs]
G5 = {
    'schema_version': 2,
    'id': 'learning-through-a-map-is-tracking-in-the-limit',
    'title': t('Learning through a map is tracking in the limit', '经映射的学习是极限中的跟随'),
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F11', 'reviewed_at_utc': NOW,
    'statement': t(
        "An extrapolation predicts a feature along every run exactly where its guess, fixed by the record through the "
        "map, tracks the feature in the limit. Where the law leaves the feature unchanged this is identification in "
        "the limit; where the law changes it, it need not be.",
        '外推沿每个运行预测一个特征，恰当它经映射由记录所定的猜测在极限中跟随该特征。律使特征不变时，这就是极限中的辨识；律改变特征时，未必如此。'),
    'laws': [
        {**t("A guess tracks a target in the limit where, on every run, from some horizon on it is the target's value at "
             "the horizon; identifying a hypothesis is tracking a target constant in the horizon, and two targets one "
             "guess tracks agree from some horizon on.",
             '猜测在极限中跟随目标，是说在每个运行上，从某个视界起它是目标在该视界的值；辨识一个假设就是跟随一个不随视界而变的目标；同一猜测跟随的两个目标从某个视界起一致。'),
         'declarations': lv('Tracks', 'identifies_iff_tracks', 'Tracks.agree')},
        {**t("An extrapolation's guess at horizon k is what it proposes from the prefix before k of the run's course "
             "through the map; it is fixed by the record through the map, so by the record. The extrapolation predicts "
             "the feature along every run exactly where its guess tracks it.",
             '外推在视界 k 的猜测是它从运行经映射之进程在 k 之前的前段所提出者；它由经映射的记录所定，从而由记录所定。外推沿每个运行预测特征，恰当其猜测跟随该特征。'),
         'declarations': lr('guess', 'FixedThrough', 'guess_fixedThrough', 'FixedThrough.byRecord', 'predicts_iff_tracks')},
        {**t("A guess fixed by the record through the map that tracks the feature gives runs beginning alike in the frame "
             "features agreeing from some step on; learnable through the map, some such guess tracks it, with no "
             "premise; in a world a list holds, learnable exactly where some such guess tracks the feature.",
             '经映射由记录所定、跟随特征的猜测，给在框架中开始相同的运行从某步起一致的特征；经映射可学，则有这样的猜测跟随它，不加前提；在列表所持的世界中，恰当有这样的猜测跟随特征时可学。'),
         'declarations': lr('agree_of_tracks', 'tracks_of_learnable', 'learnable_iff_tracks')},
        {**t("Where the law leaves the feature unchanged, it stands along a run as at the start, and in a world a list "
             "holds the feature is learnable through the map exactly where some guess fixed by the record through the "
             "map identifies in the limit its value at the run's start.",
             '律使特征不变之处，特征沿运行如在起点；在列表所持的世界中，特征经映射可学，恰当有经映射由记录所定的猜测在极限中辨识其在运行起点的值。'),
         'declarations': lr('val_invariant', 'learnable_iff_identifies')},
        {**t("In Merge every configuration goes to 0 and the feature says whether a configuration is 1: through the map "
             "that tells nothing apart it is learnable, proposing false from step 1, the law changes it, and no guess "
             "fixed by the record identifies its value at the start.",
             'Merge 中每个配置都走到 0，特征说配置是否为 1：经什么也不区分的映射它可学（从第 1 步起提出 false），律改变它，而没有由记录所定的猜测辨识它在起点的值。'),
         'declarations': lr('Merge.next', 'Merge.val', 'Merge.at_zero', 'Merge.learnable', 'Merge.not_identifies',
                            'Merge.learnable_not_identifies')},
    ],
    'hypotheses': [t(
        "No axiom. The forward directions need no premise. The converse of learnable_iff_tracks takes a world a list "
        "holds and decidable equality of the map's values (it goes through learnable_iff); learnable_iff_identifies "
        "takes also that the law leaves the feature unchanged.",
        '不加公理。正向不需前提。learnable_iff_tracks 的逆向取列表所持的世界与映射之值的相等可判定（经由 learnable_iff）；learnable_iff_identifies 另取律使特征不变。')],
    'does_not_show': [
        {**t("Tracking without a list holding the world: the converse builds the extrapolation from the law, the map, "
             "the feature and the list.", '无列表所持世界时的跟随：逆向由律、映射、特征与列表构造外推。'), 'kind': 'converse'},
        {**t("Identification of a feature the law changes: Merge is learnable and identified by no guess fixed by the "
             "record.", '律所改变之特征的辨识：Merge 可学，却不为由记录所定的任何猜测所辨识。'),
         'kind': 'non-implication', 'witness': 'Becoming.LearnableRuns.Merge.learnable_not_identifies'},
        {**t('Which maps actual learners read, or that any formation learns by extrapolation.',
             '实际的学习者读哪个映射，或任何形成以外推学习。'), 'kind': 'correspondence'},
    ],
    'counterexamples': [{'path': LR, 'detail': t(
        'Learnable through a map, not identification of the start: Merge (Merge.learnable_not_identifies).',
        '经映射可学而起点不被辨识：Merge（Merge.learnable_not_identifies）。')}],
    'standard_boundaries': BOUNDS,
    'validation_scope': t(
        f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {RID}): the cited declarations of '
        'Becoming.LearnableRuns and Becoming.LimitVerification have empty axiom reports; the checker verifies core '
        'purity. Author self-review in study section 224; not independently reviewed.',
        f'Lean 4.29.1 合并检查器实查（回执 {RID}）：所引 Becoming.LearnableRuns 与 Becoming.LimitVerification 的声明公理报告为空；'
        '检查器并核对核心纯净。作者自审见研究第 224 节；未经独立审查。'),
    'next_delta': t(
        'Tracking without a list holding the world, where turning a guess into an extrapolation needs a run chosen per '
        'prefix; learnability itself verified or refuted in the limit; an independent review.',
        '无列表所持世界时的跟随，此时把猜测变成外推需要为每个前段选一个运行；可学性本身在极限中的验证或否证；独立审查。'),
    'correspondence': t(
        "The twentieth review's G5 found two theories of learning in the limit, Learnable with Unrolling and Labels, and "
        "LimitVerification, unjoined. Learnable's target changes with the step, so the exact bridge is tracking, of "
        "which LimitVerification's identification is the case of a constant target. Reading (the AI's): to learn "
        "through a map is to come, from the record alone, to say rightly what the feature is now, not what it was at "
        "the start; the two agree only where the unfolding leaves the feature as it is.",
        '第二十次审查 G5 发现两种极限中学习的理论（Learnable 及 Unrolling、Labels，与 LimitVerification）没有接上。Learnable 的目标随步而变，'
        '所以精确的桥是跟随，LimitVerification 的辨识是目标不变的情形。读法（AI 的）：经映射学习，是仅凭记录逐渐正确地说出特征现在是什么，'
        '而不是它在起点是什么；两者只在展开让特征保持原样之处一致。'),
    'canonical_source': LR,
    'aliases': ['learning is tracking in the limit', '学习是极限中的跟随', 'tracking in the limit', '极限中的跟随',
                'Becoming.LearnableRuns.learnable_iff_identifies', 'Becoming.LearnableRuns.predicts_iff_tracks'],
    'dependencies': [
        dep('learnable-through-registration',
            'Reuses LearnableRuns.Predicts, learnable_iff and course_same: what an extrapolation can learn through a map '
            'along the runs of a determined law.',
            '复用 LearnableRuns.Predicts、learnable_iff 与 course_same：外推沿确定律的运行经映射能学到什么。',
            t('Learnability through a map along runs, and its criterion in a world a list holds.',
              '沿运行经映射的可学性，及其在列表所持世界中的判据。'),
            t('What tracking in the limit is shown equivalent to.', '与极限中的跟随证明等价者。'),
            t('A world a list holds, for the converse.', '逆向需列表所持的世界。'), LR),
        dep('what-a-method-comes-to-say-in-the-limit',
            'Reuses Limit.Identifies, of which tracking is the generalization to a target changing with the horizon.',
            '复用 Limit.Identifies；跟随是它到随视界而变之目标的推广。',
            t('Identification in the limit over the runs of a process.', '过程运行上极限中的辨识。'),
            t('The constant-target case of tracking.', '跟随中目标不变的情形。'),
            t('None beyond the process.', '过程之外无。'), LV),
    ],
    'related': [],
    'references': [
        ref(LR, 'proof', lr('guess', 'FixedThrough', 'guess_fixedThrough', 'FixedThrough.byRecord', 'predicts_iff_tracks',
                            'agree_of_tracks', 'tracks_of_learnable', 'val_invariant', 'learnable_iff_tracks',
                            'learnable_iff_identifies', 'Merge.next', 'Merge.val', 'Merge.at_zero', 'Merge.learnable',
                            'Merge.not_identifies', 'Merge.learnable_not_identifies')),
        ref(LV, 'proof', lv('Tracks', 'Identifies', 'identifies_iff_tracks', 'Tracks.agree')),
        ref(RECEIPT, 'receipt'), ref(STUDY, 'integration'), ref(CHAPTER, 'statement'), ref(FRONTIER, 'provenance'),
    ],
    'proof_bindings': [binding(LR, 'Becoming.LearnableRuns'), binding(LV, 'Becoming.LimitVerification')],
    'history': [t(
        '20 October 2026: added (R33, G5 of the twentieth review, learning in the limit joined): Limit.Tracks and the '
        'bridge from learning through a map to tracking and identification in the limit, with Merge; study section 224.',
        '2026年10月20日：新增（R33，第二十次审查 G5，极限中的学习接上）：Limit.Tracks，以及从经映射的学习到极限中跟随与辨识的桥，附 Merge；研究第 224 节。')],
}
save(G5)

# ---------------------------------------------------------------- G6
L = load('whether-a-loop-closes-a-difference')
L['statement'] = t(
    "A loop closes a difference only through a link that gives back less than it received. A return map below what it "
    "receives closes within d turns, exactly. With whole-number factors a loop closes at once, keeps the difference or "
    "runs away: nothing between.",
    '回路只经一个给回少于所受的环节闭合差别。低于所受的回返映射在 d 圈之内闭合，且恰好如此。整数倍率下，回路立即闭合、保持差别或失控：中间没有。')
last = L['laws'][-1]
assert 'whole-number strengths' in last['en']
last['en'] = last['en'].replace('whole-number strengths', 'whole-number factors')
last['zh'] = last['zh'].replace('整数强度', '整数倍率')
last['declarations'] = ['Becoming.LoopReturn.whole_factors' if x == 'Becoming.LoopReturn.whole_strengths' else x
                        for x in last['declarations']]
L['laws'].append({**t(
    "A link's factor is not a coupling strength. On a condition holding what it has and coupled to itself with "
    "strength M, the return map multiplying by 1 + M is Loops' carried amount turn by turn and its gap against the "
    "quiet course; around a cycle of several conditions, the return map by one plus the product of the strengths stays "
    "at or below the carried amount after each turn.",
    '环节的倍率不是耦合强度。保持所有且以强度 M 耦合于自身的条件，以 1 + M 相乘的回返映射逐圈就是 Loops 所携带的量及其与静默进程之差；'
    '绕几个条件的回路，以一加强度之积相乘的回返映射每圈之后不超过所携带的量。'),
    'declarations': ['Becoming.LoopReturn.factor', 'Becoming.LoopReturn.factor_single', 'Becoming.LoopReturn.geomBound_eq_course',
                     'Becoming.LoopReturn.selfLoop_carried', 'Becoming.LoopReturn.selfLoop_gap',
                     'Becoming.LoopReturn.carried_around_course']})
for item in L['does_not_show']:
    if item['en'].startswith('That closing a difference is better'):
        item['en'] = item['en'].replace('real strengths', 'real factors')
        item['zh'] = item['zh'].replace('实数强度', '实数倍率')
L['does_not_show'].append({**t(
    'The carried amount around a cycle of several conditions exactly: the intermediate conditions hold and keep '
    'giving, so only a lower bound by the return map is shown.',
    '绕几个条件的回路所携带的量的精确值：中间的条件保持并继续给出，所以只证明了回返映射给出的下界。'), 'kind': 'scope'})
L['next_delta'] = t(
    'Real factors, where a multiplication below one closes gradually; a loop of Rejoining read as a return map; the '
    'carried amount around a cycle of several conditions exactly; an independent review.',
    '实数倍率，其中小于一的乘法逐步闭合；把 Rejoining 的回路读作回返映射；绕几个条件之回路所携带的量的精确值；独立审查。')
L['aliases'] = ['Becoming.LoopReturn.whole_factors' if a == 'Becoming.LoopReturn.whole_strengths' else a
                for a in L['aliases']]
LOOPS, PROP = B + 'Loops.lean', B + 'Propagation.lean'
L['dependencies'] += [
    dep('how-a-carried-difference-grows',
        'Reuses Loops.geomBound, Loops.SelfLoop.strengths, SelfLoop.carried_eq, Loops.product, CoupledWith and '
        'carried_runaway: the self-loop of strength M and a cycle of couplings.',
        '复用 Loops.geomBound、Loops.SelfLoop.strengths、SelfLoop.carried_eq、Loops.product、CoupledWith 与 carried_runaway：'
        '强度为 M 的自环与耦合的回路。',
        t('The carried amount of a self-loop, and its lower bound around a cycle.', '自环所携带的量，以及回路上的下界。'),
        t('What the return map of one link with factor 1 + M, or one plus the product, is compared with.',
          '倍率为 1 + M 或一加强度之积的单环节回返映射所比较者。'),
        t('A cycle coupled at every step with at least the given strengths.', '每步以至少给定强度耦合的回路。'), LOOPS),
    dep('how-much-difference-arrives',
        'Reuses carried, gap and carried_attained: the carrying law attains the carried amount as its gap.',
        '复用 carried、gap 与 carried_attained：携带之律以所携带的量为其差而达到。',
        t('The carried amount and the course attaining it.', '所携带的量及达到它的进程。'),
        t('The gap the self-loop return map is.', '自环回返映射所是的差。'),
        t('None beyond the carrying law.', '携带之律之外无。'), PROP),
]
L['references'] += [
    ref(LOOPS, 'proof', ['Becoming.Loops.geomBound', 'Becoming.Loops.SelfLoop.strengths', 'Becoming.Loops.SelfLoop.carried_eq',
                         'Becoming.Loops.product', 'Becoming.CoupledWith', 'Becoming.carried_runaway']),
    ref(PROP, 'proof', ['Becoming.carried', 'Becoming.gap', 'Becoming.carried_attained']),
]
if not any(r['path'] == RECEIPT for r in L['references']):
    L['references'].append(ref(RECEIPT, 'receipt'))
L['proof_bindings'] += [binding(LOOPS, 'Becoming.Loops'), binding(PROP, 'Becoming.Propagation')]
L['reviewed_at_utc'] = NOW
L['history'].append(t(
    "20 October 2026, R33 (G6, one loop theory): LoopReturn's strength of a link was renamed its factor "
    "(LoopReturn.strength to factor, whole_strengths to whole_factors; development/r33-joins/RENAME-TABLE.json), so that "
    "strength means only a coupling strength and, around a cycle, the product of the coupling strengths; the statement, "
    "a law, an alias, a non-implication and the next step say factor. A law added: the join with Loops "
    "(selfLoop_carried, selfLoop_gap through carried_attained, carried_around_course), with dependencies on "
    "how-a-carried-difference-grows and how-much-difference-arrives and a non-implication on the cycle of several "
    "conditions. Study section 224.",
    '2026年10月20日，R33（G6，一个回路理论）：LoopReturn 中环节的强度改称倍率（LoopReturn.strength 改为 factor，whole_strengths 改为 '
    'whole_factors；development/r33-joins/RENAME-TABLE.json），使强度只指耦合强度及回路上耦合强度之积；陈述、一条规律、一个别名、一条不蕴含与下一步改说倍率。'
    '新增一条规律：与 Loops 的并合（selfLoop_carried、经 carried_attained 的 selfLoop_gap、carried_around_course），并依赖 '
    'how-a-carried-difference-grows 与 how-much-difference-arrives，加一条关于多条件回路的不蕴含。研究第 224 节。'))
save(L)

# ---------------------------------------------------------------- G7
T = load('thresholds-of-waiting')
tol = lambda *xs: ['Becoming.Tolerance.' + x for x in xs]
T['laws'].append({**t(
    "On a web whose conditions each depend only on themselves, need k units and are given one by each upstream formation "
    "supported the step before, with k at most the number upstream, support is the run of the tolerating law with "
    "tolerance the number upstream less k; with k all upstream it is Withholding's law without memory.",
    '在每个条件只依赖自身、需要 k 个单位、由上一步每个受支持的上游形成各给一个单位（k 不超过上游数）的网上，支持就是容忍数为上游数减 k 的容忍律之运行；'
    'k 取全部上游时即 Withholding 的无记忆之律。'),
    'declarations': tol('countTrue', 'countTrue_add_not', 'allBut_iff_count', 'allBut_sub_iff', 'KeepsInclusion.course_iff',
                        'web_tolerating', 'web_activity_tolerating', 'web_answers', 'giftLevels', 'giftWeb',
                        'giftWeb_tolerating')})
DEP = B + 'Dependence.lean'
T['references'].append(ref(DEP, 'proof', ['Becoming.Web.Supported']))
if not any(r['path'] == RECEIPT for r in T['references']):
    T['references'].append(ref(RECEIPT, 'receipt'))
T['proof_bindings'].append(binding(DEP, 'Becoming.Dependence'))
T['next_delta'] = t(
    'Amounts of giving and thresholds with memory; the tolerating law as an instance of an envelope law; webs whose '
    'conditions depend on others than themselves; an independent review.',
    '给出的数量与有记忆的阈值；容忍律作为包络律的实例；条件依赖自身以外者的网；独立审查。')
T['reviewed_at_utc'] = NOW
T['history'].append(t(
    '20 October 2026, R33 (G7, collective laws on webs): a law added, the tolerance law as the run of a web '
    '(web_tolerating, web_activity_tolerating, giftWeb_tolerating) with Withholding as k all upstream (web_answers), '
    'in Becoming.Tolerance with no new import; the next step names webs whose conditions depend on others. Study '
    'section 224.',
    '2026年10月20日，R33（G7，网上的集体之律）：新增一条规律，容忍律作为网的运行（web_tolerating、web_activity_tolerating、giftWeb_tolerating），'
    'k 取全部上游时即 Withholding（web_answers），在 Becoming.Tolerance 中且不加导入；下一步列出条件依赖他者的网。研究第 224 节。'))
save(T)

# ---------------------------------------------------------------- G10
IL, WL = B + 'Interleavings.lean', B + 'World.lean'
il = lambda *xs: ['Becoming.Interleavings.LocalLaw.' + x for x in xs]
G10 = {
    'schema_version': 2,
    'id': 'the-world-an-interleaving-builds',
    'title': t('The world an interleaving builds', '交错所构造的世界'),
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': NOW,
    'statement': t(
        "From a local law and a list of exchanges a World of the spine is built whose steps balance. Interleavings of "
        "the same own courses give each relatum the same course of standings and the same end; swapping two adjacent "
        "apart exchanges changes only the step between.",
        '由局部律与交换之列构造出脊柱的一个世界，其各步平衡。同一自身进程的交错给每个关系项同一串所立与同一终点；交换两个相邻而不相交的交换只改变其间一步。'),
    'laws': [
        {**t("The configuration after the first t exchanges of a list changes across step t by the exchange at t, is the "
             "whole list's from its length on, is unchanged up to a list's length by appending, is after a list the "
             "rest's from where the list ends, and agrees where the starts agree.",
             '一列交换的前 t 个之后的构形，跨第 t 步按第 t 个交换改变，从列长起是整列之构形，到列长为止不因追加而变，一列之后是余下者从该列终点出发的构形，起点一致则一致。'),
         'declarations': il('exchangeAt', 'runUpTo', 'runUpTo_succ', 'runUpTo_whole', 'runUpTo_append_le',
                            'runUpTo_append', 'runUpTo_agree')},
        {**t("The world of a local law on whole-number standings, the relata listed, a list and a start: at step t each "
             "relatum stands where the first t exchanges leave it, is active where the exchange at t touches it, and the "
             "move at t has present the listed relata it touches, each taking its fall and giving its rise; nothing is "
             "required, needed or drawn.",
             '整数所立上的局部律、所列关系项、交换之列与起点的世界：在第 t 步每个关系项立于前 t 个交换使它所在之处，被第 t 个交换触及处为活跃，第 t 步之动在场者为它触及的所列关系项，各取其降、给其升；无所求、所需或所汲。'),
         'declarations': il('touchedIn', 'fall', 'rise', 'world', 'world_level', 'touchedIn_mem', 'touchedIn_not_mem',
                            'touchedIn_mem_of', 'touchedIn_pairwise', 'total_zero_of', 'total_single', 'total_absent')},
        {**t('With every relatum listed once, every step of the world balances: the standing after the step with what '
             'the relatum took is the standing before with what it gave.',
             '每个关系项恰列一次时，世界每一步都平衡：步后所立加所取，等于步前所立加所给。'),
         'declarations': il('world_balances')},
        {**t("A relatum's course of standings is its standing after each exchange of its own course, in order. Moving "
             "an exchange forward past exchanges sharing no relatum with it keeps every course of standings, so with "
             "the relata listed two lists giving every relatum the same own course, and two interleavings of the same "
             "courses, give every relatum the same course of standings.",
             '关系项的一串所立，是它在自身进程的每个交换之后依次所立。把一个交换前移越过与它不共享关系项的交换，保持每串所立；所以关系项列出时，给每个关系项同一自身进程的两列，以及同一进程的两个交错，给每个关系项同一串所立。'),
         'declarations': il('standings', 'standings_true', 'standings_false', 'standings_agree', 'standings_move',
                            'standings_idle', 'standings_of_courses', 'standings_of_interleavings')},
        {**t('With the relata listed, the worlds of two lists giving every relatum the same own course stand alike at '
             'every step from both lengths on.',
             '关系项列出时，给每个关系项同一自身进程的两列，其世界从两者长度起每一步所立相同。'),
         'declarations': il('world_final')},
        {**t("Two adjacent exchanges sharing no relatum, taken in either order, leave the worlds alike at every step "
             "but the one between them; there a relatum the first touches stands, in the world taking it first, where "
             "it stands after both in the other, and where it stood before both in the other; one neither touches "
             "stands alike.",
             '两个相邻、不共享关系项的交换，以任一次序取用，世界在它们之间那一步以外每步相同；在那一步，先取第一个交换的世界中，它触及的关系项立于另一世界两者之后所立处，另一世界中则立于两者之前；两者都不触及者相同。'),
         'declarations': il('world_swap', 'world_swap_between')},
    ],
    'hypotheses': [t(
        "No axiom. A local law on whole-number standings (an exchange changes only the relata it touches, as their "
        "states determine); the relata listed, once where balance is stated; relata told apart for the move. The "
        "courses are finite lists.",
        '不加公理。整数所立上的局部律（交换只按所触及关系项的状态改变它们）；关系项列出，陈述平衡处恰列一次；为动区分关系项。进程是有限列。')],
    'does_not_show': [
        {**t('A step-by-step relation between the worlds of two interleavings differing by more than one exchange of '
             'adjacent apart exchanges; what is shown for them is the course of standings and the end.',
             '相差不止一次相邻不相交交换之对调的两个交错，其世界之间逐步的关系；对它们所证者是所立之串与终点。'), 'kind': 'scope'},
        {**t('The correspondence with the footprint and the order of joined exchanges of Becoming.Order.',
             '与 Becoming.Order 的足迹及相连交换之次序的对应。'), 'kind': 'correspondence'},
        {**t('Courses without end; footprints that read relata they do not change.',
             '无尽的进程；读而不改关系项的足迹。'), 'kind': 'scope'},
    ],
    'counterexamples': [],
    'standard_boundaries': BOUNDS,
    'validation_scope': t(
        f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {RID}): the cited declarations of '
        'Becoming.Interleavings have empty axiom reports; the checker verifies core purity. Author self-review in study '
        'section 224; not independently reviewed.',
        f'Lean 4.29.1 合并检查器实查（回执 {RID}）：所引 Becoming.Interleavings 的声明公理报告为空；检查器并核对核心纯净。作者自审见研究第 224 节；未经独立审查。'),
    'next_delta': t(
        'A step-by-step relation between the worlds of any two interleavings of the same courses (by the moves of '
        'split_heads); the correspondence with Becoming.Order; an independent review.',
        '同一进程任意两个交错之世界逐步的关系（经 split_heads 的移动）；与 Becoming.Order 的对应；独立审查。'),
    'correspondence': t(
        "The twentieth review's G10 asked that Interleavings, which reads the step index off the relata's own courses, "
        "construct the World, so that one shared index is a reading on the premise card. Reading (the AI's): the "
        "spine's World, with its one index, is what an interleaving of the relata's own courses builds; what the "
        "interleaving adds beyond the courses moves only where exchanges share no relatum, and there each relatum "
        "stands in one world where it stands a step earlier or later in the other.",
        '第二十次审查 G10 要求从关系项自身进程读出步指标的 Interleavings 构造世界，使唯一的共同指标在前提卡上成为一个读法。读法（AI 的）：带唯一指标的'
        '脊柱世界，是关系项自身进程的一个交错所构造者；交错在进程之外所加者只在交换不共享关系项处移动，且在那里每个关系项在一个世界中立于它在另一世界早一步或晚一步所立处。'),
    'canonical_source': IL,
    'aliases': ['the world an interleaving builds', '交错所构造的世界', 'course of standings', '所立之串',
                'Becoming.Interleavings.LocalLaw.world_swap', 'Becoming.Interleavings.LocalLaw.world_balances'],
    'dependencies': [
        dep('the-step-index-from-own-courses',
            'Reuses LocalLaw, ownCourse, run, act_comm, act_agree, split_heads, untouched_of_shares and run_of_courses: '
            'own courses and the moves past exchanges sharing no relatum.',
            '复用 LocalLaw、ownCourse、run、act_comm、act_agree、split_heads、untouched_of_shares 与 run_of_courses：自身进程及越过不共享关系项之交换的移动。',
            t('Equal own courses reach the same configuration; apart exchanges commute.', '自身进程同则构形同；不相交的交换可交换。'),
            t('The standings and the end the worlds share, and the adjacent swap.', '世界共有的所立与终点，以及相邻对调。'),
            t('The relata listed.', '关系项列出。'), IL),
        dep('worlds-are-runs',
            'Reuses World.of: a World built from a flow and a web.', '复用 World.of：由流与网构造的世界。',
            t('A World of the spine from a flow and a web.', '由流与网得到的脊柱世界。'),
            t('The world an interleaving builds.', '交错所构造的世界。'), t('None.', '无。'), WL),
    ],
    'related': [{'id': 'the-step-index-from-own-courses', 'detail': t(
        'There the index is built from the own courses and carries nothing beyond them; here the index builds the World.',
        '那里指标由自身进程构造且不带其外之物；这里指标构造世界。')}],
    'references': [
        ref(IL, 'proof', il('exchangeAt', 'runUpTo', 'runUpTo_succ', 'runUpTo_whole', 'runUpTo_append_le', 'runUpTo_append',
                            'runUpTo_agree', 'touchedIn', 'fall', 'rise', 'world', 'world_level', 'touchedIn_mem',
                            'touchedIn_not_mem', 'touchedIn_mem_of', 'touchedIn_pairwise', 'total_zero_of', 'total_single',
                            'total_absent', 'world_balances', 'standings', 'standings_true', 'standings_false',
                            'standings_agree', 'standings_move', 'standings_idle', 'standings_of_courses',
                            'standings_of_interleavings', 'world_final', 'world_swap', 'world_swap_between')),
        ref(WL, 'proof', ['Becoming.World.of']),
        ref(RECEIPT, 'receipt'), ref(STUDY, 'integration'), ref(CHAPTER, 'statement'), ref(FRONTIER, 'provenance'),
    ],
    'proof_bindings': [binding(IL, 'Becoming.Interleavings'), binding(WL, 'Becoming.World')],
    'history': [t(
        '20 October 2026: added (R33, G10 of the twentieth review, interleavings build the World): the construction, '
        'its balance, the course of standings and the end shared by interleavings of the same courses, and the adjacent '
        'swap; the general step-by-step relation is open (study section 224).',
        '2026年10月20日：新增（R33，第二十次审查 G10，交错构造世界）：构造、其平衡、同一进程之交错共有的所立之串与终点，以及相邻对调；一般的逐步关系待解（研究第 224 节）。')],
}
# related and dependency on one id: keep the dependency only
G10['related'] = []
save(G10)
