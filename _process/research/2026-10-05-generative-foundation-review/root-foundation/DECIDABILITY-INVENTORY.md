# 可判定性清点 / Decidability inventory (P58)

生成：`DECIDABILITY-INVENTORY.py` 在合并检查器回执 `20261015T153317.850533Z` 所检查的核心上运行 `DECIDABILITY-INVENTORY.lean`（源字节与回执一致；外围工具，导入 Lean 自身的库，核心从不导入它）。每一行由 Lean 读出：绑定的类型是否为可判定族、已判定的命题（对给定的 `p` 有 `p ∨ ¬ p`，如核心的 `Decided p`）或排中律（对约束所涉的每个命题或谓词，完全或受限的形式）、陈述是否依赖它、证明是否用到它。Ren 2026-10-11：“i intuitively feel decidability is too dualist”，并以“please”接受把它局部化（[原话](../../../../sources/15-codex-theory-conversations/2026-10-11-decidability-local-imbalance-relatum.md)）。

Generated: `DECIDABILITY-INVENTORY.py` runs `DECIDABILITY-INVENTORY.lean` on the core checked by consolidated receipt `20261015T153317.850533Z`, its source bytes matching the receipt (a periphery tool importing Lean's own library, which the core never does). Lean reads each row: whether a binder's type is a decidability family, a decided proposition (`p ∨ ¬ p` for a given `p`, such as the core's `Decided p`) or an excluded middle (`p ∨ ¬ p` for every proposition or predicate a binder ranges over, in full or restricted form), whether the statement depends on it, and whether the proof uses it.

## 总数 / Totals

| 类 / Class | 数 / Count |
|---|---:|
| 陈述依赖它（计数或构造），可判定是该陈述自己的条件 / statements depending on it (counting or construction): decidedness is that statement's own condition | 322 |
| 只在证明中用到 / used only in proofs | 186 |
| 不用到 / unused | 0 |
| 排中律或其受限形式作为假设（边界定理）/ excluded middle, in full or restricted form, as a hypothesis (boundary theorems) | 33 |
| 计数而可判定被证明，不是假设 / counting with decidedness proved, not assumed | 87 |
| 证明可判定的定义与实例 / definitions and instances proving decidedness | 131 |
| 取可判定族的定义（计数的原语）/ definitions taking a decidability family (counting primitives) | 89 |

## 理由 / Reasons

陈述依赖可判定性时，理由由 Lean 读出的、陈述提到的取可判定族的定义给出；只在证明中用到时，理由逐条分类，生成时断言每条都已分类。 / Where a statement depends on decidedness, the reason is given by the decidability-taking definitions its statement mentions, as Lean reads them; where only a proof uses it, each theorem is classified by hand, and generation asserts that every one is.

| 理由 / Reason | 说明 / Meaning | 定理数 / Theorems |
|---|---|---:|
| 计数 / counts | 计数：计数存在恰当所计数者已定（`counts_iff_decided`）/ counts: a count exists exactly where what it counts is decided (`counts_iff_decided`) | 77 |
| 较粗的读法 / coarser reading | 较粗的读法：粗步内每个关系项只列一次，需分辨关系项的相同 / a coarser reading: each relatum listed once within a coarse step, which tells relata apart | 88 |
| 抬高一个条件 / one condition raised | 抬高一个条件：需分辨条件的相同 / one condition raised: tells conditions apart | 8 |
| 移开依存 / dependence moved | 在不被支持之步移开依存：支持已定 / dependence moved at unsupported steps: support decided | 3 |
| 保留的列表 / a kept list | 按规定保留的列表：对其成员已定 / a list kept by a determination: decided of its members | 9 |
| 按否证学习 / learning by refutation | 按否证学习：判定主张是否被否证，以保留假设或选出记录所支持的假设，需分辨值的相同 / learning by refutation: decides whether claims are refuted, to retain a hypothesis or select one borne out by the record, which tells values apart | 23 |
| 首个符合者 / first fitting member | 选出首个符合者：依次判定列表成员是否满足规定 / first fitting member: decides the condition on each listed member in order | 10 |
| 另一个值 / another value | 另一个值：取与给定值不同的值，需分辨值的相同 / another value: a value other than a given one, which tells values apart | 1 |
| 不重复的列表 / a list without repetition | 不重复的列表：成员关系已定 / a list without repetition: membership decided | 7 |
| 逐个条件换入 / mixed in condition by condition | 逐个条件换入另一段历史：需分辨条件的相同 / another history mixed in condition by condition: tells conditions apart | 4 |
| 交换两个值 / exchanging two values | 交换两个值：需分辨输入是否为其中任一值 / exchanging two values: decides whether the input is either of the exchanged values | 10 |
| 列表成员判定 / list membership | 列表成员的布尔判定：需逐项分辨值的相同 / boolean list membership: tells values apart at each listed member | 1 |
| 分辨相同 / tells same from different | 分辨相同：证明按两个条件、关系项、值或输入是否相同、或条件是否在家族中分情形 / tells same from different: the proof splits on whether two conditions, relata, values or inputs are the same, or a condition is in a family | 123 |
| 造出指示 / builds an indicator | 造出指示：证明以已定命题的标记（成立为一、不成立为零）作为一个数，例如一个分数 / builds an indicator: the proof uses the mark of a decided proposition (one where it holds, zero where it fails) as a number, such as a score | 14 |
| 分情形 / splits on a case | 按规定分情形：证明分别用规定成立与不成立的情形 / splits on a determination: the proof uses both its holding and failing cases | 25 |
| 守护之步 / a guarded step | 守护之步：每步判定守护是否成立，不成立处停止 / a guarded step: decides the guard at each step and stops where it fails | 10 |
| 找出 / finds | 找出一步或一个成员：陈述断言其存在，不给已定时它只是不能被否证 / finds a step or a member: the statement asserts one exists, which without decidedness is only not refuted | 80 |
| 造出列表 / builds a list | 造出列表：普查或不重复的列表由已定的成员造出 / builds a list: a census or a list without repetition, from decided members | 15 |

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
| Contacts | `Contacts.agree_spot` | `DecidableEq I` | 造出指示 / builds an indicator | 可判定是它自己的条件 / its own condition |
| Contacts | `Contacts.spot_other` | `DecidableEq I` | 造出指示 / builds an indicator | 可判定是它自己的条件 / its own condition |
| Contacts | `Contacts.spot_self` | `DecidableEq I` | 造出指示 / builds an indicator | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.batch_all_iff` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.batch_all_swap` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.built_iff` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.completes_iff` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.copies` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.countOf_append` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.countOf_joinAll_replicate` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.countOf_joinAll_swap` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.countOf_other` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.countOf_remove` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.countOf_remove_other` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.countOf_remove_self` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.countOf_self` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.countOf_setAt` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.defects_beyond` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.defects_break` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.defects_fix` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.defects_self` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.defects_zero_iff` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.exchange_keeps_counts` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.exchange_le` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.inspect_keeps_counts` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.inspect_le` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.inspect_le_iff` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.inspect_matches_iff` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.ite_cases` | `Decidable c` | 分情形 / splits on a case | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.lineage_all_iff` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.pos_of_supplies` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.readStep_extends` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.readSteps_extends` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.readSteps_fixed` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.reading_iff` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.releases_iff` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.scan_le` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.steps_fixed` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.supplied_of_completes` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.supplies_append_iff` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.supplies_cons_iff` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.supplies_nil` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.tick_cons` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.use_lt_iff` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.use_midpoint` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.use_pair` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Copying | `Copying.use_word` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
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
| Coupling | `policyUpto_agrees` | `DecidableEq K` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Coupling | `policyUpto_taken` | `DecidableEq K` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Decidedness | `ceasings_counts` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Decidedness | `comings_counts` | `(a : α) → (t : Nat) → Decidable (p a t)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Decidedness | `counts_total` | `(a : α) → Decidable (q a)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Decidedness | `indicates_mark` | `Decidable p` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Dissipation | `adjoin_spec` | `DecidableEq α` | 不重复的列表 / a list without repetition | 可判定是它自己的条件 / its own condition |
| Dissipation | `insertNew_spec` | `Decidable (a ∈ l)` | 不重复的列表 / a list without repetition | 可判定是它自己的条件 / its own condition |
| Entropy | `mark_mono` | `Decidable p`；`Decidable q` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Identification | `Identification.answer_exceeds_bound` | `DecidableEq O` | 首个符合者 / first fitting member | 可判定是它自己的条件 / its own condition |
| Identification | `Identification.firstFit_found` | `(a : α) → Decidable (p a)` | 首个符合者 / first fitting member | 可判定是它自己的条件 / its own condition |
| Identification | `Identification.firstFit_sound` | `(a : α) → Decidable (p a)` | 首个符合者 / first fitting member | 可判定是它自己的条件 / its own condition |
| Identification | `Identification.held_learner_rests` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Identification | `Identification.learner_rests` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Identification | `Identification.rests_of_lasso` | `DecidableEq O` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
| Identification | `Identification.withBound_exact` | `DecidableEq O` | 首个符合者 / first fitting member | 可判定是它自己的条件 / its own condition |
| Identification | `Identification.withBound_holds` | `DecidableEq O` | 首个符合者 / first fitting member | 可判定是它自己的条件 / its own condition |
| Identity | `Web.Census.balanceFrom` | `(t : Nat) → (f : F) → Decidable (W.Continues R t f)`；`(t : Nat) → (f : F) → Decidable (W.active t f)`；`(t : Nat) → (g : F) → Decidable (W.Continued R t g)`；`(t : Nat) → (g f : F) → Decidable (R t g f)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Identity | `Web.Census.balanceFrom_at` | `(t : Nat) → (f : F) → Decidable (W.Continues R t f)`；`(t : Nat) → (f : F) → Decidable (W.active t f)`；`(t : Nat) → (g : F) → Decidable (W.Continued R t g)`；`(t : Nat) → (g f : F) → Decidable (R t g f)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Identity | `Web.Census.balanceFrom_eq` | `(t : Nat) → (f : F) → Decidable (W.Continues R t f)`；`(t : Nat) → (f : F) → Decidable (W.active t f)`；`(t : Nat) → (g : F) → Decidable (W.Continued R t g)`；`(t : Nat) → (g f : F) → Decidable (R t g f)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Identity | `Web.Census.balanceFrom_eq_at` | `(t : Nat) → (f : F) → Decidable (W.Continues R t f)`；`(t : Nat) → (f : F) → Decidable (W.active t f)`；`(t : Nat) → (g : F) → Decidable (W.Continued R t g)`；`(t : Nat) → (g f : F) → Decidable (R t g f)` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| Lasting | `Lasting.guarded_agrees` | `DecidablePred guard` | 守护之步 / a guarded step | 可判定是它自己的条件 / its own condition |
| Lasting | `Lasting.guarded_none_iff` | `DecidablePred guard` | 守护之步 / a guarded step | 可判定是它自己的条件 / its own condition |
| Lasting | `Lasting.guarded_upto_iff` | `DecidablePred guard` | 守护之步 / a guarded step | 可判定是它自己的条件 / its own condition |
| Lasting | `Lasting.guarded_within` | `DecidablePred guard` | 守护之步 / a guarded step | 可判定是它自己的条件 / its own condition |
| Lasting | `Lasting.hitTime_lowers` | `DecidablePred target` | 首个符合者 / first fitting member | 可判定是它自己的条件 / its own condition |
| Lasting | `Lasting.hitTime_of_reaches` | `DecidablePred target` | 首个符合者 / first fitting member | 可判定是它自己的条件 / its own condition |
| Lasting | `Lasting.hitTime_stable` | `DecidablePred target` | 首个符合者 / first fitting member | 可判定是它自己的条件 / its own condition |
| Lasting | `Lasting.hitTime_succ` | `DecidablePred target` | 首个符合者 / first fitting member | 可判定是它自己的条件 / its own condition |
| Learnable | `Learnable.firstFit_congr` | `(a : α) → Decidable (p a)`；`(a : α) → Decidable (q a)` | 首个符合者 / first fitting member | 可判定是它自己的条件 / its own condition |
| Learnable | `Learnable.rests_through` | `DecidableEq R` | 按否证学习 / learning by refutation | 可判定是它自己的条件 / its own condition |
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
| LossMatching | `Frame.StrictLossMatch.classCount_le` | `DecidableEq K` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| LossMatching | `Frame.distinct_lostOf` | `(c : C) → Decidable (F.realized s c)` | 保留的列表 / a kept list | 可判定是它自己的条件 / its own condition |
| LossMatching | `Frame.lossesListed_lostOf` | `(c : C) → Decidable (F.realized s c)` | 保留的列表 / a kept list | 可判定是它自己的条件 / its own condition |
| LossMatching | `Frame.matching_of_counts` | `DecidableEq C`；`DecidableEq K` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| LossMatching | `Frame.mem_lostOf` | `(c : C) → Decidable (F.realized s c)` | 保留的列表 / a kept list | 可判定是它自己的条件 / its own condition |
| LossMatching | `Frame.strictLossMatch_iff_counts` | `DecidableEq C`；`DecidableEq K` | 计数 / counts | 可判定是它自己的条件 / its own condition |
| LossMatching | `Frame.strictLossMatch_of_counts` | `DecidableEq C`；`DecidableEq K` | 计数 / counts | 可判定是它自己的条件 / its own condition |
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
| OrderNormal | `Footprinted.inList_iff` | `DecidableEq X` | 列表成员判定 / list membership | 可判定是它自己的条件 / its own condition |
| Persistence | `Reidentify.exchangeAfter_across` | `DecidableEq X` | 交换两个值 / exchanging two values | 可判定是它自己的条件 / its own condition |
| Persistence | `Reidentify.exchangeAfter_at` | `DecidableEq X` | 交换两个值 / exchanging two values | 可判定是它自己的条件 / its own condition |
| Persistence | `Reidentify.exchangeAfter_elsewhere` | `DecidableEq X` | 交换两个值 / exchanging two values | 可判定是它自己的条件 / its own condition |
| Persistence | `Reidentify.exchangeAfter_next` | `DecidableEq X` | 交换两个值 / exchanging two values | 可判定是它自己的条件 / its own condition |
| Persistence | `World.exchangeAfter_balanced` | `DecidableEq w.Relatum` | 交换两个值 / exchanging two values | 可判定是它自己的条件 / its own condition |
| Persistence | `transpose_alike` | `DecidableEq X` | 交换两个值 / exchanging two values | 可判定是它自己的条件 / its own condition |
| Persistence | `transpose_left` | `DecidableEq X` | 交换两个值 / exchanging two values | 可判定是它自己的条件 / its own condition |
| Persistence | `transpose_other` | `DecidableEq X` | 交换两个值 / exchanging two values | 可判定是它自己的条件 / its own condition |
| Persistence | `transpose_right` | `DecidableEq X` | 交换两个值 / exchanging two values | 可判定是它自己的条件 / its own condition |
| Persistence | `transpose_transpose` | `DecidableEq X` | 交换两个值 / exchanging two values | 可判定是它自己的条件 / its own condition |
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
| Reading | `Flow.adopt_census` | `(t : Nat) → (f : Option F) → Decidable ((L.withImbalance W).Exchanging t f)` | 保留的列表 / a kept list | 可判定是它自己的条件 / its own condition |
| Reading | `Flow.readOff_census` | `(t : Nat) → (f : F) → Decidable (L.Exchanging t f)` | 保留的列表 / a kept list | 可判定是它自己的条件 / its own condition |
| Readout | `Readout.pick_of` | `Decidable p` | 造出指示 / builds an indicator | 可判定是它自己的条件 / its own condition |
| Readout | `Readout.pick_of_not` | `Decidable p` | 造出指示 / builds an indicator | 可判定是它自己的条件 / its own condition |
| Regrouping | `Web.admits_iff_requiredLevel` | `(t : Nat) → (f : F) → (c : C) → Decidable (W.requires t f c)` | 造出指示 / builds an indicator | 可判定是它自己的条件 / its own condition |
| Regrouping | `Web.admits_requiredLevel` | `(t : Nat) → (f : F) → (c : C) → Decidable (W.requires t f c)` | 造出指示 / builds an indicator | 可判定是它自己的条件 / its own condition |
| Regrouping | `Web.regroup_faithful_iff_requiredLevel` | `(t : Nat) → (f : F) → (c : C) → Decidable (W.requires t f c)` | 造出指示 / builds an indicator | 可判定是它自己的条件 / its own condition |
| Regrouping | `Web.same_admission_iff_requiredLevel` | `(t : Nat) → (f : F) → (c : C) → Decidable (W.requires t f c)` | 造出指示 / builds an indicator | 可判定是它自己的条件 / its own condition |
| RegroupingSelection | `Web.group_keeps_selections_iff_faithful` | `(t : Nat) → (f : F) → (c : C) → Decidable (W.requires t f c)` | 造出指示 / builds an indicator | 可判定是它自己的条件 / its own condition |
| RegroupingSelection | `Web.merged_requirement_loses_selection` | `(t : Nat) → (f : F) → (c : C) → Decidable (W.requires t f c)` | 造出指示 / builds an indicator | 可判定是它自己的条件 / its own condition |
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
| Retrodiction | `Retrodiction.bracket` | `DecidableEq R` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Retrodiction | `Retrodiction.bracket_settles_iff` | `DecidableEq R` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Retrodiction | `Retrodiction.change_unlocated` | `DecidableEq R` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Retrodiction | `Retrodiction.changes_const` | `DecidableEq R` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Retrodiction | `Retrodiction.changes_le` | `DecidableEq R` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Retrodiction | `Retrodiction.changes_split` | `DecidableEq R` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Retrodiction | `Retrodiction.excursion_changes` | `DecidableEq R` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Retrodiction | `Retrodiction.moved_changes` | `DecidableEq R` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Retrodiction | `Retrodiction.step_changes` | `DecidableEq R` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
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
| Sampling | `World.sample_rests_unrefuted` | `DecidableEq w.Relatum` | 较粗的读法 / coarser reading | 可判定是它自己的条件 / its own condition |
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
| Segmentation | `Segmentation.bond_unique` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Segmentation | `Segmentation.no_record_groups` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Segmentation | `Segmentation.transitions_le` | `DecidableEq α` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
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
| Viability | `Viability.agrees_of_within` | `DecidablePred guard` | 守护之步 / a guarded step | 可判定是它自己的条件 / its own condition |
| Viability | `Viability.guardedStep_none` | `DecidablePred guard` | 守护之步 / a guarded step | 可判定是它自己的条件 / its own condition |
| Viability | `Viability.guarded_iff` | `DecidablePred guard` | 守护之步 / a guarded step | 可判定是它自己的条件 / its own condition |
| Viability | `Viability.guarded_never_fails_iff` | `DecidablePred guard` | 守护之步 / a guarded step | 可判定是它自己的条件 / its own condition |
| Viability | `Viability.ready_of_step` | `DecidablePred guard` | 守护之步 / a guarded step | 可判定是它自己的条件 / its own condition |
| Viability | `Viability.step_of_ready` | `DecidablePred guard` | 守护之步 / a guarded step | 可判定是它自己的条件 / its own condition |
| Weighted | `mass_dirac_pos` | `DecidableEq Ω` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |
| Weighted | `mem_of_mass_dirac_pos` | `DecidableEq Ω` | 分辨相同 / tells same from different | 可判定是它自己的条件 / its own condition |

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
| Contacts | `Contacts.added_gains` | `DecidableEq I` | 分辨相同 / tells same from different | — |
| Contacts | `Contacts.answers_iff` | `DecidableEq I` | 分辨相同 / tells same from different | — |
| Contacts | `Contacts.blind_misses` | `DecidableEq I` | 分辨相同 / tells same from different | — |
| Contacts | `Contacts.keeps_data_iff` | `DecidableEq I`；`∀ (i : I), D t i ∨ ¬D t i` | 分辨相同 / tells same from different | — |
| Contacts | `Contacts.keeps_iff_retains` | `DecidableEq I` | 分辨相同 / tells same from different | — |
| Contacts | `Contacts.mem_or_not` | `DecidableEq I` | 分辨相同 / tells same from different | — |
| Contacts | `Contacts.retired_loses` | `DecidableEq I` | 分辨相同 / tells same from different | — |
| Contacts | `Contacts.selections_survive_iff` | `DecidableEq I` | 分辨相同 / tells same from different | — |
| Contacts | `Contacts.survive_data_iff` | `DecidableEq I`；`∀ (i : I), D t i ∨ ¬D t i` | 分辨相同 / tells same from different | — |
| Contacts | `Contacts.through_at_iff` | `DecidableEq I` | 分辨相同 / tells same from different | — |
| Contacts | `Contacts.through_data_iff` | `DecidableEq I`；`∀ (i : I), D i ∨ ¬D i` | 分辨相同 / tells same from different | — |
| Contacts | `Contacts.trace_keeps_of_retains` | `DecidableEq I` | 分辨相同 / tells same from different | — |
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
| Coupling | `lumped_upto_iff` | `DecidableEq K` | 分辨相同 / tells same from different | — |
| Coupling | `no_policy_upto_iff` | `DecidableEq A`；`DecidableEq K` | 找出 / finds | — |
| Coupling | `throughout_or_fails` | `(n : Nat) → Decidable (p n)` | 找出 / finds | — |
| CrossSituational | `CrossSituational.candidates_eq_iff` | `DecidableEq M` | 分辨相同 / tells same from different | — |
| CrossSituational | `CrossSituational.reads_every_iff` | `DecidableEq M` | 分辨相同 / tells same from different | — |
| CrossSituational | `CrossSituational.resolves_explained_iff` | `DecidableEq M` | 分辨相同 / tells same from different | — |
| CrossSituational | `CrossSituational.resolves_iff` | `DecidableEq M` | 分辨相同 / tells same from different | — |
| Decidedness | `Counts.over_stretch_decided` | `∀ (a : α), a ∈ as → ∀ (t : Nat), t ∈ Becoming.steps S (n + 1) → Becoming.Decided (p a t)` | 分情形 / splits on a case | — |
| Decidedness | `Decided.and` | `Becoming.Decided p`；`Becoming.Decided q` | 分情形 / splits on a case | — |
| Decidedness | `Decided.exists_below` | `∀ (t : Nat), M ≤ t → t < U → Becoming.Decided (P t)` | 分情形 / splits on a case | — |
| Decidedness | `Decided.exists_mem` | `∀ (b : β), b ∈ l → Becoming.Decided (P b)` | 分情形 / splits on a case | — |
| Decidedness | `Decided.not` | `Becoming.Decided p` | 分情形 / splits on a case | — |
| Decidedness | `Decided.of_not_not` | `Becoming.Decided p` | 分情形 / splits on a case | — |
| Decidedness | `World.arising_iff_ceasing_of_decidable` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 找出 / finds | — |
| Diagonal | `Diagonal.alike_of_complete` | `(x : B) → Decidable (x = b)` | 分辨相同 / tells same from different | — |
| Diagonal | `Diagonal.complete_iff_alike` | `DecidableEq B` | 分辨相同 / tells same from different | — |
| Dissipation | `Flow.Enclosed.around` | `DecidableEq C` | 造出列表 / builds a list | `Flow.Enclosed.around_not_not`（不判定 / no decision） |
| Feedback | `Flow.Balances.adds_iff_exceeds_of_decidable` | `(t : Nat) → (g : F) → Decidable (sig p t g)` | 分情形 / splits on a case | — |
| Gated | `Gated.change_located` | `DecidableEq R` | 分辨相同 / tells same from different | — |
| Granularity | `Frame.byRecipes_translates` | `Becoming.TestsDecided F` | 找出 / finds | — |
| Granularity | `Frame.holds_byRecipes` | `Becoming.TestsDecided F` | 找出 / finds | — |
| Granularity | `Recipe.holds_after` | `Becoming.TestsDecided F` | 找出 / finds | — |
| Granularity | `Recipe.outcomes` | `Becoming.TestsDecided F` | 造出列表 / builds a list | — |
| Identification | `Identification.bounded_induction` | `DecidableEq O` | 分辨相同 / tells same from different | — |
| Identification | `Identification.fits_of_unrefuted` | `DecidableEq O` | 分辨相同 / tells same from different | — |
| Identification | `Identification.sameAhead_iff_classes` | `∀ (n m : Nat), Becoming.Decided (o n = o m)` | 分辨相同 / tells same from different | `Identification.sameAhead_iff_within`（N − 1，无前提，判定位置 / no premise, positions decided）；`Identification.sameAhead_iff_below`（2N − 1，无前提 / no premise） |
| Identification | `Identification.unrefuted_persists` | `DecidableEq O` | 分辨相同 / tells same from different | — |
| Identification | `Law.AgreeTo.decided` | `∀ (s s' : S), s ∈ l → s' ∈ l → Becoming.Decided (o s = o s')` | 分情形 / splits on a case | — |
| Identification | `Law.sameFuture_iff_classes` | `∀ (s s' : S), s ∈ l → s' ∈ l → Becoming.Decided (o s = o s')` | 分辨相同 / tells same from different | `Law.sameFuture_iff_within`（N − 1，无前提，判定位置 / no premise, positions decided）；`Law.sameFuture_classes_unrefuted`（不判定，不被否证 / no decision, refuted by nothing）；`Law.sameFuture_iff_below`（2N − 1，无前提 / no premise） |
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
| Lasting | `Lasting.orbit_reaches_iff_variant` | `DecidablePred target` | 造出指示 / builds an indicator | — |
| Lasting | `Lasting.reaches_iff_histories` | `DecidablePred target` | 找出 / finds | — |
| Lasting | `Lasting.reaches_iff_not_lasts` | `DecidablePred target` | 找出 / finds | — |
| Lasting | `Lasting.reaches_of_histories` | `DecidablePred target` | 找出 / finds | — |
| Lasting | `Lasting.reaches_of_not_lasts` | `DecidablePred target` | 找出 / finds | — |
| Learnable | `Learnable.learnable_iff` | `DecidableEq R` | 找出 / finds | `Learnable.agree_of_rests_both`（必要一侧，对每个学习者，不判定 / the necessary side, of every learner, no decision） |
| Learnable | `Learnable.learnable_of_lumped` | `DecidableEq R` | 找出 / finds | — |
| Learnable | `Learnable.refuted_on_one` | `DecidableEq V` | 分辨相同 / tells same from different | `Learnable.claim_not_right_on_both`（无前提：主张不在两者上都对 / no premise: the claim is not right on both） |
| Learnable | `Learnable.still_learnable_iff_lumped` | `DecidableEq R` | 找出 / finds | `Learnable.still_lumped_of_rests`（必要一侧，不判定 / the necessary side, no decision） |
| Learning | `Learning.claim_refuted_on_one` | `DecidableEq O` | 分辨相同 / tells same from different | `Learning.no_record_fixes_next`（无前提：主张不在两者上都对 / no premise: the claim is not right on both, P73） |
| Learning | `Learning.determines_lumped_iff` | `DecidableEq K` | 找出 / finds | `Learning.lumped_determines`（无前提的一个方向 / one direction, no premise, P73） |
| Learning | `Learning.eq_of_not_refuted` | `DecidableEq O` | 分辨相同 / tells same from different | — |
| Learning | `Learning.every_determines_nothing` | `DecidableEq I` | 分辨相同 / tells same from different | — |
| Learning | `Learning.every_free` | `DecidableEq I` | 分辨相同 / tells same from different | — |
| Likeness | `BranchingTest.apart_from_listed` | `∀ (y : S'), Becoming.Decided (q y)` | 找出 / finds | — |
| Likeness | `Chains.outcomes` | `∀ (k : Nat), Becoming.Decided (α k)`；`∀ (k : Nat), Becoming.Decided (β k)` | 造出列表 / builds a list | — |
| Likeness | `Chains.outcomesListed` | `∀ (k : Nat), Becoming.Decided (α k)`；`∀ (k : Nat), Becoming.Decided (β k)` | 造出列表 / builds a list | — |
| Likeness | `Decided.exists_listed` | `∀ (b : β), b ∈ l → Becoming.Decided (P b)` | 分情形 / splits on a case | — |
| Likeness | `Decided.exists_not_in` | `∀ (b : β), b ∈ l → Becoming.Decided (P b)` | 找出 / finds | — |
| Likeness | `Decided.exists_not_of_listed` | `∀ (b : β), Becoming.Decided (P b)` | 找出 / finds | — |
| Likeness | `Decided.exists_of_listed` | `∀ (b : β), Becoming.Decided (P b)` | 分情形 / splits on a case | — |
| Likeness | `Decided.forall_in` | `∀ (b : β), b ∈ l → Becoming.Decided (P b)` | 分情形 / splits on a case | — |
| Likeness | `Decided.forall_of_listed` | `∀ (b : β), Becoming.Decided (P b)` | 分情形 / splits on a case | — |
| Likeness | `Decided.iff` | `Becoming.Decided p`；`Becoming.Decided q` | 分情形 / splits on a case | — |
| Likeness | `Decided.imp` | `Becoming.Decided p`；`Becoming.Decided q` | 分情形 / splits on a case | — |
| Likeness | `EitherThroughout.list` | `∀ (k : Nat) (b : β), Becoming.Decided (P k b)` | 找出 / finds | — |
| Likeness | `OutcomesListed.forth_decided` | `∀ (t : S) (t' : S'), Becoming.Decided (R t t')` | 分情形 / splits on a case | — |
| Likeness | `OutcomesListed.matched_decided` | `∀ (t : S) (t' : S'), Becoming.Decided (R t t')` | 分情形 / splits on a case | — |
| Likeness | `OutcomesListed.unmatched` | `∀ (t : S) (t' : S'), Becoming.Decided (R t t')` | 找出 / finds | — |
| Likeness | `drops_somewhere` | `∀ (k : Nat), Becoming.Decided (P k x)` | 找出 / finds | — |
| Likeness | `forth_decided` | `∀ (t : S) (t' : S'), Becoming.Decided (R t t')` | 分情形 / splits on a case | — |
| Likeness | `stops_decreasing` | `∀ (k : Nat) (x : X), Becoming.Decided (P k x)` | 找出 / finds | — |
| Likeness | `unmatched_of_not_forth` | `∀ (t : S) (t' : S'), Becoming.Decided (R t t')` | 找出 / finds | — |
| Listing | `Flow.standing_lowers_decided` | `Becoming.IdentityDecided ds` | 造出列表 / builds a list | — |
| Listing | `Web.arising_of_ceasing_listing` | `(t : Nat) → (a b : F) → a ∈ l t → b ∈ l t → Decidable (a = b)`；`(t : Nat) → (f : F) → Decidable (W.active t f)` | 找出 / finds | `Web.arising_of_ceasing`（给定普查；此处还用 `listOnce` 造普查 / a supplied census; here `listOnce` also constructs it, P77） |
| Listing | `listsOnceBy_of_decided` | `∀ (a b : α), a ∈ l → b ∈ l → Becoming.Decided (R a b)` | 造出列表 / builds a list | — |
| Listing | `listsOnce_of_decided` | `Becoming.IdentityDecided l` | 造出列表 / builds a list | — |
| Listing | `of_listsOnce` | `Becoming.IdentityDecided l` | 造出列表 / builds a list | — |
| Locality | `Covers.coming_from_of_ceasing` | `(a : α) → (t : Nat) → Decidable (p a t)` | 找出 / finds | `Covers.not_not_coming_from`（无前提 / no premise, P48） |
| Locality | `Covers.within` | `(a : α) → (t : Nat) → Decidable (p a t)` | 找出 / finds | — |
| Locality | `coming_of_ceasing_covered` | `(a : α) → (t : Nat) → Decidable (p a t)` | 找出 / finds | `Covers.not_not_coming_from`、`Covers.ceasing_not_recurring`（无前提 / no premise, P48） |
| LossMatching | `Frame.exists_fresh` | `DecidableEq C` | 找出 / finds | — |
| LossMatching | `Frame.strictLossMatch_iff_length_of_alike` | `DecidableEq C` | 分辨相同 / tells same from different | — |
| Novelty | `upto_or_fails` | `(n : Nat) → Decidable (p n)` | 找出 / finds | — |
| Openness | `Flow.Enclosed.aroundStanding` | `DecidableEq C` | 造出列表 / builds a list | `Flow.Enclosed.aroundStanding_not_not`（不判定 / no decision） |
| Openness | `Listed.few_of_quiet` | `(a : α) → (t : Nat) → Decidable (p a t)` | 找出 / finds | `Listed.few_of_stop_unrefuted`（不判定 / no decision, P58） |
| Openness | `World.CountedBy.arising_iff_ceasing` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 找出 / finds | — |
| Openness | `World.CountedWithin.arising_iff_ceasing` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 找出 / finds | — |
| Openness | `World.Finite.arising_iff_ceasing` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 找出 / finds | — |
| Openness | `World.Finite.countedWithin` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 造出列表 / builds a list | — |
| Openness | `World.arising_of_ceasing` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 找出 / finds | — |
| Openness | `World.few_active` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` | 找出 / finds | `Listed.few_of_stop_unrefuted`、`World.rest_few`（不判定 / no decision, P58） |
| Openness | `comes_after` | `(t : Nat) → Decidable (p t)` | 找出 / finds | `comes_after_unrefuted`（不判定，那一步不能被否证 / no decision, the step unrefuted） |
| OrderNormal | `Footprinted.decidesIdle_iff` | `DecidableEq X` | 分辨相同 / tells same from different | — |
| OrderNormal | `Footprinted.least_exists_iff` | `DecidableEq X` | 分辨相同 / tells same from different | — |
| Persistence | `Web.persisting_census` | `(t : Nat) → (f : F) → Decidable ((W.persisting h).Continues R t f)`；`(t : Nat) → (f : F) → Decidable ((W.persisting h).active t f)`；`(t : Nat) → (g : F) → Decidable ((W.persisting h).Continued R t g)`；`(t : Nat) → (g f : F) → Decidable (R t g f)` | 找出 / finds | — |
| Persistence | `World.arises_fixed_iff` | `DecidableEq w.Relatum` | 分辨相同 / tells same from different | — |
| Persistence | `World.ceases_fixed_iff` | `DecidableEq w.Relatum` | 分辨相同 / tells same from different | — |
| Persistence | `World.fixed_iff` | `DecidableEq w.Relatum` | 分辨相同 / tells same from different | — |
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
| Readout | `Readout.commonWitness_or_covered` | `DecidableEq D` | 找出 / finds | — |
| Readout | `Readout.no_common_report_envelopes_iff` | `DecidableEq D` | 找出 / finds | — |
| Readout | `Readout.no_common_report_iff` | `DecidableEq D` | 找出 / finds | — |
| Refinement | `Decided.exists_within` | `∀ (x : X), x ∈ l → Becoming.Decided (P x)` | 分情形 / splits on a case | — |
| Refinement | `Refining.grow` | `∀ (k : Nat) (x y : X), x ∈ l → y ∈ l → Becoming.Decided (R k x y)` | 分情形 / splits on a case | — |
| Refinement | `Refining.steady_or_grown` | `∀ (k : Nat) (x y : X), x ∈ l → y ∈ l → Becoming.Decided (R k x y)` | 找出 / finds | — |
| Refinement | `Refining.steady_within` | `∀ (k : Nat) (x y : X), x ∈ l → y ∈ l → Becoming.Decided (R k x y)` | 找出 / finds | — |
| Response | `Flow.Balances.comparison_within_response_of_decidable` | `(g : F) → Decidable (L.WithinResponse L' W obs part g)` | 分辨相同 / tells same from different | `Flow.Balances.comparison_within_response`（覆盖不被否证在回应所及之内者，不判定 / covering what is not refuted to be within the reach, no decision, P65） |
| Retrodiction | `Retrodiction.fits_or_separated` | `DecidableEq O` | 分辨相同 / tells same from different | — |
| Retrodiction | `Retrodiction.look_right_iff` | `DecidableEq O`；`DecidableEq V` | 分辨相同 / tells same from different | — |
| Retrodiction | `Retrodiction.reading_right_iff` | `DecidableEq O`；`DecidableEq V` | 分辨相同 / tells same from different | — |
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
| TimedResponse | `TimedResponse.different_answers_require_reached` | `Decidable (Becoming.TimedResponse.ReachedBy L L' W obs source g D)` | 分情形 / splits on a case | — |
| Transmission | `Flow.transmitsWithin_iff_split` | `(t : Nat) → (x : X) → Decidable (W.requires t x c)` | 分情形 / splits on a case | — |
| Transmission | `Web.inheritsAt_of_split` | `Decidable (W.requires t x c)` | 分情形 / splits on a case | `Web.inheritsAt_not_not`（不判定时继承不能被否证 / inheritance is unrefuted without the decision, P84） |
| Unfolding | `Frame.claims_recur_iff` | `(c : C) → (t : Nat) → Decidable (F.realized (r.state t) c)` | 找出 / finds | — |
| Weighted | `every_weighting_iff` | `DecidableEq Ω` | 造出指示 / builds an indicator | — |

## 排中律或其受限形式作为假设 / Excluded middle, in full or restricted form, as a hypothesis

这些是边界定理：它们表明排中律或其受限形式（例如 `NowhereDecided`：一个已判定的族是否处处不成立已判定）给出什么，配合 `World.law_iff_em`、`World.law_decides`、`World.lpo_of_finite_ends`、`Listed.lpo_of_few`、`Web.lpo_of_ending`、`ChangeBound.lpo_of_ends`、`alike_decided_iff_em`、`alike_of_sameBranchingTests_iff_em`、`alike_of_sameBranchingTests_decided_steps_iff_em`、`alike_of_sameBranchingTests_outcomes_iff`、`matchesParts_of_compact_iff_em`、`jointAlike_of_sameJointTests_iff_em`、`Recipe.holds_after_iff_em`，表明命名一步、对每个世界要求复现、由检验判定相同、或把配方读作一个检验的形式需要可判定性。 / These are boundary theorems: they show what excluded middle, or a restricted form of it (such as `NowhereDecided`: whether a decided family holds nowhere is decided), gives, and with `World.law_iff_em`, `World.law_decides`, `World.lpo_of_finite_ends`, `Listed.lpo_of_few`, `Web.lpo_of_ending`, `ChangeBound.lpo_of_ends`, `alike_decided_iff_em`, `alike_of_sameBranchingTests_iff_em`, `alike_of_sameBranchingTests_decided_steps_iff_em`, `alike_of_sameBranchingTests_outcomes_iff`, `matchesParts_of_compact_iff_em`, `jointAlike_of_sameJointTests_iff_em`, `Recipe.holds_after_iff_em`, that the forms naming a step, asking recurrence of every world, fixing likeness by tests or reading a recipe as one test need decidedness.

- Change: `exists_not_of_em`
- Change: `persists_of_em`
- Composition: `Compact.of_listed`
- Composition: `JointFrame.TestsStable.of_em`
- Composition: `jointAlike_iff_sameJointTests_of_listed`
- Granularity: `Frame.blocks_history_matches_of_em`
- Granularity: `Frame.byRecipes_history_matches_of_em`
- Granularity: `Recipe.Advance.same_of_em`
- Granularity: `Recipe.Leaves.same_of_em`
- Granularity: `Recipe.trace_same_of_em`
- Granularity: `SameBranchingTests.step_of_em`
- Granularity: `SameBranchingTests.trace_of_em`
- Granularity: `TestsDecided.of_em`
- Granularity: `Translates.history_matches_of_em`
- Joining: `Joining.FiniteOutcomes.alike_iff_sameBranchingTests`
- Joining: `Joining.FiniteOutcomes.common_structure`
- Joining: `Joining.FiniteOutcomes.identifiesAlike`
- Joining: `Joining.FiniteOutcomes.retained_alike_iff`
- Joining: `Joining.LocallyFinite.alike_iff`
- Joining: `Joining.common_refinement_of_em`
- Joining: `Joining.retained_history_matches_of_em`
- Likeness: `EitherNever.of_nowhereDecided`
- Likeness: `EitherThroughout.of_em`
- Likeness: `EitherThroughout.of_nowhereDecided`
- Likeness: `NowhereDecided.of_em`
- Likeness: `alike_iff_sameBranchingTests_of_em`
- Likeness: `alike_of_sameBranchingTests_of_em`
- Likeness: `apart_of_not_sameBranchingTests`
- Reserve: `Web.Carries.chain_ends_of_em`
- Reserve: `Web.chain_ends_of_em_from`
- Space: `World.law_of_em`
- Space: `quiet_of_once`
- Transmission: `split_of_em`

## 计数而可判定被证明 / Counting with decidedness proved

这些定理的陈述计数，但不以可判定为假设：可判定由见证世界或体现证明（例如 `Embodied.decided`）。按模块计： / These theorems count in their statements without taking decidedness as a hypothesis: it is proved for witness worlds or from embodiment (for example `Embodied.decided`). By module:

- Counting: 35
- Entropy: 5
- Identification: 1
- Learnable: 1
- Learning: 2
- Locality: 1
- LossMatching: 1
- Novelty: 1
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
| Contacts | `Contacts.spot` | `DecidableEq I` |
| Copying | `Copying.Supplies` | `DecidableEq α` |
| Copying | `Copying.batch` | `DecidableEq α` |
| Copying | `Copying.countOf` | `DecidableEq α` |
| Copying | `Copying.defects` | `DecidableEq α` |
| Copying | `Copying.exchange` | `DecidableEq α` |
| Copying | `Copying.exchangeAt` | `DecidableEq α` |
| Copying | `Copying.inspect` | `DecidableEq α` |
| Copying | `Copying.inspectAt` | `DecidableEq α` |
| Copying | `Copying.pairDraw` | `DecidableEq α` |
| Copying | `Copying.readStep` | `DecidableEq α` |
| Copying | `Copying.readSteps` | `DecidableEq α` |
| Copying | `Copying.readTick` | `DecidableEq α` |
| Copying | `Copying.remove` | `DecidableEq α` |
| Copying | `Copying.removeAll` | `DecidableEq α` |
| Copying | `Copying.scanSites` | `DecidableEq α` |
| Copying | `Copying.steps` | `DecidableEq α` |
| Copying | `Copying.tick` | `DecidableEq α` |
| Copying | `Copying.unlikeFrom` | `DecidableEq α` |
| Counterfactual | `mixIn` | `DecidableEq C` |
| Counting | `World.CountsObey` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` |
| Counting | `World.saturated_decided` | `(t : Nat) → (x : w.Relatum) → Decidable (w.web.active t x)` |
| Coupling | `policyUpto` | `DecidableEq K` |
| Dissipation | `adjoin` | `DecidableEq α` |
| Dissipation | `decideMem` | `DecidableEq α` |
| Dissipation | `insertNew` | `Decidable (a ∈ l)` |
| Identification | `Identification.decBorneOut` | `DecidableEq O` |
| Identification | `Identification.decFits` | `DecidableEq O` |
| Identification | `Identification.firstFit` | `(a : α) → Decidable (p a)` |
| Identification | `Identification.withBound` | `DecidableEq O` |
| Identification | `Law.decideAlike` | `DecidableEq R` |
| Identity | `Web.Census.decideContinued` | `(t : Nat) → (g f : F) → Decidable (R t g f)` |
| Identity | `Web.Census.decideContinues` | `(t : Nat) → (g f : F) → Decidable (R t g f)` |
| Identity | `Web.instDecidableArisesFrom` | `(t : Nat) → (f : F) → Decidable (W.Continues R t f)`；`(t : Nat) → (f : F) → Decidable (W.active t f)` |
| Identity | `Web.instDecidableCeasesFrom` | `(t : Nat) → (f : F) → Decidable (W.active t f)`；`(t : Nat) → (g : F) → Decidable (W.Continued R t g)` |
| Lasting | `Lasting.hitTime` | `DecidablePred target` |
| Learnable | `Learnable.withWorld` | `DecidableEq R` |
| Learnable | `Learnable.withWorldAt` | `DecidableEq R` |
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
| LossMatching | `Frame.classCount` | `DecidableEq K` |
| LossMatching | `Frame.lostOf` | `(c : C) → Decidable (F.realized s c)` |
| LossMatching | `LossMatching.decideDistinct` | `DecidableEq α` |
| Order | `Web.commuteDecided` | `(n : Nat) → (f : F) → Decidable (W.active n f)` |
| OrderNormal | `Footprinted.inList` | `DecidableEq X` |
| Persistence | `Reidentify.exchangeAfter` | `DecidableEq X` |
| Persistence | `transpose` | `DecidableEq X` |
| Population | `Web.decideDissolves` | `(t : Nat) → (g : F) → (c : C) → Decidable (W.requires t g c)` |
| Population | `Web.decideForms` | `(t : Nat) → (g : F) → (c : C) → Decidable (W.requires t g c)` |
| Population | `decideSome` | `(a : α) → Decidable (p a)` |
| Premises | `keep` | `(a : α) → Decidable (p a)` |
| Readout | `Readout.blame` | `DecidableEq D` |
| Readout | `Readout.pick` | `Decidable p` |
| Regrouping | `Web.requiredLevel` | `(t : Nat) → (f : F) → (c : C) → Decidable (W.requires t f c)` |
| Reserve | `Web.redirect` | `(t : Nat) → (f : F) → Decidable (W.Supported t f)` |
| Retrodiction | `Retrodiction.changes` | `DecidableEq R` |
| Runaway | `Web.raise` | `DecidableEq C` |
| Sampling | `Flow.sample` | `DecidableEq F` |
| Sampling | `Flow.unionPresent` | `DecidableEq F` |
| Sampling | `World.sample` | `DecidableEq w.Relatum` |
| Sampling | `gate` | `DecidableEq α` |
| Sampling | `gateBy` | `Decidable p` |
| Segmentation | `Segmentation.bond` | `DecidableEq α` |
| Segmentation | `Segmentation.departures` | `DecidableEq α` |
| Segmentation | `Segmentation.transitions` | `DecidableEq α` |
| Standing | `World.DependsObey` | `(t : Nat) → (f c : w.Relatum) → Decidable (w.web.requires t f c)` |
| Testing | `recordThen` | `DecidableEq C` |
| Tower | `Tower.flow` | `DecidableEq F` |
| Tower | `Tower.reads` | `DecidableEq F` |
| Tower | `Tower.refine` | `DecidableEq F` |
| Tower | `Tower.web` | `DecidableEq F` |
| Viability | `Viability.guardedHistory` | `DecidablePred guard` |
| Viability | `Viability.guardedStep` | `DecidablePred guard` |
| Weighted | `dirac` | `DecidableEq Ω` |

另：一个部分以 `part : F → Bool` 给出，它的切分由类型定下（`Becoming.Admission`、`Becoming.Significance`）；这是比较的参数，不是关于世界的前提。 / Also: a part is given as `part : F → Bool`, its split decided by its type (`Becoming.Admission`, `Becoming.Significance`); it is a parameter of the comparison, not a premise about the world.
