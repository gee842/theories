#!/usr/bin/env python3
"""Write MA1's record and update the record it continues (capture-through-the-rule):
python3 -B make_record.py CORE_RECEIPT STUDY_SECTION   (from the checkout root, after apply_text.py)

Every declaration cited is resolved against the receipt's audited declarations of Becoming.ClosedCapture (a short
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
OPENING = 'theories/becoming/OPENING.md'
RECORDS = ROOT / 'theories/becoming/results/records'
MOD = 'ClosedCapture'
core_id, N = sys.argv[1], int(sys.argv[2])
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
HEAD = f'## {N}. The meta-attractor\'s loop closed on the spine (MA1)'
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
listed = set()

BOUNDS = ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical', 'names-provisional',
          'omission-not-refutation']


def dep(rid, relation, en, zh, out_en, out_zh, in_en, in_zh, cond_en, cond_zh, evidence):
    return {'id': rid, 'relation': relation, 'detail': {'en': en, 'zh': zh},
            'interface': {'output': {'en': out_en, 'zh': out_zh}, 'input': {'en': in_en, 'zh': in_zh},
                          'conditions': {'en': cond_en, 'zh': cond_zh}, 'evidence': evidence}}


RID = 'closed-capture'
C = 'ClosedCapture.'
B = 'ClosedCapture.Beyond.'
P = 'ClosedCapture.Proportional.'
laws = [
    ('What the loop does not read does not change it: on Pace\'s two-level course with the fast configuration a pair, '
     'the share and what lies beyond it, where neither the next share nor the rule read reads what lies beyond (Unread), '
     'courses from starts alike in share and rule stay alike in both at every step; courses that come apart read beyond '
     'the share; the share\'s law joined with a step beyond runs exactly as the share\'s law alone.',
     '回路不读的不改变它：在 Pace 的两速历程上，快构形为一对，即份额与份额之外者；下一份额与读出的规则都不读份额之外者时（Unread），'
     '份额与规则相同的起点，其进程每一步在两者上都相同；分开了的进程读份额之外者；带份额之外一步的合并之律与份额自身之律同样运行。',
     [C + 'Unread', C + 'turn_unread', C + 'unread_course', C + 'reads_beyond_of_apart', C + 'join', C + 'joinRead',
      C + 'join_unread', C + 'join_alike', C + 'turn_join', C + 'join_course']),
    ('A locked loop outlives its loss: where every step adds at least one to what lies beyond (Accrues), from a locked '
     'configuration the loss at step t is at least t above where it started, so it passes every bound, while the course '
     'stays locked and neither the share nor the rule is ever below where it started.',
     '锁定的回路比它的损失更持久：每一步都使份额之外者至少增加一（Accrues）时，从锁定的构形起，第 t 步的损失至少比起点高 t，'
     '所以越过每一界限，而进程保持锁定，份额与规则都从不低于起点。',
     [C + 'Accrues', C + 'loss_grows', C + 'lock_outlives_loss']),
    ('A reading that reads the loss turns: where the rule read favours at no configuration whose loss is at least N, and '
     'every step adds at least one, at the step after every reading step at which the loss has passed N the rule in force '
     'does not favour, so the course is not locked there, whatever the share.',
     '读损失的读法转向：在损失至少为 N 的构形上读出的规则都不偏向、且每一步至少增加一时，在损失已越过 N 的每个读取步之后的那一步，'
     '在行的规则不偏向，所以进程在那里不锁定，不论份额如何。',
     [C + 'turned_by_loss']),
    ('The reading read from the share: where how the rule is read is formed from the share at the reading step (mind) and '
     'the rule read from the share through it (read), monotonically, the rule and its reading are one rule read from the '
     'share in the order of pairs; locked, none of share, rule and reading falls below where it was; a change of the '
     'reading, any size, either way, the rule still favouring, is absorbed at the next reading step.',
     '从份额读出的读法：规则怎样被读在读取步由份额形成（mind），规则经由它从份额读出（read），且都单调时，规则与其读法在对的序中'
     '合为一个从份额读出的规则；锁定时份额、规则与读法都不低于曾在之处；读法的改变，不论大小与方向，只要规则仍偏向，在下一读取步被吸收。',
     [C + 'both', C + 'readers', C + 'byRule', C + 'both_reads', C + 'byRule_raises', C + 'both_upper',
      C + 'readers_not_below', C + 'reading_absorbed']),
    ('Where the rule read favours at every reading and every share, every course is locked from the step after its '
     'second reading step, whatever rule and reading it starts with: within a loop whose every level reads only the '
     'share, what leaves is a change of the law, such as a level reading beyond the share.',
     '读出的规则在每个读法与每个份额都偏向时，每条进程自第二个读取步之后的那一步起锁定，不论从何种规则与读法开始：在每一层都只读份额的回路中，'
     '离开的是律的改变，例如读份额之外者的一层。',
     [C + 'readers_uniform_locks']),
    ('Witnesses: carriers two to one under a rule favouring them four to one, read at every step, each step adding one '
     'to the loss; read from the share alone the course is locked at every step, read from the loss the same selection '
     'from the same start favours the others from the second step and the share falls at the third. The reading formed '
     'as the share\'s own proportion meets every premise, and a reading reversed is absorbed.',
     '见证：承载者对其他二比一，规则偏向承载者四比一，每步读取，每步损失加一；只从份额读出，进程每一步都锁定；从损失读出，'
     '同一选择从同一起点自第二步起偏向其他，份额在第三步下降。读法形成为份额自身的比例时满足每个前提，被反转的读法被吸收。',
     [B + 'lossStep', B + 'closedRead', B + 'lossRead', B + 'closed', B + 'opened', B + 'closed_locked',
      B + 'lossRead_turns', B + 'open_turned', B + 'open_falls', B + 'open_reads', P + 'mind', P + 'read',
      P + 'readMono', P + 'formed', P + 'start_locked', P + 'reform_absorbed']),
]
for en, zh, _ in laws:
    assert len(en) <= 420 and len(zh) <= 190, (en[:40], len(en), len(zh))
all_named = {n for _, _, names in laws for n in resolve(MOD, names)}
missing = sorted(d['name'] for d in m['declarations'] if d['name'] not in all_named)
assert not missing, ('declarations no law names', missing)

RULE_DEP = dep('capture-through-the-rule', 'formal-reuse',
               'Applies Becoming.RuleCapture\'s laws (Raises, ReadsShare, Locked, locked_stays, locked_not_below, '
               'perturbation_absorbed, uniform_locks) to the share\'s own law joined with a step beyond, and to a rule paired '
               'with its reading; its counts (CarrierCounts, select, hi, lo, twoToOne) give the witnesses.',
               '把 Becoming.RuleCapture 的诸律（Raises、ReadsShare、Locked、locked_stays、locked_not_below、perturbation_absorbed、'
               'uniform_locks）用于带份额之外一步的份额自身之律，以及与其读法成对的规则；其计数（CarrierCounts、select、hi、lo、twoToOne）给出见证。',
               'The lock, its absorption of a change of the rule\'s value, and leaving only by a change of how the rule reads.',
               '锁定、它对规则之值改变的吸收，以及只有改变规则怎样读才离开。',
               'What the loop does not read, and the reading itself read from the share.',
               '回路不读的，以及本身从份额读出的读法。',
               'Raises, ReadsShare and favouring kept upward, as each statement names.',
               '各陈述所列的 Raises、ReadsShare 与向上保持的偏向。', src('RuleCapture'))
PACE_DEP = dep('how-fast-a-rule-may-change', 'formal-reuse',
               'Builds on Pace\'s two-level course (Pace.paced, Pace.turn, Pace.paced_succ, Pace.paced_fast_succ).',
               '建立在 Pace 的两速历程上（Pace.paced、Pace.turn、Pace.paced_succ、Pace.paced_fast_succ）。',
               'A two-level course whose rule changes only at reading steps.', '规则只在读取步改变的两速历程。',
               'A fast configuration that is a pair, and a rule that is a pair.', '为一对的快构形，以及为一对的规则。',
               'None.', '无。', src('Pace'))

rec = {
    'schema_version': 2, 'id': RID,
    'title': {'en': 'Closed capture: a loop whose every level reads only the share',
              'zh': '闭合的捕获：每一层都只读份额的回路'},
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': NOW,
    'statement': {
        'en': 'In a selection whose rule, and how the rule is read, are read from the share it selects, a loss the loop '
              'does not read leaves it locked however large it grows, and a change of the reading is absorbed; what '
              'leaves is a change of the law, such as a reading of what lies beyond the share.',
        'zh': '在规则及规则怎样被读都从所选出份额读出的选择中，回路不读的损失不论多大都使它保持锁定，读法的改变被吸收；离开的是律的改变，例如对份额之外者的读取。'},
    'laws': [{'en': en, 'zh': zh, 'declarations': resolve(MOD, names)} for en, zh, names in laws],
    'hypotheses': [{
        'en': 'No axiom. Each statement names its hypotheses: Unread (neither the next share nor the rule read reads what '
              'lies beyond); Accrues (each step adds at least one beyond); RuleCapture\'s Raises, ReadsShare and favouring '
              'kept upward; a locked start; for the readings, the reading formed monotonically from the share (ReadsShare '
              'on mind) and the rule read monotonically from the reading and the share.',
        'zh': '不加公理。各陈述列出其假设：Unread（下一份额与读出的规则都不读份额之外者）；Accrues（每步在份额之外至少加一）；'
              'RuleCapture 的 Raises、ReadsShare 与向上保持的偏向；锁定的起点；对读法，读法由份额单调形成（mind 上的 ReadsShare），'
              '规则由读法与份额单调读出。'}],
    'does_not_show': [
        {'en': 'That any actual rule, or how it is read, is formed from the share it selects: this is the premise '
               'ReadsShare, on the rule and on mind.',
         'zh': '任何实际的规则或其被读的方式由其所选出的份额形成：这是前提 ReadsShare，在规则上，也在 mind 上。',
         'kind': 'correspondence'},
        {'en': 'That what lies beyond the share is a loss to any formation: that is a significance\'s to say (section 6); '
               'here it is a count the loop does not read. Nor how fast it grows beyond one a step.',
         'zh': '份额之外者对任何形成是损失：这要由一种重要性来说（第 6 节）；在此它只是回路不读的一个计数。也不说它比每步一增长得多快。',
         'kind': 'non-implication'},
        {'en': 'That the readers are minds, institutions or a culture: that is a reading (D58).',
         'zh': '读者是心智、机构或文化：这是读法（D58）。', 'kind': 'correspondence'},
        {'en': 'Real-valued shares, noisy or partial readings, readings that read both the share and part of what lies '
               'beyond, and the calibration of any of this to the present world.',
         'zh': '实数份额、有噪声或部分的读取、既读份额又读份额之外一部分的读法，以及其中任何一项对当今世界的校准。',
         'kind': 'scope'}],
    'counterexamples': [{'path': src(MOD), 'detail': {
        'en': 'Without Unread the loop does not outlive its loss: the same selection from the same locked start, read from '
              'the loss instead of the share, favours the others from the second step and its share falls at the third '
              '(Beyond.open_turned, Beyond.open_falls).',
        'zh': '没有 Unread，回路不比其损失更持久：同一选择从同一锁定起点，改从损失而不从份额读出，自第二步起偏向其他，份额在第三步下降'
              '（Beyond.open_turned、Beyond.open_falls）。'}}],
    'standard_boundaries': BOUNDS,
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {n_decl} declarations of '
              f'Becoming.{MOD}, {n_thm} of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'Built and reviewed in one session, with no separate reviewer; author review in study section {N}; not '
              'independently reviewed by a person.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.{MOD} 的 {n_decl} 项声明（{n_thm} 项定理）公理报告为空；'
              f'检查器并核对核心纯净。在一个会话中构建并审查，没有另设审查者；作者审查见研究第 {N} 节；未经人的独立审查。'},
    'next_delta': {
        'en': 'Readings that read the share and part of what lies beyond, and how much of the loss a reading must read to '
              'leave; a loss read late; the reading formed by a selection among readers rather than by a map; real-valued '
              'shares; an independent review.',
        'zh': '既读份额又读份额之外一部分的读法，以及读法须读多少损失才离开；迟读的损失；由读者之间的选择而非由一个映射形成的读法；实数份额；独立审查。'},
    'correspondence': {
        'en': 'The meta-attractor (theories/meta-attractor): its 2025-08 formalisation separates the state and the rule that '
              'scores it, with the rule updated from the state; partial reform re-absorbed is perturbation_absorbed and '
              'reading_absorbed, and the metric surviving its own refutation is lock_outlives_loss. Goodhart (1975) says '
              'a measure made a target stops measuring; this states why it is kept: what keeps it reads the share it '
              'gives, not what it fails to measure. Lock-in under increasing returns (Arthur 1989) and regulatory capture '
              '(Stigler 1971) are the closest prior results; the delta is the reading itself read from the share, and '
              'the exact condition (Unread) under which a loss leaves the lock.',
        'zh': '元吸引子（theories/meta-attractor）：其 2025-08 形式化把状态与评分它的规则分开，规则由状态更新；局部改革被吸收即 '
              'perturbation_absorbed 与 reading_absorbed，度量在自身被驳倒后仍存即 lock_outlives_loss。Goodhart（1975）说成为目标的度量不再度量；'
              '本记录说明它为何被保留：保留它的读的是它给出的份额，不是它没能度量的。递增回报下的锁定（Arthur 1989）与规制俘获（Stigler 1971）'
              '是最近的先前结果；增量是读法本身从份额读出，以及损失离开锁定的确切条件（Unread）。'},
    'canonical_source': src(MOD),
    'aliases': ['closed capture', '闭合的捕获', 'the loop closed in its readings', 'the metric outlives its refutation',
                'the meta-attractor loop', '元吸引子回路',
                'Becoming.ClosedCapture.lock_outlives_loss', 'Becoming.ClosedCapture.reading_absorbed',
                'Becoming.ClosedCapture.turned_by_loss', 'Becoming.ClosedCapture.unread_course'],
    'dependencies': [RULE_DEP, PACE_DEP],
    'related': [
        {'id': 'capture-through-the-rule', 'detail': {
            'en': 'The loop this record closes: what it does not read, and the reading read from the share.',
            'zh': '本记录所闭合的回路：它不读的，以及从份额读出的读法。'}},
        {'id': 'target-capture', 'detail': {
            'en': 'The share that rises under selection, and the state re-absorbed where the step does not read it.',
            'zh': '在选择下上升的份额，以及步不读状态之处被吸收的状态。'}},
        {'id': 'joint-difference-making', 'detail': {
            'en': 'What lies beyond the share is drawn jointly; that the loop does not read it does not remove a drawer '
                  'from the drawing.',
            'zh': '份额之外者是被联合汲取的；回路不读它，并不使汲取者脱离汲取。'}}],
    'references': [{'path': src(MOD), 'role': 'proof', 'declarations': sorted(d['name'] for d in m['declarations']),
                    'sha256': sha(src(MOD))},
                   {'path': src('RuleCapture'), 'role': 'proof', 'sha256': sha(src('RuleCapture'))},
                   {'path': src('Pace'), 'role': 'proof', 'sha256': sha(src('Pace'))},
                   {'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
                   {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
                   {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
                   {'path': OPENING, 'role': 'statement', 'sha256': sha(OPENING)}],
    'proof_bindings': [{'source': src(MOD), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{MOD}',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': f'20 October 2026: added (MA1), the meta-attractor\'s loop closed on the spine: OPENING\'s note on the '
              f'meta-attractor said the loop was not on the spine; study section {N}; readings D58.',
        'zh': f'2026年10月20日：新增（MA1），元吸引子的回路在主干上闭合：OPENING 关于元吸引子的注说该回路不在主干上；研究第 {N} 节；读法 D58。'}],
}
assert len(rec['statement']['en']) <= 300, len(rec['statement']['en'])
path = RECORDS / f'{RID}.json'
assert not path.exists(), ('record exists', RID)
path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
print('written', RID, n_thm, n_decl)

# The record it continues.
p = RECORDS / 'capture-through-the-rule.json'
d = json.loads(p.read_text())
d['related'].append({'id': RID, 'detail': {
    'en': 'The loop closed: a loss it does not read leaves it locked, a reading of the loss leaves, and the reading read '
          'from the share is absorbed as the rule\'s value is.',
    'zh': '闭合的回路：它不读的损失使它保持锁定，读损失则离开，从份额读出的读法如规则之值一样被吸收。'}})
for r in d['references']:
    if r['path'] == CHAPTER:
        r['sha256'] = sha(CHAPTER)
d['history'].append({
    'en': f'20 October 2026, MA1: a third level, how the rule is read, formed from the share, and a loss the loop does '
          f'not read are stated in Becoming.ClosedCapture (record {RID}, study section {N}). The claim is unchanged.',
    'zh': f'2026年10月20日，MA1：第三层，即由份额形成的规则被读的方式，以及回路不读的损失，陈述于 Becoming.ClosedCapture（记录 {RID}，研究第 {N} 节）。论断不变。'})
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated', p.name)
