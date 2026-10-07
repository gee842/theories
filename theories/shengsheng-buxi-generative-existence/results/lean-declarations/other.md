# Lean 具名声明 / Named Lean declarations

[返回 Lean 导航](../LEAN-INDEX.md)。本表显示当前工作源与审计入口；所有历史副本仍见 [JSON 清单](../data/lean-index.json)。这是显式声明的位置索引，不能代替命题、假设及对应论证的阅读。 / [Return to navigation](../LEAN-INDEX.md). Working sources and audit entries appear here; all historical copies remain in the JSON inventory. These are explicit declaration locations, not substitutes for statements, hypotheses and correspondence arguments.

定理／引理逐项列出；定义与类型声明列在同一模块的折叠项中。限定名由文本 namespace 推断，仅供导航；私有内部名称和自动生成名称以 Lean 为准。 / Theorems and lemmas are individually listed; definitions and type declarations share each module's foldout. Namespace-qualified names are textual hints; Lean determines private/internal and generated names.

[全部方向与模块 / All topics and modules](../LEAN-DECLARATIONS.md)

## 其他形式研究 / Other formal studies

<a id="module-e2e5c347dc5a"></a>

<details>
<summary>MarketGenerativity.lean — 71 explicit declarations</summary>

[原源码 / Source](../../../../experiments/market-generativity/formal/MarketGenerativity.lean) · [研究 / Study](../../../../_process/research/2026-10-05-generative-foundation-review/foundation-assessment/MARKET-LEAN-REVIEW.md) · [包说明 / Package notes](../../../../experiments/market-generativity/formal/README.md)

`experiments/market-generativity/formal/MarketGenerativity.lean`

Imports: `Std`

| 定理／引理 / Theorem or lemma | 源行 / Line |
|---|---:|
| [MarketGenerativity.profits_difference](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L25) | 25 |
| [MarketGenerativity.clip_bounds](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L31) | 31 |
| [MarketGenerativity.clip_preserves_floor](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L35) | 35 |
| [MarketGenerativity.payment_guard](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L40) | 40 |
| [MarketGenerativity.no_unfunded_activation](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L45) | 45 |
| [MarketGenerativity.reserve_accounting](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L50) | 50 |
| [MarketGenerativity.reserve_preserves_floor](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L56) | 56 |
| [MarketGenerativity.gap_monotone](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L62) | 62 |
| [MarketGenerativity.share_step_bounds](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L69) | 69 |
| [MarketGenerativity.share_strictly_increases](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L83) | 83 |
| [MarketGenerativity.influence_preserves_ceiling](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L91) | 91 |
| [MarketGenerativity.quality_preserves_floor](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L109) | 109 |
| [MarketGenerativity.support_preserves_floor](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L128) | 128 |
| [MarketGenerativity.rectangle_one_step](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L205) | 205 |
| [MarketGenerativity.rectangle_all_times](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L259) | 259 |
| [MarketGenerativity.viable_guarded_step](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L282) | 282 |
| [MarketGenerativity.failed_market_absorbing](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L291) | 291 |
| [MarketGenerativity.safe_history_never_fails](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L299) | 299 |
| [MarketGenerativity.example_certificate](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L331) | 331 |
| [MarketGenerativity.example_safe](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L334) | 334 |
| [MarketGenerativity.example_worst_admissible](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L337) | 337 |
| [MarketGenerativity.example_strict_gap](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L341) | 341 |
| [MarketGenerativity.example_one_step](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L345) | 345 |
| [MarketGenerativity.example_arbitrary_history](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L353) | 353 |
| [MarketGenerativity.example_threshold](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L360) | 360 |
| [MarketGenerativity.profitable_depletion](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L365) | 365 |
| [MarketGenerativity.capture_overwhelms_correction](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L372) | 372 |
| [MarketGenerativity.later_receipt_cannot_pay_earlier_correction](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L378) | 378 |
| [MarketGenerativity.one_support_cannot_substitute_for_another](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L384) | 384 |
| [MarketGenerativity.no_entry_at_zero](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L391) | 391 |
| [MarketGenerativity.budget_overflow_is_not_creation](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L394) | 394 |
| [MarketGenerativity.market_uses_accounting](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L398) | 398 |
| [MarketGenerativity.funded_total_accounting](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L404) | 404 |
| [MarketGenerativity.quality_corner_lower](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L415) | 415 |
| [MarketGenerativity.influence_corner_upper](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L431) | 431 |
| [MarketGenerativity.collar_certificate](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L447) | 447 |
| [MarketGenerativity.collar_recovers](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L450) | 450 |
| [MarketGenerativity.excluded_recipient_is_harmed](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L504) | 504 |
| [MarketGenerativity.excluded_recipient_harm_does_not_stop_market](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L508) | 508 |

定义与类型 / Definitions and types:

- `def` [MarketGenerativity.clip01](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L9) (L9)
- `def` [MarketGenerativity.profitR](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L10) (L10)
- `def` [MarketGenerativity.profitE](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L11) (L11)
- `def` [MarketGenerativity.gap](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L12) (L12)
- `def` [MarketGenerativity.shareStep](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L13) (L13)
- `def` [MarketGenerativity.influenceStep](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L14) (L14)
- `def` [MarketGenerativity.installed](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L15) (L15)
- `def` [MarketGenerativity.qualityStep](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L16) (L16)
- `def` [MarketGenerativity.reserveStep](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L18) (L18)
- `def` [MarketGenerativity.reserveSurplus](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L20) (L20)
- `def` [MarketGenerativity.supportStep](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L22) (L22)
- `structure` [MarketGenerativity.Parameters](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L142) (L142)
- `structure` [MarketGenerativity.Bounds](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L147) (L147)
- `structure` [MarketGenerativity.State](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L151) (L151)
- `structure` [MarketGenerativity.Disturbance](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L155) (L155)
- `structure` [MarketGenerativity.Certificate](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L159) (L159)
- `structure` [MarketGenerativity.Safe](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L183) (L183)
- `def` [MarketGenerativity.Admissible](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L194) (L194)
- `def` [MarketGenerativity.operatingStep](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L197) (L197)
- `def` [MarketGenerativity.history](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L254) (L254)
- `def` [MarketGenerativity.essentialReady](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L269) (L269)
- `def` [MarketGenerativity.guardedStep](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L276) (L276)
- `def` [MarketGenerativity.guardedHistory](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L294) (L294)
- `def` [MarketGenerativity.exampleParameters](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L314) (L314)
- `def` [MarketGenerativity.exampleBounds](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L321) (L321)
- `def` [MarketGenerativity.exampleState](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L325) (L325)
- `def` [MarketGenerativity.exampleWorstShock](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L328) (L328)
- `def` [MarketGenerativity.collarBounds](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L444) (L444)
- `def` [MarketGenerativity.exclusionParameters](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L486) (L486)
- `def` [MarketGenerativity.exclusionBounds](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L494) (L494)
- `def` [MarketGenerativity.exclusionState](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L498) (L498)
- `def` [MarketGenerativity.exclusionDisturbance](../../../../experiments/market-generativity/formal/MarketGenerativity.lean#L501) (L501)

文本中有 39 条 `#print axioms` 指令；输出请见原验证记录。 / Contains 39 textual `#print axioms` commands; results belong to the original verification records.

</details>
