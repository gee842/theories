# Protocol for endogenous continuation of correction

5 October 2026 task date supplied by the environment. Written before the new numerical study. AI-assisted research record; this is a synthetic institutional model, not a paper draft or a fitted description of a real institution.

## Question and scope

Can a system that currently corrects errors continue to select, transmit and execute the practices that enable correction? The study joins five previously separated mechanisms: changing appointment criteria, inquiry and admitted memory, implemented response, reproduction of skill, and succession. It uses work time and skilled carriers, not money or monetary payoffs. Normative commitments and the finite repertoire of practices remain specified by the analyst. Goal formation outside that repertoire is not solved.

The model was designed with adversarial review before implementation. An initial sketch made institutional renewal independent of experience and outcomes; that would not close the proposed loop. The frozen primary construction therefore includes an explicitly assumed pathway from inadequate responses to increased attrition and replacement. Its removal is a required control.

## State and events

State is `(e,r,q,k,b)` with context `e=0/1`, implemented routine `r=0/1`, installed criterion and inherited decision practice `q=volume/adaptive`, number of skilled carriers `k=0,1,2`, and admitted record `b=none,0,1`. There are 72 formal states, including some unreachable combinations. The policy never observes the hidden context directly.

Each period has the following order:

1. The context switches with probability `hazard`.
2. If skilled capacity is absent, an independently supplied entrant arrives with probability `entry`, bringing one skilled carrier and the adaptive practice. This is an explicit external source; no claim of endogenous regeneration at zero capacity follows.
3. Two available work slots are allocated by the installed practice. Volume uses both for cases (`F`). Adaptive uses one for a case and one for inquiry at `k=2` (`Q`), or one for a case and one for apprenticeship at `k=1` (`T`). At `k=0`, both practices use `F`. An action never simultaneously performs inquiry and apprenticeship.
4. Inquiry yields a context report of accuracy `accuracy`. The raw report is admitted to `b` if the admission gate is enabled. On periods without an admitted report, the previous record remains. The adaptive practice implements the routine named by its admitted record when execution is enabled and capacity is positive; volume follows its current routine. The comparison of report and old routine records discrepant evidence; a changed routine is recorded separately from a correct change.
5. Each completed case is adequate exactly when the implemented routine matches the current context. Record adequacy, number of completed cases, and number of adequate cases separately. These are not added into one welfare score.
6. Delivered apprenticeship adds one skilled carrier, capped at two; it requires at least one current carrier. The no-training arm spends the same slot but delivers no new carrier.
7. Attrition and associated appointment occur with probability `delta_base + delta_failure * inadequate`. This models an assumed consequence of failed work, such as withdrawal or overload. It does not provide a perfect diagnostic report to the policy. At most one skilled carrier is lost in an epoch. If no turnover occurs, the incumbent practice continues.
8. At turnover, after the loss, appointment selects the adaptive practice with probability `k*w_q/(1+k*w_q)`. Here `k` represents relative availability of qualified adaptive candidature and `w_q` the currently installed criterion's relative weight on its inquiry/teaching portfolio. This formula is a stipulated appointment mechanism, not a derived universal law or an empirically estimated score. Baseline weights are `w_volume=.25, w_adaptive=4`. A protected-succession comparison appoints adaptive whenever `k>0`; a volume-only comparison appoints volume. A record is forgotten with probability `forget` at turnover. The implemented routine is retained.

This yields the loop: implemented criterion/practice → inquiry and teaching → action consequences and skill → attrition, eligible succession and criterion/practice inheritance. It also represents memory transmission. It does not include strategic lying, the emergence of a new representational grammar, legitimate political goal revision, or unlimited institutional self-modification.

## Primary parameters and comparisons

Primary values: `hazard=.05`, `accuracy=.95`, `delta_base=.05`, `delta_failure=.20`, `forget=.10`, `entry=0`. Initial state is `(0,0,adaptive,2,0)`. Primary horizons are 200 and 2000 periods. State and first-period work are matched across appointment comparisons.

Required arms:

- Endogenous criterion-dependent appointment.
- Protected adaptive succession, with the same imperfect evidence and material processes.
- Volume-only succession.
- New evidence not admitted; raw inquiry still occurs.
- Amendment execution blocked; inquiry and admission still occur.
- Apprenticeship delivery absent; work time is still spent.
- Criterion feedback removed: both appointment weights equal one.
- Perfect inquiry, with actual endogenous appointment.
- External re-entry probability `.01`, with actual appointment.
- Rare adverse succession: adaptive appointment weight `10000`, volume weight unchanged.

The protected-succession arm is an externally stipulated benchmark, not a proved institution that maintains its own successor filter. No arm is designated aligned simply because it remains operational.

## Predictions and potential refutation

1. **Internal continuation differs from available control.** With no re-entry, finite positive appointment weights and positive base turnover, all endogenous states with capacity should eventually lose capacity. The protected adaptive succession arm should retain at least one carrier from the initial state. Exact support, not a long simulation, tests this claim.
2. **Regeneration matters independently of knowledge.** Perfect inquiry alone should not remove the eventual loss mechanism. Disabling apprenticeship should eliminate protected capacity persistence even under adaptive succession. A contradiction defeats the proposed mechanism or reveals an implementation error.
3. **Information and execution are separate.** With the same initial routine and no alternative diagnostic response, blocking new admission or blocking execution should yield the same observable routine, adequacy and skill distributions, despite different evidence records. Their latent memory distributions need not match. Raw report, admission and execution are logged separately.
4. **Experience can feed back into institutional continuation.** With failure-induced turnover removed, the capacity/criterion dynamics must be identical across the ordinary, no-admission and no-execution arms. With it present, differences are possible. We do not preregister a universal monotone sign: faster replacement can both remove and install adaptive practices.
5. **Finite reliability differs from indefinite preservation.** Rare adverse succession can yield high finite-horizon retention while leaving no closed persistent region. Any positive transition probability remains in graph analysis.
6. **Environmental openness matters.** Re-entry may restore recurrent inquiry and teaching after depletion. It does not make every path permanently safe, nor establish self-sufficiency.

## Analysis and verification

Construct and check the exact finite transition matrix by enumerating event branches. Determine reachable states, bottom strongly connected components and the greatest closed subset of `k>=1`. Record inquiry, admitted discrepancy, training, implemented revision and beneficial revision as transition events rather than labels attached to healthy-looking states. Compute finite-horizon first-loss probabilities, state occupancies, expected work and response measures. Where depletion is almost sure, solve the transient linear system for expected first-loss time; compare residuals and a survival-sum check.

Use an independently written event sampler to check selected finite-horizon results. Check stochastic rows, ranges, policy nonanticipation, separate gate controls, the closed-core claims and the no-experience-feedback equality. Do not round small positive probabilities away before support analysis. A numerical experiment under stipulated mechanisms is internal validation, not external validation.

Sensitivity comparisons vary context hazard, failure-induced attrition and appointment bias without re-tuning the model to obtain a desired sign. They are structural checks within this finite model, not independent domains. Report adverse or null outcomes.

## Completion criteria

This study is complete when the equations and event order determine one reproducible kernel, conditional propositions have checked proofs, independent numerical verification passes, and failed claims and remaining premises are recorded. It contributes to a general research programme without declaring that programme complete. External validation requires independently measured mechanisms and prospective or held-out predictions in real systems; finite data alone cannot establish that a rare failure transition has exactly zero probability.
