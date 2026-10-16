# Whole-port support, finite continuation and the renewal boundary

7 October 2026. AI-authored continuation of the [formal-unification handoff](../../../history/2026-10-07-handoffs/2026-10-07-formal-unification.md), [contact-formation study](CONTACT-FORMATION-LAW.md) and [connected-entry ledger](UNIFIED-ENTRY.md). This supplies a specific implementation interface to the [first-priority ethical programme](../../../../theories/becoming/history/UNIFIED-ETHICAL-GROUNDING.md#first-priority-universal-normative-grounding): how acquired selection and contact revision continue under the supporting conditions of their actual history. It establishes neither ethical warrant nor a reason to favor persistence. Normative justification, recognition, motivation and implemented preservation remain distinct questions within the same unfolding.

The handoff's native-port rename blocker is obsolete: `NativePortContinuation` is on main. Its accounting and depletion proofs now extend to `FormationClosure.process` and `RevisingPort.revising`. A further result narrows the suggested necessity claim: **formation's native interface draw is unnecessary for conservation and finite continuation**. An explicit rival retains the capacity guard, consumes the actual spare pair, opens the contact, and executes the same acquired selection and inquiry while omitting only that draw. It still satisfies the support law and has no infinite completed execution.

## What is connected

[WholePortContinuation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/WholePortContinuation.lean) adds 51 audited declarations. For a native state, write (H) for `held`, (E) for accumulated `enacted`, (A) for accumulated `arrived`, and (S) for remaining `source`. These are selected coordinates of one port history. They do not describe independent owners or a foundational partition between organization and surroundings.

Every completed native call, recovery, formation and revising encounter preserves

\[
H_t+E_t+A_s=H_s+E_s+A_t,
\qquad E_s\le E_t,\quad A_s\le A_t.
\]

Recovery changes the spare and recovered counts while its native support stage enacts the draw. Formation enacts its draw, consumes a pair and changes the contact. An encounter composes its selected act with its actual five-command inquiry. It retains the reading produced by that inquiry. The conservation proof follows these intermediate states and does not replace them with a newly funded start.

| Result | Established scope |
|---|---|
| `extended_continues`, `extended_trace_continues` | Exact native conservation through every completed extended event and finite trace. |
| `revising_continues`, `revising_trace_continues` | The same conservation for actual encounters and histories retaining acquired readings. |
| `extended_sustain_law`, `revising_sustain_law` | U1 with actual counter increments: (H_t+(E_t-E_s)=H_s+(A_t-A_s)), hence its required inequality. |
| `extended_history_bound`, `revising_history_bound` | U2 applied to actual `SupportTrace` totals; what becomes activity plus the final amount held cannot exceed the initial amount held plus actual arrivals. |
| `extended_history_length`, `revising_history_length` | Number of completed events plus final native potential is at most initial native potential. |
| `extended_cannot_continue_indefinitely`, `revising_cannot_continue_indefinitely` | No infinite sequence of completed extended events or revising encounters under the current finite-source law. |

The native potential is (H+65536S). A successful ten-unit source conversion can bring at most 655,360 held ticks; conversion therefore cannot increase this potential. Every supported stage lowers it. Native calls, recovery and formation each contain such a stage, and encounters contain the actual inquiry even when no formation is selected. These are law-relative bounds, including high-overhead and failed-contact regimes.

No intact-reset premise is needed for these support and depletion results. A broken reset can still make the retained interpretation inaccurate, as the earlier counterexample proves. Accounting correctness does not establish epistemic correctness. Event bounds count completed process edges; repeated stopped calls and idle stuttering are not silently counted as completed activity. Native interrupted outcomes remain governed by `execute_conserves`; the new trace results do not erase those outcomes or add them to the completed-edge relation.

## What the formation draw does and does not explain

The original formation mechanism remains unchanged and retains its native interface draw. Its native potential strictly decreases on each completed formation. That is a sufficient local implementation, not a proof that the draw is necessary.

`undrawnFormation` keeps capacity checking, contact opening and consumption of one spare pair. `undrawnRevising` keeps the same encounter order, acquired decision rule and five-command inquiry. Both the extended rival and the revising rival satisfy U1. A formation in this rival preserves the native potential and enacts zero held ticks, so the original claim of a strictly falling **native** potential on every formation no longer holds.

Nevertheless the rival has a strict termination potential

\[
Q(x)=2\bigl(H(x)+65536S(x)\bigr)+\operatorname{spare}(x).
\]

A native event lowers the first term without changing spare count. Recovery lowers native potential by at least one while adding exactly one pair. Formation without the draw consumes one pair. Consequently every completed extended event strictly lowers (Q); an encounter first preserves or lowers it through its act, then strictly lowers it through its inquiry. `undrawn_history_length`, `undrawn_revising_history_length` and the corresponding no-infinite-execution theorems make this exact.

The factor two is a mathematical ranking device accounting for recovery's one-pair increase. It is neither a physical exchange rate between pairs and held ticks nor an ethical aggregate. This rival preserves the independently specified targets—conservation, pair consumption, actual inquiry and bounded continuation—while removing the disputed formation draw. It therefore defeats necessity **for those targets**, rather than merely toggling an unrelated predicate in a weaker model. It does not derive a physical zero-cost formation law, show which mechanism is empirically realized, or derive the origin of the pair-opening rule. No historical source or original formation theorem is replaced.

## The exact renewal interface and its limits

[PortRenewalBoundary.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/PortRenewalBoundary.lean) adds 20 audited declarations connecting the port and the renewal package at their common U1 accounting interface. `renewal_sustain_law` proves that the actual `channelProcess` resource clause has that form. `contact_keeping_sustain_law` and `contact_changing_sustain_law` prove that the port's two relational cuts inherit U1 without supplying another rate law. `contact_change_has_actual_draw` identifies the draw of the original process's genuinely contact-changing steps; native activity and recovery cannot occupy that side of the cut.

This is **not a derived renewable `ChannelLaw` for the port**. The renewal package additionally specifies tokens that age on every tick, kind-specific spans and rates, formation demands, and actual support by a token that survives the tick. None follows from the resource inequality or the keep/change cut. The port instead represents a persistent contact coordinate, command-dependent access, and a finite source. No map carrying those additional structures and every relevant transition into the renewal model has been proved here. Calling `blocked = false` a token, or assigning an arbitrary span, would add precisely the inputs still needing derivation.

The handoff's proposed test “opening ≥ formation draw” must also preserve units and actual access:

- `source`, `transferred` and `dissipated` are in source units. A packet contains ten units.
- `held`, `enacted`, `arrived` and `draw` are in held ticks. The represented conversion gives 65,536 ticks per source unit, hence 655,360 per successful packet (`successful_packet_units`).
- The interface draw is (16384+\operatorname{live}+\operatorname{workspace}+2) held ticks. A completed probe enacts two such stages. Comparing ten transferred units directly with 16,386 held ticks would mix units.

The checked histories keep formation and conversion actual:

| Executed case | Formation draw | Actual arrival | Consequence |
|---|---:|---:|---|
| Zero live/workspace overhead, one source packet | 16,386 | 655,360 | Formation plus the two probe stages enacts 49,158; that segment is covered. |
| Live overhead 700,000, sufficient initial support/capacity, one source packet | 716,386 | 655,360 | Formation and a successful probe complete; the arrival fails to cover even the formation draw. |
| Zero source, otherwise supported formation | 16,386 | 0 | The contact opens. The subsequent probe enacts its interface stage and stops at the source guard. |

`not_every_formed_contact_covers_formation` formally rejects universal one-packet adequacy using the high-overhead completed history. The module additionally executes **failure → recovery → formation → successful probe** from zero spare pairs and an empty failure record in both overhead regimes. The low-overhead history enacts 98,316 ticks over all six supported stages and arrives 655,360. In the high-overhead history the actual recovered pair forms the contact, yet the same packet yield still falls below the single formation draw. Thus the adverse regime does not rely on supplying an unexplained spare pair.

Even the favorable start obeys the bound `events.length + finalPotential ≤ 755360`. Its source is exhausted after the packet. This says that finite source **together with the represented support demands** bounds continuation; it does not show that source exhaustion is the only possible stopping cause, or that favorable one-packet coverage yields renewable closure. New source access, material formation, aging/support correspondence and timing would need an actual connected law, not a favorable label.

## Premises, revision conditions and next bridge

Still supplied locally: native operation and capacity laws, the conversion scale and finite initial quantities, recovery's relation between the failure record and spare pairs, contact opening by pair consumption, the encounter schedule and its retained-reading mechanism, and Lean's formal background. The absence of Lean axioms does not discharge Ren's stronger no-assumptions objective. A supplied law here is a selected representation of relations within generative activity, not an assertion that law is outside generative reality.

The implementation result would change if another admitted completed event replenished source, produced pairs without any countervailing finite condition, or preserved both native and material potentials indefinitely. The renewal conclusion would change with a proved mapping deriving token formation/aging, spans, support relations and arrivals from the relevant whole process. The present counterexamples must remain admitted unless an independently defended scope condition excludes their high overhead or absent source.

For the normative programme, these proofs establish feasible and infeasible realization regimes for selected revision. They supply no inference from feasible continuation to justified ethical quality, from successful contact to practical reasons, or from a formal invariant to motivation. The next central ethical work remains the warrant of the proposed whole-process appraisal through learning and self-modification. A future renewal implementation study is supporting work only when it states which such preservation requirement it realizes.

## Reproduction

With Lean 4.29.1 on `PATH`, run:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_whole_port_continuation.py
```

If another version is the default, set `LEAN` to the installed 4.29.1 compiler executable. The passing run checked 585 axiom reports, all empty, including 71 new declarations; no compiler warnings occurred. The checker builds the recursively resolved 24-module dependency closure in a fresh temporary directory, reusing no repository `.olean`. It rejects proof placeholders, declared axioms and nonempty axiom reports, and requires an audit for every new definition and theorem. The [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/whole-port-continuation-verification.json) records compiler output and source hashes. Dependency modules' existing audit lists remain scoped to their declared entries; the new declarations' reports audit every dependency they actually use transitively. This run adds formal validation, not empirical validation or normative justification.
