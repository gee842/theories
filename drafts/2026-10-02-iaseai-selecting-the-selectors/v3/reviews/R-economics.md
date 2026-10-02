# Review R-economics: "No Viable Winner: Competitive Selection, Captured Correction, and the Necessity of Cooperation in AI Development"

**Venue.** IASEAI'27, AAAI format.
**Reviewer profile.** Industrial organization, evolutionary game theory, public economics, regulation.
**Material read.** `v3/main.tex` in full, appendices included, and the compiled `review-draft.pdf` (11 pages; the main text ends on p. 7). I ignored unresolved citations ("??").
**What I checked.** I checked the algebra of Props. 2, 5(i)–(iv) and 6, and Theorem 2(b)(I4), by hand. I checked numerically the generalizations proposed below (cost curvature in Prop. 5, the repeated-game threshold, and the time-to-alarm bound).

**Recommendation: weak reject as submitted.** Confidence 4/5. Probability of acceptance as is: about 30%.

---

## 1. Summary

Frontier developers ("carriers") deplete a shared "host" $V$. The host regenerates logistically, is depleted at rate $hE$, and is viable only above a floor $V_{\min}$. Payoffs are $\pi_k=\phi_k+(\nu-\tau)e_k+G(V)$. Under any selection rule that is invariant to common shifts in payoffs (Def. 2), $G(V)$ cancels (Lemma 1). So the race strategy spreads, and the host falls below its floor when $h\bar e>\rho(1-V_{\min}/K)$ (Prop. 1, condition C0). A static, symmetric, linear public-goods game with relative concern $\lambda$ gives a threshold $\bar\lambda=(\theta-n)/(n-1)$ and an all-lose comparison of $\nu\bar e(\theta-1)$ (Prop. 2).

The second order treats correctors (evaluation $\mathsf E$; rules and liability $\mathsf S$) as domains in a cooperative ODE system, in which a developer's success converts into rule support for its practice (Eqs. 3–4). A domain is captured when its inbound conversion exceeds one. Results:

- Appropriable control capacity is selected in carriers above a size threshold, with a return quadratic in size (Prop. 3).
- Investment in correction is selected against and free-ridden (Prop. 4).
- Assume quadratic cost, a long horizon and quasi-static adjustment. Then evaluation stays uncaptured only if independent correction exceeds $d^\ast$, and if AI lowers the cost of control at rate $g$, correction must grow at no less than $g/2$ (Prop. 5).
- Captured evaluation masks reports, so the alarm can fire after the floor is crossed (Prop. 6).

Theorem 1 puts these together. Under C0–C4, if correctors are captured before the host reaches the alarm level, the floor is crossed silently, and every carrier is worse off than under joint restraint (given $\theta>1$). Theorem 2 gives invariants I1–I4 (liability $\tau>\nu$; $d>d^\ast$; $m<m_{\mathrm{fl}}$; timing), claimed to be sufficient and "indispensable". Corollary 1 concludes that cooperation binding all carriers and states is necessary. Table 1 lists the failure modes of current remedies. Table 2 lists indicators and falsifiers for C0–C4. An appendix covers certificates, cascades, the re-absorption of reforms, and a result on pauses.

---

## 2. Is the argument really one that "cannot be simply refuted"?

Half right. The proofs are short and, apart from the statement errors in §6, correct. No one will refute the paper by finding an algebra mistake. But a conditional theorem resists refutation only to the extent that three things hold:

- (a) its listed conditions are the conditions it actually uses;
- (b) the conclusions stated in the prose are the conclusions of the theorems;
- (c) the model contains the mechanisms that would reverse the result if they were present.

At the points that matter most, the paper fails all three tests:

- **(a)** Theorem 1 and Corollary 1 rely on at least nine maintained assumptions that are not among C0–C4 and do not appear in Table 2 (R2). A critic does not need to reject C0–C4. She can reject any of these, and the paper offers no evidence for them.
- **(b)** Three headline claims go beyond what is proved:
  - "Cooperation is necessary." Theorem 2(b) proves non-redundancy, not necessity, and the model contains no object called cooperation (R1).
  - "No viable winner." The floor-crossing clause depends on an order of events that is asserted, not derived, and the payoff clause is borrowed from a different model (R2).
  - "AI makes guarding harder faster than it makes it easier." Under symmetric technological progress, the paper's own rate result says the opposite (R4).
- **(c)** By construction, the model leaves out the mechanisms an economist reaches for first: thresholds in payoffs, repeated interaction, countervailing power, assortment, feedback from field size, and capture by a lineage that practises restraint. In several cases **the paper's own results imply the counter-mechanism**:
  - With $n=1$ and $\theta>1$, a monopoly winner internalizes the host (Prop. 2).
  - Once $\tau>\nu$ binds, relative selection favours a large carrier that restrains and lobbies for liability on its rivals.

So the argument can be refuted, not by rejecting C0–C4, but by showing that its conclusions need more than C0–C4. The quickest refutation uses only the paper's own model: the $n=1$ case (R1c) plus symmetric technological progress (R4ii).

The good news is that most of these objections can be absorbed. Several of them become support for the paper's real core, the point that captured evaluation makes the problem unsolvable from inside, if the authors model them instead of assuming them away (R3, R6).

---

## 3. Strengths

1. **Explicit, compact model.** Every result is a stated proposition, and the proofs are short and checkable.
2. **The right second-order question.** Correctors are inside the selection environment, and AI changes the cost of influence over them. This is the right question for AI governance. The AI-race literature mostly stops at the first order.
3. **A useful quantitative frame.** The rate idea is a useful way to make "oversight capacity must scale with capability" quantitative: capture depends on a race between the falling cost of control and the growth of independent correction. It needs generalizing (R4).
4. **The order of capture and evidence.** Fig. 1b and the end of §6 contrast capture-before-evidence with evidence-before-capture. This is policy-relevant and memorable.
5. **The pause result (Prop. 9).** If shares are frozen while rule-making keeps converting them, capture completes above $1/R$ unless rule-making is insulated. This is non-obvious, testable and underexploited; I would give it main-text space.
6. **Candour about evidence.** The paper states falsifiers, says plainly that C0 is the least established condition, and notes that Table 2 does not estimate parameters.
7. **A link to antitrust.** Splitting the dominant carrier lowers cultivated conversion, which ties safety to competition policy.

---

## 4. The strongest refutations, ranked

### R1. "Cooperation is necessary" is not a theorem of this model

**The objection.**

- **(a) What is proved is non-redundancy, not necessity.** Theorem 2(b) shows that for each invariant there are parameters satisfying C0 and the other invariants under which the floor is crossed. Necessity would mean that every viable trajectory satisfies I1–I4. That is not shown, and it is false in the model:
  - I3 is not needed for anticipated harms under ex ante liability; Theorem 2(a) says so itself.
  - I2 is not needed when the corrector domains are unseeded or outside the hull.
  - I4 is irrelevant when capture never occurs.
- **(b) The model contains no object called cooperation.** There is no agreement, no coalition formation, no enforcement and no participation constraint. By assumption, a carrier can choose only $(e_k,q_k,u_k)$ and what it funds. $\tau$, $d$, $\chi$ and $m$ are environment parameters that no carrier can set, and anything that moves them is called "an arrangement that binds all". **The necessity of cooperation is therefore the necessity of an exogenous change in parameters, under another name.** That label covers cases most readers would not call cooperation:
  - a single state whose jurisdiction covers all frontier developers imposing $\tau>\nu$;
  - a regulator that sets conditions for market access (Bradford 2020, the Brussels effect);
  - a coalition that controls compute chokepoints and imposes conditions on all buyers. This is a club with sanctions on outsiders (Nordhaus 2015, "Climate Clubs"), which binds outsiders by sanction, not by agreement, and contradicts "an arrangement that binds all of them".
- **(c) The model itself contains non-cooperative routes to viability, which the Corollary rules out by fiat.**
  - **The monopoly winner.** §6 ("What cooperation does and does not require") says joint development makes the field a single carrier that internalizes the host ($n=1$ in Prop. 2, so restraint whenever $\theta>1$). A carrier that wins the whole field is also $n=1$, with the same $\theta$, because $\theta$ is defined per developer. So under the paper's own condition $\theta>1$, the winner restrains. In the model, the trajectory of winning fails only if the floor is crossed during the race, or if rivalry continues after the "win". **The title "No Viable Winner" is contradicted by the model's $n=1$ case; what the model supports is "no viable race".** This is Olson's stationary bandit with an encompassing interest (Olson 1993) and the hegemonic-stability argument (Kindleberger 1973).
  - **Control by a lineage that practises restraint (raising rivals' costs).** In the model, rule support accrues only to the depleting practice. Let a large carrier adopt restraint and invest $q$ in rule support for a liability on depletion.
    - Once $\tau>\nu$ binds, $\pi_k-\pi_l=(\nu-\tau)(e_k-e_l)$, and the restraining carrier gains relative share.
    - The return is appropriable in the relative sense, because the liability falls on rivals (Salop & Scheffman 1983; "bootleggers and Baptists", Yandle 1983). By the logic of Prop. 3, this strategy is selected above a size threshold.
    - The resulting configuration is "captured", but for viability, capture by the restraint lineage is benign: $\tau(1-x_\mathsf S)$ with $x_\mathsf S\to0$.
    - The paper half-concedes this ("Correction can rise transiently by riding on the success of the practice it favors… Once that practice dominates, it is the incumbent"). But that incumbent's opposition to further correction does not threaten the host.
  - **The privileged group.** Prop. 4(iii) is Olson's (1965) privileged-group condition: a carrier whose own share of the benefit exceeds the cost does supply correction. The paper's own Prop. 3 says the field concentrates, so the large carrier's share of the benefit from the host is not small.
  - **Market rewards for safety.** §8 answers "Competition produces safety innovation" with "wherever safety is privately rewarded. That is invariant (I1)." But I1 is defined as a liability enacted by correctors.
    - If market rewards count as I1, then I1 can be met without any arrangement, which contradicts Corollary 1.
    - If they do not count, they are a route to viability that the theorem does not cover.
- **(d) "The arrangement enforces itself" contradicts Prop. 4.** Corollary 1 says the arrangement enforces itself "as long as (I2)–(I4) keep the corrector independent". But by Prop. 4, independent correction is not supplied from inside, and by Prop. 5 it must keep growing at $g/2$ indefinitely.
  - The arrangement is therefore stable only against defection on $e_k$. That is trivial: it just says the tax works.
  - It is not self-enforcing in the sense used in the economics of agreements, where the hard question is whether the parties keep paying for the enforcer. The relevant benchmark is Barrett (1994): self-enforcing agreements are stable only when they achieve little. The paper does not engage it.

**How damaging.** High. This is the title claim and the last sentence of the abstract. A competent reviewer will see (a) and (b) within minutes. (c) is the kind of objection that makes a programme committee doubt the whole edifice, because it comes from the paper's own model.

**Revision.**

1. **Change the title.** For example: "Selecting the Selectors: Competitive Selection, Captured Correction, and the Conditions for Viable AI Development", or "No Viable Race: …".
2. **Rename Theorem 2(b) "Non-redundancy" and add a necessity statement that the model does support:**
   ```latex
   (c) \emph{Necessity of returning consequences.} Assume (C0), (C1), carriers that differ
   only in $e_k$, a race-strategy carrier present, and the host entering payoffs in common.
   Then every viable trajectory satisfies
   $\limsup_{T\to\infty}T^{-1}\int_0^T\tau(1-x_\dS(t))\,dt\ge\nu$.
   If moreover $\dS$ is seeded and lies in the hull of a captured set, no viable trajectory
   has $d(t)<d^\ast(t)$ for all large $t$.
   ```
   The proof is short. Under replicator dynamics, $\tfrac{d}{dt}\ln(p_k/p_l)=(\nu-\tau_{\rm eff}(t))(\bar e-e_l)$. If the time average of $\tau_{\rm eff}$ is eventually below $\nu-\epsilon$, then $p_k/p_l\to\infty$, $E\to\bar e$, and Prop. 1(iii) applies. The second part follows from Prop. 5(iii) and the first part.
3. **Replace Corollary 1:**
   ```latex
   \begin{corollary}[No unilateral solution]
   Assume (C0)--(C2), that each carrier can change only its own $e_k,q_k,u_k$ and what it
   funds, and that rule support accrues only to the depleting practice. Then no carrier's own
   choices establish (I1)--(I4). They can be established only by an authority whose rules reach
   every carrier whose combined load satisfies (C0), with correction funded so that no carrier's
   success converts into it. Where no single authority has that reach (C5), this requires an
   agreement among the authorities that jointly have it. When $\theta>1$ and parties are
   symmetric, the agreement raises every party's absolute payoff; otherwise it requires
   transfers. Once (I1) is in force, restraint is each carrier's best response, so the
   arrangement is stable against defection on load. It is not stable against erosion of the
   corrector, which by Proposition~\ref{prop:correction} must be supplied continuously from
   outside the field.
   \end{corollary}
   ```
4. **Add a remark on the winner:**
   ```latex
   \begin{remark}[The winner]
   A carrier that becomes the whole field faces $n=1$ and restrains whenever $\theta>1$
   (Proposition~\ref{prop:game}). The trajectory of winning therefore fails through the race,
   not through the winner: either the floor is crossed before the race ends, or rivalry
   continues after it (entry, rival states), so that relative selection persists. A winner's
   captured correctors matter for viability only in the second case; in the first they matter
   for those outside the field.
   \end{remark}
   ```
5. **Concede the restraint-lineage route explicitly (§6):** "If rule support can also accrue to restraint, a large carrier that restrains and invests in liability on depletion gains relative share once $\tau>\nu$, by raising its rivals' costs. This establishes (I1) without agreement, at the price of a corrector captured by a different lineage. Our viability results do not exclude this route; our normative premise of contestability does."
6. **Make I1 consistent.** Either delete "That is invariant (I1)" in the §8 objection, or redefine I1 as "effective private cost of load exceeds $\nu$, by any channel", and then drop the claim that I1 cannot be achieved unilaterally.
7. **Rewrite the last sentence of the abstract.** Replace "In this model, cooperation is not an ideal but a necessity." with: "In this model, viability requires that consequences return and that correction be supplied from outside the competition; where no single authority reaches the whole field, that requires agreement among those who do."

---

### R2. The listed conditions are not the conditions the theorems use

**The objection.** The defence "reject a condition" works only if C0–C4 really are the conditions. They are not. Theorem 1 and Corollary 1 also rely on the following:

1. **$\theta>1$.** It is needed for "every carrier ends with a lower absolute payoff" and for "the arrangement raises every carrier's payoff". It is not in C0–C4 and not in Table 2.
   - $\theta=\omega Kh/(\rho\nu)$ measures the developers' own collective stake in the host relative to the private value of racing. It is not society's stake.
   - It decides whether developers have any self-interested reason to cooperate, and no evidence for it is offered.
   - If $\theta<1$, most of the host's value accrues to non-developers. The win-win then disappears, and the problem becomes coercion of developers by the rest of society, not cooperation among developers.
2. **Symmetry in $\nu$ and $\omega$.** Suppose $\nu_k$ differs across carriers. Plausibly the defining property of the leader is that it converts depletion into advantage most efficiently.
   - Then the leader can have $\theta_k<1$ while $\theta>1$ on average. Joint restraint lowers the leader's payoff and needs side payments: Coasean bargaining with participation constraints.
   - **"Leave every participant better off" (abstract) fails exactly for the actor whose participation matters most.**
3. **The order of events.** "The corrector domains are captured before the host reaches the alarm level" is an *if* in Theorem 1: an assumption about an endogenous event. The text after the theorem argues for it informally ("Acceleration therefore favors capture before evidence").
   - In the model, AI acceleration does shorten $t^\ast$ through $g$.
   - But it also raises $\bar e$ and the speed of selection, which bring the alarm forward.
   - Nothing compares the two effects.
4. **The payoff clause comes from a different model.** "Every carrier ends with a lower absolute payoff than under joint restraint whenever $\theta>1$" is Prop. 2(iii), derived for a static symmetric game with no rule support.
   - In Theorem 1's dynamic, heterogeneous model, the dominant carrier earns control rents $\chi q^\ast y^\top My-C(q^\ast)$ (Prop. 3), which grow as $s^2$.
   - Nothing shows these rents are smaller than its loss $\omega(K-V)$.
   - **"No viable winner" in the payoff sense is unproved for the one carrier it is about.**
5. **$\phi_k=\phi_l$.** Prop. 1(i)–(ii) needs it, but its statement omits it (R5a).
6. **Uniform exposure.** $G$ is common to all carriers, with no assortment.
7. **A fixed field size.** $E$ is a share-weighted average intensity, not total load (R5b).
8. **$\tau=0$ ex ante.** This is part of C1, but it is a fact about policy, not a property of selection. Liability already reaches AI to some degree:
   - Directive (EU) 2024/2853 brings software, including AI systems, under product liability.
   - Courts have held deployers liable for chatbot outputs (*Moffatt v. Air Canada*, 2024 BCCRT 149).

   The relevant condition is $\tau_{\rm eff}<\nu$, not $\tau=0$.
9. **Technical maintained assumptions.** Corrector domains are seeded and in the hull of the captured set; $f=0$; $L=1$; adjustment is quasi-static; masking is linear; the alarm threshold is fixed (R4, R6, §6).

**How damaging.** High for the paper's rhetorical strategy. It turns "a critic must reject a condition" into "a critic may reject any of a dozen unlisted assumptions".

**Revision.**

- **Add explicit conditions to Theorem 1:**
  ```latex
  (C5) $\theta>1$, and carriers are symmetric in $\nu$ and $\omega$ (needed only for the payoff
  clause); (C6) capture precedes evidence: $t^\ast+\Delta_{\rm cap}<T_A(\bar e)$, where
  $\Delta_{\rm cap}$ is the time for $x_\dE$ to reach the level at which $m>\mfl$, and
  $T_A(\bar e)=(\rho-h\bar e)^{-1}\ln\big[(1-V^\ast_{\bar e}/V_0)/(1-V^\ast_{\bar e}/\Valarm)\big]$,
  with $V^\ast_{\bar e}=K(1-h\bar e/\rho)$, is a lower bound on the time at which the host
  reaches the alarm level when $h\bar e<\rho$.
  ```
  Why this is a lower bound: $E(t)\le\bar e$ implies $V(t)\ge V_{\bar e}(t)$ by comparison, and $V_{\bar e}$ is logistic with rate $\rho-h\bar e$ and carrying capacity $V^\ast_{\bar e}$. Follow it with a lemma on how $t^\ast$ and $T_A$ respond to $g$, under an explicit assumption about how AI shifts $\bar e$ and $h$.
- **Qualify or prove the payoff clause.** Either make it conditional ("…and, if the dominant carrier's control rents are smaller than $\omega(K-V)$ when the floor is crossed, every carrier ends with…"), or prove it in the dynamic model.
- **Add a "Maintained assumptions" paragraph.** List items 5–9, each with one line on what happens if it is dropped. This paragraph is what makes the "reject a condition" defence honest.
- **Restate C1** as "relative selection with effective liability $\tau(1-x_\mathsf S)<\nu$ unless an alarm fires".

---

### R3. The floor is not in the payoffs, and the strategic game is one-shot

**The objection.**

- **The floor never enters payoffs.** Definition 1 says viability is "a constraint on every trajectory…, not one payoff to be traded against others", and the text says "every participant persists only while the host does". Yet Prop. 2 uses $G(V)=\omega V$, linear straight through $V_{\min}$: below the floor, developers just earn a little less.
  - **Put the floor into payoffs** (a common loss $L$ below $V_{\min}$) and the static game changes character. For any finite $\lambda$, the relative term cancels $L$ but the absolute term does not: its coefficient is $(1+\lambda)-\lambda=1$.
  - A developer that is pivotal for crossing therefore restrains when $L>(w-\theta/n)\nu\bar e$. The game becomes a coordination game with equilibria at the floor. Theory: Barrett 2013, "Climate treaties and approaching catastrophes", *JEEM*. Experiments: Milinski et al. 2008; Barrett & Dannenberg 2012.
  - In that literature, what destroys cooperation is **uncertainty about where the threshold lies**, not relative concern.
  - **Prop. 2(iv) ("the equilibrium host lies below the floor although no developer chose it") is an artefact of linear $G$.**
- **Prop. 2 is one-shot.** Frontier development is a repeated game among a few long-lived players who observe one another.
  - Under grim-trigger reversion, joint restraint is a subgame-perfect equilibrium if and only if $\delta\ge\delta^\ast=(w-\theta/n)/\big((w-\theta/n)+(\theta-1)\big)$, with $w=1+\lambda(n-1)/n$.
  - I checked: for $\theta=3$ and $n=4$, $\delta^\ast=0.11$ at $\lambda=0$, $0.47$ at $\lambda=2$, and $0.95$ at $\lambda=50$.
  - So for moderate relative concern, cooperation among developers enforces itself without any outside corrector. It fails as $\lambda\to\infty$, under imperfect monitoring of $e_k$ (Green & Porter 1984), with entry, or with short horizons. None of this is discussed.
  - The right comparison is the literature on dynamic commons games (Levhari & Mirman 1980; Dutta & Radner 2009; Dockner et al. 2000), not the static voluntary-contribution game.
- **Selection is applied to a handful of strategic firms.** The paper presents pure selection (Prop. 1) as the $\lambda\to\infty$ limit, then reads it as a description of a few strategic firms with explicit plans and state backing.
  - The classic objection to the "as if" selection argument applies when selection is slow relative to strategy revision (Penrose 1952; Winter 1964).
  - With roughly five frontier developers, firms revise strategy much faster than selection moves their shares.

**How damaging.** Medium-high. It attacks the bridge from the selection mechanism to the behaviour of actual developers and states. It also shows that the need for an outside corrector depends on monitoring, not on preferences.

**The objection can and should be turned into support.** Both escape routes need observation: threshold coordination needs the host's condition to be observed, and repeated-game cooperation needs each developer's load to be observed. **Masking (C4) is exactly the failure of that observability.** Captured evaluation produces both an uncertain threshold location (Barrett & Dannenberg 2012) and noisy public monitoring (Green & Porter 1984). That version of the argument is stronger and more original than "selection is blind".

**Revision.** Add the following after Prop. 2:
```latex
\begin{remark}[Thresholds and repetition]
If crossing the floor costs every developer a common loss $L$, the relative term cancels it
but the absolute term does not, so for any finite $\lambda$ a developer that is pivotal for
crossing restrains when $L>(w-\theta/n)\nu\bar e$; the static game becomes a coordination game
with equilibria at the floor \citep{barrett2013}. In repeated play, joint restraint is sustained
by reversion whenever $\delta\ge(w-\theta/n)/(w-\theta/n+\theta-1)$. Both remedies need
observation: of the floor's location, and of each developer's load. Captured evaluation removes
both (Section~\ref{sec:silent}): masking widens uncertainty about the floor, which turns the
coordination game back into a dilemma \citep{barrettdannenberg2012}, and degrades the public
signal on which reversion depends \citep{greenporter1984}. Selection is the limit in which
neither remedy is available; masking is what pushes a field of strategic developers toward it.
\end{remark}
```
Also cite Barrett (1994) and Carraro & Siniscalco (1993) on how small stable coalitions are. Replace the §8 answer to "Rivals cannot cooperate" with one that names the actual obstacles: monitoring, commitment, and participation by asymmetric parties.

---

### R4. "Half the rate" is an artefact of functional form, and symmetric progress reverses its message

**The objection.**

- **(i) The factor ½ comes from functional form and the horizon.** With quadratic cost, $q^\ast\propto1/(\gamma d)$. The stock of support is flow divided by $d$. So cultivated conversion $\propto1/(\gamma d^2)$.
  - **General cost.** With $C(q)=\gamma q^{1+\eta}/(1+\eta)$, correction must grow at $g/(1+\eta)$ in the long-horizon limit. Checked numerically: $\eta=0.25,0.5,1,2,3$ give $0.8g$, $0.67g$, $0.5g$, $0.33g$, $0.25g$.
  - **Short horizon.** If the selection horizon is short relative to the life of rule support ($\varepsilon dT\to0$), then $L_i\approx\varepsilon_id_iT/2$, and $M_{ij}\to a_i\hat b_{ij}\varepsilon_iT/2$ no longer depends on $d$. The "double duty" disappears, and the required rate is $g/\eta$, which is $g$ for quadratic cost.
  - **So the required rate lies between $g/(1+\eta)$ and $g/\eta$, and "one half" is the quadratic, long-horizon corner.**
  - Institutional rule support takes years to build, and investor horizons are a few years, so the short-horizon case is at least as plausible.
  - Yet the abstract and the Contributions present "half" as a finding.
- **(ii) Under symmetric progress, AI favours correctors.** The paper lists "writing evaluations and benchmarks" among *control* activities. That is also the core activity of independent evaluators.
  - Suppose AI lowers the unit cost of independent correction at rate $g_c$ and its budget grows at $b$. Then $\alpha=b+g_c$.
  - In the long-horizon case, capture requires $g>(1+\eta)(b+g_c)$.
  - **With symmetric progress ($g_c=g$) and quadratic cost, the certificate holds even with flat budgets** (at the margin in the short-horizon case).
  - **Applied symmetrically, then, the model says AI favours correction.** The Conclusion's "AI makes guarding harder faster than it makes it easier unless independent correction keeps pace" needs an asymmetry, $g_c<g/(1+\eta)$, that is neither argued for nor measured.
  - The same applies to "alignment to operators raises the correction the field needs" (§5; Table 1, row 1). An aligned assistant serves independent evaluators too.
- **(iii) AI also lowers $f$.** $f$ is the linear cost term that sets the size threshold $s^\ast=\sqrt{f/(\chi\bar y^\top M\bar y)}$. A lower $f$ lets smaller carriers, challengers and civil society invest in "control". The result is contests over correctors, not capture by one lineage. The model has only one controller.

**How damaging.** Medium-high. The rate result is one of the two contributions the paper itself calls new. Under the most natural symmetric assumption, its policy message ("AI makes capture more likely") is reversed.

**Revision.**

- **Replace Prop. 5(iii)–(iv):**
  ```latex
  (iii$'$) Let $C(q)=\gamma q^{1+\eta}/(1+\eta)$ with $\eta>0$ and $\gamma(t)=\gamma_0e^{-gt}$. In the
  long-horizon limit the certificate eventually fails if independent correction grows at
  $\alpha<g/(1+\eta)$, and holds for all $t$ if $\alpha\ge g/(1+\eta)$ and $d_0$ is large enough;
  when the selection horizon is short relative to the life of rule support, the threshold is
  $g/\eta$. (iv$'$) If AI lowers the unit cost of independent correction at rate $g_c$ and its
  budget grows at $b$, then $\alpha=b+g_c$, and capture requires $g>(1+\eta)(b+g_c)$ in the
  long-horizon case.
  ```
- **Abstract.** Replace "correction that grows at less than half that rate is overtaken" with: "correction is overtaken if it becomes cheaper or better funded more slowly than a fixed fraction of the rate at which control becomes cheaper (one half for quadratic costs and long horizons)".
- **"What AI changes".** Replace the key sentence with: "Whether AI favours capture therefore depends on the ratio of two rates: how fast it cheapens control (drafting, lobbying, integrations, benchmark authorship keyed to the developer) and how fast it cheapens independent correction (evaluation, auditing, red-teaming). Capture is favoured only if the first exceeds the second by the factor $1+\eta$."
- **Table 1, row 1.** Change "bringing capture forward" to "bringing capture forward unless independent evaluators gain at least a fraction $1/(1+\eta)$ of the same cost reduction".
- **Fig. 1a.** Add the $\eta$ and short-horizon variants, or say in the caption that it shows the quadratic, long-horizon case only.
- **Table 2.** Measure $g$ and $g_c$ separately (R8).

---

### R5. Relative selection is too blunt a model of frontier AI competition, and Prop. 1 is misstated

**The objection.**

- **(a) Prop. 1 is misstated.** Prop. 1(i) says "If $e_k>e_l$, then $p_k/p_l$ increases", but the proof assumes $\phi_k=\phi_l$. Without that assumption the statement is false.
  - In general, under replicator dynamics with $\tau=0$: $\dot E=\operatorname{Cov}_p(e,\pi)=\nu\operatorname{Var}_p(e)+\operatorname{Cov}_p(e,\phi)$.
  - The race strategy spreads unless restraint is correlated strongly enough with other sources of advantage: $\operatorname{Cov}_p(e,\phi)<-\nu\operatorname{Var}_p(e)$.
  - Real-world mechanisms that could produce that covariance:
    - enterprise demand for reliability, in credence-good markets where reputation premiums sustain quality (Klein & Leffler 1981; Shapiro 1983);
    - sorting of mission-motivated researchers into restraining labs at lower wages (Besley & Ghatak 2005). Talent is one of the inputs the paper says flows by relative standing;
    - reputational losses from public failures (e.g., Alphabet's one-day fall in market value after the Gemini image-generation incident, February 2024);
    - 2025 industry surveys that reported a safety-branded developer leading in enterprise API share.

  None of this shows that $\operatorname{Cov}<-\nu\operatorname{Var}$. It shows that **the sign is an empirical question, and "whatever the participants value" is too strong**.
- **(b) Field size is fixed.** $E=\sum p_ke_k$ is an average intensity. Suppose total activity $N$ responds to absolute profitability ($\dot N=N(\bar\pi(V)-\delta)$) and load is $hNE$.
  - Then the host settles where $\bar\pi(V)=\delta$: the bionomic equilibrium of the open-access fishery (Gordon 1954).
  - Open access does not imply extinction. It implies that rents are dissipated, with collapse only if extraction stays profitable at low stock.
  - AI revenue depends on functioning institutions and a functioning information environment, so $\nu$ and $G$ both fall as $V$ falls.
  - C0 should be stated at the bionomic equilibrium, not at a fixed $N$.
- **(c) Assortment and national hosts.** The correspondence "selection = $\lambda\to\infty$" holds under uniform interaction ("playing the field").
  - **Assortment** means harms fall disproportionately on the carrier's own users, its own training data, or its own jurisdiction. Model collapse (Shumailov et al. 2024, already in the bibliography) is an example. Under assortment, selection favours preferences that internalize a fraction of the harm equal to the index of assortativity (Alger & Weibull 2013, *homo moralis*).
  - **National hosts.** Many components of the paper's host, such as institutions and information environments, are national or linguistic public goods, not global ones. For those, the "states in which they operate" can act unilaterally, and Corollary 1's "including the states" does not follow.
  - Only the truly global components (biological and cyber catastrophe, loss of control) have the paper's structure across rival states.
- **(d) Absolute payoffs.** Much of the capital in frontier AI comes from diversified owners and hyperscalers whose other businesses are exposed to $V$. These are encompassing or universal-owner interests (Olson 1982; Condon 2020; Azar, Schmalz & Tecu 2018).
  - Exit is driven by absolute losses, not by rank.
  - Both bring $G(V)$ into capital allocation. How effective universal-owner stewardship is in practice is contested, but the paper should say why it fails rather than assume it away.
- **(e) Unequal exposure cuts both ways, and should be analysed rather than left "open".**
  - Some firms' core businesses depend on the information environment. If these most exposed firms lose most as $V$ falls, then unequal exposure without assortment speeds the shift toward the least exposed depleters. That would *strengthen* the paper.
  - What matters is $\operatorname{Cov}(e_k,\text{exposure}_k)$, not unequal exposure as such.

**How the paper acknowledges this.**

- One paragraph, "When the first order fails" (liability and unequal exposure).
- One §8 objection, "Developers care about absolute payoffs", answered with Prop. 2, which is the standard voluntary-contribution game.
- One line in the Limitations.

That is not enough. At a venue like this, the first question every economist will ask is why reputation, liability and customers do not solve the problem.

**How damaging.** Medium. None of (a)–(e) refutes Lemma 1, which is true by definition. Together they restrict the first-order result to harms that are non-attributable, non-assorted and global, and whose depletion is not correlated with other sources of fitness. That domain is still important, but it is narrower than the abstract's "whatever the participants value".

**Revision.**

- **Fix Prop. 1(i):** "If $\phi_k=\phi_l$ and $e_k>e_l$, …". Then add:
  ```latex
  More generally, under replicator dynamics with $\tau=0$,
  $\dot E=\operatorname{Cov}_p(e,\pi)=\nu\operatorname{Var}_p(e)+\operatorname{Cov}_p(e,\phi)$, so the
  race strategy spreads unless restraint is correlated with other sources of advantage,
  $\operatorname{Cov}_p(e,\phi)<-\nu\operatorname{Var}_p(e)$.
  ```
- **Add (C1′) to Theorem 1 and Table 2:** $\operatorname{Cov}_p(e,\phi)>-\nu\operatorname{Var}_p(e)$. Indicator: whether developers that restrain gain share at a given capability rank.
- **Add a scope sentence to §3:** "The host is the non-attributable, non-assorted component of shared conditions: harms that do not return to their source through customers, reputation, courts or the source's own exposure. Harms that do return are outside the model."
- **Add a remark on endogenous field size.** Restate C0 at the bionomic equilibrium: $hN_\infty\bar e>\rho(1-V_{\min}/K)$.
- **Distinguish global from national hosts.** Replace "Proposition 2 applies with states as players" with a sentence that separates the global and national components of the host.

---

### R6. The capture model is not the economics of capture

**The objection.**

- **(a) Monotone by construction.** Lemma 2 needs $b_{ij}\ge0$: no domain can reduce capture in another. That rules out checks and balances, imposed only to satisfy the Kamke condition for tractability. Excluded, for example:
  - courts reviewing regulators;
  - the press exposing evaluators;
  - rival states and rival lineages contesting standards;
  - insurers, whose incentives run the other way.

  Madison's answer to the paper's opening quotation, "ambition must be made to counteract ambition" (Federalist 51), is exactly what the model cannot represent. With countervailing conversion, capture thresholds rise and the system need not be monotone.
- **(b) No regulator objective, no political market.**
  - Stigler (1971) is cited, but its canonical extensions are not. Peltzman (1976) and Becker (1983) predict interior equilibria of influence: as the deadweight loss of a captured policy grows, so does the losers' incentive to lobby against it. In the paper, correction $d$ is exogenous and does not respond to harm.
  - Laffont–Tirole (cited) is about a principal who designs organizations to be proof against collusion. The paper's correctors have no designer.
  - So its capture is "strong capture" by assumption. Carpenter & Moss (2013), also cited, argue that strong capture is the exception.
- **(c) Funding is not capture.** Corollary 1's proof and Table 1 treat any funding link as conversion into the corrector. Whether funding biases a certifier depends on who bears the loss:
  - Issuer-pays rating agencies inflated their ratings because they did not bear default losses (Bolton, Freixas & Shapiro 2012).
  - Insurers paid by the insured price risk, because they pay the claims (Ben-Shahar & Logue 2012).
  - Certifiers with enough future rents stay honest (Strausz 2005). Mathis, McAndrews & Rochet (2009) show when that fails.
  - Gatekeeper liability makes certifiers bear the cost of false certification (Kraakman 1986).

  The masking parameters $\beta_{\rm in},\beta_{\rm out}$ should depend on how exposed the corrector's own payoff is, not only on its lineage.
- **(d) A citation used for the opposite of its result.** Panchanathan & Boyd (2004) is cited for "the second-order free-rider problem of sanctioning". **Its result is that linking public-good contributions to indirect reciprocity *solves* the second-order problem.** Related work points the same way:
  - Gürerk, Irlenbusch & Rockenbach (2006) find that sanctioning institutions win in competition among institutions.
  - Sigmund et al. (2010) and Boyd, Gintis & Bowles (2010) show conditions under which institutional punishment evolves.

  Prop. 4's "selection inside the field does not sustain it" holds only in a model with no reputational linkage and no competition among institutions.
- **(e) Prop. 4(ii) is partial equilibrium and contradicts Corollary 1.** Its proof counts only the loss of rule support as $d$ rises, not the gain from a healthier host.
  - When $\theta>1$ and correction is what makes liability effective, correction can raise the incumbent's absolute payoff. Corollary 1 asserts exactly that ("the arrangement raises every carrier's absolute payoff").
  - Both cannot hold unconditionally.
- **(f) Credit for the pieces.**
  - The size threshold with a return proportional to $s^2$ is close to fixed-cost participation in lobbying (Bombardini 2008), and to the appropriability condition for niche construction that the paper already cites.
  - Re-absorption of reforms whose inbound conversion stays above one (Prop. 8(iii)) is the Acemoglu–Robinson (2008) persistence-of-power result. The paper cites that work only for "de facto power" and should credit the result as theirs.

**How damaging.** Medium. The second-order results are internally valid, and the stylization is defensible in ten pages. But they are stated as general ("control over it is selected in the largest participants"; "investment in correcting it is selected against"). In fact they hold in a model that rules out, by construction, each of the mechanisms the capture literature found to matter.

**Again, this can be turned into support.** Three of these correctives run on accurate observation of harm: Becker's countervailing feedback, reputational linkage (Panchanathan–Boyd), and insurers' pricing. Masking disables all three.

**Revision.**

- **Add to §5:**
  ```latex
  \paragraph{Countervailing pressure.} Groups harmed by the practice mobilize in proportion to
  the harm they perceive \citep{becker1983}, so independent correction responds to reports:
  $d=d_0+\kappa(K-\tilde V)$. With accurate reports this feedback stabilizes the uncaptured
  state; with masking it is disabled exactly when it is needed, since $K-\tilde V=(1-m)(K-V)$.
  ```
- **Prop. 4(ii).** Write "holding the host fixed, correction lowers…" and add: "(v) If $\theta>1$ and correction is what makes liability effective, an incumbent can gain from correction applied to all carriers; it opposes correction applied to itself alone."
- **Related work.** Fix the Panchanathan–Boyd sentence: "…the second-order free-rider problem of sanctioning \citep{yamagishi1986}, which reputation can solve when contributions are observed \citep{panchanathan2004}; masking removes that observability."
- **Make masking depend on payoff exposure.** Add after Eq. (9): "Masking is a property of the corrector's payoff, not only of its lineage: an evaluator that bears the loss of a false report, such as an insurer or a liable gatekeeper, has $\beta\le0$."
- **Credit** Bombardini (2008) and Acemoglu & Robinson (2008) explicitly.

---

### R7. Table 1 argues against weak versions of the alternatives

**The objection.** The table lists seven remedies, chosen as the ones that fail. It leaves out the alternatives an economist would rank first, and gives weak versions of two it does include.

**Omitted.**

- **Liability with mandatory insurance and insurer monitoring.** The insurer is a residual claimant with an incentive to measure $V$ accurately. Its real limits are a better argument for ex ante instruments than anything in the table, and the paper should use them:
  - Judgment-proofness caps $\tau$ below $\nu$ for harms larger than the firm's assets (Shavell 1986).
  - Correlated catastrophic losses are uninsurable.
- **Gatekeeper liability for evaluators** (Kraakman 1986).
- **Unilateral rules from a jurisdiction that reaches the whole field,** through market access (Bradford 2020) or through compute chokepoints (export controls; a club with sanctions on outsiders, Nordhaus 2015). This negates C1 for every carrier it reaches, with no agreement among rivals.
- **Structural separation (antitrust).** The paper's own fragmentation result, in which cultivated conversion falls with $k$, supports it. The table folds it into "Open release, fragmentation" and mentions only its cost (a larger $n$).
- **Evaluation markets in which the buyer or the insurer pays.**
- **Technical verification that does not depend on institutional independence:** hardware-enabled attestation, cryptographic audit of training runs, replication of open-weight models by third parties. These lower the cost of independent correction (raising $\alpha$) and reduce $\beta_{\rm out}$.
- **Judicial review and separation of powers.**

**Weak versions.**

- **"Win first, then govern"** ignores the model's own $n=1$ result (R1).
- **"Align each system to its operator"** claims alignment brings capture forward. If independent evaluators use aligned systems too, it does not (R4).
- **"Open release" and "fragmentation" are different instruments.** Open release also lowers the cost of independent evaluation, since researchers can audit open weights, and the row omits this.

**The caption.** "Each leaves at least one condition of Theorem 1 in place" holds by construction, since the remedies are chosen and described by reference to those very conditions.

**How damaging.** Medium. Governance reviewers will notice that the table argues against weak forms of the alternatives.

**Revision.** Rewrite the "Win first, then govern" row:

> Win first, then govern | A single winner internalizes the host | If the winner becomes the whole field and $\theta>1$, it restrains (Prop. 2, $n=1$). This fails if the floor is crossed during the race, or if rivalry persists after "winning" (entry, rival states), so that $n>1$ and C1 continue; the winner's captured correctors then protect its practice | Props. 1–3, 8

Add these rows:

| Remedy | What it changes | Condition left in place, and consequence | Result |
|---|---|---|---|
| Liability with mandatory insurance | A residual claimant prices load | Judgment-proofness caps $\tau$ below $\nu$ for harms exceeding assets; correlated catastrophic losses are uninsurable; the insurer depends on the same evaluation unless it builds its own (C4) | Works for attributable, moderate harms |
| Rules of a jurisdiction that reaches the field (market access, compute) | Sets $\tau$ for every carrier it reaches | Negates C1 within reach; fails where the load outside reach satisfies C0 (C5); its correctors face C2–C3 | Not cooperation among rivals; viable if reach is global |
| Structural separation | Divides cultivated conversion | Raises $n$, lowering $\bar\lambda$ (Prop. 2): an interior optimum of concentration | Props. 2, 5 |
| Technical verification independent of developers | Lowers the cost of independent correction; lowers $\beta_{\rm out}$ | Viable if $g_c\ge g/(1+\eta)$ | Prop. 5′ |

New caption: "Failure modes of current remedies under the conditions of Theorem 1. Remedies that negate a condition are viable where they reach."

---

### R8. Table 2's evidence measures different quantities from the conditions

**The objection.** The table pairs each condition with evidence about something else.

- **C1.** Governments framing development as a race is evidence about rhetoric. It does not show that capital, compute and talent respond to rank at a given level of absolute profitability. The falsifier ("restraint gains share") already has some support (R5a).
- **C2.** The condition is $\chi>0$ *and* a carrier above $s^\ast$. The evidence speaks to developers' influence over evaluation, which is fine. It says nothing about $\chi$ or the threshold.
- **C3.** The condition is $\alpha<g/2$, a comparison of two rates.
  - The evidence is capability-horizon doubling (kwa2025). That is a capability measure, not the rate at which control activities get cheaper.
  - It also cites "assurance lagging capability", which is a level, not a rate.
  - Neither bears on $g_c$ (R4).
- **C4.** The condition is $\beta_{\rm in}>m_{\rm fl}$ ($0.43$ in the illustration): in-lineage evaluators report the host's condition almost halfway to full health.
  - The evidence is self-preference of LLM judges in pairwise comparisons of outputs (panickssery2024), plus correlated errors (kim2025, goel2025).
  - That is lineage bias at the level of model outputs, not masking of societal conditions, and nowhere near the required magnitude.
  - Many components of the host (outages, fraud statistics, institutional failures) are observed through channels that no model lineage forms.
- **Missing rows:** $\theta>1$; the order of events (C6); C1′; C5.
- **The section title** "Do the conditions hold now?" promises an answer that the caption then disclaims.

**How damaging.** Medium-low on substance, but costly to credibility. An evidence table whose entries do not measure its conditions invites the inference that the conditions are unmeasured.

**Revision.** Retitle §7 "Where the conditions would be measured", and edit the cells:

- **C3, present evidence:** "No direct measurement. Capability growth \citep{kwa2025} bears on $g$ only if control activities get cheaper at the rate capability grows; nothing measures $g_c$, the rate at which independent evaluation gets cheaper."
- **C4, present evidence:** "Lineage bias of model judges on outputs \citep{panickssery2024} and correlated errors \citep{kim2025,goel2025}. No estimate of masking of shared conditions; its magnitude relative to $m_{\rm fl}$ is unknown."
- **New row, $\theta>1$:**
  - Indicator: developers' collective stake in shared conditions, relative to the private value of racing.
  - Evidence: none.
  - Refuted by: developers' revealed willingness to pay for shared conditions (for example, support for binding rules that apply to themselves) falling below the private value of racing.
- **New row, C6 (order of events):**
  - Indicator: time from capability release to independent evaluation, against time from onset of harm to detection.
  - Refuted by: independent detection of new classes of harm consistently preceding developer-funded evaluation.
- **New row, C5 (reach):**
  - Indicator: share of frontier compute and deployment within one jurisdiction's reach.
  - Refuted by: one jurisdiction's rules binding carriers whose combined load can cross the floor.

---

### R9. Novelty: the first order and Prop. 2 are known, and the λ→∞ correspondence needs qualifying

**The objection.** The paper says the first order is "classical", yet presents Prop. 2 as a result whose "message is in the comparative statics": $\bar\lambda$ falls with $n$, and the equilibrium tips as $\lambda$ rises.

- That is the linear voluntary-contribution game with status concern (Hopkins & Kornienko 2004; Aronsson & Johansson-Stenman 2008 on positional concerns and public goods).
- The AI-race version, with an explicit "enmity" parameter and a number of teams, is Armstrong, Bostrom & Shulman (2016). The paper cites it without noting that Prop. 2 reproduces its comparative statics.
- Evolutionary models of the AI race with SAFE and UNSAFE strategies under social learning already exist (Han, Pereira, Santos & Lenaerts 2020, *JAIR*; Han et al. 2021 is already in the `.bib`). So does Hendrycks (2023) on selection.
- On selection and relative payoff, the economics citations are Schaffer (1989), "Are profit-maximisers the best survivors?" (*JEBO*); Alós-Ferrer & Ania (2005); and Koçkesen, Ok & Sethi (2000) on the strategic advantage of negatively interdependent preferences. Schaffer (1988), which the paper cites, is the biology paper.
- On the second order: Bombardini (2008), Acemoglu & Robinson (2008), Grossman & Helpman (1994).

**Is "selection corresponds to $\lambda\to\infty$" correct?** As a heuristic for uniform interaction in finite populations, yes.

- Maximizing $\pi_k-\bar\pi$ is Schaffer's criterion for evolutionary stability in finite populations.
- With a symmetric common term the spite effect vanishes, so the incentive to deplete is $(n-1)\nu/n>0$ for every $\theta$.

The paper should add two qualifications:

- **(i) Prop. 2 does not need $\lambda\to\infty$.** For $n>\theta$, $\lambda=0$ already gives depletion. So $\lambda$ matters only when $n$ is small. That is the frontier-AI case, and it is exactly where the repeated-game and threshold arguments bite (R3).
- **(ii) The correspondence fails** under assortment (Alger & Weibull 2013), and when preferences are observable and can serve as commitments (Güth & Yaari 1992; Dekel, Ely & Yilankaya 2007; Heifetz, Shannon & Spiegel 2007).

**How damaging.** Low to medium. The paper does not claim the first order as new, but Contributions item (1) does claim "a first-order result connecting relative selection, the weight a contest places on winning, and the viability of a shared host".

**Revision.**

- Demote Prop. 2 to a Remark, or fold it into Prop. 1.
- Rewrite Contributions (1) as: "(1) A restatement of the commons under relative selection, used as the baseline for the second order."
- Cite Armstrong et al. for the comparative statics, and add the references above.
- Spend the space saved on the pause result and the order-of-events lemma, which are the more original contributions.

---

## 5. Answers to the committee's specific questions

| Question | Answer |
|---|---|
| **1. Is relative selection a fair model of competition among frontier developers? When does the first-order result fail, and does the paper acknowledge it adequately?** | It is fair for one component of harm: harm that is non-attributable, non-assorted and global, when restraint is not correlated with other advantages. The result fails when $\operatorname{Cov}(e,\phi)<-\nu\operatorname{Var}(e)$ (customers' demand for reliability, reputation, sorting of motivated talent); when harm falls on its source (assortment; national hosts); when field size responds to the host (bionomic feedback); when universal owners or absolute exit matter; and when existing liability brings $\tau_{\rm eff}$ near $\nu$. Unequal exposure cuts both ways: it matters through $\operatorname{Cov}(e_k,\text{exposure}_k)$. The acknowledgement (one paragraph plus one line in the Limitations) is inadequate. Prop. 1(i) is also misstated without $\phi_k=\phi_l$. See R5. |
| **2. Is Prop. 2 novel, and is "selection corresponds to $\lambda\to\infty$" correct? What does it miss?** | It is not novel (R9). The correspondence is correct as a heuristic for uniform finite populations, with the two qualifications in R9. It misses repeated play, thresholds in payoffs, coalition stability (Barrett 1994; Carraro & Siniscalco 1993), and Coasean bargaining with heterogeneous $\nu$, which needs side payments (R2, R3). Note one more point: under relative concern, a symmetric agreement leaves relative standing unchanged and raises absolute payoffs. Relative concern is therefore no obstacle to *wanting* the agreement; the obstacle is enforcement and monitoring. That supports the paper's second-order focus, but undercuts "selection is blind" as the root problem. |
| **3. Are the second-order results (Props. 3–5) credible economics, or artefacts of functional form?** | They are stylized and internally valid, but they exclude countervailing power, regulators' objectives, correctors' own payoff exposure, and reputational linkage (R6). "Half as fast" is an artefact of quadratic cost and a long horizon: the required rate is between $g/(1+\eta)$ and $g/\eta$. Under symmetric progress the policy message reverses (R4). |
| **4. Do Theorem 1 and Corollary 1 establish that cooperation is necessary? Does Table 1 treat the alternatives fairly?** | No. Within the model, necessity is shown only for time-averaged effective liability, and only if the authors add Theorem 2(c). "Cooperation" is a label for exogenous parameter change. The model's own $n=1$ case and the restraint-lineage case are counterexamples (R1). Table 1 omits the strongest alternatives (R7). |
| **5. Are C0–C4 testable, and is Table 2 honest?** | Testable in principle, in part. Identifying $R_{ij}$ needs time series of $x_i$, which no one collects. Table 2's evidence for C1, C3 and C4 measures different quantities from the conditions, and four rows are missing (R8). |
| **6. Weaknesses box and score?** | See §7 and §8. |

---

## 6. Smaller issues

1. **Prop. 2(ii).** "At every $\lambda\ge0$ when $n\ge\theta$": at $n=\theta$ and $\lambda=0$, developers are indifferent. Write $n>\theta$.
2. **Prop. 2(iii).** "The eventual winner included": the equilibrium is symmetric, so there is no winner. In a winner-take-all contest with a prize, the winner's payoff can exceed its payoff under joint restraint. Either model the prize or drop the phrase. The same applies to "the developer that wins is worse off" after Prop. 2.
3. **Lemma 1.** "Its force lies in its generality." Lemma 1 is true by the definition of a relative rule; its content lies in the assumption that $G$ enters additively and identically for all carriers. Say so.
4. **Proof of Theorem 2(a).**
   - (I2) gives $s_\mathsf S(\mathcal C)<1$ for the captured set (Prop. 5), not $\sum_jR_{\mathsf Sj}<1$, which is what the proof uses to invoke Prop. 7(b).
   - $E\to\min_ke_k$ keeps the host above the floor only if some carrier present has $he_k<\rho(1-V_{\min}/K)$.
   - "Stays above its floor" also needs the transient before $\tau_{\rm eff}>\nu$ to be short enough.

   Add all three conditions.
5. **Eq. (W) and Prop. 5 disagree.** In Eq. (W), capacity converts the carrier's *own* success (support $\propto q\sum_j\hat b_{ij}y_j$). In Prop. 5, cultivated conversion is $q^\ast\sum_{j\in\mathcal C}\hat b_{\mathsf Ej}$, without $y_j$. Under Eq. (W), splitting the carrier $k$ ways divides cultivated conversion by $k^2$, not by $k$.
6. **$V$ and $d$.** §3 includes "institutional and scientific capacity for independent correction" in $V$, yet §5 treats $d$ as exogenous. Either drop it from $V$, or let depletion lower $d$. The second option adds positive feedback and strengthens the result.
7. **I1 is a prohibitive tax.** $\tau>\nu$ bans depletion outright. The efficient instrument is a Pigouvian tax equal to marginal external damage.
   - With heterogeneous $\nu$ across uses, I1 over-restrains.
   - With damage convex near the floor, the efficient tax rises as $V$ falls.

   Say that I1 is sufficient, not efficient.
8. **Liability needs observable load.** A liability of the form $\tau e_k$ presupposes that each carrier's load can be observed and attributed. Yet the host is motivated by diffuse, non-attributable harm. Reconcile the two, for example by levying liability on observable proxies (deployment before evaluation, missing safeguards).
9. **Prop. 6(iii) and the fixed alarm rule.**
   - Prop. 6(iii) (permanent silence of moderate harm) holds for *any* upward bias whenever the true state sits just below a fixed threshold. It is not specific to capture.
   - The alarm rule is fixed. A Bayesian or robust decision-maker who knows evaluation may be captured would raise $V_{\rm alarm}$.
   - Silent crossing therefore also requires the decision-maker's beliefs to be captured (Kwak 2014). State this as part of C4.
10. **Prop. 3(ii).** "Capacity cannot invade from rarity" misuses the evolutionary term. The statement is about small carriers, not rare types.
11. **Joint development ($n=1$) is a sanctioned monopoly.** It brings monopoly deadweight loss, moral hazard among the partners (Holmström 1982), and entry outside the venture, which then needs licensing. Separately, any agreement among competitors to restrain deployment runs into antitrust law (Sherman Act §1; Art. 101 TFEU) without a statutory safe harbour. That is one more reason the arrangement must be led by states, and the paper should say so.
12. **Precedents.**
    - Montreal succeeded thanks to low abatement costs, available substitutes, trade restrictions on non-parties, and side payments through the Multilateral Fund. Barrett (2003), the source cited, uses it to explain why climate agreements failed.
    - Smallpox eradication was a best-shot or weakest-link good with low cost.
    - The Antarctic Treaty froze claims of low value at the time.
    - AI has a high private value $\nu$, closer to climate or arms control.
    - The Bletchley declaration is non-binding and does not show rivals binding themselves.

    Present the precedents as existence proofs, together with the conditions that enabled them.
13. **Statement of Contributions.** "New in this setting" is too broad: several results are standard ones under new names (R9). Say exactly which are new: the AI cost-of-control rate condition, the order of capture and evidence, and the pause result.
14. **Identification paragraph.** Recovering $R_{ij}$ needs time series of $x_i$, "the share of consequential decisions following the dominant practice" in each domain. No such series exists, and with $D$ domains and short samples the distributed-lag regression is weakly identified. Name candidate measures: the share of benchmark citations, of standards text, or of evaluation compute authored or funded by the leading lineage.
15. **Abstract.** "The more weight the contest places on winning, the sooner this holds": Prop. 2 is static. Write "the more readily".
16. **Abstract.** "Show… that it cannot correct itself": Prop. 4 shows only that selection *inside the field* does not supply correction. With repeated play or reputation, it can (R3, R6). Write "is not corrected by selection within the field".
17. **Fig. 1 label.** The schematic labels host feedback "$G(V)$: common, cancels". Under Prop. 2 with finite $\lambda$, $G$ cancels from the relative term only, not from absolute payoffs.
18. **Fig. 1a sensitivity.** Report how $t^\ast$ in Fig. 1a changes with $\eta$ and the horizon. This is the figure most readers will remember, and it shows only the quadratic, long-horizon case.

---

## 7. What a hostile but fair reviewer would write in the weaknesses box

> The paper restates the tragedy of the commons under relative selection and adds a stylized model in which developers capture evaluators and regulators. The formal results are individually simple and mostly correct, but the headline claims outrun them.
>
> (1) "Cooperation is necessary" is not proved. Theorem 2(b) shows that each invariant is non-redundant for some parameters, not that every viable trajectory satisfies them, and the model contains no agreement, coalition or enforcement: "cooperation" is the name for any exogenous change in $\tau,d,\chi$. The model's own $n=1$ case (a single winner internalizes the host when $\theta>1$) contradicts the title.
>
> (2) Theorem 1 relies on unlisted assumptions: $\theta>1$, symmetric players, capture before evidence (assumed in an "if" and argued informally), equal non-AI fitness, fixed field size, no assortment. Its payoff comparison is imported from a static symmetric game that has no control rents.
>
> (3) The game-theoretic core ignores thresholds in payoffs (Barrett 2013), repeated interaction among a few long-lived players, and coalition formation (Barrett 1994).
>
> (4) "Half the rate" is an artefact of quadratic cost and a long horizon; in general the required rate is between $g/(1+\eta)$ and $g/\eta$. And if AI cheapens independent evaluation as fast as it cheapens control (the paper lists "writing evaluations and benchmarks" as control), the model predicts that AI favours correctors.
>
> (5) The capture model excludes countervailing power by construction (monotone conversion) and equates funding with capture regardless of who bears losses. Panchanathan & Boyd (2004) is cited for a problem it solves.
>
> (6) The remedies table omits liability with insurance, gatekeeper liability, unilateral regulation by a jurisdiction with global reach, antitrust, and technical verification. The evidence table's entries for C3 and C4 measure different quantities from the conditions.
>
> The second-order question is important, and the capture-before-evidence and pause results are interesting. The paper would be stronger with half the claims.

---

## 8. Score

**Weak reject.** Confidence 4/5.

| Criterion | Score |
|---|---|
| Originality | 2.5/5 (first order and Prop. 2 known; second-order synthesis, the rate idea, ordering and pause results are new) |
| Technical soundness | 3/5 (proofs largely correct; Prop. 1(i) and Theorem 2(a) misstated; theorem statements claim more than the proofs; "necessity" not established) |
| Significance | 3.5/5 |
| Clarity | 4/5 |
| Engagement with the relevant economics | 2/5 |

**Probability of acceptance as is: about 30%.** IASEAI committees are mixed. Reviewers from AI governance will like the framing and the clarity, while any reviewer trained in IO or game theory will write something close to §7.

**With the three changes in §9:** borderline to weak accept, about 55–65%. None of them needs new data.

---

## 9. The three changes that would most raise the paper's resistance to refutation

1. **Make the list of conditions complete and the necessity claim exact (R1, R2).**
   - Add C5 ($\theta>1$, with symmetry or transfers), C6 (the order of events, with the $T_A$ bound) and C1′ (the covariance condition), plus a short "Maintained assumptions" paragraph.
   - Replace Corollary 1 with "No unilateral solution", including the reach condition C5.
   - Add Theorem 2(c): time-averaged effective liability is necessary.
   - Add the $n=1$ remark, and change the title.

   After this, "a critic must reject a condition" becomes true, and the remaining claim is still strong: viability requires that consequences return and that correction stay outside the competition.
2. **Put the floor into payoffs and treat the strategic game properly (R3, R6).**
   - Model thresholds, repeated play and coalition stability.
   - Then show that masking (C4) is what defeats each escape route: it creates uncertainty about the threshold, makes monitoring noisy, disables Becker-style counter-lobbying, cuts reputational linkage, and corrupts insurers' pricing.

   This turns the economists' strongest objections into the paper's central result. The problem is not that selection is blind; it is that captured evaluation blinds everyone, including the strategic players who could otherwise cooperate on their own.
3. **Generalize the rate result and make AI's effect a comparison of two rates (R4).**
   - The required rate is $g/(1+\eta)$ with a long horizon and $g/\eta$ with a short one.
   - $\alpha=b+g_c$, and capture requires $g>(1+\eta)(b+g_c)$.
   - Restate the abstract and the "What AI changes" paragraph accordingly, and measure $g$ and $g_c$ separately in Table 2.

   This replaces a fragile "half" with a robust, testable claim about relative rates. It also removes the easiest refutation available: that the model, applied symmetrically, says AI helps the guardians.
