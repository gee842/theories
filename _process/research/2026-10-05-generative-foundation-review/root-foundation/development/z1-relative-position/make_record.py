#!/usr/bin/env python3
"""Write Z1's record: python3 -B make_record.py CORE_RECEIPT SECTION   (from the checkout root, after the study section)

Every declaration cited is resolved against the receipt's audited declarations of Becoming.RelativePosition (a short
name must match exactly one declaration by suffix), and the receipt must bind the module's current bytes."""
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/RelativePosition.lean'
CONTINUATION = f'{PKG}/Becoming/Continuation.lean'
SIGNIFICANCE = f'{PKG}/Becoming/Significance.lean'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
OPENING = 'theories/becoming/OPENING.md'
PROPOSAL = 'drafts/2026-10-10-opening/OPENING-V7-PROPOSAL.md'
RECORDS = ROOT / 'theories/becoming/results/records'
RID = 'relative-position-is-zero-sum'
core_id, section = sys.argv[1], sys.argv[2]
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
assert core['source_sha256']['Becoming.RelativePosition'] == sha(SRC), 'receipt does not bind RelativePosition.lean'
mod = next(m for m in core['modules'] if m['module'] == 'Becoming.RelativePosition')
assert not any(mod['axiom_dependencies'].values())
FULL = sorted(d['name'] for d in mod['declarations'])
N_DECL = len(FULL)
N_THM = sum(1 for d in mod['declarations'] if d.get('kind') == 'theorem')
assert re.search(rf'^## {section}\. The game of relative position \(Z1\)$', (ROOT / STUDY).read_text(), re.M)


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
    law('Zero-sum is counting. A part\'s position is its amount counted once for each part (ahead) against the '
        'family\'s total (behind); over the family the ahead counts total what the behind counts total. Across every '
        'change of amounts the rise counts total what the fall counts total, so a part\'s change of position is the '
        'opposite of the change summed over the rest, and where it rises the rest\'s summed position falls.',
        '零和是计数。一个部分的位置，是它的量按部分数计入（在前）对全族之总（在后）；全族的在前计数之和等于在后计数之和。在量的每一变化中，'
        '升计数之和等于降计数之和，所以一个部分的位置变化恰是其余部分变化之和的相反；它升，则其余部分的位置之和降。',
        'RelativePosition.total_same', 'RelativePosition.total_split', 'RelativePosition.positions_balance',
        'RelativePosition.riseCount', 'RelativePosition.fallCount', 'RelativePosition.change_balances',
        'RelativePosition.change_opposed', 'RelativePosition.rest_falls_of_rises'),
    law('No change raises every part\'s position, and a part\'s rise needs another part\'s fall, found by a decided '
        'comparison, not by contradiction.',
        '没有一个变化使每个部分的位置都升；一个部分升需要另一部分降，后者由可判定的比较找到，而非由反证。',
        'RelativePosition.total_lt_of_mem', 'RelativePosition.not_all_rise',
        'RelativePosition.below_somewhere_or_not', 'RelativePosition.rise_needs_fall'),
    law('A nonempty family has a greatest part, no part\'s amount exceeding its own, and its position is not below '
        'the family\'s.',
        '非空的族有一个最大的部分（没有部分的量超过它），其位置不低于全族。',
        'RelativePosition.Greatest', 'RelativePosition.greatest_exists', 'RelativePosition.greatest_not_behind'),
    law('On a flow, read by what each part of a family has drawn from a condition, between any two steps, the laws '
        'above hold with no hypothesis on the flow; and where every part draws more, a part\'s position can still '
        'fall.',
        '在流上，以族中每个部分从一个条件所取之量来读，任意两步之间，上述规律成立，对流不加任何假设；每个部分都取得更多时，一个部分的位置仍可降。',
        'Flow.drawn', 'Flow.drawn_positions', 'DrawingMore.flow', 'DrawingMore.grow_and_fall'),
    law('The dependence that ends a part at the end of a race, exactly: with balance at the condition across n steps '
        'of joint excess from T, a part that at T + n requires the condition, at a need greater than the level at T '
        'less n, and is active there only while supported, is not active there. Its position does not enter, and no '
        'renewal need be gated.',
        '在竞逐结束时终结一个部分的依赖，确切地说：条件在自 T 起 n 步联合超出中平衡，一个部分若在 T + n 依赖该条件、其需要大于 T 时水平减 n，'
        '且只在被支持时活跃，则它在那时不活跃。它的位置不进入其中，也不需要更新受门控。',
        'Flow.excess_leaves_below', 'Flow.ends_at_race_end'),
    law('With renewal gated (the hypotheses of Flow.joint_excess_ends), the race changes positions by a zero-sum '
        'count while the level falls by at least n, the level stays below m, and every part depending on the '
        'condition at a need of at least m is inactive from then on, the greatest parts included; in a family whose '
        'parts all so depend, at every later step there is a greatest part and every greatest part is inactive. In '
        'Race each part takes within what the step gives and together they take more; the greatest part rises in '
        'position across the race and ends with the condition, as does every part.',
        '在更新受门控时（Flow.joint_excess_ends 的假设），竞逐以零和计数改变位置，而水平至少降 n，此后保持低于 m，'
        '每个以至少 m 之需依赖该条件的部分此后都不活跃，最大的部分也在其中；若族中各部分都如此依赖，则此后每一步都有最大的部分，且每个最大的部分都不活跃。'
        '在 Race 中，每个部分所取都在该步所给之内，合起来却取得更多；最大的部分在竞逐中位置上升，却与条件一同终结，每个部分亦然。',
        'Flow.race_ends_greatest', 'Flow.greatest_end_for_good', 'Race.Member', 'Race.level', 'Race.live',
        'Race.present', 'Race.flow', 'Race.web', 'Race.balances', 'Race.live_of_present', 'Race.acting',
        'Race.dependent', 'Race.gated', 'Race.drawn_renewer', 'Race.drawn_second_le', 'Race.first_greatest',
        'Race.excess', 'Race.all', 'Race.first_rises', 'Race.greatest_ends'),
]
counterexamples = [
    {'path': SRC, 'detail': {
        'en': 'Gated renewal is needed for the end to last: in Restored a renewer that requires nothing gives at the '
              'race\'s end; the race ends the part, greatest at every step, at its end (through Flow.ends_at_race_end), '
              'and the renewal restores it from the next step on (Restored.returns).',
        'zh': '要终结持久，需要更新受门控：在 Restored 中，一个不依赖任何条件的更新者在竞逐结束时给予；竞逐在结束时终结那个每步都最大的部分'
              '（经 Flow.ends_at_race_end），更新使它从下一步起恢复（Restored.returns）。'},
     'declarations': c('Restored.Member', 'Restored.level', 'Restored.takeAt', 'Restored.giveAt', 'Restored.live',
                       'Restored.flow', 'Restored.web', 'Restored.balances', 'Restored.acting', 'Restored.dependent',
                       'Restored.drawn_renewer', 'Restored.returns')},
    {'path': SRC, 'detail': {
        'en': 'Dependence is needed: in the clearer\'s web, read by what each part has drawn from the habitat, the '
              'clearer is the greatest part at every step; the habitat is drawn down jointly beyond what is given to '
              'it with renewal there gated, and the dweller, which depends on it, ends, while the clearer, which does '
              'not, is active and supported at every step (Clearing.greatest_continues). Its loss is one of '
              'significance, and needs one: under the continuation condition it loses the dweller from every '
              'standpoint, under no significance nothing (Clearing.loss_needs_significance).',
        'zh': '需要依赖：在清除者的网中，以每个部分从栖地所取之量来读，清除者每步都是最大的部分；栖地被联合取用超出所给，且那里的更新受门控，'
              '依赖它的栖居者终结，而不依赖它的清除者每步都活跃并受支持（Clearing.greatest_continues）。它的损失是意义上的损失，'
              '且需要一种意义：在延续条件下，从每一立场它都失去栖居者；在无意义之下则无所失（Clearing.loss_needs_significance）。'},
     'declarations': c('Clearing.acting', 'Clearing.habitat_ungiven', 'Clearing.drawn_source',
                       'Clearing.drawn_dweller', 'Clearing.greatest_continues', 'Clearing.loss_needs_significance')},
]
cited = {d for x in laws for d in x['declarations']} | {d for x in counterexamples for d in x['declarations']}
assert cited == set(FULL), ('declarations not cited', sorted(set(FULL) - cited), sorted(cited - set(FULL)))


def dep(rid, relation, en, zh, out_en, out_zh, in_en, in_zh, cond_en, cond_zh, evidence):
    return {'id': rid, 'relation': relation, 'detail': {'en': en, 'zh': zh},
            'interface': {'output': {'en': out_en, 'zh': out_zh}, 'input': {'en': in_en, 'zh': in_zh},
                          'conditions': {'en': cond_en, 'zh': cond_zh}, 'evidence': evidence}}


r = {
    'schema_version': 2, 'id': RID,
    'title': {'en': 'Relative position is zero-sum; a race ends those ahead only through their dependence',
              'zh': '相对位置是零和的；竞逐只经由依赖终结领先者'},
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': NOW,
    'statement': {
        'en': 'A part\'s position against the others is zero-sum by counting: its rise is the rest\'s summed fall, '
              'whatever the amounts do. A race of joint excess ends a part through its dependence on the condition, '
              'not its position; where those ahead do not so depend, they can continue.',
        'zh': '一个部分相对其余部分的位置按计数是零和的：它升即其余部分之和降，不论各量如何变化。联合超出的竞逐经由一个部分对条件的依赖、'
              '而非其位置终结它；领先者若不如此依赖，则可延续。'},
    'laws': laws,
    'hypotheses': [{
        'en': 'No axiom. The counting laws use no premise and hold for every reading of amounts. The end at the race\'s '
              'end needs balance at the condition across the race, joint excess at each step, a start below n plus '
              'the part\'s need, and the part requiring the condition and being active only while supported. The end '
              'for good adds Flow.joint_excess_ends\' hypotheses: balance, only active formations giving, activity '
              'needing support and renewal gated at m. The continuation condition enters only as a hypothesis of '
              'Clearing.loss_needs_significance.',
        'zh': '无公理。计数规律不用任何前提，对每一种量的读法成立。竞逐结束时的终结，需要条件在竞逐中平衡、每步联合超出、起点低于 n 加该部分之需，'
              '以及该部分依赖该条件且只在被支持时活跃。持久的终结另加 Flow.joint_excess_ends 的假设：平衡、只有活跃者给予、活跃需要支持，'
              '以及更新在 m 处受门控。延续条件只作为 Clearing.loss_needs_significance 的假设出现。'}],
    'does_not_show': [
        {'en': 'That a race for relative position produces joint excess: that is a premise of the join, not derived from '
               'the counting law or from any race dynamic.',
         'zh': '相对位置的竞逐会产生联合超出：这是连接的前提，并非由计数规律或任何竞逐动力推出。', 'kind': 'non-implication'},
        {'en': 'That any actual part depends on what its race draws down: for the present race this is the empirical '
               'premise the opening calls the entangled Earth.',
         'zh': '任何实际的部分依赖其竞逐所耗取的：对当前的竞逐，这是开篇称为纠缠的地球的经验前提。', 'kind': 'correspondence'},
        {'en': 'Positions read as ranks or shares, several shared conditions with different needs, or the dynamics by '
               'which parts race.',
         'zh': '以名次或份额读的位置、需要不同的多个共享条件，或各部分竞逐的动力。', 'kind': 'scope'}],
    'counterexamples': counterexamples,
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {N_DECL} declarations of '
              f'Becoming.RelativePosition, {N_THM} of them theorems, have empty axiom reports; the checker verifies core '
              f'purity. Author self-review in study section {section}; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.RelativePosition 的 {N_DECL} 项声明（{N_THM} 项定理）'
              f'公理报告为空；检查器并核对核心纯净。作者自审见研究第 {section} 节；未经独立审查。'},
    'next_delta': {
        'en': 'Positions read as ranks or shares; a race dynamic in which parts behind raise their take, and whether it '
              'produces joint excess; several shared conditions with different needs; an independent review.',
        'zh': '以名次或份额读的位置；落后者增加取用的竞逐动力，及其是否产生联合超出；需要不同的多个共享条件；独立审查。'},
    'correspondence': {
        'en': 'States the counting half of the opening\'s sentence "a zero-sum game of relative position, which all its '
              'winners will lose" (OPENING, Ren\'s voice; provenance, not warrant), which its note [^aligned] called "a '
              'matter of counting, not yet stated on the formal spine", and proves the second half under a stated '
              'dependence (board item Z1; v7 proposal, edits (j) and (ee)). "Winner" is read as a greatest part by '
              'the reading of positions, the AI\'s reading; the sentence the note can carry is in study section '
              f'{section}.',
        'zh': '陈述开篇一句“a zero-sum game of relative position, which all its winners will lose”（OPENING，Ren 的口吻；'
              '是出处，不是依据）的计数一半，其注 [^aligned] 称之为“a matter of counting, not yet stated on the formal spine”；'
              '并在写明的依赖下证明后一半（工作板 Z1；v7 提案编辑 (j) 与 (ee)）。“winner”读作按位置读法最大的部分，此为 AI 的读法；'
              f'注中可承载的句子见研究第 {section} 节。'},
    'canonical_source': SRC,
    'aliases': ['the game of relative position', '相对位置的博弈', 'zero-sum game of relative position',
                'relative position is zero-sum', '相对位置是零和的', 'position does not protect',
                'Becoming.RelativePosition.change_balances', 'Becoming.RelativePosition.not_all_rise',
                'Becoming.Flow.race_ends_greatest', 'Becoming.Flow.ends_at_race_end'],
    'dependencies': [
        dep('own-count-misses-joint-excess', 'formal-reuse',
            'Reuses Flow.joint_excess_ends, Flow.excess_bounded_at, Flow.stays_below and Flow.ends_below_at; the delta '
            'is the positions read alongside, the end at the race\'s end without gating, and the greatest parts.',
            '复用 Flow.joint_excess_ends、Flow.excess_bounded_at、Flow.stays_below 与 Flow.ends_below_at；增量是并读的位置、'
            '不需门控的竞逐结束时终结，以及最大的部分。',
            'Joint excess with balance lowers the level by at least one per step; with renewal gated, a level below m '
            'stays below m and every formation depending at a need of at least m is inactive.',
            '在平衡下，联合超出每步至少使水平降一；更新受门控时，低于 m 的水平保持低于 m，每个以至少 m 之需依赖者都不活跃。',
            'The race\'s steps of joint excess at the shared condition and the parts\' dependence on it.',
            '共享条件上竞逐的联合超出各步，以及各部分对它的依赖。',
            'Balance at the condition; for the lasting end, Acting, Dependent and gated renewal.',
            '条件处平衡；持久终结另需 Acting、Dependent 与受门控的更新。', CONTINUATION),
        dep('derived-extent-limits', 'formal-reuse',
            'Reuses the clearer\'s web (Clearing.flow, Clearing.web, Clearing.balances, Clearing.dependent).',
            '复用清除者的网（Clearing.flow、Clearing.web、Clearing.balances、Clearing.dependent）。',
            'A balanced web in which the clearer draws down the dweller\'s habitat and continues.',
            '一个平衡的网，其中清除者耗取栖居者的栖地而延续。',
            'The counterexample read by what each part has drawn from the habitat.',
            '以每个部分从栖地所取之量来读的反例。',
            'None beyond the witness.', '除见证外无。', CONTINUATION),
        dep('whole-first-and-bounded-centers', 'formal-reuse',
            'Reuses Clearing.free_rider_loses.', '复用 Clearing.free_rider_loses。',
            'Under the continuation condition the clearer\'s part loses the dweller from every standpoint.',
            '在延续条件下，清除者的那一份从每一立场都失去栖居者。',
            'The loss of the greatest part that does not depend on what it draws down.',
            '不依赖其所耗取者的最大部分的损失。',
            'The continuation condition, as a hypothesis.', '延续条件，作为假设。', SIGNIFICANCE)],
    'related': [{'id': 'raising-what-couples-in-draws-from-beyond', 'detail': {
        'en': 'Where the whole gains nothing (a premise), a rise of an observed family\'s stock is paid from beyond it; '
              'rise_needs_fall is the counterpart for position, with no premise, since position is relative by '
              'definition.',
        'zh': '整体无所增益时（一个前提），被观察的族的存量上升由其外支付；rise_needs_fall 是位置上的对应，不需前提，因为位置按定义是相对的。'}}],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': FULL, 'sha256': sha(SRC)},
        {'path': CONTINUATION, 'role': 'proof', 'declarations': ['Becoming.Flow.joint_excess_ends'],
         'sha256': sha(CONTINUATION)},
        {'path': SIGNIFICANCE, 'role': 'proof', 'declarations': ['Becoming.Clearing.free_rider_loses'],
         'sha256': sha(SIGNIFICANCE)},
        {'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
        {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
        {'path': OPENING, 'role': 'provenance', 'sha256': sha(OPENING)},
        {'path': PROPOSAL, 'role': 'statement', 'sha256': sha(PROPOSAL)}],
    'proof_bindings': [{'source': SRC, 'receipt': RECEIPT, 'sha256_pointer': '/source_sha256/Becoming.RelativePosition',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': f'19 October 2026: added (Z1), to state on the spine what the opening\'s note [^aligned] called "a matter '
              f'of counting, not yet stated on the formal spine", and to prove where "all its winners will lose" holds; '
              f'study section {section}.',
        'zh': f'2026年10月19日：新增（Z1），把开篇注 [^aligned] 称为“a matter of counting, not yet stated on the formal spine”'
              f'者陈述于脊柱，并证明“all its winners will lose”在何处成立；研究第 {section} 节。'}],
}
assert len(r['statement']['en']) <= 300, len(r['statement']['en'])
path = RECORDS / f'{RID}.json'
assert not path.exists(), ('record exists', RID)
path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
print('written', RID, N_DECL, N_THM)
