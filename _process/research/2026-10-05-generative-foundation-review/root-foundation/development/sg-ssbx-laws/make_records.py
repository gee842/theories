#!/usr/bin/env python3
"""Write SG's three records: python3 -B make_records.py CORE_RECEIPT   (from the checkout root, after apply_text.py)

Every declaration cited is resolved against the receipt's audited declarations of its module (a short name must
match exactly one declaration by suffix), and the receipt must bind each module's current bytes. The study section
and readings numbers come from sg-numbers.json, written by apply_text.py."""
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
STUDY = f'{RF}/BECOMING-RENEWAL-READING.md'
REVIEW = f'{RF}/SSBX-REPOSITORY-REVIEW.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SSBX = 'sources/07-shengsheng-buxi/ssbx-repo'
JUNCTURE_SRC = [f'{SSBX}/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版/03_卷二_发生.md',
                f'{SSBX}/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版/04_卷三_判准.md']
# 义理·拓扑 and 义理·形式逻辑 have spaces in their file names, which generated record pages cannot link; the review
# (a provenance reference of every record) and the study section link them.
TOPOLOGY_SRC = []
LOGIC_SRC = []
RECORDS = ROOT / 'theories/becoming/results/records'
core_id = sys.argv[1]
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
nums = json.loads((HERE / 'sg-numbers.json').read_text())
S, D = nums['study_section'], nums['readings']
assert re.search(rf'^## {S}\. Junctures, what a commuting law keeps apart, and the third value \(SG\)$',
                 (ROOT / STUDY).read_text(), re.M)


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def src(mod):
    return f'{PKG}/Becoming/{mod}.lean'


def decls(mod):
    m = next(m for m in core['modules'] if m['module'] == f'Becoming.{mod}')
    assert core['source_sha256'][f'Becoming.{mod}'] == sha(src(mod)), ('receipt does not bind', mod)
    return m


def resolve(mod, names):
    full = [d['name'] for d in decls(mod)['declarations']]
    out = []
    for n in names:
        hits = [f for f in full if f == 'Becoming.' + n or f.endswith('.' + n)]
        assert len(hits) == 1, (mod, n, hits)
        out.append(hits[0])
    return out


def counts(mod):
    m = decls(mod)
    assert not any(m['axiom_dependencies'].values()), mod
    return len(m['declarations']), sum(1 for d in m['declarations'] if d.get('kind') == 'theorem')


BOUNDS = ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical', 'names-provisional',
          'omission-not-refutation']


def dep(rid, relation, en, zh, out_en, out_zh, in_en, in_zh, cond_en, cond_zh, evidence):
    return {'id': rid, 'relation': relation, 'detail': {'en': en, 'zh': zh},
            'interface': {'output': {'en': out_en, 'zh': out_zh}, 'input': {'en': in_en, 'zh': in_zh},
                          'conditions': {'en': cond_en, 'zh': cond_zh}, 'evidence': evidence}}


def record(rid, mod, title, statement, laws, hypotheses, dns, nxt, corr, aliases, deps, related, extra_refs,
           provenance):
    n_decl, n_thm = counts(mod)
    aliases = [resolve(mod, [a[len('Becoming.'):]])[0] if a.startswith('Becoming.') else a for a in aliases]
    cited = {src(mod)} | {p for p, _ in extra_refs}
    extra_refs = list(extra_refs) + [(d['interface']['evidence'], None) for d in deps
                                     if d['interface']['evidence'] not in cited]
    assert len(statement['en']) <= 300, (rid, len(statement['en']))
    r = {
        'schema_version': 2, 'id': rid, 'title': title, 'kind': 'theorem', 'status': 'recorded-checked',
        'family': 'F01', 'reviewed_at_utc': NOW, 'statement': statement,
        'laws': [{'en': en, 'zh': zh, 'declarations': resolve(mod, names)} for en, zh, names in laws],
        'hypotheses': hypotheses, 'does_not_show': dns, 'counterexamples': [],
        'standard_boundaries': BOUNDS,
        'validation_scope': {
            'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {n_decl} declarations '
                  f'of Becoming.{mod}, {n_thm} of them theorems, have empty axiom reports; the checker verifies core purity. '
                  f'Proved in a scratch kit by the session that claimed SG; author review in study section {S}; not '
                  'independently reviewed by a person.',
            'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.{mod} 的 {n_decl} 项声明（{n_thm} 项定理）公理报告为空；'
                  f'检查器并核对核心纯净。由认领 SG 的会话在草稿中证明；作者审查见研究第 {S} 节；未经人的独立审查。'},
        'next_delta': nxt, 'correspondence': corr, 'canonical_source': src(mod), 'aliases': aliases,
        'dependencies': deps, 'related': related,
        'references': [{'path': src(mod), 'role': 'proof', 'declarations': sorted(d['name'] for d in decls(mod)['declarations']),
                        'sha256': sha(src(mod))}]
        + [dict({'path': p, 'role': 'proof'}, **({'declarations': ds} if ds else {}), sha256=sha(p)) for p, ds in extra_refs]
        + [{'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
           {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
           {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
           {'path': REVIEW, 'role': 'provenance', 'sha256': sha(REVIEW)}]
        + [{'path': p, 'role': 'provenance', 'sha256': sha(p)} for p in provenance],
        'proof_bindings': [{'source': src(mod), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{mod}',
                            'success_pointer': '/status', 'success_value': 'passed'}],
        'history': [{
            'en': f'19 October 2026: added (SG, general law {GL[rid]} of the review of the earlier 生生不息 repository), '
                  'on Ren\'s request that the earlier repository be read for what can be integrated ("please take a look '
                  f'of this … many insights can be integrated", abridged as quoted with the review); study section {S}.',
            'zh': f'2026年10月19日：新增（SG，早期《生生不息》仓库审读的一般律 {GL[rid]}），按 Ren 要求审读早期仓库中可并入者'
                  f'（“please take a look of this … many insights can be integrated”，节录，随审读引用）；研究第 {S} 节。'}],
    }
    path = RECORDS / f'{rid}.json'
    assert not path.exists(), ('record exists', rid)
    path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('written', rid)


GL = {'every-loss-passes-a-juncture': 'G1', 'what-a-commuting-law-keeps-apart': 'G2',
      'revision-with-an-undecided-value': 'G3'}
CORR = lambda en, zh: {'en': en + f' Reading the AI\'s (D{D}); Ren\'s words are provenance, not warrant.',
                       'zh': zh + f'读法是 AI 的（D{D}）；Ren 的话是出处，不是依据。'}
REC_DEP = dep('recurrence-without-premise', 'formal-reuse',
              'Reuses Law.orbit, orbit_add, orbit_shift and the run of a determined law, Law.run, whose states are the orbit.',
              '复用 Law.orbit、orbit_add、orbit_shift 与决定性律的运行 Law.run，其状态即轨道。',
              'The course of a determined law as a run of the spine.', '决定性律的进程作为脊柱的运行。',
              'The runs the laws are stated on.', '诸定律所陈述的运行。', 'None.', '无。', src('Recurrence'))
BRANCH_DEP = dep('returning-where-the-course-branches', 'formal-reuse',
                 'Reuses Reach, Trace, Returns, Reach.map and law_returns_iff of Becoming.Branching.',
                 '复用 Becoming.Branching 的 Reach、Trace、Returns、Reach.map 与 law_returns_iff。',
                 'What a process can have again, step by step, and returning under a determined law.',
                 '过程逐步可再得什么，以及决定性律下的返回。',
                 'Where a configuration is lost, and what a symmetry carries.', '配置在何处失去，对称承载什么。',
                 'None.', '无。', src('Branching'))
DIAG_DEP = dep('registration-within-what-it-registers', 'formal-reuse',
               'Reuses Diagonal.Moves, flip_moves, revision_never_rests, fixed_of_complete and Says.',
               '复用 Diagonal.Moves、flip_moves、revision_never_rests、fixed_of_complete 与 Says。',
               'A map moving every value never rests under revision; a complete family gives every map a fixed point.',
               '移动每个值的映射在修正下从不停息；完备的读法族给每个映射一个不动点。',
               'The fixed-point-free symmetry, the two-valued liar and the three-valued diagonal.',
               '无不动点的对称、二值说谎者与三值对角线。', 'None.', '无。', src('Diagonal'))

# G1
record(
    'every-loss-passes-a-juncture', 'Junctures',
    {'en': 'Every loss passes a juncture', 'zh': '每次失去都经过一个关节'},
    {'en': 'Where s returns, every course to a configuration that cannot have s again passes, not not, a juncture: one '
           'step there keeps s to be had and one loses it. Finding it is deciding reach (LPO for every process). Keeping '
           'the steps that keep s keeps s, the largest that does.',
     'zh': 's 返回时，每条到达不能再得 s 之配置的路径，不非地经过一个关节：那里一步保住 s 可得，一步失去它。找到它即判定可达（对每个过程为 LPO）。保留保住 s 之步者保住 s，是这样的最大者。'},
    [('A juncture for s has a step after which s can still be had and a step after which it cannot; it can have s '
      'again, its two steps differ in outcome, it is possibly drawn in, and on the course of s it returns.',
      's 的关节有一步之后 s 仍可得，有一步之后 s 不可得；它可再得 s，两步结果不同，可能被吸入，在 s 的路径上它返回。',
      ['Juncture', 'Juncture.reach', 'Juncture.outcomes_differ', 'Juncture.possiblyDrawn', 'Juncture.returns']),
     ('Where s returns, every course from s, or from a configuration that can have s, to one that cannot passes, up to '
      'double negation, a juncture at which it takes its losing step; so does every course of a configuration possibly '
      'drawn in.',
      's 返回时，从 s 或从可得 s 的配置到不可得 s 之配置的每条路径，在双重否定下，经过一个关节并在那里走出失去之步；可能被吸入之配置的每条路径亦然。',
      ['step_back', 'loss_passes_juncture_from', 'loss_passes_juncture', 'PossiblyDrawn.passes_juncture']),
     ('The juncture is found where it is decided along the course whether s can still be had, and for configurations a '
      'list holds with steps decided: a reading of reach that only rises settles by the list\'s length (through '
      'Undecided.settles_within) and decides reach.',
      '沿路径已判定 s 是否仍可得之处，关节被找到；配置由列表持有、步已判定时亦然：只升不降的可达读法按列表长度停住（经 Undecided.settles_within），判定可达。',
      ['loss_passes_juncture_decided_from', 'loss_passes_juncture_decided', 'leadsWithin', 'leadsWithin_sound',
       'leadsWithin_complete', 'leads_settles', 'leads_bound', 'reach_iff_leads', 'reach_decided_listed',
       'loss_passes_juncture_listed']),
     ('Finding the juncture of every loss of every process gives the limited principle of omniscience: in Hidden, '
      'whether origin can be had again from fork is whether a sequence has a true value.',
      '为每个过程的每次失去找到关节，推出有限全知原理：在 Hidden 中，从 fork 能否再得 origin，就是一个序列是否有 true 值。',
      ['Hidden.juncture_decides', 'lpo_of_junctures_found']),
     ('Keeping, the steps after which s can still be had, can have s from where the process can, keeps s, returns to s '
      'exactly where the process does and holds every sub-process keeping s on that sub-process\'s course from s; on its '
      'course it removes exactly the losing steps at junctures. Losing never returns to s.',
      '保持，即之后 s 仍可得之步，从原过程可得 s 处可得 s，保住 s，恰在原过程返回 s 处返回 s，并在每个保住 s 之子过程自 s 起的路径上包含它；在自己的路径上，它恰去掉关节处的失去之步。失去从不回到 s。',
      ['keeping', 'losing', 'SubProcess', 'Keeps', 'juncture_iff', 'reach_keeping_iff', 'keeping_keeps',
       'keeping_returns_iff', 'keeping_greatest', 'keeping_removes_at_juncture', 'losing_not_returns', 'losing_loses']),
     ('A process keeping s has no juncture on its course, however many options it has: Many has a step for every '
      'natural number and no juncture; OneWay\'s false, with two moves, is one.',
      '保住 s 的过程在其路径上没有关节，不论选项多少：Many 对每个自然数有一步而无关节；OneWay 的 false 有两种动作，是一个关节。',
      ['no_juncture_of_keeps', 'Many.no_juncture', 'OneWay.juncture'])],
    [{'en': 'No axiom and no premise on the process: the laws hold for every process; that s returns is a hypothesis of '
            'the loss laws, decided reach or listed configurations with decided steps of the found forms.',
      'zh': '不加公理，对过程不加前提：定律对每个过程成立；s 返回是失去律的假设，已判定的可达或步已判定的可列配置是找到形式的假设。'}],
    [{'en': 'Junctures for a set of configurations, or for a profile of several possibilities at once; which junctures '
            'actual unfoldings have.', 'zh': '一组配置的关节，或同时多种可能的剖面的关节；实际展开有哪些关节。',
      'kind': 'scope'},
     {'en': 'That keeping is better than losing, or which configuration ought to be kept.',
      'zh': '保持优于失去，或哪个配置应当保持。', 'kind': 'non-implication'}],
    {'en': 'Junctures for sets and profiles; keeping at the level of rules; an independent review.',
     'zh': '一组配置与剖面的关节；规则层的保持；独立审查。'},
    CORR('The earlier treatise\'s 机 (补篇一 §八, §十一), two continuations leading to different open futures, read with '
         'the open future as one configuration still to be had; 护闭 and 成闭 read as keeping and losing at a juncture '
         '(SSBX review §3.2, G1).',
         '早期论著的机（补篇一第八、十一节），即两个延续通向不同的开放之未来，读作把开放之未来取为一个仍可得的配置；护闭与成闭读作关节处的保持与失去（SSBX 审读第 3.2 节 G1）。'),
    ['every loss passes a juncture', '每次失去都经过一个关节', '机 (AI reading)', '护闭 as keeping (AI reading)',
     'Becoming.loss_passes_juncture', 'Becoming.keeping_greatest', 'Becoming.lpo_of_junctures_found'],
    [BRANCH_DEP,
     dep('necessarily-drawn-is-not-returning', 'formal-reuse',
         'Reuses PossiblyDrawn and possiblyDrawn_iff: a juncture is where possibly and necessarily drawn come apart.',
         '复用 PossiblyDrawn 与 possiblyDrawn_iff：关节是可能被吸入与必然被吸入分开之处。',
         'Being possibly drawn in is losing oneself on some course.', '可能被吸入即在某条路径上失去自身。',
         'Where on the course the loss happens.', '失去发生在路径上何处。', 'None.', '无。', src('Branching')),
     dep('coming-and-ceasing-keep-pace', 'application',
         'Uses the limited principle of omniscience, LPO, as stated in Becoming.Change.',
         '使用 Becoming.Change 中陈述的有限全知原理 LPO。',
         'The principle a sequence of truth values has a true or is false throughout.', '真值序列有 true 或处处为 false 的原理。',
         'What finding every juncture amounts to.', '找到每个关节等于什么。', 'None.', '无。', src('Change')),
     dep('revision-with-an-undecided-value', 'formal-reuse',
         'Reuses Undecided.settles_within to decide reach on listed configurations.',
         '复用 Undecided.settles_within 在可列配置上判定可达。',
         'Readings on a list that only rise settle by the list\'s length.', '列表上只升不降的读法按列表长度停住。',
         'Reach decided for listed configurations with decided steps.', '步已判定的可列配置上的可达判定。',
         'Configurations a list holds; steps decided.', '配置由列表持有；步已判定。', src('Undecided'))],
    [{'id': 'what-a-commuting-law-keeps-apart', 'detail': {
        'en': 'A symmetric process carries junctures in pairs under an exchange (Branching.Symmetric.juncture).',
        'zh': '对称过程在对换下成对地承载关节（Branching.Symmetric.juncture）。'}}],
    [(src('Branching'), ['Becoming.Branching.possiblyDrawn_iff', 'Becoming.Branching.Returns'])],
    JUNCTURE_SRC)

# G2
record(
    'what-a-commuting-law-keeps-apart', 'Commuting',
    {'en': 'What a commuting law keeps apart', 'zh': '交换之律保持什么分开'},
    {'en': 'Where a law commutes with a map moving every configuration, its runs from x and from the image of x are '
           'never at one configuration at the same step: to merge what a symmetry tells apart, a law must break it. The '
           'diagonal\'s never resting is the case of a map with itself.',
     'zh': '律与一个移动每个配置的映射交换时，它从 x 与从 x 之像出发的运行在同一步从不在同一配置：要合并对称所分开者，律必须破此对称。对角线的从不停息是映射与自身交换的情形。'},
    [('A law commuting with σ has its run from σ x the image of its run from x; where σ moves every configuration the '
      'two runs never meet at a step, and a law that merges them does not commute.',
      '与 σ 交换的律，从 σ x 出发的运行是从 x 出发之运行的像；σ 移动每个配置时，两条运行在同一步从不相遇，合并它们的律不交换。',
      ['Commutes', 'Commutes.iterate', 'Commutes.apart', 'Commutes.breaks']),
     ('No such law is constant; a run from what σ fixes stays where σ fixes; rests and returns come with their images.',
      '这样的律不是常值的；从 σ 所固定者出发的运行停在 σ 所固定者之中；静止与返回与其像成对。',
      ['Commutes.not_drawn_to_one', 'Commutes.keeps_fixed', 'Commutes.rest_paired', 'Commutes.returns_paired']),
     ('Under an exchange a run holding a configuration\'s image k steps on holds every configuration\'s image k steps on '
      'and returns at 2k; the law goes alike across the pairs, as a lumping and as a process.',
      '在对换下，k 步之后持有一个配置之像的运行，k 步之后持有每个配置之像，并在 2k 处返回；律在对之间同行，作为归并亦作为过程。',
      ['Commutes.paired_halfway', 'Commutes.halfway_returns', 'Commutes.pairs_lumped', 'Commutes.pairs_goAlike']),
     ('Every map commutes with itself, so a map moving every value never rests along its run '
      '(Diagonal.revision_never_rests as a case).',
      '每个映射与自身交换，所以移动每个值的映射沿其运行从不停息（Diagonal.revision_never_rests 作为其情形）。',
      ['Commutes.self_apart']),
     ('A process symmetric under σ carries reach, returning and, under an exchange, junctures; every run has a mirror '
      'run never at the same configuration at the same step; a commuting law is a symmetric process.',
      '在 σ 下对称的过程保持可达、返回，在对换下也保持关节；每条运行有一条镜像运行，在同一步从不在同一配置；交换之律是对称过程。',
      ['Symmetric', 'Symmetric.reach', 'Symmetric.returns', 'Symmetric.juncture', 'mirror', 'mirror_apart',
       'law_symmetric']),
     ('In the Changes the complement moves every hexagram and waxWane commutes with it: no number of steps brings a '
      'hexagram and its complement to one, the six steps to the complement are the pair halfway round the return of '
      'twelve, the going alike across pairs is the general law\'s instance, the waning into 坤 breaks the symmetry, and '
      'the change of one line is symmetric under the complement.',
      '在周易中，错卦移动每一卦，消息律与之交换：任何步数都不使一卦与其错卦合一，六步到错卦是十二步返回的半途，在对之间同行是一般律的实例，尽归坤之消破此对称，一爻之变在错卦下对称。',
      ['complement_moves', 'waxWane_apart', 'waxWane_halfway', 'pairs_goAlike_of_commutes', 'wane_breaks',
       'flip_complement', 'changes_symmetric', 'changes_mirror_apart'])],
    [{'en': 'No axiom; commuting and σ moving every configuration (or σ an exchange, or fixing x) are the hypotheses each '
            'law names; the laws are stated on runs Law.run and on processes.',
      'zh': '不加公理；交换与 σ 移动每个配置（或 σ 为对换、或固定 x）是各定律所列的假设；定律陈述在运行 Law.run 与过程上。'}],
    [{'en': 'Groups of symmetries (the four-group of 錯 and 綜, and 互), symmetries with fixed points beyond keeps_fixed, '
            'and which symmetries actual unfoldings keep.',
      'zh': '对称群（錯与綜的四元群，以及互），keeps_fixed 之外有不动点的对称，实际展开保持哪些对称。', 'kind': 'scope'},
     {'en': 'That keeping or erasing a difference is better; the earlier claim that «一» structurally does not exist.',
      'zh': '保持或抹去一个差别更好；早期“«一»结构上不存在”的主张。', 'kind': 'non-implication'}],
    {'en': 'Groups of symmetries and 互 (Y3, Becoming.HexagramLaws); an independent review.',
     'zh': '对称群与互（Y3，Becoming.HexagramLaws）；独立审查。'},
    CORR('The earlier 义理·拓扑 (§四, §九) argues that a fixed-point-free symmetry is never erased by a law keeping it, '
         'proved there for instances only (SSBX review §3.2, G2); its table equating Borsuk–Ulam with the second law is '
         'not taken.',
         '早期义理·拓扑（第四、九节）论证保持无不动点对称的律从不抹去它，那里只就实例证明（SSBX 审读第 3.2 节 G2）；其把 Borsuk–Ulam 等同于第二定律的表不取。'),
    ['what a commuting law keeps apart', '交换之律保持什么分开', 'to merge what a symmetry tells apart, a law must break it',
     'Becoming.Law.Commutes.apart', 'Becoming.Law.Commutes.breaks', 'Becoming.Hexagram.wane_breaks'],
    [REC_DEP, DIAG_DEP, BRANCH_DEP,
     dep('hexagrams-on-the-spine', 'application',
         'Applies the general law to waxWane, complement, waxWane_complement, six_steps, wane_six, pairOf and changes.',
         '把一般律用于 waxWane、complement、waxWane_complement、six_steps、wane_six、pairOf 与 changes。',
         'The law of waxing and waning commutes with the complement; the waning into 坤.', '消息律与错卦交换；尽归坤之消。',
         'The Changes as an instance.', '周易作为实例。', 'None.', '无。', src('Hexagrams')),
     dep('generalization-through-lumping', 'formal-reuse',
         'Reuses Learning.Lumped and goAlike_iff_lumped.', '复用 Learning.Lumped 与 goAlike_iff_lumped。',
         'A determined law goes alike under a map exactly where its next value, read through the map, is lumped.',
         '决定性律在一个映射下同行，恰当其下一值经映射读出时被归并。',
         'The law goes alike across the pairs.', '律在对之间同行。', 'None.', '无。', src('Learning')),
     dep('every-loss-passes-a-juncture', 'formal-reuse',
         'Reuses Branching.Juncture: a symmetric exchange carries junctures.', '复用 Branching.Juncture：对称的对换承载关节。',
         'Junctures of a process.', '过程的关节。', 'Junctures in pairs.', '成对的关节。', 'σ an exchange.', 'σ 为对换。',
         src('Junctures'))],
    [{'id': 'selection-through-a-model-of-the-options', 'detail': {
        'en': 'Relabel.Equivariant.tied keeps a tie through an exchange in selection; Law.Commutes.keeps_fixed is the fixed '
              'case for a law of change, and Law.Commutes.apart the free case. No instance theorem.',
        'zh': 'Relabel.Equivariant.tied 在选择中经对换保持并列；Law.Commutes.keeps_fixed 是变化之律的固定情形，Law.Commutes.apart 是自由情形。无实例定理。'}}],
    [(src('Diagonal'), ['Becoming.Diagonal.revision_never_rests', 'Becoming.Diagonal.Moves'])],
    TOPOLOGY_SRC)

# G3
record(
    'revision-with-an-undecided-value', 'Undecided',
    {'en': 'Revision with an undecided value', 'zh': '带未定值的修正'},
    {'en': 'With an undecided value below true and false, revision of N sentences speaking only of one another, run from '
           'all undecided, settles within N steps, exactly, at the least fixed point. Where two-valued revision has no '
           'fixed point, every fixed point leaves a sentence undecided.',
     'zh': '有一个低于真与假的未定值时，只彼此言说的 N 个句子从全未定起的修正，在 N 步内停于最小不动点，此界确切。二值修正没有不动点时，每个不动点留下一个未定的句子。'},
    [('Three values with u below t and f in information and the strong tables; evaluation is monotone in information '
      'and agrees with the two-valued tables on decided values.',
      '三个值，信息序上 u 低于 t 与 f，用强表；求值对信息序单调，在已定值上与二值表一致。',
      ['Value', 'Le', 'Term', 'eval', 'eval_mono', 'eval_mono_below', 'eval_embed']),
     ('A term with no constant is undecided where every sentence is, so a system with no constant stays wholly undecided '
      'along its run of revision.',
      '不含常量的项在每个句子都未定处未定，所以不含常量的系统沿其修正之运行始终全未定。',
      ['ConstantFree', 'eval_undecided', 'stays_undecided']),
     ('Revision run from all undecided rises at every step; for N closed sentences it settles within N steps and stays, '
      'at the least fixed point; readings on a list that only rise settle by the list\'s length.',
      '从全未定起的修正之运行每步上升；对 N 个封闭句子，它在 N 步内停住并保持，在最小不动点；列表上只升不降的读法按列表长度停住。',
      ['revise', 'stage', 'Closed', 'Steady', 'stage_up', 'stage_mono', 'settles_within', 'settles', 'settled_from',
       'stage_fixed', 'stage_le_fixed', 'least_fixed']),
     ('The bound is exact: in the chain whose first sentence says true and each next denies the one before, N + 1 '
      'sentences are steady at step N + 1 and not at N.',
      '此界确切：在首句说真、后句各否定前句的链中，N + 1 个句子在第 N + 1 步稳定，在第 N 步不稳定。',
      ['chain', 'chain_undecided', 'chain_decided', 'chain_exact']),
     ('The liar rests undecided, and a run of its revision rests exactly where it is undecided; the truth-teller keeps '
      'its start and rests undecided from all undecided.',
      '说谎者停于未定，其修正之运行恰在它未定处停住；诚实者保持其起点，从全未定起停于未定。',
      ['liar_rests', 'liar_rests_iff', 'truthTeller_keeps', 'truthTeller_rests']),
     ('Where two-valued revision of a closed system has no fixed point, every fixed point and every resting run leaves a '
      'sentence undecided; the liar never rests with two values and rests undecided with three.',
      '封闭系统的二值修正没有不动点时，每个不动点、每条停住的运行都留下一个未定句子；说谎者二值时从不停息，三值时停于未定。',
      ['undecided_of_moves', 'least_undecided', 'rest_undecided', 'liar_two_valued_never_rests', 'liar_undecided',
       'liar_both_sides']),
     ('No map monotone in information moves every value; the run of a monotone map from the undecided value rests from '
      'its first step, so the diagonal\'s gap needs a map that is not monotone; a family of three-valued readings within '
      'what it reads is still incomplete.',
      '对信息序单调的映射都不移动每个值；单调映射从未定值出发的运行从第一步起停住，所以对角线的缺口需要不单调的映射；在所读之中的三值读法族仍不完备。',
      ['monotone_fixed', 'monotone_not_moves', 'neg_not_moves', 'monotone_run_rests', 'never_rests_not_monotone',
       'moves_not_monotone', 'incomplete'])],
    [{'en': 'No axiom; finitely many sentences closed among themselves (Closed) for the settling laws; the absence of a '
            'two-valued fixed point is a hypothesis of the undecided laws.',
      'zh': '不加公理；停住诸律要求有限个彼此封闭的句子（Closed）；二值不动点不存在是未定诸律的假设。'}],
    [{'en': 'Infinitely many sentences, where the least fixed point needs a limit stage; fixed points other than the '
            'least; how many sentences stay undecided.',
      'zh': '无穷多个句子，那里最小不动点需要极限阶段；最小者之外的不动点；有多少句子保持未定。', 'kind': 'scope'},
     {'en': 'That undecided is a third truth, or that the liar is resolved: the undecided value is what revision has not '
            'decided.', 'zh': '未定是第三种真，或说谎者被解决了：未定值是修正尚未决定者。', 'kind': 'non-implication'}],
    {'en': 'Infinitely many sentences with a limit stage; a measure of what stays undecided; an independent review.',
     'zh': '带极限阶段的无穷多个句子；对保持未定者的度量；独立审查。'},
    CORR('The earlier 义理·形式逻辑 (§三) states Kleene–Kripke revision and a 三值保守律 (U ⇏ ⊤), proved there only in '
         'instances (SSBX review §3.2, G3); the third value is read as 疑, what revision has not decided.',
         '早期义理·形式逻辑（第三节）陈述 Kleene–Kripke 修正与三值保守律（U ⇏ ⊤），那里只就实例证明（SSBX 审读第 3.2 节 G3）；第三值读作疑，即修正尚未决定者。'),
    ['revision with an undecided value', '带未定值的修正', 'the gap reappears as undecidedness', 'Kleene strong tables',
     'Kripke least fixed point (finite case)', 'Becoming.Undecided.least_fixed', 'Becoming.Undecided.undecided_of_moves'],
    [REC_DEP, DIAG_DEP],
    [{'id': 'every-loss-passes-a-juncture', 'detail': {
        'en': 'Becoming.Junctures uses settles_within to decide reach on listed configurations.',
        'zh': 'Becoming.Junctures 用 settles_within 在可列配置上判定可达。'}}],
    [],
    LOGIC_SRC)
