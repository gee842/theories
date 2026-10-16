# Independent review of issued-protocol completion

6 October 2026. AI-authored internal collaborating-agent review. **Status: accepted at the conditional mathematical and implementation-interface scope below.** This is not external peer review. The reviewer owns this note and the accompanying [mathematical specification](PROTOCOL-COMPLETION-MATH.md), and did not write the new Lean implementation or its build checker. The [review receipt](PROTOCOL-COMPLETION-REVIEW.json) binds the inspected files separately from the formal producer's build receipt.

## What is being reviewed

The named obligation is whether an admitted issued physical operation must actually return, rather than merely agreeing with an abstract operation on histories that happen to complete. The fixed [foundation requirements](../../../../theories/becoming/history/GENERATIVE-GROUNDING.md#completion-of-the-unified-foundation) are unchanged. This round addresses the termination premise in a compatible implementation, not a new learning device, a full foundation proof or a replacement research goal.

The additive sources are [ProtocolCompletion.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/ProtocolCompletion.lean), [ProtocolCompletionExamples.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/ProtocolCompletionExamples.lean) and [PredictionProtocolCompletion.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/PredictionProtocolCompletion.lean), checked by [check_protocol_completion.py](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/check_protocol_completion.py). The existing [ProtocolComposition.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/ProtocolComposition.lean) and [ProtocolExamples.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/ProtocolExamples.lean) remain the declared semantics and countermodels.

The source-level novelty within this repository is real and narrow. The previous `block_length_bound` assumes a completed block. Its rank argument excludes an infinite internal run but allows finite deadlock. Its controlled-history equivalence quantifies over completed blocks. The new contract supplies the missing enabled-next-event obligation, including entry, and preserves it along every internal branch. Established total-correctness reasoning is being connected to this particular interface; no mathematical priority is claimed.

## Semantic findings

The current `CompletionContract` states all three intended obligations: an actual committed next event for each `Live` state, preservation of `Live` on every nonboundary successor, and strict natural-rank descent on each such successor. `Live` is a supplied admissible domain. Its name is not evidence of life, successful effect or value.

The declarations separately establish the following facts:

- every internal prefix retains `Live` and satisfies the length-plus-rank bound;
- every unfinished finite prefix, including the empty issued prefix, has an actual extension;
- an unfinished deadlocked prefix and an infinite internal execution are impossible;
- a nonempty completing `BlockPath` exists, and every completed block from that domain obeys the same bound;
- reports, decoded controller memory and actual boundary states can continue through the existing local exactness interface;
- every coordinate of an independently supplied account law applies at a common actual micro-history cut, including cuts inside an operation.

`FiniteMaximalAttempt` explicitly distinguishes a first-return block from an unfinished internally deadlocked path. `finite_maximal_attempt_completes` excludes the second case and bounds the first. Combining it with the infinite-internal-run exclusion supplies the maximal-discrete-run conclusion. The file does not define a new physical scheduler or elapsed-time semantics. An arbitrary prefix that stops while an event remains enabled is not a deadlocked maximal attempt. The existence declaration is essential: it avoids accepting a universal statement merely because no maximal attempts were constructed.

The examples reuse the old event laws. Positive fuel and source under the nonstalling protocol supply a two-event return. Zero fuel violates entry enabledness; source exhaustion after payment violates internal enabledness; the admitted busy self-loop defeats strict descent. A completed operation can exhaust its last source and leave an actual boundary outside the next operation's `Live` domain. These examples do not erase the old failed branches or silently restore resources.

## Composition and outcome qualifications

`issued_reference_completion` proves existence of an actual returned boundary and an abstract closed-loop step using the supplied `LocalExact` relation. The underlying contract still has to represent the intended observations and all relevant returned outcomes faithfully. Neither the rank nor completion creates a calibrated sensor, an implemented failed-return branch or a moral interpretation.

`reported_history_continues` starts its next operation at the actual endpoint of an existing history. It requires `Live` there for the next controller command. Iterating it gives finite continuation when those further premises are proved; it does not prove that the premises perpetually regenerate themselves. The account theorem retains physical payment histories instead of replacing them by the rank.

A refused entry is not a zero-event completion. A paid deadlock does not become a usable failure report because an analyst names it one. If an abort or failed-return path is desired, the actual protocol must implement it. A physically returned failure may satisfy this completion contract without satisfying a task-success claim.

## Limits that must survive final integration

The contract is sufficient, not necessary, for every possible kind of termination. A protocol with a probability-zero infinite retry branch may terminate almost surely and still fail this all-admitted-branches condition. No probability, clock, scheduler fairness, source replenishment, biological viability, empirical universality or ethical warrant follows from the new theorem.

The [application audit](PROTOCOL-COMPLETION-APPLICATIONS.md) distinguishes the paid example and the four-phase predictor instantiation from the separate total callable boundary of the accepted stochastic exposure. The new predictor source defines `phaseGuard` by remaining actual event guards and command/selector retention, rather than by asserting that a completed block already exists. Its entry condition is equivalent to the old `macroGuard`; that guard depends mathematically on the actual plant response and is not an installed online oracle. The trial commitment excludes reversal and reformation. `maximal_admitted_trial_exact` supplies the actual four-event word and endpoint; the sufficient current-fuel guard covers a mismatch as well as capture. A returned `workedUnpaid` stochastic exposure is not a completed old write trial. The evaluator's wider permission-setting repertoire can stutter, so blanket all-event termination is not inherited by calling an accepted selected trace a pipeline.

`admitted_finite_continuations` additionally gives an actual reported history of any requested finite length under explicit boundary-domain admission and closure under every actual completed block. It joins the physical words and retains the same abstract closed-loop trace. This is a conditional closure theorem; it does not derive those strong premises from one successful operation. With positive per-operation demand from a finite closed account, arbitrarily many completions are already excluded by the existing prefix account theorem, so that process cannot satisfy the nonempty boundary-closure premise. Repackaging the account consequence as a new recurrence theorem would add no new result.

An operational admission guarantee under partial information requires `Live` for every actual state compatible with the actor's available information. The sharp predictor `macroGuard` is a property of the actual state and its ensuing response. Postselecting hidden states in which writing is affordable does not produce an executable issuance rule. This is the existing information-adequacy obligation applied to admission, not a new finish line. A conservative prepayment reserve may suffice without any future-outcome sensor.

## Verification and final judgment

The [combined build receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/protocol-completion-audit.json), SHA-256 `826ac31c89cb9e8d676fa16b0888868cdae0b91a31b67448c29f0cb76838749b`, records a fresh pinned Lean 4.29.1 build of 15 modules. All 34 new theorem audits and 244 inherited audit declarations pass; eight new declarations have no axiom dependencies. The permitted standard dependencies are `propext`, `Quot.sound` and `Classical.choice`. General completion existence and its relevant corollaries disclose classical choice. No custom axiom, admitted proof or unchecked native decision is present.

The reviewer independently matched all 15 source hashes, the build checker, toolchain and compiler binary to the receipt, read the new declarations and checker, and checked the saved compiler audit names against requested theorem audits. The checker compiles frozen copies in a fresh temporary directory and confirms source identity across the run. Earlier failed and intermediate build attempts remain explicitly preserved as development provenance, not extra confirmations. No second Lean build or unrelated scientific rerun was performed for this review.

The [canonical account](../../../../theories/becoming/history/PROTOCOL-COMPLETION.md) and [integration](PROTOCOL-COMPLETION-INTEGRATION.md) preserve the fixed completion conditions, disclose supplied laws and admission meanings, and leave the active successor/correction and justified-application obligations separate. Acceptance closes the specified bounded operation-completion interface, including the existing predictor instance. It does not complete the unified foundation or certify arbitrary physical protocols, Python callers, physical timing, empirical universality or ethical grounds.
