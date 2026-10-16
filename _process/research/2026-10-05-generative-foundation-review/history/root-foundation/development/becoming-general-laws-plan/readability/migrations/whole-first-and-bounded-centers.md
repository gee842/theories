# Migration map: whole-first-and-bounded-centers

Old record sha256 `6caff59eb295dbd8516d1510e92813e226fd5ce70c228ff4cb30a0bc2de77f4b`; snapshot `_process/architecture/history/6caff59eb295dbd8/whole-first-and-bounded-centers.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, H hypotheses, R correspondence, L limitations, V validation_scope, N next_delta, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

Each law was read against its declarations in `Becoming/Significance.lean` (with `Web.AdmitsWithin`, `AdmitsWithin.narrow` and the Clearing witness in `Regions.lean`, the Clearing flow and web in `Continuation.lean`; bytes bound by the record's references). Every law states its theorem's own conditions: `Retains.of_fewer` takes `fewer : ∀ p t f, sig' p t f → sig p t f`; `retains_bounded_iff` is unconditional; `Retains.within` takes `Unrestricted sig` and holds for every `region : Pos → F → Prop` (a family of regions, one per standpoint); `admitted_all_without`, `centers_disagree` and `free_rider_loses` take the withheld levels (`flow.WithheldLevels clearerPart web l`), and `free_rider_loses` also the axiom. No law is wider than its theorem. “From step two on” counts from step zero (`unsupported_with (n) : ¬ web.Supported (n + 2) .dweller`).

| Old text | Type | New place |
|---|---|---|
| T0 “The whole first, and centers bounded by dependence” | title | title (unchanged) |
| S0–S2 “With fewer significant continuations more is retained; … and under the axiom for every standpoint.” | statement | statement (unchanged) |
| C0 “Where fewer continuations have significance, more is retained: where sig' implies sig, what retains from p for sig retains for sig' (Web.Retains.of_fewer).” | law | law 1 (Web.Retains among the declarations) |
| C1 “A significance bounded by regions (bounded region) retains from p exactly when at every step, within p's region, l admits what l' admits (Web.retains_bounded_iff, through Web.AdmitsWithin).” | law | law 2 (bounded, Web.AdmitsWithin and Web.retains_bounded_iff are its declarations) |
| C2 “Under the axiom, what retains from p retains from p for every family of regions (Web.Retains.within): the whole's judgment decides every narrower one, whether the region is a system's or a self's;” | law | law 3 |
| C3 “and what holds within a region holds within every region inside it (Web.AdmitsWithin.narrow).” | law | law 3 |
| C4 “The converse fails: in Clearing the clearer draws on a resource fed by the source, while the dweller depends on a habitat that the clearer's draw leaves unsupported from step two on.” | witness | law 4 (the Clearing flow, web, dependence, part, withheld levels and unsupported_with among the declarations) |
| C5 “Without the clearer's part every formation is admitted at every step (Clearing.admitted_all_without).” | law (witness) | law 4 |
| C6 “Let each formation's significance stop at what its dependence reaches (Clearing.dependenceRegion: …): from the clearer's standpoint its part retains what has significance at every step;” | law (witness) | law 5 (alongDependence and dependenceRegion among the declarations); counterexamples[0] (unchanged) |
| C7 “from the dweller's standpoint it loses the dweller (Clearing.centers_disagree).” | law (witness) | law 5 (Web.Adds among the declarations); counterexamples[0] (unchanged) |
| C8 “Under the axiom it loses the dweller from every standpoint, … so withholding the part ends nothing (Clearing.free_rider_loses).” | law (witness) | law 6; counterexamples[1] (unchanged) |
| C9 “No Lean axiom is used.” | evidence | validation_scope (“no Lean axiom is used, the axiom Unrestricted being a hypothesis of the theorems”); no-ethical-premise is not cited, since Unrestricted is a normative premise |
| H0–H2 | premise | hypotheses[0]–[2] (unchanged); H2's discrete steps also cite standard_boundaries: discrete-steps |
| R0–R7 “Ren's axiom is “for anything, …”. … read as the “belief” Ren names.” | correspondence | correspondence (unchanged; Ren's words verbatim). Its length warning (en 1458 > 1200, zh 1007 > 500) comes from Ren's quoted words alone: 728 quoted characters in each language, 730 en and 279 zh outside the quotes |
| L0 “Regions are parameters of the statement, and nothing models how a center forms its boundary;” | scope | does_not_show[0]; hypotheses[1] (first clause, already there); next_delta (its last item) |
| L1 “the region along dependence is a choice (the source reached along dependence, the dweller and the source alone);” | premise | hypotheses[1] (duplicate); law 5 describes the region |
| L2 “P40 shows that this region is exactly each formation's feeding closure (Clearing.dependenceRegion_iff; see feeding-closure), so the region is given by the dynamics, while bounding significance by it remains a choice;” | non-implication | does_not_show[1] (“see feeding-closure”); “P40 shows” and Clearing.dependenceRegion_iff, which is not among this record's references, → history (the migration note) |
| L3 “only formations admitted are compared, step by step;” | scope | does_not_show[2] |
| L4 “no duty or compliance is inferred, and nothing says what a center should do;” | non-implication | does_not_show[3] |
| L5 “the order of levels reads as an order of how complete a judgment is, not as what life does;” | correspondence | does_not_show[4]; the correspondence keeps the same reading |
| L6 “route (b) must face that centers bounded by their dependence license the free rider (P40: without the axiom, this loss counts only where the dependence reaches what is closed; see closure-verdict-meets-axiom);” | non-implication | does_not_show[5] (“P40:” → history) |
| L7 “the readings and names are the AI's, pending Ren.” | standard boundary | standard_boundaries: names-provisional; the correspondence keeps “(an AI argument, pending Ren)” and “the AI's, chosen by Ren's naming standard” |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T221720.428753Z): the 37 theorems of Becoming.Significance all have empty axiom reports;” | evidence | validation_scope (the receipt); the count stays in the receipt and the snapshot |
| V1 “the same receipt covers the package's 91 modules … with 4983 theorems/7020 declaration audits, and 39 inherited modules …;” | evidence (counts) | receipt + snapshot |
| V2 “periphery receipt 20261013T095049.338744Z passed.” | evidence | snapshot (the record cites no peripheral declaration); named in the migration history note |
| V3 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V4 “The axiom Unrestricted is a hypothesis of the theorems, not a Lean axiom.” | evidence | validation_scope |
| V5–V6 “The author's counterreview is in §53 of the integration note; not yet independently reviewed.” | evidence | validation_scope (§53 kept there) |
| (proof bindings) | evidence | validation_scope names the receipts that bind each source (Significance and Regions 20261013T094743.528770Z, Continuation 20261014T141427.442103Z), already in the references and proof bindings |
| N0 “Ren's judgment whether route (b), reaching the self and what it depends on, suffices (P40 shows that without the axiom centers bounded by their dependence still license the free rider beyond their feeding closure; see closure-verdict-meets-axiom);” | next step + completed connection | next_delta (“(see closure-verdict-meets-axiom)”); the P40 parenthesis is a completed connection, now does_not_show[5], and stays in full in the history note |
| N1 “whether the reach closure reads Ren's “the system that one is in” (levels-of-closure);” | next step | next_delta (unchanged) |
| N2 “the order of levels as three readings of the presupposition (presupposition-scopes);” | next step | next_delta (unchanged). *Flag:* presupposition-scopes now proves the order of the readings (Flow.presupposition_order) and gives the three readings as the AI's, pending Ren, so what is left of this item is Ren's judgment of that reading; the item is kept as it was, not rescoped |
| N3 “a model of how a center forms and represents its boundary.” | next step | next_delta (unchanged) |
| X0–X1 | counterexamples | counterexamples[0]–[1] (unchanged) |
