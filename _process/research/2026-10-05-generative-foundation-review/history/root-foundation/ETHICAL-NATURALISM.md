# 伦理自然主义的四条论证：生成论的对应、证明与未完成部分

**7 October continuation:** [Actual recovery and its retained interruption](ETHICAL-NATURALISM-ACTUAL-RECOVERY.md) now resolve the proposed immediate/eventual representation bridge. Twenty-one new axiom-free results retain actual restoration and show why eventual possibilities alone omit the interruption. The [merged integration](MERGED-OBLIGATIONS-INTEGRATION.md) also puts a contact profile and native support on the same actual port run. Neither result derives protected scope or universal ethical warrant; older package counts below describe their respective stages.

2026年10月6日。AI 撰写的研究说明，回应 [Ren 关于四条自然主义论证"都可以最终证明"的消息](../../../../sources/15-codex-theory-conversations/2026-10-06-ethical-naturalism-arguments.md)。遵循[非二元方法](../../../../theories/becoming/chapters/NONDUAL-METHOD.md)：评价、更新和纠正都作为展开内部的活动处理，不设外部裁判位置。形式部分在 [Lean 包](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/naturalism/README.md)中。按 Ren 的无公理规则改写后，整个包 120 条新声明全部审计，**全部不依赖任何公理**（包括 Lean 标准的 `propext` 与 `Quot.sound`）；无 `sorry`，继承模块的源码哈希与主收据一致。改写前的源码与收据保存在包内的 `verification-history/2026-10-06-before-axiom-removal/`。本文不是 Ren 原话，也不宣称伦理结论已经证明。

**审查状态。** 首版发表后，同日由一个独立 AI 审查者复核。审查确认证明全部成立，但指出四处阻断性的表述过度和若干应改之处。本版已按审查改写；第7节列出改正内容，首版保留在 git 历史中。新增的 `NaturalismReview.lean` 给出改正后的形式陈述，前两个模块未改动。

**一元重述（同日，Ren 要求）。** 第0至6节是按 Ren 消息中西方自然主义的提法写的："道德属性"与"自然属性"是否同一。这个提法本身预设了两类东西，再问它们怎样相连。Ren 指出本理论是一元的、关系性的，二元叙事是一个容易不自觉回去的吸引子。第9节据此重写：评价不是第二类属性，而是同一过程中的一个记录关系；"随附"和"同一"由此在 Lean 中推出，而不是作为两类属性之间的哲学论题留下。阅读第0至6节时，应把其中的"道德属性/自然属性""规范前提/中性事实"理解为对西方问题的转述，而不是本理论的框架。

## 0. 结论

1. **本轮证明的是一个候选自然属性的形式性质，不是四条论证本身。** Lean 中没有任何道德谓词。"道德属性随附于自然事实""道德事实解释我们的观察"这些前提都没有被证明。被证明的是：候选属性"整段历史没有取消任何活动的可实现性"（`Along (ContinuationLe P)`）具备四条论证所要求的若干形式特征。
2. **这些形式特征几乎不限定属性。** 随附于访问状态、可组合，对**任意**步关系都成立（`credentials_hold_for_every_relation`），包括平凡关系。所以它们既不选出取向，也不选出这个候选属性。
3. **生成论在随附性上的具体贡献是一个否定结果。** 一般而言，整体质量不能由起点、终点和动作序列决定，必须看中间状态。这是 Ren 所说"整体的积分"在随附性问题上的形式内容。
4. **选出这个属性需要额外前提，而且这些前提是规范性的。** 一是"不取消任何活动的可实现性"这一非削弱前提；二是把受保护范围取为全部活动。"不预先特权化任何活动"并不能推出取全范围：空范围同样不偏向任何活动，而在空范围下任何取向都满足前提。两项都没有证明。
5. **这个前提按现在的写法有系统性反例。** 阻止伤害、每一次排他性选择、每一次承诺都被记为损害（`restraint_registers_as_damage`、`every_exclusive_choice_registers_as_damage`）。中途下降后完全恢复，也与未恢复一样受谴责（`recovered_dip_still_condemned`）。所以它还不能充当伦理同一。下一座桥是从生成关系本身导出受保护活动的范围，并给出对生成（而不只是不损失）的正面度量。这与项目记录一致：整体质量与伦理根据的无假设普遍证明尚未完成。

下表按 Ren 列出的四条，分列各自的对应、已有结果、本轮证明和未证部分。

| 论证 | 生成论的对应 | 已有结果 | 本轮证明了什么 | 未证 |
|---|---|---|---|---|
| 随附性（Jackson） | 候选质量是整段历史的函数 | 中途下降不能由终点摘要恢复（[一体之仁 §7](../../../../theories/becoming/chapters/NONINSTRUMENTAL-CONCERN.md#7-形式化怎样保存同一历程)）；整体评价先于时间表达（[FUTURE-GOOD-INTEGRAL §7](FUTURE-GOOD-INTEGRAL.md#7-whole-appraisal-can-precede-its-temporal-expression)） | 随附蕴含在商上分解，基础的函数随附（对任意性质成立的一般事实）；候选质量一般不随附于起点、终点加动作序列 | 道德属性随附于自然基础；必然共外延到属性同一 |
| 怪异性（Mackie）／简约（Harman） | 候选质量只用过程本身定义 | 核心语义只有可行转换（`GenerativeCore`） | 保持动作词汇不变的精确重表示下不变 | 规范的"应被追求性"；对动作词汇选择的依赖 |
| 认识论 | 损失有有限见证，并落在实际转换上 | 询问何时有用（`InquiryWarrant`）；估值经共同经历形成，正负皆可（[估值发展](../../../../theories/becoming/history/VALUATION-DEVELOPMENT.md)）；完全对称的起点不能由记录决定（[记录与竞争要求](RECORDED-CLAIMS-INTEGRATION.md)） | 有限见证否定保全；损失定位；只看终点认识不到 | 道德信念怎样经观察形成并得到辩护；反思平衡是否收敛 |
| 解释作用（康奈尔） | 候选质量在一切过程中蕴含"活动始终可实现" | `short_kinds_cannot_renew_forever` | 一条跨过程成立的定律式推论 | Sturgeon/Harman 意义上对观察与信念的因果解释 |

## 1. 随附性与 Jackson 的论证

**一般事实。** `Supervenes M N` 指：基础 `N` 相同则 `M` 相同。`supervenes_factors` 证明：若 `M` 随附于 `N`，则 `M` 是 `N` 的同一类（商）上的函数；`base_defined_supervenes` 给出反方向。这对任意 `M`、`N` 都成立，是商的泛性质，不是关于道德的定理。（首版的 `supervenes_iff_factors` 依赖 `Quot.sound`，为满足无公理规则拆成这两条；命题值性质的随附改用不需要 `propext` 的共变形式 `Covaries`。）它表明：**一旦**承认道德属性全局随附于自然基础，就有一个由基础定义的性质与之在一切所论情形中共外延。前件，即道德属性确实随附，本轮没有证明；Lean 里也没有模态量化。

**生成论的具体内容。** `Run` 把历史作为数据保存，包括每个中间状态。`Along R r` 表示关系 `R` 在 `r` 的每一次实际转换上成立。取 `R` 为延续条件序 `ContinuationLe`（后一状态能实现前一状态能实现的一切有限动作序列），候选质量就是"整段展开没有取消任何活动的可实现性"。

- `along_supervenes_on_states`：任意步质量都是访问状态序列的函数。
- `quality_not_fixed_by_endpoints_and_word`、`quality_not_supervenient_on_word`：在 `dip` 过程中，两段从 2 到 2 的历史，动作序列完全相同；一段中途取消了 `use` 的可实现性，另一段没有。这只是一个例子。在确定性过程中，起点加动作序列决定全部状态，质量就随附于它们。所以结论是"一般而言不随附于更粗的基础"。注意：随附于更细的基础是更弱的命题（`supervenes_of_finer`）；实质内容在于对较粗基础的失败。

**无形状反驳。** McDowell（1981）的无形状论证针对非认知主义的"剥离"策略：伦理概念的外延在自然层面可能没有统一性。对 Jackson 的"无限析取"质疑，则主要来自特殊主义论争（Dancy；Jackson、Pettit 与 Smith 2000）。首版声称"可组合、可迁移、可定位"回应了这一反驳。这不成立：可组合、随附于状态对任意 `R` 都成立，不能显示道德外延有自然统一性。

**未证部分。** 道德属性是否随附；必然共外延是否等于属性同一（取决于属性的个体化方式）。

## 2. Mackie 的怪异性与 Harman 的简约

作为支持自然主义的论证，"简约"更接近 Harman；Mackie 是错误论者，他的怪异性论证是反对客观价值的。

候选质量只用过程 `P` 本身定义，不引入新的实体或层次。在保持动作词汇不变、可行动作序列完全对应的重表示下，它不变（`along_continuation_transport`、`converse_projection_iff`）。但细化或粗化动作词汇可以改变判断，所以它**依赖**于把哪些动作算作活动。首版说"不依赖观察者选择的描述方式"，过度了。

Mackie 还有两部分没有被消解。第一，**规范的"应被追求性"**：知道某段历史保全条件，并不使任何人必须追求它。本轮只是把这一点移到第5节的前提上。第二，**相对性论证**：第5节的中立结果说明，自然事实允许融贯的相反取向，分歧未必出于事实错误。这一点对 Mackie 有利，应当保留。

## 3. 认识论

- **损失有有限见证。** 一个动作序列在前一状态可行、在后一状态不可行，这一个有限事实就否定了保全（`witness_refutes_preservation`）。
- **保全是全称命题。** 它涉及一切动作序列，只能得到可错的支持。
- **损失落在实际转换上。** 若可行性可判定（例如有限过程），起点可行、终点不可行的动作序列一定在某一次实际转换上失去（`loss_localizes`）。不假定可判定时，"没有任何转换承担这次损失"也不可能成立（`loss_localizes_nn`）。
- **只看终点认识不到。** 这与[一体之仁 §7](../../../../theories/becoming/chapters/NONINSTRUMENTAL-CONCERN.md#7-形式化怎样保存同一历程)的中途下降结果一致。

这些是关于候选自然属性的认识论，不是关于道德知识的认识论。道德信念怎样经观察形成并得到辩护，可以接到[估值发展](../../../../theories/becoming/history/VALUATION-DEVELOPMENT.md)：对他者后果的看重经共同经历形成，正负联结都可能，所以经验形成的评价需要纠正。还可以接到[延续范围](CONTINUATION-SCOPE-INTEGRATION.md)和[记录与竞争要求](RECORDED-CLAIMS-INTEGRATION.md)。这些连接尚未做成定理。

## 4. 解释作用

`preserved_throughout` 证明：在任意过程中，一段无损历史使起点可实现的每个活动在每个访问状态都保持可实现。它由定义经传递性得到，是一条跨过程成立的定律式推论。`availability_not_fixed_by_endpoints_and_word` 说明这个被推出的事实一般不由起点、终点和动作序列决定。已有的 `short_kinds_cannot_renew_forever`（[更新包](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/README.md)）同样是一条跨实现成立的定律：每类组织带来的少于其形成所需时，无论支持关系如何，更新都必在期限内结束。

这**还不是** Sturgeon 或 Harman 意义上的解释作用。Sturgeon 举的是道德性质参与对行动的因果解释，例如希特勒的堕落解释他的行为；Harman 问的是道德事实能否解释我们的观察与道德信念。本轮都没有触及。Boyd 的独特论点是稳态性质簇与因果调节，不只是多重实现。首版的"解释作用证明属性真实"属于过度表述。

## 5. 等同于哪一个自然属性

**候选。** 整体展开对其自身后续实现、更新与纠正条件的生成或损害。**本轮形式化的只是其中一半：** `Along (ContinuationLe P)` 是二值的"无损失"，没有对生成的正面度量。它还以可行性（是否存在一条路径）为准，而不是概率、实际发生或体验。

### 5.1 中立结果：这些条件不选出取向

`naturalist_criteria_do_not_fix_orientation` 证明：延续条件序及其逆序都是预序，都随附于访问状态。对 `dipped` 中从 2 到 1 的实际转换，一个判为损失，另一个判为可接受。可组合与重表示不变另由 `credentials_hold_for_every_relation` 和 `converse_projection_iff` 给出；前者对任意关系成立，所以中立性比"两个取向"更广。这强化了已有的 `EthicalOrientation.coherence_and_annotation_invariance_do_not_select_growth`。

这是一个欠决定或是/应当的结果，可以**类比** Moore 的开放问题论证。Moore 的论证本身是关于概念与分析性的语义论点，不由这个定理表达。若同一成立，它是综合的、后验的，并由额外前提承担。Horgan 与 Timmons 的"道德孪生地球"是对 Boyd 因果调节语义的语义反驳：直觉上两个共同体在真正地分歧，而那种语义预言它们意义不同。采用一项规范前提，只是把争议移到前提上，并没有回答这个语义论证，因为孪生共同体可以采用相反的前提。

### 5.2 非削弱前提及其限度

**定义。** 若沿取向 `R` 前进时从不取消范围 `W` 中任一活动的可实现性，就说 `R` 对 `W` 非削弱。`NonUndermining` 约束所有状态对；`TransitionNonUndermining` 只约束实际转换。

**已证内容（大多由定义展开得到）。**

- `generation_order_greatest`：对全范围，延续条件序非削弱，且是最大的非削弱取向。空关系同样非削弱，所以说"最大"，不说"选出"。
- `unprivileged_scope_is_whole_scope`：对每个单独活动都非削弱，等于对全部活动非削弱。这只是一个记账引理。它**不**支持取全范围，因为空范围同样不偏向任何活动，而在空范围下逆序也满足前提。
- `guided_history_preserves`、`converse_undermines_in_dip`：按非削弱取向前进的历史保持一切初始可实现的活动，逆序在 `dip` 中会取消一个活动。模型中没有评价者或纠正过程，`use` 只是任意动作。首版说"取消评价与纠正赖以进行的活动"，应改为：会取消任何活动，若模型中有评价与纠正，它们也在其中。

**前提的地位。** 支持它的是一项自反论证：评价、更新和纠正是展开中的活动，允许取消自身行使与被修正条件的取向会削弱它自己。这不是从中性事实推出的，而且即使接受，也只推出保护评价自身所需的活动，推不出保护全部活动。取全范围是又一项规范选择。

### 5.3 与三种候选的比较（以前提为条件）

以下比较都以 5.2 的前提为条件；第 5.4 节表明该前提按现写法过强，所以它们不是对这些理论的反驳。

- **功利主义（福祉或快乐）。** 在 `switching` 过程中，两个状态之间确实可以转换，每个状态各有对方没有的活动。任何完备排序，特别是任何标量福祉排序，都会认可一次取消某个活动的实际转换（`total_orders_undermine_on_transitions`、`scalar_ranking_undermines_on_transitions`）。延续条件序只是通过两次转换都不认可才避免这一点（`generation_endorses_no_switch`）。首版的 `incomparable` 过程里没有状态间转换，那个结果只涉及假想的移动，现在由 `switching` 取代。这是完备性与非削弱之间的取舍；功利主义者完全可以回应说这个前提过强。另外，本候选还没有表示痛苦：不取消任何可行动作的痛苦在 `ContinuationLe` 中不留痕迹。首版的"痛苦确实损害后续条件"没有证明。
- **Railton（理想化的自身利益）。** `fixed_scope_permits_loss` 证明：对预先固定范围非削弱的取向，可以取消范围外的活动。它只对应 Railton 的非道德个人善（以一个中心为范围），不对应他以社会视角刻画的道德正确性。同一结构见于 `ContinuationScope.omitted_scope_admits_needless_foreclosure` 和 `InquiryWarrant.self_scoped_rule_ignores_others`。
- **Foot（自然的善，生命形式）。** 这是最接近的近亲。区别在于，Foot 预先固定物种的生命形式；在生成论中，形式本身在形成和改变。同一个 `fixed_scope_permits_loss` 适用：只保护既定形式所列的活动，可以取消新形成的活动。这对应 Ren 的研究中心："不可预先固定任何预期作为价值单位。"

### 5.4 保留的反例：阻止、选择与恢复都被记为损害

- `restraint_registers_as_damage`：阻止伤害与伤害本身都是条件损失，保留伤害的可能则不算损失。
- `every_exclusive_choice_registers_as_damage`：在两个互斥方向之间作出的任何承诺都是损失。消费、承诺、专门化、老化等一切不可逆进程同理。阻止伤害只是"选择即排除"这一一般事实的一个例子。
- `recovered_dip_still_condemned`：中途下降后完全恢复，与未恢复一样受谴责。
- 存在一条路径即算可行，所以风险暴露与安全无从区分。

这些说明，"不取消任何活动的可实现性"按字面不能充当伦理同一。所需的改进是：

1. 从生成关系导出**受保护活动的范围**，区分维持他者条件的活动与取消他者条件的活动。一个候选是"其行使不取消其他受保护活动"的最大不动点。这一导出不能把"正当活动"预先写进参数。
2. 给出对**生成**的正面度量，并允许修复抵消损失（接 [FUTURE-GOOD-INTEGRAL](FUTURE-GOOD-INTEGRAL.md) 的整体评价）。
3. 把体验与概率纳入条件，而不只用可行性。

## 6. 对 Ren 的判断："以上我们都可以最终证明"

- **本轮证明了：** 一个候选自然属性具有四条论证所要求的若干形式特征。最具体的结果是：整体质量一般不能由起点、终点和动作序列决定。在明示的前提下，延续条件序是最大的可接受取向，并能在形式例子中与三种候选对比。
- **本轮没有证明：** 四条论证的前提（道德属性随附、道德事实参与解释）；同一；前提本身。中立结果还表明，这些形式特征不能选出属性。
- **按现写法被否证的：** 以"不取消任何活动"作为伦理同一标准（第 5.4 节）。
- **下一步：** 第 5.4 节的三项改进可以用数学推进。道德属性的随附、属性同一和规范前提的地位需要哲学论证。

**后续（同日）：** [受保护范围的一次尝试](ETHICAL-NATURALISM-PROTECTED-SCOPE.md)用"不取消他者的正在进行的活动"导出范围。经审查，它不能同时消除阻止与承诺两个反例，对伤害的判断依赖建模方式，结果以否定为主。

**会改变本结论的结果。** 若能从生成关系导出受保护范围，并区分阻止与伤害、承诺与毁坏，而不预设伦理参数，第 5.4 节的反例就被消除。若能证明任何不预设伦理参数的范围都无法区分二者，则本候选需要放弃"非削弱"作为核心。

## 7. 审查与改正记录

独立 AI 审查（2026年10月6日）确认：全部证明重建通过；`dip`、`restraint_registers_as_damage`、`converse_projection_iff` 与审计计数表述正确。依审查所作改正：

- **阻断 1：** "四条论证的可形式化部分已证明"改为"候选属性的形式性质"；删去"道德属性必然共外延已证"。
- **阻断 2：** 补 `credentials_hold_for_every_relation`；撤回首版"可组合、可迁移即回应无形状反驳"的说法。
- **阻断 3：** `incomparable` 中没有状态间转换。新增 `TransitionNonUndermining` 与 `switching` 过程，在实际转换上重证完备排序的结论。
- **阻断 4：** `unprivileged_scope_is_whole_scope` 改述为记账引理，并指出空范围同样不偏向任何活动。
- **应改：**
  - 随附"更强"改为"对较粗基础一般失败"；
  - 说明候选只是二值的"无损失"；
  - 补上不可逆选择与恢复的反例，以及对动作词汇的依赖；
  - 解释作用、Moore、孪生地球、Mackie/Harman、McDowell 的表述按审查改正；
  - 候选比较改为以前提为条件。

## 8. 剩余输入的处理（Ren 的无假设、无公理规则）

Ren 于同日要求：不许有假设，不许有公理；每个输入要么在 Lean 中由过程导出，要么在 Lean 中证明其必要。本线程的处理如下。

| 输入 | 处理 | 定理 |
|---|---|---|
| Lean 标准公理 `propext`、`Quot.sound` | 已消除：102 条新声明全部不依赖任何公理 | 收据 `verification.json` |
| 取向（以"不损失"为上，而非相反） | 已证必要：所有自然资格都相同的两个关系，对同一实际转换给出相反判断 | `credentials_do_not_determine_verdict` |
| 受保护范围取全部活动 | 已证必要："不偏向任何活动"同时允许空范围与全范围，二者对逆向取向的判断不同 | `unprivileged_does_not_fix_scope` |
| 各个示例过程（`dip`、`restraint` 等） | 不是假设：一般定理对任意过程成立，示例只作为存在性见证与反例 | 各模块 |
| 活动的划分（动作词汇） | 已证必要：状态与可能的状态变化完全相同的两个过程，只在两个动作是否算作不同活动上不同，对同一转换的判断就相反 | `vocabulary_changes_verdict` |
| 可行性取"存在一条路径" | 是候选属性的定义，不是隐含假设；概率与体验版本属于另一个候选，尚未研究 | — |
| 道德属性随附、属性同一 | 首版称其"不是 Lean 命题"，这预设了两类属性。一元重述后，评价是同一过程中的记录，其值等于整段历史的关系，随附与同一都已推出（第9节） | `record_tracks_whole_history` |

三项输入（取向、范围、活动划分）都已证明不可省去。它们只出现在定理的定义或前提里，没有被任何定理暗中使用。

## 9. 一元重述：评价是同一过程内的关系

**去掉的二分。** 首版沿用西方提法，把"道德属性"与"自然基础"当作两类东西，再问一类是否随附于、等同于另一类；也把"规范前提"与"中性事实"分开。按[非二元方法](../../../../theories/becoming/chapters/NONDUAL-METHOD.md)，评价、理解和行动都是同一生成展开中分化出的关系。这里不再预设两类，而是把评价写成过程的一个组成部分，看由此能推出什么。

**形式。** [`EmbeddedEvaluation.lean`](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/naturalism/EmbeddedEvaluation.lean)（5 条新审计，均不依赖公理）定义 `recording P E`：在原过程的状态上带一个记录，记录只随原过程自己的转换而改变，改变方式由转换两端状态之间的关系 `E` 决定。评价因此就是过程的一部分，不在过程之外。

- **随附是推出的，不是假设的。** 沿耦合过程的任意历史，记录恰好等于"`E` 在同一历史的每次转换上都成立"（`record_tracks_whole_history`）。西方问题里的"道德属性随附于自然事实"和"同一"，在这里是同一个历史关系的两种说法：记录就是整段历史的关系，作为状态的一部分被携带。没有需要连接的第二类东西。
- **评价与它所评价的条件共命运。** 记录既不开启也不阻止任何活动（`recording_enabled_iff`、`recording_feasible_iff`）；过程能继续多久，评价就能继续多久。按延续条件序前进时，连同记录在内的每个初始可实现活动在每个访问状态都保持可实现（`guided_recording_keeps_continuation`）。评价不能比它赖以进行的条件活得更久。
- **哪一种评价关系形成，是历史本身的事。** 同一过程定律下，以延续条件序记录和以其逆序记录都是可能的耦合；对同一次实际的下降，两者记录相反（`law_admits_opposite_recordings`）。所以第8节证明必要的"取向输入"，一元地看，不是从过程外部输入的"应当"，而是**哪一种评价关系在展开中形成并延续**的问题。这正是[估值发展研究](../../../../theories/becoming/history/VALUATION-DEVELOPMENT.md)处理的形成问题（共同经历形成正或负的联结），也是研究目标中的"选择者的选择"。

**这改变了什么，没改变什么。**

- 改变了：Jackson 的随附与同一不再是两类属性之间待论证的关系，而是对过程内记录的定理；是/应当之分不再是两个领域之间的鸿沟，而是"过程定律不决定哪种评价关系形成"这一已证的、过程内部的事实。
- 没改变：哪一种评价关系在某段历史中实际形成，并没有被证明；也没有证明它必须是延续条件序。首版的反例（阻止、承诺、恢复、逃离）和范围问题都仍然有效，因为它们讨论的是记录所用的关系 `E` 本身。
- 下一步因此是一元的：在同一过程中研究评价关系怎样形成、怎样经后果被修正，以及哪些形成方式能维持其自身被修正的条件。这把伦理自然主义问题接到估值发展和选择者修订的主线，而不是另起一个"道德层"。

## 10. 哪一种评价会延续：直接从生成核心证明

第9节把取向问题改写为"哪一种评价关系在展开中形成并延续"。本节证明延续这一半，只用 `Process`/`Trace`，不引用任何其他模型，不预设种类、速率或支持关系，也不用任何公理。[`RegeneratingPersistence.lean`](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/naturalism/RegeneratingPersistence.lean) 有 10 条结果，全部不依赖公理。

**定义。** 评价本身是过程中的一个活动 `e`。若对每个长度，都有一条至少这么长的实际延续，终点处 `e` 仍然最终可实现，就说 `e` 从 `s` **延续**（`PersistsFrom`）。

- **延续需要一个自我再生的整体。** 在状态有限的过程中，`e` 从 `s` 延续，当且仅当 `s` 能到达某个状态 `c`，过程沿一条非空的实际路径从 `c` 回到 `c`，并且 `e` 在 `c` 处最终可实现（`persists_iff_regenerating_return`）。反方向在任何过程中都成立（`regenerating_return_gives_persistence`）。证明是沿轨迹记录已访问状态的鸽笼论证，所需的有限列表引理都在本模块中自证，没有用库引理。
- **这个整体不损失任何东西。** 沿回到 `c` 的路径，每个活动在每个访问状态的最终可实现性都与在 `c` 处相同（`return_preserves_realizability`）。所以在最终可实现性的层次上，评价赖以延续的整体不取消任何活动，包括评价自身。

**意义。** 能延续的评价，恰好是能到达"再生其自身后续实现条件的整体"的评价；而这个整体在最终可实现性层次上不造成损害。这把第9节"哪一种评价延续"的问题，在过程内部、不借外部"应当"地，连到本理论的候选：整体展开对其后续条件的生成。

**未证。** 哪段历史实际到达哪个再生整体；"延续"是否就是善的尺度（若作为前提引入，须按第8节的规则证明其必要）；以及在立即可行性（`ContinuationLe`）层次上，回路是否也不损失。后者一般不成立：`dip` 中从 2 到 1 再回到 2 是一个回路，却暂时失去了 `use` 的立即可行性。

**与估值研究的关系。** 估值研究的 `valuation_keeping_theorem` 是在更新通道过程上的对应结果（某估值能让一个种类永远延续，当且仅当存在包含它的自我更新群体）。本节的结果在一般 `Process` 上陈述，可以被那里复用。首版曾直接引用那个定理，因而继承了 `propext` 与 `Quot.sound`；按 Ren 的要求已删除（保留在 git 历史中），改为这里的直接证明。待那边的无公理版本合并后，可以证明二者在通道过程上的对应，而不是保留两套平行陈述。

## 11. 评价被实行时，取向是否由延续导出

2026年10月7日。Ren 问：取向是生成的，这是否已经推出？本节回答：**部分推出。** 在延续所定义的层次（最终可实现性）上，被无限实行的东西的方向已经推出是生成的；在立即可行性层次上没有推出；"延续即善"没有推出。[`EnactedOrientation.lean`](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/naturalism/EnactedOrientation.lean) 有 27 条结果，全部不依赖公理（整个包 147 条）。

**此前的反例是记录之间的比较。** `law_admits_opposite_recordings` 中的两种记录都不开启也不阻止任何活动（`recording_enabled_iff`），记录的取向从不影响发生什么，所以它们一样能延续。本节问的是：评价被**实行**时，即它认可的转换就是历史中实际发生的转换时，会怎样。用一个标记 `Q` 挑出被实行的转换，此外不输入任何东西。

**在最终可实现性层次上，两个取向在过程内部不对称。**

- **没有转换会增加最终可实现性**（`no_transition_gains`）。所以"以损失为上"的非严格取向 `converse CanLe` 在每段历史的每次转换上都成立（`loss_order_along_every_history`）：它认可一切发生的事，不区分任何历史。延续包含 `CanLe` 则在每次有损失的转换上不成立（`loses_not_canLe`），是唯一真正有所区分的那一个。
- **损失不能被无限实行。** 状态有限时，任何历史中造成损失的转换都少于状态数（`strict_loss_bounded`）；只认可损失的评价，沿任何历史被实行的次数都少于状态数（`loss_endorsing_enactment_bounded`）。理由在过程内部：一次损失转换的起点此后再也到达不了，所以每次损失都封闭掉一个状态（`loss_marked_bound`）。这几条不用状态的可判定相等。
- **能反复实行的都在保持。** 无论一个评价认可什么，只要它被无界地反复实行，就不可能所有可到达的实行都是损失（`recurring_enactment_not_all_loss`）；再加上状态的可判定相等，可以找到一次位于回路上的实行，它保持每个活动的最终可实现性，两个取向在它上面一致（`recurring_enactment_keeps`、`return_transition_both_orders`）。一个被无界实行的活动也就延续（`unbounded_enactment_persists`，接第10节）。

所以"以损失为其实行的评价会削弱自身的延续"这一猜想在这一层次上成立，但要说准确：**一个以损失为其实行的评价，削弱的是它自身实行的反复，而不必是评价活动本身的可实现性。** 延续选出的是被无限实行的东西的方向，不是每个延续着的评价的判断方向。

**保留的反例。**

- **损失可以先于延续。** 在 `severing` 中，一次转换永久取消了一个活动，之后评价活动 `e` 照样延续（`loss_then_persistence`）。延续给损失设了上界，但不排除损失。一个认可损失的评价也可以延续，只要它此后不再实行损失。
- **有限性是必要的。** 在 `ladder`（自然数状态）中每次转换都取消一个活动，损失转换无界反复（`ladder_loss_recurs`）。
- **在立即可行性层次上取向仍未定。** 在 `dip` 中，不满足 `ContinuationLe` 的转换可以无界反复（`dip_immediate_loss_recurs`），每次都在同一回路上恢复。第5.1、8节的反例在这个层次上仍然成立。
- 最终可实现性层次仍把每次排他性承诺记为损失（第5.4节与 `ProtectedScope`）。这里的结果说的是这些损失在任何历史中都是有限次的，并不改变它们被记为损失。

**对第8节表中"取向"一行的影响。** 该行证明的是：形式资格不决定取向。这一点不变。新增的是：在一元的、被实行的意义上，最终可实现性层次的取向不再是自由输入，过程的时间结构（可实现性只能保持或失去，不能新增）使得只有保持能被无限实行。仍然需要的输入是：取哪个层次（最终还是立即）、状态有限（已证必要）、以及正向陈述里使用的状态可判定相等（与 `persists_iff_regenerating_return` 相同的模型数据；有界性定理本身不需要它）。

**未证。** "延续"或"能被无限实行"是否就是善；哪段历史实际到达哪个回路；在立即可行性层次上对恢复与损失的整体比较（第5.4节第2点）。

### 11.1 取消活动与整体延续的评价范围

7 October 2026. [Ren 纠正前述反例的解释范围](../../../../sources/15-codex-theory-conversations/2026-10-07-whole-continuation-counterexample-scope.md)：应问取消一项活动后，整体的持续是否可以变得更好。以下是 AI 撰写的范围修正，不是新定理。

`severing` 本身是一个共同过程：两个配置、三个活动标记，没有原初的主体、客体或所有者。`loss_then_persistence` 证明 `cut` 后 `other` 永久不可实现，而 `e` 仍满足 `PersistsFrom`。这里的持续是任意长的可容许延续末端仍保有 `e` 的最终可实现性，不是实际未来必然如此、概率判断或伦理评价。

因此，该例只否定“所选活动可以持续，就必定保留先前每一种活动”。它没有证明整体变坏，也没有反驳“取消某项活动可以构成整体生成的改善”。两个状态完整描述这个极小模型，不等于已完整表达待评价的整体关系。先前助手把该例用于解释整体伦理的困难，超出了这个反例的判别能力；保留原数学结论，收窄其伦理用途。

真正的比较必须保留活动终止如何改变实际关系、实现、负担与后续生成条件。对“保留全部活动”的准则，具有充分根据的限制或完成可以构成挑战；对本已容许建设性终止的整体理论，单有取消并非反例。应检验其具体的整体质量判准及相同条件下的竞争解释，而不能随意翻转一个省略这些关系的评价谓词。[当前整体比较](../../../../theories/becoming/history/UNIFIED-ETHICAL-GROUNDING.md#ending-an-activity-and-the-quality-of-the-whole-continuation)保留善的构成说明这一研究任务，也不预先宣布改善已经成立。

## 形式索引

`EnactedOrientation.lean`：`Reach`、`CanLe`、`Loses`、`Gains`、`no_transition_gains`、`loss_order_along_every_history`、`return_transition_both_orders`、`Marked`、`RecursUnboundedly`、`loss_marked_bound`、`strict_loss_bounded`、`loss_endorsing_enactment_bounded`、`recurring_enactment_not_all_loss`、`recurring_enactment_keeps`、`unbounded_enactment_persists`、`loss_then_persistence`、`ladder_loss_recurs`、`dip_immediate_loss_recurs`。

`RegeneratingPersistence.lean`：`PersistsFrom`、`trace_returns`、`regenerating_return_gives_persistence`、`persists_iff_regenerating_return`、`return_preserves_realizability`，以及自证的有限列表引理。

`WholeQualityNaturalism.lean`：`supervenes_factors`、`Covaries`、`covaries_of_supervenes`、`chain_congr`、`base_defined_supervenes`、`supervenes_of_finer`、`Run`、`Along`、`along_iff_steps`、`along_iff_chain`、`along_supervenes_on_states`、`along_append`、`along_mono`、`chain_map`、`along_continuation_transport`、`preserved_throughout`、`witness_refutes_preservation`、`loss_localizes`、`loss_localizes_nn`、`located_loss_breaks_quality`、`quality_not_fixed_by_endpoints_and_word`、`quality_not_supervenient_on_word`、`availability_not_fixed_by_endpoints_and_word`。

`NaturalismIdentity.lean`：`converse_projection_iff`、`dip_two_dominates_one`、`naturalist_criteria_do_not_fix_orientation`、`NonUndermining`、`nonUndermining_whole_iff`、`generation_order_greatest`、`unprivileged_scope_is_whole_scope`、`guided_history_preserves`、`converse_undermines_in_dip`、`fixed_scope_permits_loss`、`generation_leaves_pair_unranked`、`total_orders_undermine`、`scalar_ranking_undermines`、`restraint_registers_as_damage`。其中 `total_orders_undermine`、`scalar_ranking_undermines` 只涉及状态对，由下一模块的实际转换版本取代。

`NaturalismReview.lean`：`credentials_hold_for_every_relation`、`TransitionNonUndermining`、`switching`、`total_orders_undermine_on_transitions`、`scalar_ranking_undermines_on_transitions`、`generation_endorses_no_switch`、`committing`、`every_exclusive_choice_registers_as_damage`、`recovered_dip_still_condemned`。

所有过程、范围与排序都是给定的局部模型输入。没有定理断言哪段历史会发生、前提为真，或在每个选项都有所取消时应如何选择。
