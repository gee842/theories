# Finite-state boundary and a positive symbolic chaos witness

6 October 2026. AI-authored proof notes for [SymbolicDynamics.lean](SymbolicDynamics.lean). This is a new mathematical development using `Std` in Lean 4.29.1. It does not alter or rerun the physical concern learner. The package's fresh-build receipt is owned by the coordinating build task; the source author's compiler check is not a substitute for that receipt.

## What is proved

The file has 32 theorem declarations and 32 corresponding `#print axioms` commands. They divide into a finite-state boundary and a positive infinite-state example. The definitions and proofs fix the relevant complete state and observation scale rather than treating complexity or unpredictable output as a chaos certificate.

### Finite autonomous deterministic dynamics

`finite_collision` proves pigeonhole directly. For any sequence into `Fin n`, it finds positions `i < j ≤ n` with equal values. The proof inducts on the size of the codomain: either its chosen last value has already occurred, or deleting that value compresses the earlier observations into the smaller codomain. The compression's injectivity is proved, not assumed.

`finite_eventually_periodic` then applies this result to a deterministic trajectory. For any total map `f : α → α`, initial state `x`, and injective encoding of the **complete** state into `Fin n`, it constructs a starting time `a` and a strictly positive period `p` such that

\[
a+p\le n,\qquad
f^{a+t+p}(x)=f^{a+t}(x)\quad\text{for every }t\ge0.
\]

The repetition propagates because the same state is followed by the same total law. The theorem does not take a repeated state as an assumption. `finite_eventuallyPeriodic` exposes the simpler eventual-periodicity property without the numerical bound.

The premise is finite complete autonomous state, not a finite observation alphabet or a finite controller considered apart from its changing environment. A partial map that can halt is not the total-map theorem's subject; adding a specified absorbing halt state is a separate representation choice. Long transients and finite-horizon approximation of another system remain possible.

### Binary one-sided shift

The state is an infinite binary stream `Nat → Bool`. One step drops its initial bit:

\[
(\sigma x)_i=x_{i+1}.
\]

`PrefixEq n x y` means exact agreement at every index below `n`. `PrefixOpen` declares a set open precisely when each of its members has a finite-prefix neighborhood contained in that set. Empty and whole sets, binary intersections and arbitrary indexed unions satisfy the topology conditions. `prefix_open_iff_coordinate_open` proves equivalence with neighborhoods that fix an arbitrary finite list of coordinates. Thus these really are the cylinder neighborhoods of the product of discrete binary coordinates; the topology was not chosen to make the final statement true.

The shift's substantive properties are proved by explicit constructions:

- **Continuity:** agreeing on `n+1` input coordinates suffices for agreement on `n` coordinates after shifting.
- **Topological transitivity:** a stream that begins with a chosen finite prefix from one open set and then follows a stream in another reaches the second set after the prefix is shifted away. `splice_shift` proves that tail equality exactly.
- **Dense periodic points:** repeating a word of length `n+1` gives a positive-period stream inside any prescribed length-`n` neighborhood. `repeat_periodic` proves equality after `n+1` shifts.
- **Uniform sensitivity:** in any length-`n` neighborhood of any stream, change its bit at coordinate `n`. After `n` shifts, the two streams disagree at their very first bit. The same separating observation length, one, works everywhere; it does not depend on the starting stream or requested neighborhood.

`binary_shift_chaotic` combines continuity, transitivity, density of periodic points and this sensitivity under the explicitly defined `PrefixDevaneyChaotic` predicate. The label abbreviates these separately proved conditions; it is not an input assumption. The sensitivity is expressed through the prefix uniformity, rather than a numerical real-valued metric object. The familiar first-disagreement metric is not implemented in this `Std` development, and neither a metric equivalence theorem nor compactness is claimed as an audited declaration.

`no_isolated_stream` and `singleton_not_open` show that no finite prefix isolates a stream. `spike_injective` constructs infinitely many distinct streams; `stream_not_finitely_encoded` rules out an injective encoding of the complete stream space into any `Fin n`. The infinite witness therefore does not evade the finite-state theorem by quietly redefining its state as a finite machine.

## Scope and axioms

All 32 declarations compiled successfully with the explicitly selected Lean 4.29.1 executable. The source has no additional axiom declarations, admitted proofs, `native_decide`, unsafe evaluation or external theorem imports. The printed dependencies are limited to `propext`, `Quot.sound` and `Classical.choice`. Classical choice appears in the finite collision branch and its consequences; `binary_shift_chaotic` itself reports only `propext` and `Quot.sound`. Several elementary topology declarations have no axiom dependencies.

The finite result is conditional and universal over its encoded state class. The shift is one explicitly defined positive chaos example. Neither proves that every generative process is chaotic, that an accepted finite learner becomes chaotic, or that a particular physical flow has this symbolic dynamics. There is no Lorenz correspondence, Lyapunov computation, empirical identification or favorable ethical direction in these theorems. Those claims would require their own premises and evidence.

The contribution to the common account is precise: a choice of complete state and continuation law constrains possible recurrence; an infinite, exactly deterministic continuation can also have a rigorously specified sensitive regime. Observations of finite prefixes are differentiated access to that same process. This strengthens the systems/complexity comparison without making chaos a prerequisite for organization, learning or concern.
