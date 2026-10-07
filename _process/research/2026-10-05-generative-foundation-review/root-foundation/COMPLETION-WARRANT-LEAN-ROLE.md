# Lean verification of completion roles and concrete lifting

7 October 2026. AI-authored formalization and scope note, responding to Ren's requirement that proofs in the current mathematical discussion be in Lean and checked. The [earlier A1–A5 argument](MATHEMATICAL-ADMISSIBILITY-MATH.md) is preserved as the historical exposition. This note records the portions verified by the two modules below, rather than revising its historical verification claim.

The investigation follows the [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md). A basis, its completed profiles and their interpretation are related mathematical roles in the same inquiry. Their representation by different Lean types does not assert that they originate in independent ontological realms. The current ethical priority receives a limited supporting contribution: this verification identifies exactly which completion and preservation consequences follow from supplied mathematical roles. It supplies no ethical identification, reason for favoring a completion, motivation, or implemented preservation under learning.

## Checked correspondence

[CompletionRole.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/completion/formal/CompletionRole.lean) imports the same `CompletionWarrant.Poset` and `Ideal` used for W1–W2a. An ideal is a nonempty directed lower predicate; neither effective descriptions nor decidable membership are required. `Directed` quantifies over nonempty subsets, and `Dcpo` supplies a supremum operation with its upper-bound and leastness laws for every such subset.

| Earlier result | Lean declaration or group | Exact coverage |
|---|---|---|
| A1.1 | `principal_embedding` | Inclusion of principal ideals iff the original order comparison. |
| A1.2 | `idealDcpo` | Directed family union is an ideal and its least upper bound, reusing the shared union construction. |
| A1.3 | `principal_compact`, `compact_iff_principal` | Principal ideals are compact, and every compact ideal is principal. |
| A1.4 | `principal_generation` | Every ideal is the directed supremum of its contained principal ideals. |
| A2 | `extend_upper`, `extend_least`, `extend_monotone`, `extend_principal`, `extend_continuous`, `extend_unique`, `unique_continuous_extension` | The supremum of the image of an ideal gives the unique monotone, directed-supremum-preserving extension of an arbitrary monotone interpretation into any supplied dcpo. |
| A2a | `positive_reading_membership`, `positive_readings_separate` | The extended positive reading of a finite approximation holds exactly when that approximation belongs to the ideal; all such readings together separate ideals. Truth values here are propositions ordered by implication. No effective Boolean decision procedure is asserted. |
| A3 | `profile_extend`, `extend_profile`, `basisIso`, `basisIso_preserves`, `basisIso_unique`, `basisIso_backward_unique`, `unique_basis_representation` | A faithful compact embedding that directedly generates every point gives an order isomorphism from the ideal completion, uniquely fixing the basis in both directions. |
| A3 converse | `ideal_basis_role` | The ideal completion with its principal embedding satisfies all the role premises. |

`orderIso_continuous` proves that any order isomorphism between the supplied dcpos preserves their directed suprema; uniqueness in A3 therefore does not silently impose continuity on a merely order-preserving competing map. The proof explicitly requires an order isomorphism, including a monotone inverse.

`BasisRole` names, rather than discharges, its premises: faithful order embedding, compactness of each embedded approximation, a nonempty directed family of approximations below every point, and generation of that point by their supremum. `Dcpo` supplies full directed completeness. The equivalence is general for type-sized posets; it needs no additional inhabited-poset premise because an empty basis and its empty ideal domain are handled by the types.

## Classical finite-branching lifting

[FiniteBranching.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/completion/formal/FiniteBranching.lean) contains six checked results:

1. `reach_mono` truncates a finite run to any shorter length.
2. `finite_unbounded` shows that a finite family containing arbitrarily deep candidates contains one candidate with every finite depth.
3. `unbounded_child` applies this to a node's finite successor family.
4. `infinite_from_unbounded` constructs an infinite branch from such a node.
5. `finite_initial_lifting` allows a finite list of possible initial nodes.
6. `labelled_lifting` obtains one infinite concrete run realizing a fixed infinite requested label sequence, provided every finite prefix is realized and each specified-label successor family is finite.

The finite families are supplied as lists, with a proof that membership is equivalent to the transition relation. Duplicates do not matter. `RequestedStep` retains both the concrete state and the position in the requested word. Its clock changes by exactly one on every transition; the theorem proves this correspondence before projecting away the clock. Thus it does not infer a concrete run merely from a projected language of finite labels.

For A4b's additional prefix-closed history obligations, instantiate the concrete node type with full admitted finite histories and the step relation with an admissible one-step extension. The admitted initial nodes and children must be the actual finite families in that history tree. This is the same finite-branching theorem; an obligation imposed only on a completed infinite history is not thereby checked. The module proves the general relation and fixed-label lifting theorems. It does not encode every possible application's history predicate or verify any physical transition law.

Classical selection of an unbounded child is explicit. No computable branch selector, observation of an enacted infinite physical history, or satisfaction of a limit-only obligation follows. The hidden finite-budget counterexample remains outside the premises because its initial choice has infinitely many successors, or because its post-choice presentation has infinitely many possible initial nodes.

## Verification and remaining scope

Both modules compile with **Lean 4.29.1**, using `Std` and the shared local ideal module. Every named theorem in each module has a `#print axioms` audit: **30** in `CompletionRole.lean` and **6** in `FiniteBranching.lean`. The role module uses only the standard logical dependencies `propext` and `Quot.sound`, where needed. The lifting module additionally uses `Classical.choice`. There are no custom axiom declarations or incomplete proof terms, and no `native_decide` proof shortcut. Standard logical dependencies and supplied mathematical premises have not been erased by checking the proofs.

A clean check compiles `IdealWarrant.lean` into a temporary object directory, adds that directory to `LEAN_PATH`, and compiles the two modules with `lean +leanprover/lean4:v4.29.1`; their audit output is returned by the same invocation. The package check records the resulting compiler output and source hashes. No interpreter cache or compiled object is needed in the source directory.

This pair of modules does **not** claim coverage of A4's finite/infinite word classification, A4a's countdown example, A5's powerset representation, or every ancillary example in the earlier exposition. Those need their own named coverage in the package inventory. It also does not formalize the metaphysical claim of unique ultimate constitution or a normative warrant. A successful Lean proof verifies the stated implication; it cannot turn an unprovided grounding argument into a theorem.

## Independent review of the shared warrant theorem

The role-formalization pass independently read the shared W1–W2a source. Its finite-refutation condition quantifies over every rejected ideal and requires one contained approximation absent from every admitted ideal. The Scott-closed classification, uniquely recovered lower basis, empty-class treatment, least closed hull and finite-prohibition specialization preserve the intended mathematical scopes. No reliance on effective witness discovery or a merely finite sample was found. W2a's maximality concerns all candidates satisfying the independently supplied prohibitions; it does not warrant those prohibitions. Compilation of the role results also checks compatibility with the shared ideal representation.

## Explicit boundary examples and retained history conditions

The later [CompletionBoundaries.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/completion/formal/CompletionBoundaries.lean) adds **26** checked theorem declarations, with a kernel dependency audit for each, and closes the two A3 prose counterexamples as actual Lean constructions.

The first carrier is the ideal completion of the natural-number order. `natInfinity_classification` proves that it consists exactly of the finite principal ideals together with `allNaturals`, so the notation represents the intended natural numbers plus one infinity rather than merely assuming that interpretation. `infinity_is_old_sup` proves that the infinity already is the supremum of its finite points. `old_infinite_supremum_not_preserved` then proves that passing to principal ideals of this enlarged carrier fails to preserve that existing infinite supremum: the supremum of its embedded finite points is `finiteSegments`, whereas the principal ideal of infinity additionally contains infinity itself.

`infinity_not_compact` identifies the failed A3 premise. The identity embedding remains faithful; `identity_approximation` proves generation by all named predecessors for every point of every supplied dcpo. Nevertheless, `flatten_not_injective` exhibits the two unequal ideals `finiteSegments` and `principal infinityOrder allNaturals` with the same image under the supremum extension of the identity. Thus the example proves the proposed collapse, instead of merely declaring compactness absent.

The second example embeds a singleton basis as `False` in the implication-ordered truth dcpo. Classically that carrier has the two extensional truth values; no effective decision operation is inferred. `onlyFalse_embedding` and `onlyFalse_compact` prove faithful comparison and compactness. Every point has a nonempty directed family of named predecessors, but `false_generation_at_true` proves that the named predecessors of `True` generate only `False`. `true_not_generated` and `onlyFalse_not_basis` record the failure. `unit_ideal_unique` separately proves that the actual ideal completion of the singleton basis has just one point. This makes the extra point and its failure of generation explicit.

Finally, `guarded_concrete_lifting` addresses the history-obligation interface directly. Given a concrete transition relation with enumerated finite successors, an admitted-node predicate, and arbitrarily long finite runs retaining that predicate, it filters initial nodes and successors by admission and obtains an infinite concrete branch whose **every node remains admitted**. To apply this to prefix-closed obligations, nodes retain full finite histories and transitions extend them by one step. A condition applying only to an infinite completed history is outside that finite-node hypothesis; the theorem does not silently turn it into a safety condition.

This module imports the existing role/examples and finite-branching modules. Lean 4.29.1 compilation succeeded, and its audits report only the standard dependencies `propext`, `Classical.choice`, and `Quot.sound`. Neither a custom axiom nor an incomplete proof is used. The combined package checker should compile this module after `CompletionExamples` and `FiniteBranching`.
