"""Chapter insertions for P49, as (kind, anchor, text) edits applied by apply_docs.py.

kind: 'before' inserts text (with a blank line after it) before the line starting with anchor;
'after_line' inserts text as new lines after the line starting with anchor;
'replace' replaces the exact substring anchor with text. Every anchor must occur once.
"""
LEAN = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
STUDY = ('../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/'
         'BECOMING-RENEWAL-READING.md#{ANCHOR}')

SECTION3_ZH = (
    '**反映与检验（第一部分，P49）。** 一个形成反映它的支持（水平是否接纳它）与它所观察之条件的水平'
    f'（[Becoming.Testing]({LEAN}/Testing.lean)）。经依存，反映是一个阈值：依存而不观察的条件只反映它是否满足所需'
    '（`Web.alike_of_threshold`）；经观察，反映其水平（`Web.observed_level_registers`）。主张只经反映的差别被否证'
    '（`Web.Refutes.not_of_alike`）：主张与其对手必须在能被反映之处不同，这是可否证性的结构。它是关系的：清除者不能检验的，栖居者能，'
    '两者合起来能检验各自都不能的（`Clearing.tested_by_dweller`、`Clearing.pooled`）。没有模型，有限的记录不否证关于其后的主张'
    '（`Web.tail_unrefuted`）；相对于交换的模型，观察储量的形成在第一步否证假的主张（`Flow.refutes_tail_within`）；相对于模型的否证是对'
    '模型与主张一起的否证，错的模型否证成立的，反映否证模型（`Web.refutesWithin_iff_conjunction`、`Stationary`）。由反映作出的判断，恰是'
    '判断过程在形成之信念上的共同回应，更晚的步与更多的观察都保持它（`Web.belief_judge_iff`）：上面的“判断即一步探究”由此接到流上。'
    '区域的成员只经自己的反映回应时，区域之外的在其中不被反映（`Flow.alike_within_closed`）；交换随形成的反映时，阈下的差别保持到两网的'
    '支持分岔（`Flow.subthreshold_alike`、`Flow.difference_changes_after_divergence`），他者回应储量本身时则不然'
    '（`Attracting.higher_breaks_first`）。平衡只在被反映的条件上逐步假设；回应的假设是给出的。读法（AI 的，经审查收窄，待 Ren）：'
    '经由支持的反馈有三种不见，各在其范围之内（阈下、视界之外、反映闭包之外）；失控读作在其一之中运行的回路，是启发，不是陈述；'
    f'理 读作对反映负责的模型。见[研究 §{{S}}]({STUDY})、'
    '[testing-within-registration](../results/records/testing-within-registration.md) 与 '
    '[subthreshold-registration](../results/records/subthreshold-registration.md)。')

SECTION3_EN = (
    '**Registration and testing (Part I, P49).** A formation registers its support, whether the levels admit it, and the '
    'levels of the conditions it observes. Through dependence registration is a threshold: a condition depended on and '
    'not observed registers only whether it meets the need; an observed one registers its level. A claim is refuted only '
    'through a difference in what registers, the structure of falsifiability, and testing is relational: the dweller '
    'refutes what the clearer cannot, and the two together what neither can alone. Without a model no finite record '
    'refutes a claim about what follows it; relative to a model of the exchange a formation observing a stock refutes a '
    'false one at the first step, the refutation being of the model and the claim together, and registration refutes a '
    'wrong model. A judgment from registration is a common response over the formation\'s belief, so judgment as a '
    'one-step inquiry reaches the flow. Where the members of a region respond only through their own registration, '
    'nothing beyond it registers within it; where the exchange follows a formation\'s registration, a difference below '
    'its threshold stays until the two webs\' support diverges, and not where others respond to the stock itself. The '
    'response hypotheses are supplied; the readings are the AI\'s, narrowed by the review, pending Ren.')

ITEM9_ZH_OLD = '不确定下的判断是一步探究（`Becoming.Inquiry`）。知识的完整说明见第 3 节。〔定理〕'
ITEM9_ZH_NEW = ('不确定下的判断是一步探究（`Becoming.Inquiry`）。一个形成只能检验在它所反映者中有所不同的主张，由反映作出的判断是'
                '对其信念的共同回应（`Becoming.Testing`）。知识的完整说明见第 3 节。〔定理〕')
ITEM9_EN_OLD = ('and judgment under uncertainty is a one-step inquiry (`Becoming.Inquiry`); section 3 gives the account of '
                'knowledge. [theorem]')
ITEM9_EN_NEW = ('and judgment under uncertainty is a one-step inquiry (`Becoming.Inquiry`); a formation can test only a claim '
                'that differs in what registers in it, and a judgment from its registration is a common response over its '
                'belief (`Becoming.Testing`); section 3 gives the account of knowledge. [theorem]')

WHOLE_II_ZH = (
    '- **反映与检验。** 依存而不观察的条件只反映它是否满足所需，观察的条件反映其水平（`Web.alike_of_threshold`）；主张只经反映的差别'
    '被否证（`Web.Refutes.not_of_alike`），相对于模型的否证是对模型与主张一起的否证（`Web.refutesWithin_iff_conjunction`）；区域的成员'
    '只经自己的反映回应时，区域之外的在其中不被反映（`Flow.alike_within_closed`）；交换随反映时，阈下的差别保持到两网的支持分岔'
    '（`Flow.difference_changes_after_divergence`）。平衡只在被反映的条件上逐步假设。')
WHOLE_II_EN = (
    '- **Registration and testing.** A condition depended on and not observed registers only whether it meets the need, '
    'an observed one its level (`Web.alike_of_threshold`); a claim is refuted only through a difference in what registers '
    '(`Web.Refutes.not_of_alike`), and refutation relative to a model is refutation of the model and the claim together '
    '(`Web.refutesWithin_iff_conjunction`); where the members of a region respond only through their own registration, '
    'nothing beyond it registers within it (`Flow.alike_within_closed`); where the exchange follows registration, a '
    'difference below the threshold stays until the two webs\' support diverges '
    '(`Flow.difference_changes_after_divergence`). Balance is assumed only on the conditions registered.')

WHOLE_III_ZH = (
    '- **模型与回应。** 模型从哪里来、他者怎样回应，不由动力学决定。没有模型，有限的记录不否证关于其后的主张（`Web.tail_unrefuted`）；'
    '相对于模型的否证可以出错（`Stationary.model_error`）。阈下与反映闭包之外的不见，以给出的回应假设为条件；他者回应储量本身时，较高的'
    '储量可以先终结形成（`Attracting.higher_breaks_first`）。一个动作造成什么，只相对于无此动作之历史的模型才可检验'
    '（`Flow.beyond_needs_model`）。')
WHOLE_III_EN = (
    '- **Models and responses.** Where a model comes from and how others respond are not decided by the dynamics. '
    'Without a model no finite record refutes a claim about what follows it (`Web.tail_unrefuted`), and refutation '
    'relative to a model can err (`Stationary.model_error`). The blindness below a threshold and beyond the registration '
    'closure is conditional on supplied response hypotheses; where others respond to the stock itself a higher stock can '
    'end the formation first (`Attracting.higher_breaks_first`). What an act does is testable only relative to a model of '
    'the history without it (`Flow.beyond_needs_model`).')

SPINE_ROW = (
    f'| L4 | [Becoming.Testing]({LEAN}/Testing.lean) | 反映与检验（不用公理，平衡只在被反映的条件上）：依存的条件只反映阈值，观察的反映水平；'
    '主张只经反映的差别被否证，相对于模型的否证是模型与主张一起的否证；判断是对信念的共同回应；成员只经自己的反映回应时闭包之外的不被反映；'
    '交换随反映时阈下的差别保持到支持分岔；检验是关系的 | {N_TESTING} |')

GLOSSARY = [
    '| 反映闭包 | registration closure | 对经所反映者受影响的闭包（另一个形成与它所依存或观察的条件交换）；含影响闭包，只反映支持时就是它；'
    '成员只经自己的反映回应时，闭包之外的在其中不被反映 | `Flow.WithinRegistration`、`Flow.alike_within_closed` |',
    '| 否证 | refutation | 满足主张的历史没有一个直到某步与实际反映相同；相对于模型（可容许历史的类）时，是对模型与主张一起的否证 | '
    '`Web.Refutes`、`Web.RefutesWithin`、`Web.refutesWithin_iff_conjunction` |',
    '| 阈下 | subthreshold | 依存而不观察的条件只反映它是否满足所需；交换随反映时，阈下的差别保持到两网的支持分岔 | '
    '`Web.alike_of_threshold`、`Flow.subthreshold_alike`、`Flow.difference_changes_after_divergence` |',
]

EDITS = [
    ('before', '**知识。** [知识一章]', SECTION3_ZH + '\n\n' + SECTION3_EN),
    ('replace', ITEM9_ZH_OLD, ITEM9_ZH_NEW),
    ('replace', ITEM9_EN_OLD, ITEM9_EN_NEW),
    ('before', '- **其余。** 运行上的端点丧失', WHOLE_II_ZH),
    ('before', '- **The rest.** The theorems on endpoint loss', WHOLE_II_EN),
    ('before', '- **意义。** 规律与定理不给任何部分以意义', WHOLE_III_ZH),
    ('before', '- **Significance.** The laws and theorems give no part significance', WHOLE_III_EN),
    ('after_line', '| L4 | [Becoming.Feedback]', SPINE_ROW),
    ('after_line', '| 所及闭包 | reach closure |', '\n'.join(GLOSSARY)),
]
