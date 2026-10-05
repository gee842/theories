# Bounded rule revision under separate operating constraints

This note constructs a controller for the existing paid verification model. It proves that a declared set of operating conditions can remain satisfied while a maintenance rule changes at a bounded rate. The guarantee holds even when the requested verification target changes or cannot be achieved within that set. It does not prove that the target will be reached, that the conditions are legitimate, or that every recoverable state has been identified.

The construction applies established forward-invariance and control-barrier methods to this particular model. The [Ames, Xu, Grizzle and Tabuada treatment](https://arxiv.org/abs/1609.06408) develops safety constraints as restrictions on admissible controls, including their interaction with performance objectives and actuator bounds. The broader idea of maintaining distinct economic and ecological conditions without combining them into a single maximand also predates this experiment; see [Béné, Doyen and Gabay's viability analysis](https://www.vliz.be/imisdocs/publications/259103.pdf). The result here is the explicit feasible region and bounded-rate certificate for the specified operating equations, not a claim to a new general control theory.

## Plant, control, and accounting

Retain the [constitutional-extension model](../../constitutional-extension/model/CONSTRUCTION.md). Use state order \((x,h,C,G,m)\), matching the numerical controller comparison. Let

\[
q(C)=\left(\frac{C}{K+C}\right)^2,\quad
p(G)=\frac{G}{L+G},\quad r(C)=y_0+Aq(C),\quad
D=hp(G),\quad V=(1-\lambda)\tau x r(C).
\]

Here \(x\) is paying participation, \(h\) is the share of contractors delivering maintenance and reporting truthfully within the stated two-practice repertoire, and \(C,G\) are useful service and verification capacities. The controlled state \(m\) is the fraction of a genuine contractor's assigned budget spent on verification maintenance. The only new control is its rate of change:

\[
\begin{aligned}
\dot x&=\kappa x(1-x)[Aq(C)D-\tau r(C)],\\
\dot h&=\nu h(1-h)V(D-m),\\
\dot C&=\eta_C\lambda\tau x r(C)-\mu_C C,\\
\dot G&=\eta_GmhV-\mu_G G,\\
\dot m&=u,\qquad |u|\le R.
\end{aligned}
\tag{1}
\]

Thus the controller cannot set \(m\) instantaneously. The operating budget is unchanged: fees still finance useful capacity, delivered verification maintenance, contractor payments, and the inert reserve. Increasing \(m\) redirects an existing contract budget from contractor retention to maintenance; it does not add operating resources.

Exact state observation, knowledge of the plant, continuous feedback, and authority to change \(m\) remain assumed. Their costs and political survival are not inside the fee ledger. This is an unpriced governance mechanism applied to an explicitly funded operating mechanism. The finite attack repertoire and the deferred-settlement primitives of the original construction remain in force.

## A sufficient controlled invariant region

Choose positive floors \(\bar x,\bar h<1\), \(\bar C,\bar G>0\), a maintenance floor \(m_\ell>0\), an incentive reserve \(\delta>0\), and a barrier gain \(\alpha>0\). Define

\[
\mathcal S=\{\bar x\le x\le1,\ \bar h\le h\le1,\
C\ge\bar C,\ G\ge\bar G,\ m\ge m_\ell,\
b:=D-m-\delta\ge0\}.
\tag{2}
\]

The last condition is distinct from a capacity floor. It reserves a positive return advantage for genuine maintenance: \(s_h=V(D-m)\ge V\delta\). Since \(D\le1\), it also implies \(m\le1-\delta\). The other conditions protect participation and the capacities financing and implementing the service. These choices encode a stated operating purpose; mathematics alone does not choose their values.

Write

\[
\underline D=\bar h\,p(\bar G),\quad
\underline V=(1-\lambda)\tau\bar x\,r(\bar C),\quad
\Delta_S=\underline D-\delta-m_\ell.
\]

The following sufficient conditions will be used:

\[
\begin{aligned}
\gamma_x&=(\underline D-\tau)Aq(\bar C)-\tau y_0>0,\\
\eta_C\lambda\tau\bar x r(\bar C)&\ge\mu_C\bar C,\\
\eta_Gm_\ell\bar h\,\underline V&\ge\mu_G\bar G,\\
\Delta_S&>0,\qquad
\alpha\Delta_S\ge\mu_G/4,\qquad R\ge\mu_G/4.
\end{aligned}
\tag{3}
\]

The first inequality implies \(\underline D>\tau\). It therefore lower-bounds user advantage throughout the whole region, not just at the corner. The next two inequalities make the stock floors sustainable at the lowest permitted participation and spending. The final inequalities supply room to adjust a changing rule fast enough to preserve both its lower bound and its incentive reserve.

These are sufficient conditions, with deliberately conservative bounds. They are not necessary conditions for operation or for viable control.

## A bounded-rate filter and its feasibility proof

Differentiate effective verification along the actual plant:

\[
\dot D=p(G)\dot h+h\frac{L}{(L+G)^2}\dot G.
\tag{4}
\]

This quantity depends on the current \(m\), but not directly on \(u=\dot m\). On \(\mathcal S\), genuine maintenance has a positive advantage, so \(\dot h\ge0\). Also \(\dot G\ge-\mu_GG\). Consequently

\[
\dot D\ge-\mu_Gh\frac{LG}{(L+G)^2}\ge-\frac{\mu_G}{4}.
\tag{5}
\]

To retain the maintenance floor and the reserve, require

\[
u\ge-\alpha(m-m_\ell),\qquad
u\le\dot D+\alpha b.
\tag{6}
\]

Intersect these derivative conditions with the actuator limit:

\[
\boxed{
\ell(z)=\max\{-R,-\alpha(m-m_\ell)\},\qquad
v(z)=\min\{R,\dot D+\alpha b\}.
}
\tag{7}
\]

For any nominal command \(u_0(t,z)\), apply

\[
\boxed{u(t,z)=\min\{v(z),\max\{\ell(z),u_0(t,z)\}\}.}
\tag{8}
\]

**Feasibility.** The interval in (7) is nonempty everywhere on \(\mathcal S\). To see this, put \(\ell_0=-\alpha(m-m_\ell)\) and \(v_0=\dot D+\alpha b\). Then

\[
v_0-\ell_0
=\dot D+\alpha(D-\delta-m_\ell)
\ge-\mu_G/4+\alpha\Delta_S\ge0.
\tag{9}
\]

Also \(v_0\ge-\mu_G/4\ge-R\), while \(\ell_0\le0\le R\). These three comparisons show that \([\ell_0,v_0]\) intersects \([-R,R]\). This proves joint feasibility of the two derivative constraints and the actuator limit; simply clipping \(m\) to an instantaneous admissible interval would not establish it.

For well-posedness, assume the nominal command is measurable in time, locally bounded, and locally Lipschitz in state uniformly on compact finite-time domains. For example,

\[
u_0(t,z)=\varepsilon m(1-m)[T(t)-G]
\tag{10}
\]

has this property for a bounded measurable target \(T(t)\). The endpoint functions and their finite max/min operations are locally Lipschitz in state. Standard Carathéodory solutions are therefore well-defined and unique. Arbitrary measurable state feedback, without a corresponding well-posedness condition, is not being claimed.

## Invariance and persistence theorem

**Proposition.** Under (3), the controller (8) keeps every initial state in \(\mathcal S\) inside \(\mathcal S\) for all future time. For every admissible nominal command,

\[
x(t)\longrightarrow1,\qquad h(t)\longrightarrow1,
\qquad C(t)\longrightarrow C_R,
\tag{11}
\]

where \(C_R>0\) is the unique solution of

\[
\eta_C\lambda\tau r(C_R)=\mu_C C_R.
\]

Verification capacity remains bounded and at least \(\bar G\). Neither \(G\) nor \(m\) must converge for an arbitrary changing nominal command.

**Proof.** Let \(w=m-m_\ell\). Conditions (6) give

\[
\dot w\ge-\alpha w,\qquad
\dot b=\dot D-u\ge-\alpha b.
\]

Hence neither nonnegative quantity can cross zero. At \(x=\bar x\), user advantage is at least \(\gamma_x>0\), so the vector field points inward. At \(h=\bar h\), the reserve makes the genuine practice at least as successful as its alternative. The two stock inequalities in (3) point the vector field inward at \(C=\bar C\) and \(G=\bar G\). The faces \(x=h=1\) are invariant. Together these conditions close a first-exit argument for the intersection (2).

Both capacities have bounded inputs because \(r(C)\le y_0+A\), the shares are at most one, and \(m\le1-\delta\). Thus there is no finite-time escape, and the solution remains global. Throughout \(\mathcal S\),

\[
\dot x\ge\kappa\gamma_x x(1-x),\qquad
\dot h\ge\nu\underline V\delta h(1-h).
\tag{12}
\]

Logistic comparison gives \(x,h\to1\), including the already fixed endpoints. The useful-capacity equation then approaches its autonomous equation with \(x=1\). That scalar equation has a unique positive, globally attracting root: under \(A\le y_0\),

\[
r(C)-Cr'(C)
=y_0+A\frac{C^2(C-K)}{(K+C)^3}
\ge y_0-A/27>0,
\]

so \(r(C)/C\) strictly decreases from infinity to zero. Scalar comparison with \(x\) arbitrarily close to one proves \(C\to C_R\). The verification and maintenance bounds have already been established. This proves (11), without assuming target convergence or a common scalar objective. \(\square\)

This result protects a process capable of continued funded operation while its requested output target changes. It does not prove the survival of the controller's own observation, authority, or normative constraint selection.

## Canonical certificate

Use the existing canonical coefficients

\[
y_0=1,\ A=.8,\ K=L=\mu_C=\mu_G=\kappa=1,
\quad\tau=.15,\ \lambda=.5,
\quad\eta_C=800/29,\ \eta_G=1600/29,\ \nu=10.
\]

Take

\[
\bar x=\bar h=.9,\quad\bar C=2.5,\quad\bar G=2.1,
\quad m_\ell=.45,\quad\delta=.02,\quad\alpha=2,\quad R=.5.
\tag{13}
\]

The useful-capacity limit is \(C_R=3\). The numerical values below are evaluations of analytic inequalities, not simulation-based certificates:

| Quantity | Value |
|---|---:|
| Minimum effective verification \(\underline D\) | 0.6096774194 |
| Minimum verification budget \(\underline V\) | 0.0950510204 |
| Minimum user advantage \(\gamma_x\) | 0.0376234365 |
| Inward useful-capacity margin | 0.1220971147 |
| Inward verification-capacity margin | 0.0238986629 |
| Reserve between the two rule bounds \(\Delta_S\) | 0.1396774194 |
| Minimum raw rate-interval width \(2\Delta_S-1/4\) | 0.0293548387 |
| Guaranteed logistic coefficient for \(h\) | 0.0190102041 |

The verification-floor condition requires \(m_\ell\ge0.4449364824\) at this corner, so the chosen 0.45 retains a strict margin. The rate requirement uses only 0.25 of the available bound 0.5. The reference initial state

\[
(x,h,C,G,m)=(.94,.93,2.7,2.4,.5)
\]

belongs to \(\mathcal S\). Every target experiment beginning there therefore has the same analytic operating guarantee when (8) is applied exactly.

## What feasibility and infeasibility mean

There are three different questions.

1. **Feasibility of this filter.** The inequalities prove that its admissible rate interval is nonempty on \(\mathcal S\). Outside that set the interval may be empty, and the implementation must report this rather than silently reversing its endpoints.
2. **Compatibility of a requested steady target with this set.** A target can conflict with one of the protected conditions even while a safe command exists. The controller must then sacrifice tracking.
3. **Viability of the original state under some controller.** This asks whether any allowed future control can maintain the declared conditions. The construction does not compute the full viability kernel, and failure of its sufficient certificate is not proof of general impossibility.

For example, changing only \(h\) in the reference state to 0.49 puts the state outside \(\mathcal S\). It gives \(b\simeq-.1741\) and \(\dot D\simeq-.0715\), hence an upper rate bound about \(-.4197\) while the lower bound is \(-.1\). The barrier intersection is empty there. This diagnoses incompatible demands from this particular pair of exponential barrier conditions at that state, not inevitable operating collapse under every conceivable rule.

An elementary genuine obstruction is different: at a proposed verification floor with \(\dot G<0\), the rate control \(u\) cannot instantly reverse \(\dot G\), because \(u\) changes \(m\) rather than \(G\) directly. Starting exactly on that floor would violate it immediately. This is why a rate-limited certificate needs a buffer and jointly feasible derivative conditions.

## Tracking is a separate claim

For the canonical model, a fully selected steady state has \(x=h=1\), \(C=3\), and \(G=6m\). If it is also required to meet a constant target \(G=T\) within \(\mathcal S\), then

\[
T\ge2.7,\qquad \frac{T}{1+T}-\frac{T}{6}\ge\delta.
\tag{14}
\]

For \(\delta=.02\), the compatible interval is exactly

\[
\boxed{2.7\le T\le T_{\max},\qquad
T_{\max}=\frac{5-6\delta+
\sqrt{(5-6\delta)^2-24\delta}}{2}
\simeq4.8552846623.}
\tag{15}
\]

The small other root of the quadratic lies below 2.7. Thus target 6 is incompatible with a fully operating steady state in this protected set. This bound is specific to the chosen reserve, floor and model. It is not a universal bound on feasible social purposes or on all controllers outside this set.

Target 4 gives \(m_*=2/3\) and strictly positive barrier margins. Near that equilibrium the filter is inactive for nominal controller (10). The previous local stability calculation therefore continues to apply: the remaining \((G,m)\) block has characteristic polynomial

\[
z^2+z+6\varepsilon m_*(1-m_*),
\]

with negative-real-part roots for every \(\varepsilon>0\); the other three eigenvalues are negative. This proves local tracking stability near that equilibrium. It does not establish global tracking from every state of \(\mathcal S\), convergence for arbitrary target switching, or optimality of the filtered path. Those stronger claims require separate analysis.

## Comparators and interpretation

The control interface is the same bounded rate \(u=\dot m\) for every dynamic comparator. Relevant controls include the raw target response with the same actuator bound, a slower response, a fixed rule, a bounded-rate move toward the known steady rule \(T/6\), and simple constant upper caps implemented with the same rate bounds. Instantaneously clipping the state \(m\) would give a comparator or treatment a different actuator and would not test the present claim.

A fixed rule \(m=.5\) already preserves operation for the reference protected box and approaches verification level 3. Its inability to reach target 4 is a tracking limitation, not a failure of institutional survival. Likewise a simple fixed cap might perform as well as the state-dependent filter on selected target paths. These alternatives are necessary to assess what the extra controller actually contributes. Neither numerical tracking success nor superiority on a finite comparison grid follows from the invariance theorem.

The chosen constraints remain separate: participation, useful capacity, verification capacity, maintenance spending, and the private incentive reserve. They are not assigned fixed exchange weights or added into a single score. But they are still externally selected constraints within a scalar-return imitation model. Their legitimacy, revisions under disagreement, informational uncertainty, sensing delays, discrete sampling, strategic evasion of the controller, and the resources needed to exercise governance remain outside the theorem. A sampled numerical implementation approximates the continuous feedback law; the exact guarantee is for (1) and (8), not for every finite-step implementation or unknown plant.

## Distinguishing delayed loss from a finite simulation record

A simple loss-entry certificate remains available for controllers that keep a positive maintenance floor. Suppose that after some time \(t_0\),

\[
m_\ell\le m(t)\le1,\qquad
h(t_0)\le h_\ell<\min\{m_\ell,\tau\},\qquad x(t_0)<1.
\tag{16}
\]

Then \(h\) is nonincreasing, because \(D\le h\le h_\ell<m_\ell\). User advantage satisfies

\[
s_x=(D-\tau)Aq(C)-\tau y_0\le-\tau y_0.
\]

For \(0<x(t_0)<1\),

\[
\operatorname{logit}x(t)
\le\operatorname{logit}x(t_0)-\kappa\tau y_0(t-t_0).
\tag{17}
\]

Thus \(x\to0\) and future receipts have finite integral. The stable linear stock equations with integrable nonnegative inputs imply \(C,G\to0\). If \(x(t_0)=0\), both capacities simply depreciate from that point. The share \(h\) can freeze above zero as financed work disappears. In the canonical case \(m_\ell=.45\), the threshold \(h_\ell=.1\) is sufficient, regardless of how much useful capacity remains at entry.

This lemma can certify eventual loss before it is visually complete. A very large but finite \(\operatorname{logit}x(t_0)\) can delay a visible drop in participation despite continuously negative selection. A numerical display rounded to \(x=1\) must not be confused with the exact invariant face \(x=1\), where the absent alternative cannot enter. Conversely, a record showing verification depletion while participation remains high must report those observed states; it should not claim that all stocks have already vanished. Disturbance or reintroduction experiments using this certificate are additional interventions, not part of the undisturbed invariance theorem.

## Two analytic extensions after the core construction

The following extensions were added after the comparison protocol was written. They are analytic variants, not claims about the previously specified numerical treatment.

**Bounded revision of one protected standard.** The reserve itself can change according to an externally supplied absolutely continuous standard \(\delta(t)\), provided

\[
0<\delta_{\min}\le\delta(t)\le\delta_{\max},\qquad
\dot\delta(t)\le\rho\quad\text{almost everywhere},\qquad \rho\ge0.
\]

Set \(b(t,z)=D-m-\delta(t)\), and replace the upper endpoint by

\[
v(t,z)=\min\{R,\dot D-\dot\delta+\alpha b\}.
\tag{18}
\]

The same argument proves safety for the moving region if its initial conditions hold and

\[
R\ge\mu_G/4+\rho,\qquad
\alpha(\underline D-\delta_{\max}-m_\ell)
\ge\mu_G/4+\rho,
\tag{19}
\]

together with the unchanged stock and user conditions in (3). Indeed the difference between the raw upper and lower endpoints is now at least \(-\mu_G/4-\rho+\alpha(\underline D-\delta_{\max}-m_\ell)\), and \(\dot b\ge-\alpha b\). The convergence proof for \(h\) uses \(\delta_{\min}\). This permits bounded revision of one declared operating standard; it does not endogenize the people, disagreements, evidence or procedures selecting that standard. Unrestricted tightening need not be feasible under the rate limit.

**A conservative controller without ongoing observation of \(h\).** Suppose only the initial bound \(h(0)\ge\bar h\) is certified. Define a smaller protected set using

\[
b_0=\bar h\,p(G)-m-\delta\ge0
\]

and the same other floors. For the upper control endpoint use

\[
v_0^{\rm obs}(z)=\min\{R,\underline{\dot D}_0+\alpha b_0\},
\qquad
\underline{\dot D}_0=
\bar h\frac{L}{(L+G)^2}
\left[\eta_Gm\bar h V-\mu_GG\right].
\tag{20}
\]

The lower endpoint is unchanged. The controller requires \(x,C,G,m\) and the certified bound \(\bar h\), rather than observing the actual share \(h\) at every instant. On this set, \(D-m\ge\delta\), so \(h\) cannot fall below \(\bar h\). Moreover

\[
\frac{d}{dt}[\bar h p(G)]\ge\underline{\dot D}_0
\ge-\bar h\mu_G/4.
\]

Consequently the same feasibility and invariance proofs hold, even with the slightly weaker sufficient rate conditions \(R\ge\bar h\mu_G/4\) and \(\alpha\Delta_S\ge\bar h\mu_G/4\). The existing canonical choices satisfy them. This variant still assumes a correct plant and an initially valid lower bound, and does not make unobserved corruption shocks or model error harmless.

The conservative protected set admits full-operation steady targets only when

\[
T\ge2.7,\qquad \bar h\frac{T}{1+T}-\frac T6\ge\delta.
\]

For the canonical choices its upper compatibility bound is approximately 4.2517765033. Even this is not an exact tracking bound for the filter (20): at an actual full-operation steady state its predicted lower \(\dot G\) is \(-(1-\bar h)T\). Thus a zero nominal command remains admissible only if

\[
\alpha\left[\bar h\frac{T}{1+T}-\frac T6-\delta\right]
\ge\bar h(1-\bar h)\frac{T}{(1+T)^2}.
\tag{21}
\]

The conservative filter can restrict tracking before the edge of its protected set. Target 4 satisfies (21) strictly. This distinction between state compatibility and the behavior of a chosen sufficient filter is another reason not to identify an invariant subset with the complete viability kernel.

The bounded conclusion is that an institution can pursue changing targets while preserving explicitly declared operating conditions, if those conditions admit a jointly feasible bounded-rate control and the assumed feedback mechanism is available. A target-only optimization rule can miss those conditions; a proven invariant-region filter can retain them. This is a conditional control result with explicit value choices and implementation assumptions, not a completed account of plural human or AI alignment.
