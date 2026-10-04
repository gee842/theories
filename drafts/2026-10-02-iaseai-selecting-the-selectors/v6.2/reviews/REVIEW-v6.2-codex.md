# V6.2 comprehensive independent review

Prepared for Ren on 4 October 2026. This file combines four review tracks: formal mathematics; systems, alignment and transition; evidence, alternatives and governance; and integration, verification and authorial fidelity. It includes the complete specialist reports after the synthesis, so the findings, demonstrations, repairs and source audit are available in one file.

**Assessment: preserve V6.2's architecture and corrected deterministic results, but revise several mathematical interfaces and decision rules before relying on the strongest claims.** The major V6.1 repairs are real. The remaining problems are concentrated where a result crosses from one model into another, where a sufficient condition becomes a boundary, or where an unmeasured recommendation acquires the language of an operational guarantee. They do not justify discarding the central question or treating the whole manuscript as invalid.

The most serious findings concern the exact strategic price of standing, delayed-breakout enforcement, the inference from masked detection to residual hazard, readiness error guarantees, and withdrawal of protection merely because risk is falling. These have mathematical demonstrations or counterexamples. Other findings concern missing premises, inconsistent scope, an unfairly staged comparison of failures, and source-specific corrections. Normative disagreements and openly acknowledged empirical gaps are identified separately.

**Verification:** the default suite reproduced **188 passed assertions and zero failures**, across all 40 blocks, in 315 seconds. Assembly and cross-reference checks passed in an isolated copy; the rebuilt material was byte-identical to the reviewed input. Independent counterexample scripts supplement that run. The passing suite and the findings are compatible: several disputed cases lie outside its tested assumptions, and some inherited computations are diagnostic rather than enforced assertions.

No manuscript, register or existing check script was edited, and no commit was made. The reviewed `THEORY.md` SHA-256 is:

```text
f50fb6a1b0f71ce33374946ab77da607a9631998d390e619296e6549e6822872
```

The [input manifest](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/review-input-manifest.json) records 61 input files. Exact references below refer to that snapshot. These are separate Codex review assignments with cross-review, not statistically independent model families or human expert endorsements. This is a deep audit across the argument, not a certification of every inherited proof or bibliography entry.

## How to read this review

Read this synthesis for the decision and revision order. The remainder contains the complete reports, including derivations and counterexamples:

1. **Formal review:** F1–F6, and scope notes F-C1/F-C2.
2. **Systems and alignment review:** SA-01–SA-09.
3. **Evidence and governance review:** EG1–EG10, including an 18-entry primary-source audit.
4. **Integration and verification review:** I1–I4, including the preservation sample and test-runner audit.

P1 means repair before treating the affected central mathematical statement or safety decision guarantee as established. P2 means a substantive local error, missing premise, or argument/design distinction. P3 means a narrow boundary, source or presentation correction. Confidence concerns the identified mismatch, not a forecast of the world. I4 is optional presentation advice: the author's direction to retain a complete theory of record is respected.

## What V6.2 has successfully repaired

| Earlier issue | Current assessment |
|---|---|
| Price of standing used beyond its convergence domain | **Closed for the deterministic structural result.** The discounted domain is now stated. Structural instability does not itself invalidate a discounted derivative. A different stochastic/strategic extension remains overbroad: F1. |
| A universal sign assigned to correction | **Closed in the channel theorem.** Capacity ratios and level-dependent rule support are now distinguished by elasticity. Do not reintroduce the claim that faster depreciation always reduces compounding. |
| Test Γ had the wrong direction | **Closed in the stated capacity example.** The ratio of responses to shared harm and private cost now rises with provision and diffusion; the perception confound is acknowledged. |
| Cap equality and diffusion omitted | **Closed in the revised conditional result.** Equality has a separate local threshold; diffusion is included; return from every start is distinguished from local return. |
| Falling positive linear costs contradicting the rate law | **Closed in the reviewed formulation.** The zero-floor and positive-floor cases are separated, and necessity requires tracking while sufficiency uses the stated capacity envelope. |
| Equal incidence called necessary for compliance | **Closed as a necessity claim.** Compliance and neutrality are separated. There remains a strict-versus-weak exclusion error in some summaries: SA-06. |
| Stage mirroring applied to all stochastic punishments | **Closed within the exchangeable continuation case.** Label-dependent and role-differentiated continuations are acknowledged. The new timing interface is a separate defect: F2. |
| The delegation result lost p=1 | **Closed.** The restriction is restored; static and dynamic claims are better separated. |
| Nonlinear fitness invalidated the between-group sign | **Closed.** Total and within-group signs are separated from the affine-only between-group conclusion. A different missing common-background premise remains: F6. |
| Row sums treated as necessary | **Closed in the reviewed certificate statement.** They are sufficient, with the low-start counterexample retained. Equality in the pruning result needs a further boundary qualification: SA-09. |
| Successful correction called a refutation of conversion | **Closed in Test M.** A successful remedy is distinguished from a refuted mechanism. Test B still needs its own correction: SA-04. |
| Joint scissors closure presented too strongly | **Substantially closed.** The arms, reduced joint computations and empirical C0 are distinguished. Keep that status; fix the remaining price/timing and channel-scope interfaces. |
| Coercive restriction treated too readily as settled policy | **Improved.** It is now in the compared tier, with its own hazards. That is a meaningful change even though the comparison and commitment rules still need repairs. |
| Lost rulings and model paraphrases obscured | **Improved in the inspected sample.** Restorations are findable, and the R/A/D/L provenance distinctions are useful. English and Chinese renderings should retain those qualifications. |

This closure table matters: the new review is not a repetition of the old one. Most of the current defects arise at new or newly emphasized connections, rather than from failure to incorporate the previous counterexamples.

## The five repairs to make first

### 1 Separate deterministic standing prices from stochastic lottery values

**F1.** [Proposition 2.2(4)](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:138) applies a local scalar resolvent to symmetric Markov equilibria, while its supporting lottery jumps away from parity after every win. An envelope theorem does not replace derivatives at those successor states with the derivative at parity.

The formal report gives both an exact two-state lottery counterexample, with true marginal value **5/6 rather than 1**, and a separately implemented strategic Bellman calculation. In the latter, the finest grid gives a scalar prediction of **0.660742**, an actual finite prize premium of **0.516436**, and a marginal injected-stock value of **0.522543**, with discounted loop gain below one. These are different mathematical objects, not alternative names for one exact number.

Retain the deterministic local theorem. State the lottery's Bellman equation and distinguish marginal value, finite prize premium and conditional mean dynamics. An approximate closure needs an approximation claim and error analysis. The numerical observation that rivals can amplify the premium remains useful.

### 2 Carry arrival times into the enforcement values

**F2.** The original next-period enforcement inequality is sound. The extension at [Remark 5.5](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:472) cannot put a slow breakout into it solely through the probability of escaping timely response.

With the same escape probability, a win at period eight has a different discounted value from a win next period. The explicit example yields a deviation value of **0.9106635**, below cooperation's 1, while the time-compressed substitution gives **1.075**, above it. Thus the substitution reverses deterrence in that example.

The repair is small but important: either make the whole episode one consistently discounted macro-period, or define conditional continuation values that include interim payoffs and random arrival times. The identity for escape probability survives. The claim that the clock enters *only* there does not. The systems reviewer independently challenged and confirmed this distinction.

### 3 Do not infer residual-risk impossibility from detection failure

**SA-01.** [Remark 6.8](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:635) correctly identifies the failure of sanctions when detection times sanction is below the cost of safety. It does not thereby prove that removal is impossible, that no intervention reduces risk, or that the residual-floor and coverage premises of Theorem 5.13 hold.

An undetectable divergence can coexist mathematically with a summable residual hazard after another intervention. This is a counterexample to the inference, not evidence that such an intervention exists today. Replace the impossibility claim with a claim about the absence of an established assurance case. If the protection standard recommends stopping or slowing on that basis, present it as that recommendation, under named premises.

### 4 Make the readiness test match the decision it controls

**SA-02.** [Remark S11.3](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:1051) correctly gives bounds for two simple registered hypotheses. It then applies them to being anywhere below or above a policy threshold. Those are different tests.

With tested means 0 and 1 and a policy threshold at 0.5, the review's simulations declare a true mean of 0.49 ready about **49%** of the time, despite a nominal endpoint false-release bound near 1%. The endpoint calculations remain valid. The threshold-wide promise does not.

Add an indifference band with a specified action, or a sequential procedure with the required composite-null guarantee. Also specify residence, repeated reopening, and the horizon over which the error budget applies. Independent mathematical cross-review supports this as a scope-transfer defect, not an error in Wald's endpoint algebra.

### 5 Replace falling-risk withdrawal with a cumulative-risk criterion

**EG1.** The C1 row at [THEORY:1200](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:1200) withdraws E3 and the case for E2 when class-specific residual risk is falling. Falling risk is neither a finite-horizon tolerance certificate nor a summability certificate.

For example, h_t=1/[2(t+1)] falls to zero while its sum diverges and survival tends to zero. The evidence report also gives a declining-risk example satisfying the manuscript's coverage-lag and residual-floor danger premises. Conversely, a very small constant hazard may satisfy a specified short-horizon tolerance despite not being summable forever.

Separate trend, cumulative finite-horizon loss, and tail claims. State which bound permits withdrawal, including deployment scale and uncertainty. A declining series is evidence of improvement; it should not alone switch protection off.

## The remaining findings and their practical effect

| Findings | What needs repair | What remains valid |
|---|---|---|
| F3 | Add cumulative actual selection strength to the fixation/floor-crossing claim. Payoff-monotonicity controls direction, not sufficient accumulated movement. | The relative direction of selection; the separate silent-crossing proposition that already assumes replicator dynamics. |
| F4 | Exclude θ₀=−1 from strict narrowing; record endpoint invariance. | The interior relative-versus-common return theorem. |
| F5 | Destruction must beat rest as well as expansion. | Relative accounting can ignore a common host cost. |
| F6, I2 | State the common-background premise of the global-benefit trait theorem; distinguish it from the author's stronger thesis about shared understanding. | The partial selection effect and the philosophical/institutional thesis, with their different status. |
| F-C1, F-C2 | Keep the won-share scaling result within fixed-decisiveness channels; label the welfare comparison as a stage comparison. | The capacity-channel pivot and the stage collective-action result. |
| SA-03 | The minimum type threshold is a conservative sufficient participation basin, not the aggregate tipping boundary. | The one-type tipping result and the below-minimum sufficient condition. |
| SA-04 | Test B must measure relative net advantage, not just the supporter's absolute cost. | Free riding in the matched-carrier comparison and the appropriability mechanism. |
| SA-05 | Make the host margin's iff statement conditional on a constant effective margin; a lower bound on a varying margin is only sufficient. | The constant-control transient viability calculation. |
| SA-06 | Distinguish weak deterrence from elimination, and zero tax from negative tax. | Protection of safe variants under weak inequality; selection-out under appropriate strict cumulative disadvantage. |
| SA-07 | Specify dependence across oversight layers or use conditional link reliabilities. | The independent-link benchmark and common-blind-spot ceiling. |
| SA-08 | Identify the joint dynamics and basin before claiming that every arrangement with the seven marks changes it. | The row-by-row intended direction and the attributed maxim. |
| SA-09 | Add strictness/nondegeneracy to core pruning at gain one. | The strict certificate and hyperbolic-configuration results. |
| EG2 | Do not infer violation of a probability tolerance merely from a possible irreversible outcome. | The declared protection values and explicitly uncomputed qualitative judgment. |
| EG3 | Compare matched fault-to-loss paths and timely remedies on both designs. | The value of designing remedies and the candid statement that they are untested. |
| EG4 | Retain execution and failed-actuation delay after precommitment; distinguish prepared from installed and binding. | The reason to prepare early and the possibility of removing later discretionary deliberation. |
| EG5 | Separate bounded preparation from binding commitment to a design whose durability is still unresolved. | Persistent reasons for research and preparation across the named cruxes. |
| EG6 | Give E2's hazard and strategic-domination triggers an explicit precedence/combination rule. | Having separate grounds for stopping; keeping stopping distinct from slowing. |
| EG7 | Reverse the mistaken pacing inference and discuss the primary paper's monitoring-lag extension. | The question of whether its particular assumptions apply here. |
| EG8–EG10 | Bound claims from public lead data; correct narrower factual statements; separate hash commitment from secrecy. | The verified observations and the aim of preventing test gaming. |
| I1 | Make intended test failures affect exit status; label exploratory output. | The actual 188 assertions and their observed passing run. |
| I3 | Operationalize estimands, rival models, effect sizes and dwell windows before treating the research outline as an executable test. | The value of registering mechanisms and possible disconfirmations in advance. |
| I4 | Optional: make the advertised entry route easier to read after the substantive repairs. | The full-length theory of record and restored authorial language. |

The final cross-review deliberately lowered the priority of EG2–EG4. The manuscript admits missing estimates, labels its ranking a judgment, says remedies are untested, and acknowledges unresolved enforcement against the strongest. Those qualifications must be credited. The remaining issues are specific unsupported inferences and incomplete operational accounting, not concealed validation or a claim that the paper has already computed an empirical ranking.

## Table 7.1 audit

The threshold table is a useful improvement. Its row-by-row theorem labels and explicit cross-model daggers should remain. Its nine rows have different scopes and should not be treated as one empirically measured state vector.

| Row | Audit result |
|---|---|
| Load | Restore the cumulative-selection premise for the asymptotic crossing claim. Equal incidence serves neutrality; effective liability and incentives serve load and compliance. |
| Compounding | Sound as a deterministic local result under the maintained channel assumptions. Separate stochastic conditional drift from random-path stability; retain the channel-specific lever signs. |
| Standing | Sound for the interior held-objective domain and stated deterministic reference. Fix the purely relative endpoint and the exact strategic-price extension. |
| Capture | The rate law and sufficient certificate are useful. A failed certificate is not itself demonstrated capture; tracking, floor, initial-state and human-capacity assumptions remain material. |
| Enforcement | The next-period condition is sound. The detection-time translation needs time-adjusted continuation values and a real response mechanism. |
| Coverage and tempo | The stated residual-hazard/summability and mode-specific timing distinctions matter. Do not replace them by a trend test at activation or release. |
| Talk | The effective-bias inequality re-derives within the specified cheap-talk game. Proposed institutional remedies must actually alter the relevant bias or information structure; naming a remedy is not measuring that change. |
| Alignment tax | The matched-variant argument survives. Keep detectability, assurance, removal, residual risk and strict exclusion distinct. |
| Delegation | The corrected certain-lock game survives its premises. Practical scope depends on pricing the lock and retaining meaningful human authority; it is not an unconditional ban proved by the static game. |

## Revision order and acceptance criteria

1. **Repair the mathematical statements by stable key in `src/`.** Start with `loopgain`, `eqgain`, `standprice`, `detectlink`, `masked`, `readrule`, `readiness`, then the smaller scope and boundary results. Retain correct subresults; do not weaken test tolerances to preserve an exact claim.
2. **Repair activation and withdrawal as one decision system.** Specify the risk measure, protected horizons, feasible mechanism, full response delay, trigger combination, uncertainty and release test. A favorable crux should withdraw only the protection whose justification it actually removes.
3. **Make comparisons parallel.** Apply the same hazard-to-terminal-loss tree and the same horizon to continuation and proposed designs. Label untested repair mechanisms as conditional opportunities for recovery.
4. **Propagate statuses across the documents.** Update Table 7.1, S13, CLAIMS, TESTS, the abstract, Chinese guide, argument chain and conclusion together. A correct Supplement cannot repair an unqualified headline by proximity.
5. **Strengthen verification where it matters.** Add the exact counterexamples and harness failure checks. Establish an indifference/composite-null readiness guarantee, a timing-aware enforcement example, and a vector participation example. Keep diagnostic tables distinct from tests.
6. **Correct the targeted sources and then operationalize one empirical test.** Read the pacing paper's full extension; fix the smaller factual and hash claims. Choose one corrector domain or one intervention with observable mediators, rather than trying to estimate the entire theory at once.

The next review should be able to close each item by a changed statement, proof, counterexample test, or explicit change of status. It should not require a new overall architecture or another layer of universal claims. No estimate of Γ, verified C0, full stochastic strategic welfare theorem, or reachable global generative basin is demanded merely to publish a conditional theory. Those remain limitations until the paper relies on them as established.

## Evidence and reproducibility record

| Artifact | Purpose |
|---|---|
| [Input manifest](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/review-input-manifest.json) | SHA-256 and size of each frozen input. |
| [Build comparison](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/build-comparison.json) and [xref log](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/xref-review.log) | Successful isolated rebuild, no content differences, structural checks. |
| [Full numerical log](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/checks-review.log) | All 40 default blocks; 188 passing assertions. The heavy `--full` and all `--legacy` suites were not rerun in this review. |
| [Counterexample entry point](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/counterexamples_v62_codex.py) | Runs the independent formal and systems audits and the failure-reporting demonstration; adds the falling-hazard example. |
| [Formal independent script](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/formal-audit/independent_audit.py) | Exact examples and a separately implemented Bellman solver, without importing manuscript model code. |
| [Systems independent script](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/systems-audit/audit_systems.py) | Independent ODE integration, readiness simulation, and dependence/boundary examples. |
| [Verification summary](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/verification-summary.json) | Runtime, input preservation and test-run summary. |

The initial isolated xref run lacked the sibling V6 bibliography imported by the reference builder. Supplying that repository dependency produced the passing run. This was not a release build failure. The default numerical suite ran against the reviewed checkout and wrote only a new review log. The separate fault injection altered checker text in memory, not the checker on disk.

The source audit verifies a targeted set of load-bearing primary sources; it is not a fresh verification of every historical book or bibliography entry. The provenance audit similarly samples restored rulings rather than certifying all 1,060 preservation-ledger sentences. All specialist limitations are retained below.


## Formal review

Date: 4 October 2026. Reviewed material: the assembled V6.2 `THEORY.md`, `SUPPLEMENT.md`, relevant `CLAIMS.md` and `TESTS.md` entries, the stable-key map, and the implementation and assertions of numerical block MP. This report concentrates on Sections 2, 3, 5 and 7: the structural loop, the price of standing, channel levers, enforcement, and the scissors. It does not claim independent verification of the entire manuscript or every one of the 188 checks.

No manuscript source or assembled document was edited. No commit was made. The independent script and its output are `reviews/formal-audit/independent_audit.py` and `reviews/formal-audit/results.json`. The script uses the Python standard library and imports no manuscript implementation.

### Overall judgment

The deterministic structural mathematics is substantially stronger than V6.1's reported form. The rank-one loop gain, the separation between common and relative returns, and the elasticity-based signs of the levers are coherent and useful results. The distinction between an instability threshold and the speed at which a gap opens is particularly important. The enforcement inequality itself is correct under its stated one-period timing and credible-continuation premises. Treating real-world co-movement as C0 is a real improvement.

Two central extensions still exceed what is proved. First, a local deterministic resolvent is presented as an exact strategic standing price, while the supporting computations solve a stochastic lottery whose continuation value is not determined by derivatives at parity. This is a theorem/model mismatch, not merely a request to run a finer grid. Second, an actual time to breakout is inserted into a one-period absorbing-state game through escape probability alone; this leaves the timing and discounting of the successful and punished branches out of the enforcement calculation. Both errors affect interfaces advertised as proved.

There are also narrower repairs: the convergence part of Proposition 3.4 needs cumulative selection, the strict narrowing statement excludes the purely relative endpoint, the frontier-switch claim must compare destruction with rest, and the common-benefit trait result needs its proof's common-background premise in its statement.

### Findings at a glance

| ID | Priority | Confidence | Finding | Stable keys |
|---|---|---|---|---|
| F1 | P1 | High | The exact strategic-price claim conflates a deterministic local system, stochastic continuation values, and a finite prize premium | `loopgain`, `eqgain`, `standprice` |
| F2 | P1 | High | Escape probability alone does not incorporate the discounted timing of a slow breakout | `detectlink`, `enforce`, `scissors`, `jointscissors` |
| F3 | P2 | High | Payoff-monotonicity plus an unbounded raw payoff advantage does not imply fixation or host-floor crossing | `load` |
| F4 | P2 | Certain | Strict narrowing fails at the permitted endpoint θ₀ = −1 | `standprice`, `scissors` |
| F5 | P2 | High | The frontier-switch inequality can select rest, not destruction | `frontier` |
| F6 | P2 | High | The global-benefit trait theorem omits the common-background premise used in its proof | `onegroup` |
| F-C1 | Scope clarification | High | Keeping the won share fixed does not hold general level-channel gains fixed | `scissors`, `chansign` |
| F-C2 | Scope clarification | High | The welfare judgment imports a stage comparison; it is not yet a lifetime-welfare theorem for the full dynamic game | `twoerrors`, `boundary` |

P1 means repair before treating the corresponding central interface as a theorem. P2 means a definite local statement or scope error with a relatively small repair. These priorities do not mean the entire thesis is refuted.

### F1. The strategic standing price is not an exact local resolvent for the lottery game

**Locations.** `THEORY.md:138` (Proposition 2.2(4)); `THEORY.md:140` (numerical strategic interpretation); `THEORY.md:271` (Proposition 3.9 strategic scope); `SUPPLEMENT.md:119–121` (proof); `SUPPLEMENT.md:139–158` (strategic computations, especially 140 and 153); `SUPPLEMENT.md:298` (finite-jump exactness and strategic price); `SUPPLEMENT.md:1104–1105` (interface status). Register: `CLAIMS.md:60`, `CLAIMS.md:74`, `CLAIMS.md:224`. Keys: `loopgain`, `eqgain`, `standprice`.

#### The three mathematical objects need separate names

1. For deterministic share reinvestment, parity is an invariant reference state. The local derivative propagates through one fixed matrix, and the discounted geometric resolvent is appropriate.
2. For a lottery, parity is not invariant path by path. A win or loss sends the process to distinct successor states even when the starting state is exactly symmetric. Its Bellman derivative depends on values and derivatives at those successor states.
3. Block MP calls a finite secant, δ[V(s_win)−V(s_lose)]/Ω, a price of standing. The marginal value of an infinitesimal capacity injection is a derivative of V. The two are close when V is almost affine on the prize-jump interval, but they are not the same definition.

The proof at `SUPPLEMENT.md:121` applies the envelope theorem and then assumes that the resulting value derivative follows the same local state matrix indefinitely. The envelope theorem removes the derivative of the actor's own optimal control; it does not move successor states back to parity or replace a stochastic transition operator with its conditional-mean Jacobian.

For the two-player lottery used by the manuscript, with no shared loss and prize Ω=1, let s_w and s_l be the win and loss successors, each with derivative 1−d with respect to s. The exact Bellman-envelope equation is

\[
V'(s)=p_{\rm pr}'(s)\{1+\delta[V(s_w)-V(s_l)]\}
 +\delta(1-d)\{p(s)V'(s_w)+(1-p(s))V'(s_l)\}.
\]

At parity p=1/2. Closing this equation with one local gain requires additional equalities or approximations: both successor derivatives must be replaced by V'(s), and the finite value difference must be replaced by V'(s)(s_w−s_l). Neither follows from differentiability of the equilibrium at parity.

#### An exact counterexample without strategic response or numerical error

The core model says p can be a probability or a share. If it is used as an actual lottery with realized winnings reinvested, take

\[
n=2,\quad \Omega=\kappa=1,\quad k_0=1/2,\quad d=1,
\quad r=2,\quad \beta=\delta_f=0,\quad \delta=1/2.
\]

The symmetric deterministic reference has K*=1, ω=1/2, Γ=1, Γδ=1/2. The claimed deterministic marginal price is therefore 1.

After an actual lottery, stocks are (1.5,0.5) or their reverse. The leader's next win probability is

\[
q=\frac{1.5^2}{1.5^2+0.5^2}=0.9.
\]

The payoff-difference mode of this two-state Markov chain has multiplier 2q−1=0.8. A relative injection y at parity changes stocks to (1+y,1−y), with dp/dy=1. Its true discounted marginal standing value is

\[
\lambda_{\rm lottery}
=\frac{\delta}{1-\delta(2q-1)}
=\frac{1/2}{1-0.4}=\frac56,
\]

not 1. This does not refute the deterministic share theorem. It establishes that the probability interpretation needs a different theorem.

#### Independent strategic calculation

The script independently solves the manuscript's two-player Tullock lottery using Bellman iteration and the analytically solved within-state effort game. It separately measures the conditional-drift elasticity, the frozen-own-effort elasticity, the prize secant premium, and the infinitesimal stock-injection value. For r=4, structural Γ=0.45, d=0.1, δ=1/1.1:

| Grid cells | Bellman residual | Γδᵖʳ | Local formula Γδᵖʳ/(1−Γδᵖʳ) | Actual prize premium | Marginal injected-stock value |
|---:|---:|---:|---:|---:|---:|
| 800 | <10⁻¹² | 0.384993 | 0.625998 | 0.503215 | 0.508360 |
| 1,600 | <10⁻¹² | 0.394690 | 0.652046 | 0.513744 | 0.519680 |
| 3,200 | <10⁻¹² | 0.397860 | 0.660742 | 0.516436 | 0.522543 |

The theorem's discounted-gain condition is satisfied in every row. Refining the grid does not remove the difference; the local formula exceeds the prize premium by about 28% in the finest run. This is consistent with, and sharper than, the manuscript's own report at `SUPPLEMENT.md:153` of 0.64 versus 0.51.

Adding a requirement that the conditional mean dynamics be stable does not make the equality exact. At structural Γ=0.3 the independently computed equilibrium Γ is about 0.353<1. At 3,200 cells the local formula is 0.195145, the prize premium 0.194093, and the marginal injection value 0.194167. The small difference is still structural: a theorem of exact equality cannot be validated by a 0.5% acceptance tolerance.

Block MP's own assertions in `checks_v62.py:1967–1971` accept 2.5% error for a selected set and 0.6% for another subset. The larger discrepancies are excluded from that assertion rather than explained by the printed theorem's premises. The tests can pass while the theorem fails.

#### Stability is also a different stochastic claim

The rank-one proof for the derivative of equilibrium win shares is good. It gives the stability of the deterministic share map, or the derivative of the lottery's conditional expected one-step drift. It does not establish local asymptotic stability of a random path at parity. Starting exactly at parity in a nondegenerate lottery immediately produces a gap regardless of whether Γᵉᑫ is above or below one; symmetry can keep the unconditional signed mean at zero while dispersion grows. The manuscript should call the measured MP quantity a drift instability, and separately specify any claim about stationary dispersion, escape probabilities, or almost-sure dynamics.

#### Minimal repair

- State explicitly that Proposition 2.2(1)–(3) uses deterministic prize shares, or a separately justified deterministic mean approximation.
- Retain the exact rank-one result for differentiable deterministic equilibrium share dynamics.
- Restrict the exact strategic price result to a deterministic invariant symmetric reference with a valid local envelope closure; add the assumptions required for that closure instead of assuming policy differentiability suffices.
- For the lottery, replace the exact scalar price claim by the Bellman-envelope equation above. Label the scalar formula a local/small-jump approximation unless an error bound is proved.
- Define the marginal stock-injection value and the finite win-versus-loss premium separately. The reported MP ratios can remain numerical observations for the premium they actually compute.
- Change the relevant interface and register entries from “form proved” to the appropriate split status. An “outside review” tag on magnitudes does not repair an overbroad theorem about their form.

The qualitative discovery that rivals' responses can greatly amplify a prize premium remains supported by the calculations. The defect concerns exact closure and the interpretation of stability, not the existence of discouragement in these examples.

### F2. A slow breakout requires discounted timing, not escape probability alone

**Locations.** `THEORY.md:457` (success is decisive from the next period); `THEORY.md:468` (slow breakout folded into p_d); `THEORY.md:472` (Remark 5.5); `SUPPLEMENT.md:462–468` (derivation and check); `SUPPLEMENT.md:544–550` (joint scissors); `SUPPLEMENT.md:1106` (join marked proved). Keys: `enforce`, `detectlink`, `scissors`, `jointscissors`.

The identity p_d=1−υ(T_dec) is correct when υ is the probability of detection and response by the decisive time. The inference that substituting this probability into equation (14) is an exact enforcement test for the resulting delayed game does not follow.

Equation (14) values the successful absorbing branch and the punishment branch from the next period. In a delayed game, those branches begin at different random dates. The interim flow payoffs, δ raised to the arrival time, and correlation between arrival time and outcome matter. The probability of escaping detection supplies none of these quantities.

#### A reversal of the deterrence conclusion

Take δ=0.9, C=1, g=0.3, D=1.5 and v=0. A deviation becomes decisive at t=8 unless answered. Detection and punishment occur at t=1 with probability 0.3, and otherwise never occur. Thus υ(8)=0.3 and p_d=0.7. On an escaping path, the actor receives C during t=1,…,7, and D from t=8 onward. The punishment branch gives zero from t=1 onward. Assume the punishment continuation is credible, just as in the original enforcement proposition.

The normalized value of cooperation is 1. Direct substitution into (14), equivalently the next-period branch calculation, gives the deviation value

\[
(1-\delta)(C+g)+\delta p_dD
=0.13+0.9(0.7)(1.5)=1.075.
\]

It declares restraint unenforceable. The actual delayed deviation is worth

\[
0.13+0.7\left[(0.9-0.9^8)\,1+0.9^8\,1.5\right]
=0.9106635<1.
\]

It is deterred. Both games have the same printed C, g, D, v, and p_d. Their difference is exactly the delay that the proposed interface suppresses.

The clock simulation at `SUPPLEMENT.md:468` checks escape probabilities and then assigns the resulting outcome the next-period values from (14). That validates the compressed model it simulates; it does not independently verify the advertised delayed interpretation.

#### Minimal repair

Retain the escape-probability identity. Then choose one of two explicit formulations:

1. Use one macro-period to include the entire race-to-detection experiment, and define g, D, v, and the effective discount consistently as payoffs/continuation values at the end of that macro-period; or
2. Keep ordinary time and use the expected discounted continuation value of each branch, including interim payoffs and the timing distribution. For the example above, the successful continuation from t=1 is C(1−δ⁷)+δ⁷D, not D.

Under either repair the probability-to-incentive bridge is conditional on those definitions. T_dec then changes both the escape probability and the discounted continuation values. The qualitative claim that faster breakout can worsen enforcement may survive, but it is not proved by differentiating p_d alone while retaining invariant per-period terminal values. Update S13 and the joint-model labels accordingly.

### F3. Proposition 3.4 needs cumulative selection, not merely payoff-monotonicity

**Locations.** `THEORY.md:214` (definition); `THEORY.md:225–227` (Proposition 3.4); `SUPPLEMENT.md:239` (proof); `THEORY.md:697` (threshold table). Key: `load`.

Payoff-monotonicity identifies the sign of relative growth, not its accumulated magnitude. The proof moves from the stated general assumption to the replicator identity d log(p_k/p_l)/dt=π_k−π_l. This is not true for every payoff-monotone rule.

Consider two carriers with loads e_R=1 and e_C=0, common background payoff, ν=1, and liability τ(t)=1−1/(1+t). The payoff gap is Δ(t)=1/(1+t)>0, and the paper's cumulative advantage is B(t)=log(1+t)→∞.

Use the relative, payoff-monotone selection rule

\[
\dot p_i=\operatorname{range}(\pi)\,p_i(\pi_i-\bar\pi).
\]

For these two carriers, range(π)=Δ(t), so

\[
\frac{d}{dt}\log\frac{x}{1-x}=\Delta(t)^2=\frac1{(1+t)^2}.
\]

The actual cumulative log-odds change is one, not infinity. Starting with x(0)=0.1 gives

\[
x(\infty)=\frac1{1+9e^{-1}}=0.2319693.
\]

With the host equation \(\dot V=V[(1-V)-x(t)]\), V(0)=1, and V_min=0.5, the manuscript's (reach) premise holds because 1>1(1−0.5). Yet the host remains above 0.768 and converges to about 0.768, not below its floor. This is a complete counterexample to the convergence-and-crossing conclusion as printed; it preserves the directional selection conclusion.

**Minimal repair:** replace “payoff-monotone” by replicator selection for the asymptotic clause, or add a condition that the actual cumulative log-ratio advantage diverges. More generally, if relative growth is a(t)(π_k−π_l), use ∫a(t)(ν−τ_eff(t))dt→∞. The term “cumulative selection” is usefully explained at `SUPPLEMENT.md:233`; import that premise into the theorem and threshold row instead of silently using it in the proof.

**Bound on impact:** Proposition 4.13 explicitly assumes replicator selection at `THEORY.md:421`, so this counterexample does not refute that theorem. Claims using the stronger cumulative-selection definition can remain; they should not cite the weaker printed Proposition 3.4 as if it supplied that condition.

### F4. The strict narrowing theorem misses the purely relative endpoint

**Locations.** `THEORY.md:234–235` (allowed θ domain); `THEORY.md:263–269` (Proposition 3.9); `SUPPLEMENT.md:279–281` (strict inequality argument); `SUPPLEMENT.md:540` (derivative sign). Key: `standprice`, with propagation to `scissors`.

The theorem assumes θ₀<n−1, while the globally declared domain includes θ₀=−1. At θ₀=−1 the common coefficient is already zero. Equation (9) gives θ=−1 for every admissible pair of gains, whether relative return is larger, smaller, or equal.

For example, n=4, θ₀=−1, Γδ=1/2, Γδᶜ=0 gives θ=−1, not θ<θ₀. The phrases “whatever θ₀<n−1,” “narrows whenever,” “widens where they do not,” and “no held self-model short of θ₀=n−1 escapes the narrowing” are therefore false at this permitted endpoint.

The fixed-prize derivative is proportional to

\[
-\frac{n(1+\theta_0)(n-1-\theta_0)}{[n-(1+\theta_0)\Gamma_\delta]^2},
\]

which vanishes at θ₀=−1. The proof at `SUPPLEMENT.md:540` reports only the other factor's sign.

**Minimal repair:** make the strict iff claim for −1<θ₀<n−1. Add that both endpoints are invariant: θ₀=−1 remains purely relative and θ₀=n−1 remains fully inclusive under the common/relative rescaling. Where endpoints are retained, state weak monotonicity. The interior theorem and its policy relevance remain intact.

### F5. The frontier switch must beat rest as well as expansion

**Locations.** `THEORY.md:451–453`; `SUPPLEMENT.md:433–440`. Key: `frontier`.

The model offers three actions: expansion, destruction, and rest. At θ=−1 their marginal values are

\[
v_X=\varphi(F)-c_x,\qquad
v_D=-c_y+\frac{\Delta_y}{n-1},\qquad v_R=0.
\]

The printed condition v_X<v_D compares only the first two. If both are negative, rest strictly dominates both, and there is no transition to mutual destruction.

Example: n=4, c_y=1, Δ_y=1, and v_X=−1. Then v_D=−2/3. The printed switch inequality holds, but the selected action is rest, with value zero. These numbers can be realized with positive remaining frontier, φ(F)=0.1 and c_x=1.1.

Nor does monotonicity of φ alone ensure a switch *before* the frontier is exhausted. That timing conclusion additionally requires φ to cross c_x+v_D while F>0.

The supplementary toy actually recognizes the costly-destruction case at line 440: “with destruction too costly to pay, no accounting fights.” That is evidence that the condition belongs in the theorem, not a reason to dismiss the counterexample as outside the model.

**Minimal repair:** destruction is strictly chosen iff v_D>max{0,v_X}. State a switch before exhaustion only when v_D>0 and the expansion value crosses v_D at positive remaining frontier. Retain the narrower conclusion that a purely relative objective ignores the common host cost even when destruction is never attractive.

### F6. The global-benefit trait result needs its proof's common background

**Locations.** `THEORY.md:281–285`; `SUPPLEMENT.md:304`; `CLAIMS.md:76`. Key: `onegroup`.

The proof writes π_j=π₀+b z̄−c z_j, with one common π₀. That makes payoff, and therefore fitness under the maintained monotonicity premise, decreasing in z alone. Under this model the Chebyshev covariance argument is correct, including the corrected distinction between total/within-group signs and the potentially positive between-group term under nonlinear fitness.

The theorem's prose only says that the trait costs its bearer and benefits everyone equally. It does not exclude correlated private background advantages. Those are enough to reverse total selection without transmission bias or a changed rule.

Take two equally weighted carriers with traits z=(0,1), backgrounds φ=(0,2), cost c=1, and the same global benefit 0.5 to each. Payoffs are (0.5,1.5), so Cov(z,π)=0.25>0. The trait bearer pays the stated cost and supplies an equal global benefit; it still expands because the associated background advantage is larger than the cost.

**Minimal repair:** state the result for otherwise identical carriers or for the partial selection effect of the trait holding background fitness fixed. More generally, with π=φ+b z̄−cz and affine fitness, total selection has sign Cov(φ,z)−c Var(z), so a no-positive-background-covariance premise suffices. The downstream institutional prose should distinguish “the globally common benefit alone supplies no differential selection advantage” from “a costly globally beneficial rule can never spread through selection.” The first is established; the second needs the extra premise.

This repair does not rescue undifferentiated selection as a reliable source of global protection. It makes the precise mathematical statement match the proof rather than claiming that all correlated routes have been excluded.

### F-C1. The won-share pivot is exact for fixed decisiveness, not for every stock channel

**Locations.** `THEORY.md:555–561`; `SUPPLEMENT.md:540`; contrast the correct elasticity result at `SUPPLEMENT.md:162–168`. Keys: `scissors`, `chansign`.

The ratio-channel capacity model has fixed r. There Γ and Γδ are proportional to ω with the other parameters fixed, and provision growing in proportion to stakes holds this capacity contribution fixed. The reduced joint models explicitly use this case and correctly demonstrate it.

The multi-channel generalization must preserve the condition that each r_j remains fixed. For a linear level channel σ=aX, decisiveness is r=aX*, so keeping ω fixed while raising both stakes and provision raises r and the gain. Take n=2, κ=a=1, d=0.2, β=δ_f=0, and k₀=Ω/2. Then ω=1/2 at every scale, X*=5Ω, and Γ=2.5Ω. Raising Ω from 0.2 to 0.8 while provision keeps exact pace moves Γ from 0.5 to 2.0.

This is already explained by Proposition S2.4, which says that provision changes no gain in a linear level channel. Consequently, the unqualified multi-channel sentence that “provision that grows with the stakes holds both still” is too broad. It should read as a property of the fixed-decisiveness capacity channel or of the two stated reduced models. It cannot cover rule-support channels without additional correction that offsets their scale dependence.

This is a scope clarification, not a rejection of the new channel-by-channel theorem. The new theorem is exactly what diagnoses the overextension.

### F-C2. The “game is wrong” welfare step needs a stage-versus-dynamic distinction

**Locations.** `THEORY.md:249–253` (Proposition 3.6); `THEORY.md:275` (Remark 3.10); `SUPPLEMENT.md:261`, `SUPPLEMENT.md:294`. Keys: `boundary`, `twoerrors`.

Proposition 3.6(1) proves a useful symmetric *stage* welfare comparison: as a common θ rises, equilibrium intensity falls, and the common flow welfare rises. Proposition 3.9 then computes a first-order continuation-induced weight under fixed rival conduct. Substituting the resulting lower θ into the static contest establishes the stated stage comparison.

It does not, without another construction, compare lifetime welfare between two fully specified dynamic equilibria in which net payoffs change capital stocks, prize growth, future intensities, and rivals' continuation responses. S13 appropriately acknowledges that the full stochastic game is open. The sentence at line 275 should specify “in the symmetric stage comparison of Proposition 3.6” or supply the dynamic welfare argument with a common feasible comparison path.

The stage-level interpretation is valid and supports a collective-action problem. It should not quietly carry the evidentiary weight of a solved dynamic welfare theorem. This clarification is especially useful because the rhetorical claim “each actor computes correctly; the game is wrong” is now a major part of the argument's front matter.

### Results that survived adversarial review

#### Structural loop gain

At a deterministic symmetric steady state, the relative Jacobian really is D+uvᵀ/n. The conditions d_j+δ_f,j≤1 and nonnegative conversions and marginal strength make it a nonnegative matrix. Its secular equation at eigenvalue one gives the printed Γ criterion, including the case of inactive channels. The common-stock deviations decay separately under a fixed prize. This result does not require strategic optimization, and it does not claim global concentration.

The proposition's exclusions of countervailing channels and different decisions feeding different stocks are substantive, not cosmetic. A negative delayed channel can destabilize a system whose signed “net gain” is below one; the displayed two-channel example correctly has complex roots of modulus greater than one. There is no valid objection that correction should simply be subtracted from Γ.

#### Discounted structural price and growing prizes

For the deterministic invariant reference, Sherman–Morrison yields the stated relative price on Γδ<1. The resolvent domain is the discounted instability condition, so structural Γ>1 alone does not invalidate a finite first-order discounted price. An objection that the price must fail whenever the undiscounted parity point is unstable should be rejected.

The common-mode Jacobian for an endogenous prize is diag(1−d_j)+κgᵀ. Diffusion cancels from this mode and remains in the relative mode. Decomposing today's payoff shock and matching the two coefficients gives equation (9). Apart from the endpoint correction in F4, the interior sign comparison is right. The fixed-prize model narrows the working weight wherever its relative return is positive; proportional prizes do not justify that same universal statement.

For Ω=gS with no provision, the common and relative absolute-stock multipliers are 1−d+κg and 1−d−δ_f+(1−β)rκg. The share multiplier is their ratio. Without diffusion, the interior narrowing threshold and the instability of equal shares both reduce to (1−β)r>1. With diffusion, their thresholds differ exactly as stated, and the gap is positive on the finite-value domain. The new growing-prize correction is mathematically meaningful.

#### Channel levers

Writing a channel term as a constant times h'(X*)/(d+δ_f) makes the elasticity result transparent. Provision affects X*; decay affects both X* and persistence. The printed signs in Proposition S2.4 follow. In particular, faster depreciation does not reduce the undiscounted gain of a pure ratio channel without diffusion, raises it with diffusion, and raises its discounted gain at δ>0. Correction in a linear level channel lowers both gains. The intuition that “faster decay always weakens compounding” is false in the maintained stationary ratio model and should not be reintroduced.

Small boundary conventions should be made explicit when wording is strict: at δ=0 all discounted gains vanish, and at a channel of zero conversion or zero decisiveness no lever can strictly lower that zero contribution. These do not alter the interior comparative statics.

#### The point of enough

The local cap-equality threshold with the restored diffusion term re-derives correctly. The fixed-opponent map is monotone under d+δ_f≤1, so the positivity of φ on the entire interval is an appropriate global-return condition. The distinction between local return just below a cap and return from every start is essential and now correctly represented. Diffusion is a source of rank-independent inflow and is not sufficient by itself to eliminate an interior trap.

“Return” should mean convergence as well as finite hitting: when the cap is exactly K*, a laggard may approach it asymptotically. This is a terminology point rather than a failure of the local condition.

#### Enforcement inequality and relative punishment

The one-period deviation valuation that produces equation (14) is correct. The comparative statics of the threshold, homogeneity in all payoff quantities, distinction between D<C, D=C and D>C, and punishment-race continuation formula are all algebraically sound. The repair that permits breakouts during punishment is important: setting punishment value equal to the no-breakout stage payoff would overstate deterrence in the manuscript's example.

Credibility remains essential and is now stated. The numerical agreement between a fixed discounted stream and (14) is an identity check, while an optimal deviation-plan computation is an incentive check; the manuscript increasingly distinguishes these correctly.

The two-player relative-objective mirroring argument is valid for an exchangeable continuation starting in an unlabelled symmetric state. It is not defeated by rock–paper–scissors or by allowing mixed actions. Label-dependent continuations and role-differentiated punishers with at least three actors can escape the bound, and the manuscript now states both. A fresh review should not recycle those already-addressed objections as new findings.

#### Scissors arms and their limitations

Within the one-channel fixed-ratio model, increasing ω raises the linearized gap multiplier. The time-to-threshold formula is a local extrapolation, not a global hitting-time theorem; the text now acknowledges that diffusion can prevent the decisive gap from being reached.

The objective arm is algebraically correct when a deviation lowers the mean, raises the actor relative to it, punishment is a lower symmetric profile, and D−C does not fall as the objective narrows. Those premises supply the monotone changes of temptation and sanction. The sanction and stakes arms are also correct partial comparative statics. They do not prove co-movement in a complete strategic system.

Registering co-movement as C0 and presenting the joint calculations as reduced numerical models are appropriate. The outstanding issues are the exactness of the strategic-price interface, the time compression in F2, and the generalization of the fixed-ratio pivot in F-C1—not the mere absence of a universal whole-world scissors theorem, which the manuscript no longer claims.

#### Survival and communication

The conditional-hazard lemma does not require independence between rounds when the stated bounds hold on every surviving history. Under uniformly vanishing contestable coverage and a positive residual floor, the survival bound follows; hazardous-variety growth is not needed in that proof. The manuscript now identifies it as motivation rather than an unused theorem premise. Objections that merely remove the residual floor or assume AI restores coverage change an explicit premise and are applicability tests, not theorem counterexamples.

The shared-self-model cheap-talk ideal-point difference re-derives to b₀(n−1−θ)/(n−1+θ) when the common curvature is negative. The n≥3 relative endpoint yields b₀n/(n−2); the two-player endpoint is degenerate and must be treated separately, as it is. Under zero material bias, informative communication need not disappear among three or more actors, and the supplement already recognizes this.

### Numerical and proof workflow recommendations

1. Keep the current 188 checks, but stop treating their count as certification of theorem scope. In particular, approximate matching within 2.5% cannot certify an exact strategic-price theorem.
2. Separate deterministic share dynamics, conditional drift of a lottery, and the lottery's value function into distinct result and test names.
3. Add exact boundary tests: θ₀=−1, δ=0 when permitted, destruction versus rest, and a payoff-monotone rule with integrable actual selection strength.
4. Add a timing-aware stochastic enforcement example in which actual stopping times—not only the escape event—enter discounted streams.
5. Preserve rejected-objection records: global concentration is not implied by Γ>1; global real-world scissors closure is C0; diffusion is not a universal cap rescue; the residual-risk floor is a premise; an absorbing winner can value cooperation more than victory; stochastic punishment must be credible.
6. Reconcile the proof/status tables after the mathematical fixes. At present, `CLAIMS.md` and S13 call some forms proved while the supplement's numerical discussion openly reports their failure to match. The candid numerical discussion should be retained; the theorem should be narrowed to meet it.

### Disposition of the earlier review issues within this audit's scope

| Earlier issue | V6.2 disposition from this independent audit |
|---|---|
| The standing-price formula was used outside its convergence domain | **Substantially fixed for the deterministic model.** Γδ<1 is in the statement, unstable-but-discounted cases are correctly admitted, and the cusp beyond the domain replaces the meaningless negative resolvent. The new strategic/lottery extension is **not closed**, for F1's separate reason. |
| Faster correction/decay was claimed to lower every loop gain | **Fixed in the formal result.** Proposition S2.4 gives the correct elasticity thresholds, and the main channel discussion distinguishes capacity depreciation from rule-support correction. F-C1 concerns a later unqualified pivot sentence, not the validity of that repair. |
| Test Γ confused raw intensity with the price-induced change in objectives | **Improved and conditionally coherent.** `TESTS.md:132` now proposes the ratio of response to shared harm and private cost, which is 1+θ in the maintained fixed-θ contest. Provision/diffusion predictions follow through the fixed-prize ratio-capacity model. The test still needs the manuscript's identification controls: perceived harm, held objectives, contest parameters, and strategic responses cannot be allowed to vary unmeasured. Under an endogenous prize, the common return must also be estimated or held fixed; Proposition 3.9 establishes a comparison of two returns, not an unconditional empirical provision effect in every growth model. |
| The cap claim failed at equality, and diffusion was omitted | **Fixed in the stated fixed-opponent model.** Equality has its own correct local threshold; diffusion is restored; local and every-start return are separated; conditions keeping the leaders at the cap and the limits of diffusion alone are stated. |
| A relative-objective punishment theorem ignored asymmetric roles or stochastic continuations | **Fixed for the printed exchangeable class.** The state/exchangeability condition, labelled-continuation counterexample, n≥3 role distinction, and strictness perturbations are all relevant. Do not reopen the objection merely because asymmetric punishment exists. |
| Punishment was treated as the no-breakout stage payoff | **Fixed in Proposition 5.4(5).** The recursive punishment value accounts for exclusive and independent breakout lotteries and states credibility limits. The delayed-breakout timing problem in F2 is distinct from this successful repair. |
| The scissors was presented as a unified real-world theorem | **Largely fixed in status.** Separate arms are proved under separate premises; real-world conjunction is C0; the two joint runs are reduced numerical models. F1/F2 identify two exact-interface claims still requiring repair. |

Passing the existing checks is compatible with these positive dispositions and the new findings simultaneously: the successful repairs deserve to remain, while the expanded claims need the same discipline of model and domain matching.

### Reproduction

From the V6.2 directory:

```sh
python3 reviews/formal-audit/independent_audit.py > reviews/formal-audit/results.json
```

The output includes the exact lottery counterexample, the slow-breakout deterrence reversal, the payoff-monotone host counterexample, the relative-objective endpoint, the frontier/rest comparison, the trait/background covariance, the level-channel scaling example, and independent Bellman calculations at three grid resolutions. Six assertions guard the central numerical directions. Bellman convergence on a grid is numerical evidence, not a proof of existence of a smooth continuous-state equilibrium; the analytic lottery example and Bellman derivative identity establish the underlying model distinction independently of that existence question.

The most economical revision preserves the deterministic backbone, limits the strategic-price theorem, restores discounted timing at the enforcement interface, and applies the stated small repairs. It does not require discarding the theory's central account of relative selection or its newly corrected channel-specific levers.

## Systems and alignment review

**Reviewed 4 October 2026.** Scope: THEORY §§4, 6, 9, 10, 11; SUPPLEMENT S4, S6, S9–S11, S13; the corresponding CLAIMS/TESTS entries; relevant boundary cases in S14 and numerical implementations. Reviewer: an independent Codex subagent assigned to the systems/alignment track. No manuscript edits or commits were made.

### Assessment

The revision materially improves the mathematics-to-argument boundary. The separation of sufficiency from necessity in the correction-rate law, the explicit capacity-tracking hypothesis, the corrected delegation game, the two-clock condition for silent crossing, the retained-host transient calculation, and the separation of institutional independence from independent errors are all substantive improvements. Several of the manuscript's strongest claims now have recognizable, checkable mathematical content.

The principal remaining problems in this track are **transfers from a valid local calculation to a stronger operational conclusion**. A failure of behavioral detection is made to imply failure of removal and the hypotheses of a survival theorem. A simple-versus-simple sequential test is made to implement a threshold decision with uniform error guarantees. A sufficient multitype participation basin is treated as the tipping boundary. A constant-liability calculation is stated as an iff criterion without fixing the liability path. These problems survive a passing numerical suite because the suite exercises narrower cases than the prose claims.

There are nine findings below: two P1, six P2, one P3. P1 means that a central recommendation or operational guarantee is stronger than its support; P2 means an incorrect result, empirical discriminator or scope statement needing repair; P3 is a boundary qualification. None is an argument to discard the entire framework.

### Findings at a glance

| ID | Priority | Confidence | Finding | Main stable key / location |
|---|---|---|---|---|
| SA-01 | P1 | High | Masked detection does not establish impossibility of removal or the residual-risk floor | `masked`, THEORY 635–637; SUPPLEMENT 625–629 |
| SA-02 | P1 | High | Readiness's SPRT guarantee applies to its registered endpoint hypotheses, not every state above/below a policy threshold | `readrule`, `readiness`, SUPPLEMENT 1051–1057; THEORY 1096–1098 |
| SA-03 | P2 | High | The minimum type threshold is a sufficient participation basin, not a scalar tipping boundary | `unravel`, SUPPLEMENT 879–883 |
| SA-04 | P2 | High | Test B mistakes an absolute cost for a relative disadvantage | `noinside`, TESTS 121; SUPPLEMENT 320, 334–336 |
| SA-05 | P2 | High | The host's scalar iff margin needs a constant effective-liability hypothesis | `safeguards`, THEORY 982–983; SUPPLEMENT 953 |
| SA-06 | P2 | High | Weak sanctions preserve safe variants but need not remove unsafe variants; zero tax is neutral | `nested`, `masked`, THEORY 627–639 |
| SA-07 | P2 | High | Oversight products require independence across layers or conditional link reliabilities | `topology`, THEORY 651; SUPPLEMENT 655 |
| SA-08 | P2 | High | The conclusion's universal basin claim outruns the expressly conjectural whole-system result | THEORY 1225 versus 1013; SUPPLEMENT 1081, 1094 |
| SA-09 | P3 | High | The core-pruning stability result omits its strict/nondegenerate boundary condition | `certificate`, THEORY 400–402 |

### SA-01 — Keep detection failure, removal failure, and residual risk distinct

**Priority P1; high confidence.**

**Locations.** [THEORY.md:635](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:635), continuing at line 637; [SUPPLEMENT.md:625](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:625), especially lines 627–629. Stable key `masked`. Propagation: THEORY 920 and 1090; TESTS 26, 74, 99–100; CLAIMS 126, 193, 206. Relevant limiting statements: THEORY 506, 514–518, 647; SUPPLEMENT 510, 1129.

**What is proved.** Given a safe variant costing `c_k` and an unsafe variant detected with probability `p_det`, sanctions change their payoff difference by `p_det F - c_k`. If this is negative, sanctions based on that detector do not protect the safe variant against its matched unsafe variant. The manuscript proves this correctly.

**What is added without proof.** The text then says that no developer can buy removal it cannot verify, that beyond the capability of a shown-safe control protocol nothing admission can see reduces the uncovered share, and that Theorem 5.13 applies. None follows from the payoff difference:

1. A detector can fail while an intervention removes or reduces a divergence. Inability to confirm removal using a given detector is an epistemic limitation, not proof that no removal intervention exists. An architecture restriction, a monitored training intervention or a resource/permission restriction can be evaluated through evidence other than the hidden behavior. Even when removal is uncertain, an intervention can improve its probability without providing a proof of absence.
2. `p_det` is a detection probability. It is not the probability of an irreversible event after all correction. No equation in `masked` connects these quantities.
3. A limit on currently demonstrated control is a limit on the established safety case. It is not a lower bound on actual residual hazard. Theorem 5.13 additionally needs `(residual floor)`, explicitly described elsewhere as an empirical crux that a safety architecture could refute. It also needs `(coverage lags)` in its specified uniform sense; incomplete coverage alone is insufficient.

**Concrete mathematical counterexample to the survival inference.** Let every deployed divergence be completely masked under the evaluation, `p_det,t = 0`, and let its realized irreversible-event hazard after an independent intervention be `h_t = 2^(-t-2)` for `t ≥ 0`. The detector and sanction result still fails maximally, but `Σ h_t = 1/2`, so survival has a positive infinite-horizon lower bound by the manuscript's own Lemma 5.11. One can even take the contestable uncovered share to be one throughout: in that case `(residual floor)` is false, and that is precisely why the survival theorem cannot be invoked. This counterexample is not a claim that such an intervention is available now; it shows which additional premise the inference needs.

**Consequence.** The new alignment route into E2/E3 is presented with more mathematical force than the model supplies. The scope language of §5.3 and §6.5 handles this distinction well; Remark 6.8 reintroduces the inference they carefully reject.

**Minimal repair.** Replace the removal impossibility with “these tests cannot establish that the developer has removed the divergence.” Replace the claim that nothing can reduce coverage beyond shown-safe control with a statement about the absence of an established assurance case. Invoke Theorem 5.13 only with its named premises, particularly a justified residual-risk floor for that masked class. Keep E2/E3 as a recommendation under the protection standard where assurance is absent; distinguish that recommendation from a theorem that continued deployment necessarily loses survival. Add an explicit masking-to-coverage/risk interface to S13, separate from the existing masking-to-reports interface.

### SA-02 — A two-point SPRT does not give the claimed threshold-wide readiness guarantee

**Priority P1; high confidence.**

**Locations.** [SUPPLEMENT.md:1051](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:1051), proof at 1053 and application at 1057; [THEORY.md:1096](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:1096)–1098. Stable keys `readrule`, `readiness`. TESTS 154 adopts the rule. Existing implementation: [checks_v62.py:4504](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/checks_v62.py:4504)–4523.

**What is correct.** The likelihood-ratio boundaries and conservative error bounds are valid for the two registered simple hypotheses under the stated independent-observation likelihood model. The union bound across seven dimensions is valid without cross-dimension independence. The computation at Gaussian means zero and one reproduces this result. The conjunction calculation `0.95^7` is also correct under its explicit independence premise.

**Missing step.** Definition 11.2 defines “met” by being past a threshold for a residence time. S11.3 tests a registered value below that threshold against another above it. Its endpoint error bounds do not apply to every value between those two hypotheses. No indifference region or rule for it is defined. Consequently the claim that a ready state is held back with at most the registered probability is not supported for a state just beyond the actual threshold.

**Independent check.** Use exactly the manuscript's Gaussian likelihood ratio, `H0: μ=0`, `H1: μ=1`, noise `σ=1`, `α=.01`, `β=.05/7`, and define the policy threshold at `.5`. In 20,000 independent runs per mean, seed 17:

| True mean | Relation to policy threshold | Probability declared met |
|---|---|---:|
| 0 | Registered null | 0.00555 |
| .49 | Not met | 0.49395 |
| .51 | Met | 0.54665 |
| 1 | Registered alternative | 0.99595 |

The asserted endpoint bounds are about `.01007` and `.007215`. A state barely below the threshold is falsely released about half the time; a state barely above it is held back about 45% of the time. Neither numerical sampling uncertainty nor changing the noise explains this discrepancy. The implementation checks only the two endpoints, where the theorem works.

**Additional operational gap.** The iid fixed-parameter test does not establish that a time-varying state remained above a threshold for a residence time. Deferring the stopping date until the residence interval has elapsed is not itself a test of sustained compliance throughout the interval. Reopening dimensions repeatedly also requires stating whether the error budget is per episode or across the lifetime of the arrangement. These are implementation gaps, not claims that sequential testing is unusable.

**Consequence.** This is the rule that would release a pause, and the paper uses its claimed control of false holds to limit participation erosion. The guarantee presently protects a narrower statistical decision than the policy decision.

**Minimal repair.** Define an explicit indifference band `[q0,q1]` and state which policy action applies inside it, or formulate a one-sided sequential test with guarantees uniform over the unsafe parameter set and a stated alternative separated by a margin. Distinguish “not yet certified” from “proved unmet”; uniform low false-release and low false-hold probabilities with guaranteed finite stopping cannot simply be demanded arbitrarily close to a sharp threshold. Add the sampling, stationarity and residence assumptions, and state the error-budget horizon. Preserve the valid endpoint result as an example, not as the completed readiness rule.

### SA-03 — Multitype participation has a multidimensional basin

**Priority P2; high confidence.**

**Locations.** [SUPPLEMENT.md:879](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:879)–883, stable key `unravel`; [THEORY.md:933](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:933); CLAIMS 154. Existing check: [checks_v62.py:4662](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/checks_v62.py:4662)–4697.

The proof correctly establishes that `x < min_k x†_k` makes every type's outside share decrease, so this is a sufficient basin returning to participation, subject to an inside seed in each type. It does not establish the next claim: crossing that aggregate minimum makes the first type's departure push the system toward the next threshold. Types still below their own thresholds can return faster than the first type leaves, reducing aggregate `x` and reversing the first type's incentive.

**Counterexample inside the stated dynamics.** Use two types with fixed masses `(0.1,0.9)`, `c1=c2=.3`, `s1(x)=.48(1-x)`, `s2(x)=.6-.4x`. The tipping shares are `.375` and `.75`, the same sanction functions as the manuscript's examples. Start at type-specific outside shares `(.5,.4)`, so aggregate `x=.41 > .375`. Under the proof's dynamics:

`ẋ1 = .5·.5·(.3-.48·.59) = .0042`,

`ẋ2 = .4·.6·(.3-(.6-.4·.41)) = -.03264`,

`ẋ = .1 ẋ1 + .9 ẋ2 = -.028956`.

RK4 integrations at steps `.02` and `.01` cross back below `.375` by approximately `t=1.17` and return to essentially full participation by `t=500` (aggregate outside share `3.62×10^-40`). Thus aggregate coverage below the proposed `1-.375=.625` threshold is compatible with full recovery: the initial coverage is `.59`.

The suite samples 800 states only **below** the minimum and puts its two above-minimum examples' outside mass almost entirely in the first type. Those examples are valid but do not test the claimed general boundary. Different distributions across types at the same aggregate coverage can have different outcomes.

**Minimal repair.** Call `1-min x†_k` a conservative sufficient coverage level, not the arrangement's tipping threshold. State cascades conditionally on departures keeping aggregate `x` above the current type's threshold and reaching the next. If an actual multitype tipping boundary is wanted, compute the separatrix in the vector of type shares or give additional conditions that make the scalar reduction valid. Record fixed type masses and positive initial participation explicitly.

### SA-04 — Test B does not discriminate the proposed mechanism as written

**Priority P2; high confidence.**

**Locations.** [TESTS.md:121](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/TESTS.md:121); [SUPPLEMENT.md:320](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:320), 334–336; [THEORY.md:429](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:429). Relevant key `noinside`.

Test B predicts opposition to correction keyed to no one **even where it burdens rivals more**, and treats support at a net cost to the carrier as refuting the mechanism. Proposition 4.4 proves a different comparison: among otherwise identical carriers facing the same externally changed correction, the carrier paying more of the contribution cost loses. A choice about a policy that changes everyone's rents is not a matched-carrier contribution comparison.

**Counterexample.** For two carriers with the paper's relative objective `J_i=π_i-π_j`, a uniform rise in correction lowers own rent by 1 and the rival's by 2. The actor incurs an absolute cost yet gains 1 in its objective. This can arise directly from rule rents `R_i/d`: take `(R_i,R_j)=(2,4)` and increase the same `d` from 1 to 2, with no rule keyed to the supporting carrier. The correction changes rents from `(2,4)` to `(1,2)` and improves the supporter's relative position. The actor can therefore support precisely the observation that Test B calls a refutation.

This does not challenge free riding on independently funded correction. It challenges treating absolute-cost support for a universally applied policy as evidence against relative incentives. Proposition 4.4(5) already admits gains from correction applied to everyone under another route.

**Consequence.** A central registered rival-theory discriminator can classify evidence predicted by the paper's own relative-objective model as a refutation. Conversely, support could be dismissed under entry-barrier theory even when it is fully consistent with the paper.

**Minimal repair.** Measure the supporter's **relative** net effect, including rivals' costs, its remaining rents, host benefits and any benefit mediated through customers or liability. Predict opposition only where the policy reduces the relevant relative objective after these effects, or use the narrower matched-carrier contribution experiment. Retain the appropriability contrast, but do not infer distinct predictions from whether a rule is formally keyed to a carrier alone.

### SA-05 — The sufficient-safeguard margin is exact only for a fixed liability path

**Priority P2; high confidence.**

**Locations.** [THEORY.md:982](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:982)–983; [SUPPLEMENT.md:953](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:953). Key `safeguards`; relevant interface SUPPLEMENT 1117.

The proof tilts the initial distribution by `exp(-s Δ e t)`, which assumes a constant effective margin `Δ`. Yet the theorem defines `Δ=τ_eff-ν` in a setting where `τ_eff=τ(1-x_rule)` changes as capture unwinds. The scalar iff statement neither fixes `Δ` thereafter nor says that it is a constant design parameter. In the dynamic case the exact tilt is

`exp[-s e ∫_0^t (τ_eff(u)-ν)du]`.

The entire cumulative path enters the host trajectory. A constant lower bound above the computed threshold is sufficient by comparison; it is not necessary for every varying path.

**Independent check.** Use the manuscript's forgiving-host parameters `ρ=.05`, `hV=.08`, `V0=1`, `e_min=0`, `e_max=1`, race share `.99`, and floor `.3`. Both paths start with margin `.08`:

| Effective margin path | Minimum host level |
|---|---:|
| `Δ(t)=.08` | .139732 |
| `Δ(t)=.08+.92(1-exp(-t))` | .701216 |

The first crosses the floor; the second remains well above it. Both step sizes `.02` and `.01` agree to better than `6×10^-8` in the minimum. Thus neither the initial margin nor its global minimum decides the iff criterion. A rising margin is particularly relevant here because independent correction restores effective liability over time.

**Minimal repair.** State the exact theorem for a constant effective margin imposed at the stated initial state. Add a corollary that a time-varying margin bounded below by that constant is sufficient. If a parametric liability schedule is wanted, define the schedule first and compute the threshold in its scalar parameter. Preserve the current host calculations; they are useful constant-control viability boundaries, as the manuscript already says they are not the full correctable kernel.

### SA-06 — Weak deterrence is not exclusion; a zero tax is not spread

**Priority P2; high confidence.**

**Locations.** [THEORY.md:627](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:627), lines 631 and 639; [SUPPLEMENT.md:612](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:612), 625. Keys `nested`, `masked`; compare the correctly worded Lemma 3.3(3), THEORY 219.

The core says a sanction “at least” the gain from evasion keeps the divergence out. The proof only says evasion does not grow, and explicitly reserves selection-out for strict inequality. At `c=.3` and `p_det F=.3`, safe and unsafe variants have equal payoffs. Under replicator dynamics their starting shares remain unchanged; an unsafe share of one half remains one half forever. Weak deterrence may sustain a fully safe initial configuration without new entry, but does not establish elimination from a mixed field, robust exclusion under mutation or unique compliance among indifferent strategic actors.

The same distinction is lost at THEORY 639, where a tax of “zero or below” is said to spread a safeguard. THEORY 629 and SUPPLEMENT 618 correctly state that a zero tax is neutral.

**Minimal repair.** Use “protects compliance from being selected against” for `≥`, and “selects evasion out” only for a uniformly strict margin or an explicitly divergent cumulative selective disadvantage, with a safe variant present. For actual admission exclusion, state the separate blocking mechanism. Change “zero or below spreads” to “negative spreads; zero is neutral.” This is a wording repair grounded in a distinction the paper already proves correctly.

### SA-07 — The oversight formulas need a cross-layer dependence assumption

**Priority P2; high confidence.**

**Locations.** [THEORY.md:651](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:651); [SUPPLEMENT.md:655](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:655)–657. Key `topology`.

A check at each of `k` layers catching with marginal probability `p_l` does not imply serial success `p_l^k`. The proposition explicitly assumes independence of duplicate checks, but does not impose independence of layers or define `p_l` as a conditional success probability given the preceding links' success. The same issue affects multiplying layer-level redundant success probabilities.

For six layers, each with marginal catch probability `.9`, independent successes give `.531441`. Perfectly correlated successes give `.9`; disjoint failure events of mass `.1` each give `.4`. All have the stated marginal reliability. No separately stipulated all-defeating common-cause variable is needed for the discrepancy. The exact general bounds are the Fréchet bounds `max(0,k p_l-(k-1)) ≤ P(all succeed) ≤ p_l`, before additional dependence structure is assumed.

The common-blind-spot ceiling is sound and valuable. It does not by itself establish the independence needed for the preceding product formulas or the budget-efficiency ranking.

**Minimal repair.** Add conditional independence across layers, or define each link reliability conditionally so the product follows from the chain rule. Describe the numerical topology comparison as an independent-link benchmark. State that realistic comparisons require the joint failure structure, not only each check's marginal accuracy and one common-cause probability.

### SA-08 — The conclusion should preserve the declared status of the generative basin

**Priority P2; high confidence.**

**Locations.** [THEORY.md:1225](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:1225), against [THEORY.md:1013](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:1013), THEORY 833, [SUPPLEMENT.md:1081](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:1081), and 1094. Related keys `profile`, `capturebasin`, `reachable`.

“Any arrangement with these marks, whatever it is called, changes the basin” is universal dynamical language. The seven marks describe mechanisms and intended effects, and each has support within particular models. The manuscript expressly says that whole-level attraction is conjectural, no result shows the transition requirements can be met together, and the multi-domain viable capture basin with the host is not computed. A design checklist does not supply the missing joint dynamics or a reachable viable basin.

This is not an objection that the paper must solve the whole institutional transition before making recommendations. The careful qualifications are already present. Also, changing a basin is a weaker claim than proving a reachable, durable generative attractor: missing reachability alone would not refute the sentence. The precise defect is that the joint dynamics and the basin allegedly changed have not been identified, so the unconditional system-wide assertion is stronger than the available row-by-row directional results.

**Minimal repair.** Say that arrangements with the marks are intended to change the selection dynamics in the generative direction, and that their viable basin, reachability and durability still have to be established. Keep “Change the basin, then add speed” as the clearly attributed authorial maxim; distinguish it from what the assembled models prove.

### SA-09 — Core pruning needs a strictness convention at gain one

**Priority P3; high confidence.**

**Locations.** [THEORY.md:400](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:400)–402; [SUPPLEMENT.md:399](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:399). Key `certificate`; Table 9.1 R3b at THEORY 909.

The core removes domains whose inbound gain is **below** one. Proposition 4.10(4) then says a nonempty core's configuration is stable. Hyperbolicity is stated for part (1), not for part (4).

Take one domain with `a=b=c=d=ε=ζ=1`, so `G=1`. It is never pruned, but captured state `(x,z)=(1,1)` is not stable. From arbitrarily nearby states `x=z=1-δ`, `z≤1`, so the share cannot increase; any positive interior limiting share would have `z=x<1` and strictly negative share drift, a contradiction. The trajectory tends to `(0,0)`. An independent integration from `(.99,.99)` confirms this. Thus a nonempty threshold-one core need not be stable.

**Minimal repair.** State the nondegeneracy assumption excluding gain-one subset sums for the pruning theorem, or define/prune a strictly sustaining core and analyze equality cases separately. In “every initial state” language also retain the share-below-one restriction: exact boundary `x=1` is invariant under replicator dynamics even when the gain is below one.

### Results re-derived without finding a substantive error

The following checks support retaining the corresponding mechanisms. They are mathematical checks within their stated models, not empirical validation.

#### Correction, influence and field dynamics

- Integrating carrier-keyed support over a fixed horizon gives `z_i*=χ q Σ_j b̂_ij y_j/d_i` and the horizon factor `L_i=1-(1-exp(-ε_i d_i T_h))/(ε_i d_i T_h)`. Weighting by own decisions gives the quadratic `p²` term. The threshold `p*=(f/(χ ȳᵀMȳ))^(1/(2-ξ_f))` follows from the marginal condition at zero.
- With no floor, optimizing `χ q Ŷ/d - γ p^ξ_v q^(1+η)/(1+η)` gives `q*=(χ Ŷ/(d γ p^ξ_v))^(1/η)`. Substitution into the evaluation row sum gives a cultivated term proportional to `γ^(-1/η) d^(-(1+η)/η)`. Its growth exponent is `[α_ctl-(1+η)α_cor]/η`; the correction threshold follows.
- The sufficient rate law needs only the envelope on capacity stated in the paper. The necessary half correctly requires tracking; gradually selected capacity with bounded integrated forcing is an important, explicitly registered counterexample to unconditional necessity.
- Replacing `d` by `d_eff=d exp(-w δ_h t)` gives the shift `w δ_h`. This is a valid result for the specified production form. Its empirical elasticity and the effect of AI assistance remain open, as S13 correctly records.
- With `q*∝p^((2-ξ_v)/η)`, cultivated conversion scales as `p q*`, yielding the stated high moment and splitting factor. The size elasticities matter; the revision no longer overstates a universal cubic law.
- At a binary field configuration, share-direction eigenvalues have the signs stated in Proposition 4.10(1); full-row gain below one gives global asymptotic removal for shares initially below one. The strict row certificate is sufficient, not necessary, as the manuscript states.
- The affine masking threshold and the two-clock silent-crossing condition are correctly separated. Capture in the limit is insufficient to show silence before the first host crossing, and the revision now makes this explicit.
- For one-domain insulation, `z̃(t)=G exp(-εdt)` and `u(t)=u0+ζc[G(1-exp(-εdt))/(εd)-t]`. These give the initial increase in capture, the return-of-share equation and the depth lower bound. The recruitable-lineage result is a genuine conditional mechanism; protecting a nonrecruiting alternative is correctly distinguished from bounding the competing lineage's depth.

#### Delegation and alignment

- In the faithful-instrument game the private gain from racing is `ε(b-h_d)-c`; adding the others' mean payoff produces the stated `θ*`. A faithful instrument need not fix the principals' game.
- In the speed game the winning-probability gain is monotone in speed, with the stated limits for zero or positive numbers of other delegators. Shared control-loss cost is independent of speed under the model. Universal adoption leaves rank probability unchanged and worsens shared survival.
- The full survival-ratio form of Proposition 6.4 supports the certain-lock dominance result when survival without delegation is positive. The correction restricting strategic complements to `p=1` matters and is properly retained. The model is static, and the text correctly declines to infer a dynamic elimination theorem from it.
- Capacity erosion and recovery times follow directly from their exponential ODEs. Whether losing the capacity to execute every delegated task implies losing effective authority is an interface governed by the O2 operational test, not the ODE alone; the manuscript's practical override discussion helps here.
- The matched-variant alignment-tax result is correct under its premise, and does not eliminate unmatched developers with offsetting advantages. The revision's examples and scope reflect this. The remaining issue is the weak-versus-strict sanction language, not the matched-variant mechanism.
- The opaque-corrector summability statement and its revised numerical example are correct. The manuscript properly separates residual safety from the normative status of legibility. This distinction should also govern Remark 6.8.

#### Generative alternative and transition

- The common-frontier public-good calculation yields the stated private and joint first-order conditions for interior solutions. The underprovision of chosen common effort is now explicitly acknowledged.
- The two sharing conventions give different effective prizes, and the revision correctly withdraws the old positive-positional-prize claim under unrestricted “others only” sharing. Neutrality at complete pooling needs the already noted care with zero relative differences.
- The constant-margin host comparison is valid and the independent calculation reproduces its minimum. It is useful as a boundary for that fixed control, although it is not the full viable kernel and does not determine general time-varying controls.
- The signalling model's mixed-equilibrium correction is sound on its stated support: when prior trust is insufficient, the receiver's restraint after the costly step is bounded by `c_R/Π_R`; the candidate attaining the bound requires the stated survival-type incentive condition. The paper correctly limits its zero-cost-imitation conclusion to this signal game.
- A hazard-free pause that shifts only the calendar preserves survival over the same active rounds. The distinction between buying calendar time and changing the hazard process is clear and useful.

### Disposition of earlier review corrections in this track

| Earlier issue | Current disposition | Evidence and remaining qualification |
|---|---|---|
| A falling positive cost floor could invalidate an unconditional correction-rate necessity | **Corrected** | THEORY 365 and SUPPLEMENT 350 distinguish the three relative-growth cases; SUPPLEMENT 358 and S14 1197–1199 include a floor that ends cultivation below the no-floor rate law and a long dangerous transient. The no-floor necessity is now explicitly conditional. |
| Equal incidence was treated as necessary for keeping a common constraint | **Corrected** | THEORY 219 and 627; SUPPLEMENT 612, 859–860 separate within-type sanctions from among-complier neutrality. The across-type counterexample is retained. SA-06 concerns a remaining weak-versus-strict boundary wording problem, not a reopening of the incidence correction. |
| The delegation equilibrium classification omitted `p=1` | **Corrected** | THEORY 605 and SUPPLEMENT 580–584 impose `p=1` on the complementary-delegation result and give the `p<1` example with only an intermediate number of delegators. |
| Full-row certification was treated as necessary for absence of capture | **Corrected** | THEORY 404 and 655; SUPPLEMENT 399; S14 1204 explicitly identify sufficiency and give a row-sum-two low-seed counterexample. SA-09 is a distinct equality case in the maximal-core stability statement. |
| Test M blurred a successful remedy with refutation of the capture mechanism | **Corrected in the registered interpretation** | TESTS 131 now distinguishes present institutions working, the proposed mandates working, and the mandates failing their stress test; it sends mechanism discrimination to Test B rather than treating remedy success as mechanism failure. Actual row-gain identification and causal evaluation remain research work. SA-04 identifies a separate problem in that delegated Test B discriminator. |
| A fixed opaque-corrector blocking rate was called a summable-risk example | **Corrected** | SUPPLEMENT 645–651 states the exact summability conditions, replaces the example and explicitly withdraws the old claim. |
| Long-run recovery was substituted for transient host viability | **Substantially corrected** | THEORY 983 and SUPPLEMENT 953–961 introduce an explicit fixed-control transient margin and separate the forgiving and threshold hosts. SA-05 asks that the constant-effective-margin assumption be stated in the theorem, not that these calculations be removed. |
| Capture eventually was treated as capture before evidence | **Corrected** | THEORY 420–427 requires the threshold during the alarm band or the ordering of the two clocks; SUPPLEMENT 411–413 demonstrates both orderings. |

### Open issues correctly disclosed, not new defects

These matters remain substantial research needs, but the reviewed version marks them sufficiently explicitly that they should not be counted as newly discovered errors:

1. No estimated structural loop gain and no calibrated whole-field capture model.
2. Several coupled domains with endogenous capacity, moving carrier shares and strategic responses are not jointly solved.
3. Correction rate, human capacity, contestable coverage, detection and effective sanction are distinct quantities; several mappings are assumed rather than derived.
4. The rate-law necessity applies to tracking capacity, not every gradual-selection mechanism.
5. The four scissors arms are not jointly established empirically; C0 is a real conjecture, not another numerical identity.
6. Correctable kernels, stochastic viability under disturbances and multi-host thresholds are not computed.
7. The generative order's attraction, funding equilibrium, free-rider control and durable coverage are not proved by the mechanism list.
8. The common-frontier calculation fixes pooled effort; it does not solve individually chosen contributions.
9. Masking and evaluation awareness evidence comes from constructed settings; the capability dependence of detection remains C12.
10. The institution-level magnitudes of dwell, human-capacity loss and recovery are conjectural. Numerical time units are not estimates of institutional years.

The next joint model with the greatest payoff for this track would connect endogenous selection of conversion capacity, multiple corrector domains, effective liability and the host while preserving a viable transient. The manuscript identifies much of this agenda already. For readiness, the priority is more concrete: write one full decision protocol for one measurable dimension, including its unsafe set, tolerance band, sampling model, residence requirement and error horizon, then establish its actual guarantee.

### Reproducibility and coverage limits

Independent code: [audit_systems.py](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/systems-audit/audit_systems.py). Output: [results.json](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/systems-audit/results.json).

The script uses only Python's standard library and imports no manuscript functions. It verifies the multitype participation counterexample, the gain-one field boundary, the dependence of host viability on the liability path, the endpoint-versus-threshold readiness discrepancy, and the closed-form relative-payoff and oversight examples. ODE cases use an independent RK4 implementation; the participation and liability cases are repeated at half the time step. The readiness calculation uses the exact Gaussian likelihood ratio and 20,000 runs at each of four means. These checks establish the reported counterexamples, not the universality of a replacement model.

The root reviewer reports that the full default suite passed all 188 assertions in approximately 315 seconds, manuscript input hashes were unchanged, and an isolated build reproduced the artifacts exactly. This review does not claim a separate rerun of that full suite. It inspects relevant implementations to explain why passing checks do not address the counterexamples. It does not independently validate every cited empirical paper, every legacy numerical block or the manuscript's Chinese/corpus fidelity; those are separate review tracks. The new findings concern the current assembled version, with stable keys supplied where available.

## Evidence and governance review

Reviewed 4 October 2026. Reviewer: Codex evidence/governance subagent, independently assigned within the multi-agent review. This is a review artifact only; no manuscript files were changed and no commits were made. References below use the generated V6.2 files as read in this session. Stable identifiers accompany line numbers where available.

### Overall assessment

V6.2 has a substantially more defensible argument than a simple claim that competition inevitably causes catastrophe. Its most important improvements are substantive: C0 now identifies the empirical joining of mechanisms as a conjecture; the evidence table separates declarations from behavior; the proposed institutions are expressly untested; the coercive fallback is compared rather than endorsed; and the manuscript acknowledges that regulated competition can satisfy particular requirements without being renamed. These changes should be preserved.

The remaining weakness is the last mile from conditional mechanisms to decision rules. Several release and activation rules do not actually implement the conditions of the theorems they cite. The qualitative ranking also gains apparent support from a comparison that puts terminal losses on the continuation side and attempted repairs on the design side. Calling the ranking a judgment is appropriate, but does not eliminate the need to compare the same events and horizons.

My judgment is **major revision before presenting the recommendations as an operationally specified protection policy**. The manuscript can already support a serious research programme, explicit reasons to investigate institutional correction, and conditional arguments for preparation. It does not yet support a computed robust ranking, a validated custody activation mechanism, or a release rule based simply on falling residual risk. None of these criticisms requires rejecting the author's values or the basic selection mechanism.

#### Findings at a glance

| ID | Priority | Confidence | Finding |
|---|---|---|---|
| EG1 | P1 | Very high | Falling residual risk is not enough to withdraw E3 or establish C1 favorable; the theorem turns on cumulative hazard/summability. |
| EG2 | P2 | High | Possibility of irreversible loss is treated as failure of a finite-horizon probability tolerance that has not been specified or bounded. |
| EG3 | P2 | High | The reversibility comparison omits matched terminal failure branches for the proposed design. |
| EG4 | P2 | High | Advance commitment removes a decision step, not physical response, installation, execution, or reneging; “only detecting” is unsupported. |
| EG5 | P2 | High | Tier 1(a)'s universal warrant exceeds the demonstrated option-value case, especially for institutional preparation plus binding activation commitment. |
| EG6 | P2 | Very high | E2 has two rationales but the C1 withdrawal rule and the C5/C7 activation rule do not say which takes precedence. |
| EG7 | P2 | Very high | The pacing comparison reverses one hazard inference and overlooks the cited paper's explicit monitoring-lag extension. |
| EG8 | P2 | High | Short public benchmark leads are turned into an unmeasured assertion that no breakout has put an actor beyond punishment. |
| EG9 | P3 | Very high | Several smaller source/operational statements remain stronger than their evidence: BEAD funds, UK remit, and readiness. |
| EG10 | P2 | Very high | Hash commitment does not establish held-out secrecy or prevent training on the committed metrics. |

P1 here means that the issue can change the warranted policy or the stated ranking; P2 changes scope or interpretation; P3 is a narrower correction. Confidence is confidence in the identified mismatch, not confidence in any prediction about future AI.

### EG1 — The C1 release rule substitutes declining risk for sufficiently low cumulative risk

**Location.** THEORY.md:516–520 (Theorem 5.13 / `coverage`, E3); THEORY.md:1166 (E3 trigger); THEORY.md:1200 (C1); TESTS.md:12,84,108,150. Related historical overstatement: DISCUSSION.md:501.

**Priority/confidence.** P1; very high. This is a logical mismatch, not an empirical dispute.

**Finding.** The theorem distinguishes a branch with persistent uncovered hazard from a branch with a summable upper bound. The practical register instead says that residual risk “falling under present incentives” causes E3 and the case for E2 to lapse for the class, with their triggers withdrawn. Declining hazard does not establish that distinction.

An example inside the theorem's own danger premises is U_t/Y_t = 1/(t+2), residual-floor coefficient h = 0.02, and actual conditional loss probability q_t = 0.02 + 0.01/(t+1), for t >= 0. Coverage lags, q_t exceeds h(1-U_t/Y_t), and q_t is strictly falling, yet survival tends to zero. Thus the current verbal withdrawal condition can be met while the theorem's failure premises continue to hold. Even requiring risk to tend to zero does not fix the issue: q_t = 1/[2(t+1)] decreases to zero but has a divergent sum, so log(1-q_t) <= -q_t still forces the survival product to zero. Conversely, an extremely low constant hazard may meet a specified five-year tolerance while failing an infinite-horizon summability criterion. Trend, finite-horizon acceptability, and asymptotic survival are three different propositions.

**Consequence.** The registered rule can withdraw precisely the protection meant to address cumulative exposure while the theorem's long-run failure mechanism remains. It also makes C1 easier to label favorable than the paper's own definition of E3 warrants. The converse activation rule, “residual risk not falling,” can activate on a safe low plateau unless the magnitude and exposure horizon are also specified.

**Repair.** Give C1 at least two separately scored parts:

1. A finite-horizon decision test: an independently estimated upper bound on the cumulative probability of O1/O2 over each protected horizon, including confidence, model uncertainty, and deployment scale, is below a registered tolerance.
2. If the asymptotic theorem is being invoked, a justified tail bound strong enough to establish summability, or an explicit assumption about the future trajectory. A finite sequence of declining observations is not a tail certificate.

“Residual risk falling” can remain an encouraging diagnostic, but should not by itself switch E2/E3 off. Apply the same repair to the claim that Cold War learning supplies a case of summable residual risk (DISCUSSION.md:501): a finite historical survival record and declining estimated hazards do not establish an infinite sum.

**Minimal acceptable revision.** Replace “falling” in the release condition with “bounded below the registered cumulative-risk tolerance at the relevant horizons, with the conditions for any invoked tail claim separately satisfied.” Keep the weaker trend claim as evidence that the case for slowing may weaken.

### EG2 — The protection standard is not instantiated, and its third step is not yet applied

**Location.** THEORY.md:796–812 (§8.1, Definition 8.1 / `kernel`); THEORY.md:1175–1179 (Tier 3); DISCUSSION.md:292,338; CLAIMS.md:21,36,39.

**Priority/confidence.** P2; high. This concerns consistency of the stated decision procedure. Final cross-review lowered the priority because the manuscript explicitly admits that the estimates are absent and labels its ranking a judgment; the defect is the unsupported move to the standard's third step, not concealment of an uncomputed ranking.

**Finding.** The standard compares upper bounds on probabilities of O1/O2 at common finite horizons over Θ, against a stated tolerance. The manuscript then concludes that every path fails that tolerance because every path's worst case includes an irreversible loss. No actual tolerance, bounded parameter set, finite-horizon risk bounds, or joint dependence assumptions are supplied.

The existence of an admissible irreversible event is not the same as a probability bound exceeding a tolerance. A path with a worst-case five-year loss probability of 0.001 contains irreversible-loss outcomes, as does one with probability 0.5. The standard distinguishes them; the verbal comparison does not.

There are two coherent readings, and the manuscript currently moves between them:

- **Probabilistic robust comparison:** Θ contains models with probabilities; use the supremum of the relevant cumulative probability. The bounds must be supplied or left unestimated.
- **Adversarial possibility comparison:** any named, uncontradicted catastrophic mechanism suffices to fail. This can be a normative rule, but if every path admits catastrophe, it often produces a tie. Qualitative preference for repairability is then an additional rule, not a calculation of the lowest probability bound.

The correctable kernel is an all-disturbance guarantee and is an appropriate separate concept. It should not silently turn a probability-based satisficing rule into zero-tolerance worst-outcome reasoning.

**Consequence.** Readers can mistakenly understand the Tier 3 preference as what the protection standard implies, when the text has not established that any path fails its finite-horizon tolerance, let alone identified the smallest upper bound. The manuscript does acknowledge missing estimates; the problem is retaining the preceding unconditional conclusion despite that acknowledgment.

**Repair.** State an explicit schematic decision rule, for example B_j(H) = sup over θ in Θ of Pr_j,θ(O1 or O2 by H), and specify how the multiple horizons and O1/O2 bounds are combined. Publish at least one transparent illustrative Θ and tolerance analysis, keeping it separate from an empirical estimate. Until calibrated bounds exist, say: “No candidate has yet been demonstrated to meet the tolerance; current evidence does not permit the standard to rank their bounds. We provisionally prefer X for the following qualitative, normative reasons.” If reversibility breaks an otherwise unranked tie, add it explicitly to the rule.

### EG3 — The proposed design receives remedies where continuation receives terminal outcomes

**Location.** THEORY.md:1176–1177; DISCUSSION.md:294–334 (failure-mode table), especially 298–304 versus 326–332; DISCUSSION.md:342,393,407–416.

**Priority/confidence.** P2; high. The problem is comparison structure; the paper already admits that the design is untested. Final cross-review lowered the priority to recognize that explicit qualification. Continuation's table also contains some remediable branches; the imbalance is the stage and timing of the compared failures, rather than a complete omission of its possible remedies.

**Finding.** Continuation's table includes capture before evidence, a floor crossed, an admitted masked divergence, and a lost capacity to overrule. The design's table mostly includes a captured function followed by recertification, collusion followed by rotation, service interruption followed by standby, and overreach followed by appeal. It then names only two irreversible design failures: coercive escalation and custody capture.

A shared disclosure registry could be captured or mistaken, causing a hazardous system to be admitted and an irreversible loss before recertification. A standby service could fail to restore essential provision before a catastrophic loss. A masked system could outrun oversight while the custodians remain formally independent. These are the same kinds of late-detection or failed-response branches already admitted for continuation; neither requires capture of decisive custody or a coercive strike. THEORY.md:520 explicitly says the growth hazard persists after racing stops.

Giving the design a planned response does not exclude these branches. Continuation also has planned responses—recall, courts, replacement of regulators, reciprocal limits—before a terminal threshold is crossed. Conversely, after a terminal threshold is crossed, the design's appeal or rotation is no more a reversal of the loss than continuation's is.

**Consequence.** The sentence that every other design failure has a reversal is too strong, even with the qualification that the reversals have not been tested. It supports the central qualitative ranking using a timing asymmetry. The issue is not that proposed designs must already have real-world outcome data; it is that they must face the same fault-to-loss chains.

**Repair.** Use a common event tree for both candidates:

fault -> detected before critical boundary? -> independent remedy available? -> remedy executes before the boundary? -> common-cause failure? -> protected loss avoided?

For each shared hazard, put the two pathways side by side. Separate “a remedy is specified” from “the failure is reversible with probability/bound X before O1/O2.” Add the design's uncovered-hazard, false-negative, covert internal-deployment, service-continuity, and delayed-repair branches to Θ. The defense may then be that the design plausibly lowers particular transition probabilities, not that the terminal branches are absent by design.

**What survives.** The preference for building explicit, independent remedies is a defensible value and engineering principle. It is stronger when described as a hypothesis about the probability of timely recovery rather than an exhaustive classification of irreversible failures.

### EG4 — A registered trigger is not yet a commitment technology, and does not leave only detection delay

**Location.** THEORY.md:749,1157,1165–1169; TESTS.md:142–150; DISCUSSION.md:357–359,393,411,441. The mathematical time-to-decisiveness indicator is TESTS.md:146, citing Remark S2.1 / `tdec`.

**Priority/confidence.** P2; high. Final cross-review treats this as a delay-accounting and implementation-interface defect. X10 explicitly acknowledges unresolved enforcement against the strongest participant; the review does not allege that this uncertainty is concealed.

**Finding.** It is sensible to prepare and agree a trigger before incentives deteriorate. The stronger statement that commitment leaves “only detecting” does not follow. Even a valid automatic decision has to be communicated, executed, and made effective. A plant needs to stop, keys need to be transferred or disabled, a violating actor may withhold access, and an executive or host jurisdiction may refuse. X10 expressly leaves execution against the strongest participant unresolved. A prior agreement cannot remove the enforcement failure merely by calling later activation mechanical.

The policy also mixes **prepared**, **installed**, and **in force**. The trigger subtracts the time to install and verify custody; the commitment paragraph treats building and deciding as already removed. Which physical and legal controls have actually been installed before the trigger fires is not specified.

Finally, the trigger's T_dec indicator is calculated using a constant local gap-growth factor and a finite decisive threshold. The manuscript correctly calls the decisive gap a quantity to measure, but does not show that the extrapolated hitting time is a conservative bound under saturation, strategic response, changing channels, or masking. A local growth estimate is useful for research without yet being an activation estimator.

**Consequence.** The recommendation can activate too late or claim incentive compatibility exactly where its actuator fails. The warning-time rationale for early preparation remains, but it is not a proof that precommitment solves the critical commitment problem.

**Repair.** Define the full response chain and its measured distribution: observation, classification, authorization if any, communication, execution, and time until the restraint actually binds. Mark completed preparation separately from remaining installation. Specify the precommitment instrument—escrow, already-installed controls, legal authority, custody of keys, or another concrete mechanism—and model revocation/bypass as a deviation rather than assuming it away. Use a conservative bound on T_dec across admitted models, including uncertainty in the decisive gap. Put response latency and the chance of failed execution into p_d. Then either prove the resulting enforcement inequality or call the mechanism a candidate to be tested under C4/C7.

**Minimal acceptable wording.** “Precommitment can remove the need for a new discretionary policy decision; detection and verified execution still take time and remain enforceability conditions.”

### EG5 — Tier 1(a) is an option-value argument, not established to pay on every reading

**Location.** THEORY.md:1153–1158; TESTS.md:44–65, especially 55,56,58,60; DISCUSSION.md:342,348,377,393.

**Priority/confidence.** P2; high.

**Finding.** The central issue is whether a binding activation commitment belongs in a tier whose warrant is independent of C4 while the design it would activate is still being compared under C4. Persistent reasons for information, research and preparation can survive every named crux without constituting a mathematical dominance theorem, and the tier is marked as a recommendation. TESTS also permits its contents to change with the evidence. The review therefore does not reject bounded research merely because it has costs. The stronger concern begins when preparation includes durable authority, financing, access rights and a binding commitment to an unresolved institutional design; describing that as forgoing nothing needs a separate argument.

This is clearest for item 4. If C5 establishes no route to a decisive advantage in the relevant range, or C4 indicates that common custody is more fragile than available verification arrangements, some continuing research option may remain sensible. It does not follow that the same level of institutional preparation and the same activation commitment remain warranted. Saying that the whole cost is the cost of preparation records the cost but does not show that it should be paid.

The asymmetry between item 4 and Tier 3 is also substantive: the latter compares whole custody configurations under uncertainty, while the former commits in advance to activating a custody mechanism whose implementation is still under comparison. This is not resolved merely by saying the tiers are simultaneous kinds of justification.

**Consequence.** The “on every reading” label should distinguish a continuing reason to investigate and prepare from an unconditional warrant to establish and bind a particular mechanism. Without that distinction, the recommendation can commit to the implementation before its own stated crux has been resolved.

**Repair.** Divide preparation into bounded research/design/pilot expenditure and the creation or irrevocable delegation of powers. Specify a budget, exit conditions, institutional option costs, and the counterfactual uses of resources. Treat the former as a provisionally justified option under named assumptions about possible warning times; require the latter to pass the same C4 comparison as the design it binds. Narrow the claim from “on every reading” to “robust across the presently plausible readings, within a stated budget and without activating the relevant restrictions.” Binding activation should be conditional on both the hazard trigger and a prior demonstration that the chosen mechanism can meet its own safeguards.

### EG6 — Clarify which E2 rationale survives a favorable C1

**Location.** THEORY.md:1165–1166,1195,1200,1205; TESTS.md:7,12,51,84,91,142–150.

**Priority/confidence.** P2; very high.

**Finding.** The theory gives E2 at least two intelligible rationales: dangerous capability outruns correction, and a decisive capability would defeat enforcement or permanently concentrate authority. Those need not coincide. Tier 2 activates custody and E2 from C5/C7 indicators of approach to decisiveness. C1 separately says that falling residual risk makes E3 and the case for E2 lapse, with their triggers withdrawn. The recommendation gives no precedence rule when these judgments differ.

Consider a class with a satisfactory hazard bound and good contestable control, but which gives one state a durable strategic advantage beyond external sanction. C1 can be favorable while C5/C7 support the strategic rationale for E2. The C1 row withdraws “their triggers”; Tier 2 still activates. Conversely, a hazardous class may warrant a pause or rollback even when strategic advantage is not decisive. The existing definition of E2 as decisive-class stopping does not cleanly name that case.

**Consequence.** Two readers implementing the same registered indicators can make opposite activation decisions. This is an operational ambiguity, not an objection to having multiple rationales.

**Repair.** Register separate hazard/control and strategic-domination triggers, say whether they combine by OR or AND, and specify which protection each favorable crux withdraws. A compact truth table should cover favorable/unfavorable C1, decisive/not-decisive C5, timely/untimely C7, and feasible/infeasible C4. Avoid making a favorable C1 erase a strategic-domination trigger unless that is the intended normative choice. Apply EG1's magnitude/cumulative-risk correction before filling the table.

### EG7 — Correct and deepen the comparison with spontaneous pacing

**Location.** DISCUSSION.md:180,186–191; EVIDENCE.md:197; THEORY.md §8.3(b). Source: [Fudenberg and Koh, *Cooperating against Catastrophe*, full text](https://arxiv.org/html/2609.28291v1), especially §§2.3 and 3.5.

**Priority/confidence.** P2; very high for the directional error and omission, high for the interface critique.

**Finding.** The sentence at DISCUSSION.md:187 has the direction backwards. Lower perceived hazard moves the calculation toward racing; it cannot explain participants computing pacing while true parameters put them in the racing region. A case with sufficiently high true hazard but understated perceived hazard gives the reverse discrepancy.

The full paper also explicitly includes private internal capability and a deployment/monitoring lag. Under its assumptions, sufficiently high effective hazard sustains pacing at every lag. Its effective hazard is a payoff-equivalent mathematical quantity; it is not defined simply as the fraction of harm an actor notices or morally counts. The manuscript transparently says it read the abstract, but then builds several paragraphs of substantive contrast that the full source qualifies. [Primary full text](https://arxiv.org/html/2609.28291v1)

**Consequence.** One of the strongest alternatives is made weaker by the comparison's source coverage, and a proposed cross-model mapping is described too close to a direct application. The conclusion that transparent incentives can produce endogenous restraint remains useful; the contrast should concern which specific assumptions fail, not the mere presence of internal deployment.

**Repair.** Reverse the sentence. Distinguish the source's defined effective hazard from this paper's conjectured transformation under relative accounting. Rework the comparison around the full source's relevant assumptions, including what determines risk, what becomes observable, and what is assumed about survival payoffs. Supply a translation between payoff functions or keep that translation expressly heuristic. Cite the lag extension and explain why a threat before deployment or an absorbing strategic breakout falls outside its scope. Do not claim that monitoring delay alone refutes spontaneous pacing.

### EG8 — The evidence on short leads does not establish the absence of decisive strategic capability

**Location.** THEORY.md:751; EVIDENCE.md:109–117; TESTS.md:17,146; DISCUSSION.md:462.

**Priority/confidence.** P2; high.

**Finding.** EV5's benchmark evidence is appropriately qualified and its limits are largely explicit. The core then says that short leads support enforcement because no breakout has yet put anyone beyond punishment. Public benchmark lag does not measure the existence of a position beyond sanction, let alone establish its absence. The relevant tests omit concealed internal systems, complementary assets, actual response capacity, deployment permissions, and whether even a short capability edge can cross an irreversible threshold. The manuscript itself treats internal deployment and masking as major limitations elsewhere.

The verified [Epoch ECI observation](https://epoch.ai/data-insights/open-closed-eci-gap) concerns public model-capability measurements and a historical average lag. The verified [METR page](https://metr.org/time-horizons/) measures success on specified task suites and warns about its upper-range reliability. Neither is a direct sanctionability measure.

**Consequence.** “Not established” in the evidence row becomes “has not happened” in the policy timing argument. This can give false assurance about the remaining preparation window even while the manuscript argues that observation lags are dangerous.

**Repair.** State that available public measures provide no affirmative demonstration of decisive breakout and are consistent with a remaining window, while its size is unbounded by those data. Add operational indicators of convertibility into strategic control and the time needed for effective balancing, rather than treating benchmark lead duration as a surrogate for T_dec. Keep unmeasured internal capability in the uncertainty range on the same basis as other unmeasured failure modes.

### EG9 — Narrow corrections and implementation caveats

These do not defeat the core argument. They matter because V6.2 otherwise takes care to distinguish what sources actually establish.

| Location | Issue | Concrete repair |
|---|---|---|
| EVIDENCE.md:77, EV3 | EO 14365 §5(a) concerns eligibility for remaining BEAD **non-deployment** funds; the register says “remaining broadband-deployment funds.” Section 5(b) separately orders assessment of discretionary grants. | Use the precise program/fund category and distinguish the directed policy notice from already completed withholding. [Primary order](https://www.govinfo.gov/content/pkg/FR-2025-12-16/html/2025-23092.htm) |
| EVIDENCE.md:76,82; THEORY.md:763 | The UK release establishes a rename, specified remit, a new misuse team, and a separate Sovereign AI partnership. It also expressly presents the work/security focus as continuous. The release alone does not establish a **narrowing** from the prior remit. | Record the new stated focus; compare archived prior remit and actual programme changes before concluding narrowing. Retain the excellent existing qualification that impairment of an entrusted purpose is not shown. [Primary release](https://www.gov.uk/government/news/tackling-ai-security-risks-to-unleash-growth-and-deliver-plan-for-change) |
| DISCUSSION.md:464; TESTS.md:154 | “No dimension is met” is stronger than “none is measured in the required form.” Some dimensions can be unsupported, others contradicted; these are different states. | Use “none has been demonstrated to meet the registered criterion,” then distinguish absence of measurement from affirmative failure for each Q dimension. |
| DISCUSSION.md:256, present-policy table | “No, unless custody follows” for reporting/evaluation conflicts with the explicit detection-and-response route in C7 and Remark 5.5. | State “only if detection and response prevent decisive breakout, or custody does”; do not make custody necessary where the theory presents an alternative. |
| TESTS.md:149; EVIDENCE.md:183–184 | The 2.8× annual cap adjustment is valid arithmetic for the cited benchmark trend, but is not a measured rate for every hazardous or decisive capability. EV9 says this; the operational indicator can read as a universal rule. | Keep it illustrative; estimate an efficiency envelope for each regulated capability and add post-training/inference and algorithmic uncertainty before using it as a binding cap schedule. [Primary paper abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/6b066da6a23bc55f9b887e7298102884-Abstract.html) |
| DISCUSSION.md:490 | The historical record can illustrate difficulty of control after asymmetric advantage; it does not establish the necessity proposition “custody must precede decisiveness.” | Label that column as the theory's interpretation of the precedent, with alternate explanations and the source's historical limitations. |

### EG10 — A hash commits a metric without guaranteeing that it is held out

**Location.** DISCUSSION.md:353,373 (X10, held-out metrics).

**Priority/confidence.** P2; very high. This is a specific implementation error, not a general objection to preregistration.

**Finding.** The design concludes that publishing a hash before evaluation lets everyone verify prior choice and ensures that no one can train on the metric. The two guarantees are distinct. A deterministic hash over a small candidate set can be recovered by hashing every candidate. Even a properly randomized hiding commitment does not hide the material from whoever created or holds it, and publication at the first evaluation exposes it for later reuse. Standard commitment definitions distinguish binding from hiding; a hash-based hiding construction includes fresh random secret material. [Stanford CS355, lecture 3, §§1 and 3](https://crypto.stanford.edu/cs355/23sp/lec3.pdf)

**Consequence.** The same institutional capture channel the paper studies can expose the metric through the standards body's insiders while every published commitment still verifies. The design therefore cannot count this clause as ruling out assessment gaming.

**Repair.** Commit to a salted, high-entropy test package under a specified scheme; protect the nonce and test content until use; separate holders from assessed parties; record access and leaks; and rotate tests after revelation. State the guarantee as verifiable prior commitment plus a separately tested secrecy protocol. None of these mechanisms warrants the unrestricted phrase “no one can train on it.”

### Targeted primary-source audit

This was a substantive sample, not an exhaustive bibliography verification. “Verified” means that the specific recorded proposition was found in the retrieved primary text, not that the proposition proves the theory. “Limited” means that the text supports only a narrower claim, only an abstract was checked, or the source's own methodology was not independently reproduced. “Unverified” is a retrieval/coverage limitation, not a finding that the source is false. All accesses below occurred on 4 October 2026.

| Source / register use | Status and retrieval | Result for the manuscript |
|---|---|---|
| [Anthropic RSP v3.0](https://www.anthropic.com/responsible-scaling-policy/rsp-v3-0), EV2 | Verified; primary PDF text, introduction and policy sections read | The change from unilateral absolute-risk commitments to company plans and industry recommendations is directly supported. This verifies a policy declaration, not a causal estimate of actual racing. |
| [Anthropic RSP history/current page](https://www.anthropic.com/responsible-scaling-policy), EV2 | Verified; primary page | v3.4 dated 8 July 2026 is listed as current; retained discretion to pause and the intervening revisions are supported. The register appropriately distinguishes discretion from obligation. |
| [OpenAI Preparedness Framework v2](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf), EV2 | Verified; primary PDF §4.3 | Competitor-contingent adjustment and all four stated safeguards are accurately represented. The source also includes safeguards during internal development. |
| [Zhu, Silent Revision](https://arxiv.org/abs/2609.08789), EV2 | Limited; primary abstract and metadata | The 710 commitment instances, twelve consecutive version pairs, 77% of traced changes, silence figures, and workshop-review status match. The manuscript now gives the correct denominator. No independent recoding performed. |
| [EvalDetectBench](https://arxiv.org/abs/2609.01611), EV6 | Limited; primary abstract and metadata | The 11.25% measurement-variance point and transfer failure of elicitation prompts match. Its unusual identifier/date combination is reproduced on the retrieved record; do not “correct” it solely from the identifier. |
| [METR time horizons](https://metr.org/time-horizons/), EV5 | Verified; primary methodology/updates page | The above-16-hour warning and task-suite limitation are supported. It is not an operational autonomy-duration or strategic-dominance measure. |
| [Epoch open–closed ECI gap](https://epoch.ai/data-insights/open-closed-eci-gap), EV5 | Verified; primary analysis | The four-month average and eight-point gap on 29 May 2026 match. Downstream inference to sanctionability remains unvalidated (EG8). |
| [Ho et al., Algorithmic progress](https://proceedings.neurips.cc/paper_files/paper/2024/hash/6b066da6a23bc55f9b887e7298102884-Abstract.html), EV9 | Limited; official proceedings abstract | Eight-month halving, 90% interval of approximately 2–22 months, two pre-training benchmarks, 2012–2023, and 200+ evaluations match. Extrapolation to decisive agentic capabilities is not measured by it. |
| [Fudenberg–Koh full text](https://arxiv.org/html/2609.28291v1), EV11 / X8 | Verified relevant sections; not a proof replication | Supports the pacing alternative but requires the substantive comparison correction in EG7. |
| [Anthropic July Public First Action announcement](https://www.anthropic.com/news/donation-public-first-action), EV4 | Verified; primary page | Additional $20m, $40m total, restricted education/policy purpose, and non-election-use statement match. This is the donor's report, not audited recipient accounts. |
| [UK AISI rename announcement](https://www.gov.uk/government/news/tackling-ai-security-risks-to-unleash-growth-and-deliver-plan-for-change), EV3 | Verified facts / limited interpretation; primary page | Date, new name, security remit, and Sovereign AI partnership are supported. “Narrowed remit” requires a before/after comparison (EG9). |
| [EO 14365](https://www.govinfo.gov/content/pkg/FR-2025-12-16/html/2025-23092.htm), EV1/EV3 | Verified; primary legal text | Dominance objective, task force, funding instructions and legislative carve-outs match in substance; repair the non-deployment-funds wording (EG9). This audit does not establish later implementation or litigation outcomes. |
| [White House 25 September 2026 fact sheet](https://www.whitehouse.gov/fact-sheets/2026/09/fact-sheet-president-donald-j-trump-advances-a-fair-and-reciprocal-relationship-with-china-while-hosting-historic-state-visit/), EV8 | Verified; primary page | SI dialogue, next exchange by November, and agreement to establish an incident channel match. The register correctly marks absence of binding development limits as its interpretation. |
| [UN preliminary-report announcement](https://www.un.org/en/node/245172), EV7/EV8 | Unverified in this review; 403 retrieval failure | Do not treat this review as independent verification of the quoted July report, panel membership, or meeting details. Preserve the original register's precise coverage statement. |
| [Business Roundtable 2019 statement](https://www.businessroundtable.org/business-roundtable-redefines-the-purpose-of-a-corporation-to-promote-an-economy-that-serves-all-americans), EV15/X1 | Verified; primary statement | Date, 181 CEOs, stakeholder turn, and the organization's retrospective statement that versions since 1997 endorsed shareholder primacy match. This verifies declared purpose, not compliance. |
| [Truman policy memorandum to Baruch, 7 June 1946](https://history.state.gov/historicaldocuments/frus1946v01/d448), X11 | Verified relevant passages; primary historical record | International control, absence of stockpiles when fully operational, and distinction between dangerous and licensable activities are supported. Custody's success or universal necessity does not follow. |
| [OECD 5 January 2026 package announcement](https://www.oecd.org/en/about/news/press-releases/2025/12/international-community-agrees-way-forward-on-global-minimum-tax-package.html), EV18/X10 | Limited; primary announcement, not full implementing package | Confirms the side-by-side agreement and continued role of domestic minimum top-up taxation. The exemption's exact legal scope remains dependent here on the register's professional source. Interpretation as “coverage unravelling” should acknowledge this alternative-rule structure. |
| [Stanford CS355 commitment-scheme lecture](https://crypto.stanford.edu/cs355/23sp/lec3.pdf), X10 technical check | Verified; university's original lecture notes, definitions and hash construction | Binding and hiding are distinct; the hash construction uses message plus random secret string. This supports EG10's correction but cannot certify the design's operational security. |

#### Sources not independently reverified in this pass

The Colorado litigation docket/order, original Wired memo, original July UN panel report, all military-AI endorsement lists, all author-corpus quotations, the complete AI 2040 plans, the Jones full paper, and most historical books were not independently re-read. The manuscript is often explicit about relying on reports or abstracts; retain those distinctions. No contradiction was inferred merely from an inaccessible source or lack of verification.

### What is strong and should remain

1. **C0 is now in the right logical place.** THEORY.md:693–707 and TESTS.md:11 openly separate within-model comparative statics, unproved interfaces, reduced numerical joint models, and real-world co-movement. That is a meaningful repair. No amount of passing numerical checks alone would have established C0, and the text now says so.
2. **The evidence register has a usable adversarial structure.** EV1 separates domestic and external declarations; EV2 preserves competitor-contingent safeguards and contrary commitments; EV3 says it has not established capture under Definition 4.1; EV4 records rule-making expenditures in both directions; EV5 distinguishes metrics; EV6 distinguishes constructed demonstrations from deployment prevalence.
3. **The author’s failed pilot is disclosed.** EV12 explicitly says there is no experimental support for the §4 mechanism yet and does not convert failed P1 into confirmation. This should not be weakened in the next draft.
4. **Whole designs are not presented as uniquely derived.** The polycentric alternative, regulated competition, verification-plus-provision, benign-winner argument, and the design's own D4/D5 failures are taken seriously. The coercive fallback's move to a compared tier is a significant improvement.
5. **The draft distinguishes normative disputes from algebra.** Protection of O2, the treatment of benefits forgone, and AI standing are declared cruxes. A reader may disagree with them without refuting the conditional mechanisms.
6. **Institutional details have become specific enough to criticize.** The chamber, formula funding, recusal, provider participation, fallback, escrow, and execution bodies expose real design choices. The next step is a feasibility model with timing and correlated failure, rather than more architectural labels.

### C0 and the empirical programme: assessment without overclaiming

C0 is not presently demonstrated; the manuscript admits this. That admission is not a defect. The weaker support actually available is that several recognizable observations are consistent with components of the proposed mechanisms and that the models can be coupled under specified assumptions. The evidence does not yet show a common causal driver, a measured Γ, an observed scissors crossing, or a stable empirical measure of success-to-corrector conversion.

Test E should be treated as a research design to operationalize, not a completed preregistration. It needs a fixed unit of analysis, a parameter intervention whose direct channels are identified, prespecified W/C/N outcomes, a justified observation/dwell window, effect-size and power criteria, and controls for changes that affect multiple outcomes without passing through the proposed common parameter. A disclosure intervention can itself change funding, access, reputation, enforcement and language; it is not automatically a single-signature negative control. The root review separately audits the tests' discriminating claims, so this report does not duplicate its findings.

The most useful near-term empirical sequence would be:

1. Operationalize one corrector-domain certificate on observed data, including unobserved-channel uncertainty, and check it against actual adverse findings against a leader.
2. Run a modest intervention or credible natural experiment whose incidence and timing are known, measuring the behavioral response and the proposed mediator separately.
3. Estimate a class-specific cumulative-risk or coverage model rather than substituting general capability trends for hazardous variety.
4. Conduct adversarial drills of the institutional response chain, with a deliberately noncompliant strongest participant and an injected correlated error.
5. Use those results to construct a bounded Θ and an illustrative, then empirical, comparison of a specific custody mechanism with a strong verification/regulation alternative.

This sequence would make both favorable and unfavorable findings actionable. It would also prevent the architecture from becoming insulated against evidence by moving every adverse result from a mechanism test into a design-revision exception.

### Normative disagreements that are not errors

The protection standard may deliberately give irreversible common catastrophe priority over diffuse deaths caused by benefits forgone. That is an explicit N1 choice, not a mathematical inconsistency. It would still help to define the boundary between O1 and forgone-benefit mortality so two equally large irreversible losses are not classified differently simply because one occurs by omission.

Likewise, excluding providers from formal votes is a contestable institutional tradeoff. X10 openly records the loss of local knowledge and participation incentives and acknowledges that influence can return through voice. That is a candidate policy choice, not something Proposition 4.3 alone proves necessary. The review's recommendation is to test the tradeoff under C4, not to insist on a different constitution.

Preference for broad distribution, non-domination, and human authority can support preparation even before probabilities are precisely estimated. The necessary correction is to call that a provisional practical judgment under stated uncertainty and cost limits, rather than claim that an uninstantiated robust calculation or a theorem has already selected it.

### Reading coverage and limits

Read closely: THEORY §§7 and 8, §12, the front-matter and claim-status passages, relevant §§5.3, 10.5 and 11 passages; DISCUSSION X1's literature/novelty structure and X8, X10, X11; the EVIDENCE register; TESTS' cruxes, tier matrix, tests and operational indicators; CLAIMS' definitions, support/status entries and normative summary. Line-numbered passages underpin every finding above. Supplement references were followed at the level needed for the policy checks, but this agent did not re-prove all mathematics, rerun the numerical suite, or certify the build. Those are separate streams of the multi-agent review.

The principal uncertainty is empirical, and the manuscript already states much of it correctly. The needed revision is concentrated: align C1's decision criteria with cumulative risk; distinguish unestimated from unsafe; compare matched fault-to-loss paths; specify the physical commitment and response chain; and repair the strongest-alternative comparison against the full source. These changes would make the practical argument much harder to dismiss without asking it to claim more evidence than exists.

## Integration and verification review

Reviewed on 4 October 2026. This report covers the argument's status across documents, the empirical test programme, preservation of the author's directions, and what the automated checks establish. It supplements the separate formal, systems and alignment, and evidence and governance reviews. The review does not change the manuscript.

### Main assessment

V6.2 is a substantial improvement in the discipline with which the project distinguishes results, premises, conjectures, numerical examples and values. Its strongest contribution is a connected set of conditional mechanisms and a programme for testing whether their interfaces matter in the world. Neither a unified model of the whole argument nor an empirical demonstration of the present trajectory has been supplied. The text often says this clearly. Its weakest passages temporarily drop these distinctions, especially when moving from mechanisms into the conclusion and activation or release rules.

The appropriate revision is targeted. Preserve the corrected price-of-standing distinction, channel-specific levers, the conjectural status of C0, the separation of E2 and E3, and the explicit accounting of a cooperative arrangement's own hazards. Repair the few mathematical and logical bridges that still carry more weight than their support.

### I1 The test runner does not fail on all reported numerical failures

**Priority P2. Confidence high. Category verification.**

Locations: `checks_v62.py:65–78`, the main execution and final assertion counter at the end of the script, and `SUPPLEMENT.md:1282–1284,1290–1329,1347–1349`.

The reported 188 assertions are actual checks, but they are not a blanket regression gate for every computation printed by the 40 blocks. Twenty-three original `check_*` function bodies contain neither `expect` nor an `assert`. Nine receive additional asserting extensions later; several of their original comparisons remain print-only. Fourteen block names have no such asserting extension: FB, TC, TH, CB, RH, FS, BI, WG, PE, FD, LG, T3, AC and FA. This does not mean all fourteen contain a failed comparison, or that all should be turned into tests without deciding what counts as success. It means exit status does not certify all their displayed results.

A minimal fault-injection experiment confirms the distinction. In memory only, the review replaced FB's agreement increment with `agree += False`, and ran only FB. The output was:

```text
agreement 0/200000
=== assertions: 0 passed, 0 failed (default sizes)
```

The process exited 0. The experiment changed neither the manuscript nor its checker. Its log and exact mutation are in `harness-audit/injected-failure.log` and `harness-audit/audit.json`.

**Impact.** A later regression in an inherited block can leave the aggregate success message intact. A reviewer should not interpret the 188 count as 188 independently proved claims, 40 fully guarded blocks, or a complete certification of all computed examples. The Supplement already disclaims proof and empirical certification; that disclaimer is correct and should be retained.

**Repair.** Add an `expect` for each comparison intended to gate the build, starting with `agree == N` in FB, zero mismatch counts in TC and LG, and the explicit truth conditions of other print-only comparisons. Leave exploratory tables labelled diagnostic. Add a small harness self-test that injects a known false result and requires nonzero exit. The purpose is to verify failure reporting, not to duplicate the mathematics.

### I2 The necessity of shared understanding is a thesis beyond Lemma 3.11

**Priority P2. Confidence high about the logical scope, not a rejection of the author's philosophy. Category argument.**

Locations: `THEORY.md:281–285,293–300,1185–1187,1223`; proof at `SUPPLEMENT.md:302–304`; provenance at `CLAIMS.md:426` and the entry D36 in that table.

Lemma 3.11 proves a useful selection result for a costly trait whose benefit is equally distributed. It also explicitly permits transmission and rules that change relative payoffs. From this, the manuscript moves to a stronger statement: because a global irreversible failure cannot teach its survivors, anticipation on an accurate model is the only timely route, and shared understanding that we are one is a long-term requirement when growth and change are favoured.

The first implication is valid in its narrow sense: learning *from that terminal failure after it occurs* cannot prevent it. The stronger necessity does not follow. Rules can be learned from reversible precursors, local experiments, historical analogies or simulation; they can be maintained by sanctions and individually advantageous service arrangements. Actors can comply with a useful safety rule without sharing a comprehensive understanding of the whole system. A rule that changes relative payoffs is expressly outside the lemma's adverse-selection premise. The lemma contains no theorem that all such rules require common adoption of the proposed understanding.

This is not an objection to retaining Ren's words or to the pragmatic value of a shared model. It is an objection to calling that stronger necessity the lemma's formal content. If a system 'understands' solely by satisfying the institutional definition in §3.7, the claim instead risks becoming definitional. If cognitive understanding is also necessary, the required breadth and level of that understanding remain unspecified. The text need not, and does not explicitly, require every individual to comprehend the whole system. It already acknowledges local experimentation; what is missing is an argument that such routes cannot sustain the required institutions without the stronger shared understanding.

**Repair.** Preserve the author's statement as an explicit philosophical and institutional thesis. State separately the proved claim, the anticipation argument, and the conjecture that shared understanding is required to establish and sustain the relevant rules under open-ended change. Identify whose understanding, of what, and over which time horizon is required. A concise formulation is: 'The lemma explains why shared understanding and rules that change relative incentives are candidate routes; it does not establish that a shared global model is necessary for every viable arrangement.'

The provenance check found the 'favoured' formulation in the planning record as the author's stated choice, and CLAIMS correctly records that choice. A revision should correct its inferential status without silently replacing it with a different claim.

### I3 The test register is a research design outline rather than an operational preregistration

**Priority P2. Confidence high. Category empirical identification.**

Locations: `THEORY.md:775–780`; `TESTS.md:11,114–136,140–178,192–202`.

The register names promising observables and rival predictions. It also explicitly admits that loop gains are unestimated and readiness dimensions have not been measured. These admissions are strengths. Nevertheless, 'registered tests', 'registered indicators', 'certified row sums' and 'the dwell time' can sound like executable decision rules before the relevant estimands and measurement procedures exist.

For Test E in particular, an intervention having effects in more than one signature group does not uniquely identify the proposed interlock. A conventional causal network with several mechanisms and ordinary spillovers can also produce cross-effects. A disclosure duty can change reputation, financing, entry costs or selection, and thus need not be a clean intervention on conduct alone. Conversely, a true cross-effect can be small, delayed or masked by offsetting responses. A null estimate is not automatically the absence of the mechanism.

The same difficulty appears in the requirement that signatures persist 'unchanged over the dwell time'. The threshold model supplies a dwell time given its parameters and state. The empirical register has not supplied an independently estimated institutional dwell time, an equivalence margin for 'unchanged', or a rule for treating missing access as missing evidence rather than safety or capture.

**Repair.** Keep the present tables as a mechanism-testing agenda. For each first implemented test, register the following before observing its outcome:

1. The population, unit of observation, selection rule and observation horizon.
2. The intervention and the measured first-stage changes in the model parameters.
3. The primary outcome and its quantitative link to the model variable.
4. The rival causal model, including possible cross-effects and anticipation.
5. A minimum consequential effect, an equivalence margin for a null, and the uncertainty procedure.
6. The dwell horizon, fixed independently of the outcome being explained.
7. Treatment of strategic missingness, measurement changes, substitution and spillovers.
8. The precise inference to be withdrawn on a positive, negative or inconclusive result.

The first Test E should compare estimated cross-derivatives and their direction, lag and size under explicit rival models, rather than 'more than one group changes' against 'only one changes'. Do not require this entire programme before publishing the theoretical paper; require it before claiming that a pilot has confirmed or refuted C0, or using that result to activate a consequential policy.

### I4 The short reading path compresses conditions beyond safe readability

**Priority P3 advisory. Confidence high. Category presentation. This is optional entry-point advice, not a requirement to shorten the theory of record.**

Locations: `README.md` reading paths; `THEORY.md:5,17–31,57–69,1223–1227`; build report `reviews/xref-review.log`.

The assembled build counts 56,194 core words, 58,890 Supplement words and 20,573 Discussion words, excluding references and using the builder's formula-stripping convention. This is approximately 135,657 words before the registers. Length is not itself a defect: the recorded author direction explicitly says to complete the theory before compression and not let page limits govern it.

The problem is the density of the advertised short route. The English abstract is one long paragraph combining local stability, common and relative continuation returns, correction rates, enforcement, asymptotic survival, masked divergence, ontology and three policy tiers. Readers must hold several distinct domains of validity in working memory before the definitions exist. The Chinese guide is substantially more natural than mechanically translated prose, and 母体 is consistent, but technical clauses such as '决定性增长不及存量比例者' still require the formal text to decode. A bilingual keyword score checks vocabulary, not equivalent qualifications or comprehensibility.

**Repair.** Keep the full files as the authoritative research dossier. Add a genuinely short entry point only after the substantive repairs: question, three main established results, three major open bridges, and what each tier recommends. In the abstract separate results from diagnosis and judgment into short paragraphs. Introduce 'won share' with one plain-language sentence before using it as the scissors' pivot. Preserve the author's expressions as quotations or declared commitments; distinguish their force from a theorem's force.

### Preservation and provenance sample

The review checked the fourteen-loss table in `LEDGER.md:312–333` against its stated homes and directly compared a targeted sample with the source records. This is a sample, not a fresh adjudication of all 1,060 sentences in the preservation ledger.

| Item | Source inspected | Assessment |
|---|---|---|
| Growth and the mind | `sources/16-claude-code-directions/2026-09-25-the-mind-not-the-approach.md` | The underlying ruling is present. 'Growth is not the danger; the mind is' is a rendering of a longer English statement, and CLAIMS D13 correctly marks that fact. |
| AI as planetary technology and broad E1 | `sources/16-claude-code-directions/2026-09-26-planetary-technology-and-the-literature.md` | The broad scope is the author's. The narrow list as an ordering of first steps originated as the assistant's reading; the register correctly distinguishes it. |
| Falling behind a cancer-like winner | `sources/16-claude-code-directions/2026-10-03-v4-direction-cooperation.md` | The Chinese ruling supports the restoration in §3.8; the English remains a rendering. |
| E2 and E3 remain distinct | Same 3 October record | Explicitly supported by the author's rejection of merging stop and slow. The review's recommendations preserve both. |
| Decay as growth | `drafts/2026-10-02-friend-conversation/transcript.md:483` | Speaker B explicitly states this. The manuscript discloses the provisional identification of Speaker B as Ren. |
| Identity with the process | Same transcript around `:557`, and `CLAIMS.md` D34 | The distinctive identity formulation is restored; removal of opening speech repetitions is recorded. |
| Favoured growth and change | `v6-planning/P5-ren-corpus-generators.md:137`, CLAIMS D36 | The wording choice is recorded. This review does not claim to have independently recovered the original audio or message behind that planning note. |

The register's distinctions between Ren's words, AI drafts he adopted, model renderings awaiting confirmation and literature are valuable. No sampled attribution defect justifies undoing these restorations. 'Restored in your words' should still be read with the register's own qualifications: many English and Chinese sentences are renderings, and some corpus phrases are explicitly not the author's original drafting.

### What the build checks establish

An isolated copy was assembled and checked to avoid overwriting the reviewed release. The assembly and xref checks passed, and every compared assembled file and keyed source was byte-identical to the reviewed input. The isolated xref initially failed because `refs_v62.py` imports the bibliography from the sibling `v6/THEORY.md`; supplying that repository dependency made the run pass. This was a limitation of the initial isolated copy, not a manuscript build failure. A standalone release should document or bundle that dependency.

The checker reported 93 core declarations and 35 Supplement declarations, 103 cited works in THEORY, 89 in SUPPLEMENT and 132 in DISCUSSION, with matching bibliography counts. It found all 32 required core items and nine Chinese guide items matching the nine English argument items under its vocabulary criterion.

The register-only citation warnings are informational under the current checker. Some entries are parser artefacts, while others are actual works absent from the three bibliographies. Their presence is not a contradiction of 'xref passes'; it is a limit of what that pass means. A public release should either give registers their own bibliography or make their references resolvable directly.

The source manifest, isolated-build comparison, main numerical log and fault-injection evidence are retained in this review directory. A clean build validates assembly, numbering and the implemented syntactic checks. It does not validate the semantic use of a cited source, equivalence of English and Chinese qualifications, completeness of a proof, or the policy applicability of a numerical example.
