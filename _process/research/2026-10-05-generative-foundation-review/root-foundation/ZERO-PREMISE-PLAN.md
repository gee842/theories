# 零前提的规律 / Laws with zero premises

2026-10-11，Asia/Bangkok。AI（Claude Opus 5.5）应 Ren 的转向指示撰写的计划与清点（[原话](../../../../sources/15-codex-theory-conversations/2026-10-11-zero-premise-laws.md)）：

> stop extending the premise-selection tables. New goal: remove premises and derive the most general versions, zero premises first.

本文是计划与清点。它不向核心加入定理，也不登记成果。下面的分类与“Y 当且仅当 Z”形式是 AI 的提议，待 Ren 审阅；其中 (b) 类需要 Ren 决定。

2026-10-11, Asia/Bangkok. A plan and inventory written by the AI (Claude Opus 5.5) following Ren's redirect. Nothing enters the core and no result is registered. The classification and the proposed “Y iff Z” forms are the AI's, pending Ren; the items in class (b) need Ren's decision.

## 0. 方向 / The direction

**中文。** 到 P45 为止，前进的方式是选择表：对八个前提的 256 个选择，各给出恰在何处成立的规律。现在反过来：取每条规律，去掉前提，使它对每个世界成立，而把证明实际用到的条件写进规律本身，作为关于该世界在那些步、那些关系项上的条件 Z。规律取确切的形式“Y 当且仅当 Z”；选择定理应作为推论得出：一个前提对每一步都成立，就使 Z 在每一步成立。表示之内各前提已证明是偶然的、彼此独立的（`World.contingent`、`World.independent`），所以从不声称某个前提作为规律被推出；推出的只是带着局部条件的规律。每一步都写明所作的是哪一种：局部化；重新奠定表示（需 Ren 决定）；或推广表示。

**English.** Up to P45 the work advanced by selection tables: for each of the 256 selections of the eight premises, the laws holding exactly where it is selected. The direction is now reversed. Each law is taken, its premises are removed, and it is stated for every world, with the condition its proof actually uses written into the law itself as a condition Z on that world at those steps and relata. The law takes the exact form “Y iff Z”. The selection theorems should follow as corollaries: a premise holding at every step makes Z hold at every step. Within the representation the premises are proved contingent and independent (`World.contingent`, `World.independent`). So no premise is ever claimed as derived as a law; what is derived is the law with its local condition. Each move is named as one of three: localize; re-found the representation (Ren's decision); or generalize the representation.

## 1. 清点 / The inventory

### 1.1 方法 / Method

**中文。** 对象是第一部分的主要定理：其记录的 canonical source 是 Becoming 核心模块、不属第二部分（Significance、Metaethics、Standpoints、Ranking、Renewal、Bridge、Correspondence）的 39 条成果记录所列的定理。脚本从这些记录所列声明的签名中找出用到八个前提、有限、被围住或可判定的，共 355 处，其中 339 处在定理上（[脚本](ZERO-PREMISE-INVENTORY.py)）；见证世界（例如 `Shuttle.shuttle`、`Brood.brood`）不是规律，不计。然后逐一读证明，看前提在哪一步、对哪些关系项或家族被用到。分类：
- (a) 可局部化：证明只在某些步、对某些关系项或家族用到它；
- (b) 属于表示，需 Ren 决定；
- (c) 确实需要全局成立。

**English.** The scope is the main theorems of Part I: those listed by the 39 result records whose canonical source is a Becoming core module outside Part II (Significance, Metaethics, Standpoints, Ranking, Renewal, Bridge and Correspondence are excluded). A script found the declarations listed by those records whose signatures use any of the eight premises, finiteness, enclosure or decidability: 355 in all, 339 of them theorems ([script](ZERO-PREMISE-INVENTORY.py)); witness worlds such as `Shuttle.shuttle` and `Brood.brood` are not laws and are not counted. Each proof was then read to see at which step, and for which relata or family, it uses the premise. The classes are:
- (a) localizable to those steps and relata;
- (b) belonging to the representation, which needs Ren's decision;
- (c) genuinely needed globally.

记号 / Notation: `t` a step; `x` a relatum whose standing or activity changes across `t`; `f` a relatum present in the flow at `t`; `c` a condition; `es_t` the family closed at `t`; `[T, ∞)` the steps from `T` on. “Bal(t, c)” is balance at one step and condition: `level (t+1) c + taken t c = level t c + given t c`. “Diss(es, t)” is `Flow.DissipatesOn es t`. “Emb(x, t)” is `active t x ↔ 0 < level t x`. “Act(t, f, c)” and “Take(t, f, c)” are the instances of only active relata giving and taking. “Dep(t, g)” is `active t g → Supported t g`.

### 1.2 结论 / Findings

**中文。**
- **八个前提的每一处使用都属 (a)。** 每个证明都只在特定的步、对特定的关系项或家族用到前提：平衡在 `(t, c)` 上，`c` 是水平改变者或被围住家族的成员；只有活跃者给予或取用，在给予或取用 `x` 的那个 `f` 上；耗散，在那一步被围住的那个家族 `es_t` 上；体现，在开始或不再活跃的那个 `x` 上，于 `t` 与 `t+1`；活动需要支持，在那一步活跃的那个 `g` 上；普查，在所计数的那些步上；有界传递，在世系所涉的条件 `c` 上。没有哪处证明用到前提对一切步、一切关系项的普遍形式。
- **有限与被围住也属 (a)。** 有限只经由它的局部推论被使用：每步有一个封闭的家族（全部关系项），每步有普查，计数有界。被围住本身就是关于一步的条件。静止定理要求被围住的步从 `T` 起不断，这是对尾段 `[T, ∞)` 的每一步的条件，仍是局部的：只有那些步上被用到。
- **(b) 类是表示的承诺，共五项。**
  1. 以整单位计的量：静止依靠总水平是自然数、不能无穷次下降（`falls_finitely`）；耗散中的 `sign` 项（每次取用至少失去一个单位）就是最小差异。Ren 已为最小差异选 A（属于生成本身，[来源](../../../../sources/15-codex-theory-conversations/2026-10-11-difference-in-becoming.md)），R4 把单位的细分算作给予。最小损失能否推出由熵的会话研究，这里不重复。
  2. 被计数处的可判定性（`mark`、计数表）。
  3. 离散的步与共同的时间索引。
  4. 流中每个参与者列出一次，家族不重复（`Distinct`）。
  5. 逐点（`Pointwise`，代替函数外延性）。
- **(c) 类：八个前提中没有。** 唯一被证明不能局部化的需要是逻辑的，不是关于世界的前提：要对每个有限世界给出此后不再生起的一步，就推出有限全知原则（`World.lpo_of_finite_ends`、`Listed.lpo_of_few`、`Web.lpo_of_ending`）；不加可判定性而要求有限世界中生起复现恰当止息复现，就等于排中律（`World.law_iff_em`）。这些是 (b) 中第 2 项的边界：去掉可判定性时，“明确的终止之步”的陈述形式不能保留，“不复现”的形式可以保留。

**English.**
- **Every use of the eight premises is in class (a).** Each proof uses a premise only at particular steps and for particular relata or families:
  - balance at `(t, c)`, where `c` is a condition whose level changes or a member of the enclosing family;
  - only active relata giving or taking, at the `f` that gives to or takes from `x`;
  - dissipation, on the family `es_t` closed at that step;
  - embodiment, at the `x` that arises or ceases, at `t` and `t+1`;
  - activity needing support, at the `g` active at that step;
  - a census, at the steps counted;
  - bounded transmission, at the condition `c` the lineage concerns.

  No proof uses a premise in its universal form, over every step and every relatum.
- **Finiteness and enclosure are in class (a) too.** Finiteness is used only through its local consequences: a closed family at each step (all relata), a census at each step, and bounded counts. Enclosure is a condition on a step. The rest theorem asks for enclosure at every step from `T` on. That is a condition on each step of the tail `[T, ∞)`, still local: it is used only at those steps.
- **Class (b), the commitments of the representation, has five items.**
  1. Amounts in whole units. Rest relies on the total standing being a natural number, which cannot fall infinitely often (`falls_finitely`). The `sign` term of dissipation, at least a unit lost whenever something is taken, is the least difference. Ren chose A for the least difference: it belongs to becoming itself ([source](../../../../sources/15-codex-theory-conversations/2026-10-11-difference-in-becoming.md)). R4 counts the refinement of the unit as a giving. Whether the least loss can be derived is the entropy session's question and is not duplicated here.
  2. Decidability where counted (`mark`, tallies).
  3. Discrete steps and a shared time index.
  4. Each relatum taking part in the flow listed once, and families without repetition (`Distinct`).
  5. Pointwise properties (`Pointwise`, in place of function extensionality).
- **Class (c): none among the eight premises.** The only needs proved not to localize are logical, not premises about worlds:
  - an explicit step after which nothing arises, asked of every finite world, gives the limited principle of omniscience (`World.lpo_of_finite_ends`, `Listed.lpo_of_few`, `Web.lpo_of_ending`);
  - asking of finite worlds without decidability that arising recurs exactly when ceasing does is excluded middle (`World.law_iff_em`).

  These mark the boundary of item 2 of class (b). Without decidability, statements naming an explicit end step cannot be kept; statements that something does not recur can.

### 1.3 逐条 / Theorem by theorem

列中“位置”写证明在哪一步、对哪些关系项或家族用到它。“类”写 a、b 或 c。/ “Where” gives the step and the relata or family at which the proof uses the premise; “Class” is a, b or c.

| 定理 / Theorem (record) | 前提 / Premise | 位置 / Where | 类 / Class |
|---|---|---|---|
| **A. 计数 / Counting** | | | |
| `Web.arising_of_ceasing`, `World.arising_of_ceasing` (ceasing-needs-arising) | census | listing at the steps of `[N, N+n]` for each `N`; only `\|alive N\|` and the census balance on the stretch are used | a — a finite list holding the active at one step `N` after which nothing arises suffices (with nothing arising, later activity is within it) |
| 同上 / same | decidability | `mark (Ceases t a)`, `mark (Arises t a)` on the listed relata | b (2) |
| `Web.unceasing_iff_bounded`, `CountedBy.arising_iff_ceasing` (bounded-census-keeps-pace) | census; bound `B`/`K` | listing on the stretch; `\|alive t\| ≤ K` at arbitrarily late `t` | a — already an exact iff without a bound: `Listed.ceasing_iff_shortfall`, `Listed.coming_iff_excess` |
| `Listed.tally`, `counting_laws`, `tally_iff_counted` (whole-law-of-counting) | decidability | the marks counted | b (2); no premise on worlds |
| `counting_binds_jointly`, `Web.Embodied.arises_given` (whole-law-of-counting, life-as-condition-of-life) | balance | `Bal(t, x)` for the `x` arising across `t` | a |
| 同上 / same | acting | `Act(t, f, x)` for the `f` present giving to `x` | a |
| 同上 / same | embodiment | `Emb(x, t)`, `Emb(x, t+1)` | a |
| 同上 / same | census | only to turn “`f` active at `t`” into a positive count at `t` | a |
| `World.taking_binds_counting` | taking | `Take(t, f, c)` for each `f` present at `t` (nothing active, so nothing taken) | a |
| 同上 / same | balance | `Bal(t, c)` for `x` and for the members of the family active after `t` | a |
| 同上 / same | dissipation | `Diss(alive (t+1), t)`: the family active after the step | a |
| 同上 / same | embodiment, census | `Emb(c, t)`, `Emb(c, t+1)` on that family; listing at `t`, `t+1` | a |
| `World.enclosed_binds_counting` | balance, dissipation | `Bal(t, x)`; `Diss(cs, t)` for the `cs` closed at `t` | a |
| 同上 / same | embodiment | `Emb(c, t)` for `c ∈ cs`; `Emb(x, t)`, `Emb(x, t+1)` | a |
| `counting_under`, `counting_binds_iff`, `enclosed_counting_under`, `finite_counting_under`, `binding_*` (selection tables) | all | through the laws above and B3 | a, b (2) — become corollaries |
| **B. 静止与开放 / Rest and openness** | | | |
| `Flow.standing_runs_down`, `standing_never_rises`, `change_lowers`, `exchange_lowers`, `fall_lowers_on`, `rise_lowers_on` (continued-change-needs-openness, rising-and-falling-in-one-exchange) | balance | `Bal(t, c)`, `c ∈ es_t` (`Balances.over` sums them) | a |
| 同上 / same | dissipation | `Diss(es_t, t)` | a; its `sign` term is b (1) |
| 同上 / same | standing census | `stand t`, `stand (t+1)` only to equate the total standing with `stock es_t` | a — removable: `es_t` already holds what stands |
| `Flow.stills`, `exchanges_finitely`, `World.arising_stops`, `comes_to_rest`, `rests_around`, `rests_enclosed`, `arising_opens`, `Finite.comes_to_rest`, `World.rests` (continued-change-needs-openness, space-and-its-parts) | balance, dissipation, enclosure | the step law above at each `t ∈ [T, ∞)` | a |
| 同上 / same | embodiment | `Emb(x, t)`, `Emb(x, t+1)` for the `x` arising or ceasing in the tail | a |
| 同上 / same | census of activity | only for ceasing, through the census law | a |
| 同上 / same | decidability | `comes_to_rest`'s ceasing half; `rests_enclosed` needs none (¬¬ enclosure) | b (2) |
| 同上 / same | whole units | `falls_finitely` on the total standing | b (1) |
| 同上 / same | finiteness | supplies a closed family at each step (all relata) and the census | a |
| `World.enclosure_bounds_change`, `ChangeBound.not_recurring` (counting-under-enclosure) | balance, dissipation, enclosure, embodiment, census | as in the rest theorem, at each `t ≥ T` | a |
| 同上 / same | decidability, whole units | marks; `falls_by_occurrences` | b (1), b (2) |
| `Balances.runs_down`, `takers_within`, `taking_ceases`, `Dissipative.opens`, `finite_ceases`, `More.opens`, `opens_of_arising` (no-finite-part-bears-taking) | balance, dissipation | `Bal(t, c)`, `c ∈ cs`; `Diss(ds, t)` for the families containing `cs` at the late steps | a |
| 同上 / same | finiteness | `finite_ceases`: the family of all conditions, closed at every step | a |
| `Flow.rise_with_fall`, `standing_with_fall`, `rise_alone_opens` (rising-and-falling-in-one-exchange) | balance, dissipation | already stated on `ds` at `t` | a — already local |
| `generation_needs_replenishment`, `Embodied.given_of_arises`, `generation_opens`, `generation_ceases`, `generation_draws_in` (generation-is-replenishment) | balance, embodiment, dissipation, finiteness | `Bal(t, c)` on the family from `T`; `Emb(x, ·)` for the arising `x`; `Diss` on the closed families; finiteness as above | a |
| `Flow.fed_from_beyond`, `rising_fed_from_beyond`, `generation_fed_from_beyond` (continuing-self-fed-from-beyond) | balance, dissipation, embodiment | at the step and family | a |
| 同上 / same | decidability | inward or fed decided | b (2) |
| `Flow.replenishment_recurs`, `renewing_recurs`, `uptake_needs_replenishment` (unceasing-generation-needs-renewal) | balance, taking | `Bal(t, c)` on the depleted family over the stretch; `Take(t, f, c)` for the arising formations taking from it | a |
| `Balances.replenished_over`, `renewers_over`, `More.replenishment_unbounded` (more-needs-renewers) | balance | `Bal(t, c)`, `c ∈ cs`, over the stretch | a |
| `More.unceasing`, `More.grows`, `unceasing_of_growth` | taking, census, decidability | `Take` at the first step of the arising formations; listing on the stretch; marks | a, a, b (2) |
| **C. 依存、储备与支持 / Dependence, reserve and support** | | | |
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
| **D. 整体、前提图与逻辑 / The whole, the map of premises, and logic** | | | |
| `World.arising_iff_ceasing`, `World.rests` (space-and-its-parts) | finiteness | a closed family at each step; a listing of every relatum | a |
| 同上 / same | decidability | the finite-world law | b (2); `World.law_iff_em` proves it cannot be dropped from this statement |
| `World.lpo_of_finite_ends`, `Listed.lpo_of_few` (counting-under-enclosure, continued-change-needs-openness) | decidability | an explicit end step for every finite world | b (2), the proved boundary |
| `World.acting_across`, `acting_of_enclosed`, `Finite.acting`, `Finite.counted` (map-of-premises) | taking, dissipation, enclosure, finiteness, decidability | `Take(t, f, c)` and `Diss(es_t, t)` at the enclosed step; the finite list | a; b (2) for `Finite.counted` |
| `Flow.More.unceasing_reidentified` (identity-across-steps) | taking, census, decidability | as in `More.unceasing` | a, a, b (2) |
| **E. 每一分辨率 / Every resolution** (R-line, another session) | | | |
| `Flow.quantum_bound`, `uptake_bound`, `World.rests_at_resolution`, `World.rests_refinement_counted` (rest-at-every-resolution, rest-with-refinement-counted) | balance, dissipation (`DissipatesBy`), enclosure, embodiment, census | at each step of the tail and the enclosing family | a; the loss in proportion and the counted refinement are b (1), already put to Ren and decided as A |

### 1.4 Ren 的决定 / For Ren to decide

**中文。** 以下各项改动表示本身，所以属于 Ren：
- **(b1) 最小差异。** 已决定：A（属于生成本身）。熵的会话研究它能否推出。
- **(b2) 可判定性。** 保留，或者在不复现的形式中去掉。后一种做法中，明确终止之步的陈述按已证明的边界放弃。已决定（Ren 2026-10-11：“too dualist”，再以“please”接受，[原话](../../../../sources/15-codex-theory-conversations/2026-10-11-decidability-local-imbalance-relatum.md)）：局部化。可判定性不再是表示的承诺；计数或命名一步的规律把在所计数之处已定写作自己的条件，不需要它的规律不用它陈述（P58，`Becoming.Decidedness`，研究 §84，[清点](DECIDABILITY-INVENTORY.md)）。仍用它的：226 条定理的陈述依赖它（73 条计数，153 条关于由判定造出的对象），106 条只在证明中用到（53 条找出一步或成员，39 条分辨相同，8 条造出列表，5 条分情形，1 条造出指示），各有理由；静止定理已不用它，学习者的静止定理（P73）除外：学习者在主张被否证处换假设，陈述依赖分辨值。
- **(b3) 时间。** 只检验更粗的步（采样）是否保持规律，还是也研究连续时间。另一个会话的工作区中有一个尚未提交的 `Sampling` 模块（见 §4）。已决定（Ren 2026-10-12，[原话](../../../../sources/15-codex-theory-conversations/2026-10-12-unit-of-need-and-tower-of-time.md)）：较粗的步已检验（`Becoming.Sampling`）；连续时间在核心中读作一座越来越细的离散读法之塔，由 `Sampling` 连接，连续时间的规律就是每一层上的规律；实数时间是以后的外围对应。损失仍按交换计，不按细步计。
- **(b4) 需要的单位。** 已决定（同上）：较细的单位下，需要与水平以同一单位计；不变的需要随细分放大，以 `r > 0` 为这一读法的条件，所以支持不依赖量度的粒度。这是关于怎样量度需要的表示承诺，公开陈述，不是世界的前提。
- **两种可能的重新奠定（AI 的提议）。**
  - 把不平衡算作关系项：任一步、任一条件上的不平衡，都可以算作一个只给或只取的关系项的交换，就像 R4 把细分算作给予。这样平衡就由表示成立，而它的局部失效成为可见的交换。已决定（Ren 2026-10-11，“please”）：先作为与现行表示等价的表示加以证明（P59，`Becoming.Imbalance`，研究 §85）：每个流都平衡，平衡恰是新增关系项的闲置，活动的前提逐步等价；是否采用由 Ren 定。
  - 把体现读作定义：活跃就是立着。这会失去形成与条件两个角色的区分，所以 AI 不建议。已决定（同上）：不读作定义；体现仍是前提，在生起或止息的关系项上局部化。

  两者都属于重新奠定表示；Ren 2026-10-11 的决定见上，是否采用不平衡关系项仍由 Ren 定。

**English.** These change the representation itself and so are Ren's:
- **(b1) The least difference.** Decided: A, it belongs to becoming. Whether it can be derived is the entropy session's question.
- **(b2) Decidability.** Keep it, or drop it in the forms stating that something does not recur. In the second case, statements naming an explicit end step are given up, as the proved boundary requires. Decided (Ren, 11 October 2026: “too dualist”, then “please”, [words](../../../../sources/15-codex-theory-conversations/2026-10-11-decidability-local-imbalance-relatum.md)): made local. Decidability is no longer a commitment of the representation; the laws that count or name a step state decidedness where they count as their own condition, and the laws that do not need it are stated without it (P58, `Becoming.Decidedness`, study section 84, [inventory](DECIDABILITY-INVENTORY.md)). What still uses it: 226 theorems whose statements depend on it (73 count, 153 concern objects built by deciding) and 106 that use it only in proofs (53 find a step or a member, 39 tell same from different, 8 build a list, 5 split on a case, 1 build an indicator), each with its reason; the rest theorems no longer use it, except the learner's (P73): the learner moves on where its claim is refuted, so their statements depend on telling values apart.
- **(b3) Time.** Test only coarser steps (sampling), or also continuous time. Another session's worktree holds an uncommitted `Sampling` module (section 4). Decided (Ren, 12 October 2026, [words](../../../../sources/15-codex-theory-conversations/2026-10-12-unit-of-need-and-tower-of-time.md)): coarser steps are tested (`Becoming.Sampling`); continuous time is read in the core as a tower of ever finer discrete readings linked by `Sampling`, a law of continuous time being a law at every level; real-valued time is a later periphery correspondence. Loss stays counted per exchange, not per fine step.
- **(b4) The unit of need.** Decided (same source): at a finer unit a need is counted in the same unit as the level; an unchanged need scales with the split, with `r > 0` the reading's condition, so support does not depend on the grain of measurement. This is a commitment of the representation about how need is measured, stated openly, not a premise on worlds.
- **Two possible re-foundings, proposed by the AI.**
  - Count imbalance as a relatum. An imbalance at a step and condition can be counted as the exchange of a relatum that only gives or only takes, as R4 counts the refinement as a giving. Balance then holds by the representation, and its local failure becomes a visible exchange. Decided (Ren, 11 October 2026, “please”): proved first as a representation equivalent to the current one (P59, `Becoming.Imbalance`, study section 85): every flow balances, balance is exactly the added relatum idle, and the activity premises are equivalent step by step; whether to adopt it is Ren's.
  - Read embodiment as a definition: to be active is to stand. This loses the distinction between the two roles of formation and condition, so the AI does not recommend it. Decided (same source): not read as a definition; embodiment stays a premise, made local at the relata that arise or cease.

  Both re-found the representation; Ren's decisions of 11 October 2026 are above, and whether to adopt the imbalance relatum is still Ren's.

**表示的检验（P77、P78）。** 列出一次已重新奠定：列表恰在成员之间同一已定时能列出一次，否证形式的规律不需要它，按关系不可分辨地计数在每个世界都固定数目等价于排中律（`Becoming.Listing`，研究 §101）。这保留名字与关系的区别，不替 Ren 选择同一的读法。时间也不只检验粗化：停顿与去掉空步保留所名规律，给定足迹时，有交集交换的偏序恰刻画可通过交换无交集相邻步达到的次序（`Becoming.Order`，研究 §102）。足迹本身、最小足迹、正规形、重排中的普查及实际时间对应仍须分别处理。

**Tests of the representation (P77, P78).** Listing once is re-founded: a list can be listed once exactly where identity among its members is decided; refutation laws need no such premise, and fixing every list's number up to relational indiscernibility in every world is equivalent to excluded middle (`Becoming.Listing`, study §101). This preserves the distinction between names and relations and does not choose Ren's reading of identity. Time is tested beyond coarsening: stuttering and removing idle steps keep the named laws; for a supplied footprint, the partial order of joined exchanges characterizes the orders reached by commuting unjoined neighbouring exchanges (`Becoming.Order`, study §102). The footprint itself, the least footprint, normal forms, censuses along reorderings and actual time correspondence remain separate questions.

## 2. 零前提的重述 / Zero-premise restatements

**现状（P77–P79）。** P77 的列出一次与 P78 的步序见上。P79 不重复 P48 的局部化：它证明所给一步样式的实现恰是它遵守所名条件的规律（`OneStep.every_iff`、`OneStep.laws`），补出所取非零须有取者、所给非零须有给者，精确刻画给者、容量与活动所加的规律，以及单一家族与逐步选家族上的接续（研究 §103）。这关闭所给样式的完备性问题，不是全部生成或全部规律的普遍完备性证明；活跃者计数、整段容量与活动仍开放。下面的旧清点、提议与历史现状按原范围保留。

**Status (P77–P79).** P77's listing once and P78's step order are stated above. P79 adds to P48's localization: realizing a specified one-step pattern is exactly obeying the laws of the named conditions (`OneStep.every_iff`, `OneStep.laws`). It supplies the missing nonzero-taking/taker and nonzero-giving/giver laws, characterizes exactly what givers, capacity and activity add, and the chaining on one family or continuity on families chosen step by step (study §103). This closes completeness for those patterns, not universal completeness for becoming or every law. Counts of active relata and capacity and activity over runs remain open. The earlier inventory, proposals and historical status below retain their original scope.

**现状（P48）。** 下面四条已在 `Becoming.Locality` 中检查并登记为 [laws-of-one-step](../../../../theories/becoming/results/records/laws-of-one-step.md)（[研究 §66](BECOMING-RENEWAL-READING.md#66-一步的规律条件在规律之内p48)）；下面保留的是检查前的提议。检查改变了三处：规律 1 的条件不需要封闭（`Flow.RunsDownOn`：包含所立者、被平衡与耗散的家族即可，封闭只在交换的当且仅当中出现）；规律 3 对所立者不需要体现；规律 2 的不复现形式不需要判定（`Covers.ceasing_not_recurring`），确切计数需要。提议中的 `stock es (t+1) + takers es t ≤ stock es t` 是 `Flow.RunsDownOn.takers_le_fall`。

**Status (P48).** The four laws below are checked in `Becoming.Locality` and registered as [laws-of-one-step](../../../../theories/becoming/results/records/laws-of-one-step.md) ([study section 66](BECOMING-RENEWAL-READING.md#66-一步的规律条件在规律之内p48)); what follows keeps the proposals as they stood before the check. The check changed three things: law 1's condition needs no closure (`Flow.RunsDownOn`: a family holding what stands, balanced and dissipated on, suffices, closure entering only the iff for the exchange); law 3 needs no embodiment for what stands; law 2's form that ceasing does not recur needs no decision (`Covers.ceasing_not_recurring`), while the exact count does. The proposed `stock es (t+1) + takers es t ≤ stock es t` is `Flow.RunsDownOn.takers_le_fall`.

**现状（P50）。** 清点 C 组（依存、储备与支持，§1.3）与普查平衡已对每个世界重述，条件写在规律之内，由“0 axiom completeness”会话起草并验证（[研究 §71](BECOMING-RENEWAL-READING.md#71-依存储备支持与普查平衡的规律条件在规律之内p50)）。证明对活动的要求只以一种方式出现：给予所用条件者在所用一步被支持（`Flow.GiversSupported`）。不需要 b 类的决定。剩下的是组 B 其余（`Dissipation` 与 `Flow` 中的规律）与组 D。

**Status (P50).** Group C of the inventory (dependence, reserve and support, section 1.3) and the census balance are restated for every world with their condition inside them, drafted and verified by the session “0 axiom completeness” ([study section 71](BECOMING-RENEWAL-READING.md#71-依存储备支持与普查平衡的规律条件在规律之内p50)). What the proofs need of activity appears in one way only: whatever gives to the condition used is supported across the step used (`Flow.GiversSupported`). No decision of class (b) was needed. What remains is the rest of group B (the laws in `Dissipation` and `Flow`) and group D.

**现状（P57、P60、P61）。** B 组其余（`Dissipation` 与 `Flow` 中的规律）、D 组与延续之下的普查定律已对每个世界重述，由“0 axiom completeness”会话起草并验证（研究 [§74](BECOMING-RENEWAL-READING.md#74-静止开放与补给的规律条件在规律之内p57)、[§75](BECOMING-RENEWAL-READING.md#75-整体的规律条件在规律之内p60)、[§76](BECOMING-RENEWAL-READING.md#76-延续之下的普查定律只用一个覆盖列表p61)）。共享的引理移入需要它的最低模块（`Flow.BalancesOn` 移入 `Flow`），名称与陈述不变。清点的四组至此都已局部化。剩下的不是局部化：b 类的表示决定（最小差异已由 Ren 定为 A；可判定性由 P58 清点；时间由 `Sampling` 检验），以及超出整单位的量的检验。

**Status (P57, P60, P61).** The rest of group B (the laws in `Dissipation` and `Flow`), group D and the census law under a continuation are restated for every world, drafted and verified by the session “0 axiom completeness” (study sections [74](BECOMING-RENEWAL-READING.md#74-静止开放与补给的规律条件在规律之内p57), [75](BECOMING-RENEWAL-READING.md#75-整体的规律条件在规律之内p60), [76](BECOMING-RENEWAL-READING.md#76-延续之下的普查定律只用一个覆盖列表p61)). Shared lemmas move to the lowest module that needs them (`Flow.BalancesOn` into `Flow`), names and statements unchanged. Every group of the inventory is now localized. What remains is not localization: the representation decisions of class (b) (the least difference, decided A by Ren; decidability, inventoried by P58; time, tested by `Sampling`) and the test with amounts finer than whole units.

**现状（P63、P61b、Sampling）。** C 组中 P50 漏掉的储备一行已局部重述（P63，研究 §79）；P61 的反方向已证（P61b）。时间：较粗的步已检验（`Becoming.Sampling`，研究 §80）：平衡（每个关系项只列出一次时）、耗散、封闭与下降跨粗步合成，不合成回细步，活动、取用与传递依步而定。整单位：以单位读变化时一步的规律成立，以原始计数读时不成立；需要与水平以同一单位计（`Becoming.Units`）。

**Status (P63, P61b, Sampling).** The reserve row of group C missed in P50 is restated locally (P63, study section 79); the converse of P61 is proved (P61b). Time: coarser steps are tested (`Becoming.Sampling`, study section 80): balance (with each relatum listed once), dissipation, closure and running down compose across a coarse step, nothing composes back to the fine steps, and acting, taking and transmission are step-relative. Whole units: the laws of one step hold with change read in the unit and fail read in raw counts; a need is counted in the same unit as the level (`Becoming.Units`).

**现状（P58、P59）。** 可判定性已局部化（P58，研究 §84）：计数是关系，计数存在恰当所计数者已定；计数之间的普查、有限家族中复现的不终止形式与静止定理都不用可判定性；仍用它的定理各有理由，列在[清点](DECIDABILITY-INVENTORY.md)。不平衡关系项已证与现行表示等价（P59，研究 §85），未采用。

**Status (P58, P59).** Decidability is made local (P58, study section 84): a count is a relation, existing exactly where what it counts is decided; the census between counts, the never-stopping forms of recurrence in finite families and the rest theorems need no decidedness; the theorems still using it each have a reason, listed in the [inventory](DECIDABILITY-INVENTORY.md). The imbalance relatum is proved equivalent to the current representation (P59, study section 85) and not adopted.

**中文。** 按 Ren 的顺序，从四条规律开始。每条都对每个世界陈述，局部条件写在规律之内。每一条的所作都是“局部化”。下面的形式是提议，在 Lean 中检查之前不作为结论。

**English.** In Ren's order, four laws come first. Each is stated for every world, with its local condition inside it. The move in each is “localize”. The forms below are proposals, not results until checked in Lean.

1. **一次交换的规律与静止 / The law of one exchange, and rest.** Let `es` be a family without repetition, closed across `t`, holding whatever stands at `t` or `t+1`, balanced on its members across `t` and dissipated on across `t`. Then `stock es (t+1) + takers es t ≤ stock es t`, and the following are equivalent (“Y iff Z”):
   - some condition's standing changes across `t`;
   - the total standing falls across `t`;
   - some relatum taking part takes or gives across `t`.

   Rest is the corollary over a tail: if this holds at every step of `[T, T+N)`, the steps there at which some standing changes number at most `stock(T) − stock(T+N)`. Continued change needs openness: change recurs only where the local condition fails at arbitrarily late steps. With what stands finite at each step, so that the total standing is a number, the count is exact: from `T`, the changes at steps meeting the condition number at most the total standing at `T` plus the rises of the total standing at the steps not meeting it. The selection results follow, since the eight premises with enclosure give the condition at every step.
2. **不再存在需要生起 / Ceasing needs arising.** If a finite list holds the relata active at step `N` and nothing arises from `N` on, then at each later step the relata active, with those that ceased since `N`, number exactly those active at `N`. So ceasing recurs with arising stopped at `N` only if no finite list holds what is active at any step from `N`. The census law is the corollary under a census. The exact iffs `Listed.ceasing_iff_shortfall` and `Listed.coming_iff_excess` remain, with a listing needed only at the steps they compare.
3. **封闭约束变化 / Closure bounds change.** Over steps `[T, T+N)` each meeting the condition of item 1, the relata standing at `T+N`, with the steps at which some standing changed, number at most the total standing at `T`. This needs no embodiment. For activity, embodiment is needed only at the relata that arise or cease at those steps. `World.enclosure_bounds_change` and P47's `World.enclosure_bounds_standing` are corollaries.
4. **生起需要活跃的给予者 / Arising needs an active giver.** This recasts the three lemmas of the withdrawn P48. With balance at `(t, x)`, each of the following is an exact iff:
   - (i) `x` comes to stand across `t` iff `level t x = 0` and `taken t x < given t x`;
   - (ii) `x` ceases to stand across `t` iff `0 < level t x` and `taken t x = level t x + given t x`;
   - (iii) across a step at which nothing is taken from a family holding what stands after it, balanced on its members across the step, some member rises iff some relatum taking part gives to the family without taking from it; coming to stand is such a rise. Where the family is also closed across the step, dissipation on it at that step excludes exactly this, so nothing comes to stand.

   Corollaries:
   - with `Emb(x, t)` and `Emb(x, t+1)`, an `x` arising across `t` is given to by a relatum other than `x`; with `Act(t, f, x)` for its givers, something is active at `t`;
   - `Web.Embodied.arises_given`, `counting_binds_jointly`, `taking_binds_counting` and the three P48 lemmas.

**规律需要的表示承诺 / Commitments each law needs (step 4, to be tested).**
- Law 4 (i)–(iii) needs no whole unit: it is ordered-sum arithmetic of one step. It needs no decidability. It concerns one step, so whether it survives coarser steps turns on balance composing, which the uncommitted `Sampling` module reports it does.
- Laws 1 and 3 need the least difference, b (1). With finer units they fail unless the refinement is counted (R4) or the loss is proportional (R3). They need no decidability in their “does not recur” form, and they need discrete steps.
- Law 2 needs decidability for the count; whether a ¬¬ or pigeonhole form avoids it is to be tested. It needs discrete steps.

**检查后（P48）/ As checked (P48).**
- 可判定：规律 1、3、4 不判定世界的任何谓词，证明只判定数的大小；规律 2 的确切计数需要标记，不复现形式不需要。 / Decidability: laws 1, 3 and 4 decide no predicate of the world, their proofs deciding only the order of numbers; law 2's exact count needs marks, its form that ceasing does not recur none.
- 整单位：规律 1、4 的一步当且仅当只用加法与次序；规律 1 的复现与规律 3 的界用最小差异（A）。超出整单位的量尚未检验；静止由 R4 覆盖（`World.rests_refinement_counted`、`World.arising_opens_refinement_counted`）。 / Whole units: the one-step iffs of laws 1 and 4 use addition and order only; the recurrence of law 1 and the bounds of law 3 use the least difference (A). Amounts finer than whole units are not yet tested; rest is covered by R4 (`World.rests_refinement_counted`, `World.arising_opens_refinement_counted`).
- 时间：较粗的步由局部化的 `Sampling` 检验（落地队列）。 / Time: coarser steps are tested by the localized `Sampling` (landing queue).
- 有限：所立者的普查只被规律 1 的复现与规律 3 用到，作用只是使每步的总水平是一个数。 / Finiteness: the census of what stands is used only by law 1's recurrence and by law 3, to make the total standing a number at each step.

## 3. 不主张什么 / What is not claimed

**中文。** 不主张任何前提作为规律被推出；不主张最小差异已被推出（那是熵的会话的问题）；不主张八个前提之外没有别的前提被用到。逻辑、`Std` 与核心的纯净规则不变。已落地的选择定理保持其范围内的成果。

**English.** No premise is claimed derived as a law. The least difference is not claimed derived; that is the entropy session's question. It is not claimed that no premise beyond the eight is used. The logic, `Std` and the pure-core rules are unchanged. The selection theorems already landed remain results at their scope.

## 4. 协调 / Coordination

- **The entropy session** (“Derive entropy: is a lossless exchange possible?”). A message on 2026-10-11 asked which definitions and files it is changing, and whether it will produce a local law of the form “dissipation at step `t` on family `F` iff …”. The message expired undelivered because the two sessions run in different permission modes. Until it is answered:
  - this work states dissipation only as `Flow.DissipatesOn es t` at the steps used;
  - it does not touch `Becoming/Dissipation.lean`, `Becoming/Flow.lean` or `Becoming/Resolution.lean`;
  - it does not take up the derivability of the least loss.

  更新（P48 落地时）：消息已送达，熵的会话已答复。它的 R5 `Becoming.Entropy` 只导入 `Becoming.Resolution`，不改任何已有模块，排在落地队列第 8 项；它报告 b(1) 的结果是分解而不是推导（尚未落地）。 / Update (as P48 lands): the message was delivered and the entropy session replied. Its R5 `Becoming.Entropy` imports only `Becoming.Resolution` and changes no existing module; it is item 8 of the landing queue. It reports its result on b(1) as a decomposition, not a derivation (not yet landed).
- **Another session's uncommitted modules.** A worktree under session `858b224e` holds uncommitted modules:
  - `StandingCounting`, `DependenceCounting` and `FiniteBinding`, which overlap P47 and P46;
  - `Sampling`, coarser steps, which bears on the time test of step 4;
  - `Determination`, standing fixed by the exchange and one cross-section.

  P46 and P47 land first, as Ren directed. Where those modules land, step 4 reuses `Sampling` rather than rebuilding it.

  更新（P48 落地时）：P46、P47 已落地；同一会话（“0 axiom completeness”）起草了规律 2，并入 `Becoming.Locality`；它把 `Sampling` 局部化（落地队列第 7 项），并交付了清点 C 组的局部重述（第 5 项，P50）。 / Update (as P48 lands): P46 and P47 have landed; the same session (“0 axiom completeness”) drafted law 2, folded into `Becoming.Locality`; it localized `Sampling` (queue item 7) and delivered the local restatements of the inventory's group C (item 5, P50).
- **P42–P44** of the peer session land before P46 and P47, as agreed.

## 5. 连续时间：范围（AI 的提议，待 Ren）/ Continuous time: scope (AI proposal, awaits Ren)

更新（2026-10-12）：Ren 已决定，连续时间在核心中读作越来越细的离散读法之塔（见 §1.4 (b3)）；下面的范围保留为当时的提议。 / Update (12 October 2026): Ren decided that continuous time is read in the core as a tower of ever finer discrete readings (see section 1.4, b3); the scope below is kept as the proposal it was.

2026-10-11。会话 “0 axiom completeness” 应整合者之请撰写；没有 Lean，没有成果。Ren：“let's finish one first, then another”——先完成更粗的步（`Sampling`，已在 scratch 中验证，待落地），再做连续时间。下面只是范围。

2026-10-11, written by the session “0 axiom completeness” at the integrator's request. There is no Lean and no result. Ren: “let's finish one first, then another”. Coarser steps come first (`Sampling`, verified in scratch, awaiting landing), then continuous time. What follows is scope only.

**中文。**
- **在核心之内能说什么。** 核心只用 Lean 的 prelude，没有实数，所以连续时间在核心里只能读作步的细分：一个细的世界，给定的世界是它在某些时刻的采样。这是 `Sampling` 的反方向。`Sampling` 已证明各局部条件从细步组合到粗步（平衡在每个关系项每步只列一次时，耗散，封闭恰好如此，耗散地运行下去只需两端）；`Cancelling` 与 `Averaging` 已证明反方向不自动成立。连续时间就读作一座塔：每一层都是下一层的采样，没有最细的一层。以实数为时间的模型只能放在外围（可用 Mathlib），用对应定理连到核心。选哪一种属于表示，所以是 Ren 的决定（b3 的第二部分）。
- **塔上可以问的问题（待证，都是猜想）。**
  1. 细分总是存在：把每一粗步的全部交换放在它的第一个细步，其余细步什么也不发生。这时所有局部条件都向下传递。所以单是“存在细分”没有内容，要问的是哪些条件在每一个细分中都成立。
  2. 各层的局部条件：条件在第 k+1 层成立，就在第 k 层成立（由 `Sampling` 得）。所以在任意细的层上成立的条件，在每一个更粗的层上都成立。
  3. 与最小差异（b1，Ren 选 A）相互作用：耗散的每一次取用至少失去一个单位。如果连续的交换在越来越细的步上都算作取用，有限时间里的损失就没有上界。一个猜想：在 A 与耗散之下，塔的每一层上改变的步数都以同一个总量为界（单位不随时间细分而变），所以连续时间中有耗散的生成只有有限多个改变事件，没有芝诺式的无穷细分。如果成立，最小差异就把连续时间中的改变定为离散的，这是 b1 与 b3 的连接。
  4. 只有活跃者给予与取用、有界传递依赖于步（`Strobe`、`Delay`）。在塔中它们需要“活动在区间内保持”（`Web.Held`）在每一层成立，或者需要在没有最细层时重新表述。
- **需要 Ren 决定的。** 核心中的塔，还是外围的实数时间（或两者，用对应定理连接）；交换事件按细步计，还是按交换计（这决定第 3 项）。

**English.**
- **What can be said inside the core.** The core uses only Lean's prelude and has no reals. So inside the core, continuous time can only be read as a refinement of the step: a fine world of which the given world is the sampling at some times. This is the converse direction of `Sampling`. `Sampling` proved that the local conditions compose from fine steps to a coarse step:
  - balance, where each relatum is listed once at each step;
  - dissipation;
  - closure, exactly;
  - running down, which needs only the two ends.

  `Cancelling` and `Averaging` proved that the converse does not hold automatically. Continuous time then reads as a tower of worlds, each the sampling of the next, with no finest level. A model with real-valued time would sit in the periphery, which may use Mathlib, joined to the core by correspondence theorems. Which to choose is a matter of the representation, so it is Ren's decision (the second half of b3).
- **Questions on a tower (to prove; all conjectures).**
  1. A refinement always exists: put all of a coarse step's exchange at its first fine step, with nothing at the others. Then every local condition passes down. So mere existence says nothing; the question is which conditions hold in every refinement.
  2. A condition holding at level k+1 holds at level k (by `Sampling`). So a condition holding at arbitrarily fine levels holds at every coarser one.
  3. The interaction with the least difference (b1, where Ren chose A). Every taking under dissipation loses at least a unit. If a continuous exchange counts as a taking at ever finer steps, the loss in finite time has no bound. Conjecture: under A and dissipation, the steps of change at every level of a tower are bounded by the same total standing, since the unit does not change with the step. A dissipating becoming in continuous time would then have only finitely many events of change, with no Zeno-like infinite subdivision. If so, the least difference makes change in continuous time discrete, which links b1 and b3.
  4. Only active relata giving, only active relata taking, and bounded transmission depend on the step (`Strobe`, `Delay`). In a tower they need activity held on the intervals (`Web.Held`) at every level, or a restatement for the case with no finest level.
- **For Ren.**
  - A tower in the core, or real time in the periphery, or both joined by correspondence theorems.
  - Whether events of exchange are counted per fine step or per exchange. This settles question 3.
