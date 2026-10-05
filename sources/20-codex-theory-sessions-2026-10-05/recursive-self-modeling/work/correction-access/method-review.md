# Independent method review: correction access

5 October 2026. Design recommendations prepared before development or evaluation of this continuation. This file distinguishes proposed design choices from later observed results. It does not modify the earlier frozen experiment.

## Adopted protocol review, before development results

The coordinating researcher subsequently supplied `protocol.json`. The adopted protocol is coherent and has no blocking design issue. It uses development seeds 20000–20199, evaluation seeds 30000–31999, test seeds 40000 onward, eight factorial worlds plus a descriptive no-bias world, and hidden uniformly sampled integer change times 8–47. The scalar audit update is shared and fixed; only innovation and hybrid thresholds are selected on development. Primary inference concerns six gate-minus-confidence contrasts: three alternatives, each averaged within seed over the four change worlds or the four constant worlds. Estimate uncertainty across the 2000 seed averages, not 8000 world trajectories.

Protected periodic times are 0,10,20,35,45,55. Hybrid protects 0,25,55 and permits at most three other purchases, so its reserve cannot be consumed early. Innovation is evaluated before the current reference update and records the maximum score between opportunities; clearing at each opportunity is explicitly declared. The residual standardization is a heuristic, not an exact conditional innovation test. The no-change alarm count is correctly described without assuming each alarm is a false statistical discovery.

One deliberate revision from the initial recommendation below is that computation has no price in this continuation. The primary score is control plus sensing loss only. Monitoring workload is counted separately. Therefore interpret results as gate performance under free computation, not total resource efficiency or empirical cognitive efficiency, and do not directly compare its loss scale with the earlier compute-priced study without adjustment.

Policies assume g=0 while challenge worlds contain constant hidden forcing ±.15; scalar correction also assumes reference offset d=0 while challenge worlds contain ±.25. This is explicit model misspecification. The stochastic factorial has supplied priors and does not itself instantiate every world in the unrestricted shift-symmetry class. For the correction h, distinguish relative calibration target b−d from absolute sensor bias b. A three-state anchor estimator is a descriptive benchmark, because it changes inference as well as access.

The six primary tests describe a supplied equal-weight mixture of four factorial settings in each change group. Every world-specific result should still be shown, so an average gain cannot conceal harm under forcing or a biased reference. The adopted practical margin .02 and Bonferroni family of six are declared before evaluation. Secondary recovery/delay/coverage remain descriptive. These adopted choices supersede conflicting conditional suggestions below.

## Question and intervention

The preceding experiment identified a specific failure: an audit could assess a calibration discrepancy only after a variance gate allowed access to calibration. This continuation should test whether another route to buying evidence helps under randomized change times, without simultaneously changing the underlying estimator and attributing everything to access.

Hold fixed the correction estimator, its update rule, control gain, observation opportunities, cost accounting, and simulator dynamics across the main confidence, innovation, periodic, and hybrid policies. Vary only the acquisition decision and the state required to implement it. A different estimator may be a separately named benchmark but should not enter the primary claim as if it isolated acquisition. The retained bias estimate itself remains a kind of model of the observation process; policy names do not establish representational depth.

Suggested primary estimand: the within-world paired mean full-horizon total-loss difference for each alternative access policy minus confidence access. Use identical exogenous draws and true-change timing within seed. Full-horizon loss includes pre-change operation, false triggers, observation cost, computation overhead, and post-change control. Do not replace it with recovery speed after seeing outcomes. The estimand is a policy effect inside the specified simulator, not the benefit of an additional semantic meta-level.

## Fresh samples and freezing

Previously used ranges include development 0–99, evaluation 1000–1999, and tests 7000–7010. One suitable new allocation is development 20000–20199, evaluation 30000–31999, and tests starting at 40000, but any recorded disjoint allocation is acceptable. Pre-generate every possible sensor/process draw and a hidden change time for each seed before running policies. Do not consume reference noise only on purchases. Save exact seed ranges, simulation and policy parameters, candidate grids, development scores, selection rules, price weights, practical margin, and code hashes before evaluation.

Randomize the hidden change time uniformly over a declared interior range that includes all offsets modulo the five-step opportunity spacing. The exact range is a research choice. It should leave adequate pre-change calibration and post-change follow-up, and should not be chosen from evaluation performance. Generate a latent time even in no-change controls to support a comparable descriptive observation window. Do not pass true change time or true forcing/reference bias to the policy. The gate may know the fixed horizon and its own prespecified schedule.

Tune each alternative globally on the same development objective and equally weighted worlds, rather than selecting a favorable threshold per evaluation world. If the estimator has parameters, fix or tune them globally before the acquisition-policy comparison. A separate exploration of estimator-policy co-design changes the estimand and should be labeled separately.

## Worlds and anchors

Use separate factors for sensor change versus no change, constant forcing zero versus an unknown nonzero forcing, and clean versus biased reference. A full factorial is interpretable if computationally affordable; otherwise name each chosen contrast and its confounding factors. At minimum retain a clean no-change control, a clean sensor-change world, a forcing-misspecification world, a biased-reference world, and a joint challenge. Keep initial sensor-bias distributions comparable in change and no-change worlds. If initial bias can be zero, report the actual nonzero-change subset for detection/recovery metrics rather than treating a sign reversal of zero as an event.

Unknown forcing can mean that its realized value is hidden but its family is correctly modeled, or that the estimator wrongly fixes it at zero. These are different tests. Likewise distinguish an unknown reference bias from incorrectly assumed perfect reference calibration. A four-variable unanchored state/bias/reference/forcing model has the previously derived shift symmetry, but a supplied initial-state prior or known population distributions can still be statistical anchors. Do not describe failure of a misspecified filter as a proof of absolute non-identifiability for the actual sampled model.

An ordinary innovation can reveal mismatch without identifying which assumption failed. In particular, a change or error in physical forcing can create an innovation even when the ordinary sensor's bias is unchanged. Acquiring the reference can then be useful, useless, or harmful depending on its credibility. A successful gate is not a causal diagnosis of the origin of error.

## Acquisition policies and fairness

1. **Confidence gate:** retain the prior modeled-variance gate as a frozen comparator, including its cost assumptions and limitations. It does not by itself establish a globally rational value of information.
2. **Ordinary innovation gate:** compute a prediction residual before conditioning on current ordinary observation. Evaluate at every declared monitoring time, and charge that overhead. When opportunities occur only every five steps, latch a threshold crossing until the next opportunity or a declared expiration/reset; otherwise a step-32 discrepancy may vanish before inspection at step 35. State whether the latch resets on a successful purchase, on any eligible attempt, or only on an explicit rule.
3. **Protected periodic checks:** guarantee a declared schedule within the common acquisition cap. Its protected checks must not be consumed by earlier optional access. Schedule timing should not use the realized change time. Specify whether initial calibration is a protected purchase shared by all policies.
4. **Hybrid:** combine a fixed protected reserve with innovation-triggered optional acquisitions. Deduct protected future purchases before allowing discretionary ones, so it really preserves the guarantee. Report reserved, discretionary, attempted, successful, and denied counts separately. If the chosen hybrid is simply a union that can exhaust its cap early, call it a union gate rather than claiming guaranteed checks.

The cap is a sensing cap unless computation has its own enforced cap. Charge monitor and budget checks even when no purchase occurs. A common cap does not establish equal actual expenditure. Do not force a frugal policy to waste remaining allowance; show expenditure alongside loss. A cheap periodic method and a more expensive monitor should retain their actual execution counts under the disclosed abstract price model.

For a scalar correction implementation using previous ordinary y and bias estimate h, a possible ordinary residual is

`r_t = y_t - a*y_(t-1) - u_(t-1) - (1-a)*h_(t-1)`.

Under the extended dynamics its exact decomposition is

`r_t = g + b_t - a*b_(t-1) - (1-a)*h_(t-1) + w_(t-1) + eps_t - a*eps_(t-1)`.

This explains why an abrupt bias switch may trigger it and why unknown forcing can also do so. Its nominal standardization is generally approximate: h is itself estimated from past observations and residuals are serially correlated. A joint filter may instead expose its conventional pre-update innovation. Do not label a residual normalized by an approximate variance as a calibrated z-test without checking the conditional assumptions.

## Outcomes and inference

Keep the prior declared loss form unless there is a documented reason to change it: sum of next-state squared error and .05 action effort, plus .02 per acquired reference and .0001 per disclosed weighted work block. Report these components separately. Include state-estimate error, action-conditioned forecast error, Brier score, interval coverage and width, normalized forecast error, maximum excursion, acquisition counts/timing, and operation counts. Supplied prices are research preferences, not psychological measurements.

Report delay to the first acquired reference after a true switch and confirmed recovery delay as secondary outcomes. Right-censor episodes with no post-change reference or no confirmed recovery; state the horizon-dependent cap and non-event fraction separately. Acquisition delay and detection delay differ if the gate does not diagnose or record a change. Recovery under a biased reference can remain misleading as evidence of knowledge; the hidden physical state is available here only to the scorer.

Report no-change alarm/purchase cost without calling every no-change acquisition pointless: initial calibration or reducing uncertainty about constant bias can still help. If using a false-alarm rate, define its ground-truth target and timing convention beforehand. An innovation caused by a real forcing error is not a false alarm for generic model mismatch, although it may be a false sensor-change diagnosis. Disaggregate triggered, protected, and initial purchases.

For inference use a complete seed trajectory as the independent unit. Retain its paired observations across policies and worlds. For K prespecified primary contrasts, use two-sided normal or t intervals with per-interval coverage 1-.05/K for Bonferroni family coverage of at least .95, subject to the approximation. Alternatively give explicitly descriptive 95% intervals without family-wide claims. State whether the family covers three alternatives across every world or a smaller focused subset. The practical margin must be frozen, with a favorable difference required to clear its bound. Secondary endpoints and post-observation subgroup analyses remain exploratory.

If stratifying by switch-time offsets or late versus early changes, fix bins in advance or label them exploratory; never select the strongest bin as the overall result. Equal-weight averages across chosen worlds answer an explicitly supplied mixture objective. Show world-specific effects so an average benefit cannot hide failure under an inaccurate reference or physical model. Monte Carlo uncertainty covers this data-generating procedure, not uncertainty that it describes cognition.

## Primary-source context already verified

- [Friedland 1969](https://researchwith.njit.edu/en/publications/treatment-of-bias-in-recursive-filtering/) provides established precedent for state and constant-bias estimation under linear assumptions. This review previously inspected the author-institution abstract, not the full article. It does not validate the new thresholds or unknown-forcing assumptions.
- [Hay et al. 2012](https://people.eecs.berkeley.edu/~russell/papers/uai12-meta.pdf) formulates metalevel computation choices and demonstrates limitations of myopic evaluation. Its results do not prove the acquisition gates optimal.
- [Tzoumas et al. 2020](https://arxiv.org/pdf/1802.08376) evaluates sensing through control objectives with fixed sensor-set selection and declared costs. Its guarantees do not transfer automatically to online, observation-triggered purchases, clipped actions, or misspecified models.
- [Gneiting and Raftery 2007](https://sites.stat.washington.edu/people/raftery/Research/PDF/Gneiting2007jasa.pdf) supports proper forecast scoring and separating calibration from sharpness. Brier differences across intervention policies also reflect their induced event distributions; interval coverage and state error remain useful complementary diagnostics.
- [Banerjee and Veeravalli 2012](https://vvv.ece.illinois.edu/papers/journal/bane-veer-sqa-2012.pdf), checked during the later audit, studies quickest detection with a geometric change-time prior, known pre/post-change observation laws, and observation control. Equation 2.3 updates the change posterior to `p+(1-p)rho` even without a new sample. The paper also gives cases where a simple two-threshold policy is not exactly optimal. Its asymptotic results do not transfer to our uniform timing, control objective, or misspecified physical/reference model. It supports treating absence of sampling separately from absence of possible change.

No new empirical consciousness claim or universally optimal reflection policy follows from this design. Its useful possible result is narrower: whether a specific affordable route to fresh evidence improves judgment/control when the current model can otherwise suppress that evidence.

## Later audit status

New simulator code and raw evaluation results were not yet present when this design review was written. After the freeze and evaluation, independently inspect update chronology, forbidden access, cap reservations, operation charges, raw paired contrasts, forecast calibration, acquisition timing, and chosen-world limits. Preserve any discovered defects or unfulfilled hypotheses without rewriting the frozen protocol to match results.

## Final report review

Reviewed `report.md` against the frozen protocol, independently audited raw results, and post-evaluation diagnostics. No numerical or inferential defect found in the six primary contrasts, adjusted uncertainty, mixture-level estimands, world-specific tables, miss percentages and censoring, or diagnostic change-probability crossovers. The three-state estimator is appropriately described as a different inference mechanism under a false forcing assumption, with the coordinate explanation separated from an exact finite-filter convergence claim. Source limitations are correctly preserved.

Two wording corrections were recommended to the coordinating researcher before packaging:

- Replace “improve average loss after changes” with “improve average full-horizon loss in episodes containing a change,” because the primary endpoint includes pre-change behavior.
- Describe the unpurchased-reference API check as a selective noninterference test on reserved seed40000 for all five policies, alongside the code/dataflow review and independent scalar replay. The test alone does not prove a universal noninterference theorem.

Image-path and final reproduction-artifact fixes were already being handled by the coordinating researcher. No additional simulation or policy change was needed.

## Independent numerical audit after evaluation

5355 assertions passed. Read raw episode arrays and recomputed all summary intervals. Independently regenerated all random tapes and replayed every scalar episode from a separately written vectorized implementation, deriving the innovation by cancellation of physical state. Scalar results and all acquisition/alarm/fast-update arrays match. A separate selective API test changes only unacquired reference values and verifies identical behavior for all five policies on test seed40000; this test imports the runner, unlike the independent replay.

The data contain 90,000 episodes (nine worlds × five policies × 2,000 seeds). Primary uncertainty uses 2,000 paired seed averages across four worlds, not 8,000 independent world episodes. All six primary intervals, every summary mean/interval, sensing caps, protected checks, purchase delays, scalar recovery, and frozen source hashes were verified. The anchor benchmark is independently checked through aggregate consistency and its saved example forecast math; this audit does not independently replay every anchor episode.

### Six primary comparisons

| Stratum | Alternative minus confidence | Mean | Adjusted lower | Adjusted upper | Decision at .02 margin |
|---|---|---:|---:|---:|---|
| constant | innovation minus confidence | +2.718009 | +2.505006 | +2.931012 | harm |
| constant | periodic minus confidence | +3.044418 | +2.902139 | +3.186696 | harm |
| constant | hybrid minus confidence | +2.284758 | +2.100403 | +2.469114 | harm |
| change | innovation minus confidence | -3.209291 | -4.112976 | -2.305605 | benefit |
| change | periodic minus confidence | -2.570684 | -3.532591 | -1.608776 | benefit |
| change | hybrid minus confidence | -0.838130 | -1.801584 | +0.125324 | unresolved |

Critical normal value: 2.638257273477; 99.1667% individual two-sided intervals, Bonferroni family of six.

### World-specific effects and access

| World | Policy | Total loss | Control loss | Purchases | Alarms | Coverage90 | Width90 | NPE | Access delay | Post-change sample fraction | Recovery fraction |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| constant_g0_d0 | confidence | 7.206467 | 7.086857 | 5.980500 | 0.000000 | 0.953183 | 1.378495 | 0.858234 | — | — | — |
| constant_g0_d0 | innovation | 9.473977 | 9.363107 | 5.543500 | 7.813500 | 0.966692 | 1.577157 | 0.848114 | — | — | — |
| constant_g0_d0 | periodic | 10.508832 | 10.388832 | 6.000000 | 0.000000 | 0.968292 | 1.626420 | 0.882182 | — | — | — |
| constant_g0_d0 | hybrid | 9.279535 | 9.161985 | 5.877500 | 7.791500 | 0.967183 | 1.562530 | 0.842840 | — | — | — |
| constant_g0_d0 | anchor_filter | 0.656956 | 0.536956 | 6.000000 | 0.000000 | 0.911033 | 0.286219 | 0.929908 | — | — | — |
| constant_g0_d1 | confidence | 8.291607 | 8.172417 | 5.959500 | 0.000000 | 0.916925 | 1.376911 | 1.041148 | — | — | — |
| constant_g0_d1 | innovation | 10.205066 | 10.094146 | 5.546000 | 7.938500 | 0.939800 | 1.572126 | 0.990221 | — | — | — |
| constant_g0_d1 | periodic | 11.134108 | 11.014108 | 6.000000 | 0.000000 | 0.947467 | 1.623057 | 0.982091 | — | — | — |
| constant_g0_d1 | hybrid | 10.090009 | 9.972629 | 5.869000 | 7.927500 | 0.940333 | 1.558496 | 0.983492 | — | — | — |
| constant_g0_d1 | anchor_filter | 0.722724 | 0.602724 | 6.000000 | 0.000000 | 0.902383 | 0.286219 | 1.002635 | — | — | — |
| constant_g1_d0 | confidence | 9.744004 | 9.624394 | 5.980500 | 0.000000 | 0.919425 | 1.378495 | 0.989578 | — | — | — |
| constant_g1_d0 | innovation | 13.196270 | 13.085640 | 5.531500 | 9.713000 | 0.936375 | 1.549280 | 0.966435 | — | — | — |
| constant_g1_d0 | periodic | 12.974175 | 12.854175 | 6.000000 | 0.000000 | 0.937933 | 1.626420 | 0.975534 | — | — | — |
| constant_g1_d0 | hybrid | 12.514315 | 12.397455 | 5.843000 | 9.860000 | 0.935617 | 1.547140 | 0.956139 | — | — | — |
| constant_g1_d0 | anchor_filter | 30.215730 | 30.095730 | 6.000000 | 0.000000 | 0.025658 | 0.286219 | 75.527858 | — | — | — |
| constant_g1_d1 | confidence | 10.725364 | 10.606174 | 5.959500 | 0.000000 | 0.887075 | 1.376911 | 1.160866 | — | — | — |
| constant_g1_d1 | innovation | 13.964164 | 13.853594 | 5.528500 | 9.832500 | 0.914358 | 1.546675 | 1.108569 | — | — | — |
| constant_g1_d1 | periodic | 13.527997 | 13.407997 | 6.000000 | 0.000000 | 0.917950 | 1.623057 | 1.071416 | — | — | — |
| constant_g1_d1 | hybrid | 13.222616 | 13.105866 | 5.837500 | 9.964000 | 0.914525 | 1.543707 | 1.076542 | — | — | — |
| constant_g1_d1 | anchor_filter | 30.270766 | 30.150766 | 6.000000 | 0.000000 | 0.024733 | 0.286219 | 75.580129 | — | — | — |
| change_g0_d0 | confidence | 19.248018 | 19.135248 | 5.638500 | 0.000000 | 0.803658 | 1.325719 | 2.863651 | 8.737000 | 0.710500 | 0.514000 |
| change_g0_d0 | innovation | 14.360441 | 14.244141 | 5.815000 | 9.677000 | 0.863433 | 1.431044 | 1.782274 | 3.899500 | 0.885000 | 0.581500 |
| change_g0_d0 | periodic | 17.287675 | 17.167675 | 6.000000 | 0.000000 | 0.814608 | 1.519652 | 1.706151 | 5.464500 | 1.000000 | 0.554000 |
| change_g0_d0 | hybrid | 17.662262 | 17.542962 | 5.965000 | 10.137500 | 0.820750 | 1.442120 | 2.130490 | 6.482000 | 1.000000 | 0.440500 |
| change_g0_d0 | anchor_filter | 0.659465 | 0.539465 | 6.000000 | 0.000000 | 0.909400 | 0.286219 | 0.938928 | 5.464500 | 1.000000 | 1.000000 |
| change_g0_d1 | confidence | 21.629657 | 21.517237 | 5.621000 | 0.000000 | 0.754975 | 1.325042 | 3.394559 | 8.912000 | 0.710000 | 0.390000 |
| change_g0_d1 | innovation | 15.685640 | 15.569300 | 5.817000 | 9.850500 | 0.806717 | 1.428304 | 2.175042 | 4.014500 | 0.878500 | 0.432000 |
| change_g0_d1 | periodic | 18.471701 | 18.351701 | 6.000000 | 0.000000 | 0.769800 | 1.513922 | 2.075621 | 5.464500 | 1.000000 | 0.426000 |
| change_g0_d1 | hybrid | 18.941130 | 18.821800 | 5.966500 | 10.281500 | 0.770067 | 1.437755 | 2.541396 | 6.462000 | 1.000000 | 0.357500 |
| change_g0_d1 | anchor_filter | 0.725208 | 0.605208 | 6.000000 | 0.000000 | 0.900675 | 0.286219 | 1.011587 | 5.464500 | 1.000000 | 1.000000 |
| change_g1_d0 | confidence | 22.061161 | 21.948391 | 5.638500 | 0.000000 | 0.768333 | 1.325719 | 3.095569 | 8.737000 | 0.710500 | 0.344500 |
| change_g1_d0 | innovation | 21.523831 | 21.406311 | 5.876000 | 11.631500 | 0.803483 | 1.417132 | 2.613106 | 5.849500 | 0.790000 | 0.347500 |
| change_g1_d0 | periodic | 20.041875 | 19.921875 | 6.000000 | 0.000000 | 0.781425 | 1.519652 | 1.924101 | 5.464500 | 1.000000 | 0.366500 |
| change_g1_d0 | hybrid | 22.930353 | 22.810953 | 5.970000 | 11.895000 | 0.778258 | 1.429370 | 2.620828 | 7.439500 | 1.000000 | 0.295500 |
| change_g1_d0 | anchor_filter | 30.226894 | 30.106894 | 6.000000 | 0.000000 | 0.025658 | 0.286219 | 75.560870 | 5.464500 | 1.000000 | 0.000000 |
| change_g1_d1 | confidence | 24.257207 | 24.144787 | 5.621000 | 0.000000 | 0.734600 | 1.325042 | 3.597167 | 8.912000 | 0.710000 | 0.316500 |
| change_g1_d1 | innovation | 22.788967 | 22.671497 | 5.873500 | 11.793500 | 0.769308 | 1.413943 | 3.006277 | 5.839500 | 0.791000 | 0.317500 |
| change_g1_d1 | periodic | 21.112057 | 20.992057 | 6.000000 | 0.000000 | 0.752933 | 1.513922 | 2.281667 | 5.464500 | 1.000000 | 0.332000 |
| change_g1_d1 | hybrid | 24.309778 | 24.190408 | 5.968500 | 12.093000 | 0.748208 | 1.426409 | 3.053963 | 7.547000 | 1.000000 | 0.260000 |
| change_g1_d1 | anchor_filter | 30.281906 | 30.161906 | 6.000000 | 0.000000 | 0.024733 | 0.286219 | 75.613075 | 5.464500 | 1.000000 | 0.000000 |
| no_bias | confidence | 1.628529 | 1.508529 | 6.000000 | 0.000000 | 0.996058 | 1.380572 | 0.288956 | — | — | — |
| no_bias | innovation | 1.587320 | 1.487850 | 4.973500 | 6.592500 | 0.998450 | 1.701506 | 0.200800 | — | — | — |
| no_bias | periodic | 1.592252 | 1.472252 | 6.000000 | 0.000000 | 0.998833 | 1.627644 | 0.206291 | — | — | — |
| no_bias | hybrid | 1.596424 | 1.483224 | 5.660000 | 6.683000 | 0.998575 | 1.641094 | 0.210522 | — | — | — |
| no_bias | anchor_filter | 0.652760 | 0.532760 | 6.000000 | 0.000000 | 0.911117 | 0.286219 | 0.926784 | — | — | — |

All primary results describe the frozen equal-weight mixture and free-computation assumptions. Individual cells are descriptive, not additional multiplicity-controlled discoveries. Access delay measures arrival of a purchased sample, not successful diagnosis or trustworthy correction. Forecast interval coverage is an empirical check of model assumptions; low control loss does not establish calibrated uncertainty. No-change alarms are not automatically false discoveries.

### Mechanism checks and interpretation

The constant-bias control is not initially calibrated: h starts at zero while b is ±1. With noiseless clean calibration and no fast update, the residual bias after n slow updates is .8^n times its initial error. Postponing early observations can therefore prolong initial error even without a later change. This is a mechanism explanation under the shared rule, not a randomized mediation estimate.

| Policy in constant_g0_d0 | Mean purchases through15 | Through25 | Through55 |
|---|---:|---:|---:|
| confidence | 3.998000 | 4.991000 | 5.980500 |
| innovation | 2.538000 | 3.536500 | 5.543500 |
| periodic | 2.000000 | 3.000000 | 6.000000 |
| hybrid | 2.538000 | 3.963000 | 5.877500 |

Periodic and hybrid have a guaranteed post-change purchase because both protect step55 and all changes occur by47. Their 100% sample-arrival fraction is therefore a design guarantee, not successful learned diagnosis. The six-purchase cap trades earlier calibration against later access; hybrid reserves fewer closely spaced checks than periodic and can still leave long delays.

The anchor estimator uses the same periodic six measurements but can fail badly when its known-zero-forcing assumption is false. The previously derived shift explains a candidate mechanism: true g=.15 can be represented in a nominal g=0 model by shifting x by−.75 and both biases by+.75. The prespecified seed30000 constant_g1_d0 example ends with true x=.6834, estimated x=.01247, b=1 versus estimated1.7954, and d=0 versus estimated.7458. These finite-run values illustrate, rather than prove exact convergence to, that explanation. Across forcing worlds its very low interval coverage and high normalized error contradict calibrated uncertainty. More reliable access cannot alone correct a false physical anchor.
