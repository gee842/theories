# Third review: Sections 2–3 and S2–S3

Reviewed 4 October 2026, after the repairs recorded in the current source changelog. No manuscript files were changed. The scope is the current source, not the earlier assembled snapshots. Findings are deliberately narrower than a rejection of the main loop-gain results.

## M3-01 — P2 — The finite-jump correction has not reached the standing-price proof

**Stable keys:** `standprice`, `eqgain`, `loopgain`.

**Current locations:** `src/supp/03_S3.md:82` (the whole first sentence and the following transfer to the strategic price); compare `src/supp/02_S2.md:48` and `src/core/20_s2.md:43–45`. Related strategic-scope wording remains at `src/core/30_s3.md:80` and S0 assumption A9, `src/supp/00_S0.md:16`.

S3 still states, without a linear-strength qualification, that with fixed opponents the exact finite-jump price equals the structural multiplier “even at the paper's jump sizes”. It then treats the strategic price elasticity as the relative return used in the objective formula. The repaired S2 explicitly distinguishes these objects and reports a nonlinear counterexample. Consequently the main restriction to the deterministic share model does not yet govern its proof and propagation.

**Reproduction.** Re-running the previous independent Bellman implementation, with `r=1.5`, structural `Gamma=.6`, decay `.2`, discount `.97`, gives finite-jump price `1.03110642` on 1,000 cells and `1.03111035` on 2,000 cells, versus multiplier `1.08178439`. The r=1 control gives `1.08178439` for both. The nonlinear discrepancy is about 4.68%, not grid error. Results are in `results.json`; `audit_math.py` imports only the prior independent review implementation, never the manuscript's numerical implementation.

**Repair.** Restrict S3's exact passive-lottery assertion to the proved linear case. Carry the deterministic-share restriction into its strategic transfer, the corresponding core scope and A9. For a lottery, use an explicitly computed continuation value with a stated mapping into the objective; do not identify its finite winner/loser value difference with the deterministic local multiplier. Keep the valid local deterministic formula and the numerical lottery magnitudes.

## M3-02 — P2 — A stationary reference alone does not justify the nonlinear infinite-horizon common price

**Stable keys:** `standprice`, with the boundary against `growprize`.

**Current locations:** `src/core/30_s3.md:72–74`; `src/supp/03_S3.md:49–57`, especially the “finite iff” valuation at line 57. The related qualification is at `src/supp/03_S3.md:78`.

The repair requiring constant linearized coefficients fixes the moving-Jacobian counterexample. It does not ensure that the infinite-horizon value in the nonlinear growing-prize model is finite or differentiable. The local multiplier is valid as the sum of linearized future-payoff derivatives. Interchanging that sum with the derivative of actual lifetime value additionally needs a tail/integrability condition.

**Exact counterexample.** Take two actors, one stock, `kappa=d=delta=1/2`, no provision, sharing or diffusion, ratio strength `r=1`, and prize `Omega(S)=S^2`. The symmetric reference `S*=1`, `X_i*=1/2` is a steady state. Its coefficients are constant. The two stated gains are

```
Gamma_delta   = (1/2)(1/2) / [1-(1/2)(1/2)] = 1/3,
Gamma_c_delta = (1/2)(1/2)(2) / [1-(1/2)(1/2)] = 2/3.
```

Both are inside the theorem's stated domain, which assigns relative price `1/2` and common price `2`.

After any positive common perturbation the symmetric total instead follows

```
S_{t+1} = (S_t+S_t^2)/2,  S_0>1.
```

It increases without bound: a finite limit above one would have to solve `S=(S+S^2)/2`, which has only roots zero and one. Once `S>=4`, `S_next>=2S`. Discounted winnings per actor, `(1/2)^t S_t^2/2`, thereafter grow by at least a factor two each period. Thus actual discounted winnings are infinite for every positive perturbation, whereas the reference value is finite. No finite right derivative or finite common price exists. A derivative of the linearized system still equals the displayed value `2`; this distinction is precisely the finding.

**Scope check.** S0 states no global growth/integrability hypothesis. A6's brief “payoffs linear” accompanies the field-model assumptions and does not clearly restrict the prize, which S3:49 explicitly introduces as a general `Omega(S)` with `g_j` a local derivative. Core line 72 distinguishes a general symmetric steady state from the proportional-prize balanced path. If A6 is intended to forbid nonlinear prizes, that restriction must be made explicit here; the theorem currently reads more broadly. The fixed-prize result and proportional-prize ratio case are not invalidated by this example.

**Repair.** Either say explicitly that the generic formula values the linearized system, without claiming it is the derivative of nonlinear lifetime utility, or add a global growth/tail bound sufficient for differentiation of the discounted continuation sum. Restricting to the already analysed globally proportional prize is a simpler sufficient repair. Merely adding finiteness at the reference point or constant coefficients there is insufficient.

## M3-03 — P2, narrow wording repair — The alternative premise in `onegroup` still admits its own covariance counterexample

**Stable key:** `onegroup`.

**Current locations:** `src/core/30_s3.md:90–92`; proof `src/supp/03_S3.md:88`.

The added “among carriers otherwise alike” is the right premise. Its disjunct “or holding each carrier's other payoff fixed” does not imply it: heterogeneous fixed background payoffs can remain correlated with the trait. In a population of equal masses with traits `z=(1,0)`, fixed backgrounds `phi=(2,0)`, trait cost `c=1`, global benefit `b*zbar=1/2`, and increasing affine fitness `w=1+pi`, fitness is `(2.5,1.5)` and `Cov(w,z)=1/4>0`. There is no transmission. This satisfies the literal second branch of the premise and violates the conclusion even for the single-group partition.

The new scope immediately below correctly states the covariance formula and therefore already explains why the example works. This is an incomplete premise repair, not a fresh objection to the corrected otherwise-alike lemma. The proof also assumes a common `pi_0`, not merely fixed heterogeneous backgrounds.

**Repair.** Delete the second branch or replace it with an explicit zero-background-covariance condition sufficient for each claimed partition (otherwise-alike backgrounds are simpler). If the intended claim is a controlled marginal comparison within a carrier, state that separately from the aggregate Price selection theorem. Retain the new covariance scope.

## Repairs checked and retained

- The nonnegative rank-one stability derivation and structural loop gain are correct under the stated decay/diffusion and reinforcing-channel premises.
- The channel-elasticity calculation correctly distinguishes provision, correction, capacity ratios and linear rule support. Faster capacity depreciation can raise the discounted gain; the source preserves that correction.
- The changed definition of `r_pr` directly along a zero-sum relative shift repairs the specific own-only versus relative derivative error. This review does not claim that repair alone proves every strategic continuation assertion.
- The cap-equality distinction and diffusion term in the laggard's inflow are retained correctly, including the local moving-leader cases and the excluded knife edge.
- Cumulative payoff-monotone selection, rather than sign monotonicity alone, now carries `load`'s extinction conclusion.
- The proportional-prize ratio model has constant coefficients; without provision/diffusion, its relative/common comparison and share-instability threshold coincide. The moving-Jacobian repair preserves this valid result.
- The exclusion of `theta_0=-1` from strict narrowing, and the welfare comparison's explicit restriction to a symmetric stage comparison, fix those previous overclaims.
- The otherwise-alike `onegroup` proof is correct; M3-03 concerns only the remaining alternative wording.

## Verification record

`python3 reviews/codex-third/math/audit_math.py` passes. The script checks the exact gains and divergence bound for M3-02, the Price covariance for M3-03, and independently re-runs the passive Bellman counterexample at two resolutions plus a linear control for M3-01. `results.json` contains the output. No assertion was changed in the manuscript's test suite.
