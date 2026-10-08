# Infinite branching, common witnesses and explanatory recovery

8 October 2026, Asia/Bangkok. AI-authored continuation of [Ren's instruction](../../../../sources/15-codex-theory-conversations/2026-10-08-generative-explanatory-necessity.md#继续检验范围--continue-the-scope-test). The [preceding branching study](EXPLANATORY-BRANCHING-INTEGRATION.md) established the finite-branching bridge. This round tests that restriction and retains the question of universal explanatory necessity.

**Result / 结果。** Finite branching can be replaced by successor compactness: every family of finite continuation questions whose finite parts are jointly realizable among the successors has a single successor realizing the whole family. Under this explicit condition, finite-test equivalence again forces bisimulation and, with reachability and state separation, a unique structural correspondence. Exact reduced codes preserve all finite histories and lift an entire infinite code run from its particular compatible native start. 无限分支本身不是障碍；有限部分的见证能否统一，是这条恢复推理的关键。

**Boundary / 边界。** A countably branching countdown process and a version admitting an additional endless branch agree on **all finite Boolean modal questions**, despite differing on infinite-run existence and admitting no root-related bisimulation. The second model is successor compact and not image-finite; the first is not successor compact. Thus the replacement genuinely extends the model class, and the condition cannot simply be omitted. It is a sufficient condition for the general theorem, not a claimed necessary condition for every particular successful comparison.

**Checks.** 36 new Lean theorems: 14 general results and 22 concrete results, including supporting lemmas. Eleven modules yield 159 declaration audits, of which 123 are inherited. The new dependency lists are 5 empty, 5 `propext` only, 13 `propext`/`Quot.sound`, 12 `propext`/`Quot.sound`/`Classical.choice`, and 1 `Classical.choice` only. Full totals: 102 empty and 57 standard lists. No custom axiom or proof hole is used. These are declaration counts, not 36 independent mathematical discoveries.

## 1. The universal inference being tested

The governing question is why an adequate explanation must preserve generative relationships. The prior affirmative argument concerns fidelity to an independently specified target: an account of formed capacities cannot erase a difference that changes which capacities the same reached condition retains. It does not require every local explanation to recover all reality or every actual past.

This round tests a precise inference within that argument:

**correct answers to every finite compound continuation question → a common relation matching the possible successors.**

The mathematical work extends where that implication is valid and locates a substantive failure when it is generalized without qualification. It neither grounds G0 nor reopens the completed ethical comparison and practical-judgment route. Its supporting relevance to generative alignment is fidelity of a claimed preservation argument: finite opportunities and a single sustained possibility have different content. Any normative significance or actual obligation to sustain them remains separately warranted.

States and steps articulate conditions and occurrences of one unfolding. The two models compare alternative whole descriptions of its admitted relations, not independently existing observer and world domains. A test is a semantic question about those relations. No apparatus, negative-evidence channel or ability to perform every test is assumed to have been physically constructed. The decomposition retains sequential possibilities and omits probability, duration, shared-resource concurrency and actual historical provenance.

## 2. Why successor compactness supplies the missing bridge

For a condition `s`, event `a` and family `Γ` of the existing finite tests, `FinitelyRealizable m s a Γ` means that every finite list from `Γ` holds jointly at some admitted `a` successor. That successor may depend on the list. `SuccessorCompact m` requires a single admitted successor satisfying all of `Γ` whenever this holds.

This is a realization requirement on the selected model. It is not the first-order compactness theorem's permission to find a different model, and not a rule authorizing enlargement of the actual possibilities. It is also not a prediction obtained from finitely many observations. Actual justification of this condition can come from a specified law or another supported construction; it is not automatic because the word “generative” is used.

`imageFinite_successorCompact` proves that the old hypothesis supplies the new one. If every candidate successor fails some requirement, finitely many candidates give a finite list of failed requirements, contradicting finite joint realizability. Empty successor sets are handled by the empty finite list, not by adding a successor.

For the converse from answers to structure, take the complete finite-test theory of one actual successor. Agreement at the initial conditions makes each finite conjunction from that theory realizable among the other condition's successors. Compactness supplies one successor satisfying the entire theory. Since the test language includes negation, it agrees on all tests in both directions. Apply this in both directions to derive a bisimulation.

The initial explanation is still an encoding with readings for questions; it contains no transition-decoder or structure-matching field. Reachability and separation of native states by the declared test family support the stronger uniquely matched relation and preservation/reflection of steps. No determinism or total-state finiteness is assumed.

## 3. A genuine infinite-branch comparison

The construction has one root, countdown conditions `finite n`, and a condition `endless`. A countdown greater than zero steps to its predecessor, zero has no continuation, and `endless` steps to itself. The root can enter any countdown. In the second version it can also enter `endless`; in the first version that condition is unreachable from the root. The same empty atomic vocabulary is used throughout.

Every finite modal formula has a finite depth. `finite_approximates_endless` proves that a countdown at least that deep and the endless condition agree on the formula, including arbitrary finite conjunctions and negations. A root-level existential question answered using the endless branch can consequently be answered using a sufficiently long countdown. Structural induction proves `roots_same_all_finite_tests` for the entire language, not just enumerated examples or finite words.

Nevertheless no fixed countdown matches the endless condition: a question asking for one more step than its length separates them. `no_rooted_bisimulation` rules out every root-related bisimulation. `countdown_has_no_infinite_run` and `completed_has_infinite_run` establish the difference for full functions `Nat → Node`, not merely for progressively longer observed prefixes.

The earlier [completion study](COMPLETION-WARRANT-LEAN-INTEGRATION.md#1-mathematical-content-and-formal-correspondence) already checked finite countdown words without an infinite concrete run. That fact and the classical example are credited. The present extension checks agreement on **all finite Boolean branching tests** in the new interface and identifies the exact successor-compactness contrast; the old finite-word obstruction is not advertised as a fresh discovery.

This is a formal rival about the same root continuation questions, not an empirical assertion that real processes terminate or an arbitrary change to a detached predicate. The recurrence of one condition is a legitimate limiting case here: no theorem claims it creates new diversity at every step.

## 4. The positive extension is nonempty and strictly broader

`completed_successorCompact` proves compactness for the second model. For any finitely realizable family, either every requirement holds at the endless successor, or some requirement fails there. In the latter case, the formula-depth theorem bounds the countdowns that can satisfy that requirement. Only finitely many candidates remain, and the finite-exclusion argument supplies one common witness. Other conditions have at most one successor.

`completed_not_imageFinite` proves that the root's successors cannot be listed finitely. Its countdown successors also have pairwise distinguishable continuation lengths, as characterized by `finite_survives_iff`; the extension is not produced solely by adding infinitely many indistinguishable names. Conversely, `countdown_not_successorCompact` proves that the first model fails the new condition.

Calling the second version “completed” names this constructed comparison. It does not license replacing a genuinely terminating process by that version: doing so changes its admitted whole histories while preserving its finite modal answers. The model's global realization condition must be assessed, not supplied by linguistic convention.

## 5. Whole-history lifting and the question-language boundary

The code law reuses the earlier existential projection of native edges. Under compactness, exact readings and reduction by all finite answers, every coded edge lifts from **each** native representative of its source code. `compact_code_trace_lifts` extends this to every finite trace. Thus projected pieces cannot create a spurious finite history through incompatible representative choices.

`code_run_lifts_of_step_lifts` proves a further generic connection: a specified infinite code run lifts from its specified compatible native start whenever representative-wise one-step lifting holds. Standard classical choice selects the consecutive witnesses; a dependent recursion keeps each chosen state connected to the next and preserves the code at every position. `compact_code_run_lifts` applies the result to the compact model condition. This is mathematical existence, not an effective selection algorithm, a physical infinite experiment, or an inference that every finite prefix was independently realizable.

A richer semantic question asks whether **one immediate successor** satisfies every finite survival requirement. The two constructed models give different answers. `no_finite_test_defines_unbounded_successor` proves that no single formula of the existing finite test language expresses that distinction even just across these two roots. Moreover their entire finite-test profiles agree, so merely collecting more answers from that language does not fix the omission.

This question quantifies over survival depths at one successor; in arbitrary processes it is still distinct from a single infinite run. Both predicates are checked separately in this example. No global equivalence is asserted. If a claimed explanation covers sustained realization, its question scope must retain the relevant common-witness or whole-run content. A narrower finite-question explanation remains adequate to its narrower target.

## 6. Counterreview and source assessment

| Challenge | Assessment |
|---|---|
| Compactness hides the desired bisimulation in a definition. | It specifies realization of finitely consistent test requirements in the same successor set. No relational correspondence is a field; the correspondence is proved. The condition is substantive and needs application warrant. |
| Infinite branching always defeats structural recovery. | False: the checked second model is compact with infinitely many distinguishable successors. The general compactness theorem applies. |
| Compactness is universally necessary. | Not claimed. It supplies a sufficient class condition; a particular noncompact pair may still be bisimilar. |
| The counterexample only matches words. | It matches every finite formula of the five-constructor language, including nested negations and shared-condition conjunctions. |
| Finite tests being inconclusive makes infinite truths unknowable. | No. A finite proof from an adequately supported rule can establish an infinite property. The insufficiency concerns the selected finite-test profile, not every form of reasoning or evidence. |
| The model class can be repaired by adding missing branches for free. | Such an addition can change infinite realization. Whether it faithfully describes the target is precisely a remaining explanatory requirement. |
| Whole-run lifting demonstrates actual persistence. | It establishes existence for a supplied, valid complete code run under audited hypotheses. It neither records an actual run nor supplies ethical warrant to enact one. |
| A static whole-constraint rival is excluded. | No. A rival retaining the same finite and relevant global relations may use a static representation. Ontological or explanatory priority is not settled. |
| This settles general shared-resource joining. | No. Sequential composition is preserved; genuine joint realization and competing resource use still need their own explanatory content. |

Read de Groot and Pattinson, [*Hennessy-Milner Properties via Topological Compactness*](https://arxiv.org/html/2105.01855), introduction and §7.1, especially Definition 7.54 and Proposition 7.55 in the retrieved HTML. Their account states modal saturation and its connection to image compactness, crediting the established classical Hennessy–Milner result. The present `SuccessorCompact` is an action-indexed semantic realization formulation of that familiar condition. No topology-equivalence theorem is formalized here, and no mathematical priority is claimed. The HTML and PDF were available; no source bytes were imported. Link-only reading on 8 October 2026 local time.

The [scientific-philosophy necessity assessment](SCIENTIFIC-COMPATIBILITY-NECESSITY.md) was read for integration. Its argument already distinguishes target-relative preservation from obligatory acceptance of the whole theory and G0/J. The present result strengthens a mathematical interface that it cites; it does not claim that its separate 13-theorem study or other studies' independent reviews validate this new package. This counterreview is by the authoring agent; no independent agent was requested or used.

## 7. Formal inventory and reproduction

- [ExplanatoryCompactness.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryCompactness.lean): 14 theorems. Finite conjunction semantics; finite exclusion; finite branching implies compactness; complete-theory matching; finite realizability from root agreement; compact successor matching; bisimulation; equivalence; reachable separated correspondence; step recovery; code steps; finite code histories; generic infinite-run lifting; compact infinite-run lifting.
- [ExplanatoryInfiniteBranches.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryInfiniteBranches.lean): 22 theorems. Three successor semantics lemmas; depth approximation; finite-branch agreement; two root decompositions; all-finite-test equivalence; endless survival; exact countdown lengths; failed matching; no rooted bisimulation; failure of compactness; three infinite-run lemmas and their combined witness; absent/present unbounded successors; failure of finite definability; positive compactness; failure of image finiteness.

The [immutable successful receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/explanatory-compactness-checks/20261008T075934.453234Z/receipt.json) records Lean 4.29.1, eleven current/frozen source bindings, compiler logs and all 159 declaration dependency lists. New counts are 36 = 5 empty + 31 standard; the inherited 123 are 97 empty + 26 standard. The new generic infinite-run lemma depends on `Classical.choice` alone; it must not be called constructive. No custom postulate, hole, unsafe bypass or warning is accepted.

Reproduce with `python3 experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_explanatory_compactness.py`. The runner compiles an isolated copied import closure; compiler products remain temporary. Earlier failures and the successful 34-theorem intermediate receipt are development history, not extra results. The final two theorems extend the same package to infinite code runs.

[Documentary checks](EXPLANATORY-COMPACTNESS-CHECKS.json) bind the proof inventory, current/frozen hashes, logs, local links, chapter additions and paired C30/F22 rows. [Owned edits](EXPLANATORY-COMPACTNESS-INDEX-EDITS.json) retain all prior row contributions and other rendered lines. These checks are local maintenance, not a repository-wide scientific audit. Previous receipts remain historical to their accepted source versions.

## 8. Integrated result and next unresolved bridge

The affirmative result is now broader: sufficiently complete answers preserve branching across a class including genuinely infinite branching, and the resulting coding can preserve entire infinite continuations. The counterexample identifies a real limit: a whole-run difference can survive complete agreement on every finite compound answer.

For the universal programme, the remaining burden is therefore to justify **which whole-realization and joint-realization questions the claimed explanatory target includes**, and what actual laws warrant the common-witness conditions. Adding compactness to every model by definition would not supply that warrant. The present generic theorem does not invalidate concrete laws or correspondences already established in the repository. Where a target includes actual formation history or competing simultaneous activity, use its warranted records and joint relations; the finite forward language alone still omits them.

**中文结论。** 已从有限分支推进到后继紧致性，并给出真正无限分支的正例；准确约简编码还能提升完整无限路径。但全部有限复合答案仍可能遗漏无限持续。解释必要性的根据应落实到目标确实包含的共同实现关系，不能由有限局部可行直接升级为普遍整体实现，也不能由这一反例宣布整个生成基础失败。
