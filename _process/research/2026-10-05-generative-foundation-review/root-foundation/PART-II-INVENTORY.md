# 第二部分的清点 / Inventory of Part II

2026-10-11，Asia/Bangkok。AI（Claude Opus 5.5，会话 Universal Metaethical Core）撰写的清点，回答 Ren 的两条消息（[原话一](../../../../sources/15-codex-theory-conversations/2026-10-11-one-unified-theory-together.md)，[原话二](../../../../sources/15-codex-theory-conversations/2026-10-11-fold-g0.md)）：

> part i first, then consider second(maybe a lot in second will move to part i)

> if we don't need G0 as axiom, fold it, at least for part i, and commit

本文是清点与提议。它不向核心加入定理，也不登记成果。分类可由[脚本](PART-II-INVENTORY.py)从两张回执所绑定的源重现；用到公理之处已逐一读证明核对。移动章节内容的提议是 AI 的，待 Ren。

2026-10-11, Asia/Bangkok. An inventory written by the AI (Claude Opus 5.5, session Universal Metaethical Core) in answer to Ren's two messages quoted above. It is an inventory and a proposal: nothing enters the core and no result is registered. The classification is reproduced by a [script](PART-II-INVENTORY.py) from the sources the two receipts bind, and each use of the axiom was checked by reading the proof. The proposal to move material is the AI's, pending Ren.

## 0. 问题 / The question

**中文。** G0 折叠之后（P51，[研究 §67](BECOMING-RENEWAL-READING.md#67-折叠-g0p51)），第二部分所加的只有一条公理 `Unrestricted`：从每个立场，任何东西在每一步的延续都有意义。问题是：第二部分的定理中，哪些用到它？用在哪里？不用它的，就属于第一部分。零前提的清点（[ZERO-PREMISE-PLAN §1](ZERO-PREMISE-PLAN.md#1-清点--the-inventory)）排除了第二部分的模块（Significance、Metaethics、Standpoints、Ranking、Renewal、Bridge、Correspondence），并且早于 P42–P44 的落地（Feedback、Boundaries、Relevance）；本清点补上这一部分，并加上公理与评价条件这一维。

**English.** After the fold of G0 (P51, study section 67), what Part II adds is one axiom, `Unrestricted`: from every standpoint, the continuation of anything has significance at every step. The question is which of Part II's theorems use it, and where; those that do not belong to Part I. The zero-premise inventory (ZERO-PREMISE-PLAN section 1) excluded Part II's modules (Significance, Metaethics, Standpoints, Ranking, Renewal, Bridge, Correspondence), and it predates the landing of P42–P44 (Feedback, Boundaries, Relevance). This inventory covers them and adds the dimension of the axiom and the evaluative conditions.

## 1. 方法 / Method

**中文。** 对象是章节第二部分以名称引用的全部声明，从“第二部分”标题到 §8 之前（§6 与 §7）：197 个名称，去掉模块名、见证的命名空间与变量后是 182 个声明，其中 157 条定理、25 个定义。声明在核心与外围两张回执所绑定的源中查找（核心 `20261011T071749.484228Z`，外围 `20261011T071753.574921Z`，即 `Becoming.Locality` 落地之后；在 R6 之前的回执 `20261011T003217.297180Z` 与 `20261011T003646.599930Z` 之下结果相同）。

核心没有公理，所以一条定理用到公理，只能是以 `Unrestricted sig` 为假设；用到 G0 或其各部分、其他评价条件、结构条件或第一部分的前提，也只能是假设。只在陈述中出现，例如在“当且仅当”之中或在结论中，不算用到。假设取自签名中的约束与陈述最外层蕴涵的前件。各节的 `variable` 只引入数据（流、网、部分、关系），不引入假设，已逐一核对。分类如下：
- **公理**：以 `Unrestricted` 为假设；
- **刻画公理**：公理只出现在陈述中；
- **评价条件**：以 G0、种子加两条中立（`Grounds`）、S0、N、A、预设（`SubTrue`）或不变（`BoundaryInvariant`）为假设；
- **第一部分的前提**：只以平衡、耗散、体现、普查、取用、给予、依存、被围住、有限或可判定为假设；
- **结构条件**：只以连通或被持有为假设；
- **无**：以上都没有。

**English.** The scope is every declaration that Part II of the chapter names, from its heading to that of section 8 (sections 6 and 7): 197 names, which after removing module names, witness namespaces and variables are 182 declarations, 157 theorems and 25 definitions. Declarations are looked up in the sources bound by the core and periphery receipts (core `20261011T071749.484228Z`, periphery `20261011T071753.574921Z`, after `Becoming.Locality` landed; the result is the same under the receipts before R6, `20261011T003217.297180Z` and `20261011T003646.599930Z`).

The core has no axioms, so a theorem can use the axiom only by taking `Unrestricted sig` as a hypothesis. The same holds for G0 or its parts, the other evaluative conditions, the structural conditions and Part I's premises. A mention only in the statement, inside an iff or in the conclusion, is not a use. Hypotheses are read from the signature's binders and the antecedents of the statement's outermost implications. Section `variable`s introduce only data (flows, webs, parts, relations), never hypotheses; each was checked. The classes:
- **axiom**: takes `Unrestricted` as a hypothesis;
- **characterizes the axiom**: the axiom occurs only in the statement;
- **evaluative condition**: takes G0, the seed with both neutralities (`Grounds`), S0, N, A, the presupposition (`SubTrue`) or invariance (`BoundaryInvariant`) as a hypothesis;
- **Part I's premises**: takes only balance, dissipation, embodiment, census, taking, acting, dependence, enclosure, finiteness or decidability;
- **structural condition**: takes only connection or holding;
- **none**: takes none of these.

## 2. 结论 / Findings

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

**English.**
- **Of 157 theorems, 22 use the axiom and 135 do not.** Of the 135, 85 take no premise at all, 18 take only Part I's premises, 12 take an evaluative condition, 2 take a structural condition, and 18 characterize the axiom without assuming it, for example `unrestricted_iff_g0`, `unrestricted_iff_presupposed`, `bounded_rival`.
- **Each of the 22 uses the axiom only at named points** (section 3.1). A point is the significance, from a standpoint, of a formation's continuation at a step. The points are of three kinds:
  - (i) one formation at one step of a witness: `Clearing.free_rider_loses` uses only the dweller at step 2, and `Preemption.not_undermining_yet_loses` only `false` at step 1;
  - (ii) the formations a compared path admits, or where it exceeds;
  - (iii) living realized claims, in the derivations of G0.
- **Each is a law holding for any significance, specialized at those points.**
  - For (ii) the general local form is already P42's: any significance covering what a part has reached before each step compares that part as the axiom does (`Flow.Balances.comparison_within_reach`).
  - For (iii) the local form is G0 itself: with positive relevance read from significance, G0 is exactly the axiom restricted to realized living content (the fold, section 67).
- **So Part II adds one assertion to Part I.** Each theorem of Part II is a Part I law with its conditions written inside it. The axiom, once asserted, meets the significance condition at the points named; for the comparison of a part it need only meet it where the part reaches (P42). A, C, L and J1–J4 stay disclosed conditions of the practical laws and are not asserted.
- **The statements themselves name the points needed.** That a universal hypothesis in Lean is always used at some points is trivial. What the inventory adds is which points: the compared paths, the part's reach, the living claims. So each theorem can be stated with a local condition.
- **Localizing the premises remains.** The 18 theorems that take only Part I's premises use global balance and the like; none of the 22 that use the axiom takes a Part I premise. By the zero-premise inventory's classes all 18 are localizable, two of them needing only decidability, class (b2). Four are already in that inventory (`Flow.fed_from_beyond`, `Flow.excess_bounded`, `Flow.joint_excess_ends`, `Flow.Balances.consumption_ends_with_feeders`). The other 14 are not: two need only decidability; `Flow.region_not_a_cut` goes through `Flow.fed_from_beyond`; and 11 lie in Part II's modules and use balance only at earlier steps, on the conditions the compared formations require (section 3.3).

## 3. 逐条 / Theorem by theorem

### 3.1 用到公理的 22 条 / The 22 that use the axiom

“经由”指证明经另一条用到公理的定理用到它。/ “Via” means the proof uses the axiom through another of the 22.

| 定理 / Theorem | § | 用到的点 / Points used | 所特化的、对任何意义成立的规律 / The law for any significance it specializes |
|---|---|---|---|
| `Clearing.free_rider_loses` | II, 6.8 | `(p, 2, dweller)` | 见证的接纳事实（`admitted_without`、`unsupported_with`）与 `Web.Retains.not_added`；以区域为界的形式是 `Clearing.centers_disagree` / the witness's admission facts with `Web.Retains.not_added`; the bounded form is `Clearing.centers_disagree` |
| `Clearing.within_closure_yet_loses` | 6.9 | 经由 / via `free_rider_loses` | 同上；另两项对以闭包为界的意义成立 / as above; its other two parts hold for significance bounded by the closures |
| `Preemption.not_undermining_yet_loses` | 6.8 | `(p, 1, false)` | 见证的接纳事实与 `Web.Retains.not_added` / the witness's admission facts with `Web.Retains.not_added` |
| `Trophic.mediated_unregistered` | 6.10 | `(p, 1, deer)` | 同上 / as above |
| `Transfer.unordered` | 6.8 | 经由 `Web.adds_iff_exceeds`，在两个超出点 / via `Web.adds_iff_exceeds`, at the two exceeding points | `Web.Adds.exceeds`，`Web.Retains.not_added` |
| `Trophic.responsive_mixed` | 6.10 | 同上 / as above | 同上 / as above |
| `Restoring.Inflow.retains_adds` | 6.8 | 经由 `Web.adds_iff_exceeds`，在超出点 / via `Web.adds_iff_exceeds`, at the exceeding point | 保留部分对任何意义成立（`Web.Includes.retains`）/ its retaining part holds for any significance (`Web.Includes.retains`) |
| `Web.retains_iff_includes` | 6.8 | 被比较路径在 `t` 所接纳的每个 `f`：`(p, t, f)` / `(p, t, f)` for each `f` the compared path admits at `t` | `Web.Includes.retains` 与 `Web.Retains` 的定义；对一个部分的比较是 `Flow.Balances.comparison_within_reach` / `Web.Includes.retains` with the definition of `Web.Retains`; for a part's comparison, `Flow.Balances.comparison_within_reach` |
| `Web.adds_iff_exceeds` | 6.8 | 超出之处的 `(p, t, f)` / the exceeding `(p, t, f)` | `Web.Adds.exceeds` |
| `Web.retains_agree` | 6.8 | 经由 `Web.retains_iff_includes`，在 `p` 与 `q` / via `Web.retains_iff_includes`, at `p` and `q` | 同 `Web.retains_iff_includes` / as `Web.retains_iff_includes` |
| `Web.Retains.within` | 6.8 | 区域中的 `f`：`(p, t, f)` / `(p, t, f)` for `f` in the region | `Web.Retains.of_fewer` |
| `Web.retains_bounded_iff_retains` | 6.9 | 经由 / via `Web.retains_iff_includes` | `Web.retains_bounded_iff_includes` |
| `Flow.within_closure_iff_retains` | 6.9 | 经由 / via `Web.retains_bounded_iff_retains` | 同上，以供给闭包为区域 / as above, with the feeding closure as the region |
| `Overshoot.within_closure_iff_retains` | 6.9 | 经由 / via `Flow.within_closure_iff_retains` | 同上 / as above |
| `Ranking.possible_extends_iff` | 6.12 | 被记入的事件：`(p, t, f)` / `(p, t, f)` at the credited events | `Ranking.possible_course_iff`（记入即接纳）与 `Retains`、`Adds` 的定义 / `Ranking.possible_course_iff` (credit is admission) with the definitions of `Retains` and `Adds` |
| `Valuation.premises_of_unrestricted` | 6.8 | 每个活的主张 `c`：`(p, step c, formation c)` / `(p, step c, formation c)` for each living claim `c` | `Significant`、`SelfGood`、`Seed`、`Neutral` 的定义 / the definitions of `Significant`, `SelfGood`, `Seed`, `Neutral` |
| `Web.significant_of_unrestricted` | 6.8 | 同上，对事件与关系 / as above, for events and relations | 同上 / as above |
| `Conditions.significant_of_unrestricted` | 6.8 | 同上，对整段的事件 / as above, for whole-run events | 同上 / as above |
| `Web.paths_g0_comparison` | 6.8 | 同上，在水平路径上；以及增加之处 / as above, on level paths, and the added point | 同上；`Web.Retains`、`Web.Adds` 的定义 / as above; the definitions of `Web.Retains`, `Web.Adds` |
| `g0_of_unrestricted` | 6.12 | 已实现的活的 `c`：`(p, step c, formation c)` / `(p, step c, formation c)` for realized living `c` | `G0` 的定义：以从意义读出的正面相关，G0 就是公理在这些点上 / the definition of `G0`: with positive relevance read from significance, G0 is the axiom at these points |
| `relevance_least` | 6.12 | 同上 / as above | 同上 / as above |
| `universal_reason_of_unrestricted` | 6.12 | 经由 / via `Valuation.premises_of_unrestricted` | `universal_reason_living`，以 `V.Significant` 为条件 / `universal_reason_living`, with `V.Significant` as a condition |

### 3.2 刻画公理的 18 条 / The 18 that characterize the axiom

**中文。** 它们说公理何时成立，或在一个见证中成立与否；不假设它。它们是关于公理的第一部分规律。

**English.** They say when the axiom holds, or whether it holds in a witness, without assuming it. They are Part I laws about the axiom.

- §6.8：`bounded_rival`
- §6.9：`bounded_whole`
- §6.10：`Clearing.system_whole`、`Flow.bounded_system_whole`、`Clearing.reach_counts_dweller`
- §6.11：`unrestricted_iff_superTrue`、`unrestricted_of_presupposed`（以预设与不变为假设 / takes the presupposition and invariance）、`unrestricted_iff_presupposed`、`unrestricted_iff_presupposed_along`、`Clearing.without_presupposition`、`Clearing.without_invariance`、`Clearing.with_fixed_boundary`、`unrestricted_iff_presupposed_of_whole`、`Flow.unrestricted_iff_system_presupposed`、`Flow.unrestricted_iff_presupposed_of_common`、`Clearing.system_presupposition`
- §6.12：`unrestricted_iff_g0`、`Web.unrestricted_iff_paths_g0`

### 3.3 只用第一部分前提的 18 条 / The 18 that take only Part I's premises

| 定理 / Theorem | § | 前提 / Premises | 局部化 / Localization |
|---|---|---|---|
| `Flow.fed_from_beyond` | 6.7 | 平衡、耗散、可判定 / balance, dissipation, decidability | 零前提清点组 B / zero-premise inventory group B |
| `Flow.region_not_a_cut` | 6.7 | 平衡、耗散、可判定 / balance, dissipation, decidability | **不在清点之内。** 经由 `Flow.fed_from_beyond`（组 B）/ **Not in the inventory.** Through `Flow.fed_from_beyond` (group B) |
| `Flow.excess_bounded`、`Flow.joint_excess_ends` | 6.7 | 平衡（与给予、依存）/ balance (with acting, dependence) | 组 C / group C |
| `Flow.Balances.consumption_ends_with_feeders` | 6.9 | 平衡、给予、依存 / balance, acting, dependence | 组 C / group C |
| `Flow.inward_iff_not_fed`、`Valuation.significant_iff_reached` | 6.7 | 只有可判定 / decidability only | **不在清点之内。** (b2)，属 Ren / **Not in the inventory.** (b2), Ren's |
| `Flow.Balances.retains_iff_within_margin`、`loses_iff_beyond_margin`、`adds_iff_within_margin` | 6.8 | 平衡 / balance | **不在清点之内。** 经 `Balances.supported_iff_within_margin`，最终经 `Balances.withheld`：平衡在 `t` 之前各步、在 `f` 所需的条件上 / **Not in the inventory.** Through `Balances.supported_iff_within_margin` and in the end `Balances.withheld`: balance at the steps before `t`, on the conditions `f` requires |
| `Flow.Balances.unregistered_beyond_influence`、`comparison_within_reach`、`closed_comparison`、`comparison_within_difference`、`comparison_local`、`adds_iff_exceeds_of_decidable` | 6.10 | 平衡（一条加可判定）/ balance (one with decidability) | **不在清点之内。** 经 `Balances.agrees_or_reaches_before`，最终经 `Balances.withheld`：平衡在 `t` 之前各步、在所比较的形成所需的条件上；`comparison_within_difference` 经 `Balances.differs_before`，用两个流在之前各步、在该条件上的平衡 / **Not in the inventory.** Through `Balances.agrees_or_reaches_before` and in the end `Balances.withheld`: balance at the steps before `t`, on the conditions the compared formations require; `comparison_within_difference` goes through `Balances.differs_before`, using both flows' balance at earlier steps on that condition |
| `Flow.Balances.presupposed_comparison`、`presupposed_reach_comparison` | 6.11 | 平衡 / balance | **不在清点之内。** 经 `comparison_within_reach` / **Not in the inventory.** Through `comparison_within_reach` |

### 3.4 以评价条件或结构条件为假设的 14 条 / The 14 with an evaluative or structural condition

**中文。** 它们对满足条件的每个评价成立，与 G0 折叠之后一样是第一部分的条件规律。

**English.** They hold for every valuation meeting the condition; like G0 after the fold, they are Part I's conditional laws.

| 定理 / Theorem | § | 条件 / Condition |
|---|---|---|
| `Valuation.significant_iff` | 6.1 | 连通 / connected |
| `Conditions.valuing_consumption_reaches`、`Web.valuing_breaking_reaches`、`Flow.valuing_reaches_source` | 6.3, 6.7 | N_rel |
| `universal_reason` | 6.3 | 种子加两条中立、A、连通 / the seed with both neutralities, A, connected |
| `positioned_articulation_of_articulates` | 6.4 | A |
| `Valuation.significant_iff_held` | 6.7 | 被持有 / held |
| `Valuation.own_transmission` | 6.7 | S0 |
| `Valuation.significant_of_transmits` | 6.7 | S0、N_rel、连通 / S0, N_rel, connected |
| `subTrue_of_larger`、`boundaryInvariant_iff_all` | 6.11 | 预设 / the presupposition |
| `not_subTrue_of_invariant` | 6.11 | 不变 / invariance |
| `retains_agree_of_presupposed`、`Valuation.significant_of_presupposed` | 6.11 | 预设与不变 / the presupposition and invariance |

### 3.5 什么前提都不用的 85 条 / The 85 that take no premise

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

**English.** Theorems about witnesses (such as `Clearing.*`, `Trophic.*`) prove that their witness satisfies balance and the like; these premises occur in the conclusion, not as hypotheses.

## 4. 提议（待 Ren）/ Proposal (for Ren)

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

**English.**
1. **The chapter.** Move what in Part II does not use the axiom into Part I. After Part I's section 5 (how evaluation forms), add a section “Laws of significance”, stated for any significance:
   - retaining and adding, and the boundary of not harm (the margin);
   - the whole first and regions, route (b) (the feeding closure), feedback and reach;
   - the decomposition of the axiom (presupposition and invariance);
   - the characterizations of G0 and of the axiom (`significant_iff`, `significant_iff_held`, `unrestricted_iff_g0`, `unrestricted_iff_presupposed`);
   - centers and standpoints, the correspondence discipline and connection;
   - reasons (with A as a condition) and comparison (with the reading compared as a condition).

   Part II keeps three things: the assertion of the axiom; that it meets the significance condition at the points named, so that the 22 of section 3.1 no longer need that condition (their other conditions stay, as A stays for `universal_reason_of_unrestricted`); and the question of its warrant (section 8).
2. **Localizing the premises.** The 12 rows of section 3.3 outside the zero-premise inventory that use balance (`Flow.region_not_a_cut` and the 11 in Part II's modules) are re-proved in place as corollaries once their local forms land. The 11 go through `Balances.withheld`, whose local forms `withheld_at` and `supported_iff_within_margin_at` group C's patch provides (the zero-premise inventory places `supported_iff_within_margin` in group C through `Balances.withheld`); `comparison_within_difference` also goes through `Balances.differs_before`. `Becoming.Locality` has landed (12c7cb44). The integrator orders them.
3. **Lean (optional).** Most local forms of the 22 are already in Lean as laws for any significance: the margin laws, `comparison_within_reach`, `Retains.of_fewer`, `retains_bounded_iff_includes`. Where the chapter needs it, the witnesses of kind (i) can be stated with their local significance condition, with the axiom's forms as corollaries. This needs a claim and a core checker run, queued after Part I's items.

## 5. 不主张什么 / What is not claimed

**中文。**
- 没有新的定理。分类读自签名，用到公理的点读自证明；公理报告不变。
- 不主张公理可以推出：动力学不决定意义（`Web.significance_undetermined`）。移入第一部分的是不用公理的规律，不是公理本身。
- 不主张移动已被采纳：章节的结构属 Ren，第一部分的顺序与接口属整合者。
- §7 以记录名引用的外围结果（纠正序列等）不在本清点之内。
- 读法不变，仍待 Ren：正面相关从意义读出，C 的可能性读法。

**English.**
- No new theorem. The classes are read from signatures and the points from proofs; the axiom reports are unchanged.
- The axiom is not claimed derivable: the dynamics does not decide significance (`Web.significance_undetermined`). What moves into Part I are the laws that do not use the axiom, not the axiom.
- The move is not claimed adopted: the chapter's structure is Ren's, and Part I's order and interfaces are the integrator's.
- The periphery results that section 7 cites by record name (the correction sequences and the like) are outside this inventory.
- The readings are unchanged and still Ren's: positive relevance read from significance, and the possibility reading of C.

## 6. 协调 / Coordination

- **整合者 / The integrator.** 本清点是对第一部分结构的输入；§4 的第 1、2 项交整合者排序。 / This inventory is input to Part I's structure; items 1 and 2 of section 4 go to the integrator to order.
- **零前提清点 / The zero-premise inventory.** 本清点补上其所排除的第二部分模块；§3.3 中标“不在清点之内”的 14 条可并入其 §1.3。 / This inventory covers the Part II modules it excluded; the 14 rows of section 3.3 marked as outside it can join its section 1.3.
