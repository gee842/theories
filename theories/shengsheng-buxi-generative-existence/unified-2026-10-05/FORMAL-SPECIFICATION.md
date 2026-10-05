# Formal specification for the integrated generative theory

Version 0.2, 5 October 2026. AI-assisted formal development of Ren's research direction. This is a specification and a set of proof obligations, not a completed universal theorem. It extends the [formal core](FORMAL-CORE.md), preserves the existing theories, and is governed by the [completion plan](COMPLETION-PLAN.md). The [integration record](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/INTEGRATION.md) separates inherited results, new interface propositions, and pending work.

## 1. Research target and levels of claim

The subject is the coupled situation: differentiated centers, their relations, and the conditions through which they act. A center may be a useful coordinate or organization within this situation. It is not an isolated object subsequently given a free environment.

The positive research target is to explain whether, how, and across which physically characterized conditions activity produces and maintains increasingly shared possibilities for further activity. Ren's present use of 善 asks about a direction of reality itself. Moral goodness is a separate interpretation requiring further premises if asserted. The target must not be replaced by a definition that calls whatever persists good.

Keep four claims separate:

1. **Constitutive:** an activity depends on conditions and changes some conditions of subsequent activity.
2. **Mechanistic:** specified interactions generate, maintain, revise, or destroy particular organizations and capacities.
3. **Directional:** the actual dynamics favor specified changes in joint capability under a declared comparison, preparation, and timescale.
4. **Coverage:** the mechanism's premises hold throughout an independently described class, or with stated probability under a justified preparation ensemble.

The first is a proposed organizing commitment. The second has several conditional witnesses. The third has separate conditional mathematical results whose physical premises still need to be connected. The fourth is open. None derives the actual fundamental laws of physics from the mere existence of difference.

## 2. Common operational interface

Use a typed interface

\[
\mathfrak M=(\mathsf P,\mathsf O,\Pi,\mathbb P,\mathsf L,\mathsf T).
\]

Here \(\mathsf P\) specifies physical preparations and their uncertainty; \(\mathsf O\) specifies available observations; \(\Pi(p)\) contains physically realizable interaction protocols from preparation \(p\); \(\mathbb P_p^\pi\) is the law of recorded outcomes under such a protocol; \(\mathsf L\) records resources, work, transfers, duration and construction costs; and \(\mathsf T\) specifies functional and protected-condition tests. Outcome events and protocols must have measurable semantics wherever probabilities are used.

A protocol is an arrangement realized within the situation. Its sensing, memory, inference, action, maintenance and replacement must have physical implementations and ledger entries. Changing the installed controller is a physical intervention with a construction path. It is not a free choice by an outside optimizer.

Protocol-indexed laws must obey the restriction, continuation and causal-composition conditions of their physical realization. A protocol and its prefix cannot have arbitrarily unrelated laws. For the present classical specimen, histories and their conditional continuation laws share one nonanticipating construction, and actions depend only on the permitted past and present information. Other realizations must state their own valid composition rules; this condition does not impose a joint classical hidden state for incompatible experiments.

This interface does not require a common classical hidden trajectory for incompatible experiments. A classical stochastic process, a process with memory, and a quantum instrument model require different realizations of the protocol-to-outcome law. Compatibility at the interface is a language for comparison, not evidence that one realization covers every physical regime. A quantum specialization and its composition laws remain work to do.

For the current classical specimen, use a joint state such as

\[
x=(n_R,n_C,n_Y,n_D,e,s,m,c,v,a,\ell,t).
\]

The roles are material counts, accessible work reserve, source/sink condition, memory, installed controller, evaluator, action permissions, succession state and time. Include only roles present in an actual specimen, and include additional memory when needed for closure. A biological model need not have an institutional permission register. A source held fixed by a reservoir is an explicit boundary condition; enlarging the boundary requires modeling that source too.

The actual installed dynamics and the possible protocol family have different uses: the former predict what happens; the latter define what a situation can do. An existentially feasible protocol does not establish its construction, selection, or use.

## 3. Physical realization obligation

A first [declared stochastic realization](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/STOCHASTIC-REALIZATION.md) now supplies the event table for the existing shared-resource equations, exact material/work-equivalent accounting, nonexplosion and a finite-system absorption proof. The [joint-capability bridge](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/JOINT-CAPABILITY-BRIDGE.md) derives finite-horizon probabilities and a restricted capability comparison directly from that generator. Physical identification, a larger protocol class and a reduced regime-transition law remain open.

The [constructed-regulation extension](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/PHYSICAL-REGULATION.md) now adds material G, fuel binding and catalytic inhibition to that same process. It supplies explicit formation, switching, wear and replacement costs; bound Y retains reproduction. An exact finite-copy binding diagnostic proves the intended fuel-response sign in its isolated assay. The [construction-lag theorem](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/REGULATION-LAG.md) proves an early reserve debit before inhibition can act. The [prespecified whole-process comparison](../../../experiments/shared-renewal-capability/regulation/README.md) is unfavorable in all tested constructed-versus-absent assay comparisons, including stronger source conditions. Physical regulation exists in the model, but net generative advantage does not follow from that fact. These numerical results have truncation accounting and internal checks, not a directed-arithmetic certificate or external validation.

For a countable, nonexplosive jump realization, specify elementary events \(r\), state updates \(\nu_r\), and propensities \(a_r\):

\[
(\mathcal L_\theta f)(x)
=\sum_r a_r(x;\theta)[f(x+\nu_r)-f(x)].
\]

Continuous energy storage or deterministic source variation may require a hybrid process instead. Prove state-space invariance and nonexplosion under the declared preparation and source assumptions. Every consumptive event must be disabled when its physical inputs are unavailable.

The event specification must supply:

- material conservation or measured boundary exchange;
- total-energy accounting, separately from usable-work accounting;
- the capture process, fuel or radiation source, waste route and work dissipation;
- formation and loss of the relevant machinery;
- any seed, mutation, transport or restart channel and its cost;
- physical observations and controller modifications when those are part of the claim.

The current concentration equations do not uniquely identify this event law. Adding equal opposing event fluxes can leave the drift unchanged while changing fluctuations and escape probabilities. A mesoscopic realization therefore starts as a declared model, then requires independent physical identification. Thermodynamic consistency is an additional condition; a nonnegative abstract energy reserve alone does not prove it. Stochastic thermodynamics constrains work, heat and entropy distributions under specified reservoir assumptions; it does not license nonnegative entropy production on every individual trajectory. See [Seifert's review](https://arxiv.org/abs/1205.4176).

## 4. Joint capability, with information and costs included

Fix a finite assay vocabulary initially: outputs \(q\in\mathbb R_+^d\), common horizon \(H\), reliability \(\alpha\in(0,1]\), and protected-condition tests. Define the event \(E(q,H)\) to require all outputs jointly, all protected conditions at the stipulated times, and every-prefix ledger feasibility.

For a specified preparation distribution \(p\), define

\[
\mathcal C_{H,\alpha}(p)
=\{q:\exists\pi\in\Pi(p),\quad
\mathbb P_p^\pi(E(q,H))\ge\alpha\}.
\tag{1}
\]

If preparation uncertainty is a set \(\mathcal P\), use

\[
\mathcal C_{H,\alpha}(\mathcal P)
=\{q:\exists\pi\in\Pi(\mathcal P),\quad
\inf_{p\in\mathcal P}\mathbb P_p^\pi(E(q,H))\ge\alpha\}.
\tag{2}
\]

The same protocol must work for the uncertainty it cannot distinguish. The order of the quantifiers is essential. The existence of a different successful protocol for each hidden microstate is insufficient.

The assay vocabulary describes physically testable functions; protected conditions are declared separately. These can include individual reserves even when aggregate production survives. Protection is not inferred from a favorable total. If new functions appear, compare both situations in a common extended vocabulary with explicit interpretations, rather than comparing dimension counts. Open-ended discovery of such tests remains an additional problem.

Order capability regions by set inclusion. This gives a partial order on regions and a preorder on physical situations; different situations can have identical regions. Regions may be incomparable. A larger scalar volume, mean score, or longer survival does not imply inclusion.

The joint-capability bridge now gives a concrete fixed-reliability example: on eight joint tests of recycling, assembly and retained work reserve, the autonomous-run regions for two catalytic coefficients are incomparable at H=1/4 and reliability 1/2. The computation includes continued activity and all modeled packet costs. These regions are exact for the singleton installed protocol and only inner bounds for a larger physical protocol class. Opposing tail probabilities alone would not have sufficed; the calculation supplies crossing witnesses at the same reliability.

For future capability, evaluate the physically available preparation and information after the specified history. Any state information needed by the protocol must be obtainable there. A hidden microscopic state used by the analyst does not grant the actor access to it. Time spent transforming a situation and resources used in the transformation must be charged before comparing future possibilities.

## 5. Composition and abstraction: two interface propositions

**P1 — Sequential certification.** Suppose a realizable first-stage protocol reaches a declared entry set while meeting all of its prefix conditions with probability at least \(1-\varepsilon_1\). Let \(E_1\) denote that success and \(\tau\) its completion time. Require one implementable observation-adapted continuation rule, not a separately chosen rule for each hidden history. For this rule suppose \(\Pr(E_2\mid\mathcal F_\tau)\ge1-\varepsilon_2\) almost surely on \(E_1\), where \(\mathcal F_\tau\) is the full modeled entry-history information and \(E_2\) its successful continuation. The rule itself can use only the declared accessible sub-information. Require compatible physical interfaces, retained resource debits, and combined elapsed time. Then their implemented composition succeeds with probability at least

\[
1-\varepsilon_1-\varepsilon_2.
\]

Proof: failure is contained in first-stage failure or second-stage failure following first-stage success. The latter has unconditional probability at most \(\varepsilon_2\). No independence assumption is used. A tighter product bound is available from the same uniform conditional guarantee, but the union bound composes simply over multiple stages. A separate pair of experiments does not establish the required conditional premise.

Here \(\tau\) is a stopping time in the modeled history filtration, and \(E_1\) is measurable at \(\tau\). Prefix and continuation laws must be the compatible laws of the same implemented composition as required in Section 2.

**P2 — Capability transfer through a justified approximation.** Fix identical assay semantics, time and resource accounting. Suppose every coarse admissible protocol has an admissible microscopic implementation, and every microscopic admissible protocol has a corresponding coarse one. Require success-probability discrepancy at most \(\delta\) for every matched protocol, preparation and assay. For \(0<\alpha-\delta\le\alpha+\delta\le1\),

\[
\mathcal C^{\rm coarse}_{H,\alpha+\delta}
\subseteq\mathcal C^{\rm micro}_{H,\alpha}
\subseteq\mathcal C^{\rm coarse}_{H,\alpha-\delta}.
\tag{3}
\]

Proof: transfer a witnessing protocol in either direction and subtract at most \(\delta\) from its success probability. The same argument applies to (2) when the same implementing protocol corresponds across the entire uncertainty set and the error bound holds uniformly over preparations. Choosing a different hidden-preparation-specific implementation is insufficient. One-way implementability gives only the corresponding inclusion. Good prediction under a single controller does not establish this two-way capability contract.

For a discrete-time reduction with matched initial laws, preserved observations and interventions, and uniformly bounded conditional one-step total-variation error \(\epsilon\), a coupling gives path-law error at most \(1-(1-\epsilon)^n\le n\epsilon\) over \(n\) steps. This is not a bound from average training fit. Continuous-time reduction needs its own rate/coupling or path-law argument. The [causal-foundations results](../../../_process/research/2026-10-05-causal-foundations/outputs/formal-results.md) supply the existing abstraction contract.

These are elementary conditional interface propositions, not new fundamental laws. They explain exactly how a validated result could feed the next result without losing its guarantees.

## 6. Deriving actual transitions

Use the physical realization to derive first-entry probabilities, passage-time distributions, residence times, exit destinations and extinction. An ordered birth–death chain is permitted only after showing that its levels represent distinct nested capability regions and that its transition structure and memory assumptions are justified.

Exact lumpability, a controlled metastable approximation, or an explicit memory-dependent kernel are possible routes. An inverse mean residence time alone does not establish an exponential holding-time law. A deterministic attracting equilibrium alone does not establish a finite stochastic stationary active state.

Keep three outcomes separate: finite-horizon performance; the unconditional stationary law, when it exists; and survival-conditioned or quasi-stationary performance. If a finite process is ultimately absorbed into inactivity, a positive quasi-stationary result cannot be reported as indefinite unconditional persistence. Restart must be a modeled physical event rather than a favorable boundary rate inserted afterward.

An [exact response identity](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/REGULATION-RESPONSE.md) now supplies a direct alternative to prematurely reducing the model to ordered regimes. On a common finite state space, augment the event counts needed for a joint terminal test f. For function semigroups P_i(t)=exp(t L_i),

\[
(P_1(H)-P_0(H))f
=\int_0^H P_1(t)(L_1-L_0)P_0(H-t)f\,dt.
\tag{3a}
\]

Thus a reaction change affects a joint possibility through both its rate and its conditional downstream consequences. The construction contrast consumes R and F in the state update itself; costs need not be inserted as an arbitrary scalar penalty. The sign remains a mechanistic calculation. The linked proof handles the unbounded original reserve through explicit overflow errors rather than assuming an unbounded-operator identity. This compares individual installed joint tests; it does not by itself establish the stronger future-capability distribution order below.

## 7. Exact directional target

Let \(F\) and \(0\) be two declared physical arrangements, such as functioning shared renewal and a specified alteration to it. Match preparation, exogenous source schedule, assay semantics, observation opportunities and comparison time; retain unavoidable construction and maintenance costs in their respective ledgers. Specify the altered mechanism before observing results.

Let \(\mathcal G_t\) be the physically accessible record. In a closed classical state model, use the preparation \(p_t=\operatorname{Law}(X_t\mid\mathcal G_t)\), under a declared model and prior, and set \(\mathbf C_t=\mathcal C_{H,\alpha}(p_t)\). If the model/prior is uncertain, retain the declared conditional uncertainty set. If memory remains outside the state, use the conditional continuation process rather than assume that a state posterior is sufficient. The record includes installed arrangements, permissions and source phase where needed; analysts cannot reveal hidden microstates for free. This definition uses regular conditional laws where they exist, as in the countable or standard Borel settings contemplated here.

Let \(\mathbf C_t^F\) and \(\mathbf C_t^0\) denote these random future capability regions under the actual installed dynamics, using the same future assay horizon and reliability. For a measurable upward set \(U\) of regions, the strong finite-time target is

\[
\Pr(\mathbf C_t^F\in U)\ge
\Pr(\mathbf C_t^0\in U)
\quad\text{for every such }U.
\tag{4}
\]

For strict directional gain, require strict inequality for at least one prespecified nontrivial comparison. The simplest first implementation uses finitely many assay profiles and their attainable subsets, avoiding unproved measurable-random-set machinery. A continuous-region extension must supply its measurable structure.

Specify in advance whether (4) is required at selected times, throughout an interval, or only for stationary laws. A stationary comparison does not imply an early-time advantage. A comparison between interventions also does not by itself prove spontaneous temporal progress within one unaltered world; that claim needs its own preparations and time-comparison theorem.

The existing [birth–death result](../../../_process/research/2026-10-05-support-and-shared-generativity/outputs/shared-generative-direction-mathematics.md) proves stationary stochastic dominance from improved adjacent formation/loss ratios. It supplies a conditional final step. The physical mechanism has not yet been shown to produce those ratios, and the current \(C,Y\) construction has not been shown to produce nested capability regions.

For a class-wide claim, quantify over an independently specified class \(\mathscr D\) of mechanisms, sources and preparations. Do not define \(\mathscr D\) by whether (4) holds or whether its transition ratios improve. If the claim is about typical systems, specify and justify the ensemble measure. A finite successful sample does not establish unrestricted universality.

## 8. Formation, selection, learning and revision

In models containing adaptive centers, put evaluators, recognition, records, permissions, construction and succession into the realized process. The relevant target is the probability that such arrangements form, remain usable, and pass the capacity/direction tests under actual dynamics. Feasibility alone is insufficient.

The [concern study](../../../_process/research/2026-10-05-concern-theory/START-HERE.md) supplies conditional learning and renewal; [revisable concern](../../../_process/research/2026-10-05-revisable-concern/START-HERE.md) adds finite reason-extension and strategic obstruction. The completed [joint-formation theorem](JOINT-FORMATION-MATH.md), accepted in the [contribution review](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/JOINT-FORMATION-INTEGRATION.md), now joins useful learning, acquired concern, paid evidence/control, a persistent opponent and fully funded rebuilding. It proves existence of a protected subgame-perfect equilibrium under explicit conditions. Financial viability survives the stated operator deviations along selected trustee continuations; patient safety is an equilibrium-path guarantee. Arrival at that equilibrium, empirical prevalence and physical-direction comparison remain distinct obligations.

The completed [revisable-concern settlement](REVISABLE-CONCERN-SETTLEMENT.md), accepted in the [source review](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/CONCERN-SETTLEMENT-INTEGRATION.md), extends this conditional strategic construction with paid scope revision, retained grounds, retraction and succession. Its gate-price and tie-selection repair is essential. Supplied normative anchors, sound known-context audits, authority and equilibrium-path protection remain premises; admitted scope does not define moral standing. The ethical decision results are not yet composed with the strategic theorem. Bounded feature construction is not unrestricted discovery. Its evidence reanalysis adds no observations, and the proposed human study is unrun. This closes the registered source review, not I1–I6 or the overall goal.

Do not assume that preserving these architectures is selected simply because they are useful to the whole. Account for cheaper insulation, suppressed learning, destruction of reserves, bypassed control, misleading evidence and incentives to exclude affected parties. The supplied repertoire and primitive evaluative routes remain premises until their formation receives its own mechanism.

The [installed-process certification](../../../sources/20-codex-theory-sessions-2026-10-05/full-picture-conjecture/outputs/combined-process-proof.md) supplies an existing route for certifying actual safety and recurrent delivered functions, including changing controllers. Its finite witness is useful for composition; it does not derive its supplied technologies, calibration, protected duties or environment.

## 9. Six acceptance interfaces

| Interface | Output required before the next step |
|---|---|
| I1 Physical realization | Well-defined event/history law, balances, source/sink assumptions, formation/restart pathways and identified parameters |
| I2 Implementation | Realizable observation and intervention protocols with all costs and information restrictions |
| I3 Joint capability | Certified assay regions, protected conditions, and compatible composition guarantees |
| I4 Actual dynamics | Derived regime transitions or retained memory, quantified approximation, extinction/restart treatment |
| I5 Direction and formation | A proved comparison with the favorable sign derived from mechanism and costs; actual formation/retention where claimed |
| I6 Coverage and evidence | Independently described domain, counterexample search, competing predictions, outside-domain checks, and empirical validation |

Moral interpretation is a separate optional argument for the current descriptive request. The existing [ethical foundation](ETHICAL-FOUNDATION.md) is retained; it does not convert (4) into a theorem of moral goodness. More attainable activity can include harmful activity, and an aggregate gain can coexist with an affected being's loss unless protection is included and justified.

The complete formal account must also say what distinguishes this proposal from established reaction-network, control, evolutionary and institutional explanations. Standard mathematical tools are welcome; predictive or unifying contribution must be demonstrated rather than inferred from vocabulary.
