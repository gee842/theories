# Migration map: comparison-within-reach

Old record sha256 `19132902842e1dd68c2309ac7226005077490399c9792b739f82eb03c505db06`; snapshot `_process/architecture/history/19132902842e1dd6/comparison-within-reach.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses and quotations): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence (zh C2–C3 hold en C2, so zh C4–C13 are en C3–C12; zh C14 holds en C13–C14).

Each law was read against its declarations in `Becoming/Feedback.lean` (with `Becoming/Significance.lean` for `Web.Retains`, `Web.Adds`, `Web.retains_iff_includes`, `Web.adds_iff_exceeds` and `bounded`, `Becoming/Admission.lean` for `Web.Includes` and `Web.Exceeds`, and `Becoming/Regions.lean` for `Clearing.clearerPart`). Three wordings were made exact:

- C3–C4 said “Where significance is decidable, adding is exceeding” and “for every significance, exceeding gives adding up to double negation”. Both theorems (`Flow.Balances.adds_iff_exceeds_of_decidable`, `Flow.Balances.not_not_adds_of_exceeds`) ask the significance to cover what the part has reached before each step, as in C2; law 3 says “for such a covering significance” and “for every covering significance”. L1 is read the same way in does_not_show[1].
- C9–C10 said significance bounded by each system, or by each reach closure, judges the clearer's part “to lose the dweller”. `Clearing.system_counts_dweller` and `Clearing.reach_counts_dweller` state that the levels without the part add a continuation with significance (`Web.Adds`) and that the part does not retain; their proofs exhibit the dweller at step 2. Law 6 states the added continuation and names the dweller in parentheses. C17's “the part loses the deer” is treated the same way in law 11 (`Trophic.mixed_part` states `¬ web.Retains sig .far web.level l`; its proof exhibits the deer at step 1).
- C12 said “the levels with it include those without”; `Margin.reach_without_misjudgment` states inclusion both ways, and law 8 says so (“include each other … retains both ways”).

No law states more than its declaration.

| Old text | Type | New place |
|---|---|---|
| T0 “Comparison within reach” | title | title (unchanged) |
| S0–S1 “The comparison is decided within what the part reaches: …” | statement | statement (unchanged) |
| C0 “Let the flow balance and l be the levels with a part withheld.” | framing | law 1 (unchanged); hypotheses[0]–[1] state the premises |
| C1 “Two significances that agree, from standpoint p, … (retaining and not adding carry over …: Flow.Balances.retains_transfer, not_adds_transfer) make the same four comparisons … (Flow.Balances.comparison_local).” | law | law 1 (names → declarations; the parenthesis became the clause after the colon) |
| C2 “For any significance covering what the part has reached before each step, … (Flow.Balances.comparison_within_reach): the comparisons under the axiom (Web.retains_iff_includes, Web.adds_iff_exceeds).” | law | law 2 (names → declarations) |
| C3–C4 decidable adding; double negation | law | law 3 (with the covering condition, see above) |
| C5–C6 “Significance bounded by a region closed under affecting … with no axiom (Flow.Balances.closed_comparison); the reach closure is the least such region holding a center, and the system is one.” | law | law 4 (names → declarations; closedUnder_withinClosure and Flow.withinSystem_closed for the second clause) |
| C7–C8 “Where the levels of two balanced flows from one start differ at a step, … (Flow.DiffersBefore, Flow.Balances.differs_before); any significance covering what the difference has reached … (Flow.Balances.comparison_within_difference).” | law | law 5 (names → declarations) |
| C9–C10 “Witnesses: in Clearing, from the clearer's standpoint, significance bounded by each system judges the clearer's part to lose the dweller, and bounded by each influence closure to retain (Clearing.system_counts_dweller); significance bounded by each reach closure is not the axiom, yet judges the part to lose the dweller as the axiom does (Clearing.reach_counts_dweller);” | law (witness) | law 6 (see above; “as the axiom does” written out as “retaining exactly where inclusion holds”, the theorem's last conjunct) |
| C11 “the source gives what the clearer takes, and with the rest of the exchange fixed no levels balance the flow without the source's part, so that comparison does not exist (Clearing.no_levels_without_source).” | law (witness) | law 7 (“In Clearing” added) |
| C12 “In Margin a part reaches beyond a formation's influence closure while the levels with it include those without, so every significance retains: covering is enough and not needed (Margin.reach_without_misjudgment).” | law (witness) | law 8 (see above) |
| C13–C14 “In Trophic, a trophic cascade, the wolves' part does not reach the forest (Trophic.wolves_unreached); with the rest of the exchange fixed … closing the deer (Trophic.deer_without_wolves), so under the axiom it does not retain from any standpoint (Trophic.mediated_unregistered);” | law (witness) | law 9 (names → declarations) |
| C15–C16 “against the flow in which the deer respond the same taking is mixed, … (Trophic.responsive_mixed); the wolves' part does not reach the forest while the difference … reaches it before the third step (Trophic.difference_reaches_forest);” | law (witness) | law 10 (“In Trophic” added) |
| C17 “the far formation's system holds only itself (Trophic.far_system), and from its standpoint … to retain, while under the axiom the part loses the deer (Trophic.mixed_part).” | law (witness) | law 11 (see above) |
| C18 “The general theorems use no axiom;” | premise | hypotheses[2] (first clause) and law 4 (“With no axiom”); the no-ethical-premise key is not cited, because three witnesses take the axiom as a hypothesis |
| C19 “the axiom Unrestricted appears only as a hypothesis of three witnesses.” | premise (duplicate of H2) | hypotheses[2] |
| L0 “Significance itself stays supplied;” | scope | does_not_show[0] |
| L1 “the adding comparisons in positive form follow for every significance only where it is decidable, and otherwise up to double negation;” | scope | does_not_show[1] (“for every covering significance”, see above), witness Flow.Balances.not_not_adds_of_exceeds |
| L2 “the comparison by withheld levels keeps the rest of the exchange fixed, a comparison in which others respond needs the second flow supplied, and responding flows are supplied in the witnesses;” | scope | does_not_show[2] |
| L3 “that a center knows what it reaches is not derived;” | non-implication | does_not_show[3] (“Does not show that a center knows what it reaches.”) |
| L4 “the readings and names are the AI's, pending Ren;” | reading | standard_boundaries: names-provisional; hypotheses[2] (the axiom reading) and the correspondence (the other readings and the names) |
| L5 “contains no ethical predicate.” | standard boundary | standard_boundaries: no-evaluation |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 100 theorems of Becoming.Feedback all have empty axiom reports;” | evidence | validation_scope; the count stays in the receipt and the snapshot |
| V1 “the same receipt covers the package's 75 modules … and 22 inherited modules …” | evidence (counts) | receipt + snapshot |
| V2 “periphery receipt 20261013T095049.338744Z passed.” | evidence | receipt + history + snapshot (every cited module is a core module) |
| V3 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (“core purity verified”); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V4 “The axiom Unrestricted appears only as a hypothesis, not as a Lean axiom.” | evidence | validation_scope |
| V5 “The author's counterreview is in §61 of the integration note;” | evidence | validation_scope (“in the integration note”); §61 stays in history (the entry that added the record) and the snapshot |
| V6 “reviewed before integration by the sixteenth independent review (BECOMING-P42-P43-REVIEW.md), whose treatment is in §62.1;” | evidence | validation_scope (“the sixteenth independent review read it before integration”); the review file is the record's `review` reference; §62.1 stays in history and the snapshot |
| V7 “the text after that treatment is not yet independently reviewed.” | evidence | validation_scope |
| R0–R2 Ren's long-term objectives, “pursue the strongest claims and complete proof”, Ren's levels | Ren's words | correspondence (verbatim) |
| R3 | reading | correspondence (unchanged) |
| R4 “… (P40 read the feeding closure as the system one is in; that reading is withdrawn);” | reading | correspondence (parenthesis → “the feeding closure was earlier read as the system one is in; that reading is withdrawn”; zh “P40 把供给闭包读作所在系统，这一读法撤回” → “供给闭包曾被读作所在系统，这一读法已撤回”); P40 → history + snapshot |
| R5–R8 | reading + names | correspondence (unchanged); standard_boundaries: names-provisional |
| N0 “A comparison whose responses the dynamics give without supplying that the rest responds only through its registration (under that premise P65 decides it within the responsive reach, comparison-where-the-rest-responds);” | next step | next_delta (“Give a comparison …”; “P65 decides it” → “comparison-where-the-rest-responds decides it”); P65 → history + snapshot. Flag: feedback-and-reach's next step records that where the rest follows a supplied law of exchange reading what has stood, comparison-where-the-rest-responds and counterfactual-is-the-course make the response premise a theorem. N0 may be partly answered by that; it is kept unchanged in scope and flagged here |
| N1 “how a center represents what it reaches;” | next step | next_delta (“model how a center represents what it reaches”) |
| N2 “Ren's judgment whether the weaker version reads as significance covering what a center reaches.” | next step | next_delta (“Whether the weaker version reads as significance covering what a center reaches is Ren's to judge.”) |
| H0–H1, H3–H4 | premises | hypotheses[0]–[1], [3]–[4] (unchanged) |
| H2 “The axiom Unrestricted appears only as a hypothesis of three witnesses (…); reading it as Ren's axiom is the AI's reading, pending Ren.” | premise | hypotheses[2] (C18 prefixed; otherwise unchanged) |
| X0 | counterexample | counterexamples[0] (unchanged) |

Remaining lint findings: the correspondence is over its length guide (en 1299/1200, zh 740/500). It quotes Ren's three passages verbatim in both languages (about 320 characters each time), without which it is within the guide; the remaining sentences are attributions of AI readings and names. It is kept rather than moved out of the record.
