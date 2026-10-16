# Second V6.2 review: checks and transition audit

Reviewed the frozen V6.2 snapshot. No manuscript or pre-existing script was edited. This report covers checks_v62.py, S14–S15, Proposition 11.1/S11, and dwell. Locations below are assembled snapshot line numbers.

## Assessment

The default suite completed in 290 seconds: **188 passed, 0 failed**, all 40 blocks ran, and all ten outside-review entries reported holds (eight required by the final index, two extra). Log: `checks-output.txt`. Passing these regressions does not remove the missing premises below. The repaired mixed equilibrium and the substantive monotonicity/unbounded-depth result are mathematically sound once their stated domains and boundary rules are corrected.

## Confirmed corrections

### 1. The core receiver rule excludes the mixed equilibrium it claims

**THEORY.md:1073–1075; SUPPLEMENT.md:1009,1013.** The core says the receiver restrains iff the posterior is *at least* the threshold. The proof instead permits mixing at equality. That difference is essential: the bounding equilibrium has posterior exactly the threshold and restraint probability strictly between zero and one.

Independent calculation at the paper's example: prior S=.5, threshold=.6, costs cS=-.05,cR=.05, restraint values PiS=.4,PiR=.2. Then sigmaR=2/3, rhoE=1/4, posteriorE=.6. R's E and N payoffs are both zero and S's E payoff is .15. Under the core's deterministic tie rule rhoE must equal 1, making R's E payoff .15>0, so the claimed mixed strategy is not a best response. **Repair:** state restraint with certainty above the threshold, no restraint below it, any probability at equality. With this repair, the bound and hybrid proof close the V6.1 mistake.

### 2. Independence of readings is insufficient for the SPRT termination theorem

**SUPPLEMENT.md:1051–1053.** The statement assumes independent readings and a correctly computed likelihood ratio, then asserts almost-sure termination at every noise level. It omits the information/identical-distribution hypotheses needed for that conclusion.

Exact counterexample: under H0 let X_t~Bernoulli(1/2); under H1 let X_t~Bernoulli(1/2+2^(-t-4)), independently for t>=1. Every reading is informative, and the correct likelihood increment is log(1+2^(-t-3)) when X_t=1 and log(1-2^(-t-3)) otherwise. Every partial log-likelihood sum is between -0.127702 and +0.122485. The paper's alpha=.01,beta=.05/7 boundaries are -4.931592 and +4.598002. Neither can ever be reached: termination probability is zero.

**Repair:** use iid informative observations under the registered hypotheses with the usual Wald conditions, or explicitly require enough accumulated information for boundary exit. Keep calibration at the specified hypotheses; do not silently apply endpoint error guarantees throughout an unmodeled indifference band. The numerical Gaussian iid checks remain sound. The [thm] tag is justified only after the premise is restored.

### 3. Dwell is an infimum, not an attained minimum

**SUPPLEMENT.md:1061,1064,1069,1081.** The basin of absence is open. The first intersection of the continuous insulated path with its boundary lies on the saddle's stable manifold and converges to the saddle after release, not absence. Therefore there is no least successful duration at a positive crossing threshold. There is an infimum T*, with successful release for T>T*. The text calls it the least T and later says it is the minimum capture time/iff held for T_min.

Independent RK4 from x0=.99,ztilde0=G=2, equal speeds gives T*=5.8589560559. Releasing at T*-.001 converges to capture; at T*+.001 to absence. Exactly at the separatrix the defining theorem itself gives saddle convergence. **Repair:** define critical dwell as infimum, require strict release beyond it, and describe reported decimals as numerical thresholds. This does not change the printed rounded values or the depth result.

### 4. Summability alone does not ensure positive survival

**SUPPLEMENT.md:1027,1029.** S11.2(2) states that a summable post-pause hazard sequence keeps survival bounded away from zero; its proof adds a summable bound strictly below one in every round. A sequence h1=1, ht=0 thereafter is summable and gives survival zero. **Repair:** carry 0<=ht<1 (or the displayed strict upper bound) and positive survival before the pause into the statement. If hazards are history-dependent, carry the history-uniform bound used in the proof as well.

## Dwell conclusions that are sound

For 0<x0<1, G>1, fixed positive rates, initial ztilde=G, the comparison proof works. Under insulation u(T)=u0+a[G(1-exp(-bT))/b-T], with a=zeta*c,b=epsilon*d. It preserves order in u0, while the absence basin is a down-set. Hence the critical dwell is nondecreasing in u0 and exceeds (u0-logit(x_sigma))/a when positive. It grows without bound as u0 grows. Along an actual captured trajectory ztilde->G and u(t)/t->a(G-1), so age gives asymptotically linear growth in depth. Say asymptotically; the literal boundary equilibrium x=1 has no finite logit and never escapes in the unseeded replicator equation.

Independent values at G=2,equal speeds: x0=.9,.99,.999 yield critical dwell 3.4459303,5.8589561,8.1719294, reproducing the printed 3.45,5.86,8.17. The recruitable-floor comparison is sound under the specified hard cap on share and continued recruitment. The suite reproduces all printed floor values, including 10.45 to 3.81; this is not an effect of merely sequestering a non-recruiting alternative.

### Ratchet qualification (interpretation issue, not an additional definitive finding)

**SUPPLEMENT.md:1077; THEORY.md:1120.** Reversible subcritical pulses can leave residual progress rather than fully resetting. Independent example: G=2,equal speeds,x0=.99,z0=2; alternate insulation .2 and full conversion .05. After 20 cycles release still captures; after 40 cycles state x=.462748,z=.266560 releases to absence. Each insulating pulse is much shorter than the original dwell 5.858956. Thus "a sequence of re-absorptions" needs either complete recovery between pulses or a definition of each step's dwell from its actual current state. If the claim only means the final pulse must cross the basin boundary, it is true but does not prove permanent control-ratcheting necessary. The source's single sustained-control theorem is not a theorem about arbitrary switching schedules.

## The 188 assertions: method map and limitations

`assertion-audit.tsv` assigns a category and source line to all 188 executed expect assertions. There are 186 static call sites in functions, NB's call at 1314 executes twice, and the final index adds one. `assertions-static.tsv` also preserves each condition and label. Categories are deliberately about computational method, not 188 independent proofs:

| Category | Count | Interpretation |
|---|---:|---|
| I | 150 |Model outcome/trajectory/numerical optimization regression, sometimes conditional on lower-level closed forms; independent of the high-level inequality being tested, not necessarily an independent test of the whole cited proposition|
| P | 30 |Algebraic identity, substitution into a derived formula, or parts S15 itself labels identity|
| V | 6 |Evaluation/simulation of a stipulated play path; validates value arithmetic, not credibility or all deviation plans|
| D | 1 |ML's derived toy|
| X | 1 |Final bookkeeping index|

The P entries by checks_v62.py line are: 1314(twice),1441,1442,1574,1575,1576,1665,1678,1716,1911,2372,2401,2663,2758,3425,3748,3760,3780,3788,3939,4221,4284,4343,4349,4355,4479,4493,4503,4534. V: 418,3667,3867,3878,3891,3921. D: 4560. X: 5634. The remaining entries are I in the stated limited sense. Some I assertions combine an independent outcome with formula arithmetic; the manifest is a coarse classification of entire assertions, not every conjunct.

The S15 classification is therefore directionally candid but incomplete at subpart level. Examples needing relabeling or qualification:

- SP(H), line 1665, simply evaluates theta_effective(gains(...)) before and after provision; S15 calls H independent.
- CH lines2372,2401,2663 evaluate the gain formula; they are not independent numerical Jacobian checks (other CH parts do provide those).
- ES(e),(g),(h), lines3748,3780,3788, use cond/pbar/the displayed inequality. ES(d),3740, is the genuine maximization over deviation plans and is the important incentive check.
- AL(BT),AL(bounded),AL(contest), lines4284,4349,4355, directly evaluate their stated formulas. AL(6.1),4221, and AL(6.11),4343, also evaluate derived expressions. S15 only explicitly marks AL topology derived.
- TR(d),4479, inserts zeros in the same product; TR(f),4493, evaluates .95^7;4503 evaluates a normal-CDF formula. These are arithmetic/model-probability regressions, not independent validation of readiness governance. TR's iid Gaussian simulations do not cover the SPRT generality claimed at 1051.
- MP(a),1911, obtains equilibrium effort from its closed form and finite-differences it, rather than independently finding that equilibrium.

Thirteen blocks contribute zero counted expect assertions: FB,LG,TC,TH,CB,FA,AC,RH,FS,BI,WG,PE,FD. They run and print numerical diagnostics; the 188 count must not be read as comprehensive automated pass/fail coverage of every printed comparison. There are also internal Python argument assertions not included in 188.

## Text-number routing and S14(O)

All newly restated §11 numbers were routed and reproduced: TR's 300/200/135 signal cases; .667/.25 example; survival .7969 to 10,000 and .7968 limit approximation against 2.25e-44; fixed-test and sequential-test probabilities/durations; DW's six main dwells and floor/depth variants. There is no missing numerical block for these results. THEORY/SUPPLEMENT num/identity tag inventory finds only current block codes, explicitly labeled legacy references, and S15's declared placeholders/arithmetic exceptions. I did not independently compare every numerical token in all three prose documents to output or rerun legacy/full grids; absence of unmapped tags is not an exhaustive number audit. S15:1282 also says a default run writes checks_v62.log, whereas the script writes stdout and needs the redirection shown in its own docstring; minor documentation correction.

S14(O) statuses (all passed and consistent with the corrected claims):

| S14 line | Case | Block | Status |
|---:|---|---|---|
|1158|Price outside convergence|PD|Reproduced; does not certify a finite derivative outside domain|
|1160|Decay in a ratio channel|CH|Reproduced; formula substitution backed elsewhere by nonlinear/Jacobian comparisons|
|1169|Cap at equality|CE|Reproduced|
|1170|Diffusion restores without provision|CE|Reproduced|
|1182|Provision increases 1+theta|SP|Reproduced by formula; observable itself independently optimized in SP(G)|
|1183|Unequal compliance incidence|CI|Reproduced|
|1189|Nonlinear-fitness Price between term|PR|Reproduced|
|1197|Falling positive cost floor|FF|Reproduced|
|1222|Label-dependent punishment|ES|Reproduced under explicitly exogenous labeled continuation; does not contradict exchangeable-continuation theorem|
|1241|Delegation p<1|DL|Reproduced|

## Reusable files

- `independent_transition.py`: standard-library derivations/calculations for receiver equality, dwell thresholds, pulsed insulation, and exact SPRT counterexample.
- `independent-transition-output.txt`: results.
- `checks-output.txt`: untouched-suite full default stdout/stderr.
- `assertion-audit.tsv`: all 188 counted assertions, lines and categories.
- `assertions-static.tsv`: static call-site condition/label manifest.

No --full grids, legacy suites, bibliography, real-world evidence, or continuous-state Markov-equilibrium validation was performed by this subreview.
