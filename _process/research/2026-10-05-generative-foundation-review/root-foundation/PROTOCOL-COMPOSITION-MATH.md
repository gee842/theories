# Paid implementation across event scales

6 October 2026. AI-authored companion under the [generative-grounding programme](../../../../theories/becoming/chapters/GENERATIVE-GROUNDING.md). The named connection is **several physical events → one implemented observation/update step → successive learned responses**. This develops the step-granularity obligation left open by [controlled refinement](CONTROLLED-REFINEMENT-MATH.md).

## 1. Why another interface is needed

The previous result uses the same action and event granularity in the concrete and abstract descriptions. An actual implementation may need to assemble, measure, write and return to a decision point before a single abstract update has happened. Those intermediate conditions can block completion or change the information delivered. Treating a whole protocol as one event therefore needs more than an endpoint label.

The earlier [finite instruction compiler](../../../../experiments/integrated-correction/general-framework/generative-basis/formal/FORMAL.md#5-an-explicit-generative-instruction-set) already declares macro boundaries and warns that intermediate writes and costs are not automatically invisible. The present construction retains actual micro-events and their accounts; it does not replace that finite probabilistic compiler or infer its stochastic guarantees.

## 2. Completed blocks and their actual states

Let \(P(s,e,t)\) be the micro-event law, \(B(s)\) identify a declared decision boundary, and \(a\) be the command committed at that boundary. A supplied protocol specifies which micro-edges are permitted while carrying out \(a\), and each permitted edge must be an actual \(P\)-edge.

A completed block for \(a\) is a **nonempty finite path** from a boundary state to its first subsequent boundary state, using only those permitted edges. Intermediate states are not boundaries. The committed command stays the same throughout that block. This contract does not make the underlying world deterministic or choose among its permitted internal alternatives.

Let \(S_B=\{s\mid B(s)\}\). The block process on \(S_B\) admits \(s\xrightarrow{a}t\) exactly when such a completed path exists. Its reported version additionally labels the edge with the observation delivered at the end. The report is a declared function of the concrete boundary states and command; if an intermediate distinction affects the report or later choice, it must be retained in the concrete state or represented by a richer interface.

These definitions describe completed executions. They do not remove the ambient micro-process, nor do they declare every interrupted prefix to be a completed abstract action. A required abort, interleaved external observation, change of command or intermediate memory use must be exposed through additional states, boundaries or labels before a stronger equivalence is claimed.

## 3. Composition and controlled history

**Flattening.** A finite history of completed blocks can be realized as one actual micro-history. For each macro edge, choose its witnessing micro-path. Consecutive blocks share the exact same boundary state, so their paths concatenate by the existing `trace_append_iff`. No resources or records are initialized at the join. The concatenated word contains at least one micro-event per block.

This is an existence result for a compatible realization of the declared block history. It does not claim that a particular scheduler will execute the witnesses, or that all micro-histories finish at such boundaries.

To connect to a learner, let \(L\) be the existing controlled process for a supplied world law, channel and deterministic controller. Let

\[
d:S_B\longrightarrow X\times M
\]

decode the abstract world condition and the controller's memory **from actual boundary states**. This avoids adding an unaccounted memory register at every macro step. The implementation still has to justify that decoding, including any physical cost or limitation of the records it reads.

The local implementation obligation is

\[
L(d(s),(a,o),r)\ \Longleftrightarrow\
\exists t\;[\operatorname{ReportedBlock}(s,(a,o),t)\land d(t)=r]. \tag{1}
\]

The obligation holds from each actual concrete boundary state. Since \(L\) is a controlled process, it includes the equation selecting the command from inherited memory, the delivered observation and the update equation for final memory. An exact resource projection alone cannot establish (1).

**Controlled implementation theorem.** Under (1), every finite abstract controlled history from \(d(s)\) has a corresponding history of concrete completed blocks from \(s\), with the same action/observation word and final decoded world/memory. Conversely, each such concrete block history projects to that abstract history. Flattening its witnesses produces one actual micro-history joining its actual initial and final states.

**Proof.** Apply the causal core's `local_exact_iff_trace_exact` to the reported-block process and \(L\), using \(d\) and (1). This proves exact finite macro histories. Apply block flattening to the concrete history. Endpoint equality retains exactly the final decoded memory, and induction carries the actual intermediate boundary state into the next lift. ∎

The theorem is conditional on an established protocol implementation relation. It does not construct that relation for the concurrent selector, updater or predictor modules. A weaker one-way simulation can be useful when full exactness fails, but its scope must be stated separately.

## 4. Costs belong to micro-events and their prefixes

Suppose each actual micro-edge satisfies the previously defined account law

\[
b(t)+D(s,e,t)\le b(s)+C(s,e,t).
\]

Every flattened trace has a `SupportTrace` using the same intermediate states. Its terminal reserve plus total expenditure is bounded by its initial reserve plus credits actually delivered along that trace. The same necessary inequality holds for each actual prefix. Credits after a prefix do not appear in that prefix's account.

This account law alone is **not a prepayment condition**: credit and expenditure on the same declared edge may balance. A claim that an operation must pay before receiving its own return requires an appropriate guard, separate payment and receipt events, or the further condition \(D(s,e,t)\le b(s)\). Neither aggregate balance nor a favorable net return supplies that guard.

The concrete example separates payment and receipt. A ready state must already have one usable fuel unit to pay and enter the busy state. A later receipt transfers one unit from a finite source and returns to a boundary. A completed block restores usable fuel while consuming one source unit. Starting with zero usable fuel satisfies the numerical net-cycle balance but cannot begin the payment event. Two completed blocks use two actual source units; the second cannot reuse the first unit.

## 5. Completion requires a separate argument

An implementation can permit both a finite route to the next boundary and an internal execution that remains busy forever. Adding such a permitted stall need not change the relation of **completed** blocks at all. It changes the set of possible executions and can defeat a guarantee that an issued command finishes.

The counterexample must place the stall inside the permitted protocol for the same committed command. A spare ambient-world action excluded by the protocol would not refute termination of that protocol. A loop permitted only by one arbitrary scheduler likewise does not establish its probability under a different specified scheduler.

A natural-number rank strictly decreasing on every permitted internal step rules out an infinite sequence of those steps and bounds their number. It does not establish that the next step is enabled: an unfinished state can be deadlocked. Eventual completion needs additional progress assumptions appropriate to the actual process. A time or probability guarantee needs its own timing or transition law.

The no-stall example also admits a concrete incomplete prefix: one initial usable fuel unit and zero source permit payment into a busy state, after which no micro-event is enabled. Its spending remains in the micro-history. The theorem about prefixes of completed realizations cannot turn this aborted execution into a completed one; the original micro-event law and support account still describe it directly. Any later probability model must retain its mass rather than normalize only over successful returns to a boundary.

## 6. Integration scope

The contribution connects finite controlled descriptions to completed, paid multi-event implementations. It preserves intermediate states, inherited material stocks and physically decoded memory while exposing the difference between availability of a completion and assured execution.

The protocol repertoire, boundaries, report channel, controller equations and mapping remain local inputs to establish for each concrete mechanism. The general interface does not derive their formation. It supplies the next prediction-to-action construction with explicit obligations: identify the physical record at boundaries, preserve all relevant intermediate effects, pay along actual prefixes, and state which claim is made about interrupted execution. Shared evaluation and concern remain further derivations.

## 7. Formal correspondence and verification

The [formal module](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/ProtocolComposition.lean) uses `BlockPath` for nonempty first-return paths, `Realization` for consecutive physical blocks and `ReportedRealization` for the actual report at every intermediate boundary. `controller_trace_iff_implementation` proves the controlled-history equivalence under its full local implementation contract. `realization_support_bound` and `realization_prefix_support` reuse the existing micro-event account. `block_length_bound` bounds completed blocks; `internal_trace_rank_bound` and `no_infinite_internal_execution` separately address arbitrary internal paths and an infinite internal execution under strict descent.

The [example module](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/ProtocolExamples.lean) proves the exact completed-step condition: usable fuel is positive, one source unit is consumed, and usable fuel is restored. The condition is unchanged by permitting the busy-state self-loop. `completed_histories_agree` lifts that equality to all finite completed histories; `infinite_committed_busy_run` and `busy_run_never_returns` exhibit the infinite execution under the same committed protocol. The upfront-payment and deadlock witnesses retain their actual intermediate stocks.

The [fresh-build record](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/protocol-composition-audit.txt) passes 39 new audits, split into 17 general and 22 example theorems. Seventeen have empty axiom dependencies; the remaining dependencies are confined to the standard `propext` and/or `Quot.sound`. The seven canonical source modules, checker and compiler are hashed separately. The [independent review](PROTOCOL-COMPOSITION-REVIEW.md) examines meaning and compatibility as well as artifact provenance. No empirical validation, probability law or automatic discovery of the protocol is inferred from these checks.
