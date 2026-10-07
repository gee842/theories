# Living realization: deriving maintenance demand from transport

7 October 2026. AI-authored mathematical realization study supporting [living-dependency grounding](LIVING-GENERATIVITY-GROUNDING.md). Its contribution to the universal programme is a precise connection: **a specified operative relationship → actual compensatory activity → the support required for its continuation**. The operative relationship is a maintained bound on accumulated material under inward transport. It is not a definition or complete characterization of life.

**Result:** the support/demand accounting premise of the existing situated-renewal interface is derived from two more concrete laws: transport balance and work coupling. The demand is actual inward transport, rather than elapsed time or an analyst's assigned maintenance score. A finite included provision store remains part of the accounting; supplying support to one relation does not prove new whole-level formation. Ten new named theorems and twenty explicit declarations are checked in Lean 4.29.1. The correspondence and full-domain coverage obligations remain explicit below.

## 1. Source and intended realization

The accompanying primary-source investigation identifies an empirically motivated route in carbon-starved *E. coli*: inward ion transport and active export participate in maintenance of polarization and volume regulation. Its 2024 source uses a stochastic concentration equation and derives a near-steady pumping-demand relation; its 2019 predecessor connects population maintenance and nutrient recycling. The exact reading scope, source equations and experimental limits belong to [the mechanism study](LIVING-DEPENDENCY-MECHANISMS.md), whose source investigator communicated the relevant relations during this formalization. This note does not claim a separate primary-paper reading or data replication.

The present module is a deterministic, discrete, nonnegative-quantity abstraction motivated by that mechanism. It does **not** prove a refinement from the empirical stochastic model. Representing inside amount requires a fixed reference volume or an independently tracked conversion from concentration and geometry. The paper's changing volume cannot silently be suppressed and still called exact correspondence. Stochastic laws, variable geometry, multiple ion species and other work demands are not represented here.

The `inward` coordinate is **net unpowered inward transport over a modeled transition**, restricted to transitions where that net is nonnegative. Unpowered outward transport must be included in that net; it cannot be discarded or truncated to manufacture demand. `exported` then denotes the active export subject to the work-coupling law. A transition with net unpowered outward transport falls outside this representation unless a separately justified, exact reorganization of the represented intervals is made. No such general reduction is proved. In particular, gross inward flux alone cannot establish the support demand when uncounted passive relief is available. This explicitly restricts the model's coverage of noisy empirical histories.

“Inside” identifies a differentiated relation through the selected compartment and membrane; it does not introduce an ontologically independent system and environment. The whole represented state can include their joint conditions. The additional provision-store result explicitly follows a support transfer through another coordinate of the same history.

## 2. Exact model and hypotheses

The source is [LivingRealization.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LivingRealization.lean), importing the existing [SituatedRenewal](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SituatedRenewal.lean) interface and its closure. A `TransportLaw` concerns an arbitrary core process, an arbitrary type of dependency indices, and the following natural-number coordinates for each index:

| Coordinate | Declared interpretation |
|---|---|
| `inside` | Material amount whose maintained bound is under study. |
| `ceiling` | Fixed bound for this operative regime; not a general death or viability threshold. |
| `work` | Available support in the declared work units. |
| `inward` | Actual net unpowered inward transport on the transition, in the nonnegative regime above. |
| `exported` | Actual active compensatory export subject to the stated work coupling. |
| `supplied` | Actual support supplied or transformed into the work coordinate. |
| `cost` | Declared integer-scaled lower work cost per export unit. |

For each actual transition, the supplied physical-model laws are:

\[
x' + q = x + \ell,
\qquad e' + kq \le e + r.
\]

Here \(x\) is inside amount, \(q\) export, \(\ell\) inward transport, \(e\) work support, \(r\) supplied support and \(k\) export cost. There is no field asserting that maintenance demand already consumes a combined stock. That conclusion is derived.

The `maintained` process retains an actual core transition only when **all indexed bounds hold at its before and after states**. Thus a theorem about an actual maintained history is conditional on the history remaining in this regime. Crossing a bound is not defined as death or irreversible failure. The source investigator reports rescue before lysis after depolarization; this model must not turn the maintained restriction into a universal survival criterion.

These bounds concern the represented states. They do not independently establish that a continuous trajectory remains below the bound between sampled states. A fixed amount bound also does not automatically encode a fixed concentration bound when volume changes.

Units and cost are supplied correspondence choices. They are not a claim that every living act costs one ATP or that a universal positive cost follows from the core. The formal interface even admits zero cost; conclusions requiring excess cumulative cost-weighted load then have no application at that index. Recurrence requires the independently stated cumulative-load condition, not mere passage of time.

## 3. Derived accounts

`ion_account` derives the exact headroom account, provided both endpoint bounds hold:

\[
(B-x')+\ell=(B-x)+q.
\]

Consequently, actual inward transport beyond the initial headroom requires actual compensatory export somewhere in the same window. `compensation_required` obtains this through the existing general theorem, with export as its actual addition coordinate. It neither demands compensation on every step nor asserts that every unit of ingress is immediately exported.

`support_account` derives the coupled account for

\[
H = kB-kx+e:
\qquad H' + k\ell \le H+r.
\]

The subtraction is exact headroom under the maintained bounds; natural-number truncation is accounted for in the proof. This is an accounting potential combining unused admissible tolerance and work support in scaled units, **not a single physical energy store** or a claim that unused tolerance can be converted into energy. It is also not an ethical value or universal measure of generativity. `supportDependency` supplies it to the existing interface with a constant provision-route label, demand \(k\ell\), and support addition \(r\).

`support_input_required` therefore establishes actual positive support input inside any actual maintained window whose cost-weighted inward transport exceeds its initially available **cost-weighted headroom plus work support**. The conclusion identifies an actual event. It cannot be satisfied by a change of label, an unexercised opportunity, or a state reset.

`recurrent_support_input` applies the existing indexed recurrence result: **if** every dependency and start has an actual finite window whose cumulative weighted inward transport exceeds the then-current supported headroom, actual positive input recurs arbitrarily late for every index on this same history. Actual-load coverage remains a premise. The module does not infer it from a stochastic hazard, positive expected loss, or a finite observation.

## 4. Including finite provision and inherited efficacy

Support input can be supplied from an already formed relation elsewhere in the history. `included_store_account` takes a further coordinate \(d\) with the actual transfer law

\[
d'+r\le d
\]

and derives

\[
(H'+d')+k\ell\le H+d.
\]

`storeDependency` and `included_store_bounds_load` then establish that cumulative weighted inward transport in any actual maintained window cannot exceed the initially included headroom, work and provision. This does not imply that the history must choose a particular failure time; it bounds any admitted maintained window. Nor does inclusion of the store prove how it was formed or that all recyclable material can be converted without loss. Those are supplied realization questions.

Three explicit witnesses preserve the distinction between inherited efficacy and present input:

- `headroom_can_accommodate_ingress`: actual inward transport can occur with neither export nor new support while staying within the bound.
- `retained_work_can_compensate`: actual compensatory export can consume previously available work support with zero new support input on that step.
- `inactive_then_compensating_history`: an inactive transition and the later compensating transition compose through the actual same intermediate state. Retained support is consumed later; it is not reset between stages.

These witnesses test forbidden stronger conclusions from the account. They are exact finite examples in the declared model, not biological parameter estimates or a simulation of the dormant-spore experiment. They show why a supported living dependency must not be redescribed as universal immediate production by every bearer.

## 5. Novelty and remaining dependencies

The earlier theorem began with a supplied `DependencyLaw`. This module supplies a mechanistic derivation of that law for a maintained transport regime, connecting actual physical-model flux with the support obligation. It also distinguishes necessary compensatory transport from the later necessity of new support input. This removes an unexplained maintenance-demand account at this correspondence point; it does not remove the more concrete transport and energetic premises.

This is therefore neither a renamed theorem that assumes a renewal predicate nor a derivation of every living dependency. To apply it, the investigator must establish the selected operative bounds, transport balance, work coupling, units and actual cumulative load for the realization being studied. A finite inward flux may be fully accommodated by inherited conditions. An alternative adequate regime may abandon the selected bound. Repeated restoration need not introduce a novel organization. A changed or dying bearer does not by itself establish that its support has become available to another.

The universal inference advanced is that a real class of maintenance demands can arise from the internal transport relationships of the continuation, rather than being independently assigned by an analyst. Wider biological and organizational coverage remains research work. The proposed common ethical principle may evaluate the actual supported continuation, its losses and alternatives, but none of these physical accounts establishes its first normative warrant.

## 6. Verification

Lean version: `/Users/ren/.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean`. A fresh temporary directory received source copies of `GenerativeCore`, `ContinuationRenewal`, `SituatedRenewal` and `LivingRealization`; each was compiled in dependency order with `LEAN_PATH` containing only that directory in addition to the toolchain's standard library. An additional generated audit imported the new module and printed the axioms of every explicit new declaration.

**Initial verification:** all four modules compile. The new module contains **10 named theorems and 20 explicit declarations**. Seven audited declarations have empty axiom dependencies; thirteen use only the standard `propext` and `Quot.sound`. No custom axiom, `sorry`, `admit`, `native_decide`, or choice axiom is used in the new source. The three finite witnesses use ordinary kernel-checked proofs. These results concern the represented inference; they do not certify empirical correspondence or ethical truth.

**Final source-bound verification:** the root's [reproducible checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/check_living_realization.py) passes on the final source bytes, with **four modules and 87 explicit declaration audits** in the complete closure, including the same **20 new declarations / 10 named theorems**. The [current receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/living-realization-verification.json) records compiler and source hashes, the actual audit results, and the [immutable run](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/living-realization-checks/20261007T165626.734264Z/verification.json). The final new-source SHA-256 is `539742f929fbc8d3d9efc015ae0b08d80463ed99e65a0ea4af4c4f2eaf80b083`.

No generated `.olean`, interpreter cache or temporary installation is imported into the research tree. Any subsequent source change requires a new checked receipt before these counts are reported as current.
