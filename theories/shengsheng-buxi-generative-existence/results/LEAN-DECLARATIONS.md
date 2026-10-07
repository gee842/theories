# Lean 具名声明 / Named Lean declarations

[返回 Lean 导航](LEAN-INDEX.md)。本表显示当前工作源与审计入口；所有历史副本仍见 [JSON 清单](data/lean-index.json)。这是显式声明的位置索引，不能代替命题、假设及对应论证的阅读。 / [Return to navigation](LEAN-INDEX.md). Working sources and audit entries appear here; all historical copies remain in the JSON inventory. These are explicit declaration locations, not substitutes for statements, hypotheses and correspondence arguments.

定理／引理逐项列出；定义与类型声明列在同一模块的折叠项中。限定名由文本 namespace 推断，仅供导航；私有内部名称和自动生成名称以 Lean 为准。 / Theorems and lemmas are individually listed; definitions and type declarations share each module's foldout. Namespace-qualified names are textual hints; Lean determines private/internal and generated names.

## 按方向浏览 / Browse by topic

| 方向 / Topic | 模块／审计入口 / Entries | theorem/lemma 位置 / Occurrences |
|---|---:|---:|
| [规范根据与生成方向 / Normative grounding and generative direction](lean-declarations/ethics.md) | 24 | 314 |
| [评价的形成与良知 / Valuation development and liangzhi](lean-declarations/valuation.md) | 19 | 202 |
| [可达询问、接触与过程律 / Attainable inquiry, contact and process laws](lean-declarations/inquiry.md) | 48 | 1,473 |
| [支持与更新 / Support and renewal](lean-declarations/renewal.md) | 12 | 309 |
| [学习、预测与动力学 / Learning, prediction and dynamics](lean-declarations/learning.md) | 32 | 553 |
| [抽象、适用性与构成 / Abstraction, applicability and constitution](lean-declarations/abstraction.md) | 41 | 858 |
| [关切与共同活动 / Concern and shared activity](lean-declarations/concern.md) | 15 | 246 |
| [组织形成到可修正评价 / Organizational formation through revisable evaluation](lean-declarations/shared.md) | 67 | 1,501 |
| [生成核心与关系结构 / Generative core and relational structure](lean-declarations/core.md) | 50 | 536 |
| [其他形式研究 / Other formal studies](lean-declarations/other.md) | 1 | 39 |

## 按名称查找 / Find by name

各分组页可使用浏览器查找；编辑器的跨文件搜索可查全部名称。命令行可从仓库根运行： / Use browser find within a topic page or an editor's cross-file search for every name. From the repository root:

```sh
rg -n 'theorem_name' theories/shengsheng-buxi-generative-existence/results/lean-declarations/
```

## 模块清单 / Module list

| 模块 / Module | 方向 / Topic |
|---|---|
| [AcquiredActivityScope.lean](lean-declarations/concern.md#module-9a94f43dc79c) | 关切与共同活动 / Concern and shared activity |
| [AcquiredApplicability.lean](lean-declarations/abstraction.md#module-3a9468f07796) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [AcquiredContact.lean](lean-declarations/inquiry.md#module-16b45775dfc4) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [AcquiredEvaluation.lean](lean-declarations/shared.md#module-1f4b41b7b576) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [AcquiredInitiationConstraint.lean](lean-declarations/concern.md#module-078cf605a4ff) | 关切与共同活动 / Concern and shared activity |
| [AcquiredPerspective.lean](lean-declarations/core.md#module-469910b4b12f) | 生成核心与关系结构 / Generative core and relational structure |
| [AcquiredPredictionRecord.lean](lean-declarations/learning.md#module-e55152492e3a) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [AcquiredPurposeCriterion.lean](lean-declarations/concern.md#module-2f598ac2951f) | 关切与共同活动 / Concern and shared activity |
| [ActionPreparation.lean](lean-declarations/shared.md#module-c89e3d27ff4d) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ActionWitness.lean](lean-declarations/shared.md#module-1e9f6921303e) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ActualRecovery.lean](lean-declarations/core.md#module-6b8e6a0d66ac) | 生成核心与关系结构 / Generative core and relational structure |
| [AdaptiveCore.lean](lean-declarations/learning.md#module-c3234339b888) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [Admission.lean](lean-declarations/abstraction.md#module-d133a5ed4253) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [ApplicabilityGrounding.lean](lean-declarations/abstraction.md#module-3a59dae65c20) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [ApplicabilityProofs.lean](lean-declarations/abstraction.md#module-1c37938595ec) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [ApplicationEvidence.lean](lean-declarations/shared.md#module-dd170fb920e6) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ArchivePreparation.lean](lean-declarations/shared.md#module-f08c6d6875b6) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [AttainableQuestions.lean](lean-declarations/inquiry.md#module-eb7be2a9177f) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [Audit.lean](lean-declarations/valuation.md#module-037c0640f9e2) | 评价的形成与良知 / Valuation development and liangzhi |
| [Audit.lean](lean-declarations/valuation.md#module-6b4c32dcec82) | 评价的形成与良知 / Valuation development and liangzhi |
| [AxiomFree.lean](lean-declarations/valuation.md#module-697097c023d4) | 评价的形成与良知 / Valuation development and liangzhi |
| [BoundaryModels.lean](lean-declarations/core.md#module-5ffb89fcbb01) | 生成核心与关系结构 / Generative core and relational structure |
| [BridgesAudit.lean](lean-declarations/valuation.md#module-e1bed40c8da7) | 评价的形成与良知 / Valuation development and liangzhi |
| [CalibratedMacro.lean](lean-declarations/inquiry.md#module-c90fa4594397) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [CalibrationRevision.lean](lean-declarations/abstraction.md#module-365cf9c6139b) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [CarrierTurnover.lean](lean-declarations/shared.md#module-abe231e35227) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [Cases.lean](lean-declarations/concern.md#module-5fd22deccdc6) | 关切与共同活动 / Concern and shared activity |
| [ClaimLedger.lean](lean-declarations/shared.md#module-970e18466304) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ClosedLoopAudit.lean](lean-declarations/valuation.md#module-a5bbd3ef7a72) | 评价的形成与良知 / Valuation development and liangzhi |
| [ClosedLoopValuation.lean](lean-declarations/valuation.md#module-c43d59d00448) | 评价的形成与良知 / Valuation development and liangzhi |
| [CompletionApplicability.lean](lean-declarations/core.md#module-b4ba5435b460) | 生成核心与关系结构 / Generative core and relational structure |
| [CompletionAudit.lean](lean-declarations/valuation.md#module-3ae2f0d8deb5) | 评价的形成与良知 / Valuation development and liangzhi |
| [CompletionBoundaries.lean](lean-declarations/abstraction.md#module-c1591ec1fb8e) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [CompletionExamples.lean](lean-declarations/abstraction.md#module-d333c1de816c) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [CompletionRole.lean](lean-declarations/abstraction.md#module-cd95616611d7) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [ConnectedGenerativeModel.lean](lean-declarations/core.md#module-5fa095440b41) | 生成核心与关系结构 / Generative core and relational structure |
| [ConnectedModel.lean](lean-declarations/core.md#module-5c73c09dd045) | 生成核心与关系结构 / Generative core and relational structure |
| [ConsequenceInquiry.lean](lean-declarations/abstraction.md#module-6c65c55bbb0f) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [ConsequenceTransmission.lean](lean-declarations/shared.md#module-af38a04c2c3b) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ConstructedPrediction.lean](lean-declarations/learning.md#module-0122dd51e123) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ConstructedSelector.lean](lean-declarations/learning.md#module-339f067fcb29) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ConstructedUpdater.lean](lean-declarations/learning.md#module-f1c81893690e) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ConstructiveDecisions.lean](lean-declarations/core.md#module-b25b9b8fad1d) | 生成核心与关系结构 / Generative core and relational structure |
| [ContactFormation.lean](lean-declarations/inquiry.md#module-7bd60e384c41) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [ContinuationRenewal.lean](lean-declarations/ethics.md#module-3e3471402b88) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ContinuationRenewalAudit.lean](lean-declarations/ethics.md#module-38d6a8892340) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ContinuationScope.lean](lean-declarations/abstraction.md#module-62dd1356dc98) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [ControlledRefinement.lean](lean-declarations/learning.md#module-8fa0f7430ad8) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ControllerRevision.lean](lean-declarations/learning.md#module-8763b069f801) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [CoreTreeRearticulation.lean](lean-declarations/inquiry.md#module-2bcbeddc6d03) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [CorrespondenceSamples.lean](lean-declarations/ethics.md#module-059498ea4742) | 规范根据与生成方向 / Normative grounding and generative direction |
| [CoupledConcernHistory.lean](lean-declarations/concern.md#module-8c7efefb404f) | 关切与共同活动 / Concern and shared activity |
| [CoupledOccurrence.lean](lean-declarations/core.md#module-9f09dc9dc6b1) | 生成核心与关系结构 / Generative core and relational structure |
| [CouplingOptima.lean](lean-declarations/abstraction.md#module-ad36cb089189) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [CoverageBoundary.lean](lean-declarations/abstraction.md#module-83c27fd36c83) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [CoverageBoundary.lean](lean-declarations/abstraction.md#module-e839ddaa98f9) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [CutCoverageAudit.lean](lean-declarations/ethics.md#module-17d9a609f504) | 规范根据与生成方向 / Normative grounding and generative direction |
| [DenseOrder.lean](lean-declarations/abstraction.md#module-8080157d8373) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [DependentCompletion.lean](lean-declarations/abstraction.md#module-363e3103ce55) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [Depletion.lean](lean-declarations/core.md#module-5391ff34d63c) | 生成核心与关系结构 / Generative core and relational structure |
| [DerivedInquiryCertificates.lean](lean-declarations/inquiry.md#module-c250dc5a85ef) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [DynamicClassification.lean](lean-declarations/core.md#module-b7c8638a14c9) | 生成核心与关系结构 / Generative core and relational structure |
| [DynamicConsequences.lean](lean-declarations/core.md#module-bf65a1ee68e5) | 生成核心与关系结构 / Generative core and relational structure |
| [DynamicSymmetry.lean](lean-declarations/core.md#module-d33bc0ead9a9) | 生成核心与关系结构 / Generative core and relational structure |
| [DynamicUnderdetermination.lean](lean-declarations/core.md#module-9120ff48313a) | 生成核心与关系结构 / Generative core and relational structure |
| [EmbeddedEvaluation.lean](lean-declarations/core.md#module-ce2fc7445eba) | 生成核心与关系结构 / Generative core and relational structure |
| [EmissionArchive.lean](lean-declarations/shared.md#module-4ee9e7930d43) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [EnactedOrientation.lean](lean-declarations/core.md#module-7587315c346a) | 生成核心与关系结构 / Generative core and relational structure |
| [Enumeration.lean](lean-declarations/shared.md#module-2aa3f81f3ba3) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [EqualityGenerativity.lean](lean-declarations/abstraction.md#module-475eb20715c8) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [EthicalOrientation.lean](lean-declarations/core.md#module-b65d39fd3ece) | 生成核心与关系结构 / Generative core and relational structure |
| [Evaluate.lean](lean-declarations/learning.md#module-95295e365c1b) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [EvaluationPreparation.lean](lean-declarations/shared.md#module-29ef86360e74) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [EvaluationWitness.lean](lean-declarations/shared.md#module-121ae848f6c7) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [EvaluativeSuccession.lean](lean-declarations/shared.md#module-d6e11394f125) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ExplorationAudit.lean](lean-declarations/valuation.md#module-bd4702a9521f) | 评价的形成与良知 / Valuation development and liangzhi |
| [ExplorationCoverage.lean](lean-declarations/valuation.md#module-793ac042ad50) | 评价的形成与良知 / Valuation development and liangzhi |
| [Exposure.lean](lean-declarations/learning.md#module-4d87e1bfa317) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ExposureExamples.lean](lean-declarations/learning.md#module-0882888ab9e6) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [FamilyAdmission.lean](lean-declarations/abstraction.md#module-f0533e96feaa) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [FeedbackDynamics.lean](lean-declarations/learning.md#module-95c70a079b33) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [FeedbackExamples.lean](lean-declarations/learning.md#module-0db80602d519) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [FiniteAdmission.lean](lean-declarations/abstraction.md#module-910666c286d1) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [FiniteBranching.lean](lean-declarations/abstraction.md#module-5f36470a468d) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [FiniteExposureKernel.lean](lean-declarations/learning.md#module-be5433d0f096) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [FiniteInquiryClassification.lean](lean-declarations/inquiry.md#module-13aee3c0e811) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [FormationAccounts.lean](lean-declarations/shared.md#module-411df828cbbe) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [FormationClosure.lean](lean-declarations/inquiry.md#module-d330223ee429) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [FormationDraw.lean](lean-declarations/inquiry.md#module-1d28de9ca37e) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [FormationRoot.lean](lean-declarations/shared.md#module-3599c054bffb) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [FormationRoutes.lean](lean-declarations/ethics.md#module-43eea8d884d9) | 规范根据与生成方向 / Normative grounding and generative direction |
| [FormationSupport.lean](lean-declarations/learning.md#module-4716569d13e3) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [FormativeCapacity.lean](lean-declarations/ethics.md#module-baa982e92c5c) | 规范根据与生成方向 / Normative grounding and generative direction |
| [FormedContactCycle.lean](lean-declarations/inquiry.md#module-b5e59468402d) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [FormedRecipientRoute.lean](lean-declarations/shared.md#module-3d3e3f859742) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [FormedRouteMonitor.lean](lean-declarations/shared.md#module-e00c807b1ad5) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [FormedSelection.lean](lean-declarations/shared.md#module-c9712e044702) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [FreshRevision.lean](lean-declarations/shared.md#module-b592dcce60e2) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [FulfillmentStatus.lean](lean-declarations/shared.md#module-641fa8f3ad8b) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [FunctionGraphs.lean](lean-declarations/abstraction.md#module-967f5a53d7df) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [GeneratedPaths.lean](lean-declarations/core.md#module-553e96448b89) | 生成核心与关系结构 / Generative core and relational structure |
| [GeneratedSelf.lean](lean-declarations/core.md#module-134b1f2adf22) | 生成核心与关系结构 / Generative core and relational structure |
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
| [GroundingContract.lean](lean-declarations/concern.md#module-618302908b9f) | 关切与共同活动 / Concern and shared activity |
| [HistoryIdeals.lean](lean-declarations/abstraction.md#module-81928aacbe61) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [HistoryRealization.lean](lean-declarations/core.md#module-a7d9b0de6d97) | 生成核心与关系结构 / Generative core and relational structure |
| [IdealWarrant.lean](lean-declarations/abstraction.md#module-e3abf1a9ab66) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [IndexedAssembly.lean](lean-declarations/abstraction.md#module-e1734fcd36ac) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [InductiveDomain.lean](lean-declarations/abstraction.md#module-c3d844e3d579) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [Initiality.lean](lean-declarations/abstraction.md#module-831623a203ba) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [InquiryFamilies.lean](lean-declarations/inquiry.md#module-bfb389247e8c) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [InquiryRelevance.lean](lean-declarations/abstraction.md#module-102e6587264a) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [InquiryRevision.lean](lean-declarations/shared.md#module-df65151201cb) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [InquirySufficiency.lean](lean-declarations/inquiry.md#module-8f3efb8aecfe) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [InquiryWarrant.lean](lean-declarations/abstraction.md#module-162f3791d24f) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [InspectionPreparation.lean](lean-declarations/shared.md#module-42569f077f11) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [InspectionWitness.lean](lean-declarations/shared.md#module-3ca0f0fbccd6) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [IntegratedPortContinuation.lean](lean-declarations/inquiry.md#module-9e3c69c03ebf) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [JointContinuationClassification.lean](lean-declarations/ethics.md#module-2c0028cc241e) | 规范根据与生成方向 / Normative grounding and generative direction |
| [KeptSupport.lean](lean-declarations/abstraction.md#module-c764abc871d9) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [LineageAudit.lean](lean-declarations/valuation.md#module-7d1b924b40d2) | 评价的形成与良知 / Valuation development and liangzhi |
| [LineageInProcess.lean](lean-declarations/valuation.md#module-45b450e65721) | 评价的形成与良知 / Valuation development and liangzhi |
| [LivingRealization.lean](lean-declarations/ethics.md#module-90135b67b58c) | 规范根据与生成方向 / Normative grounding and generative direction |
| [LivingRecovery.lean](lean-declarations/ethics.md#module-37187272c431) | 规范根据与生成方向 / Normative grounding and generative direction |
| [MarketGenerativity.lean](lean-declarations/other.md#module-e2e5c347dc5a) | 其他形式研究 / Other formal studies |
| [NativePacketCases.lean](lean-declarations/inquiry.md#module-08a4b3aa7401) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [NativePacketProcess.lean](lean-declarations/inquiry.md#module-a594aff718eb) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [NativePortContinuation.lean](lean-declarations/renewal.md#module-948079a4c2d6) | 支持与更新 / Support and renewal |
| [NaturalismIdentity.lean](lean-declarations/core.md#module-3a02a4d6964b) | 生成核心与关系结构 / Generative core and relational structure |
| [NaturalismReview.lean](lean-declarations/core.md#module-063fe108d1e9) | 生成核心与关系结构 / Generative core and relational structure |
| [NondualConcernAdapter.lean](lean-declarations/concern.md#module-fcb630ff99c3) | 关切与共同活动 / Concern and shared activity |
| [NondualCore.lean](lean-declarations/core.md#module-3efe43e1116b) | 生成核心与关系结构 / Generative core and relational structure |
| [NondualFormation.lean](lean-declarations/concern.md#module-ddda3346b696) | 关切与共同活动 / Concern and shared activity |
| [OddsEnvelope.lean](lean-declarations/concern.md#module-f809c3938a43) | 关切与共同活动 / Concern and shared activity |
| [OfferedChoiceBounds.lean](lean-declarations/concern.md#module-9b9421d95d90) | 关切与共同活动 / Concern and shared activity |
| [OnePacketAdmissibility.lean](lean-declarations/inquiry.md#module-fa2ef58e134e) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [OnePacketInquirySynthesis.lean](lean-declarations/inquiry.md#module-8c13eaf34b78) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [OnePacketQuestions.lean](lean-declarations/inquiry.md#module-e5043c6b7615) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [OneProcess.lean](lean-declarations/valuation.md#module-a454cc03f2a3) | 评价的形成与良知 / Valuation development and liangzhi |
| [OneProcessAudit.lean](lean-declarations/valuation.md#module-297e01080273) | 评价的形成与良知 / Valuation development and liangzhi |
| [OutcomeContinuation.lean](lean-declarations/core.md#module-c48ee824a0b3) | 生成核心与关系结构 / Generative core and relational structure |
| [PacketLawDerivation.lean](lean-declarations/inquiry.md#module-db5cafd783d9) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PaidArchiveReader.lean](lean-declarations/shared.md#module-dacef2fbbee5) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [PaidPreImport.lean](lean-declarations/shared.md#module-72d53bbb0ddb) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [PaidRecipientReasons.lean](lean-declarations/shared.md#module-c2e841f7d5e2) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [PairedPlasticity.lean](lean-declarations/shared.md#module-0f653cfbf240) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [PatientConcern.lean](lean-declarations/concern.md#module-5ad0b8e8fd94) | 关切与共同活动 / Concern and shared activity |
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
| [PhaseRecoveredContact.lean](lean-declarations/inquiry.md#module-b51b3a4c7541) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PlasticityPreparation.lean](lean-declarations/shared.md#module-c527ff17c751) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [PlasticityWitness.lean](lean-declarations/shared.md#module-ac933f076498) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [PluralRecords.lean](lean-declarations/abstraction.md#module-2a54e07465df) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [PortAlignment.lean](lean-declarations/inquiry.md#module-7c982b0727b0) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PortDirectRenewal.lean](lean-declarations/inquiry.md#module-073ae3eb42fa) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PortRenewalBoundary.lean](lean-declarations/inquiry.md#module-c7210c591afe) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PortRenewalLawClosure.lean](lean-declarations/inquiry.md#module-5c50415006f1) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PortValuation.lean](lean-declarations/inquiry.md#module-e625c38f5208) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [PotentialTruth.lean](lean-declarations/abstraction.md#module-e847c1e507df) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
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
| [ProtocolCompletion.lean](lean-declarations/learning.md#module-6272b5e2fc0c) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ProtocolCompletionExamples.lean](lean-declarations/learning.md#module-0744fae15585) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ProtocolComposition.lean](lean-declarations/learning.md#module-3e53edd102e4) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [ProtocolExamples.lean](lean-declarations/learning.md#module-45b8809c9dd8) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [PublicationBridge.lean](lean-declarations/shared.md#module-255a96b41300) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [PublicationBudget.lean](lean-declarations/shared.md#module-2c579a67c493) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [PublicationSafety.lean](lean-declarations/shared.md#module-946dd1d4cfb2) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [PurposeCorrection.lean](lean-declarations/concern.md#module-51689dfd2a2c) | 关切与共同活动 / Concern and shared activity |
| [PurposeCorrectionHistory.lean](lean-declarations/concern.md#module-41ff61a5ae5b) | 关切与共同活动 / Concern and shared activity |
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
| [RecipientReasons.lean](lean-declarations/shared.md#module-69dd2fd3322c) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ReconfigurableRoutes.lean](lean-declarations/ethics.md#module-bec079c8bd79) | 规范根据与生成方向 / Normative grounding and generative direction |
| [ReconfigurationCorrespondenceSamples.lean](lean-declarations/ethics.md#module-12ce623ea5ce) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RecordedClaims.lean](lean-declarations/abstraction.md#module-33531476b412) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [RecordedEvidence.lean](lean-declarations/shared.md#module-d6edcd35ca09) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RecoveryQuantum.lean](lean-declarations/inquiry.md#module-02ce03487a51) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [RecursiveGenerativeSelection.lean](lean-declarations/ethics.md#module-ecb2b467bd36) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RecursiveGenerativeSelectionAudit.lean](lean-declarations/ethics.md#module-002fc680ef8a) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RecursiveSelectionInheritance.lean](lean-declarations/ethics.md#module-177504233211) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RecursiveSelectionInheritanceAudit.lean](lean-declarations/ethics.md#module-0f28a5ad9488) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RegeneratingPersistence.lean](lean-declarations/core.md#module-d8a479331a75) | 生成核心与关系结构 / Generative core and relational structure |
| [RegenerativeDiversity.lean](lean-declarations/ethics.md#module-fb7ea9229d0d) | 规范根据与生成方向 / Normative grounding and generative direction |
| [RelationalAssembly.lean](lean-declarations/abstraction.md#module-b1e9ae8b3572) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [RelationalContinuation.lean](lean-declarations/core.md#module-670551b8b671) | 生成核心与关系结构 / Generative core and relational structure |
| [RelationalCut.lean](lean-declarations/inquiry.md#module-8965a528dcb0) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [RelationalDynamics.lean](lean-declarations/core.md#module-af635c4a4144) | 生成核心与关系结构 / Generative core and relational structure |
| [RemainingDependency.lean](lean-declarations/abstraction.md#module-c1c11c83ec55) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [RenewalAccounting.lean](lean-declarations/renewal.md#module-b8df4e3120cc) | 支持与更新 / Support and renewal |
| [RenewalBasics.lean](lean-declarations/renewal.md#module-77ecd2c775da) | 支持与更新 / Support and renewal |
| [RenewalCharacterization.lean](lean-declarations/renewal.md#module-5fca0507b290) | 支持与更新 / Support and renewal |
| [RenewalClosure.lean](lean-declarations/renewal.md#module-35b608afeb1a) | 支持与更新 / Support and renewal |
| [RenewalConfigurations.lean](lean-declarations/renewal.md#module-a218916039de) | 支持与更新 / Support and renewal |
| [RenewalExamples.lean](lean-declarations/renewal.md#module-87b5bd85fd55) | 支持与更新 / Support and renewal |
| [RenewalLedger.lean](lean-declarations/shared.md#module-46a3e9d8b95a) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RenewalLink.lean](lean-declarations/renewal.md#module-28c0ce8386f8) | 支持与更新 / Support and renewal |
| [RenewalLiquidity.lean](lean-declarations/shared.md#module-a8de4892aa41) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RenewalPremises.lean](lean-declarations/renewal.md#module-8149a0ba6370) | 支持与更新 / Support and renewal |
| [RenewalSufficiency.lean](lean-declarations/renewal.md#module-c1beae045284) | 支持与更新 / Support and renewal |
| [ReserveTurnover.lean](lean-declarations/shared.md#module-6fd1230f8bb2) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ResourceContinuation.lean](lean-declarations/renewal.md#module-b17cc0c41017) | 支持与更新 / Support and renewal |
| [Retention.lean](lean-declarations/shared.md#module-4ab19d4a2066) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RevisingPort.lean](lean-declarations/inquiry.md#module-c215038e7e48) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [RevisionPreparation.lean](lean-declarations/shared.md#module-cd73453f54b6) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RevisionSuccession.lean](lean-declarations/shared.md#module-737754c24400) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RevisionWitness.lean](lean-declarations/shared.md#module-d03c440ac0b4) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RootBridge.lean](lean-declarations/shared.md#module-6ab582d74d00) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RootGrounding.lean](lean-declarations/concern.md#module-c86f0b363b70) | 关切与共同活动 / Concern and shared activity |
| [RootRealization.lean](lean-declarations/core.md#module-62ba3600c9f2) | 生成核心与关系结构 / Generative core and relational structure |
| [RouteDiagnostics.lean](lean-declarations/shared.md#module-6d5ab3eb998c) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RouteRevision.lean](lean-declarations/shared.md#module-39cee25a965f) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [RoutesCorrespondenceSamples.lean](lean-declarations/ethics.md#module-b49c122e730b) | 规范根据与生成方向 / Normative grounding and generative direction |
| [SecondOrder.lean](lean-declarations/abstraction.md#module-438373a5bced) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [SelectorRevision.lean](lean-declarations/shared.md#module-d4766cfc350c) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [SelfModelCertification.lean](lean-declarations/shared.md#module-2633962036d2) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [SemanticAction.lean](lean-declarations/shared.md#module-a51c4566a005) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [SemanticCalibration.lean](lean-declarations/shared.md#module-ad79f81f6792) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ShrinkingGain.lean](lean-declarations/learning.md#module-59ffcfa61113) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [SignatureTruth.lean](lean-declarations/abstraction.md#module-aacdf65172d8) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [SituatedContinuation.lean](lean-declarations/ethics.md#module-4199e2843e06) | 规范根据与生成方向 / Normative grounding and generative direction |
| [SituatedPractice.lean](lean-declarations/concern.md#module-618b534f95cf) | 关切与共同活动 / Concern and shared activity |
| [SituatedRenewal.lean](lean-declarations/ethics.md#module-4c743231f0b3) | 规范根据与生成方向 / Normative grounding and generative direction |
| [StartingStock.lean](lean-declarations/inquiry.md#module-086d448b5bc8) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [SuccessionHistoryInterface.lean](lean-declarations/shared.md#module-6c08598bc18a) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [SuccessionPreparation.lean](lean-declarations/shared.md#module-0316e1fac3b9) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [SuccessionWitness.lean](lean-declarations/shared.md#module-d529bfeccc02) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [SuccessorLearning.lean](lean-declarations/shared.md#module-5dd8cb345fbf) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [SupportHandoff.lean](lean-declarations/shared.md#module-15a26dae9373) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [SupportNecessity.lean](lean-declarations/renewal.md#module-bedcaae2aaa8) | 支持与更新 / Support and renewal |
| [SupportedRevision.lean](lean-declarations/learning.md#module-ed748ff2bb5a) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [SymbolicDynamics.lean](lean-declarations/learning.md#module-0146a609b532) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [SystemsComplexity.lean](lean-declarations/learning.md#module-f2ed510fb44f) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [SystemsOrganization.lean](lean-declarations/learning.md#module-4a3c27c14d5e) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [TieBreaking.lean](lean-declarations/abstraction.md#module-c67844003d2b) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [TrajectoryFidelity.lean](lean-declarations/valuation.md#module-baf6d4d24a70) | 评价的形成与良知 / Valuation development and liangzhi |
| [TypedRenewal.lean](lean-declarations/shared.md#module-04366373329a) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [TypedTruth.lean](lean-declarations/abstraction.md#module-77505a9c5a3f) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
| [UpdaterFormation.lean](lean-declarations/shared.md#module-98344ea49fe4) | 组织形成到可修正评价 / Organizational formation through revisable evaluation |
| [ValuationBridges.lean](lean-declarations/valuation.md#module-f496d68a278b) | 评价的形成与良知 / Valuation development and liangzhi |
| [ValuationCompletion.lean](lean-declarations/valuation.md#module-ff2eea4e63b0) | 评价的形成与良知 / Valuation development and liangzhi |
| [ValuationDevelopment.lean](lean-declarations/valuation.md#module-d23b7065be00) | 评价的形成与良知 / Valuation development and liangzhi |
| [ValuationInCore.lean](lean-declarations/inquiry.md#module-3c5f4e829425) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [ValuationRenewal.lean](lean-declarations/valuation.md#module-003faae288bf) | 评价的形成与良知 / Valuation development and liangzhi |
| [ValuationRenewalAudit.lean](lean-declarations/valuation.md#module-b05da0412da4) | 评价的形成与良知 / Valuation development and liangzhi |
| [VaryingFeedback.lean](lean-declarations/learning.md#module-8300137fadf5) | 学习、预测与动力学 / Learning, prediction and dynamics |
| [WholeGroundCoverage.lean](lean-declarations/ethics.md#module-386072b758e7) | 规范根据与生成方向 / Normative grounding and generative direction |
| [WholePortContinuation.lean](lean-declarations/inquiry.md#module-8eff53ffc111) | 可达询问、接触与过程律 / Attainable inquiry, contact and process laws |
| [WholePracticalRestriction.lean](lean-declarations/ethics.md#module-4271de674110) | 规范根据与生成方向 / Normative grounding and generative direction |
| [WholeQualityNaturalism.lean](lean-declarations/core.md#module-b4942b7409e4) | 生成核心与关系结构 / Generative core and relational structure |
| [WitnessHull.lean](lean-declarations/abstraction.md#module-72d18a9b2453) | 抽象、适用性与构成 / Abstraction, applicability and constitution |
