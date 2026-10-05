# Selection over renewal practices with paid appropriation

Mathematical working memo, 5 October 2026. AI-generated research derivation, prepared for Ren's foundational program and intended for independent checking by the coordinating agent. This is a restricted mechanism model, not a universal claim about property, markets, cooperation, or alignment. No originality claim is made.

## 1. What this module adds

The earlier [integrated dynamics model](integrated-dynamics.md) changes maintenance's relative return through a fixed compensation parameter. The [endogenous-renewal model](endogenous-renewal-math.md) makes correction consume support and reproduce its own capacity, but does not select among operating rules.

This memo makes a maintenance reward come from an explicit share of actual production. Retaining more of that production can help the maintenance practice spread, while leaving less output to maintain shared support. A claim/enforcement cost is charged to contributors. The resulting selection advantage depends on how many contributors exist, and a support floor can select a bounded interval of admissible appropriation rules.

Operating scale is fixed in this module. It describes replacement of practices among a fixed mass of carriers; it does not track demographic growth or recover the earlier model's absolute-population dynamics. Support depletion slows both production and revision. The appropriation rule itself remains a parameter, and its institutional persistence remains to be modeled.

## 2. Explicit production, allocation, and costs

Let \(x\in[0,1]\) be the share using maintenance practice \(R\); the remainder uses practice \(D\). Labels refer to practices, not moral kinds of people. Let \(E\geq0\) denote shared functional support, and define the activity factor

\[
g(E)=\frac{E}{L+E},\qquad L>0.
\tag{1}
\]

The gross output per unit active time is

\[
P(x)=\frac{Bx}{h+x},
\qquad B>0,\ h>0.
\tag{2}
\]

This is a stipulated diminishing-return production technology. Output vanishes without contributors and is bounded. Resources or opportunities outside the modeled boundary supply this production; it is not energy created from functional support.

A fraction \(\phi\in[0,1]\) of output is earmarked for contributors and distributed equally among them. The rest replenishes shared support. For \(x>0\), the retained output per contributor is

\[
\frac{\phi P(x)}x=\frac{\phi B}{h+x}.
\]

Each contributor pays maintenance cost \(c>0\) and an additional claim, accounting, or enforcement charge \(\kappa\phi\), where \(\kappa\geq0\). These costs are private resource or opportunity costs per active time; they must be funded from the carrier's operating budget. A common operating-income component can be added to both practices and cancels from the comparison below. This is an accounting of differential current returns, not a complete material model of those private budgets.

The private return difference per active time is therefore

\[
\boxed{
s(x;\phi)=\frac{\phi B}{h+x}-c-\kappa\phi.
}
\tag{3}
\]

The retained reward is not supplied as a free bonus. The production split satisfies

\[
x\left[\frac{\phi P(x)}x\right]+(1-\phi)P(x)=P(x).
\tag{4}
\]

Enforcement expenditure additionally leaves contributors' private budgets. Its recipients, institutional capacity, and possible recycling are outside this module. Where exclusion is physical rather than institutional, \(\kappa\phi\) may instead represent a measured retention cost. The linear cost law is an assumption to test.

This one-for-one division assumes a divisible flow. It should not be applied unchanged to information or other outputs that can be shared without comparable subtraction.

## 3. A microscopic replacement process and its mean dynamics

Suppose a carrier samples another carrier and switches to its practice at a rate proportional to the positive current-return advantage. The per-carrier switching rates are

\[
k_{D\to R}=\nu xg(E)[s(x;\phi)]_+,
\qquad
k_{R\to D}=\nu(1-x)g(E)[-s(x;\phi)]_+,
\qquad \nu>0.
\tag{5}
\]

These nonnegative event rates specify an imitation mechanism. They do not assume that carriers maximize long-run support or social welfare. Current-return imitation is an empirical behavioral assumption, not a universal theory of learning.

The corresponding deterministic mean balance is

\[
\boxed{
\begin{aligned}
\dot x&=\nu g(E)x(1-x)s(x;\phi),\\
\dot E&=g(E)(1-\phi)P(x)-\delta E,
\qquad \delta>0.
\end{aligned}}
\tag{6}
\]

For finite carrier counts, (5) gives a stochastic switching process; (6) is its large-population approximation, not an exact closed equation for expected nonlinear states. Pairwise proportional imitation and its replicator mean dynamics are established mathematics; [Sandholm's primary analysis](https://doi.org/10.3390/g1010003) explicitly discusses this derivation and the limitations of purely imitative boundaries.

Both resource allocation and costs are incurred at activity rate \(g(E)\). The factor also slows revision as support disappears. Equation (6) is thus coupled in both directions, although a common factor preserves a simple sign structure for selection.

The rectangle \(0\leq x\leq1,\ E\geq0\) is invariant, and

\[
\dot E\leq B-\delta E
\]

gives boundedness. At \(E=0\), both dynamics stop. This absorbing boundary excludes restarting through outside aid or spontaneous reconstruction. It means cessation of modeled activity, not a proof that every carrier literally dies.

## 4. Invasion and persistence are separate from support viability

For \(\phi>0\),

\[
s'(x;\phi)=-\frac{\phi B}{(h+x)^2}<0.
\tag{7}
\]

Thus the private advantage of contributing decreases with contributor prevalence. Conditional on positive activity:

- Contributors increase when rare exactly when
  \[
  s(0;\phi)=\frac{\phi B}{h}-c-\kappa\phi>0.
  \tag{8}
  \]
- At a positive pure-contributor support equilibrium, a rare noncontributor has a strictly negative linear invasion exponent exactly when
  \[
  s(1;\phi)=\frac{\phi B}{h+1}-c-\kappa\phi>0.
  \tag{9}
  \]
- If \(s(0)>0>s(1)\), there is a unique stable interior composition
  \[
  \boxed{x_*=\frac{\phi B}{c+\kappa\phi}-h\in(0,1).}
  \tag{10}
  \]

These statements follow directly from the sign of the first equation in (6). At \(\phi=0\), \(s=-c\) everywhere. Boundary equality cases require separate nonhyperbolic analysis and are not covered by the strict stability claims.

In particular, a zero linear invasion exponent does not imply neutral nonlinear dynamics. If \(s(1)=0\) and \(\phi>0\), then \(s'(x)<0\) makes \(s(x)>0\) for \(x<1\). Under sustained positive activity, rare noncontributors decline at quadratic leading order. Thus the strict condition in (9) characterizes a negative linear exponent, not every possible form of resistance to invasion.

The phrase “increase when rare” in (8) concerns an active state with inherited support. The all-noncontributor ecological equilibrium has \(E=0\), so this model supplies no positive-activity resident equilibrium there from which successful invasion could automatically be inferred. A favorable rare-type sign cannot restart a completely depleted system.

More formally, define active time

\[
\tau(t)=\int_0^t g(E(s))\,ds.
\]

Where activity is positive, \(dx/d\tau=\nu x(1-x)s(x;\phi)\). If total active time is infinite, composition approaches the root selected by this one-dimensional equation. If total active time is finite, the bounded integrable input \(g(E)(1-\phi)P(x)\) and the linear loss equation imply \(E\to0\); practice change can stop before its limiting active-time composition is attained.

### Exact viable-but-invasible result

At \(x=1\), a positive support equilibrium exists precisely when

\[
E_R=\frac{(1-\phi)B}{\delta(h+1)}-L>0.
\tag{11}
\]

Its ecological eigenvalue is \(-\delta E_R/(L+E_R)<0\). For a rare noncontributing practice \(y=1-x\), the invasion exponent is

\[
\boxed{
\lambda_{D\mid R}
=-\nu g(E_R)s(1;\phi).
}
\tag{12}
\]

Hence a pure-maintenance regime may have \(E_R>E_{\min}\) and recover from small support perturbations, while remaining unstable to replacement by a noncontributing practice. This result uses independently specified output allocation and current-return copying; “goodness” is absent from the switching rates.

Conversely, \(s(1)>0\) makes the pure-maintenance practice resistant to this particular invader, but it does not ensure (11) exceeds a support floor. Excessive earmarking can leave too little shared renewal.

## 5. A stable interior state and an explicit retention window

In the interior regime (10), define

\[
D=B-h\kappa,\qquad H=hc.
\tag{13}
\]

At the selected composition, gross production remaining public is

\[
\boxed{
R_*(\phi):=(1-\phi)P(x_*)
=(1-\phi)\left(D-\frac H\phi\right).
}
\tag{14}
\]

A positive support equilibrium exists if \(R_*(\phi)>\delta L\), with

\[
\boxed{E_*=\frac{R_*(\phi)}{\delta}-L.}
\tag{15}
\]

This equilibrium is locally asymptotically stable. The Jacobian is lower triangular because \(s(x_*)=0\), and its diagonal entries are

\[
\nu g(E_*)x_*(1-x_*)s'(x_*)<0,
\qquad
-\frac{\delta E_*}{L+E_*}<0.
\tag{16}
\]

For a required floor \(E_{\min}>0\), put

\[
Q=\delta(L+E_{\min}).
\]

A strict support margin requires \(R_*(\phi)>Q\), or equivalently

\[
\boxed{D\phi^2-(D+H-Q)\phi+H<0.}
\tag{17}
\]

The solution must also satisfy \(0<\phi<1\) and \(0<x_*(\phi)<1\). An algebraic root outside the interior-composition regime is not a valid bound for this branch.

If \(D>H>0\), the unconstrained interior-branch public flow is strictly concave:

\[
R_*'(\phi)=-D+\frac{H}{\phi^2},
\qquad
R_*''(\phi)=-\frac{2H}{\phi^3}<0.
\]

Its unique maximum on \((0,1)\) occurs at

\[
\boxed{
\phi_{\mathrm{opt}}=\sqrt{\frac HD},
\qquad
R_{*,\max}=(\sqrt D-\sqrt H)^2.
}
\tag{18}
\]

Formula (18) is the actual interior-branch optimum only if \(\phi_{\mathrm{opt}}\) also satisfies (10). Otherwise the composition boundary must be evaluated. No universal optimal appropriation fraction follows.

When the strict inequality \(Q<(\sqrt D-\sqrt H)^2\) holds, the algebraic support interval is between

\[
\phi_\pm=
\frac{D+H-Q\pm\sqrt{(D+H-Q)^2-4DH}}{2D},
\tag{19}
\]

intersected with the interior regime. Once selection reaches \(x=1\), the correct public flow is instead

\[
R_R(\phi)=\frac{(1-\phi)B}{h+1},
\]

which strictly decreases with \(\phi\).

The mechanism creates two different limitations: insufficient retained return cannot pay contributors' costs, while excessive retention can deprive shared support even though contribution remains individually favored. Enforcement cost narrows the available range through \(D=B-h\kappa\).

## 6. Analytical illustration

Take

\[
B=4,\quad h=c=\delta=1,\quad \kappa=.2,\quad
L=.1,\quad E_{\min}=.7,
\]

with any \(\nu>0\). These are illustrative dimensionless parameters, not estimates.

| Retained fraction \(\phi\) | Active-time selected composition | Positive selected support | Assessment relative to \(E_{\min}=.7\) |
|---|---:|---:|---|
| .1 | \(x\to0\), if activity lasts sufficiently long | No positive selected equilibrium | Pure maintenance would support \(E_R=1.7\), but a noncontributor invades |
| .3 | \(x_*=7/53\approx.1321\) | \(E_*=17/75\approx.2267\) | Maintenance is selected when rare, but support remains below the floor |
| .5 | \(x_*=9/11\approx.8182\) | \(E_*=.8\) | Stable equilibrium exceeds the floor |
| .8 | \(x\to1\), if activity lasts sufficiently long | \(E_R=.3\) | Full contribution is stable, but public support is below the floor |

The interior optimum is

\[
\phi_{\mathrm{opt}}=\frac1{\sqrt{3.8}}\approx.5130,
\qquad
E_{*,\max}=(\sqrt{3.8}-1)^2-.1\approx.8013.
\]

The pure-contributor branch begins at \(\phi=5/9\). At this boundary,
\[
s(x)=\frac{10(1-x)}{9(1+x)},\qquad E^*=\frac{71}{90}>.7.
\]
The share increases toward one from the physical side \(x<1\), with quadratic decay of the rare noncontributor; the ecological direction is stable. Near this positive equilibrium activity remains bounded away from zero, so the state is asymptotically stable relative to the physical domain despite a zero composition eigenvalue. This separate argument justifies including the boundary when combining the branches. Stable selected equilibria strictly above the support floor occur for

\[
\boxed{\frac{10-\sqrt5}{19}<\phi<\frac35.}
\tag{20}
\]

The endpoints have no support margin. This interval concerns selected-equilibrium feasibility; it does not certify that every initially admissible state stays above the floor. The temporary resource cost of reaching a new regime and the basin of sufficient activity require separate analysis.

Independent proof review identified the need for the equality argument above. The initial wording conflated strict linear resistance with all resistance to invasion; this working memo was corrected, and the change is retained in the research log.

## 7. Established mathematics and close primary prior art

[Gore, Youk, and van Oudenaarden (2009)](https://www.nature.com/articles/nature07921) experimentally and theoretically study yeast cooperation with partially retained benefits and nonlinear returns. Their system exhibits frequency-dependent advantages and coexistence. It is a close precedent for why incomplete sharing can support contributors; it does not validate this memo's production or enforcement functions.

[Lerch et al. (2022)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010666) explicitly model production and privatization of microbial resources, derive conditions under which production persists, and distinguish environmental contexts. Their resource-explicit analysis also shows that successful producers can reduce extracellular resource availability through increased population density. That mechanism is absent at our fixed operating scale. This is especially close prior art, and rules out claiming a new general principle that appropriation sustains public production.

[Sandholm (2010)](https://doi.org/10.3390/g1010003) gives established microfoundations for revision protocols and their deterministic population dynamics. The present switching law uses a standard imitative protocol, with the usual inability to create a practice that has disappeared.

The model and calculations here were assembled for this research program. Their specific novelty has not been established. The local contribution is an auditable connection among actual production, its division, paid claiming, practice replacement, support-dependent activity, and an independently declared support floor.

## 8. Relationship to the coordinating agent's paid-renewal copying extension

The coordinating agent separately proposed two operating practices \(u_H>u_L\) carried by capacities \(C_H,C_L\), using the existing paid-renewal model. With current-cost copying from \(H\) to \(L\) at flow

\[
J=\kappa_{\mathrm{copy}}E(u_H-u_L)\frac{C_HC_L}{C_H+C_L},
\]

the share balance is

\[
\dot x=(\eta-\kappa_{\mathrm{copy}})E(u_H-u_L)x(1-x).
\]

This agent checked that copying cancels from total capacity and the support-plus-converted-capacity balance. The coordinator's two-case proof also checks: if \(\int E\,dt<\infty\), capacity decays from its per-capita loss; if \(\int E\,dt=\infty\) and \(\kappa_{\mathrm{copy}}>\eta\), the low-intensity practice takes over. When \(u_L\) is below the paid-renewal feasibility threshold, an eventual upper bound on average intensity permits the earlier logarithmic extinction estimate.

That mechanism assumes imitation responds to immediate expenditure saved while ignoring the associated replacement benefit. It should be measured as a behavioral restriction, not represented as universally rational choice. It is complementary to this memo's explicit division of produced benefits. The symbol \(\kappa_{\mathrm{copy}}\) is distinct from the enforcement cost \(\kappa\) used above.

## 9. What remains unproved or untested

- The parameter \(\phi\) is an allocation rule; the model does not explain which coalition adopts it, prevents false claims, revises it, or maintains enforceable authority. Charging a fee exposes a cost but does not establish that enforcement exists or works.
- The actual finite-population process can lose a practice through stochastic absorption even near a stable deterministic mixture. Innovation or external reintroduction would require additional events.
- Fixed operating scale omits rebound effects, endogenous population density, and expansion of extraction. The close resource-explicit prior art shows why those omissions can change conclusions.
- Maintenance and claiming costs must fit available private budgets. Their financing and distribution are not inferred from the shared support equation.
- The particular production and activity functions require independent evidence. Support could affect payoff differences asymmetrically, and learning could use longer horizons or different information.
- The protected floor is an explicit evaluation criterion. Nothing in the dynamics determines whose support deserves protection or whether exclusion is legitimate.
- A positive selected equilibrium does not imply safe passage from present conditions. Both production and revision can stop as inherited support vanishes.

Useful next tests are to verify the table and interval independently; perturb initial \(x\) and \(E\); compare the specified copying process with learning from measured delayed returns; and experimentally vary retained output and enforcement expense while measuring public replenishment separately. A reward merely labeled “regenerative” without an observed production debit would not test this mechanism.
