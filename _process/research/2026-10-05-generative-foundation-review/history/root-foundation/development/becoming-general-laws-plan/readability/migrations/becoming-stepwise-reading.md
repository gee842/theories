# Migration map: becoming-stepwise-reading

Old record sha256 `84b7edf8bfc55cd3ed0da3775c61c708d427db0211ec391b9c1f82998d82c691`; snapshot `_process/architecture/history/84b7edf8bfc55cd3/becoming-stepwise-reading.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence (zh C9–C10 hold en C9, so the later zh labels run one ahead; zh L1 holds en L1–L2).

Each law was read against its declarations in `Becoming/Dependence.lean` and `Becoming/Metaethics.lean`. One law is written narrower than the old text, to match the theorem: `Web.significant_iff_of_common` (through `Valuation.significant_iff`) takes a standpoint `p₀` and a living event `alive₀` as hypotheses, which C15 left out; law 7 now says “given a standpoint and a living event”.

| Old text | Type | New place |
|---|---|---|
| T0 “The stepwise reading” | title | title (unchanged) |
| S0–S1 “The stepwise reading classifies events within renewal … it reads living as active and not undermining.” | statement | statement (unchanged) |
| C0 “On a web of dependence, an event (formation, step) is within renewal when …” | definition | law 1 |
| C1 “Whole-run renewal includes every active step;” | law | law 1 |
| C2 “a step breaking a dependence on a condition the event participates in is not within renewal;” | law | law 1 |
| C3 “a formation can be within renewal at each of its own active steps without renewing in the run.” | law (witness) | law 1 (Dip.renewing_at_each_step_not_in_run among its declarations); counterexamples[0] states it too |
| C4 “A formation's relation to a condition undermines at a step when …” | definition | law 2 |
| C5 “drawing at a step that breaks a dependence (breaking) is a case of undermining, and an event within renewal neither undermines nor breaks.” | law | law 2 |
| C6 “Taking “active and not undermining” as `living` … the broken formation is not within renewal at the breaking step but does not undermine, so it is included;” | definition + law | law 3 |
| C7 “drawing after a loss breaks nothing further yet undermines, while with the same first step and nothing further taken (action 0) the condition returns;” | law (witness) | law 3 |
| C8 “a requirement never met at its own need while it held makes no event undermine, also when the need falls;” | law (witnesses) | law 4 |
| C9 “falling short only of a need grown beyond anything met does not undermine, while after a need has grown a draw … undermines without breaking;” | law (witnesses) | law 4 |
| C10 “and a dependence that lapses for a step starts a new tenure.” | law (witness) | law 4 |
| C11 “Undermining reads co-participation in an unrestored shortfall, not what a draw does: …” | law (witness) | law 5 (unchanged) |
| C12 “The whole-run reading and this one differ in both directions: a formation drawing within renewal at first and beyond it later is consuming on the whole-run reading while its first event is included stepwise;” | law (witness) | law 6 (“is consuming on … while its first event is included” → “consumes on …, its first event included”) |
| C13 “a formation that draws beyond renewal once while the condition later returns is not consuming on the whole-run reading while its event at the breaking step is not included stepwise;” | law (witness) | law 6 (“is not consuming on the whole-run reading” → “does not consume on that reading”) |
| C14 “both include the broken formation's event at the breaking step.” | law | law 6 |
| C15 “A condition in which every living event participates makes the whole connected, so G0 is exactly a seed with N_rel and N_std;” | law | law 7, with “given a standpoint and a living event” written in (judgment call, see above and history) |
| C16 “an event drawing at a breaking step is not living and is related to every event of the broken formation …, so under N_rel a standpoint valuing it holds those living events significant.” | law | law 7 |
| C17–C18 “A relation-level reading takes (formation, condition, step) as claims … one event can have a living and an undermining relation.” | definition + law | law 8 (unchanged) |
| C19 “With constant dependence the whole-run and stepwise readings have the same `related`.” | law | law 9 (unchanged) |
| L0 “Proves none of S0, N, A, C, L or J and binds no position rejecting them.” | non-implication | does_not_show[0] |
| L1–L2 “The whole-run, stepwise and relation-level readings are disclosed reading choices; none is proved to be the right reading of 生生.” | non-implication | does_not_show[1] |
| L3 “The readings are relative to a run and include no component of further generation;” | scope | does_not_show[2] |
| L4 “tenure, undermining and the stepwise living depend on identity across steps (identity-across-steps): …” | scope | does_not_show[3] |
| L5 “no causal or difference-making attribution is made, and undermining involves neither the amount nor the effect of a draw;” | non-implication | does_not_show[4] |
| L6 “the correspondence discipline for conditions is in condition-correspondence-discipline.” | cross-reference | related (condition-correspondence-discipline, whose detail states the discipline) and hypotheses[2] (“depends on a correspondence discipline for conditions and participation”) |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the stepwise theorems of Becoming.Dependence and the 9 theorems of the “The stepwise reading” section of Becoming.Metaethics all have empty axiom reports.” | evidence | validation_scope (with the binding receipt of the current bytes, 20261014T091930.724493Z, from proof_bindings); the count (9) stays in the receipt and the snapshot |
| V1 “The control that the stepwise reading is connected by a common condition and has a living event is not counted;” | evidence (counts) | snapshot |
| V2 “the same receipt covers the package's 75 modules … 4518 theorems/6370 declaration audits, and 22 inherited modules …” | evidence (counts) | receipt + snapshot |
| V3 “The author's counterreview is in §§4 and 6 of the integration note;” | evidence | validation_scope (“in the integration note”; §§4, 6 stay in the snapshot) |
| V4 “a separate agent (Claude Opus 5.5, not an author) reviewed it independently (BECOMING-RENEWAL-READING-REVIEW.md), and its corrections are handled in §7;” | evidence (review) | validation_scope (“the first's corrections are handled”); reviewer, file and §7 stay under sources and in the snapshot |
| V5 “a second independent review (BECOMING-P7-REVIEW.md) corrected the definition of undermining, see §11;” | evidence (review) | validation_scope (“the second to fourth brought undermining to its minimum form”); §11 → snapshot |
| V6 “a third (BECOMING-P8-P9-P7B-REVIEW.md) corrected it again to compare the need at that step, see §12;” | evidence (review) | validation_scope (same clause); counterexamples[9] and [12] keep the detail; §12 → snapshot |
| V7 “a fourth (BECOMING-P9B-P10-P11-REVIEW.md) changed it to the minimum form, see §15;” | evidence (review) | validation_scope (same clause); §15 → snapshot |
| V8 “a fifth (BECOMING-P11B-P12-REVIEW.md) asked that the reading's dependence on identity across steps be noted, see §19;” | evidence (review) | validation_scope; §19 → snapshot |
| V9 “a sixth (BECOMING-P13-P14-P12B-REVIEW.md) accepted that note, see §22.” | evidence (review) | validation_scope; §22 → snapshot |
| V10 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (“core purity verified”); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| R0–R3 | correspondence | correspondence (unchanged) |
| R4 “Stepwise living had three candidates in turn … with what it gives up (integration note §§7, 11, 12).” | correspondence | correspondence (“integration note §§7, 11, 12” → “integration note”; the section numbers stay in the snapshot, so the field cites one section, below the round-accretion limit) |
| R5 “Which reading, or combination, is the reading of 生生 is a choice within Ren's direction … (integration note §8.5).” | correspondence | correspondence (unchanged) |
| N0 “Ren's choice of the reading of 生生, or a combination (material in integration note §§8.5, 11, 12), and whether the verdict on winning by consumption covers events before the threshold;” | next step | next_delta (“material in integration note §§8.5, 11, 12” → “see the integration note”) |
| N1 “how a tenure continues through bounded absence (dormancy, migration);” | next step | next_delta (“tenure through bounded absence (dormancy, migration)”) |
| N2 “a web of dependence with amounts and renewal rates;” | next step | next_delta (“webs with amounts and renewal rates”) |
| N3–N4 | next step | next_delta (unchanged) |
| N5 “a component of further generation in living.” | next step | next_delta (“further generation in living”) |
| H0–H3 | premises | hypotheses[0]–[3] (unchanged) |
| X0–X4, X6, X7, X11 | counterexamples | counterexamples (unchanged) |
| X5 “… Under the corrected definition (Web.MetSince, from P11b the minimum form Web.MetAbove) …” | counterexample | counterexamples[5] (“from P11b the minimum form” → “later the minimum form”) |
| X8 “Second independent review: the mathematics of P7 is accepted; … the §8.5 table … (corrected, integration note §11).” | counterexample (review summary) | counterexamples[8] (the rewrite of joint-difference-making: “of P7” → “under review”; “the §8.5 table” → “the integration note's comparison table”; “integration note §11” dropped) |
| X9 “The P7b definition compared the present need with an earlier level: … Under the P9b definition (…) …” | counterexample | counterexamples[9] (“The P7b definition” → “MetSince as first corrected”; “the P9b definition” → “the definition as corrected again”) |
| X10 “… The P11b minimum form keeps this choice …” | counterexample | counterexamples[10] (“The P11b minimum form” → “The minimum form (MetAbove)”) |
| X12 “Third independent review: every P8, P9 and P7b declaration is accepted …; … (corrected, integration note §12).” | counterexample (review summary) | counterexamples[12] (the rewrite of joint-difference-making and ranking-under-readings) |
| X13 “A grown need erased the met history (fourth independent review H1): under the P9b definition, … Under the P11b minimum form … the three P9b witnesses keep their conclusions.” | counterexample | counterexamples[13] (“the P9b definition” → “MetSince as corrected again”; “the P11b minimum form” → “the minimum form”; “the three P9b witnesses” → “the three witnesses made for that definition (FallingNeed, RisingNeed, Gap)”, as the dependence-dynamics receipt note lists them) |
| X14 “Fourth independent review: every P9b, P10 and P11 declaration is accepted …; … the prose on Paid, the hierarchy, givers and dissipation overclaimed (corrected, integration note §15).” | counterexample (review summary) | counterexamples[14] (“every P9b, P10 and P11 declaration” → “every declaration under review”; “Paid” → “the definition now named Depletes”, its current name in the spine; “integration note §15” → “in the integration note”) |
