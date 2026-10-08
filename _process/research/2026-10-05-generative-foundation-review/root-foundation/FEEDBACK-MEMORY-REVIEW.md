# Independent review: retained feedback memory and saturation

8 October 2026, Asia/Bangkok. AI-authored independent completion-stage review of the local feedback-memory continuation. The reviewer did not write its source, producer or argument. Read the [integration](FEEDBACK-MEMORY-INTEGRATION.md), `FeedbackMemory.lean`, its checker/receipt, the numerical producer and complete results/certificates; inspected the relevant inherited PI definitions and plant-horizon hypotheses from the preceding reviewed study. The shared nondual method and explicit normative-axiom scope continue to apply.

**Verdict: accepted at the stated local scope; no required repair found.** This closes the formerly supplied per-step retained-memory bound by deriving it along the actual declared recurrence. It also demonstrates a genuine failure of repeatedly substituting zero memory discrepancy. The numerical study is retrospective controller evaluation on the same archived readings, not additional physical validation of altered actions. The wider three-part goal remains active.

## Independent verification and preserved evidence

The [independent Lean runner](development/feedback-memory-review/check_lean_review.py) compiled all six repository modules from current source in fresh scratch and generated a complete declaration audit. The runner reuses the inspected author's closure parser, not the author's compilation entry point. The existing pinned Mathlib cache was reused, while no compiled repository module was reused. No original source or author receipt was overwritten.

All six modules—`GenerativeCore`, `SystemsOrganization`, `RelationsAcrossScales`, `EmbodiedChoiceScales`, `MeasuredFeedback`, `FeedbackMemory`—compiled without warnings or errors. All **168 explicit-declaration audits** passed, including **13 new theorems and 21 new declarations**. Only the recorded standard logical dependencies are admitted. Generated declarations are kernel-checked with their modules. [Independent receipt](development/feedback-memory-review/verification.json), [axiom log](development/feedback-memory-review/axioms.txt) and [audit source](development/feedback-memory-review/Audit.lean) are retained with the six module logs. The independent run completed at `2026-10-07T21:34:33.212341+00:00`, which is 8 October in Asia/Bangkok.

The [independent rational runner](development/feedback-memory-review/check_rational_review.py) imports neither the producer nor its predecessor. It retains unweighted accumulated error and multiplies by the integral gain when needed, rather than duplicating the producer's weighted-memory representation. It constructs raw-command interval endpoints from the readout and memory enclosures, then uses interval containment to determine the branch certificate. [Receipt](development/feedback-memory-review/rational-verification.json) and [full output](development/feedback-memory-review/rational-log.txt) preserve its results.

**Every field of all 7,176 exact row certificates and every reported summary value agrees exactly.** The comparison includes nominal/variant commands, next memories, prior/next memory radius, reading/raw/command radii, branch labels, branch disagreements and false-zero-memory failure indices. The twelve sequences include three unchanged controls; all three retain zero errors and zero radii throughout. These are not twelve new physical trials.

| Binding | SHA-256 or snapshot |
|---|---|
| New Lean source | `b36ea4f3949ccb1354fdb4e5bb5bc6a46ee50f097f96e0996526b977cb1c8d12` |
| Author Lean checker | `c1ed01aee675ebe4b9488a280baa4bf25a4e8de23ca056e547edaf259d6e8bcd` |
| Numerical producer | `57e3a1ead595bdf6b2b99535152a7f8a2562b778556937f01e3571e035676a84` |
| Numerical results | `b8bcb98bee2e4a56fac821b4c15561f389298151f23c2ab91666450ef733f8e9` |
| Integration at substantive review | `52470aaaaa03123e6967c8b7b51cfbcb23de09becf261196909fefcbbfab6e5e` |
| Author formal snapshot | `feedback-memory-checks/20261007T213114.163118Z` under the analysis directory |

Current module bytes, preserved snapshot sources, checker, executable, manifest, logs and recorded absolute direct-import fingerprints matched the author's receipt. The toolchain limitations remain those already disclosed: upstream caches were not rebuilt, and `bin/lean` alone does not fingerprint the linked runtime. This is actual local independent compilation, not a hermetic toolchain attestation. Build products were confined to temporary scratch; only unique review scripts, audit source, logs and receipts are preserved.

## Soundness of the branch-dependent enclosure

The raw discrepancy is correctly decomposed into reading contribution and prior-memory difference, with absolute gain coefficient `|Kp + Ki dt|`. The increment discrepancy separately uses `|Ki dt|`. These identities retain the same target, gains and elapsed interval on the two compared paths. They do not claim to cover unequal targets or unrepresented timing errors for free.

The exterior condition is strict. If the whole nominal raw interval is below zero or above 100, both paths reject their increments, so the previous memory radius suffices. The interior condition includes zero and 100, matching the archived controller's source-level strict saturation test; both paths then keep the increments and their difference is bounded by `M+A`.

The uncertain case genuinely covers all four branch combinations. If only the nominal path retains its increment, its extra magnitude is bounded by `|b|`. If only the compared path retains, its increment is bounded by its discrepancy from the nominal increment plus `|b|`. If both retain, `M+A` already suffices; if both reject, `M` suffices. Hence `M+A+|b|` is sound across these cases without assuming observed nominal and variant branches coincide. The proof's implicit nonnegativity follows from the absolute-value premises; it does not silently assume a possibly negative radius is meaningful.

`memory_horizon` uses initial discrepancy and both actual retention recurrences to derive later discrepancy by induction. It does not receive the later memory bounds as extra premises. `command_horizon` consumes that result and combines it with the established [0,100] command range. `controller_plant_horizon` directly applies the earlier `MeasuredFeedback.measured_feedback_horizon`, supplying the generated command bounds. This is an actual formal composition, not a restatement with an unrelated success predicate.

The plant theorem still assumes both physical/model trajectories follow their declared laws, appropriate projection defects, state-error propagation and response sensitivity. The controller theorem does not establish those premises from the archived temperature series. This separation is explicit and appropriate.

## The boundary witness is a genuine mechanism counterexample

With the stated unit gains and interval, target 100 and readout 50 produce raw command 100. Because the boundary belongs to the updating branch, retained memory becomes 50. Any positive perturbation to `50−δ` raises raw command above 100, so the other path rejects its increment and retains zero. Both issued commands are 100; at the next shared zero-error sample they differ by 50.

This holds for every positive δ, so arbitrarily small readout differences expose a fixed retained-memory discontinuity. It is not a freely toggled memory predicate: the same actual branch law generates both outcomes. It does not refute command clipping's nonexpansiveness with fixed memory, nor the preceding conditional command-error theorem. It refutes extending that fact to repeated execution while erasing memory history. The illustrative gains and boundary values are not reported as observations from the archived runs.

## Numerical correspondence and indexing

The review reconstructed all twelve exact-rational trajectories from the preserved decimal readings and the previously recorded gain values. The initial gain is the rational interpretation of the earlier reported floating gain, not a newly claimed exact derivation of its original tuning formula. This is disclosed by the producer's recorded-gain input and remains consistent with its small nominal-command replay discrepancy. Real-arithmetic retention is not a verified refinement of floating subtraction at saturation boundaries.

All transformed paths use the same target and intervals and begin with equal integral zero. For the previous-record transformation, the pointwise radius is the observed adjacent difference. Its membership is exact retrospectively; knowing that radius requires the current recorded reading. It cannot be used to justify skipping an unknown future observation. The ±1°C cases are declared sensitivity domains, not inferred noise distributions, absolute sensor certificates or predictions of future temperature error.

There are 599 command positions per sequence, including the initial zero command, and 598 updates. Movement uses all 598 adjacent command differences. Its difference enclosure adds the radii at both endpoints of each movement. Exposure uses exactly 598 left-held intervals: the first interval uses the initial command, and the last newly computed command has no later measured interval in this file. Both compared paths use the same intervals. The proof and numerical implementation agree on this shift; no extra last interval or right-held command was inserted.

The retained radius can be very conservative: the second validation's ±1°C domains reach approximately `417.967` memory units, while the selected minus-one path's maximum memory difference is `36.667`. Command bounds of 100 are merely the full actuator range and cannot certify a narrow comparison. The report retains those cases rather than claiming a tight enclosure. A single successful perturbed path would not justify shrinking the radius for every member of the broader domain.

The thousands of exceeded falsely memory-free bounds and the preserved saturation disagreements agree with the report. They reject the unauthorized assumption `M=0` at every step; they are not failures of the correctly stated original one-step bound. All unchanged controls satisfy exact equality. The exact numerical certificates check these sampled recurrences; the quantified domain implication comes from Lean, not from counting the sampled paths.

## Practical and foundational scope

Commanded exposure remains a proxy, not measured energy. Logged cycle intervals remain distinct from exact switching times or end-to-end latency. No counterfactual heater experiment is implied by driving the mathematical controller with a modified recorded sequence. Altered real commands would ordinarily alter later real readings, which this fixed-input replay deliberately does not simulate or observe.

`separated_costs` requires independently warranted intervals that actually separate. Overlap is not a demonstrated reversal, and the theorem does not decide which cost has normative priority. G0, protection/authority commitments, the relevant affected lives and justification of future readout domains remain separate from the controller arithmetic. No material or practical loss is renamed away to obtain a favorable comparison.

The nominal and compared histories are analytical descriptions of linked readout, memory and action relations; they do not presuppose an ontological subject/world split. The new work explains a supplied premise by following the same retention mechanism, credits conventional control theory and the previous empirical study, and preserves the exact scope of what remains supplied. It therefore advances the requested connection rather than replacing it with a disconnected controller exercise.

**Final local acceptance: no repairs required.** The wider three-part objective is not complete merely because this continuation passes. Remaining physical uncertainty/timing, policy-generation discrepancies and justified practical comparison should stay explicit in the governing completion audit. Prior review evidence and original sources remain untouched.


## Final current-account scope check

Read the canonical bilingual addition **From initial error to the whole feedback history** and the updated completion audit. Both correctly credit the derived recurrent-memory premise and its direct horizon composition, retain loose radii and the genuine boundary witness, distinguish 7,176 controller recomputations from physical trials, and preserve retrospective readout-domain and common-interval limits. They keep future readout warrant, physical response/timing, the tuning-model/objective contract and warranted practical comparison open. No required scope repair was found; local acceptance remains unchanged.

Current canonical SHA-256 at this check: `6ffcdd44631505aa5755ad7c0585aab7b7c304f9b74d13aa756cd13958bb476c`. Current completion-audit SHA-256: `2faef4586955e29bb6b1fb628dfdb1979c3648addf50cf62446953f3915c714b`. These are document bindings, not an additional scientific run. Formal and numerical source bindings remain those verified above.
