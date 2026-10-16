# Systems and complexity: Lean source and coverage review

6 October 2026. AI-authored review under the [shared method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md) and the already accepted [conceptual comparison](../../../../theories/becoming/history/SYSTEMS-COMPLEXITY-CHAOS.md). Scope is the requested mathematical completion, not a new physical concern experiment or proof of universal favorable direction.

**Initial source-review checkpoint:** the four source modules below passed the source-level mathematical and interpretation review. The symbolic module passed its author's Lean 4.29.1 check. Separate fresh-package and real-analysis receipts were pending at that checkpoint; their subsequent acceptance is recorded separately below rather than inferred from source inspection.

**Authorship boundary:** this reviewer wrote `SymbolicDynamics.lean` and its companion notes. The discussion of that module records construction and scope, not an independent reimplementation of its proofs. The reviewer independently read the other three authors' complete modules. The coordinating authors own the fresh compiler harnesses and coverage review.

## Exact organization and projection

[SystemsOrganization.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/SystemsOrganization.lean) has 24 theorem declarations and matching axiom audits. Its general results operate on actual deterministic action laws and reuse the existing `GenerativeCore` trace semantics. A one-step commuting projection implies preservation of every action word, and preservation of every word implies the one-step condition. Existence of a reduced law is characterized by consistency on projection fibers, given an explicit representative section. That section is a supplied modeling input; it is not silently obtained from the mere choice of a boundary.

The coupled-components result allows each component update to depend on both coordinates. Its concrete crossed-copy example shows why discarding the other coordinate destroys autonomous closure for that projection and the fixed `Unit` action alphabet. It does not establish indeterminism of the complete process or prohibit a richer reduced state or input. The separate parts-only example gives an actual obstruction to preserving all future feasible words when identical cell values conceal different link formation. The spare, assembly rule and fuel cost are explicit; exchange is deliberately free in this small structural example. No sustainability, learned selection or ethical conclusion is hidden in its recurrence.

**Verdict:** meaningful conditional closure and representation results, with a genuine countermodel to an inadequate projection. They do not simply decree that all distinctions are independent or that all wholes are irreducible.

## Rational feedback: actual convergence and divergence

[FeedbackDynamics.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/FeedbackDynamics.lean) has 20 declarations and matching audits. At the same gain \(6/5\), it proves ordinary two-sided epsilon convergence for every rational immediate-feedback initial state. Its delayed conclusion is stronger than a finite growing sample: every nonzero rational full state eventually remains outside any requested bound on squared norm.

The proof derives an Archimedean bound from rational floor, computes the exact quadratic-energy transport, proves coercive bounds, and propagates the resulting estimates for every time. It does not assume convergence through a predicate named stability. The period-six result at gain one is a recurrence identity, correctly distinguished from chaos. This module's all-time contrast is over rational states at the specified gain; it is not the all-real gain classification.

**Verdict:** the theorem conclusions match the declared exact linear plant and observation delay. No costs, saturation, disturbance robustness or identification with the concern learner are asserted.

## Real feedback: full gain classification

[RealFeedback.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/RealFeedback.lean) is a separate Mathlib extension. The inspected source has 21 theorem declarations; its audit directives and fresh harness were still being completed at the initial checkpoint. Its immediate theorem proves universal convergence precisely for \(0<k<2\) and verifies the recurrence of the closed-form trajectory.

For delayed feedback \(A_k(x,y)=(x-ky,x)\), the source uses

\[
V_k(x,y)=2x^2+2k(x-y)^2+k^2(k+1)y^2,
\qquad d_k=k(1-k)(k+2).
\]

The identity \(V_k(A_k s)=V_k(s)-d_k\lVert s\rVert^2\) is algebraically correct. For \(0<k<1\), the proved bounds \(k^2\lVert s\rVert^2\le V_k(s)\le8\lVert s\rVert^2\) and \(0\le1-d_k/8<1\) yield actual geometric decay and convergence of squared full-state norm. The law, coefficients and decay rate are not assumed stability conclusions.

Necessity is also substantive. When \(k\le0\), the initial state \((1,1)\) retains coordinate deviations bounded below. For \(k\ge1\), the transported quadratic \(x^2-xy+ky^2\), starting at \((1,0)\), remains bounded below while a multiple of squared norm bounds it above. Thus universal convergence is impossible. The resulting iff covers **all real gains** and universal convergence over real initial states. It does not say that the zero initial state fails outside the interval, or prove divergence of every nonzero real state at every excluded gain. Its explicit conclusion is convergence classification; the coercive bounds support the usual linear stability interpretation without falsely claiming a separately audited theorem for every definition of stability.

**Verdict:** no mathematical or causal-scope correction is required by source inspection. Kernel acceptance remains a separate receipt obligation because this module imports Mathlib.

## Positive symbolic chaos and the finite boundary

[SymbolicDynamics.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/SymbolicDynamics.lean) has 32 theorem declarations with 32 audits. It proves an actual pigeonhole collision for `Fin n`, then bounded eventual periodicity for a total autonomous law whose complete state injects into `Fin n`. Neither a repeated state nor a period is a supplied premise. A partial halting law or an environmentally driven finite controller is outside that exact theorem until the complete continuation is specified.

The positive witness is the binary one-sided shift. The source proves the topology conditions, equivalence of prefix neighborhoods and arbitrary finite-coordinate product neighborhoods, shift continuity, topological transitivity, dense periodic points and a fixed separating prefix length for sensitivity. The witnesses respectively use splicing, repetition and a later-bit flip. It additionally proves that no finite prefix isolates a stream and that the entire stream space has no finite encoding. These are substantive constructions, not a definition that declares the chosen example chaotic without conditions.

The sensitivity is stated in the product's prefix uniformity. A real-valued metric object, compactness theorem, Lorenz correspondence and Lyapunov computation are not included or claimed. The exact convention is exposed in `PrefixDevaneyChaotic`; periodic points within this chaotic system are explicitly expected. [The author's notes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/CHAOS-LEAN-NOTES.md) state these limits and report the initial successful compiler check. Its printed axiom union is limited to `propext`, `Quot.sound` and `Classical.choice`; the chaos conclusion itself uses the first two.

## Acceptance boundary

Together these sources provide the requested mathematical strengthening: exact organization/description conditions, a real timing-dependent convergence contrast and classification, a finite-state obstruction and a positive infinite symbolic chaos example. Their local laws and observation structure remain explicit. They neither turn the established inquiry-limit rewrite into a bifurcation nor require every learning mechanism to be chaotic. They preserve the completed local concern and conditional-universality results.

After the separate fresh builds and complete axiom audits pass on these sources, the mathematical package can be accepted at this stated scope. It is unnecessary to add an empirical chaos experiment or a new controller to complete that request. A stronger physical or ethical application remains a different claim, not a withheld prerequisite.

## Fresh Std package accepted — 6 October 2026

The independent builder's [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/verification.json) passes in an isolated temporary Lean 4.29.1 build. It records **76 new theorem audits** across organization (24), rational feedback (20) and symbolic dynamics (32), plus **18 selected inherited audits** from `GenerativeCore`. Every theorem in the three new modules has exactly one requested dependency audit; the inherited count is explicitly selected coverage, not every declaration in that source. Thirty-one new audits have empty dependency lists. The remaining dependencies are limited to the three standard logical axioms already disclosed.

This reviewer checked the receipt against the four current source files, four frozen source snapshots, four compiler logs, compiler executable, checker and toolchain hashes, as well as all four requested/audited name sets: 19 checks, no mismatch. Receipt SHA-256: `a7ab2fbd68f66517c065bbb0159e4ea34ad1534b18353d34d3ceb679c2895352`. No scientific or compiler rerun was performed for this read-only receipt check. This accepts the complete Std portion at its stated mathematical scope. The separate real-analysis module still awaits its own receipt at this checkpoint.

## Exact core correspondence and extended Std acceptance — 6 October 2026

The added [SystemsComplexity.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/SystemsComplexity.lean) was independently read. It proves that arbitrary iterates produce the corresponding finite `Generative.Trace`; specializes this to the **same** binary shift whose chaos conditions were proved; proves equality of the rational delayed recurrence with the common iterate; and maps that recurrence's complete paired state into the core trace. No delayed coordinate or update law is discarded. This is an exact mathematical representation, not empirical identification or a new explanation of how the map physically forms.

The extended [fresh receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/verification.json) passes with **80 new plus 18 selected inherited audits** across five modules. The prior receipt and its source/log snapshots are preserved in [verification history](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/verification-history/before-core-correspondence/verification.json). All prior scientific module hashes are unchanged. The reviewer rechecked 23 current source/snapshot/log/coverage/compiler/checker/toolchain items and the prior receipt hash: 24 checks with no mismatch. Current receipt SHA-256: `b63d7ee11df965310e6632dc68a4b0d1d4cc6600fa0317dbbb9f06e7b0284411`.

A second agent, the feedback mechanism author, independently reviewed the complete symbolic source and notes after they froze. That review accepted the codomain-deletion pigeonhole proof, finite-coordinate topology equivalence and constructive transitivity/periodicity/sensitivity witnesses, including the fixed nonvacuous separating length. It also confirmed the explicit metric/compactness limits. This supplies peer source review separate from the symbolic author's own explanation and the fresh compiler build.

**Current Std verdict: accepted, including the core correspondence.** The real-analysis receipt remains separately pending; its eventual acceptance must not be retroactively attributed to this Std build.

## Final real-analysis acceptance and completion — 6 October 2026

The final [RealFeedback source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/RealFeedback.lean) and [fresh receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/verification.json) were read. The final module has **24 new declarations and audits**. Beyond the initial source-review checkpoint, it explicitly proves squared-norm Lyapunov stability for \(0<k<1\), divergence of squared full-state norm for **every nonzero real initial state when \(k>1\)**, a six-step return at gain one, equality to the common iterate and an exact trace in the existing generative core.

These additions have the correct quantitative content. Stability chooses \(\delta=\epsilon k^2/8>0\) and combines the coercive and geometric bounds for every time. Large-gain divergence uses positive transported energy and an upper comparison with squared norm, not a claim that the Euclidean norm increases at every step. The trace retains both the current and delayed coordinates. The period-six identity and real convergence classification do not assert nonlinear chaos.

This is a **separate Lean 4.30.0-rc2 build** against the already installed Mathlib revision `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa`. All six local sources were freshly compiled in a temporary directory; upstream Mathlib was used from its pinned cache, not rebuilt. The receipt replays 98 prior audits and adds 24. This reviewer performed 31 read-only source/snapshot/log/audit-coverage/compiler/checker/toolchain/manifest/direct-library-fingerprint checks, all matching. The temporary local compiled object's recorded fingerprint was not rechecked after its build directory was removed, and no full transitive cache revalidation is claimed. Receipt SHA-256: `192ddc29f5aec599db60fae63d09b18d33e7282efae04825447d857eba3b50ef`. The 24 new audit dependency lists contain only `propext`, `Classical.choice` and `Quot.sound`.

**Final verdict: accepted; the requested bounded mathematical completion is achieved.** The two successful builds establish **104 distinct new theorem audits**—80 in the Std package and 24 in the real-analysis extension—alongside 18 selected inherited core audits. Replayed declarations are not counted again as new results. The different toolchains and upstream-library boundary remain explicit. No further simulation, controller, metric formalization or ethical theorem is a prerequisite for this completed scope. Physical identification, Lorenz-system chaos and universal favorable direction have not been claimed.
