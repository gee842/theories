# Lean 具名声明 / Named Lean declarations

[返回 Lean 导航](../LEAN-INDEX.md)。本表显示当前工作源与审计入口；所有历史副本仍见 [JSON 清单](../data/lean-index.json)。这是显式声明的位置索引，不能代替命题、假设及对应论证的阅读。 / [Return to navigation](../LEAN-INDEX.md). Working sources and audit entries appear here; all historical copies remain in the JSON inventory. These are explicit declaration locations, not substitutes for statements, hypotheses and correspondence arguments.

定理／引理逐项列出；定义与类型声明列在同一模块的折叠项中。限定名由文本 namespace 推断，仅供导航；私有内部名称和自动生成名称以 Lean 为准。 / Theorems and lemmas are individually listed; definitions and type declarations share each module's foldout. Namespace-qualified names are textual hints; Lean determines private/internal and generated names.

[全部方向与模块 / All topics and modules](../LEAN-DECLARATIONS.md)

## 支持与更新 / Support and renewal

<a id="module-87b5bd85fd55"></a>

<details>
<summary>RenewalExamples.lean — 36 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CONDITIONAL-UNIVERSALITY-REVIEW.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean`

Imports: `ResourceContinuation`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [Generative.Conditional.Examples.renewal_sustain_law](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L40) | 40 |
| [Generative.Conditional.Examples.renewal_unit_enactment](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L44) | 44 |
| [Generative.Conditional.Examples.renewal_arrival_cap](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L48) | 48 |
| [Generative.Conditional.Examples.renewal_cycle](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L52) | 52 |
| [Generative.Conditional.Examples.terminal_branch](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L56) | 56 |
| [Generative.Conditional.Examples.terminal_has_no_continuation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L59) | 59 |
| [Generative.Conditional.Examples.cycle_is_lawful](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L71) | 71 |
| [Generative.Conditional.Examples.renewal_admits_infinite_execution](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L79) | 79 |
| [Generative.Conditional.Examples.same_law_admits_continuation_and_loss](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L84) | 84 |
| [Generative.Conditional.Examples.insufficient_sustain_law](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L100) | 100 |
| [Generative.Conditional.Examples.insufficient_arrival_is_always_positive](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L108) | 108 |
| [Generative.Conditional.Examples.insufficient_finite_bound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L113) | 113 |
| [Generative.Conditional.Examples.insufficient_has_no_infinite_execution](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L123) | 123 |
| [Generative.Conditional.Examples.free_sustain_law](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L146) | 146 |
| [Generative.Conditional.Examples.free_infinite_execution](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L151) | 151 |
| [Generative.Conditional.Examples.free_process_has_no_unit_enactment](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L156) | 156 |
| [Generative.Conditional.Examples.bulk_sustain_law](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L167) | 167 |
| [Generative.Conditional.Examples.bulk_has_no_uniform_arrival_cap](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L172) | 172 |
| [Generative.Conditional.Examples.bulk_single_delivery](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L178) | 178 |
| [Generative.Conditional.Examples.bulk_consumes_held](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L186) | 186 |
| [Generative.Conditional.Examples.bulk_single_delivery_then_run](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L197) | 197 |

定义与类型 / Definitions and types:

- `inductive` [Generative.Conditional.Examples.Phase](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L12) (L12)
- `inductive` [Generative.Conditional.Examples.Event](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L16) (L16)
- `inductive` [Generative.Conditional.Examples.RenewalStep](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L20) (L20)
- `def` [Generative.Conditional.Examples.renewalProcess](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L26) (L26)
- `def` [Generative.Conditional.Examples.held](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L28) (L28)
- `def` [Generative.Conditional.Examples.enacted](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L32) (L32)
- `def` [Generative.Conditional.Examples.arrived](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L36) (L36)
- `def` [Generative.Conditional.Examples.even](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L64) (L64)
- `def` [Generative.Conditional.Examples.cycleStates](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L68) (L68)
- `def` [Generative.Conditional.Examples.cycleActions](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L69) (L69)
- `def` [Generative.Conditional.Examples.insufficientProcess](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L94) (L94)
- `def` [Generative.Conditional.Examples.insufficientEnacted](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L97) (L97)
- `def` [Generative.Conditional.Examples.insufficientArrived](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L98) (L98)
- `def` [Generative.Conditional.Examples.freeProcess](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L143) (L143)
- `def` [Generative.Conditional.Examples.bulkProcess](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/RenewalExamples.lean#L164) (L164)

文本中有 21 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 21 textual `#print axioms` commands; results belong to the original verification records.

</details>

<a id="module-b17cc0c41017"></a>

<details>
<summary>ResourceContinuation.lean — 29 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/LEARNING-SUPPORT-MATH.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean`

Imports: `GenerativeCore`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [Generative.Conditional.sustain_law_pullback](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L37) | 37 |
| [Generative.Conditional.le_cancel_left](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L52) | 52 |
| [Generative.Conditional.step_then_rest](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L60) | 60 |
| [Generative.Conditional.rest_then_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L70) | 70 |
| [Generative.Conditional.support_trace_is_trace](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L92) | 92 |
| [Generative.Conditional.trace_has_support_totals](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L101) | 101 |
| [Generative.Conditional.support_trace_append](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L111) | 111 |
| [Generative.Conditional.repeat_supported_cycle](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L130) | 130 |
| [Generative.Conditional.support_trace_bound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L143) | 143 |
| [Generative.Conditional.support_cycle_arrival_covers_enactment](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L154) | 154 |
| [Generative.Conditional.support_trace_unit_enactment](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L164) | 164 |
| [Generative.Conditional.amount_le_cap_times_arrival_events](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L177) | 177 |
| [Generative.Conditional.support_trace_arrival_cap](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L184) | 184 |
| [Generative.Conditional.support_trace_length_bound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L198) | 198 |
| [Generative.Conditional.interval_total_positive_witness](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L215) | 215 |
| [Generative.Conditional.interval_total_le_of_pointwise](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L231) | 231 |
| [Generative.Conditional.interval_total_unit_bound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L238) | 238 |
| [Generative.Conditional.interval_total_cap_bound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L245) | 245 |
| [Generative.Conditional.execution_interval_bound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L257) | 257 |
| [Generative.Conditional.componentwise_execution_bound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L274) | 274 |
| [Generative.Conditional.unbounded_enactment_requires_unbounded_arrival](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L290) | 290 |
| [Generative.Conditional.infinite_unit_execution_arrival_window](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L311) | 311 |
| [Generative.Conditional.infinite_unit_execution_unbounded_arrival](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L334) | 334 |
| [Generative.Conditional.execution_interval_frequency_bound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L346) | 346 |

定义与类型 / Definitions and types:

- `def` [Generative.Conditional.SustainLaw](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L31) (L31)
- `def` [Generative.Conditional.arrivalEvent](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L49) (L49)
- `inductive` [Generative.Conditional.SupportTrace](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L81) (L81)
- `def` [Generative.Conditional.repeatWord](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L123) (L123)
- `def` [Generative.Conditional.intervalTotal](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean#L211) (L211)

文本中有 24 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 24 textual `#print axioms` commands; results belong to the original verification records.

</details>

<a id="module-bedcaae2aaa8"></a>

<details>
<summary>SupportNecessity.lean — 24 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CONDITIONAL-SUPPORT-MATH.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean`

Imports: `GenerativeCore`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [Generative.Conditional.Support.expiry_le_potential](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L44) | 44 |
| [Generative.Conditional.Support.alive_le_potential](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L70) | 70 |
| [Generative.Conditional.Support.expiry_le_rank_deadline](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L80) | 80 |
| [Generative.Conditional.Support.alive_le_rank_deadline](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L101) | 101 |
| [Generative.Conditional.Support.late_alive_requires_higher_rank](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L111) | 111 |
| [Generative.Conditional.Support.bounded_rank_deadline](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L126) | 126 |
| [Generative.Conditional.Support.no_alive_after_bounded_rank_deadline](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L139) | 139 |
| [Generative.Conditional.Support.strict_rank_bounds_type_trace](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L154) | 154 |
| [Generative.Conditional.Support.strict_rank_excludes_nonempty_type_cycle](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L167) | 167 |
| [Generative.Conditional.Support.renewing_alive_at_every_time](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L194) | 194 |
| [Generative.Conditional.Support.renewing_has_type_cycle](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L197) | 197 |
| [Generative.Conditional.Support.renewing_has_no_strict_type_rank](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L201) | 201 |
| [Generative.Conditional.Support.finiteInitial_has_type_cycle](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L220) | 220 |
| [Generative.Conditional.Support.finiteInitial_dead_after_two](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L224) | 224 |
| [Generative.Conditional.Support.infiniteChain_alive_at_every_time](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L245) | 245 |
| [Generative.Conditional.Support.infiniteChain_rank_rises](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L248) | 248 |
| [Generative.Conditional.Support.infiniteChain_has_no_nonempty_type_cycle](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L254) | 254 |
| [Generative.Conditional.Support.external_arrivals_without_internal_parents](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L263) | 263 |

定义与类型 / Definitions and types:

- `structure` [Generative.Conditional.Support.EpisodeSystem](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L25) (L25)
- `def` [Generative.Conditional.Support.Alive](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L38) (L38)
- `def` [Generative.Conditional.Support.typeProcess](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L151) (L151)
- `def` [Generative.Conditional.Support.renewing](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L181) (L181)
- `def` [Generative.Conditional.Support.finiteInitial](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L210) (L210)
- `def` [Generative.Conditional.Support.infiniteChain](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/SupportNecessity.lean#L232) (L232)

文本中有 18 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 18 textual `#print axioms` commands; results belong to the original verification records.

</details>

<a id="module-948079a4c2d6"></a>

<details>
<summary>NativePortContinuation.lean — 32 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/PROCESS-LAW-ENTRY-DEPENDENCY-MAP.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean`

Imports: `NativePacketProcess`, `ResourceContinuation`, `Depletion`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [Generative.NativePortContinuation.cancel_right](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L46) | 46 |
| [Generative.NativePortContinuation.sub_add_restore](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L51) | 51 |
| [Generative.NativePortContinuation.add_sub_self_left](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L61) | 61 |
| [Generative.NativePortContinuation.chain](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L67) | 67 |
| [Generative.NativePortContinuation.continues_refl](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L76) | 76 |
| [Generative.NativePortContinuation.continues_trans](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L79) | 79 |
| [Generative.NativePortContinuation.enact_continues](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L86) | 86 |
| [Generative.NativePortContinuation.convert_continues](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L94) | 94 |
| [Generative.NativePortContinuation.phase_continues](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L101) | 101 |
| [Generative.NativePortContinuation.supported_continues](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L105) | 105 |
| [Generative.NativePortContinuation.execute_conserves](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L112) | 112 |
| [Generative.NativePortContinuation.step_continues](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L138) | 138 |
| [Generative.NativePortContinuation.trace_continues](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L146) | 146 |
| [Generative.NativePortContinuation.step_sustained_exact](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L159) | 159 |
| [Generative.NativePortContinuation.port_sustain_law](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L176) | 176 |
| [Generative.NativePortContinuation.completed_shape](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L183) | 183 |
| [Generative.NativePortContinuation.draw_positive](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L204) | 204 |
| [Generative.NativePortContinuation.step_enacts](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L209) | 209 |
| [Generative.NativePortContinuation.port_history_bound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L224) | 224 |
| [Generative.NativePortContinuation.continuing_port_needs_arrivals](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L233) | 233 |
| [Generative.NativePortContinuation.arrival_amount](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L245) | 245 |
| [Generative.NativePortContinuation.enact_lowers_potential](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L251) | 251 |
| [Generative.NativePortContinuation.convert_keeps_potential_bound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L258) | 258 |
| [Generative.NativePortContinuation.phase_keeps_potential](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L274) | 274 |
| [Generative.NativePortContinuation.step_lowers_potential](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L278) | 278 |
| [Generative.NativePortContinuation.port_history_length](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L290) | 290 |
| [Generative.NativePortContinuation.port_cannot_continue_indefinitely](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L295) | 295 |

定义与类型 / Definitions and types:

- `def` [Generative.NativePortContinuation.Continues](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L39) (L39)
- `def` [Generative.NativePortContinuation.enactedBy](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L153) (L153)
- `def` [Generative.NativePortContinuation.arrivedBy](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L156) (L156)
- `def` [Generative.NativePortContinuation.yieldPerUnit](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L243) (L243)
- `def` [Generative.NativePortContinuation.potential](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean#L249) (L249)

文本中有 27 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 27 textual `#print axioms` commands; results belong to the original verification records.

</details>

<a id="module-b8df4e3120cc"></a>

<details>
<summary>RenewalAccounting.lean — 27 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/PORT-RENEWAL-LAW-CLOSURE.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean`

Imports: `GenerativeCore`, `Depletion`, `RenewalBasics`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [Generative.Conditional.Renewal.weighted_append](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L75) | 75 |
| [Generative.Conditional.Renewal.weighted_aged](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L84) | 84 |
| [Generative.Conditional.Renewal.weighted_formed_le](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L111) | 111 |
| [Generative.Conditional.Renewal.formation_exceeds_opening](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L127) | 127 |
| [Generative.Conditional.Renewal.opening_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L167) | 167 |
| [Generative.Conditional.Renewal.short_opening_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L190) | 190 |
| [Generative.Conditional.Renewal.life_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L206) | 206 |
| [Generative.Conditional.Renewal.short_renewal_depletes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L228) | 228 |
| [Generative.Conditional.Renewal.short_renewal_deadline](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L250) | 250 |
| [Generative.Conditional.Renewal.short_kinds_cannot_renew_forever](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L260) | 260 |
| [Generative.Conditional.Renewal.closedOpenShort_ticks](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L289) | 289 |
| [Generative.Conditional.Renewal.closed_open_short_cannot_renew_forever](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L303) | 303 |

定义与类型 / Definitions and types:

- `structure` [Generative.Conditional.Renewal.Token](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L31) (L31)
- `structure` [Generative.Conditional.Renewal.Config](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L36) (L36)
- `structure` [Generative.Conditional.Renewal.ChannelLaw](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L41) (L41)
- `def` [Generative.Conditional.Renewal.aged](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L50) (L50)
- `def` [Generative.Conditional.Renewal.weighted](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L56) (L56)
- `def` [Generative.Conditional.Renewal.opened](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L61) (L61)
- `def` [Generative.Conditional.Renewal.formed](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L66) (L66)
- `def` [Generative.Conditional.Renewal.formation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L71) (L71)
- `def` [Generative.Conditional.Renewal.channelProcess](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L141) (L141)
- `def` [Generative.Conditional.Renewal.Live](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L148) (L148)
- `def` [Generative.Conditional.Renewal.renewingProcess](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L151) (L151)
- `def` [Generative.Conditional.Renewal.openingPotential](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L155) (L155)
- `def` [Generative.Conditional.Renewal.lifePotential](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L159) (L159)
- `def` [Generative.Conditional.Renewal.renewalPotential](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L162) (L162)
- `def` [Generative.Conditional.Renewal.closedOpenShort](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean#L282) (L282)

文本中有 12 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 12 textual `#print axioms` commands; results belong to the original verification records.

</details>

<a id="module-77ecd2c775da"></a>

<details>
<summary>RenewalBasics.lean — 35 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/README.md) · 尚无直接模块文档链接 / No direct module-documentation link found

`experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [Generative.Conditional.Renewal.mem_cons_split](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L19) | 19 |
| [Generative.Conditional.Renewal.mem_singleton_eq](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L24) | 24 |
| [Generative.Conditional.Renewal.mem_append_split](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L29) | 29 |
| [Generative.Conditional.Renewal.append_nil_eq](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L41) | 41 |
| [Generative.Conditional.Renewal.append_assoc_eq](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L45) | 45 |
| [Generative.Conditional.Renewal.length_append_eq](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L50) | 50 |
| [Generative.Conditional.Renewal.eq_of_mem_replicate_eq](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L56) | 56 |
| [Generative.Conditional.Renewal.succ_ne_zero_of](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L66) | 66 |
| [Generative.Conditional.Renewal.add_right_cancel_eq](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L68) | 68 |
| [Generative.Conditional.Renewal.add_left_cancel_eq](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L72) | 72 |
| [Generative.Conditional.Renewal.le_of_add_le_add_right_of](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L76) | 76 |
| [Generative.Conditional.Renewal.le_of_add_le_add_left_of](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L80) | 80 |
| [Generative.Conditional.Renewal.add_mul_eq](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L84) | 84 |
| [Generative.Conditional.Renewal.mul_assoc_eq](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L87) | 87 |
| [Generative.Conditional.Renewal.add_sub_cancel_eq](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L91) | 91 |
| [Generative.Conditional.Renewal.add_sub_cancel_left_eq](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L98) | 98 |
| [Generative.Conditional.Renewal.sub_add_cancel_of_le](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L102) | 102 |
| [Generative.Conditional.Renewal.add_sub_of_le_eq](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L106) | 106 |
| [Generative.Conditional.Renewal.le_sub_of_add_le_of](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L110) | 110 |
| [Generative.Conditional.Renewal.sub_eq_zero_of_le_of](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L115) | 115 |
| [Generative.Conditional.Renewal.sub_le_of_le_add_of](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L122) | 122 |
| [Generative.Conditional.Renewal.add_le_of_le_sub_of](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L130) | 130 |
| [Generative.Conditional.Renewal.min_eq_left_of_le](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L135) | 135 |
| [Generative.Conditional.Renewal.min_eq_right_of_le](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L139) | 139 |
| [Generative.Conditional.Renewal.le_min_of](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L146) | 146 |
| [Generative.Conditional.Renewal.min_le_left_of](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L154) | 154 |
| [Generative.Conditional.Renewal.min_le_right_of](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L162) | 162 |
| [Generative.Conditional.Renewal.min_zero_eq](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L170) | 170 |
| [Generative.Conditional.Renewal.add_le_add_of](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L173) | 173 |
| [Generative.Conditional.Renewal.le_of_add_le_left_of](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L176) | 176 |
| [Generative.Conditional.Renewal.le_of_add_le_right_of](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L179) | 179 |
| [Generative.Conditional.Renewal.lt_of_add_one_le_of](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L182) | 182 |
| [Generative.Conditional.Renewal.add_one_le_of_lt_of](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L184) | 184 |
| [Generative.Conditional.Renewal.pos_of_ne_zero_of](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L186) | 186 |
| [Generative.Conditional.Renewal.eq_zero_or_pos_of](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalBasics.lean#L191) | 191 |

文本中有 35 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 35 textual `#print axioms` commands; results belong to the original verification records.

</details>

<a id="module-5fca0507b290"></a>

<details>
<summary>RenewalCharacterization.lean — 68 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/PLURAL-CLAIMS-INTEGRATION.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean`

Imports: `RenewalSufficiency`, `RenewalLink`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [Generative.Conditional.Renewal.block_within](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L75) | 75 |
| [Generative.Conditional.Renewal.steady_within](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L87) | 87 |
| [Generative.Conditional.Renewal.mem_positivePart](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L110) | 110 |
| [Generative.Conditional.Renewal.positivePart_mem](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L125) | 125 |
| [Generative.Conditional.Renewal.positivePart_balance](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L139) | 139 |
| [Generative.Conditional.Renewal.positivePart_renewing](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L157) | 157 |
| [Generative.Conditional.Renewal.standingExecution_live](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L186) | 186 |
| [Generative.Conditional.Renewal.self_renewing_renews_forever](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L196) | 196 |
| [Generative.Conditional.Renewal.range_search](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L203) | 203 |
| [Generative.Conditional.Renewal.tick_search](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L216) | 216 |
| [Generative.Conditional.Renewal.weighted_formed_eq](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L225) | 225 |
| [Generative.Conditional.Renewal.spanOpening_le_formation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L230) | 230 |
| [Generative.Conditional.Renewal.spanOpening_lt_formation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L240) | 240 |
| [Generative.Conditional.Renewal.characterization_cancel](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L264) | 264 |
| [Generative.Conditional.Renewal.characterization_cancel_short](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L268) | 268 |
| [Generative.Conditional.Renewal.tick_potential](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L279) | 279 |
| [Generative.Conditional.Renewal.tick_potential_short](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L287) | 287 |
| [Generative.Conditional.Renewal.stretch_potential](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L298) | 298 |
| [Generative.Conditional.Renewal.stretch_potential_short](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L313) | 313 |
| [Generative.Conditional.Renewal.cycle_with_tail](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L337) | 337 |
| [Generative.Conditional.Renewal.excess_population](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L366) | 366 |
| [Generative.Conditional.Renewal.keeps_decide](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L389) | 389 |
| [Generative.Conditional.Renewal.live_keeps_everything](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L395) | 395 |
| [Generative.Conditional.Renewal.support_closed_append](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L399) | 399 |
| [Generative.Conditional.Renewal.traced_support_closed](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L413) | 413 |
| [Generative.Conditional.Renewal.characterization_lt_of_add_lt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L425) | 425 |
| [Generative.Conditional.Renewal.kept_kind_descends](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L434) | 434 |
| [Generative.Conditional.Renewal.characterization_add_succ_le](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L469) | 469 |
| [Generative.Conditional.Renewal.characterization_le_of_add_lt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L474) | 474 |
| [Generative.Conditional.Renewal.kept_through_window_has_population](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L486) | 486 |
| [Generative.Conditional.Renewal.renewal_dichotomy_keeping](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L620) | 620 |
| [Generative.Conditional.Renewal.renewal_dichotomy](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L648) | 648 |
| [Generative.Conditional.Renewal.span_le_longest](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L663) | 663 |
| [Generative.Conditional.Renewal.renews_forever_has_self_renewing_population](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L669) | 669 |
| [Generative.Conditional.Renewal.renewal_closure_theorem](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L682) | 682 |
| [Generative.Conditional.Renewal.steady_contains_fresh](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L688) | 688 |
| [Generative.Conditional.Renewal.renewal_keeping_theorem](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L703) | 703 |
| [Generative.Conditional.Renewal.no_keeping_population_deadline](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L726) | 726 |
| [Generative.Conditional.Renewal.no_self_renewing_population_deadline](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L741) | 741 |
| [Generative.Conditional.Renewal.opened_le_weighted](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L752) | 752 |
| [Generative.Conditional.Renewal.length_le_formation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L767) | 767 |
| [Generative.Conditional.Renewal.spanOpening_le_length](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L777) | 777 |
| [Generative.Conditional.Renewal.potential_growth](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L791) | 791 |
| [Generative.Conditional.Renewal.potential_bound](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L809) | 809 |
| [Generative.Conditional.Renewal.no_keeping_population_explicit_deadline](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L834) | 834 |
| [Generative.Conditional.Renewal.no_self_renewing_population_explicit_deadline](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L853) | 853 |
| [Generative.Conditional.Renewal.characterization_shuffle](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L866) | 866 |
| [Generative.Conditional.Renewal.closed_open_short_has_no_self_renewing_population](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L870) | 870 |
| [Generative.Conditional.Renewal.dangling_closure_falls_short](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L901) | 901 |
| [Generative.Conditional.Renewal.dangling_kind_outside_every_closure](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L909) | 909 |
| [Generative.Conditional.Renewal.dangling_support_renews_forever](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L921) | 921 |
| [Generative.Conditional.Renewal.lapsing_closure_renews_forever](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L939) | 939 |
| [Generative.Conditional.Renewal.lapsing_balance](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L944) | 944 |
| [Generative.Conditional.Renewal.lapsing_correction_gap](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L957) | 957 |
| [Generative.Conditional.Renewal.lapsing_correction_cannot_be_kept](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L982) | 982 |

定义与类型 / Definitions and types:

- `def` [Generative.Conditional.Renewal.SupportClosed](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L61) (L61)
- `def` [Generative.Conditional.Renewal.SelfRenewing](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L66) (L66)
- `def` [Generative.Conditional.Renewal.RenewsForever](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L70) (L70)
- `def` [Generative.Conditional.Renewal.steadyExecution](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L96) (L96)
- `def` [Generative.Conditional.Renewal.positivePart](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L106) (L106)
- `def` [Generative.Conditional.Renewal.standingExecution](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L179) (L179)
- `def` [Generative.Conditional.Renewal.potential](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L276) (L276)
- `def` [Generative.Conditional.Renewal.Keeps](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L382) (L382)
- `def` [Generative.Conditional.Renewal.KeepsForever](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L386) (L386)
- `def` [Generative.Conditional.Renewal.renewalWindow](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L719) (L719)
- `def` [Generative.Conditional.Renewal.renewalGrowth](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L824) (L824)
- `def` [Generative.Conditional.Renewal.danglingSupport](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L894) (L894)
- `def` [Generative.Conditional.Renewal.lapsingCorrection](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalCharacterization.lean#L932) (L932)

文本中有 55 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 55 textual `#print axioms` commands; results belong to the original verification records.

</details>

<a id="module-35b608afeb1a"></a>

<details>
<summary>RenewalClosure.lean — 25 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/README.md) · 尚无直接模块文档链接 / No direct module-documentation link found

`experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean`

Imports: `GenerativeCore`, `SupportNecessity`, `RenewalBasics`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [Generative.Conditional.Renewal.Walk.snoc](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L49) | 49 |
| [Generative.Conditional.Renewal.Walk.length_pos](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L55) | 55 |
| [Generative.Conditional.Renewal.Walk.end_mem](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L61) | 61 |
| [Generative.Conditional.Renewal.Walk.split_aux](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L67) | 67 |
| [Generative.Conditional.Renewal.Walk.split](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L104) | 104 |
| [Generative.Conditional.Renewal.Walk.start_mem](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L109) | 109 |
| [Generative.Conditional.Renewal.Walk.trace](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L116) | 116 |
| [Generative.Conditional.Renewal.Walk.after_start](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L128) | 128 |
| [Generative.Conditional.Renewal.Walk.before_end](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L146) | 146 |
| [Generative.Conditional.Renewal.Walk.predecessor](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L164) | 164 |
| [Generative.Conditional.Renewal.Walk.successor](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L175) | 175 |
| [Generative.Conditional.Renewal.Walk.end_predecessor](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L195) | 195 |
| [Generative.Conditional.Renewal.closed_walk_dependence_closed](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L215) | 215 |
| [Generative.Conditional.Renewal.contains_or_drawn_from](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L241) | 241 |
| [Generative.Conditional.Renewal.duplicate_of_long](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L271) | 271 |
| [Generative.Conditional.Renewal.support_walk](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L297) | 297 |
| [Generative.Conditional.Renewal.late_occurrence_descends_from_realized_closure](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L336) | 336 |
| [Generative.Conditional.Renewal.late_occurrence_requires_type_cycle](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L380) | 380 |
| [Generative.Conditional.Renewal.acyclic_support_deadline](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L393) | 393 |
| [Generative.Conditional.Renewal.episode_acyclic_deadline](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L422) | 422 |
| [Generative.Conditional.Renewal.episode_late_life_descends_from_realized_closure](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L440) | 440 |

定义与类型 / Definitions and types:

- `structure` [Generative.Conditional.Renewal.OccurrenceSupport](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L33) (L33)
- `inductive` [Generative.Conditional.Renewal.Walk](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L44) (L44)
- `def` [Generative.Conditional.Renewal.DependenceClosed](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L211) (L211)
- `def` [Generative.Conditional.Renewal.episodeSupport](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalClosure.lean#L405) (L405)

文本中有 21 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 21 textual `#print axioms` commands; results belong to the original verification records.

</details>

<a id="module-a218916039de"></a>

<details>
<summary>RenewalConfigurations.lean — 37 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/README.md) · 尚无直接模块文档链接 / No direct module-documentation link found

`experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean`

Imports: `RenewalCharacterization`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [Generative.Conditional.Renewal.opened_one_pos](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L46) | 46 |
| [Generative.Conditional.Renewal.alive_token_live](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L59) | 59 |
| [Generative.Conditional.Renewal.dead_stays_dead](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L64) | 64 |
| [Generative.Conditional.Renewal.renewable_live_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L102) | 102 |
| [Generative.Conditional.Renewal.renewable_of_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L109) | 109 |
| [Generative.Conditional.Renewal.renewable_iff_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L121) | 121 |
| [Generative.Conditional.Renewal.renewability_not_generated](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L129) | 129 |
| [Generative.Conditional.Renewal.mem_agedN](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L149) | 149 |
| [Generative.Conditional.Renewal.configurations_enlarge_balance](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L162) | 162 |
| [Generative.Conditional.Renewal.renewable_of_more](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L196) | 196 |
| [Generative.Conditional.Renewal.mem_aged_of_kept](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L217) | 217 |
| [Generative.Conditional.Renewal.agedN_empty](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L234) | 234 |
| [Generative.Conditional.Renewal.configurations_build_balance](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L249) | 249 |
| [Generative.Conditional.Renewal.build_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L260) | 260 |
| [Generative.Conditional.Renewal.build_live](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L292) | 292 |
| [Generative.Conditional.Renewal.le_longer_left](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L309) | 309 |
| [Generative.Conditional.Renewal.le_longer_right](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L317) | 317 |
| [Generative.Conditional.Renewal.configurations_sub_succ_lt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L331) | 331 |
| [Generative.Conditional.Renewal.configurations_sub_succ_add_one](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L335) | 335 |
| [Generative.Conditional.Renewal.seeded_positivePart](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L341) | 341 |
| [Generative.Conditional.Renewal.formation_le_mul](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L345) | 345 |
| [Generative.Conditional.Renewal.seeded_renewable](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L355) | 355 |
| [Generative.Conditional.Renewal.balanced_population](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L411) | 411 |
| [Generative.Conditional.Renewal.young_token_renewable](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L415) | 415 |
| [Generative.Conditional.Renewal.last_tick_not_renewable](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L421) | 421 |
| [Generative.Conditional.Renewal.young_token_without_reserve_not_renewable](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L444) | 444 |
| [Generative.Conditional.Renewal.renewability_not_function_of_reserve_and_kinds](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L474) | 474 |
| [Generative.Conditional.Renewal.renewability_not_function_of_tokens](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L483) | 483 |
| [Generative.Conditional.Renewal.keeping_and_losing_renewal](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L494) | 494 |

定义与类型 / Definitions and types:

- `def` [Generative.Conditional.Renewal.Renewable](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L43) (L43)
- `def` [Generative.Conditional.Renewal.History.next](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L83) (L83)
- `def` [Generative.Conditional.Renewal.History.cons](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L89) (L89)
- `def` [Generative.Conditional.Renewal.agedN](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L145) (L145)
- `def` [Generative.Conditional.Renewal.History.enlarge](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L171) (L171)
- `def` [Generative.Conditional.Renewal.Seeded](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L214) (L214)
- `def` [Generative.Conditional.Renewal.build](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L257) (L257)
- `def` [Generative.Conditional.Renewal.buildLength](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalConfigurations.lean#L328) (L328)

文本中有 29 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 29 textual `#print axioms` commands; results belong to the original verification records.

</details>

<a id="module-28c0ce8386f8"></a>

<details>
<summary>RenewalLink.lean — 24 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/README.md) · 尚无直接模块文档链接 / No direct module-documentation link found

`experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean`

Imports: `RenewalClosure`, `RenewalAccounting`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [Generative.Conditional.Renewal.link_add_one_comm](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L33) | 33 |
| [Generative.Conditional.Renewal.link_le_of_add_eq](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L36) | 36 |
| [Generative.Conditional.Renewal.mem_aged](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L39) | 39 |
| [Generative.Conditional.Renewal.mem_formed](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L60) | 60 |
| [Generative.Conditional.Renewal.token_origin](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L88) | 88 |
| [Generative.Conditional.Renewal.le_maxOver](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L117) | 117 |
| [Generative.Conditional.Renewal.History.settled_within](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L144) | 144 |
| [Generative.Conditional.Renewal.step_within](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L165) | 165 |
| [Generative.Conditional.Renewal.execution_within](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L181) | 181 |
| [Generative.Conditional.Renewal.execution_formation_supported](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L188) | 188 |
| [Generative.Conditional.Renewal.live_has_alive_token](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L236) | 236 |
| [Generative.Conditional.Renewal.alive_token_recent_formation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L251) | 251 |
| [Generative.Conditional.Renewal.live_late_has_recent_formation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L275) | 275 |
| [Generative.Conditional.Renewal.live_late_descends_from_realized_closure](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L288) | 288 |
| [Generative.Conditional.Renewal.find_or_none](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L327) | 327 |
| [Generative.Conditional.Renewal.endless_renewal_needs_closure_and_adequate_kind](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L344) | 344 |

定义与类型 / Definitions and types:

- `structure` [Generative.Conditional.Renewal.History](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L72) (L72)
- `def` [Generative.Conditional.Renewal.WithinSpan](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L78) (L78)
- `structure` [Generative.Conditional.Renewal.Execution](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L83) (L83)
- `def` [Generative.Conditional.Renewal.maxOver](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L113) (L113)
- `def` [Generative.Conditional.Renewal.History.shift](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L133) (L133)
- `def` [Generative.Conditional.Renewal.History.settle](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L139) (L139)
- `def` [Generative.Conditional.Renewal.History.settled](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L161) (L161)
- `def` [Generative.Conditional.Renewal.executionSupport](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalLink.lean#L228) (L228)

文本中有 16 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 16 textual `#print axioms` commands; results belong to the original verification records.

</details>

<a id="module-8149a0ba6370"></a>

<details>
<summary>RenewalPremises.lean — 26 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/REGENERATIVE-DIVERSITY-MATH.md) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/README.md)

`experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean`

Imports: `RenewalConfigurations`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [Generative.Conditional.Renewal.liveFor_zero](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L50) | 50 |
| [Generative.Conditional.Renewal.liveFor_of_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L56) | 56 |
| [Generative.Conditional.Renewal.formed_replicate](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L66) | 66 |
| [Generative.Conditional.Renewal.aged_replicate_two](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L74) | 74 |
| [Generative.Conditional.Renewal.aged_replicate_one](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L82) | 82 |
| [Generative.Conditional.Renewal.chain_not_supported](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L101) | 101 |
| [Generative.Conditional.Renewal.chain_has_no_self_renewing_population](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L114) | 114 |
| [Generative.Conditional.Renewal.chain_renews_forever](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L134) | 134 |
| [Generative.Conditional.Renewal.infinitely_many_kinds_break_the_equivalence](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L139) | 139 |
| [Generative.Conditional.Renewal.free_formation_closed_members](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L173) | 173 |
| [Generative.Conditional.Renewal.free_formation_short](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L190) | 190 |
| [Generative.Conditional.Renewal.free_formation_has_no_self_renewing_population](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L202) | 202 |
| [Generative.Conditional.Renewal.free_formation_complete](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L215) | 215 |
| [Generative.Conditional.Renewal.free_formation_histories_end](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L223) | 223 |
| [Generative.Conditional.Renewal.formation_replicate_free](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L230) | 230 |
| [Generative.Conditional.Renewal.opened_replicate_free](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L237) | 237 |
| [Generative.Conditional.Renewal.cycle_lives](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L247) | 247 |
| [Generative.Conditional.Renewal.free_formation_lives_long](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L265) | 265 |
| [Generative.Conditional.Renewal.zero_demand_defeats_initial_deadline](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L331) | 331 |

定义与类型 / Definitions and types:

- `def` [Generative.Conditional.Renewal.History.idle](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L40) (L40)
- `def` [Generative.Conditional.Renewal.LiveFor](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L47) (L47)
- `def` [Generative.Conditional.Renewal.chainLaw](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L93) (L93)
- `def` [Generative.Conditional.Renewal.chainHistory](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L123) (L123)
- `inductive` [Generative.Conditional.Renewal.SeedKind](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L147) (L147)
- `def` [Generative.Conditional.Renewal.freeFormation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L155) (L155)
- `def` [Generative.Conditional.Renewal.freeStart](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalPremises.lean#L261) (L261)

文本中有 19 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 19 textual `#print axioms` commands; results belong to the original verification records.

</details>

<a id="module-c1beae045284"></a>

<details>
<summary>RenewalSufficiency.lean — 36 explicit declarations</summary>

[原源码 / Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean) · [包说明 / Package notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/README.md) · 尚无直接模块文档链接 / No direct module-documentation link found

`experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean`

Imports: `RenewalAccounting`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [Generative.Conditional.Renewal.aged_append](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L52) | 52 |
| [Generative.Conditional.Renewal.opened_append](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L62) | 62 |
| [Generative.Conditional.Renewal.sufficiency_sub_ne_zero_of_lt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L70) | 70 |
| [Generative.Conditional.Renewal.sufficiency_not_lt_of_sub_le_one](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L76) | 76 |
| [Generative.Conditional.Renewal.sufficiency_lt_of_not_sub_le_one](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L79) | 79 |
| [Generative.Conditional.Renewal.aged_block](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L84) | 84 |
| [Generative.Conditional.Renewal.block_beyond](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L99) | 99 |
| [Generative.Conditional.Renewal.formed_eq_block_zero](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L108) | 108 |
| [Generative.Conditional.Renewal.steady_shift](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L118) | 118 |
| [Generative.Conditional.Renewal.steady_fixed](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L126) | 126 |
| [Generative.Conditional.Renewal.opened_block](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L132) | 132 |
| [Generative.Conditional.Renewal.capped_step](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L149) | 149 |
| [Generative.Conditional.Renewal.sum_map_add](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L157) | 157 |
| [Generative.Conditional.Renewal.sum_map_zero](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L165) | 165 |
| [Generative.Conditional.Renewal.sufficiency_sum_map_congr](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L172) | 172 |
| [Generative.Conditional.Renewal.opened_steady](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L181) | 181 |
| [Generative.Conditional.Renewal.spanOpening_eq](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L191) | 191 |
| [Generative.Conditional.Renewal.mem_block](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L201) | 201 |
| [Generative.Conditional.Renewal.block_one_survives](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L214) | 214 |
| [Generative.Conditional.Renewal.steady_renews](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L226) | 226 |
| [Generative.Conditional.Renewal.steady_endless](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L258) | 258 |
| [Generative.Conditional.Renewal.formation_append](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L268) | 268 |
| [Generative.Conditional.Renewal.spanOpening_append](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L276) | 276 |
| [Generative.Conditional.Renewal.formation_replicate](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L284) | 284 |
| [Generative.Conditional.Renewal.spanOpening_replicate](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L291) | 291 |
| [Generative.Conditional.Renewal.balanced_of_each](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L300) | 300 |
| [Generative.Conditional.Renewal.balanced_closure_renews](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L310) | 310 |
| [Generative.Conditional.Renewal.mem_append_replicate](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L319) | 319 |
| [Generative.Conditional.Renewal.append_nonempty](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L325) | 325 |
| [Generative.Conditional.Renewal.balanced_with_excess](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L331) | 331 |
| [Generative.Conditional.Renewal.excess_supported_by_closure_renews](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L343) | 343 |
| [Generative.Conditional.Renewal.closed_open_balanced_renews_forever](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L381) | 381 |

定义与类型 / Definitions and types:

- `def` [Generative.Conditional.Renewal.block](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L37) (L37)
- `def` [Generative.Conditional.Renewal.steady](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L43) (L43)
- `def` [Generative.Conditional.Renewal.spanOpening](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L48) (L48)
- `def` [Generative.Conditional.Renewal.closedOpenBalanced](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalSufficiency.lean#L372) (L372)

文本中有 32 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 32 textual `#print axioms` commands; results belong to the original verification records.

</details>
