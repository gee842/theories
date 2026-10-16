<a id="一般规律的独立审查第十七次-independent-review-of-the-general-laws-seventeenth"></a>
# 一般规律的独立审查（第十七次）

> **中文版（2026-10-17）。** 正典文本是[英文版](BECOMING-GENERAL-LAWS-REVIEW.md)；本版由重构时从双语原文拆出，不与英文同步维护，两者有出入时以英文为准。

2026-10-14，Asia/Bangkok。**AI 独立审查（第十七次；另一 agent，未参与撰写）。** Ren 对开放问题计划第 19 项选了“一个 agent”（`development/becoming-general-laws-plan/OPEN-ISSUES-PLAN.md` §3）。整合会话下达任务，并负责落地。

审查对象
- 2026-10-13 至 14 日加入 Becoming 包的一般规律，状态为 `822b6cfb`（第四批落地后的主线）。
- 核心模块
- 核心模块中的新增
- 桥
- 外围 / Periphery：`MachineInstances`、`CopyingInstances`、`ProtocolInstances`、`MarketInstances`、`VersionedTaskInstances`、`RetrodictionInstances`，以及 `LearnedProcedureTransmission` 的新增。
- 引用它们的记录，研究 `BECOMING-RENEWAL-READING.md` 第 112–119 节。
- 审查期间主线前进到 `25cd209a`（相同之桥，第 120 节）。其中核心只改了 `Likeness.lean` 与 `Bridge.lean`，这两处新增不在本审查范围内。两个更正提交建在 `25cd209a` 上。

严重度
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

<a id="english-summary"></a>

---

<a id="0-范围与方法--scope-and-method"></a>
## 0. 范围与方法

  - `development/becoming-general-laws-plan/PLAN.md`;
  - `OPEN-ISSUES-PLAN.md`;
  - `theories/becoming/chapters/NONDUAL-METHOD.md`.

- `Substitution`: `DependenceChanged`, `ConsumingThrough`, `consumingIn_kept_iff`, `Lone`.
- `Countdown`: `Counts`, `Advances`, `completes_iff`, `pending_before`, `not_done_before`.
- `Retrodiction`: `bracket`, `bracket_settles_iff`, `change_unlocated`.
- `Copying`: `use`, `pairDraw`, `unlikeFrom`, `use_word`, `use_midpoint`, `use_lt_iff`.
- `RenewalBridge`: `surplus`, `flow`, `level_succ_le`, `balances`, `surplus_active`.
- `Revision`: `Revising.step_iff`, `covered_not_enacted`.
- `ReferencePlan`: `frozen_blind`, `frozen_misses`.
- `Gated.kept_along`, `kept_along_iff`.
- `Viability`: `within_not_kernel`, `needs_admissible`.
- `Likeness.alike_decided_iff_em`; `Histories.alike_iff_sameTests`.

- L2:
- §113:
- §§114–116:
- §117:
- §§118–119:

---

<a id="1-发现表--findings-table"></a>
## 1. 发现表

<a id="errors-overstatements-presentation-and-names"></a>

| id | module / record | finding（中文 / English） | severity | evidence | proposed correction |
|---|---|---|---|---|---|
| G1 | `LossMatching`, `RepairComparison`; rec finite-aggregation-within-restorable-basic-losses; study §112 | 说“失去共同支持的配置在任何配置之下都没有严格匹配”，自然读法是：它不是任何严格匹配中较差的一方。Lean 说的是：它不是任何严格匹配中较好的一方。第 10 项只改了定律 5。 | error | `not_strictLossMatch_of_base_lost` concludes `¬ F.StrictLossMatch same b w`, with `b` (the configuration losing `base`) in the *better* slot (*core* `LossMatching.lean` l. 100, 236–247). Probe `lost_side_is_worse`: every claim rests on `false`, configuration `false` loses it, and `true` strictly matches `false`. So a configuration losing the support can be the worse side. Remaining text: rec laws[8] and counterexamples[2] (en, zh); study l. 7240; `LossMatching.lean` l. 28 and l. 237; `RepairComparison.lean` l. 346; the name `fragile_b3_below_nothing` (l. 348). | Records: done in `96812ae6` (law 5's wording, "strictly better by matching than no course" / “经严格匹配不优于任何路线”). Integrator: the same wording in study l. 7240 and the three docstrings; rename `fragile_b3_below_nothing` → `fragile_b3_better_than_none` (§3). |
| G2 | `Copying`; rec inherited-structural-copying | 主张说“相异邻对较多的词汲取较少，当且仅当异类之后的接合汲取较少”，漏了“同长的词中”，等差一句也是。 | error | `use_lt_iff` and `use_midpoint` take `lm : l.length = m.length` (*core* `Copying.lean` l. 664–683; the module doc says "among words of one length"). Probe `longer_word_draws_more`: with `pairDraw 1 2 1`, ABAB (3 unlike pairs) uses 4 and AA (0) uses 3, so the word with more unlike pairs draws more although `differ < same`. The study §115 zh (l. 7448) keeps "同长". | Done in `b4496892`: "among words of one length", "than a like one", and "depends on the law only through its length and unlike adjacent pairs" (`use_word`). |
| G3 | `Substitution`; rec substitution-preserves-consumption (statement, en/zh) | 陈述说“以转化依存的方式持续的消耗者仍是消耗的，恰在损失落在它所转化的依存之外的依存上时”。Lean 的等价只对“在每一种这样的转化下仍消耗”成立。对一次转化，两个方向都可能不成立。 | overstatement | `Web.consumingIn_kept_iff`: `(∀ V, W.DependenceChanged V f T₀ → V.ConsumingIn f) ↔ W.ConsumingThrough f T₀`. The forward direction instantiates the worst-case `V`, with the own dependence removed from `T₀` (*core* `Substitution.lean` l. 81–92). Probe `one_change_keeps`: moving the lone consumer's dependence from step 0 to step 1 is a `DependenceChanged` with `T₀ = 0`. It keeps consumption, through the moved dependence itself, although `¬ ConsumingThrough () 0`. Law 0 of the record is stated correctly. | “…**在每一种这样的转化下**仍是消耗的，恰当损失落在该转化所留下的依存上时…”. |
| G4 | `Retrodiction`; rec historical-source-binding (claim en/zh); study §115 l. 7501; spine l. 1521 | “区间两端的控制确定其间每个日期，恰当至多允许一次变化或其间无日期”漏了“两端读数相同”。两端不同时，至多一次变化也不能确定其间的日期（`change_unlocated`）。 | overstatement | `bracket_settles_iff` has the antecedent `c (a + n) = c a` and the condition `two : r ≠ r'` (*core* `Retrodiction.lean` l. 255–261). Its docstring says "that returns to its value at `a`"; the record and study drop it. The record's later clause about agreeing prior and following controls uses the right reading. | “区间两端**读数相同**的控制确定其间每个日期，当且仅当至多允许一次变化或其间无日期（关系取两值时）”. |
| G5 | `Countdown`; rec acquired-revision-of-pending-task (first sentence); study English summary l. 9125 | “没有更短的运行完成”由 `pending_before` 引出，但 `Counts` 不使“未完成”与“完成”互斥。需要的是 `not_done_before` 及其条件 `apart`。 | overstatement (minor) | Module doc l. 16 and the `pending_before` docstring (l. 186) say "No shorter run finishes", but `pending_before` concludes `busy t ∧ work t + k = work s`. Probe `done_before_without_apart`: a `Counts` with `busy = done = True` is finished after 0 ≤ work ticks. The instances are unaffected: `busy`/`done` in `ProtocolInstances` and `Pending`/`Delivered` in `VersionedTaskInstances` are exclusive by construction. | Docstrings: "**Every shorter run leaves the task pending**"; add "where pending and finished are exclusive, no shorter run finishes (`not_done_before`)". Record: "…and, pending and delivered being exclusive, no shorter run delivers it". |
| G6 | `LossMatching` (`ReadsAt`); rec finite-aggregation law 5; study §112 l. 7240 | “在时刻被读”的两条规律是定义的展开：`ReadsAt` 把 t 时的实现定义为 τ 时的支持，所以“支持恢复后仍失去”写在定义里。实质内容是：一个框架在片段时刻读，是一个前提；读当前支持的框架不是这样读的（`not_readsAt_of_recovery`）。 | presentation | `ReadsAt F r c τ support := ∀ t, τ ≤ t → (F.realized (r.state t) c ↔ support (r.state τ) c)` (l. 447–449). `readsAt_iff_settled` takes `support := F.realized` (l. 459–463). `ReadsAt.loss_retained` is one application of the definition (l. 453–456). | Law 5: "By definition, a frame that reads a claim at its episode time keeps a missed claim missed when support returns; a frame reading current support is not read at that time where support fails and returns (`not_readsAt_of_recovery`). Whether an actual frame reads at episode time is the premise." Cite `not_readsAt_of_recovery` in the declarations. |
| G7 | `RenewalBridge`, `Continuation`; rec supported-renewal-recovery | 支持门控族“是一个平衡流”是构造出来的：焦点形成的取用被定义为这一步的剩余，所以只要 `level_succ_le` 成立，平衡就成立。在任何平衡流中，“一步共同给予多于取用”就是“水平上升”，所以 `surplus_raises_at` 是平衡方程的算术。实质在 `level_succ_le`、`givers_supported` 和族的算术（`repair_restores`）。 | presentation | `flow`'s focal `take t := L.level t + (renewal L t + surplus L t) - L.level (t + 1)` (*core* `RenewalBridge.lean` l. 99–108). `balances` is `add_sub_of_le (level_succ_le L t)` (l. 144–146). Balance is `level (t+1) + taken = level t + given`, so `taken < given ↔ level t < level (t+1)` (`Continuation.lean` l. 236–245). The module doc says "takes what it actually removes", so the construction is disclosed but not marked as such. | Module doc and record: "The focal formation's take is defined as what the step removes, so balance holds by construction wherever the level does not exceed level + renewal + net contribution (`level_succ_le`). The instance's content is that the given amounts are the family's renewal and net contribution, given only where supported (`givers_supported`), and the family arithmetic of `repair_restores`." |
| G8 | `Lasting.exhausts` | 新绑定名 `costs`，文档 “cost one level”。 | naming | *core* `Lasting.lean` l. 34 (module doc), l. 392 (docstring), l. 401 and l. 410 (binder). The records already say "lowers the level by one" (market-finite-support-obstruction). | Binder `costs` → `lowers`; "cost one level" → "lower the level by one" (§3). |
| G9 | `Continuation`, `RenewalBridge`; rec supported-renewal-recovery; spine l. 1482 | 新名 `surplus`。第十六次审查已让 `surplus_untouched`、`surplus_after_break` 改名（研究 l. 4713），包里已有结构词“净给予”。 | naming | `Flow.surplus_raises_at`, `Flow.surplus_bounded_at` and binder `surplus` (`Continuation.lean` l. 35, 236–280). `SupportGated.surplus`, `surplus_active`, "joint surplus" (`RenewalBridge.lean` l. 94–215). Record statement and law 0 (en "joint surplus", zh “共同盈余”); spine l. 1482 “共同盈余”. Existing vocabulary: `Flow.Balances.supported_of_net_give`, `admits_of_net_draw` (`Admission.lean` l. 417–500). | `surplus_raises_at` → `net_give_raises_at`; `surplus_bounded_at` → `net_give_bounded_at`; binder `surplus` → `netGive`; `SupportGated.surplus` → `netGive`; `surplus_active` → `netGive_active`; "joint surplus" → "joint net giving"; “共同盈余” → “共同净给予” (§3). |
| G10 | `ProtocolInstances` | 新标题 “Funded completion”，`fuel` 的文档 “can still pay”，新定理名 `charge_some`、`charge_none`。 | naming | *gc* `ProtocolInstances.lean` l. 18, 120, 137, 160, 166; spine l. 1530 "funded completion as counted work"; study English summary l. 9125 "funded publication". `RecoverableControl.charge` and `funded_suffix_publishes` are inherited names and are not judged here. | "Supported completion"; "the units a pending description can still draw"; `charge_some` → `unit_drawn`, `charge_none` → `stalls_unsupported` (§3). |
| G11 | `MarketInstances` | 新文档 “each step costs the stock a unit”。<br>New docstrings "costs the stock a unit". | naming (minor) | `experiments/market-generativity/formal/MarketInstances.lean` l. 27, 199. The binder `cost` mirrors the inherited `RegimeTransition.cover (cost : Rat)` and is not judged here. The record uses "taking one unit of the stock above the floor 5". | "each step takes one unit of the stock above the floor `5`". |

<a id="confirmed"></a>

| id | module / record | finding（中文 / English） | severity | evidence | proposed correction |
|---|---|---|---|---|---|
| C1 | `Stock`; `Revision`; rec selection-under-registration-revision, consequence-revised-reference-plan, recurring-reference-revision | 存量的规律与记录相符；`Revising` 确是登记与存量的乘积。 | confirmed | `covered_iff_prefix` and `product_feasible_iff` are exact. `Revising.step_iff` is a step-for-step equivalence with `productProcess (Stock.process draw restore) registration`, so `feasible_iff` is a genuine instance. `covered_not_enacted` and `linked_not_enacted` show that stock and registration each fail to enact on their own. `MachineInstances.cycles_iff` was checked by hand. | — |
| C2 | `Contacts`; `ReferencePlan` | `blind_misses` 与实例 `frozen_misses` 正确。实例的前提 `frozen_blind` 是定义性的（`fun _ _ => rfl`），这是如实的。`answers_iff`、`stays_iff` 近于定义（薄）。 | confirmed | `ReferencePlan.lean` l. 476–482. | — |
| C3 | `LossMatching` | 计数律、`StrictLossMatch.length_lt`（只有非自反与不对称，第 10 项已把记录改为只说所证）、`EndlessLosses` 都正确。 | confirmed | Lean statements against rec laws 0–4. | — |
| C4 | `Assurance`, `Segmentation`, `Readout`, `Gated`, `Instances` | 规律与实例都成立；`Instances` 经规律重述旧定理，而不是另证一遍。 | confirmed | `completes_ofMap_single`, `two_word_iff`, `Gated.kept_along_iff` are exact. `assured_iff_completes`, `chunks_eq`/`encode_eq`, the readout no-decoder theorems, and `rule_kept`/`rule_change_located` are genuine instances. Rec assured-route-criterion, transition-grouping-word-partition, control-coherence-loss and organizational-rule-inheritance match. | — |
| C5 | `Viability`; `MarketInstances` (protection) | 核是最大证书；`needs_admissible` 说明“给定一个可容许扰动”是必要的；市场实例用 `worst_admissible` 满足这一前提。 | confirmed | `never_fails_iff` against rec market-protected-continuation. `within_not_kernel` is as cited. | — |
| C6 | `Countdown`; `ProtocolInstances`; `VersionedTaskInstances` | 计数工作的 `completes_iff` 是确切的；`counts` 与 `head_advances` 是真实例；`publishes_iff` 确切；预留出口的界可达（`Slow.misses`）。 | confirmed | Recs recoverable-mediated-change, reserved-shutdown-during-recovery, versioned-request-completion, acquired-revision-of-pending-task (apart from G5) and pending-task-context-applicability match. `continuation_eq` holds for every condition; `review_losses`/`review_adds_loss_iff` are exact; `losses_kept` is a `Gated.KeptBy` instance. | — |
| C7 | `Lasting`; `MarketInstances` (obstruction, transition, boundary) | 梯子／必要族／漏斗／盆地的等价、永不到达与闭集的等价、`exhausts`、`Collapse.level_not_lasting` 都正确。市场的增益估计是实例自己的内容，已如实写出。 | confirmed | `forces_failure_instance`, `cover_ladder`/`cover_exact`, `rising_funnel` → `seed_reaches_landing`, `margin_iff` and `fixed_point_instance` give the exact boundary `b ≤ 5/12`. The four market records match. | — |
| C8 | `Copying`; `CopyingInstances` | 除 G2 外，复制的规律都确切；`view_tick` 使机器的每一步成为核心的一步；`lineage_used_iff` 与 `strands_do_not_show_release` 正确。 | confirmed | `built_iff`, `releases_iff`, `batch_all_iff`, `lineage_all_iff`, `reading_iff`, `inspect_le_iff`, `doubling_iff`. Recs recurrent-chain-assembly, formed-copying-registration and formed-copying-correction match. | — |
| C9 | `Retrodiction`; `RetrodictionInstances` | 除 G4 外正确。`reading_right_iff` 是在报告可判时的逆否（薄）。旧的开放情形确是规律不成立的一侧。 | confirmed | `acquire_eq`/`fits_iff` identify the machine's records with the core's. `controls_settle_naming` goes through `bracket`. | — |
| C10 | `CrossSituational`; `MachineInstances` | 正确。`retrospective_resolves_iff` 的覆盖前提 `produced` 很强，记录已写出（hypotheses[1]）。`resolves_explained_iff` 是分离的改写（薄）。 | confirmed | `scene_interprets_every_iff`, `naming_narrows`, `better_iff`, `round_iff` against the §117 records. The Repeated and Omitted counterexamples hold. | — |
| C11 | `Likeness` (at `822b6cfb`); rec determinacy-up-to-likeness, tests-fix-likeness-where-determined, configurations-alike-by-relation | 规律、`Parting`、`OneLoop` 与判定见证都说的是所证。`alike_iff_sameTests` 要求两框架都在相同之下确定，`Choosing` 是反例。 | confirmed | `Histories.lean` l. 289–309; `Likeness.lean` l. 839–852 (at `822b6cfb`). | — |
| C12 | `Learnable`; rec learnable-through-registration, learning-by-refutation | `learnable_iff` 是确切的。充分一侧的学习者被给予世界与目标，“未表明”中已写出。`rests_through` 是对 `held_learner_rests` 的重述（薄）。 | confirmed | `Pair.first_not_rests`; the decidability inventory matches hypotheses[0]. | — |
| C13 | `Joint`, `Substitution`, `Ranking`, `Continuation` (L2) | 除 G3、G7、G9 外，新规律与其反例都正确。 | confirmed | `differenceOnlyTogether_iff` with `Blocked` and `NeedRises`; `consumingIn_kept_iff` with `Lone`; `renewed_extends_iff` with `ThirdParty.renewal_needed`; `restores_at`, `restores`. | — |
| C14 | `LearnedProcedureTransmission` additions; rec learned-procedure-transmission | `cycle_transmits` 等是这一构造自己的规律，记录限定为“在所述构造中”，不说是核心实例。 | confirmed | `8cf2161a` diff. | — |

---

<a id="2-各模块结论--verdict-per-module"></a>
## 2. 各模块结论

| 模块 | 结论 |
|---|---|
| Stock | 接受 |
| Contacts | 接受；两条近于定义 |
| LossMatching | 接受 Lean；改文字 G1、G6 |
| Assurance, Segmentation, Readout, Gated | 接受 |
| Viability | 接受 |
| Countdown | 接受 Lean；文档注释 G5 |
| Lasting | 接受 Lean；改名 G8 |
| Copying | 接受 Lean；记录 G2 已改 |
| Retrodiction | 接受 Lean；记录与研究 G4 |
| CrossSituational | 接受 |
| Likeness（822b6cfb 时） | 接受 / accept (C11). 第 120 节的新增不在范围内 / §120 additions not reviewed. |
| Learnable | 接受 |
| Joint, Ranking | 接受 |
| Substitution | 接受 Lean；陈述 G3 |
| Continuation | 接受 Lean；改名 G9，表述 G7 |
| Instances | 接受 |
| RenewalBridge | 接受；说明平衡是构造的（G7），改名（G9） |
| MachineInstances | 接受 |
| CopyingInstances | 接受 |
| ProtocolInstances | 接受；改名 G10 |
| MarketInstances | 接受；文档 G11 |
| VersionedTaskInstances | 接受 |
| RetrodictionInstances | 接受 |
| LearnedProcedureTransmission（新增） | 接受 |

---

<a id="3-改名--renames-proposed-old--new-none-applied"></a>
## 3. 改名

<a id="4-更正提交--correction-commits"></a>
## 4. 更正提交

<a id="5-一元关系方法--the-nondual-method"></a>
## 5. 一元关系方法

所审规律都以过程、框架、运行、依存网与流陈述：配置怎样相关、怎样一起变。没有设独立的价值所有者，没有固定的共同效用，也没有伦理谓词。`Joint` 说部分“一起”使出差别，`Substitution` 说消耗经哪一个依存成立，`Retrodiction` 与 `Learnable` 把认识写成记录与配置的关系。这些都从关系出发。`RenewalBridge` 的给予／取用是 `Continuation` 已有的关系词。G7 只要求说明一个取用量是构造出来的，与一元方法无冲突。没有发现分立实体被偷渡进来。

<a id="6-未能检查--what-could-not-be-checked"></a>
## 6. 未能检查

<a id="附录-a-探针--appendix-a-probes"></a>
## 附录 A. 探针
