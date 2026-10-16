# Independent review of bounded evaluative identification

6 October 2026. AI-authored internal collaborating-agent review. **Accepted for the bounded analytical, formal and numerical scope below.** This is internal collaborating-AI review, not external peer review. The prospective review and declared grids are preserved in the [development record](../../../../experiments/recipient-value-learning/bounded-identification/development/prospective-review.md); this unchanged snapshot retains its original review-directory link base, as recorded in its [provenance](../../../../experiments/recipient-value-learning/bounded-identification/development/prospective-review-provenance.json). The reviewer did not write the analytical note or Lean producer. No empirical observations, estimators or accepted results are changed.

## Named contribution and overlap

The accepted [identification argument](IDENTIFICATION.md) already proves that unrestricted private expectancy can absorb an apparent change in recipient evaluation. The [canonical empirical account](../../../../theories/becoming/history/REWARD-LEARNING-AND-RECIPIENT-CHOICE.md) asks for a new-recipient contrast exceeding independently bounded unchanged-evaluation alternatives. The [new mathematics](BOUNDED-IDENTIFICATION-MATH.md) supplies an explicit ceiling for that previously qualitative requirement. It is a conditional identification result, not evidence that those measurement bounds already hold in humans, and not a new apparatus or an ethical derivation.

## Independent mathematical assessment

Let the common paired population have response probabilities `r_j`, choice probabilities `p_j`, response means `R_j` and offered-choice means `L_j=E[r_j p_j]`. On a common covered set of mass at least `1−ε`, suppose `|p_1−p_0|≤m`. The fractional common response is `h=min(r_0,r_1)`. The good-set overlap satisfies

`E[1_G h] ≥ max(0,R_0+R_1−1−ε)`.

On the good set, direct decomposition gives `r_1p_1−r_0p_0 ≤ r_1−(1−m)h`; outside it the difference is at most `r_1`. Integration gives the proposed upper bound, and exchanging arms gives the lower bound. No independence of response, choice or latent type is needed.

The five-stratum construction is sharp for fixed marginal response levels. It first minimizes their intersection, assigns as much of that intersection as allowed to the uncovered set, and centers the remaining common logits. With arbitrary bounded probabilities the extrema are attained. With finite logistic logits, exclusive-response and uncovered strata generally need limits toward probabilities zero or one: the corresponding result is a sharp supremum, not a generally attained maximum.

The independently derived logistic displacement maximum is `m=tanh(D/4)`. The earlier pointwise gate-cap envelope is also correct, including its `exp(D)(1−ρ)≤1` branch and its `D=0` boundary. A mean absolute gate-change bound gives a different envelope. Neither can use `|R_1−R_0|` as a substitute for a paired gate-change bound.

## Assumptions that cannot be supplied by the contrast itself

1. The bound concerns a common paired population. Random assignment identifies marginal potential means under appropriate observation/sampling conditions; it does not identify latent cross-condition pairs or cure post-assignment selection.
2. Under fixed recipient evaluation, the nuisance budget must bound the full score displacement, including baseline, factual expectation and `Δ(βe)`. Holding the mean of a belief report fixed does not bound individual score changes; allowing payoff sensitivity or baseline to move freely restores the original nonidentification.
3. The exception budget is for paired validity. Two armwise error budgets require their union allowance unless their overlap is independently justified. It is not legitimate to count each arm's calibration as the same covered population automatically.
4. Rejection concerns the joint unchanged-evaluation/model/nuisance/measurement/population class. Attributing rejection uniquely to acquired evaluation needs independent support for the other restrictions. Effective recipient valuation is not an ethical ground, and a product coefficient need not identify its constituent mechanisms.
5. The existing 333 eligible or 385 saved records do not establish `D` or `ε`, or eliminate missing-population concerns. No application to those observations is licensed by this theorem alone.

## Sampling uncertainty review

For two predeclared arms with independent bounded participant-level observations of offered-choice fraction and response fraction, four simultaneous Hoeffding intervals may use arm-specific radius `sqrt(log(8/α)/(2n_j))`. Each two-sided interval fails with probability at most `α/4`; their union therefore fails with probability at most `α`. Choice and response statistics within a participant may be correlated. Participants, not their individual repeated trials, are the independent units.

The upper null ceiling `B` is nonincreasing in `R_0` and nondecreasing in `R_1,m,ε`. Thus a sufficient positive rejection rule is

`L_1,lo − L_0,hi > B(R_0,lo, R_1,hi; m, ε)`.

Intervals are clipped to `[0,1]`. Plugging estimated response means into the ceiling does not provide this guarantee. The same simultaneous rectangle supports the mirrored negative rule without an extra direction-selection allowance. Estimated calibration budgets must join the coverage accounting. Outcome-dependent sample selection, optional stopping or additional strata need their own valid sampling contract; ordinary fixed-size intervals do not establish it. This review does not claim an optimal-power test or calculate a test result on the old data.

## Declared independent finite checks

The following scope was fixed before running the checker. All calculations use constructed populations, with no imports from the formal producer and no empirical data reads.

- Exact sharp witnesses: `m,R_0,R_1,ε` each range over `{0,1/4,1/2,3/4,1}`, with both signed endpoints and all probability/coverage constraints checked.
- Exact inequality stress: every ordered pair of atoms whose four gate/probability coordinates are in `{0,1/2,1}` and whose covered flags are Boolean, mixed with weights `{0,1/4,1/2,3/4,1}`. Use each population's strongest applicable good-set displacement bound and exact uncovered mass.
- Real-variable diagnostics: fixed grids `D∈{0,.1,.5,1,2,4}` and `ρ∈{0,.05,.25,.5,.9,1}`; dense logit evaluation and analytic maximizing points check the hand formulas. These floating checks supplement the proof; they do not machine-prove real calculus.
- Fault cases: equal mean gates with opposite individual response selection; equal mean expectancy with nonlinear choice; disjoint armwise calibration failures; and treatment-dependent selected populations. All are exact constructed counterexamples except the explicitly numerical logistic approximation.
- Boundary and statistical checks: monotonicity of the exact frontier, symmetric arm reversal, zero/full response and coverage limits, and conservative confidence-rectangle endpoints.

The [checker](../../../../experiments/recipient-value-learning/bounded-identification/check_bounds.py) and [passed result](../../../../experiments/recipient-value-learning/bounded-identification/checks.json) are saved. No claim of whole-foundation completion follows from this bounded discriminator.

## Completed checks and preserved correction

The independent calculation passed 1,250 signed sharp witnesses, 131,220 ordered two-atom mixtures, 45,927 applicable mean-absolute gate bounds, 5,625 confidence rectangles with 30,625 interior comparisons, and 5,625 budget-monotonicity comparisons. It checked 288,036 dense logit evaluations across the 36 declared `(D,ρ)` combinations and 500 finite-logit approaches to the sharp response-level frontier. The canonical example is exactly `117/1000`. These finite and floating checks supplement the proofs; they do not establish the general real-variable or statistical claims by enumeration.

Four retained countermodels show why the missing premises matter. Equal response means coexist with offered-choice change `1/4` and no conditional-choice change. Equal mean private expectancy coexists with conditional-choice change `1/14`. Two disjoint armwise exception sets of mass `1/4` each permit a change `2/5`, exceeding the incorrectly reused single-arm bound `1/4` but respecting the correct paired bound `1/2`. Treatment-dependent selection creates an apparent change `1/2` from a common population with zero change. None is a participant observation.

The first computation completed all assertions and saved a passed scientific report, then failed while printing a `Fraction` in its final stdout summary. The only code correction applies the existing serializer to that summary. The subsequent run exited successfully with unchanged grids, formulas and assertions. The [first-failure record](../../../../experiments/recipient-value-learning/bounded-identification/development/first-stdout-reporting-failure/provenance.json) preserves the error and source: the original source was reconstructed by reversing that one reporting patch and matched its independently recorded pre-run SHA256. The original report's values were recovered from the saved prior-attempt record; its pre-overwrite byte hash was not recorded, so exact original receipt-byte identity is not claimed. This reporting correction changed no scientific result.

## Formal proposition and receipt review

The two source modules and the fresh-build checker were read independently. The [current Lean receipt](../../../../experiments/recipient-value-learning/formal/verification.json), saved build copy, both source snapshots, both logs, compiler binary, pinned toolchain, prospective contract and checker hashes match. All 27 audited declarations—16 in `OfferedChoiceBounds`, 11 in `OddsEnvelope`, including algebra helpers—have the stated standard `propext`, `Quot.sound` and `Classical.choice` dependencies, with no custom axiom, proof hole or unchecked native decision. This review inspected the frozen build evidence and did not rerun that build.

The main theorem concerns arbitrary finite rational weighted paired populations satisfying the explicit range, normalization, coverage and probability-gap premises. General sharpness uses three separate claims: validity of the constructed population, its accounts and attainment. The algebraic account statement alone allows inputs outside the probability domain; the validity theorem supplies the required restrictions. The mirrored bound does not assume equal response rates.

The odds module proves a pointwise quadratic equivalence after clearing positive denominators. Its coefficient/discriminant condition is a sufficient certificate for that quadratic, not an asserted necessary criterion. Its paired-gate transport uses a unitwise gate premise, not a marginal gate difference. The source does not silently formalize exponentials, square roots, real calculus, integration, Hoeffding concentration or empirical calibration. Those arguments have the separate analytical review above. At `r_j=0`, the latent conditional-choice value is a declared model extension, not an observable conditional probability.

## Final integration verdict

The [canonical account](../../../../theories/becoming/history/VALUATION-IDENTIFICATION-BOUNDS.md), mathematical companion, formal README and three owned research-map fragments accurately distinguish sharp bounded-probability attainment, finite-logit suprema, the sampling contract and the unestablished measurement premises. The fragment texts are bound individually because other sessions are editing the surrounding maps. The [review receipt](bounded-identification-review.json) identifies the frozen reviewed files without recursively hashing itself.

The accepted addition is a quantitative discriminator for a named unchanged-evaluation class. It advances the existing foundation's empirical-identification obligation without changing the five completion conditions. Common-population transport, bounded latent alternatives, fixed decision scale and valid measurement coverage remain supplied requirements for empirical use. No new data are analyzed, no old estimate is reinterpreted as a significant effect or an equivalence result, and no ethical warrant is inferred. Formation, persistence through succession, fresh correction and justified action remain the separately owned constructive connections. No substantive blocker remains for this scoped acceptance.
