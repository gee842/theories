# Formal supplement: selection, correction, and cooperative choice

Version 5.0, 3 October 2026. Companion to [the manuscript](THEORY.md).

This supplement supplies eleven connected but distinct mathematical modules. Each result holds in its stated model. A shared symbol or an intuitively similar mechanism does not establish an interface between models. In particular, an equilibrium calculation is not a growth law; lost advantage is not lost survival; a safety property is not a complete account of political legitimacy. These results establish neither that every competitive policy fails nor that one institutional arrangement is the unique exit.

The proofs below are self-contained. [checks_v5.py](checks_v5.py) checks selected identities, boundaries, and counterexamples using the Python standard library; [checks_v5.log](checks_v5.log) records the run. Computation supplements the proofs and does not measure real institutions. Numbering M1–M11 is stable for references from the manuscript. Historical sources and novelty comparisons belong to the manuscript's evidence and contribution registers; the elementary constructions here are not claims of mathematical originality.

## M1. Relative selection and mean load

Let finitely many practices have fixed loads \(e_k\), shares \(p_k\ge0\), \(\sum_kp_k=1\), and payoffs

\[
\pi_k(t)=\phi_k(t)+[\nu-\tau(t)]e_k+G(t).
\]

Here \(\nu>0\) is private benefit per load unit, \(\tau\) is effective liability, \(\phi_k\) collects other advantages, and \(G\) is an identical additive common consequence. Replicator selection is \(\dot p_k=p_k(\pi_k-\bar\pi)\), with \(\bar\pi=\sum_kp_k\pi_k\). Define mean load \(E=\sum_kp_ke_k\).

**M1.1.** The common term cancels from the vector field, and

\[
\dot E=(\nu-\tau)\operatorname{Var}_p(e)+\operatorname{Cov}_p(e,\phi).
\]

If all \(\phi_k\) are equal and both shares are positive,

\[
\frac{d}{dt}\log\frac{p_k}{p_l}=(e_k-e_l)(\nu-\tau).
\]

Consequently, if \(B(t)=\int_0^t(\nu-\tau(s))ds\to+\infty\), mean load converges to the greatest load initially represented. If \(B(t)\to-\infty\), it converges to the smallest initially represented load. If \(B\) has a finite real limit, every initially positive share has a positive limit.

**Proof.** Subtracting the mean removes \(G\). Then \(\dot E=\sum_kp_ke_k(\pi_k-\bar\pi)=\operatorname{Cov}_p(e,\pi)\), giving the identity. With equal \(\phi\), integration gives

\[
p_k(t)=\frac{p_k(0)e^{e_kB(t)}}{\sum_lp_l(0)e^{e_lB(t)}}.
\]

Divide numerator and denominator by the largest or smallest represented exponential to obtain the limits. Zero shares remain zero. ∎

This is blindness of a particular selection rule to an identical additive term, not blindness of people or systems to information. A common consequence may change feasible actions, admission rules, transmission, liability, or heterogeneous private losses; those changes do not cancel. Under a different rule, cancellation must be checked again.

Positive mean-load growth also does not mean that the highest-load practice grows. For equal shares, \(e=(0,0.9,1)\), \(\phi=(0,10,0)\), and \(\nu-\tau=1\), mean load rises by \(1.091111\ldots\), while the share of the practice with \(e=1\) falls at rate \(-0.988889\ldots\). The covariance identity describes a mean; extreme-type dominance needs M1.1's additional assumptions.

## M2. Faithful AI in a harmful principal game

There are \(n\ge2\) human principals. Principal \(i\) chooses \(a_i\in\{0,1\}\), restraint or one increment of racing. Its faithfully implemented objective is

\[
u_i=b\left(a_i-\frac{1}{n-1}\sum_{j\ne i}a_j\right)-ca_i-d\sum_ja_j,
\qquad c,d>0.
\]

The terms represent relative standing, private cost, and a shared loss experienced by each principal. AI contributes no independent objective, deception, or departure from the principal's constraints; humans can retain every decision.

**M2.1.** If \(b>c+d\), racing is strictly dominant and all-racing is the unique Nash equilibrium. Nevertheless, all-restraint strictly Pareto-dominates it and maximizes summed objectives.

**Proof.** Changing one's action from zero to one changes one's objective by \(b-c-d>0\), independently of others. Hence every equilibrium has all actions one. Relative-standing terms sum to zero, because each action appears negatively \(n-1\) times with coefficient \(b/(n-1)\). Thus

\[
\sum_iu_i=-(c+nd)\sum_ia_i.
\]

All-restraint gives each principal zero; all-racing gives each \(-c-nd<0\). ∎

This establishes insufficiency of principal fidelity under these incentives, not actual parameter values or inevitable collapse. A marginal rule that adds an enforceable private cost \(\tau a_i\), with \(\tau>b-c-d\), reverses the dominance comparison. That observation concerns incentives; financing, implementation, and welfare accounting of a tax or restriction require separate analysis. Repetition, observability, heterogeneous stakes, and bargaining are not excluded by this one-period game.

## M3. When control over selection is itself selected

A carrier has a fixed local share profile \(y=p\bar y\), where \(p\ge0\) measures size and \(\bar y\ge0\) describes its distribution across domains. An investment \(q\ge0\) builds rule support keyed to that carrier. During a comparison horizon \(T>0\), with the profile held fixed, support begins at zero and obeys

\[
\dot z_i=\epsilon_i\left(\chi q\sum_j\hat b_{ij}y_j-d_iz_i\right),
\qquad \epsilon_i,d_i>0,\quad\hat b_{ij}\ge0.
\]

The appropriable fraction is \(\chi\in[0,1]\). Support pays \(\sum_i a_iy_iz_i\), with \(a_i>0\), while investment costs

\[
C(q)=fq+\frac{\gamma q^{1+\eta}}{1+\eta},
\qquad f\ge0,\quad\gamma,\eta>0.
\]

Here \(f\) is a persistent **linear marginal cost**, not a lump-sum entry cost. Let

\[
L_i=1-\frac{1-e^{-\epsilon_id_iT}}{\epsilon_id_iT},\qquad
B=\sum_{ij}\frac{a_iL_i\hat b_{ij}}{d_i}\bar y_i\bar y_j.
\]

**M3.1.** Horizon-average net return is

\[
F(q)=\chi p^2Bq-C(q),\qquad
F'(q)=\chi p^2B-f-\gamma q^\eta.
\]

Its unique maximizer is

\[
q^*=\left(\frac{(\chi p^2B-f)^+}{\gamma}\right)^{1/\eta}.
\]

If \(\chi B>0\), positive investment occurs exactly when \(p>\sqrt{f/(\chi B)}\); equality gives \(q^*=0\). With \(f=0\), the initial marginal return is positive for every \(p>0\). If \(\chi B=0\), investment has no positive return in this model.

**Proof.** Solving the linear support equation gives
\(z_i(t)=\chi q\sum_j\hat b_{ij}y_j(1-e^{-\epsilon_id_it})/d_i\). Averaging over \([0,T]\), multiplying by \(a_iy_i\), and summing gives \(\chi p^2Bq\). The derivative decreases strictly for positive \(q\), tends to minus infinity, and crosses zero exactly at the stated positive optimum when the intercept is positive. ∎

For a faithful, variation-preserving replicator population of investment traits with frequencies \(\mu_r\) and payoffs \(F(q_r)\),

\[
\frac{d}{dt}\bar q=\operatorname{Cov}_\mu(q,F(q))
=\frac12\sum_{r,s}\mu_r\mu_s(q_r-q_s)[F(q_r)-F(q_s)].
\]

Thus mean investment increases when \(F\) is increasing on the represented support, strictly if distinct positively weighted traits have distinct increasing payoffs. This is a selection result conditional on available variants and faithful transmission. Trait mutation, entry barriers, sanctions, institutional inheritance, or selection at another level require additional terms. It does not prove convergence to \(q^*\), nor a full strategic equilibrium in which shares and other investments move simultaneously.

The square of share arises because share generates support and also determines how much of its benefit is received. Under equal within-domain size across \(m\) domains and common diagonal/off-diagonal coefficients, the return coefficient is proportional to
\(p^2m[\beta_{\rm diag}+(m-1)\beta_{\rm cross}]\). At fixed per-domain share, positive cross-domain terms produce superlinear scope returns. At fixed total size \(mp\), increasing scope raises this expression only when \(\beta_{\rm cross}>\beta_{\rm diag}\).

An unkeyed correction effort that changes a benefit identically for two otherwise identical practices but costs only its contributor has the reverse selection comparison: the contributor's relative payoff is lower by its cost. This limited public-good result does not rule out private reliability gains, remuneration, reputation, mandated funding, or collective institutions that change who pays and benefits.

## M4. Correction rates, cost reductions, and concentration

Consider M3 in the long-horizon regime, with a common correction rate \(d\), no linear cost, and a fixed return coefficient \(H\), with \(\chi H>0\). Then

\[
q^*=\left(\frac{\chi H}{\gamma d}\right)^{1/\eta}.
\]

Suppose an evaluation domain has baseline inbound support \(A\ge0\), cultivated conversion coefficient \(B_0>0\), and resistance \(c>0\). Its normalized steady support is

\[
R(d,\gamma)=\frac{A+B_0q^*}{cd}
=\frac{A}{cd}+D\gamma^{-1/\eta}d^{-(1+1/\eta)},
\quad D=\frac{B_0(\chi H)^{1/\eta}}c>0.
\]

The condition \(R<1\) is the full-row certificate interpreted dynamically in M5. For \(\eta=1\), the threshold is

\[
d^*(\gamma)=\frac{A+\sqrt{A^2+4cB_0\chi H/\gamma}}{2c}.
\]

**M4.1.** If \(\gamma(t)=\gamma_0e^{-gt}\), \(d(t)=d_0e^{\alpha t}\), with \(g,\alpha\ge0\), then

\[
R(t)=\frac{A}{cd_0}e^{-\alpha t}
+D\gamma_0^{-1/\eta}d_0^{-(1+1/\eta)}
e^{[g-(1+\eta)\alpha]t/\eta}.
\]

If \(\alpha\ge g/(1+\eta)\), an initial strict certificate remains strict. If \(\alpha<g/(1+\eta)\), \(R(t)\to\infty\). When independent correction's budget grows at rate \(b\) and its unit cost falls at rate \(g_c\), the assumed production relation \(d\propto\text{budget}/\text{unit cost}\) gives \(\alpha=b+g_c\).

**Proof.** Substitute the exponential paths. In the first case both terms are nonincreasing. In the second case the positive cultivated term diverges. The budget identity follows directly from the stated production relation. ∎

Thus AI-assisted correction can preserve the certificate. For example, \(g_c=g\) and \(b\ge0\) satisfy the rate inequality. Nothing here derives a bound on \(d\) from human understanding \(U\). That needs a separate production relation including authority, response time, reusable certificates, and resources.

Two scope qualifications matter. First, \(q^*\) is an optimum, not a demonstrated adaptive trajectory. Second, failure of a moving steady-state certificate is not by itself a proof of realized capture in a time-varying system. Applying M5 requires its fixed-parameter conditions or an actual eventual bound on realized support. Tracking cannot be assumed silently.

With persistent \(f>0\), the optimum becomes
\(q^*=[(\chi H/d-f)^+/\gamma]^{1/\eta}\). A constant rate
\(d>\max\{A/c,\chi H/f\}\) therefore eliminates cultivated investment and keeps \(R<1\), regardless of further reductions in \(\gamma\). This sufficient floor concerns the stated linear cost model.

**M4.2.** If independent carriers have shares \(p_k\) summing to one and selected capacities \(q_k^*=Qp_k^{2/\eta}\), their total cultivated conversion proportional to \(\sum_kp_kq_k^*\) is

\[
Q\sum_kp_k^{1+2/\eta}.
\]

Equal division into \(k\) genuinely independent parts gives \(Qk^{-2/\eta}\). At \(\eta=1\), this is a third moment, not the Herfindahl second moment. If the cultivated term otherwise grows as \(e^{\kappa t}\), \(\kappa>0\), this fixed division delays its crossing of a fixed threshold by \(2\log k/(\eta\kappa)\); it does not eliminate the eventual crossing. These statements follow by substitution. Common control, scale-dependent parameters, dynamic fragmentation, and removal of a conversion channel are different mechanisms.

## M5. A field of selectors: configurations, certificates, and reform

For \(i=1,\ldots,D\), let \(x_i\in[0,1]\) be a practice's decision share and \(z_i\ge0\) its rule support:

\[
\dot x_i=\zeta_ix_i(1-x_i)(a_iz_i-c_i),\qquad
\dot z_i=\epsilon_i\left(\sum_jb_{ij}x_j-d_iz_i\right).
\]

All displayed rates and \(a_i,c_i,d_i\) are positive; \(b_{ij}\ge0\). Parameters are fixed. Define \(R_{ij}=a_ib_{ij}/(c_id_i)\) and \(s_i(C)=\sum_{j\in C}R_{ij}\). “Capture” in this model means \(x_i\to1\), not an empirical verdict about any institution.

**M5.1.** The state space is forward invariant, the flow preserves componentwise order, and
\(\limsup z_i\le\sum_jb_{ij}/d_i\). If a full inbound row satisfies \(\sum_jR_{ij}<1\), then \(x_i\to0\) whenever \(x_i(0)<1\), regardless of the other domains.

**Proof.** At \(x_i=0,1\), its derivative vanishes; at \(z_i=0\), its derivative is nonnegative. Variation of constants bounds support by the solution driven with all \(x_j=1\). All cross-coordinate derivatives are nonnegative on the state space. A first-crossing comparison, or its strictly perturbed version followed by a limit, therefore preserves order. With a strict row margin, eventually \(a_iz_i-c_i\le-\delta\) for some \(\delta>0\). For \(0<x_i<1\),
\(d\log[x_i/(1-x_i)]/dt=\zeta_i(a_iz_i-c_i)\), which tends to minus infinity after integration. If \(x_i(0)=0\), it remains zero. ∎

The boundary exception \(x_i=1\) is substantive: pure replicator dynamics cannot reintroduce an absent alternative. A reform or entry mechanism is needed to leave that boundary.

**M5.2.** For every subset \(C\), the corner configuration \(Z_C\), with \(x_i=1\) on \(C\), zero elsewhere, and \(z_i=\sum_{j\in C}b_{ij}/d_i\), is an equilibrium. If no \(s_i(C)=1\), it is locally asymptotically stable exactly when

\[
s_i(C)>1\ (i\in C),\qquad s_i(C)<1\ (i\notin C).
\]

**Proof.** At a corner, the top-right Jacobian block is zero because \(x_i(1-x_i)=0\). The eigenvalues are \(-\epsilon_id_i\), together with \(-\zeta_ic_i[s_i(C)-1]\) on \(C\) and \(\zeta_ic_i[s_i(C)-1]\) outside it. All are negative exactly under the displayed inequalities. A positive eigenvalue has a feasible inward perturbation and makes the corner unstable. Equality is nonhyperbolic and is deliberately left undecided. ∎

Testing only a domain's own influence cannot certify it. For example,
\(R=\begin{pmatrix}.4&.8\\.8&.4\end{pmatrix}\)
has both self-conversions below one but a stable full-capture corner. The sum must include external, rival, and shared-source conversion, insofar as those channels fit this model.

**M5.3.** Suppose domains in a set \(C\) actually satisfy \(x_j\to1\). If \(s_i(C)>1\) and \(x_i(0)>0\), then \(x_i\to1\). Repeating this rule generates a guaranteed cascade. A reform resetting \(x_i\) or \(z_i\), while leaving such an inbound set captured, is eventually reabsorbed if \(i\) is subsequently reseeded.

**Proof.** For any small \(\varepsilon>0\), all seed shares eventually exceed \(1-\varepsilon\). The linear support equation then has eventual lower limit at least \((1-\varepsilon)\sum_{j\in C}b_{ij}/d_i\). Choose \(\varepsilon\) so that the implied selection margin is strictly positive. Integrating the log-odds equation proves convergence to one. Induct over newly added domains. A finite reset does not alter the eventual lower bound; exact zero without reseeding is excluded. ∎

This theorem is about seeds known to persist. It does not declare every possible seed self-sustaining or characterize every basin of attraction.

**M5.4. A scoped pause result.** In one dimension, write \(R=ab/(cd)>1\), \(x_*=1/R\), \(z_*=c/a\). During a pause hold \(x=x_p\in(0,1)\), while support follows \(\dot z=\epsilon(b_px_p-dz)\). Restore the original dynamics afterward.

With ordinary conversion \(b_p=b\), a sufficiently long pause leads after release to capture if \(x_p>x_*\), and absence if \(x_p<x_*\). With insulated conversion \(b_p=0\), absence holds for sufficiently long pauses for every \(x_p\le x_*\), and also for some open interval immediately above \(x_*\).

**Proof.** During the pause, \(z\to b_px_p/d\). In the ordinary case, this limit is above \(z_*\) exactly when \(x_p>x_*\). The rectangle \(x\ge x_p,z\ge z_*\) is forward invariant; support eventually stays strictly above \(z_*\), so log odds diverge upward. Below the threshold, the rectangle \(x\le x_p,z\le z_*\) is invariant and yields the reverse result. A sufficiently long finite pause places the state in the appropriate strict rectangle. For insulation, \(z\to0\). Starting at \((x_*,0)\), initially \(\dot x<0\), and for a short time \(z<z_*\); hence the path enters a strict lower rectangle and converges to zero. Continuous dependence provides a neighborhood of \((x_*,0)\) with the same property, including some \(x_p>x_*\) and sufficiently small positive support. ∎

This establishes that what continues during a pause can change its outcome. It is not a theorem about arbitrary multidomain pauses, and it supplies no universal duration.

## M6. Correction architectures and net risk

Suppose an error must pass \(k\) reporting or correction steps, and let \(f_j\) be the conditional probability that step \(j\) succeeds given all earlier required steps succeeded. The success probability is exactly \(\prod_jf_j\), by the chain rule; independence is unnecessary. If each equals \(f<1\), reliability is \(f^k\).

If instead each of \(k\) monitors can directly block the error, and their misses are independent conditional on the error, with individual detection probability \(f\), combined detection is \(1-(1-f)^k\). Conditional common-cause errors can make that independence false. At \(f=.9,k=6\), the two expressions are .531441 and .999999. Choosing the formula requires specifying intervention topology, not calling both arrangements “layers.”

For an actionable institutional correction, define successive events: relevant evidence is obtained, the error is detected, an authorized decision is made, and that decision is executed in time. If their successive conditional success probabilities are \(r_1,r_2,r_3,r_4\), correction succeeds with probability \(\prod_jr_j\). This identity locates bottlenecks; it does not say every safety architecture requires precisely this chain or that every stage has a constant failure probability. Understanding coverage and executable correction remain distinct quantities.

**M6.1.** If primary failure has conditional probability at most \(q_t\), correction misses conditional on that failure with probability at most \(m_t\), and a new harmful failure introduced by correction has probability at most \(r_t\), residual terminal risk is at most \(q_tm_t+r_t\).

**Proof.** Terminal failure is contained in the union of unblocked primary failure and introduced harmful failure. Conditional multiplication bounds the first event by \(q_tm_t\); the union bound adds \(r_t\). Independence between the two events is unnecessary. ∎

For example, \(q_t=.1\), \(m_t=2^{-t}\), \(r_t=.01\,2^{-t}\), \(t\ge1\), give residual risk at most \(.11\,2^{-t}\). The corrector remains fallible, yet its risks are summable and probability of avoiding the specified loss is at least .89. A claim that correction merely relocates equal danger must exclude this structure with quantitative premises. Neither opacity nor fallibility alone does so. Conversely, a proof of one safety invariant need not establish contestability, consent, or retained human agency.

## M7. Conditional residual hazards and freezing

Fix a terminal event, an affected actor or population, and a policy. Let \(S_t\) mean no terminal event through period \(t\), with \(S_0\) certain. On each surviving history let \(q_t\) be the conditional probability of terminal loss next period, after the actual safeguards being evaluated.

**M7.1.** If deterministic \(\ell_t\in[0,1]\) satisfy \(q_t\ge\ell_t\) on every surviving history, then

\[
\Pr(S_H)\le\prod_{t=0}^{H-1}(1-\ell_t)
\le\exp\left(-\sum_{t=0}^{H-1}\ell_t\right).
\]

Thus a divergent sum forces zero infinite-horizon survival. If instead \(q_t\le b_t<1\) on every surviving history and \(\sum_tb_t<\infty\), infinite-horizon survival is positive.

**Proof.** Conditional expectation gives \(\Pr(S_{t+1})=E[1_{S_t}(1-q_t)]\). Bound the factor and iterate. For the upper estimate use \(1-x\le e^{-x}\). For the lower statement, iteration gives survival at least \(\prod_t(1-b_t)\). Eventually \(b_t\le1/2\), and \(-\log(1-b_t)\le2b_t\); the tail log product is finite and every finite initial factor is positive. Continuity of probability for decreasing events completes both limits. ∎

There is no independence assumption. A finite delay followed by the same nonsummable lower-bound sequence preserves the zero-survival conclusion, provided the resumed process still has infinitely many rounds and the same conditional bound. A pause that changes the hazard, action set, or termination rule is a different policy.

Let \(Y_t>0\) measure dangerous demand and \(U_t\ge0\) effective coverage in the same units, and write \(u_t=(1-U_t/Y_t)^+\). If actual residual risk satisfies \(q_t\ge h u_t\), \(h>0\), uniformly across surviving histories, a deterministic nonsummable lower bound on \(u_t\) suffices for failure. In particular, deterministic or history-uniform exponential growth of \(Y\) against subexponential \(U\) gives \(u_t\to1\) uniformly and eventually a constant positive bound.

The premise concerns **actual residual terminal risk**, not the count of nominally dangerous capabilities. It must be re-established after changing correction architecture and separately for propagation to another actor. The result gives a risk lower bound, not equality with \(h\). It gives a necessary coverage condition for positive survival, not sufficiency: even summable \(u_t\) is compatible with another persistent hazard. Nor does summability require exact catch-up. Take \(u_t=1/(t+2)^2\), \(U_t=t+1\), \(Y_t=U_t/(1-u_t)\); coverage remains strictly incomplete forever.

**M7.2. Freeze formulas.** For a continuous-time calculation, assume an actual conditional terminal intensity at least \(h(1-U(t)/Y)^+\) after freezing a fixed dangerous demand \(Y>0\). Conditional survival over that phase is at most \(e^{-hI}\), where \(I=\int_0^\infty(1-U(t)/Y)^+dt\). This is the intensity convention, not an exact formula for discrete per-period probabilities.

If \(U(t)=U_0+vt\), \(v>0\), then

\[
I=\frac{(Y-U_0)_+^2}{2vY}.
\]

If \(U(t)=U_0e^{gt}\), \(g>0,U_0>0\), then \(I=0\) for \(Y\le U_0\), and otherwise, with \(\Gamma=Y/U_0>1\),

\[
I=\frac{\log\Gamma-1+1/\Gamma}{g}.
\]

**Proof.** In the linear case, integrate the linearly declining uncovered share until \((Y-U_0)/v\), if positive. In the exponential case, integrate until \(\log\Gamma/g\). The survival inequality follows by integrating the conditional intensity bound. ∎

The frozen quantity is \(Y\), not all behavior \(X\). If only \(Y\ge\varphi X\) is known, substituting \(\varphi X\) supplies a conservative lower bound on exposure, not permission to use \(X\). With \(X=2,Y=U_0=1,v=1\), true guaranteed exposure is zero; substitution of \(X\) spuriously creates .25. Equality in the survival expression requires equality of actual intensity with the bound and no additional hazard.

Subexponential growth also does not imply \(\dot U/U\to0\): let \(\log U\) accumulate smooth, fixed-area bumps centered at times \(k^2\). Its value is \(O(\sqrt t)\), while its derivative has nonvanishing peaks. Catch-up costs inferred from one instantaneous growth rate therefore need regularity over the whole future catch-up interval. Freezing or rolling back can preserve positive survival while surrendering a lead; M7 does not exclude that policy.

## M8. Delegation with agency loss priced explicitly

Let \(n\ge2\) actors choose \(d_i\in\{0,1\}\). Delegation gives strength \(1+sd_i\), \(s\ge0\), and contest-winning probability \(w_i=(1+sd_i)/\sum_j(1+sd_j)\). Let \(0\le\psi_0,\psi_1<1\) be shared-loss contributions and \(Q=\prod_j(1-\psi_{d_j})>0\). Delegation ends the delegator's agency with probability \(q_L\in[0,1]\); losing ends agency with probability \(p\in[0,1]\). Within this stipulated multiplicative model,

\[
\Phi_i=(1-q_Ld_i)Q[w_i+(1-w_i)(1-p)].
\]

**M8.1.** For finite \(s,n\) and \(q_L=1\), nondelegation strictly dominates against every profile, for every \(p\). All-nondelegation is the unique Nash equilibrium, including mixed equilibria.

**Proof.** Delegation gives zero. Nondelegation gives at least \(Qw_i>0\). Every delegated action, including positive probability assigned to it, is strictly worse. ∎

This strong result concerns a decision defined to terminate its own actor's agency with certainty. It is not a result about all AI assistance.

For \(p=1\), suppose \(k\) other actors delegate and set \(A=(1-q_L)(1-\psi_1)/(1-\psi_0)\). Direct substitution gives

\[
\frac{\Phi_D}{\Phi_N}=A(1+s)\frac{n+ks}{n+(k+1)s}.
\]

Consequently all-D is an equilibrium exactly when \(A[n+(n-1)s]/n\ge1\), while all-N is one exactly when \(An(1+s)/(n+s)\le1\). High \(q_L<1\) alone does not determine the game type. Under all-D,
\(\Phi_D=(1-q_L)(1-\psi_1)^n/n\), independently of speed.

For \(n=2,q_L=.99,\psi_0=.01,\psi_1=.05\), this survival is .0045125 and all-D requires \(s\ge206.421052\ldots\). For \(q_L=p=1,s=1,\psi_0=0,\psi_1=.01\), a nondelegator facing one delegator has survival .33. If the contest then ends and subsequent operation is safe, calendar time does not erase that probability. A speed limit and a lifetime limit are different; “not everyone survives” does not imply “each actor fails.”

## M9. Finite horizons, exact risk, and assurance

For a policy \(B\), define its aggregate conditional one-period loss probability \(q_t^B=\Pr(S_t^B\setminus S_{t+1}^B\mid S_t^B)\). When survival is positive, its exact horizon probability is \(\Phi_B(H)=\prod_{t<H}(1-q_t^B)\). Set the discrete log hazard \(\lambda_t^B=-\log(1-q_t^B)\).

**M9.1.** If \(\sum_{t<H}(\lambda_t^B-\lambda_t^R)\to+\infty\), then \(\Phi_B(H)/\Phi_R(H)\to0\). An eventual per-period gap of at least \(\delta>0\) gives exponential decay at least \(\delta\), up to a finite initial factor.

**Proof.** Take logarithms of the exact products and subtract. ∎

For constant risks .05 and .005, the exact rate gap is \(\log(.995/.95)=.04628075256\ldots\), not .045. Both infinite-horizon survival probabilities are zero. A decision criterion maximizing permanent survival alone ties them; preference for one requires a finite horizon, survival-time criterion, or an explicitly specified asymptotic ordering. Ratios cannot silently change the criterion.

For a two-action comparison at a fixed horizon, write \(R,T,S,P\) for cooperation/cooperation, racing/cooperation, cooperation/racing, and racing/racing payoffs to one actor. These may be survival probabilities under a stated criterion. With belief \(v\) that the other cooperates, cooperation's advantage is

\[
\Delta(v)=v(R-T)-(1-v)(P-S).
\]

If \(g_C=R-T>0\) and \(g_D=P-S>0\), cooperation is optimal exactly when \(v\ge g_D/(g_C+g_D)\). This follows by solving the linear inequality. Other sign combinations need their own classification; a negative expression obtained outside this region is not a negative “trust threshold.”

In an \(n\)-player setting with independent cooperation probability \(v\) for each rival, let \(D_k\) be own cooperation-minus-racing payoff when \(k\) rivals race. Expected advantage is
\(\sum_{k=0}^{n-1}\binom{n-1}{k}(1-v)^kv^{n-1-k}D_k\).
If \(D_0\ge g_C>0\) and **every** other \(D_k\ge-g_D\), the conservative sufficient condition is \(v^{n-1}\ge g_D/(g_C+g_D)\). Bounding only the cooperator's payoff is insufficient. For \(D=(1,-10,-1)\), \(v=\sqrt{.5}\), the supposed endpoint-only test fails: expected advantage is approximately \(-3.727922\).

A correlated belief placing all weight on “everyone else cooperates” and “everyone else races” gives an endpoint cutoff, not automatically risk dominance of the original multiplayer game or a coalition game. A coalition's objectives and actions must be specified separately.

Under model uncertainty, average policy survival across worlds before computing preferences. For instance, put probability .99 on a world in which racing survival is \(e^{-.05H}\), and .01 on a world with racing endpoint survivals \((T,P,S)=(.9,.4,.1)\). If cooperation survival is \(R=e^{-.005H}\) in either world, at \(H=1000\), \(T\approx.009>R\approx.006738\) and \(P>S\): racing strictly dominates in that finite game. High premise confidence alone does not preserve assurance. A threshold asymptotic in belief confidence needs uniform payoff-gap assumptions and a stated order of limits.

## M10. Participation and incentive compatibility

Consider \(n\) actors, a cooperative surplus \(S_a>0\), common cooperative survival \(\Phi_R>0\), and a common baseline value \(\bar V\). Actor \(i\)'s utility at share \(s_i\) is \(\Phi_R(S_as_i+\bar V)\). Feasible shares satisfy \(s_i\ge0\), \(\sum_is_i=1\). Let \(o_i\) be its outside-option utility, measured at the same horizon and including survival.

**M10.1.** Under complete information, weak participation is feasible exactly when

\[
\sum_i\max\left\{0,\frac{o_i/\Phi_R-\bar V}{S_a}\right\}\le1.
\]

Strict participation for all is feasible exactly when the inequality is strict.

**Proof.** Each actor needs at least its displayed required share, truncated at zero. Necessity follows by summing. For weak sufficiency, allocate these minimum shares and distribute the remainder. With a strict inequality, distribute positive portions of the remainder to make every binding participation constraint strict. Conversely, strict participation forces shares strictly above every nonnegative required share; their sum cannot be one if those minima already sum to one. ∎

If signed transfers are allowed, the corresponding total-utility test is \(\Phi_R(S_a+n\bar V)\ge\sum_io_i\); it is not interchangeable with constrained nonnegative shares. Larger cooperative surplus, lower outside advantage, different risk, and enforceable transfers are distinct participation levers. There is no unique lever in this model.

Now let each actor have a privately known type in a finite set, independently distributed with positive probabilities. The mechanism always cooperates. Its share rule \(s_i(t_i,t_{-i})\) can depend on reports, but utility from cooperation is linear in share and type-independent as above. The outside option is type-dependent, \(o_i(t_i)\), evaluated **interim**, before seeing other actors' types.

**M10.2.** Bayesian incentive compatibility requires each actor's interim expected share to be constant across its reports. It does not require its ex-post share to be constant. Weak BIC and interim participation are feasible exactly when

\[
\sum_i\max\left\{0,\max_{t_i}\frac{o_i(t_i)/\Phi_R-\bar V}{S_a}\right\}\le1.
\]

Strict interim participation is feasible when and only when this inequality is strict.

**Proof.** Independence makes the distribution of others' truthful reports identical for every own type. Let \(m_i(r_i)=E_{t_{-i}}s_i(r_i,t_{-i})\). Truthful reporting for type \(t\) requires \(m_i(t)\ge m_i(r)\) for all reports \(r\). Reversing the two types gives equality. Thus \(m_i\) is a constant \(k_i\), with \(k_i\ge0\) and \(\sum_ik_i=1\) by budget balance. Interim participation imposes exactly the lower bounds in the display. M10.1's allocation argument proves necessity and sufficiency, implemented by constant shares. The finite type assumption makes the maximum attained and gives the strict version. ∎

For an explicit nonconstant BIC allocation, take two independent types, strong with probability .8 and weak with probability .2. Let \(h(S)=.2,h(W)=-.8\), and
\(s_1=.5+.5h(t_1)h(t_2)\), \(s_2=1-s_1\).
The first actor's share matrix is \(\begin{pmatrix}.52&.42\\.42&.82\end{pmatrix}\). Every report has expected share .5. Truth is weakly optimal, although ex-post shares vary. This mechanism does not strictly elicit information.

If race survival depends on both types, the correct outside utility is \(o_i(t_i)=E[\Phi_i^{\rm race}(t_i,t_{-i})(V_i^{\rm race}(t_i,t_{-i})+\bar V)\mid t_i]\). Products of unconditional expectations need not equal it. Correlated types, type-dependent cooperative preferences, verification, ex-post participation, coalition deviations, and second-best mechanisms are outside M10.2. Failure of its restricted always-cooperate mechanism is not a theorem that an optimal general mechanism must race.

## M11. A sufficient host-viability condition, including the transient

Let a shared condition satisfy

\[
\dot V=V[\rho(1-V/K)-hE(t)],
\qquad \rho,K,h>0,\quad E(t)\ge0,
\]

with a required floor \(0<V_{\min}<K\). Assume continuous or piecewise continuous bounded load. Define \(E_{\rm safe}=\rho(1-V_{\min}/K)/h\).

**M11.1.** If \(V(0)\ge V_{\min}\) and \(E(t)\le E_{\rm safe}\) for all time, then \(V(t)\ge V_{\min}\) for all time. If instead \(0<V(0)\le K\), load is at most \(E_{\max}\) until time \(T\), and thereafter at most \(E_{\rm safe}\), the sufficient transient condition

\[
V(0)e^{-hE_{\max}T}\ge V_{\min}
\]

also guarantees viability.

**Proof.** At the lower boundary the derivative is nonnegative under the permanent cap; scalar comparison makes the interval invariant. With nonnegative load and \(V(0)\le K\), the upper boundary \(K\) is invariant as well. Therefore before \(T\), \(d\log V/dt\ge-hE_{\max}\). Integrate and apply the permanent-cap result at time \(T\). ∎

By M1, a divergent cumulative liability margin \(\int_0^t[\tau(s)-\nu]ds\to+\infty\), with equal other advantages and a represented minimum-load practice, makes load approach that minimum. An eventual uniform margin \(\tau\ge\nu+\delta\), \(\delta>0\), suffices; merely exceeding \(\nu\) by an integrable amount does not. If the minimum is strictly below \(E_{\rm safe}\), load eventually enters the safe region. This alone does **not** certify the preceding transient. An institution combining M5's correction certificate with liability must still show implementation time, initial margin, and a bound such as M11.1's. Viability is also distinct from participation: a safe arrangement need not be one all actors voluntarily enter.

The modules therefore support a demanding but finite institutional question: can a proposed change establish and retain adequate correction, incentives, participation, and transient safety for specified hazards? They supply conditional mechanisms and falsifiable requirements. Applying them to the present AI trajectory requires evidence at each interface, and comparing policies requires common outcomes, horizons, and decision standards.
