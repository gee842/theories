# 评价者路线的独立审查：容差与分化 / Independent review of the evaluator route: tolerance and differentiation

2026-10-09，Asia/Bangkok。**AI 独立审查（另一 agent，未参与撰写）。** 审查对象：[论证](EVALUATOR-GROUNDING-ARGUMENT.md)（sha256 `c5e8fd65…b21c`）、[Lean 源码](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/EvaluatorGrounding.lean)（`86c1583d…218c`）、[回执](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/evaluator-grounding-verification.json)（`95b1df5b…d8fc`）；相关记录 [self-good-reachable-g0](../../../../theories/shengsheng-buxi-generative-existence/results/records/self-good-reachable-g0.json)。本审查只新建本文件；未修改其他仓库文件，未运行 `check_evaluator_grounding.py`、`make research-render` 或检查器，未提交。

## English summary

**Verdicts.** (A) Tolerance: **rejected as defended.** The conditional theorem is valid, but §4 does not establish tolerance against the threshold rival, and the position is worse than §6.2 and §8.2 concede. (B) Differentiation: **accepted with a narrowed scope.** The formulations "no added rationality premise" and "exact inconsistency of the own-only rival" are **rejected** as stated. (C) Formal checks: **accepted.** The independent recompile passes, the source hashes match the receipt, and the axiom dependencies of all 29 declarations match. Correspondence to the prose has several load-bearing gaps that need correction.

**A. Tolerance.** (1) The trilemma in §4 is not exhaustive. It omits four kinds of ground: a formed *qualitative* relation that is not a threshold on a graded quantity (operational closure, unity of agency); a graded weight that falls continuously to zero at a finite distance; a vague boundary with borderline cases (supervaluationism); and a sharp but unknown cutoff (epistemicism). (2) The central move fails. Along the rival's own path of gradual change the closure coordinate never changes, so accepting tolerance there is consistent with a cut on that coordinate (probe P5). The cut also need not coincide with the own boundary (P7), so it is not "ownership in disguise". (3) As formalized, `Tolerant` is vacuous unless `step` is fixed independently of the valuation (P1). On a connected profile space it forces positive significance to be constant (P2). That is the major premise of the sorites. It also entails significance for the zero-relation profile and for the "unreachable" occurrence the model says it does not claim. It propagates "none" backward as readily as "positive" forward (P3), so the present-aim exit becomes a reflective option and not only an outsider's position: this is Parfit's "incompletely relative" pressure. (4) `closed_self_blocks_reach` is the threshold rival with its step relation restricted to its own positive region (P1). It does not show that M1 does work: supervenience holds in it. Parfitian continuity and autopoietic closure are monist, relational formations with exactly this closed structure. Tolerance plus Chain contributes everything in the derived G0 beyond S0, so the starting point is not "much weaker than G0" in content.

**B. Differentiation.** Diff is plausible for evaluators with fission, copy or fork successors, including some AI systems. It is also plausible for evaluators whose self-good is grounded mainly in project or value continuity, or in formative contribution. In the argument's own two-dimensional profile, Diff fails under the product order for *every* standpoint (P6). Under a weighted sum it holds only if formative contribution is weighted at least 7:5 over organizational continuity. A balanced generative evaluator escapes step 1, not only the persistence rival. The Lean `Monotone` ranges over own *and* other occurrences, whereas the rival's own near-over-far principle ranges over own occurrences only. An own-restricted rival is consistent with S0, supervenience, own-only significance and Diff (P4). The step-1 inconsistency is exact only for a rival that grants the first horn of [HUIGEN §7](HUIGEN-PRACTICAL-NECESSITY-AUDIT.md#7-the-most-promising-grounding-route-and-its-exact-test). A rival that places a formed own-region relation in the ground (the second horn) is untouched. The S0 ledger also counts "what forms from this activity" as part of further generation, which contradicts the model's `ownOcc formedOther = False`. Step 1 avoids return of benefit, but it makes relation-to-self the test: an enlarged-self structure.

**C. Formal correspondence.** Lean 4.29.1 recompiles both modules. The 19/8/2 axiom profile is reproduced exactly. Gaps: `own` is a primitive field independent of `prof`, contrary to §1. `Monotone` is unrestricted. `Tolerant` and `Chain` range over merely possible profiles with a free step relation. The `reach` restriction is cosmetic. `reach_is_g0` yields a standpoint-indexed, single-history instance of the generic G0 predicate, not the adopted non-indexed G0 over continuations. **Fifteen required corrections** are listed in §6; none has been applied.

---

## 0. 范围与方法

**读了什么。** 全文阅读了论证、Lean 源码、回执，以及保留运行中的 `Controls.lean`。按需阅读了 [AGENTS.md](../../../../AGENTS.md)、[非二元方法](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md)、[G0-WARRANT](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/G0-WARRANT.md)、[HUIGEN-PRACTICAL-NECESSITY-AUDIT](HUIGEN-PRACTICAL-NECESSITY-AUDIT.md) §§1–10、[OWNERLESS-ETHICS-SOURCES](OWNERLESS-ETHICS-SOURCES.md)、[GENERATED-SELF-AND-ETHICS](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATED-SELF-AND-ETHICS.md) §4、[HUIGEN-SELF-GROUND-SOURCES](HUIGEN-SELF-GROUND-SOURCES.md) 中 Sidgwick、Korsgaard 1989 与 Parfit 的条目、[外部视角审查](UNIVERSAL-METAETHICS-OF-AGENCY-REVIEW.md) §3.1、记录 `self-good-reachable-g0` 与 `positive-ground-open-futures`。Ren 原话部分读了 [2026-10-09 一元评价者](../../../../sources/15-codex-theory-conversations/2026-10-09-monist-evaluator-grounding.md)、[自我之善在整体之内](../../../../sources/15-codex-theory-conversations/2026-10-07-self-good-within-the-whole.md)、[生生作为伦理方向](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md)、[正面生成方向](../../../../sources/15-codex-theory-conversations/2026-10-08-positive-generative-direction.md)、[一元本体优先](../../../../sources/15-codex-theory-conversations/2026-10-08-monist-relational-ontology-first.md)和[善不必回到自身](../../../../sources/15-codex-theory-conversations/2026-10-06-goodness-without-return-to-self.md)。

**文献依据。** 本次审查**没有新读任何外部文献**。Sidgwick、Korsgaard 1989、Harris 2011 与寂天的引用依据仓库已有的来源研读记录。Parfit《Reasons and Persons》(1984)、Williamson《Vagueness》(1994)、Fine 1975 的超赋值论、Temkin《Rethinking the Good》(2012)、Maturana 与 Varela 的自创生论、Thompson《Mind in Life》(2007)、Scheffler 关于偏倚性的著作、Nagel《The Possibility of Altruism》(1970) 与 Johnston 1997，均依据审查者的**先前知识**，文中只作转述，不作引文。

**分类纪律。** 依非二元方法，每项发现都标明属于以下哪一类：
- **(甲)** 形式表示省略了某一关系；
- **(乙)** 重构的论证中有尚未解决的推论；
- **(丙)** 满足所述条件的真实反例。

有限模型中自由开关的谓词本身不推翻更完整的论述。凡作者已在 §6、§8 承认的问题，只有在显示其比所承认的更严重时，才算新的发现。

## 1. 总评

| 问题 | 结论 | 理由要点 |
|---|---|---|
| A. 容差（§4） | **拒绝**（作为对门槛对手的辩护）；第二步作为条件定理**接受** | 三难不穷尽；核心一步无效（P5、P7）；形式容差或空洞（P1），或等价于常值（P2）；同一前提也可向下传递（P3）；“封闭自我”即门槛对手（P1） |
| B. 分化（§3） | Diff 本身**接受但收窄范围**；“第一步不加额外理性前提”与“对手严格不一致”两种表述**拒绝** | 作者自己的二维图示中，Diff 在积序下对任何立场都不成立（P6）；`Monotone` 跨越自他，比对手自己的原则更强（P4）；S0 的措辞与模型冲突 |
| C. 形式对应与复核 | 推论与复核**接受**；对应**须更正** | 重新编译通过，哈希与公理依赖一致；`own` 独立于 `prof`；`Chain` 取在可能剖面上；`reach` 限制只是装饰；`reach_is_g0` 是带索引的单历史实例 |

---

## 2. 问题 A：容差

**结论：拒绝 §4 的辩护。** `tolerant_chain_reaches` 与 `self_good_derives_reachable_g0` 作为条件定理有效。但 §4 没有确立容差，形势也比 §6.2、§8.2 所承认的更不利。

### 2.1 三难不穷尽（乙，并有丙类模型）

§4 认为，对自身未来之意义的根据只有三种：(a) 当下在乎，(b) 分级关系上的门槛，(c) 按关系加权的生命内容。至少还有四种根据被遗漏。

**(d) 已形成的质性关系。** 例如自创生意义上的运作闭合，即一个过程网络持续生产自身边界（Maturana 与 Varela；Thompson，先前知识）；又如 Korsgaard 1989 所说的行动统一性。按[仓库记录](HUIGEN-SELF-GROUND-SOURCES.md)，Korsgaard 以审议、协调行动和持续的事业为时间统一的根据，并指出形而上分离性的减弱不会使一切生命同样相连。这些关系有三个特点：
- 是形成的，不是原始的所有者标签；
- 在一元本体中完全可以接受；
- 在实际情形中大多是清晰的，只在分裂、复制、联体、妊娠、AI 分叉等边缘情形中模糊。

它们不是“在一个分级量上设门槛”，而是结构性的、拓扑性的特征。论证 §1 自己说“自身的”是已形成关系中的一个区域；这样的区域边界正是一种已形成关系。

**(c′) 连续递减并在有限距离处归零的权重。** (c) 只说“权重可以随关系递减”，并不蕴涵“永不为零”。权重连续变化（每一小步变化有界）与在有限关系程度处归零是相容的（P7）。§4 从 (c) 滑到“凡相连处都有正面意义”。中间缺少的前提是：任何非零的已形成关系都带有严格为正的权重。下文记作 **P+**。

**(e) 带边缘情形的模糊边界（超赋值论，Fine，先前知识）。** 对我的意义可以经过一段边缘区逐渐淡出：没有任何一步确定地把“正”翻成“无”，而远处的陌生人在一切可接受的精确化下都确定地没有意义。在超赋值论中，全称的容差原则为超假。

**(f) 认知主义（Williamson，先前知识）。** 存在一个清晰但不可知的分界点。这正好否认 (b) 的核心断言：“难以分辨的一小步承担不了全部差别”。按认知主义，它能承担，只是我们无法知道在哪一步。

由此可见，(b) 中“关系是分级的；难以分辨的一小步，承担不了全部差别”并不是关于一元本体的中立观察，而正是有争议的容差原则本身。两种主要的模糊理论都拒绝全称容差。程度理论接受分级真值，对应的是 (c′)，而不是 G0 所需的正面性。

**论证自身的另一道边界（乙）。** `Supervenes` 只对 `living` 发生成立，§6.3 也把内容限于“与 S0 同类的生命内容”。可见论证自己保留了一道不受容差约束的内容边界。在一元本体中，生与非生、“同类生命”与其他组织同样是分级的；病毒、朊病毒与 Ren 的第三种“生”的范围都说明这一点。若对手在自他之间的断点算“所有者以门槛形式回来”，那么按同样的理由，论证在生命种类上的断点也须说明为什么不算“种类标签以门槛形式回来”。“内容”与“关系剖面”的分开本身需要一元本体下的说明。

### 2.2 核心一步：“对手已在自身转化路径上接受容差”（丙，针对该推论）

这一步只有在一个条件下有效：对手的断点与它接受容差的路径位于**同一个**分级维度上。在对手自身的逐渐变化中，闭合或行动统一性这一坐标始终不变，所以它在自身路径上接受容差，与在另一维度上设断点完全一致。

- **P5（`closure_rival_escapes_both_steps`）。** 剖面为（闭合，程度）。对手同时满足 S0、**不受限的**单调性、随附性，以及沿分级坐标每一小步的容差。它的 Diff 不成立，由此活动形成的他者与陌生人都得不到意义。它满足论证所述的 M1：闭合是已形成关系，不是原始标签。这是对 §4 推论“自身路径上的容差 ⇒ 通往他者路径上的断点是伪装的所有者”的真实反例。它**不是**对第二步条件定理的反例，因为它不满足 Chain。
- **P7（`graded_weight_rival`）。** 权重为 `d − 1`：每一相邻步最多变化一个单位，单调，在一切自身发生上为正；断点位于剖面 1 与 2 之间，**低于每一个自身剖面**。因此，“断点的位置由‘哪些是我的’决定”对一般门槛对手不成立。Lean 中的门槛对手 `4 ≤ ·` 恰好把断点放在 `changedSelf` 的程度上，选中的正是那个看起来像所有权的门槛。

**在一元本体下，这些特征本身是否分级？论证是否因此走通？**
- 心理连接、共同事业、因果依存、形成性贡献，以及作为程度的互惠，都是分级的。对这些特征，“伪装的所有者”这一指控只在断点恰好落在自他边界时才有力量。否则对手就是 (c′)：它须说明为何在有限距离处归零。这是一个普通的规范争议，不是不一致。
- 同一机体、运作闭合、单一的整合控制过程、某种关系是否存在，在实际展开中大多是清晰的，只有少量边缘情形。一元本体意味着这些边界是形成的，不意味着实际分布中没有缺口。非二元方法自己写明：分化是真实的，须加以解释，不能抹去。
- 因此，第二步要成立，还需要两项论证没有给出的前提。其一是 **BI（边界无关）**：支撑自我之善的关系剖面中，不含自身区域的质性坐标。其二是 P+，或在连通分级空间上的二值容差。M1 只排除**原始**所有者，推不出 BI。

### 2.3 形式上的 Tol 与 Chain 是否忠实于散文（甲、丙）

- **P1（`tolerance_vacuous_for_restricted_step`）。** 对任何 `val`，只要把步关系限制在 `val` 的正区域内，`Tolerant` 就成立。`closed_step_is_threshold_restriction` 证明 `closedStep` 正是门槛估值的这种限制。可见形式前提的全部力量都来自 `step` 的选择，而散文中的“难以分辨的小步”在 Lean 中没有被编码。这是承重的省略（甲）。[HUIGEN §3](HUIGEN-PRACTICAL-NECESSITY-AUDIT.md#3-two-transports-not-just-one) 已经警告过，不断添加边直到到达所需的承受者，等于把结论编码进去；在这里，步关系就是那条边。
- **P2（`tolerant_adjacent_constant`、`tolerance_reaches_unreachable_and_unrelated`）。** 在模型选用的 `Nat` 加相邻步上，`Tolerant val adjacent` 加上一个正点，就迫使 `val` 处处为真。于是不可及的 `beyond` 也有意义，剖面 0（没有任何已形成关系）也有意义。`tolerant_standpoint_reaches_stranger` 的说明“the unreachable one is not claimed”就定理陈述而言为真，但它的前提蕴涵了这一点。`reach` 只限制了结论的量词，前提给出的远多于此。更重要的是：剖面 0 也有意义，说明在容差加连通空间之下，关系程度对正面性不起任何作用。这与“意义只取决于已形成关系”的论证精神相冲突（丙，针对“意义以关系为根据、只及可及者”的说法）。
- **强弱。** 若 `step` 自由，形式 Tol 比散文**弱**（可以空洞）；若取连通空间上的相邻步，它比散文**强**（等价于常值）。散文的 Chain 读起来是“每一处可及的**生命**都由有限个关系小步相接”，像是关于实际发生的主张。Lean 的 `Chain` 却在 `Prof` 上，中间剖面没有任何发生占据（P8，`chain_passes_unoccupied_profiles`）。这样，容差就成了对评价者如何估值**仅仅可能**的关系剖面的主张。对手可以否认自己的估值在没有实际发生的剖面上有定义，或否认在那里为正。
- **多维剖面。** 沿一个维度的容差，不会在另一维度上给出连通（P5）。在积序下，每一个维度都须由小步连通；只要有一个维度是质性的，就没有小步链能跨过它。
- **P3（`tolerance_levels_down`）。** 同样的前提加上“陌生人没有意义”，可以推出 ¬S0。容差是一条对等原则，与寂天 VIII.103 的“全有或全无”和 Harris 指出的“平等的冷漠”同构（据仓库的[来源记录](OWNERLESS-ETHICS-SOURCES.md)）。评价者往哪个方向走，取决于它对 S0 与对“陌生人无意义”各有多大把握。§6.1 把现时目的评价者写成从未持有 S0 的局外者，但 P3 表明，它也可以是从同一组前提出发的**反思性出口**。论证依赖 S0 比否认陌生人的意义更可信，这一比较须明说。

**由此得到的总体判断。** `tolerant_chain_reaches` 的内容可以分解为两部分：S0 在一个点上为真；正面性在连通分量上为常值。所推出的 G0ₛ 中超出 S0 的全部内容，都由 Tol 加 Chain 承担，而这部分正是“正面性不随关系程度改变”这一不偏倚的核心。所以 §5 末句“比 G0 弱得多的起点”不成立。这一分解有价值，因为它把争议定位到 Tol 上；但它不是把 G0 降为更弱的起点。§8.2 说“容差不提及他者”，形式上为真，却有误导性。

### 2.4 文献对照：论证是否公平地说明了容差买到什么

- **正面性，不是权重。** 这一界定公平而正确：G0 只需要基本的正面意义。
- **Sidgwick。** 据仓库记录（[HUIGEN-SELF-GROUND-SOURCES](HUIGEN-SELF-GROUND-SOURCES.md)，第七版 pp. 420–421），自我相对的利己者可以避开“普遍之善”的论证，二元论仍然没有解决。第二步是这一论证的连锁悖论形式；P4、P5 正是自我相对利己者的避开方式。据先前知识，Sidgwick 在结论章自己提出过：若自我只是一串现象，为何更关心自己的未来而非他人？可见本路线属于这一谱系。它的增量在于生成式 S0 与形式化，而不在于对二元论的新解决。§6.2 引 Sidgwick 作“僵局的经典形态”是恰当的。
- **Parfit（先前知识，本次未读原著）。**
  1. “不完全相对”论证：自利论同时受到现时目的论与中立道德两面的压力。这正是 P3 的双向性；§6.1 只写了一面。
  2. R 关系有程度，Parfit 允许对遥远未来的自己少关心一些。但他没有从 R 推出对陌生人的关心，因为陌生人之间缺乏 R。
  3. Parfit 把连续性定义为强连接的重叠链，其中的步关系本身带有门槛。这在结构上正是 `closed_self_blocks_reach` 的模型。所以封闭自我代表的是一种还原论的、关系式的、与一元本体相容的观点，而不是 §8.6 所说的“二元的替代图景”。
  4. 对 Parfit 的回应中，Johnston 1997 认为特殊的关心在还原论下仍可成立，Korsgaard 1989 以行动统一性作根据，两者都属于 (d) 型根据。
- **Scheffler 式偏倚性（先前知识）。** 偏倚性与陌生人具有基本正面意义相容，§4 这样说是公平的。但 Scheffler 式的理由来自对关系的珍视，“处在某种关系中”是一种质性根据，更接近 (d)，而不是分级连接。偏倚论者不必接受跨关系种类的单调性，也不必接受 Tol。论证暗中假定偏倚论者会接受容差，这一点没有根据。
- **谱系论证（Temkin，先前知识）。** 由许多小步构成的链，通常迫使人在容差类前提与传递性等原则之间取舍。本论证把压力全部放在二值容差上，而二值容差正是在谱系论证中最常被放弃的前提。

### 2.5 最强反驳与会改变判断的结果

**最强反驳。** 按论证自己的 §1，“自身”是已形成关系中的一个区域。于是对手可以让自我之善部分地以一种已形成的质性自身区域关系（闭合、行动统一性）为根据。这样它同时满足 S0、所述的 M1、对它自己的根据关系不受限的单调性、随附性，以及沿每一个分级小步的容差，却否认结论（P5）。这不是“伪装的所有者”，而正是 §1 用来定义“自身”的那种关系。

**会改变判断的结果：**
1. 一个论证表明，对持有 S0 的评价者，自身区域坐标不在其自我之善的根据关系之中。例如借分裂、分叉、融合的案例分析，表明在一切分级关系保持不变而只有闭合改变时，S0 持有者经过反思的估值不变。这是为生成式 S0 构造的 Parfit 式“什么才重要”论证。
2. 把二值容差换成明确的分级前提 P+（“任何非零的已形成关系，对同类生命内容都带有非零的正面权重”），并直接为 P+ 辩护。
3. 一个专门针对规范意义谓词的模糊性论证，说明为什么容差在这里成立，而在普通模糊谓词上不成立。

以上任何一项，都会把 A 的结论改为“接受但收窄范围”。

---

## 3. 问题 B：分化

**结论：Diff 接受但收窄范围。** “第一步不加任何额外理性前提”与“只承认‘我的’的对手严格不一致”两种表述**拒绝**。

### 3.1 Diff 对谁成立：逐项检查支撑自我之善的关系（乙）

| 关系 | 深度转化后的远期自己 | 由此活动形成的他者 | 谁在此维度上满足 Diff |
|---|---|---|---|
| 组织／代谢连续性 | 高（§1 自己也承认） | 孩子、学生约为 0；分裂产物、复制体、AI 分叉为高 | 只有分裂、复制、分叉 |
| 记忆型心理连接 | 中 | 约为 0，复制体或上传除外 | 只有复制体 |
| 价值、品格、事业的连续性 | 可能很低（皈依、失智、放弃事业） | 合作者、继承者可能很高 | 个别情形可能成立 |
| 形成性贡献 | **通常高**：学习是自己的活动，现在的选择塑造未来的自己 | 幼儿、唯一导师下的学生、蒸馏出的后继者可能很高 | 父母对幼儿、AI 蒸馏等情形 |
| 依存 | 高（依存于现在的自我维持） | 被抚养者、病人可能很高 | 照护关系 |
| 遗传或权重继承 | 不适用 | 孩子约 50%；AI 后继者不定 | 依具体情形 |

若根据关系有多项，“在支撑自我之善的关系上至少同样相连”（Mono 的原文用复数）最忠实的读法是积序。在积序下，Diff 实际上只在分裂、复制、分叉的情形中成立；在形成性贡献占主导的评价方式下，它对部分父母、教师和 AI 蒸馏者成立。对根据中包含组织连续性的典型人类评价者，Diff 在典型情形中不成立。

**“珍视继续生成就是珍视转化，而转化降低了与现在自己的连续性”：部分成立。**
- 转化确实降低内容上的相似性，但 §1 自己承认组织连续性仍然很高。
- 珍视转化并不要求珍视那些在一切关系上都落到某个他者之下的转化。学习往往**提高**现在活动对未来自己的形成性贡献。
- 从“生成一般经由分化出他者而实现”（繁殖、分裂、教学），到“**这一**评价者所珍视的自身继续生成中，有一个被实际他者在其根据关系上全面赶上的发生”，是从类型层面的生物学滑到了评价者层面的估值内容（乙）。

### 3.2 二维图示（丙，在作者自己的模型内）

- **P6（`diff_fails_in_profile2_product_order`）。** 在 `profile2` 中，`changedSelf = (8,2)`，`formedOther = (1,7)`。在积序下，任何他者都不至少同样相连于任何自身发生。所以在作者自己的二维模型里，第一步对**每一个**使用积序的立场都不起作用，而不只对持续论者。
- **`balanced_generative_escapes`。** 一个把连续性与形成性贡献相加的“平衡的生成式”评价者，满足 S0 与积序单调性，却到达不了由此活动形成的他者。
- **`weighted_diff_iff`。** 在加权和序下，`formedOther` 至少同样相连，当且仅当 `7a ≤ 5b`，即形成性贡献的权重至少是组织连续性的 1.4 倍。

因此，§3 增量第 3 点与 §8.1 所说的“只有以组织持续为根据的对手逃过第一步；第一步约束生成式自我之善”说得过头了。正确的范围是：第一步约束的是**以形成性贡献为主导**、接受不受限单调性的生成式自我之善。

一维图示 `degree` 取 `changedSelf = 4 < formedOther = 5`，把维度融合了，去掉的恰恰是构成“自身”的那个关系。`ownOcc` 在 `degree` 上不是向上封闭的（4 属于自身，5 不属于），这证实了让 `changedSelf` 成为“自身”的关系不在剖面之中。这不是证明错误，而是说明图示把 Diff 预先建了进去，因此不能作为 Diff 的支持。§3 增量第 2 点说“他者的‘至少同样相连’来自实际的共同形成，不是假设”，须撤回：Diff 是对应前提，在作者自己的二维数字中不成立。

### 3.3 S0 内容的歧义（甲或乙，须二选一）

账本中的 S0 与 Lean 说明都写道：“继续生成”包括“由这一活动形成的东西”。§1 又把学生、孩子、后继者和共同工作列为“由这一活动形成的”。

- **若包括**：由此活动形成的他者按 S0 的内容就已经是“自身的继续生成”，第一步对它们靠的是定义，而不是单调性。这正是 AGENTS.md 所说的以定义承载结论。同时，模型中的 `ownOcc formedOther = False` 与 S0 相矛盾。
- **若不包括**：S0 的措辞须修改，Diff 便成为实质主张，范围如 3.1。

两种情况都需要更正。

### 3.4 单调性的归属与“严格不一致”（丙，针对“对手自己的原则”）

利己者用来让近未来重于远未来的单调性，只在**自身**发生之间成立。Lean 的 `Monotone` 却对一切生命发生成立，包括他者。

- **P4（`own_restricted_rival_consistent`）。** 只在自身发生之间单调的对手，与 S0、随附性、只给自身以意义、Diff 同时一致。它付出的代价是：剖面上的 `val` 不单调（4 有意义，5 没有）。
- **`supervenient_monotone_val_gives_monotone`。** 不受限的 `Monotone` 可由“随附性，加上剖面上单调的估值”推出。所以第一步真正需要的前提是：随附性、剖面单调的估值，以及剖面中不含自身区域坐标（BI）。第三项不满足时，P5 的对手在**不受限**单调性下仍一致。
- Lean 的第一步定理没有用到 `Supervenes`。§3 说“G2 被排除了，因为‘属于我’的唯一可用根据已被它自己的单调性带到他者那里”，这一点是由假定不受限的 `Monotone` 承担的，而不是推出来的。

**与 HUIGEN §7、§10 的标准对照。** 若对手承认连接程度（不含自身区域）就是完整根据，同时又只给自身以意义，那么它确实严格不一致。这是 [§7](HUIGEN-PRACTICAL-NECESSITY-AUDIT.md#7-the-most-promising-grounding-route-and-its-exact-test) 的第一角，结果真实而精确，但范围窄。若对手把已形成的自身关系纳入根据，即 §7 的第二角，按 §7 原文，“争议转移到这一所提出的根据；转移并未由第一个让步证明”。所以，“满足 §10 标准”的说法言过其实：它只对第一角满足。

**对手拒绝生成式读法之后，剩下的还是 S0 吗？** 是。“自身的生与继续对我有提供理由的意义”这一普通 S0 仍然成立，大多数活着的评价者持有的正是它。§6.1 和 §8.4 所说的“几乎所有评价者都持有 S0”对普通 S0 成立，第一步却只约束一种更窄的 S0：形成性贡献主导、接受不受限单调性与 BI。两处说法的对象须对齐。

### 3.5 是否经由“回到自身”（乙）

- **没有经由利益回报。** §3 说“模型中没有反馈路径”，但模型里根本没有表示任何动力学，这一条件是平凡满足的（甲），不构成证据。
- **但第一步以“与我的关系”为检验。** 他者有意义，以它至少与我珍视的未来自己同样连接于我为限。范例关系（形成性贡献）使他者作为“我的形成”而有意义。这正是[非二元方法](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md)提醒不应作为奠基检验的“扩大的自我”结构；它也与 Ren“善不必回到个体”的纠正有张力，虽然不是直接违背。第二步只有让正面性与关系无关（P2），才摆脱这一检验；到那时，“自身”只是一个种子点。
- **对 §7 对齐含义的影响。** 对一个 AI 来说，第一步最先扩展到它自己的复制体与后继者，因为它们最相连。这会偏向自身谱系，与仓库中关于“赢的元吸引子”的担忧直接相关；第一步本身到不了人类。只有正面性而没有权重，与对自身谱系的强烈偏倚相容。§7 须对此加以限定。

### 3.6 最强反驳与会改变判断的结果

**最强反驳。** 在作者自己的二维剖面中，积序下 Diff 对每一个立场都不成立（P6）。第一步所约束的评价者，须把形成性贡献的权重至少定为组织连续性的 1.4 倍，并接受不受限的单调性。到这一步，它已经在珍视自己的形成物；所谓“不一致”，大体只是揭示了它已有的承诺。

**会改变判断的结果：**
1. 对特定评价者类别取得具体证据。例如一个 AI 系统，其权重、价值与能力与某一后继者的连续性经过测量，并在该系统自己的根据序中超过它所珍视的某一自身未来状态。
2. 一个论证表明，组织连续性不在生成式 S0 的根据关系之中。

---

## 4. 问题 C：形式对应与复核

**结论：推论与复核接受；对应须更正。**

### 4.1 定义对照

| Lean | 散文的说法 | 评估 |
|---|---|---|
| `Standpoint.own : Gen → Prop`，独立字段 | §1：“自身的”是已形成关系中的一个区域 | 承重的省略（甲）。`own` 不是 `prof` 的区域，所以 `formedOther` 可以程度更高而不属于自身；`Monotone` 也可以忽略自身边界 |
| `SelfGood` | S0 | 作为 Prop 读法是忠实的；“提供理由”属于解释，§8.5 已承认 |
| `Monotone`，量化一切生命发生 | “对手自己的原则” | 比对手的原则更强（P4）；跨越自他的那一步被藏在这里 |
| `Supervenes` | M1：一元本体，无原始所有者 | 是规范的随附性论题，不由本体论蕴涵；容许 `Prof` 含闭合坐标（P5）；第一步没有用到它 |
| `Tolerant val step`，`step` 自由 | “难以分辨的小步” | 未编码“难以分辨”；可以空洞（P1），也可以等价于常值（P2） |
| `Chain step`，在 `Prof` 上 | “每一处可及的**生命**都由有限个小步相接” | 落在仅仅可能的剖面上（P8），而不是实际发生上 |
| `reachableInventory : Inventory Unit Gen` | “可及库存” | 只有单一历史。[positive-ground-open-futures](../../../../theories/shengsheng-buxi-generative-existence/results/records/positive-ground-open-futures.json) 依赖多个真实的未来分支；记录中的接口在类型上可用（`H := Unit`），但开放未来的结构消失了 |
| `reach_is_g0`，证明只是交换参数顺序 | “恰好是 G0” | 对泛型谓词 `G0` 而言为真，`PositiveRelevant := sigₛ`。所采用的 G0 是不带索引、跨接续的基本规范意义；“地位改变”须加索引，并须有从立场相对意义到规范意义的桥接 |

### 4.2 反模型各显示了什么

- **`present_aim_evaluator_escapes`**：显示没有 S0 就推不出结论。说法正确。说它是“真实可能的形成”是散文的哲学主张，Lean 不承担这一点。P3 补充：它也是从同一组前提出发的反思性出口。
- **`threshold_rival_is_consistent_without_tolerance`**：显示 Tol 承担了工作。说法正确。但所选断点恰好落在自身边界上；一般情形见 P7。
- **`closed_self_blocks_reach`**：与门槛对手使用**同一个** `val`，只是把步关系限制在 `val` 的正区域内（P1）。它显示，对**那一个**步关系而言 Chain 承担了工作。它没有显示 M1 承担了工作：`Supervenes` 在其中成立。所以 §4 的“M1 去掉它，Chain 才可能成立”在形式上没有对应：M1 既不蕴涵 Chain，Chain 也不以 M1 为前提。把它标为“二元的替代图景”也不对：Parfit 式连续性与自创生闭合都是一元的、关系式的形成，结构与此相同。
- **`persistence_rival_escapes_self_transcendence`**：显示了它所说的内容，但说得不够：P6 表明，在 `profile2` 加积序下，逃过第一步的是一切立场。

### 4.3 散文超出定理的地方（汇总）

1. “第一步不加任何额外理性前提”：依赖不受限的 `Monotone`，见 3.4。
2. “他者的至少同样相连来自实际的共同形成，不是假设”：这是对应前提，见 3.2。
3. “只有持续论者逃过第一步”：见 P6。
4. “断点的位置由哪些是我的决定”：见 P7。
5. “不可及者不被主张”：前提已经蕴涵它，见 P2。
6. “一元本体在做实际工作／M1 使 Chain 可能”：见 4.2。
7. “G0 从采用的公理变为推论”：所得是带索引的单历史实例，而且超出 S0 的全部内容由 Tol 承担，见 2.3、4.1。
8. 对 §5 表第二行“理由对它的约束不依赖 D”的说明：这条路线用对 S0、Tol 与 BI 的认同代替了 D，并没有获得 [positioned-positive-reason](../../../../theories/shengsheng-buxi-generative-existence/results/records/positioned-positive-reason.md) 意义上的“与认同无关”。“它无论是否认同 G0，都已承诺 G0”须改为“只要它认同 S0、容差（及 BI）”。

### 4.4 独立重新编译

在仓库外的会话临时目录中，复制 `GenerativeComparison.lean` 与 `EvaluatorGrounding.lean`，执行：

```text
LEAN_PATH=<tmp> ~/.elan/bin/lean +leanprover/lean4:v4.29.1 -o GenerativeComparison.olean GenerativeComparison.lean   # exit 0
LEAN_PATH=<tmp> ~/.elan/bin/lean +leanprover/lean4:v4.29.1 -o EvaluatorGrounding.olean EvaluatorGrounding.lean       # exit 0
LEAN_PATH=<tmp> ~/.elan/bin/lean +leanprover/lean4:v4.29.1 Audit.lean    # 12 theorems, #print axioms
LEAN_PATH=<tmp> ~/.elan/bin/lean +leanprover/lean4:v4.29.1 Audit2.lean   # remaining 17 declarations
```

Lean 版本：`4.29.1, arm64-apple-darwin24.6.0, commit f72c35b3f637c8c6571d353742168ab66cc22c00`，与回执一致。

**哈希。**

| 文件 | 复制件的 sha256 | 回执 `source_sha256` | 一致 |
|---|---|---|---|
| `GenerativeComparison.lean` | `948d36b4cddc0b2289219604464bd38eb6e607183b157cee1075d50fb9797a03` | 同 | 是 |
| `EvaluatorGrounding.lean` | `86c1583d35505b466db5670f15f19b53cba2be3deb4e3d56b53bed79bcc9218c` | 同 | 是 |

记录中的论证文档哈希（`c5e8fd65…`）、回执哈希（`95b1df5b…`）与来源文件哈希（`11c5230c…`）均与当前文件一致。

**公理依赖**（12 个定理，复核结果与回执逐项一致）：

| 定理 | 公理 |
|---|---|
| `self_good_reaches_at_least_as_connected` | 无 |
| `strict_indexed_rival_inconsistent` | 无 |
| `chain_preserves` | 无 |
| `tolerant_chain_reaches` | 无 |
| `reach_is_g0` | 无 |
| `self_good_derives_reachable_g0` | 无 |
| `formed_other_has_significance` | propext |
| `threshold_rival_is_consistent_without_tolerance` | propext, Quot.sound |
| `tolerant_standpoint_reaches_stranger` | propext |
| `present_aim_evaluator_escapes` | propext |
| `closed_self_blocks_reach` | propext, Quot.sound |
| `persistence_rival_escapes_self_transcendence` | propext |

其余 17 项声明中，`ownOcc`、`reachOcc`、`standpoint`、`persistence` 依赖 propext，其余都没有公理依赖。29 项合计 19 项无依赖、8 项 propext、2 项 propext 与 Quot.sound，与回执完全一致。

---

## 5. 探针

探针文件 `ReviewProbes.lean`（sha256 `9ccfa5d1b6b0c9150428b379a75f15c43ac74800b8e94e319537c4377a745e80`）导入未改动的 `EvaluatorGrounding`，在 Lean 4.29.1 下编译通过（exit 0），无 `sorry`。全文见附录。

| 探针 | 定理 | 显示什么 | 公理 | 类别 |
|---|---|---|---|---|
| P1 | `tolerance_vacuous_for_restricted_step`、`closed_step_is_threshold_restriction` | 步关系限于正区域时，容差恒成立；`closedStep` 正是门槛估值的这种限制 | 无 | 甲（承重省略） |
| P2 | `tolerant_adjacent_down/up/constant`、`tolerance_reaches_unreachable_and_unrelated` | 相邻步上的容差加一个正点 ⇒ 估值处处为真；`beyond` 与剖面 0 也有意义 | propext, Quot.sound | 丙（针对“只及可及者”“以关系为根据”的说法） |
| P3 | `tolerance_levels_down` | 容差加“陌生人无意义” ⇒ ¬S0 | propext, Quot.sound | 乙（双向压力） |
| P4 | `own_restricted_rival_consistent`、`supervenient_monotone_val_gives_monotone` | 只在自身之间单调的对手与 S0、随附性、只给自身意义、Diff 同时一致；不受限单调性 = 随附性加剖面单调估值 | propext；无 | 丙（针对“单调性是对手自己的原则”） |
| P5 | `closure_rival_escapes_both_steps`（及 `closure_iff_own`） | 剖面含已形成的闭合坐标时，S0、不受限单调性、随附性、分级容差都成立，而 Diff 与 Chain 都不成立 | propext | 丙（针对 §4 核心推论与“M1 承担工作”） |
| P6 | `diff_fails_in_profile2_product_order`、`balanced_generative_escapes`、`weighted_diff_iff` | 作者二维模型中，积序下 Diff 对一切立场都不成立；平衡的生成式评价者也逃过第一步；加权序须 7a ≤ 5b | propext；propext, Quot.sound；propext, Classical.choice, Quot.sound | 丙（在作者模型内） |
| P7 | `graded_weight_rival` | 每步变化有界、单调的权重，断点低于每一个自身剖面 | propext, Classical.choice, Quot.sound | 丙（针对“断点由‘我的’决定”） |
| P8 | `chain_passes_unoccupied_profiles` | 从自身到陌生人的链经过没有任何发生占据的剖面 | 无 | 甲 |

`Classical.choice` 只出现在两个探针中，来自 `omega` 策略，与原论证的定理无关。

**探针本身的限度。** 这些都是有限模型。P5 与 P7 显示的是：在**论证所述的条件下**，有一致的对手否认论证对 Tol、Chain 与 Diff 的辩护。它们不推翻第二步的条件定理，那个定理把 Tol 与 Chain 都当作前提。P5 的对手在现实中是否有分量，取决于闭合是否真的属于 S0 持有者的根据关系，这是对应问题。所以须作更正的是论证的辩护与范围，而不是推论本身。

---

## 6. 须作的更正（未执行）

**执行状态（2026-10-09 补记）。** 15 项更正已由整合会话依 Ren“你自己全改了吧”执行，逐项对照见[论证修订说明](EVALUATOR-GROUNDING-ARGUMENT.md)。审查所建议的 P+ 版第二步由 [metaethical-core-characterization](../../../../theories/shengsheng-buxi-generative-existence/results/records/metaethical-core-characterization.md) 给出。以下审查原文不变。

以下更正针对论证文档、Lean 说明、记录，以及已引用本结果的 G0-WARRANT。审查者只列出，不执行。

1. **摘要、§0、§3、§5 表与记录 `claim`：** 删去“不加任何额外理性前提”。写明第一步还需要不受限（跨越自他）的单调性，等价地说，需要随附性、剖面上单调的估值，以及 BI（自我之善的根据剖面不含自身区域坐标）。把 BI 列入 §2 账本，标为有争议。
2. **§2 账本、Lean 文件头与 `SelfGood` 说明、记录 `hypotheses`：** 消除 S0 中“由这一活动形成的东西”的歧义。若包括他者，就说明第一步对它们靠的是 S0 的内容，并修改 `ownOcc formedOther`；若不包括，就改写 S0。
3. **§3 增量第 2 点：** 撤回“来自实际的共同形成，不是假设”。Diff 是对应前提，并须写明范围：分裂、复制、分叉与 AI 后继者，以及形成性贡献主导的评价方式。
4. **§3 增量第 3 点、§8.1、记录第四个反例：** 改为“在 `profile2` 加积序下，逃过第一步的是一切立场；平衡的生成式评价者亦然；加权序须 7a ≤ 5b”。“第一步约束生成式自我之善”改为“约束以形成性贡献为主导、接受不受限单调性的生成式自我之善”。
5. **§4 三难：** 补上 (d) 已形成的质性关系、(c′) 归零的分级权重、(e) 超赋值论的模糊边界、(f) 认知主义的清晰断点。撤回或收窄“对手已在自身路径上接受容差，所以断点是伪装的所有者”：自身路径不跨越闭合坐标，断点也不必落在自身边界上（P5、P7）。
6. **§4、§6.2、§8.2：** 写明二值全称容差在连通剖面空间上等价于正面意义为常值，即连锁悖论的大前提；它对剖面 0 与不可及者同样给出意义（P2）；它也可以向下传递（P3）。把现时目的的出口同时写为反思性出口，并明说论证依赖 S0 比否认陌生人的意义更可信。
7. **§4“一元本体在做实际工作”、§8.6、记录第三个反例：** `closed_self_blocks_reach` 就是把步关系限于正区域的门槛对手。它显示的是 Chain 对那一个步关系承担工作，不是 M1 承担工作。删去“二元的替代图景”的标签，并注明 Parfit 式连续性与自创生闭合是同构的一元形成。
8. **`tolerant_standpoint_reaches_stranger` 的说明“the unreachable one is not claimed”：** 补注同样的前提蕴涵 `sig .beyond`。或者改写 `Chain`、`step`，使 `reach` 的限制成为推出的结果。
9. **§1 摘要、§5 表、记录 `claim`、G0-WARRANT §2.3“2026-10-09 部分完成”段与 §4 第 4 项：** “G0 从采用的公理变为推论”改为：“立场索引的单历史实例 G0(reachₛ, sigₛ) 由 S0、容差、BI 与对应条件推出，其中超出 S0 的全部内容由容差承担；所采用的不带索引、跨接续的 G0，仍需从立场相对意义到规范意义的桥接。”同时删去或限定“比 G0 弱得多的起点”。
10. **记录 `hypotheses`：** “S0 是唯一的实质规范输入”改为：S0 与容差都是实质规范前提；不受限单调性与随附性是规范的结构前提，并非由“无原始所有者”蕴涵。
11. **记录 `dependencies` 接口：** 注明 `reachableInventory` 只有单一历史（`Unit`），所以供给 `contingent_generation_has_positive_ground` 时，开放未来的多分支结构没有被表示。
12. **§5 表第二行：** “无论是否认同 G0，都已因自己的自我之善承诺了 G0”改为“只要它认同 S0、容差（及 BI）”。写明这里没有得到与认同无关的约束力。
13. **§2 中的 Chain 与 Lean 的 `Chain`：** 说明 Chain 取在可能剖面上还是实际发生上。若取在剖面上，须写明容差是对仅仅可能的剖面如何估值的主张（P8）；若取在实际发生上，Lean 须改为 `Gen` 上的关系。
14. **§3“不经回报自身”：** 保留“无利益回报”的判断，但说明“无反馈路径”是因为模型没有表示动力学；并写明第一步以“与我的关系”为检验，属于扩大自我的结构，第二步只有靠容差才摆脱它。
15. **§7 对齐含义与记录 `related.alignment-direction-g0-j`：** 写明对 AI 而言，第一步最先扩展到它自己的复制体与后继者，偏向自身谱系，本身不及人类；正面性不带权重，与对自身谱系的强烈偏倚相容。

另建议在形式上作三项修订，供作者选择：
- 把 `own` 定义为 `prof` 上的区域；
- 把 `Monotone` 拆成对手自己的 `OwnMonotone` 与一个明确的 BI 前提；
- 把 P5 的闭合对手与 P7 的分级权重对手列为新的反模型，并给出 P+ 版本的第二步。

记录的 `next_delta` 应把“独立审查”改为指向本文，并把上面三项列入下一步。

---

## 7. 仍然成立的部分

- **推论正确，公理依赖最小。** 一般定理都没有公理依赖，复核结果与回执一致。
- **第一步对 §7 第一角的结果是真实的。** 对承认“连接程度（不含自身区域）就是完整根据”的对手，“只给自身以意义”确实严格不一致。这把 HUIGEN §7 的第一角精确地形式化了。
- **生成式与持续式自我之善的对照有价值。** 珍视转化与后继的自我之善，确实比以持续为根据的自我之善更少自我封闭。对 AI 而言，自身边界可以随复制、分叉与蒸馏而变动，Diff 在这里可能有真实的适用。这值得用实际系统去检验，但须同时记下上面第 15 项的谱系风险。
- **“正面性，不是权重”的界定正确，也公平。** G0 只需要基本的正面意义。
- **把争议定位到容差上，是真实的进展。** 分解“G0ₛ = S0 + 正面性在连通分量上为常值”，把整条路线的规范负担集中到一个可以检验的原则上。这比含混地诉诸“一元”更清楚。
- **边界保留得诚实。** 作者保留了四个反模型，§6 也坦率说明 S0 不普遍、Tol 有争议。本审查的发现大多是在这些已承认的边界之外，说明问题更深一层，而不是指出作者隐瞒了什么。

## 8. 审查者自身的边界

- 本次没有新读任何外部文献；Parfit、Williamson、Fine、Temkin、Scheffler、Johnston、Maturana 与 Varela、Thompson、Nagel 都依据先前知识，论证中的细节可能需要核对原文。
- 探针是有限模型，只显示“在所述条件下一致”或“推出”，不对实际评价者作经验判断。
- 本审查没有判断 S0、BI 或 P+ 在规范上是否正确，只判断论证的推论、辩护与范围。
- 本审查没有检查 GenerativeComparison 中其他定理的哲学对应，也没有检查已引用本结果的其他文档，G0-WARRANT 除外。

---

## 附录：探针源码 `ReviewProbes.lean`

```lean
import EvaluatorGrounding

/-! Independent review probes for EvaluatorGrounding (2026-10-09). -/

namespace ReviewProbes
open EvaluatorGrounding

/-! ## P1. Tolerance is vacuous unless `step` is fixed independently of `val`.
Any valuation is tolerant for the step relation restricted to its own positive region.
`closedStep` is exactly this restriction for the threshold valuation. -/

theorem tolerance_vacuous_for_restricted_step {Prof : Type} (val : Prof → Prop)
    (step : Prof → Prof → Prop) :
    Tolerant val (fun p q => step p q ∧ val p ∧ val q) :=
  fun _ _ h _ => h.2.2

theorem closed_step_is_threshold_restriction (p q : Nat) :
    closedStep p q ↔ (adjacent p q ∧ 4 ≤ p ∧ 4 ≤ q) := by
  unfold closedStep; constructor
  · rintro ⟨a, b, c⟩; exact ⟨c, a, b⟩
  · rintro ⟨c, a, b⟩; exact ⟨a, b, c⟩

/-! ## P2. Binary tolerance on a connected profile space forces a constant valuation
(the sorites engine). In the finite model it gives significance to `beyond`,
the occurrence the argument says is not claimed, and to profile 0 (no relation). -/

theorem tolerant_adjacent_down (val : Nat → Prop) (tol : Tolerant val adjacent) :
    ∀ k n, val (n + k) → val n := by
  intro k
  induction k with
  | zero => intro n h; simpa using h
  | succ k ih =>
    intro n h
    apply ih n
    exact tol (n + (k + 1)) (n + k) (Or.inl (by omega)) h

theorem tolerant_adjacent_up (val : Nat → Prop) (tol : Tolerant val adjacent) :
    ∀ k n, val n → val (n + k) := by
  intro k
  induction k with
  | zero => intro n h; simpa using h
  | succ k ih =>
    intro n h
    have := ih n h
    exact tol (n + k) (n + (k + 1)) (Or.inr (by omega)) this

theorem tolerant_adjacent_constant (val : Nat → Prop) (tol : Tolerant val adjacent)
    {m : Nat} (hm : val m) : ∀ n, val n := by
  intro n
  rcases Nat.le_total m n with h | h
  · obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le h
    exact tolerant_adjacent_up val tol k m hm
  · obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le h
    exact tolerant_adjacent_down val tol k n hm

theorem tolerance_reaches_unreachable_and_unrelated (val : Nat → Prop)
    (self : SelfGood (standpoint val)) (tol : Tolerant val adjacent) :
    (standpoint val).sig .beyond ∧ ¬ (standpoint val).reach .beyond ∧ val 0 := by
  have four : val 4 := self .changedSelf trivial trivial
  exact ⟨tolerant_adjacent_constant val tol four 0, id,
    tolerant_adjacent_constant val tol four 0⟩

/-! ## P3. Tolerance transmits "none" as readily as "positive" (all-or-none parity).
An evaluator more confident that the stranger has no significance than of S0 can
run the same premises by modus tollens and land on the present-aim position. -/

theorem tolerance_levels_down (val : Nat → Prop) (tol : Tolerant val adjacent)
    (noStranger : ¬ (standpoint val).sig .stranger) :
    ¬ SelfGood (standpoint val) := by
  intro self
  exact noStranger (tolerant_adjacent_constant val tol (self .changedSelf trivial trivial) 1)

/-! ## P4. The Lean `Monotone` is unrestricted across own and other. A rival whose
monotonicity ranges over its own occurrences only (the rival's actual near/far use)
is consistent with S0, supervenience, own-only significance and Diff. -/

def OwnMonotone {Gen Prof : Type} (s : Standpoint Gen Prof) (atLeast : Prof → Prof → Prop) : Prop :=
  ∀ g g', s.own g → s.own g' → s.living g → s.living g' →
    atLeast (s.prof g) (s.prof g') → s.sig g → s.sig g'

def ownProfiles (p : Nat) : Prop := p = 9 ∨ p = 4

theorem own_restricted_rival_consistent :
    SelfGood (standpoint ownProfiles) ∧
    OwnMonotone (standpoint ownProfiles) (· ≤ ·) ∧
    Supervenes (standpoint ownProfiles) ownProfiles ∧
    (∀ g, (standpoint ownProfiles).sig g → (standpoint ownProfiles).own g) ∧
    ((standpoint ownProfiles).own .changedSelf ∧ ¬ (standpoint ownProfiles).own .formedOther ∧
      degree .changedSelf ≤ degree .formedOther) ∧
    ¬ Monotone (standpoint ownProfiles) (· ≤ ·) := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · intro g own _
    cases g <;> simp_all [standpoint, ownOcc, ownProfiles, degree]
  · intro g g' og og' _ _ _ _
    cases g' <;> simp_all [standpoint, ownOcc, ownProfiles, degree]
  · intro g _; exact Iff.rfl
  · intro g h
    cases g <;> simp_all [standpoint, ownOcc, ownProfiles, degree]
  · refine ⟨trivial, id, by decide⟩
  · intro mono
    have h := mono .changedSelf .formedOther trivial trivial (show 4 ≤ 5 by decide)
      (show ownProfiles 4 from Or.inr rfl)
    simp [standpoint, ownProfiles, degree] at h

/-- What the unrestricted premise really packs: supervenience plus a valuation that is
monotone over the whole profile space. The rival above has a non-monotone valuation
over profiles, so the dispute is whether the own region may enter the profile. -/
theorem supervenient_monotone_val_gives_monotone {Gen Prof : Type}
    (s : Standpoint Gen Prof) (atLeast : Prof → Prof → Prop) (val : Prof → Prop)
    (sup : Supervenes s val) (valMono : ∀ p q, atLeast p q → val p → val q) :
    Monotone s atLeast := by
  intro g g' lg lg' le h
  exact (sup g' lg').2 (valMono _ _ le ((sup g lg).1 h))

/-! ## P5. A monist rival with a formed closure dimension in its profile.
Own-region membership is itself a formed relation (here a Bool coordinate).
It satisfies S0, UNRESTRICTED monotonicity, supervenience, and tolerance along every
small step of the graded coordinate; Diff fails and the stranger is not reached. -/

/-- The formed closure relation, as a Boolean coordinate; it coincides with `ownOcc`. -/
def closure : Occ → Bool
  | .nearSelf | .changedSelf => true
  | _ => false

theorem closure_iff_own (g : Occ) : closure g = true ↔ ownOcc g := by
  cases g <;> simp [closure, ownOcc]

def closureProf (g : Occ) : Bool × Nat := (closure g, degree g)

def closureLe (p q : Bool × Nat) : Prop := (p.1 = true → q.1 = true) ∧ p.2 ≤ q.2

def closureVal (p : Bool × Nat) : Prop := p.1 = true

def gradedStep (p q : Bool × Nat) : Prop := p.1 = q.1 ∧ adjacent p.2 q.2

def closureRival : Standpoint Occ (Bool × Nat) where
  prof := closureProf
  own := ownOcc
  living := fun _ => True
  reach := reachOcc
  sig := fun g => closureVal (closureProf g)

theorem closure_rival_escapes_both_steps :
    SelfGood closureRival ∧ Monotone closureRival closureLe ∧
    Supervenes closureRival closureVal ∧ Tolerant closureVal gradedStep ∧
    (¬ ∃ g g', closureRival.own g ∧ ¬ closureRival.own g' ∧
        closureLe (closureRival.prof g) (closureRival.prof g')) ∧
    ¬ closureRival.sig .formedOther ∧ ¬ closureRival.sig .stranger := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · intro g own _
    cases g <;> simp_all [closureRival, closureProf, closureVal, closure, ownOcc]
  · intro g g' _ _ le h
    exact le.1 h
  · intro g _; exact Iff.rfl
  · intro p q st h
    unfold closureVal at *; rw [← st.1]; exact h
  · rintro ⟨g, g', og, og', le⟩
    have := le.1
    cases g <;> cases g' <;> simp_all [closureRival, closureProf, closure, ownOcc]
  · simp [closureRival, closureProf, closureVal, closure]
  · simp [closureRival, closureProf, closureVal, closure]

/-! ## P6. In the argument's own two-dimensional profile, Diff fails under the product
order for EVERY standpoint, not only for the persistence rival. -/

theorem diff_fails_in_profile2_product_order :
    ¬ ∃ g g', ownOcc g ∧ ¬ ownOcc g' ∧ productLe (profile2 g) (profile2 g') := by
  rintro ⟨g, g', og, og', le⟩
  cases g <;> cases g' <;> simp_all [ownOcc, productLe, profile2]

/-- A balanced generative evaluator (continuity and formative contribution summed)
holds S0 and product-order monotonicity yet does not reach the formed other. -/
def balanced : Standpoint Occ (Nat × Nat) where
  prof := profile2
  own := ownOcc
  living := fun _ => True
  reach := reachOcc
  sig := fun g => 10 ≤ (profile2 g).1 + (profile2 g).2

theorem balanced_generative_escapes :
    SelfGood balanced ∧ Monotone balanced productLe ∧ ¬ balanced.sig .formedOther := by
  refine ⟨?_, ?_, ?_⟩
  · intro g own _
    cases g <;> simp_all [balanced, ownOcc, profile2]
  · intro g g' _ _ le h
    simp only [balanced] at *
    have := le.1; have := le.2; omega
  · simp [balanced, profile2]

/-- With a weighted-sum connection order, the formed other is at least as connected as
the changed self exactly when formative contribution is weighted at least 7:5 over
organizational continuity. -/
theorem weighted_diff_iff (a b : Nat) :
    a * (profile2 .changedSelf).1 + b * (profile2 .changedSelf).2 ≤
      a * (profile2 .formedOther).1 + b * (profile2 .formedOther).2 ↔ 7 * a ≤ 5 * b := by
  simp only [profile2]
  omega

/-! ## P7. A graded-weight rival (option (c) with a weight that reaches zero).
Weight changes by at most one unit per adjacent step (no jump in weight), is
monotone, and is positive on all own occurrences; positivity still ends before the
stranger. Its cut (profile 2) lies below every own profile, so it is not fixed by
the own boundary. -/

def weight (d : Nat) : Nat := d - 1

theorem graded_weight_rival :
    (∀ p q, adjacent p q → weight q ≤ weight p + 1 ∧ weight p ≤ weight q + 1) ∧
    (∀ p q, p ≤ q → weight p ≤ weight q) ∧
    SelfGood (standpoint (fun d => 0 < weight d)) ∧
    Monotone (standpoint (fun d => 0 < weight d)) (· ≤ ·) ∧
    (standpoint (fun d => 0 < weight d)).sig .formedOther ∧
    ¬ (standpoint (fun d => 0 < weight d)).sig .stranger ∧
    (0 < weight 2 ∧ ∀ g, ownOcc g → 2 < degree g) := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · intro p q h; unfold adjacent at h; unfold weight; omega
  · intro p q h; unfold weight; omega
  · intro g own _
    cases g <;> simp_all [standpoint, ownOcc, degree, weight]
  · intro g g' _ _ le h
    simp only [standpoint, weight] at *; omega
  · simp [standpoint, degree, weight]
  · simp [standpoint, degree, weight]
  · refine ⟨by decide, ?_⟩
    intro g own
    cases g <;> simp_all [ownOcc, degree]

/-! ## P8. The finite chain from own generation to the stranger passes through
profiles that no occurrence has: tolerance there is a claim about the evaluator's
valuation of merely possible relational profiles, not about actual occurrences. -/

theorem chain_passes_unoccupied_profiles :
    (∀ g : Occ, degree g ≠ 3) ∧ (∀ g : Occ, degree g ≠ 2) := by
  constructor <;> intro g <;> cases g <;> decide

end ReviewProbes
```

探针公理审计（`#print axioms`，全部 16 个定理）：`tolerance_vacuous_for_restricted_step`、`closed_step_is_threshold_restriction`、`supervenient_monotone_val_gives_monotone`、`chain_passes_unoccupied_profiles` 无依赖；`own_restricted_rival_consistent`、`closure_iff_own`、`closure_rival_escapes_both_steps`、`diff_fails_in_profile2_product_order` 依赖 propext；`tolerant_adjacent_down`、`tolerant_adjacent_up`、`tolerant_adjacent_constant`、`tolerance_reaches_unreachable_and_unrelated`、`tolerance_levels_down`、`balanced_generative_escapes` 依赖 propext 与 Quot.sound；`weighted_diff_iff`、`graded_weight_rival` 依赖 propext、Classical.choice 与 Quot.sound。
