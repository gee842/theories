# Independent review of bounded evaluative identification

6 October 2026. AI-authored internal collaborating-agent review. **Prospective status: the analytical contract passes independent review; numerical checks and frozen formal receipt are pending.** The reviewer did not write the analytical note or Lean producer. No empirical observations, estimators or accepted results are changed.

## Named contribution and overlap

The accepted [identification argument](IDENTIFICATION.md) already proves that unrestricted private expectancy can absorb an apparent change in recipient evaluation. The [canonical empirical account](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/REWARD-LEARNING-AND-RECIPIENT-CHOICE.md) asks for a new-recipient contrast exceeding independently bounded unchanged-evaluation alternatives. The [new mathematics](BOUNDED-IDENTIFICATION-MATH.md) supplies an explicit ceiling for that previously qualitative requirement. It is a conditional identification result, not evidence that those measurement bounds already hold in humans, and not a new apparatus or an ethical derivation.

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

Before running the new checker, its scope is fixed as follows. All calculations use constructed populations, with no imports from the formal producer and no empirical data reads.

- Exact sharp witnesses: `m,R_0,R_1,ε` each range over `{0,1/4,1/2,3/4,1}`, with both signed endpoints and all probability/coverage constraints checked.
- Exact inequality stress: every ordered pair of atoms whose four gate/probability coordinates are in `{0,1/2,1}` and whose covered flags are Boolean, mixed with weights `{0,1/4,1/2,3/4,1}`. Use each population's strongest applicable good-set displacement bound and exact uncovered mass.
- Real-variable diagnostics: fixed grids `D∈{0,.1,.5,1,2,4}` and `ρ∈{0,.05,.25,.5,.9,1}`; dense logit evaluation and analytic maximizing points check the hand formulas. These floating checks supplement the proof; they do not machine-prove real calculus.
- Fault cases: equal mean gates with opposite individual response selection; equal mean expectancy with nonlinear choice; disjoint armwise calibration failures; and treatment-dependent selected populations. All are exact constructed counterexamples except the explicitly numerical logistic approximation.
- Boundary and statistical checks: monotonicity of the exact frontier, symmetric arm reversal, zero/full response and coverage limits, and conservative confidence-rectangle endpoints.

The checker and its receipt will be saved in [bounded-identification](../../../../experiments/recipient-value-learning/bounded-identification/). Final acceptance will separately inspect the additive formal proposition scope, frozen source/build hashes and final analytical/canonical wording. No claim of whole-foundation completion follows from this bounded discriminator.
