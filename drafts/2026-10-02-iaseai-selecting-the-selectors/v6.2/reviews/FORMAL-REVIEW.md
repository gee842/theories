# V6.2 independent formal review

Date: 4 October 2026. Reviewed material: the assembled V6.2 `THEORY.md`, `SUPPLEMENT.md`, relevant `CLAIMS.md` and `TESTS.md` entries, the stable-key map, and the implementation and assertions of numerical block MP. This report concentrates on Sections 2, 3, 5 and 7: the structural loop, the price of standing, channel levers, enforcement, and the scissors. It does not claim independent verification of the entire manuscript or every one of the 188 checks.

No manuscript source or assembled document was edited. No commit was made. The independent script and its output are `reviews/formal-audit/independent_audit.py` and `reviews/formal-audit/results.json`. The script uses the Python standard library and imports no manuscript implementation.

## Overall judgment

The deterministic structural mathematics is substantially stronger than V6.1's reported form. The rank-one loop gain, the separation between common and relative returns, and the elasticity-based signs of the levers are coherent and useful results. The distinction between an instability threshold and the speed at which a gap opens is particularly important. The enforcement inequality itself is correct under its stated one-period timing and credible-continuation premises. Treating real-world co-movement as C0 is a real improvement.

Two central extensions still exceed what is proved. First, a local deterministic resolvent is presented as an exact strategic standing price, while the supporting computations solve a stochastic lottery whose continuation value is not determined by derivatives at parity. This is a theorem/model mismatch, not merely a request to run a finer grid. Second, an actual time to breakout is inserted into a one-period absorbing-state game through escape probability alone; this leaves the timing and discounting of the successful and punished branches out of the enforcement calculation. Both errors affect interfaces advertised as proved.

There are also narrower repairs: the convergence part of Proposition 3.4 needs cumulative selection, the strict narrowing statement excludes the purely relative endpoint, the frontier-switch claim must compare destruction with rest, and the common-benefit trait result needs its proof's common-background premise in its statement.

## Findings at a glance

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

## F1. The strategic standing price is not an exact local resolvent for the lottery game

**Locations.** `THEORY.md:138` (Proposition 2.2(4)); `THEORY.md:140` (numerical strategic interpretation); `THEORY.md:271` (Proposition 3.9 strategic scope); `SUPPLEMENT.md:119–121` (proof); `SUPPLEMENT.md:139–158` (strategic computations, especially 140 and 153); `SUPPLEMENT.md:298` (finite-jump exactness and strategic price); `SUPPLEMENT.md:1104–1105` (interface status). Register: `CLAIMS.md:60`, `CLAIMS.md:74`, `CLAIMS.md:224`. Keys: `loopgain`, `eqgain`, `standprice`.

### The three mathematical objects need separate names

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

### An exact counterexample without strategic response or numerical error

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

### Independent strategic calculation

The script independently solves the manuscript's two-player Tullock lottery using Bellman iteration and the analytically solved within-state effort game. It separately measures the conditional-drift elasticity, the frozen-own-effort elasticity, the prize secant premium, and the infinitesimal stock-injection value. For r=4, structural Γ=0.45, d=0.1, δ=1/1.1:

| Grid cells | Bellman residual | Γδᵖʳ | Local formula Γδᵖʳ/(1−Γδᵖʳ) | Actual prize premium | Marginal injected-stock value |
|---:|---:|---:|---:|---:|---:|
| 800 | <10⁻¹² | 0.384993 | 0.625998 | 0.503215 | 0.508360 |
| 1,600 | <10⁻¹² | 0.394690 | 0.652046 | 0.513744 | 0.519680 |
| 3,200 | <10⁻¹² | 0.397860 | 0.660742 | 0.516436 | 0.522543 |

The theorem's discounted-gain condition is satisfied in every row. Refining the grid does not remove the difference; the local formula exceeds the prize premium by about 28% in the finest run. This is consistent with, and sharper than, the manuscript's own report at `SUPPLEMENT.md:153` of 0.64 versus 0.51.

Adding a requirement that the conditional mean dynamics be stable does not make the equality exact. At structural Γ=0.3 the independently computed equilibrium Γ is about 0.353<1. At 3,200 cells the local formula is 0.195145, the prize premium 0.194093, and the marginal injection value 0.194167. The small difference is still structural: a theorem of exact equality cannot be validated by a 0.5% acceptance tolerance.

Block MP's own assertions in `checks_v62.py:1967–1971` accept 2.5% error for a selected set and 0.6% for another subset. The larger discrepancies are excluded from that assertion rather than explained by the printed theorem's premises. The tests can pass while the theorem fails.

### Stability is also a different stochastic claim

The rank-one proof for the derivative of equilibrium win shares is good. It gives the stability of the deterministic share map, or the derivative of the lottery's conditional expected one-step drift. It does not establish local asymptotic stability of a random path at parity. Starting exactly at parity in a nondegenerate lottery immediately produces a gap regardless of whether Γᵉᑫ is above or below one; symmetry can keep the unconditional signed mean at zero while dispersion grows. The manuscript should call the measured MP quantity a drift instability, and separately specify any claim about stationary dispersion, escape probabilities, or almost-sure dynamics.

### Minimal repair

- State explicitly that Proposition 2.2(1)–(3) uses deterministic prize shares, or a separately justified deterministic mean approximation.
- Retain the exact rank-one result for differentiable deterministic equilibrium share dynamics.
- Restrict the exact strategic price result to a deterministic invariant symmetric reference with a valid local envelope closure; add the assumptions required for that closure instead of assuming policy differentiability suffices.
- For the lottery, replace the exact scalar price claim by the Bellman-envelope equation above. Label the scalar formula a local/small-jump approximation unless an error bound is proved.
- Define the marginal stock-injection value and the finite win-versus-loss premium separately. The reported MP ratios can remain numerical observations for the premium they actually compute.
- Change the relevant interface and register entries from “form proved” to the appropriate split status. An “outside review” tag on magnitudes does not repair an overbroad theorem about their form.

The qualitative discovery that rivals' responses can greatly amplify a prize premium remains supported by the calculations. The defect concerns exact closure and the interpretation of stability, not the existence of discouragement in these examples.

## F2. A slow breakout requires discounted timing, not escape probability alone

**Locations.** `THEORY.md:457` (success is decisive from the next period); `THEORY.md:468` (slow breakout folded into p_d); `THEORY.md:472` (Remark 5.5); `SUPPLEMENT.md:462–468` (derivation and check); `SUPPLEMENT.md:544–550` (joint scissors); `SUPPLEMENT.md:1106` (join marked proved). Keys: `enforce`, `detectlink`, `scissors`, `jointscissors`.

The identity p_d=1−υ(T_dec) is correct when υ is the probability of detection and response by the decisive time. The inference that substituting this probability into equation (14) is an exact enforcement test for the resulting delayed game does not follow.

Equation (14) values the successful absorbing branch and the punishment branch from the next period. In a delayed game, those branches begin at different random dates. The interim flow payoffs, δ raised to the arrival time, and correlation between arrival time and outcome matter. The probability of escaping detection supplies none of these quantities.

### A reversal of the deterrence conclusion

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

### Minimal repair

Retain the escape-probability identity. Then choose one of two explicit formulations:

1. Use one macro-period to include the entire race-to-detection experiment, and define g, D, v, and the effective discount consistently as payoffs/continuation values at the end of that macro-period; or
2. Keep ordinary time and use the expected discounted continuation value of each branch, including interim payoffs and the timing distribution. For the example above, the successful continuation from t=1 is C(1−δ⁷)+δ⁷D, not D.

Under either repair the probability-to-incentive bridge is conditional on those definitions. T_dec then changes both the escape probability and the discounted continuation values. The qualitative claim that faster breakout can worsen enforcement may survive, but it is not proved by differentiating p_d alone while retaining invariant per-period terminal values. Update S13 and the joint-model labels accordingly.

## F3. Proposition 3.4 needs cumulative selection, not merely payoff-monotonicity

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

## F4. The strict narrowing theorem misses the purely relative endpoint

**Locations.** `THEORY.md:234–235` (allowed θ domain); `THEORY.md:263–269` (Proposition 3.9); `SUPPLEMENT.md:279–281` (strict inequality argument); `SUPPLEMENT.md:540` (derivative sign). Key: `standprice`, with propagation to `scissors`.

The theorem assumes θ₀<n−1, while the globally declared domain includes θ₀=−1. At θ₀=−1 the common coefficient is already zero. Equation (9) gives θ=−1 for every admissible pair of gains, whether relative return is larger, smaller, or equal.

For example, n=4, θ₀=−1, Γδ=1/2, Γδᶜ=0 gives θ=−1, not θ<θ₀. The phrases “whatever θ₀<n−1,” “narrows whenever,” “widens where they do not,” and “no held self-model short of θ₀=n−1 escapes the narrowing” are therefore false at this permitted endpoint.

The fixed-prize derivative is proportional to

\[
-\frac{n(1+\theta_0)(n-1-\theta_0)}{[n-(1+\theta_0)\Gamma_\delta]^2},
\]

which vanishes at θ₀=−1. The proof at `SUPPLEMENT.md:540` reports only the other factor's sign.

**Minimal repair:** make the strict iff claim for −1<θ₀<n−1. Add that both endpoints are invariant: θ₀=−1 remains purely relative and θ₀=n−1 remains fully inclusive under the common/relative rescaling. Where endpoints are retained, state weak monotonicity. The interior theorem and its policy relevance remain intact.

## F5. The frontier switch must beat rest as well as expansion

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

## F6. The global-benefit trait result needs its proof's common background

**Locations.** `THEORY.md:281–285`; `SUPPLEMENT.md:304`; `CLAIMS.md:76`. Key: `onegroup`.

The proof writes π_j=π₀+b z̄−c z_j, with one common π₀. That makes payoff, and therefore fitness under the maintained monotonicity premise, decreasing in z alone. Under this model the Chebyshev covariance argument is correct, including the corrected distinction between total/within-group signs and the potentially positive between-group term under nonlinear fitness.

The theorem's prose only says that the trait costs its bearer and benefits everyone equally. It does not exclude correlated private background advantages. Those are enough to reverse total selection without transmission bias or a changed rule.

Take two equally weighted carriers with traits z=(0,1), backgrounds φ=(0,2), cost c=1, and the same global benefit 0.5 to each. Payoffs are (0.5,1.5), so Cov(z,π)=0.25>0. The trait bearer pays the stated cost and supplies an equal global benefit; it still expands because the associated background advantage is larger than the cost.

**Minimal repair:** state the result for otherwise identical carriers or for the partial selection effect of the trait holding background fitness fixed. More generally, with π=φ+b z̄−cz and affine fitness, total selection has sign Cov(φ,z)−c Var(z), so a no-positive-background-covariance premise suffices. The downstream institutional prose should distinguish “the globally common benefit alone supplies no differential selection advantage” from “a costly globally beneficial rule can never spread through selection.” The first is established; the second needs the extra premise.

This repair does not rescue undifferentiated selection as a reliable source of global protection. It makes the precise mathematical statement match the proof rather than claiming that all correlated routes have been excluded.

## F-C1. The won-share pivot is exact for fixed decisiveness, not for every stock channel

**Locations.** `THEORY.md:555–561`; `SUPPLEMENT.md:540`; contrast the correct elasticity result at `SUPPLEMENT.md:162–168`. Keys: `scissors`, `chansign`.

The ratio-channel capacity model has fixed r. There Γ and Γδ are proportional to ω with the other parameters fixed, and provision growing in proportion to stakes holds this capacity contribution fixed. The reduced joint models explicitly use this case and correctly demonstrate it.

The multi-channel generalization must preserve the condition that each r_j remains fixed. For a linear level channel σ=aX, decisiveness is r=aX*, so keeping ω fixed while raising both stakes and provision raises r and the gain. Take n=2, κ=a=1, d=0.2, β=δ_f=0, and k₀=Ω/2. Then ω=1/2 at every scale, X*=5Ω, and Γ=2.5Ω. Raising Ω from 0.2 to 0.8 while provision keeps exact pace moves Γ from 0.5 to 2.0.

This is already explained by Proposition S2.4, which says that provision changes no gain in a linear level channel. Consequently, the unqualified multi-channel sentence that “provision that grows with the stakes holds both still” is too broad. It should read as a property of the fixed-decisiveness capacity channel or of the two stated reduced models. It cannot cover rule-support channels without additional correction that offsets their scale dependence.

This is a scope clarification, not a rejection of the new channel-by-channel theorem. The new theorem is exactly what diagnoses the overextension.

## F-C2. The “game is wrong” welfare step needs a stage-versus-dynamic distinction

**Locations.** `THEORY.md:249–253` (Proposition 3.6); `THEORY.md:275` (Remark 3.10); `SUPPLEMENT.md:261`, `SUPPLEMENT.md:294`. Keys: `boundary`, `twoerrors`.

Proposition 3.6(1) proves a useful symmetric *stage* welfare comparison: as a common θ rises, equilibrium intensity falls, and the common flow welfare rises. Proposition 3.9 then computes a first-order continuation-induced weight under fixed rival conduct. Substituting the resulting lower θ into the static contest establishes the stated stage comparison.

It does not, without another construction, compare lifetime welfare between two fully specified dynamic equilibria in which net payoffs change capital stocks, prize growth, future intensities, and rivals' continuation responses. S13 appropriately acknowledges that the full stochastic game is open. The sentence at line 275 should specify “in the symmetric stage comparison of Proposition 3.6” or supply the dynamic welfare argument with a common feasible comparison path.

The stage-level interpretation is valid and supports a collective-action problem. It should not quietly carry the evidentiary weight of a solved dynamic welfare theorem. This clarification is especially useful because the rhetorical claim “each actor computes correctly; the game is wrong” is now a major part of the argument's front matter.

## Results that survived adversarial review

### Structural loop gain

At a deterministic symmetric steady state, the relative Jacobian really is D+uvᵀ/n. The conditions d_j+δ_f,j≤1 and nonnegative conversions and marginal strength make it a nonnegative matrix. Its secular equation at eigenvalue one gives the printed Γ criterion, including the case of inactive channels. The common-stock deviations decay separately under a fixed prize. This result does not require strategic optimization, and it does not claim global concentration.

The proposition's exclusions of countervailing channels and different decisions feeding different stocks are substantive, not cosmetic. A negative delayed channel can destabilize a system whose signed “net gain” is below one; the displayed two-channel example correctly has complex roots of modulus greater than one. There is no valid objection that correction should simply be subtracted from Γ.

### Discounted structural price and growing prizes

For the deterministic invariant reference, Sherman–Morrison yields the stated relative price on Γδ<1. The resolvent domain is the discounted instability condition, so structural Γ>1 alone does not invalidate a finite first-order discounted price. An objection that the price must fail whenever the undiscounted parity point is unstable should be rejected.

The common-mode Jacobian for an endogenous prize is diag(1−d_j)+κgᵀ. Diffusion cancels from this mode and remains in the relative mode. Decomposing today's payoff shock and matching the two coefficients gives equation (9). Apart from the endpoint correction in F4, the interior sign comparison is right. The fixed-prize model narrows the working weight wherever its relative return is positive; proportional prizes do not justify that same universal statement.

For Ω=gS with no provision, the common and relative absolute-stock multipliers are 1−d+κg and 1−d−δ_f+(1−β)rκg. The share multiplier is their ratio. Without diffusion, the interior narrowing threshold and the instability of equal shares both reduce to (1−β)r>1. With diffusion, their thresholds differ exactly as stated, and the gap is positive on the finite-value domain. The new growing-prize correction is mathematically meaningful.

### Channel levers

Writing a channel term as a constant times h'(X*)/(d+δ_f) makes the elasticity result transparent. Provision affects X*; decay affects both X* and persistence. The printed signs in Proposition S2.4 follow. In particular, faster depreciation does not reduce the undiscounted gain of a pure ratio channel without diffusion, raises it with diffusion, and raises its discounted gain at δ>0. Correction in a linear level channel lowers both gains. The intuition that “faster decay always weakens compounding” is false in the maintained stationary ratio model and should not be reintroduced.

Small boundary conventions should be made explicit when wording is strict: at δ=0 all discounted gains vanish, and at a channel of zero conversion or zero decisiveness no lever can strictly lower that zero contribution. These do not alter the interior comparative statics.

### The point of enough

The local cap-equality threshold with the restored diffusion term re-derives correctly. The fixed-opponent map is monotone under d+δ_f≤1, so the positivity of φ on the entire interval is an appropriate global-return condition. The distinction between local return just below a cap and return from every start is essential and now correctly represented. Diffusion is a source of rank-independent inflow and is not sufficient by itself to eliminate an interior trap.

“Return” should mean convergence as well as finite hitting: when the cap is exactly K*, a laggard may approach it asymptotically. This is a terminology point rather than a failure of the local condition.

### Enforcement inequality and relative punishment

The one-period deviation valuation that produces equation (14) is correct. The comparative statics of the threshold, homogeneity in all payoff quantities, distinction between D<C, D=C and D>C, and punishment-race continuation formula are all algebraically sound. The repair that permits breakouts during punishment is important: setting punishment value equal to the no-breakout stage payoff would overstate deterrence in the manuscript's example.

Credibility remains essential and is now stated. The numerical agreement between a fixed discounted stream and (14) is an identity check, while an optimal deviation-plan computation is an incentive check; the manuscript increasingly distinguishes these correctly.

The two-player relative-objective mirroring argument is valid for an exchangeable continuation starting in an unlabelled symmetric state. It is not defeated by rock–paper–scissors or by allowing mixed actions. Label-dependent continuations and role-differentiated punishers with at least three actors can escape the bound, and the manuscript now states both. A fresh review should not recycle those already-addressed objections as new findings.

### Scissors arms and their limitations

Within the one-channel fixed-ratio model, increasing ω raises the linearized gap multiplier. The time-to-threshold formula is a local extrapolation, not a global hitting-time theorem; the text now acknowledges that diffusion can prevent the decisive gap from being reached.

The objective arm is algebraically correct when a deviation lowers the mean, raises the actor relative to it, punishment is a lower symmetric profile, and D−C does not fall as the objective narrows. Those premises supply the monotone changes of temptation and sanction. The sanction and stakes arms are also correct partial comparative statics. They do not prove co-movement in a complete strategic system.

Registering co-movement as C0 and presenting the joint calculations as reduced numerical models are appropriate. The outstanding issues are the exactness of the strategic-price interface, the time compression in F2, and the generalization of the fixed-ratio pivot in F-C1—not the mere absence of a universal whole-world scissors theorem, which the manuscript no longer claims.

### Survival and communication

The conditional-hazard lemma does not require independence between rounds when the stated bounds hold on every surviving history. Under uniformly vanishing contestable coverage and a positive residual floor, the survival bound follows; hazardous-variety growth is not needed in that proof. The manuscript now identifies it as motivation rather than an unused theorem premise. Objections that merely remove the residual floor or assume AI restores coverage change an explicit premise and are applicability tests, not theorem counterexamples.

The shared-self-model cheap-talk ideal-point difference re-derives to b₀(n−1−θ)/(n−1+θ) when the common curvature is negative. The n≥3 relative endpoint yields b₀n/(n−2); the two-player endpoint is degenerate and must be treated separately, as it is. Under zero material bias, informative communication need not disappear among three or more actors, and the supplement already recognizes this.

## Numerical and proof workflow recommendations

1. Keep the current 188 checks, but stop treating their count as certification of theorem scope. In particular, approximate matching within 2.5% cannot certify an exact strategic-price theorem.
2. Separate deterministic share dynamics, conditional drift of a lottery, and the lottery's value function into distinct result and test names.
3. Add exact boundary tests: θ₀=−1, δ=0 when permitted, destruction versus rest, and a payoff-monotone rule with integrable actual selection strength.
4. Add a timing-aware stochastic enforcement example in which actual stopping times—not only the escape event—enter discounted streams.
5. Preserve rejected-objection records: global concentration is not implied by Γ>1; global real-world scissors closure is C0; diffusion is not a universal cap rescue; the residual-risk floor is a premise; an absorbing winner can value cooperation more than victory; stochastic punishment must be credible.
6. Reconcile the proof/status tables after the mathematical fixes. At present, `CLAIMS.md` and S13 call some forms proved while the supplement's numerical discussion openly reports their failure to match. The candid numerical discussion should be retained; the theorem should be narrowed to meet it.

## Disposition of the earlier review issues within this audit's scope

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

## Reproduction

From the V6.2 directory:

```sh
python3 reviews/formal-audit/independent_audit.py > reviews/formal-audit/results.json
```

The output includes the exact lottery counterexample, the slow-breakout deterrence reversal, the payoff-monotone host counterexample, the relative-objective endpoint, the frontier/rest comparison, the trait/background covariance, the level-channel scaling example, and independent Bellman calculations at three grid resolutions. Six assertions guard the central numerical directions. Bellman convergence on a grid is numerical evidence, not a proof of existence of a smooth continuous-state equilibrium; the analytic lottery example and Bellman derivative identity establish the underlying model distinction independently of that existence question.

The most economical revision preserves the deterministic backbone, limits the strategic-price theorem, restores discounted timing at the enforcement interface, and applies the stated small repairs. It does not require discarding the theory's central account of relative selection or its newly corrected channel-specific levers.
