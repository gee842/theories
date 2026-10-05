# Testing bounded rule revision under separate operating constraints

5 October 2026. AI-assisted model experiment following the [systems study](../systems-dynamics/README.md). This protocol is written before running the new controller comparisons. It is an internal, time-ordered research record, not an independent preregistration. The preceding target-only failure and recovery cases are already known. No empirical data are used.

## Question and scope

Can a bounded-rate maintenance-rule controller preserve distinct operating conditions while pursuing changing verification targets, without adding resources to the operating ledger? Does it add anything beyond a fixed rule, slower response or fixed cap? The analysis will distinguish an invariant-set guarantee from sampled target tracking and from full viability-kernel computation.

Use the canonical constitutional-extension equations unchanged, except that m becomes a controlled state and u=mdot is bounded by .5 in absolute value. All controllers share initial state, operating resources, physical equations and access to the exact state. Observation and governance remain unpriced assumptions, and identical access does not mean identical information-processing cost. Report rule variation separately rather than pretending the unpriced actuator is a funded institution.

## Proposed controller and conditions

Protect x>=.9, h>=.9, C>=2.5, G>=2.1, m>=.45, and b=D-m-.02>=0, where D=hG/(1+G). These floors are declared design choices, not discovered human values. The protected region is a sufficient subset, not the full set of viable or recoverable states.

For alpha=2 and R=.5, require u in [max(-R,-alpha(m-.45)), min(R,Ddot+alpha*b)]. Compute Ddot from the actual four-state plant. Project the nominal response epsilon*m*(1-m)*(target-G) into this interval. Prove feasibility on the entire protected region before claiming invariance. Outside it, report that the certificate does not apply; never silently swap reversed interval endpoints.

## Comparators

Compare the filtered controller with the same nominal target-only response, a ten-times-slower response, a fixed initial rule (.5 in reference cases; .45 or .5 in the grid), a bounded-rate move toward the known full-operation equilibrium rule target/6, and constant upper caps .6, .7 and .8 with the same rate limit. The constant caps use derivative barriers with the same alpha and lower floor .45. A fixed rule can preserve operation yet fail to track a requested target; report those outcomes separately. A simple cap matching the filtered rule weakens any claim that state-dependent control is necessary.

## Cases fixed before these runs

1. Reference state (x,h,C,G,m)=(.94,.93,2.7,2.4,.5), target 4, epsilon 1. Known failure for the preceding unbounded-rate target response.
2. Same state, target 3.6, epsilon 10. Known counterexample to the claim that rapid response is always harmful.
3. Reference state, target sequence 4, 4.7, 3, 6, 4, with 150 time units per phase. The target 6 deliberately tests refusal or saturation under incompatible requirements; the controller must not be credited with achieving it.
4. A Cartesian grid x in {.9,.94,.99}, h in {.9,.95,.99}, C in {2.5,3}, G in {2.1,3}, m in {.45,.5}, target 4.7, epsilon 1. All 72 starts lie in the claimed protected region. This grid is a declared comparison set, not independent validation of a data-fitted model.
5. Out-of-certificate initial conditions and at least one analytically impossible boundary case. Report lack of certification separately from actual failure or impossibility. Do not interpret every point outside the sufficient region as nonviable.

## Measurements and checks

Record each protected margin separately, late target error, final state, peak work requirement, total integral of abs(u), nominal-control intervention, and any explicitly certified loss entry. Do not combine these into an overall score. An operating-floor breach is not automatically operating collapse.

Use the existing model as the source of equations, preserve its hash, independently check the barrier feasibility inequalities, and compare selected trajectories with a second adaptive solver. Record numeric tolerances and refine if conclusions depend on solver error. A mathematical invariant-region proof supplies the guarantee; numerical checks do not establish exact geometry or robustness to unmodeled disturbances.

Any additions after inspecting outcomes must be labeled exploratory. Preserve adverse controls and negative results in the synthesis. Do not claim endogenous goals, consent, legitimacy, protection against all strategic practices, empirical validity, or a solution to AI alignment.

## Exploratory addition after the initial comparison

The [original protocol](PROTOCOL-INITIAL.md) is preserved. The first runs showed that the equilibrium-rule comparator could reach G near 6 during the finite target phase, despite violating the protected incentive margin. Earlier favorable selection had made the represented false-maintenance alternative extremely rare. This is an informative counterexample to identifying every margin violation with immediate operating failure.

Add a separate exploratory version of the changing-target case: at time 450, when the target changes to 6, impose h := min(h,.99) for every controller. This reintroduces a one-percent represented alternative where it was rarer; it is not an endogenous mutation model. Apply the identical map, preserve all other state variables, and record the realized jump and post-jump certificate membership. Already depleted arms experience little or no change. Test whether apparent target success survives that perturbation. Keep the original unperturbed result.

Also report integrated fee revenue and delivered maintenance expenditure as separate endogenous outcomes. This adds resource-accounting visibility, not a new controller or an assumption that all arms must realize identical revenue.
