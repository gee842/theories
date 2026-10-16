<a id="第二部分的清点--inventory-of-part-ii"></a>
# 第二部分的清点

> **中文版（2026-10-17）。** 正典文本是[英文版](PART-II-INVENTORY.md)；本版由重构时从双语原文拆出，不与英文同步维护，两者有出入时以英文为准。

2026-10-11，Asia/Bangkok。AI（Claude Opus 5.5，会话 Universal Metaethical Core）撰写的清点，回答 Ren 的两条消息（[原话一](../../../../sources/15-codex-theory-conversations/2026-10-11-one-unified-theory-together.md)，[原话二](../../../../sources/15-codex-theory-conversations/2026-10-11-fold-g0.md)）：

本文是清点与提议。它不向核心加入定理，也不登记成果。分类可由[脚本](PART-II-INVENTORY.py)从两张回执所绑定的源重现；用到公理之处已逐一读证明核对。移动章节内容的提议是 AI 的，待 Ren。

<a id="0-问题--the-question"></a>
## 0. 问题

**中文。** G0 折叠之后（P51，[研究 §67](BECOMING-RENEWAL-READING.md#67-折叠-g0p51)），第二部分所加的只有一条公理 `Unrestricted`：从每个立场，任何东西在每一步的延续都有意义。问题是：第二部分的定理中，哪些用到它？用在哪里？不用它的，就属于第一部分。零前提的清点（[ZERO-PREMISE-PLAN §1](ZERO-PREMISE-PLAN.md#1-清点--the-inventory)）排除了第二部分的模块（Significance、Metaethics、Standpoints、Ranking、Renewal、Bridge、Correspondence），并且早于 P42–P44 的落地（Feedback、Boundaries、Relevance）；本清点补上这一部分，并加上公理与评价条件这一维。

<a id="1-方法--method"></a>
## 1. 方法

**中文。** 对象是章节第二部分以名称引用的全部声明，从“第二部分”标题到 §8 之前（§6 与 §7）：197 个名称，去掉模块名、见证的命名空间与变量后是 182 个声明，其中 157 条定理、25 个定义。声明在核心与外围两张回执所绑定的源中查找（核心 `20261011T071749.484228Z`，外围 `20261011T071753.574921Z`，即 `Becoming.Locality` 落地之后；在 R6 之前的回执 `20261011T003217.297180Z` 与 `20261011T003646.599930Z` 之下结果相同）。

核心没有公理，所以一条定理用到公理，只能是以 `Unrestricted sig` 为假设；用到 G0 或其各部分、其他评价条件、结构条件或第一部分的前提，也只能是假设。只在陈述中出现，例如在“当且仅当”之中或在结论中，不算用到。假设取自签名中的约束与陈述最外层蕴涵的前件。各节的 `variable` 只引入数据（流、网、部分、关系），不引入假设，已逐一核对。分类如下：
- **公理**：以 `Unrestricted` 为假设；
- **刻画公理**：公理只出现在陈述中；
- **评价条件**：以 G0、种子加两条中立（`Grounds`）、S0、N、A、预设（`SubTrue`）或不变（`BoundaryInvariant`）为假设；
- **第一部分的前提**：只以平衡、耗散、体现、普查、取用、给予、依存、被围住、有限或可判定为假设；
- **结构条件**：只以连通或被持有为假设；
- **无**：以上都没有。

<a id="2-结论--findings"></a>
## 2. 结论

**中文。**
- **157 条定理中，22 条用到公理，135 条不用。** 不用的 135 条中：85 条什么前提都不用；18 条只用第一部分的前提；12 条以评价条件为假设；2 条以结构条件为假设；18 条刻画公理而不假设它，例如 `unrestricted_iff_g0`、`unrestricted_iff_presupposed`、`bounded_rival`。
- **22 条都只在所指名的点上用到公理**（§3.1）。一个点是：从某个立场，某个形成在某一步的延续有意义。点有三种：
  - (i) 见证中的一个形成在一步：`Clearing.free_rider_loses` 只用到栖居者在第 2 步，`Preemption.not_undermining_yet_loses` 只用到第 1 步的 `false`；
  - (ii) 被比较的路径所接纳、或超出之处的形成；
  - (iii) 活的、已实现的主张，即 G0 的各个推出。
- **每条都是一条对任何意义成立的规律在这些点上的特例。**
  - (ii) 的一般局部形式 P42 已经给出：意义覆盖部分在每步之前已到达者，就对这个部分作公理的比较（`Flow.Balances.comparison_within_reach`）。
  - (iii) 的局部形式就是 G0 本身：以从意义读出的正面相关，G0 恰是公理限于已实现的活的内容（§67 的折叠）。
- **所以第二部分在第一部分之外只加一句断言。** 第二部分的每条定理都是第一部分的一条规律，其条件写在规律之内。公理一经断言，就在所指名的点上满足意义的条件；对一个部分的比较，只需在部分所及之处满足（P42）。A、C、L 与 J1–J4 仍是实践规律的公开条件，不被断言。
- **所需的点由陈述本身给出。** 在 Lean 中，用一个全称假设总是用在某些点上，这一点是平凡的。清点所加的是“哪些点”：被比较的路径、部分的所及、活的主张。所以每条都可以带着局部条件陈述。
- **前提的局部化仍要做。** 18 条只用第一部分前提的定理用的是全局的平衡等；22 条用到公理的都不以第一部分的前提为假设。按零前提清点的分类，这 18 条都可局部化，其中两条只用可判定，属 (b2)。4 条已在那份清点之内（`Flow.fed_from_beyond`、`Flow.excess_bounded`、`Flow.joint_excess_ends`、`Flow.Balances.consumption_ends_with_feeders`）。其余 14 条不在：两条只用可判定；`Flow.region_not_a_cut` 经由 `Flow.fed_from_beyond`；11 条在第二部分的模块里，只在之前各步、在所比较的形成所需的条件上用到平衡（§3.3）。

<a id="3-逐条--theorem-by-theorem"></a>
## 3. 逐条

<a id="31-用到公理的-22-条--the-22-that-use-the-axiom"></a>
### 3.1 用到公理的 22 条

“经由”指证明经另一条用到公理的定理用到它。

| 定理 | § | 用到的点 | 所特化的、对任何意义成立的规律 |
|---|---|---|---|
| `Clearing.free_rider_loses` | II, 6.8 | `(p, 2, dweller)` | 见证的接纳事实（`admitted_without`、`unsupported_with`）与 `Web.Retains.not_added`；以区域为界的形式是 `Clearing.centers_disagree` |
| `Clearing.within_closure_yet_loses` | 6.9 | 经由 | 同上；另两项对以闭包为界的意义成立 |
| `Preemption.not_undermining_yet_loses` | 6.8 | `(p, 1, false)` | 见证的接纳事实与 `Web.Retains.not_added` |
| `Trophic.mediated_unregistered` | 6.10 | `(p, 1, deer)` | 同上 |
| `Transfer.unordered` | 6.8 | 经由 `Web.adds_iff_exceeds`，在两个超出点 | `Web.Adds.exceeds`，`Web.Retains.not_added` |
| `Trophic.responsive_mixed` | 6.10 | 同上 | 同上 |
| `Restoring.Inflow.retains_adds` | 6.8 | 经由 `Web.adds_iff_exceeds`，在超出点 | 保留部分对任何意义成立（`Web.Includes.retains`） |
| `Web.retains_iff_includes` | 6.8 | 被比较路径在 `t` 所接纳的每个 `f`：`(p, t, f)` | `Web.Includes.retains` 与 `Web.Retains` 的定义；对一个部分的比较是 `Flow.Balances.comparison_within_reach` |
| `Web.adds_iff_exceeds` | 6.8 | 超出之处的 `(p, t, f)` | `Web.Adds.exceeds` |
| `Web.retains_agree` | 6.8 | 经由 `Web.retains_iff_includes`，在 `p` 与 `q` | 同 `Web.retains_iff_includes` |
| `Web.Retains.within` | 6.8 | 区域中的 `f`：`(p, t, f)` | `Web.Retains.of_fewer` |
| `Web.retains_bounded_iff_retains` | 6.9 | 经由 | `Web.retains_bounded_iff_includes` |
| `Flow.within_closure_iff_retains` | 6.9 | 经由 | 同上，以供给闭包为区域 |
| `Overshoot.within_closure_iff_retains` | 6.9 | 经由 | 同上 |
| `Ranking.possible_extends_iff` | 6.12 | 被记入的事件：`(p, t, f)` | `Ranking.possible_course_iff`（记入即接纳）与 `Retains`、`Adds` 的定义 |
| `Valuation.premises_of_unrestricted` | 6.8 | 每个活的主张 `c`：`(p, step c, formation c)` | `Significant`、`SelfGood`、`Seed`、`Neutral` 的定义 |
| `Web.significant_of_unrestricted` | 6.8 | 同上，对事件与关系 | 同上 |
| `Conditions.significant_of_unrestricted` | 6.8 | 同上，对整段的事件 | 同上 |
| `Web.paths_g0_comparison` | 6.8 | 同上，在水平路径上；以及增加之处 | 同上；`Web.Retains`、`Web.Adds` 的定义 |
| `g0_of_unrestricted` | 6.12 | 已实现的活的 `c`：`(p, step c, formation c)` | `G0` 的定义：以从意义读出的正面相关，G0 就是公理在这些点上 |
| `relevance_least` | 6.12 | 同上 | 同上 |
| `universal_reason_of_unrestricted` | 6.12 | 经由 | `universal_reason_living`，以 `V.Significant` 为条件 |

<a id="32-刻画公理的-18-条--the-18-that-characterize-the-axiom"></a>
### 3.2 刻画公理的 18 条

**中文。** 它们说公理何时成立，或在一个见证中成立与否；不假设它。它们是关于公理的第一部分规律。

- §6.8：`bounded_rival`
- §6.9：`bounded_whole`
- §6.10：`Clearing.system_whole`、`Flow.bounded_system_whole`、`Clearing.reach_counts_dweller`
- §6.11：`unrestricted_iff_superTrue`、`unrestricted_of_presupposed`（以预设与不变为假设
- §6.12：`unrestricted_iff_g0`、`Web.unrestricted_iff_paths_g0`

<a id="33-只用第一部分前提的-18-条--the-18-that-take-only-part-is-premises"></a>
### 3.3 只用第一部分前提的 18 条

| 定理 | § | 前提 | 局部化 |
|---|---|---|---|
| `Flow.fed_from_beyond` | 6.7 | 平衡、耗散、可判定 | 零前提清点组 B |
| `Flow.region_not_a_cut` | 6.7 | 平衡、耗散、可判定 | **不在清点之内。** 经由 `Flow.fed_from_beyond`（组 B） |
| `Flow.excess_bounded`、`Flow.joint_excess_ends` | 6.7 | 平衡（与给予、依存） | 组 C |
| `Flow.Balances.consumption_ends_with_feeders` | 6.9 | 平衡、给予、依存 | 组 C |
| `Flow.inward_iff_not_fed`、`Valuation.significant_iff_reached` | 6.7 | 只有可判定 | **不在清点之内。** (b2)，属 Ren |
| `Flow.Balances.retains_iff_within_margin`、`loses_iff_beyond_margin`、`adds_iff_within_margin` | 6.8 | 平衡 | **不在清点之内。** 经 `Balances.supported_iff_within_margin`，最终经 `Balances.withheld`：平衡在 `t` 之前各步、在 `f` 所需的条件上 |
| `Flow.Balances.unregistered_beyond_influence`、`comparison_within_reach`、`closed_comparison`、`comparison_within_difference`、`comparison_local`、`adds_iff_exceeds_of_decidable` | 6.10 | 平衡（一条加可判定） | **不在清点之内。** 经 `Balances.agrees_or_reaches_before`，最终经 `Balances.withheld`：平衡在 `t` 之前各步、在所比较的形成所需的条件上；`comparison_within_difference` 经 `Balances.differs_before`，用两个流在之前各步、在该条件上的平衡 |
| `Flow.Balances.presupposed_comparison`、`presupposed_reach_comparison` | 6.11 | 平衡 | **不在清点之内。** 经 `comparison_within_reach` |

<a id="34-以评价条件或结构条件为假设的-14-条--the-14-with-an-evaluative-or-structural-condition"></a>
### 3.4 以评价条件或结构条件为假设的 14 条

**中文。** 它们对满足条件的每个评价成立，与 G0 折叠之后一样是第一部分的条件规律。

| 定理 | § | 条件 |
|---|---|---|
| `Valuation.significant_iff` | 6.1 | 连通 |
| `Conditions.valuing_consumption_reaches`、`Web.valuing_breaking_reaches`、`Flow.valuing_reaches_source` | 6.3, 6.7 | N_rel |
| `universal_reason` | 6.3 | 种子加两条中立、A、连通 |
| `positioned_articulation_of_articulates` | 6.4 | A |
| `Valuation.significant_iff_held` | 6.7 | 被持有 |
| `Valuation.own_transmission` | 6.7 | S0 |
| `Valuation.significant_of_transmits` | 6.7 | S0、N_rel、连通 |
| `subTrue_of_larger`、`boundaryInvariant_iff_all` | 6.11 | 预设 |
| `not_subTrue_of_invariant` | 6.11 | 不变 |
| `retains_agree_of_presupposed`、`Valuation.significant_of_presupposed` | 6.11 | 预设与不变 |

<a id="35-什么前提都不用的-85-条--the-85-that-take-no-premise"></a>
### 3.5 什么前提都不用的 85 条

- II：`Clearing.loses_beyond`
- §6.1：`Mutualism.significant_iff`
- §6.3：`Conditions.significant_iff_of_common`、`Web.significant_iff_of_common`、`Separate.not_connected`、`Web.inert_connects`、`Web.connected_of_renewable`、`Shared.connection_by_living_use`、`Web.one_use_connects`、`Renewable.class_belongs_to_the_run`、`Renewable.readings_differ`、`Web.living_iff_relations`、`Renewable.finite_reading_credits_consumption`、`Renewable.amount_reading`、`Dependence.Overdetermined.no_difference`、`Renewable.no_finite_segment_makes_difference`
- §6.5：`articulation_iff_lifted`、`Ranking.restraint_ranks`、`Ranking.malignant_restraint`
- §6.7：`Lone.fed_not_recurring`、`Pair.own_not_joint`、`Exceeding.all_end`、`Alone.all_continue`、`Downstream.one_way`、`Mortal.after_its_end`、`Clearing.undermines_within_renewal`、`Apart.not_enough`、`Web.significant_iff_self`、`Clearing.clearer_not_living`、`Clearing.center_not_derived`、`Flow.conveyance_idle`、`Clearing.resource_not_cut_living_on`、`Clearing.conveyance_only`
- §6.8：`Web.Retains.not_added`、`Web.Retains.of_fewer`、`Web.retains_bounded_iff`、`Web.AdmitsWithin.narrow`、`Clearing.centers_disagree`、`Web.significance_undetermined`
- §6.9：`Flow.beyond_gives_nothing`、`Clearing.dependenceRegion_iff`、`Overshoot.ends_through_feeder`、`Clearing.closure_supported`、`Web.retains_bounded_iff_includes`、`Clearing.levels`、`Clearing.reach_middle`、`Trophic.mediates`
- §6.10：`Flow.system_whole_of_common`、`Clearing.unregistered`、`Clearing.reaches_dweller`、`Clearing.system_counts_dweller`、`Trophic.difference_reaches_forest`、`Clearing.no_levels_without_source`、`Margin.reach_without_misjudgment`、`Flow.reach_whole_of_common`
- §6.11：`Boundary.closure`、`Boundary.whole`、`Boundary.only_whole`、`superTrue_iff`、`boundaryInvariant_iff_determinate`、`superTrue_member_iff`、`subTrue_member`、`subTrue_significantWithin_iff`、`superTrue_significantWithin_iff_union`、`superTrue_level_free`、`subTrue_empty_iff`、`subTrue_total_iff`、`bounded_closure_iff`、`bounded_closure_least`、`presupposition_scopes`、`boundaryInvariant_iff_conditional`、`boundaryInvariant_iff_standpointInvariant`、`OneCounts.forms_apart`、`Clearing.without_standpoint_invariance`、`Flow.presupposition_order`、`Clearing.levels_differ`、`Clearing.own_presupposition`
- §6.12：`articulates_total`、`Widening.bare_forces_reason`、`Ranking.malignant_possible`、`Ranking.possible_tie`、`Ranking.readings_rank_presence`、`Ranking.possibleFirst_order`、`Ranking.possibleFirst_presence`、`Ranking.Rest.rest_ranked_below`

**中文。** 见证中的定理（如 `Clearing.*`、`Trophic.*`）证明其见证满足平衡等，这些前提出现在结论中，不是假设。

<a id="4-提议待-ren-proposal-for-ren"></a>
## 4. 提议（待 Ren）

**中文。**
1. **章节。** 把第二部分中不用公理的内容移入第一部分。在第一部分 §5（评价的形成）之后加一节“意义的规律”，对任何意义陈述：
   - 保留与增加，不损的界（余量）；
   - 整体优先与区域，路线 (b)（供给闭包），反馈与所及；
   - 公理的分解（预设与不变）；
   - 对 G0 与公理的刻画（`significant_iff`、`significant_iff_held`、`unrestricted_iff_g0`、`unrestricted_iff_presupposed`）；
   - 中心与立场，对应纪律与连通；
   - 理由（以 A 为条件），比较（以所比较的读法为条件）。

   第二部分只留三样：公理的断言；它在所指名的点上满足意义的条件，于是 §3.1 的 22 条不再需要这一条件（其他条件照旧，例如 `universal_reason_of_unrestricted` 仍以 A 为条件）；它的根据问题（§8）。
2. **前提的局部化。** §3.3 中不在零前提清点之内、用到平衡的 12 条（`Flow.region_not_a_cut` 与第二部分模块中的 11 条），在其局部形式落地之后作为推论在原处重证。11 条经由 `Balances.withheld`：组 C 的补丁给出它的局部形式 `withheld_at` 与 `supported_iff_within_margin_at`（零前提清点正是经 `Balances.withheld` 把 `supported_iff_within_margin` 归入组 C）；`comparison_within_difference` 另经 `Balances.differs_before`。`Becoming.Locality` 已落地（12c7cb44）。顺序由整合者决定。
3. **Lean（可选）。** 22 条的局部形式大多已在 Lean 中，是对任何意义的规律：余量规律、`comparison_within_reach`、`Retains.of_fewer`、`retains_bounded_iff_includes`。若章节需要，可把见证中 (i) 类的几条写成带局部意义条件的形式，公理的形式作为推论。这需要认领与一次核心检查，排在第一部分各项之后。

<a id="5-不主张什么--what-is-not-claimed"></a>
## 5. 不主张什么

**中文。**
- 没有新的定理。分类读自签名，用到公理的点读自证明；公理报告不变。
- 不主张公理可以推出：动力学不决定意义（`Web.significance_undetermined`）。移入第一部分的是不用公理的规律，不是公理本身。
- 不主张移动已被采纳：章节的结构属 Ren，第一部分的顺序与接口属整合者。
- §7 以记录名引用的外围结果（纠正序列等）不在本清点之内。
- 读法不变，仍待 Ren：正面相关从意义读出，C 的可能性读法。

<a id="6-协调--coordination"></a>
## 6. 协调
