# No Winning Position: why AI races fail, why trust is the bottleneck, and what cooperation requires

*Theory draft v4.0, 3 October 2026. Written by Claude (Opus 5.5) from Ren's direction (`sources/16-claude-code-directions/2026-10-03-v4-direction-cooperation.md`, with the 10-02 conversation with Alex and the 10-02 direction for v3). Every sentence is AI-drafted; none is Ren's verbatim. It has not been reviewed. Closed forms and numbers are checked by `checks_v4.py` (log: `checks_v4.log`). This is the full theory, written without a page limit; the paper will be compressed from it.*

**中文概要.** 本稿给出完整理论，分四部分：
- **第一部分（定理 A）：竞赛的理由驳倒它自己的前提。** 若 AI 带来决定性且快速的优势，则每条单边路径都失败：
  - 选择会划出"自我"边界，这条边界损害自我；
  - 任何一方加速，其余方只能加入或消灭它；
  - 决定性竞赛把奖品耗散殆尽，甚至更多；
  - 竞争迫使决策交给 AI，且回不去；
  - 纠错的速度跟不上；
  - 领先者招致预防性打击；
  - 胜出者内部的守护者照样被捕获。

  若前提为假，竞赛就没有理由。
- **第二部分：信任是瓶颈。** 合作需要的信任门槛有精确公式。消息的可信度取决于利益是否对齐（Crawford–Sobel），承诺的可信度取决于权力转移的大小（Fearon）。唯一能同时放松这三者的杠杆，是降低"赢"的私人价值，也就是对齐理解。
- **第三部分（定理 B）：验证必要但不充分。** 这一部分是对 AI 2040 的回应。
- **第四部分（定理 C）：合作需要什么。** 共同理解、共享前沿、渐进互惠地建立信任、对手相互核查加上用 AI 武装的独立纠错，以及自我模型的修正。

理论的认识论地位：它不是无条件定理，因为局势在变、观测不完美。它是理性从今天成立的条件推出的结论；第 6 节列出这些条件，以及什么观察会改变结论。

---

## 0. What the theory is for

A good theory predicts. When it predicts an outcome that no one wants, including those who appear to gain from the present course, and the outcome still cannot be avoided, the obstacle is coordination, and coordination needs the understanding to be shared first. This theory is written for that purpose. It shows that the present course of AI development, a contest among actors each seeking to win, defeats every actor who plays it, the strongest included. It shows that the remedy now pursued, verified agreement among rivals, is necessary but not sufficient. And it shows that what is missing is trust, which only a shared understanding of the first two results can supply.

The theory does not assume that anyone intends harm. It concerns a structure that any actors enter when they contest a technology that can confer decisive advantage: states against states, firms against firms, blocs against blocs. No actor is named, because the argument holds for any actors wherever the dynamics hold.

The conclusion is affirmative. The value AI can create jointly is very large. The race dissipates it; cooperation realizes it. Nothing here asks any actor to sacrifice its interests. It asks each actor to see its interests in a system it cannot leave.

**Epistemic status.** No theorem proves unconditionally that the world must cooperate: situations change and observation is imperfect. Every result below is a derivation from stated conditions. Section 6 lists the conditions, why they hold today, and which observations would change the conclusion. Under the conditions that hold today, reason concludes that the actors must cooperate. That is as firm as any practical conclusion can be.

---

## 1. Setting

**Actors and the contest.** There are $n\ge2$ actors $i=1,\dots,n$, for example states, firms or blocs. They contest capability in AI. Actor $i$ chooses an intensity $e_i\ge0$: how far it pushes capability at the expense of safety margins, deploys ahead of evaluation, accepts risk, or delegates. Who prevails is decided by a contest success function
$$p_i=\frac{\sigma_i^{\,r}}{\sum_j\sigma_j^{\,r}},$$
where $\sigma_i$ is effective strength and $r>0$ is *decisiveness*. Small $r$ means outspending others buys little; large $r$ means the leader takes nearly everything. The case $r\to\infty$ is the all-pay auction.

**The larger system.** Three couplings embed the actors in a system larger than any of them.
1. *Shared conditions.* Each unit of total intensity $E=\sum_je_j$ imposes an expected loss $\rho L$ on every actor: loss of control over AI systems, catastrophic misuse, degraded security or information environment. This term is common to all payoffs.
2. *Interdependence.* Actor $i$'s welfare runs partly through the others: supply chains no actor completes alone, markets, finance, research, the biosphere. In reduced form, $i$'s true welfare is
$$W_i=m_i+\kappa\,\bar m_{-i},\qquad \kappa\in[0,n-1),$$
where $m_i$ is $i$'s own material position and $\bar m_{-i}$ the average of the others'. $\kappa$ measures how much of $i$'s welfare is produced through the others. It is a material fact, not altruism.
3. *Correction.* Institutions (evaluators, rule-makers, courts, treaty bodies) make costs return to their source. They act with a delay, and they are themselves selection environments into which success converts (Section 2.7).

**Self-models.** An actor acts on an objective
$$O_i=m_i+\theta_i\,\bar m_{-i}.$$
$\theta_i$ is the weight the actor's model of itself places on the others.
- $\theta_i=\kappa$ is the *accurate* self-model.
- $\theta_i<\kappa$ draws a boundary inside the system and constructs opposition that the payoffs do not contain. $\theta_i<0$ is rivalry.
- $\theta_i=n-1$ counts the others' welfare as one's own. It is the self-model of an actor that takes the whole system as itself.

**The race premise (P).** The case for racing rests on one premise: AI confers an advantage that is
- (P1) *decisive*: $r$ is large; and
- (P2) *fast*: capability grows at a high rate $g$, so that leads open within short windows.

The premise is widely held and openly stated. We take it as given wherever a result needs it, and Theorem A considers both cases.

**Notation from the earlier versions.**
- The *host* $V$ of v3 is the shared-conditions term written dynamically.
- The field model of correctors is Section 2.7.
- The v3 ratio $\theta=\omega Kh/(\rho\nu)$ is written $\Theta$ here.

**Lemma 0 (Blindness; v3 Lemma 1).** *Under any relative selection rule, a term common to all payoffs does not affect the trajectory of shares; under any payoff-monotone rule it never changes which of two actors grows relative to the other.* The proof is one line: such rules depend on payoff differences, from which common terms cancel. Every result that involves selection rests on this.

---

## 2. Part I: why the race cannot be won

### 2.1 Selection draws a boundary, and the boundary costs the self

Take the setting of Section 1 with effective strength $\sigma_i=e_i$, prize $V>0$, private cost $c>0$ per unit of intensity, and $r\in(0,\,n/(n-1)]$. Material payoffs are
$$m_i=V\,p_i-c\,e_i-\rho L\,E .$$

**Proposition 1 (The boundary error).**
1. *For every $\theta\in[-1,n-1)$ the game in objectives $O_i$ has the symmetric pure equilibrium*
   $$e(\theta)=\frac{rV\,(n-1-\theta)}{n^2\,\big(c+(1+\theta)\rho L\big)}.$$
2. *$e(\theta)$ is strictly decreasing in $\theta$, and every actor's true welfare at the symmetric equilibrium, $W(\theta)=(1+\kappa)\big[V/n-e(\theta)(c+n\rho L)\big]$, is strictly increasing in $\theta$. It is maximal, $(1+\kappa)V/n$, as $\theta\to n-1$.*
3. *Against any fixed intensities of the others, the intensity that maximizes $i$'s own true welfare is its best response under $\theta_i=\kappa$. Acting on $\theta_i<\kappa$ raises $i$'s intensity and, for $r\le1$ (and generically for larger $r$), strictly lowers $i$'s own true welfare.*
4. *Relative selection in a finite population favours $\theta=-1$. There the shared loss $\rho L$ drops out of the objective, intensity is $rV/(nc)$, and each actor's material payoff is $\frac Vn\big(1-r-r\,n\rho L/c\big)$. At $r=1$ the prize is fully dissipated, and with any shared risk every actor ends below zero.*

*Proof.* Expanding,
$$O_i=V\Big(1-\tfrac{\theta}{n-1}\Big)p_i-\big(c+(1+\theta)\rho L\big)e_i+\text{terms independent of }e_i,$$
because each other actor's payoff contains $-Vp_i/(n-1)$ through $1-p_i$, and $-\rho L E$.
1. The game is a Tullock contest with prize $A=V(n-1-\theta)/(n-1)>0$ and marginal cost $c'=c+(1+\theta)\rho L>0$. Its symmetric equilibrium is $e=r(n-1)A/(n^2c')$, which exists in pure strategies for $r\le n/(n-1)$ (Pérez-Castrillo and Verdier 1992). Substitution gives the formula.
2. The numerator of $e(\theta)$ falls and the denominator rises in $\theta$. $W$ is decreasing in $e$ because $c+n\rho L>0$.
3. $W_i=O_i|_{\theta=\kappa}$, so the true best response is the $\theta=\kappa$ best response. Lowering $\theta$ raises the marginal value of intensity by $V\,\partial p_i/\partial e_i/(n-1)+\rho L>0$, so the best response rises. For $r\le1$, $p_i$ is strictly concave in $e_i$, so $W_i$ has a unique maximizer and any other intensity lowers it.
4. In a finite population of size $n$, a strategy is evolutionarily stable if a single deviant does no better than the residents it meets (Schaffer 1988). The resident strategy must therefore maximize the difference between a deviant's payoff and the residents' payoff, $m_i-\bar m_{-i}$, which is the case $\theta=-1$. Substituting $\theta=-1$ into (1) gives $rV/(nc)$, as in Hehenkamp, Leininger and Possajennikov (2004). $\square$

The closed form matches numerical best responses to within $10^{-7}$ for $n\in\{2,3,5\}$, $r\in\{0.5,1,n/(n-1)\}$ and $\theta\in\{-1,\dots,n-1.5\}$. For $n=4$, $r=1$, $\rho L=0.3$, $\kappa=0.4$, true welfare rises from $-0.42$ at $\theta=-1$ to $0.33$ near $\theta=n-1$ (`checks_v4.log`).

*Remark (strategic aggression).* If self-models are observable, an actor can gain by committing to appear more aggressive than its interests warrant, so that rivals back off; the favourite in a contest gains from precommitting (Dixit 1987; Fershtman and Judd 1987). When every actor can do so, the commitment game is itself a race whose equilibrium is mutual aggression and greater dissipation, as in delegation to aggressive agents in contests (Baik and Kim 1997; Konrad, Peters and Wärneryd 2004). Constructing opposition is then a second-order race. It is not an exit from the first.

**In plain words.** A model of oneself that draws a boundary inside a coupled system, and treats what lies outside as opponent, does four things:
- it is what selection on relative standing produces (4);
- it is blind to the shared conditions (Lemma 0);
- it lowers the actor's own welfare whatever the others do (3);
- when everyone holds it, it lowers everyone's welfare (2).

Constructing opposition within one system is therefore not merely unkind. It is a mistake about the system one is part of. The self-model under which every actor does best is the one that counts the system as itself ($\theta\to n-1$). It is the accurate model of a coupled whole, not an ideal imposed on it.

There is one limit, and it leads into Part II. The accurate self-model ($\theta=\kappa$) is individually rational whatever others do. The fully inclusive one ($\theta=n-1$) is collectively optimal but individually rational only if others reciprocate. Between the two lies the problem of trust.

### 2.2 No unilateral exit; the most aggressive actor sets the race

Reduce each actor's choice to racing or restraint. For actor $i$ let
- $R_i$ be its payoff when all restrain;
- $T_i$ when it races against restrainers;
- $P_i$ when all race;
- $S_i$ when it restrains while some rival races.

**Proposition 2 (Join or eliminate).**
1. *If $S_i<P_i$ (restraint against a racer is worse than joining it: "if you are behind, you are dead"), then restraint is never a best response to a racing rival. Once any actor races, each of the others can only join the race or act to stop the racer by force (Section 2.6). In the contest of Proposition 1, $S_i<P_i$ holds whenever racing is a strict best response to racing, which is the case for $r<n/(n-1)$. For more decisive contests, mixed equilibria leave racers indifferent at the margin because the race has consumed the prize (Proposition 3). It holds a fortiori when falling behind costs more than the prize forgone, for example subordination.*
2. *The race begins if any single actor has $T_i>R_i$. If the events $T_i>R_i$ are independent with probabilities $q_i$, the race begins with probability $1-\prod_i(1-q_i)\ge 1-(1-\min_iq_i)^n$, which tends to one as the number of capable actors grows.*

*Proof.* (1) compares $S_i$ with $P_i$. For (2), the race does not begin only if no actor races. $\square$

The race is set by the most race-inclined actor, not the average one (compare the unilateralist's curse, Bostrom, Douglas and Sandberg 2016). That is why the condition is easy to reach and hard to foresee: it needs only one actor, anywhere, to judge that winning pays. It is also why any remedy must cover every capable actor.

### 2.3 A decisive race consumes its prize, and more

**Proposition 3 (Dissipation and overdissipation).** *In the setting of Proposition 1 with $\theta=0$ (self-interested actors), each actor's loss relative to joint restraint is*
$$\Delta=\frac{r(n-1)}{n}\cdot\frac Vn\cdot\frac{c+n\rho L}{c+\rho L}.$$
1. *$\Delta$ increases with decisiveness $r$ and with the shared risk $\rho L$.*
2. *$\Delta$ exceeds $V/n$, so that every actor would be better off if the prize did not exist, iff $r(n-1)(c+n\rho L)>n(c+\rho L)$.*
3. *Beyond $r=n/(n-1)$ there is no pure equilibrium. In the two-actor case with $r\ge2$, and in the all-pay limit $r\to\infty$ for any $n$, the prize is fully dissipated in expectation (Hillman and Riley 1989; Baye, Kovenock and de Vries 1994, 1996; Alcalde and Dahm 2010; Ewerhart 2015). The shared risk then comes on top of full dissipation.*

*Proof.* Joint restraint gives $V/n$. At the equilibrium of Proposition 1 with $\theta=0$, each actor bears $c\,e$ privately and $\rho L\,ne$ from total intensity. (1) and (2) follow by inspection, and (3) is cited. $\square$

For $n=4$, $r=1$, $\rho L=0.3c$, $\Delta=1.27\,V/n$: every actor is worse off than if AI conferred no prize at all (`checks_v4.log`). What is spent in this race is not only money. It is safety margin, accepted risk and delegated control, and part of it ($\rho L$) is borne by everyone. **The more decisive the advantage, the more of its value is consumed in the race to obtain it.** The premise that motivates the race is what makes the race ruinous.

### 2.4 Point of no return I: decisions forced onto AI

Let each actor choose whether to delegate consequential decisions in the contest (strategic, military, economic, research) to AI systems without human review: $d_i\in\{0,1\}$.
- Delegation multiplies effective strength: $\sigma_i=1+a\,d_i$, where $a$ is the advantage of AI-paced over human-paced decision. It grows with capability, $a(t)=a_0e^{gt}$.
- Defeat in the contest costs $L_e$.
- Loss of control by any actor costs every actor $L_c$.
- The per-period hazard of losing control is $h_0$ without delegation and $h_1>h_0$ with it; write $\Delta h=h_1-h_0$.

Payoffs are $u_i=-L_e(1-p_i)-L_c\big[1-\prod_j(1-h_j)\big]$.

**Proposition 4 (Forced delegation).**
1. *If $k$ others delegate, delegating gains $i$ the amount $L_e\big[p_i(1,k)-p_i(0,k)\big]$, which increases in $a$ and tends to $L_e(1-1/n)$ for $k=0$ and to $L_e/(k+1)$ for $k\ge1$. It costs $i$ the amount $L_c\,\Delta h\,(1-h_0)^{n-1-k}(1-h_1)^k\le L_c\Delta h$, which decreases in $k$: the more others delegate, the less one's own restraint buys.*
2. *If $L_e/n>L_c\Delta h$, there is a finite $a^\ast$ beyond which delegation is strictly dominant for every actor. With $a(t)=a_0e^{gt}$ this happens at $t^\ast=\ln(a^\ast/a_0)/g$.*
3. *Universal delegation is worse for every actor than none, by $L_c\big[(1-h_0)^n-(1-h_1)^n\big]>0$.*
4. *Under relative objectives the shared loss $L_c$ cancels (Lemma 0), and delegation is chosen at every $a>0$.*

*Proof.* (1) is direct computation from the contest success function. (2): the gain exceeds the cost for each $k$ once $a$ is large, because the limiting gains are at least $L_e/n$. (3): with all delegating, $p_i=1/n$ as with none, and the hazard is higher. (4): $L_c[\cdot]$ is common to all payoffs. $\square$

For $n=3$, $r=1$, $L_e=L_c$, $h_0=0.01$, $h_1=0.2$: $a^\ast\approx1.16$. Once AI-paced decision is about twice as effective as human-paced decision, delegation is dominant, although universal delegation lowers every actor's payoff from $0.30$ to $-0.15$. Even with $\Delta h=0.49$, beyond the sufficient condition, delegation remains dominant at large $a$ (`checks_v4.log`).

The threshold $a^\ast$ depends on rivals' capabilities, which are not observed. The point is therefore reached without a visible line, and the most advanced actor's capability sets it for all (Proposition 2).

**Lemma 1 (Irreversibility).** Let human capacity to take the delegated decisions decay with disuse, $\dot k=-\delta k$ under delegation, and recover as $\dot k=\beta(\bar k-k)$ otherwise; safe operation without AI requires $k\ge k_{\min}$.
- After $T_{\text{lock}}=\ln(k_0/k_{\min})/\delta$ of delegation, an actor that reverts must operate below $k_{\min}$ for a recovery period $T_{\text{rec}}=\beta^{-1}\ln\big[(\bar k-k)/(\bar k-k_{\min})\big]$.
- During that period, reverting alone is dominated (Proposition 4). Reverting together requires every actor to trust every other through $T_{\text{rec}}$.

*Proof.* Solve the two linear equations. $\square$

**The point of no return** is the state in which unilateral reversal is dominated and collective reversal needs trust at the moment trust is hardest to obtain.

*Remark (what decides once decisions are delegated).* The systems to which decisions pass are themselves selected by contest performance. By Lemma 0, terms common to all actors (shared risk, the condition of the host) cancel from that selection. Delegation therefore hands decisions to procedures selected for relative advantage and blind to the shared system, and it executes the boundary error of Proposition 1 at machine tempo. Whether delegation ends well "depends on what we build". Under race selection, what is built is optimized for winning. Alignment of each system to its operator does not change this, since a faithful system pursues its operator's relative objective.

### 2.5 Point of no return II: correction cannot keep pace

**Lemma 2 (Delay bound; Hayes 1950).** For $\dot x(t)=a\,x(t)-k\,x(t-\tau)$ with $a>0$, $\tau>0$: there is a gain $k$ making $x=0$ asymptotically stable iff $a\tau<1$. Stabilizing gains are then exactly $a<k<\sqrt{a^2+\omega^2/\tau^2}$, where $\omega\in(0,\pi/2)$ solves $\omega=a\tau\tan\omega$.

Here $x$ is a deviation that grows at rate $a$ unless corrected, and correction responds to the deviation observed $\tau$ earlier. The check shows decay inside the window at $a\tau\in\{0.5,0.9\}$ and no stabilizing gain on a grid at $a\tau\in\{1.1,2\}$ (`checks_v4.log`).

**Proposition 5 (The tempo bound).**
1. *Correction that responds to observed deviations cannot stabilize any mode whose growth rate exceeds $1/\tau$, whatever its strength.*
2. *Correction that acts on prediction can do more in principle (predictor feedback; Artstein 1982; Krstic 2009), but it needs a model of the system whose errors are amplified by roughly $e^{a\tau}$ over the delay. In a contest of adaptive actors, the predictable part of the system shrinks.*
3. *For hazard classes whose evidence arrives only after a manifestation window $m$ that no testing shortens (the epistemic lag of the 09-28 paper), $\tau\ge m$, which gives a speed limit $a<1/m$ independent of the resources spent on assurance.*
4. *The race raises $a$: intensity rises with decisiveness (Propositions 1 and 3), and capability grows at $g$. For any hazard class with $a\tau\ge1$, only two options remain:*
   - *lower $a$ by slowing down, which no actor can do alone (Proposition 2); or*
   - *lower $\tau$ by handing correction itself to AI, which is Proposition 4.*

*Proof.* (1) and (3) follow from Lemma 2. (2) is a known property of predictor feedback, stated qualitatively. (4) combines Propositions 1–4. $\square$

**In plain words.** When the situation changes faster than human understanding can follow, correction by humans stops working. What then remains is either to slow down together or to let AI correct AI. The second point of no return therefore runs into the first, unless the actors slow down together.

### 2.6 The leader invites preventive attack

Let two actors bargain over a flow of value normalized to 1 per period, with a common discount factor $\delta$ per period. Fighting ends bargaining: actor A then obtains the whole flow with its current probability of prevailing, less a cost $c_A$ per period. Today A prevails with probability $p_1$. After the rival gains its AI advantage, which takes one period (the *window*), A prevails with probability $p_2<p_1$. The rival cannot commit today to how it will use tomorrow's advantage.

**Proposition 6 (Preventive attack).** *Fighting now is rational for A iff*
$$p_1-p_2>(1-\delta)(1+c_A-p_2)\quad\text{when }p_2\ge c_A,\qquad p_1>c_A+(1-\delta)\quad\text{when }p_2<c_A.$$
*Under the race premise the shift is decisive ($p_2\to0$) and fast (a short window, so $\delta\to1$). The condition then reduces to $p_1>c_A$ plus a vanishing margin: preventive attack is rational whenever A's present prospect in a conflict exceeds its cost.*

*Proof.* The most the rival can offer is the whole flow today plus, from tomorrow, A's then-credible value $\max(p_2-c_A,0)$ per period. Fighting now is worth $(p_1-c_A)/(1-\delta)$. Comparing the two gives the conditions (Fearon 1995; Powell 2006). The closed form agrees with direct comparison on a grid of 2,508 cases (`checks_v4.log`). $\square$

For example, at parity ($p_1=0.5$), a decisive shift ($p_2=0$) and $c_A=0.2$, attack is rational once $\delta>0.7$; a gradual shift from 0.5 to 0.4 at $\delta=0.8$ is not (`checks_v4.log`). Strikes aimed only at compute, cheaper than war (lower $c_A$), make the condition easier to meet. Some strategists now propose exactly this threat as a stabilizer (Hendrycks, Schmidt and Wang 2025). The leader, anticipating it, has reason to hide its progress, which degrades the observation that any restraint relies on (Sections 3 and 5.3).

**In plain words.** A race to decisive advantage is the textbook condition under which rational actors who would prefer to bargain fight instead. The alternative to the race is not a quiet loss. It is "missiles at the data centres".

### 2.7 The winner is a field: its guardians are selected

Suppose an actor does prevail. It is not a single mind. It contains agencies, firms, laboratories and AI systems, among which relative selection continues. Its correctors (evaluators, regulators, courts, auditors) are selection environments into which success converts. We restate the core of v3 with the corrections of the 10-03 external review.

In each corrector domain $i$, a share $x_i$ of consequential decisions follows the dominant practice, and success converts into rule support $r_i$ (symbols in this section are local to it):
$$\dot x_i=\zeta_ix_i(1-x_i)(a_ir_i-c_i),\qquad \dot r_i=\varepsilon_i\big(\textstyle\sum_jb_{ij}x_j-d_ir_i\big).$$
With $R_{ij}=a_ib_{ij}/(c_id_i)$, a domain whose full row sum is below one cannot be captured. A seeded domain whose inbound conversion from a captured set exceeds one is captured.

Actors differ in a capacity $q$ to cultivate conversion:
- its cost is $C(q)=fq+\gamma q^{1+\eta}/(1+\eta)$;
- appropriability is $\chi$;
- its return over a selection horizon is $W(q)=\chi q\,y^\top My-C(q)$, with $y=p\bar y$.

**Proposition 7 (Control over correctors; v3 Propositions 3–5, corrected).**
1. *The selection gradient on control capacity is $\chi p^2\,\bar y^\top M\bar y-C'(q)$, which scales with the square of the actor's share. With a positive linear cost $f>0$ there is a size threshold $p^\ast=\sqrt{f/(\chi\bar y^\top M\bar y)}$. With $f=0$ every actor with $p>0$ has a positive marginal return at $q=0$.*
2. *Investment in correction that benefits everyone is selected against within any practice, and dispersed beneficiaries free-ride. Correction keyed to the corrector creates a return to control investment. Whether that investment produces capture depends on whether row sums cross one, which the investment alone does not settle.*
3. *Let AI lower the cost of control as $\gamma(t)=\gamma_0e^{-gt}$. Take a positive cultivation channel ($\chi\hat B\hat Y>0$), $f=0$, an initially valid certificate, and long selection horizons. Then independent correction growing at rate $\alpha$ keeps evaluation certified uncaptured for all $t$ iff $\alpha\ge g/(1+\eta)$, and it fails in finite time otherwise. Under short horizons ($\varepsilon dT\ll1$) the rate $g/\eta$ applies only over the interval in which that approximation holds; asymptotically the long-horizon rate returns.*
4. *If AI also lowers the unit cost of independent correction at rate $g_c$ and its budget grows at $b$, then $\alpha=b+g_c$: AI favours capture only if $g>(1+\eta)(b+g_c)$.*
5. *Splitting a dominant actor into $k$ equal parts divides cultivated conversion by $k^{2/\eta}$, provided the parts have no common controller.*

*Proof.* As in v3 Appendix A, with the review's corrections: the size threshold needs $f>0$; the short-horizon rate is pre-asymptotic (review §9); the split exponent is $2/\eta$ (review §10); appropriable investment is not the same as capture (review §11). $\square$

**In plain words.** Once one actor has won, the race continues inside it, and its guardians are captured by the same dynamics. Moreover, it got there by delegating (2.4) past the tempo bound (2.5). There is no better guardian to be found by winning.

### 2.8 Theorem A: the case for racing refutes its premise

**Theorem A.** *Let conditions K1–K7 of Section 6 hold.*
- *If the race premise holds (decisive and fast):*
  - *(a) unilateral restraint is never a best response to a racer (Proposition 2);*
  - *(b) racing dissipates the prize, and with shared risk leaves every actor below joint restraint, more so under the self-models that selection produces (Propositions 1 and 3);*
  - *(c) as capability grows, delegating decisions to AI becomes dominant, and after capacity decays it becomes irreversible except by collective action requiring trust (Proposition 4 and Lemma 1);*
  - *(d) human correction cannot stabilize hazard classes with $a\tau\ge1$ unless the actors slow down together (Proposition 5);*
  - *(e) an actor nearing decisive advantage gives others a rational motive for preventive attack (Proposition 6);*
  - *(f) an actor that prevails remains a field whose correctors are selected toward capture (Proposition 7).*
- *If the premise fails ($r$ small), outspending others buys little ($p_i\to1/n$), so the gain from racing against restrained rivals becomes negative, $T-R\to-(c+\rho L)(e-e_0)<0$, and racing has no rationale.*
- *In either case, provided the losses in (c)–(e) (loss of control and conflict) are large relative to any actor's advantage in the contest (K7), every actor, the strongest included, does better under joint restraint than on any unilateral path.*

*Proof.* Collect the propositions cited. For the second case, take restraint to be a baseline intensity $e_0>0$ and let $r\to0$ in the contest success function. For the last claim: with asymmetric actors the strongest actor's contest rent is not fully dissipated, so its comparison is between that rent and the expected losses of (c)–(f). K7 states that the latter dominate. $\square$

The theorem is the formal answer to the claim that one must race because others will. If the advantage is as decisive and fast as that claim requires, racing ends in one of four places:
- forced delegation;
- correction outrun;
- preventive war;
- a winner whose guardians are captured.

If the advantage is not that decisive, there is nothing to race for.

---

## 3. Part II: trust is the bottleneck

### 3.1 The assurance threshold

Reduce the interaction between an actor and the rest to two actions: cooperate (restrain under an agreement) or defect.
- Payoffs are $R$ (both cooperate), $T$ (defect against a cooperator), $P$ (both defect) and $S$ (cooperate against a defector), with $R>P>S$.
- Verification detects a defection in time with probability $q$. A detected defector receives $P-F$ ($F\ge0$ is a sanction), and the detecting cooperator reverts in time and receives $P$. Undetected defection yields $T$ and $S$.
- Let $p$ be the actor's degree of trust: its belief that the other will cooperate.

Write $T_q=q(P-F)+(1-q)T$.

**Proposition 8 (Assurance).**
1. *Cooperation is a best response iff*
   $$p\ \ge\ p^\ast=\frac{(1-q)(P-S)}{(R-T_q)+(1-q)(P-S)}\quad\text{when }R>T_q .$$
   *If $R<T_q$, no degree of trust suffices.*
2. *When $T>R$, cooperation is possible at all only if $q>q_{\min}=(T-R)/(T-P+F)$. For a fixed sanction, $q_{\min}\to1$ as $T\to\infty$: the larger the perceived prize of winning, the closer verification must come to perfection, or the larger the sanction must be.*
3. *If $q<1$ and $P>S$, then $p^\ast>0$: no verification short of perfect, timely detection removes the need for trust.*
4. *When actors observe payoffs with small noise, they coordinate on the risk-dominant equilibrium (Harsanyi and Selten 1988; Carlsson and van Damme 1993). Cooperation is risk-dominant iff $p^\ast<1/2$, that is, iff*
   $$R-T_q>(1-q)(P-S).$$

*Proof.* (1) compares $pR+(1-p)\big(qP+(1-q)S\big)$ with $pT_q+(1-p)P$. (2) rearranges $R>T_q$. (3) is immediate from (1). (4) applies the cited results to (1). The formula agrees with direct best responses on a grid (`checks_v4.log`). $\square$

For example, take $R=3$, $P=1$, $S=-5$.
- With $T=2.5$, trust must be $0.92$ without verification and $0.25$ at $q=0.9$.
- With $T=10$, cooperation is impossible without verification and needs $q>0.78$.
- With $T=100$, it needs $q>0.98$, and at $q=0.9$ it is impossible (`checks_v4.log`).

**In plain words.** Four levers act on cooperation:
- **the value of winning, $T$, relative to the joint value $R$:** how clearly every actor sees that winning does not pay;
- **verification, $q$;**
- **the vulnerability of the one who restrains, $P-S$:** "if you are behind, you are dead";
- **sanctions, $F$.**

Trust must exceed a threshold set by all four. Verification lowers the threshold but never to zero. When the perceived prize of winning is large, verification cannot open the door at all.

### 3.2 Credible messages need aligned interests

Each actor knows things the others do not: what its own systems are doing, whether it has seen warning signs, what it intends. Take the standard model (Crawford and Sobel 1982):
- the state $\omega$ is uniform on $[0,1]$ and known to the sender;
- the receiver chooses a response $y$, ideally $y=\omega$;
- the sender values the receiver's correct response but also gains $2\lambda\beta$ per unit of the receiver's response in one direction (for example, the receiver restraining more than the state warrants), where $\lambda$ is the weight on relative standing and $\beta$ the advantage conferred.

The sender's utility is then $-(y-\omega)^2+2\lambda\beta y=-(y-\omega-\lambda\beta)^2+\text{const}$, so its bias is $b=\lambda\beta$.

**Proposition 9 (Credibility of messages).** *Informative communication is possible iff $b<1/4$. The most informative equilibrium partitions the state into $N(b)$ messages, the largest $N$ with $2N(N-1)b<1$. Information that cannot be verified passes only to the extent that interests are aligned.*

*Proof.* This is Crawford and Sobel (1982), uniform-quadratic case; the bias is derived above. $\square$

At $b=0.01$ seven messages can be distinguished; at $b\ge0.25$ only babbling remains (`checks_v4.log`).

**In plain words.** Verification can carry what can be measured: chips, workloads, declared computations. What cannot be measured is carried only by words, and words are believed only when interests are aligned: early warnings that one's own systems are behaving dangerously, assessments of risk, intentions. Under rivalry, the information that joint safety needs most is exactly what an actor has most reason to withhold or shade, since disclosing it hands rivals an advantage.

### 3.3 Credible commitments need bounded stakes

Proposition 6 already shows that a large, fast shift in power makes promises about the future incredible. The same holds inside an agreement. Let an agreement hold back capability; let $K(t)$ be the capability held in check (the overhang); and let an actor's value of exiting first, $X(t)$, increase with $K(t)$. Let exit occur at an exogenous per-period hazard $h(t)$ (changes of leadership, shocks, miscalculation), and let a fraction $\mu$ of the overhang be destroyed on exit.

**Proposition 10 (Commitment under a growing overhang).**
1. *Deterring deliberate exit requires $qF\ge X(t)-X_{\text{stay}}(t)$, so the required verification or sanction grows with $K(t)$.*
2. *The expected loss from exogenous exit per period is $h(t)(1-\mu)\Lambda\big(K(t)\big)$, with $\Lambda$ increasing. It rises over time whenever $K$ grows faster than $h$ falls, unless $\mu\to1$.*
3. *An agreement that preserves the parties' relative positions (proportional caps and proportional reserves) preserves the relative term of every payoff, and with it the motive in $X(t)$.*

*Proof.* (1) and (2) are direct. (3): proportional arrangements leave $p_i$ unchanged and therefore leave the relative component of the payoff active. Compare also the pause result of the 09-28 paper: a pause that freezes shares can complete capture as well as undo it. $\square$

### 3.4 The bottleneck

**Corollary 1 (Trust is the binding constraint, and understanding is the lever).** *The trust threshold $p^\ast$ (Proposition 8), the possibility of credible messages $b<1/4$ (Proposition 9), and the credibility of commitments under a growing overhang (Proposition 10) are all relaxed by the same change: lowering the private value of winning relative to the joint value. This lowers $T-R$, $\lambda$ and $X$. Verification relaxes only the first, and only on verifiable dimensions. Sanctions relax the first at the price of escalation.*

This is the exact form of "the understanding has to be aligned first". What has to be aligned is each actor's understanding of what winning is worth, and Theorem A shows it is worth much less than it appears. Once that understanding is common knowledge, the same verification supports cooperation that it could not support before, words become credible, and commitments become cheaper to keep.

---

## 4. Part III: verification is necessary but not sufficient

### 4.1 The current path

The most complete current plan for avoiding a race to superintelligence is *AI 2040: Plan A* (Larsen, Dean, Halstead, Lifland, Greenblatt and Kokotajlo 2026, ai-2040.com). It proposes a deal between the two leading powers to slow AI development and delay superintelligence until 2040. The deal is to be enforced "without relying on trust" through:
- compute declarations and supply-chain audits;
- inference-only retrofits of datacenters;
- packet-based recomputation of workloads;
- total research transparency;
- mutually assured destruction of compute, fabs and robots on dissolution;
- hardened reserves proportional to pre-deal compute;
- sanctions, cyberattack and the prospect of war against any party that leaves.

We agree with its destination: an agreement among the leading actors to slow down is better than any race. Our claim is that its foundation is insufficient.

### 4.2 Theorem B

**Theorem B (Verification is necessary but not sufficient).**
1. *Necessary.* *Without verification ($q=0$), cooperation is impossible if $T>R$; if $T<R$ it needs $p^\ast=(P-S)/((R-T)+(P-S))$, which approaches one when restraint against a racer is costly ($P-S$ large relative to $R-T$). Among rivals, verification is therefore required.*
2. *Not sufficient.* *Verification that leaves the value of winning unchanged:*
   - *cannot make cooperation possible when $T_q>R$, except by approaching perfection ($q\to1$) or by escalating sanctions (Proposition 8.2);*
   - *never removes the need for trust (Proposition 8.3);*
   - *does not carry unverifiable information, such as early warnings, risk assessments and intentions (Proposition 9);*
   - *checks present compliance but does not secure future commitments against an exit value that grows with the overhang (Proposition 10);*
   - *certifies that declared work is the work run, not that the approval of that work is right. Approval is judgment exercised by a corrector, and Proposition 7 applies to it.*
3. *Hence a verified agreement among rivals that leaves the value of winning intact holds only while verification stays near perfect against a growing exit value, and its failure grows more costly with time.*

*Proof.* Collect Propositions 7–10. $\square$

### 4.3 Plan A read through Theorem B

Plan A's own analysis supplies the evidence.
- **It bets on near-perfect verification.** Its verification supplement concedes that verification is not yet mature, and that verifying a pause with very high assurance today would probably require powering datacenters down. It assumes that a research sprint will close the gap.
- **Its deal is expected to decline.** Its own estimate is roughly 50% by 2040 (deal-decline supplement). The causes it lists include becoming more optimistic about winning the race once the deal has declined, wanting to gain power by developing superintelligence before a leadership transition, and wanting to grab power illegitimately. These are the race's motive surviving inside the agreement (Proposition 10.3), estimated from base rates of past arms-control treaties.
- **Its stakes grow, so its stabilizers must escalate.** World compute in the scenario rises from about $5\times10^8$ to about $10^{12}$ H100-equivalents between 2030 and 2040. By its own model, if the deal dissolves without destroying compute, superintelligence follows in about a week rather than a year. Hence the stabilizers: datacenters, fabs and robots placed where they can be destroyed, self-destruct mechanisms, and war threats (Proposition 10.2). The regime's safety comes to rest on $\mu\to1$: on destruction mechanisms that must work at the moment of greatest temptation, and that are themselves guardians.
- **Its hardest part is judgment.** It calls workload approval and the control of research speed the hardest part of the deal to execute competently, and assigns approval to teams of auditors. That is a corrector inside the field (Proposition 7).
- **It assumes the will and the trust.** By design it is optimistic about government action, and it expects reality to look more like its earlier scenario. Its verification apparatus presupposes trust: taps installed in each other's datacenters, recomputation servers trusted by one side, and research programmes made open so as to build trust. Verification amplifies trust; it does not originate it.
- **It names the door itself.** Its assumptions supplement grants that if high takeover risk becomes common knowledge, relying on trust may be the best option.

Theorem B says this last case is not a fallback but the foundation. Plan A already contains the elements that lower $T$:
- total research transparency;
- many companies in many countries at the frontier;
- broad diffusion;
- a dividend to citizens.

They are load-bearing. The theory says they should be made the base, with verification built on top of them, not the reverse.

---

## 5. Part IV: what has to change

**5.1 Align understanding.** Make Theorem A common knowledge among the actors and their publics. This lowers the perceived $T$ toward its true value, which by Theorem A lies below $R$. It also moves self-models toward the accurate one (Proposition 1). It is the only lever in Corollary 1 that acts on all three constraints at once. Producing and spreading this understanding is itself the first act of cooperation. It needs no agreement to begin, and theories like this one are its instruments.

**5.2 Take AI development out of the contest.** Hold the capability frontier in common rather than freezing relative shares.

**Proposition 11 (A common frontier changes the failure mode).** Let the value of capability be common, $m_i=V(E)/n-ce_i-\rho LE$ with $V$ concave, rather than allocated by a contest.
- *Private incentives then give $V'(E)=n(c+\rho L)$, and the joint optimum gives $V'(E)=c+n\rho L$.*
- *Total intensity is therefore at or below the joint optimum: the residual failure is too little speed, not too much.*
- *The temptation that remains is the gap a covert private effort can open over the common frontier, which is small when the common frontier leads.*
- *Under frozen shares, by contrast, the relative term persists and the exit value grows with the overhang (Proposition 10).*

*Proof.* Compare the first-order conditions. $\square$

A common frontier turns a race, whose failure is catastrophe, into a public good, whose failure is slowness. It also lowers $P-S$, since restraint no longer means falling behind, and so lowers the trust threshold (Proposition 8). This is what "take AI and compute out of competition first" means formally.

**5.3 Build trust deliberately.**
- *Graduated reciprocal steps:* each side takes a small verifiable step and invites reciprocation (Osgood 1962).
- *Costly signals:* a trustworthy actor can reassure by a signal that an untrustworthy one would not send. That works only if the signal's cost exceeds what the untrustworthy actor would gain by mimicking it (Kydd 2005), a gain that grows with $T$. Lowering $T$ (5.1, 5.2) therefore makes trust cheaper to build.
- *Repeated observation:* repetition sustains cooperation only with observation (v3 Remark 1: the cutoff on the discount factor rises with the weight on winning).
- *Rivals' evaluation:* observation must not be self-reported by the evaluated party, since captured evaluation masks harm (v3 Proposition 6).

**5.4 Use rivals as each other's guardians, and equip independent correction with AI.** In the field model, a corrector is captured only through conversion from success. Between rivals, cross-conversion is near zero: the verified actor's success does not convert into the rival's evaluators. Its inbound row sum from the verified actor is below one, so the verified actor cannot capture it, whatever is captured inside the verified actor itself (v3 Appendix B certificate).

The rival's verifier may carry its own side's bias, but that bias runs toward finding violations, not toward masking them. The structure that makes the race also makes mutual verification hard to capture in the direction that matters. Rivals need not trust each other for this. They need to accept each other's verification, and their distrust keeps the verifier independent. The price is false alarms, which joint protocols for resolving them must absorb.

Two limits:
- Rivals can collude against third parties, so coverage and third-party access are required.
- Mutual verification checks compliance, not judgment. Approval needs independent correction funded and equipped with AI at least at the rate of Proposition 7(3–4).

**5.5 Correct the self-model.** The deepest lever is the self-model itself, the variable $\theta$ of Proposition 1.
- The accurate self-model, which counts the coupling that exists, is individually rational whatever others do.
- The inclusive self-model, which counts the system as oneself, is the one under which every actor does best. It becomes individually rational once trust exceeds the threshold.

This is the non-dual view stated as a property of a coupled system, not as an ideal.

**Theorem C (Cooperation is the viable path, and it is in every actor's interest).** *Let K1–K7 hold. Then:*
1. *every unilateral path fails (Theorem A);*
2. *verified agreement that leaves the value of winning intact is insufficient (Theorem B);*
3. *a cooperative regime that (a) makes Theorem A common knowledge, (b) holds the frontier in common, (c) builds trust by reciprocal costly steps, and (d) rests on mutual verification by rivals and on independent correction equipped with AI lowers $T$ and $P-S$ and raises $q$.*

*If these together achieve $R-T_q>(1-q)(P-S)$, cooperation is risk-dominant (Proposition 8.4). It is then the outcome actors coordinate on under uncertainty, without perfect verification and without escalating sanctions, and it is individually rational for every actor, the strongest included.*

*Proof.* (1) and (2) are cited. For (3), each element acts on a named term:
- under the true payoffs $T<R$ (Theorem A with K7), and (a) makes the true $T$ the perceived one;
- (b) lowers $P-S$, since restraint no longer means falling behind (Proposition 11);
- (d) raises $q$ and lowers the effective vulnerability $(1-q)(P-S)$;
- (c) raises trust $p$ toward and past $p^\ast$.

The risk-dominance condition is therefore not assumed. It is what the regime is built to achieve, and the contribution of each element to it is identified. $\square$

---

## 6. Conditions, why they hold today, and what would change the conclusion

| | Condition | Why it holds today | What would change the conclusion |
|---|---|---|---|
| K1 | Actors act on the race premise (large perceived $r$) | Development is openly framed and financed as a race for decisive advantage. This needs no elaboration and will be documented in revision | If no actor believed in decisive advantage, racing would lose its rationale (Theorem A, second case), which strengthens the case for cooperation |
| K2 | Capability grows fast (large $g$); leads can open within short windows | Rapid capability growth, with automation of AI research as a stated goal | Sustained slowdown in capability growth would relax Propositions 4–6 |
| K3 | Shared exposure and interdependence ($\rho L>0$, $\kappa>0$) | Loss of control, misuse, cyber and information risks cross every boundary; no actor completes the frontier supply chain alone | Independent, unshared payoffs would remove Propositions 1 and 3 in their shared-risk parts, but not Propositions 2, 4 and 6 |
| K4 | Correction delays comparable to or longer than $1/a$ for some hazard classes | Legislative and evaluation cycles; hazards that manifest only through exposure | Correction demonstrably faster than the hazards it governs would relax Proposition 5 |
| K5 | Verification imperfect ($q<1$) | Its leading proponents call the verification frontier immature; unverifiable information remains | Perfect, timely verification would weaken Theorem B(2), but not the need to lower $T$ when $T$ is very large |
| K6 | Success converts into influence over correctors, and AI lowers the cost of control | Developers fund evaluators, write benchmarks and standards, and supply the models that judge | Zero appropriability ($\chi=0$) or independent correction keeping pace (Proposition 7.4) would relax Proposition 7 |
| K7 | The losses from loss of control and from conflict between capable actors are large relative to any actor's advantage in the contest | Loss of control over advanced AI, and conflict between capable actors, put at risk what any advantage would be for | If the strongest actor's contest rent exceeded its expected losses from delegation, preventive attack and captured guardians, racing could pay for that actor alone. Propositions 2–6 would still hold for all the others, and Proposition 7 for it |

Three further points:
- **If alignment is solved robustly and verifiably before delegation becomes dominant:** that removes part of the cost in Proposition 4, but not Propositions 3, 6 and 7.
- **If defence comes to dominate offence:** that relaxes Proposition 6 and part of $\rho L$, but not Propositions 1, 4 and 7.
- **If AI were diffused openly without removing the contest:** that would spread the race, not end it. The compounding continues, and Proposition 2 applies to more actors.

---

## 7. Objections

**"Let the right side win, then govern well."** This is answered by Theorem A(e) and (f), together with (c) and (d). Racing to win invites preventive attack. The winner gets there by delegating past the tempo bound. Once it has won, the race continues inside it and selects its guardians. "No better guardian" is a result, not a slogan.

**"Deterrence (mutual threat to sabotage) is stable without agreement."** Deterrence needs observation of the other's progress, which the leader has reason to hide (2.6). It faces the preventive-attack condition whenever shifts are fast and large. It does nothing about forced delegation (2.4). It is the race held at the brink, and it resolves into conflict or into agreement.

**"Technical alignment will be solved in time."** It might. But aligning each system to its operator transmits the operator's relative objective (2.4, Remark). The tempo bound limits how fast its adequacy can be checked (2.5). It does not touch Propositions 3, 6 and 7.

**"The other side will never cooperate."** Proposition 2 agrees that any single actor can start the race. That is why cooperation must cover all capable actors, and why the first act is to change the perceived value of winning everywhere (5.1). It is also why unilateral restraint is not proposed.

**"Status is valued for its own sake."** Standing has value only within a system that continues. A preference whose pursuit removes the conditions of its own satisfaction defeats itself. That preference is also the product of the selection described in Proposition 1(4), not a fixed fact about actors.

---

## 8. Relation to v3.1 and the external review

**Kept and moved:**
- Lemma 1 becomes Lemma 0.
- v3 Proposition 2 (weight on winning) is subsumed by Propositions 1–3.
- v3 Propositions 3–5 become Proposition 7, with corrections.
- Masking and silent descent (v3 Proposition 6) serve 2.6 and 5.3: self-reported evaluation cannot replace rivals' verification.
- The certificate and the pause result become 5.4 and Proposition 10.3.

**Dropped as the spine:**
- The host-and-floor theorem (v3 Theorem 1), which the review showed admits counterexamples without a cumulative-selection condition. Shared conditions remain as $\rho L$ and as the host $V$.
- The necessity theorem (v3 Theorem 2) and Corollary 1. Necessity is now argued by exhausting the unilateral paths (Theorem A), by the assurance analysis (Proposition 8), and by Theorem C.

**Review items addressed:**
- R1: the floor theorem is no longer used.
- R2: no longer used.
- R3: necessity is restructured.
- R4: masking is used only for self-reported evaluation, and conservative alarms are compatible.
- R5: Proposition 7(3).
- R6: Proposition 7(5).
- R7: Proposition 7(2).
- R8: no longer used.
- R9: to be done by a joint simulation in the paper.
- R10: Proposition 7 conditions.

---

## 9. References used in this draft

Entries not carried over from v3's verified bibliography are marked † and still need verification.

- Alcalde, J. and Dahm, M. (2010). Rent seeking and rent dissipation: a neutrality result. *Journal of Public Economics* 94. †
- Artstein, Z. (1982). Linear systems with delayed controls: a reduction. *IEEE Transactions on Automatic Control* 27. †
- Baik, K. H. and Kim, I.-G. (1997). Delegation in contests. *European Journal of Political Economy* 13. †
- Baye, M., Kovenock, D. and de Vries, C. (1994). The solution to the Tullock rent-seeking game when R > 2. *Public Choice* 81. †
- Baye, M., Kovenock, D. and de Vries, C. (1996). The all-pay auction with complete information. *Economic Theory* 8. †
- Bostrom, N., Douglas, T. and Sandberg, A. (2016). The unilateralist's curse and the case for a principle of conformity. *Social Epistemology* 30. †
- Carlsson, H. and van Damme, E. (1993). Global games and equilibrium selection. *Econometrica* 61. †
- Crawford, V. and Sobel, J. (1982). Strategic information transmission. *Econometrica* 50. †
- Dixit, A. (1987). Strategic behavior in contests. *American Economic Review* 77. †
- Ewerhart, C. (2015). Mixed equilibria in Tullock contests. *Economic Theory* 60. †
- Fearon, J. (1995). Rationalist explanations for war. *International Organization* 49. †
- Fershtman, C. and Judd, K. (1987). Equilibrium incentives in oligopoly. *American Economic Review* 77. †
- Harsanyi, J. and Selten, R. (1988). *A General Theory of Equilibrium Selection in Games*. MIT Press. †
- Hayes, N. D. (1950). Roots of the transcendental equation associated with a certain difference-differential equation. *Journal of the London Mathematical Society* 25. †
- Hehenkamp, B., Leininger, W. and Possajennikov, A. (2004). Evolutionary equilibrium in Tullock contests: spite and overdissipation. *European Journal of Political Economy* 20. †
- Hendrycks, D., Schmidt, E. and Wang, A. (2025). *Superintelligence Strategy*. †
- Hillman, A. and Riley, J. (1989). Politically contestable rents and transfers. *Economics and Politics* 1. †
- Konrad, K., Peters, W. and Wärneryd, K. (2004). Delegation in first-price all-pay auctions. *Managerial and Decision Economics* 25. †
- Krstic, M. (2009). *Delay Compensation for Nonlinear, Adaptive, and PDE Systems*. Birkhäuser. †
- Kydd, A. (2005). *Trust and Mistrust in International Relations*. Princeton University Press. †
- Larsen, T., Dean, R., Halstead, B., Lifland, E., Greenblatt, R. and Kokotajlo, D. (2026). *AI 2040: Plan A*. AI Futures Project, ai-2040.com; supplements on verification, assumptions and deal decline.
- Osgood, C. (1962). *An Alternative to War or Surrender*. University of Illinois Press. †
- Pérez-Castrillo, J. and Verdier, T. (1992). A general analysis of rent-seeking games. *Public Choice* 73. †
- Powell, R. (2006). War as a commitment problem. *International Organization* 60. †
- Schaffer, M. (1988). Evolutionarily stable strategies for a finite population and a variable contest size. *Journal of Theoretical Biology* 132. (In v3.)
- Also carried over from v3: the field model, certificates, the pause result, and the masking model, with their references.
