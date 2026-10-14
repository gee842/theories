# Migration map: closure-verdict-meets-axiom

Old record sha256 `6c316b3c54c5f169ecaf48e0194894effb31cde6554627740ae4f0b0967d0cc3`; snapshot `_process/architecture/history/6c316b3c54c5f169/closure-verdict-meets-axiom.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses and quotations): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence (the labels align in both languages).

Each law was read against its declarations in `Becoming/Interdependence.lean` (with `Becoming/Significance.lean` for `Unrestricted`, `bounded`, `Web.Retains` and `Web.Adds`, `Becoming/Admission.lean` for `Web.Admits`, `Web.Includes` and `Flow.WithheldLevels`, and `Becoming/Regions.lean` for `Clearing.clearerPart`). The laws are the old claim's sentences with the declaration names moved into `declarations`. Law 3 adds why the covering condition holds in Overshoot (`Overshoot.closure_whole`: either formation's feeding closure is the whole), which C5 left implicit. No law states more than its declaration.

Two standard boundaries are not cited. no-ethical-premise is not cited because the comparison theorems take the axiom Unrestricted as a hypothesis (hypotheses[0]); that the theorems use no Lean axiom stays in the validation scope. no-evaluation is not cited because the old text did not state that the record contains no ethical predicate.

| Old text | Type | New place |
|---|---|---|
| T0 “Where the verdict within the closure meets the axiom” | title | title (unchanged) |
| S0–S2 “Significance bounded by the whole is the axiom. …; in the clearer's web the two part.” | statement | statement (unchanged) |
| C0 “Significance bounded by the whole (each standpoint's region the whole) is the axiom Unrestricted (bounded_whole).” | law | law 1 (name → declarations) |
| C1–C3 “Given regions region, a standpoint p and level paths l and l', suppose … (covers). Then … (Web.retains_bounded_iff_includes); under the axiom … (Web.retains_bounded_iff_retains), so the two verdicts agree.” | law | law 2 (names → declarations; the variable name “region” and the label “covers” dropped, hypotheses[1] keeps “covers”) |
| C4–C5 “Where a formation p's feeding closure is the whole, … (Flow.within_closure_iff_retains); in Overshoot this holds from either standpoint (Overshoot.within_closure_iff_retains).” | law | law 3 (names → declarations; Overshoot.closure_whole added, see above) |
| C6–C9 “In Clearing the two part: let l be the levels with the clearer's part withheld (Flow.WithheldLevels); … (Clearing.within_closure_yet_loses).” | law (witness) | law 4 (names → declarations) |
| C10 “No Lean axiom is used;” | evidence | validation_scope (“have empty axiom reports, … not a Lean axiom”) |
| C11 “the axiom appears only as a hypothesis of the comparison theorems.” | premise (duplicate of H0) | hypotheses[0] |
| L0 “The axiom appears only as a hypothesis of the comparisons and is not proved;” | premise (duplicate of H0) | hypotheses[0] |
| L1 “the covering condition is sufficient, not necessary;” | converse | does_not_show[0] (“for the two verdicts to agree”), witness Web.retains_bounded_iff_retains |
| L2 “only formations admitted are compared, step by step;” | scope | does_not_show[1] |
| L3 “comparisons by withheld levels keep the rest of the exchange fixed;” | premise (duplicate of H2) | hypotheses[2] |
| L4 “route (b) claims no warrant;” | non-implication | does_not_show[2] |
| L5 “selection between wholes is not modelled;” | scope | does_not_show[3] |
| L6 ““a center whose represented boundary is the whole” is a reading, and how a center represents is not modelled;” | scope + reading | does_not_show[4]; correspondence (R9 gives the reading) |
| L7 “the readings and names are the AI's, pending Ren;” | reading | standard_boundaries: names-provisional; correspondence (“The author's reading (an AI argument, pending Ren)” and the names sentence); hypotheses[0] (the axiom reading) |
| L8 “G0 follows from Part II's axiom, and since Ren folded it on 11 October 2026 it is no longer an axiom (P51).” | scope | does_not_show[5] (kind scope; new item: “G0 follows from Part II's axiom and, since Ren folded it, is no longer an axiom.”; placed among the hypotheses by the migration and moved to a scope item at landing, since it is not a hypothesis of the theorems); the date and P51 stay in history (the P51 entry, with Ren's words) and the snapshot |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 30 theorems of Becoming.Interdependence all have empty axiom reports;” | evidence | validation_scope; the count stays in the receipt and the snapshot |
| V1 “the same receipt covers the package's 75 modules … and 22 inherited modules …” | evidence (counts) | receipt + snapshot |
| V2 “periphery receipt 20261013T095049.338744Z passed.” | evidence | receipt + history + snapshot (every cited module is a core module) |
| V3 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (“core purity verified”); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V4 “The axiom Unrestricted is a hypothesis of the comparison theorems, not a Lean axiom.” | evidence | validation_scope |
| V5 “The author's counterreview is in §56 of the integration note;” | evidence | validation_scope (“in the integration note”); §56 stays in history (the entry that added the record) and the snapshot |
| V6 “not yet independently reviewed.” | evidence | validation_scope |
| R0 Route (b) and Ren's two quotations | Ren's words | correspondence (verbatim) |
| R1 “The author's reading (an AI argument, pending Ren): the feeding closure reads “what it actually depends on”.” | reading | correspondence (unchanged) |
| R2 “P40 also read it as Ren's “the system that one is in”, …;” | reading | correspondence (“P40 also read it” → “It was also read”; zh “P40 也把它读作” → “它也曾被读作”); P40 → history + snapshot |
| R3 “P42 withdraws that reading: …” | reading | correspondence (“P42 withdraws that reading” → “that reading is withdrawn”; zh “这一读法由 P42 撤回” → “这一读法已撤回”); P42 → history + snapshot |
| R4 “The names (FedClosed, WithinFeeding, Overshoot and others) are the AI's, chosen by Ren's naming standard.” | names | correspondence (unchanged); standard_boundaries: names-provisional |
| R5–R6 Ren's levels and “there could be the whole realizes itself …” | Ren's words | correspondence (verbatim) |
| R7 “The author's reading (an AI argument, pending Ren): route (b) reaches the self and what it depends on (P42 correction: it said “the self and the system one is in”), and the whole only where …” | reading | correspondence (“P42 correction: it said” → “corrected from”; zh “P42 更正：原写” → “更正自”); P42 → history + snapshot |
| R8–R9 | reading | correspondence (unchanged) |
| N0–N1 “Ren's judgments: whether route (b), reaching the self and what it depends on, suffices or Part II's axiom is adopted; how the whole realizing itself is read (a represented boundary that is the whole, bounded_whole).” | next step | next_delta (“Ren judges whether …, and how the whole realizing itself is read …”) |
| N2 “P42 derives the covering condition from the dynamics wherever significance covers what the part has reached before each step (comparison-within-reach);” | completed connection | related entry comparison-within-reach (unchanged; it says the covering condition follows from the dynamics); P42 → history + snapshot |
| N3 “route (b) is the same presupposition at narrow scope (presupposition-scopes);” | completed connection | related entry presupposition-scopes (unchanged; it says route (b) and the axiom are one presupposition at narrow and at wide scope) |
| N4 “closures step by step remain open.” | next step | next_delta (“Give the closures step by step.”) |
| H0–H3 | premises | hypotheses[0]–[3] (unchanged) |
| X0 | counterexample | counterexamples[0] (unchanged) |

Remaining lint findings: the correspondence is over its length guide (en 1765/1200, zh 1125/500). It quotes verbatim the route (b) wording Ren quoted, Ren's choice, Ren's levels and Ren's passage on the whole realizing itself (about 740 characters each time), without which it is within the guide; the remaining sentences are attributions of AI readings. They are kept rather than moved out of the record.
