#!/usr/bin/env python3
"""Write EV1's record and update the record it continues (evolution-on-descent):
python3 -B make_record.py CORE_RECEIPT STUDY_SECTION   (from the checkout root, after apply_text.py)

Every declaration cited is resolved against the receipt's audited declarations of Becoming.SelectionTerm (a short
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
MOD = 'SelectionTerm'
core_id, N = sys.argv[1], int(sys.argv[2])
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
HEAD = f'## {N}. The selection term proper and its course over generations (EV1)'
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


RID = 'selection-term-over-generations'
S = 'SelectionTerm.'
G = 'SelectionTerm.Generations.'
laws = [
    ('With no premise: over any finite family read with weights and amounts, the number of members times the weighted '
     'total, with the discordant pairs (more weight with less amount), is the total weight times the total amount, with '
     'the concordant pairs. It rests on one balance for each pair, and is the covariance with its denominators cleared.',
     '不加前提：在以权重与量读出的任意有限家族上，成员数乘加权总量，加上不一致的对（权重更多而量更少），等于总权重乘总量，加上一致的对。它基于每一对的一个平衡，即消去分母的协方差。',
     [S + 'concordPair', S + 'discordPair', S + 'pair_balance', S + 'weighted', S + 'concord', S + 'discord',
      S + 'covariation', S + 'half']),
    ('With offspring numbers as weights, the weighted total exceeds its uniform share exactly where concordance exceeds '
     'discordance and equals it exactly where they are equal; uniform offspring numbers or uniform amounts leave '
     'neither, so the weighted total can move with no selection proper.',
     '以后代数为权重时，加权总量恰在一致超过不一致之处超过其均匀份额，恰在两者相等之处等于它；后代数均匀或量均匀时两者皆无，所以加权总量可以移动而没有真正的选择。',
     [S + 'born', S + 'selection_covariation', S + 'selection_exceeds_iff', S + 'selection_none_iff',
      S + 'concord_uniform', S + 'discord_uniform', S + 'concord_alike', S + 'discord_alike']),
    ('With the counting form of Price\'s equation: the number of parents times the offspring\'s total, with what '
     'transmission lowered so counted and the discordant pairs, is the number of offspring times the parents\' total, '
     'with the concordant pairs and what transmission raised so counted.',
     '与 Price 方程的计数形式合起来：亲代数乘后代总量，加上这样计数的传递所降低的与不一致的对，等于后代数乘亲代总量，加上一致的对与这样计数的传递所升高的。',
     [S + 'offspring_covariation', S + 'Exact', S + 'raised_exact', S + 'lowered_exact']),
    ('Where a member below another in amount has no more weight, nothing is discordant and the weighted total is at least '
     'its uniform share. Where only active formations give and activity needs support, a reading highest at the '
     'supported parents is so: it is never selected against.',
     '一个成员的量低于另一个时权重不更多，就没有不一致的对，加权总量至少是其均匀份额。只有活跃形成给予、活动需要支持时，在被支持的亲代处最高的读数正是如此：它从不被逆向选择。',
     [S + 'discord_zero_of_below', S + 'share_le_of_below', S + 'Flow.support_not_against']),
    ('Over generations each the offspring of the last, the number of offspring is the next size and their total the next '
     'total; the mean amount, compared by cross-multiplying, is kept across a step exactly where selection proper and '
     'transmission balance, and rises exactly where they raise.',
     '在每一代都是上一代后代的世代中，后代数是下一代的规模，其总量是下一代的总量；以交叉相乘比较的均值，恰在真正的选择与传递相抵之处跨一步保持，恰在它们使之升高之处上升。',
     [S + 'Generations', G + 'family', G + 'size', G + 'sum', G + 'born_eq', G + 'offspring_eq', G + 'mean_step',
      G + 'Balanced', G + 'Raises', G + 'kept_step_iff', G + 'rises_step_iff', G + 'empty_after']),
    ('Kept, rising or not falling at every step of a stretch, the mean is so over the stretch; an empty generation leaves '
     'the next empty.',
     '在一段的每一步都保持、上升或不降，均值在整段上也如此；空的一代使下一代也空。',
     [G + 'kept', G + 'rises', G + 'not_lower_step', G + 'not_lower', G + 'empty_sum']),
    ('Where a generation\'s mean differs from the first\'s, some step before it is unbalanced, found by deciding each step; '
     'with exact transmission it has selection proper, with uniform offspring numbers inexact transmission.',
     '一代的均值与第一代不同之处，其前有某一步不相抵，逐步判定即可找到；传递精确时那一步有真正的选择，后代数均匀时那一步传递不精确。',
     [G + 'moved_unbalanced', G + 'balanced_exact_iff', G + 'raises_exact_iff', G + 'moved_by_selection',
      G + 'balanced_uniform_iff', G + 'moved_by_transmission']),
    ('Over generations of descent in a flow where only active formations give and activity needs support, a reading '
     'highest at each generation\'s supported members, which transmission never lowers, has a mean that does not fall '
     'over any stretch; with exact transmission a moved mean rose, through a step where more offspring went with more of '
     'it.',
     '在只有活跃形成给予、活动需要支持的流中，沿世系的世代，在每一代被支持的成员处最高、且传递从不降低的读数，其均值在任何一段上都不降；传递精确时，移动了的均值是上升了，且经由一步，那里后代更多者其读数更多。',
     [S + 'Flow.Descended', S + 'Flow.support_not_lower', S + 'Flow.support_moved_rises']),
    ('Witnesses: a parent carrying one unit with two offspring beside one carrying none with none (exact transmission, '
     'concordance two, the mean rising from a half to one); two parents each with two offspring (the weighted total '
     'moves, selection proper none, the mean kept); Drawdown\'s flow meeting the support laws\' premises.',
     '见证：一个载一单位、有两个后代的亲代，旁边一个什么都不载、没有后代的亲代（传递精确，一致为二，均值从二分之一升到一）；两个各有两个后代的亲代（加权总量移动，真正的选择为零，均值保持）；Drawdown 的流满足支持之律的前提。',
     [S + 'Rising.rising', S + 'Rising.exact', S + 'Doubling.doubling', S + 'SupportedDescent.supported_descent']),
]
for en, zh, _ in laws:
    assert len(en) <= 420 and len(zh) <= 190, (en[:40], len(en), len(zh))

EVO_DEP = dep('evolution-on-descent', 'formal-reuse',
              'Reuses Becoming.Evolution\'s counting form of Price\'s equation (price, selected, raised, lowered, '
              'offspring), descent (Flow.DescendsAt) and selection through support (Flow.unsupported_childless), and its '
              'witness Drawdown.',
              '复用 Becoming.Evolution 的 Price 方程计数形式（price、selected、raised、lowered、offspring）、世系（Flow.DescendsAt）、经支持的选择（Flow.unsupported_childless）及其见证 Drawdown。',
              'Price\'s counting identity, descent, only supported formations leaving descendants.',
              'Price 的计数恒等式、世系、只有被支持的形成留下后代。',
              'The selection term proper, its course over generations, support never selected against.',
              '真正的选择项、它在世代中的进程、支持从不被逆向选择。',
              'Acting and Dependent for the support laws.', '支持之律需 Acting 与 Dependent。', src('Evolution'))
CHANGE_DEP = dep('coming-and-ceasing-keep-pace', 'formal-reuse',
                 'Reuses Becoming.Change\'s excess and its balance (excess_balance), and the totals of Becoming.Flow.',
                 '复用 Becoming.Change 的 excess 及其平衡（excess_balance），以及 Becoming.Flow 的总量。',
                 'Truncated differences and their balance; totals over lists.', '截断差及其平衡；列表上的总量。',
                 'Concordance and discordance as products of excesses.', '以超出之积表示的一致与不一致。',
                 'None.', '无。', src('Change'))

rec = {
    'schema_version': 2, 'id': RID,
    'title': {'en': 'The selection term proper, over generations', 'zh': '真正的选择项及其在世代中的进程'},
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': NOW,
    'statement': {
        'en': 'Price\'s selection term proper is concordance less discordance of offspring number and amount, '
              'denominators cleared; over generations a mean moves only through selection proper or transmission, and '
              'where activity needs support a reading highest at the supported is never selected against.',
        'zh': 'Price 方程中真正的选择项是后代数与量的一致减去不一致，分母消去；在世代中均值只经由真正的选择或传递而移动；活动需要支持时，在被支持者处最高的读数从不被逆向选择。'},
    'laws': [{'en': en, 'zh': zh, 'declarations': resolve(MOD, names)} for en, zh, names in laws],
    'hypotheses': [{
        'en': 'No axiom. The identities have no premise: any finite lists, any natural-number weights and amounts. Over '
              'generations: discrete generations, each listed as the offspring of the last. The support laws take '
              'Acting and Dependent, generations of descent (Flow.Descended), a reading highest at each generation\'s '
              'supported members, and transmission never lowering it (exact, for support_moved_rises).',
        'zh': '不加公理。恒等式不加前提：任意有限列表、任意自然数的权重与量。世代：离散的世代，每一代列为上一代的后代。支持之律需 Acting 与 Dependent、世系的世代（Flow.Descended）、在每一代被支持的成员处最高的读数，以及传递从不降低它（support_moved_rises 需传递精确）。'}],
    'does_not_show': [
        {'en': 'The rational reading: the covariance as concordance less discordance over the square of the number of '
               'parents, and the standard form of Price\'s equation, are arithmetic on the identities and not stated; '
               'nor are rational amounts beyond a common denominator.',
         'zh': '有理数的读法：协方差即一致减不一致除以亲代数的平方，以及 Price 方程的标准形式，是这些恒等式上的算术，未陈述；公分母之外的有理数的量亦未陈述。',
         'kind': 'scope'},
        {'en': 'The variance form of the response to selection (Fisher\'s fundamental theorem), a law of forming that is '
               'necessary as well as sufficient, dependences newly formed by descent, and how offspring numbers are bounded '
               'by what is given.',
         'zh': '对选择的响应的方差形式（Fisher 的基本定理）、既必要又充分的形成之律、世系新形成的依存，以及后代数如何受给予之量约束。',
         'kind': 'scope'},
        {'en': 'That transmission never lowers a reading is a premise, as TransmitsWithin is; the support laws read a '
               'reading highest at the supported members, not support itself carried by descent, and on Drawdown the '
               'rise comes from transmission, as its single parent leaves no pair.',
         'zh': '传递从不降低读数是前提，如 TransmitsWithin；支持之律读的是在被支持成员处最高的读数，不是由世系承载的支持本身；在 Drawdown 上上升来自传递，因为唯一的亲代不构成对。',
         'kind': 'scope'},
        {'en': 'Fitness is not defined and no amount is said to be better: offspring numbers enter only as weights.',
         'zh': '适应度没有定义，也不说哪种量更好：后代数只作为权重。', 'kind': 'non-implication'}],
    'counterexamples': [{'path': src(MOD), 'detail': {
        'en': 'Two parents each with two offspring carrying their amounts: the weighted total is twice the parents\' total, '
              'so it moves, while concordance and discordance are both none and the mean is kept (Doubling.doubling).',
        'zh': '两个亲代各有两个承载其量的后代：加权总量是亲代总量的两倍，所以它移动，而一致与不一致都为零，均值保持（Doubling.doubling）。'}}],
    'standard_boundaries': BOUNDS,
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {n_decl} declarations of '
              f'Becoming.{MOD}, {n_thm} of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'Built and reviewed in one session, with no separate reviewer; author review in study section {N}; not '
              'independently reviewed by a person.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.{MOD} 的 {n_decl} 项声明（{n_thm} 项定理）公理报告为空；'
              f'检查器并核对核心纯净。在一个会话中构建并审查，没有另设审查者；作者审查见研究第 {N} 节；未经人的独立审查。'},
    'next_delta': {
        'en': 'A law of reproduction bounding offspring numbers by what is given; the variance form; a witness of selection '
              'proper on a flow; an independent review.',
        'zh': '以给予之量约束后代数的繁殖之律；方差形式；流上真正选择的见证；独立审查。'},
    'correspondence': {
        'en': 'Price\'s equation (Price 1970): with mean offspring number w̄, w̄Δz̄ = Cov(w, z) + E(wΔz). Divided by the '
              'square of the number of parents, offspring_covariation is this identity; concordance less discordance over '
              'ordered pairs is n² Cov(w, z), the pair form of covariance also used for Kendall\'s concordance. The '
              'counting of a moved mean through an unbalanced step is the counting form of the response to selection '
              'over generations (Frank 2012). Readings (the AI\'s): the selection term proper is how far more offspring '
              'go with more of an amount; where only the supported give, what reads support is never selected against.',
        'zh': 'Price 方程（Price 1970）：以平均后代数 w̄，w̄Δz̄ = Cov(w, z) + E(wΔz)。除以亲代数的平方，offspring_covariation 即此恒等式；有序对上的一致减不一致即 n² Cov(w, z)，即 Kendall 一致性所用的协方差对形式。经由不相抵之步对移动均值的计数，是世代中对选择之响应的计数形式（Frank 2012）。读法（AI 的）：真正的选择项是后代更多与量更多相伴的程度；只有被支持者给予之处，读出支持的从不被逆向选择。'},
    'canonical_source': src(MOD),
    'aliases': ['the selection term proper, over generations', '真正的选择项及其在世代中的进程',
                'covariance form of Price\'s equation', 'response to selection over generations',
                'Becoming.SelectionTerm.covariation', 'Becoming.SelectionTerm.offspring_covariation',
                'Becoming.SelectionTerm.Flow.support_not_lower'],
    'dependencies': [EVO_DEP, CHANGE_DEP],
    'related': [
        {'id': 'evolution-on-descent', 'detail': {
            'en': 'The selection term proper that evolution-on-descent left unstated, and selection through support read '
                  'over generations.',
            'zh': 'evolution-on-descent 未陈述的真正选择项，以及在世代中读出的经支持的选择。'}}],
    'references': [{'path': src(MOD), 'role': 'proof', 'declarations': sorted(d['name'] for d in m['declarations']),
                    'sha256': sha(src(MOD))},
                   {'path': src('Evolution'), 'role': 'proof', 'sha256': sha(src('Evolution'))},
                   {'path': src('Change'), 'role': 'proof', 'sha256': sha(src('Change'))},
                   {'path': src('Flow'), 'role': 'proof', 'sha256': sha(src('Flow'))},
                   {'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
                   {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
                   {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)}],
    'proof_bindings': [{'source': src(MOD), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{MOD}',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': f'20 October 2026: added (EV1), section 8.1 item 9\'s covariance form and its course over many steps; study '
              f'section {N}.',
        'zh': f'2026年10月20日：新增（EV1），第 8.1 节第 9 项的协方差形式及其多步进程；研究第 {N} 节。'}],
}
assert len(rec['statement']['en']) <= 300, len(rec['statement']['en'])
path = RECORDS / f'{RID}.json'
assert not path.exists(), ('record exists', RID)
path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
print('written', RID)

# The record it continues.
p = RECORDS / 'evolution-on-descent.json'
d = json.loads(p.read_text())
k = [i for i, x in enumerate(d['does_not_show']) if x['en'].startswith('The selection term proper, the covariance')]
assert len(k) == 1, k
d['does_not_show'][k[0]] = {
    'en': 'The selection term proper is not stated in this module: it is stated in counting form, with its course over '
          f'generations, in Becoming.SelectionTerm (record {RID}).',
    'zh': f'真正的选择项不在此模块中陈述：它的计数形式及其在世代中的进程陈述于 Becoming.SelectionTerm（记录 {RID}）。',
    'kind': 'scope'}
old = d['next_delta']['en']
assert 'rational amounts and the covariance form; ' in old and '; the accumulation of selection and transmission over many steps' in old
d['next_delta'] = {
    'en': 'A law of forming that is also necessary; how the number of offspring is bounded by the amounts given (a reading '
          'of reproduction); correspondence theorems to structural copying, reconstruction and the inheritance of '
          'organizational rules (periphery).',
    'zh': '同时是必要条件的形成规律；后代数如何受给予的量约束（繁殖的读法）；与结构复制、重构及组织规则继承的对应定理（外围）。'}
d['related'].append({'id': RID, 'detail': {
    'en': 'The selection term proper in counting form, the mean\'s course over generations, and support never selected '
          'against.',
    'zh': '计数形式的真正选择项、均值在世代中的进程，以及支持从不被逆向选择。'}})
for r in d['references']:
    if r['path'] == CHAPTER:
        r['sha256'] = sha(CHAPTER)
d['history'].append({
    'en': f'20 October 2026, EV1: the covariance form and the accumulation over many steps are stated in '
          f'Becoming.SelectionTerm (record {RID}, study section {N}); the scope item saying the selection term proper is '
          'not stated now points there, and those two parts leave the next step. The claim is unchanged.',
    'zh': f'2026年10月20日，EV1：协方差形式与多步累积陈述于 Becoming.SelectionTerm（记录 {RID}，研究第 {N} 节）；说明真正选择项未陈述的范围项现指向那里，这两部分移出下一步。论断不变。'})
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated', p.name)
