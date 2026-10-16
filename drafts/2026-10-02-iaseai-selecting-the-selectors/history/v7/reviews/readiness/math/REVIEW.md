# V7 fresh mathematical readiness review

Reviewed 4 October 2026. Reviewer role: adversarial formal mathematics, independent of the manuscript's verification scripts. No manuscript or assembled document was edited. Earlier review files were not read. The parent reviewer asked for independent adjudication of the opening's concentration/continuation equivalence after this review had already started; that provenance applies to Finding 2. Findings 1 and 3 arose from this review's own reading.

## Readiness verdict

- **Private specialist circulation: ready as an explicitly provisional draft**, with this review attached and the unproved strategic extensions identified. There is enough correct and explicitly conditional mathematics to support useful specialist scrutiny.
- **Public working paper: hold for a small, material correction pass.** R1 presently labels a false condition necessary in its stated class of selection rules. The opening also uses objective narrowing as a concentration criterion even though the paper's own results distinguish them. These are not defects that more numerical repetitions of the existing examples can settle.
- **Publication-ready theory: no.** Correct the findings below, obtain independent specialist review of the strategic continuation/enforcement claims already marked for review, and distinguish proof verification from empirical validation. This review did not audit all numerical equilibria, references, or empirical premises.

**There is a supported formal blocker as printed: Finding 1.** It limits the claimed universality of a requirements row; it does not refute the core reflexive-selection mechanism or the replicator special case.

All line numbers below are one-based. Paths are relative to `/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v7/`.

## Findings, ranked by severity

### 1. P1 — R1 is not necessary under the stated class of cumulative selection

**Location.** `src/core/90_s9.md:13` (assembled `THEORY.md:916`), with derivation at `src/supp/09_S9.md:7` (assembled `SUPPLEMENT.md:873`). Related scope ambiguity: `src/core/a0_s10.md:46–49` and `src/supp/10_S10.md:37` (assembled `THEORY.md:992–995`). The operative definition is `src/core/30_s3.md:23`; the earlier, valid load proposition at `src/core/30_s3.md:34–36` explicitly assumes `tau_eff(t) < nu`.

**Claim.** Viability at every horizon requires both `B(t)=integral(nu-tau_eff) not tending to +infinity` and `limsup average(tau_eff) >= nu`, under cumulative payoff-monotone selection.

**Why the implication fails.** The cumulative condition lower-bounds relative growth when a payoff gap is positive. On intervals when that same gap is negative, applying the definition with the carrier order reversed gives an *upper* bound on its growth. It therefore cannot be integrated as a lower bound over a gap that changes sign. The proof silently extends the positive-gap load proposition beyond that premise.

**Exact counterexample.** Use two otherwise identical load types, `e_race=1`, `e_rest=0`, private advantage `nu=1`, and race share `x`. Let

```
g(t) = pi_race-pi_rest = 1-tau_eff(t),
d logit(x)/dt = f(g),       f(g)=g+g^3.
```

This is a smooth, relative, payoff-monotone selection rule. For every positive gap, `f(g)>=g`; reversing the carrier order gives the same inequality for the other carrier, so it is cumulative with `varkappa=1` exactly as defined. Use a repeating 1.4-unit cycle:

- `tau_eff=0` for 1 time unit: `g=1`, `f(g)=2`;
- `tau_eff=3` for 0.4 time units: `g=-2`, `f(g)=-10`.

Each cycle adds `1-0.8=0.2` to `B`, so `B(t) -> +infinity` and average liability tends to `1.2/1.4=6/7 < 1`. Yet each cycle adds `2-4=-2` to the race log-odds: the race share tends to zero. From `x(0)=0.001`, its global maximum is attained at the end of the first positive interval and equals

```
x_max = logistic(logit(.001)+2) = .0073421467117.
```

Take the paper's host, `rho=.05`, `h_V=.08`, `V(0)=1`, and floor `.3`. The reach condition holds because `.08 > .05*(1-.3)`. But comparison with the constant maximal load gives, for **all time**,

```
V(t) >= 1-(.08/.05)*x_max = .988252565261 > .3.
```

Both claimed necessities fail on a viable trajectory. The discontinuities are in a permissible external liability schedule, not in the selection rule; short smooth transitions preserve both strict cycle inequalities. The independent numerical integration over 100 cycles gave minimum `V=.999674536352`, final race share `1.3853e-90`, and `B=20`. The all-time analytical comparison, rather than that finite run, establishes the counterexample.

**Minimal correction.** Restrict R1 to replicator dynamics, or an explicitly constant positive multiple of payoff differences, when liability may cross the private advantage. Alternatively state a requirement in terms of the actual integrated selection response. Do not repair this by merely adding “cumulative”: the example satisfies that condition. Preserve the load result under its original positive-gap premise.

The safeguards theorem begins by assuming replicator dynamics, so its part (3) can be read as still inheriting that restriction. On that reading the theorem is correct and R1 is the false generalization. Clarify this rather than presenting the theorem itself as refuted in its replicator form.

**Effect on the thesis.** The manuscript cannot reject all arrangements with sub-threshold time-average liability on the stated general selection class. Strong intermittent correction can work. The selection-of-load mechanism and the need to account for correction remain intact.

### 2. P2 — The opening equates objective narrowing with concentration

**Location.** `src/core/10_s01.md:7` (assembled `THEORY.md:50`); parallel Chinese opening in `src/core/00_head.md:14`. Policy scope is developed at `src/core/60_s6.md:103`; claim-register rendering D19 is at `src/reg/CLAIMS.md:263`. The correct distinction already appears in `src/core/20_s2.md:38`, `src/core/30_s3.md:75–80`, and `src/supp/03_S3.md:73–78`.

**Claim.** Games “competitive in dynamics and [that] concentrate” are identified parenthetically with games “where reinvestment's relative return exceeds its common return.”

**Counterexample within the exact printed stock model.** Set a fixed prize, `n=2`, `kappa*Omega=1`, `d=.2`, `r=1`, `beta=.5`, no provision or diffusion, and discount `.9`. Then

```
Gamma=.5 < 1,
Gamma_delta=9/28,
lambda_rel=9/19 > lambda_com=0.
```

Total capacity at the symmetric steady state is 5. From stocks `(2.6,2.4)`, every relative gap shrinks exactly by `.9` each period; after 100 periods it falls from `.2` to `5.31228e-6`. The common/relative calculation narrows the working objective, while the allocation converges to equality. No inference to concentration is available. The proportional-prize model with diffusion supplies a second counterexample band explicitly proved in S3.

**Minimal correction.** Give concentration and continuation narrowing separate criteria. The equivalence can be retained only for the paper's proportional-prize, no-provision, no-diffusion case, with the local qualifications. For broad E1, say whether concentration is a separate empirical eligibility condition rather than something established by the return inequality or by universal adoption leaving relative shares unchanged.

**Effect on the thesis.** This does not invalidate the correctly stated continuation theorem. It matters because the opening makes the inequality appear to operationalize the scope of a proposed restriction, and thereby includes stable, equalizing contests without an additional concentration argument.

### 3. P2 — The correction requirement need not rise with scope at fixed total size

**Location.** `src/core/40_s4.md:46` (assembled `THEORY.md:368`); proof `src/supp/04_S4.md:29`. The necessary qualifier is already stated in the scope proposition at `src/supp/04_S4.md:13`.

**Claim.** `d_star` rises with the dominant carrier's “size and scope,” without specifying what is held fixed or the pattern of conversion across domains.

**Counterexample.** Hold total share `p=1` fixed and broaden the profile on two occupied domains from `(1,0)` to `(.5,.5)`. Take the occupied-domain block of `Ahat` to be `I_2`, and `chi=gamma=eta=c_ev=a_ev=Bhat=1`, with baseline conversion `A=0` and no cost floor. Evaluation is a separate unoccupied domain; its two incoming conversion coefficients can both equal one, keeping `Bhat` fixed. Then `Yhat` falls from `1` to `.5`, the selected capacity is `q_star=Yhat/d`, and the certificate boundary is `d_star=sqrt(Yhat)`: it falls from `1` to `1/sqrt(2)`. Spreading fixed activity across domains with no conversion between them lowers the requirement.

**Minimal correction.** Specify a fixed per-domain footprint, or state the cross-domain conversion condition from the scope proposition. At fixed total size in its symmetric parameterization, scope raises the return only when off-diagonal conversion exceeds diagonal conversion. The proof's reference to the scope proposition does not supply this missing condition to the core statement.

**Effect on the thesis.** Larger carriers can still cultivate more influence under the size assumptions. Diversification across domains has no universal sign; the proposed empirical scope measure must distinguish total expansion from spreading a fixed footprint.

## Results that withstood this review

- **Core loop gain.** The deterministic nonnegative rank-one linearization and the `Gamma<1` local stability criterion check out. Independently generated one- to five-channel systems produced zero threshold mismatches in 1,000 cases. This does not validate global concentration or the lottery/strategic extensions.
- **Continuation objective.** The common/relative decomposition, Sherman–Morrison prices, and working-weight identity are coherent under the current deterministic, fixed-opponent, constant-coefficient and discounted-tail premises. The fixed-prize and one-stock proportional-prize tail arguments are substantive safeguards against a false nonlinear infinite-horizon inference. No counterexample was found within those narrowed cases.
- **Selection and capture.** Translation invariance, the positive-gap load result, the otherwise-alike Price-covariance result, the field's row-sum recovery certificate with its initial-state qualifications, and the correction-rate exponent have coherent derivations. The transient bound `a*z(0)<=c` prevents an initially acceptable share from increasing under a uniformly safe inbound bound. These do not prove current institutional independence or connect coverage to authority.
- **Enforcement.** The deviation-value accounting identity passed 1,000 independent randomized cases with maximum absolute error `8.9e-16`. Its necessity/sufficiency for a particular credible reversion is distinct from existence of globally optimal credible punishment in a stochastic game; I did not independently certify that extension.
- **Coverage.** The uniform coverage-lag/residual-floor implication to zero survival follows from the conditional product bound. The converse with a uniform summable residual upper bound below one also follows. Neither is evidence that the residual-floor premise holds for AI.
- **Later spot checks.** The sharing-convention algebra, host-margin comparison for fixed replicator dynamics, pause/depth formulas, and stated sequential-test boundary error inequalities were checked analytically at the level of their displayed derivations. The high-precision dwell numbers and the full signaling-equilibrium inventory were not independently recomputed.

## Computation and limits

`independent_checks.py` and `independent_results.json` in this directory contain all fresh computations reported above. Run with ordinary Python 3; no external package or manuscript code is imported. The file includes the exact R1 cycle calculation plus a bounded RK4 host check, the equalizing fixed-prize counterexample, direct power iteration for independently generated stock Jacobians, and direct discounted valuation of enforcement deviations.

I read the current core sources through the requirements and generative sections, the relevant proofs in S2–S6/S9–S11, S13's interface inventory, and the claims/test registers as scope checks. I checked assembled line locations for the findings. I did not use old reviews or the existing test suite as proof of correctness, run a mutating build, inspect all citations, independently solve every reported strategic equilibrium, or verify the empirical applicability of the formal premises. S13's open links and the manuscript's own specialist-review flags remain real limits to readiness.
