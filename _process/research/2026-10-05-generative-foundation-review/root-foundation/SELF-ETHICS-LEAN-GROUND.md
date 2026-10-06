# Generated histories and ethical orientation: exact Lean boundary

6 October 2026. AI-authored formal study of **generated self/history → objective moral direction**, under Ren's no-assumptions requirement. The [chapter on the generated I](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATED-SELF-AND-ETHICS.md) supplies the research question, not a premise of the proofs. [EthicalOrientation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/EthicalOrientation.lean) adds no transition law, reward, ethical contract, custom axiom, or asserted property of all physical processes. It imports the existing `DynamicConsequences` interface.

The completed result is a structural derivation and a precise failure of a proposed sufficient condition. It does not complete the derivation of ethical significance or the formation of a phenomenal self. Empty Lean axiom dependencies do not discharge the interpretation of Lean, the supplied models, or the truth of a universal metaphysical foundation.

## What is derived

For the existing `Process` and `Trace`, define a comparison by feasible finite action words:

\[
s\preceq_P t \quad\Longleftrightarrow\quad
\forall w,\;\operatorname{Feasible}(P,s,w)\Rightarrow
\operatorname{Feasible}(P,t,w).
\]

This comparison is reflexive and transitive. It is preserved under the core's synchronous product: inclusion in both component states implies inclusion in the paired state. An exact representation of feasible words preserves and reflects the comparison. These are facts about declared finite existential capabilities. They require no preferred score, observer, or owner variable. They do not certify guaranteed control, infinite continuation, welfare, or moral value. The representation theorem has its exactness hypothesis written in its type; it does not assert that every proposed summary is exact.

A different derived statistic is a history's event count. Its usual order and its converse are both reflexive and transitive. Both survive any action renaming because list length is unchanged. Attaching a descriptive Boolean annotation to a history and then projecting it away also preserves both orders. The Boolean is not asserted to be a self, an ownership judgment, or any physically realized state. This construction tests invariance under an irrelevant description; it does not establish that every actual change in ownership experience is irrelevant.

## The closed counterexample

The existing `toggle` process has the following histories, without adding a new event law:

| Retained history | Initial state | Final state | Event count |
|---|---|---|---|
| `[]` | `false` | `false` | 0 |
| `[(), ()]` | `false` | `false` | 2 |

Both histories occur in the declared relational sense of `Trace`. Both permit every finite future action word. The entire compared histories remain available; the argument does not erase them merely because their endpoints coincide.

Ordering by increasing event count places the empty history before the cycle. Ordering by decreasing event count reverses that strict comparison. Both orderings are coherent, action-renaming invariant, and independent of the attached annotation. The process, endpoint facts, histories and future-word profiles remain identical between these candidate interpretations. The theorem `actual_histories_with_unselected_orientation` joins the actual traces and equal future profiles to the exact rejection of the implication

> Every reflexive, transitive, annotation-invariant ordering places the empty history before this cycle.

The theorem refutes that sufficient condition. It does not certify either ordering as morally correct, treat the two as equally justified moral accounts of reality, or prove that no richer constitutive account of value is possible. In particular, the converse is a counterinterpretation to the proposed formal criterion, not a defense of preferring extinction, cruelty, or fewer lives.

A second closed result shows that `toggle` admits no irreflexive, transitive state relation that strictly improves along every allowed event. The two directed steps would entail a strict self-comparison. This excludes the claim that this recurrent process strictly improves on every step under such a state order. It does not exclude weak progress, improvement in some regimes, history-sensitive evaluation, or a justified ethical reason that actual behavior violates.

## What remains supplied or unestablished

The existing law of `toggle`, discrete finite-history semantics, and mathematical background remain the supplied model context. The new orderings and annotations are mathematical constructions, not newly discovered physical or ethical laws. Generic mathematical parameters and hypotheses are quantified in theorem statements; they are not adopted as universal facts about reality.

No theorem identifies a trace with experienced adversity, establishes an actor-addressed reason from that adversity, derives morally legitimate authority, or identifies a continuation as beneficial to an affected center. A capability can sustain exploitation; reducing one capability may protect another center. Neither continuation inclusion nor event count therefore acquires an ethical interpretation merely by being definable without a fundamental owner. Conversely, the possibility of a justified owner-independent ethical ground remains open. Its positive identification and justification must supply content that distinguishes it from these opposite formally admissible extensions, without hiding the desired answer in a reward, `good` predicate, or C1/C2 contract.

What would change this assessment is a proposed derivation that identifies relevant actual conditions and proves why the warranted practical relation follows, while accounting for adverse regimes and the meaning of its formal terms. The present result only rules out using coherence, record retention, recurrence, event count, and description invariance as a sufficient substitute for that derivation. The next central bridge remains **actual experiential adversity and eligible response → justified practical significance**, together with explanation of how the relevant self/other representations arise and can be mistaken.

## Verification and the preserved unsuccessful route

The final module compiled in a fresh temporary directory with Lean 4.29.1, compiling all imported repository sources there rather than using local precompiled modules. All 17 new theorems have explicit `#print axioms` requests, and all 17 outputs state that the declaration does not depend on any axioms. The checked source SHA-256 is `00bcc4a7542d4b81f1e924207d1d5b82e1ae032c4e26d7031d2779914fd56cc4`. Integrated verification is maintained by the [model checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/check.py) and its [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/verification.json).

The first draft instead tried to instantiate strict continuation inclusion using the existing `Realization.process true`: its terminal state permits only the empty word, whereas its ready state permits `use`, and the existing law reaches both renewable and terminal outcomes. The intended opposed orders were inclusion and reverse inclusion, projected through the existing decorated badge. This remains a useful interpretation of that old model at its original scope. It was not accepted as a new empty-dependency proof.

The draft build first exposed omitted intermediate-state annotations in several reconstructed trace terms. More decisively, direct dependency queries showed that `Realization.law`, `Realization.process`, and `Realization.decoratedProcess` themselves already depend on `propext`. Therefore even a corrected proof whose type mentions them inherits that dependency. Replacing proof tactics would not remove it. The underlying pattern-compiled law was left unchanged, and its older claims and recorded audits retain their historical scope. The accepted module reuses the already axiom-free `toggle` model instead. This sacrifices the proposed new strict-capability witness; it does not repackage that witness as verified or claim to have removed the old dependency.
