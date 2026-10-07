# Lean correspondence for general ideal admission

7 October 2026. AI-authored implementation note responding to Ren's requirement that proofs in this continuation be formalized and checked. The [Lean source](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/completion/formal/IdealWarrant.lean) compiles with **Lean 4.29.1**, importing only `Std`. It proves the general poset results in [the existing hand proof](COMPLETION-WARRANT-MATH.md); it does not encode philosophical warrant as an axiom or claim that normative justification follows from completion.

The supplied `Poset` represents the selected approximation relations. `Ideal` explicitly requires nonemptiness, lower closure and directedness. `FiniteRefutable`, `ScottClosed` and `Admits` are separately defined predicates. Consequently the equivalence is proved between independently stated conditions rather than inserted into a definition. Predicates range over arbitrary ideals and families, not an enumerated finite sample. The implementation even permits the approximation type itself to be empty, although the original exposition fixes a nonempty poset.

| Existing result | Checked declarations |
|---|---|
| Principal ideals, arbitrary directed unions, principal approximation of every ideal | `principal_le_iff`, `le_familyUnion`, `familyUnion_le`, `principalFamily_directed`, `union_principalFamily` |
| W1, finite refutation iff Scott closure iff a lower permitted basis | `finiteRefutable_iff_scottClosed`, `scottClosed_iff_lower_basis`, `finiteRefutable_iff_lower_basis` |
| W1, unique basis and its principal/union descriptions | `lower_basis_unique`, `basis_eq_permitted`, `permitted_eq_content`, `basis_eq_content`, `refutable_eq_admits` |
| Explicit identification with ideals of the lower subtype | `lift_restrict`, `restrict_lift`, `lift_order_iff` |
| Empty admission class and empty lower basis | `admits_empty`, `empty_scottClosed`, `empty_finiteRefutable`, `empty_content`, `empty_lower_no_ideal` |
| W2, least Scott-closed enlargement | `hull_scottClosed`, `hull_contains`, `hull_least`, `hull_unique` |
| W2, no new finite content and no unsupported finite combination | `hull_preserves_content`, `hull_joint_content` |
| W2a, finite prohibitions and maximality | `avoiding_lower`, `respects_iff_admits_avoiding`, `respects_maximal` |
| W2a, unique finite-refutable class with the specified principal classification | `respects_finiteRefutable`, `respects_principal`, `respects_unique` |

Here “finite” refers to the stipulated interpretation of elements of the approximation poset. The theorem does not prove that arbitrary poset elements are finitely observable, computationally decidable or physically available. `Respects` permits an arbitrary set of forbidden finite contents; the set itself need not be finite or decidable.

Every named theorem has a `#print axioms` audit. The maximum dependency set reported is `propext`, `Classical.choice`, and `Quot.sound`, Lean's standard logical foundations. There are no custom axioms, proof placeholders, admitted goals or `native_decide` calls. In particular, classical extraction of a forbidden approximation is not an effective witness procedure. The exact audit output should be retained by the aggregate checker alongside the toolchain identity and source hashes.

From the repository root, the direct check is:

```sh
lean +leanprover/lean4:v4.29.1 experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/completion/formal/IdealWarrant.lean
```

This supports the current normative priority by identifying precisely what a preservation/completion argument establishes. Closure of an independently admitted class does not justify that class's ethical warrant, and an omitted global requirement cannot be recovered merely by completing its finite content. That distinction concerns what the selected representation preserves within the same unfolding; it does not posit separate causal and evaluative realities. The substantive argument and rival assessment remain separate research obligations.
