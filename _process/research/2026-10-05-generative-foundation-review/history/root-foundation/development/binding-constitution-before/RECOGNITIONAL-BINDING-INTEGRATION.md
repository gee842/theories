# 指回关系与同一规则 / Binding and the identity rule

2026-10-08，Asia/Bangkok。本轮接续 Ren 的[无前提元逻辑方向及最新“继续”](../../../../sources/15-codex-theory-conversations/2026-10-08-generative-logic-investigation.md#recognitional-continuation)。候选解释、形式化及作者反审为 AI 工作。[当前理论第14节](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATED-LOGIC.md#recognitional-binding)。

**推进：把“辨认同一”分成有不同根据的任务。** 同一论证中直接指回已引入的根据，可以由引入与使用的绑定关系构成；它不必先被描述成两个独立对象之间的经验比对。新的形式检查也不止验证一个恒等函数：在给定的有限推理语言中，无额外来源、无周围假设的原子型 `A → A` 项必定返回所给根据。新增7项定理，连同14项继承声明共21项审计，命名公理报告均为空。

**Status:** a scoped constitutive explanation, accompanied by a standard logical-relations uniqueness argument. The syntax already contains context use and its interpretation. The new result does **not** derive that interpretation, all semantic recognition or Lean's metatheory without premises. The philosophical grounding remains unfinished, without an impossibility verdict.

## 1. The exact connection advanced

The [previous identity study](REFLECTIVE-IDENTITY-INTEGRATION.md) left content/ground recognition open. The [earlier inference study](GROUNDING-INFERENCE-AND-PRESENTATION.md), especially §§11 and 15, already derived transport from atomic correspondences and examined operation-relative identity. Those results are credited here. In particular, its paired-representation construction already exhibits a correspondence; we do not claim to discover that possibility again.

This continuation tests a narrower transition: **displayed introduction-and-use relation → retention through every term in a specified source-free fragment → preservation of the same assessment requirement**. It removes the earlier transport theorem's independent source-link premise only where no source constructor occurs. It adds uniqueness for all closed atomic endomorphism terms, rather than selecting a convenient identity implementation.

The differentiated roles—introduction, use, context position and assessed content—belong to one displayed inferential activity. The representation preserves their binding and evaluation relations. It omits physical persistence, time, perception and the adequacy of representing actual judging this way. These omissions are not independent ontological realms, and their absence alone is not a refutation of the fuller proposal.

## 2. Positive constitutive argument

Consider: “let this ground be g; now use g for the very requirement under which it was introduced.” The later use can be constituted as a reference to that introduction. The account need not first posit two independently encountered grounds, then demand another certificate that they match. The act's referential organization is a candidate source of the sameness at issue.

The warrant claimed is restricted: the use introduces no new ground and makes no stronger assessment claim. If the given ground meets a requirement, this re-presentation preserves it. This is not an unconditional assertion that any particular proposition is true. Nor is mere repetition of a sound or mark sufficient: a binding relation must actually be exhibited, and an attempted use can misidentify its introduction.

中文例子：在“假定这里给出的根据为 g；仍凭 g 回答同一个要求”中，后一个 g 的角色由它指回哪次引入确定。我们据此区分**构成共同指向**与**重新辨认某个独立遇到的对象**。后者可能需要感知、记忆和校准；不能由前者自动获得。这个区别使研究不必为每一次指回另设一个独立裁判，但也不把所有看似正确的指回当作已经正确。

## 3. Formal contract and actual proof

[RecognitionalBinding.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/RecognitionalBinding.lean) imports the existing `InferentialGrounds` and `GroundRelationTransport`. Forms are atomic labels, products and arrows. Finite terms can use a typed context position, pair/project, abstract/apply, or introduce a supplied atomic ground. `SourceFree` excludes only the last constructor, recursively; it contains no predicate meaning “valid” or “correct.”

The semantic clauses are supplied openly. Context use returns the value at its bound position; abstraction extends that context; application applies the interpreted function. The language has no atomic inspection, general recursion, divergence or effects. Types, equality, induction and those clauses remain the metatheoretical contract.

| Checked declaration | Exact contribution |
|---|---|
| `source_free_related` | Every source-free term preserves any specified family of binary ground relations when its two context assignments are related. Proved by induction on the actual term, rather than assuming parametricity of its result. |
| `no_closed_source_free_atom` | There is no source-free closed term of atomic form, even if its carrier happens to have values. Use the everywhere-false relation; it must hold of the supposed result. |
| `closed_identity_forced` | For every carrier G, atomic index i, closed source-free term of `atom i → atom i` interpreted with G at each atomic index, and g:G, evaluation at g equals g. |
| `closed_identity_preserves` | Any criterion on G satisfied by g also holds of that output, using the preceding equality. No criterion is thereby established for g. |
| `bound_identity_spec` | The explicit term that abstracts and uses its newest bound position is source-free and returns its argument, for any atomic carrier family. This shows the uniqueness result has inhabitants. |
| `ambient_ground_can_replace` | Without a source constant, an additional context ground can still be returned instead of the argument. |
| `introduced_ground_can_replace` | With empty ambient context, an introduced source constant can still be returned instead of the argument. |

For the uniqueness proof, fix an arbitrary g:G and use the relation `R i x y := x = g`. The term's relation-preservation theorem applies to empty contexts; supplying g on both sides yields `eval(term)(g) = g`. No separate assumption that this particular function preserves all relations is made. It was derived from the supplied grammar and evaluation.

This is an **atomic-type** result. “Every A → A term is identity” without that qualification is not the checked statement: a compound type can expose structure the language can manipulate. It is also not a System F formalization, an equality-decision procedure, a normalization theorem, a running-time theorem or a statement about arbitrary programs of a host-language function type.

## 4. Rivals and failure boundaries

The two controls use the same evaluation rules as the positive result. With Bool as the ground carrier, the argument is false and the alternative ground is true. `ambientChoice` returns the existing surrounding true; `introducedChoice` returns the newly supplied true. These are Bool **values**, not judgments that falsehood becomes true.

They demonstrate why empty context and exclusion of sources both matter. They also give a substantive alternate account: an activity may select among several grounds while preserving the same input/output type. Merely displaying an arrow type or using the word “same” cannot certify retention of its particular input. A source-free but open term remains a perfectly meaningful construction; the exact target of sole-input retention distinguishes it from our closed fragment.

The earlier mixed-standard rival remains intact. Retaining the same value does not promote tentative support into established support. The previous Curry control also remains intact; no arbitrary self-certifying assertion is authorized by the binding argument.

## 5. Author counterreview

| Objection | Assessment |
|---|---|
| “The `use` clause has already encoded identity.” | Correct as a mathematical dependency. Its interpretation selects the bound ground. The theorem establishes closure and uniqueness given these clauses, not the absolute warrant of the clause itself. The philosophical proposal must explain that clause through the exhibited activity. |
| “Source-free secretly means correct.” | It only excludes a constructor. Arbitrary relation preservation is proved, while the grammar/evaluation and their correspondence remain explicit commitments. |
| “The all-terms theorem is vacuous.” | `bound_identity_spec` supplies a closed source-free inhabitant. By contrast, the atomic no-term result intentionally concerns a different type shape. |
| “Any attempt to dispute this has accepted all logic.” | Unsupported. Our controls and mixed standards describe intelligible alternative tasks. No performative shortcut yields classical logic or universal semantic agreement. |
| “A displayed link can be mistaken or misrepresented.” | Yes. A formal binding checks a representation. Its match to an actual act and whether the present demonstration adequately exhibits that match remain substantive obligations. Adding the label ‘self-present’ would not discharge them. |
| “A further certificate is always needed, so the project is impossible.” | That does not follow. Constitutive presentation is a candidate mode of warrant, not an endless hierarchy of independent certificates. Its adequacy still needs argument and testing. |
| “This is new logic at the frontier.” | No such claim is made. The mathematical method has established precedents; its role here is to sharpen the foundational proposal and expose its exact commitments. |

## 6. Primary-source assessment

Wadler's [author-maintained parametricity page](https://homepages.inf.ed.ac.uk/wadler/topics/parametricity.html) and [institutional record of *Theorems for free!* (1989)](https://www.research.ed.ac.uk/en/publications/theorems-for-free/) describe consequences of polymorphic types through Reynolds's abstraction theorem. Those abstracts were inspected. Our use of arbitrary logical relations is a standard methodological relative, with a much smaller supplied language. We do not claim to have re-proved the full polymorphic theorem. A course-hosted PDF had garbled text extraction; no unread full-text argument is attributed to it.

Martin-Löf's [*On the Meanings of the Logical Constants and the Justifications of the Logical Laws*](https://michaelt.github.io/martin-lof/Meanings-of-the-Logical-Constants-1983.pdf), lectures from 1983, published 1996, was inspected at PDF pp.1–3, 9–10 and 15–17 in the relevant passages. It distinguishes judging from what is judged, discusses proof as an act, and explains hypothetical proof through completion by proofs of its hypotheses. This is a substantive precedent for examining the inferential activity. Its own primitive explanations do not certify our stronger no-presuppositions target, and we do not import an independent mind/world division from its terminology.

## 7. What is complete, and the next unresolved bridge

**Locally complete:** the source-free transport and atomic endomorphism uniqueness checks, their two controls, and their integration with the constitutive candidate. Repeating an identity evaluation or redoing the earlier paired-source transport would not advance the next step.

**Still unresolved:** whether the actually exhibited introduction/use relation warrants its interpretation without an unexamined commitment, and how a warranted hypothetical construction permits substitution of an actual ground while preserving the relevant content and assessment. This must address a concrete attempted binding or substitution and a rival account of the same displayed act. It should not simply assume that every participation in inquiry validates our chosen grammar. The question concerns the warrant of the connection; an implementation test alone would answer a different question.

中文结论：本轮将“同一根据如何认出”的一部分改写为“共同指向如何在活动中构成”，并检验了给定形式语言中这个结构的普遍后果。仍不能把局部形式闭包等同于完整无前提元逻辑；后续中心是具体引入／指回及假设代入的根据。用逻辑考察逻辑本身，并未在这里被宣布为自动失败。

## 8. Verification and preservation

The [isolated Lean checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_recognitional_binding.py) compiled the three source snapshots. [The frozen successful receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/recognitional-binding-checks/20261008T120159.334011Z/receipt.json) records **7 new theorem audits plus 14 inherited declaration audits, all 21 with empty named-axiom reports**, without warnings or proof holes. The inherited 14 comprise 8 theorems and 2 supporting definitions in `InferentialGrounds`, plus 4 theorems in `GroundRelationTransport`; they are not 14 new theorems. The first compile failed on dependent indices and inference of the example's carrier; explicit binders repaired these typing errors without changing the intended statements.

An empty report concerns dependencies of the checked Lean declarations, not the absence of grammar, inference, evaluation or metatheory. There was no independent-agent review or empirical validation. [Before editions](development/recognitional-binding-before/manifest.json), [owned index edits](RECOGNITIONAL-BINDING-INDEX-EDITS.json) and [documentary checks](RECOGNITIONAL-BINDING-CHECKS.json) preserve the prior result and shared concurrent work. Only the owned F01 additions and read/authored source versions are maintained; the separate full-results catalogue and unrelated pending reviews are preserved.

<a id="binding-preserving-substitution"></a>

## 9. 接续：假设代入保留哪种关系 / Continuation: what substitution preserves

9 October 2026, Asia/Bangkok. Ren's [latest continuation](../../../../sources/15-codex-theory-conversations/2026-10-08-generative-logic-investigation.md#substitution-continuation) keeps the direct metalogical target. The present section supersedes only the mathematical substitution question in §7; the philosophical warrant remains under investigation.

**Result:** [binding-preserving-substitution](../../../../theories/shengsheng-buxi-generative-existence/results/records/binding-preserving-substitution.json). **Reused sources:** the unmigrated `InferentialGrounds` language and evaluation, `GroundRelationTransport`'s prior propagation result, and `RecognitionalBinding`'s source-free identity result. Only the first is imported in the new module; the latter two are conceptual predecessors, not dependencies of its proof. The registered [derivation-soundness](../../../../theories/shengsheng-buxi-generative-existence/results/records/derivation-soundness.json) is a related premise-preservation boundary in a different calculus, not a formal adapter to this result.

**Delta:** construct simultaneous substitution under nested binders and prove its evaluation law, with an exact all-consumer criterion and a same-type capture control. Earlier `application_after_abstraction` supplied an environment and reduced by definition; it did not recursively insert an open producer term inside every use of a consumer. `CoreTreeRearticulation.substitute_derived_basis`, also inspected, expands closed basis derivations in a different calculus; it is credited, not reproduced as a new result here.

**Premises and correspondence:** finite typed syntax, stable atomic labels, the same ground-family interpretation and evaluation clauses. The construction has no mutation, divergence or physical cost. Context positions articulate relations of introduction and use within one derivation; context lists do not posit independently existing domains. Reference to actual reasoning, intensional content or temporally changing grounds still needs an adequate account.

**Evidence and integration:** nine new Lean theorems with a source-bound receipt below. An actual producer term can now replace the consumer's designated assumption throughout the finite expression, including under new binders. A producer meeting the consumer's input requirement supplies the premise of the checked assessment theorem; neither requirement nor its satisfaction is manufactured by substitution.

### 9.1 Start with the relation that changes

A hypothetical derivation already differentiates an introduction and its dependent uses. When a concrete derivation replaces that introduction, its output must reach those uses. Meanwhile, assumptions introduced later inside the consumer retain their own uses. These roles form through nesting in the same argument; they are not two pre-existing things joined by an unexplained outside operation.

The positive candidate is **continuation of the designated dependence through replacement**. A use that originally depended on the substituted assumption receives the producer's output; a use of a newly introduced assumption continues to depend on that new assumption. On this account, permission to substitute is justified locally by the preserved relation, not by a further assertion announcing that replacement is valid. The formal result below tests this proposal's mathematical consequence under explicit interpretation.

中文例子：先有根据 x，再暂设 y，随后在论证内部暂设 z，而结论仍凭 y。现在用 x 代入 y：正确的接续是在暂设 z 的范围内仍凭 x；若把 x 改接到 z，就改变了根据。x 与 z 即使属于同一类型，也不能因此互换。这个例子所问的是一个论证内部的依存怎样保持，不是独立主体怎样给独立对象赋义。

### 9.2 Exact checked statement

Let σ assign a replacement term to every position of a consumer context. Let η give the original context grounds and ρ interpret the replacement terms. In the existing language:

\[
\left[\forall t,\quad
  \operatorname{eval}(\operatorname{substitute}(\sigma,t),\rho)
  =\operatorname{eval}(t,\eta)\right]
\quad\Longleftrightarrow\quad
\left[\forall p,\quad
  \operatorname{eval}(\sigma(p),\rho)=\eta(p)\right].
\]

Both quantifiers range over the declared types and contexts. The forward direction tests the term that uses each position. The reverse direction is an induction over every term. Under abstraction, the newest position remains bound locally, while older replacement terms are shifted across the new binder. This is constructed by `liftSubstitution`, with `extract_rename` proving that the shift preserves their evaluated grounds. It is not a separately assumed global semantic-correctness predicate.

The necessity concerns **agreement for all consumers**. A particular consumer can ignore a changed position. The criterion also concerns equality of interpreted values; distinct historical sources that currently evaluate equally may satisfy it. It does not uniquely reconstruct provenance or prove identity of all meanings.

| New checked declaration | Scope |
|---|---|
| `extract_rename` | Position maps preserve evaluation when the mapped positions supply the original grounds. |
| `extract_substitute` | The recursively constructed replacement preserves evaluation when its position outputs match. |
| `all_terms_agree_iff_positions` | The displayed exact criterion; individual use terms give necessity. |
| `discharge_matches_supply` | Replacing one assumption by a producer agrees with evaluating the consumer under the producer's supplied ground. |
| `discharge_preserves_assessment` | Given a hypothetical assessment guarantee and a producer meeting its input condition, the substituted term meets the output condition. |
| `successive_substitution` | Two syntactic insertions and the composed insertion evaluate identically; not syntactic equality or equal physical execution cost. |
| `nested_substitution_retains_outer` | The concrete replacement under an inner binder retains the earlier outer position. |
| `typed_capture_changes_answer` | Correct and captured alternatives have the same type but give true and false when their two grounds differ. |
| `matching_values_hide_capture` | Those two alternatives agree when the two grounds happen to have equal values. One matching answer therefore does not distinguish the bindings. |

The assessment theorem keeps both inputs explicit: `∀ g, input g → output (eval body [g,env])`, and `input (eval producer env)`. It does not prove the hypothetical guarantee or the supplied ground's adequacy by discharging a variable. No unconditional conclusion or axiom-free metatheory follows from removing a local assumption slot.

### 9.3 A substantive rival, and what the comparison decides

The captured candidate follows the nearest newly introduced same-type position. It remains a well-typed, meaningful term. It can be understood as a different instruction: “use the newest available ground.” Both candidates preserve the same available Bool values and inner/outer nesting; they differ in which introduction the conclusion depends upon. With outer=true and inner=false they diverge; with both=true they agree. These are Bool data, not assertions that falsehood is provable.

This rival defeats the broader claim that preserving type, surface name or one observed answer suffices for substitution fidelity. It does not refute the narrower criterion that retains designated dependence. Conversely, designating the original dependence as the target requires justification in applying the account to an actual argument. An activity intentionally redirecting its dependence may be coherent; it simply does not preserve this specified hypothetical derivation. We do not label every such activity “not reasoning.”

The strongest unresolved objection is that the semantic equations already interpret what counts as supplying the same ground. The response is a bounded explanation: the constructed insertion exposes and preserves those position relations throughout the term, so correctness at every compound expression need not be assumed separately. That removes one explanatory burden, **not** the warrant of the primitive context-use interpretation. Equal output is also weaker than complete sameness of content, experience or history. The model's omission of those relations must not be reported as their ontological absence.

### 9.4 Primary sources and novelty assessment

The authors' [PLFA chapter on de Bruijn representation](https://plfa.github.io/DeBruijn/) was inspected at its introduction and its renaming, simultaneous substitution and single substitution sections. It presents typed position indices, extends substitution under a binder by retaining the new variable and shifting earlier replacements, and illustrates avoidance of capture. This is an established technique; our Lean implementation adapts it to the repository's existing language and proves a denotational criterion. It is not a claim to have discovered substitution, de Bruijn indices or their philosophical justification.

The previously inspected Martin-Löf discussion in §6 remains the source for the hypothetical-proof comparison. No new full-text or historical-priority claim is made here. Source comparison supports reusing the mathematical method; it supplies no authority that would settle the stronger foundational question.

### 9.5 What this changes in the foundational account

Identity and substitution now have a connected candidate explanation: a use refers to an introduced ground; replacing that introduction preserves the designated dependencies through the continuation. The equality theorem exposes the exact supplied interface. The capture control shows a genuine difference within the same representational scope, not an arbitrary truth-label switch.

The mathematical continuation is complete. The next **foundational** question is why a displayed introduction/use relation warrants its claimed referential role across the relevant variations—rather than merely coinciding with another interpretation at the current values—and how that warrant is recognized or corrected in actual argument. The target must remain fixed enough for a rival to contest it. Merely compiling a larger interpreter, renaming a position “self-evident,” or demanding an endless independent certificate would not answer this question.

This remains a proposed internal account of warrant, not proof that use of logic makes the project impossible. It also does not substitute the independently authorized Theory of Becoming or the completed G0/J ethical route for this session's metalogical objective.

### 9.6 Actual checks and records

[InferentialSubstitution.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/InferentialSubstitution.lean) was compiled with its unchanged `InferentialGrounds` import by the [isolated checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_inferential_substitution.py). The [final frozen receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/inferential-substitution-checks/20261008T181823.552825Z/receipt.json) records **9 new theorems, 10 inherited declaration audits, 19 total**: 13 empty reports and 6 depending only on `Quot.sound` through function extensionality. There are no custom postulates, proof holes, warnings or classical-choice dependencies. Reporting those six as empty would be incorrect. First attempts failed on an unavailable congruence helper and an implicit context type; explicit rewriting and annotation repaired them. A subsequent successful eight-theorem build was extended by the equal-value control; only the final nine-theorem build is the current result.

The inherited ten comprise eight theorems and two supporting definitions; they are not new. The [before-edition manifest](development/inferential-substitution-before/manifest.json) preserves the preceding theory, study and source record. [Scoped integration checks](INFERENTIAL-SUBSTITUTION-CHECKS.json) and [owned chain edits](INFERENTIAL-SUBSTITUTION-INDEX-EDITS.json) distinguish this work from concurrent research. Generated overviews follow the canonical record; no independent-agent acceptance, empirical validation or full presuppositionless completion is claimed.
