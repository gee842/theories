"""Chapter insertions for P53, as (kind, anchor, text) edits applied by apply_docs.py.

kind: 'before' inserts text before the line starting with anchor (a blank line after a
paragraph, none after a list item); 'after_line' inserts text as new lines after the line
starting with anchor; 'replace' replaces the exact substring anchor with text. Every anchor
must occur once.
"""
LEAN = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
STUDY = ('../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/'
         'BECOMING-RENEWAL-READING.md#{ANCHOR}')

SECTION3_ZH = (
    '**实验（第一部分，P53）。** 一个动作造成什么，是有与无此动作的两段历史的比较，而一个展开只有其中一段'
    f'（[Becoming.Experiment]({LEAN}/Experiment.lean)）。相对于确定性（`Determined`，动作决定一步），记录恰在运行取过某动作之处'
    '固定它在那里的结果（`Run.fixes_of_takes`）；未取的动作即使一切都被反映也不被固定（`Run.not_fixes_of_untaken`）。所以自己的动作'
    '若换一个会怎样，只在配置返回之处被固定（`Run.fixes_on_return`）；保留其全部历史的运行每步都是新的，关于自己的动作只固定所做的'
    '（`keepHistory_fixes_nothing_else`）。实验因此需要一个关于何者无关的模型：步骤经一个投影分解为确定过程时，一次场合代表投影相同的'
    '整个类（`Run.generalizes`），有限多个投影配置之内投影必返回（`Run.projection_returns`）。模型可以错：错误的投影把差别归于不造成'
    '差别的动作，动作与它所略去者同步时永不被否证，与之错开时被否证（`Confound`）。读法（AI 的，待 Ren）：重复是返回，对照是步骤经'
    '读法分解的模型，与略去者无关的变动是随机化的结构形式。'
    f'见[研究 §{{S}}]({STUDY})与 [experiment-needs-return](../results/records/experiment-needs-return.md)。')

SECTION3_EN = (
    '**Experiment (Part I, P53).** What an act does compares the history with the act and the history without it, and one '
    'unfolding has only one of them. Relative to determinacy, the record fixes what a move does at a configuration '
    'exactly where the run has taken it there; an untaken move is not fixed even with everything registered. So what '
    'one\'s act would have done otherwise is fixed only where the configuration returns, and a run keeping its whole '
    'history, new at every step, fixes nothing about its acts but what it did. Experiment therefore needs a model of '
    'what is irrelevant: where the step factors through a projection into a determined process, one occasion stands '
    'for its whole class, and within finitely many projected configurations the projection returns. The model can be '
    'wrong: a wrong projection misattributes, is never refuted by moves in step with what it leaves out, and is refuted '
    'by moves varied against it. On the AI\'s reading, pending Ren, replication is return, a control is the model that '
    'the step factors through the reading, and variation independent of what is left out is the structural form of '
    'randomization.')

ITEM9_ZH_OLD = '对其信念的共同回应（`Becoming.Testing`）。知识的完整说明见第 3 节。〔定理〕'
ITEM9_ZH_NEW = ('对其信念的共同回应（`Becoming.Testing`）。一个动作造成什么，只在配置返回之处由记录固定，所以实验需要一个关于何者无关的模型'
                '（`Becoming.Experiment`）。知识的完整说明见第 3 节。〔定理〕')
ITEM9_EN_OLD = ('belief (`Becoming.Testing`); section 3 gives the account of knowledge. [theorem]')
ITEM9_EN_NEW = ('belief (`Becoming.Testing`); what an act does is fixed by the record only where the configuration returns, so '
                'experiment needs a model of what is irrelevant (`Becoming.Experiment`); section 3 gives the account of '
                'knowledge. [theorem]')

WHOLE_II_ZH = (
    '- **实验。** 相对于确定性，记录恰在运行取过某动作之处固定它的结果，未取的动作不被固定（`Run.fixes_of_takes`、'
    '`Run.not_fixes_of_untaken`）；自己的动作若换一个会怎样，只在配置返回之处被固定；保留历史的运行永不返回'
    '（`keepHistory_fixes_nothing_else`）；步骤经投影分解为确定过程时，一次场合代表其类（`Run.generalizes`）。')
WHOLE_II_EN = (
    '- **Experiment.** Relative to determinacy, the record fixes a move\'s outcome exactly where the run has taken it, and '
    'an untaken move is not fixed (`Run.fixes_of_takes`, `Run.not_fixes_of_untaken`); what one\'s act would have done '
    'otherwise is fixed only where the configuration returns, and a kept history never returns '
    '(`keepHistory_fixes_nothing_else`); where the step factors through a projection into a determined process, one '
    'occasion stands for its class (`Run.generalizes`).')

WHOLE_III_ZH = (
    '- **对照。** 步骤经哪个投影分解，不由动力学决定，也不由记录确证：错误的投影在动作与它所略去者同步时永不被否证，只在动作与之错开时被'
    '否证（`Confound.confounded`、`Confound.varied_refutes`）。')
WHOLE_III_EN = (
    '- **Controls.** Which projection the step factors through is decided neither by the dynamics nor by the record: a '
    'wrong projection is never refuted while the moves follow what it leaves out, and is refuted only by moves varied '
    'against it (`Confound.confounded`, `Confound.varied_refutes`).')

SPINE_ROW = (
    f'| L3 | [Becoming.Experiment]({LEAN}/Experiment.lean) | 实验（不加前提）：相对于确定性，记录恰在取过之处固定一个动作的结果，'
    '未取的不被固定；自己的动作若换一个会怎样，只在配置返回之处被固定，保留历史的运行永不返回；经步骤可分解的投影，一次场合代表其类；'
    '错误的投影误归因，同步的动作永不否证它，错开的动作否证它 | {N_MODULE} |')

GLOSSARY = [
    '| 实验 | experiment | 在配置（按实验者的读法）返回之处变动自己的动作；相对于确定性，记录恰在取过之处固定一个动作的结果 | '
    '`Run.Fixes`、`Run.fixes_of_takes`、`Run.not_fixes_of_untaken`、`Run.fixes_on_return` |',
    '| 对照 | control | 两次场合之间不同的与变化无关这一模型：步骤经读法分解为确定过程；可被与略去者错开的动作否证，不被同步的动作否证 | '
    '`FactorsThrough`、`Run.generalizes`、`Confound` |',
]

EDITS = [
    ('before', '**知识。** [知识一章]', SECTION3_ZH + '\n\n' + SECTION3_EN),
    ('replace', ITEM9_ZH_OLD, ITEM9_ZH_NEW),
    ('replace', ITEM9_EN_OLD, ITEM9_EN_NEW),
    ('before', '- **其余。** 运行上的端点丧失', WHOLE_II_ZH),
    ('before', '- **The rest.** The theorems on endpoint loss', WHOLE_II_EN),
    ('before', '- **意义。** 规律与定理不给任何部分以意义', WHOLE_III_ZH),
    ('before', '- **Significance.** The laws and theorems give no part significance', WHOLE_III_EN),
    ('after_line', '| L3 | [Becoming.Joint]', SPINE_ROW),
    ('after_line', '| 阈下 | subthreshold |', '\n'.join(GLOSSARY)),
]
