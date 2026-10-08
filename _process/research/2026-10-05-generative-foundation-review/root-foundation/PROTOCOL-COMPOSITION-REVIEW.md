# Independent review of paid protocol composition

6 October 2026. Independent collaborating-AI review of the protocol proof, separately authored examples, dedicated checker and saved verification record. This review is internal mathematical and implementation scrutiny, not external peer review or empirical validation.

**Verdict: accepted at its stated conditional scope.** Nonempty completed protocols can realize finite controlled histories across different event granularities, while retaining their actual intermediate states, delivered observations, inherited physical memory and declared resource accounts. A supplied exact local implementation contract is required. The result does not establish that every issued command completes, or that the repository's different concrete learning mechanisms already satisfy that contract.

## Inspected definitions and proof obligations

I read the complete [ProtocolComposition.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/ProtocolComposition.lean), [ProtocolExamples.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/ProtocolExamples.lean), [dedicated checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/check_protocol_composition.py), [saved audit](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/protocol-composition-audit.txt), [mathematical companion](PROTOCOL-COMPOSITION-MATH.md) and [canonical account](../../../../theories/becoming/chapters/PROTOCOL-COMPOSITION.md). I also inspected the imported causal, controller, refinement and support interfaces, and the earlier [finite rational compiler](../../../../experiments/integrated-correction/general-framework/generative-basis/formal/FORMAL.md#5-an-explicit-generative-instruction-set).

The new boundary-state subtype restricts macro states to actual permitted boundaries. `BlockPath` requires at least one actual micro-event and returns to a boundary for the first time: every intermediate state is nonboundary. The same committed command constrains every edge. This prevents an empty macro action from supplying an unmodeled memory update, although a nonempty event can still have zero declared cost.

`Realization` retains the actual representative at each successive boundary before concatenating micro-event words. `ReportedRealization` additionally retains the observation delivered at every such boundary. The proof does not replace that intermediate representative with another state having a convenient report or reserve.

The controller theorem decodes both abstract world and memory from the concrete boundary state. Its local premise equates the reported block relation with the abstract closed-loop relation from **each concrete starting representative**. The premise therefore includes the selected command, complete relevant observation and controller update. The existing finite-history lifting theorem, followed by block realization, gives the claimed equivalence. No separate free memory register is added by the construction.

This is a criterion for an implementation, not a demonstrated implementation of the formed selector, updater or paid predictor. Neither this theorem nor the examples establish the required decoding and local equivalence for those distinct material laws. The protocol's permissions, command retention and report mechanism remain supplied. In particular, an existential micro-path is not an observation-adapted scheduler capable of selecting that path without hidden information.

## Costs, incomplete executions and completion

The support proof applies the existing account law to the actual flattened micro-history. Its prefix theorem splits a **completed realization** at an actual intermediate state and retains both accounting histories. It is not a claim that an arbitrary unsuccessful attempt is a completed realization. Incomplete attempts remain describable by the original micro-process and its ordinary trace/support account.

An account law is a net inequality. It does not establish prepayment: a credit and expense on one edge may balance without a separate upfront guard. The example implements the stronger requirement through distinct payment and receipt events. Entry requires positive usable fuel; later replenishment consumes a finite source unit. A favorable terminal balance cannot enable entry from zero usable fuel. Two completed blocks consume two different source units, and the third completion is unavailable.

The paid-deadlock witness is especially useful. From one usable fuel unit and no source, the process pays into a busy state with zero fuel and zero source, where every event is disabled in the nonstall implementation. This last-fuel loss has no completed macro edge. The proof preserves it as an explicit micro-history rather than calling absence of completion absence of an attempt.

The stall counterexample survives the stronger protocol-level check requested during review. It does not merely add an unrelated ambient action: the same permitted internal `tick` can either complete or remain busy under the same committed command. The two implementations have identical completed macro-step and finite macro-history relations, while one admits an explicit infinite committed execution that never returns to a boundary. This refutes a guarantee inferred from completed-block equivalence. No scheduler, probability, fairness, physical elapsed time or thermodynamic plausibility is inferred from that discrete run.

The rank results are also correctly limited. Strict descent of a natural-number rank on every internal transition bounds internal histories and excludes infinite internal execution. It does not prove that an unfinished state has an enabled next event. Deadlock remains possible; a completion theorem needs additional progress premises.

## Verification evidence

The saved audit reports a fresh temporary build with Lean 4.29.1, all seven source modules compiled successfully, and no source change during the build. The checker copies the captured source bytes into the temporary directory, recompiles project dependencies there, rejects the declared proof placeholders and shortcuts, and matches the requested axiom audits to the new theorem declarations. I inspected the checker and compiler output; I did not rerun the build.

The record contains **39 new theorem audits: 17 generic protocol results and 22 example results**. Seventeen have empty axiom-dependency lists; the remaining dependencies are limited to standard `propext` and `Quot.sound`. These counts concern theorem declarations, not distinct scientific observations or 39 independent discoveries. The central controlled-implementation equivalence has an empty dependency list.

At this review, all seven source hashes, the checker hash, toolchain-file hash and compiler-binary hash matched the saved record. The following digests identify the reviewed artifacts:

| Artifact | SHA-256 |
|---|---|
| `ProtocolComposition.lean` | `f7722a463fe05d2cc14b7c1cc3bc89b9c1d1435febb1c084a000f48ce98d9ee3` |
| `ProtocolExamples.lean` | `0b575dcc675e9489b3e7cbeece309061352d840b60f9565b8ac6ba46df502e14` |
| `check_protocol_composition.py` | `e9c1d2e52ac46058a659af7f256f75442f6509e4db181f0f4c15d9e96405e412` |
| `protocol-composition-audit.txt` | `14f33300e7e03383e71bb9aea2b1530d0d40de3a17876876060fb3851a42eb90` |

The code and inspected prose agree on the accepted scope. The canonical verification paragraph was still marked pending during this inspection; it can now be updated to the recorded result above. No blocking mathematical or implementation-scope issue remains in the reviewed artifacts.

## Remaining connection to the foundation

The earlier rational compiler established expressiveness at atomic macro boundaries while explicitly leaving paid intermediate execution outside its model. This result supplies a relational interface for actual finite micro-execution; it does not prove that compiler's physical implementation or transport its stochastic probabilities.

Boundary equivalence alone preserves neither intermediate safety nor probability, elapsed time, fairness or a completion guarantee. Any intermediate harm, intervention, record mutation or command interruption relevant to an application must remain represented and checked. Returning to an equivalent boundary cannot erase it.

The next concrete mechanism must establish the local contract for an actual acquired-and-revised predictor: locate its inherited records, identify each paid physical operation, match commands and delivered observations, and retain aborted histories under the claimed outcome measure. Hardware formation, shared evaluative use, concern and universal explanatory adequacy remain further obligations. This accepted result closes the missing event-granularity interface at its conditional scope; it does not complete that end-to-end derivation.
