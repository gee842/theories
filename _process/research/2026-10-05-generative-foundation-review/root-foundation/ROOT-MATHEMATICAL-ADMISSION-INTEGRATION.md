# Full admission: exact completion strength and a common graph representation

7 October 2026, Asia/Bangkok. AI-authored integration of [Ren's continuation](../../../../sources/15-codex-theory-conversations/2026-10-07-continue-mathematical-admission.md) after the [completed conditional higher-order reconstruction](ROOT-MATHEMATICAL-HIGHER-ORDER-INTEGRATION.md).

**This round establishes an exact admission equivalence and extends the reconstruction to function graphs.** Finite admission plus closure under every ambient nonempty directed union is equivalent to full predicate admission. A proper finite/cofinite range passes all the displayed finite-pattern, finite Boolean and renaming tests while failing that closure. Predicates and arrows can now both be represented through relation ideals at every finite type of the declared language, preserving all its formulas. A fresh Lean 4.29.1 build passes **52 new named theorems and 86 declaration audits**.

The independent warrant for full admission remains unresolved. The strongest affirmative argument does not derive its all-family range from the root's weaker formation content. The next universal inference must justify that range or resolve its explanatory dependence against a matched full-target account. Merely changing its representation will not finish that inference.

Read the [affirmative admission argument](ROOT-MATHEMATICAL-ADMISSION-ARGUMENT.md), [counterreview](ROOT-MATHEMATICAL-ADMISSION-REVIEW.md), [primary-source assessment](ROOT-MATHEMATICAL-ADMISSION-SOURCES.md), [admission correspondence](ROOT-MATHEMATICAL-ADMISSION-LEAN.md) and [function-graph correspondence](ROOT-MATHEMATICAL-ADMISSION-FUNCTIONS.md). The [formal package](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/admission/README.md) gives reproduction instructions and exact source scope.

**有限区分、有限布尔组合、任意重命名下的不变性，以及对每个有限成员模式的覆盖，仍不足以推出全部谓词的准入。加入“形式化所量化的所有非空有向族的并均准入”，才得到本轮检验的完整等价。函数也可以通过有限关系图的完备化重构，但所有理想与处处有值的条件仍需说明其根据。**

## 1. The completion premise is now exact

For a supplied carrier and predicate admission condition `C`, `full_iff_finite_directed` proves equivalence between full admission and the conjunction of finite admission with unrestricted nonempty directed-union closure. With finite admission fixed, `directed_iff_full_given_finite` isolates the remaining closure condition.

The proof exposes the relevant step. Given an arbitrary target predicate `S`, `FiniteProfiles S` selects all finite predicates contained in it. This is a nonempty directed family, every member satisfies finite admission, and its union equals `S`. Fullness follows when closure applies to that entire family.

The family range is not a range of computable, named or otherwise independently generated families. It ranges over every ambient family of predicates. The equivalence is therefore both constructive and diagnostic: an independently warranted all-family closure would give full admission; the proof does not make that warrant disappear. Selecting the entire family of finite parts of `S` already refers to `S` at the family-selection level. The argument is mathematically valid, while the foundational reduction still has to explain that range.

This migrates and refines the earlier [closure results P2/P3](MATHEMATICS-CLOSURE-RESOLUTION.md#proposition-p2--which-union-closure-yields-all-subsets), previously preserved as hand arguments. It is not a claim to have discovered the distinction between finite and full formation for the first time.

## 2. A stronger test of the proposed warrant

The proper comparison family consists of finite or cofinite predicates: either the included elements or the excluded elements have a finite-list witness. The new Lean module proves that this family admits every finite predicate, the empty and total predicates, and singletons; it is closed under complement and binary union. Admission is preserved and reflected by arbitrary supplied bijections.

It also realizes every finite membership pattern: for any target predicate and any finite list of arguments, some admitted predicate agrees on that list. This is an exact finite-pattern result, not agreement on every sentence or every possible observation.

On the natural numbers, the even predicate belongs to neither the finite nor the cofinite class. The module proves its exclusion and gives the directed family of its finite parts as an explicit closure failure. Consequently the displayed finite formation, extensionality and renaming conditions do not force full admission. The missing principle cannot be justified merely by saying that no element or label should be privileged.

The comparison tests those weaker conditions. It is not a model of full comprehension, an adequate replacement for the independently fixed full predicate subject, or a counterexample to a richer root that actually warrants completion. The broader foundational comparison retains the full subject on both sides.

## 3. Functions now share the completion representation

The previous typed reconstruction used ideal completion for predicates and ordinary full function carriers for arrows. The new graph module represents arrows by ideals of finite relations that are functional and total. It proves that functionality of the union is equivalent to functionality of each finite member. Totality separately requires each input to appear with some output in a member; the empty functional ideal shows why compatibility alone does not establish this condition on an inhabited input carrier.

The concrete encoding takes all finite parts of a function's graph. Decoding uses the uniquely determined value supplied by totality. Both inverse laws are checked. The decoder uses classical choice and is not an algorithm for recovering arbitrary functions from finite observations.

`GraphCompleted` applies this construction recursively through the earlier finite `base`/`arr`/`pred` type grammar. Predicates become finite-subset ideals; arrows become total functional finite-graph ideals. Term transport covers lambda abstraction and application. `graph_formula_transport` and `graph_sentence_transport` preserve every formula and closed sentence of the declared language, including quantification at every represented type. This closes the earlier representational limitation at arrow types.

Two checked connections retain the admission accounting. First, finite admission and unrestricted directed-union closure on a product carrier admit every function graph. Second, for one predicate-domain condition, admission of the true fibers of every Boolean-valued function is equivalent to full predicate admission. The second statement does not postulate an independent function-admission family or infer fiber closure from an unspecified function repertoire.

The completed presentation now has a common ideal framework for predicates and arrows. The direct interpretation still uses ambient full functions; the completed interpretation admits all qualifying relation ideals and global totality. The result reduces presentation resources without claiming to derive their universal availability from finite generation alone.

## 4. What the affirmative attempt establishes

The [argument](ROOT-MATHEMATICAL-ADMISSION-ARGUMENT.md) reconstructs a positive chain: finite distinctions specify membership, extensional identity removes duplicate descriptions, renaming neutrality removes privileged labels, and compatible completion presents the entire relation. This earns a substantive account of admitted content. A total functional ideal leaves no additional output unspecified; a predicate ideal leaves no additional membership unspecified.

The step from this exhaustiveness to admitting every complete profile remains unproved. The finite/cofinite comparison defeats one proposed inference to that step. Maximality or no-arbitrary-exclusion can require fidelity to an independently justified full subject, but cannot yet establish the full subject from weaker formation conditions. Explanatory openness is a reason to investigate an extension; it is not by itself a general existence principle.

A matched structural account can accept the same full predicate domains, function graphs, concrete maps and higher-type truths while disputing their proposed ultimate dependence. It also owes a warrant for full admission. Its survival here does not show that it is a completed alternative foundation. It does show that mathematical correspondence alone has not resolved the shared explanatory question.

The [focused Feferman reading](ROOT-MATHEMATICAL-ADMISSION-SOURCES.md) supplies a useful comparison about which starting concepts, operations and totalities an unfolding accepts. It is not adopted as Ren's foundation, used to equate predicativity with finite/cofinite admission, or treated as a proof that full mathematics is illegitimate. Source interpretation and the new Lean statements have separate evidential roles.

These distinctions remain within one generative account. A supplied law or full range is not thereby external to reality. The unresolved explanation concerns its derivation within the reconstructed theory; no separate realm or independent meaning-giver is assumed.

## 5. Current result and stopping condition for this argument

The reconstruction programme has advanced: the declared finite higher-type semantics can now represent both predicates and functions through completed finite relations. The admission audit has also advanced: the desired full range is exactly characterized by the stated closure, and a stronger finite/symmetry comparison survives the weaker proposed warrant.

No new independently justified full-admission premise or exclusive constitutive priority has been established. Repeating “no privileged exclusion,” “all compatible profiles,” or the same complete representation does not supply the missing inference. The next universal result must explain which whole families the root admits and why, including their completion and the total graph families at the required levels, or establish an explanatory reduction/equivalence against the matched rival.

This stops the repeated argument, not the universal project. It preserves the possibility that an infinitary admission principle can receive an independent generative justification; no theorem here rules that out.

## 6. Verification and preservation

The [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/admission/verification.json) records a fresh frozen-source build in an isolated directory. `Admission.lean` contributes **34 named theorems and 50 audits**; `FunctionGraphs.lean` contributes **18 theorems and 36 audits**. The only reported axioms are `propext`, `Quot.sound` and `Classical.choice`; there are no custom axioms, proof holes or unsafe bypasses. Four inherited source modules were freshly rebuilt after their prior receipt hashes were matched; inherited results are not counted as new.

Root and the collaborating reviewer read both final modules. The review independently matched all recorded new/inherited source, prior-receipt and support-file hashes. This is internal collaborating-AI review, not external peer review or empirical validation. The [document receipt](ROOT-MATHEMATICAL-ADMISSION-CHECKS.json) separately checks links, receipt bindings and preservation of earlier proof assets. No source bytes were imported from the external reading and no claim of mathematical priority is made.
