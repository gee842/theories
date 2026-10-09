# P7 与“侵蚀”更正的独立审查 / Independent review of P7 and of the undermining correction

2026-10-09, Asia/Bangkok. **Independent AI review by a separate agent (Claude Opus 5.5) that did not write the work under review.** It was requested within Ren's continuing instruction to pursue the Theory of Becoming and "prove the necessary proofs" ([source](../../../../sources/15-codex-theory-conversations/2026-10-09-pure-core.md#rens-follow-up-finish-the-renames-then-continue-the-theory)). This file is the only repository file the reviewer created or changed. No repository checker was run and nothing was committed.

## 0. Scope, materials and method

**Object.** P7 as committed in `278de821`:

- study [BECOMING-RENEWAL-READING](BECOMING-RENEWAL-READING.md) §8 (8.1–8.7) and its English summary, together with the §7.1 correction that adopted "not undermining" as the stepwise `living`;
- Lean: [Becoming.Return](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Return.lean), [Becoming.Horizon](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Horizon.lean), [Becoming.Joint](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Joint.lean), [Becoming.Substitution](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Substitution.lean), and the stepwise parts of [Becoming.Dependence](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Dependence.lean) and [Becoming.Metaethics](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Metaethics.lean);
- records becoming-return-grades, becoming-finite-horizon, joint-difference-making, substitution-preserves-consumption, becoming-stepwise-reading, becoming-dependence-dynamics (JSON);
- canonical chapter [THE-THEORY-OF-BECOMING](../../../../theories/becoming/chapters/THE-THEORY-OF-BECOMING.md) §§0, 1, 2, 4, 6.3, 8, 9, 10.

**A concurrent commit.** While this review was in progress, another session committed P8 (`7103b4e1`): `Becoming.Ranking`, record ranking-under-readings, and a new study §9. It replaced the unproved "cost" paragraph of §8.5 with a proof and re-pointed the P7 records to a new receipt without changing their claims (each record's history says so). Every finding below is stated against `278de821` and still applies at `7103b4e1` unless marked. `Becoming.Ranking` was read only as far as it bears on question 4; it is not reviewed here.

| File | sha256 at `278de821` | sha256 at `7103b4e1` |
|---|---|---|
| study | `1d688e486e43dc44…` | `c216517f8f3f4069…` |
| chapter | `f6bf597a812ea0f8…` | `b60f5cd100781fb0…` |
| receipt | `91d752e46064bf0a…` (`20261009T002925.265132Z`) | `3f9d093aefb63002…` (`20261009T005555.457210Z`) |
| Dependence / Return / Horizon / Joint / Substitution / Metaethics | `b9a5e970…` / `b036d18a…` / `3ee4f914…` / `8513d13f…` / `2355d189…` / `df97cd99…` | unchanged |

**Read in full:** [AGENTS.md](../../../../AGENTS.md); study §§7–8 and the English summary (§§1–6 for context); the [earlier independent review](BECOMING-RENEWAL-READING-REVIEW.md), for criteria (a)–(e) and probe method; the six Lean modules above, `Becoming.Renewal`, `RelationalRenewal` (the `Law` family) and `RenewalComparison`; the six record JSONs; the chapter sections listed. **Ren's words read:** [以关系结构分开更新型与消耗型形成](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md), for the provenance of criterion (a). **No external literature was newly read.**

**Recompilation.** In a scratch directory outside the repository, the `278de821` bytes of `GenerativeCore` (with `import Std` removed), `InquirySufficiency`, `RelationalRenewal` and `Becoming/{Frame, Inquiry, Renewal, Dependence, Return, Horizon, Joint, Substitution, Metaethics}` were compiled in dependency order with Lean 4.29.1 (commit `f72c35b3`). All 12 exit 0 from the prelude. Source hashes equal the receipt's. `#print axioms` on 24 named P7 and §7 declarations (among them `consumed_iff`, `RenewingIn.within_one`, `prefix_does_not_decide`, `finite_reading_credits_consumption`, `Overdetermined.no_difference`, `Pool.difference_belongs_to_the_joint`, `depletion_is_joint`, `persists_consuming`, `drawing_after_loss`, `readings_differ`) reports no axioms. Theorem counts by `^theorem`: Return 26, Horizon 2, Joint 12, Substitution 4, Dependence 35, Metaethics 35, as recorded; the total of 169 at `278de821` matches the chapter.

**Probes.** Two files, reproduced in the appendix: `P7Probes.lean` (sha256 `1f829dd1a991b085…`) and `P7Feedback.lean` (`43da4d375ba71841…`). Both import the unchanged core and compile with exit 0. All 23 audited probe declarations report "does not depend on any axioms". Two core lemmas, `Nat.le_of_add_le_add_right` and `Nat.add_right_cancel`, depend on `propext` in 4.29.1, so the probe proves local replacements. The probes are minimal models that satisfy the published definitions unchanged. Following the [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md), they show what the definitions admit, not what actual systems usually do. Where a fuller account would exclude a probe, the relation that excludes it is what the representation omits; it is not a refutation of the theory.

**Severity labels.** *error*: a definition does not match its stated meaning, or a stated claim is false of the definitions. *overclaim*: prose stronger than the Lean. *missing counterexample*: a relevant witness absent from the comparison or record. *presentation*: wording, provenance or bookkeeping.

## 1. Verdicts

| Question | Verdict | Findings |
|---|---|---|
| 1. Do the Lean statements prove what the prose says? | **The Lean is accepted.** All P7 theorems recompile without axioms and are correct as stated. The mismatches are in definition docstrings and in prose, which overclaims in seven places: never-met requirements, (a)/(c) conflict, "the rest as it was", joint depletion, "renewal is renewal within one", finite decidability of cycle readings, and substitution "preserves". | F1, F2, F3, F6, F7, F8, F9 |
| 2. Are the definitions good formalizations? | **`UnderminingOn` and `UnderminingFor` need repair.** "Met then or before" compares the current need with any past level, whether or not the dependence existed then. The reading ties an event to any unrestored shortfall on what it draws, not to what its draw does. **`MakesDifference` and `Overdetermined` hold the state fixed but not the move**, so an exogenous move decides them. `ReturnsWithin` is sound, but `RenewedWithin 1` is strictly weaker than `Renewed`. The horizon notion is sound for run-level readings. | F1, F4, F5, F6, F8, F10 |
| 3. Is the Horizon result correctly interpreted? | **The theorem is correct, and it transfers unchanged to the support-gated law with feedback (probe).** The claimed conflict between (a) and (c) holds only if Ren's verdict is read as "agree with the whole-run classification on every renewing run". The whole-run reading itself credits drawing beyond renewal in the run that stops. A per-step amount reading is finitely decidable and withholds every overdraw. The conflict is an artifact of that reading of (a) and of amount-free observables, not of missing feedback. | F2 |
| 4. Is §8.5 fair, and is the split labelled and its cost right? | **The table is partly unfair:** (a) for the whole-run and stepwise columns, (b) for the stepwise, cycle and relation columns, and the but-for column. **The split is clearly labelled** as an AI argument not confirmed by Ren. **The stated cost is correct but conditional:** it needs a credited event before the loss. P8 now proves it under that hypothesis and finds that the sharing-over-winning ranking survives, which the committed paragraph did not anticipate. | F2, F3, F4, F7; §3 |
| 5. Records | **Counts are correct.** Five claims or hypotheses need correcting; one `related` sentence is false as stated. | F15 |
| 6. AGENTS.md | **No ethical predicate in the Lean definitions,** and nothing argued is called proved. **The provenance of criterion (a)** and the word "adopted" (采用) for a reading the study says Ren chooses need correcting. | F11 |

## 2. Findings

### F1. error: `UnderminingOn` does not formalize "a dependence on it, met then or before"

**Location.**

- `Becoming.Dependence`: the definition and docstring of `Web.UnderminingOn`, and module doc lines 56–57 ("A requirement never met makes no drawer undermining").
- `Becoming.Return`: `UnderminingFor`, which has the same clause.
- Study §7.1: the "不侵蚀（采用）" row ("不受从未被满足的依存影响") and the English summary ("ignores never-met requirements").
- Chapter §2, the bullet "不受从未被满足的依存影响".
- Record becoming-stepwise-reading, `claim` ("a requirement never met makes no event undermine").

**What the Lean says.** The clause is `∃ s, s ≤ t ∧ W.need t g c ≤ W.level s c`. It compares the need *at t* with the level at some earlier `s`. It does not require that `g` depended on `c` at `s` (`requires s g c`), nor that the need was the same then.

**Evidence.** Probe `NewNeed.undermining_without_met_dependence`. The web is `Dependent`. The level is 2 at step 0 and 0 thereafter. A formation `late` depends on the condition at need 1 only from step 5 on: unmet at every step at which it holds, never `Broken`, never active. A drawer draws from step 5. Then every drawer event from step 5 undermines, so the stepwise reading credits none. The general claim is false; Lean supports only the special case `Unmet.consumed_without_loss`, whose level is below the need at every step.

**Why it matters.** It is what the §7.1 choice was meant to fix: review Q2 was that a never-met requirement voids participants. In an actual history, a newly arrived dependent whose need the condition met only long ago, before a decline nobody drew, voids every current drawer from its arrival on.

**Correction.** Either redefine, or narrow the prose.

- *Redefine:* `∃ s ≤ t, W.requires s g c ∧ W.need s g c ≤ W.level s c`, with the dependence holding from `s` to `t` and `W.need t g c ≤ W.need s g c`. The existing witnesses (`BreakingOn.undermining`, `drawing_after_loss`, `readings_differ`, `Unmet`, `Mixed`) have constant needs and should re-prove unchanged.
- *Narrow:* "a requirement whose present need exceeds every level up to the step makes no drawer undermining".

Apply the same to `UnderminingFor` and to `Web.relations`.

### F2. overclaim: the conflict between (a) and (c) rests on one reading of (a) and on amount-free observables, not on missing feedback

**Location.**

- Study §8.5, constraint 1 ("(a) 与 (c) 在渐进耗竭上冲突 … 所以没有一种可由有限历史判定的事件读法能扣下渐进耗竭的全部事件"); its second sentence drops the hypothesis "不扣下更新运行".
- Study §8.2 interpretation and §8.6, response 3.
- Chapter §6.3 ("符合 Ren 有来源的判决与可由有限探究判定，在渐进耗竭上冲突").
- English summary.
- Record becoming-finite-horizon: `related[0]` ("any event reading decidable from a finite history credits some events of a gradual depletion") and `correspondence` ("not proved" with feedback).

**What the Lean proves.** `finite_reading_credits_consumption` is correct: a run-level reading fixed by the first `h` steps that credits every whole-run-renewing run credits some consuming run. The work is done by the hypothesis "credits every renewing run". In `prefix_does_not_decide`, the renewing run itself draws two units, one beyond renewal, at every step before `h`, from a stock that absorbs it.

**Evidence.**

- *The whole-run reading credits overdraw.* `HorizonProbe.whole_run_credits_overdraw`: for every `h`, that renewing run draws two units at every step before `h`, and `Conditions.valuation` credits every one of those focal events. If Ren's verdict is about the activity of winning by consumption, drawing beyond renewal, the whole-run reading fails it too. The table's "是" for the whole-run column under (a) presupposes that the verdict concerns the eventual outcome.
- *A finitely decidable reading escapes.* `HorizonProbe.amount_reading`: "draws no more than is renewed at this step" (`act t ≤ 1` in the commons) is fixed by the first `t + 1` steps, credits every event of `sharing`, and withholds every event before `h` in both runs of `prefix_does_not_decide`. It escapes the theorem only by not crediting every whole-run-renewing run. So the record's `related[0]` and the study's "所以…" sentence are false as stated. Such a reading cannot be expressed on `Web`, because `draws` carries no amount and a web has no renewal rate.
- *Feedback is not the issue.* `Feedback.prefix_does_not_decide_with_feedback`: in `RelationalRenewal.Law` with start `h+1`, renewal 1, `needG = 1`, `needF = 0` and no contribution, the schedule drawing 2 before `h` and 1 after renews, and drawing 2 throughout consumes. The draws agree before `h` and the start is the same. The renewing schedule never reaches the threshold, so `no_return_below_support` never acts. This answers §8.6 response 3 and the record's "not proved".
- *Unknown action, not unknown dynamics.* In the commons the dynamics are deterministic given the actions. What no prefix decides is the future action. "需要对继续的探究" therefore partly means deliberating about what will be done. A conditional reading, "continuing this step's draw would consume", is decidable from the state and the law in all these witnesses. This point is an argument, not formalized.

**Correction.** Restate constraint 1 as: "Any reading fixed by a finite prefix that credits every run the whole-run reading classifies as renewing credits some run it classifies as consuming."

- Say that whether Ren's verdict requires the whole-run classification of pre-threshold events is interpretive (see F11).
- Add the amount-sensitive and conditional readings as rivals, with the observables they need.
- Delete or qualify the "所以…" sentence and record `related[0]`.
- Update the record's `correspondence` and `limitations` with the feedback result.

### F3. missing counterexample: after substitution, the stepwise reading credits the consumer

**Location.**

- Study §8.4 interpretation ("替代保持分类 … 靠消耗取胜的一方可以转向别处而持续").
- Module doc of `Becoming.Substitution` ("Substitution preserves the classification").
- Record substitution-preserves-consumption, `claim` and `correspondence`.
- Chapter §2 and §4 ("替代不证明更新").
- Study §8.5, row (a), for the stepwise, cycle and relation columns.

**Evidence.** Probe `Switch.stepwise_credits_switched_consumer`. In `Substitution.extracting` the focal formation is `ConsumingIn`, yet `Web.valuation` credits its event at every step except step 2, where the shared condition falls below support. Before the crossing, its draws leave every need met. After it, it draws on nothing in the model, since the alternative is not drawn, so it can undermine nothing. The relation-level reading agrees.

**Why it matters.**

- "Preservation" holds only for the whole-run reading, where it is nearly definitional. `ConsumingIn f` is `∃ t c, draws t f c ∧ Consumed c`, so nothing a formation does after one draw on a consumed condition can change it.
- On the stepwise reading, the meta-attractor case named in §8.4, a winner that turns elsewhere and persists, is credited at every step but one.
- This is a sharper failure of (a) than the crediting of pre-threshold events listed in the table.

**Correction.** State substitution's "preservation" as whole-run only and as a property of the existential definition. Add the probe's situation to the (a) row and to the record's `counterexamples`. "替代不证明更新" remains true: stepwise living is not renewal.

### F4. overclaim: criterion (b) is not met by the stepwise, cycle or relation readings

**Location.** Study §8.5, row (b) ("是：被断裂者被记入；只看事件所汲取的条件") for the stepwise, cycle-`p` and relation columns.

**Evidence.**

- *A drawer within its share.* `PoolProbe.within_share_condemned`, in the unchanged `Pool` process. The first drawer takes one unit, exactly the renewal; the second takes two. The second's part makes the difference (`MakesDifference`) and the first's does not. Yet the first drawer's event undermines, so the stepwise reading does not credit it. This is the synchronic analogue of the earlier review's Q11.
- *A drawer that changes nothing.* `Pinned.undermining_without_effect`. An exogenous collapse holds the level at 0 after every step. Two runs, one where the drawer takes a unit at every step and one where it takes nothing, have identical levels at every step. In the first, every drawer event from step 1 undermines, and the whole-run reading counts the drawer as consuming. This mirrors Q11: there, a later break condemned earlier drawers; here, an earlier loss condemns every later drawer, for as long as the lost formation's requirement persists.

**Why.** With `draws` amount-free and no reference to effect, the reading satisfies (b) only for formations that draw nothing.

**Correction.** Mark (b) as "partial" in those columns, citing these witnesses. In §7.1's statement of the cost, add that the reading withholds drawers that leave the condition unchanged, not only drawers that take little.

### F5. overclaim: the reason for preferring "not undermining" is counterfactual, and the definition is not

**Location.**

- Study §7.1, the "不断裂" row: post-loss drawing "使条件回不来".
- `Dependence` module doc: "it can keep the condition from returning".
- §8.5, thermodynamic bullet: "逐步读法保留此前各步".

**Evidence.**

- *No difference to return.* `Pinned.undermining_without_effect`: drawing after the loss is undermining although withholding it changes no level.
- *The support-gated law.* By `RelationalRenewal.Law.no_return_below_support`, with draw 0 and contribution 0, a condition below support stays where it is. So post-loss drawing there does not keep it from returning, yet it undermines. In the `winning` law, for example, the sustaining need met at step 0 stays unmet, so every later winner event undermines (this follows from the definition; it is not separately formalized).
- *What the witness depends on.* `drawing_after_loss` depends on two features of the commons: renewal continues below support (no feedback), and the lost formation is dormant and can revive, rather than ended.
- *Later drawers.* Once any once-met dependence is permanently unmet while its `requires` persists, the stepwise reading withholds every later drawing event on that condition, forever. In a run-down world this leaves no credited drawer after the losses, which is the thermodynamic pressure, half of it omitted.

**Correction.** Say that `UnderminingOn` reads co-participation in an unrestored shortfall, not contribution to non-return, and that "keeps it from returning" holds in the commons witness only. Complete the thermodynamic bullet.

### F6. overclaim (definition): but-for holds the configuration fixed but not the move

**Location.**

- `Becoming.Joint`: `BreaksFrom`, `MakesDifference`, `Overdetermined`, and the module doc ("with that part withheld and the rest as it was").
- Record joint-difference-making, `hypotheses`.

**What the Lean says.** `BreaksFrom` is `∃ a t, P.step s a t ∧ Breaks …`; `MakesDifference` requires every move from the withheld configuration to keep the dependence. The move is part of "the rest", and it is not held fixed.

**Evidence.**

- `Shock.sole_drawer_overdetermined`: if the process also admits an exogenous "shock", the loss caused by a single drawer is `Overdetermined`, so no part ever makes a difference. Under the calm move, the drawer's part alone breaks the dependence, and withholding it keeps the dependence.
- `Shock.difference_without_loss`: a move open only while the drawer takes something makes the drawer "make the difference" to a loss that the calm move actually taken does not produce.

**Scope.** `Pool` is unaffected, because its next level does not depend on the move.

**Correction.** Make the test relative to the move actually taken: `(∃ t, P.step s a t ∧ Breaks s t g c) ∧ ∀ t, P.step (withhold f s) a t → Keeps (withhold f s) t g c`. Then re-prove `Pool`. Alternatively, state the hypothesis that the level after a step does not depend on the move. Add this to the record.

### F7. overclaim: `depletion_is_joint` is tail-invariance, and step-level but-for picks out the breaking event

**Location.**

- Study §8.3 interpretation ("每一步的汲取单独都不造成差别，共同造成了消耗").
- §8.5, constraint 2, and the but-for column.
- Chapter §6.3 ("but-for 差别制造不能代替参与（`depletion_is_joint`）") and chapter §4.
- `Joint` module doc ("A formation's events over time are a joint activity too"; "Of the readings here, only the whole-run reading counts the depletion").

**Evidence.**

- *No finite set of events matters.* `Tail.no_finite_segment_makes_difference`: withholding every draw before any `N` leaves the condition consumed. No finite set of events makes the run-level difference, unlike `Pool`, where withholding a pair keeps the dependence. Consumption is fixed by the tail, which is the same fact as the horizon result.
- *The breaking event is a step-level cause.* `Tail.breaking_event_makes_step_difference`: at the breaking step of `depleting`, drawing nothing would keep the dependence.
- *The two tests are different.* `depletion_is_joint` does not use `MakesDifference`, which cannot be instantiated in `Commons` because the draw is the action, not part of the state.
- *The stepwise reading counts some depletion.* It withholds the breaking event and every later one, so "only the whole-run reading counts the depletion" means only that only it also withholds event 0.

**Correction.**

- Distinguish run-level withholding (outcome "consumed") from step-level withholding (outcome "this break").
- Say the run-level outcome is a tail property of the continuation, and that "but-for cannot replace participation" is shown for the single-part run-level test only. The NESS test (§8.6) is a further rival.

### F8. overclaim: "renewal is renewal over cycles of one" is one-directional

**Location.**

- `Becoming.Return` module doc, Results bullet 4.
- Study §8.1 table, the row for `RenewingIn.within_one` ("更新即一步周期内更新").
- Study §8.1 interpretation (the ladder).

**Evidence.** `LateMet.within_one_not_renewing`: on a `Dependent` web, a formation satisfies `RenewingInWithin 1` but not `RenewingIn`. `RenewedWithin p` never asks whether a dependence is met at its own step, while `Renewed` (through `Kept`) does. The ladder is therefore `Renewed ⊊ RenewedWithin 1 ⊆ … ⊆ Returns`, with the first inclusion strict. This repeats, at the top rung, the asymmetry about unmet requirements found by review Q2. The record's `counterexamples` already discloses the one-way implication.

**Correction.** Write "renewal implies renewal within one step" in the module doc and the study, and add the witness.

### F9. overclaim: the cycle readings are not all finitely decided

**Location.**

- Study §8.2 interpretation ("逐步读法与周期读法都由有限的步决定").
- Record becoming-finite-horizon, `counterexamples` ("The stepwise and cycle readings are fixed by finitely many steps").
- `Horizon` module doc ("each decided by one step").

**Evidence.** `HorizonProbe.cycle_reading_not_finite`: for every `h` and every `p > 0`, the formation-level `RenewingInWithin p` is not fixed by the first `h` steps. It is a corollary of the authors' own theorem, since that reading never credits a consuming run. Only the event-level `UnderminingFor p` is fixed, by the history up to `t + p`. `UnderminingAt` needs the whole past (`∃ s ≤ t`), not one step. The table in §8.5 uses the event readings, so its row (c) stands.

**Correction.** Say "the event-level stepwise and cycle readings".

### F10. presentation: cycle length 0 is degenerate

**Location.** `Becoming.Return`: `UnderminingFor`, `RenewedWithin`, and `escalation_undermines_for_every_cycle`.

**Evidence.** `HorizonProbe.undermining_for_zero`: `UnderminingFor 0` holds of any draw on a condition with a dependence met then or before, even in the renewing run `sharing`. `RenewedWithin 0 c` holds only when nothing depends on `c`. "For every cycle" therefore includes a vacuous case; `depletion_is_joint` already assumes `0 < p`.

**Correction.** Index cycles by `p + 1`, or state `1 ≤ p`.

### F11. presentation (AGENTS.md): the provenance of criterion (a), and "adopted"

**Location.**

- Study §8.5, criterion (a) ("符合 Ren 有来源的判决：恶性增殖、以消耗取胜不是生生") and its grading of the stepwise column as "部分".
- §7.1 ("不侵蚀（采用）"; "这与 Ren 关于以消耗取胜的判决不合").

**Evidence.** In the [source](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md), the list of cancer, arms race and the self-reinforcing "win" is an AI review's text. Ren quoted it and asked to separate the two kinds of formation by relational structure "不需要任何axiom". Ren's own follow-up is "generative和degenerate虽然都在一个becoming model上，但是他们不overlap吧". Ren's words endorse the problem and the non-overlap. They do not say whether the events of a formation, before its drawing exceeds renewal, are excluded. That was the AI's whole-run choice (earlier review 2.1), and the grades in rows (a) and constraint 1 rest on it.

"采用" (adopted) for the reading in `Web.valuation` sits beside "读法由 Ren 选择" (the reading is Ren's choice).

**Correction.**

- Label (a) as "the problem Ren adopted and the non-overlap Ren stated". Mark the verdict on pre-threshold events as an AI extension.
- Call "not undermining" the working stepwise candidate in `Web.valuation`, pending Ren's choice.

### F12. presentation: the premise of the thermodynamic claim is missing

**Location.** Study §8.5, the thermodynamic bullet ("整段读法在整个历史中都没有 living 事件").

**Evidence.** On the whole-run reading, a formation that draws on nothing keeps its active events: `Conditions.valuation` withholds only formations that draw on a consumed condition. The earlier review's Q10a had the premise "每个形成都汲取 c₀".

**Correction.** Add "if every formation draws on such a condition".

### F13. presentation: chapter §4, English text

**Location.** Chapter §4, English text: "Two spine facts bear on it:" is followed by four bullets.

**Correction.** Change "Two" to "Four", or drop the number.

### F14. presentation: "draws nothing" in `drawing_after_loss`

**Location.** The docstring of `Commons.drawing_after_loss`: "then draws nothing".

**Evidence.** In `Commons.conditions` the focal formation's `draws` is constantly `True`, so in `pausing` it formally draws at every step while its action is 0. The theorem is unaffected.

**Correction.** Write "takes nothing (action 0)", and note that the commons' `draws` is blind to amount even at zero.

### F15. records

**Counts.** Correct: Return 26, Horizon 2, Joint 12, Substitution 4, and 169 theorems / 332 declaration audits at `278de821`. Re-pointed to 186 / 361 by P8.

**Corrections needed.**

- **becoming-finite-horizon.**
  - Add a hypothesis: the renewing witness overdraws for `h` steps, so "credits every renewing run" includes crediting drawing beyond renewal.
  - Correct `related[0]` (F2, false as stated) and the `counterexamples` sentence on cycle readings (F9).
  - Replace "not proved" for feedback with the probe's answer (F2).
- **joint-difference-making.** Add a hypothesis: moves are held fixed, or the level does not depend on them (F6). Distinguish the run-level test of `depletion_is_joint` from `MakesDifference` (F7).
- **substitution-preserves-consumption.** "Preserves" is whole-run only and near-definitional. Add the stepwise counterexample (F3).
- **becoming-stepwise-reading.** Correct the claim about never-met requirements (F1). The (b) and amount costs (F4, F5) belong in `counterexamples`.
- **becoming-return-grades.** Sound; the one-way implication is disclosed. Add the `LateMet` witness (F8) and `p ≥ 1` (F10).

**Outside scope.** The `correspondence` of relational-reading-comparison refers to Ren as "his"; the repository's practice is "Ren" or they/them.

## 3. Question 4 in detail: the table, the split and its cost

**Fairness of the table.**

- **Row (c)** is fair for the event-level columns (F9).
- **Row (e)** is fair for verdicts on existing claims. One nuance: for the relation-level reading, an added need-0 condition `c₀` creates new living claims `(f, c₀, t)` for every active formation. Through `related`, which is "same condition, or same event", it connects the whole. So connection is again free at that level, as in review Q4.
- **Rows (a) and (b)** are uneven, for the reasons given in F2, F3 and F4.
- **The but-for column** merges two tests (F7).
- **Row (d)**, "no further generation" for every reading, is fair.

**The split.** It is clearly labelled "作者的候选分工（AI 论证，未经 Ren 确认）", and the final paragraph leaves the choice to Ren. It relocates rather than removes the failure of (c): C's comparison of whole continuations is not finitely decidable either. The study acknowledges this ("要求对继续的探究").

**The cost as committed.** The stated cost is: "under the stepwise reading the ranking 'absence of the overdrawing formation above its occurrence' no longer follows from C alone". It is correct with one unstated condition: the consuming formation must have a credited event before the loss. When the first step already crosses support (for example, start equal to `needG` with overdraw from step 0), no focal event is credited. The course without the formation then extends the course with it under the stepwise reading too, and C ranks it. This follows from the definitions; it is not formalized here.

P8's `stepwise_unranked` and `readings_rank_differently` state exactly this hypothesis (`credited`) and prove the cost. P8 also proves `stepwise_contest`: sharing still extends winning by consumption under the stepwise reading. The committed paragraph did not anticipate that survival, so it overstated what was lost.

The reviewer expects the same survival for malignant growth compared with the same formation stopping within renewal before the threshold. This is not formalized here; it would show that only the comparison with non-existence is lost.

## 4. What remains sound

- Every P7 theorem: statement, proof and empty axiom report, recompiled from the prelude.
- `consumed_iff` and the strict grades `seasonal_renewed_within_two` and `Slowing.slowing_recovery`.
- `Pool.difference_belongs_to_the_joint`, as a witness that single-part but-for status depends on the other parts.
- `persists_consuming`, as a fact about the law family read through changing dependence.
- The labelling of the split, and the refusal to choose the reading on Ren's behalf.
- The disclosure of modelling duties for withholding, for horizons and for the cost of the alternative.

## 5. What would change these verdicts

1. A repaired `UnderminingOn` (F1), with the stepwise theorems re-proved. F1 would close, and the §7.1 comparison of the three candidates would stand.
2. Ren's words, or Ren's decision, that the verdict on winning by consumption covers the whole-run classification of events before the threshold. F2's conflict would then be a real constraint relative to that choice, and F11 would close.
3. A web with amounts and renewal rates, and either a finitely decidable reading that meets (a) as Ren states it, or a proof that every such reading fails (a) in a sourced case. Either would settle whether (a) and (c) conflict at all.
4. A move-relative `MakesDifference` with `Pool` re-proved (F6), and a step-level statement of joint depletion (F7).
5. A proof that, under the stepwise reading, C ranks stopping within renewal above malignant overdraw. It would confirm that the cost is confined to comparison with non-existence.

## Appendix: probe sources

Compiled with Lean 4.29.1 against the unchanged `278de821` core bytes (with `import Std` removed from `GenerativeCore`, as the checker does). The audit file prints the axioms of the 23 declarations named in §0; every one reports "does not depend on any axioms".

### `P7Probes.lean`

```lean
import Becoming.Metaethics
import Becoming.Return
import Becoming.Horizon
import Becoming.Joint
import Becoming.Substitution

/-!
# Probes for the independent review of P7 and of the undermining correction

Each probe is a minimal model satisfying the published definitions unchanged. It tests
what the definitions admit, not what actual systems usually do.
-/

namespace P7Probe

open Becoming

/-! ## R1. `RenewingIn.within_one` has no converse -/

namespace LateMet

/-- The level is 0 at step 0 and 1 afterwards. One formation depends on the condition at
need 1 throughout and is active from step 1, where it is supported. -/
def web : Web Unit Unit :=
  ⟨fun t _ => match t with | 0 => 0 | _ + 1 => 1,
   fun t _ => match t with | 0 => False | _ + 1 => True,
   fun _ _ _ => True, fun _ _ _ => 1, fun _ _ _ => False⟩

theorem dependent : web.Dependent
  | 0, _, active, _, _ => False.elim active
  | _ + 1, _, _, _, _ => Nat.le_refl 1

/-- Renewal over cycles of one does not give renewal: the dependence is not met at its
own step 0, so it is not kept there, yet it is met at every next step. -/
theorem within_one_not_renewing : web.Dependent ∧ web.RenewingInWithin 1 () ∧ ¬ web.RenewingIn () :=
  ⟨dependent, fun _ _ _ _ _ _ => ⟨1, Nat.zero_lt_one, Nat.le_refl 1, Nat.le_refl 1⟩,
   fun renewing => Nat.not_succ_le_zero 0 (renewing 0 () (Or.inl trivial) 0 () trivial).1⟩

end LateMet

/-! ## R2. Undermining through a dependence that was never met while it held -/

namespace NewNeed

inductive F where
  | late
  | drawer

/-- The level is 2 at step 0 and 0 from step 1 on; nothing draws before step 5. `late`
depends on the condition at need 1 only from step 5 on, when the level is 0, and is never
active. `drawer` draws from step 5 on. -/
def web : Web F Unit where
  level t _ := match t with | 0 => 2 | _ + 1 => 0
  active t f := match f with | .late => False | .drawer => 5 ≤ t
  requires t f _ := match f with | .late => 5 ≤ t | .drawer => False
  need _ _ _ := 1
  draws t f _ := match f with | .late => False | .drawer => 5 ≤ t

theorem level_late {t : Nat} (late : 5 ≤ t) : web.level t () = 0 :=
  match t, late with
  | _ + 1, _ => rfl

/-- `late`'s dependence is unmet at every step at which it holds and is never broken, yet
every event of `drawer` undermines through it, so the stepwise reading credits none of
`drawer`'s events. The definition compares the current need with a level from before the
dependence existed. -/
theorem undermining_without_met_dependence (own sig : Unit → F × Nat → Prop) :
    web.Dependent ∧
    (∀ t, web.requires t .late () → web.level t () < web.need t .late ()) ∧
    (∀ t, ¬ web.Broken t .late ()) ∧
    (∀ t, 5 ≤ t → web.UnderminingAt t .drawer ∧ ¬ (web.valuation own sig).living (.drawer, t)) := by
  have unmet : ∀ t, web.requires t .late () → web.level t () < web.need t .late () :=
    fun t late => (level_late late).symm ▸ Nat.zero_lt_one
  refine ⟨?_, unmet, fun t ⟨late, met, _⟩ => Nat.not_le_of_gt (unmet t late) met, fun t late => ?_⟩
  · intro t f active c depends
    cases f with
    | late => exact False.elim active
    | drawer => exact False.elim depends
  · have undermining : web.UnderminingAt t .drawer :=
      ⟨(), late, .late, late, ⟨0, Nat.zero_le t, Nat.le_succ 1⟩,
        (level_late (Nat.le_succ_of_le late)).symm ▸ Nat.zero_lt_one⟩
    exact ⟨undermining, fun ⟨_, notUndermining⟩ => notUndermining undermining⟩

end NewNeed

/-! ## R3. Drawing that changes no level is undermining, and consuming, for ever -/

namespace Pinned

inductive F where
  | old
  | drawer

/-- The level of the condition and the amount the drawer takes at this step. -/
structure State where
  level : Nat
  taking : Nat

/-- An exogenous collapse: whatever is taken, the level is 0 after every step. The action
sets the next amount taken. -/
def process : Generative.Process State Nat :=
  ⟨fun _ a t => t = ⟨0, a⟩⟩

/-- `old` depends on the condition at need 1 and is active while supported; `drawer`
draws when it takes a positive amount. -/
def dependence : Dependence State F Unit where
  level s _ := s.level
  active s f := match f with | .old => 1 ≤ s.level | .drawer => True
  requires _ f _ := match f with | .old => True | .drawer => False
  need _ _ _ := 1
  draws s f _ := match f with | .old => False | .drawer => 0 < s.taking

def takingState : Nat → State
  | 0 => ⟨2, 0⟩
  | _ + 1 => ⟨0, 1⟩

def restingState : Nat → State
  | 0 => ⟨2, 0⟩
  | _ + 1 => ⟨0, 0⟩

/-- The drawer takes one unit at every step from step 1. -/
def taking : Run process :=
  ⟨takingState, fun _ => 1, fun | 0 => rfl | _ + 1 => rfl⟩

/-- The drawer takes nothing. -/
def resting : Run process :=
  ⟨restingState, fun _ => 0, fun | 0 => rfl | _ + 1 => rfl⟩

/-- Both runs have the same level at every step, so the drawer's taking changes no level.
Yet in the run where it takes, each of its events from step 1 undermines, so the stepwise
reading credits none of them, and the whole-run reading counts it as consuming. -/
theorem undermining_without_effect (own sig : Unit → F × Nat → Prop) :
    (∀ t, (dependence.along taking).level t () = (dependence.along resting).level t ()) ∧
    (∀ t, 1 ≤ t → (dependence.along taking).UnderminingAt t .drawer ∧
      ¬ ((dependence.along taking).valuation own sig).living (.drawer, t)) ∧
    (dependence.along taking).ConsumingIn .drawer ∧
    ∀ t, ¬ (dependence.along resting).draws t .drawer () := by
  refine ⟨fun | 0 => rfl | _ + 1 => rfl, fun t later => ?_,
    ⟨1, (), Nat.zero_lt_one, .old, 0, trivial, fun | _ + 1, _ => Nat.zero_lt_one⟩,
    fun | 0 => Nat.lt_irrefl 0 | _ + 1 => Nat.lt_irrefl 0⟩
  match t, later with
  | n + 1, _ =>
    have undermining : (dependence.along taking).UnderminingAt (n + 1) .drawer :=
      ⟨(), Nat.zero_lt_one, .old, trivial, ⟨0, Nat.zero_le _, Nat.le_succ 1⟩, Nat.zero_lt_one⟩
    exact ⟨undermining, fun ⟨_, notUndermining⟩ => notUndermining undermining⟩

end Pinned

/-! ## J1. A loss with one drawer is "overdetermined" once an exogenous move exists -/

namespace Shock

inductive F where
  | drawer
  | sustaining

structure State where
  level : Nat
  taking : Nat

inductive Move where
  | calm (next : Nat)
  | shock

/-- A calm step renews one unit and takes the current amount; a shock empties the
condition. -/
def process : Generative.Process State Move :=
  ⟨fun s a t => match a with
    | .calm next => t = ⟨s.level + 1 - s.taking, next⟩
    | .shock => t = ⟨0, s.taking⟩⟩

def withhold (f : F) (s : State) : State :=
  match f with
  | .drawer => ⟨s.level, 0⟩
  | .sustaining => s

def dependence : Dependence State F Unit where
  level s _ := s.level
  active s f := match f with | .drawer => True | .sustaining => 1 ≤ s.level
  requires _ f _ := match f with | .drawer => False | .sustaining => True
  need _ _ _ := 1
  draws s f _ := match f with | .drawer => 0 < s.taking | .sustaining => False

def start : State := ⟨1, 2⟩

/-- The sole drawer's part is not a but-for cause by `MakesDifference`, because the
withheld configuration still has a breaking step (the shock). Under the calm move, its
part alone breaks the dependence and withholding it keeps the dependence. -/
theorem sole_drawer_overdetermined :
    dependence.Overdetermined process withhold start .sustaining () ∧
    ¬ dependence.MakesDifference process withhold .drawer start .sustaining () ∧
    process.step start (.calm 2) ⟨0, 2⟩ ∧ dependence.Breaks start ⟨0, 2⟩ .sustaining () ∧
    process.step (withhold .drawer start) (.calm 0) ⟨2, 0⟩ ∧
    dependence.Keeps (withhold .drawer start) ⟨2, 0⟩ .sustaining () := by
  have over : dependence.Overdetermined process withhold start .sustaining () :=
    ⟨⟨.calm 2, ⟨0, 2⟩, rfl, trivial, Nat.le_refl 1, Nat.zero_lt_one⟩, fun f => by
      cases f with
      | drawer => exact ⟨.shock, ⟨0, 0⟩, rfl, trivial, Nat.le_refl 1, Nat.zero_lt_one⟩
      | sustaining => exact ⟨.shock, ⟨0, 2⟩, rfl, trivial, Nat.le_refl 1, Nat.zero_lt_one⟩⟩
  exact ⟨over, over.no_difference .drawer, rfl, ⟨trivial, Nat.le_refl 1, Nat.zero_lt_one⟩, rfl,
    ⟨Nat.le_refl 1, Nat.le_succ 1⟩⟩

/-- A surge move is open only while the drawer takes something. -/
inductive SurgeMove where
  | calm (next : Nat)
  | surge

def surgeProcess : Generative.Process State SurgeMove :=
  ⟨fun s a t => match a with
    | .calm next => t = ⟨s.level + 1 - s.taking, next⟩
    | .surge => 0 < s.taking ∧ t = ⟨0, s.taking⟩⟩

def calmStart : State := ⟨1, 1⟩

/-- The drawer "makes the difference" to a loss that the move actually taken does not
produce: `BreaksFrom` is witnessed by the surge, which the run need not take. -/
theorem difference_without_loss :
    dependence.MakesDifference surgeProcess withhold .drawer calmStart .sustaining () ∧
    surgeProcess.step calmStart (.calm 1) ⟨1, 1⟩ ∧
    dependence.Keeps calmStart ⟨1, 1⟩ .sustaining () := by
  refine ⟨⟨⟨.surge, ⟨0, 1⟩, ⟨Nat.zero_lt_one, rfl⟩, trivial, Nat.le_refl 1, Nat.zero_lt_one⟩,
    fun a t step => ?_⟩, rfl, ⟨Nat.le_refl 1, Nat.le_refl 1⟩⟩
  cases a with
  | calm next =>
    have reached : t = ⟨2, next⟩ := step
    subst reached
    exact ⟨Nat.le_refl 1, Nat.le_succ 1⟩
  | surge => exact absurd step.1 (Nat.lt_irrefl 0)

end Shock

/-! ## J2. Gradual depletion: the step-level test singles out the breaking event, and
the run-level outcome is fixed by the tail -/

namespace Tail

/-- In `depleting`, the step from level 1 drawing two units breaks the dependence, and
the same configuration drawing nothing keeps it: the breaking event is a step-level
but-for cause of the break. -/
theorem breaking_event_makes_step_difference :
    Commons.depleting.state 1 = 1 ∧ Commons.depleting.act 1 = 2 ∧
    Commons.conditions.dependence.Breaks (Commons.depleting.state 1)
      (Commons.depleting.state 2) .sustaining () ∧
    Commons.process.step 1 0 2 ∧ Commons.conditions.dependence.Keeps 1 2 .sustaining () :=
  ⟨rfl, rfl, ⟨trivial, Nat.le_refl 1, Nat.zero_lt_one⟩, rfl, ⟨Nat.le_refl 1, Nat.le_succ 1⟩⟩

/-- Withholding every draw before any step `N` leaves the condition consumed: no finite
set of events makes the run-level difference. -/
theorem no_finite_segment_makes_difference (N : Nat) :
    (Commons.conditions.dependence.along
      (Commons.drawing 2 fun t => if t < N then 0 else 2)).Consumed () :=
  Commons.overdraw_consumes fun _ later => Nat.le_of_eq (if_neg (Nat.not_lt_of_le later)).symm

end Tail

/-! ## J3. The stepwise reading condemns a drawer within its share that makes no
difference -/

namespace PoolProbe

/-- The first drawer takes one unit, exactly the renewal; the second takes two. -/
def mixed : Pool.Draw := ⟨1, 2, 0⟩

def mixedRun : Run Pool.process :=
  ⟨Pool.steady mixed, fun _ => mixed, fun | 0 => rfl | _ + 1 => rfl⟩

/-- The second drawer's part makes the difference and the first's does not, yet the
stepwise reading does not credit the first drawer's event at the breaking step. -/
theorem within_share_condemned (own sig : Unit → Pool.Formation × Nat → Prop) :
    Pool.dependence.MakesDifference Pool.process Pool.withhold .second (mixedRun.state 0)
      .sustaining () ∧
    ¬ Pool.dependence.MakesDifference Pool.process Pool.withhold .first (mixedRun.state 0)
      .sustaining () ∧
    (Pool.dependence.along mixedRun).UnderminingAt 0 .first ∧
    ¬ ((Pool.dependence.along mixedRun).valuation own sig).living (.first, 0) := by
  have undermining : (Pool.dependence.along mixedRun).UnderminingAt 0 .first :=
    ⟨(), Nat.zero_lt_one, .sustaining, trivial, ⟨0, Nat.le_refl 0, Nat.le_refl 1⟩, Nat.zero_lt_one⟩
  refine ⟨⟨Pool.breaks_from_one mixed rfl, fun _ _ step => ?_⟩, fun ⟨_, keeps⟩ => ?_, undermining,
    fun ⟨_, notUndermining⟩ => notUndermining undermining⟩
  · subst step
    exact ⟨Nat.le_refl 1, Nat.le_refl 1⟩
  · exact Nat.not_succ_le_zero 0 (keeps mixed ⟨0, mixed⟩ rfl).2

end PoolProbe

/-! ## S1. After substitution the stepwise reading credits the consumer -/

namespace Switch

open RelationalRenewal

theorem extracting_low : ∀ n, Law.level Substitution.extracting (n + 3) = 0
  | 0 => rfl
  | n + 1 => by
    show Law.level Substitution.extracting (n + 3 + 1) = 0
    rw [Law.level_succ, extracting_low n]
    rfl

/-- The consuming formation that substitutes is credited by the stepwise reading at every
step except the one at which the shared condition falls below support. -/
theorem stepwise_credits_switched_consumer (own sig : Unit → Law.Part × Nat → Prop) :
    (Substitution.web Substitution.extracting).ConsumingIn .focal ∧
    (∀ t, t ≠ 2 → ((Substitution.web Substitution.extracting).valuation own sig).living (.focal, t)) ∧
    ¬ ((Substitution.web Substitution.extracting).valuation own sig).living (.focal, 2) := by
  refine ⟨Substitution.extracting_persists_consuming.2.2.2.1, fun t other => ?_, ?_⟩
  · refine ⟨trivial, fun ⟨c, drawn, g, _, _, fell⟩ => ?_⟩
    match t, other, c, drawn, g, fell with
    | 0, _, .shared, _, .focal, fell => exact absurd fell (by decide)
    | 0, _, .shared, _, .sustaining, fell => exact absurd fell (by decide)
    | 1, _, .shared, _, .focal, fell => exact absurd fell (by decide)
    | 1, _, .shared, _, .sustaining, fell => exact absurd fell (by decide)
    | 2, other, _, _, _, _ => exact absurd rfl other
    | n + 3, _, .shared, drawn, _, _ =>
      have low : Law.level Substitution.extracting (n + 3) = 0 := extracting_low n
      have on : 1 ≤ Law.level Substitution.extracting (n + 3) := drawn.1
      exact Nat.not_succ_le_zero 0 (Nat.le_trans on (Nat.le_of_eq low))
    | _, _, .alternative, drawn, _, _ => exact drawn
  · exact fun ⟨_, notUndermining⟩ => notUndermining
      ⟨.shared, ⟨Nat.le_refl 1, Nat.zero_lt_two⟩, .sustaining, trivial,
        ⟨0, Nat.zero_le 2, Nat.le_succ_of_le (Nat.le_succ 1)⟩, Nat.zero_lt_one⟩

end Switch

/-! ## H1. The whole-run reading credits drawing beyond renewal in the run that stops -/

namespace HorizonProbe

/-- For every horizon, the renewing run of `prefix_does_not_decide` draws two units, one
beyond renewal, at every step before the horizon, and the whole-run reading credits every
event of its focal formation, those included. -/
theorem whole_run_credits_overdraw (h : Nat) (own sig : Unit → Commons.Formation × Nat → Prop) :
    ∃ r : Run Commons.process, (∀ t, t < h → r.act t = 2) ∧
      ∀ t, (Commons.conditions.valuation r own sig).living (.focal, t) :=
  match Commons.prefix_does_not_decide h with
  | ⟨r, _, ⟨_, acts⟩, over, _, renews, _⟩ =>
    ⟨r, fun t before => (acts t before).trans (over t before),
     fun _ => ⟨trivial,
       RelationalRenewal.renewing_not_consuming ((Web.static_renewingIn _ _).mp renews)⟩⟩

/-- A per-step amount reading, "draws no more than is renewed at this step", is fixed by
the first `t + 1` steps, credits every event of `sharing` and withholds every event
before the horizon in both runs of `prefix_does_not_decide`. It escapes the horizon
theorem only by not crediting every renewing run. -/
theorem amount_reading (h : Nat) :
    (∀ t (r r' : Run Commons.process), r.AgreeUpTo (t + 1) r' → (r.act t ≤ 1 ↔ r'.act t ≤ 1)) ∧
    (∀ t, Commons.sharing.act t ≤ 1) ∧
    ∃ r c : Run Commons.process, (Commons.conditions.dependence.along r).RenewingIn .focal ∧
      (Commons.conditions.dependence.along c).ConsumingIn .focal ∧
      ∀ t, t < h → ¬ r.act t ≤ 1 ∧ ¬ c.act t ≤ 1 :=
  ⟨fun t _ _ ⟨_, acts⟩ => acts t (Nat.lt_succ_self t) ▸ Iff.rfl, fun _ => Nat.le_refl 1,
   match Commons.prefix_does_not_decide h with
   | ⟨r, c, ⟨_, acts⟩, over, _, renews, consumes⟩ =>
     ⟨r, c, renews, consumes, fun t before =>
       ⟨fun le => Nat.not_succ_le_self 1
          (Nat.le_trans (Nat.le_of_eq ((acts t before).trans (over t before)).symm) le),
        fun le => Nat.not_succ_le_self 1 (Nat.le_trans (Nat.le_of_eq (over t before).symm) le)⟩⟩⟩

/-- The formation-level cycle reading is not fixed by any finite prefix. -/
theorem cycle_reading_not_finite (h p : Nat) (positive : 0 < p) :
    ¬ ∀ r r' : Run Commons.process, r.AgreeUpTo h r' →
      (Commons.conditions.dependence.along r).RenewingInWithin p .focal →
      (Commons.conditions.dependence.along r').RenewingInWithin p .focal :=
  fun decided =>
    match Commons.finite_reading_credits_consumption h _ decided
      (fun _ renews => (Web.RenewingIn.within_one renews).mono positive) with
    | ⟨_, consumes, renews⟩ => renews.not_consuming consumes

/-- Undermining for zero steps holds of every draw on a condition with a dependence met
then or before, even in the renewing run `sharing`. -/
theorem undermining_for_zero :
    (Commons.conditions.dependence.along Commons.sharing).RenewingIn .focal ∧
    (Commons.conditions.dependence.along Commons.sharing).UnderminingFor 0 0 .focal :=
  ⟨fun _ _ _ _ g depends => match g, depends with
    | .sustaining, _ => ⟨Nat.le_refl 1, Nat.le_refl 1⟩,
   ⟨(), trivial, .sustaining, trivial, ⟨0, Nat.le_refl 0, Nat.le_refl 1⟩,
    fun _ positive within => absurd (Nat.lt_of_lt_of_le positive within) (Nat.lt_irrefl 0)⟩⟩

end HorizonProbe

end P7Probe
```

### `P7Feedback.lean`

```lean
import RelationalRenewal

/-!
# H2. The horizon result in the support-gated law, which has feedback

In `RelationalRenewal.Law` the renewal stops once the condition is below the sustaining
formation's support (`no_return_below_support`). For every horizon `h`, two draw
schedules from the same start agree before `h`; under one the focal formation is
renewing, under the other consuming. The feedback is never reached in the renewing
schedule, so it does not change the horizon result.
-/

namespace P7Probe.Feedback

open RelationalRenewal RelationalRenewal.Law

/-- Start `h + 1`, renewal one unit, sustaining need one, focal need zero, no contribution. -/
def law (h : Nat) (d : Nat → Nat) : Law := ⟨h + 1, 1, 1, 0, d, fun _ => 0⟩

/-- Two units a step before `h`, then the renewal only. -/
def stopping (h t : Nat) : Nat := if t < h then 2 else 1

/-- Two units a step throughout. -/
def continuing (_ : Nat) : Nat := 2

/-- As `Nat.le_of_add_le_add_right`, with an empty axiom report. -/
theorem le_cancel : ∀ {a b : Nat} (k : Nat), a + k ≤ b + k → a ≤ b
  | _, _, 0, h => h
  | _, _, k + 1, h => le_cancel k (Nat.le_of_succ_le_succ h)

/-- As `Nat.add_right_cancel`, with an empty axiom report. -/
theorem eq_cancel : ∀ {a b : Nat} (k : Nat), a + k = b + k → a = b
  | _, _, 0, h => h
  | _, _, k + 1, h => eq_cancel k (Nat.succ.inj h)

theorem step_two {h t m : Nat} {d : Nat → Nat} (high : (law h d).level t = m + 2)
    (two : d t = 2) : (law h d).level (t + 1) = m + 1 := by
  rw [level_succ, high, if_pos (show (law h d).needG ≤ m + 2 from Nat.succ_le_succ (Nat.zero_le _)),
    if_pos (show (law h d).needF ≤ m + 2 from Nat.zero_le _)]
  show m + 1 + 1 + 1 + 0 - d t = m + 1
  rw [two]
  exact add_sub_self (m + 1) 2

theorem step_one {h t : Nat} {d : Nat → Nat} (one : (law h d).level t = 1) (same : d t = 1) :
    (law h d).level (t + 1) = 1 := by
  rw [level_succ, one, if_pos (show (law h d).needG ≤ 1 from Nat.le_refl 1),
    if_pos (show (law h d).needF ≤ 1 from Nat.zero_le _)]
  show 1 + 1 + 0 - d t = 1
  rw [same]

/-- Before the horizon, the level falls by one a step under either schedule. -/
theorem descending (h : Nat) (d : Nat → Nat) (two : ∀ t, t < h → d t = 2) :
    ∀ k, k ≤ h → (law h d).level k + k = h + 1
  | 0, _ => rfl
  | k + 1, le => by
    have ih := descending h d two k (Nat.le_of_succ_le le)
    have bound : 2 + k ≤ (law h d).level k + k := by
      rw [ih, Nat.add_comm 2 k]
      exact Nat.succ_le_succ le
    obtain ⟨m, hm⟩ := Nat.le.dest (le_cancel k bound)
    have high : (law h d).level k = m + 2 := by rw [← hm, Nat.add_comm]
    rw [step_two high (two k (Nat.lt_of_succ_le le))]
    rw [high] at ih
    rw [Nat.add_succ, ← Nat.succ_add]
    exact ih

theorem at_horizon (h : Nat) : (law h (stopping h)).level h = 1 :=
  eq_cancel h ((descending h (stopping h) (fun _ before => if_pos before) h
    (Nat.le_refl h)).trans (Nat.add_comm h 1))

theorem after_horizon (h : Nat) : ∀ j, (law h (stopping h)).level (h + j) = 1
  | 0 => at_horizon h
  | j + 1 => step_one (after_horizon h j) (if_neg (Nat.not_lt_of_le (Nat.le_add_right h j)))

theorem supported (h t : Nat) : 1 ≤ (law h (stopping h)).level t :=
  match Nat.lt_or_ge t h with
  | .inl before =>
    le_cancel t (Nat.le_trans
      (show 1 + t ≤ h + 1 from (Nat.add_comm 1 t) ▸ Nat.succ_le_succ (Nat.le_of_lt before))
      (Nat.le_of_eq (descending h (stopping h) (fun _ b => if_pos b) t
        (Nat.le_of_lt before)).symm))
  | .inr after =>
    match Nat.le.dest after with
    | ⟨j, sum⟩ => sum ▸ Nat.le_of_eq (after_horizon h j).symm

/-- For every horizon, the same law with feedback, from the same start, under draws that
agree before the horizon (two units, one beyond renewal): stopping there renews,
continuing consumes. -/
theorem prefix_does_not_decide_with_feedback (h : Nat) :
    (law h (stopping h)).start = (law h continuing).start ∧
    (∀ t, t < h → stopping h t = continuing t) ∧
    RenewingIn (law h (stopping h)).unfolding .focal ∧
    ConsumingIn (law h continuing).unfolding .focal :=
  ⟨rfl, fun _ before => if_pos before,
   fun _ _ t g depends => match g, depends with
     | .sustaining, _ => supported h t,
   (overdraw_consuming (law h continuing) Nat.zero_lt_one (Nat.zero_le 1) (T0 := 0)
     fun _ _ => Nat.lt_succ_self 1).1⟩

end P7Probe.Feedback
```

### `Audit.lean`

```lean
import P7Probes
import P7Feedback
open P7Probe
#print axioms LateMet.within_one_not_renewing
#print axioms NewNeed.undermining_without_met_dependence
#print axioms Pinned.undermining_without_effect
#print axioms Shock.sole_drawer_overdetermined
#print axioms Shock.difference_without_loss
#print axioms Tail.breaking_event_makes_step_difference
#print axioms Tail.no_finite_segment_makes_difference
#print axioms PoolProbe.within_share_condemned
#print axioms Switch.extracting_low
#print axioms Switch.stepwise_credits_switched_consumer
#print axioms HorizonProbe.whole_run_credits_overdraw
#print axioms HorizonProbe.amount_reading
#print axioms HorizonProbe.cycle_reading_not_finite
#print axioms HorizonProbe.undermining_for_zero
#print axioms Feedback.step_two
#print axioms Feedback.step_one
#print axioms Feedback.descending
#print axioms Feedback.at_horizon
#print axioms Feedback.after_horizon
#print axioms Feedback.supported
#print axioms Feedback.prefix_does_not_decide_with_feedback
#print axioms NewNeed.level_late
#print axioms LateMet.dependent
```
