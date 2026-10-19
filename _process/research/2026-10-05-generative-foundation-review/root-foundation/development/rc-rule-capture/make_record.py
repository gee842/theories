#!/usr/bin/env python3
"""Write RC's record: python3 -B make_record.py CORE_RECEIPT SECTION DECISION   (from the checkout root, after
apply_text.py)

Every declaration of Becoming.RuleCapture is cited, each resolved against the receipt's audited declarations (a short
name must match exactly one declaration by suffix), and the receipt must bind the module's current bytes."""
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/RuleCapture.lean'
PACE = f'{PKG}/Becoming/Pace.lean'
CAPTURE = f'{PKG}/Becoming/Capture.lean'
IDEALS = f'{PKG}/Becoming/Ideals.lean'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
STUDY = f'{RF}/BECOMING-RENEWAL-READING.md'
DC = f'{RF}/DELEGATED-CHOICES.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
RO_CHAPTER = 'theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md'
PASSAGES = f'{RF}/development/ro-relational-sources/passages.json'
RECORDS = ROOT / 'theories/becoming/results/records'
RID = 'capture-through-the-rule'
core_id, section, decision = sys.argv[1], sys.argv[2], sys.argv[3]
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
assert core['source_sha256']['Becoming.RuleCapture'] == sha(SRC), 'receipt does not bind RuleCapture.lean'
assert core['source_sha256']['Becoming.Pace'] == sha(PACE), 'receipt does not bind Pace.lean'
assert core['source_sha256']['Becoming.Capture'] == sha(CAPTURE), 'receipt does not bind Capture.lean'
mod = next(m for m in core['modules'] if m['module'] == 'Becoming.RuleCapture')
assert not any(mod['axiom_dependencies'].values())
FULL = sorted(d['name'] for d in mod['declarations'])
N_DECL = len(FULL)
N_THM = sum(1 for d in mod['declarations'] if d.get('kind') == 'theorem')
assert (N_DECL, N_THM) == (74, 53), (N_DECL, N_THM)
assert re.search(rf'^## {section}\. Capture through the rule \(RC\)$', (ROOT / STUDY).read_text(), re.M)
assert f'| D{decision} | the readings of capture through the rule' in (ROOT / DC).read_text()


def c(*names):
    out = []
    for n in names:
        hits = [f for f in FULL if f == 'Becoming.' + n or f.endswith('.' + n)]
        assert len(hits) == 1, (n, hits)
        out.append(hits[0])
    return out


def law(en, zh, *names):
    return {'en': en, 'zh': zh, 'declarations': c(*names)}


laws = [
    law('The loop, stated for every pair of orders: on Pace\'s two-level course, the fast step a selection that does '
        'not lower the share under a favouring rule (Raises), the rule read at a reading step a monotone function of '
        'the share alone (ReadsShare); a course read from a later step is the course from its configuration there, and '
        'the fast configuration after a step is the selection by the rule in force.',
        '回路，对每一对序陈述：在 Pace 的两速历程上，快步是在偏向的规则下不降低份额的选择（Raises），读取步所读出的规则只是份额的单调函数'
        '（ReadsShare）；从较后一步读起的历程即从它在那里的构形出发的历程，一步之后的快构形是在行规则下的选择。',
        'Pace.paced_shift', 'Pace.paced_fast_succ', 'RuleCapture.reverse', 'RuleCapture.Raises', 'RuleCapture.ReadsShare',
        'RuleCapture.ReadsShare.reverse'),
    law('Where no rule turns against the reading, the loop locks at its first reading step: where the start\'s rule and '
        'every rule read favour, the share falls at no step from the start and the course is locked from the step after '
        'its first reading step. On counts with a margin m (each carrier leaving a + m offspring, each other a), the '
        'share falls at no step and, from the step after the first reading step, the margin falls at no step; the share '
        'rises strictly at every step whose margin is positive, carriers present, along every course.',
        '没有规则反对读法之处，回路在第一个读取步锁定：起点的规则与每个读出的规则都偏向时，从起点起份额在任何一步都不降，进程自第一个读取步之后的那一步起锁定。'
        '在带余裕 m 的计数上（每个承载者留 a + m 个后代，其他每个留 a 个），份额在任何一步都不降，自第一个读取步之后的那一步起余裕在任何一步都不降；'
        '在每条进程上，余裕为正且有承载者的每一步，份额严格上升。',
        'RuleCapture.favours_throughout', 'RuleCapture.favouring_locks', 'Counts.margin', 'Counts.margin_favours',
        'Counts.margin_le', 'Counts.byMargin', 'Counts.byMargin_reads', 'Counts.margin_course', 'Counts.rises_strictly',
        'Counts.rises_strictly_along'),
    law('Locked, the loop does not turn back: favouring kept by every rule not lower, a configuration whose rule favours '
        'and is not above what the reading of its share gives stays locked at every later step, and neither the share '
        'nor the rule falls across any step, reading steps included, nor is ever again below where it was.',
        '锁定之后回路不回转：偏向为每个不更低的规则所保持时，一个规则偏向、且不高于其份额所读出者的构形，此后每一步都保持锁定，'
        '份额与规则跨任何一步都不降（读取步也在内），也不再低于它们曾在之处。',
        'RuleCapture.Locked', 'RuleCapture.turn_locked', 'RuleCapture.locked_stays', 'RuleCapture.locked_rises',
        'RuleCapture.locked_not_below'),
    law('A perturbation of the rule that keeps its direction is absorbed: from a locked configuration, with the rule '
        'replaced by any favouring one, above or below, at the step after every reading step the rule is at least the '
        'rule before the perturbation and the course is locked again.',
        '保持方向的规则扰动被吸收：从一个锁定的构形起，把规则换成任何偏向的规则（更高或更低），在每个读取步之后的那一步，规则至少是扰动前的规则，进程重新锁定。',
        'RuleCapture.perturbation_invariant', 'RuleCapture.perturbation_absorbed'),
    law('Leaving: where the reading favours at every share, every course, whatever its start, is locked from the step '
        'after its second reading step, so only a change of the law, of how the rule reads or of the selection, leaves.',
        '离开：读法在每个份额都偏向时，每条进程，不论从何开始，自第二个读取步之后的那一步起锁定；所以只有改变律、规则怎样读或选择，才离开。',
        'RuleCapture.favours_after_reading', 'RuleCapture.uniform_locks'),
    law('Order kept: where selection is monotone in the share and the rule and the reading monotone in the share, two '
        'courses keep their order at every step, and a perturbation lowering the rule keeps its course below the course '
        'without it; on counts under every monotone reading.',
        '次序保持：选择对份额与规则单调、读法对份额单调时，两条进程每一步都保持其次序；降低规则的扰动使其进程保持在没有扰动的进程之下；在计数上对每个单调读法成立。',
        'RuleCapture.order_kept', 'RuleCapture.perturbation_keeps_below', 'Counts.select_mono',
        'Counts.perturbation_keeps_below_counts'),
    law('Counts: two counts, the second positive, ordered by cross-multiplication, the comparison of share_not_lower. '
        'Selection multiplies each kind by what the rule gives it; it does not lower the share under a favouring rule nor '
        'raise it under a disfavouring one, and favouring and disfavouring are kept upward and downward. Under the '
        'proportional reading, from a rule that favours and is not above the population\'s own proportion, the share and '
        'the rule fall at no step; from one that disfavours and is not below it, they rise at none. A threshold reading '
        'is monotone where its lower rule is not above its upper one, and favours at every share where both favour.',
        '计数：两个计数，第二个为正，以交叉相乘排序，即 share_not_lower 的比较。选择以规则给各类之数乘各类；在偏向的规则下不降低份额，在不偏向的规则下不提高份额，'
        '偏向与不偏向分别向上、向下保持。在比例读法下，从一个偏向、且不高于人口自身比例的规则起，份额与规则在任何一步都不降；从一个不偏向、且不低于它的规则起，'
        '二者在任何一步都不升。阈值读法在其下规则不高于上规则时单调，二者都偏向时在每个份额都偏向。',
        'RuleCapture.Counts', 'Counts.mul_right_comm_nat', 'Counts.mul_mul_mul_comm_nat', 'Counts.order',
        'Counts.favours', 'Counts.disfavours', 'Counts.select', 'Counts.raises', 'Counts.lowers', 'Counts.upper',
        'Counts.lower', 'Counts.share_not_lower_counts', 'Counts.proportional', 'Counts.proportional_reads',
        'Counts.proportional_locks', 'Counts.proportional_locks_down', 'Counts.threshold', 'Counts.threshold_above',
        'Counts.threshold_below', 'Counts.threshold_reads', 'Counts.threshold_favours', 'Counts.always_step'),
]
counterexamples = [
    {'path': SRC, 'detail': {
        'en': 'Without the start condition the lock fails: under the threshold reading hi/lo read at every step, from '
              'carriers two to one under lo (a rule in force against the reading, read one step late), the share falls '
              'at every even step and the rule at every odd step, without end, and the course is locked neither way at '
              'any step (Alternating.alternates, Alternating.never_locked); its start is the locked configuration '
              'with its rule reversed (Alternating.before_locked).',
        'zh': '没有起点条件，锁定不成立：阈值读法 hi/lo 每步都读，从 lo 下二比一的承载者起（一个反对读法、晚一步被读的在行规则），份额在每个偶数步下降、'
              '规则在每个奇数步下降，无尽，进程在任何一步两个方向都不锁定（Alternating.alternates、Alternating.never_locked）；其起点是锁定的构形把规则反转'
              '（Alternating.before_locked）。'},
     'declarations': c('Counts.hi', 'Counts.lo', 'Counts.twoToOne', 'Counts.lo_le_hi', 'Counts.hi_not_le_lo',
                       'Alternating.course', 'Alternating.course_step', 'Alternating.before_locked',
                       'Alternating.lt_four', 'Alternating.from_even', 'Alternating.even', 'Alternating.odd',
                       'Alternating.alternates', 'Alternating.never_locked')},
    {'path': SRC, 'detail': {
        'en': 'A perturbation that reverses the direction is not absorbed: from the same locked configuration, the rule '
              'reversed and held for one step before the reading, the share crosses the threshold, the course is locked '
              'the other way, neither share nor rule rises again, and the rule after the first reading step is below '
              'the rule before the perturbation (Reversed.not_absorbed).',
        'zh': '反转方向的扰动不被吸收：从同一锁定构形起，规则被反转并在读取前保持一步，份额越过阈值，进程锁向另一方向，份额与规则不再上升，'
              '第一个读取步之后的规则低于扰动前的规则（Reversed.not_absorbed）。'},
     'declarations': c('Reversed.late', 'Reversed.course', 'Reversed.locked_down', 'Reversed.not_absorbed')},
    {'path': SRC, 'detail': {
        'en': 'The bound of uniform_locks is exact: under the threshold reading hi/twoToOne, which favours at every '
              'share, read at every step from one to one under lo, the course is not locked at the step after its first '
              'reading step and its rule falls across the second (Second.second_exact).',
        'zh': 'uniform_locks 的界是确切的：在每个份额都偏向的阈值读法 hi/twoToOne 下，每步都读，从 lo 下一比一起，进程在第一个读取步之后的那一步不锁定，'
              '其规则跨第二个读取步下降（Second.second_exact）。'},
     'declarations': c('Second.oneToOne', 'Second.course', 'Second.second_exact', 'Counts.hi_not_le_twoToOne',
                       'Counts.twoToOne_le_hi')},
]
cited = {d for x in laws for d in x['declarations']} | {d for x in counterexamples for d in x['declarations']}
assert cited == set(FULL), ('declarations not cited', sorted(set(FULL) - cited), sorted(cited - set(FULL)))


def dep(rid, relation, en, zh, out_en, out_zh, in_en, in_zh, cond_en, cond_zh, evidence):
    return {'id': rid, 'relation': relation, 'detail': {'en': en, 'zh': zh},
            'interface': {'output': {'en': out_en, 'zh': out_zh}, 'input': {'en': in_en, 'zh': in_zh},
                          'conditions': {'en': cond_en, 'zh': cond_zh}, 'evidence': evidence}}


r = {
    'schema_version': 2, 'id': RID,
    'title': {'en': 'Capture through the rule: a selection whose rule reads the share it selects',
              'zh': '经由规则的捕获：规则读其所选出之份额的选择'},
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': NOW,
    'statement': {
        'en': 'Where a selection\'s rule is read monotonically from the share it selects, the loop locks: share and rule '
              'stop falling, a change of the rule\'s value that keeps its direction is absorbed at the next reading, '
              'and only a change of how the rule reads leaves. Without the start condition, it fails.',
        'zh': '选择的规则从它所选出的份额单调地读出时，回路锁定：份额与规则不再下降，保持方向的规则之值的改变在下一次读取被吸收，只有改变规则怎样读才离开。没有起点条件则不成立。'},
    'laws': laws,
    'hypotheses': [{
        'en': 'No axiom. Each statement names its hypotheses: the fast step does not lower the share under a favouring '
              'rule (Raises); the rule read is a monotone function of the share alone (ReadsShare); favouring is kept '
              'upward; and, as the statement needs, the start locked (Locked), the start\'s rule and every rule read '
              'favouring, or the reading favouring at every share. The order statements add selection monotone in the '
              'share and the rule. On counts, offspring numbers per carrier and per other, others present.',
        'zh': '无公理。每条陈述列出其假设：快步在偏向的规则下不降低份额（Raises）；读出的规则只是份额的单调函数（ReadsShare）；偏向向上保持；'
              '以及按陈述所需，起点锁定（Locked）、起点规则与每个读出的规则都偏向，或读法在每个份额都偏向。次序陈述另加选择对份额与规则单调。'
              '在计数上，每个承载者与其他每个的后代数，其他者在场。'}],
    'does_not_show': [
        {'en': 'That any actual rule reads the share it selects, or reads it monotonically: this is the premise '
               'ReadsShare, where "the winner shapes the rule" of Becoming.Capture enters.',
         'zh': '任何实际的规则读其所选出的份额，或单调地读：这是前提 ReadsShare，即 Becoming.Capture 的“胜者塑造规则”进入之处。',
         'kind': 'correspondence'},
        {'en': 'That offspring carry their parents\' target (a premise as in Becoming.Capture), or that share or rule '
               'rises strictly, except on counts under a positive margin.',
         'zh': '后代携带其亲代的目标（与 Becoming.Capture 同为前提），或份额、规则严格上升（计数上余裕为正时除外）。',
         'kind': 'non-implication'},
        {'en': 'Real-valued shares and rates, rules that read more than the share, many levels, or noisy readings.',
         'zh': '实数份额与比率、读份额以外之物的规则、多层，或有噪声的读法。', 'kind': 'scope'}],
    'counterexamples': counterexamples,
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {N_DECL} declarations of '
              f'Becoming.RuleCapture, {N_THM} of them theorems, have empty axiom reports; the checker verifies core '
              f'purity. Author self-review in study section {section}; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.RuleCapture 的 {N_DECL} 项声明（{N_THM} 项定理）'
              f'公理报告为空；检查器并核对核心纯净。作者自审见研究第 {section} 节；未经独立审查。'},
    'next_delta': {
        'en': 'Real-valued shares and rates; rules that read the share and the rule in force, or a history of shares; '
              'many levels; noisy or later readings; a join with two-sided regulation of a level (board item RG) once it '
              'lands; an independent review.',
        'zh': '实数份额与比率；读份额与在行规则、或读份额之史的规则；多层；有噪声或更迟的读法；与水平的双向调节（工作板 RG）落地后的连接；独立审查。'},
    'correspondence': {
        'en': 'Closes the third gap of the map of the Chinese sources onto the spine (record chinese-sources-on-the-spine, '
              'chapter CHINESE-SOURCES-AND-BECOMING §8; passages 二柄, 据有余而制不足, 壹赏、壹刑、壹教). RO\'s proposed '
              'statement takes the margin as a natural number; there its claims hold, stronger than stated (at every step, '
              'not only at reading steps). Where rules can favour the others, the lock needs a start condition, absorption '
              'holds exactly for perturbations keeping the direction, and leaving needs a change of how the rule reads '
              f'where the reading favours at every share. The readings of the three passages are the AI\'s, D{decision}.',
        'zh': '闭合中国思想诸传统对脊柱之映射的第三项缺口（记录 chinese-sources-on-the-spine，《中国思想的关系本体与生成之论》§8；二柄、据有余而制不足、'
              '壹赏壹刑壹教诸段）。RO 所拟陈述以自然数为余裕；在其中它的诸论断成立，且强于所述（在每一步，而不只在读取步）。规则可以偏向他者时，锁定需要起点条件，'
              f'吸收恰对保持方向的扰动成立，读法在每个份额都偏向时离开需要改变规则怎样读。三段的读法是 AI 的，D{decision}。'},
    'canonical_source': SRC,
    'aliases': ['capture through the rule', '经由规则的捕获', 'rule capture', 'the winner shapes the rule',
                '胜者塑造规则', '二柄', '君反制于臣', '据有余而制不足', '壹赏壹刑壹教',
                'Becoming.RuleCapture.locked_stays', 'Becoming.RuleCapture.perturbation_absorbed',
                'Becoming.RuleCapture.uniform_locks', 'Becoming.RuleCapture.favouring_locks',
                'Becoming.RuleCapture.Counts.margin_course'],
    'dependencies': [
        dep('how-fast-a-rule-may-change', 'formal-reuse',
            'Builds on Pace\'s two-level course (Pace.paced, Pace.turn, Pace.paced_succ); adds that a course read from a '
            'later step is the course from its configuration there and that the fast configuration after a step is the '
            'selection by the rule in force. The delta is a rule read from a share, with a selection as the fast step.',
            '建立在 Pace 的两速历程之上（Pace.paced、Pace.turn、Pace.paced_succ）；增加从较后一步读起的历程即从它在那里的构形出发的历程，'
            '以及一步之后的快构形是在行规则下的选择。增量是从份额读出的规则，以选择为快步。',
            'A two-level course whose rule changes only at reading steps, as a run of one law.',
            '规则只在读取步改变的两速历程，作为一条律的运行。',
            'The course on which the lock, absorption and leaving are stated.', '陈述锁定、吸收与离开所在的历程。',
            'None beyond the course\'s law.', '除历程之律外无。', PACE),
        dep('target-capture', 'formal-reuse',
            'Reuses share_not_lower\'s comparison as the share order of counts (Counts.share_not_lower_counts) and '
            'mul_assoc_nat; the delta is the rule that Capture supposes holds the outcome, here read from the share and '
            'shown to hold it.',
            '复用 share_not_lower 的比较作为计数的份额序（Counts.share_not_lower_counts）与 mul_assoc_nat；增量是 Capture 所设持住结果的规则，'
            '这里从份额读出，并证明它持住结果。',
            'Where each carrier leaves at least as many offspring as each other parent, the share among offspring is not '
            'lower, by cross-multiplication.', '每个承载者留下的后代不少于其他每个亲代时，后代中的份额以交叉相乘计不更低。',
            'The order of shares on counts.', '计数上份额的次序。',
            'Others present before and after.', '前后都有其他者在场。', CAPTURE)],
    'related': [
        {'id': 'chinese-sources-on-the-spine', 'detail': {
            'en': 'The map that found the gap this record closes; its passages 二柄, 据有余而制不足 and 壹 now cite these laws.',
            'zh': '发现本记录所闭合之缺口的映射；其二柄、据有余而制不足与壹诸段现引这些定律。'}},
        {'id': 'a-history-read-off-its-finite-stretches', 'detail': {
            'en': 'Ideals.Preorder, the order this record\'s laws are stated for, is defined there.',
            'zh': '本记录诸律所对之序 Ideals.Preorder 在那里定义。'}}],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': FULL, 'sha256': sha(SRC)},
        {'path': PACE, 'role': 'proof', 'declarations': ['Becoming.Pace.paced', 'Becoming.Pace.turn',
                                                         'Becoming.Pace.paced_succ'], 'sha256': sha(PACE)},
        {'path': CAPTURE, 'role': 'proof', 'declarations': ['Becoming.share_not_lower', 'Becoming.mul_assoc_nat'],
         'sha256': sha(CAPTURE)},
        {'path': IDEALS, 'role': 'proof', 'declarations': ['Becoming.Ideals.Preorder'], 'sha256': sha(IDEALS)},
        {'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
        {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
        {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
        {'path': DC, 'role': 'integration', 'sha256': sha(DC)},
        {'path': RO_CHAPTER, 'role': 'integration', 'sha256': sha(RO_CHAPTER)},
        {'path': PASSAGES, 'role': 'integration', 'sha256': sha(PASSAGES)}],
    'proof_bindings': [{'source': SRC, 'receipt': RECEIPT, 'sha256_pointer': '/source_sha256/Becoming.RuleCapture',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': f'19 October 2026: added (RC), the third gap the map of the Chinese sources found, its proposed statement '
              f'checked, sharpened where rules can favour the others, and refuted there without the start condition; '
              f'study section {section}; readings D{decision}.',
        'zh': f'2026年10月19日：新增（RC），中国思想映射所见的第三项缺口；其所拟陈述经查验，在规则可偏向他者处收紧，在那里没有起点条件则被驳倒；'
              f'研究第 {section} 节；读法 D{decision}。'}],
}
assert len(r['statement']['en']) <= 300, len(r['statement']['en'])
path = RECORDS / f'{RID}.json'
assert not path.exists(), ('record exists', RID)
path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
print('written', RID, N_DECL, N_THM)
