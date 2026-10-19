#!/usr/bin/env python3
"""Write O2's record and update the two records it continues or reads beside:
python3 -B make_record.py CORE_RECEIPT STUDY_SECTION   (from the checkout root, after apply_text.py)

Every declaration cited is resolved against the receipt's audited declarations of Becoming.LimitVerification (a short
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
MOD = 'LimitVerification'
core_id, N = sys.argv[1], int(sys.argv[2])
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
HEAD = f'## {N}. What a method comes to say in the limit (O2)'
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


RID = 'what-a-method-comes-to-say-in-the-limit'
L = 'Limit.'
laws = [
    ('A method guesses yes or no at each horizon of a run; fixed by the record, its guess at k is the same on runs '
     'agreeing up to k. It verifies a reading in the limit where it converges to yes exactly inside, and refutes it in '
     'the limit where its yes recurs exactly inside; converging to no puts a run outside.',
     '方法在运行的每个界上猜是或否；由记录确定时，它在 k 处的猜测在到 k 为止一致的运行上相同。它在极限中证实读法，指它恰在读法之内收敛到是；在极限中否证读法，指它的是恰在读法之内复现；收敛到否则运行在外。',
     [L + 'Method', L + 'ByRecord', L + 'Converges', L + 'YesFrom', L + 'YesAfter', L + 'YesRecurs', L + 'Verifies',
      L + 'Refutes', L + 'converges_unique', L + 'not_recurs_of_no', L + 'Verifies.outside_of_no',
      L + 'Refutes.outside_of_no']),
    ('A reading verified in the limit by a method fixed by the record is the union of closed readings "from n on the '
     'guess is yes"; one refuted in the limit is the meet of verifiable readings "a yes comes at or after n".',
     '由记录确定的方法在极限中证实的读法，是闭读法“从 n 起猜测为是”之并；在极限中否证的读法，是可证实读法“n 处或之后有一个是”之交。',
     [L + 'verifies_iff_union', L + 'yesFrom_closed', L + 'refutes_iff_meet', L + 'yesAfter_verifiable']),
    ('A reading of tests is verified and refuted in the limit by "no test has failed so far", and "some test succeeds" '
     'by "some test has succeeded so far", each fixed by the record for tests fixed by prefixes.',
     '测试读法在极限中由“迄今无测试失败”证实并否证，“某测试成功”由“迄今某测试已成功”证实并否证；测试由前缀确定时，二者皆由记录确定。',
     [L + 'noneFailed', L + 'noneFailed_byRecord', L + 'noneFailed_verifies', L + 'noneFailed_refutes', L + 'Succeeds',
      L + 'someSucceeded', L + 'someSucceeded_byRecord', L + 'someSucceeded_verifies', L + 'someSucceeded_refutes']),
    ('The meet of two readings verified in the limit is verified by the conjunction of the guesses; the meet of two '
     'refuted in the limit is refuted by the joint guess, yes where each guess has said yes since the last joint yes.',
     '两个在极限中被证实的读法之交，由两猜测之合取证实；两个在极限中被否证的读法之交，由联合猜测否证：自上一次联合的是以来每个猜测都说过是时，它说是。',
     [L + 'both', L + 'both_byRecord', L + 'both_verifies', L + 'pending', L + 'jointly', L + 'jointly_byRecord',
      L + 'jointly_refutes']),
    ('A guess of values converging on each run to the run\'s hypothesis verifies and refutes in the limit each reading '
     '"the hypothesis is v".',
     '在每个运行上收敛到该运行之假说的取值猜测，在极限中证实并否证每个读法“假说为 v”。',
     [L + 'Identifies', L + 'says', L + 'says_byRecord', L + 'identifies_verifies', L + 'identifies_refutes']),
    ('With configurations told apart, "the last step changed nothing" is fixed by the record and verifies settling in '
     'the limit.',
     '构型可区分时，“上一步没有改变什么”由记录确定，并在极限中证实止定。',
     [L + 'still', L + 'still_byRecord', L + 'still_verifies', L + 'Free.settles_verified']),
    ('On the free process settling and its complement are dense; settling is neither verifiable nor refutable; under '
     'Markov\'s principle no method fixed by the record refutes it in the limit (the run changing where it says yes).',
     '在自由过程上止定及其补集都稠密；止定既不可证实也不可否证；在马尔可夫原则下，没有由记录确定的方法在极限中否证它（在方法说是处改变的运行）。',
     [L + 'Free.settles_dense', L + 'Free.unsettled_dense', L + 'Free.settles_not_verifiable',
      L + 'Free.settles_not_refutable', L + 'Free.against', L + 'Free.against_state', L + 'Free.settles_not_refuted']),
    ('On the sequences of moves "the last move was true" refutes recurrence in the limit and its negation verifies '
     'that from some step on every move is false; under Markov\'s principle no method fixed by the record verifies '
     'recurrence in the limit.',
     '在步序列上，“上一步为 true”在极限中否证复现，其否定在极限中证实“从某步起每步为 false”；在马尔可夫原则下，没有由记录确定的方法在极限中证实复现。',
     [L + 'Sequences.lastMove', L + 'Sequences.lastMove_byRecord', L + 'Sequences.lastMove_refutes',
      L + 'Sequences.EventuallyFalse', L + 'Sequences.notLastMove_verifies',
      L + 'Sequences.not_recurs_of_eventuallyFalse', L + 'Sequences.against', L + 'Sequences.against_act',
      L + 'Sequences.recurs_not_verified']),
    ('Saying from a run\'s not recurring that from some step on its moves are false, and saying which of two guesses '
     'recurs from their disjunction recurring, each give the limited principle of omniscience.',
     '由运行不复现说出从某步起其各步为 false，以及由两猜测之析取复现说出哪个猜测复现，各自给出有限全知原则。',
     [L + 'Sequences.eventuallyFalse_lpo', L + 'Sequences.either_recurs_lpo']),
]
for en, zh, _ in laws:
    assert len(en) <= 420 and len(zh) <= 190, (en[:40], len(en), len(zh))

O1_DEP = dep('what-a-finite-stretch-verifies', 'formal-reuse',
             'Reuses Becoming.Verification\'s Dense and its reading of verifiable and refutable readings of runs: the '
             'limit levels are stated above them.',
             '复用 Becoming.Verification 的 Dense 及其对运行读法可证实与可否证的读法：极限层级陈述于其上。',
             'Verifiable, refutable and dense readings of runs.', '运行的可证实、可否证与稠密读法。',
             'Readings verified or refuted in the limit, and where settling and recurrence sit.',
             '极限中被证实或被否证的读法，以及止定与复现的位置。', 'None.', '无。', src('Verification'))
HORIZON_DEP = dep('what-a-finite-history-refutes', 'formal-reuse',
                  'Reuses Becoming.Horizon\'s Run.AgreeUpTo, Adheres, tests fixed by prefixes, Markov\'s principle and the '
                  'sequences of moves with their recurrence.',
                  '复用 Becoming.Horizon 的 Run.AgreeUpTo、Adheres、由前缀确定的测试、马尔可夫原则及步序列与其复现。',
                  'Agreement up to a horizon, tests, Markov\'s principle, the sequences.', '到一界的一致、测试、马尔可夫原则、序列。',
                  'Methods fixed by the record, readings of tests in the limit, recurrence in the limit.',
                  '由记录确定的方法、极限中的测试读法、极限中的复现。', 'Markov\'s principle where a law takes it.',
                  '定律取之处的马尔可夫原则。', src('Horizon'))
SETTLE_DEP = dep('when-the-runs-of-a-process-settle', 'formal-reuse',
                 'Reuses Becoming.Enough\'s Settles and its free process of two configurations with the alternating run.',
                 '复用 Becoming.Enough 的 Settles 及其两构型的自由过程与交替运行。',
                 'Settling of runs, the free process, a run that does not settle.', '运行的止定、自由过程、不止定的运行。',
                 'Settling verified in the limit and refuted in the limit by no method.',
                 '止定在极限中被证实，且在极限中不被任何方法否证。', 'Decidable configurations where stated.',
                 '所述处构型可判定。', src('Enough'))

rec = {
    'schema_version': 2, 'id': RID,
    'title': {'en': 'What a method comes to say in the limit', 'zh': '方法在极限中所能说出者'},
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': NOW,
    'statement': {
        'en': 'A method fixed by the record verifies in the limit unions of closed readings and refutes meets of open '
              'ones. Settling is verified in the limit, at no finite stretch; recurrence is refuted in the limit and, '
              'under Markov\'s principle, verified there by no method.',
        'zh': '由记录确定的方法在极限中证实闭读法之并、否证开读法之交。止定在极限中被证实，而不在任何有限片段；复现在极限中被否证，在马尔可夫原则下没有方法在极限中证实它。'},
    'laws': [{'en': en, 'zh': zh, 'declarations': resolve(MOD, names)} for en, zh, names in laws],
    'hypotheses': [{
        'en': 'No axiom. Decidable configurations for settling (still and its laws); Markov\'s principle as the hypothesis '
              'of Free.settles_not_refuted and Sequences.recurs_not_verified; the limited principle of omniscience only '
              'as the calibrated conclusion of eventuallyFalse_lpo and either_recurs_lpo. Processes, readings and methods '
              'are otherwise arbitrary.',
        'zh': '不加公理。止定处构型可判定（still 及其定律）；马尔可夫原则作为 Free.settles_not_refuted 与 Sequences.recurs_not_verified 的假设；有限全知原则只作为 eventuallyFalse_lpo 与 either_recurs_lpo 被校准的结论。过程、读法与方法此外任意。'}],
    'does_not_show': [
        {'en': 'Joins: of readings verified in the limit (the classical dovetail is not stated), and of readings refuted in '
               'the limit by the disjunction of the guesses, whose split is the limited principle of omniscience.',
         'zh': '并：极限中被证实读法之并（未陈述经典的交错构造），以及由猜测之析取给出的极限中被否证读法之并，其拆分即有限全知原则。',
         'kind': 'scope'},
        {'en': 'That the two diagonal laws need Markov\'s principle: each proof uses it once; whether it can be dropped is '
               'open.', 'zh': '两条对角定律需要马尔可夫原则：每个证明各用它一次；能否去掉尚未定。', 'kind': 'scope'},
        {'en': 'That a method can be found for every union of closed readings, or that identification follows from '
               'deciding each of finitely many hypotheses in the limit.',
         'zh': '对闭读法的每个并都能找到方法，或由在极限中判定有限多个假说中的每一个即得辨识。', 'kind': 'scope'},
        {'en': 'An instance theorem on Becoming.Learnable\'s orbits: the record notes that Learnable.Rests is '
               'identification in the limit along an orbit through a map.',
         'zh': 'Becoming.Learnable 轨道上的实例定理：记录只注明 Learnable.Rests 是经一映射沿轨道的极限辨识。', 'kind': 'scope'}],
    'counterexamples': [{'path': src(MOD), 'detail': {
        'en': 'On the free process, the run that changes where a method says yes and stays where it says no: under '
              'Markov\'s principle it settles exactly where the method\'s yes does not recur, so no method refutes '
              'settling in the limit (Free.settles_not_refuted); on the sequences, the run playing the negation of the '
              'guess does the same for verifying recurrence (Sequences.recurs_not_verified).',
        'zh': '在自由过程上，在方法说是处改变、说否处停留的运行：在马尔可夫原则下，它恰在方法的是不复现时止定，故没有方法在极限中否证止定（Free.settles_not_refuted）；在序列上，下出猜测之否定的运行对证实复现同样如此（Sequences.recurs_not_verified）。'}}],
    'standard_boundaries': BOUNDS,
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {n_decl} declarations of '
              f'Becoming.{MOD}, {n_thm} of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'Built and reviewed in one session, with no separate reviewer; author review in study section {N}; not '
              'independently reviewed by a person.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.{MOD} 的 {n_decl} 项声明（{n_thm} 项定理）公理报告为空；'
              f'检查器并核对核心纯净。在一个会话中构建并审查，没有另设审查者；作者审查见研究第 {N} 节；未经人的独立审查。'},
    'next_delta': {
        'en': 'Joins at the limit levels; whether the diagonal laws need Markov\'s principle; actual inquiries read at '
              'these levels; an independent review.',
        'zh': '极限层级上的并；对角定律是否需要马尔可夫原则；实际探究读到这些层级上；独立审查。'},
    'correspondence': {
        'en': 'Readings verified in the limit are the Σ⁰₂ classes and those refuted in the limit the Π⁰₂ classes of the '
              'topology of runs; verification and refutation in the limit are those of formal learning theory (Putnam '
              '1965, Gold 1967, Kelly 1996), stated with the positive form of refutation. Readings (the AI\'s): "this '
              'has stopped changing" is a claim inquiry can come to make by watching each step, though no step tells it '
              'the claim has become final; "this changes again and again" cannot be come to even in the limit; locating '
              'where a run stopped, from its not going on, is deciding.',
        'zh': '极限中被证实的读法即运行拓扑的 Σ⁰₂ 类，极限中被否证的即 Π⁰₂ 类；极限中的证实与否证即形式学习理论中的（Putnam 1965、Gold 1967、Kelly 1996），否证取正面形式。读法（AI 的）：“这已不再改变”是探究可以通过逐步观察而得出并保持的主张，但没有哪一步告诉它这一主张已成定论；“这一再改变”即使在极限中也得不出；由运行不再继续而定位它在何处停止，就是判定。'},
    'canonical_source': src(MOD),
    'aliases': ['what a method comes to say in the limit', '方法在极限中所能说出者', 'verification in the limit',
                'refutation in the limit', 'Becoming.Limit.still_verifies',
                'Becoming.Limit.Free.settles_not_refuted', 'Becoming.Limit.Sequences.recurs_not_verified'],
    'dependencies': [O1_DEP, HORIZON_DEP, SETTLE_DEP],
    'related': [
        {'id': 'the-last-change-of-a-run', 'detail': {
            'en': 'Deciding settling outright is the limited principle of omniscience; here settling is verified in the '
                  'limit with no premise beyond decidable configurations.',
            'zh': '直接判定止定即有限全知原则；此处止定在极限中被证实，除构型可判定外无需前提。'}},
        {'id': 'learnable-through-registration', 'detail': {
            'en': 'Learnable.Rests is identification in the limit along an orbit through a map; identification decides '
                  'each hypothesis in the limit.',
            'zh': 'Learnable.Rests 是经一映射沿轨道的极限辨识；辨识在极限中判定每个假说。'}}],
    'references': [{'path': src(MOD), 'role': 'proof', 'declarations': sorted(d['name'] for d in m['declarations']),
                    'sha256': sha(src(MOD))},
                   {'path': src('Verification'), 'role': 'proof', 'sha256': sha(src('Verification'))},
                   {'path': src('Horizon'), 'role': 'proof', 'sha256': sha(src('Horizon'))},
                   {'path': src('Enough'), 'role': 'proof', 'sha256': sha(src('Enough'))},
                   {'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
                   {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
                   {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)}],
    'proof_bindings': [{'source': src(MOD), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{MOD}',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': f'19 October 2026: added (O2), the next step of what-a-finite-stretch-verifies (readings verifiable or '
              f'refutable in the limit, joined to the laws of settling and learning); study section {N}.',
        'zh': f'2026年10月19日：新增（O2），承接 what-a-finite-stretch-verifies 的下一步（极限中可证实或可否证的读法，与止定和学习之律相接）；'
              f'研究第 {N} 节。'}],
}
assert len(rec['statement']['en']) <= 300, len(rec['statement']['en'])
path = RECORDS / f'{RID}.json'
assert not path.exists(), ('record exists', RID)
path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
print('written', RID)

# The record it continues: its next step is taken.
p = RECORDS / 'what-a-finite-stretch-verifies.json'
d = json.loads(p.read_text())
old = 'Readings verifiable or refutable in the limit, the next levels above open and closed classes.'
k = [i for i, x in enumerate(d['does_not_show']) if x['en'] == old]
assert len(k) == 1, k
d['does_not_show'].pop(k[0])
assert d['next_delta']['en'].startswith('Readings verifiable or refutable in the limit, joined to the laws of learning')
d['next_delta'] = {'en': 'The three cases of the demarcation assessment read on actual inquiries; an independent review.',
                   'zh': '划界评估的三种情形读到实际探究上；独立审查。'}
d['related'].append({'id': RID, 'detail': {
    'en': 'The next levels: readings verified or refuted in the limit, where settling and recurrence sit.',
    'zh': '下一层级：极限中被证实或被否证的读法，以及止定与复现所处的位置。'}})
for r in d['references']:
    if r['path'] == CHAPTER:
        r['sha256'] = sha(CHAPTER)
d['history'].append({
    'en': f'19 October 2026, O2: the next step taken. Readings verified or refuted in the limit are stated in '
          f'Becoming.LimitVerification (record {RID}, study section {N}); the scope item naming them is removed and the '
          'next step revised. THE-THEORY-OF-BECOMING.md re-pointed after reading: since this record\'s reviewed hash the '
          'chapter gained the paragraph on what a method comes to say in the limit after this record\'s paragraph, and '
          'its section 8 and 9 rows changed. The claim is unchanged.',
    'zh': f'2026年10月19日，O2：下一步已完成。极限中被证实或被否证的读法在 Becoming.LimitVerification 中陈述（记录 {RID}，研究第 {N} 节）；'
          '删去指出它们的范围项，修订下一步。读过后 THE-THEORY-OF-BECOMING.md 重新指向：自本记录所审哈希以来，该章在本记录段落之后加入了关于方法在极限中所能说出者的段落，第 8、9 节各行有改动。论断不变。'})
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated', p.name)

# The settling record read beside it: settling decided outright and settling said in the limit.
p = RECORDS / 'the-last-change-of-a-run.json'
d = json.loads(p.read_text())
d['related'].append({'id': RID, 'detail': {
    'en': 'Settling, decided outright here exactly under the limited principle of omniscience, is verified in the limit '
          'with decidable configurations and refuted in the limit by no method under Markov\'s principle.',
    'zh': '止定在此恰在有限全知原则下被直接判定；构型可判定时它在极限中被证实，在马尔可夫原则下没有方法在极限中否证它。'}})
d['history'].append({
    'en': f'19 October 2026, O2: related entry for what-a-method-comes-to-say-in-the-limit (study section {N}). The claim '
          'is unchanged.',
    'zh': f'2026年10月19日，O2：加入与 what-a-method-comes-to-say-in-the-limit 的关联条目（研究第 {N} 节）。论断不变。'})
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated', p.name)
