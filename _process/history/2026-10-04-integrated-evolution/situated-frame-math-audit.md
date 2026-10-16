# Situated frame revision: attraction, paid discovery, and escape

Mathematical audit, 5 October 2026. AI-generated research assistance for Ren. This memo was prepared after reading the situated-correction framework, research hub, and latest log. The coordinating agent proposed the two-state and protected-introduction equations below; this agent checked their mechanism, equilibria, stability, escape conditions, and limitations, and supplied the paid-channel extension and proposal-origination countercase.

This is a finite, analyst-specified example with common interests. It does not explain genuinely unanticipated categories, changing values, or every situated institution. No originality or empirical-validation claim is made.

## 1. Keep the epistemic distinction explicit

The example has two representations. The initial representation contains familiar outcomes and the visible cost of inquiry. The expanded representation additionally distinguishes a consequential effect and an associated response. The expanded representation is included in the analyst's model but is not initially available to every modeled decision maker.

Learning a familiar parameter within the initial representation does not expand it. For example, if familiar prediction error \(e\) obeys the mean learning law

\[
\dot e=-r(1-q)e,\qquad r>0,
\tag{1}
\]

then familiar prediction becomes accurate whenever sufficient routine experience accumulates. This auxiliary law can coexist with the frame dynamics below. It is a simple learning model, not a universal claim about Bayesian inference.

In the two-state model, successful diagnostic experience moves a member from the initial representation to the expanded one. This is an explicitly specified transition in representation, not a change in a probability assigned to a category that the initial representation already contains.

The example initially assumes that a successful diagnostic episode conveys the relevant effect accurately. Learning its magnitude after recognizing the category, ambiguous diagnosis, and false evidence require additional state variables or transition mechanisms.

## 2. Common interests and an explicit policy update

Let \(q\in[0,1]\) be the institutional share or intensity devoted to inquiry and the associated alternative practice. Let \(z\in[0,1]\) be the fraction retaining the expanded frame. The actual common marginal benefit is \(b\); visible cost is \(c>0\). Initially take \(b>c\), so the modeled activity has positive actual net value for everyone. The comparison world \(b=0\) will expose the cost of unsuccessful inquiry.

Members with the initial frame do not represent the \(b\) contribution. Members with the expanded frame do. If the institution aggregates their represented common consequences by their population shares, its current estimated marginal common return is \(bz-c\).

A log-odds policy-adjustment rule is

\[
\frac{d}{dt}\log\frac{q}{1-q}=bz-c.
\]

This yields

\[
\boxed{
\begin{aligned}
\dot q&=q(1-q)(bz-c),\\
\dot z&=\lambda q(1-z)-\mu z,
\end{aligned}}
\qquad \lambda,\mu>0.
\tag{2}
\]

The first equation is adjustment of a common policy according to its represented common return. It should not be described as individual reproductive fitness: public benefit does not automatically give an individual its full reproductive payoff. A revision protocol or policy-learning mechanism has been specified, not derived from the bare fact of common interests.

The second equation follows from nonnegative transitions: each member lacking the expanded frame encounters and successfully incorporates diagnostic experience at rate \(\lambda q\); each expanded frame is lost through turnover, forgetting, or failure of organizational transmission at rate \(\mu\). The parameter \(\lambda\) therefore requires separate evidence about access, recognition, credibility, and successful uptake. It is not a guaranteed arrival of a corrective proposal from outside.

Inquiry costs \(cq\) per unit time. Its diagnostic productivity can be written

\[
\lambda q=\frac{\lambda}{c}(cq).
\tag{3}
\]

Thus diagnostic experience is produced by paid activity. The model assumes this activity can be funded and implemented. Those conditions should be checked rather than inferred from the cost term.

All coefficients and returns are expressed in normalized units compatible with the policy-adjustment timescale. A physical application needs the conversion from money, effort, or foregone output into the policy-update rate.

## 3. Derived attraction to the reduced frame

The square \(0\leq q,z\leq1\) is forward invariant. The reduced-frame equilibrium

\[
O=(0,0)
\]

has Jacobian

\[
J_O=
\begin{pmatrix}
-c&0\\
\lambda&-\mu
\end{pmatrix}.
\tag{4}
\]

Both eigenvalues are strictly negative. Therefore the reduced-frame regime attracts a neighborhood even when \(b>c\): the result is stronger than saying that the boundary is invariant. Small initial amounts of inquiry and awareness can disappear under this specified adjustment and turnover process.

The feedback is consequential: low awareness makes inquiry appear costly; its withdrawal reduces the experience that would expand awareness; turnover removes what was previously learned. There is no disagreement about actual interests in this example.

Along a trajectory converging to \(O\), \(q\) eventually decays exponentially, so total diagnostic exposure \(\lambda\int_0^\infty q(t)\,dt\) is finite. Conditional on a specified inquiry path, a member with Poisson diagnostic opportunities has probability

\[
\exp\left[-\lambda\int_0^\infty q(t)\,dt\right]>0
\]

of never receiving a diagnostic encounter. This is a conditional exposure calculation, not the full distribution of an interacting finite-population process.

At the same time, (1) gives \(e\to0\) on that trajectory, since \(q\to0\) and routine exposure continues. Accurate familiar prediction can therefore accompany loss of the channel for revising the representation.

## 4. Invasion, coexistence of attractors, and exact threshold states

There is a full-inquiry equilibrium

\[
H=\left(1,\frac{\lambda}{\lambda+\mu}\right).
\tag{5}
\]

Its eigenvalues are

\[
-\left(\frac{b\lambda}{\lambda+\mu}-c\right),
\qquad
-(\lambda+\mu).
\]

It is locally asymptotically stable exactly when

\[
\boxed{\lambda(b-c)>\mu c.}
\tag{6}
\]

The first eigenvalue is the invasion rate of a small reduction in inquiry, with sign reversed. A beneficial activity can fail this persistence test if discovery and transmission cannot offset frame loss.

When (6) holds, there is an interior equilibrium

\[
\boxed{
q_s=\frac{c\mu}{\lambda(b-c)},\qquad
z_s=\frac cb.
}
\tag{7}
\]

Its Jacobian has zero upper-left entry, positive off-diagonal entries, and negative lower-right entry. Its determinant is

\[
-bq_s(1-q_s)\lambda(1-z_s)<0.
\]

It is a saddle. Hence the same common interests and technological parameters admit an attracting reduced-frame regime and an attracting sustained-inquiry regime, with a saddle between them.

Two useful certificates avoid claiming an exact global separatrix:

- The rectangle \(q\geq q_s,\ z\geq z_s\) is forward invariant. Every point in it except the saddle converges to \(H\).
- The rectangle \(q\leq q_s,\ z\leq z_s\) is forward invariant. Every point in it except the saddle converges to \(O\).

For the upper rectangle, inquiry cannot decrease; at its lower awareness boundary, awareness cannot decrease. The only compatible limit above the saddle is \(H\). The lower rectangle has the reversed argument. The other two quadrants require the actual stable manifold; neither inquiry share nor awareness alone gives the complete escape threshold.

On the open square, the Dulac multiplier \(1/[q(1-q)]\) gives

\[
\frac{\partial}{\partial q}
\left(\frac{\dot q}{q(1-q)}\right)
+
\frac{\partial}{\partial z}
\left(\frac{\dot z}{q(1-q)}\right)
=-\frac{\lambda q+\mu}{q(1-q)}<0.
\tag{8}
\]

There are no interior periodic orbits. This supports the planar basin interpretation; it does not identify the separatrix analytically.

If \(\lambda(b-c)<\mu c\), all initial states with \(q<1\) converge to \(O\). Indeed \(z\) is eventually bounded above by a value below \(c/b\), since \(\dot z\leq\lambda-(\lambda+\mu)z\), and then inquiry decays. If \(b\leq c\), inquiry similarly cannot sustain the represented advantage. The boundary \(q=1\) is invariant under the pure log-odds rule and must be excluded from a global claim about withdrawal.

At equality in (6), the full-inquiry equilibrium has a zero eigenvalue. It is not neutrally robust. With \(x=1-q\), \(y=z_s-z\), its center-manifold expansion is

\[
y=\frac{\lambda(1-z_s)}{\lambda+\mu}x+O(x^2),
\qquad
\dot x=
\frac{b\lambda(1-z_s)}{\lambda+\mu}x^2+O(x^3).
\tag{9}
\]

The positive coefficient repels a small interior reduction in inquiry. Strict inequality in (6) is therefore the robust persistence condition. This is a local equality-case calculation; the strict-regime results above do not rely on extending a hyperbolic argument through the boundary.

## 5. Paid protected introductions and a finite escape threshold

Allow protected introductions of inquiry at rate \(u\geq0\):

\[
\boxed{
\begin{aligned}
\dot q&=(1-q)[q(bz-c)+u],\\
\dot z&=\lambda q(1-z)-\mu z.
\end{aligned}}
\tag{10}
\]

The introductions sustain an experimental practice, not knowledge of a successful answer. Frame expansion still requires the diagnostic events in the second equation. The cost of operating inquiry remains \(cq\). The cost of maintaining the protection mechanism itself is addressed below.

Assume the baseline bistable condition (6). At an interior equilibrium, the awareness nullcline gives \(z=\lambda q/(\lambda q+\mu)\), and the inquiry equation becomes

\[
P_u(q)=Aq^2+(\lambda u-c\mu)q+\mu u=0,
\qquad A=\lambda(b-c)>0.
\tag{11}
\]

The lower stable equilibrium and the interior saddle meet at

\[
\boxed{
u_{\mathrm{SN}}=
\frac{\mu}{\lambda}
(\sqrt b-\sqrt{b-c})^2,
\qquad
q_{\mathrm{SN}}=
\frac{\mu}{\lambda}
\left(\sqrt{\frac b{b-c}}-1\right).
}
\tag{12}
\]

The baseline condition ensures \(0<q_{\mathrm{SN}}<1\).

For \(0<u<u_{\mathrm{SN}}\), both roots of (11) are inside the square. At either root, the Jacobian trace is negative and

\[
\det J=-(1-q)P_u'(q).
\]

The lower root is stable; the upper is a saddle. Full inquiry remains stable. Weak protected experimentation thus changes complete exclusion into a low-inquiry regime but need not remove the attraction toward inadequate representation.

For \(u>u_{\mathrm{SN}}\), no interior equilibrium remains. The same Dulac multiplier gives

\[
-\frac{u}{q^2}
-\frac{\lambda q+\mu}{q(1-q)}<0.
\tag{13}
\]

Together with the inward boundary flow and the unique remaining equilibrium, planar limit-set arguments give convergence to \(H\) from every state in the square. At \(u=u_{\mathrm{SN}}\), the saddle-node equilibrium is semistable: approach from its lower side need not escape. A guaranteed escape statement requires a strict margin above the threshold.

Maintaining \(u>u_{\mathrm{SN}}\) long enough eventually places the state in the upper rectangle from section 4. Protection can then be withdrawn without relapse in this deterministic, unchanged environment. The required duration is not given by the equilibrium threshold. A short high-intensity pulse can fail to cross the basin boundary.

For \(b=4,\ c=\lambda=\mu=1\),

\[
u_{\mathrm{SN}}=(2-\sqrt3)^2\approx.0717968,
\quad
q_{\mathrm{SN}}=\frac2{\sqrt3}-1\approx.154701,
\quad
(q_s,z_s)=\left(\frac13,\frac14\right).
\]

These are analytical illustration parameters, not empirical estimates.

## 6. A maintained discovery channel has an additional resource obligation

Treating \(u\) as fixed does not establish that the institution implementing protected trials lasts. A minimal paid-capacity extension is

\[
\boxed{\dot u=\xi w-\delta_u u,}
\qquad \xi,\delta_u>0,\quad w\geq0,
\tag{14}
\]

where \(w\) is the resource flow maintaining the introduction mechanism. This is distinct from spending \(cq\) on the trials themselves.

With constant funding \(w\), \(u\to\bar u=\xi w/\delta_u\). A strict sufficient condition for eventual escape is

\[
\boxed{w>\frac{\delta_u}{\xi}u_{\mathrm{SN}}.}
\tag{15}
\]

Eventually \(u\) exceeds a constant strictly above \(u_{\mathrm{SN}}\); monotone comparison with (10), whose off-diagonal state derivatives are nonnegative, then yields convergence to \(H\). This result assumes funding and authority remain available during the approach.

A conservative per-time budget sufficient for continuous operation is

\[
\boxed{B>c+\frac{\delta_u}{\xi}u_{\mathrm{SN}}.}
\tag{16}
\]

One can choose \(w\) between the second term and \(B-c\), so the budget covers both \(cq\leq c\) and protected-channel maintenance. This is sufficient, not necessary: temporary support, state-dependent spending, or a different institution can require less.

This extension endogenizes the stock of protection, not the selection and enforcement of the funding rule. Constant \(w\) remains a declared external policy. A fee or an assigned budget is not proof of legitimate authority, reliable execution, or indefinite resource supply.

Even without a separate protection stock, a spending cap can prevent sustained inquiry. If actual funded inquiry is capped at \(Q\leq1\), with \(cQ\leq B\), replace the first equation of (2) by

\[
\dot q=q(1-q/Q)(bz-c).
\]

The high-intensity boundary is stable only when

\[
\lambda Q(b-c)>\mu c,
\quad\text{equivalently}\quad Q>q_s.
\tag{17}
\]

This exposes a maintenance requirement on the discovery channel rather than assuming that any nonzero inquiry is enough.

## 7. More inquiry can be wasteful

In the absent-benefit comparison \(b=0\), protected introductions give

\[
\dot q=(1-q)(u-cq).
\]

For \(0<u<c\) and \(q_0<1\), the attracting inquiry level is \(q_*=u/c\), and its recurring trial cost is

\[
cq_*=u.
\tag{18}
\]

If the protection mechanism is separately maintained, \(w\) must be added. Thus protected inquiry has a real ongoing cost when no benefit is found. The example does not justify maximizing inquiry, preserving every proposal, or forcing every frame revision.

Final synthesis review identified a boundary qualification: the exact state \(q_0=1\) remains invariant because of the factor \(1-q\), even when \(b=0\). Its trial cost stays at \(c\). It is therefore excluded from the convergence claim above; the numerical control starts in the interior.

The beneficial-world model assumes reliable diagnostic experience and a correct expanded evaluation. False signals, mistaken categories, coercive revision, and damaging trials require explicit countercases. Protection should not be evaluated only in a world where the protected inquiry is guaranteed to reveal a useful answer.

## 8. Endogenous proposal origination: robustness and a countercase

The factor \(q\) in (2) means retained knowledge can increase an existing inquiry practice but cannot introduce it from \(q=0\). This is a substantive property of the policy-update mechanism.

Let holders of the expanded frame originate inquiry proposals at rate \(\beta z\), while retaining the same payoff-adjustment mechanism:

\[
\boxed{
\dot q=(1-q)[q(bz-c)+\beta z+u],
\qquad
\dot z=\lambda q(1-z)-\mu z.
}
\tag{19}
\]

This added proposal route is considered in the beneficial case \(b>c\), where the aware proponents have grounds for the alternative. It is not a rule that every recognized but unhelpful proposal should be originated continually. Its administrative costs, if material beyond the resulting inquiry cost \(cq\), need an additional budget term.

For \(u=0\), its closed-state Jacobian is

\[
\begin{pmatrix}
-c&\beta\\
\lambda&-\mu
\end{pmatrix}.
\]

The closed state is locally asymptotically stable when \(\beta\lambda<c\mu\), and unstable when

\[
\boxed{\beta\lambda>c\mu.}
\tag{20}
\]

Thus a small rate of endogenous origination does not remove the attractor; the baseline result is not solely an artifact of forbidding proposals at zero prevalence.

Under the baseline bistability condition (6) and \(0\leq\beta\lambda<c\mu\), the interior saddle moves to

\[
q_s(\beta)=
\frac{c\mu-\beta\lambda}{\lambda(b-c)},
\qquad
z_s(\beta)=\frac{\lambda q_s(\beta)}{\lambda q_s(\beta)+\mu}.
\tag{21}
\]

The high equilibrium remains stable. The sign classification follows by substituting the awareness nullcline: the inquiry drift is proportional to
\(q[\lambda(b-c)q+\beta\lambda-c\mu]\). Positive origination lowers the interior threshold, but a finite threshold remains until the feedback exceeds the decay product.

For \(\beta\lambda>c\mu\), no positive interior saddle remains and the closed state has an expanding positive direction. This supplies a countercase to the assertion that situated representation necessarily produces an attracting closed regime. The strict inequality boundary is nonhyperbolic and is not covered by linear stability alone.

The generalized Dulac expression is

\[
-\frac{\beta z+u}{q^2}
-\frac{\lambda q+\mu}{q(1-q)}<0.
\]

The exact protected-introduction fold (12) concerns \(\beta=0\). It should not be reused unchanged after adding proposal origination.

Both results matter: a reduced-frame attractor can be robust to small endogenous novelty entry, while sufficiently productive proposal origination can make it locally repelling. Proposal origination is a different mechanism from changing relative support among options already in use.

## 9. Prior art and scope of the result

[Esponda and Pouzo's Berk–Nash framework](https://arxiv.org/abs/1411.1152) formalizes best-fitting beliefs within possibly misspecified subjective models, with the fit depending on the evidence generated by action. This precedes the general claim that accurate adaptation to endogenous experience can sustain a mistaken account.

[Schipper's discovery framework](https://faculty.econ.ucdavis.edu/faculty/schipper/sceunaw.pdf) distinguishes changing beliefs within a game representation from discovering actions that change the representation. The analyst still specifies the formal awareness structure. The present binary frame is an even narrower illustration and must not be called a formalization of all genuine novelty.

The contribution attempted here is a tractable connection among common interests, represented evaluation, paid experience production, loss of institutional memory, attraction from nearby states, and a financed escape channel. The particular equations and bifurcations may have mathematical equivalents in other domains; their novelty has not been established.

The critical assumptions are separately testable: aggregation of represented common returns by \(z\), log-odds policy adjustment, diagnostic exposure proportional to funded activity, reliable frame expansion, frame loss at rate \(\mu\), and enforceable protected introductions. A finding that affected people can originate informative alternatives without prior inquiry, or that memory is retained without continuing experience, changes the analysis rather than becoming evidence of a hidden version of the same mechanism.

Useful empirical distinctions are familiar prediction error versus diagnostic coverage; retained categories versus confidence within them; proposal entry versus selection among existing proposals; authorized experimentation versus receipt of a signal; and the cost of maintaining those channels. None should be replaced by a single score for “openness.”
