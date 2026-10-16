"""Chapter insertions for P62, as (kind, anchor, text) edits applied by apply_docs.py."""
LEAN = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
STUDY = ('../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/'
         'BECOMING-RENEWAL-READING.md#{ANCHOR}')

SECTION3_ZH = (
    '**无明的边界条件（第一部分，P62）。** 寻求读作朝向一个在某状态被满足之目标的活动，目标在展开之中形成'
    f'（[Becoming.Seeking]({LEAN}/Seeking.lean)）。在确定的律之下，寻求恰在到达律所不变、满足其目标的状态时，带着满足的目标静止'
    '（`Law.rests_iff`）：够的边界。“比现在更多”只由变化满足，每步都满足就需要开放的世界（`more_needs_open`）；“高于一切他者”在一个'
    '状态至多被一个寻求者满足，所以两个这样的寻求者从不同时静止（`aboveAll_unique`、`Law.aboveAll_never_rests`）。所立者被列出时，'
    '不断上升需要所立者在任意晚处不衰减的步，即从其外汲取或不耗散的交换；所立者从某步起每步衰减时，上升不再复现：追逐因耗尽而止，不是因'
    '到达够（`Flow.more_needs_unrun`、`Flow.more_exhausted`）。损失只经寻求者所识者到达它（P49、P55），所以被锁定的寻求不被自身的反馈'
    '纠正；识及支持所不标记者的识，即量度、模型或他者，纠正它。劫持（B5，'
    f'[Becoming.Capture]({LEAN}/Capture.lean)）：带着目标的亲代留下更多后代时，目标的份额上升（`share_rises`），这是 Evolution 未陈述的选择项；'
    '所立者衰减不断则世系与选择停止（`Flow.descent_exhausted`）；下一配置取决于规则时，只改状态被重新吸收（`Law.reform_reabsorbed`）。'
    '读法（AI 的，待 Ren）：无明是使寻求锁定在不能于静止中满足之目标上的不见；'
    '明是识及支持所不标记者的识；知足、知止是 B1 边界之内的目标；劫持是奖赏不能静止者的选择所形成、由胜者所写之规则保持的目标；'
    '支配本身不在所排除者之内。'
    f'见[研究 §{{S}}]({STUDY})、[seeking-boundary](../results/records/seeking-boundary.md) 与 '
    '[target-capture](../results/records/target-capture.md)。')

SECTION3_EN = (
    '**The boundary condition for 无明 (Part I, P62).** Seeking is read as activity toward a target met at a state, the '
    'target formed within the unfolding. Under a determined law, seeking comes to rest with its target met exactly when '
    'it reaches a state the law leaves unchanged that meets it: the boundary of enough. "More than now" is met only by '
    'change and, met at every step, needs an open world; "above all others" is met by at most one seeker at a state, so '
    'two such seekers never rest together. Where what stands is listed, rising without end needs steps at arbitrarily '
    'late times at which what stands does not run down, drawing from beyond or exchange that does not dissipate; where '
    'it runs down from some step on, the rises stop: the pursuit ends by exhaustion, not by reaching enough. Losses reach '
    'a seeker only through what it registers (P49, P55), so locked seeking is not corrected by its own feedback; '
    'registration reaching what support does not mark corrects it. Hijacking (B5): where a target\'s carriers leave '
    'more offspring its share rises, the selection term Evolution leaves unstated; running down stops descent and the '
    'selection; and where the next configuration depends on the rule, reforming the state alone is re-absorbed. On '
    'the AI\'s reading, pending Ren, 无明 is the '
    'not-seeing that keeps seeking locked onto a target that cannot be met at rest, and 明 is registration reaching what '
    'support does not mark.')

WHOLE_II_ZH = (
    '- **够。** 在确定的律之下，寻求恰在到达律所不变、满足其目标的状态时静止（`Law.rests_iff`）；“比现在更多”需要开放的世界，“高于一切他者”'
    '不同时满足两个寻求者（`more_needs_open`、`aboveAll_unique`）；所立者被列出时，不断上升需要不衰减的步（`Flow.more_needs_unrun`）。')
WHOLE_II_EN = (
    '- **Enough.** Under a determined law, seeking comes to rest exactly when it reaches a state the law leaves unchanged '
    'meeting its target (`Law.rests_iff`); "more than now" needs an open world, and "above all others" never holds of two '
    'seekers at once (`more_needs_open`, `aboveAll_unique`); where what stands is listed, rising without end needs steps '
    'at which it does not run down (`Flow.more_needs_unrun`).')

WHOLE_II_ZH += (
    '\n- **劫持。** 带着目标的亲代留下更多后代时目标的份额上升（`share_rises`）；所立者衰减不断则选择停止（`Flow.descent_exhausted`）；'
    '下一配置取决于规则时，只改状态被重新吸收（`Law.reform_reabsorbed`）。')
WHOLE_II_EN += (
    '\n- **Hijacking.** Where a target\'s carriers leave more offspring its share rises (`share_rises`); running down '
    'stops the selection (`Flow.descent_exhausted`); where the next configuration depends on the rule, reforming the '
    'state alone is re-absorbed (`Law.reform_reabsorbed`).')

WHOLE_III_ZH = (
    '- **目标。** 实际的形成持有什么目标，目标怎样形成、被劫持、被传递，不由动力学决定；寻求者追求其目标也不推出（`Becoming.Seeking`）。')
WHOLE_III_EN = (
    '- **Targets.** Which targets actual formations hold, and how targets form, are hijacked or transmitted, are not '
    'decided by the dynamics; nor is it derived that a seeker pursues its target (`Becoming.Seeking`).')

SPINE_ROW = (
    f'| L3 | [Becoming.Seeking]({LEAN}/Seeking.lean) | 无明的边界条件（不用公理）：寻求恰在到达律所不变、满足其目标的状态时静止；'
    '“比现在更多”需要开放的世界，“高于一切他者”至多一个；不断上升需要不衰减的步，衰减不断则上升停止 | {N_MODULE} |')

SPINE_ROW_CAP = (
    f'| L3 | [Becoming.Capture]({LEAN}/Capture.lean) | 劫持（无明边界的 B5，不用公理）：带着目标的亲代留下更多后代时目标的份额上升；'
    '所立者衰减不断则世系与选择停止；下一配置取决于规则时只改状态被重新吸收 | {N_CAP} |')

GLOSSARY = [
    '| 够 | enough | 目标在一个展开所不变的状态被满足；在确定的律之下，寻求恰在到达这样的状态时静止 | `Law.rests_iff`、`Law.fixed_rests` |',
    '| 无明 | 无明 (not-seeing) | AI 的读法（待 Ren）：使寻求锁定在不能于静止中满足之目标上的不见；其边界是够 | `Becoming.Seeking` |',
    '| 劫持 | hijacking | AI 的读法（待 Ren）：奖赏不能静止者的选择所形成、由胜者所写之规则保持的目标；份额随后代上升，结果握在规则里 | '
    '`share_rises`、`Law.reform_reabsorbed` |',
]

EDITS = [
    ('before', '**知识。** [知识一章]', SECTION3_ZH + '\n\n' + SECTION3_EN),
    ('before', '- **其余。** 运行上的端点丧失', WHOLE_II_ZH),
    ('before', '- **The rest.** The theorems on endpoint loss', WHOLE_II_EN),
    ('before', '- **意义。** 规律与定理不给任何部分以意义', WHOLE_III_ZH),
    ('before', '- **Significance.** The laws and theorems give no part significance', WHOLE_III_EN),
    ('after_line', '| L3 | [Becoming.Locality]', SPINE_ROW),
    ('after_line', '| L3 | [Becoming.Evolution]', SPINE_ROW_CAP),
    ('after_line', '| 对照 | control |', '\n'.join(GLOSSARY)),
]
