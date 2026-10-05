# Independent audit of root calculation

5 October 2026. Reviewed `work/check_scientific_principles.py` and `outputs/verification-results.json` without modifying either.

The recurrence stores probability mass for paths that have not yet rejected, absorbs rejected branches exactly once, and preserves total mass at every step. Expected samples accumulate the probability of still sampling immediately before each observation; this is the finite tail-sum identity. Binomial tails and likelihood ratios are exact fractions.

Independent implementation in `work/formal/checks.py`, run with the root's alternative .75 and horizon 100, agrees on likelihood-ratio crossing probabilities: .04088964341296718 under p=.5 and .993448809246945 under p=.75. The independent binomial-tail implementation agrees on n20 threshold-15 power .6171726543871046 and terminal n100 null rejection .04431304005703379.

An additional read-only audit enumerated all 4,096 binary paths of length 12 with exact rational weights at each of p=.5 and p=.75. It compared direct stopping time and rejection sums against the root recurrence for (i) LR(.75/.5)≥20, (ii) repeated ordinary exact p≤.05, and (iii) a terminal-only n12 exact p≤.05 rule. All six probability and six expected-sample comparisons agreed exactly.

The root's built-in n10 brute-force check is nontrivial for sequential rules but vacuous for its terminal-only rule because that closure retains nmax=100. The supplemental terminal12 check addresses that narrow test-coverage gap. This does not identify a defect in the calculation or require changes to its results.

Statistical interpretation: the ordinary repeated-p procedure's .20205809786793333 rejection probability violates a .05 lifetime Type I claim while preserving each fixed-time test's marginal guarantee. Spending and likelihood procedures are valid under the stated iid simple null. The latter also extends to predictable Bernoulli null success probabilities ≤.5 with this fixed .75 alternative, because each multiplicative factor has conditional expectation .5+p_t≤1; that extension is not needed for the reported result. No independence claim about repeated prefix tests is needed. The causal and XOR measurement tables match their declared structural equations; they are constructed illustrations rather than empirical estimates.

No statistical or recurrence errors found. Exact arithmetic verifies finite model calculations, not the model's adequacy for actual scientific practice.
