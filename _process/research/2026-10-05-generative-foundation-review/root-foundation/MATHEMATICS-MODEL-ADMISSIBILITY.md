# Resolving model admissibility, truth selection and structural identity

6 October 2026. AI-authored continuation of [mathematical truth and the root](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/MATHEMATICAL-TRUTH-AND-THE-ROOT.md), following Ren's request to finish the remaining bridges. This note tests the concrete proposal **admissible mathematical structure = model of a consistent specification**. It closes the relative model-existence question in a declared classical first-order setting, then proves the separate conditions for truth selection and the obstruction to selecting an infinite term-generated structure by first-order axioms alone.

These are standard model-theoretic results and their application to this theory. Soundness, completeness and compactness are established antecedents, not newly formalized here. The proofs below are hand arguments in an ordinary classical set-based metatheory. No new Lean verification, empirical evidence or mathematical originality is claimed.

## 1. A definite positive admission principle

Fix a countable finitary first-order language with equality, ordinary nonempty structures, and a sound and complete classical deductive calculus. Let \(T\) be any set of its sentences; it need not be finite or effectively enumerable.

The model-existence form of completeness gives

\[
T\text{ is syntactically consistent}
\quad\Longleftrightarrow\quad
\exists M\;(M\models T).
\tag{A1}
\]

The right-to-left implication is soundness. The left-to-right implication is the completeness theorem. A model can be constructed by extending the language with witnesses, choosing a consistent complete extension, and interpreting closed terms modulo its equality relation. The existence of that extension need not be an effective search procedure. Tao's author-hosted exposition states the countable model-existence result and its construction in §1.4.3, Proposition 1.4.15. [Primary exposition](https://terrytao.wordpress.com/wp-content/uploads/2012/12/mbk-77-tao4-epsilon2.pdf).

Thus consistency is a substantive relative admission criterion, rather than the circular instruction to admit exactly the desired truths. Contradictory specifications receive no ordinary classical model; consistent specifications receive at least one.

Four limits remain part of the theorem's meaning. Consistency is measured in a supplied calculus. Model existence is established in a supplied metatheory. A model is not automatically a physical realization or a metaphysically possible world. And the criterion does not select one intended model when several satisfy the specification. Calling all four matters “admissibility” would erase essential distinctions.

## 2. Exactly when a specification selects one truth profile

Call \(T\) **negation-complete** if for each sentence \(\varphi\), either \(T\vdash\varphi\) or \(T\vdash\neg\varphi\). Assume \(T\) is consistent.

### Proposition A2 — Unique model truth profile iff negation-completeness

The following are equivalent:

1. Any two models of \(T\) agree on every sentence of its original language.
2. For every sentence \(\varphi\), either all models of \(T\) satisfy \(\varphi\), or all satisfy \(\neg\varphi\).
3. \(T\) is negation-complete.

**Proof.** By (A1), there is a model \(M\). If 1 holds, each sentence has the same classical truth value in every model as in \(M\), giving 2. Statement 2 gives 1 directly. Completeness of the calculus takes 2 to 3, and soundness takes 3 to 2. Consistency ensures that the alternatives cannot both hold. ∎

There is an explicit witness when the condition fails. If neither \(T\vdash\varphi\) nor \(T\vdash\neg\varphi\), both \(T\cup\{\varphi\}\) and \(T\cup\{\neg\varphi\}\) are consistent: inconsistency of one would prove the opposite sentence from \(T\), using the classical deduction rules. By (A1) they have models, so \(T\) admits opposite answers to that sentence.

This is an exact completion criterion for a model family, not a metaphysical uniqueness theorem. The different models are alternative interpretations under an incompletely specified subject. It would be incorrect to say that they assign opposite truth values to one already fully interpreted proposition. A common root may instead retain the models as distinct indexed subjects; then it determines their different indexed answers.

### Corollary A2a — Completing a consistent specification requires choices

A consistent classical first-order specification can be extended to a negation-complete one, but an undecided sentence supplies at least two incompatible such extensions. The consistent completions therefore need not be unique.

**Proof.** Extend each of the two consistent sets above to a complete consistent set by the standard Lindenbaum construction. One contains \(\varphi\), the other \(\neg\varphi\). Neither complete extension can contain the other. ∎

The existence of a completion answers whether completion is possible. It does not answer which completion correctly describes an intended mathematical subject. For arithmetic, a chosen standard structure answers that semantic question; a bare instruction to keep adding consistent sentences does not identify it.

## 3. A complete truth profile still need not select the structure

### Proposition A3 — Infinite term coverage cannot be imposed by ordinary first-order axioms alone

Let \(T\) have an infinite model in its original language \(L\). Adjoin a new constant \(c\), and add

\[
c\ne t\qquad\text{for every closed }L\text{-term }t.
\tag{A3}
\]

Every finite subset is satisfiable: in an infinite model of \(T\), interpret \(c\) outside the finitely many values mentioned. Compactness yields a model satisfying all the additions. Its \(L\)-reduct is a model of \(T\) with an element named by no original closed term. Hence a first-order theory with an infinite model cannot require all of its models to be generated by their original closed terms. ∎

This is the familiar coverage obstruction recorded in the Open Logic Project's completeness chapter, Example com.24; the argument here explicitly uses **closed** terms. [Primary project text, §§com.8–com.9](https://builds.openlogicproject.org/content/first-order-logic/completeness/completeness.pdf).

For an especially strong instance, take \(T=\operatorname{Th}(\mathbb N)\), every first-order sentence true in standard arithmetic. Every standard closed arithmetic term has a numeral value. A model supplied by A3 therefore has an element outside all those numeral values, while agreeing with standard arithmetic on every original-language sentence. It is not isomorphic to the standard structure: an isomorphism would preserve \(0\) and \(S\), and every element of the standard structure is a finite successor of zero.

Thus even fixing **all first-order arithmetic truth** does not fix the structure up to isomorphism. This does not contradict the [initial arithmetic construction](MATHEMATICS-TRUTH-CONSTITUTION-MATH.md#proposition-c4--four-recursive-equations-plus-initiality-fix-ordinary-arithmetic). Initiality and external generation by finite terms are stronger semantic conditions than an arbitrary first-order axiom collection. They can select the standard structure, but their use must be recorded.

The result also corrects a possible over-demand on the theory: if its target is truth determination, structural categoricity may be unnecessary. If its target is the entire mathematical subject and its ontological identity, agreement on a language's truths is insufficient. The claimed kind of uniqueness must stay explicit.

## 4. Why a stronger specification need not become an all-truth algorithm

Suppose the proposed root is formalized as a consistent computably enumerable first-order theory in the usual arithmetic language, extending Robinson arithmetic. If all of its models agreed on every arithmetic sentence, A2 would make the theory negation-complete. The standard incompleteness theorem excludes that combination of conditions. The language restriction ensures that deciding the arithmetic fragment is not silently equated with completeness in an expanded language. The [prior foundation audit](MATHEMATICS-FOUNDATION-AUDIT.md#5-exact-limits-on-an-all-truth-generator) records the hypotheses and primary antecedents.

The consequence is a precise restriction on one design: **an effective first-order axiom specification with all its models admitted cannot supply an unrestricted unique arithmetic truth profile under those hypotheses**. It says nothing against selecting standard arithmetic by a richer semantic condition, using a noneffective complete theory, or pursuing a nonalgorithmic constitutive explanation. Each alternative has an additional commitment to explain, not an automatic contradiction.

The original initial-algebra result already uses such a richer semantic condition. It remains sound and is not weakened by the present observation. What fails is treating it as though it had removed the distinction between a specified intended structure and an effective first-order axiom system.

## 5. Resolution for the common-root claim

| Proposed bridge | Result of completing this test |
|---|---|
| Consistency → some mathematical realization | Closed within the declared classical first-order metatheory by model existence |
| Consistency → one intended realization | Does not follow; consistent completions and models can differ |
| Specification → one sentence-truth profile across all its models | Exactly negation-completeness, assuming consistency and the declared calculus |
| Complete first-order truth → unique structure | False in general; A3 applies even to true arithmetic |
| Finitary construction → no extra domain elements | Valid for the externally selected generated structure; ordinary first-order axioms alone cannot universally impose infinite term coverage |
| These relative theorems → our root's unique metaphysical priority | Does not follow; no theorem here identifies mathematical model existence with ultimate grounding |

The mathematical admission question therefore has a finished conditional answer. The philosophical proposal can adopt this classical framework, or explicitly defend another. The causal root's current vocabulary does not make that adoption inevitable. A claim that the root uniquely selects the framework would need a substantive justification for excluding or deriving rivals; merely completing a consistent theory does not provide it.

This result contributes to the repository's explicit-grounding requirement. It explains which premises support a mathematical model of regulation or learning without making the model's truth a proof of its empirical identification, its evaluative adequacy, or the necessity of the entire generative theory.
