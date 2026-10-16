# Independent audit of the restricted reproduction comparison

5 October 2026. Scope: the discrimination implementation, frozen protocol, saved results and result interpretation; comparison against the unchanged formation kernel; and the proposed empirical design in `../design/DESIGN.md`. No implementation or result files were changed. This is an independent internal audit, not external peer review or empirical validation.

**Finding: no substantive implementation or mathematical blocker.** The projected equivalence is correctly qualified, the primary effect is reproduced, and the rival changes the stated turnover dependence while retaining the other mechanisms. The design identifies assignment effects on specified transmission routes; it does not yet identify a generic maintenance mediator or the effects of physically causing harm.

## 1. The changed mechanism and calibration equivalence

The new transition calculation matches the baseline's work portfolios, physical responses, complaint generation, inquiry counts, nomination, candidate-assumed feasibility, training, successor selection, and archival loss. The substantive alternative is exactly

\[
\delta(H,n)=1/20+H/(5n)
\quad\longrightarrow\quad
\delta_R=3/20.
\]

The additional turnover label records the branch; it does not change its probability or the successor state. Feedback mode reproduces all six old endpoint and cumulative-reward vectors. In particular, both implementations use the corrected accounting for losing a package when the last skilled carrier disappears.

For the execution-blocked, training-enabled regime, the projected-path argument is valid. At every compatible reachable full state, ordinary service has expected harm proportion one half; randomized inquiry also has that expectation. Training takes `(k,q)=(1,1)` to two carriers before turnover. Every other portfolio leaves pre-turnover skill unchanged. Appointment depends only on that pre-turnover skill, old practice and the turnover event. Consequently the event-labeled row after marginalizing harm depends only on `(k,q)`, and is identical under both laws. Conditioning on any earlier projected history cannot alter this common row. This proves equality of the entire projected path law, rather than just matching a one-period mean or a 25-period marginal.

The qualifications in the protocol and results are essential and correct:

- This is a fixed execution-blocked regime with the stated training and appointment rules, not equivalence under every intervention.
- The allowed calibration record is skill, installed practice and the event label. Harms, complaints, archive contents, portfolios and service counts are excluded. Their joint laws need not match.
- Thus the rival matches a declared observation channel, not all potentially observable pre-intervention data.
- At zero skill, the code can still label a turnover draw even though no qualified carrier remains to be lost. Interpret that label as the model's personnel-turnover event, not an additional loss of corrective skill.

The constant-turnover model is still adaptive: harms produce complaints, and records can produce new frames. Describing it as an entirely fixed institution would be incorrect. The current result note explicitly avoids that claim.

## 2. Independent numerical reconstruction

The reconstruction is now rerunnable with [verify_independent.py](verify_independent.py); its saved report is [verification.json](verification.json). It requires only the Python standard library and preserves the audited source files. The checker validates dependency hashes before using the earlier independent enumerator.

I reused the previously audited raw-case rational enumerator in `../../gap-resolution/formation-coupled/verify_independent.py`, without calling the production portfolio, physical-profile, query, nomination or transition helpers to construct rows. In memory, its single turnover expression was extended to select `Fraction(3,20)` for the rival. No source file was changed.

I exhausted all reachable states for the four feedback/constant × execution-enabled/blocked arms, independently reconstructing **724 transition rows**. After marginalizing the production event label, supports agreed and the maximum row-probability discrepancy was **2.22×10⁻¹⁶**. Rational row probabilities were converted to floating point only for full-distribution propagation.

| Model and execution | Independently reconstructed probability of positive skill at round 25 |
|---|---:|
| Feedback, enabled | 0.6793088915746338 |
| Feedback, blocked | 0.5794189291049126 |
| Constant, enabled | 0.5794189291049129 |
| Constant, blocked | 0.5794189291049129 |

The independently reconstructed difference between within-model effects is **0.09988996246972126**, or **9.988996246972126 percentage points**. The largest discrepancy against a saved endpoint was 1.78×10⁻¹⁵. This confirms the reported +9.99-point contrast; it is exhaustive finite probability propagation, not a Monte Carlo estimate. The displayed decimals are numerical evaluations, not symbolic exact arithmetic for the entire feedback path distribution.

As a separate calculation, rational propagation of the reduced skill/practice chain gives the blocked and constant-model survival probability exactly:

\[
\frac{2897094645524565070998538830349299923811927497027}
{5000000000000000000000000000000000000000000000000}
=0.579418929104913\ldots.
\]

The three common-state expected-turnover witnesses also follow directly from physical mean harms `.15`, `.85`, and `.5`: `.08`, `.22`, and `.15`. The covariance formula is correct under the stated independent fresh-case model. Neither the one-round witnesses nor the covariance justify observational causal identification in an uncontrolled real institution.

## 3. Interpretation

The endpoint concerns retention of skilled capacity. It does not establish that every maintained frame is adequate, that every inquiry case meets the ordinary-service harm bound, or that maintaining this institution is ethically preferable. The result note keeps retained ordinary-service compliance, ordinary/inquiry harm, burden and service quantities separate.

The clamp-to-`.15` negative control is a structural identity: after applying it, the two supplied transition laws coincide. It locates the source of their computed disagreement, but is not independent evidence that the original feedback law occurs in nature. Similarly, a different rival could match the proposed intervention effect. The test discriminates these specified models.

One wording clarification for future use: the common initial state has two skilled carriers but no installed frame. Call it “initially unrepresented” or “without an installed frame,” rather than the design note's “untrained” state. No calculation depends on that wording.

## 4. Audit of the prospective design

The two-stage handoff design is causally coherent within its communication boundary and is explicitly unrun. Baseline outcomes are measured before disclosure randomization; the package is sealed before access randomization; and the primary estimands retain all assigned lineages. These choices avoid conditioning on post-disclosure package production or subsequent survival.

Before implementation, preserve the following distinctions in the operational protocol:

1. **Allocation, delivery and use are separate measurements.** Record the work slots allocated, the artifact actually delivered, its accessible contents, successor exposure and subsequent use. An intention to maintain is not a delivered capability. The proposed primary maintenance indicator may be “a completed package produced using a work slot,” provided completion has a fixed observable definition.
2. **Assignment to access is not actual receipt or use.** The randomized B contrast is an intention-to-treat effect of making the specified packet accessible. Logged opening, comprehension or use are downstream outcomes, not grounds for excluding a lineage. The current access intervention need not produce a useful packet or an obedient successor. A received-treatment or latent-capacity causal effect would require additional assumptions.
3. **Outcome disclosure is not outcome production.** A randomizes the timing of truthful information about prior errors. It identifies an informational route into maintenance. Error severity itself is not randomized; pre-A error strata estimate moderation of disclosure, not the effect of inducing errors or injury. This also means the empirical intervention does not directly validate the numerical harm-to-turnover law.
4. **Task correctness is a declared reference standard.** In a benign classification task, “harm” should mean the prespecified error or burden measure, not an unsupported equivalence to human welfare. Record initial errors, later correctness, deadline completion, service sacrificed and inherited-rule compliance separately. Do not redefine success after observing treatment effects.
5. **The second arrow remains intervention-specific.** B randomizes a package-access policy conditional on whatever the founder produced. Its effect is not the effect of setting every possible value of the post-A maintenance variable M. The factorial interaction is identified by assignment; a natural indirect effect through M is not supplied by this design alone.
6. **One handoff tests a causal segment.** A second prespecified generation is needed to observe the newly produced outcomes feed into another maintenance decision. Even that establishes a finite repeated mechanism, not indefinite self-maintenance.

The current design already states these principal limits, including no post-treatment package selection, no mediator-regression shortcut, and separate allocation denominators and task nonresponse. The points above sharpen what must be logged and named; they do not require altering the synthetic code or promoting a new empirical claim.

## Provenance

- Formation source SHA-256: `82045d4ef5d29efbbf2ccdcc9ea3180de5b591428292689e9ccf60ee3941aeca`.
- Discrimination source SHA-256: `c79c92fa500e900a71087015e806aecf54afdfcff1e8b817f95df9a84ff436ea`.
- Audited discrimination output SHA-256: `b029f0a1b790f59558f42687c021451a2ee5a972cc1ec20d321a69752cb7acad`.
- Independent raw-case enumerator SHA-256: `fb39a40507661dc3d8ec51e158a4d132d0763d4ffcb065ab4ab0af58e245835f`.
