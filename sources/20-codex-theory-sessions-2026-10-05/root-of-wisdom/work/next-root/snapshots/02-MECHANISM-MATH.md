# Mechanism-to-persistence closure for a class of endogenous renewal systems

Mathematical contribution and audit memo, 5 October 2026. Prepared for the final synthesis of *Alignment as the Reproduction of Its Conditions*. Conditional results, not a claim of an unrestricted law of nature or established scientific priority.

## 1. What this adds, and what already existed

The existing [practice-transmission model](../../2026-10-04-integrated-evolution/practice-transmission-model.md) already derives a three-variable system with paid capacity renewal, inheritance, competing practice transmission, positive equilibria, and global collapse under selection for a subcritical practice. The [endogenous-renewal memo](../../2026-10-04-integrated-evolution/endogenous-renewal-math.md) already derives the associated saturating-production threshold. Those are mechanism results, not merely tests of an unexplained Markov kernel. They should not be presented as newly obtained here.

This memo strengthens their mathematical scope in four specific ways:

1. A whole class of increasing, strictly concave, bounded production laws has one exact surplus threshold governing its positive equilibria.
2. Combining that threshold with endogenous practice transmission gives an if-and-only-if criterion for a **hyperbolic locally attracting positive equilibrium**, and a sharp noncritical criterion for **collapse from every mixed initial condition**.
3. Separate protected floors yield an exact admissible effort interval and an explicit tradeoff: more renewal effort increases equilibrium capacity while reducing the available support stock.
4. A finite stochastic counterpart establishes almost-sure eventual extinction under explicit no-restart assumptions. It prevents a deterministic attractor from being misreported as guaranteed indefinite persistence of a finite population.

The contribution is an integrated class theorem and its limits. The exact equations, paid renewal, transmission conflict, rational example, and its previously demonstrated collapse mechanism are inherited from the research record.

## 2. Events, actors, supplied boundaries

Let \(E\geq0\) be usable support and \(C_H,C_L\geq0\) be capacities carried by agents or components following efforts \(u_H>u_L>0\). Put \(C=C_H+C_L\). Capacity can mean a continuous large-population density; it is not an integer count in this deterministic theorem.

The declared local mechanisms are:

- Functioning capacity obtains support at rate \(P(C)\), through a specified external feedstock or opportunity environment.
- Support disappears at rate \(\delta E\).
- Practice \(i\) spends support at rate \(u_i E C_i\), converting that expenditure into new, same-practice capacity at rate \(\eta u_i E C_i\).
- Existing capacity disappears at rate \(\mu C_i\).
- High-effort carriers copy the low practice in response to its current expenditure saving. The conversion flow is
  \[
  J=\kappa E(u_H-u_L)\frac{C_HC_L}{C},\qquad C>0,
  \tag{M1}
  \]
  and \(J=0\) at \(C=0\). Copying conserves total capacity.

Here \(\eta,\mu,\delta>0\) and \(\kappa\geq0\). The copying rule responds to immediate expenditure savings; it does not optimize a correctly specified long-run objective. Its declared observation requirement is access to the relevant expenditure difference and encounters, or a local mechanism implementing the stated rate. An analyst's knowledge of all stocks is not assigned to the agents.

The resulting equations are
\[
\begin{aligned}
\dot E&=P(C)-\delta E-E(u_HC_H+u_LC_L),\\
\dot C_H&=(\eta u_HE-\mu)C_H-J,\\
\dot C_L&=(\eta u_LE-\mu)C_L+J.
\end{aligned}
\tag{M2}
\]

**What is endogenous:** current support, absolute maintaining capacity, expenditures, deaths, replacement by new carriers, practice composition, and therefore the effort actually reproduced by the population. Positive functioning must pay for the replacement of its own carriers. No separate infallible maintenance agent supplies that replacement.

**What remains supplied:** the feedstock and production technology \(P\); conversion efficiency; loss laws; the two practices; inheritance fidelity; the encounter and copying rule; the fixed copying coefficient \(\kappa\); and any authority permitting an outside designer to change these. The model does not derive their historical origin, implementation rights, ethical legitimacy, or the reproduction of an additional institution enforcing \(\kappa\). If such an institution is causally essential, its carriers and expenses need an additional model. Declaring this boundary is part of closure, not a claim that these inputs explain themselves.

For dimensional consistency, if \(E\) has support units and \(C\) capacity units, \(\eta\) and \(\kappa\) have capacity/support units; \(u\) has \(1/(\text{capacity}\cdot\text{time})\) units; and \(P\) has support/time units.

## 3. Production class and a scalar accounting threshold

Assume
\[
P\in C^2([0,\infty)),\quad P(0)=0,\quad P'>0,\quad P''<0,
\quad \sup_{C\geq0}P(C)=P_{\max}<\infty.
\tag{M3}
\]
These hypotheses are restrictions on a model class, not universal claims about ecology, production, cognition, or institutions. Increasing returns, spatial bottlenecks, additional resources, delays, stochastic disasters, and nonconcave technology can require different theorems.

Write
\[
m=\mu/\eta,\qquad h(C)=P(C)-mC,
\qquad H=\max_{C\geq0}h(C).
\tag{M4}
\]
The maximum exists because \(h(C)\to-\infty\). It is a maximum of **one declared physical accounting surplus**, not a utility function aggregating ethical interests.

If \(P'(0)\leq m\), strict concavity implies \(h(C)<0\) for \(C>0\), hence \(H=0\). If \(P'(0)>m\), there is a unique \(C_*>0\) such that
\[
P'(C_*)=m,\qquad H=h(C_*)>0.
\tag{M5}
\]
Indeed, \(P'\) is strictly decreasing and tends to zero: a positive limiting derivative would contradict boundedness. In this case \(h\) increases from zero to \(H\), then decreases to minus infinity. Let \(C_0>C_*\) be its unique strictly positive zero, and define
\[
u_c=\frac{\delta m}{H}.
\tag{M6}
\]
When \(H=0\), no finite effort will support a positive equilibrium; it is convenient to write \(u_c=+\infty\).

## 4. Basic well-posedness and the actual selection clock

For \(C>0\), set \(x=C_H/C\), \(\Delta u=u_H-u_L\), and \(\bar u=u_L+\Delta u x\). Direct summation and the quotient rule give
\[
\begin{aligned}
\dot E&=P(C)-\delta E-\bar u EC,\\
\dot C&=(\eta\bar u E-\mu)C,\\
\dot x&=(\eta-\kappa)E\Delta u\,x(1-x).
\end{aligned}
\tag{M7}
\]
The nonnegative domain is forward invariant, and \(C(t)>0\) for every finite \(t\) whenever \(C(0)>0\). The original copying function extends continuously and locally Lipschitzly at zero capacity. In the transformed equations \(x\) is physically irrelevant at \(C=0\).

For \(V=E+C/\eta\),
\[
\dot V=P(C)-\delta E-mC
\leq P_{\max}-\min(\delta,\mu)V.
\tag{M8}
\]
Thus solutions are bounded and exist for all nonnegative time.

For a mixed initial condition \(0<x(0)<1\), integration gives the exact formula
\[
\operatorname{logit}x(t)=\operatorname{logit}x(0)
+(\eta-\kappa)\Delta u\int_0^tE(s)\,ds.
\tag{M9}
\]
Selection runs on accumulated exposure \(\int E\,dt\), not elapsed time alone. Infinite chronological time need not supply infinite selective exposure. Uniformly changing the clock multiplies the entire vector field by a positive factor and preserves the phase portrait. It cannot turn zero coupling or finite total exposure into the claimed missing causal mechanism.

When \(\kappa\neq\eta\), call
\[
u_s=\begin{cases}u_H,&\kappa<\eta,\\u_L,&\kappa>\eta\end{cases}
\tag{M10}
\]
the **selection-favored effort**. This describes its relative sign when activity occurs; it does not assume that selection completes before the system collapses.

## 5. Exact positive-equilibrium and local-attractor theorem

**Theorem M1.** Under (M3), positive fixed-effort ecological equilibria satisfy
\[
E^*(u)=m/u,\qquad h(C^*)=\delta m/u.
\tag{M11}
\]
For \(H>0\):

- If \(u<u_c\), there are none.
- If \(u=u_c\), there is exactly one, \((m/u_c,C_*)\), with a zero ecological eigenvalue.
- If \(u>u_c\), there are exactly two capacities \(C_-(u)<C_*<C_+(u)<C_0\). The lower equilibrium is a saddle and the upper equilibrium is locally asymptotically stable in the ecological plane.

For the full endogenous system (M7), assume \(\kappa\neq\eta\). A **positive hyperbolic locally asymptotically stable equilibrium exists if and only if**
\[
H>0\quad\text{and}\quad u_s>u_c.
\tag{M12}
\]
It is the upper equilibrium at the selection-favored pure practice. Stability is relative to the nonnegative state space; its basin contains mixed initial compositions.

**Proof.** At a positive ecological equilibrium, \(\dot C=0\) gives \(E=m/u\), and \(\dot E=0\) gives (M11). The shape of \(h\) proves the number and ordering of roots. The ecological Jacobian is
\[
J_{\rm eco}=
\begin{pmatrix}
-\delta-uC^*&P'(C^*)-m\\
\eta uC^*&0
\end{pmatrix}.
\tag{M13}
\]
Its trace is strictly negative and its determinant is \(-\eta uC^*h'(C^*)\). At the lower root the determinant is negative; at the upper root it is positive. At the double root it is zero.

For a positive equilibrium of (M7), \(E>0\) and \(\kappa\neq\eta\) force \(x=0\) or \(x=1\). The third eigenvalue at the favored endpoint is
\[
\lambda_{\rm practice}=-|\eta-\kappa|E^*\Delta u<0;
\tag{M14}
\]
at the other endpoint it is positive. The Jacobian is block triangular because the derivatives of \(\dot x\) with respect to \(E,C\) vanish at these endpoints. Consequently exactly the favored upper equilibrium is hyperbolically attracting. Its stable neighborhood intersects \(0<x<1\), proving the final assertion. ∎

At \(\kappa=\eta\), composition is constant, so the fixed-effort result applies with the initial \(\bar u\). There can be a family of positive equilibria, but no isolated hyperbolic attracting equilibrium of the three-variable system. No selection direction should be assigned at equality.

**Fold and sensitivity.** Since \(h''(C_*)=P''(C_*)<0\), as \(u\downarrow u_c\) from above,
\[
C_\pm(u)=C_*\pm
\sqrt{\frac{2H}{u_c[-P''(C_*)]}}\sqrt{u-u_c}
+o(\sqrt{u-u_c}).
\tag{M15}
\]
This follows by Taylor expansion of \(h(C)=\delta m/u\). One ecological eigenvalue tends to zero while the other tends to \(-\delta-u_cC_*<0\). The equilibrium threshold is a generic saddle-node in this class, with vanishing local restoration rate. This is a proved local bifurcation statement; a global basin boundary has not been located for every member of the class.

## 6. Protected reserves, plural requirements, and a genuine design interval

Let separately specified floors be \(E_{\min}>0\) and \(C_{\min}\geq0\). “Protected attracting equilibrium” means a positive hyperbolic locally asymptotically stable equilibrium with **strict** margins \(E^*>E_{\min}\) and \(C^*>C_{\min}\).

**Corollary M1a.** For \(\kappa\neq\eta\), such an equilibrium exists if and only if
\[
H>0,\qquad u_c<u_s<\frac{m}{E_{\min}},
\qquad C_+(u_s)>C_{\min}.
\tag{M16}
\]
Strict margins and Lyapunov stability imply that some neighborhood of this equilibrium preserves both floors at every future time and converges to it. This is a local all-time statement, not safety from arbitrary starting states.

The capacity condition can be made explicit without solving for \(C_+\):

- If \(C_{\min}\leq C_*\), it adds no restriction beyond \(u_s>u_c\).
- If \(C_*<C_{\min}<C_0\), it is equivalent to
  \[
  u_s>\frac{\delta m}{h(C_{\min})}.
  \tag{M17}
  \]
- If \(C_{\min}\geq C_0\), no finite effort works.

**Proof.** The equilibrium support formula gives the upper effort bound. On \((C_*,C_0)\), \(h\) strictly decreases, so comparing \(h(C_+)\) with \(h(C_{\min})\) proves (M17). The other cases follow from the root ordering. ∎

Implicit differentiation on the upper branch gives
\[
\frac{dC_+}{du}=\frac{-\delta m/u^2}{h'(C_+)}>0,
\qquad \frac{dE^*}{du}=-m/u^2<0.
\tag{M18}
\]
Consequently increasing renewal effort can improve one protected condition while worsening another. The admissible interval can be empty. This supplies a concrete reason not to identify “more maintenance” with a universal ethical or dynamical improvement direction.

## 7. A global collapse theorem and unavoidable depleted basins

**Theorem M2.** Suppose \(C(0)>0\), \(E(0)\geq0\), \(0<x(0)<1\), and \(\kappa\neq\eta\). If \(H=0\), or if \(H>0\) and \(u_s<u_c\), then
\[
E(t)\to0,\quad C(t)\to0,\quad
\int_0^\infty E(t)\,dt<\infty.
\tag{M19}
\]
The stocks decay exponentially, allowing a harmless polynomial factor at a coinciding linear decay rate. The limiting \(x\) is strictly interior. It increases when \(\kappa<\eta\) and decreases when \(\kappa>\eta\), but it does not reach the favored boundary.

**Proof.** First suppose \(\int_0^\infty E<\infty\). From \(\bar u\leq u_H\),
\[
C(t)=C(0)\exp\!\left(\eta\int_0^t\bar u(s)E(s)\,ds-\mu t\right)
\leq K_1e^{-\mu t}.
\tag{M20}
\]
Concavity and \(P(0)=0\) give \(P(C)\leq P'(0)C\), and \(\dot E\leq P'(0)C-\delta E\). Variation of constants proves decay of \(E\) and integrability.

Now suppose instead \(\int_0^\infty E=\infty\). Formula (M9) implies \(\bar u\to u_s\). If \(H>0\) and \(u_s<u_c\), choose \(u_s<\widehat u<u_c\); eventually \(\bar u\leq\widehat u\). If \(H=0\), take \(\widehat u=u_H\), which dominates \(\bar u\) at all times. With any fixed reference capacity \(C_{\rm ref}>0\), define
\[
W=E+C/\eta+\frac{\delta}{\eta\widehat u}
\log(C/C_{\rm ref}).
\tag{M21}
\]
For all sufficiently large times,
\[
\begin{aligned}
\dot W
&=h(C)-\frac{\delta m}{\widehat u}
+\delta(\bar u/\widehat u-1)E\\
&\leq H-\frac{\delta m}{\widehat u}
=-\gamma<0.
\end{aligned}
\tag{M22}
\]
Since \(E+C/\eta\geq0\), this upper bound on \(W\) bounds \(\log C\) above by an affine function with strictly negative slope. Thus \(C\) decays exponentially. The same support comparison then proves \(E\) integrable, contradicting the supposed infinite exposure. Only the first case is possible. Finally, finite exposure in (M9) gives an interior limiting composition, with the asserted direction. ∎

“Interior limiting composition” does not mean a surviving mixed population: absolute capacity vanishes. In the deterministic equations extinction is asymptotic, while every positive protected floor is eventually crossed at a finite time.

**Sharp noncritical consequence.** For fixed parameters satisfying the theorem's model assumptions and \(\kappa\neq\eta\), exclude the critical equality \(u_s=u_c\). Then **all mixed initial conditions collapse if and only if \(u_s<u_c\)**, using \(u_c=+\infty\) when \(H=0\). Necessity follows from Theorem M1: if \(u_s>u_c\), an open set of mixed initial conditions instead approaches the positive attracting equilibrium. The critical equality is intentionally not classified by this global dichotomy.

**Proposition M3: a depleted basin exists even on the viable side.** Choose \(\overline E>0\) with \(\eta u_H\overline E<\mu\). By continuity at zero choose \(\overline C>0\) with \(P(\overline C)<\delta\overline E\). Then
\[
0\leq E\leq\overline E,\qquad
0<C\leq\overline C,\qquad 0\leq x\leq1
\tag{M23}
\]
is forward invariant and every trajectory in it has \(E,C\to0\).

At the upper support face, \(\dot E\leq P(\overline C)-\delta\overline E<0\). Throughout the box, \(\dot C/C\leq\eta u_H\overline E-\mu<0\), so capacity decays exponentially. The previous support comparison gives \(E\to0\). ∎

Thus favorable selection and a positive attractor do not imply rescue from depletion. When (M12) holds, positive and depleted basins coexist. In the bistable rational example, changing \(\kappa\) through \(\eta\) can also change the selected endpoint from a supercritical practice to a subcritical one. That change eliminates positive local attraction and implies collapse from every mixed start on the subcritical side; it does not claim that every start was viable on the other side.

## 8. Exact rational witness and independent numerical check

Take
\[
P(C)=\frac{aC}{1+C/K},\qquad a,K>0.
\tag{M24}
\]
If \(a>m\), direct maximization gives
\[
C_*=K(\sqrt{a/m}-1),\quad
H=K(\sqrt a-\sqrt m)^2,\quad
u_c=\frac{\delta m}{K(\sqrt a-\sqrt m)^2}.
\tag{M25}
\]
Writing \(A=a/m\) and \(d=\delta/(uK)\),
\[
C_\pm(u)=\frac K2\left[A-1-d\pm
\sqrt{(A-1-d)^2-4d}\right],\quad E^*=m/u.
\tag{M26}
\]
The condition for two distinct positive roots is \(A>(1+\sqrt d)^2\); equality gives one positive double root. When \(a\leq m\), \(H=0\), and the displayed positive-maximizer formula does not apply.

For \(a=9\), \(K=\delta=\eta=\mu=1\), \(u_L=1/10\), \(u_H=1/2\),
\[
H=4,\quad u_c=1/4,\quad C_*=2,\qquad
(E_H^*,C_{H,+}^*)=(2,3+\sqrt7).
\tag{M27}
\]
The high equilibrium's ecological eigenvalues are approximately \(-3.097167541\) and \(-0.725708115\). Its practice eigenvalue is \(-0.4\) at \(\kappa=0.5\) and \(+0.4\) at \(\kappa=1.5\). The low effort is subcritical. Theorem M2, rather than simulation, establishes collapse of every mixed start when \(\kappa=1.5\).

An independent numerical check of the inherited witness used the initial state \((E,C,x)=(2,3+\sqrt7,0.99)\), integration to \(t=200\), relative tolerance \(10^{-10}\), absolute tolerance \(10^{-12}\), and maximum step \(0.1\). For \(\kappa=0.5\), it approached \((2,5.645751311,1)\). For \(\kappa=1.5\), it returned \(E\approx3.32\times10^{-77}\), \(C\approx2.02\times10^{-80}\), and \(x\approx0.00146664561\); support first rose to approximately \(4.63336\). The endpoint's minute positive stocks are numerical values, not a proof of finite-time extinction or a certified precision claim at those magnitudes. The monotone integral identity and global argument establish the limiting result.

A separate plural-floor witness keeps the same \(P,\delta,\eta,\mu\) but permits the selection-favored effort to be designed. Require \(E^*>3/2\) and \(C^*>6\). Since \(h(6)=12/7\), the exact interval is
\[
\frac7{12}<u_s<\frac23.
\tag{M28}
\]
For \(u_s=5/8\),
\[
E^*=8/5,\qquad C_+^*=\frac{16+6\sqrt6}{5}
\approx6.139387691,
\tag{M29}
\]
so both strict floors hold. At \(u_s=1\), capacity rises to \((7+3\sqrt5)/2\approx6.854101966\), but support falls to \(E^*=1\), violating its floor. The composition mechanism must actually favor the chosen effort, and its basin must be reached; choosing the numerical effort alone does not implement either condition.

## 9. Finite stochastic carriers: a different infinite-horizon conclusion

**Theorem M4.** Consider a nonexplosive stochastic carrier process with these properties:

1. Its carrier count is always \(0\leq N\leq N_{\max}<\infty\).
2. Total capacity-creating birth intensity is bounded above by \(B_{\max}<\infty\).
3. Every extant carrier has death intensity at least \(\mu_0>0\), allowing independent baseline death clocks of rate \(\mu_0\) plus nonnegative additional death hazards. Ordinary individually labeled single-death processes with those intensity bounds admit this construction.
4. Copying or internal state changes preserve the count; no further event increases it except the bounded births. Zero carriers cannot regenerate themselves, and there is no immigration, protected seed, or external restart.

Then the extinction time \(T_0=\inf\{t:N(t)=0\}\) is finite almost surely. For any block length \(T>0\),
\[
p_T=e^{-B_{\max}T}(1-e^{-\mu_0T})^{N_{\max}}>0,
\qquad
\Pr(T_0>kT)\leq(1-p_T)^k.
\tag{M30}
\]

**Proof.** Construct births by thinning an independent dominating Poisson clock of rate \(B_{\max}\), and construct each current carrier's baseline death clock independently. Conditional on any past at the start of a block, the event of no proposed births and expiry of every baseline death clock by its end has probability at least \(p_T\). Additional deaths can only assist this event. On the event there are no new carriers and all existing ones disappear, so extinction has occurred. Repeating the conditional bound yields (M30); independence of extinction events across blocks is unnecessary. Taking \(k\to\infty\) proves almost-sure extinction. ∎

The bound is deliberately crude and can be extremely small. It is not an estimate of a useful operational lifetime. Finite-horizon survival probabilities, rare escape rates, and quasi-stationary lifetimes require further analysis of a specified stochastic implementation.

The theorem applies even when internal renewal sustains a deterministic positive equilibrium, provided the stochastic realization satisfies its hypotheses. It does **not** apply to every uncapped branching process, models with exact immortal seeds, or systems with recurrent restart. It proves carrier extinction, not literal finite-time disappearance of a continuous residual resource. If production ceases at zero carriers and support obeys \(\dot E=-\delta E\), residual support subsequently tends to zero.

Large-population deterministic limits can approximate finite time intervals under appropriate scaling. They are generally not exact equations for nonlinear finite-population expectations, and finite-horizon convergence does not justify interchanging the infinite-time and infinite-population limits. This distinction is established population-process methodology; see [Champagnat, Ferrière, and Méléard, *Individual-based probabilistic models of adaptive evolution and various scaling approximations*](https://arxiv.org/abs/math/0510453).

## 10. Partial observation, robust exclusions, and actual implementation

The autonomous mechanism results analyze actual installed rates. They do not require a controller to observe the analyst's full state, and they do not grant one that information. An observer who cannot distinguish candidate production or loss mechanisms may be unable to choose a safe design even when each candidate admits one.

The distinction is exact:
\[
\forall M\in\mathfrak M\;\exists d_M\;\text{protected attractor in }M
\quad\not\Rightarrow\quad
\exists d\text{ permitted by the common information}\;
\forall M\in\mathfrak M\;\text{protected attractor in }M.
\tag{M31}
\]
The right side additionally requires a common implementable choice. Reaching its basin and staying safe before arrival are further properties. An adaptive designer needs the actual observation history, intervention permissions, time and resource costs, and a feasible policy; the response-profile machinery of [OPTIMAL-FOUNDATION](../OPTIMAL-FOUNDATION.md) preserves these distinctions but does not manufacture missing information.

One uncertainty-robust impossibility certificate follows directly from (M22). Suppose \(\eta,\mu,\delta\) are known and actual production may vary, but always satisfies \(P_t(C)\leq\overline P(C)\), where \(\overline P(0)=0\), \(\overline P(C)\leq a_0C\) near zero, and
\[
\overline H=\sup_{C\geq0}[\overline P(C)-mC]<\infty.
\tag{M32}
\]
Suppose all actual permitted effort obeys \(\bar u(t)\leq\widehat u\), and
\[
\overline H<\delta m/\widehat u.
\tag{M33}
\]
Then the same \(W\) has a uniformly negative derivative, forcing exponential capacity decay and then support decay. The certificate allows time variation and arbitrary observation-limited effort choices within this bound. It cannot be repaired by better inference or a different choice within the same bounded effort set. It is a necessary-resource exclusion, not a sufficient condition for successful design when the inequality reverses.

The certificate presumes existence of the solutions being discussed and the original support/capacity accounting. Outside subsidies, bootstrap births, or stock transfers that add terms to that accounting must be included before applying it.

## 11. Exact scope of closure and remaining checks

This mechanism class closes a substantive mathematical gap: **specified local loss, conversion, inheritance, and copying events imply exact conditions for persistent attracting functioning, global collapse, and coexistence of basins**. Persistent capacity is not inserted as a property of a supplied transition table. Its agents must be regenerated by the same support flows whose future availability their practices change.

It does not close every question by renaming it “selection.” The remaining supplied causal mechanisms are itemized in Section 2. The results are compatible with multiple, separate protected conditions; they do not derive ethical standing or legitimate authority from persistence. A higher-level maintaining institution requires the same event-and-expense analysis if the application depends on it, and some applications may need different mechanisms entirely.

Specific limits and follow-up checks are:

- The global equality case \(u_s=u_c\) is not classified. The positive equilibrium there is nonhyperbolic, so it lies outside the exact robust-attractor theorem as stated.
- The theorem establishes positive and depleted basins, but does not provide every member's complete basin boundary or a globally safe rescue policy.
- Fixed efforts, perfect inherited practice, one support stock, concave production, and immediate conversion are consequential assumptions. Mutation, multiple resources, delays, endogenous copying institutions, and spatial encounter restrictions require new analysis rather than an assertion that this proof covers them.
- The finite stochastic theorem supplies a rigorous infinite-horizon warning and a coarse bound, not measured extinction risk for a real AI organization, ecosystem, or institution.
- Applying the class across domains requires measured mechanisms and discriminating interventions. These equations and numerical witnesses are theoretical constructions, not evidence that the same fitted causal law governs every proposed domain.

Environmental feedback in evolutionary games already has a substantial primary literature; for example [Tilman, Plotkin, and Akçay, *Evolutionary games with environmental feedbacks*](https://pmc.ncbi.nlm.nih.gov/articles/PMC7021758/) analyzes strategic/environmental coupling and timescale-dependent regimes. The present memo claims the stated derivations and their integration into this programme. It does not claim to have originated eco-evolutionary feedback, bistability, selection equations, stochastic extinction, or a globally optimal theory of all coordination.

**Internal mathematical cross-review.** A separate agent checked the threshold, Jacobian, global-collapse proof, fold expansion, protected-floor interval, stochastic extinction bound, and uncertainty certificate. Its requested distinction between two distinct roots and the critical double root has been incorporated. This is an internal preparation check, not independent specialist peer review.
