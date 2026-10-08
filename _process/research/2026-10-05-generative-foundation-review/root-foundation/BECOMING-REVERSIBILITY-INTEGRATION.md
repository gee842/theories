# Becoming, return and loss of possibility / 变化、返回与可能性丧失

9 October 2026, Asia/Bangkok. AI-authored continuation under the [Theory of Becoming priority](../../../../sources/15-codex-theory-conversations/2026-10-08-theory-of-becoming-priority.md). This is a separate scoped connection alongside the concurrent [effective-capacity study](RELATIONAL-BECOMING-INTEGRATION.md), not a replacement of its formation-mechanism frontier.

## Reuse and new inference

Result: `endpoint-loss-and-return`. Reuse the existing `Generative.Trace`, its zero-step history, and `trace_append_iff`. Related results are `trace-law-equivalence` and `effective-capacity-and-eventual-reachability`; they are conceptual connections, not imported adapters. The present module imports only `GenerativeCore`.

Delta: an exact return criterion for preserving all existential endpoint possibilities; a constructive witness for their loss; persistence of that loss along admitted continuations; and controls distinguishing incomplete observation from genuine preservation. The prefix-composition lemma is credited as reused mathematics, not another foundational discovery. The result is a structural characterization in the existing finite-history language, with no claim of mathematical novelty.

Supplied: a fixed relational process law, configuration identity, finite labelled traces, existential reachability, endpoint predicates and Lean's logical machinery. The full endpoint test family is mathematical: it does not assert that an inquirer knows every question or can recognize an entire configuration. G0/J and ethical rankings are absent. None of this establishes zero substantive assumptions.

## 1. The question concerns one unfolding

同一变化使关系发生、持续或消失；我们问其后是否仍有实际路径恢复所指关系。状态不是独立主体，步骤也不是一个外部主体推动客体：它们表示同一展开中选定的关系及其接续。需要保留的身份与区别须由实际目标说明。

An actual path from `s` to `t` is assumed when interpreting the result as a change. `Reach P s t` means some finite trace reaches `t`. `Possible P s q` means some reachable endpoint satisfies `q`. A returned configuration does not erase the intervening history, experienced losses, obligations or resource use. If those belong to the target, they must be represented; equality of a coarser configuration is insufficient.

## 2. Exact checked characterization

For an actual reached pair, the theorem is:

\[
s\leadsto t\quad\Longrightarrow\quad
\bigl[\forall q,\ \mathrm{Possible}(s,q)\leftrightarrow\mathrm{Possible}(t,q)\bigr]
\leftrightarrow t\leadsto s.
\]

One direction uses concatenation: return followed by an earlier possible continuation remains possible. The converse needs only the particular endpoint question `q(r) := r = s`, which is initially possible through the empty trace. If every initially possible endpoint question remains possible, this return question does too.

`irreversible_iff_endpoint_loss` proves the constructive negative characterization: failure to return has an explicit lost endpoint witness, namely reaching `s`. No classical choice or excluded-middle search is used to invent a lost question. `loss_persists_along_continuation` shows that an actually unreachable endpoint property cannot become reachable after further admitted steps under the same complete law: such later recovery would already have been a path from `t`.

**不可达不等于暂时做不到。** A capability temporarily unavailable can be restored through preparation; it was then still *eventually reachable*. The preceding effective-capacity result addresses exactly this difference. A discovery of a new route can correct a mistaken judgment of unreachability. Neither learning about a path nor restoring an immediate capacity refutes the fixed-law theorem. An actual repair already permitted in the full represented process is part of its reachability, including changes of effective local rules carried by that process.

## 3. Controls and correspondence limits

Two declared Boolean laws both admit the event `false → true`. One has no return; the other permits `true → false`. This tests exactly what the single observed event fails to specify. It does **not** show that two processes preserving all independently specified real relations can arbitrarily choose different laws. The fuller constitutive account is not refuted by these weaker descriptions.

The second control gives a constant observation of the one-way process. Every predicate on that observation has identical possibility answers before and after, although return is impossible. The hidden distinction is explicitly omitted by the observation. This is a diagnostic for inadequate representation, not evidence that the real distinction is absent. The [existing return-condition study](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ReturnConditions.lean) already shows how an added counter can prevent exact return while preserving projected endpoint questions. That result is interpretive context, not newly compiled here.

The remaining positive requirement is **target-relative recovery**: specify which actually formed relations need restoration and which changes must remain recorded. Recovery of a living function need not recreate an entire earlier configuration. Conversely, restoring a readout alone does not establish restoration of the relations it summarizes. The current theorem supplies a criterion once those meanings are fixed; it does not choose them automatically.

## 4. Author counterreview

- **Does including all outcomes explain the law?** No. The law determines which paths exist; the theorem derives a relation among those paths. This is progress in the explanatory structure, not a completed law-origin explanation.
- **Does irreversible change imply ethical deterioration?** No. Ending a harmful arrangement can be irreversible; a reversible process can cause real loss. Such ethical claims require the independently retained G0/J account and actual correspondence.
- **Does a return delete harm?** No. Equal modeled endpoints do not equate histories. This result provides no release of a responsibility and no compensation theorem.
- **Does every possible predicate have to be known before action?** No. The universal quantification belongs to a structural characterization. A particular supported lost possibility is already sufficient to rule out return within this representation; finite inquiry and practical judgment keep their existing scopes.
- **Is this a proof against the strong zero-axiom programme?** No. It identifies the current supplied law and identity obligations. The toy alternatives test a weaker event description only. Deriving or justifying the fuller relations remains an open foundational task.

## 5. Actual Lean verification

[Source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/BecomingReversibility.lean), [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_becoming_reversibility.py), and [source-bound receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/becoming-reversibility-verification.json).

Lean 4.29.1 compiled **10 new theorem declarations / 14 declaration audits**, all with empty named-axiom dependencies. These include helper lemmas and controls, not ten independent foundational discoveries. Recompiled `GenerativeCore`: **23 inherited theorems / 28 audits**, also empty. Two additional compiled examples are not counted as new theorems. Sources, checker, inherited scanner, compiler binary, signatures and logs are hash-bound in the retained run. An initial attempt had one impossible pattern alternative rejected by Lean; the corrected check passed and the earlier failed run remains preserved. This is author counterreview, not independent-agent acceptance or empirical validation.

## 6. Integration and next connection

The universal inference advanced is conditional but unrestricted over the supplied relational process types: return, preservation and loss follow one common path-composition structure. It adds no privileged agent, favorable direction or irreversible time law. The full Theory of Becoming and its zero-substantive-axiom hypothesis remain open.

Next use an existing actual formation/reconstruction mechanism to specify what restoration preserves, including support, history and effective capacity. Test whether the same continuation restores the relevant relations or merely a selected summary. Do not rebuild the already checked prefix composition, return controls or foundational conditional mechanisms. The canonical theory, result record and curated chain carry this contribution at its stated scope.
