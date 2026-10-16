"""Chapter insertions for P55, as (kind, anchor, text) edits applied by apply_docs.py."""
LEAN = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
STUDY = ('../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/'
         'BECOMING-RENEWAL-READING.md#{ANCHOR}')

SECTION3_ZH = (
    '**失控（第一部分，P55）。** 经反映的策略加其余固定，就是交换随反映'
    f'（[Becoming.Runaway]({LEAN}/Runaway.lean)，`Flow.exchangeFollows_of_policy`）；所以每个这样的策略保持支持就永不动用它不观察的'
    '较多储量，动用了就已失去支持（`Flow.policy_keeps_difference`、`Flow.policy_uses_after_failure`）。断裂之前，对每个视界，都有储量'
    '抬高的世界与实际在形成所反映的一切上相同，并撑过那个视界（`Web.break_not_bounded`）：断裂还有多远不被反映；观察储量则立刻反映'
    '（`Web.observed_raise_registers`）。读法（AI 的，待 Ren）：失控是断裂之前自身反映与储量多出任意多的世界相同的回路；要避免它而又不'
    '放弃所有的，需要量度、模型或他者的反映。'
    f'见[研究 §{{S}}]({STUDY})与 [runaway-distance-unregistered](../results/records/runaway-distance-unregistered.md)。')

SECTION3_EN = (
    '**Runaway (Part I, P55).** A policy through registration, with the rest of the exchange fixed, is exchange '
    'following registration; so every such policy that keeps its support never uses a larger stock it does not '
    'observe, and one that has used it has already lost its support. Before the break, for every horizon a world with '
    'the stock raised registers alike in everything the formation registers and lasts past it: how far off the break '
    'is does not register, while observing the stock registers it at once. On the AI\'s reading, pending Ren, a runaway '
    'is a loop whose own registration before the break is that of a world with as much more stock as one likes, and '
    'avoiding it without forgoing what is there needs measurement, a model or another formation\'s registration.')

WHOLE_II_ZH = (
    '- **失控。** 每个经反映、其余固定的策略，保持支持就永不动用它不观察的较多储量（`Flow.policy_keeps_difference`）；断裂之前，断裂还有'
    '多远不被反映（`Web.break_not_bounded`）。')
WHOLE_II_EN = (
    '- **Runaway.** Every policy through registration, with the rest fixed, that keeps its support never uses a larger '
    'stock it does not observe (`Flow.policy_keeps_difference`); before the break, how far off it is does not register '
    '(`Web.break_not_bounded`).')

SPINE_ROW = (
    f'| L4 | [Becoming.Runaway]({LEAN}/Runaway.lean) | 失控（不用公理，平衡只在被反映的条件上）：经反映的策略加其余固定就是交换随反映，'
    '保持支持就永不动用较多的储量；断裂之前，断裂的距离不被反映；观察储量立刻反映 | {N_MODULE} |')

EDITS = [
    ('before', '**知识。** [知识一章]', SECTION3_ZH + '\n\n' + SECTION3_EN),
    ('before', '- **其余。** 运行上的端点丧失', WHOLE_II_ZH),
    ('before', '- **The rest.** The theorems on endpoint loss', WHOLE_II_EN),
    ('after_line', '| L4 | [Becoming.Testing]', SPINE_ROW),
]
