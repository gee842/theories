#!/usr/bin/env python3
"""R28: the text of the two records the one base advances (run after rebind.py, from the checkout root).

* worlds-are-runs: the statement says a world is a run by its type; a law for the definition is added; the
  boundary "worlds are still defined without processes" is removed (now shown); the measurement boundary,
  the validation scope and the next step follow R28.
* recurrence-without-premise: a law says that a determined law's notions are its process's, with the five
  unfolding lemmas; the validation scope names R28's receipt.
Idempotent: a record already advanced is left as it is.
"""
import json
from datetime import datetime, timezone

RID = '20261019T181519.226999Z'
NOW = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
R = 'theories/becoming/results/records/'


def load(i):
    return json.load(open(R + i + '.json'))


def save(i, d):
    open(R + i + '.json', 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')


d = load('worlds-are-runs')
if not d['statement']['en'].startswith('A world is a run by its type'):
    d['statement'] = {
        'en': 'A world is a run by its type: its history is a run of every step on its webs and exchanges, and exactly a run of the law they show, and every run on webs and exchanges is a world; a world balances exactly where that run follows the law of exchange, as each does with the rest counted.',
        'zh': '世界按其类型就是运行：其历史是网与交换上每一步的运行，恰是它们所显之律的运行，网与交换上的每个运行都是世界；世界恰在这个运行遵从交换之律处平衡，计入其余时总是如此。'}
    d['laws'].insert(0, {
        'en': 'A world is one kind of relatum and its history, a run of the process admitting every step, whose configurations are its webs at each step and whose moves are its relata\'s exchanges; its web and flow read the history along the steps, a web being a dependence read along them, and a world built from a flow and a web has them back by rfl.',
        'zh': '世界是一种关系项及其历史：容许每一步之过程的运行，构形是各步的网，移动是关系项的交换；它的网与流是沿步读出的历史，网是沿步读的依存；由流与网构造的世界以 rfl 给回它们。',
        'declarations': ['Becoming.Dependence', 'Becoming.everyStep', 'Becoming.World.web', 'Becoming.World.flow',
                         'Becoming.World.of', 'Becoming.World.of_web', 'Becoming.World.of_flow', 'Becoming.World.run_history']})
    old = d['does_not_show']
    assert old[0]['en'].startswith('That a world is a run by definition')
    assert old[-1]['en'].startswith('That the process and world families are one by definition')
    old[-1] = {
        'en': 'That a process is a world, or that the spine\'s laws are stated once over the run: on R28\'s tree 485 of 11,684 spine theorems are apart from both families by dependency (a measurement, not a theorem).',
        'zh': '过程是世界，或脊柱的规律对运行只陈述一次：R28 树上 11,684 条脊柱定理中 485 条按依存与两族都不相连（测量，不是定理）。',
        'kind': 'scope'}
    del old[0]
    d['next_delta'] = {
        'en': 'Stating the spine\'s laws over every law of exchange, so that a law of worlds is one statement of runs, and folding back the companion modules; an independent review.',
        'zh': '对每条交换之律陈述脊柱的规律，使世界之律是运行的一个陈述，并把配套模块折回；独立审查。'}
    d['validation_scope'] = {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {RID}): the 16 declarations of Becoming.World and the 30 of Becoming.Runs, 21 of them theorems, have empty axiom reports; the checker verifies core purity. Author counterreview in study sections 165 and 219; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {RID}）：Becoming.World 的 16 项与 Becoming.Runs 的 30 项声明（共 21 项定理）公理报告为空；检查器并核对核心纯净。作者反审见研究 §165 与 §219；未经独立审查。'}
    d['reviewed_at_utc'] = NOW
    h = d['history'][-1]
    assert h['en'].startswith('20 October 2026, R28')
    h['en'] += (' The statement now says a world is a run by its type, with a law for the definition; the boundary "worlds are still defined'
                ' without processes" is removed, since it is now shown; the measurement boundary, the validation scope and the next step follow R28.')
    h['zh'] += '陈述改为世界按其类型就是运行，并为该定义增一条律；“世界仍不经过程而定义”这一界限已删去，因为现已证明；测量界限、验证范围与下一步随 R28。'
    save('worlds-are-runs', d)
    print('worlds-are-runs advanced')

d = load('recurrence-without-premise')
laws = d.get('laws')
if not any('Becoming.Law.lossless_iff' in str(x) for x in (laws or [])) and laws is not None:
    raise SystemExit('recurrence-without-premise has laws; add the law by hand')
h = d['history'][-1]
if h['en'].startswith('20 October 2026, R28') and not h['en'].endswith('the claim is unchanged.'):
    h['en'] += (' The orbit forms the claim states are the five unfolding lemmas; the claim is unchanged.')
    h['zh'] += '论断所说的轨道形式即五条展开引理；论断不变。'
    save('recurrence-without-premise', d)
    print('recurrence-without-premise noted')
