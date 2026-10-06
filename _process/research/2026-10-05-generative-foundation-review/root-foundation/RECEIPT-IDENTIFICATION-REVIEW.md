# Receipt identification and revision: independent review

6 October 2026. AI-authored internal review of **actual action/receipt → justified inference → retained correction under outages and changed conditions**.

**Verdict: accepted at the stated scope; no material blocker found.** The new results characterize what the existing receipt relation identifies and connect that characterization to the unchanged paid predictor. They do not install a replacement decoder, derive the physical relation, assume a universally stable regime, guarantee continuing work, or complete the no-assumptions foundation.

## Review independence

This reviewer independently inspected [ReceiptIdentification](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/ReceiptIdentification.lean), [GenerativeReceiptModel](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeReceiptModel.lean), the final Lean checker, and the evidence script/report. The reviewer authored `ReceiptRevisionBoundary`, so this note does not claim independent review of that source.

A separate internal reviewer explicitly confirmed source-level review of all 15 final [ReceiptRevisionBoundary](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/ReceiptRevisionBoundary.lean) theorems, including the phase-exhaustion lemma and the final three dynamic-pooling results. That review found no material issue, preserved the unfunded-deadlock boundary, and confirmed that opposite successes conflict with a fixed-regime interpretation rather than with the actual changing history. It also reviewed both final public wrapper theorems. That cross-review involved no duplicate compilation or source edits.

## Identification and its exact scope

The new module uses the existing Boolean relation `receiptOf action regime available`. `Compatible` asks whether an availability value could produce the observed action/receipt pair. This is a candidate test, not a new transition law or an assertion about the actual availability process.

- A successful receipt fixes the regime at that observation to the executed action. A failed receipt permits both regimes when availability is unconstrained and unobserved.
- The old complete decoder is correct exactly when availability is true or the action differs from the regime. Its error case is a matching action during an outage. The available-work decoder follows as a specialization of that proved characterization.
- A finite record is compatible with a single fixed regime precisely when all successful actions match it. All-failure records leave both candidates, while opposed successful actions leave no fixed-regime candidate. The theorem tests stationarity; it does not assert that the world is stationary or that inconsistent fixed pooling makes either recorded success false.
- The mathematical partial decoder answers exactly the singleton-candidate observations. Its maximality and pointwise uniqueness apply to certainty-level answers from these specified inputs, sound over every compatible availability value. They do not establish optimal learning, usefulness, posterior accuracy, or maximal inference after adding other observations and assumptions.

The all-failure result is finite and relative to this observation relation. Allowing adaptive choices based on earlier receipts does not itself eliminate the all-outage ambiguity. Additional known policy constraints, informative sensors, availability restrictions or a probability model would require their own analysis. The final comments correctly say that failures eliminate no candidate under this relation, rather than claiming they contain no statistical information.

`SoundDecoder`, `Identifies` and `StableCompatible` introduce tested mathematical properties. No theorem silently asserts that every actual decoder is sound, that the actual dynamics satisfy the fixed-regime predicate, or that the partial decoder has been implemented inside the learner. Existing physical recipes, event semantics and the interpretation of the receipt remain supplied.

## Concrete integration and timing

The public `partial_answer_matches_actual_receipt` theorem correctly instantiates compatibility with the actual availability value from the given response relation. Its conclusion concerns the regime in that receipt, not an unspecified later state.

The public `actual_next_step_uses_fresh_receipt` theorem uses two actual native steps. The first reaches the observed phase. The existing phase guards force any enabled next event to be a write, after which the available work/write law derives the score update and preserves the event-time regime. This discharges the next-event-kind condition within that law. It does not assert that a next step exists, that writing is affordable, or that an external scheduler will execute it.

The boundary module and its separate cross-review preserve three further distinctions:

1. The deterministic `PredictionAction` work law fixes availability to true and requires a packet. Its formal work steps are not the separately executable stochastic outage branches.
2. Finish clears the transient receipt. Later references to an earlier success are historical proof references, not evidence of an additional native stored transcript. Reversal can preserve the acquired score and command while changing the current target.
3. Fresh target identification need not immediately change a Slow controller's command. The actual continuation writes a changed score but initially retains the stale action; the later existing corrective continuation succeeds. Two opposed successes in that one legal changing history refute fixed pooling, without refuting either observation.

These are actual state/edge connections with inherited resources, not a newly defined favorable process or a supplied correct teaching label. They still rely on the existing sensing, update and command laws. No selfhood, phenomenal identification or ethical standing follows.

## Evidence and probabilistic interpretation

The [evidence report](RECEIPT-IDENTIFICATION-EVIDENCE.md), [script](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/check_receipt_identification.py) and [result artifact](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/receipt-identification-results.json) agree on their scope and counts. Source review found the following material safeguards intact:

- The eight truth-table assignments are logical cases, not equally likely observations. The 87,381 finite channel records and 128 depth-three feedback policies are analysis objects, not claims that the finite paid learner can execute every record.
- Replay of 6,640 saved tape records checks their complete stored successors, increments and statuses against the unchanged micro-interpreter. Only 3,744 records contain an actual trial; non-trials are excluded rather than treated as failed observations.
- The 2,452 ambiguous paid writes include 1,180 writes using a label wrong about the actual event-time regime. Those counts are saved call/tape coverage, with duplicates induced by unused tape bits and no entrance-mass weighting. The report does not turn them into frequencies, independent observations or a new expected process result.
- The old whole-history expected decoder-error metric is separately attributed to the preserved old result. Replaying the old interpreter and classifying saved histories is not a new independent validation of the physical plant or a new Lean/Python refinement theorem.
- The exact posterior `1/65537` after eight failed fixed-action trials explicitly assumes a stable regime, a fair prior, funded trials and independent availability with known probability `3/4`. It demonstrates statistical information without logical candidate elimination. Those conditions are neither hidden in the Lean result nor installed as new physical laws.
- Partial inference was not connected to an updater or evaluated as a controller. Abstaining avoids unsupported categorical answers at this contract, but can delay learning or action. No policy superiority follows.

The evidence report's first-cycle staleness example and the formal module's later sixth-success example are separate reached instances of the same existing reversal law; they need not be identical histories to support their stated boundary. Neither gives the controller access to the analyst's reversal knowledge or retrospectively identified regime.

## Final verification and preservation

The [dedicated Lean checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/check_receipt_lean.py) freezes sources, builds them from fresh temporary imports under pinned Lean 4.29.1, and requires complete audit coverage and the named substantive interfaces. Its public entry-point imports are checked explicitly. The baseline manifest is pinned by its literal hash. Duplicate inherited modules from the two predecessor suites must agree in source path and audit entries.

Crucially, the checker requires each inherited module's entire ordered audit output to equal its archived predecessor output. Every new module must report empty dependencies. It neither transfers historical dependencies to new declaration names nor widens the original root allowance.

The [final receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/receipt-identification-verification.json), recorded at **05:56:19 UTC**, passes **24 modules and 349 audits**, comprising 21 unchanged inherited modules and **32 new empty-dependency results**: 15 identification theorems, 15 boundary theorems and two public wrappers. These counts are for this round and include the inherited overlap only once.

Independent read-only reconciliation confirmed the receipt's current source, checker, log and toolchain hashes; all **51 archived baseline files**; exact audit-map agreement for all 21 inherited modules; empty dependencies for every added declaration; and all **22 evidence-input hashes**. The count identities in the evidence artifact also match its report. No Lean suite or broad scientific experiment was rerun by this independent review.

The next unresolved mechanism obligation is how the learner obtains, pays for and uses justified availability evidence or change detection, and how the relevant sensing, decoding and action rules form or are revised. The current results identify when a receipt supports a target and when that support expires; they do not supply that further machinery or eliminate the inherited foundational premises.
