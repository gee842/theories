# Frozen software-target transfer protocol

This is a prospective local protocol, not an external preregistration. It will be hashed with all executable source before calibration; calibrated predictions will then be hashed before the 1,024 held-out target seeds are run. No target integrated recovery outcomes were examined while choosing these regimes. The investigator knows the constructed service laws. This is synthetic software evidence, with no people, institutions, physical systems, or observed production service.

## Claim and boundary

The transported equations are exactly R[f,a] = p[f] q[a] and Delta = (p[1]-p[0])(q[1]-q[0]). Source: next-test.md, quantitative subclaim and stage two; fundamental-theory-audit.md, task-service proposal. No mechanisms will be added to these predictions after target evaluation. Calibration is local to the new implementation and never measures its joint recovery rate. This does NOT refit a source stock model or establish a universal law. It tests one fixed two-gate candidate against an independently implemented queue model.

The source identity requires no alternative recovery, no finance-dependent conditional enactment success or relevant recommendation distribution, no enactment effect on diagnostic production, and matched timing/protected functions. Our reserved/batched control meets those requirements by construction. The two shared-worker regimes deliberately challenge their applicability. A failure there refutes the registered transport application, not the probability identity under its assumptions. Local recommendation standardization preserves a pooled timing marginal; it does not assert that a marginal can preserve its correlation with backlog. This omission is locked now rather than repaired later.

## Runnable target

The target is an integer-clock, discrete-event software service, not the earlier stock-and-cash recurrence. A FIFO executes application, diagnostic and deployment job objects. The service begins faulted; applications consume work but yield bad responses until a successful deployment. Every application has an arrival+3 deadline. Expired applications still occupy the FIFO; there is no deadline-aware dropping. The primary protected function is restored service by the regime's recovery deadline. Application deadline misses and good responses are separate secondary outcomes, not silently folded into recovery.

Each seed supplies initial application backlog B in {0,1,3} with probabilities (.25,.50,.25), Bernoulli arrivals of batches of two unit-duration application jobs at times (0,2,4,6,8), diagnostic duration D in {1,2,4} with probabilities (.25,.50,.25), a correct-diagnosis indicator of probability .85, deployment duration L in {2,4} equiprobably, and technical deployment success of probability .95. Initial backlog jobs arrive at zero. All primitive random variables are independent before interventions. Main cells use paired shocks from each target seed.

Total endowment is six credits in all cells: three in a locked diagnostic purse and three in an accessible deployment purse. Finance f=1 unlocks diagnostic funds at t=0; f=0 at t=3. Diagnosis pays three before enqueue. Deployment pays three before enqueue, after a valid timely recommendation and authority permission. There is no borrowing, production income, direct repair, or spontaneous clearance. Finance changes only unlock time. Authority changes only the earliest allowed deployment enqueue. Actual spending may differ.

At integer t, jobs finishing at t complete first, then application arrivals enqueue, then the diagnostic submission (if due), then a permitted deployment submission, then idle workers start FIFO jobs. A valid diagnosis must complete by t=5; later or wrong diagnoses cannot create an accepted recommendation. Deployment completion at exactly the recovery deadline counts as timely. Technical failure never restores service.

Regimes, all fixed before execution:

| regime | application burst probability | worker allocation | recommendation release | authority opening a=0 / a=1 | recovery deadline |
|---|---:|---|---|---|---:|
| reserved_control | .35 | separate maintenance and application workers | all timely diagnoses released at t=5 | 7 / 0 | 9 |
| shared_fifo | .35 | one shared worker | immediately on timely completion | 7 / 0 | 9 |
| urgent_fifo | .65 | one shared worker | immediately on timely completion | 5 / 0 | 7 |

The reserved control factorization is intentionally a constructed sanity check. In shared regimes, finance can change recommendation time and conditional backlog; diagnostic work itself displaces applications. The parameter choices have not been tuned on target outcomes.

## Independent local measurements

1. Primitive component calibration: 65,536 independent draws per regime measure backlog category, arrival probability, diagnostic duration, diagnostic accuracy, deployment duration and deployment efficacy. The domain model receives these component frequencies and the declared scheduling/resource rules. It never receives p, q, joint outcomes or target shocks.
2. p calibration: 65,536 diagnosis-only trials per finance cell and regime, with no deployment. Record whether a valid recommendation is timely and the completion/release-time histogram among successes.
3. q calibration: 65,536 enactment-only trials per authority cell and regime. Inject a standardized correct recommendation into an independent workload-only service. Draw its release time by first choosing finance 0 or 1 with equal probability, then sampling that arm's successful p-trial release-time histogram. The diagnostic job is absent; backlog comes from the fresh workload. This q trial never conditions on the integrated target's recovery. Balanced proposal timing is the frozen bridge measurement; diagnosis-induced backlog and time/backlog association are discarded. If any p arm has no successes, use release time five and flag the calibration as undefined for that arm.

Every fitted scalar and supplied rule is reported. The transported recovery predictor has four calibrated scalar inputs p0,p1,q0,q1 per regime; its measurement pipeline additionally uses the proposal-time histograms. Claiming four numbers captures its whole measurement cost would be misleading. The domain predictor uses eight free primitive frequencies per regime (two backlog, one arrival, two diagnosis duration, one diagnosis accuracy, one deployment duration, one deployment efficacy), plus explicit scheduler/resource rules. No complexity penalty is selected and no advantage in compression is inferred from raw parameter counts alone.

## Locked comparisons and sample splits

All randomness uses numpy PCG64 seed sequences [namespace, regime_index, arm_index]. Namespaces: primitive calibration 11001; diagnosis calibration 22002; enactment calibration 33003; held-out integrated target 44004; uncertainty resampling 55005. Target uses exactly 1,024 independent seed clusters, pairing every primitive across all four interventions within a regime. The four binary outcomes of one seed are never counted as independent replication. Calibration has no target seeds. Domain predictions exactly enumerate the finite nontechnical primitives under fitted probabilities and multiply the separately measured diagnostic accuracy and technical efficacy.

Additional weak controls are frozen: current-output/total-resource predictor uses the same average of the four transported predictions in every cell; fixed-diagnostic-access predictor uses p0*q[a] for both finance values. These controls are not the basis of any unification claim.

## Decision rules and uncertainty

Primary practical tolerance is **0.075 absolute recovery probability** in every cell. For each model and regime, report all four residuals (observed minus frozen prediction), maximum absolute error, and mean squared error. A model is practically equivalent in a regime only if all four simultaneous residual intervals lie within [-.075,.075]; rejected if any interval is wholly outside that band; otherwise inconclusive. Also report whether a residual excludes zero, which rejects exact sampled agreement under the source rule even if smaller than .075.

Primary uncertainty uses 20,000 bootstrap replicates, with an entire four-cell seed vector as the resampling unit. The actual implementation may equivalently resample the 16 observed binary outcome patterns by a multinomial distribution, which is the same cluster bootstrap. p and q are independently resampled from their observed binomial counts; q's estimated proposal-time mixing distribution is held fixed in this conditional analysis. Accordingly this interval is conditional on the calibration bridge distribution, not an unconditional CI for a hypothetical new bridge calibration. Use the 95th percentile of the largest absolute *unstudentized centered* error across all 12 cell residuals to give simultaneous nominal 95% bands. Domain bands resample target clusters plus component calibration through a first-order delta approximation; finite differences of exact predictions determine its calibration covariance. Report that approximation. Each model's 12-cell family is separate; claims comparing multiple model families are descriptive.

For interactions, bootstrap the clustered vector contrast Y11-Y01-Y10+Y00 and the independently resampled product (p1-p0)(q1-q0); use the same unstudentized maximum over the three regimes for simultaneous nominal 95% bands. The bootstrap is a nominal sampling procedure, not an exact finite-sample coverage theorem.

After the held-out evaluation, exhaustive oracle enumeration of this finite software's primitive law is a predeclared structural check. Independently implemented engines must agree pathwise on every enumerated state/intervention/regime. Oracle p and q use the same local-calibration definitions as above, with exact distribution weights. Structural numerical tolerance is 1e-12. This checks whether a discrepancy is a feature of the specified program rather than sampling or an implementation mismatch. It does not become a new prediction, replace the frozen prediction or claim real empirical validation.

## Integrity and records

The independent queue predictor must not call the target service execution function. It computes FIFO start/finish times by event recurrence rather than mutating job/worker objects. Validate integer completion/deadline boundaries, account conservation, no finance effect on initial total, authority exclusion from the diagnosis-only gate, and exact agreement of both engines across all enumerated finite shock combinations. Preserve scripts, protocol and prediction SHA-256 manifests, unmodified calibration estimates/predictions, per-seed held-out outcomes, concise results, and audit details. Code changes after the first freeze require a dated amendment and preserved original hashes; no outcome-driven protocol edits are permitted.
