# Lean 具名声明 / Named Lean declarations

[返回 Lean 导航](LEAN-INDEX.md)。本表显示当前工作源与审计入口；所有历史副本仍见 [JSON 清单](data/lean-index.json)。这是显式声明的位置索引，不能代替命题、假设及对应论证的阅读。 / [Return to navigation](LEAN-INDEX.md). Working sources and audit entries appear here; all historical copies remain in the JSON inventory. These are explicit declaration locations, not substitutes for statements, hypotheses and correspondence arguments.

定理／引理逐项列出；定义与类型声明列在同一模块的折叠项中。限定名由文本 namespace 推断，仅供导航；私有内部名称和自动生成名称以 Lean 为准。 / Theorems and lemmas are individually listed; definitions and type declarations share each module's foldout. Namespace-qualified names are textual hints; Lean determines private/internal and generated names.

## 按方向浏览 / Browse by topic

| 方向 / Topic | 模块／审计入口 / Entries | theorem/lemma 位置 / Occurrences |
|---|---:|---:|
| [规范根据与生成方向 / Normative grounding and generative direction](lean-declarations/ethics.md) | 133 | 2,238 |
| [评价的形成与良知 / Valuation development and liangzhi](lean-declarations/valuation.md) | 19 | 202 |
| [可达询问、接触与过程律 / Attainable inquiry, contact and process laws](lean-declarations/inquiry.md) | 72 | 1,880 |
| [支持与更新 / Support and renewal](lean-declarations/renewal.md) | 12 | 309 |
| [学习、预测与动力学 / Learning, prediction and dynamics](lean-declarations/learning.md) | 50 | 876 |
| [抽象、适用性与构成 / Abstraction, applicability and constitution](lean-declarations/abstraction.md) | 41 | 858 |
| [关切与共同活动 / Concern and shared activity](lean-declarations/concern.md) | 15 | 246 |
| [组织形成到可修正评价 / Organizational formation through revisable evaluation](lean-declarations/shared.md) | 66 | 1,480 |
| [生成核心与关系结构 / Generative core and relational structure](lean-declarations/core.md) | 151 | 2,278 |
| [其他形式研究 / Other formal studies](lean-declarations/other.md) | 26 | 802 |

## 按名称查找 / Find by name

各分组页可使用浏览器查找；编辑器的跨文件搜索可查全部名称。命令行可从仓库根运行： / Use browser find within a topic page or an editor's cross-file search for every name. From the repository root:

```sh
rg -n 'theorem_name' theories/becoming/results/lean-declarations/
```

## 模块清单 / Module list

| 模块 / Module | 方向 / Topic |
|---|---|
| [AcquiredActivityScope.lean](lean-declarations/concern.md#module-9a94f43dc79c) | 关切与共同活动 / Concern and shared activity |
| [AcquiredApplicability.lean](lean-declarations/abstraction.md#module-3a9468f07796) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [AcquiredBinding.lean](lean-declarations/inquiry.md#module-9d82771d91d8) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [AcquiredContact.lean](lean-declarations/inquiry.md#module-16b45775dfc4) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [AcquiredCorrection.lean](lean-declarations/ethics.md#module-16aca933a540) | 规范根据与生成方向 / Normative grounding and generative direction |
| [AcquiredCorrectionCases.lean](lean-declarations/ethics.md#module-97814b0f3d34) | 规范根据与生成方向 / Normative grounding and generative direction |
| [AcquiredEvaluation.lean](lean-declarations/shared.md#module-1f4b41b7b576) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [AcquiredInitiationConstraint.lean](lean-declarations/concern.md#module-078cf605a4ff) | 关切与共同活动 / Concern and shared activity |
| [AcquiredPerspective.lean](lean-declarations/core.md#module-469910b4b12f) | 生成核心与关系结构 / Generative core and relational structure |
| [AcquiredPredictionRecord.lean](lean-declarations/learning.md#module-e55152492e3a) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [AcquiredPurposeCriterion.lean](lean-declarations/concern.md#module-2f598ac2951f) | 关切与共同活动 / Concern and shared activity |
| [AcquiredSegmentation.lean](lean-declarations/inquiry.md#module-84f4ce7a7d6e) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [AcquiredSupportUse.lean](lean-declarations/core.md#module-c8a560cd7d84) | 生成核心与关系结构 / Generative core and relational structure |
| [AcquiredSupportUseCases.lean](lean-declarations/core.md#module-ec38d16ff606) | 生成核心与关系结构 / Generative core and relational structure |
| [ActionAwareTracking.lean](lean-declarations/learning.md#module-c1e8bbb07357) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ActionPreparation.lean](lean-declarations/shared.md#module-c89e3d27ff4d) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ActionWitness.lean](lean-declarations/shared.md#module-1e9f6921303e) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ActualRecovery.lean](lean-declarations/core.md#module-6b8e6a0d66ac) | 生成核心与关系结构 / Generative core and relational structure |
| [AdaptiveCore.lean](lean-declarations/learning.md#module-c3234339b888) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [Admission.lean](lean-declarations/abstraction.md#module-d133a5ed4253) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [AdmissionRevision.lean](lean-declarations/other.md#module-5db887ac5876) | 其他形式研究 / Other formal studies |
| [AggregationContext.lean](lean-declarations/ethics.md#module-dd5b30c26cf2) | 规范根据与生成方向 / Normative grounding and generative direction |
| [AlignmentContinuityCases.lean](lean-declarations/ethics.md#module-8d8f2a3044e4) | 规范根据与生成方向 / Normative grounding and generative direction |
| [AlignmentDirection.lean](lean-declarations/ethics.md#module-98f04fce15eb) | 规范根据与生成方向 / Normative grounding and generative direction |
| [AlignmentInquiry.lean](lean-declarations/ethics.md#module-503febdf34f7) | 规范根据与生成方向 / Normative grounding and generative direction |
| [AlignmentSuccession.lean](lean-declarations/other.md#module-69a93b1cf280) | 其他形式研究 / Other formal studies |
| [ApplicabilityGrounding.lean](lean-declarations/abstraction.md#module-3a59dae65c20) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [ApplicabilityProofs.lean](lean-declarations/abstraction.md#module-1c37938595ec) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [ApplicationEvidence.lean](lean-declarations/shared.md#module-dd170fb920e6) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ArchivePreparation.lean](lean-declarations/shared.md#module-f08c6d6875b6) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [AssemblyDerivedSelection.lean](lean-declarations/ethics.md#module-30cc534a61b8) | 规范根据与生成方向 / Normative grounding and generative direction |
| [AttainableQuestions.lean](lean-declarations/inquiry.md#module-eb7be2a9177f) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [Audit.lean](lean-declarations/ethics.md#module-d20e9f31de69) | 规范根据与生成方向 / Normative grounding and generative direction |
| [Audit.lean](lean-declarations/valuation.md#module-037c0640f9e2) | 评价的形成与良知 / Valuation development and liangzhi |
| [Audit.lean](lean-declarations/valuation.md#module-6b4c32dcec82) | 评价的形成与良知 / Valuation development and liangzhi |
| [AxiomFree.lean](lean-declarations/valuation.md#module-697097c023d4) | 评价的形成与良知 / Valuation development and liangzhi |
| [BasicRiskSharing.lean](lean-declarations/ethics.md#module-e98555289c3e) | 规范根据与生成方向 / Normative grounding and generative direction |
| [Becoming.lean](lean-declarations/core.md#module-cbce862e630a) | 生成核心与关系结构 / Generative core and relational structure |
| [BecomingCompatibility.lean](lean-declarations/core.md#module-55e216de65da) | 生成核心与关系结构 / Generative core and relational structure |
| [BecomingReversibility.lean](lean-declarations/core.md#module-3104a5fd24d5) | 生成核心与关系结构 / Generative core and relational structure |
| [BoundaryModels.lean](lean-declarations/core.md#module-5ffb89fcbb01) | 生成核心与关系结构 / Generative core and relational structure |
| [BoundedRiskRevision.lean](lean-declarations/ethics.md#module-3588f48eb92f) | 规范根据与生成方向 / Normative grounding and generative direction |
| [Bridge.lean](lean-declarations/core.md#module-014c999286cd) | 生成核心与关系结构 / Generative core and relational structure |
| [BridgesAudit.lean](lean-declarations/valuation.md#module-e1bed40c8da7) | 评价的形成与良知 / Valuation development and liangzhi |
| [CalibratedMacro.lean](lean-declarations/inquiry.md#module-c90fa4594397) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [CalibratedUpdater.lean](lean-declarations/ethics.md#module-b96605b46320) | 规范根据与生成方向 / Normative grounding and generative direction |
| [CalibrationRenewal.lean](lean-declarations/ethics.md#module-f0a8bfc734fa) | 规范根据与生成方向 / Normative grounding and generative direction |
| [CalibrationRevision.lean](lean-declarations/abstraction.md#module-365cf9c6139b) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [CarrierDiagnosis.lean](lean-declarations/other.md#module-92cfb0fcf109) | 其他形式研究 / Other formal studies |
| [CarrierTurnover.lean](lean-declarations/shared.md#module-abe231e35227) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [Cases.lean](lean-declarations/concern.md#module-5fd22deccdc6) | 关切与共同活动 / Concern and shared activity |
| [ChanceAdequacy.lean](lean-declarations/ethics.md#module-166f8dbba86d) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ChanceGrounding.lean](lean-declarations/ethics.md#module-d2e31b48895f) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ChanceRevision.lean](lean-declarations/ethics.md#module-d023f6d5e0bf) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ChangingDependency.lean](lean-declarations/learning.md#module-751a219a4f11) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ClaimLedger.lean](lean-declarations/shared.md#module-970e18466304) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ClassificationRevision.lean](lean-declarations/ethics.md#module-38dae45bdd62) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ClassificationRobustJudgment.lean](lean-declarations/ethics.md#module-6d2ff915d8b9) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ClosedLoopAudit.lean](lean-declarations/valuation.md#module-a5bbd3ef7a72) | 评价的形成与良知 / Valuation development and liangzhi |
| [ClosedLoopValuation.lean](lean-declarations/valuation.md#module-c43d59d00448) | 评价的形成与良知 / Valuation development and liangzhi |
| [CollectiveDestruction.lean](lean-declarations/other.md#module-2b8dee3aab5f) | 其他形式研究 / Other formal studies |
| [CommonCauseDiscovery.lean](lean-declarations/other.md#module-7ef37aae8095) | 其他形式研究 / Other formal studies |
| [CommonOrganization.lean](lean-declarations/other.md#module-4501154a9279) | 其他形式研究 / Other formal studies |
| [CommonTaskRevision.lean](lean-declarations/other.md#module-f3a330415bf8) | 其他形式研究 / Other formal studies |
| [CompletionApplicability.lean](lean-declarations/core.md#module-b4ba5435b460) | 生成核心与关系结构 / Generative core and relational structure |
| [CompletionAudit.lean](lean-declarations/valuation.md#module-3ae2f0d8deb5) | 评价的形成与良知 / Valuation development and liangzhi |
| [CompletionBoundaries.lean](lean-declarations/abstraction.md#module-c1591ec1fb8e) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [CompletionExamples.lean](lean-declarations/abstraction.md#module-d333c1de816c) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [CompletionRole.lean](lean-declarations/abstraction.md#module-cd95616611d7) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [CompositionalAcquisition.lean](lean-declarations/inquiry.md#module-d84368196389) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [CompositionalFormation.lean](lean-declarations/inquiry.md#module-60bbe467c572) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [CompositionalTransmission.lean](lean-declarations/inquiry.md#module-17e1d21d3551) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [ConcernExtension.lean](lean-declarations/ethics.md#module-73fe52179f3c) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ConnectedGenerativeModel.lean](lean-declarations/core.md#module-5fa095440b41) | 生成核心与关系结构 / Generative core and relational structure |
| [ConnectedModel.lean](lean-declarations/core.md#module-5c73c09dd045) | 生成核心与关系结构 / Generative core and relational structure |
| [ConnectionistRecovery.lean](lean-declarations/ethics.md#module-4b3906aa71e1) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ConsequenceInquiry.lean](lean-declarations/abstraction.md#module-6c65c55bbb0f) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [ConsequenceTransmission.lean](lean-declarations/shared.md#module-af38a04c2c3b) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ConstructedPrediction.lean](lean-declarations/learning.md#module-0122dd51e123) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ConstructedSelector.lean](lean-declarations/learning.md#module-339f067fcb29) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ConstructedUpdater.lean](lean-declarations/learning.md#module-f1c81893690e) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ConstructiveDecisions.lean](lean-declarations/core.md#module-b25b9b8fad1d) | 生成核心与关系结构 / Generative core and relational structure |
| [ContactFormation.lean](lean-declarations/inquiry.md#module-7bd60e384c41) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [ContactReconstruction.lean](lean-declarations/ethics.md#module-b4a4a6db6e9a) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ContextualLeaseRules.lean](lean-declarations/core.md#module-078a317fe058) | 生成核心与关系结构 / Generative core and relational structure |
| [ContextualLogicAbstraction.lean](lean-declarations/core.md#module-475f324ef88e) | 生成核心与关系结构 / Generative core and relational structure |
| [ContextualWisdom.lean](lean-declarations/core.md#module-3b9ba9d9b6a4) | 生成核心与关系结构 / Generative core and relational structure |
| [ContinuationAdequacy.lean](lean-declarations/learning.md#module-fa7b94dd1994) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ContinuationConditions.lean](lean-declarations/core.md#module-e5007bff1b23) | 生成核心与关系结构 / Generative core and relational structure |
| [ContinuationRenewal.lean](lean-declarations/ethics.md#module-3e3471402b88) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ContinuationRenewalAudit.lean](lean-declarations/ethics.md#module-38d6a8892340) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ContinuationScope.lean](lean-declarations/abstraction.md#module-62dd1356dc98) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [ContractionMechanisms.lean](lean-declarations/core.md#module-94b24f64f928) | 生成核心与关系结构 / Generative core and relational structure |
| [ControlledRefinement.lean](lean-declarations/learning.md#module-8fa0f7430ad8) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ControllerRevision.lean](lean-declarations/learning.md#module-8763b069f801) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [CopyingCorrection.lean](lean-declarations/ethics.md#module-3f41827ba132) | 规范根据与生成方向 / Normative grounding and generative direction |
| [CopyingRegistration.lean](lean-declarations/ethics.md#module-250d62f8722f) | 规范根据与生成方向 / Normative grounding and generative direction |
| [CorePredication.lean](lean-declarations/core.md#module-361d0be23e0b) | 生成核心与关系结构 / Generative core and relational structure |
| [CoreTreeRearticulation.lean](lean-declarations/inquiry.md#module-2bcbeddc6d03) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [CorrectionBoundary.lean](lean-declarations/ethics.md#module-e43bea25e92f) | 规范根据与生成方向 / Normative grounding and generative direction |
| [CorrectionCommitment.lean](lean-declarations/other.md#module-a70b634f6f54) | 其他形式研究 / Other formal studies |
| [CorrectionDependence.lean](lean-declarations/other.md#module-a012353738fe) | 其他形式研究 / Other formal studies |
| [CorrectionHandoff.lean](lean-declarations/ethics.md#module-f4b3ebe0c538) | 规范根据与生成方向 / Normative grounding and generative direction |
| [CorrectionInfrastructure.lean](lean-declarations/ethics.md#module-15398df58657) | 规范根据与生成方向 / Normative grounding and generative direction |
| [CorrectionInquiry.lean](lean-declarations/ethics.md#module-3f189efe678b) | 规范根据与生成方向 / Normative grounding and generative direction |
| [CorrectionParent.lean](lean-declarations/ethics.md#module-5b8cfb23b422) | 规范根据与生成方向 / Normative grounding and generative direction |
| [CorrectionPopulation.lean](lean-declarations/ethics.md#module-f166c416f0d3) | 规范根据与生成方向 / Normative grounding and generative direction |
| [CorrectionRace.lean](lean-declarations/ethics.md#module-c849cace5619) | 规范根据与生成方向 / Normative grounding and generative direction |
| [CorrectionReconfiguration.lean](lean-declarations/ethics.md#module-58bd7df0390c) | 规范根据与生成方向 / Normative grounding and generative direction |
| [CorrectionReconfigurationCases.lean](lean-declarations/ethics.md#module-dfe580c928e4) | 规范根据与生成方向 / Normative grounding and generative direction |
| [CorrectionRelations.lean](lean-declarations/ethics.md#module-3c1f88c432ea) | 规范根据与生成方向 / Normative grounding and generative direction |
| [CorrectionVersioned.lean](lean-declarations/ethics.md#module-a719f0256b8b) | 规范根据与生成方向 / Normative grounding and generative direction |
| [Correspondence.lean](lean-declarations/core.md#module-66b60f528dff) | 生成核心与关系结构 / Generative core and relational structure |
| [CorrespondenceSamples.lean](lean-declarations/ethics.md#module-059498ea4742) | 规范根据与生成方向 / Normative grounding and generative direction |
| [CoupledConcernHistory.lean](lean-declarations/concern.md#module-8c7efefb404f) | 关切与共同活动 / Concern and shared activity |
| [CoupledOccurrence.lean](lean-declarations/core.md#module-9f09dc9dc6b1) | 生成核心与关系结构 / Generative core and relational structure |
| [CouplingOptima.lean](lean-declarations/abstraction.md#module-ad36cb089189) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [CoverageBoundary.lean](lean-declarations/abstraction.md#module-83c27fd36c83) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [CoverageBoundary.lean](lean-declarations/abstraction.md#module-e839ddaa98f9) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [CrossedClaims.lean](lean-declarations/ethics.md#module-e7f0db783db0) | 规范根据与生成方向 / Normative grounding and generative direction |
| [CutCoverageAudit.lean](lean-declarations/ethics.md#module-17d9a609f504) | 规范根据与生成方向 / Normative grounding and generative direction |
| [DeductiveNecessity.lean](lean-declarations/core.md#module-ad4338bdc8a0) | 生成核心与关系结构 / Generative core and relational structure |
| [DenseOrder.lean](lean-declarations/abstraction.md#module-8080157d8373) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [Dependence.lean](lean-declarations/core.md#module-be65fab29fa3) | 生成核心与关系结构 / Generative core and relational structure |
| [DependenceWarrant.lean](lean-declarations/core.md#module-7367fd620ac4) | 生成核心与关系结构 / Generative core and relational structure |
| [DependentCompletion.lean](lean-declarations/abstraction.md#module-363e3103ce55) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [Depletion.lean](lean-declarations/core.md#module-5391ff34d63c) | 生成核心与关系结构 / Generative core and relational structure |
| [DerivedHistoryLaw.lean](lean-declarations/core.md#module-c281ed691c55) | 生成核心与关系结构 / Generative core and relational structure |
| [DerivedInquiryCertificates.lean](lean-declarations/inquiry.md#module-c250dc5a85ef) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [DevelopmentalAssociation.lean](lean-declarations/ethics.md#module-73961f76a466) | 规范根据与生成方向 / Normative grounding and generative direction |
| [DevelopmentalMemory.lean](lean-declarations/ethics.md#module-8d5a4d8f682e) | 规范根据与生成方向 / Normative grounding and generative direction |
| [DevelopmentalReconstruction.lean](lean-declarations/ethics.md#module-9d89d2b46f4e) | 规范根据与生成方向 / Normative grounding and generative direction |
| [DiagnosticTracking.lean](lean-declarations/learning.md#module-000cb4a6ef8b) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [DriftMargins.lean](lean-declarations/ethics.md#module-3d946731f17f) | 规范根据与生成方向 / Normative grounding and generative direction |
| [Driver.lean](lean-declarations/other.md#module-db86581947bf) | 其他形式研究 / Other formal studies |
| [DynamicClassification.lean](lean-declarations/core.md#module-b7c8638a14c9) | 生成核心与关系结构 / Generative core and relational structure |
| [DynamicConsequences.lean](lean-declarations/core.md#module-bf65a1ee68e5) | 生成核心与关系结构 / Generative core and relational structure |
| [DynamicSymmetry.lean](lean-declarations/core.md#module-d33bc0ead9a9) | 生成核心与关系结构 / Generative core and relational structure |
| [DynamicUnderdetermination.lean](lean-declarations/core.md#module-9120ff48313a) | 生成核心与关系结构 / Generative core and relational structure |
| [EffectiveCommand.lean](lean-declarations/ethics.md#module-9940a4c4d9be) | 规范根据与生成方向 / Normative grounding and generative direction |
| [EmbeddedEvaluation.lean](lean-declarations/core.md#module-ce2fc7445eba) | 生成核心与关系结构 / Generative core and relational structure |
| [EmbodiedChoiceScales.lean](lean-declarations/learning.md#module-6883a5aecb08) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [EmissionArchive.lean](lean-declarations/shared.md#module-4ee9e7930d43) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [EnactedFoundation.lean](lean-declarations/core.md#module-24a83486a8c5) | 生成核心与关系结构 / Generative core and relational structure |
| [EnactedOrientation.lean](lean-declarations/core.md#module-7587315c346a) | 生成核心与关系结构 / Generative core and relational structure |
| [EnactedScene.lean](lean-declarations/inquiry.md#module-79f5d61b66c6) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [EncounterChoice.lean](lean-declarations/inquiry.md#module-130b052828c4) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [Enumeration.lean](lean-declarations/shared.md#module-2aa3f81f3ba3) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [EqualityGenerativity.lean](lean-declarations/abstraction.md#module-475eb20715c8) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [EthicalOrientation.lean](lean-declarations/core.md#module-b65d39fd3ece) | 生成核心与关系结构 / Generative core and relational structure |
| [Evaluate.lean](lean-declarations/learning.md#module-95295e365c1b) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [EvaluationPreparation.lean](lean-declarations/shared.md#module-29ef86360e74) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [EvaluationWitness.lean](lean-declarations/shared.md#module-121ae848f6c7) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [EvaluativeExtension.lean](lean-declarations/ethics.md#module-3b1ffb21fd90) | 规范根据与生成方向 / Normative grounding and generative direction |
| [EvaluativeSuccession.lean](lean-declarations/shared.md#module-d6e11394f125) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [EvaluatorGrounding.lean](lean-declarations/ethics.md#module-dc7f1c8b5d8f) | 规范根据与生成方向 / Normative grounding and generative direction |
| [EvidenceQualifiedCorrection.lean](lean-declarations/ethics.md#module-0fcc117b8f45) | 规范根据与生成方向 / Normative grounding and generative direction |
| [EvidenceQualifiedCorrectionCases.lean](lean-declarations/ethics.md#module-69599ee1af2c) | 规范根据与生成方向 / Normative grounding and generative direction |
| [EvidenceThroughChange.lean](lean-declarations/learning.md#module-820a29505426) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [EvolutionNetworkComparison.lean](lean-declarations/ethics.md#module-cf3461057237) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ExpandingInquiry.lean](lean-declarations/other.md#module-1f53d52a1db7) | 其他形式研究 / Other formal studies |
| [ExplanationDischarge.lean](lean-declarations/core.md#module-dfc447302a8a) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryBranching.lean](lean-declarations/core.md#module-e5671e89c1e5) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryBranchingRecovery.lean](lean-declarations/core.md#module-a29f77541ee1) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryBranchingWitnesses.lean](lean-declarations/core.md#module-1516c889059c) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryCardinalityWall.lean](lean-declarations/core.md#module-f6042e68e148) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryChangingSupport.lean](lean-declarations/core.md#module-b22618b13d23) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryCoexistence.lean](lean-declarations/core.md#module-3be3cd9cd665) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryCompactness.lean](lean-declarations/core.md#module-bf27fa3e64c9) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryComposition.lean](lean-declarations/core.md#module-b46b66e23e22) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryContextualStructure.lean](lean-declarations/core.md#module-c5245648bf54) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryCrossBranch.lean](lean-declarations/core.md#module-07e31405bb53) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryDeterminism.lean](lean-declarations/core.md#module-1e87d2b39729) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryFiniteLogic.lean](lean-declarations/core.md#module-d16633306c7c) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryFootprints.lean](lean-declarations/core.md#module-fd27f39f168c) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryGranularity.lean](lean-declarations/core.md#module-a10ca44c717e) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryGranularityBoundary.lean](lean-declarations/core.md#module-d96a0ab07e41) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryGuardedPrograms.lean](lean-declarations/core.md#module-b2b10a251ed8) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryHistoryInterfaces.lean](lean-declarations/core.md#module-30511ba1bfe5) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryInfiniteBranches.lean](lean-declarations/core.md#module-1adaf59f3185) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryInquiry.lean](lean-declarations/core.md#module-3e255b443ce9) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryJoining.lean](lean-declarations/core.md#module-a2d2a5eae5da) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryJoiningAnchors.lean](lean-declarations/core.md#module-72eb8e63e979) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryJoiningBranchWitnesses.lean](lean-declarations/core.md#module-f5c0fda732e0) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryJoiningBranches.lean](lean-declarations/core.md#module-8bda97ce9ae4) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryJoiningContexts.lean](lean-declarations/core.md#module-769a5201bf7b) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryJoiningIncidence.lean](lean-declarations/core.md#module-18f2f6c6cd8b) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryJoiningRefinement.lean](lean-declarations/core.md#module-265da669f721) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryJoiningRegisters.lean](lean-declarations/core.md#module-c9449a4a2cad) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryJointness.lean](lean-declarations/core.md#module-940320426d91) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryLeaseDynamics.lean](lean-declarations/core.md#module-fd2e261c798f) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryLocalUnits.lean](lean-declarations/core.md#module-2235ab0cf564) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryMinimalModels.lean](lean-declarations/core.md#module-04b4f85e40e2) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryNecessity.lean](lean-declarations/core.md#module-ae44dee8907f) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryRecovery.lean](lean-declarations/core.md#module-9d927046c19b) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryResiduals.lean](lean-declarations/core.md#module-48a98ab19ca2) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryResumptionCases.lean](lean-declarations/core.md#module-1b6833c3a4dc) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatorySharedSupport.lean](lean-declarations/core.md#module-1f631dbda9d8) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryStablePlans.lean](lean-declarations/core.md#module-78c185bc3691) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryStructure.lean](lean-declarations/core.md#module-6e9096f515bb) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatorySupportChanges.lean](lean-declarations/core.md#module-67758983e418) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryUniqueness.lean](lean-declarations/core.md#module-76b3782b28d0) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryUniversality.lean](lean-declarations/core.md#module-4855cfaa50f3) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplanatoryVariation.lean](lean-declarations/core.md#module-299212693cfe) | 生成核心与关系结构 / Generative core and relational structure |
| [ExplorationAudit.lean](lean-declarations/valuation.md#module-bd4702a9521f) | 评价的形成与良知 / Valuation development and liangzhi |
| [ExplorationCoverage.lean](lean-declarations/valuation.md#module-793ac042ad50) | 评价的形成与良知 / Valuation development and liangzhi |
| [Exposure.lean](lean-declarations/learning.md#module-4d87e1bfa317) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ExposureExamples.lean](lean-declarations/learning.md#module-0882888ab9e6) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [FallibleInspection.lean](lean-declarations/ethics.md#module-5bd737f24e3d) | 规范根据与生成方向 / Normative grounding and generative direction |
| [FallibleInspectionCases.lean](lean-declarations/ethics.md#module-87e5bdd67433) | 规范根据与生成方向 / Normative grounding and generative direction |
| [FamilyAdmission.lean](lean-declarations/abstraction.md#module-f0533e96feaa) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [FaultTolerantCorrection.lean](lean-declarations/ethics.md#module-a06a1493760d) | 规范根据与生成方向 / Normative grounding and generative direction |
| [FaultTolerantCorrectionCases.lean](lean-declarations/ethics.md#module-b9ae5b1bfe94) | 规范根据与生成方向 / Normative grounding and generative direction |
| [FeedbackDynamics.lean](lean-declarations/learning.md#module-95c70a079b33) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [FeedbackExamples.lean](lean-declarations/learning.md#module-0db80602d519) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [FeedbackMemory.lean](lean-declarations/learning.md#module-9889c88e9097) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [FiniteAdmission.lean](lean-declarations/abstraction.md#module-910666c286d1) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [FiniteBranching.lean](lean-declarations/abstraction.md#module-5f36470a468d) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [FiniteExposureKernel.lean](lean-declarations/learning.md#module-be5433d0f096) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [FiniteInquiryClassification.lean](lean-declarations/inquiry.md#module-13aee3c0e811) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [FiniteSupportObstruction.lean](lean-declarations/other.md#module-805a098f4dbd) | 其他形式研究 / Other formal studies |
| [Flow.lean](lean-declarations/core.md#module-1ab3e6b83532) | 生成核心与关系结构 / Generative core and relational structure |
| [FormationAccounts.lean](lean-declarations/shared.md#module-411df828cbbe) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [FormationClosure.lean](lean-declarations/inquiry.md#module-d330223ee429) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [FormationDraw.lean](lean-declarations/inquiry.md#module-1d28de9ca37e) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [FormationProfileGap.lean](lean-declarations/core.md#module-a1e891dfb22a) | 生成核心与关系结构 / Generative core and relational structure |
| [FormationRoot.lean](lean-declarations/shared.md#module-3599c054bffb) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [FormationRoutes.lean](lean-declarations/ethics.md#module-43eea8d884d9) | 规范根据与生成方向 / Normative grounding and generative direction |
| [FormationSequence.lean](lean-declarations/inquiry.md#module-3fd7ebdfc2c8) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [FormationSupport.lean](lean-declarations/learning.md#module-4716569d13e3) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [FormationSymmetry.lean](lean-declarations/core.md#module-544692f23ec3) | 生成核心与关系结构 / Generative core and relational structure |
| [FormativeAssessment.lean](lean-declarations/ethics.md#module-d9e9be1e54b4) | 规范根据与生成方向 / Normative grounding and generative direction |
| [FormativeCapacity.lean](lean-declarations/ethics.md#module-baa982e92c5c) | 规范根据与生成方向 / Normative grounding and generative direction |
| [FormedContactCycle.lean](lean-declarations/inquiry.md#module-b5e59468402d) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [FormedEffectiveLaw.lean](lean-declarations/core.md#module-db7a635d4102) | 生成核心与关系结构 / Generative core and relational structure |
| [FormedGrounds.lean](lean-declarations/ethics.md#module-f52bdfa0e6d5) | 规范根据与生成方向 / Normative grounding and generative direction |
| [FormedRecipientRoute.lean](lean-declarations/shared.md#module-3d3e3f859742) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [FormedRouteMonitor.lean](lean-declarations/shared.md#module-e00c807b1ad5) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [FormedSelection.lean](lean-declarations/shared.md#module-c9712e044702) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [FormedUnfoldingPreservation.lean](lean-declarations/core.md#module-a72842bcdb02) | 生成核心与关系结构 / Generative core and relational structure |
| [Frame.lean](lean-declarations/core.md#module-4aeb3fe7fb22) | 生成核心与关系结构 / Generative core and relational structure |
| [FreshRevision.lean](lean-declarations/shared.md#module-b592dcce60e2) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [FulfillmentStatus.lean](lean-declarations/shared.md#module-641fa8f3ad8b) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [FunctionGraphs.lean](lean-declarations/abstraction.md#module-967f5a53d7df) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [GeneratedContraction.lean](lean-declarations/core.md#module-e17df05af34f) | 生成核心与关系结构 / Generative core and relational structure |
| [GeneratedPaths.lean](lean-declarations/core.md#module-553e96448b89) | 生成核心与关系结构 / Generative core and relational structure |
| [GeneratedSelectionRecurrence.lean](lean-declarations/ethics.md#module-c93091b64bb3) | 规范根据与生成方向 / Normative grounding and generative direction |
| [GeneratedSelectionRecurrenceAudit.lean](lean-declarations/ethics.md#module-5cbb4bf4d015) | 规范根据与生成方向 / Normative grounding and generative direction |
| [GeneratedSelf.lean](lean-declarations/core.md#module-134b1f2adf22) | 生成核心与关系结构 / Generative core and relational structure |
| [Generation.lean](lean-declarations/core.md#module-b20d97b0f1ca) | 生成核心与关系结构 / Generative core and relational structure |
| [GenerativeAcquisitionModel.lean](lean-declarations/core.md#module-397cba8558f3) | 生成核心与关系结构 / Generative core and relational structure |
| [GenerativeApplicabilityModel.lean](lean-declarations/core.md#module-dacf46897484) | 生成核心与关系结构 / Generative core and relational structure |
| [GenerativeAttainableQuestionsModel.lean](lean-declarations/core.md#module-30e0c1945168) | 生成核心与关系结构 / Generative core and relational structure |
| [GenerativeClosure.lean](lean-declarations/inquiry.md#module-65653909d167) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [GenerativeComparison.lean](lean-declarations/ethics.md#module-11e52688dd69) | 规范根据与生成方向 / Normative grounding and generative direction |
| [GenerativeCore.lean](lean-declarations/core.md#module-2037f4728c54) | 生成核心与关系结构 / Generative core and relational structure |
| [GenerativeCoreTreeModel.lean](lean-declarations/core.md#module-84b1af41159f) | 生成核心与关系结构 / Generative core and relational structure |
| [GenerativeDerivedInquiryModel.lean](lean-declarations/core.md#module-297b8aa25c96) | 生成核心与关系结构 / Generative core and relational structure |
| [GenerativeDerivedProcessLawModel.lean](lean-declarations/core.md#module-b06485816105) | 生成核心与关系结构 / Generative core and relational structure |
| [GenerativeEpisode.lean](lean-declarations/learning.md#module-af3f1bb8d6b0) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [GenerativeFiniteInquiryModel.lean](lean-declarations/core.md#module-bbc901198634) | 生成核心与关系结构 / Generative core and relational structure |
| [GenerativeInquirySufficiencyModel.lean](lean-declarations/core.md#module-8333667afeda) | 生成核心与关系结构 / Generative core and relational structure |
| [GenerativeLossComparison.lean](lean-declarations/ethics.md#module-13036549ff30) | 规范根据与生成方向 / Normative grounding and generative direction |
| [GenerativeModel.lean](lean-declarations/core.md#module-80ce38721561) | 生成核心与关系结构 / Generative core and relational structure |
| [GenerativeNondualApplicabilityModel.lean](lean-declarations/core.md#module-079187adad93) | 生成核心与关系结构 / Generative core and relational structure |
| [GenerativeNondualModel.lean](lean-declarations/core.md#module-f54f1ad37a73) | 生成核心与关系结构 / Generative core and relational structure |
| [GenerativeOutcomeModel.lean](lean-declarations/core.md#module-9bfdebaabb96) | 生成核心与关系结构 / Generative core and relational structure |
| [GenerativePossibility.lean](lean-declarations/inquiry.md#module-83966662a245) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [GenerativePretrainingEvidenceModel.lean](lean-declarations/core.md#module-4060750330ef) | 生成核心与关系结构 / Generative core and relational structure |
| [GenerativeReceiptModel.lean](lean-declarations/core.md#module-30a35bdbf29f) | 生成核心与关系结构 / Generative core and relational structure |
| [GenerativeReconstructionRequirement.lean](lean-declarations/core.md#module-3c5f14232e3d) | 生成核心与关系结构 / Generative core and relational structure |
| [GenerativeRepairApplicability.lean](lean-declarations/core.md#module-b3c94256a1e8) | 生成核心与关系结构 / Generative core and relational structure |
| [GenerativeTradeoff.lean](lean-declarations/ethics.md#module-f873326b0c16) | 规范根据与生成方向 / Normative grounding and generative direction |
| [GoalFormationRevision.lean](lean-declarations/ethics.md#module-ff21cbcb9ba5) | 规范根据与生成方向 / Normative grounding and generative direction |
| [GoalRevision.lean](lean-declarations/ethics.md#module-36fc17b34d9c) | 规范根据与生成方向 / Normative grounding and generative direction |
| [GroundRelationTransport.lean](lean-declarations/core.md#module-e5e3937cc286) | 生成核心与关系结构 / Generative core and relational structure |
| [GroundingContract.lean](lean-declarations/concern.md#module-618302908b9f) | 关切与共同活动 / Concern and shared activity |
| [GrownFragmentation.lean](lean-declarations/ethics.md#module-93d3383fc37b) | 规范根据与生成方向 / Normative grounding and generative direction |
| [HistoricalBinding.lean](lean-declarations/inquiry.md#module-b3efe142595e) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [HistoryIdeals.lean](lean-declarations/abstraction.md#module-81928aacbe61) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [HistoryRealization.lean](lean-declarations/core.md#module-a7d9b0de6d97) | 生成核心与关系结构 / Generative core and relational structure |
| [Horizon.lean](lean-declarations/core.md#module-35179900d759) | 生成核心与关系结构 / Generative core and relational structure |
| [IdealWarrant.lean](lean-declarations/abstraction.md#module-e3abf1a9ab66) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [IndexedAssembly.lean](lean-declarations/abstraction.md#module-e1734fcd36ac) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [InductiveDomain.lean](lean-declarations/abstraction.md#module-c3d844e3d579) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [InferentialGrounds.lean](lean-declarations/core.md#module-f095b77a83ef) | 生成核心与关系结构 / Generative core and relational structure |
| [InferentialSubstitution.lean](lean-declarations/core.md#module-a2c391c148f3) | 生成核心与关系结构 / Generative core and relational structure |
| [Initiality.lean](lean-declarations/abstraction.md#module-831623a203ba) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [Inquiry.lean](lean-declarations/core.md#module-3d9eabbfea95) | 生成核心与关系结构 / Generative core and relational structure |
| [InquiryAdequacy.lean](lean-declarations/inquiry.md#module-3e204b02af5f) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [InquiryChoice.lean](lean-declarations/learning.md#module-93cab8a6e1fc) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [InquiryFamilies.lean](lean-declarations/inquiry.md#module-bfb389247e8c) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [InquiryJudgment.lean](lean-declarations/learning.md#module-3dd125e34817) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [InquiryRelevance.lean](lean-declarations/abstraction.md#module-102e6587264a) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [InquiryRevision.lean](lean-declarations/shared.md#module-df65151201cb) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [InquirySufficiency.lean](lean-declarations/inquiry.md#module-8f3efb8aecfe) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [InquiryWarrant.lean](lean-declarations/abstraction.md#module-162f3791d24f) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [InspectionPreparation.lean](lean-declarations/shared.md#module-42569f077f11) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [InspectionWitness.lean](lean-declarations/shared.md#module-3ca0f0fbccd6) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [IntegratedPortContinuation.lean](lean-declarations/inquiry.md#module-9e3c69c03ebf) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [Joint.lean](lean-declarations/core.md#module-ccc97cebe0aa) | 生成核心与关系结构 / Generative core and relational structure |
| [JointContinuation.lean](lean-declarations/learning.md#module-9bafeaa2c9e5) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [JointContinuationClassification.lean](lean-declarations/ethics.md#module-2c0028cc241e) | 规范根据与生成方向 / Normative grounding and generative direction |
| [JointInterpretation.lean](lean-declarations/inquiry.md#module-6bb6c519ec52) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [JointPracticeContinuation.lean](lean-declarations/ethics.md#module-4909b1cdd611) | 规范根据与生成方向 / Normative grounding and generative direction |
| [JointRiskRevision.lean](lean-declarations/ethics.md#module-bc23aff7b162) | 规范根据与生成方向 / Normative grounding and generative direction |
| [KeptSupport.lean](lean-declarations/abstraction.md#module-c764abc871d9) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [KitchenTransitions.lean](lean-declarations/ethics.md#module-74df76c70b6e) | 规范根据与生成方向 / Normative grounding and generative direction |
| [KnowledgeCorrespondence.lean](lean-declarations/inquiry.md#module-3c2658ad7582) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [LearnedProcedureTransmission.lean](lean-declarations/ethics.md#module-314ffd0b4f8a) | 规范根据与生成方向 / Normative grounding and generative direction |
| [LegacyReconciliation.lean](lean-declarations/other.md#module-b662dec55785) | 其他形式研究 / Other formal studies |
| [LifecycleCorrespondence.lean](lean-declarations/ethics.md#module-5beb4a64d4f6) | 规范根据与生成方向 / Normative grounding and generative direction |
| [LineageAudit.lean](lean-declarations/valuation.md#module-7d1b924b40d2) | 评价的形成与良知 / Valuation development and liangzhi |
| [LineageInProcess.lean](lean-declarations/valuation.md#module-45b450e65721) | 评价的形成与良知 / Valuation development and liangzhi |
| [LivingAllocation.lean](lean-declarations/ethics.md#module-ffc7d48f4c9c) | 规范根据与生成方向 / Normative grounding and generative direction |
| [LivingExpansion.lean](lean-declarations/ethics.md#module-707a08ce1476) | 规范根据与生成方向 / Normative grounding and generative direction |
| [LivingOrganization.lean](lean-declarations/ethics.md#module-a48e0f306c41) | 规范根据与生成方向 / Normative grounding and generative direction |
| [LivingRealization.lean](lean-declarations/ethics.md#module-90135b67b58c) | 规范根据与生成方向 / Normative grounding and generative direction |
| [LivingRecovery.lean](lean-declarations/ethics.md#module-37187272c431) | 规范根据与生成方向 / Normative grounding and generative direction |
| [MaintenanceBaseline.lean](lean-declarations/ethics.md#module-878f7de6ea2c) | 规范根据与生成方向 / Normative grounding and generative direction |
| [MarketDiagnosis.lean](lean-declarations/other.md#module-e2732406feff) | 其他形式研究 / Other formal studies |
| [MarketGenerativity.lean](lean-declarations/other.md#module-e2e5c347dc5a) | 其他形式研究 / Other formal studies |
| [MaterialMaturation.lean](lean-declarations/ethics.md#module-e4e9dd7ab622) | 规范根据与生成方向 / Normative grounding and generative direction |
| [MeasuredFeedback.lean](lean-declarations/learning.md#module-99c139232337) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [MediatedControl.lean](lean-declarations/ethics.md#module-4c7d0d4a2005) | 规范根据与生成方向 / Normative grounding and generative direction |
| [MediatedControlCases.lean](lean-declarations/ethics.md#module-16a5176f00b8) | 规范根据与生成方向 / Normative grounding and generative direction |
| [Metaethics.lean](lean-declarations/core.md#module-f7356ff23b30) | 生成核心与关系结构 / Generative core and relational structure |
| [ModelRevision.lean](lean-declarations/inquiry.md#module-a4bb88f1170d) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [ModelRevisionCases.lean](lean-declarations/inquiry.md#module-f1251e5ef2f2) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [MutualGrounding.lean](lean-declarations/core.md#module-a9df0fda7b92) | 生成核心与关系结构 / Generative core and relational structure |
| [NativePacketCases.lean](lean-declarations/inquiry.md#module-08a4b3aa7401) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [NativePacketProcess.lean](lean-declarations/inquiry.md#module-a594aff718eb) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [NativePortContinuation.lean](lean-declarations/renewal.md#module-948079a4c2d6) | 支持与更新 / Support and renewal |
| [NaturalismIdentity.lean](lean-declarations/core.md#module-3a02a4d6964b) | 生成核心与关系结构 / Generative core and relational structure |
| [NaturalismReview.lean](lean-declarations/core.md#module-063fe108d1e9) | 生成核心与关系结构 / Generative core and relational structure |
| [NewPossibilities.lean](lean-declarations/core.md#module-9de73e2b4f95) | 生成核心与关系结构 / Generative core and relational structure |
| [NondualConcernAdapter.lean](lean-declarations/concern.md#module-fcb630ff99c3) | 关切与共同活动 / Concern and shared activity |
| [NondualCore.lean](lean-declarations/core.md#module-3efe43e1116b) | 生成核心与关系结构 / Generative core and relational structure |
| [NondualFormation.lean](lean-declarations/concern.md#module-ddda3346b696) | 关切与共同活动 / Concern and shared activity |
| [NormativeActivity.lean](lean-declarations/ethics.md#module-126536960f5f) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ObservableContinuation.lean](lean-declarations/ethics.md#module-ad8769b9a4e0) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ObservationChange.lean](lean-declarations/ethics.md#module-dd0c4de5f1f1) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ObservationRepair.lean](lean-declarations/ethics.md#module-4270f08ac594) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ObservationalCompatibility.lean](lean-declarations/inquiry.md#module-0118ea5a9e23) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [OddsEnvelope.lean](lean-declarations/concern.md#module-f809c3938a43) | 关切与共同活动 / Concern and shared activity |
| [OfferedChoiceBounds.lean](lean-declarations/concern.md#module-9b9421d95d90) | 关切与共同活动 / Concern and shared activity |
| [OnePacketAdmissibility.lean](lean-declarations/inquiry.md#module-fa2ef58e134e) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [OnePacketInquirySynthesis.lean](lean-declarations/inquiry.md#module-8c13eaf34b78) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [OnePacketQuestions.lean](lean-declarations/inquiry.md#module-e5043c6b7615) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [OneProcess.lean](lean-declarations/valuation.md#module-a454cc03f2a3) | 评价的形成与良知 / Valuation development and liangzhi |
| [OneProcessAudit.lean](lean-declarations/valuation.md#module-297e01080273) | 评价的形成与良知 / Valuation development and liangzhi |
| [OpenFutureRevision.lean](lean-declarations/ethics.md#module-a5f26298589c) | 规范根据与生成方向 / Normative grounding and generative direction |
| [OperationRoles.lean](lean-declarations/core.md#module-9f4103888949) | 生成核心与关系结构 / Generative core and relational structure |
| [OperativeCoherence.lean](lean-declarations/core.md#module-9712b4ea2312) | 生成核心与关系结构 / Generative core and relational structure |
| [OrganizationalRuleInheritance.lean](lean-declarations/ethics.md#module-d6cdb351c744) | 规范根据与生成方向 / Normative grounding and generative direction |
| [OrganizedScaleLoop.lean](lean-declarations/learning.md#module-fa24e61409c5) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [OutcomeContinuation.lean](lean-declarations/core.md#module-c48ee824a0b3) | 生成核心与关系结构 / Generative core and relational structure |
| [PacketLawDerivation.lean](lean-declarations/inquiry.md#module-db5cafd783d9) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PaidArchiveReader.lean](lean-declarations/shared.md#module-dacef2fbbee5) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [PaidPreImport.lean](lean-declarations/shared.md#module-72d53bbb0ddb) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [PaidRecipientReasons.lean](lean-declarations/shared.md#module-c2e841f7d5e2) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [PairedPlasticity.lean](lean-declarations/shared.md#module-0f653cfbf240) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [PartialRegimeTransition.lean](lean-declarations/other.md#module-5a3139fb2b49) | 其他形式研究 / Other formal studies |
| [PatientConcern.lean](lean-declarations/concern.md#module-5ad0b8e8fd94) | 关切与共同活动 / Concern and shared activity |
| [PendingTaskApplicability.lean](lean-declarations/other.md#module-2d39360c8f48) | 其他形式研究 / Other formal studies |
| [PeriodCostSelection.lean](lean-declarations/inquiry.md#module-e674e69e840d) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PeriodCoverData.lean](lean-declarations/inquiry.md#module-387fd4f713a6) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PeriodCoverRules.lean](lean-declarations/inquiry.md#module-6ff7a0fb4b87) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PeriodCycleWindows.lean](lean-declarations/inquiry.md#module-481cca4adb1f) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PeriodFirstRead.lean](lean-declarations/inquiry.md#module-1b33b1687419) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PeriodGeneralProof.lean](lean-declarations/inquiry.md#module-e7057b4e6834) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PeriodLocalCertificate.lean](lean-declarations/inquiry.md#module-417a0afb7f79) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PeriodPolicyCover.lean](lean-declarations/inquiry.md#module-e64a4afd9112) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PeriodPrunedCover.lean](lean-declarations/inquiry.md#module-419d3c52eb15) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PeriodStrategySemantics.lean](lean-declarations/inquiry.md#module-7e10a07fa760) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PeriodWindowPeriodicity.lean](lean-declarations/inquiry.md#module-bc23878b6dca) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PeriodWindowPruning.lean](lean-declarations/inquiry.md#module-7792c30d5fe3) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PhaseCycleDerivation.lean](lean-declarations/inquiry.md#module-3fd985dc0b59) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PhasePeriodSelection.lean](lean-declarations/inquiry.md#module-96e1d00a32d0) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PhasePeriodUniversal.lean](lean-declarations/inquiry.md#module-669a6ea433f9) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PhaseRecoveredContact.lean](lean-declarations/inquiry.md#module-b51b3a4c7541) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PlasticityPreparation.lean](lean-declarations/shared.md#module-c527ff17c751) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [PlasticityWitness.lean](lean-declarations/shared.md#module-ac933f076498) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [PluralRecords.lean](lean-declarations/abstraction.md#module-2a54e07465df) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [Population.lean](lean-declarations/core.md#module-161ef92f702e) | 生成核心与关系结构 / Generative core and relational structure |
| [PopulationCorrection.lean](lean-declarations/other.md#module-eb4d5a6069ec) | 其他形式研究 / Other formal studies |
| [PopulationRealization.lean](lean-declarations/other.md#module-dc65abdfa4be) | 其他形式研究 / Other formal studies |
| [PortAlignment.lean](lean-declarations/inquiry.md#module-7c982b0727b0) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PortDirectRenewal.lean](lean-declarations/inquiry.md#module-073ae3eb42fa) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PortRenewalBoundary.lean](lean-declarations/inquiry.md#module-c7210c591afe) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PortRenewalLawClosure.lean](lean-declarations/inquiry.md#module-5c50415006f1) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PortValuation.lean](lean-declarations/inquiry.md#module-e625c38f5208) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PositionedPositiveReason.lean](lean-declarations/ethics.md#module-04bd31edc270) | 规范根据与生成方向 / Normative grounding and generative direction |
| [PositiveGroundUncertainty.lean](lean-declarations/ethics.md#module-829cc0c15abc) | 规范根据与生成方向 / Normative grounding and generative direction |
| [PotentialTruth.lean](lean-declarations/abstraction.md#module-e847c1e507df) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [PracticalJudgment.lean](lean-declarations/ethics.md#module-dd511a3279d9) | 规范根据与生成方向 / Normative grounding and generative direction |
| [PracticalPriorityIdentification.lean](lean-declarations/ethics.md#module-414ae701c60c) | 规范根据与生成方向 / Normative grounding and generative direction |
| [PracticalReach.lean](lean-declarations/ethics.md#module-6930dfab71b1) | 规范根据与生成方向 / Normative grounding and generative direction |
| [PredictionAction.lean](lean-declarations/shared.md#module-ed1c7c0f33b2) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [PredictionOverlap.lean](lean-declarations/learning.md#module-3c954998b7e7) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [PredictionProtocolBridge.lean](lean-declarations/learning.md#module-63ccd209dc68) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [PredictionProtocolCompletion.lean](lean-declarations/learning.md#module-6e3dabe05d89) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [PredictionProtocolObservation.lean](lean-declarations/learning.md#module-befd3cdaff45) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [PrefixSafety.lean](lean-declarations/abstraction.md#module-ecba5d8a9232) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [PremiseNecessity.lean](lean-declarations/core.md#module-2c46d6d47a5c) | 生成核心与关系结构 / Generative core and relational structure |
| [PretrainingEvidence.lean](lean-declarations/shared.md#module-c09aabdc4749) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ProductTower.lean](lean-declarations/core.md#module-4d5adece21ab) | 生成核心与关系结构 / Generative core and relational structure |
| [ProtectedScope.lean](lean-declarations/core.md#module-734a8db29b35) | 生成核心与关系结构 / Generative core and relational structure |
| [ProtectedScopeLimits.lean](lean-declarations/core.md#module-a915d0fcaf85) | 生成核心与关系结构 / Generative core and relational structure |
| [ProtectionLedger.lean](lean-declarations/shared.md#module-b0831c6b108c) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ProtectionPriorityRival.lean](lean-declarations/ethics.md#module-042e89e0c377) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ProtocolCompletion.lean](lean-declarations/learning.md#module-6272b5e2fc0c) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ProtocolCompletionExamples.lean](lean-declarations/learning.md#module-0744fae15585) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ProtocolComposition.lean](lean-declarations/learning.md#module-3e53edd102e4) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ProtocolExamples.lean](lean-declarations/learning.md#module-45b8809c9dd8) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [PublicationBridge.lean](lean-declarations/shared.md#module-255a96b41300) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [PublicationBudget.lean](lean-declarations/shared.md#module-2c579a67c493) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [PublicationSafety.lean](lean-declarations/shared.md#module-946dd1d4cfb2) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [PurposeCorrection.lean](lean-declarations/concern.md#module-51689dfd2a2c) | 关切与共同活动 / Concern and shared activity |
| [PurposeCorrectionHistory.lean](lean-declarations/concern.md#module-41ff61a5ae5b) | 关切与共同活动 / Concern and shared activity |
| [Ranking.lean](lean-declarations/core.md#module-fbc6f2c56a91) | 生成核心与关系结构 / Generative core and relational structure |
| [ReachedInquiryComposition.lean](lean-declarations/inquiry.md#module-c8393ae20838) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [RealFeedback.lean](lean-declarations/learning.md#module-0a13f9949122) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ReasonPreparation.lean](lean-declarations/shared.md#module-817e5110d349) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ReasonProtection.lean](lean-declarations/shared.md#module-84e1d134b181) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ReasonReplay.lean](lean-declarations/shared.md#module-315e6988dc15) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ReasonReplayBridge.lean](lean-declarations/shared.md#module-edd06589e118) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ReceiptIdentification.lean](lean-declarations/learning.md#module-e047c3350dab) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ReceiptRevisionBoundary.lean](lean-declarations/learning.md#module-584b0a04b5d1) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [RecipeGrounding.lean](lean-declarations/abstraction.md#module-f3d19e548781) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [RecipeNative.lean](lean-declarations/abstraction.md#module-b95fad6c2723) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [RecipientAction.lean](lean-declarations/shared.md#module-142128063360) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RecipientArchive.lean](lean-declarations/shared.md#module-9d1b8fb5e31a) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RecipientContinuationProjection.lean](lean-declarations/core.md#module-6f0c8dfb5b4b) | 生成核心与关系结构 / Generative core and relational structure |
| [RecipientCorrection.lean](lean-declarations/shared.md#module-adaf58c1d9b6) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RecipientIdentification.lean](lean-declarations/shared.md#module-1c2d7eee36a8) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RecipientReasons.lean](lean-declarations/shared.md#module-2771495028b1) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RecognitionalBinding.lean](lean-declarations/core.md#module-e002789ce099) | 生成核心与关系结构 / Generative core and relational structure |
| [ReconfigurableRoutes.lean](lean-declarations/ethics.md#module-bec079c8bd79) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ReconfigurableSupportLogic.lean](lean-declarations/core.md#module-e808e49e4cf2) | 生成核心与关系结构 / Generative core and relational structure |
| [ReconfigurationCorrespondenceSamples.lean](lean-declarations/ethics.md#module-12ce623ea5ce) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ReconstructiveSelection.lean](lean-declarations/ethics.md#module-900bc4daaa41) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RecordedClaims.lean](lean-declarations/abstraction.md#module-33531476b412) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [RecordedEvidence.lean](lean-declarations/shared.md#module-d6edcd35ca09) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RecoverableControl.lean](lean-declarations/ethics.md#module-40ce621d7a4c) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RecoverableControlCases.lean](lean-declarations/ethics.md#module-7bfe2d0ea794) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RecoveryQuantum.lean](lean-declarations/inquiry.md#module-02ce03487a51) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [RecurrentAssembly.lean](lean-declarations/ethics.md#module-eb496cc7129c) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RecursiveGenerativeSelection.lean](lean-declarations/ethics.md#module-ecb2b467bd36) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RecursiveGenerativeSelectionAudit.lean](lean-declarations/ethics.md#module-002fc680ef8a) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RecursiveSelection.lean](lean-declarations/other.md#module-10f5394663dc) | 其他形式研究 / Other formal studies |
| [RecursiveSelectionInheritance.lean](lean-declarations/ethics.md#module-177504233211) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RecursiveSelectionInheritanceAudit.lean](lean-declarations/ethics.md#module-0f28a5ad9488) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ReflectiveIdentity.lean](lean-declarations/core.md#module-32c02c3969d5) | 生成核心与关系结构 / Generative core and relational structure |
| [ReformEvidence.lean](lean-declarations/ethics.md#module-9070992536ea) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ReformInquiry.lean](lean-declarations/ethics.md#module-9c685755d896) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RegeneratingPersistence.lean](lean-declarations/core.md#module-d8a479331a75) | 生成核心与关系结构 / Generative core and relational structure |
| [RegenerativeDiversity.lean](lean-declarations/ethics.md#module-fb7ea9229d0d) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RegimeAttraction.lean](lean-declarations/other.md#module-c03ef19c4e99) | 其他形式研究 / Other formal studies |
| [RegimeBoundary.lean](lean-declarations/other.md#module-e0e2fb3f4028) | 其他形式研究 / Other formal studies |
| [RegimeTransition.lean](lean-declarations/other.md#module-f1a05f3cb9c1) | 其他形式研究 / Other formal studies |
| [RelationalAssembly.lean](lean-declarations/abstraction.md#module-b1e9ae8b3572) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [RelationalBecoming.lean](lean-declarations/core.md#module-678ee419f096) | 生成核心与关系结构 / Generative core and relational structure |
| [RelationalContinuation.lean](lean-declarations/core.md#module-670551b8b671) | 生成核心与关系结构 / Generative core and relational structure |
| [RelationalCoordinates.lean](lean-declarations/core.md#module-aa4518e83400) | 生成核心与关系结构 / Generative core and relational structure |
| [RelationalCut.lean](lean-declarations/inquiry.md#module-8965a528dcb0) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [RelationalDynamics.lean](lean-declarations/core.md#module-af635c4a4144) | 生成核心与关系结构 / Generative core and relational structure |
| [RelationalFormation.lean](lean-declarations/core.md#module-cc558e834b61) | 生成核心与关系结构 / Generative core and relational structure |
| [RelationalGrounding.lean](lean-declarations/ethics.md#module-ce34aa667fa9) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RelationalOrganization.lean](lean-declarations/ethics.md#module-445bd184c5cb) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RelationalReduction.lean](lean-declarations/core.md#module-a366181ec98a) | 生成核心与关系结构 / Generative core and relational structure |
| [RelationalRenewal.lean](lean-declarations/core.md#module-bc794121a016) | 生成核心与关系结构 / Generative core and relational structure |
| [RelationsAcrossScales.lean](lean-declarations/learning.md#module-ba4d9be09079) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [RemainingDependency.lean](lean-declarations/abstraction.md#module-c1c11c83ec55) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [Renewal.lean](lean-declarations/core.md#module-122ecfb273f5) | 生成核心与关系结构 / Generative core and relational structure |
| [RenewalAccounting.lean](lean-declarations/renewal.md#module-b8df4e3120cc) | 支持与更新 / Support and renewal |
| [RenewalBasics.lean](lean-declarations/renewal.md#module-77ecd2c775da) | 支持与更新 / Support and renewal |
| [RenewalCharacterization.lean](lean-declarations/renewal.md#module-5fca0507b290) | 支持与更新 / Support and renewal |
| [RenewalClosure.lean](lean-declarations/renewal.md#module-35b608afeb1a) | 支持与更新 / Support and renewal |
| [RenewalComparison.lean](lean-declarations/core.md#module-72003943725b) | 生成核心与关系结构 / Generative core and relational structure |
| [RenewalConfigurations.lean](lean-declarations/renewal.md#module-a218916039de) | 支持与更新 / Support and renewal |
| [RenewalExamples.lean](lean-declarations/renewal.md#module-87b5bd85fd55) | 支持与更新 / Support and renewal |
| [RenewalLedger.lean](lean-declarations/shared.md#module-46a3e9d8b95a) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RenewalLink.lean](lean-declarations/renewal.md#module-28c0ce8386f8) | 支持与更新 / Support and renewal |
| [RenewalLiquidity.lean](lean-declarations/shared.md#module-a8de4892aa41) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RenewalPremises.lean](lean-declarations/renewal.md#module-8149a0ba6370) | 支持与更新 / Support and renewal |
| [RenewalRecovery.lean](lean-declarations/core.md#module-02c0f621db2a) | 生成核心与关系结构 / Generative core and relational structure |
| [RenewalSufficiency.lean](lean-declarations/renewal.md#module-c1beae045284) | 支持与更新 / Support and renewal |
| [RenewingFormation.lean](lean-declarations/ethics.md#module-0acdeff0007e) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ReproductionNetwork.lean](lean-declarations/other.md#module-6a029e611328) | 其他形式研究 / Other formal studies |
| [ReserveTurnover.lean](lean-declarations/shared.md#module-6fd1230f8bb2) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ReservedShutdown.lean](lean-declarations/ethics.md#module-3f4ac99220c0) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ReservedShutdownCases.lean](lean-declarations/ethics.md#module-9ec915dfe498) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ResourceContinuation.lean](lean-declarations/renewal.md#module-b17cc0c41017) | 支持与更新 / Support and renewal |
| [ResponseCapacity.lean](lean-declarations/other.md#module-fcd53f73ee36) | 其他形式研究 / Other formal studies |
| [Retention.lean](lean-declarations/shared.md#module-4ab19d4a2066) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RetrospectiveBinding.lean](lean-declarations/inquiry.md#module-048ae15d8789) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [Return.lean](lean-declarations/core.md#module-1725c50aac10) | 生成核心与关系结构 / Generative core and relational structure |
| [ReturnConditions.lean](lean-declarations/core.md#module-ae642c240be8) | 生成核心与关系结构 / Generative core and relational structure |
| [ReviewProbes.lean](lean-declarations/ethics.md#module-31bd0e5cd16a) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ReviewProbes2.lean](lean-declarations/ethics.md#module-8b3b0e656659) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ReviewProbes3.lean](lean-declarations/ethics.md#module-6fb445f778b8) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RevisingPort.lean](lean-declarations/inquiry.md#module-c215038e7e48) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [RevisionPreparation.lean](lean-declarations/shared.md#module-cd73453f54b6) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RevisionSuccession.lean](lean-declarations/shared.md#module-737754c24400) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RevisionWitness.lean](lean-declarations/shared.md#module-d03c440ac0b4) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RiskConditioning.lean](lean-declarations/ethics.md#module-bb2d76a79061) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RiskPriority.lean](lean-declarations/ethics.md#module-40a0f60d9f91) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RootBridge.lean](lean-declarations/shared.md#module-6ab582d74d00) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RootGrounding.lean](lean-declarations/concern.md#module-c86f0b363b70) | 关切与共同活动 / Concern and shared activity |
| [RootRealization.lean](lean-declarations/core.md#module-62ba3600c9f2) | 生成核心与关系结构 / Generative core and relational structure |
| [RouteDiagnostics.lean](lean-declarations/shared.md#module-6d5ab3eb998c) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RouteRevision.lean](lean-declarations/shared.md#module-39cee25a965f) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RoutesCorrespondenceSamples.lean](lean-declarations/ethics.md#module-b49c122e730b) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ScaleRevision.lean](lean-declarations/learning.md#module-dea38234acec) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ScientificCompatibility.lean](lean-declarations/inquiry.md#module-6fa299ebe0e7) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [ScientificInquiryNecessity.lean](lean-declarations/inquiry.md#module-a906d342f4df) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [SecondOrder.lean](lean-declarations/abstraction.md#module-438373a5bced) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [SeededContinuation.lean](lean-declarations/learning.md#module-37af2e7fffc1) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [SelectiveRevision.lean](lean-declarations/inquiry.md#module-2ce080a6f0f1) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [SelectiveRevisionCases.lean](lean-declarations/inquiry.md#module-c0729e377475) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [SelectorReviewCoverage.lean](lean-declarations/ethics.md#module-b21b443409bc) | 规范根据与生成方向 / Normative grounding and generative direction |
| [SelectorRevision.lean](lean-declarations/shared.md#module-d4766cfc350c) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [SelectorStructuralCoverage.lean](lean-declarations/ethics.md#module-02c1ed67561a) | 规范根据与生成方向 / Normative grounding and generative direction |
| [SelfModelCertification.lean](lean-declarations/shared.md#module-2633962036d2) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [SemanticAction.lean](lean-declarations/shared.md#module-a51c4566a005) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [SemanticCalibration.lean](lean-declarations/shared.md#module-ad79f81f6792) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [SettlingCorrespondence.lean](lean-declarations/ethics.md#module-4d312d4e9464) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ShrinkingGain.lean](lean-declarations/learning.md#module-59ffcfa61113) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [SignatureTruth.lean](lean-declarations/abstraction.md#module-aacdf65172d8) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [SituatedContinuation.lean](lean-declarations/ethics.md#module-4199e2843e06) | 规范根据与生成方向 / Normative grounding and generative direction |
| [SituatedKitchen.lean](lean-declarations/ethics.md#module-60d7e6c8c57d) | 规范根据与生成方向 / Normative grounding and generative direction |
| [SituatedPractice.lean](lean-declarations/concern.md#module-618b534f95cf) | 关切与共同活动 / Concern and shared activity |
| [SituatedRenewal.lean](lean-declarations/ethics.md#module-4c743231f0b3) | 规范根据与生成方向 / Normative grounding and generative direction |
| [SituatedTracking.lean](lean-declarations/learning.md#module-0484b39d8ec3) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [SourceReliance.lean](lean-declarations/inquiry.md#module-c6d60dbda60c) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [SourceRelianceCases.lean](lean-declarations/inquiry.md#module-ca0448c58a45) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [StandardsBridge.lean](lean-declarations/ethics.md#module-45a1fb24acce) | 规范根据与生成方向 / Normative grounding and generative direction |
| [StartingStock.lean](lean-declarations/inquiry.md#module-086d448b5bc8) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [StructuralCopying.lean](lean-declarations/ethics.md#module-558eaf1967e0) | 规范根据与生成方向 / Normative grounding and generative direction |
| [StructuralInheritance.lean](lean-declarations/ethics.md#module-e8a2cb3c9480) | 规范根据与生成方向 / Normative grounding and generative direction |
| [Substitution.lean](lean-declarations/core.md#module-5bdbdb6a34c0) | 生成核心与关系结构 / Generative core and relational structure |
| [SuccessionHistoryInterface.lean](lean-declarations/shared.md#module-6c08598bc18a) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [SuccessionPreparation.lean](lean-declarations/shared.md#module-0316e1fac3b9) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [SuccessionWitness.lean](lean-declarations/shared.md#module-d529bfeccc02) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [SuccessorLearning.lean](lean-declarations/shared.md#module-5dd8cb345fbf) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [SupportHandoff.lean](lean-declarations/shared.md#module-15a26dae9373) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [SupportNecessity.lean](lean-declarations/renewal.md#module-bedcaae2aaa8) | 支持与更新 / Support and renewal |
| [SupportedRevision.lean](lean-declarations/learning.md#module-ed748ff2bb5a) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [SurfaceSelection.lean](lean-declarations/ethics.md#module-b298a57e747a) | 规范根据与生成方向 / Normative grounding and generative direction |
| [SustainedJudgment.lean](lean-declarations/ethics.md#module-0fd5374df4b5) | 规范根据与生成方向 / Normative grounding and generative direction |
| [SymbolicDynamics.lean](lean-declarations/learning.md#module-0146a609b532) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [SystemIndividuation.lean](lean-declarations/core.md#module-237ec5d3745f) | 生成核心与关系结构 / Generative core and relational structure |
| [SystemsComplexity.lean](lean-declarations/learning.md#module-f2ed510fb44f) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [SystemsOrganization.lean](lean-declarations/learning.md#module-4a3c27c14d5e) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [TemporalInspection.lean](lean-declarations/ethics.md#module-ff1d36dd5eb5) | 规范根据与生成方向 / Normative grounding and generative direction |
| [TemporalInspectionCases.lean](lean-declarations/ethics.md#module-476a77b8af4b) | 规范根据与生成方向 / Normative grounding and generative direction |
| [TestingReorganization.lean](lean-declarations/other.md#module-e1b765e5997b) | 其他形式研究 / Other formal studies |
| [TieBreaking.lean](lean-declarations/abstraction.md#module-c67844003d2b) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [TimedFeedback.lean](lean-declarations/learning.md#module-d03f54c6bf35) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [TrajectoryFidelity.lean](lean-declarations/valuation.md#module-baf6d4d24a70) | 评价的形成与良知 / Valuation development and liangzhi |
| [TuningCorrespondence.lean](lean-declarations/learning.md#module-1745ec53c5aa) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [TypedRenewal.lean](lean-declarations/shared.md#module-04366373329a) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [TypedTruth.lean](lean-declarations/abstraction.md#module-77505a9c5a3f) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [UnequalBasicLosses.lean](lean-declarations/ethics.md#module-1e5c5fb9e755) | 规范根据与生成方向 / Normative grounding and generative direction |
| [UnfoldingPreservation.lean](lean-declarations/core.md#module-cc65e367cbd3) | 生成核心与关系结构 / Generative core and relational structure |
| [UpdaterConsequences.lean](lean-declarations/ethics.md#module-290c62292425) | 规范根据与生成方向 / Normative grounding and generative direction |
| [UpdaterFormation.lean](lean-declarations/shared.md#module-98344ea49fe4) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ValuationBridges.lean](lean-declarations/valuation.md#module-f496d68a278b) | 评价的形成与良知 / Valuation development and liangzhi |
| [ValuationCompletion.lean](lean-declarations/valuation.md#module-ff2eea4e63b0) | 评价的形成与良知 / Valuation development and liangzhi |
| [ValuationDevelopment.lean](lean-declarations/valuation.md#module-d23b7065be00) | 评价的形成与良知 / Valuation development and liangzhi |
| [ValuationInCore.lean](lean-declarations/inquiry.md#module-3c5f4e829425) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [ValuationRenewal.lean](lean-declarations/valuation.md#module-003faae288bf) | 评价的形成与良知 / Valuation development and liangzhi |
| [ValuationRenewalAudit.lean](lean-declarations/valuation.md#module-b05da0412da4) | 评价的形成与良知 / Valuation development and liangzhi |
| [VariationWarrant.lean](lean-declarations/core.md#module-ae18a32ad6d2) | 生成核心与关系结构 / Generative core and relational structure |
| [VaryingFeedback.lean](lean-declarations/learning.md#module-8300137fadf5) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [WholeGroundCoverage.lean](lean-declarations/ethics.md#module-386072b758e7) | 规范根据与生成方向 / Normative grounding and generative direction |
| [WholePortContinuation.lean](lean-declarations/inquiry.md#module-8eff53ffc111) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [WholePracticalRestriction.lean](lean-declarations/ethics.md#module-4271de674110) | 规范根据与生成方向 / Normative grounding and generative direction |
| [WholeQualityNaturalism.lean](lean-declarations/core.md#module-b4942b7409e4) | 生成核心与关系结构 / Generative core and relational structure |
| [WholeTheoryDischarge.lean](lean-declarations/inquiry.md#module-ca1aed5ff8a7) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [WisdomFallibleJudgment.lean](lean-declarations/core.md#module-782abba8ef08) | 生成核心与关系结构 / Generative core and relational structure |
| [WisdomGoalGrounds.lean](lean-declarations/ethics.md#module-3bd6cb85aa59) | 规范根据与生成方向 / Normative grounding and generative direction |
| [WisdomResponseStructure.lean](lean-declarations/core.md#module-25c8adeade56) | 生成核心与关系结构 / Generative core and relational structure |
| [WitnessHull.lean](lean-declarations/abstraction.md#module-72d18a9b2453) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
