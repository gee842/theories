# 一体之仁的共同形成接口：逐发生的后果、取得与回应

6 October 2026. AI-authored formal/mechanism contribution following the [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md). This is **a new representational adequacy interface applied to an existing causal formation history**. It does not install a new benevolent controller, establish felt experience, or finish the ethical identification of 一体之仁.

The connection addressed is **actual consequences → acquired and revisable influence → response → changed consequences and further response possibilities**, with every stage retaining its actual conditions. The concrete mechanism already exists in PairedPlasticity. The new work makes its successive joint changes explicit and gives an exact composition and abstraction test. This distinction matters: an additional notation for coupling is not itself a derivation of coupling.

## 1. Why an occurrence interface is useful

The [existing generative core](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean) already requires actual intermediate states in `Trace`. The previous [outcome interface](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/OutcomeContinuation.lean) explicitly retains selected endpoint outcomes; the [nondual core extension](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/NondualCore.lean) permits derived descriptions of a history and compares selected start/end readings. None of those statements denied intermediate activity.

For the present question, the selected descriptions must also distinguish **what happened along the way**. A later restoration can make the final quantity equal its initial quantity. A record can be cleared or unavailable while the condition it would describe persists. Two histories can have the same selected current records and resource totals but different formed links and different responses. A representation that leaves these relations implicit can invite incorrect interpretation even when the underlying `Trace` is adequate.

The new [CoupledOccurrence.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/CoupledOccurrence.lean) therefore describes each occurrence with a joint report derived from its actual before-state, event and after-state. It is not three independently evolving processes subsequently joined by an evaluator. It also does not require all reported dimensions to change simultaneously.

## 2. Exact generic statement

Let \(P\) be the existing transition relation on states \(S\), with events \(E\). Choose a declared description

\[
j:S\times E\times S\longrightarrow J.
\]

The described relation has the **same states** and labels \((e,z)\):

\[
P_j(s,(e,z),t)\iff P(s,e,t)\land z=j(s,e,t).
\]

`J` is an arbitrary report type. For example, it can contain several before/after readings of one occurrence. There is no primitive Actor, Patient, Subject or ethical predicate in this module. The choice of readout is an explicit representational input; its construction does not make it an internal sensor or acquired understanding.

The principal results are:

- **Exact description/forgetting:** `described_trace_exact` says an ordinary actual trace exists precisely when a described trace with the same start, event word and endpoint exists. `describe_actual_trace` constructs the description from one trace; `erase_described_trace` forgets it. A nondeterministic event word can have several different described executions; the theorem does not collapse them into a unique history.
- **Actual continuation:** `described_append_actual_iff` factors a described history at one full, shared intermediate state. Matching only one current reported quantity is insufficient. This reuses the core's established `trace_append_iff` at the richer event interface rather than claiming a new composition law for reality.
- **Joint before coarse:** `map_described_trace` extracts a coarser view from one jointly witnessed history. It does not reconstruct a joint execution from independently possible marginal descriptions.
- **Earlier occurrence remains in the history:** `actual_continuation_retains_occurrence` retains an earlier described occurrence when an actual suffix is joined. This is retention in the mathematical audit description, not proof that a physical system remembers everything.
- **Deterministic replay:** `replay_append` splits a computable description at the state actually reached by replay. Replay alone grants no event admissibility; the concrete adapter must discharge the existing guards.

These are finite, existential trace claims, not probabilities, control guarantees, or infinite persistence. A description can also omit important aspects of an occurrence; exact decoration relative to that description is not an assertion of complete observation.

## 3. The existing mechanism supplying the real coupling

[CoupledConcernHistory.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/CoupledConcernHistory.lean) imports the unchanged [PlasticityWitness](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/revision/evaluation/plasticity/formal/PlasticityWitness.lean) and [PairedPlasticity](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/revision/evaluation/plasticity/formal/PairedPlasticity.lean).

Its joint `Snapshot` reads recipient quantity, available fuel, native record `n`, formed links, both latches, their validity phase, factual command, response port and remaining packets. `occurrence` gives the before/after pair. These fields are analyst descriptions of existing runtime coordinates. The record `n`, links and latches themselves are already actual internal state in the old mechanism; the new `Snapshot` is not.

The old step equations establish the dependence:

1. An actual recipient contribution reduces its local quantity by two; a return, if it occurs, restores two. The selected local coordinate is real within this model, but **quantity reduction is not identified with suffering or adverse experience**.
2. The actual return enters a latch. A faithful read transforms it into the corresponding acquired loss distinction. A missing read enters `.missing`; it supplies no acquired negative finding.
3. The acquired recipient-loss bit enables binding or replacement. The actual own-loss bit sets the learned sign; binding/replacement alters physical link occupancy, fuel and the valid continuation phase. This own-loss dependence is precisely a substantive limitation of the installed local evaluator, not a detail erased by the common history.
4. Native writing updates \(n'=\lfloor n/2\rfloor+4\,\mathbf1_{\text{own loss}}\), advances the encounter count and clears the temporary latches. It does not restore recipient quantity.
5. At assessment, the installed rule reads \(10n(\ell_0+\ell_1)>64\). The result changes the response port and hence which response events are enabled. Factual command, acquired evaluative influence, consent/scope, material feasibility and remaining opportunities remain differentiated conditions.
6. Actual service changes the same recipient coordinate and consumes the available response packet. The end is consequently a new situation, not a reset instance of the original response opportunity.

The links, threshold, channels, target calibration, lossmeter and permitted event repertoire remain supplied in this local explanation. They are not therefore outside generative reality. Their formation and justification beyond this model remain research questions. The generic occurrence interface neither inserts these dependencies nor explains their origin.

## 4. One actual formation and response, without reset

`actual_formation_then_response` now describes the old actual histories and joins them at `trained .active`:

| Actual boundary | Recipient quantity | Native record | Formed links | Relevant continuation |
|---|---:|---:|---|---|
| `entry .active` | 40 | 0 | none, none | existing acquisition events admissible |
| `trained .active` | 36 | 4 | positive, positive | close, read, assess, then actual service |
| `final` | 46 | 4 | retained | packet exhausted; a new attempt is disabled |

The prefix is `aligned`; the suffix is `responseWord = [close, read, assess] ++ actionWord`. `runnable_occurrences` uses every original guard to construct the described trace. `occurrences_join_at_actual_state` proves that the whole description is the prefix description followed by the suffix description beginning from the exact reached state. No final quantity, original stock, fresh packet or unused actuator is reintroduced at the boundary.

This is the previous formation/use result made occurrence-explicit. It is not a new service behavior. The earlier [nondual tree mechanism note](NONDUAL-TREE-MECHANISM.md) similarly reconstructs the acquired perspective mechanism's record/action/support dependence; neither branch becomes one physically concatenated history merely because both instantiate the same generic interface.

`consequence_and_acquisition_are_distinct_dependent_changes` checks an earlier segment of this very formation. A recipient contribution takes the quantity from 40 to 38 while leaving `n` and the first link unchanged. Later, the actual acquired recipient-loss bit is true and valid; binding changes the first link from none to positive while the recipient quantity stays 38. Thus shared unfolding retains distinct changes and their order. Joint description does not assert that an alteration in understanding always changes the affected condition, nor that such an alteration could never genuinely change experience in a model that realizes it.

## 5. Continued feedback changes response possibilities

`actual_feedback_changes_response_constraints` describes both previously established six-pair feedback histories. The actual active and frozen variants reach equal native record, recipient quantity, fuel and factual command. Their acquired first links differ. The active variant permits abstention and forbids an attempt; the frozen variant permits an attempt and forbids abstention.

The difference is a changed acquired influence, not an invented flag added by this work. In the existing active history, the fifth encountered pair supplies no own loss with recipient loss, so replacement changes the first sign to negative. The sixth pair preserves the compared totals while the native record reaches five. The frozen variant retains the positive sign. This is an existing mechanism showing that acquired distinctions can change actual response constraints even when the compared factual command remains the same.

These histories **branch before the original service**. They are not a continuation from recipient quantity 46 after that service. The [practical-boundary integration](PRACTICAL-BOUNDARY-INTEGRATION.md) preserves this genealogy and explains why the change does not settle warranted revision: the active mechanism withdraws influence according to its own-loss rule while recipient consequences persist. Actual mutability is not yet justified restraint, relief or concern.

The old `no_recipient_actor_source_credit` result also preserves the local separation between recipient returns and the responding organization's fuel. The original successful response changes recipient quantity without being paid back through that channel. This is relevant operational noninstrumentality within the declared causal routes; it neither proves a comprehensive absence of every possible later advantage nor supplies ethical justification.

## 6. Two actual tests against erasure by report

### Restoration does not erase an earlier occurrence

Take the actual existing `pair false false`, here named `returnedWord`. The recipient contribution briefly takes its quantity from 40 to 38; the actual return restores it to 40. At the end, the selected tuple

\[
(\text{recipient quantity}, n,\ell_0,\ell_1,\text{factual command})
\]

is identical to the tuple at the original entry. The empty history has that same tuple. Only the returned pair contains an actual recipient-decrease occurrence.

`actual_return_does_not_erase_intermediate_decrease` proves the lawful described trace, selected endpoint equality and different historical readings. `no_endpoint_summary_decoder_of_actual_decrease` then proves that no function of **that selected summary** recovers whether a recipient decrease occurred on all actual histories. The proof uses the real empty and returned-pair histories; it does not toggle an arbitrary ethical predicate.

The complete endpoint states are different: count and resources, among other fields, were deliberately omitted by this summary. This is therefore a precise failure of that abstraction, not a claim that no larger endpoint description can ever retain history. Nor does it infer that the intermediate decrease was painful, impermissible or uncompensated. If those matters are the target, they need further independently assessed descriptions and mechanisms.

The concurrent [pretraining-evidence result](PRETRAINING-EVIDENCE-INTEGRATION.md) already identifies a real structural history record: occupied sockets retain net depletion through its declared class of complete faithful prefixes, and retired material extends the account through the selected replacement. That result should not be erased or presented as still awaiting this occurrence interface. Its target is **net depletion at complete boundaries**. The present target is **whether any intermediate decrease occurred**, including an actually refunded contribution. In `returnedWord`, occupancy remains zero and net depletion is zero, exactly as that invariant requires; there was nonetheless a temporary decrease. Different historical questions require different preserved distinctions. This new proof neither refutes the net-depletion decoder nor claims to discover the first retained consequence record.

### Missing acquired evidence does not remove the condition

The existing `missingWord` incurs recipient loss but ends with a missing recipient read. `missing_readout_does_not_remove_consequence` proves an actual described trace ending at quantity 38 with recipient latch false and phase `.missing`; binding and native writing are blocked.

The phase is essential. The cleared latch does not assert known absence of recipient loss. The quantity has not been restored. This is a concrete distinction among a present consequence, an unavailable acquisition and a disabled response. It does not imply that every cognitive change is merely superficial reporting: here the actual event law says what changed, and in another realization interpretation may itself change the experience.

## 7. What this advances, and what remains

The new positive integration makes a common generative history answerable to **joint, successive, consequence-sensitive descriptions and actual continuation**. An ethical reading can now cite a faithful occurrence chain rather than only an endpoint gain or a current command. The old causal mechanism supplies the actual feedback; these concrete reports retain the selected distinctions and make their omission testable, while the shared-state trace rule prevents false recombination. This is a formal adequacy condition for an explanation of 一体之仁, not its sufficient ethical definition. Shared generic interfaces or public imports do not physically splice this history with the acquired perspective, applicability, or [participation/consequence realization](PARTICIPATION-CONSEQUENCE-INTEGRATION.md).

It does not establish these stronger claims:

- that the concrete recipient quantity realizes an experienced undergoing;
- that faithful prediction or revisable influence necessarily constitutes concern;
- that the installed own-loss-based revision ought to govern recipient response;
- that every derived perspective must include every affected continuity in its appropriate concern;
- that nonduality by itself chooses one response, erases permission or alternative courses, or proves an assumption-free foundation.

The concrete next mechanism remains the [practical-boundary problem](PRACTICAL-BOUNDARY-RECONSTRUCTION.md): actual acquired consequences must be able to change the continuation of the practice that produces them while retaining outstanding consequences, available alternatives and permission. Its ethical warrant must be assessed within that situation. Merely adding a benevolent response bit, relabeling the present evaluator, or declaring the analyst report internal would not discharge it.

## 8. Verification scope

The dedicated checker is [check_coformation.py](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/check_coformation.py). Its final [coformation-verification.json](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/coformation-verification.json) records a **passed fresh 28-module build**: the unchanged 26-module PlasticityWitness closure plus the two new modules. It binds source and compiler hashes, audits the declared proof dependencies and confirms that inputs and the old verification receipt remain unchanged. Its own receipt and logs are separate from every previous check.

The two new modules contain 18 audited theorems, including three small helpers for reusing the already proved deterministic histories. Five use no printed axioms, seven use `propext`, and six use `propext` and `Quot.sound`; the inherited closure also retains its existing `Classical.choice` dependencies. No custom axiom or new runtime law was added. The count describes the verification scope, not the degree of foundational or ethical completion.

The [first development timeout](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/coformation-checks/1791270016396226000/TIMEOUT.md) and the [subsequent failed compilation](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/coformation-checks/1791270570053836000/receipt.json) remain preserved. Reusing the existing actual-trace certificates removed the unnecessary full-history recomputation; syntax/type issues were repaired before the successful fresh build. No failure was relabeled a passing result, and no favorable dynamics were added to obtain the proof.

Standard Lean proof dependencies, local transition laws and representational choices are different kinds of premise. An empty printed axiom list would not show that the description, mechanism or ethical interpretation was assumption-free.
