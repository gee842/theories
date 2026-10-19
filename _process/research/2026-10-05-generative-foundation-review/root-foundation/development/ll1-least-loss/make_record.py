#!/usr/bin/env python3
"""Write LL1's record least-loss-rest: python3 -B make_record.py CORE_RECEIPT SECTION

The receipt is checked against the current bytes of the sources it binds, and every declaration the record
cites against those Lean elaborated, before anything is written. Run after the study section is in place."""
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/LeastLoss.lean'
DISSIPATION = f'{PKG}/Becoming/Dissipation.lean'
FLOW = f'{PKG}/Becoming/Flow.lean'
SPACE = f'{PKG}/Becoming/Space.lean'
OPENNESS = f'{PKG}/Becoming/Openness.lean'
LOCALITY = f'{PKG}/Becoming/Locality.lean'
RENEWAL = f'{PKG}/Becoming/Renewal.lean'
RECURRENCE = f'{PKG}/Becoming/Recurrence.lean'
BRANCHING = f'{PKG}/Becoming/Branching.lean'
DEV = '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/ll1-least-loss'
AUDIT = f'{DEV}/audit/LeastLossDeps.lean'
AUDIT_LOG = f'{DEV}/audit/deps.log'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
RECORDS = ROOT / 'theories/becoming/results/records'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
core_id, section = sys.argv[1], sys.argv[2]
core_receipt = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


core = json.loads((ROOT / core_receipt).read_text())
assert core['status'] == 'passed'
BOUND = [('Becoming.LeastLoss', SRC), ('Becoming.Dissipation', DISSIPATION), ('Becoming.Flow', FLOW),
         ('Becoming.Space', SPACE), ('Becoming.Renewal', RENEWAL), ('Becoming.Openness', OPENNESS),
         ('Becoming.Locality', LOCALITY), ('Becoming.Recurrence', RECURRENCE),
         ('Becoming.Branching', BRANCHING)]
for module, path in BOUND:
    assert core['source_sha256'][module] == sha(path), ('core receipt does not bind', path)
decls = {d['name'] for m in core['modules'] if m['module'] == 'Becoming.LeastLoss' for d in m['declarations']}
axioms = {n: a for m in core['modules'] if m['module'] == 'Becoming.LeastLoss'
          for n, a in m['axiom_dependencies'].items()}
assert decls and not any(axioms.values())
every = {d['name'] for m in core['modules'] for d in m['declarations']}
log = (ROOT / AUDIT_LOG).read_text()
assert log.count('same statement = true') == 6 and 'NOT FOUND' not in log and '[]' not in log, 'audit log'
STUDY_TEXT = (ROOT / STUDY).read_text()
heading = f'## {section}. The least loss as a premise of rest (LL1)'
assert re.search('^' + re.escape(heading) + '$', STUDY_TEXT, re.M)
ANCHOR = f'#{section}-the-least-loss-as-a-premise-of-rest-ll1'


def c(*names):
    out = ['Becoming.' + n for n in names]
    missing = [n for n in out if n not in decls]
    assert not missing, missing
    return out


def e(*names):
    out = ['Becoming.' + n for n in names]
    missing = [n for n in out if n not in every]
    assert not missing, missing
    return out


laws = [
    {'en': 'Amounts: an addition, associative and commutative with nothing as its unit, and an order that addition '
           'keeps and that cancels, with nothing least; no amount need be a whole number, and the order may be dense. '
           'The order is a preorder, so no quotient is taken.',
     'zh': '量：一个加法，结合、交换，以无为单位；一个加法保持并可消去的序，无为最小。量不必是整数，序可以稠密。'
           '序是预序，所以不取商。',
     'declarations': c('Amounts', 'Amounts.times', 'Amounts.sum', 'Amounts.add_zero', 'Amounts.le_of_eq',
                       'Amounts.add_le_add_left', 'Amounts.le_add_right', 'Amounts.le_add_left', 'Amounts.add_swap',
                       'Amounts.times_le')},
    {'en': 'The loss law: where across each step from T on the amount after the step, with the step\'s loss, is within '
           'the amount before, the losses since T, added, are within the amount at T. No least loss is named; the '
           'losses of a falling stock are summable in any amounts.',
     'zh': '损失律：若自 T 起每一步后的量加上该步的损失不超过步前的量，则自 T 起的损失之和不超过 T 时的量。'
           '不指定最小损失；在任何量中，下降的存量的损失都可求和。',
     'declarations': c('Amounts.losses_within')},
    {'en': 'The least-loss law of rest: where an amount does not rise from T on, falls by at least ε across each step '
           'at which P holds, and m copies of ε are not within its value at T, steps at which P holds do not recur; '
           'with the premises read as far as can be refuted, it is not the case that after every step a later such '
           'step stays unrefuted. The premises are the least loss ε and the bound of the stock by finitely many '
           'copies of it.',
     'zh': '停息的最小损失律：若一个量自 T 起不上升，在 P 成立的每一步至少下降 ε，且 m 份 ε 不在 T 时的量之内，'
           '则 P 成立的步不会反复出现；前提按不可否定来读时，并非每一步之后都有一个不被否定的此类后续步。'
           '前提是最小损失 ε，以及存量被有限份 ε 所界。',
     'declarations': c('Amounts.still_le', 'Amounts.loses_times', 'Amounts.rests_unrefuted', 'Amounts.rests')},
    {'en': 'In Archimedean amounts every amount lies within finitely many copies of any amount above nothing, so a least '
           'loss above nothing alone brings rest.',
     'zh': '在阿基米德的量中，任何量都在任一大于无的量的有限份之内，所以仅有大于无的最小损失就带来停息。',
     'declarations': c('Amounts.Archimedean', 'Amounts.rests_of_archimedean')},
    {'en': 'The approach to rest, with no least loss: where across each step from T on the amount after the step, with '
           'the step\'s loss, is within the amount before, then for any k steps f 0 < f 1 < … from T on, each losing at '
           'least ε, k copies of ε are within the amount at T; so where m copies are not, fewer than m steps lose at '
           'least ε, a bound on the count with no decision. In Archimedean amounts such an m exists for every ε above '
           'nothing: a closed amount comes arbitrarily near rest, and steps losing at least ε do not recur. The '
           'Archimedean property is the one structural premise. In whole numbers approach is rest: no more steps lose '
           'anything than the stock counts.',
     'zh': '趋近停息，无需最小损失：若自 T 起每一步后的量加该步损失不超过步前的量，则自 T 起任意 k 个递增的步 f 0 < f 1 < …，'
           '各至少损失 ε 时，k 份 ε 在 T 时的量之内；所以 m 份不在其内时，至少损失 ε 的步少于 m 个，这是对个数的界，不需判定。'
           '在阿基米德的量中，对每个大于无的 ε 都有这样的 m：封闭的量任意地趋近停息，至少损失 ε 的步不复现。'
           '阿基米德性是唯一的结构前提。在整数中趋近即停息：有所损失的步不多于存量之数。',
     'declarations': c('Amounts.still_within', 'Amounts.still_of_falls', 'Amounts.large_losses_from',
                       'Amounts.large_losses_within', 'Amounts.few_large_losses',
                       'Amounts.few_large_losses_of_archimedean', 'Amounts.approaches_rest',
                       'Amounts.whole_losing_steps')},
    {'en': 'A family at rest in any amounts: where from T on the stock after a step with the uptake is within the stock '
           'before with the replenishment, the replenishment is within the uptake, at each step at which P holds the '
           'replenishment with ε is, and the stock at T lies within fewer than m copies of ε, steps at which P holds '
           'do not recur.',
     'zh': '任何量中的家族停息：若自 T 起，一步后的存量加取用不超过步前的存量加补给，补给不超过取用，'
           '在 P 成立的每一步补给加 ε 不超过取用，且 T 时的存量少于 m 份 ε，则 P 成立的步不会反复出现。',
     'declarations': c('Amounts.family_still', 'Amounts.family_loses', 'Amounts.family_rests',
                       'Amounts.family_rests_of_archimedean')},
    {'en': 'Whole numbers are the instance: the least loss is one and every stock lies within its own count of ones '
           'plus one, and whole numbers are Archimedean. From the law, the spine\'s two descents falls_not_recurring '
           'and falls_stop_unrefuted, Flow.taking_not_recurring_from, Flow.takers_within_on, '
           'Flow.change_stops_unrefuted and the rest theorem World.rests_unrefuted_enclosed are proved again with '
           'their statements unchanged.',
     'zh': '整数是其实例：最小损失为一，每个存量都在其自身个数加一份一之内，整数是阿基米德的。'
           '由此律重新证明脊柱的两个下降 falls_not_recurring 与 falls_stop_unrefuted、Flow.taking_not_recurring_from、'
           'Flow.takers_within_on、Flow.change_stops_unrefuted 以及停息定理 World.rests_unrefuted_enclosed，陈述不变。',
     'declarations': c('Amounts.whole', 'Amounts.whole_times_one', 'Amounts.whole_within', 'Amounts.whole_archimedean',
                       'Amounts.whole_sum',
                       'whole_falls_not_recurring', 'whole_falls_stop_unrefuted', 'Flow.taking_not_recurring_whole',
                       'Flow.takers_within_on_whole', 'Flow.change_stops_unrefuted_whole',
                       'World.rests_unrefuted_enclosed_whole')},
    {'en': 'Without a least loss: dyadic amounts are dense, every amount above nothing having its half below it and '
           'above nothing, and Archimedean; a stock halving in them at every step loses at every step, no amount above '
           'nothing is within every loss, and it never rests.',
     'zh': '没有最小损失：二进分数的量是稠密的（任何大于无的量都有其一半在其下且大于无），并且是阿基米德的；'
           '在其中每步减半的存量每步都有损失，没有大于无的量在每个损失之内，它从不停息。',
     'declarations': c('Dyadic', 'Dyadic.mul_assoc\'', 'Dyadic.right_distrib\'',
                       'Dyadic.mul_right_comm\'', 'Dyadic.mul_left_comm\'', 'Dyadic.pow_add\'', 'Dyadic.ext\'',
                       'Dyadic.add', 'Dyadic.le', 'Dyadic.zero', 'Dyadic.le_trans\'', 'Dyadic.add_assoc\'',
                       'Dyadic.add_comm\'', 'Dyadic.zero_add\'', 'Dyadic.expand', 'Dyadic.add_le_add_right\'',
                       'Dyadic.le_of_add_le_add_right\'', 'Dyadic.zero_le\'', 'Dyadic.amounts', 'Dyadic.num_pos',
                       'Dyadic.half_below', 'Dyadic.times_ge', 'Dyadic.archimedean', 'Halving.stock', 'Halving.loss',
                       'Halving.falls', 'Halving.loss_positive', 'Halving.no_least_loss', 'Halving.falls_strictly',
                       'Halving.never_rests', 'Halving.approaches_without_reaching')},
    {'en': 'Without the bound by least losses: in layered amounts, a coarse dyadic layer and a fine whole-number layer '
           'counting only where the coarse layers agree, a stock falls by a least loss of one fine unit at every step, '
           'lies beyond every multiple of it, and never rests.',
     'zh': '没有被最小损失所界：在分层的量中（粗层为二进分数，细层为整数，仅在粗层相互不超过时才计），'
           '存量每步至少下降一个细单位的最小损失，处于其每一倍数之上，从不停息。',
     'declarations': c('Layered', 'Layered.ext\'', 'Layered.add', 'Layered.le',
                       'Layered.zero', 'Layered.le_trans\'', 'Layered.add_le_add_right\'',
                       'Layered.le_of_add_le_add_right\'', 'Layered.amounts', 'Layered.stock', 'Layered.least',
                       'Layered.least_positive', 'Layered.loses', 'Layered.times_coarse',
                       'Layered.beyond_every_multiple', 'Layered.never_rests', 'Layered.not_archimedean')},
    {'en': 'Rest and return: over finitely many configurations a law that merges nothing returns every configuration, '
           'so an amount that does not rise along an orbit is at its start within its value at every step, and where it '
           'falls by a loss at each step every loss is nothing. A loss above nothing needs a law that merges: the least '
           'loss on which rest turns is a premise of descriptions that lump configurations and dissipate, and a finite '
           'law that merges nothing returns rather than rests.',
     'zh': '停息与回返：在有限多个构形上，不合并任何东西的规律使每个构形回返，所以沿轨道不上升的量在起点不超过其每一步的值；'
           '若它每步以一个损失下降，则每个损失都为无。大于无的损失需要有所合并的规律：停息所依的最小损失是归并构形而耗散的描述的前提，'
           '不合并任何东西的有限规律回返而不停息。',
     'declarations': c('Law.Lossless.regains', 'Law.Lossless.loses_nothing', 'Law.loss_needs_merge',
                       'Branching.Lossless.loses_nothing', 'Branching.loss_needs_merge')},
]
listed = {d for law in laws for d in law['declarations']}
extra = {d for d in decls if d not in listed}
assert not (listed - decls), sorted(listed - decls)
assert all(re.search(r'\.(mk|rec|recOn|casesOn|noConfusion|noConfusionType|brecOn|below|binductionOn|ibelow|'
                     r'mk\.inj|mk\.injEq|mk\.sizeOf_spec|sizeOf_spec|match_\d+|proof_\d+|_sizeOf_\d+|_sizeOf_inst|'
                     r'eq_\d+|ctorIdx)$', d) or '.match_' in d or '._' in d or d.endswith('.inj') or d.endswith('.injEq')
           for d in extra), sorted(extra)

record = {
    'schema_version': 2,
    'id': 'least-loss-rest',
    'title': {'en': 'The least loss as a premise of rest', 'zh': '最小损失作为停息的前提'},
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': json.loads((RECORDS / 'rest-at-every-resolution.json').read_text())['family'],
    'reviewed_at_utc': NOW,
    'statement': {
        'en': 'In Archimedean amounts a closed amount approaches rest with no least loss: few steps lose at least any ε '
              'above nothing. Rest needs a least loss at each change counted: halving approaches rest and never reaches '
              'it. Whole numbers are the instance with ε one; a loss needs a law that merges.',
        'zh': '在阿基米德的量中，封闭的量无需最小损失即趋近停息：至少损失任一大于无的 ε 的步只有有限个。'
              '停息需要每次被计的变化有最小损失：减半趋近停息而达不到。整数是 ε 为一的实例；损失需要有所合并的规律。'},
    'laws': laws,
    'hypotheses': [
        {'en': 'No axiom. The least loss ε at each step at which P holds and the bound of the stock at T by m copies of ε '
               'are hypotheses of Amounts.rests, Amounts.rests_unrefuted and Amounts.family_rests; in Archimedean '
               'amounts the bound follows from ε above nothing, and the approach law asks only the Archimedean '
               'property. The amounts\' eleven laws are the fields of Amounts; '
               'antisymmetry, totality and decidability of the order are not asked.',
         'zh': '无公理。P 成立的每一步的最小损失 ε，以及 T 时存量被 m 份 ε 所界，是 Amounts.rests、Amounts.rests_unrefuted '
               '与 Amounts.family_rests 的假设；在阿基米德的量中，界由 ε 大于无得出，趋近之律只要求阿基米德性。量的十一条规律是 Amounts 的字段；'
               '不要求序的反对称、全序或可判定。'},
    ],
    'does_not_show': [
        {'en': 'Flow, Web and World with levels in any amounts: the step the rest laws turn on is stated for any amounts, '
               'not those structures over any amounts.',
         'zh': 'Flow、Web 与 World 以任何量为水平：停息规律所依赖的那一步对任何量陈述，那些结构本身并未在任何量上重述。',
         'kind': 'scope'},
        {'en': 'That any physical system has a least loss per change; the statistical second law names none, and which '
               'physical premises supply one is stated, as a correspondence, in least-loss-from-entropy-production (T1).',
         'zh': '任何物理系统每次变化有最小损失；统计意义上的第二定律不给出它，哪些物理前提给出它，作为对应，见 least-loss-from-entropy-production（T1）。',
         'kind': 'scope'},
        {'en': 'Real numbers; dyadic amounts witness density in the core, and the reals are not constructed.',
         'zh': '实数；二进分数的量在核心中见证稠密，实数并未构造。', 'kind': 'scope'},
        {'en': 'That coming to rest supports or damages 生生.',
         'zh': '停息支持或损害生生。', 'kind': 'non-implication'},
    ],
    'counterexamples': [
        {'path': SRC, 'detail': {
            'en': 'Halving.never_rests: dense, Archimedean dyadic amounts, every loss above nothing and no least loss, '
                  'the stock falling at every step.',
            'zh': 'Halving.never_rests：稠密且阿基米德的二进分数量，每个损失都大于无而无最小损失，存量每步都下降。'}},
        {'path': SRC, 'detail': {
            'en': 'Layered.never_rests: a least loss at every step, the stock beyond every multiple of it, falling at '
                  'every step; the amounts are not Archimedean (Layered.not_archimedean), so approach fails too.',
            'zh': 'Layered.never_rests：每步都有最小损失，存量处于其每一倍数之上，每步都下降；这些量不是阿基米德的'
                  '（Layered.not_archimedean），所以趋近也不成立。'}},
        {'path': SRC, 'detail': {
            'en': 'Halving.approaches_without_reaching: the halving stock approaches rest, few steps losing at least any ε '
                  'above nothing, and falls at every step, as exponential relaxation does.',
            'zh': 'Halving.approaches_without_reaching：减半的存量趋近停息，至少损失任一大于无的 ε 的步只有有限个，'
                  '而每步都下降，如指数弛豫。'}},
    ],
    'standard_boundaries': ['discrete-steps', 'no-ethical-premise', 'no-evaluation', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {len(decls)} '
              f'declarations of Becoming.LeastLoss have empty axiom reports; the checker verifies core purity. A '
              f'dependency audit (audit/LeastLossDeps.lean in the development folder) finds every one of 15 named rest '
              f'laws reaching falls_not_recurring or falls_stop_unrefuted, and the six whole-number restatements '
              f'with Lean types identical to the theorems they restate. Author self-review in study section {section}; '
              f'not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.LeastLoss 的 {len(decls)} 项声明公理报告为空；'
              f'检查器并核对核心纯净。依赖审计（开发目录中的 audit/LeastLossDeps.lean）表明所列 15 条停息规律都经过 '
              f'falls_not_recurring 或 falls_stop_unrefuted，六个整数重述的 Lean 类型与所重述的定理相同。'
              f'作者自审见研究第 {section} 节；未经独立审查。'},
    'next_delta': {
        'en': 'Flow and World with levels in any amounts, restating the rest family there with the least loss as the '
              'premise of dissipation; a least loss that holds only in expectation over amounts that may be dense; an '
              'independent review.',
        'zh': '以任何量为水平的 Flow 与 World，在其中以最小损失为耗散的前提重述停息族；在可稠密的量上只在期望中成立的最小损失；'
              '独立审查。'},
    'correspondence': {
        'en': 'The outside review of 19 October 2026 (R20) and an outside reader named the rest laws\' dependence on '
              'whole-number amounts as the main gap between the spine and our universe: with real-valued amounts losses '
              'can shrink geometrically. Reading (the AI\'s): what the whole numbers carry is a floor on the cost of '
              'each change counted, and the stock\'s being finitely many floors deep; where change has no floor a closed '
              'system can change ever more slightly for ever without exhausting what it has.',
        'zh': '2026年10月19日的外部审查（R20）与一位外部读者指出，停息规律依赖整数的量，是脊柱与我们宇宙之间的主要差距：'
              '若量取实数，损失可以几何地缩小。读法（AI 的）：整数所承载的是每次被计的变化的代价有一个下限，'
              '且存量只有有限个下限之深；变化没有下限之处，封闭系统可以无尽地越来越微小地变化，而不耗尽其所有。'},
    'canonical_source': SRC,
    'aliases': ['least loss', '最小损失', 'approach to rest', '趋近停息', 'exponential relaxation', '指数弛豫', 'rest over dense amounts', '可稠密的量上的停息', 'geometric loss never rests',
                '几何损失不停息', 'Becoming.Amounts.rests', 'Becoming.Amounts.rests_unrefuted',
                'Becoming.Amounts.family_rests', 'Becoming.Halving.never_rests', 'Becoming.Layered.never_rests',
                'Becoming.Amounts.approaches_rest', 'Becoming.Law.loss_needs_merge'],
    'dependencies': [
        {'id': 'no-finite-part-bears-taking', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Flow.DissipatesOn and Flow.DissipatesOn.replenishment_takers to restate '
                          'Flow.taking_not_recurring_from as the family law at whole-number amounts.',
                    'zh': '复用 Flow.DissipatesOn 与 Flow.DissipatesOn.replenishment_takers，把 '
                          'Flow.taking_not_recurring_from 重述为整数量上的家族律。'},
         'interface': {'output': {'en': 'Dissipated on, a family\'s replenishment with its takers is within its uptake.',
                                  'zh': '被耗散时，家族的补给加取用者数不超过其取用。'},
                       'input': {'en': 'At whole-number amounts, the replenishment within the uptake, and with a least '
                                       'loss of one at each taking step.',
                                 'zh': '在整数量上，补给不超过取用，在每个取用步补给加最小损失一不超过取用。'},
                       'conditions': {'en': 'Balance on the family and dissipation from T on.',
                                      'zh': '自 T 起家族上的平衡与耗散。'},
                       'evidence': DISSIPATION}},
        {'id': 'continued-change-needs-openness', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses what stands running down (Flow.RunsDown.standing_le, Flow.RunsDown.changes_iff), the '
                          'census of what stands and enclosure around it to prove Flow.change_stops_unrefuted and '
                          'World.rests_unrefuted_enclosed again from the least-loss law, statements unchanged.',
                    'zh': '复用所立者的下降（Flow.RunsDown.standing_le、Flow.RunsDown.changes_iff）、所立者的普查与围住它的步，'
                          '由最小损失律重新证明 Flow.change_stops_unrefuted 与 World.rests_unrefuted_enclosed，陈述不变。'}},
        {'id': 'space-and-its-parts', 'relation': 'formal-reuse',
         'detail': {'en': 'States falls_stop_unrefuted, the descent of the world-level rest laws, as the least-loss law '
                          'at whole-number amounts with its statement unchanged.',
                    'zh': '把世界层停息规律所用的下降 falls_stop_unrefuted 陈述为整数量上的最小损失律，陈述不变。'}},
    ],
    'related': [
        {'id': 'least-loss-from-entropy-production',
         'detail': {'en': 'There the physical premises that give the spine\'s least loss are stated (periphery '
                          'EntropyProduction, a stated correspondence); here the least loss is the exact premise of rest '
                          'over amounts that may be dense, and approach to rest needs none.',
                    'zh': '那里陈述给出脊柱最小损失的物理前提（外围 EntropyProduction，一种陈述的对应）；'
                          '这里最小损失是可稠密之量上停息的确切前提，而趋近停息不需要它。'}},
        {'id': 'recurrence-without-premise',
         'detail': {'en': 'There a law that merges nothing returns every configuration within finitely many; here that '
                          'return makes every loss along an orbit nothing, so the least loss of the rest laws needs a '
                          'law that merges (Law.Lossless.loses_nothing, Law.loss_needs_merge).',
                    'zh': '那里不合并任何东西的规律在有限多个构形中使每个构形回返；这里这一回返使沿轨道的每个损失都为无，'
                          '所以停息规律的最小损失需要有所合并的规律（Law.Lossless.loses_nothing、Law.loss_needs_merge）。'}},
        {'id': 'rest-at-every-resolution',
         'detail': {'en': 'There the unit may split and the same boundary is read at a refining unit (Asymptote, Dwindle); '
                          'here amounts have no unit and the least loss is a premise.',
                    'zh': '那里单位可以细分，同一边界在细分的单位下被读出（Asymptote、Dwindle）；这里量没有单位，最小损失是前提。'}},
        {'id': 'rest-with-refinement-counted',
         'detail': {'en': 'There counting the refinement brings rest at every resolution with no premise added; here the '
                          'premise whole numbers supplied is named for amounts with no unit.',
                    'zh': '那里把细分算入，不添前提就在每一分辨率下带来停息；这里为无单位的量指明整数所供给的前提。'}},
    ],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted(listed), 'sha256': sha(SRC)},
        {'path': core_receipt, 'role': 'receipt', 'declarations': [], 'sha256': sha(core_receipt)},
        {'path': DISSIPATION, 'role': 'proof',
         'declarations': e('Flow.DissipatesOn', 'Flow.DissipatesOn.replenishment_takers',
                           'Flow.BalancesOn.runs_down', 'Flow.takers_within_on',
                           'Flow.taking_not_recurring_from'), 'sha256': sha(DISSIPATION)},
        {'path': OPENNESS, 'role': 'proof',
         'declarations': e('Flow.change_stops_unrefuted', 'Flow.Enclosed.aroundStanding_not_not',
                           'Flow.AroundStanding.runsDownClosed', 'World.standingCensus', 'World.rises_of_arises',
                           'World.falls_of_ceases', 'World.rests_unrefuted_enclosed'), 'sha256': sha(OPENNESS)},
        {'path': LOCALITY, 'role': 'proof',
         'declarations': e('Flow.RunsDown', 'Flow.RunsDown.standing_le', 'Flow.RunsDown.changes_iff',
                           'Flow.RunsDownClosed.runsDown'), 'sha256': sha(LOCALITY)},
        {'path': FLOW, 'role': 'proof', 'declarations': e('Flow.BalancesOn', 'Flow.BalancesOn.over'),
         'sha256': sha(FLOW)},
        {'path': SPACE, 'role': 'proof', 'declarations': e('falls_stop_unrefuted'), 'sha256': sha(SPACE)},
        {'path': RENEWAL, 'role': 'proof', 'declarations': e('falls_not_recurring'), 'sha256': sha(RENEWAL)},
        {'path': RECURRENCE, 'role': 'proof',
         'declarations': e('Law.orbit', 'Law.orbit_mul', 'Law.Lossless', 'Law.Returns', 'Law.Lossless.returns'),
         'sha256': sha(RECURRENCE)},
        {'path': BRANCHING, 'role': 'proof',
         'declarations': e('Branching.Lossless', 'Branching.Lossless.recurs', 'Branching.law_lossless_iff'),
         'sha256': sha(BRANCHING)},
        {'path': AUDIT, 'role': 'review', 'declarations': [], 'sha256': sha(AUDIT)},
        {'path': AUDIT_LOG, 'role': 'review', 'declarations': [], 'sha256': sha(AUDIT_LOG)},
        {'path': STUDY, 'role': 'integration', 'declarations': [], 'sha256': sha(STUDY)},
        {'path': CHAPTER, 'role': 'statement', 'declarations': [], 'sha256': sha(CHAPTER)},
    ],
    'proof_bindings': [
        {'source': p, 'receipt': core_receipt, 'sha256_pointer': f'/source_sha256/{m}',
         'success_pointer': '/status', 'success_value': 'passed'}
        for m, p in BOUND
    ],
    'history': [
        {'en': f'19 October 2026: added (LL1), after the outside review of 19 October (R20) named the rest laws\' '
               f'dependence on whole-number amounts; study section {section}.',
         'zh': f'2026年10月19日：新增（LL1），在 10 月 19 日的外部审查（R20）指出停息规律依赖整数的量之后；研究第 {section} 节。'},
    ],
}
for item in (record['statement'],):
    assert len(item['en']) <= 300 and len(item['zh']) <= 150, (len(item['en']), len(item['zh']))
(RECORDS / 'least-loss-rest.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print('written', len(listed), 'cited of', len(decls), 'declarations')
