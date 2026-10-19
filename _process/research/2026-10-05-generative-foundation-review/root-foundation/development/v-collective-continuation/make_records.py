#!/usr/bin/env python3
"""Write V's five records: python3 -B make_records.py CORE_RECEIPT   (from the checkout root, after apply_text.py)

Every declaration cited is resolved against the receipt's audited declarations of its module (a short name must
match exactly one declaration by suffix), and the receipt must bind each module's current bytes."""
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
SOURCE = 'sources/15-codex-theory-conversations/2026-10-19-collective-continuation.md'
RECORDS = ROOT / 'theories/becoming/results/records'
core_id = sys.argv[1]
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
assert re.search(r'^## 193\. What a collective\'s continuation needs \(V\)$', (ROOT / STUDY).read_text(), re.M)


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


def record(rid, mod, title, statement, laws, hypotheses, dns, counterexamples, nxt, corr, aliases, deps, related,
           extra_refs):
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
        'hypotheses': hypotheses, 'does_not_show': dns, 'counterexamples': counterexamples,
        'standard_boundaries': BOUNDS,
        'validation_scope': {
            'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {n_decl} declarations '
                  f'of Becoming.{mod}, {n_thm} of them theorems, have empty axiom reports; the checker verifies core purity. '
                  'Built in scratch by an Opus prover, reviewed by a separate Opus reviewer against the brief, fixed; '
                  'author review in study section 193; not independently reviewed by a person.',
            'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.{mod} 的 {n_decl} 项声明（{n_thm} 项定理）公理报告为空；'
                  '检查器并核对核心纯净。由一个 Opus 证明者在草稿中构建，由另一个 Opus 审查者依简报审查并修正；作者审查见研究第 193 节；'
                  '未经人的独立审查。'},
        'next_delta': nxt, 'correspondence': corr, 'canonical_source': src(mod), 'aliases': aliases,
        'dependencies': deps, 'related': related,
        'references': [{'path': src(mod), 'role': 'proof', 'declarations': sorted(d['name'] for d in decls(mod)['declarations']),
                        'sha256': sha(src(mod))}]
        + [dict({'path': p, 'role': 'proof'}, **({'declarations': ds} if ds else {}), sha256=sha(p)) for p, ds in extra_refs]
        + [{'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
           {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
           {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
           {'path': SOURCE, 'role': 'provenance', 'sha256': sha(SOURCE)}],
        'proof_bindings': [{'source': src(mod), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{mod}',
                            'success_pointer': '/status', 'success_value': 'passed'}],
        'history': [{
            'en': '19 October 2026: added (V), on Ren\'s "does our theories fully cover this?" with a pasted account of '
                  'social viability, "please, spawn a swarm of subagents, think hard, let\'s fully complete this" and "I agree '
                  'with your push back, let\'s think about how to resolve them elegantly"; study section 193.',
            'zh': '2026年10月19日：新增（V），按 Ren 随一段社会可存续性文字所问的"does our theories fully cover this?"，以及'
                  '"please, spawn a swarm of subagents, think hard, let\'s fully complete this"与"I agree with your push back, '
                  'let\'s think about how to resolve them elegantly"；研究第 193 节。'}],
    }
    path = RECORDS / f'{rid}.json'
    assert not path.exists(), ('record exists', rid)
    path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('written', rid)


CORR_EN = ('An account of social viability Ren brought on 19 October 2026 lists eight constraints and a unifying ninth; '
           'the AI\'s mapping found this one {gap}. Ren\'s words are provenance, not warrant; the reading onto collectives '
           'is the AI\'s (D48).')
CORR_ZH = ('Ren 于 2026年10月19日带来的一段社会可存续性文字列出八条约束与统一它们的第九条；AI 的对照发现此条{gap}。Ren 的话是出处，不是依据；'
           '读到集体上是 AI 的（D48）。')
REC_DEP = dep('recurrence-without-premise', 'formal-reuse',
              'Reuses Law.orbit and the run of a determined law, Law.run, whose states are the orbit.',
              '复用 Law.orbit 与决定性律的运行 Law.run，其状态即轨道。',
              'The course of a determined law as a run of the spine.', '决定性律的进程作为脊柱的运行。',
              'The courses the laws are stated on.', '诸定律所陈述的进程。', 'None.', '无。', src('Recurrence'))

# V1
record(
    'giving-that-waits-on-giving', 'Withholding',
    {'en': 'Giving that waits on giving', 'zh': '等待给出的给出'},
    {'en': 'Where giving waits on giving: with memory one withholding ends all giving in a family it reaches, from then on; '
           'without memory withholding passes out where no chain of waits is long enough and returns around every loop. '
           'More waiting is less giving.',
     'zh': '给出等待给出之处：有记忆时，一处扣留永久结束它所及之族的一切给出；无记忆时，扣留在没有足够长的等待链处消散，并沿每个回路复返。等待越多，给出越少。'},
    [('With memory, a formation gives at step n exactly where every formation within n waits of it gave at the start; '
      'giving at n + 1 gives giving at n, so withholding stays; it spreads downstream along every chain of waits.',
      '有记忆时，一个形成在第 n 步给出，恰当在 n 次等待之内的每个形成在开始时给出；第 n + 1 步给出推出第 n 步给出，因此扣留保持；扣留沿每条等待链向下游扩散。',
      ['waitsAll', 'Chain', 'Within', 'waitsAll_closed', 'waitsAll_gives_earlier', 'waitsAll_withholding_stays',
       'waitsAll_withholding_stays_le', 'withholding_spreads']),
     ('One withholding ends all giving in a family reached from it: where every formation lies within d waits of b and '
      'b withholds at the start, every formation withholds at every step from d on; two courses withholding everywhere '
      'go on alike.',
      '一处扣留结束它所及之族的一切给出：每个形成都在 b 的 d 次等待之内且 b 在开始时扣留，则从第 d 步起每个形成在每一步扣留；两条处处扣留的进程此后一致。',
      ['withholding_absorbs', 'total_withholding_merges']),
     ('Without memory, a formation gives at step n exactly where every formation with a chain of exactly n waits to it '
      'gave at the start; where no chain of L waits exists, every formation gives from step L on, whatever the start '
      '(exact in Line); on a loop of p waits, withholding returns at every multiple of p.',
      '无记忆时，一个形成在第 n 步给出，恰当以恰好 n 次等待链到它的每个形成在开始时给出；不存在 L 次等待的链时，无论开始如何，每个形成从第 L 步起给出（在 Line 中精确）；在 p 次等待的回路上，扣留在 p 的每个倍数处复返。',
      ['answers', 'answers_closed', 'no_longer_chain', 'gives_without_chain', 'Line.passes_out_exact',
       'withholding_returns']),
     ('More waiting, less giving: adding waits takes giving away at every step under both laws.',
      '等待越多，给出越少：增加等待在两条律下都在每一步减少给出。',
      ['waitsAll_more_waiting', 'answers_more_waiting']),
     ('Restoring needs another law: in Ring, three formations each waiting on the one before, with memory all withhold '
      'from step 2, exactly; without memory the withholding circulates; under the law in which one formation gives '
      'whatever it waits on, every formation gives from step 3 on from every start, exactly.',
      '恢复需要另一条律：在 Ring 中，三个形成各等待前一个，有记忆时从第 2 步起全部扣留，且恰好如此；无记忆时扣留循环；在一个形成不论所等待者如何都给出的律下，从每个开始，每个形成从第 3 步起给出，且恰好如此。',
      ['givesFirst', 'Ring.waitsAll_absorbs_exact', 'Ring.answers_circulates', 'Ring.answers_returns',
       'Ring.givesFirst_restores', 'Ring.givesFirst_restores_exact'])],
    [{'en': 'No axiom and no premise about the formations or the relation of waiting: no finiteness, no decision of '
            'equality or of giving. The relation of waiting is given; every law is stated on runs Law.run of the two laws.',
      'zh': '不加公理，对形成与等待关系不加前提：不要求有限，不要求相等或给出可判定。等待关系是给定的；每条定律都陈述在两条律的运行 Law.run 上。'}],
    [{'en': 'How the relation of waiting forms, or amounts of giving and thresholds of waiting (giving where at least k of '
            'what one waits on gave).', 'zh': '等待关系如何形成，或给出的数量与等待的阈值（所等待者中至少 k 个给出时才给出）。',
      'kind': 'scope'},
     {'en': 'Which laws that give first restore giving in a general family; that cooperation is good, or which giving '
            'supports 生生.', 'zh': '在一般的族中哪些先给出的律能恢复给出；合作是好的，或哪种给出支持生生。', 'kind': 'non-implication'}],
    [],
    {'en': 'Thresholds and amounts; restoring laws in general families; deriving the waiting relation from a flow; an '
           'independent review.', 'zh': '阈值与数量；一般族中的恢复律；由流导出等待关系；独立审查。'},
    {'en': CORR_EN.format(gap='partly carried, through the selfishness spiral, and with no law'),
     'zh': CORR_ZH.format(gap='只经自私螺旋部分承载，没有定律')},
    ['giving that waits on giving', '等待给出的给出', 'withholding absorbs', 'Becoming.withholding_absorbs',
     'Becoming.withholding_returns', 'cooperation among strangers (reading)'],
    [REC_DEP],
    [{'id': 'how-a-carried-difference-grows', 'detail': {
        'en': 'Parallel, with no instance theorem: there a finite order is exact where no chain of couplings is long enough '
              'and what reaches a loop keeps arriving; here withholding passes out and returns.',
        'zh': '平行，无实例定理：那里在没有足够长耦合链处有限阶精确，抵达回路者持续到来；这里扣留消散与复返。'}},
     {'id': 'target-capture', 'detail': {
        'en': 'As a perturbed state is re-absorbed under one rule, giving is regained only under another law.',
        'zh': '如同受扰状态在一条规则下被重新吸收，给出只在另一条律下恢复。'}}],
    [])

# V2
record(
    'whether-a-loop-closes-a-difference', 'Widening',
    {'en': 'Whether a loop closes, keeps or widens a difference', 'zh': '回路闭合、保持还是扩大差别'},
    {'en': 'A loop closes a difference only through a link that gives back less than it received. A return map below '
           'what it receives closes within d turns, exactly. With whole-number strengths a loop closes at once, keeps the '
           'difference or runs away: nothing between.',
     'zh': '回路只经一个给回少于所受的环节闭合差别。低于所受的回返映射在 d 圈之内闭合，且恰好如此。整数强度下，回路立即闭合、保持差别或失控：中间没有。'},
    [('A return map giving back what it receives keeps a difference; where every link gives on at least what it '
      'receives, the difference never falls below where it began, so a loop that closes a difference has a link giving '
      'back less than it received, found.',
      '给回所受的回返映射保持差别；每个环节所传至少等于所受时，差别从不低于起点，因此闭合差别的回路有一个给回少于所受的环节，且可找到。',
      ['returnMap', 'kept_of_identity', 'loop_kept', 'never_closes_of_no_less', 'closing_needs_less']),
     ('A return map with f 0 = 0 and f x < x at every positive x closes within d turns and stays closed (an instance of '
      'Lasting.Variant.reaches), exactly by Nat.pred; a closing loop merges two differences and is not lossless.',
      'f 0 = 0 且对每个正 x 有 f x < x 的回返映射在 d 圈之内闭合并保持闭合（Lasting.Variant.reaches 的实例），由 Nat.pred 知其精确；闭合的回路合并两个差别，不是无损的。',
      ['difference_variant', 'closes_within', 'closes_within_exact', 'closing_merges', 'closing_not_lossless']),
     ('Taking a constant off leaves d - n * c after n turns, closed exactly from the least n with n * c ≥ d; a cut '
      'closes at once where every later link gives nothing for nothing, and is reopened otherwise.',
      '每圈减去常数 c，n 圈后余 d - n * c，恰从满足 n * c ≥ d 的最小 n 起闭合；切断在其后每个环节无来则无往之处立即闭合，否则被重新打开。',
      ['orbit_sub_const', 'sub_const_closes', 'sub_const_open', 'cut_closes', 'cut_reopened']),
     ('Monotone return maps settle within d turns at a fixed value where f d ≤ d (exact) and never fall where d ≤ f d; '
      'doubling links run away, at least 2 ^ n * d after n turns, exactly for one doubling link.',
      '单调回返映射在 f d ≤ d 时于 d 圈之内停于不动值（精确），在 d ≤ f d 时从不下降；加倍的环节失控，n 圈后至少 2 ^ n * d，单个加倍环节恰好如此。',
      ['never_rises', 'never_falls', 'settles_within', 'settles_within_exact', 'runs_away', 'runs_away_unbounded',
       'doubling_exact']),
     ('With links multiplying by whole-number strengths, product 0 closes at the first turn, product 1 keeps the '
      'difference, product at least 2 exceeds every bound; no such loop closes gradually, while taking one off does.',
      '各环节以整数强度相乘时，乘积为 0 在第一圈闭合，为 1 保持差别，至少为 2 则超过一切界；这样的回路都不逐步闭合，而减一则可以。',
      ['scaling', 'returnMap_scaling', 'whole_strengths', 'nothing_between', 'gradual_needs_another_link'])],
    [{'en': 'No axiom; the difference is a natural number and a link a map of natural numbers; every law is stated on runs '
            'Law.run of the return map; the hypotheses each law names (monotonicity, f 0 = 0, links giving nothing for '
            'nothing) are hypotheses.',
      'zh': '不加公理；差别是自然数，环节是自然数的映射；每条定律都陈述在回返映射的运行 Law.run 上；各定律所列的条件（单调、f 0 = 0、无来则无往的环节）是假设。'}],
    [{'en': 'A loop of Rejoining read as a return map: the difference here is one number, not levels at many conditions.',
      'zh': '把 Rejoining 的回路读作回返映射：这里的差别是一个数，不是多个条件上的水平。', 'kind': 'scope'},
     {'en': 'That closing a difference is better than keeping or widening it; real strengths.',
      'zh': '闭合差别优于保持或扩大它；实数强度。', 'kind': 'non-implication'}],
    [],
    {'en': 'Real strengths, where a multiplication below one closes gradually; a loop of Rejoining read as a return map; '
           'many conditions at once; an independent review.',
     'zh': '实数强度，其中小于一的乘法逐步闭合；把 Rejoining 的回路读作回返映射；多个条件同时；独立审查。'},
    {'en': CORR_EN.format(gap='(bounded conflict) partial: runaway was proved, closing was not; it also answers, for loops, '
                              'the chapter\'s open question which law closes rather than widens a difference'),
     'zh': CORR_ZH.format(gap='（有界冲突）部分承载：失控已证，闭合未证；它也就回路回答了本章的开放问题：哪条律闭合而非扩大差别')},
    ['whether a loop closes a difference', '回路是否闭合差别', 'closing needs a link that gives back less',
     'Becoming.Widening.closing_needs_less', 'Becoming.Widening.whole_strengths', 'bounded conflict (reading)'],
    [REC_DEP],
    [{'id': 'where-two-courses-rejoin', 'detail': {
        'en': 'There a difference closes only through a response; here which return laws close, keep or widen it.',
        'zh': '那里差别只经回应闭合；这里哪些回返律闭合、保持或扩大它。'}},
     {'id': 'how-often-couplings-act', 'detail': {
        'en': 'Parallel to Frequency\'s doubling at every return, with no instance theorem; here the count is of turns.',
        'zh': '与 Frequency 每次回返加倍平行，无实例定理；这里计的是圈数。'}}],
    [(src('Lasting'), ['Becoming.Lasting.Variant.reaches', 'Becoming.Lasting.orbit_mono'])])

# V3
record(
    'how-fast-a-rule-may-change', 'Pace',
    {'en': 'How fast a rule may change', 'zh': '规则可以多快地改变'},
    {'en': 'A rule that never reads the fast level is unreached and loses what it merges; a fast difference reaches a rule '
           'only at a reading step. Given two values, a stretch of L steps fixes every pair of held courses with at most N '
           'states exactly when L ≥ 2N − 1.',
     'zh': '从不读快层的规则不被触及，并失去它所合并者；快层的差别只在读取之步触及规则。给定两个值，L 步的段落确定每对至多 N 个状态的持守进程，恰当 L ≥ 2N − 1。'},
    [('A two-level course, the fast configuration stepping by a rule that changes only at reading steps, is a run of one '
      'law; a rule that never reads is kept, nothing the fast level meets reaches it, and under it what is lost stays '
      'lost and merges lose configurations.',
      '两层进程（快构形依规则步进，规则只在读取之步改变）是一条律的运行；从不读取的规则保持不变，快层所遇的都触及不到它，在它之下失去的保持失去，合并失去构形。',
      ['paced', 'paced_run', 'rule_kept', 'rule_unreached', 'never_reads_lost', 'never_reads_merged',
       'never_reads_loses', 'byRule_reabsorbed']),
     ('A fast difference reaches the rule only at a reading step: up to and including the first reading step the rule is '
      'the one at the start, exact in Copying; regaining what a fixed rule loses needs a change of rule (Switching).',
      '快层的差别只在读取之步触及规则：直到并包括第一个读取之步，规则都是开始时的那个，在 Copying 中精确；恢复固定规则所失去的需要改变规则（Switching）。',
      ['rule_until_reading', 'rule_alike_until_reading', 'rule_at_reading', 'Copying.rule_parts',
       'Switching.fixed_loses', 'Switching.changing_regains']),
     ('Given two values, a stretch of L steps fixes every pair of courses with at most N states that held rules generate '
      'exactly when L ≥ 2N − 1: shorter stretches dissolve (from prefix_short_twice), longer ones fix (from bounded_agree); '
      'within a paced course a rule held that long is fixed over its stretch.',
      '给定两个值，L 步的段落确定由持守规则生成的每对至多 N 个状态的进程，恰当 L ≥ 2N − 1：更短的段落消散（由 prefix_short_twice），更长的确定（由 bounded_agree）；在分层进程中持守这么久的规则在其段落上被确定。',
      ['heldCourse', 'held_statesBelow', 'held_realizes', 'dissolving', 'held_fixed', 'stretch_fixed', 'StretchFixes',
       'pace_law']),
     ('A course of configurations read whole, with at most N states, is fixed among every run of every law by its first '
      'N + 1 steps, exactly.',
      '整体读取、至多 N 个状态的构形进程，在每条律的每次运行之间由其前 N + 1 步确定，且恰好如此。',
      ['whole_fixed', 'whole_fixed_exact'])],
    [{'en': 'No axiom; the fast law, the reading law and the reading steps are given; courses with at most N states are '
            'read through a map; the pace law quantifies over fast levels in Type, the fixing side in every universe.',
      'zh': '不加公理；快律、读取律与读取之步是给定的；至多 N 个状态的进程经一个映射读取；步调律对 Type 中的快层量化，确定的一侧在每个宇宙中成立。'}],
    [{'en': 'Which rule a slow level reads into, that it reads at stretches of any length, or how many states an actual '
            'fast level has.', 'zh': '慢层读入哪条规则，它以任何长度的段落读取，或实际快层有多少状态。', 'kind': 'scope'},
     {'en': 'That a layered pace is better than another; many levels and rules that change by chance.',
      'zh': '一种分层步调优于另一种；多层与随机改变的规则。', 'kind': 'non-implication'}],
    [],
    {'en': 'Many levels; noisy rules; which reading law adapts; an independent review.',
     'zh': '多层；有噪声的规则；哪条读取律能适应；独立审查。'},
    {'en': CORR_EN.format(gap='(stability with adaptability) partial, with no law of the pace of a rule'),
     'zh': CORR_ZH.format(gap='（稳定与适应）部分承载，没有关于规则步调的定律')},
    ['how fast a rule may change', '规则可以多快地改变', 'the pace law', 'Becoming.Pace.pace_law',
     'stability with adaptability (reading)'],
    [REC_DEP,
     dep('identification-where-bounded', 'formal-reuse',
         'Reuses bounded_agree and the witness of prefix_short_twice: the pace law is identification read on held rules.',
         '复用 bounded_agree 与 prefix_short_twice 的见证：步调律是在持守规则上读的辨认。',
         'A bounded prefix fixes the course at the exact length N + N\' − 1.', '有界前缀在精确长度 N + N\' − 1 处确定进程。',
         'What a stretch of a held rule fixes.', '持守规则的段落确定什么。', 'Courses with at most N states.',
         '至多 N 个状态的进程。', src('Identification'))],
    [{'id': 'target-capture', 'detail': {
        'en': 'byRule_reabsorbed is the instance of Law.perturbation_reabsorbed on the two-level course.',
        'zh': 'byRule_reabsorbed 是 Law.perturbation_reabsorbed 在两层进程上的实例。'}}],
    [(src('Identification'), ['Becoming.Identification.bounded_agree', 'Becoming.Identification.prefix_short_twice'])])

# V4
record(
    'a-pattern-lasts-through-passing', 'Passing',
    {'en': 'A pattern outlasting its carriers lasts through passing', 'zh': '比承载者更持久的样式经传递而持续'},
    {'en': 'A pattern present from T on whose carriers are brief for d has a carrier beginning within every d steps; under '
           'the passing premise it is passed across one of every d steps, one empty step ends it, and if passing stops it '
           'ends within d steps.',
     'zh': '从 T 起存在、其承载者对 d 短暂的样式，在每 d 步之内有承载者开始；在传递前提下，它在每 d 步中的一步被传递，一步无承载者即结束，传递停止则在 d 步之内结束。'},
    [('Present at every step from T on, its carriers brief for d, some carrier begins within every d consecutive steps '
      '(an instance of Covered.arises_within).',
      '从 T 起每一步都存在、其承载者对 d 短暂，则每 d 个连续步之内有承载者开始（Covered.arises_within 的实例）。',
      ['carrying', 'carrying_iff', 'Present', 'begins_within']),
     ('Under the passing premise every beginning is a passing, and the pattern is passed across one of every d '
      'consecutive steps from T on; PatternRelay attains the bound.',
      '在传递前提下，每次开始都是一次传递，样式从 T 起在每 d 个连续步中的一步被传递；PatternRelay 达到此界。',
      ['PassesAt', 'ByPassing', 'ByPassing.begins_passed', 'ByPassing.trace', 'ByPassing.passes_within',
       'PatternRelay.shifts']),
     ('Under the passing premise a step with no carrier is followed by none with one; with carriers brief for d and no '
      'passing from T on, no formation carries it from T + d on, attained in PatternRelay.',
      '在传递前提下，无承载者的一步之后再无有承载者的一步；承载者对 d 短暂且从 T 起无传递，则从 T + d 起无形成承载它，在 PatternRelay 中达到。',
      ['ByPassing.present_back', 'ByPassing.empty_stays', 'ByPassing.ends_within', 'PatternRelay.relay',
       'PatternRelay.stopped_relay'])],
    [{'en': 'No axiom; the passing premise Web.ByPassing is a hypothesis, supplied as transmission is in Becoming.Evolution; '
            'every law is stated for any web, its activity read as carrying.',
      'zh': '不加公理；传递前提 Web.ByPassing 是假设，如同 Becoming.Evolution 中的传承那样给定；每条定律对任何网陈述，其活动读作承载。'}],
    [{'en': 'Whether carrying forms by passing, which formations pass, when or to which formations, or whether a pattern '
            'changes as it is passed.', 'zh': '承载是否经传递形成，哪些形成传递、何时、传给哪些形成，或样式在传递中是否改变。',
      'kind': 'scope'},
     {'en': 'Which patterns are worth passing, or what carrying one does to the carriers or to anything else.',
      'zh': '哪些样式值得传递，或承载它对承载者或别的什么做了什么。', 'kind': 'non-implication'}],
    [],
    {'en': 'Passing derived from descent (Flow.DescendsAt) rather than supplied; patterns that change as they pass; an '
           'independent review.', 'zh': '由世系（Flow.DescendsAt）导出传递而非给定；在传递中改变的样式；独立审查。'},
    {'en': CORR_EN.format(gap='(forming the next members) partial: the whole persists through the generation of its '
                              'parts, but no law of passing a pattern'),
     'zh': CORR_ZH.format(gap='（形成下一代成员）部分承载：整体经其部分的生成而持续，但没有样式传递的定律')},
    ['a pattern lasts through passing', '样式经传递而持续', 'one empty step ends it', 'Becoming.Web.ByPassing.ends_within',
     'forming the next members (reading)'],
    [dep('whole-persists-through-generation', 'formal-reuse',
         'Reuses Web.Brief, Web.Covered and Covered.arises_within: begins_within is its instance on the formations of the '
         'web as parts.', '复用 Web.Brief、Web.Covered 与 Covered.arises_within：begins_within 是其以网中形成为部分的实例。',
         'Parts covering the steps need a part arising within every d steps.', '覆盖诸步的部分需要每 d 步之内有部分产生。',
         'That a lasting pattern of brief carriers has carriers beginning.', '短暂承载者的持久样式有承载者开始。',
         'Carriers brief for d.', '承载者对 d 短暂。', src('Wholes'))],
    [{'id': 'transmission-is-inheritance-and-need', 'detail': {
        'en': 'The passing premise plays the role transmission plays in evolution: supplied, not derived.',
        'zh': '传递前提所起的作用如同传承在演化中：给定，不导出。'}}],
    [(src('Wholes'), ['Becoming.Web.Covered.arises_within'])])

# V5
record(
    'conditions-kept-together', 'JointKeeping',
    {'en': 'Conditions kept together, and keeping a part', 'zh': '共同保持的条件，以及保持一个部分'},
    {'en': 'Under every course, guards decompose exactly; along some course they do not, and no rule on the separate '
           'keepabilities decides the joint one. No course leaving a part\'s guard decides neither renewal nor what the run '
           'does to others.',
     'zh': '在每条进程下，守卫恰好分解；沿某条进程则不，且没有作用于各自可保持性的规则决定联合的可保持性。没有进程离开一个部分的守卫，既不决定更新，也不决定运行对他者做了什么。'},
    [('No course leaves two guards together exactly where no course leaves either, and for a list exactly where no course '
      'leaves any.', '没有进程离开两个守卫的联合，恰当没有进程离开其中任一个；对一列守卫，恰当没有进程离开其中任何一个。',
      ['kernel_and_iff', 'AllOf', 'kernel_allOf_iff']),
     ('A guard is keepable where some run stays within it; keepable together gives keepable each, and the converse fails '
      'in ChoicePoint; where either guard lies in the kernel, keeping both is keeping the other; likewise for n steps.',
      '某次运行保持在守卫之内，则守卫可保持；联合可保持推出各自可保持，反之在 ChoicePoint 中不成立；任一守卫在核中时，保持两者即保持另一个；n 步亦然。',
      ['Keepable', 'Keepable.each', 'Keepable.of_keepsMoving', 'keepable_and_iff_of_kernel_left',
       'keepable_and_iff_of_kernel_right', 'KeptFor.each', 'ChoicePoint.each_not_joint',
       'ChoicePoint.keptFor_each_not_joint']),
     ('No rule on the separate answers decides the joint one: on ChoicePoint two configurations have both guards keepable '
      'and only one has them together; decisions exist, and for every F : Bool → Bool → Bool the joint decision is not F '
      'of the separate ones.',
      '没有作用于各自答案的规则决定联合的答案：在 ChoicePoint 上两个构形两个守卫都可保持，只有一个可联合保持；判定存在，对每个 F : Bool → Bool → Bool，联合的判定都不是各自判定的 F。',
      ['ChoicePoint.joint_differs', 'ChoicePoint.decisions_exist', 'ChoicePoint.no_rule_decides_joint',
       'ChoicePoint.no_respecting_rule_decides_joint']),
     ('Keeping a part decides neither renewal nor what the run does to others: in Renewable no course leaves the guard '
      '"the focal formation is active" from any configuration, while from one configuration one run renews and another '
      'consumes the sustaining formation\'s condition, which ends.',
      '保持一个部分既不决定更新，也不决定运行对他者做了什么：在 Renewable 中，从任何构形都没有进程离开“焦点形成活动”这一守卫，而从同一构形，一次运行更新，另一次消耗维持者的条件，后者终结。',
      ['Renewable.kept_part_not_renewal'])],
    [{'en': 'No axiom and no premise; which guards mark what each activity needs is supplied with each application.',
      'zh': '不加公理，不加前提；哪些守卫标出每个活动所需，随每个应用给定。'}],
    [{'en': 'Which choices an actual collective\'s continuation goes through, or a measure of joint keeping.',
      'zh': '实际集体的延续经过哪些选择，或联合保持的度量。', 'kind': 'scope'},
     {'en': 'That a kept collective is better than another, or that renewing is better than consuming.',
      'zh': '一个被保持的集体优于另一个，或更新优于消耗。', 'kind': 'non-implication'}],
    [],
    {'en': 'Joint keeping over a horizon with the choices given by a law of exchange; fault tolerance joined to '
           'Becoming.FaultEnvelopes; an independent review.',
     'zh': '在一个时域上、由交换律给出选择的联合保持；容错与 Becoming.FaultEnvelopes 相连；独立审查。'},
    {'en': CORR_EN.format(gap='carries two of the five pushbacks as laws: the product formula decides joint viability only '
                              'under every course, and survival of a part is not renewal'),
     'zh': CORR_ZH.format(gap='以定律承载五条反驳中的两条：乘积公式只在每条进程下决定联合可存续性，部分的存续不是更新')},
    ['conditions kept together', '共同保持的条件', 'keeping a part is not renewal',
     'Becoming.Viability.ChoicePoint.no_rule_decides_joint', 'Becoming.Renewable.kept_part_not_renewal',
     'viability is not a product (reading)'],
    [dep('becoming-renewal-reading', 'formal-reuse',
         'Reuses Renewable.class_belongs_to_the_run: one configuration, one run renewing and one consuming.',
         '复用 Renewable.class_belongs_to_the_run：同一构形，一次运行更新、一次消耗。',
         'Renewal belongs to the run.', '更新属于运行。', 'That keeping a part decides no renewal.',
         '保持一个部分不决定更新。', 'The renewable process.', '可更新过程。', src('Labelled')),
     dep('where-a-run-goes-on', 'formal-reuse', 'Reuses Onward.KeepsMoving.run for Keepable.of_keepsMoving.',
         '为 Keepable.of_keepsMoving 复用 Onward.KeepsMoving.run。', 'A run from each member of a family that keeps moving.',
         '持续移动之族每个成员出发的运行。', 'Keepability within finitely many configurations.', '有限构形内的可保持性。',
         'Finitely many configurations.', '有限多个构形。', src('Onward'))],
    [{'id': 'finite-continuation-plans', 'detail': {
        'en': 'Keeping for n steps through moves taken; here kept jointly versus kept each.',
        'zh': '经所取之移动保持 n 步；这里是联合保持与各自保持。'}}],
    [(src('Viability'), ['Becoming.Viability.Kernel', 'Becoming.Viability.Kernel.mono', 'Becoming.Viability.Kernel.run']),
     (src('Labelled'), ['Becoming.Renewable.class_belongs_to_the_run'])])
print('done')
