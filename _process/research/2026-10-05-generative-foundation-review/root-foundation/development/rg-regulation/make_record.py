#!/usr/bin/env python3
"""Write RG's record: python3 -B make_record.py CORE_RECEIPT   (from the checkout root, after apply_text.py and
ro_points.py, whose chapter and map edits the record binds)

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
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
STUDY = f'{RF}/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCES = 'theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md'
PASSAGES = f'{RF}/development/ro-relational-sources/passages.json'
SIMULATE = f'{RF}/development/rg-regulation/simulate.py'
RECORDS = ROOT / 'theories/becoming/results/records'
MOD = 'Regulation'
RID = 'two-sided-regulation-and-late-reading'
core_id = sys.argv[1]
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
section = re.search(r'^## (\d+)\. A level held from both sides, and a level read late \(RG\)$',
                    (ROOT / STUDY).read_text(), re.M)
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


def cited(module, names):
    """Declarations of another module, checked against the receipt."""
    have = {d['name'] for d in next(x for x in core['modules'] if x['module'] == f'Becoming.{module}')['declarations']}
    missing = [n for n in names if n not in have]
    assert not missing, missing
    return names


def dep(rid, en, zh, out_en, out_zh, in_en, in_zh, cond_en, cond_zh, evidence):
    return {'id': rid, 'relation': 'formal-reuse', 'detail': {'en': en, 'zh': zh},
            'interface': {'output': {'en': out_en, 'zh': out_zh}, 'input': {'en': in_en, 'zh': in_zh},
                          'conditions': {'en': cond_en, 'zh': cond_zh}, 'evidence': evidence}}


STATEMENT = {
    'en': 'Opposed from both sides within its gap, which is exactly not overshooting, a level settles at m; read l '
          'steps late, every rule needs a band at least 2(l+1)d wide, which the late return keeps; a late relay '
          'settles from every start held below exactly where a + (l+1)M <= b + 1.',
    'zh': '两侧相反且在距离之内（恰是不越过）时，水平定于 m；迟 l 步读时，每个规则所需之带至少宽 2(l+1)d，迟返恰保此带；'
          '迟读的阈值调节，自带下保持的每个起点，恰在 a + (l+1)M ≤ b + 1 时定于带内。'}
assert len(STATEMENT['en']) <= 300, len(STATEMENT['en'])
assert len(STATEMENT['zh']) <= 150, len(STATEMENT['zh'])

LAWS = [
    ('With balance across a step, the joint exchange departs from evenness by at most the level\'s gap to m on each '
     'side exactly where the next level lies between m and the present one: the bound is exactly no overshoot; for an '
     'opposing exchange the cases above, below and at m are exact.',
     '一步之间平衡时，合取交换在两侧偏离均衡都不超过水平与 m 的距离，恰是下一水平落在 m 与当前水平之间：界恰是不越过；'
     '对相反的交换，高于、低于与等于 m 三种情形都是确切的。',
     ['Flow.WithinGap', 'Flow.Opposes', 'Regulation.within_iff_between', 'Flow.withinGap_iff_between',
      'Flow.withinGap_iff_of_above', 'Flow.withinGap_iff_of_below', 'Flow.withinGap_iff_of_at']),
    ('Within the gap the gap does not rise and the level never crosses m; within it and opposing, the gap falls by at '
     'least one at each step where it is positive, by n over n steps, and the level is m from the step its gap is used '
     'up; from below, restoration with the bound reaches m exactly and stays.',
     '在距离之内，距离不升，水平永不越过 m；在其内且相反时，距离为正则每步至少降一，n 步降 n，距离用尽之步起水平为 m；'
     '自下且有界时，恢复恰到 m 而止。',
     ['Flow.gap_le_of_within', 'Flow.stays_between_at', 'Flow.gap_falls', 'Flow.regulates_at', 'Flow.regulates',
      'Flow.settles_at', 'Flow.settles_from', 'Flow.settles', 'Flow.restores_exactly']),
    ('Beyond the bound an opposing exchange crosses m; a balanced witness opposing the departure at every step and '
     'exceeding the gap at every step oscillates about m and is never m.',
     '越界的相反交换越过 m；一个平衡、每步都与偏离相反且每步都超出距离的证人在 m 两侧往复，永不为 m。',
     ['Flow.crosses_of_above', 'Flow.crosses_of_below', 'Regulation.Overshooting.balances',
      'Regulation.Overshooting.opposes', 'Regulation.Overshooting.beyond', 'Regulation.Overshooting.oscillates',
      'Regulation.Overshooting.never_at']),
    ('One side is not regulation: a balanced witness meets the premise of the law of restoration from every step and '
     'the bound at every step, does not oppose the departure above m, and stays above m.',
     '一侧不是调节：一个平衡的证人自每步起满足恢复律的前提、每步都在界内，却不与高于 m 的偏离相反，水平永在 m 之上。',
     ['Regulation.OneSided.balances', 'Regulation.OneSided.within', 'Regulation.OneSided.restores_premise',
      'Regulation.OneSided.not_opposes', 'Regulation.OneSided.above']),
    ('A rule reading l steps late answers alike two rests agreeing before T up to step T + l; the levels reached at '
     'T + l + 1 differ by exactly what the rests exchange differently over the l + 1 steps from T, so one raising and '
     'one lowering by d over the window leave no band narrower than 2(l + 1)d.',
     '迟 l 步读的规则，对在 T 之前相同的两种扰动直到 T + l 步都回答相同；在 T + l + 1 所达水平之差恰是两种扰动在自 T 起 '
     'l + 1 步中交换之差，所以一升 d、一降 d 时，没有带窄于 2(l + 1)d。',
     ['Regulation.Record', 'Regulation.Rule', 'Regulation.ReadsLate', 'Regulation.NetWithin', 'Flow.FollowsRule',
      'Regulation.ReadsLate.alike', 'Regulation.levels_alike', 'Regulation.late_spread', 'Regulation.late_band']),
    ('On the course a rule generates from a start, no rule reading l late keeps the level within [a, b], 0 < a, under '
     'every rest moving it by at most d a step unless a + 2(l + 1)d <= b.',
     '在规则自一个起点所生成的进程上，迟 l 步读的规则在每步至多移动 d 的一切扰动下把水平保持于 [a, b]（0 < a），'
     '仅当 a + 2(l + 1)d ≤ b。',
     ['Regulation.course', 'Regulation.courseFlow', 'Regulation.courseWeb', 'Regulation.courseFlow_follows',
      'Regulation.course_balances_of_pos', 'Regulation.no_narrower_band']),
    ('The late return, moving back what the rest exchanged l + 1 steps before, reads l late, needs only the level read '
     'l steps late and its own exchanges, and keeps every course within (l + 1)d of its start: the least band is '
     'attained.',
     '迟返把扰动在 l + 1 步之前的交换移回，它迟 l 步读，只需迟 l 步读到的水平与自己的交换，并使每个进程都在其起点的 '
     '(l + 1)d 之内：最小带宽可达。',
     ['Regulation.lateReturn', 'Regulation.lateReturn_readsLate', 'Regulation.lateReturn_reads_levels',
      'Regulation.lateReturn_keeps', 'Regulation.lateReturn_course_balances', 'Regulation.lateReturn_band']),
    ('The relay reading l late pushes M for a reading below a, pulls M for one above b and rests within; a level '
     'entering the band after l readings below goes on by exactly lM, and its own rise or fall, read late, feeds '
     'itself.',
     '迟 l 步读的阈值调节，读数低于 a 时推 M，高于 b 时拉 M，带内不动；在 l 次带下读数之后入带的水平恰再走 lM，'
     '它自己的升降迟读后自我延续。',
     ['Regulation.relay', 'Flow.RelaysLate', 'Regulation.push_ramp', 'Regulation.pull_ramp', 'Regulation.rest_ramp',
      'Regulation.overshoot', 'Regulation.undershoot', 'Regulation.rise_run', 'Regulation.fall_run']),
    ('From a start held below a for its first l + 1 steps the level rises by M a step, settles where its entry carried '
     'lM further is within b, and passes b otherwise.',
     '前 l + 1 步保持在 a 之下的起点，水平每步升 M；入带处再走 lM 仍在 b 之内则定于带内，否则越过 b。',
     ['Regulation.held_rise', 'Regulation.held_settles', 'Regulation.held_leaves']),
    ('An upward crossing is followed by a downward one and that by an upward one, so after every step the level is '
     'somewhere above b and somewhere below a; the start held at a - 1 crosses exactly where b + 2 <= a + (l + 1)M.',
     '向上越出之后有向下越出，其后又有向上越出，所以每一步之后水平都还会高于 b、也还会低于 a；保持于 a - 1 的起点，'
     '恰在 b + 2 ≤ a + (l + 1)M 时越出。',
     ['Web.UpCrossing', 'Web.DownCrossing', 'Regulation.upCrossing_next', 'Regulation.downCrossing_next',
      'Regulation.upCrossing_later', 'Regulation.crossing_oscillates', 'Regulation.held_crosses',
      'Regulation.held_oscillates']),
    ('The relay has a run from every start where (l + 1)M <= b + 1, by its window law on Law.orbit; for 0 < a <= b and '
     '0 < M, every start held below the band settles in it exactly where a + (l + 1)M <= b + 1.',
     '(l + 1)M ≤ b + 1 时，阈值调节以其窗口之律在 Law.orbit 上从每个起点都有运行；0 < a ≤ b、0 < M 时，带下保持的每个'
     '起点恰在 a + (l + 1)M ≤ b + 1 时定于带内。',
     ['Regulation.held_below_settles', 'Regulation.relayWindow', 'Regulation.relayLevel', 'Regulation.relayFlow',
      'Regulation.relayWeb', 'Regulation.relay_runs', 'Regulation.relay_threshold']),
]

COUNTER = [
    {'path': src(MOD), 'detail': {
        'en': 'Opposing on both sides without the bound is not regulation: Regulation.Overshooting balances and opposes '
              'the departure from m = 1 at every step, its level alternates between 2 and 0 and is never 1 '
              '(Overshooting.oscillates, Overshooting.never_at).',
        'zh': '两侧相反而无界不是调节：Regulation.Overshooting 每步平衡并与对 m = 1 的偏离相反，水平在 2 与 0 之间往复，'
              '永不为 1（Overshooting.oscillates、Overshooting.never_at）。'}},
    {'path': src(MOD), 'detail': {
        'en': 'The premise of the law of restoration, with the bound, does not give regulation: Regulation.OneSided meets '
              'both from every step and its level stays at 2 above m = 1 (OneSided.restores_premise, OneSided.above).',
        'zh': '恢复律的前提加上界并不给出调节：Regulation.OneSided 自每步起两者都满足，水平停在 2，高于 m = 1'
              '（OneSided.restores_premise、OneSided.above）。'}},
    {'path': src(MOD), 'detail': {
        'en': 'A relay entering its band does not settle there in general: past b + 2 <= a + (l + 1)M the start held at '
              'a - 1 leaves both ends without end (held_oscillates).',
        'zh': '阈值调节入带并不一般地定于带内：过 b + 2 ≤ a + (l + 1)M，保持于 a - 1 的起点两端越出而无尽（held_oscillates）。'}},
]
resolve(['Regulation.Overshooting.oscillates', 'Regulation.Overshooting.never_at', 'Regulation.OneSided.restores_premise',
         'Regulation.OneSided.above', 'Regulation.held_oscillates'])

BOUNDS = ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical', 'names-provisional',
          'omission-not-refutation']

DEPS = [
    dep('how-much-difference-arrives',
        'Uses Propagation\'s gap and its laws (gap_le_iff, gap_total, gap_comm, gap_zero) for the distance to m and the '
        'width of a band.',
        '以 Propagation 的距离及其定律（gap_le_iff、gap_total、gap_comm、gap_zero）表示与 m 的距离与带宽。',
        'The gap between two amounts, bounded exactly by each side, and bounded over a stretch by the gaps summed.',
        '两个量之间的距离，恰以两侧为界，在一段之上以诸距离之和为界。',
        'The gap to m falls under regulation; the spread between two courses under a late rule is the exchanged gap.',
        '调节下与 m 的距离下降；迟读规则下两个进程之差是所交换之差。',
        'Whole-number amounts.', '整数量。', src('Propagation')),
    dep('recurrence-without-premise',
        'Uses Law.orbit to iterate the relay\'s window law into a run from every start.',
        '以 Law.orbit 迭代阈值调节的窗口之律，得到自每个起点的运行。',
        'The orbit of a law from a state.', '一个律自一个状态的轨道。',
        'The relay\'s levels along its run, held for l + 1 steps and then moved by the relay\'s late reading.',
        '阈值调节沿其运行的水平：保持 l + 1 步，此后由迟读移动。',
        '(l + 1)M <= b + 1 for the run to balance.', '(l + 1)M ≤ b + 1，运行才平衡。', src('Recurrence')),
]

RELATED = [
    {'id': 'supported-renewal-recovery',
     'detail': {'en': 'Flow.restores is the one-sided law: giving more than taking below m reaches at least m. With the '
                      'bound it reaches m exactly (Flow.restores_exactly), and without the other side it is not '
                      'regulation (Regulation.OneSided).',
                'zh': 'Flow.restores 是单侧之律：低于 m 时给多于取，则至少到 m。有界时恰到 m（Flow.restores_exactly），'
                      '无另一侧则不是调节（Regulation.OneSided）。'}},
    {'id': 'own-count-misses-joint-excess',
     'detail': {'en': 'The excess laws lower a level above a need and raise one below it, each on one side; two-sided '
                      'regulation holds both sides with a bound.',
                'zh': '过量之律降低高于需要的水平、提高低于需要的水平，各在一侧；双向调节以界保持两侧。'}},
    {'id': 'assured-route-criterion',
     'detail': {'en': 'AssurancePlans.Regulation has two levels and an immediate response; a response that reads late '
                      'needs a band growing with the lateness.',
                'zh': 'AssurancePlans.Regulation 只有两档、即时响应；迟读的响应需要随迟而增的带。'}},
    {'id': 'whether-a-loop-closes-a-difference',
     'detail': {'en': 'A loop closes a difference only through a link giving back less; within the gap and opposing, '
                      'the difference to m closes by at least one a step at one condition.',
                'zh': '回路只经返还较少的环节闭合差异；在距离之内且相反时，一个条件上与 m 之差每步至少闭合一。'}},
    {'id': 'how-fast-a-rule-may-change',
     'detail': {'en': 'A slow rule reading a fast level at stretches; reading late, here, needs a band of 2(l + 1)d.',
                'zh': '慢规则分段读快层；这里迟读需要 2(l + 1)d 之带。'}},
    {'id': 'chinese-sources-on-the-spine',
     'detail': {'en': 'Closes the first gap of the map: 损有余而补不足 and 张弓, 冲气以为和, 济其不及以泄其过 and '
                      '宽猛相济, and 中节 are re-pointed to these laws.',
                'zh': '补上对应表的第一项缺口：损有余而补不足与张弓、冲气以为和、济其不及以泄其过与宽猛相济、中节改指向这些律。'}},
]

record = {
    'schema_version': 2, 'id': RID,
    'title': {'en': 'Two-sided regulation, and regulation that reads late', 'zh': '双向调节，与迟读的调节'},
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': NOW,
    'statement': STATEMENT,
    'laws': [{'en': en, 'zh': zh, 'declarations': resolve(names)} for en, zh, names in LAWS],
    'hypotheses': [
        {'en': 'No axiom. Balance at the condition, the bound, opposition, a rule reading l late, a rest within d a '
               'step, the relay\'s step M and band [a, b], and a start held for l + 1 steps are named premises stated '
               'where they are used.',
         'zh': '不加公理。条件处的平衡、界、相反、迟 l 步读的规则、每步至多 d 的扰动、阈值调节的步长 M 与带 [a, b]、'
               '保持 l + 1 步的起点，都是在用处陈述的具名前提。'}],
    'does_not_show': [
        {'en': 'That a given system regulates a level, which level, how late it reads, or the size of its step.',
         'zh': '某个系统在调节某个水平、是哪个水平、它迟读多少、步长多大。', 'kind': 'scope'},
        {'en': 'One policy keeping a band from every start in it under late reading; several regulated levels lumped '
               'into one; regulation of several conditions at once.',
         'zh': '迟读下对带中每个起点都保带的单一策略；把几个受调节的水平归并为一个；同时调节几个条件。', 'kind': 'scope'},
        {'en': 'That holding a level is good: the laws say what holds it and how wide a band it needs.',
         'zh': '保持一个水平是好的：这些律只说什么保持它、它需要多宽的带。', 'kind': 'non-implication'}],
    'counterexamples': COUNTER,
    'standard_boundaries': BOUNDS,
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {n_decl} declarations of '
              f'Becoming.{MOD}, {n_thm} of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'The statements were checked by simulation before the proofs (simulate.py). Author review in study '
              f'section {N}; not independently reviewed by a person.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.{MOD} 的 {n_decl} 项声明（{n_thm} 项定理）公理报告为空；'
              f'检查器并核对核心纯净。证明之前已以模拟核对各陈述（simulate.py）。作者审查见研究记录；未经人的独立审查。'},
    'next_delta': {
        'en': 'One policy keeping a band from every start under late reading; the lumping of several regulated levels; '
              'amounts in a field, where a factor below one closes gradually; an independent review.',
        'zh': '迟读下对每个起点都保带的单一策略；几个受调节水平的归并；域上的量，其中小于一的因子渐近闭合；独立审查。'},
    'correspondence': {
        'en': 'The map of Chinese sources onto the spine found no law for a level held from both sides, nor for one held '
              'by a rule reading it late (损有余而补不足, 张弓, 冲气以为和, 济其不及以泄其过, 宽猛相济, 中节). These '
              'laws are the formal statements it proposed; reading the passages as them is the AI\'s.',
        'zh': '中国思想与脊柱的对应没有找到两侧保持水平之律，也没有迟读保持之律（损有余而补不足、张弓、冲气以为和、'
              '济其不及以泄其过、宽猛相济、中节）。这些律是它所拟的形式陈述；把这些段落读作这些律是 AI 的读法。'},
    'canonical_source': src(MOD),
    'aliases': [
        'two-sided regulation', 'regulation that reads late', 'late reading', 'late relay', '双向调节', '迟读的调节',
        'Becoming.Flow.withinGap_iff_between', 'Becoming.Flow.settles', 'Becoming.Regulation.no_narrower_band',
        'Becoming.Regulation.lateReturn_band', 'Becoming.Regulation.relay_threshold'],
    'dependencies': DEPS,
    'related': RELATED,
}
evidence = []
for d in DEPS:
    e = d['interface']['evidence']
    if e not in evidence:
        evidence.append(e)
record['references'] = (
    [{'path': src(MOD), 'role': 'proof', 'declarations': sorted(FULL), 'sha256': sha(src(MOD))}]
    + [{'path': p, 'role': 'proof', 'sha256': sha(p)} for p in evidence]
    + [{'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
       {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
       {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
       {'path': SOURCES, 'role': 'provenance', 'sha256': sha(SOURCES)},
       {'path': PASSAGES, 'role': 'integration', 'sha256': sha(PASSAGES)},
       {'path': SIMULATE, 'role': 'review', 'sha256': sha(SIMULATE)}])
record['proof_bindings'] = [{'source': src(MOD), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{MOD}',
                             'success_pointer': '/status', 'success_value': 'passed'}]
record['history'] = [{
    'en': f'19 October 2026: added (RG), the first gap of the map of Chinese sources onto the spine; study section {N}.',
    'zh': f'2026年10月19日：新增（RG），即中国思想与脊柱对应表的第一项缺口；研究第 {N} 节。'}]
path = RECORDS / f'{RID}.json'
assert not path.exists(), 'record exists'
path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print('written', RID, n_thm, n_decl)
