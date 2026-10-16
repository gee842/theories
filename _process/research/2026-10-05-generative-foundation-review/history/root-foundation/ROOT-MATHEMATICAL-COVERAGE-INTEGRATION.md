# Admission and mathematical coverage: finite completion and generic named theories

7 October 2026, Asia/Bangkok. AI-authored integration following [Ren's instruction to finish items 1 and 2](../../../../sources/15-codex-theory-conversations/2026-10-07-mathematical-admission-and-coverage.md): full-domain admission from the root and coverage across mathematics. This round advances both, without declaring their universal form complete.

**Two specific gaps are now closed.** On a supplied finite carrier, one target-independent finite construction covers every predicate; empty, singleton and binary-union formation suffice for full admission. This extends through every finite function/predicate type over a finite base. Separately, the higher-order reconstruction now supports arbitrary typed named signatures and preserves whole theories, satisfiability and semantic consequence over the declared model classes.

The [formal package](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/coverage/README.md) passes a fresh Lean 4.29.1 build: **36 new theorems and 66 declaration audits**. The [proof correspondence](ROOT-MATHEMATICAL-COVERAGE-LEAN.md) states the exact hypotheses; the [critical review and source assessment](ROOT-MATHEMATICAL-COVERAGE-REVIEW.md) tests the affirmative interpretation. This round was implemented and reviewed by the same agent, without independent-agent review.

**有限载体上，可以用一个不依赖目标谓词的有限生成过程覆盖全部谓词；空集、单点和二元并的准入即可推出完整准入。这一结果延伸到有限基底上每个有限层级的函数／谓词类型。任意命名的类型化理论也获得语义保持。但无限域的根基准入，以及从根基覆盖全部数学，仍未因此完成。**

## 1. The common finite-family warrant

The [preceding reassessment](ROOT-MATHEMATICAL-FAMILY-WARRANT-REASSESSMENT.md) corrected an overly restrictive demand: a universal explanation may warrant a whole family collectively, without supplying a separate finite recipe for each member. The new finite construction realizes that collective approach at a precise scope.

Given a finite list covering a carrier, `selections` recursively keeps each existing selection both without and with the next element. It does not take an arbitrary predicate as input. `finite_domain_family_complete` proves that this one generated family represents every predicate on the carrier. Repeated entries are harmless; the claim is coverage, not a duplicate-free or efficient enumeration.

`full_of_finite_formation` then derives full predicate admission from admission of the empty predicate and every singleton, together with binary-union closure. At this scope, arbitrary directed completion is no longer an additional premise. `directed_closure_of_finite` derives it instead.

The affirmative explanation is relative but substantive: once the carrier's distinctions and finite combination are warranted, the entire finite predicate domain is accounted for by that formation. It does not leave one unexplained membership selection per predicate. The finite carrier, the formation operations and classical extensional interpretation remain commitments; the theorem does not derive them from an assumption-free root.

## 2. Extension through every finite type over that base

The proof goes beyond predicates on the initial base. The predicate carrier itself has a finite cover from the selection family. For two finite carriers, a finite assignment construction covers every function between them, with empty-domain and empty-codomain cases included.

These results compose through the existing `base`/`arr`/`pred` grammar. Every type of finite construction depth over a finite base remains finite. At each carrier, the three finite-formation conditions therefore suffice for full predicate admission. The earlier graph/ideal correspondence carries these finite-cover and admission results into the completed presentation as well.

This is an unbounded schema over finite type expressions, not one internal type containing all levels. It does not establish full admission on arbitrary infinite bases. The checked `nat_not_finite` prevents applying the finite-carrier premise to the natural numbers; the earlier arbitrary-chain/fullness result remains the relevant boundary there.

## 3. Named mathematical content and entire theories

The previous higher-order syntax could carry operations as free parameters, but had no generic named-signature theorem. The new module adds symbols at arbitrary declared types. An interpretation can name base elements, curried functions, predicates and higher-type values. It retains lambda abstraction, application, typed equality, predicate membership and quantification at every represented type.

The hypothesis `Compatible` requires the named values to correspond under the concrete type maps. Formula truth is not a premise. The new term, formula and sentence theorems derive its preservation and reflection. A separate comprehension theorem represents each named formula's extension as an ideal under the supplied full predicate interpretation.

`theory_transport` applies to an arbitrary collection of sentences, not just a finite example. `entailment_transport` and `satisfiability_transport` also cover all direct and completed interpretations over bases in the stated metatheoretic universe. The backward interpretation matters: the result is not restricted to a conveniently chosen forward image of models.

This completes the named-theory representational extension for the declared language. It does not establish a proof calculus's completeness, an algorithm for higher-order truth, or a model for every theory. The model class includes an empty base where the signature admits an interpretation; no silent change of model class is made between the two presentations.

## 4. Concrete correspondence and counterreview

The supplied natural-number interpretation names zero and addition. Lean checks the universally quantified addition-associativity sentence and its truth in the graph/ideal presentation. This demonstrates application to named mathematics, while leaving the natural numbers and their addition as inputs to that particular model.

A second checked example makes two symbols equal in one Boolean interpretation and distinct in the other. Their equality sentence then changes truth. This shows why symbol correspondence cannot be omitted. It changes the subject's interpreted relation and is not a full-target counterexample to the nondual theory.

The stronger structural comparator retains the finite constructions, arbitrary named interpretations and all established truth preservation. It can accept their local relational explanation while disputing that the same work justifies every infinite domain from the root. It also owes a warrant for its own infinite-domain commitments. The comparison preserves the target rather than freely changing a grounding label or weakening the rival's mathematics.

All these distinctions concern roles and explanations within one generative account. A supplied semantic carrier is not thereby outside reality. A missing connection in this formalization is not automatically a substantive failure of the richer theory. Here the demonstrated improvement is finite admission and broader conditional semantic coverage; the unproved connection remains independent infinite-domain warrant.

## 5. Exact status of the requested items

| Requested obligation | Newly established | Still required for its universal form |
| --- | --- | --- |
| 1. Full-domain admission from the root | Full admission follows from finite formation on a supplied finite carrier, and at every declared finite type over a finite base. A common finite family is explicitly constructed. | Independently warrant infinite bases and the full predicate/function ranges needed over them. The finite formation premises also remain relative to their justification in the root. |
| 2. Coverage across mathematics | Arbitrary named theories in the declared finite simple-type language preserve truth, comprehension, theory satisfaction, satisfiability and semantic consequence under the concrete correspondence. | Establish a faithful foundation-wide account beyond this grammar and its supplied base domains, with the source/target admission commitments justified. |

The generic signature theorem prevents named operations from remaining an open representational objection in this language. A further isolated named example would not solve the universal coverage problem. Dependent types, internal universes, and a proof that every intended mathematical subject is represented with independently warranted domains are not part of this package.

Consequently the two universal obligations remain unfinished. The advance is that their finite and named-theory subproblems now have exact, checked resolutions. No assumption of full infinite admission has been relabeled as a derivation.

## 6. Evidence, verification and preservation

The [review](ROOT-MATHEMATICAL-COVERAGE-REVIEW.md) reuses the earlier primary assessments of full/general semantics and explicit formation commitments. No new external retrieval or source import was needed, and earlier readings are not counted as independent evidence again. The new evidence consists of the mathematical sources and the fresh Lean run; no empirical or mathematical novelty claim is made.

The [proof receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/coverage/verification.json) binds the frozen source, inherited sources and receipts, audit driver and logs. `FiniteAdmission` contributes **23 theorems / 27 audits**; `SignatureTruth` contributes **13 / 39**. Only `propext`, `Quot.sound` and `Classical.choice` occur. There are no custom axioms or proof holes. The six inherited modules were rebuilt but not counted as new.

The [document receipt](ROOT-MATHEMATICAL-COVERAGE-CHECKS.json) separately validates owned links, proof bindings and preservation of 70 earlier proof assets. Unrelated concurrent edits were retained and no commits were made. The earlier admission, assembly and stopping assessments retain their original scopes; this new round supersedes only the finite-domain and named-signature omissions it actually closes.
