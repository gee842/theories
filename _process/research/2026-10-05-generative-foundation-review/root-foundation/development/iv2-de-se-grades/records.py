#!/usr/bin/env python3
"""IV2's records: what-the-step-across-standpoints-reaches gains the de se laws and the web reading of what the step
forces; widening-as-what-every-weighting-ranks is rebound (its module grew; its laws are unchanged); the new record
graded-significance-and-priority. Each changed record gets a history note.
python3 -B records.py CORE_RECEIPT STUDY_SECTION   (from the checkout root, after land_text.py)"""
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
HEAD = f'## {N}. The de se question and graded significance (IV2)'
assert re.search('^' + re.escape(HEAD) + '$', (ROOT / STUDY).read_text(), re.M)


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def src(mod):
    return f'{PKG}/Becoming/{mod}.lean'


m = next(m for m in core['modules'] if m['module'] == f'Becoming.{MOD}')
assert core['source_sha256'][f'Becoming.{MOD}'] == sha(src(MOD)), 'receipt does not bind'
assert not any(m['axiom_dependencies'].values())
FULL = [d['name'] for d in m['declarations']]
ALL = sorted(FULL)
n_decl, n_thm = len(m['declarations']), sum(1 for d in m['declarations'] if d.get('kind') == 'theorem')


def resolve(names):
    out = []
    for n in names:
        hits = [f for f in FULL if f == 'Becoming.' + n or f.endswith('.' + n)]
        assert len(hits) == 1, (n, hits)
        out.append(hits[0])
    return out


def rebind(rec, history_en, history_zh):
    for ref in rec['references']:
        if ref['path'] == src(MOD):
            ref['declarations'] = ALL
        if ref['role'] == 'receipt':
            ref['path'] = RECEIPT
        ref['sha256'] = sha(ref['path'])
    for b in rec['proof_bindings']:
        b['receipt'] = RECEIPT
    rec['validation_scope'] = VALIDATION
    rec['reviewed_at_utc'] = NOW
    rec['history'].append({'en': history_en, 'zh': history_zh})


VALIDATION = {
    'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {n_decl} declarations of '
          f'Becoming.{MOD}, {n_thm} of them theorems, have empty axiom reports; the checker verifies core purity. The '
          'literature checks before any Lean are sections of the significance review; the argument is the chapter '
          f'THE-STEP-OF-INVARIANCE. Built and reviewed in one session, no separate reviewer; author review in study '
          f'sections 256 and {N}; not independently reviewed by a person.',
    'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.{MOD} 的 {n_decl} 项声明（{n_thm} 项定理）公理报告为空；'
          '检查器并核对核心纯净。动手写 Lean 之前的文献核查是显著性审查中的两节；论证见章节 THE-STEP-OF-INVARIANCE。'
          f'在一个会话中构建并审查，没有另设审查者；作者审查见研究第 256 与 {N} 节；未经人的独立审查。'}

# Record 1.
p1 = RECORDS / 'what-the-step-across-standpoints-reaches.json'
r1 = json.loads(p1.read_text())
new_laws = [
    ('A content held de se is a property each standpoint ascribes to its own center; one held de dicto is one '
     'proposition from every standpoint. Standpoint-invariance is exactly holding one shared content, and a content '
     'held de se is invariant exactly where its readings at the centers agree.',
     '从己地持有的内容是每个立场归于其自身中心的性质；从言地持有的内容是从每个立场看都相同的一个命题。对立场不变恰是持有一个'
     '共有的内容；从己的内容恰在其于诸中心的读出一致处不变。',
     ['selfAscribed', 'shared', 'shared_standpointInvariant', 'standpointInvariant_iff_shared',
      'selfAscribed_standpointInvariant_iff']),
    ('Held de se, the presupposition about the own closure along a relation meets every standpoint\'s presupposition, '
     'is standpoint-invariant exactly where the centers\' closures agree, and is the continuation condition exactly '
     'where every center\'s closure is the whole, with no step.',
     '从己地持有，关于沿一个关系的自身闭包的预设满足每个立场的预设，恰在诸中心的闭包一致处对立场不变，恰在每个中心的闭包都是'
     '整体处是延续条件，无需那一步。',
     ['ownClosure', 'ownClosure_presupposed', 'ownClosure_standpointInvariant_iff', 'ownClosure_unrestricted_iff',
      'ownClosure_unrestricted_of_whole']),
    ('Held de dicto, what each standpoint\'s presupposition at its center\'s closure and standpoint-invariance force '
     'is exactly the union of the closures; on a web, admitting what the step forces is admitting every center, or '
     'the union along a relation.',
     '从言地持有，各立场在其中心闭包处的预设与对立场不变所迫使者恰是诸闭包之并；在依存网上，接纳那一步所迫使者，即接纳每个中心，'
     '或沿一个关系的并。',
     ['withinSome', 'forced_iff_within_some', 'Web.admitsWithin_forced_iff',
      'Web.admitsWithin_forced_within_some_iff']),
    ('The de se and de dicto readings give significance alike from every standpoint exactly where whatever lies within '
     'one center\'s closure lies within every center\'s. Witness: two standpoints, each its own center along the empty '
     'relation, where they part.',
     '从己与从言的读法恰在凡位于一个中心闭包之内者都位于每个中心闭包之内处，从每个立场给出相同的意义。见证：沿空关系、各自为中心的'
     '两个立场，两种读法在此分开。',
     ['selfAscribed_iff_withinSome', 'Divided.not_within', 'Divided.selfAscribed_not_invariant',
      'Divided.withinSome_both']),
]
for en, zh, names in new_laws:
    assert len(en) <= 420 and len(zh) <= 190, (en[:40], len(en), len(zh))
    r1['laws'].append({'en': en, 'zh': zh, 'declarations': resolve(names)})
dns = r1['does_not_show'][0]
assert dns['en'].startswith('The step of invariance itself')
dns['en'] = ('The step of invariance itself, or the self\'s presupposition: both are hypotheses. Whether the '
             'presupposition is held de se of a self drawn along a relation narrower than being related at all is open.')
dns['zh'] = '不变之步本身，或自我的预设：二者都是假设。预设是否以从己的方式、关于沿比“有所关联”更窄的关系所画的自我而持有，仍未定。'
assert len(dns['en']) <= 240 and len(dns['zh']) <= 110, (len(dns['en']), len(dns['zh']))
r1['next_delta'] = {
    'en': 'An argument on the exact de se question (de se of a self drawn along a privileged relation narrower than '
          'being related at all); which formations are centers on the base; an independent philosophical review.',
    'zh': '对确切的从己问题的论证（关于沿比“有所关联”更窄的特许关系所画之自我的从己预设）；在基底上哪些构成是中心；独立的哲学审查。'}
r1['aliases'] += ['the de se question', 'de se and de dicto presupposition', 'Becoming.selfAscribed_iff_withinSome',
                  'Becoming.forced_iff_within_some']
rebind(r1, f'20 October 2026 (IV2): four laws added, the de se and de dicto readings of the presupposition and where '
           f'they part, and the web reading of what the step forces (Web.admitsWithin_forced_iff, which puts '
           f'forced_iff_center on the base); the first non-implication restated in the exact form of the de se '
           f'question; rebound to receipt {core_id}; readings D60; study section {N}.',
       f'2026年10月20日（IV2）：新增四条规律，即预设的从己与从言读法及其分开之处，以及那一步所迫使者在依存网上的读法'
       f'（Web.admitsWithin_forced_iff，使 forced_iff_center 落在基底上）；第一条“不表明”改述为从己问题的确切形式；改绑到回执 '
       f'{core_id}；读法 D60；研究第 {N} 节。')
p1.write_text(json.dumps(r1, ensure_ascii=False, indent=2) + '\n')

# Record 2.
p2 = RECORDS / 'widening-as-what-every-weighting-ranks.json'
r2 = json.loads(p2.read_text())
rebind(r2, f'20 October 2026 (IV2): the module grew (grades, levels, priority, sufficiency; record '
           f'graded-significance-and-priority); this record\'s laws and declarations are unchanged; rebound to receipt '
           f'{core_id}; study section {N}.',
       f'2026年10月20日（IV2）：模块扩充（等级、层级、优先、充足；记录 graded-significance-and-priority）；本记录的规律与声明不变；'
       f'改绑到回执 {core_id}；研究第 {N} 节。')
p2.write_text(json.dumps(r2, ensure_ascii=False, indent=2) + '\n')

# Record 3.
W = 'Weighting.'
laws = [
    ('A graded significance gives each listed item a natural grade from each standpoint; its standing is whether the '
     'grade is positive. Invariant grades give invariant standing and rank alike from every standpoint.',
     '分级的意义从每个立场给每个所列项一个自然数等级；其“是否算数”即等级是否为正。等级不变则“是否算数”不变，且从每个立场排序相同。',
     [W + 'GradeInvariant', W + 'StandingInvariant', W + 'standingInvariant_of_gradeInvariant',
      W + 'weighed_eq_of_gradeInvariant', W + 'ranks_alike_of_gradeInvariant']),
    ('Witness: two standpoints grading their own formation two and the other one. Standing is invariant, grades are '
     'not, and the two standpoints rank a mixed comparison opposite ways.',
     '见证：两个立场把自己的构成评为二、另一个评为一。“是否算数”不变，等级不变不成立，两个立场对一个混合比较的排序相反。',
     ['Partial.grade', 'Partial.standing', 'Partial.not_gradeInvariant', 'Partial.ranks_differ']),
    ('A formation\'s level in a course is how many of its listed items the course admits. Inclusion never lowers a '
     'level, and a sum of a strictly increasing transform of the listed formations\' levels ranks every widening '
     'higher where every item belongs to a listed formation.',
     '一个构成在一条进程中的层级，是该进程所接纳的它的所列项之数。包含从不降低层级；每项都属于某个所列构成时，所列构成层级的严格递增'
     '变换之和把每个扩大都排得更高。',
     [W + 'level', W + 'level_le_of_includes', W + 'level_lt_of_includes_at', W + 'prior', W + 'prior_lt_of_widens']),
    ('A transform strictly concave up to a bound ranks higher a course that moves one step of continuation from a '
     'formation at a higher level to one at a lower, every other level the same; no whole-number transform is '
     'strictly concave everywhere.',
     '直到某个界都严格凹的变换，把从较高层级的构成向较低层级的构成移动一步延续、其余层级不变的进程排得更高；没有整数变换在全域严格凹。',
     [W + 'ConcaveTo', W + 'concave_gap', W + 'prior_transfer']),
    ('A transform that rises no further from a threshold weighs alike two courses whose levels differ only at or '
     'above it.',
     '从某阈值起不再上升的变换，对层级只在阈值及其之上不同的两条进程给出相同的权衡。',
     [W + 'SufficientAt', W + 'sufficient_ties']),
    ('Witness: two formations over three steps, continuing two and two in one course and three and one in the other. '
     'The comparison is mixed; a concave transform ranks the even course higher, through the general law as well; '
     'the sum of levels ties them; a convex transform ranks the uneven course higher.',
     '见证：两个构成、三步，一条进程中各延续二与二，另一条中三与一。比较是混合的；凹变换把均匀的进程排得更高，经一般规律亦然；'
     '层级之和持平；凸变换把不均匀的进程排得更高。',
     ['LevelTransfer.mixed', 'LevelTransfer.concave_to', 'LevelTransfer.by_law', 'LevelTransfer.decided']),
]
for en, zh, _ in laws:
    assert len(en) <= 420 and len(zh) <= 190, (en[:40], len(en), len(zh))
RID = 'graded-significance-and-priority'
rec = {
    'schema_version': 2, 'id': RID,
    'title': {'en': 'Graded significance and priority', 'zh': '分级的意义与优先'},
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F07', 'reviewed_at_utc': NOW,
    'statement': {
        'en': 'Invariant grades give invariant standing, not conversely. On levels of continuation, a strictly '
              'increasing transform ranks every widening higher, one strictly concave up to a bound decides transfers '
              'C leaves mixed, and a threshold of sufficiency ties above it.',
        'zh': '等级不变则“是否算数”不变，反之不然。在延续的层级上，严格递增的变换把每个扩大排得更高，直到某界严格凹的变换决定 C 留为混合的转移，'
              '充足的阈值在其之上持平。'},
    'laws': [{'en': en, 'zh': zh, 'declarations': resolve(names)} for en, zh, names in laws],
    'hypotheses': [{
        'en': 'No axiom. Finite listings of items (steps and formations), each item belonging to a listed formation '
              'where stated; two-valued admission; natural grades and natural-valued transforms; strict concavity up '
              'to a bound; levels as listed items admitted.',
        'zh': '不加公理。项（步与构成）的有限列举，所述之处每项属于某个所列构成；接纳取二值；自然数等级与取自然数值的变换；直到某界的严格凹性；'
              '层级为所接纳的所列项之数。'}],
    'does_not_show': [
        {'en': 'That status is invariant across standpoints, or equal: the step as argued gives standing only.',
         'zh': '地位（算多少）跨立场不变或相等：如所论证的那一步只给出“是否算数”。', 'kind': 'non-implication'},
        {'en': 'That priority, sufficiency or equal counting is right: each decides only what C leaves mixed, and which '
               'decides is not settled.',
         'zh': '优先、充足或同等计数是对的：每一种只决定 C 留为混合者，哪一种来决定未定。', 'kind': 'non-implication'},
        {'en': 'Well-being beyond the length of admitted continuation, lexical priority, or constraints on acts '
               'rather than outcomes.',
         'zh': '超出所接纳延续之长度的福祉、词典式优先，或对行为而非结果的约束。', 'kind': 'scope'}],
    'counterexamples': [{'path': src(MOD), 'detail': {
        'en': 'Partial: standing invariant, grades not, and two standpoints ranking a mixed comparison opposite ways '
              '(Partial.ranks_differ). LevelTransfer: a mixed comparison the sum of levels ties and concave and convex '
              'transforms rank opposite ways (LevelTransfer.decided).',
        'zh': 'Partial：“是否算数”不变而等级不然，两个立场对一个混合比较排序相反（Partial.ranks_differ）。LevelTransfer：层级之和持平、'
              '凹与凸变换排序相反的混合比较（LevelTransfer.decided）。'}}],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'no-definition-by-verdict',
                            'names-provisional', 'formal-not-empirical'],
    'validation_scope': VALIDATION,
    'next_delta': {
        'en': 'Well-being beyond the length of continuation; leximin and its relation to bounded concavity; act '
              'constraints as de se rankings of outcomes; an independent review.',
        'zh': '超出延续长度的福祉；leximin 及其与有界凹性的关系；作为结果之从己排序的行为约束；独立审查。'},
    'correspondence': {
        'en': 'Standing and status are Kagan\'s and Sebo\'s distinction (How to Count Animals, more or less, 2019; '
              'McMahan 2002 on graded status). Priority is Parfit\'s ("Equality and Priority", 1997): a sum of a strictly '
              'increasing, strictly concave transform, satisfying Pareto (prior_lt_of_widens) and Pigou-Dalton '
              '(prior_transfer). Sufficiency is Frankfurt\'s (1987) and Crisp\'s (2003); sufficient_ties is Casal\'s '
              'negative thesis (2007). The theory reads well-being as the length of admitted continuation, and '
              'sufficiency as a scope denial above its threshold.',
        'zh': '“是否算数”与“算多少”是 Kagan 与 Sebo 的区分（《如何或多或少地计数动物》2019；McMahan 2002 论分级地位）。优先是 Parfit 的'
              '（《平等与优先》1997）：严格递增、严格凹之变换的和，满足 Pareto（prior_lt_of_widens）与 Pigou-Dalton（prior_transfer）。'
              '充足是 Frankfurt（1987）与 Crisp（2003）的；sufficient_ties 即 Casal 的否定命题（2007）。本理论把福祉读作所接纳延续的长度，'
              '把充足读作阈值之上对范围的否认。'},
    'canonical_source': src(MOD),
    'aliases': ['graded significance and priority', '分级的意义与优先', 'standing and status', 'prioritarianism on levels',
                'sufficiency as a scope denial', 'Becoming.Weighting.prior_transfer', 'Becoming.Weighting.prior_lt_of_widens',
                'Becoming.Weighting.ranks_alike_of_gradeInvariant'],
    'dependencies': [
        {'id': 'widening-as-what-every-weighting-ranks', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses the weighted count, inclusion and widening on listed items (Weighting.weighed, '
                          'IncludesOn, WidensOn, weighed_le_of_includes).',
                    'zh': '复用所列项上的加权计数、包含与扩大（Weighting.weighed、IncludesOn、WidensOn、weighed_le_of_includes）。'},
         'interface': {
             'output': {'en': 'Inclusion never lowers a weighted count, whatever the weights.',
                        'zh': '包含从不降低加权计数，不论权重如何。'},
             'input': {'en': 'Levels as weighted counts of a formation\'s items; priority as a sum over them.',
                       'zh': '层级即一个构成之项的加权计数；优先即其上的和。'},
             'conditions': {'en': 'None.', 'zh': '无。'},
             'evidence': src(MOD)}}],
    'related': [
        {'id': 'protection-priority-excludes-uniform-aggregation', 'detail': {
            'en': 'Lexical priority of basic conditions is no natural-number score; priority on levels here is.',
            'zh': '基本条件的词典式优先不是自然数得分；此处层级上的优先是。'}},
        {'id': 'what-the-step-across-standpoints-reaches', 'detail': {
            'en': 'The step across standpoints, two-valued, makes standing invariant; status is a further premise.',
            'zh': '二值的跨立场之步使“是否算数”不变；“算多少”是进一步的前提。'}}],
    'references': [{'path': src(MOD), 'role': 'proof', 'declarations': ALL, 'sha256': sha(src(MOD))},
                   {'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
                   {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
                   {'path': REVIEW, 'role': 'integration', 'sha256': sha(REVIEW)},
                   {'path': CHOICES, 'role': 'integration', 'sha256': sha(CHOICES)},
                   {'path': ARGUMENT, 'role': 'statement', 'sha256': sha(ARGUMENT)},
                   {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)}],
    'proof_bindings': [{'source': src(MOD), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{MOD}',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': f'20 October 2026: added (IV2), graded significance, standing against status, and priority and '
              f'sufficiency on levels of continuation, after a literature check (significance review, section "the de '
              f'se question and graded significance"); readings D60; study section {N}.',
        'zh': f'2026年10月20日：新增（IV2），分级的意义、“是否算数”与“算多少”、延续层级上的优先与充足，此前做了文献核查（显著性审查'
              f'“从己问题与分级的意义”一节）；读法 D60；研究第 {N} 节。'}],
}
assert len(rec['statement']['en']) <= 300 and len(rec['statement']['zh']) <= 150, (len(rec['statement']['en']), len(rec['statement']['zh']))
assert len(rec['correspondence']['en']) <= 1200 and len(rec['correspondence']['zh']) <= 500
for x in rec['does_not_show']:
    assert len(x['en']) <= 240 and len(x['zh']) <= 110, (x['en'][:40], len(x['en']), len(x['zh']))
assert len(rec['hypotheses'][0]['en']) <= 420 and len(rec['hypotheses'][0]['zh']) <= 190
assert len(rec['validation_scope']['en']) <= 600 and len(rec['validation_scope']['zh']) <= 260
assert len(rec['next_delta']['en']) <= 400 and len(rec['next_delta']['zh']) <= 180
path = RECORDS / f'{RID}.json'
assert not path.exists()
path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
print('records written')
