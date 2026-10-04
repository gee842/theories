# Independent authority and feasible correction

This experiment extends the manuscript’s selected influence capacity model by making effective correction depend on enforceable authority that influence can erode. It derives an authority reserve sufficient to preserve the existing row-gain certificate, and a separate deadline test showing when a reform cannot act soon enough. The proofs concern the specified equations. The numerical checks verify implementation and illustrate counterexamples; they are neither empirical evidence nor a novelty claim. No evaluator-succession benchmark outcomes are reported here.

The starting points are [Section 4](../../drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/core/40_s4.md), its [S4 proofs](../../drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/supp/04_S4.md), and the open correction-production interface in [S13](../../drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/supp/13_S13.md). The initial proposal is recorded in the [contribution-space note](../../sources/15-codex-theory-conversations/2026-10-04-alignment-coordination-contribution-space.md). This experiment does not change the canonical manuscript.

## Model and assumptions

Specialize the manuscript to quadratic variable cost, no per-unit cost floor, no background conversion into evaluation, a fixed carrier share and profile, uniform effective correction, and the long-horizon approximation for the return to influence. In its notation these assumptions are \(\eta=1\), \(f=A=0\), fixed \(p,\bar y,\gamma,\xi_v\), and \(L_i=1\). Define

\[
C=\frac{\chi\hat Y}{\gamma p^{\xi_v}}>0,
\qquad K=\frac{a_{\rm ev}\hat B}{c_{\rm ev}}>0.
\]

The size-cost factor \(p^{\xi_v}\) must be included in \(C\); it disappears only if \(\xi_v=0\) or has explicitly been absorbed into the cost coefficient. Let \(D>0\) be nominal correction capacity and \(\ell\in(0,1]\) independent enforceable authority. The proposed production relation and existing conditional optimum are

\[
d_{\rm eff}=D\ell,
\qquad q^*(\ell)=\frac{C}{D\ell},
\qquad G=\frac{Kq}{D\ell}.
\]

Here \(q\ge0\) is cultivated influence capacity, and \(G<1\) is the manuscript’s row-gain certificate. The fixed-authority threshold at selected capacity is

\[
d_{\rm base}^*=\sqrt{KC}.
\]

Authority follows the additional, explicitly assumed relation

\[
\dot\ell=\rho_\ell(1-\ell)-\kappa_\ell q\ell,
\qquad \rho_\ell>0,\quad\kappa_\ell\ge0.
\]

The regeneration rate \(\rho_\ell\) and erosion coefficient \(\kappa_\ell\) are distinct from similarly named parameters elsewhere in the manuscript. The implementation calls them `rho` and `kappa` inside this isolated model. Authority is a scalar here; appointments, access, budgets, and execution rights have not yet been separated into components.

The same \(d_{\rm eff}\) enters both the return that selects influence capacity and the damping of evaluation-domain support. Thus the authority multiplier affects all corrector domains supplying that return uniformly. If it degrades only evaluation while the return to influence is earned under a different correction rate, this model and its reserve formula do not apply unchanged.

The optimum \(q^*(\ell)\) holds current authority fixed. It is an instantaneous, conditional optimum, not a derived solution to a strategic problem in which an actor anticipates how its influence will change future authority. Finite-speed payoff-gradient adjustment can implement the assumed local response. Financing, legitimacy, and the selection stability of authority rebuilding are still outside this model.

## Proposition 1 Authority reserve under instantaneous adjustment

Define \(R=\kappa_\ell C/\rho_\ell\). Under instantaneous adjustment \(q=q^*(\ell)\), with constant parameters,

\[
\ell^*=1-\frac{R}{D},
\qquad
\ell(t)=\ell^*+(\ell_0-\ell^*)e^{-\rho_\ell t},
\qquad
d_{\rm eff}^*=D-R.
\]

If \(\ell_0\in(0,1]\) and \(D>R\), this solution remains positive. It has a uniform strict row-gain margin, meaning \(\sup_{t\ge0}G(t)<1\), if and only if

\[
\min\{D\ell_0,D-R\}>d_{\rm base}^*.
\]

In particular, its limiting row gain is strictly below one exactly when

\[
\boxed{D>d_{\rm base}^*+\frac{\kappa_\ell C}{\rho_\ell}.}
\]

**Proof.** Substituting \(q^*(\ell)\) cancels \(\ell\) from the erosion term, giving \(\dot\ell=\rho_\ell(1-\ell)-\kappa_\ell C/D\). Solving the scalar linear equation gives the stated path. It is monotone between its initial value and its limit, so \(\inf_{t\ge0}D\ell(t)=\min\{D\ell_0,D-R\}\). Since \(G(t)=KC/[D\ell(t)]^2\), the equivalence follows. ∎

The equality case matters. If \(D-R=d_{\rm base}^*\) and \(D\ell_0>d_{\rm base}^*\), then \(G(t)<1\) at every finite time but \(G(t)\to1\). The boxed strict condition characterizes a strict limiting margin, not every possible finite-time strict inequality. When \(D<R\), the instantaneous-adjustment solution can reach zero authority in finite time while \(q^*\) diverges. The approximation must stop before that singularity; it does not describe a negative-authority society.

## Proposition 2 A certificate for finite adjustment speeds

Let \(\dot q=F(t,q,\ell)\) have a unique solution, with sufficient continuity and local Lipschitz regularity for the boundary invariance argument. Assume \(F(t,0,\ell)\ge0\) and

\[
F(t,q,\ell)\le0\quad\text{whenever }q\ge q^*(\ell).
\]

These conditions allow inherited influence above the current optimum; they prevent it from increasing further there. They do not require convergence to the optimum. Linear adjustment \(F=\nu(q^*-q)\), \(\nu\ge0\), is one example.

If the boxed reserve condition holds, choose

\[
\frac{d_{\rm base}^*}{D}<m\le1-\frac{R}{D},
\qquad Q=\frac{C}{Dm}.
\]

Then the rectangle

\[
\mathcal R_m=\{(\ell,q):m\le\ell\le1,\;0\le q\le Q\}
\]

is forward invariant. Every trajectory starting there satisfies the uniform bound

\[
G(t)\le\frac{KC}{D^2m^2}<1,
\]

independently of its permitted adaptation speed.

**Proof.** On \(\ell=m\), the smallest authority derivative occurs at \(q=Q\), where

\[
\dot\ell\ge\rho_\ell(1-m)-\kappa_\ell Qm
=\rho_\ell(1-m)-\frac{\kappa_\ell C}{D}\ge0.
\]

On \(\ell=1\), \(\dot\ell=-\kappa_\ell q\le0\). On \(q=Q\), \(q^*(\ell)\le C/(Dm)=Q\), so \(F\le0\). On \(q=0\), \(F\ge0\). Thus the vector field points inward or tangentially at each boundary. Regularity gives invariance, and the compact region prevents finite-time escape. Maximizing \(Kq/(D\ell)\) over this rectangle gives the stated bound. The permitted interval for \(m\) is nonempty exactly when \(D>d_{\rm base}^*+R\). ∎

This is sharp for this family of rectangular certificates uniformly covering every adjustment law with the stated sign restrictions. For a rectangle \([m,1]\times[0,Q]\), an upper capacity boundary must have \(Q\ge C/(Dm)\) to cover adjustment laws that increase below their optimum. Authority invariance requires \(\rho_\ell(1-m)\ge\kappa_\ell Qm\). A uniform row certificate requires \(KQ/(Dm)<1\). Combining these yields the same reserve inequality.

It is not a necessary condition for every trajectory. For example, \(q(0)=0\) and \(F=0\) give \(G=0\) even below the reserve threshold. Nor is a nominal reserve plus \(G(0)<1\) sufficient when initial influence lies outside the certified stock bounds. Finally, the row certificate is not a guarantee of present independence, removal of existing rule support, or avoidance of harm already under way. Section 4’s additional requirements for a decision-usable corrector still apply.

## Proposition 3 A bound on correction before a deadline

At intervention time \(\tau\), suppose persistent rule support is \(s_\tau>c/a>0\). During the intervention it satisfies

\[
\dot s=\varepsilon(I(t)-d_{\rm eff}(t)s),
\qquad I(t)\ge0,\quad d_{\rm eff}(t)\ge0,\quad\varepsilon>0.
\]

The current payoff advantage remains positive while \(as>c\). The intervention is restricted to damping support; it does not directly reset \(s\), change \(a,c\), suspend the practice, or repair the host. Let \(\ell_\tau\in[0,1]\), and suppose authority and available correction obey

\[
\dot\ell\le\rho_\ell(1-\ell),
\qquad 0\le d_{\rm eff}\le D\ell.
\]

For \(\Delta=T-\tau\ge0\), define

\[
H_\tau=\frac1\varepsilon\log\frac{as_\tau}{c},
\qquad
U(\Delta)=D\left[\Delta-
\frac{(1-\ell_\tau)(1-e^{-\rho_\ell\Delta})}{\rho_\ell}\right].
\]

Reaching even the neutral threshold \(as\le c\) at some time by \(T\) requires \(U(\Delta)\ge H_\tau\). Thus \(U(\Delta)<H_\tau\) certifies that this intervention class cannot neutralize the current advantage by that deadline. Strict reversal requires a strict dose surplus in the best case.

**Proof.** The integrating-factor solution gives, for every \(t\in[\tau,T]\),

\[
s(t)=s_\tau e^{-\varepsilon\int_\tau^t d_{\rm eff}}
+\varepsilon\int_\tau^t I(v)
 e^{-\varepsilon\int_v^t d_{\rm eff}}\,dv
\ge s_\tau e^{-\varepsilon\int_\tau^t d_{\rm eff}}.
\]

Scalar comparison gives \(\ell(t)\le1-(1-\ell_\tau)e^{-\rho_\ell(t-\tau)}\). Integrating \(d_{\rm eff}\le D\ell\) bounds its cumulative dose by \(U(t-\tau)\). This upper bound is nondecreasing. If \(U(\Delta)<H_\tau\), support therefore stays strictly above \(c/a\) throughout the interval, not merely at its endpoint. ∎

The bound is attained in the relaxed best case of no incoming support, no authority erosion, maximal rebuilding, and \(d_{\rm eff}=D\ell\). Equality gives neutralization exactly at the deadline. In the coupled authority model, positive incoming support or continuing erosion can prevent attainment. Passing this necessary test is not sufficient for feasibility. To infer host-floor crossing, one must separately establish that continued advantage necessarily crosses that floor by the deadline; this model supplies no such host premise by itself.

## Deterministic verification

Run `python3 experiments/evaluator-succession/authority_model.py --output experiments/evaluator-succession/authority_results.json` from the repository root. The script uses only the Python standard library, checks all results before writing JSON, records its source hash, and never clips or projects numerical states back into the proposed safe region. [The saved output](authority_results.json) records parameters, extrema, error checks, and sampled crossings. The [implementation](authority_model.py) contains no evaluator-succession benchmark outcomes.

Every finite-adjustment trajectory is computed with classical RK4 at step 0.02 and again at step 0.01. Their maximum state disagreement at matching times must be below \(10^{-5}\). The quasi-static equation is separately compared with its analytic solution at both steps; halving the step reduced the error by approximately 16.13, consistent with fourth-order convergence. These are deterministic implementation checks over finite horizons, not proofs of continuous-time invariance or a complete numerical analysis.

| Check | Parameters and result | What it establishes |
|---|---|---|
| Invariant rectangle | \(C=K=\rho_\ell=1,\kappa_\ell=0.4,D=1.6,m=0.7\). Four boundary corners at adjustment rates 0.05, 1, and 10 stayed inside through time 20; the gain bound is 0.797194. Maximum step-halving state disagreement was \(5.48\times10^{-6}\). | The implementation agrees with the certificate for these twelve trajectories. |
| Inadequate reserve with tracking | \(D=1.3\), otherwise the same constants, \(\ell_0=1,q_0=1/1.3,\nu=1\). The gain starts below one, first reaches or exceeds one on the fine grid at time 2.45, and approaches 1.234568. | Nominal capacity above the fixed-authority threshold can lose the certificate. |
| Equality at the reserve threshold | \(D=1.4\), instantaneous adjustment, \(\ell_0=1\). Gains at times 1, 5, and 10 are below one but converge to one. | Finite-time strict inequality is different from a uniform strict margin. |
| Oversized inherited influence | \(D=1.6,\ell_0=1,q_0=1.5,\nu=0.001\). Initial gain is 0.9375; the first fine-grid crossing is at 0.12 and the maximum observed gain is 1.496007. | The reserve condition does not replace initial-stock bounds. |
| No authority erosion | \(\kappa_\ell=0,D=1.2\). The added reserve is zero and the checked trajectory retains the certificate. | Reduction to the fixed-authority threshold. |
| No tracking below the threshold | \(D=0.8,q_0=0,\nu=0\). Gain remains zero. | Reserve failure is not universal capture. |
| Deadline shortage | \(D=1.6,\rho_\ell=1,\ell_\tau=0.2,s_\tau=4,c/a=1,\varepsilon=1\). Required dose is 1.386294; by elapsed time 1, at most 0.790886 is available. Best-case support remains 1.813772. | Damping cannot neutralize the advantage by this deadline. |
| Best-case neutralization | For the same parameters, the earliest relaxed best-case neutralization is at elapsed time 1.485283; support at time 2 is 0.493153 with zero incoming support. | The dose bound can be attained under its relaxed assumptions. |
| Continuing incoming support | Incoming support \(I=10\) leaves support at 7.717721 at elapsed time 2, despite adequate best-case cumulative dose. | Meeting the necessary dose threshold is not sufficient. |
| Direct-removal escape | Resetting support to 0.5 removes the current advantage immediately. | The impossibility bound does not cover direct removal; this escape says nothing about lasting safety. |

Crossing times in the table are sampled at step 0.01, not exact event times. All parameters are illustrative and dimensionless. No institutional measurements or empirical thresholds have been fitted.

## Interpretation and remaining work

The model separates nominal correction capacity from the authority needed to exercise it. Its conditional prediction is that increasing evaluator spending can coexist with declining effective correction when the evaluated can erode access or executive independence. A study should measure those channels separately rather than infer authority from budget or the formal presence of an override.

The next substantial extension must explain the resources and authorization behind \(\rho_\ell\), and test whether rebuilding itself survives evaluator succession. Strategic agents anticipating authority changes, multiple authority components, finite selection horizons, nonquadratic costs, background conversion, and time-varying carrier shares can change the threshold. The finite-time test already shows why a satisfactory eventual equilibrium is an incomplete reform criterion.

This uses established boundary-invariance and comparison reasoning. [Control-barrier methods](https://arxiv.org/abs/1609.06408) and work on [degraded control authority](https://arxiv.org/abs/2310.15132) are relevant precedents. The candidate contribution is the explicit coupling to the manuscript’s selected influence capacity and the resulting, testable authority and deadline conditions. Its originality has not been established by a comprehensive literature review.
