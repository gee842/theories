# Mathematical core exposition and proof correspondence

8 October 2026, Asia/Bangkok. AI-authored record for [Ren's document request](../../../../sources/15-codex-theory-conversations/2026-10-08-mathematical-core-document.md). The current account is [A mathematical core for systems predicates and proofs](../../../../theories/becoming/chapters/MATHEMATICAL-CORE.md).

## Scope and contribution

The account reconstructs the context needed to understand and use the existing mathematical process core: the nondual method, the adopted logic, supplied dynamical content, inductive traces, least endpoint closure, predicates, conditional prediction, history representation, composition and exact abstraction. It distinguishes a motivated choice of representation from a deductive proof that reality uniquely requires that representation.

The substantive addition is a small pedagogical companion establishing invariant preservation, composition of existential/universal endpoint predicates, determinism of trace endpoints, and two counterexamples separating possibility, universal endpoint claims and execution. These are elementary results, not a novelty claim or a replacement of the existing derivation programme.

This supports the common derivation by clarifying the representation and inference contracts used in later organization, learning and ethical studies. Its universal statements quantify over the supplied process domains and laws. They do not establish universal normative warrant, physical coverage, or the unique constitution of mathematics. The current alignment task's explicit G0 route remains in force.

## Existing formal results rechecked

The [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_core_document.py) compiles six modules in a fresh temporary directory with a pinned toolchain and isolated `LEAN_PATH`. It copies source bytes before compilation, saves logs and source snapshots, checks expected empty-axiom audit counts, and verifies that each source remained unchanged during its check. Compiler products are discarded with the temporary directory. No shared project object files or other sessions' receipts are overwritten.

The [immutable successful receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/core-document-checks/20261007T192102.355920Z/receipt.json) records Lean 4.29.1 and **61 empty printed axiom audits across six modules**. The UTC timestamp is 7 October; the local user-facing date in Asia/Bangkok is 8 October. The [latest-run pointer](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/core-document-verification.json) permits routine reproduction without changing this historical link.

Forty-nine audits concern existing results: `GenerativeCore` 18, `GeneratedPaths` 9, `HistoryRealization` 7, `ProductTower` 7 and `BoundaryModels` 8. Their hypotheses and interpretations are preserved. This rerun is justified by their direct use in the requested foundational exposition; it is not a retrospective repository-wide audit.

## New companion claims and exact hypotheses

All names below are in `Generative.CorePredication`, in [CorePredication.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/CorePredication.lean). `P` is an arbitrary declared process. `May` existentially quantifies over endpoints of a fixed finite word; `Must` universally quantifies over those endpoints. Neither definition supplies a scheduler, probability, progress law or control ability.

| Declaration | Hypotheses and conclusion |
|---|---|
| `may_append_iff` | Under the existing trace definition, existential endpoint satisfaction for concatenated words equals nested existential satisfaction through a common intermediate configuration. |
| `must_append_iff` | Under that same trace definition, universal endpoint satisfaction for concatenated words equals nested universal satisfaction. Both sides allow vacuity when a continuation has no endpoint. |
| `trace_invariant` | A supplied predicate preserved by every primitive step, true at the starting configuration, holds at the endpoint of every supplied finite trace. |
| `reach_invariant` | The same hypotheses preserve the predicate under the existing existential finite-word reachability definition. |
| `invariant_excludes_endpoint` | With the same preservation law and initial truth, an endpoint violating the predicate is unreachable. |
| `feasible_and_must_implies_may` | A feasible fixed word and universal satisfaction at all its endpoints imply existential satisfaction at an endpoint. This does not prove completion of every partial execution. |
| `deterministic_trace_endpoint` | If each configuration/event pair has at most one successor, two traces with the same starting configuration and word have equal endpoints. No totality is assumed or concluded. |
| `deterministic_may_implies_must` | Under that determinism hypothesis, an endpoint satisfying the predicate implies every endpoint of the same word satisfies it. |
| `possible_not_guaranteed` | For the explicit Boolean process admitting every one-event endpoint, reaching `true` is possible but not universally guaranteed. |
| `blocked_word_not_feasible` | The one-event word is infeasible in the explicit process with no steps. |
| `blocked_must_is_vacuous` | In that blocked process, universal endpoint satisfaction of `False` holds vacuously for the one-event word. |
| `blocked_may_is_false` | In that blocked process, even existential endpoint satisfaction of `True` fails for the one-event word. |

All 12 declarations pass Lean and have empty printed axiom dependencies. The user-facing invariant proof is an explanation of these checked declarations, not a substitute for formal verification. No claim is made to have derived the meaning or ethical warrant of an arbitrary predicate from its name.

## Exposition review and substantive limits

The following is author self-review, not independent agent verification. The user requested a complete document; this task does not claim completion of the separate alignment or universal mathematical-grounding programmes that have their own review requirements.

**Positive argument.** The core connects local admissibility to arbitrary finite continuation. It permits predicates and induction over those histories and gives exact obligations for representation changes. It makes a broad class of mechanism arguments concrete without beginning from primitive actors or scalar objectives.

**Substantive alternative.** A history-language presentation can preserve the same finite-word feasibility, and the existing theorem explicitly constructs one. This shows the present state/event notation is a usable presentation rather than a certified uniquely necessary foundation. That alternative's supplied language is a substantive input too. The account compares what the two presentations preserve instead of calling the alternative a refutation of the whole theory.

**Counterexamples retained.** Product iteration cannot create a distinction from a subsingleton seed. Individually feasible allocations may have no common realization. Recurrent change need not revise a selector. A coarse observation can lose an operability distinction. Possibility does not imply universal endpoint satisfaction; universal endpoint satisfaction may be vacuous. These are scoped mathematical boundaries, not free reassignment of a rich ethical predicate presented as an ethical counterexample.

**Corrections applied in the exposition.** Formal zero-length histories do not assert physical waiting. `Trace` in `Prop` is not an exported execution data structure or a free category of path witnesses. A synchronized product is a stipulated composition mode. The abstraction lifting obligation applies to every detailed starting configuration in the relevant fiber. Exact finite-word behavior does not establish probabilities, intervention powers or infinite progress. A changing operative rule inside a configuration still has a declared broader law.

**Primary-source assessment.** The mathematical evidence is the actual repository source and its fresh Lean run. The official Lean chapters [Propositions and Proofs](https://lean-lang.org/theorem_proving_in_lean4/Propositions-and-Proofs/) and [Inductive Types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/) were read for the narrow account of proof terms and inductive reasoning. They are documentation of the logical machinery, not evidence for a generative ontology or ethical axiom. No new physical or biological claim is introduced.

## Repository integration and next connection

The current exposition is in the existing theory directory, the companion and reproducible check are in the existing Lean deeper-core directory, and this correspondence record remains in the established root-foundation study. Ren's exact messages are preserved separately from AI elaboration. Existing source modules are unchanged.

Navigation is added to `RESEARCH.md` and the theory README. The paired F01 chain entry is updated for the expanded explanatory scope, retaining the historic receipt while adding this document, companion and verification record. No new scheduled task is created and the separate full-results catalogue is not regenerated.

The document request is complete at the level of exposition and its declared proof scope. The next explanatory connection remains **justified actual law and predicate correspondence → warranted application of the finite-history results**, with probability, control, continuous dynamics and infinite continuation treated through the additional structures their claims require. This clarification does not restart already completed mechanism work or claim that G0 alone determines every practical comparison.
