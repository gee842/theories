<a id="一般规律的独立审查第十七次-independent-review-of-the-general-laws-seventeenth"></a>
# Independent review of the general laws (seventeenth)

> Some passages exist only in the [Chinese edition](BECOMING-GENERAL-LAWS-REVIEW.zh.md): sections “一般规律的独立审查（第十七次）/ Independent review of the general laws (seventeenth)”; “摘要”; “Verdict per module”.

Object:
- Core modules：`Stock`、`Contacts`、`LossMatching`、`Assurance`、`Segmentation`、`Readout`、`Gated`、`Viability`、`Countdown`、`Lasting`、`Copying`、`Retrodiction`、`CrossSituational`、`Likeness`、`Learnable`。
- Additions to core modules：`Joint`、`Substitution`、`Ranking`、`Continuation`（L2，`8cf2161a`）。
- Bridges：`Instances.lean`、`RenewalBridge.lean`。

本审查在自己的 git 工作树中进行。没有运行仓库的 `check_*.py`，没有改动回执、证明绑定或来源哈希，没有编辑 `_process/BECOMING-WORKBOARD.md`。Lean 试验只用 `scratch_build.py`：探针放在仓库外的空目录里构建，构建后复制到 `development/becoming-general-laws-review-probes/`。
The review ran in its own git worktree. No repository `check_*.py` was run, and no receipt, proof binding or source hash was changed. `_process/BECOMING-WORKBOARD.md` was not edited. Lean experiments used only `scratch_build.py`, on a probe built in an empty directory outside the repository and then copied to `development/becoming-general-laws-review-probes/`.

Severity:

---

<a id="摘要"></a>

| 严重度 |
|---|
| error |
| overstatement |
| understatement |
| presentation |
| naming |
| confirmed |

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

<a id="0-范围与方法--scope-and-method"></a>
## 0. Scope and method

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

<a id="1-发现表--findings-table"></a>
## 1. Findings table

Lean line numbers are at `822b6cfb`; they are unchanged at `25cd209a` except in `Likeness.lean`. Study and spine line numbers are at `25cd209a`. Paths are abbreviated as follows:
- *core* = `experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/`
- *gc* = `experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/`
- *rec* = `theories/becoming/results/records/`
- *study* = `BECOMING-RENEWAL-READING.md`
- *spine* = `theories/becoming/chapters/THE-THEORY-OF-BECOMING.md`

### Errors, overstatements, presentation and names

| id | module / record | finding（中文 / English） | severity | evidence | proposed correction |
|---|---|---|---|---|---|
| G1 | `LossMatching`, `RepairComparison`; rec finite-aggregation-within-restorable-basic-losses; study §112 | "Strictly matched below no configuration" reads as "the worse side of no strict match". The Lean says it is the better side of none. Item 10 fixed only law 5. | error | `not_strictLossMatch_of_base_lost` concludes `¬ F.StrictLossMatch same b w`, with `b` (the configuration losing `base`) in the *better* slot (*core* `LossMatching.lean` l. 100, 236–247). Probe `lost_side_is_worse`: every claim rests on `false`, configuration `false` loses it, and `true` strictly matches `false`. So a configuration losing the support can be the worse side. Remaining text: rec laws[8] and counterexamples[2] (en, zh); study l. 7240; `LossMatching.lean` l. 28 and l. 237; `RepairComparison.lean` l. 346; the name `fragile_b3_below_nothing` (l. 348). | Records: done in `96812ae6` (law 5's wording, "strictly better by matching than no course" / “经严格匹配不优于任何路线”). Integrator: the same wording in study l. 7240 and the three docstrings; rename `fragile_b3_below_nothing` → `fragile_b3_better_than_none` (§3). |
| G2 | `Copying`; rec inherited-structural-copying | The claim drops "among words of one length" from the ranking law and from the arithmetic-progression law. | error | `use_lt_iff` and `use_midpoint` take `lm : l.length = m.length` (*core* `Copying.lean` l. 664–683; the module doc says "among words of one length"). Probe `longer_word_draws_more`: with `pairDraw 1 2 1`, ABAB (3 unlike pairs) uses 4 and AA (0) uses 3, so the word with more unlike pairs draws more although `differ < same`. The study §115 zh (l. 7448) keeps "同长". | Done in `b4496892`: "among words of one length", "than a like one", and "depends on the law only through its length and unlike adjacent pairs" (`use_word`). |
| G3 | `Substitution`; rec substitution-preserves-consumption (statement, en/zh) | The statement's "exactly" holds only for "still consumes under every such transformation". For one transformation, both directions can fail. | overstatement | `Web.consumingIn_kept_iff`: `(∀ V, W.DependenceChanged V f T₀ → V.ConsumingIn f) ↔ W.ConsumingThrough f T₀`. The forward direction instantiates the worst-case `V`, with the own dependence removed from `T₀` (*core* `Substitution.lean` l. 81–92). Probe `one_change_keeps`: moving the lone consumer's dependence from step 0 to step 1 is a `DependenceChanged` with `T₀ = 0`. It keeps consumption, through the moved dependence itself, although `¬ ConsumingThrough () 0`. Law 0 of the record is stated correctly. | Statement: "…still consumes **under every such transformation** exactly where the loss falls on a dependence the transformation leaves…" |
| G4 | `Retrodiction`; rec historical-source-binding (claim en/zh); study §115 l. 7501; spine l. 1521 | "Controls at both ends settle every date between exactly when…" drops "that read the same". Where the ends differ, one change leaves the dates between unsettled. | overstatement | `bracket_settles_iff` has the antecedent `c (a + n) = c a` and the condition `two : r ≠ r'` (*core* `Retrodiction.lean` l. 255–261). Its docstring says "that returns to its value at `a`"; the record and study drop it. The record's later clause about agreeing prior and following controls uses the right reading. | "controls at both ends of a span **that read the same** settle every date between exactly when at most one change is admitted or no date lies strictly between (where the relation takes two values)" |
| G5 | `Countdown`; rec acquired-revision-of-pending-task (first sentence); study English summary l. 9125 | "No shorter run finishes" is cited to `pending_before`. `Counts` does not make pending and finished exclusive; the theorem needed is `not_done_before`, with its condition `apart`. | overstatement (minor) | Module doc l. 16 and the `pending_before` docstring (l. 186) say "No shorter run finishes", but `pending_before` concludes `busy t ∧ work t + k = work s`. Probe `done_before_without_apart`: a `Counts` with `busy = done = True` is finished after 0 ≤ work ticks. The instances are unaffected: `busy`/`done` in `ProtocolInstances` and `Pending`/`Delivered` in `VersionedTaskInstances` are exclusive by construction. | Docstrings: "**Every shorter run leaves the task pending**"; add "where pending and finished are exclusive, no shorter run finishes (`not_done_before`)". Record: "…and, pending and delivered being exclusive, no shorter run delivers it". |
| G6 | `LossMatching` (`ReadsAt`); rec finite-aggregation law 5; study §112 l. 7240 | `ReadsAt` defines realization at `t` as support at `τ`, so "stays lost when support returns" is in the definition. The substance is the premise that a frame reads at episode time, plus `not_readsAt_of_recovery`. | presentation | `ReadsAt F r c τ support := ∀ t, τ ≤ t → (F.realized (r.state t) c ↔ support (r.state τ) c)` (l. 447–449). `readsAt_iff_settled` takes `support := F.realized` (l. 459–463). `ReadsAt.loss_retained` is one application of the definition (l. 453–456). | Law 5: "By definition, a frame that reads a claim at its episode time keeps a missed claim missed when support returns; a frame reading current support is not read at that time where support fails and returns (`not_readsAt_of_recovery`). Whether an actual frame reads at episode time is the premise." Cite `not_readsAt_of_recovery` in the declarations. |
| G7 | `RenewalBridge`, `Continuation`; rec supported-renewal-recovery | The family's balance holds by construction: the focal take is defined as the step's residual. Under any balance, joint giving above taking is the level rising. The content is `level_succ_le`, `givers_supported` and the family's arithmetic. | presentation | `flow`'s focal `take t := L.level t + (renewal L t + surplus L t) - L.level (t + 1)` (*core* `RenewalBridge.lean` l. 99–108). `balances` is `add_sub_of_le (level_succ_le L t)` (l. 144–146). Balance is `level (t+1) + taken = level t + given`, so `taken < given ↔ level t < level (t+1)` (`Continuation.lean` l. 236–245). The module doc says "takes what it actually removes", so the construction is disclosed but not marked as such. | Module doc and record: "The focal formation's take is defined as what the step removes, so balance holds by construction wherever the level does not exceed level + renewal + net contribution (`level_succ_le`). The instance's content is that the given amounts are the family's renewal and net contribution, given only where supported (`givers_supported`), and the family arithmetic of `repair_restores`." |
| G8 | `Lasting.exhausts` | New binder `costs`; docstring "cost one level". | naming | *core* `Lasting.lean` l. 34 (module doc), l. 392 (docstring), l. 401 and l. 410 (binder). The records already say "lowers the level by one" (market-finite-support-obstruction). | Binder `costs` → `lowers`; "cost one level" → "lower the level by one" (§3). |
| G9 | `Continuation`, `RenewalBridge`; rec supported-renewal-recovery; spine l. 1482 | New `surplus` names. The sixteenth review had `surplus_*` renamed (study l. 4713), and the package already uses "net give". | naming | `Flow.surplus_raises_at`, `Flow.surplus_bounded_at` and binder `surplus` (`Continuation.lean` l. 35, 236–280). `SupportGated.surplus`, `surplus_active`, "joint surplus" (`RenewalBridge.lean` l. 94–215). Record statement and law 0 (en "joint surplus", zh “共同盈余”); spine l. 1482 “共同盈余”. Existing vocabulary: `Flow.Balances.supported_of_net_give`, `admits_of_net_draw` (`Admission.lean` l. 417–500). | `surplus_raises_at` → `net_give_raises_at`; `surplus_bounded_at` → `net_give_bounded_at`; binder `surplus` → `netGive`; `SupportGated.surplus` → `netGive`; `surplus_active` → `netGive_active`; "joint surplus" → "joint net giving"; “共同盈余” → “共同净给予” (§3). |
| G10 | `ProtocolInstances` | New heading "Funded completion", `fuel` docstring "can still pay", new theorem names `charge_some`, `charge_none`. | naming | *gc* `ProtocolInstances.lean` l. 18, 120, 137, 160, 166; spine l. 1530 "funded completion as counted work"; study English summary l. 9125 "funded publication". `RecoverableControl.charge` and `funded_suffix_publishes` are inherited names and are not judged here. | "Supported completion"; "the units a pending description can still draw"; `charge_some` → `unit_drawn`, `charge_none` → `stalls_unsupported` (§3). |
| G11 | `MarketInstances` | 新文档 “each step costs the stock a unit”。<br>New docstrings "costs the stock a unit". | naming (minor) | `experiments/market-generativity/formal/MarketInstances.lean` l. 27, 199. The binder `cost` mirrors the inherited `RegimeTransition.cover (cost : Rat)` and is not judged here. The record uses "taking one unit of the stock above the floor 5". | "each step takes one unit of the stock above the floor `5`". |

### Confirmed

| id | module / record | finding（中文 / English） | severity | evidence | proposed correction |
|---|---|---|---|---|---|
| C1 | `Stock`; `Revision`; rec selection-under-registration-revision, consequence-revised-reference-plan, recurring-reference-revision | The stock laws match their records; `Revising` is really a product of registration and stock. | confirmed | `covered_iff_prefix` and `product_feasible_iff` are exact. `Revising.step_iff` is a step-for-step equivalence with `productProcess (Stock.process draw restore) registration`, so `feasible_iff` is a genuine instance. `covered_not_enacted` and `linked_not_enacted` show that stock and registration each fail to enact on their own. `MachineInstances.cycles_iff` was checked by hand. | — |
| C2 | `Contacts`; `ReferencePlan` | Correct; `frozen_blind` is definitional and honest; `answers_iff` and `stays_iff` are thin. | confirmed | `ReferencePlan.lean` l. 476–482. | — |
| C3 | `LossMatching` | The counting law, `StrictLossMatch.length_lt` (irreflexive and asymmetric only; item 10 already narrowed law 3) and `EndlessLosses` are correct. | confirmed | Lean statements against rec laws 0–4. | — |
| C4 | `Assurance`, `Segmentation`, `Readout`, `Gated`, `Instances` | The laws and instances hold; `Instances` restates the old theorems through the laws rather than re-proving them. | confirmed | `completes_ofMap_single`, `two_word_iff`, `Gated.kept_along_iff` are exact. `assured_iff_completes`, `chunks_eq`/`encode_eq`, the readout no-decoder theorems, and `rule_kept`/`rule_change_located` are genuine instances. Rec assured-route-criterion, transition-grouping-word-partition, control-coherence-loss and organizational-rule-inheritance match. | — |
| C5 | `Viability`; `MarketInstances` (protection) | The kernel is the largest certificate; `needs_admissible` shows the admissible-disturbance premise is needed; the market discharges it with `worst_admissible`. | confirmed | `never_fails_iff` against rec market-protected-continuation. `within_not_kernel` is as cited. | — |
| C6 | `Countdown`; `ProtocolInstances`; `VersionedTaskInstances` | `completes_iff` is exact; `counts` and `head_advances` are genuine instances; `publishes_iff` is exact; the reserved-exit bound is attained. | confirmed | Recs recoverable-mediated-change, reserved-shutdown-during-recovery, versioned-request-completion, acquired-revision-of-pending-task (apart from G5) and pending-task-context-applicability match. `continuation_eq` holds for every condition; `review_losses`/`review_adds_loss_iff` are exact; `losses_kept` is a `Gated.KeptBy` instance. | — |
| C7 | `Lasting`; `MarketInstances` (obstruction, transition, boundary) | The ladder, necessary-family, funnel and basin equivalences, never-reaching iff a closed set, `exhausts` and `Collapse.level_not_lasting` are correct. The market's gain estimates are the instance's own content, and this is disclosed. | confirmed | `forces_failure_instance`, `cover_ladder`/`cover_exact`, `rising_funnel` → `seed_reaches_landing`, `margin_iff` and `fixed_point_instance` give the exact boundary `b ≤ 5/12`. The four market records match. | — |
| C8 | `Copying`; `CopyingInstances` | Apart from G2, the copying laws are exact; `view_tick` makes each machine move a core move; `lineage_used_iff` and `strands_do_not_show_release` are correct. | confirmed | `built_iff`, `releases_iff`, `batch_all_iff`, `lineage_all_iff`, `reading_iff`, `inspect_le_iff`, `doubling_iff`. Recs recurrent-chain-assembly, formed-copying-registration and formed-copying-correction match. | — |
| C9 | `Retrodiction`; `RetrodictionInstances` | Correct apart from G4. `reading_right_iff` is contraposition with decided reports (thin). The old open cases are the failing side, as claimed. | confirmed | `acquire_eq`/`fits_iff` identify the machine's records with the core's. `controls_settle_naming` goes through `bracket`. | — |
| C10 | `CrossSituational`; `MachineInstances` | Correct. The strong coverage premise `produced` is disclosed in the record (hypotheses[1]). `resolves_explained_iff` is a rewrite of separation (thin). | confirmed | `scene_interprets_every_iff`, `naming_narrows`, `better_iff`, `round_iff` against the §117 records. The Repeated and Omitted counterexamples hold. | — |
| C11 | `Likeness` (at `822b6cfb`); rec determinacy-up-to-likeness, tests-fix-likeness-where-determined, configurations-alike-by-relation | The laws, `Parting`, `OneLoop` and the decision witness say what is proved. `alike_iff_sameTests` needs both frames determined up to likeness; `Choosing` is the counterexample. | confirmed | `Histories.lean` l. 289–309; `Likeness.lean` l. 839–852 (at `822b6cfb`). | — |
| C12 | `Learnable`; rec learnable-through-registration, learning-by-refutation | `learnable_iff` is exact. The sufficient side's learner is given the world and the target, as does_not_show 0 says. `rests_through` restates `held_learner_rests` (thin). | confirmed | `Pair.first_not_rests`; the decidability inventory matches hypotheses[0]. | — |
| C13 | `Joint`, `Substitution`, `Ranking`, `Continuation` (L2) | Apart from G3, G7 and G9, the new laws and their counterexamples are correct. | confirmed | `differenceOnlyTogether_iff` with `Blocked` and `NeedRises`; `consumingIn_kept_iff` with `Lone`; `renewed_extends_iff` with `ThirdParty.renewal_needed`; `restores_at`, `restores`. | — |
| C14 | `LearnedProcedureTransmission` additions; rec learned-procedure-transmission | `cycle_transmits` and the rest are laws of this construction. The record scopes them "in the declared construction" and does not call them core instances. | confirmed | `8cf2161a` diff. | — |

---

<a id="2-各模块结论--verdict-per-module"></a>
## 2. Verdict per module

| module | verdict |
|---|---|
| Stock | accept (C1). |
| Contacts | accept; two thin laws (C2). |
| LossMatching | accept the Lean; fix the text (G1, G6). |
| Assurance, Segmentation, Readout, Gated | accept (C4). |
| Viability | accept (C5). |
| Countdown | accept the Lean; docstrings (G5). |
| Lasting | accept the Lean; rename (G8). |
| Copying | accept the Lean; record fixed (G2). |
| Retrodiction | accept the Lean; record and study (G4). |
| CrossSituational | accept (C10). |
| Likeness（822b6cfb 时） | 接受 / accept (C11). 第 120 节的新增不在范围内 / §120 additions not reviewed. |
| Learnable | accept (C12). |
| Joint, Ranking | accept (C13). |
| Substitution | accept the Lean; statement (G3). |
| Continuation | accept the Lean; rename (G9), presentation (G7). |
| Instances | accept (C4). |
| RenewalBridge | accept; say the balance is by construction (G7); rename (G9). |
| MachineInstances | accept (C1, C10). |
| CopyingInstances | accept (C8). |
| ProtocolInstances | accept; rename (G10). |
| MarketInstances | accept; docstrings (G11). |
| VersionedTaskInstances | accept (C6). |
| RetrodictionInstances | accept (C9). |
| LearnedProcedureTransmission（新增） | accept (C14). |

---

<a id="3-改名--renames-proposed-old--new-none-applied"></a>
## 3. Renames (proposed, old → new; none applied)

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

<a id="4-更正提交--correction-commits"></a>
## 4. Correction commits

Each commit edits record text only, adds a paired zh/en history note, and regenerates the record page and `_process/architecture/generated-manifest.json` with `research.py render`. `research.py check --ids <id>` reports 0 errors and no drift. No premise, status, dependency, reference, proof binding or source hash changed. The core is untouched, so its axiom reports are unchanged.

| commit | finding | files |
|---|---|---|
| `96812ae6` | G1 | rec finite-aggregation-within-restorable-basic-losses (.json, .md), manifest |
| `b4496892` | G2 | rec inherited-structural-copying (.json, .md), manifest |

These commits did not change the study, the spine or Lean. Each such edit would change hashes that many records bind, and the integrator rebinds after a checker run.

<a id="5-一元关系方法--the-nondual-method"></a>
## 5. The nondual method

The laws reviewed are stated over processes, frames, runs, dependence webs and flows: how configurations relate and change together. They posit no independent owner of value, no fixed common utility and no ethical predicate.
- `Joint` states parts making a difference *together*.
- `Substitution` locates consumption in a particular dependence.
- `Retrodiction` and `Learnable` state knowing as a relation of records to configurations.

`RenewalBridge`'s give and take use `Continuation`'s existing relational vocabulary. G7 asks only that a constructed take be described as constructed, which does not conflict with the method. No separately posited entity was found.

<a id="6-未能检查--what-could-not-be-checked"></a>
## 6. What could not be checked

- **Likeness bridge.** Its additions (study §120, `25cd209a`: `Likeness.lean` +927 lines, `Bridge.lean`) landed after the brief and were not reviewed.
- **Proofs.** Every statement in scope was read, but not every proof. Correctness of unread proofs rests on the checker receipts.
- **Peripheral Mathlib modules.** These were read, not rebuilt.
- **Spine and generated pages.** The spine chapter was sampled by search, and README and other generated pages were not reviewed. More of the G1, G4, G9 and G10 wordings may stand there.
- **Correspondence to actual devices.** Correspondence of the machines to actual devices, authorities, markets or learners is outside the formal scope. The records say so.

<a id="附录-a-探针--appendix-a-probes"></a>
## Appendix A: probes

`development/becoming-general-laws-review-probes/ReviewProbeGL.lean` (sha256 `29710a3a0708419c0624b1f0609283a06744b9c273e44a5451c8532105c7e3e0`); build output `scratch-build.out.json`.

| probe | finding | statement |
|---|---|---|
| `one_change_keeps` | G3 | `Web.DependenceChanged Lone.web moved () 0 ∧ moved.ConsumingIn () ∧ ¬ Lone.web.ConsumingThrough () 0` |
| `lost_side_is_worse` | G1 | every claim rests on `false`; `false` loses it; `frame.StrictLossMatch (fun _ _ => True) true false` |
| `longer_word_draws_more` | G2 | `use (pairDraw 1 2 1) none [t,f,t,f] = 4`, `use … [t,t] = 3`, unlike pairs 3 and 0 |
| `counts`, `done_before_without_apart` | G5 | a `Counts` with `busy = done = True`; `ticks tick 0 3 = some 3` is already finished |

Axiom reports: all empty (5 theorems, 8 declarations). The module imports only `Becoming.Substitution`, `Becoming.LossMatching`, `Becoming.Countdown` and `Becoming.Copying`, and uses no `propext`, `Classical.choice` or `Quot.sound`.
