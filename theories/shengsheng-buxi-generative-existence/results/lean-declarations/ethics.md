# Lean 具名声明 / Named Lean declarations

[返回 Lean 导航](../LEAN-INDEX.md)。本表显示当前工作源与审计入口；所有历史副本仍见 [JSON 清单](../data/lean-index.json)。这是显式声明的位置索引，不能代替命题、假设及对应论证的阅读。 / [Return to navigation](../LEAN-INDEX.md). Working sources and audit entries appear here; all historical copies remain in the JSON inventory. These are explicit declaration locations, not substitutes for statements, hypotheses and correspondence arguments.

定理／引理逐项列出；定义与类型声明列在同一模块的折叠项中。限定名由文本 namespace 推断，仅供导航；私有内部名称和自动生成名称以 Lean 为准。 / Theorems and lemmas are individually listed; definitions and type declarations share each module's foldout. Namespace-qualified names are textual hints; Lean determines private/internal and generated names.

[全部方向与模块 / All topics and modules](../LEAN-DECLARATIONS.md)

## 规范根据与生成方向 / Normative grounding and generative direction

<a id="module-3e3471402b88"></a>

<details>
<summary>ContinuationRenewal.lean — 21 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CONTINUATION-RENEWAL-MATH.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [ContinuationRenewal.no_unrenewed_tail_of_accessible](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L28) | 28 |
| [ContinuationRenewal.no_renewal_free_tail](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L43) | 43 |
| [ContinuationRenewal.renewal_after_of_accessible](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L54) | 54 |
| [ContinuationRenewal.renewal_arbitrarily_late](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L71) | 71 |
| [ContinuationRenewal.renewal_arbitrarily_late_of_decidable](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L80) | 80 |
| [ContinuationRenewal.renewal_within_rank_bound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L92) | 92 |
| [ContinuationRenewal.renewal_within_rank_plus_one_steps](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L116) | 116 |
| [ContinuationRenewal.rank_renewal_arbitrarily_late](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L122) | 122 |
| [ContinuationRenewal.alternating_actual_steps](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L147) | 147 |
| [ContinuationRenewal.alternating_nonrenewal_decreases](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L154) | 154 |
| [ContinuationRenewal.alternating_renews_arbitrarily_late](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L164) | 164 |
| [ContinuationRenewal.alternating_period_two](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L169) | 169 |
| [ContinuationRenewal.alternating_one_restoring_form](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L175) | 175 |
| [ContinuationRenewal.alternating_restoration_raises_rank](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L181) | 181 |
| [ContinuationRenewal.alternating_has_actual_unrenewed_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L190) | 190 |
| [ContinuationRenewal.alternating_no_new_configurations](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L198) | 198 |
| [ContinuationRenewal.alternating_every_configuration_score_bounded](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L207) | 207 |

定义与类型 / Definitions and types:

- `def` [ContinuationRenewal.alternatingState](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L132) (L132)
- `def` [ContinuationRenewal.alternatingRank](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L136) (L136)
- `def` [ContinuationRenewal.alternatingRenewal](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L138) (L138)
- `def` [ContinuationRenewal.alternatingStep](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean#L144) (L144)

</details>

<a id="module-38d6a8892340"></a>

<details>
<summary>ContinuationRenewalAudit.lean — 0 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewalAudit.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CONTINUATION-RENEWAL-MATH.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewalAudit.lean`

Imports: `ContinuationRenewal`

没有扫描到显式 theorem/lemma；可能是导入、审计或定义模块。 / No explicit theorem/lemma scanned; this may be an import, audit or definition module.

文本中有 22 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 22 textual `#print axioms` commands; results belong to the original verification records.

</details>

<a id="module-17d9a609f504"></a>

<details>
<summary>CutCoverageAudit.lean — 17 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/UNIVERSAL-METAETHICS-LEAN-INTEGRATION.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [UniversalEthics.CutCoverageAudit.reach_avoids_reverse_closed_cut](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean#L54) | 54 |
| [UniversalEthics.CutCoverageAudit.reachable_implies_no_cut](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean#L65) | 65 |
| [UniversalEthics.CutCoverageAudit.has_cut_implies_not_reachable](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean#L73) | 73 |
| [UniversalEthics.CutCoverageAudit.not_reachable_has_cut](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean#L80) | 80 |
| [UniversalEthics.CutCoverageAudit.has_cut_iff_not_reachable](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean#L90) | 90 |
| [UniversalEthics.CutCoverageAudit.no_cut_iff_double_negated_reachability](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean#L96) | 96 |
| [UniversalEthics.CutCoverageAudit.no_cut_to_reachable_of_decidable](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean#L106) | 106 |
| [UniversalEthics.CutCoverageAudit.no_cut_iff_reachable_of_decidable](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean#L116) | 116 |
| [UniversalEthics.CutCoverageAudit.singleton_reachability_iff](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean#L131) | 131 |
| [UniversalEthics.CutCoverageAudit.double_negation_elimination_implies_universal_cut_upgrade](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean#L143) | 143 |
| [UniversalEthics.CutCoverageAudit.universal_cut_upgrade_implies_double_negation_elimination](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean#L149) | 149 |
| [UniversalEthics.CutCoverageAudit.universal_cut_upgrade_iff_double_negation_elimination](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean#L166) | 166 |

定义与类型 / Definitions and types:

- `inductive` [UniversalEthics.CutCoverageAudit.Reach](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean#L36) (L36)
- `def` [UniversalEthics.CutCoverageAudit.HasCut](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean#L41) (L41)
- `def` [UniversalEthics.CutCoverageAudit.NoCut](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean#L49) (L49)
- `def` [UniversalEthics.CutCoverageAudit.DoubleNegationElimination](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean#L123) (L123)
- `def` [UniversalEthics.CutCoverageAudit.UniversalCutUpgrade](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean#L126) (L126)

文本中有 12 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 12 textual `#print axioms` commands; results belong to the original verification records.

</details>

<a id="module-2c0028cc241e"></a>

<details>
<summary>JointContinuationClassification.lean — 21 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/ZERO-AXIOM-CLASSIFICATION-MATH.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean`

Imports: `Std`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [JointContinuationClassification.whole_profile_preservation_iff_joint_bundle_preservation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L49) | 49 |
| [JointContinuationClassification.whole_profile_preservation_composes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L63) | 63 |
| [JointContinuationClassification.faithful_history_transport_preserves_joint_bundles](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L77) | 77 |
| [JointContinuationClassification.complement_closed_preservation_excludes_new_realization](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L95) | 95 |
| [JointContinuationClassification.same_marginal_realizations_can_lose_a_joint_bundle](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L173) | 173 |

定义与类型 / Definitions and types:

- `structure` [JointContinuationClassification.Continuations](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L30) (L30)
- `def` [JointContinuationClassification.Jointly](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L34) (L34)
- `def` [JointContinuationClassification.CarriesWholeProfiles](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L39) (L39)
- `def` [JointContinuationClassification.PreservesJointBundles](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L44) (L44)
- `inductive` [JointContinuationClassification.Configuration](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L121) (L121)
- `inductive` [JointContinuationClassification.Event](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L125) (L125)
- `inductive` [JointContinuationClassification.Step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L129) (L129)
- `structure` [JointContinuationClassification.History](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L138) (L138)
- `def` [JointContinuationClassification.Admissible](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L144) (L144)
- `inductive` [JointContinuationClassification.Claim](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L148) (L148)
- `def` [JointContinuationClassification.Realized](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L152) (L152)
- `def` [JointContinuationClassification.retained](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L156) (L156)
- `def` [JointContinuationClassification.released](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L160) (L160)
- `def` [JointContinuationClassification.together](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L164) (L164)
- `def` [JointContinuationClassification.leftOnly](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L166) (L166)
- `def` [JointContinuationClassification.rightOnly](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/JointContinuationClassification.lean#L168) (L168)

</details>

<a id="module-90135b67b58c"></a>

<details>
<summary>LivingRealization.lean — 20 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/LIVING-DEPENDENCY-INTEGRATION.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean`

Imports: `SituatedRenewal`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [Generative.LivingRealization.ion_account](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L59) | 59 |
| [Generative.LivingRealization.support_account](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L70) | 70 |
| [Generative.LivingRealization.compensation_required](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L100) | 100 |
| [Generative.LivingRealization.support_input_required](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L117) | 117 |
| [Generative.LivingRealization.recurrent_support_input](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L134) | 134 |
| [Generative.LivingRealization.included_store_account](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L153) | 153 |
| [Generative.LivingRealization.included_store_bounds_load](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L175) | 175 |
| [Generative.LivingRealization.headroom_can_accommodate_ingress](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L211) | 211 |
| [Generative.LivingRealization.retained_work_can_compensate](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L218) | 218 |
| [Generative.LivingRealization.inactive_then_compensating_history](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L226) | 226 |

定义与类型 / Definitions and types:

- `structure` [Generative.LivingRealization.TransportLaw](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L28) (L28)
- `def` [Generative.LivingRealization.Within](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L45) (L45)
- `def` [Generative.LivingRealization.maintained](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L49) (L49)
- `def` [Generative.LivingRealization.ionHeadroom](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L52) (L52)
- `def` [Generative.LivingRealization.supportedHeadroom](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L55) (L55)
- `def` [Generative.LivingRealization.transportDependency](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L83) (L83)
- `def` [Generative.LivingRealization.supportDependency](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L91) (L91)
- `def` [Generative.LivingRealization.storeDependency](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L162) (L162)
- `def` [Generative.LivingRealization.exampleProcess](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L196) (L196)
- `def` [Generative.LivingRealization.exampleLaw](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean#L199) (L199)

</details>

<a id="module-37187272c431"></a>

<details>
<summary>LivingRecovery.lean — 20 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/LIVING-RECOVERY-EVIDENCE.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean`

Imports: `LivingRealization`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [Generative.LivingRecovery.fluxSum_succ](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L45) | 45 |
| [Generative.LivingRecovery.positive_flux_has_event](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L53) | 53 |
| [Generative.LivingRecovery.window_transport](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L69) | 69 |
| [Generative.LivingRecovery.window_work](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L88) | 88 |
| [Generative.LivingRecovery.recovery_account](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L107) | 107 |
| [Generative.LivingRecovery.compensation_required](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L125) | 125 |
| [Generative.LivingRecovery.support_input_required](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L139) | 139 |
| [Generative.LivingRecovery.window_store](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L154) | 154 |
| [Generative.LivingRecovery.included_store_bounds_recovery](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L174) | 174 |
| [Generative.LivingRecovery.recurrent_input_at_returns](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L191) | 191 |
| [Generative.LivingRecovery.embedded_passive_total_zero](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L221) | 221 |
| [Generative.LivingRecovery.old_maintained_window_is_unrestricted](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L228) | 228 |
| [Generative.LivingRecovery.passive_relief_without_work](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L254) | 254 |
| [Generative.LivingRecovery.passive_excursion_then_return](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L262) | 262 |
| [Generative.LivingRecovery.retained_work_restores_after_excursion](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L273) | 273 |

定义与类型 / Definitions and types:

- `structure` [Generative.LivingRecovery.TransportLaw](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L23) (L23)
- `def` [Generative.LivingRecovery.fluxSum](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L41) (L41)
- `def` [Generative.LivingRecovery.fromRealization](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L210) (L210)
- `def` [Generative.LivingRecovery.exampleProcess](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L237) (L237)
- `def` [Generative.LivingRecovery.exampleLaw](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRecovery.lean#L242) (L242)

</details>

<a id="module-ecb2b467bd36"></a>

<details>
<summary>RecursiveGenerativeSelection.lean — 15 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelection.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RECURSIVE-GENERATIVE-SELECTION-MATH.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelection.lean`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [RecursiveGenerativeSelection.mul_assoc_eq](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelection.lean#L20) | 20 |
| [RecursiveGenerativeSelection.add_mul_eq](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelection.lean#L24) | 24 |
| [RecursiveGenerativeSelection.strict_mul_cancel_right](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelection.lean#L27) | 27 |
| [RecursiveGenerativeSelection.cross_compare_iff](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelection.lean#L52) | 52 |
| [RecursiveGenerativeSelection.more_supporters_produce_more_support](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelection.lean#L59) | 59 |
| [RecursiveGenerativeSelection.supporter_share_falls_within](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelection.lean#L66) | 66 |
| [RecursiveGenerativeSelection.descendant_totals_positive](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelection.lean#L91) | 91 |
| [RecursiveGenerativeSelection.pooled_counts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelection.lean#L98) | 98 |
| [RecursiveGenerativeSelection.support_contribution_threshold](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelection.lean#L128) | 128 |
| [RecursiveGenerativeSelection.global_supporter_share_rises_iff](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelection.lean#L153) | 153 |
| [RecursiveGenerativeSelection.weak_coupling_witness](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelection.lean#L173) | 173 |
| [RecursiveGenerativeSelection.strong_coupling_witness](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelection.lean#L188) | 188 |

定义与类型 / Definitions and types:

- `def` [RecursiveGenerativeSelection.support](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelection.lean#L36) (L36)
- `def` [RecursiveGenerativeSelection.descendants](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelection.lean#L40) (L40)
- `def` [RecursiveGenerativeSelection.pooled](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelection.lean#L46) (L46)

</details>

<a id="module-002fc680ef8a"></a>

<details>
<summary>RecursiveGenerativeSelectionAudit.lean — 0 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelectionAudit.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RECURSIVE-GENERATIVE-SELECTION-MATH.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveGenerativeSelectionAudit.lean`

Imports: `RecursiveGenerativeSelection`

没有扫描到显式 theorem/lemma；可能是导入、审计或定义模块。 / No explicit theorem/lemma scanned; this may be an import, audit or definition module.

文本中有 15 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 15 textual `#print axioms` commands; results belong to the original verification records.

</details>

<a id="module-177504233211"></a>

<details>
<summary>RecursiveSelectionInheritance.lean — 13 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveSelectionInheritance.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RECURSIVE-SELECTION-INHERITANCE-MATH.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveSelectionInheritance.lean`

Imports: `RecursiveGenerativeSelection`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [RecursiveSelectionInheritance.operation_accounts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveSelectionInheritance.lean#L93) | 93 |
| [RecursiveSelectionInheritance.assembly_accounts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveSelectionInheritance.lean#L107) | 107 |
| [RecursiveSelectionInheritance.connected_two_generation_accounts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveSelectionInheritance.lean#L120) | 120 |
| [RecursiveSelectionInheritance.assembly_row_limits](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveSelectionInheritance.lean#L134) | 134 |
| [RecursiveSelectionInheritance.fully_assembled_strong_share_rises_iff](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveSelectionInheritance.lean#L149) | 149 |
| [RecursiveSelectionInheritance.faithful_two_generation_history](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveSelectionInheritance.lean#L166) | 166 |
| [RecursiveSelectionInheritance.converted_two_generation_history](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveSelectionInheritance.lean#L181) | 181 |
| [RecursiveSelectionInheritance.insufficient_source_or_excess_assembly_fails](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveSelectionInheritance.lean#L199) | 199 |

定义与类型 / Definitions and types:

- `structure` [RecursiveSelectionInheritance.State](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveSelectionInheritance.lean#L25) (L25)
- `structure` [RecursiveSelectionInheritance.Transfer](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveSelectionInheritance.lean#L38) (L38)
- `def` [RecursiveSelectionInheritance.material](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveSelectionInheritance.lean#L46) (L46)
- `def` [RecursiveSelectionInheritance.operate](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveSelectionInheritance.lean#L52) (L52)
- `def` [RecursiveSelectionInheritance.assemble](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveSelectionInheritance.lean#L73) (L73)

</details>

<a id="module-0f28a5ad9488"></a>

<details>
<summary>RecursiveSelectionInheritanceAudit.lean — 0 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveSelectionInheritanceAudit.lean) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/README.md) · 尚无直接模块文档链接 / No direct module-documentation link found

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RecursiveSelectionInheritanceAudit.lean`

Imports: `RecursiveSelectionInheritance`

没有扫描到显式 theorem/lemma；可能是导入、审计或定义模块。 / No explicit theorem/lemma scanned; this may be an import, audit or definition module.

文本中有 13 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 13 textual `#print axioms` commands; results belong to the original verification records.

</details>

<a id="module-fb7ea9229d0d"></a>

<details>
<summary>RegenerativeDiversity.lean — 36 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVE-CAPACITY-INTEGRATION.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean`

Imports: `GenerativeCore`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [RegenerativeDiversity.prefix_depth](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L41) | 41 |
| [RegenerativeDiversity.prefix_evaluation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L46) | 46 |
| [RegenerativeDiversity.prefix_distinguishable](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L65) | 65 |
| [RegenerativeDiversity.retained_tap](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L77) | 77 |
| [RegenerativeDiversity.step_balance](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L145) | 145 |
| [RegenerativeDiversity.trace_balance](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L151) | 151 |
| [RegenerativeDiversity.growth_cycle](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L168) | 168 |
| [RegenerativeDiversity.growth_trace](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L187) | 187 |
| [RegenerativeDiversity.growing_repertoire](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L196) | 196 |
| [RegenerativeDiversity.one_shot_construction](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L210) | 210 |
| [RegenerativeDiversity.one_shot_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L218) | 218 |
| [RegenerativeDiversity.one_shot_trace](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L230) | 230 |
| [RegenerativeDiversity.copy_cycle](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L253) | 253 |
| [RegenerativeDiversity.copying_without_diversification](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L274) | 274 |

定义与类型 / Definitions and types:

- `inductive` [RegenerativeDiversity.Circuit](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L20) (L20)
- `def` [RegenerativeDiversity.depth](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L25) (L25)
- `def` [RegenerativeDiversity.evaluate](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L29) (L29)
- `def` [RegenerativeDiversity.prefixCircuit](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L33) (L33)
- `inductive` [RegenerativeDiversity.Tap](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L37) (L37)
- `def` [RegenerativeDiversity.cutInput](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L62) (L62)
- `structure` [RegenerativeDiversity.State](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L90) (L90)
- `inductive` [RegenerativeDiversity.Event](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L99) (L99)
- `def` [RegenerativeDiversity.intakeState](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L106) (L106)
- `def` [RegenerativeDiversity.assemblyState](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L109) (L109)
- `def` [RegenerativeDiversity.duplicateState](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L116) (L116)
- `def` [RegenerativeDiversity.reconstructionState](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L123) (L123)
- `inductive` [RegenerativeDiversity.Step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L127) (L127)
- `def` [RegenerativeDiversity.process](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L140) (L140)
- `def` [RegenerativeDiversity.Balanced](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L143) (L143)
- `def` [RegenerativeDiversity.growthState](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L158) (L158)
- `def` [RegenerativeDiversity.growthCycle](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L161) (L161)
- `def` [RegenerativeDiversity.growthHistory](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L163) (L163)
- `def` [RegenerativeDiversity.OneShotBound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L206) (L206)
- `def` [RegenerativeDiversity.copyState](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L243) (L243)
- `def` [RegenerativeDiversity.copyCycle](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L247) (L247)
- `def` [RegenerativeDiversity.copyHistory](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/RegenerativeDiversity.lean#L249) (L249)

</details>

<a id="module-4199e2843e06"></a>

<details>
<summary>SituatedContinuation.lean — 25 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/ZERO-AXIOM-CLASSIFICATION-MATH.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean`

Imports: `GenerativeCore`, `ContinuationRenewal`, `SituatedRenewal`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [Generative.SituatedContinuation.actual_suffix_continues](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L40) | 40 |
| [Generative.SituatedContinuation.excludes_all_routes_cannot_sustain](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L56) | 56 |
| [Generative.SituatedContinuation.joint_continuation_supplies_components](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L70) | 70 |
| [Generative.SituatedContinuation.continuation_realizes_required_dependencies](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L82) | 82 |
| [Generative.SituatedContinuation.rules_retain_invariant](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L108) | 108 |
| [Generative.SituatedContinuation.certified_history_renews](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L122) | 122 |
| [Generative.SituatedContinuation.implemented_rules_sustain](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L165) | 165 |
| [Generative.SituatedContinuation.alternatives_remain_alternatives](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L200) | 200 |
| [Generative.SituatedContinuation.support_progress](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L227) | 227 |
| [Generative.SituatedContinuation.repair_implements](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L240) | 240 |
| [Generative.SituatedContinuation.replacement_implements](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L244) | 244 |
| [Generative.SituatedContinuation.repair_never_replaces](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L248) | 248 |
| [Generative.SituatedContinuation.replacement_never_repairs](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L251) | 251 |
| [Generative.SituatedContinuation.adequate_alternative_histories](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L255) | 255 |
| [Generative.SituatedContinuation.permanent_opportunity_without_completion](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L301) | 301 |

定义与类型 / Definitions and types:

- `def` [Generative.SituatedContinuation.trajectory](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L26) (L26)
- `def` [Generative.SituatedContinuation.HasContinuation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L32) (L32)
- `inductive` [Generative.SituatedContinuation.Event](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L211) (L211)
- `def` [Generative.SituatedContinuation.supportProcess](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L216) (L216)
- `def` [Generative.SituatedContinuation.restorative](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L222) (L222)
- `def` [Generative.SituatedContinuation.supportRank](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L225) (L225)
- `def` [Generative.SituatedContinuation.repairChoice](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L237) (L237)
- `def` [Generative.SituatedContinuation.replacementChoice](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L238) (L238)
- `inductive` [Generative.SituatedContinuation.Opportunity](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L290) (L290)
- `def` [Generative.SituatedContinuation.opportunityProcess](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean#L294) (L294)

文本中有 25 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 25 textual `#print axioms` commands; results belong to the original verification records.

</details>

<a id="module-4c743231f0b3"></a>

<details>
<summary>SituatedRenewal.lean — 17 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERAL-GENERATIVE-REQUIREMENT-ARGUMENT.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean`

Imports: `GenerativeCore`, `ContinuationRenewal`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [Generative.SituatedRenewal.window_is_trace](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean#L51) | 51 |
| [Generative.SituatedRenewal.sumWindow_append](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean#L70) | 70 |
| [Generative.SituatedRenewal.window_account_or_response](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean#L84) | 84 |
| [Generative.SituatedRenewal.response_before_exhaustion](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean#L125) | 125 |
| [Generative.SituatedRenewal.inherited_failure_requires_replacement](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean#L142) | 142 |
| [Generative.SituatedRenewal.every_required_dependency_recurrently_responds](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean#L166) | 166 |
| [Generative.SituatedRenewal.no_response_strictly_depletes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean#L181) | 181 |
| [Generative.SituatedRenewal.response_within_remaining_bound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean#L191) | 191 |
| [Generative.SituatedRenewal.continuation_without_required_use_has_no_response](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean#L228) | 228 |

定义与类型 / Definitions and types:

- `structure` [Generative.SituatedRenewal.DependencyLaw](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean#L22) (L22)
- `def` [Generative.SituatedRenewal.Response](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean#L36) (L36)
- `def` [Generative.SituatedRenewal.Window](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean#L41) (L41)
- `def` [Generative.SituatedRenewal.windowWord](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean#L46) (L46)
- `def` [Generative.SituatedRenewal.sumWindow](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean#L61) (L61)
- `def` [Generative.SituatedRenewal.totalDemand](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean#L65) (L65)
- `def` [Generative.SituatedRenewal.idle](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean#L218) (L218)
- `def` [Generative.SituatedRenewal.idleDependencies](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean#L221) (L221)

文本中有 17 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 17 textual `#print axioms` commands; results belong to the original verification records.

</details>

<a id="module-386072b758e7"></a>

<details>
<summary>WholeGroundCoverage.lean — 44 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/UNIVERSAL-METAETHICS-LEAN-INTEGRATION.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean`

Imports: `Std`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [WholeGroundCoverage.reason_inheritance](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L51) | 51 |
| [WholeGroundCoverage.reached_is_admissible](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L59) | 59 |
| [WholeGroundCoverage.reached_iff_entails](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L64) | 64 |
| [WholeGroundCoverage.universal_target_coverage_iff](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L74) | 74 |
| [WholeGroundCoverage.uncovered_has_admissible_omission](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L85) | 85 |
| [WholeGroundCoverage.reached_mono](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L91) | 91 |
| [WholeGroundCoverage.substitute_grounded_seeds](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L100) | 100 |
| [WholeGroundCoverage.local_sound_iff_joined_sound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L126) | 126 |
| [WholeGroundCoverage.local_sound_gives_global_inheritance](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L137) | 137 |
| [WholeGroundCoverage.local_reach_in_joined](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L143) | 143 |
| [WholeGroundCoverage.glued_ground_iff_local](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L165) | 165 |
| [WholeGroundCoverage.compatible_local_ground_transport_glues](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L179) | 179 |
| [WholeGroundCoverage.jointly_grounded_scope_inheritance](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L189) | 189 |
| [WholeGroundCoverage.history_edge_preserves_history](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L211) | 211 |
| [WholeGroundCoverage.history_reach_projects](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L218) | 218 |
| [WholeGroundCoverage.history_reach_lifts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L230) | 230 |
| [WholeGroundCoverage.history_reach_iff](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L242) | 242 |
| [WholeGroundCoverage.history_local_sound_gives_global](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L250) | 250 |
| [WholeGroundCoverage.alternating_domains_cover](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L288) | 288 |
| [WholeGroundCoverage.alternating_first_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L295) | 295 |
| [WholeGroundCoverage.alternating_second_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L298) | 298 |
| [WholeGroundCoverage.alternating_join_reaches_finish](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L301) | 301 |
| [WholeGroundCoverage.first_scope_reach_stays_inside](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L306) | 306 |
| [WholeGroundCoverage.second_scope_reach_stays_at_seed](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L315) | 315 |
| [WholeGroundCoverage.alternating_beyond_separate_closures](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L324) | 324 |
| [WholeGroundCoverage.unconnected_reach_is_seed](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L338) | 338 |
| [WholeGroundCoverage.local_domain_coverage_insufficient](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L348) | 348 |

定义与类型 / Definitions and types:

- `inductive` [WholeGroundCoverage.Reached](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L36) (L36)
- `def` [WholeGroundCoverage.Admissible](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L41) (L41)
- `def` [WholeGroundCoverage.Entails](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L47) (L47)
- `structure` [WholeGroundCoverage.LocalAtlas](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L108) (L108)
- `def` [WholeGroundCoverage.ScopedEdge](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L112) (L112)
- `def` [WholeGroundCoverage.JoinedEdge](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L117) (L117)
- `def` [WholeGroundCoverage.LocalSound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L121) (L121)
- `def` [WholeGroundCoverage.CompatibleGrounds](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L153) (L153)
- `def` [WholeGroundCoverage.GluedGround](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L159) (L159)
- `inductive` [WholeGroundCoverage.HistoryEdge](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L204) (L204)
- `inductive` [WholeGroundCoverage.Place](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L263) (L263)
- `inductive` [WholeGroundCoverage.Window](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L268) (L268)
- `def` [WholeGroundCoverage.firstSeed](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L272) (L272)
- `inductive` [WholeGroundCoverage.InWindow](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L274) (L274)
- `inductive` [WholeGroundCoverage.WindowStep](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L280) (L280)
- `def` [WholeGroundCoverage.alternatingAtlas](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L284) (L284)
- `def` [WholeGroundCoverage.unconnectedAtlas](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean#L334) (L334)

文本中有 27 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 27 textual `#print axioms` commands; results belong to the original verification records.

</details>

<a id="module-4271de674110"></a>

<details>
<summary>WholePracticalRestriction.lean — 31 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVE-PREMISE-INTEGRATION.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [WholePracticalRestriction.descent_implies_compatibility](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L68) | 68 |
| [WholePracticalRestriction.joined_descends_iff_compatible](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L79) | 79 |
| [WholePracticalRestriction.compatibility_iff_common_whole_relation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L92) | 92 |
| [WholePracticalRestriction.joined_is_least_extension](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L104) | 104 |
| [WholePracticalRestriction.extensions_agree_on_covered_pairs](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L113) | 113 |
| [WholePracticalRestriction.pair_coverage_gives_unique_comparisons](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L122) | 122 |
| [WholePracticalRestriction.uncovered_pair_has_disagreeing_extensions](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L130) | 130 |
| [WholePracticalRestriction.point_coverage_does_not_give_pair_coverage](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L159) | 159 |
| [WholePracticalRestriction.faithful_recoding_preserves_comparison](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L174) | 174 |
| [WholePracticalRestriction.strict_whole_relation_restricts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L183) | 183 |
| [WholePracticalRestriction.cycle_charts_descend](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L212) | 212 |
| [WholePracticalRestriction.locally_strict_compatible_cycle_has_no_strict_extension](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L219) | 219 |
| [WholePracticalRestriction.whole_comparison_and_strictness_do_not_force_correspondence](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L254) | 254 |
| [WholePracticalRestriction.same_comparisons_do_not_determine_supporting_entries](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L292) | 292 |

定义与类型 / Definitions and types:

- `structure` [WholePracticalRestriction.Family](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L30) (L30)
- `def` [WholePracticalRestriction.Compatible](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L35) (L35)
- `def` [WholePracticalRestriction.Descends](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L42) (L42)
- `def` [WholePracticalRestriction.Joined](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L46) (L46)
- `def` [WholePracticalRestriction.CoveredPair](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L50) (L50)
- `def` [WholePracticalRestriction.PointCoverage](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L54) (L54)
- `def` [WholePracticalRestriction.PairCoverage](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L58) (L58)
- `def` [WholePracticalRestriction.Irreflexive](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L62) (L62)
- `def` [WholePracticalRestriction.Transitive](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L65) (L65)
- `def` [WholePracticalRestriction.singletonCharts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L154) (L154)
- `inductive` [WholePracticalRestriction.Three](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L196) (L196)
- `def` [WholePracticalRestriction.cycleNext](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L200) (L200)
- `def` [WholePracticalRestriction.cycleCharts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L205) (L205)
- `def` [WholePracticalRestriction.cycleWhole](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L210) (L210)
- `def` [WholePracticalRestriction.firstSupport](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L279) (L279)
- `def` [WholePracticalRestriction.secondSupport](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L283) (L283)
- `def` [WholePracticalRestriction.supportSum](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholePracticalRestriction.lean#L287) (L287)

</details>

<a id="module-059498ea4742"></a>

<details>
<summary>CorrespondenceSamples.lean — 6 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrespondenceSamples.lean) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrespondenceSamples.lean`

Imports: `FormativeCapacity`

没有扫描到显式 theorem/lemma；可能是导入、审计或定义模块。 / No explicit theorem/lemma scanned; this may be an import, audit or definition module.

定义与类型 / Definitions and types:

- `def` [treeWord](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrespondenceSamples.lean#L6) (L6)
- `def` [bit](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrespondenceSamples.lean#L11) (L11)
- `def` [stateLine](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrespondenceSamples.lean#L13) (L13)
- `def` [frontier](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrespondenceSamples.lean#L18) (L18)
- `def` [checkedRun](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrespondenceSamples.lean#L22) (L22)
- `def` [main](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrespondenceSamples.lean#L26) (L26)

</details>

<a id="module-43eea8d884d9"></a>

<details>
<summary>FormationRoutes.lean — 77 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVE-CAPACITY-INTEGRATION.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean`

Imports: `GenerativeCore`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [FormationRoutes.common_address_distinguishes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L49) | 49 |
| [FormationRoutes.forms_distinct](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L54) | 54 |
| [FormationRoutes.finite_branching](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L138) | 138 |
| [FormationRoutes.disconnected_step_is_bypass](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L160) | 160 |
| [FormationRoutes.step_accounts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L164) | 164 |
| [FormationRoutes.trace_accounts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L180) | 180 |
| [FormationRoutes.bypass_step_progress](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L189) | 189 |
| [FormationRoutes.bypass_trace_progress](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L205) | 205 |
| [FormationRoutes.forget_bypass](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L212) | 212 |
| [FormationRoutes.bypass_output_bound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L218) | 218 |
| [FormationRoutes.bypass_three_work_at_most_one](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L227) | 227 |
| [FormationRoutes.unfed_step_spends](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L232) | 232 |
| [FormationRoutes.zero_work_no_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L239) | 239 |
| [FormationRoutes.zero_work_trace_constant](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L245) | 245 |
| [FormationRoutes.disconnected_fresh_step_no_product](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L251) | 251 |
| [FormationRoutes.disconnected_one_work_no_product](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L257) | 257 |
| [FormationRoutes.disconnection_preserves_support](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L273) | 273 |
| [FormationRoutes.pushed_length](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L313) | 313 |
| [FormationRoutes.receive_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L319) | 319 |
| [FormationRoutes.attach_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L322) | 322 |
| [FormationRoutes.formed_prefix](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L327) | 327 |
| [FormationRoutes.synchronized_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L331) | 331 |
| [FormationRoutes.synchronized_list](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L337) | 337 |
| [FormationRoutes.formed_joint_history](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L344) | 344 |
| [FormationRoutes.formed_joint_costs](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L349) | 349 |
| [FormationRoutes.multiple_completions_exceed_bypass](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L356) | 356 |
| [FormationRoutes.both_forms_in_one_history](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L362) | 362 |
| [FormationRoutes.both_forms_unreachable_by_bypass](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L367) | 367 |
| [FormationRoutes.manual_two_steps](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L380) | 380 |
| [FormationRoutes.either_form_without_coupling](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L389) | 389 |
| [FormationRoutes.matched_connected_can_finish](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L396) | 396 |
| [FormationRoutes.matched_disconnected_cannot_finish](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L400) | 400 |
| [FormationRoutes.repair_uses_last_work](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L404) | 404 |
| [FormationRoutes.connected_underfunded_cannot_finish](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L409) | 409 |
| [FormationRoutes.redundant_for_single_target_with_two_work](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L414) | 414 |

定义与类型 / Definitions and types:

- `inductive` [FormationRoutes.Role](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L21) (L21)
- `inductive` [FormationRoutes.Tree](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L25) (L25)
- `def` [FormationRoutes.parts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L30) (L30)
- `inductive` [FormationRoutes.Port](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L34) (L34)
- `def` [FormationRoutes.inspect](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L38) (L38)
- `def` [FormationRoutes.dyadAB](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L44) (L44)
- `def` [FormationRoutes.dyadBC](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L45) (L45)
- `def` [FormationRoutes.leftForm](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L46) (L46)
- `def` [FormationRoutes.rightForm](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L47) (L47)
- `inductive` [FormationRoutes.Bar](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L56) (L56)
- `def` [FormationRoutes.barParts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L62) (L62)
- `def` [FormationRoutes.Spans](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L66) (L66)
- `structure` [FormationRoutes.Lot](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L73) (L73)
- `structure` [FormationRoutes.State](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L78) (L78)
- `def` [FormationRoutes.initial](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L88) (L88)
- `def` [FormationRoutes.stocked](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L89) (L89)
- `inductive` [FormationRoutes.Event](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L91) (L91)
- `def` [FormationRoutes.advance](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L96) (L96)
- `def` [FormationRoutes.Enabled](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L116) (L116)
- `def` [FormationRoutes.Step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L128) (L128)
- `def` [FormationRoutes.process](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L129) (L129)
- `def` [FormationRoutes.Synchronized](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L131) (L131)
- `def` [FormationRoutes.bypassProcess](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L132) (L132)
- `def` [FormationRoutes.children](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L134) (L134)
- `def` [FormationRoutes.sourceRaw](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L148) (L148)
- `def` [FormationRoutes.sourceWork](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L149) (L149)
- `def` [FormationRoutes.partialParts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L150) (L150)
- `def` [FormationRoutes.productParts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L151) (L151)
- `def` [FormationRoutes.material](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L156) (L156)
- `def` [FormationRoutes.workAccount](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L157) (L157)
- `def` [FormationRoutes.manualProgress](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L158) (L158)
- `def` [FormationRoutes.disconnect](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L271) (L271)
- `inductive` [FormationRoutes.Form](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L281) (L281)
- `def` [FormationRoutes.treeOf](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L285) (L285)
- `def` [FormationRoutes.syncEvent](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L289) (L289)
- `def` [FormationRoutes.startEvent](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L293) (L293)
- `def` [FormationRoutes.finishEvent](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L297) (L297)
- `def` [FormationRoutes.dyadOf](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L301) (L301)
- `def` [FormationRoutes.ready](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L306) (L306)
- `def` [FormationRoutes.pushed](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L309) (L309)
- `def` [FormationRoutes.manualPending](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L374) (L374)
- `def` [FormationRoutes.manualResult](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormationRoutes.lean#L377) (L377)

</details>

<a id="module-baa982e92c5c"></a>

<details>
<summary>FormativeCapacity.lean — 74 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVE-CAPACITY-INTEGRATION.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean`

Imports: `GenerativeCore`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [FormativeCapacity.grow_parts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L60) | 60 |
| [FormativeCapacity.close_parts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L65) | 65 |
| [FormativeCapacity.close_has_no_socket](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L70) | 70 |
| [FormativeCapacity.grow_socket_address](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L75) | 75 |
| [FormativeCapacity.grow_live](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L82) | 82 |
| [FormativeCapacity.spine_grows](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L87) | 87 |
| [FormativeCapacity.spine_depth](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L94) | 94 |
| [FormativeCapacity.spine_socket_address](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L100) | 100 |
| [FormativeCapacity.spine_closed_address](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L105) | 105 |
| [FormativeCapacity.finite_branching](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L159) | 159 |
| [FormativeCapacity.step_accounts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L185) | 185 |
| [FormativeCapacity.trace_accounts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L195) | 195 |
| [FormativeCapacity.build_reconstructs_next_interface](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L208) | 208 |
| [FormativeCapacity.no_socket_no_capture](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L217) | 217 |
| [FormativeCapacity.closed_step_spends](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L223) | 223 |
| [FormativeCapacity.closed_no_infinite](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L244) | 244 |
| [FormativeCapacity.infinite_never_commissions_closed](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L257) | 257 |
| [FormativeCapacity.one_shot_infinite_only_gathers](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L272) | 272 |
| [FormativeCapacity.gather_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L313) | 313 |
| [FormativeCapacity.gather_trace](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L322) | 322 |
| [FormativeCapacity.batch_commission](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L332) | 332 |
| [FormativeCapacity.batch_build](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L338) | 338 |
| [FormativeCapacity.batch_builds](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L345) | 345 |
| [FormativeCapacity.batch_terminal](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L356) | 356 |
| [FormativeCapacity.arbitrary_finite_terminal_depth](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L365) | 365 |
| [FormativeCapacity.open_commission](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L379) | 379 |
| [FormativeCapacity.cycle_capture](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L382) | 382 |
| [FormativeCapacity.cycle_build](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L387) | 387 |
| [FormativeCapacity.two_frames](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L398) | 398 |
| [FormativeCapacity.even_frame](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L401) | 401 |
| [FormativeCapacity.growth_lawful](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L411) | 411 |
| [FormativeCapacity.continuing_formation_run](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L430) | 430 |
| [FormativeCapacity.actual_growth_milestones](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L440) | 440 |
| [FormativeCapacity.completed_formations_recur](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L453) | 453 |
| [FormativeCapacity.actual_depth_unbounded](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L459) | 459 |
| [FormativeCapacity.infinite_gathering_without_formation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L466) | 466 |
| [FormativeCapacity.finite_feed_cursor_bound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L473) | 473 |
| [FormativeCapacity.finite_feed_trace_bound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L483) | 483 |

定义与类型 / Definitions and types:

- `inductive` [FormativeCapacity.Tree](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L23) (L23)
- `def` [FormativeCapacity.parts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L29) (L29)
- `def` [FormativeCapacity.depth](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L33) (L33)
- `def` [FormativeCapacity.socketAddress](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L38) (L38)
- `def` [FormativeCapacity.live](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L43) (L43)
- `def` [FormativeCapacity.grow](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L46) (L46)
- `def` [FormativeCapacity.close](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L52) (L52)
- `def` [FormativeCapacity.spine](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L56) (L56)
- `inductive` [FormativeCapacity.Phase](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L110) (L110)
- `structure` [FormativeCapacity.State](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L115) (L115)
- `inductive` [FormativeCapacity.Event](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L123) (L123)
- `abbrev` [FormativeCapacity.Feed](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L132) (L132)
- `def` [FormativeCapacity.initial](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L134) (L134)
- `def` [FormativeCapacity.advance](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L136) (L136)
- `def` [FormativeCapacity.Enabled](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L142) (L142)
- `def` [FormativeCapacity.Step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L150) (L150)
- `def` [FormativeCapacity.process](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L153) (L153)
- `def` [FormativeCapacity.children](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L155) (L155)
- `def` [FormativeCapacity.material](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L171) (L171)
- `def` [FormativeCapacity.inputLots](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L173) (L173)
- `def` [FormativeCapacity.workSpent](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L177) (L177)
- `def` [FormativeCapacity.total](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L181) (L181)
- `def` [FormativeCapacity.InfiniteFrom](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L241) (L241)
- `def` [FormativeCapacity.constantFeed](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L309) (L309)
- `def` [FormativeCapacity.gathered](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L311) (L311)
- `def` [FormativeCapacity.gatherWord](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L318) (L318)
- `def` [FormativeCapacity.batchState](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L329) (L329)
- `def` [FormativeCapacity.milestone](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L375) (L375)
- `def` [FormativeCapacity.charged](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L377) (L377)
- `def` [FormativeCapacity.nextFrame](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L392) (L392)
- `def` [FormativeCapacity.frame](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L394) (L394)
- `def` [FormativeCapacity.growthStates](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L408) (L408)
- `def` [FormativeCapacity.growthEvents](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L409) (L409)
- `def` [FormativeCapacity.fullStates](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L420) (L420)
- `def` [FormativeCapacity.fullEvents](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L425) (L425)
- `def` [FormativeCapacity.finiteFeed](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/FormativeCapacity.lean#L471) (L471)

</details>

<a id="module-11e52688dd69"></a>

<details>
<summary>GenerativeComparison.lean — 27 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVE-PREMISE-INTEGRATION.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean`

Imports: `Std`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [GenerativeComparison.new_realization_has_positive_relevance](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L100) | 100 |
| [GenerativeComparison.generative_extension_irreflexive](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L108) | 108 |
| [GenerativeComparison.generative_extension_transitive](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L114) | 114 |
| [GenerativeComparison.comparison_supplies_situated_reason](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L123) | 123 |
| [GenerativeComparison.coherent_selection_survives_filter](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L136) | 136 |
| [GenerativeComparison.feasible_restriction_preserves_survivor](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L150) | 150 |
| [GenerativeComparison.continual_improvement_has_no_survivor](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L162) | 162 |
| [GenerativeComparison.both_appraisals_respect_all_extensions](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L197) | 197 |
| [GenerativeComparison.tradeoff_has_opposite_strict_appraisals](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L208) | 208 |
| [GenerativeComparison.both_tradeoff_options_survive](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L213) | 213 |
| [GenerativeComparison.each_appraisal_has_a_different_coherent_selection](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L232) | 232 |

定义与类型 / Definitions and types:

- `structure` [GenerativeComparison.Inventory](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L48) (L48)
- `def` [GenerativeComparison.G0](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L52) (L52)
- `def` [GenerativeComparison.Extends](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L57) (L57)
- `def` [GenerativeComparison.GenerativeExtension](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L61) (L61)
- `def` [GenerativeComparison.ComparisonPrinciple](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L69) (L69)
- `structure` [GenerativeComparison.Situation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L73) (L73)
- `def` [GenerativeComparison.PracticalArticulation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L79) (L79)
- `def` [GenerativeComparison.SelectionCoherence](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L86) (L86)
- `def` [GenerativeComparison.Survives](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L94) (L94)
- `abbrev` [GenerativeComparison.Profile](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L177) (L177)
- `def` [GenerativeComparison.profileInventory](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L179) (L179)
- `def` [GenerativeComparison.count](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L184) (L184)
- `def` [GenerativeComparison.firstAppraisal](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L186) (L186)
- `def` [GenerativeComparison.secondAppraisal](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L188) (L188)
- `def` [GenerativeComparison.ScoreBetter](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L190) (L190)
- `def` [GenerativeComparison.tradeoffSituation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeComparison.lean#L193) (L193)

</details>

<a id="module-13036549ff30"></a>

<details>
<summary>GenerativeLossComparison.lean — 23 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVE-LOSS-COMPARISON-INTEGRATION.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean`

Imports: `Std`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [GenerativeLossComparison.strict_improvement_transport](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L34) | 34 |
| [GenerativeLossComparison.strict_rejection_transport](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L43) | 43 |
| [GenerativeLossComparison.matched_loss_reduction_preserves_priority](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L52) | 52 |
| [GenerativeLossComparison.matched_loss_increase_preserves_rejection](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L59) | 59 |
| [GenerativeLossComparison.transported_comparison_supplies_reason](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L70) | 70 |
| [GenerativeLossComparison.faithful_redescription_preserves_strict](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L81) | 81 |
| [GenerativeLossComparison.cutoff_transitive](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L107) | 107 |
| [GenerativeLossComparison.shorter_interruption_no_worse](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L111) | 111 |
| [GenerativeLossComparison.cutoff_priority_iff](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L114) | 114 |
| [GenerativeLossComparison.cutoff_rejection_iff](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L122) | 122 |
| [GenerativeLossComparison.compatible_cutoffs_disagree](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L130) | 130 |
| [GenerativeLossComparison.a_good_anchor_does_not_license_more_loss](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L137) | 137 |
| [GenerativeLossComparison.continuation_first_transitive](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L151) | 151 |
| [GenerativeLossComparison.continuation_first_still_prefers_shorter](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L155) | 155 |
| [GenerativeLossComparison.continuation_first_accepts_every_finite_loss](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L159) | 159 |
| [GenerativeLossComparison.loss_sensitivity_alone_supplies_no_cutoff](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L163) | 163 |

定义与类型 / Definitions and types:

- `def` [GenerativeLossComparison.Strict](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L25) (L25)
- `def` [GenerativeLossComparison.Transitive](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L28) (L28)
- `def` [GenerativeLossComparison.Compatible](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L31) (L31)
- `def` [GenerativeLossComparison.PracticalBridge](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L66) (L66)
- `inductive` [GenerativeLossComparison.Route](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L95) (L95)
- `def` [GenerativeLossComparison.Cutoff](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L101) (L101)
- `def` [GenerativeLossComparison.ContinuationFirst](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean#L145) (L145)

</details>

<a id="module-f873326b0c16"></a>

<details>
<summary>GenerativeTradeoff.lean — 28 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVE-TRADEOFF-INTEGRATION.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean`

Imports: `Std`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [GenerativeTradeoff.retained_actuality_receives_certified_necessity](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L77) | 77 |
| [GenerativeTradeoff.refinement_preserves_certified_necessity](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L88) | 88 |
| [GenerativeTradeoff.actual_alternative_refutes_necessity](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L97) | 97 |
| [GenerativeTradeoff.uniform_response_supplies_each_route](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L106) | 106 |
| [GenerativeTradeoff.restoration_matches_endpoint_but_retains_interruption](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L171) | 171 |
| [GenerativeTradeoff.absent_handover_makes_interruption_necessary](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L178) | 178 |
| [GenerativeTradeoff.available_handovers_are_actual_lossless_alternatives](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L188) | 188 |
| [GenerativeTradeoff.truthful_identification_can_resolve_uncertain_necessity](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L194) | 194 |
| [GenerativeTradeoff.deleting_actual_circumstance_fabricates_necessity](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L207) | 207 |
| [GenerativeTradeoff.pointwise_routes_do_not_supply_uniform_response](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L217) | 217 |
| [GenerativeTradeoff.conditional_necessity_allows_lossless_nonattainment](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L241) | 241 |

定义与类型 / Definitions and types:

- `structure` [GenerativeTradeoff.Problem](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L44) (L44)
- `def` [GenerativeTradeoff.Successful](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L50) (L50)
- `def` [GenerativeTradeoff.LosslessSuccess](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L56) (L56)
- `def` [GenerativeTradeoff.NecessaryLoss](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L62) (L62)
- `def` [GenerativeTradeoff.Certain](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L68) (L68)
- `def` [GenerativeTradeoff.UniformLossless](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L72) (L72)
- `inductive` [GenerativeTradeoff.SupportCase](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L113) (L113)
- `inductive` [GenerativeTradeoff.Response](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L119) (L119)
- `inductive` [GenerativeTradeoff.Stage](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L126) (L126)
- `structure` [GenerativeTradeoff.History](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L132) (L132)
- `def` [GenerativeTradeoff.maintained](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L136) (L136)
- `def` [GenerativeTradeoff.restored](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L140) (L140)
- `def` [GenerativeTradeoff.endpoint](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L147) (L147)
- `def` [GenerativeTradeoff.interruption](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L150) (L150)
- `def` [GenerativeTradeoff.handoverProblem](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L153) (L153)
- `def` [GenerativeTradeoff.unresolvedSide](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L165) (L165)
- `def` [GenerativeTradeoff.onlyNoHandover](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeTradeoff.lean#L168) (L168)

</details>

<a id="module-bec079c8bd79"></a>

<details>
<summary>ReconfigurableRoutes.lean — 65 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVE-CAPACITY-INTEGRATION.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean`

Imports: `FormationRoutes`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [ReconfigurableRoutes.z_common_address](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L25) | 25 |
| [ReconfigurableRoutes.z_distinct](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L31) | 31 |
| [ReconfigurableRoutes.finite_branching](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L63) | 63 |
| [ReconfigurableRoutes.old_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L75) | 75 |
| [ReconfigurableRoutes.old_trace](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L78) | 78 |
| [ReconfigurableRoutes.step_accounts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L92) | 92 |
| [ReconfigurableRoutes.trace_accounts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L110) | 110 |
| [ReconfigurableRoutes.release_preserves_products_and_history](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L118) | 118 |
| [ReconfigurableRoutes.bypass_step_progress](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L127) | 127 |
| [ReconfigurableRoutes.bypass_trace_progress](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L140) | 140 |
| [ReconfigurableRoutes.forget_bypass](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L147) | 147 |
| [ReconfigurableRoutes.old_bypass_trace](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L153) | 153 |
| [ReconfigurableRoutes.bypass_output_bound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L160) | 160 |
| [ReconfigurableRoutes.step_three_part_products](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L170) | 170 |
| [ReconfigurableRoutes.trace_three_part_products](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L188) | 188 |
| [ReconfigurableRoutes.trace_product_material_bound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L194) | 194 |
| [ReconfigurableRoutes.retaining_starved_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L203) | 203 |
| [ReconfigurableRoutes.retaining_starved_trace](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L218) | 218 |
| [ReconfigurableRoutes.unfed_step_spends](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L229) | 229 |
| [ReconfigurableRoutes.zero_work_trace_constant](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L238) | 238 |
| [ReconfigurableRoutes.small_fresh_step_no_product](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L244) | 244 |
| [ReconfigurableRoutes.small_one_work_no_product](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L254) | 254 |
| [ReconfigurableRoutes.coupled_prefix](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L271) | 271 |
| [ReconfigurableRoutes.coupled_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L278) | 278 |
| [ReconfigurableRoutes.coupled_list](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L285) | 285 |
| [ReconfigurableRoutes.manual_z](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L298) | 298 |
| [ReconfigurableRoutes.reclaim_then_z](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L306) | 306 |
| [ReconfigurableRoutes.reclaim_then_existing](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L316) | 316 |
| [ReconfigurableRoutes.reconfigured_alternatives_match_support](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L327) | 327 |
| [ReconfigurableRoutes.formed_then_reconfigured_history](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L338) | 338 |
| [ReconfigurableRoutes.final_reconfigured_costs](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L347) | 347 |
| [ReconfigurableRoutes.repeated_use_strict_threshold](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L354) | 354 |
| [ReconfigurableRoutes.retained_material_cannot_complete](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L361) | 361 |
| [ReconfigurableRoutes.two_uses_then_reclaim](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L367) | 367 |
| [ReconfigurableRoutes.two_use_ordinary_tie](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L374) | 374 |
| [ReconfigurableRoutes.direct_z_from_small_source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L390) | 390 |
| [ReconfigurableRoutes.premature_coupling_history](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L398) | 398 |
| [ReconfigurableRoutes.premature_coupling_loses_completion](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L402) | 402 |
| [ReconfigurableRoutes.premature_release_exhausts_work](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L406) | 406 |
| [ReconfigurableRoutes.common_choice_actual_history](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L413) | 413 |
| [ReconfigurableRoutes.common_can_reuse_coupling](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L421) | 421 |
| [ReconfigurableRoutes.common_can_form_z_without_release](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L426) | 426 |
| [ReconfigurableRoutes.common_can_release_then_z](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L431) | 431 |
| [ReconfigurableRoutes.common_cannot_add_two_completions](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L437) | 437 |
| [ReconfigurableRoutes.ordinary_z_keeps_more_work_and_bar](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L445) | 445 |

定义与类型 / Definitions and types:

- `def` [ReconfigurableRoutes.dyadAC](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L22) (L22)
- `def` [ReconfigurableRoutes.zForm](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L23) (L23)
- `inductive` [ReconfigurableRoutes.Event](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L33) (L33)
- `def` [ReconfigurableRoutes.advance](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L38) (L38)
- `def` [ReconfigurableRoutes.Enabled](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L45) (L45)
- `def` [ReconfigurableRoutes.Step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L54) (L54)
- `def` [ReconfigurableRoutes.process](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L55) (L55)
- `def` [ReconfigurableRoutes.oldEvents](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L57) (L57)
- `def` [ReconfigurableRoutes.events](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L60) (L60)
- `def` [ReconfigurableRoutes.children](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L61) (L61)
- `def` [ReconfigurableRoutes.Synchronized](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L85) (L85)
- `def` [ReconfigurableRoutes.bypassProcess](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L89) (L89)
- `def` [ReconfigurableRoutes.retainingProcess](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L90) (L90)
- `def` [ReconfigurableRoutes.ThreePartProducts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L168) (L168)
- `def` [ReconfigurableRoutes.coupled](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L268) (L268)
- `def` [ReconfigurableRoutes.zPending](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L292) (L292)
- `def` [ReconfigurableRoutes.zResult](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L295) (L295)
- `def` [ReconfigurableRoutes.allThree](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L365) (L365)
- `def` [ReconfigurableRoutes.prematurelyCoupled](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L396) (L396)
- `def` [ReconfigurableRoutes.commonChoice](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurableRoutes.lean#L411) (L411)

</details>

<a id="module-12ce623ea5ce"></a>

<details>
<summary>ReconfigurationCorrespondenceSamples.lean — 10 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurationCorrespondenceSamples.lean) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/README.md) · 尚无直接模块文档链接 / No direct module-documentation link found

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurationCorrespondenceSamples.lean`

Imports: `ReconfigurableRoutes`

没有扫描到显式 theorem/lemma；可能是导入、审计或定义模块。 / No explicit theorem/lemma scanned; this may be an import, audit or definition module.

定义与类型 / Definitions and types:

- `def` [ReconfigurationSamples.treeWord](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurationCorrespondenceSamples.lean#L7) (L7)
- `def` [ReconfigurationSamples.portWord](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurationCorrespondenceSamples.lean#L13) (L13)
- `def` [ReconfigurationSamples.barWord](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurationCorrespondenceSamples.lean#L17) (L17)
- `def` [ReconfigurationSamples.bit](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurationCorrespondenceSamples.lean#L22) (L22)
- `def` [ReconfigurationSamples.events](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurationCorrespondenceSamples.lean#L24) (L24)
- `def` [ReconfigurationSamples.permitted](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurationCorrespondenceSamples.lean#L30) (L30)
- `def` [ReconfigurationSamples.stateLine](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurationCorrespondenceSamples.lean#L35) (L35)
- `def` [ReconfigurationSamples.next](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurationCorrespondenceSamples.lean#L46) (L46)
- `def` [ReconfigurationSamples.testFrontiers](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurationCorrespondenceSamples.lean#L50) (L50)
- `def` [main](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ReconfigurationCorrespondenceSamples.lean#L60) (L60)

</details>

<a id="module-b49c122e730b"></a>

<details>
<summary>RoutesCorrespondenceSamples.lean — 11 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RoutesCorrespondenceSamples.lean) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RoutesCorrespondenceSamples.lean`

Imports: `FormationRoutes`

没有扫描到显式 theorem/lemma；可能是导入、审计或定义模块。 / No explicit theorem/lemma scanned; this may be an import, audit or definition module.

定义与类型 / Definitions and types:

- `def` [roleWord](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RoutesCorrespondenceSamples.lean#L6) (L6)
- `def` [treeWord](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RoutesCorrespondenceSamples.lean#L11) (L11)
- `def` [portWord](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RoutesCorrespondenceSamples.lean#L15) (L15)
- `def` [barWord](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RoutesCorrespondenceSamples.lean#L19) (L19)
- `def` [bit](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RoutesCorrespondenceSamples.lean#L24) (L24)
- `def` [events](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RoutesCorrespondenceSamples.lean#L26) (L26)
- `def` [permitted](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RoutesCorrespondenceSamples.lean#L29) (L29)
- `def` [stateLine](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RoutesCorrespondenceSamples.lean#L32) (L32)
- `def` [frontier](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RoutesCorrespondenceSamples.lean#L43) (L43)
- `def` [testFrontiers](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RoutesCorrespondenceSamples.lean#L48) (L48)
- `def` [main](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/RoutesCorrespondenceSamples.lean#L53) (L53)

</details>
