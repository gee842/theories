# D2. Mathematical repairs for V6.2 (Opus)

*4 October 2026. One of two independent memos (Fable, Opus) on the same prompt; written without seeing the other. Inputs: SYNTHESIS-v6.1 §二, §四A–B and §H; the two math reviews, the two adversarial reviews (F1, I1–I2), the systems review (I1–I4, m2), the alignment review's minor items on §6, and Codex's review with `counterexamples_v61_codex.py`; the V6.1 statements in THEORY and proofs in SUPPLEMENT; the reviewers' scripts. Everything below was re-derived; nothing is taken from the draft or the reviews on trust, and where a reviewer is wrong or incomplete §22 says so with the derivation.*

*Scripts: `planning/math-opus/m01`–`m10`, pure Python, standard library, each with its `.log` beside it. Run any of them with `python3 mNN_*.py`. `m01` takes about four minutes; each of the others takes under a minute. No file outside `planning/` was edited.*

*Model-family note: I am the drafting model's family. The parts most exposed to shared bias, and most in need of Codex's eyes, are listed in §24.*

---

## 0. What changes, in one page

The repairs do not retract the argument. Four of them make it tighter and more unified than V6.1 was.

**1. Two loop gains price standing, not one.** The relative loop gain $\Gamma_\delta$ of Proposition 2.2 prices a unit of relative payoff. When the stakes grow with total capacity, a second loop gain, the *common* gain $\Gamma^{\rm c}_\delta=\sum_j\delta\kappa_jg_j/(1-\delta(1-d_j))$, prices a unit that all share ($g_j=\partial\Omega/\partial S^j$). The working self-model is set by the ratio of the two closed-loop factors:
$$\frac{1+\theta}{n-1-\theta}=\frac{1+\theta_0}{n-1-\theta_0}\cdot\frac{1-\Gamma_\delta}{1-\Gamma^{\rm c}_\delta}.$$
- With a fixed prize, $\Gamma^{\rm c}_\delta=0$ and this is V6.1's (9).
- The objective narrows iff $\Gamma_\delta>\Gamma^{\rm c}_\delta$, that is, iff reinvestment's relative return exceeds its common return.
- With stakes proportional to capacity and no diffusion, $\Gamma_\delta/\Gamma^{\rm c}_\delta=(1-\beta)r$. **Compounding then narrows the working objective exactly where winnings compound** (Proposition 2.3(1), growth form).

One inequality, relative return against common return, now runs through compounding (2.3), the working objective (3.9), talk (5.15) and the scissors (§5.5). That is the unification the prompt asks for (m02, m10).

**2. The domain is $\Gamma_\delta<1$, and beyond it the price is infinite, not negative.** At $\Gamma_\delta\ge1$ the value of standing has a cusp at equal standing: an advantage $\varepsilon$ is worth order $\varepsilon^{a}$ with $a=\ln(1/\delta)/\ln\Lambda^\ast<1$, where $\Lambda^\ast$ is the growth factor of a relative deviation. The marginal price diverges. The limit from below, $\theta\to-1$ as $\Gamma_\delta\to1^-$, is therefore the right reading of "where the loop gain is high" (m02 D).

**3. Rivals who respond: the form survives, the number does not.**
- *Theorem.* In any symmetric Markov equilibrium that is differentiable at equal standing, Proposition 2.2 holds verbatim with an equilibrium decisiveness $r^{\rm eq}_j$ for stability, and with $r^{\rm pr}_j$ (own intensity held, rivals at their equilibrium policies) for the price. In a static Tullock contest $r^{\rm pr}/r=2(n-1)/n$ exactly.
- *Computation* (m01). Three regimes appear:
  - A *smooth* equilibrium in which the theorem's price is confirmed to within 0.5%, with small corrections (5–12% at structural $\Gamma\le0.3$).
  - Above a structural gain of about 0.45, an *amplified* equilibrium:
    - $r^{\rm eq}\approx2.5$–$5\,r$;
    - equal standing is unstable although $\Gamma<1$;
    - the price is 1.8–3.2 times the structural value.
  - When contests run in many small rounds, a *winner-take-all* equilibrium **coexists** with the smooth one already at $\Gamma=0.2$. Its price is about 9–13 times the structural value.

  The belief that a lead is decisive selects the equilibrium in which it is. This is the formal content of §3.8's "Ψ3 is partly made true".

**4. Correction and provision act channel by channel.**
- Raising the decay/correction rate $d_j$ of a stock lowers the loop gain iff the stock's decisiveness rises with its level faster than the diffusion share: $\xi_{r,j}>\delta_f/(d_j+\delta_f)$, where $\xi_{r,j}=d\ln r_j/d\ln X^j$.
  - Rule support (a level channel, $\xi_r=1$): correction lowers the gain.
  - Capacity (a ratio channel, $\xi_r=0$): faster turnover leaves the gain unchanged without diffusion and raises it with diffusion.
- New, and found by no reviewer: **provision not won lowers the gain only in channels with $\xi_r<1$.** In a linear level channel it has no effect at all, because it adds the same to everyone. Provision is the remedy for compounding through capacity; for the reflexive channel the remedy is $\chi\to0$ and correction.
- The shared-parameter table splits accordingly (§20).

**5. The rate law has a robust half and a strategic half.**
- *Sufficiency holds whatever the speed of adaptation.* $\alpha_{\rm cor}\ge\alpha_{\rm ctl}/(1+\eta)$ suffices under every capacity dynamic that moves monotonically toward its selected level.
- *Necessity holds for carriers that set capacity at its optimum.* Under additive selection any $\alpha_{\rm cor}>0$ eventually certifies, because the gradient's force falls with the return while the optimum runs away.
- *A slow variable raises the threshold.* If correction rests on human capacity that delegation erodes at $\delta_h$, the threshold rises by $w\delta_h$ (verified exactly).
- *Falling floor.* The falling-$f$ clause and the $[H_f]$ rate are corrected, with the initial condition.
- *What enters the paper.* The joint simulation enters as a short [thm; num] proposition (m06).

**6. Enforcement, checked by explicit best response.**
- Condition (14) holds deviation by deviation.
- Part (5) needs at most one breakout per period.
- A new example has $P<v<C$, with a whole window $q\in(0.0354,0.0556)$ in which race reversion fails to deter although it still leaves the deviator below cooperation.
- A best-response value iteration over all deviation plans agrees with (14) in 19,965 of 19,965 random games in which the punishment is credible (m07).

**7. Talk, unified.** Under a common $\theta$ among $n$ actors, a material bias $b_0$ between sender and receiver acts as $b_0(n-1-\theta)/(n-1+\theta)$, and talk is informative iff that is below 1/4.
- At $n=2$, $\theta=-1$ the bias is infinite: no informative talk (5.15(1)).
- At $\theta=-1$, $n\ge3$ it is $b_0n/(n-2)$ (5.15(2)).
- In between, narrowing the self-model drains talk continuously (m09).

The talk column of the shared-parameter table becomes a result, not an interface.

The remaining items are statements whose premises were lost in compression and are restored here, and corrected numbers.

---

## 1. `loopgain`, Proposition 2.2

### (a) V6.2 core statement

**Proposition 2.2 (One loop gain) [thm].** The conditions multiply into a single loop gain. Equal standing breaks when the gain exceeds one, and its discounted form prices standing while below one.

*Model.* As V6.1, equations (1) and (2), unchanged.

1. *Equal standing is locally asymptotically stable if $\Gamma<1$ and unstable if $\Gamma>1$. The channels add, because every stock is fed by the same winnings: compounding through capacity and the reflexive closure through rule support are terms of one sum, and channels each too weak to open the loop can open it together.*
2. *$\Gamma=0$ if any condition is removed: all of the prize divided equally ($\beta=1$), nothing convertible ($\kappa_j=0$ for all $j$), or no decisiveness ($r_j=0$ for all $j$).*
3. *(The price of standing.) Hold the prize and the others' conduct fixed, and let an actor discount at $\delta$ and convert relative net payoff into stocks at the rates $\kappa_j$. If $0\le\Gamma_\delta<1$, a unit of relative net payoff today is worth, to first order, $\Gamma_\delta/(1-\Gamma_\delta)$ units of the actor's own future winnings. Here*
   $$\Gamma_\delta=(1-\beta)\sum_jr_j\omega_j\frac{\delta d_j}{1-\delta(1-d_j-\delta_{f,j})}<\Gamma .$$
   *The price grows without bound as $\Gamma_\delta\to1^-$. At $\Gamma_\delta\ge1$ no first-order price exists: the value of standing has infinite slope at equal standing.*
4. *(Rivals who respond.) Suppose strength also depends on a chosen intensity, and carriers follow a symmetric Markov equilibrium that is differentiable at equal standing and in which a carrier's equilibrium win share rises with its own stocks. Then (1)–(2) hold for the equilibrium path with $r_j$ replaced by the equilibrium decisiveness $r^{\rm eq}_j$: the response of the equilibrium win share to a relative shift of standing in stock $j$, all intensities responding. And (3) holds with $r^{\rm pr}_j$: the same response with the actor's own intensity held at its current level, plus the change in shared loss from the rivals' intensities.*

*Scope.*
- Local, at equal standing. Reinforcing channels: a countervailing channel cannot be subtracted, and with delay it can produce growing oscillation even when the net gain is below one (Remark S2.2). The prize is fixed; Proposition 3.9 lets it grow.
- The structural $\Gamma$ is a benchmark. In contests with effort, leaders press and laggards are discouraged, so $r^{\rm eq}>r$. Computed equilibria range from near the benchmark to several times it. When contests run in many small rounds, a winner-take-all equilibrium can coexist with the smooth one [num, S2]. So a structural $\Gamma<1$ does not by itself ensure stability.
- What $\Gamma$ does not decide is as V6.1 states.

*Proof:* S2.

Three wording changes elsewhere follow from this statement:
- The §2 "Why" box: "the same number prices standing for every actor" becomes "the same gain, discounted, prices standing against what all share (Proposition 3.9)".
- §1.2(1) and the Chinese guide (导读): "decides whether leads compound and prices standing for every actor" becomes "sets whether leads compound and, against the common return, what standing is worth".
- "Every forward-looking actor" is deleted everywhere.

### (b) Proofs

**(1)–(2).** As V6.1 (secular equation, Perron–Frobenius, Sherman–Morrison). No change.

**(3), domain and cusp.**
- Let $\Lambda^\ast$ be the Perron root of $\mathcal J=\mathcal D+\frac1n\mathbf u\mathbf v^\top$. In the single-channel case $\Lambda^\ast=1+(d+\delta_f)(\Gamma-1)$.
- Applying the secular argument to $\delta\mathcal J$ gives $\delta\Lambda^\ast<1\iff\Gamma_\delta<1$.
- Write the nonlinear relative deviation along the Perron direction as $y_{t+1}=f(y_t)$, with $f(0)=0$ and $f'(0)=\Lambda^\ast$. Own extra winnings are $w(y)$, with $w'(0)>0$, and the present value is $PV(\varepsilon)=\sum_{t\ge1}\delta^tw(y_t)$.

*Case $\delta\Lambda^\ast<1$.*
- Fix $\Lambda'$ with $\Lambda^\ast<\Lambda'<1/\delta$. While $|y_t|\le\eta$, we have $|y_t|\le C\Lambda'^t\varepsilon$ and the linearization error is $O(y_t^2)$.
- After $T=\ln(\eta/\varepsilon)/\ln\Lambda'$ periods, the tail is at most $\delta^T\sup|w|/(1-\delta)=O(\varepsilon^{\ln(1/\delta)/\ln\Lambda'})=o(\varepsilon)$.
- So $PV(\varepsilon)/\varepsilon\to\Gamma_\delta/(1-\Gamma_\delta)$, which is V6.1's Sherman–Morrison value.
- When $\Lambda^\ast>1$ (that is, $\Gamma>1>\Gamma_\delta$) the convergence is slow, of order $\varepsilon^{-\ln(\delta\Lambda^\ast)/\ln\Lambda^\ast}$.

*Case $\delta\Lambda^\ast>1$.*
- Choose $\Lambda''<\Lambda^\ast$ with $\delta\Lambda''>1$. For $t\le T$ we have $y_t\ge c\Lambda''^t\varepsilon$, so $PV(\varepsilon)\ge c'\sum_{t\le T}(\delta\Lambda'')^t\varepsilon\ge c''\eta\,\delta^T$.
- With $T=\ln(\eta/\varepsilon)/\ln\Lambda''$ this gives $PV(\varepsilon)\ge c'''\varepsilon^{\ln(1/\delta)/\ln\Lambda''}$, and the exponent is below one. So $PV(\varepsilon)/\varepsilon\to\infty$.

*Case $\delta\Lambda^\ast=1$.* The same bound gives $PV(\varepsilon)/\varepsilon\ge c\ln(1/\varepsilon)$. $\square$

**(4).**
- *Rank one.* In a symmetric (exchangeable) Markov equilibrium, $p_i^{\rm eq}(X)=P(X_i;\{X_k\}_{k\ne i})$ is symmetric in the others' stocks. Linearize at equal standing: $dp_i=\sum_ja_j\,dX_i^j+\sum_jb_j\sum_{k\ne i}dX_k^j$. Since $\sum_ip_i\equiv1$, perturbing one carrier's stock $j$ alone gives $a_j+(n-1)b_j=0$. Hence $dp_i=\sum_ja_j\frac n{n-1}(dX_i^j-\overline{dX^j})$.
- *Same dynamics.* So the deviation dynamics have exactly the form $\mathcal D+\frac1n\mathbf u\mathbf v^{\rm eq\top}$, with $v^{\rm eq}_j=a_jn^2/(n-1)$ and $r^{\rm eq}_j=v^{\rm eq}_jX^{j\ast}$. Mean deviations still decay at $1-d_j$, because $\sum p\equiv1$. With $v^{\rm eq}\ge0$ the Perron argument of (1) applies unchanged. If some $v^{\rm eq}_j<0$ (catch-up stronger than the structural advantage) the sign pattern breaks and $\Gamma^{\rm eq}$ alone does not decide.
- *Price.* For the price, apply the envelope theorem to $V_i$, which is differentiable at equal standing by premise. Own intensity is optimal, so its response drops out at first order. The derivative of $V_i$ follows the state with the actor's own intensities held as numbers and the rivals' at their Markov policies.
- *The relative shift stays relative.* A relative shift (own stocks $+\varepsilon$, the others' $-\varepsilon/(n-1)$ each) leaves totals unchanged, since $\sum p\equiv1$ holds whatever $i$ does. It therefore stays a relative shift, with $dp_i=(r^{\rm pr}_j/(nX^{j\ast}))\,y^j$.
- *Conclusion.* The present value is the Sherman–Morrison expression of (3) with $\mathbf v^{\rm pr}$, plus $-\ell\sum_{k\ne i}\partial e_k/\partial X_i$ per period when intensities carry a shared loss. $\square$

### (c) Tags

- (1)–(4): [thm].
- The magnitudes in the Scope: [num].
- "The channels add": [thm], with its premise (one source of winnings) now stated.

### (d) Checks

**m01 (independent).** A two-actor Tullock lottery with effort, each round's win converted into capacity; symmetric Markov-perfect equilibrium (MPE) by value iteration; global best-response gap at parity $\le10^{-16}$.

| Structural $\Gamma$ ($\Gamma_\delta=\Gamma/2$) | MPE price | Envelope formula with measured $r^{\rm pr}$ | Structural price | $r^{\rm eq}/r$ |
|---|---|---|---|---|
| 0.2 | 0.1164 | 0.1166 | 0.1111 | 1.09 |
| 0.3 | 0.1941 | 0.1950 | 0.1765 | 1.18 |
| 0.4 | 0.3099 | 0.3170 | 0.2500 | 1.41 |
| 0.45 | 0.513 | 0.643 | 0.290 | 2.48 ($\Gamma^{\rm eq}=1.11$) |
| 0.6 | 1.142 | 6.14, not applicable | 0.429 | 4.72 |
| 0.8 | 1.861 | — | 0.667 | 5.09 |

- *Shared loss* ($\ell=0.5$, $\Gamma=0.3$): 0.2201 against 0.2221, with the rivals' shared-loss term included.
- *Static n-player Tullock:* $r^{\rm pr}/r=1.000$, 1.333, 1.500, 1.667 and 1.800 for $n=2,3,4,6,10$, equal to $2(n-1)/n$ in every case.
- *Multiplicity (m01 F).* Value iteration from $V=0$ and from a step at parity converge to different fixed points:
  - $\Gamma=0.2$, $d=0.05$: from $V=0$, price 0.1169 (smooth). From the step, price 1.392 at $N=3000$ and 1.410 at $N=6000$ (12.5× and 12.7× the structural value). Both converged to $10^{-11}$.
  - $\Gamma=0.3$, $d=0.05$: 0.1969 and 1.551 (8.8×).
  - At $d=0.1$ the step start returns to the smooth equilibrium. The winner-take-all branch needs fine rounds.
- *Catch-up (m01 E).* A strong concave cost of standing below the top ($L_{\rm sub}=100$) gives $r^{\rm eq}/r=0.993<1$ at $\Gamma=0.3$, and the laggard tries harder. The sign of the strategic correction is not universal.
- *Off parity* ($r=1$, where the structural price is the same at every state): the laggard's price at $s=0.25$ is 57% of the structural value at $\Gamma=0.3$ and 25% at $\Gamma=0.6$. The leader's at $s=0.75$ is 153%.

**m02 (D) (independent), the domain.**
- Codex's case ($\Gamma=2$, $\Gamma_\delta=9/7$): the fitted exponent of $PV(\varepsilon)$ is 0.5628, 0.5758, 0.5776, 0.5778 over $\varepsilon=10^{-2},\dots,10^{-8}$; predicted $\ln(1/0.9)/\ln1.2=0.5779$.
- Inside the domain but above $\Gamma=1$ ($\delta=0.8$, $\Gamma_\delta=0.889$): $PV/\varepsilon$ is 7.163, 7.702, 7.894, 7.962, 7.987 as $\varepsilon\to10^{-12}$, converging to 8.000 at the predicted rate $\varepsilon^{0.224}$.
- At $\delta\Lambda^\ast=1$, $PV/\varepsilon$ grows by 8.42 per two decades: logarithmic.

---

## 2. `tdec`, Remark S2.1 (time to decisiveness)

**V6.2 statement.**
- In the linearized loop a relative gap grows by the Perron root $\Lambda^\ast$ of (S1) per period. With one channel, $\Lambda^\ast=1+(d+\delta_f)(\Gamma-1)$.
- So a gap grows from $\varepsilon_0$ to a decisive level $\bar\Delta$ in about $\ln(\bar\Delta/\varepsilon_0)/\ln\Lambda^\ast$ periods [num: 1%→50% at $\Gamma=3$, $d=0.2$, $\delta_f=0$: 11.6 linear, 13 in the nonlinear model].
- **$\Gamma$ sets the sign of growth, not its speed.** Speed is set by turnover times $(\Gamma-1)$. At the same $\Gamma=1.2$ a fast channel ($d+\delta_f=0.5$) needs 41 periods and a slow one (0.02) needs 980. With several channels $\Lambda^\ast$ is not a function of $\Gamma$: at $\Gamma=1.2$, splitting the turnover as $(0.3,0.02)$ against $(0.1,0.1)$ gives $\Lambda^\ast=1.0088$ against 1.0200.
- With diffusion the nonlinear gap can settle short of decisive: at $\Gamma=1.5$, $d=\delta_f=0.05$, $r=3$, the gap never reaches 50%.
- The link to $p_d$ is $p_d=1-\upsilon(T_{\rm dec})$: the probability that a breakout is not detected and answered within the time it needs to become decisive. This joins $p_d$ to the verification parameter $\upsilon$ of §8.3(g) (Adv-F F7).

**Proof.** Single channel: $y'=(1-d-\delta_f)y+(1-\beta)\kappa\Omega\frac{r}{nX^\ast}y$ and $(1-\beta)\kappa\Omega r/(nX^\ast)=(1-\beta)r\omega d=(d+\delta_f)\Gamma$. V6.1's factor $1+d_K(\Gamma-1)$ omitted $\delta_f$. $\square$

**Tag.** [thm] for the factor; [num] for the times.

**Check.** m03 (C), independent: the simulated factors 1.40000, 1.05000, 1.10000, 1.03000 equal $1+(d+\delta_f)(\Gamma-1)$ exactly. V6.1's formula gives 1.025 and 1.067 where the truth is 1.05 and 1.10.

**Also new: Remark S2.2 (a countervailing channel with delay) [thm; num].** A reinforcing channel ($a_1=0.5$, $1-d_1=0.6$) plus a slow countervailing one ($a_2=-0.05$, $1-d_2=0.95$) has net DC gain 0.25. Its eigenvalues are $1\pm0.1225i$, modulus 1.0075: a growing oscillation with period 51.6 (m03 D). Correction cannot be subtracted from $\Gamma$, and Remark 4.6's "regulatory cycle" can diverge.

---

## 3. `compound`, Proposition 2.3

### (a) V6.2 core statement

**Proposition 2.3 (When winnings compound, and what enough requires) [thm].** *Let capacity $K_i$ receive a share $\kappa_c$ of what $i$ wins, an inflow $k_0$ not won in the contest, depreciation at rate $d_K$ and diffusion at rate $\delta_f$, with $p_i=K_i^r/\sum_jK_j^r$, and let $K^\ast$ and $S^\ast=nK^\ast$ be individual and total capacity at equal standing.*
1. *Equal standing is locally stable if $\kappa_c\Omega((1-\beta)r-1)<nk_0+\delta_fS^\ast$ and unstable if the inequality is reversed. Without provision and diffusion the condition is $(1-\beta)r\gtrless1$, and $\kappa_c$ sets only the level of capacity. With provision, a smaller convertible share stabilizes equal standing.*
2. *A point of enough. If carriers stop reinvesting at a cap $\bar K$ strictly below $K^\ast$, equal standing at the cap is locally stable. At $\bar K=K^\ast$ it can fail: a laggard just below is excluded when $(1-\beta)r\omega(n-1)/n>1+\delta_f(n-1)/(nd_K)$. With the others at the cap, a laggard's net inflow is*
   $$\phi(K)=\kappa_c\Omega\Big[(1-\beta)\frac{K^r}{K^r+(n-1)\bar K^r}+\frac\beta n\Big]+k_0-d_KK+\delta_f\frac{n-1}n(\bar K-K),$$
   *and the laggard returns to the cap from every start iff $\phi>0$ on $(0,\bar K)$. When $r>1$, $\phi(0^+)=\beta\kappa_c\Omega/n+k_0+\delta_f(n-1)\bar K/n$, so recovery needs an inflow not tied to rank: sharing, provision or diffusion. $\beta\kappa_c\Omega/n+k_0\ge d_K\bar K$ suffices. Without any of the three, laggards below a threshold are excluded.*

*Scope.*
- Fixed prize; the growth form is in S2.
- The others stay at the cap when $\bar K\le(\kappa_c\Omega+nk_0)/(nd_K+\delta_f)$, because their own inflow at the cap is then non-negative whatever the laggard does. Above that, the leaders' own losses to diffusion enter.

*Proof:* S2.

The sentence after the proposition changes from "needs inflow not tied to rank, from sharing or provision" to "**needs an inflow not tied to rank: sharing, provision or diffusion.**" Diffusion is the third source, and it supports openness positively: knowledge that flows is part of what makes a point of enough hold.

### (b) Proof of (2)

- *Laggard's diffusion term.* With the others at $\bar K$ and the laggard at $K$, the mean is $\bar X=(K+(n-1)\bar K)/n$. The laggard's diffusion inflow is $-\delta_f(K-\bar X)=\delta_f\frac{n-1}n(\bar K-K)$, which V6.1 dropped.
- *Strict cap.* For $\bar K<K^\ast$, $\phi(\bar K)=\kappa_c\Omega/n+k_0-d_K\bar K>0$, and by continuity $\phi>0$ just below the cap, so the cap is locally stable.
- *Cap at $K^\ast$.* At $\bar K=K^\ast$, $\phi(K^\ast)=0$ and $\phi'(K^\ast)=\kappa_c\Omega(1-\beta)r\frac{n-1}{n^2K^\ast}-d_K-\delta_f\frac{n-1}n$. Using $\kappa_c\Omega/(nK^\ast)=d_K\omega$, this equals $d_K[(1-\beta)r\omega\frac{n-1}n-1]-\delta_f\frac{n-1}n$. If $\phi'>0$, $\phi<0$ just below the cap and the laggard leaves.
- *Global recovery.* The laggard reaches the cap from $K$ iff $\phi>0$ on $(K,\bar K)$, since it is a scalar ODE/map with the others held.
- *Leaders held.* The leader's inflow at the cap is at least $\kappa_c\Omega/n+k_0-d_K\bar K-\delta_f\bar K/n$, because $p_L\ge1/n$ and its diffusion loss is $\delta_f(\bar K-K)/n$. This is non-negative under the Scope bound.
- *Near zero.* At $K\to0$ with $r>1$ the rank term vanishes faster than $K$.
- *Sufficient condition.* $\phi$ is at least the linear function $\beta\kappa_c\Omega/n+k_0+\delta_f\frac{n-1}n(\bar K-K)-d_KK$, which is positive on $(0,\bar K)$ when it is non-negative at $\bar K$. $\square$

Part (1) at equality is a neutral linearization; the V6.1 "iff" is replaced by the two strict statements (Math-F minor 1).

### (c) Tag

[thm].

### (d) Checks

m04, independent:
- *Cap at $K^\ast$.* Codex's case is reproduced: the laggard falls to $2.4\times10^{-32}$.
- *Strict cap.* $0.98K^\ast$ restores the laggard. Over 400 random settings, a strict cap ($0.97K^\ast$) is restored from just below in 400 of 400.
- *Equality.* The exclusion criterion at $\bar K=K^\ast$ predicts the simulated outcome in 400 of 400.
- *Global criterion.* $\phi>0$ agrees with simulation from 1% of the cap in 444 of 446 settings with leaders provably held. In the 2 disagreements the exclusion threshold (0.7% and 0.2% of the cap) lies below the start.
- *Diffusion.* Codex's case: the minimum of $\phi$ is 0.0001 > 0, and $(0.01, 2.5)\to(2.5, 2.5)$.
- *Each of the three inflows suffices.* At $n=5$, $r=1.5$, cap 0.8: with none of the three, laggards at 0.05 and 0.2 are excluded; with $\beta=0.1$, $k_0=0.05$ or $\delta_f=0.15$ alone, all return.

---

## 4. The sign of correction and provision, channel by channel

This item is new as a statement. It replaces the "correction lowers it" clause of the §2 box and splits the $d$ and $k_0$ rows of the shared-parameter table.

### (a) V6.2 statement (core: one sentence in §2 and the §7.1 table; full form as Proposition S2.3)

**Proposition S2.3 (Which levers lower the loop gain) [thm].**
- Let stock $j$ act through strength $h_j(X^j)$, with $r_j=h_j'(X^{j\ast})X^{j\ast}$ and level elasticity $\xi_{r,j}=d\ln r_j/d\ln X^j$ at equal standing. Ratio channels ($h=r\ln X$, as capacity in a Tullock contest) have $\xi_r=0$; linear level channels ($h=aX$, as rule support in the field model) have $\xi_r=1$.
1. *Sharing $\beta$ and diffusion $\delta_{f,j}$ lower $\Gamma$ and $\Gamma_\delta$ in every channel.*
2. *A faster decay or correction rate $d_j$ changes $\Gamma$ with the sign of $\delta_{f,j}/(d_j+\delta_{f,j})-\xi_{r,j}$, and $\Gamma_\delta$ with the sign of $(1-\delta+\delta\delta_{f,j})/(1-\delta+\delta d_j+\delta\delta_{f,j})-\xi_{r,j}$. Correction therefore lowers the gain of level channels. In ratio channels it leaves $\Gamma$ unchanged without diffusion, raises it with diffusion, and always raises $\Gamma_\delta$: a stock that turns over faster is made more of recent winnings.*
3. *Provision not won, $k_{0j}$, lowers the gain through stock $j$ iff $\xi_{r,j}<1$. In a linear level channel it adds the same to everyone and changes nothing.*
4. *The convertible share $\kappa_j$ raises the gain through ratio channels only when $k_{0j}>0$, and through level channels always.*

### (b) Proof

- *Steady state.* $X^\ast=c/d$ with $c=\kappa\Omega/n+k_0$, and $\omega=(\kappa\Omega/n)/(dX^\ast)$, so $r\omega\frac d{d+\delta_f}=\frac{\kappa\Omega}n\cdot\frac{r(X^\ast)}{X^\ast}\cdot\frac1{d+\delta_f}$.
- *(2), correction.* By the chain rule, $dr/dd=(r\xi_r/X^\ast)(-X^\ast/d)=-r\xi_r/d$. Hence $\partial_d[r\,d/(d+\delta_f)]=\frac r{d+\delta_f}\big[\frac{\delta_f}{d+\delta_f}-\xi_r\big]$. The $\Gamma_\delta$ case is the same computation with $\delta d/(1-\delta+\delta d+\delta\delta_f)$.
- *(3), provision.* $k_0$ moves only $X^\ast$, and $\partial_{X^\ast}(r/X^\ast)$ has the sign of $\xi_r-1$.
- *(4), conversion.* For ratio channels, $\omega$ rises with $\kappa$ iff $k_0>0$. For level channels, $r\omega=a\kappa\Omega/(nd)$. $\square$

### (c) Tag

[thm].

### (d) Check

m03 (A, B), independent: the relative-mode growth factor is simulated in the nonlinear model for five channel forms (log, linear, $X^{0.5}$, $X^2$, $\ln(1+X)$), with and without diffusion. Every sign agrees with the rule.
- *Log channel:* $\Gamma=0.8571\to0.9643$ when $d$ rises from 0.2 to 0.3 with $\delta_f=0.1$, and is unchanged without diffusion.
- *Linear channel:* $1.125\to0.750$.
- *$k_0$ from 0.1 to 0.2:* the log channel's gain falls $1.2857\to1.0000$; the linear channel's stays at 1.125; the $X^2$ channel's rises.
- *Ratio channel, $\Gamma_\delta$:* 0.853, 1.157, 1.409 at $d=0.1,0.2,0.4$, with $\Gamma$ unchanged.

### Consequences to carry

1. §2 "Why" box: "Sharing and diffusion lower it in every channel; provision lowers it where decisiveness is a ratio of stocks, as with capacity; correction lowers it where decisiveness rises with a stock's level, as with rule support."
2. The trees sentence of §7.1 ("Provision not won in the contest lowers the loop gain, the drift of working objectives and the breakout probability at once") stays true for capacity, which is where provision is meant to act. Add "through capacity". The reflexive channel is answered by $\chi\to0$ and correction (§10.2 already says this).
3. Test Γ (Codex 2) has the wrong sign. With $J_i=\pi_i+\theta\bar\pi_{-i}$ in the contest of §3.4, the ratio of intensity's response to the shared loss and to private cost is exactly $1+\theta$; m02 (E) confirms this from numerical equilibria to $10^{-4}$. Provision lowers $\Gamma_\delta$ in ratio channels and so *raises* $1+\theta$. Registered form: *"$1+\theta$, measured as the ratio of conduct's response to shared harm and to private cost, should rise with provision not won relative to the stakes, holding declared objectives fixed; a fixed relative preference predicts no such interaction."*

---

## 5. `blind`, Lemma 3.3

### (a) V6.2 statement, part (3)

*3. Evasion. If carriers of type $k$ can evade a constraint costing them $c_k$ against an expected sanction $\bar F_k$, a type's evading variant grows relative to its complying variant iff $c_k>\bar F_k$. Compliance therefore prevails under cumulative payoff-monotone selection if $\bar F_k>c_k$ for every type that can evade, whatever the incidence, which then only re-sorts the compliers. If the sanction falls as evaders spread, because detection is funded by compliers or rule-making is captured by evaders, the outcome depends on its endpoints:*
- *if it starts above the cost at full compliance and falls below it at full evasion, $\bar F(0)>c>\bar F(1)$, compliance and evasion are both stable, separated by a tipping share;*
- *if it never falls below the cost, compliance is globally stable;*
- *if it starts below it, evasion is globally stable.*

Rename $s_k$ to $\bar F_k$: $s$ is speed in S0, and $F$ is the global sanction.

### (b) Proof

- *Within a type.* An evader's payoff exceeds that of a complier of its type by $c_k-\bar F_k$.
- *Prevailing.* If every difference is negative, each evading variant's share relative to its own complying variant tends to zero, so the compliant share tends to one whatever the cross-type payoffs.
- *Not necessary across types.* The converse fails across types: a type whose evasion pays can still be eliminated by another type's compliers if those earn more.
- *Falling sanction.* With $\bar F(x)$ continuous and decreasing in the evading share $x$, $\dot x=x(1-x)(c-\bar F(x))$. A root in $(0,1)$ exists iff $\bar F(0)>c>\bar F(1)$, and it is unstable, which gives bistability. Otherwise $c-\bar F$ has one sign on $(0,1)$. $\square$

### (c) Tag

[thm].

### (d) Check

m05 (A, B), independent:
- *Bistability endpoints.* With $c=0.3$:
  - $\bar F=0.5+0.5(1-x)$: compliance from every start.
  - $0.24(1-x)$: evasion from every start.
  - $0.48(1-x)$ and $1.2(1-x)$: bistable, with tipping shares 0.375 and 0.75.
- *Unequal compliance costs.* With costs 0.1 and 0.2:
  - sanctions 1 and 1: compliance goes to 1, all of it in type A;
  - sanctions 1 and 0.15 ($\bar F_B<c_B$): compliance still goes to 1, because B's evaders lose to A's compliers;
  - sanctions 1 and 0.05: evasion takes over.

---

## 6. `boundary`, Proposition 3.6; Ψ; the divisible/positional split (Adv-O I2)

### (a) V6.2 statements

**Equation (8), rewritten.**
$$W_i=\pi_i+\kappa\,\bar\pi^{\rm e}_{-i}+\kappa_s\,\bar\pi^{\rm s}_{-i}.$$
- $\pi^{\rm e}$ is the *divisible* part of payoffs: rents, services, the material gains of capability.
- $\pi^{\rm s}$ is the *positional* part: standing, the power to set rules, the loss of being subordinated.
- $\kappa\in[0,n-1)$ is coupling through the divisible part that prices do not settle: shared hazards, supply chains, systemic risk.
- $\kappa_s\in[-1,0]$ records that a rival's standing is one's own subordination.
- In the contest, the prize splits the same way: $\Omega=\Omega_e+\Omega_s$.

**Proposition 3.6 (The boundary error of the self-model) [thm].** A self-model narrower than the real coupling raises intensity and lowers its holder's own welfare where the coupling is real; selection favours the narrowest; and compounding makes a narrow *working* objective individually accurate and collectively self-defeating.
1. *For every $\theta\in[-1,n-1)$, the game in objectives has the symmetric equilibrium $e(\theta)$ of V6.1, decreasing in $\theta$. True welfare there rises with $\theta$.*
2. *Against fixed intensities of the others, $i$'s true welfare is maximized by its best response when it weighs others' divisible payoffs by $\kappa$ and their positional payoffs by $\kappa_s$. Acting on $\theta<\kappa$ toward the divisible part lowers welfare whenever it changes the chosen intensity and the maximizer is unique. Toward the positional part, relative concern is accurate. What corrects it is not a wider self-model but keeping positional prizes from forming (Section 10.2).*
3. *Selection on intensities favours what an actor with $\theta=-1$ would choose (V6.1 (3)).*
4. *Under compounding, the accurate working objective is $\theta(\kappa)$ of Proposition 3.9 with $\theta_0=\kappa$, narrower than $\kappa$ wherever the relative return exceeds the common return. It is individually accurate. Every actor acting on it is worse off than if all acted on $\kappa$, by (1): the narrowing is a collective trap, not an individual mistake.*

**§3.8.** "Ψ is locally rational and systemically false" becomes "**Ψ is individually rational under compounding, collectively self-defeating, and false as a doctrine about nature.**"
- The "error" that §3.4 names is the *held* self-model $\theta_0<\kappa$ on the divisible part.
- Compounding's narrowing is accurate arithmetic inside a game that should be changed. This is "judge the game, not the act" in formal form.
- §3 claim box: "where the coupling is real the narrow boundary is an error, and the selected one" becomes "where coupling is real a narrow held boundary is an error and the selected one; compounding then makes a narrow working boundary accurate for each and ruinous for all".

### (b) Proof

- *Splitting the objective.* Write $\pi_i=w_i\Omega_e-ce_i-\ell\mathcal E+w_i\Omega_s$. Then $W_i$, as a function of $e_i$ with the others fixed, is a contest objective with effective prize $\big[\Omega_e(n-1-\kappa)+\Omega_s(n-1-\kappa_s)\big]/(n-1)$ and unit cost $c+(1+\kappa)\ell$.
- *(2).* The welfare-maximizing response is the best response under exactly these weights. Lowering the divisible weight below $\kappa$ raises the marginal value of intensity by $\Omega_e\partial_{e_i}w_i/(n-1)+\ell>0$. On the positional part, $\kappa_s\le0$ makes the positional prize count at least fully.
- *(4).* Proposition 3.9 with $\theta_0=\kappa$ gives the working objective. At the symmetric equilibrium relative standing does not move, so per-period true welfare is $(1+\kappa)\pi(e)$, and (1) applies. $\square$

### (c) Tags

- (1)–(4): [thm].
- "$\kappa_s\le0$" as a description of positional goods: [def].

### (d) Check

None new. Part (4) composes two results that are each checked (m02 B; RH). The split is an algebraic identity.

---

## 7. `standprice`, Proposition 3.9 (general form)

### (a) V6.2 core statement

**Proposition 3.9 (Compounding prices standing) [thm].** Near equal standing, compounding makes a unit of relative payoff worth more than a unit of shared payoff wherever reinvestment's relative return exceeds its common return.

*Setting.*
- The model of Proposition 2.2, but with the prize $\Omega$ allowed to depend on total stocks, with $g_j=\partial\Omega/\partial S^j\ge0$.
- The reference state is a symmetric steady state, or a balanced-growth path when $\Omega$ is proportional to capacity.
- $\Gamma_\delta=(1-\beta)\sum_j\delta\kappa_jr_j(\Omega/S^{j\ast})/(1-\delta(1-d_j-\delta_{f,j}))$, evaluated at the reference state. With a fixed prize at a steady state, $\kappa_j\Omega/S^{j\ast}=\omega_jd_j$ and this is Proposition 2.2's $\Gamma_\delta$. Write
  $$\Gamma^{\rm c}_\delta=\sum_j\frac{\delta\kappa_jg_j}{1-\delta(1-d_j)}$$
  for the common loop gain, with both gains in $[0,1)$.

*Statement.* An actor holding $\theta_0<n-1$, discounting at $\delta$ and converting net payoff at the rates $\kappa_j$, with the others' conduct fixed, acts to first order on the objective of Proposition 3.5 with
$$\frac{1+\theta}{n-1-\theta}=\frac{1+\theta_0}{n-1-\theta_0}\cdot\frac{1-\Gamma_\delta}{1-\Gamma^{\rm c}_\delta}.\tag{9}$$
1. *The working objective narrows iff $\Gamma_\delta>\Gamma^{\rm c}_\delta$. With a fixed prize $\Gamma^{\rm c}_\delta=0$, it always narrows, and $\theta\to-1$ as $\Gamma_\delta\to1^-$ for every $\theta_0<n-1$. Along with $\theta$, the weight of the common channel falls: the visibility of the host, the point of enough, the weight of a rebated levy and the gain from breaking a promise.*
2. *If the stakes are proportional to capacity and there is no diffusion, $\Gamma_\delta/\Gamma^{\rm c}_\delta=(1-\beta)r$: the working objective narrows exactly where winnings compound (Proposition 2.3(1)), and widens where they do not.*
3. *At $\Gamma_\delta\ge1$ the first-order price of standing is infinite (Proposition 2.2(3)).*

*Scope.*
- First order; others' conduct fixed. With rivals responding, $\Gamma_\delta$ is replaced by its equilibrium form (Proposition 2.2(4)). In the computed class this amplifies the narrowing, sometimes by a multiple, and can make it self-fulfilling [num, S2].
- At a stationary total, equal standing can be stable while the objective narrows. With a fixed prize, every positive relative gain narrows it.

*Proof:* S3.

Closed form, for the Supplement: with $\rho=\frac{(1+\theta_0)(1-\Gamma_\delta)}{(n-1-\theta_0)(1-\Gamma^{\rm c}_\delta)}$, $\theta=\frac{\rho(n-1)-1}{1+\rho}$. At $\Gamma^{\rm c}_\delta=0$ this equals V6.1's $\frac{n\theta_0-(n-1)(1+\theta_0)\Gamma_\delta}{n-(1+\theta_0)\Gamma_\delta}$.

The sentence after it, Powell 1991, stays and gains precision: concern for relative gains depends on how far gains convert into future advantage *relative to how far they grow what all share*.

### (b) Proof (S3)

*Decomposition.* Split a payoff change into its common part $\bar\Delta$ and relative part $y=\Delta\pi_i-\bar\Delta$. The two parts evolve separately to first order, because the prize depends on totals and a relative shift leaves totals unchanged.

*Relative part.*
- Own stocks rise by $\kappa_jy$; the others' fall, summing to the same.
- Relative deviations follow $\mathcal D+\frac1n\mathbf u\mathbf v^\top$, with $\frac1nu_jv_j=(1-\beta)\kappa_jr_j\Omega/S^{j\ast}$. At a fixed-prize steady state this is $(1-\beta)r_j\omega_jd_j$, so $\Gamma_\delta$ is unchanged.
- Own future winnings rise by $\lambda_ry$ with $\lambda_r=\Gamma_\delta/(1-\Gamma_\delta)$. Since the prize is unchanged, the others' fall by $\lambda_ry$ in total.

*Common part.*
- Every stock $j$ rises by $\kappa_j\bar\Delta$, so $S^j$ rises by $n\kappa_j\bar\Delta$.
- Common deviations $c^j$ follow $c^{j\prime}=(1-d_j)c^j+\kappa_j\sum_kg_kc^k$, a rank-one Jacobian $\operatorname{diag}(1-d_j)+\boldsymbol\kappa\mathbf g^\top$. Diffusion does not act on common deviations.
- Each actor's winnings rise by $\sum_kg_kc^k_t$ per period. By Sherman–Morrison, the present value is $\lambda_c\bar\Delta$ with $\lambda_c=\Gamma^{\rm c}_\delta/(1-\Gamma^{\rm c}_\delta)$.

*Matching.*
- $\Delta J_i=(1+\theta_0)(1+\lambda_c)\bar\Delta+\frac{n-1-\theta_0}{n-1}(1+\lambda_r)y$.
- Matching to $(1+\theta)\bar\Delta+\frac{n-1-\theta}{n-1}y$, up to a positive factor, and using $1+\lambda=1/(1-\Gamma)$, gives (9).

*Part (2).* $\Omega=gS$, $k_0=\delta_f=0$: $\Gamma_\delta=\delta(1-\beta)r\kappa g/(1-\delta(1-d))$ and $\Gamma^{\rm c}_\delta=\delta\kappa g/(1-\delta(1-d))$. The shares' multiplier is $\frac{1-d+(1-\beta)r\kappa g}{1-d+\kappa g}$, which exceeds one iff $(1-\beta)r>1$. $\square$

### (c) Tag

[thm].

### (d) Checks

**m02 (A), independent: nonlinear simulation of the stock model against the closed forms.** Largest relative error $2.5\times10^{-5}$ inside the domain, over five steady-state and two balanced-growth cases (with sharing, provision and diffusion).

| Case | Relative price, simulated / formula | Common price, simulated / formula |
|---|---|---|
| Fixed prize | 2.213115 / 2.213115 | — |
| Growing prize | 4.764587 / 4.764706 | 0.473684 / 0.473684 |
| Balanced growth, $r=0.8$ | 1.317073 / 1.317073 | 2.454545 / 2.454545 |

The balanced-growth case $r=1.5$ lies outside the domain ($\Gamma_\delta=1.066$): simulated 226, against a "formula" of $-16.2$.

**m02 (B): two-period strategic contest; algebra check, first order by construction at a symmetric point.** The directly computed symmetric equilibrium matches $e(\theta)$ of (9) to 7 digits in six cases, while V6.1's fixed-prize formula is off by up to 15%.
- $g=0.6$, $\Omega_{20}=0$, $r=1$: $\theta=\theta_0$ exactly.
- $r=0.7$: the objective widens ($\theta=0.549>0.5$).
- $r=1.4$: it narrows.

This reproduces Adv-F F1.

**m02 (C), independent: narrowing and share instability coincide.** With proportional stakes and no diffusion they coincide in 24 of 24 cases. With diffusion they part as predicted: at $r=1.17$, $\delta_f=0.03$ the objective narrows while equal shares are stable.

**m10 (B): the narrowing arm of the scissors weakens with the common return.** The largest enforceable $\Gamma_\delta$ at $p_d=0.9$ rises from 0.387 to 0.571 and 0.755 as $\Gamma^{\rm c}_\delta$ goes from 0 to 0.3 and 0.6.

---

## 8. `onegroup`, Lemma 3.10

### (a) V6.2 statement

**Lemma 3.10 (What selection at any level cannot supply) [thm].** A trait whose benefit goes equally to everyone is selected against at every level of grouping.
- *Let a trait cost its bearer and benefit every member of the population equally. Under every partition into groups and every payoff-monotone rule, the total selection term and the within-group term of the Price equation are non-positive.*
- *The between-group term is non-positive when fitness is affine in payoff. Otherwise it can be positive, by Jensen's inequality across groups of unequal variance, but never enough to make the total positive.*
- *The trait can rise only through the transmission term, or through a rule that changes the bearer's relative payoff (V6.1 list).*

### (b) Proof

- Payoffs are $\pi_j=\pi_0+b\bar z-cz_j$, the same decreasing function of $z_j$ for every member, since $b\bar z$ is common.
- A payoff-monotone rule orders growth rates as payoffs, so $w_j=\psi(\pi_j)$ with $\psi$ increasing on the payoffs present.
- Hence $w_j$ is a decreasing function of $z_j$ alone. By Chebyshev's association inequality, $\operatorname{Cov}(w,z)\le0$ in the population and within every group.
- The between-group term is the difference, and is $-c\operatorname{Var}_g(\bar z_g)\le0$ only when $\psi$ is affine. $\square$

### (c) Tag

[thm].

### (d) Check

m05 (C), independent: 3,000 random partitioned populations under each of six monotone transforms (affine, $e^{5\pi}$, $\log$, $\pi^3$, logistic, near-step).
- Total > 0 in 0 of 3,000, for every transform.
- Within-group > 0 in 0 of 3,000, for every transform.
- Between-group > 0: 0 of 3,000 for affine fitness; 3–346 of 3,000 for the nonlinear transforms.
- Reviewers' examples: Opus total −0.364, between +0.017; Codex total −0.115, between +0.0092.

---

## 9. `corrrate`, Proposition 4.5; `costq`, Assumption 4.2; a new Proposition 4.6 (Study 2)

### (a) V6.2 core statements

**Assumption 4.2 (The cost of conversion capacity) [prem].**
- *A carrier with share $p$ pays $\mathrm{Cost}(q;p)=f\,p^{\xi_f}q+\gamma\,p^{\xi_v}q^{1+\eta}/(1+\eta)$, with $\eta>0$, a **per-unit cost floor** $f\ge0$ and size elasticities $\xi_f,\xi_v\in[0,1]$.* The floor is a marginal cost that every unit of capacity pays, such as per-item legal procedure. V6.1's "fixed part" was a misnomer.
- *$[H_\gamma]$: $\gamma(t)=\gamma_0e^{-\alpha_{\rm ctl}t}$. $[H_f]$: $f(t)=f_0e^{-\alpha_ft}$.* Both are stated as hypotheses.
- "Capacity is at its selected level at every date" moves out of the assumption and into Proposition 4.5(2) and the new Proposition 4.6, where it is used.

**Definitions, add to (11)–(12).**
- $\hat Y=p^2\bar y^\top\hat A\bar y$ with $\hat A_{ij}=a_i\hat b_{ij}$: the cultivated return per unit of capacity times $d$.
- $\hat B=p\sum_j\hat b_{{\rm ev},j}\bar y_j$: cultivated conversion into evaluation per unit of capacity.
- So $q^\ast=\big[(\chi\hat Y/d-fp^{\xi_f})/(\gamma p^{\xi_v})\big]_+^{1/\eta}$. Splitting into $k$ parts divides $\hat Y$ by $k^2$.

**Proposition 4.5 (Required independent correction, and its rate) [thm].**
1. *(unchanged)*
2. *(Rate law.) Assume $[H_\gamma]$, no per-unit floor ($f=0$), $d(t)=d_0e^{\alpha_{\rm cor}t}$, a positive cultivation channel and long horizons.*
   - *Sufficient, whatever the speed at which capacity adjusts toward its selected level: if $\alpha_{\rm cor}\ge\alpha_{\rm ctl}/(1+\eta)$ and $d_0>d^\ast(\gamma_0)$, the certificate holds at every date.*
   - *Necessary for carriers that set capacity at its selected level: if $\alpha_{\rm cor}<\alpha_{\rm ctl}/(1+\eta)$, the certificate fails beyond a finite time, after which a seeded evaluation domain is captured.*
   - *Both hold for every size elasticity $\xi_v$.*
3. *(A per-unit floor.) If $f>0$, cultivation stops once $d\ge d_f=\chi\hat Y/(fp^{\xi_f})$, so the requirement levels off at $\max\{A/c_{\rm ev},d_f\}$. Under $[H_f]$, $d_f$ rises at $\alpha_f$, and the certificate holds eventually iff one of the following holds:*
   - *$\alpha_{\rm cor}>\alpha_f$;*
   - *$\alpha_{\rm cor}=\alpha_f$ and nothing is cultivated at the start ($d_0\ge d_f(0)$);*
   - *the rate law of (2) holds.*

   *If correction starts above $d_f$ and grows at least at $\alpha_f$, nothing is cultivated at any date. A lump-sum cost of capacity, by contrast, only delays cultivation: it changes the size threshold to $F^{\eta/(2+2\eta-\xi_v-\eta\xi_f)}$ and leaves the requirement unbounded.*
4. *(unchanged)*

*Scope.* The rate law does not depend on how the cost of influence scales with size; the threshold, the splitting factor and the concentration measure do. Off the selected level see Proposition 4.6.

*Proof:* S4.

**Proposition 4.6 (When capacity lags its optimum) [thm; num].** New key `caplag`. The quasi-static model is the worst case for a falling cost of control, and the best case after a reform and wherever correction rests on a slow variable.
1. *If capacity never rises while above its selected level, the sufficient half of the rate law holds from any start with capacity at or below that level. Examples: any first-order lag, or gradient selection.*
2. *Two dynamics behave differently:*
   - *With adjustment at a constant proportional rate $\kappa_q$, failure is delayed by about $\eta\ln(1+g/\kappa_q)/(\alpha_{\rm ctl}-(1+\eta)\alpha_{\rm cor})$, with $g=(\alpha_{\rm ctl}-\alpha_{\rm cor})/\eta$, but not prevented.*
   - *With selection whose speed falls as control cheapens, such as additive-variance gradient selection, $q(t)\le q(0)+V\chi\hat Y/(d_0\alpha_{\rm cor})$, so any $\alpha_{\rm cor}>0$ eventually certifies.*

   *The necessary half of the rate law is therefore a result about optimizing carriers.*
3. *If correction rests on human capacity that delegation erodes, $d_{\rm eff}=d(\mathcal M/\mathcal M_0)^w$ with $\dot{\mathcal M}=-\delta_h\mathcal M$, the required rate rises to $\alpha_{\rm ctl}/(1+\eta)+w\delta_h$.*
4. *After a reform that temporarily raises $d$ in a self-sustaining captured domain, a capacity stock that adjusts slowly lengthens the hold needed to undo capture [num: +17% at $\kappa_q=0.1$, +54% at $\kappa_q=0.03$].*

*Scope.* A joint simulation of capacity and the field model in one evaluation domain. Four independent implementations agree in direction: the systems review (s4, s5), Math-Opus (s4), Math-Fable (m5) and m06 here. The hysteresis of correction, masking and delegation reported by the systems review is a further [num] (S4).

*Proof:* S4.

**R3a**, in Proposition 9.1:
- Kind: "necessary for carriers that set capacity at its selected level; sufficient whatever the adjustment".
- Not needed when: "$\chi=0$ or channels removed; a per-unit cost floor AI does not lower; nothing captured; horizon shorter than the failure time; capacity adjusting more slowly than its optimum drifts (finite horizons)".
- Add: "with a slow variable under correction, the rate rises by $w\delta_h$".
- §4.3's durable remedies: "a fixed cost of control AI does not lower" becomes "**a per-unit cost of capacity AI does not lower**". A lump-sum cost is not durable.

**TESTS, Study 2.** The predicted failure signature reverses. Slow adaptation of capacity lets the certificate hold *below* the rate law. "Correction growing slightly faster than the rate law still fails" is produced by a slow variable that erodes correction itself, not by capacity lag. Test the adjustment speed of capacity directly.

### (b) Proofs

- *Optimum and certificate.* $q^\ast$ is the root of $\chi\hat Y/d-fp^{\xi_f}-\gamma p^{\xi_v}q^\eta=0$, or zero. Then $G_{\rm ev}=(A+a_{\rm ev}\hat Bq)/(c_{\rm ev}d)$.

- *(2), sufficient.*
  - Under the stated dynamics, $q(t)\le\max\{q(0),\sup_{s\le t}q^\ast(s)\}$.
  - So $G(t)\le\max\{G(0)d_0/d(t),\sup_{s\le t}G^{\rm QS}(s)d(s)/d(t)\}\le\max\{G(0),\sup_sG^{\rm QS}(s)\}$, since $d$ is nondecreasing.
  - $G^{\rm QS}(t)=\frac A{c_{\rm ev}d}+Z_\eta(\gamma p^{\xi_v})^{-1/\eta}d^{-(1+\eta)/\eta}$ is nonincreasing when $\alpha_{\rm cor}\ge\alpha_{\rm ctl}/(1+\eta)$.
  - $G(0)\le G^{\rm QS}(0)<1$ by the start conditions.
- *(2), necessary.* As V6.1, under quasi-statics.

- *(3).*
  - $q^\ast=0$ iff $d\ge d_f$, and $d_f\propto1/f$ rises at $\alpha_f$ under $[H_f]$; V6.1's S4 said "falls".
  - If $\alpha_{\rm cor}>\alpha_f$, $d/d_f\to\infty$ and cultivation stops in finite time. Then $G=A/(c_{\rm ev}d)\to0$.
  - If $\alpha_{\rm cor}=\alpha_f$, $d/d_f$ is constant. With $d_0<d_f(0)$, $q^\ast=[(\chi\hat Y/d)(1-d_0/d_f(0))/(\gamma p^{\xi_v})]^{1/\eta}$, which grows as in the $f=0$ case. So the certificate fails if $\alpha_{\rm cor}<\alpha_{\rm ctl}/(1+\eta)$.
  - If $\alpha_{\rm cor}<\alpha_f$, $d/d_f\to0$ and the $f=0$ asymptotics apply.
  - *Lump sum.* Cultivation pays iff $\frac\eta{1+\eta}(\chi\hat Y/d)^{(1+\eta)/\eta}(\gamma p^{\xi_v})^{-1/\eta}>Fp^{\xi_f}$. With $\hat Y\propto p^2$, solving for $p$ gives the threshold exponent. Once cultivation pays, $q^\ast$ is the $f=0$ level, so the requirement grows as $\gamma\to0$.

- *Proposition 4.6.*
  - (1) is the sufficiency argument above.
  - (2), lag: $q=q^\ast\kappa_q/(\kappa_q+g)$ on the asymptotic path, which shifts the exponential by $\ln(1+g/\kappa_q)$ at rate $(\alpha_{\rm ctl}-(1+\eta)\alpha_{\rm cor})/\eta$.
  - (2), additive selection: $\dot q=V(\chi\hat Y/d-\gamma p^{\xi_v}q^\eta)\le V\chi\hat Y/d(t)$; integrate. Then $G\le(A+a_{\rm ev}\hat Bq_{\max})/(c_{\rm ev}d)\to0$.
  - (3): $d_{\rm eff}$ grows at $\alpha_{\rm cor}-w\delta_h$; apply (2).
  - (4) is numerical. $\square$

### (c) Tags

- Assumption 4.2: [prem].
- Proposition 4.5: [thm].
- Proposition 4.6: (1)–(3) [thm]; (4) and the hysteresis [num].
- R3a: as above.

### (d) Checks

m06, independent. One evaluation domain, $\dot x=\zeta x(1-x)(az-c)$, $\dot z=\varepsilon(A+\hat Bq-dz)$, with exact exponential steps for the stiff parts.

- **(A) Falling floor.** Codex's counterexample is reproduced: cultivation stops at $t=0.50507$ and the certificate never fails, at $\alpha_{\rm cor}=0.05<0.1$.
- **(B) Corrected $[H_f]$ rule.** It predicts the eventual certificate in 32 of 32 cases ($\alpha_f\in\{0.02,0.05\}$, eight values of $\alpha_{\rm cor}$, with and without initial cultivation). Opus's case $\alpha_{\rm cor}=\alpha_f$ with initial cultivation fails at $t=15.4$; without initial cultivation it never fails.
- **(C) Lump-sum cost.**
  - The threshold exponents computed by bisection on $p$ are 0.2500, 0.3333, 0.4000 and 0.2273, against $\eta/(2+2\eta-\xi_v-\eta\xi_f)$ exactly in four settings. The per-unit floor gives $1/(2-\xi_f)$.
  - As $\gamma$ falls from $10^{-2}$ to $10^{-8}$, $d^\ast$ is 10, 100, 1000 and 10000 under a lump sum, against 3.03, 3.33, 3.33 and 3.33 under a per-unit floor.
- **(D) The joint table.** The rate law is 0.1. Each entry is certificate failure / capture ($x>\tfrac12$):

| $\alpha_{\rm cor}$ | Quasi-static | Lag $\kappa_q=0.1$ | Lag $\kappa_q=0.03$ | Additive, $V=1$ | Multiplicative, $V=1$ |
|---|---|---|---|---|---|
| 0.05 | 13.0 / 25.4 | 22.5 / 36.9 | 31.3 / 47.5 | never / never | 23.8 / 58.9 |
| 0.09 | 69.3 / 118.8 | 106.4 / 169.9 | 146.3 / 221.7 | never | never |
| 0.10, 0.12 | never | never | never | never | never |

  - *Lag delay:* 9.42 simulated against 9.16 by formula, 18.23 against 17.92, 6.33 against 6.44.
  - *Additive selection at $\alpha_{\rm cor}=0.01$:* the certificate fails transiently at $t=10.6$, then recovers; the final $G$ is $5\times10^{-8}$.
  - *Human capacity:* the threshold is exactly 0.15 and 0.20 at $\delta_h=0.05$ and $0.1$.
  - *Capture lags certificate failure* by 12–75 periods. This is the "two clocks" of Theorem 4.12.
- **(E) Reversal.** Hold needed to undo capture: 38.05 quasi-static, 44.34 with lag 0.1, 58.67 with lag 0.03.

---

## 10. `slowroute`, Theorem 4.12

### (a) V6.2 core statement

**Theorem 4.12 (Silent crossing when capture precedes evidence) [thm∣prem].** *Assume (reach) and:*
- *(a) replicator selection among carriers differing only in load, with a race carrier present and cumulative advantage unbounded on every alarm-free continuation;*
- *(d) a fixed averaged alarm with $0\le m_{\rm out}<m_{\rm fl}<m_{\rm in}<1$;*
- *(e) capture before evidence: $x_{\rm ev}(t)>(m_{\rm fl}-m_{\rm out})/(m_{\rm in}-m_{\rm out})$ whenever $V_{\min}\le V(t)\le V_{\rm alarm}$.*

*Then the host crosses its floor before any alarm. If $m_{\rm in}\le m_{\rm fl}$, the alarm is delayed, not silenced.*

*Scope.*
- (e) carries the conclusion. What makes it likely is the rate law: if the cost of control falls faster than correction can follow, evaluation is captured in finite time (Propositions 4.5(2), 4.6). In the joint simulation capture follows the certificate's failure by 12–75 periods [num].
- Whether that happens before the host reaches its alarm level is a comparison of two clocks, and a slower adjustment of capacity can reverse it (S4).
- V6.1's conditions (b) and (c) become this mechanism sentence. They are not premises of the theorem.
- Earlier labels are kept as aliases.

The V6.1 sentence "If instead $m_{\rm in}\le m_{\rm fl}$… escapes re-absorption" goes to the Scope as an informal reading.

### (b) Proof

- By (a) and Proposition 3.4, on every alarm-free path the load tends to $\bar e$ and $\limsup V\le(1-h_V\bar e/\rho)^+<V_{\min}$ under (reach).
- By (e), $m(t)>m_{\rm fl}$ throughout the band $[V_{\min},V_{\rm alarm}]$. Proposition 4.7 then says no alarm fires there.
- So the host reaches $V<V_{\min}$ on an alarm-free path. $\square$

### (c) Tag

[thm∣prem]. The rename follows the synthesis A.8.

### (d) Check

None needed for the logic. The clocks are in m06 (D).

---

## 11. `enforce`, Proposition 5.4

### (a) V6.2 statement changes

- Model: "let $g_i(a)$ be the one-period gain from a deviation $a$ of $i$, $p_d(a)$ the probability that it yields a decisive position from the next period, worth $D_i(a)$".
- **(1)** *$a^\ast$ is sustained by reversion to that punishment iff, for every $i$ and every one-period deviation $a$,*
  $$(1-\delta)g_i(a)+\delta p_d(a)\big(D_i(a)-C_i\big)\le\delta\big(1-p_d(a)\big)(C_i-v_i).\tag{14}$$
  *The deviation with the largest gain need not bind: a quiet deviation with a small gain and a high chance of breakout can, which is exactly the kind masking hides.*
- (2)–(4) apply per deviation, with $\bar p_{d,i}(a)$.
- **(5)** *If punishment is reversion to a race in which each of two racers breaks out with probability $q\le1/2$ per period, at most one per period, being subordinated worth $D^-_i$ (renamed from $U_i$), then $v_i=[(1-\delta)P_i+\delta q(D_i+D^-_i)]/(1-\delta+2\delta q)$. When $D_i+D^-_i>2P_i$, reversion to the race is a lottery the deviator welcomes. It can fail to deter while still leaving the deviator below cooperation ($P<v<C$), even where the deviation itself never breaks out.*
- Scope:
  - "direct evaluation of discounted values agrees with part (1) in all of 200,000 random settings" becomes "a valuation check confirms the algebra of (1) [identity, EC]".
  - Add: "an explicit-action stochastic game, in which one breakout technology sets both $p_d$ and $q$, agrees with (14) by best-response computation in every credible case [num, ES]".
  - The Abreu-type premise (the harshest *credible* punishment) is now in the core Scope (Adv-F F10).

*Example* (replacing $D=4$, $U=0$, $q=0.1$, which had $v>C$): $C=1$, $P=0$, $D=4$, $D^-=0$, $g=2$, $\delta=0.9$. Restraint is enforceable at $q=0$ and not for $q\in(0.0354,0.0556)$, where $v\in(0.778,1)$, still below cooperation.

### (b) Proof

- *(1) per deviation.* The V6.1 proof applies deviation by deviation; the one-shot deviation principle covers every deviation, not only the one with the largest gain.
- *(5).* $V_P=P+\delta[qD/(1-\delta)+qD^-/(1-\delta)+(1-2q)V_P]$ requires $1-2q\ge0$.
- *Window.* Restraint is enforceable at $p_d=0$ iff $(1-\delta)g\le\delta(C-v)$, that is $v\le0.7778$. With $v(q)=3.6q/(0.1+1.8q)$ this holds iff $q\le0.0354$. And $v<C$ iff $q<0.0556$. $\square$

### (c) Tag

[thm].

### (d) Checks

m07, independent:
- *(A) Per-deviation* (Fable's case): deviation A, $g=1$, $p_d=0.1$, is deterred (temptation 0.37 ≤ remaining sanction 1.62). Deviation B, $g=0.2$, $p_d=0.6$, is not (1.64 > 0.72).
- *(B) The window,* from the explicit chain: enforceable at $q\le0.035$; not at 0.036–0.055 while $v<1$; at 0.056, $v=1.004>C$.
- *(C) Explicit-action best response.* Player 1's optimum over all deviation plans is computed by value iteration on the explicit Markov decision process, so this is not a one-shot comparison. It agrees with (14), evaluated with $v$ from (5), in 19,965 of 19,965 random settings where the punishment is credible. In 35 settings quitting the race pays the punisher; there (5) is not the credible punishment value, which is the theorem's premise.
- *(E) Homogeneity.* $\bar p_d$ is homogeneous of degree zero: scaling all of $(g,C,D,v)$ by 10 leaves 0.2963 unchanged, while scaling only $g$ and $D$ moves it to −0.0037.

---

## 12. `relpunish`, Corollary 5.5; `restraint`, Corollary 5.6

### (a) V6.2 statements

**Corollary 5.5 [thm].** *Let the stage game be symmetric, every actor hold $\theta=-1$, and let the punishment phase start from a state that treats the punished and the punishers alike: states and transitions exchangeable under relabelling the players.* The rest is as in V6.1.

*Scope.*
- *With $n\ge3$, punishers in different roles can hold a relative deviator below zero.* In the three-player example the punishment is a stage equilibrium:
  - weak when the positional payoffs of the roles are equal;
  - strict under any small asymmetry between them, with roles assigned accordingly;
  - strict in most nearby games under small anonymous perturbations [num].

  It sustains cooperation for $\delta\ge0.706$. A purely relative punisher is indifferent between hurting the deviator and hurting its fellow punisher, so who takes which role is a matter of coordination: blocs need role assignment.
- *A continuation that treats the deviator asymmetrically, such as a stochastic punishment whose absorbing prize goes to the punisher, escapes the bound altogether.*

**Corollary 5.6.** "(a) keeping $p_d$ low" becomes "**(a) changing that premise**: making $p_d$ low, by not building capability of the decisive class, holding it so no party can use it alone, or detecting and answering faster than breakout".

### (b) Proof of the symmetric-continuation version

- *Two actors.* Let the punisher use any strategy $\sigma_2$. The punished plays its mirror, $\sigma_1(h)=\sigma_2(\text{swap}(h))$.
- From an exchangeable start state the distribution of play is swap-invariant. So $E[J_1]=E[J_2]$, and since $J_1+J_2\equiv0$ at $\theta=-1$, both are 0. Hence $v_1\ge0$.
- *$n\ge3$.* Imitating punishers who all use the same strategy yields an exchangeable profile, with the same conclusion.
- *Asymmetric continuations.* Codex's continuation breaks the start-state symmetry, which is where the bound fails. $\square$

### (c) Tags

- Corollaries 5.5 and 5.6: [thm].
- The strictness claims: [num].

### (d) Checks

m08, independent:
- *The printed example.* Deviation gains in the punishment are (0, 0, −0.2): weak.
- *Label asymmetry.* With unique-X paying $1\pm\varepsilon$, the matching role assignment is strict, with gains (−0.005, −0.005, −0.2) at $\varepsilon=0.01$ and $\delta^\ast=0.706$; the mismatched assignment is not strict.
- *Random anonymous perturbations.* A strict punishment holding the deviator below cooperation exists in 300 of 300 games at $e=0.02$ and $e=0.05$ (median $\delta^\ast$ 0.708 and 0.711), and in 282 of 300 at $e=0.1$ (median 0.713).
- *Codex's stochastic asymmetry.* The target's normalized punishment value is −8.18 and the deviation is worth −69.6, so cooperation is sustained. The symmetric variant gives $v=0$ and the deviation is worth +4, so it is not.

---

## 13. `coverage`, Theorem 5.12; `talk`, Proposition 5.15

**Theorem 5.12 [thm∣prem].**
- Premises: (coverage lags) and (residual floor) only. "(variety grows)" moves to the text as the mechanism behind (coverage lags).
- Statement otherwise unchanged.
- *Proof:* as V6.1. Uniform $U_t/Y_t\to0$ gives a hazard of at least $h(1-\varepsilon)$ after $T_\varepsilon$; $Y_t$'s growth is never used.

**Proposition 5.15 (Talk under relative accounting) [thm].** Relative accounting amplifies the material conflict between a sender and a receiver. Between two rivals at $\theta=-1$ it removes informative talk entirely; among three or more it multiplies their conflict by $n/(n-2)$.
1. *(V6.1 (1), unchanged.)*
2. *Let all $n$ actors hold a common $\theta\in(-(n-1),n-1]$, with sender and receiver in the uniform-quadratic model with a material bias $b_0$ between them, and third parties affected linearly. Talk is informative iff the effective bias $b_0(n-1-\theta)/(n-1+\theta)<1/4$. At $n=2$ the effective bias is $b_0(1-\theta)/(1+\theta)$, infinite at $\theta=-1$. At $\theta=-1$ with $n\ge3$ it is $b_0n/(n-2)$, most at three and falling toward $b_0$ as $n$ grows. A narrower self-model drains talk continuously.*
3. *(V6.1 (3), unchanged.)*

*Scope.* Cheap talk. Third parties enter both objectives alike and do not affect the bias. That rivals who still talk do so as blocs against third parties is [conj].

*Proof (2).*
- $J_S=\pi_S+\frac\theta{n-1}(\pi_R+\sum_k\pi_k)$ and $J_R=\pi_R+\frac\theta{n-1}(\pi_S+\sum_k\pi_k)$.
- With $\pi_S=-(y-u-b_0)^2$, $\pi_R=-(y-u)^2$ and $\pi_k$ linear in $y$, both objectives have curvature $1+\theta/(n-1)$.
- Their ideal points differ by $b_0(n-1-\theta)/(n-1+\theta)$; the third-party terms shift both alike.
- Crawford and Sobel's condition applies to that bias. $\square$

Check: m09, independent. Numerically maximized ideal points match the formula to $1.5\times10^{-8}$ in 19 combinations of $n\in\{2,3,4,6\}$ and $\theta$.

§1.2(4) and the Chinese guide: "among three or more it forms blocs" becomes "among three or more it amplifies their conflict by $n/(n-2)$". Blocs move to [conj].

---

## 14. The scissors (§5.5)

### (a) V6.2 statement

**The scissors, stated exactly.** Each arm is a result under its own conditions; the conjunction is composite, and that the arms move together in the world is a conjecture (C0, tested in §7.4). Restraint is enforceable iff $p_d\le\bar p_d$ (Proposition 5.4). Under the conditions of Definition 2.1:
1. *A larger loop gain raises $p_d$* [thm, with the Remark S2.1 interface]. When $\Gamma>1$, a lead becomes decisive in about $\ln(\bar\Delta/\varepsilon_0)/\ln\Lambda^\ast$ periods, and $p_d=1-\upsilon(T_{\rm dec})$.
2. *Larger stakes lower $\bar p_d$* [thm∣prem]. This holds if the gain from deviating and the value of a decisive position grow faster than the cooperative surplus $C-v$, since $\bar p_d$ is homogeneous of degree zero in $(g,C,D,v)$.
3. *Capture of the correctors lowers $\bar p_d$ through $v$* [thm].
4. *Compounding lowers $\bar p_d$ by narrowing working objectives where the relative return exceeds the common return* [thm]. The arm vanishes where stakes grow in proportion to capacity with $(1-\beta)r\le1$.

**Reduced form [num, rivals not responding].** In the binary game of Remark S5.1 at $D=C$, the largest enforceable discounted loop gain is 0.92 at $p_d=0$, 0.85 at 0.5 and 0.39 at 0.9. None exists above $p_d\approx0.95$ ($\theta_0=0$) or $\approx0.98$ ($\theta_0=0.4$). With a common return $\Gamma^{\rm c}_\delta=0.3$, the value at $p_d=0.9$ is 0.57.

The §5 claim box and the §1.2(4) thesis sentence become conditional:
> "Where stakes outgrow what all share and the cost of control falls, growth moves temptation up and restraint down at once."

### (b) Proof

- *Arm 1.* Remark S2.1, plus the definition of $p_d$ as the probability that $T_{\rm dec}$ is shorter than detection plus response.
- *Arm 2.* $\partial\bar p_d$ along a common scaling is zero (homogeneity); along a scaling of $g$ and $D$ alone it is negative, by the monotonicities of 5.4(2).
- *Arm 3.* $\bar p_d$ falls in $v$.
- *Arm 4.* Proposition 3.9 with Remark S5.1. $\square$

### (c) Tags

- Arms: as marked.
- Conjunction: [conj].
- Reduced form: [num].

### (d) Checks

m10, independent: direct valuation of cooperation and deviation paths, with bisection on $\Gamma_\delta$ and no threshold formula.
- *Largest enforceable $\Gamma_\delta$:* 0.924, 0.852 and 0.387 at $p_d=0$, 0.5 and 0.9.
- *Last $p_d$ with any enforceable gain:* 0.9495 for $\theta_0=0$ and 0.9793 for $\theta_0=0.4$. V6.1 wrote 0.99; Math-Opus's correction is right.

**Test G (Sys m2) changes.** The restraint gap between wider and narrower objectives rises with $p_d$ when $D=C$:
- +0.05, +0.09, +0.21, +0.34, +0.50, +0.82, +0.97 at $p_d=0$, 0.5, 0.8, 0.9, 0.95, 0.99 and 1.

When $D-C=0.5$ it is hump-shaped:
- +0.05, +0.30, +0.92, +0.33, 0, 0, 0 at the same values of $p_d$.

Registered wording: "the gap grows with $p_d$ over the range in which the wider objective still sustains restraint; when a decisive position is worth more than cooperation it closes as $p_d\to1$, where this theory and structural realism agree; the test discriminates at intermediate $p_d$."

---

## 15. `delegatelock` (6.4), `nested` (6.7), R8

**Proposition 6.4 [thm].**
- *If $q_L=1$, then for every finite speed, every $n$, every $p$ and every profile of the others, not delegating gives strictly higher survival, and no one delegating is the unique equilibrium.*
- ***If $q_L<1$ and losing the contest means subordination ($p=1$), at least one of all-delegating and no-delegating is an equilibrium, and both can be.***
- *With $p<1$, an interior number of delegators can be the only equilibrium.*

Check: m09, independent:
- *Codex's case* ($n=3$, $p=0.1$): delegate/not ratios 1.00259, 1.00097, 0.99928 for $k=0,1,2$ others delegating, so exactly two delegators.
- *Random draws:* "neither all nor none is an equilibrium" occurs 0 times in 20,000 at $p=1$, 1,586 times at $p=0.5$, and 60 times at $p=0.1$.

§11.3 and tier 1 of §12.1: "a strict equilibrium among informed actors" gains "when the lock is certain, $q_L=1$".

**Proposition 6.7 [thm∣prem].**
- **$(A_\tau)$ with a matched variant:** *countering the divergence lowers the developer's payoff, net of every private benefit, relative to an otherwise identical developer that does not counter it, and such a matched variant is in the support of selection.*
- (2): *"…developers that counter it lose share relative to their matched variants, tending to zero; the tax can be paid out of a lead while the lead lasts."*
- (3): *"…enforced on every developer as a condition of admission, it survives evasion iff the expected sanction is at least each developer type's gain from evasion. Equal incidence keeps it neutral among those who comply; unequal incidence re-sorts compliers without letting the divergence back in."*

Check: m05 (D), independent:
- A safeguarded developer with baseline 2 and tax 0.1, against an unsafe one with baseline 1: the safeguarded share goes to 1.
- Add its matched twin: the safeguarded share falls to $10^{-87}$.
- Tax 0.01 paid from an independent advantage of 0.02: survives. From 0.005: eliminated.

**R8**, in Proposition 9.1:

| | |
|---|---|
| Requirement | **R8** Common admission constraints before consequential deployment, internal deployment included, for divergences with common costs, with an expected sanction above every developer type's gain from evasion; decisions retained by contest performance only inside them. |
| Kind | necessary |
| Model | relative, cumulative selection among developers under $(A_\tau)$ with a matched variant; decisions retained by performance |
| Basis | Proposition 6.7(3); Lemma 6.5; Lemma 3.3(3) |
| Not needed when | selection by public mandate; zero or negative alignment tax; decisions not retained by contest performance; a liability that turns the common cost into a private one (R1) |

- Add a limits note: "admission reaches only to release; openly released weights can be fine-tuned around it".
- Equal incidence moves to the remark under the table: "desirable, for neutrality among compliers; not necessary for keeping the divergence out".

---

## 16. `opaquecorr` (6.8), `topology` (6.9), `homeostasis` (6.11(3))

**Proposition 6.8 [thm].** *A correction architecture that blocks a share $c_{b,t}$ of failures at base hazard $q_0$ and adds a residual hazard $q_{c,t}$ of its own lowers residual risk iff $q_0c_{b,t}>q_{c,t}$, and makes it summable iff $\sum_t[q_0(1-c_{b,t})+q_{c,t}]<\infty$, which needs blocking that becomes complete.*

Check: m09.
- *V6.1's example* (fixed $c_b=0.99$): survival to period 200 is 0.630 counting from $t=1$ and 0.473 from $t=0$. To 20,000 it is $1.6\times10^{-9}$: not summable. S14's "summable" claim for this example is wrong.
- *Replacement example,* $c_{b,t}=1-2^{-t}$: survival 0.6888 at 200 and at 20,000, against $7\times10^{-10}$ without the corrector at 200.

**Proposition 6.9 and the sentence after it.** "The row-sum certificate is necessary for independent correction, not sufficient" becomes:
> "**Full row sums below one are a sufficient certificate** that no party controls the checks' funding, appointment or access (Proposition 4.9(2)); they say nothing about whether the checks' errors are independent, which must be measured directly."

The certificate is not necessary: a row sum of two from a low start converges to no capture (S14, FA). Make the same change at THEORY line 543 and CLAIMS line 87.

Check: the numbers are reproduced in m09 (0.531, 0.989, 0.940, 0.941, 0.994).

**Proposition 6.11(3).** "…full delegation is an equilibrium for $t\ge5$, with total realized risk at most 3/16 from then on" becomes:
> "**full delegation is an equilibrium at every $t$** (the marginal gain at full delegation is +0.111, +0.023, +0.037, +0.102 and +0.154 for $t=0$–4); the realized hazard is 1 at $t=0$; **from $t=5$ the realized risk sums to 0.1836 ≤ 3/16**."

Check: m09.

---

## 17. `require` (9.1), `share` (10.3(2)), `safeguards` (10.5(1))

### R1

Core column: "long-run effective liability, measured as the **lim sup** of its time average, at least the private advantage of load".

Full form, in S9:
- *Viability at every horizon under (reach) requires that the cumulative advantage $B(t)=\int_0^t(\nu-\tau_{\rm eff})$ not tend to $+\infty$. That implies $\limsup_t\frac1t\int_0^t\tau_{\rm eff}\ge\nu$, and is sharper.*
- *Proof:* if $B\to\infty$, Proposition 3.4 applies.
- Check: m09. $\tau=\nu-1/(2\sqrt{t+1})$ has average tending to $\nu$, yet the host crosses its floor at $t=89$ from a 0.1% race share; with $\tau=\nu$ it does not cross.

### R3a

See §9 above.

### R4

Delete "$D<C$" from "Not needed when", and keep "objectives and sanctions with $\bar p_d\ge1$, for example $(1-\delta)g\le\delta(C-D)$". S9 changes the same way.
- Check: m07 (D). $C=1$, $D=0.9$, $v=0$, $g=2$, $\delta=0.9$ give $\bar p_d=0.8642$; (14) fails at $p_d=0.87$ and 0.9 although $D<C$.

### Proposition 9.1's title

"Proposition 9.1 (Requirements, by the kind of support each has) [thm∣prem]" becomes "**Table 9.1 (Requirements, by the kind of support each has) [def; each row cites its support]**". It organizes results proved elsewhere, as its own text says. Fable F9 and Adv-O make the same point.

### Proposition 10.3(2) [thm]

> *Sharing a fraction $\beta$ of the divisible prize among all $n$, the winner included, with the promise kept with probability $\varrho$, is the contest with prize $\Omega_{\rm eff}=(1-\beta\varrho)\Omega_e+\Omega_s$. Sharing it among the $n-1$ others gives $\Omega_{\rm eff}=(1-\beta\varrho\,n/(n-1))\Omega_e+\Omega_s$.*

The rest is unchanged; it matches Proposition 5.7's $n$/$n-1$ distinction.
- Proof: the winner's own share of what is shared is $1/n$ of $\beta\Omega_e$ in the first case and nothing in the second.
- Check: m09, independent. The uninvadable intensity, found by root and grid search, equals $r\Omega_{\rm eff}/(nc)$ under both conventions at $\beta=0.3$ and 0.6 (0.300, 0.275, 0.225 and 0.175).

### Theorem 10.5(1) [thm]

> *Sufficiency. Under (I1)–(I4), effective liability exceeds the advantage after a finite time and the load falls to its minimum. If that minimum satisfies $h_Ve_{\min}<\rho(1-V_{\min})$, the host's long-run level exceeds its floor. The trajectory stays above the floor throughout iff the liability margin $\Delta=\tau_{\rm eff}-\nu$ is at least a minimum $\Delta_{\min}$, set by the host, the floor, the initial composition and the speed of selection. Without that margin the forgiving host dips below its floor and recovers. A host that degrades by itself below a threshold does not recover, and also needs a floor at or above its own threshold.*

- Replace "the first computable instance of the correctable kernel" with "**an instance of the boundary of viable parameters for a fixed strategy**". It is not a discriminating kernel: it neither takes the union over strategies nor intersects over disturbances.
- The V6.1 clause "viable if, in addition, the host stays above its floor while the load falls" is circular (Opus M5) and goes.
- Check: m09, independent. The logistic transient minimum at $\Delta=0.08$ is 0.1397. $\Delta_{\min}$ is 0.108, 0.165 and 0.355 for floors 0.2, 0.3 and 0.5, reproducing Opus M5 with an independent integrator.

---

## 18. Tags and wording elsewhere

| Location | V6.2 |
|---|---|
| Theorem 7.1, Branch I′ | "…and none beyond, *as at a survivable second strike*"; move "can stabilize as nuclear deterrence did" to the text with [obs]. Also: rename to "Summary 7.1 (Contest branches) [thm, each item cites its result]", since it collects results. |
| Corollary 7.3 | Split it. "In Branch I, or II without timely detection, racing can be each actor's best response to a racing rival; the race as a collective course leaves everyone's protection after a win to the winner's objective (5.7) and, under 7.2's premise, shifts winners toward those whose objectives give least" [thm∣prem]. "*Therefore the premise of the race cannot justify it as a collective course*" [val]. |
| Theorem 8.11, last sentence | "That bound holds only while the verified coalition's advantage in effective compute stays above the decisive ratio; since effective compute is algorithmic efficiency times compute, the coalition's compute advantage must grow as fast as diffusion erodes its algorithmic one" [def: an identity of the definition], with the rate at which diffusion erodes algorithmic leads as [obs] (EV9). Also: the S8 proof cites "(1)–(4)", which the core statement does not number. Number the four sentences of the core statement, or change the proof to cite by content. |
| Proposition 11.5 | "Definition 11.5 (Requirements of a reachable path) [def], with the support of each requirement" — or, if a theorem is wanted, the capture-basin form of Sys I8, which is not proved here. I recommend [def]. |
| Remark 2.5 | "the two-channel case of Proposition 2.2" becomes "**of the same form** as Proposition 2.2: a cross-coupled pair with no self-gain, where 2.2 is a rank-one perturbation of a diagonal; the stability criterion of both is a loop gain below one" (Sys m1; I checked that no rank-one choice reproduces it). |
| Line 363 (§4.6) | "The same recursion can be generative: success that funds correctors it cannot control is selected in the same way" contradicts Proposition 4.4(1). Correction keyed to no one is selected *against* among carriers. Replace with: "The same recursion can be generative, but not by selection among carriers: correction keyed to no one is selected against (Proposition 4.4); it persists by coverage, formula financing and a loop that runs through the whole (Section 10.4)." |
| Proposition 2.2 Scope | The "200,000 draws" and "six digits" sentences: EC becomes a valuation check (identity); LG(C) becomes an identity (Opus M6). |
| Proposition 3.11 / 5.5 "blocs" | "Relative actors can enforce cooperation only as blocs" becomes "only by role-differentiated punishment, which needs coordination on roles" [thm, 5.5 Scope]; "blocs" stays as the interpretation [conj]. |

---

## 19. Notation

Withdraw the claim that "each symbol has one meaning in all three documents". Replace it with: "Each symbol in this table has one meaning throughout; any other symbol is local to the model in which it is declared." Rename the clashes that fall on table symbols:

| Clash | Where | V6.2 |
|---|---|---|
| $J$ (objective) / Jacobian | S2 | $\mathcal J$ |
| $\lambda$ (weight on winning) / eigenvalue | S2 | Perron root $\Lambda^\ast$; S5.1's local $\Lambda$ becomes $\Lambda_p$ |
| $D$ (decisive value) / diagonal / number of domains | S2, S4 | $\mathcal D$; number of domains $N_D$ |
| $u,v$ in S2 / Remark 2.5 / $v_i$ punishment / $v_d$ | S2, 2.5, S4 | $\mathbf u,\mathbf v$ (bold); Remark 2.5 uses $y_s,y_c$; $v_d$ becomes $k_V$ |
| $C(q;p)$ / $C_i$ | 4.2 | $\mathrm{Cost}(q;p)$ |
| $d$ (correction) / harm coefficient | (15) | $h_d$ |
| $U$ (coverage) / $U_i$ / $U_t$ / $U$ race payoff | 5.4(5), S8, S10 | $D^-_i$; $\mathsf u_t$; $U^{\rm race}$ |
| $m$ (masking) / non-contestants / checks per layer | 3.11, 6.9 | $n_o$; $\mathsf m$ |
| $\tau$ (liability) / detection lag | S5 | $\tau_{\rm det}$ |
| $q$ (capacity) / breakout probability | 5.4(5) | $q_b$ |
| $s$ (speed) / sanction / bloc size | 3.3, 3.11 | $\bar F_k$; $n_b$ |
| $F$ (sanction) / maps | Def 2.4, 3.2 | $\mathcal F$, $\mathcal G$ |
| $\mu$ (prior) / transmission rate | S3, S14 | $\mu_{\rm tr}$ |
| $\varpi$ (trust) / $G=\varpi V$ | S3 | $G=g_VV$ |
| $\kappa_k$ as costs | S3 | $c_k$ |
| $\sigma$ (strength) / rule | Def 2.4 | rule $\mathcal S$ |
| new | — | $\Gamma^{\rm c}_\delta$ common loop gain; $r^{\rm eq}_j,r^{\rm pr}_j$, $\Gamma^{\rm eq}$; $\xi_{r,j}$, level elasticity of decisiveness (joins $\xi_v,\xi_f$); $\Lambda^\ast$; $\bar F_k$; $\kappa_s$, positional coupling |

Fix the doubled kind names ("Proposition Proposition 9.2", "Theorem Theorem 10.5(3)", "Assumption Assumption 4.2") in the `src` files: `{{>key}}` already prints the kind. Add an xref check for doubled kind names (SYNTHESIS H).

---

## 20. Interfaces (S13) and the shared-parameter table (§7.1, S7)

### New or changed S13 rows

| Interface | Between | Assumption | Status |
|---|---|---|---|
| Structural and equilibrium gain | $\Gamma$ (2.2) and contests with chosen intensity | Differentiable symmetric Markov equilibrium | (1)–(3) hold with $r^{\rm eq},r^{\rm pr}$ [thm]; magnitudes, multiplicity and catch-up [num]; the class and sign are crux C5-adjacent |
| Loop gain and working objectives | $\Gamma_\delta,\Gamma^{\rm c}_\delta$ and $\theta$ | First order, others' conduct fixed, both gains below one | Proposition 3.9; the strategic analogue is in 2.2(4) |
| Loop gain and breakout probability | $\Gamma$ and $p_d$ | $p_d=1-\upsilon(T_{\rm dec})$, $T_{\rm dec}$ set by $\Lambda^\ast$, not by $\Gamma$ alone | Linearized; with diffusion the gap can settle short of decisive |
| Correction across models | $d_j$ in (1) and $d$ in (10) | A shared symbol is not a shared mechanism | Proposition S2.3: level channels ↓, ratio channels 0/↑ |
| Capacity and the field | $q$ and the field model | Quasi-static | Replaced by Proposition 4.6 [thm; num] |
| Human capacity and correction (new) | $\mathcal M$ (Lemma 6.3) and $d$ | $d_{\rm eff}=d(\mathcal M/\mathcal M_0)^w$ | Rate law $+w\delta_h$ [thm]; hysteresis loop through masking [num, Sys] |
| Reflexive gain off parity (new) | 2.2 at parity and 4.5(4) | Cultivated conversion $\propto\sum_kp_k^{1+(2-\xi_v)/\eta}$ | The reflexive channel's gain is higher at present inequality (3.5× at a leader share of 0.6, $n=4$, $\eta=1$, $\xi_v=0$; Sys) |
| Talk and the self-model | $\theta$ and 5.15 | Uniform-quadratic, common $\theta$ | Now a result (5.15(2)), not an interface |

### §7.1 table, corrected rows

↑ means a rise raises the danger. Each cell names its model.

| Parameter (what is moved; what is held) | Loop gain (2.2, S2.3) | Working objective (3.9) | Enforcement (5.4) | Capture certificate (4.5) | Talk (5.15) |
|---|---|---|---|---|---|
| sharing $\beta$, contemporaneous | ↓ every channel | ↓ | ↓ ($g$ falls); promised ↑ | — | ↓ |
| provision not won $k_0$ | ↓ ratio channels (capacity); 0 linear level channels | ↓ (capacity) | ↓ ($p_d$ falls) | — | ↓ |
| diffusion $\delta_f$ | ↓ every channel | ↓ | ↓ (leads decay) | — | ↓ |
| decisiveness $r$ | ↑ | ↑ | ↑ | ↑ via reflexive channels | ↑ |
| correction of capture (rule support, a level channel) | ↓ | ↓ | ↓ ($v$ falls) | ↓ | ↓ |
| turnover of capacity, $d_K$ (a ratio channel) | 0 without diffusion, ↑ with | ↑ ($\Gamma_\delta$ rises) | ↑ when $\Gamma>1$ (leads open faster) | — | ↑ |
| appropriability $\chi$, conversion $b_{ij}$ | ↑ | ↑ | ↑ | ↑ | ↑ |
| cost of control, falling | ↑ | ↑ | ↑ | ↑ | ↑ via masking |
| stakes, provision fixed | ↑ | ↑ | ↑ via $p_d$; on $\bar p_d$ only if $g,D$ outgrow $C-v$ | ↑ | ↑ |
| stakes growing with capacity (common return) | — | ↑ if $(1-\beta)r>1$, ↓ if $<1$ (proportional case) | as working objective | — | as working objective |
| patience $\delta$ | ↑ ($\Gamma_\delta$) | ↑ with a fixed prize; with a common return, as $\Gamma_\delta$ against $\Gamma^{\rm c}_\delta$ | ↓ (repetition) | — | as working objective |
| held self-model $\theta_0$ | — | ↓ | ↓ | — | ↓ |

Each entry is a result in its own model. The arrows that cross models go through S13. That the parameters move together in the world is C0.

---

## 21. Checks for `checks_v62.py`

### Relabels

- **EC:** independent → **identity (valuation)**. The value-iteration line for the punishment value is the only computed part. Keep it as a regression check.
- **LG(C):** independent → identity.
- **RH:** independent → identity, except its final grid best-response line.
- **BI:** stays identity.
- **NB:** stays derived; its thresholds become 0.9495 and 0.9793.
- In the core text, rephrase "in all of 200,000" and "to six digits" (§18).

### New or extended blocks

All are independent unless marked. Runtimes are on this machine.

| Block | Keys | What it tests | How (independent of the statement) | ≈ s |
|---|---|---|---|---|
| **MP** | `loopgain`, `standprice` | 2.2(4) price with $r^{\rm pr}$; amplification; multiplicity | MPE by value iteration (m01). Three solves: $\Gamma=0.3$ smooth (price vs envelope, within 1%); $\Gamma=0.6$ amplified ($\Gamma^{\rm eq}>1$); $\Gamma=0.2$, $d=0.05$ from $V=0$ and from a step (two fixed points). Plus the static Tullock $2(n-1)/n$ | 60 |
| **GP** | `standprice`, `loopgain`, `compound` | (9) general; $\Gamma^{\rm c}_\delta$; narrowing ⟺ compounding (proportional case) | Nonlinear PV by simulation (m02 A, C) | 3 |
| **G2** *(identity)* | `standprice` | Two-period equilibrium against $e(\theta)$ | Numerical best response; first order by construction | 2 |
| **DO** | `loopgain`, `standprice` | Domain: cusp exponent beyond $\Gamma_\delta=1$; slow convergence for $\Gamma>1>\Gamma_\delta$; log at the boundary | Nonlinear PV at $\varepsilon=10^{-2}$–$10^{-12}$ (m02 D) | 2 |
| **CH** | `loopgain`, `tdec` | Signs of $d$ and $k_0$ by $\xi_r$; S2.1 factor; Perron root ≠ function of $\Gamma$; delayed countervailing channel | Nonlinear relative-mode simulation, eigenvalues (m03) | 1 |
| **CQ** | `compound` | Cap equality; strict cap; diffusion inflow; three inflows | Simulation with min(cap, ·), 400 + 446 random settings (m04) | 12 |
| **PN** | `onegroup` | Total and within ≤ 0 for any monotone fitness; between can be > 0 | Price terms in 3,000 random populations × 6 transforms (m05 C) | 1 |
| **IN** | `blind`, `nested`, `require` | Bistability endpoints; unequal incidence; cross-type exclusion; matched variant; tax from a lead | Replicator simulation (m05 A, B, D) | 1 |
| **FC** | `corrrate`, `costq` | Falling floor (Codex); $[H_f]$ rule with initial condition; $d_f$ rises; lump-sum threshold and no cap | Direct certificate paths, bisection (m06 A–C) | 1 |
| **QS** | `corrrate`, `caplag` | Proposition 4.6: lag delay, additive bound, multiplicative, $+w\delta_h$, reversal | Joint capacity–field simulation, exact stiff steps (m06 D, E) | 2 |
| **ES** | `enforce`, `require` | (14) per deviation; part (5) window; explicit-action best response; R4 | Value iteration on the explicit MDP, 20,000 games (m07) | 25 (or 5 with 4,000 games) |
| **CR** *(extended)* | `relpunish` | Strictness; random anonymous perturbations; continuation asymmetry | Exhaustive pure-profile search (m08) | 3 |
| **DL** | `delegatelock` | $p<1$ interior equilibrium; "neither" counts by $p$ | Direct survival comparison (m09) | 1 |
| **TK2** | `talk` | Effective bias $b_0(n-1-\theta)/(n-1+\theta)$ | Numerical ideal points (m09) | 1 |
| **MS** | `opaquecorr`, `homeostasis`, `share`, `safeguards`, `require` | 6.8 summable vs not; 6.11(3) every $t$; 10.3(2) both conventions; 10.5(1) $\Delta_{\min}$ on the logistic host; R1 example | m09 | 3 |
| **SC** | `zonesillus`, `standprice`, `enforce` | Scissors thresholds by direct valuation; with $\Gamma^{\rm c}_\delta$; Test G hump | m10 | 1 |
| **CS** *(extended)* | `influence`, `corrrate` | Add $\eta\in\{0.5,2\}$ and $\xi\in\{0,0.3,0.5,0.7,1\}$ | Fable m4's grid | 2 |
| **LG** *(extended)* | `loopgain` | Three stocks, mixed strength forms | Fable m1 | 3 |

Total added ≈ 2 minutes, plus MP's 60 s. Keep `--fast` to skip MP and ES.

Codex's eight boundary cases are now all inside blocks:

| Codex case | Block |
|---|---|
| $\Gamma_\delta\ge1$ | DO |
| Cap equality | CQ |
| Positive diffusion | CQ |
| Falling positive $f$ | FC |
| Unequal compliance costs | IN |
| Stochastic punishment asymmetry | CR |
| $p<1$ | DL |
| Nonlinear fitness | PN |

---

## 22. Where the reviewers are wrong, incomplete or need refining

1. **Fable I1** ("$\Gamma_\delta$ itself no longer prices"). The form survives: the price is $\Gamma^{\rm pr}_\delta/(1-\Gamma^{\rm pr}_\delta)$ with the rivals' equilibrium response in $r^{\rm pr}$. The factor $2(n-1)/n$ is exactly $r^{\rm pr}/r$ in the static Tullock (m01 D). Fable's number is right; the conclusion should be "$\Gamma$ prices standing once $r$ is read as $r^{\rm pr}$", not "no longer".
2. **Math-Opus M1** ("structural $\Gamma<1$ is necessary, not sufficient, for stability").
   - It is necessary only in contests where the strategic correction is non-negative. With a strongly concave value of standing, $r^{\rm eq}<r$ (m01 E, $r^{\rm eq}/r=0.993$), and structural $\Gamma<1$ is then not necessary either.
   - Opus's MPE/formula ratios at $\Gamma\ge0.6$ were computed where no local formula can apply ($\Gamma^{\rm eq}_\delta>1$).
   - Opus did not find the multiplicity, which is the more important fact: the same structural gain admits a smooth and a winner-take-all equilibrium (m01 F).
3. **Codex 2.**
   - The sign correction is right. Its proposed remedy ("derive the signs with the strength function stated") is now a theorem with a single parameter, $\xi_r$.
   - Codex and every reviewer missed that **provision** is also channel-dependent: no effect in a linear level channel (§4).
4. **Synthesis A.15 and Codex 5** ("compliance needs $\bar F_k\ge c_k$ for every type"). It is sufficient, not necessary. With heterogeneous types a type whose evasion pays can still be eliminated by another type's compliers (m05 B, sanctions (1, 0.15)). The within-type statement is the exact one.
5. **Math-Opus M2** ("under additive dynamics any $\alpha_{\rm cor}>0$ eventually certifies"). Right, but only *eventually*. At $\alpha_{\rm cor}=0.01$ the certificate fails at $t=10.6$ and recovers later (m06 D). Proposition 4.6 says "eventually".
6. **Math-Fable** ("EC is genuinely independent"). It is not: $V_{\rm coop}\ge V_{\rm dev}$ is (14) rearranged, and Opus and the synthesis are right. A *one-shot* explicit check would be an identity too. That is why ES computes a best response over all deviation plans, including the punisher's incentive in the punishment phase.
7. **Sys I3** (reversal +6–14%). In a self-sustaining domain I find +17% and +54% for adjustment rates 0.1 and 0.03. The direction agrees; the size depends on the model, so the core should give the direction and the Supplement the numbers.
8. **Adv-F F1, a refinement.** "With the prize proportional to total capacity, narrowing iff $(1-\beta)r>1$" also needs **no diffusion**. With diffusion, narrowing begins at $(1-\beta)r>1+\delta\delta_f/(1-\delta(1-d))$ while instability begins at $(1-\beta)r>1+\delta_f/(\kappa g)$. They part (m02 C).
9. **Codex 1.** The nonlinear discounted advantage is positive and the printed multiplier is negative, as Codex says. What Codex leaves open is what happens there. The value has a cusp at parity, with exponent $\ln(1/\delta)/\ln\Lambda^\ast$, so "use a finite-horizon derivative or the nonlinear value function" can be replaced by an exact statement (§1).
10. **Alignment minor 5.** Survival 0.63 to period 200 counts from $t=1$; from $t=0$ it is 0.473. The example is not summable. Confirmed (m09).
11. **Math-Opus minor 3** ($q\in(0.016,0.056)$ at $g=5$). In my $g=2$ example the window is $(0.0354,0.0556)$. Both show the effect is not knife-edge.

No reviewer's algebra was found wrong where they said "verified". The errors were in scope and premises, as the synthesis says.

---

## 23. Elegance: what the repairs unify

1. **One inequality: relative return against common return.** It decides:
   - whether the working objective narrows (3.9);
   - in the proportional case, whether winnings compound (2.3);
   - whether the fourth arm of the scissors acts (§5.5);
   - through $\theta$, how much talk survives (5.15).

   The thesis sentence can be "*where reinvestment's relative return exceeds what all share, compounding narrows the working objective of whoever looks ahead*".
2. **"One loop gain prices standing", said correctly.** "The loop gain that decides whether leads compound also, discounted, prices standing; what standing is worth against what all share is the ratio of two closed-loop factors, $(1-\Gamma_\delta)/(1-\Gamma^{\rm c}_\delta)$."
3. **Three inflows not tied to rank: sharing, provision, diffusion.** They are the three terms of $\phi(0^+)$ in 2.3(2). Two of them, sharing and diffusion, lower the loop gain in every channel; the third, provision, lowers it in ratio channels. This is the formal content of the trees, with knowledge flow now a named third tree.
4. **Correction and provision by channel.** One parameter, $\xi_r$, separates "what correction does" (level channels) from "what provision does" (ratio channels). This explains why the paper's two remedies attach to different channels: provision to capacity, $\chi\to0$ and correction to rule support.
5. **The rate law is a strategic result.** Its sufficiency is robust; its necessity belongs to optimizing carriers. This is §3.1's rule applied to §4: a selection result transfers to strategic actors only where the selected objective is theirs.
6. **Ψ3 partly made true, formally.** The same structural gain supports a smooth equilibrium and a winner-take-all one. The belief that a lead is decisive selects the equilibrium in which it is. §3.8 can cite this [num] as the mechanism behind "Ψ3 holds where institutions built under Ψ make it hold". The generative answer is the same as the paper's: change the gain (sharing, provision, diffusion, $\chi\to0$) so that only one equilibrium remains. In m01 the winner-take-all branch did not appear at coarse rounds, and a smaller gain shrinks the region where it does.
7. **Talk as a function of $\theta$.** One formula covers 5.15(1) and (2) and makes the talk column a theorem.

---

## 24. Open questions, and what needs outside review

1. **Multiplicity of Markov equilibria** (m01 F). This needs an outside check (Codex):
   - that the winner-take-all fixed point is a genuine MPE of the continuous-state game, not an artefact of interpolation (grid refinement 3000 → 6000 moved the price by 1.3%);
   - the threshold, in step size and gain, at which it appears;
   - whether it exists in the deterministic share version of model (1), not only in the lottery.

   If it holds, it is the strongest new result of this round; if it does not, the core loses one sentence.
2. **The sign class of the strategic correction.** I found amplification in Tullock with effort and a reversal only under a strong concave cost of standing. Which contests in the AI field are of which class (catch-up versus discouragement) is an empirical question, adjacent to C5.
3. **Two-arm calibration.** Nothing yet estimates $\Gamma_\delta$ against $\Gamma^{\rm c}_\delta$ for any channel. Adv-O's calibration table (I1(v)) should now carry both gains.
4. **Proposition 4.6(4)** (reversal) was computed in a one-domain self-sustaining model. Whether the field model of §4 with several domains preserves the +17–54% is open.
5. **Strategic version of the common gain.** With rivals responding, a common increase of stocks may change intensities symmetrically and hence shared loss. I did not compute the equilibrium analogue of $\Gamma^{\rm c}_\delta$.
6. **Lemma 3.3(3) with a continuum of types**, and **Proposition 6.7 with heterogeneous baselines but no matched twin.** Is there a clean necessary-and-sufficient condition on the type distribution? I only have the within-type statement.
7. **Model-family bias.** Every simulation here, and those of the four reviewers who ran the joint model, comes from one family. Three choices are the most likely shared blind spots:
   - Tullock as the representative strategic contest;
   - parameters near the draft's;
   - the reading of amplification as strengthening the thesis.

   The multiplicity result and the "two loop gains" form are where an outside mathematician's check would add most.
