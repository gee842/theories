# Migration map: four-cases-of-a-part

Old record sha256 `515adab08df51e90630052fd43056e52b18faf82250fca98551b6e7c81b52b62`; snapshot `_process/architecture/history/515adab08df51e90/four-cases-of-a-part.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, H hypotheses, R correspondence, L limitations, V validation_scope, N next_delta, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

Each law was read against its declarations in `Becoming/Admission.lean` (inclusion, the three balance laws, Inflow and Transfer), `Becoming/Regions.lean` (the four cases and the Clearing withheld levels) and `Becoming/Significance.lean` (`widens_iff_within_margin_at`), with the Clearing flow and web in `Continuation.lean`; bytes bound by the record's references. The laws keep their theorems' conditions: `closes_nothing`, `opens_nothing` and `changes_nothing` take `balances : L.Balances W` and the withheld levels, and compare `partTaken` with `partGiven` at every step and condition; `changes_nothing` concludes inclusion both ways, which is `Web.Keeps` by definition, so “the case of keeping the same” adds nothing to the theorem; `widens_iff_within_margin_at` takes balance only at the conditions each formation requires, across the steps before it (`∀ t f c, W.requires t f c → ∀ s, s < t → L.BalancesOn W [c] s`). “From step one on” and “from step two on” count from step zero (`Supported (t + 1) false`, `¬ Supported (n + 2) .dweller`). No law is wider than its theorem.

| Old text | Type | New place |
|---|---|---|
| T0 “Four cases of a part” | title | title (unchanged) |
| S0–S2 “By inclusion of the level paths with it and with it withheld, a part widens, narrows, keeps the same or is mixed. …” | statement | statement (unchanged) |
| C0 “A level path l includes another l′ (Web.Includes) when at every step l admits every formation l′ admits;” | definition | law 1 |
| C1 “inclusion is a preorder (Web.Includes.refl, Web.Includes.trans).” | law | law 1 |
| C2 “l exceeds l′ (Web.Exceeds) when at some step l admits a formation l′ does not;” | definition | law 1 |
| C3 “a path that includes l′ is not exceeded by it (Web.Includes.not_exceeded).” | law | law 1 |
| C4 “In a balanced flow, where the levels without a part exist: a part giving each condition at every step at least what it takes from it closes nothing … (Flow.Balances.closes_nothing);” | law | law 2 |
| C5 “one giving no more than it takes opens nothing … (Flow.Balances.opens_nothing);” | law | law 2 |
| C6 “one giving back exactly what it takes changes nothing that can form (Flow.Balances.changes_nothing).” | law | law 2 |
| C7 “Compared by inclusion in both directions with the levels without it, a part widens, narrows, keeps the same or is mixed (this split is classical logic, not a theorem here);” | premise (classical split) | statement (already says it); hypotheses[2] (duplicate: “the split into four cases is classical logic over the two inclusions, not a Lean theorem”) |
| C8 “the witness of each case exhibits its levels without the part.” | framing of the witnesses | law 4 (its first sentence) |
| C9 “It widens, the levels with it including and exceeding those without it: in Inflow, without the giver's part (Restoring.Inflow.giverPart) the condition stays at zero (Restoring.Inflow.withheld) and false is admitted at no step, while with it false is supported from step one on (Restoring.Inflow.widens).” | law (witness) | law 4 |
| C10 “It narrows, the converse: in Clearing, without the clearer's part the resource rises by one at each step and the habitat stays at two (Clearing.withheld), and the dweller is admitted at every step (Clearing.admitted_without), while with the part it is not supported from step two on (Clearing.unsupported_with);” | law (witness) | law 5 (the Clearing flow, web, balance and withheldLevel among the declarations) |
| C11 “so the part opens nothing and closes the dweller (Clearing.narrows).” | law (witness) | law 5; counterexamples[1] (unchanged) |
| C12 “It keeps the same, the case of changes_nothing.” | law | law 2 (“the case of keeping the same”); does_not_show[2] keeps that there is no separate witness |
| C13 “It is mixed, each path exceeding the other: in Transfer the conveyor takes a unit from the first condition at step zero and gives it to the second;” | law (witness) | law 6 (the Transfer flow, web, balance, acting, taking, dependence and unitDrop among the declarations) |
| C14 “without its part the first condition stays at one and the second at zero (Transfer.withheld);” | law (witness) | law 6 |
| C15 “with it, from step one on, the second formation is supported and the first is not, while without it the first is admitted at every step and the second at none (Transfer.mixed).” | law (witness) | law 6; counterexamples[0] (unchanged) |
| C16 “A mixed part is not ordered by inclusion: ordering it needs a measure trading some possibilities against others, which is a further premise.” | non-implication | does_not_show[1] (witness Transfer.mixed). Wording: “trading” → “weighing”, as the Chinese 权衡 already says; the meaning is unchanged |
| C17 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (the hypotheses hold no ethical premise; the receipts report empty axioms) |
| C18 “P56: the four cases are definitions: l widens l′ (Web.Widens) when it includes and exceeds it, two keep the same (Web.Keeps) when each includes the other, and two are mixed (Web.Mixed) when each exceeds the other;” | definitions | law 3 (“P56:” → history) |
| C19 “widening goes one way (Web.Widens.not_reverse) and is transitive (Web.Widens.trans), and the four cases exclude one another (Web.Widens.not_keeps, Web.Widens.not_mixed, Web.Keeps.not_mixed, with the symmetries Web.Keeps.symm and Web.Mixed.symm), with no classical logic.” | law | law 3 (“keeping the same and being mixed are symmetric”) |
| C20 “With balance at the conditions each formation requires, across the steps before it, the levels with a part widen those without it exactly when … (Flow.widens_iff_within_margin_at, on the local phase boundary of closing-needs-net-draw);” | law | law 7 |
| C21 “in a balanced flow this is Flow.Balances.widens_iff_within_margin.” | law | law 7 (“so too in a balanced flow”; the name is among its declarations) |
| H0–H3 | premise | hypotheses[0]–[3] (unchanged); H3's discrete steps also cite standard_boundaries: discrete-steps |
| R0–R7 “Ren wrote that being generative is … The reading and the names are the AI's.” | correspondence | correspondence (unchanged; Ren's words verbatim) |
| L0 “The comparison looks only at which formations are admitted at each step, not at reachability over several steps, renewal capacity or richness of relations;” | scope | does_not_show[0]; next_delta (its last item, unchanged) |
| L1 “that the four cases exclude one another is a Lean theorem (P56), while that every part falls under one of them uses classical logic and is not a Lean theorem;” | law + premise | law 3 (the exclusion; “P56” → history); hypotheses[2] (duplicate: the classical split) |
| L2 “keeping the same has no separate witness and is given by changes_nothing;” | scope | does_not_show[2]; law 2; next_delta (its second item, unchanged) |
| L3 “the rest of the exchange does not adjust;” | scope | does_not_show[3] (“With a part withheld, …”) |
| L4 “where no level path balances the flow without the part there is nothing to compare;” | scope | does_not_show[4] |
| L5 “a mixed part is not ordered by inclusion;” | non-implication | does_not_show[1] (with C16) |
| L6 “the witnesses are minimal, their endings stipulated in activity or requirements and shown consistent with balance, support and dependence;” | correspondence | does_not_show[5] |
| L7 “contains no ethical predicate and does not say which part should be withheld or ended;” | standard boundary + non-implication | standard_boundaries: no-evaluation (“contains no ethical predicate”); does_not_show[6] (“Nothing says which part should be withheld or ended.”) |
| L8 “reading widening, narrowing and keeping the same as generative, degenerative and neutral is the AI's reading, pending Ren;” | reading | correspondence (already: “The author's reading (an AI argument, pending Ren): widening reads as generative, …”); standard_boundaries: names-provisional |
| L9 “the names are the AI's wording, for Ren to choose.” | standard boundary | standard_boundaries: names-provisional; the correspondence keeps “The reading and the names are the AI's” |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T221720.428753Z): the 46 theorems of Becoming.Admission and the 26 of Becoming.Regions all have empty axiom reports;” | evidence | validation_scope (the receipt); the counts stay in the receipt and the snapshot |
| V1 “the same receipt covers the package's 91 modules … 4983 theorems/7020 declaration audits, and 39 inherited modules …;” | evidence (counts) | receipt + snapshot |
| V2 “periphery receipt 20261013T095049.338744Z passed.” | evidence | snapshot (the record cites no peripheral declaration); named in the migration history note |
| V3 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V4–V5 “The author's counterreview is in §51 of the integration note; not yet independently reviewed.” | evidence | validation_scope (§51 kept there) |
| (proof bindings) | evidence | validation_scope names the receipts that bind each source (Admission, Regions and Significance 20261013T094743.528770Z, Continuation 20261014T141427.442103Z), already in the references and proof bindings |
| N0–N2 “The premises a measure for mixed parts would need …; a witness for keeping the same; comparisons of renewal capacity and richness of relations.” | next step | next_delta (unchanged) |
| X0–X1 | counterexamples | counterexamples[0]–[1] (unchanged) |
