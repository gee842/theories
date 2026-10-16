# Mathematical-root frontier: definability, reconstruction and source

6 October 2026. AI-authored primary-source audit and mathematical development. This supports the newly requested frontier beyond the [conditional foundation assessment](FIXED-FINISH-LINE-AUDIT.md#15-completion-assessment-of-the-conditional-candidate). It does not revise that assessment's finish line. Named connection: independently warranted generative commitments → uniquely recoverable mathematical content; separate operational connection: consequences → formation of the rule that revises a method. The latter cannot silently serve as evidence for the former.

## 1. What advances the previous argument

The [truth-constitution proofs](MATHEMATICS-TRUTH-CONSTITUTION-MATH.md) already establish compositional truth after structure and semantics are fixed, initial presentations under fixed equations, and a factorization criterion: a target descends to a proposed root exactly when it is constant on the root's fibers. The [closure resolution](MATHEMATICS-CLOSURE-RESOLUTION.md) identifies substantive distinctions among finite generation, stronger closure and domain fullness. The [foundation audit](MATHEMATICS-FOUNDATION-AUDIT.md) preserves the difference between such mathematics and universal metaphysical justification.

Two stronger positive tests are now available:

1. **Implicit-to-explicit definition:** in ordinary first-order semantics, uniform unique determination of an added relation entails an actual definition in the root language.
2. **Reconstruction from transport:** in a fixed equational class, every operation commuting with all homomorphisms is already a generated term operation.

These improve on saying that a chosen formal presentation works. They give precise exhaustiveness criteria. Their decisive inputs are the comparison class, expressive resources and admissible maps; proving the criteria does not independently justify those inputs.

## 2. Four primary works and access limits

**Parikh, *Beth definability, interpolation and language splitting*.** The inspected author manuscript is dated 5 May 2009; publication is *Synthese* 179 (2011), 211–221. Section 1 states the same-reduct test and proves Beth's result through Craig interpolation. This is a primary research paper containing the proof, not Beth's original 1953 publication; the latter was not inspected in full. The result concerns first-order models generally, not merely finite models or one intended structure. [Author-uploaded full text](https://www.researchgate.net/publication/220608027_Beth_definability_interpolation_and_language_splitting).

**Lawvere, *Functorial Semantics of Algebraic Theories*.** The original 1963 PNAS announcement, pp. 869–872, was inspected in full. Page 870 explicitly identifies the reconstructed theory's operations with natural transformations of the underlying-set functor and states that reconstruction recovers the algebraic theory up to natural equivalence. The underlying-set functor and homomorphisms are part of the datum. The short proof below is an independently written specialization, not a new general-algebra theorem. [Primary scan](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/lawvere.pdf).

**Tarski, *The Semantic Conception of Truth and the Foundations of Semantics* (1944).** Sections 7–12 and notes 16–18 were inspected in the original article scan, including the object/meta-language distinction, semantic contradiction and recursive satisfaction construction. This is Tarski's own partly informal exposition; it is not presented here as a full modern proof of the corollary below. The corollary is derived explicitly with its diagonalization premise. [Primary scan](https://inters.org/files/tarski1944.pdf).

**Fine, *Essence and Modality*.** The inspected author-uploaded manuscript is dated June 1992, revised February 1993; the published paper is from 1994. Fine argues that necessary connections do not by themselves identify their constitutive source, using the asymmetric relation between an object and its singleton. His philosophical argument provides a substantive rival to identifying essence with necessary coextension. It is not an established mathematical theorem or an empirical result. [Author-uploaded full text](https://www.researchgate.net/publication/366643157_ESSENCE_AND_MODALITY_Kit_Fine_Philosophy_NYU).

No result here is inferred from an abstract alone. No human, biological or physical experiment was performed. These works establish antecedents and constraints, not priority or empirical support for the repository's distinctive root interpretation.

## 3. A positive criterion stronger than supervenience

Let \(L_0\) be a first-order root language, \(R\) a new relation on its existing domain, and \(T\) a consistent theory in \(L_0\cup\{R\}\). Suppose any two models of \(T\) with **identical \(L_0\)-reducts**, including domain and every root-symbol interpretation, agree on \(R\). Beth's theorem yields an \(L_0\)-formula \(\varphi(\bar x)\) such that

\[
T\models\forall\bar x\,[R(\bar x)\leftrightarrow\varphi(\bar x)].
\]

This yields an explicit definition, not merely an arbitrary set-theoretic function of a reduct. It is unique up to equivalence under the theory, not unique as a string of symbols. At-most-one expansion does not ensure that every proposed root model has an expansion. To claim a conservative definitional extension of a root theory \(T_0\), also require \(T\supseteq T_0\) and expansion existence for every model of \(T_0\).

**Application proposed here.** Choose a substantive target relation and root vocabulary before testing uniqueness. Specify admission conditions without inserting the target's intended definition as an axiom. Either prove the two-expansion condition or exhibit two expansions disagreeing on the target. A proof would close an actual root-to-content bridge; a countermodel would identify missing information. Same-domain expansion excludes silently adding a new mathematical carrier. Higher-order, inductive or intended-model restrictions require their own metatheory; ordinary Beth cannot simply be carried over by name.

This is a useful next study for a bounded mathematical subject. It is not yet a theorem that the current physical root uniquely defines every mathematical subject, nor does linguistic definability establish a metaphysically privileged direction of explanation.

## 4. Positive reconstruction of all algebraic operations

Fix a finitary signature \(\Sigma\), equations \(E\), and the class \(\mathcal V\) of all \(E\)-algebras with all homomorphisms. Write \(U\) for the underlying-set functor. For \(n\geq1\), let \(F(n)\) be the free algebra on \(x_1,\ldots,x_n\).

**Reconstruction theorem.** Every family \(\eta_A:(UA)^n\to UA\) satisfying

\[
h(\eta_A(\bar a))=\eta_B(h\bar a)
\quad\text{for every homomorphism }h:A\to B
\]

is a single term operation, unique modulo the equations valid in \(\mathcal V\).

**Proof.** The element \(\eta_{F(n)}(x_1,\ldots,x_n)\) is represented by a term \(t\). For any \(A,\bar a\), the unique evaluation homomorphism \(h_{\bar a}:F(n)\to A\) sends the generators to \(\bar a\). Naturality gives

\[
\eta_A(\bar a)=h_{\bar a}(\eta_{F(n)}(\bar x))=t_A(\bar a).
\]

Conversely, term operations commute with homomorphisms by induction on terms. Two terms define the same family exactly when their generator values agree in \(F(n)\), equivalently when their equation holds throughout \(\mathcal V\). ∎

For \(n=0\), the same argument requires a free zero-generated algebra and the declared convention concerning empty algebras. In a category requiring nonempty carriers, an empty signature need not have such an initial algebra. The proof does not erase that existence issue.

**A concrete instance and a sharp failure.** In groups, the free one-generated group is \(\mathbb Z\), so every unary family natural for all group homomorphisms is \(g\mapsto g^k\) for one fixed integer \(k\). Isomorphism invariance alone permits

\[
q_G(g)=\begin{cases}e_G,&G\text{ finite},\\g,&G\text{ infinite}.\end{cases}
\]

This is invariant under every group isomorphism. But for the inclusion \(C_2\to C_2\times\mathbb Z\), a nonidentity element is sent to a nonidentity element: applying \(q\) before the inclusion gives the identity; applying it afterwards gives that nonidentity element. Thus the map class makes a demonstrable difference to reconstruction.

**Consequence for the root, inferred here.** This supplies a constructive answer to “how could generative operations be exhaustive?” Establish an independently motivated realization category and underlying carriers; then show the relevant operations respect every admitted homomorphism. The free realization reconstructs all such operations from terms. This is stronger than only showing that already given terms preserve structure.

The condition is demanding. An arbitrary physical transfer need not be a homomorphism, and physical admissibility need not include every algebraic quotient or every abstract algebra. Conversely, allowing only physical isomorphisms weakens the conclusion, as the counterexample shows. Fixing \(\Sigma,E,\mathcal V,U\) already fixes substantial mathematics. The theorem neither derives these data from bare causal formation nor covers every relation, quantifier, infinity principle or truth predicate. It reconstructs a specified algebraic operation theory.

## 5. An exact limit on a same-level uniqueness target

Let \(L\) be an effectively coded first-order language and \(T\) a consistent first-order theory in \(L\cup\{\mathrm{Tr}\}\). Assume:

- its arithmetic proves diagonalization for arbitrary \(L\)-formulas;
- for every \(L\)-sentence \(\phi\), \(T\) entails \(\mathrm{Tr}(\ulcorner\phi\urcorner)\leftrightarrow\phi\).

**Corollary.** \(T\) cannot implicitly determine \(\mathrm{Tr}\) over all identical \(L\)-reducts.

**Proof.** Otherwise Beth supplies an \(L\)-formula \(\theta(x)\) defining \(\mathrm{Tr}\) in \(T\). Diagonalization gives an \(L\)-sentence \(\lambda\) with \(T\vdash\lambda\leftrightarrow\neg\theta(\ulcorner\lambda\urcorner)\). Its truth biconditional and the definition give \(T\vdash\lambda\leftrightarrow\theta(\ulcorner\lambda\urcorner)\), contradicting consistency. ∎

No recursive enumeration of \(T\)'s axioms is assumed. The target is truth for the whole defining language \(L\), not truth for a smaller arithmetic fragment in a richer language. External truth for one standard structure, typed truth hierarchies and stronger semantics are not refuted. Nor is the existence of one common generative metaphysics refuted. What fails is this exact first-order, same-level, all-model implicit-uniqueness demand.

The advance is diagnostic: specifying a universal root in this format creates a provable boundary. Changing the format may be legitimate, but its stronger semantic resources must be named and justified. Tarski's external satisfaction construction and the repository's prior compositional truth theorem remain intact.

## 6. Why greater autonomy does not settle ontological source

The current [method-revision construction](../../../../theories/becoming/history/METHOD-REVISION.md) installs a larger supplied controller, uses a paid consequence receipt to change its method bit, and thereby changes a subsequent candidate generator. The causal connection is substantive. Its recipe, consequence-to-bit mapping, receipt calibration and initial commissioning are supplied. A further experiment could form or revise that mapping from earlier operational consequences, reducing one identifiable dependency. The [comparator note](METHOD-REVISION-COMPARATORS.md) already separates this from differential survival and supplies the necessary intervention logic.

No change in that physical history alone determines whether the mathematical constraints it realizes are constituted by generativity, independently existing and discovered, or structurally specified through an alternative foundation. Those accounts need not disagree about any receipt, resource movement or newly assembled controller. This is an observational-equivalence claim about those proposed protocols, not a proof that every metaphysical distinction is empirically inaccessible.

The remaining challenge is therefore more specific than adding an unconstrained “ground” predicate. **Definitional equivalence, natural reconstruction and physical realization answer different questions.** The first eliminates vocabulary; the second recovers operations from a declared semantic category; the third explains how a carrier obtains a functioning capability. Exclusive constitution additionally requires an argument that these forms of recovery identify the source of mathematical necessity, with the intended explanatory direction. Fine supplies a serious objection to treating necessity alone as that argument. One may dispute his view, but it cannot be excluded by simply defining “constitution” to mean coextension.

A causally formed learning law also need not arise without any prior physical law. “Formed rather than preinstalled” is a relative historical claim about the apparatus and available parts. Every finite implementation can be described by a fixed larger transition rule. That redescription does not invalidate acquired organization; equally, acquired organization does not establish that all constraints governing its formation were themselves generated by that particular carrier.

## 7. Attainable next argument and discriminators

The strongest warranted next formulation is conditional: **relative to independently defended formation, identity, realization and transport conditions, mathematical operations can be reconstructible and extensionally unique; where first-order implicit uniqueness holds, added relational content is explicitly definable.** This leaves plural mathematical subjects available. It does not require one privileged structure to contain every branch of mathematics.

The next substantive test should specify one candidate bridge before the desired mathematical outcome is imposed:

1. Give root-language constraints and a designated target operation or relation. Record every new logical, domain and closure premise.
2. Prove existence and uniqueness in the resulting comparison class, or exhibit a same-root rival. For algebraic operations, test all proposed homomorphisms rather than only isomorphisms.
3. Test conservative enrichments: does adding causally idle descriptive structure change the supposed root or reconstruction? If it does, explain why that is ontologically significant rather than a presentation choice.
4. State what would discriminate constitutive source from faithful realization. If no operational difference is predicted, provide the separate explanatory or metaphysical premise and its argument; do not call a controller experiment that premise's empirical confirmation.

A successful theorem would narrow the constitution gap by eliminating a real freedom in interpretation. A successful formation experiment would narrow a supplied-mechanism gap. Neither achievement should be discounted, and neither should be substituted for the other. The unrestricted metaphysical frontier remains a research target; the positive criteria and exact obstruction above are completed mathematical assessments within their stated scope.
