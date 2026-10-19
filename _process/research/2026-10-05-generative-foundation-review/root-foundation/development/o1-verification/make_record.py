#!/usr/bin/env python3
"""Write O1's record and update the two records it continues:
python3 -B make_record.py CORE_RECEIPT STUDY_SECTION   (from the checkout root, after apply_text.py)

Every declaration cited is resolved against the receipt's audited declarations of Becoming.Verification (a short name
must match exactly one declaration by suffix), and the receipt must bind the module's current bytes."""
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
SCI = 'theories/becoming/chapters/SCIENTIFIC-PHILOSOPHY.md'
RECORDS = ROOT / 'theories/becoming/results/records'
MOD = 'Verification'
core_id, N = sys.argv[1], int(sys.argv[2])
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
HEAD = f'## {N}. What a finite stretch verifies, and what none can refute (O1)'
assert re.search('^' + re.escape(HEAD) + '$', (ROOT / STUDY).read_text(), re.M)
ANCHOR = f'{STUDY}#{N}-what-a-finite-stretch-verifies-and-what-none-can-refute-o1'


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


RID = 'what-a-finite-stretch-verifies'
laws = [
    ('A reading of points read as ideals is verifiable where every point inside has a stretch through which only points '
     'inside pass; the interior holds only points inside, is verifiable and holds every verifiable part.',
     '以理想读出的点的读法可证实，指每个在内的点都有一个只有在内的点经过的片段；内部只含在内的点，可证实，并包含每个可证实的部分。',
     ['Ideals.VerifiableBy', 'Ideals.InteriorBy', 'Ideals.InteriorBy.holds', 'Ideals.verifiableBy_iff_interior',
      'Ideals.interiorBy_verifiable', 'Ideals.interiorBy_largest', 'Ideals.VerifiableBy.interior_iff']),
    ('Refuting is verifying the complement, with no premise; a stable verifiable reading has a refutable complement; a '
     'point adhering to a reading lies outside the interior of its complement.',
     '否证即证实补集，无需前提；稳定的可证实读法有可否证的补集；附着于读法的点不在其补集的内部。',
     ['Ideals.refutableBy_iff_compl', 'Ideals.VerifiableBy.compl_refutable', 'Ideals.AdheresBy.not_interior_compl',
      'Ideals.InteriorBy.not_adheres_compl']),
    ('A class of ideals is open exactly where it is the class meeting an upper set of stretches, the set fixed by its '
     'finite histories; open is verifiable with no premise either way, and refutable is complement open.',
     '理想之类为开，恰当它是与片段的一个上集相交的类，该集由其有限历史确定；开即可证实，两向都无需前提；可否证即补集为开。',
     ['Ideals.Upper', 'Ideals.Meets', 'Ideals.Open', 'Ideals.meets_open', 'Ideals.open_iff_meets_principal',
      'Ideals.open_iff_upper', 'Ideals.upper_unique', 'Ideals.open_iff_verifiable', 'Ideals.refutable_iff_compl_open',
      'Ideals.Open.compl_closed']),
    ('Open classes hold every union and every meet of two; the interior is the largest open subclass. Asked of every '
     'order, a verifiable class has a refutable complement exactly under double-negation elimination.',
     '开类含每个并与两者之交；内部是最大的开子类。对每个序要求时，可证实类有可否证补集恰在双重否定消去之下。',
     ['Ideals.open_exists', 'Ideals.open_and', 'Ideals.open_true', 'Ideals.open_false', 'Ideals.interior_open',
      'Ideals.interior_largest', 'Ideals.Open.interior_iff', 'Ideals.verifiable_compl_refutable_iff']),
    ('On runs: Horizon\'s Verifiable is verifiability at stretches; a run is verified where a stretch of it is a stretch '
     'only of runs inside, the largest verifiable part; refuting a reading is verifying its complement.',
     '在运行上：Horizon 的 Verifiable 即在片段处可证实；运行被证实，指它有一个只属于在内运行的片段，这是最大的可证实部分；否证读法即证实其补集。',
     ['verifiable_iff_verifiableBy', 'Verified', 'verified_iff_interiorBy', 'Verified.holds', 'verifiable_iff_verified',
      'verified_verifiable', 'verified_largest', 'refutable_iff_compl_verifiable', 'Verifiable.compl_refutable',
      'Adheres.not_verified_compl', 'Verified.not_adheres_compl']),
    ('A run lies in an open class of histories exactly where a finite history of it does; a reading of runs is '
     'verifiable exactly where it is the reading of an open class; verifiable readings hold meets and unions, refutable '
     'ones joins of two.',
     '运行在一个历史开类中，恰当其某个有限历史在其中；运行读法可证实，恰当它是某个开类的读法；可证实读法对交与并封闭，可否证读法对两者之并封闭。',
     ['Stretches.open_runs', 'Stretches.open_iff_upper', 'Stretches.verifiable_of_class', 'Stretches.verifiable_iff_open',
      'Stretches.verifyingClass', 'Stretches.verifiable_iff_class', 'Stretches.verifiable_and',
      'Stretches.verifiable_exists', 'Stretches.refutable_or', 'Stretches.verifiable_true_false',
      'Stretches.open_compl_adheres', 'Stretches.refutable_of_compl_open']),
    ('Asked of every process, a verifiable reading has a refutable complement only under Markov\'s principle; a reading '
     'both verifiable and refutable is decided by a finite stretch of each run at which it is decided.',
     '对每个过程要求时，可证实读法有可否证补集仅在马尔可夫原则之下；既可证实又可否证的读法，在每个它已被判定的运行上由一个有限片段判定。',
     ['verifiable_compl_refutable_markov', 'decided_at_stretch']),
    ('Every reading is its hull met with its remainder, holding wherever it is adhered to: the largest part so splitting '
     'it, the reading itself where it is adhered to; a reading is closed exactly where its remainder holds everywhere.',
     '每个读法都是其包与其余部之交，余部即凡附着处皆成立：这是如此分解它的最大部分，在附着处即读法本身；读法为闭恰当其余部处处成立。',
     ['Ideals.RemainderBy', 'Ideals.splitBy', 'Ideals.remainderBy_largest', 'Ideals.remainderBy_iff_of_adheres',
      'Remainder', 'remainder_iff_remainderBy', 'split', 'remainder_largest', 'remainder_iff_of_adheres',
      'Stretches.closed_iff_remainder']),
    ('No finite stretch refutes the remainder; it is met through every stretch up to double negation, and outright where '
     'it is decided whether the reading can still hold there.',
     '没有有限片段否证余部；它经过每个片段都被遇到，至多差双重否定；在判定读法在该处是否仍可成立时则直接成立。',
     ['Ideals.remainderBy_not_refuted', 'Ideals.remainderBy_meets_not_not', 'Ideals.remainderBy_meets_of_decided',
      'remainder_not_refuted', 'remainder_meets_not_not', 'Dense', 'remainder_dense_of_decided']),
    ('The disjunctive remainder, holding or not adhering, is the same split within the remainder; asked of every process, '
     'its density is exactly excluded middle.',
     '析取余部（成立或不附着）给出同一分解并含于余部；对每个过程要求时，其稠密恰是排中律。',
     ['Ideals.OrNotAdheresBy', 'Ideals.splitBy_or', 'Ideals.OrNotAdheresBy.remainder',
      'Ideals.orNotAdheresBy_meets_of_decided', 'OrNotAdheres', 'split_or', 'OrNotAdheres.remainder',
      'orNotAdheres_dense_iff_em']),
    ('What a finite stretch finds against a reading is exactly what it finds against its hull, so readings with one hull '
     'are refuted by the same stretches; a dense reading, and every remainder, is refuted by no stretch.',
     '有限片段对读法所发现的反证，恰是它对其包所发现的，故同包的读法被同样的片段否证；稠密读法以及每个余部都不被任何片段否证。',
     ['refutes_iff_refutes_hull', 'same_hull_same_refutations', 'NoStretchRefutes', 'Dense.noStretchRefutes',
      'remainder_noStretchRefutes']),
    ('A refutable reading refuted by no stretch excludes nothing, up to double negation; a reading whose remainder is '
     'refutable holds, up to double negation, wherever it is adhered to.',
     '不被任何片段否证的可否证读法不排除任何东西（至多差双重否定）；余部可否证的读法，在其附着处成立（至多差双重否定）。',
     ['Refutable.noStretchRefutes_not_not', 'Refutable.remainder_not_not']),
    ('A practice keeping verdicts within a favoured reading, each fixed by the record so far and met through its stretch, '
     'exists exactly where the reading is dense; a refutable favoured reading so kept excludes nothing.',
     '一种做法把结论保持在所偏好的读法之内，每个结论由迄今记录确定并经过该记录的片段被遇到；它恰在该读法稠密时存在；如此保住的可否证读法不排除任何东西。',
     ['Practice', 'ByRecord', 'Insulates', 'insulates_iff_dense', 'Insulates.refutable_not_not']),
    ('In the Boolean sequences, some move being true is verifiable and dense; recurrence is dense and not verifiable, as '
     'it is not refutable.',
     '在布尔序列中，某步为 true 可证实且稠密；复现稠密且不可证实，正如它不可否证。',
     ['Sequences.eventually_verifiable', 'Sequences.eventually_dense', 'Sequences.recurs_dense',
      'Sequences.recurs_not_verifiable']),
]
for en, zh, _ in laws:
    assert len(en) <= 420 and len(zh) <= 190, (en[:40], len(en), len(zh))

HORIZON_DEP = dep('what-a-finite-history-refutes', 'formal-reuse',
                  'Reuses Becoming.Horizon\'s Run.AgreeUpTo, Refutable, Verifiable and Adheres, the sequences and '
                  'Markov\'s principle: Verifiable is read here at stretches and its complement calibrated.',
                  '复用 Becoming.Horizon 的 Run.AgreeUpTo、Refutable、Verifiable 与 Adheres、序列及马尔可夫原则：此处在片段处读 Verifiable 并校准其补集。',
                  'Agreement up to a horizon, refutability, verifiability and adherence of readings of runs.',
                  '到一界的一致，以及运行读法的可否证、可证实与附着。',
                  'The readings of runs whose verification, interior and split are stated.',
                  '其证实、内部与分解被陈述的运行读法。', 'None.', '无。', src('Horizon'))
IDEALS_DEP = dep('a-history-read-off-its-finite-stretches', 'formal-reuse',
                 'Reuses the order of stretches, ideals, directed unions, the hull, closed classes, avoidance and the '
                 'two-element chain of Becoming.Ideals, and Becoming.HistoryIdeals\' runs as ideals with their laws.',
                 '复用 Becoming.Ideals 的片段之序、理想、有向并、包、闭类、回避与二元链，以及 Becoming.HistoryIdeals 中作为理想的运行及其律。',
                 'Histories as ideals of their stretches, the hull as the least closed class, closed classes as lower sets.',
                 '作为片段理想的历史，作为最小闭类的包，作为下集的闭类。',
                 'The open classes, dual to the closed ones, and the split of a reading with its hull.',
                 '与闭类对偶的开类，以及读法与其包的分解。', 'None.', '无。', src('HistoryIdeals'))

rec = {
    'schema_version': 2, 'id': RID,
    'title': {'en': 'What a finite stretch verifies, and what none can refute', 'zh': '有限片段所证实者，与无片段能否证者'},
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': NOW,
    'statement': {
        'en': 'Open classes of histories are the verifiable ones, with no premise; refuting is verifying the complement. '
              'Every reading is its hull met with a remainder no finite stretch refutes, dense exactly where it is '
              'decided at each stretch whether the reading can still hold.',
        'zh': '历史的开类即可证实类，无需前提；否证即证实补集。每个读法都是其包与一个无有限片段能否证的余部之交，余部恰在每个片段处判定读法是否仍可成立时稠密。'},
    'laws': [{'en': en, 'zh': zh, 'declarations': resolve(MOD, names)} for en, zh, names in laws],
    'hypotheses': [{
        'en': 'No axiom and no premise: the order of stretches is any preorder, the points and readings arbitrary, the '
              'process arbitrary. remainder_dense_of_decided takes, as a hypothesis, the decision at each stretch whether '
              'a run of the reading passes through it; double-negation elimination, excluded middle and Markov\'s '
              'principle appear only as the calibrated sides of verifiable_compl_refutable_iff, orNotAdheres_dense_iff_em '
              'and verifiable_compl_refutable_markov.',
        'zh': '不加公理、不加前提：片段之序是任意预序，点与读法任意，过程任意。remainder_dense_of_decided 以“在每个片段处判定是否有读法中的运行经过它”为假设；双重否定消去、排中律与马尔可夫原则只作为 verifiable_compl_refutable_iff、orNotAdheres_dense_iff_em 与 verifiable_compl_refutable_markov 被校准的一侧出现。'}],
    'does_not_show': [
        {'en': 'Which readings of an actual inquiry are verifiable, refutable or dense: that depends on the process they '
               'are read on.', 'zh': '实际探究的哪些读法可证实、可否证或稠密：这取决于读它们的过程。', 'kind': 'scope'},
        {'en': 'That a reading no finite record refutes lacks standing: recurrence is dense and can be an honest '
               'hypothesis about an unending course.',
         'zh': '不被任何有限记录否证的读法就没有地位：复现是稠密的，可以是关于无尽进程的诚实假说。', 'kind': 'non-implication',
         'witness': 'Becoming.Sequences.recurs_dense'},
        {'en': 'That the remainder is dense without a decision: asked of every process, the density of the disjunctive '
               'remainder is exactly excluded middle.',
         'zh': '不经判定余部即稠密：对每个过程要求时，析取余部的稠密恰是排中律。', 'kind': 'non-implication',
         'witness': 'Becoming.orNotAdheres_dense_iff_em'},
        {'en': 'That a verifiable reading has a refutable complement without a decision: asked of every order it is '
               'exactly double-negation elimination, and on runs it gives Markov\'s principle.',
         'zh': '不经判定可证实读法就有可否证补集：对每个序要求时恰是双重否定消去，在运行上给出马尔可夫原则。',
         'kind': 'non-implication', 'witness': 'Becoming.Ideals.verifiable_compl_refutable_iff'},
        {'en': 'Readings verifiable or refutable in the limit, the next levels above open and closed classes.',
         'zh': '极限中可证实或可否证的读法，即开类与闭类之上的下一层级。', 'kind': 'scope'}],
    'counterexamples': [{'path': src(MOD), 'detail': {
        'en': 'In the Boolean sequences recurrence is dense, not verifiable (the run of true throughout adheres to its '
              'complement) and not refutable (the run of false throughout adheres to it): no finite record counts for or '
              'against it (recurs_dense, recurs_not_verifiable, Horizon\'s recurs_not_refutable).',
        'zh': '在布尔序列中复现稠密、不可证实（处处为 true 的运行附着于其补集）且不可否证（处处为 false 的运行附着于它）：没有有限记录支持或反对它（recurs_dense、recurs_not_verifiable、Horizon 的 recurs_not_refutable）。'}}],
    'standard_boundaries': BOUNDS,
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {n_decl} declarations of '
              f'Becoming.{MOD}, {n_thm} of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'Built and reviewed in one session, with no separate reviewer; author review in study section {N}; not '
              'independently reviewed by a person.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.{MOD} 的 {n_decl} 项声明（{n_thm} 项定理）公理报告为空；'
              f'检查器并核对核心纯净。在一个会话中构建并审查，没有另设审查者；作者审查见研究第 {N} 节；未经人的独立审查。'},
    'next_delta': {
        'en': 'Readings verifiable or refutable in the limit, joined to the laws of learning and settling; the three cases '
              'of the demarcation assessment read on actual inquiries; an independent review.',
        'zh': '极限中可证实或可否证的读法，与学习和止定之律相接；划界评估的三种情形读到实际探究上；独立审查。'},
    'correspondence': {
        'en': 'Open classes of ideals are the Scott-open sets, on runs the open sets of the topology of runs; verifiable '
              'and refutable readings are the open and closed classes of formal learning theory (Kelly 1996); the split is '
              'the decomposition of every property into a safety and a liveness property (Alpern and Schneider 1985), the '
              'remainder its largest liveness part. Readings (the AI\'s): a verification must find a stretch it is only '
              'known not to miss; systematic insulation of a favoured verdict, the pattern the demarcation assessment of '
              'SCIENTIFIC-PHILOSOPHY names, keeps a verdict no finite record refutes; separating what a reading says that '
              'a record can count against from what none can is deciding, at each stretch, whether it can still hold.',
        'zh': '理想的开类即 Scott 开集，在运行上即运行拓扑的开集；可证实与可否证读法即形式学习理论的开类与闭类（Kelly 1996）；分解即每个性质分为安全性与活性性质之交（Alpern 与 Schneider 1985），余部是其最大的活性部分。读法（AI 的）：证实必须找到一个只知道不会错过的片段；对所偏好结论的系统性免疫（SCIENTIFIC-PHILOSOPHY 的划界评估所指的模式）保住的是没有有限记录能否证的结论；把读法中记录能反对的与不能反对的分开，就是在每个片段处判定它是否仍可成立。'},
    'canonical_source': src(MOD),
    'aliases': ['what a finite stretch verifies', '有限片段所证实者', 'open classes of histories', 'safety and liveness',
                'Becoming.split', 'Becoming.insulates_iff_dense', 'systematic insulation (reading)'],
    'dependencies': [IDEALS_DEP, HORIZON_DEP],
    'related': [{'id': 'scientific-inquiry-foundation', 'detail': {
        'en': 'The formal side of the demarcation comparison: a practice that insulates its favoured verdict keeps a '
              'verdict no finite record refutes.',
        'zh': '划界对照的形式一面：对所偏好结论加以免疫的做法，保住的是没有有限记录能否证的结论。'}}],
    'references': [{'path': src(MOD), 'role': 'proof', 'declarations': sorted(d['name'] for d in m['declarations']),
                    'sha256': sha(src(MOD))},
                   {'path': src('HistoryIdeals'), 'role': 'proof', 'sha256': sha(src('HistoryIdeals'))},
                   {'path': src('Horizon'), 'role': 'proof', 'sha256': sha(src('Horizon'))},
                   {'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
                   {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
                   {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
                   {'path': SCI, 'role': 'statement', 'sha256': sha(SCI)}],
    'proof_bindings': [{'source': src(MOD), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{MOD}',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': f'19 October 2026: added (O1), the next step of a-history-read-off-its-finite-stretches (what a finite '
              f'stretch verifies, the open classes) and the formal side of the demarcation comparison of the '
              f'scientific-inquiry target; study section {N}.',
        'zh': f'2026年10月19日：新增（O1），承接 a-history-read-off-its-finite-stretches 的下一步（有限片段所证实者，即开类），'
              f'并给出科学探究目标之划界对照的形式一面；研究第 {N} 节。'}],
}
assert len(rec['statement']['en']) <= 300, len(rec['statement']['en'])
path = RECORDS / f'{RID}.json'
assert not path.exists(), ('record exists', RID)
path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
print('written', RID)

# The record it continues: its next step is taken.
p = RECORDS / 'a-history-read-off-its-finite-stretches.json'
d = json.loads(p.read_text())
old = 'What a finite stretch verifies, the open classes of histories, is not stated on this order.'
k = [i for i, x in enumerate(d['does_not_show']) if x['en'] == old]
assert len(k) == 1, k
d['does_not_show'].pop(k[0])
assert d['next_delta']['en'].startswith('What a finite stretch verifies (the open classes)')
d['next_delta'] = {'en': 'Readings verifiable or refutable in the limit on the order of stretches; an independent review.',
                   'zh': '片段之序上极限中可证实或可否证的读法；独立审查。'}
d['related'].append({'id': RID, 'detail': {
    'en': 'What a finite stretch verifies, the open classes dual to the closed classes here, and the split of every '
          'reading into its hull and a remainder no stretch refutes.',
    'zh': '有限片段所证实者，即与此处闭类对偶的开类，以及每个读法分为其包与无片段能否证的余部。'}})
for r in d['references']:
    if r['path'] == CHAPTER:
        r['sha256'] = sha(CHAPTER)
d['history'].append({
    'en': f'19 October 2026, O1: the next step taken. What a finite stretch verifies (the open classes) is stated in '
          f'Becoming.Verification (record {RID}, study section {N}); the scope item saying it was not stated is removed '
          'and the next step revised. THE-THEORY-OF-BECOMING.md re-pointed after reading: since this record\'s reviewed '
          'hash the chapter gained the paragraphs on what a finite stretch verifies and on what a method comes to say '
          'in the limit (O2, landed with O1) after this record\'s paragraph, and its section 8 and 9 rows changed. The '
          'claim is unchanged.',
    'zh': f'2026年10月19日，O1：下一步已完成。有限片段所证实者（开类）在 Becoming.Verification 中陈述（记录 {RID}，研究第 {N} 节）；'
          '删去说它未陈述的范围项，修订下一步。读过后 THE-THEORY-OF-BECOMING.md 重新指向：自本记录所审哈希以来，该章在本记录段落之后加入了关于有限片段所证实者与方法在极限中所能说出者（O2，与 O1 同时落地）的段落，第 8、9 节各行有改动。论断不变。'})
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated', p.name)

# The scientific-inquiry target: progress on the formal side of the comparison; the target's wording is unchanged.
p = RECORDS / 'scientific-inquiry-foundation.json'
d = json.loads(p.read_text())
d['progress'].append({
    'en': 'Formal side of the demarcation comparison: every reading is what a finite record can refute met with a '
          'remainder none can, and a practice keeping a favoured verdict, never refuted by the record, exists exactly '
          'where no finite record refutes the verdict; the form alone does not decide standing.',
    'zh': '划界对照的形式一面：每个读法都是有限记录能否证的部分与无记录能否证的余部之交；一种保住所偏好结论、从不被记录否证的做法，恰在没有有限记录能否证该结论时存在；仅凭形式不能判定地位。',
    'source': ANCHOR})
if not any(r['path'] == STUDY for r in d['references']):
    d['references'].append({'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)})
d['related'].append({'id': RID, 'detail': {
    'en': 'The formal side of the comparison of a warranted claim, an investigated failure and systematic insulation.',
    'zh': '有根据的主张、经研究的失败与系统性免疫三者对照的形式一面。'}})
d['history'].append({
    'en': f'19 October 2026, O1: progress entry for the formal side of the demarcation comparison (record {RID}, study '
          f'section {N}). The target, its status and its next step are unchanged: the comparison on actual inquiries '
          'remains.',
    'zh': f'2026年10月19日，O1：为划界对照的形式一面加入进展条目（记录 {RID}，研究第 {N} 节）。目标、状态与下一步不变：在实际探究上的对照仍待完成。'})
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated', p.name)
