# 独立审查：RenewingFormation 与 ProtectionPriorityRival / Independent review of the generative-discrimination results

2026-10-09，Asia/Bangkok。

**审查方式。** 审查者是 AI（Claude，独立子代理），未参与编写；审查期间未修改仓库任何文件。

**审查对象。** 提交 `b5a236e7` 中的：
- [RenewingFormation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RenewingFormation.lean)（sha256 `2fe6aa4e…`）；
- [ProtectionPriorityRival.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ProtectionPriorityRival.lean)（`cedaf977…`）；
- 两条记录、[整合说明](GENERATIVE-DISCRIMINATION-INTEGRATION.md)、[G0-WARRANT](../../../../theories/becoming/chapters/G0-WARRANT.md) 与首页证据行。

**审查任务。** 设定为反向审查：
- 重编译与哈希核对；
- 陈述是否忠实；
- `WearLaw` 是否使结论空洞或循环；
- 方向与范围；
- 相对 Depletion／ResourceContinuation 的新颖性；
- 哲学上是否说过头。

**探针。** 审查者的探针保存在 [generative-discrimination-review/](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/generative-discrimination-review/)：`ReviewProbes.lean`、`ReviewProbes2.lean`、`ReviewProbes3.lean` 与 `Audit.lean`。它们对应上述提交的源码；作者复核时用 Lean 4.29.1 重新编译，返回码均为 0。

## 1. 审查结论（摘要，AI 审查者文字）

**重编译与哈希。** 四份源码按依赖顺序编译，无 error 或 warning。sha256 与回执、记录一致。两个新文件中没有 sorry、admit、native_decide、axiom、extern、unsafe 或 opaque。所有别名声明只依赖标准公理（propext、Quot.sound、Classical.choice）。定理数与依赖分布与回执一致。

**总体判断。**
- **RenewingFormation：附更正后接受。** 证明正确，不空洞。
- **ProtectionPriorityRival：附更正后接受。** 证明正确，范围正确。
- **文字与证据行：附更正后接受。** 一句 README 证据行按字面为假，发布前必须修正。核心问题是把“AI 的描述性谓词能分开两者”说成了“Ren 的整体判准能分开两者”或“Lean 赋予了 G0 区分力”。另有“恰好”“均匀”两处措辞不准确。

**没问题的部分。**
- A 部分确实不含规范谓词；
- 外部化消耗的边界表述正确，与 `RelationalRenewal.independent_overdraw_persists` 一致；
- `ComparisonPrinciple` 与 `PracticalJudgment.Better` 的方向正确；
- `generative .basic := False` 这一约定无害（探针 9）；
- 两条记录的局限写得准确。

## 2. 发现与处置

| 编号 | 发现 | 处置 |
|---|---|---|
| R1 | `BeyondRenewal` 以初始速率为准，比证明所需强；只需超过当前速率（探针 1）。 | 新增 `BeyondCurrent`，`beyond_current_*` 系列在其下证明；`beyond_renewal_*` 作为推论保留原名。`beyond_current_strictly_weaker` 证明这是严格更弱的条件。 |
| R2 | `Ceaseless` 一次休息即不成立；察觉不到永久能力损失（探针 8）；不表示“更多”。建议改用能力读法（探针 4）。 | 新增 `KeepsCapacity`、`keeps_capacity_iff`、`beyond_loses_capacity_at_once`、`renewal_loss_persists`、`capacity_separates`。两种读法并列；以 `rest_keeps_capacity_not_ceaseless` 与 `wears_yet_ceaseless` 表明二者不同。“更多”与复杂度上升写为边界。 |
| R3 | 不循环，但 `WearLaw` 承担大部分内容；停止的证明是 Depletion 的势函数模式。 | 头注释、整合说明与 G0-WARRANT 写明：区分是所给不可恢复规律的推论。 |
| R4 | `whole_direction_separates` 的名称断言了解释；`event_reading_favors_both` 中的 “favors” 暗示比较；未证明 C 分不开二者（探针 2）。 | 改名为 `ceaseless_separates`、`event_reading_recognizes_both`。新增 `comparison_does_not_apply`：对规律类中任意规律，两者互不为生成扩展。 |
| R5 | `shared_formation_ceases` 的前提比证明所需强；可推广到联合超出。 | 新增 `joint_excess_ends_shared_formation`、`jointly_exceeding_parts_end_shared_formation` 与 `joint_consumption_inhabited`：两个部分各自都在更新之内、只是合起来超出时，共享形成也停止。原定理改为推论。 |
| R6 | 对比定理可推广到每一个更新之内的接续（探针 5）。 | 新增 `within_eventually_exceeds_every_beyond`（在 `BeyondCurrent` 下）。 |
| P1 | “scalar” 的名称与 ℕ 值域不符；ℚ 评分可以恰好表示 J2，但审查者未形式化。 | 改名为 `every_nat_score_trades`、`no_nat_score_represents_priority`。新增 `priority_iff`、`ratio_agrees_with_priority`、`bounded_score_represents_priority`：以交叉相乘比较的有界有理评分 `k/(k+1)`，在每一对选项上与 J2 一致。审查者的数学论证因此有了 Lean 检查。 |
| P2、P3 | 方向、独立性、范围正确；`generative .basic := False` 无害。 | 无须修改。 |
| P4 | G0 不约束排序，“J2 不由 G0 推出”是平凡的；“可同时满足”没有对应定理（探针 7）。 | 新增 `g0_leaves_ordering_open`；文字改为“J2 不由 C 推出；G0 约束相关性，不约束排序”。 |
| P5 | 应标明前例。 | 整合说明与 G0-WARRANT 引用 `both_appraisals_respect_all_extensions`、`tradeoff_has_opposite_strict_appraisals`、`loss_sensitivity_alone_supplies_no_cutoff`，并写明真正新增的三点。 |
| X1 | 首页证据行“磨损其所依存的更新组织的形成有界、停止”按字面为假（探针 8），且漏了“在所给规律下”。 | positive-ground-open-futures 的证据行改为：在所给不可恢复磨损规律下，持续超出更新的形成…… |
| X2 | “Lean 检查……使它有区分力”不对：Lean 检查的是描述性区分。 | 同一证据行与该记录的 related 说明已修正。 |
| X3 | G0-WARRANT 把 AI 的 `Ceaseless` 当作 Ren 的判准；`ceaseless_separates` 用的是总形成的持续，与 §2.2 的范围段落相矛盾。 | §2.2 改写为 AI 的两个形式读法，并说明总形成的持续只在本规律类中与依存关系的接续一致。 |
| X4 | “符号翻转探针不适用”不对：新定理按构造对符号中立，诊断相同。 | 整合说明首段与审查 §6 的更正段落已改。 |
| X5 | “整体方向的读法不会犯这个错误”没有被形式化；证据行合并了两个定理。 | G0-WARRANT §2.4 与 alignment-direction-g0-j 的证据行和 related 说明改为：一步计数把消耗型排在前面；整体方向的读法旨在避免这一错误；尚无已检查的优化结论。 |
| X6 | “恰好排除……均匀聚合”不准确。 | 标题、主张与 G0-WARRANT §2.3 改为“自然数值（单位步长）评分”，并以 `bounded_score_represents_priority` 写明有界评分在此恰好表示 J2。记录 ID 保持稳定，历史中说明其含义。 |
| X7 | practical-judgment-g0-j 证据行漏了“在一个构造情境中”。 | 已补。 |
| X8 | ResourceContinuation 的到达量可以依赖状态，包括内部再生；“外给”不准确。 | 改为：真正的 delta 是磨损反馈，即到达取决于活动自身的压力，总到达不超过 `tri renew`。 |
| X9 | 审查 §6 中“出路 (A) 的代价因此不必承担”过强。 | §6 原文保留，后加更正段落。出路 (A) 不再需要，另有理由：Ren 追问确认，G0 的对象本来就是生生。 |
| X10 | G0-WARRANT 举的例子与范围段落不一致。 | 写明肿瘤式增殖接近本规律类，外部化的竞争性扩张不在其中。 |
| X11 | 偏向消耗型的是一步计数，不是 G0。 | 整合说明与证据行均改为“一步计数”。 |
| X12 | 逐事件读法下，C 把一次休息排在持续形成之下（探针 3）。这是表示上的限制，不是反驳。 | 新增 `event_comparison_ranks_rest_below`，写为边界：本规律不许更新增长，休息的恢复作用被省略。 |

## 3. 更正后的检查

更正后的源码以 Lean 4.29.1 重新检查并通过：
- RenewingFormation：42 项定理／60 项声明；
- ProtectionPriorityRival：15 项定理／25 项声明；
- 全部只依赖标准公理；4 个控制例。

回执见[整合说明 §3](GENERATIVE-DISCRIMINATION-INTEGRATION.md#3-检查)。首次运行与中间运行均保留在 `generative-discrimination-checks/`。

**未复审的部分。** 更正由作者会话依审查意见完成，审查者没有再次复审更正后的版本。新增定理都经 Lean 检查。

## 4. 同日 Ren 追问带来的修订

审查之后，Ren 在另一会话中追问：“我G0是什么？generative和degenerate虽然都在一个becoming model上，但是他们不overlap吧”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md#ren-follow-up)）。由此确认：
- G0 的对象本来就是生生；
- 把形式库存读成“任何新组织都是生成内容”，是 AI 的宽读法。

审查中“效价附着是解释前提”的说法相应细化为两点：
- 生生的正面意义就是 G0 本身；
- 不由 Lean 提供的是两件事：AI 的形式读法确实刻画了生生；“消耗更坏”这一由 C 承担的比较。后者在关系读法下已由 [relational-reading-comparison](../../../../theories/becoming/results/records/relational-reading-comparison.md) 检查。

RenewingFormation 的注释、整合说明、G0-WARRANT 与审查 §6 已同步修订。
