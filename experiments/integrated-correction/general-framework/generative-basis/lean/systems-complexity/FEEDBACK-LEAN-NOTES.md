# Exact rational feedback comparison

6 October 2026. AI-authored formalization of the elementary feedback comparison in the [mechanism note](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/SYSTEMS-COMPLEXITY-MECHANISM.md). The [source](FeedbackDynamics.lean) imports only `Std` and was compiled with Lean 4.29.1. Fresh package compilation and source binding are reported separately by the package checker; this note is an explanation, not a verification receipt.

## What the model assumes

The plant obeys `x(t+1) = x(t) + u(t)` with exact rational arithmetic, stationary linear dynamics, the declared observation timing, and no saturation, disturbance or resource limit. Its coordinates are analytical descriptions of one coupled process. They do not posit independently existing controller and world substances. These assumptions are supplied to this comparison, not derived from the generative foundation.

Immediate correction uses `u(t) = −k x(t)`. Delayed correction uses `u(t) = −k x(t−1)` and therefore has complete state `(current, previous)`. Both main results use the **same gain `6/5`**. The rational state space is infinite; this is not a finite-precision simulation.

The term `delayedEnergy` names a quadratic mathematical quantity. It is not the actor's physical fuel or a new source of physical energy.

## Checked arbitrary-time results

Let

\[
S(x,y)=x^2+y^2,\qquad E_k(x,y)=x^2-xy+ky^2.
\]

The file proves these statements by induction and exact ordered-field arithmetic:

| Theorem | Exact scope |
| --- | --- |
| `immediate_formula` | For any rational gain and initial state, \(x_n=(1-k)^n x_0\). |
| `delayed_energy_step` | For every rational gain and pair, \(E_k(x-ky,x)=kE_k(x,y)\). The identity alone does not make this quantity positive. |
| `delayed_energy_formula` | For every natural time, \(E_k(s_n)=k^nE_k(s_0)\). |
| `energy_lower`, `energy_upper`, `energy_positive` | At `k = 6/5`, \(S/2\le E_k\le2S\), with positive energy for every nonzero pair. |
| `immediate_bound` | At the same gain, \((n+1)x_n^2\le x_0^2\) for every natural time. |
| `immediate_tends_zero` | For every rational initial state and positive rational \(\epsilon\), some \(N\) satisfies \(-\epsilon<x_n<\epsilon\) for **every** \(n\ge N\). |
| `delayed_energy_growth` | At the same gain, \((1+n/5)E_k(s_0)\le E_k(s_n)\). |
| `delayed_normSq_tends_infinity` | For every nonzero rational initial pair and every rational bound \(B\), some \(N\) satisfies \(B<S(s_n)\) for **every** \(n\ge N\). |
| `delayed_one_six`, `delayed_one_periodic` | At gain `1`, every pair returns after six steps and \(s_{n+6}=s_n\). These theorems assert a period dividing six, not a least-period classification. |

The limit statements are actual quantified eventual properties. They are not finite sample checks or definitions that rename an eigenvalue condition “stability.” The rational Archimedean lemma is derived from the floor operation, so the existence of a sufficiently late time is also proved. The divergence result concerns the full pair; a particular scalar sample may vanish and the Euclidean norm need not increase monotonically at every step.

## Verification and limits

All 20 theorem declarations have explicit `#print axioms` audits. Direct compilation succeeds without errors or warnings; the only reported dependencies are Lean's standard `propext`, `Classical.choice` and `Quot.sound`. No `sorry`, admitted theorem, `native_decide`, custom axiom or external mathematical library is used.

This module proves the exact rational `6/5` contrast and the listed generic algebraic identities. It does not by itself formalize the complete real-parameter stability intervals, a topology library, a chaotic regime, or a dynamical correspondence with the finite concern model. The separate real analysis can strengthen the parameter scope without altering these exact statements. Connecting them to a physical process still requires identifying its plant, timing, support and admissible disturbances.
