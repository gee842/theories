# 可判定性清点 / Decidability inventory (P58)

生成：`DECIDABILITY-INVENTORY.py` 在合并检查器回执 `20261013T090945.451917Z` 所检查的核心上运行 `DECIDABILITY-INVENTORY.lean`（源字节与回执一致；外围工具，导入 Lean 自身的库，核心从不导入它）。每一行由 Lean 读出：绑定的类型是否为可判定族或排中律、陈述是否依赖它、证明是否用到它。Ren 2026-10-11：“i intuitively feel decidability is too dualist”，并以“please”接受把它局部化（[原话](../../../../sources/15-codex-theory-conversations/2026-10-11-decidability-local-imbalance-relatum.md)）。

Generated: `DECIDABILITY-INVENTORY.py` runs `DECIDABILITY-INVENTORY.lean` on the core checked by consolidated receipt `20261013T090945.451917Z`, its source bytes matching the receipt (a periphery tool importing Lean's own library, which the core never does). Lean reads each row: whether a binder's type is a decidability family or an excluded middle, whether the statement depends on it, and whether the proof uses it.

## 总数 / Totals

| 类 / Class | 数 / Count |
|---|---:|
| 陈述依赖它（计数或构造），可判定是该陈述自己的条件 / statements depending on it (counting or construction): decidedness is that statement's own condition | 214 |
| 只在证明中用到 / used only in proofs | 100 |
| 不用到 / unused | 0 |
| 排中律作为假设（边界定理）/ excluded middle as a hypothesis (boundary theorems) | 7 |
| 计数而可判定被证明，不是假设 / counting with decidedness proved, not assumed | 79 |
| 证明可判定的定义与实例 / definitions and instances proving decidedness | 86 |
| 取可判定族的定义（计数的原语）/ definitions taking a decidability family (counting primitives) | 50 |

## 理由 / Reasons

陈述依赖可判定性时，理由由 Lean 读出的、陈述提到的取可判定族的定义给出；只在证明中用到时，理由逐条分类，生成时断言每条都已分类。 / Where a statement depends on decidedness, the reason is given by the decidability-taking definitions its statement mentions, as Lean reads them; where only a proof uses it, each theorem is classified by hand, and generation asserts that every one is.

| 理由 / Reason | 说明 / Meaning | 定理数 / Theorems |
|---|---|---:|
| 计数 / counts | 计数：计数存在恰当所计数者已定（`counts_iff_decided`）/ counts: a count exists exactly where what it counts is decided (`counts_iff_decided`) | 72 |
| 较粗的读法 / coarser reading | 较粗的读法：粗步内每个关系项只列一次，需分辨关系项的相同 / a coarser reading: each relatum listed once within a coarse step, which tells relata apart | 88 |
| 抬高一个条件 / one condition raised | 抬高一个条件：需分辨条件的相同 / one condition raised: tells conditions apart | 8 |
| 移开依存 / dependence moved | 在不被支持之步移开依存：支持已定 / dependence moved at unsupported steps: support decided | 3 |
| 保留的列表 / a kept list | 按规定保留的列表：对其成员已定 / a list kept by a determination: decided of its members | 4 |
| 按否证学习 / learning by refutation | 按否证学习：判定主张是否被否证，以保留假设或选出记录所支持的假设，需分辨值的相同 / learning by refutation: decides whether claims are refuted, to retain a hypothesis or select one borne out by the record, which tells values apart | 25 |
| 首个符合者 / first fitting member | 选出首个符合者：依次判定列表成员是否满足规定 / first fitting member: decides the condition on each listed member in order | 2 |
| 另一个值 / another value | 另一个值：取与给定值不同的值，需分辨值的相同 / another value: a value other than a given one, which tells values apart | 1 |
| 不重复的列表 / a list without repetition | 不重复的列表：成员关系已定 / a list without repetition: membership decided | 7 |
| 逐个条件换入 / mixed in condition by condition | 逐个条件换入另一段历史：需分辨条件的相同 / another history mixed in condition by condition: tells conditions apart | 4 |
| 找出 / finds | 找出一步或一个成员：陈述断言其存在，不给已定时它只是不能被否证 / finds a step or a member: the statement asserts one exists, which without decidedness is only not refuted | 52 |
| 造出列表 / builds a list | 造出列表：普查或不重复的列表由已定的成员造出 / builds a list: a census or a list without repetition, from decided members | 8 |
| 分辨相同 / tells same from different | 分辨相同：证明按两个条件、关系项、值或输入是否相同、或条件是否在家族中分情形 / tells same from different: the proof splits on whether two conditions, relata, values or inputs are the same, or a condition is in a family | 34 |
| 分情形 / splits on a case | 按规定分情形：证明分别用规定成立与不成立的情形 / splits on a determination: the proof uses both its holding and failing cases | 5 |
| 造出指示 / builds an indicator | 造出指示：证明以已定命题的标记（成立为一、不成立为零）作为一个数，例如一个分数 / builds an indicator: the proof uses the mark of a decided proposition (one where it holds, zero where it fails) as a number, such as a score | 1 |

## 陈述依赖可判定性的定理（计数或构造） / Theorems whose statements depend on decidedness (counting or construction)

| 模块 / Module | 定理 / Theorem | 可判定 / Decidability | 理由 / Reason | 另一形式 / Other form |
|---|---|---|---|---|
| Change | `Web.activity_over_stretch` | `(t : Nat) → (f : F) → Decidable (W.active t f)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Change | `excess_mark` | `Decidable p`；`Decidable q` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Change | `fall_mark` | `(t : Nat) → Decidable (p t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Change | `held_over_stretch` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | `Counts.over_stretch`（无前提 / no premise） |
| Change | `keep_pace` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | `CountsAcross.keep_pace`（无前提 / no premise） |
| Change | `mark_cases` | `Decidable p` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Change | `mark_iff` | `Decidable p`；`Decidable q` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Change | `mark_le_one` | `Decidable p` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Change | `mark_pos` | `Decidable p` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Change | `marks_within` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | `Counts.le_length`（无前提 / no premise） |
| Change | `rise_mark` | `(t : Nat) → Decidable (p t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Counterfactual | `mixIn_alike` | `DecidableEq C` | 逐个条件换入 / mixed in condition by condition | 可判定是它自己的条件 / its own condition |
| Counterfactual | `mixIn_either` | `DecidableEq C` | 逐个条件换入 / mixed in condition by condition | 可判定是它自己的条件 / its own condition |
| Counterfactual | `mixIn_listed` | `DecidableEq C` | 逐个条件换入 / mixed in condition by condition | 可判定是它自己的条件 / its own condition |
| Counterfactual | `swap_alike` | `DecidableEq C` | 逐个条件换入 / mixed in condition by condition | 可判定是它自己的条件 / its own condition |
| Counting | `World.binds_arising` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Counting | `World.counts_arising` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Counting | `World.enclosed_binds_counting` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Counting | `World.enclosure_bounds_change` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Counting | `World.finite_binding_census` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Counting | `World.taking_binds_counting` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Decidedness | `ceasings_counts` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Decidedness | `comings_counts` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Decidedness | `counts_total` | `(a : α) → Decidable (q a)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Decidedness | `indicates_mark` | `Decidable p` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Dissipation | `adjoin_spec` | `DecidableEq α` | 不重复的列表 / a list without repetition | 可判定是它自己的条件 / its own condition |
| Dissipation | `insertNew_spec` | `Decidable (a ∈ l)` | 不重复的列表 / a list without repetition | 可判定是它自己的条件 / its own condition |
| Identification | `Identification.answer_exceeds_bound` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Identification | `Identification.firstFit_found` | `(a : α) → Decidable (p a)` | 首个符合者 / first fitting member | 可判定是它自己的条件 / its own condition |
| Identification | `Identification.firstFit_sound` | `(a : α) → Decidable (p a)` | 首个符合者 / first fitting member | 可判定是它自己的条件 / its own condition |
| Identification | `Identification.held_learner_rests` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Identification | `Identification.knowing_holds` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Identification | `Identification.knowing_right` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Identification | `Identification.learner_rests` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Identification | `Identification.rests_of_lasso` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Identity | `Web.Census.balanceFrom` | `(t : Nat) → (f : F) → Decidable (W.Continues R t f)`；`(t : Nat) → (f : F) → Decidable (W.active t f)`；`(t : Nat) → (g : F) → Decidable (W.Continued R t g)`；`(t : Nat) → (g f : F) → Decidable (R t g f)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Identity | `Web.Census.balanceFrom_at` | `(t : Nat) → (f : F) → Decidable (W.Continues R t f)`；`(t : Nat) → (f : F) → Decidable (W.active t f)`；`(t : Nat) → (g : F) → Decidable (W.Continued R t g)`；`(t : Nat) → (g f : F) → Decidable (R t g f)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Identity | `Web.Census.balanceFrom_eq` | `(t : Nat) → (f : F) → Decidable (W.Continues R t f)`；`(t : Nat) → (f : F) → Decidable (W.active t f)`；`(t : Nat) → (g : F) → Decidable (W.Continued R t g)`；`(t : Nat) → (g f : F) → Decidable (R t g f)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Identity | `Web.Census.balanceFrom_eq_at` | `(t : Nat) → (f : F) → Decidable (W.Continues R t f)`；`(t : Nat) → (f : F) → Decidable (W.active t f)`；`(t : Nat) → (g : F) → Decidable (W.Continued R t g)`；`(t : Nat) → (g f : F) → Decidable (R t g f)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.diagonal_not_lasso` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.held_learner_bounded` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.held_rest_unrefuted` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.index_kept` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.index_le_of_holds` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.index_le_succ` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.index_mono` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.index_mono_le` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.index_refuted` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.index_succ_le` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.index_unbounded` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.lasso_learner_bounded` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.lasso_of_rest` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.learner_through_record` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.merged_bound` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.merged_unrested` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.refutations_not_recurring` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.refuted_before` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.rest_unrefuted` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Learning | `Learning.swapTo_moves` | `DecidableEq O` | 另一个值 / another value | 可判定是它自己的条件 / its own condition |
| Listing | `Flow.BalancesOn.sample_byOccurrence` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Listing | `Listed.of_listing` | `(t : Nat) → (a b : α) → a ∈ l t → b ∈ l t → Decidable (a = b)` | 不重复的列表 / a list without repetition | 可判定是它自己的条件 / its own condition |
| Listing | `keepFresh_spec` | `Decidable (a ∈ l)` | 不重复的列表 / a list without repetition | 可判定是它自己的条件 / its own condition |
| Listing | `listOnce_listsOnce` | `(a b : α) → a ∈ l → b ∈ l → Decidable (a = b)` | 不重复的列表 / a list without repetition | 可判定是它自己的条件 / its own condition |
| Locality | `ceasing_needs_arising` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Locality | `cohort_closes_iff` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_idle_balancesOn` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_idle_closedAt` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_idle_dissipatesOn` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_idle_enclosed` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_idle_give` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_idle_not_descends` | `DecidableEq X` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_idle_present` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_idle_runsDownOn` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_idle_take` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_idle_takers` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_moves_acting_iff` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_moves_balancesOn_iff` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_moves_closedAt_iff` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_moves_descends_iff` | `DecidableEq X` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_moves_dissipatesOn_iff` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_moves_give` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_moves_given` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_moves_mem` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_moves_runsDownOn_iff` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_moves_take` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_moves_taken` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_moves_taking_iff` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.sample_not_more` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.stutter_acting_iff` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.stutter_balances_iff` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.stutter_dissipative_iff` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.stutter_given` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.stutter_taken` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.stutter_taking_iff` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Flow.stutter_transmitsWithin_iff` | `DecidableEq X` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `Reorders.counts` | `(n : Nat) → (x : X) → Decidable (W'.active n x)`；`(n : Nat) → (x : X) → Decidable (W.active n x)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Order | `World.commute_counts` | `(n : Nat) → (x : (w.commute t side).Relatum) → Decidable ((w.commute t side).web.active n x)`；`(n : Nat) → (x : w.Relatum) → Decidable (w.web.active n x)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Order | `World.stutter_arisingRecurs_iff` | `DecidableEq w.Relatum` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `World.stutter_ceasingRecurs_iff` | `DecidableEq w.Relatum` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `World.stutter_change_recurs_iff` | `DecidableEq w.Relatum` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `World.stutter_counted` | `DecidableEq w.Relatum` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `World.stutter_counted_of_section` | `DecidableEq w.Relatum` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `World.stutter_premises_iff` | `DecidableEq w.Relatum` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Order | `World.withoutIdle_counts` | `(n : Nat) → (x : v.Relatum) → Decidable (v.web.active n x)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Order | `ceasings_moved` | `(a : α) → (n : Nat) → Decidable (p a n)`；`(a : α) → (n : Nat) → Decidable (p' a n)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Order | `ceasings_of_iff` | `(a : α) → (n : Nat) → Decidable (p a n)`；`(a : α) → (n : Nat) → Decidable (q a n)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Order | `comings_moved` | `(a : α) → (n : Nat) → Decidable (p a n)`；`(a : α) → (n : Nat) → Decidable (p' a n)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Order | `comings_of_iff` | `(a : α) → (n : Nat) → Decidable (p a n)`；`(a : α) → (n : Nat) → Decidable (q a n)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Order | `stutter_ceasings` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Order | `stutter_comings` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `Listed.across` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | `Counts.listed_across`（无前提 / no premise） |
| Population | `Listed.across_at` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | `Counts.listed_across`（无前提 / no premise） |
| Population | `Listed.ceasing_iff_shortfall` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `Listed.ceasing_iff_shortfall_from` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `Listed.ceasing_of_outpacing` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `Listed.ceasings_within` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `Listed.coming_iff_excess` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `Listed.coming_iff_excess_from` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `Listed.comings_within` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `Listed.keeps` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `Listed.keeps_at` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `Listed.over_stretch` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | `Counts.listed_over_stretch`（无前提 / no premise） |
| Population | `Listed.over_stretch_on` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | `Counts.listed_over_stretch`（无前提 / no premise） |
| Population | `Listed.tally` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `Web.Census.over_stretch` | `(t : Nat) → (f : F) → Decidable (W.active t f)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `Web.Census.over_stretch_on` | `(t : Nat) → (f : F) → Decidable (W.active t f)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `Web.DependenceCensus.over_stretch` | `(t : Nat) → (g : F) → (c : C) → Decidable (W.requires t g c)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `Web.DependenceCensus.over_stretch_on` | `(t : Nat) → (g : F) → (c : C) → Decidable (W.requires t g c)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `mark_add_not` | `Decidable q`；`Decidable r` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `mark_le_total` | `(a : α) → Decidable (q a)`；`Decidable P` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `mark_one` | `Decidable p` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `mark_turn` | `Decidable p`；`Decidable q` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `mark_zero` | `Decidable p` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `marks_le_of_sub` | `(a : α) → Decidable (q a)`；`(a : α) → Decidable (r a)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Population | `total_le_mark` | `(a : α) → Decidable (q a)`；`Decidable P` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Premises | `World.keep_lists` | `(x : w.Relatum) → Decidable (w.web.active t x)` | 保留的列表 / a kept list | 可判定是它自己的条件 / its own condition |
| Premises | `keep_distinct` | `(a : α) → Decidable (p a)` | 保留的列表 / a kept list | 可判定是它自己的条件 / its own condition |
| Premises | `listed_of_ever` | `(a : α) → (t : Nat) → Decidable (p a t)` | 保留的列表 / a kept list | 可判定是它自己的条件 / its own condition |
| Premises | `mem_keep` | `(a : α) → Decidable (p a)` | 保留的列表 / a kept list | 可判定是它自己的条件 / its own condition |
| Reserve | `Web.Carries.lasts` | `(t : Nat) → Decidable (W.active t f)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Reserve | `Web.Carries.lasts_within` | `(t : Nat) → Decidable (W.active t f)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Reserve | `Web.Carries.step` | `Decidable (W.active t f)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Reserve | `Web.CarriesAcross.step` | `Decidable (W.active t f)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Reserve | `Web.lasts_on` | `(t : Nat) → Decidable (W.active t f)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Reserve | `Web.redirect_dependent` | `(t : Nat) → (f : F) → Decidable (W.Supported t f)` | 移开依存 / dependence moved | 可判定是它自己的条件 / its own condition |
| Reserve | `Web.redirect_same` | `(t : Nat) → (f : F) → Decidable (W.Supported t f)` | 移开依存 / dependence moved | 可判定是它自己的条件 / its own condition |
| Reserve | `Web.redirect_supported_at` | `(t : Nat) → (f : F) → Decidable (W.Supported t f)` | 移开依存 / dependence moved | 可判定是它自己的条件 / its own condition |
| Resolution | `Web.CarriesAt.lasts` | `(t : Nat) → Decidable (W.active t f)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Resolution | `Web.CarriesIn.lasts_unrefined` | `(t : Nat) → Decidable (W.active t f)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Runaway | `Flow.BalancesOn.raise` | `DecidableEq C` | 抬高一个条件 / one condition raised | 可判定是它自己的条件 / its own condition |
| Runaway | `Web.Dependent.raise` | `DecidableEq C` | 抬高一个条件 / one condition raised | 可判定是它自己的条件 / its own condition |
| Runaway | `Web.Supported.raise` | `DecidableEq C` | 抬高一个条件 / one condition raised | 可判定是它自己的条件 / its own condition |
| Runaway | `Web.break_not_bounded` | `DecidableEq C` | 抬高一个条件 / one condition raised | 可判定是它自己的条件 / its own condition |
| Runaway | `Web.le_raise` | `DecidableEq C` | 抬高一个条件 / one condition raised | 可判定是它自己的条件 / its own condition |
| Runaway | `Web.observed_raise_registers` | `DecidableEq C` | 抬高一个条件 / one condition raised | 可判定是它自己的条件 / its own condition |
| Runaway | `Web.raise_other` | `DecidableEq C` | 抬高一个条件 / one condition raised | 可判定是它自己的条件 / its own condition |
| Runaway | `Web.registersAlike_raise` | `DecidableEq C` | 抬高一个条件 / one condition raised | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.BalancesOn.sample` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.DissipatesOn.sample` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.RunsDownOn.sample` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.RunsDownOn.sample_of_fine` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.gateBy_dissipates` | `Decidable p` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.pos_of_gated` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.sample_acting` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.sample_acting_on` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.sample_balances` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.sample_closed` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.sample_closedAt_iff` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.sample_dissipative` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.sample_give_total` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.sample_given` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.sample_given_on` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.sample_once` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.sample_take_total` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.sample_taken` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.sample_taken_on` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.sample_taking` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.sample_taking_on` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `Flow.unionPresent_spec` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `World.sample_acting` | `DecidableEq w.Relatum` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `World.sample_arisingRecurs` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)`；`DecidableEq w.Relatum` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `World.sample_balanced` | `DecidableEq w.Relatum` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `World.sample_ceasingRecurs` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)`；`DecidableEq w.Relatum` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `World.sample_counted` | `DecidableEq w.Relatum` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `World.sample_dependent` | `DecidableEq w.Relatum` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `World.sample_dissipative` | `DecidableEq w.Relatum` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `World.sample_embodied` | `DecidableEq w.Relatum` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `World.sample_finite` | `DecidableEq w.Relatum` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `World.sample_rests` | `DecidableEq w.Relatum` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `World.sample_survives` | `DecidableEq w.Relatum` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `World.sample_taking` | `DecidableEq w.Relatum` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `gateBy_of` | `Decidable p` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `gateBy_of_not` | `Decidable p` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `gateBy_zero` | `Decidable p` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `gate_mem` | `DecidableEq α` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `mem_adjoin` | `DecidableEq α` | 不重复的列表 / a list without repetition | 可判定是它自己的条件 / its own condition |
| Sampling | `mem_insertNew` | `Decidable (a ∈ l)` | 不重复的列表 / a list without repetition | 可判定是它自己的条件 / its own condition |
| Sampling | `mem_of_gateBy_pos` | `Decidable p` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `mem_of_gate_pos` | `DecidableEq α` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `total_gate` | `DecidableEq α` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Sampling | `total_gateBy` | `Decidable p` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Standing | `World.Embodied.standsObey_iff` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Standing | `World.Embodied.tally_of_stands` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Standing | `ceasings_congr` | `(a : α) → (t : Nat) → Decidable (p a t)`；`(a : α) → (t : Nat) → Decidable (q a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Standing | `comings_congr` | `(a : α) → (t : Nat) → Decidable (p a t)`；`(a : α) → (t : Nat) → Decidable (q a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Tower | `Tower.balances_coarser` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Tower | `Tower.changes_within` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Tower | `Tower.dissipative_coarser` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Tower | `Tower.flow_sample` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Tower | `Tower.level_zero` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Tower | `Tower.reads_strict` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Tower | `Tower.strict` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Tower | `Tower.web_sample` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
| Tower | `Tower.web_zero` | `DecidableEq F` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |

## 只在证明中用到可判定性的定理 / Theorems using decidability only in proofs

| 模块 / Module | 定理 / Theorem | 可判定 / Decidability | 理由 / Reason | 另一形式 / Other form |
|---|---|---|---|---|
| Attraction | `Law.lossless_iff_none_drawn` | `DecidableEq S` | 分辨相同 / tells same from different | `Law.Lossless.not_drawn`、`Law.none_drawn_merges_nothing`（不判定 / no decision, P67） |
| Attraction | `Law.none_drawn_lossless` | `DecidableEq S` | 分辨相同 / tells same from different | `Law.none_drawn_merges_nothing`（不判定 / no decision, P67） |
| Change | `Web.arising_recurs_iff` | `(t : Nat) → (f : F) → Decidable (W.active t f)` | 找出 / finds | 同上 / as for `coming_recurs_iff` |
| Change | `Web.unceasing_iff` | `(t : Nat) → (f : F) → Decidable (W.active t f)` | 找出 / finds | `Web.unceasing_iff_decided`（从某步起已定 / decided from some step on） |
| Change | `Web.unceasing_iff_covering` | `(t : Nat) → (f : F) → Decidable (W.active t f)` | 找出 / finds | — |
| Change | `coming_recurs_iff` | `(a : α) → (t : Nat) → Decidable (p a t)` | 找出 / finds | `Recurs.ceasing_not_stopping`、`Recurs.coming_not_stopping`（无前提 / no premise）；`coming_recurs_iff_decided`（从某步起已定 / decided from some step on） |
| Change | `persists` | `(t : Nat) → Decidable (p t)` | 分情形 / splits on a case | `stays_failing`（不成立的持续，不判定 / failing persists, no decision）；`persists_of_em` 示其需要 / shows the need |
| Continuation | `Flow.fed_from_beyond` | `DecidableEq C` | 分辨相同 / tells same from different | — |
| Continuation | `Flow.fed_from_beyond_from` | `DecidableEq C` | 分辨相同 / tells same from different | — |
| Continuation | `Flow.fed_of_not_inward` | `DecidableEq C` | 分辨相同 / tells same from different | — |
| Continuation | `Flow.inward_iff_not_fed` | `DecidableEq C` | 分辨相同 / tells same from different | — |
| Continuation | `Flow.inward_of_not_fed` | `DecidableEq C` | 分辨相同 / tells same from different | — |
| Continuation | `Flow.rising_fed_from_beyond` | `DecidableEq C` | 分辨相同 / tells same from different | — |
| Continuation | `Flow.rising_fed_from_beyond_from` | `DecidableEq C` | 分辨相同 / tells same from different | — |
| Continuation | `Web.generation_fed_from_beyond` | `DecidableEq X` | 分辨相同 / tells same from different | — |
| Counterfactual | `ExchangeLaw.Nonanticipating.through_of_observed` | `DecidableEq C` | 分辨相同 / tells same from different | `ExchangeLaw.Nonanticipating.through_all`（不判定 / no decision, P80）；逆向 `ExchangeLaw.Through.registers_of_sensitive`（不判定 / the converse, no decision） |
| Counterfactual | `ExchangeLaw.Nonanticipating.through_sensitive` | `DecidableEq C` | 分辨相同 / tells same from different | `ExchangeLaw.Nonanticipating.through_all`（不判定 / no decision, P80）；逆向 `ExchangeLaw.Through.registers_of_sensitive`（不判定 / the converse, no decision） |
| Counterfactual | `alike_of_sensitive_agree` | `DecidableEq C` | 分辨相同 / tells same from different | `ExchangeLaw.Nonanticipating.through_all`（经识一切，不判定 / through registering everything, no decision, P80） |
| Counterfactual | `comparison_through_sensitivity` | `DecidableEq C` | 分辨相同 / tells same from different | `comparison_of_courses`（经律所经的识，不判定 / through a registration the law reads through, no decision, P80） |
| Decidedness | `World.arising_iff_ceasing_of_decidable` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 找出 / finds | — |
| Diagonal | `Diagonal.alike_of_complete` | `(x : B) → Decidable (x = b)` | 分辨相同 / tells same from different | — |
| Diagonal | `Diagonal.complete_iff_alike` | `DecidableEq B` | 分辨相同 / tells same from different | — |
| Dissipation | `Flow.Enclosed.around` | `DecidableEq C` | 造出列表 / builds a list | `Flow.Enclosed.around_not_not`（不判定 / no decision） |
| Feedback | `Flow.Balances.adds_iff_exceeds_of_decidable` | `(t : Nat) → (g : F) → Decidable (sig p t g)` | 分情形 / splits on a case | — |
| Identification | `Identification.bounded_induction` | `DecidableEq O` | 分辨相同 / tells same from different | — |
| Identification | `Identification.fits_of_unrefuted` | `DecidableEq O` | 分辨相同 / tells same from different | — |
| Identification | `Identification.unrefuted_persists` | `DecidableEq O` | 分辨相同 / tells same from different | — |
| Identity | `Flow.More.unceasingFrom` | `(t : Nat) → (f : F) → Decidable (W.Continues R t f)` | 找出 / finds | — |
| Identity | `Flow.More.unceasing_reidentified` | `(t : Nat) → (f : F) → Decidable (W.active t f)` | 找出 / finds | — |
| Identity | `Flow.More.unceasing_reidentified_covering` | `(s : Nat) → (f : F) → S ≤ s → Decidable (W.active s f)` | 找出 / finds | — |
| Identity | `Web.Census.arisingFrom_of_ceasingFrom` | `(t : Nat) → (f : F) → Decidable (W.Continues R t f)`；`(t : Nat) → (f : F) → Decidable (W.active t f)`；`(t : Nat) → (g : F) → Decidable (W.Continued R t g)`；`(t : Nat) → (g f : F) → Decidable (R t g f)` | 找出 / finds | — |
| Identity | `Web.Census.arisingFrom_of_ceasingFrom_from` | `(t : Nat) → (f : F) → Decidable (W.Continues R t f)`；`(t : Nat) → (f : F) → Decidable (W.active t f)`；`(t : Nat) → (g : F) → Decidable (W.Continued R t g)`；`(t : Nat) → (g f : F) → Decidable (R t g f)` | 找出 / finds | — |
| Identity | `Web.Census.ceasingFrom_of_arisingFrom` | `(t : Nat) → (f : F) → Decidable (W.Continues R t f)`；`(t : Nat) → (f : F) → Decidable (W.active t f)`；`(t : Nat) → (g : F) → Decidable (W.Continued R t g)`；`(t : Nat) → (g f : F) → Decidable (R t g f)` | 找出 / finds | — |
| Identity | `Web.Census.ceasingFrom_of_arisingFrom_from` | `(t : Nat) → (f : F) → Decidable (W.Continues R t f)`；`(t : Nat) → (f : F) → Decidable (W.active t f)`；`(t : Nat) → (g : F) → Decidable (W.Continued R t g)`；`(t : Nat) → (g f : F) → Decidable (R t g f)` | 找出 / finds | — |
| Identity | `Web.arisesFrom_of_more` | `(f : F) → Decidable (W.Continues R t f)` | 找出 / finds | — |
| Identity | `Web.unceasingFrom_of_growth` | `(t : Nat) → (f : F) → Decidable (W.Continues R t f)` | 找出 / finds | — |
| Identity | `forces_iff_noSplit` | `DecidableEq F` | 分辨相同 / tells same from different | — |
| Learning | `Learning.claim_refuted_on_one` | `DecidableEq O` | 分辨相同 / tells same from different | `Learning.no_record_fixes_next`（无前提：主张不在两者上都对 / no premise: the claim is not right on both, P73） |
| Learning | `Learning.determines_lumped_iff` | `DecidableEq K` | 找出 / finds | `Learning.lumped_determines`（无前提的一个方向 / one direction, no premise, P73） |
| Learning | `Learning.eq_of_not_refuted` | `DecidableEq O` | 分辨相同 / tells same from different | — |
| Learning | `Learning.every_determines_nothing` | `DecidableEq I` | 分辨相同 / tells same from different | — |
| Learning | `Learning.every_free` | `DecidableEq I` | 分辨相同 / tells same from different | — |
| Listing | `Web.arising_of_ceasing_listing` | `(t : Nat) → (a b : F) → a ∈ l t → b ∈ l t → Decidable (a = b)`；`(t : Nat) → (f : F) → Decidable (W.active t f)` | 找出 / finds | `Web.arising_of_ceasing`（给定普查；此处还用 `listOnce` 造普查 / a supplied census; here `listOnce` also constructs it, P77） |
| Locality | `Covers.coming_from_of_ceasing` | `(a : α) → (t : Nat) → Decidable (p a t)` | 找出 / finds | `Covers.not_not_coming_from`（无前提 / no premise, P48） |
| Locality | `Covers.within` | `(a : α) → (t : Nat) → Decidable (p a t)` | 找出 / finds | — |
| Locality | `coming_of_ceasing_covered` | `(a : α) → (t : Nat) → Decidable (p a t)` | 找出 / finds | `Covers.not_not_coming_from`、`Covers.ceasing_not_recurring`（无前提 / no premise, P48） |
| Openness | `Flow.Enclosed.aroundStanding` | `DecidableEq C` | 造出列表 / builds a list | `Flow.Enclosed.aroundStanding_not_not`（不判定 / no decision） |
| Openness | `Listed.few_of_quiet` | `(a : α) → (t : Nat) → Decidable (p a t)` | 找出 / finds | `Listed.few_of_stop_unrefuted`（不判定 / no decision, P58） |
| Openness | `World.CountedBy.arising_iff_ceasing` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 找出 / finds | — |
| Openness | `World.CountedWithin.arising_iff_ceasing` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 找出 / finds | — |
| Openness | `World.Finite.arising_iff_ceasing` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 找出 / finds | — |
| Openness | `World.Finite.countedWithin` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 造出列表 / builds a list | — |
| Openness | `World.arising_of_ceasing` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 找出 / finds | — |
| Openness | `World.few_active` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 找出 / finds | `Listed.few_of_stop_unrefuted`、`World.rest_few`（不判定 / no decision, P58） |
| Openness | `comes_after` | `(t : Nat) → Decidable (p t)` | 找出 / finds | `comes_after_unrefuted`（不判定，那一步不能被否证 / no decision, the step unrefuted） |
| Population | `Flow.More.unceasing` | `(t : Nat) → (f : F) → Decidable (W.active t f)` | 找出 / finds | — |
| Population | `Flow.More.unceasing_covering` | `(s : Nat) → (f : F) → S ≤ s → Decidable (W.active s f)` | 找出 / finds | — |
| Population | `Listed.ceasing_of_coming` | `(a : α) → (t : Nat) → Decidable (p a t)` | 找出 / finds | — |
| Population | `Listed.ceasing_of_returning` | `(a : α) → (t : Nat) → Decidable (p a t)` | 找出 / finds | — |
| Population | `Listed.coming_iff_ceasing` | `(a : α) → (t : Nat) → Decidable (p a t)` | 找出 / finds | — |
| Population | `Listed.coming_of_ceasing` | `(a : α) → (t : Nat) → Decidable (p a t)` | 找出 / finds | — |
| Population | `Web.DependenceCensus.forming_iff_dissolving` | `(t : Nat) → (g : F) → (c : C) → Decidable (W.requires t g c)` | 找出 / finds | — |
| Population | `Web.DependenceCensus.forming_of_dissolving` | `(t : Nat) → (g : F) → (c : C) → Decidable (W.requires t g c)` | 找出 / finds | — |
| Population | `Web.arises_of_more` | `(t : Nat) → (f : F) → Decidable (W.active t f)` | 找出 / finds | — |
| Population | `Web.arising_of_ceasing` | `(t : Nat) → (f : F) → Decidable (W.active t f)` | 找出 / finds | — |
| Population | `Web.ceasing_of_arising` | `(t : Nat) → (f : F) → Decidable (W.active t f)` | 找出 / finds | — |
| Population | `Web.unceasing_iff_bounded` | `(t : Nat) → (f : F) → Decidable (W.active t f)` | 找出 / finds | — |
| Population | `Web.unceasing_of_growth` | `(t : Nat) → (f : F) → Decidable (W.active t f)` | 找出 / finds | — |
| Population | `came_between` | `(t : Nat) → Decidable (q t)` | 找出 / finds | — |
| Population | `came_between_from` | `(s : Nat) → S ≤ s → Decidable (q s)` | 找出 / finds | — |
| Population | `search` | `(a : α) → Decidable (p a)` | 找出 / finds | — |
| Premises | `World.Finite.counted` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 造出列表 / builds a list | — |
| Premises | `World.counted_of_ever` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 造出列表 / builds a list | — |
| Response | `Flow.Balances.comparison_within_response_of_decidable` | `(g : F) → Decidable (L.WithinResponse L' W obs part g)` | 分辨相同 / tells same from different | `Flow.Balances.comparison_within_response`（覆盖不被否证在回应所及之内者，不判定 / covering what is not refuted to be within the reach, no decision, P65） |
| Runaway | `Flow.exchangeFollows_of_policy` | `DecidableEq F` | 分辨相同 / tells same from different | — |
| Runaway | `Flow.policy_keeps_difference` | `DecidableEq C`；`DecidableEq F` | 分辨相同 / tells same from different | — |
| Runaway | `Flow.policy_uses_after_failure` | `DecidableEq F` | 分辨相同 / tells same from different | — |
| Sampling | `Flow.sample_ceasesToStand_iff` | `DecidableEq F` | 造出列表 / builds a list | — |
| Sampling | `Flow.sample_changes_iff` | `DecidableEq F` | 造出列表 / builds a list | — |
| Sampling | `Flow.sample_comesToStand_iff` | `DecidableEq F` | 造出列表 / builds a list | — |
| Sampling | `Web.sample_arises` | `(t : Nat) → (x : F) → Decidable (W.active t x)` | 找出 / finds | — |
| Sampling | `Web.sample_ceases` | `(t : Nat) → (x : F) → Decidable (W.active t x)` | 找出 / finds | — |
| Sampling | `Web.sample_ceasing` | `(t : Nat) → (x : F) → Decidable (W.active t x)` | 找出 / finds | — |
| Sampling | `Web.sample_unceasing` | `(t : Nat) → (x : F) → Decidable (W.active t x)` | 找出 / finds | — |
| Sampling | `arises_within` | `(n : Nat) → Decidable (p n)` | 找出 / finds | — |
| Sampling | `ceases_within` | `(n : Nat) → Decidable (p n)` | 找出 / finds | — |
| Selection | `Web.scores_alike_iff` | `(m : Nat → C → Nat) → Decidable (W.RegistersAlikeUpTo obs g l m t)` | 造出指示 / builds an indicator | `Web.selects_alike_iff`（选择而非分数，不判定 / selections rather than scores, no decision, P64） |
| Space | `World.arising_iff_ceasing` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 找出 / finds | `World.ceasing_not_stopping`、`World.arising_not_stopping`（无前提 / no premise）；`World.arising_iff_ceasing_decided`（从某步起已定 / decided from some step on） |
| Space | `World.arising_iff_ceasing_covering` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 找出 / finds | — |
| Standpoints | `Flow.boundary_crossed` | `DecidableEq X` | 分辨相同 / tells same from different | — |
| Standpoints | `Flow.region_not_a_cut` | `DecidableEq X` | 分辨相同 / tells same from different | — |
| Standpoints | `Valuation.significant_iff_reached` | `(c : C) → Decidable (∃ p, V.own p c)` | 分情形 / splits on a case | — |
| Substitution | `ceasing_step` | `DecidablePred p` | 找出 / finds | — |
| Testing | `Flow.subthreshold_alike` | `DecidableEq C` | 分辨相同 / tells same from different | — |
| Testing | `Flow.subthreshold_alike_always` | `DecidableEq C` | 分辨相同 / tells same from different | — |
| Testing | `Web.alike_of_threshold` | `DecidableEq C` | 分辨相同 / tells same from different | — |
| Testing | `Web.tail_unrefuted` | `DecidableEq C` | 分辨相同 / tells same from different | — |
| Transmission | `Flow.transmitsWithin_iff_split` | `(t : Nat) → (x : X) → Decidable (W.requires t x c)` | 分情形 / splits on a case | — |
| Transmission | `Web.inheritsAt_of_split` | `Decidable (W.requires t x c)` | 分情形 / splits on a case | `Web.inheritsAt_not_not`（不判定时继承不能被否证 / inheritance is unrefuted without the decision, P84） |
| Unfolding | `Frame.claims_recur_iff` | `(c : C) → (t : Nat) → Decidable (F.realized (r.state t) c)` | 找出 / finds | — |

## 排中律作为假设 / Excluded middle as a hypothesis

这些是边界定理：它们表明排中律给出什么，配合 `World.law_iff_em`、`World.law_decides`、`World.lpo_of_finite_ends`、`Listed.lpo_of_few`、`Web.lpo_of_ending`、`ChangeBound.lpo_of_ends`，表明命名一步或对每个世界要求复现的形式需要可判定性。 / These are boundary theorems: they show what excluded middle gives, and with `World.law_iff_em`, `World.law_decides`, `World.lpo_of_finite_ends`, `Listed.lpo_of_few`, `Web.lpo_of_ending`, `ChangeBound.lpo_of_ends`, that the forms naming a step or asking recurrence of every world need decidedness.

- Change: `exists_not_of_em`
- Change: `persists_of_em`
- Reserve: `Web.Carries.chain_ends_of_em`
- Reserve: `Web.chain_ends_of_em_from`
- Space: `World.law_of_em`
- Space: `quiet_of_once`
- Transmission: `split_of_em`

## 计数而可判定被证明 / Counting with decidedness proved

这些定理的陈述计数，但不以可判定为假设：可判定由见证世界或体现证明（例如 `Embodied.decided`）。按模块计： / These theorems count in their statements without taking decidedness as a hypothesis: it is proved for witness worlds or from embodiment (for example `Embodied.decided`). By module:

- Counting: 35
- Identification: 1
- Learning: 2
- Locality: 1
- Openness: 2
- Order: 1
- Population: 14
- Reserve: 2
- Resolution: 3
- Runaway: 1
- Sampling: 6
- Standing: 11

## 计数的原语 / Counting primitives

| 模块 / Module | 定义 / Definition | 可判定 / Decidability |
|---|---|---|
| Change | `Web.instDecidableArises` | `(t : Nat) → (f : F) → Decidable (W.active t f)` |
| Change | `Web.instDecidableCeases` | `(t : Nat) → (f : F) → Decidable (W.active t f)` |
| Change | `ceasings` | `(a : α) → (t : Nat) → Decidable (p a t)` |
| Change | `comings` | `(a : α) → (t : Nat) → Decidable (p a t)` |
| Change | `instDecidableCeasesToBe` | `(t : Nat) → Decidable (p t)` |
| Change | `instDecidableComesToBe` | `(t : Nat) → Decidable (p t)` |
| Change | `mark` | `Decidable p` |
| Counterfactual | `mixIn` | `DecidableEq C` |
| Counting | `World.CountsObey` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` |
| Counting | `World.saturated_decided` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` |
| Dissipation | `adjoin` | `DecidableEq α` |
| Dissipation | `decideMem` | `DecidableEq α` |
| Dissipation | `insertNew` | `Decidable (a ∈ l)` |
| Identification | `Identification.decBorneOut` | `DecidableEq O` |
| Identification | `Identification.decFits` | `DecidableEq O` |
| Identification | `Identification.firstFit` | `(a : α) → Decidable (p a)` |
| Identification | `Identification.knowing` | `DecidableEq O` |
| Identification | `Law.decideAlike` | `DecidableEq R` |
| Identity | `Web.Census.decideContinued` | `(t : Nat) → (g f : F) → Decidable (R t g f)` |
| Identity | `Web.Census.decideContinues` | `(t : Nat) → (g f : F) → Decidable (R t g f)` |
| Identity | `Web.instDecidableArisesFrom` | `(t : Nat) → (f : F) → Decidable (W.Continues R t f)`；`(t : Nat) → (f : F) → Decidable (W.active t f)` |
| Identity | `Web.instDecidableCeasesFrom` | `(t : Nat) → (f : F) → Decidable (W.active t f)`；`(t : Nat) → (g : F) → Decidable (W.Continued R t g)` |
| Learning | `Learning.decRefuted` | `DecidableEq O` |
| Learning | `Learning.decRefutedAt` | `DecidableEq O` |
| Learning | `Learning.decideSeen` | `DecidableEq K` |
| Learning | `Learning.index` | `DecidableEq O` |
| Learning | `Learning.indexOn` | `DecidableEq O` |
| Learning | `Learning.learner` | `DecidableEq O` |
| Learning | `Learning.swapTo` | `DecidableEq O` |
| Listing | `decideIn` | `(b : α) → b ∈ l → Decidable (a = b)` |
| Listing | `keepFresh` | `Decidable P` |
| Listing | `listOnce` | `(a b : α) → a ∈ l → b ∈ l → Decidable (a = b)` |
| Order | `Web.commuteDecided` | `(n : Nat) → (f : F) → Decidable (W.active n f)` |
| Population | `Web.decideDissolves` | `(t : Nat) → (g : F) → (c : C) → Decidable (W.requires t g c)` |
| Population | `Web.decideForms` | `(t : Nat) → (g : F) → (c : C) → Decidable (W.requires t g c)` |
| Population | `decideSome` | `(a : α) → Decidable (p a)` |
| Premises | `keep` | `(a : α) → Decidable (p a)` |
| Reserve | `Web.redirect` | `(t : Nat) → (f : F) → Decidable (W.Supported t f)` |
| Runaway | `Web.raise` | `DecidableEq C` |
| Sampling | `Flow.sample` | `DecidableEq F` |
| Sampling | `Flow.unionPresent` | `DecidableEq F` |
| Sampling | `World.sample` | `DecidableEq w.Relatum` |
| Sampling | `gate` | `DecidableEq α` |
| Sampling | `gateBy` | `Decidable p` |
| Standing | `World.DependsObey` | `(t : Nat) → (f c : w.Relatum) → Decidable (w.web.requires t f c)` |
| Testing | `recordThen` | `DecidableEq C` |
| Tower | `Tower.flow` | `DecidableEq F` |
| Tower | `Tower.reads` | `DecidableEq F` |
| Tower | `Tower.refine` | `DecidableEq F` |
| Tower | `Tower.web` | `DecidableEq F` |

另：一个部分以 `part : F → Bool` 给出，它的切分由类型定下（`Becoming.Admission`、`Becoming.Significance`）；这是比较的参数，不是关于世界的前提。 / Also: a part is given as `part : F → Bool`, its split decided by its type (`Becoming.Admission`, `Becoming.Significance`); it is a parameter of the comparison, not a premise about the world.
