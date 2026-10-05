# Diagnosing the effect of constructing a regulator

5 October 2026. AI-assisted secondary analysis of the saved regulator comparison. This diagnostic is specified before its own numerical decomposition, but its case is selected after seeing the original outcomes. It is not an independent prospective confirmation.

## Question and fixed case

Decompose the negative construction effect in the existing network at g=8, H=3, original profile (1,1,1): recycling and C assembly have occurred, at least one free fuel packet remains, and productive material A remains. Retain all supplied rates, material N=3 and the original zero-regulator preparation. No parameters or reactions are tuned.

Use the exact finite-generator identity in the mathematical [response note](../../../../_process/research/2026-10-05-support-and-shared-generativity/completion/REGULATION-RESPONSE.md). The changed law has kappa=1, alpha=mu=4. The conditional baseline has kappa=0 but retains alpha=mu=4 on states containing G. It agrees with the absent-regulator arm from the initial zero-G preparation, while supplying the correct hypothetical conditional futures after construction. Both generators use the same closed responsive state graph, including capped assay flags and total-packet overflow.

The local contribution at time t and augmented state z is

`p1(t,z) * R*F * [u0(H-t, construct(z)) - u0(H-t,z)]`.

The total over states and time equals the terminal success difference in exact arithmetic. Resource and material costs occur in the construction update. The decomposition keeps all later binding, wear, and productive consequences; it does not separately identify a pure energy cost, a pure material cost, or a pure feedback benefit. The baseline continuation disables further construction; the outer occupation law retains it. That reference choice is part of the decomposition and cannot be suppressed in interpretation.

## Outputs

Report endpoint probabilities, integrated signed effect, positive and negative contributions separately, and counts of reachable construction states with meaningful positive or negative contributions. Retain the largest state contributions of both signs, grouped totals by productive material and whether C is present, and time bins [0,.25,.5,1,2,3]. Report whether unused free reserve has a known competing productive demand in this model; the numerical effect alone cannot establish that purpose.

## Numerical checks and scope

Compute matrix exponential trajectories and backward success functions on uniform grids of 192 and 384 intervals at packet cap 48, integrate using composite Simpson quadrature, and compare the integral with the independently computed endpoint difference. Repeat cap64 at384 intervals as a truncation sensitivity check. If an integral/endpoints residual exceeds 1e-7, refine to768 intervals and disclose all resolutions. Do not claim an interval certificate from empirical convergence. Sign-separated integrals may converge more slowly because clipping creates nonsmooth points.

Original-process endpoint error is bounded by each arm's overflow in exact arithmetic. Individual state/group attribution is representation- and baseline-dependent and does not inherit the same one-sided overflow bound automatically. Numerical arithmetic errors and quadrature errors remain separate. An independent checker should verify the common-state generators and use an augmented block-matrix exponential for the net identity, avoiding numerical time quadrature. No new empirical observations are collected.
