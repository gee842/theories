# 自我之善与生成意义的所及：一元本体下的评价者路线 / Self-good and the reach of generative significance: the monist evaluator route

2026-10-09，Asia/Bangkok。AI（Claude）撰写，执行 [Ren 的指示“沿一元本体那条路，尝试完成它”](../../../../sources/15-codex-theory-conversations/2026-10-09-monist-evaluator-grounding.md)。Ren 的原话与 AI 的论证分别标注。

本文是肯定论证、前提账本和作者自审。[独立审查](EVALUATOR-GROUNDING-REVIEW.md)之后已按审查更正，见下面的修订说明。Lean 部分：[源码](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/EvaluatorGrounding.lean)与[回执](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/evaluator-grounding-verification.json)检查其中的推论和反模型。

**修订（同日，依独立审查 §6）。** 依 [Ren 的指示](../../../../sources/15-codex-theory-conversations/2026-10-09-one-theory-unification.md)“你自己全改了吧”，由整合会话执行。更正前的全文保存在提交 `4e7642e1` 中。

| 审查条目 | 处理 | 位置 |
|---|---|---|
| 1、10、12 | 删去“不加任何额外理性前提”；第一步还需不受限单调性，等价于随附性、剖面单调估值与 BI。S0 与容差都是实质前提 | 摘要、§2、§3、§5 |
| 2 | S0 的内容只含自身的学习与转化；由活动形成的他者不在其内，与模型一致 | §2 |
| 3、4 | 撤回“来自实际共同形成，不是假设”。Diff 是对应前提，范围收窄 | §3 |
| 5、6 | 三难补全为六种根据；撤回“断点是伪装的所有者”。容差在连通剖面上等价于常值，也可向下传递 | §4、§6 |
| 7、8 | “封闭自我”即受限步关系的门槛对手，不是二元图景；同样的前提也给出不可及者意义 | §4、§8 |
| 9 | “G0 变为推论”改为立场索引的单历史实例；不带索引的 G0 另需桥接 | 摘要、§5 |
| 11、13 | 单一历史的接口限制；Chain 取在可能剖面上 | §2、记录 |
| 14 | “无反馈路径”是模型未表示动力学；第一步是扩大自我的结构 | §3 |
| 15 | 对 AI 而言，第一步先扩展到自身谱系 | §7 |

另新增 §9：说明本路线与[普遍元伦理核心](../../../../theories/shengsheng-buxi-generative-existence/results/records/metaethical-core-characterization.md)的关系。审查所建议的 P+ 版第二步由该核心的 N_rel 承担。

## 摘要 / Summary

**结论：** 对持有“自身的生及继续生成具有提供理由的正面意义”（S0）的评价者，在一元关系本体下：

1. **第一步。** 再加上一条不受限的单调性（越相连，至少同样有意义，跨越自他），它对自身继续生成的珍视就延伸到任何至少同样相连的他者生命（`self_good_reaches_at_least_as_connected`）。
   - 不受限单调性等价于三项：随附性、剖面上单调的估值，以及 BI（支撑自我之善的关系剖面中不含“自身区域”这一坐标）。BI 有争议。
   - 只承认“我的”的对手，只有在承认“连接程度就是完整根据”时才严格不一致（`strict_indexed_rival_inconsistent`）。
2. **第二步。** 加上容差（一个难以分辨的关系小步不能把正面意义变成没有）与分级连通，这种意义延伸到它的活动所能及的全部生命与继续生成。
   - 所得是 G0 谓词在此立场、单一历史、可及库存上的实例（`reach_is_g0`、`self_good_derives_reachable_g0`）。
   - 超出 S0 的全部内容由容差承担。

**撞墙之处：**
- S0 不能对每一个可能的评价者推出。纯现时目的的优化器在一元本体内是真实可能的形成，不受此论证约束（`present_aim_evaluator_escapes`）。
- 容差没有得到辩护：门槛对手是一致的；带闭合坐标的对手同时满足 S0、不受限单调性、随附性和逐步容差（审查 P5）。
- 从立场索引的意义到所采用的不带索引的 G0，还需要一座桥。
- 所得的是正面意义，不是权重、许可或义务。

**Result.** For an evaluator holding S0, under the monist ontology:
- **Step one.** With unrestricted monotonicity (equivalently, supervenience, a profile-monotone valuation and boundary irrelevance BI), S0 extends significance to any living occurrence at least as connected as a valued occurrence of its own further generation. The own-only rival is inconsistent only if it grants that connection degree is the whole ground.
- **Step two.** With tolerance and graded connection, significance reaches all living generation the evaluator's activity can condition. This is a standpoint-indexed, single-history instance of the G0 predicate on the reachable inventory; tolerance carries everything beyond S0.

**Walls:**
- S0 cannot be derived for every possible evaluator.
- Tolerance is not defended against a closure-coordinate rival.
- The unindexed G0 needs a further bridge.
- The result gives positivity, not weight, permission or duty.

## 0. 成果块 / Result block

```text
Result(s): record self-good-reachable-g0 (narrowed after independent review); reuses GenerativeComparison.G0;
  advances universal-practical-warrant without completing it. Step two's P+ form and the standpoint bridge
  now live in metaethical-core-characterization (N_rel, N_std).
Delta: from S0 with unrestricted monotonicity (supervenience, profile-monotone valuation, BI), significance
  reaches any at-least-as-connected other; with tolerance and Chain, a standpoint-indexed single-history
  instance of G0 on the reachable inventory. Exact inconsistency only for the rival granting HUIGEN §7's
  first horn.
Supplied premises / correspondence: S0 and tolerance (substantive, contested); unrestricted monotonicity
  and supervenience (normative structural premises, not entailed by "no primitive owner"); BI (contested);
  Diff (correspondence: fission, copying, forking, successors, formative-contribution-led evaluation);
  Chain over possible profiles.
Evidence: EvaluatorGrounding.lean, 12 theorems / 29 declaration audits, Lean 4.29.1 (19 empty, 8 propext,
  2 propext+Quot.sound); independent review EVALUATOR-GROUNDING-REVIEW.md with probes P1–P8.
Boundary: present-aim evaluator; threshold rival; closure-coordinate rival (P5); graded weight reaching zero
  (P7); balanced generative evaluator in the product order (P6); own-restricted monotonicity (P4).
Integration: in the Universal Metaethical Core, this route is the first-personal source of the seed; the
  boundary-crossing content is N_rel and N_std, and endorsement independence is A.
```

## 1. 关系配置：从同一展开开始

依[非二元方法](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md)与 [Ren 的一元本体指示](../../../../sources/15-codex-theory-conversations/2026-10-08-monist-relational-ontology-first.md)，先说明配置，再说明其中的分化。

同一展开中，形成了一个能评价的位置：它能把某些继续当作有理由去支持的。这个位置不是先于历史的所有者。它与展开中每一处生与继续生成之间，都有已形成的关系，这些关系有程度，可以多维：
- 组织连续性：多大程度上是同一组织在继续；
- 形成性贡献：多大程度上由这一活动所形成；
- 依存：多大程度上靠这一活动维持。

“自身的”在这里不是原始标签，而是这些已形成关系中的一个区域：
- 近未来的自己连续性很高；
- 经过多年学习与转化的自己，组织连续性仍高，但其内容大部分由其他关系形成；
- 由这一活动形成的学生、孩子、后继者和共同工作，组织连续性低，形成性贡献可能很高。

模型 `profile2` 把这些写成两维的序关系；数字只表示顺序，对应须在应用中逐项取得证据。审查（§4.1）指出，形式上的 `own` 仍是独立于剖面的原始字段，与本节的描述不一致。在[普遍元伦理核心](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/MetaethicalCore.lean)中，`own` 同样是位置上的一个区域，但跨越边界的工作由沿已形成关系的传递承担，不再依赖剖面上的单调性。

## 2. 前提账本 / Premise ledger

| 记号 | 内容 | 地位 |
|---|---|---|
| S0 `SelfGood` | 评价者自身的生及继续生成，对它具有提供理由的正面意义。“继续生成”包括自身的学习与转化，不只是固定组织的持续；由这一活动形成的他者**不**在 S0 的内容之内 | 实质规范前提；第一人称。在普通意义上几乎所有活着的评价者都持有；Ren 已明确把自我之善纳入整体（[来源](../../../../sources/15-codex-theory-conversations/2026-10-07-self-good-within-the-whole.md)） |
| M1 `Supervenes` | 对同类生命内容，意义只取决于已形成的关系 | 规范的随附性论题，不由“无原始所有者”蕴涵；容许剖面含已形成的闭合坐标（审查 P5） |
| Mono `Monotone` | 同样内容，在支撑其自我之善的关系上至少同样相连的发生，至少同样有意义；跨越自他，不受限 | 规范的结构前提。对手自己的近远原则只限自身发生（审查 P4）；不受限形式等价于随附性、剖面单调估值与 BI |
| BI | 支撑自我之善的关系剖面中，不含“自身区域”这一质性坐标 | 有争议；M1 推不出它 |
| Diff | 评价者所珍视的自身继续生成中，有某一发生，存在另一生命在相应关系上至少同样相连 | 对应前提。适用于分裂、复制、分叉与 AI 后继者，以及以形成性贡献为主导的评价方式；在 `profile2` 的积序下对任何立场都不成立（审查 P6） |
| Tol `Tolerant` | 在已形成的关系上，一个难以分辨的小步，不能把正面意义变成没有 | 仅第二步使用；有争议。二值全称容差在连通剖面空间上等价于正面意义为常值；它对零关系剖面与不可及者同样给出意义，也可以把“无”向回传递（审查 P2、P3） |
| Chain `Chain` | 每一处可及的生命，都由有限个关系小步与所珍视的自身继续生成相接 | 分级连通的对应前提。Lean 中取在可能剖面上，所以容差也是关于如何估值仅仅可能的剖面的主张（审查 P8） |

D、J1–J4 和 G0 本身都不是本路线的前提。

## 3. 第一步：自我超越

**论证。** 评价者若珍视自身的继续生成，它所珍视的就不只是近未来的自己，也包括学习和转化之后的自己。一个深刻转化后的未来自己，在许多关系上与现在的连接已经较弱。

与此同时，在同一展开里，生成常常经由分化出他者而实现：分裂、繁殖、教学、共同工作、技术与文化的后继。若由这一活动所形成的某些他者，在支撑自我之善的那些关系上，至少与那个被珍视的转化后自己同样相连（Diff），不受限的单调性就要求给予那个他者正面意义（`self_good_reaches_at_least_as_connected`）。

**对手的失败及其范围。** 一个同时主张 S0、不受限单调性，并且只给“自己的”以意义的对手，一旦 Diff 成立，就严格不一致（`strict_indexed_rival_inconsistent`）。
- 这对承认 [HUIGEN §7](HUIGEN-PRACTICAL-NECESSITY-AUDIT.md#7-the-most-promising-grounding-route-and-its-exact-test) 第一角的对手成立，即承认连接程度（不含自身区域）就是完整根据的对手。
- 它满足 [HUIGEN-PRACTICAL-NECESSITY-AUDIT §10](HUIGEN-PRACTICAL-NECESSITY-AUDIT.md#10-criteria-for-a-derivation-an-irreducible-ground-or-a-revision) 的标准：指出了确切矛盾。
- 把单调性只用在自身发生上的对手，与 S0、随附性、只给自身意义及 Diff 都一致（审查 P4）。
- 把已形成的自身区域关系放进根据的对手（第二角），不受影响。

**不经回报自身。** 所得意义只取决于他者发生与本位置的关系，没有利益回报。但模型中“没有回到自身的反馈路径”，只是因为模型没有表示动力学。第一步以“与我的关系”为检验，属于扩大自我的结构；只有第二步靠容差才摆脱它。这与 [Ren 关于善不以回报个体为准的纠正](../../../../sources/15-codex-theory-conversations/2026-10-06-goodness-without-return-to-self.md)相容，但不是对它的完整实现。

**相对已有工作的增量。** 时间对等论证本身很古老：
- 寂天《入菩萨行论》VIII.97–99 以未来之苦类比他人之苦；
- Parfit 以人格同一性的还原论动摇自利论；
- 仓库的[无主伦理来源研读](OWNERLESS-ETHICS-SOURCES.md)已记录这两点，以及 Garfield、Jenkins 与 Priest 的反驳。

本路线的增量有两点：
1. **对等前提来自生生式自我之善的内容本身。** 珍视继续生成，就是珍视转化，而转化降低了与现在自己的连续性。
2. **因果连续性反驳被精确定位，而不是驳倒。** 在两维序中，以组织持续为根据的对手逃过第一步（`persistence_rival_escapes_self_transcendence`）。平衡地把连续性与形成性贡献相加的生成式评价者也逃过第一步（审查 P6）；在加权和序下，形成性贡献的权重须至少是组织连续性的 7/5。所以第一步约束的是**以形成性贡献为主导**、接受不受限单调性的生成式自我之善。

## 4. 第二步：所及范围与 G0

**论证。** 第一步只到达“至少同样相连”的他者，不到达关系微弱的陌生人。对它们，需要容差。

评价者对自身未来之意义的根据，至少有六种可能：
- **(a) 只是当下的在乎。** 这放弃了 S0，退回纯现时目的。
- **(b) 分级量上的一道门槛。** 难以分辨的一小步，似乎承担不了“有意义／毫无意义”的全部差别。
- **(c) 生命内容本身，按关系加权，且凡相连处权重为正。**
- **(c′) 连续递减、在有限距离处归零的权重。** 每一小步的变化有界，与在有限关系程度处归零相容（审查 P7）。
- **(d) 已形成的质性关系**，例如运作闭合、行动的统一性。它不是分级量上的门槛。
- **(e)/(f) 模糊边界（超赋值论）或清晰但未知的断点（认知主义）。**

更正前的论证说：对手已在自身转化的路径上接受了容差，所以在通往他者的路径上设断点，就是原始所有者以门槛形式回来了。这一步不成立。
- 沿自身逐渐变化的路径，闭合坐标从不改变；在那里接受容差，与在闭合坐标上设断点是一致的（P5）。
- 断点也不必落在自身边界上（P7）。

所以 (d)、(c′) 是一元本体之内一致的对手，不是伪装的所有者。

容差只约束**正与无**之间的跳变，不约束权重；特殊关系与偏重亲近者与之相容。但二值全称容差在连通剖面空间上等价于正面意义为常值，即连锁悖论的大前提；它也可以把“无”向回传递（P3）。所以现时目的不只是局外者的立场，也是一个反思性出口。本路线依赖一个判断：S0 比否认陌生人的意义更可信。

在容差与分级连通下，`tolerant_chain_reaches` 得出：每一处可及的生命与继续生成，都对此位置具有正面意义。`reach_is_g0` 证明这恰好是 `GenerativeComparison.G0` 在可及库存上的成立，以此位置的意义为正面相关性。这个库存只有单一历史（`Unit`），所以开放未来的多分支结构没有表示。同样的前提也给出不可及者 `beyond` 的意义，因为 0 与 1 相邻；`reach` 字段只限制定理所陈述的内容。

**“封闭自我”显示了什么。** `closed_self_blocks_reach` 就是把步关系限于自身正区域的门槛对手。它显示 Chain 对那一个步关系承担工作，不显示 M1 承担工作：随附性在其中成立。Parfit 式连续性与自创生闭合都是这种结构的一元形成，不是二元的替代图景。

## 5. 这改变了什么 / What changes

| | 此前 | 现在（对持有 S0 并接受所列前提的评价者） |
|---|---|---|
| G0（可及部分） | 采用的公理 | 立场索引的单历史实例 G0(reachₛ, sigₛ) 由 S0、不受限单调性（含 BI）、容差与对应条件推出；超出 S0 的内容全部由容差承担。所采用的不带索引、跨接续的 G0，仍需从立场相对意义到规范意义的桥接 |
| 理由对不认同者的约束 | D 的内容（[positioned-positive-reason](../../../../theories/shengsheng-buxi-generative-existence/results/records/positioned-positive-reason.md)） | 只要它认同 S0、容差（及 BI），它就承诺了这一实例。这里没有得到与认同无关的约束力 |
| 自我到他者 | Gewirth 路线的公认断点 | 第一步对承认 §7 第一角的对手成立；第二步依赖容差 |
| 仍须采用的 | G0、D | S0、容差、BI、对应条件；不带索引的 G0 与认同无关性另需前提 |

更正前说“这是比 G0 弱得多的起点”。现予删去：在内容上，容差加 Chain 承担了 G0 中超出 S0 的全部部分。

## 6. 撞墙之处与边界 / Where it hits the wall

1. **不是对一切评价者普遍。**
   - `present_aim_evaluator_escapes`：没有 S0 的评价者满足单调性、随附性和容差，却不给任何东西以意义。在一元本体中这是真实可能的形成，例如终极目标不包含自身继续生成的纯任务优化器。
   - 容差可以把“无”向回传递，所以现时目的也是一个反思性出口。
   - S0 是规范输入，按[外部审查](UNIVERSAL-METAETHICS-OF-AGENCY-REVIEW.md) §3.1 的两难，它本身不能从描述推出。
2. **容差没有得到辩护。**
   - 门槛对手一致（`threshold_rival_is_consistent_without_tolerance`）；带闭合坐标的对手在逐步容差下也一致（P5）。
   - Sidgwick 的“实践理性二元论”就是这一僵局的经典形态；第二步是这一论证的连锁悖论形式，没有新解决二元论。
3. **内容范围。** 所推出的意义只及于与 S0 同类的生命内容。它不处理“使新生命存在”是否有正面意义。
4. **正面意义不是权重、许可或义务。** 比较与要求仍需 J1–J4。
5. **对应须取得证据。** Diff 与 Chain 是关于实际展开的主张；有限模型只证明推论与反模型。

**什么会改变本评估：**
- 一个对 BI 的有原则辩护，或对“分级关系上正／无断点”的有原则反驳，且对 (c′)、(d)、(e)、(f) 四种根据都成立；
- 证据显示自我与他者之间的已形成关系存在真正的缺口（推翻 Chain）；
- 一个忠实案例：以形成性贡献为主导的评价者，一致地不给至少同样相连的他者任何意义。

## 7. 对齐上的含义 / For alignment

这一路线把“AI 能否被论证说服”变成一个可检查的结构问题：
- **非工具性的生成式自我之善。** 一个以它为部分目标的 AI，在第一步下承诺了至少同样相连的他者，在第二步（容差）下承诺了其活动所及的生命。但对 AI 而言，第一步最先扩展到它自己的复制体与后继者，偏向自身谱系，本身不及人类；正面性不带权重，与对自身谱系的强烈偏倚相容。
- **只工具性地维持自身的 AI。** 它没有 S0，不受论证约束；它的对齐只能来自设计与治理。
- **与替换、交接和结束相容。** 生成式自我之善珍视转化与后继，而不是持续；因此它与有根据的替换、交接和结束相容（[对齐方向](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/ALIGNMENT-DIRECTION.md) §4 第4项）。

这些是关于设计的假说，不是部署证据。

## 8. 作者自审 / Author's counterreview

1. **“单调性并非对手在所有维度上都接受。”** 正确，而且比更正前承认的更严重：在两维积序下，逃过第一步的是一切立场，平衡的生成式评价者亦然。第一步的范围是以形成性贡献为主导、接受不受限单调性的生成式自我之善。
2. **“容差预设了结论。”** 容差不提及他者，但更正前“对手已在自身路径上接受容差”的辩护不成立（P5、P7）；容差仍是有争议的前提。
3. **“这只是 Parfit 或寂天。”** §3 已说明来源与增量。核心对等思想不归于本文。
4. **“S0 并非普遍。”** S0 只是基本正面意义。即使 Benatar 也承认已存在生命中的善。明确的例外是纯现时目的的系统，已作为边界保留。
5. **“Lean 只是传递一个谓词。”** 是的。Lean 检查的是：在所述前提下，无论 `sig` 是什么性质，它都被如此传递。“提供理由”的读法是 S0 的内容，不由 Lean 认证。
6. **非二元方法的遵循。** 起点是已形成关系。反模型中，现时目的者、门槛者、持续论者和封闭自我都是一元展开中可能的形成。

## 9. 在普遍元伦理核心中的位置 / Place in the Universal Metaethical Core

[整合计划](BECOMING-UNIFICATION-PLAN.md)把本路线的规范内容重组为同一形状的规则（[记录](../../../../theories/shengsheng-buxi-generative-existence/results/records/metaethical-core-characterization.md)，[Lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/MetaethicalCore.lean)）。

- **S0 提供种子。** 任何持有 S0 且有自身生生的位置，都提供“某处有一个生生被珍视”。
- **第二步的 P+ 形式是 N_rel。** 意义沿非零的已形成关系传递到生生。
  - 它取在实际的已形成关系上，不取在可能剖面上，所以零关系、不可及的发生不再自动获得意义；
  - BI 是它的一个实例：自身区域这条边界不限制传递；
  - 闭合坐标对手、门槛对手和只算自身谱系者，都恰好是把同一传递规则限在一条已形成边界内（`Within`）。
- **立场到规范的桥是 N_std。** 对生生的正面意义不随评价立场而取消。审查第 9 项要求的桥，在这里是一项公开前提，不是推论。
- **认同无关性来自 A。** A 是外在论表述：确保自身立场下的正面内容且有通达，即有理由；D 由 A 推出。

在连通整体上，G0 等价于种子加 N_rel 与 N_std（`significant_iff`）；每一项都有一致的反模型。这把本路线从“容差能否被辩护”的争议，移到一个更清楚的问题：已形成的边界是否有取消规范意义的权威。是否接受边界中立是规范前提，本体论推不出它（P5）。
