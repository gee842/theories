# Direction, relational generativity, and effective correction: synthesis and independent audit

Prepared 5 October 2026 for the unified-theory synthesis, after the completion supplement and checkpoint `38f8022`. This memo changes no canonical theory. It distinguishes proved constructions, representational commitments, evaluative commitments, and the remaining causal hypothesis. Mathematical priority is not claimed.

## 1. Recommended center of the unified account

**A differentiated situation produces, consumes, transfers, and sometimes renews the conditions through which further activity, response, and transformation are possible. Some organizations formed within it become causally involved in maintaining those conditions; some can also correct the arrangements through which they are maintained.**

The unit of explanation is the whole relevant situation, containing centers, environments, boundaries, relations, memories, and the inquiry itself. Starting from that unit does not require all centers to have one experience, one interest, or one controller. A boundary is a consequential organization and an accounting choice; it is not permission to omit the dependencies crossing it.

The strongest causal advance in the completed sessions is now substantial: a supplied reaction repertoire can produce its renewal machinery from an initially absent state and converge globally to an active regenerative regime under a calculable material/energy condition. The institutional construction then shows why that result does not already imply 善: the whole's productive support can remain fully renewed while a dispensable affected participant loses a protected capacity. Making that participant's condition effective requires a maintained, executable correction route, with a separate recurring budget, liquidity requirement, and deadline.

The root can be formulated as **conditions becoming participants in the production of further conditions**, with correction becoming one such maintained capacity where its mechanisms arise. The root of wisdom is the corresponding situated practice: retaining and improving contact with consequential differences, and keeping justified responses and revisions executable through their actual costs and effects. This is a candidate philosophical synthesis, not a theorem that every phenomenon is alive, knows, cares, or improves.

A universal theory must explain inert persistence, dormancy, harmful regeneration, exploitation, breakdown, and successful endings as well as active flourishing. “Everything becomes more generative” would exclude precisely the counterexamples the theory must explain.

## 2. Source map and what is inherited

Paths below are exact. Abbreviations only shorten citations inside this memo.

- **R0:** `/Users/ren/theories/sources/20-codex-theory-sessions-2026-10-05/root-of-wisdom/outputs/relational-regeneration-and-direction.md`
- **R1:** `/Users/ren/theories/sources/20-codex-theory-sessions-2026-10-05/root-of-wisdom/outputs/regulating-generative-conditions.md`
- **R2:** `/Users/ren/theories/sources/20-codex-theory-sessions-2026-10-05/root-of-wisdom/outputs/generation-generating-generation.md`
- **R3:** `/Users/ren/theories/sources/20-codex-theory-sessions-2026-10-05/root-of-wisdom/outputs/nonseparation-and-selfhood.md`
- **R4:** `/Users/ren/theories/sources/20-codex-theory-sessions-2026-10-05/root-of-wisdom/outputs/generative-becoming.md`
- **R5:** `/Users/ren/theories/sources/20-codex-theory-sessions-2026-10-05/root-of-wisdom/work/alignment-and-regeneration/model.md`
- **R6:** `/Users/ren/theories/sources/20-codex-theory-sessions-2026-10-05/root-of-wisdom/work/alignment-and-regeneration/ethics-audit.md`
- **N1:** `/Users/ren/theories/sources/20-codex-theory-sessions-2026-10-05/completion-supplement/root-of-wisdom/outputs/endogenous-renewal-mathematics.md`
- **N2:** `/Users/ren/theories/sources/20-codex-theory-sessions-2026-10-05/completion-supplement/root-of-wisdom/outputs/endogenous-renewal-and-consequential-feedback.md`
- **N3:** `/Users/ren/theories/sources/20-codex-theory-sessions-2026-10-05/completion-supplement/root-of-wisdom/outputs/regeneration-and-effective-correction.md`
- **N4:** `/Users/ren/theories/sources/20-codex-theory-sessions-2026-10-05/completion-supplement/root-of-wisdom/work/correctable-regeneration/model.md`
- **N5:** `/Users/ren/theories/sources/20-codex-theory-sessions-2026-10-05/completion-supplement/root-of-wisdom/work/correctable-regeneration/audit.md`
- **N6:** `/Users/ren/theories/sources/20-codex-theory-sessions-2026-10-05/completion-supplement/root-of-wisdom/work/correctable-regeneration/final-scope-review.md`
- **G1:** `/Users/ren/theories/_process/research/2026-10-05-generative-health/MATHEMATICAL-ANALYSIS.md`
- **G2:** `/Users/ren/theories/_process/research/2026-10-05-generative-health/COUNTEREXAMPLES.md`
- **G3:** `/Users/ren/theories/_process/research/2026-10-05-generative-health/RESEARCH.md`
- **G4:** `/Users/ren/theories/_process/research/2026-10-05-generative-health/discovery/DISCOVERY-MATH.md`
- **G5:** `/Users/ren/theories/_process/research/2026-10-05-generative-health/succession/MATHEMATICAL-CORE.md`
- **S1:** `/Users/ren/theories/_process/research/2026-10-04-integrated-evolution/selection-of-renewal.md`
- **S2:** `/Users/ren/theories/_process/research/2026-10-04-integrated-evolution/continuing-participation-math.md`

All the above were read for this audit. The full mathematical proofs in N1 and N4 were independently rederived. The source code in the supplement's `work/correctable-regeneration/check_model.py` was read, but the independent checks below neither import its transitions nor call its verification routines. I did not reverify external empirical papers cited by these reports; the synthesis should preserve their existing narrow source scopes and not turn citations into proof of our exact models.

## 3. Endogenous machinery formation: proof audit

### 3.1 Global deterministic theorem

The supplied model, with positive finite rates and nonnegative states, is

\[
\dot R=kCD-aR,\qquad \dot C=aR-bC,\qquad \dot D=bC-kCD.
\]

The reactions are assembly `R→C`, wear `C→D`, and powered catalysis `D+C→R+C`. The material total is `M=R+C+D`; the energy source maintaining the catalytic conversion is outside these three material variables and explicitly assumed.

At each zero coordinate its derivative is nonnegative. Conservation bounds the solution on the simplex, giving global forward existence. Let `d*=b/k`. Direct integration gives

\[
D(t)-d_*=(D_0-d_*)\exp\left[-k\int_0^t C(s)ds\right].
\]

Thus D moves monotonically toward d* without crossing it and converges to some `ell`. Eliminating R gives the stable scalar filter

\[
\dot C+(a+b)C=a(M-D),
\]

so `C→a(M-ell)/(a+b)`.

If `M>d*` and `R0+C0>0`, both `D0` and `d*` are strictly below M. Monotonicity gives `ell≤max(D0,d*)<M`; therefore the C limit is positive. If `ell≠d*`, then `D'→kC∞(d*-ell)≠0`, contradicting D's convergence. Hence

\[
D_*={b\over k},\quad C_*={a\over a+b}(M-b/k),\quad R_*={b\over a+b}(M-b/k).
\]

If `M≤d*`, D is nondecreasing. Any putative `ell<M` would give `C∞>0` and `b-k ell>0`, hence `D'` bounded away from zero eventually, again a contradiction. Thus `D→M`, `R,C→0`, including the critical equality.

**Verdict:** the proof is sound, including the equality case and boundary exception. It is stronger than the earlier local-regeneration example R0: it proves formation and global attraction throughout the stated active basin.

### 3.2 What is actually endogenous

At `C0=0<R0`, `C'(0)=aR0>0`; the machinery starts absent and forms. The catalytic organization is maintained through turnover. The resting level `D*=b/k` is selected by the reaction rates, not separately inserted as a controller setpoint.

The functional reaction repertoire, positive assembly rate, catalytic specificity, constant-volume kinetic idealization, and energetic driving are still supplied. This derives the abundance and operation of a capable organization; it does not derive why the available chemistry contains that capability. The all-degraded state is absorbing even above the threshold. “Formable without a machinery seed” is justified; “forms from every state” or “creates its own energy source” is not.

### 3.3 Stability and distinct limits

In coordinates `(C,D)` the positive-equilibrium Jacobian is triangular:

\[
J_* = \begin{pmatrix}-(a+b)&-a\\0&-kC_*\end{pmatrix}.
\]

Its eigenvalues are strictly negative. As `kM↓b`, `C*↓0`, and the slow return rate tends to zero. Near all-degraded, the `(R,C)` Jacobian is

\[
J_0=\begin{pmatrix}-a&kM\\a&-b\end{pmatrix},
\]

with determinant `a(b-kM)`. One eigenvalue becomes positive above the same threshold. The threshold's independence of a depends on the absence of a competing loss of R before assembly; it is not a general claim that assembly rate never affects establishment.

For arbitrary recycle flux J, available material `A=R+C` obeys `A'=J-bC`. If J consumes finite work reserve at `E'=-epsilon J`, then

\[
{d\over dt}(A+E/\epsilon)=-bC,
\quad
b\int_0^T C(t)dt\le A_0+E_0/\epsilon.
\]

Finite total work precludes a positive asymptotic average machinery population in this model. Expanding the boundary records the dependency; it cannot erase its cost.

For the finite-particle CTMC with finite positive rates, all states can reach `(0,0,N)` by assembling all R then allowing every C to degrade without a recycling event. Each required event sequence has positive probability. Since the state space is finite and there is no other closed class, absorption is almost sure with finite expected time. No conflict exists between this and deterministic global attraction: infinite-particle and infinite-time limits differ. A finite-population longevity claim requires a separate lifetime calculation, which neither the sources nor this audit supplies.

## 4. Network renewal obstruction and correction observability

### 4.1 Exact insufficient-renewal result

Assume a nonnegative absolutely continuous capacity vector satisfies uniformly over all accessible states

\[
\dot z\le(B-L)z,
\qquad B\ge0,\quad L=\operatorname{diag}(\delta_i)>0.
\]

If `rho(L^-1 B)<1`, then `(L-B)^-1=sum_n (L^-1 B)^n L^-1≥0`. With

\[
w^\top=\mathbf1^\top(L-B)^{-1}>0,
\]

we have `w^T(B-L)=-1^T`, and consequently

\[
(w^Tz)'\le-\mathbf1^Tz\le-{w^Tz\over\max_iw_i}.
\]

This proves exponential decay and `integral 1^Tz≤w^Tz0`. The inverse expansion and weight orientation in N1 are correct. In an acyclic production graph, diagonal multiplication preserves acyclicity, so `L^-1B` is nilpotent and subcritical regardless of finite edge magnitudes.

This proves a **necessary** cycle/adequate-gain condition inside its class. Presence of a cycle, a locally supercritical linearization, or a large gain on one edge is not generally sufficient for bounded persistence. Independent supply changes the bound; durable nondecaying supports, arbitrary time variation, and production without a uniform linear upper bound lie outside it. For the chemical model, the globally valid bound uses `D≤M` and gives `rho=sqrt(kM/b)`; the nonlinear theorem supplies the additional sufficiency result.

### 4.2 The hidden-difference obstruction

For the exact linear plant `e'=aIe-Hu`, with `a>0` and observation `y=e1+e2`, two initial plants differing by `epsilon(1,-1)` and sharing the same deterministic controller state cannot be distinguished by a controller that sees only y. Subtracting their equations under equal commands gives

\[
\delta e(t)=\epsilon e^{at}(1,-1),\qquad \delta y(t)=0.
\]

Well-posedness ensures the constructed equal-output histories indeed produce equal commands. Since their separation grows, both trajectories cannot converge to one reference. This is an exact information restriction, not a claim that every hidden difference requires explicit sensing. It matters here because the hidden mode is unstable and the target requires controlling it.

For the supplied response law `u'=kappa(P+ +hP-)e-gamma u`, the common and difference mode polynomials are

\[
\lambda^2+(\gamma-a)\lambda+(b\kappa-a\gamma),
\quad
\lambda^2+(\gamma-a)\lambda+(b\kappa h-a\gamma).
\]

Both are Hurwitz exactly when

\[
\gamma>a,\quad b\kappa>a\gamma,\quad b\kappa h>a\gamma.
\]

Our exact full-matrix determinant checks independently recover both factors. At `a=1,gamma=2,b kappa=6`, the difference mode with `h=0` has eigenvalues 1 and -2; at `h=1/2` it has roots `(-1±i sqrt3)/2`. Receiving a signal is insufficient unless the pathway into action has enough effective strength and appropriate dynamics.

The chemical and control constructions are separate witnesses. N1 explicitly does **not** couple the construction, energetic maintenance, and adaptation of the observation/controller machinery into the chemical ODE. The unified document must not imply that a single completed physical model already derives chemistry, sensing, cognition, and ethical responsiveness.

## 5. Why selection is not a universal gradient toward renewal

R1's covariance identity

\[
\bar g'-\bar g={\operatorname{Cov}(g,W)\over\bar W}
\]

is exact under fixed inherited types/scores and positive census totals. It places the explanatory burden on the relation between an independently specified capacity score g and actual continuation W. It does not determine the covariance sign.

S1 adds a real mechanism: from production `P(x)=Bx/(h+x)`, contributors retain fraction phi and pay costs `c+kappa phi`. Their relative current return is

\[
s(x;\phi)={\phi B\over h+x}-c-\kappa\phi.
\]

With activity `g(E)=E/(L+E)`, composition changes at `nu g(E)x(1-x)s` and support at `g(E)(1-phi)P(x)-delta E`. On the interior branch,

\[
x_*={\phi B\over c+\kappa\phi}-h,
\quad
E_*={(1-\phi)(B-h\kappa-hc/\phi)\over\delta}-L.
\]

Too little retention fails to sustain contributors, too much fails to fund shared support. For the source's parameters the stable selected equilibria above the declared support floor exist exactly over `(10-sqrt5)/19<phi<3/5`, with the nonhyperbolic composition boundary separately justified in S1. This is a selected-equilibrium feasibility window, not a safe-trajectory certificate or universal optimal property rule.

R5 then allows inherited high-retention traits to spread. With all carriers contributing, `v=B/(h+1)`, `phi_H=1>phi_L`, and `v>kappa`,

\[
\dot p=\nu g(E)p(1-p)(1-\phi_L)(v-\kappa),
\quad
\dot E=g(E)v(1-p)(1-\phi_L)-\delta E.
\]

For every `p0>0`, E tends to zero. Re-derivation: if total active time `tau=integral g(E)dt` is finite, renewal input is integrable and its stable linear convolution decays, hence E→0. If tau is infinite, logistic evolution in tau gives p→1. Eventually `E'≤-delta E/2`, implying finite remaining tau and contradiction. Therefore tau is finite; from an interior initial p, the limiting p is below one. Shared collapse can freeze takeover before fixation.

This is a particularly strong counterexample to the idea that productive individual advantage inevitably selects shared regeneration. Every carrier contributes. Their private retention difference alone can destroy the support required by both. The model's actual copying rule, fixed operating scale, retained-output technology, and energy assumptions remain substantive premises.

## 6. Effective participant correction: exact independent audit

### 6.1 What changes relative to the earlier work

S2 already addresses participation after observations/recommendations and compensation from actual liquid resources. Its one-period repair example yields surplus 0.3, yet the revealed worker refuses without gross compensation in `[0.7,1.3]`. Physical repair costs three; with no borrowing, cash three cannot prefund accepted repair, whereas cash four and compensation one can. Participation, aggregate surplus, and liquidity are distinct.

N3–N4 add repeated replacement of an allocation rule and a material mechanism enabling an affected participant to change it repeatedly. This is a genuine coupling, not merely a renamed transfer constraint. It remains a **supplied institution with maintained operational capacity**, rather than a derivation of the historical creation or strategic persistence of its constitution.

### 6.2 Full accounting and event order

Production is ten each round for shared support `E≥2`; two units repair shared wear. Both allocation templates maintain E. With correction earmark f, F allocates participant 3 and incumbent `5-f`; X allocates participant 1 and incumbent `7-f`. The incumbent-current-return rule selects X outside a binding corrective mandate. Gross production and shared maintenance are identical across the alternatives.

The affected participant, deliberately unnecessary to production, has B capped at six, ordinary demand two, protected end-round floor one. A claim consumes one from B before receipts. The corrective carrier must prefund one upkeep plus two on activation from its stock Q, capped at K; earmark f arrives only after those expenses. An unpaid upkeep round destroys the channel; later receipts do not automatically rebuild it.

When B≤4 and X is active, the affordable automatic claim starts two extraction rounds including its own filing round. Then a binding gate enforces F until B returns to six; the mandate releases and X becomes the current-return winner again.

Thus the participant is causally inside the situation but not an input required for aggregate persistence. Protecting this participant cannot be smuggled in as an automatic consequence of protecting production.

### 6.3 Recurrence proof and exact boundaries

From `E=3,B=6,Q=23/9`, with operative access/authority and `f=11/9,K=3`, the pre-round `(B,Q)` states are

\[
(6,23/9),(5,25/9),(4,3),(2,11/9),(1,13/9),
(2,15/9),(3,17/9),(4,19/9),(5,21/9).
\]

The next state returns to `(6,23/9)` with the same ordinary mode and functioning carrier. This is equality of the full state, not an artificial resource reset. The end-round B minimum is one. Induction proves indefinite protection under the specified unchanged protocol.

Each nine-round cycle receives 90 total resource units: 18 shared maintenance, 11 carrier funding, 19 participant receipts, 42 incumbent receipts. The carrier consumes nine upkeep and two activation; the participant consumes eighteen ordinary need and one filing. The cycle uses no cap overflow.

The carrier's cycle drift before clipping is `9(f-1)-2`. Since discarded surplus is nonnegative and initial Q is finite, infinitely many required cycles are impossible below `f=11/9`. A filing needs three prefunded units, so `K≥3` separately. With `K=3,f=11/9,B0=6`, two ordinary rounds precede the latest safe claim and add `4/9`, giving exact initial condition `Q0≥3-4/9=23/9`.

For positive integral processing delay d, filing cost c, and trigger h, the participant's minimum is `h-c-d`. Therefore protection requires `h≥1+c+d`. With capacity M, the full cycle length is

\[
L=2(M-h)+c+2d,
\]

and the recurring carrier requirement is `f≥m+k/L`. These general formulas presume unit extraction loss and unit restoration gain per round, the supplied integer timing, release at M, and a funded trigger. They are not formulas for arbitrary institution design. In particular d=0 has different within-round accounting and was correctly excluded by the source's prior audit.

Earlier filing can buy a larger reserve margin but increase recurring expense under this compulsory release rule: h=5 gives L=7 and `f≥9/7`, rather than 11/9. Keeping F permanent would avoid this repeated filing bill but would need its own continuing implementation account.

### 6.4 Independent verification and quantitative results

A new standalone exact-Fraction model was written for this audit, reconstructing textual event order without importing source transitions. Results are saved in

- `/Users/ren/Documents/Codex/2026-10-05/fo/work/direction-review/independent_audit.py`
- `/Users/ren/Documents/Codex/2026-10-05/fo/work/direction-review/independent-results.json`

It independently reproduces all source finite-graph counts: 2,380 canonical states, 1,008 satisfying pointwise protection, 272 preserving it indefinitely, seven recurrent attractors, and two protected attractors. It checks every exact successor remains in the enumerated state space and every initial Q on the ninth-unit grid has indefinite protection exactly when Q≥23/9. A separate 125-case family with changed participant ceiling, trigger, delay, and filing cost reproduces the positive-delay timing and cycle formula.

Independently reproduced failure rounds are: participant access absent, round 6; upkeep-only funding, round 15; three-round delay, round 5; funding `109/90=11/9-1/90`, initial Q=K=5, round 194. These exact results distinguish gross lack of access, recurrent underfunding, an unmet deadline, and a large reserve concealing a long-run deficit.

The chemistry checks cover six parameter/preparation cases at two integration step sizes through t=200, with conserved mass and monotone approach of D; 192 exact determinant checks reconstruct the four-dimensional controller polynomial; CTMC reachability checks cover N=1,…,25. These verify the stated constructions; the analytic proofs establish claims beyond finite checked cases. No empirical validation is implied.

### 6.5 Remaining limitations that must survive unification

- Protection is an end-of-round B floor. Ordinary demand may be paid using that round's receipt; filing and Q bills are prefunded. A stronger intraround floor changes the model.
- B measures one specified capacity. It is not a complete welfare, suffering, agency, or personal-identity measure.
- The gate, signal, protected earmark, automatic claim behavior, and replacement law are supplied. Affording them neither creates binding authority nor proves legitimacy or voluntary participation.
- Carrier upkeep makes continued operation resource dependent. There is no separately derived production/inheritance mechanism for the whole constitution, nor reconstruction after channel destruction.
- Disabling the combined access switch does not independently isolate sensing, communication, decision authority, and actuation.
- The fair-rule benchmark supplies permanent enforcement. It is not evidence for free permanent goodness, nor is the X comparison an impossibility theorem about every possible controller.
- A present protected state need not belong to the actual-policy viability kernel. The 272/1,008 count is a finite-state count, not a probability for real institutions.

No new material error was found in the completed N1 or N4 proofs. The source's earlier zero-delay correction is valid and should remain in provenance.

## 7. The coherent connection to transformability and wisdom

G1 distinguishes a viable present from paid establishment of another viable arrangement. With incumbent `c'=alpha u-delta c`, successor progress `x'=beta(1-u)`, floor c*, and `p=delta c*/alpha≤1`, the exact maximum construction by T is

\[
X_{max}(T)=\beta[\min(T,t_0)+(1-p)(T-t_0)_+],
\quad t_0=\delta^{-1}\log(c_0/c_*).
\]

The minimizing maintenance trajectory is `max(c*,c0 exp(-delta t))`; integrating the maintenance equation proves its optimality. If `c0=c*` and p=1, the present can operate indefinitely while every nonzero successor is impossible. Thus existing persistence does not entail the means of transformation.

G4 maintains both operation and inquiry, with exact available nonmaintenance work

\[
B(T)=T-\sum_{i=1}^2p_i(T-t_i)_+,
\quad p_1+p_2\le1.
\]

That work must pay discovery, fresh validation, and installation. A functioning inquiry apparatus can be idle because no work remains to use it. A good discovery can be unusable because installation is unfunded. Fixed noisy testing does not become arbitrarily reliable simply by financing more attempts.

G5 then charges repeated construction, validation, and handoff. For a finite fully observed task/configuration model, its exact reserve recursion is

\[
H_{n+1}(z)=\max_{q\in Q(z)}\min_{a\in A(z,q)}
\max\{c(z,q,a),d(z,q,a)+H_n(f(z,q,a)),0\}.
\]

Here c is actual peak prefix draw and d is net cost; cash arrives when the model says it does. The finite-action monotone-limit argument yields an indefinite certificate where `H∞=sup Hn` is finite. The appearance of a new form does not reset its resource account, and the delivered successor must actually retain the means needed for the next episode.

These modules connect naturally to N3: the correction cycle is an elementary paid succession of temporary rules whose ending state delivers the capacity for its next corrective episode. They need no immortal external governor for their **operational recurrence proof**; but the law/protocol and supporting environment are still premises. A complete unified account should keep formation, maintenance, selection, and meta-correction distinct enough to locate which have actually been explained.

“Wisdom” should therefore be framed as an orientation and capability of situated participants, including their own dependence and fallibility. It involves revising what they attend to when current interfaces hide consequential differences; testing responses; paying for their implementation; checking effects on others; and maintaining or handing on the means of future correction. It does not follow that all regulation has experience, that every life must endlessly innovate, or that personal loss is cancelled by later organization elsewhere.

## 8. Formal integration without overstating the result

A shared state `w` should contain physical supports, differentiated participant conditions, controller/record states, active rules, correction channels, reserves, and handoff phases to the degree required for the claim. Let the actual dynamics be `F_pi`, including its actual selection/replacement law. Let `S` be the independently declared protected conditions and bounded response obligations, including deadlines when necessary.

For a finite deterministic case the actual-policy viable set is

\[
K_\pi=\{w:F_\pi^t(w)\in S\ \forall t\ge0\}.
\]

It is the greatest subset of S mapped into itself by `F_pi`. If controls/disturbances are allowed, the corresponding greatest fixed point instead uses actual observation-compatible policies and the declared quantifier order. The mere existence of an action that stays in S is not evidence that the installed rule chooses, funds, or permits it.

This gives one precise place to compose the modules:

1. The renewal equations determine which material supports persist and which basins can form them.
2. Observation and execution determine which deviations can causally reach a successful response.
3. Participant constraints specify which consequences cannot be erased by an aggregate score.
4. Prefix budgets and deadlines determine whether correction/handoff is reachable before failure.
5. Succession retains the means for subsequent correction or transformation.

These are related causal requirements, not a newly proved universally minimal ontology. In the source institution, `K_pi` has exactly 272 states within the supplied 2,380-state model; in the chemical model, global attraction identifies a different type of result. Naming both “generativity” does not equate their state spaces or evidential status.

A short derived corollary is useful: **no certificate depending only on the institution's shared E and total production history can certify participant protection in this model class.** The participant-effective and no-access trajectories have identical `E=3` and production ten forever, while one maintains B≥1 and the other reaches B=0. Any function of those identical aggregate histories returns the same result for both. This is an immediate indistinguishability counterexample, not a new general information theorem. Participant consequences or a valid mechanism certificate must enter somewhere.

## 9. Direction toward 善: preserve the causal ambition and its burden

The work supports several distinct strengths of direction:

- **Actual local/global restoring dynamics:** proved for specified deterministic renewal and regulation models.
- **Asymmetric continuation constraints:** finite loss without adequate renewal forces failure under the stated assumptions; supported renewal can permit continuation.
- **Selection bias toward a defined regenerative feature:** contingent on the actual variation, transmission, and return mechanisms; counterexamples exist within the corpus.
- **Widening effective responsiveness to affected centers:** operationally demonstrated by a supplied institution, not derived as the inevitable output of chemistry or evolution.
- **A universal direction of reality toward 善:** an open explanatory hypothesis, not a proved corollary of relationality, thermodynamics, persistence, or recurrence.

Keeping the last question open does not replace causal inquiry with ethics. It identifies what the causal inquiry would have to explain: why, under independently specified physical preparations and driving conditions, arrangements that renew multiple affected capacities and retain meaningful correction arise, become accessible, or recur more often than appropriate alternatives. Moral standing should not be restricted to centers a dominant process needs for survival.

A useful next hypothesis can compare probabilities of entering and retaining a declared relationally regenerative regime over a specified horizon, under full dynamics and a controlled intervention that removes a proposed mechanism. Initial preparations, external work, measured consequences, and allowed disturbance must be matched independently. Positive evidence would identify a conditional causal bias. It would not establish universal monotonicity or all-future inevitability.

There is already a decisive limitation on one overly strong formalization. For a finite irreducible time-homogeneous Markov chain with stationary distribution pi>0, if `PG-G≥0` at every state, then averaging against pi gives zero. Every component drift must therefore be zero; finite irreducible harmonic functions are constant by the maximum principle. Thus no nonconstant state scalar has nonnegative expected drift everywhere in this class. Driving does not invalidate the theorem if the effective model remains finite, time homogeneous, and irreducible. A real direction must invoke its actual state space, preparation, transience, absorbing structure, timescale, or changing laws/conditions; a name for the scalar cannot supply the missing mechanism.

The new chemical model illustrates the honest alternative: an actual attracting basin and an excluded inactive boundary under maintained driving. Its finite-particle counterpart illustrates a different direction at sufficiently long times: eventual extinction. Both belong inside the same theory.

## 10. Editorial recommendation

Use the relational situation as the starting point. Make **production and renewal of enabling conditions, including the means of consequential correction and paid transformation**, the central causal thread. Present universal direction toward 善 as the ambitious conjecture this thread makes testable, with the deterministic formation theorem and funded-correction cycle as its strongest current constructive witnesses and the retention/extinction/capture cases as essential constraints.

Do not call the current synthesis a completed physical theory of everything, a universal fitness theorem for goodness, or an empirically established foundation of morality. It can be a coherent formal research theory with explicit premises, exact model results, faithful philosophical commitments, countermodels, and a sharply located frontier. That is stronger than either asserting unsupported cosmic benevolence or abandoning the user's causal question for a generic ethical recommendation.
