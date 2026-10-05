# Systems dynamics, situated goals and the limits of the current construction

5 October 2026. Internal AI research review. This note distinguishes the broader research programme from what the paid-correction construction currently establishes. The literature comparison is targeted, not a systematic novelty audit. It does not rank this programme as the best theory or infer a general solution to alignment.

## The strongest defensible framing

The broad object is a coupled system in which behavior changes material and institutional conditions, those conditions change what behavior is rewarded or possible, and the processes producing evaluations and preferences may themselves change. A common global objective is unnecessary. Some components can use explicit optimization while their joint dynamics fail to optimize any shared quantity.

This has an established mathematical home in evolutionary games with environmental feedback, adaptive dynamical systems and endogenous institutional change. The project's potentially useful emphasis is more specific: identify the resources and practices that reproduce a system's capacity for informed revision, and ask whether the selection processes using that capacity also maintain it. Its scientific value must come from distinctions and predictions this accounting adds, not from renaming all feedback as backpropagation.

The current four-state construction is a worked module in this broader programme. It couples two practice populations to two paid capacities. It does not yet model an ecology of institutions, changing ends, open-ended model discovery, or normative disagreement. Both populations currently respond to specified private resource returns, and the service's task interpretation remains fixed.

## Dynamical distinctions that should survive the synthesis

| Concept | Meaning and implication here |
|---|---|
| Attractor | An invariant set attracting nearby states. It can be a point, a cycle or a more complicated set; it need not be socially desirable. |
| Basin | States approaching a particular attracting set under fixed rules. Different outcomes at identical parameters can result from different starting states. |
| Basin crossing | An intervention or perturbation moves the state across an existing basin boundary. This need not change the attractors themselves. |
| Bifurcation | A parameter change alters the qualitative dynamical structure. A zero invasion eigenvalue is a candidate location; classification needs the local branches or other appropriate analysis. |
| Noise-induced tipping | Stochastic disturbances cause escape or transition. It requires a noise or finite-population model, absent from the deterministic construction. |
| Rate-induced tipping | The speed of changing conditions causes failure to track a regime, potentially without a frozen-parameter bifurcation. A static parameter sweep cannot demonstrate it. |
| Positive feedback | A reinforcing loop. It can saturate, support bistability, accelerate depletion, or interact with other loops; it does not imply infinite growth. |
| Unbounded runaway | A state grows without bound, or blows up in finite time, in the declared model. This is not what the four operating equations do. |

The distinction among bifurcation-, noise- and rate-dependent tipping is developed explicitly by [Ashwin, Wieczorek, Vitolo and Cox, *Tipping points in open systems*](https://arxiv.org/abs/1103.0169), published in Philosophical Transactions A 370, 1166–1184 (2012). Their examples show why rapid change can matter without a loss of stability in the corresponding frozen system. The current model would need a time-dependent intervention to test that possibility.

“Phase transition” can be used informally for a qualitative regime change if the underlying event is named. It should not imply that a finite-dimensional differential equation has established a thermodynamic phase transition, a universality class, critical exponents or universal early-warning indicators.

The current equations satisfy

\[
\dot C\le\eta_C\lambda\tau(y_0+A)-\mu_C C,
\qquad
\dot G\le\eta_Gm(1-\lambda)\tau(y_0+A)-\mu_GG.
\]

With x,h in [0,1], all four operating states are bounded. The correct language is reinforcing recovery or reinforcing loss, not unbounded runaway. The inert reserve can accumulate, but it has no feedback and does not generate an operating runaway.

The depleted states form a family, x=C=G=0 with arbitrary residual h. Different failures can leave different latent practice shares. Likewise, adding the inert reserve creates an additional neutral coordinate. A unique attracting point in all five coordinates has not been established.

## Why local adaptation need not be a global gradient

There is a simple counterexample independent of the institutional model. Consider two interacting strategy shares:

\[
\dot u=u(1-u)(2v-1),\qquad
\dot v=-v(1-v)(2u-1).
\]

Each is a payoff-driven replicator response in a zero-sum interaction. Yet

\[
H(u,v)=\log[u(1-u)v(1-v)]
\]

is conserved in the interior: substitution gives \(\dot H=0\). Away from the central equilibrium, its compact regular level curves are periodic orbits. No single-valued scalar can strictly increase along each entire nonstationary orbit and return to its initial value. Thus local payoff improvement mechanisms do not entail ascent of a shared objective.

This example is a direct mathematical illustration, not a claim about the current four-state model. More generally, [Mertikopoulos, Papadimitriou and Piliouras, *Cycles in adversarial regularized learning*](https://epubs.siam.org/doi/abs/10.1137/1.9781611975031.172), SODA 2018, 2703–2717, prove recurrent behavior for a class of coupled regularized learning dynamics in zero-sum games. An [open author version](https://arxiv.org/abs/1709.02738) is available. Optimization by individual learners is compatible with cycling by the joint system.

If a future version claims a common gradient, it must identify the scalar, the geometry or metric, and the domain over which the gradient representation holds. Drawing arrows on a feedback diagram does not supply those objects. Conversely, the absence of a global scalar does not prevent useful local interventions or partial predictions.

## Attractiveness, desirability and revisability are different properties

A dynamically stable institution can maintain a harmful task. An institution can also satisfy a locally chosen welfare criterion while being unable to fund itself or resist an admitted replacement practice. A third question is whether it preserves the ability to revise its task, representation and rules when those become inadequate. These three assessments should be recorded separately.

For a situated, plural framework, distinguish at least:

1. **Behavioral explanation:** what each agent perceives, values, learns and can do under the current conditions.
2. **Material feasibility:** whether resources, maintenance and ecological support can sustain the proposed activities.
3. **Normative evaluation:** whose interests, rights, harms and disagreements are represented, and who has standing to contest a proposed improvement.

A vector of outcomes can preserve disagreement that a single weighted sum hides. It does not resolve disagreement automatically: the dimensions, admissible constraints and weights remain choices. A Pareto comparison can establish agreement on some changes while leaving others incomparable. Procedural rights and prohibitions may be modeled as constraints rather than exchangeable terms in a score. These are proposed modeling choices, not consequences of the current resource equations.

Endogenous preferences require particular care. A system may change what people endorse as well as change their circumstances. Satisfaction measured only against the resulting preferences cannot by itself distinguish improved opportunities from adaptation to deprivation. An explanatory law for preference change therefore should not silently become the criterion for approving that change.

[Bowles, *Endogenous Preferences: The Cultural Consequences of Markets and Other Economic Institutions*](https://sites.santafe.edu/~bowles/1998JEL.pdf), Journal of Economic Literature 36, 75–111 (1998), directly examines how institutions shape preferences and why this complicates policy evaluation. [Bisin and Verdier, *The Economics of Cultural Transmission and the Dynamics of Preferences*](https://www.sciencedirect.com/science/article/pii/S0022053100926784), Journal of Economic Theory 97, 298–319 (2001), supplies an explicit intergenerational transmission model with conditions for persistent preference heterogeneity. Its mechanism is cultural socialization, not interchangeable with payoff imitation. These precedents support modeling preferences as endogenous; neither licenses treating whatever preferences survive as normatively correct.

## Across levels does not mean identical mechanisms

A multilevel model needs to specify the carriers at each level, the outcomes affecting their persistence, transmission between generations or periods, migration or exchange across groups, and the effects each level has on the others. Two role populations interacting within one institution are not automatically multilevel selection. An institution competing against other institutions needs an additional survival, reproduction or adoption mechanism.

[Traulsen and Nowak, *Evolution of cooperation by multilevel selection*](https://www.pnas.org/doi/10.1073/pnas.0602530103), PNAS 103, 10952–10955 (2006), gives a concrete example: individuals reproduce within groups, groups grow and split, and population structure creates between-group effects. Its derived condition is specific to that model. It does not show that all competition favors cooperation, or that biological and political units share identical equations.

The same caution applies to cancer, markets, organizations and AI training. A common feedback pattern can guide comparison, but a transfer claim needs explicit correspondence between states, selection mechanisms, constraints and observations. Similar diagram shapes do not establish identical attractors or empirical predictions.

“Meta-attractor” can be made precise in several different ways. One option is a joint attractor of operating states z and slowly changing rules θ, with \(\dot z=F(z,\theta)\) and \(\dot\theta=\epsilon G(z,\theta)\). Another is a family of regimes under external change, requiring a nonautonomous analysis. Neither follows just from locating two basins in a fixed-rule model. Until an option is chosen, the term should identify a research question rather than an established object.

## Commons failures are conditional, not inevitable optimization results

A commons failure describes a specified mismatch between individually rewarded actions and collective outcomes. It can involve externalities, incomplete information, incentives, power, coordination or bounded adjustment. It does not require a world that globally optimizes anything, nor show that every local optimizing process causes collapse.

[Ostrom, *Beyond Markets and States: Polycentric Governance of Complex Economic Systems*](https://www.aeaweb.org/articles?id=10.1257/aer.100.3.641), American Economic Review 100, 641–672 (2010), synthesizes empirical and experimental research on diverse arrangements and motivates institutions fitted to particular settings. Its [open primary text](https://web.pdx.edu/~nwallace/EHP/OstromPolyGov.pdf) also distinguishes common-pool, public, private and toll goods. This is a reason to specify the resource and institutional setting, not infer either inevitable tragedy or guaranteed success from decentralization.

The present correction model primarily concerns financing and maintenance of a service with controlled access. It contains no depleting host-resource stock. It should not be redescribed as an already completed model of ecological overharvesting merely because both can contain reinforcing failure.

## Closest systems precedents and the contribution boundary

[Weitz, Eksin, Paarporn, Brown and Ratcliff, *An oscillating tragedy of the commons in replicator dynamics with game-environment feedback*](https://pmc.ncbi.nlm.nih.gov/articles/PMC5127343/), PNAS 113, E7518–E7525 (2016), couples evolving strategies and environment-dependent incentives. The key comparison is that behavior changes the conditions governing subsequent behavioral selection; oscillation is possible instead of convergence to a shared optimum.

[Tilman, Plotkin and Akçay, *Evolutionary games with environmental feedbacks*](https://www.nature.com/articles/s41467-020-14531-6), Nature Communications 11, 915 (14 February 2020), develops a broad framework with renewing and decaying environments. Its analysis already distinguishes equilibria, bistability and cycles and shows how relative timescales matter. The [open primary PDF](https://www.zoology.ubc.ca/let/pdfs/Tilman%20et%20al%202020.pdf) was inspected. The general feedback architecture is therefore prior art; this project needs a more specific contribution than its rediscovery.

[Itao and Kaneko, *Self-organized institutions in evolutionary dynamical-systems games*](https://doi.org/10.1073/pnas.2500960122), PNAS 122(15), e2500960122 (11 April 2025), is especially close to the situated extension. Its [open author version](https://arxiv.org/html/2501.07249v2) evolves decision functions responding to environmental and player states and studies emergent institutional modes. It distinguishes evolutionary robustness from the performance of a mode in a homogeneous population. The model is limited and its broader claims require their own audit, but contextual decision rules, emergent norms and institutional attractors are clearly not untouched territory.

The current defensible contribution is a transparent, budgeted correction-and-maintenance module with specified selection threats and proved conditional failure/recovery. A stronger programme would need to show why explicitly representing the reproduction of correction changes a prediction, diagnosis or intervention relative to these neighboring models. Relevant comparisons include equal-output states with different renewal capacity, interventions that improve present performance while damaging later revisability, and plural constraints that prevent a technically sustainable institution from qualifying as acceptable.

## A checked restriction on the fixed-rule model

The mathematical lead identified a stronger property of the existing four-state equations. In their strict interior, change time by dθ/dt=xr(C)>0 and write β(C)=Aq(C)/r(C). The equations become

\[
\begin{aligned}
x_\theta&=\kappa(1-x)[\beta(C)D-\tau],\\
C_\theta&=\eta_C\lambda\tau-\mu_C C/[xr(C)],\\
G_\theta&=\eta_Gm(1-\lambda)\tau h-\mu_G G/[xr(C)],\\
h_\theta&=\nu(1-\lambda)\tau h(1-h)(D-m).
\end{aligned}
\]

I independently checked that all off-diagonal derivatives are nonnegative and the coupling graph is irreducible in this interior. Apparent negative cross-effects in the original h equation partly arose from a state-dependent common speed of replacement. Removing that speed reveals a strongly cooperative system; this is a mathematical order property, not a claim of social cooperation.

Consequently a nonconstant interior periodic orbit cannot be attracting. Its positive variational monodromy has a principal positive eigenvector. The orbit's tangent is an eigenvector with multiplier one, but cannot be one-signed around a closed nonconstant path. The principal multiplier must therefore exceed one. The positive time change preserves orbital stability near any such compact interior orbit. This agrees with [Hirsch, *Systems of Differential Equations that are Competitive or Cooperative II: Convergence Almost Everywhere*](https://escholarship.org/content/qt67z7c17v/qt67z7c17v.pdf), SIAM Journal on Mathematical Analysis 16(3), 423–439 (May 1985).

This excludes attracting interior cycles in this model, not cycles in the wider programme. It also does not prove that every trajectory converges: the rescaled time can have a finite endpoint during depletion, and boundary invariant sets require their own analysis. A full global classification should not be inferred from the title of the cited theorem.

## Auditing the proposed adaptive-rule bridge

The added rule

\[
\dot m=\epsilon m(1-m)(G_{\rm target}-G)
\]

turns one contract parameter into a state. It represents a specified controller: when checking capacity is below target, require more work from genuine contractors. The same increase also lowers their retained compensation. Thus the controller can improve one immediate production input while damaging the incentives that produce it.

With the canonical conversion parameters and target G_target=4, the clean stationary operating state is x=h=1, C=3, G=4, m=2/3. The G,m block has characteristic polynomial

\[
z^2+z+6\epsilon m_*(1-m_*).
\]

It is stable for every ε>0, while at ε=0 the unchanged m coordinate is neutral. The other operating eigenvalues are negative at this state. Therefore different outcomes at different positive response speeds do not by themselves demonstrate a Hopf bifurcation. A trajectory can leave the attraction basin of a destination that remains locally stable.

This extension is still a fixed-target controller with accurately observed G and implementable rule changes. The target, observation mechanism, political authority and cost of changing m are not explained. In particular, continued m adjustment after fees disappear is an idealized governance capability. It should not be presented as endogenous formation of goals or complete resource closure of governance itself.

The contrast between ε=.1 recovery and ε=1 failure at target 4 is supported by the reviewed implementation and its recorded numerical trajectories. The target-3.6 comparison recovering at ε=10 is an appropriate control against the stronger claim that fast adaptation is invariably harmful. “Rate-sensitive outcome under coupled feedback” is defensible; a standard externally forced rate-tipping theorem has not been established.

One failure certificate does transfer exactly. The existing low-service region x≤.15,C≤.4 remains invariant for arbitrary m(t) in [0,1], because its x and C bounds do not use m. Entry gives x,C→0 and hence G→0. For this positive-target controller, logit(m)'=ε(G_target−G) then implies m→1. Successful adaptive recovery needs its own invariant neighborhood or should remain numerical convergence toward a separately proved locally stable state; the fixed-m recovery box cannot be silently reused.

## Acceptance criteria for the new figures and framework

A basin chart should state all fixed parameters, the two plotted initial coordinates, held-fixed capacities, time horizon and classification rule. Certified entry into a proved region should be distinguished from a finite-horizon guess. Unclassified slow trajectories should remain unclassified, and the figure should not imply its two-dimensional slice is the entire four-dimensional basin. Numerical grids do not prove a boundary is smooth or exclude unseen cycles.

A parameter diagram should distinguish the existence of a regime, its local invasion stability and the outcome from a chosen initial condition. The canonical fully maintained regime has C*=3 and G*=6m when only m changes; the strict stability interval supplied by the mathematical lead is 29/186<m<5/6. Endpoints must not be turned into a claim of global failure without branch and basin analysis. The term bifurcation should be supported by that analysis.

A plural framework should state which additions are mathematical definitions, which are proposed dynamics, and which have already been analyzed. Adding a vector of interests or a changing representation variable is not yet a theorem of plural coordination. The model must expose the effect of those additions on decisions and on the judgment of success. The strongest presentation retains the established four-state module while openly identifying the broader situated programme as work still to be done.

## Completed numerical and framework review

I reviewed `analyze_system.py`, its saved analysis, the protocol, the rendered four-panel atlas and `review/MULTILEVEL.md`. The basin plot holds C=G=3 and m=.5 and correctly separates initial-state dependence from the local parameter-stability plot. Its 51×51 grid records 2,380 entries into proved loss regions and 221 entries into the proved recovery region, with none unresolved at the specified horizon. Halving the step leaves all classifications unchanged; 32 adaptive-solver spot checks agree. These are approximate numerical entries into analytical regions, not interval-certified trajectory enclosures or a theorem about all initial states.

The adaptive-rule implementation matches the declared five equations and the local eigenvalue factorization. I also integrated an independently written physical-coordinate version to time 30 for the failing ε=1 controller; it agrees with the implementation's logarithmic-coordinate trajectory within 1.2×10⁻¹¹ across the five states. Both current source hashes match the saved record.

The implemented adaptive loss certificate uses h≤.1, m≥.9, C≤108/29 and G≤1 with x<1. It is valid for target 4. At the G upper face, input is at most 21.6/29<1; the C upper face is nonoutward, h decreases and m increases. Throughout that region the payer advantage is at most .04−.15<0. Thus the recorded entry at sampled time 21.6 supplies an analytic future-loss argument, conditional on the numerical entry.

The proposed plural diagnostic in MULTILEVEL correctly preserves separate conditions on immediate stock maintenance and custodian returns. Its feasible interval need not exist, and a choice mechanism is still necessary when it does. Brief violation of that interval does not itself prove eventual failure: the lower-target, high-speed controller recovers after some such violations. The memo correctly distinguishes this instantaneous diagnostic from a global control guarantee.

No blocking implementation or framing issue remains in the reviewed atlas and framework. The unproved parts are still substantial: successful adaptive recovery from the selected starting point remains numerical convergence toward a locally stable equilibrium; the general plural state schema has no completed update-law theorem; and the finite practice repertoire, financial execution and observation primitives remain explicit restrictions.
