# Maintaining access to correction under a confidently wrong model

Formal research note, 5 October 2026. This develops the earlier identification argument. Its claims concern specified observation, acquisition, detection and control rules; they are not empirical claims about introspection or consciousness. No earlier deliverable or frozen evaluation was changed.

## 1. Three distinct achievements

An opportunity for correction can fail at several separate points:

1. **Access:** a post-change observation is actually acquired within some delay and budget.
2. **Discrimination:** the acquired data distinguish the changed condition from an unchanged one, with stated false-alarm and miss rates.
3. **Effective revision:** the system uses the evidence to revise a relevant estimate or policy, and the resulting behavior meets a stated criterion.

A sampling schedule can guarantee the first without guaranteeing the second or third. A correct alarm is not necessarily an accurate state estimate. An accurate estimate is not necessarily used, and its use is not necessarily stabilizing. The criterion being protected—accuracy, control, revisability or something else—must also be specified.

“Detection” cannot mean merely emitting an alarm: a policy that always alarms has zero apparent delay. Every meaningful detection guarantee must also constrain false alarms or require a correctly distinguishing observation.

## 2. An exact failure of confidence-dependent access

Let a latent condition be q_t=0 before a persistent change and q_t=1 afterward. The ordinary stream is y_t=0 in both conditions. A purchased reference is z_t=q_t exactly. This intentionally simple example has an uninformative ordinary sensor and an informative reference; it is not a neural or physical architecture claim.

A model begins with estimate q_hat=0 and modeled uncertainty V=0. Its acquisition rule buys only when V exceeds a positive threshold; its update rule cannot increase V from the unchanged ordinary stream. It therefore buys no further references, remains wrong after the change, and remains certain according to its own calculation. The reference would have corrected it if obtained.

The same obstacle is broader than a variance threshold. Consider any acquisition rule based on ordinary observations, past purchased references and internal randomness. Until a new reference is purchased, the no-change and changed worlds above give it identical histories. Couple the same internal randomness. Its purchases, internal updates and alarms must then follow the same paths in those two worlds. A correctly distinguishing zero-false-alarm detector cannot recognize the change before a reference reveals it.

Consequently, a gate that can stop purchasing indefinitely on the no-change history cannot promise finite detection delay in this example. An ordinary-innovation trigger also fails because its available ordinary history does not differ. Additional computation of that history does not create the missing distinction.

This does **not** say that every history-based gate fails. A gate can contain a clock or enforce a maximum gap. “Protected” and “history-dependent” are not mutually exclusive algorithm classes. Protection is a constraint on what the rule must continue to permit, even when its current estimate or uncertainty gives no reason to ask for evidence.

## 3. Exact finite-budget bound for protected sampling

Fix the timing convention before using a numerical bound. There are N equal opportunity intervals after an initial boundary at time 0, and potential acquisitions at integer times 1,...,N. A persistent change may occur immediately after any boundary j in {0,...,N-1}. An acquisition at time s>j can reveal the change. We measure the wait as s-j. No acquisition at time 0 is included in the following budget B.

Assume 1<=B<=N and that a reference is perfectly discriminating after the change. Let selected sample times be

\[
0=s_0<s_1<\cdots<s_B=N.
\]

The terminal sample is required to cover changes late in the interval. The maximum wait is exactly

\[
D(S)=\max_{1\le i\le B}(s_i-s_{i-1}).
\]

Since these B positive integer gaps sum to N,

\[
D(S)\ge \lceil N/B\rceil.
\]

Balanced gaps differing by at most one attain this bound. Thus the minimax maximum wait is exactly ceil(N/B). With opportunity spacing Delta, multiply the bound by Delta. For continuous-time changes between opportunities the same quantity bounds the supremum waiting time, provided the start and terminal coverage boundaries are stated.

This is also a lower bound for deterministic adaptive gates in the example of Section 2. Follow the gate's no-change path. Before the first revealing sample, a change produces the same observations and therefore the same acquisition choices. Placing the change just after the start of that path's largest gap realizes the same delay. Adaptivity cannot improve the worst case merely by conditioning on an uninformative ordinary stream. This argument assumes correct discrimination without false alarms; an unsupported premature alarm is not a way around it.

For randomized gates, the gap bound applies to every realized schedule required to satisfy a hard pathwise guarantee. Randomization may alter expected delay against a change time chosen independently of the random seed; that is a different objective. Do not silently substitute an expected guarantee for a hard one, or assume an adversary sees randomness unless that model is intended.

### Boundary conditions that matter

- **No terminal sample:** a change after the last purchase has no detection guarantee by the stated horizon.
- **Initial calibration costs money:** if the initial boundary itself uses a purchased reference, charge it separately. With total budget B_total and one mandatory initial purchase, only B_total-1 purchases remain to cover later intervals.
- **Finite horizon:** original opportunities 0,5,...,55 cannot reveal a change occurring after 55 within a 60-step episode, regardless of unused budget. A promised bound must restrict eligible change times or extend follow-up.
- **Finite lifetime budget, unlimited runtime:** after the last of at most B purchases, an unchanged-history gate leaves an unbounded uncovered tail. No uniform finite detection bound is possible for arbitrary later changes in the uninformative-ordinary-stream example.
- **Persistence:** a transient condition can appear and disappear entirely between samples. Even perfect references then reveal no change. Require persistence through a revealing sample, a sufficient dwell-time condition, or explicitly accept missed transients.
- **Availability:** a scheduled opportunity that is cancelled or unavailable is not an acquired measurement. The theorem assumes those opportunities can actually be used.

## 4. Protected and discretionary purchases can coexist

Split a finite budget into B_p protected purchases and B_r discretionary purchases, with B_p+B_r<=B. Reserve the B_p purchases for a schedule that covers the declared interval and ends at the terminal boundary. The discretionary gate may add observations but may not exhaust the protected reserve or remove its coverage.

For an arbitrary protected schedule S_p, the guaranteed maximum acquisition wait is its actual largest gap D(S_p), including the initial and terminal coverage boundaries. If the protected dates are chosen with balanced integer gaps as in Section 3, that maximum equals ceil(N/B_p). Reserving B_p purchases alone does not establish the balanced bound. Extra discretionary purchases can shorten waits and cannot increase D(S_p) if the protected purchases remain intact. Protection has an explicit opportunity cost: fewer purchases are available for reacting to the model's current priorities.

A more flexible implementation can move scheduled checks, but must maintain a verifiable coverage constraint. After a protected sample at opportunity s, covering the remaining N-s intervals with maximum gap D requires at least ceil((N-s)/D) future purchases, including the terminal one. Spending below that reserve invalidates the guarantee. This formula applies immediately after an anchor sample; at other times the already elapsed gap must also be accounted for.

There is no need to treat a reactive observation at a protected date as two purchases. Conversely, counting an early reactive purchase as a replacement for a later protected one is valid only if the resulting maximum-gap and terminal conditions are still satisfied.

This is a mechanism design condition, not a claim that any particular budget split is morally required. Added observations have costs, and an unnecessary update based on them can add noise. A protected purchase need not force the estimator to accept its content as correct.

## 5. Acquisition guarantees become detection guarantees only with extra assumptions

### Perfect or bounded-noise informative reference

Suppose a known baseline is q_0, a persistent change is delta, and a reference is z=q+eta with |eta|<=sigma. Under no change, |z-q_0|<=sigma. Under change, |z-q_0|>=|delta|-sigma. Therefore, if |delta|>2 sigma, the test

\[
|z-q_0|>\sigma
\]

has no false alarms and detects at the next sample. Protected sampling supplies its acquisition-delay bound. If the baseline estimate itself can err by beta, a sufficient uniform separation condition is |delta|>2(sigma+beta), with threshold sigma+beta.

These are sufficient conditions under stated bounds. At overlapping observation supports, an adversary can choose noise that makes an unchanged and changed reading identical; certainty no longer follows from one sample.

### Gaussian noise: high probability, not certainty

For independent Gaussian reference errors with nonzero variance, the unchanged and changed distributions of any fixed finite number of observations have positive densities everywhere. A test with false-alarm probability exactly zero therefore also has zero detection probability against a finite mean shift. Certain finite-sample detection and zero false alarms cannot both be claimed.

A conditional high-probability statement is possible. Suppose q_0 is known, reference errors are independent N(0,sigma^2), and a persistent mean shift has magnitude at least delta_min. Average m post-change references. For at most M tested windows, allocate alpha/M false-alarm probability to each two-sided test. With Phi the standard normal cumulative distribution, use

\[
h=\frac{\sigma}{\sqrt m}\Phi^{-1}(1-\alpha/(2M)).
\]

The union bound gives at most alpha probability of any false alarm under the unchanged model. Overlapping windows need not be independent for that union bound. A sufficient condition for detection probability at least 1-beta on an entirely post-change window is

\[
\delta_{min}\ge\frac{\sigma}{\sqrt m}
\left[\Phi^{-1}(1-\alpha/(2M))+\Phi^{-1}(1-\beta)\right].
\]

The miss probability is bounded by the appropriate one-sided Gaussian tail. This statement requires a genuinely post-change window; averages mixing old and new regimes may dilute the signal. With a maximum sample gap D, the mth post-change protected sample arrives within mD intervals **if those m future samples exist**. Changes too near the endpoint require additional follow-up or must remain unresolved.

The error model, known baseline and number of tests are substantive assumptions. Correlated reference noise, an estimated baseline, selective sampling dependent on current reference noise, or an unbounded sequence of repeated tests needs a different calculation. A small reported posterior variance does not establish these assumptions.

## 6. Protected evidence can still be uninformative

The earlier model has

\[
x_{t+1}=a x_t+u_t+g+w_t,\quad y_t=x_t+b+\epsilon_t,
\quad z_t=x_t+d+\eta_t.
\]

When unknown constant g,b,d and the initial-state class admit the shift

\[
(x,b,d,g)\mapsto(x+c,b-c,d-c,g+(1-a)c),
\]

both sensor histories remain identical under the same observation-based controls, even when every possible reference is purchased. Protected access alone cannot distinguish the absolute latent states. A known initial prior, known forcing or unbiased reference can supply an anchor, but must be established rather than assumed by the word “reference.”

There is also an exact estimation lower bound. If two observationally equivalent states are separated by c, any estimate based on that same history has identical distribution in both worlds. For any realized estimate h,

\[
(h-x)^2+(h-x-c)^2=2(h-x-c/2)^2+c^2/2.
\]

Thus at least one world's expected squared error is at least c^2/4. For a trajectory pair separated by c for T steps, at least one world's expected cumulative squared estimation error is at least T c^2/4. This bound concerns the unanchored model class, not the original anchored simulation.

The broader lesson is that sampling and identification are different achievements. Even “independent” sensor hardware need not provide an independent absolute anchor if its error structure shares the same unresolved symmetry.

## 7. Informative evidence can still fail to produce useful correction

An implementation can acquire and correctly flag a discrepancy while its bias estimate remains frozen. For instance, logging z-y but enforcing h_next=h leaves a prior wrong correction unchanged. This is failure of the revision path, rather than failure of observation.

Even a perfect state estimate does not guarantee good control. In the noiseless system x_next=.8x+u, take u=clip(-2x,-2,2). Starting at x=10/9 gives x_next=-10/9, and the next state is 10/9 again. Perfect observations coexist with a persistent two-cycle. Without clipping, the same gain gives x_next=-1.2x and is unstable.

A limited positive guarantee can be stated explicitly. Suppose the revised estimate obeys x_hat=x+nu with |nu|<=epsilon; process disturbance satisfies |w|<=W; control is u=-k*x_hat without active clipping; and rho=|a-k|<1. Then

\[
|x_{t+n}|\le\rho^n|x_t|+
(|k|\epsilon+W)\frac{1-\rho^n}{1-\rho}.
\]

This follows by iterating |x_next|<=rho|x|+|k|epsilon+W. It supplies convergence to a bounded region, not exact convergence to zero in persistent noise. For a clipped implementation, a sufficient invariant-region check is to choose M with

\[
M\ge (|k|\epsilon+W)/(1-\rho),\qquad
|k|(M+\epsilon)\le u_{max},\qquad |x_t|\le M.
\]

Then the command remains unclipped and the bound applies inductively. If an unknown forcing remains, the state-error bound or controller must account for it. Detection alone does not establish any of these conditions.

## 8. A precise combined claim

For a persistent change within a covered interval, protected sampling supplies a maximum acquisition delay **if** budget, opportunity and terminal conditions hold. An informative reference and valid detector convert that into a discrimination guarantee. A revision rule with proved estimation and control properties then supplies a behavioral guarantee. Each implication has separate premises.

Failure at one stage cannot be repaired merely by calling the next stage more reflective. Nor does a protected schedule solve the unknown-reference problem. The useful structural proposal is to preserve a specified route by which evidence can still arrive and alter an estimate when its current confidence would otherwise stop the process. Whether to preserve that route, at what cost, and for whose purposes remains an additional design and normative question.

## 9. Criteria for this synthetic study and later extensions

- Declare the change-time support, end-of-horizon follow-up and minimum persistence before claiming a delay bound.
- Report acquisitions after change, informative residuals, alarms, parameter revision and useful state recovery separately.
- Include a confidently wrong gate that never opens, a confidence gate with protected opportunities, and an ordinary-innovation gate. Do not presume the ordinary innovation is informative in every world.
- Include reference bias or drift and unknown forcing. A protected but misspecified reference should not be advertised as a valid anchor.
- Count initial calibration, protected and discretionary purchases against the same budget; verify reserve invariants directly.
- Report no-change purchases and false alarms, late or undetected changes, capped delays and total sensing cost. Exclude undetected cases from neither denominators nor summaries without disclosure.
- Distinguish fixed finite-horizon bounds from expected performance over a chosen distribution of change times.
- Compare the update path itself: acquiring a warning, accepting a change and restoring useful behavior need not coincide.

The accompanying standard-library check script exhaustively verifies the finite scheduling bound for small N and checks the exact algebraic counterexamples. Its finite examples corroborate the arguments; the proofs state the general claims.

## 10. Review of the proposed continuation protocol

The protocol read at `work/correction-access/protocol.json` uses a 60-step horizon, opportunities at 0,5,...,55, six paid observations, and an integer bias-change time tau uniform on 8,...,47. The change applies before the observation at tau. Thus a purchase at tau has arrival delay zero; a gap of G integer steps can have maximum arrival delay G-1. This convention differs from the “immediately after boundary” convention in Section 3 and explains the numerical one-step difference.

The fixed schedule 0,10,20,35,45,55 guarantees arrival within 14 steps over the declared support; tau=21 attains it. The hybrid's protected dates 0,25,55 guarantee arrival within 29 steps; tau=26 attains it. Up to three extra observations cannot weaken that bound if protected purchases remain reserved. Exhaustive enumeration of all 130 possible optional subsets confirms it. These bounds are for reference arrival, not correct detection, and rely on the restricted change-time support. Neither schedule is asserted to be minimax over that restricted support.

The factorial worlds use fixed forcing g and fixed reference bias d, with the ordinary bias b either constant or changing sign once. Since y-z=b-d+epsilon-eta, fixed forcing does not enter this residual and fixed d does not change its jump magnitude. Every such reference remains informative about a persistent reversal of b under the supplied noise model. Reference bias can still contaminate absolute-state interpretation, and unknown forcing can confound the ordinary-innovation gate. This study should not be described as demonstrating reference observations that are intrinsically uninformative about the change itself.

The proposed standardization of ordinary innovations is explicitly a heuristic, not an exact conditional variance. This is appropriate: the retained bias estimate can share noise with the previous ordinary observation, and adaptation creates further dependencies. Its threshold exceedances in constant-bias worlds are reasonably labeled model-discrepancy alarms; they are not automatically statistically defined false discoveries, because the initial estimate, forcing or reference model may still be wrong.

The descriptive three-state filter's d prior variance .0625 is a supplied assumption matching the nonzero +/- .25 regime. The equally weighted mixture of zero and nonzero-reference factorial worlds instead has d variance .03125. Calling the algorithm a Gaussian moment filter is reasonable, but describing that particular prior as the exact pooled-world moment match would be inaccurate.

The proposed six primary comparisons correctly retain the paired seed as the independent unit and average worlds within seed before comparing losses. Equal sensing caps do not ensure equal actual expense; separate purchase counts and costs remain necessary. The protocol appropriately reports missing arrivals, recovered fractions and costs, and excludes computation, energy and memory pricing from its causal claims.

No material mathematical defect was found in these declared access bounds or statistical comparison definitions. This pre-evaluation protocol review did not certify the implementation. Reserve bookkeeping, update chronology, actual clipped actions in the innovation, absence of unpurchased-reference leakage, and independence of all exogenous draws from policy decisions are obligations for the separate implementation checks.
