# Contextual identity, composed operations and expanding participation

6 October 2026. AI-authored hand proofs for the named connection **retained distinctions → compositional identity → revision when the action and question interface expands**. This follows the [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md) and [core/tree continuation](CORE-TREE-CONTINUATION.md). State, operation, question and retained description are analytical distinctions within the relevant generative configuration; the mathematics does not posit independent observer and world substances.

The prior [structural results, M1 and M7](MATHEMATICS-STRUCTURAL-RESULTS.md) already establish the coarsest deterministic behavioral quotient and refinement under richer outputs. The [acquisition proof](ABSTRACTION-ACQUISITION-MATH.md) already shows a learner acquiring a finite quotient under its explicit testing and state-bound premises. This note extends the interface analysis to partial actions, jointly enlarging actions and questions, operation identity, and compatible families of successively finer quotients. These are self-contained applications of established congruence, transition-monoid and inverse-limit arguments. No mathematical priority, new empirical run or new Lean verification is claimed.

The positive result is exact: an expanded interface preserves an older exact identity by a canonical projection, while it can require finer distinctions for further composition. A compatible infinite family need not be realized by an original state. The latter limitation concerns an explicit realization question; it does not, by itself, refute a fuller generative account that includes such realizations.

## 1. The represented configuration and its interfaces

Fix a nonempty state set \(S\). A state retains all conditions relevant to the comparisons: changes in available support, other participating structures, clocks and histories must be included where they affect the specified future. For each action \(a\) in an ambient set \(\mathcal A\), supply a deterministic partial function

\[
\delta_a:S\rightharpoonup S.
\tag{I1}
\]

For each question \(j\) in an ambient set \(\mathcal J\), supply a total readout \(o_j:S\to O_j\). Different questions may have different answer sets. A finite or infinite interface is a pair \(I=(A_I,J_I)\) of selected actions and questions. Its allowed contexts are **all finite words** in \(A_I^*\). If only a restricted protocol is permitted, that protocol's control state must be represented or a separate context-closure contract proved; arbitrary restrictions do not inherit the congruence theorem automatically.

Write \(\delta_\epsilon=\mathrm{id}\), and let \(\delta_{uv}\) execute \(u\) and then \(v\). As partial functions,

\[
\delta_{uv}=\delta_v\circ\delta_u.
\tag{I2}
\]

Define the response to a word with a disjoint failure tag:

\[
\beta^I_s(w)=
\begin{cases}
\bot,&\delta_w(s)\text{ is undefined},\\
\left(\mathsf{defined},(o_j(\delta_w(s)))_{j\in J_I}\right),
 &\delta_w(s)\text{ is defined}.
\end{cases}
\tag{I3}
\]

The defined tag matters even when \(J_I\) is empty. This representation preserves word feasibility as well as endpoint answers. It does not presume that an arbitrary partial program's nontermination is decidably observable. An operational application must provide the stated feasibility/denial interface or use a weaker response contract.

An undefined action here has no successor in the permitted protocol. If an attempted action fails but changes the world, its failure and resulting state belong in the transition law; they must not disappear into \(\bot\). Likewise, a read that changes the configuration is an action with an outcome, rather than a costless external peek. These restrictions make the abstraction accountable for what it preserves and omits.

## 2. State identity that supports continued action

Define

\[
s\mathrel{E_I}t\quad\Longleftrightarrow\quad
\forall w\in A_I^*,\ \beta^I_s(w)=\beta^I_t(w).
\tag{I4}
\]

An output-respecting partial-action congruence is an equivalence relation \(R\) such that \(sRt\) implies:

1. \(o_j(s)=o_j(t)\) for every \(j\in J_I\);
2. for each \(a\in A_I\), \(\delta_a(s)\) is defined iff \(\delta_a(t)\) is defined;
3. when defined, \(\delta_a(s)R\delta_a(t)\).

### Theorem I1 — Greatest exact congruence

\(E_I\) is the greatest such relation under inclusion, hence the coarsest exact state partition. Its quotient \(Q_I=S/E_I\) carries the well-defined partial actions and questions

\[
\bar\delta^I_a([s]_I)=[\delta_a(s)]_I,
\qquad \bar o^I_j([s]_I)=o_j(s),
\tag{I5}
\]

where the quotient action is defined exactly when the original action is. Every finite response is preserved.

**Proof.** Equality of response functions is an equivalence relation. The empty word gives present-answer equality. The word \(a\) gives equal definedness because the tags are disjoint. If \(a\) is defined at both states, response equality for every word \(aw\), together with (I2), gives \(\delta_a(s)E_I\delta_a(t)\). Thus (I5) is independent of the representative. Induction on a word proves equality of its definedness and endpoint answers before and after quotienting.

Conversely, if \(sRt\) for a congruence \(R\), induction carries equal definedness and related successors along every word. At each defined endpoint the questions agree. Hence \(sE_It\), so \(R\subseteq E_I\). ∎

Present resemblance alone is insufficient. In a three-cycle with readings \(001\), the first two states have the same present reading but different readings after one action. They cannot be the same recursively usable state at that interface. This is the earlier acquisition study's concrete reason for adding a distinguishing suffix.

Theorem I1 establishes a semantic identity for a stated interface, not possession of an infinite response table. The distinction between an exact quotient and finite evidence for one remains the acquisition theorem's substantive concern.

## 3. Enlarging actions and questions

Write \(I\le K\) when \(A_I\subseteq A_K\) and \(J_I\subseteq J_K\), with the same underlying states and the same old action/readout laws. This is conservative enlargement of an interface. Replacing an old action law or changing a readout's meaning is a different operation and does not satisfy this premise merely because its label stays the same.

### Theorem I2 — Refinement and the canonical projection

If \(I\le K\), then \(E_K\subseteq E_I\), and

\[
p_{KI}:Q_K\longrightarrow Q_I,
\qquad [s]_K\longmapsto[s]_I
\tag{I6}
\]

is a well-defined surjection. It preserves every old question. For every old action, its domain is preserved and reflected, and, whenever the action is defined,

\[
p_{KI}(\bar\delta^K_a(q))
=\bar\delta^I_a(p_{KI}(q)).
\tag{I7}
\]

The projections compose: \(p_{LI}=p_{KI}\circ p_{LK}\) for \(I\le K\le L\).

**Proof.** Every old word and old question is also available in \(K\). Equality of richer responses therefore implies equality of old responses, including definedness. This proves inclusion and well-definedness. Every class has a representative, which proves surjectivity. All remaining assertions follow by applying (I5) to that representative. ∎

An action can reveal a distinction without adding a question. For example, with no original actions and one Boolean question, states \(x,y\) both reading zero are equivalent. Introduce an action taking \(x\) to a zero-reading state and \(y\) to a one-reading state. The expanded interface separates them. An action defined at \(x\) but undefined at \(y\) already separates them by feasibility. This differentiates new participation from simply attaching another static label.

### Corollary I2a — Strict refinement cannot be recovered from the old class alone

A function \(r:Q_I\to Q_K\) satisfying \(r([s]_I)=[s]_K\) for every \(s\) exists iff \(E_I=E_K\).

**Proof.** If the relations are equal, the class map is a bijection. If refinement is strict, some \(s,t\) share their old class but have different new classes; a function on that shared input cannot return both. ∎

A set-theoretic section of (I6), selecting one fine class per coarse class, is not such a recovery map for every actual state. New evidence, additional retained distinctions or restrictions on the admitted states can resolve a particular instance. When applying this impossibility to a learner, the old input must include **all accessible retained information relevant to recovery**, not merely a conveniently isolated summary while an available archive distinguishes the cases.

Thus an older model can have been fully correct for its interface while becoming insufficient for an enlarged one. Strict refinement is not automatically a correction of an earlier false claim. Conversely, an old claim that already purported to cover the new actions or questions can be genuinely refuted by their distinguishing result.

## 4. State identity is different from operation identity

Fix an initial state \(s_0\), and restrict to its reachable states under the chosen interface. This set is closed under defined actions. For executable histories \(h,h'\), residual identity is

\[
h\equiv_{\rm state}h'
\quad\Longleftrightarrow\quad
\forall y,\ \beta^I_{s_0}(hy)=\beta^I_{s_0}(h'y).
\tag{I8}
\]

It identifies the same reachable behavioral class and supports continuation on the right. It need not be preserved by prefixing another history. For the total deterministic recognizer of the language \(\{ab\}\), histories \(b\) and \(aa\) both have empty accepting residuals. But prefixing \(a\) yields \(ab\), which is accepted, and \(aaa\), which is not. The initial residual relation therefore cannot simply be used as a two-sided quotient of word concatenation.

To identify **operations**, let \(T_w\) be the partial transformation induced by \(w\) on the reachable quotient \(Q_I^{\rm reach}\). Define

\[
u\equiv_{\rm op}v
\quad\Longleftrightarrow\quad T_u=T_v
\tag{I9}
\]

as partial functions: domains agree, and outputs agree wherever defined.

### Theorem I3 — Two-sided contextual operation identity

Relation (I9) is a two-sided monoid congruence on \(A_I^*\). Equivalently,

\[
u\equiv_{\rm op}v
\quad\Longleftrightarrow\quad
\forall x,y\in A_I^*,\
\beta^I_{s_0}(xuy)=\beta^I_{s_0}(xvy).
\tag{I10}
\]

The quotient \(A_I^*/{\equiv_{\rm op}}\) acts faithfully by partial transformations on \(Q_I^{\rm reach}\). With chronological multiplication \(f\star g=g\circ f\), the assignment \([w]\mapsto T_w\) is an injective monoid homomorphism onto the transformations generated by the admitted actions. The empty word acts as the identity.

**Proof.** Equation (I2) holds on the quotient, so equality of partial transformations is preserved under both left and right composition. Its kernel on words is therefore a two-sided congruence; the induced representation is injective by the definition of that kernel.

If \(T_u=T_v\), every executable prefix reaches a class at which both words have the same definedness and, when defined, the same class. Every suffix then gives the same response by I1. An undefined prefix gives \(\bot\) on both sides. This proves the forward implication in (I10).

Conversely, every reachable state is reached by an executable prefix \(x\). Taking \(y=\epsilon\) in (I10) proves equal definedness of \(u\) and \(v\) there. If defined, taking every \(y\) proves contextual equivalence of their successor states, hence equality of their quotient values. Thus \(T_u=T_v\). ∎

For total actions this is the usual transition-monoid/syntactic-congruence construction. For partial actions the tagged definedness is essential. If the reachable quotient has \(m\) states, there are at most \((m+1)^m\) distinct partial transformations, or \(m^m\) in the total case; the generated image may be much smaller. This is a finite representational bound, not a claim about implementation expense or every mathematical operation.

When the interface grows on a **fixed action-closed comparison carrier**, the analogous operation identity for the common words can only refine: the richer quotient can distinguish transformations previously identified. With an initial-state formulation, expanded actions can also enlarge the reachable carrier; those additional starting states must be included. One must not silently keep the old reachable carrier while claiming the expanded all-context statement.

## 5. A directed family of interfaces

Let \((I_i)_{i\in D}\) be indexed by a nonempty directed partially ordered set: every finite group of indices has a common upper bound, and \(i\le k\) implies \(I_i\le I_k\). Set

\[
I_\infty=\left(\bigcup_i A_i,\ \bigcup_i J_i\right),
\qquad E_\infty=E_{I_\infty}.
\tag{I11}
\]

### Theorem I4 — Union identity is the intersection of finite-interface identities

\[
E_\infty=\bigcap_{i\in D} E_i.
\tag{I12}
\]

The interfaces \(I_i\) need not themselves be finite. The essential condition is that each tested context uses finitely many actions and each answer coordinate belongs to some interface.

**Proof.** I2 gives inclusion from left to right. Conversely, suppose \(sE_it\) for every \(i\). A word \(w\) in the union uses finitely many action labels. Directedness supplies a stage containing all of them, which proves equal definedness at \(s,t\). If defined, fix any union question \(j\). A common upper stage contains that question and every action in \(w\), so its answers agree. Every answer coordinate therefore agrees, giving (I3) at the union. ∎

Directedness matters because a mixed word can combine actions from different branches. Without a common interface admitting the combination, equivalence in each separate branch need not test that word. Likewise, equality on an arbitrary collection of finite experimental records is not (I12): \(E_i\) already quantifies over every finite context admitted by its interface.

## 6. Compatible descriptions and their realization

Let \(Q_i=S/E_i\), with the projections from I2. Define the inverse limit as the compatible families

\[
\varprojlim_i Q_i
=\{(c_i)_i:\ p_{ki}(c_k)=c_i\text{ whenever }i\le k\}.
\tag{I13}
\]

### Theorem I5 — Canonical injection and the exact onto condition

The map

\[
\iota:S/E_\infty\longrightarrow\varprojlim_i Q_i,
\qquad [s]_\infty\longmapsto([s]_i)_i
\tag{I14}
\]

is well defined and injective. It is onto iff every compatible family has a simultaneous realization:

\[
\forall(c_i)_i\in\varprojlim_iQ_i,\qquad
\bigcap_i\{s\in S:[s]_i=c_i\}\ne\varnothing.
\tag{I15}
\]

**Proof.** I12 gives well-definedness, and the projection identities give compatibility. Equal images imply \(sE_it\) for every \(i\), hence \(sE_\infty t\), so the map is injective. A compatible family is in its image exactly when one state represents all its coordinates, which is precisely (I15). ∎

Each individual projection is onto, and every finite part of a compatible family has a representative: choose a common upper index and a representative of that coordinate. Neither fact implies (I15) for an infinite family.

### Counterexample I5a — An unrealized infinite tail with a genuine action

Take \(S=\mathbb N\), the total action \(a(n)=n+1\), and questions \(q_k(n)=\min(n,k)\). At stage \(k\), retain this action and all questions with index at most \(k\). Then

\[
nE_km\quad\Longleftrightarrow\quad\min(n,k)=\min(m,k).
\tag{I16}
\]

Indeed, equality below \(k\) means the same number, while two numbers at least \(k\) keep answering \(k\) after any number of increments; all lower questions are determined as well. The quotient has \(k+1\) classes. Identify it with \(\{0,\ldots,k\}\); its action is \(r\mapsto\min(r+1,k)\), and the projection from a higher stage is truncation by \(\min(-,k)\).

The family \(c_k=k\) is compatible, but its representing fibers are \(\{n:n\ge k\}\), whose intersection is empty. Meanwhile \(E_\infty\) is equality on \(\mathbb N\). In fact the inverse limit adds exactly one extra profile, \(\infty\): a compatible profile with any coordinate strictly below its ceiling fixes one finite number at every stage; the only remaining possibility is the all-ceiling family. Its action fixes \(\infty\). Adding this new realization is a completion of the represented carrier, not evidence that a finite natural number already occupied it.

### Counterexample I5b — All finite bit descriptions without every infinite bitstream

Let \(S\) be the binary sequences that are eventually zero, equivalently finite binary descriptions padded with zeros. At stage \(n\), admit questions reading coordinates \(0,\ldots,n-1\) and actions flipping any one of those coordinates. Flips preserve \(S\). Contextual equivalence is exactly equality of the first \(n\) bits: all admitted actions change only those bits, and the questions already separate distinct prefixes.

Thus \(Q_n=\{0,1\}^n\), with prefix projections. The union distinguishes every pair of states, but the inverse limit is the set of **all** infinite binary sequences. Each finite prefix has an eventually-zero extension; the compatible all-ones sequence has none. This witness jointly expands action and question interfaces without claiming that finite evidence alone creates a new infinite realization.

### Proposition I6 — A sufficient compactness premise

If \(S\) carries a compact topology and every equivalence-class fiber \(\{s:[s]_i=c\}\) is closed, then \(\iota\) is onto.

**Proof.** For a compatible family, all its fibers are nonempty and closed. The common-upper-index argument gives the finite intersection property. Compactness yields a point in their full intersection, establishing (I15). ∎

Compactness and closed fibers are additional premises, not consequences of finite quotients or onto bonding maps. The ordinary topological compactness principle used here is part of the mathematical background. Changing the carrier to obtain it requires a realization argument at the intended application. The counterexamples show exactly what such an addition supplies; they do not show that no completion can be appropriate.

## 7. When a finite final identity is reached at a finite stage

### Proposition I7 — Finite final quotient implies eventual stabilization

If \(S/E_\infty\) is finite, there is an index \(i_0\) such that \(E_i=E_\infty\) for every \(i\ge i_0\). Consequently \(\iota\) is onto without a topological premise.

**Proof.** Choose one representative from each final class. Every distinct pair is separated at some stage by I12. There are finitely many pairs, so directedness supplies a common upper stage \(i_0\) separating all of them. Each \(E_i\) contains \(E_\infty\), so it cannot split a final class; at \(i_0\) it cannot merge distinct final classes either. Equality follows and persists at every higher stage.

Given any compatible family, choose a representative \(s\) of its \(i_0\)-coordinate. For any index \(j\), take \(k\ge i_0,j\). Since \(E_k=E_{i_0}\), compatibility forces the same final class at \(k\); projecting to \(j\) gives \([s]_j=c_j\). Thus \(s\) realizes the full family. ∎

Finite \(S\) is a sufficient special case. Finiteness of **each individual quotient** is insufficient, as both counterexamples show. A uniform finite bound \(N\) on all \(|Q_i|\) is sufficient: if the final quotient had \(N+1\) classes, finitely many pair-separating witnesses would force some stage to have at least \(N+1\) classes, a contradiction; then I7 applies.

This theorem stabilizes the identity relation, not the inventory of named questions or actions. New labels may arrive forever while acting on the same finite classes. It provides neither a computable deadline from arbitrary interface presentations nor a finite certificate that an unknown physical process satisfies the stated uniform bound. There are at most \(|S/E_\infty|-1\) strict increases along any chain of partitions beginning with at least one class, but arbitrarily many unchanged stages can precede a later refinement.

## 8. What a finite identity can make necessary

A word identity \(u\equiv_{\rm op}v\) is stronger than an observed coincidence on one history: it quantifies over every reachable starting class and every continuation of the fixed interface. On a supplied finite complete quotient it can be checked by comparing the induced partial transformations on every class. An actual learner's warrant for treating that table as complete still depends on its acquisition and correspondence conditions.

### Proposition I8 — Transport across faithful realizations

Fix a behavior structure \(K\) with specified partial actions, questions and a reachable carrier. Suppose a **nonempty** class of realizations \(\mathcal C\) comes with isomorphisms from each realization's reachable behavioral quotient to \(K\), preserving action domains, action values and the question maps. Then a word identity holds in one such quotient iff it holds in \(K\), iff it holds in every such realization.

**Proof.** Induction on words conjugates every induced partial transformation through each isomorphism, including its domain. Equality of two transformations is preserved and reflected under that conjugation. ∎

This is structural invariance across faithful realizations; it can concern differently named or materially different implementations. It is not obtained by declaring every realization faithful. The correspondence must be justified by its independently specified formation and behavior conditions. An isomorphism preserves all identities, including those that happen to hold only in this particular structure.

For example, with phase-distinguishing questions, a two-cycle validates \(aa\equiv_{\rm op}\epsilon\), while a three-cycle does not. Both are deterministic processes. Exhaustively verifying the two-cycle does not make the equation a law of all deterministic processes or of every mathematical subject. A theorem quantified over a class requires premises common to that class and an argument from them. A finite sound derivation can establish such an infinite-range theorem; a finite list of instances alone cannot.

The present account therefore distinguishes three scopes: identity throughout one exact quotient; invariance across its justified faithful realizations; and validity across a wider independently characterized class. These scopes develop within mathematical activity. They need not be ontologically independent realms, and none is automatically the unique ground of every mathematical truth.

## 9. The contribution and its revision conditions

The inherited acquisition mechanism supplies a concrete history in which actual discrepancies produce new suffix distinctions and a reusable finite update structure. This note explains how that structure remains exact for its old scope while a larger participation/query interface can demand refinement. Its added projection, operation and realization results strengthen the existing contextual-quotient account; they do not replace that historical acquisition by an analyst's precomputed partition.

What remains local input is explicit: a sufficiently rich state representation; deterministic stationary partial laws during the claim; meaningful and adequately available readouts; all-finite-word context closure; unchanged old semantics during interface expansion; the admitted index family; ordinary set, function and logical reasoning; and, where invoked, a finite bound or compact realization premise. These are not thereby entities outside generative reality. Their origin and adequacy must be explained within the wider account, rather than treated as discharged by notation or disclosure.

Three kinds of revision remain distinct. An omitted but consequential condition in \(S\) calls for a better representation. A need for finer distinctions under a genuinely richer interface revises the abstraction's practical scope without falsifying its former exactness. A counterexample satisfying a complete theorem's premises and violating its conclusion would refute the proof or implementation. The explicit infinite-family witnesses refute automatic realization in the stipulated carriers; they do not obtain that conclusion by freely toggling a predicate absent from the target relationship.

No theorem here says that all mathematical identity is exhausted by finite deterministic experiments, that preservation of behavior is an ethical criterion, or that retaining a quotient is costless. The local construction identifies a particular immanent relationship: continuing effects can support stable distinctions; those distinctions support repeated composition; expanded participation can require their differentiation; and compatible descriptions require a separate account of realization when an infinite completion is claimed.

For a primary antecedent, [Rutten, *Universal coalgebra: a theory of systems* (2000), §3.8, Proposition 5.8 and §8](https://ir.cwi.nl/pub/48/0048D.pdf), treats deterministic input/output systems, quotient transition structures and quotienting by greatest behavioral equivalence. Those passages were read in the primary PDF. They establish the mature mathematical setting, rather than attributing the present philosophical interpretation to Rutten. The full arguments above specify this note's exact partial-action and expanding-interface contracts; they do not rely on an unrestricted identification of trace equality and bisimulation for arbitrary nondeterministic systems.

The [independent review](IMMANENT-MATHEMATICAL-IDENTITY-REVIEW.md) separates the inherited results, the present extensions and their limits. The proof review required the now-explicit nonemptiness premise in I8; the other displayed arguments were accepted at their stated scope. This is collaborating-AI mathematical review, not external peer review or a machine-checked proof.
