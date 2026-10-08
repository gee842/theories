# G0 的根据：一项采用的公理怎样得到支持 / The warrant for G0: how an adopted axiom is supported

2026-10-09，Asia/Bangkok。AI（Claude）撰写，执行 [Ren 的指示](../../../sources/15-codex-theory-conversations/2026-10-09-lean-evidence-roles.md)。本章不证明 G0，也不把它从公理改成定理。它整理适合于一项采用公理的支持，说明形式检查在其中各承担什么，并写明什么结果会修订它。Ren 的原话与 AI 的重构分别标注；[外部视角审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/UNIVERSAL-METAETHICS-OF-AGENCY-REVIEW.md)与[区分内容整合](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVE-DISCRIMINATION-INTEGRATION.md)记录了本章的起因与新证明。

This chapter does not prove G0 or convert it into a theorem. It organizes the kinds of support appropriate to an adopted axiom, states what each formal check contributes, and names results that would revise it.

## 1. 地位 / Status

**G0：整体中的生及其继续生成具有基本正面规范意义。** 这是对 Ren 输入的 AI 重构。2026-10-08 Ren 明确：“当然，这种地方需要有axiom才行，不要继续白费功夫”（[来源](../../../sources/15-codex-theory-conversations/2026-10-08-alignment-grounding-axiom-correction.md)）。审查 §3.1 的修订说明了为什么：规范谓词与描述关系之间的连接，要么不存在，此时描述推不出规范结论；要么由前提、定义或构成性同一给出，此时这一连接本身就是承诺。审查附录用 Lean 检查了这一两难的形式核心。Kant、Gewirth、Parfit、功利主义与契约主义都有自己的起点；因此，有一项公理本身不构成相对于对手的缺陷。

**G0: living and further generation within the whole have basic positive normative significance.** It is an adopted axiom. Every normative foundation has a starting commitment; what remains open is comparative: what G0 explains, how much it assumes, which positions it addresses, and what would revise it.

G0 只给出效价：实现了的生及继续生成有正面意义。把它变成某一位置的理由，靠的是直接实践解释 D／P；把各种理由变成比较与要求，靠的是 J1–J4；把它们用于具体处境，靠的是对应条件 E。下面各节分别说明这些承诺获得支持的方式。

G0 supplies valence only. Direct articulation (D/P) makes it a reason for a position, J1–J4 turn reasons into comparisons and requirements, and E applies them to a situation.

## 2. 支持的四种方式 / Four kinds of support

### 2.1 解释统一 / Explanatory unification

照护、修复、创造、学习、更新、休息、有限完成与建设性结束，都可以从同一根据得到说明，而无须分别假定各自独立的内在价值（[前提推导](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVE-PREMISE-DERIVATION.md) §§1、3；[对齐方向](ALIGNMENT-DIRECTION.md) §1）。自我照护被纳入，不必先产生外部收益；结束被纳入，不必先证明旧安排永久无用。若一种对手需要更多相互独立的起点才能解释同样的范围，这就是支持 G0 的比较理由。

Care, repair, creation, learning, renewal, rest, finite fulfillment and constructive ending are explained from one ground. A rival needing more independent starting points to cover the same range loses on this comparison.

### 2.2 区分力 / Discriminating content

逐项读取 G0，即每一项实现了的新组织都有正面意义，会把同样的正面意义给予持续形成新组织却毁坏其依存条件的过程，例如肿瘤式增殖与自我强化的竞争性扩张。Ren 的判准本身是整体的：“一种整体的，不断创造更多生的方向”，并且明确不缩成“已被独立判好的可能性”（[原话](../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md)）。

问题是：整体判准能否不借先行的好坏筛选，就把两者分开？[RenewingFormation.lean](../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RenewingFormation.lean) 在一个明确的局部规律类中回答“能”：

- 形成压力在更新之内时，形成生生不息（`within_renewal_ceaseless`）；
- 压力持续超出更新、并因此磨损进行更新的组织时，整个展开的累计形成以 `stock + tri renew` 为界，并在这一时刻之前停止（`beyond_renewal_bounded`、`beyond_renewal_ceases`）；
- 共享这些条件的其他形成，无论怎样分配，都随之停止，尽管它们本身原可生生不息（`consuming_part_ends_otherwise_ceaseless_formation`）；
- 消耗型形成起初可以形成得更多；预算之后，持续形成超过每一种消耗型接续（`consuming_forms_more_first`、`sustained_eventually_exceeds_every_consuming`）；
- 逐事件读取的 G0 同时承认两者的形成事件；把它们分开的，是动力学上的 `Ceaseless`（`event_reading_favors_both`、`whole_direction_separates`）。

Read event by event, G0 grants positive relevance to malignant formation as well. Under one supplied law class, the theorems show that Ren's whole-direction criterion separates formation within renewal (ceaseless) from formation that consumes the renewing organization (bounded, ceasing, and ending co-dependent formation), without any prior goodness filter, although the consuming process forms more at first. The separating content is dynamical and contains no normative predicate. G0 supplies valence; these theorems supply discrimination.

“生生不息”在此的形式读法是：在所表示的范围内，每一步都有进一步的形成。这是 AI 的重构。停止本身没有被判为坏的，有限完成、休息与适当结束仍是 G0 所承认的生。伦理上更尖锐的关系，是终止那些本身并未超出更新的共享形成；对它的判断仍须经 J1／J3 与对应条件。真实过程是否满足所给磨损规律，须各自取得证据。

**这一区分的范围。** 在上述规律类中，消耗者本身依存于它所消耗的条件，因此终将终止自身。另一种情形不在其中：一个形成取用另一关系所依存的条件，自身却不依存于它。它可以每步都在、形成无界，而那一关系永久失去其条件；把代价外部化的“赢家”式扩张，即 meta-attractor 的情形，就是这样。此时，焦点形成自身的 `Ceaseless` 以至总形成的 `Ceaseless`，都识别不出这种消耗。起决定作用的是关系性质：是否有依存的关系永久失去其条件。另一分支的 `relational-renewal-classification`（登记中）在任意展开上给出这一分类，并证明焦点形成自身的活动与形成不决定其类别。因此，“整体方向”须读作每个依存关系的接续，而不是任何一个形成自身的持续或总量的持续。

Scope of this separation: in this law class the consumer depends on what it consumes and so ends itself. A formation drawing on a condition that another relation depends on, without depending on it itself, can stay active and form without bound while that relation loses its condition for ever (the externalizing "winner", the meta-attractor case). Neither its own nor total ceaselessness detects this. The deciding property is relational: whether some dependent relation permanently loses its condition. The whole direction must be read over every dependent relation's continuation.

### 2.3 与对手的判别 / Discrimination against rivals

**均匀聚合。** [ProtectionPriorityRival.lean](../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ProtectionPriorityRival.lean) 检查了一个保护对增益的情境：

- J2 的排序满足无损扩展比较 C，并且从不以任何数量的增益交换基本条件；
- 另有一个满足 C 的标量排序会交换，因此 J2 不能由 G0 与 C 推出；
- 每一个满足 C 的自然数评分都会在有限数量的增益处交换。

由此，J2 恰好排除“每项增益至少加一个单位”的整个聚合对手类。实数值、边际递减且有上界的评分没有被排除，仍是实质对手。此前已检查的结果分别说明：`no_protection_trade_by_count` 给出 J2 的不交换性质；`compatible_cutoffs_disagree` 与 `loss_sensitivity_alone_supplies_no_cutoff` 说明损失敏感性本身不给出截断；`both_tradeoff_options_survive` 说明 C 在真实取舍中留下不止一个选项。

J2 is independent of G0 and C, and excludes exactly the uniform-unit aggregation class in this situation; bounded-sensitivity rivals remain.

**以后来认可为最终尺度。** [生成对齐修订](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVE-ALIGNMENT-REVISION.md)中的对手一主张，后来的充分认可就足以证明形成过程正当。本框架拒绝其充分性：后来无异议不会使已发生的损失没有发生，J2 也不允许以更多认可换取仍存在的基本剥夺。

**Gewirth 与辩证路线。** Gewirth 试图从任何目的性行动者已有的承诺推出普遍原则，而不另设价值公理（[来源研读](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/NORMATIVE-WARRANT-SOURCES.md) §1）。他的论证公认在“我需要 X”到“他人也应尊重每个人的 X”这一步上有争议。审查 §3.1 提出一个研究假说：一元关系本体下，评价者自身的评价与延续形成于并依存于与他者的关系，阻断这一步的自我边界并不是给定的。若这条路走通，G0 可以降为接近“构成我之评价的那些生成关系的延续”，所支持的也正是 §2.2 中的更新型形成。这是待证目标（`universal-practical-warrant`，open），不是成果。

**2026-10-09 部分完成**（[自我之善推出可及范围的 G0](../results/records/self-good-reachable-g0.md)，[论证](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/EVALUATOR-GROUNDING-ARGUMENT.md)）。起点改为评价者自身的自我之善 S0：它自己的生及继续生成对它有提供理由的意义。意义只取决于已形成关系，不取决于原始所有者。第一步不加额外理性前提：S0 加上对手自己的单调性，及于至少同样相连的他者；只承认“我的”的对手严格不一致。第二步加上容差与分级连通，及于全部可及的生命，所得恰为可及库存上的 G0。因此对持 S0 的评价者，G0 的可及部分由其自身之善推出，理由的约束也不依赖 D。墙仍在：没有 S0 的现时目的评价者不受约束；容差对门槛式对手仍有争议；所得是正面意义，不是权重；`universal-practical-warrant` 仍为 open。

Partially completed on 9 October: starting from the evaluator's own self-good S0, with significance determined by formed relations rather than a primitive owner, monotonicity alone reaches others at least as connected (the own-only rival is inconsistent), and tolerance with graded connection yields G0 on the reachable inventory. Present-aim evaluators without S0 escape; tolerance remains contested; the target stays open.

**构成主义与 shmagency。** 任何论证都不能约束一个不评价任何东西、或对一切延续都漠然的过程。因此即使最强的辩证路线成功，所得也是“对一切评价者普遍”，不是“对一切可能存在普遍”。G0 公开采用，承认这一限度。

### 2.4 对齐上的丰饶性 / Fruitfulness for alignment

在 G0、J1–J4 与 E 之下，人类指令、机构目标和 AI 当前目的都可受伦理评价；一个具体案例已显示，哪些事实变化会改变判断（[对齐方向](ALIGNMENT-DIRECTION.md) §5）。§2.2 的结果为对齐补上一个可检查的警示：一个按局部生成计数优化的系统，可能偏好起初形成更多、随后终止共享形成的消耗型接续。按每个依存关系的接续来读的整体方向，不会犯这个错误；只看系统自身能否持续，则会漏掉把代价外部化的扩张。

Under the same commitments, human instructions, institutional aims and AI goals are open to ethical evaluation. §2.2 adds a checkable caution: optimizing local generative counts can prefer consuming continuations that form more at first and later end shared formation. Reading the whole direction over every dependent relation avoids this; checking only whether the system itself persists misses externalizing expansion.

## 3. 形式检查各承担什么 / What each formal check contributes

| 检查 | 承担的内容 | 不承担的内容 |
|---|---|---|
| [PositiveGroundUncertainty](../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/PositiveGroundUncertainty.lean) | 前提足迹：正面结论只需 G0 与实际对应，不需整体改善、完整排序或未来积分；量词结构（每段接续都有某种生成，而没有一种固定形态遍及所有接续）；证书可撤回 | G0 为真 |
| [PositionedPositiveReason](../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/PositionedPositiveReason.lean) | 前提足迹：每个能通达回应的位置都有该理由，不论是否认同；这种认同无关性来自 D，不来自 G0 与 E | D 本身的根据 |
| [RenewingFormation](../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RenewingFormation.lean) | 动力学区分：更新型与依存于所耗条件的消耗型形成、共享形成的终止、局部与整体比较的反转 | 外部化的消耗；真实过程对规律的对应；停止的伦理评价 |
| [ProtectionPriorityRival](../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ProtectionPriorityRival.lean) | J2 相对 G0/C 的独立性；被排除的聚合对手类 | 有界敏感性对手；基本分类 |
| [AlignmentDirection](../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/AlignmentDirection.lean)、[PracticalJudgment](../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/PracticalJudgment.lean) | 案例中的判断确由所述前提推出；交叉基本损失不排序 | 前提正确；部署可靠 |

Lean verifies inference, premise footprint, dynamical discrimination and independence. It cannot verify the axiom. The README evidence lines state these roles rather than counts alone.

## 4. 什么会修订 G0 / What would revise G0

1. 一个忠实表示的案例中，更新内、无反向损失的生生不息形成，经过充分审查后仍被判定毫无正面意义，而不只是被其他理由压倒。
2. 一个案例中，整体方向的读法给出的判断，被同一组忠实事实显示为错误，而 J1–J4 无法说明这一差异。
3. 一个对手能以更少或更弱的承诺解释 §2.1 的同一范围，并在 §2.2–§2.3 的判别案例中至少同样好。
4. 辩证路线（§2.3）成功，使 G0 降为评价者已有的前提。这不推翻 G0，而是改变它的地位。对持 S0 的评价者，这一改变已在所述前提下部分发生（§2.3）。

## 5. 仍未完成 / Open

普遍实践根据（`universal-practical-warrant`）仍是开放目标。[位置索引的正面理由](../results/records/positioned-positive-reason.md)已检查：每个能通达回应的位置都有该理由，而认同无关性是 D 的内容，不是 G0 的推论。因此“普遍”在形式上有了对应，但它依赖 D；D 本身尚未从行动者自身立场得到论证。§2.2 的规律类没有更新组织的恢复、先冲高后回落的情形，也没有外部化的消耗。各项对应仍需具体证据。

The universal practical warrant remains open. Position-indexed reasons are now checked, and endorsement independence is located in D rather than G0; D itself is not yet argued from an agent's own standpoint.
