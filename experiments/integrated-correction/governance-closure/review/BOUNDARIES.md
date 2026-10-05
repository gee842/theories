# Boundaries of funded observation and executable governance

5 October 2026. Independent internal review. This note separates information, payment, implementation and incentive requirements before assessing the proposed governance extension. It is a targeted primary-source comparison and an elementary impossibility argument, not a claim of novel impossibility theory or universal institutional closure.

## The gap that payment alone cannot close

Debiting money for a sensor or governor is necessary for resource accounting, but it does not show that the purchased report is informative, that a command is executed, or that the settlement rule survives manipulation. Giving genuine governors a positive long-run payoff advantage is also insufficient for pathwise safety: a rare remaining dishonest governor can issue an unsafe command before selection removes it.

A positive construction therefore needs explicit attack semantics. Possibilities include bounded measurement and actuation errors; withholding that invokes a proved fallback; or commands accepted only through a specified evidence and settlement interface. Each can support a conditional result. None justifies unrestricted observer or authority corruption unless that threat has itself been modeled. In particular, a post hoc fraud penalty does not undo a constraint violation already caused by an executed command.

## An information obstruction, including randomized policies

Consider the next decision interval before a new informative observation can arrive. A command may be a held scalar input or an entire permitted open-loop input function for that interval. There are two possible worlds, indexed by `i∈{0,1}`, with observation histories `Y` distributed according to `P_i`. Let `A_i` be a measurable **necessary** set of commands for maintaining the declared constraints over that interval in world `i`. Every command outside `A_i` fails the required guarantee there. This formulation concerns actual dynamics, not merely a convenient sufficient barrier certificate.

A causal signal-only policy is a common probability kernel `K(da|Y)`, possibly using private randomization independent of the world. Its induced command law is `Q_i=P_i K`. Suppose

`A_0 ∩ A_1 = ∅`.

**Proposition.** If the observation laws coincide, no such policy can guarantee safety with probability one in both worlds. At least one world has failure probability at least `1/2`. More generally, if `d=TV(P_0,P_1)`, with total variation defined as the supremum over measurable events, at least one world has failure probability at least `(1−d)/2`.

**Proof.** Let `s_i` be the actual safety probability. Necessity gives `s_i≤Q_i(A_i)`. The common kernel cannot increase total variation, so

`Q_0(A_0)+Q_1(A_1) ≤ Q_1(A_0)+d+Q_1(A_1) ≤ 1+d`.

Consequently `min(s_0,s_1)≤(1+d)/2`. When `d=0`, probability-one safety would additionally require the same command law to assign full probability to both disjoint sets, which is impossible. Randomizing commands does not repair missing information. □

For a finite collection of compatible worlds with identical observations, probability-one safety requires a command distribution concentrated on their common necessary safe-action intersection. Pairwise disjoint sets for `n` worlds imply worst-case success at most `1/n`. These statements concern robust safety across the specified possible worlds; they do not say that every particular uncertain system lacks a safe policy.

An elementary witness is `ż=θu−1`, `z(0)=0`, `z≥0`, `u∈[−1,1]`, with unknown `θ∈{−1,+1}`. Before any distinguishing observation, a constant held command must be `+1` in the positive world and `−1` in the negative world. The same observed initial state cannot support both guarantees. A model-based observer cannot manufacture the missing distinction from identical data. Waiting is itself unsafe in this example.

This obstruction can be avoided by a common conservative action, additional timely information, a changed initial buffer, a narrower uncertainty class, or acceptance of explicit risk. It does **not** imply that high-frequency observation is always required: a fixed rule may preserve a conservative region without observing the full state. Nor does disjointness of two sufficient CBF intervals establish impossibility for the underlying control problem; those intervals can be conservative.

## A budget–latency compatibility condition

Suppose a chosen observation-dependent certificate requires no more than `Δ` time between usable observations. Let each observation cost `c_s>0`, executed rule variation cost `c_a≥0` per unit, initial spendable reserve be `B_0`, and available governance revenue be `γF(t)`. With no external subsidy or borrowing, accounting requires

`c_s N(T)+c_a TV(m;[0,T]) ≤ B_0 + ∫_0^T γF(t)dt`,

where `N(T)` counts paid observations and `TV` denotes total variation. The maximum-gap condition implies `N(T)≥T/Δ−1`, up to the initialization convention. Therefore a necessary asymptotic financing condition for this certificate is

`liminf_{T→∞} [T^−1∫_0^T γF(t)dt − c_a TV(m;[0,T])/T] ≥ c_s/Δ`.

This is a necessary accounting condition, not a sufficient scheduling, information or safety theorem. A reserve can finance temporary deficits; it cannot finance a permanent average deficit. Fraudulent payments are additional costs unless already included in the counted allocations. Certificate-specific sampling requirements must not be mistaken for a universal minimum observation rate, and computing a sampling period must not assume away execution delay or stale reports.

## Closest primary precedents

| Primary source | Verified result and relevant limit |
|---|---|
| Robert M. Townsend, **“Optimal Contracts and Competitive Markets with Costly State Verification,”** *Journal of Economic Theory* 21(2), 265–293 (1979), [open published paper](https://economics.mit.edu/research/publications/optimal-contracts-and-competitive-markets-costly-state-verification), [DOI](https://doi.org/10.1016/0022-0531(79)90031-0). | Verification consumes resources and affects implementable contingent contracts. In the model, purchased verification makes the state known without error, and contract execution follows stated allocation rules. Thus costly monitoring is established theory, while error-free verification and execution remain primitives rather than results of paying auditors. |
| Xi Alice Gao, James R. Wright and Kevin Leyton-Brown, **“Incentivizing evaluation with peer prediction and limited access to ground truth,”** *Artificial Intelligence* 275, 618–638 (2019), [author repository](https://uwspace.uwaterloo.ca/items/19ea8bc1-f265-48d7-8ce4-8591b86a928a), [authors’ IJCAI 2020 journal-track summary](https://www.ijcai.org/proceedings/2020/0723.pdf). | Their universal report-only mechanism class cannot guarantee a Pareto-dominant truthful equilibrium across the considered multiple-signal environments when useful information costs more than a cheap coordinated signal. This is not impossibility of every truthful peer mechanism. Their spot-checking alternative uses a trusted, possibly noisy signal; invoking it does not explain how that trusted signal is produced. |
| Andrew Singletary, Yuxiao Chen and Aaron D. Ames, **“Control Barrier Functions for Sampled-Data Systems with Input Delays,”** 2020, [open author paper](https://arxiv.org/abs/2005.06418). | The paper treats held commands, state uncertainty and known input delays, requiring protection over the entire interval between updates. Sampling an ideal continuous controller does not automatically preserve its guarantee. Its backup-control and reachability conditions remain explicit hypotheses. |
| Pradeep Sharma Oruganti, Parinaz Naghizadeh and Qadeer Ahmed, **“Robust Control Barrier Functions for Sampled-Data Systems,”** 2023 preprint, [open paper](https://arxiv.org/abs/2309.08050). | Measurement error and disturbances are bounded by declared compact uncertainty sets; robust margins also cover intersample state movement. Such bounds specify the guarantee’s threat class. They are not established merely because a sensing institution is paid. |
| Laura Doval and Vasiliki Skreta, **“Mechanism Design With Limited Commitment,”** *Econometrica* 90(4), 1463–1500 (2022), [open published version](https://discovery.ucl.ac.uk/id/eprint/10154019/), [DOI](https://doi.org/10.3982/ECTA16846). | The designer can commit only to short-term mechanisms, and acquired information shapes subsequent mechanism choices. Limited commitment therefore changes the mechanism-design problem; it cannot be represented simply by retaining a fixed settlement rule while calling the authority endogenous. The paper does not eliminate all commitment or cover arbitrary captured authorities. |

These are close constraints and construction methods, not an exhaustive novelty comparison. The elementary proposition above applies the standard inability of a common decision rule to distinguish identical observations; its proof is supplied to make the exact quantifiers visible.

## Acceptance criteria for the funded extension

1. **Resource diversion is real.** Governance spending is deducted from the same production stream, changes the remaining useful and verification inputs, and pays sensor operation, replacement, execution and any stated wages. Initial capacity and working capital are declared. Integrating a positive stock without charging its production is not funding.
2. **Signals carry justified information.** State exactly what a delivered report certifies, its error and delay bounds, and which manipulation breaks the bound. Consensus among reports is not by itself evidence of task-relevant truth. Reusing the existing paid verification stock avoids a new institutional level only for measurements it can actually test.
3. **Authority has an executable interface.** Separate the requested rate, authorized command and realized rate. Include bounded saturation and the effects of withheld, forged or stale commands. A physical limiter or settlement interface can be an explicit primitive; its correctness must not be described as an endogenous payoff result.
4. **Safety covers behavior before convergence.** Expected or mean-field selection against corruption does not establish safety against individual arbitrary attacks. State whether the result protects a deterministic aggregate, a bounded disturbance class, a high-probability stochastic process, or every allowed attack path.
5. **Fallback has its own proof.** Freezing the current rule can be safe in some regions and unsafe in others. No-resource or no-command behavior must be specified, and any claimed fallback region must remain viable under that behavior.
6. **Payment discipline has a declared endpoint.** Identify who authenticates delivery, holds or releases payments, prevents double spending, applies the command, and cannot be replaced within the finite threat model. Pricing the work of these operations does not prove that their prescribed mapping is physically unavoidable.
7. **Failure comparisons remove the relevant mechanism.** Withhold funding, allow cheaper false reports, remove enforceable withholding, reduce actuation, or enlarge observation ambiguity one at a time. Distinguish theorem failure, controller infeasibility, lost tracking and actual operating failure.

The useful target is a finite closure result: within a declared class of dishonest service provision and bounded observation/execution failure, production funds the means of obtaining and acting on sufficiently informative feedback, and the resulting closed dynamics preserve specified operating conditions. The construction need not explain all legitimacy or all physical law. It must state where its explanations stop.

## Audit of the proposed majority-based architecture

The candidate assigns a governance share `W=.02F` from existing fees, reduces the two prior operating allocations accordingly, and maintains a paid joint capacity `J`. A delivery share `z` actually maintains the contracted package; shirkers divert resources. Existing funded verification supplies the detection term `D`, with an increased workload parameter. The proposed payoff difference between maintenance and shirking is `W(D−d)` for expenditure fraction `d=.3`, and `Jdot=2500 d zW−J`. This can explain persistence of actual provision under the stated financial selection process. It does not explain why a truthful majority exists initially or survives actors with unrestricted control over membership and settlement.

The aggregation step has a simple exact lemma. If more than half of authenticated weight reports numbers in `[v−ε,v+ε]`, every weighted median lies in that interval regardless of minority values. If more than half proposes the **same** executable command, every weighted median command equals that command. No convergence of the minority to truth is required for these two statements. They require a common authenticated weight assignment and a shared aggregation result. They are not a protocol for establishing distributed consensus when those premises themselves are attacked.

A maintained `J` can support a stipulated bounded-error instrument and a rate-limited actuator without a new free observer. Nevertheless the inference has distinct premises: calibrated physical instrumentation supplies the error bound; paid procurement maintains that instrumentation; the majority lemma tolerates the specified reporting attacks; a robust controller handles residual error; and the specified command interface executes the aggregate. The construction must keep these separate. Charging their maintenance does not derive the correctness of the interface or the physical calibration law.

The first candidate bundled spending, accurate reporting and compliant commands in one practice. This review identified a hybrid that maintains capacity but lies or issues another command; it can have the same monetary return as truthful provision if auditing tests only completion. The agreed repair includes three practices: truthful maintainers `a`, lying maintainers `b`, and shirkers `c=1−a−b`. The first two earn `(1−d)W`, while shirkers earn `(1−D)W`; lying maintainers and shirkers may submit arbitrary reports and commands. Set `z=a+b` and `θ=a/z`.

Under the common replicator update, direct differentiation gives

`zdot=ν_z z(1−z)W(D−d), θdot=0`.

Thus if the operating proof maintains `z≥z_min` and `θ(0)z_min>1/2`, truthful command weight stays above one half. The proposed `θ(0)=.9,z_min=.9` gives at least `.81` truthful weight, while allowing persistent arbitrary minority corruption. This repair needs no fabricated semantic-truth audit. It instead admits that truthfulness is neutral between the two maintaining practices: initial composition is preserved by these particular dynamics, not selected into existence. Mutation, strategy drift, bribery, unequal additional payoffs and capture of authenticated weights can invalidate that premise. The original operational-verification model also retains its own finite repertoire and physical verification assumptions.

The paid package should include the recurring resources used for sensing, aggregation, computation, communication and actuation maintenance, or identify which of those remain unpriced. Non-Sybil membership, certified identities/weights, the nonbypassable command channel, verifiable delivery and conditional settlement remain a physical and procedural boundary even when all their operating costs are charged.

## Completed equation audit

The revised [mathematical construction](../model/ANALYSIS.md) includes the three governance practices, charges the joint service package, and distinguishes neutral truthfulness from selected maintenance. The core conditional proof passes this review. Independently recalculated lower-face margins match the note: user advantage `.0298469388`, useful-capacity renewal `.0696551724`, verification renewal `.1201820690`, maintenance-over-shirking advantage divided by `W` of `.290625`, and governance renewal `1.5663775510`.

The robust command is computed from purchased `G,m` observations plus invariant lower bounds, without reading hidden `h` or `z`. The signs of `f_G` and `f_m` justify the chosen conservative measurement endpoints over the whole stated domain. Their worst-case errors leave a raw interval gap of at least `.10356640625`; the actual actuator supports every selected command while `J≥1`. These bounds close the joint first-exit argument, rather than assuming that paid observation stays available independently of participation and funding. The limiting stocks `C_R=2.9290487362` and `J_R=3.2503474496` also match independent scalar calculations.

Removing withholding yields `zdot=−ν_Z dWz(1−z)`. For `z(0)<1`, the logarithmic identity bounds `∫zW`; the linear `J` equation consequently gives `J→0` and finite `∫J`. Since executable speed is at most `J`, the total remaining variation of `m` is finite and its setting approaches a limit. This is a correct loss-of-governance theorem. It does not imply that all production collapses, that the frozen setting is unsafe, or that the truthful fraction itself must tend to zero when fee revenue disappears.

Two feasibility calculations expose real tradeoffs. The chosen corner needs `γ≥.0077930856` to renew governance but `γ≤.0465646806` to preserve the useful-capacity floor. These are individual necessary funding inequalities for this certificate, not a complete viability interval. The error-free sufficient filter already refuses exact target 4 at its corresponding full-operation steady state: its upper-command margin is about `−.0197705`. These adverse bounds should remain visible in the synthesis.

## Implementation audit

The implementation's honest controller receives only the aggregated `G,m` pair, target and declared parameters. It does not read actual `h,z,J,x,C`. The physical simulation uses `J` to generate instrument error and to limit realized actuation, as the modeled technology requires; this is distinct from supplying `J` to the controller. The conservative measurement box, lower funding bound and derivative formula match the proof. Coordinatewise medians need not come from one underlying sensor, which the full componentwise error box correctly accommodates.

Truthful mass is `θz`, including the neutral lying maintainers among arbitrary message providers. The capture intervention changes only `θ` at the declared time, preserving `z,J` and all contemporaneous resource flows. Command aggregation occurs before the actual `J/(1+J)` rate saturation. Outside the certificate, an empty interval is recorded and produces a zero proposal; this freezes the rule through the specified interface and must not be described as a certified safe return.

A manually recomputed physical-coordinate plant, sensor-median reduction and robust command from the lowest certified corner to time 40 at target 3.8 agrees with the production log-coordinate implementation within `3.37×10^−7`. Every independently sampled protected margin was nonnegative. This check covers the altered budgets, actual actuation limit and purchased observation errors. It does not prove robustness to an omitted physical disturbance or discrete-delay model.

The final [saved output](../results/analysis.json) matches the current source, baseline and protocol hashes. The renamed `all_protected_state_bounds_preserved` field correctly concerns states alone: an observation or actuator outage can preserve those bounds while violating the interface premises. It is not mislabeled as complete satisfaction of the theorem's assumptions. The alternate-solver discrepancies are below `8.1×10^−6`; the maximum flow-ledger residual is approximately `8.33×10^−17`.

The outcomes support the bounded interpretation. Funded governance preserves the declared state conditions and tracks target 3.8 with late error below `.0008` in the tested case. Its high request of 4.7 remains unmet, settling near 3.945 during that phase. The selected truth-capture and command-bypass attacks deplete verification and subsequently revenue; removing withholding loses funded governance and also produces operating depletion for the chosen attack. Only the capability-loss claim is general in the no-withholding theorem.

Adverse controls are preserved. Outages freeze a rule that remains viable in the tested trajectories, while missing later requests. Low governance allocations `.002,.005` lose the declared `J` floor without destroying operation; higher allocations `.05,.08` breach declared floors temporarily but reach positive operating states. Starts with `z=.6,.8` can recover despite lying outside the sufficient region. These observations reject interpreting the certificate's boundary as the exact viability boundary, or interpreting every governance disruption as inevitable collapse. No remaining proof, accounting or implementation blocker was found for the final stated conditional result.
