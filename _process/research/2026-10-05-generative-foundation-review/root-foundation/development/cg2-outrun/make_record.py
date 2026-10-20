#!/usr/bin/env python3
"""Write CG2's record the-rest-outruns-the-renewal:
python3 -B make_record.py CORE_RECEIPT STUDY_SECTION   (from the checkout root, after the study section is in)

Every declaration cited is resolved against the receipt's audited declarations of Becoming.Exclusion, and the
receipt must bind the module's current bytes. Empirical numbers come from the experiment's VERDICTS.json."""
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
EXP = 'experiments/commons-outrun'
RECORDS = ROOT / 'theories/becoming/results/records'
MOD = 'Exclusion'
core_id, N = sys.argv[1], int(sys.argv[2])
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
assert re.search(rf'^## {N}\. .*\(CG2\)$', (ROOT / STUDY).read_text(), re.M)
V = json.loads((ROOT / EXP / 'results' / 'VERDICTS.json').read_text())


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def src(mod):
    return f'{PKG}/Becoming/{mod}.lean'


m = next(m for m in core['modules'] if m['module'] == f'Becoming.{MOD}')
assert core['source_sha256'][f'Becoming.{MOD}'] == sha(src(MOD)), 'receipt does not bind'
assert not any(m['axiom_dependencies'].values())
FULL = [d['name'] for d in m['declarations']]


def resolve(names):
    out = []
    for n in names:
        hits = [f for f in FULL if f == 'Becoming.' + n or f.endswith('.' + n)]
        assert len(hits) == 1, (n, hits)
        out.append(hits[0])
    return out


OWN = ['Flow.rest_le_taken', 'Flow.outrun_excess', 'Flow.outrun_below', 'Flow.outrun_ends',
       'Flow.outrun_reading_alike']
RID = 'the-rest-outruns-the-renewal'
laws = [
    ('Where a part (the rest) takes from a condition jointly more than a step gives to it, the joint taking exceeds '
     'what is given, whatever any formation outside the part takes; a full taker with one other taker is the case of '
     'a part of two.',
     '一个部分（其余者）在一步中从条件联合所取多于该步所给时，联合所取超过所给，不论部分之外的任何形成取多少；取尽所给者加另一取用者，是两成员之部分的情形。',
     ['Flow.rest_le_taken', 'Flow.outrun_excess', 'Flow.excess_of_takesAll']),
    ('Where renewal depends on what it renews at need m, n such steps from a level below n + m leave the level below '
     'm from then on and end every formation depending on the condition at such a need, whatever a member outside '
     'the part takes.',
     '更新以需要 m 依存于所更新者之处，从低于 n + m 的水平起 n 个这样的步，使水平此后低于 m，并终结以该需要依存于条件的每个形成，不论部分之外的成员取多少。',
     ['Flow.outrun_below', 'Flow.outrun_ends']),
    ('With need one, in two flows in which the rest outruns from a level at most n, every score reading the condition '
     'only from step T + n on scores the two alike, however a member\'s act differs between them: its restraint is '
     'invisible to such a reading.',
     '需要为一时，在其余者都从至多 n 的水平起超出更新的两个流中，只读第 T + n 步起该条件的每个评分对两者评分相同，不论成员的行动在两者之间如何不同：其克制对这样的读取不可见。',
     ['Flow.outrun_reading_alike']),
]
for en, zh, _ in laws:
    assert len(en) <= 420 and len(zh) <= 190, (en[:40], len(en), len(zh))

C = V['conditions']
def pct(name):
    return round(100 * C[name]['alive_probe_mean'])
X = V['contrasts']
ident = V['identity']

rec = {
    'schema_version': 2, 'id': RID,
    'title': {'en': 'The rest outruns the renewal', 'zh': '其余者超出更新'},
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': NOW,
    'statement': {
        'en': 'Where the other members alone take more than a gated renewal gives, the condition ends whatever a member '
              'takes, and with need one every reading of it after the end is alike under the member\'s acts: no weight '
              'of such a reading selects its restraint.',
        'zh': '其余成员单独所取就多于门控更新所给之处，条件终结，不论某成员取多少；需要为一时，终结之后对它的每个读取在该成员的各行动下相同：这样的读取无论权重多大，都不选择其克制。'},
    'laws': [{'en': en, 'zh': zh, 'declarations': resolve(names)} for en, zh, names in laws],
    'hypotheses': [{
        'en': 'No axiom. Balance; only active formations give; activity needs support; whatever gives to the condition '
              'depends on it at the need (the gate); the rest as a list without repetition of formations taking part '
              'where they take. Natural-number amounts, discrete steps; for the reading law, need one.',
        'zh': '不加公理。平衡；只有活跃的形成给予；活动需要支持；给予该条件者以该需要依存于它（门）；其余者为无重复的形成列表，取用时参与。自然数的量，离散的步；读取之律需要为一。'}],
    'does_not_show': [
        {'en': 'That depletion is the only equilibrium: where the rest outruns, restraint by all may also be one; which '
               'is reached is a claim about learning, tested in CG2, not a theorem.',
         'zh': '耗尽是唯一的均衡：其余者超出之处，全体克制也可能是均衡；到达哪一个是关于学习的断言，由 CG2 检验，不是定理。',
         'kind': 'non-implication'},
        {'en': 'Anything about stochastic regrowth: the laws hold course by course; whether the rest outruns in a '
               'stochastic environment is computed (exact best responses), not proved.',
         'zh': '关于随机再生的任何结论：这些律逐个进程成立；随机环境中其余者是否超出是计算出来的（精确的最佳反应），不是证明的。',
         'kind': 'scope'},
        {'en': 'That restraint is better: the laws say where a reading cannot see it, not that seeing it is owed.',
         'zh': '克制是更好的：这些律说明读取在何处看不到它，而不说看到它是应当的。',
         'kind': 'non-implication'}],
    'counterexamples': [],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'names-provisional',
                            'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the declarations of '
              f'Becoming.{MOD}, these among them, have empty axiom reports; the checker verifies core purity. Tested on '
              f'learners in CG2 ({EXP}, predictions frozen at 8a049b4fb before any learning run; verdicts in its '
              f'README and study section {N}). Literature check in the significance review. One session; not '
              'independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.{MOD} 的声明（含此处各项）公理报告为空；检查器并核对核心纯净。'
              f'在 CG2 中以学习者检验（{EXP}，预测在任何学习运行之前冻结于 8a049b4fb；判定见其 README 与研究第 {N} 节）。'
              '文献核查见显著性审查。一个会话；未经独立审查。'},
    'next_delta': {
        'en': 'A stochastic form (the probability that the rest outruns before a reading, from the margin and the '
              'maximum expected renewal); which equilibrium learners reach where both exist; an independent review.',
        'zh': '随机形式（其余者在读取之前超出的概率，由余量与最大期望更新给出）；两者都是均衡时学习者到达哪一个；独立审查。'},
    'correspondence': {
        'en': 'Pivotality at a threshold (Palfrey and Rosenthal 1984) read on the rest: a member is pivotal exactly '
              'where the rest alone does not cross the margin before the reading. Coordination at a known threshold '
              '(Barrett 2013; Diekert 2017); the folk theorem for stochastic games (Dutta 1995); extinction in '
              'equilibrium past a player-number threshold (Mitra and Sorger 2014); risk-dominant selection under '
              'learning (Kandori, Mailath and Rob 1993). CG2, on tabular learners in a Harvest-style commons '
              '(Perolat et al. 2017): ' + ('; '.join(f'{k} {"held" if v else "failed"}' for k, v in X.items())) + '.',
        'zh': '在阈值处的关键性（Palfrey 与 Rosenthal 1984）读到其余者上：成员恰在其余者单独不会在读取之前越过余量时是关键的。已知阈值处的协调（Barrett 2013；Diekert 2017）；随机博弈的无名氏定理（Dutta 1995）；超过参与者数阈值时均衡中的灭绝（Mitra 与 Sorger 2014）；学习下的风险占优选择（Kandori、Mailath 与 Rob 1993）。CG2 以表格学习者在 Harvest 式公地中检验（Perolat 等 2017）。'},
    'canonical_source': src(MOD),
    'aliases': ['the rest outruns the renewal', '其余者超出更新', 'restraint invisible after the rest\'s end',
                'Becoming.Flow.outrun_below', 'Becoming.Flow.outrun_reading_alike'],
    'dependencies': [
        {'id': 'own-count-misses-joint-excess', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses joint excess bounded by the level and the gate keeping a level below the need '
                          '(Flow.excess_bounded_at, Flow.stays_below).',
                    'zh': '复用由水平界定的联合超出与使水平保持低于需要的门（Flow.excess_bounded_at、Flow.stays_below）。'},
         'interface': {
             'output': {'en': 'n steps of joint excess from below n + m leave the level below m for good.',
                        'zh': '从低于 n + m 起 n 步联合超出，使水平永远低于 m。'},
             'input': {'en': 'Joint excess supplied by the rest alone, whatever a member takes.',
                       'zh': '由其余者单独提供的联合超出，不论成员取多少。'},
             'conditions': {'en': 'Balance; the gate; givers supported.', 'zh': '平衡；门；给予者被支持。'},
             'evidence': src('Continuation')}},
        {'id': 'what-taking-all-excludes', 'relation': 'formal-reuse',
         'detail': {'en': 'Full taking alongside another taker (Flow.excess_of_takesAll) is now derived as the case of '
                          'a part of two; the ending of dependents below the need (Flow.ends_below_at).',
                    'zh': '与另一取用者并存的取尽所给（Flow.excess_of_takesAll）现作为两成员之部分的情形推出；低于需要时依存者的终结（Flow.ends_below_at）。'},
         'interface': {
             'output': {'en': 'A full taker with another taker exceeds what is given.',
                        'zh': '取尽所给者加另一取用者超过所给。'},
             'input': {'en': 'The same, read as a part of two outrunning the renewal.',
                       'zh': '同一事实，读作两成员之部分超出更新。'},
             'conditions': {'en': 'The two apart and taking part.', 'zh': '两者相异且参与。'},
             'evidence': src(MOD)}}],
    'related': [
        {'id': 'the-gap-for-ones-own-act', 'detail': {
            'en': 'The gap read on the rest: the member\'s act differs only where its reading no longer looks once the '
                  'rest has ended the condition, so no selection through that reading tells its acts apart.',
            'zh': '读到其余者上的间隙：其余者终结条件之后，成员行动的差异只在其读取不再看的地方，故经由该读取的选择分不出其各行动。'}}],
    'references': [{'path': src(MOD), 'role': 'proof', 'declarations': resolve(OWN + ['Flow.excess_of_takesAll']), 'sha256': sha(src(MOD))},
                   {'path': src('Continuation'), 'role': 'proof', 'sha256': sha(src('Continuation'))},
                   {'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
                   {'path': f'{EXP}/README.md', 'role': 'integration', 'sha256': sha(f'{EXP}/README.md')},
                   {'path': f'{EXP}/PREDICTIONS-2026-10-20.md', 'role': 'integration',
                    'sha256': sha(f'{EXP}/PREDICTIONS-2026-10-20.md')},
                   {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
                   {'path': REVIEW, 'role': 'integration', 'sha256': sha(REVIEW)}],
    'proof_bindings': [{'source': src(MOD), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{MOD}',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': f'20 October 2026: added (CG2), the condition on the rest that CG1\'s D2b failure turned on, after a '
              f'literature check (significance review, "restraint as an equilibrium on a gated renewal"), and tested '
              f'on learners with predictions frozen before any run; study section {N}.',
        'zh': f'2026年10月20日：新增（CG2），即 CG1 的 D2b 失败所系的关于其余者的条件，此前做了文献核查（显著性审查“门控更新上作为均衡的克制”），并以学习者检验，预测在任何运行之前冻结；研究第 {N} 节。'}],
}
assert len(rec['statement']['en']) <= 300, len(rec['statement']['en'])
assert len(rec['statement']['zh']) <= 150, len(rec['statement']['zh'])
for x in rec['does_not_show']:
    assert len(x['en']) <= 240 and len(x['zh']) <= 110, (x['en'][:40], len(x['en']), len(x['zh']))
path = RECORDS / f'{RID}.json'
assert not path.exists(), ('record exists', RID)
path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
print('written', RID)
