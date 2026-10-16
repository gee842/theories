# Formal event-law check and connection to the causal root

6 October 2026. AI-authored formalization of the [endogenous-regulation construction](ENDOGENOUS-REGULATION-MATH.md), following Ren's accepted dependency-to-regulation gate. The [Lean sources and checker](../../../../experiments/shared-renewal-capability/regulation/retention/formal/README.md) certify 32 new theorem declarations using Lean 4.29.1 and `Std`. The existing root is compiled from its original source as a checked dependency.

## What has been established

The seven supplied events now have explicit natural-number reactant guards and state updates. The formal state is `(C,G,F,E)` with fixed site count N, regulator-material count M and storage capacity B; damaged sites and precursor are derived as `N-C` and `M-G`. Every allowed event preserves those physical bounds, and every finite valid path preserves both material totals.

Fuel accounting is exact on arbitrary finite paths: final usable fuel, final incident fuel and all spent fuel sum to the initial two fuel stocks. Fabrication, repair, copying and leakage each spend one unit. It follows that copy events are bounded by the initial total support. No later state is independently re-prepared.

For an initially all-damaged state with no regulator and fewer than two usable fuel units, `C=0 ∧ F+G≤1` is an invariant. Repair, capture and copying cannot become enabled there. The supplied positive witness uses exactly two initial usable fuel units, restores capture, and then uses two newly captured units to make two copies.

The proof also strengthens the original termination account. The rank

\[
V=4E+2F+C+G
\]

strictly decreases on every event. Damage, fabrication, repair, copying and wear decrease it by one; capture and leakage decrease it by two. Consequently the total number of physical events is at most V at the initial state, every nonempty event cycle is impossible, and there is no infinite event sequence. This deterministic fact does not require a stochastic almost-sure argument. When the enabled relation includes damage, wear and leak, a valid terminal state has exactly C=G=F=0; incident fuel may remain inaccessible.

This rank is a proof device for this finite-stock reaction law. It is not proposed as a universal scalar of generation or ethical value. It does not bound how long a wait may take, and an absorbing process may persist forever in elapsed time without another event.

## What connects to the previous root

`RootBridge.lean` defines this concrete law as a `Generative.Process`. It proves both directions of the equivalence between this development's trace representation and the previous root's `Generative.Trace`.

The fuel ledger, copy budget, bootstrap obstruction and positive witness therefore become theorems about actual processes in the existing causal interface. A further theorem obtains actual-successor composition directly from the earlier root's concatenation theorem. This is an exact mathematical interface between studies, rather than a shared use of the words “process” and “generation.”

The bridge does not derive the supplied chemistry from the abstract root. It establishes that the concrete formation mechanism inhabits that root and carries its stated constraints through actual state changes.

## Scope and remaining work

The formalization certifies admissible discrete transitions, not their stochastic intensities or waiting times. The analytical expected-copy comparisons—including their coupling argument and rational lower bounds—remain separate mathematical claims. No continuous-time Markov chain implementation, numerical enclosure, empirical parameter or thermodynamic identification is certified by these Lean proofs. Negative-control event laws are also outside this seven-event module unless separately checked.

The witness's damage-coupled fabrication, repair action and autocopy specificity are supplied local laws. Their cost and causal composition are explicit. The result does not show that useful variants defeat nonrepairing variants sharing the same fuel, that copying constitutes individual learning, or that the learning architecture revises itself. The next connection must explain those further capacities while retaining resource accounting and the failed routes.

The [verification record](../../../../experiments/shared-renewal-capability/regulation/retention/formal/verification.json) pins the toolchain, compiler, sources and logs. Each new theorem has an axiom-dependency audit; only the disclosed standard Lean foundational axioms are admitted. There were no rejected mathematical claims in this formalization. An unavailable tactic spelling was replaced with an elementary case split during development; the final fresh build passes without incomplete proofs or warnings.
