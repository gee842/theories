# Validation design for a finite, nonfinancial closure study

5 October 2026. Internal AI research-design memo. This is a synthetic model-validation protocol, not an empirical study or a new paper. The coordinating agent's finalized model and protocol should state which candidate mechanisms below are adopted. Mathematical validation of a finite kernel does not validate its interpretation as a real institution or a universal theory.

## The question and the unit of explanation

Can a specified appointment-and-work process preserve the means to learn from consequential experience, implement a changed response, and transmit the required skill through replacement of its participants? When does its own appointment criterion instead favor activities that remove those means?

The model should link five mechanisms inside the actual transition process:

1. an installed criterion selecting an incoming evaluator or practice;
2. production and admission of experience relevant to a changing situation;
3. effective amendment of the response being used;
4. regeneration and loss of skilled carriers;
5. succession that changes the criterion and future work allocation.

These links must be checked individually. Renaming the whole process “adaptive” does not establish that they are present. The finite model concerns two represented criteria and a fixed family of possible contexts and responses. It can model succession of these criteria, not the open-ended emergence of every possible purpose.

## A small candidate state with actual nonfinancial mechanisms

The coordinating agent proposes 72 states:

`s=(e,r,q,k,b)`.

- e∈{0,1}: the current case context;
- r∈{0,1}: the implemented routine or response;
- q∈{volume, adaptive}: the installed appointment/work criterion;
- k∈{0,1,2}: the number of available skilled carriers;
- b∈{none,0,1}: a retained context record that can inform a response.

All five variables have distinct causal roles. The controller must use b and other declared observations, not hidden e. The environment may use e when determining whether the implemented response has an adequate consequence. Computing a physical consequence from e is not the same as giving e to the evaluator.

There are three work plans, each using two time slots:

| Plan | Slot one | Slot two | Direct limitation |
|---|---|---|---|
| F | Complete a case | Complete another case | Produces neither a new inquiry record nor an apprentice |
| Q | Complete a case | Inquiry into the current context | Can improve information; does not add a skilled carrier |
| T | Complete a case | Apprenticeship | Can add a skilled carrier when an existing mentor is available; does not identify a new context |

The installed volume criterion favors F. The candidate adaptive work rule uses T when k=1 and Q when k=2; with k=0 no skilled inquiry or apprenticeship can occur and the work plan is F. This is a declared institutional rule, not an optimal policy derived from a universal scalar. Its consequences must be compared with alternatives, including excessive teaching, excessive inquiry and an externally maintained version of the same rule.

Apprenticeship can increase k only when k>0. A departure can remove a skilled carrier. Thus skill is reproduced through actual work and lost through lifecycle events; the model contains neither an immortal qualified evaluator nor free spontaneous recreation from k=0. An external qualified entrant, if included, must be recorded as an environmental source. Its rate and contribution must be held constant across the comparisons that claim to isolate institutional mechanisms.

The proposed appointment probability is

`P(q_next=adaptive | q,k)=k w_q/(1+k w_q)`.

The suggested weights are w_volume=1/4 and w_adaptive=4. This represents a weighted appointment procedure over k qualified adaptive candidates and a unit mass of routine candidature. The weights express incumbent criteria; they are not monetary returns or a reproduction payoff. They remain modeling assumptions. If described as portfolio scoring, state which completed-work, inquiry or teaching records justify eligibility and weight. Merely writing two weights does not demonstrate that appointments respond to observed performance.

## Event ordering to freeze before computation

The exact order matters. The finalized kernel should specify one complete period in an explicit order, such as:

1. A context transition occurs, or the current context remains in place. The controller is not automatically told its value.
2. The incumbent criterion assigns a work plan from the available skilled-carrier state.
3. Inquiry, if attempted by a qualified carrier, produces a noisy raw observation. Admission is a separate event that determines whether that observation replaces b.
4. A proposal derived from the admitted record may change r through the specified amendment channel. The model must say whether it occurs before or after the period's completed cases and whether it consumes part of the inquiry slot.
5. The completed cases produce observable or physical consequences. Record adequacy and completion count separately.
6. Apprenticeship produces a new skilled carrier only when its actual prerequisites hold. Turnover and any consequence-induced loss are applied in their stated order.
7. The actual appointment procedure selects the successor criterion from the surviving candidates. Records are retained, altered or lost according to an explicit handover mechanism.
8. If the model allows an external entrant, apply its stated arrival and transfer rule without also calling that transfer internal regeneration.

Equivalent orderings are acceptable, but must not be mixed across the implementation, proof and explanation. In particular, a current successful inquiry cannot justify a past appointment unless the observation already existed at that appointment time.

Each probabilistic primitive should have a direct interpretation: context switching, observation error, admission, execution, departure, candidate selection or arrival. Simple rational probabilities permit exact transition probabilities and transparent sensitivity checks. They are illustrative rates, not empirical estimates.

## A structural integration test before claiming closure

The initial candidate has an important possible deficiency. If q and k evolve independently of e, r and b, then skill and criterion dynamics support an information-action module, but case experience never changes the institutional dynamics supporting it. The transition graph is partly triangular. That is a legitimate model, but not yet the requested full reciprocal loop.

A minimal repair is to let an inadequate case response create a physical overload or repair burden that changes subsequent skill loss or delivered apprenticeship. This uses the actual consequence in the plant equation without disclosing hidden e to the controller. Another possible repair lets an actually obtained and admitted validation result change candidature or appointment weighting. These are different mechanisms and should not be quietly combined.

The final model should document a closed causal path such as

`q → work allocation → inquiry/teaching → b and k → implemented r → consequences → k or appointment evidence → successor q`.

Check this path directly from the transition construction and with a controlled intervention. A claimed feedback edge that can be removed without changing any transition is not present.

It is particularly important to specify whether ordinary turnover and overload can remove two carriers in one period or only one. A bounded one-loss process can have an invariant skill floor under a suitable work rule; two simultaneous losses can defeat it. A rare positive-probability route to k=0 can dominate the infinite-horizon conclusion even when its finite-time effect looks small.

## Comparisons that identify mechanisms

Use the same initial state, context process, time slots, turnover, error rates and external arrivals wherever the intervention does not explicitly change one of them.

| Arm | Intervention | Purpose and qualification |
|---|---|---|
| Actual institution | All appointments, records, work and amendments follow the endogenous kernel | Main process to be assessed |
| Protected criterion | Keep q adaptive externally; retain actual evidence, execution limits and turnover | Isolate the cost of selecting and transmitting the rule; label the external protection |
| Perfect information only | Supply correct current evidence while retaining actual appointments and other mechanics | Isolate informational limitation; this is an ideal information intervention |
| Ideal external controller | Supply the declared ideal information and protect the chosen rule, under a specified action interface | Benchmark, not evidence that the actual institution implements this controller |
| No apprenticeship delivery | Keep the assigned time cost but suppress the addition of a skilled carrier | Test regeneration rather than crediting nominal training |
| No new record admission | Raw inquiries still occur; new evidence cannot enter b | Test the admission channel; retained old records may remain |
| No effective amendment | Proposals and records remain; changes to r are not executed | Test implementation separately from diagnosis |
| No institutional feedback | Remove the consequence-to-renewal or consequence-to-appointment link while keeping the other mechanisms | Determine whether the claimed reciprocal loop changes the prediction |
| No external entrant | Set the outside restoration source to zero | Distinguish endogenous continuity from repeated outside rescue |

Observation production and evidence admission can induce identical state kernels when both merely prevent b from updating. Record raw observations, admitted records and executed changes as separate event outcomes; otherwise the model cannot distinguish these explanations using final performance alone. These event records need not enlarge the causal state unless their history changes future transitions.

Do not force realized outcomes to match across arms. Case adequacy, completed work and skilled capacity are outcomes. Time slots and permissions are controlled inputs. A control that reallocates a removed inquiry slot to more completed work asks a different question from one that keeps the slot occupied but disables the information it produces; report the distinction.

## Outcomes without a universal objective

Report a profile rather than one optimized score:

- adequate-case probability and number of adequate completed cases;
- completed-case count and resulting delay or backlog, if modeled;
- probability and expected time to skill depletion;
- probability and time to recovery after depletion or turnover;
- raw inquiry, admitted evidence and executed amendment rates;
- recurrence of actual teaching, inquiry and successful response after a contextual change;
- time spent under each criterion and dependence on external entry.

An institution can trade some completed volume for continuity or informed response. The mathematics should expose those consequences rather than declare one criterion morally superior. If a protected condition is changed between comparisons, report that change separately from any change in the underlying process.

## Exact finite-state verification

Once all transitions are frozen, enumerate every state and every possible event sequence. Construct the actual transition matrix P from those events, rather than choosing next states to satisfy the desired property.

Validation should include:

1. **Kernel accounting:** every transition probability is nonnegative and every row sums to one; resource/time and carrier changes match the event sequence, including arrivals and departures.
2. **Independent implementation:** compare event enumeration with an independently written one-step simulator or transition builder over every finite state. Agreement between two solvers using the same incorrect matrix is insufficient.
3. **Exact support graph:** use the positive-probability transition support to identify reachable states and bottom strongly connected components. Rational primitive probabilities allow support to be decided without an arbitrary floating-point threshold.
4. **Finite-horizon probabilities:** compute survival, hitting and recovery by matrix recursions or the corresponding absorbing-chain construction. Call these exact only if exact arithmetic or a justified error enclosure is actually used. Otherwise report numerical error, residuals and conditioning.
5. **Long-run classes:** classify recurrent outcomes for every allowed initial state, not only a favorable initial distribution. Stationary occupancy and expected return times require the relevant class assumptions; reducible chains can have several limiting classes.
6. **Temporal obligations:** if correction must follow a discrepancy or turnover, add a finite monitor for the pending obligation. A count of amendments somewhere in the run does not establish that a required amendment occurred in response to the event in question.

For a finite chain, an almost-sure safety claim requires every positively reachable state to satisfy the safety condition. For conjunctions of ordinary recurrence obligations, every reachable bottom recurrent class must meet each required event set, with event sets represented by an appropriate state monitor if necessary. These are properties of the actual kernel. The existence of a different controller satisfying them does not imply that the endogenous appointment process does so.

## Rare failures and the horizon trap

Finite good trajectories cannot validate indefinite preservation. If a finite chain is irreducible and contains an unsafe state, that state is eventually reached with probability one. A very small transition probability may make the expected waiting time very large without changing this conclusion.

If k=0 is absorbing and is reachable from every recurrent candidate regime with positive probability, eventual depletion can be certain. External arrivals may instead make depletion temporary and produce a stationary mixture of operational and failed episodes. Such a system can have high availability and repeated recovery without satisfying “never fails.” These are different achievements.

Accordingly, report separate results for zero error, positive error, zero outside entry and positive outside entry. Inspect changes in the support graph as well as smooth changes in numerical rates. A probability set to exactly zero can change recurrence classes discontinuously. Positive results that depend on that zero should say so.

## Actual falsifiers and scope of completeness

The study can falsify its own proposed mechanism or claimed adequacy in several concrete ways:

- The actual institution cannot sustain a claimed condition that an external controller sustains under the advertised boundary.
- A supposedly essential channel ablation has no effect because the channel is absent, redundant or not binding in the tested regime.
- The proposed feedback is triangular rather than reciprocal, or predicts no additional effect beyond a fixed-criterion model.
- A long favorable trajectory hides almost-sure eventual failure or dependence on repeated external restoration.
- A criterion labeled adaptive depletes a required capability, or gains apparent adequacy only by changing the scoring rule.
- Independently constructed transitions disagree, or a proof assumes an observation or action that the actual process never supplies.

“Complete and validated” can be meaningful relative to the declared finite question. It would mean that the state and event semantics are fixed, all relevant mechanisms within that question are represented, the actual transition kernel is verified, the claimed temporal properties are checked for the stated initial conditions and parameter class, and every conclusion is separated from its boundary assumptions. Exact checking can resolve every state of that finite model.

That does not establish that the state description captures a real institution, that the rates are realistic, or that the mechanism transfers to ecology, life and AI in general. Those require independent operationalization, observations and interventions. This study can close a specified synthetic mechanism-and-verification task while leaving broader empirical and normative questions open. Calling it a complete general theory would conflate those levels.

## Review after the primary protocol was frozen

The [primary protocol](PROTOCOL.md) now adopts the 72-state construction and repairs the missing reciprocal link. Inadequate case response raises attrition probability from `delta_base` to `delta_base+delta_failure`, while leaving the hidden context unavailable to the policy. Attrition changes both skilled capacity and the opportunity for criterion succession. The protocol removes this consequence-induced component in a required control. Thus the implemented-response branch can affect subsequent institutional continuation through a declared physical/social consequence.

The event order also makes the positive benchmark transparent: apprenticeship precedes attrition, and at most one carrier is lost in a period. Under protected adaptive succession, k=1 triggers apprenticeship to two, and k=2 triggers inquiry; either case leaves k≥1 after at most one departure. The actual endogenous appointment process lacks that protected succession premise.

A simple bound exposes the difference before any simulation. Let `delta_base>0`, let all appointment weights be finite with maximum `w_max`, and exclude outside entry. From any state with k>0, the first turnover leaves at most one carrier. With probability at least `1/(1+w_max)`, it appoints the volume practice. A second turnover then removes the remaining carrier because the volume practice performs no apprenticeship. Consequently a depletion path exists within two periods with probability at least

`epsilon = delta_base²/(1+w_max) > 0`.

This is a conservative uniform bound. Conditional survival through n two-period blocks is at most `(1−epsilon)^n`, so eventual depletion has probability one. The argument does not require independent blocks. A very large but finite adaptive appointment weight makes the path rarer; it does not make the acceptable set closed. Exact matrix calculations can provide much sharper finite-horizon probabilities and expected times.

The protocol's gate controls have a useful exact prediction. Starting with routine and stored record both zero, preventing new evidence admission or preventing execution keeps the implemented routine at zero in both arms. Their records can differ, but their routine, adequacy, skill and criterion marginals should agree. When failure-induced attrition is removed, the skill/criterion marginal must also agree across ordinary, no-admission and no-execution arms. These are genuine structural falsifiers of the implementation, not merely desired qualitative plots.

The protected-succession comparator is an explicitly supplied appointment rule under the same imperfect inquiry and lifecycle processes. It is sufficient to exhibit the difference between available institutional control and the actual endogenous rule. It has not been proved optimal for the separate outcome dimensions, and should not be described as such.
