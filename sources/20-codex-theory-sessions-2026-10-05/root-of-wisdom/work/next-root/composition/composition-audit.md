# Composition as the next root: joint possibility precedes justified separation

Mathematical investigation for the parent research task, 5 October 2026. The previous theories are preserved. This is a proposed next layer and a set of established-style mathematical examples with self-contained proofs, not a claim to have discovered new general mathematics or proved monism.

## Recommended candidate

> What can happen together is part of the structure of reality. An adequate description must preserve that joint structure; treating aspects as independently recombinable requires a warranted factorization.

The previous account starts with interactions, constraints, consequential distinctions, and the production of conditions for further action. This proposal asks an earlier question: **what licenses us to regard those distinctions, processes, or conditions as separately specifiable parts?** Individually possible values do not imply that their combination is possible. Individually accurate models do not imply that their simultaneous composition is realizable. Even complete descriptions of every proper subsystem need not determine the whole joint state.

Three claims must remain separate:

1. **Existence:** do local descriptions admit any common realization?
2. **Determination:** do those descriptions uniquely identify that realization?
3. **Separation:** does the realization factor into independent pieces?

The theorems below separate all three. They are about finite classical probability and constraint systems. They do not presume that every physical measurement admits a single classical assignment of context-independent outcomes.

## 1. Every proper subsystem can be insufficient

Let \(n\ge2\), \(x_i\in\{-1,+1\}\), and \(-1\le\tau\le1\). Define

\[
\boxed{P_\tau(x_1,\ldots,x_n)=2^{-n}\left(1+\tau\prod_{i=1}^{n}x_i\right).}
\tag{C1}
\]

**Theorem.** These are valid joint distributions. Every proper-subset marginal is uniform, independently of \(\tau\), but

\[
\mathbb E_\tau\left[\prod_{i=1}^{n}X_i\right]=\tau.
\tag{C2}
\]

For \(\tau\ne0\), the distribution fails to factor across every nontrivial partition of the supplied coordinates into two blocks. This holds even for \(|\tau|<1\), when every joint state has positive probability.

**Proof.** Nonnegativity follows from \(|\tau|\le1\). Summing over the whole cube cancels the product term and leaves total mass one. Marginalizing a proper subset sums over at least one missing sign; summing that sign cancels the product term and leaves the uniform distribution on the retained signs. Multiplying by the full product before summing instead cancels the constant term and gives \(\tau\). For a nontrivial bipartition \(A\sqcup B=\{1,\ldots,n\}\), both block marginals are uniform. Their product is therefore the uniform full distribution \(P_0\), which differs from \(P_\tau\) when \(\tau\ne0\). □

**Consequential difference.** Suppose an action \(a\in\{-1,+1\}\) receives reward \(a\prod_i X_i\). Its expected reward is \(a\tau\). The distributions \(P_{+\varepsilon}\) and \(P_{-\varepsilon}\), for \(0<\varepsilon\le1\), therefore require opposite optimal actions, although every proper-subsystem marginal agrees. Any fixed randomized action based only on those marginals has worst-case expected regret at least \(\varepsilon\); choosing each action with probability one half attains that bound. Indeed, if the probability of \(a=+1\) is \(q\), the two regrets are \(\varepsilon[1-(2q-1)]\) and \(\varepsilon[1+(2q-1)]\).

This is not an intervention claim about the variables. It is a decision problem with a specified joint observation and reward. Observational distributions alone do not determine the results of interventions on their generating mechanism.

**What is missing?** No local variable was omitted: all \(n\) variables were named and every proper joint marginal was supplied. What was omitted is the relation that organizes them together. A program searching only for another variable could miss this correction.

**Scope.** The restriction is access to proper-subset marginals, not a ban on combining measurements from the same physical specimen. If repeated observations on the same specimen recover all its coordinates, they recover the full joint sample and can estimate parity. The impossibility concerns the supplied statistical interface, not the inaccessible nature of a cosmic whole.

## 2. Tree-shaped overlap permits composition

Let \(T=(V,E)\) be a finite tree. Each vertex \(i\) has a finite value space, each vertex distribution is \(p_i\), and every edge distribution \(p_{ij}\) has the supplied \(p_i,p_j\) as marginals. Thus the edge descriptions agree wherever they overlap.

Choose a root and direct each edge from parent to child. When \(p_i(x_i)>0\), define

\[
q_{j|i}(x_j\mid x_i)=\frac{p_{ij}(x_i,x_j)}{p_i(x_i)}.
\]

When \(p_i(x_i)=0\), choose any probability row for \(q_{j|i}(\cdot\mid x_i)\). Then

\[
\boxed{P(x_V)=p_r(x_r)\prod_{i\to j}q_{j|i}(x_j\mid x_i)}
\tag{C3}
\]

is a normalized joint distribution with all the specified node and edge marginals.

**Proof.** Successively sum over leaves. Every conditional row sums to one, proving normalization. The root marginal is its specified distribution. If a parent has its specified marginal, then its joint distribution with a child is \(p_iq_{j|i}=p_{ij}\) on positive parent states. On zero parent states both are zero, because a nonnegative joint table with zero parent marginal has a zero corresponding row. Induction away from the root gives every edge marginal. □

Thus tree-shaped overlap guarantees at least one common realization. Formula C3 selects the conditional-independence realization; the given edge marginals need not force that independence. For example, on a three-vertex path, every distribution C1 has uniform edge marginals, while C3 selects only \(\tau=0\). **Guaranteed existence does not imply unique determination or factual independence.**

## 3. A cycle can obstruct composition

The smallest stochastic example uses three binary variables. For each of the three pairs, assign probability one half to \((+1,-1)\) and one half to \((-1,+1)\). Each pair distribution is valid and every single-variable marginal is uniform. Their overlapping marginals therefore agree exactly.

But no joint distribution realizes all three pairs. They would require

\[
X_1X_2=X_2X_3=X_3X_1=-1
\]

almost surely. Multiplying yields \(1=-1\). The contradiction is in the composition, not inside any individual pair description.

The quantitative form is useful for noise. For any jointly defined binary triple,

\[
\boxed{\mathbb E[X_1X_2]+\mathbb E[X_2X_3]+\mathbb E[X_3X_1]\ge-1.}
\tag{C4}
\]

For each assignment the sum is either \(3\) or \(-1\), so averaging proves the inequality. If all three pair correlations are \(-\rho\), a common classical joint realization therefore requires \(\rho\le1/3\). This threshold is sufficient as well: at \(\rho=1/3\), put equal probability on the six assignments in which not all signs agree; mix with uniform independent signs to obtain every \(0\le\rho\le1/3\).

**General binary relation theorem.** Give every edge of a finite undirected graph a prescribed sign \(s_{ij}\in\{-1,+1\}\). There is an assignment satisfying \(x_ix_j=s_{ij}\) on every edge if and only if

\[
\boxed{\prod_{e\in C}s_e=+1\quad\text{for every cycle }C.}
\tag{C5}
\]

When realizable, a graph with \(c\) connected components has exactly \(2^c\) satisfying assignments, counting isolated vertices as components.

**Proof.** Multiplying edge equations around a cycle makes every vertex sign occur twice and therefore gives \(+1\). Conversely, choose a sign at a root in each component and propagate it along a spanning tree. A non-tree edge closes a cycle; condition C5 makes its required relation agree with the propagated signs. Each component has exactly two root choices, and connected propagation determines everything else. □

A spanning forest supplies the constructive test. Only the fundamental cycles created by adding non-tree edges need checking; their consistency implies consistency on all cycles.

This theorem relates the possibility of a whole to a property invisible on each individual edge. It also shows that relations can determine all local values up to one freely chosen overall sign per component. That limited relational determination is mathematical; it does not establish that objects are metaphysically constituted entirely by relations.

## 4. Why this is a different root

The previous quotient theorem asks whether a compressed description preserves specified future consequences. The current result asks whether separately specified descriptions can be composed in the first place, whether their composition is determined, and whether it is independent. These questions precede the decision about which distinctions can safely be compressed.

The hierarchy is:

\[
\text{compatible organization of possibilities}
\longrightarrow
\text{warranted decomposition into parts}
\longrightarrow
\text{effective interactions and laws}
\longrightarrow
\text{consequence-preserving distinctions}.
\]

This is a proposed order of explanatory questions, not a demonstrated temporal creation sequence or an ontological grounding theorem. A relational presentation itself still uses mathematical relata, and a useful decomposition can be selected by experimental access, time scale, or task.

The new practical instruction is: **when all pieces look correct and the result fails, test their composition.** Check shared assumptions and overlaps, missing higher-order relations, context dependence, and whether apparent independence was actually established. More detailed inspection of each piece alone cannot resolve every such failure.

## 5. Distance to monism

The strongest supported step toward the user's trajectory is that independent parts are not an automatic starting entitlement. Relations among parts can contain indispensable information and determine which proposed combinations are possible.

Several stronger conclusions do not follow:

- Statistical dependence does not establish that there is only one substance or one concrete object.
- A common mathematical state description does not establish that a whole metaphysically grounds its parts. Any finite collection can be encoded into one mathematical object.
- Failure of one factorization does not establish failure of every possible decomposition. The parity example proves nonfactorization across all nontrivial partitions of its supplied coordinates; changing the coordinate algebra changes the question.
- A universal demand for one classical joint assignment across incompatible measurement contexts would be too strong. One may need a contextual or quantum composition rule instead.
- A part's functional dependence does not establish its ethical subordination to a whole.

Monism is a further interpretation with multiple meanings: one substance, one fundamental concrete whole, or a unified explanatory framework. The current mathematics supports **structured dependence and the need to justify separation**, while leaving those ontological alternatives open. This is an affirmative next step without pretending to finish the staircase.

## 6. Primary-source lineage and review scope

The distinction between compatible marginal measures and an extending joint measure is established mathematics. Vorob'ev's original paper identifies the combinatorial structure of a family of domains as central to extension. Its journal-hosted abstract and theorem statement were read; the full Russian proof was not reviewed. The finite tree construction above is self-contained. [N. N. Vorob'ev, Consistent Families of Measures and Their Extensions, 1962](https://www.mathnet.ru/eng/tvp4710).

Abramsky and Brandenburger formulate contextuality through obstructions to a global distribution over context-independent assignments. Their framework makes clear why agreeing distributions on overlaps need not have a global extension. The introduction and definitions were read in the primary full-text version. This audit does not infer that the three-pair classical example is physically realizable as a quantum experiment, or that contextuality proves monism. [Abramsky and Brandenburger, 2011](https://arxiv.org/html/1102.0264).

The exact parity construction, elementary cycle proof, decision consequence, and tree construction have been derived here for this inquiry. They are not represented as historically novel theorems.

## 7. Verification

`check_composition.py` independently enumerates all joint assignments for every signed simple graph with two through five vertices and compares them with the spanning-forest consistency criterion. It verifies both feasibility and the exact \(2^c\) solution count. It also constructs parity distributions with two through eight variables and five rational parameter values, checks normalization and nonnegativity, computes every proper-subset marginal, and verifies the global parity expectation. Finally it reconstructs compatible four-vertex chain and branching-tree laws from their node and edge marginals, including zero-probability node values and deterministic conditional rows.

These are exact constructed mathematical checks; no physical, human, or AI-response experiment was conducted. The general claims rest on the proofs, not extrapolation from the finite checks. Results are saved alongside this audit in `composition-checks.json`.
