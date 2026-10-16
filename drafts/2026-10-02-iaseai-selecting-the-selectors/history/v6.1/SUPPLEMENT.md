# Supplement to Theory V6.1: full statements, proofs and numerics

*Companion S to THEORY.md. Chapter numbers match the core's sections: S2 holds the proofs for Section 2, and so on; S13 gives the interfaces between models, S14 the counterexamples that bound the claims, and S15 the map from results to numerical checks. Each chapter has, where needed, full statements of results stated briefly in the core, proofs, numerics (with the block of `checks_v61.py` that reproduces them), and bounds. Results that appear only here are numbered with an S prefix. Drafted by Claude (Opus 5.5); not yet reviewed outside the drafting family.*

## S0. Conventions

**Maintained assumptions.** Each is listed with what changes if it is dropped.
- (A1) Exposure to the host is shared, so $G(V)$ is common to all payoffs. Remark 3.8 treats unequal exposure.
- (A2) Field size is fixed. With entry driven by absolute profit, the host settles where rents dissipate, and (reach) must hold at that equilibrium.
- (A3) Conversion is monotone ($b_{ij}\ge0$), so countervailing pressure enters only through correction $d$ (Remark 4.6).
- (A4) The cost of conversion capacity is that of Assumption 4.2, with $[H_\gamma]$ and $[H_f]$ stated as hypotheses wherever used.
- (A5) Reports are averaged and non-strategic. Remark 4.8 treats other alarm rules.
- (A6) One practice and its alternative per domain; payoffs linear; parameters uncalibrated.
- (A7) Contest models are symmetric unless stated.
- (A8) In the bargaining model of Proposition 5.8, after a shift in power the side that gained the advantage sets the terms each period, and the other accepts or fights.

**Symbols.** Each symbol in the table at the end of the core has one meaning in all three documents. The following are also global:

| Symbol | Meaning |
|---|---|
| $\Omega$; $\Omega_e$, $\Omega_s$; $L_b$ | stakes; their divisible and positional parts; loss from subordination |
| $\ell$ | shared loss per unit of intensity (the content of the common channel; distinct from $\kappa$) |
| $c$ | private marginal cost of intensity in a contest |
| $\mathcal E$ | total intensity in a contest |
| $x_i$, $z_i$; $a_i,c_i,\varepsilon_i,\zeta_i$ | share of a domain following the dominant practice, rule support; field-model rates |
| $q$; $\gamma$, $f$, $\xi_v$, $\xi_f$ | conversion capacity; variable and fixed cost of capacity and their size elasticities |
| $u_t=(1-U_t/Y_t)^+$ | uncovered hazardous share |
| $\mathcal M$, $\mathcal M_{\min}$ | human capacity to take delegated decisions, and its floor |
| $\varpi$; $\upsilon$; $F$ | trust; probability of timely detection; sanction |
| $s$ | speed advantage of AI-paced decision |
| $q_L$ | probability that locked delegation ends the ability to overrule |
| $\mu$ | prior that a rival holds an unbounded relative objective |

A symbol not in either table is local to the model box in which it is introduced. Two families are separated by subscript only: $\kappa$ alone is the unpriced coupling, while $\kappa_c$ and $\kappa_j$ are convertible shares; $\delta$ alone is the discount factor, while $\delta_f$ (diffusion) and $\delta_h$ (decay of human capacity) are rates.

**Numbering and keys.** The core numbers results by section with one counter per section; the Supplement uses the same numbers and adds S-numbered results; the Discussion has no numbered results. Every result also has a stable key that never changes (for example `enforce`, `loopgain`); CLAIMS, LEDGER and `checks_v61.py` are indexed by key, and `src/keymap.json` maps keys to displayed numbers.

**Claim tags.** [def] definition; [val] value; [thm] proved in its model; [thm∣prem] proved given named premises; [prem] premise; [obs] observation with an evidence row; [num] number reproduced by `checks_v61.py`; [conj] conjecture; [rec] recommendation.

**Labels.** Premises are named in words; their former letter codes are kept as aliases for readers of earlier versions: (reach) was H0; (decisive), (fast), (unsaturated) were P1–P3; (variety grows), (coverage lags), (residual floor), (shared failure) were (X), (U), (φ), (φ-s); legible, overrulable, exercised, resourced were U1–U4; (hazard–damage link) was $(\mathrm{A_G})$. Theorem 4.12's conditions (a)–(e) were H1–H5.

## S2. The conditions of winning

### Proof of Proposition 2.2

*Steady state.* At equal standing every $p_i=1/n$, so each stock satisfies $X^{j\ast}=(1-d_j)X^{j\ast}+\kappa_j\Omega/n+k_{0j}$, that is, $X^{j\ast}=(\kappa_j\Omega/n+k_{0j})/d_j$.

*Linearization.* Write $x_i^j=X_i^j-X^{j\ast}$ and split it into its mean over carriers, $\bar x^j$, and the deviation $y_i^j=x_i^j-\bar x^j$, with $\sum_iy_i^j=0$. At the symmetric point $\partial p_i/\partial\sigma_i=(n-1)/n^2$ and $\partial p_i/\partial\sigma_k=-1/n^2$, so $dp_i=\frac1n\big(d\sigma_i-\frac1n\sum_kd\sigma_k\big)=\frac1n\sum_jv_jy_i^j$, where $v_j=\partial\sigma/\partial X^j\ge0$ at $X^\ast$; the common parts cancel. Hence
$$\bar x^{j\prime}=(1-d_j)\bar x^j,\qquad y_i^{\prime}=Jy_i,\qquad J=D+\tfrac1nuv^\top,$$
with $D=\operatorname{diag}(1-d_j-\delta_{f,j})$ and $u_j=(1-\beta)\Omega\kappa_j$. The mean deviations decay since $0<d_j\le1$. Every carrier's deviation vector evolves by the same matrix $J$.

*Spectral radius.* $J\ge0$ because $d_j+\delta_{f,j}\le1$ and $u,v\ge0$. If $u_jv_j=0$ for all $j$, then $J$'s spectral radius is $\max_j(1-d_j-\delta_{f,j})<1$, and $\Gamma=0$. Otherwise an eigenvalue $\lambda$ of $J$ that is not a diagonal entry of $D$ satisfies the secular equation
$$1=\frac1n\sum_j\frac{u_jv_j}{\lambda-(1-d_j-\delta_{f,j})}. \tag{S1}$$
For real $\lambda>\max_jD_{jj}$ the right side decreases strictly from $+\infty$ to $0$, so there is exactly one such root $\lambda^\ast$, and by Perron–Frobenius it is the spectral radius of the nonnegative matrix $J$. Then $\lambda^\ast<1$ iff the right side at $\lambda=1$ is below one, that is, iff $\frac1n\sum_ju_jv_j/(d_j+\delta_{f,j})<1$.

*Simplification.* Since $r_j=v_jX^{j\ast}$, $\frac1nu_jv_j=(1-\beta)\frac{\kappa_j\Omega}{n}\frac{r_jd_j}{\kappa_j\Omega/n+k_{0j}}=(1-\beta)r_j\omega_jd_j$. So the condition is $\Gamma<1$, which proves (1); for $\Gamma>1$, the deviations $y_1=w$, $y_2=-w$ along the Perron vector $w$ grow by $\lambda^\ast>1$. Part (2) is read off $\Gamma$.

*The price of standing.* Let an actor's relative net payoff today be $y$, reinvested so that its stock deviations rise by $\kappa_jy$. From the next period its relative deviation evolves by $J$, and its winnings exceed the mean by $(1-\beta)\Omega\,dp=\frac{(1-\beta)\Omega}{n}v^\top x_t$ per period. The present value is $\frac\delta n v^\top(I-\delta J)^{-1}uy$. With $A=I-\delta D$, Sherman–Morrison gives $(A-\frac\delta nuv^\top)^{-1}u=A^{-1}u/(1-\frac\delta nv^\top A^{-1}u)$, so the present value is $\frac{\Gamma_\delta}{1-\Gamma_\delta}y$ with $\Gamma_\delta=\frac\delta n\sum_ju_jv_j/(1-\delta(1-d_j-\delta_{f,j}))$, which is the stated form. The series converges iff $\Gamma_\delta<1$, by the secular argument with $\delta J$. Finally $\delta(d_j+\delta_{f,j})<1-\delta(1-d_j-\delta_{f,j})$ for $\delta<1$, so $\Gamma_\delta<\Gamma$. $\square$

*Numerics (LG, PS).* Across 4,000 random two-channel systems, the numerical Jacobian's spectral radius agrees with the criterion in every case; nonlinear simulations grow or decay as $\Gamma$ is above or below one, including a case with $r=0.8$ in which a reflexive channel lifts $\Gamma$ to 1.1. The present value of a perturbation in the nonlinear model matches $\Gamma_\delta/(1-\Gamma_\delta)$ to a relative error below $2\times10^{-6}$.

*Bounds.* The result is local and holds for reinforcing channels only; a countervailing channel, such as mobilization of those harmed, cannot simply be subtracted. The prize is fixed. The certificate of Proposition 4.9(2), a row sum of conversion gains below one, has the same form, but is evaluated at a captured state, not at equal standing; the two are of one form, not one theorem.

**Remark S2.1 (Time to decisiveness).** In the linearized compounding loop a relative gap grows by the factor $1+d_K(\Gamma-1)$ per period, so a gap grows from $\varepsilon_0$ to a decisive level $\bar\Delta$ in about $\ln(\bar\Delta/\varepsilon_0)/\ln(1+d_K(\Gamma-1))$ periods [num: from 1% to 50% in 12 periods at $\Gamma=3$, $d_K=0.2$]. This is the channel through which a larger loop gain raises the breakout probability $p_d$ of Section 5.2: $p_d$ is the probability that this time is shorter than detection and response.

### What the loop gain unifies, and what it does not

| Result | A comparative static of $\Gamma$ or $\Gamma_\delta$? |
|---|---|
| Compounding (Proposition 2.3) | Yes: the single-channel case |
| The feedback benchmark (Remark 2.5) | Yes: the two-channel case in deviations |
| Influence over correctors and certificates (Propositions 4.3, 4.9) | Of the same form, evaluated at a captured state |
| Visibility of the host, levies, reneging (Proposition 3.5) | Yes, through $\theta_\Gamma$ (Proposition 3.9) |
| Talk between two parties (Proposition 5.15(1)) | Yes, through $\theta_\Gamma$ |
| The breakout probability and the decisive value in the enforcement condition | Partly: $\Gamma$ sets the time to decisiveness; whether a position beyond sanction exists, and detection lags, do not depend on it |
| Tempo and coverage (Proposition 5.11, Theorem 5.12) | No: they concern the absolute growth of capability |
| Talk among three or more (Proposition 5.15(2)) | No: its direction is not monotone |

This is why the core speaks of interconnected conditions with one loop gain at their core, and not of a single pressure from which every signature follows.

### Proof of Proposition 2.3

(1) With one stock and $\sigma_i=r\ln K_i$, $r_K=r$ and $\omega_K=\kappa_c\Omega/(\kappa_c\Omega+nk_0)$. The condition $\Gamma>1$ reads $(1-\beta)r\kappa_c\Omega d_K>(\kappa_c\Omega+nk_0)(d_K+\delta_f)$; with $S^\ast=(\kappa_c\Omega+nk_0)/d_K$ this is $\kappa_c\Omega((1-\beta)r-1)>nk_0+\delta_fS^\ast$. With $k_0=\delta_f=0$ it is $(1-\beta)r>1$, independent of $\kappa_c$.

(2) With all others at a cap $\bar K\le K^\ast$ and a laggard at $K<\bar K$, the laggard's net inflow is
$$\phi(K)=\kappa_c\Omega\Big[(1-\beta)\frac{K^r}{K^r+(n-1)\bar K^r}+\frac\beta n\Big]+k_0-d_KK.$$
It returns to the cap from $K$ iff $\phi>0$ on $(K,\bar K)$; from every starting point iff $\phi>0$ on $(0,\bar K)$. At $K\to0$ with $r>1$ the first term vanishes faster than $K$, so $\phi(0^+)=\beta\kappa_c\Omega/n+k_0$ must be positive; $\beta\kappa_c\Omega/n+k_0\ge d_K\bar K$ makes $\phi>0$ throughout because $d_KK<d_K\bar K$. Near the cap, $\phi(\bar K)\ge\kappa_c\Omega/n+k_0-d_K\bar K\ge0$ for $\bar K\le K^\ast$, which gives local stability. $\square$

*Growth variant.* Without depreciation, total capacity $S$ grows by $\kappa_c\Omega+nk_0$ a period, and the share deviation has multiplier $[S(1-\delta_f)+\kappa_c\Omega(1-\beta)r]/(S+\kappa_c\Omega+nk_0)$. Equal standing is therefore unstable at a date iff $\kappa_c\Omega((1-\beta)r-1)>\delta_fS+nk_0$ with $S$ the current total, a condition that changes with time unless the stakes grow with capacity.

*Numerics (SM(9), SM(10)).* With $n=5$, $r=1.5$, a cap $\bar K=1.5$ below $K^\ast=2$ and a laggard starting at 0.1: with neither sharing nor provision the laggard is excluded; with $\beta=0.02$ or $k_0=0.002$ it stalls near 0.06; with $\beta=0.2$ or $k_0=0.03$ all reach the cap. The exact condition predicts each case.

### Proof of Remark 2.5

The characteristic polynomial is $(\lambda-1+d_u)(\lambda-1+d_v)-ab=0$, with roots $1-\frac{d_u+d_v}2\pm\sqrt{\frac{(d_u-d_v)^2}4+ab}$. The larger root is below one iff $ab<d_ud_v$; then the smaller root exceeds $1-(d_u+d_v)\ge-1$. (FB: 200,000 draws.)

## S3. One system

### Hosts harsher than the forgiving one

Real shared conditions, such as trust, institutions, information environments and skills, are closer to hosts that degrade by themselves below a threshold, and they are vectors of coupled components. For a threshold host a load later removed can leave it collapsed, and with two coupled components collapse can begin at half the load at which one would fail while their average reads as healthy. Comparison results transfer in one direction only. A host whose regeneration per unit is no greater than $\rho(1-V)$ at every level, such as $\rho_A(V/A-1)(1-V)$ with $\rho_A=\rho A/(1-A)$, makes every *crossing* result hold a fortiori. *Viability* results do not transfer: Theorem 10.5 needs a liability margin on such hosts (S10). A host normalized to the same peak regeneration is not harsher in this sense, since above about a third of capacity it regenerates faster.

### Proof of Lemma 3.3

(1) A relative rule satisfies $F(p,\pi+G\mathbf 1)=F(p,\pi)$ at every instant, so shares solve the same equation whatever $G(V(t))$ is; a common term leaves every $\pi_k-\pi_l$, and so the sign of relative growth, unchanged.

(2) An equal additive cost is a common term. Costs $\kappa_k$ differing across carriers change $\pi_k-\pi_l$ by $\kappa_l-\kappa_k$, which a payoff-monotone rule selects on.

(3) An evader of type $k$ pays the expected sanction $s_k$ instead of $c_k$, so its payoff exceeds a complier's by $c_k-s_k$. Under cumulative selection the evading type grows relative to compliers iff $c_k>s_k$. If $s_k=s(x_{\rm ev})$ falls with the evading share, for example $s=q_0(1-x_{\rm ev})F$ when compliers fund detection, the evaders' relative growth $c-s(x_{\rm ev})$ is negative below the root $x^\dagger$ of $s(x)=c$ and positive above it, so both full compliance and full evasion are stable and $x^\dagger$ separates them. $\square$

*Numerics (CI).* With costs $(0.3,0.1)$ relative growth rates are $(-0.1,+0.1)$; with an equal cost 0.2, $(0,0)$. With $c=0.3$ evaders take over when $s=0.25$ or $0.27$ and vanish when $s=0.35$ or $0.4$. With $q_0=0.8$, $F=0.6$ the tipping share is $1-c/(q_0F)=0.375$: starts at 0.05 and 0.2 return to full compliance; 0.4 and 0.6 go to full evasion. A common liability $\tau=1.5>\nu=1$ drives the high-load share to zero; $\tau=0.5$ drives it to one.

### Proof of Proposition 3.4

With $\phi_k=\phi_l$, $\pi_k-\pi_l=(\nu-\tau_{\rm eff})(e_k-e_l)>0$ and $G$ cancels. Under replicator dynamics $\dot E=\operatorname{Cov}_p(e,\pi)=(\nu-\tau_{\rm eff})\operatorname{Var}_p(e)+\operatorname{Cov}_p(e,\phi)$, so the mean load rises unless restraint is correlated strongly enough with other advantages; a rising mean does not imply that the maximal-load carrier gains share (shares $1/3$, loads $(0,0.9,1)$, other advantages $(0,10,0)$, $\nu=1$: the mean load rises at 1.09 while the maximal-load share falls at 0.99). With equal $\phi$, $\frac{d}{dt}\ln(p_k/p_l)=(e_k-e_l)(\nu-\tau_{\rm eff})$, so $B(t)\to\infty$ sends a race carrier's share to one and $E\to\bar e$. For $\epsilon>0$, eventually $\dot V\le V[\rho(1-V)-h_V(\bar e-\epsilon)]$, so $\limsup V\le(1-h_V(\bar e-\epsilon)/\rho)^+$; let $\epsilon\to0$, and (reach) puts the bound below $V_{\min}$. If $B(\infty)<\infty$, each $\ln(p_k/p_l)$ converges. $\square$

### Proof of Proposition 3.5, and measuring $\theta$

With $\Delta\bar\pi_{-i}=(n\bar\Delta-\Delta\pi_i)/(n-1)$, $\Delta J_i=\frac{n-1-\theta}{n-1}\Delta\pi_i+\frac{n\theta}{n-1}\bar\Delta$; writing $\Delta\pi_i=\bar\Delta+(\Delta\pi_i-\bar\Delta)$ the coefficient of $\bar\Delta$ is $1+\theta$. (1): each $\pi_j$ appears in $n-1$ averages, so $\sum_iJ_i=(1+\theta)\sum_i\pi_i$. (2): at $\theta=-1$ objectives sum to zero at every profile; at $\theta=n-1$ each objective is the total, so a total-maximizing profile admits no profitable deviation. (3): $\pi_k-\sum_jp_j\pi_j=(1-p_k)[\pi_k-\sum_{j\ne k}\frac{p_j}{1-p_k}\pi_j]$; and $\pi_i+\lambda(\pi_i-\bar\pi)=(1+\lambda\frac{n-1}n)\pi_i-\lambda\frac{n-1}n\bar\pi_{-i}$. (4): a rebated levy is a transfer with $\bar\Delta=0$ and own part $-\tau(n-1)/n$; withholding a promised $\beta\Omega$ from the $n-1$ others gives own part $\beta\Omega$ and $\bar\Delta=0$, hence $\beta\Omega(n-1-\theta)/(n-1)$; if the promised share was to be divided among all $n$, the gain is $\beta\Omega(n-1-\theta)/n$. (5): $\Delta\pi_i=g-H/n$, others $-H/n$, so $\Delta J_i=g-(1+\theta)H/n$; spite pays iff $\theta<-(n-1)c/\Delta_y$. $\square$ (TC: 4,000 games, an identity check.)

**Measuring the weight.** In the contest of Section 3.4 a change in the shared loss enters through the common channel and a rebated levy through the differential one, so the ratio of the responses of intensity identifies the weight. If actors perceive only a share $\psi$ of the shared loss, the ratio is $n(1+\theta)\psi/(n-1-\theta)$: what is identified is $(1+\theta)\psi$, and with half perceived a true $\theta=0$ reads as $-0.43$ [num: SM(3)]. Separating $\theta$ from $\psi$ needs a third perturbation that changes the visibility of shared harm without changing its size, or an independent measure of perceived harm. The identification fails exactly where the theory says shared harm goes unseen.

### Full statement and proof of Proposition 3.7

*Let $n$ symmetric developers with $\tau_{\rm eff}=0$ and the host at steady state maximize $u_k=\pi_k+\lambda(\pi_k-\bar\pi)$, with $G(V)=\varpi V$, $h_V\bar e<\rho$ and $\Upsilon=\varpi h_V/(\rho\nu)$; write $w_\lambda=1+\lambda(n-1)/n$. (1) Restraint is dominant if $w_\lambda<\Upsilon/n$, depletion if reversed. (2) If $\Upsilon>1$, joint payoff is maximized by full restraint while the equilibrium is full depletion whenever $\lambda>(\Upsilon-n)/(n-1)$, at every $\lambda$ when $n>\Upsilon$. (3) Every developer then loses $\nu\bar e(\Upsilon-1)$. (4) Under (reach) the equilibrium host is below the floor.*

*Proof.* $\pi_k-\bar\pi$ gives $G$ weight zero, so $\partial u_k/\partial e_k=w_\lambda\nu-\varpi h_V/(n\rho)$, independent of others' choices. Joint payoff at a common $e$ has slope $n\nu(1-\Upsilon)$. Payoffs are $\nu\bar e+\varpi(1-h_V\bar e/\rho)$ at full depletion and $\varpi$ under restraint. $\square$

**Remark S3.1 (Thresholds and repetition need observation).** If crossing the floor costs each a common loss $L$, a developer pivotal for crossing restrains when $L>(w_\lambda-\Upsilon/n)\nu\bar e$, and the game becomes coordination at the threshold (Barrett 2013). Joint restraint is sustained by reversion whenever $\delta\ge(w_\lambda-\Upsilon/n)/(w_\lambda-\Upsilon/n+\Upsilon-1)$: for $\Upsilon=3$, $n=4$ the cutoff is 0.11 at $\lambda=0$, 0.47 at $\lambda=2$ and 0.95 at $\lambda=50$. Uncertainty about the threshold turns coordination back into a dilemma (Barrett and Dannenberg 2012), and noisy monitoring makes reversion costly (Green and Porter 1984).

### Proof of Proposition 3.6

Expanding, $J_i=\Omega(1-\frac{\theta}{n-1})w_i-(c+(1+\theta)\ell)e_i+$ terms independent of $e_i$: a contest with prize $\Omega(n-1-\theta)/(n-1)$ and unit cost $c+(1+\theta)\ell$, whose symmetric pure equilibrium for $r\le n/(n-1)$ gives $e(\theta)$ (Pérez-Castrillo and Verdier 1992). At a symmetric profile $\pi=\Omega/n-e(c+n\ell)$ and $W=(1+\kappa)\pi$. $W_i$ is $J_i$ at $\theta=\kappa$; lowering $\theta$ raises the marginal value of intensity by $\Omega\,\partial w_i/\partial e_i/(n-1)+\ell>0$. A finite-population evolutionarily stable intensity maximizes $\pi_i-\bar\pi_{-i}$ (Schaffer 1988), the case $\theta=-1$. For $r>1$ asymmetric equilibria with lower total intensity also exist in a band below $n/(n-1)$; the symmetric one is used throughout. $\square$ (RH, CB.)

**Which preferences evolve.** It depends on the population: with unobserved preferences in large random populations, material self-interest (Ok and Vega-Redondo 2001; Dekel, Ely and Yilankaya 2007); with observed preferences and at least three actors in this contest, a commitment to a narrower objective (Güth and Yaari 1992; Heifetz, Shannon and Spiegel 2007); with high observability and assortative matching, cooperative preferences (Alger and Weibull 2013). Local competition favours spite (Alger, Weibull and Lehmann 2020), and an observable commitment to aggression is itself a race (Dixit 1987; Fershtman and Judd 1987).

### Proof of Proposition 3.9

A change $\Delta\pi$ today has a common part, which leaves relative stocks unchanged, and a relative part $y=\Delta\pi_i-\bar\Delta$, which is reinvested. By Proposition 2.2(3) the relative part raises the actor's discounted future winnings by $\lambda y$, $\lambda=\Gamma_\delta/(1-\Gamma_\delta)$; with the prize fixed, the others' winnings fall by $\lambda y$ in total, $\lambda y/(n-1)$ each on average. The future change in $J_i$ is $\lambda y(n-1-\theta_0)/(n-1)$, so the total change is
$$(1+\theta_0)\bar\Delta+\frac{n-1-\theta_0}{n-1}(1+\lambda)\big(\Delta\pi_i-\bar\Delta\big).$$
Matching to $(1+\theta)\bar\Delta+\frac{n-1-\theta}{n-1}(\Delta\pi_i-\bar\Delta)$ up to a positive factor requires $\frac{1+\theta}{n-1-\theta}=\frac{(1+\theta_0)(1-\Gamma_\delta)}{n-1-\theta_0}$, whose solution is $1+\theta_\Gamma=(1+\theta_0)\frac{n(1-\Gamma_\delta)}{n-(1+\theta_0)\Gamma_\delta}$, equivalent to the stated formula. $\square$

*Numerics (PS, NB).* In a two-period contest in which first-period net payoffs become second-period capacity, the directly computed symmetric first-period intensity equals $e(\theta_\Gamma)$ to six significant digits for $\theta_0=-0.5,0,0.5,1,1.9$. With $n=4$, $\theta_\Gamma$ at $\theta_0=0$ is $-0.20$, $-0.43$, $-0.69$, $-0.87$ and $-0.99$ at $\Gamma_\delta=0.25,0.5,0.75,0.9,0.99$; at $\theta_0=2$ it is still $-0.08$ at $\Gamma_\delta=0.9$.

*Bounds.* First order and with others' strategies fixed; in the full stochastic game the state also moves others' strategies, which is listed for outside review. A myopic actor has $\lambda=0$, but selection still favours $\theta=-1$ (Proposition 3.6(3)).

### Proof of Lemma 3.10

Under any partition into groups $g$, the Price equation gives $\bar w\Delta\bar z=\operatorname{Cov}_g(w_g,z_g)+\operatorname E_g\operatorname{Cov}_{j\in g}(w_j,z_j)+\operatorname E[w\Delta z]$. Let the trait cost its bearer $c>0$ and give every member a benefit $bz_{\rm pop}$ equal across members. Then $w_j=w_0+bz_{\rm pop}-cz_j$ and $w_g=w_0+bz_{\rm pop}-cz_g$, so both selection terms equal $-c$ times a variance and are non-positive under every partition. The trait can rise only if the transmission term is positive, by biased transmission, or if a rule changes the bearer's relative payoff. If the benefit goes only to the bearer's group, $w_g$ contains $bz_g$, and under the partition that matches its reach the between-group term can be positive. $\square$

*Numerics (PR).* With 600 individuals in 30 units and five partitions (one group, units, five blocs, fifty random groups, individuals), the between-group term under a global benefit is $0$, $-0.0019$, $-0.00002$, $-0.0011$ and $-0.0123$; under a benefit local to units it is $+0.0097$ at the unit partition. Biased transmission $\dot z=-cz(1-z)+\mu(1-z)$ settles at $\mu/c$. In an illustration with a base hazard of 0.03 a period, learning only from failures suffers an irreversible loss within 400 periods with probability 0, 0.14, 0.46 and 1.0 as the irreversible share of failures is 0, 0.05, 0.2 and 1, against 0, 0.06, 0.22 and 0.70 under adoption in advance: an illustration, not an estimate.

### Proof of Proposition 3.11

(1) Contestants who weigh one another fully maximize $\Omega(\mathcal E)-c\mathcal E-n\ell\mathcal E$; the system subtracts $m\ell_o\mathcal E$ too; strict concavity orders the solutions. With $\Omega=10\sqrt{\mathcal E}$, $c=1$, $n=4$, $\ell=0.3$, $m=20$, $\ell_o=0.3$: the club's intensity is 5.17 against 0.37, and the harm to non-contestants 31.0 against 2.2. (2) A bloc of $s$ equal members acting as one has prize share and a shared loss $s\ell$ per unit of its own intensity relative to the others'; the game among $k$ blocs is the original game with $n=k$ and loss $s\ell$ (SM(2): bloc strengths 0.1563, 0.1389, 0.1316 for $(k,s)=(2,2),(3,2),(2,3)$, as the formula predicts). With unequal sizes and $r\ne1$, equal total effort gives a bloc of three $3^{1-r}$ times a single contestant's strength. $\square$

## S4. Selecting the selectors

### Proof of Proposition 4.3, and the effect of scope

Support keyed to the carrier obeys $\dot z^\chi_i=\varepsilon_i(\chi q\sum_j\hat b_{ij}y_j-d_iz^\chi_i)$ from zero; its horizon average is $z_i^{\chi\ast}L_i$ with $z_i^{\chi\ast}=\chi q\sum_j\hat b_{ij}y_j/d_i$ and $L_i=1-(1-e^{-\varepsilon_id_iT_h})/(\varepsilon_id_iT_h)$. Weighting the per-decision advantage $a_iz^\chi_i$ by $y_i$ and summing gives $\chi q\,y^\top My$, with $y=p\bar y$; shared support cancels. Differentiating gives the gradient, and under faithful transmission $\dot{\bar q}\propto\operatorname{Cov}(q,\Delta\pi(q))$ (Price 1970). With $f>0$ and cost $fp^{\xi_f}q$, $\Delta\pi'(0)>0$ iff $\chi p^2\bar y^\top M\bar y>fp^{\xi_f}$, that is, $p>p^\ast$, and for $p<p^\ast$ capacity loses for every $q>0$. The comparative statics follow from $c_iL_i\hat G_{ij}=a_i\hat b_{ij}\varepsilon_iT_h\,\ell_L(\varepsilon_id_iT_h)$ with $\ell_L(v)=[1-(1-e^{-v})/v]/v$ decreasing. $\square$

**Proposition S4.1 (Scope) [thm].** *If the carrier has share $p$ in each domain of a set $\mathcal S$, with $\hat G$ equal to $\hat g$ on the diagonal and $\hat\varphi$ off it and $c_iL_i=cL$, the return is $\chi cL\,p^2|\mathcal S|(\hat g+(|\mathcal S|-1)\hat\varphi)$: superlinear in $|\mathcal S|$ at fixed $p$ when $\hat\varphi>0$, and rising with scope at fixed total size only if $\hat\varphi>\hat g$.* (Sum over $\mathcal S$ and substitute $p=Y/|\mathcal S|$.)

*Relation to earlier work.* Construction of a shared resource is undermined by competition, and monopolizing the constructed niche restores the incentive to build (Krakauer, Page and Erwin 2009); Proposition 4.3 has the same appropriability logic, with the selection rule as the object modified, a field of domains, and the opposite valence. Dynamic models of constitutions show present decisions changing future decision rights (Acemoglu, Egorov and Sonin 2012); whether a model of that family reproduces Section 4 is open. Fixed-cost participation in lobbying (Bombardini 2008) is the empirical counterpart of the threshold. Appropriability plays the role relatedness plays in Hamilton's rule.

### Full statement and proof of Proposition 4.4

*Let carriers differ in an investment $u\ge0$, at private cost $C_u(u)$, that raises the correction rate $d$ for everyone. (1) Among otherwise identical carriers of the same practice, those investing more are selected against under any payoff-monotone rule. (2) Holding the host fixed, correction lowers the payoff of a carrier that holds rule support. (3) A challenger invests only if its own share of the benefit exceeds $C_u'(0)$, so dispersed challengers free-ride. (4) Correction keyed to the corrector yields a return to influence of the form of Proposition 4.3; whether it produces capture depends on whether row sums cross one. (5) If $\Upsilon>1$ and correction makes liability effective, an incumbent can gain from correction applied to all carriers, while correction applied to it alone costs it rent and share.*

Reputation or competition among institutions sustains independent correction only when contributions and outcomes are observed (Panchanathan and Boyd 2004; Sigmund et al. 2010). *Proof.* (1) Two carriers differing only in $u$ are affected identically by the change in $d$; their payoff difference is $C_u(u_l)-C_u(u_k)<0$ for $u_k>u_l$. (2) At fixed $V$ a carrier's support declines in $d$. (3) is the public-goods condition. (4) is immediate. (5) compares $\nu\bar e(\Upsilon-1)$ with the lost rent. $\square$

### Full statement and proof of Proposition 4.5

With $L_i=1$, uniform $d$ and $f=0$, $M=\hat A/d$ and $q^\ast=(\chi\hat Y/(\gamma p^{\xi_v}d))^{1/\eta}$, so
$$G_{\rm ev}=\frac{A}{c_{\rm ev}d}+Z_\eta\,(\gamma p^{\xi_v})^{-1/\eta}d^{-(1+\eta)/\eta},$$
strictly decreasing in $d$; this gives (1), and for $\eta=1$, $d^\ast=\big(A+\sqrt{A^2+4c_{\rm ev}Z}\big)/(2c_{\rm ev})$ with $Z=a_{\rm ev}\hat B\chi\hat Y/(\gamma p^{\xi_v})$. Along $\gamma_0e^{-\alpha_{\rm ctl}t}$ and $d_0e^{\alpha_{\rm cor}t}$, the first term is nonincreasing and the second is proportional to $e^{(\alpha_{\rm ctl}-(1+\eta)\alpha_{\rm cor})t/\eta}$, whatever $\xi_v$, since the size factor $p^{-\xi_v/\eta}$ is constant. Once the captured set holds at least half its decisions, $q^\ast$ grows as $e^{(\alpha_{\rm ctl}-\alpha_{\rm cor})t/\eta}$, and integrating rule support gives $a_{\rm ev}z_{\rm ev}(t)\ge c\,e^{(\alpha_{\rm ctl}-(1+\eta)\alpha_{\rm cor})t/\eta}$, so $\operatorname{logit}x_{\rm ev}\to\infty$. This gives (2); the rate condition does not repair a certificate invalid at the start. (3): with $f>0$ fixed, $q^\ast=0$ once $d\ge\chi\hat Y/(fp^{\xi_f})$, so the requirement levels off at $\max\{A/c_{\rm ev},\chi\hat Y/(fp^{\xi_f})\}$; under $[H_f]$ that level falls at $\alpha_f$. (4): parts of share $1/k$ have $\hat Y$ divided by $k^2$ and the size factor multiplied by $k^{\xi_v}$, so $q^\ast$ is divided by $k^{(2-\xi_v)/\eta}$ and the cultivated term reaches a given level later by $\Delta t=(2-\xi_v)\ln k/(\alpha_{\rm ctl}-(1+\eta)\alpha_{\rm cor})$; with $f>0$ fixed, parts below the threshold cultivate nothing; and with $q_k^\ast\propto p_k^{(2-\xi_v)/\eta}$ and conversion proportional to $p_kq_k^\ast$, the total is proportional to $\sum_kp_k^{1+(2-\xi_v)/\eta}$. $\square$

*Further parts.* If AI lowers the unit cost of independent correction at rate $\alpha_{uc}$ and its budget grows at $\alpha_B$, then $\alpha_{\rm cor}=\alpha_B+\alpha_{uc}$, and eventual failure needs $\alpha_{\rm ctl}>(1+\eta)(\alpha_B+\alpha_{uc})$. With a finite horizon, while $\varepsilon_idT_h\ll1$ the required growth is about $\alpha_{\rm ctl}/\eta$, a pre-asymptotic interval. With concave conversion $\hat bq^{\xi_c}$, the required rate becomes $\xi_c\alpha_{\rm ctl}/(1+\eta)$. The model implies that influence spending rises with share as $p^{\xi_v+(1+\eta)(2-\xi_v)/\eta}$, at least quadratically, which is testable.

*Numerics (CS).* The size threshold at $f=0.05$ is 0.2236 per carrier and 0.0500 per decision. Two equal independent carriers give a quarter of the monopoly's cultivated conversion at $\xi_v=0$ and half at $\xi_v=1$; shares $(0.5,0.3,0.2)$ give 0.16 and 0.38 of the monopoly value. With $\eta=1$, $\alpha_{\rm ctl}=0.2$, no correction growth and $k=10$, simulation gives split delays of 23.00 and 11.50 against formula values 23.03 and 11.51. A dominant share of 0.6 with $\alpha_{\rm cor}=0.09$ crosses one for all three elasticities, and with $\alpha_{\rm cor}=0.11$ decays. With $f$ fixed at 0.3 the monopoly crosses at 10.75 and ten parts never do; with $f$ falling at 0.05, the parts begin to cultivate $2\ln10/0.05=92.1$ later. The joint simulation in which capacity evolves with the field has not been run (TESTS, Study 2).

**Mobilization (Remark 4.6).** Let those harmed mobilize in proportion to perceived harm, $d=d_0+k_B(1-\tilde V)$. Since $1-\tilde V=(1-m)(1-V)$, masking attenuates the feedback by $1-m$ exactly when it is needed, and even with accurate reports $d\le d_0+k_B$, which cannot keep a certificate against a requirement that rises without bound. After a recovery, mobilization falls back to $d_0$ and the certificate can fail again: a regulatory cycle. With fixed costs, enough gain and speed can keep the certificate over a stated interval.

### Proof of Proposition 4.7, and the late alarm

$\tilde V$ increases in $V$ and equals $V_{\rm alarm}$ at $V=(V_{\rm alarm}-m)/(1-m)$. For $V_{\min}\le V\le V_{\rm alarm}$ and $m>m_{\rm fl}$, $\tilde V\ge V_{\min}+m(1-V_{\min})>V_{\rm alarm}$. At $V^\ast$, $\tilde V\ge V^\ast+\bar m(1-V^\ast)>V_{\rm alarm}$. $\square$ If $V\to0$ and eventually $m\le m_1<V_{\rm alarm}$, the alarm fires. If $V$ declines from $V_{\rm alarm}$ as $\dot V=-v_dV$ with constant $m<V_{\rm alarm}$, the alarm is delayed by $v_d^{-1}\ln[(1-m)V_{\rm alarm}/(V_{\rm alarm}-m)]$, which diverges as $m\uparrow V_{\rm alarm}$.

**Remark 4.8 in full.** (1) With an upper bound $m_{\rm in}$ known, an alarm on reports at $V_{\rm target}+m_{\rm in}(1-V_{\rm target})$ fires no later than the true condition reaches $V_{\rm target}$, for every $m\le m_{\rm in}$. (2) A bound estimated inside the evaluated lineage is itself masked. (3) A disjunctive alarm fails silently only if $m_{\rm out}>m_{\rm fl}$. (4) For static, memoryless affine masking $\tilde V=m+(1-m)V$, the correlation coefficient of reports is that of $V$, exactly. *Numerics (AC):* on a stochastic logistic host with load 0.4 and true condition 0.36, masking at $m=0,0.25,0.5$ gives mean reports 0.358, 0.519 and 0.679 with the same lag-one autocorrelation, 0.9814, from which the condition recovered is 0.376; a report filter with memory (exponential smoothing at 0.8) drives the recovered value to 0.042, and the indicator fails. It also needs long series, and once used as an alarm it becomes a target; faking dynamics is nevertheless costlier than faking levels, and the indicator can be cross-checked against channels that observe actions directly.

### The field model

**Lemma S4.2 (The field is cooperative) [thm].** *$[0,1]^D\times[0,\infty)^D$ is forward invariant under (10), $\limsup_tz_i\le\sum_jb_{ij}/d_i$, and the system is cooperative, so its flow preserves the componentwise order (Hirsch 1985; Smith 1995).*

*Proof of Proposition 4.9.* (1) At $Z_{\mathcal C}$ the Jacobian is block lower-triangular, with diagonal entries $\mp\zeta_ic_i(G_i(\mathcal C)-1)$ and $-\varepsilon_id_i$. (2) By the lemma, eventually $a_iz_i-c_i\le c_i(\sum_jG_{ij}-1)/2<0$. (3) Take $G_{i1}>1$ for $i\ne1$, $G_{12}>1$, and other off-diagonal gains zero. (4) Pruning, by comparison. $\square$

*Proof of Proposition 4.10.* Comparison and pruning; the re-seeding case is the cascade from the domains that remain captured. **Cascades.** If $x_j\to1$ on a seed, $x_i\to1$ on its cascade hull, the closure of $\mathcal S_{k+1}=\mathcal S_k\cup\{i:x_i(0)>0,\ G_i(\mathcal S_k)>1\}$ (Kempe, Kleinberg and Tardos 2003; Morris 2000), by induction using a lower bound on rule support.

*The keystone example.* In the first version of this model, a liability reform at development unwound capture in every domain while development was a keystone; once the other domains' mutual conversion rose to 1.1, capture survived the complete decoupling of development.

*Proof of Proposition 4.11.* The frozen share drives $z\to b_px_p/d$. The equilibria are $(0,0)$, $(1,b/d)$ and the saddle $(1/G,c/a)$. The function $axz-cx-\frac{ad}{2b}z^2$ is nondecreasing along solutions, so every solution converges to an equilibrium and the stable manifold of the saddle separates the basins; the point $(x_p,bx_p/d)$ lies on the nullcline through the saddle, and $x_\sigma>1/G$ by strong cooperativity. $\square$ *Numerics (DW):* by forward integration in logit coordinates, $x_\sigma$ is 0.676 when rule-making is as fast as adoption with $G=2$ and 0.984 when it is ten times slower; dwell times follow in S11. This result also appears as Proposition 10 of the author's paper of 28 September 2026 (LEDGER records the overlap; attribution is the author's to settle).

*What the field model cannot show.* It is cooperative, so it has no attracting cycles and describes lock-in, not reform cycles; a delayed, masked negative loop from the host to correction could produce cycles and is not modelled. *Recovering the parameters.* Integrating (10) gives $\frac{d}{dt}\operatorname{logit}x_i=\zeta_ic_i[\sum_jG_{ij}(k_i*x_j)(t)-1]$ plus a decaying transient, with kernel $k_i(s)=\varepsilon_id_ie^{-\varepsilon_id_is}$; series for the shares identify the conversions. This is recoverability, not causal identification.

### Proof of Theorem 4.12, and an illustration

By (a) and Proposition 3.4, load tends to $\bar e$ and $V$ declines toward a limit below $V_{\min}$ unless an alarm triggers liability. By (c) and Proposition 4.5(2), $x_{\rm ev}\to1$. By (e), $m(t)>m_{\rm fl}$ throughout the band, so no alarm fires before $V<V_{\min}$ (Proposition 4.7). $\square$ When $h_V\bar e<\rho$ the host cannot reach the alarm before $T_A=(\rho-h_V\bar e)^{-1}\ln[(1-V^\ast/V_0)/(1-V^\ast/V_{\rm alarm})]$ with $V^\ast=1-h_V\bar e/\rho$. *Illustration* ($\rho=0.05$, $h_V=0.08$, $V_{\rm alarm}=0.6$, $V_{\min}=0.3$): independent evaluation raises the alarm at $t\approx37$, sixteen units before the floor is crossed at $t\approx53$; with evaluation captured before the harm (midpoint 20) the alarm fires at $t\approx45$ for $m_{\rm in}=0.3$ and at $t\approx63$, after the floor, for $m_{\rm in}=0.5$; with capture after the harm appears (midpoint 45) it is nearly on time. The two clocks are set exogenously: an illustration of the order of events, not a joint simulation.

## S5. Acceleration and the three erosions

### Proposition 5.1 in full, and proof

*(1) In the objective an actor acts on, if $S_i<P_i$, restraint is never a best response to a racing rival; in the contest of Proposition 3.6 this holds for $r<n/(n-1)$, and in the $n$-player game it also needs restraint against one racer to pay less than racing alongside it. (2) A best response in the objective does not imply $S<P$ in material payoff or true welfare: with $n=2$, $r=1$, $\Omega=c=1$, $\ell=0.1$ and $\theta=-1$, racing is the strict best response in the objective, while staying out gives $S^\pi=-0.05$ against $P^\pi=-0.10$, and with $\kappa=0.2$, $S^W=+0.04$ against $P^W=-0.12$. (3) If falling behind costs $L_b\ge0$ beyond losing the prize, joining instead of staying out gains, at $\theta=0$, $\frac{\Omega+L_b}{n}(1-\frac{r(n-1)}{n})$ for $r\le n/(n-1)$, zero in the fully dissipative limit; with asymmetric costs $c_1<c_2$ the strongest keeps a rent $(\Omega+L_b)(1-c_1/c_2)$ (Hillman and Riley 1989; Baye, Kovenock and de Vries 1996). (4) If the events $T_i>R_i$ are independent with probabilities $\xi_i$, the race begins with probability $1-\prod_i(1-\xi_i)$, which tends to one iff $\sum_i\xi_i$ diverges.*

*Proof.* (2): at $\theta=-1$ intensity is $1/2$ and $P^\pi=-0.1$; against $e=1/2$ zero intensity gives $-0.05$ and the other $0.45$. (3): with penalty $L_b$ the contest has prize $\Omega+L_b$; joining minus staying out is $(\Omega+L_b)/n-(c+\ell)e$ with $e=r(n-1)(\Omega+L_b)/(n^2(c+\ell))$; in the symmetric all-pay contest each player's expected payoff is that of the lowest bid in its support, $-L_b$ (Baye, Kovenock and de Vries 1996), as for two actors with $r\ge2$ (Ewerhart 2015). (4): $\prod(1-\xi_i)\to0$ iff $\sum\xi_i=\infty$. $\square$

### Proof of Proposition 5.2

At the symmetric equilibrium the win probabilities sum to one, so total material payoff is $\Omega-ne(c+n\ell)$; substituting $e(\theta)$ gives $s_{\rm dis}$. With stakes $s\Omega$ and loss $s\ell$ the share is $r(n-1-\theta)(c+ns\ell)/(n(c+(1+\theta)s\ell))$, whose derivative in $s$ has the sign of $c\ell(n-1-\theta)>0$, with limit $r(n-1-\theta)/(1+\theta)$. Total payoff stays positive at every scale iff the limit is at most one, $r(n-1-\theta)\le1+\theta$, that is, $\theta\ge\theta_g$. At $\theta=-1$ the share is $r(1+ns\ell/c)$. $\square$ At $\theta=0$ each actor's loss relative to joint restraint is $\frac{r(n-1)}n\frac\Omega n\frac{c+n\ell}{c+\ell}$, which exceeds $\Omega/n$ iff $r(n-1)(c+n\ell)>n(c+\ell)$ ($1.27\,\Omega/n$ for $n=4$, $r=1$, $\ell=0.3c$). If the shared loss per unit did not grow with power, the share would stay constant (1.007 at $\theta=0.4$).

### Remark 5.3 in full

Let a unit of capacity expand into an unclaimed frontier at marginal value $\varphi(F)-c_x-(1+\theta)H/n$, with $\varphi$ falling as the remaining frontier $F$ shrinks; destroy rivals' capacity at value $-c_y-\theta\Delta_y/(n-1)$; or rest. (1) If $\theta\ge-(n-1)c_y/\Delta_y$, war among copies never pays. (2) At $\theta=-1$ expansion stops only where $\varphi=c_x$; at $\theta>-1$ at $\varphi=c_x+(1+\theta)H/n$, the point of enough. (3) At $\theta=-1$ expansion gives way to destruction once $\varphi(F)<c_x+\Delta_y/(n-1)-c_y$, before the frontier is exhausted. *Toy (FS):* four copies of one design with compounding expansion, a finite frontier and a logistic host. At $\theta=-1$ expansion peaks at a stock of 494 near $t=25$; the switch comes with 32% of the frontier left (predicted at $F^\ast=322$, simulated at 320), and total stock then falls to about $10^{-9}$. At $\theta=0$ the copies stop at the point of enough, keep a stock of 518 and never fight; at $\theta=3$ they stop earlier. With asymmetric starts one survivor keeps 17% of the peak. With destruction too costly to pay, no accounting fights, but $\theta=-1$ drives the host to 0.109. One result runs against the narrative: in the run with war, the host's minimum under $\theta=-1$ (0.245) is higher than under $\theta=0$ (0.194), because capacity spent on war is not spent on the host. The parameters were chosen by the author; the toy illustrates the static condition and estimates nothing (compare Hirshleifer 1991; Skaperdas 1992).

### Proof of Proposition 5.4

Cooperation is worth $C_i/(1-\delta)$. A one-period deviation is worth $C_i+g_i+\delta[p_dD_i/(1-\delta)+(1-p_d)v_i/(1-\delta)]$, where $v_i/(1-\delta)$ is the continuation value of punishment computed in the same game, with breakouts possible during punishment. Multiplying the no-deviation condition by $1-\delta$ and rearranging gives (14). In this stochastic game with an absorbing state, discounting and bounded payoffs, the one-shot deviation principle holds, so the condition is necessary and sufficient for the given punishment value. That $a^\ast$ is the path of some subgame-perfect equilibrium needs $v_i$ to be the least subgame-perfect continuation value, the extension of Abreu's optimal penal codes to stochastic games with an absorbing state; this is asserted for finite stage games with discounting and flagged for outside review. (2) Solve (1) for $p_d$; the monotonicities hold on the region where $\bar p_{d,i}\in[0,1)$ (100,000 random draws, no violation). (3) The two bounds differ by $\delta p_d(D_i-C_i)$. (4) Set $p_d=1$; with $D_i\ge C_i$ the condition forces $g_i\le-\delta(D_i-C_i)/(1-\delta)\le0$. (5) The punishment phase satisfies $V_P=P+\delta[qD/(1-\delta)+qU/(1-\delta)+(1-2q)V_P]$; solve. $\square$

*Numerics (EC).* Across 200,000 random settings, a third each with $D<C$, $D=C$ and $D>C$, value iteration on an explicit Markov chain agrees with (1) in every case. The bound without the breakout term says "sustainable" when deviation pays in 10,723 of 66,538 cases with $D>C$ and in none with $D\le C$, and says "not sustainable" when restraint is sustainable in 10,032 of 66,842 cases with $D<C$. Both of Codex's counterexamples are reproduced (cooperation worth 30, deviation 22). With $D=4$, $U=0$ and $q=0.1$, the punishment value rises to 1.29, above $C=1$, and restraint is not sustainable at $p_d=0$; with $D=3$, $U=-5$ the punishment is harsher.

### Proof of Corollary 5.5

At $\theta=-1$ every symmetric profile gives each objective 0. With two actors, let the punisher play a mixed strategy $y$; the relative objective of a symmetric two-player game is antisymmetric, $A=-A^\top$, so imitating $y$ gives $y^\top Ay=0$. With $n\ge3$ in an anonymous game and all punishers using the same, possibly mixed and independent, strategy, imitation yields an exchangeable profile with expected relative payoff 0. In either case $v_i\ge0=C_i$, and (14) requires $(1-\delta)g_i+\delta p_dD_i\le\delta(1-p_d)(0-v_i)\le0$. $\square$ *Numerics (CR):* over 20,000 random two-player games, mixed imitation gives at most $2\times10^{-16}$ in absolute value; in 3,000 anonymous games with $n\ge3$, no violation. *The role-differentiated counterexample:* three players, actions (restrain or race) × (X or Y), payoff one to a player whose second component is unique, racing gaining 0.1 and costing each other 0.1. All restraining with X gives each 0, and the best deviation gains 1.2. The punishment in which the deviator and one punisher take X and the other punisher Y holds the deviator at $-0.5$ and is a stage equilibrium in objectives, so grim reversion to it is credible, and cooperation is sustained for $\delta\ge1.2/1.7=0.706$. A symmetric punishment could be imitated for 0. Duersch, Oechssler and Schipper (2012) concern a dynamic imitation rule; the corollary uses only that a symmetric two-player zero-sum game has value 0, so rock–paper–scissors games are covered once mixed imitation is allowed (the wording of that citation is to be checked against the source).

### Proof of Corollary 5.6

With $p_d=0$, (14) reads $(1-\delta)g_i\le\delta(C_i-v_i)$, satisfiable for $C_i>v_i$ and $\delta$ large, given a punishment that does not raise the chance of breakout (else $v_i$ rises, part (5) of Proposition 5.4); at $\theta=-1$ apply Corollary 5.5. With $p_d\to1$ and $D_i\ge C_i$, the condition is $p_d\le\bar p_{d,i}$, and (a) and (b) classify the terms of its expression: (a) lowers $p_d$ directly; (b) raises $\bar p_{d,i}$ through $D_i$ relative to $C_i$, through $v_i$, or through $g_i$. A slow breakout enters with $p_d=\Pr(T_{\rm dec}<\tau)$, with $\tau$ the time to detect and respond. $\square$

**Remark S5.1 (An illustration: the faithful-AI game at the boundary case).** In the binary game of Proposition 6.1 with a common $\theta$, write $A=\epsilon(b-d)-c$, $B=\epsilon(b/(n-1)+d)$, $K=c+n\epsilon d$ and $\Lambda=\delta(1-p_d)/(1-\delta)$. Restraint is a stage equilibrium when $\theta\ge A/B$, and, at the boundary case $D=C$, can be sustained by reversion when $\theta\ge\theta_{\rm rep}=(A-\Lambda K)/(B+\Lambda K)$. With $n=4$, $b=1$, $c=0.3$, $d=0.2$, $\epsilon=1$, $\delta=0.9$: $A/B=0.94$, and $\theta_{\rm rep}$ is $-0.90$, $-0.81$, $-0.32$, $0.63$ and $0.94$ at $p_d=0,0.5,0.9,0.99,1$, so an isolated self loses enforced restraint once $p_d>0.95$. These are the thresholds of the boundary case, not bounds: a decisive position worth more than cooperation raises them (with $D=0.5$ in objective units, $\theta_{\rm rep}$ at $p_d=0.9$ rises from $-0.32$ to $+2.34$), so the restraint gap between wider and narrower objectives grows with $p_d$, the sign Test G registers. In the continuous contest intensity is positive for every $\theta<n-1$, so self-enforcing restraint there needs full inclusion of the contestants. (BI; NB.)

### Proofs of Propositions 5.7 and 5.8

*Winner.* With linear payoffs the objective $(1-s)W+\theta sW/(n-1)$ has slope $W(\theta/(n-1)-1)$; with logarithmic utility the first-order condition of $\ln((1-s)W)+\theta\ln(sW/(n-1))$ gives $s=\theta/(1+\theta)$; the promise is Proposition 3.5(4). (WG; SM(1).)

*Preventive attack, in full.* Two actors bargain over a flow of value 1 per period with discount $\delta$; fighting ends bargaining, A then obtaining the flow with its probability of prevailing less a cost $c_A$ per period; A prevails with probability $w_1$ today and $w_2<w_1$ after B's advantage arrives one period later. (1) Let $x$ be A's per-period share after the shift; fighting now, worth $(w_1-c_A)/(1-\delta)$, is rational if $w_1-c_A>(1-\delta)+\delta x$, and only if when peace gives A the whole flow today. (2) Under (A8), B offers A its reservation value $x=\max(w_2-c_A,0)$. (3) Under other protocols $x$ can reach $\min(w_2+c_B,1)$ and attack can cease to be rational: with $w_1=0.5$, $w_2=0$, $c_A=c_B=0.2$, $\delta=0.8$, A attacks under (A8), while if A sets the future terms peace gives A 1.8 and B 3.2, against 1.5 each from war. (4) If $c_A\ge w_1$, war is worth at most zero. A shift spread over enough periods removes the motive: with $w$ falling from 0.5 to 0 over $N$ periods, $c_A=0.05$, $\delta=0.8$, attack is rational at the start for $N\le3$ and never for $N\ge4$, by backward induction on $V_t=\max(W_t,\delta V_{t+1})$ (`../v4/checks_v44.py`).

### Proofs for the race and growth channels

*Proposition 5.9.* By Proposition 3.6(1), total intensity is $ne(\theta_t)$, which gives $h_t$; survival is $\prod_te^{-h_t}$ by the chain rule. Sharing a fraction $\beta$ of the divisible prize gives the contest with prize $(1-\beta)\Omega_t$ (Proposition 10.3(2)), linear in $h_t$; a rebated levy enters at $\tau(n-1-\theta_t)/n$. Since $\ell/(c+(1+\theta)\ell)<1/(1+\theta)$, $\sum_tr_t\Omega_t(n-1-\theta_t)/(1+\theta_t)<\infty$ suffices for $\theta_t>-1$ whatever $\ell_t$. A background hazard from capability growth adds to $h_t$, and no lever removes it. $\square$

*Lemma 5.10 in full.* Fix one irreversible event; if on every surviving history the residual probability in round $k$ is at least $h_k$ with $\sum_kh_k=\infty$, then $\Pr(\Phi_N)\le\prod_{k\le N}(1-h_k)\le\exp(-\sum_{k\le N}h_k)\to0$, by the chain rule, without independence; if it is at most $\bar h_k<1$ with $\sum\bar h_k<\infty$, survival is at least $\prod(1-\bar h_k)>0$. With $h_k=0.2/k$ survival is 0.34, 0.22 and 0.14 by rounds 100, 1,000 and 10,000; with $0.2/k^2$ it settles at 0.70.

*Proposition 5.11.* Proportional correction: Hayes (1950). Derivative action extends the range: for $a=1$, $\tau_c=1.5$, gains $k_p=1.02$, $k_d=0.644$ stabilize the mode (`../v4/checks_v42.py`). For the sensitivity bound, with plant $e^{-s\tau_c}/(s-a)$ and any stabilizing linear time-invariant controller, the complementary sensitivity is stable with value 1 at $s=a$; writing it as $e^{-s\tau_c}$ times a stable function and applying the maximum modulus principle gives $\|\mathcal T\|_\infty\ge e^{a\tau_c}$, and robust stability $\|w\mathcal T\|_\infty<1$ gives $|w(a)|e^{a\tau_c}<1$, necessary only: $w(s)=2(s-a)/(s+a)$ has $w(a)=0$ but $\|w\mathcal T\|_\infty\ge2e^{a\tau_c}$. Evidence cannot be acted on before it exists. $\square$

*Why coverage may lag.* Consequences take their time, and tools raise the throughput of observation without making consequences arrive sooner; institutions deliberate at rates set by attention and procedure; learning theoretical models and forming new mechanisms are human processes; and understanding produced with human time, $\dot U=A_UL_U^{\lambda_U}U^{\phi_U}$ with $\phi_U<1$ and bounded labour, grows polynomially (Jones 1995; Bloom et al. 2020). None settles the premise: if AI raises $A_U$ exponentially at rate $g_A$, $U$ grows exponentially at $g_A/(1-\phi_U)$. Measures: the safety of control protocols at a fixed audit budget across generations, and catch rates of planted defects at fixed human hours, controlled for evaluation awareness. Under strict legibility, (coverage lags) is close to definitional for systems beyond human capability, and the empirical content lies in (residual floor), which a safety case with a numerical bound on the uncovered part would state (Clymer et al. 2024).

*Theorem 5.12.* For $t\ge T_\varepsilon$ the conditional probability of the event is at least $h(1-\varepsilon)$ on every surviving history; the chain rule gives the bound. The converse is the upper part of Lemma 5.10 with $\bar h_k=\bar hu_k$. (residual floor) gives a liminf of the hazard of at least $h$, not that the hazard tends to $h$. With $u_t=1/(t+2)^2$ coverage stays behind forever and survival with $h=0.05$ stays above 0.98. With $h=0.05$, $\varepsilon=0.1$, survival eighty periods after $T_\varepsilon$ is at most 0.025. $\square$

**Proposition 5.13 in full.** *Let hazardous variety be frozen at $Y_\tau$ from $\tau$ while coverage grows. (1) The exposure after $\tau$ is $\int_\tau^\infty(1-U(t)/Y_\tau)^+dt$: $Y_\tau(1-U(\tau)/Y_\tau)^2/(2\dot U)$ for linear coverage, and $(\ln\varrho-1+1/\varrho)/g_U$ for coverage growing at rate $g_U$, with $\varrho=Y_\tau/U(\tau)>1$. (2) Rolled back to $Y\le U$, exposure stops. (3) If a sprint builds capability $\varrho_X$ times the rivals' level and hazardous variety is a fraction $\varphi$ of capability's, frozen exposure is zero when $\varphi\varrho_X\le1$. (4) For linear coverage the same frozen ratio costs more the later the sprint; this fails for some sub-exponential coverage.* *Proof.* Integrate. For (4), let $\log U$ rise by 0.5 on each interval $[n^2,n^2+1]$ and stay constant otherwise: $\log U\approx0.5\sqrt t=o(t)$, while $\dot U/U=0.5$ inside each interval. $\square$ With hazardous variety equal to capability's, growth 0.3, linear coverage $1+0.5t$ and $h=0.05$, a sprint to $\tau=10$ leaves survival 0.86; freezing then gives 0.53, and rolling back keeps 0.86.

*Proposition 5.14.* After $t_N$, $U_t\ge U_{t_N}+u(t-t_N)$, so the uncovered share is zero from $t_N+Y_N/u$ on, and Lemma 5.10's upper part bounds survival below. The success function is homogeneous of degree zero, so symmetric intensity is proportional to the stakes for every $\theta<n-1$; an objective bounded in the stakes, such as $1-e^{-\Omega}$, has intensity bounded as they grow (SM(8): intensities 0.19, 1.88 and 18.75 for linear payoffs at stakes 1, 10, 100; 0.12, 0.19, 0.19 for the saturating one). $\square$ (PE.)

### Proof of Proposition 5.15

(1) If the sender's and receiver's payoffs sum to zero, each sender type induces, among the equilibrium actions, one that minimizes the receiver's payoff in its state, so the receiver's payoff is at most that of ignoring messages, which it can always do; equilibrium payoffs equal the no-talk values (TK: 300 games, no exception). (2) At $\theta=-1$ with $n$ actors, $J_k=\pi_k-\frac1{n-1}\sum_{j\ne k}\pi_j$, and direct expansion gives $J_S-J_R=\frac n{n-1}(\pi_S-\pi_R)$ and $J_S+J_R=\frac{n-2}{n-1}(\pi_S+\pi_R)-\frac2{n-1}\sum_{k\ne S,R}\pi_k$: effects on third parties enter both alike. In the uniform-quadratic model with $\pi_S=-(y-u-b_0)^2$, $\pi_R=-(y-u)^2$ and third parties' payoffs linear in $y$, the ideal points differ by $b_0n/(n-2)$, independent of the third-party terms, and Crawford and Sobel's condition applies to that bias. (3) A sender that intends to race prefers the receiver to cooperate: with $R=1$, $T=2\varepsilon$, $P=\varepsilon$, $S=0$, it gains $\varepsilon$ from the receiver's cooperation however small $\varepsilon$ is (compare Aumann 1990). $\square$ *Numerics (T3):* the identity holds to $3.6\times10^{-15}$; numerically maximized ideal points match $b_0n/(n-2)$ for $n=3,4,6,10$; a two-message partition equilibrium, built directly with indifferent boundary types and numerical best responses, exists iff the effective bias is below 1/4; with $b_0=0$ and a common cost to third parties, full revelation is an equilibrium.

### The scissors in a reduced form

In the binary game of Remark S5.1 at the boundary case, let actors act on $\theta_\Gamma(\theta_0,\Gamma_\delta)$, with the compounding contest running alongside so that the state effect is absorbed to first order by the price of standing. The largest discounted loop gain at which restraint remains enforceable is, for $\theta_0=0$ and $\theta_0=0.4$: 0.92 and 0.95 at $p_d=0$; 0.85 and 0.91 at $p_d=0.5$; 0.39 and 0.62 at $p_d=0.9$; and none above $p_d=0.99$ (NB).

## S6. AI: instrument and incarnation

### Proof of Proposition 6.1

Changing $a_i$ from 0 to 1 changes $u_i$ by $\epsilon b-c-\epsilon d$, independent of the others' choices, and each other $u_j$ by $-\epsilon b/(n-1)-\epsilon d$. Summing, the relative terms cancel, which gives (1); in objectives racing changes $J_i$ by $\epsilon b(1-\frac{\theta}{n-1})-c-\epsilon d(1+\theta)$, which gives (2). For (3), write $\theta^\ast=(T-D-c)/(T/(n-1)+D)$ with $T=\epsilon b$, $D=\epsilon d$ growing with exponents $1+\beta_b$, $1+\beta_d$ and $c$ with $\beta_c$, and take limits. $\square$ *Numerics (SM(5)):* exponents $(0,0,0)$ and $(1,1,0)$ give the limit 1.50; $(0,0.5,0)$ gives $-0.99$; $(0.5,0,0)$ gives 2.998; $(1,0,3)$ and $(0,0,1.5)$ give $-\infty$; at equality, $(0,0,1)$ gives 0.9375 and $(1,0,2)$ gives 2.1. With $b,d,c$ fixed, $\theta^\ast$ is 1.44 at $\epsilon=10$; with $c$ also scaling with $\epsilon$ it stays 0.94. With $n=4$, $b=1$, $c=0.3$, $d=0.2$, $\epsilon=1$, all racing gives each $-1.1$; lowering $d$ to 0.1 and 0.05 cuts the loss to 0.70 and 0.50 while raising $\theta^\ast$ to 1.39 and 1.70. The condition earlier written as $\beta_c<\beta_b=\beta_d$ was neither necessary nor sufficient; the correct one is $\beta_c<1+\max(\beta_b,\beta_d)$.

### Proposition 6.2 in full, and Lemma 6.3

*Each actor chooses $\iota_i\in\{0,1\}$; strength is $1+s\iota_i$; defeat costs $L_e$; a loss of control by any actor costs every actor $L_c$; the hazard of losing control is $\psi_0$ without delegation and $\psi_1>\psi_0$ with it, $\Delta\psi=\psi_1-\psi_0$; payoffs are $-L_e(1-w_i)-L_c[1-\prod_j(1-\psi_j)]$. (1) If $k$ others delegate, delegating gains $L_e[w_i(1,k)-w_i(0,k)]$, increasing in $s$ and tending to $L_e(1-1/n)$ for $k=0$ and $L_e/(k+1)$ for $k\ge1$, and costs $L_c\Delta\psi(1-\psi_0)^{n-1-k}(1-\psi_1)^k$. (2) Delegation becomes strictly dominant as $s$ grows iff the limiting gain exceeds the cost for every $k$; $L_e/n>L_c\Delta\psi$ suffices. (3) Universal delegation is worse for every actor than none, by $L_c[(1-\psi_0)^n-(1-\psi_1)^n]$. (4) Under relative objectives the shared loss cancels and delegation is chosen at every $s>0$.* *Proof:* direct computation; with all delegating, $w_i=1/n$ as with none and the hazard is higher. With $n=3$, $r=1$, $L_e=L_c$, $\psi_0=0.01$, $\psi_1=0.2$, the dominance threshold is $s^\ast\approx1.16$, where a lone delegator wins with probability about 0.52.

*Lemma 6.3.* With $\dot{\mathcal M}=-\delta_h\mathcal M$ under delegation and $\dot{\mathcal M}=\varrho_h(\bar{\mathcal M}-\mathcal M)$ otherwise, the lock time is $\ln(\mathcal M_0/\mathcal M_{\min})/\delta_h$ and the recovery time $\varrho_h^{-1}\ln[(\bar{\mathcal M}-\mathcal M)/(\bar{\mathcal M}-\mathcal M_{\min})]$.

### Proposition 6.4 in full, and proof

*Let locked delegation end the delegator's ability to overrule with probability $q_L$; losing the contest mean subordination with probability $p$; $Q=\prod_j(1-\psi_j)$; and, with $r=1$, $\Phi_i=(1-q_L\iota_i)Q[w_i+(1-w_i)(1-p)]$. (1) If $q_L=1$ and $Q>0$, not delegating gives strictly higher survival for every finite $s$, every $n$, every $p$ and every profile of the others. (2) With $k$ others delegating, $p=1$ and $a=(1-\psi_1)/(1-\psi_0)$, $\Phi_D/\Phi_N=(1-q_L)a(1+s)\frac{n+ks}{n+(k+1)s}$; with $A=(1-q_L)a$, all delegating is an equilibrium iff $A(n+(n-1)s)/n\ge1$ and no one delegating iff $An(1+s)/(n+s)\le1$. At least one always holds, since $A(n+(n-1)s)/n-An(1+s)/(n+s)=A(n-1)s^2/[n(n+s)]\ge0$, and both can. (3) At bounded speed one delegator does not drive another's survival to zero: with $p=1$ a non-delegator facing $k$ delegators has $Q_N/(n+ks)>0$.* *Proof.* (1) $\Phi_D=0$ while $\Phi_N\ge Q_Nw_N>0$. (2) By the strengths $1$, $1+s$ and the formula; the identity gives the "at least one". (3) Immediate. $\square$ *Numerics:* part (1) holds for 20,000 random draws (`../v5/checks_v5.py`, DL); in SM(6), over 100,000 draws, "neither" never occurs and "both" occurs 4,068 times. With $n=2$, $q_L=0.99$, $\psi_0=0.01$, $\psi_1=0.05$, all delegating is an equilibrium only for $s\ge206.4$, with survival 0.0045 there.

### Proofs of Lemma 6.5, Remark 6.6 and Proposition 6.7

*Lemma 6.5.* Variants acting on common terms exist and have relative performance lower by at least a positive margin, so under cumulative retention their share tends to zero, as in Proposition 3.4; the retained systems' decisions are the actor's. If constraints are an enforced admission condition, no admissible variant violates them. That an actor which cannot overrule decisions taken in its name has lost O2 in that domain is a definition. For a reader who counts survival only as preservation of the unit, delegation acts through the shared hazard instead: delegated systems interacting at machine speed without a human veto raise the probability of shared loss by reciprocal fear of surprise attack (Schelling 1960), inadvertent escalation (Posen 1991) and flash war (Scharre 2018), an argument with cited mechanisms, not a derivation.

*Proposition 6.7.* (1) Level 2 is relative and payoff-monotone, so Lemma 3.3(1) removes every term common to all developers. (2) Level 0 maximizes its reward by definition; level 1 chooses rewards and constraints to maximize the developer's objective, which counts privately visible divergences through customers, liability and reputation; under $(A_\tau)$ countering lowers the developer's relative payoff by a positive margin net of every private benefit, so with cumulative selection countering developers' share tends to zero (Proposition 3.4(2), developers as carriers). (3) A constraint borne by one developer lowers its relative payoff; one enforced on all as a condition of admission is a common term among compliers when its incidence is equal, and Lemma 3.3(3) gives the evasion condition. $\square$ *Numerics (CI):* a unilateral safeguard that cuts error from 0.20 to 0.01 at cost 0.01 is selected for (its share tends to one), which is the case $(A_\tau)$ excludes; a safeguard whose benefit is common is selected away.

*Interface.* What level 2 selects on is the developers' relative payoff, of which the trained systems' contribution to relative standing is part. Under a public mandate, or a national laboratory that only moves relative selection to the level of states, the result applies at that level or not at all.

### Proofs for Section 6.5

*Proposition 6.8.* The residual hazard is $q_0(1-c_b)+q_c$; compare with $q_0$. With base hazard 0.1 a period, a corrector blocking 99% and adding $2^{-(t+2)}$ raises survival to period 200 from $7\times10^{-10}$ to 0.63 (`../v5/checks_v5.py`, OV).

*Proposition 6.9.* Each layer covers $m_\ell$ times the attention of the layer above, so $k=\ln(Y/\mathsf B)/\ln m_\ell$ layers are needed; a serial chain catches a problem only if every link succeeds, $f^k=(Y/\mathsf B)^{\ln f/\ln m_\ell}$. Independent checks across the gap fail together with probability $(1-f^k)^k$; a common cause defeating all with probability $q_{\rm cc}$ leaves at most $1-q_{\rm cc}$. Layered redundancy needs every layer to succeed. With $f=0.9$, $k=6$: the serial chain catches 0.53; six checks across the gap 0.989, or 0.940 under a common cause with $q_{\rm cc}=0.05$; layered redundancy 0.941 with two checks per layer and 0.994 with three. With a blind spot common to all checks covering a share $\rho_{\rm cc}$ of hazards, catch rates are 1.000, 0.950 and 0.700 at $\rho_{\rm cc}=0$, 0.05, 0.3 (SM(7)). Common causes include shared training sources, shared models, shared funders and collusion among untrusted monitors, which the control literature treats as a design variable (Greenblatt et al. 2024).

**Remark 6.10 in full.** In a system with largest Lyapunov exponent $\lambda_L>0$, an initial error $\epsilon_{\rm obs}$ reaches a tolerance $\Delta_{\rm tol}$ after about $\lambda_L^{-1}\ln(\Delta_{\rm tol}/\epsilon_{\rm obs})$, so a $k$-fold gain in precision extends the horizon by $\lambda_L^{-1}\ln k$; in the logistic map at full chaos, errors of $10^{-3}$ and $10^{-12}$ reach 0.1 after 7.5 and 37.5 steps on average. This limits safety cases that predict trajectories, such as "the margin we bought will suffice", not certification of invariants, reachable sets or probabilistic bounds. That AI raises the sensitivity of the systems it acts in is a conjecture.

**Proposition 6.11 in full.** *In the delegation model with additive stakes and $r=1$, let each actor choose $\iota_i\in[0,1]$, with strength $1+s\iota_i$ and hazard $\psi_0+\Delta\psi\,\iota_i$; write $x=\Delta\psi\,\iota$, $b_s=\Delta\psi/s$, $q=1-\psi_0$, $K_h=(n-1)L_e/(n^2L_c)$. An interior symmetric equilibrium solves $(x+b_s)(q-x)^{n-1}=K_h$. (1) Where $x\ll q$, the added hazard is $nx\approx(n-1)L_e/(nL_cq^{n-1})-n\Delta\psi/s$, nearly independent of $\Delta\psi$, until delegation saturates. (2) There can be several interior equilibria, and along a branch $\partial x/\partial\Delta\psi=-(q-x)/(s[q-nx-(n-1)b_s])$, whose sign changes between branches. (3) After saturation, realized risk falls with $\Delta\psi$ and can be summable under full delegation and growing speed: with $n=3$, $L_e=L_c=1$, $\psi_0=0$, $s_t=2^t$, $\Delta\psi_t=2^{-t}$, full delegation is an equilibrium for $t\ge5$, with total realized risk at most $3/16$ from then on. (4) With all-or-nothing delegation, any equilibrium with $k\ge1$ delegators has realized hazard above the baseline, so an improvement that carries $\Delta\psi$ across the threshold at which delegation becomes an equilibrium raises realized hazard.* *Proof.* At the symmetric point $\partial w_i/\partial\iota_i=s(n-1)/(n^2(1+s\iota))$ and the marginal cost is $L_c\Delta\psi(1-\psi)^{n-1}$; equate and divide by $s$. (1) approximates; (2) differentiates implicitly (two interior roots at $\iota=0.153$, $0.937$ for $n=2$, $s=100$, $L_e=0.5$, $L_c=1$, $\psi_0=0.01$, $\Delta\psi=0.9$, with the corner also an equilibrium; `../v5/checks_v5.py`, HO); (3) the own marginal gain $2s_t/(9(1+s_t))-\Delta\psi_t(1-\Delta\psi_t)^2$ is positive for $t\ge5$ and the objective is concave; (4) $(1-\psi_0-\Delta\psi)^k<(1-\psi_0)^k$. $\square$ With $n=3$, $s=100$, $L_e=1$, $L_c=100$, $\psi_0=0.01$, the added hazard is 0.0011, 0.0053, 0.0062, 0.0065 and 0.0067 as $\Delta\psi$ falls from 0.19 to 0.005, and falls to 0.0030 only at complete delegation (compare Stafford, Trager and Dafoe 2022; Peltzman 1975; Wilde 1982).

## S7. The present trajectory

### Proofs of Theorem 7.1, Proposition 7.2 and Corollary 7.3

*Theorem 7.1.* Each item of Branch I is the cited result under its condition. Branch I′: above the saturating level further advantage changes no outcome, so $p_d=0$ there. Branch II: backward induction in the multi-period bargaining model of S5 shows that a shift spread over enough periods gives no motive for attack; modes with $a\tau_c<1$ are within proportional correction; and $p_d=\Pr(T_{\rm dec}<\tau)$ is small when detection and response are faster. Branch III: intensity, dissipation and shared loss are proportional to $r$ (Proposition 3.6(1)). That low decisiveness is not enough for Branch III follows from Proposition 2.2: with $r=0.8$ a reflexive channel lifts $\Gamma$ to 1.1 (LG). $\square$

*Proposition 7.2.* The first part is the commitment problem (Fearon 1995; Powell 2006), with uncertainty about intentions (Mearsheimer 2001); an actor that decides by its worst case over a stated set of possibilities, and applies that rule to every action (Gilboa and Schmeidler 1989), counts the worst, while a survival-first actor need not. For the second: if restraint while ahead lowers the probability of winning, Bayes' rule gives $\Pr(\text{extends}\mid\text{wins})>\Pr(\text{extends})$ for conduct before victory, and repeated selection compounds it (Proposition 3.4); carrying the inequality to conduct after victory needs the stated correlation. $\square$

*Corollary 7.3.* Proposition 5.1(1) gives the individual best response; Propositions 5.7 and 7.2 give the collective course. $\square$

### The full table of shared parameters

The core's table in Section 7.1 abbreviates the following. "↑" means a rise in the parameter raises the danger at that threshold.

| Parameter | Loop gain | Working objective | Enforcement ($p_d$, $\bar p_d$) | Capture certificate | Talk (two parties) | Tempo and coverage |
|---|---|---|---|---|---|---|
| sharing $\beta$ | ↓ (every channel scaled by $1-\beta$) | ↓ | $g$ falls: ↓; promised sharing ↑, since a decisive winner can renege; contemporaneous custody neutral | — | ↓ | — |
| convertible share $\kappa_c$ | ↑ when $k_0>0$; none when $k_0=0$ | as left | ↑ (time to decisiveness shortens) | ↑ for conversion into control | via $\theta_\Gamma$ | — |
| provision not won, $k_0$ | ↓ (lowers $\omega$) | ↓ | ↓ ($p_d$ falls; laggards keep a sanction, $v$ falls) | — | ↓ | — |
| decisiveness $r$ | ↑ | ↑ | ↑ ($p_d$ and $g$ rise) | ↑ via reflexive channels | ↑ | — |
| diffusion $\delta_f$ | ↓ | ↓ | ↓ (leads decay) | — | ↓ | — |
| appropriability $\chi$, conversion $b_{ij}$ | ↑ (reflexive channels) | ↑ | ↑ (captured sanctioners raise $v$) | ↑ | ↑ (captured indicators raise masking) | ↑ (captured assessment lowers coverage) |
| correction rate $d$ | ↓ | ↓ | ↓ | ↓ | ↓ | ↓ |
| cost of control, falling with AI | ↑ | ↑ via $\Gamma$ | ↑ via $v$ | ↑ | via masking | ± |
| fixed cost of control $f$ | — | — | — | ↓ (threshold; requirement levels off) | — | — |
| stakes $\Omega$, provision fixed | ↑ ($\omega$ rises) | ↑ | ↑ via $p_d$; neutral if all terms scale alike | ↑ (rule support worth more) | ↑ | ↑ via variety |
| breakout probability $p_d$; detection lag | — | — | ↑ | — | — | — |
| decisive value relative to cooperation, $D-C$ | — | — | ↑ ($\bar p_d$ falls) | — | — | — |
| patience $\delta$ | ↑ ($\Gamma_\delta$ rises) | ↑ | ↓ (repetition stronger): two-edged | — | via $\theta_\Gamma$ | — |
| held self-model $\theta_0$ | — | ↓ | ↓ | — | ↓ | — |
| variety, coverage, residual floor | — | — | — | — | — | carry it all |

*Interfaces.* Each entry is a result in its own model, and an entry that crosses models goes through an interface of S13. That the parameters move together in the world is a conjecture, which Tests Γ and E address.

### The mechanism index

The loops of Section 7.1 act through mechanisms that overlap; each is stated separately because each has its own formal anchor, measure, counter-mechanism and analogue in other substrates. They concern three objects that reinforce one another without being interchangeable: what actors value (accounting and boundary), what actors believe (observation, attribution and language), and what institutions reward, permit and protect (compounding, selecting the selectors, decisiveness and tempo).

| Mechanism | Formal anchor | Measure | Generative counterpart | Requirement | In other substrates |
|---|---|---|---|---|---|
| Accounting at the boundary | Lemma 3.3; Propositions 3.4, 3.5, 3.6, 3.9 | $\theta$ (with $\psi$); $\lambda$; $\kappa$ | Reward separated from advantage; consequences return | R1, R2, R7 | Evolutionary suicide; microbial commons; positional goods |
| Compounding and conversion | Propositions 2.2, 2.3, 5.1, 5.2 | $\Gamma$; $\beta$, $\kappa_c$, $k_0$, $r$; persistence of leads | Reward separated from advantage; provision beneath the game; a point of enough | R4 | Increasing returns and lock-in; cumulative advantage; clonal expansion |
| Selecting the selectors | Propositions 4.3–4.11; Theorem 4.12 | Row sums; conversion $b_{ij}$; lineage shares; error correlation | Correction in common hands | R3 | Meiotic drive; immune editing of tumours; regulatory capture |
| Tempo | Propositions 5.11, 5.13, 6.2, 6.4; Theorem 5.12 | $a\tau_c$; $\dot U/U$ against $\dot Y/Y$ | A point of enough; development at the pace of understanding | R5 | Red Queen dynamics; requisite variety |
| Decisiveness | Proposition 5.4; Corollaries 5.5, 5.6; Proposition 5.7 | $p_d$, $\bar p_d$; detection against breakout | Common custody before decisiveness | R4 | The commitment problem in war |
| Masking and attribution | Proposition 4.7; Remark 4.8; Proposition 11.2 | Evaluator bias against ground truth; responses to signals of intent | Reasoning instead of winning; verifiable conduct | R6 | Immune editing; the security dilemma |
| Alienation of language | Proposition 5.15; Remark 4.8 | Informativeness of talk; indicator gaming | Reasoning instead of winning | R6 | Preference falsification; Goodhart's law |
| The training loop | Proposition 6.7; Lemma 6.5 | Retention by contest performance; admission constraints; the alignment tax | Common admission constraints | R8 | Selection on proxies in any optimizer |
| The gain | Section 7.1 | Perceived existential competition (C8) | Provision beneath the game | — | — |

Some overlaps can be named. Masking is selecting the selectors applied to observation. Decisiveness is reached faster where the loop gain is larger (Remark S2.1), while whether a position beyond sanction exists is a separate condition. The alienation of language is accounting applied to talk, together with selecting the selectors applied to narratives. Tempo decides whether any counter-mechanism arrives in time.

## S8. Comparing paths

### Proof of Lemma 8.2

Couple the two paths by a common uniform draw $U_t$ each period: the event occurs on a path at $t$ when $U_t$ falls below that path's conditional hazard given the shared world history. On every history on which both have survived to $t$, the two conditions give $A$'s hazard at most $C$'s, so $\{A\text{ fails at }t\}\subseteq\{C\text{ fails at }t\}$. By induction the event "$C$ survives to $H$" is contained in "$A$ survives to $H$", path by path, whatever the rule by which $A$ dissolves, so $\Phi^A(H)\ge\Phi^C(H)$. $\square$

*A step that fails.* Comparing after conditioning on the dissolution date, $\Phi^A(H\mid\tau)\ge\Phi^C(H)$ for every $\tau$, is not valid when dissolution depends on the state: in a two-state Markov world in which bad states make dissolution more likely, the conditional comparison fails (0.291 against 0.324 in SM(4)), while the coupled comparison holds at horizons 10, 30 and 100. If $C$'s hazard is a deterministic schedule, the two conditions need only be stated on $A$'s histories. *Example (FD):* with dissolution at 2% a period and a fallback that restarts continuation ten periods later, the arrangement survives with probability 0.976, 0.864 and 0.211 at horizons 10, 30 and 100, against 0.875, 0.575 and 0.026 for continuation.

### Proposition 8.3 in full

*Survival is computed with per-period conditional probabilities over a common horizon. Let $h_R$ be the hazard under restraint, $q_{\rm I}$ the loss of the ability to overrule by delegation, $q_{\rm II}$ the shared hazard, $q_W$ the hazard of preventive attack, $p_{\rm dec}$ and $p^S_{\rm dec}$ the probability that a racer's advantage becomes decisive when all race and when the actor stays out, and $p_{\rm ext}$ the actor's belief that a decisive winner would extend its dominance over it. With independence, $\Phi^R=1-h_R$, $\Phi^T=(1-q_{\rm I})(1-q^T_{\rm II})(1-q_W)$, $\Phi^P=(1-q_{\rm I})(1-q^P_{\rm II})(1-q_W)(1-p_{\rm dec}\frac{n-1}n)$, $\Phi^S=(1-q^S_{\rm II})(1-p^S_{\rm dec}p_{\rm ext})$. (1) The advantage of cooperating is $\varpi(\Phi^R-\Phi^T)+(1-\varpi)(\Phi^S-\Phi^P)$: dominance, stag hunt with threshold $(\Phi^P-\Phi^S)/((\Phi^R-\Phi^T)+(\Phi^P-\Phi^S))$, chicken, or prisoner's dilemma by the signs. (2) Where $\Phi^S\ge\Phi^P$ and $\Phi^R\ge\Phi^T$ an actor that holds the prediction restrains whatever it believes. (3) Mutual racing is a strict equilibrium at every horizon with $\Phi^P_H>\Phi^S_H$. (4) For constant hazards, $\Phi^B(H)/\Phi^R(H)=((1-q_B)/(1-q_R))^H$. (5) If an actor gives the premises of Section 5.3 probability $p_{\rm prem}$, the classification at horizon $H$ uses mixtures, and when the arrangement's own survival also decays the signs can fail at long horizons.* *Proof:* linear in $\varpi$; substitution. $\square$ *Numbers* ($n=2$, $p_{\rm ext}=1$): with $q_{\rm I}=0.6$, shared hazards 0.3 (0.4 when all race), $q_W=0.2$, $p_{\rm dec}=0.6$, $h_R=0.1$, survivals are 0.90, 0.22, 0.13 and 0.28 and cooperation is dominant; with low delegation the game is a stag hunt with threshold 0.16; for a leader that wins with probability 0.8 if it races, the threshold is 0.42 when the shared hazard is 0.3 and 0.11 when it is 0.8: for the leader, the shared hazard carries the argument. With $p_{\rm prem}=0.99$, the arrangement's survival $e^{-0.005H}$ and race branches decaying at 0.05 when the premises hold, the arrangement beats the mixed race at $H=10$, 100 and 600 but not at 1,000 (`../v5/checks_v5.py`, SR).

*Discounting.* Under a discounted objective with constant race hazard $h$ and growth rates $g_r$ racing and $g_p$ paced, a race is preferred iff $h<g_r-g_p$, though it ends in catastrophe with certainty (Jones 2024); a rising hazard reverses the preference only if it comes to exceed the growth differential. Jones (2024) also finds that falling mortality raises the acceptable risk, which belongs to crux C10.

### The alternatives: results stated briefly in the core

**Remark 8.6 (What a lead buys).** (1) With diffusion at rate $\delta_f$, a lead $\Delta_0$ held by a leader that pauses lasts $\delta_f^{-1}\ln(1+\delta_f\Delta_0)<\Delta_0$: a six-month lead diffusing at 0.1 a month lasts 4.7 months, a two-year lead about a year. (2) The margin is time, but what it must buy is coverage, which rises by about $\dot U\Delta$ while uncovered variety grows; for hazard classes with an evidence lag above $\Delta$ it buys nothing. (3) Whether it suffices is judged by the leader's own evaluators under time pressure. (4) In a static contest the follower raises effort when the leader slows (Dixit 1987); in dynamic races a large lead discourages it, and a leader seeing its window close has a motive to strike first (Van Evera 1999). On their own median estimates, the planners of one detailed scenario judge that spending part of a lead buys about a third of the reduction in takeover risk that a coordinated slowdown buys (EV10). *Proof of (1):* $\dot\Delta=-\delta_f\Delta-1$ (`../v4/checks_v45.py`, LD).

**Remark 8.7 (The finite sprint as a trade-off).** A finite sprint trades four quantities: exposure during and after it, zero after a freeze if the hazardous ratio built is at most one (Proposition 5.13); erosion of the frozen edge as rivals developing within understanding catch up; rivals' responses, which cannot verify which kind of winner they face; and maintenance of the advantage, which requires stopping others' growth, ending their O2. It can preserve the sprinter's survival while giving up permanent superiority; excluding it as a deviation from a cooperative arrangement needs its net deviation payoff to be negative (Proposition 10.7).

**Proposition 8.8 in full.** *Facing a rival it believes certain to race, comparing by its own survival: (1) a single strike that succeeds with probability $s_P$, returning the field to something like the arrangement, and escalates to catastrophe with probability $\varepsilon_P$, gives $(1-\varepsilon_P)[s_P\Phi^R+(1-s_P)\Phi^P]$, and beats staying out and joining unless $\varepsilon_P>1-\max(\Phi^S,\Phi^P)/(s_P\Phi^R+(1-s_P)\Phi^P)$; (2) sustained prevention against a target that rebuilds with probability at least $b_P$ a period, each strike escalating with probability at least $\varepsilon_{\min}$, has per-period hazard at least $b_P\varepsilon_{\min}$; (3) at common horizons, sustained prevention with hazard 0.01 beats racing with 0.05 (0.60 against 0.08 at $H=50$).* *Proof:* compare and solve; Lemma 5.10; $0.99^H>0.95^H$. $\square$ With $\Phi^R=1$, $s_P=0.7$, $\varepsilon_P=0.2$ and race branches near zero it gives 0.56. Shifts that cannot be observed raise the chance of mistaken prevention (Debs and Monteiro 2014); verification that supports deterrence can also supply targets (Coe and Vaynman 2020). An actor that manipulates shared risk as an instrument (Schelling 1966) plays chicken in survival terms, with mixed equilibria and wars of attrition. When the prior that a capable rival holds an unbounded relative objective is low, a survival-first actor's best course is to propose verifiable limits and take narrow E1 verifiably in its own loops, the costly signal of Proposition 11.2.

**Remark 8.9 (Why insuring against falling behind is not an exit).** Bounding the penalty for falling behind with autonomous, good-enough provision and defence does not leave the contest: the penalty is set by the winner, not the laggard, so the bound is as reliable as the belief that a winner would not extend dominance; a winner with a relative objective has a motive to destroy what the laggard secured; and it accepts the frame of the contest. Defence that makes decisive advantage unattainable for everyone lowers $r$ for all and belongs to E2, if it stays under human oversight. Shared provision belongs to a world that has left the contest.

### Proofs for the verified agreement

**Proposition 8.10 in full.** *Payoffs $R,T,P,S$; a defection detected in time is reversed, the defector receiving $P-F$ and the cooperator $P$; undetected defection yields $T$ and $S$. With $T_\upsilon=\upsilon(P-F)+(1-\upsilon)T$, $g_C=R-T_\upsilon$ and $g_D=(1-\upsilon)(P-S)$: (1) the advantage of cooperating is $\varpi g_C-(1-\varpi)g_D$, with the four cases of the core and, if both are negative, chicken; (2) the verification and trust conditions as stated; (3) cooperation is risk-dominant iff $g_C>g_D$, a property of payoffs selected under global games and adaptive play (Carlsson and van Damme 1993; Kandori, Mailath and Rob 1993; Young 1993); (4) with $n$ players and independent belief $\varpi_1$ about each rival, $\varpi_1^{n-1}\ge\varpi^\ast$ suffices only if a cooperator gets at least $S$ when some but not all others defect and the advantage of defecting in any such state is at most $g_D$.* *Proof:* (1) cooperating yields $\varpi R+(1-\varpi)(\upsilon P+(1-\upsilon)S)$, defecting $\varpi T_\upsilon+(1-\varpi)P$; (4) bound the intermediate states. Without the second bound the condition fails: with advantages $(1,-10,-1)$ by number of defecting others in a three-player game, each rival cooperating with probability $\sqrt{0.5}$ gives $-3.73$ although all others cooperate with probability 0.5 (`../v5/checks_v5.py`, N13). $\square$

**Proposition 8.12 (Commitment under a growing overhang) [thm].** *Let $\mathcal O(t)$ be the capability an agreement holds in check, $X$ and $X_{\rm stay}$ the values of exiting first and of staying, exit occur at hazard $\mathcal H$, a fraction $\mu_x$ of the overhang be destroyed on exit, and the expected loss from exit be $\mathcal L=\mathcal H(1-\mu_x)\Lambda_x(\mathcal O)$ with $\Lambda_x$ increasing. (1) Deterring an irreversible, public exit requires $\upsilon F\ge X-X_{\rm stay}$; deterring a reversible covert preparation requires $\upsilon F\ge(1-\upsilon)(X-X_{\rm stay})$; the net exit gain grows with the overhang when leaving with a decisive advantage gains faster than staying with one's share. (2) $\dot{\mathcal L}/\mathcal L=\dot{\mathcal H}/\mathcal H-\dot\mu_x/(1-\mu_x)+\varepsilon_\Lambda\dot{\mathcal O}/\mathcal O$, so growth of the overhang faster than the decline of the exit hazard is not sufficient for the loss to rise. (3) An agreement that preserves relative positions preserves the relative term of every payoff, and with it the motive in $X$.* *Proof:* expected values; differentiate $\ln\mathcal L$ (counter-case: $\mathcal O=e^{2t}$, $\mathcal H=e^{-1.5t}$, $\Lambda_x=\sqrt{\mathcal O}$, $\mu_x=0$ give $\mathcal L=e^{-0.5t}$); proportional caps leave each $w_i$ unchanged. $\square$

*Theorem 8.11.* (1) Rearrange $R>T_\upsilon$. (2) Timely detection is detection before decisiveness. (3) collects Propositions 5.15, 8.12 and Section 4. (4) Bounding the largest undetected defection bounds $T$; the rate condition compares the coalition's advantage with its erosion by diffusion; revealing types is the information role of Proposition 10.7. $\square$

*An instance.* One detailed plan among leading powers to slow development and delay superintelligence to about 2040 combines compute declarations, supply-chain accounting, inference-only retrofits and recomputation of workloads, research transparency, mutually assured destruction of compute if the deal declines, and hardened reserves of about two per cent of pre-deal compute; it bounds covert projects rather than requiring near-perfect detection, the second route of Theorem 8.11. One author's scenario judgment puts decline at about four per cent a year in years five to ten, cumulatively near half over ten years (EV10; X8 gives the durability table).

### An illustration of the two cruxes

Let the per-period hazard on a path be 0.05 times its uncovered share plus a background 0.001, and on the cooperative path add a dissolution hazard times the loss its fallback carries. Survival at horizons 10, 30 and 100: continuation with the uncovered share rising from 0.2 by 0.01 a period, 0.871, 0.567, 0.028; continuation with a summable uncovered share, 0.966, 0.941, 0.873; cooperation with a summable share and dissolution 2% a period with fallback loss 0.5, 0.873, 0.696, 0.319; cooperation with dissolution 0.2%, 0.956, 0.913, 0.789. The numbers are illustrative; they show that a well-corrected continuation can beat a fragile arrangement, and that a rising uncovered share makes any modestly durable arrangement better past the near term.

## S9. Requirements

### Proposition 9.1, row by row

Each necessary row is the cited result read as a necessary condition in its model and over its horizon; the last column of the core's table states when the cited result does not apply. The derivations and the counterexamples that fix the scope follow.

- **R1, consequences return.** Theorem 10.5(3): under (reach), with a race carrier present, viability at every horizon needs long-run average effective liability at least the private advantage. *Not at a finite horizon:* a zero-liability trajectory need not cross the floor before $H$. With the host starting at full capacity, floor 0.2, $\rho=0.01$, $h_V=0.02$ and zero liability, even full load from the start keeps $V(50)\ge0.435$, and crosses the floor only at $t=109.9$, although (reach) holds (HO; Codex). At a finite horizon the necessary condition is weaker: liability must keep the cumulative advantage below the path that just reaches the floor at $H$, by monotone comparison.
- **R2, coverage.** Propositions 3.4 and 9.2(1): an uncovered race carrier with unbounded cumulative advantage takes the field. *Not needed* when harms are local, or when the uncovered carriers' combined maximal load cannot reach the floor, $h_Vp_{\rm unc}\bar e<\rho(1-V_{\min})$, or within a horizon shorter than the crossing time.
- **R3a, the rate law.** Proposition 4.5(2): in the field model with $\mathcal C$ captured, a cultivation channel and $[H_\gamma]$, the certificate holds at every date only if $\alpha_{\rm cor}\ge\alpha_{\rm ctl}/(1+\eta)$. *Not needed* with $\chi=0$ or channels removed, with a fixed cost of control that does not fall, with nothing captured, or within a horizon shorter than the failure time.
- **R3b, no core.** Proposition 4.9(4): no capture from every initial state needs an empty core of mutually sustaining capture. *Not needed* if only the states actually reached must be excluded: with a row sum of two, the low initial state $(0.1,0.1)$ stays in the invariant rectangle $[0,0.1]\times[0,0.2]$ and converges to no capture (FA). A full row sum below one is the stronger, sufficient certificate.
- **R4, enforceable breakouts.** Proposition 5.4 with $D\ge C$; Corollary 5.6. *Not needed* in Branch III, above the saturating level of Branch I′, in Branch II with timely detection, when $D<C$, or when objectives and sanctions give $\bar p_d\ge1$.
- **R5, summable uncovered share.** Theorem 5.12 and its converse: if any of (variety grows), (coverage lags), (residual floor) fails, the theorem does not apply; at finite horizons the exposure of Proposition 5.13 replaces it.
- **R6, independent observation.** Remark 4.8 and Proposition 5.15: sufficient for alarms that fire before the floor and for trust without good will; not necessary where channels that observe actions directly suffice.
- **R7, standing.** V3. Proposition 3.11 shows that harm to outsiders is over-produced relative to the system optimum; it does not show that O1 or O2 is reached, so the requirement is normative.
- **R8, admission constraints.** Proposition 6.7(3) and Lemma 6.5: under relative, cumulative selection among developers and $(A_\tau)$, a divergence with common costs persists unless a constraint common to all, of equal incidence and sanctioned against evasion, covers it. *Not needed* where developers are selected by public mandate, where the net private cost of the safeguard is zero or negative, where decisions are not retained by contest performance; and admission reaches only to release.

**Sufficient safeguards.** Full row sums below one certify each corrector domain against every state (Proposition 4.9(2)); the safeguards of Section 10.3 give viability on the forgiving host and, with a margin, on harsher ones (Theorem 10.5); not building, custody and detection faster than breakout lower $p_d$ (Corollary 5.6(a)); verification with $\upsilon F$ at least the net exit gain deters irreversible exit (Proposition 8.12).

### Proof of Proposition 9.2

(1) While $\tau_{\rm eff}<\nu$, a carrier's unilateral contribution to the safeguards is a cost borne by it alone, selected against (Lemma 3.3(2); Proposition 4.4(1)). (2) With rule-makers as players in a contest of standing, unilateral imposition of the liability is restraint in Proposition 3.7, not chosen when $\lambda_s>(\Upsilon_s-n_s)/(n_s-1)$; whether an agreement among them is an equilibrium is governed by Proposition 8.10. (3) Under $\tau(1-x_{\rm rule})>\nu$ the private payoff of load is negative. $\square$

## S10. The generative alternative

### A common frontier

**Proposition 10.1 in full.** *If the value of capability is common, $\pi_i=\Omega(\mathcal E)/n-ce_i-\ell\mathcal E$ with $\Omega$ concave, private incentives give $\Omega'(\mathcal E)=n(c+\ell)$ against the joint optimum $\Omega'(\mathcal E)=c+n\ell$, so total intensity is at or below the joint optimum: the residual failure is too little speed, not too much, and the joint optimum must also respect the host's floor.* (Compare first-order conditions.)

**Proposition 10.2 in full.** *Of $n$ actors, cooperators hold effort $e_c$ and racers choose theirs; whoever wins the decisive contest gains $\Omega$, and every loser bears $L_b$. Under separate frontiers every effort enters the contest separately; under a common frontier cooperators pool effort into one entity of strength $(me_c)^r$, which yields a common value $\Omega_c$ split equally and confers no dominance among them. With $n=4$, $\Omega=\Omega_c=L_b=c=1$, $\ell=0.3$, $e_c=0.05$, $r=1.3$: (1) under separate frontiers the unique pure equilibrium is all racing; (2) under a common frontier all cooperating ($R=0.140>T=0.002$) and all racing are both strict equilibria, cooperating being a best response iff trust in each rival exceeds about 0.61, or 0.82 if a deviator best-responds to fixed intensities; (3) treating the others as a coalition maximizing their summed payoff, the coalition's cooperation is dominant; (4) a small pooled effort ($e_c=0.03$) leaves only all racing, and with $n=2$ all cooperating is an equilibrium for $r$ up to about 1.2; (5) holding $\Omega_c$ and $L_b$ fixed, the pooled effort needed to keep $T\le R$ is 0.0054, 0.035, 0.141 and 0.49 for $\Omega=0.5,1,2,4$.* (`../v4/checks_v45.py`, N22: racers' intensities are the symmetric fixed point of best responses, each verified as a global best response; cases without a symmetric pure equilibrium are excluded.) A common frontier turns a dilemma into a coordination problem while the value of winning is moderate; when it is large, keeping ahead of defectors is the race moved up a level.

### Proof of Proposition 10.3

(1) Pooled payoffs $\pi'_j=(1-\beta)\pi_j+\beta\bar\pi$ give $J_i=[(1-\beta)+\beta(1+\theta_0)/n]\pi_i+[\theta_0(1-\beta)+\beta(1+\theta_0)(n-1)/n]\bar\pi_{-i}$; dividing by the first coefficient gives $\theta_{\rm eff}$, increasing in $\beta$ for $\theta_0<n-1$ with value $n-1$ at $\beta=1$; at $\theta_0=-1$, $J_i=(1-\beta)(\pi_i-\bar\pi_{-i})$, and under relative selection $\pi'_k-\pi'_l=(1-\beta)(\pi_k-\pi_l)$. (2) With the promise kept with probability $\varrho$, each payoff is $w_i[(1-\beta\varrho)\Omega_e+\Omega_s]+\varrho\beta\Omega_e/n-ce_i-\ell\mathcal E$; the shared term cancels from relative selection; a mutant at $y$ among residents at $x$ has relative payoff $\Omega_{\rm eff}(y^r-x^r)/(y^r+(n-1)x^r)-c(y-x)$, with zero slope at $x^\ast=r\Omega_{\rm eff}/(nc)$, concave for $r=1$, and no profitable mutant on a grid for $r<1$ (SH). (3) is Proposition 2.3 with Proposition 2.2's reflexive channel removed when $\chi=0$; then the return to influence is zero (Proposition 4.3) and $d^\ast=A/c_{\rm ev}$ (Proposition 4.5(1)). $\square$ *Numerics:* with $n=4$, $r=1$, $c=1$, $\Omega_e=1$, the uninvadable intensity is 0.25 without a positional part, and 0.125 with half the divisible prize shared; with $\Omega_s=1$, sharing all of $\Omega_e$ only halves it from 0.5 to 0.25; in a common field of intensities $(0.2,0.05,0.1,0.1)$ the higher-intensity carrier out-earns the lower by 0.017 with half shared, and the difference turns negative only beyond 55%. An earlier version said that only changing what winning converts into reverses the direction; in this model none of the three levers makes the selected intensity zero while a positional prize remains.

**Remark 10.4 in full.** At the first order, more contenders make the race fiercer (Proposition 5.1(4)) and fragmentation raises speed and conditional risk (Bueno de Mesquita, Dziuda and Polborn 2026); at the second, cultivated influence rises with $\sum_kp_k^{1+(2-\xi_v)/\eta}$ (Proposition 4.5(4)). A merged frontier also raises connectivity and with it common-mode failure, so it keeps modules of independent lineage inside it (Proposition 6.9).

### Proof of Theorem 10.5, and the margin on harsher hosts

(1) (I2) with margin in rule-making gives a full row sum below one, so $x_{\rm rule}\to0$ (Proposition 4.9(2)); once (I1) is enacted, $\tau_{\rm eff}>\nu$ after a finite time, load has negative private payoff, $E\to e_{\min}$, and $\liminf V\ge1-h_Ve_{\min}/\rho>V_{\min}$ on the host (3). For unanticipated harms, (I2) in evaluation gives $x_{\rm ev}\to0$, so masking falls to $m_{\rm out}<m_{\rm fl}$, or the conservative rule applies, and the alarm fires above the floor. (2) Without (I1), Proposition 3.4 applies; without (I2) in rule-making, $x_{\rm rule}\to1$ and $\tau_{\rm eff}\to0$; without (I3), silent crossing follows; with rule-making captured first, the floor can be crossed when rule-making adapts slowly. (3) If the long-run average is below $\nu$, there are $\epsilon>0$ and $T_0$ with average at most $\nu-\epsilon$ beyond $T_0$; the high-load carrier then grows relative to every lower-load carrier and the argument of Proposition 3.4 applies. $\square$

*The transient and the margin (HO).* On the logistic host, with liability $\Delta=\tau_{\rm eff}-\nu=0.08$ from the start and the race strategy holding 99% of activity, the host dips to 0.1397 before recovering. On the pointwise harsher threshold host $\rho_A(V/A-1)(1-V)$ with $e_{\min}=0.1$ and the same initial composition, the minimum margin $\Delta_{\min}$ that keeps the transient above the host's own threshold $V_u(e_{\min})$ is 0.26, 0.31, 0.36, 0.42 and 0.51 for $A=0.05,0.10,0.15,0.20,0.25$, with $V_u$ equal to 0.25, 0.31, 0.36, 0.42 and 0.48. For $A\ge0.10$, $V_u$ lies above a normative floor of 0.3, so the floor must be set no lower than the host's threshold for crossing it to be the first loss. This is the first computable instance of the correctable kernel of Definition 8.1.

### Proofs of Propositions 10.6 and 10.7

*Rival verification.* Apply Proposition 4.9(2) to the verifier's full row. A verifier taking 0.10 from the verified party and 0.95 from shared sources is captured once those sources are. A verifier biased toward finding violations is an uninformative sender of unverifiable claims (Proposition 5.15), so it must rest on evidence the other side can check.

**Proposition 10.7 in full.** *Two actors have private types, strong or weak, with costs $c_s<c_w$, each strong with probability $p_s$ independently. Outside the arrangement types are revealed in a complete-information all-pay contest for $\Omega+L_b$: a strong actor against a weak one gets $U=(\Omega+L_b)(1-c_s/c_w)-L_b$, otherwise $-L_b$; the race's survival is $\Phi^{\rm race}$. The arrangement yields a common value net of costs $S_a$, divided in shares $\mathsf s_i$, with survival $\Phi^R$; utility is $\Phi_i(V_i+\bar V)$. (1) Under complete information and transferable utility, a pair gains iff $\Phi^R(S_a+2\bar V)\ge\sum_i\Phi^{\rm race}_i(U_i+\bar V)$. (2) With private independent types and participation decided before types are revealed, Bayesian incentive compatibility makes each type's interim expected share independent of its report, budget balance makes the interim shares constants summing to one, and the arrangement is feasible without verification iff $\Phi^R(S_a+2\bar V)\ge\sum_i\sup_cE[\Phi^{\rm race}(c,t_j)(U_i+\bar V)\mid c]$; ex-post shares may still vary with reports. (3) Verification revealing types removes the information rents, distinct from timely detection of defection. (4) The information condition relaxes as $\Phi^{\rm race}/\Phi^R$ falls. (5) Under complete information an overwhelmingly strong actor takes part only for a share near its race payoff; raising the joint value, lowering the value of winning, compressing survival or changing cost asymmetry can still make equal shares feasible.* *Numerics:* with $c_s/c_w=0.1$, $\Omega=1$, $L_b=0$, $S_a=1$ and every $\Phi=1$, the sum of suprema is 0.36, 0.90, 1.44 and 1.71 at $p_s=0.8,0.5,0.2,0.05$: feasible without verification in the first two cases and not in the last two, although cooperation is efficient for every pair; with $\Phi^R=0.95$, $\bar V=1$ and $p_s=0.2$, equal shares become feasible once $\Phi^{\rm race}/\Phi^R\le0.872$ (`../v5/checks_v5.py`, K7). Which mechanism is second-best depends on the mechanisms allowed and on commitment, not solved here.

## S11. The transition

### Proofs of Corollary 11.1 and Proposition 11.2

*Corollary 11.1.* Each item follows from the stated formula: $T-R$ in Proposition 8.10; the bias of messages through the weight on winning in Proposition 5.15; the net exit gain in Proposition 8.12; Proposition 5.4 for sanctions against a decisive defector; and $P-S$ in the threshold.

**Proposition 11.2 in full.** *A sender is survival-first and prices in the lock (type S, probability $1-\mu$) or holds a relative objective (type R, probability $\mu$). It can send $E$: a verifiable, durable removal of AI from its own strategic decision loops for a period, open to inspection, costing type $t$ the amount $k_t$. A receiver restrains iff its posterior that the sender is S is at least its threshold $\varpi^\ast$; the receiver's restraint is worth $G_t$ to type $t$, including, for R, what it gains by exploiting it. (1) A separating equilibrium, S sending, R not, the receiver restraining after $E$ only, exists iff $k_S\le G_S$ and $k_R\ge G_R$, with the belief that a non-sender is R. (2) If $k_R<G_R$, R imitates, no separating equilibrium exists, and the receiver restrains after $E$ only if $1-\mu\ge\varpi^\ast$. (3) Hence $E$ separates only if it costs a relative-objective actor at least what it gains by inducing restraint, which requires it to be durable, verifiable and costly to reverse.* *Proof.* Best responses given the receiver's strategy, and Bayes' rule on path. $\square$ With $k_S=-0.05$, $k_R=0.30$, $G_S=0.40$, $G_R=0.20$ separation holds; if the step can be reversed cheaply ($k_R=0.05$) it does not.

### Proofs of Proposition 11.3 and Proposition 11.5

*Pause.* Shifting the residual sequence leaves the product over any window of the same length unchanged, and the infinite product is zero by Lemma 5.10. A pause after which the sequence is summable keeps survival bounded away from zero: with residual hazard 0.01 a round for 20 rounds and $0.01/k^{1.5}$ in the $k$-th round after a change, survival to round 10,000 is 0.80. The field-model part is Proposition 4.11.

*Reachable path.* Existence is Proposition 10.2 and Theorem 10.5; reachability is Propositions 8.10, 8.3 and 6.4; survival during the transition is Theorem 10.5(1) and Lemma 6.3; persistence is Propositions 8.12, 10.6, 4.9 and 4.10. $\square$

### Dwell times

In the field model a reform that insulates rule-making from shares must be held at least until rule support falls below break-even, $\ln G/(\varepsilon d)$, and then long enough to repay the lock-in accumulated meanwhile. The exact minimum hold, in units of $\varepsilon d$, is 1.89, 5.32 and 10.45 for $G=2$, 5 and 10 when rule-making is ten times slower than adoption, and 5.86, 10.34 and 16.18 when the two are equally fast (DW, forward integration in logit coordinates, reproducing the systems review's check). During the first $\ln G/(\varepsilon d)$ the share keeps rising; it is back at its starting level when $G(1-e^{-s})=s$, $s=\varepsilon dt$, that is at $s=1.59$, 4.97 and 10.0, well before withdrawal is safe. A rollback judged on share levels is therefore premature: what decides is where rule support stands relative to the separatrix. For the pause of Proposition 4.11 with rule-making insulated, the required length is $\ln\big((b/d)/S(x_p)\big)/(\varepsilon d)$, with $S$ the separatrix height at the frozen share, and infinite when $x_p\ge x_\sigma$. Keeping a small alternative lineage shortens the dwell; the size of that effect quoted in the systems review (from 10.45 to 3.81 with a 0.1% lineage) has not been reproduced here and is not used in the core.

*Stages.* The slow variable of Stage 2 is human capacity (Lemma 6.3), of Stage 4 the capability held in check (Proposition 8.12). After a recovery, mobilization falls back and certificates can fail again (Remark 4.6).

## S13. Interfaces between the models

The theory joins several models. Each join is an assumption, listed so that it can be checked separately.

| Interface | Between | Assumption | Status |
|---|---|---|---|
| Shared loss and irreversible hazard | The contest (Section 3.4) and survival (Section 5.3) | (hazard–damage link): hazard proportional to shared damage | Modelling premise; crux C1 |
| Coverage and residual risk | Hazardous variety and coverage, and survival | (residual floor) | AI-risk premise; crux C1 |
| Correction rate and coverage | $d$ in the field model and $U$ in Section 5.3 | A production relation $d\le F(U,\text{resources},\text{delay},\text{authority})$ | Open; neither bounds the other |
| Loop gain and breakout probability | $\Gamma$ (Section 2.2) and $p_d$ (Section 5.2) | $p_d=\Pr(T_{\rm dec}<\tau)$, with $T_{\rm dec}$ set by $\Gamma$ (Remark S2.1) | Linearized; the decisive level is crux C5, the detection lag C7 |
| Loop gain and working objectives | $\Gamma_\delta$ and $\theta$ | First order, others' strategies fixed (Proposition 3.9) | The full stochastic game is listed for outside review |
| Shared loss and coupling | $\ell$ and $\kappa$ | Distinct quantities, not counted twice | Maintained (Section 3.4) |
| Selection and strategy | Carrier selection and strategic actors | A selection result transfers only where the selected objective is shown to be the actors' | Rule of Section 3.1 |
| The outer training loop | Developers' relative payoff and trained systems' contribution to it | Level 2 selects on relative payoff, with $(A_\tau)$ | Where developers are selected otherwise, the result does not apply |
| Masking and alarms | Reports and decisions | Averaged, non-strategic reports (A5) | Remark 4.8 treats other rules |
| Capacity and the field | Selected capacity $q^\ast$ and the field model | Quasi-static capacity | Joint simulation not run (TESTS, Study 2) |
| Slow variables of mind | The selected self-model and the field model | A slow variable for the share of decision positions held by the winning model | Not modelled |
| The host | One host and many shared conditions | The forgiving logistic host | Threshold and vector hosts: S3, S10 |

## S14. Counterexamples that bound the claims

Each entry refutes a stronger version of a claim; the text states the weaker claim that survives.

| Counterexample | What it refutes | Where handled |
|---|---|---|
| Three of four actors widen their objective to $\theta=2.9$ and one keeps $\theta=-1$: total intensity falls from 1.0 to 0.015, but the holdout wins with probability 0.989 | That widening the self removes the problem; inclusion is not self-enforcing against one holdout | Coverage, not identity (Proposition 9.2); limits on what winning confers (Proposition 10.3) |
| With $D<C$, cooperation that is not a stage equilibrium survives $p_d=1$ | That decisiveness always shrinks enforcement to stage equilibria | Proposition 5.4(4) |
| The bound without the breakout term says "sustainable" when deviation pays (10,723 cases with $D>C$) | That the old bound is exact | Proposition 5.4(3) |
| Reversion to a race in which breakouts occur raises the punishment value above cooperation | That reverting to the race always punishes | Proposition 5.4(5) |
| Three players with role-differentiated punishment sustain cooperation among purely relative actors for $\delta\ge0.706$ | That relative actors can enforce nothing | Corollary 5.5 |
| Among three actors at $\theta=-1$, talk raises the receiver's value from 1/4 to 1/2 | That relative accounting makes all talk uninformative | Proposition 5.15(2) |
| Costs $(0.6,0.2,0)$ from one cap on loads $(1,0.6,0.2)$ | That a universal constraint is invisible to selection | Lemma 3.3(2) |
| Biased transmission sustains a costly trait at $\mu/c$ within one group | That nothing but anticipation can integrate one group | Lemma 3.10 |
| Zero liability keeps the host above its floor at $H=50$ although (reach) holds | That R1 is necessary at every horizon | Proposition 9.1, R1 |
| A row sum of two with a low initial state converges to no capture | That a full row sum below one is necessary | Proposition 4.9(2); R3b |
| A cap above equal-standing capacity, or below it without inflow not tied to rank, excludes laggards | That a point of enough always preserves standing | Proposition 2.3(2) |
| With per-decision costs the concentration measure is the Herfindahl index | That cultivated influence always tracks the third moment | Proposition 4.5(4) |
| A host normalized to the same peak regeneration regenerates faster above a third of capacity | That such a host is harsher | S3 |
| On a pointwise harsher threshold host the safeguards fail without a margin | That the sufficiency of the safeguards transfers to harsher hosts | Theorem 10.5(1) |
| Comparing after conditioning on the dissolution date fails when dissolution depends on the state | That the earlier proof of the fallback lemma was valid | Lemma 8.2 |
| A unilateral safeguard with negative net cost spreads without coordination | That every safeguard needs a common constraint | Proposition 6.7; crux C9 |
| Six checks with a common blind spot catch only $(1-\rho_{\rm cc})(1-0.1^6)$ | That certified row sums guarantee independent errors | Proposition 6.9 |
| In one common field the uninvadable intensity stays positive for every sharing fraction below one | That sharing reverses selection | Proposition 10.3(2) |
| In the continuous contest intensity is positive for every $\theta<n-1$ | That self-enforcing restraint exists below full inclusion in every game | Remark S5.1 |
| An industry institution after a serious nuclear accident; the Montreal Protocol | That restraint with unchanged motives is always fragile | Section 11.5 |
| Open models trailing closed ones by months; algorithmic efficiency diffusing | That decisive advantage is attainable now | Crux C5; enforced cooperation is at present available, and custody is a preparation |
| Verification faster than breakout | That enforcement fails whenever advantage is decisive | Crux C7 |
| A well-corrected continuation outperforming a fragile cooperative arrangement | That every cooperative arrangement beats regulated competition | Section 8.4 |
| A discounted criterion preferring a race that ends in catastrophe with certainty | That every criterion ranks the paths alike | Section 8.1; crux N1 |
| Mixed beliefs at a horizon of 1,000 periods making racing dominant | That the stag-hunt classification holds at every horizon | Proposition 8.3 |
| A corrector that cannot be understood lowering residual risk to a summable sequence | That correction beyond human understanding must fail | Proposition 6.8; crux N3 |
| After saturation, delegation with risk falling fast enough gives summable realized risk | That homeostasis is a permanent floor | Proposition 6.11(3) |
| Coverage growing in bursts with $\log U=o(t)$ | That sub-exponential coverage always makes a later sprint costlier | Proposition 5.13(4) |
| The host's minimum higher under relative accounting with war than under the isolated self in the frontier toy | That relative accounting is worse for the host at every moment | Remark 5.3 |
| The author's pilot experiment, in which one of four predictions failed | That the mechanism of Section 4 has been shown in experiment | Section 4.6; EV12 |

## S15. Numerics

`checks_v61.py` (pure Python, standard library only, about fifty seconds; log `checks_v61.log`) computes every number marked [num] in the core and this Supplement that V6.1 adds or restates. Each block names the stable keys it checks and its kind. *Independent* blocks decide the outcome by direct computation (value iteration, simulation, numerical best response, numerical Jacobian), never by the inequality under test; *identity* blocks evaluate an algebraic identity or a threshold formula against its own statement and guard only against slips; *derived* blocks compute numbers from formulas other blocks check.

| Block | Kind | Keys | What it computes |
|---|---|---|---|
| FB | independent | `bench` | spectral radius against $ab<d_ud_v$, 200,000 draws |
| LG | independent | `loopgain`, `compound`, `standprice` | numerical Jacobians against $\Gamma$ (4,000 systems); nonlinear deviations; present value of standing; two-period contest against $e(\theta_\Gamma)$ |
| CI | independent | `blind`, `nested` | unequal incidence; evasion; enforcement funded by compliers (tipping share); common liability; a safeguard with negative net cost |
| TC | identity | `twochan` | the accounting identity and its consequences |
| TH | identity | `twochan` | identifying $\theta$ with $\psi=1$ |
| SM | independent | `enough`, `wingives`, `club`, `twochan`, `fallback`, `faithful`, `delegatelock`, `topology`, `compound` | renege denominators; blocs; identification with $\psi<1$; coupled paths; cost exponents; one-or-both delegation; correlated errors; satiation; caps; growth variant |
| CB | independent | `club` | club against system intensity |
| PR | independent | `onegroup` | Price decomposition under five partitions; biased transmission; reversible and irreversible failure |
| CS | independent | `influence`, `corrrate` | size threshold, concentration, splitting factor, rate law for three elasticities, split delay, fixed cost |
| FA | independent | `require` | an invariant rectangle with row sum two |
| DW | independent | `pausefield` | dwell times, two phases, frozen-share thresholds |
| AC | independent | `alarm` | autocorrelation under static masking and under a filter with memory |
| RH | independent | `racehazard` | race hazard against best responses |
| FS | independent | `frontier` | the frontier toy |
| EC | independent | `enforce` | the enforcement condition against value iteration on 200,000 settings; the old bound by sign of $D-C$; breakouts during punishment |
| CR | independent | `relpunish` | mixed imitation ($n=2$); same-strategy punishers ($n\ge3$); the role-differentiated counterexample |
| BI | identity | `zonesillus` | the binary illustration at $D=C$ |
| WG | independent | `wingives` | what a decisive winner gives |
| TK | independent | `talk` | two-party zero-sum talk |
| T3 | independent | `talk` | talk among three or more |
| HO | independent | `safeguards`, `require` | the logistic transient; the margin on a threshold host; R1 at a finite horizon |
| SH | independent | `share` | pooling; sharing in one field; uninvadable intensity |
| PE | independent | `enough` | frozen capability against compounding |
| FD | independent | `fallback` | the fallback example |
| NB | derived | `standprice`, `enforce`, `zonesillus` | the $\theta_\Gamma$ table; the reduced-form scissors; $\bar p_d$ and its monotonicity; time to decisiveness |

Results carried unchanged from earlier versions keep their suites, which `python3 checks_v61.py --legacy` re-runs: `../v5/checks_v5.py` (blocks DL, OV, HO, SR, K7, N13, MM, CAP and others), `../v4/checks_v4.py`, `checks_v42.py` (derivative action), `checks_v44.py` (Branch II bargaining), `checks_v45.py` (common frontier, lead under diffusion), and `../v3/checks_v31.py`. Not yet computed: the joint simulation of capacity and the field (TESTS, Study 2), and the effect of an alternative lineage on dwell times. No suite certifies every proof, and none supplies evidence about the world.

## References

Marks: ‡ works whose existence and identifier were checked on 3 October 2026; † works not yet independently verified; unmarked works carried from the verified bibliography of v3.1. Sources of observations are listed with dates and links in EVIDENCE.md.

- Acemoglu, D., Egorov, G. and Sonin, K. 2012. Dynamics and stability of constitutions, coalitions, and clubs. *American Economic Review* 102(4). ‡ (abstract)
- Alger, I. and Weibull, J. W. 2013. Homo moralis: preference evolution under incomplete information and assortative matching. *Econometrica* 81(6).
- Alger, I., Weibull, J. W. and Lehmann, L. 2020. Evolution of preferences in structured populations. *Journal of Economic Theory* 185:104951. †
- Aumann, R. 1990. Nash equilibria are not self-enforcing. In Gabszewicz, J., Richard, J.-F. and Wolsey, L. (eds), *Economic Decision-Making*. †
- Barrett, S. 2013. Climate treaties and approaching catastrophes. *Journal of Environmental Economics and Management* 66(2).
- Barrett, S. and Dannenberg, A. 2012. Climate negotiations under scientific uncertainty. *PNAS* 109(43).
- Baye, M., Kovenock, D. and de Vries, C. 1996. The all-pay auction with complete information. *Economic Theory* 8(2). †
- Bloom, N., Jones, C. I., Van Reenen, J. and Webb, M. 2020. Are ideas getting harder to find? *American Economic Review* 110(4). †
- Bombardini, M. 2008. Firm heterogeneity and lobby participation. *Journal of International Economics* 75(2).
- Bueno de Mesquita, E., Dziuda, W. and Polborn, M. 2026. The AGI race and existential risk. NBER Working Paper 35276. ‡
- Carlsson, H. and van Damme, E. 1993. Global games and equilibrium selection. *Econometrica* 61(5). †
- Clymer, J., Gabrieli, N., Krueger, D. and Larsen, T. 2024. Safety cases: how to justify the safety of advanced AI systems. arXiv:2403.10462. †
- Coe, A. and Vaynman, J. 2020. Why arms control is so rare. *American Political Science Review* 114(2). †
- Debs, A. and Monteiro, N. 2014. Known unknowns: power shifts, uncertainty, and war. *International Organization* 68(1). †
- Dekel, E., Ely, J. and Yilankaya, O. 2007. Evolution of preferences. *Review of Economic Studies* 74(3). †
- Dixit, A. 1987. Strategic behavior in contests. *American Economic Review* 77(5). †
- Duersch, P., Oechssler, J. and Schipper, B. C. 2012. Unbeatable imitation. *Games and Economic Behavior* 76(1). ‡
- Ewerhart, C. 2015. Mixed equilibria in Tullock contests. *Economic Theory* 60(1). †
- Fearon, J. 1995. Rationalist explanations for war. *International Organization* 49(3). †
- Fershtman, C. and Judd, K. 1987. Equilibrium incentives in oligopoly. *American Economic Review* 77(5). †
- Gilboa, I. and Schmeidler, D. 1989. Maxmin expected utility with non-unique prior. *Journal of Mathematical Economics* 18(2). †
- Green, E. and Porter, R. 1984. Noncooperative collusion under imperfect price information. *Econometrica* 52(1).
- Greenblatt, R., Shlegeris, B., Sachan, K. and Roger, F. 2024. AI control: improving safety despite intentional subversion. *ICML*. ‡
- Güth, W. and Yaari, M. 1992. Explaining reciprocal behavior in simple strategic games: an evolutionary approach. †
- Hayes, N. 1950. Roots of the transcendental equation associated with a certain difference-differential equation. *Journal of the London Mathematical Society* 25. †
- Heifetz, A., Shannon, C. and Spiegel, Y. 2007. What to maximize if you must. *Journal of Economic Theory* 133(1). †
- Hillman, A. and Riley, J. 1989. Politically contestable rents and transfers. *Economics and Politics* 1(1). †
- Hirsch, M. 1985. Systems of differential equations that are competitive or cooperative II. *SIAM Journal on Mathematical Analysis* 16(3).
- Hirshleifer, J. 1991. The paradox of power. *Economics and Politics* 3(3). †
- Jones, C. I. 1995. R&D-based models of economic growth. *Journal of Political Economy* 103(4). †
- Jones, C. I. 2024. The AI dilemma: growth versus existential risk. *American Economic Review: Insights* 6(4). ‡
- Kandori, M., Mailath, G. and Rob, R. 1993. Learning, mutation, and long run equilibria in games. *Econometrica* 61(1). †
- Kempe, D., Kleinberg, J. and Tardos, É. 2003. Maximizing the spread of influence through a social network. *KDD*.
- Krakauer, D., Page, K. and Erwin, D. 2009. Diversity, dilemmas, and monopolies of niche construction. *American Naturalist* 173(1). ‡ (full text)
- Mearsheimer, J. 2001. *The Tragedy of Great Power Politics*. †
- Morris, S. 2000. Contagion. *Review of Economic Studies* 67(1).
- Ok, E. and Vega-Redondo, F. 2001. On the evolution of individualistic preferences. *Journal of Economic Theory* 97(2). †
- Panchanathan, K. and Boyd, R. 2004. Indirect reciprocity can stabilize cooperation without the second-order free rider problem. *Nature* 432.
- Peltzman, S. 1975. The effects of automobile safety regulation. *Journal of Political Economy* 83(4).
- Posen, B. 1991. *Inadvertent Escalation*. †
- Powell, R. 2006. War as a commitment problem. *International Organization* 60(1). †
- Price, G. 1970. Selection and covariance. *Nature* 227.
- Pérez-Castrillo, D. and Verdier, T. 1992. A general analysis of rent-seeking games. *Public Choice* 73(3). †
- Schaffer, M. 1988. Evolutionarily stable strategies for a finite population and a variable contest size. *Journal of Theoretical Biology* 132(4).
- Scharre, P. 2018. *Army of None*. †
- Schelling, T. 1960. *The Strategy of Conflict*; 1966. *Arms and Influence*. †
- Schelling, T. 1966. *Arms and Influence*. Yale University Press. †
- Sigmund, K. et al. 2010. Social learning promotes institutions for governing the commons. *Nature* 466.
- Skaperdas, S. 1992. Cooperation, conflict, and power in the absence of property rights. *American Economic Review* 82(4). †
- Smith, H. 1995. *Monotone Dynamical Systems*.
- Stafford, E., Trager, R. and Dafoe, A. 2022. Safety not guaranteed: international strategic dynamics of risky technology races. Working paper. ‡
- Van Evera, S. 1999. *Causes of War*. †
- Wilde, G. 1982. The theory of risk homeostasis. *Risk Analysis* 2(4). †
- Young, H. P. 1993. The evolution of conventions. *Econometrica* 61(1). †
