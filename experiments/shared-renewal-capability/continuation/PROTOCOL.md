# Delivered-continuation comparison

5 October 2026. AI-assisted mathematical follow-up. Written before this calculation, after observing the earlier readiness tradeoff and regulator failure. This is a prospective specification for a secondary model experiment, not a preregistered empirical test. The original models, protocols and results remain unchanged.

## Question and fixed preparations

Does the same coupled process actually assemble again after its initial activity, and how does that relate to free fuel at the intermediate time? The [opportunity audit](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/REGULATION-OPPORTUNITY-AUDIT.md) motivates this distinction. No new controller, reaction, favorable rate or optimized intervention is added.

Use the frozen [regulator event table](../regulation/compare.py), material total N=3 and initial state (R,C,Y,D,F,G,GF,YG)=(0,1,1,1,1,0,0,0). Include these twelve cases:

- Two original catalytic preparations: g=1, absent regulator, theta=0 or4. Implement the theta change only in free-Y recycling. This is a comparison of supplied catalysts, not paid construction of a different theta.
- The ten previously fixed regulator preparations: g=4 or8; absent, burden, buffer, inhibitor and responsive arms; theta=4 throughout. Rates, material costs and bound-Y reproduction remain exactly as in the earlier comparison.

H=tau is 0.25,1 or3. The process runs autonomously for H+tau. Reliability alpha=0.5. The chosen horizons extend the previously used cases; they are not selected after this assay's outcomes.

## Common sequential assay vocabulary

For each (j,b,f,n) in {0,1}^4 require jointly:

    J_H >= j, B_H >= b, F_H >= f,
    B_(H+tau) - B_H >= n,
    A_s >=1 for every 0<=s<=H+tau.

J and B count actual recycling and C assembly; F is free fuel and A=R+C+Y+YG is productive material. A=0 is invariant, so final survival enforces the full path condition. The primary repeated-delivery profile is (1,1,0,1): initial recycling and assembly, another assembly later, and continuing productive material. These are sixteen profiles of a new sequential vocabulary, not a reclassification of the old eight tests, whose survival requirement ended at H. Extra assembly need not use newly captured energy: reusable material, stored R and later recycling are all legitimate routes.

For the primary profile, partition entry at H into F_H=0 and F_H>=1. Report each entry mass, its joint repeated-delivery probability and, when the entry mass is positive, their ratio. These strata depend on the preceding dynamics. Conditional ratios describe selected states; they do not identify the causal effect of possessing a fuel packet. The two joint contributions must sum to the primary result.

Time windows and event counters belong to the analyst's assessment, not a free physical controller. Experiments measuring them need their own observation implementation. One repeated function is not indefinite renewal, every future capability, newly evolved architecture or a universal direction.

## Exact finite-chain identity and numerical method

Use the original augmented reachable graph with flags for historical recycling, assembly and regulator construction. Let Q be its function-column generator. Let C contain only the off-diagonal rates for labeled C-assembly events, including events whose historical flag is already saturated. Define K=Q-C: remove assembly arrivals but keep their loss in the diagonal. This sub-Markov generator counts trajectories with no further assembly.

For final productive-survival indicator h and a diagonal prefix selector D_(j,b,f), the n=1 probability is

    p0^T exp(H Q) D_(j,b,f) [exp(tau Q)-exp(tau K)] h.

For n=0 replace the bracket by exp(tau Q). A marked-process reconstruction of the first later assembly can check this identity without subtraction. Prefix probabilities at H are also retained to compare the earlier readiness measurement with this longer test.

Stop at an absorbing failure state when U=F+GF exceeds Kcap=48, then repeat every case with Kcap=64. Do not delete an overflowing capture propensity. Finite success is below original success, and finite success plus initial-preparation overflow through H+tau is above it in exact arithmetic. A global overflow bound is used even though it may be conservative for a selected prefix. Report all caps and all profiles. No parameter changes or additional favorable-arm searches are part of this protocol.

Compute forward laws and backward functions with sparse matrix-exponential actions in float64. Preserve raw results, mass errors, generator identities, fuel-partition residuals and subtraction minima. A tolerance of1e-10 is an implementation-comparison tolerance, not a proved arithmetic enclosure. Numerical reliability classification uses the finite success/overflow interval, with values within1e-10 of alpha labeled numerically unresolved. Negative probabilities below -1e-10 or structural-check failures require investigation, not silent clipping. Smaller signed residuals remain visible.

An independent implementation must reconstruct the labeled reactions and use a positive marked process for selected cases, including the primary profile at all three horizons for g=1/theta0 and4, and g=8/absent and responsive. Record every inspected input hash. Independent agreement does not convert these calculations into interval-certified probabilities or empirical observations.
