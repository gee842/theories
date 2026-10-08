# Resolution of mathematical uniqueness: exact achievements and remaining choices

**6 October 2026. AI-authored continuation of the requested attempt to finish the stronger mathematical claim.** This note examines whether stronger plausible principles of generation, exactness, closure and determination establish unique universal grounding. It supplements [the constitution mathematics](MATHEMATICS-TRUTH-CONSTITUTION-MATH.md) and [the rival-account study](MATHEMATICS-CONSTITUTION-RIVALS.md). It does not replace the [governing generative project](../../../../theories/becoming/chapters/GENERATIVE-GROUNDING.md).

**Resolution:** several remaining *mathematical* questions can be settled. A specified presentation and semantics determine truth; every nonempty set-sized finitary first-order structure has a naming-and-table presentation; and precise countermodels show that substantial generic generative principles still leave rule, logic and domain choices open. Extensional dependence cannot by itself identify the ground of necessary truths. These results close the audited inferences. They do not prove that no more informative root or further metaphysical argument can succeed.

The examples below do more than change an unconstrained grounding predicate. They test substantive proposed criteria. Their proofs use ordinary classical set-based mathematics; where countable collections of countable sets are used, the metatheory is ZFC. This is an explicit comparative background, not a claim to have derived that background from the root.

## U1. Necessary truth makes extensional grounding tests non-specific

Let \(W\neq\varnothing\) be a declared comparison class of worlds or explanatory accounts. Fix **one interpreted mathematical proposition** \(p\), not merely its spelling. Let \(t:W\to\{0,1\}\) record its truth. Suppose \(p\) is necessary throughout this comparison class:

\[
\forall w\in W\quad t(w)=1.
\]

Let \(b:W\to B\) be **any** proposed base datum, relevant or irrelevant. Then

\[
b(w)=b(v)\Longrightarrow t(w)=t(v)
\]

holds automatically. Indeed \(t=f\circ b\), where \(f\) is the constant function with value 1. This includes a base containing no information at all: take \(B=\{*\}\).

The same argument applies to a fixed collection of interpreted necessary truths. If \(q\) indexes the questions and \(t(w,q)=\tau(q)\) is independent of \(w\), then

\[
t(w,q)=F(b(w),q),\qquad F(b,q)=\tau(q)
\]

for every base \(b\). An entire fixed mathematical truth set can therefore extensionally factor through an irrelevant base together with the question index.

**What this proves.** The criterion “truth cannot change without the base changing,” by itself, cannot uniquely distinguish a constitutive ground of necessary mathematical truths within this comparison class. This is a no-go for that criterion's discriminatory sufficiency, not for every account of grounding.

**What it does not prove.** The constant map does not provide an algorithm for discovering an unknown truth, a finite description of the full truth set, or a reason why the proposition is true. Nor does every mathematical sentence count as necessary without fixing its interpretation and modal scope. The theorem's necessity hypothesis is explicit. If a proposed criterion also requires an informative, independently justified construction, it has gone beyond mere extensional factorization and must be assessed accordingly.

The existing semantic-determination theorem remains valuable: it constructs the truth relation recursively from specified atomic data and semantic clauses. U1 explains why **determination alone** cannot establish the unique metaphysical priority of those data. To identify a ground, the account needs explanatory dependence that distinguishes candidates even when the relevant truths agree in every admitted world.

## U2. Least generation is decisive only relative to its rules

Consider the following substantial common requirements for a proposed abstract subject:

1. A fixed signature has a constant \(0\) and a unary constructor \(S\).
2. Every finite closed expression is admitted.
3. Every object is denoted by such an expression; there are no additional unnamed objects.
4. Equality is the least congruence containing a specified set of equations.
5. The quotient is initial among algebras satisfying those equations.
6. Operations are total and compositional, and ordinary classical first-order semantics is exact.

These requirements do not select the equations. Two explicit realizations are:

| | Free iteration | Idempotent iteration |
|---|---|---|
| Supplied equations | None | \(S(S(x))=S(x)\) |
| Initial domain | \(\mathbb N\) | \(\{0,1\}\) |
| Constructor | \(S(n)=n+1\) | \(S(0)=1,\ S(1)=1\) |
| Closed-term equality | Equal numbers of \(S\)'s | All positive numbers of \(S\)'s agree |
| Nontriviality | \(0\neq S(0)\) | \(0\neq S(0)\) |

For the first, every closed expression is \(S^n(0)\), and the empty equational theory identifies none of the distinct terms. Evaluation into any pointed unary algebra is the unique homomorphism, proving initiality.

For the second, repeated application of the equation reduces every positive numeral to \(S(0)\). The displayed two-element algebra satisfies the equation and separates \(0\) from \(S(0)\), proving there are exactly two classes. In every algebra satisfying the equation, \(S^n(0)=S(0)\) for \(n\geq1\), so evaluation again gives the unique homomorphism. Both fulfill all six requirements, including least identification and initiality in their stated categories.

A causal process and all its practice records can be held fixed while either abstract presentation is considered; the extra mathematical specification need not alter that process. The two subjects have different truths, but this is **not** a counterexample with one mathematical proposition reinterpreted covertly. It is a counterexample to **unique subject selection by the six generic requirements**. A theory admitting both subjects remains possible.

If the root explicitly fixes the empty equation set, then it does select the free unary term algebra. That positive theorem should be accepted. To encompass quotients, arithmetic operations and other subjects, it must subsequently justify the additional constructions and identifications. Saying “use the least structure” without naming the rule set does not complete that work.

More generally, for an underlying carrier \(X\), seed \(S\subseteq X\) and rule collection \(\mathcal R\), the least closed set is

\[
\operatorname{Cl}_{\mathcal R}(S)
=\bigcap\{Y\subseteq X:S\subseteq Y\text{ and }Y\text{ is }\mathcal R\text{-closed}\}.
\]

Its minimality is real, but indexed to \(X,S,\mathcal R\). For \(X=\{a,b\}\), seed \(\{a\}\), no rules give \(\{a\}\); adding the rule \(a\Rightarrow b\) gives \(\{a,b\}\). Both are exactly least. Minimality does not choose its own closure relation.

## U3. Strong compositional closure still does not select Boolean logic

Let

\[
H_2=\{0,1\},\qquad H_3=\{0,u,1\},\quad0<u<1.
\]

In both finite chains set

\[
x\wedge y=\min(x,y),\quad x\vee y=\max(x,y),
\]

\[
x\Rightarrow y=
\begin{cases}1&x\leq y,\\y&x>y,\end{cases}
\qquad\neg x=x\Rightarrow0.
\]

Both satisfy the following stronger criteria:

- All operations are total, finite and exactly evaluable.
- Each has all joins and meets, including those of arbitrary subsets of its carrier.
- Implication is characterized by the same exact compositional law
  \(z\wedge x\leq y\iff z\leq(x\Rightarrow y)\).
- Every monotone self-map has a least fixed point.
- Given atomic values, every finite formula has a uniquely determined value by structural recursion.

For the implication law, if \(x\leq y\), both sides hold for every \(z\); if \(x>y\), the left side holds exactly when \(z\leq y\), which is the right side. For fixed points, start at \(x_0=0\) and put \(x_{n+1}=f(x_n)\). Monotonicity gives an ascending sequence; finiteness forces stabilization. Induction shows every iterate lies below every fixed point, so the stabilized value is the least one. These are direct proofs for the displayed algebras.

Nevertheless,

\[
\forall p\in H_2\quad p\vee\neg p=1,
\qquad
u\vee\neg u=u<1\text{ in }H_3.
\]

Thus completeness of this order, compositional exactness, residual implication and availability of all monotone least fixed points **jointly** do not entail Boolean validity. This is not merely a shortage of finite observations or an omitted grounding label.

The shared \(\{0,1\}\) subalgebra has the same operations in both regimes; shared already interpreted arithmetic can remain unchanged. The counterexample concerns a selection principle for logical validity. It does not refute a common root that admits both regimes, does not reinterpret their intermediate values as uncertainty, and does not show that classical logic is false.

A universal account has two constructive options: derive an additional principle selecting the intended regime for a subject, or explain why multiple regimes are admissible and preserve their distinct judgments. Either option requires more than these generic closure properties. The earlier [primary-source comparison](MATHEMATICS-CONSTITUTION-RIVALS.md#5-what-established-foundational-alternatives-actually-show) explains why categorical and type-theoretic foundations likewise state substantive extra conditions rather than deriving every logic from composition alone.

## U4. The same arithmetic can support different quantified domains

Keep **exactly the same** first-order arithmetic structure \((\mathbb N,0,S,+,\times)\), with all its first-order truths. Add a sort of admissible subsets of \(\mathbb N\), ordinary membership and finite Boolean set operations. Compare

\[
\mathcal B_{\mathrm{fc}}
=\{X\subseteq\mathbb N:X\text{ is finite or cofinite}\},
\qquad
\mathcal B_{\mathrm{all}}=\mathcal P(\mathbb N).
\]

Both contain every singleton, the empty set and \(\mathbb N\); both are closed under finite unions, finite intersections and complements. Membership and every operation are exact. Both are closed under successor image and inverse image, and under the positive monotone operation

\[
F(X)=\{0\}\cup\{n+2:n\in X\}.
\]

Yet the two-sorted sentence

\[
\exists X\;\forall n\in\mathbb N\quad
\bigl(n\in X\iff(n=0\ \lor\ \exists m\;(n=m+2\land m\in X))\bigr)
\]

is true in the full-subset expansion and false in the finite/cofinite expansion. To prove this, any solution must contain 0, omit 1, and have \(n+2\in X\iff n\in X\); induction forces precisely the even numbers. That set and its complement are infinite, so it belongs only to \(\mathcal B_{\mathrm{all}}\).

The missing ingredient is especially visible in the construction: starting at \(\varnothing\), every finite iterate of \(F\) is an admitted finite set. Their union is the even numbers and is not in \(\mathcal B_{\mathrm{fc}}\). Thus admitting each finite stage, preserving all arithmetic, and admitting the same positive construction operation do not themselves admit its completed least fixed point.

Requiring closure under these increasing countable unions excludes the finite/cofinite expansion. That would be a genuine added condition, with a precise consequence. It still would not automatically imply full power-set closure. In ZFC, for an uncountable carrier \(U\), the countable/co-countable subsets form a collection closed under complements and countable unions and containing every singleton. For \(U=\mathcal P(\mathbb N)\times\{0,1\}\), the subset \(\mathcal P(\mathbb N)\times\{0\}\) and its complement are both uncountable, so this subset is missing. Full \(\mathcal P(U)\) admits it. Stronger closure levels need separate justification.

Again, the expanded quantified subjects differ because their set domains differ. This is not a same-content contradiction. It demonstrates that a shared base, including **every ordinary first-order arithmetic truth**, does not select the scope of higher quantification. The universal theory can include both indexed domains while still owing an account of admissibility and closure.

## U5. One unrestricted set-sized totality cannot close the universal problem

Suppose a proposed set-sized domain \(U\) can encode **every** subset of itself, with an exact decoding function

\[
d:U\twoheadrightarrow\mathcal P(U).
\]

Define \(D=\{x\in U:x\notin d(x)\}\). Surjectivity gives \(a\in U\) with \(d(a)=D\). Then

\[
a\in D\iff a\notin d(a)\iff a\notin D,
\]

a contradiction. Hence no such set-sized exact coding exists. The familiar proposal \(\mathcal P(U)\subseteq U\) is a special case: decode a member of \(U\) that is a subset of \(U\) as itself, and decode every other member as \(\varnothing\).

This is a genuine no-go for one specified form of universal closure. It does not block a hierarchy, a proper-class account, a schema of domains or a modal description of all structures. Those alternatives must keep their size and comprehension rules explicit. Moving to a wider level addresses a particular bound; it does not establish that a single self-enclosing totality has been produced.

## U6. Equivalence and shortest description require a declared comparison

An equivalence of categories is meaningful evidence of shared structural content, but the content being preserved must be specified. Here is a small exact warning against using an unqualified equivalence criterion.

Let \(C\) have one object and its identity arrow. Let \(D\) have two distinct objects and exactly one arrow between each ordered pair; composition is forced. The unique functor \(D\to C\) is fully faithful and essentially surjective, so the categories are equivalent. But the ordinary first-order statement “there are two unequal objects” is false in \(C\) and true in \(D\).

This is not a defect of categorical equivalence: literal multiplicity of isomorphic representatives is intentionally discarded. It shows that an explanatory equivalence must state which distinctions are meaningful and preserve those, including any designated interpretation. Equivalence of appropriately structured presentations can settle mathematical sameness. It does not, without a further argument, establish that one equivalent presentation grounds another, or that all ultimate rivals have been exhausted.

Likewise, “the shortest root” is not yet a language-independent selector. Any finitely written candidate theory \(T\) can be made a one-token invocation in a language containing a macro whose expansion is \(T\). This is a faithful abbreviation, but its apparent shortness disappears when the dictionary cost is counted. A rival finite theory can be abbreviated in the same way. Counting axioms has the same problem: finitely many axioms can be combined into one conjunction.

This does not rule out informative economy comparisons. It requires a fixed or explicitly costed language, an admissible family of transformations, and a criterion that counts the data and semantic commitments being imported. Under those conditions one candidate may win. Generic minimality or arbitrary compression cannot establish unique ultimate explanation.

## What is now settled, and what would change the conclusion

| Inference being assessed | Settled result | Remaining constructive route |
|---|---|---|
| Specified generation and semantics determine truth | Yes, at the declared structural and logical scope. | Recover more regimes with their inputs exposed. |
| Every nonempty set-sized first-order structure is representable generatively | Yes, using names and complete atomic tables; the companion proves this. | Derive informative structure without supplying the entire target diagram. |
| Leastness alone selects its own admissible rules | No; U2 supplies exact countermodels. | Independently derive or justify the rules and comparator category. |
| Strong compositional closure selects Boolean logic | No for the criteria of U3. | Additional logical principle or principled plural interpretation. |
| All finite constructions supply full infinite closure | No; U4 isolates the missing union and quantifier-domain principles. | State and justify successive closure commitments. |
| One set-sized self-power-closed totality contains everything | Impossible in the precise sense of U5. | A disciplined hierarchy, class, schema or modal account. |
| Necessary truth's extensional dependence uniquely identifies its ground | No; U1 makes the criterion non-specific. | A substantive account of explanatory dependence and its rivals. |
| Equivalent presentations or unqualified brevity establish unique metaphysical priority | No such implication follows; U6 specifies the missing comparison. | Content- and dependence-preserving equivalence, with explicit economy criteria. |

These boundaries are compatible with a strong **structural-modal generative foundation**. Such a theory can include classical and constructive regimes, finite and infinite domains, and distinct admissible presentations without choosing one structure as all of mathematics. The open question is whether the root explains the entire admission and interpretation scheme, rather than redescribing it after mathematics has supplied it.

A decisive positive development would derive a nontrivial closure, identity or logical principle from a smaller independently justified root, recover the intended subjects faithfully, and demonstrate a form of explanatory dependence that the rival account cannot match without comparable commitments. A decisive negative development would show that the proposed *specific* strengthened principles force a contradiction, fail intended coverage, or leave exactly the claimed selection undecided. More favorable examples cannot replace either argument.

The final attainable settled formulation from this round is:

> **Generative specifications, together with explicit identity, domain and semantic conditions, can determine mathematical structures and all their interpreted truths. This has universal representational scope for nonempty set-sized finitary first-order structures, and informative economical instances such as arithmetic. Generic generation, exact composition, minimal closure and extensional dependence do not by themselves establish a unique ultimate grounding of all mathematics. A universal structural-modal constitution remains a substantive research target whose admission and explanatory principles must still be justified.**

This finishes the inference audit and the available conditional mathematics. It does not label an unproved metaphysical proposition proved in order to call the task complete. The next named connection is **an independently justified generative principle → a specific nontrivial admissibility, identity or closure law**, assessed with the comparisons above.

**Verification:** all counterexamples and no-go arguments here are self-contained hand proofs; no new empirical evidence or machine verification is claimed. The external foundational comparisons used for context are primary-source checked in the linked rival-account note. Only this owned note was written; integration and the governing research index remain the parent study's responsibility.
