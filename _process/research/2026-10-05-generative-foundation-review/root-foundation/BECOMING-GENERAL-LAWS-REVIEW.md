# 一般规律的独立审查（第十七次）/ Independent review of the general laws (seventeenth)

2026-10-14，Asia/Bangkok。**AI 独立审查（第十七次；另一 agent，未参与撰写）。** Ren 对开放问题计划第 19 项选了“一个 agent”（`development/becoming-general-laws-plan/OPEN-ISSUES-PLAN.md` §3）。整合会话下达任务，并负责落地。

审查对象 / Object:
- 2026-10-13 至 14 日加入 Becoming 包的一般规律，状态为 `822b6cfb`（第四批落地后的主线）。
- 核心模块 / Core modules：`Stock`、`Contacts`、`LossMatching`、`Assurance`、`Segmentation`、`Readout`、`Gated`、`Viability`、`Countdown`、`Lasting`、`Copying`、`Retrodiction`、`CrossSituational`、`Likeness`、`Learnable`。
- 核心模块中的新增 / Additions to core modules：`Joint`、`Substitution`、`Ranking`、`Continuation`（L2，`8cf2161a`）。
- 桥 / Bridges：`Instances.lean`、`RenewalBridge.lean`。
- 外围 / Periphery：`MachineInstances`、`CopyingInstances`、`ProtocolInstances`、`MarketInstances`、`VersionedTaskInstances`、`RetrodictionInstances`，以及 `LearnedProcedureTransmission` 的新增。
- 引用它们的记录，研究 `BECOMING-RENEWAL-READING.md` 第 112–119 节。
- 审查期间主线前进到 `25cd209a`（相同之桥，第 120 节）。其中核心只改了 `Likeness.lean` 与 `Bridge.lean`，这两处新增不在本审查范围内。两个更正提交建在 `25cd209a` 上。

本审查在自己的 git 工作树中进行。没有运行仓库的 `check_*.py`，没有改动回执、证明绑定或来源哈希，没有编辑 `_process/BECOMING-WORKBOARD.md`。Lean 试验只用 `scratch_build.py`：探针放在仓库外的空目录里构建，构建后复制到 `development/becoming-general-laws-review-probes/`。
The review ran in its own git worktree. No repository `check_*.py` was run, and no receipt, proof binding or source hash was changed. `_process/BECOMING-WORKBOARD.md` was not edited. Lean experiments used only `scratch_build.py`, on a probe built in an empty directory outside the repository and then copied to `development/becoming-general-laws-review-probes/`.

严重度 / Severity:
- **error**：所写的话是假的（在 Lean、记录或研究中）；
- **overstatement**：所写的比所证的强，通常是漏了一个条件或量词；
- **understatement**：所写的比所证的弱；
- **naming**：名字或用词不合命名规则（市场词等）；
- **presentation**：真，但会误导，或把定义的展开当作规律；
- **confirmed**：核对过，所写与所证相符。

与此前审查的分类对应 / Against the earlier classes：error 与 overstatement 属（乙）；探针 `one_change_keeps`、`lost_side_is_worse`、`longer_word_draws_more`、`done_before_without_apart` 是（丙）型的反例，都针对文字，不针对 Lean 陈述。没有发现（甲）型省略。

---

## 摘要

**形式状态。**
- 没有发现假的 Lean 定理。每个核对过的定理都证明了它自己的陈述。
- 每个“恰当”（exactly）都核对了 Lean 陈述：都是真正的当且仅当。量词与记录相符，下列 G2–G5 漏掉条件的几处除外。
- 实例都确实经过核心的规律。外围模块用 `view_tick`、`history_eq`、`guardedStep_eq`、`run_eq`、`head_advances`、`counts`、`acquire_eq` 等，把机器的一步对到核心的一步，再引用核心定理。没有发现只靠有限检查冒充实例的情形。
- 需要判定的定理都证明了它们所说的：`Lasting.histories_need_decision` 给出 LPO，`dual_needs_decision` 给出双重否定消去，`numeric_needs_decision` 给出可判等，`Likeness.alike_decided_iff_em` 给出排中律。
- 探针模块（5 个定理，8 个声明）用 `scratch_build.py` 构建：没有错误或警告，公理报告为空。

**计数（按严重度）。**

| 严重度 | 数目 | 编号 |
|---|---|---|
| error | 2 | G1、G2 |
| overstatement | 3 | G3、G4、G5 |
| understatement | 0 | — |
| presentation | 2 | G6、G7 |
| naming | 4 | G8、G9、G10、G11 |
| confirmed | 14 | C1–C14 |

**最重要的发现。**
1. **G1（error）。** “在任何配置／路线之下都没有严格匹配”把 `not_strictLossMatch_of_base_lost` 的方向说反了。开放问题第 10 项只改了一处（定律 5），同一说法还留在定律 9、第五个反例、第 112 节、`LossMatching` 的两段文档注释，以及 `RepairComparison` 的文档注释和名字 `fragile_b3_below_nothing` 里。记录中的两处已更正（`96812ae6`）；其余要改 Lean 或研究，会改变来源哈希，留给整合会话。
2. **G2（error）。** `inherited-structural-copying` 的主张漏了“同长的词中”。没有它，局部汲取的排序律是假的：ABAB 用 4、AA 用 3，而异类之后汲取较少。已更正（`b4496892`）。
3. **G3–G5（overstatement）。** 三处漏了条件：
   - 替代：陈述漏了“在每一种这样的转化下”。对一次转化，所述的等价两个方向都可能不成立。
   - 回溯：两端控制要读数相同。
   - 计数：“没有更短的运行完成”需要 `apart`，即 `not_done_before`，而不是 `pending_before`。
4. **G8–G11（naming）。** 新名字里重新出现了市场词：`Lasting.exhausts` 的 `costs`；`Continuation` 与 `RenewalBridge` 的 `surplus`（第十六次审查已让 `surplus_*` 改名；包里已有结构词“净给予”，见 `Flow.Balances.supported_of_net_give`）；`ProtocolInstances` 的 “Funded completion”、“can still pay”、`charge_some`；`MarketInstances` 文档中的 “costs the stock”。

**保留什么。** 全部 Lean 都保留。改动只在文字、名字和文档注释上。G6 与 G7 指出两处薄的内容被说成规律：`ReadsAt` 的两条“规律”是定义的展开；`RenewalBridge` 的平衡是构造出来的。应如实说明，不必删去。

## English summary

**Formal status.**
- No false Lean theorem was found. Every theorem checked proves its own statement.
- Every "exactly" was checked against its Lean statement, and each is a genuine iff. Quantifiers match the records, except at the places listed under G2–G5, where a condition was dropped.
- The instances really go through the core laws. Each peripheral module first identifies one machine move with one core move (`view_tick`, `history_eq`, `guardedStep_eq`, `run_eq`, `head_advances`, `counts`, `acquire_eq`) and then cites the core theorem. No finite check poses as an instance.
- The needs-a-decision theorems show what they claim: `Lasting.histories_need_decision` gives LPO, `dual_needs_decision` double-negation elimination, `numeric_needs_decision` decidable equality, and `Likeness.alike_decided_iff_em` excluded middle.
- The probe module (5 theorems, 8 declarations) builds with `scratch_build.py` with no error or warning and empty axiom reports.

**Counts by severity:** error 2 (G1, G2); overstatement 3 (G3–G5); understatement 0; presentation 2 (G6, G7); naming 4 (G8–G11); confirmed 14 (C1–C14).

**Top findings.**
1. **G1 (error).** "Strictly matched below no configuration/course" inverts the direction of `not_strictLossMatch_of_base_lost`.
   - Open-issues item 10 corrected one occurrence, law 5. The same wording remains in:
     - law 9 and the fifth counterexample;
     - study §112;
     - two `LossMatching` docstrings;
     - `RepairComparison`'s docstring and the name `fragile_b3_below_nothing`.
   - The two record occurrences are corrected (`96812ae6`). The rest change source hashes and are left to the integrator.
2. **G2 (error).** `inherited-structural-copying` dropped "among words of one length". Without it the local-draw ranking is false: ABAB uses 4 and AA uses 3, although an unlike attachment draws less. Corrected (`b4496892`).
3. **G3–G5 (overstatement).** Each drops a condition:
   - The substitution statement drops "under every such transformation". For one transformation, both directions of the stated equivalence can fail.
   - The retrodiction bracket needs the two end controls to read the same.
   - "No shorter run finishes" needs `apart`, through `not_done_before`, not `pending_before`.
4. **G8–G11 (naming).** Market words return in new names:
   - `costs` in `Lasting.exhausts`;
   - `surplus` in `Continuation` and `RenewalBridge`. The sixteenth review had `surplus_*` renamed, and the package already has the structural "net give" (`Flow.Balances.supported_of_net_give`).
   - "Funded completion", "can still pay" and `charge_some` in `ProtocolInstances`;
   - "costs the stock" in `MarketInstances`' docstrings.

**What to keep.** Keep all the Lean. The changes are to text, names and docstrings only. G6 and G7 are two places where thin content is presented as a law, and they should be described as such rather than removed:
- `ReadsAt`'s two "laws" unfold its definition.
- `RenewalBridge`'s balance holds by construction.

---

## 0. 范围与方法 / Scope and method

**Read in full.**
- The plans:
  - `development/becoming-general-laws-plan/PLAN.md`;
  - `OPEN-ISSUES-PLAN.md`;
  - `theories/becoming/chapters/NONDUAL-METHOD.md`.
- Study `BECOMING-RENEWAL-READING.md` §§112–119 (lines 7204–7841), and the English summaries of those sections.
- The two earlier reviews used as format: `BECOMING-P49-REVIEW.md` and the head of `BECOMING-P30-P31-P29B-REVIEW.md`.

**Lean, every statement.** Every theorem statement, definition and docstring was extracted and read, with a script that prints them without proofs.

| Module | Lines | Theorems |
|---|---|---|
| Stock | 537 | 40 |
| Contacts | 252 | 24 |
| LossMatching | 493 | 34 |
| Assurance | 238 | 20 |
| Segmentation | 360 | 17 |
| Readout | 101 | 7 |
| Gated | 85 | 4 |
| Viability | 312 | 25 |
| Countdown | 338 | 20 |
| Lasting | 889 | 69 |
| Copying | 1188 | 68 |
| Retrodiction | 333 | 17 |
| CrossSituational | 460 | 37 |
| Likeness (at `822b6cfb`) | 936 | 61 |
| Learnable | 314 | 17 |
| Instances | 293 | 22 |
| RenewalBridge | 334 | 18 |
| MachineInstances | 1320 | |
| CopyingInstances | 1216 | |
| ProtocolInstances | 343 | |
| MarketInstances | 719 | |
| VersionedTaskInstances | 512 | |
| RetrodictionInstances | 264 | |

Also read:
- the L2 diffs to `Joint`, `Substitution`, `Ranking` and `Continuation` (`8cf2161a`);
- the C1 rename "credits" → "includes" (`b7126563`);
- the `LearnedProcedureTransmission` additions.

**Lean, proofs read where a finding turns on them.**
- `LossMatching`: `StrictLossMatch`, `not_strictLossMatch_of_base_lost`, `ReadsAt` and its three theorems.
- `Substitution`: `DependenceChanged`, `ConsumingThrough`, `consumingIn_kept_iff`, `Lone`.
- `Countdown`: `Counts`, `Advances`, `completes_iff`, `pending_before`, `not_done_before`.
- `Lasting`: `exhausts`, `small_descends`, the three decision witnesses.
- `Retrodiction`: `bracket`, `bracket_settles_iff`, `change_unlocated`.
- `Copying`: `use`, `pairDraw`, `unlikeFrom`, `use_word`, `use_midpoint`, `use_lt_iff`.
- `RenewalBridge`: `surplus`, `flow`, `level_succ_le`, `balances`, `surplus_active`.
- `Revision`: `Revising.step_iff`, `covered_not_enacted`.
- `ReferencePlan`: `frozen_blind`, `frozen_misses`.
- `Gated.kept_along`, `kept_along_iff`.
- `Viability`: `within_not_kernel`, `needs_admissible`.
- `Likeness.alike_decided_iff_em`; `Histories.alike_iff_sameTests`.
- `VersionedTaskInstances.continuation_of_completed` and `GoalFormationRevision.operate`.

**Records** (`theories/becoming/results/records/`), read in English with every field.
- Batch 1:
  - selection-under-registration-revision
  - consequence-revised-reference-plan
  - recurring-reference-revision
  - finite-aggregation-within-restorable-basic-losses
- L2:
  - joint-difference-making
  - substitution-preserves-consumption
  - ranking-under-readings
  - supported-renewal-recovery
  - relational-reading-comparison
  - relational-renewal-classification
  - learned-procedure-transmission
- §113:
  - assured-route-criterion
  - formed-goal-revision-continuation
  - material-preparation-output
  - transition-grouping-word-partition
  - acquired-binding-compositional-use
  - control-coherence-loss
  - joint-correlation-reduced-dynamics
  - organizational-rule-inheritance
  - joint-practice-forms-continuation
- §§114–116:
  - market-protected-continuation
  - market-finite-support-obstruction
  - market-partial-correction-boundary
  - market-supported-finite-transition
  - recoverable-mediated-change
  - mediated-evidence-transport
  - reserved-shutdown-during-recovery
  - inherited-structural-copying
  - recurrent-chain-assembly
  - formed-copying-registration
  - formed-copying-correction
  - historical-source-binding
- §117:
  - enacted-scene-binding
  - encounter-selection-and-revision
  - retrospective-source-binding
  - acquired-revision-of-pending-task
  - pending-task-context-applicability
  - versioned-request-completion
- §§118–119:
  - determinacy-up-to-likeness
  - tests-fix-likeness-where-determined
  - configurations-alike-by-relation
  - learnable-through-registration
  - learning-by-refutation

**Chinese, compared sentence by sentence with the English.**
- the claims of inherited-structural-copying and historical-source-binding;
- finite-aggregation laws 4, 5 and 8, its fifth counterexample and history entry 5;
- the statement of substitution-preserves-consumption;
- the statement and law 0 of supported-renewal-recovery;
- study §112 line 7240, §115 lines 7448 and 7501.

**Sampled.** The spine chapter's §9 rows for the new modules, in `THE-THEORY-OF-BECOMING.md`. Only the lines found by search for the wordings in G1, G2, G4 and G9 were read.

**Tested in Lean.** `development/becoming-general-laws-review-probes/ReviewProbeGL.lean`:
- Built with `LEAN_TIMEOUT=2400 python3 -B scratch_build.py <empty dir outside the repo> Becoming.ReviewProbeGL` against this checkout, Lean 4.29.1 (`f72c35b3`).
- The other 20 build steps were restored from the shared cache, since their inputs were unchanged.
- No error or warning; the axiom reports are empty (`scratch-build.out.json`).
- No hypothesis needed a Lean drop-test beyond these probes. The hypotheses that could be idle were checked by reading the proofs. Each one is used, apart from the disclosed cases: `registered_inheritance_instance` drops the old non-empty premise, and the records say so.

**Not done.**
- No `check_*.py` and no package rebuild.
- The peripheral Mathlib modules were read, not rebuilt.
- The likeness bridge (§120, `25cd209a`) was not reviewed.
- README and other generated overviews were not reviewed.
- Every theorem statement was read, but not every proof. Proofs were read where a finding depended on them; the rest is covered by the checkers' receipts.

---

## 1. 发现表 / Findings table

Lean line numbers are at `822b6cfb`; they are unchanged at `25cd209a` except in `Likeness.lean`. Study and spine line numbers are at `25cd209a`. Paths are abbreviated as follows:
- *core* = `experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/`
- *gc* = `experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/`
- *rec* = `theories/becoming/results/records/`
- *study* = `BECOMING-RENEWAL-READING.md`
- *spine* = `theories/becoming/chapters/THE-THEORY-OF-BECOMING.md`

### Errors, overstatements, presentation and names

| id | module / record | finding（中文 / English） | severity | evidence | proposed correction |
|---|---|---|---|---|---|
| G1 | `LossMatching`, `RepairComparison`; rec finite-aggregation-within-restorable-basic-losses; study §112 | 说“失去共同支持的配置在任何配置之下都没有严格匹配”，自然读法是：它不是任何严格匹配中较差的一方。Lean 说的是：它不是任何严格匹配中较好的一方。第 10 项只改了定律 5。<br>"Strictly matched below no configuration" reads as "the worse side of no strict match". The Lean says it is the better side of none. Item 10 fixed only law 5. | error | `not_strictLossMatch_of_base_lost` concludes `¬ F.StrictLossMatch same b w`, with `b` (the configuration losing `base`) in the *better* slot (*core* `LossMatching.lean` l. 100, 236–247). Probe `lost_side_is_worse`: every claim rests on `false`, configuration `false` loses it, and `true` strictly matches `false`. So a configuration losing the support can be the worse side. Remaining text: rec laws[8] and counterexamples[2] (en, zh); study l. 7240; `LossMatching.lean` l. 28 and l. 237; `RepairComparison.lean` l. 346; the name `fragile_b3_below_nothing` (l. 348). | Records: done in `96812ae6` (law 5's wording, "strictly better by matching than no course" / “经严格匹配不优于任何路线”). Integrator: the same wording in study l. 7240 and the three docstrings; rename `fragile_b3_below_nothing` → `fragile_b3_better_than_none` (§3). |
| G2 | `Copying`; rec inherited-structural-copying | 主张说“相异邻对较多的词汲取较少，当且仅当异类之后的接合汲取较少”，漏了“同长的词中”，等差一句也是。<br>The claim drops "among words of one length" from the ranking law and from the arithmetic-progression law. | error | `use_lt_iff` and `use_midpoint` take `lm : l.length = m.length` (*core* `Copying.lean` l. 664–683; the module doc says "among words of one length"). Probe `longer_word_draws_more`: with `pairDraw 1 2 1`, ABAB (3 unlike pairs) uses 4 and AA (0) uses 3, so the word with more unlike pairs draws more although `differ < same`. The study §115 zh (l. 7448) keeps "同长". | Done in `b4496892`: "among words of one length", "than a like one", and "depends on the law only through its length and unlike adjacent pairs" (`use_word`). |
| G3 | `Substitution`; rec substitution-preserves-consumption (statement, en/zh) | 陈述说“以转化依存的方式持续的消耗者仍是消耗的，恰在损失落在它所转化的依存之外的依存上时”。Lean 的等价只对“在每一种这样的转化下仍消耗”成立。对一次转化，两个方向都可能不成立。<br>The statement's "exactly" holds only for "still consumes under every such transformation". For one transformation, both directions can fail. | overstatement | `Web.consumingIn_kept_iff`: `(∀ V, W.DependenceChanged V f T₀ → V.ConsumingIn f) ↔ W.ConsumingThrough f T₀`. The forward direction instantiates the worst-case `V`, with the own dependence removed from `T₀` (*core* `Substitution.lean` l. 81–92). Probe `one_change_keeps`: moving the lone consumer's dependence from step 0 to step 1 is a `DependenceChanged` with `T₀ = 0`. It keeps consumption, through the moved dependence itself, although `¬ ConsumingThrough () 0`. Law 0 of the record is stated correctly. | Statement: "…still consumes **under every such transformation** exactly where the loss falls on a dependence the transformation leaves…" / “…**在每一种这样的转化下**仍是消耗的，恰当损失落在该转化所留下的依存上时…”. |
| G4 | `Retrodiction`; rec historical-source-binding (claim en/zh); study §115 l. 7501; spine l. 1521 | “区间两端的控制确定其间每个日期，恰当至多允许一次变化或其间无日期”漏了“两端读数相同”。两端不同时，至多一次变化也不能确定其间的日期（`change_unlocated`）。<br>"Controls at both ends settle every date between exactly when…" drops "that read the same". Where the ends differ, one change leaves the dates between unsettled. | overstatement | `bracket_settles_iff` has the antecedent `c (a + n) = c a` and the condition `two : r ≠ r'` (*core* `Retrodiction.lean` l. 255–261). Its docstring says "that returns to its value at `a`"; the record and study drop it. The record's later clause about agreeing prior and following controls uses the right reading. | "controls at both ends of a span **that read the same** settle every date between exactly when at most one change is admitted or no date lies strictly between (where the relation takes two values)" / “区间两端**读数相同**的控制确定其间每个日期，当且仅当至多允许一次变化或其间无日期（关系取两值时）”. |
| G5 | `Countdown`; rec acquired-revision-of-pending-task (first sentence); study English summary l. 9125 | “没有更短的运行完成”由 `pending_before` 引出，但 `Counts` 不使“未完成”与“完成”互斥。需要的是 `not_done_before` 及其条件 `apart`。<br>"No shorter run finishes" is cited to `pending_before`. `Counts` does not make pending and finished exclusive; the theorem needed is `not_done_before`, with its condition `apart`. | overstatement (minor) | Module doc l. 16 and the `pending_before` docstring (l. 186) say "No shorter run finishes", but `pending_before` concludes `busy t ∧ work t + k = work s`. Probe `done_before_without_apart`: a `Counts` with `busy = done = True` is finished after 0 ≤ work ticks. The instances are unaffected: `busy`/`done` in `ProtocolInstances` and `Pending`/`Delivered` in `VersionedTaskInstances` are exclusive by construction. | Docstrings: "**Every shorter run leaves the task pending**"; add "where pending and finished are exclusive, no shorter run finishes (`not_done_before`)". Record: "…and, pending and delivered being exclusive, no shorter run delivers it". |
| G6 | `LossMatching` (`ReadsAt`); rec finite-aggregation law 5; study §112 l. 7240 | “在时刻被读”的两条规律是定义的展开：`ReadsAt` 把 t 时的实现定义为 τ 时的支持，所以“支持恢复后仍失去”写在定义里。实质内容是：一个框架在片段时刻读，是一个前提；读当前支持的框架不是这样读的（`not_readsAt_of_recovery`）。<br>`ReadsAt` defines realization at `t` as support at `τ`, so "stays lost when support returns" is in the definition. The substance is the premise that a frame reads at episode time, plus `not_readsAt_of_recovery`. | presentation | `ReadsAt F r c τ support := ∀ t, τ ≤ t → (F.realized (r.state t) c ↔ support (r.state τ) c)` (l. 447–449). `readsAt_iff_settled` takes `support := F.realized` (l. 459–463). `ReadsAt.loss_retained` is one application of the definition (l. 453–456). | Law 5: "By definition, a frame that reads a claim at its episode time keeps a missed claim missed when support returns; a frame reading current support is not read at that time where support fails and returns (`not_readsAt_of_recovery`). Whether an actual frame reads at episode time is the premise." Cite `not_readsAt_of_recovery` in the declarations. |
| G7 | `RenewalBridge`, `Continuation`; rec supported-renewal-recovery | 支持门控族“是一个平衡流”是构造出来的：焦点形成的取用被定义为这一步的剩余，所以只要 `level_succ_le` 成立，平衡就成立。在任何平衡流中，“一步共同给予多于取用”就是“水平上升”，所以 `surplus_raises_at` 是平衡方程的算术。实质在 `level_succ_le`、`givers_supported` 和族的算术（`repair_restores`）。<br>The family's balance holds by construction: the focal take is defined as the step's residual. Under any balance, joint giving above taking is the level rising. The content is `level_succ_le`, `givers_supported` and the family's arithmetic. | presentation | `flow`'s focal `take t := L.level t + (renewal L t + surplus L t) - L.level (t + 1)` (*core* `RenewalBridge.lean` l. 99–108). `balances` is `add_sub_of_le (level_succ_le L t)` (l. 144–146). Balance is `level (t+1) + taken = level t + given`, so `taken < given ↔ level t < level (t+1)` (`Continuation.lean` l. 236–245). The module doc says "takes what it actually removes", so the construction is disclosed but not marked as such. | Module doc and record: "The focal formation's take is defined as what the step removes, so balance holds by construction wherever the level does not exceed level + renewal + net contribution (`level_succ_le`). The instance's content is that the given amounts are the family's renewal and net contribution, given only where supported (`givers_supported`), and the family arithmetic of `repair_restores`." |
| G8 | `Lasting.exhausts` | 新绑定名 `costs`，文档 “cost one level”。<br>New binder `costs`; docstring "cost one level". | naming | *core* `Lasting.lean` l. 34 (module doc), l. 392 (docstring), l. 401 and l. 410 (binder). The records already say "lowers the level by one" (market-finite-support-obstruction). | Binder `costs` → `lowers`; "cost one level" → "lower the level by one" (§3). |
| G9 | `Continuation`, `RenewalBridge`; rec supported-renewal-recovery; spine l. 1482 | 新名 `surplus`。第十六次审查已让 `surplus_untouched`、`surplus_after_break` 改名（研究 l. 4713），包里已有结构词“净给予”。<br>New `surplus` names. The sixteenth review had `surplus_*` renamed (study l. 4713), and the package already uses "net give". | naming | `Flow.surplus_raises_at`, `Flow.surplus_bounded_at` and binder `surplus` (`Continuation.lean` l. 35, 236–280). `SupportGated.surplus`, `surplus_active`, "joint surplus" (`RenewalBridge.lean` l. 94–215). Record statement and law 0 (en "joint surplus", zh “共同盈余”); spine l. 1482 “共同盈余”. Existing vocabulary: `Flow.Balances.supported_of_net_give`, `admits_of_net_draw` (`Admission.lean` l. 417–500). | `surplus_raises_at` → `net_give_raises_at`; `surplus_bounded_at` → `net_give_bounded_at`; binder `surplus` → `netGive`; `SupportGated.surplus` → `netGive`; `surplus_active` → `netGive_active`; "joint surplus" → "joint net giving"; “共同盈余” → “共同净给予” (§3). |
| G10 | `ProtocolInstances` | 新标题 “Funded completion”，`fuel` 的文档 “can still pay”，新定理名 `charge_some`、`charge_none`。<br>New heading "Funded completion", `fuel` docstring "can still pay", new theorem names `charge_some`, `charge_none`. | naming | *gc* `ProtocolInstances.lean` l. 18, 120, 137, 160, 166; spine l. 1530 "funded completion as counted work"; study English summary l. 9125 "funded publication". `RecoverableControl.charge` and `funded_suffix_publishes` are inherited names and are not judged here. | "Supported completion"; "the units a pending description can still draw"; `charge_some` → `unit_drawn`, `charge_none` → `stalls_unsupported` (§3). |
| G11 | `MarketInstances` | 新文档 “each step costs the stock a unit”。<br>New docstrings "costs the stock a unit". | naming (minor) | `experiments/market-generativity/formal/MarketInstances.lean` l. 27, 199. The binder `cost` mirrors the inherited `RegimeTransition.cover (cost : Rat)` and is not judged here. The record uses "taking one unit of the stock above the floor 5". | "each step takes one unit of the stock above the floor `5`". |

### Confirmed

| id | module / record | finding（中文 / English） | severity | evidence | proposed correction |
|---|---|---|---|---|---|
| C1 | `Stock`; `Revision`; rec selection-under-registration-revision, consequence-revised-reference-plan, recurring-reference-revision | 存量的规律与记录相符；`Revising` 确是登记与存量的乘积。<br>The stock laws match their records; `Revising` is really a product of registration and stock. | confirmed | `covered_iff_prefix` and `product_feasible_iff` are exact. `Revising.step_iff` is a step-for-step equivalence with `productProcess (Stock.process draw restore) registration`, so `feasible_iff` is a genuine instance. `covered_not_enacted` and `linked_not_enacted` show that stock and registration each fail to enact on their own. `MachineInstances.cycles_iff` was checked by hand. | — |
| C2 | `Contacts`; `ReferencePlan` | `blind_misses` 与实例 `frozen_misses` 正确。实例的前提 `frozen_blind` 是定义性的（`fun _ _ => rfl`），这是如实的。`answers_iff`、`stays_iff` 近于定义（薄）。<br>Correct; `frozen_blind` is definitional and honest; `answers_iff` and `stays_iff` are thin. | confirmed | `ReferencePlan.lean` l. 476–482. | — |
| C3 | `LossMatching` | 计数律、`StrictLossMatch.length_lt`（只有非自反与不对称，第 10 项已把记录改为只说所证）、`EndlessLosses` 都正确。<br>The counting law, `StrictLossMatch.length_lt` (irreflexive and asymmetric only; item 10 already narrowed law 3) and `EndlessLosses` are correct. | confirmed | Lean statements against rec laws 0–4. | — |
| C4 | `Assurance`, `Segmentation`, `Readout`, `Gated`, `Instances` | 规律与实例都成立；`Instances` 经规律重述旧定理，而不是另证一遍。<br>The laws and instances hold; `Instances` restates the old theorems through the laws rather than re-proving them. | confirmed | `completes_ofMap_single`, `two_word_iff`, `Gated.kept_along_iff` are exact. `assured_iff_completes`, `chunks_eq`/`encode_eq`, the readout no-decoder theorems, and `rule_kept`/`rule_change_located` are genuine instances. Rec assured-route-criterion, transition-grouping-word-partition, control-coherence-loss and organizational-rule-inheritance match. | — |
| C5 | `Viability`; `MarketInstances` (protection) | 核是最大证书；`needs_admissible` 说明“给定一个可容许扰动”是必要的；市场实例用 `worst_admissible` 满足这一前提。<br>The kernel is the largest certificate; `needs_admissible` shows the admissible-disturbance premise is needed; the market discharges it with `worst_admissible`. | confirmed | `never_fails_iff` against rec market-protected-continuation. `within_not_kernel` is as cited. | — |
| C6 | `Countdown`; `ProtocolInstances`; `VersionedTaskInstances` | 计数工作的 `completes_iff` 是确切的；`counts` 与 `head_advances` 是真实例；`publishes_iff` 确切；预留出口的界可达（`Slow.misses`）。<br>`completes_iff` is exact; `counts` and `head_advances` are genuine instances; `publishes_iff` is exact; the reserved-exit bound is attained. | confirmed | Recs recoverable-mediated-change, reserved-shutdown-during-recovery, versioned-request-completion, acquired-revision-of-pending-task (apart from G5) and pending-task-context-applicability match. `continuation_eq` holds for every condition; `review_losses`/`review_adds_loss_iff` are exact; `losses_kept` is a `Gated.KeptBy` instance. | — |
| C7 | `Lasting`; `MarketInstances` (obstruction, transition, boundary) | 梯子／必要族／漏斗／盆地的等价、永不到达与闭集的等价、`exhausts`、`Collapse.level_not_lasting` 都正确。市场的增益估计是实例自己的内容，已如实写出。<br>The ladder, necessary-family, funnel and basin equivalences, never-reaching iff a closed set, `exhausts` and `Collapse.level_not_lasting` are correct. The market's gain estimates are the instance's own content, and this is disclosed. | confirmed | `forces_failure_instance`, `cover_ladder`/`cover_exact`, `rising_funnel` → `seed_reaches_landing`, `margin_iff` and `fixed_point_instance` give the exact boundary `b ≤ 5/12`. The four market records match. | — |
| C8 | `Copying`; `CopyingInstances` | 除 G2 外，复制的规律都确切；`view_tick` 使机器的每一步成为核心的一步；`lineage_used_iff` 与 `strands_do_not_show_release` 正确。<br>Apart from G2, the copying laws are exact; `view_tick` makes each machine move a core move; `lineage_used_iff` and `strands_do_not_show_release` are correct. | confirmed | `built_iff`, `releases_iff`, `batch_all_iff`, `lineage_all_iff`, `reading_iff`, `inspect_le_iff`, `doubling_iff`. Recs recurrent-chain-assembly, formed-copying-registration and formed-copying-correction match. | — |
| C9 | `Retrodiction`; `RetrodictionInstances` | 除 G4 外正确。`reading_right_iff` 是在报告可判时的逆否（薄）。旧的开放情形确是规律不成立的一侧。<br>Correct apart from G4. `reading_right_iff` is contraposition with decided reports (thin). The old open cases are the failing side, as claimed. | confirmed | `acquire_eq`/`fits_iff` identify the machine's records with the core's. `controls_settle_naming` goes through `bracket`. | — |
| C10 | `CrossSituational`; `MachineInstances` | 正确。`retrospective_resolves_iff` 的覆盖前提 `produced` 很强，记录已写出（hypotheses[1]）。`resolves_explained_iff` 是分离的改写（薄）。<br>Correct. The strong coverage premise `produced` is disclosed in the record (hypotheses[1]). `resolves_explained_iff` is a rewrite of separation (thin). | confirmed | `scene_interprets_every_iff`, `naming_narrows`, `better_iff`, `round_iff` against the §117 records. The Repeated and Omitted counterexamples hold. | — |
| C11 | `Likeness` (at `822b6cfb`); rec determinacy-up-to-likeness, tests-fix-likeness-where-determined, configurations-alike-by-relation | 规律、`Parting`、`OneLoop` 与判定见证都说的是所证。`alike_iff_sameTests` 要求两框架都在相同之下确定，`Choosing` 是反例。<br>The laws, `Parting`, `OneLoop` and the decision witness say what is proved. `alike_iff_sameTests` needs both frames determined up to likeness; `Choosing` is the counterexample. | confirmed | `Histories.lean` l. 289–309; `Likeness.lean` l. 839–852 (at `822b6cfb`). | — |
| C12 | `Learnable`; rec learnable-through-registration, learning-by-refutation | `learnable_iff` 是确切的。充分一侧的学习者被给予世界与目标，“未表明”中已写出。`rests_through` 是对 `held_learner_rests` 的重述（薄）。<br>`learnable_iff` is exact. The sufficient side's learner is given the world and the target, as does_not_show 0 says. `rests_through` restates `held_learner_rests` (thin). | confirmed | `Pair.first_not_rests`; the decidability inventory matches hypotheses[0]. | — |
| C13 | `Joint`, `Substitution`, `Ranking`, `Continuation` (L2) | 除 G3、G7、G9 外，新规律与其反例都正确。<br>Apart from G3, G7 and G9, the new laws and their counterexamples are correct. | confirmed | `differenceOnlyTogether_iff` with `Blocked` and `NeedRises`; `consumingIn_kept_iff` with `Lone`; `renewed_extends_iff` with `ThirdParty.renewal_needed`; `restores_at`, `restores`. | — |
| C14 | `LearnedProcedureTransmission` additions; rec learned-procedure-transmission | `cycle_transmits` 等是这一构造自己的规律，记录限定为“在所述构造中”，不说是核心实例。<br>`cycle_transmits` and the rest are laws of this construction. The record scopes them "in the declared construction" and does not call them core instances. | confirmed | `8cf2161a` diff. | — |

---

## 2. 各模块结论 / Verdict per module

| 模块 / module | 结论 / verdict |
|---|---|
| Stock | 接受 / accept (C1). |
| Contacts | 接受；两条近于定义 / accept; two thin laws (C2). |
| LossMatching | 接受 Lean；改文字 G1、G6 / accept the Lean; fix the text (G1, G6). |
| Assurance, Segmentation, Readout, Gated | 接受 / accept (C4). |
| Viability | 接受 / accept (C5). |
| Countdown | 接受 Lean；文档注释 G5 / accept the Lean; docstrings (G5). |
| Lasting | 接受 Lean；改名 G8 / accept the Lean; rename (G8). |
| Copying | 接受 Lean；记录 G2 已改 / accept the Lean; record fixed (G2). |
| Retrodiction | 接受 Lean；记录与研究 G4 / accept the Lean; record and study (G4). |
| CrossSituational | 接受 / accept (C10). |
| Likeness（822b6cfb 时） | 接受 / accept (C11). 第 120 节的新增不在范围内 / §120 additions not reviewed. |
| Learnable | 接受 / accept (C12). |
| Joint, Ranking | 接受 / accept (C13). |
| Substitution | 接受 Lean；陈述 G3 / accept the Lean; statement (G3). |
| Continuation | 接受 Lean；改名 G9，表述 G7 / accept the Lean; rename (G9), presentation (G7). |
| Instances | 接受 / accept (C4). |
| RenewalBridge | 接受；说明平衡是构造的（G7），改名（G9）/ accept; say the balance is by construction (G7); rename (G9). |
| MachineInstances | 接受 / accept (C1, C10). |
| CopyingInstances | 接受 / accept (C8). |
| ProtocolInstances | 接受；改名 G10 / accept; rename (G10). |
| MarketInstances | 接受；文档 G11 / accept; docstrings (G11). |
| VersionedTaskInstances | 接受 / accept (C6). |
| RetrodictionInstances | 接受 / accept (C9). |
| LearnedProcedureTransmission（新增） | 接受 / accept (C14). |

---

## 3. 改名 / Renames (proposed, old → new; none applied)

Each of these changes a Lean source hash, and some change declarations named in proof bindings. They are proposals for the integrator to batch with the next checker run.

| old | new | where | finding |
|---|---|---|---|
| `RepairComparison.fragile_b3_below_nothing` | `fragile_b3_better_than_none` | *core* `RepairComparison.lean`; rec finite-aggregation laws[8] declarations | G1 |
| binder `costs` (`Lasting.exhausts`) | `lowers` | *core* `Lasting.lean` | G8 |
| `Flow.surplus_raises_at` | `Flow.net_give_raises_at` | *core* `Continuation.lean`; rec supported-renewal-recovery | G9 |
| `Flow.surplus_bounded_at` | `Flow.net_give_bounded_at` | same | G9 |
| binder `surplus` (`Continuation`) | `netGive` | same | G9 |
| `SupportGated.surplus` | `SupportGated.netGive` | *core* `RenewalBridge.lean` | G9 |
| `SupportGated.surplus_active` | `SupportGated.netGive_active` | same | G9 |
| `ProtocolInstances.charge_some` | `ProtocolInstances.unit_drawn` | *gc* `ProtocolInstances.lean` | G10 |
| `ProtocolInstances.charge_none` | `ProtocolInstances.stalls_unsupported` | same | G10 |

Prose, also proposed:
- "cost one level" → "lower the level by one" (G8).
- "joint surplus" / “共同盈余” → "joint net giving" / “共同净给予” (G9).
- "Funded completion" → "Supported completion" and "can still pay" → "can still draw" (G10).
- "costs the stock a unit" → "takes one unit of the stock" (G11).

None of the proposed names is an existing declaration in the package, so there are no clashes. `net_give` occurs only inside the existing `Flow.Balances.supported_of_net_give(_at)`, which the new names are meant to echo.

## 4. 更正提交 / Correction commits

Each commit edits record text only, adds a paired zh/en history note, and regenerates the record page and `_process/architecture/generated-manifest.json` with `research.py render`. `research.py check --ids <id>` reports 0 errors and no drift. No premise, status, dependency, reference, proof binding or source hash changed. The core is untouched, so its axiom reports are unchanged.

| commit | finding | files |
|---|---|---|
| `96812ae6` | G1 | rec finite-aggregation-within-restorable-basic-losses (.json, .md), manifest |
| `b4496892` | G2 | rec inherited-structural-copying (.json, .md), manifest |

These commits did not change the study, the spine or Lean. Each such edit would change hashes that many records bind, and the integrator rebinds after a checker run.

## 5. 一元关系方法 / The nondual method

所审规律都以过程、框架、运行、依存网与流陈述：配置怎样相关、怎样一起变。没有设独立的价值所有者，没有固定的共同效用，也没有伦理谓词。`Joint` 说部分“一起”使出差别，`Substitution` 说消耗经哪一个依存成立，`Retrodiction` 与 `Learnable` 把认识写成记录与配置的关系。这些都从关系出发。`RenewalBridge` 的给予／取用是 `Continuation` 已有的关系词。G7 只要求说明一个取用量是构造出来的，与一元方法无冲突。没有发现分立实体被偷渡进来。

The laws reviewed are stated over processes, frames, runs, dependence webs and flows: how configurations relate and change together. They posit no independent owner of value, no fixed common utility and no ethical predicate.
- `Joint` states parts making a difference *together*.
- `Substitution` locates consumption in a particular dependence.
- `Retrodiction` and `Learnable` state knowing as a relation of records to configurations.

`RenewalBridge`'s give and take use `Continuation`'s existing relational vocabulary. G7 asks only that a constructed take be described as constructed, which does not conflict with the method. No separately posited entity was found.

## 6. 未能检查 / What could not be checked

- **Likeness bridge.** Its additions (study §120, `25cd209a`: `Likeness.lean` +927 lines, `Bridge.lean`) landed after the brief and were not reviewed.
- **Proofs.** Every statement in scope was read, but not every proof. Correctness of unread proofs rests on the checker receipts.
- **Peripheral Mathlib modules.** These were read, not rebuilt.
- **Spine and generated pages.** The spine chapter was sampled by search, and README and other generated pages were not reviewed. More of the G1, G4, G9 and G10 wordings may stand there.
- **Correspondence to actual devices.** Correspondence of the machines to actual devices, authorities, markets or learners is outside the formal scope. The records say so.

## 附录 A. 探针 / Appendix A: probes

`development/becoming-general-laws-review-probes/ReviewProbeGL.lean` (sha256 `29710a3a0708419c0624b1f0609283a06744b9c273e44a5451c8532105c7e3e0`); build output `scratch-build.out.json`.

| probe | finding | statement |
|---|---|---|
| `one_change_keeps` | G3 | `Web.DependenceChanged Lone.web moved () 0 ∧ moved.ConsumingIn () ∧ ¬ Lone.web.ConsumingThrough () 0` |
| `lost_side_is_worse` | G1 | every claim rests on `false`; `false` loses it; `frame.StrictLossMatch (fun _ _ => True) true false` |
| `longer_word_draws_more` | G2 | `use (pairDraw 1 2 1) none [t,f,t,f] = 4`, `use … [t,t] = 3`, unlike pairs 3 and 0 |
| `counts`, `done_before_without_apart` | G5 | a `Counts` with `busy = done = True`; `ticks tick 0 3 = some 3` is already finished |

Axiom reports: all empty (5 theorems, 8 declarations). The module imports only `Becoming.Substitution`, `Becoming.LossMatching`, `Becoming.Countdown` and `Becoming.Copying`, and uses no `propext`, `Classical.choice` or `Quot.sound`.
