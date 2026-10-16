# Prior art and adversarial review of bounded rule revision

5 October 2026. Independent internal review of the specified model and controller. This is a targeted primary-source comparison, not an exhaustive novelty search or empirical validation. The equations inherit the assumptions and finite strategy repertoire of the constitutional extension.

## Verdict and contribution boundary

The proposed controller is a valid candidate application of established viability and control-barrier methods. Its useful model-specific contribution is to protect the funded production of correction and the incentives of its maintainers while permitting a separately supplied target to change. The maintained incentive gap is part of the controlled state: an adjustment that requests more maintenance can destroy the behavior and revenue needed to deliver it.

This is stronger than observing that a target-only rule sometimes fails. A uniform feasibility proof supplies a sufficient operating region and a rule that preserves it under an explicitly bounded actuator. It does not establish a new general theory of viability, plural objectives, institutional legitimacy, or AI alignment. Whether the state-dependent filter improves on a simple cap or slower rule remains a comparative question.

## Closest primary sources

| Source | Established result relevant here | Implication for the present contribution |
|---|---|---|
| Christophe Béné, Luc Doyen and Daniel Gabay, **“A viability analysis for a bio-economic model,”** *Ecological Economics* 36(3), 385–396 (2001), [DOI](https://doi.org/10.1016/S0921-8009(00)00261-5). The accessible [2000 author working paper](https://www.vliz.be/imisdocs/publications/259103.pdf) identifies the subsequent article. | A resource model includes bounded changes in harvesting effort and simultaneous ecological and economic constraints. It distinguishes current admissibility from continued viability and characterizes viable and crisis regions. | Bounded adjustment, separate constraints, path dependence, and viability without reducing all concerns to one maximized payoff are established ideas. |
| Aaron D. Ames, Xiangru Xu, Jessy W. Grizzle and Paulo Tabuada, **“Control Barrier Function Based Quadratic Programs for Safety Critical Systems,”** *IEEE Transactions on Automatic Control* 62(8), 3861–3876 (2017), [open author paper](https://arxiv.org/abs/1609.06408), [DOI](https://doi.org/10.1109/TAC.2016.2638961). | Control-barrier inequalities restrict inputs to maintain forward invariance; optimization combines these restrictions with performance objectives. The applications explicitly include actuator bounds. | Projecting a nominal command into a feasible interval of barrier-compatible inputs is an elementary instance of this method. The new work must be in the institutional model, its explicit feasible set, and the comparison—not in claiming invention of the filter. |
| Isabelle Alvarez, Laetitia Zaleski, Jean-Pierre Briot and Marta de A. Irving, **“Collective management of environmental commons with multiple usages: A guaranteed viability approach,”** *Ecological Modelling* 475, 110186 (2023; online 24 November 2022), [open published paper](https://perso.lip6.fr/Jean-Pierre.Briot/cv/guaranteed-viability-em-2023.pdf), [DOI](https://doi.org/10.1016/j.ecolmodel.2022.110186). | Stakeholders can supply different acceptable sets and conflicting models. Guaranteed viability seeks common controls that preserve their constraints across the considered models. The construction requires shared state variables, compatible controls and acceptable states, and a trusted assistant; it does not require a consensual dynamical model. | Situated plurality and model disagreement already have substantive viability formulations. The current single-model experiment is less general along these dimensions. Its potential distinction is its explicit incentive and funding feedback, not plurality itself. |
| Keith Paarporn, Ceyhun Eksin, Joshua S. Weitz and Yorai Wardi, **“Optimal control policies for evolutionary dynamics with environmental feedback,”** 2018, [open author paper](https://arxiv.org/abs/1803.06737), [conference DOI](https://doi.org/10.1109/CDC.2018.8619604). | A coupled strategic–environmental system admits controlled incentives and opinions. Optimizing accumulated resource can retain oscillations with exposure to depletion. | Improving an aggregate objective need not protect the full trajectory. That general observation is prior art; the present example isolates a particular failure of maintaining the people and resources that implement the rule. |

These sources support an integration claim. This review has not established that no previous institutional model combines all of the present ingredients.

## Mathematical audit of the proposed certificate

Let the operating state be `(x,h,C,G,m)` and let `u=mdot`, with `|u|≤.5`. Use the unchanged funded plant, `D=hG/(1+G)`, and the declared set

`S={x≥.9, h≥.9, C≥2.5, G≥2.1, m≥.45, b=D−m−.02≥0}`

inside the physical state space. The bounds on `m` and `b` imply `m≤.98`. The candidate projects its nominal rate onto

`L=max(−.5,−2(m−.45)), U=min(.5,Ddot+2b)`.

The feasibility argument checks out. On `S`, `hdot≥0` and `Gdot≥−G`, giving

`Ddot≥−hG/(1+G)^2≥−1/4`.

Also `Dmin=.9×2.1/3.1=.609677419…`. Hence the unclipped upper-minus-lower gap is at least

`−1/4+2(Dmin−.02−.45)=.029354838…>0`.

The unclipped upper bound is at least `−.25` and the lower bound is nonpositive, so their intersection with the actuator interval is nonempty everywhere on `S`. The two scalar barrier inequalities preserve the floor on `m` and the buffer `b`. The original physical lower faces are inward: even the lower-corner verification input at `m=.45` is approximately `2.12390>2.1`. Monotonicity of the relevant plant factors establishes the other faces. This closes the first-exit argument; checking one corner alone would not.

With bounded measurable target input and a nominal rule measurable in time and locally Lipschitz in the state, uniformly on compact finite-time domains, the projected dynamics have the usual unique Carathéodory solution. A merely arbitrary measurable **state feedback** is not enough to claim uniqueness. Finite initial stocks remain bounded by their finite production rates and depreciation. Positive user and maintainer margins throughout `S` imply `x,h→1`, and then `C→3`. This does not imply convergence of `G` under every changing target, or successful tracking of an arbitrary target.

The controller changes a rate, not the state instantaneously. It introduces no new transfer into the operating resource equations. Exact observation, executable rule revision and the computation itself remain unpriced. Preserving the old ledger therefore does not prove that the governance mechanism is itself financed or protected from capture.

## Distinctions that the report must retain

- **Pointwise admissible input:** the current interval is nonempty. This alone says nothing about its future feasibility.
- **Certified controlled invariant subset:** this particular `S` remains intact under the prescribed filter. This is the proved object.
- **Viability kernel:** the largest set from which at least one admissible policy can preserve the declared constraints. The construction does not calculate it.
- **Robust viability:** a guarantee over specified uncertainty, observation error or disturbance sets. The exact-model result does not establish it.
- **Target performance:** a separate trajectory outcome or theorem. A supplied target can be infeasible under the maintained constraints.

Here “protected” describes declared operating conditions. It does not mean that the maintained institution is just, that its goals are legitimate, or that every affected person's concerns are represented. A successful filter preserves these maintenance incentives even when they conflict with its supplied target; that priority is a design commitment, not a value-free conclusion of the equations.

## Discriminating comparison and possible refutations

The written protocol appropriately includes fixed, slow, fixed-cap and equilibrium-rule comparators, gives every arm the same actuator bound, and distinguishes operating-floor breach from certified loss. The grid's fixed arm holds its own initial `m` (including `.45`), so any aggregate label must say “fixed initial rule,” rather than imply all those trajectories use `.5`. A fixed cap that matches the filter's outcome is evidence for a simpler precaution. Such a result does not refute the invariance theorem, but it defeats a claim that this state-dependent controller is necessary or uniformly better.

Concrete mathematical falsifiers are a point in `S` with an empty admissible interval, a permitted input at a boundary pointing outward, or a trajectory starting in `S` that violates a protected condition while all theorem assumptions hold. In the numerical study, resetting `h`, adding unreported funds, instantaneously clamping `m`, or changing the payment equation for one arm would invalidate the resource-matched comparison. Sampling minima does not prove invariance; the analytic result supplies that guarantee.

Outside `S`, an empty interval must be reported as infeasible, not repaired by reversing its endpoints. A nonempty interval outside `S` does not extend the certificate. Failure after observation delay or model error is an applicability limit of the present idealization; it becomes a mathematical counterexample only if robustness to that error was claimed. Goals, constraint legitimacy, peer-reporting incentives, and the observation-to-command authority remain material open modeling questions.

## Narrow statement supported by this work

For this paid correction system, a bounded-rate filter can preserve explicit production, participation and maintenance-incentive conditions throughout a certified region while allowing the nominal rule to respond to changing targets whenever those conditions permit. The construction is a model-specific application of viability and barrier control. Comparative benefit, robustness and empirical relevance require their own evidence.

## Proof and implementation audit

The completed [mathematical note](../model/ANALYSIS.md) states the requisite regularity conditions, distinguishes target compatibility from tracking, and handles the general `L,μG` bound correctly. Its convergence proof uses the inherited assumption `A≤y0`; the scalar useful-capacity argument and the steady-target interval endpoints are consistent. I found no mathematical blocker to the stated conditional theorem.

I inspected the controller implementation and its unchanged-plant comparison. The log-coordinate integration retains the actual replicator update and the physical capacity equations; the filter acts on `mdot` rather than resetting `m`. An independent implementation in physical coordinates, integrated with Radau from `(.9,.9,2.5,2.1,.45)` to time 50 at target 4.7, agrees with the comparison implementation within `5.53×10^−8`. The smallest buffer in that independent trajectory was about `−1.04×10^−12`, consistent with numerical error at an active boundary. This is a useful implementation check, not a substitute for invariance.

In the complete output, the 72 declared starts all preserved the protected conditions and tracked target 4.7 under the filter. The fixed arm and cap `.6` also preserved all conditions but missed that target. Cap `.7` had four mild operating-floor breaches and no operating depletion; the fast rule had 48 depletions, the slow rule 26, and the equilibrium-rule comparator 46. These are outcomes of the specified grid, not estimates of real-world probabilities. The reference target-four case is also solved by slower response, cap `.7`, and the equilibrium rule. Thus the filter is not necessary for that single example.

One instructive adverse result must remain visible: in the original changing-target schedule, a comparator can temporarily reach target 6 while violating the maintenance-incentive buffer, and then recover when the target changes again. Previously accumulated selection can delay the growth of its alternative. A protected-margin breach is consequently neither an immediate-collapse theorem nor evidence that the temporary target was sustainably compatible. An imposed reintroduction of the represented alternative can probe this sensitivity, but it must be labeled exploratory and external, with post-jump certificate membership checked. It does not supply an endogenous mutation or political reform model.

The added exploratory case applies `h←min(h,.99)` to every arm at time 450 and records the pre/post shares and post-jump certificate membership. The filter remains protected; the slow arm enters its established loss box at time 651. The equilibrium-rule arm loses verification and genuine maintenance, but retains approximately `x=.99865,C=2.996` at the final time 750. Its finite-horizon result must not be described as completed depletion of every operating state. Fixed and conservative-cap arms remain useful negative controls. Current saved source and protocol hashes matched the rerun results when audited; the reported alternate-solver maximum discrepancy was below `5×10^−7`. Fee and delivered-maintenance integrals are now reported, while the governance mechanism and the imposed perturbation remain explicitly unpriced.

The post-protocol analytic variants also pass this review. A time-varying positive reserve needs a bounded rate of tightening and its actual almost-everywhere derivative in the rate constraint. The conservative controller replacing observed `h` by a certified initial lower bound uses a valid lower bound on verification growth; it reduces ongoing information requirements but does not prove the initial bound or tolerate arbitrary hidden shocks. Its explicit steady-command restriction correctly distinguishes compatibility of a state with a set from whether this particular conservative filter permits that equilibrium. These are analytic extensions, not additional tested arms in the numerical comparison.
