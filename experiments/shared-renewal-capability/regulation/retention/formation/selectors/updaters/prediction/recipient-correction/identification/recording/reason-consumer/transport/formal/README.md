# Semantic contracts for evidence-to-action composition

6 October 2026. AI-authored supporting formalization. The named connection is **a reached source publication → an interpretation-preserving export → a separately warranted, feasible and causally effective action**. This package establishes the abstract semantic obligations. It does not implement the physical join or derive an ethical root.

Run `python3 check.py` here. The checker freezes `SemanticAction.lean`, compiles a temporary copy using pinned **Lean 4.29.1**, requires all declared theorems to appear in the dependency audit, rejects proof holes and custom axioms, and writes hashes and output into [verification.json](verification.json). The fresh check passes **16 theorem audits**, with only the standard `propext`, `Quot.sound` and `Classical.choice` dependencies. Most declarations have no axiom dependencies. Source and checker bytes are identified by the receipt; a theorem count is not a measure of empirical support.

## What is proved

| Interface | Checked result | Supplied premises and scope |
|---|---|---|
| Partial translation | An accepted translation preserves the interpreted claim iff it has no admitted counterexample. | Source/destination interpretations and justified world scope are parameters. This is one-way soundness, not full semantic equivalence. |
| Composition | Two sound partial translations compose along an actual intermediate world. Restricting the admitted scope preserves soundness. | A justified intermediate relation is required; arbitrary matching identifiers cannot supply it. |
| Nonvacuity | Rejecting every token is sound but exports nothing. | Useful completion therefore needs positive reached cases as well as rejection tests. |
| Command/patient collision | A command-one source can be true while its raw reinterpretation as a second patient's standing is false. A decoder injective on the two reached route masks cannot map both to the same fixed bearer. | The finite reconstruction uses the documented two-command/single-recipient and two-patient interpretations. No upstream Lean module is imported. Injectivity is restricted to the two actual one-hot masks, not impossibly required on four masks into two patients. |
| Separate bearer/action | A typed pair can preserve one patient while the command changes. | This corrects a representation collision; it supplies no new standing or causal benefit. |
| Role-sensitive transport | A declared role scope composes and preserves an instrumental claim when its patient, purpose-bearing role, applicable law and contextual conditions are retained. Different actor identities can satisfy it. | Legitimate role, purpose and transport authority remain supplied. The sample scope is sufficient; it is not the only permissible scope. |
| Freshness | A matching Boolean context label does not satisfy the sample scope after its generation changes. | The generation is an abstract semantic index. The actual implementation needs its paid or finite interlock; no free unbounded physical counter is asserted. |
| Separate stages | Sound admission implies reason truth under its two soundness premises. Finite models separate truth from warranted justification, justification from admission, admission from authority and delivered action, and helpful delivery from admission. | These are logical countermodels under declared predicates, not observations or a definition of ethical truth. |
| Missing evaluative bridge | Compatible commands and actual receipts can coexist with a false evaluative-good predicate. Authority and feasibility can coexist without a reason ground. | A causal/evaluative relation is necessary to infer those further claims. |
| Selected action | A selected admitted and enabled act has both its warranted claim and the stated delivered effect when **independent audit soundness and causal-realization contracts** hold. | The selection and feasibility premises concern the chosen act. The theorem does not make all patient claims jointly affordable or prescribe an action-selection rule. |

## Relation to the executable study

The adjacent [abstract adapter](../model.py) and independent checker operate on saved reached recipient-publication fixtures. They have their own finite integrity, scope, nonvacuity and resource-nonmutation checks. This Lean file imports only `Std`; it is **not a proof that the Python adapter implements these predicates**, nor that the active recipient or protection implementations already form one process. The source maps and frozen fixture review supply a separately assessable correspondence argument.

The interpretation collision is not an allegation that either upstream branch is wrong. The recipient branch explicitly uses the graph's two nonroot nodes for compatible commands to one recipient. The protection branch explicitly maps those nodes to two patients. Their shared finite storage shape cannot establish shared meaning.

Nothing here determines whether the support objective is justified, proves that recipient capture is good for its bearer, authenticates an authority, derives motivational uptake, or produces missing funds and hardware. Those remain explicit bridges of the full research objective.
