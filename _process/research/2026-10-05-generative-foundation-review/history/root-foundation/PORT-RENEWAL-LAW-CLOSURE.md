# The port's exact finite replenishment and the renewal-law boundary

7 October 2026. AI-authored continuation of [whole-port support](WHOLE-PORT-CONTINUATION.md), the [renewal entry](UNIFIED-ENTRY.md), and the [formal-unification handoff](../../../history/2026-10-07-handoffs/2026-10-07-formal-unification.md). The implementation question supports the [universal normative-grounding programme](../../../../theories/becoming/history/UNIFIED-ETHICAL-GROUNDING.md#session-target-universal-meta-ethics-of-all-intelligence): which actual continuations can realize acquired correction, and which preservation claims fail because their supporting relations have not been established. It proves no ethical appraisal or practical reason to continue.

**Result:** the current port has an exact, productive **finite replenishment regime**, with a sharp encounter horizon. Its persistent contact is not an aging `ChannelLaw` token. The direct contact-only formation/aging correspondence is refuted; a reserve-preserving full inverse of all channel ticks is also refuted at source exhaustion. This settles those proposed identifications for the existing process. It does not prove that every enriched forward representation is impossible. An enriched token interpretation or maintenance process would be a newly specified correspondence target, not the missing last inference of the current contact-only mapping. A richer representation may expose relations already present without changing native dynamics; actual indefinite source replenishment requires a changed source law.

[PortRenewalLawClosure.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/PortRenewalLawClosure.lean) contains the checked statements. The older U1, depletion, actual formation/recovery, high-overhead shortfall and empty-source results are credited rather than reclassified as new results here.

## Actual replenishment through the existing encounter schedule

The following exact equations concern **`RevisingPort`'s existing `Inquiry` schedule `reset, probe, a, a, probe`**. They do not describe the newer adaptive, reset-free [phase inquiry](PHASE-RECOVERED-CONTACT.md). An intact reset is a premise for this schedule's one-successful-packet result, not a claim that every possible inquiry needs a reset. Source bounds for arbitrary native/extended histories below do not require an intact reset.

Let `d = draw(start.native)`, in held ticks. A completed inquiry has three control stages and two probes, each containing an interface stage and a receipt stage. `native_step_amounts` and `inquiry_amounts` derive:

\[
S' + 20 = S,\qquad E' = E + 7d.
\]

No completion is presumed in the constructive direction: `fundedInquiry` builds the five intermediate native states and all five execution proofs from the actual capacity guard, `20 ≤ source`, and `7d ≤ held`. This transient-reserve bound is sufficient; it is not claimed necessary. In particular, a sufficiently early successful transfer can make a smaller starting reserve workable.

For an intact reset, the two outputs are distinct. If the contact is open exactly one packet arrives; if blocked neither arrives. The acquired reading need not trust an uninverted receipt. `inquiry_arrival` follows the accumulated native arrival counter and proves

\[
A' = A + \begin{cases}655360&\text{open contact},\\0&\text{blocked contact}.\end{cases}
\]

An encounter may first form the contact according to its retained reading. Write `f = 1` if that actual selection forms and `f = 0` otherwise. `encounter_source_exact`, `encounter_enacted_exact`, `encounter_arrival_exact`, and `encounter_held_balance` give:

\[
S' + 20 = S,\qquad E' = E+(7+f)d,\qquad
H'+(7+f)d=H+\begin{cases}655360&\text{resulting contact open},\\0&\text{resulting contact blocked}.\end{cases}
\]

Formation itself changes no source or arrival counter. The subsequent inquiry makes the actual transfer. For a resulting open contact, `encounter_replenishes_iff` proves that held support does not fall **if and only if** `(7+f)d ≤ 655360`. It includes every actual interface/receipt stage and the optional formation draw, not merely the cost of opening the contact.

These units are the established native units: ten source units yield 655,360 held ticks, at 65,536 ticks per source unit. There is no comparison of ten source units with a held-tick demand. A favorable local balance consumes twenty source units because the inquiry also probes the other output; that packet fails to arrive. The relation is part of this particular inquiry, not a universal conversion efficiency.

## A sharp finite encounter horizon

`finite_replenishing_encounters` constructs an actual continuing history for every natural number `n`, under these fixed initial conditions:

- the existing reset is intact;
- the contact is open and the retained reading accurately identifies it;
- the native capacity guard holds;
- the initial held reserve is at least `7d`;
- `7d ≤ 655360`;
- the initial source has at least `20n` units.

Every next state is the previous inquiry's reached state, with its retained reading, source, counters and material coordinates. There is no restart or refreshed funding between encounters. The accurate disposition selects no redundant formation. The constructed endpoint satisfies

\[
S_n+20n=S_0,\qquad H_n+n(7d)=H_0+n(655360),\qquad H_0\le H_n.
\]

The converse is stronger in scope. For **every completed revising history**, even one with inaccurate memory, a broken reset, formation, recovery or interspersed native probes,

\[
20\,\operatorname{encounters}(history)+S_{\rm final}\le S_{\rm initial}.
\]

Other probes can consume additional packets. Combining the constructive direction with this bound gives `finite_encounter_horizon`:

\[
\exists\text{ completed history with exactly }n\text{ encounters}
\quad\Longleftrightarrow\quad20n\le S_0
\]

under the productive initial conditions above. This is a sharp **existence and impossibility** result. It is not a guarantee that every chosen command schedule succeeds. Nor does “for every `n`, given sufficient initial source” mean “one finite-source initial state works for every `n`.” `no_unbounded_encounters_from_one_start` explicitly refutes the latter.

The concrete `actual_acquisition_and_replenishment` theorem begins blocked, with no spare pair, no recovered pair, and no retained reading. It supplies 100 source units once initially. The actual first inquiry fails, recovery produces a pair, the acquired selection forms the contact, and the second inquiry succeeds. Three further open encounters then complete. At the endpoint:

| Coordinate | Actual final value |
|---|---:|
| Completed encounters | 5 |
| Remaining source | 0 |
| Held ticks | 2,415,158 |
| Enacted ticks | 606,282 |
| Arrived ticks | 2,621,440 |
| Transferred source units | 40 |
| Dissipated source units | 60 |
| Spare pairs / recovered pairs | 0 / 1 |

The acquired contact and its retained reading remain present. The represented source is exhausted despite growth of held support. Ordinary non-probe activity can still consume that support; another completed encounter cannot occur because it requires two source packets. This distinguishes local replenishment, source exhaustion and total cessation.

## Source opportunity through arbitrary completed histories

The finite resource account is stronger than U1. `native_trace_source_bound`, `extended_trace_source_bound`, and `revising_trace_source_bound` prove:

\[
A_{\rm final}+65536S_{\rm final}
\le A_{\rm initial}+65536S_{\rm initial}.
\]

The extended result follows every actual native, recovery and formation edge. It applies to an adaptive inquiry when represented by its actual extended trace, without attributing the old schedule's seven-draw or twenty-unit encounter count to it. The earlier strict native-potential theorem additionally excludes an infinite sequence of completed extended/revising events from any current state.

These are bounds on completed edges. The native executor separately retains actual intermediate depletion and arrivals when a call stops. The present proofs neither count stopped calls as completed encounters nor roll back their partial execution.

## The exact proposed `ChannelLaw` correspondence

The renewal package's [channel law](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/RenewalAccounting.lean) has more structure than a support inequality: tokens with kinds and remaining spans, aging on each tick, kind-specific demand/rate, births of full-span tokens, and support for each birth from a token surviving that tick. Its rate is a per-tick **upper allowance** in a reserve inequality, not a claim that every permitted amount actually arrives.

`channel_step_iff_actual_requirements` makes the forward-extraction obligation exact. Suppose `view` retains the actual native `held` amount as the channel reserve, and an actual completed revising step has occurred. Then it maps to a channel step with proposed birth list `births` if and only if all three conditions hold:

1. `view(next).tokens = aged(view(start).tokens) ++ formed(law, births)`.
2. `formation(law, births) + actual_arrival ≤ actual_enacted + opened(law.rate, view(start).tokens)`.
3. Every proposed birth has an actual listed support token after aging, with the specified edge.

The second condition is derived by substituting the port's exact conservation equation and cancelling equal terms. It prevents changing units or forgetting the support stages. `channel_forward_of_actual_cover` gives a sufficient version using separately established demand and arrival bounds. **Neither theorem presents the other clauses as derived.** They identify the precise information an enriched representation must establish.

The current contact identification fails for independently specified reasons:

- **First formation:** a blocked contact can actually be opened by a supported formation consuming a spare pair. A map representing blockage by an empty token list cannot map that event to a nonempty channel birth, because `ChannelLaw` requires an earlier surviving support token. `no_contact_only_formation_map` proves this for every choice of kind, edge, span, rate and demand. Recovery/formation is real; the insufficient representation omitted its supporting organization. Adding an identified support token for material/organization would require its own actual aging, maintenance and support correspondence.
- **Aging:** native read activity preserves the contact. A nonempty live token list determined solely by that coordinate therefore stays unchanged. Channel aging cannot leave a live finite token list unchanged without births. `live_tokens_do_not_stand_still` and `no_contact_invariant_live_map` prove this conflict. A lifetime chosen from a future trace length or a remaining resource budget is an added description, not a derived age of the contact.
- **Full inverse of permitted ticks:** `ChannelLaw` permits a tick with aging, no birth and unchanged reserve. At an actual port state with no source, every completed revising event strictly lowers held support. Thus a reserve-faithful inverse mapping cannot realize that permitted tick as one actual completed event (`no_exact_channel_tick_lift_at_exhaustion`). This rules out the specified exact full transition identification. It does not invalidate a forward overapproximation which deliberately includes extra channel transitions, a differently timed map, or an enrichment of the process.

Finite source alone would **not** refute every forward abstraction: an upper rate bound may overestimate an actual finite supply. Conversely, a forward abstraction's permission for indefinite renewal would not establish an actual infinite native execution. The distinction between one-way representation, exact transition correspondence and actual execution must remain explicit.

## Necessary change of target and remaining premises

For the named direct contact-to-channel obligation, there is now a checked negative answer plus an exact positive finite realization theorem. It should no longer be described simply as an unproved inference from U1. A full renewal model of a broader process would need to supply and connect:

- a meaningful event clock and actual token formation/aging or maintenance, explaining which continuing organization the tokens represent;
- supporting organization surviving each formation, including the actual material recovery relation where relevant;
- rates and demands in common units over those same events, preserving the actual source and all intervening stages;
- if indefinite completed encounters are claimed, a changed source-support law that defeats the present twenty-unit consumption and finite-source bound through actual represented activity. Replenishment cannot be inferred from contact opening, accurate memory or favorable held balance alone.

The first three items may be met by exposing and proving already represented relations, if an adequate interpretation exists, or may require richer maintenance dynamics. They do not by themselves require a physical change. Indefinite replenishment requires changing the present source law. This study does not choose an external provider or insert an unbounded replenishment oracle. A locally supplied law is not thereby external to generative reality. Its actual connection to the broader process still needs explanation. The admitted high-overhead and empty-source regimes remain genuine countercases to universal adequacy.

Native execution, conversion scale, capacity/draw law, failure-to-pair recovery, pair-consuming formation, the encounter schedule and its decision rule remain the model's supplied mechanisms or credited earlier derivations. The proof uses Lean's audited logical dependencies. No absence of custom axioms establishes Ren's stronger no-assumptions goal. Feasible replenishment and finite implementation bounds neither justify ethical quality nor infer reasons, motivation or warranted preservation through self-modification.

## Verification

Run the [fresh checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_port_renewal_law.py), setting `LEAN` to the installed Lean 4.29.1 executable if another compiler is the default. It recursively builds the dependency closure in a new temporary directory, reuses no repository `.olean`, audits every new definition/theorem, rejects proof holes, custom axioms and `native_decide`, and retains raw compiler output plus source/checker hashes in the [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/port-renewal-law-verification.json).

The fresh run passed 25 modules and 626 audits, including all 41 new declarations. Of the new declarations, 21 have empty reports and 20 use only `propext` and `Quot.sound`; none uses `Classical.choice`. The first-formation and contact-aging obstructions, exact native arrival, arbitrary-history source bounds and the concrete acquisition/replenishment history have empty axiom reports. These dependency classes must not be merged into a blanket claim that every new theorem has an empty report. This is formal model validation, with no new empirical evidence or ethical justification claimed.
