# D2 — Mathematical repairs for V6.2 (Fable)

4 October 2026. Prepared from the V6.1 sources (`v6.1/src/core`, `v6.1/src/supp`), the review round (`v6.1/reviews/`) and the reviewers' scripts. Every derivation below is my own; where a reviewer's claim is wrong or incomplete I say so with the derivation. Scripts (pure Python, standard library) and their logs are in `v6.2/planning/math-fable/`: `f1_standprice.py` (3.9, 2.2(3) domain), `f2_mpe.py` (strategic response), `f3_compound.py` (2.3, d-sign, S2.1), `f4_selection.py` (3.3, 3.10, 6.7/R8), `f5_corrrate.py` (4.5), `f6_enforce.py` (5.4, 5.5, scissors, R4), `f7_misc.py` (6.4, 6.8, 6.11, 10.5, 10.3, 4.12, 6.9). Each `.log` is the output quoted here. Nothing outside `v6.2/planning/` was edited.

**Conventions.** "Core form" is what the proposition states in THEORY, with every premise its proof uses; "full form" goes to the Supplement. Tags follow S0. Keys are the stable keys of `src/keymap.json`. Where I propose new text I mark it `>`.

**Three findings that go beyond the reviews.**
1. *Two loop gains, not one, once rivals respond.* In the stochastic compounding contest the price of standing is the closed-loop gain $\tilde\Gamma_\delta/(1-\tilde\Gamma_\delta)$ of the *partial-equilibrium* loop (own intensity fixed, the rival responding to the state), while the stability of equal standing is decided by the *full-equilibrium* gain $\Gamma_{\rm eq}$ (both respond). They coincide with the structural $\Gamma$ when strategies are fixed. `f2`: with small jumps the equilibrium price equals the partial-equilibrium closed-loop gain to four digits, and the expected-deviation multiplier equals $1+d(\Gamma_{\rm eq}-1)$ to five. This is the exact sense in which "one loop gain prices standing" survives, and the exact sense in which it does not (§1–2).
2. *Compounding narrows the working objective exactly where reinvestment pays relatively.* $\theta_{\rm eff}<\theta_0$ iff $\lambda_{\rm rel}>\lambda_{\rm com}$. With a fixed prize this is always (the future is zero-sum). With a prize proportional to total capacity, $\lambda_{\rm rel}/\lambda_{\rm com}=(1-\beta)r$ at every horizon, so the narrowing condition is literally the compounding condition of Proposition 2.3(1): compounding narrows objectives exactly where leads compound (§2, §26).
3. *Beyond $\Gamma_\delta=1$ the price of standing is not negative and not finite: it diverges as a power.* The present value of a relative perturbation $\varepsilon$ scales as $\varepsilon^{\alpha}$ with $\alpha=\ln(1/\delta)/\ln\lambda^\ast<1$, so the price per unit grows as $\varepsilon^{\alpha-1}$; `f1(C)` measures the exponent $-0.42$ against the predicted $-0.4221$. The reading "$\theta\to-1$ from below" is right; no finite first-order $\theta$ exists beyond.

---

## 1. `loopgain` (Proposition 2.2)

**(a) Core form.**

> **Proposition 2.2 (One loop gain) [thm].** The conditions multiply into a single loop gain; equal standing breaks when it exceeds one; and, while the discounted loop is stable, the same gain prices standing.
>
> *Model.* [as V6.1: $n$ carriers, prize $\Omega$, shared fraction $\beta$, $p_i=e^{\sigma_i}/\sum_k e^{\sigma_k}$, stocks (1), $r_j$, $\omega_j$, $\Gamma$ as (2).] **Intensities, strategies and the prize are fixed; $r_j$ is the structural elasticity $\partial\sigma/\partial\ln X^j$ at equal standing.**
> 1. [as V6.1] *Equal standing is locally asymptotically stable if $\Gamma<1$ and unstable if $\Gamma>1$. The channels add because every stock is fed by the same winnings (a rank-one coupling through the win probability): compounding through capacity and the reflexive closure through rule support are terms of one sum, and channels each too weak to open the loop can open it together.*
> 2. [as V6.1]
> 3. *For an actor that discounts at $\delta$ and reinvests its net payoff at the rates at which winnings convert, with $0\le\Gamma_\delta<1$, a unit of relative net payoff today is worth, to first order, $\Gamma_\delta/(1-\Gamma_\delta)$ units of its own future winnings: the closed-loop gain of the discounted loop. Here $\Gamma_\delta=(1-\beta)\sum_j r_j\omega_j\,\delta d_j/(1-\delta(1-d_j-\delta_{f,j}))<\Gamma$, and $\Gamma_\delta\to\Gamma$ as $\delta\to1$. The series defining the price converges iff $\Gamma_\delta<1$; as $\Gamma_\delta\to1^-$ the price diverges, and for $\Gamma_\delta\ge1$ the value of standing at equal standing has no finite slope (S2).*
>
> *Scope.* Local, at equal standing, for reinforcing channels and a prize of fixed size. If intensities respond to the state, (1) holds with $r_j$ replaced by the full-equilibrium elasticity and (3) with the partial-equilibrium one (S2, Remark S2.2); in discouragement contests both exceed the structural value several-fold, so a structural $\Gamma<1$ is necessary, not sufficient, for the stability of equal standing in the class computed [num]. The additivity in (1) needs the rank-one structure: a channel fed by a separately chosen expenditure (lobbying bought from profits by a different rule) does not simply add. It does not decide global behaviour, whether a position beyond sanction can be reached, or whether capability outruns correction.

**(b) Proof.** The V6.1 proof of (1)–(3) is correct as written (checked by two reviewers and by `f3(B)`, `f1(C)` here); add three sentences:

- *Convergence.* The present value is $\frac{\delta}{n}v^\top\sum_{t\ge0}(\delta J)^t u\,y$. By the secular argument applied to $\delta J$, $\rho(\delta J)<1$ iff $\frac{\delta}{n}\sum_j u_jv_j/(1-\delta(1-d_j-\delta_{f,j}))<1$, i.e. iff $\Gamma_\delta<1$. Sherman–Morrison is valid exactly there.
- *Beyond the domain.* For $\Gamma_\delta\ge1$ write $\lambda^\ast>1$ for the Perron root of $J$. A relative perturbation $\varepsilon$ grows as $\varepsilon\lambda^{\ast t}$ until it saturates at order one, after $T(\varepsilon)=\ln(1/\varepsilon)/\ln\lambda^\ast$ periods, so the discounted excess winnings are of order $\varepsilon\sum_{t<T}(\delta\lambda^\ast)^t+\sum_{t\ge T}\delta^t$. With $\delta\lambda^\ast>1$ the first sum is of order $\varepsilon(\delta\lambda^\ast)^{T}=\varepsilon^{\alpha}$, $\alpha=\ln(1/\delta)/\ln\lambda^\ast\in(0,1)$, and the second of order $\delta^T=\varepsilon^{\alpha}$ as well. Hence $PV(\varepsilon)\asymp\varepsilon^\alpha$ and $PV/\varepsilon\to\infty$: the value function is continuous at equal standing with infinite slope, and no finite first-order weight represents the actor. (With $\delta\lambda^\ast<1$ but $\Gamma_\delta\ge1$ — impossible, since $\Gamma_\delta<1\iff\rho(\delta J)<1$ — so the two regimes are exactly the two signs of $\Gamma_\delta-1$.)
- *Rank-one.* The additivity of (1) is the secular equation (S1), which holds because $J=D+\frac1n uv^\top$; a channel fed by an input chosen by another rule contributes a term that is not of this form.

**(c) Tag.** [thm]; the "necessary, not sufficient" clause of the Scope is [num].

**(d) Checks.** `f1(C)`: $n=2$, $r=2$, $d=0.2$, $\delta=0.9$ ($\Gamma=2$, $\Gamma_\delta=9/7$): PV positive at every $\varepsilon$; local exponent of $PV/\varepsilon$: $-0.444,-0.430,-0.425,-0.423,-0.4225$ for $\varepsilon=10^{-3}\dots10^{-7}$, against the predicted $-0.4221$. `f3(B)`: numerical spectral radius against $\Gamma$ for ratio-form and level-form channels (also covers item 4). `f2(1)`: the equilibrium elasticities (item 2).

---

## 2. `standprice` (Proposition 3.9), with the strategic case

**(a) Core form.**

> **Proposition 3.9 (Compounding prices standing) [thm∣prem].** Near equal standing, compounding raises the weight a forward-looking actor puts on standing wherever reinvestment returns more through relative standing than through the common growth of the prize.
>
> *In the contest of Proposition 2.2, let an actor holding $\theta_0<n-1$ discount at $\delta$ and reinvest its net payoff at the rates at which winnings convert, with others' strategies fixed. Write $\lambda_{\rm rel}$ for the discounted return of a unit of relative payoff through its own future winnings and $\lambda_{\rm com}$ for the discounted return of a unit of payoff common to all through the growth of the prize. To first order the actor acts on the objective of Proposition 3.5 with the working self-model $\theta_{\rm eff}$ given by*
> $$\frac{1+\theta_{\rm eff}}{\,n-1-\theta_{\rm eff}\,}=\frac{(1+\theta_0)(1+\lambda_{\rm com})}{(n-1-\theta_0)(1+\lambda_{\rm rel})},$$
> *so that $\theta_{\rm eff}<\theta_0$ if and only if $\lambda_{\rm rel}>\lambda_{\rm com}$.*
> 1. *(Fixed prize.) $\lambda_{\rm com}=0$ and, for $0\le\Gamma_\delta<1$, $\lambda_{\rm rel}=\Gamma_\delta/(1-\Gamma_\delta)$, which gives (9); $\theta_{\rm eff}=\theta_\Gamma$ falls toward $-1$ as $\Gamma_\delta\to1^-$ for every $\theta_0<n-1$, and the weight of the common channel, the visibility of the host, the point of enough, the weight of a rebated levy and the gain from breaking a promise, falls with it.*
> 2. *(Prize that grows with capacity.) If the prize is $\Omega_0+g\sum_jK_j$ with a share $\beta$ divided equally, then $\lambda_{\rm rel}/\lambda_{\rm com}=(1-\beta)r\,\Omega/(n K g)$ in the two-period contest; when the prize is proportional to total capacity, $\lambda_{\rm rel}/\lambda_{\rm com}=(1-\beta)r$ at every horizon, so compounding narrows the working self-model if and only if $(1-\beta)r>1$: the condition under which leads compound (Proposition 2.3(1)).*
> 3. *(Strategic response) [num].* *If rivals' intensities respond to the state, the first-order form survives but the price is the closed-loop gain of the partial-equilibrium loop (S2, Remark S2.2): at equal standing it exceeds the fixed-strategy value, by $2(n-1)/n$ in a two-period Tullock contest with effort in the second period and by 1.1–4.8 in the stochastic contest computed, and far from equal standing a laggard's price tends to zero or turns negative: it stops contesting standing.*
>
> *Scope.* First order; the prize fixed or of the stated form; "reinvests net payoff" is load-bearing (if only gross winnings convert, the relative part of private cost is not amplified and $\theta_{\rm eff}$ is lower still, `f1(D)`). Where the loop gain is high enough that $\Gamma_\delta\ge1$, no finite weight represents the actor; the limit from below is the reading. *Proof:* S3 [num: in a two-period contest the computed symmetric equilibrium equals $e(\theta_{\rm eff})$ to seven digits in 14 cases spanning both signs].

The headline sentence "every forward-looking actor acts as if it valued only its standing" goes; the §1.2, §2 claim box, §3 claim box and 导读 sentences become: *"near equal standing, compounding raises the weight on standing wherever reinvestment's relative return exceeds its common return; with a fixed prize it always does."*

**(b) Proof (full form, for S3).** Let $\Delta\pi$ be a change in today's payoffs with mean $\bar\Delta$ and relative part $y_i=\Delta\pi_i-\bar\Delta$; the actor reinvests $x_j=\kappa\Delta\pi_j$ into capacity. Future winnings are $w_i=(1-\beta)\Omega_2p_i+\beta\Omega_2/n$ with $p_i=K_i^r/\sum K^r$ and $\Omega_2=\Omega_0+g\sum K$. At equal standing $\partial p_i/\partial K_i=r(n-1)/(n^2K)$, $\partial p_i/\partial K_j=-r/(n^2K)$, and $\partial\Omega_2/\partial K_j=g$, so
$$\Delta w_i=\frac{(1-\beta)\Omega_2 r}{nK}\,(x_i-\bar x)+g\,\bar x .$$
Discounting, the future term is $F_i=\lambda_{\rm rel}y_i+\lambda_{\rm com}\bar\Delta$ with $\lambda_{\rm rel}=\delta\kappa(1-\beta)\Omega_2r/(nK)$, $\lambda_{\rm com}=\delta\kappa g$. Since $\sum_iF_i=n\lambda_{\rm com}\bar\Delta$, the others' average is $\bar F_{-i}=\lambda_{\rm com}\bar\Delta-\lambda_{\rm rel}y_i/(n-1)$, and the future change in $J_i=\pi_i+\theta_0\bar\pi_{-i}$ is $\frac{n-1-\theta_0}{n-1}\lambda_{\rm rel}y_i+(1+\theta_0)\lambda_{\rm com}\bar\Delta$. Adding today's change $(1+\theta_0)\bar\Delta+\frac{n-1-\theta_0}{n-1}y_i$:
$$\Delta J_i^{\rm total}=(1+\theta_0)(1+\lambda_{\rm com})\,\bar\Delta+\frac{n-1-\theta_0}{n-1}(1+\lambda_{\rm rel})\,y_i .$$
Matching to $(1+\theta)\bar\Delta+\frac{n-1-\theta}{n-1}y_i$ up to a positive factor gives the displayed ratio. The map $\theta\mapsto(1+\theta)/(n-1-\theta)$ is increasing on $[-1,n-1)$, so $\theta_{\rm eff}<\theta_0$ iff $(1+\lambda_{\rm com})/(1+\lambda_{\rm rel})<1$. (1): $g=0$, $\lambda_{\rm rel}=\Gamma_\delta/(1-\Gamma_\delta)$ by Proposition 2.2(3), so $1+\lambda_{\rm rel}=1/(1-\Gamma_\delta)$ and the ratio is $(1+\theta_0)(1-\Gamma_\delta)/(n-1-\theta_0)$, which is (9). (2): with $\Omega_0=0$, $\Omega_2=gnK$ and $\lambda_{\rm rel}=\delta\kappa(1-\beta)gr$, so the ratio of returns is $(1-\beta)r$. *Infinite horizon, proportional prize, no depreciation, all winnings reinvested:* the mean stock grows by $(1+g)$ a period and a relative deviation by $1+(1-\beta)rg$ (S2's linearization with $\Omega_t=gS_t$), so $\lambda_{\rm rel}=\delta(1-\beta)gr/(1-\delta(1+(1-\beta)rg))$ and $\lambda_{\rm com}=\delta g/(1-\delta(1+g))$ when both series converge, and
$$\frac{\lambda_{\rm rel}}{\lambda_{\rm com}}=\frac{(1-\beta)r\,(1-\delta(1+g))}{1-\delta(1+(1-\beta)rg)}\ \gtrless\ 1\iff(1-\beta)r\gtrless1 .$$
(3) is Remark S2.2 below. $\square$

**Remark S2.2 (Two gains when strategies respond) [thm∣prem, num].** In the stochastic compounding contest with intensity (two actors, lottery prize, state $s=K_1/S^\ast$), let $p_{\rm eq}(s)$ be the equilibrium win probability and $\tilde p(s)$ the win probability when own intensity is held at its equilibrium level and the rival re-optimizes. Write $\Gamma_{\rm eq}=(1-\beta)\omega\,p_{\rm eq}'(\tfrac12)$ and $\tilde\Gamma=(1-\beta)\omega\,\tilde p'(\tfrac12)$, and the discounted forms as in (3). *(i) The expected relative deviation at equal standing evolves, to first order, by the multiplier $1+d(\Gamma_{\rm eq}-1)$: equal standing is stable for the expected state iff $\Gamma_{\rm eq}<1$. (ii) With small jumps and no shared loss, the equilibrium price of a relative unit is $\tilde\Gamma_\delta/(1-\tilde\Gamma_\delta)$. (iii) Both reduce to the structural $\Gamma$ when intensities are fixed.* *Proof.* (i): $E[s'\mid s]=(1-d)s+j_l+(j_w-j_l)p_{\rm eq}(s)$ with $j_w-j_l=\kappa(1-\beta)\Omega/S^\ast=d\omega(1-\beta)\cdot\Omega/\Omega$; differentiate at $\tfrac12$. (ii): let $W(s)$ be the equilibrium value. By the envelope theorem on own intensity, $W'(s)=A_1\big(\partial_sp+\partial_{e_2}p\,e_2^{\ast\prime}\big)-\ell e_2^{\ast\prime}+\delta(1-d)E[W'(s')]$ with $A_1=(1-\beta)\Omega+\delta(W(s_w)-W(s_l))$ the effective valuation; the bracket is $\tilde p'$. With $\ell=0$ and $W(s_w)-W(s_l)\approx W'(s)(j_w-j_l)$, writing $\lambda=\delta(W(s_w)-W(s_l))/((1-\beta)\Omega)$ gives $\lambda(1-\delta(1-d))=\tilde\Gamma\,\delta d\,(1+\lambda)$, i.e. $\lambda=\tilde\Gamma_\delta/(1-\tilde\Gamma_\delta)$. With shared loss the term $-\ell e_2^{\ast\prime}$ adds to the price (a leader's lead makes the rival spend less, which is worth $\ell$ per unit). $\square$ Opus's suggestion to redefine $r_j$ as "the" equilibrium elasticity is right for stability and wrong for the price: the two elasticities differ by the own-response term $\partial_{e_1}p\,e_1^{\ast\prime}$, and the price is not $\Gamma_{\rm eq,\delta}/(1-\Gamma_{\rm eq,\delta})$ (which is negative or infinite in every case Opus computed, since $\Gamma_{\rm eq,\delta}>1$ there, while the MPE price is finite).

**(c) Tags.** Proposition: [thm∣prem] (premises: first order, net payoff reinvested, others fixed, prize of the stated form, $\Gamma_\delta<1$ in (1)). Part (3): [num] with the two-period factor [thm]. Remark S2.2: (i),(iii) [thm]; (ii) [thm∣prem] (small jumps, $\ell=0$) with [num] support.

**(d) Checks.** `f1(A)`: 14 cases ($n=4$ with $r\le4/3$, $n=2$ with $r\le2$; $\theta_0\in\{-0.5,0,0.3,0.5,1,1.9\}$; $\beta\in\{0,0.2,0.3,0.5,0.6\}$; fixed, mixed and proportional prizes): $\max|\theta_{\rm eff}-{\rm formula}|=7.6\times10^{-8}$; the sign rule held in 14/14, including the three knife-edge cases $(1-\beta)r=1$ where $\theta_{\rm eff}=\theta_0$ to five digits. `f1(B)`: infinite horizon, six $(r,\beta)$ pairs, PV ratio by simulation equals the closed form to five digits (2.53846, 0.68750, 0.62264, 1.00000, 2.08108, 0.92958). `f2(1)`: $d=0.02$, five cases: $\lambda_{\rm MPE}$ = closed-loop($\tilde\Gamma_\delta$) to four digits (0.0319/0.0319, 0.0491/0.0491, 0.0492/0.0492, 0.0768/0.0768, 0.1078/0.1079); expected-deviation multiplier = $1+d(\Gamma_{\rm eq}-1)$ to five digits. `f2(2)`: $d=0.2$: amplification ×1.12 ($\Gamma=0.3$), ×2.58, ×2.39, ×4.75 ($\ell=0.5$), ×2.19 ($\Gamma=0.9$); $\Gamma_{\rm eq}=1.96$ at structural $\Gamma=0.6$ with $E|s-\tfrac12|$ after 60 periods 0.198 against 0.120 under the structural lottery; laggard's price at $s=0.25$: 0.065 (vs 1.62 at parity), negative ($-0.039$) with shared loss. The two-period factor $2(n-1)/n$: Fable's `m2` (1.0000, 1.3333, 1.5000, 1.6667) and my derivation: with second-period value $V_i=\Omega_2w_i^2$, $dV_i/d\alpha_i=2\Omega_2(n-1)^2/(\alpha n^3)$ against the fixed-effort $\Omega_2(n-1)/(n^2\alpha)$.

---

## 3. `compound` (Proposition 2.3)

**(a) Core form.** Part (1) unchanged. Part (2):

> 2. *A point of enough. Hold every other carrier at a cap $\bar K\le K^\ast$. (i) If $\bar K<K^\ast$, a laggard just below the cap returns to it. At $\bar K=K^\ast$ it returns iff $\Gamma_0\,\frac{n-1}{n}<1+\frac{\delta_f(n-1)}{n\,d_K}$, with $\Gamma_0=(1-\beta)r\omega_K$ the gain without diffusion; without diffusion, iff $\Gamma<n/(n-1)$. (ii) Standing is restored from every starting point iff the laggard's net inflow exceeds its depreciation at every level below the cap. When $r>1$ that needs inflow not tied to rank: sharing, provision or diffusion; without all three, laggards below a threshold are excluded, and $\beta\kappa_c\Omega/n+k_0\ge d_K\bar K$ suffices.*

Scope adds: *others held at the cap (their inflow at the cap exceeds depreciation plus diffusion loss, which $\bar K<K^\ast$ with $d_K(K^\ast-\bar K)\ge\delta_f\bar K/n$ guarantees).* The sentence after the proposition becomes: *"stop at a point of enough, which holds globally only with inflow not tied to rank: sharing, provision, or diffusion"*; and the bold sentence keeps provision as what makes non-convertible rewards work and a point of enough hold, adding that diffusion, the openness of knowledge, is the third such flow (which is why §10 counts open diffusion as a restoring flow, not only as an erosion of leads).

**(b) Proof.** With the others at $\bar K$ and diffusion toward the mean $\bar X=(K+(n-1)\bar K)/n$, the laggard's net inflow is
$$\phi(K)=\kappa_c\Omega\Big[(1-\beta)\frac{K^r}{K^r+(n-1)\bar K^r}+\frac\beta n\Big]+k_0-d_KK+\delta_f\frac{n-1}{n}(\bar K-K).$$
At the cap $\phi(\bar K)=\kappa_c\Omega/n+k_0-d_K\bar K=d_K(K^\ast-\bar K)$: positive for $\bar K<K^\ast$ (a laggard just below returns), zero at $\bar K=K^\ast$, where the sign just below is that of $-\phi'(K^\ast)$:
$$\phi'(\bar K)=\frac{(1-\beta)\kappa_c\Omega\,r(n-1)}{n^2\bar K}-d_K-\delta_f\frac{n-1}{n}=d_K\Big[\Gamma_0\frac{n-1}{n}-1\Big]-\delta_f\frac{n-1}{n}\quad\text{at }\bar K=K^\ast,$$
using $\kappa_c\Omega/n=d_K\omega_KK^\ast$. Hence (i). For (ii): return from $K$ iff $\phi>0$ on $(K,\bar K)$. As $K\to0^+$ with $r>1$ the contest term is $O(K^r)=o(K)$, so $\phi(K)=\phi(0^+)-d_KK+o(K)$ with $\phi(0^+)=\beta\kappa_c\Omega/n+k_0+\delta_f(n-1)\bar K/n$; if this is zero, $\phi<0$ near zero and laggards below a threshold are excluded; if positive, exclusion needs $\phi$ to dip below zero somewhere, which $\beta\kappa_c\Omega/n+k_0\ge d_K\bar K$ rules out since then the non-contest inflow alone exceeds $d_KK$ for all $K<\bar K$. $\square$ Note that equality of the cap is the interesting boundary: for $1<\Gamma\le n/(n-1)$ equal standing is unstable without a cap, yet a cap at exactly $K^\ast$ holds a laggard, because the cap stops the leaders from pulling away.

**(c) Tag.** [thm]; the diffusion example [num].

**(d) Checks.** `f3(A)`: ten cases of the local condition at $\bar K=K^\ast$, each predicted and observed (returns/falls away) in agreement, including $n=4,r=2$ with $\delta_f=0.3$ (returns), $\delta_f=0.1$ (falls to a stalled $0.48K^\ast$) and $\delta_f=0$ (excluded), and a case with provision $k_0=0.05$ ($\Gamma_0(n-1)/n=1.026$: falls away). Strictly lower caps ($0.98K^\ast$, $0.9K^\ast$) at $\Gamma=3$: returns. Codex's diffusion case ($n=2,r=2,\delta_f=0.6$, no sharing or provision): restored from $K=0.01$, $\min\phi=0.0007>0$. Necessity: $\beta=k_0=\delta_f=0$, laggard from $0.3\bar K$ excluded ($10^{-324}$); with $\delta_f=0.05$ alone it stalls at $0.36\bar K$ ($\phi(0^+)>0$ but $\min\phi<0$): diffusion is a source, not a guarantee.

---

## 4. The sign of $d$ by channel, and the shared-parameter table (Codex 2, Sys I1)

**(a) Statement.** From (2), with $r_j,\omega_j$ fixed, $\partial\Gamma/\partial d_j=(1-\beta)r_j\omega_j\delta_{f,j}/(d_j+\delta_{f,j})^2\ge0$, and $\partial\Gamma_\delta/\partial d_j$ has the sign of $\delta(1-\delta+\delta\delta_{f,j})>0$. So for a *ratio-form* channel ($\sigma=r\ln K$, decisiveness independent of the level) faster depreciation leaves $\Gamma$ unchanged without diffusion and raises it with diffusion, and always raises $\Gamma_\delta$ (a smaller stock makes a unit of winnings count for more). For a *level-form* channel ($\sigma=aZ$, rule support offsetting a cost, as in the field model) $r_j=aZ^\ast=a(\kappa_j\Omega/n+k_{0j})/d_j\propto1/d_j$, so correction lowers $\Gamma$ and $\Gamma_\delta$. The field model's $d_i$ in $G_{ij}=a_ib_{ij}/(c_id_i)$ is of the second kind.

**Repair of the tables (§2 "Why" box, §7.1, S7).** Split the row "correction rate $d$":
- *correction of rule support (level-form)*: loop gain ↓, working objective ↓ (via $\Gamma_\delta$), enforcement ↓ (sanctions survive), capture certificate ↓, talk ↓, tempo/coverage ↓ — the V6.1 row;
- *depreciation of capacity (ratio-form)*: loop gain 0 without diffusion, ↑ with; working objective ↑ ($\Gamma_\delta$ rises); enforcement ↑ (with $\Gamma$ fixed above one the gap multiplier $1+(d+\delta_f)(\Gamma-1)$ rises with $d$: leads open faster); other columns —.

"Why" box: *"Sharing, provision that does not have to be won, and diffusion lower it in every channel; correction lowers it in the channels whose strength rises with the level of the stock, such as rule support, and not in ratio-form channels such as capacity, where faster depreciation leaves it unchanged without diffusion and raises it with diffusion (Proposition 2.3)."* Each row of the S7 table gets four entries, as the synthesis asks: intervention; what is held fixed; the model giving the sign; interfaces not proved. Test Γ (§7.4) is reversed: provision lowers $\Gamma_\delta$, raises $\theta_\Gamma$ and so raises the weight on shared harm; the clean observable is the ratio of marginal responses of intensity to the shared loss and to private cost, $\partial e/\partial\ell\div\partial e/\partial c=1+\theta$ from $e(\theta)$ of Proposition 3.6(1).

**(c) Tag.** [thm] (comparative statics of (2)); the table entries that cross models stay [conj] by S7's own rule.

**(d) Check.** `f3(B)`: $n=2$, $\kappa\Omega=1$, $k_0=0.2$, $\delta_f=0.1$. Ratio form: $d=0.1,0.2,0.3,0.6\Rightarrow\Gamma=0.71,0.95,1.07,1.22$, spectral radius $0.943,0.986,1.029,1.157$: stable, stable, unstable, unstable. Level form ($a=1.2$): $\Gamma=3.0,2.0,1.5,0.86$, radius $1.40,1.30,1.20,0.90$: correction stabilizes. (Independent: the radius is computed from the nonlinear map's numerical Jacobian, not from (2).)

---

## 5. Remark S2.1 (`tdec`)

**(a) Statement.** *In the linearized single-channel loop a relative gap grows by $\lambda^\ast=1+(d_K+\delta_f)(\Gamma-1)$ a period; with several channels by the Perron root $\lambda^\ast$ of (S1), which is not a function of $\Gamma$ alone: at equal $\Gamma$ a slow channel opens leads slowly. The time from a gap $\varepsilon_0$ to a decisive level $\bar\Delta$ is about $\ln(\bar\Delta/\varepsilon_0)/\ln\lambda^\ast$ [num: 1% to 50% in 12 periods at $\Gamma=3$, $d_K=0.2$, $\delta_f=0$; 41 at $\Gamma=1.2$ when the gain sits on a channel with turnover 0.5, 980 when it sits on one with turnover 0.02].* S13's interface row: "$T_{\rm dec}$ set by $\lambda^\ast$", and "$\Gamma$ decides the sign, $\lambda^\ast$ the speed".

**(b) Proof.** $J=1-d-\delta_f+\frac1n uv=1-d-\delta_f+(1-\beta)r\omega d=1+(d+\delta_f)(\Gamma-1)$, since $\frac1nuv=(1-\beta)r\omega d$ and $\Gamma=(1-\beta)r\omega d/(d+\delta_f)$. $\square$

**(c) Tag.** [thm]; numbers [num].

**(d) Check.** `f3(C)`: exact multiplier from the nonlinear Jacobian equals $1+(d+\delta_f)(\Gamma-1)$ in four cases (1.4000, 1.1000, 1.0500, 0.7400) while the text's formula gives 1.4000, 1.0667, 1.0250, 0.8960; two-channel secular roots 1.1000, 1.0040, 1.0092 at the same $\Gamma=1.2$.

---

## 6. `blind` (Lemma 3.3(3))

**(a) Core form.** *3. Evasion. If carrier $k$ can evade a constraint costing it $c_k$ against an expected sanction $s_k$, compliance survives cumulative payoff-monotone selection iff $s_k\ge c_k$ for every type that can evade. If the sanction falls as evaders spread, because detection is funded by compliers or rule-making is captured by evaders, and it exceeds the cost at full compliance and falls below it at full evasion ($s(0)>c>s(1)$), compliance and evasion are both stable, separated by the tipping share $x^\dagger$ with $s(x^\dagger)=c$; if $s(1)\ge c$ compliance is globally stable, if $s(0)\le c$ evasion is.*

**(b) Proof.** As V6.1, with the root's existence supplied by the endpoint conditions and the intermediate value theorem; the two one-sided cases follow because $c-s(x)$ then has one sign on $(0,1)$. $\square$ **(c)** [thm]. **(d)** `f4(A)`: four sanction schedules, replicator from $x_0=0.05,0.5,0.95$: bistable with tipping 0.375 and 0.750 when $s(0)>c>s(1)$; a single global attractor when $s(0)<c$ (evasion) or $s(1)>c$ (compliance).

---

## 7. `boundary`, `standprice`, W_i and the divisible/positional split (Adv-Opus I2)

**(a) Statements.** Two distinct things are now called "error":

- *The boundary error* (Proposition 3.6(2)): a held self-model $\theta_0<\kappa$ against the real coupling lowers its holder's welfare. This is an error about the world.
- *The working objective under compounding* (Proposition 3.9): an actor with accurate $\theta_0=\kappa$ computes correctly that a relative unit buys future winnings, and acts on $\theta_{\rm eff}<\kappa$, below the isolated self once $\Gamma_\delta>\frac{n\kappa}{(n-1)(1+\kappa)}$ (solve $\theta_\Gamma(\kappa)=0$; for $\kappa=0.4,n=4$: 0.38). This is individually accurate and collectively self-defeating: a dilemma, not a mistake.

So §3.8's "Ψ is locally rational and systemically false" becomes *"individually rational, collectively self-defeating, and false as a doctrine about nature"*, and the §3 claim box's "the narrow boundary is an error" is restricted to the held model. **The coupling $\kappa\ge0$ in (8) is the divisible part.** The positional prize $\Omega_s$ of §10.2 (decisive standing, subordination) is coupling of the opposite sign: another's gain in it is my loss. Write $W_i=\pi_i+\kappa_e\bar\pi^{e}_{-i}+\kappa_s\bar\pi^{s}_{-i}$ with $\kappa_e\in[0,n-1)$ on divisible payoffs and $\kappa_s\in[-1,0]$ on positional ones; Proposition 3.6 holds for the divisible part, and on the positional part relative accounting is accurate (Grieco 1988; Powell 1991 in X1). This also clears the apparent conflict with $U_i$, $L_b$ in 5.4(5) and S0, which are positional.

**(c) Tag.** [thm] for the threshold $\Gamma_\delta^\ast=n\kappa/((n-1)(1+\kappa))$ (algebra of (9)); the reading is [def]/[val].

**(d) Check.** Adv-Opus `adv_checks.py` §2 computed the threshold; it is an algebraic consequence of (9), so no new numerics are needed; `f1(A)` covers (9) itself.

---

## 8. `onegroup` (Lemma 3.10)

**(a) Core form.** *Let a trait cost its bearer and benefit every member of the population equally. Under every partition into groups and every payoff-monotone rule, the total selection term of the Price equation and every within-group term are non-positive; the between-group term is non-positive when fitness is affine in payoff, and can take either sign otherwise, without changing the total. The trait can rise only through the transmission term, or through a rule that changes the bearer's relative payoff.*

**(b) Proof.** With $w_j=\varphi(\pi_j)$, $\varphi$ increasing, $\pi_j=w_0+bz_{\rm pop}-cz_j$: $w_j$ is a decreasing function of $z_j$, so $\operatorname{Cov}(w,z)\le0$ over the population and within every group (Chebyshev's sum inequality). For affine $\varphi$, $\bar w_g=\varphi(w_0+bz_{\rm pop}-c\bar z_g)$ is decreasing in $\bar z_g$, so the between term is $\le0$. For nonlinear $\varphi$, $\bar w_g$ depends on the within-group spread as well as the mean (Jensen), so $\operatorname{Cov}_g(\bar w_g,\bar z_g)$ can be positive; the total is unchanged since the decomposition is an identity. $\square$ Conclusion of the lemma unchanged.

**(c) Tag.** [thm].

**(d) Check.** `f4(B)`: 600 random populations ($N\in[6,40]$, random $b,c$, random partitions into 2–6 groups), four families of increasing $\varphi$ (affine, concave $-e^{-kx}$, convex $e^{kx}$, mixed $x+0.9\sin(kx)/k$): total $>0$ in 0/600, any within-group term $>0$ in 0/600, between-group $>0$ in 13/600, none of them affine. Codex's instance reproduced (between $+0.00920$, total $-0.11496$). The PR block of `checks_v62.py` needs a nonlinear case (§28).

---

## 9. `corrrate` (Proposition 4.5), `costq` and $\hat Y$

**(a) Core form.**

> **Assumption 4.2.** *... pays $\mathcal C(q;p)=f\,p^{\xi_f}q+\gamma\,p^{\xi_v}q^{1+\eta}/(1+\eta)$: $f$ is a per-unit (marginal) cost of capacity, such as a statutory procedural cost per unit of influence, not a lump sum; $\gamma$ the variable cost. [$H_\gamma$], [$H_f$] as before. Capacity is at its selected level at every date (quasi-static); Proposition 4.5 states what survives when it is not.*
>
> In §4.3, after (11): *with $\hat Y=p^2\bar y^\top\hat A\bar y$ the cultivated return per unit of capacity and of $1/d$, selected capacity is $q^\ast=\big[(\chi\hat Y/d-fp^{\xi_f})_+/(\gamma p^{\xi_v})\big]^{1/\eta}$.*
>
> **Proposition 4.5.** 1. [as V6.1]
> 2. *(Rate law.) Under $[H_\gamma]$ with $d(t)=d_0e^{\alpha_{\rm cor}t}$, a positive cultivation channel, long horizons and $f=0$. Sufficient: if $\alpha_{\rm cor}\ge\alpha_{\rm ctl}/(1+\eta)$ and $d_0>d^\ast(\gamma_0)$, the certificate holds for all $t$, whatever the speed at which capacity adjusts, provided it never exceeds its selected level. Necessary: if $\alpha_{\rm cor}<\alpha_{\rm ctl}/(1+\eta)$ the certificate fails beyond a finite time whenever capacity keeps a positive fraction of its selected level ($\liminf q/q^\ast>0$): for optimizing carriers, for adjustment at a constant rate $k$, where failure is delayed by about $\eta\ln(1+g/k)/(\alpha_{\rm ctl}-(1+\eta)\alpha_{\rm cor})$ with $g=(\alpha_{\rm ctl}-\alpha_{\rm cor})/\eta$, and for gradient dynamics whose variance grows with capacity; not for gradient dynamics with constant variance, whose adjustment rate falls with the cost of control and whose capacity stays bounded, so that the certificate then holds eventually for every $\alpha_{\rm cor}>0$. This holds for every size elasticity $\xi_v$.*
> 3. *(Marginal-cost floor.) With $f>0$, capacity is cultivated only while $d(t)<d_f(t)=\chi\hat Y/(f(t)p^{\xi_f})$; if $f$ does not fall the requirement levels off at $\max\{A/c_{\rm ev},d_f\}$. Under $[H_f]$, $d_f$ rises at $\alpha_f$. If $\alpha_{\rm cor}>\alpha_f$ cultivation ends at a finite date and the certificate thereafter needs only $d>A/c_{\rm ev}$; if $\alpha_{\rm cor}<\alpha_f$ the rate law of (2) decides; if $\alpha_{\rm cor}=\alpha_f$ nothing is cultivated when $d_0\ge d_f(0)$ and (2) decides otherwise. In every case the certificate must also hold through the transient, which a bounded cultivated term does not guarantee [num]. A true fixed cost, paid once if any capacity is held, delays cultivation (threshold exponent $\eta/(2\eta+2-\xi_v-\eta\xi_f)$) and does not cap it.*
> 4. [as V6.1]

Scope: *"The quasi-static model is conservative while the cost of control falls monotonically (failure is earlier than under any lag), and optimistic after a reform is withdrawn and wherever correction itself rests on a slow variable that the contest erodes (S4, Proposition S4.x)."* The paragraph after 4.5: "a fixed cost of control AI does not lower" → "a per-unit cost of control that AI does not lower, or lowers more slowly than correction grows"; S4's "that level falls at $\alpha_f$" → rises; R3a accordingly (§23).

**(b) Proofs.** (2) *Sufficient.* $G_{\rm ev}(t)=A/(c_{\rm ev}d)+a_{\rm ev}\hat Bp\,q(t)/(c_{\rm ev}d)$ and $q\le q^\ast$ give $G_{\rm ev}\le G^{\rm QS}_{\rm ev}$, which is nonincreasing when $\alpha_{\rm cor}\ge\alpha_{\rm ctl}/(1+\eta)$ (first term decreasing, cultivated term $\propto e^{(\alpha_{\rm ctl}-(1+\eta)\alpha_{\rm cor})t/\eta}$ nonincreasing), so $G_{\rm ev}(t)\le G_{\rm ev}(0)<1$. *Necessary.* If $q\ge\rho q^\ast$ eventually with $\rho>0$, the cultivated term is at least $\rho$ times the quasi-static one, which $\to\infty$. Constant-rate lag: $\dot q=k(q^\ast-q)$ with $q^\ast\propto e^{gt}$ gives $q/q^\ast\to k/(k+g)$, and the failure date shifts by $-\ln(k/(k+g))/[(\alpha_{\rm ctl}-(1+\eta)\alpha_{\rm cor})/\eta]$, the stated delay. Constant-variance gradient: $\dot q=V(\chi\hat Yp^{2-\xi_v}/d-\gamma p^{\xi_v}q^\eta)\le V\chi\hat Yp^{2-\xi_v}/d(t)$, so $q(t)\le q_0+V\chi\hat Yp^{2-\xi_v}/(d_0\alpha_{\rm cor})$, bounded, and $G_{\rm ev}\to0$. Variance $\propto q^2$: the relaxation rate $\propto Vq^{\ast2}\gamma\propto e^{(\alpha_{\rm ctl}-2\alpha_{\rm cor})t}$ grows below the threshold ($2\alpha_{\rm cor}<\alpha_{\rm ctl}$), so $q/q^\ast\to1$. (3) $q^\ast>0$ iff $\chi\hat Y/d>fp^{\xi_f}$ iff $d<d_f$. Under $[H_f]$, $d/d_f=(d_0/d_f(0))e^{(\alpha_{\rm cor}-\alpha_f)t}$: the three cases follow; when $d/d_f\to0$ the bracket $(1-d/d_f)^{1/\eta}\to1$ and $q^\ast$ is asymptotically the $f=0$ value. Lump sum: the maximized surplus at $q^\ast_{f=0}$ is $\frac{\eta}{1+\eta}q^\ast\chi\hat Yp^{2}/d\propto p^{2+(2-\xi_v)/\eta}$, positive against $Fp^{\xi_f}$ iff $p>p^\ast\propto F^{\eta/(2\eta+2-\xi_v-\eta\xi_f)}$; as $\gamma\to0$ the surplus grows without bound so the lump sum never binds. $\square$

**Where a reviewer is incomplete.** Math-Opus (minor 2) proposes "$\alpha_{\rm cor}>\alpha_f$; or $\alpha_{\rm cor}\ge\alpha_f$ and no initial cultivation; or $\alpha_{\rm cor}\ge\alpha_{\rm ctl}/(1+\eta)$ and $d_0>d^\ast$" as the corrected requirement. The first alternative is not sufficient: cultivation ends at $T_f=\ln(d_f(0)/d_0)/(\alpha_{\rm cor}-\alpha_f)$, which is long when $\alpha_{\rm cor}-\alpha_f$ is small, and the cultivated term grows meanwhile at rate $(\alpha_{\rm ctl}-(1+\eta)\alpha_{\rm cor})/\eta$. `f5(B)`: $f_0=0.1$, $\alpha_f=0.05$, $\alpha_{\rm cor}=0.051$: cultivation ends at $t=588$ but the certificate fails at $t=38.4$ (peak $G_{\rm ev}=2\times10^{21}$). Codex's reading of part (2) is right; the correct repair is the three-case statement plus the transient clause.

**(c) Tags.** (2) sufficient half [thm]; necessary half [thm] under the tracking premise; the named dynamics [thm] (constant-rate, bounded GA) and [num] (GM). (3) [thm]; transient clause [num]. Lump-sum exponent [thm].

**(d) Checks.** `f5(A)`: QS/R(0.3)/R(0.1)/R(0.03)/GA(1)/GM(1) failure dates at $\alpha_{\rm cor}=0.05$: 28.8/32.9/38.1/46.9/never/28.9; at 0.09: 145.9/161.5/183.0/222.9/never/146.2; at 0.11 none. Delay vs formula: 4.11/4.05, 9.29/9.16, 18.11/17.92 ($\alpha_{\rm cor}=0.05$); 8.40/8.41, 19.70/19.71, 40.23/40.24 (0.08). GA bound: $q(600)=7.29\le9.18$, $2.18\le3.78$, peak $G_{\rm ev}$ 0.51, 0.20. `f5(B)`: Codex's $q^\ast$ hits zero at $t=0.505$ and stays; the $3\times5$ table of $(f_0,\alpha_{\rm cor})$ cases; $d_f$ rising 1.20, 1.98, 3.26. `f5(C)`: lump-sum exponents 0.2500, 0.5000, 0.3333, 0.2500 equal the formula; $d^\ast$ with the linear floor levels off at 1.200 while with a lump sum it tracks $f=0$ (4.65, 46.5, 465). `f5(D)`: $d\ln q^\ast/d\ln p=(2-\xi_v)/\eta$ in four cases.

---

## 10. `slowroute` (Theorem 4.12)

**(a) Core form.**

> **Theorem 4.12 (Silent crossing when capture precedes evidence) [thm∣prem].** *Assume (reach) and: (a) replicator selection among carriers differing only in load, a race carrier present, cumulative advantage unbounded on every alarm-free continuation; (d) a fixed averaged alarm with $0\le m_{\rm out}<m_{\rm fl}<m_{\rm in}<1$; (e) capture before evidence: $x_{\rm ev}(t)>(m_{\rm fl}-m_{\rm out})/(m_{\rm in}-m_{\rm out})$ whenever $V_{\min}\le V(t)\le V_{\rm alarm}$. Then the host crosses its floor before any alarm. If instead $m_{\rm in}\le m_{\rm fl}$ [as V6.1].*
>
> *What makes (e) plausible.* Appropriable control with a falling cost of control and correction growing more slowly than the rate law ((b), (c) of V6.1) drive $x_{\rm ev}\to1$ (Proposition 4.5(2)); they do not imply (e), which compares two clocks: the time for the host to reach the alarm band under the race load, $T_A=(\rho-h_V\bar e)^{-1}\ln[(1-V^\ast/V_0)/(1-V^\ast/V_{\rm alarm})]$ when $h_V\bar e<\rho$ and finite in any case, and the time for $x_{\rm ev}$ to pass the masking threshold. *With (b), (c) and the clock premise $T_{\rm cap}<T_A$ in place of (e), the theorem holds [thm∣prem].* Acceleration brings both clocks forward, so (e) is a condition to check (TESTS, Study 2).

**(b) Proof.** As S4 with the second sentence (the use of (c)) deleted; the clock version: (b),(c) give $x_{\rm ev}(t)\uparrow1$, so the threshold is passed at a finite $T_{\rm cap}$ and $x_{\rm ev}$ stays above it; if $T_{\rm cap}<T_A$ then (e) holds on the band, and Proposition 4.7 applies. $\square$

**(c) Tag.** [thm∣prem] both ways; the title no longer says "no viable race".

**(d) Check.** `f7(F)`: $\rho=0.05$, $h_V=0.08$, floor 0.3, alarm 0.6, $m_{\rm in}=0.5$ ($m_{\rm fl}=0.43$, threshold $x_{\rm ev}>0.857$): with capture complete by $t\approx3.6$ the alarm never fires and the floor is crossed at $t=21$ (silent); with capture midpoints 20 or 45, $x_{\rm ev}\to1$ still holds but the alarm fires at $t=7.4$, before the floor: (b),(c) without (e).

---

## 11. `enforce` (Proposition 5.4)

**(a) Core form.** Part (1): *$a^\ast$ is sustained by reversion to that punishment iff, for every $i$ and every deviation $a_i'$, with its own gain $g_i(a_i')$ and its own breakout probability $p_d(a_i')$,* (14) *holds. If $p_d$ is common to all deviations, the deviation with the largest gain binds.* Part (2) unchanged (monotonicities weak at the edges of $[0,1)$). Part (5): *If punishment is reversion to a stage equilibrium in which both race, worth $P_i$, and in each period at most one racer breaks out, each with probability $q\le\tfrac12$, being subordinated worth $U_i$, then $v_i=[(1-\delta)P_i+\delta q(D_i+U_i)]/(1-\delta+2\delta q)$; with independent breakouts and a simultaneous breakout leaving the race as it was, replace $q$ by $q(1-q)$. When $D_i+U_i>2P_i$, reversion to the race is a lottery the deviator welcomes, and can fail to deter even where the deviation itself never breaks out and cooperation is still preferred to the race* [num: $C=1$, $P=0$, $D=4$, $U=0$, $g=2$, $\delta=0.9$: restraint is enforceable at $q=0$ and not at $q=0.045$, where $v=0.895<C$].

Remove the V6.1 example ($q=0.1$, $v=1.29>C$): there both prefer the race-with-breakouts to cooperation, which is a different point (and keep it in S5 as that different point).

**(b) Proof.** (1) The one-shot deviation principle holds deviation by deviation; (14) with $(g_i(a'),p_d(a'))$ is the no-gain condition for $a'$. (5) $V_P=P+\delta[q\frac{D}{1-\delta}+q\frac{U}{1-\delta}+(1-2q)V_P]$ requires the three events to partition the period, so $q\le\tfrac12$; with independent breakouts the exclusive probabilities are $q(1-q)$ each and $q^2+(1-q)^2$ for "race continues", giving the same closed form in $q(1-q)$. $\square$

**(c) Tag.** [thm]; the example [num].

**(d) Checks.** `f6(A)`: $C=3,D=6,v=1,\delta=0.9$: deviation X ($g=1,p_d=0.1$) deterred ($V_{\rm dev}=17.5<30$), deviation Y ($g=0.2,p_d=0.6$) not ($39.2>30$). `f6(B)`: closed forms against value iteration on the explicit chain, exclusive and independent, $q=0.045,0.1,0.3$ (all agree); the new example (deterred at $q=0$, not at $q=0.045$, $v=0.895$); $q=0.6$ exclusive invalid ($1-2q<0$), independent form valid ($v=1.624$).

---

## 12. `relpunish` (Corollary 5.5)

**(a) Core form.** *Let the stage game be symmetric, every actor hold $\theta=-1$, and the stochastic game be exchangeable: stage payoffs and transitions invariant under relabelling the actors, so that no state carries a label that changes payoffs or transitions, though strategies may condition on who deviated. Then every symmetric profile gives each 0. With two actors every punishment, mixed or pure, leaves the punished at least 0, since it can mirror the punisher in an exchangeable zero-sum game; with $n\ge3$ in an anonymous game, so does every punishment in which all punishers use the same strategy. A symmetric cooperative profile is then sustainable only if $(1-\delta)g_i+\delta p_dD_i\le0$, and when $D_i\ge0$ only if it is a stage equilibrium in objectives.*

Scope: *A decisive position reached through an exchangeable lottery is covered; one assigned by label to the "target" is not, and relative actors can then sustain non-stage cooperation (S14). With $n\ge3$, punishers in different roles can hold a relative deviator below zero; in the three-player example that punishment is a weak stage equilibrium, strict under small symmetric perturbations and destroyed by a small asymmetry of the opposite sign; which punisher takes which role is an equilibrium-selection problem, since both prefer the same role [num].*

**(b) Proof.** Under exchangeability the mirrored strategy pair (the punished playing, at every state, what the punisher would play with the roles swapped) makes the joint distribution of the two payoff streams exchangeable, so the expected relative payoff is zero at every period; the stage argument ($y^\top Ay=0$ for antisymmetric $A$) is the one-period case. $\square$

**(c) Tag.** [thm]; strictness clauses [num].

**(d) Checks.** `f6(D)`: (i) an exchangeable continuation (Tullock lottery with absorbing $\pm10$ at probability 0.3 a period): mirrored relative value $0.000000$; (ii) Codex's label-dependent continuation: target's value $-8.18$, deviation worth $-69.6<0$ (cooperation sustained among relative actors). `f6(E)`: the printed game: margins $[0,0,0.2]$ (weak NE); $+0.02$ on the X prize: $[0.01,0.01,0.2]$ (strict); $-0.02$: $[-0.01,-0.01,0.2]$ (not an equilibrium). Opus's 400/400 strict under anonymous perturbations stands.

---

## 13. `restraint` (Corollary 5.6)

**(a) Core form.** *... Where $p_d\to1$ and $D_i\ge C_i$, durable restraint requires $p_d\le\bar p_{d,i}$ for every $i$, by two kinds of means: (a) changing the premise itself, so that deviations do not become decisive: not building capability of the decisive class, holding it so no party can use it alone, or detecting and answering faster than breakout; (b) raising $\bar p_d$ ...* **(c)** [thm], a classification. No check needed beyond `f6`.

---

## 14. `coverage` (Theorem 5.12)

**(a) Core form.** *Under (coverage lags) and (residual floor), for every $\varepsilon\in(0,1)$ there is $T_\varepsilon$ with $\Pr(\Phi_H)\le(1-h(1-\varepsilon))^{H-T_\varepsilon}\to0$. Conversely [as V6.1].* (variety grows) moves to the paragraph before, as what makes (coverage lags) plausible on the continuation branch ("hazardous variety grows at least exponentially while coverage grows at human rates"); R5's "not needed when" list keeps it. **(b)** The S5 proof uses only the two premises. **(c)** [thm∣prem] with two named premises.

---

## 15. `talk` (Proposition 5.15(2))

**(a) Core form.** Title: *Between two rivals relative accounting silences talk; among three or more it amplifies a pair's conflict by $n/(n-2)$, a factor that falls toward one as $n$ grows.* Part (2): *With $n\ge3$ actors at $\theta=-1$, $J_S-J_R=\frac{n}{n-1}(\pi_S-\pi_R)$: what the receiver's action does to third parties enters both alike. In the uniform-quadratic model with third parties affected linearly, a material bias $b_0$ between them becomes $b_0n/(n-2)$, and informative talk exists iff $b_0n/(n-2)<1/4$.* The sentence after: *"Rivals stop informing one another; that pairs then talk as blocs against third parties is a reading, not a result [conj] (compare Snidal 1991: the force of relative gains falls with the number of actors)."* §1.2(4) and 导读 the same.

**(b) Proof.** As S5; the ideal points: $y_S-u=\frac{b_0(n-1)}{n-2}-\frac{L}{2(n-2)}$, $y_R-u=-\frac{b_0}{n-2}-\frac{L}{2(n-2)}$ with $L$ the summed slope of third-party payoffs; difference $b_0n/(n-2)$, independent of $L$. **(c)** [thm]; bloc reading [conj]. **(d)** Opus's `s5_misc` (nonlinear third-party term: still $b_0n/(n-2)$ in state units) and V6.1's T3 suffice.

---

## 16. The scissors (§5.5, Remark S5.1, Test G)

**(a) Core form.** *The scissors, stated exactly [each arm thm; conjunction conj].* *Growth in the stakes relative to provision, and a falling cost of control, (i) raise $p_d$ where they raise the gap multiplier $\lambda^\ast$ (Remark S2.1); (ii) lower $\bar p_d$ where the stakes of deviation and of a decisive position, $g$ and $D-C$, grow faster than the value of cooperation over punishment, $C-v$ ($\bar p_d$ is homogeneous of degree zero in $(g,C,D,v)$); (iii) weaken the sanction where correctors are captured (Section 4); (iv) move working objectives toward the relative one where the relative return to reinvestment exceeds its common return (Proposition 3.9). Each arm is proved in its model; that they move together in the world is conjecture C0 [num: in a reduced form with non-responding rivals and $\theta_0=0$, the largest enforceable discounted loop gain falls from 0.92 at $p_d=0$ to 0.39 at $p_d=0.9$, and none exists above $p_d\approx0.95$ (0.98 for $\theta_0=0.4$)].* Remark S5.1 and Test G: *"the restraint gap between wider and narrower objectives grows with $p_d$ over the range in which the wider objective still sustains restraint; when a decisive position is worth more than cooperation the gap closes as $p_d\to1$, where no $\theta\le n-1$ sustains restraint (Proposition 5.4(4)) and this theory and structural realism agree; the test discriminates at intermediate $p_d$."*

**(b) Proof of (ii) and the hump.** $\bar p_d=1-[(1-\delta)g+\delta(D-C)]/[\delta(D-v)]$ is unchanged when $g,C,D,v$ scale alike; it falls when $g$ and $D-C$ grow at fixed $C-v$. With $D>C$ at $p_d=1$ the condition is $(1-\delta)g\le\delta(C-D)<0$, impossible for $g\ge0$, so the enforceable set is empty for every $\theta\le n-1$ and the gap is zero. $\square$

**(c) Tags.** As stated. **(d)** `f6(F)`: by direct discounted streams, $\theta_{\rm rep}(p_d)=-0.901,-0.812,-0.322,+0.005,+0.634,+0.937$ at $p_d=0,0.5,0.9,0.95,0.99,1$; $\theta_0=0$ loses enforced restraint at $p_d=0.9495$, $\theta_0=0.4$ at 0.9793; gap profile monotone at $D=C$ ($+0.05\ldots+0.97$) and hump-shaped at $D=0.5$ ($+0.05,+0.30,+0.92,+0.33,0,0,0$). Also `f6(C)` for R4.

---

## 17. `delegatelock` (Proposition 6.4)

**(a) Core form.** *If $q_L=1$, then for every finite speed, every $n$, every $p$ and every profile of the others, not delegating gives strictly higher survival, and no one delegating is the unique equilibrium. If $q_L<1$ and losing means subordination with certainty ($p=1$), at least one of all-delegating and no-delegating is an equilibrium, and both can be; with $p<1$ the gain from delegating can fall as others delegate, and an interior profile can be the only pure equilibrium [num].* §11.3 and tier 1: *"a strict equilibrium among informed actors who price in a lock they take to be certain ($q_L=1$)"*; X11's "lock near-certain in narrow domains" moves into the core sentence.

**(b) Proof.** As S6 for $p=1$. For $p<1$, $\Phi_D/\Phi_N=(1-q_L)a\,[1-p+pw_D(k)]/[1-p+pw_N(k)]$ with $w_D=(1+s)/(n+(k+1)s)$, $w_N=1/(n+ks)$; both $w$ fall in $k$ and the ratio can cross one from above, which excludes both corners. $\square$ **(c)** [thm]; interior example [num]. **(d)** `f7(A)`: Codex's case ($n=3,s=1,p=0.1,q_L=0,\psi_1=0.015$): ratios 1.00259, 1.00097, 0.99928 for $k=0,1,2$; the only pure equilibrium has two delegators; with $p=1$ the ratios rise with $k$ (1.48, 1.58, 1.64) and all-delegating is the equilibrium.

---

## 18. `nested` (Proposition 6.7) and R8

**(a) Core form.** Premise added to the proposition: *Assume $(A_\tau)$ and that for every developer that counters the divergence there is an admissible variant identical in everything else that does not (a matched unsafe variant), as the symmetry convention (A7) supplies.* (2): *under $(A_\tau)$ developers that counter the divergence lose share to their matched variants, tending to zero; a safeguarding developer with a higher baseline can outgrow an unsafe one with a lower baseline, so the result is about variants, not about every pair of firms.* (3): *a constraint enforced on every developer as a condition of admission survives evasion iff the expected sanction is at least each developer's gain from evasion, a sanction itself subject to Section 4; when its incidence is equal it is also neutral among compliers, preserving their relative shares, and when unequal it selects among compliers without reintroducing the divergence.* Line 525: *"where the tax is negative the safeguard spreads without coordination; where it is zero it is neutral."*

R8 (Proposition 9.1): *necessary:* common admission constraints sanctioned against evasion, with decisions retained by performance only inside them; *neutrality clause, not necessity:* equal incidence preserves shares among compliers; *limitation* (new column entry, not "not needed when"): admission reaches only to release, so openly released weights escape it.

**(b) Proof.** (2) with matched variants: Proposition 3.4(2), developers as carriers. (3): Lemma 3.3(2) for neutrality; Lemma 3.3(3) for survival; unequal costs among compliers are payoff differences among compliers only, so the evading variants are still selected out as long as $s_k\ge c_k$ for each type. $\square$ **(c)** [thm∣prem] ($(A_\tau)$, matched variant). **(d)** `f4(C)`: costs 0.1/0.2 with sanction 1: compliant share $0.999999975$ at $t=20$, shares among compliers 0.88/0.12; equal incidence: compliers' ratio preserved (1.000000); unmatched (baseline 2, tax 0.1 vs baseline 1): safeguarded share $\to1$; matched: $2\times10^{-9}$ at $t=200$; zero tax: shares unchanged. Codex's reading stands; the Supplement should say so (S14 row: "unequal compliance costs do not undo compliance").

---

## 19. Propositions 6.8 and 6.11(3)

**6.8 `opaquecorr`.** *... lowers residual risk iff $q_0c_b>q_c$, and makes it summable iff $\sum_t[q_0(1-c_{b,t})+q_{c,t}]<\infty$, which a fixed $c_b<1$ never does.* S6's example changes to $c_{b,t}=1-2^{-(t+1)}$, $q_{c,t}=2^{-(t+2)}$ at $q_0=0.1$: survival 0.510 at every horizon beyond 200. The V6.1 example ($c_b=0.99$ fixed) is not summable: survival 0.473 to period 200 counting from $t=0$ (0.630 counting from $t=1$, the quoted number) and $1.2\times10^{-9}$ by 20,000. S14's row "lowering residual risk to a summable sequence" cites the new example. [thm]; `f7(B)`.

**6.11(3) `homeostasis`.** *With $n=3$, $L_e=L_c=1$, $\psi_0=0$, $s_t=2^t$, $\Delta\psi_t=2^{-t}$, full delegation is an equilibrium at every $t$ (the objective is concave in own delegation and increasing at the corner), and the realized risk summed from $t=5$ is at most $3/16$; the hazard at $t=0$ alone is 1.* [thm]; `f7(C)`: full delegation is a best response on a grid at $t=0,\dots,7$; $\sum_{t\ge5}3\cdot2^{-t}=0.1875$.

---

## 20. `topology` (Proposition 6.9) and the §6.5 sentence

*"A full inbound row sum below one is a sufficient certificate that no party controls a check's funding, appointment or access (Proposition 4.7(2)); it is not necessary (S14), and it does not certify that the checks' errors are independent."* The V6.1 sentence "necessary for independent correction, not sufficient" inverts the first half. CLAIMS line 87 the same. [thm]; `f7(G)` reproduces the $(1-\rho_{\rm cc})(1-0.1^6)$ figures (1.000, 0.950, 0.700).

---

## 21. `safeguards` (Theorem 10.5(1))

**(a) Core form.** *1. Sufficiency. Under (I1)–(I4), effective liability exceeds the advantage after a finite time and the load falls to its minimum; on the host (3) the long-run level $1-h_Ve_{\min}/\rho$ exceeds the floor. The trajectory is viable iff the liability margin $\Delta=\tau_{\rm eff}-\nu$ is at least a threshold $\Delta_{\min}$ set by the host, the floor, the initial composition and the speed of selection [num: 0.108, 0.165 and 0.355 for floors 0.2, 0.3 and 0.5 with the race strategy at 99%; the text's $\Delta=0.08$ dips to 0.14]. On a host whose regeneration is lower at every level and which degrades by itself below a threshold, the margin must also keep the transient above the host's own threshold, and a shortfall is then permanent where on (3) it is recoverable.* Scope: *"an instance of a viable parameter boundary under one fixed strategy; the correctable kernel of Definition 8.x takes a union over strategies and an intersection over disturbances, and is not computed here."*

**(b) Proof.** The S10 proof gives $\liminf V>V_{\min}$; viability over the transient is a condition on the minimum of $V$ along the path, monotone in $\Delta$ (a larger margin lowers the race share faster, by comparison), so there is a unique threshold $\Delta_{\min}$. $\square$ **(c)** [thm]; margins [num]. **(d)** `f7(D)`: HO's model ($e_{\min}=0$, closed-form logit decline): $\Delta=0.08$ gives minimum 0.1397; $\Delta_{\min}=0.108/0.165/0.355$ (matching Opus independently); with $e_{\min}=0.1$: 0.125/0.192/0.414.

---

## 22. `share` (Proposition 10.3(2))

*Sharing a fraction $\beta$ of the divisible prize, kept with probability $\varrho$, is the contest with prize $\Omega_{\rm eff}=(1-\beta\varrho)\Omega_e+\Omega_s$ when the shared part is divided among all $n$, and $(1-\beta\varrho\,n/(n-1))\Omega_e+\Omega_s$ when it goes to the $n-1$ others, the convention of Propositions 3.5(4) and 5.7.* [thm]; `f7(E)`: Nash intensities 0.13125 / 0.11250 at $\beta=0.3$ and 0.07500 / 0.03750 at $\beta=0.6$ equal $r\Omega_{\rm eff}(n-1)/(n^2c)$ under each convention.

---

## 23. `require` (Proposition 9.1)

Retitle **Table 9.1 (Requirements, by the kind of support each has) [def]**, each row carrying the tag of its source result; the organizing claim is a definition, the rows are the cited results. Row changes:
- **R1**: "the upper limit of the time average of effective liability is at least the private advantage" ($\limsup$ of the running average; the proof uses exactly this).
- **R3a**: kind "necessary when capacity tracks its selected level ($\liminf q/q^\ast>0$); sufficient whatever the speed"; model column adds "quasi-static or tracking capacity"; "not needed when" adds "selection on capacity slower than the drift of its target (constant-variance gradient dynamics)", and replaces "a fixed cost of control AI does not lower" with "a per-unit cost of control that AI does not lower, or lowers more slowly than correction grows".
- **R4**: exception "$D<C$" → "$(1-\delta)g\le\delta(C-D)$, i.e. $\bar p_d\ge1$"; proof: for $D>v$ and this inequality, $(1-\delta)g-\delta p_d(C-D)\le\delta(1-p_d)(C-D)\le\delta(1-p_d)(C-v)$ for every $p_d\in[0,1]$. `f6(C)`: $D<C$ with $g=2$ fails at $p_d=0.9$ ($\bar p_d=0.864$); with $g=0.5$ ($(1-\delta)g=0.05\le0.09$) it holds at $p_d=0,0.5,0.9,1$.
- **R8**: §18.
- Sufficient safeguards paragraph: "full inbound row sums below one" stays sufficient; "the safeguards of Section 10.3, with a margin" → "with the margin $\Delta_{\min}$ on every host".

---

## 24. Tags

| Result | V6.1 | V6.2 |
|---|---|---|
| Thm 7.1, Branch I′ "can stabilize as nuclear deterrence did" | inside [thm] | split: the branch's formal content [thm]; the stabilization clause [obs] (EV row) |
| Cor 7.3 "cannot justify" | [thm∣prem] | formal part [thm∣prem]; "cannot justify as a collective course" [val] (V1–V3) |
| Thm 8.11(3) last sentence (compute accounting bound holds only if the coalition's advantage grows at least as fast as diffusion erodes it) | inside [thm] | [prem], named "(advantage keeps pace)"; S8 derives nothing for it |
| Prop 9.1 | [thm∣prem] | Table [def], rows tagged by source |
| Prop 11.5 | [thm] | [def] plus support, or restated as a capture-basin proposition (Sys I8); "graduated steps alone reach the threshold is not shown" stays |
| Thm 10.5(1) margin | prose | [num] |
| Prop 3.9 | [thm] | [thm∣prem]; (3) [num] |
| Thm 4.12 | [thm∣prem] | [thm∣prem], premises (reach),(a),(d),(e) or (reach),(a),(b),(c),(d),(clock) |
| Scissors §5.5 | [thm∣prem] | arms [thm], conjunction [conj] (C0) |
| Prop 5.15 "allies form blocs" | [thm] | $n/(n-2)$ [thm]; blocs [conj] |
| Prop 6.9 row-sum sentence | [thm] | [thm], sufficiency only |

---

## 25. Notation

The claim "each symbol has one meaning in all three documents" cannot be kept; replace by: *"the symbols of the two tables have one meaning throughout; a symbol not in them is local to the model box or proof in which it is introduced."* Rename the collisions that sit inside one section or clash with a table symbol:

| Clash | Where | Proposal |
|---|---|---|
| $J$ Jacobian vs $J_i$ objective | S2 | $\mathcal J$ |
| $\lambda$ eigenvalue vs weight on winning | S2 | $\lambda^\ast$ is kept for the Perron root only inside S2 and Remark S2.1, declared local; the weight on winning is $\lambda$ elsewhere (acceptable since S2 never uses the weight), or rename the root $\varrho_J$ |
| $D$ diagonal matrix / number of domains vs decisive value | S2, S4 | $\mathfrak D$ for the matrix; $N_D$ for the number of domains |
| $v$ deviation (Remark 2.5), $v_j$ (S2), $v_d$ (S4) vs $v_i$ punishment value | §2, S2, S4 | Remark 2.5 uses $(u,w)\to(\xi,\zeta_u)$; S2 $v_j\to\varsigma_j$ |
| $C(q;p)$ cost vs $C_i$, $\mathcal C$ captured set | §4 | $\mathcal C_q(q;p)$ or $\mathrm{Cost}(q;p)$ |
| $d$ harm coefficient in (15) vs correction rate | §6.2 | $h_d$ |
| $U_i$ subordinated value (5.4(5)), $U_t$ uniform draw (S8), $U$ contest payoff (S10) vs coverage $U$ | §5.2, S8, S10 | $L_{{\rm sub},i}$; $\upsilon_t$ → use $\xi_t$ for the uniform draw; S10 $U\to\pi^{\rm race}$ |
| $m$ non-contestants (3.11), checks per layer (6.9) vs masking | §3.6, §6.5 | $n_o$; $m_\ell$ already used in S6, adopt it in the core |
| $\tau$ detection lag (S5) vs liability | S5 | $\tau_{\rm det}$ |
| $q$ breakout probability (5.4(5)) vs conversion capacity | §5.2 | $q_b$ |
| $s$ bloc size (3.11), $s(x)$ sanction (3.3) vs speed advantage | §3 | $n_b$; $s(x)\to\varsigma(x)$ or keep $s_k$ with a footnote (it is in the table as "sanction $F$"; unify: sanction $F$, expected sanction $\bar F_k$) |
| $F,G$ maps (Def 2.4, 3.2) vs sanction $F$ | §2.3, §3.2 | maps $\Phi_x,\Phi_\sigma$ (Def 2.4 is prose; a footnote suffices) |
| $\varpi$ in $G(V)=\varpi V$ (S3) vs trust | S3 | $g_V$ |
| $\mu$ biased transmission (S3, S14) vs prior | S3 | $\mu_{\rm tr}$ |
| $\kappa_k$ cost (S3 proof of 3.3) vs convertible share | S3 | $c_k$ (as in the core statement) |
| "gain" of §7.1 (drives) vs loop gain | §7.1 | "amplifier" or "driver's weight", with one sentence that it is not a factor of $\Gamma$ but enters $\theta_\Gamma$ |

Also the three "Kind Kind" doublings ("Proposition Proposition 9.2", "Theorem Theorem 10.5(3)", "Assumption Assumption 4.2") come from writing the kind before `{{>key}}`; xref should flag the pattern.

---

## 26. Elegance: cleaner statements that unify

**(i) One loop gain, two prices.** The elegant and correct sentence is: *"The open-loop gain $\Gamma$ decides whether a lead grows; discounted, it is the open-loop gain of the actor's own future, and the closed-loop gain $\Gamma_\delta/(1-\Gamma_\delta)$ is the price of standing."* This is the closed-loop formula $L/(1-L)$ of feedback control, valid exactly where the discounted loop is stable ($L=\Gamma_\delta<1$), diverging as $L\to1^-$, and undefined beyond, where the price per unit is unbounded ($\varepsilon^{\alpha-1}$). It is one number in the fixed-strategy model. When strategies respond it splits into two gains, $\Gamma_{\rm eq}$ (stability) and $\tilde\Gamma$ (price), with the same closed-loop form (Remark S2.2). I would put the control reading in the core in one sentence and the split in the Scope.

**(ii) Compounding narrows objectives exactly where reinvestment pays relatively.** Proposition 3.9's general form says: narrowing iff $\lambda_{\rm rel}>\lambda_{\rm com}$. Specializing: fixed prize, always; proportional prize, iff $(1-\beta)r>1$. The second is Proposition 2.3(1)'s compounding condition, at every horizon. So the sentence that links 2.3 and 3.9 is: *"With a fixed prize, compounding manufactures the relative objective in every forward-looking actor; with a prize that grows with capacity, it does so exactly where leads compound."* The first half is what V6.1 claimed, now with its premise visible (a zero-sum future); the second is the correction Adv-Fable asked for, and it strengthens the thesis, since decisiveness and sharing, not the loop gain as such, are the levers.

**(iii) Three flows not tied to rank.** Sharing, provision and diffusion enter Proposition 2.3(2) symmetrically as the sources of $\phi(0^+)$; §10.2's three levers become three flows plus one cut ($\chi\to0$). The image of trees gains diffusion as the openness of knowledge: what one grows, others can learn.

**(iv) One table, four columns.** For S7, every arrow gets (intervention, held fixed, model, unproved interface). Then the §2 "Why" sentence and the §7.1 table cannot drift apart again.

**(v) The two senses of error.** Boundary error (held model) vs working objective (accurate under compounding); the second is the dilemma, and "judge the game, not the act" is exactly the right verdict on it.

---

## 27. Study 2 as a numbered result

Three independent simulations (Sys `s4/s5/s5b`, Math-Opus `s4(c)`, Math-Fable `m5`; now also `f5`) agree. I propose one Supplement proposition with proved and numerical parts kept apart:

> **Proposition S4.x (The rate law under finite adjustment) [thm; num].** *In the joint model of (10) and Assumption 4.2 with capacity adjusting at a finite rate:*
> *(1) [thm] Sufficiency of $\alpha_{\rm cor}\ge\alpha_{\rm ctl}/(1+\eta)$ holds for every adjustment rule under which capacity never exceeds its selected level.*
> *(2) [thm] Necessity holds iff $\liminf q/q^\ast>0$. Under a constant adjustment rate $k$ the ratio tends to $k/(k+g)$ and failure is delayed by $\eta\ln(1+g/k)/(\alpha_{\rm ctl}-(1+\eta)\alpha_{\rm cor})$; under gradient dynamics with constant variance, $q\le q_0+V\chi\hat Yp^{2-\xi_v}/(d_0\alpha_{\rm cor})$ and the certificate holds eventually for every $\alpha_{\rm cor}>0$; under gradient dynamics with variance proportional to $q^2$ the ratio tends to one below the threshold.*
> *(3) [num] After a reform that raises $d$ and is then withdrawn, the hold needed to undo capture is 6–14% longer than the quasi-static estimate at the parameters computed, more when adjustment is slow relative to $\varepsilon d$.*
> *(4) [num] If correction rests on human capacity that delegation erodes at $\delta_h$, the required rate shifts to about $\alpha_{\rm ctl}/(1+\eta)+\delta_h$, and when capture makes delegation look safe the system shows hysteresis: undoing capture needs 1.6–2.6 times the quasi-static reform (Sys E4; a modelling choice inside S13's open interface $d\le F(\ldots)$).*
> *Reading: quasi-static capacity is conservative while the cost of control falls monotonically and optimistic after reversals and where correction itself rests on a slow eroded variable.*

TESTS Study 2 then changes its predicted failure signature: slow adaptation does not produce failure below the rate law (it delays it); failure below the rate law points to an eroded slow variable in correction. S13 gains the row "Human capacity and correction". Which numbers enter the core: one sentence in 4.5's Scope with the delay formula and the two directions.

---

## 28. Check blocks for `checks_v62.py`

Relabel: EC → *valuation check* (identity: the closed-form values against (14); the only computed object is $V_P$); LG(C)/(C′) → identity (the two-period $\lambda$ is the model's own derivative); RH → identity for the closed-form part, independent only for the grid best response. Core text: "200,000 settings" and "six digits" become "an algebraic check". New independent blocks (names, what, kind):

| Block | Kind | Keys | What it tests (independent of the inequality under test) |
|---|---|---|---|
| **SP** standing price, general | independent | `standprice` | two-period equilibrium by best-response iteration, prize $\Omega_0+g\sum K$ with $\beta$, $n\in\{2,4\}$ within $r\le n/(n-1)$; reads $\theta_{\rm eff}$ off $e^\ast$; tests the sign rule and the knife-edge $(1-\beta)r=1$; infinite-horizon proportional-prize PV ratio by simulation (`f1` A, B) |
| **PD** price domain | independent | `loopgain`, `standprice` | PV of a perturbation for $\Gamma_\delta\ge1$: positivity and the scaling exponent $\alpha-1$ (`f1` C) |
| **MP** Markov-perfect contest | independent | `loopgain`, `standprice` | MPE by value iteration; $\lambda_{\rm MPE}$ vs closed-loop($\tilde\Gamma_\delta$) at small jumps; expected-deviation multiplier vs $1+d(\Gamma_{\rm eq}-1)$; amplification and the laggard's price at the paper's jumps; Monte Carlo spread vs the structural lottery (`f2`) |
| **CE** cap edge and diffusion | independent | `compound` | cap at $K^\ast$ with the local condition; diffusion-only restoration; necessity of a non-rank flow (`f3` A) |
| **DS** d-sign by channel | independent | `loopgain`, S7 table | numerical spectral radius for ratio- and level-form channels as $d$ varies (`f3` B) |
| **TD** time to decisiveness | independent | `tdec` | exact multiplier vs $1+(d+\delta_f)(\Gamma-1)$; two-channel secular root (`f3` C) |
| **CI** extended | independent | `blind`, `nested` | add the three sanction regimes; unequal compliance costs; matched vs unmatched variants; zero tax (`f4` A, C) |
| **PR** extended | independent | `onegroup` | nonlinear increasing fitness with random partitions: total and within $\le0$, between either sign (`f4` B) |
| **JS** joint simulation | independent | `corrrate`, S4.x | QS/R/GA/GM failure dates; delay formula; GA bound; (optional) reversal hold and the $\delta_h$ shift (`f5` A; Sys s5) |
| **FF** falling floor | independent | `corrrate` | Codex's case; the $(f_0,\alpha_{\rm cor})$ grid; lump-sum vs linear floor $d^\ast$ as $\gamma\to0$; threshold exponents (`f5` B, C) |
| **ES** enforcement, stochastic | independent | `enforce`, `relpunish` | explicit-action chain: per-deviation $p_d$; 5.4(5) exclusive vs independent by value iteration; the $P<v<C$ example; R4 exception; exchangeable vs label-dependent continuations (`f6` A–D) |
| **CR** extended | independent | `relpunish` | report strictness margins; $\pm\varepsilon$ perturbations (`f6` E) |
| **SC** scissors | independent | `zonesillus`, `enforce` | direct discounted streams: $\theta_{\rm rep}(p_d)$, the 0.9495 threshold, gap profile at $D=C$ and $D>C$ (`f6` F) |
| **DL** extended | independent | `delegatelock` | $p<1$ interior equilibrium; $p=1$ corners (`f7` A) |
| **HO** extended | independent | `safeguards` | $\Delta_{\min}$ for three floors on the logistic host, two $e_{\min}$ (`f7` D) |
| **SH** extended | independent | `share` | all-$n$ vs $n-1$ sharing by numerical equilibrium (`f7` E) |
| **SR** silent route | independent | `slowroute` | (b),(c) with and without (e): the two clocks (`f7` F) |
| **SM** fixes | independent | `opaquecorr`, `homeostasis` | summable example and the start index; 6.11 best response at every $t$ (`f7` B, C) |
| CS | independent | `influence`, `corrrate` | add $\eta\in\{0.5,2\}$ and $\xi\in\{0,0.3,0.5,0.7,1\}$ (Fable `m4`); add $\hat Y$ scaling (`f5` D) |

All of these run in under 30 s total in pure Python at the grid sizes used here (`f2` is 4 s at $N=400$).

---

## 29. Where the reviewers are wrong or incomplete

1. **Math-Opus M1, repair 2** ("define $r_j$ as the equilibrium elasticity and Proposition 2.2's form is preserved"): true for stability (1), false for the price (3). The price is the closed-loop gain of the *partial*-equilibrium loop (own intensity fixed), and the full-equilibrium discounted gain exceeds one in every case Opus computed, which would give a negative or infinite "price" where the MPE price is finite (§2, Remark S2.2; `f2(1)`).
2. **Math-Opus minor 2** (the $[H_f]$ repair): "$\alpha_{\rm cor}>\alpha_f$" is not sufficient; the transient can fail the certificate before cultivation ends (`f5(B)`, $f_0=0.1$, $\alpha_{\rm cor}=0.051$: fails at 38.4, cultivation ends at 588). The three-case statement with a transient clause is the correct form (§9).
3. **Math-Fable I1 and Math-Opus M1 together**: both are right that the price is amplified at parity, but the two mechanisms differ: the two-period factor $2(n-1)/n$ vanishes at $n=2$ and is a within-period rival response; the MPE amplification at $n=2$ is a dynamic effect (convexity of the value in the state). Neither is "the" factor; the core should quote both as instances.
4. **Codex 1**: right that the printed value is meaningless and that the PV is positive; the stronger statement is that the price per unit diverges as a power $\varepsilon^{\alpha-1}$, so there is no finite-horizon fix that recovers a first-order $\theta$ at parity (a finite horizon $T$ gives a $T$-dependent price that grows without bound in $T$).
5. **Adv-Fable F1**: right about the sign rule and $(1-\beta)r>1$ (the $\beta$ was implicit); the claim that the "environment (1) reinvests $\kappa\times$winnings while 3.9 reinvests net payoff" is an inconsistency is better read as a premise: Proposition 2.2(3) states "reinvests its net payoff", and `f1(D)` shows it is load-bearing (with gross winnings only, $\theta_{\rm eff}$ is lower still: $-0.31$ vs $-0.16$).
6. **Systems I1**: right throughout; the one addition is that $\Gamma_\delta$ rises with $d$ even without diffusion, so the "working objective" column for capacity depreciation is ↑ unconditionally.
7. **Math-Fable I4 / Math-Opus M2 / Systems I3**: consistent; the exact statement is the tracking condition $\liminf q/q^\ast>0$, which covers all three sets of dynamics in one line (§9, §27).
8. **Alignment minor 6** (6.11(3)): right that full delegation is an equilibrium at every $t$; the correct sentence is about realized risk from $t=5$, not about equilibrium existence (`f7(C)`).
9. **Synthesis §四A.3** ("needs inflow not tied to rank: sharing, provision or diffusion"): right, with the caveat that diffusion is a source and not a guarantee (`f3(A)`: $\delta_f=0.05$ alone stalls the laggard at $0.36\bar K$).

---

## 30. Open questions

1. **The two-gain split in the core.** Should Remark S2.2 be summarized in the core's Proposition 2.2 Scope (one sentence) or in Proposition 3.9(3)? I favour 2.2's Scope, since it is a statement about which number means what.
2. **Catch-up contests.** All strategic computations (Fable, Opus, mine) are discouragement contests, where $p'_{\rm eq}>r$. In contests with catch-up (handicaps, learning from the leader, diminishing returns to effort at the top) $p'_{\rm eq}<r$ and the strategic response lowers the price. The statement "structural $\Gamma<1$ is necessary, not sufficient" holds only in the first class; the core should say "in the class computed", and TESTS could add a search for the reverse case.
3. **The general-prize infinite horizon with depreciation.** I proved the proportional-prize ratio at every horizon without depreciation; with depreciation and $\Omega_0>0$ the steady state and the ratio are messier. Is the two-period form enough for the core, with the infinite-horizon proportional case in S3? I think yes.
4. **Prize growth and Proposition 2.3's growth variant.** The growth variant's condition $\kappa_c\Omega((1-\beta)r-1)>\delta_fS+nk_0$ is "date by date"; with $\Omega_t=gS_t$ it is constant. Should 2.3's Scope say "and is constant exactly when the stakes are proportional to capacity, where it coincides with the narrowing condition of Proposition 3.9(2)"? This is the link of §26(ii).
5. **$\lambda_{\rm com}$ in the shared-parameter table.** A new row "prize growth with capacity, $g$" (↓ working objective, 0 loop gain, ↑ stakes in enforcement) would record that positive-sum growth widens working objectives. It cuts across the table's current framing (stakes with provision fixed); worth a row?
6. **Study 2 part (4).** The human-capacity coupling is one reviewer's modelling choice; should it enter S4.x at all, or only S13 and TESTS?
7. **Tag of Proposition 5.15's "blocs".** [conj] or a one-line [obs] from the IR literature (Snidal)? Both are defensible; [conj] keeps the model honest.
8. **Notation policy.** Rename as in §25, or only restrict the uniqueness claim? Renaming costs little in `src/` and removes a reviewer-visible defect; I recommend renaming the in-section clashes ($J$, $v$, $C(q;p)$, $d$ in (15), $U_i$, $q$ in 5.4(5)) and declaring the rest local.
