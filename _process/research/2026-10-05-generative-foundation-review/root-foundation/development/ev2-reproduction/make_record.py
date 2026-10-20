#!/usr/bin/env python3
"""Write EV2's record and update the record it continues (selection-term-over-generations):
python3 -B make_record.py CORE_RECEIPT STUDY_SECTION   (from the checkout root, after apply_text.py)

Every declaration cited is resolved against the receipt's audited declarations of Becoming.Reproduction (a short
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
MOD = 'Reproduction'
core_id, N = sys.argv[1], int(sys.argv[2])
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
HEAD = f'## {N}. What bounds offspring numbers, and selection on offspring number itself (EV2)'
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


RID = 'what-bounds-offspring-numbers'
R = 'Reproduction.'
B = 'Reproduction.Generations.ByNumber.'
F = 'Reproduction.Flow.'
laws = [
    ('With no premise: read on the weights themselves no pair is discordant, so the number of members times the total of '
     'the squared weights is the square of the total weight with the squared differences over pairs; never below the '
     'square, and equal exactly where the weights are uniform. Divided through, the mean square is the square of the mean '
     'with the variance.',
     '不加前提：以权重读其自身，没有不一致的对，故成员数乘权重平方之和，等于总权重的平方加上各对差的平方；从不低于该平方，恰在权重均匀处相等。除尽后，均方等于均值的平方加方差。',
     [R + 'excess_cross', R + 'discord_self', R + 'concord_self', R + 'variation', R + 'never_against',
      R + 'concord_self_zero_iff', R + 'none_iff_uniform']),
    ('With offspring numbers as the weights: the number of parents times their offspring numbers weighted by their '
     'offspring numbers is the square of the number of offspring with the squared differences; over offspring the mean of '
     'their parent\'s offspring number is at least the mean over parents, and equal exactly where offspring numbers are '
     'uniform.',
     '以后代数为权重：亲代数乘以后代数加权的后代数，等于后代数的平方加上各差的平方；在后代上，其亲代后代数的均值至少是亲代上的均值，恰在后代数均匀处相等。',
     [R + 'number_variation', R + 'number_never_against', R + 'number_none_iff']),
    ('Over generations read by offspring number, a generation\'s total is the next size and no pair is discordant; the size '
     'times the size two steps on, with what transmission lowered, is the square of the next size with the concordance and '
     'what transmission raised. Where transmission lowers none, the mean offspring number does not fall.',
     '以后代数读世代，一代的总量是下一代的规模，且无不一致的对；规模乘两步后的规模，加上传递所降低的，等于下一代规模的平方加上一致与传递所升高的。传递不降低任何后代数时，平均后代数不降。',
     [R + 'Generations.ByNumber', B + 'sum_eq', B + 'discord_none', B + 'concord_eq', B + 'step', B + 'not_lower_step']),
    ('With exact transmission (each offspring leaving as many offspring as its parent), the mean offspring number rises '
     'across a step exactly where offspring numbers vary and is kept exactly where they are uniform: the counting form of '
     'Fisher\'s fundamental theorem with exact transmission.',
     '传递精确时（每个后代留下与其亲代一样多的后代），平均后代数跨一步恰在后代数有差异处上升，恰在均匀处保持：传递精确时 Fisher 基本定理的计数形式。',
     [B + 'rises_exact_iff', B + 'kept_exact_iff']),
    ('Where a mean fell over a stretch, some step fell, found by deciding each step (a bounded search); a step falls '
     'exactly where what transmission lowered, with the discordant pairs, exceeds the concordance with what transmission '
     'raised; an empty generation leaves every later one empty.',
     '均值在一段上下降之处，某一步下降，逐步判定（有界搜索）即可找到；一步下降，恰在传递所降低的加上不一致的对超过一致与传递所升高的之处；空的一代使此后每一代皆空。',
     [R + 'search', R + 'Generations.fell_step', R + 'Generations.falls_step_iff', R + 'Generations.empty_from']),
    ('A descendant is given to by its parent, at least one unit, so a parent\'s offspring number is at most what it gives '
     'them. Its offspring distinct and standing within a family dissipated on across the step, its offspring number with '
     'one more where there is any is at most what it takes from the family: the weights are amounts the flow fixes.',
     '后代由其亲代给予，至少一单位，故亲代的后代数至多为它给予它们的量。其后代互异且立于跨这一步被耗散的族内时，后代数（有后代时加一）至多为它从该族所取之量：权重是流所定的量。',
     [F + 'born_le_given', F + 'born_le_given_family', F + 'number_within_take']),
    ('Across a step at which a family is balanced and dissipated on, distinct offspring standing within it number, with the '
     'formations taking from it, at most its stock before the step; where any offspring stand within it, some formation '
     'takes from it.',
     '在一个族跨一步平衡且被耗散之处，立于其内的互异后代，连同从中取者，至多为该步前的存量；有后代立于其内之处，必有某形成从中取。',
     [F + 'born_within_stock', F + 'takers_pos_of_born', R + 'born_flatMap', R + 'mem_flatMap_cases']),
    ('Over generations of descent whose offspring stand within a family balanced and dissipated on across each step of a '
     'stretch, the steps at which the lineage reproduces number at most the stock at the start; over steps up to that '
     'stock, the generation after them is empty.',
     '在后代立于一个族内、该族跨一段的每一步平衡且被耗散的世系世代中，世系繁殖的步数至多为起点的存量；经过至多该存量的步数，其后的一代为空。',
     [F + 'reproducing_le_takers', F + 'reproducing_within', F + 'lineage_ends', F + 'last_reproducing']),
    ('Read by offspring number, a lineage that began reproducing within such a family has a step, before the stock runs out, '
     'at which transmission lowered offspring number by more than the concordance and what transmission raised together; '
     'offspring numbers are not transmitted exactly at every step up to the stock.',
     '以后代数读之，在这样的族内开始繁殖的世系，在存量耗尽之前有一步，传递对后代数的降低超过一致与传递所升高的之和；后代数不在至该存量的每一步都精确传递。',
     [F + 'closed_lineage_lowered', F + 'closed_not_exact']),
    ('Witnesses: a parent with two offspring beside one with none (over offspring the mean parental offspring number two, '
     'over parents one); a parent taking three units from a pool and giving one to each of two offspring that never '
     'reproduce (the lineage ends, transmission lowered offspring number by four); a lossless relay keeping a lineage going '
     'within a family of stock one without dissipation.',
     '见证：一个有两个后代的亲代旁边一个没有后代的亲代（后代上亲代后代数的均值为二，亲代上为一）；一个亲代从池中取三单位、给两个永不繁殖的后代各一单位（世系终止，传递使后代数降低四）；无耗散时，无损的接力使世系在存量为一的族内延续。',
     [R + 'Spread.spread', R + 'OnePool.one_pool', R + 'OnePool.balances', R + 'OnePool.dissipates',
      R + 'OnePool.descended', R + 'OnePool.within', R + 'Relay.relay', R + 'Relay.balances', R + 'Relay.not_dissipates',
      R + 'Relay.descended']),
]
for en, zh, _ in laws:
    assert len(en) <= 420 and len(zh) <= 190, (en[:40], len(en), len(zh))

TERM_DEP = dep('selection-term-over-generations', 'formal-reuse',
               'Reuses Becoming.SelectionTerm\'s covariation (concordance and discordance, the balance of each pair), '
               'listed generations (Generations, mean_step, kept_step_iff, rises_step_iff, not_lower), exact transmission '
               'and its witness family Rising.',
               '复用 Becoming.SelectionTerm 的协变（一致与不一致、每一对的平衡）、列出的世代（Generations、mean_step、kept_step_iff、rises_step_iff、not_lower）、精确传递及其见证家族 Rising。',
               'The selection term proper and the mean\'s course over generations.', '真正的选择项及均值在世代中的进程。',
               'Selection on offspring number itself (the variance form) and its meeting with a lineage that ends.',
               '对后代数本身的选择（方差形式）及其与终止之世系的相遇。',
               'None for the identities; ByNumber and exact transmission where named.', '恒等式无；所列处需 ByNumber 与精确传递。',
               src('SelectionTerm'))
DISS_DEP = dep('no-finite-part-bears-taking', 'formal-reuse',
               'Reuses Becoming.Dissipation\'s DissipatesOn, takes_of_gives, BalancesOn.runs_down, takers_within_on and '
               'total_le_of_support, and Becoming.Evolution\'s descent (Flow.DescendsAt).',
               '复用 Becoming.Dissipation 的 DissipatesOn、takes_of_gives、BalancesOn.runs_down、takers_within_on 与 total_le_of_support，以及 Becoming.Evolution 的世系（Flow.DescendsAt）。',
               'A family dissipated on falls by at least its takers; its takers over a stretch number at most its stock.',
               '被耗散的族至少下降其取者之数；一段上的取者至多为其存量。',
               'Offspring numbers bounded by what is taken and by the stock; a lineage within the family ends.',
               '后代数受所取之量与存量约束；族内的世系终止。',
               'Balance and dissipation on the family across the steps used.', '所用各步上该族的平衡与耗散。',
               src('Dissipation'))

rec = {
    'schema_version': 2, 'id': RID,
    'title': {'en': 'What bounds offspring numbers, and selection on offspring number itself',
              'zh': '什么约束后代数，以及对后代数本身的选择'},
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': NOW,
    'statement': {
        'en': 'Selection on offspring number itself is its spread over pairs, never negative; offspring numbers are '
              'bounded by what is given and taken; a lineage within a family dissipated on ends within its stock, so its '
              'transmission must lower offspring number by more than selection raises it.',
        'zh': '对后代数本身的选择即其在各对上的离散，从不为负；后代数受给予与所取之量约束；被耗散的族内的世系在其存量内终止，故其传递对后代数的降低必超过选择的升高。'},
    'laws': [{'en': en, 'zh': zh, 'declarations': resolve(MOD, names)} for en, zh, names in laws],
    'hypotheses': [{
        'en': 'No axiom. The identities have no premise: any finite lists and natural-number weights. Over generations: '
              'discrete generations, each listed as the offspring of the last, read by offspring number (ByNumber) where '
              'named, exact transmission where named. The base laws take descent (Flow.DescendsAt), offspring standing '
              'within a family, distinct where named, and balance and dissipation on that family across the steps used.',
        'zh': '不加公理。恒等式不加前提：任意有限列表与自然数权重。世代：离散的世代，每一代列为上一代的后代，所列处以后代数读（ByNumber），所列处传递精确。流上之律需世系（Flow.DescendsAt）、后代立于一族之内（所列处互异），以及所用各步上该族的平衡与耗散。'}],
    'does_not_show': [
        {'en': 'Fisher\'s theorem in general: the additive part (the regression of offspring number on what is carried) '
               'and the rational reading (variance over mean) are not stated; the statement is the case of exact '
               'transmission of offspring number, denominators cleared.',
         'zh': '一般形式的 Fisher 定理：加性部分（后代数对所载之物的回归）与有理数的读法（方差除以均值）未陈述；所陈述的是后代数精确传递的情形，分母消去。',
         'kind': 'scope'},
        {'en': 'Where something flows into the family from outside, the bounds read only its stock and what flows in: '
               'without dissipation a lossless relay keeps a lineage going within a family of stock one (Relay). Whether '
               'actual lineages lie within such families is an application question.',
         'zh': '有外部之物流入族内之处，诸界只读其存量与流入之物：无耗散时，无损的接力使世系在存量为一的族内延续（Relay）。实际的世系是否位于这样的族内，是应用问题。',
         'kind': 'scope'},
        {'en': 'How much each offspring is given beyond one unit, and a law of forming that is necessary as well as '
               'sufficient, are not stated; dependences newly formed by descent stay open.',
         'zh': '每个后代得到一单位以上多少，以及既必要又充分的形成之律，未陈述；世系新形成的依存仍开放。',
         'kind': 'scope'},
        {'en': 'Offspring number is a weight and a reading, not a measure of worth: no amount is said to be better, and '
               'that transmission lowers offspring number says nothing about what ought to be.',
         'zh': '后代数是权重与读数，不是价值的量度：不说哪种量更好；传递降低后代数，不说明应当如何。', 'kind': 'non-implication'}],
    'counterexamples': [{'path': src(MOD), 'detail': {
        'en': 'Without dissipation the lineage law fails: two relata each give their one unit to the other in turn, '
              'losing nothing; the family of the two has stock one at every step and every generation has one member '
              '(Relay.relay).',
        'zh': '无耗散时世系之律不成立：两个关系项轮流把自己的一单位给另一个，毫无损失；二者之族在每一步存量为一，每一代有一个成员（Relay.relay）。'}}],
    'standard_boundaries': BOUNDS,
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {n_decl} declarations of '
              f'Becoming.{MOD}, {n_thm} of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'Built and reviewed in one session, with no separate reviewer; author review in study section {N}; not '
              'independently reviewed by a person.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.{MOD} 的 {n_decl} 项声明（{n_thm} 项定理）公理报告为空；'
              f'检查器并核对核心纯净。在一个会话中构建并审查，没有另设审查者；作者审查见研究第 {N} 节；未经人的独立审查。'},
    'next_delta': {
        'en': 'The additive part of Fisher\'s theorem (a regression read in counting form); offspring numbers bounded by what '
              'a parent takes from the conditions it depends on, with support; a lineage open to inflow, bounded by what '
              'flows in; an independent review.',
        'zh': 'Fisher 定理的加性部分（以计数形式读出的回归）；以亲代从其所依存条件所取之量、连同支持来约束后代数；向流入开放的世系，受流入之量约束；独立审查。'},
    'correspondence': {
        'en': 'Fisher\'s fundamental theorem (Fisher 1930) in its case of exact transmission: the change of mean fitness '
              'is the variance of fitness over its mean. With n_t the size of generation t, number_variation and '
              'ByNumber.step say n_t n_(t+2) - n_(t+1)^2 = concordance + n_t(raised - lowered), the concordance over ordered '
              'pairs being n_t^2 times the variance of offspring number; Price (1972) reads the general theorem as the '
              'partial change, the rest left to the environment. That a finite closed resource ends reproduction is the '
              'Malthusian bound. Readings (the AI\'s): selection on offspring number never lowers its mean; where nothing '
              'flows in, transmission must.',
        'zh': 'Fisher 基本定理（Fisher 1930）在传递精确时的情形：平均适应度的变化等于适应度的方差除以其均值。以 n_t 为第 t 代的规模，number_variation 与 ByNumber.step 说 n_t n_(t+2) - n_(t+1)^2 = 一致 + n_t(升高 - 降低)，有序对上的一致为 n_t^2 乘后代数的方差；Price（1972）把一般定理读作部分变化，其余归于环境。有限封闭资源使繁殖终止，即马尔萨斯界。读法（AI 的）：对后代数的选择从不降低其均值；无物流入之处，传递必降低它。'},
    'canonical_source': src(MOD),
    'aliases': ['what bounds offspring numbers', '什么约束后代数', 'selection on offspring number itself',
                'variance form of the response to selection', 'counting form of Fisher\'s fundamental theorem',
                'a lineage within a closed family ends', 'Becoming.Reproduction.variation',
                'Becoming.Reproduction.Flow.lineage_ends', 'Becoming.Reproduction.Flow.closed_lineage_lowered'],
    'dependencies': [TERM_DEP, DISS_DEP],
    'related': [
        {'id': 'selection-term-over-generations', 'detail': {
            'en': 'The variance form and the bound on offspring numbers that selection-term-over-generations left open.',
            'zh': 'selection-term-over-generations 留下的方差形式与后代数之界。'}},
        {'id': 'evolution-on-descent', 'detail': {
            'en': 'Descent read with what it gives: offspring numbers bounded by giving and taking, and a lineage that ends '
                  'within a closed family.',
            'zh': '连同所给予之量读出的世系：后代数受给予与所取约束，以及在封闭族内终止的世系。'}}],
    'references': [{'path': src(MOD), 'role': 'proof', 'declarations': sorted(d['name'] for d in m['declarations']),
                    'sha256': sha(src(MOD))},
                   {'path': src('SelectionTerm'), 'role': 'proof', 'sha256': sha(src('SelectionTerm'))},
                   {'path': src('Dissipation'), 'role': 'proof', 'sha256': sha(src('Dissipation'))},
                   {'path': src('Evolution'), 'role': 'proof', 'sha256': sha(src('Evolution'))},
                   {'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
                   {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
                   {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)}],
    'proof_bindings': [{'source': src(MOD), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{MOD}',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': f'20 October 2026: added (EV2), section 8.1 item 9\'s bound on offspring numbers and the variance form; '
              f'study section {N}.',
        'zh': f'2026年10月20日：新增（EV2），第 8.1 节第 9 项的后代数之界与方差形式；研究第 {N} 节。'}],
}
assert len(rec['statement']['en']) <= 300, len(rec['statement']['en'])
path = RECORDS / f'{RID}.json'
assert not path.exists(), ('record exists', RID)
path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
print('written', RID)

# The record it continues.
p = RECORDS / 'selection-term-over-generations.json'
d = json.loads(p.read_text())
k = [i for i, x in enumerate(d['does_not_show']) if x['en'].startswith('The variance form of the response to selection')]
assert len(k) == 1, k
d['does_not_show'][k[0]] = {
    'en': 'A law of forming that is necessary as well as sufficient, and dependences newly formed by descent. The variance '
          'form (in the case of exact transmission of offspring number) and how offspring numbers are bounded by what is '
          f'given are stated in Becoming.Reproduction (record {RID}).',
    'zh': f'既必要又充分的形成之律，以及世系新形成的依存。方差形式（后代数精确传递的情形）与后代数如何受给予之量约束，陈述于 Becoming.Reproduction（记录 {RID}）。',
    'kind': 'scope'}
d['next_delta'] = {
    'en': 'The additive part of Fisher\'s theorem; a witness of selection proper on a flow with more than one parent; an '
          'independent review.',
    'zh': 'Fisher 定理的加性部分；流上有多于一个亲代的真正选择的见证；独立审查。'}
d['related'].append({'id': RID, 'detail': {
    'en': 'Selection on offspring number itself (the variance form), offspring numbers bounded by what is given and taken, '
          'and a lineage within a closed family that ends.',
    'zh': '对后代数本身的选择（方差形式）、受给予与所取之量约束的后代数，以及在封闭族内终止的世系。'}})
for r in d['references']:
    if r['path'] == CHAPTER:
        r['sha256'] = sha(CHAPTER)
d['history'].append({
    'en': f'20 October 2026, EV2: the variance form and the bound on offspring numbers are stated in Becoming.Reproduction '
          f'(record {RID}, study section {N}); the scope item naming them now points there and the next step is revised. '
          'The claim is unchanged.',
    'zh': f'2026年10月20日，EV2：方差形式与后代数之界陈述于 Becoming.Reproduction（记录 {RID}，研究第 {N} 节）；列出它们的范围项现指向那里，下一步相应修订。论断不变。'})
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated', p.name)
