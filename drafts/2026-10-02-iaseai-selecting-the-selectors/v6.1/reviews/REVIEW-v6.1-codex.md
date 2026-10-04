# V6.1 review: repair the boundaries and the connections between models

Prepared for Ren on 4 October 2026, following the request for another review round. Reviewed the actual V6.1 core, Supplement, claim and test registers, relevant build/check scripts, and the changes from the previous Codex review. Parallel reviews covered the new mathematics, AI/alignment and requirements, and systems/capture and judgment.

**V6.1 is a substantial repair. Keep its architecture. It needs a focused mathematical and consistency pass before its strongest claims can be endorsed.** The previous enforcement error is genuinely fixed. The largest remaining problems are in the new loop-gain results, the connections between parameters in different models, and assumptions lost between a full proof and its compressed statement.

This is a targeted review of the new formal core and the argument it supports, not a certification of every inherited result or of the unverified references. No manuscript or source file was edited, and nothing was committed. The original files are recorded in [snapshot-v61-codex.json](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/reviews/snapshot-v61-codex.json).

I ran the structure checker and all 25 numerical blocks in a temporary copy, because `xref_v61.py` rebuilds documents. Both commands exited successfully; the numerical run took about 50 seconds. Logs: [structure](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/reviews/xref-v61-codex.log), [numerics](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/reviews/checks-v61-codex.log). The independent [counterexample script](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/reviews/counterexamples_v61_codex.py) passes all its assertions. These computations check the examples below; they do not estimate real-world parameters.

## What the previous review can now close

| Previous problem | V6.1 status |
|---|---|
| Decisive continuation valued on the wrong side of cooperation; attainability confused with certainty | **Repaired.** Equation (14) includes the breakout term and separates $p_d>0$ from $p_d\to1$. |
| Enforcement check defined sustainability by the disputed inequality | **Repaired.** EC independently evaluates discounted values, including both earlier counterexamples. Its credibility assumptions remain separate from numerical valuation. |
| Universal rule equated with identical additive cost | **Lemma substantially repaired.** Incidence and evasion are now explicit. A necessity overstatement persists downstream in R8. |
| Price decomposition omitted transmission and local experimentation | **Repaired.** The revised proof includes transmission and distinguishes global from local benefits. A new fitness-scope issue is listed below. |
| Requirements mixed finite-horizon necessity, sufficient safeguards and values | **Substantially repaired.** R1, R3 and R7 now make those distinctions. Some summaries and R8 remain inconsistent. |
| A zero sum among many actors used to prohibit all communication | **Formal treatment improved.** Third-party interests and an explicit informative-communication model are included. “Rivals fall silent” still needs its model conditions. |
| Export controls classified as not changing selection | **Repaired.** Profiles now record the direction of selection change. |
| Protection standard claimed to establish a ranking it had not computed | **Substantially repaired.** Whole-design ranking is explicitly a judgment. One reason given for that judgment still excludes admitted failure modes. |
| Need-directed growth itself claimed to bound hazardous variety | **Repaired.** The connection to a deliberate bound is now a design hypothesis. |

The improved separation of mechanism, diagnosis and judgment is worth keeping. Another reorganization would not fix the remaining issues more efficiently.

## Findings affecting central claims

### 1. High priority — the standing-value formula is used outside its convergence domain

Locations: [THEORY:114](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/THEORY.md:114), [THEORY:232–236](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/THEORY.md:232); [SUPPLEMENT:58](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/SUPPLEMENT.md:58). Keys: `loopgain`, `standprice`.

The Supplement correctly says the series giving the price of standing converges **iff $\Gamma_\delta<1$**. Neither main proposition includes that restriction. The inequality $\Gamma_\delta<\Gamma$ does not imply it.

Within the stated model, set

$$n=2,\quad\Omega=\kappa=1,\quad d=.2,\quad r=2,\quad
\beta=k_0=\delta_f=0,\quad\delta=.9.$$

Then $K^*=2.5$, $\Gamma=2$, and $\Gamma_\delta=9/7$. The printed value multiplier becomes

$$\frac{\Gamma_\delta}{1-\Gamma_\delta}=-4.5.$$

But a positive relative-capacity perturbation increases every future winning. Directly evolving the nonlinear stock model from $(2.50001,2.49999)$ gives a **positive** discounted advantage, approximately $.0107012$. The linearized infinite-horizon derivative diverges; it does not become negative.

This matters for the central claim that compounding manufactures a relative objective in “every forward-looking actor.” The derived transformation is a local result inside a specified convergence region, with a limit taken **from below**. It cannot be extrapolated through the singularity into the strongest compounding regimes. The numerical checks restrict the tested present-value region and therefore do not validate that extrapolation.

**Repair:** state $0\le\Gamma_\delta<1$ in both propositions and all summaries relying on them. Write $\Gamma_\delta\to1^-$ for the limit. Outside that region, use a finite-horizon derivative or the nonlinear value function. Retain the broader insight that reinvestment gives relative gains additional instrumental value, without claiming a universal objective transformation.

### 2. High priority — the shared-parameter table transfers a correction sign that is not generally true

Locations: [THEORY:83](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/THEORY.md:83), [THEORY:575](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/THEORY.md:575), Equation (2); related Test Γ at [THEORY:633](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/THEORY.md:633) and [TESTS:71](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/TESTS.md:71).

For the explicitly permitted strength function $\sigma=r\ln K$, with fixed $r,\omega,\delta_f$,

$$\Gamma=(1-\beta)r\omega\frac{d}{d+\delta_f}.$$

Increasing stock decay $d$ **raises** this gain when diffusion is positive; without diffusion it leaves the gain unchanged. The discounted gain also rises. Set $r=1.8$, $\beta=k_0=0$, $\delta_f=.1$, $\delta=.9$. Raising $d$ from $.1$ to $.2$ moves

$$\Gamma:.9\longrightarrow1.2,\qquad
\Gamma_\delta:.578571\longrightarrow.875676.$$

Equal standing changes from locally stable to unstable. The table assigns the opposite sign.

Damping an additive rule-support stock can have the claimed effect: for $\sigma=aZ$, the equilibrium elasticity $r=aZ^*$ itself falls with decay. That requires a particular channel and functional form. Stock depreciation in Equation (1) and correction of institutional capture in Equation (12) cannot be identified merely because both use $d$.

**Repair:** separate these interventions and derive their signs with the strength function stated. Label cross-model connections as assumptions where no common model establishes them. This is central to the new interconnection claim, not a notation-only correction.

Test Γ also points the wrong way for the normalized common-channel weight. More provision lowers $\Gamma_\delta$ and raises $\theta_\Gamma$, restoring weight to shared consequences. The test currently predicts sensitivity to shared harm **falls** with provision and diffusion. Define the observable first: raw effort elasticity need not be globally monotone. For the stated contest, the ratio of marginal effort responses to shared harm and private cost is $1+\theta_\Gamma$, which provides a precise possible target.

### 3. High priority — the cap result fails at equality and its proof drops diffusion

Locations: [THEORY:120–126](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/THEORY.md:120); [SUPPLEMENT:85–87](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/SUPPLEMENT.md:85). Key: `compound`.

**Equality is not covered by the claimed local guarantee.** Set $n=2$, $\kappa\Omega=1$, $d=.2$, $r=3$, and $\beta=k_0=\delta_f=0$. The equal-standing capacity is $K^*=2.5$. With cap $\bar K=K^*$ and initial stocks $(2.499,2.5)$, the next stocks are

$$ (2.49889994,\ 2.5). $$

The laggard moves away from equality and falls to about $2.4\times10^{-32}$ after 400 periods. The proof treats $\phi(\bar K)=0$ as enough for local stability; the sign immediately below the cap matters. A strictly lower cap avoids this particular boundary error.

**Diffusion is present in the model but absent from the laggard equation.** With the other actors at the cap, the missing term is

$$\delta_f\frac{n-1}{n}(\bar K-K).$$

For $n=2$, $r=2$, $d=.2$, $\delta_f=.6$, $\bar K=2.5$, $\kappa\Omega=1$, and no sharing or provision, the laggard's net inflow, writing $s=K/\bar K$, is

$$\phi(K)=\frac{(1-s)(1.25s^2-.5s+.75)}{1+s^2}>0
\quad(0<s<1).$$

Direct joint simulation from $(.01,2.5)$ restores both actors to the cap. Thus diffusion can supply recovery without either sharing or outside provision. The asserted necessity of those two sources is false when diffusion is allowed. The existing cap checks use strictly lower caps and zero diffusion, missing both cases.

**Repair:** use $\bar K<K^*$ for the simple local guarantee; analyze equality separately; restore diffusion in the inflow criterion. Restrict necessity of sharing/provision to the zero-diffusion case. The positive case for provision remains, but it is one mechanism supplying a restorative flow, not the only one in the stated model.

### 4. High priority — the falling linear-cost component contradicts the correction rate law

Locations: [THEORY:315–316](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/THEORY.md:315), [SUPPLEMENT:177](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/SUPPLEMENT.md:177), R3a at 736. Key: `corrrate`.

Part (2) applies the threshold $\alpha_{\rm ctl}/(1+\eta)$ when $f=0$ **or falling**. Part (3) gives a different threshold when positive $f$ falls. The full optimum is

$$q^*(t)=\left[
\frac{\chi\hat Y/d(t)-f(t)p^{\xi_f}}{\gamma(t)p^{\xi_v}}
\right]_+^{1/\eta}.$$

For an explicit counterexample, set $\eta=p=\chi\hat Y=c_{\rm ev}=a_{\rm ev}\hat B=1$, $A=0$, and

$$\gamma=e^{-.2t},\qquad d=2e^{.05t},\qquad f=.49e^{-.01t}.$$

Correction grows at $.05<.1$, so part (2) predicts eventual certificate failure. Instead,

$$q^*(t)=[.5e^{-.05t}-.49e^{-.01t}]_+e^{.2t}$$

decreases from $.01$ to zero at $t\approx.50507$. The row gain $G_{m ev}=q^*/d$ starts at $.005$, decreases, and remains zero thereafter. The certificate never fails. The cost of cultivation falls, but its marginal benefit falls faster than the positive linear cost component.

**Repair:** restrict part (2) to $f=0$. State the positive, falling-$f$ branch separately, with its threshold and boundary/amplitude conditions, and propagate the distinction to R3a and Theorem 4.12. The Supplement's sentence saying $\chi\hat Y/(fp^{\xi_f})$ “falls” under falling $f$ also has its sign reversed. The unrun joint simulation is a useful future study, but this counterexample already occurs inside the assumed quasi-static model.

### 5. High priority — equal incidence is still falsely necessary for sustained compliance

Locations: [THEORY:523](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/THEORY.md:523), [R8 at 742](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/THEORY.md:742), SUPPLEMENT:409, CLAIMS dependency chain. Keys: `blind`, `nested`, `require`.

The revised equal-incidence lemma is useful. Its neutrality condition is still imported into R8 as a necessary condition for keeping unsafe variants out.

Consider two developer types, both with baseline payoff 1. Compliance costs $.1$ and $.2$ respectively; either type's evasion has expected sanction 1. Their four variants have payoffs

$$ (A_C,A_E,B_C,B_E)=(.9,0,.8,0). $$

From positive initial shares, replicator selection eliminates both evading variants. The cheaper compliant type displaces the more expensive compliant type, and the compliant share tends to one. At $t=20$, starting from equal shares, it is about $.999999973$. Compliance survives unequal incidence perfectly well.

**Repair:** distinguish preserving relative shares among compliant firms from preserving compliance. Equal incidence is sufficient for the former identity and unnecessary for the latter outcome. Safety requires the relevant unsafe alternatives to be excluded or unprofitable under enforceable rules; it need not preserve every compliant firm's market position.

A second premise should be explicit in Proposition 6.7. A positive **marginal** alignment tax does not by itself imply that safeguarding developers disappear against heterogeneous competitors. A safeguarded developer with baseline 2 and tax $.1$ outgrows an unsafe developer with baseline 1. To derive extinction, specify a matched unsafe variant in the support with an unbounded cumulative advantage, or a uniform payoff gap between the competing populations. If the general symmetry convention is intended to provide matched baselines here, state that directly in this selection result. Zero tax gives neutrality; it does not alone make a safeguard spread, as line 525 says.

### 6. Medium priority — stage imitation no longer bounds the full stochastic punishment value

Locations: [THEORY:402](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/THEORY.md:402), [SUPPLEMENT:233](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/SUPPLEMENT.md:233). Key: `relpunish`.

The repaired enforcement proposition correctly defines $v_i$ in the full stochastic continuation game. The imitation proof still infers $v_i\ge0$ from equality of current stage payoffs. Imitating an action need not copy the opponent's continuation state or breakout opportunities.

Take a symmetric material prisoner's dilemma with $CC=(3,3)$, $DC=(4,0)$, $DD=(1,1)$ and purely relative objectives. Cooperation gives 0 and deviation gains 4. A deviation has no immediate breakout but labels the deviator as the punishment target. During punishment both play $D$, receiving 0 currently; each period a probability $.5$ gives the punisher an absorbing relative payoff $+10$ and the target $-10$. Actions do not affect this transition. Both playing $D$ is a credible continuation: it maximizes stage payoff, with action-independent continuation.

At $\delta=.9$, the target's normalized continuation value is $v=-8.1818$. Deviating from cooperation is worth

$$4+.9\frac{-8.1818}{.1}=-69.636<0.$$

Two relative actors can therefore sustain non-stage cooperation in this symmetric-stage but role-dependent continuation game. This is a model counterexample, not a claim that such sanctions are available in the world.

**Repair:** require symmetry/exchangeability of the entire relevant continuation state and transitions, or restrict the corollary to ordinary repeated-stage punishments without asymmetric breakout opportunities. The new race-reversion formula likewise needs an actually credible stochastic continuation; being a stage equilibrium alone is insufficient if actions change breakout chances.

## Other definite corrections

| Location | Finding and minimal repair |
|---|---|
| [THEORY:505](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/THEORY.md:505), SUPPLEMENT:285; `delegatelock` | The compressed core loses **$p=1$**, which the full statement requires for “at least one of all/no delegation.” With $n=3,s=1,p=.1,q_L=0,\psi_0=0,\psi_1=.015$, delegation/nondelegation survival ratios for $k=0,1,2$ others delegating are $1.0025893,1.0009730,.9992754$. Neither extreme is an equilibrium; exactly two delegators is. Restore the condition. |
| [THEORY:244](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/THEORY.md:244), SUPPLEMENT:149; `onegroup` | The proof makes both Price selection terms non-positive for **affine fitness**, while the statement says every payoff-monotone rule. For groups $(0,1)$ and $(.4,.4)$ with fitness proportional to $e^{-5z}$, the between-group covariance is $+.00920084$ while total selection is $-.11495691$. Normalized exponential selection is relative and payoff-monotone. Restrict the every-partition result to the proved specification; the overall negative selection result can remain. |
| [THEORY:543](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/THEORY.md:543), CLAIMS:87; `topology` | Row sums below one are again called **necessary**, despite the repaired actual-basin counterexample and the sufficient classification at 744. They also certify asymptotic behavior in a capture model, not the absence of current control over appointments or statistical independence of errors. Use the same qualified sufficient-certificate statement throughout. |
| [THEORY:363](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/THEORY.md:363), versus 301, 305, 817 | The statement that success funding correctors it cannot control “is selected in the same way” conflicts with zero appropriability and with the revised whole-system maintenance account. Replace it with that newer account; generative persistence remains a conjecture. |
| [THEORY:190](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/THEORY.md:190), SUPPLEMENT:109 | Declining sanctions alone do not imply bistability. The proof also needs $s(0)>c>s(1)$. Keep those endpoint conditions in the core. |
| [TESTS:70](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/TESTS.md:70) | Test M introduces independent access/funding, sees correction work while leaders grow, and calls C2 refuted. That is a predicted successful-remedy branch. Relabel it as a remedy test and a reason to weaken the current diagnosis; test the conversion mechanism separately while accounting for changed correction. |

## The judgment needs one more symmetric comparison

The three-tier structure is a real improvement. At [THEORY:940](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/THEORY.md:940), however, the preference still rests partly on the claim that the cooperative design's worst case requires its certified correctors to fail.

Its own uncertainty range includes dissolution, coercive enforcement, service disruption, and collusion. These can cause protected losses even with valid institutional row-sum certificates. Measurability of capture parameters neither bounds these other risks nor establishes that the design keeps more corrective options open overall.

Keep the ranking explicitly a judgment, but give reasons that cover all admitted failure modes. The first-tier phrase “on any reading of the cruxes” also needs narrowing: C2 itself says new funding/access mandates can become unnecessary, while C9 can remove the need for particular common admission constraints. Distinguish continuing measurement and preparedness from activating a particular institutional mandate.

## What the checks establish, and what to do next

The numerical workflow has improved materially. Identity, independent, and derived blocks are labeled; the old circular enforcement validation has been replaced. The remaining counterexamples mostly fall outside the sampled cases: the standing-value calculation stays inside its convergence region; cap examples omit equality and diffusion; the delegation check uses $p=1$; Price checks use the affine fitness specification. Successful execution cannot supply those omitted assumptions to the core.

The most economical next pass is:

1. **Repair by stable key in `src/`.** Start with `loopgain`, `standprice`, `compound`, `corrrate`, `nested`, `relpunish`, `delegatelock`, `onegroup`, and `require`. Edit the keyed sources and regenerate; do not patch assembled documents alone.
2. **Keep the logical conditions in compressed statements.** Move derivations and examples to the Supplement, but retain convergence domains, horizon, symmetry, initial-state and functional-form conditions beside each result. The lost $p=1$ condition is a concrete cost of the last compression pass.
3. **Audit every cross-model arrow.** In the parameter table, specify the actual intervention, the variables held fixed, the model supplying the sign, and any unproved interface. A shared symbol is not a shared mechanism.
4. **Update the summaries and tests from the repaired statements.** In particular: Chinese guide, §1.2, claim boxes, R8, the §12 judgment, CLAIMS, and Tests Γ/M. Do not merely correct the Supplement while leaving a stronger headline in place.
5. **Add boundary and exclusion cases to the checks.** Include $\Gamma_\delta\ge1$, cap equality, positive diffusion, falling positive $f$, unequal compliance costs, stochastic punishment asymmetry, $p<1$, and nonlinear fitness. Then run the proposed joint capacity/field simulation as a separate test of the quasi-static approximation.

I would defer further length cutting until this pass is complete. The core can still be shortened, but its assumptions are part of its argument, not supplementary detail.

The central question remains strong: **can restraint remain incentive-compatible when success changes both the gains from defection and the institutions capable of correcting it?** V6.1 now has a correct enforcement condition and a useful local feedback calculation for that question. Give those results their exact domains, establish the connections between them, and let the institutional programme be tested against the same complete set of risks as its alternatives.
