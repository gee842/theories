# Independent second review: chapters 2–3 / S2–S3

All line references below are to the frozen assembled THEORY.md and SUPPLEMENT.md, not source fragments. No existing V6.2 review was read. Calculations use only the standard library and do not import the manuscript's checks.

## Assessment

The repaired structural results are substantially sound: the discounted domain for the fixed-prize structural model, channel-dependent correction/provision signs, cap equality and diffusion, the affine-fitness qualification, and the endpoint sanction condition can close. The proportional-prize, fixed-exponent capacity result also survives independent derivation over every positive finite horizon and the stated convergent infinite horizon. But the *general* balanced-path price theorem omits a time-invariance premise, and the general private-equilibrium elasticity argument uses a symmetry that disappears when one actor's intensity is frozen. The Markov calculations reproduce as discretized stochastic games; several statements interpret them as more than that.

## 1. General balanced-path price formula is false for permitted level channels

**Location:** THEORY:263–269; SUPPLEMENT:267–284. Priority: substantive (P1/P2 depending on whether the general formulation is retained).

Proposition 3.9 allows arbitrary increasing strength functions from Proposition 2.2 and claims a constant-reference resolvent on a balanced growth path. Proportionality of the prize does not make the strengths' derivatives constant along that path. The one-channel special case in (2), inherited from Proposition 2.3 with fixed exponent r, has this property; the general proposition does not.

**Counterexample within the stated stock model.** Two actors, sigma_i=K_i, Omega=S=K_1+K_2, kappa=.2, d=.1, beta=diffusion=provision=0, discount=.8. Start on the symmetric balanced path at K_1=K_2=1. The path is K_t=1.1^t. At the reference date the structural elasticity is r=1 and both printed discounted gains equal

    Gamma_delta = Gamma_c_delta = .8*.2 / (1-.8*.9) = 4/7 < 1.

The printed formula therefore gives lambda_rel=lambda_com=4/3. The common result is correct. For a relative stock displacement x_t, however, the exact nonlinear recurrence and excess winnings are

    x_(t+1) = .9*x_t + .2*K_t*tanh(x_t),
    excess_winnings_t = K_t*tanh(x_t).

Thus the relative variational multiplier is .9+.2*1.1^t, not the constant 1.1 used by the reference resolvent. It grows without bound. Starting with x_0=.2*y, partial sums of the discounted relative derivative through 5, 10, 20, 30 and 40 future periods are approximately

    .7783713, 1.8005125, 27.477427, 122097.22, 1.1704731e12.

Every summand is nonnegative. The variational terms eventually grow without bound, so finite-horizon derivatives and Fatou's lemma give an infinite derivative of the infinite-horizon value. The value itself remains finite, because excess winnings are at most K_t and sum .8^(t+1)*1.1^t converges. Direct nonlinear values divided by y are approximately 472.94, 193927.49, 1.0373e8 and 6.2564e10 at y=1e-3,1e-6,1e-9,1e-12.

**Repair:** keep the general result at symmetric steady states; for a balanced path explicitly assume the full common and relative Jacobians and output coefficients are constant along that path, as in homogeneous ratio strengths with fixed exponents and proportional prizes. Otherwise define lambda_rel and lambda_com with the time-ordered products of date-dependent Jacobians. The accounting identity (9) survives whenever those actual returns exist. This does not refute Proposition 3.9(2) / S3.2's fixed-exponent proportional-capacity result.

**Reproduction:** `analytic_audit.py`, function `audit_balanced`.

## 2. The private-elasticity proof loses its required symmetry

**Location:** THEORY:138 (part 4), THEORY:271; SUPPLEMENT:119–121 and :298. Priority: substantive proof gap; do not label the finite-terminal example itself a complete stationary infinite-horizon counterexample.

The rank-one **equilibrium** argument is correct: exchange symmetry and sum p_i=1 imply a+(n-1)b=0 when every actor responds. Holding only actor i's intensity fixed breaks that symmetry. The private share's own-stock partial no longer determines its response to a mean-preserving stock perturbation. SUPPLEMENT:121 applies the former relation without proving it for the latter derivative. A common stock shift may now affect private value even with a fixed prize.

**Explicit local counterexample to the identity used in the proof.** A two-actor terminal contest has

    p_i = exp(K_i e_i) / sum exp(K_k e_k),
    payoff_i = p_i - e_i^2/2.

At K_1=K_2=1 its symmetric equilibrium is e_1=e_2=1/4. Each player's stage objective is strictly concave near this state (indeed its probability term's second derivative is bounded in magnitude by K_i^2/(6 sqrt(3)), below the unit quadratic-cost curvature). The equilibrium is therefore a genuine local smooth Nash branch, not an arbitrary response policy. The FOCs give e_i=K_i p(1-p), and at parity

    partial e_2/partial K_1=0,
    partial e_2/partial K_2=1/4.

Holding e_1=1/4 while letting the rival follow that policy gives

    partial p_1/partial K_1 = 1/16,
    partial p_1/partial K_2 = -1/8.

The theorem's definition reads r_pr=4*(1/16)=1/4. Its proof predicts a relative derivative r_pr/(n K)=1/8. The actual derivative along (K_1,K_2)=(1+y,1-y) is 3/16. The derivative of the **net equilibrium payoff** is also 3/16, by the envelope theorem. Under a common shift of both stocks its derivative is -1/16, so the assertion in :298 that a fixed prize makes the common value zero is not a general property of responding contests.

The same missing term can be seen formally in a stationary extension. Set d=1, Omega=1, and k0=1-kappa/2, so next-period total capacity is always 2. In any smooth symmetric stationary equilibrium of this contest let D=V_K1-V_K2 and z=1+discount*kappa*D. The parity FOC is e=z/4. Under a common current-stock shift the continuation state stays at parity and de_2/d(common stock)=z/4. Therefore, after freezing e_1, the sum of private share derivatives is -z/16, not zero. If alpha is the private own-stock derivative, the actual relative derivative is 2 alpha+z/16, while the proof uses 2 alpha. This algebra identifies the omitted term but does not by itself prove existence of the full stationary equilibrium branch; the terminal contest suffices to refute the proof's purported symmetry principle.

**Repair:** define the private derivative on the actual mean-preserving direction; add common-scale invariance (and suitable cost/state assumptions) if a fixed prize is supposed to make the common value vanish. Prove the deterministic stationary Bellman derivative with all state and payoff channels. The equilibrium-stability half can remain. The stochastic finite-jump game needs its own statement, below.

**Reproduction:** `analytic_audit.py`, function `audit_private`; outputs r_pr=.25, claimed relative derivative=.125, actual=.1875, common=-.0625.

## 3. The exact finite-jump identity is only checked at r=1 and is false more generally

**Location:** SUPPLEMENT:140, :298; `checks_v62.py` check_MP(h). Priority: P2.

The prose says that with others' conduct fixed the exact finite-jump price equals Gamma_delta/(1-Gamma_delta), and concludes that all deviation from the formula comes from strategic response. The script asserts that identity only when r==1. For a nonlinear success function, finite winner/loser state jumps sample a nonlinear value function and do not equal its parity derivative.

Independent passive policy evaluation in exactly the stochastic winner/loser model gives, at r=1.5, Gamma=.6, d=.2, discount=.97 and 1500 cells,

    exact finite-jump price (interpolated Bellman): 1.031109173689984
    printed local structural formula:            1.081784386617101
    Bellman residual:                            9.95e-12.

At r=1 under the same parameters the values agree to machine precision. The r=1 identity is sound because the fixed-policy reward and mean transition are affine.

The responding solver is also a stochastic game, unlike the deterministic share recurrence used in the local theorem. At r=4, Gamma=.45, d=.1, discount=1/1.1, 1500 cells, the reproduced price is .5131005855, while the measured local-private formula is .6534211711 even though Gamma_pr_delta=.3951934<1. The manuscript itself acknowledges this discrepancy at :153 and excludes the case because Gamma_eq>1. That exclusion is neither in Proposition 2.2(4) nor a consequence of the corrected discounted-domain argument. In the stochastic lottery even exact parity moves to two distinct states next period; a local parity Jacobian does not close its Bellman equation.

**Repair:** qualify the exact passive identity by r=1; describe other comparisons as local/small-jump approximations with measured errors. Separate deterministic local stability, drift of the stochastic conditional mean, and stochastic value/dispersion. The reported expected-deviation multiplier does not make parity an absorbing/stable state of the stochastic process.

**Reproduction:** `markov_audit.py`, function `passive`; and `solve(r=4,gamma=.45,decay=.1,cells=1500)`.

## 4. Strict narrowing has an omitted endpoint

**Location:** THEORY:263–269; SUPPLEMENT:279–282. Priority: P2/P3.

The held domain in (6) includes theta_0=-1. Equation (9) then gives theta=-1 for every admissible relative/common return. Thus 'whatever theta_0<n-1' and 'narrows whenever Gamma_delta>0' are false at the included lower endpoint. The purely relative objective is already at the lower bound and cannot narrow. Use -1<theta_0<n-1 for strict inequalities, and state that both endpoints are fixed. The finite-horizon proportional-prize comparison is otherwise correct for every horizon with at least one future payoff and positive discount/conversion.

**Reproduction:** `analytic_audit.py`, function `audit_endpoint`.

## 5. Payoff monotonicity does not supply the cumulative selection rate

**Location:** THEORY:214, :225–227; SUPPLEMENT:239. This corroborates the lead reviewer's finding.

With two loads 0 and 1, let Delta pi=1/(1+t), so B(t)=log(1+t) diverges. The relative, strictly payoff-monotone autonomous rule

    dot p = p(1-p)*(Delta pi)^3

has logit p(t)=logit p(0)+(1-(1+t)^(-2))/2, so its higher-load share stays strictly below one. The proof uses the replicator identity for log share ratios although the core quantifies over all payoff-monotone rules. Use replicator/cumulative-gap dynamics or impose divergent cumulative *selection* advantage.

## Markov findings that reproduce, with their limits

- **Multiplicity:** independently reproduced the smooth and steep branches. For Gamma=.2,d=.05,r=4, discount=1/(1+d), the step-start branch's finite winner/loser value is 1.3918628713 on 3000 cells and 1.4102793965 on 6000. Bellman residuals are below 1e-11. Every interior-grid continuation contest valuation is positive (minimum about .754 on the 6000 grid), and the computed win probabilities agree with the probabilities generated by both efforts to machine precision. Thus no simple negative-value clamping or invalid zero-effort explanation defeats the reported branches. What is corroborated is two discretized fixed points; convergence to a continuous-state Markov-perfect equilibrium and deterministic-model multiplicity remain unproved. Retain the explicit outside-review qualification and avoid promoting the label 'winner-take-all equilibrium' to a proved continuum result.
- **Catch-up:** at L_sub=100,Gamma=.3,r=4,d=.1 the independent result is r_eq/r=.9934254 and r_pr/r=.9967083, confirming a small reversal in the *elasticity correction*. But the total computed continuation price is 4.5818657, versus the structural .1764706, because the new flow penalty directly values standing. The price is not reduced below the structural price. The wording in THEORY:271 / SUPPLEMENT:298 should explicitly say the reversal concerns the equilibrium/private win-share elasticities, not the total value of standing in the augmented payoff model. The general theorem's price correction lists shared intensity loss but does not model this direct standing payoff.
- **Static factor:** 2(n-1)/n is correct for the stated weighted Tullock contest with linear effort cost. Its ratio-scale invariance is a feature of that contest, not a proof of the unrestricted private derivative claim.
- **High patience / off parity:** the stochastic price amplifications and the distinction between finite-jump value and a local slope are real numerical features; they do not verify the general closed form. In the reproduced high-patience case r=1.5,Gamma=.6,d=.2,discount=.97 the responding finite-jump price is 8.5139658, its local derivative-based price is about 9.056084, and the local private gain exceeds one while both computed stochastic prices remain finite.

## Previous findings that can close in this remit

1. **Price domain:** fixed for the fixed-prize structural deterministic model. The correct finite first-order domain is Gamma_delta<1, which can include Gamma>1; the divergent derivative above that threshold is not a negative price. The new errors above concern extensions, not the old structural repair.
2. **Sign of correction:** fixed. S2.4 correctly differentiates the stock-level dependence of r. Correction lowers both gains when xi_r>=1; a ratio channel has xi_r=0, making the undiscounted gain unchanged without diffusion and increased with diffusion, and the discounted gain increased. Sharing/diffusion reduce the corresponding positive terms; provision has the sign of xi_r-1. These are conditional channel statements, not one universal correction sign.
3. **Cap equality and diffusion:** fixed under the stated held-leader premise and rate assumptions. The derivative at K*=bar K is d[Gamma_0(n-1)/n-1]-delta_f(n-1)/n. A strict lower cap has positive drift immediately below it. Return from every positive start is exactly phi>0 on the open interval because the scalar capped update is monotone; diffusion contributes the missing rank-independent source. A positive source is necessary for r>1 and is correctly no longer said to be sufficient. The manuscript now states when leaders can actually stay at the cap.
4. **Affine fitness:** fixed in Lemma 3.11 / SUPPLEMENT:302–306. Under the specified common-benefit, common-baseline payoff model the total and each within-group covariance are nonpositive for increasing fitness; only affine fitness guarantees the between-group covariance is nonpositive under every partition. The old nonlinear counterexample is correctly retained as a boundary.
5. **Falling-sanction endpoints:** fixed in Lemma 3.3 / SUPPLEMENT:233. Continuity and strict decrease give an interior root exactly under F(0)>c>F(1); otherwise the sign over the open interval gives the stated one-sided dynamics. The cumulative-selection qualification added to the fixed-sanction evasion claim is useful, but does not propagate to Proposition 3.4.
6. **Test Gamma's observable:** the change of sign is fixed. In the static contest the ratio of responses to shared harm and private cost is 1+theta; provision lowers the ratio-channel discounted gain and raises this observable. Identifying it with a full dynamic equilibrium still requires the interfaces the paper acknowledges.

The other previous findings (falling cost, R8, stochastic punishment, delegation endpoint, row-sum necessity, line 363, Test M) belong to the other reviewers' remit.

## What is sound in the new proportional-prize result

For one fixed-exponent ratio channel, no provision or diffusion, Omega=gS, write a=(1-beta)r, b=kappa*g, and D=1-d. Then Lambda_rel=D+ab, Lambda_com=D+b, and the period-t relative/common increment ratio is a*(Lambda_rel/Lambda_com)^(t-1). Both factors are above one exactly when a>1, below one when a<1, and equal at one. Thus every positive finite partial sum compares in the claimed direction, as does the convergent infinite sum. This is the same condition for share instability. With diffusion f the two derived thresholds are a>1+delta*f/(1-delta*D) for narrowing and a>1+f/b for share instability, with the stated positive gap when the common discounted loop is finite. No discrepancy found in that result.

## Scope of verification

Read the full chapters 2–3 and S2–S3 and the relevant MP/SP/CE/CH/PR portions of the check implementation. Derived the structural local Jacobian, channel signs, cap conditions, price accounting, proportional-prize all-horizon comparison, affine-fitness covariance and sanction-root conditions independently. Wrote and ran the independent scripts named above. Reproduced selected smooth, steep, catch-up and passive Markov cases. Did not prove continuous-state Markov existence/uniqueness or check every external literature claim. No manuscript, register or existing script was edited.
