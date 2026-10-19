#!/usr/bin/env python3
"""U5 (19 October 2026): chapter (English and Chinese) and study text. Each edit must match exactly once.
Every count is read from the checker log and the connectivity outputs, so the edit holds on whatever main it relands on.
usage (from the checkout root): python3 -B apply_text.py SECTION MAIN_COMMIT RECEIPT CONNECTIVITY_JSON BEFORE_JSON"""
import json
import re
import sys
from pathlib import Path

section, main_commit, RECEIPT, conn_path, before_path = sys.argv[1:6]
HERE = Path(__file__).resolve().parent
log = (HERE / 'checker-u5.log').read_text()
chk = json.loads(log[log.index('{'):log.rindex('}') + 1])
assert chk['status'] == 'passed'
conn = json.loads(Path(conn_path).read_text())
before = json.loads(Path(before_path).read_text())
n_mod = len(chk['spine_theorems'])
n_thm = sum(chk['spine_theorems'].values())
n_closure = len(chk['core_closure'])
apart = lambda c: c['classes']['apart: own vocabulary'] + c['classes']['apart: prelude-only statement']
APART, TOTAL = apart(conn), conn['spine_theorems']
B_APART, B_TOTAL = apart(before), before['spine_theorems']
assert TOTAL == n_thm, (TOTAL, n_thm)
REMOVED = len(conn['register_entries_not_apart_roots'])
COMPONENTS = conn['components']['count']
OUTSIDE = len(conn['components']['theorems_outside_the_main_component'])
BOTH = conn['classes']['statement on both families']
fmt = '{:,}'.format
C = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md')
CZ = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md')
STUDY = Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md')
SLUG = f'{section}-general-laws-read-on-the-base-joint-plans-inspection-narrowing-and-the-histories-of-words-u5'
STUDY_LINK = f'../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#{SLUG}'
PKG_LINK = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
MOD = lambda m: f'[Becoming.{m}]({PKG_LINK}/Becoming/{m}.lean)'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


t = C.read_text()
# Premise card F: J3 on a world's moves.
t = once(t, 'read on a frame by `FrontierFrames.Priority` and `FrontierFrames.Options` (core; empty axiom reports) |',
         'read on a frame by `FrontierFrames.Priority` and `FrontierFrames.Options`, and J3\'s assignment and discharge on '
         'a world\'s moves by `FrontierWorlds` (core; empty axiom reports) |')
# Section 3: the word half on the courses a process can take.
old = ('a continuous reading of the histories is fixed at every run by its values on the finite ones '
       '(`Stretches.histories_representation`, `Stretches.run_reading_unique`).')
t = once(t, old, old + ' Read by its moves alone, a history of a process is a course it can take, or a sequence of moves '
         'each of whose initial courses it can take: an ideal of feasible courses that settles, or goes on with its courses '
         'picked, is such a history, and a run\'s moves go on (' + MOD('HistoryIdealsTraces') + ', `classification`, '
         '`run_goesOn`). The converse fails: in a process that from no configuration goes to any count and then counts '
         'down, every course of `()`s is feasible and no run starts there (`history_without_run`). Reading a history by '
         'its moves omits whether some configuration continues every course.')
# Section 3: narrowing along the runs of the pure observation.
old = ('Refining observation narrows belief, so it preserves them (`commonResponse_antitone`; the periphery bridge '
       '[CorrectionInquiry](../../../experiments/integrated-correction/general-framework/generative-basis/lean/'
       'universal-ethics/generative-capacity/CorrectionInquiry.lean), with no axioms).')
t = once(t, old, old + ' Narrowing a list of candidate rules by an observation is `After` on the pure observation '
         '(`Narrowing.revise_is_after`); on the belief so narrowed, the answer of the learned list is safe and, where '
         'the belief holds a rule, the greatest safe answer and the only one, and along every run observing a candidate '
         'rule it asserts only the observed rule\'s values (' + MOD('NarrowingRuns') + ', `narrowed_answer_greatest`, '
         '`run_answer_greatest`; [becoming-spine-instances](../results/records/becoming-spine-instances.md)).')
# Section 6: the practical commitments in a world.
old = ('keeping them is required of the choice where decided (`FrontierFrames.Priority.kept_required`) '
       '([practical-judgment-g0-j](../results/records/practical-judgment-g0-j.md)).')
t = once(t, old, old + ' In a world, J3\'s joint plan at a step is the world\'s move: where a formation requires a '
         'condition, someone gives to it at each such step and only one relatum does, that relatum\'s giving is required, '
         'and where only active formations give it is active there; an undertaking to give to what a formation requires '
         'is discharged where at every required step it is given or the formation no longer acts '
         '(`FrontierWorlds.sole_giver_required`, `FrontierWorlds.sole_giver_active`, '
         '`FrontierWorlds.Discharged.no_residual`; reading the plan as the move is the AI\'s).')
# Section 4: evidence under fallible witnesses, for every roster.
old = ('complete diagnosability under fallible witnesses ([fallible-witness-diagnosability](../results/records/'
       'fallible-witness-diagnosability.md)).')
t = once(t, old, old[:-2] + '), read on the process of inspection for every roster: two candidates are told apart by '
         'every step on a complete transcript exactly where their fault envelopes are cross-separated, a model admitting '
         'every witness\'s failure is kept by every step and blocks every later certificate, and the audit and the '
         'inquiry move their candidates by it (' + MOD('WitnessRefinementRuns') + ', `diagnosable_iff`, '
         '`total_fault_blocks`).')
# Section 8.2: the integration row.
old = ' The two course worlds are two readings of one flow and one web, defined once.'
t = once(t, old, f' Rerun with U5 (receipt {RECEIPT}), it counts {APART} of {fmt(TOTAL)} ({B_APART} of '
         f'{fmt(B_TOTAL)} before), none in `Becoming.WitnessRefinementRuns`, `Becoming.NarrowingRuns`, '
         '`Becoming.HistoryIdealsTraces` or `Becoming.FrontierWorlds`: the groups study section 196 left apart as general '
         'structure without a base object are stated on the base, joint plans and undertakings on a world\'s moves, the '
         'roster laws on the process of inspection for every roster, the safe and greatest answer on the belief narrowed '
         f'on the pure observation and its runs, and the word half on the courses a process can take; {REMOVED} apart '
         'roots are now used on the base and left the register, and what stays apart in these modules is model witnesses '
         f'and support ([study section {section}]({STUDY_LINK})); {COMPONENTS} dependency components, {OUTSIDE} spine '
         f'theorems outside the main one, {BOTH} statements on both families.' + old)
# Section 9: the receipt and the counts.
m = re.search(r'The \[current receipt\]\([^)]*becoming-verification\.json\) is run `[^`]+`.*? in the working tree\.', t)
assert m and t.count(m.group(0)) == 1
t = t.replace(m.group(0),
              f'The [current receipt]({PKG_LINK}/becoming-verification.json) is run `{RECEIPT}`, frozen in '
              f'[`becoming-checks/{RECEIPT}/`]({PKG_LINK}/becoming-checks/{RECEIPT}/verification.json). It was checked '
              f'with Lean 4.29.1 on main {main_commit} with U5 (`Becoming.WitnessRefinementRuns`, `Becoming.NarrowingRuns`, '
              '`Becoming.HistoryIdealsTraces`, and new theorems in `Becoming.FrontierWorlds`, '
              f'[study §{section}]({STUDY_LINK})) in the working tree.')
for pattern, new in [
        (r'\| Core modules \(with the root `Becoming`, 0 theorems\) \| [\d,]+ modules, [\d,]+ theorems \|',
         f'| Core modules (with the root `Becoming`, 0 theorems) | {n_mod} modules, {fmt(n_thm)} theorems |'),
        (r'\| Core closure \| [\d,]+ modules, [\d,]+ theorems \|',
         f'| Core closure | {n_closure} modules, {fmt(n_thm + 74)} theorems |'),
        (r'\| Spine \(the core; no bridge since the F3 sweep\) \| [\d,]+ theorems \|',
         f'| Spine (the core; no bridge since the F3 sweep) | {fmt(n_thm)} theorems |'),
        (r'\| Audited spine declarations \| [\d,]+ \|', f'| Audited spine declarations | {fmt(chk["spine_declaration_audits"])} |'),
        (r'\| Modules in the compile order \| [\d,]+ \|', f'| Modules in the compile order | {n_closure} |'),
        (r'- That run reused [\d,]+ cached Lean steps from `~/\.cache/becoming-lean` and ran \d+\.',
         f'- That run reused {fmt(chk["lean_steps_reused"])} cached Lean steps from `~/.cache/becoming-lean` and ran '
         f'{chk["lean_steps_run"]}.')]:
    found = re.findall(pattern, t)
    assert len(found) == 1, (pattern, found)
    t = re.sub(pattern, lambda _: new, t)
assert '| Foundation modules | 3 modules, 74 theorems |' in t
C.write_text(t)

z = CZ.read_text()
z = once(z, '在框架上由 `FrontierFrames.Priority` 与 `FrontierFrames.Options` 读出（核心；公理报告为空） |',
         '在框架上由 `FrontierFrames.Priority` 与 `FrontierFrames.Options` 读出，J3 的分派与了结由 `FrontierWorlds` '
         '在世界的移动上读出（核心；公理报告为空） |')
old = ('可错见证下的完整可诊断性（[fallible-witness-diagnosability](../results/records/'
       'fallible-witness-diagnosability.md)）。')
z = once(z, old, old[:-1] + '，并在对每个名册的检视过程上读出：答案不同的两个候选，恰在其故障集合族交叉分离时被完整报告上的每一步分开；'
         '允许全部见证失实的模型被每一步保留，并阻断此后的每个证书；审计与探询按此过程移动候选（' + MOD('WitnessRefinementRuns')
         + '，`diagnosable_iff`、`total_fault_blocks`）。')
m = re.search(r'\*\*判断即一步探究。\*\*[^\n]*', z)
assert m and z.count(m.group(0)) == 1
z = z.replace(m.group(0), m.group(0) + '\n\n**沿纯观察收窄。** 以一次观察收窄候选规则的列表，即纯观察上的 After'
              '（`Narrowing.revise_is_after`）。在如此收窄的信念上，所学列表的回答是安全的；信念持有规则时，它是最大的安全回答，且唯一；'
              '沿每个观察某候选规则的运行，它只断言所观察规则的值（' + MOD('NarrowingRuns') + '，`narrowed_answer_greatest`、'
              '`run_answer_greatest`）。\n\n**只按移动读历史。** 只按移动读，过程的一个历史是它能走的一个进程，或每个初始进程都可走的移动序列：'
              '可行进程的理想止定、或取定其进程而继续，即是这样的历史，运行的移动继续（' + MOD('HistoryIdealsTraces')
              + '，`classification`、`run_goesOn`）。反之不然：从无构形可去任何计数、再逐一倒数的过程中，每个由 `()` 组成的进程都可行，'
              '却没有运行从那里开始（`history_without_run`）。只按移动读历史，略去的是有没有构形接续每个进程。')
C.write_text(t)
CZ.write_text(z)

s = STUDY.read_text()
body = (HERE / 'study_u5.txt').read_text().replace('## 200.', f'## {section}.', 1)
for key, value in (('{RECEIPT}', RECEIPT), ('{APART}', str(APART)), ('{TOTAL}', fmt(TOTAL)),
                   ('{BEFORE_APART}', str(B_APART)), ('{BEFORE_TOTAL}', fmt(B_TOTAL)),
                   ('{ROOTS_REMOVED}', str(REMOVED))):
    assert key in body, key
    body = body.replace(key, value)
assert not s.rstrip('\n').endswith(body.rstrip('\n'))
STUDY.write_text(s.rstrip('\n') + '\n\n' + body.rstrip('\n') + '\n')
print('applied', APART, TOTAL, B_APART, B_TOTAL, REMOVED)
