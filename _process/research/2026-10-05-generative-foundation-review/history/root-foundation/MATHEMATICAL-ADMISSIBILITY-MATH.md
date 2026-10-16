# Conservative completion from finite approximations

6 October 2026. AI-authored hand proofs for **finite generative articulation → coherent approximation → an explicitly justified completion**. This follows the [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md). Finite construction, mathematical comparison and completion are practices and structures investigated within generative activity. Their mathematical separation does not posit a completed world independently supplied to an external observer.

The [closure resolution](MATHEMATICS-CLOSURE-RESOLUTION.md) already proves least finite-rule closure, least identity and conditional truth determination; it separately characterizes full subset admission. The [identity study](IMMANENT-MATHEMATICAL-IDENTITY-MATH.md#6-compatible-descriptions-and-their-realization) already distinguishes compatible finite descriptions from their realization in an original carrier. This note adds an exact positive construction between those results: **ideal completion**, its universal property, and conditions that force a proposed completion to be this one. The construction is standard domain theory, not new mathematics or a new Lean development. Its explanatory application and limitations are the work here.

The proof takes place in ordinary classical set-based mathematics; ZFC suffices. The approximation order, all subsets used to define ideals, directed completeness and mathematical logic are explicit premises. The result does not derive unrestricted completion from finite generation alone. Nor does a mathematical ideal automatically establish an actually infinite physical history or a uniquely necessary metaphysics.

## 1. The information carried by an approximation order

Let \((P,\leq)\) be a nonempty set-sized partial order. Its elements represent the declared finite approximations or partial constructions, and \(p\leq q\) means that \(q\) extends the information or construction expressed by \(p\). The order interpretation must be independently justified for its application. An arbitrary order does not make its elements physically finite or effectively describable merely because they are called approximations.

A nonempty subset \(A\subseteq P\) is **directed** when any two of its members have a common upper bound that also belongs to \(A\). Equivalently, every nonempty finite subset of \(A\) has such a bound. Directedness expresses joint extension within this particular family. It is stronger than saying that every pair has some upper bound somewhere in a larger universe.

An **ideal** is a nonempty directed lower set \(I\subseteq P\): if \(q\in I\) and \(p\leq q\), then \(p\in I\). Write

\[
\operatorname{Idl}(P)=\{I\subseteq P:I\text{ is a nonempty directed lower set}\},
\qquad
\eta(p)=\mathord\downarrow p=\{q:q\leq p\}.
\tag{A1}
\]

Order \(\operatorname{Idl}(P)\) by inclusion. Lower closure retains what an admitted approximation already includes; directedness says the admitted partial contents fit within further admitted partial contents. Neither clause says every pair of conceivable alternatives must be jointly admitted. Incompatible branches can remain different ideals.

A partially ordered set \(D\) is a **dcpo** when every nonempty directed subset has a supremum. An element \(k\in D\) is **compact** when, for every nonempty directed \(A\subseteq D\),

\[
k\leq\sup A\quad\Longrightarrow\quad
\exists a\in A\ (k\leq a).
\tag{A2}
\]

Here compactness expresses a finite-witness property relative to the order: a compact approximation cannot first become included only at the completion of a directed development. It is not topological compactness of a physical region, finite duration, or a claim that an entire completed result has a finite description.

Our directed sets are nonempty throughout. Thus a dcpo need not have a least element. If \(P\) has a least element \(\bot\), then \(\downarrow\bot\) is the least ideal; the examples below have such an element. Admitting the empty ideal would be a different convention adding a new point below every nonempty ideal, including below \(\downarrow\bot\) when \(P\) already has a least element.

## 2. A completion with exactly the original compact approximations

### Theorem A1 — Directed completion, conservation and compact generation

For every nonempty poset \(P\):

1. \(\eta:P\to\operatorname{Idl}(P)\) is an order embedding.
2. \(\operatorname{Idl}(P)\) is a dcpo, and the supremum of a nonempty inclusion-directed family of ideals is its union.
3. Its compact elements are exactly the principal ideals \(\downarrow p\).
4. Every ideal is the directed supremum of the principal ideals it contains:
   \[
   I=\bigcup_{p\in I}\mathord\downarrow p.
   \tag{A3}
   \]

**Proof.** A principal lower set is nonempty and directed, because its generator is an upper bound for all its members. Moreover \(\downarrow p\subseteq\downarrow q\) iff \(p\leq q\), which proves 1.

For a nonempty directed family \(\mathcal D\subseteq\operatorname{Idl}(P)\), its union is nonempty and lower. Given two elements of the union, select ideals containing them, then an ideal of \(\mathcal D\) containing both selected ideals. Directedness inside that ideal supplies a common upper bound in the union. Thus the union is an ideal, and inclusion makes it the supremum. This proves 2.

If \(\downarrow p\subseteq\bigcup\mathcal D\), the element \(p\) lies in one member \(J\in\mathcal D\). Lower closure gives \(\downarrow p\subseteq J\), proving that every principal ideal is compact. For an arbitrary ideal \(I\), its principal subideals form a nonempty directed family: a common upper bound for \(p,q\in I\) also gives a principal ideal containing \(\downarrow p\) and \(\downarrow q\). Their union is \(I\), establishing 4. If \(I\) is compact, apply compactness to this family to obtain \(I\subseteq\downarrow p\) for some \(p\in I\). The reverse inclusion holds by lower closure, so \(I=\downarrow p\). This proves 3. ∎

A dcpo whose every element is the directed supremum of its compact elements below it is called **algebraic**. A1 therefore says that the completion is algebraic and introduces no additional compact elements. It adds possible coherent total profiles without creating new finite approximations or changing their old comparisons.

If a finite nonempty set of elements of \(P\) has a least upper bound in \(P\), its principal image is also the least upper bound of their principal ideals. Indeed, any ideal containing those finitely many elements contains a common upper bound for them, and consequently contains their least upper bound by lower closure. This is a further finite-order conservation result, not preservation of arbitrary existing infinite suprema.

For example, if \(P=\mathbb N\cup\{\omega\}\) already has \(\omega\) as the supremum of its natural numbers, then

\[
\sup_n\eta(n)=\mathbb N
\quad\ne\quad
\eta(\omega)=\mathbb N\cup\{\omega\}.
\tag{A4}
\]

Ideal completion treats every element of the supplied \(P\), including its old \(\omega\), as a compact generator. It does not preserve an old infinite-limit identification unless the specification separately requires it. Thus “conservative” here means the stated approximation comparisons and finite consequences, not every infinitary commitment one could attach to the same symbols.

It is also **not full first-order truth conservativity**. The unary finite-word order \(\{\epsilon,a,a^2,\ldots\}\) satisfies “every element has a strictly larger element.” Its ideal completion adds a greatest element \(a^\infty\), so that sentence becomes false when its quantifier ranges over the completed domain. Old comparisons are preserved; the range of quantified statements has changed.

## 3. Why this completion is free for directed-continuous interpretation

A map between dcpos is **Scott-continuous** here when it is monotone and preserves all nonempty directed suprema. No appeal to a topology is needed for the following proof.

### Theorem A2 — Unique extension of a monotone finite interpretation

For every dcpo \(D\) and monotone map \(f:P\to D\), there is a unique Scott-continuous map

\[
\bar f:\operatorname{Idl}(P)\longrightarrow D
\quad\text{with}\quad \bar f\circ\eta=f.
\tag{A5}
\]

It is given by

\[
\bar f(I)=\sup\{f(p):p\in I\}.
\tag{A6}
\]

**Proof.** The image \(f[I]\) is nonempty and directed by monotonicity, so the supremum exists. Inclusion of ideals implies the corresponding inequality of suprema. At a principal ideal, \(f(p)\) is the maximum image value, hence \(\bar f(\downarrow p)=f(p)\).

If \(\mathcal D\) is an inclusion-directed nonempty family of ideals, both \(\bar f(\bigcup\mathcal D)\) and \(\sup_{I\in\mathcal D}\bar f(I)\) are the least upper bound of all \(f(p)\) with \(p\in\bigcup\mathcal D\). Thus \(\bar f\) preserves the directed supremum. Finally, any other continuous extension \(g\) must, by (A3), satisfy

\[
g(I)=\sup_{p\in I}g(\eta(p))
=\sup_{p\in I}f(p)=\bar f(I).
\]

This proves uniqueness. ∎

The universal property specifies both its maps and its objects. It says that once finite interpretation and directed-supremum preservation are fixed, the interpretation of all completed profiles has no remaining freedom. It does not prove that every interpretation should preserve those suprema, or that every intended mathematical structure is an algebraic dcpo with this basis.

### Corollary A2a — Positive finite information has a unique extended reading

For a fixed \(p\in P\), map an approximation \(q\) to 1 when \(p\leq q\) and to 0 otherwise, using the ordered two-element dcpo \(0<1\). This map is monotone. Its unique continuous extension answers 1 at an ideal \(I\) exactly when \(p\in I\).

**Proof.** Formula (A6) takes the supremum of these Boolean values. It is 1 iff some \(q\in I\) has \(p\leq q\), which is equivalent to \(p\in I\) by lower closure and reflexivity. ∎

These positive finite readings separate distinct ideals. The conclusion does not identify every truth predicate with a continuously decidable finite observation. For example, the property “this word is infinite” is false at every finite prefix and true at their infinite supremum, so its Boolean indicator does not preserve that directed supremum. Negated or endpoint questions likewise require their own interpretation and evidence contract.

Nor can arbitrary operations on old histories be extended by invoking A2 without checking monotonicity. On binary finite words, right-appending 1 sends \(\epsilon\leq0\) to 1 and 01, which are not ordered by prefix. Thus chronological right-append does not satisfy this theorem's premise. Prefixing a fixed word does preserve prefix order on the full word language; a restricted language would additionally have to be closed under that operation. Existing action laws are not automatically continuous interpretations of the chosen approximation order.

## 4. Requirements that force a proposed completion to have this form

The universal property has an equivalent concrete representation theorem. This is useful because it locates the explanatory work in separate, assessable conditions rather than solely in the name “completion.”

### Theorem A3 — Compact approximation and full directed admission force unique completion

Suppose a dcpo \(D\) comes with an order embedding \(e:P\to D\), such that:

1. Every \(e(p)\) is compact in \(D\).
2. For every \(x\in D\), the set
   \[
   P_x=\{p\in P:e(p)\leq x\}
   \tag{A7}
   \]
   is nonempty and directed, and \(x=\sup e[P_x]\).

Then \(D\) is uniquely order-isomorphic to \(\operatorname{Idl}(P)\) by an isomorphism preserving every named approximation. Explicit inverse maps are

\[
\Phi(x)=P_x,
\qquad
\Psi(I)=\sup e[I].
\tag{A8}
\]

Conversely, \(\operatorname{Idl}(P)\) with its principal embedding satisfies these requirements. Consequently the requirements characterize the completion exactly, up to the unique isomorphism fixing \(P\).

**Proof.** Each \(P_x\) is lower because \(e\) is monotone, and is nonempty directed by the premise, so \(\Phi\) lands in the ideal completion. Every \(e[I]\) is nonempty directed, giving \(\Psi\).

For any ideal \(I\), if \(p\in I\), then \(e(p)\leq\sup e[I]\), so \(I\subseteq\Phi\Psi(I)\). Conversely, if \(p\in\Phi\Psi(I)\), compactness of \(e(p)\) gives \(q\in I\) with \(e(p)\leq e(q)\). Order reflection gives \(p\leq q\); lower closure gives \(p\in I\). Thus \(\Phi\Psi(I)=I\). The second requirement gives \(\Psi\Phi(x)=x\). Both maps are monotone, so they are inverse order isomorphisms, and \(\Psi(\downarrow p)=e(p)\).

Any order isomorphism fixing these approximations preserves their directed suprema, and every ideal has the representation (A3). Its value at every ideal must therefore be (A8); uniqueness follows. The converse is A1. ∎

The roles are precise:

* **Order embedding** preserves and reflects the established finite comparison structure.
* **Compactness** prevents a finite approximation from appearing below a completed supremum without being witnessed at an earlier member of that directed family.
* **Directed approximation of every element** rules out added completed distinctions invisible to all the admitted finite approximations.
* **Full directed completeness of \(D\)** admits a supremum for every nonempty directed family of those approximations, including families with no effective description.

The last condition is substantive admission content. Indeed, for each ideal \(I\), the proof explicitly uses that condition to construct \(\Psi(I)\). A3 does not eliminate the need to justify admitting every such coherent profile. It shows that **if these independently motivated requirements are accepted together, they leave no further choice of completion over \(P\)**. Calling an object generative or coherent alone does not establish the requirements.

Two small examples show that the requirements do distinct work. First, let \(P=D=\mathbb N\cup\{\omega\}\) with its usual order and let \(e\) be the identity. This is a dcpo, the embedding is faithful, and every element is the supremum of its directed set of named predecessors. But \(e(\omega)\) is not compact: the natural numbers have supremum \(\omega\) without any member above it. The distinct ideals \(\mathbb N\) and \(\mathbb N\cup\{\omega\}\) both map to \(\omega\) under \(I\mapsto\sup e[I]\), so omitting compactness loses the asserted faithful completion. Second, let \(P\) have one element and embed it as 0 in the two-element chain \(D=\{0<1\}\). Both the dcpo and compact-embedding conditions hold, but 1 is not the supremum of the named approximations below it. Omitting directed generation permits that extra element, whereas \(\operatorname{Idl}(P)\) has only one element.

## 5. Finite histories and their possible infinite extensions

Let \(\Sigma\) be an alphabet and \(H\subseteq\Sigma^*\) a nonempty prefix-closed language of admitted finite histories, ordered by prefix. Prefix closure includes the empty word. Set

\[
\partial H=\{\alpha\in\Sigma^{\mathbb N}:\alpha\mathbin{\upharpoonright}n\in H\text{ for every }n\}.
\tag{A9}
\]

### Proposition A4 — Ideal completion of a history tree

The ideals of \(H\) are exactly:

1. the prefixes of one finite word \(w\in H\); and
2. the finite prefixes of one infinite word \(\alpha\in\partial H\).

Thus \(\operatorname{Idl}(H)\) is order-isomorphic to \(H\cup\partial H\), with the usual finite/infinite prefix order.

**Proof.** Two words in one directed ideal have a common extension in the ideal, so they are comparable by prefix. The ideal is therefore a nonempty chain. If its lengths are bounded, it has a member of greatest length. Lower closure makes the ideal exactly that word's prefixes. If lengths are unbounded, comparability makes the letters at each coordinate consistent; their union is a unique infinite word. Every finite prefix occurs in the ideal, by unboundedness and lower closure, and thus belongs to \(H\). Conversely, the prefixes of a finite admitted word or an infinite word in (A9) form a nonempty directed lower set. The classification preserves and reflects inclusion and prefix order. ∎

For \(H=\Sigma^*\), this gives every finite and infinite word. For a history law excluding a finite prefix, it excludes every infinite word with that prefix. Infinite histories are therefore constrained by the finite generation relation; their admission is not arbitrary. But admitting the entire boundary (A9) is an additional completion commitment, rather than execution of infinitely many finite rules in finite time.

The application depends critically on what a history retains. If labels omit conditions needed to lift later steps consistently, an abstract infinite word may fail to represent any single concrete history.

### Counterexample A4a — Every finite observable prefix without one infinite run

There is one initial state \(r\). An event labeled \(c\) takes it to \((n,0)\) for any chosen finite budget \(n\in\mathbb N\). A tick labeled \(a\) takes \((n,k)\) to \((n,k+1)\) when \(k<n\), and no tick is possible at \((n,n)\). There is no replenishment operation. The \(c\) transition is infinitely branching; no finite budget is an infinite budget.

Every finite word \(ca^m\) is executable by choosing a budget \(n\geq m\), so the projected observable history language is \(H=\{\epsilon\}\cup\{ca^m:m\in\mathbb N\}\). Its ideal completion includes \(ca^\infty\). But no concrete execution is infinite: after the first transition chooses \(n\), every run has at most \(n\) ticks.

The failure is an exchanged quantifier:

\[
\forall m\ \exists n\ \text{a run of length }m
\quad\not\Rightarrow\quad
\exists n\ \text{an infinite run}.
\tag{A10}
\]

If the finite history instead retains which budget was initialized, the branches are already differentiated by that information, and none has unbounded tick length. The ideal \(ca^\infty\) came from a projection that forgot this consequential relation. Equivalently, begin just after the hidden choice with the infinite initial-state family \(\{(n,0):n\in\mathbb N\}\); its tick-only language is \(\{a^m:m\in\mathbb N\}\), whose ideal completion includes \(a^\infty\). The counterexample concerns the adequacy of that projection for infinite-run claims, not evidence against the full generative account. It is a dynamic instance of the [previous compatible-profile realization gap](IMMANENT-MATHEMATICAL-IDENTITY-MATH.md#6-compatible-descriptions-and-their-realization), not a newly discovered general limit on finite consistency.

### Proposition A4b — A sufficient concrete lifting condition

Fix a labeled transition system with finitely many possible initial states, at least one of them, and finitely many successors under each specified label from every state. Require any additional obligations imposed on admitted finite histories to be prefix-closed. If every finite prefix of a fixed infinite word \(\alpha\) has an admitted concrete run from one of those initial states, then one infinite concrete run has labels \(\alpha\), with every finite prefix admitted.

**Proof.** Form the tree of all admitted finite concrete runs matching a prefix of \(\alpha\), adding one root above the finitely many initial states. Prefix closure makes this a tree of the stipulated histories. Each node has finitely many children and every finite depth is represented. Starting at the root, select a child with descendants at arbitrarily large depths; such a child exists because there are finitely many children. Repeat. The resulting branch is an infinite concrete run with the specified labels, and each of its finite prefixes is admitted. This is the classical finitely branching tree argument. ∎

The main finite-budget counterexample violates finite branching at its \(c\) transition; its post-choice presentation violates the finite-initial-state premise. A4b establishes existence of a mathematically consistent run under the supplied transition law; it is not an observation that a physical infinite run has occurred or a proof that the transition law remains correct forever. It proves no additional limit-only obligation merely from the admitted finite prefixes. Where outputs or resources affect continuation, the concrete states and labels in the lifting claim must preserve those relations.

## 6. Full subsets from finite subset approximations

Let \(D\) be any set and \(P=\mathcal P_{\mathrm{fin}}(D)\), ordered by inclusion and including the empty finite subset.

### Proposition A5 — Ideal completion recovers the full powerset

There is a canonical order isomorphism

\[
\operatorname{Idl}(\mathcal P_{\mathrm{fin}}(D))\cong\mathcal P(D),
\qquad
I\longmapsto\bigcup I,
\qquad
S\longmapsto\mathcal P_{\mathrm{fin}}(S).
\tag{A11}
\]

**Proof.** The finite subsets of \(S\) form a nonempty lower directed family: it contains the empty set and combines two members by their union. Its union is \(S\). Conversely, set \(S=\bigcup I\) for an ideal \(I\). Every member of \(I\) is a finite subset of \(S\). If \(F\subseteq S\) is finite, select for each element of \(F\) a member of \(I\) containing it. Directedness combines these finitely many members into an upper bound in \(I\), and lower closure puts \(F\) in \(I\). The empty \(F\) belongs to \(I\) because the ideal is nonempty and lower. Hence \(I=\mathcal P_{\mathrm{fin}}(S)\). Both maps preserve inclusion. ∎

This gives a positive completion account of the full subset sort. It does not derive full powerset admission using only finite unions. The additional directed family \(\mathcal P_{\mathrm{fin}}(S)\) exists for **each external subset \(S\subseteq D\)**, whether or not it has a finite name or computable presentation. The full directed-completeness requirement admits its supremum. In this basis, that admission is as strong as the full subset realization proved separately in [closure resolution P1–P3](MATHEMATICS-CLOSURE-RESOLUTION.md#5-full-subsets-have-a-positive-uniqueness-theorem-of-their-own).

The construction is informative because it identifies how each completed subset relates to its finite approximations and why the result is unique under those conditions. It would be circular to present the quantification over all such directed families as already explained merely by invoking finite generativity. The same caution applies when \(D\) is uncountable: the finite subsets can have uncountably many possible elements, and the premise supplies that base domain.

## 7. Effective construction and full admission remain different

For \(P=\mathcal P_{\mathrm{fin}}(\mathbb N)\), unions of computably generated increasing sequences of finite sets are exactly the computably enumerable subsets of \(\mathbb N\). In one direction, enumerate the finite sets stage by stage. In the other, take the finite set enumerated by a given enumerator through each stage. Both constructions use a fixed ordinary program model and effective encodings of finite sets.

There are subsets of \(\mathbb N\) outside this class. For example, enumerate all computably enumerable sets as \(W_0,W_1,\ldots\) and set \(A=\{i:i\notin W_i\}\). If \(A=W_j\), its membership at \(j\) contradicts that defining equation. Thus \(A\) is not computably enumerable.

Every finite subset of \(A\) remains an admitted finite approximation, and the mathematical sequence

\[
F_n=A\cap\{0,\ldots,n\}
\tag{A12}
\]

is increasing with union \(A\). It is not thereby a computably supplied sequence. Requiring suprema for **all mathematical increasing sequences** of finite subsets of \(\mathbb N\) already requires every subset of \(\mathbb N\), because (A12) is available for each of them in the ambient set theory. Restricting to effective sequences yields a different admission contract, which does not satisfy A3's full dcpo premise.

Consequently “every finite approximation is constructible,” “a completed profile is effectively generated,” and “every directed profile is admitted” have different mathematical contents. A completion theorem can relate them under explicit premises; it cannot equate them by terminology. The existence of non-effective ideals does not show that finite descriptions cannot denote a completion as a whole, only that such a description does not give an effective enumeration or individual finite name for every member.

## 8. What this establishes for the mathematical-root bridge

The positive result is stronger than an arbitrary permission to append infinite objects: finite approximation order, compactness, directed generation and full directed admission force one completion over the given basis. Every completed element has exactly its coherent finite profile, and every interpretation preserving directed development is fixed by its finite interpretation. This is a precise case of mathematical identity and extension being constrained by generative relations.

The remaining admission premise is equally precise. Finite generation does not select full directed completeness rather than an effective, bounded, physically realized or otherwise restricted class of continuations. Nor does one completion construction cover every mathematical subject without additional representations and constraints. The general theorem remains valid if the theory independently justifies its premises; it does not make those premises disappear.

Three different conclusions must therefore be kept apart:

1. **Mathematical conservative completion:** A1–A3 establish the exact object and universal property relative to a specified approximation order and completion contract.
2. **Realization of an abstract continuation:** A4a–A4b identify when a completed history profile need not, or does, lift to one concrete run under a stated transition law.
3. **Philosophical admissibility:** explaining why the relevant mathematical subject should admit every ideal, and why that mode of admission follows from the proposed root rather than an equally adequate alternative, needs an argument at that scope.

This classification does not posit three independent realms. It separates three claims about related aspects of the same investigation, so evidence for one is not silently counted as evidence for all. A projection missing the budget relation requires representational correction; lack of a justified full-admission principle is a remaining explanatory obligation; a counterexample satisfying A3's premises but violating its conclusion would refute the proof. These are different revision conditions.

## 9. Antecedents and verification scope

The mathematical mechanisms are standard ideal completion and algebraic-domain representation. Abramsky and Jung's *Domain Theory* (1994), §2.2.6, is the classical antecedent; [the authors' publication record](https://ora.ox.ac.uk/objects/uuid%3A447e1def-cc66-4d2b-b4f2-b6ddc5f0ca02) identifies the handbook chapter. The [source companion](MATHEMATICAL-ADMISSIBILITY-SOURCES.md) records the source-review agent's successful direct inspection of the author-hosted corrected and expanded PDF, including §2.2.6, printed pp. 26–28. The proof-writing pass also read Tom de Jong's primary [ideal-completion construction](https://martinescardo.github.io/TypeTopology/DomainTheory.IdealCompletion.IdealCompletion.html) and [properties](https://martinescardo.github.io/TypeTopology/DomainTheory.IdealCompletion.Properties.html), which explicitly track logical assumptions and the size of directed families. These sources concern a more general abstract-basis formulation; this note proves the ordinary poset specialization directly.

The hand proofs above establish the declared propositions without importing a new runtime or claiming that source code from another project was compiled here. This note adds no empirical experiment, physical infinite execution or new Lean verification. Local validation should check the displayed arguments, source correspondence and limits, rather than treating finite enumerations as proof that every infinite ideal is realized.
