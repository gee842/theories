# 既有伦理模块在 Becoming 脊柱上的位置 / Ethics modules on the Becoming spine

由 [BECOMING-INSTANCE-CHECK.py](BECOMING-INSTANCE-CHECK.py) 生成，勿手改；检查结果见 [BECOMING-INSTANCE-CHECKS.json](BECOMING-INSTANCE-CHECKS.json)。这是[统一计划](BECOMING-UNIFICATION-PLAN.md) P3 的分类表。

按计划第 1 节的判据，伦理族中含类型多态定理的模块共 46 个（10,895 行、765 条定理）。通用模块对小接口多态，因此不复制、不改写：脊柱给出接口的实例，或证明模块自建的组合子就是脊柱上的同一概念，它们的定理便直接作用于同一展开。具名声明在 [Becoming.Bridge](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Bridge.lean)、[Becoming.Renewal](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Renewal.lean) 或 [Becoming.Metaethics](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Metaethics.lean) 中，由脊柱回执逐条检查，公理报告为空。Mathlib 叶子的具名声明在外围桥接 [CorrectionInquiry](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrectionInquiry.lean) 中，由它自己的回执（Lean 4.30.0-rc2）检查，公理报告同样为空。

Generated; do not edit. The polymorphic ethics modules are not copied: the spine instantiates their interfaces or proves their combinators equal to its own, so their theorems apply to one unfolding. Each named declaration is kernel-checked with an empty axiom report by the spine receipt, or, for Mathlib leaves, by the receipt of the peripheral bridge CorrectionInquiry.

**方向约定。** `GenerativeComparison` 中 `Better first second` 表示后者更好；`PracticalJudgment` 与 `LiftBetter` 中 `better x y` 表示前者更好。桥接定理保留各自的约定。

**提升规则 L 是实质承诺。** 一个回应若有一好一坏两个结果，保守规则在两个方向上都不作比较（`LiftModel.some_outcome_does_not_lift`）；经无结果的中间回应，传递性失败（`LiftModel.lift_needs_live_middle`）。

| 类别 / Category | 模块 | 行 | 定理 |
|---|---:|---:|---:|
| 接口实例或等价定理 / Interface instantiated or proved equal | 11 | 2,974 | 199 |
| 已在核心上 / Already on the core | 8 | 2,456 | 130 |
| 对历史类型多态 / Polymorphic over histories | 10 | 2,109 | 138 |
| 运行上的更新界（P3b） / Renewal bounds on runs (P3b) | 2 | 382 | 27 |
| Mathlib 叶子（P5c） / Mathlib leaves (P5c) | 6 | 1,340 | 140 |
| 具体模型 / Concrete models | 9 | 1,634 | 131 |

## 接口实例或等价定理 / Interface instantiated or proved equal

模块自建的接口或组合子，脊柱给出具名实例，或证明它就是脊柱上的同一概念。

| 模块 | 定理（多态） | 脊柱声明 | 说明 |
|---|---:|---|---|
| [CutCoverageAudit](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean) | 12（8） | `cutReach_iff_closure` | `Reach` 与 WholeGroundCoverage 的 `Reached` 逐字同构 |
| [JointContinuationClassification](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean) | 5（4） | `Frame.continuations`，`Frame.map_preserves_bundles`，`Frame.lift_reflects_bundles` | 可达配置即延续空间；忠实变换来自核心 `trace_map`／`trace_lift` |
| [WholeGroundCoverage](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean) | 27（18） | `reached_iff_closure` | `Reached` 即沿边的可达闭包 |
| [CorrectionInfrastructure](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrectionInfrastructure.lean) | 34（17） | `liveStep_iff_enabled` | `LiveStep` 即 `Enabled` |
| [EvaluatorGrounding](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/EvaluatorGrounding.lean) | 12（0） | `chain_iff_reach` | `Chain` 即边过程上的可达；路线在核心中的位置见 EVALUATOR-GROUNDING-ARGUMENT §9 |
| [GenerativeComparison](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean) | 11（7） | `Frame.inventory`，`g0_iff`，`extension_iff`，`comparison_iff`，`comparison_lifts`，`articulation_iff_lifted`，`lifted_comparison_supplies_reason`，`lift_coherent_selection_survives`，`lift_continual_improvement_has_no_survivor` | G0、生成扩展与 C 在定义上即核心的；函数式情境恰为提升规则 L 下的确定情形；比较、理由、存活与持续改进推广到每个框架 |
| [PositionedPositiveReason](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/PositionedPositiveReason.lean) | 9（3） | `securesPositiveGround_iff`，`positionedArticulation_iff`，`positioned_articulation_of_articulates`，`universal_reason` | 确保的正面根据与 D 在定义上即核心的；路线理由由表述前提 A 给出 |
| [PositiveGroundUncertainty](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/PositiveGroundUncertainty.lean) | 9（3） | `universal_reason` | 可靠探究的范围给出 `SecuresPositiveGround` 的实例 |
| [PracticalJudgment](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/PracticalJudgment.lean) | 30（20） | `commonResponse_is_robust`，`robust_iff_commonResponse`，`BetterAt` | `Robust` 即共同回应，反之每个稳健回应都是某过程的共同回应；`Better` 在配置上即 `BetterAt` |
| [PracticalReach](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/PracticalReach.lean) | 24（12） | `guarantees_iff_completes` | `Guarantees` 即一步完成 |
| [StandardsBridge](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/StandardsBridge.lean) | 26（15） | `revise_is_after` | 按观察过滤规则表即纯观察上的 `After` |

## 已在核心上 / Already on the core

定理陈述在核心 `Process`／`Trace` 上；框架的 `P` 直接代入，无需桥接。

| 模块 | 定理（多态） | 脊柱声明 | 说明 |
|---|---:|---|---|
| [LivingAllocation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingAllocation.lean) | 16（0） | — | — |
| [LivingExpansion](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingExpansion.lean) | 14（0） | — | — |
| [LivingOrganization](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingOrganization.lean) | 22（0） | — | 生命组织的轨迹与可行动作 |
| [LivingRealization](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean) | 10（0） | — | — |
| [LivingRecovery](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean) | 15（0） | — | — |
| [SituatedContinuation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean) | 15（2） | — | 也用到 ContinuationRenewal，见 P3b |
| [SituatedRenewal](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean) | 9（0） | — | 也用到 ContinuationRenewal，见 P3b |
| [SustainedJudgment](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SustainedJudgment.lean) | 29（7） | — | 同时用到 `PracticalJudgment`，经其桥接 |

## 对历史类型多态 / Polymorphic over histories

定理对历史（完整相关延续）类型及外给关系多态；取历史为框架的配置即直接适用，前提仍由使用者提供。用到 `Robust`、`Better`、`Inventory` 处，经第一类的桥接定理与脊柱概念等同。

| 模块 | 定理（多态） | 脊柱声明 | 说明 |
|---|---:|---|---|
| [WholePracticalRestriction](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean) | 14（10） | — | `Family Whole Index`：整体取配置，指标取立场 |
| [AlignmentDirection](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/AlignmentDirection.lean) | 9（1） | — | 唯一的多态定理是忠实修订保持要求；其余为具体 AI 服务例 |
| [ClassificationRevision](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ClassificationRevision.lean) | 16（7） | — | 记录与目标在历史上 |
| [ClassificationRobustJudgment](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ClassificationRobustJudgment.lean) | 13（7） | — | 经 `PracticalJudgment` |
| [ConcernExtension](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ConcernExtension.lean) | 8（8） | — | 经 `PracticalJudgment` |
| [EvaluativeExtension](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/EvaluativeExtension.lean) | 20（7） | — | 经 `PracticalJudgment` |
| [GenerativeLossComparison](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean) | 16（6） | — | 外给的 `Le` 可取 `BetterAt` |
| [GenerativeTradeoff](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean) | 11（4） | — | `Problem Circumstance Response History` |
| [RelationalOrganization](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RelationalOrganization.lean) | 13（1） | — | 经 `PracticalJudgment` |
| [SelectorReviewCoverage](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/SelectorReviewCoverage.lean) | 18（6） | — | `live`／`menu` 与 `Robust` 同形，世界取范围内的配置 |

## 运行上的更新界（P3b） / Renewal bounds on runs (P3b)

定理对状态序列 `Nat → S` 多态，运行的 `state` 直接代入；其自然数秩的更新或完成界是 `falls_finitely` 的情形。`ContinuationRenewal` 的良基形式比自然数秩更一般，不由该原则导出。

| 模块 | 定理（多态） | 脊柱声明 | 说明 |
|---|---:|---|---|
| [ContinuationRenewal](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean) | 17（5） | `falls_finitely`，`Run.renewal_recurs` | 无更新尾部与任意晚的更新 |
| [OpenFutureRevision](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/OpenFutureRevision.lean) | 10（3） | `falls_finitely` | 交接的剩余步数证书；完成界来自 ContinuationRenewal |

## Mathlib 叶子（P5c） / Mathlib leaves (P5c)

依赖 Mathlib，用 4.30.0-rc2 检查，不进入核心。外围桥接 `CorrectionInquiry` 导入核心与两个叶子：在每个观察值的格上，纠正与安全选择就是核心判断过程的共同回应，细化观察就是收窄信念（`commonResponse_antitone`）。其余是具体模型或关系代数，核心没有对应的接口。

| 模块 | 定理（多态） | 脊柱声明 | 说明 |
|---|---:|---|---|
| [CorrectionBoundary](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrectionBoundary.lean) | 19（4） | `implements_iff_commonResponse`，`commonAction_iff_commonResponse`，`implements_refine` | 实施即每个格上的共同回应；`refine_observation` 由核心导出 |
| [CorrectionInquiry](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrectionInquiry.lean) | 7（4） | — | 外围桥接本身 |
| [CorrectionParent](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrectionParent.lean) | 16（1） | — | 具体的父子纠正模型；多态引理只组合已给的可行命令 |
| [CorrectionRelations](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrectionRelations.lean) | 39（9） | — | 关系边界的代数（`Boundary`、`Couple`）；核心不陈述异类关系的合成 |
| [ObservationChange](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ObservationChange.lean) | 28（3） | `safeOn_iff_commonResponse`，`safeOn_refine` | `SafeOn` 即显示该值的世界上的共同回应；细化保持安全选择由核心导出 |
| [ObservationRepair](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ObservationRepair.lean) | 31（4） | — | 具体的实数评分模型 |

## 具体模型 / Concrete models

具体反例、可执行规划器或证据模型。多态引理服务于这些模型（列表、过滤、可执行计算），不是需要在脊柱上实例化的接口；两个探究模块是探究层的确定、可计算特例。

| 模块 | 定理（多态） | 脊柱声明 | 说明 |
|---|---:|---|---|
| [AggregationContext](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/AggregationContext.lean) | 6（1） | — | — |
| [AlignmentInquiry](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/AlignmentInquiry.lean) | 9（9） | — | 可执行的一次探测规划器，是探究层的确定、可计算特例 |
| [EvidenceQualifiedCorrection](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/EvidenceQualifiedCorrection.lean) | 24（9） | — | 候选模型池与保守证书 |
| [FallibleInspection](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FallibleInspection.lean) | 24（4） | — | — |
| [FormativeAssessment](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeAssessment.lean) | 18（3） | — | 确定性评估序列，是探究层的特例 |
| [ReformEvidence](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReformEvidence.lean) | 23（1） | — | — |
| [RelationalGrounding](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RelationalGrounding.lean) | 6（1） | — | 关于边际描述的具体反例 |
| [UnequalBasicLosses](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/UnequalBasicLosses.lean) | 14（2） | — | 两层损失诊断；多态引理是报告去重 |
| [WisdomGoalGrounds](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/WisdomGoalGrounds.lean) | 7（1） | — | — |

## 范围 / Scope

分类与逐行机械检查。被继承模块不在此重新编译；具名声明的内核检查由脊柱回执或外围桥接的回执提供。第三类定理的前提（历史类型的含义、外给关系的规范根据）仍由使用者提供，取配置为历史并不证明这些前提。未桥接的 Mathlib 叶子与具体模型是有意的：它们没有核心上的接口需要实例化。
