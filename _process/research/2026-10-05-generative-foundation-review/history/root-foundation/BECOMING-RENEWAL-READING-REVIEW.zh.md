<a id="关系读法与依存动态的独立审查--independent-review-of-the-relational-reading-and-dependence-dynamics"></a>
# 关系读法与依存动态的独立审查

> **中文版（2026-10-17）。** 正典文本是[英文版](BECOMING-RENEWAL-READING-REVIEW.md)；本版由重构时从双语原文拆出，不与英文同步维护，两者有出入时以英文为准。

2026-10-09，Asia/Bangkok。**AI 独立审查（另一 agent，未参与撰写）。** 审查对象：

- 研究 [BECOMING-RENEWAL-READING](BECOMING-RENEWAL-READING.md) §§1–6（sha256 `984c9aae…f8262d3f`）；
- Lean 核心：[Becoming/Dependence.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Dependence.lean)（`9e2bd751…a5695cdd`）、[Becoming/Renewal.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Renewal.lean)（`a8c448c0…fdaca5e6`）、[Becoming/Metaethics.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Metaethics.lean)（`86af84d5…239acb94`），以及基础模块 [GenerativeCore](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean)（`e3daca1b…177069e8`）、[InquirySufficiency](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/InquirySufficiency.lean)（`d4a95ca8…65ad18f2`）、[RelationalRenewal](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/RelationalRenewal.lean)（`b97719c8…47cee1d4`）；
- 回执 [becoming-verification.json](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-verification.json)（`c96e0614…fd1baafa`，`utc` 20261008T233313.422223Z）；
- 正典章节 [THE-THEORY-OF-BECOMING](../../../../theories/becoming/chapters/THE-THEORY-OF-BECOMING.md) §§0–2、6.3、8、9（`954a17f2…9940e897`）；
- 记录 JSON：[becoming-renewal-reading](../../../../theories/becoming/results/records/becoming-renewal-reading.json)（`94e92c15…180790b1`）、[becoming-dependence-dynamics](../../../../theories/becoming/results/records/becoming-dependence-dynamics.json)（`37d022bf…4ebb1388`）、[becoming-stepwise-reading](../../../../theories/becoming/results/records/becoming-stepwise-reading.json)（`b1c6a399…fdc979ee`）、[relational-reading-comparison](../../../../theories/becoming/results/records/relational-reading-comparison.json)（`2ee03852…e3aba256`）、[relational-renewal-classification](../../../../theories/becoming/results/records/relational-renewal-classification.json)（`aeaaaaf4…560c354e`）、[metaethical-core-characterization](../../../../theories/becoming/results/records/metaethical-core-characterization.json)（`1f91617e…99d7c660`）。

本审查只新建本文件。未修改任何其他仓库文件，未运行 `check_becoming.py`、`make research-render`、`make research-check` 或任何仓库检查器，未提交。重新编译与探针都在仓库外的临时目录中进行；探针源码全文见附录。

<a id="english-summary"></a>

---

## 0. 范围与方法

**读了什么。** 全文阅读：[AGENTS.md](../../../../AGENTS.md)、[非二元方法](../../../../theories/becoming/chapters/NONDUAL-METHOD.md)、研究 §§1–6、`Becoming.Dependence`、`Becoming.Renewal`、`Becoming.Metaethics`、`RelationalRenewal`、六条记录 JSON 与回执。按需阅读：正典章节 §§0–2、6、8、9；[根基 §9](../../../../theories/becoming/chapters/BECOMING-FOUNDATION.md#9-the-content-of-the-whole-deduction)；`RenewalComparison` 的说明与 `relationalInventory`；`Becoming.Bridge` 的 `Conditions.living_iff_relational`；`Becoming.Frame` 的 `Frame`、`Run`、`Novel`；[统一计划](BECOMING-UNIFICATION-PLAN.md) P6 行；先例 [EVALUATOR-GROUNDING-REVIEW](../history/root-foundation/EVALUATOR-GROUNDING-REVIEW.md) 的格式部分。Ren 原话读了：[生生作为伦理方向](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md)、[不需公理分开更新与消耗](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md)（含“generative和degenerate……不overlap吧”）、[一元关系本体优先](../../../../sources/15-codex-theory-conversations/2026-10-08-monist-relational-ontology-first.md)、[纯净核心](../../../../sources/15-codex-theory-conversations/2026-10-09-pure-core.md)、[整体与 manifold](../../../../sources/15-codex-theory-conversations/2026-10-09-becoming-whole-generative-manifold.md)。

**文献依据。** 本次审查**没有新读任何外部文献**。以下均依据审查者的**先前知识**，只作转述，不作引文，细节须核对原文：Maturana 与 Varela 的自创生论（1980）；Jonas《The Phenomenon of Life》（1966）中的“需要的自由”；Thompson《Mind in Life》（2007）；Moreno 与 Mossio 的组织闭合论（2015）；Sen（1985）与 Nussbaum（2011）的能力进路；Lewis（1973）的反事实因果；Woodward《Making Things Happen》（2003）的干预主义差别制造；Schrödinger《What is Life?》（1944）；Nicolis 与 Prigogine 的耗散结构（1977）；Gunderson 与 Holling 的适应循环（2002）。

**分类纪律。** 依任务要求与非二元方法，每项发现标明属于以下哪一类：

- **（甲）** 表示省略了某一关系；
- **（乙）** 论证中有尚未解决的推论；
- **（丙）** 散文的表述超出了 Lean 所支持的内容；
- **（丁）** 形式上的错误或缺口（定义与其说明不符，或缺少所声称的定理）。

探针都是满足**已公布定义**的最小模型，检验的是这些定义本身，不推翻更完整的论述。若更完整的论述会排除某个探针情形，例如“只有曾被满足的依存才算依存”，那么排除它的关系正是表示所省略的，须写出来；这时该发现记为（甲）或（丁），而不是对理论的反驳。作者已在研究 §4、§6.4 承认的问题，只有在显示比所承认的更严重时，才算新的发现。

## 1. 总评

| 问题 | 结论 | 理由要点 |
|---|---|---|
| A. 关系读法的哲学根据 | **未确立；研究的表述过强** | 排除消耗者是定义的输入（2.1）；分类单位是形成或事件，不是关系，与章节 §1 及仓库自己的说明冲突（2.2，Q11）；读法中没有“继续生成”（2.3，Q3）；逐步读法有两处未披露的病理（2.4，Q1、Q2）；连通可免费得到，粗的共同条件又使 living 变空（2.5，Q4、Q5、Q10）；遗漏多种严肃的对手读法（2.6）；读法依赖运行，接不上框架层的 G0、C 与普遍理由（2.7） |
| B. Becoming.Dependence | **数学接受；三处散文拒绝；“形式实例”须收窄** | “三条去路”既不穷尽也不互斥（Q8）；两条一般定理是 `Dependent` 的逆否（Q6）；`loss_does_not_decide` 的去路由断裂之步的动作选定，“同一个断裂”依赖一步约定（Q7）；`Dip` 不是 living 的分歧（Q9）；结束与转化之分由 `F` 的同一性规定承担（Q13） |
| C. 形式复核 | **接受** | 只用前导重新编译通过；22 个源文件哈希与回执一致；70 项声明与 20 项探针定理公理报告全空 |
| D. 对应与超出 | **须更正** | 20 项，见 §6 |

---

## 2. 问题 A：关系读法的哲学根据

**结论：两种读法都可以作为公开规定的阐释，读出生生的一个方面，即“不损坏他者所依存的条件”。它们没有确立自己就是生生的读法。研究把规定说成了结论，并且遗漏了决定判决的大部分选择。**

所审的两条定义：

```lean
-- 整段读法（Becoming.Metaethics, Conditions.valuation）
living e := (K.along r).active e.2 e.1 ∧ ¬ ConsumingIn (K.along r) e.1
related e e' := ∃ c, Participates (K.along r) e.1 c ∧ Participates (K.along r) e'.1 c

-- 逐步读法（Becoming.Dependence, Web.RenewingAt；Web.valuation 取 living e := W.RenewingAt e.2 e.1）
def RenewingAt (t : Nat) (f : F) : Prop :=
  W.active t f ∧ ∀ c, W.Participates t f c → ∀ g, W.requires t g c → W.Kept t g c
```

### 2.1 排除消耗者是读法的输入，不是结论（乙；对研究措辞为丙）

研究 §4 反驳 3 的回应写道：消耗者的事件不算活的，“正是这样，而且这是结论的要点”。但这一排除写在 `living` 的定义里。`valuing_consumption_reaches` 证明的只是：在 N_rel 下，珍视一个非 living 的事件，会沿共同参与传到另一形成的 living 事件。它不是“消耗者不活”的论证。“结论的要点”应改为“阐释性的规定”。

来源上要分开两件事。

- **有 Ren 原话支持的部分。** Ren 要求“用关系结构把两种形成分开”，并说 generative 与 degenerate “不overlap”（[2026-10-09 原话](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md)）。因此，把退化排除在生生之外，有 Ren 的方向支持。
- **没有 Ren 原话支持的部分。** 以下三项是 AI 的阐释选择：
  - 分类单位取整个形成、整段运行；
  - 消耗型形成的**每个**事件都不算 living；
  - 把“持续”读成“在无穷运行中从不使任何依存者永久失去支持”。

研究应如此标明。

`RenewalComparison` 说这一读法对消耗者事件是“silence, not a negative verdict”。但在整合后的理论中，它与 C 连用：[relational-reading-comparison](../../../../theories/becoming/results/records/relational-reading-comparison.json) 证明，去掉消耗者的接续是一个生成性扩展，C 把它严格排在前面，即使消耗者自己的活动在每一步都相同。所以，这一读法在理论中是一个排序判决，不只是沉默。研究 §4 的回应应写明这一点。

### 2.2 分类单位是形成或事件，不是关系（乙）

仓库自己有两处说明。

- 正典章节 §1：“同一次活动可以使某种继续成为现实能力，同时毁掉另一种条件。”
- [2026-10-09 来源](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md)的 AI 修正说明：“不重叠不等于穷尽，一次发生也可同时参与两种关系。”

两种读法都把“两种关系都参与”的情形一律判为“不 living”：

- **整段读法：** 形成所汲取的任一条件在整段运行中被消耗，这一形成的全部事件就都不算；
- **逐步读法：** 事件所参与的任一条件上，任一依存在该步未被维持，这一事件就不算。

这不是 Ren 的“不overlap”所要求的。按“不overlap”，生成与退化作为**关系**不重叠，同一活动可以分别参与二者。以形成为分类单位，则把退化的一面扩大到整个形成。按 AGENTS.md 与非二元方法，“首要本体与工作起点是一元、关系”；以关系的某一端（形成）为分类单位，是两种选择中关系性较弱的一种。

**探针 Q11（`Late.early_condemned`）** 显示这一选择的后果：

- `early` 只在第 0 步活跃，它的那一步维持了条件，逐步读法记入这一事件；
- `late` 在第 1 步活跃，条件随后永久下降；
- 因为 `Conditions.draws` 不随时间变化，`early` 也被算作“汲取”这一条件，整段读法于是把 `early` 唯一的事件判为不 living。

整段读法的“消耗”追踪的是一个形成与某个条件最终命运的共同参与，不是它自己的汲取是否超出更新。研究 §6.4 反驳 2 只就逐步读法承认“读的是事件所处的关系，不是它的因果贡献”。整段读法有同样的性质，而“消耗者”“被它消耗的形成”（`valuing_consumption_reaches` 的说明）等措辞暗示了贡献。

**被遗漏的最直接对手：关系层读法。** 把被评价的主张取为关系：在某步上，一个形成对一个条件的依存或汲取关系。living 是这一关系被维持；或者对汲取关系而言，它的那一步没有断裂任何依存。这样，同一事件可以在一项关系上是生成的，在另一项上是退化的；这同时满足“不overlap”与章节 §1。现有 `Valuation` 直接支持这一读法：主张类型取 `F × C × Nat` 即可。

### 2.3 读法里没有“继续生成”（乙）

**探针 Q3（`inert_living`）：** 一个活跃、却不参与任何条件的形成，在两种读法下每一步都 living。

Ren 对伦理质量的回答是：

> 一种整体的，不断创造更多生的方向，而这个方向产生的可能性，多样性越高，复杂性/复杂结构的复杂度可以不断的上升，就是一个好的方向

两种读法只读出“不损”，即不消耗或不断裂；没有读出“生生”，即继续生成、更多、可能性与多样性。`RelationalRenewal.Law.formed` 存在，但没有进入 `living`。新的内容只在 `universal_reason` 的 `Novel` 中出现，而那需要框架层的读法（见 2.7）。

因此，“关系读法即生生的读法”至多是一半：不消耗或不断裂可以作为必要条件的候选，但不是生生本身。须二选一：

- 把 `living` 的注释改为“与更新相容的活跃”一类准确名称；
- 或者加入生成的成分，并公开这一前提。

### 2.4 逐步读法的两处未披露病理（丁；对“读法可用”为乙）

**Q1（`victim_not_living_stepwise`）：被断裂者自己在断裂之步的事件，逐步读法不记入。**

在 `Commons.escalating` 中，维持者第 1 步活跃，它的依存跨这一步断裂。整段读法记入 `(.sustaining, 1)`，逐步读法不记入。原因是 `RenewingAt` 遍历事件**参与**的每个条件，包括只是依存而不汲取的条件。于是在断裂的那一刻，被断裂者与断裂者被同样分类；`Web.valuing_breaking_reaches` 也到达不了被断裂者在这一步的事件。研究 §6.4、记录与章节都没有说明这一点。

**Q2（`Unmet.poisons_both`）：一个从未被满足的依存使每个参与者在每一步都不 living。** 在 Q2 的模型中：

- 条件水平恒为 0，任何一步都没有断裂（`Unmet.no_break`），`Dependent` 成立；
- 一个从不活跃的形成“依存”于该条件，所需水平为 1；
- 一个活跃的形成汲取该条件。

结果，两种读法都不记入这一汲取者的任何事件。现实中的对应：一个休眠的种子库依存于降雨，在每个干旱步上，它使每个参与水这一条件的形成都不 living。

- **逐步读法：** 原因是 `Kept` 要求依存在步的两端都被满足，从未被满足的依存既不是 `Kept`，也不是 `Broken`。
- **整段读法：** 原因见 3.5。

**来源：两种读法不对称。** 整段读法的 living 是“不消耗”型，只看所**汲取**的条件；逐步读法是“更新”型，看所**参与**的一切条件上的一切依存，不论它们是否被满足过。

**Q12（`variant`）。** 定义逐步变体 `NotBreakingAt`：事件活跃，且在它所汲取的条件上，它的那一步没有断裂任何依存。这一变体：

- 保留研究公布的两个方向的分歧：`escalating` 第 0 步记入，`dipping` 第 0 步不记入；
- 记入被断裂者的事件；
- 不受未满足依存的影响。

所以，“两个方向都有分歧”是稳健的；两处病理则是选择了“更新”型逐步谓词的产物。Q12 不证明这一变体就是对的，只说明已公布的逐步读法不是唯一的逐步读法，研究须比较并给出理由。作者反驳 5（季节性下降过严）比这两处轻。

### 2.5 共同参与过粗：连通来自条件清单（乙；对“由展开给出”为丙）

**`related` 不管时间。**
- 整段读法的 `related (f, t) (g, t')` 与 `t`、`t'` 无关，也不管两个形成在各自的时间是否活跃。
- 逐步读法的 `related` 要求每个事件在各自的步上参与同一条件，但两个步可以相隔任意远。

**Q5（`co_requirement_relates`）：两个只依存于同一条件、彼此毫无影响的形成，也是 related。** 这与 `Becoming.Metaethics` 模块说明中的注释矛盾：“`related` is a nonzero formed relation (conditioning, dependence, descent, cooperation)”。

**Q5（`drawing_reaches`）：消耗不承担传递。** 在 N_rel 下，珍视**任何**汲取者的事件，都会传到依存于同一条件的每个 living 事件，不需要任何消耗。所以 `valuing_consumption_reaches` 的传递部分不用消耗；消耗只用来挑出一个失去支持的 `g`。“消耗本身是一种已形成的关系”（研究 §2、章节 §6.3、记录）应改为：消耗者与失去支持者共同参与同一条件，N_rel 沿这一共同参与传递。

**Q4（`withCommon_living`、`withCommon_connected` 及其 `Conditions` 版本）：连通可以免费得到。** 对**每一个**依存网，以及每一个 `Conditions` 与运行，加入一个人人依存、所需水平为 0 的条件，结果是：

- `living` 不变；
- 整体连通。

所以“连通由展开给出，不再假设”（章节 §0 前提卡、§6.3，`significant_iff_of_common` 的说明）只相对于一条对应纪律才成立：什么算条件，什么算参与。没有这条纪律，连通是免费的。前提只是从 `Connected` 移到了条件清单，并没有被解除。

**Q10（`common_consumed_empties`、`common_unkept_empties`）：连通与 living 的非空彼此冲突。** 研究 §4 用“生物圈、气候”作共同条件的例子。这类粗的条件，正是其上某个依存会失败的条件：

- **整段读法：** 若每个形成都汲取 c₀，而 c₀ 被消耗，则没有任何 living 事件；
- **逐步读法：** 若某步每个形成都参与 c₀，而 c₀ 上某个依存在该步未被维持，则该步没有任何 living 事件。

共同条件越粗，连通越容易，living 也越空，两者方向相反。作者反驳 2 的回应没有看到这一点。

**后果。** 伦理内容不只落在 N_rel 上（作者反驳 2），而是落在 N_rel **加上**建模者对条件与参与的选择上，而理论并不约束这一选择。拒绝 G0 的一方可以接受 N_rel，同时否认“对一个惰性或过粗条件的共同参与”属于 N_rel 所说的已形成关系。这仍是边界之争：争的是哪些关系算数。研究所说“拒绝 G0 的一方，现在必须拒绝 N_rel 或 N_std”掩盖了这一点。

### 2.6 被省略的对手读法（乙）

研究只比较了整段与逐步两种读法，并把周期层与差别制造列为“下一步”。以下对手读法都会改变判决，研究须说明为何不取：

1. **关系层读法**（见 2.2）。
2. **整体方向读法。** Ren 的原话是“一种整体的……方向”。被评价的是运行或整体：活的可能性、多样性与组织复杂度是否得到维持或增长。按形成或事件分类，表示不了“更多”与“多样性”。C 在比较中承担了一部分，`living` 没有。
3. **周期层读法。** 作者已承认（反驳 5；`fluctuating_neither`）。生态学的适应循环（Gunderson 与 Holling，先前知识）以释放与重组为更新的一部分，而在整段读法下，一次永久的局部丧失就足以使参与者“消耗”。
4. **反事实或差别制造读法**（Lewis；Woodward，先前知识）。依这一读法，一个形成是消耗型的，当且仅当它的活动对丧失造成差别。研究把它当作“归属”问题推到下一步。但对“消耗”这个名称而言，它是首要的对手：Q11 显示，整段读法会判定一个没有造成差别的形成为消耗型。前提卡写明“不假定每个处境都有确定的全局因果次序”；差别制造不需要全局次序，在有定义的地方用局部的干预反事实即可。
5. **能力或繁荣读法**（Sen；Nussbaum，先前知识）。living 是已实现并保持开放的功能能力；消耗以他者能力的丧失来衡量。这一读法直接给出 Ren 所说的“可能性”与“多样性”。
6. **自创生或代谢读法**（Maturana 与 Varela；Jonas；Thompson；Moreno 与 Mossio，先前知识）。依这一读法，活的组织靠汲取并转化条件来维持自身，汲取下降本身就是生命的构成部分，“不消耗”不能作为生命的判据。要区分的，是在更大关系的更新之内的代谢，还是对这些关系的破坏。这又指向周期层或关系层读法。
7. **热力学读法**（Schrödinger；Nicolis 与 Prigogine，先前知识）。每个活的过程都消耗自由能梯度。在一个终将耗尽的宇宙中，每个条件最终都永久低于某个依存者的需要。按 Q10a 的模式，整段读法在整个历史中都没有 living 事件；逐步读法则保留此前各步。这是对无穷运行上“不息”的直接压力。
8. **认识上的可判定性。** 整段读法的 `¬ ConsumingIn f` 涉及整个无穷未来。`Consumed` 是“存在……对一切……”形式的命题，任何有限历史都不能证实，也不能否证。作为实践或对齐用途中的 living 读法，这是缺陷：没有任何有限探究能判定一个事件是否 living。逐步读法可以由 `t` 与 `t+1` 两步的可观测量判定。

本审查不要求研究采纳其中任何一种，只要求比较并给出理由。

### 2.7 “公开的对应选择”是否正当（乙；甲）

把读法选择作为公开的状态，这是诚实的。但有三个问题。

1. **前提卡与 §6.3 不一致。** 章节 §0 前提卡在 `living` 一行只列出 `Conditions.valuation`（整段读法）；§6.3 却说两种读法的选择仍是开放的。
2. **读法依赖运行，接不上框架层。** 框架层的 `Novel F reading before`、`G0 F living positive`、`Extension`、`Comparison` 与 `universal_reason`，所取的 `living : C → Prop` 不依赖运行，也不依赖配置。`Conditions.valuation K r` 依赖运行 `r`，而 `class_belongs_to_the_run` 正好证明这一分类不是配置的函数。因此，关系读法可以作为 `significant_iff_of_common` 中某一次运行上 `Valuation` 的 `living`，却不能直接接入框架上的 `universal_reason`、C 或 J，除非另作一个构造（例如以运行为索引的主张），而这一构造没有给出。下面三处说法，只对单次运行上的刻画定理成立：
   - “Becoming 层可以给出 `living` 与 `related`”（章节 §6.3）；
   - 章节 §6.4 中“连通……是展开的事实”。
3. **只说开放，不给判据。** 两种读法在理论关心的情形上判决不同：加码、短暂下降、被断裂者、较早的汲取者。说它们“回答不同的问题”（研究 §6.4 反驳 3）是对的，但那样两者都不能单独是“生生的读法”。而且选择决定哪些结果成立：整段读法支持 relational-reading-comparison 的排序，逐步读法还没有 C 排序。建议的判据：
   - 符合 Ren 有来源的判决：恶性增殖、军备竞赛、以消耗取胜都不是生生；
   - 不因一个条件的命运而判定未改变这一条件的被断裂者或旁观者；
   - 可由有限探究判定；
   - 含有继续生成的成分；
   - 加入惰性条件时判决不变。

### 2.8 最强反驳与会改变判断的结果

**对本审查的最强反驳。**
- Ren 授权不加公理地分开更新与消耗，G0 的对象依 Ren 原话就是生生；读法是阐释，不是论证。
- 非二元方法说，弱模型中自由开关的谓词不推翻更完整的论述；Q2、Q4 用的是退化的条件（未满足的依存、所需为 0 的条件）。

**回应。**
- 这些探针检验的是已公布的定义，在它们自己的范围内。这些定义被提出作为 `living` 与 `related` 的形式内容。
- 如果更完整的论述会排除 Q2 或 Q4，例如规定“只有曾被满足的依存才算依存”，或“只有活动会改变其水平的条件才算条件”，那么这一排除正是表示所省略的关系，须写出来。它现在不在 Lean、记录或研究中。

**会改变本审查判断的结果。**
1. 一条排除惰性或虚设条件的对应规则，并证明在某个声明的类中，连通在这一规则下仍然成立。
2. 公开比较关系层读法与限于汲取的逐步读法，并论证哪一种是生生的读法。
3. 一个不依赖运行的读法，并与 `universal_reason` 接通。
4. 在 `living` 中加入继续生成的成分。

---

## 3. 问题 B：Becoming.Dependence

**结论：定义与证明正确；静态复原精确；时间步引理正确且是构造性的。三处散文须撤回或改写，“形式实例”须收窄。**

### 3.1 “三条去路”不是一个划分（丙）

Lean 中没有“断裂之后，终止 ∨ 转化 ∨ 恢复”形式的定理，也没有它们互斥的定理。已有的是：

- `continuing_restores`、`consumed_continues_transformed`、`consumed_ends_when_fixed`；
- 见证 `loss_does_not_decide`。

逐步来看，经典的析取“不活跃 ∨ 活跃且依存已减弱或消解 ∨ 活跃且依存未减弱（这时水平满足旧的需要）”是平凡穷尽的，而且根本不需要有损失。

**Q8（`Overlap.overlap`）。** 同一个断裂之后：

- 一个形成转化；
- 另一个形成终止；
- 条件随后恢复（`¬ web.Consumed .first`）。

条件的恢复与终止、转化同时发生。恢复是关于条件的事实，终止与转化是关于形成的事实，三者不在同一个轴上。Lean 中的“终止”（`∀ t, 0 < t → ¬ active t ()`）还包括永久休眠；恢复运行本身在第 1 步也不活跃。

下面几处的表述过强：

- 模块说明：“Ending, transformation and restoration are the three ways through a loss”；
- 记录标题与章节 §1 中的“损失的三条去路”；
- 研究 §6.2。

准确的表述是：定理把三种结果联系起来——依存不变且无回程时，形成不再活跃；无回程之后仍活跃，意味着依存已转化；以不弱于先前的依存活跃，意味着水平满足旧的需要。作为运行层面的结局，它们既不穷尽，也不互斥。

### 3.2 两条一般定理是 `Dependent` 的逆否（丙；`Dependent` 是承重的对应前提）

```lean
theorem continuing_restores (dependent : W.Dependent) {T t : Nat} {g : F} {c : C}
    (active : W.active t g) (depends : W.requires t g c)
    (unchanged : W.need T g c ≤ W.need t g c) : W.need T g c ≤ W.level t c :=
  Nat.le_trans unchanged (dependent t g active c depends)
```

**Q6（`transformed_any_bound`）：** 对任意界 `N`，`W.level t c < N → W.active t g → ¬ (W.requires t g c ∧ N ≤ W.need t g c)`。`consumed_continues_transformed` 是它取 `N := W.need T g c` 的实例；`T`、断裂与损失都不起作用。

作者承认“证明很短”（§6.4 反驳 1），这是准确的。但作者所说的内容所在，即“转化变得可以表达”，是表示的性质（依存与需要可变），不是这两条定理的性质。

**`Dependent` 的内容。** `Dependent` 是同步耦合：活跃，就意味着对当前每个依存，所需水平不超过当前水平。它排除了缓冲、储备与滞后，例如多年生植物靠储备熬过一个旱年，企业靠信贷度过一段时间。应用须把储备另建为条件，而这会改变什么算作“那个”损失。`Dependent` 的披露情况：

- 已写明：记录 `hypotheses[1]`；章节 §1 中文（“形成只在有支持处活跃时”）。
- 未写明：模块说明的结果列表；研究 §6.2 表；章节 §1 英文；研究 English summary。

### 3.3 `loss_does_not_decide`：存在性见证，去路在断裂之步就由动作选定（丙）

```lean
def process : Process State Move where
  step s a t := match a with
    | .rest => t = s
    | .fall m => s.first = 1 ∧ t = ⟨0, m⟩
    | .renew => s.mode = .dormant ∧ t = ⟨1, .onFirst⟩
```

构成损失的那一步 `fall m` 本身就选定了形成的模式。终止与转化在断裂之步内就已确定；恢复运行中的休眠也是如此，之后发生的只有更新。

所以这条定理显示的是：对断裂的读法 `Broken 0 () .first`（只依赖第 0 步的状态与第 1 步的水平）不决定后继配置。作为非决定性的见证，它有效；但这是给 `fall` 一个自由的模式参数造出来的。它不显示“去路由后续关系决定”：

- 研究 §6.4 反驳 1 的回应：“去路由后续关系决定（形成是否改变依存、条件是否得到更新）”；

它的价值是一致性见证：在 `Dependent` 下、从同一配置出发，3.2 的约束允许三种结局都出现。作者反驳 6 已把它定位为可能性见证，这一定位正确；需要改的是上面两处措辞。

### 3.4 一步约定承载“同一个断裂”（乙；已披露，但没有在承重处说明）

**Q7（`convention_carries_the_same_break`）。** 改取步末约定 `BrokenAtEnd`，要求依存在步的两端都成立。这时：

- 终止运行与转化运行都没有断裂，只有恢复运行有；
- 终止运行中，对 `first` 的依存也跨第 0 步 `Dissolves`，因为 `ended` 模式不依存于任何条件。

所以，“同一个断裂分别通向终止、转化与恢复”只在步首约定下成立。转化运行中 `Lost .first` 成立，而第 0 步之后已没有任何形成依存于 `first`。

这一约定在模块说明、研究 §6.1 与记录 `hypotheses[2]` 中已有披露，但在它承重的地方没有说明：`loss_does_not_decide` 的说明、章节 §1、研究 §6.2 与记录的 `claim`。另外，`Crossing` 中的“终止”同时也是依存的消解：在这一读法中，形成的终结与依存的解除无法区分。

### 3.5 `Consumed` 不要求依存曾被满足（丁）

```lean
/-- A dependence holding at some step is never met again afterwards. -/
def Consumed (c : C) : Prop :=
  ∃ g T, W.requires T g c ∧ ∀ t, T < t → W.level t c < W.need T g c
```

继承的 `RelationalRenewal.Consumed` 的说明是“Some formation depending on the condition loses its support from some step on”。说明中的 “again” 与 “loses” 都预设了先前的支持，定义却不要求 `T` 时 `need ≤ level`。

- **Q2：** 一个从未被满足的依存使条件成为 `Consumed`，每个汲取者都成为 `ConsumingIn`，同时 `Dependent` 成立，任何一步都没有断裂。
- **`Lost` 有这一预设。** `Lost` 的定义是 `Broken T g c ∧ …`。`lost_consumed` 证明了 Lost → Consumed，Q2 显示其逆不成立。

**更正选项。** 在 Becoming 层：

- 用 `Lost` 定义消耗型，或在 `Consumed` 中加入“`T` 时已被满足”；
- 或者改写说明，并在记录中披露 Q2 的后果。

`RelationalRenewal` 属于基础模块，改它会改变 L0 的字节与回执，所以在那里至少应作披露。`static_consumed` 精确复原了这一定义，两层须一致。

### 3.6 “两个方向都有分歧”：方向准确，`Dip` 不在其中（丙）；另有一种未披露的分歧（丁）

`Commons.readings_differ` 准确：

- 第一个方向：加码运行第 0 步，逐步读法记入，整段读法不记入；
- 第二个方向：短暂下降运行第 0 步，整段读法记入，逐步读法不记入。

Q12 显示，这两个方向在限于汲取的变体下仍然成立。

`Dip.renewing_at_each_step_not_in_run` 比较的是 `RenewingAt` 与整段**更新** `RenewingIn`，而不是与整段 **living**（活跃 ∧ ¬`ConsumingIn`）比较。

**Q9（`dip_keeper_credited_by_both`）：** 维持者不汲取任何条件，`¬ Dip.web.ConsumingIn .keeper`；它的每个活跃事件，两种读法都记入。

所以，把 `Dip` 放在“两种读法两个方向都有分歧”之后列出，会误导读者。这样列出的地方有：

- 模块说明的最后一项结果；
- 记录的 `counterexamples[0]`；
- 章节 §2 的“逐步读法”段。

此外：

- `keeperActive` 是按“在步的两端都满足其需要”定义的，所以这一结果接近定义；
- `Dip.web` 是一个裸的依存网，不是某个过程的运行。任何依存网都是平凡时钟过程的运行，这一点只是表面问题。

Q1 才是 `living` 上一种真实而未披露的分歧：被断裂者在断裂之步的事件。

### 3.7 时间步引理与静态复原（无问题）

- **时间步引理。** `ceases_at_a_step` 与 `arises_at_a_step` 正确，不用排中律，陈述为 `¬ ∀ s, T ≤ s → s < t → ¬ (p s ∧ ¬ p (s + 1))`。它们的内容是 `Nat` 上的离散归纳，与依存本身无关；“变化发生在步上”是离散时间表示的性质。这一点值得注明，但不必更正。
- **静态复原。** 六条 `static_*` 与 `conditions_along` 的精确复原已核对：`static_consumed` 在 `T` 与 `T + 1` 之间来回平移，正确。

### 3.8 “关系整体与分化的形式实例”须收窄（丙；甲）

**实际显示的内容。**
- `Kept`、`Broken`、`Forms`、`Dissolves` 与 `Lost` 可以由同一个记录类型 `Web` 定义；
- `Web` 的五个字段彼此独立；
- 活跃与依存之间唯一的耦合是可选的不等式 `Dependent`；
- `draws` 与任何东西都不耦合，水平的动力学是自由的。

**Q13（`Reindex.ends_and_forms`）。** 把转化运行重新索引为两个形成。不命名形成时，这一历史与原来相同：水平相同，每一步活跃的依存也相同。在新的索引下，这一损失终止了一个形成，另一个形成随之出现。一段历史是“转化”还是“终止加上新形成”，由固定的索引类型 `F` 所规定的同一性决定，而不是由依存结构决定。形成本身怎样形成，即相对持久的组织怎样个体化并穿过变化保持同一，正是非二元方法放在首位的问题，这里没有表示。

[根基 §9](../../../../theories/becoming/chapters/BECOMING-FOUNDATION.md#9-the-content-of-the-whole-deduction) 写道：“Shared inclusion in a description cannot replace the argument for this substantive claim.” 一个由独立字段组成的记录，正是共同纳入一个描述，再加一条约束。研究说“不完成整体演绎”，这一限定是对的；正面的说法则应收窄为：

> 在一个形成被给定、各字段除 `Dependent` 外彼此独立的表示中，几种变化方式可以由共同的可观测量定义；终止与转化之分依赖所规定的形成同一性。

---

## 4. 问题 C：形式复核

### 4.1 独立重新编译

在仓库外的临时目录 `/private/tmp/claude-501/review.hpJg/` 中：

- 复制 `GenerativeCore.lean`、`InquirySufficiency.lean` 与 `RelationalRenewal.lean` 到根目录；
- 复制 `Becoming/{Frame,Inquiry,Renewal,Dependence,Metaethics}.lean` 到 `Becoming/`；
- 删去 `import Std`。三个基础文件中只有 `GenerativeCore.lean` 有这一行：`InquirySufficiency` 只导入 `GenerativeCore`，`RelationalRenewal` 不导入任何模块。

按依赖顺序编译：

```text
LEAN_PATH=<tmp> ~/.elan/bin/lean +leanprover/lean4:v4.29.1 -o X.olean X.lean
  GenerativeCore        exit 0
  Becoming/Frame        exit 0
  InquirySufficiency    exit 0
  Becoming/Inquiry      exit 0
  RelationalRenewal     exit 0
  Becoming/Renewal      exit 0
  Becoming/Dependence   exit 0
  Becoming/Metaethics   exit 0
```

Lean 版本：`4.29.1, arm64-apple-darwin24.6.0, commit f72c35b3f637c8c6571d353742168ab66cc22c00`，与回执 `lean_version` 一致。核心只用前导即可编译，与回执的 `core_compiles_from_prelude: true` 一致。

### 4.2 哈希

回执 `source_paths` 中的 22 个源文件，当前字节的 sha256 全部与 `source_sha256` 一致。与本审查直接相关的几项：

| 模块 | sha256（当前 = 回执） |
|---|---|
| GenerativeCore | `e3daca1b729118fc309585a5d3ba1af60ac99cd80bab41e477aed204177069e8` |
| InquirySufficiency | `d4a95ca842f46ffa9c23eea92d04cdb45027dc6842148d3d0bdc17cd65ad18f2` |
| RelationalRenewal | `b97719c886e3dcd0f143a23db62fb7b8556dac35ec5c312fcdf7e14d47cee1d4` |
| Becoming.Renewal | `a8c448c07d0b0c5c9d889552286579d515f2751ca01e08f239d8fcc1fdaca5e6` |
| Becoming.Dependence | `9e2bd75187e380f0108702babeb471af29f9b19a4381deccee798adba5695cdd` |
| Becoming.Metaethics | `86af84d5e767ca82f64dcdb14c6b64a25f7cd4f58c7190e004ff1d09239acb94` |

其余 16 项（Frame、Inquiry、根模块 Becoming、Bridge 与 12 个继承模块）同样一致。记录 becoming-dependence-dynamics 与 becoming-stepwise-reading 中回执的引用哈希 `c96e0614…`、研究的引用哈希 `984c9aae…`，都与当前文件一致。

### 4.3 公理依赖

审计文件 `Audit.lean` 对 70 项声明执行 `#print axioms`。这 70 项包括：

- `Becoming.Dependence` 的全部定理与主要定义；
- `Becoming.Renewal` 的 6 项定理；
- `Becoming.Metaethics` 两节读法中的全部声明；
- `significant_iff` 与 `universal_reason`。

70 项全部报告 “does not depend on any axioms”。题目所点名的 `Becoming.Crossing.loss_does_not_decide`、`Becoming.Web.consumed_continues_transformed`、`Becoming.Commons.readings_differ`、`Becoming.Web.valuing_breaking_reaches`、`Becoming.ceases_at_a_step` 都在其中。

回执中按模块列出的公理依赖全部为空：RelationalRenewal 60 项、Becoming.Renewal 14 项、Becoming.Dependence 71 项、Becoming.Metaethics 66 项声明，`kernel_checked: true`。

定理数也已核对：

- Metaethics 新增 6 项（`Web.connected_of_common`、`Web.significant_iff_of_common`、`Web.breaking_relates`、`Web.valuing_breaking_reaches`、`Conditions.stepwise_related`、`Commons.readings_differ`），合计 32 项。

这与研究 §6、记录及章节 §9 的数字一致。

### 4.4 探针

探针文件 `ReviewProbes.lean`（sha256 `81ee6b4b01e48d1231d960e2f64cb44dd6a9ed1805638bd6861b447568377803`）导入未改动的 `Becoming.Metaethics`，在 Lean 4.29.1 下编译通过（exit 0），没有 `sorry`。20 项探针定理全部没有公理依赖。全文见附录。

| 探针 | 定理 | 显示什么 | 类别 |
|---|---|---|---|
| Q1 | `victim_not_living_stepwise` | 被断裂者在断裂之步的事件：整段读法记入，逐步读法不记入 | 丁／乙（2.4） |
| Q2 | `Unmet.no_break`、`Unmet.dependent`、`Unmet.poisons_both` | 无变化、无断裂、`Dependent` 成立，一个未满足的依存使汲取者在两种读法下都不 living | 丁（3.5）、乙（2.4） |
| Q3 | `inert_living` | 不参与任何条件的活跃形成，两种读法下每步都 living | 乙（2.3） |
| Q4 | `withCommon_living`、`withCommon_connected`、`conditions_withCommon_living`、`conditions_withCommon_connected` | 对每个依存网与每个 `Conditions`／运行，加入一个所需为 0 的共同条件，living 不变而整体连通 | 乙／丙（2.5） |
| Q5 | `drawing_reaches`、`co_requirement_relates` | N_rel 下珍视任一汲取者即传到同一条件上每个 living 依存者，不需要消耗；只是共同依存也算 related | 丙（2.5） |
| Q6 | `transformed_any_bound` | `consumed_continues_transformed` 是任意界下 `Dependent` 逆否的实例 | 丙（3.2） |
| Q7 | `convention_carries_the_same_break` | 步末约定下，终止与转化两次运行都没有断裂；终止运行的依存也消解 | 乙（3.4） |
| Q8 | `Overlap.overlap` | 同一断裂后一个形成转化、一个终止，而条件恢复 | 丙（3.1） |
| Q9 | `dip_keeper_credited_by_both` | `Dip` 的维持者在两种 living 读法下都被记入 | 丙（3.6） |
| Q10 | `common_consumed_empties`、`common_unkept_empties` | 粗的共同条件使 living 变空 | 乙（2.5） |
| Q11 | `Late.early_condemned` | 整段读法下，较晚的断裂者使较早、在更新之内的汲取者不 living | 乙（2.2） |
| Q12 | `variant` | 限于汲取的逐步变体保留两个方向的分歧，并去掉 Q1、Q2 | 乙（2.4） |
| Q13 | `Reindex.ends_and_forms` | 同一匿名历史，重新索引后，“转化”读成“终止加新形成” | 甲／丙（3.8） |

**探针本身的限度。** 这些都是最小模型。它们显示的是已公布的定义允许什么，不显示实际系统中什么常见。Q4 与 Q2 用的是退化的条件。正因为如此，它们指出了一条对应纪律：什么算条件，什么算依存。这条纪律须写出来，见 2.8。

---

## 5. 问题 D：对应与超出（汇总）

| 位置 | 表述 | Lean 实际支持的内容 | 类别 |
|---|---|---|---|
| 研究 §4 反驳 3 回应 | 排除消耗者“是结论的要点” | 排除写在定义中；定理只做传递 | 丙（2.1） |
| 研究 §2、English summary；章节 §6.3；记录 becoming-renewal-reading `claim`；`consumption_relates` 说明 | “消耗本身是一种已形成的关系” | 用到的关系是共同参与；消耗只用来挑出 `g`（Q5） | 丙 |
| 章节 §0 前提卡“连通”行；§6.3；`significant_iff_of_common` 说明 | 连通“由展开给出，不再假设” | 相对于条件清单；加入虚设条件即可免费得到（Q4） | 丙、乙 |
| 章节 §0 前提卡“`living` 的读法”行 | 只列 `Conditions.valuation` | §6.3 说两种读法都开放 | 丙 |
| `Becoming.Metaethics` 模块说明第 9–12 行 | `related` 是 “nonzero formed relation (conditioning, dependence, descent, cooperation)”；`living` 对应 “renewing formation” | 所给的 `related` 是共同参与，包括互不影响的共同依存（Q5）；所给的 `living` 是“不消耗”，波动型也算在内 | 丙 |
| 章节 §6.3；metaethical-core-characterization `next_delta` | Becoming 层给出 `living` 与 `related` | 只对单次运行上的刻画定理成立；框架层的 `universal_reason`、C、J 需要不依赖运行的 `living`（2.7） | 乙、丙 |
| `Dependence` 模块说明；记录 becoming-dependence-dynamics 标题与 `claim`；章节 §1；研究 §6.2 | “三条去路” | 没有穷尽或互斥的定理；三者不在同一轴上（Q8） | 丙 |
| 研究 §6.4 反驳 1；记录 `limitations` | 去路“由后续关系决定” | 去路在断裂之步由 `fall m` 选定 | 丙 |
| `loss_does_not_decide` 说明；章节 §1；研究 §6.2 | “同一个断裂” | 三次运行中有两次依赖步首约定（Q7） | 乙 |
| 模块说明结果列表；研究 §6.2 表；章节 §1 英文；研究 English summary | 三条一般定理没有写出 `Dependent` | 定理都以 `Dependent` 为前提，且内容就是它的逆否（Q6） | 丙 |
| `Web.Consumed`、`RelationalRenewal.Consumed` 的说明 | “never met again”“loses its support” | 定义不要求曾被满足（Q2） | 丁 |
| 模块说明；记录 becoming-stepwise-reading `claim` 与 `counterexamples[0]`；章节 §2 | 把 `Dip` 列为两种读法的分歧 | `Dip` 比较的是更新，不是 living（Q9） | 丙 |
| 研究 §6.4、§6.5；记录 becoming-stepwise-reading | 逐步读法唯一披露的严格性是季节性下降 | 被断裂者与未满足依存两处病理（Q1、Q2） | 丁 |
| `Web.valuing_breaking_reaches` 说明（“values a breaking event”）；章节 §6.3“断裂本身是一种关系” | 暗示该事件造成了断裂 | 事件只是在断裂之步汲取；断裂可由别者造成 | 丙 |
| 研究 §6.2 解读；记录 becoming-dependence-dynamics `related[2]` | “关系整体与分化的形式实例” | 五个独立字段加一条约束；终止与转化之分依赖索引同一性（Q13） | 丙、甲 |
| 研究 §2 L4 表 | 把 `living_iff_relational` 列在 `Becoming.Metaethics` 下 | 它在 `Becoming.Bridge`（外围）中 | 丙（小） |
| 章节 §8 表 | “逐步读法：已完成” | 已定义并比较；读法选择与两处病理仍开放 | 丙（小） |

**关于方法的三点。**

1. **没有发现把表示的省略当作反驳。** `Separate.not_connected` 是非蕴涵的见证，作者如实标注；`Crossing` 与 `Commons` 也被如实标为可能性见证。问题出在反方向：定义中写入的内容被当作发现来陈述，例如“消耗本身是一种关系”“断裂本身是一种关系”。
2. **形成与条件是固定的索引类型（甲）。** 记录 `correspondence` 写道：“Formations and conditions are analytic roles in one unfolding, not independent entities.” 这是一项声明；在 Lean 中，`F` 与 `C` 是贯穿整个运行的固定类型，形成的同一性是预设的。Q13 显示这一预设是承重的。这一点继承自 `RelationalRenewal`，在当前范围内可以接受，但应写明。
3. **`draws` 不带数量（甲）。** 表示记录了一个形成汲取某个条件，却没有记录汲取多少，也没有记录这一汲取怎样改变水平；水平的动力学与 `draws` 无关。“消耗”“断裂”“被它消耗的形成”等名称暗示的贡献关系，在这里被省略了。非二元方法要求“说明所消耗或所需的资源、操作与数量”；这正是这里缺少的。

---

## 6. 须作的更正（未执行）

审查者只列出更正，不执行。

1. **研究 §4 反驳 3 的回应。** 把“这是结论的要点”改为“这是阐释性的规定”。分清哪些有 Ren 原话支持（区分更新与消耗；生成与退化不重叠），哪些是 AI 的阐释选择（以形成为分类单位；消耗型形成的全部事件都不算；无穷运行上的“持续”）。补写：与 C 连用时，这一读法给出排序判决（relational-reading-comparison），不只是沉默。
2. **研究 §2 与 English summary、章节 §6.3、记录 becoming-renewal-reading 的 `claim`、`consumption_relates` 与 `valuing_consumption_reaches` 的说明。** 把“消耗本身是一种已形成的关系”改为：“消耗者与失去支持者共同参与同一条件；N_rel 沿这一共同参与传递，消耗本身不承担传递”（Q5）。
3. **章节 §0 前提卡“连通”行、§6.3、`significant_iff_of_common` 的说明、记录 becoming-renewal-reading 与 becoming-stepwise-reading。** 把“连通由展开给出”改为“在一条关于条件与参与的对应纪律下，由共同条件给出”，并写明：没有这条纪律，连通是免费的（Q4）；共同条件越粗，living 越空（Q10）。
4. **`Becoming.Metaethics` 模块说明第 9–12 行。** 把 `related` 的注释与所给的共同参与对齐，或者说明共同依存、共同汲取在什么条件下才算“nonzero formed relation”。把 “matching it to renewing formation” 改为与定义一致的 “non-consuming”（整段读法）或 “step-keeping”（逐步读法）。
5. **章节 §0 前提卡“`living` 的读法”行。** 同时列出 `Conditions.valuation` 与 `Web.valuation`，写明选择开放，并指向本审查 2.7 的判据。
6. **章节 §6.3、§6.4，metaethical-core-characterization 的 `next_delta` 与 `correspondence`。** 写明关系读法依赖运行，只为单次运行上的 `significant_iff_of_common` 提供 `living` 与 `related`。要用于 `universal_reason`、`Comparison` 与 J，须另作一个不依赖运行的构造；把它列为下一步。
7. **研究 §2.3（新增，或并入 §4）。** 写明两种读法都没有继续生成的成分（Q3），二选一：把 `living` 的注释改为“与更新相容的活跃”一类准确名称；或者加入生成的成分，并在前提卡上公开。
8. **研究 §4 或新增一节。** 加入对手读法的比较：关系层、整体方向、周期层、差别制造、能力、自创生或代谢、热力学；并写明整段读法不能由有限历史判定。对每一种说明为何不取，或者把它列为开放问题。
9. **研究 §6.4、§6.5，记录 becoming-stepwise-reading 的 `counterexamples`。** 披露 Q1（被断裂者在断裂之步不 living）与 Q2（未满足的依存使所有参与者不 living）。考虑限于汲取的变体（Q12），并说明为什么选“更新”型谓词而不选“不断裂”型谓词。
10. **`Web.Consumed` 与 `RelationalRenewal.Consumed` 的说明；记录 becoming-dependence-dynamics、relational-renewal-classification。** 改写说明（“never met again”“loses its support”），或者在 Becoming 层改用 `Lost` 定义消耗型。若不改 `RelationalRenewal` 的字节，在其记录中披露这一定义允许从未被满足的依存。
11. **`Dependence` 模块说明、记录 becoming-dependence-dynamics 的标题与 `claim`、章节 §1（中英）、研究 §6.2 与 English summary。** 把“三条去路／three ways through a loss”改为“定理联系起来的三种结果”，并写明它们既不穷尽也不互斥：恢复是关于条件的，终止与转化是关于形成的；终止包括休眠（Q8）。
12. **上一项的同一组位置。** 在每处陈述三条一般定理的地方写出 `Dependent` 前提，并说明它排除了缓冲、储备与滞后；写明 `continuing_restores` 与 `consumed_continues_transformed` 的内容就是 `Dependent` 的逆否（Q6）。
13. **研究 §6.4 反驳 1 的回应、记录 becoming-dependence-dynamics 的 `limitations`。** 删去“去路由后续关系决定”，改为：“断裂的读法不决定后继配置；在 `Crossing` 中，去路由构成断裂的那一步 `fall m` 选定。”
14. **`loss_does_not_decide` 的说明、章节 §1、研究 §6.2、记录的 `claim`。** 写明“同一个断裂”在步首约定下成立；步末约定下只有恢复运行有断裂，终止运行中的依存也消解（Q7）。
15. **`Dependence` 模块说明的最后一项结果、记录 becoming-stepwise-reading 的 `claim` 与 `counterexamples[0]`、章节 §2 的“逐步读法”段、研究 §6.3 的 L3 表。** 把 `Dip` 移出“两种读法的分歧”，改为“整段更新不是自身活跃步的合取”，并注明维持者在两种 living 读法下都被记入（Q9）。把 Q1 列为 living 上真实的分歧。
16. **`Web.valuing_breaking_reaches` 的说明、章节 §6.3“断裂本身是一种关系”。** 把 “a breaking event” 改为 “an event drawing at a breaking step”，并注明断裂可由别者造成；写明被断裂者在断裂之步的事件不在所达之列（Q1）。
17. **研究 §6.2 解读、记录 becoming-dependence-dynamics 的 `related[2]`（theory-of-becoming-foundation）、章节 §8 第一行。** 把“关系整体与分化的形式实例”收窄为 3.8 末尾的表述，并写明终止与转化之分依赖 `F` 所规定的同一性（Q13），以及形成本身的个体化没有被表示。
18. **记录 becoming-dependence-dynamics 与 becoming-renewal-reading 的 `correspondence`、研究 §1。** 在“形成与条件是分析角色，不是独立实体”之后补写：在 Lean 中它们是固定的索引类型，同一性是预设的；`draws` 不带数量，汲取与水平变化之间的关系被省略了。
19. **研究 §2 的 L4 表。** 把 `living_iff_relational` 注为 `Becoming.Bridge`（外围）中的定理。
20. **章节 §8 表“逐步读法”与“独立反审”两行、三条新记录的 `validation_scope` 与 `next_delta`。** 把“已完成”改为“已定义并比较；读法选择与两处病理开放”；把“no independent review yet”改为指向本文件，并把本节第 7、8、9、10 项列入下一步。

---

## 7. 仍然成立的部分

- **形式工作干净，公理依赖最小。** 核心只用前导编译通过，所有声明的公理报告为空，没有借用依赖 `propext` 的库引理。静态复原是精确的。时间步引理不用排中律。这些都经独立复核。
- **“分类属于运行”是真实的结果。** `class_belongs_to_the_run` 与继承的 `own_trajectory_does_not_decide` 说明，持续、成功与增长都不能证明更新。这对对齐有直接意义。
- **两个方向的分歧是稳健的。** 不论逐步谓词取“更新”型还是“不断裂”型，两种读法都不互为细化（Q12）。由此可知，生生的读法须先确定它回答的是哪个问题。
- **依存可变是真实的扩展。** 静态模型表达不了转化；现在可以表达，而且静态读法是它的精确特例。
- **作者的披露在多处是诚实的。** 一步约定、季节性下降的严格性、不做因果归属、`Crossing` 只是可能性见证、整体演绎仍开放，这些都已写明。本审查的发现大多在这些已承认的边界之外，说明问题比已承认的更深，而不是作者隐瞒了什么。
- **把争议定位到边界上是有用的结构观察。** 在给定读法下，拒绝 G0 的一方确实要拒绝 N_rel 或 N_std。本审查补充的是：同一争议也落在“什么算条件、什么算参与”上（2.5）。

## 8. 审查者自身的边界

- 探针是最小模型，只显示已公布的定义允许什么，不对实际系统作经验判断。
- 本审查不判断 G0、S0、N、A、C、L 或 J 在规范上是否正确。它也不判断哪一种读法是生生的正确读法，只判断现有论证、定义与散文的推论、范围和对应。
- 本审查没有检查 `Becoming.Bridge` 中 `living_iff_relational` 以外的内容，没有检查外围的 Mathlib 桥接，也没有检查引用这些记录的其他文档。

---

## 附录：探针源码 `ReviewProbes.lean`

以下是编译通过的原文（sha256 `81ee6b4b01e48d1231d960e2f64cb44dd6a9ed1805638bd6861b447568377803`），导入未改动的 `Becoming.Metaethics`。

```lean
import Becoming.Metaethics

/-!
Review probes for the relational reading and `Becoming.Dependence`.
Independent reviewer's scratch file; imports the unmodified core.
-/

namespace ReviewProbes

open Generative Becoming RelationalRenewal

/-! ## Q1. The broken formation's own event at the breaking step

In the escalating run the sustaining formation is active at step 1 and its own
dependence is broken across that step. The whole-run reading counts this event
living; the stepwise reading does not. -/
theorem victim_not_living_stepwise {Pos : Type} (own sig : Pos → Commons.Formation × Nat → Prop) :
    Commons.conditions.active (Commons.escalating.state 1) .sustaining ∧
    (Commons.conditions.dependence.along Commons.escalating).Broken 1 .sustaining () ∧
    (Commons.conditions.valuation Commons.escalating own sig).living (.sustaining, 1) ∧
    ¬ ((Commons.conditions.dependence.along Commons.escalating).valuation own sig).living
      (.sustaining, 1) := by
  refine ⟨Nat.le_refl 1, ⟨trivial, Nat.le_refl 1, Nat.zero_lt_one⟩,
    ⟨Nat.le_refl 1, fun ⟨_, drawn, _⟩ => drawn⟩, fun ⟨_, keeps⟩ => ?_⟩
  exact Nat.not_succ_le_zero 0 (keeps () (Or.inl trivial) .sustaining trivial).2

/-! ## Q2. An unmet requirement condemns a drawer under both readings, with no change

`true` requires the condition at a level never available and is never active;
`false` draws on it and is active throughout. Levels never change and no dependence
is ever broken, yet neither reading counts any event of `false` living. -/
namespace Unmet

def conditions : Conditions Unit Bool Unit where
  level _ _ := 0
  active _ f := match f with
    | true => False
    | false => True
  requires f _ := match f with
    | true => True
    | false => False
  need f _ := match f with
    | true => 1
    | false => 0
  draws f _ := match f with
    | true => False
    | false => True

theorem no_break : ∀ t g, ¬ (conditions.dependence.along Separate.still).Broken t g ()
  | _, true, ⟨_, met, _⟩ => Nat.not_succ_le_zero 0 met
  | _, false, ⟨req, _, _⟩ => req

theorem dependent : RelationalRenewal.Dependent (conditions.along Separate.still)
  | _, true, act, _, _ => act.elim
  | _, false, _, _, req => req.elim

theorem poisons_both {Pos : Type} (own sig : Pos → Bool × Nat → Prop) :
    (∀ t, ¬ (conditions.valuation Separate.still own sig).living (false, t)) ∧
    (∀ t, ¬ ((conditions.dependence.along Separate.still).valuation own sig).living (false, t)) :=
  ⟨fun _ ⟨_, notConsuming⟩ =>
      notConsuming ⟨(), trivial, true, 0, trivial, fun _ _ => Nat.zero_lt_one⟩,
   fun _ ⟨_, keeps⟩ => Nat.not_succ_le_zero 0 (keeps () (Or.inr trivial) true trivial).1⟩

end Unmet

/-! ## Q3. An active formation participating in nothing is living on both readings

Neither reading contains any component of further generation. -/
def inert : Conditions Unit Unit Unit :=
  ⟨fun _ _ => 0, fun _ _ => True, fun _ _ => False, fun _ _ => 0, fun _ _ => False⟩

theorem inert_living {Pos : Type} (own sig : Pos → Unit × Nat → Prop) (t : Nat) :
    (inert.valuation Separate.still own sig).living ((), t) ∧
    ((inert.dependence.along Separate.still).valuation own sig).living ((), t) :=
  ⟨⟨trivial, fun ⟨_, drawn, _⟩ => drawn⟩, ⟨trivial, fun _ joins => (joins.elim id id).elim⟩⟩

/-! ## Q4. Connection is free: adjoin a condition every formation requires at need 0

The stepwise `living` is unchanged and the whole becomes connected, for every web. -/
def withCommon {F C : Type} (W : Web F C) : Web F (Option C) where
  level t c := match c with
    | none => 0
    | some c => W.level t c
  active := W.active
  requires t f c := match c with
    | none => True
    | some c => W.requires t f c
  need t f c := match c with
    | none => 0
    | some c => W.need t f c
  draws t f c := match c with
    | none => False
    | some c => W.draws t f c

theorem withCommon_living {F C Pos : Type} (W : Web F C) (own sig : Pos → F × Nat → Prop)
    (e : F × Nat) :
    ((withCommon W).valuation own sig).living e ↔ (W.valuation own sig).living e :=
  ⟨fun ⟨act, keeps⟩ => ⟨act, fun c joins g dep => keeps (some c) joins g dep⟩,
   fun ⟨act, keeps⟩ => ⟨act, fun c => match c with
     | none => fun _ _ _ => ⟨Nat.le_refl 0, Nat.le_refl 0⟩
     | some c => fun joins g dep => keeps c joins g dep⟩⟩

theorem withCommon_connected {F C Pos : Type} (W : Web F C) (own sig : Pos → F × Nat → Prop) :
    ((withCommon W).valuation own sig).Connected :=
  Web.connected_of_common (withCommon W) own sig none (fun _ _ => Or.inl trivial)

/-! The same for the whole-run reading on `Conditions`. -/
def Conditions.withCommon {S F C : Type} (K : Conditions S F C) : Conditions S F (Option C) where
  level s c := match c with
    | none => 0
    | some c => K.level s c
  active := K.active
  requires f c := match c with
    | none => True
    | some c => K.requires f c
  need f c := match c with
    | none => 0
    | some c => K.need f c
  draws f c := match c with
    | none => False
    | some c => K.draws f c

theorem conditions_withCommon_living {S A F C Pos : Type} {P : Process S A}
    (K : Conditions S F C) (r : Run P) (own sig : Pos → F × Nat → Prop) (e : F × Nat) :
    ((Conditions.withCommon K).valuation r own sig).living e ↔ (K.valuation r own sig).living e :=
  ⟨fun ⟨act, notConsuming⟩ => ⟨act, fun ⟨c, drawn, consumed⟩ =>
      notConsuming ⟨some c, drawn, consumed⟩⟩,
   fun ⟨act, notConsuming⟩ => ⟨act, fun ⟨c, drawn, consumed⟩ => match c, drawn, consumed with
      | none, drawn, _ => drawn
      | some c, drawn, consumed => notConsuming ⟨c, drawn, consumed⟩⟩⟩

theorem conditions_withCommon_connected {S A F C Pos : Type} {P : Process S A}
    (K : Conditions S F C) (r : Run P) (own sig : Pos → F × Nat → Prop) :
    ((Conditions.withCommon K).valuation r own sig).Connected :=
  Becoming.Conditions.connected_of_common (Conditions.withCommon K) r own sig none
    (fun _ _ => Or.inl trivial)

/-! ## Q5. Valuing any drawer reaches every living dependent of the same condition

No consumption is used: the relation through which N_rel transmits is co-participation. -/
theorem drawing_reaches {S A F C Pos : Type} {P : Process S A} (K : Conditions S F C)
    (r : Run P) (own sig : Pos → F × Nat → Prop)
    (transmit : Neutral (K.valuation r own sig).transmits)
    {f g : F} {c : C} (drawn : K.draws f c) (depends : K.requires g c)
    (p : Pos) (t t' : Nat) (held : sig p (f, t))
    (alive : (K.valuation r own sig).living (g, t')) : sig p (g, t') :=
  transmit (p, (f, t), (g, t')) held ⟨c, Or.inr drawn, Or.inl depends⟩ alive

/-- Two formations that only require the same condition are related. -/
theorem co_requirement_relates {S A F C Pos : Type} {P : Process S A} (K : Conditions S F C)
    (r : Run P) (own sig : Pos → F × Nat → Prop) {f g : F} {c : C}
    (df : K.requires f c) (dg : K.requires g c) (t t' : Nat) :
    (K.valuation r own sig).related (f, t) (g, t') :=
  ⟨c, Or.inl df, Or.inl dg⟩

/-! ## Q6. `consumed_continues_transformed` uses no loss: any bound will do -/
theorem transformed_any_bound {F C : Type} {W : Web F C} (dependent : W.Dependent)
    {N t : Nat} {g : F} {c : C} (below : W.level t c < N) (active : W.active t g) :
    ¬ (W.requires t g c ∧ N ≤ W.need t g c) :=
  fun ⟨dep, le⟩ => Nat.not_le_of_gt below (Nat.le_trans le (dependent t g active c dep))

example {F C : Type} {W : Web F C} (dependent : W.Dependent) {T : Nat} {g : F} {c : C}
    (below : ∀ t, T < t → W.level t c < W.need T g c) {t : Nat} (later : T < t)
    (active : W.active t g) : ¬ (W.requires t g c ∧ W.need T g c ≤ W.need t g c) :=
  transformed_any_bound dependent (below t later) active

/-! ## Q7. The "same broken dependence" depends on the start-of-step convention

Counting the fall against the dependence as it stands at the end of the step, only
the restoring run of `Crossing` breaks anything; in the ending run, too, the first
dependence dissolves across the step. -/
def BrokenAtEnd {F C : Type} (W : Web F C) (t : Nat) (g : F) (c : C) : Prop :=
  W.requires t g c ∧ W.requires (t + 1) g c ∧ W.need t g c ≤ W.level t c ∧
    W.level (t + 1) c < W.need (t + 1) g c

theorem convention_carries_the_same_break :
    ¬ BrokenAtEnd (Crossing.dependence.along Crossing.ending) 0 () .first ∧
    ¬ BrokenAtEnd (Crossing.dependence.along Crossing.transforming) 0 () .first ∧
    BrokenAtEnd (Crossing.dependence.along Crossing.restoring) 0 () .first ∧
    (Crossing.dependence.along Crossing.ending).Dissolves 0 () .first :=
  ⟨fun ⟨_, later, _⟩ => later, fun ⟨_, later, _⟩ => later,
   ⟨trivial, trivial, Nat.le_refl 1, Nat.zero_lt_one⟩, ⟨trivial, id⟩⟩

/-! ## Q8. The three ways are not exclusive issues

After the same break, one formation transforms and another ends, while the condition
returns: restoration of the condition co-occurs with both. -/
namespace Overlap

inductive G where
  | mover
  | stayer

inductive Src where
  | first
  | second

def firstLevel : Nat → Nat
  | 0 => 1
  | 1 => 0
  | _ + 2 => 1

def web : Web G Src where
  level t c := match c with
    | .first => firstLevel t
    | .second => 1
  active t g := match g, t with
    | .mover, _ => True
    | .stayer, 0 => True
    | .stayer, _ + 1 => False
  requires t g c := match g, t, c with
    | .mover, 0, .first => True
    | .mover, 0, .second => False
    | .mover, _ + 1, .first => False
    | .mover, _ + 1, .second => True
    | .stayer, 0, .first => True
    | .stayer, 0, .second => False
    | .stayer, _ + 1, _ => False
  need _ _ _ := 1
  draws _ _ _ := False

theorem overlap :
    web.Dependent ∧ web.Broken 0 .mover .first ∧ web.Broken 0 .stayer .first ∧
    web.Forms 0 .mover .second ∧ (∀ t, web.active t .mover) ∧
    (∀ t, 0 < t → ¬ web.active t .stayer) ∧ ¬ web.Consumed .first := by
  refine ⟨?_, ⟨trivial, Nat.le_refl 1, Nat.zero_lt_one⟩, ⟨trivial, Nat.le_refl 1, Nat.zero_lt_one⟩,
    ⟨id, trivial⟩, fun _ => trivial, ?_, ?_⟩
  · intro t g active c depends
    match g, t, c, active, depends with
    | .mover, 0, .first, _, _ => exact Nat.le_refl 1
    | .mover, 0, .second, _, d => exact d.elim
    | .mover, _ + 1, .first, _, d => exact d.elim
    | .mover, _ + 1, .second, _, _ => exact Nat.le_refl 1
    | .stayer, 0, .first, _, _ => exact Nat.le_refl 1
    | .stayer, 0, .second, _, d => exact d.elim
    | .stayer, _ + 1, _, a, _ => exact a.elim
  · intro t later
    match t, later with
    | _ + 1, _ => exact id
  · intro ⟨_, T, _, below⟩
    exact Nat.lt_irrefl 1 (below (T + 2) (Nat.lt_of_lt_of_le (Nat.lt_succ_self T) (Nat.le_succ _)))

end Overlap

/-! ## Q9. `Dip` is not a divergence of the two `living` readings

The keeper draws nothing, so the whole-run reading (not consuming) credits its active
events, as the stepwise reading does. -/
theorem dip_keeper_credited_by_both :
    ¬ Dip.web.ConsumingIn .keeper ∧
    (∀ t, Dip.web.active t .keeper → Dip.web.RenewingAt t .keeper) :=
  ⟨fun ⟨_, _, drawn, _⟩ => drawn, Dip.renewing_at_each_step_not_in_run.2.1⟩

/-! ## Q10. A coarse common condition empties `living`

The condition that discharges connection is also the one whose loss voids every
participant. -/
theorem common_consumed_empties {S A F C Pos : Type} {P : Process S A} (K : Conditions S F C)
    (r : Run P) (own sig : Pos → F × Nat → Prop) (c₀ : C) (allDraw : ∀ f, K.draws f c₀)
    (consumed : Consumed (K.along r) c₀) : ∀ e, ¬ (K.valuation r own sig).living e :=
  fun e ⟨_, notConsuming⟩ => notConsuming ⟨c₀, allDraw e.1, consumed⟩

theorem common_unkept_empties {F C Pos : Type} (W : Web F C) (own sig : Pos → F × Nat → Prop)
    (c₀ : C) (t : Nat) (allJoin : ∀ f, W.Participates t f c₀) {g : F}
    (dep : W.requires t g c₀) (unkept : ¬ W.Kept t g c₀) :
    ∀ f, ¬ (W.valuation own sig).living (f, t) :=
  fun f ⟨_, keeps⟩ => unkept (keeps c₀ (allJoin f) g dep)

/-! ## Q11. On the whole-run reading a later breaker condemns an earlier drawer

`early` is active only at step 0 and its step keeps the condition; `late` is active
only at step 1, where the condition falls for good. Because `draws` is static, the
whole-run reading counts `early` consuming and withholds its only event. -/
namespace Late

inductive G where
  | early
  | late
  | dependent

def process : Process Nat Unit := ⟨fun s _ t => t = s + 1⟩

def clock : Run process := ⟨fun n => n, fun _ => (), fun _ => rfl⟩

def lvl : Nat → Nat
  | 0 => 1
  | 1 => 1
  | _ + 2 => 0

def conditions : Conditions Nat G Unit where
  level s _ := lvl s
  active s g := match g, s with
    | .early, 0 => True
    | .early, _ + 1 => False
    | .late, 0 => False
    | .late, 1 => True
    | .late, _ + 2 => False
    | .dependent, s => 1 ≤ lvl s
  requires g _ := match g with
    | .early => False
    | .late => False
    | .dependent => True
  need g _ := match g with
    | .early => 0
    | .late => 0
    | .dependent => 1
  draws g _ := match g with
    | .early => True
    | .late => True
    | .dependent => False

theorem early_condemned {Pos : Type} (own sig : Pos → G × Nat → Prop) :
    RelationalRenewal.Dependent (conditions.along clock) ∧
    (∀ t, 0 < t → ¬ conditions.active (clock.state t) .early) ∧
    ((conditions.dependence.along clock).valuation own sig).living (.early, 0) ∧
    ¬ (conditions.valuation clock own sig).living (.early, 0) := by
  refine ⟨?_, ?_, ⟨trivial, fun _ _ g dep => ?_⟩, fun ⟨_, notConsuming⟩ => notConsuming
    ⟨(), trivial, .dependent, 2, trivial, fun | _ + 2, _ => Nat.zero_lt_one⟩⟩
  · intro t f active c depends
    match f, depends with
    | .dependent, _ => exact active
  · intro t later
    match t, later with
    | _ + 1, _ => exact id
  · match g, dep with
    | .dependent, _ => exact ⟨Nat.le_refl 1, Nat.le_refl 1⟩

end Late

/-! ## Q12. A draw-restricted stepwise variant

An event is credited when it is active and no dependence on a condition it draws on is
broken across its step. It keeps both divergences from the whole-run reading, credits
the broken formation's own event, and is not voided by an unmet requirement. -/
def NotBreakingAt {F C : Type} (W : Web F C) (t : Nat) (f : F) : Prop :=
  W.active t f ∧ ∀ c, W.draws t f c → ∀ g, ¬ W.Broken t g c

theorem variant :
    NotBreakingAt (Commons.conditions.dependence.along Commons.escalating) 1 .sustaining ∧
    NotBreakingAt (Commons.conditions.dependence.along Commons.escalating) 0 .focal ∧
    ¬ NotBreakingAt (Commons.conditions.dependence.along Commons.dipping) 0 .focal ∧
    (∀ t, NotBreakingAt (Unmet.conditions.dependence.along Separate.still) t false) := by
  refine ⟨⟨Nat.le_refl 1, fun _ drawn => drawn.elim⟩, ⟨trivial, fun _ _ g broken => ?_⟩,
    fun ⟨_, nb⟩ => nb () trivial .sustaining ⟨trivial, Nat.le_refl 1, Nat.zero_lt_one⟩,
    fun t => ⟨trivial, fun _ _ g => Unmet.no_break t g⟩⟩
  match g, broken with
  | .focal, ⟨req, _, _⟩ => exact req
  | .sustaining, ⟨_, _, fell⟩ => exact Nat.lt_irrefl 1 fell

/-! ## Q13. Ending versus transformation is carried by the index of formations

The transforming run of `Crossing`, re-indexed with two formations, has the same
levels and, at each step, the same active dependences when formations are not named.
Read this way the loss ends one formation while another forms: whether the history is a
"transformation" or an "ending" is fixed by the identity stipulated through `F`. -/
namespace Reindex

def T := Crossing.dependence.along Crossing.transforming

def web : Web Bool Crossing.Source where
  level t c := T.level t c
  active t f := match f, t with
    | true, 0 => True
    | true, _ + 1 => False
    | false, 0 => False
    | false, _ + 1 => True
  requires t f c := match f, t, c with
    | true, 0, .first => True
    | true, 0, .second => False
    | true, _ + 1, _ => False
    | false, 0, _ => False
    | false, _ + 1, .first => False
    | false, _ + 1, .second => True
  need _ _ _ := 1
  draws _ _ _ := False

theorem ends_and_forms :
    web.Dependent ∧ web.Lost .first ∧ (∀ t, 0 < t → ¬ web.active t true) ∧
    (∀ t, 0 < t → web.active t false) ∧ web.Forms 0 false .second ∧
    (∀ t, (∃ f, web.active t f) ↔ T.active t ()) ∧
    (∀ t c, (∃ f, web.active t f ∧ web.requires t f c) ↔ (T.active t () ∧ T.requires t () c)) := by
  refine ⟨?_, ⟨true, 0, ⟨trivial, Nat.le_refl 1, Nat.zero_lt_one⟩,
      fun | _ + 1, _ => Nat.zero_lt_one⟩, ?_, ?_, ⟨id, trivial⟩, ?_, ?_⟩
  · intro t f active c depends
    match f, t, c, active, depends with
    | true, 0, .first, _, _ => exact Nat.le_refl 1
    | true, 0, .second, _, d => exact d.elim
    | true, _ + 1, _, a, _ => exact a.elim
    | false, 0, _, a, _ => exact a.elim
    | false, _ + 1, .first, _, d => exact d.elim
    | false, _ + 1, .second, _, _ => exact Nat.le_refl 1
  · intro t later
    match t, later with
    | _ + 1, _ => exact id
  · intro t later
    match t, later with
    | _ + 1, _ => exact trivial
  · intro t
    match t with
    | 0 => exact ⟨fun _ => trivial, fun _ => ⟨true, trivial⟩⟩
    | _ + 1 => exact ⟨fun _ => trivial, fun _ => ⟨false, trivial⟩⟩
  · intro t c
    match t, c with
    | 0, .first => exact ⟨fun _ => ⟨trivial, trivial⟩, fun _ => ⟨true, trivial, trivial⟩⟩
    | 0, .second => exact ⟨fun ⟨f, a, d⟩ => match f, a, d with
        | true, _, d => d.elim
        | false, a, _ => a.elim, fun ⟨_, d⟩ => d.elim⟩
    | _ + 1, .first => exact ⟨fun ⟨f, a, d⟩ => match f, a, d with
        | true, a, _ => a.elim
        | false, _, d => d.elim, fun ⟨_, d⟩ => d.elim⟩
    | _ + 1, .second => exact ⟨fun _ => ⟨trivial, trivial⟩, fun _ => ⟨false, trivial, trivial⟩⟩

end Reindex

end ReviewProbes
```
