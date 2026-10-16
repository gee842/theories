# Composition and the scope of an optimum

Mathematical companion to Alignment as the Reproduction of Its Conditions. Prepared 5 October 2026. This note supplies a sufficient composition result and distinguishes the optimization problems that a general theory can actually solve. These are applications of established invariance and decision principles, not claims to have invented those principles.

## 1 Closing dependencies without an ideal governor

A mechanism that repairs a system can itself require competence, information, authority, participation, energy, and replacement. Adding those dependencies to a diagram does not establish that they continue. The relevant question is whether their joint dynamics satisfy their own operating requirements. This question need not generate an infinite hierarchy of supervisors: a finite, reciprocally supporting network can be checked as one process, conditional on its declared boundary inputs.

Let a discrete-time state be \(z=(z_1,\ldots,z_n)\), with component memories included. Let \(w\in W(z)\) denote a joint admissible disturbance, including dependencies among disturbances. Component \(i\) receives only its actual observation \(o_i(z)\) and uses an installed rule \(u_i=\pi_i(o_i(z))\). Memory updates are part of the transition. The joint dynamics are

\[
z_i^+=F_i(z,u,w),\qquad u=(u_1,\ldots,u_n).
\]

Assume \(W(z)\) is nonempty and the transition is defined for every admitted state, joint action, and disturbance. Terminal outcomes, if permitted, have an explicit continuation convention such as an absorbing state. This prevents a vacuous guarantee obtained by leaving no next transition. No actor is granted the other actors' private observations. Refusal, attempted capture, succession, communications failure, and rule changes must be represented in \(F\) or the permitted disturbance set when the guarantee claims robustness to them. Genuine external inputs remain explicit assumptions; closure of organizational dependencies is not energetic isolation.

**Proposition C1 Composed continuation.** Choose component sets \(S_i\) and let \(S=\prod_iS_i\). Suppose:

1. \(S\) satisfies the declared joint protected constraints, not merely each component's private constraint.
2. For every \(z\in S\), the installed joint action belongs to the actual joint action set \(U(z)\). In particular, it does not spend the same shared resource twice or assume incompatible permissions.
3. For every \(z\in S\) and \(w\in W(z)\), every component satisfies \(F_i(z,\pi(o(z)),w)\in S_i\).
4. The initial state belongs to \(S\).

Then the actual installed system remains in \(S\) at every step, for every admitted disturbance sequence.

**Proof.** At the initial step all component membership conditions hold simultaneously. Conditions 2 and 3 make the next actual transition admissible and place every next component in its corresponding set. Induction gives the claim. No independence assumption is used. ∎

The quantification over the current joint set makes this an inductive certificate, rather than the circular argument that each component will succeed because the others succeed. Establishing membership initially and checking the transition are indispensable. A mutually dependent cycle that cannot be initialized is not made viable by its diagram.

The proposition is deliberately sufficient, not necessary. Many viable sets have correlated coordinates and are not Cartesian products. The exact finite information-state construction in [Adaptive optimum](ADAPTIVE-OPTIMUM.md) searches a larger class when its premises hold. An application must also demonstrate how the installed rules are produced and retained; if selection can replace them, their modes and replacement events belong in the state.

## 2 Safe changes across levels

Let \(v\) label an installed organizational or controller mode and \(S_v\) its certified operating region. A transition may change both \(z\) and \(v\). It is insufficient to prove that each mode works when held fixed: switching can invalidate the assumptions of the next mode.

**Proposition C2 Switching with establishment.** Suppose every permitted actual transition from \((z,v)\), with \(z\in S_v\), reaches a pair \((z^+,v^+)\) satisfying \(z^+\in S_{v^+}\). Then \(\bigcup_v(S_v\times\{v\})\) is invariant. This holds under arbitrary sequences of those permitted transitions.

**Proof.** It is the same one-step induction on the enlarged state. ∎

Costs and delays during establishment are transitions too. If a new institution is sustainable after installation but the old institution runs out of capacity during the handoff, C2 fails. Hiding the handoff inside an instantaneous mode change would certify a different model.

A common invariant region is one convenient way to satisfy C2, but is not required. Region-to-region transfers can also work. A permission rule excluding unsafe switches must itself have an executable implementation; otherwise it describes an available policy rather than the actual process.

These results are specializations of established assume-guarantee and invariant-set methods. Prior work already supplies compositional safety theorems for networked systems, including decentralized information restrictions. The contribution sought here concerns their use when the continuation of observation, authority, participation, and replacement is itself part of the protected dynamics. See [Chen and colleagues](https://arxiv.org/abs/1810.10636) and [Ghasemi, Sadraddini, and Belta](https://arxiv.org/abs/1909.06425). The elementary discrete-time proofs above are self-contained and do not import continuous-time composition assumptions.

## 3 Continuation must include an independently specified function

Preserving a state forever is not automatically preserving alignment. A frozen, unresponsive institution might maintain itself perfectly. A contract can require bounded response, inquiry, or replenishment intervals, represented by finite counters. For example, if every rolling \(D\)-step window must contain a named service, reset its counter to zero on delivery, increment it otherwise, and prohibit values greater than or equal to \(D\). Initialize the counter from the actual elapsed time since the last delivery, or explicitly credit a delivery at time zero. Include service cost and its actual delivery mechanism. Safety of this augmented process then entails the bounded recurrence requirement.

This construction is exact for a specified finite bound. It does not reduce every unbounded eventuality to a finite counter. An authorized ending or safe shutdown can be a successful terminal outcome where the contract permits it; endless organizational survival is not made an ethical axiom.

## 4 Several optima rather than one unstated ordering

The phrase optimal final theory mixes distinct comparisons. A precise integrated architecture can solve several of them without pretending that they share one objective.

| Question | Declared comparison | Result and boundary |
|---|---|---|
| Which distinctions must a representation preserve | Exact deterministic encodings of the same intervention response contract | The existing canonical quotient is least informative up to relabeling; this is not causal discovery |
| Where is continued satisfaction possible | Implementable policies with the same information, model uncertainty, costs, and disturbances | Finite viability recursion identifies the maximal feasible region for its declared safety or bounded monitor contract |
| Which feasible intervention costs least | Actual observation policies with hard separate requirements and a specified resource cost | Finite backward recursion attains the minimum worst-case cost; changing the cost criterion can change the answer |
| Which feasible test best separates specified rivals | A finite experiment family and a dated experimental budget | The companion design program maximizes a specified minimum pairwise separation; different statistical loss criteria can select other designs |
| Which scientific model is best overall | Predictive accuracy, causal transport, measurement burden, complexity, and interpretability | Usually a partial ordering; the framework does not prove a unique optimum without priorities among these criteria |

The first four optimization problems are useful because their feasible sets and objectives are explicit. None supplies an ethically optimal evaluation contract. Minimizing a resource cost subject to plural requirements does not mean assuming that the world or its participants maximize that cost's negative.

For a finite nonempty set of feasible candidates and finitely many declared scores, at least one Pareto-undominated candidate exists. A candidate is undominated when no other is no worse on every score and better on at least one. Existence follows by following strict dominance improvements; a finite set cannot contain an infinite strict improvement chain. This does not guarantee uniqueness or make every frontier point equally desirable. It tells us exactly where an additional methodological or public choice is needed.

## 5 Direction without a universal gradient

Two policies can be compared by the requirements they preserve, the disturbances they withstand, the burdens they impose on each affected party, and their revision possibilities. Improvements can be genuine without collapsing these quantities into a universal scalar. Inclusion of feasible task sets supplies one partial order; separately bounded burdens supply others.

Where all requirements improve together, direction is unambiguous relative to them. Where one improves and another worsens, dynamics alone does not choose a tradeoff. Where no feasible policy satisfies all requirements, a correct theory should return a conflict certificate or an explicitly revised problem. Inventing a scalar to conceal the conflict would reduce the theory's explanatory value.

The feasible region depends on the declared model family. More information can expand it only when acquiring, storing, and acting on that information does not consume the very capacity needed to remain feasible. More rules can shrink it; more options can introduce burdens. These are questions for the paid transition model, not automatic benefits of institutional complexity.

## 6 Attractors and persistent revision are different objects

An attractor describes the long-run behavior of a specified installed dynamics. A viability region describes states from which at least one admissible policy can continue satisfying a contract. A robust invariant region for an installed policy describes what that policy actually preserves. A basin describes the initial conditions attracted to a particular regime. These sets need not coincide.

Changing rules can alter attractors and basins. A theory of change must therefore study the joint state including rule formation, not infer a single universal basin from a few similar pictures. Safe revision can move through a family of regimes while preserving common obligations. In this operational sense, a desirable meta-level property is continued capacity for justified, executable change, not convergence to an immutable institutional configuration.

This is a research interpretation of the mathematics. Whether a particular society, ecosystem, or AI deployment satisfies it remains a causal and normative application question.
