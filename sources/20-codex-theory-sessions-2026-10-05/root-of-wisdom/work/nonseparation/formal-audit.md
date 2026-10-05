# Nonseparation as boundary-consistent dynamics

Formal audit for the new research branch, 5 October 2026. This note does not alter the retained theories. The results below are elementary derivations; no historical novelty or experimental verification is claimed.

## The useful refinement of “one truth applies to every thing”

A single encompassing reality and a law valid for every region are distinct claims. The first does not make every property of the whole a property of each part. A closed exchange system can have constant total amount while every proper region gains or loses amount. “No exterior to the whole” therefore does not imply “no exchanges across any interior boundary.”

A stronger and more useful interpretation of universality is:

> The same accounting of production, transformation, and exchange remains consistent wherever a boundary is drawn. Changing the boundary changes which processes count as internal and which count as exchange; it does not create or erase their consequences.

This is a precise conditional result for the following class of systems. It is not a proof that every kind of physical quantity is conserved, nor a derivation of monism from notation.

## A balance law with no privileged boundary

Let a finite set of sites be V. Site i has an amount x_i(t). Let j_ij(t) be the signed instantaneous current from j to i, so j_ij = -j_ji. Let s_i(t) be production minus destruction that is not represented as transfer of this same quantity between modeled sites. Assume

\[
\dot x_i=s_i+\sum_{j\in V}j_{ij}.
\tag{1}
\]

For every subset S of V, define X_S=Σ_{i∈S}x_i and S_S=Σ_{i∈S}s_i. Then

\[
\boxed{\dot X_S=S_S+\sum_{i\in S,\ j\notin S}j_{ij}.}
\tag{2}
\]

Proof: sum (1) over S. For every pair internal to S, j_ij+j_ji=0. Precisely the crossing terms remain. This includes the empty set and the whole. For S=V, the boundary sum vanishes. For s=0, the whole conserves its amount, while its proper regions generally do not. Conversely, if (2) holds for every subset with the stated currents and sources, its singleton cases recover (1). Thus the all-boundary statement and local dynamics are equivalent, not merely analogous.

For disjoint regions A and B, define J_AB=Σ_{i∈A,j∈B}j_ij. These block currents obey J_AB=-J_BA. For any partition π={B_1,...,B_m},

\[
\boxed{\dot X_{B_\alpha}=S_{B_\alpha}+\sum_\beta J_{B_\alpha B_\beta}.}
\tag{3}
\]

If several blocks are grouped again, summing their block currents gives exactly the currents obtained by grouping the original sites directly. Internal block interfaces cancel. Consequently, every nested partition gives the same total and exchange accounting; aggregation is associative. No particular partition is privileged by this balance law.

The equation is exact even when currents depend nonlinearly on states or on retained history. It does **not** imply that block totals alone determine those currents. Predictive closure of the coarse dynamics is an additional demand, already investigated in the preceding branch. A block can have an exact balance equation while still requiring boundary conditions, hidden state, or its environment for prediction.

## When a part cannot be dynamically self-sufficient

Specialize to symmetric linear exchange:

\[
j_{ij}=w_{ij}(x_j-x_i),\qquad w_{ij}=w_{ji}\ge0,\qquad s_i=0.
\tag{4}
\]

For a nonempty proper subset S, ask whether an exact law for its complete state x_S can be written as \dot x_S=f_S(x_S), valid for every allowed initial state of the whole. Such a law exists if and only if every crossing weight w_ij, i∈S,j∉S, is zero.

Sufficiency is direct. For necessity, choose a crossing edge of positive weight. Hold x_S fixed and change only the exterior x_j. The derivative of at least one interior x_i changes by w_ij Δx_j, although its proposed local input x_S has not changed. Thus no single f_S can give the derivative for both preparations. Nonnegativity creates no obstacle: compare all-zero amounts with one positive exterior amount. The same argument excludes an autonomous law for the total X_S alone whenever a crossing edge exists, because its exterior coefficient is Σ_{i∈S}w_ij>0.

Therefore, if the positive-weight graph is connected, **no nonempty proper region is exactly dynamically self-sufficient across arbitrary preparations**. Every cut has at least one positive crossing edge. This gives a precise sense in which distinct regions can belong to one dynamically inseparable process.

The quantifiers matter. Particular currents may vanish at equilibrium. Approximate autonomy may be excellent when crossing rates are small relative to internal rates over a specified time. Statistical independence at one instant is a different property. Causal communication can also be absent on a timescale even when a more comprehensive model has connections. This theorem concerns this specified finite exchange system and unrestricted nonnegative initial states, not a claim that all regions of the actual universe are mutually reachable.

## A simple failure of part–whole inheritance

For two sites with unit exchange,

\[
\dot x_1=x_2-x_1,\qquad \dot x_2=x_1-x_2.
\]

At x=(1,0), the whole has derivative zero, while the two site derivatives are -1 and +1. Applying “the total never changes” separately to each site would be false. Applying the boundary balance to each site and to their union is correct. The universal content is a compatible law of relations, with the appropriate boundary terms, not identical behavior at every scale.

An ontology containing exactly one fundamental entity is also compatible with many distinct possible dynamics. The same two-site whole can obey rates 1 or 2; it can also have zero exchange. Counting fundamentals does not select these rates or decide whether a dynamical distinction is consequential. Additional structure remains necessary.

## Why the boundary law is necessary but not the whole root

Conservation alone does not recover physical currents. Given any finite derivative vector v with Σ_i v_i=0 and any connected graph, choose a root and a spanning tree. A leaf edge can carry its leaf's required derivative; remove that leaf and transfer its accounting requirement to its parent. Induction constructs antisymmetric tree currents with divergence v. These are signed currents; this construction does not establish a physical transport law, nonnegative conductance, locality beyond the supplied tree, or energetically permissible flow.

Currents need not be unique. A circulating current around a cycle has zero net divergence at every site, so adding it changes edge flows without changing any instantaneous site derivative. Site trajectories alone can therefore leave consequential throughput undetermined.

This identifies the empirical burden: independently warranted transport mechanisms, rates, resources, and boundary observations must select the physically realized currents. Writing everything as one global differential equation is not by itself explanatory. The previous report's diffusion derivation supplies an example of additional constraints that genuinely select a law's form.

## Observers and interventions are within the accounting

An external input in a subsystem equation is external relative to that chosen subsystem. If the controller and energy or material source are included in a larger model, the relevant transfers become internal there and cancel in its aggregate balance. This is a change in modeling scope, not the disappearance of agency or of the consequences of intervention. Quantities converted to another kind require a suitable transformation law or expanded accounting; merely relabeling conversion as transport would be incorrect.

No claim that an observer can possess a complete model follows. The observer remains one participating process with limited access, memory, and action. A local point of view and an encompassing physical account can coexist.

## What this does and does not establish about “no self”

For a modeled participant, distinguish:

1. Its operational boundary: where a specified description, control, or accounting is drawn.
2. Its organizational persistence: what process keeps a recognizable pattern going.
3. Absolute self-sufficiency: the claim that its state and continued existence require no external conditions.

The balance theorem preserves the first. A suitable maintained-process model could explain the second. Connected exchange contradicts the third in its stated setting. Thus “no independently self-sufficient self” has a precise possible interpretation that does not erase organisms, personal experience, or distinct vulnerabilities.

This mathematics alone neither establishes a religious doctrine of no-self nor establishes metaphysical monism. It provides a common formal question to bring to those accounts: which purported boundaries are merely operational, which support relative autonomy, and which have mistakenly been treated as absolute independence?

Likewise, removing absolute self/other independence does not make different experiences identical. A harm concentrated in one participant does not vanish when one totals the larger system. A moral conclusion requires a reason for how the affected experiences, agency, and interests count. Global amount conservation supplies no such moral ranking.

## Strongest usable synthesis

> **A part is a real differentiation within a larger process. Its apparent independence is a claim about suppressed dependencies, to be established for a specified purpose and scale. A universal account must remain consistent across changes of boundary while retaining the exchanges and conditions that make each differentiation possible.**

This strengthens the previous branch in one respect: “no separation” need not mean a denial of differences. It can mean that no operational cut licenses us to discard the causal and material conditions crossing it. In the connected exchange example this is an exact theorem; its extension to living selves or the universe is a further substantive claim requiring the appropriate evidence and ontology.

Exact checks are recorded separately in formal-checks.json. They corroborate the proofs on finite constructed systems and do not validate a cosmological or ethical interpretation.
