# 伦理自然主义的四条论证：生成论的对应、证明与未完成部分

2026年10月6日。AI 撰写的研究说明，回应 [Ren 关于四条自然主义论证"都可以最终证明"的消息](../../../../sources/15-codex-theory-conversations/2026-10-06-ethical-naturalism-arguments.md)。遵循[非二元方法](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md)：评价、更新和纠正都作为展开内部的活动处理，不设外部裁判位置。形式部分在新的 [Lean 包](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/naturalism/README.md)中，43 条声明全部审计，39 条不依赖任何公理，其余只依赖 Lean 标准的 `propext` 与 `Quot.sound`；无 `sorry`、无自定义公理，继承模块的源码哈希与主收据一致。本文不是 Ren 原话，也不宣称伦理结论已经证明。

## 0. 结论

1. **四条论证的可形式化部分，生成论都能证明，本轮已证明。** 证明的内容是：如果有道德属性，它可以是生成历史的自然属性。它随附于历史，由过程本身定义，可以通过有限证据认识，并在跨实现的解释中起作用。
2. **生成论使随附性更强、更具体。** 随附基础必须是**整段历史**，包括中间状态；终点加动作序列不够。这正是 Ren 所说"整体的积分"在随附性问题上的形式内容。
3. **但四条论证对"等同于哪一个自然属性"是中立的。** 本轮严格证明：相反取向（以损失为上）同样满足全部这些条件，而且对同一次实际转换作出相反判断。所以单靠这四条，不能推出"善 = 整体展开生成其后续条件"。这就是开放问题论证和是/应当问题在本理论中的准确位置。
4. **再加一项自反前提，就可以选出这个属性。** 评价、更新和纠正本身是展开中的活动；若不预先特权化任何活动（包括评价者自己的），一个取向就不得取消任何活动的可实现性。在这个前提下，可接受的取向**恰好**是延续条件序的子关系（定理）。功利主义的标量排序、Railton 的单一中心范围、Foot 的固定生命形式范围，都在有限例子中违反这个前提。
5. **这项前提本身未证明，而且按现在的写法已有反例。** 把所有活动同等计入时，阻止伤害与伤害本身一样被记为条件损失，保留伤害的可能则不算损失（`restraint_registers_as_damage`）。所以它还不能直接充当伦理同一的最终表述。下一座桥是：从生成关系本身导出受保护活动的范围，区分维持他者条件的活动与取消他者条件的活动。这与项目记录一致：整体质量与伦理根据的无假设普遍证明尚未完成。

下表按 Ren 列出的四条依次给出对应关系。

| 论证 | 生成论的对应 | 已有结果 | 本轮新证 | 仍属哲学 |
|---|---|---|---|---|
| 随附性（Jackson） | 整体质量随附于整段生成历史 | 中途下降不能由终点摘要恢复（[一体之仁 §7](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONINSTRUMENTAL-CONCERN.md#7-形式化怎样保存同一历程)）；整体评价先于时间表达（[FUTURE-GOOD-INTEGRAL §7](FUTURE-GOOD-INTEGRAL.md#7-whole-appraisal-can-precede-its-temporal-expression)） | 随附 ⇔ 经基础同一类分解；质量随附于访问状态序列，不随附于终点与动作序列；可组合、可迁移 | 从必然共外延到属性同一；"必然"的模态范围 |
| 本体论简约（Mackie） | 质量由过程本身定义，不另立一层 | 核心语义只有可行转换（`GenerativeCore`） | 质量在精确重表示下不变 | 规范的"应被追求性"未被消解，只被归约为自反前提 |
| 认识论 | 损失有有限见证，必定落在实际转换上 | 询问何时有用（`InquiryWarrant`）；估值经共同经历形成，正负皆可（[估值发展](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/VALUATION-DEVELOPMENT.md)）；完全对称的起点不能由记录决定（[记录与竞争要求](RECORDED-CLAIMS-INTEGRATION.md)） | 有限见证否定保全；损失定位（可判定时构造性，一般情形双重否定）；只看终点不能认识 | 反思平衡是否收敛；直觉的证据地位 |
| 解释作用（康奈尔） | 整体质量解释"某活动始终可实现"，且对任意过程成立 | 每类组织带来的少于其形成所需时，无论支持关系如何，更新必在期限内结束（`short_kinds_cannot_renew_forever`） | 无损历史保全一切初始可实现活动；被解释事实不由较粗描述决定 | 解释作用证明属性真实，不证明它就是善 |

## 1. 随附性与 Jackson 的论证

**形式对应。** `Supervenes M N` 指：基础 `N` 相同则 `M` 相同。`supervenes_iff_factors` 证明：`M` 随附于 `N`，当且仅当 `M` 是 `N` 的同一类（商）上的函数。这正是 Jackson 第二步的形式内容：全局随附给出一个由基础定义、与道德属性在一切情形中共外延的性质。这里的"一切情形"是所讨论的历史全体；跨过程的必然性是范围声明，不是额外定理。

**生成论使基础更具体。** `Run` 把历史作为数据保存，包括每个中间状态。`Along R r` 表示关系 `R` 在 `r` 的每一次实际转换上成立。取 `R` 为延续条件序 `ContinuationLe`（后一状态能实现前一状态能实现的一切有限活动），`Along` 就是"整段展开没有取消任何活动的可实现性"。

- `along_supervenes_on_states`：任意步质量都是访问状态序列的函数。
- `quality_not_fixed_by_endpoints_and_word`、`quality_not_supervenient_on_word`：在 `dip` 过程中，两段历史起点、终点和动作序列完全相同，一段中途取消了 `use` 的可实现性，另一段没有。所以整体质量**不**随附于终点加动作序列，而随附于整段历史。
- 对 McDowell"无形状"反驳的回应：Jackson 的对应自然属性可能只是一个无限析取，没有自然统一性。本轮证明这个质量有结构：经共享边界状态可组合（`along_append`），在精确重表示下不变（`along_continuation_transport`），损失可定位（第4节）。

**未证部分。** 必然共外延是否等于属性同一，取决于属性的个体化方式。超内涵立场下，这一步不成立，也不是形式定理能决定的。本文把 Jackson 的结论读作"道德属性至少与一个结构化的自然属性必然共外延"，这一部分已证。

## 2. 本体论简约与 Mackie

质量 `Along (ContinuationLe P)` 只用过程 `P` 本身定义，不引入新的实体或层次。它在精确重表示下保持不变，所以不依赖观察者选择的描述方式。Mackie 怪异性论证的形而上部分在这个意义上被回应：所需的只是已有世界中的生成关系。

Mackie 还有两部分没有被消解。第一，**规范的"应被追求性"**：知道某段历史保全条件，并不使任何人必须追求它。本轮把这一点精确地移到自反前提上（第5节），而不是宣称它消失了。第二，**相对性论证**：第5节的取向中立定理说明，自然事实允许融贯的相反取向，所以分歧未必出于事实错误。这一点对 Mackie 有利，应当保留。

## 3. 认识论

- **损失有有限见证。** 一个活动在前一状态可实现、在后一状态不可实现，这一个有限事实就否定了保全（`witness_refutes_preservation`）。损害可以观察，也可以证伪。
- **保全是全称命题。** 它涉及一切活动，只能得到可错的支持。这种不对称与经验科学中的普遍命题相同。
- **损失必定发生在实际转换上。** 若活动的可实现性可判定（例如有限过程），起点可实现、终点不可实现的活动一定在历史中的某一次实际转换上失去（`loss_localizes`）。不假定可判定性时，"没有任何转换承担这次损失"也不可能成立（`loss_localizes_nn`）。所以认识整体质量可以靠逐步记录，不需要外部视角。
- **只看终点不能认识。** `dip` 的两段历史终点相同。认识需要历史记录，这与[一体之仁 §7](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONINSTRUMENTAL-CONCERN.md#7-形式化怎样保存同一历程)的中途下降结果一致。

**复用的已有结果。** 自然主义说"像认识其他事物一样认识道德事实"。生成论的对应是：评价本身在展开中形成。[估值发展](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/VALUATION-DEVELOPMENT.md)证明，对他者后果的看重经共同经历形成，好的共同事件形成正联结，坏的形成负联结。所以经验形成的评价需要纠正，这正是反思平衡在生成论中的位置。[延续范围](CONTINUATION-SCOPE-INTEGRATION.md)证明，评估若漏掉实际触及的延续，会在两个方向上失真。[记录与竞争要求](RECORDED-CLAIMS-INTEGRATION.md)证明，完全对称的起点不能由记录决定，这是经验认识的一个精确界限。

**未证部分。** 反思平衡是否收敛、直觉在其中算作什么证据，是哲学问题，也是今后可以做经验研究的问题。

## 4. 解释作用与康奈尔实在论

**解释的定律对一切过程成立。** `preserved_throughout` 说：在任意过程中，一段无损历史使起点可实现的每个活动在每个访问状态都保持可实现。被解释的事实是"某活动在整段历程中始终可实现"。`availability_not_fixed_by_endpoints_and_word` 说明这个事实不由终点和动作序列决定：较粗的自然描述承担不了这项解释，整体历史质量可以。这个定律对任意过程成立，正是 Boyd 强调的多重实现。

**已有的更新定律。** [`RenewalAccounting`](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/README.md) 的 `short_kinds_cannot_renew_forever` 证明：当每类组织带来的少于其形成所需，**无论支持关系如何**，更新都必在明确期限内结束。这是一条"展开损害自身后续条件"解释终结的定律，同样跨实现成立。这里只引用，不重复证明。

**对 Harman 挑战的回应及其限度。** 若道德属性与这个自然属性同一，它的解释就是自然解释，不与物理解释竞争。但解释作用证明的是这个自然属性真实且有解释力。相反取向同样有解释作用（第5节）。所以解释作用不能单独证明这个属性就是善。

## 5. 等同于哪一个自然属性

**候选。** 整体展开对其自身后续实现、更新与纠正条件的生成或损害。形式上，它是沿整段历史的延续条件序 `Along (ContinuationLe P)`，连同其可组合、定位与不可比的结构。

### 5.1 开放问题与是/应当：严格的中立结果

`naturalist_criteria_do_not_fix_orientation` 证明：延续条件序及其逆序都是预序，都随附于访问状态，都可组合，在精确重表示下都不变（`converse_projection_iff`）。但对 `dipped` 中从 2 到 1 的实际转换，一个判为损失，另一个判为可接受。这强化了已有的 `EthicalOrientation.coherence_and_annotation_invariance_do_not_select_growth`。

这是 Moore 开放问题论证在本理论中的准确形式，也是 Horgan 与 Timmons"道德孪生地球"的形式版本：两个共同体可以用同样的实践角色使用"善"，却追踪相反的自然属性。结论是：若同一成立，它是综合的、后验的（康奈尔实在论本来就这样主张，如"水 = H₂O"），由一项额外前提承担，而不是从中性事实中读出。

### 5.2 自反前提与最大可接受取向

**前提（非削弱）。** 若沿取向 `R` 前进时从不取消范围 `W` 中任一活动的可实现性，就说 `R` 对 `W` 非削弱。

**为什么取全范围。** 评价、更新和纠正本身是展开中的活动。依非二元方法，没有站在展开之外的评价者，也没有哪个中心的活动可以预先特权化。`unprivileged_scope_is_whole_scope` 证明：对每一个单独活动都非削弱，恰好等于对全部活动非削弱。

**定理。** `generation_order_greatest` 证明：延续条件序本身非削弱，而任何非削弱的取向都包含在它之中。`guided_history_preserves` 证明：按非削弱取向前进的历史，使评价者自己的活动在内，所有初始可实现的活动始终可实现。`converse_undermines_in_dip` 证明：逆序取向会取消评价与纠正赖以进行的活动。在这个前提下，孪生地球的对称被打破。

**前提的地位。** 这是一项自反论证，形式上类似先验论证：一个取向若允许取消自身被行使和被修正的条件，就削弱了它自己。但这不是从中性事实推出的。不在乎自身能否继续、能否被纠正的评价者，可以融贯地拒绝它。项目记录中"无假设普遍证明未完成"的位置，现在精确地落在这项前提上。

### 5.3 与三种候选的比较

- **功利主义（福祉或快乐）。** 任何完备排序，特别是任何标量福祉排序，在 `incomparable` 过程中都会取消某个可实现活动（`total_orders_undermine`、`scalar_ranking_undermines`）。延续条件序则让这一对保持不可比（`generation_leaves_pair_unranked`）。这是完备性与非削弱之间的取舍，不是对功利主义的反驳：功利主义者可以接受某些损失值得。代价在本候选一边同样存在：它在悲剧性选择上不给出裁决。另外，[FUTURE-GOOD-INTEGRAL §7](FUTURE-GOOD-INTEGRAL.md#7-whole-appraisal-can-precede-its-temporal-expression) 已证明任何整体评价都有逐时表达，所以差别不在于是否可以按时间相加，而在于评价追踪的是什么。痛苦确实损害后续条件；福祉可以是本候选的重要组成部分，但不是它的定义。
- **Railton（理想化的自身利益）。** 自身利益以一个中心为范围。`fixed_scope_permits_loss` 证明：对预先固定的范围非削弱的取向，可以取消范围外的活动。这与对齐线程的 `ContinuationScope.omitted_scope_admits_needless_foreclosure` 和 `InquiryWarrant.self_scoped_rule_ignores_others` 是同一结构的两层表达。Railton 的道德正确性取社会视角，比他的个人善更接近本候选；他的理想化（完全知情的反事实视角）在生成论中本身是在展开中形成的能力，不能预先给出。
- **Foot（自然的善，生命形式）。** 这是最接近的近亲：好坏按生命继续的条件判断。区别在于，Foot 预先固定物种的生命形式；在生成论中，形式本身在形成和改变，范围也跨越物种。同一个 `fixed_scope_permits_loss` 适用：只保护既定形式所列的活动，可以取消新形成的活动。这对应 Ren 的研究中心："不可预先固定任何预期作为价值单位。"

### 5.4 保留的反例：阻止伤害被记为损害

`restraint_registers_as_damage`：一个中心的活动 `live` 会被 `harm` 取消，`restrain` 取消 `harm` 的可能。按全部活动同等计入的延续条件序，阻止伤害（到 `restrained`）与伤害本身（到 `harmed`）都是条件损失，而保留伤害的可能不算损失。

所以第 5.2 节的前提若按字面理解为"任何活动都不得取消"，就会谴责正当的阻止。这不是形式细节，而是伦理上的实质缺陷。它说明：

- 全范围非削弱还不能直接充当伦理同一；
- 下一步要从生成关系本身导出**受保护活动的范围**，区分维持他者条件的活动与取消他者条件的活动；一个自然的候选是"其行使本身不取消其他受保护活动"这一条件的最大不动点；
- 这项导出必须避免把"正当活动"预先写进范围参数，否则就是循环。

## 6. 对 Ren 的判断："以上我们都可以最终证明"

- **随附性、简约、认识论、解释作用：** 它们的形式内容本轮已证明，而且生成论版本更强（基础是整段历史，解释跨实现成立）。
- **等同于哪种自然属性：** 在明示的自反前提下，已证明延续条件序是唯一的最大可接受取向，并在有限例子中把三种候选区分开。
- **未完成的部分有三项，都有精确位置：**
  1. 从必然共外延到属性同一（属性个体化的哲学问题）；
  2. 自反前提的地位（规范输入，不是中性事实的推论）；
  3. 受保护活动范围的导出（第 5.4 节的反例要求修正）。
  第3项是可以继续用数学推进的下一座桥，第1、2项需要哲学论证。

**会改变本结论的结果：** 若能从生成关系导出受保护范围，且该范围能区分阻止与伤害而不预设伦理参数，第 5.4 节的反例就被消除。若能证明任何不预设伦理参数的范围都无法区分二者，则本候选需要放弃"非削弱"作为同一标准的核心。

## 形式索引

`WholeQualityNaturalism.lean`：`supervenes_iff_factors`、`base_defined_supervenes`、`supervenes_of_finer`、`Run`、`Along`、`along_iff_steps`、`along_iff_chain`、`along_supervenes_on_states`、`along_append`、`along_mono`、`chain_map`、`along_continuation_transport`、`preserved_throughout`、`witness_refutes_preservation`、`loss_localizes`、`loss_localizes_nn`、`located_loss_breaks_quality`、`quality_not_fixed_by_endpoints_and_word`、`quality_not_supervenient_on_word`、`availability_not_fixed_by_endpoints_and_word`。

`NaturalismIdentity.lean`：`converse_projection_iff`、`dip_two_dominates_one`、`naturalist_criteria_do_not_fix_orientation`、`NonUndermining`、`nonUndermining_whole_iff`、`generation_order_greatest`、`unprivileged_scope_is_whole_scope`、`guided_history_preserves`、`converse_undermines_in_dip`、`fixed_scope_permits_loss`、`generation_leaves_pair_unranked`、`total_orders_undermine`、`scalar_ranking_undermines`、`restraint_registers_as_damage`。

所有过程、范围与排序都是给定的局部模型输入。没有定理断言哪段历史会发生、前提为真，或在每个选项都有所取消时应如何选择。本轮未经独立 AI 审查。
