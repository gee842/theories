# Lean correspondence for finite and infinite history ideals

7 October 2026. AI-authored continuation of the [general ideal-admission formalization](COMPLETION-WARRANT-LEAN-IDEALS.md). The [Lean module](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/completion/formal/HistoryIdeals.lean) imports `IdealWarrant` and `PrefixSafety`, and compiles on Lean 4.29.1. It connects [A4's history-tree completion](MATHEMATICAL-ADMISSIBILITY-MATH.md#proposition-a4--ideal-completion-of-a-history-tree) to [W3–W6's admitted histories](COMPLETION-WARRANT-MATH.md#5-infinite-word-admissibility-and-forbidden-prefixes).

`Word A` is a finite length together with a coordinate function `Fin length → A`. This is the usual finite word represented by its positions rather than by a list. `Prefix` independently states the length comparison and agreement at every earlier position. `PrefixTrace` independently relates a finite word to a function `Nat → A`. `History` distinguishes these finite and infinite representations within this one prefix structure; it asserts no separate ontological kinds and makes no claim that a mathematical infinite trace has been physically enacted.

| Existing result | Checked declarations |
|---|---|
| Directed ideals contain compatible, hence comparable words | `compatible_prefix`, `ideal_comparable_by_length` |
| Bounded ideal has a greatest word and is principal | `bounded_has_max`, `bounded_is_principal` |
| Unbounded ideal assembles one coherent infinite trace | `mem_unionTrace`, `unionTrace_prefix_mem`, `unbounded_is_trace` |
| A4, complete finite/infinite classification | `ideal_classification`, `historyIdeal_surjective`, `historyIdeal_injective` |
| A4, order isomorphism rather than just a bijection | `history_order_iff`, with all four finite/infinite cases proved |
| A4, arbitrary prefix-closed language H | `history_admitted_iff`, `admitted_history_classification`, `lower_history_classification`, `admitted_history_unique` |
| W4, finite-only admission is lower, fails finite refutation and Scott closure, and has full hull | `finiteOnly_lower`, `finiteOnly_not_refutable`, `finiteOnly_not_scottClosed`, `finiteOnly_hull_full` |
| General finite-partial plus restricted-infinite admission | `propertyClass_trace_iff`, `propertyClass_lower`, `propertyClass_hull_full`, `propertyClass_not_refutable`, `propertyClass_not_scottClosed` |
| W5, recurrence class in the actual ideal carrier | `recurrence_ideal_not_refutable`, `recurrence_ideal_hull_full` |
| W6, countably represented infinite traces in the actual ideal carrier | `represented_ideal_not_refutable`, `represented_ideal_hull_full` |
| Dead ends and closed infinite languages | `bounded_language_boundary_empty`, `prefixLanguage_lower`, `boundary_prefixLanguage_iff`, `closed_language_boundary` |

The explicit lower-subtype maps from `IdealWarrant` identify ideals of H with ambient word ideals contained in H. The finite/infinite representation is proved both injective and surjective, and `history_order_iff` preserves and reflects inclusion. This is the content of the claimed order isomorphism, without hiding the classification in a chosen definition of “ideal.” No finiteness assumption is made about the alphabet.

`PropertyClass K` admits all finite partial words and exactly the infinite traces satisfying the independently supplied property K. This convention is the one used in W4–W6. It is not the same carrier as the infinite-only trace property K. The import from `PrefixSafety` supplies the explicit recurrence violation and the diagonal trace absent from any countable output enumeration. The latter's application to computable sequences retains that module's specified finite-program representation and output interpretation. No theorem equates all infinite traces with effectively realizable ones.

Every named theorem receives a `#print axioms` audit. Compilation reports only Lean's standard `propext`, `Classical.choice`, and `Quot.sound`, with no custom axioms, admitted goals, proof placeholders or `native_decide`. The unbounded trace assembly uses classical choice and does not supply an executable method for discovering an arbitrary ideal's letters. The aggregate checker should compile the two imports into an isolated build directory, then compile this module with that directory in `LEAN_PATH`, preserving source hashes and audit output.

These results specify what a finite preservation requirement can guarantee and the global requirements it can erase. They support the normative-priority investigation by preventing preservation or closure from being mistaken for a justification of the admitted ethical target. Such justification remains a substantive argument about relationships within the unfolding, not a theorem silently imported through the property K.
