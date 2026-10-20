#!/usr/bin/env python3
"""Write IV1's records what-the-step-across-standpoints-reaches and widening-as-what-every-weighting-ranks:
python3 -B make_record.py CORE_RECEIPT STUDY_SECTION   (from the checkout root, after land_text.py)

Every declaration cited is resolved against the receipt's audited declarations of Becoming.Weightings (a short
name must match exactly one declaration by suffix), and the receipt must bind the module's current bytes.
Adapted from OW1's make_record.py."""
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
REVIEW = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-SIGNIFICANCE-REVIEW.md'
CHOICES = '_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
ARGUMENT = 'theories/becoming/chapters/THE-STEP-OF-INVARIANCE.md'
RECORDS = ROOT / 'theories/becoming/results/records'
MOD = 'Weightings'
core_id, N = sys.argv[1], int(sys.argv[2])
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
HEAD = f'## {N}. The step of invariance: what it reaches across standpoints, and the order every weighting shares (IV1)'
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
ALL = sorted(d['name'] for d in m['declarations'])

VALIDATION = {
    'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {n_decl} declarations of '
          f'Becoming.{MOD}, {n_thm} of them theorems, have empty axiom reports; the checker verifies core purity. The '
          'literature check before any Lean is a section of the significance review; the argument is the chapter '
          f'THE-STEP-OF-INVARIANCE. Built and reviewed in one session, no separate reviewer; author review in study '
          f'section {N}; not independently reviewed by a person.',
    'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.{MOD} 的 {n_decl} 项声明（{n_thm} 项定理）公理报告为空；'
          '检查器并核对核心纯净。动手写 Lean 之前的文献核查是显著性审查中的一节；论证见章节 THE-STEP-OF-INVARIANCE。'
          f'在一个会话中构建并审查，没有另设审查者；作者审查见研究第 {N} 节；未经人的独立审查。'}
HISTORY = lambda en, zh: [{
    'en': f'20 October 2026: added (IV1), {en}, after a literature check (significance review, section "the step of '
          f'invariance and the literature"); readings D59; study section {N}.',
    'zh': f'2026年10月20日：新增（IV1），{zh}，此前做了文献核查（显著性审查“不变之步与文献”一节）；读法 D59；研究第 {N} 节。'}]
COMMON_REFS = [{'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
               {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
               {'path': REVIEW, 'role': 'integration', 'sha256': sha(REVIEW)},
               {'path': CHOICES, 'role': 'integration', 'sha256': sha(CHOICES)},
               {'path': ARGUMENT, 'role': 'statement', 'sha256': sha(ARGUMENT)},
               {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)}]
BINDING = [{'source': src(MOD), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{MOD}',
            'success_pointer': '/status', 'success_value': 'passed'}]


def check(rec):
    assert len(rec['statement']['en']) <= 300, len(rec['statement']['en'])
    assert len(rec['statement']['zh']) <= 150, len(rec['statement']['zh'])
    assert len(rec['correspondence']['en']) <= 1200, len(rec['correspondence']['en'])
    assert len(rec['correspondence']['zh']) <= 500, len(rec['correspondence']['zh'])
    for x in rec['laws']:
        assert len(x['en']) <= 420 and len(x['zh']) <= 190, (x['en'][:40], len(x['en']), len(x['zh']))
    for x in rec['does_not_show']:
        assert len(x['en']) <= 240 and len(x['zh']) <= 110, (x['en'][:40], len(x['en']), len(x['zh']))
    for x in rec['hypotheses']:
        assert len(x['en']) <= 420 and len(x['zh']) <= 190, (x['en'][:40], len(x['en']), len(x['zh']))
    assert len(rec['validation_scope']['en']) <= 600 and len(rec['validation_scope']['zh']) <= 260
    assert len(rec['next_delta']['en']) <= 400 and len(rec['next_delta']['zh']) <= 180
    path = RECORDS / f'{rec["id"]}.json'
    assert not path.exists(), ('record exists', rec['id'])
    return path


# ---------------------------------------------------------------------------------------------------------------
# Record 1: what the step across standpoints reaches.
STEP = 'what-the-step-across-standpoints-reaches'
step_laws = [
    ('Let each standpoint\'s presupposition about its own center\'s continuation hold (sub-true along the empty '
     'relation) and significance be standpoint-invariant. Then from every standpoint the continuation of every center '
     'has significance, and the significance of exactly the centers\' continuation meets both premises: what they '
     'force is exactly that the centers count.',
     '设每个立场关于其中心之延续的预设成立（沿空关系为次真），且意义对立场不变。则从每个立场看，每个中心的延续都有意义，'
     '而恰好诸中心之延续的意义满足这两个前提：二者所迫使的恰是诸中心算数。',
     ['atCenters', 'atCenters_least', 'atCenters_presupposed', 'atCenters_standpointInvariant', 'forced_iff_center']),
    ('With some standpoint, the significance of the centers\' continuation is the continuation condition exactly when '
     'every formation is some standpoint\'s center.',
     '只要有一个立场，诸中心之延续的意义恰在每个构成都是某个立场的中心时，就是延续条件。',
     ['unrestricted_atCenters_iff']),
    ('Along a relation, what every significance making a standpoint\'s presupposition sub-true at a formation\'s '
     'closure gives significance to is exactly what lies within that closure: a standpoint\'s own presupposition, with '
     'nothing else, reaches its closure and no further.',
     '沿一个关系，凡使某立场的预设在某构成的闭包处为次真的意义所共同赋予意义者，恰是该闭包之内者：立场自身的预设，'
     '别无其他时，达到其闭包而不更远。',
     ['forced_iff_within']),
    ('The presupposition sub-true along every relation of a family is significance over the union of the closures; '
     'drawn along being related by some relation of the family, it gives the presupposition along each.',
     '沿一族中每个关系为次真的预设，即在诸闭包之并上的意义；沿“被族中某个关系关联”来画，它给出沿每个关系的预设。',
     ['Related', 'subTrue_every_iff', 'subTrue_every_of_related']),
    ('Witness: of three formations, the first bears one relation to the second and the second another to the third. '
     'The third lies within the first\'s closure along being related at all and within no closure along a single '
     'relation, so the presupposition along every relation one at a time does not give the one along being related.',
     '见证：三个构成中，第一个对第二个有一种关系，第二个对第三个有另一种。第三个在第一个沿“有所关联”的闭包之内，'
     '却不在沿任何单一关系的闭包之内，所以逐一沿每个关系的预设不给出沿“有所关联”的预设。',
     ['Chain.rel', 'Chain.third_related', 'Chain.third_not_within', 'Chain.every_not_related']),
    ('Retaining what has significance at the centers is admitting, at every step, every center the other path admits. '
     'In Clearing, with the clearer the only center, the clearer\'s part retains at the centers against the levels '
     'without it, while under the continuation condition it loses the dweller.',
     '保留在诸中心处有意义者，即在每一步接纳另一路径所接纳的每个中心。在 Clearing 中，以清除者为唯一中心，'
     '清除者的部分相对无它的水平在诸中心处保留，而在延续条件之下它失去居者。',
     ['Web.retains_atCenters_iff', 'Clearing.centers_retain_yet_loses']),
]
rec1 = {
    'schema_version': 2, 'id': STEP,
    'title': {'en': 'What the step across standpoints reaches', 'zh': '跨立场的一步达到哪里'},
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F07', 'reviewed_at_utc': NOW,
    'statement': {
        'en': 'From each standpoint\'s presupposition about its own continuation and standpoint-invariance, exactly the '
              'centers\' continuation is forced to have significance, the continuation condition only where every '
              'formation is a center; a standpoint\'s own presupposition forces exactly its closure.',
        'zh': '由各立场关于自身延续的预设与对立场不变，被迫有意义的恰是诸中心的延续，仅当每个构成都是中心时才是延续条件；'
              '一个立场自身的预设恰迫使其闭包。'},
    'laws': [{'en': en, 'zh': zh, 'declarations': resolve(MOD, names)} for en, zh, names in step_laws],
    'hypotheses': [{
        'en': 'No axiom. Standpoints and formations as types, each standpoint\'s center given as a function; '
              'significance a Prop-valued family indexed by standpoint, step and formation; the presupposition and the '
              'step of invariance as hypotheses of the laws they appear in, never asserted.',
        'zh': '不加公理。立场与构成为类型，每个立场的中心由一个函数给出；意义为按立场、步与构成索引的命题族；预设与不变之步'
              '只作为出现它们的规律的假设，从不断言。'}],
    'does_not_show': [
        {'en': 'The step of invariance itself, or the self\'s presupposition: both are hypotheses, and whether the '
               'presupposition is essentially de se, which decides the narrow or wide scope, is open.',
         'zh': '不变之步本身，或自我的预设：二者都是假设；预设是否本质上是从己的（de se），这决定窄或宽的辖域，仍未定。',
         'kind': 'non-implication'},
        {'en': 'Which formations are centers, or that every formation is one: "what wants its continuation" is read as '
               'the centers, and the reading is the AI\'s (D59).',
         'zh': '哪些构成是中心，或每个构成都是：“想要其延续者”读作诸中心，此读法是 AI 的（D59）。',
         'kind': 'scope'},
        {'en': 'That gaining what the narrower scope retains is better, or that losing what lies beyond it is worse: '
               'scope is fixed, order is C\'s.',
         'zh': '较窄范围所保留者的获得是更好的，或失去其外者是更坏的：范围已定，定序属于 C。',
         'kind': 'non-implication'},
        {'en': 'A right or a duty: Gewirth\'s step from a needed good to a claim on others has no counterpart; '
               'significance is from a standpoint and claims nothing of anyone.',
         'zh': '权利或义务：Gewirth 从所需之善到对他者之要求的那一步在此没有对应；意义是从一个立场而言的，不向任何人要求什么。',
         'kind': 'correspondence'}],
    'counterexamples': [{'path': src(MOD), 'detail': {
        'en': 'Chain: three formations under two relations, where the presupposition along every relation one at a time '
              'leaves the third outside and the one along being related at all includes it '
              '(Chain.every_not_related); Clearing, where the narrower scope retains and the condition loses '
              '(Clearing.centers_retain_yet_loses).',
        'zh': 'Chain：两种关系下的三个构成，逐一沿每个关系的预设把第三个留在外面，沿“有所关联”的预设则包括它'
              '（Chain.every_not_related）；Clearing：较窄的范围保留而条件失去（Clearing.centers_retain_yet_loses）。'}}],
    'standard_boundaries': ['significance-related-not-asserted', 'no-ethical-premise', 'conditional-not-universal',
                            'no-definition-by-verdict', 'names-provisional', 'formal-not-empirical'],
    'validation_scope': VALIDATION,
    'next_delta': {
        'en': 'Whether the self\'s presupposition is essentially de se (the narrow or wide scope); which formations are '
              'centers on the base (a formation whose activity keeps its own conditions); graded significance across '
              'standpoints; an independent philosophical review.',
        'zh': '自我的预设是否本质上是从己的（窄或宽的辖域）；在基底上哪些构成是中心（其活动维持自身条件的构成）；'
              '跨立场的分级意义；独立的哲学审查。'},
    'correspondence': {
        'en': 'The step across standpoints is Gewirth\'s argument from the sufficiency of agency (Reason and Morality, '
              '1978; defended by Beyleveld 1991), with Nagel 1970, Hare 1981 and Korsgaard 1996 as variants; the law '
              'says it reaches exactly the centers, and the egoist objection (Williams 1985; Regis, ed., 1984) is the '
              'narrow scope (Boundaries\' presupposition_scopes). The step across drawings is Parfit\'s (1984, Part '
              'Three) and Siderits\'s Buddhist reductionism (2003), and Wolf\'s (1986) point that reductionism can '
              'dissolve concern is Boundaries\' not_subTrue_of_invariant. Williams\'s internal reasons (1979) reach '
              'exactly the closure (forced_iff_within). The open question is the de se one (Perry 1979, Lewis 1979; '
              'Guillot and O\'Brien 2023 against Setiya).',
        'zh': '跨立场的一步即 Gewirth 的“行动者之充分性”论证（《理性与道德》1978；Beyleveld 1991 辩护），Nagel 1970、Hare 1981 与 '
              'Korsgaard 1996 是其变体；此律说它恰达到诸中心，利己主义的反驳（Williams 1985；Regis 编 1984）即窄辖域'
              '（Boundaries 的 presupposition_scopes）。跨画法的一步是 Parfit（1984 第三部分）与 Siderits 的佛教还原论（2003），'
              'Wolf（1986）指出还原论也可消解关切，即 Boundaries 的 not_subTrue_of_invariant。Williams 的内在理由（1979）恰达到闭包'
              '（forced_iff_within）。悬而未决的是从己问题（Perry 1979、Lewis 1979；Guillot 与 O\'Brien 2023 对 Setiya）。'},
    'canonical_source': src(MOD),
    'aliases': ['what the step across standpoints reaches', '跨立场的一步达到哪里', 'Gewirth\'s step reaches the centers',
                'the narrower scope as the centers', 'what wants its continuation', 'Becoming.forced_iff_center',
                'Becoming.forced_iff_within', 'Becoming.unrestricted_atCenters_iff'],
    'dependencies': [
        {'id': 'continuation-condition-decomposition', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses standpoint-invariance (StandpointInvariant), the condition (Unrestricted) and '
                          'sub-truth along the empty relation (subTrue_empty_iff).',
                    'zh': '复用对立场不变（StandpointInvariant）、条件（Unrestricted）与沿空关系的次真（subTrue_empty_iff）。'},
         'interface': {
             'output': {'en': 'The presupposition along the empty relation is the significance of the center\'s own '
                              'continuation; standpoint-invariance carries significance from one standpoint to another.',
                        'zh': '沿空关系的预设即中心自身延续的意义；对立场不变把意义从一个立场带到另一个。'},
             'input': {'en': 'What the two premises force: exactly the centers.', 'zh': '两个前提所迫使者：恰是诸中心。'},
             'conditions': {'en': 'None.', 'zh': '无。'},
             'evidence': src('Boundaries')}},
        {'id': 'presupposition-scopes', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses the boundary drawn along a relation and its characterization by the closure '
                          '(subTrue_significantWithin_iff).',
                    'zh': '复用沿一个关系所画的边界及其以闭包的刻画（subTrue_significantWithin_iff）。'},
         'interface': {
             'output': {'en': 'The presupposition sub-true at a closure is significance over the closure.',
                        'zh': '在闭包处为次真的预设，即在闭包上的意义。'},
             'input': {'en': 'What a standpoint\'s own presupposition forces, and the union over a family of relations.',
                       'zh': '立场自身的预设所迫使者，以及在一族关系上的并。'},
             'conditions': {'en': 'None.', 'zh': '无。'},
             'evidence': src('Boundaries')}}],
    'related': [
        {'id': 'loss-beyond-a-region', 'detail': {
            'en': 'Clearing\'s clearer loses the dweller beyond its dependence; the narrower scope, with the clearer the '
                  'only center, reads that loss as nothing, and the condition reads it.',
            'zh': 'Clearing 中的清除者在其依存之外失去居者；以清除者为唯一中心的较窄范围把这一损失读作无，条件则读到它。'}},
        {'id': 'widening-as-what-every-weighting-ranks', 'detail': {
            'en': 'The same section\'s order: once scope is fixed, C is what every positive weighting ranks higher.',
            'zh': '同一节中的序：范围一旦确定，C 即每个正的加权都排得更高者。'}}],
    'references': [{'path': src(MOD), 'role': 'proof', 'declarations': ALL, 'sha256': sha(src(MOD))},
                   {'path': src('Boundaries'), 'role': 'proof', 'sha256': sha(src('Boundaries'))},
                   {'path': src('Clearing'), 'role': 'proof', 'sha256': sha(src('Clearing'))}] + COMMON_REFS,
    'proof_bindings': BINDING,
    'history': HISTORY('stating exactly what the step of invariance reaches when it is taken across standpoints '
                       '(Gewirth\'s form) and what a standpoint\'s own presupposition reaches',
                       '确切陈述不变之步跨立场（Gewirth 的形式）时达到哪里，以及一个立场自身的预设达到哪里'),
}

# ---------------------------------------------------------------------------------------------------------------
# Record 2: widening as what every weighting ranks.
ORDER = 'widening-as-what-every-weighting-ranks'
W = 'Weighting.'
order_laws = [
    ('Over a finite listing of items, a course is the items it admits and a weighting gives each a natural weight. '
     'Inclusion never lowers a weighted count, and every weighting positive on every item ranks a widening strictly '
     'higher.',
     '在有限列举的项上，一条进程即其所接纳的项，加权给每项一个自然数权重。包含从不降低加权计数，每个在每项上为正的加权'
     '都把扩大严格排得更高。',
     [W + 'weighed', W + 'Positive', W + 'weighed_le_of_includes', W + 'weighed_lt_of_widens']),
    ('Where one course admits a listed item the other does not, some positive weighting ranks it higher; so a mixed '
     'comparison is decided both ways by positive weightings.',
     '一条进程接纳另一条不接纳的某个所列项时，有某个正的加权把它排得更高；所以混合的比较由正的加权两个方向都能决定。',
     [W + 'outweighing', W + 'outweighs', W + 'mixed_either_way']),
    ('On the listed items one course widens another exactly when every positive weighting ranks it higher.',
     '在所列项上，一条进程扩大另一条，恰当每个正的加权都把它排得更高。',
     [W + 'widens_iff_every_positive']),
    ('Where every item a course admits beyond another weighs nothing, the two weigh the same: a weighting that leaves '
     'an item out does not rank a widening that adds only that item.',
     '一条进程超出另一条所接纳的每一项都权重为零时，两者等重：把某项排除在外的加权，不为只添这一项的扩大排序。',
     [W + 'weighed_eq_of_unweighted']),
    ('Under one positive weight for every item, a course weighs more exactly when it admits more items.',
     '每项同一个正权重之下，一条进程恰在接纳更多项时更重。',
     [W + 'weighed_const', W + 'neutral_ranks_by_number']),
    ('On a web, where admission is decided and what either level path admits is listed, one path widens the other '
     'exactly when every weighting positive on the listed steps and formations ranks it higher.',
     '在依存网上，接纳可判定且两条水平路径所接纳者都已列出时，一条路径扩大另一条，恰当每个在所列步与构成上为正的加权都把它排得更高。',
     ['Web.DecidesAdmission', 'Web.ListsAdmitted', 'Web.widens_iff_every_weighting']),
    ('Where one level path admits a formation at a step and another does not, the other neither widens nor keeps it: '
     'the comparison never ranks the course in which something is closed above the one in which it is not.',
     '一条水平路径在某步接纳某构成而另一条不接纳时，后者既不扩大也不保持前者：这一比较从不把有所关闭的进程排在无所关闭的进程之上。',
     ['Web.not_widens_of_closes']),
]
rec2 = {
    'schema_version': 2, 'id': ORDER,
    'title': {'en': 'Widening as what every weighting ranks', 'zh': '扩大即每个加权所排者'},
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F07', 'reviewed_at_utc': NOW,
    'statement': {
        'en': 'Over a finite listing, one course widens another exactly when every weighting positive on every item '
              'ranks it higher; a mixed comparison is decided both ways by positive weightings; a zero weight ties; '
              'one weight for all ranks by number.',
        'zh': '在有限列举上，一条进程扩大另一条，恰当每个在每项上为正的加权都把它排得更高；混合的比较由正的加权两个方向都能决定；'
              '零权持平；一律同权即按数目排。'},
    'laws': [{'en': en, 'zh': zh, 'declarations': resolve(MOD, names)} for en, zh, names in order_laws],
    'hypotheses': [{
        'en': 'No axiom. Finite listings of items (steps and formations); admission two-valued (Bool) and, on webs, '
              'decided; weights natural numbers; a standpoint\'s order represented as an additive weighting, a '
              'representation supplied, not derived.',
        'zh': '不加公理。项（步与构成）的有限列举；接纳取二值（Bool），在依存网上可判定；权重为自然数；立场的序表示为可加的加权，'
              '这一表示是所设而非推出。'}],
    'does_not_show': [
        {'en': 'That a standpoint\'s order is additive or its weights positive, or which weighting a standpoint has.',
         'zh': '立场的序是可加的或其权重为正，或某个立场有哪一个加权。', 'kind': 'scope'},
        {'en': 'That the impartial order is what every standpoint shares rather than one privileged weighting, or that '
               'widening is better: calling widening better is C, a premise.',
         'zh': '不偏的序是所有立场共有者而非某个特许的加权，或扩大是更好的：把扩大称为更好的是 C，是前提。', 'kind': 'non-implication'},
        {'en': 'Graded significance, chance, or magnitude beyond counting listed items; partiality outside mixed '
               'comparisons is not excluded for weightings that are not positive.',
         'zh': '分级的意义、机会，或超出计数所列项的量；对不为正的加权，不排除混合比较之外的偏倚。', 'kind': 'scope'}],
    'counterexamples': [{'path': src(MOD), 'detail': {
        'en': 'For a mixed pair, the weighting giving the items one course admits beyond the other more weight than the '
              'other\'s whole listing (Weighting.outweighing) ranks it higher, and the swapped weighting the other way '
              '(Weighting.mixed_either_way): no positive weighting is forced on a mixed comparison.',
        'zh': '对一对混合的进程，给一条超出另一条所接纳的项以多于另一条整个列举之权重的加权（Weighting.outweighing）把它排得更高，'
              '互换的加权则反过来（Weighting.mixed_either_way）：混合的比较上没有哪个正的加权是被迫的。'}}],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'decidability', 'discrete-steps',
                            'no-definition-by-verdict', 'names-provisional'],
    'validation_scope': VALIDATION,
    'next_delta': {
        'en': 'Graded significance and weights beyond naturals; orders that are not additive (lexical, threshold) and '
              'where they part from the shared order; a base reading of a standpoint\'s weighting from what its '
              'activity keeps; an independent review.',
        'zh': '分级的意义与自然数之外的权重；不可加的序（词典式、阈值式）及其与共有之序分开之处；从立场的活动所维持者读出其加权的'
              '基底读法；独立审查。'},
    'correspondence': {
        'en': 'Sen\'s intersection approach (Collective Choice and Social Welfare, 1970; "On Weights and Measures", '
              '1977): the judgments every weighting in a set shares form a quasi-ordering; any quasi-ordering is an '
              'intersection of orderings (Donaldson and Weymark 1998). In multi-objective optimization, dominance in '
              'every coordinate is ranking by every positive weighted sum, here the finite 0/1 case. The inclusion '
              'order with strict monotonicity on opportunity sets is Pattanaik and Xu (1990). The reading places '
              'Scheffler\'s agent-centred prerogative (1982) and Williams\'s partiality (1976) in exactly the mixed '
              'comparisons, and Taurek\'s question (1977) at the equal weighting.',
        'zh': 'Sen 的交集方法（《集体选择与社会福利》1970；《权重与度量》1977）：一组中每个加权所共有的判断构成拟序；任何拟序都是'
              '若干序的交（Donaldson 与 Weymark 1998）。多目标优化中，在每个坐标上占优即被每个正的加权和排序，此处为有限的 0/1 情形。'
              '机会集上带严格单调的包含序是 Pattanaik 与 Xu（1990）。这一读法把 Scheffler 的行动者中心特权（1982）与 Williams 的'
              '偏倚（1976）恰放在混合的比较里，把 Taurek 的问题（1977）放在同权之处。'},
    'canonical_source': src(MOD),
    'aliases': ['widening as what every weighting ranks', '扩大即每个加权所排者', 'C as the order every weighting shares',
                'partiality decides the mixed comparisons', 'Becoming.Weighting.widens_iff_every_positive',
                'Becoming.Weighting.mixed_either_way', 'Becoming.Web.widens_iff_every_weighting'],
    'dependencies': [
        {'id': 'comparison-by-widening', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses the comparison by widening on webs (Web.Widens, Web.Keeps, Web.Admits).',
                    'zh': '复用依存网上以扩大的比较（Web.Widens、Web.Keeps、Web.Admits）。'},
         'interface': {
             'output': {'en': 'One level path widens another where it admits at every step what the other admits and at '
                              'some step more.',
                        'zh': '一条水平路径扩大另一条，若每步都接纳另一条所接纳者，且某步更多。'},
             'input': {'en': 'Widening as what every positive weighting of the listed admissions ranks higher.',
                       'zh': '扩大即所列接纳的每个正的加权都排得更高者。'},
             'conditions': {'en': 'Admission decided; what either path admits listed.',
                            'zh': '接纳可判定；两条路径所接纳者都已列出。'},
             'evidence': src('Regions')}}],
    'related': [
        {'id': STEP, 'detail': {
            'en': 'The same section\'s scope: what the step of invariance reaches across standpoints.',
            'zh': '同一节中的范围：不变之步跨立场达到哪里。'}},
        {'id': 'protection-priority-excludes-uniform-aggregation', 'detail': {
            'en': 'A priority of basic conditions is a lexical order no natural-number score represents; such an order '
                  'is not one of the weightings here, and it can decide comparisons the shared order leaves mixed.',
            'zh': '基本条件的优先是任何自然数得分都不能表示的词典式序；这样的序不在此处的加权之中，它能决定共有之序留为混合的比较。'}}],
    'references': [{'path': src(MOD), 'role': 'proof', 'declarations': ALL, 'sha256': sha(src(MOD))},
                   {'path': src('Regions'), 'role': 'proof', 'sha256': sha(src('Regions'))}] + COMMON_REFS,
    'proof_bindings': BINDING,
    'history': HISTORY('stating C as the order every positive weighting shares and partiality as the mixed comparisons',
                       '把 C 陈述为每个正的加权所共有的序，把偏倚陈述为混合的比较'),
}

for rec in (rec1, rec2):
    path = check(rec)
for rec in (rec1, rec2):
    (RECORDS / f'{rec["id"]}.json').write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
    print('written', rec['id'])
