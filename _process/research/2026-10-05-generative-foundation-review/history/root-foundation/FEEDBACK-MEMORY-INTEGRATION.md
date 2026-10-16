# Retained memory, saturation and whole-history feedback bounds

8 October 2026. AI-authored continuation of the active request to **compose existing results, explain a supplied premise, and establish real-world correspondence**. The preceding turn made verified progress: [physical correspondence and premise explanation](INQUIRY-JUDGMENT-EMPIRICAL.md), its independent review and source-bound integration checks passed. This continuation addresses the specific per-step retained-memory premise identified by that review. It reuses the same preserved physical records and controller law; it is not another physical experiment.

## Affirmative contribution and the exact missing premise

The earlier command theorem assumes a reading discrepancy `E` and a retained-integral discrepancy `M` at the instant of the command. Its plant-horizon theorem requires an appropriate command bound at every step. Providing only an initial memory error does not discharge those later hypotheses. The inspected controller has two branches: when the tentative command lies in [0,100], retain the integral increment; outside that range, cancel it. Even nearly identical readings can straddle this branch boundary.

The new account explains the later memory discrepancy from the **initial memory relation, the actual recurrence, the readout domain, targets and elapsed intervals**. Measurement, retained integral, issued command and subsequent response remain related aspects of one continuing process. The nominal and compared histories are analytical descriptions whose equivalence conditions are stated; they are not separate ontological subjects and worlds.

The relevance to practical judgment is exact: an uncertainty-sensitive response comparison must preserve the memory and saturation relations through the history it compares. A proof that substitutes zero memory difference at each step can certify the wrong command interval. The current work supplies that previously unproved implementation condition. G0/J commitments, the importance of the affected lives, permissions, physical thermal response and justified future readout bounds do not follow from it.

## The propagated bound

For the same target `r`, interval `dt` and PI gains, let `j` be nominal retained integral, `z` nominal readout, `b = Ki (r-z) dt`, and `v = Kp (r-z) + j + b` the tentative nominal command. Starting from a justified memory radius `M` and readout radius `E`, the already inspected mechanism yields:

- raw-command radius `C = |Kp + Ki dt| E + M`;
- increment radius `A = |Ki dt| E`;
- issued-command radius `min(100,C)` from the clipping range.

The next memory radius depends on where the entire tentative-command interval lies:

| Certified branch | Next memory radius | Why |
|---|---:|---|
| `v+C < 0` or `100 < v-C` | `M` | Both recurrences reject their increments. |
| `0 ≤ v-C` and `v+C ≤ 100` | `M+A` | Both retain their increments; the incremental discrepancy is bounded. |
| Neither condition | `M+A+|b|` | One recurrence may retain an increment which the other rejects. |

The strict exterior and inclusive interior agree with the archived source. The uncertain case bounds all possibilities rather than assuming both executions take the observed branch. Induction supplies the memory radius at every step. The command theorem consumes those derived radii, and the new plant theorem directly calls the previously checked `MeasuredFeedback.measured_feedback_horizon`. Plant defects, response sensitivity and realization of both plant histories remain explicit hypotheses. In particular, a transformed readout file is not evidence that a counterfactual thermal trajectory follows it.

This is a conservative scalar enclosure. It can lose dependence between uncertain reading, memory and branch choice. Soundness of a bound does not establish that it is tight, useful for a particular decision, or empirically warranted outside its input domain.

## A genuine source-mechanism counterexample

`FeedbackMemory.saturation_boundary_hidden_memory` checks the following for **every positive δ** under gains `Kp=Ki=1`, equal initial memory zero and interval one:

- target 100, reading 50 gives tentative command 100 and retained integral 50;
- reading `50−δ` gives a command clipped to 100 and retained integral zero;
- both current issued commands are identical, although the memory difference is 50;
- at a subsequent shared zero-error sample, the issued commands differ by 50.

The theorem concerns the same branch law as the physical controller with illustrative gains; it does not claim those exact values occurred in the archived trials. It shows why clipping's nonexpansiveness does not provide continuity of the retained-memory transition at this boundary. The earlier one-step theorem is still valid. Its repeated use requires the derived memory term instead of repeatedly assuming equal memory.

## Exact archival computation and meaning of the uncertainty domain

[Producer](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/analyze_memory.py) · [all exact certificates and results](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/memory-results.json) · [unchanged original provenance](../../../../sources/tclab-benchmark/PROVENANCE.json).

The producer reads the preserved decimal strings into rational numbers and uses the previously recorded gains. The nominal recurrence differs from logged floating-point commands by less than `10⁻¹⁰` percentage points; the successful earlier floating replay and its separate limitations remain credited. We do not claim a kernel-verified floating-program refinement.

For each of three published physical runs, four readout sequences are evaluated: unchanged, previous recorded reading, current reading plus one degree, and current reading minus one degree. All start with equal integral zero and retain the original targets and actual recorded interval differences. **Twelve sequences and 7,176 recurrence updates** are checked. This count includes three unchanged controls; it is not twelve physical trials or 7,176 independent observations. The 7,176 row certificates retain exact command and memory values, radii and branch certificates.

For the previous-record sequence, `E_t = |z_t−z_(t−1)|` is exactly calculable from these files, so membership of that particular transformed sequence is established. The general radius theorem covers every sequence within those pointwise radii. **That domain is retrospective:** knowing the current difference requires the current reading. It does not authorize skipping the next measurement or bound unknown physical evolution during an unobserved delay. The ±1-degree domains are declared sensitivity scenarios, not learned noise distributions or calibrated sensor specifications. Gains, targets and elapsed intervals remain equal between the nominal and compared recurrences.

| Run and transformed readout | Maximum command difference, percentage points | Maximum proved-model command radius | Steps exceeding a falsely memory-free bound | Saturation-branch disagreements |
|---|---:|---:|---:|---:|
| Initial, previous record | 3.430415 | 11.938047 | 285 | 5 |
| First validation, previous record | 3.786149 | 100 | 258 | 5 |
| Second validation, previous record | 7.921460 | 100 | 248 | 3 |
| Initial, +1°C / −1°C | 13.996246 / 15.169441 | 64.706743 | 415 / 440 | 25 / 24 |
| First validation, +1°C / −1°C | 39.490422 / 44.662882 | 100 | 377 / 387 | 103 / 50 |
| Second validation, +1°C / −1°C | 38.471591 / 46.666780 | 100 | 374 / 388 | 117 / 47 |

The falsely memory-free bound is the earlier command expression with `M=0` at every step. These exceedances refute that unauthorized substitution, not the original conditional theorem. The exact propagated bound contains every evaluated command and memory difference. Unchanged readouts have zero memory and command radii throughout.

The 100-point bounds expose lost precision: they are no narrower than the physical command range. The retained-memory radius reaches approximately 418 in one sensitivity domain while the evaluated memory difference is below 37. A loose universal enclosure and a small selected trajectory difference answer different questions; one selected path cannot tighten the whole domain without proof. All loose bounds and branch disagreements remain in the result file.

## Timing, movement and comparison

The recurrence uses each recorded interval rather than silently replacing it by one second. Both compared sequences use the same intervals. Logs record time before temperature acquisition and command transmission; those intervals are not measured end-to-end sensor/actuator latencies or exact switching timestamps. Nothing here establishes an unmeasured physical deadline.

Two additional induction results transport command radii into total absolute command movement and interval-weighted command exposure. The exposure follows the same left-held convention as the preceding study: interval `t` uses command `t`, including the initial zero command. The metric certificates are evaluated for every sequence. Percent-seconds remains commanded exposure, not measured electrical energy. A final interval-separation theorem preserves the condition needed for a robust cost comparison; overlapping bounds do not prove a reversal or select a response.

This gives a connected conditional route from readout and initial memory through the complete command history to plant-error and burden estimates. A practical conclusion still needs an independently justified readout domain, actual plant response, relevant alternatives, timely feasibility and a warranted comparison. More precise engineering estimates do not manufacture those normative premises.

## Lean source, correspondence and proof audit

[FeedbackMemory.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/FeedbackMemory.lean) imports the existing `MeasuredFeedback` module. [Fresh checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/check_feedback_memory.py) rebuilds all six repository modules from source, with the existing pinned Mathlib cache, and records every explicit declaration's logical dependencies. Generated constructors are kernel checked with their modules. [Receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/feedback-memory-verification.json).

| New formal component | Premises and scope |
|---|---|
| `raw_error`, `increment_error` | Same gains, target and interval; supplied reading and initial/current memory bounds. |
| `retained_interior_error`, `retained_mixed_error`, `retained_margin_error` | Actual branch law; exact inclusive/strict thresholds; scalar enclosure may be conservative. |
| `memory_horizon` | Both retained-memory recurrences, initial memory bound and casewise readout bounds. No independently supplied later memory bounds. |
| `command_difference_at_most_100`, `command_horizon` | Prior command range and the new derived memory history. |
| `controller_plant_horizon` | Direct composition into the preceding plant theorem; plant realization, defects and response sensitivity still supplied. |
| `saturation_boundary_hidden_memory` | General positive perturbation witness under stated illustrative gains and values. |
| `movement_error`, `exposure_error`, `separated_costs` | Command radii and matched intervals; nonnegative interval lengths for exposure; disjoint warranted cost intervals for comparison. |

There are **13 new theorems / 21 new explicit declarations**, with **168 audits across the six-module closure**. Validation status and immutable source bindings are recorded in the receipt; a source listing or finite calculation alone is not mathematical validation. Standard logical dependencies remain disclosed, with no custom axiom, `sorry`, `native_decide` or unsafe bypass. Compiler executable and pinned-cache limitations are the same as in the preceding accepted review.

## Substantive counterreview and next inference

**Could conventional control theory already express this?** Yes. This is an explanation and verified composition of the inspected controller, with no claim to invent hybrid control or show unique superiority of the generative terminology. Its contribution to the shared theory is a traced missing hypothesis and a concrete failure when that relation is omitted.

**Is this merely another isolated model?** It imports and uses the exact prior PI definitions and plant-bound theorem, and evaluates the same physical-source records. The new retained-memory recurrence is the one already present in the archived controller. It closes a specific missing premise; it does not relabel the thermal record as the earlier toy dose process.

**Does the finite replay verify every possible perturbed history?** No. Lean supplies the quantified implication under its hypotheses. Rational replay checks the implementation of that construction on the declared archived transformations and retains exact certificates. Independent reconstruction is a separate evidence layer. Neither layer establishes absolute temperature truth.

**Does the favorable bound solve the practical question?** Some enclosures are deliberately recorded as too broad to certify a narrow comparison. The completed conditional step is now initial/readout uncertainty → retained memory → commands → supplied plant and burden bounds. The governing [completion audit](THREE-CONNECTIONS-COMPLETION-AUDIT.md) remains active: future readout warrant, physical response/timing, corrected candidate generation and justified practical comparison remain to be integrated. The next work should test the archived tuning procedure's model and objective contracts; it should not reintroduce an unexplained per-step memory bound or claim measured future calibration from these retrospective domains.
