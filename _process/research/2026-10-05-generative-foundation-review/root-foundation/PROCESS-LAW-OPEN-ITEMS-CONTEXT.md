# 三项未能消除的输入：具体上下文

2026年10月6日（UTC）。AI 撰写，应 Ren 要求说明[依赖图台账](PROCESS-LAW-ENTRY-DEPENDENCY-MAP.md#7-no-assumptions-ledger)中三项“搞不定”的输入。下面区分：Lean 里实际证明了什么；它说明了什么、没说明什么；以及按一元、关系的读法可以怎么走。标为“推测”的是 AI 的判断，未经证明。

## 1. 动力学由什么选定

**模块：** [DynamicUnderdetermination.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/DynamicUnderdetermination.lean)，[DynamicSymmetry.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/DynamicSymmetry.lean)。

**实际证明的内容。** 取同一个载体：状态是 `Bool`（两个状态），动作是 `Unit`（一种事件）。在它上面定义三条规律：

- `idle`：什么都不能发生；
- `static`：事件发生，状态不变（`s → s`）；
- `toggle`：事件发生，状态翻转（`s → !s`）。

`same_carrier_incompatible_laws` 证明：在完全相同的状态和动作上，`toggle` 允许 `false → true`，`idle` 不允许；`static` 允许 `false → false`，`toggle` 不允许。

`DynamicSymmetry` 再加强：`static` 和 `toggle` 都满足全域（每个状态都有后继）、确定（后继唯一）、可逆（每步可反向）、前驱唯一，并且在 `Bool` 的所有双射改名下不变。它们仍然在“状态能否保持不变”上相反（`symmetric_dynamics_remain_underdetermined`）。

**这说明了什么。** “有哪些区分”加上这几条结构性质，不能决定发生什么。这是一个有限反例，只否定这一种蕴含。

**没说明什么。** 模块自己写明：这不是“从更丰富的根据也推不出规律”的不可能性定理。

**一元地看（推测）。** 这个反例本身用了一个二分：先给“载体”（状态集合），再在外面挑“规律”。按一元、关系的读法，状态不是先于关系的东西，状态就是由关系（哪些转换发生）区分出来的。那么问题应改成：在同一过程里，哪些转换关系能自我延续。这与第2项现在的做法同构（见下）。可能的定理形式：一个关系系统中，能持续生成自身后续转换的那部分，就是“选定的动力学”。这还没有做。

**已证（2026年10月6日，按 Ren“你不确定就先证一下试试”）。** [RelationalDynamics.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/RelationalDynamics.lean) 把“状态由关系区分”写成双模拟（bisimulation）：两个位置算同一个，当且仅当它们能发生的转换一一对应、并且对应之后仍然对应。这是定义，不是公理。13 条审计全部为空，连同 `GenerativeCore`、`DynamicUnderdetermination` 整个闭包都不用任何公理（[检查器](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_relational.py)，[回执](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/relational-dynamics-verification.json)）。

- `continuing_single_event_is_one_recurrence`：只有一种事件、且每处都能继续的过程，不论载体是什么，关系上都是同一个“单一复现”（一个点、一个自环）。
- `static_toggle_one_dynamics`、`static_toggle_same_histories`：`static` 和 `toggle` 关系上是同一个动力学，有完全相同的历史。
- `states_relationally_identical`、`unchanged_reads_carrier_identity`：`Bool` 的两个状态关系上不可区分；“状态不变”这个区别读的是载体上的相等，不是任何关系。
- `idle_differs_from_recurrence`、`toggle_continues`、`idle_cannot_continue`：剩下唯一的区别是有活动与无活动：`toggle` 永远能继续，`idle` 一步也不能。

**结论与范围。** 原反例里 `static` 与 `toggle` 的不确定，是因为先给了载体身份再挑规律；按关系的读法它消失了。剩下的是“继续还是不继续”，而这个区别本身就是关系上的区别。说生生之理选定了“继续”，是解释，不是定理。范围只到一种事件：有两种以上事件时，关系上不同的动力学仍然很多（例如只发生 a，与 a、b 交替），它们由什么选定，仍未解决；下一步要证的是：在同一过程里，哪些关系类能维持自身的后续转换。

## 2. 评价方向

**模块：** [EthicalOrientation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/EthicalOrientation.lean)。

**实际证明的内容。** 用现有 `toggle` 过程比较两段历史：空历史，和一次真实的两步循环（同一起点、同一终点、同一规律）。“历史越长越好”与它的逆序“历史越短越好”都满足：自反、传递、在动作改名下不变、与历史上附加的标注无关。两者对这两段历史排序相反（`opposed_coherent_annotation_invariant_orders`、`coherence_and_annotation_invariance_do_not_select_growth`）。所以一致性加不变性选不出方向。

**最新进展（另一线程，已在 main，全部无公理）。** 伦理自然主义研究[§9–10](ETHICAL-NATURALISM.md)把评价改写成过程内部的记录，而不是过程外部的“应当”：

- 同一过程定律下，按延续序记录和按逆序记录都是可能的耦合（`law_admits_opposite_recordings`）；方向问题因此变成“哪一种评价关系在展开中形成并延续”。
- 评价能无限延续，当且仅当它属于一个自我更新的群体，而这个群体生成自身后续形成的条件（`evaluation_persists_iff_member`、`persisting_evaluation_renews_its_conditions`）。

**仍未证。** 延续下来的评价是否就按“延续条件”的方向记录；以及“延续”是否就是善的尺度。按无假设规则，后者若作为前提，就要证明其必要。另外 §10 的这三条结果目前仍依赖 `propext` 和 `Quot.sound`，来自所引用的估值研究模块，需要那些线程改写。

## 3. Lean 自身的逻辑

**是什么。** 现在审计“为空”，意思是证明只用了 Lean 内核的推理规则：依值类型论、归纳类型、定义相等。没有加任何公理（包括 `propext`、`Quot.sound`、选择公理）。剩下的是这些推理规则本身。

**为什么在 Lean 里消除不了。** 任何形式系统都只能在某套推理规则内证明东西。足够强的系统不能在自身内部证明自身一致（哥德尔第二不完备定理）。所以“不用任何规则”的证明不存在，这不是工程问题。

**一元地看（推测）。** 按[非二元方法](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md)，“提供给局部模型的规律并不因此外在于生成实在”。推理规则可以读作同一过程中分化出来的一种实践（构造与检验），而不是理论之外的前提。这改变的是它的地位，不是它可以被消除。可以做的是：把所用规则缩到最小并公开列出；以及用第二个独立的检查器（例如另一个类型论内核）复核，减少对单一实现的依赖。
