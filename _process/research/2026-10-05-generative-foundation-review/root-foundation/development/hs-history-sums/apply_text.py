#!/usr/bin/env python3
"""HS (19 October 2026): chapter (English and Chinese) and study text. Each edit must match exactly once.
Every count is read from the checker log and the connectivity output, so the edit holds on whatever main it relands on.
usage (from the checkout root): python3 -B apply_text.py SECTION MAIN_COMMIT RECEIPT CONNECTIVITY_LOG"""
import json
import re
import sys
from pathlib import Path

section, main_commit, RECEIPT, conn_path = sys.argv[1:5]
HERE = Path(__file__).resolve().parent
log = (HERE / 'checker-hs.log').read_text()
chk = json.loads(log[log.index('{'):log.rindex('}') + 1])
assert chk['status'] == 'passed'
craw = Path(conn_path).read_text()
conn = json.loads(craw[craw.index('{'):craw.rindex('}') + 1])
n_mod = len(chk['spine_theorems'])
n_thm = sum(chk['spine_theorems'].values())
n_closure = len(chk['core_closure'])
n_found = n_closure - n_mod
HS_THM = chk['spine_theorems']['Becoming.HistorySums']
receipt = json.loads(Path('experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
                          f'becoming-checks/{RECEIPT}/verification.json').read_text())
assert receipt['status'] == 'passed'
HS_DECLS = len(next(m for m in receipt['modules'] if m['module'] == 'Becoming.HistorySums')['declarations'])
APART = conn['classes']['apart: own vocabulary'] + conn['classes']['apart: prelude-only statement']
TOTAL = conn['spine_theorems']
assert TOTAL == n_thm, (TOTAL, n_thm)
HS_APART = conn['apart_by_module'].get('Becoming.HistorySums', [0])[0]
COMPONENTS = conn['components']['count']
OUTSIDE = len(conn['components']['theorems_outside_the_main_component'])
BOTH = conn['classes']['statement on both families']
fmt = '{:,}'.format
C = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md')
CZ = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md')
STUDY = Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md')
SLUG = f'{section}-sums-over-histories-by-support-horizon-and-exact-order-hs'
STUDY_LINK = f'../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#{SLUG}'
PKG_LINK = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
REVIEW_LINK = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/SSBX-REPOSITORY-REVIEW.md'
RECORD = 'sums-over-histories-by-support-horizon-and-order'
RECORD_LINK = f'[{RECORD}](../results/records/{RECORD}.md)'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


PARA = (
    '\n\n**Support, splitting, exact orders and the steps between.** Four laws of the sum over histories complete the two '
    f'modules above ([Becoming.HistorySums]({PKG_LINK}/Becoming/HistorySums.lean)). For every weighting that vanishes '
    'off the steps a possibility admits, reading what vanishes where the possibility\'s reading fails, the sum vanishes '
    'wherever possibility does not reach the reading (`Weights.transfer_zero_of_impossible`). The transfer over n + m '
    'steps is m steps of the transfer over n (`Weights.transfer_split`), and the weight along a joined course composes '
    'at the joint (`Weights.along_append`). The exact order i (`Weights.exactly`) reads order i through each step\'s '
    'ground part and order i − 1 through its response part. For every weighting it vanishes above the horizon '
    '(`Weights.exactly_above`); where alternatives commute it is the sum over the courses that take exactly i responses '
    '(`Weights.exactly_eq_courses`), the orders of `Becoming.Routes` are its partial sums '
    '(`Weights.within_eq_sum_exactly`) and the whole sum is the sum of all of them (`Weights.transfer_eq_sum_exactly`); '
    'for one configuration with ground weight one and response weight M it is `Loops.binom n i` · M^i '
    '(`Routes.SelfLoop.exactly_eq`). The weighting that keeps the first possible course in listed order satisfies every '
    'law of weights, but its alternatives do not commute, and there one step\'s sum is not the sum of its exact orders '
    '(`HistorySums.grouping_needs_commuting`). Two weightings that vanish off a possibility\'s steps and agree on each '
    'step that a course from a configuration passes on its way to where a reading holds have the same transfer '
    '(`Weights.transfer_between`). On a process whose steps the weights read, each law is a law of its traces '
    '(`Weights.transfer_zero_of_no_trace`, `HistorySums.trace_split_iff`, `HistorySums.exactly_trace`, '
    '`HistorySums.exactly_responses_trace`, `HistorySums.labelled_trace_iff`, `Weights.transfer_between_traces`). '
    '*Readings* [AI reading]. Support and `Interference.unseen` bound each other from either side: a weighting adds '
    'nothing where possibility has nothing, and possibility read from a weighting that cancels can see something where '
    'the weighting has nothing. An exact order regroups the alternatives by how many responses a course takes, so it '
    'needs them to commute; the cumulative orders keep the listed order and need nothing. The steps between are the '
    'coupling that carries, read off the courses with no prior order of cause and effect. The four laws were candidates '
    f'(W1–W4) in the [review of the exploratory repository]({REVIEW_LINK}). See {RECORD_LINK}.')

t = C.read_text()
t = once(t, 'the match is structural, and counting weights do not cancel.', 'the match is structural, and counting '
         'weights do not cancel.' + PARA)
t = once(t, 'laws reading only above a threshold or in other shapes; grouping by exactly i responses, signed carried '
            'differences and cancellation,',
         'laws reading only above a threshold or in other shapes; grouping by exactly i responses where alternatives do '
         'not commute (stated where they do, `Becoming.HistorySums`), signed carried differences and cancellation,')
t = once(t, '[orders-as-a-sum-over-histories](../results/records/orders-as-a-sum-over-histories.md), [how-loops-form]',
         f'[orders-as-a-sum-over-histories](../results/records/orders-as-a-sum-over-histories.md), {RECORD_LINK}, '
         '[how-loops-form]')
m = re.search(r'There are (\d+) dependency components, with (\d+) spine theorems outside the main one; (\d+) statements '
              r'use both families\.', t)
assert m and t.count(m.group(0)) == 1
t = t.replace(m.group(0),
              f'Rerun with HS (receipt {RECEIPT}), it counts {APART} of {fmt(TOTAL)}, {HS_APART} of {HS_THM} in '
              '`Becoming.HistorySums`: two witnesses that grouping by order needs commuting, the self-loop\'s exact '
              'orders, and the weight along a joined course, registered; each other law of the module is read on the '
              f'traces of a process. There are {COMPONENTS} dependency components, with {OUTSIDE} spine theorems '
              f'outside the main one; {BOTH} statements use both families.')
m = re.search(r'The \[current receipt\]\([^)]*becoming-verification\.json\) is run `[^`]+`.*? in the working tree\.', t)
assert m and t.count(m.group(0)) == 1
t = t.replace(m.group(0),
              f'The [current receipt]({PKG_LINK}/becoming-verification.json) is run `{RECEIPT}`, frozen in '
              f'[`becoming-checks/{RECEIPT}/`]({PKG_LINK}/becoming-checks/{RECEIPT}/verification.json). It was checked '
              f'with Lean 4.29.1 on main {main_commit} with HS (`Becoming.HistorySums`, [study §{section}]({STUDY_LINK})) '
              'in the working tree.')
for pattern, new in [
        (r'with the package\'s base and four layers: \d+ modules counting the root `Becoming`, and \d+ in the core '
         r'closure with the foundation\.',
         f'with the package\'s base and four layers: {n_mod} modules counting the root `Becoming`, and {n_closure} in '
         'the core closure with the foundation.'),
        (r'\| Core modules \(with the root `Becoming`, 0 theorems\) \| [\d,]+ modules, [\d,]+ theorems \|',
         f'| Core modules (with the root `Becoming`, 0 theorems) | {n_mod} modules, {fmt(n_thm)} theorems |'),
        (r'\| Core closure \| [\d,]+ modules, [\d,]+ theorems \|',
         f'| Core closure | {n_closure} modules, {fmt(n_thm + 74)} theorems |'),
        (r'\| Spine \(the core; no bridge since the F3 sweep\) \| [\d,]+ theorems \|',
         f'| Spine (the core; no bridge since the F3 sweep) | {fmt(n_thm)} theorems |'),
        (r'\| Audited spine declarations \| [\d,]+ \|', f'| Audited spine declarations | {fmt(chk["spine_declaration_audits"])} |'),
        (r'\| Modules in the compile order \| [\d,]+ \|', f'| Modules in the compile order | {n_closure} |'),
        (r'\| Generated `injEq` lemmas on `propext` \| \d+ in the core closure \|',
         f'| Generated `injEq` lemmas on `propext` | {chk["generated_with_axioms"]} in the core closure |'),
        (r'- That run reused [\d,]+ cached Lean steps from `~/\.cache/becoming-lean` and ran \d+\.',
         f'- That run reused {fmt(chk["lean_steps_reused"])} cached Lean steps from `~/.cache/becoming-lean` and ran '
         f'{chk["lean_steps_run"]}.')]:
    found = re.findall(pattern, t)
    assert len(found) == 1, (pattern, found)
    t = re.sub(pattern, lambda _: new, t)
assert n_found == 3 and '| Foundation modules | 3 modules, 74 theorems |' in t
C.write_text(t)

ZPARA = (
    '\n\n**历史之和的支撑、拆分、确切阶与其间之步。** 历史之和的四条律补足上面两个模块'
    f'（[Becoming.HistorySums]({PKG_LINK}/Becoming/HistorySums.lean)）。对每一种在可能性所容之步以外为零、所读在可能性之读'
    '不成立处为零的权重，历史之和在可能性达不到所读之处为零（`Weights.transfer_zero_of_impossible`）。n + m 步的转移是 n 步'
    '之转移的 m 步（`Weights.transfer_split`），拼接历程上的权重在接点处复合（`Weights.along_append`）。确切的 i 阶'
    '（`Weights.exactly`）跨每步由基础部分读 i 阶、由回应部分读 i − 1 阶。对每一种权重它在视界之上为零'
    '（`Weights.exactly_above`）；选项可交换时它是恰取 i 次回应的历程之和（`Weights.exactly_eq_courses`），'
    '`Becoming.Routes` 的各阶是它的部分和（`Weights.within_eq_sum_exactly`），整个和是所有确切阶之和'
    '（`Weights.transfer_eq_sum_exactly`）；一个构形、基础权重一、回应权重 M 时它是 `Loops.binom n i` · M^i'
    '（`Routes.SelfLoop.exactly_eq`）。保留按列出次序第一个可能历程的权重满足权重的每条律，但其选项不可交换，那里一步的和'
    '不是其各确切阶之和（`HistorySums.grouping_needs_commuting`）。两种在可能性之步以外为零、且在从一个构形到所读成立处的'
    '历程所经的每一步上一致的权重，转移相同（`Weights.transfer_between`）。在步由权重读出的进程上，每条律都是其迹的律'
    '（`Weights.transfer_zero_of_no_trace`、`HistorySums.trace_split_iff`、`HistorySums.exactly_trace`、'
    '`HistorySums.exactly_responses_trace`、`HistorySums.labelled_trace_iff`、`Weights.transfer_between_traces`）。'
    '读法〔AI 读法〕：支撑与 `Interference.unseen` 从两侧互为界：权重不在可能性一无所有处添加什么，而从会相消的权重读出的'
    '可能性可在权重一无所有处看到什么。确切阶按历程取几次回应重组选项，所以需要它们可交换；累积的阶保持列出次序，什么也不'
    f'需要。其间之步就是承载的耦合，由历程读出，不预设因果次序。四条律是[对探索性仓库的评审]({REVIEW_LINK})中的候选（W1–W4）。'
    f'见 {RECORD_LINK}。')
ZBULLET = ('- **历史之和的支撑、拆分、确切阶与其间之步。** 在可能性之步以外为零的权重在可能性达不到处和为零'
           '（`Weights.transfer_zero_of_impossible`）；转移在每个视界拆分（`Weights.transfer_split`）；选项可交换时 i 阶是'
           '恰有 i 次回应的历程之和，`Becoming.Routes` 的各阶是其部分和（`Weights.exactly_eq_courses`、'
           '`Weights.within_eq_sum_exactly`），不可交换时分组可以失败（`HistorySums.grouping_needs_commuting`）；'
           '所携带的只依赖其间之步（`Weights.transfer_between`）；每条律都在进程的迹上读出。')
z = CZ.read_text()
z = once(z, '对应是结构的，计数的权重不相消。\n', '对应是结构的，计数的权重不相消。' + ZPARA + '\n')
lines = z.split('\n')
at = [i for i, line in enumerate(lines) if line.startswith('- **携带差别的阶作为历史之和。**')]
assert len(at) == 1, at
lines.insert(at[0] + 1, ZBULLET)
CZ.write_text('\n'.join(lines))

s = STUDY.read_text()
body = (HERE / 'study_hs.txt').read_text().replace('## {N}.', f'## {section}.', 1)
conn_text = (f'connectivity check passes, {APART} apart of {fmt(TOTAL)}, {HS_APART} of {HS_THM} in the module (two '
             'model witnesses for commuting, the self-loop\'s exact orders and the list law along_append, registered)')
for key, value in (('{RECEIPT}', RECEIPT), ('{THEOREMS}', str(HS_THM)),
                   ('{DECLS}', str(HS_DECLS)),
                   ('{CONNECTIVITY}', conn_text)):
    assert key in body, key
    body = body.replace(key, value)
assert not s.rstrip('\n').endswith(body.rstrip('\n'))
STUDY.write_text(s.rstrip('\n') + '\n\n' + body.rstrip('\n') + '\n')
print('applied')
