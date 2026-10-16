<a id="零前提的规律--laws-with-zero-premises"></a>
# 零前提的规律

> **中文版（2026-10-17）。** 正典文本是[英文版](ZERO-PREMISE-PLAN.md)；本版由重构时从双语原文拆出，不与英文同步维护，两者有出入时以英文为准。

2026-10-11，Asia/Bangkok。AI（Claude Opus 5.5）应 Ren 的转向指示撰写的计划与清点（[原话](../../../../sources/15-codex-theory-conversations/2026-10-11-zero-premise-laws.md)）：

本文是计划与清点。它不向核心加入定理，也不登记成果。下面的分类与“Y 当且仅当 Z”形式是 AI 的提议，待 Ren 审阅；其中 (b) 类需要 Ren 决定。

<a id="0-方向--the-direction"></a>
## 0. 方向

**中文。** 到 P45 为止，前进的方式是选择表：对八个前提的 256 个选择，各给出恰在何处成立的规律。现在反过来：取每条规律，去掉前提，使它对每个世界成立，而把证明实际用到的条件写进规律本身，作为关于该世界在那些步、那些关系项上的条件 Z。规律取确切的形式“Y 当且仅当 Z”；选择定理应作为推论得出：一个前提对每一步都成立，就使 Z 在每一步成立。表示之内各前提已证明是偶然的、彼此独立的（`World.contingent`、`World.independent`），所以从不声称某个前提作为规律被推出；推出的只是带着局部条件的规律。每一步都写明所作的是哪一种：局部化；重新奠定表示（需 Ren 决定）；或推广表示。

<a id="1-清点--the-inventory"></a>
## 1. 清点

<a id="11-方法--method"></a>
### 1.1 方法

**中文。** 对象是第一部分的主要定理：其记录的 canonical source 是 Becoming 核心模块、不属第二部分（Significance、Metaethics、Standpoints、Ranking、Renewal、Bridge、Correspondence）的 39 条成果记录所列的定理。脚本从这些记录所列声明的签名中找出用到八个前提、有限、被围住或可判定的，共 355 处，其中 339 处在定理上（[脚本](ZERO-PREMISE-INVENTORY.py)）；见证世界（例如 `Shuttle.shuttle`、`Brood.brood`）不是规律，不计。然后逐一读证明，看前提在哪一步、对哪些关系项或家族被用到。分类：
- (a) 可局部化：证明只在某些步、对某些关系项或家族用到它；
- (b) 属于表示，需 Ren 决定；
- (c) 确实需要全局成立。

记号

<a id="12-结论--findings"></a>
### 1.2 结论

**中文。**
- **八个前提的每一处使用都属 (a)。** 每个证明都只在特定的步、对特定的关系项或家族用到前提：平衡在 `(t, c)` 上，`c` 是水平改变者或被围住家族的成员；只有活跃者给予或取用，在给予或取用 `x` 的那个 `f` 上；耗散，在那一步被围住的那个家族 `es_t` 上；体现，在开始或不再活跃的那个 `x` 上，于 `t` 与 `t+1`；活动需要支持，在那一步活跃的那个 `g` 上；普查，在所计数的那些步上；有界传递，在世系所涉的条件 `c` 上。没有哪处证明用到前提对一切步、一切关系项的普遍形式。
- **有限与被围住也属 (a)。** 有限只经由它的局部推论被使用：每步有一个封闭的家族（全部关系项），每步有普查，计数有界。被围住本身就是关于一步的条件。静止定理要求被围住的步从 `T` 起不断，这是对尾段 `[T, ∞)` 的每一步的条件，仍是局部的：只有那些步上被用到。
- **(b) 类是表示的承诺，共五项。**
  1. 以整单位计的量：静止依靠总水平是自然数、不能无穷次下降（`falls_not_recurring`）；耗散中的 `sign` 项（每次取用至少失去一个单位）就是最小差异。Ren 已为最小差异选 A（属于生成本身，[来源](../../../../sources/15-codex-theory-conversations/2026-10-11-difference-in-becoming.md)），R4 把单位的细分算作给予。最小损失能否推出由熵的会话研究，这里不重复。
  2. 被计数处的可判定性（`mark`、计数表）。
  3. 离散的步与共同的时间索引。
  4. 流中每个参与者列出一次，家族不重复（`Distinct`）。
  5. 逐点（`Pointwise`，代替函数外延性）。
- **(c) 类：八个前提中没有。** 唯一被证明不能局部化的需要是逻辑的，不是关于世界的前提：要对每个有限世界给出此后不再生起的一步，就推出有限全知原则（`World.lpo_of_finite_ends`、`Listed.lpo_of_few`、`Web.lpo_of_ending`）；不加可判定性而要求有限世界中生起复现恰当止息复现，就等于排中律（`World.law_iff_em`）。这些是 (b) 中第 2 项的边界：去掉可判定性时，“明确的终止之步”的陈述形式不能保留，“不复现”的形式可以保留。

<a id="13-逐条--theorem-by-theorem"></a>
### 1.3 逐条

列中“位置”写证明在哪一步、对哪些关系项或家族用到它。“类”写 a、b 或 c。

| 定理 | 前提 | 位置 | 类 |
|---|---|---|---|
| **A. 计数 | | | |
| `Web.arising_of_ceasing`, `World.arising_of_ceasing` (ceasing-needs-arising) | census | listing at the steps of `[N, N+n]` for each `N`; only `\|alive N\|` and the census balance on the stretch are used | a — a finite list holding the active at one step `N` after which nothing arises suffices (with nothing arising, later activity is within it) |
| 同上 | decidability | `mark (Ceases t a)`, `mark (Arises t a)` on the listed relata | b (2) |
| `Web.unceasing_iff_bounded`, `CountedBy.arising_iff_ceasing` (bounded-census-keeps-pace) | census; bound `B`/`K` | listing on the stretch; `\|alive t\| ≤ K` at arbitrarily late `t` | a — already an exact iff without a bound: `Listed.ceasing_iff_shortfall`, `Listed.coming_iff_excess` |
| `Listed.tally`, `counting_laws`, `tally_iff_counted` (whole-law-of-counting) | decidability | the marks counted | b (2); no premise on worlds |
| `counting_binds_jointly`, `Web.Embodied.arises_given` (whole-law-of-counting, life-as-condition-of-life) | balance | `Bal(t, x)` for the `x` arising across `t` | a |
| 同上 | acting | `Act(t, f, x)` for the `f` present giving to `x` | a |
| 同上 | embodiment | `Emb(x, t)`, `Emb(x, t+1)` | a |
| 同上 | census | only to turn “`f` active at `t`” into a positive count at `t` | a |
| `World.taking_binds_counting` | taking | `Take(t, f, c)` for each `f` present at `t` (nothing active, so nothing taken) | a |
| 同上 | balance | `Bal(t, c)` for `x` and for the members of the family active after `t` | a |
| 同上 | dissipation | `Diss(alive (t+1), t)`: the family active after the step | a |
| 同上 | embodiment, census | `Emb(c, t)`, `Emb(c, t+1)` on that family; listing at `t`, `t+1` | a |
| `World.enclosed_binds_counting` | balance, dissipation | `Bal(t, x)`; `Diss(cs, t)` for the `cs` closed at `t` | a |
| 同上 | embodiment | `Emb(c, t)` for `c ∈ cs`; `Emb(x, t)`, `Emb(x, t+1)` | a |
| `counting_under`, `counting_binds_iff`, `enclosed_counting_under`, `finite_counting_under`, `binding_*` (selection tables) | all | through the laws above and B3 | a, b (2) — become corollaries |
| **B. 静止与开放 | | | |
| `Flow.standing_runs_down`, `standing_never_rises`, `change_lowers`, `exchange_lowers`, `fall_lowers_on`, `rise_lowers_on` (continued-change-needs-openness, rising-and-falling-in-one-exchange) | balance | `Bal(t, c)`, `c ∈ es_t` (`Balances.over` sums them) | a |
| 同上 | dissipation | `Diss(es_t, t)` | a; its `sign` term is b (1) |
| 同上 | standing census | `stand t`, `stand (t+1)` only to equate the total standing with `stock es_t` | a — removable: `es_t` already holds what stands |
| `Flow.change_stops_unrefuted_around`, `exchange_not_recurring_around`, `World.arising_stops_unrefuted`, `comes_to_rest_unrefuted`, `rests_unrefuted_around`, `rests_unrefuted_enclosed`, `arising_opens`, `Finite.comes_to_rest_unrefuted`, `World.rests_unrefuted` (continued-change-needs-openness, space-and-its-parts) | balance, dissipation, enclosure | the step law above at each `t ∈ [T, ∞)` | a |
| 同上 | embodiment | `Emb(x, t)`, `Emb(x, t+1)` for the `x` arising or ceasing in the tail | a |
| 同上 | census of activity | only for ceasing, through the census law | a |
| 同上 | decidability | `comes_to_rest_unrefuted`'s ceasing half; `rests_unrefuted_enclosed` needs none (¬¬ enclosure) | b (2) |
| 同上 | whole units | `falls_not_recurring` on the total standing | b (1) |
| 同上 | finiteness | supplies a closed family at each step (all relata) and the census | a |
| `World.enclosure_bounds_change`, `ChangeBound.not_recurring` (counting-under-enclosure) | balance, dissipation, enclosure, embodiment, census | as in the rest theorem, at each `t ≥ T` | a |
| 同上 | decidability, whole units | marks; `falls_by_occurrences` | b (1), b (2) |
| `Balances.runs_down`, `takers_within`, `taking_not_recurring`, `Dissipative.opens`, `finite_taking_not_recurring`, `More.opens`, `opens_of_arising` (no-finite-part-bears-taking) | balance, dissipation | `Bal(t, c)`, `c ∈ cs`; `Diss(ds, t)` for the families containing `cs` at the late steps | a |
| 同上 | finiteness | `finite_taking_not_recurring`: the family of all conditions, closed at every step | a |
| `Flow.rise_with_fall`, `standing_with_fall`, `rise_alone_opens` (rising-and-falling-in-one-exchange) | balance, dissipation | already stated on `ds` at `t` | a — already local |
| `generation_needs_replenishment`, `Embodied.given_of_arises`, `generation_opens`, `generation_not_recurring`, `generation_draws_in` (generation-is-replenishment) | balance, embodiment, dissipation, finiteness | `Bal(t, c)` on the family from `T`; `Emb(x, ·)` for the arising `x`; `Diss` on the closed families; finiteness as above | a |
| `Flow.fed_from_beyond`, `rising_fed_from_beyond`, `generation_fed_from_beyond` (continuing-self-fed-from-beyond) | balance, dissipation, embodiment | at the step and family | a |
| 同上 | decidability | inward or fed decided | b (2) |
| `Flow.replenishment_recurs`, `renewing_recurs`, `uptake_needs_replenishment` (unceasing-generation-needs-renewal) | balance, taking | `Bal(t, c)` on the depleted family over the stretch; `Take(t, f, c)` for the arising formations taking from it | a |
| `Balances.replenished_over`, `renewers_over`, `More.replenishment_unbounded` (more-needs-renewers) | balance | `Bal(t, c)`, `c ∈ cs`, over the stretch | a |
| `More.unceasing`, `More.grows`, `unceasing_of_growth` | taking, census, decidability | `Take` at the first step of the arising formations; listing on the stretch; marks | a, a, b (2) |
| **C. 依存、储备与支持 | | | |
| `continuing_restores`, `consumed_continues_transformed`, `static_dependent` (becoming-dependence-dynamics) | dependent | `Dep(t, g)` for the `g` active at the steps considered | a — `Kept` and `Broken` are already local |
| `Web.Dependent.inactive_below`, `ceases_below`, `Downstream.one_way`, `Mortal.after_its_end` (space-and-its-parts, derived-extent-limits) | dependent, balance | `Dep(t, g)` for the one `g` whose condition falls below its need; `Bal` on that condition | a |
| `Web.Census.over_stretch`, `Census.balanceFrom`, `arisingFrom_of_ceasingFrom` (census-balance, census-balance-under-continuation) | census; decidability | listing on the stretch compared; marks | a; b (2) |
| `Web.carries_zero`, `Carries.lasts`, `lasts_within` (reserve-defers-ending) | dependent; decidability | `Dep` as the zero reserve; marks of `f`'s activity | a; b (2) |
| `Carries.chain_ends_of_em`, `Web.lpo_of_ending` | excluded middle, LPO | the explicit end of a chain | b (2), with the proved boundary |
| `rise_given_by_supported`, `gains_from_supported`, `unsupported_stays`, `nothing_supported_stays` (support-from-the-supported) | balance, acting, dependent | `Bal(t, c)` for the required `c` that rise; `Act(t, g, c)` and `Dep(t, g)` for the givers `g` | a |
| `Balances.supported_iff_within_margin`, `supported_of_net_give`, `admits_of_net_draw`, `closes_nothing`, `opens_nothing` (closing-needs-net-draw, four-cases-of-a-part) | balance | `Bal(s, c)` for `s < t` and the `c` that `f` requires (through `Balances.withheld`) | a; the withheld levels are a disclosed choice of the representation |
| `Balances.consumption_ends_with_feeders`, `unfed_consumption_ends`, `Overshoot.ends_through_feeder` (consumption-ends-with-feeders) | balance, acting, dependent | `Bal(T+k, c)`; `Act(T+k, f, c)`, `Dep(T+k, f)` for the givers `f` of `c`, `k < n` | a |
| `joint_excess_ends`, `stays_below`, `excess_bounded` (own-count-misses-joint-excess) | balance, acting, dependent | as above, on `c` over the stretch | a |
| `DescendsAt.supported`, `unsupported_childless`, `selected_le`, `selection_within` (evolution-on-descent) | acting, dependent | `Act(t, g, x)` for the parent giving at descent; `Dep(t, g)` | a |
| `transmitted_supported`, `transmitted_within` | transmitting | `TransmitsWithin c δ` for the one `c` concerned; the uniform `δ` over all `c` is not used | a |
| `Mortal.without_continues`, `Clearing.undermines_within_renewal` (derived-extent-limits) | balance, dissipation, dependent | at the steps and conditions of the formation considered | a |
| **D. 整体、前提图与逻辑 | | | |
| `World.arising_iff_ceasing`, `World.rests_unrefuted` (space-and-its-parts) | finiteness | a closed family at each step; a listing of every relatum | a |
| 同上 | decidability | the finite-world law | b (2); `World.law_iff_em` proves it cannot be dropped from this statement |
| `World.lpo_of_finite_ends`, `Listed.lpo_of_few` (counting-under-enclosure, continued-change-needs-openness) | decidability | an explicit end step for every finite world | b (2), the proved boundary |
| `World.acting_across`, `acting_of_enclosed`, `Finite.acting`, `Finite.counted` (map-of-premises) | taking, dissipation, enclosure, finiteness, decidability | `Take(t, f, c)` and `Diss(es_t, t)` at the enclosed step; the finite list | a; b (2) for `Finite.counted` |
| `Flow.More.unceasing_reidentified` (identity-across-steps) | taking, census, decidability | as in `More.unceasing` | a, a, b (2) |
| **E. 每一分辨率 | | | |
| `Flow.quantum_bound`, `uptake_bound`, `World.not_recurring_at_resolution`, `World.rests_unrefuted_refinement_counted` (rest-at-every-resolution, rest-with-refinement-counted) | balance, dissipation (`DissipatesBy`), enclosure, embodiment, census | at each step of the tail and the enclosing family | a; the loss in proportion and the counted refinement are b (1), already put to Ren and decided as A |

<a id="14-ren-的决定--for-ren-to-decide"></a>
### 1.4 Ren 的决定

**中文。** 以下各项改动表示本身，所以属于 Ren：
- **(b1) 最小差异。** 已决定：A（属于生成本身）。熵的会话研究它能否推出。
- **(b2) 可判定性。** 保留，或者在不复现的形式中去掉。后一种做法中，明确终止之步的陈述按已证明的边界放弃。已决定（Ren 2026-10-11：“too dualist”，再以“please”接受，[原话](../../../../sources/15-codex-theory-conversations/2026-10-11-decidability-local-imbalance-relatum.md)）：局部化。可判定性不再是表示的承诺；计数或命名一步的规律把在所计数之处已定写作自己的条件，不需要它的规律不用它陈述（P58，`Becoming.Decidedness`，研究 §84，[清点](DECIDABILITY-INVENTORY.md)）。仍用它的：368 条定理的陈述依赖它（77 条计数，291 条关于由判定造出的对象），226 条只在证明中用到（87 条找出一步或成员，89 条分辨相同，16 条造出列表，29 条分情形，5 条造出指示），各有理由；静止定理已不用它，学习者的静止定理（P73）除外：学习者在主张被否证处换假设，陈述依赖分辨值。
- **(b3) 时间。** 只检验更粗的步（采样）是否保持规律，还是也研究连续时间。另一个会话的工作区中有一个尚未提交的 `Sampling` 模块（见 §4）。已决定（Ren 2026-10-12，[原话](../../../../sources/15-codex-theory-conversations/2026-10-12-unit-of-need-and-tower-of-time.md)）：较粗的步已检验（`Becoming.Sampling`）；连续时间在核心中读作一座越来越细的离散读法之塔，由 `Sampling` 连接，连续时间的规律就是每一层上的规律；实数时间是以后的外围对应。损失仍按交换计，不按细步计。
- **(b4) 需要的单位。** 已决定（同上）：较细的单位下，需要与水平以同一单位计；不变的需要随细分放大，以 `r > 0` 为这一读法的条件，所以支持不依赖量度的粒度。这是关于怎样量度需要的表示承诺，公开陈述，不是世界的前提。
- **两种可能的重新奠定（AI 的提议）。**
  - 把不平衡算作关系项：任一步、任一条件上的不平衡，都可以算作一个只给或只取的关系项的交换，就像 R4 把细分算作给予。这样平衡就由表示成立，而它的局部失效成为可见的交换。已决定（Ren 2026-10-11，“please”）：先作为与现行表示等价的表示加以证明（P59，`Becoming.Imbalance`，研究 §85）：每个流都平衡，平衡恰是新增关系项的闲置，活动的前提逐步等价；是否采用由 Ren 定。已决定（Ren 2026-10-14：“please, finish all”，[原话](../../../../sources/15-codex-theory-conversations/2026-10-14-relation-first-refounding.md)）：采用。`Becoming.Reading` 在每个世界中算入其余（`World.withRest`），从交换读出活跃与汲取：平衡、只有活跃者给与取、对交换之律的活动需要支持由读法成立，封闭读作其余闲置；已落地的规律保留其陈述（P107，研究 §125）。
  - 把体现读作定义：活跃就是立着。这会失去形成与条件两个角色的区分，所以 AI 不建议。已决定（同上）：不读作定义；体现仍是前提，在生起或止息的关系项上局部化。

  两者都属于重新奠定表示；Ren 2026-10-11 的决定见上；不平衡关系项已由 Ren 2026-10-14 采用（见上）。

**表示的检验（P77、P78、P88）。** 列出一次已重新奠定：列表恰在成员之间同一已定时能列出一次，否证形式的规律不需要它，按关系不可分辨地计数在每个世界都固定数目等价于排中律（`Becoming.Listing`，研究 §101）。这保留名字与关系的区别，不替 Ren 选择同一的读法。时间也不只检验粗化：停顿与去掉空步保留所名规律，给定足迹时，有交集交换的偏序恰刻画可通过交换无交集相邻步达到的次序（`Becoming.Order`，研究 §102）。P88 对有限、有名的交换段，在对称相连关系与不相连可判定下构造正规形；以自然数为值的完备不变量存在，当且仅当该段的不相连可判定。任意交换的普查可向前传递，两侧分开的重排及含交换足迹的独立重排可双向传递；这不声称中间每步人数相同。给定每步每项的闲置判定可构造最小布尔足迹，其存在的逆刻画另需关系项相等可判定（`Becoming.OrderNormal`，研究 §109）。无名正规形、Foata 同时层、无界运行的正规形、无上述判定的最小足迹、具体闲置不可判定的见证及实际连续时间对应仍开放；固定命名与足迹的读法仍不由这些证明替 Ren 决定。

<a id="2-零前提的重述--zero-premise-restatements"></a>
## 2. 零前提的重述

**现状（P77–P79）。** P77 的列出一次与 P78 的步序见上。P79 不重复 P48 的局部化：它证明所给一步样式的实现恰是它遵守所名条件的规律（`OneStep.every_iff`、`OneStep.laws`），补出所取非零须有取者、所给非零须有给者，精确刻画给者、容量与活动所加的规律，以及单一家族与逐步选家族上的接续（研究 §103）。这关闭所给样式的完备性问题，不是全部生成或全部规律的普遍完备性证明；活跃者计数、整段容量与活动仍开放。下面的旧清点、提议与历史现状按原范围保留。

**现状（P48）。** 下面四条已在 `Becoming.Locality` 中检查并登记为 [laws-of-one-step](../../../../theories/becoming/results/records/laws-of-one-step.md)（[研究 §66](BECOMING-RENEWAL-READING.md#66-一步的规律条件在规律之内p48)）；下面保留的是检查前的提议。检查改变了三处：规律 1 的条件不需要封闭（`Flow.RunsDownOn`：包含所立者、被平衡与耗散的家族即可，封闭只在交换的当且仅当中出现）；规律 3 对所立者不需要体现；规律 2 的不复现形式不需要判定（`Covers.ceasing_not_recurring`），确切计数需要。提议中的 `stock es (t+1) + takers es t ≤ stock es t` 是 `Flow.RunsDownOn.takers_le_fall`。

**现状（P50）。** 清点 C 组（依存、储备与支持，§1.3）与普查平衡已对每个世界重述，条件写在规律之内，由“0 axiom completeness”会话起草并验证（[研究 §71](BECOMING-RENEWAL-READING.md#71-依存储备支持与普查平衡的规律条件在规律之内p50)）。证明对活动的要求只以一种方式出现：给予所用条件者在所用一步被支持（`Flow.GiversSupported`）。不需要 b 类的决定。剩下的是组 B 其余（`Dissipation` 与 `Flow` 中的规律）与组 D。

**现状（P57、P60、P61）。** B 组其余（`Dissipation` 与 `Flow` 中的规律）、D 组与延续之下的普查定律已对每个世界重述，由“0 axiom completeness”会话起草并验证（研究 [§74](BECOMING-RENEWAL-READING.md#74-静止开放与补给的规律条件在规律之内p57)、[§75](BECOMING-RENEWAL-READING.md#75-整体的规律条件在规律之内p60)、[§76](BECOMING-RENEWAL-READING.md#76-延续之下的普查定律只用一个覆盖列表p61)）。共享的引理移入需要它的最低模块（`Flow.BalancesOn` 移入 `Flow`），名称与陈述不变。清点的四组至此都已局部化。剩下的不是局部化：b 类的表示决定（最小差异已由 Ren 定为 A；可判定性由 P58 清点；时间由 `Sampling` 检验），以及超出整单位的量的检验。

**现状（P63、P61b、Sampling）。** C 组中 P50 漏掉的储备一行已局部重述（P63，研究 §79）；P61 的反方向已证（P61b）。时间：较粗的步已检验（`Becoming.Sampling`，研究 §80）：平衡（每个关系项只列出一次时）、耗散、封闭与下降跨粗步合成，不合成回细步，活动、取用与传递依步而定。整单位：以单位读变化时一步的规律成立，以原始计数读时不成立；需要与水平以同一单位计（`Becoming.Units`）。

**现状（P58、P59）。** 可判定性已局部化（P58，研究 §84）：计数是关系，计数存在恰当所计数者已定；计数之间的普查、有限家族中复现的不终止形式与静止定理都不用可判定性；仍用它的定理各有理由，列在[清点](DECIDABILITY-INVENTORY.md)。不平衡关系项已证与现行表示等价（P59，研究 §85），未采用。

**现状（P58c）。** 静止一族按所证强度命名（Ren 2026-10-12：“agree with you”，[原话](../../../../sources/15-codex-theory-conversations/2026-10-12-rest-family-strengths.md)，研究 §111）：从某步起静止不能被否证（`World.RestsFrom`，`World.rests_unrefuted` 等，陈述加强）与只证不复现（`…_not_recurring`）分开；前者也不用判定程序，止息一半在双重否定之内用有限鸽巢（`Covers.ceasing_stops_unrefuted`）。表中名称为现名。

**中文。** 按 Ren 的顺序，从四条规律开始。每条都对每个世界陈述，局部条件写在规律之内。每一条的所作都是“局部化”。下面的形式是提议，在 Lean 中检查之前不作为结论。

1. **一次交换的规律与静止

2. **不再存在需要生起
3. **封闭约束变化
4. **生起需要活跃的给予者

**规律需要的表示承诺

**检查后（P48）
- 可判定：规律 1、3、4 不判定世界的任何谓词，证明只判定数的大小；规律 2 的确切计数需要标记，不复现形式不需要。
- 整单位：规律 1、4 的一步当且仅当只用加法与次序；规律 1 的复现与规律 3 的界用最小差异（A）。超出整单位的量尚未检验；静止由 R4 覆盖（`World.rests_unrefuted_refinement_counted`、`World.arising_opens_refinement_counted`）。
- 时间：较粗的步由局部化的 `Sampling` 检验（落地队列）。
- 有限：所立者的普查只被规律 1 的复现与规律 3 用到，作用只是使每步的总水平是一个数。

<a id="3-不主张什么--what-is-not-claimed"></a>
## 3. 不主张什么

**中文。** 不主张任何前提作为规律被推出；不主张最小差异已被推出（那是熵的会话的问题）；不主张八个前提之外没有别的前提被用到。逻辑、`Std` 与核心的纯净规则不变。已落地的选择定理保持其范围内的成果。

<a id="4-协调--coordination"></a>
## 4. 协调

  更新（P48 落地时）：消息已送达，熵的会话已答复。它的 R5 `Becoming.Entropy` 只导入 `Becoming.Resolution`，不改任何已有模块，排在落地队列第 8 项；它报告 b(1) 的结果是分解而不是推导（尚未落地）。

  更新（P48 落地时）：P46、P47 已落地；同一会话（“0 axiom completeness”）起草了规律 2，并入 `Becoming.Locality`；它把 `Sampling` 局部化（落地队列第 7 项），并交付了清点 C 组的局部重述（第 5 项，P50）。

<a id="5-连续时间范围ai-的提议待-ren-continuous-time-scope-ai-proposal-awaits-ren"></a>
## 5. 连续时间：范围（AI 的提议，待 Ren）

更新（2026-10-12）：Ren 已决定，连续时间在核心中读作越来越细的离散读法之塔（见 §1.4 (b3)）；下面的范围保留为当时的提议。

2026-10-11。会话 “0 axiom completeness” 应整合者之请撰写；没有 Lean，没有成果。Ren：“let's finish one first, then another”——先完成更粗的步（`Sampling`，已在 scratch 中验证，待落地），再做连续时间。下面只是范围。

**中文。**
- **在核心之内能说什么。** 核心只用 Lean 的 prelude，没有实数，所以连续时间在核心里只能读作步的细分：一个细的世界，给定的世界是它在某些时刻的采样。这是 `Sampling` 的反方向。`Sampling` 已证明各局部条件从细步组合到粗步（平衡在每个关系项每步只列一次时，耗散，封闭恰好如此，耗散地运行下去只需两端）；`Cancelling` 与 `Averaging` 已证明反方向不自动成立。连续时间就读作一座塔：每一层都是下一层的采样，没有最细的一层。以实数为时间的模型只能放在外围（可用 Mathlib），用对应定理连到核心。选哪一种属于表示，所以是 Ren 的决定（b3 的第二部分）。
- **塔上可以问的问题（待证，都是猜想）。**
  1. 细分总是存在：把每一粗步的全部交换放在它的第一个细步，其余细步什么也不发生。这时所有局部条件都向下传递。所以单是“存在细分”没有内容，要问的是哪些条件在每一个细分中都成立。
  2. 各层的局部条件：条件在第 k+1 层成立，就在第 k 层成立（由 `Sampling` 得）。所以在任意细的层上成立的条件，在每一个更粗的层上都成立。
  3. 与最小差异（b1，Ren 选 A）相互作用：耗散的每一次取用至少失去一个单位。如果连续的交换在越来越细的步上都算作取用，有限时间里的损失就没有上界。一个猜想：在 A 与耗散之下，塔的每一层上改变的步数都以同一个总量为界（单位不随时间细分而变），所以连续时间中有耗散的生成只有有限多个改变事件，没有芝诺式的无穷细分。如果成立，最小差异就把连续时间中的改变定为离散的，这是 b1 与 b3 的连接。
  4. 只有活跃者给予与取用、有界传递依赖于步（`Strobe`、`Delay`）。在塔中它们需要“活动在区间内保持”（`Web.Held`）在每一层成立，或者需要在没有最细层时重新表述。
- **需要 Ren 决定的。** 核心中的塔，还是外围的实数时间（或两者，用对应定理连接）；交换事件按细步计，还是按交换计（这决定第 3 项）。
