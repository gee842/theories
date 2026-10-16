"""Additive R5 landing from preserved branch 52ff83a4, using the shared landing kit.
Only the current integrator runs these scripts against the chosen landing checkout.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent


def doc(name):
    return (HERE / 'docs' / name).read_text().rstrip('\n')


LABEL = 'R5 Entropy'
PACKAGES = [dict(
    module='Entropy', package='becoming-entropy-landing', key='ENTROPY', prefix='r5',
    after='Resolution', scope_before='Continuation: across a step',
    bullet=doc('root_bullet.md'), scope=doc('checker_scope.txt'),
    readme_zh=doc('readme_zh.md'), readme_en=doc('readme_en.md'),
    imports_zh=('`Units` 导入 `Resolution`；', '`Entropy` 导入 `Resolution` 与 `Recurrence`；`Units` 导入 `Resolution`；'),
    imports_en=('`Units` imports `Resolution`;', '`Entropy` imports `Resolution` and `Recurrence`; `Units` imports `Resolution`;'),
)]
PLAN_ZH = doc('plan_zh.md')
PLAN_EN = doc('plan_en.md')
CHAPTER_EDITS = [
    ('before', '- **依存与储备。**', doc('chapter_zh.md')),
    ('before', '- **Dependence and reserve.**', doc('chapter_en.md')),
    ('after_line', '| L3 | [Becoming.Resolution]', doc('chapter_spine.md')),
]
READING = dict(
    after_zh='最后是开放纲领。',
    after_en='The open programme follows.',
    zh='R5 复用同一流说明交换的历史与保存记录的条件：历史计数单调，平衡时水平变化增加它；无损交换可以复返，耗散等价于守恒量中的逐次记录，这是分解而非从更少前提推出耗散；有限家族的水平箭头、合并与遗忘保留各自条件，并给出 R6 的实例。',
    en=' R5 uses the same flow to state exchange history and the conditions for holding a record: the history count is monotone and, under balance, level changes increase it; lossless exchanges can recur, and dissipation is equivalent to recording each exchange within the conserved amount, a decomposition rather than a derivation from less. Arrows, merging and forgetting on finite families keep their hypotheses, with instances of R6.',
    lean_after='Resolution.lean',
)
RECORDS = {'entropy-history-and-record': {'package':'ENTROPY', **json.loads(doc('record_spec.json'))}}
HISTORY = {'ENTROPY': (
    '2026-10-13：按 Ren 的合并接手指令从 R5 分支 52ff83a4 整合；原始源码逐字节保留，四个冲突列表辅助名限定到 EntropyLists，研究 §{S}；补全导入、去掉未证明的唯一性读法，区分不需要平衡的历史单调性与使用平衡的变化／逆转结论；新合并回执核对当前源码，原有历史如下。',
    '2026-10-13: integrated from R5 branch 52ff83a4 under Ren’s takeover and merge request; original source bytes retained, four colliding list helpers qualified under EntropyLists, study §{S}. Imports are corrected, an unproved uniqueness reading removed, and premise-free history monotonicity distinguished from change/reversal results using balance. Current receipts check the integrated source; prior history is retained below.',
)}
DELTAS = ['finish_record.py']
