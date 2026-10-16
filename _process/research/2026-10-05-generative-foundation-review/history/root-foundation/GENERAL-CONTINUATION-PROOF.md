# General continuation requirements and their actual implementation

7 October 2026. AI-authored mathematical proof report for [Ren's request for a general derivation](../../../../sources/15-codex-theory-conversations/2026-10-07-general-generative-proof-request.md). This accompanies the [dependency proof](SITUATED-RENEWAL-PROOF.md), [ethical argument](GENERAL-GENERATIVE-REQUIREMENT-ARGUMENT.md) and [integration](GENERAL-GENERATIVE-REQUIREMENT-INTEGRATION.md). All new mathematical statements below refer to the checked [SituatedContinuation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedContinuation.lean) and [SituatedRenewal.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean).

**The proof is uniform over represented processes, histories and dependency families. It does not enumerate cases.** It establishes necessary responses to actual dependency use, requirements on the actions of a continuing history, and sufficient certificates from which an actual indefinitely continuing history is constructed. The examples delimit stronger inferences; they are not the basis of the general proofs.

## 1. The common represented subject

`GenerativeCore.Process` supplies a relation `P.step s a t`. Its states represent selected configurations of one unfolding and its events represent changes within it. Actual finite traces retain their intermediate states. The new results do not posit an independently existing agent and environment, or treat an evaluator's success measure as the origin of the process.

The representation preserves the relationships needed for the stated claims. It does not identify biological life or ethics merely by naming a predicate. `alive` is an independently specified represented condition. A genuine application must explain which living relationships it preserves and what it omits. The whole process, its actual supply relations and the adequate interpretation of replacement cannot be recovered from the mathematical type alone.

## 2. Necessary renewal or replacement

For each dependency, the [support-accounting theorem](SITUATED-RENEWAL-PROOF.md) starts with a transition inequality: if its provision route stays the same, remaining support after the step plus required use cannot exceed previous support plus the support actually added. That local law does not assume renewal will happen.

Composing these inequalities proves that any actual finite demand exceeding inherited support must include positive support addition or a route change. If the inherited route cannot add support during that window, a change away from that route is necessary. Repeated excess demand from every reached starting point yields arbitrarily late responses for each required dependency on the same actual history.

Zero-demand steps are allowed. Requirements are indexed separately; there is no single global support score or requirement that every participant perform every response. A response can be too small or an alternative inadequate: the theorem establishes necessity, not successful repair. Support accounting on a changed route and joint adequacy remain obligations for the actual process.

## 3. Actual continuation constrains situated actions

`HasContinuation P alive s` means there is one infinite admissible history beginning at `s` in which the represented condition holds at every state. It supplies no algorithm for deciding that property and no policy for selecting such a history.

`actual_suffix_continues` proves that every reached state of an actual continuing history has its actual suffix as such a continuation. All states and events are shifted together; nothing resets at the new starting point.

`excludes_all_routes_cannot_sustain` gives the corresponding general exclusion. If every admissible outcome of an action lacks the specified continuation, no actual history taking that action can sustain it. This is a necessary constraint relative to that fixed target. It does not say that one favorable outcome guarantees success, or that any unrelated target has thereby become mandatory.

`joint_continuation_supplies_components` retains the same witness when projecting a jointly satisfied family of conditions. It does not infer joint feasibility from separate histories. `continuation_realizes_required_dependencies` then joins the two modules: given one actual living-condition continuation and the independently stated cumulative-demand premise, that same history contains the required responses for every dependency. There is no exchange of “each dependency has some possible history” with “one history satisfies them together.”

These are exact logical consequences about actual realization. They constrain a practical claim to sustain the target, but their statements contain no ethical obligation.

## 4. A sufficient certificate for situated realization

The next result makes adequate local rules precise. Supply:

1. A state predicate `Inv` and a proof that it realizes the independently stated `alive` condition.
2. A context-dependent action relation `allowed s a`.
3. A retention proof: every actual allowed outcome from an `Inv` state remains in `Inv`.
4. An independently identified renewal event and a natural-number rank. Every such outcome either realizes renewal or strictly lowers that rank.

`rules_retain_invariant` proves invariant retention by induction on the actual history. `certified_history_renews` proves that, after any reached starting time, renewal occurs within the current rank plus one candidate transitions. Its constructive proof examines the positive renewal-or-decrease disjunction. If renewal has not occurred, it descends to the next smaller bound; rank zero excludes another nonrenewing step. The rank can reset when renewal occurs. It is a certificate for this implementation, not a universal material stock or ethical quantity.

The theorem covers **every supplied actual history complying with the rules**, including all nondeterministic outcomes governed by those universal hypotheses. It does not assert that an action is available at each state or that a compliant history exists. Nor does the renewal conclusion independently establish `alive`: that follows through the separate invariant and realization certificate.

`implemented_rules_sustain` supplies the existence direction. In addition to the certificate, provide explicit functions `choose s` and `next s`, together with a proof that every invariant state admits that chosen action with the selected successor, and that the action is allowed. Starting from an invariant state, recursive iteration constructs a single actual infinite history, retains `alive`, and realizes renewal within the proved bounds.

No choice axiom selects unknown successors. The implementation functions are supplied data whose admissibility is proved, not functions synthesized by the theorem. If an event has outcomes beyond those the implementation can control, existence of this selected realization is not a guarantee that it will occur; the all-outcomes history theorem has its own stated hypotheses. Full-state access, empirical controllability and finding the certificate are not silently established.

## 5. Checked limits and alternatives

The following checked constructions protect the general result's interpretation:

| Construction | Exact conclusion |
|---|---|
| Idle process in `SituatedRenewal` | Abstract admissible continuation with zero required use can have no renewal or route change. The generic core alone therefore does not entail the extra dependence premise. This is a limit of that interface, not a model of life or a refutation of the fuller theory. |
| Two restoring implementations | A supported-use event reduces a two-state support condition; either repair or replacement restores it. Two actual recurring histories exist, one never using replacement and one never using repair. Neither sufficient recipe is individually necessary. |
| Permanent opportunity | Every state reached by an actual waiting history admits a one-step completion, but that history never completes. Continued availability does not itself supply actual progress. |

The opportunity example does not make all waiting wrong. It shows why a claim of actual realization needs more than preserved attainability. The restoring implementations do not assert rising complexity or diversity. Their event laws are transparent witness constructions; the universal theorems do not depend on choosing these examples.

## 6. What comes from the core and what remains supplied

The core supplies admissible state changes and composition through the actual reached states. The proof adds general explicit premises: dependency accounting and repeated use for necessity; invariant retention, progress and an admissible implementation for sufficiency. Consequences are then proved for every instance meeting those premises.

This is a real general derivation from the core **plus those identified relationships**. It is not a derivation of all physical laws or living dependencies from the bare `Process` type. The idle construction makes that boundary exact. A law supplied to a local formalization is not thereby outside generative reality; its formation, interpretation and connection to the full account remain research obligations. Previously established native accounting laws and formation mechanisms remain credited rather than reopened as if absent.

The condition that continued humanity or life deserves support, and the justified scope of particular responses, is also not produced by assigning `alive`. The accompanying ethical argument explains conditional practical relevance through the same justified continuation and retains the first-warrant task. There is no proof here that every persistent system ought to continue, that more complexity always improves life, or that every individual must produce.

## 7. Verification

The [fresh checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/check_situated_continuation.py) snapshots the full four-module repository import closure and compiles it in an isolated directory with Lean **4.29.1**, using no cached project imports. It generates a separate audit for every explicit top-level declaration, including definitions, structures, inductives and the named instance in the inherited module. Generated declarations are also kernel-checked during compilation; the audit count refers to explicit declarations.

The [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/situated-continuation-verification.json) records **92 audits**, including **42 new declarations and 24 new named theorems**. Thirty-five new declarations have empty dependency reports; seven use only `propext` and `Quot.sound`—six dependency arithmetic declarations and the composition that uses them. There is no custom axiom, `Classical.choice`, proof hole, `native_decide`, warning or compiler error. These are not 24 independent discoveries or a no-assumptions completion claim.

Exact source, checker, compiler, generated audit and raw output are retained in the dated run identified by the receipt. The [independent review](GENERAL-GENERATIVE-REQUIREMENT-REVIEW.md) checked the theorem interpretations and current/snapshot hashes without repeating compilation. The renewal investigator separately reviewed the implementation module. Neither internal review nor formal checking establishes empirical correspondence or first ethical warrant.
