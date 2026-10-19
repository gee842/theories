#!/usr/bin/env python3
"""U5 (19 October 2026): attach the base readings to the records whose laws they read:
python3 -B make_records.py CORE_RECEIPT SECTION   (from the checkout root)

The receipt is checked against the current bytes of every module cited, and every declaration cited against the
receipt's audited list, before anything is written. SECTION is the study section number U5 lands as."""
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
RECORDS = ROOT / 'theories/becoming/results/records'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
core_id, section = sys.argv[1], sys.argv[2]
SLUG = f'{section}-general-laws-read-on-the-base-joint-plans-inspection-narrowing-and-the-histories-of-words-u5'
core_receipt = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / core_receipt).read_text())
assert core['status'] == 'passed'
MODS = {m['module']: m for m in core['modules']}


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def src(module):
    path = f'{PKG}/Becoming/{module}.lean'
    assert core['source_sha256'][f'Becoming.{module}'] == sha(path), f'receipt does not bind {module}'
    assert not any(MODS[f'Becoming.{module}']['axiom_dependencies'].values()), module
    return path


def decls(module, *names):
    have = {d['name'] for d in MODS[f'Becoming.{module}']['declarations']}
    out = ['Becoming.' + n for n in names]
    missing = [n for n in out if n not in have]
    assert not missing, missing
    return out


def count(module):
    ds = MODS[f'Becoming.{module}']['declarations']
    return len(ds), sum(1 for d in ds if d.get('kind') == 'theorem')


def binding(path, module):
    return {'source': path, 'receipt': core_receipt, 'sha256_pointer': f'/source_sha256/Becoming.{module}',
            'success_pointer': '/status', 'success_value': 'passed'}


def receipt_ref(r):
    if not any(ref['path'] == core_receipt for ref in r['references']):
        r['references'].append({'path': core_receipt, 'role': 'receipt', 'sha256': sha(core_receipt),
                                'declarations': []})


def study_ref(r):
    if not any(ref['path'] == STUDY for ref in r['references']):
        r['references'].append({'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY), 'declarations': []})


def add_proof(r, module, names):
    """Add a proof reference for a new module, with the receipt and its binding."""
    path = src(module)
    assert not any(ref['path'] == path for ref in r['references'])
    r['references'].append({'path': path, 'role': 'proof', 'sha256': sha(path), 'declarations': names})
    receipt_ref(r)
    r['proof_bindings'].append(binding(path, module))


def repoint(r, module, extra=()):
    """Re-point an existing proof reference to the module's current bytes and receipt."""
    path = src(module)
    refs = [ref for ref in r['references'] if ref['path'] == path]
    assert len(refs) == 1, (r['id'], module, len(refs))
    refs[0]['sha256'] = sha(path)
    for name in extra:
        if name not in refs[0]['declarations']:
            refs[0]['declarations'].append(name)
    bound = [b for b in r['proof_bindings'] if b['source'] == path]
    assert bound, (r['id'], module)
    for b in bound:
        b['receipt'] = core_receipt
    receipt_ref(r)


def alias(r, *names):
    for a in names:
        if a not in r['aliases']:
            r['aliases'].append(a)


def load(i):
    return json.loads((RECORDS / f'{i}.json').read_text())


def save(r):
    (RECORDS / f"{r['id']}.json").write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print(r['id'])


SOURCE = f'{STUDY}#{SLUG}'

# (1) Joint plans and undertakings on the world's moves.
fw_n, fw_t = count('FrontierWorlds')
r = load('practical-judgment-g0-j')
r['reviewed_at_utc'] = NOW
fw_new = decls('FrontierWorlds', 'FrontierWorlds.Gives', 'FrontierWorlds.sole_giver_required',
               'FrontierWorlds.giver_active', 'FrontierWorlds.sole_giver_active', 'FrontierWorlds.Discharged',
               'FrontierWorlds.Residual', 'FrontierWorlds.Discharged.no_residual',
               'FrontierWorlds.residual_of_unfulfilled')
repoint(r, 'FrontierWorlds', fw_new)
alias(r, 'Becoming.FrontierWorlds.sole_giver_required', 'Becoming.FrontierWorlds.Discharged.no_residual')
r['progress'].append({
    'en': 'Assignment and discharge read in a world (U5): the joint plan at a step is the world\'s move, a relatum '
          'assigned the giving to a condition where it takes part and gives to it. Where a formation requires the '
          'condition at some step, someone gives at each such step and only one relatum does, its giving is required '
          '(sole_giver_required), and where only active formations give it is active there (sole_giver_active); an '
          'undertaking to give to what a formation requires is discharged where at every required step it is given or '
          'the formation no longer acts, and leaves no residual step (Discharged.no_residual).',
    'zh': '在世界中读分派与了结（U5）：一步的联合计划即世界在该步的移动，某关系项参与并给予某条件，即被分派给予该条件。'
          '某构成在某步要求该条件、每个这样的步都有给予者且只有一个关系项给予时，它的给予是被要求的（sole_giver_required）；'
          '在只有活跃者给予之处，它在那里活跃（sole_giver_active）；给予某构成所求的担当，若在每个被要求之步都有给予、'
          '或该构成不再活跃，则了结，不留余欠之步（Discharged.no_residual）。',
    'source': SOURCE})
study_ref(r)
old_en, old_zh = r['validation_scope']['en'], r['validation_scope']['zh']
assert old_en.count('FrontierWorlds, 3)') == 1 and old_zh.count('FrontierWorlds 3 项') == 1, (old_en, old_zh)
r['validation_scope']['en'] = old_en.replace('FrontierWorlds, 3)', f'FrontierWorlds, {fw_t} since U5)')
r['validation_scope']['zh'] = old_zh.replace('FrontierWorlds 3 项', f'FrontierWorlds {fw_t} 项（U5 起）')
assert len(r['validation_scope']['en']) <= 600 and len(r['validation_scope']['zh']) <= 260
r['history'].append({
    'en': f'19 October 2026, U5 (study section {section}): FrontierWorlds gains the assignment and discharge laws of '
          'Frontier read on the world\'s moves (sole giver required and active; discharge leaves no residual step); its '
          f'proof reference and binding move to core receipt {core_id}. The statement and the warrant of the commitments '
          'are unchanged.',
    'zh': f'2026年10月19日，U5（研究第 {section} 节）：FrontierWorlds 新增在世界移动上读出的 Frontier 分派与了结规律'
          f'（唯一给予者被要求且活跃；了结不留余欠之步）；其证明引用与绑定移到核心回执 {core_id}。陈述与承诺的根据不变。'})
save(r)

# (2) Inspection by fallible witnesses, for every roster.
wr = decls('WitnessRefinementRuns', 'WitnessRefinementRuns.inspection', 'WitnessRefinementRuns.testing',
           'WitnessRefinementRuns.mem_step', 'WitnessRefinementRuns.silent_step',
           'WitnessRefinementRuns.step_certificate_candidate', 'WitnessRefinementRuns.complete_step_agrees',
           'WitnessRefinementRuns.complete_run_agrees', 'WitnessRefinementRuns.responsive_step_excludes',
           'WitnessRefinementRuns.covering_step_keeps_both', 'WitnessRefinementRuns.diagnosable_iff',
           'WitnessRefinementRuns.doubled_roster_same', 'WitnessRefinementRuns.total_fault_blocks',
           'WitnessRefinementRuns.test_emptied', 'WitnessRefinementRuns.test_step_completes',
           'WitnessRefinementRuns.audit_step_inspection', 'WitnessRefinementRuns.inquiry_step_testing')
wr_n, wr_t = count('WitnessRefinementRuns')
r = load('fallible-witness-diagnosability')
r['reviewed_at_utc'] = NOW
add_proof(r, 'WitnessRefinementRuns', wr)
study_ref(r)
r['claim']['en'] += (' Read on the process of inspection for every roster (Becoming.WitnessRefinementRuns), two '
                     'candidates with different answers are told apart by every step on a complete transcript exactly '
                     'where their envelopes are CrossSeparated (diagnosable_iff), and once a complete transcript is read, '
                     'remaining cross-separated candidates agree at every later state (complete_run_agrees).')
r['claim']['zh'] += ('在对每个名册的检视过程上读（Becoming.WitnessRefinementRuns）：答案不同的两个候选，恰在其故障集合族 '
                     'CrossSeparated 时被完整报告上的每一步分开（diagnosable_iff）；读过一份完整报告后，留下的交叉分离候选在此后'
                     '每个状态都一致（complete_run_agrees）。')
alias(r, 'Becoming.WitnessRefinementRuns.diagnosable_iff', 'Becoming.WitnessRefinementRuns.complete_run_agrees',
      'inspection by fallible witnesses as a process', '可失实见证的检视过程')
r['history'].append({
    'en': f'19 October 2026, U5 (study section {section}): the roster laws of WitnessRefinement, FaultEnvelopes and '
          'PooledEnvelopes read on the processes of inspection and testing for every roster, fault sets and answers '
          f'(Becoming.WitnessRefinementRuns, {wr_t} theorems, core receipt {core_id}); the audit and the inquiry move '
          'their candidates by them. Two sentences added to the claim; the earlier claim is unchanged.',
    'zh': f'2026年10月19日，U5（研究第 {section} 节）：WitnessRefinement、FaultEnvelopes 与 PooledEnvelopes 的名册规律，'
          f'在对每个名册、故障集合与答案的检视与检验过程上读出（Becoming.WitnessRefinementRuns，{wr_t} 项定理，核心回执 '
          f'{core_id}）；审计与探询按它们移动候选。论断添两句，原论断不变。'})
save(r)

# (3) Narrowing along the runs of the pure observation.
nr = decls('NarrowingRuns', 'NarrowingRuns.SafeFor', 'NarrowingRuns.GreatestFor', 'NarrowingRuns.settles_iff_answer',
           'NarrowingRuns.narrowed_answer_greatest', 'NarrowingRuns.narrowed_answer_unique',
           'NarrowingRuns.narrowed_answer_unique_of_ext', 'NarrowingRuns.run_constant', 'NarrowingRuns.record',
           'NarrowingRuns.run_kept', 'NarrowingRuns.run_answer_correct', 'NarrowingRuns.run_answer_greatest',
           'NarrowingRuns.transport_settles_iff')
nr_n, nr_t = count('NarrowingRuns')
r = load('becoming-spine-instances')
r['reviewed_at_utc'] = NOW
add_proof(r, 'NarrowingRuns', nr)
study_ref(r)
alias(r, 'Becoming.NarrowingRuns.narrowed_answer_greatest', 'Becoming.NarrowingRuns.run_answer_greatest')
r['history'].append({
    'en': f'19 October 2026, U5 (study section {section}): the answer laws of Narrowing read on the belief After narrows '
          'on the pure observation and along its runs (Becoming.NarrowingRuns, '
          f'{nr_t} theorems, core receipt {core_id}): the answer is the greatest safe answer of the narrowed belief, the '
          'only one; along every run observing a candidate rule it asserts the observed rule\'s values; re-encoding '
          'transports what the belief settles. The claim is unchanged.',
    'zh': f'2026年10月19日，U5（研究第 {section} 节）：Narrowing 的回答规律在纯观察上由 After 收窄的信念及其运行上读出'
          f'（Becoming.NarrowingRuns，{nr_t} 项定理，核心回执 {core_id}）：回答是收窄信念唯一的最大安全回答；沿每个观察'
          '候选规则的运行，它所断言的是所观察规则的值；重新编码搬运信念所定者。论断不变。'})
save(r)

# (4) The word half of HistoryIdeals on the courses a process can take.
ht = decls('HistoryIdealsTraces', 'HistoryIdealsTraces.HistoryOf', 'HistoryIdealsTraces.classification',
           'HistoryIdealsTraces.course_settles', 'HistoryIdealsTraces.run_initial_trace',
           'HistoryIdealsTraces.run_goesOn')
ht_n, ht_t = count('HistoryIdealsTraces')
witness = decls('HistoryIdealsTraces', 'HistoryIdealsTraces.countdown', 'HistoryIdealsTraces.history_without_run')
r = load('a-history-read-off-its-finite-stretches')
r['reviewed_at_utc'] = NOW
add_proof(r, 'HistoryIdealsTraces', ht + witness)
study_ref(r)
r['laws'].append({
    'en': 'The word half on the courses a process can take: an ideal of courses feasible from a configuration that '
          'settles, or goes on with a course of each length picked, is a history of the process from there (one feasible '
          'course, or a sequence of moves each of whose initial courses is feasible); a feasible course settles; a run\'s '
          'moves go on, each initial course the trace of its first steps.',
    'zh': '词的一半读在过程能走的进程上：从某构形可行之进程的理想，止定、或取定每个长度的进程而继续，即过程从那里的历史'
          '（一个可行进程，或每个初始进程都可行的移动序列）；可行进程止定；运行的移动继续，每个初始进程都是其最初各步的踪迹。',
    'declarations': ht})
r['counterexamples'].append({
    'path': f'{PKG}/Becoming/HistoryIdealsTraces.lean',
    'detail': {
        'en': 'A history of feasible courses need not be a run\'s moves: from no configuration the countdown goes to any '
              'count and then counts down, so every course of ()s is feasible from there, and no run starts there '
              '(history_without_run).',
        'zh': '可行进程的历史不必是某运行的移动：倒数过程从无构形可去任何计数再逐一倒数，故从那里每个由 () 组成的进程都可行，'
              '却没有运行从那里开始（history_without_run）。'}})
alias(r, 'Becoming.HistoryIdealsTraces.classification', 'Becoming.HistoryIdealsTraces.history_without_run')
r['history'].append({
    'en': f'19 October 2026, U5 (study section {section}): the word half read on the courses a process can take '
          f'(Becoming.HistoryIdealsTraces, {ht_t} theorems, core receipt {core_id}); one law and one counterexample added '
          '(a history of feasible courses that is no run\'s moves). The statement and the earlier laws are unchanged.',
    'zh': f'2026年10月19日，U5（研究第 {section} 节）：词的一半读在过程能走的进程上（Becoming.HistoryIdealsTraces，'
          f'{ht_t} 项定理，核心回执 {core_id}）；新增一条规律与一个反例（不是任何运行之移动的可行进程历史）。陈述与原规律不变。'})
save(r)
print('written', fw_t, wr_t, nr_t, ht_t)
