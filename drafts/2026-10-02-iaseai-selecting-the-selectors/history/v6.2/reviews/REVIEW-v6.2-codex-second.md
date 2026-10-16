# V6.2: second independent review — keep the repairs, narrow the extensions

Prepared for Ren on 4 October 2026. This is an additional review alongside the existing review work, not a replacement for it. The separate filenames preserve the first review's outputs. No manuscript, register, or pre-existing script was edited; nothing was committed.

**V6.2 repairs most of the specific V6.1 counterexamples. Its fixed-prize structural model, the proportional-prize ratio-channel result, and the revised correction-rate law are substantially stronger. The generalizations to arbitrary balanced growth, responsive rivals, and delayed detection still exceed their proofs. Several policy conclusions also treat asymptotic or neutral results as stronger guarantees than they supply. I would retain the architecture and repair these claims before treating the version as mathematically settled.** Length is outside this review's scope.

Reviewed `THEORY.md` SHA-256:

```
f50fb6a1b0f71ce33374946ab77da607a9631998d390e619296e6549e6822872
```

All locations below refer to the frozen snapshot recorded in [snapshot-v62-codex-second.json](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/snapshot-v62-codex-second.json). The review used independent parallel audits of §§2–3, §§4–5, and the numerical harness/§11, with a separate audit of §§6–12 and their registers. Calculations were derived from the models, rather than adopted from the earlier V6.2 audit reports.

The default numerical run completed in about 290 seconds: **40 blocks, 188 assertions passed, zero failed** ([run log](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/codex-second/second-checks/checks-output.txt)). The structure checker also passed in a disposable copy with its required V6 bibliography present ([structure log](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/codex-second/xref.log)). Passing these checks does not settle the findings below. The independent [counterexample script](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/counterexamples_v62_codex_second.py) is standard-library-only and imports none of the manuscript's check implementation; [its assertions pass](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/counterexamples-v62-codex-second.log).

## What the V6.1 review can now close

| V6.1 finding | Status in this snapshot |
|---|---|
| Price of standing outside its convergence domain | **Closed for the fixed-prize structural model.** THEORY:135–137 and SUPPLEMENT:109–116 impose the domain, take the limit from below, and replace the negative multiplier outside it by a continuous value with infinite slope. The growing-prize and strategic extensions have separate problems below. |
| Wrong sign of correction | **Closed in the channel theorem.** S2 derives the signs with the strength function and stock elasticity specified. The ratio channel with diffusion has the formerly omitted adverse decay sign; linear rule-support channels have the intended restorative sign. Test Γ now uses the correctly signed response ratio, with a perception confound explicitly recorded. |
| Cap at equality; diffusion omitted | **Closed in Proposition 2.3.** The simple local guarantee uses a strict cap; equality is separated; the laggard inflow includes diffusion. Sharing/provision are no longer the only possible restorative flow. CE contains the old counterexamples. |
| Falling linear cost | **Closed in Proposition 4.5 and its proof; not fully propagated.** The basic rate law now requires no per-unit floor. Part (3) separates the growth-rate cases and permits transient failure even when cultivation eventually ends. Table 7.1 drops this restriction again; see Finding 7. |
| Equal incidence in R8 | **Closed as a necessity claim in R8.** R8a concerns compliance; R8b concerns neutrality among compliers. Proposition 6.7 now includes a matched unsafe variant. Unequal incidence can re-sort compliant types without restoring evasion. Equality of sanction and tax still supplies neutrality rather than elimination; see Finding 6. |
| Stochastic punishment | **Substantially closed.** Corollary 5.6 requires exchangeability of the relevant continuation state and transitions and expressly excludes the labeled-target example. The text also warns that stage-race reversion need not be credible when quitting pays. The separate optimal-penal-code existence claim remains unverified by this review. |
| Missing `p=1` in delegation | **Closed.** Proposition 6.4 states `p=1` for the all-or-none claim, separates `p<1`, and reproduces the interior-number counterexample. |
| Affine fitness in the old Lemma 3.10 | **Closed.** Renumbered Lemma 3.11 restricts the between-group sign to affine fitness while preserving the total/within-group result. |
| Row sums called necessary | **The necessity wording is closed; the guarantee is still overstated.** THEORY:655 now says sufficient, not necessary, and separates error correlation. It still reads eventual decay as present independence; see Finding 5. |
| Old line 363: success financing correction it cannot appropriate | **Closed in the revised account.** THEORY:352 identifies the private selection cost, while maintenance through the shared system is distinguished from a proof that a generative order attracts. |
| Missing sanction endpoints `s(0)>c>s(1)` | **Closed.** Lemma 3.3(3), THEORY:219, retains both endpoints and distinguishes the one-basin cases. |
| Test M counted a successful remedy as a refutation | **Closed.** TESTS:131 distinguishes favorable present institutions, successful new mandates, and a mandate that fails its stress test. |

These are real repairs. The remaining findings do not justify undoing them.

## Findings by priority

### 1. High — a balanced growth path does not make the general standing-price Jacobian constant

Locations: [THEORY:263](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:263)–269; SUPPLEMENT:267–275, 300. Key: `standprice`.

The general statement allows every increasing strength function of Proposition 2.2 and a prize proportional to total stocks. It evaluates the gains at one reference state and sums a geometric resolvent. Balanced growth of the stocks does not imply that their elasticities, and therefore the linearized relative dynamics, stay constant.

Take two actors, one stock, strength `σ_i=K_i`, prize `Ω=K_1+K_2`, conversion `κ=.2`, depreciation `d=.1`, discount `.8`, and no sharing, provision, or diffusion. At the start of the continuation let equal stocks be one. The balanced path is

\[
K_t=1.1^t,
\]

but its strength elasticity is `r_t=K_t`, not a constant. At the reference state both printed discounted gains are `4/7`, so the printed formula assigns both returns the finite value `4/3`.

For a zero-sum stock displacement `u_t`, however,

\[
u_{t+1}=(.9+.2K_t)u_t,
\qquad \Delta w_{i,t}=K_tu_t.
\]

The relative derivative sum diverges: its successive discounted terms have an eventual ratio `.8·1.1·(.9+.2·1.1^t)`, which exceeds one and grows without bound. The common derivative remains `4/3`. Using the same continuation indexing as the resolvent, independent relative derivative partial sums are `1.80051` at 10 periods, `27.47743` at 20, and about `122097.22` at 30, already incompatible with the alleged infinite sum `1.33333`.

This is a failure of the **general balanced-path closed form**. The one-channel ratio-strength case in Proposition 3.9(2), `p_i∝K_i^r`, has constant linearized coefficients and survives this objection.

**Repair:** restrict the closed form to steady reference states or balanced paths whose linearized coefficients are constant, with the required homogeneity stated. For general balanced paths, use products of time-dependent Jacobians and a corresponding convergence condition. Preserve the relative-versus-common decomposition, which remains useful. Do not use a gain below one at the initial point as a convergence certificate for a changing sequence of gains.

### 2. High — the responsive-rival price proof loses a derivative, and its stochastic check claims an exactness it does not have

Locations: [THEORY:138](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:138)–140, 271; SUPPLEMENT:119–121, 139–140, 298. Key: `loopgain`, strategic part of `standprice`.

There are two distinct issues.

**The price half does not follow from the symmetry argument used for stability.** When all actors respond symmetrically, own and cross partials obey `a+(n−1)b=0`; the relative-state stability reduction is sound under its stated nonnegativity premise. Freezing just one actor's intensity destroys that symmetry. Conservation of total winning probabilities does not restore the missing identity for that actor's row of derivatives.

A small final-stage contest exposes the faulty derivative step. Let

\[
p_i=\frac{e^{K_ie_i}}{e^{K_1e_1}+e^{K_2e_2}},
\qquad U_i=p_i-e_i^2/2.
\]

At `K_1=K_2=1`, the symmetric equilibrium is `e_1=e_2=1/4`. The first-order conditions are `e_i=K_i p(1−p)`. Hold actor 1's effort fixed and let actor 2 use its equilibrium policy. At equality,

\[
\partial_{K_1}p_1=1/16,
\quad \partial_{K_2}p_1=-1/8.
\]

The definition in Proposition 2.2(4) therefore gives `r^pr=4·(1/16)=1/4`. But on `(K_1,K_2)=(1+ε,1−ε)`, the actual derivative is `3/16`, whereas the proof's substitution gives `r^pr/2=1/8`. A common perturbation also has a nonzero private derivative, `−1/16`, even with a fixed prize and no shared loss. The equilibrium **net payoff** has the same relative derivative by the envelope theorem; the envelope theorem does not remove the cross partial.

This example diagnoses the invalid local identity; it is not presented as a fully solved infinite-horizon stationary counterexample. The universal stationary price theorem needs a replacement proof. Scale invariance and an appropriately defined directional elasticity could recover a narrower result.

**The finite-jump lottery is a different valuation problem.** Its Bellman equation samples winner and loser states at finite separation. The deterministic structural derivative uses a Jacobian at equal standing. They coincide in special linear cases; they are not identical in general. The passive, fixed-effort lottery with `r=1.5`, `Γ=.6`, `d=.2`, `δ=.97` independently gives a finite-jump price about `1.03111`; the structural expression is `1.08178`, a discrepancy of about 4.68%. Yet SUPPLEMENT:140 and 298 call the equality exact with opponents fixed. MP(h) only enforces that equality for `r==1`.

The numerical strategic cases should also stay numerical: for the smooth case `r=4`, `Γ=.45`, `d=.1`, the computed stochastic price is about `.5131`, while the measured-private-elasticity formula gives about `.6534`, with its discounted private gain still below one. Excluding this case because the *equilibrium* gain exceeds one does not establish the claimed private-price domain.

**Repair:** keep the deterministic equilibrium-stability result separate from the private value calculation. Define the latter using the full own/cross derivatives, common-state effects, costs, and equilibrium transition operator. Separate local derivatives from finite winner/loser value differences. Restrict the exact passive-lottery assertion to the cases actually proved, and label discretized Markov equilibria accordingly.

The independent Bellman audit corroborates distinct smooth and concentrated numerical fixed points, including the reported concentrated price about `1.39186` on a 3,000-cell grid and `1.41028` on a 6,000-cell grid. That supports numerical multiplicity; it does not prove continuous-state existence, differentiability of the concentrated branch, or selection of an equilibrium by belief.

Catch-up needs one further distinction. In the checked catch-up specification with the added standing penalty `L_sub=100`, `Γ=.3`, `r=4`, and `d=.1`, the equilibrium and private win-share elasticity ratios are about `.99343` and `.99671`, corroborating a small reversal of those elasticity corrections. The total computed continuation price is nevertheless about `4.58187`, above the structural `.17647`, because the added payoff penalty itself values standing. Clarify that the reported reversal concerns win-share elasticities; it is not a reversal of the entire standing-price premium. This is a property of the specified payoff modification, not a general sign theorem.

### 3. High — the detection link substitutes an eventual probability into a next-period value equation

Locations: [THEORY:457](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:457), 468, 472; SUPPLEMENT:462–468, 544–550; `checks_v62.py:3951–3955`. Key: `detectlink`; downstream enforcement row and joint scissors.

Equation (14) puts the decisive or punished continuation in the **next period**. Remark 5.5 introduces a breakout requiring `T_dec` periods and a random detection time, but replaces only the probability of escape. The waiting times also change discounted value.

Set

\[
C=1,\quad D=1.5,\quad v=0,\quad g=.3,\quad\delta=.9.
\]

The deviation pays `1.3` at date zero; unresolved dates pay `C`. With probability `.36`, detection and response occur at date 9, paying the absorbing payoff `v` from that date onward. Otherwise decisiveness arrives at date 10, paying `D` from that date onward. Response is strictly before decisiveness, and `p_d=1−υ(10)=.64` exactly. Action-free absorbing states make credibility of the continuation unproblematic in this counterexample.

The printed normalized advantage is

\[
.03+.9[.64(.5)-.36]=-.006,
\]

so the printed condition deters. The actual advantage is

\[
.03+.64(.9)^{10}(.5)-.36(.9)^9
=.002105724792>0.
\]

The actual escape bound is `.6362515560`, below the printed `.6444444444`. The error changes the compliance prediction.

For interim payoff `C`, the correct condition is

\[
(1-\delta)g+
\mathbb E[\mathbf1_{\rm escape}\delta^{T_{\rm dec}}(D-C)
+\mathbf1_{\rm detected}\delta^{T_{\rm det}}(v-C)]\le0.
\]

JX samples a detection time, then assigns `δ*(D if escape else v)` immediately. That independently checks the escape probability; it does not check the delayed payoff stream. The reduced joint scissors model inherits the timing assumption.

**Repair:** either derive the delayed condition, redefine `D` and `v` as conditional discounted continuation values at date one including the waiting interval, or explicitly assume the entire detection/breakout process occurs within one strategic period. Under the latter convention, label the aggregation and distinguish its time unit from the stock model's. Recompute the joint crossing values if using actual multi-period delay. The immediate-transition enforcement theorem and the identity for eventual escape probability can be retained.

### 4. High — unbounded payoff advantage does not imply extinction under every payoff-monotone rule

Locations: [THEORY:214](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:214), 225–229, 906; SUPPLEMENT:239, 851. Keys: selection of load; R1.

Definition 3.2 requires only the sign of relative growth to agree with the payoff gap. Proposition 3.4 nevertheless uses the raw integrated payoff gap as an extinction condition. Its proof uses the replicator identity for log share ratios, which is stronger than payoff monotonicity.

For two types with loads zero and one, let `ν=1` and `τ_eff(t)=1−1/(1+t)`. The high-load payoff advantage is `Δπ=1/(1+t)`, and the specified cumulative advantage is `B(t)=ln(1+t)→∞`.

Choose the relative, strictly payoff-monotone rule

\[
\dot p=p(1-p)(\Delta\pi)^3.
\]

Adding a common payoff changes nothing, and cubing preserves every payoff-gap sign. Nevertheless,

\[
\operatorname{logit}p(t)=\operatorname{logit}p(0)
+\tfrac12[1-(1+t)^{-2}],
\]

so the high-load share does not tend to one. Starting at `.001`, it tends to about `.00164765`. With host regeneration `.05`, harm coefficient `.08`, initial host one, and floor `.3`, `(reach)` holds for full load, while the actual host stays above `.9973` by comparison. The sharper R1 requirement `B(t) not→∞` is therefore not necessary under the selection class printed in its row.

**Repair:** state replicator dynamics, or impose an effective-selection condition making the integrated *growth-rate difference* diverge. Carry that condition into R1 and any downstream necessity claims. Merely repeating “payoff-monotone” cannot supply it. This correction does not undermine the result under replicator selection.

### 5. High — an asymptotic row-sum certificate is not evidence of independence at the time of a decision

Locations: [THEORY:328](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:328), 402, 655, 1154–1157, 1167; DISCUSSION:327, 354, 358. Key: `topology` and the institutional use of `certificate`.

Proposition 4.10(2) proves `x_i→0` from `x_i(0)<1` when the full inbound row sum is below one. THEORY:655 calls that a sufficient certificate that no party **controls** the checks' funding, appointment, or access. The theorem permits substantial current control and a long period of increasing capture before recovery.

Take an evaluator with `a=c=d=ζ=1`, slow support adjustment `ε=.01`, and incoming conversion `.5` from an external domain kept captured. Its row sum is `.5`. Start with `x(0)=.9`, `z(0)=2`. Then exactly

\[
z(t)=.5+1.5e^{-.01t},\qquad
\operatorname{logit}x(t)=\ln9-.5t+150(1-e^{-.01t}).
\]

After 50 periods the support is about `1.410`, and the captured share exceeds `.999999999999`; it eventually falls to zero. The certificate is true throughout. It does not make decisions during those 50 periods independent. At the excluded start `x(0)=1`, the boundary is invariant and no decay occurs at all.

**Repair:** call the row sum a sufficient certificate of eventual removal in the field model, with its initial-state restriction. To certify an evaluator for use now, add a bound on current captured share/support, a recovery or residence condition, and evidence about actual access, appointment, and authority. Keep the already repaired distinction between institutional capture and correlated errors. These additional requirements matter especially for the estimators and custody decisions on which the activation mechanism relies.

### 6. Medium — zero tax and equality of sanctions preserve a safeguard; they do not make it spread or remove evaders

Locations: [THEORY:627](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:627)–639, 1156, 1162; SUPPLEMENT:612, 618, 766; TESTS:59, 74, 95.

The proof and some core wording now correctly distinguish neutrality from selection. The recommendations lose the distinction again: a tax “zero or below” is repeatedly said to spread the safeguard, and admission sanctioned **at least** at the gain from evasion is said to keep a divergence out.

With identical developer payoffs and zero tax, a population initially half safe and half unsafe stays half unsafe under replicator selection. Likewise, baseline payoff one, compliance cost `.2`, and expected evasion sanction `.2` give both variants payoff `.8`; existing evaders remain. Lemma 3.3 correctly reserves convergence to full compliance for strict inequalities.

At equality, the correct conclusion is no strict selection advantage to evasion. A wholly compliant starting population can remain compliant in the mutation-free model; that is weaker than elimination or reliable admission.

**Repair:** use a **negative** tax for private selection toward the safeguard, and zero tax for neutrality. Use strict expected sanction, a tie-breaking rule, or actual exclusion of violating variants when claiming elimination. Withdrawal of an existing admission requirement at zero tax requires a separate adoption/persistence argument, particularly for previously deployed unsafe variants. Preserve R8b's correct separation of neutrality from compliance.

### 7. Medium — Table 7.1 is not yet an exact summary of the repaired inequalities and levers

Locations: [THEORY:697](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:697)–705; comparison with THEORY:364–365, 908.

The most definite remaining omission is the capture row's rate condition. It includes cheapening variable control cost and capacity tracking, but drops the **no per-unit floor** premise. The V6.1 counterexample still applies to the row as printed:

\[
d=2e^{.05t},\quad f=.49e^{-.01t},\quad\gamma=e^{-.2t},
\quad q=q^*=[.5e^{-.05t}-.49e^{-.01t}]_+e^{.2t}.
\]

With the remaining normalized coefficients one and baseline inbound conversion zero, cultivation ends at about `.505` and the certificate never fails, although correction grows at `.05<.1`. Proposition 4.5(3) now explains this correctly; the table does not.

Other cells need explicit scope, rather than a general assertion that every lever reverses the row:

| Row | Review result |
|---|---|
| Load | The threshold works for the corrected selection class of Finding 4. “Unequal incidence” alone has no universally adverse direction: it can penalize the more harmful variant. Equal incidence preserves neutrality; it is not generally required for host protection. Keep that distinction here as in R8b. |
| Compounding | The structural signs are channel-dependent as stated. The strategic instability claim requires the premises of the all-response calculation. Moving a gain downward need not cross one. |
| Standing | Correct in the fixed-prize and specified ratio-channel models, subject to Findings 1–2 and the strict-weight endpoint below. “Reversed by” should mean the stated comparative static unless a threshold-crossing magnitude is supplied. |
| Capture | Restore the floor cases, initial certification and adjustment conditions. `G≥1` also means loss of this sufficient certificate, not capture from every start. |
| Enforcement | Correct in the immediate-transition model; the detection version needs Finding 3. A decisive payoff no greater than cooperation does not alone deter a sufficiently large immediate gain; the text's full R4 exception correctly includes that gain. |
| Coverage/tempo | Preserve the residual-floor and shared-failure assumptions. Local slowing that reduces exposure is not by itself a proof of summability. |
| Talk | The effective-bias threshold is sound in its specified quadratic/uniform model. Verification and costly signals are alternative information channels, not proofs that the cheap-talk bias becomes smaller than `1/4`. |
| Alignment tax | Matched variants and type-specific incidence are now explicit. Apply the neutrality correction of Finding 6. |
| Delegation | Correct with the finite-speed and lock-probability conditions; the near-certainty bound must remain part of the intervention's scope. |

**Repair:** distinguish a lever's directional effect, sufficient magnitude to cross a threshold, and an alternative mechanism bypassing that threshold. Propagate each result's floor, horizon, channel and initial-state premises into the row that claims its conclusion. The † marks are useful and should stay.

### 8. Medium — independent informative readings do not ensure the readiness test terminates

Locations: [SUPPLEMENT:1051](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/SUPPLEMENT.md:1051)–1057. Key: readiness decision rule.

Remark S11.3(2) asserts almost-sure termination from independent readings and correctly computed likelihood ratios, without a condition guaranteeing continuing accumulation of information.

Let the independent observations satisfy

\[
H_0:X_t\sim\mathrm{Bernoulli}(1/2),\qquad
H_1:X_t\sim\mathrm{Bernoulli}(1/2+2^{-t-4}),\quad t\ge1.
\]

Every reading is informative and its likelihood ratio is exact. Nevertheless, on **every possible observation path**, every partial log-likelihood ratio stays between approximately `−.127702` and `.122485`. The manuscript's boundaries for `α=.01`, `β=.05/7` are approximately `−4.93159` and `4.59800`. Neither boundary can ever be reached. Thus noise or declining informativeness can produce permanent nondecision, not merely delay.

**Repair:** state the appropriate termination premises, such as informative iid readings with the required likelihood regularity, or a condition ensuring divergent accumulated information. Scope error guarantees to the registered hypotheses and the actual stopping procedure. The iid Gaussian computations remain valid examples; they do not prove termination for the statement's full class.

### 9. Medium — the judgment still adds decision principles that the protection standard does not establish

Locations: [THEORY:1153](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/THEORY.md:1153)–1179, compared with 796–802; TESTS:44–65; DISCUSSION:292–334.

**Tier 1(a).** The robustness matrix is much more useful than the previous unqualified list, but its letters state reasons to consider an action, not proofs that it is warranted on every reading. Public-good status supplies a reason for funding but does not establish a proposed programme's net value or appropriate scale. Custody preparation can have option value without its lead time exceeding every possible warning. “Preparation forgoes nothing” in TESTS:60 omits its cost and commitments. Narrow E1 is explicitly conditional on the objective that prices the lock; TESTS:65 already acknowledges N2. Qualify the heading accordingly: “every reading of the cruxes” cannot literally include every normative reading.

The defensible claim is robustness **within the adopted values and stated cost, information and lead-time assumptions**, with scale adjusted to evidence. Separate low-cost measurement/design work from committing in advance to a particular activation rule. The latter already carries consequences in unfavorable C4 cases.

**Tier 1(b).** Hazard arriving before evidence is a reason not to demand direct observation of catastrophe before acting. It is not, by itself, a comparison of an intervention's worst-case risk with the alternatives. Section 8.1 asks for that comparison on one uncertainty range. For example, hypothetical bounds `.1` without a mandate and `.2` with a poorly designed mandate are compatible with delayed evidence; the protection standard does not instruct keeping that mandate until the protected-against mechanism is measured absent. These are logical countervalues, not estimates.

The “withdrawn only where its named crux is favorable” rule therefore needs an additional precautionary value premise and an explicit escape for evidence that the remedy itself fails or causes greater protected risk. Test M and C4 already contain parts of that escape. Bring them into the withdrawal rule rather than leaving the rule apparently dependent only on C2/C9/C12. Also apply Finding 6 at a measured zero tax.

**Tier 2.** The advance-commitment requirement is now explicit and repairs the earlier discretionary-trigger problem **as a design specification**. It is not yet a proof that the mechanism executes against the strongest violator. That depends on custody, authority, monitoring and continuing correction; Findings 3, 5 and 8 affect those dependencies. Keep E2 and E3 separate, as the text now does.

**Tier 3.** The failure-mode table names the proposed design's own failures and labels its reversals untested; that is a major improvement. The comparison still applies different conditions when calling a failure reversible. The design's capture and collusion are called reversible given timely recertification, replacement or rotation. A restrictor's converted correctors are simply called irreversible (DISCUSSION:314, 321), citing Proposition 4.3, which proves selection for influence, not impossibility of subsequent correction. Apply the same “before protected loss, with a surviving independent corrector” condition to both.

THEORY:1176 also loses the delegation qualification already stated correctly at THEORY:603 and in R9: Lemma 6.3 alone gives delayed recovery, not irreversibility. With capacity `.2`, recoverable level `1`, required floor `.5`, and recovery rate `.1`, capacity returns to the floor after `10 ln(1.6)≈4.70004`. Irreversibility needs the further condition that the contest or another hazard denies that interval, or an actually irreversible decision has already occurred. This is a premise lost in the summary, not a counterexample to Proposition 6.4 when its lock event is imposed.

Likewise, standby service provision is a proposed way to prevent irreversible harm during an interruption; restoration after an interruption cannot reverse deaths already caused by it. Give the design's service failures the same time-to-loss qualification as continuation's failures.

**Repair:** retain the ranking as an explicitly conditional judgment. Use paired branches for every path: timely successful correction before O1/O2, versus correction failing or arriving too late. Distinguish a proposed reversal, its demonstrated feasibility, and the actual risk bound. The existence of an irreversible outcome in a path's uncertainty range alone does not establish that its finite-horizon probability bound exceeds the tolerance; Section 8.1 needs that extra assessment too.

## Other definite boundary and premise corrections

| Location | Problem and repair |
|---|---|
| THEORY:263–268; SUPPLEMENT:279 | The strict narrowing statement allows `θ_0=−1`, but (9) then gives `θ=−1` for every finite pair of returns. Require `−1<θ_0<n−1` for strict narrowing; state invariance at `−1`. “Every horizon” also needs at least one future payoff. The all-shared endpoint is separately invariant. |
| THEORY:400–402; SUPPLEMENT:399 | The core-pruning algorithm removes gains **below** one, but Proposition 4.10(4) claims the surviving core is stable without excluding equality. With `a=b=c=d=ζ=ε=1`, gain one survives pruning, while `xdot=x(1−x)(z−1)`, `zdot=x−z` sends starts `(1−ε,1−ε)` toward `(0,0)`, away from the captured corner. Exclude nonhyperbolic equality cases or prove them separately. This is distinct from the repaired cap equality. |
| THEORY:1073–1075; SUPPLEMENT:1009, 1013 | The receiver is said to restrain **iff** its posterior is at least the threshold, but the mixed equilibrium requires randomization at equality. At `μ=.5`, threshold `.6`, `c_R=.05`, `Π_R=.2`, the posterior is `.6` and restraint probability `.25`; mandatory restraint at equality makes imitation strictly profitable. Specify restraint above, racing below, and indifference at equality. The mixed-equilibrium derivation then works. |
| SUPPLEMENT:1061, 1081; Proposition S11.4 | The least successful dwell is generally an **infimum**, not an attained minimum: release exactly on the separatrix approaches the saddle. Require a duration strictly beyond the boundary, preferably with a margin. Independent integration gives boundary about `5.858956` at `G=2`, equal speeds, starting share `.99` and support `2`; `±.001` falls into opposite basins. Starts with `x=1` itself cannot be restored by this control because the boundary is invariant. |
| SUPPLEMENT:1027–1029 | Summability of post-pause hazards preserves positive survival only if every hazard is below one and survival to the pause is positive. The proof adds the former but the statement omits it. The sequence `(1,0,0,…)` is summable and has zero survival. For history-dependent hazards, also retain the history-uniform bound used by the proof. |
| THEORY:651; SUPPLEMENT:655 | The serial formula `p_ℓ^k` needs independence across layers, or `p_ℓ` interpreted as each layer's success probability conditional on all preceding successes. Marginal catch probabilities alone do not imply the product. Make the convention explicit, also for layered redundancy. The common-blind-spot ceiling is sound. |

## What is sound, with its scope retained

- **Proposition 3.9(2), in its stated ratio channel:** with `Ω=gS`, no provision or diffusion, write `a=(1−β)r`. The relative and common one-period return coefficients are `aκg` and `κg`, and the multipliers are `1−d+aκg` and `1−d+κg`. Their discounted increments compare in the same direction at every positive horizon exactly when `a>1`. The infinite-horizon comparison additionally needs convergence. Diffusion separates relative-return and share-instability thresholds as S3.2 states.
- **Channel signs:** sharing and diffusion lower the reinforcing-channel gain; provision lowers it when decisiveness grows less than proportionally with stock; correction lowers it in the complementary class. Strict effects may become zero at boundaries. The ratio-channel decay counterexample is now incorporated rather than denied.
- **Proposition 4.5:** the sufficiency comparison handles slow adjustment from the stated certified start. Necessity correctly requires capacity to track a positive fraction of its selected level. Fixed/falling floors and lump sums are now distinguished.
- **Proposition 4.6:** substituting `d_eff=d_0 exp[(α_cor−wδ_h)t]` gives the stated `wδ_h` shift. A positive human-capacity floor changes the required level rather than the long-run exponential rate.
- **Gradual selection:** the prompt is stale here. SUPPLEMENT:366 now uses the divergence condition `∫∞dq/V_q(q)=∞`, with constant/linear variance examples, rather than asserting that all variance `o(q²)` suffices. The revised integral comparison supports its bounded-capacity conclusion. THEORY:368 and R3a use the compatible “not faster than capacity” restriction.
- **Enforcement and punishment:** the immediate-transition inequality, its per-deviation use, the `D<C` exception, homogeneity under common scaling, and exclusive/independent breakout Bellman formulas check out under their stated assumptions. These results should not be weakened merely because the delayed extension needs repair.
- **Proposition 5.16:** directly subtracting the sender's and receiver's quadratic ideal actions gives `b_0(n−1−θ)/(n−1+θ)`. The common linear third-party term cancels from the gap. The two-relative-actor degeneracy and the uniform-quadratic informative-communication boundary are treated separately as required.
- **Proposition 5.17:** the three arms and the stakes comparative static are sound in their individual models and stated domains. In the ratio channel the gains' dependence on the won share supplies the pivot. Joint movement in the world remains C0; the delayed-enforcement join requires Finding 3, and extension beyond the price domain is a modeling choice.
- **§11:** after repairing the tie rule, the mixed signaling equilibrium and its cost-ratio bound are sound in the stated game. Dwell grows with interior logit depth and is unbounded as capture ages in the field model; a maintained alternative bounds the depth. Finite age is not literally the corner `x=1`, and exact-boundary release needs the strict-duration correction above.

## What the checks establish, and what was not checked

The check suite usefully includes the previous outside-review boundary cases: price-domain failure; the correction sign; cap equality; diffusion-only restoration; falling positive floor; unequal incidence; label-dependent stochastic punishment; delegation with `p<1`; nonlinear fitness; and the corrected Test Γ sign. The old counterexamples are substantively reproduced. Their presence does not validate every generalized statement built around them.

The 188 is a count of runtime `expect()` checks, not 188 independent derivations. Some older blocks only print comparisons. Blocks also mix genuinely independent computations with identities and formula-based checks, so a binary label for an entire block can mislead. Important distinctions are:

- **Independent numerical evidence:** nonlinear stock trajectories versus derivatives; equilibrium or best-response searches; value iteration on explicit stochastic states; cap/diffusion and floor boundary cases; direct field integration; and simulated observations under a specified sampling model.
- **Algebraic or construction checks:** rearranging a value inequality and comparing it to itself; transforming one objective weight by its derived formula; testing a threshold with values generated by that same threshold; closed-form topology probabilities; the `0.95^7` product; exact correspondence of verification thresholds after payoffs have been defined to make the correspondence hold.
- **Hybrid checks needing narrow claims:** JX independently samples the escape event but assumes the disputed timing of payoffs. MP solves a discretized stochastic lottery and sometimes compares a finite-state value difference with a local derivative. Passing either block does not prove the stronger joins in Findings 2–3. A final index of outside-review cases checks their registered flags, not new independent examples.

The [complete assertion map](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/codex-second/second-checks/assertion-audit.tsv) classifies all 188 executed checks, with source lines: 150 direct model regressions (some using subsidiary closed forms), 30 formula/identity checks, six stipulated-path valuations, one derived toy and one bookkeeping index. The 150 are **not** 150 independent theorem tests. Thirteen blocks contribute no counted `expect()` assertions and instead print diagnostics. The [detailed audit](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/codex-second/second-checks/AUDIT-CHECKS-TRANSITION.md) lists those blocks and the individual classifications.

The numerical-tag inventory found no missing current block code, and the newly restated §11 numbers were routed and reproduced. This was not an exhaustive comparison of every numeral in the three documents with output; legacy references and expanded grids were not rerun. S15's statement that the default run writes `checks_v62.log` also needs the shell redirection shown in the script's own instructions: the script writes standard output.

The [independent Markov solver](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/codex-second/second-standing/markov_audit.py) and [formal audit detail](/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/reviews/codex-second/second-standing/FINDINGS.md) preserve the longer computations. No assertion failure was needed to produce the counterexamples here: the omitted cases fall outside what the passing assertions test.

This was a targeted formal and consistency review of the requested repairs and extensions. It checked the named proofs, core-to-proof premise transfer, selected registers and summary tables, the structure build, and the complete default numerical run. It did **not** independently re-prove every inherited theorem, establish continuous-state existence/selection of all Markov equilibria, prove the optimal stochastic punishment existence assertion, calibrate any institutional parameter, validate every empirical citation against its original source, or establish any whole design's protected-loss probability. Citation coverage from the structure checker establishes matching references, not external evidentiary truth. Claim tags should be narrowed wherever a finding above leaves a result conditional, numerical, or unproved.

The most useful revision is by claim: repair the general standing-price domain, the responsive-rival derivatives, and the detection clock; then propagate those conditions through Table 7.1, R1/R4, the activation logic, and the judgment. Keep the repaired special cases, the explicit open interfaces, and the separation between stopping E2 and slowing E3.
