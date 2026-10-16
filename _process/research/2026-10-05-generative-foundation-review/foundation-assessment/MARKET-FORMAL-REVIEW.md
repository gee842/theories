# Independent review of the coupled market construction

6 October 2026. AI-authored independent mathematical review within the market study. This review examines the installed model and the exact parameter specification, rather than treating the conceptual proposal as an empirical result. The named connection is **shared consequences → implemented payments → selection → revision of selection conditions**. The governing scope remains the [generative foundation](../../../../theories/becoming/history/GENERATIVE-GROUNDING.md).

**Current decision:** accepted within the stated scope. The equations, primary invariant/recovery constructions and implementation checks below are consistent under their explicit guards. An independent equation implementation reproduced the exact local certificates and all saved finite numerical trajectories within the stated precision. This is acceptance of a conditional model and its reported computation, not a proof that actual markets obey its laws. This review does not certify the separate Lean file.

## 1. Model and accounting inspected

There is a unit mass of service providers. While every indispensable support remains above its physical service floor, each receives fixed receipts \(P\). Renewers pay maintenance \(c\); extractors pay fixed political expenditure \(\ell\) and an effective fine \(fq\). Both pay levy \(\tau\). Thus

\[
\pi_R=P-\tau-c,\qquad
\pi_E=P-\tau-fq-\ell,\qquad
\pi_R-\pi_E=fq+\ell-c.
\]

The solvency assumption \(P\ge\tau+\max(c,f+\ell)\) permits all these payments even at full effective sanction. The fine must appear in its declared restitution ledger; the levy enters the correction fund; maintenance and political spending remain separately accounted expenditures. A restitution payment does not automatically restore a damaged support. The production/receipts law, maintenance technology, enforcement technology and political influence conversion remain supplied local mechanisms.

The state equations inspected are

\[
\begin{aligned}
x'&=x+\eta x(1-x)(fq+\ell-c),\\
w'&=(1-\mu)w+\mu\lambda(1-x),\\
q'&=[(1-\alpha u-\beta w)q+\alpha u-e]_0^1,\\
B'&=\min\{B_{\max},B-ku+\tau\},\\
C_j'&=\max\{0,(1-\delta_j)C_j+(r_j+d_j)x-d_j-h_j-v_j\}.
\end{aligned}
\]

The main installed policy authorizes \(u=1\) exactly when \(B\ge k\); expenditure precedes the current levy. Disbursed cap surplus must be retained in the ledger. The influence parameter \(\lambda=a\ell\le1\) describes the effectiveness of a paid, fixed activity, not wealth accumulated from profits. The share law supplies payoff-sensitive switching; it does not derive the formation of that switching architecture or the voluntary adoption of the levy and enforcement institution.

The physical support guard is essential: a history stops receiving these continuing-service updates when an indispensable support falls below its declared physical floor. Numerical continuation of the equations past that event is only a shadow process. It cannot establish feasible later tax collection, enforcement or recovery.

## 2. Domain and monotonicity

Require \(0<\eta,\alpha,\mu\), \(0\le\beta\), \(\alpha+\beta\le1\), \(0<\mu\le1\), \(0<\delta_j\le1\), \(0\le\lambda\le1\), \(0\le e\le\epsilon\), and \(0\le v_j\le\nu_j\). Let

\[
\theta=(c-\ell)/f\in(0,1),\qquad
\eta\max(c-\ell,f+\ell-c)\le1.
\]

The share increment has the form \(x'=x+A x(1-x)\), where \(-1\le A\le1\). Therefore \(0\le x'\le1\), and

\[
\frac{\partial x'}{\partial x}=1+A(1-2x)\ge0,
\qquad
\frac{\partial x'}{\partial q}=\eta f x(1-x)\ge0.
\]

Consequently corner evaluation is valid for the share bounds, including the recovery box whose lowest accountability is outside the target rectangle. The influence map is increasing in \(w\) and decreasing in \(x\). For funded enforcement, the unclipped accountability map is increasing in \(q\), because \(1-\alpha-\beta w\ge0\), and decreasing in \(w,e\). Support maps are increasing in their own support and in \(x\). Clipping preserves these monotonicities.

## 3. Rectangle certificate and sharpness

For \(0<\bar x<1\), \(0<\bar q\le1\), \(0\le\bar w\le1\), positive support floors and \(B_{\max}\ge k\), consider

\[
\mathcal R=\{x\ge\bar x, q\ge\bar q, w\le\bar w,
\ k\le B\le B_{\max},\ C_j\ge C_{\min,j}\}.
\]

With the ordinary unit-interval restrictions on \(x,q,w\), it is invariant under all admitted disturbances when

\[
\begin{aligned}
\bar q&\ge\theta,\\
\bar w&\ge\lambda(1-\bar x),\\
\alpha(1-\bar q)&\ge\beta\bar w\bar q+\epsilon,\\
\tau&\ge k,\\
(r_j+d_j)\bar x-d_j-h_j-\nu_j&\ge\delta_jC_{\min,j}.
\end{aligned}
\]

Each inequality is independently necessary for invariance of this full product set under the stated law: set the relevant coordinate at its boundary and other coordinates at the adverse admitted corners. These are sharp boundaries for this certificate, not necessary conditions for every safe history or every possible controller. For the share face, equality \(\bar q=\theta\) permits invariance; strict \(\bar q>\theta\) is the stronger condition used for uniform growth below. For a zero support floor, clipping makes its lower-bound condition unnecessary; the primary floor is positive.

## 4. Primary exact parameters

The reviewed primary parameters are

\[
\begin{gathered}
P=10,\quad\tau=k=1,\quad B_{\max}=3,\quad c=2,
\quad f=4,\quad\ell=\tfrac12,\quad\eta=\tfrac15,\\
\alpha=\tfrac14,\quad\beta=\tfrac12,\quad\mu=\tfrac14,
\quad\lambda=1,\\
r=2,\quad d=1,\quad\delta=\tfrac1{10},\quad h=0,
\quad C_{\min}=5.
\end{gathered}
\]

Here \(\theta=3/8\). The share step-size maximum is \(1/2\), strictly within the allowed interval. Solvency holds since \(10\ge1+9/2\).

Take \(\bar x=3/4\), \(\bar q=1/2\), \(\bar w=1/4\), \(\epsilon=1/20\), and \(\nu=1/2\). Exact worst-corner next coordinates are

| Coordinate | Worst next value | Required boundary |
|---|---:|---:|
| Renewer share | \(123/160\) | \(3/4\) |
| Accountability | \(41/80\) | \(1/2\) |
| Influence | \(1/4\) | \(1/4\) |
| Essential support | \(21/4\) | \(5\) |
| Correction fund | \(B\) | \(B\ge1\) |

Thus the primary rectangle is robustly invariant. The influence boundary is an equality, not a strict inward margin. With \(\tau=k\), the fund is constant on this funded region; that assertion must not be extended to initially unfunded states, where a levy can accumulate without an intervention.

## 5. Zero-disturbance convergence inside the rectangle

With \(e=v=0\), the minimum selection coefficient is

\[
\eta(f\bar q+\ell-c)=\tfrac1{10}.
\]

Since \(x\ge3/4\),

\[
1-x'=(1-x)[1-\eta x(fq+\ell-c)]
\le\tfrac{37}{40}(1-x).
\]

Therefore \(x_t\to1\) geometrically. The stable affine recursion for \(w\), driven by \(1-x_t\to0\), gives \(w_t\to0\). Writing \(z_t=1-q_t\), with clipping inactive in the invariant rectangle,

\[
z_{t+1}=\tfrac34z_t+\tfrac12w_tq_t\longrightarrow0.
\]

The conclusion follows from the standard finite-head/vanishing-tail bound on a stable affine recursion, not merely from the displayed forcing tending to zero. Thus \(q_t\to1\). Support remains above five, so its lower clipping is inactive, and

\[
C_{t+1}-20=\tfrac9{10}(C_t-20)+3(x_t-1)
\]

gives \(C_t\to20\) by the same argument. The actual full state approaches the equilibrium family

\[
\{(x,q,w,C,B)=(1,1,0,20,B):1\le B\le3\}.
\]

It does not approach one unique full-state point independent of the initial fund. A version with \(\tau>k\) would reach the fund cap in finite time under continuous funded service. Persistent admitted disturbances retain the invariant guarantee; the zero-disturbance limit must not be transferred unchanged to them.

## 6. Explicit one-step recovery region

Consider initially functioning and funded states with

\[
x\ge\tfrac45,\qquad q\ge\tfrac{49}{100},\qquad
w\le\tfrac{13}{50},\qquad C\ge5,\qquad1\le B\le3.
\]

The same monotonicities give, under the primary disturbance bounds,

\[
x'\ge\tfrac{2546}{3125}=0.81472,\qquad
q'\ge\tfrac{2519}{5000}=0.5038,\qquad
w'\le\tfrac{49}{200}=0.245,\qquad
C'\ge\tfrac{27}{5}=5.4.
\]

Every such state enters \(\mathcal R\) in one step. This is a genuine region extending outside the target rectangle in its accountability and influence coordinates. It is a certified recovery region and, in the zero-disturbance case, a subset of the attracting set's basin. It is not a computation of the entire basin. Its minimum accountability still exceeds \(\theta=3/8\), so it does not by itself establish escape from an initially extraction-favoring selection regime.

The implementation adds a distinct zero-disturbance reversal witness:

\[
(x,q,w,C,B)=(4/5,7/20,1/20,5,1)
\longmapsto(498/625,403/800,7/80,59/10,1).
\]

Its first profit gap is \(-1/10\), so the renewer share initially decreases. Paid restoration nevertheless brings the next state into \(\mathcal R\) before physical failure. This establishes a particular successful reversal of initially adverse selection, while neither implying universal recovery nor erasing the adverse first step.

## 7. Adverse selection and finite physical failure

Under the same primary parameters and zero disturbances, the box

\[
0\le x\le\tfrac1{10},\qquad
0\le q\le\tfrac9{25},\qquad
\tfrac9{10}\le w\le1
\]

is invariant for its three displayed coordinates as long as the process remains physically active. At its adverse upper share/accountability faces,

\[
fq+\ell-c\le-\tfrac3{50},\qquad
x'\le\tfrac{2473}{2500}x,
\]

while \(w'\ge9/10\) and

\[
q'\le\tfrac14+\left(\tfrac34-\tfrac12\cdot\tfrac9{10}\right)
\tfrac9{25}=\tfrac{179}{500}<\tfrac9{25}.
\]

Under the hypothetical continued funded law, \(x\to0\), \(w\to1\), and \(q\to1/3\). Those are shadow limits. Actual service fails earlier. Before failure, the support satisfies

\[
C'\le\tfrac9{10}C-\tfrac7{10}.
\]

For any finite starting support \(C_0\ge5\), indefinite functioning would imply

\[
C_t\le(C_0+7)(\tfrac9{10})^t-7,
\]

which becomes less than five after finitely many steps. This contradiction proves finite physical failure without using fictitious post-failure revenue. The bound applies up to failure; after failure, the untruncated right-hand side cannot serve as an upper bound for a nonnegative clipped stock. The construction demonstrates two different regions under the same installed law: a viable attracting region and a region whose active histories necessarily fail. It does not demonstrate two physically realized stationary market equilibria.

## 8. Scope and retained obligations

The construction makes the reward channel inspectable: the fine, its enforceability, the paid correction capacity and paid political influence jointly determine relative returns. The analyst does not directly pay for an assigned generativity score. Nevertheless the installed levy, authority, fine level, observation law, political-effectiveness law, payoff-switching rule and maintenance technology remain model premises. Explaining their origin, endogenous strategic adoption or justified scope is a further study.

The model's support coordinates protect only admitted supports. It does not infer standing for an unrepresented person, capture all dimensions of market quality, or prove that preserved production makes the regime ethically sufficient. Empirical identification must test the parameter meanings, channels and time scale, and compare conventional institutional models. Exact arithmetic and a simulation audit test implementation and deductions; they cannot establish those empirical or ethical premises.

## 9. Independent implementation and trajectory audit

The [independent audit program](../../../../experiments/market-generativity/independent_check.py) imports neither the model nor its runner. It reconstructs the equations with a separate state representation, different algebraic groupings, and independent cash and fund balances. Its [saved result](../../../../experiments/market-generativity/results/independent-verification.json) fingerprints the reviewed model, runner, original report, original trajectories and audit program.

Exact rational checks passed for all 2,187 primary rectangle grid points, 21,600 broader domain/payment points, 48 steps from short histories of all 12 scenarios, and the three independently calculated boundary/recovery witnesses above. The broader checks retain unaffordable correction, withheld authority, clipping, support failure and the absence of payments after failure. These finite grids support the implementation; the all-state conclusions depend on the hand proofs, not interpolation between grid points.

The audit then recomputed all 12 saved 800-step continuations at 120-digit precision and compared 48,861 scalar coordinates with the original 80-digit trajectories. Every comparison passed the declared absolute tolerance of \(10^{-68}\); the largest observed difference was approximately \(2.979\times10^{-78}\). Operating flags, first failure dates, first support violations, paid-round counts and minimum support values also matched.

| Scenario | First service failure | Other relevant finding |
|---|---:|---|
| Primary renewal region | None through round 800 | 800 paid correction rounds |
| Bounded adverse disturbances | None through round 800 | No admitted support-floor violation |
| Capture region | Round 21 | Matches finite-failure proof |
| Same initial state, capture coefficient zero | None through round 800 | Changed mechanism changes the finite outcome |
| Accountability frozen at its initial low value | Round 21 | A disclosed frozen-rule comparator |
| Accountability frozen at one | None through round 800 | An ideal-rule comparator, not derived adoption |
| First correction unaffordable | Round 5 | The first levy cannot pay the earlier bill |
| Permanent authority veto | Round 28 | No correction bills paid |
| Levy reduced to one half | None through round 800 | 400 paid correction rounds |
| No renewer present initially | Round 19 | Payoff-sensitive switching supplies no absent variant |
| Initially negative profit gap, then correction | None through round 800 | Exact one-step recovery witness above |
| Nonessential recipient excluded from the service guard | None through round 800 | Recipient floor violated in round 1 |

The half-levy case is a substantive limitation to preserve: \(\tau\ge k\) is necessary for the specified continuously funded product rectangle and sufficient for correction every active round. It is not necessary for long-run survival under the general budget-triggered policy. This finite run survives with intermittent repair, paying in 400 of 800 rounds. The run itself supplies no proof of indefinite survival for that alternative regime; such a proof would need a different invariant including its funding phase.

No discrepancy requiring a model correction was found in this audit. The physical-failure guard, qualified funding claim, equilibrium family, supplied technologies and authority, and excluded-recipient counterexample are essential parts of that acceptance.

## 10. Final paper review and corrected hypotheses

The final [mathematical paper](../../../../theories/becoming/chapters/MARKET-DYNAMICS-MATH.md) is accepted as a conditional construction after three explicit corrections made during review. The recovery theorem now inherits Theorem 3's funding and authorization hypotheses: without that qualification its support/share inequalities could hold with \(B=k\) and \(\tau<k\), while the next fund would fall outside the target region. The finite-failure theorem now requires a nonempty essential-support set and the recurring-funding hypotheses; with no essential supports, harm to every nonessential coordinate would not activate economic shutdown. Finally, the recovery box is called external rather than larger, since the supplied collar extends outside the target in some coordinates while imposing a stronger lower share and need not contain the target rectangle.

The general clipped-stock argument in Theorem 6 is valid. Under its hypothetical indefinitely operating history,

\[
0\le C^j_{t+1}\le(1-\delta_j)C^j_t+(r_j+d_j)x_t,
\]

because \(d_j+h_j\ge0\). The right-hand recurrence contracts with a vanishing input, proving convergence to zero even when the limiting negative forcing is clipped. A positive essential floor therefore supplies the finite-failure contradiction; no conclusion relies on actual receipts after failure.

Equation (14) is also valid with its stated \(0<\delta_j<1\) restriction. Before the first violating prefix, the positive floor makes clipping inactive and the ordinary affine unfolding is exact. At that first prefix, \(\max(0,z)<L_j\) holds exactly when \(z<L_j\), since \(L_j>0\). Thus clipping cannot invalidate either implication of the claimed floor-feasibility equivalence. The separate \(\delta_j=1\) condition is correct.

The recovery monotonicity, exact instance margins, collar bounds and negative-gap witness agree with the preceding independent audit. Attraction is appropriately limited to a certified set of initial conditions converging to the specified equilibrium set, with the inherited fund retained. The paper does not compute the whole basin or turn a finite numerical continuation into an asymptotic theorem. No additional computation was needed for these exposition and hypothesis corrections.
