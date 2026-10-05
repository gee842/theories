# Independent review of the actual prediction protocol

6 October 2026. Independent collaborating-AI review of the concrete protocol bridge, its separately authored observation and failure companion, the dedicated checker, saved compiler output and current explanatory drafts. This is internal mathematical and implementation review, not external peer review or empirical validation.

**Verdict: accepted for the actual deterministic, payable-write trial subprocess.** The work establishes a concrete connection that the generic protocol theorem previously left as an obligation: directly specified macro guards, state changes and reported receipts agree with the original predictor's completed physical trials. It preserves the actual memory, material, source and intermediate costs. It does not prove a refinement of the full numerical model or create a new observation channel.

## Sources and scope inspected

I read the actual [PredictionAction.lean](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/formal/PredictionAction.lean) definitions of state, command, enabled events, physical updates, score bounds, cycle and energy account. I then read the complete [PredictionProtocolBridge.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/PredictionProtocolBridge.lean), [PredictionProtocolObservation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/PredictionProtocolObservation.lean), [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/check_prediction_protocol.py) and [saved audit](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/prediction-protocol-audit.txt). The [canonical account](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/PREDICTION-PROTOCOL.md) and [mathematical companion](PREDICTION-PROTOCOL-MATH.md) were checked against those sources. The earlier [protocol review](PROTOCOL-COMPOSITION-REVIEW.md) supplies the already accepted generic context.

The new macro process keeps the full physical boundary state, including the inherited score, last executed action, installed updater, resources and leases. It contracts event granularity; it is not a smaller-state quotient or proof of a minimal sufficient representation. Its command and update equations are embedded in the direct macro relation. It does not introduce a separate `Controller` instance and then invoke the generic closed-loop implementation theorem. Instead it instantiates the block and reported-realization interfaces on an already controlled physical law.

## The concrete correspondence

The boundary requires readiness and a score at most four. Retrofit starts with score two, and the parent's score-invariance theorem preserves that bound. The original event guards and phase transitions force a completed trial to have exactly the word `rent, work, write, finish`. The converse proof checks those same guards on the actual successive states. Ready-state updater formation and regime reversal remain outside this trial protocol.

The command constraint is correctly phased. At entry and work it equals the circuit's current command. After work it equals the executed action recorded in the selector. Writing can change the command for the next trial before finish, without changing which trial is being completed. The companion includes a concrete witness of this distinction.

The arithmetic `macroGuard` and `macroEnd` do not define themselves by existence of a block. The guard requires positive leases and source, enough initial fuel for rent and work, and enough actual post-work fuel for writing. The endpoint gives the original score update, fuel, source debit, executed selector, leases, cleared receipt and ready phase. Their equivalence to the original sequential guards and endpoint is proved before the exact completed-step and history results.

This is a real instance of the protocol interface rather than another uninstantiated generic theorem. The direct equations still describe a supplied recipe; their agreement is not independent empirical support for that recipe.

An important interpretation is that `macroGuard` describes **completion feasibility**. It depends on the realized post-work return and can therefore depend on a hidden regime. It is not a newly available runtime test telling the actor in advance which trial will complete. The actor can pay rent or execute work in a history where this completed-trial guard is false. The abort witnesses preserve precisely those cases.

## The consumed receipt is preserved semantically

Finish clears the physical receipt field. The companion does not mistake that final `false` value for the outcome. It first proves that, for either installed updater and each score at most four, the two target labels give different updated scores. It then recovers the actual target from the old and new scores and recovers the actual receipt from that target and the executed action.

The proof connects this reconstruction to the label consumed at the intermediate paid write and the receipt generated by actual work. The reporting function itself does not read the hidden regime; an explicit invariance theorem checks that fact. The hidden regime enters the parent plant's response, not the controller's command or a newly supplied teaching oracle.

The algebraic update identities alone do not assert that a trial was executable. The reported-step theorem uses them only after establishing a completed physical block. At the invalid score five, Slow maps both targets to four; the checked collision correctly limits this decoder to the invariant domain.

This report is a historical semantic annotation of the actual consumed observation. It is not an endpoint sensor, an extra stored copy of the old score, or evidence that another physical recipient can read the cleared receipt for free. Any runtime recipient needs its own retained record or delivery mechanism. Exact reconstruction of a receipt also differs from correctness of its interpretation: the inference from receipt to environmental target uses the parent's noiseless complementary response law and does not survive arbitrary source outages.

## Payments, source and failed prefixes

The completed-history theorem concatenates trials through the same full physical boundary states. Each trial contains four micro-events and consumes one source packet. The exact source theorem is `final packets + completed trials = initial packets`. This is a finite event/accounting result, not a timing or renewal guarantee.

Under the parent's `UpdaterFormation.Admissible` premise, the original exact energy ledger and unchanged material count hold for the flattened history. Every cut within a completed realization retains the actual intermediate state and both prefix/suffix accounts. The prefix theorem is conditional on a completed realization; it does not convert an aborted attempt into one.

The companion independently reads the unchanged parent law to establish meaningful edge cases:

- Three fuel units can pay rent but leave too little for work, even when the prospective route would capture support.
- Four fuel units can fund a wrong work attempt and its actual failure record while leaving no fuel for writing. The old score remains, and the declared subprocess has no next event.
- Four fuel units on a correct route can fund rent and work; the actual capture then funds the later write. Requiring all three bills upfront would incorrectly exclude this completion.
- A completed trial can leave an expired updater and prevent a further cycle despite retained score and remaining source.
- Writing can correct the future command while the old executed action remains the one legitimately finished.

These are counterchecks of the actual predictor, not a separate illustrative physical process. The first two unfinished paths are explicitly proved as micro-traces with disabled continuations. They remain outside completed macro histories and must retain their probability mass in any later stochastic refinement. No physical rescue impossibility is claimed beyond this declared event repertoire.

## Verification record

The saved dedicated audit reports a successful fresh build with Lean 4.29.1. It compiles all twelve captured project modules from their frozen source bytes in a temporary directory, checks the imported project-module set, rejects the specified proof holes and shortcuts, matches each new theorem to its requested axiom audit, and checks that source bytes remain unchanged during the build. I inspected the checker and recorded output; I did not rerun the build or numerical experiments.

The accepted record contains **38 new theorem audits: 15 bridge results and 23 observation/example results**. Nineteen have empty axiom-dependency lists. The remaining new declarations depend only on standard `propext` and `Quot.sound`. The broader compiled dependency record also contains `Classical.choice` in earlier updater/prediction declarations; it would be incorrect to describe the whole imported development as having only the first two dependencies. No custom axioms or proof holes are reported.

At this review all twelve source hashes, the checker hash, toolchain-file hash and compiler-binary hash matched the saved audit. The following digests identify the reviewed artifacts:

| Artifact | SHA-256 |
|---|---|
| `PredictionProtocolBridge.lean` | `4a96b3a8a6a37e592a28d18e9b7b2db805bd58d8070b076b843c33d1c89320e0` |
| `PredictionProtocolObservation.lean` | `34ef90783f4f82dba05f5ae04776da90d71e2e2591a87820aef705365ff22d89` |
| `check_prediction_protocol.py` | `36be649bb14f82c2e8d5e5ec1eb0039499fc43833a44d171bb7b3349f3896649` |
| `prediction-protocol-audit.txt` | `4ca25364c37d2ea8c80dc199c183ee10288229c51263daea0c47c8309a9fa18a` |

I re-read the finalized canonical and mathematical accounts after their verification sections were updated. They now report the audited counts and explicitly preserve the full-state event-granularity scope, the distinction between completion feasibility and a runtime pretrial test, and the limits of semantic receipt recovery. No blocking error remains in the reviewed proof, checker, finalized prose or stated correspondence.

## Remaining boundary of the result

The correspondence covers deterministic-capture trials whose write can be paid. It excludes the full numerical model's outages, skipped writes, circuit rebuilding, failed retention/rebuild branches, scheduling and probability law. It also does not compress the parent's complete formation, reversal and updater-replacement history into repeated trial steps. Those operations can remain real source-law events without already possessing this macro correspondence.

No chemical calibration, new learner, action-route origin or shared evaluation is established. The retrofit, sensor interpretation, update repertoire and normal prediction-to-action coupling remain supplied. The advance is a verified concrete connection between that existing mechanism and the protocol interface, preserving its actual causal input and material history. Further mechanisms must retain these conditions when extending it toward reliable evidence use, revised action coupling and concern for distinct centers.
