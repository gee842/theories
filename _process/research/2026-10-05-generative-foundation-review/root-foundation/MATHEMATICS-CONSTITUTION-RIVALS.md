# Mathematical constitution: rival groundings and the missing modal bridge

**Date:** 6 October 2026. **Status:** adversarial research note; AI elaboration, not a quotation of Ren. **Connection under examination:** generative formation and composable possibility → the constitution of every mathematical truth. This is stronger than the existing acquisition, representation, quotient and proof-system results. It concerns why mathematical truths hold, including truths nobody discovers or physically instantiates.

**Finding:** the present causal root does not entail unique mathematical constitution. There is a precise underdetermination even when the entire causal process and the entire interpreted mathematical content are fixed. This rules out the inference from the current premises alone; it does not establish that no further metaphysical argument could succeed. A structural-modal account of **all admissible organizations**, with truth indexed to its structure and logic, is a serious positive repair. Plural mathematical structures do not refute that account. Its missing work is to explain admissibility, closure, modality and grounding rather than inherit them from mathematics and rename them.

Read with [the foundational premises](../../../../theories/becoming/history/FOUNDATION-PREMISES.md), [the deeper root](../../../../theories/becoming/history/DEEPER-GENERATIVE-ROOT.md), [the main mathematics formulation](../../../../theories/becoming/history/MATHEMATICS-AND-GENERATIVITY.md), [generative presentations](MATHEMATICS-GENERATIVE-PRESENTATIONS.md), [structural results](MATHEMATICS-STRUCTURAL-RESULTS.md) and [learning evidence](MATHEMATICS-LEARNING-EVIDENCE.md).

## 1. Four different claims

| Claim | What would establish it | What does not establish it |
|---|---|---|
| Mathematical practice is a formation within reality. | A causal account of formation, acquisition, retention and use of mathematical representations. | That the represented truths are constituted by those acts. |
| A mathematical domain has a generative presentation. | A specified grammar or construction, equations, interpretation and adequate representation theorem. | That the presentation is the sole ground of the represented domain. |
| Mathematical truth expresses necessary relations among possible organizations. | A justified notion of possibility and a truth-preserving connection between mathematical structures and those possibilities. | Observing successful finite constructions alone. |
| The generative root uniquely constitutes every mathematical truth. | The preceding coverage plus an account of explanatory dependence and a reason rival grounds are inadmissible or equivalent in the relevant sense. | Universal descriptive applicability, shared vocabulary, or agreement with all observed mathematics. |

The existing process interface supplies states, actions and allowed transitions, with finite histories composing through shared actual boundary states. Its results quantify over a supplied law. The stronger claim concerns the ground of those quantifiers, interpretations and mathematical possibilities as well. Moving from the first two rows to the last two therefore changes the explanatory target; additional premises must be stated.

The word **unique** also needs a target. Unique up to a proved equivalence of presentations is a mathematical claim. Unique ultimate explanation is a metaphysical claim. Several equivalent foundations need not defeat the latter, but their equivalence alone does not establish it.

## 2. An exact countermodel with the mathematical content held fixed

The strongest rival test should not compare arithmetic with modular arithmetic and announce that mathematics is inconsistent. It should preserve the very same mathematical content while changing the proposed grounding relation.

### Expansion lemma

Let a base language describe:

1. a causal process \(P=(S,A,E)\), including every mathematical-practice record we wish to examine;
2. a fixed interpreted mathematical structure \(M\);
3. a nonempty collection \(C\) of true, interpreted mathematical claims about \(M\).

Let \(T\) be any theory of this base structure. It may include the current formal root and all the mathematical truths about \(M\) available in that language. Expand the language with a predicate \(G(c)\), intended to mean “the root constitutes the truth of claim \(c\).” Assume \(T\) has no axiom constraining \(G\).

For any base model \(B\models T\), form two expansions with **exactly the same underlying objects, operations, mathematical interpretation and process**:

\[
B_+ : G=C,
\qquad
B_- : G=\varnothing.
\]

Both satisfy \(T\), because every sentence of \(T\) is evaluated in the unchanged base interpretation. But

\[
B_+\models\forall c\in C\,G(c),
\qquad
B_-\not\models\forall c\in C\,G(c).
\]

Therefore \(T\) does not entail even universal constitution, and hence does not entail unique universal constitution. We can take \(M\) to be one fixed interpretation of ordinary arithmetic throughout; no arithmetic truth needs to change. The example also works for a fixed finite structure and one true equation, so the underdetermination does not depend on controversial infinity.

**Scope of the proof.** This is a formal non-entailment result relative to the stated premises, using an ordinary supplied metatheory. It is not a proof that every arbitrary assignment of a metaphysical predicate corresponds to a genuinely possible world. Its point is to locate the missing bridge exactly. A defender may supply substantive constraints on grounding that eliminate \(B_-\); those constraints and their justification are then the argument to assess. Adding the desired universal-grounding sentence itself closes the formal gap by assumption, without yet giving that justification.

### A substantive rival reading

The two expansions correspond to a genuine explanatory disagreement worth developing:

- **Generative constitution:** structural necessity is grounded in the generative root; human practices discover or articulate its consequences.
- **Independent structural necessity:** the same mathematical relations hold necessarily in the same interpreted structures; the causal root explains how organisms, communities and machines gain access to them, while their necessity is primitive or receives a different structural/modal explanation.

Both can accept every result about paid formation, exact abstraction, reusable invariants and proof checking. Both can accept the very same interpreted theorem. Agreement of those results therefore does not settle the direction of grounding. This is stronger than showing that two different mathematical structures exist.

If “root” is defined to include all truths and all their grounds, the rival is excluded verbally. That definition may express a metaphysical commitment, but inclusion in one comprehensive reality is not yet a derivation of explanatory dependence from differentiation and composition. Conversely, calling mathematical necessity primitive does not show that the rival is the best explanation. Its explanatory cost is a legitimate subject of comparison.

## 3. Composition does not by itself choose a completion

Fix the same elementary process in both cases:

\[
S=\{s\},\quad A=\{a\},\quad E=\{(s,a,s)\}.
\]

Its finite histories are \(a^n\), and concatenation gives \(a^m a^n=a^{m+n}\). Keep all these histories, their prefix order and their composition unchanged. Consider an additional sort of objects permitted as bounds for these histories:

\[
D_{\mathrm{fin}}=\mathbb N,
\qquad
D_{\mathrm{comp}}=\mathbb N\cup\{\omega\},
\]

with the usual order on the shared natural-number part and \(n<\omega\) for every finite \(n\). The finite-number sort and its arithmetic are the same in both expansions. The bound sort is different.

The assertion

\[
\exists x\in D\;\forall n\in\mathbb N\;(n\leq x)
\]

is false for \(D_{\mathrm{fin}}\): for each candidate \(x=n\), the finite history of length \(n+1\) exceeds it. It is true for \(D_{\mathrm{comp}}\), witnessed by \(\omega\). The completed object need not be an additional state or actual event of \(P\), so the process itself has not changed.

This is an explicit failure of the implication “finite composability supplies a completed bound object.” It uses natural numbers in the external metatheory and does not pretend to derive that metatheory from the process. Nor is the finite-bound domain being proposed as all of mathematics.

An account of all possible organizations can include **both** structures and correctly state the two indexed truths. That is a good answer to the plurality, not a contradiction. The remaining question is why the root licenses the expanded domain, which other completions it licenses, and how its notion of possibility distinguishes an admissible mathematical object from an arbitrary notation. The same issue recurs for function spaces, power objects, unrestricted subsets, universes and stronger infinities. The example establishes the first missing closure rule, not the impossibility of any eventual closure argument.

## 4. Composition does not by itself choose a validity regime

Keep the causal process fixed and compare two truth-value algebras for an additional logical language:

\[
H_2=\{0,1\},\qquad H_3=\{0,u,1\},\quad 0<u<1.
\]

In either chain define conjunction as minimum, disjunction as maximum, and

\[
x\Rightarrow y=
\begin{cases}
1 & x\leq y,\\
y & x>y.
\end{cases}
\qquad \neg x=(x\Rightarrow0).
\]

These are Heyting algebras; their implication satisfies the adjunction \(z\wedge x\leq y\) iff \(z\leq(x\Rightarrow y)\). The two-value algebra is Boolean. In it, every value satisfies \(p\vee\neg p=1\). In the three-value algebra,

\[
\neg u=0,
\qquad
u\vee\neg u=u\neq1.
\]

Thus universal excluded-middle validity holds in one regime and fails in the other. The common subalgebra \(\{0,1\}\) has exactly the same operations in both. In particular, this comparison need not alter any shared interpreted finite arithmetic facts. The intermediate value is not automatically a probability or a psychological degree of confidence; it is part of an algebraic semantics.

The calculation shows that the existing causal root, with no additional rule selecting logical semantics, does not force Boolean validity. It does **not** show that classical logic is false, that intuitionistic logic cannot describe classical mathematics, or that one root cannot ground both regimes with their distinct validity conditions. An all-regimes theory still needs a justified metalanguage and rules governing which semantic regimes it recognizes. Encoding those regimes in classical mathematics demonstrates representability; it does not by itself derive the constitutive priority of classical logic or of the root.

## 5. What established foundational alternatives actually show

These are comparators for explicit premise accounting, not authorities that decide the metaphysical dispute.

**Categorical foundations.** Lawvere's category-of-sets program makes composition central, but its mathematical strength is supplied by substantive axioms. Leinster's primary equivalence proof identifies an ETCS formulation with a well-pointed topos equipped with a natural numbers object and choice. The topos conditions include finite limits, exponentials and a subobject classifier. Having a category of composable arrows alone does not supply that package. This is a constructive precedent for a relational foundation and a warning against treating “composition” as already containing every needed existence principle. [Lawvere, original long version and commentary](https://pages.jh.edu/rrynasi1/FoundationsOFMath/Literature/Lawvere2005AnElementaryTheoryOfTheCategoryOfSets%28LongVersion%29WithCommentary.pdf); [Leinster, proof of the equivalence](https://webhomes.maths.ed.ac.uk/~tl/rst_supp.pdf).

**Homotopy type theory.** The HoTT Book explicitly adds univalence because its underlying type theory does not establish that the canonical map from identity of types to equivalence of types is itself an equivalence. It also distinguishes ordinary excluded middle for mere propositions from a stronger assertion for arbitrary types: ordinary excluded middle may be added, whereas the stronger formulation is incompatible with univalence. Thus HoTT is not a simple counterexample to classical mathematics. It makes the identity/equivalence bridge and the relevant logical choice explicit. Saying that our root has paths or composition does not yet derive those axioms. [HoTT Book, univalence section](https://raw.githubusercontent.com/HoTT/book/master/basics.tex); [classical versus intuitionistic logic section](https://raw.githubusercontent.com/HoTT/book/master/logic.tex).

**Set-theoretic multiverse.** Hamkins argues for multiple set concepts and corresponding universes, understood realistically; the view is not merely a synonym for formal symbol manipulation. It demonstrates how a foundational program can recognize a plurality of structures without asking one structure to settle every unindexed assertion. This is a philosophical proposal supported by mathematical work, not an established verdict that all mathematics has a multiverse ground. Its relevance here is that plural scope and common grounding can coexist. [Hamkins, *The set-theoretic multiverse*](https://arxiv.org/abs/1108.4223).

These sources do not prove that our root and each alternative are mutually inconsistent, nor that they are equally adequate. They reveal additional mathematical choices which an encompassing generative theory must recover, interpret or explicitly leave as local structure. Successful translations among foundations would support shared content; an extra argument would still be needed to establish which account explains that content's necessity.

## 6. The strongest positive repair

A defensible candidate is:

> Mathematical truths state necessary relations within, and between, admissible differentiated and composable possibilities. Actual formation is one realization of this wider generative structure; mathematical possibility is not exhausted by the structures physically realized so far.

This can preserve the ambition that the root constitutes mathematics without claiming that people produce truths by thinking them, that mathematics is limited to finite computation, or that all structures collapse into one preferred structure. It should index a truth by its interpretation, for example

\[
(L,T,M,\varphi),\qquad M\models_L T,\qquad M\models_L\varphi.
\]

A validity claim across an admitted class \(K_L(T)\) then has the form

\[
\forall M\in K_L(T)\;M\models_L\varphi.
\]

The union of everything true in some structure is not a single unindexed theory: a sentence and its negation may each be true somewhere. Indexing preserves the differences. Nor must all admitted possibilities form one set; a proposed account may require classes, universes, a schema or another explicit size discipline.

The displayed notation is a **research interface**, not a completed foundation. It already borrows language, models, quantification, truth and possibility from a metatheory. The work is to explain or minimize that borrowing, rather than hide it. Defining “admissible” as “whatever mathematics allows” gives immediate coverage at the cost of making the constitutive claim circular. Defining it as “whatever is consistent” needs a specified logic, a notion of consistency and a justified connection to semantic realization; a completeness theorem for one logic cannot silently be generalized to every possible framework.

The strongest next result would recover a substantial, independently specified mathematical regime from a smaller generative premise set, make each closure and identity principle explicit, and explain why the resulting interpretation is invariant under changes of presentation. That would be real progress beyond universal redescription. It would remain a result about the recovered regime until its coverage and grounding argument were extended.

## 7. Exact discriminators and what they can decide

| Question | A discriminating result | Limit |
|---|---|---|
| Does the root recover a chosen mathematics? | A faithful interpretation or equivalence with explicit background assumptions; retained failure cases outside its domain. | Recovery establishes content preservation, not ultimate ground. |
| Does it determine admission of a completion? | A non-circular premise entailing the bound object's existence, while explaining why the finite-only expansion fails that premise. | An added existence axiom must be justified; relabeling it “generativity” does not reduce it. |
| Does it determine identity and logic? | Derive the relevant identity, inference and validity conditions, or explain principled plural indexing. | Composition alone has not selected these conditions. |
| Does it explain more than an independent-necessity rival? | An argument showing explanatory dependence, economy or necessity which the rival cannot reproduce without adding comparable premises. | Agreement of interpreted theorems is insufficient. |
| Can practice select the constitutive account? | The accounts imply different distributions of observations or different feasible interventions, with the difference derived from their grounding commitments. | Identical observational and interventional laws cannot empirically identify the grounding label. |
| Is the account universal? | A justified coverage argument for its intended range, including its handling of non-finitary and noncomputable objects. | A growing list of examples or all currently formalized cases is not that argument. |

The empirical identification limit can be stated exactly. Suppose two accounts assign the same distribution to every practice record under every available intervention. Any statistic of those records then has the same distribution under both accounts. No test built only from those records can distinguish their grounding attributions. This follows from equality of the observation laws; it is not an empirical discovery that every future theory will be observationally equivalent. A future generative account could acquire empirical content by imposing additional constraints on physical realizability or cognition. Such constraints would then need independent testing.

Mathematical and philosophical discrimination remain possible even without an empirical difference. Contradiction, circular explanation, unnecessary assumptions, failure to preserve meaning, or inability to recover an intended domain can count against an account. Those assessments must be made on their own merits, without presenting mathematical-practice data as uniquely confirming metaphysical constitution.

## 8. Claim boundary and next connection

The present result is stronger than “we have not yet checked enough examples”: the existing premises omit a constraint required for the proposed entailment, and the unchanged-content expansions display that omission. Conversely it is weaker than “no generative constitution argument is possible”: such a conclusion has not been established.

The best current position is that generativity supplies a promising account of mathematical formation and a candidate structural-modal account of mathematical being. Existing exact presentations and quotients strengthen the former and offer tools for the latter. They do not yet establish that the root uniquely constitutes every mathematical truth.

The next named connection is **causal differentiation and finite composition → a justified space of mathematical possibilities, with explicit identity and closure principles**. To change this assessment, the project needs a bridge argument that eliminates the same-content rival for a substantive reason, or reduces it to an explicitly proved equivalence of explanatory accounts. Further evidence that people learn mathematics through compositional processes would advance acquisition research; it would not, by itself, close this bridge.

**Verification scope.** The expansion lemma, completion example and truth-value calculation above are explicit mathematical arguments, not reported human experiments or newly machine-checked theorems. The literature comparisons were checked against primary text: Leinster's complete proof, the HoTT Book's relevant source chapters, and Hamkins's full paper sections describing the rival positions. Lawvere's original long version is linked as the foundational antecedent; the precise ETCS axiom characterization used here is supported by Leinster's displayed theorem and proof. No empirical uniqueness claim is made.
