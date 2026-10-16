# Review of derived inquiry certificates and reached continuations

6 October 2026. **Accepted at the stated scope.** The new construction calculates actual finite policies and continuation trees with native execution and answer certificates, removes unnecessarily global agreement preservation from composition, and derives the formerly separate nonemptiness requirement where sound non-abort execution already entails it. It preserves genuine refusals and the supplied representation's explanatory limits. No semantic or verification blocker was found.

This reviewer authored `ReachedInquiryComposition.lean`; that module is therefore not presented as independently reviewed by its own author. A separate agent independently checked its exact composition characterization, non-abort equivalence and original-target witness, and the coordinating agent reviewed its integration. This reviewer independently inspected the other three new proof modules, the coordinating agent's checker and explanatory account, and the final recorded build. The synthesis author also independently reviewed the concrete packet fixture. No duplicate full build or scientific producer was run for this review.

## What is established

[DerivedInquiryCertificates.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/DerivedInquiryCertificates.lean) makes a substantive change to the application interface. Its `WitnessResult.found` carries an actual `Policy` or `LeafContinuations` value together with the relevant proof. A caller supplies executable transition, condition, observation and question data, plus the finite carriers and bound. A successful soundness or identification certificate is not an input to `inquirySearch` or `composedSearch`. Thus this is certificate construction rather than a renaming of the former success premises.

The bounded search handles all policy constructors. A nonempty homogeneous possibility set can respond immediately. Otherwise it tests every available action, quantifies over every current possible state and every native successor, and recursively assembles every observation branch. A failure proof rejects all first-action alternatives within the declared depth. Nondeterministic transitions remain inside these universal checks; an available favorable endpoint cannot conceal another admitted endpoint that violates the condition or defeats the continuation.

The internal search returns `abort` for an empty branch because that branch is unreachable. The public initial search instead rejects an empty starting possibility set. `soundDecision` checks the prescribed prefix recursively, including the distinction between empty `abort` branches and live responding or inquiring branches. These cases are not treated as vacuous successful inquiry.

`continuationSearch` transports each prefix possibility set through the existing native `After`, and computes its suffix at the resulting leaf. `composedSearch` checks initial nonemptiness and prefix soundness before assembling suffixes. Its negative result means that no certificate exists for **that prescribed prefix with the specified bound at each suffix leaf**. It may reflect an empty initial set, an invalid prescribed prefix or failed bounded suffixes. It does not reject every alternative prefix, rule out repairing an invalid prefix syntactically, or prove unbounded nonattainability.

[ReachedInquiryComposition.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/ReachedInquiryComposition.lean) characterizes final identification exactly at reached leaves, assuming an executable prefix. It does not require the prefix already to answer the final question or require preservation by every process event. Its finite witness distinguishes an admitted observation event from an excluded alteration event. The latter defeats the old global property, while a separate theorem proves that every admitted actual trace retains the same original readout. This does not silently substitute a question about a changed target. The necessary final distinction and execution conditions remain; the finite synthesizer calculates them rather than receiving them as assumptions.

The sound-non-abort equivalence removes a duplicate nonemptiness input in applicable constructions. It does not establish that every process or belief is inhabited: sound `abort` is permitted only for empty beliefs, and a requested actual start must still be represented.

## Concrete law and correspondence

[OnePacketAdmissibility.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/OnePacketAdmissibility.lean) uses the existing packet coordinate as a nontrivial operational access condition. It proves probe admissibility equivalent to avoiding exhausted denial; either positive or negative test answers are admitted. The native process still contains depleted-probe denial transitions, which accepted policies under this stronger condition cannot use. This is not a derivation of ethical harmlessness or a change to the native transition law.

The exact attainable family remains `f B = f C ∨ f A = f C`, including its original all-finite-policy exclusions. The positive witnesses derive initial nonemptiness and availability. Forgetting the stronger condition transports a purported counterexample to the already refuted permissive case. No unavailable joint answer is manufactured by changing the law.

[OnePacketInquirySynthesis.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/OnePacketInquirySynthesis.lean) represents all six states and all five actions with proved inverse encodings. Its transition table is computed from the unchanged `advance`, and proved to match the native step relation. Its observations use native `sense`, its access condition matches `packetSafe`, and its questions read retained initial targets.

The concrete A?/B? witnesses are tied to actual search results: `search_selects_probe` proves equality of the returned `policyOption` and the exhibited finite policy; `policyOption_certified` extracts that result's certificate. The same decoded policy then receives a native identification proof. The argument uses pointwise branch correspondence, not an unrelated separately selected native witness or an unaudited function-extensionality step. It certifies these selected decoded policies; it is not a full refinement proof of the original costed Python apparatus.

Closed kernel reductions include empty-start refusal, immediate constant answers, the two separately attainable questions, blocked and joint refusals, exhausted-state outcomes and three actual-prefix continuation outcomes. Computed negative horizons remain bounded. The additional `exhausted_native_iff` independently proves the exact constant-question criterion for arbitrary finite policies, so no depth-two experiment is extrapolated into an unbounded theorem.

## Verification and preservation

The [fresh combined receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/derived-inquiry-runs/1791286286937536000/receipt.json) records **28 modules and 409 empty axiom-dependency audits** under pinned Lean 4.29.1. It preserves all 307 earlier audit entries and adds 102: 55 theorems, 42 definitions, four abbreviations and one inductive declaration. The new public entry contains imports only.

| New module | Audited declarations |
|---|---:|
| `ReachedInquiryComposition` | 24 |
| `DerivedInquiryCertificates` | 32 |
| `OnePacketAdmissibility` | 11 |
| `OnePacketInquirySynthesis` | 35 |

The reviewer reconciled 123 file-hash checks: the baseline receipt, all current and frozen module sources, compilation logs, checker/toolchain/compiler bindings, the evidence manifest and all 16 original current/frozen evidence files. The current convenience receipt exactly matches the frozen result. Every log's ordered audit outputs match its requests; every prior declaration retains its exact dependency map; every new audit is empty. All new named theorems, definitions, abbreviations and the `WitnessResult` inductive declaration are represented. Manual source inspection found no omitted explicit proof declaration, anonymous example, opaque/axiom declaration or metaprogram hiding a new proof. Automatically generated inductive machinery is not counted as additional handwritten declarations.

The reviewed [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_derived_inquiry.py) freezes inputs, rebuilds project imports in a fresh temporary directory, rejects errors and warnings, and checks sources again before accepting the result. It preserves the original source/evidence hashes and exact inherited audits. It does not rerun the apparatus producer or replace earlier receipts.

Receipt SHA256: `01fad790e1436e72ab967cf8163240452b360ea2ed8972000ce1caedf93b51ee`.

Checker SHA256: `b5d8af0216d38efc540411615c43c18050fadaf80e59aadc5b080baa7a5057f1`.

## Remaining explanatory scope

The [integration account](DERIVED-INQUIRY-PREMISES.md) correctly distinguishes derived proof obligations from supplied model data. The algorithm accepts arbitrary finite executable relations; that generality does not derive which relations describe a real process, why its represented inquiry matters, or how a planner, sensor or retained answer forms and operates within that process. The finite native correspondence does not supply the original apparatus's funding, memory or physical scheduling, nor whole-process ethical warrant.

These are relations still to connect within the generative account, not a demonstration that law, inquiry and value must be ontologically external to it. The result advances the actual-conditions-to-inquiry interface while preserving the stronger no-assumptions objective and existing formation, revision and stopping results. It does not announce completion of the universal foundation.
