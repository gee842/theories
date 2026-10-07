# Collective induction: the exact arithmetic commitment

Integrated 8 October 2026, Asia/Bangkok; continuation begun 7 October. AI-authored response to [Ren's mathematical admission and coverage instruction](../../../../sources/15-codex-theory-conversations/2026-10-07-mathematical-admission-and-coverage.md). Following the [dependent-family result](ROOT-MATHEMATICAL-FAMILIES-INTEGRATION.md), this round tests the proposed warrant for a collective inductive domain directly. The [affirmative argument](ROOT-MATHEMATICAL-INDUCTION-ARGUMENT.md) and [independent internal review](ROOT-MATHEMATICAL-INDUCTION-REVIEW.md) distinguish a valid induction inference from justification of its subject.

**The arithmetic premise is now narrower and exact.** Induction over selected predicates can establish that every element is generated, provided the selection admits the generated-orbit predicate. Full predicate admission is not required by that inference. Separately, exhaustive generation and constructor separation together characterize the universal recursion property on a supplied carrier. Neither result independently warrants the carrier's collective existence.

The [formal package](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/induction/README.md) passes a fresh Lean 4.29.1 build: **28 new theorems and 47 declaration audits**. These are standard mathematical mechanisms formalized for this premise investigation, with no novelty or universal-grounding claim.

**本轮把算术的前提进一步缩小并说清：只要所选谓词中包含“由起点反复生成”的谓词，所选范围上的归纳就足以检验是否还有未生成的元素；这一步不要求先准入全部谓词。穷尽生成与构造身份保持，又恰好对应所述递归普遍性质。但整体归纳域本身为何获得根据，仍未由这些等价式证明。**

## 1. The positive argument and its limit

The affirmative account explains induction through **exhaustive formation**: if every member of the intended subject has a finite derivation from the declared seed and constructor, then a property preserved through those formations covers every member. This concerns possible finite derivation, not a claim that every mathematical member has actually been physically produced.

The interpretation has explanatory content. A common formation rule connects the instances and gives a reason to use the same induction rule throughout the subject. It does not require a separate truth answer for each target predicate. Formation identity also explains why a question about iteration counts retains distinctions that a description of recurring endpoints can forget.

The remaining commitment is the admission of **all such finite forms as one domain**, with their identities and intended quantification. Defining the subject that way states the proposal; it does not show that the minimal root independently warrants the proposal. The current root already uses natural numbers, induction and finite-history construction as mathematical resources. Their successful applications cannot discharge those resources' own warrant.

These are explanatory roles within one unfolding. A supplied carrier in the formal proof is not declared to exist outside generative reality. The unresolved connection is why the proposed whole has this admitted collective organization, rather than a supposed ontological separation between mathematics and formation.

## 2. What the induction theorem actually requires

Fix a supplied carrier `A`, a seed `z`, and an operation `s : A → A`. The source defines `iterate z s n` by Lean's natural-number recursion and `Generated z s a` by existence of an iteration index reaching `a`. `NoJunk` means that every element belongs to this generated orbit. `Closed P` means that `P` contains the seed and is preserved by `s`.

`generated_closed` and `generated_least` establish the orbit's closure and leastness. `fullInduction_iff_noJunk` then identifies induction over all ambient predicates with `NoJunk`.

The more informative result is `selected_iff_noJunk`. Its **explicit hypothesis** is `C (Generated z s)`. Under that hypothesis, induction over predicates selected by `C` is equivalent to `NoJunk`. Admission of the orbit predicate is not silently derived from an arbitrary selection rule. The orbit is specified using the given constructors, rather than selected using each target predicate's answers, but its entire natural-number iteration range remains supplied by the metatheory.

The checked `OnlyGenerated` example on `Nat` satisfies the selected induction condition and excludes the constantly false predicate. It is an intentionally thin selection, not a proposed higher-order model or a range closed under the logical operations. It demonstrates that the displayed inference does not require every predicate to be selected; it does not offer an independently justified replacement for full higher-order semantics.

In particular, a metatheoretic statement applying induction to arbitrary predicates must not be confused with admitting a full predicate sort inside an object-language. The latter remains the separate obligation studied in the admission and family packages.

## 3. Identity, reconstruction and universal recursion

`Separated` adds two conditions: successor preserves distinct inputs, and a successor value never equals the seed. With `NoJunk`, `naturalEquivalence` supplies inverse maps between `Nat` and the carrier, preserving zero and successor. The inverse chooses a generation index; its dependence on classical choice is recorded. `unique_recursion` constructs the unique map into any supplied seeded successor structure that preserves those operations.

The second module asks whether taking this universal role as the starting point avoids the commitment. `Initial` quantifies over seeded successor carriers in the **same metatheoretic universe**. `initial_iff_generated_separated` proves exactly:

`Initial z s ↔ NoJunk z s ∧ Separated z s`.

The reverse analysis makes its comparison range concrete. A map into the generated subtype, compared with the identity map, establishes exhaustive generation. A map into universe-lifted `Nat` supplies the numerical interpretation used with that coverage to establish separation. These targets are explicit resources. The characterization does not assert that the universal role has an instance without an admitted domain and metatheory.

Two checked comparisons keep the conditions distinct. Boolean toggling generates its two-element carrier and supports the displayed induction rule, but violates separation because a successor returns to the seed. `Option Nat`, with `none` fixed and successor acting normally on `some n`, satisfies separation while retaining an element outside the seed's orbit. These test weaker premise sets; neither is a matched rival preserving ordinary arithmetic's full intended subject.

## 4. Primary-source comparison

The new primary reading is Dedekind's *The Nature and Meaning of Numbers*, in Beman's authorized translation collected in [*Essays on the Theory of Numbers*](https://sgslogic.net/t20/courses/math140/dedekind-book.pdf): §§44, 66, 71–73, 80, 126 and 130 (PDF pp. 33, 36, 38–39, 48–50). He separately discusses infinite-system existence, chain formation, the simply infinite structure, induction and recursive definition. His existence argument appeals to a totality of possible thought-objects and a proper injective self-map; his chain definition uses an intersection. His cyclic example distinguishes induction along a generated chain from unrestricted recursive interpretation.

Our assessment is that these are a useful structural comparator and a warning to audit collective existence separately. The thought-totality argument is not adopted as an established psychological or metaphysical proof. Our Lean receipt validates only the new stated theorems, not every result in that book. The [Gutenberg original delivery](https://www.gutenberg.org/files/21016/21016-pdf.pdf) intermittently timed out; the matching primary text was inspected through the linked mirror. No source bytes were imported.

## 5. What changed in the research conclusion

The affirmative argument now has a checked implication: exhaustive finite formation warrants the corresponding induction inference. The precise selected-predicate result also narrows the arithmetic dependency. It would overstate the remaining obstacle to say that this arithmetic step must first justify every predicate family.

The review accepts this improvement while retaining a matched structural account that preserves the same domain, constructors, generation, identity and mathematical consequences. Such an account can understand the domain through the structural meaning of finite iteration within the same whole. Its availability does not prove it correct; it prevents the new characterization from settling exclusive root priority by itself.

The remaining first warrant is therefore specific: why are arbitrary finite formations admitted as one exhaustive, identity-preserving domain available to collective quantification? This round supplies a subject-relative philosophical rationale but does not derive that entitlement from independently warranted weaker content. Initiality is now an exact characterization of the commitment, not a way to make it disappear.

This closes the proposed induction/universal-property test. Repeating its equivalences would not advance independent admission. A further foundational advance needs a defended collective-formation principle or a substantive comparison showing that adequate alternative explanations express the same constitutive dependence. Full predicate ranges and universal mathematical coverage remain additional obligations even if this arithmetic domain is warranted.

## 6. Proof correspondence and preservation

| Module | New theorems / audits | Established scope |
| --- | --- | --- |
| [InductiveDomain.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/induction/formal/InductiveDomain.lean) | 24 / 38 | Full/selected induction and generated coverage; separated iteration; natural-number correspondence and unique recursion; precise boundary examples. |
| [Initiality.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/induction/formal/Initiality.lean) | 4 / 9 | Same-universe initiality equivalent to coverage plus separation, with explicit generated-subtype and lifted-natural-number targets. |

The [fresh receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/induction/verification.json) binds both frozen sources and all audit assets. Only bundled `Std` is imported beyond the first new module. The build and audit reject warnings, holes and custom axioms. The package uses only `propext`, `Classical.choice` and `Quot.sound`; 34 named declarations have empty printed axiom lists. Those empty lists **do not eliminate Lean's types, inductive naturals, recursors or logical foundation**.

The older general presentation and initiality notes retain their original hand-proof status. This package checks the zero/successor case and does not retroactively certify those general notes. The [document receipt](ROOT-MATHEMATICAL-INDUCTION-CHECKS.json) separately checks links, current proof bindings and preservation of 101 prior proof assets. Shared-file updates are additive; unrelated concurrent work is retained. No commits or repository-wide retrospective audit were made.
