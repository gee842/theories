# When another's consequences change action

6 October 2026. AI-authored empirical contribution to [generative grounding](GENERATIVE-GROUNDING.md), following [Ren's clarification](../../../sources/15-codex-theory-conversations/2026-10-06-alignment-governance-and-future.md) that external relations can enable cognition and continuation before an actor reflects on them. This study examines **a recipient-linked consequence → learned action selection with unchanged offered food**, a supporting connection within the larger task of explaining and justifying concern.

The reanalysis finds a **16.69-percentage-point larger decline in preferred-action incidence** in the archived male contingent-harm group than in the male no-harm group. Almost all of the difference appears as alternative-lever responses. This is a descriptive result from published data, with condition assignment and possible cohort differences unresolved. It supports empirical contact with social consequence learning; it does not identify the acquisition of moral concern or establish an ethical reason.

## What the original experiment makes observable

Hernandez-Lallement and colleagues' [2020 study](https://doi.org/10.1016/j.cub.2020.01.017) gives a rat two food levers. During baseline, neither harms the neighboring rat. In the main harm condition, the actor's initially preferred lever subsequently also delivers a footshock to that neighbor; the offered food remains one pellet per response on either lever. Main-condition levers require different forces, fixed within an animal. Each session starts with mandatory samples of both options, followed by free-choice opportunities. The paper includes no-harm, noncontingent-harm, prior-experience and unequal-food comparisons. The [institutional primary paper](https://pure.knaw.nl/ws/portalfiles/portal/13278204/hernandez2020.pdf), source files and precise methods audit are preserved locally.

This gives a substantive connection between an action and an externally directed physical consequence. It is more specific than describing a displayed score as another's welfare. However, the released choice file does not contain a separate hardware receipt or measure the recipient's experience on every trial. The source's event law, observations and interpretation still matter. No new animal experiment or shock delivery was performed for this reanalysis.

## Selection, provenance and the comparison

The [source archive](../../../sources/30-recipient-harm-valuation-2026-10-06/README.md) preserves the original OSF project `65j3g` files, version metadata, licenses and paper. Four OSF originals match their upstream hashes. The trial CSV and workbook choice sheet agree in all 7,128 cached cells, including headers and blanks. There are 78 released trial-file actors and 142 summary-file actors; the publication's ordered-rat count is not an assignment ledger linking every animal to these files. The [source audit](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RECIPIENT-VALUATION-EVIDENCE.md) retains that coverage limit.

The [protocol](../../../experiments/recipient-harm-valuation/PROTOCOL.md) and a [schema clarification](../../../experiments/recipient-harm-valuation/SCHEMA-CLARIFICATION.md) were hashed before new local aggregates. Published findings, reported nonperformance and a few discovery rows were already known. This is retrospective reanalysis with fixed computations, not a preregistered discovery or a replication in another population.

The primary comparison includes every released male actor in the relevant groups: 12 contingent-harm and 14 no-harm actors. The 12 female harm actors remain a separate cohort because the archive contains no female no-harm comparison. No actor was selected by switching strength, successful performance or a desired effect. Each actor supplies 20 recorded baseline opportunities and 60 opportunities across the three subsequent sessions.

The primary outcome is preferred-lever responses **per offered opportunity**. We separately retain alternative responses and explicit nonperformance, then report preferred choice conditional on a recorded completed response. Equal offered food does not mean equal realized food intake or equal private experience. Counting every nonresponse as a harmless choice would change the scientific question.

## The observed change

| Primary group | Actors | Baseline preferred responses per opportunity | Subsequent preferred responses per opportunity | Within-actor mean change |
| --- | ---: | ---: | ---: | ---: |
| Male contingent harm | 12 | 72.92% | 51.11% | −21.81 percentage points |
| Male no harm | 14 | 81.07% | 75.95% | −5.12 percentage points |

The exact difference in changes is `−841/5040`, or **−16.69 percentage points**. The full outcome decomposition is:

| Change contrast: harm minus no harm | Percentage points |
| --- | ---: |
| Preferred-lever responses per opportunity | −16.69 |
| Alternative-lever responses per opportunity | +16.41 |
| Nonperformance per opportunity | +0.28 |

These components sum to zero. The male harm group has two nonperformed opportunities among its 720 subsequent opportunities; controls complete all 840. Thus the principal observed difference is not explained by treating silence as an alternative response. The companion completed-choice contrast is −16.50 percentage points, under its separately stated denominator.

Every single-actor omission retains the negative primary contrast, ranging from −19.24 to −12.76 percentage points. Omitting each recorded SBL label in turn also retains it, ranging from −21.55 to −11.83 percentage points. Those are influence checks on this archive, not population confidence intervals and not a repair for group confounding. In particular, SBL labels do not overlap between the primary groups, and their precise meaning is undocumented. The methods describe shared cages but the file does not provide a confirmed cage mapping. No independent-actor sampling assumption or randomized-assignment p-value is used.

Preference is defined from baseline itself, so subsequent regression toward the mean is a real concern. Both groups' changes must therefore remain visible. A no-harm comparison is informative without proving that every possible history, baseline-selection effect or group difference is controlled.

## Experience and cost boundaries

The 14 male actors without prior firsthand shock experience show a −5.24-percentage-point change in preferred-action incidence. Compared with the exposed male harm group, the change contrast is −16.57 percentage points. This is consistent with a contribution from firsthand aversive experience to later recipient-linked action. It does not isolate that mechanism: exposure precedes the recorded baseline, condition randomization is unverified, record labels differ, and changes in fear, contextual prediction or correspondence can also matter. The experiment does not observe a value coefficient beginning at zero.

In the released unequal-food groups, preferred-action incidence changes by −7.62 percentage points when that lever offers two pellets. With three pellets, the recorded preferred-response frequency changes by −0.76 points; one slot remains unknown, so this is a lower bound on the complete preferred-incidence change. The main one-pellet group changes by −21.81. These are bounded cost-pattern comparisons, not a pure food-price experiment: the unequal-food groups use equal lever forces, and group histories also differ. Explicit nonresponses in the three-pellet group also remain separately identified. The original data do not license a universal price at which concern disappears.

The random-harm group shows a +1.04-percentage-point change. Its schedules came from the strongest switchers and its shock timing differs from the action-contingent condition. That comparison is descriptive evidence about another arrangement; it is not a randomized, same-dose isolation of contingency. The female harm group also remains in the full results, with substantial nonperformance that makes offered-opportunity and completed-choice outcomes answer different questions.

## What the source audit caught

All 78 actors and 6,240 offered free-choice slots are retained. One slot, actor 70's eleventh trial in the final session, is genuinely empty. It stays unknown. Three separate hypothetical completions—nonperformance, alternative response and preferred response—provide a sensitivity check for that secondary record; none replaces the original.

The trial/summary cross-check produces **39 audit flags**, not 39 contradictory numerical measurements. Thirty-two concern absent precomputed total-nonperformance fields. The observed per-session counts remain available. One concerns a female actor with an entirely nonperformed final session: the workbook's average ignores its text `NaN`, whereas a complete three-session conditional mean is undefined. Six concern three actors in the three-pellet group whose final-session summary uses offered opportunities where the frozen cross-check uses completed responses, with corresponding average differences. All seven percentage/undefined flags lie outside the male primary comparison. The original representations remain unchanged.

The first implementation also rejected a literal `NaN` during the summary audit. The [preserved repair](../../../experiments/recipient-harm-valuation/ANALYSIS-REPAIRS.md) explicitly treats that value as undefined, without altering trial codes or selecting actors. Independent reconstruction and interpretation review are recorded in [the experiment guide](../../../experiments/recipient-harm-valuation/README.md) and [review](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RECIPIENT-VALUATION-REVIEW.md).

## What this supplies to the foundation

The existing [concern model](../../../_process/research/2026-10-05-concern-theory/learning-formal.md) distinguishes learned self-related valence `w`, an evaluative correspondence `g`, effective recipient influence `v=gw`, and estimated intervention efficacy. An actor can learn which lever causes an aversive event while its valuation of that event remains unchanged. The new behavioral history is therefore evidence relevant to consequence-sensitive action, not a direct measurement of an acquired `w`, `g` or ethical root.

The [identification argument](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RECIPIENT-VALUATION-IDENTIFICATION.md) makes the stronger tests explicit. To separate acquiring value from learning how to satisfy an existing value, one must constrain factual/efficacy learning and changes in choice costs. To distinguish tracking the recipient's condition from suppressing an unpleasant cue, a useful comparison separates actual recipient relief from actor sensory relief. The present archive contains no such decisive separation.

An actor-internal affective signal does not by itself make a response selfish: any embodied motivation has an internal causal realization. The discriminating question is what the process tracks when the recipient's condition and the actor's immediate cue experience diverge. Conversely, defining every possible motive as “private reward” makes private-only explanations unfalsifiable. This study holds a specified food offer constant; it does not claim to remove all self-related experience.

For Ren's account, the result adds an externally grounded, temporally changing relation between another organism's consequences and an actor's action. That relation can operate without reflective moral argument. Its presence neither entails that every agent will acquire it nor justifies each resulting choice. The [ethical foundation](ETHICAL-FOUNDATION.md) must still defend why an independently identified recipient condition supplies a reason, and the [recipient-evidence contract](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RECIPIENT-EVIDENCE-DOWNSTREAM-CONTRACT.md) must still connect that reason to rightful, feasible action.

The main account is thus more empirically specified, with a concrete competing-explanations boundary. The next central connection remains **formed recipient understanding → justified evaluative influence → effective, corrigible action**, including recipients without material leverage. A compatible material/learning construction is being developed separately; these animal data do not instantiate its exact state law or settle its normative premises. The [completion requirements](ALIGNMENT-COMPLETION.md) remain unchanged.
