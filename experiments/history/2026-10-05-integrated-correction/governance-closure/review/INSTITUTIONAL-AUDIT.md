# Institutional audit: paying for observation and executable revision

5 October 2026. Internal AI mechanism, accounting and research-design audit. This memo records initial requirements, review of the completed mathematical construction, and independent checks of the implementation and its reported numerical results. It is not external peer review or empirical validation.

## The gap being addressed

The viability controller currently receives the actual state, computes a derivative from an exact model, and changes the work requirement through a functioning actuator. None of those capabilities is paid from the operating revenue, and the rule can keep updating after operating revenue has disappeared.

A new state named governance is not enough to close that gap. A substantive extension should identify the observations actually produced, the authority actually executable, their resource cost, their degradation, and the alternatives that can replace genuine provision. A theorem must then survive the cost subtraction and the admitted failures.

There are two different questions:

1. Can the system finance and retain a specified observation-and-revision service?
2. Can that service determine, revise or legitimately enforce every purpose and rule supporting its own existence?

The first can be addressed in a bounded model. It does not establish the second by implication.

## Resource accounting requirements

Observation and actuation must consume money, labor or functional resources already present in the balance. If a fraction of collected revenue F funds governance, that fraction is unavailable for the previous useful and verification capacities. Their old inward inequalities and reference equilibrium must be re-derived; a ledger that charges governance but still gives C and G the full old budget is invalid.

A useful general ledger splits F into θ_C F, θ_G F and θ_J F with nonnegative fractions summing to one. The first funds useful capacity. The second funds verification contracts. The third purchases observation and executable control, represented by a genuine functional package J. If governance contractors can file false completion claims, partition their budget into actually delivered work, legitimate compensation, undetected diversion and withheld amounts. These flows must sum to θ_J F. Withheld money must not also appear as produced capacity unless an explicit second allocation spends it.

Existing verification can inspect governance contracts, but its workload increases. The same G does not provide an unlimited number of free checks merely because another layer has been named. Either its conversion cost and half-saturation parameter must include all declared workloads, or checks must compete for a finite inspection budget.

A governance contractor's legitimate return and fraudulent return should be derived from these actual payments. An extra reward for being a good governor would supply the desired selection result by assumption. If the same people hold several roles, all relevant income and authority consequences must enter their decisions; separate-population models should state that separation.

## What is observed, and when it is identifiable

The honest-maintenance fraction h is a modeled operating practice, not a number every controller can read directly. One possible interface is to purchase challenge audits that estimate effective verification D, together with a measurement of G. In the current model D=h p(G), so h=D/p(G) when p(G)>0.

This reconstruction has a meaningful limit. When G is small, uncertainty in D is amplified by 1/p(G). At G=0, D=0 for every h, so these observations cannot identify h at all. Paying a generic sensor stock does not remove that ambiguity. A protected region with a verified lower bound on G can bound the conditioning, but that lower bound itself belongs in the maintained certificate.

The error model must be stated honestly:

- A finite sample of random audits ordinarily supplies a probability statement, not an infallible point estimate. A guarantee needs a declared horizon and confidence treatment, or a suitable bound on the cumulative probability of a bad certificate.
- A deterministic bounded-error instrument is a possible model primitive, but its observable quantity, calibration, error envelope and admissible attacks must be explicit. It should not be described as something automatically implied by finite audit expenditure.
- Between observations, a command uses aging information. Sampling and transmission delay require bounds on the unobserved evolution, not merely accurate values at the previous sample.
- A model-derived Ddot requires either an admissible dynamic model or a conservative derivative bound. Paying for a measurement does not by itself establish the exact dynamics used in a safety proof.

One can propagate an interval or set of possible states and require a common feasible action for all of them. If their safe-action sets have an empty intersection, more calculation does not solve the missing-information problem. The implementation should report loss of certification or enter a physically justified fallback.

## Nondelivery differs from fabricated state evidence

A dishonest contractor that claims work but builds no functioning instrument is one threat. A contractor that supplies plausible but fabricated state measurements is another. The latter can defeat a controller even while its expenditure accounts and sensor-capacity stock appear satisfactory.

If fraudulent measurements can be admitted with positive probability, a deterministic all-time invariance claim needs an additional corruption bound or must become probabilistic. Renaming a perfectly accurate observer as a paid observer does not resolve this issue.

A bounded alternative is to let false completion reduce actual J while an explicitly trusted measurement interface authenticates real readings within a declared error envelope. That can support a conditional result, but forged accepted observations and capture of the interface remain outside its threat class. The physical anchor is the instrument's relation to the measured process, not the fact that someone signed a report.

## Executable authority and the fallback test

Changing a command in software is not necessarily changing an enforceable contract. The model must identify which actuator changes m, its rate and operating range, the capacity that powers it, and what happens when that capacity fails. Detection without execution is already a known failure mode in this programme.

A fallback such as “set m=.5 when governance is unavailable” is not automatically passive. It can require recognizing the failure, overriding the current rule, obtaining permission, and doing the work of reversal. An instantaneous reset also supplies more actuator authority than the previously limited |mdot|≤.5.

A genuinely precommitted fallback can be modeled, for example, as a default contract that permits a temporary deviation only while a valid paid lease remains active. Lease expiry returns subsequent transactions to the default. Alternatively, an actual mechanical or logical relaxation mechanism can return a setting using stored capacity. Either interpretation must state its timing, wear, physical execution and attack boundary. If stored energy or replacement resources are used, they belong in the budget. A clock or release mechanism that remains reliable after all operational funding is gone is an explicit residual primitive.

Freezing the last rule on loss of control is a different fallback. It avoids assuming an active reset, but a last rule outside a robust operating range can be dangerous. The model should not use the safety properties of one fallback while implementing the other.

## Conditions that would count as a substantive partial closure

A convincing bounded result would demonstrate all of the following together:

- The observation and implementation service is purchased from actual operating output.
- Its real capacity can degrade or fail, and an admitted dishonest provider can avoid its cost.
- Existing paid scrutiny, with its additional workload charged, supplies the stated selection consequence for that alternative.
- Accepted observations have an explicit uncertainty model, and actions remain feasible under that uncertainty and their actual execution limits.
- Loss of governance has a specified physical transition; continued safe operation or graceful withdrawal does not rely on an invisible controller.
- The resulting financial and dynamic inequalities still have a nonempty feasible example after all these costs are charged.

The trusted kernel should then be named: perhaps a bounded-error physical measurement interface, a precommitted default contract, authentic escrow settlement and an unmanipulable assignment mechanism. Naming it does not invalidate the result. Calling those assumptions fully endogenous would.

## Hard resource-matched counterfactuals

1. **Direct maintenance instead of governance.** Spend the same additional allocation on C and G under a fixed conservative rule. Compare protection, achieved requests, capacity renewal and costs. If active governance adds no relevant benefit, its overhead has not earned its place.
2. **Observation without execution.** Retain and charge for the sensor, but remove or delay the actuator. Accurate diagnosis must not be counted as an implemented remedy.
3. **Execution without usable observation.** Retain the actuator while degrading, delaying or biasing accepted measurements within the declared threat class. Measure what the mechanism does when a common certified action is unavailable.
4. **False governance completion.** Admit providers who claim the governance tranche while delivering no functional package; remove the corresponding payment consequence while preserving nominal inspections. This tests whether their maintenance is selected or simply assumed.
5. **Combined funding and observation stress.** Reduce the fee base and let lower G degrade both enforcement and identifiability. A test that holds measurement precision fixed while its producing infrastructure disappears misses the central coupling.
6. **Fallback failure modes.** Compare the actual fallback with a frozen last command and a documented failure of its trigger or execution. Distinguish attacks covered by the theorem from violations of its declared kernel.
7. **Reintroduced alternatives.** After long favorable operation, impose the same small reintroduction of a false practice across arms. Long accumulation of favorable log odds can otherwise conceal present invasibility over a finite observation window. This is an imposed perturbation, not endogenous mutation unless modeled as such.

Match the initial resource stocks, prices, task process, feasible actuators and external interventions. Realized fee revenue and delivered maintenance are outcomes, so they should be recorded rather than forced to remain equal. Keep target attainment, protected conditions, uncertainty, operating costs and rule-change costs separate; no single aggregate should conceal a tradeoff or unachieved request.

The strongest honest contribution would be a condition under which an institution can purchase and retain the means of observing and revising its own operating rules, plus a counterexample showing how that capability disappears. It would still be a conditional architecture with declared physical and procedural primitives, not a model in which every source of trustworthy evidence and authority has been generated from nothing.

## Review of the frozen candidate

The coordinating and mathematical agents chose the following concrete candidate. Later sections record the completed mathematical and implementation checks.

### Actual fee diversion and the expanded ledger

Let `W=γF`, with `γ=.02`, purchase governance contracts. The previous operating inputs are reduced to `(1−γ)λF` for useful capacity and `V=(1−γ)(1−λ)F` for verification contracts. Thus governance is funded from the same receipts, rather than being an added subsidy. The complete flow balance is

```
useful work                         (1−γ)λF
verification work                   m h V
verification compensation           (1−m)h V
verification diversion              (1−h)(1−D)V
verification withheld reserve       (1−h)D V
governance work                      d z W
governance compensation              (1−d)z W
governance diversion                 (1−z)(1−D)W
governance withheld reserve          (1−z)D W
                                   -----------
total                               F.
```

Here `d=.3`, and genuine governance capacity is produced according to `Jdot=2500 d z W−J`. The two withheld flows enter inert reserves, without also funding current work. Initial positive C, G and J are endowed capital; the construction does not create their seed resources for free.

The verification half-saturation parameter changes from 1 to 1.1 to represent extra governance inspection load. This is a declared congestion technology, not a measurement of an actual 10% labor cost. It avoids treating the old inspection effectiveness as unchanged when an additional task is introduced, but its quantitative value remains an assumption. The purchased J package must explicitly cover sensing, aggregation, computation, communication and actuator operation or upkeep. The mathematical model may bundle these complementary services; it should not imply that some are costless simply because they lack separate stock variables.

### A three-practice repertoire separates maintenance from truth

The important repair admits three governance practices:

- a: maintain the service and report or command truthfully;
- b: maintain the service but submit arbitrary reports or commands;
- c: claim completion without delivering the service, also with arbitrary reports or commands.

Write `z=a+b` and `θ=a/z` when z>0. The first two have equal monetary payoff `(1−d)W`; the third has expected payoff `(1−D)W`. Under the specified replicator rule,

`zdot=ν_z z(1−z)W(D−d)` and `θdot=0`.

The conservation statement follows directly because a and b have the same per-capita growth rate. Paid completion audits select maintenance over nondelivery when D>d. They do **not** select truthful maintenance over lying maintenance. This is a strength of the repaired accounting: semantic truth is no longer silently awarded a bonus or assumed to be observable by an unspecified superior auditor.

The starting ratio θ=.9 is consequently a preserved input under this finite practice class. A lower bound z≥.9 supplies truthful weight `a=θz≥.81`. The general condition needed for the median argument is `θz>1/2`; on this proposed region it is sufficient that `θ>5/9`. A majority of maintainers is not by itself a majority of truthful controllers.

A particularly discriminating counterfactual converts a into b while holding z, J and every monetary flow unchanged. Once truthful weight ceases to be a majority, adversarial report and command values can control the median even though expenditure, maintenance and the financial selection indicator look healthy. This isolates the still-assumed truth coalition from the endogenous funding result. It need not be described as an inevitable attack: it is outside the conserved-θ theorem and is a direct test of that theorem's boundary.

### What majority aggregation actually guarantees

If more than half of authenticated weight reports a scalar observable inside `[v−e,v+e]`, every weighted median is inside that interval, regardless of other reports. Componentwise medians preserve the separate coordinate error bounds. They need not correspond to any one reporter or to a jointly feasible hidden state, so a robust controller must work for the resulting uncertainty box rather than assume its coordinates form a true state.

All truthful controllers can calculate the same command only if they receive the same aggregate and use the same declared rule. A weighted median of commands then equals their common command. Distinct honest local aggregates or unsynchronized controller states would require an additional analysis. Authenticated population weights, common aggregation, and a command interface that cannot be bypassed are the finite model's physical and procedural anchor. Maintaining their operating resources is endogenous; the correctness of their stipulated mapping is not derived from the payment equations.

No direct observation of the latent verification practice h is required if the controller uses the proved lower bound h≥.9 and robust bounds based on actual measured G and m. That is a conservative certificate, not an assertion that h has become observable. Its usefulness depends on the protected region being maintained jointly.

### Availability at the edge of the certificate

The revised genuine instrument error is `e(J)=.002/J` for J>0, with no informative instrument guarantee at J=0. Thus J≥1 yields the useful bound e≤.002, while the uncertainty bound diverges under depletion. This repairs an earlier candidate law that would have left a finite error guarantee at zero functional capacity. Actual actuation is limited by `R(J)=J/(1+J)`, which supplies the old rate budget .5 on the protected region and vanishes at J=0.

The positive theorem can remain entirely inside J≥1. It should not convert that protected result into a claim that accurate observation survives resource depletion.

Likewise, a no-command freeze of m is a possible passive actuator behavior, whereas an automatic reset of m requires a stated implementation. The final construction should say which is used. A proof that the funded region never reaches the unavailable mode does not constitute a recovery proof from unavailable initial states.

## Mathematical construction audit

The completed [mathematical note](../model/ANALYSIS.md) was read independently. It now uses the three-practice interpretation and `ν_Z=100`. Its protected region deliberately raises the work floor from the previous .45 to .48. This change is necessary for the revised budget: keeping the previous .45 floor would give a negative verification derivative at the lower corner after governance's fee diversion.

The robust controller uses a certified lower contractor share `h_bar=.9`, rather than reading latent h. Define `b0=h_bar p(G)−m−.02`. Its derivative bound uses the minimum paid verification input from the same joint region. The endpoint construction accounts for the entire coordinatewise error box: the lower observation bound is used for G, the upper bound for m in the upper command limit, and the lower bound for m in the lower command limit. The reported monotonicities of f(G,m) follow from differentiation. They make the observation-based bounds conservative for the actual state; the separate positive gap calculation establishes that conservatism has not made the interval empty.

An independent arithmetic check reproduced the key quantities:

| Quantity | Value |
|---|---:|
| Minimum actual fee flow F | 0.1901020408163 |
| Minimum verification-contract budget V | 0.09315 |
| Minimum governance-contract budget W | 0.00380204081633 |
| User advantage at the lower corner | 0.0298469387755 |
| Useful-capacity derivative at its floor | 0.0696551724138 |
| Verification derivative at its floor | 0.120182068966 |
| Governance-capacity derivative at its floor | 1.56637755102 |
| Limiting useful capacity C_R | 2.92904873619 |
| Limiting maintained governance capacity J_R | 3.25034744960 |

The separate funding requirements also reproduce: governance renewal requires γ≥.00779308562, while useful-capacity renewal permits γ≤.0465646806 at the chosen floors. These are certificate-specific necessary funding inequalities, not a complete operating interval for every other assumption. Their overlap shows that the example can pay for governance without silently retaining its former operating budget. It does not estimate a real institution's governance price.

The no-withholding argument also checks. For any initial z<1, integration of `log(1−z)'=ν_Z dWz` bounds total delivered governance spending. The linear stock equation then gives J→0 and finite integral of J. Because actual rule speed is at most R(J)≤J, total rule variation is finite and the rule approaches a limit. This is a loss-of-capability result, without an unsupported assertion that the remaining productive system or every share goes to zero.

No mathematical blocker was found in these checks. Implementation, trajectory and discrete-time checks remain separate; the theorem assumes a continuous deterministic population and the specified physical interface. Its conditional majority guarantee is `θz≥.81`, not an incentive theorem that truthful practice takes over. Under the stated dynamics, z→1 but truthful share a→θ=.9.

## Initial implementation checks

The [simulation implementation](../simulate_governance.py) was independently read and imported. Its physical accounting uses the reduced operating budgets and the full nine-flow ledger. In the no-withholding arm, discovered governance false claims retain payment: the withheld governance term becomes zero, fraud retention receives that amount, and the maintenance share's selected advantage becomes negative. Existing verification-contract withholding remains in place. This removes the named mechanism without inventing a replacement source of funds.

Independent execution of the algebra checks found a maximum ledger residual of 8.33×10⁻¹⁷, and a maximum derivative discrepancy of 1.78×10⁻¹⁵ against the prior physical equations after the declared budget and congestion changes. The 2,000 sampled states and their four observation-error corners passed the barrier checks. These numerical checks support implementation consistency; the exact inequalities in the mathematical note establish the all-state result inside its domain.

The truth-capture intervention changes θ at time 100 without changing z, J or the other physical states. Because θ is absent from the physical ledger, every contemporaneous monetary flow is unchanged. Accepted reports and commands can change immediately, and their later physical consequences alter the flows. This is an imposed change in practice composition, explicitly outside the conserved-θ theorem. It is not falsely labeled as an invasion generated by equal monetary payoffs.

An initial defect was reported to the coordinating agent: the unpriced and reallocated fixed-rule comparators evaluated the unused paid observation path before replacing its command. Because they allocate zero governance funds, J decays and the intermediate expression for a huge measurement-error interval eventually overflows. A direct import at J=10⁻¹⁸⁰ reproduced the error in both modes. The completed implementation repairs this by branching before unused paid-observer evaluation. The full comparison run then completed.

## Completed comparison audit

The [numerical results](../results/analysis.json) and stored physical/log coordinates were inspected. In the main funded cases, all protected state inequalities remain satisfied. Constant target 3.8 is reached to within .00080 over the final reporting window; the changing-target case preserves operation while refusing part of the requested 4.7 phase. Independent solver comparisons reported maximum physical-state differences of 2.84×10⁻⁶ for constant funded control, 8.05×10⁻⁶ for changing funded control, and 2.16×10⁻⁷ for the truth-capture case. These are numerical consistency checks, not interval-arithmetic certification of the trajectories.

The comparison outcomes support several distinctions that the report should preserve:

- The fixed rule reallocating governance funds to C/G remains operational, with limiting C=G=3. It misses changing requests. Active governance has a tracking benefit in these examples, alongside a visible opportunity cost in useful capacity.
- Sensing and actuation outages hold an already viable rule. Operation persists while later requested targets are missed. These are deliberate failures of an interface assumption, not evidence that every such failure causes collapse or that observation is universally necessary for static survival.
- No withholding, truth capture and command-router bypass produce severe operating depletion in the supplied trajectories. The separate no-withholding theorem establishes loss of governance capacity; the stronger operating depletion is a result of these specific simulated attacks and controls.
- The depleted trajectories retain finite encoded log states and tiny positive stocks or shares. For example, the no-withholding trajectory retains z≈.00308 after operating revenue disappears. Numerical output should not label every alternative exactly extinct.
- Low governance allocations γ=.002 and .005 breach J≥1 but continue operating in the tested cases. High allocations γ=.05 and .08 breach chosen operating floors but approach positive regimes. Initial z=.6 and .8 also recover in the supplied runs. Being outside the certificate is not equivalent to impossibility or collapse.

The summary boolean originally named `all_certificate_conditions_preserved` only evaluates state inequalities. It does not test every measurement, routing or execution premise; outage arms can preserve those inequalities while violating the interface assumptions. The coordinating agent was asked to name it as preservation of protected **state bounds**, or explain that restriction in the report. This distinction matters for interpreting the negative controls.

No remaining accounting or implementation blocker was identified after the overflow repair. The main inference is bounded: the chosen service can finance and maintain its observation and revision machinery, with protected physical instruments and a preserved truthful majority. Financial maintenance selection alone remains neutral between truthful and lying maintainers. The resource-preserving truth-capture comparison makes that residual dependency visible instead of silently assigning it to another perfect governor.
