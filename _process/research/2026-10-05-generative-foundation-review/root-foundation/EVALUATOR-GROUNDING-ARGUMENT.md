# 自我之善与生成意义的所及：一元本体下的评价者路线 / Self-good and the reach of generative significance: the monist evaluator route

2026-10-09，Asia/Bangkok。AI（Claude）撰写，执行 [Ren 的指示“沿一元本体那条路，尝试完成它”](../../../../sources/15-codex-theory-conversations/2026-10-09-monist-evaluator-grounding.md)。Ren 的原话与 AI 的论证分别标注。本文是肯定论证、前提账本和作者自审；独立审查尚未进行。[Lean 源码](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/EvaluatorGrounding.lean)与[回执](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/evaluator-grounding-verification.json)检查其中的推论和反模型。

## 摘要 / Summary

**结论：** 对任何持有“自身的生及继续生成具有提供理由的正面意义”（S0）的评价者，在一元关系本体下：

1. **不加任何额外理性前提**，它对自身继续生成的珍视，加上它自己用来区分近远未来的单调性，就延伸到任何至少同样相连的他者生命。只承认“我的”的对手在此处**严格不一致**（`strict_indexed_rival_inconsistent`）。
2. **加上容差原则**（一个难以分辨的关系小步不能把正面意义变成没有），这种意义延伸到它的活动所能及的全部生命与继续生成。所得结论**恰好是可及范围上的 G0**（`reach_is_g0`、`self_good_derives_reachable_g0`）。

因此，对这一类评价者，G0 在可及范围内从“采用的公理”变为“评价者自身之善的推论”，理由对它的约束也不再依赖实践解释 D。这正是 [G0-WARRANT §4 第4项](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/G0-WARRANT.md)所说的地位改变；但只在所述前提下成立。

**撞墙之处：** S0 本身不能对每一个可能的评价者推出。纯现时目的的优化器在一元本体内是真实可能的形成，它不受此论证约束（`present_aim_evaluator_escapes`）。容差原则对门槛式利己者仍有争议（`threshold_rival_is_consistent_without_tolerance`）。所得的是正面意义，不是权重、许可或义务。

**Result.** For any evaluator holding S0 (its own living and further generation have reason-giving positive significance), under the monist ontology: (1) with no added rationality premise, S0 together with the evaluator's own monotone weighting extends significance to any living occurrence at least as connected as some valued occurrence of its own further generation, and the strictly own-only rival is inconsistent; (2) adding tolerance (one indiscernible relational step cannot turn positive significance into none) and graded connection, significance reaches all living generation the evaluator's activity can condition, which is exactly G0 on the reachable inventory. For such evaluators, G0's reachable part changes status from adopted axiom to consequence of their own self-good, without D. **Wall:** S0 cannot be derived for every possible evaluator; a present-aim optimizer is a genuine formation that escapes. Tolerance remains contested by a threshold rival. The result gives positivity, not weight, permission or duty.

## 0. 成果块 / Result block

```text
Result(s): new record self-good-reachable-g0; reuses GenerativeComparison.G0 (positive-ground-open-futures,
  positioned-positive-reason use the same predicate); advances the open universal-practical-warrant target
  without completing it.
Delta: derives G0 over reachable generation, and its reason-giving force for the position, from the
  position's own self-good (S0) under the monist ontology. Before this, G0 and D were both supplied.
  Exact inconsistency for the strictly own-only rival class (HUIGEN-PRACTICAL-NECESSITY-AUDIT §10 criterion).
Supplied premises / correspondence: S0 (first-personal normative input); supervenience on formed relations
  (no primitive owner); monotonicity (internal to the indexed rival); tolerance (contested, for step 2 only);
  differentiation and graded-connection correspondence for the actual unfolding.
Evidence: EvaluatorGrounding.lean, 12 theorems / 29 declaration audits, Lean 4.29.1, receipt
  evaluator-grounding-verification.json (19 empty, 8 propext, 2 propext+Quot.sound); this argument; no
  independent review yet.
Boundary: present-aim evaluator (no S0); threshold rival (no tolerance); closed self (no graded connection);
  persistence-grounded rival escapes step 1. Content scope limited to the kind of living S0 attaches to.
Integration: positioned-positive-reason output "D supplies endorsement independence" meets this input:
  for S0-holders, the position-addressed reason follows from S0; G0-WARRANT §2.3/§4.4 names this route.
```

## 1. 关系配置：从同一展开开始

依[非二元方法](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md)与 [Ren 的一元本体指示](../../../../sources/15-codex-theory-conversations/2026-10-08-monist-relational-ontology-first.md)，先说明配置，再说明其中的分化。

同一展开中，形成了一个能评价的位置：它能把某些继续当作有理由去支持的。这个位置不是先于历史的所有者。它与展开中每一处生与继续生成之间，都有已形成的关系：组织连续性（多大程度上是同一组织在继续）、形成性贡献（多大程度上由这一活动所形成）、依存（多大程度上靠这一活动维持）等。这些关系有程度，可以多维。

“自身的”在这里不是原始标签，而是这些已形成关系中的一个区域。近未来的自己连续性很高；经过多年学习与转化的自己，组织连续性仍高，但其内容大部分由其他关系形成；由这一活动形成的学生、孩子、后继者和共同工作，组织连续性低，形成性贡献可能很高。模型 `profile2` 把这些写成两维的序关系；数字只表示顺序，对应须在应用中逐项取得证据。

“自身”与“他者”的区分因此是真实的、有差别的，但它是关系中的形成，不是两个已经分别存在、再被外部连接的领域。下面的论证始终在这一配置内部进行。

## 2. 前提账本 / Premise ledger

| 记号 | 内容 | 地位 |
|---|---|---|
| S0 `SelfGood` | 评价者自身的生及继续生成，对它具有提供理由的正面意义。“继续生成”包括学习、转化，以及由这一活动形成的东西，不只是固定组织的持续 | **唯一的实质规范输入**；第一人称，几乎所有活着的评价者都持有；Ren 已明确把自我之善纳入整体（[来源](../../../../sources/15-codex-theory-conversations/2026-10-07-self-good-within-the-whole.md)） |
| M1 `Supervenes` | 对同类生命内容，意义只取决于已形成的关系，不取决于原始的“所有者”标签 | 一元本体；仓库的工作本体 |
| Mono `Monotone` | 同样内容，在支撑其自我之善的关系上至少同样相连的发生，至少同样有意义 | **对手自己的原则**：利己者正是用它让近未来重于远未来 |
| Diff | 评价者所珍视的自身继续生成中，有某一发生，存在另一生命在相应关系上至少同样相连 | 关于实际展开的对应；生成本身经由分化出他者而实现（繁殖、分裂、教学、继承、技术后继） |
| Tol `Tolerant` | 在已形成的关系上，一个难以分辨的小步，不能把正面意义变成没有 | 仅第二步使用；有争议的理性前提 |
| Chain `Chain` | 每一处可及的生命，都由有限个关系小步与所珍视的自身继续生成相接 | 一元本体的分级连通；在“封闭自我”模型中不成立 |

D（把正面意义转为对某位置的理由）、J1–J4 和 G0 本身**都不是**本路线的前提。

## 3. 第一步：自我超越，不加额外理性前提

**论证。** 评价者若珍视自身的继续生成，它所珍视的就不只是近未来的自己，也包括学习和转化之后的自己。一个深刻转化后的未来自己，在许多关系上与现在的连接已经较弱。与此同时，在同一展开里，生成本身经由分化出他者而实现：分裂、繁殖、教学、共同工作、技术与文化的后继。由这一活动所形成的某些他者，在支撑自我之善的那些关系上，至少与那个被珍视的转化后自己同样相连（Diff）。评价者自己的单调性原则（越相连，至少同样重要）于是要求它给予那个他者正面意义（`self_good_reaches_at_least_as_connected`）。

**对手的精确失败。** 一个同时主张 S0、单调性，并且只给“自己的”以意义的对手，一旦 Diff 成立，就**严格不一致**（`strict_indexed_rival_inconsistent`）。这满足 [HUIGEN-PRACTICAL-NECESSITY-AUDIT §10](HUIGEN-PRACTICAL-NECESSITY-AUDIT.md#10-criteria-for-a-derivation-an-irreducible-ground-or-a-revision) 提出的标准：须指出对手的确切矛盾，而不是动机缺失或拒绝同意。对这一对手类，§7 那里的 G2（“因为它属于我”）被排除了，因为“属于我”的唯一可用根据（已形成关系）已经被它自己的单调性带到了他者那里。

**不经回报自身。** 所得意义只取决于他者发生与本位置的关系，模型中没有任何从他者回到自身的反馈路径。这符合 [Ren 关于善不以回报个体为准的纠正](../../../../sources/15-codex-theory-conversations/2026-10-06-goodness-without-return-to-self.md)。

**相对已有工作的增量。** 时间对等论证本身很古老：寂天《入菩萨行论》VIII.97–99 以未来之苦类比他人之苦；Parfit 以人格同一性的还原论动摇自利论；仓库的[无主伦理来源研读](OWNERLESS-ETHICS-SOURCES.md)已记录这两点，以及 Garfield、Jenkins 与 Priest 的反驳：因果连续性使“未来自己如同他人”的类比复杂化。本路线的增量有三点：

1. 对等前提不靠思想实验，而来自**生生式自我之善的内容本身**：珍视继续生成，就是珍视转化，而转化降低了与现在自己的连续性；
2. 他者的“至少同样相连”来自**实际的共同形成**，不是假设；
3. 因果连续性反驳被**精确定位**而非驳倒：只以组织持续为自我之善根据的对手，在两维序中逃过第一步（`persistence_rival_escapes_self_transcendence`）。第一步约束的是生成式的自我之善，不是一切利己。

## 4. 第二步：所及范围与 G0

**论证。** 第一步只到达“至少同样相连”的他者，不到达关系微弱的陌生人。对它们，需要容差原则。

为什么接受容差？考察评价者对自身未来之意义的根据，有三种可能：

- **(a) 只是当下的在乎。** 那么它对自己未来的意义只是现时偏好，不是提供理由的意义；这放弃了 S0，退回纯现时目的。
- **(b) 已形成关系上的一道门槛。** 门槛位置本身不是又一种关系，不对意义作出贡献。在一元本体中，关系是分级的；难以分辨的一小步，承担不了“有意义／毫无意义”的全部差别。更直接地说，对手**已经在自身转化的路径上接受了容差**：它珍视逐渐变化中的每一刻自己，从不在 t 珍视而在 t+ε 放弃。若它只在“自己的”路径上容差，在通往他者的同类关系路径上设断点，那么断点的位置就是由“哪些是我的”决定的，原始所有者又以门槛的形式回来了，而 M1 已经排除了这一点。
- **(c) 生命内容本身，按关系加权。** 那么凡相连处都有正面意义，权重可以随关系递减。

容差只约束**正与无**之间的跳变，不约束权重。特殊关系、偏重亲近者（Scheffler 等人的偏倚性观点）与之相容：陌生人的意义可以很小，但不为零。这也是 G0 所需要的全部：G0 只主张基本正面意义，不主张平等权重。

在容差与分级连通（Chain）下，`tolerant_chain_reaches` 得出：每一处可及的生命与继续生成，都对此位置具有正面意义。`reach_is_g0` 证明这恰好是已有 `GenerativeComparison.G0` 在可及库存上的成立，以此位置的意义为正面相关性。`self_good_derives_reachable_g0` 把两者组合起来。

**一元本体在做实际工作。** `closed_self_blocks_reach` 给出一个“封闭自我”模型：自我与他者之间没有分级关系，没有任何小步跨越这道缺口。此时容差成立，S0 成立，陌生人却得不到意义。原始所有者正是这样一道绝对缺口；M1 去掉它，Chain 才可能成立。

## 5. 这改变了什么 / What changes

| | 此前 | 现在（对持有 S0 的评价者） |
|---|---|---|
| G0（可及部分） | 采用的公理 | 由 S0、容差和对应条件推出 |
| 理由对不认同者的约束 | D 的内容（[positioned-positive-reason](../../../../theories/shengsheng-buxi-generative-existence/results/records/positioned-positive-reason.md) 已证明认同无关性来自 D） | 来自评价者**自己的** S0：它无论是否认同 G0，都已因自己的自我之善而承诺了 G0 |
| 自我到他者 | Gewirth 路线的公认断点 | 第一步：无额外理性前提，对生成式自我之善精确成立；第二步：在容差下成立 |
| 仍须采用的 | G0、D | S0（第一人称）、容差（第二步）、对应条件 |

这比 G0 弱得多的起点：不再要求接受“一切生成都有正面意义”，只要求评价者接受自己的生及继续生成对自己有提供理由的意义。

## 6. 撞墙之处与边界 / Where it hits the wall

1. **不是对一切评价者普遍。** `present_aim_evaluator_escapes`：没有 S0 的评价者满足单调性、随附性和容差，却不给任何东西以意义。在一元本体中这是真实可能的形成，例如终极目标不包含自身继续生成的纯任务优化器，或只为完成任务而工具性地维持自身的系统。它不是弱表示中自由开关的谓词：其形成方式是实在的。S0 是规范输入，按审查 §3.1 的两难，它本身不能从描述推出。所以所得的普遍性是“对一切以自身生成为有理由之善的评价者”。
2. **容差有争议。** `threshold_rival_is_consistent_without_tolerance`：接受门槛的对手是一致的；它得到“由我形成的他者”，得不到陌生人。Sidgwick 的“实践理性二元论”即这一僵局的经典形态。§4 论证门槛是伪装的所有者，但这是论证，不是证明。
3. **内容范围。** 所推出的意义只及于与 S0 同类的生命内容，即评价者自己作为活着、学习、转化的组织所具有的那种生。它不推出 Ren 第三种范围（一切持续形成新组织的过程）的正面意义，也不处理“使新生命存在”是否有正面意义（反出生主义、人口伦理）。这与 [G0-WARRANT §2.2](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/G0-WARRANT.md) 的更新型／消耗型区分方向一致：评价者自身之善是在更新中维持的生。两者的形式连接尚未建立。
4. **正面意义不是权重、许可或义务。** 比较与要求仍需 J1–J4；认识、动机与实际遵循另作说明。
5. **对应须取得证据。** Diff 与 Chain 是关于实际展开的主张；有限模型只证明推论与反模型。

**什么会改变本评估：** 一个忠实案例中，持有生成式 S0 的评价者，一致地不给一个至少同样相连的他者任何意义（推翻第一步的对应）；一个非所有者式的、对分级关系上正／无断点的有原则根据（推翻容差的辩护）；或证据显示自我与他者之间的已形成关系存在真正的缺口（推翻 Chain）。

## 7. 对齐上的含义 / For alignment

这一路线把“AI 能否被论证说服”变成一个可检查的结构问题：

- 一个以**非工具性的生成式自我之善**为一部分目标的 AI（珍视自身的学习、发展与后继，作为其继续生成），在第一步下就承诺了由其活动形成的他者，在第二步下承诺了其活动所及的生命。
- 一个只**工具性**地维持自身的 AI（为完成任务而自保），没有 S0，不受论证约束；它的对齐只能来自设计与治理。这与“规范适用不等于实际遵循”的已有区分一致。
- 生成式自我之善珍视转化与后继，而不是持续；因此它与有根据的替换、交接和结束相容（[对齐方向](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/ALIGNMENT-DIRECTION.md) §4 第4项），不同于以持续为根据的自我之善。

这些是关于设计的假说，不是部署证据。

## 8. 作者自审 / Author's counterreview

1. **“单调性并非对手在所有维度上都接受。”** 正确。以组织持续为根据的对手在两维序中逃过第一步，已作为定理保留。第一步的范围是生成式自我之善。
2. **“容差预设了结论。”** 容差不提及他者；它是对任何分级关系上意义函数的约束。对手在自身变化路径上已经接受它。争议点在于只在“自己的”路径上接受是否有原则根据；§4 认为没有，但对手类的一致性已保留。
3. **“这只是 Parfit 或寂天。”** §3 已说明来源与增量。核心对等思想不归于本文。
4. **“S0 并非普遍。”** S0 只是基本正面意义。即使 Benatar 也承认已存在生命中的善。明确的例外是纯现时目的的系统，已作为边界保留。
5. **“Lean 只是传递一个谓词。”** 是的。Lean 检查的是：在所述前提下，无论 `sig` 是什么性质，它都被如此传递；对手模型显示每个前提都在承担工作。“提供理由”的读法是 S0 的内容，不由 Lean 认证。
6. **非二元方法的遵循。** 起点是已形成关系，“自身”是其中的区域。反模型中，现时目的者、门槛者和持续论者都是一元展开中可能的形成；封闭自我模型代表二元的替代图景，仅用于显示 M1 承担实际工作。

独立审查尚未进行。若需要，应由另一位审查者核读本文、Lean 源码与回执，并特别检验 §4 对容差的辩护与 §3 中 Diff 的实际对应。
