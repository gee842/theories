#!/usr/bin/env python3
"""Write RB1's record and update the record it continues (raising-what-couples-in-draws-from-beyond):
python3 -B make_record.py CORE_RECEIPT STUDY_SECTION   (from the checkout root, after apply_text.py)

Every declaration cited is resolved against the receipt's audited declarations of Becoming.DrawnBeyond (a short
name must match exactly one declaration by suffix), and the receipt must bind the module's current bytes."""
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
RECORDS = ROOT / 'theories/becoming/results/records'
MOD = 'DrawnBeyond'
core_id, N = sys.argv[1], int(sys.argv[2])
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
HEAD = f'## {N}. What a rise draws from beyond: dependences broken above the slack, and the share that reaches (RB1)'
assert re.search('^' + re.escape(HEAD) + '$', (ROOT / STUDY).read_text(), re.M)


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


m = decls(MOD)
assert not any(m['axiom_dependencies'].values())
n_decl, n_thm = len(m['declarations']), sum(1 for d in m['declarations'] if d.get('kind') == 'theorem')

BOUNDS = ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical', 'names-provisional',
          'omission-not-refutation']


def dep(rid, relation, en, zh, out_en, out_zh, in_en, in_zh, cond_en, cond_zh, evidence):
    return {'id': rid, 'relation': relation, 'detail': {'en': en, 'zh': zh},
            'interface': {'output': {'en': out_en, 'zh': out_zh}, 'input': {'en': in_en, 'zh': in_zh},
                          'conditions': {'en': cond_en, 'zh': cond_zh}, 'evidence': evidence}}


RID = 'what-a-rise-draws-from-beyond'
FL = 'Flow.'
B = 'Flow.Balances.'
D = 'DrawnBeyond.'
laws = [
    ('In a balanced flow, where the family with the conditions beyond it gains nothing across a step, the two stocks '
     'after the step with what the whole loses are the two before: the beyond falls by at least the rise, and under '
     'dissipation by at least one unit more for each formation taking from the whole.',
     '在平衡的流中，家族连同其外的条件跨一步无所增益时，步后两者的存量加上整体所失，等于步前两者：其外至少降低上升之量，耗散时每个从整体汲取的构成再多一个单位。',
     [B + 'beyond_falls_exactly', B + 'rise_lowers_beyond', B + 'rise_lowers_beyond_dissipating']),
    ('Name on each condition beyond a formation depending on it at a need met at the step; the slack is what the '
     'conditions stand above those needs. Where the rise with the loss exceeds the slack, one of those dependences is '
     'broken across the step, found by deciding each; conditions in the whole nothing depends on count in full.',
     '在其外每个条件上指名一个以该步所满足之需求依存于它的构成；余量是这些条件高出需求之量。上升连同损失超出余量时，其中一个依存跨该步被打断，逐一判定即可找到；整体中无所依存的条件全数计入。',
     ['Web.slack', 'Web.MetOn', 'Web.MetOn.stock_eq', 'Web.MetOn.breaks_of_falls', B + 'breaks_beyond',
      B + 'rise_breaks_beyond', B + 'breaks_beyond_past_free']),
    ('Where activity needs support, the formation whose dependence breaks is not, after the step, active with that '
     'dependence at a need as strong: it ends, or its dependence weakens or dissolves; with the dependence as it was, '
     'it ends.',
     '活动需要支持时，依存被打断的构成在步后不会以同样强的需求带着该依存而活跃：它终止，或其依存减弱或消解；依存照旧时，它终止。',
     [B + 'breaks_beyond_unsettles', B + 'breaks_beyond_ends']),
    ('Where every condition a group couples into is in the family and the beyond lies outside it, every selection '
     'holding only where the family rises above the slack beyond holds only where a formation outside the group has '
     'its dependence broken, on a condition no member couples into.',
     '群体耦合入的每个条件都在家族中、其外在家族之外时，每个只在家族升过其外余量处成立的选择，只在群体之外某构成的依存被打断处成立，且所依存的条件无一成员耦合入。',
     [FL + 'favours_breaking_beyond']),
    ('Where the whole gains nothing, a formation giving the family more than it takes from it takes from the beyond. '
     'Over generations whose members take part in the flow, read by whether each reaches beyond, where more offspring '
     'go only to raisers no pair is discordant: the share reaching beyond is never selected against.',
     '整体无所增益时，给予家族多于取自它的构成从其外汲取。在成员参与流、以是否伸向之外读出的世代中，后代更多者只是升高者时没有不一致的对：伸向之外者的份额从不被逆向选择。',
     [FL + 'RaisesOn', FL + 'reach', FL + 'reach_of_pos', FL + 'RaisesOn.reaches', FL + 'share_not_against']),
    ('Where also each offspring of a reaching member reaches, the share does not fall over any stretch; with exact '
     'transmission, where it moved it rose, and at some step more offspring went with reaching beyond.',
     '若伸向之外的成员的每个后代也伸向之外，份额在任何一段上都不降；传递精确时，份额移动了就是上升了，且在某一步后代更多者伸向之外。',
     [FL + 'lowered_none', FL + 'share_not_lower', FL + 'share_moved_rises']),
    ('Over a stretch at every step of which the whole gains nothing, the family rose by at most what the beyond lost; '
     'a rise above all the whole held at the start needs a step at which it gains.',
     '在整体每一步都无所增益的一段上，家族至多升高其外所失之量；高于整体起初所有的上升，需要有一步整体有所增益。',
     [B + 'stock_not_rises_over', B + 'rise_bounded_by_beyond', B + 'open_of_rise_above']),
    ('Witnesses: in Diversion the store\'s rise breaks the dweller\'s dependence and the dweller ends, a selection '
     'through the taker that does not see it; a slack equal to the rise breaks nothing; the share rises from a half to '
     'the whole in Spreading, whose closed store never exceeds two, and falls in Lapsing, where reaching is not carried '
     'on.',
     '见证：在 Diversion 中，库存的上升打断了居者的依存，居者终止，经取者的选择看不见这一点；余量等于上升时什么也不打断；在 Spreading 中份额从二分之一升到全部，其封闭的库存从不超过二；在 Lapsing 中伸向之外不被延续，份额下降。',
     [D + 'Dweller.rise_ends_dweller', D + 'Dweller.selected_breaks', D + 'WithinSlack.within_slack',
      D + 'Spreading.share_rises', D + 'Spreading.store_bounded', D + 'Lapsing.share_falls']),
]
for en, zh, _ in laws:
    assert len(en) <= 420 and len(zh) <= 190, (en[:40], len(en), len(zh))

REACH_DEP = dep('raising-what-couples-in-draws-from-beyond', 'formal-reuse',
                'Reuses Becoming.SelectionReach\'s selection through coupling of a rise (Web.raises_selectsThrough), the '
                'search over a decidable property and Diversion\'s world and its taker\'s coupling (taker_listed).',
                '复用 Becoming.SelectionReach 中上升作为经耦合的选择（Web.raises_selectsThrough）、可判定性质上的搜索，以及 Diversion 的世界及其取者的耦合（taker_listed）。',
                'A rise of what couples in drawn from beyond; the rise a selection through coupling.',
                '耦合入者的上升取自其外；该上升是经耦合的选择。',
                'Whose dependence the draw breaks, how much is drawn, the share that reaches beyond.',
                '汲取打断了谁的依存、汲取多少、伸向之外者的份额。',
                'Balance and the whole gaining nothing.', '平衡与整体无所增益。', src('SelectionReach'))
ENTROPY_DEP = dep('entropy-history-and-record', 'formal-reuse',
                  'Reuses Becoming.Entropy\'s gaining nothing (Flow.GainlessOn), the stock falling by what is lost '
                  '(Flow.Balances.stock_lost, Flow.Balances.nonrising) and dissipation\'s loss per taker.',
                  '复用 Becoming.Entropy 的无所增益（Flow.GainlessOn）、存量降低所失之量（Flow.Balances.stock_lost、Flow.Balances.nonrising）及耗散中每个取者的损失。',
                  'A gainless family falls by exactly what it loses.', '无所增益的家族恰降低其所失。',
                  'The beyond\'s fall by the rise and the loss.', '其外降低上升之量加损失。',
                  'Balance.', '平衡。', src('Entropy'))
TERM_DEP = dep('selection-term-over-generations', 'formal-reuse',
               'Reuses Becoming.SelectionTerm\'s generations, discordance and its laws over a stretch (Generations, '
               'discord_zero_of_below, not_lower, moved_by_selection, lowered_exact).',
               '复用 Becoming.SelectionTerm 的世代、不一致及其在一段上的规律（Generations、discord_zero_of_below、not_lower、moved_by_selection、lowered_exact）。',
               'The mean over generations moved only by selection proper and transmission.',
               '世代中的均值只经由真正的选择与传递而移动。',
               'The share reaching beyond over generations.', '世代中伸向之外者的份额。',
               'More offspring going only to raisers; reaching transmitted.', '后代更多者只是升高者；伸向之外被传递。',
               src('SelectionTerm'))
DEP_DEP = dep('becoming-dependence-dynamics', 'formal-reuse',
              'Reuses Becoming.Dependence\'s broken and kept dependences (Web.Broken, Web.Kept) and activity needing '
              'support (Web.Dependent).',
              '复用 Becoming.Dependence 的被打断与被保持的依存（Web.Broken、Web.Kept）及活动需要支持（Web.Dependent）。',
              'A met dependence is kept or broken across a step; under Dependent a formation active is supported.',
              '被满足的依存跨一步被保持或被打断；在 Dependent 下活跃的构成是被支持的。',
              'Which dependence the rise breaks, and that its formation does not go on as it was.',
              '上升打断哪个依存，以及其构成不再照旧。',
              'Dependent for the endings.', '终止需 Dependent。', src('Dependence'))

rec = {
    'schema_version': 2, 'id': RID,
    'title': {'en': 'What a rise draws from beyond', 'zh': '上升从其外汲取什么'},
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F04', 'reviewed_at_utc': NOW,
    'statement': {
        'en': 'Where the whole gains nothing, the beyond falls by the rise and the loss; past the slack of the '
              'dependences there one breaks, unseen by a selection rewarding the rise; raising is reaching beyond, '
              'whose share over generations favouring raisers is never selected against; closed, the beyond bounds it.',
        'zh': '整体无所增益时，其外降低上升之量加损失；超出其外依存的余量时其中一个被打断，奖励上升的选择看不见它；升高即伸向之外，在偏向升高者的世代中其份额从不被逆向选择；封闭时其外约束上升。'},
    'laws': [{'en': en, 'zh': zh, 'declarations': resolve(MOD, names)} for en, zh, names in laws],
    'hypotheses': [{
        'en': 'No axiom. Balance; the whole (the family with the conditions beyond, and with any listed conditions nothing '
              'depends on) gaining nothing across the step; a dependence named on each condition beyond, met at the step. '
              'Endings take Dependent, and breaks_beyond_ends the dependence as it was after the step; the selection law '
              'takes every coupled condition in the family and the beyond outside it. Over generations: members taking '
              'part, more offspring only to raisers, reaching transmitted (exactly, for share_moved_rises).',
        'zh': '不加公理。平衡；整体（家族连同其外的条件，以及所列的无所依存的条件）跨该步无所增益；在其外每个条件上指名一个依存，在该步被满足。终止需 Dependent，breaks_beyond_ends 还需依存在步后照旧；选择之律需耦合入的条件都在家族中、其外在家族之外。世代：成员参与流，后代更多者只是升高者，伸向之外被传递（share_moved_rises 需精确）。'}],
    'does_not_show': [
        {'en': 'That more offspring go to raisers: a premise, not derived from the flow; the offspring relation is any '
               'listing of generations, not descent in the flow.',
         'zh': '后代更多者归于升高者：这是前提，不由流导出；后代关系是任意列出的世代，不是流中的世系。',
         'kind': 'scope'},
        {'en': 'Which dependence breaks when several formations take at once, or that the selecting formation causes the '
               'break beyond the accounting; the break is read at the step\'s start, as in Becoming.Dependence.',
         'zh': '多个构成同时汲取时哪个依存被打断，或除记账之外选择者导致了打断；打断按该步开始时读出，如 Becoming.Dependence。',
         'kind': 'scope'},
        {'en': 'Replenishment of the beyond from outside the whole, which the gainless premise excludes, and the rise it '
               'sustains; the openness law bounds the family\'s stock, not the share.',
         'zh': '来自整体之外对其外的补充（无所增益的前提排除了它）及其所维持的上升；开放之律约束的是家族的存量，不是份额。',
         'kind': 'scope'},
        {'en': 'That the draw is wrong or the ending a harm: the laws say where what a rise draws lands and why a '
               'selection through the group does not register it.',
         'zh': '汲取是错的或终止是伤害：这些规律说的是上升所汲取者落在何处，以及经群体的选择为何不记下它。',
         'kind': 'non-implication'}],
    'counterexamples': [{'path': src(MOD), 'detail': {
        'en': 'Lapsing: with the same offspring, more going to the taker which raises the store, nothing is discordant, '
              'yet the taker\'s offspring do not reach beyond and the share falls from a half to nothing: selection alone '
              'does not carry the share (Lapsing.share_falls). WithinSlack: a rise equal to the slack breaks nothing.',
        'zh': 'Lapsing：后代相同，更多归于升高库存的取者，没有不一致的对，但取者的后代不伸向之外，份额从二分之一降到零：仅靠选择不能延续份额（Lapsing.share_falls）。WithinSlack：等于余量的上升什么也不打断。'}}],
    'standard_boundaries': BOUNDS,
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {n_decl} declarations of '
              f'Becoming.{MOD}, {n_thm} of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'Built and reviewed in one session, with no separate reviewer; author review in study section {N}; not '
              'independently reviewed by a person.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.{MOD} 的 {n_decl} 项声明（{n_thm} 项定理）公理报告为空；'
              f'检查器并核对核心纯净。在一个会话中构建并审查，没有另设审查者；作者审查见研究第 {N} 节；未经人的独立审查。'},
    'next_delta': {
        'en': 'Offspring numbers tied to what a formation gives, so that the share laws\' premise follows from the flow; '
              'which dependence breaks when several take at once; replenishment from outside the whole; an independent '
              'review.',
        'zh': '后代数与构成所给予之量相连，使份额之律的前提由流得出；多个构成同时汲取时哪个依存被打断；来自整体之外的补充；独立审查。'},
    'correspondence': {
        'en': 'The accounting is a conservation law on a closed whole, as in material-flow and ecological budgets; the '
              'slack is the buffer of the dependences there, so a draw within it is absorbed and past it breaks one '
              '(compare thresholds in Becoming.Tolerance). The share law is the selection term proper of Price\'s '
              'equation on an indicator, with zero discordance. Readings (the AI\'s): the selection that rewards a rise '
              'rewards, past the slack beyond, ending or changing what it cannot see; reaching beyond spreads as far as '
              'it is carried and, closed, no further than the beyond holds.',
        'zh': '记账是封闭整体上的守恒律，如物质流与生态收支；余量是那里诸依存的缓冲，所以余量之内的汲取被吸收，超出则打断一个（比较 Becoming.Tolerance 中的阈值）。份额之律是 Price 方程中真正的选择项在指示量上、不一致为零的情形。读法（AI 的）：奖励上升的选择，超出其外的余量后，奖励的是终止或改变它看不见的东西；伸向之外传播到它被延续之处，封闭时不超过其外所有。'},
    'canonical_source': src(MOD),
    'aliases': ['what a rise draws from beyond', '上升从其外汲取什么', 'a rise above the slack breaks a dependence beyond',
                'the share that reaches beyond', 'Becoming.Flow.Balances.breaks_beyond',
                'Becoming.Flow.favours_breaking_beyond', 'Becoming.Flow.share_not_against'],
    'dependencies': [REACH_DEP, ENTROPY_DEP, TERM_DEP, DEP_DEP],
    'related': [
        {'id': 'raising-what-couples-in-draws-from-beyond', 'detail': {
            'en': 'Whether what the rise draws from beyond is depended on, how much more is drawn, and the share that '
                  'reaches beyond, which that record left open.',
            'zh': '上升从其外所汲取者是否被依存、多汲取多少，以及伸向之外者的份额，即该记录留下的开放问题。'}},
        {'id': 'the-gap-for-ones-own-act', 'detail': {
            'en': 'The broken dependence lies on a condition no member couples into, so by the gap no selection through '
                  'a member registers it.',
            'zh': '被打断的依存所在的条件无一成员耦合入，所以按其缺口，经任何成员的选择都不记下它。'}}],
    'references': [{'path': src(MOD), 'role': 'proof', 'declarations': sorted(d['name'] for d in m['declarations']),
                    'sha256': sha(src(MOD))},
                   {'path': src('SelectionReach'), 'role': 'proof', 'sha256': sha(src('SelectionReach'))},
                   {'path': src('SelectionTerm'), 'role': 'proof', 'sha256': sha(src('SelectionTerm'))},
                   {'path': src('Entropy'), 'role': 'proof', 'sha256': sha(src('Entropy'))},
                   {'path': src('Dependence'), 'role': 'proof', 'sha256': sha(src('Dependence'))},
                   {'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
                   {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
                   {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)}],
    'proof_bindings': [{'source': src(MOD), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{MOD}',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': f'20 October 2026: added (RB1), section 8.1 item 10: whether what a rise draws is depended on, how much is '
              f'drawn, and the share that reaches beyond; study section {N}.',
        'zh': f'2026年10月20日：新增（RB1），第 8.1 节第 10 项：上升所汲取者是否被依存、汲取多少，以及伸向之外者的份额；研究第 {N} 节。'}],
}
assert len(rec['statement']['en']) <= 300, len(rec['statement']['en'])
path = RECORDS / f'{RID}.json'
assert not path.exists(), ('record exists', RID)
path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
print('written', RID)

# The record it continues.
p = RECORDS / 'raising-what-couples-in-draws-from-beyond.json'
d = json.loads(p.read_text())
k = [i for i, x in enumerate(d['does_not_show']) if x['en'].startswith('How much more than the rise is drawn beyond;')]
assert len(k) == 1, k
d['does_not_show'][k[0]] = {
    'en': 'That drawing from beyond is wrong. How much more than the rise is drawn, and whether what is drawn is '
          f'depended on, are stated in Becoming.DrawnBeyond (record {RID}): exactly the loss more, and depended on past '
          'the slack of the dependences there.',
    'zh': f'取自其外是错的。比上升多取多少、所取者是否被依存，陈述于 Becoming.DrawnBeyond（记录 {RID}）：恰多出损失之量，超出那里诸依存的余量即被依存。',
    'kind': 'non-implication'}
k = [i for i, x in enumerate(d['does_not_show']) if x['en'].startswith('The rising share of what reaches beyond')]
assert len(k) == 1, k
d['does_not_show'][k[0]] = {
    'en': f'The share of what reaches beyond over generations is stated in Becoming.DrawnBeyond (record {RID}), under '
          'the premise that more offspring go to raisers; that premise is not derived from the flow.',
    'zh': f'世代中伸向之外者的份额陈述于 Becoming.DrawnBeyond（记录 {RID}），前提是后代更多者归于升高者；该前提不由流导出。',
    'kind': 'scope'}
d['next_delta'] = {
    'en': 'Offspring numbers tied to what a formation gives (record ' + RID + '); replenishment from outside the whole; an '
          'independent review.',
    'zh': '后代数与构成所给予之量相连（记录 ' + RID + '）；来自整体之外的补充；独立审查。'}
d['related'].append({'id': RID, 'detail': {
    'en': 'Whose dependence the draw breaks past the slack, how much is drawn, and the share that reaches beyond.',
    'zh': '超出余量时汲取打断谁的依存、汲取多少，以及伸向之外者的份额。'}})
for r in d['references']:
    if r['path'] == CHAPTER:
        r['sha256'] = sha(CHAPTER)
d['history'].append({
    'en': f'20 October 2026, RB1: whether what is drawn is depended on, how much more than the rise is drawn and the '
          f'rising share of what reaches beyond are stated in Becoming.DrawnBeyond (record {RID}, study section {N}); the '
          'scope items now point there and those parts leave the next step. The claim is unchanged.',
    'zh': f'2026年10月20日，RB1：所取者是否被依存、比上升多取多少、伸向之外者份额的上升，陈述于 Becoming.DrawnBeyond（记录 {RID}，研究第 {N} 节）；范围项现指向那里，这些部分移出下一步。论断不变。'})
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated', p.name)
