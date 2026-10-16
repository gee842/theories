# Migration map: unceasing-generation-needs-renewal

Old record sha256 `5b1ab679ee0e6c3a00664622a3fad6904d248f80171f212d5a5a87f547dfc125`; snapshot `_process/architecture/history/5b1ab679ee0e6c3a/unceasing-generation-needs-renewal.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence (zh R4–R5 hold en R4, so later zh correspondence labels run one ahead).

Each law was read against its declarations in `Becoming/Generation.lean` and `Becoming/Flow.lean`; none states more than the declaration (`depletes_iff` is the “exactly” of law 2, `renewing_recurs` the recurring renewers of law 4).

| Old text | Type | New place |
|---|---|---|
| T0 “Unceasing generation needs renewal” | title | title (unchanged) |
| S0–S1 “Where arising depletes finitely many conditions, unceasing generation needs renewal to recur; renewal does not imply generation.” | statement | statement (unchanged) |
| C0–C1 “On a web of dependence, a formation arises across a step when …; generation is unceasing when …” | definitions | law 1 (unchanged) |
| C2 “Arising, becoming active, is the formal carrier of one reading of the second 生 of 生生 (the author's reading).” | reading | law 1 (unchanged); the correspondence's repetition of it (R2) is dropped there |
| C3–C4 “An event depletes a finite family of conditions when …; this says exactly that some condition of the family changes at each step of the event, whatever its relation to the event.” | definition + law | law 2 (unchanged) |
| C5 “If from some step none of them rises, events depleting the family do not occur at arbitrarily late steps.” | law | law 2 (unchanged) |
| C6–C7 “Hence, if arising depletes the family, unceasing generation makes some condition of the family rise (a net rise) at arbitrarily late steps; and if every rise is made by …, renewing activity recurs.” | law | law 3 (unchanged) |
| C8–C10 “Balanced flows give a form that needs no net rise: …; in this form arising works only through the uptake it brings.” | law | law 4 (unchanged) |
| C11 “This form sees replenishment concurrent with drawing.” | scope | does_not_show[5] (“concurrent replenishment is visible only in the flow form”, the same sentence as L6), witness Expansion.undepleted |
| C12 “A formation lowering some condition of the family at each active step is not active at arbitrarily late steps … : substitution defers the end and does not escape it.” | law | law 5 (unchanged) |
| C13–C14 “If a quantity never rises and every arising lowers it (dissipation), generation is not unceasing; a closed cycle whose total stays constant sustains unceasing generation.” | law (with witness) | law 6 (unchanged) |
| C15 “Renewal can recur with nothing arising (a tide the moon renews), so under these premises unceasing generation is strictly stronger than recurring renewal.” | law (witness) | law 7 (unchanged); counterexamples[0] states it too |
| C16–C17 “Formations can arise one after another while drawing an unrenewed condition, consume it, and arising does not recur; a consumer can move from one source to another and end.” | law (witnesses) | law 8 (unchanged) |
| C18–C19 “A formation arising again and again on a condition the source renews meets every premise and generation is unceasing; the stepwise working candidate withholds each of its arisings, and the reading over cycles of two includes it.” | law (witness) | law 9 (unchanged) |
| C20 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (the hypotheses hold no ethical premise; the receipts report empty axioms for Becoming.Generation and the flow form) |
| L0 “Contains no ethical predicate and yields no “unceasing is better” or any ranking;” | standard boundary + non-implication | standard_boundaries: no-evaluation; does_not_show[0] |
| L1 “does not state “more”, diversity or complexity;” | scope | does_not_show[1] (hypotheses[5] says the same) |
| L2 “the generation component is not added to any reading of living;” | non-implication | does_not_show[1] |
| L3 “the depletion premise asks only that some condition of the family change (depletes_iff) and does not screen out arisings made by naming (TideFlip);” | scope | does_not_show[2], witness TideFlip.naming_meets_premises |
| L4 “in the flow form of the two-kind reading arising works only through uptake (Steady), while the arising of an embodied relatum is itself replenishment (generation-is-replenishment);” | scope | does_not_show[3], witness Steady.steady |
| L5 “Unceasing depends on identity across steps (identity-across-steps): …” | scope | does_not_show[4] (unchanged) |
| L6 “Rises is a net rise, and concurrent replenishment is visible only in the flow form;” | scope | does_not_show[5] |
| L7 “the conclusion of RenewedBy is only as strong as the renews the application supplies;” | premise (duplicate of H2) | hypotheses[2] (“the conclusion is only as strong as it”) |
| L8 “dissipation is a physical premise (for the arisings of embodied members of a closed family it follows from balance, dissipation on flows and embodiment; see generation-is-replenishment), and the total presupposes commensurable units;” | premise (duplicate of H4) | hypotheses[4] (physical premise, commensurable units); the parenthesis is the related entry generation-is-replenishment (“the premise of this result's dissipation_generation_not_recurring follows, for the arisings of embodied members of a closed family, from balance, dissipation and embodiment”) |
| L9 “families of conditions are finite;” | premise (duplicate of H0) | hypotheses[0] |
| L10 “the witnesses are minimal;” | scope | does_not_show[6] |
| L11 “the depletion premise, ArisesTaking, RenewedBy and dissipation are application duties;” | premise (duplicate) | hypotheses[1]–[4] (correspondence, supplied and physical premises) and the correspondence's last empirical sentence (R9) |
| L12 “the new names are the reviewer's suggestions, and the final choice is Ren's.” | reading | correspondence (last sentence; “, and” → “;”) |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): all 30 theorems of Becoming.Generation and the flow-form theorems of Becoming.Flow have empty axiom reports;” | evidence | validation_scope (with the binding receipt of the current Becoming.Generation bytes, 20261014T091930.724493Z, from proof_bindings); the count (30) stays in the receipt and the snapshot |
| V1 “the same receipt covers the package's 75 modules … 4518 theorems/6370 declaration audits, and 22 inherited modules …” | evidence (counts) | receipt + snapshot |
| V2 “The author's counterreview is in §13 of the integration note;” | evidence | validation_scope (“in the integration note”; §13 stays in the snapshot) |
| V3 “a separate agent (Claude Opus 5.5, not an author) reviewed it independently (BECOMING-P9B-P10-P11-REVIEW.md), and its corrections are handled in §15;” | evidence (review) | validation_scope (“the fourth independent review … is handled there”; counterexamples[9] names it the fourth); reviewer and §15 stay under sources and in the snapshot |
| V4 “a fifth independent review (BECOMING-P11B-P12-REVIEW.md) reviewed those corrections and added that the flow form uses only uptake and that naming can make the arisings, see §19;” | evidence (review) | validation_scope; §19 → snapshot |
| V5 “the sixth independent review (BECOMING-P13-P14-P12B-REVIEW.md) accepted these corrections, see §22.” | evidence (review) | validation_scope; §22 → snapshot |
| V6 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (“core purity verified”); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V7 “This record's local laws (P57–P61) are in the same receipt, with empty axiom reports.” | evidence + round labels | validation_scope (the flow-form theorems include them); P57–P61 → history (existing entries) + snapshot |
| R0 “Ren's words are “生生不息 - 一种整体的，不断创造更多生的方向” (a whole direction of unceasingly creating more 生).” | Ren's words | correspondence (verbatim) |
| R1 “This result formalizes only “unceasingly … 生” and states it on the whole's continuation, which is the author's reading;” | correspondence | correspondence (unchanged) |
| R2 “arising is the formal carrier of one reading of the second 生, whose scope is left to Ren.” | correspondence (first half duplicate of C2) | correspondence (“the scope of the second 生 is left to Ren”); the first half is law 1 |
| R3–R7 | correspondence | correspondence (unchanged) |
| R8 “without dissipation a closed cycle can be unceasing (Recycle).” | law (duplicate) | law 6 (“a closed cycle whose total stays constant sustains unceasing generation”) and counterexamples[3] (Recycle.closed_unceasing) |
| R9 “Whether actual unfoldings meet the depletion premise, RenewedBy, the flow correspondence and dissipation is an empirical question.” | correspondence | correspondence (unchanged) |
| N0 “The exact restatement for every world is this record's Flow.uptake_needs_replenishment_from, replenishment_recurs_from, renewing_recurs_from (P57), the local condition inside the law: balance on the family only from some step on;” | local laws appended to next | law 10; P57 → history (existing entry) |
| N1 “Flow.uptake_needs_replenishment, replenishment_recurs, renewing_recurs are their corollaries;” | corollaries | law 10 (“the forms with balance everywhere are their corollaries”) |
| N2 “one reading of “more” (the number of takers) is stated in more-needs-renewers, and dissipation on flows in no-finite-part-bears-taking;” | completed connection (not a next step) | related (more-needs-renewers, whose detail states the reading) and correspondence (no-finite-part-bears-taking, in the author's interpretation) |
| N3 “rising possibility, diversity and complexity, connecting the generation component to Frame.Novel and to the “new living content” of universal_reason, and whether a generation component can enter a reading of living without repeating what “no harm” gives up remain open;” | next step | next_delta (stated positively: “State …; connect …; test whether …”) |
| N4 “the scope of the second 生 and whether arising on a consumed condition is generation are Ren's to say.” | next step | next_delta (unchanged) |
| H0 | premise | hypotheses[0] (unchanged) |
| H1 “The depletion premise (before P11b, the payment premise): …” | premise | hypotheses[1] (the old-name note “(before P11b, the payment premise)” dropped: a round label and a word of exchange; it stays in history and the snapshot) |
| H2–H5 | premises | hypotheses[2]–[5] (unchanged) |
| X0–X8 | counterexamples | counterexamples[0]–[8] (unchanged) |
| X9 “Fourth independent review: every P10 declaration is accepted …; Paid did not involve the arising formation, …, and the payment vocabulary conflicted with Ren's corrections (corrected, integration note §15).” | counterexample (review summary) | counterexamples[9] (“every P10 declaration” → “every declaration under review”; “Paid” → “the definition now named Depletes”; “the payment vocabulary” → “the vocabulary of exchange”; “(corrected, integration note §15)” → “(corrected in the integration note)”) |
| X10 “Fifth independent review: every P11b declaration is accepted …; …, and rebuttal 2 of §15.4 was stronger than the theorem; … (corrected, integration note §19).” | counterexample (review summary) | counterexamples[10] (“every P11b declaration” → “every declaration under review”; “rebuttal 2 of §15.4” → “a rebuttal in the integration note”; “(corrected, integration note §19)” → “(corrected in the integration note)”) |
