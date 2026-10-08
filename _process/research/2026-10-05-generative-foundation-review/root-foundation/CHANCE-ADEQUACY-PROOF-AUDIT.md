# 机会充分性：既有证明与适用对应审计

2026-10-08。AI 撰写。本轮沿 G0/J 公理路线检验：共同安排准备接管、关闭或替换原先可继续的正当保护通道时，既有关系如何限制它可以宣称已经完成的承接。**新增 Lean 定理 0 项，新增形式声明审计 0 项，编译重跑 0 次。** 本文核读现有源码与回执，不把哲学适用论证算作新的机器证明。

## 1. 本轮新增内容在哪里

已有 [J3](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/PRACTICAL-JUDGMENT.md#4-谁承担什么--allocating-responsibilities)将正当承担、合理依赖及可归责地撤去替代，与有界履行、修复和交接相连。本轮尝试把它用于**接管之前已经存在的实际保护**：新的共同安排不能仅凭取得控制，就把被它关闭的正当通道降成可忽略的过去。

这一适用须分别说明：旧通道实际保护什么、在相关期限内是否还可继续、其使用或承担何以正当、接管怎样撤去了它，以及何种承接、释放或更充分根据可改变责任。原有概率高、时间上先存在或实际控制强，都不能单独证明其受保护资格。旧安排若依赖不正当剥夺，也不能靠“保持原状”取得新正当性。

故本轮的实质连接是**已有 J3 的责任根据 → 特定接管中仍有效的保护要求**；不是再假定一个任意概率下界，也不是从 G0 独自推出所有初始份额。活动、供给、选择、风险和受影响位置在同一历史中形成；没有先置独立的价值所有者。具体责任仍保留各位置、时间与共同支承的差别。

## 2. 从现有源码直接核对的可复用结果

下表列原模块自己的验证范围；数字全部属于既有成果，不新增或重新相加。源码链接所指为本轮实际读取版本。

| 既有模块与结果 | 可以复用的准确内容 | 仍须另证的适用关系 |
|---|---|---|
| [PracticalJudgment](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/PracticalJudgment.lean)，30 项定理／46 项审计 | `necessary_means_required`：在已有非空合格方案集、已成立任务及必要条件对应下，必要条件继承要求。`transfer_requires_actual_successor`、`uncovered_demand_is_failure`：实际需求时撤去旧支持后，完整承接不能缺少后继。`unfulfilled_unreleased_remains`：未履行、未获释放的既有承担保留残余。 | 这些声明不判断哪项承担正当；`Covered` 是需求时点的确定性覆盖，**没有自动把概率保护转译成确定履行**。新的概率对应须独立说明。 |
| [CrossedClaims](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CrossedClaims.lean)，8／23 | `replacement_preserves_each_ticket` 保留同一实际票中的 P、R 保护并改善 Q；`transfer_conserves_total_and_chances`、`transfer_preserves_any_satisfied_floor` 保留共同正分母下已经满足的机会下界。 | 有效路线、许可、时限和原下界的规范资格是输入。它不是任意接管的完备分类，也不证明本轮旧通道天然享有任何特定份额。 |
| [ChanceRevision](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ChanceRevision.lean)，7／15 | `no_terminal_law_characterization`：该四票模型中，完整终点分布不足以刻画对先前结果的忠实；`settlement_forces_conditional_concentration`、`preservation_composes` 保留给定已确定结果的历史范围。 | 原结果是否有效确定、是否仍有约束力、是否正当释放，并不由 `Preserves` 证明。接管尚未开奖的通道与推翻已经确定的分配不是同一情境。 |
| [JointRiskRevision](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/JointRiskRevision.lean)，18／30 | `compatible_iff` 给出该有限二风险表的准确相容条件；`better_marginals_worse_joint` 与 `no_marginal_only_joint_estimator` 限制只保留各处风险数字的概括。 | 该相容定理不证明任意三处救助、现实随机化或新接管菜单可行。须保留原保护所依赖的共同事件、支承和时间关系；实际概率来源也不是由有限计数认证。 |
| [ChanceGrounding](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ChanceGrounding.lean)，4／10 | `no_maximum_in_unbounded_positive_ticket_domain` 与 `fixed_resolution_unique_maximum` 已检验正票约束配合指定人数目标的限度。 | 不证明 CP 错误、任何统一概率下界必要，或某个原机会充分；不能把固定票数所生的最小正票当作伦理尺度。 |
| [BoundedRiskRevision](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/BoundedRiskRevision.lean)，9／13；其 BasicRiskSharing 19／36 为继承 | `frontier_exact`、`whole_allowance_iff`、`four_point_constraint_optimum` 已处理给定共同风险律和诊断约束的范围；`scope_bounds_compose` 与 `resetting_allowance_exceeds_original_scope` 检验逐步重设基准怎样越出原范围。 | 总风险及最大风险是公开诊断，指定 allowance 不是获辩护的伦理容差。新承接若改变比较基准，仍须保留原要求的范围，不能仅援引一次局部改进。 |

原回执：[PracticalJudgment](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/practical-judgment-verification.json)、[CrossedClaims](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/crossed-claims-verification.json)、[ChanceRevision](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/chance-revision-verification.json)、[JointRiskRevision](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/joint-risk-revision-verification.json)、[ChanceGrounding](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/chance-grounding-verification.json)、[BoundedRiskRevision](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/bounded-risk-revision-verification.json)。本轮只读比对六份回执绑定的七个不同当前源码文件，SHA-256 全部相符；这不是重新编译、全产物重审或对并行研究的整体认证。

## 3. 本轮不声称的新数学

不新增“给定双方可接受代价界，所以份额落入某闭区间”的定理。它会把正在追问的可接受性直接放进前提；即使代数正确，也没有补充本轮的责任根据。若今后采用新的概率公式、区间充要条件、严格可行性例或优化结论，仍须另行 Lean 实查，不能以初等为由免除。本轮不报告这些新结论，也不把上表定理当作它们的检查回执。

不将一次基本救助改写成可以反复补偿的服务频率。已有 [SustainedJudgment](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SustainedJudgment.lean) 的 `scheduled_actual_history` 和 `partial_competence_misses_deadline` 已保留实际串接与给定期限。本轮没有取得当前损失可等到下一轮、重复供给可行或后续份额足以承接本次损失的对应依据；因此不另造时序模型代填一次机会的充分性。

## 4. 可以继续到哪里，哪里仍未决定

在具体正当通道被实际接管的情境中，可以依据 J3 审查它原先保护的内容是否被承接，拒绝把名义正机会直接当作完整履行。若实际条件不足，可要求修正接管范围、保留原路线、寻求有根据的释放或记录未满足责任；不能从方案集空缺推出无限义务，也不必等待全部伦理争议解决才作有根据的及时行动。

这一审计没有决定**不存在此类受保护旧通道的初始共同救助**应当分配多少，也没有证明保住旧机会便已公平、完整或最优。它把一类机会限制连接到有内容的责任历史，同时保留 CP 的一般充分性、真实共同可行性与新比较根据各自的未决范围。
