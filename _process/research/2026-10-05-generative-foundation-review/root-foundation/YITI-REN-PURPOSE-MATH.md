# Purpose correction through actual continuation

6 October 2026. AI-authored mathematical note for Ren's request to complete formal proofs alongside the proposed direction of inquiry. This note explains [PurposeCorrection.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/PurposeCorrection.lean), using the existing `Generative.Process`, `Generative.Trace` and conservative joint-occurrence interface. The [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md) governs its interpretation.

## Declared content and preserved distinctions

An activity's selected continuation contract consists of a state condition \(K\) that must hold throughout the continuation, and a terminal condition \(G\). Neither is a reward, an ethical reason predicate or a primitive owner. They are supplied local descriptions of the activity being studied. Their historical formation, adequacy as descriptions and ethical standing remain further questions. The current representation preserves actual transitions and intermediate states; it omits phenomenology and the endogenous formation of its own descriptive criteria.

Write \(P|K\) for the process retaining exactly the transitions \(s\xrightarrow e t\) of \(P\) for which \(K(s)\land K(t)\). A contract-fulfilling continuation from \(s\) to \(t\) is a trace of \(P|K\), together with \(K(s)\) and \(G(t)\). Explicitly requiring the source condition prevents an empty trace from bypassing it. An empty completion is legitimate precisely where both \(K\) and \(G\) already hold; it does not demonstrate newly formed capability.

`Viable P K G s` means that some actual finite contract-fulfilling continuation exists from \(s\). This is an existential possibility claim. It is not guaranteed success, actual selection, low resource use, autonomous initiation or termination of every run. In particular, retaining a self-loop can leave a state viable while an infinite repetition never completes.

## The exact productive restriction

Define \(R\) by

\[
R(s,e,t)\iff P(s,e,t)\land K(s)\land\operatorname{Viable}_{P,K,G}(t).
\]

This is a mathematical construction. The Lean proofs are constructive in their handling of existential witnesses: composition uses the supplied continuation from the actual reached state and does not need a choice principle. That does **not** furnish a decision procedure for viability over an arbitrary process, nor a physically formed mechanism that computes and installs \(R\).

Moreover, \(R\) restricts transitions, including successor outcomes. In a nondeterministic process, removing a bad successor while retaining another successor under the same event need not be an available intervention. Existential viability is therefore not an executable policy with partial observation or a guarantee against adverse outcomes. Such claims additionally require a realizable control interface, sufficient available distinctions and a contract over the relevant alternative outcomes; the separate inquiry-sufficiency results address that kind of obligation. The present theorem does not import their stronger conclusions.

`productive_trace_exact` proves, from a viable source, that

\[
\operatorname{Trace}_R(s,w,t)
\iff
\operatorname{Trace}_{P|K}(s,w,t)\land\operatorname{Viable}_{P,K,G}(t).
\]

In the reverse direction, the actual remaining suffix followed by the terminal continuation supplies viability at each intermediate state. The proof does not splice an unrelated favorable endpoint into the history. `contract_append_iff` makes the same requirement explicit for two contract segments: they must meet at the same full state.

`productive_contract_exact` proves that this restriction loses none of the original finite completions of the same \(K,G\) contract. `productive_restriction_largest` gives its maximality among subrelations of \(P\) whose steps begin in \(K\) and end at states admitting a \(P\)-completion. This is a precise relative maximality result; it is not a largest universally good organization.

## Why filtering alone is insufficient

`no_restriction_creates_completion` proves: if \(P\) admits no contract-fulfilling continuation from \(s\), then no restriction of \(P\) can supply one. A correctness filter can remove inadmissible histories but cannot generate a missing route. The concrete [inquiry-history adapter](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/PurposeCorrectionHistory.lean) tests whether an actual arrangement change supplies such a route; it must not be described as simply applying the filter.

Conversely, if \(Q\) retains every transition of \(P\), `contract_extension` preserves every existing contract continuation, and `productive_capacity_extension` preserves every old productive transition. Both use exactly the same \(K,G\). They do not show that arbitrary newly added paths preserve the contract, that the target is adopted, or that expanding capacity creates ethical authority. If the actual meaning of the target changes, a further correspondence argument is needed.

## Actual histories cannot be replaced by an equally labeled alternative

In a nondeterministic process an unannotated event word can have several realizations. Existence of a safe realization does not certify every realization of that word. `stateOccurrences` therefore preserves each event's full before/after states using the existing conservative description interface.

`actual_violation_not_erased` takes an actual described prefix, its actual continuation from the reached state, and a witnessed violation in the prefix. It proves both that the combined history remains an actual history and that this same full occurrence history cannot be certified as \(K\)-preserving. A later successful outcome cannot remove the earlier occurrence. This does not forbid prospective repair, and it does not define all burden as a violation of \(K\): the selected activity's actual requirement must be independently specified.

## Scope of the advancement

The formal result distinguishes three tasks that a purpose-correction account cannot conflate: retaining the content of a selected activity across actual intermediate changes; removing routes that defeat that content; and forming a new route when none of the old continuations meets it. The proofs complete these structural claims for arbitrary declared processes. They do not complete the genesis or universal normative justification of 仁. The native bridge and philosophical argument must state separately what they add to this structural result.
