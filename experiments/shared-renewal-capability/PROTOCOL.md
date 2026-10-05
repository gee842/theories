# Protocol: joint assays of the existing renewal process

5 October 2026, AI-assisted mathematical experiment for Ren. Recorded before numerical results. This uses the event law already declared in [the stochastic realization](../../_process/research/2026-10-05-support-and-shared-generativity/completion/STOCHASTIC-REALIZATION.md), without new productive reactions, controllers or favorable transition rates.

## Question and fixed comparison

Compare the actual finite-horizon outputs of the same preparation under recycling coefficient theta=0 and theta=4. Fix V=epsilon=a=b=d=beta=k=ell=g=1, N=M=3, and initial counts (R,C,Y,D,F)=(0,1,1,1,1). A compatible source has eta=1 and incident power density I=3. The two parameterizations have identical source, initial material and reserve, and all other event rates. The altered catalytic coefficient is a model-level intervention, with no claim that converting between two physical catalysts is free or available. The comparison is between two supplied preparations, not a construction theorem.

Evaluate horizons H=0.05,0.25,1 and reliability alpha=0.5. These small-system, finite-time choices are exploratory mechanism tests, not fitted physical parameters or an empirical universality sample.

## Actual joint tests

Let J count D→R recycling events from either catalyst. Let B count R→C assembly events. Let F_H be the remaining usable packets and A_H=R_H+C_H+Y_H the remaining active material. For q=(j,b,f) in {0,1}^3, test jointly

    J_H >= j, B_H >= b, F_H >= f, A_H >= 1.

The final active-material requirement also ensures activity never reached the absorbing all-degraded material face before H. It does not guarantee indefinite continuation or protect every differentiated carrier. Resource conversions are physically delivered events; the final energy reserve is a readiness constraint, not automatically a further delivered function.

The fixed protocol is to run the already installed process for the stated horizon. The model does not condition actions on the analyst's event counters. Counters define the physical assessment; no free sensing, computation or actuator is granted to an actor. Measuring them experimentally would require an identified instrument and its effects.

The resulting reliable set is exact for this singleton protocol class. It is only an inner bound for a larger class of implementable controllers. A failed fixed-run profile does not establish impossibility under all physically realizable interventions.

## Numerical method and error accounting

Augment the same count process with both event counters capped at one. Cap the energy count at K=12 for H<=0.25 and K=24 for H=1. Send transitions exceeding that cap to a marked overflow state; do not silently suppress their propensity. This yields a finite chain with an exact uniformization expansion.

Compute lower and upper arithmetic bounds using directed decimal rounding for nonnegative transition probabilities and Poisson weights. Bound all omitted Poisson terms by their total mass. Overflow contributes zero to every lower bound and its entire mass to every upper bound. Thus bounds apply to the original countable-state process, provided the implementation matches the declared generator. Independently compare numerical central values and the generator's drift/accounting where practical.

Report every declared profile and both positive and negative comparisons. Determine reliable profiles only when the interval lies entirely on one side of alpha; otherwise report unresolved. Opposite signs for two output events establish delivery-law non-dominance; incomparable capability sets at one fixed alpha require separate certified crossing witnesses at that alpha.

## Analytical predictions and boundaries

With lambda=1+theta, small-H expansion predicts recycling probability lambda H+O(H²), retained-reserve probability 1-(2+theta)H+O(H²), and joint recycling-plus-assembly probability lambda H²/2+O(H³). Thus the whole delivery vector is not universally improved by increasing theta. These expansions alone do not prove incomparable regions at alpha=0.5.

All results concern a stipulated passive mesoscopic mechanism. Physical catalyst identification, construction costs, a broader admissible protocol class, formation/selection of theta, long-time transition reduction and universal direction remain separate obligations.
