# Indexed finite assembly: explicit parity and the strength of all chains

7 October 2026, Asia/Bangkok. AI-authored correspondence record for [IndexedAssembly.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/assembly/formal/IndexedAssembly.lean), namespace `IndexedAssembly`. The module contains **19 named theorems and 26 explicitly named declarations**. The combined package's fresh Lean 4.29.1 build passed with **31 new theorems and 48 declaration audits**, including the separate `RelationalAssembly.lean` development. Inherited admission and completion dependencies were freshly rebuilt; only `propext`, `Classical.choice` and `Quot.sound` occur as logical dependencies. The final source bindings are recorded in its [verification receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/assembly/verification.json).

This is a checked continuation of the [admission result](ROOT-MATHEMATICAL-ADMISSION-LEAN.md). The unrestricted sequence argument migrates and refines the earlier [closure study's P2](MATHEMATICS-CLOSURE-RESOLUTION.md) and [finite-prefix analysis](MATHEMATICAL-ADMISSIBILITY-MATH.md). It is not presented as a new mathematical discovery or an independent proof of generative admission.

## 1. The precise chain interface

`FiniteChain A` consists of a sequence `Nat → FinitePart A` and a proof that later stages include earlier ones. `ChainUnion T a` means that `a` belongs to some stage. `FiniteChainClosed C` requires admission of this union for **every ambient finite chain** whose stages are admitted by `C`.

`ChainFamily` turns such a sequence into the family of its stage predicates. `chainFamily_directed` proves that it is nonempty and directed, using the larger of two stage indices as a common upper bound. `union_chainFamily` identifies its union with `ChainUnion`. Hence `directed_implies_chain_closed` derives this sequence closure from the earlier arbitrary directed-union principle, on any supplied carrier.

The definition does not restrict chains to effective, definable or independently generated sequences. Natural-number indexing limits the index type; it does not by itself limit which sequence is supplied.

## 2. An actual recurrence independent of a target predicate

`parityStages` starts with the empty finite part and follows the recursion

\[
E_0=\varnothing,\qquad E_{n+1}=E_n\cup\{2n\}.
\]

The definition takes only the stage index. It has no parameter for an arbitrary target predicate and does not ask whether an element belongs to such a predicate. `parity_zero` and `parity_successor` expose the initial and successor clauses.

| Declaration | Exact result |
| --- | --- |
| `parity_stage_membership` | Membership at stage `n` is exactly `∃ k < n, a = 2*k`. |
| `parity_stages_finite` | Each stage has a finite-list witness. |
| `parity_stages_increasing` | Stages are inclusion-monotone. |
| `parity_union` | The union is exactly the existing predicate `Even a`, defined by `a % 2 = 0`. |
| `finiteOrCofinite_parity_stages` | The earlier finite-or-cofinite comparison admits every stage. |
| `finiteOrCofinite_parity_union_excluded` | That comparison rejects their union. |

This strengthens the preceding calibration. The missing parity completion can be presented through one explicit recurrence, rather than only through a family selected by first supplying the full target predicate. It remains a mathematical construction within supplied natural-number arithmetic and union semantics. It does not prove that any physically instantiated history runs through all natural-number stages.

The theorem `parity_admitted` has a deliberately broader hypothesis: finite admission plus **global** `FiniteChainClosed`. It is not a proof of parity admission from a weaker rule restricted to this particular recurrence. The bounded positive result here is the recurrence and exact union. A warrant for admitting that union must be argued separately or expressed through the companion local assembly interface.

That companion interface concerns admission of output-valued presentations under explicit whole-witness and abstraction hypotheses. It does not automatically establish a separate predicate-admission assertion `C (ChainUnion T)` without a correspondence between those two admission notions.

## 3. Why unrestricted countable indexing still commits to fullness

For an arbitrary `S : Nat → Prop`, `prefixChain S` uses the inherited `boundedPart S n`, whose membership is exactly `S a ∧ a < n`. This definition is explicitly noncomputable at the generality of arbitrary `S`; the finite-list witness uses the supplied predicate. It must not be confused with the independent parity recursion.

`prefix_stage_membership` exposes that dependence. `prefix_union` proves that the union of these prefixes is `S`. Applying global finite-chain closure therefore yields:

| Declaration | Exact result on `Nat` |
| --- | --- |
| `full_of_finite_chain` | Finite admission and closure under every finite chain imply full predicate admission. |
| `full_iff_finite_chain` | Those two conditions together are equivalent to full admission. |
| `chain_iff_full_given_finite` | Given finite admission, unrestricted finite-chain closure is equivalent to fullness. |
| `chain_iff_directed_given_finite` | Under that same premise, it is equivalent to the earlier unrestricted directed-union closure. |

The converse directions are also checked. These equivalences are stated for the actual natural-number carrier, not asserted here for arbitrary uncountable carriers. Every individual chain has countably many stages, but the closure rule quantifies over all chains available in the ambient metatheory. An arbitrary subset enters through its predicate-dependent prefix sequence. Thus the sequence formulation does not independently explain the full family range.

`finiteOrCofinite_not_chain_closed` gives the explicit countercase to this closure principle using the parity recurrence itself. It preserves the finite/cofinite family's established weaker properties; it does not claim that family is adequate for a target already requiring all chain completions.

## 4. What this contributes to the root question

The result distinguishes a concrete uniform construction from unrestricted availability of every indexed construction. It supports examining whether the root independently warrants whole relations generated by such specified rules and the operation that takes their union. It also blocks an unjustified inference from “the stages are naturally indexed” to “the admission obligation has become weaker than fullness on `Nat`.”

These are different relationships within the same investigation. A sequence or union represented in Lean is not thereby outside generative reality. Its being supplied identifies what this proof assumes; it does not settle how that content arises or why its completion is warranted within the whole.

The module provides no theorem that every mathematical subset has an effective generating sequence, no independent derivation of full admission, and no conclusion of exclusive metaphysical priority. Those stronger commitments remain the intended foundational questions rather than being replaced by this conditional equivalence.

## 5. Reproduction

From the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/assembly/check.py
```

The package checker freshly builds the inherited dependencies and new modules before auditing declarations. The receipt binds the exact source and support files. Automatically generated projections and recursors are kernel checked with the full source but not separately counted in the 26-declaration headline. No custom axioms, proof holes, unsafe declarations or `native_decide` are used. Earlier proof sources remain unchanged.
