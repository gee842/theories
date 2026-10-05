# Closing the construction, identity and subset-closure questions

6 October 2026. AI-authored mathematical continuation of [mathematical truth and the root](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/MATHEMATICAL-TRUTH-AND-THE-ROOT.md), following Ren's request to finish the remaining connections. This note completes the **conditional construction** question: what independently stated formation and identity data suffice to determine a mathematical subject and all its interpreted first-order truths? It also gives exact countermodels to obtaining stronger closure from weaker rules.

**Result:** fixed positive formation rules determine a least generated carrier; fixed equations determine a least identity congruence; no junk and no unforced identifications characterize the resulting initial algebra. Fixed, compatible atomic interpretations and classical semantic clauses then determine the complete first-order truth relation. These are finished relative theorems. They do not select the formation rules, equations, admissibility constraints or logic from the presently stated causal root. Full subset closure has its own exact characterization and is strictly stronger than finite construction over an infinite base.

All proofs below are hand arguments in ordinary classical set-based mathematics; ZFC suffices. The ambient sets, powersets used in the proofs, completed finite syntax and external induction are part of that metatheory. The note does not derive this background from no assumptions. These are standard mathematical mechanisms applied to the theory, not claims of new mathematics, empirical confirmation or new Lean verification. The existing [truth-constitution note](MATHEMATICS-TRUTH-CONSTITUTION-MATH.md) proves the semantic and arithmetic results used here; [model admissibility](MATHEMATICS-MODEL-ADMISSIBILITY.md) separately addresses general first-order consistency and model existence.

## 1. Positive rules give a unique least admissible carrier

Fix an ambient set \(U\), a seed set \(B\subseteq U\), and a set of positive formation rules

\[
\mathcal R\subseteq \mathcal P_{\mathrm{fin}}(U)\times U.
\]

A rule \((F,u)\) permits \(u\) whenever every member of the finite premise set \(F\) is already admitted. Empty premise sets are allowed. A subset \(X\subseteq U\) is **closed** when it contains \(B\) and includes every permitted consequence whose premises it contains. “Admissible” in this section means exactly this rule closure; it does not also mean logically consistent, physically possible or metaphysically necessary.

Define

\[
C(X)=X\cup B\cup\{u:\exists(F,u)\in\mathcal R, F\subseteq X\},
\qquad
X_0=B,\quad X_{n+1}=C(X_n),\quad X_\omega=\bigcup_{n<\omega}X_n.
\tag{F1}
\]

### Proposition F1 — Three equivalent descriptions of the least generated carrier

The set \(X_\omega\) is simultaneously:

1. the least closed subset of \(U\);
2. the intersection of all closed subsets of \(U\);
3. the elements possessing a finite derivation tree from seeds and rules.

**Proof.** The stages are increasing. If a finite premise set lies in their union, each premise belongs to some stage, and all belong to one common stage by taking the maximum of finitely many indices. Its consequence belongs to the next stage. A rule with no premises also fires at a finite stage. Thus \(X_\omega\) is closed.

If \(Y\) is closed, induction gives \(X_n\subseteq Y\) for every \(n\); hence \(X_\omega\subseteq Y\). This proves leastness. The family of closed sets is nonempty because it includes \(U\). Its intersection is closed and must therefore equal the least member. Finally, stage induction constructs finite derivation trees, and induction on a finite tree puts its conclusion in some finite stage. ∎

This closes the least-carrier question once the formation law and ambient possibilities are fixed. It is a mathematical completion of all finite derivations, not a claim that a physical process executes infinitely many steps. Neither the seeds nor the rule relation need be effectively enumerable, so the result does not by itself give an algorithm.

Finitary rules alone do not imply a countable carrier: an uncountable collection of zero-premise rules can admit uncountably many objects. The familiar countability bound requires countably many symbols and seeds, or another actual countability restriction on the generation data.

### Proposition F2 — Exactly which closure operations are finitarily generative

Let \(\operatorname{cl}:\mathcal P(U)\to\mathcal P(U)\) be extensive, monotone and idempotent. The following are equivalent:

1. **Finite character:**
   \[
   \operatorname{cl}(X)=\bigcup_{F\subseteq X, F\text{ finite}}\operatorname{cl}(F).
   \tag{F2}
   \]
2. **Directed-union preservation:** for every nonempty family \(\{X_i\}\) directed by inclusion,
   \[
   \operatorname{cl}\left(\bigcup_iX_i\right)=\bigcup_i\operatorname{cl}(X_i).
   \tag{F3}
   \]
3. There is one fixed set of positive finite-premise rules whose least closure of each seed set \(X\) is \(\operatorname{cl}(X)\).

**Proof, 1 implies 2.** A finite set of witnesses in \(\bigcup_iX_i\) lies in one \(X_j\), by directedness and finitely many choices of containing indices. Finite character puts every element of the left side into some \(\operatorname{cl}(X_j)\). The opposite inclusion follows from monotonicity. The empty witness case uses nonemptiness of the directed family.

**Proof, 2 implies 1.** The family of finite subsets of \(X\) is nonempty, directed, and has union \(X\). Apply (F3).

**Proof, 1 implies 3.** Take exactly the rules

\[
\mathcal R_{\operatorname{cl}}=
\{(F,u):F\subseteq U\text{ finite},\ u\in\operatorname{cl}(F)\}.
\tag{F4}
\]

The set \(\operatorname{cl}(X)\) contains \(X\) and is rule-closed: if \(F\subseteq\operatorname{cl}(X)\), then
\(\operatorname{cl}(F)\subseteq\operatorname{cl}(\operatorname{cl}(X))=\operatorname{cl}(X)\).
Therefore the least rule closure is contained in it. Conversely, finite character writes any element of \(\operatorname{cl}(X)\) as a consequence of some finite \(F\subseteq X\), so the least rule closure contains it.

**Proof, 3 implies 1.** By F1, every derived element has a finite derivation tree and hence uses only finitely many leaves from \(X\). It is consequently in the closure of a finite subset of \(X\). The reverse inclusion follows from monotonicity. ∎

Thus finite composition has an exact mathematical scope: **algebraic closure**, meaning finite character. It does not characterize every possible closure principle. Representation (F4) is not automatically explanatory compression: specifying its rules by a preexisting closure operator can import the very information one hoped to explain.

## 2. What changes with infinitary premises or negative conditions

### Proposition F3 — Positive infinitary closure still exists, but can exceed stage omega

Allow \(\mathcal R\subseteq\mathcal P(U)\times U\), with premises of arbitrary set size. The intersection of all seed-containing rule-closed subsets is still the unique least closed set.

**Proof.** The family contains \(U\). If all premises of a rule lie in its intersection, they lie in every member, so the consequence lies in every member and in the intersection. ∎

The finite-stage union need not be closed. Let

\[
U=\mathbb N\cup\{\star\},\quad B=\{0\},\quad
\mathcal R=\{(\{n\},n+1):n\in\mathbb N\}\cup\{(\mathbb N,\star)\}.
\tag{F5}
\]

Then \(X_n=\{0,\ldots,n\}\), while \(X_\omega=\mathbb N\) omits \(\star\). The additional rule first fires at stage \(\omega+1\). There is no finite derivation tree for \(\star\) under these rules.

More generally, use successor stages \(X_{\alpha+1}=C(X_\alpha)\) and unions at limit ordinals. In ZFC this iteration on a fixed set stabilizes and reaches the least closed set. To see a bound, put \(\kappa=\max(\lvert U\rvert,\aleph_0)\) and fix a well-order of \(U\). If every successor stage before \(\kappa^+\) added an element, choose the least newly added element at each stage. These choices would inject \(\kappa^+\) into \(U\), which is impossible. At a stage with no addition the iteration is fixed; induction places every stage in every closed set, proving leastness of the fixed stage. This bound uses the declared set-theoretic background; it supplies no physical transfinite execution or effective stopping test.

This is a special set-theoretic instance of monotone fixed-point theory. Tarski's general theorem establishes fixed points on complete lattices; the direct arguments here expose the specific hypotheses needed for formation. [Tarski, 1955, Theorem 1](https://people.csail.mit.edu/carroll/probSem/Documents/Tarski.pdf).

### Counterexample F3a — Negative premises can remove leastness

On \(U=\{p,q\}\), impose the conditions

\[
p\notin X\Rightarrow q\in X,\qquad
q\notin X\Rightarrow p\in X.
\tag{F6}
\]

The sets \(\{p\}\), \(\{q\}\), and \(\{p,q\}\) satisfy both conditions. Their intersection is empty and fails both. No least satisfying set exists. A synchronous procedure that starts empty and adds both conclusions selects \(\{p,q\}\), but that is not the least satisfying set. Other semantics for negative rules require their own justification.

Positive closure also does not establish logical consistency. If the objects of \(U\) are formula tokens, zero-premise rules admitting both \(p\) and \(\neg p\) have a perfectly well-defined least generated set. That set cannot be an all-true theory under ordinary classical semantics. Existence of the closure and admissibility as jointly true content are different properties.

## 3. Least identity, consistency of distinctions, and initiality

Fix a set-sized finitary functional signature \(\Sigma\), designated generators \(G\), and the nonempty term set \(T=T_\Sigma(G)\). Nonemptiness holds if there is a generator or a constant; without either, a nonempty first-order carrier needs an additional provision. Generators here are designated inputs, not universally quantified variables in an equation schema.

Let \(E\subseteq T\times T\) be declared equations. If equations are given as universal schemas, include their relevant substitution instances in \(E\). Let \(\theta_E\) be the intersection of all congruences on \(T\) containing \(E\). The family is nonempty because the universal relation is a congruence. Its intersection is again a congruence.

### Proposition I1 — Least identity is exactly finite equational derivability

The relation \(\theta_E\) consists exactly of pairs having a finite derivation using equations in \(E\), reflexivity, symmetry, transitivity and substitution into operation contexts.

**Proof.** The finite-derivation relation contains \(E\), is an equivalence relation, and is compatible with every operation: finite arity permits combining finitely many finite derivations. It is therefore a congruence containing \(E\), so it contains \(\theta_E\). Conversely, every congruence containing \(E\) respects every listed proof rule and contains every finitely derived pair. Their intersection does too. ∎

This is the **least amount of identification** compatible with the equations. It is the finest admissible equivalence relation, yielding the largest freely generated quotient in the quotient-map order. It is not a minimization of the number of domain elements. Further identifications produce smaller quotients.

No algorithmic decidability follows for arbitrary presentations: a finite proof for each positive equality is a different matter from an effective procedure deciding every equality or inequality. Even enumeration requires the relevant syntax and axiom instances to be effectively available.

### Proposition I2 — Exact admissibility criterion for required distinctions

Let \(D\subseteq T\times T\) be required ground disequalities. There exists a nonempty \(\Sigma\)-algebra with assigned generator values satisfying every equation in \(E\) and every disequality in \(D\) **if and only if**

\[
D\cap\theta_E=\varnothing.
\tag{I1}
\]

**Proof.** For any realization, term evaluation has a congruence kernel containing \(E\), hence containing \(\theta_E\). It cannot distinguish a pair in \(\theta_E\). Conversely, the quotient algebra \(Q=T/\theta_E\), with generators interpreted by their classes, satisfies \(E\), and (I1) says it satisfies every required disequality. It is nonempty because \(T\) is. ∎

Thus preserving declared distinctions has a complete relative test. With equations alone the quotient always exists, even if it has just one element; existence is not nontriviality. For example, if the signature contains only constants \(a,b\) and \(E=\{(a,b)\}\), the quotient is a singleton and the requirement \(a\ne b\) is impossible. I2 concerns ground equations and disequalities; it is not being substituted for the broader first-order admissibility theorem in the companion note.

### Proposition I3 — No junk and no unforced identity are equivalent to initiality

Consider the category whose objects are nonempty \(\Sigma\)-algebras \(A\) with designated generator maps \(\eta:G\to A\) satisfying \(E\), and whose arrows are homomorphisms preserving the designated generators. Let \(e:T\to A\) be evaluation. The following are equivalent:

1. **No junk:** \(e\) is onto; and **no unforced identities:** \(\ker(e)\subseteq\theta_E\).
2. The evaluation map induces an isomorphism \(Q=T/\theta_E\to A\) preserving the generators.
3. \((A,\eta)\) is initial in this category.

**Proof.** Since \(A\) satisfies \(E\), \(\theta_E\subseteq\ker(e)\). Condition 1 therefore gives equality of the two relations. Evaluation descends to a well-defined injective map from \(Q\); no junk makes it onto. It preserves operations and generators, so it is an isomorphism. Conversely, the induced isomorphism gives both assertions in 1.

For any object \((B,\zeta)\), evaluation in \(B\) respects \(\theta_E\) and descends to a homomorphism \(Q\to B\). A homomorphism preserving generators must take each term class to that term's evaluation; hence this map is unique. Thus \(Q\) is initial, proving 2 implies 3. If \(A\) is initial, its unique maps to and from \(Q\) have identity composites, because each initial object has only one endomorphism. They are inverse isomorphisms, and generator preservation forces the map out of \(Q\) to be the evaluation map. Hence 3 implies 2. ∎

Initiality has therefore been reduced to two explicit constitutive conditions rather than left as an unexplained label. The resulting isomorphism is unique **in the given category**, with its fixed signature and designated generators. This does not assert that an arbitrary reduct has no automorphisms.

No junk alone permits extra quotient identifications. No unforced identities alone permits extra unnamed elements: with one constant and no other operations, a two-element algebra assigning the constant to one element has the correct term-equality kernel but has junk. Both conditions do indispensable work.

If condition (I1) holds, the same quotient is also initial in the full subcategory of objects satisfying the required ground disequalities. This follows because it belongs to that subcategory and already has a unique arrow into each of its objects. It does not imply that arbitrary additional relational constraints have such an initial object.

## 4. The completed relative constitution theorem

### Theorem C — Formation, identity and interpretation determine all truth in the stated scope

Supply the following data and requirements:

1. A set-sized finitary signature and designated generators, with a nonempty term set generated by the specified formation rules.
2. An equation presentation \(E\) and the requirement of no junk and no identifications beyond \(\theta_E\).
3. Any required ground disequalities, with (I1) satisfied.
4. For each relation symbol, a predicate on the appropriate finite tuples of terms invariant under replacement by \(\theta_E\)-equivalent terms.
5. Ordinary finitary first-order syntax and fixed classical satisfaction clauses, with equality interpreted as identity on the quotient and quantifiers ranging over the whole quotient.

Then there exists a generated interpreted structure satisfying these specifications. Any two such realizations are uniquely isomorphic under their designated term interpretation, and they agree on every sentence of this language. The satisfaction relation is uniquely fixed, whether or not it is computable or effectively enumerable.

**Proof.** F1 constructs the term carrier from its positive formation rules. I1 constructs its least congruence; I2 ensures the requested distinctions survive. Operations descend through congruence, and predicates descend through the stated invariance. I3 identifies every realization with the same quotient algebra. Exact agreement with the supplied predicates makes that algebra isomorphism preserve and reflect all relations. Structural induction on terms and formulas gives unique satisfaction and its invariance under isomorphism, as proved in [C1–C3 of the truth-constitution note](MATHEMATICS-TRUTH-CONSTITUTION-MATH.md#2-a-unique-compositional-truth-relation-for-fixed-semantic-data). ∎

The predicate condition is substantive. One way to obtain it is to define relations directly on the quotient. Another is to use positive formation rules on atomic term statements and include rules replacing each argument by an equivalent one. The least resulting relation is then invariant. Taking that least extension is an additional closed-world choice: a theory that only requires the positive instances to hold may admit larger relations and different negative or quantified truths.

“Least” consequently has three separate roles: least generated syntax excludes ungenerated objects; least congruence excludes unforced equalities; a least generated predicate extension excludes ungenerated positive instances. Each order and its effect must be stated. None is a general injunction to minimize every aspect of a mathematical subject.

This theorem closes the mathematical construction pipeline. It is relative to the recipe, the surrounding mathematics and the semantics. The [arithmetic construction](MATHEMATICS-TRUTH-CONSTITUTION-MATH.md#proposition-c4--four-recursive-equations-plus-initiality-fix-ordinary-arithmetic) supplies a compact instance; the [universal naming construction](MATHEMATICS-TRUTH-CONSTITUTION-MATH.md#corollary-c3a--every-set-sized-first-order-structure-has-such-a-presentation) represents every nonempty set-sized first-order structure while importing its full domain and atomic data. Those are different degrees of explanatory economy within the same conditional theorem.

## 5. Full subsets have a positive uniqueness theorem of their own

Fix an actual set \(D\). A candidate subset sort consists of a set \(S\) and membership \(\epsilon\subseteq D\times S\). Define

\[
\operatorname{ext}(s)=\{d\in D:d\mathrel\epsilon s\}.
\tag{P1}
\]

### Proposition P1 — Extensionality and fullness characterize the powerset sort

The extension map is a bijection \(S\to\mathcal P(D)\) if and only if:

- **Extensionality:** equal extensions imply equal members of \(S\).
- **Fullness:** every external subset \(A\subseteq D\) is the extension of some member of \(S\).

**Proof.** The first condition is exactly injectivity of the extension map, and the second is exactly surjectivity. ∎

Consequently any two full extensional subset sorts have a unique membership-preserving isomorphism fixing the base \(D\): map each subset object to the unique object with the same extension. Once that sort, any further operations and classical semantics are fixed, truth in its two-sorted first-order language is fixed by the same compositional argument. Full second-order quantification over subsets of \(D\) can thereby be interpreted through this chosen powerset sort.

This genuinely closes the uniqueness question **if fullness is justified**. Fullness here quantifies over the surrounding mathematics' actual \(\mathcal P(D)\). Merely asserting “every subset in our present subset sort is present” supplies no such condition. An internal quantifier over an already restricted sort cannot establish external fullness.

### Proposition P2 — Which union closure yields all subsets

Let \(\mathcal F\subseteq\mathcal P(D)\) contain the empty set and every singleton.

1. If \(D\) is finite, closure under finite unions already gives \(\mathcal F=\mathcal P(D)\).
2. For arbitrary \(D\), closure under unions of **all** subfamilies of \(\mathcal F\) gives \(\mathcal F=\mathcal P(D)\).
3. For \(D=\mathbb N\), closure under unions of **all external countable** subfamilies suffices. Another sufficient condition is finite union closure together with closure under unions of all external increasing omega sequences of members.

**Proof.** Every \(A\subseteq D\) is the union of its singleton members. This is a finite family in 1, a permitted family in 2, and a countable family in 3. For the increasing-sequence version of 3, finite union closure supplies each finite set \(A\cap\{0,\ldots,n\}\), and their increasing union is \(A\). The converse closure properties hold in the full powerset. ∎

The increasing-sequence formulation assumes finite union closure in addition to singletons and the empty set; without it, increasing-sequence closure alone need not create a two-element set. With this assumption the equivalence is exact.

The word “all” does the substantive work. A sequence externally selected using an arbitrary subset \(A\) is not necessarily a computable, definable or internally available sequence. Restricting the admitted sequences changes the closure principle. P2 provides a positive route to full subsets over a countable base, but does not derive that route from finite composition alone.

## 6. Three strict closure levels over exactly the same arithmetic base

Keep actual standard arithmetic \((\mathbb N,0,S,+,\times)\) fixed. Use a two-sorted language with this number sort, a subset sort, membership, singleton formation, empty and universal sets, binary union and complement. Interpret all subset operations by their ordinary set meanings.

Consider the following subset carriers:

\[
\begin{aligned}
\operatorname{FC}(\mathbb N)&=\{A\subseteq\mathbb N:A\text{ is finite or cofinite}\},\\
\operatorname{Def}(\mathbb N)&=\{A\subseteq\mathbb N:A\text{ is definable in first-order arithmetic}\\
&\hspace{40mm}\text{using finitely many natural-number parameters}\},\\
\mathcal P(\mathbb N)&=\{A:A\subseteq\mathbb N\}.
\end{aligned}
\tag{P2}
\]

### Proposition P3 — Finite generation, definability and fullness are strictly different

\[
\operatorname{FC}(\mathbb N)\subsetneq
\operatorname{Def}(\mathbb N)\subsetneq
\mathcal P(\mathbb N).
\tag{P3}
\]

All three sorts are extensional, contain every singleton, and are closed under the specified finite Boolean operations. The first is exactly the least such Boolean family generated by all singletons.

**Proof.** Finite unions of singletons yield all finite sets; complementation yields all cofinite sets. Finite and cofinite sets remain finite or cofinite under complement and finite union, hence also intersection and difference. This proves the leastness assertion and closure for \(\operatorname{FC}\).

Finite and cofinite sets are arithmetically definable with number parameters. Definable sets are closed under Boolean operations by combining their formulas. The even numbers are definable by \(\exists k\ n=k+k\), but both the evens and their complement are infinite. This proves the first strict inclusion.

There are countably many finite arithmetic formulas and countably many finite tuples of natural parameters. Thus there are at most countably many arithmetically definable subsets. Cantor's diagonal argument makes \(\mathcal P(\mathbb N)\) uncountable, proving the second strict inclusion. ∎

The scope of \(\operatorname{Def}(\mathbb N)\) is precise: arithmetic formulas with number parameters. It is not claimed to satisfy every comprehension scheme involving quantification over arbitrary sets, or to be closed under definitions using arbitrary external subsets as parameters.

### Corollary P3a — A designated stronger closure claim is independent of the weaker conditions

Let

\[
\varphi_{\mathrm{even}}\equiv
\exists X\ \forall n\left(n\mathrel\epsilon X\leftrightarrow\exists k\ n=k+k\right).
\tag{P4}
\]

This is a sentence of the displayed two-sorted first-order language. It is false in the \(\operatorname{FC}(\mathbb N)\) expansion and true in the other two expansions. These expansions have exactly the same actual arithmetic base and agree on membership and operation tables wherever their subset carriers overlap.

Therefore even fixing standard arithmetic, extensionality, all singleton subsets and their finite Boolean closure does not determine the existence of the even subset. An explicit arithmetic comprehension principle closes that particular gap; it still does not establish full powerset closure, by P3. The stronger conditions are mathematically intelligible additions with definite effects, not consequences of merely renaming finite formation “unrestricted generation.”

The distinction also explains the countable-term restriction. A countable finitary signature with countably many generators has only countably many finite terms, and every quotient of that term set has at most countably many elements. It cannot name every element of the uncountable subset sort \(\mathcal P(\mathbb N)\). One can enlarge the generators, allow stronger formation principles, or name \(\mathcal P(\mathbb N)\) as one higher-level object; none makes its individual members finitely nameable by the original countable syntax. The universal naming construction remains valid because it explicitly permits an uncountable family of generators.

P3a is not a refutation of one common root supporting many mathematical subjects. Once each complete subset carrier is designated, its own interpreted truths are determinate. It is a refutation of the narrower claim that the **shared weaker specification alone** already selects the stronger closure or its truth profile.

## 7. The domain cannot also contain distinct codes for all its own subsets

### Proposition P4 — No set-sized carrier is a faithful container for its entire powerset

There is no injection \(j:\mathcal P(U)\to U\) for any set \(U\).

**Proof.** Such an injection would give a surjection \(f:U\to\mathcal P(U)\): use the inverse on the image of \(j\), and assign the empty set outside that image. For \(A=\{u\in U:u\notin f(u)\}\), choose \(a\) with \(f(a)=A\). Then \(a\in A\) if and only if \(a\notin A\), a contradiction. ∎

This forbids one particular all-encompassing set-sized container. It does not forbid a common generative account with successively larger typed domains or a properly formulated class-level account.

Nor does it forbid a set closed under taking powersets of its **members**. The hereditarily finite sets \(V_\omega=\bigcup_{n<\omega}V_n\), with \(V_0=\varnothing\) and \(V_{n+1}=\mathcal P(V_n)\), give a counterexample to that overstatement. If \(x\in V_\omega\), then \(x\subseteq V_n\) for some finite \(n\), so \(\mathcal P(x)\subseteq V_{n+1}\) and \(\mathcal P(x)\in V_{n+2}\subseteq V_\omega\). But \(\mathbb N\subseteq V_\omega\) and \(\mathbb N\notin V_\omega\), so \(\mathcal P(V_\omega)\) is not contained in \(V_\omega\). Memberwise closure and closure over the whole carrier are different claims.

## 8. What is now settled for the root claim

The current [deeper causal root](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/DEEPER-GENERATIVE-ROOT.md) already separates a supplied event law from its least finite reachability closure. F1 generalizes the mathematical form of that separation: a law fixes its closure; the existence of closure does not select the law. I1–I3 and Theorem C finish the corresponding formation-to-identity-to-truth analysis.

There is also an exact non-entailment result. Formalize the presently supplied causal vocabulary in one sort, and retain the same fixed causal process in two expansions. Add the same actual arithmetic sort and the finite subset-closure requirements of section 6. Give one expansion the subset sort \(\operatorname{FC}(\mathbb N)\), and the other \(\mathcal P(\mathbb N)\). The causal reduct, arithmetic base and all stated finite-closure requirements agree, while (P4) differs. Consequently those commitments entail neither (P4) nor its negation. No derivation from just those premises can settle that closure claim in classical semantics.

The argument assumes exactly the absence of an additional axiom connecting causal data to the stronger mathematical closure. It does not assert that every conceivable enriched root has these same models, or treat their existence as proof of two metaphysically possible worlds. It identifies an actual logical boundary of the current specification. Adding a bridge can change the result; the added bridge then carries identifiable explanatory content.

| Connection | Finished status |
|---|---|
| Fixed positive finite rules and seeds → least admissible carrier | Established; finite trees, omega-stage union and intersection characterize the same object |
| Finitary generation → exact class of closure operators | Established: finite character is equivalent to directed-union preservation and finite-rule presentation |
| Positive infinitary rules → least closure | Established on a fixed set; omega-stage completion can fail and transfinite stages can be needed |
| Arbitrary negative admission conditions → least closure | False; F3a has incomparable minimal solutions and no least one |
| Fixed equations → least identity | Established; precisely finite equational consequence |
| Equations plus required ground distinctions → realizability | Exactly the disjointness criterion (I1) |
| No junk plus no unforced identities → initiality | Established, and conversely, in the declared algebra category |
| Fixed compatible atomic meanings and classical clauses → all first-order truth | Established by compositional semantics; no effectiveness claim |
| Extensionality plus external fullness → unique subset sort | Established; it is isomorphic to the actual powerset |
| Finite subset composition over an infinite base → full subset closure | False; P3 and P3a separate the conditions explicitly |
| Current causal root alone → this uniquely necessary recipe and logic | Not entailed by its present formal commitments; the shared-reduct countermodels exhibit the missing information |

The local mathematical task is therefore resolved: **conditional constitution is proved, and the stronger unlicensed inferences are ruled out at their stated scope.** No remaining theorem in this note is being deferred under the label “open.” What the formal results do not establish is the independent metaphysical defense of selecting these constitutive principles and reducing every adequate rival to them. The positive method principles are candidates for such a stronger theory; they are not already consequences of the thin causal root.

For the governing derivation, this also prevents a category error about learned abstraction. An acquired representation can warrant further inferences once its formation, identity and interpretation conditions are established. Theorems about those conditions do not explain how a physical learner obtains reliable observations, pays for the representation, preserves a suitable interpretation or becomes concerned with another center. Those remain operational connections in the accepted research sequence, with their supplied premises preserved.

## 9. Antecedents and validation

The closure, congruence and initial-object mechanisms are standard. The [existing generative-presentation study](MATHEMATICS-GENERATIVE-PRESENTATIONS.md) records the universal-algebra antecedents; Burris and Sankappanavar's [author-hosted text](https://www.math.uwaterloo.ca/~snburris/htdocs/ualg.html) is the primary book reference for closure operators, congruences and free algebras. Tarski's fixed-point theorem is cited at its specific use above. Semantic recursion, arithmetic initiality, universal presentation and their limits have self-contained proofs and primary references in the [truth-constitution companion](MATHEMATICS-TRUTH-CONSTITUTION-MATH.md).

Validation here consists of the explicit hand proofs and countermodels, checked against their declared domains and category. No executable package was added for routine finite examples, and no earlier finite check is being relabeled as a proof about arbitrary closure or every mathematical truth.
