# General-law audit of records changed since 2026-10-12, and general laws for P100

Scratch only; nothing in `/Users/ren/theories` was edited (git status clean). Scratch: `/private/tmp/claude-501/-Users-ren-theories/de45ebc5-e5b8-4ea1-944c-69eadababe8f/scratchpad/agent-laws-audit/`.

## 1. Audit (Task A)

122 records changed since 10-12 (51 added). Classes: **G 53, G+W 56, W 2, W-neg 2, F 2, borderline G+W\* 1, excluded 3 (P93/P99/P103, other agent), open 3.** Method: each claim read against the bound modules' theorem statements (a parser flags binder-free/`decide` theorems per module). Older records were classified from their claims plus statement scans, not proof-by-proof reading.

- **W**: the positive point rests only on constructed instances.
- **W-neg**: witness-only, but the point is a counterexample or limit. These are legitimate.
- **F**: general only over one constructed parametric law family (the support-gated family).

Records that are not plain G or G+W (the full 122-row table is in the appendix):

| record | modules | class | justification |
|---|---|---|---|
| finite-aggregation-within-restorable-basic-losses (P100, reviewed-scoped) | RepairComparison, Frame, GenerativeLossComparison | **W** | `StrictLossMatch` is defined generally, but every fact about it is proved by `decide` on one repair process |
| learned-procedure-transmission | evolution-connectionism/LearnedProcedureTransmission | **W** | one constructed finite history; only the `construct_*` lemmas are general |
| joint-difference-making | Joint | G+W\* | the dichotomy is general; "the difference belongs to the joint activity" is shown only in `Pool` |
| substitution-preserves-consumption | Substitution | F | `persists_consuming` covers the support-gated law family only |
| ranking-under-readings | Ranking, Bridge, … | F | the restraint/sharing verdicts hold only in the support-gated family; `ThirdParty` is a counterexample |
| becoming-finite-horizon | Horizon, Testing | W-neg | for every horizon a witness pair shows the class is not fixed by a prefix |
| derived-extent-limits | Continuation, Standpoints, Dependence | W-neg | four limits, each a minimal witness |
| consequence-revised-reference-plan / recurring-reference-revision / selection-under-registration-revision | ReferencePlan / ContinuingRevision / Revision | excluded | another agent has these (ReferencePlan: 22 of 43 theorems are closed `decide` facts) |

Every other P90–P105 Lean result is G or G+W: Regrouping, RegroupingSelection, TimedResponse, FallibleInquiry and P89 OpenFutureRevision.

**W count: 2** (P100 and learned-procedure-transmission). Add 1 borderline and 2 family-scoped. The 3 excluded records are not counted.

## 2. Task B

### 2.1 P100 — `Becoming.RepairComparison` (FR record)

**Current content.** The module defines a general `Frame.StrictLossMatch`, an injective, content-preserving map of losses plus one extra loss. It then proves the anchors (one protection is insufficient, three suffice, two against two only correspond), the fragile control and historical reading only for one constructed four-course repair process, by `decide`.

**Existing general pieces I reused.** From `GenerativeLossComparison`: `Strict` and `strict_improvement_transport`. From Metaethics: `Extension`/`Comparison`. From Population: `Distinct`, `length_le_of_matched`/`length_le_of_sub`, `marks_le_of_sub`, `search`, `decideSome`, `distinct_remove`, `mem_insert`. From Flow/Change: `total`, `mark`, `total_map`, `total_pos`, `total_congr_on`. From Dependence: `le_of_add_le_add_right`, because core `Nat.le_of_add_le_add_left` carries `propext`. No general strict-loss-matching law existed anywhere: Regrouping and GenerativeLossComparison have none.

**Proposed laws.** These are in the new pure-core module `Becoming.LossMatching`. The definition moves there unchanged. Every law below is for every `F : Frame S A C`.

| Lean (abridged) | Reading | 中文 |
|---|---|---|
| `StrictLossMatch.trans (chain : ∀ a b c, same a b → same b c → same a c) : M x y → M y z → M x z` and `StrictLossMatch.mono` (wider `same`, fewer losses at the better, more at the worse) | Matches compose and are monotone | 内容关系可传递时，严格损失匹配可复合；对损失单调 |
| `strictLossMatch_of_extension (refl) : Extension F living s t → M t s`; `SufficientMatching.comparison : F.SufficientMatching same scope Le → Comparison F living (fun s t => Le s t ∧ ¬ Le t s)` | A generative extension is identity matching, so P100's sufficiency commitment contains C | 生成扩展即恒等匹配；充分匹配承诺包含比较原则 C |
| `SufficientMatching.not_mutual`, `.not_self`; `EndlessLosses.self_match`, `EndlessLosses.no_sufficient_matching` | The commitment is consistent only where matching is asymmetric. With infinitely many losses (ℕ, shift by `succ`) a configuration strictly matches itself, so the commitment fails | 充分匹配只在匹配不对称处自洽；损失无穷时可自我严格匹配，故须有限 |
| `StrictLossMatch.length_lt (listedB : F.LossesListed b lb) (heldW) : M b w → lb.length < lw.length`; `.irrefl`, `.asymm`, `not_strictLossMatch_of_length_le` | With losses listed once, a strict match needs strictly more losses at the worse configuration, under any content relation. It is then a strict order | 损失有限列出时，严格匹配要求较差者损失严格更多 |
| **`strictLossMatch_iff_counts [DecidableEq C] (listedB) (listedW) : F.StrictLossMatch (fun c d => κ c = κ d) b w ↔ (∀ k, classCount κ k lb ≤ classCount κ k lw) ∧ lb.length < lw.length`** | **Counting law (Y iff Z).** With content read as class `κ`, a strict match exists exactly when the better loses no more in each class and fewer in total | 按内容类计数：每类不多、总数更少，当且仅当存在严格损失匹配 |
| `strictLossMatch_iff_length_of_alike (alike : lost-at-b c → lost-at-w d → same c d) : M b w ↔ lb.length < lw.length` | Within one class, a strict match exists exactly when the better configuration has fewer losses | 同类之内，严格匹配当且仅当损失更少 |
| `lossesListed_lostOf (distinct all) (every) : F.LossesListed s (F.lostOf s all)` | Finitely listed claims with decided realization list their losses | 请求有限且实现可判定时，损失可列出 |
| `not_strictLossMatch_of_kept`; **`not_strictLossMatch_of_base_lost (rests : ∀ s c, F.realized s c → F.realized s base) (distinct all) (every) (lost : ¬ F.realized b base) (w) : ¬ M b w`** | A kept counterpart class blocks matching. Where every claim rests on one common support, losing it ranks a configuration strictly below nothing, under any `same` | 所有请求依赖同一共同支持时，失去它的构型不严格优于任何构型 |
| `readsAt_iff_settled : (∃ support, F.ReadsAt r c τ support) ↔ ∀ t, τ ≤ t → (realized (r t) c ↔ realized (r τ) c)`; `ReadsAt.loss_retained`; `not_readsAt_of_recovery` | A claim is read at its time exactly when its realization is settled from then on. Restored support never re-realizes a missed claim | 请求按其时读，当且仅当自该时起已定；恢复支持不恢复已失请求 |

**The P100 example as an instance.** These theorems are added to the bridge `RepairComparison`, and the old theorems are kept.

- `matches_iff x y : M (final x) (final y) ↔ lostCount x < lostCount y` holds for all four courses, and `lost_counts : 3/4/3/2`. From these, `focal_matches_one_by_count`, `three_matches_focal_by_count` and `two_focal_neither` follow.
- `fragile_three_below_nothing` holds for any `same` and any `w`. It is stronger than `fragile_three_not_matching`.
- `reads_at_episode` shows that every owned episode claim is `ReadsAt` its episode time along every course, at all `t`.
- `focal_losses_retained` holds for all `t ≥ 3`.
- `sufficientMatching_iff` is `Iff.rfl`.

**Counterexamples to the converses.**
- `focal_one_not_extension`: the lower anchor matches but is no Extension.
- `EndlessLosses`: finiteness is needed.
- `two_focal_neither`: equal counts give a correspondence but no strict match.
- `not_readsAt_of_recovery`: a current-support reading is not read at the episode time.

**Scratch status: proved, with empty axiom reports.** `scratch_build.py` builds cleanly with no warnings:
- `Becoming.LossMatching`: 34 theorems, 42 declarations, `with_axioms {}`.
- `Becoming.RepairComparison`: 36 theorems (17 old and 19 new), 65 declarations, `with_axioms {}`.

Files:
- `tree/Becoming/LossMatching.lean` (494 lines)
- `tree/Becoming/RepairComparison.lean` (410 lines)
- `build-output.txt`

Not run: the checker's environment audit, controls and the prelude-only compile. LossMatching imports only core modules (Population and Metaethics, a closure of 14 modules). No `sorry`.

**Not done.** An exact characterization for a non-equivalence `same` would be a Hall condition; only `length_lt` (necessity) is general there. The parametric FR family "a episodes against m single episodes ⇒ match iff m > a" is now arithmetic on `strictLossMatch_iff_length_of_alike`. It is not built as its own process family.

**Record change.** Replace the claim's P100 sentence with this one: "For every frame with content classes and finitely listed losses, strict loss matching holds exactly under per-class domination with strictly fewer losses (`strictLossMatch_iff_counts`). It composes and is a strict order. It contains C as identity matching, and it is inconsistent with sufficiency over infinitely many losses. The repair process is an instance: loss counts 3/4/3/2 give one protection insufficient, three sufficient and two unresolved. A lost common support blocks every match."
- Add `Becoming/LossMatching.lean` to `proof_bindings`.
- Limitations: the counting law needs class-equality content; `SufficientMatching` stays a normative commitment; Hall is open.
- Status stays reviewed-scoped, because FR is normative.

**Effort and risks.** Landing is integration only, about half a day:
- register the module in `Becoming.lean` and the checker;
- the `Frame.StrictLossMatch` declaration moves from the RepairComparison registry to the new module;
- update the spine §9 totals (+34 core, +19 bridge);
- update the record and the argument §11 text.

Names (`LossMatching`, `EndlessLosses`, `ReadsAt`, `lostOf`) need Ren's naming check. There is no overlap with P93, P99 or P103 modules.

### 2.2 Other results flagged

None of these was attempted in Lean.

- **learned-procedure-transmission (W, periphery).** Proposed laws:
  - `expose_isSome_iff : (expose ch ts s).isSome ↔ 0 < s.active ∧ s.active*ts.length ≤ s.source`. The existing `exhausted_source_blocks` is one direction.
  - `reconstruct_isSome_iff : … ↔ s.tested ∧ 0 < capacity s`.
  - `reconstruct_inherits : reconstruct ch t s = some s' → s'.kit.network = inheritedRecord t s ∧ s'.kit.apparatus.inhibit = inheritedProcedure t s`.
  - Support conservation across `reconstruct`.

  In words: wherever the source covers the demand and capacity is positive, every expose–reconstruct cycle passes on the retained matrix and procedure bit, with support accounted. The constructed history becomes an instance. The module is periphery (simp/omega allowed). Effort about half a day; risk low.
- **joint-difference-making (borderline).** Generalize `MakesDifference` to a decided part `part : F → Bool`. Law: if withholding each single member leaves a breaking step by the same move, and withholding the whole part keeps the dependence, then the part makes the difference and no member does. `Pool` becomes the instance. This is core and small (≤ 1 h), and close to definitional.
- **F results (substitution-preserves-consumption, ranking-under-readings).** A Part I lift would be a Web-level law: `ConsumingIn` is kept under any change of dependence that keeps the draw on the consumed condition. Lifting the restraint verdicts needs Ren's decision on whether family-scoped results must be lifted. Medium effort.
- **W-neg results.** No change is needed; they are legitimate counterexamples.

## 3. Recommended order

1. Land P100 (`LossMatching` plus the bridge instances). It is verified in scratch; claim it on the work board and land it in the integrator's queue. It is independent of the other agent's P93, P99 and P103.
2. joint-difference-making: the part-level law (small, core).
3. learned-procedure-transmission: the iff laws (periphery).
4. The F-scoped lifts, after Ren rules on whether family-scoped results need lifting.

## Appendix: full audit table (122 records)

| record | modules (first 4) | class | justification |
|---|---|---|---|
| attraction-is-not-returning | Attraction, Recurrence, Frame | G+W | Law.* over every determined law; small laws refute converses |
| axiom-decomposition | Boundaries, Feedback, Interdependence, Significance … | G | boundary-invariance iffs over every standpoint/presupposition |
| becoming-dependence-dynamics | Dependence, Renewal, RelationalRenewal | G+W | web readings for every run; RelationalRenewal shows cases |
| becoming-finite-horizon | Horizon, Testing | W-neg | for every h a witness pair: class not fixed by a prefix (legit negative) |
| becoming-renewal-reading | Renewal, Metaethics, Frame, RelationalRenewal … | G+W | general readings; one-process witness: class belongs to the run |
| becoming-return-grades | Return, Dependence | G+W | grade order general; seasonal witness separates grades |
| becoming-spine-instances | Bridge, Frame, Metaethics, WholeGroundCoverage … | G | instance/equivalence theorems for every closure, chain, frame |
| becoming-stepwise-reading | Metaethics, Dependence | G+W | stepwise reading general; witnesses separate run/step |
| bounded-census-keeps-pace | Population, Openness, Dependence, Change … | G+W | Listed.ceasing_of_coming for every listing; procession control |
| causal-models-as-processes | Mechanism, Experiment, Joint | G | every F : X → U → E → X |
| ceasing-needs-arising | Population, Openness, Dependence, Change … | G+W | Listed.coming_of_ceasing general; one-way census control |
| census-balance-under-continuation | Identity, Population, Flow, Change | G+W | every continuation R; budding/self controls |
| census-balance | Population, Openness, Dependence, Change … | G | Listed.across / over_stretch for every listing |
| classification-robust-generative-comparison | PracticalJudgment, ConcernExtension, RelationalOrganization, JointContinuationClassification … | G | iff over all fresh classifications |
| closing-needs-net-draw | Admission, Flow, Dependence, Change | G | every balanced flow and decided part |
| closure-verdict-meets-axiom | Interdependence, Significance, Regions, Admission | G | retains_bounded_iff_includes for all regions |
| coming-and-ceasing-keep-pace | Change | G | every web, no premise |
| comparison-by-widening | Significance, Regions, Metaethics, Admission | G | paths_extension_iff_widens for every web |
| comparison-content-under-regrouping | Regrouping, Significance, Admission, Counterfactual | G+W | fidelity iffs general; Transfer witness shows hidden mixed loss |
| comparison-where-the-rest-responds | Response, Testing, Feedback, Flow … | G+W | responsive-reach closure laws general; forest controls |
| comparison-within-reach | Feedback, Significance, Admission, Regions | G+W | comparison_local general; wolves/forest controls |
| condition-correspondence-discipline | Correspondence | G | idle-condition laws on every web |
| configurations-alike-by-relation | Unfolding, Joint, Frame, Mechanism … | G+W | bisimulation laws for every frame; controls |
| consequence-revised-reference-plan | ReferencePlan | excl. | P99, other agent (ReferencePlan: 22 of 43 theorems by decide) |
| consumption-ends-with-feeders | Interdependence, Continuation, Regions, Flow … | G+W | unfed_consumption_ends general; steady/withheld controls |
| contextual-registration | Context, Quantum, Frame | G+W | glues_iff_agree general; no-global witnesses |
| continued-change-needs-openness | Openness, Dissipation, Flow, Roles … | G+W | standing_runs_down etc. general; hatch/holding controls |
| continuing-self-fed-from-beyond | Continuation, Dissipation, Roles, Flow … | G+W | inward_iff_not_fed general; relay witness |
| continuous-time-as-tower | Tower, Sampling, Locality | G | every tower |
| conveyance-crosses-the-boundary | Standpoints, Continuation, Roles, Descent … | G | boundary_crossed under stated premises |
| counterfactual-is-the-course | Counterfactual, Response, Testing, Mechanism … | G+W | ExchangeLaw laws general; reply/escalation controls |
| counting-standing-and-dependence | Standing, Counting, Openness, Population … | G+W | standsObey_iff general; driven-queue counterexample |
| counting-under-enclosure | Population, Openness, Premises, Counting … | G+W | enclosure_bounds_change general; controls |
| counts-exist-where-decided | Decidedness, Change, Space | G | indicates_iff_decided etc. |
| derived-extent-limits | Continuation, Standpoints, Dependence | W-neg | four limits, each a minimal witness (legit counterexamples) |
| determinacy-up-to-likeness | Branching, Unfolding, Joint, Mechanism … | G | up-to-likeness laws for every process |
| entropy-history-and-record | Entropy, Resolution, Recurrence, Openness … | G+W | history_mono, restores_levels_not_history general |
| evolution-on-descent | Evolution, Change, Flow | G | Price identity over every finite family |
| exchanges-commute-unless-joined | Order, Flow, Dissipation, Dependence … | G+W | commute_laws general; reorders controls |
| experiment-needs-return | Experiment, Joint, Recurrence, Frame … | G | not_fixes_of_untaken for every determined process |
| feedback-and-reach | Feedback, Admission, Flow, Regions … | G+W | levels_agree/support_agrees general; dweller controls |
| feeding-closure | Interdependence, Standpoints, Regions, Significance … | G+W | closure laws general; store/dweller controls |
| finite-aggregation-within-restorable-basic-losses | RepairComparison, Frame, GenerativeLossComparison | W | P100: StrictLossMatch general def, every fact by decide on one repair process |
| finite-fallible-inquiry-necessity | ScientificInquiryNecessity, FallibleInquiry | G+W | coverage bounds general; P94 omitted-exchange controls |
| four-cases-of-a-part | Admission, Regions, Continuation, Significance | G | closes_nothing/opens_nothing for every balanced flow |
| generalization-through-lumping | Learning, LearningCorrespondence, Mechanism, Selection … | G+W | lumped_determines iff general; updating controls |
| generation-is-replenishment | Roles, Dissipation, Flow, Reserve | G+W | general under one-kind reading; not_dissipative control |
| held-lives-g0-is-centering | Standpoints, Metaethics | G+W | significant_iff_held general; each-needed witnesses |
| histories-fix-law-up-to-dead-ends | Histories, Unfolding, Joint, Frame … | G+W | ShownBy/SpliceClosed iffs general |
| identification-where-bounded | Identification, Learning, Description, Unfolding … | G | bounded_agree, statesBelow_iff_lasso |
| identity-across-steps | Identity, Persistence, Unfolding | G | every re-identification |
| imbalance-as-relatum | Imbalance, Resolution, Flow, Premises | G | withImbalance laws for every flow |
| joint-difference-making | Joint | G+W* | dichotomy general; "difference belongs to the joint" only in Pool |
| laws-at-coarser-steps | Sampling, Locality, Change, Premises | G | composition laws for every sampling |
| laws-at-finer-units | Units, Locality, Resolution | G+W | every r; endless control |
| laws-of-one-step-complete | OneStep, Flow, Population, Space … | G | Realizes.every and iffs |
| laws-of-one-step | Locality, Openness, Roles, Counting … | G | localized laws, every world |
| learned-procedure-transmission | LearnedProcedureTransmission | W | one finite constructed history; general construct_* lemmas only |
| learning-by-refutation | Learning, Recurrence, Testing | G | no_record_fixes_next for every course |
| least-footprint-where-idleness-decided | OrderNormal, Order | G | least_exists_iff |
| levels-of-closure | Feedback, Bridge, Interdependence, Regions … | G+W | closure laws general; reach controls |
| life-as-condition-of-life | Roles, Correspondence, Locality | G | every one-kind reading |
| listing-once-is-decided-identity | Listing, Population, Space, Openness … | G+W | listsOnce_iff_decided; needs_once control |
| living-on-and-descent | Descent, Evolution | G+W | LivesOn laws general; Drowsy/Mutualism possibility witnesses |
| loss-beyond-a-region | Regions, Admission, Continuation, Standpoints | G | every region |
| losses-of-the-sum-over-histories | Weighted | G+W | truncation general; Interference cancels witness |
| map-of-premises | Premises, Space, Dissipation, Population … | G+W | premise implications general; hatch/draining controls |
| metaethical-core-characterization | Metaethics, Inquiry, Frame, InquirySufficiency … | G | G0 iff seed+N_rel+N_std |
| more-needs-renewers | Flow, Population | G | every balanced flow |
| necessarily-drawn-is-not-returning | Branching, Attraction, Recurrence, Frame … | G+W | necessarilyDrawn_iff_not_returns; controls |
| no-finite-part-bears-taking | Dissipation, Dependence | G | every dissipative balanced flow |
| normal-forms-need-decided-apartness | OrderNormal, Order | G | rearranges_iff, normalForm_iff |
| one-axiom-yields-g0 | Significance, Metaethics, Frame, Admission … | G | under Unrestricted, every valuation |
| one-step-missing-laws | OneStep, Locality | G+W | whole law general; standing-bound control |
| only-the-order-of-change-registers | Order, Sampling | G+W | stutter_premises_iff; step-relative controls |
| open-form-realization-under-revision | OpenFutureRevision, ContinuationRenewal, PositiveGroundUncertainty, Bridge | G+W | finite-renewal bound general; revising run counterexample |
| order-of-exchanges-is-the-invariant | Order, Flow, Dependence | G | Precedes order laws |
| organizational-formation-from-generative-comparison | RelationalOrganization | G | (reviewed-scoped) every finite eligible range |
| own-count-misses-joint-excess | Continuation, Flow | G+W | joint_keeps/excess_bounded; Pair control |
| practical-judgment-g0-j | PracticalJudgment | G | (reviewed-scoped) conditional on J1–J4; not re-read in depth |
| presupposition-scopes | Boundaries, Feedback, Interdependence, Significance … | G | Boundary/SuperTrue laws |
| process-and-frame-as-readings | Unfolding, Space, Flow, Generation … | G+W | withMove/closedBy iffs; controls |
| projection-carrying-a-law | Mechanism, Experiment, Joint, Recurrence | G+W | image_determined_iff; controls |
| ranking-under-readings | Ranking, Bridge, Relevance, Significance … | F | restraint verdicts only in the support-gated family |
| recurrence-without-decidedness | Decidedness, Change, Space | G | every finite family |
| recurrence-without-premise | Recurrence, Frame | G | every law of change |
| recurring-reference-revision | ContinuingRevision | excl. | P103, other agent |
| registration-within-what-it-registers | Diagonal, Frame, Recurrence | G | diagonal laws for every ψ |
| relata-counted-up-to-indiscernibility | Listing, Decidedness, Unfolding, Sampling | G | numbersBy_iff_decided |
| represented-boundary-against-dependence | Regions, Admission, Dependence, Flow … | G | RenewingOver laws |
| reserve-defers-ending | Reserve | G+W | Carries laws general; seed/cascade controls |
| rest-at-every-resolution | Resolution, Openness, Dissipation, Flow … | G+W | general at every r; quantum controls |
| rest-with-refinement-counted | Resolution, Openness, Dissipation, Flow … | G | balancesAt_iff_withRefinement |
| returning-where-the-course-branches | Branching, Recurrence, Frame, Unfolding … | G+W | Branching laws; fork/merge controls |
| rising-and-falling-in-one-exchange | Dissipation, Flow, Roles | G | every balanced flow |
| runaway-distance-unregistered | Runaway, Testing, Dependence, Flow | G | every policy through registration |
| runs-on-families-chosen-step-by-step | OneStep | G | step_*_iff (section variables) |
| scientific-inquiry-foundation |  | open | no Lean claim |
| seeking-boundary | Seeking, Locality, Recurrence | G | Law.rests_iff, more_never_rests |
| selection-through-registration | Selection, Testing, Feedback, Capture … | G+W | selects_alike_iff; dweller controls |
| selection-under-registration-revision | Revision | excl. | P93 example part, other agent; iff part general |
| separation-loses-the-relation | Description, Context | G+W | separation_faithful_iff; parity/Specker witnesses |
| significance-retained-within-margin | Significance, Admission, Dependence | G | Retains laws |
| space-and-its-parts | Space, Change, Roles, Reserve … | G+W | general over the space; seedbank/grazing controls |
| substitution-preserves-consumption | Substitution | F | persists_consuming over the support-gated law family only |
| subthreshold-registration | Testing, Admission, Feedback, Roles … | G+W | difference_kept etc.; gauge controls |
| sum-over-histories-exact | Weighted, Mechanism, GenerativeCore | G | sum_courses for every weighting |
| support-from-the-supported | Admission, Change, Flow, Dependence … | G | GainsSupport.rises etc. |
| target-capture | Capture, Evolution, Flow, Locality … | G | share_not_lower/share_rises over every family |
| testing-within-registration | Testing, Feedback, Admission, Inquiry … | G+W | registration laws; model controls |
| tests-fix-likeness-where-determined | Histories, Unfolding, Frame, GenerativeCore | G+W | alike_iff_sameTests; early-choice counterexample |
| the-split-that-makes-sense | Description, Unfolding, Mechanism, Recurrence … | G+W | makesSense laws; registration controls |
| timely-response-necessity | TimedResponse, FallibleInquiry | G+W | Spread/ReachedBy laws general; 2-step controls |
| transmission-independent-where-it-binds | Transmission, Premises, Space | G+W | drop laws general; finiteHatch pair |
| transmission-is-inheritance-and-need | Transmission, Evolution | G | transmits_at_iff |
| unceasing-generation-needs-renewal | Generation, Flow | G | every web |
| universal-practical-warrant |  | open | no Lean claim |
| whole-first-and-bounded-centers | Significance, Regions, Continuation | G+W | retains laws; Clearing refutes converse |
| whole-law-of-counting | Population, Premises, Openness, Counting … | G+W | tally laws; balance_not_tally control |
| whole-persists-through-generation | Wholes | G+W | Whole laws; generations/immortal controls |
| wisdom-root-part-one | Testing, Inquiry, Experiment, Selection … | G | (reviewed-scoped) checked laws over every learner etc. |
| wisdom-root | GenerativeClosure, JointInterpretation, AcquiredBinding, InferentialGrounds … | open | no Lean claim of its own |
