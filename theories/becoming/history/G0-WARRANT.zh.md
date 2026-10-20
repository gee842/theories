<a id="g0-的根据一项采用的公理怎样得到支持--the-warrant-for-g0-how-an-adopted-axiom-is-supported"></a>
# G0 的根据：一项采用的公理怎样得到支持

> **中文版（2026-10-17）。** 正典文本是[英文版](G0-WARRANT.md)；本版由重构时从双语原文拆出，不与英文同步维护，两者有出入时以英文为准。

2026-10-09，Asia/Bangkok。AI（Claude）撰写，执行 [Ren 的指示](../../../sources/15-codex-theory-conversations/2026-10-09-lean-evidence-roles.md)。本章不证明 G0，也不把它从公理改成定理。它整理适合于一项采用公理的支持，说明形式检查在其中各承担什么，并写明什么结果会修订它。Ren 的原话与 AI 的重构分别标注；[外部视角审查](../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/UNIVERSAL-METAETHICS-OF-AGENCY-REVIEW.md)与[区分内容整合](../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/GENERATIVE-DISCRIMINATION-INTEGRATION.md)记录了本章的起因与新证明。

<a id="1-地位--status"></a>
## 1. 地位

**G0：整体中的生及其继续生成具有基本正面规范意义。** 这是对 Ren 输入的 AI 重构。2026-10-08 Ren 明确：“当然，这种地方需要有axiom才行，不要继续白费功夫”（[来源](../../../sources/15-codex-theory-conversations/2026-10-08-alignment-grounding-axiom-correction.md)）。审查 §3.1 的修订说明了为什么：规范谓词与描述关系之间的连接，要么不存在，此时描述推不出规范结论；要么由前提、定义或构成性同一给出，此时这一连接本身就是承诺。审查附录用 Lean 检查了这一两难的形式核心。Kant、Gewirth、Parfit、功利主义与契约主义都有自己的起点；因此，有一项公理本身不构成相对于对手的缺陷。

G0 的对象从一开始就是生生。Ren 追问：“我G0是什么？generative和degenerate虽然都在一个becoming model上，但是他们不overlap吧”（[来源](../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md#ren-follow-up)）。生成与退化作为关系不重叠，但一次发生可以同时参与二者。把形式库存中的 `generative` 读成“任何已实现的新组织”，是 AI 的宽读法，不是 G0。

G0 只给出效价：实现了的生及继续生成有正面意义。把它变成某一位置的理由，靠的是直接实践解释 D／P；把各种理由变成比较与要求，靠的是 J1–J4；把它们用于具体处境，靠的是对应条件 E。下面各节分别说明这些承诺获得支持的方式。

<a id="2-支持的四种方式--four-kinds-of-support"></a>
## 2. 支持的四种方式

<a id="21-解释统一--explanatory-unification"></a>
### 2.1 解释统一

照护、修复、创造、学习、更新、休息、有限完成与建设性结束，都可以从同一根据得到说明，而无须分别假定各自独立的内在价值（[前提推导](../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/GENERATIVE-PREMISE-DERIVATION.md) §§1、3；[对齐方向](ALIGNMENT-DIRECTION.md) §1）。自我照护被纳入，不必先产生外部收益；结束被纳入，不必先证明旧安排永久无用。若一种对手需要更多相互独立的起点才能解释同样的范围，这就是支持 G0 的比较理由。

<a id="22-区分力--discriminating-content"></a>
### 2.2 区分力

若把形式 G0 的库存读宽，使每一项实现了的新组织都算作生成内容，形式 G0 就会把同样的正面意义给予那些持续形成新组织、却毁坏其依存条件的过程。肿瘤式增殖是这样，把代价外部化的竞争性扩张也是这样；后者不在下面的规律类中，见本节“这一区分的范围”。

这是宽读法的问题，不是 G0 的问题（§1）。Ren 的判准是整体的：“一种整体的，不断创造更多生的方向”，并且明确不缩成“已被独立判好的可能性”（[原话](../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md)）。

问题因此是：能否不借先行的好坏筛选，以可检查的描述性内容认出哪些形成属于生生？[RenewingFormation.lean](../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RenewingFormation.lean) 在一个明确的不可恢复磨损规律类中，以 AI 的两个形式读法回答“能”：

- 形成压力在更新之内时，每步都有形成（`within_renewal_ceaseless`），更新能力保持不变；允许休息时也是如此（`keeps_capacity_iff`）；
- 压力持续超出当前更新速率时，整个展开的累计形成以 `stock + tri renew` 为界，并在这一时刻之前停止（`beyond_current_bounded`、`beyond_current_ceases`）；从第一步超出起，更新能力永久下降（`beyond_loses_capacity_at_once`）；
- 共享这些条件的其他形成，无论怎样分配，都随之停止（`consuming_part_ends_otherwise_ceaseless_formation`）。两个部分各自都在更新之内、只是合起来超出时，也是如此（`jointly_exceeding_parts_end_shared_formation`）；
- 消耗型形成起初可以形成得更多，按一步计数它排在前面；预算之后，每一种更新内的接续都超过每一种超出型接续（`consuming_forms_more_first`、`within_eventually_exceeds_every_beyond`）；
- 逐事件读取的 G0 同时承认两者的形成事件，无损比较 C 在两者之间也不适用，因为互不为生成扩展。分开它们的是动力学性质 `Ceaseless` 与 `KeepsCapacity`（`event_reading_recognizes_both`、`comparison_does_not_apply`、`ceaseless_separates`、`capacity_separates`）。

这些区分是所给规律的推论，规律本身承担了大部分内容。定理按构造对符号中立：哪一侧在 G0 的对象之内，Lean 不提供。

- 生生有正面意义，就是 G0 本身，不是另欠的前提。
- 不是 Lean 结果、须另行承担的有两项。其一，这两个形式读法确实刻画了生生，这是 AI 的读法与对应。其二，“消耗更坏”这一比较由 C 承担。本模块的逐事件宽读法下，C 不适用。在关系读法下，另一会话的 [relational-reading-comparison](../results/records/relational-reading-comparison.md) 已检查：规律族中每一种超出更新的取用，都被 C 严格排在它不发生的接续之下。

两个形式读法各有缺陷。`Ceaseless`（每一步都有形成）捕捉“不息”，但一次休息就使它不成立，而先冲高、再在降低的速率内持续的形成会永久失去更新能力，它却仍然成立（`rest_keeps_capacity_not_ceaseless`、`wears_yet_ceaseless`）。`KeepsCapacity`（更新组织保持其速率）容许休息，且在第一步超出时就判定。两者都不表示“更多”或复杂度上升，因为本规律不许更新速率增长。停止本身没有被判为坏的，有限完成、休息与适当结束仍是 G0 所承认的生。不过本表示省略了休息的恢复作用：逐事件读法下，C 甚至把一次休息严格排在持续形成之下（`event_comparison_ranks_rest_below`）。这是表示中省略的关系，不是对理论的反驳。伦理上更尖锐的关系，是终止那些本身并未超出更新的共享形成；对它的判断仍须经 J1／J3 与对应条件。真实过程是否满足所给磨损规律，须各自取得证据。

**这一区分的范围。** 在上述规律类中，消耗者本身依存于它所消耗的条件，因此终将终止自身。另一种情形不在其中：一个形成取用另一关系所依存的条件，自身却不依存于它。它可以每步都在、形成无界，而那一关系永久失去其条件；把代价外部化的“赢家”式扩张，即 meta-attractor 的情形，就是这样。此时，焦点形成自身的 `Ceaseless` 以至总形成的 `Ceaseless`，都识别不出这种消耗。起决定作用的是关系性质：是否有依存的关系永久失去其条件。另一分支的 `relational-renewal-classification`（登记中）在任意展开上给出这一分类，并证明焦点形成自身的活动与形成不决定其类别。因此，“整体方向”须读作每个依存关系的接续，而不是任何一个形成自身的持续或总量的持续。上面的 `ceaseless_separates` 用的是总形成的持续；它之所以足够，是因为本规律类只有一个共享条件，消耗者又依存于它，于是总形成的持续与依存关系的接续恰好一致。在这个规律类之外，二者不一致。

<a id="23-与对手的判别--discrimination-against-rivals"></a>
### 2.3 与对手的判别

**自然数评分与有界评分。** [ProtectionPriorityRival.lean](../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ProtectionPriorityRival.lean) 检查了一个构造的保护对增益情境：

- G0、无损扩展比较 C 与 J2 的排序可同时成立，J2 从不以任何数量的增益交换基本条件（`livingSignificance_leaves_ordering_open`、`priority_never_trades`）；
- G0 只约束正面相关性，不约束排序：它同样与一个满足 C、却会交换的排序并存。因此 J2 不由 C 推出；说它“不由 G0 推出”是平凡的（`comparison_does_not_yield_priority`）；
- 每一个满足 C 的自然数评分都会在 `score 0 + 2` 项增益处交换（`every_nat_score_trades`）。起作用的是严格递增的自然数评分每步至少加一；
- 一个有界的有理评分（保护为 1，`k` 项增益为 `k/(k+1)`）满足 C、从不交换，并在每一对选项上与 J2 一致（`ratio_agrees_with_priority`、`bounded_score_represents_priority`）。

因此，这个情境把 J2 与自然数值（单位步长）评分分开，却分不开 J2 与有界、边际递减的评分。后者在此恰好表示 J2，仍是实质对手；要分开它们，需要别的情境。J2 不由 C 推出，是“C 对取舍不置可否”这一既有结果在保护对增益情境中的实例：`both_appraisals_respect_all_extensions`、`tradeoff_has_opposite_strict_appraisals`、`loss_sensitivity_alone_supplies_no_cutoff` 已有此意，`compatible_cutoffs_disagree` 与 `both_tradeoff_options_survive` 也相关。`no_protection_trade_by_count` 给出 J2 的不交换性质。新增的是三点：J2 在此满足 C；自然数评分不能表示 J2；有界评分能。

**以后来认可为最终尺度。** [生成对齐修订](../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/GENERATIVE-ALIGNMENT-REVISION.md)中的对手一主张，后来的充分认可就足以证明形成过程正当。本框架拒绝其充分性：后来无异议不会使已发生的损失没有发生，J2 也不允许以更多认可换取仍存在的基本剥夺。

**Gewirth 与辩证路线。** Gewirth 试图从任何目的性行动者已有的承诺推出普遍原则，而不另设价值公理（[来源研读](../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/NORMATIVE-WARRANT-SOURCES.md) §1）。他的论证公认在“我需要 X”到“他人也应尊重每个人的 X”这一步上有争议。审查 §3.1 提出一个研究假说：一元关系本体下，评价者自身的评价与延续形成于并依存于与他者的关系，阻断这一步的自我边界并不是给定的。若这条路走通，G0 可以降为接近“构成我之评价的那些生成关系的延续”，所支持的也正是 §2.2 中的更新型形成。这是待证目标（`universal-practical-warrant`，open），不是成果。

**2026-10-09 部分完成，经独立审查收窄**（[记录](../results/records/self-good-reachable-g0.md)，[论证](../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/EVALUATOR-GROUNDING-ARGUMENT.md)，[审查](../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/EVALUATOR-GROUNDING-REVIEW.md)）。

起点改为评价者自身的自我之善 S0：它自己的生及继续生成对它有提供理由的意义。
- **第一步。** S0 加上不受限（跨越自他）的单调性，及于至少同样相连的他者。不受限单调性等价于随附性、剖面单调估值与 BI；BI 有争议。只承认“我的”的对手，只有在承认“连接程度就是完整根据”时才严格不一致。
- **第二步。** 加上容差与分级连通，及于全部可及的生命。所得是 G0 谓词的**立场索引的单历史实例** G0(reachₛ, sigₛ)，超出 S0 的全部内容由容差承担。
- **仍需桥接。** 所采用的不带索引、跨接续的 G0，仍需从立场相对意义到规范意义的桥接。
- **约束力取决于认同。** 理由对一个位置的约束，取决于它是否认同 S0、容差（及 BI），不是与认同无关的。
- **墙。** 没有 S0 的现时目的评价者不受约束；容差对闭合坐标与归零权重的对手没有得到辩护；所得是正面意义，不是权重。

**2026-10-09 内容刻画**（[记录](../results/records/metaethical-core-characterization.md)，[Lean](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Metaethics.lean)）。在已形成关系把生生连在一起的整体上，G0 等价于三项合取：
- 某处有一个生生被某立场珍视（种子；持 S0 的位置都提供一个）；
- 正面意义沿非零的已形成关系传递（N_rel）；
- 对生生的正面意义不随立场而取消（N_std）。

D 由外在论表述 A 推出。种子、N_rel、N_std、连通与 A 各有一个一致的反模型；每个规范对手都恰是同一规则加上一条已形成的边界：自身区域、自身立场、认同者。

这不是对 G0 的证明，也不替换 G0。它说明：G0 中超出评价者本来就持有的东西，精确落在“已形成的边界不能取消规范意义”这一前提上。上面评价者路线的容差与 BI、审查要求的“立场到规范的桥”，都是这一形状的规则。Sidgwick 的二元论没有被消解，只被定位到这里。

**构成主义与 shmagency。** 任何论证都不能约束一个不评价任何东西、或对一切延续都漠然的过程。因此即使最强的辩证路线成功，所得也是“对一切评价者普遍”，不是“对一切可能存在普遍”。G0 公开采用，承认这一限度。

<a id="24-对齐上的丰饶性--fruitfulness-for-alignment"></a>
### 2.4 对齐上的丰饶性

在 G0、J1–J4 与 E 之下，人类指令、机构目标和 AI 当前目的都可受伦理评价；一个具体案例已显示，哪些事实变化会改变判断（[对齐方向](ALIGNMENT-DIRECTION.md) §5）。§2.2 的结果为对齐补上一个已检查的警示：按一步的形成计数，消耗型接续排在持续形成之前；而在同一规律下，这种消耗随后会终止共享形成。按每个依存关系的接续来读的整体方向，旨在避免这一错误，所需的区分由 `relational-renewal-classification` 提供。至于哪一种优化目标避免它，尚无已检查的结论：这里没有形式化任何优化器。只看系统自身能否持续，则会漏掉把代价外部化的扩张，以及磨损一次后稳定的情形。

<a id="3-形式检查各承担什么--what-each-formal-check-contributes"></a>
## 3. 形式检查各承担什么

| 检查 | 承担的内容 | 不承担的内容 |
|---|---|---|
| [PositiveGroundUncertainty](../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/PositiveGroundUncertainty.lean) | 前提足迹：正面结论只需 G0 与实际对应，不需整体改善、完整排序或未来积分；量词结构（每段接续都有某种生成，而没有一种固定形态遍及所有接续）；证书可撤回 | G0 为真 |
| [Becoming.Metaethics](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Metaethics.lean) | 内容刻画：连通整体上 G0 ⇔ 种子 ∧ N_rel ∧ N_std；D 由 A 推出；每项前提的极小性，以及对手即有界规则；所见范围由探究的实际执行给出 | 种子、N、A 为真；`living` 即生生的认定；连通的实际对应 |
| [PositionedPositiveReason](../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/PositionedPositiveReason.lean) | 前提足迹：每个能通达回应的位置都有该理由，不论是否认同；这种认同无关性来自 D，不来自 G0 与 E | D 本身的根据 |
| [RenewingFormation](../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RenewingFormation.lean) | 所给不可恢复磨损规律下的描述性区分：两种形式读法（`Ceaseless`、`KeepsCapacity`）、共享与联合超出时共享形成的终止、一步计数与整体比较的反转；逐事件 G0 与 C 都不分开两者 | 形式读法即生生的认定（读法与对应）；“消耗更坏”的比较（由 C 承担，关系读法下见 relational-reading-comparison）；外部化的消耗；“更多”与复杂度上升；真实过程对规律的对应；停止的伦理评价 |
| [ProtectionPriorityRival](../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ProtectionPriorityRival.lean) | 在一个构造情境中：J2 相对 C 的独立性（G0 不约束排序）；自然数评分都交换；有界评分恰好表示 J2 | 把 J2 与有界敏感性对手分开；其他情境；基本分类 |
| [AlignmentDirection](../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/AlignmentDirection.lean)、[PracticalJudgment](../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/PracticalJudgment.lean) | 案例中的判断确由所述前提推出；交叉基本损失不排序 | 前提正确；部署可靠 |

<a id="4-什么会修订-g0--what-would-revise-g0"></a>
## 4. 什么会修订 G0

1. 一个忠实表示的案例中，更新内、无反向损失的生生不息形成，经过充分审查后仍被判定毫无正面意义，而不只是被其他理由压倒。
2. 一个案例中，整体方向的读法给出的判断，被同一组忠实事实显示为错误，而 J1–J4 无法说明这一差异。
3. 一个对手能以更少或更弱的承诺解释 §2.1 的同一范围，并在 §2.2–§2.3 的判别案例中至少同样好。
4. 辩证路线（§2.3）成功，使 G0 降为评价者已有的前提。这不推翻 G0，而是改变它的地位。目前只得到：立场索引的单历史实例由 S0、不受限单调性（含 BI）、容差与对应条件推出；不带索引的 G0 另需立场中立 N_std（§2.3 内容刻画），后者本身是一项规范前提。

<a id="5-仍未完成--open"></a>
## 5. 仍未完成

普遍实践根据（`universal-practical-warrant`）仍是开放目标。[位置索引的正面理由](../results/records/positioned-positive-reason.md)已检查：每个能通达回应的位置都有该理由，而认同无关性是 D 的内容，不是 G0 的推论。因此“普遍”在形式上有了对应，但它依赖 D。内容刻画进一步把 D 分解为外在论表述 A 与立场中立 N_std；二者都是公开前提，都未从行动者自身立场得到论证。§2.2 的规律类没有更新组织的恢复、休息的恢复作用、“更多”或复杂度上升，也没有外部化的消耗；先冲高后回落的情形只由 `KeepsCapacity` 识别，`Ceaseless` 识别不了。§2.3 的情境分不开 J2 与有界敏感性对手。各项对应仍需具体证据。
