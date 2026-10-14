# Migration map: axiom-decomposition

Old record sha256 `3ecd675234f5776fa29b28acc7f27f918a8ea8ae1a4bcb7918500ae3add5724c`; snapshot `_process/architecture/history/3ecd675234f5776f/axiom-decomposition.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence (zh C12–C13 hold en C12, so later zh claim labels run one ahead).

Each law was read against its declarations in `Becoming/Boundaries.lean`, with `Unrestricted`, `bounded`, `Valuation.premises_of_unrestricted` and `Web.retains_agree` in `Becoming/Significance.lean`, `Valuation.significant_iff` in `Becoming/Metaethics.lean`, `Valuation.significant_iff_held` in `Becoming/Standpoints.lean`, `Flow.system_whole_of_common`, `Clearing.system_whole` and `WithinClosure` in `Becoming/Feedback.lean`, and `Flow.WithinFeeding` and `Clearing.dweller_beyond` in `Becoming/Interdependence.lean`. None states more than the declaration. Every law about one standpoint keeps the condition that the whole is admissible (`whole`), and laws 4 and 7 keep covering (`covers`, `centers`). Two places are written as the Lean has them, narrower or more exact than the old text:

- Law 3 says the axiom *is* boundary neutrality for the significance of continuation, which is the Lean definition of `Unrestricted` (`Neutral` of the significance of continuation); the old claim said a work item “reads” it so.
- Law 8 names the conditions of the two core decompositions: `Valuation.significant_iff` needs a connected whole with some living claim, and `Valuation.significant_iff_held` needs every living claim to be some standpoint's own (`V.Held`). The old text gave the decompositions without these conditions.

Law 1 is added: it states the Lean definitions (`SuperTrue`, `SubTrue`, `BoundaryInvariant`, `SignificantWithin`) that the other laws use, which the old record took from its dependency presupposition-scopes; hypotheses[0] (unchanged) already says what a boundary along a relation is.

| Old text | Type | New place |
|---|---|---|
| T0 “Decomposition of the axiom” | title | title (unchanged) |
| S0–S2 “Where the whole is admissible, the axiom is exactly the presupposition sub-true and boundary-invariant at every standpoint. Invariance is exactly the conditional from presupposition to axiom, carrying all it adds; with presupposition and covering everywhere, it is standpoint-invariance (N_std).” | statement | statement (unchanged) |
| — | definitions | law 1 (added; see above) |
| C0 “Wherever the whole is admissible, the presupposition is boundary-invariant exactly when, holding as drawn anywhere, it holds as drawn at the whole (boundaryInvariant_iff_extends);” | law | law 2 |
| C1 “that is exactly the conditional from the presupposition to the axiom at p, with no presupposition assumed (boundaryInvariant_iff_conditional);” | law | law 2 |
| C2 “with the presupposition sub-true, invariance is exactly the axiom at p (boundaryInvariant_iff_all), and since P39 reads the axiom as boundary neutrality, at one standpoint the step is boundary neutrality;” | law + work-item label | law 3; “P39 reads” → the Lean definition `Unrestricted` (see above); the dependency one-axiom-yields-g0 (unchanged) keeps its own detail |
| C3 “where some continuation lacks significance from p, an invariant presupposition holds as the boundary is drawn nowhere (not_subTrue_of_invariant): the step runs both ways.” | law | law 2 (“holds at no drawing”, with the whole admissible as the declaration needs) |
| C4 “Let every formation lie within some admissible boundary of every self (covering), let each standpoint's presupposition be sub-true, and let it be invariant: then the axiom holds (unrestricted_of_presupposed);” | law | law 4 |
| C5 “where the whole is admissible for every self, the axiom is exactly the presupposition sub-true and invariant at every standpoint (unrestricted_iff_presupposed), along any relation (unrestricted_iff_presupposed_along);” | law | law 5 (“along any relation” states the boundaries along it, as the declaration does) |
| C6 “where each center's closure is the whole, the whole is the only boundary, invariance holds trivially, and the axiom is exactly the presupposition sub-true at every standpoint (unrestricted_iff_presupposed_of_whole).” | law | law 5 |
| C7 “Corollaries: standpoints retain alike (…), and G0 holds at the level of claims on every reading in which a claim's significance is that of some formation's continuation at some step (…).” | laws | law 6 (the premises of both corollaries written out: the whole admissible for every self, the presupposition sub-true and invariant at every standpoint) |
| C8 “Significance is standpoint-invariant (StandpointInvariant) when …, the rule of N_std;” | definition | law 7 |
| C9 “along a relation, with every formation within some center's closure and every standpoint's presupposition sub-true, it gives the axiom (…) and is equivalent to boundary-invariance everywhere (…);” | laws | law 7 (“everywhere” → “at every standpoint”) |
| C10 “without the presupposition everywhere the two come apart (OneCounts.forms_apart).” | law | law 7; counterexamples[0] (unchanged) |
| C11 “So the premises carry two decompositions already in the core to the significance of continuation: Valuation.significant_iff (…) and Valuation.significant_iff_held (…).” | law (comparison) | law 8 (conditions named; see above) |
| C12 “Where each center's system is the whole, the axiom is exactly the presupposition sub-true along sharing a condition at every standpoint (…), one common condition sufficing (…);” | laws | law 9 (“one common condition, in which every formation takes part”, as the declaration's `common`) |
| C13 “Clearing is one system (Clearing.system_presupposition).” | law | law 9 |
| C14 “Each premise is needed: in Clearing, with nothing significant, the presupposition is invariant and the whole admissible while the axiom fails (…);” | law (witness) | law 10 (“the whole a boundary of every self”, as the declaration states); “Each premise is needed” → counterexamples[0] (unchanged), which opens with it |
| C15 “significance bounded by each feeding closure makes every presupposition sub-true with the whole admissible while the axiom fails, the presupposition at the clearer is not invariant (…), and significance is not standpoint-invariant (…);” | law (witness) | law 10 |
| C16 “were each self's only admissible boundary its feeding closure, … and the axiom would still fail (Clearing.with_fixed_boundary).” | law (witness) | law 11 |
| C17 “The decomposition locates the step and does not lower the axiom's content.” | non-implication | does_not_show[0] (with L0, which repeats it) |
| C18 “No Lean axiom is used;” | evidence | hypotheses[0] (unchanged: “hypotheses, not Lean axioms”); validation_scope (empty axiom reports) |
| C19 “covering, sub-truth and invariance are hypotheses.” | premise | hypotheses[0] (unchanged); does_not_show[1]; standard_boundaries: conditional-not-universal |
| L0 “The decomposition locates the step and does not lower the axiom: invariance is the conditional …, and given the presupposition it is the axiom at that standpoint;” | non-implication | does_not_show[0] (witness boundaryInvariant_iff_conditional) |
| L1 “the presupposition, covering and invariance themselves are not derived;” | scope | does_not_show[1] (“hypotheses of the theorems, which give no derivation of them”) |
| L2 “one who denies the step can hold the presupposition only relative to a drawing or a standpoint, or give it up;” | non-implication | does_not_show[2] (“It does not compel the step: …”; witness Clearing.without_invariance, where every presupposition is sub-true and the clearer's is not invariant) |
| L3 “which premise each rival denies (…) is located, not refuted;” | scope | does_not_show[3] |
| L4 “the literature is from prior knowledge;” | source | does_not_show[3] (second clause) |
| L5 “the step from significance to a reason, to motivation or to practice is not derived;” | non-implication | does_not_show[4] (“lies outside the theorems”) |
| L6 “the readings and names are the AI's, pending Ren;” | standard boundary | standard_boundaries: names-provisional; the correspondence keeps “(an AI argument, pending Ren)” and “the other names are the AI's” |
| L7 “after the audit of G0's uses (P44) came out clean, Ren folded G0 on 11 October 2026, and it is no longer an axiom (P51).” | status + date + work-item labels | correspondence (last sentence, without date and labels); the fold with Ren's words is history entry 2 (existing); P44's landing is history entry 1 (existing) |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 47 theorems of Becoming.Boundaries all have empty axiom reports;” | evidence | validation_scope (receipt and empty axiom reports; the count stays in the receipt and the snapshot); Becoming.Metaethics's current binding receipt 20261014T091930.724493Z is named, as the proof bindings have it |
| V1 “the same receipt covers the package's 75 modules … and 22 inherited modules …;” | evidence (counts) | receipt + snapshot |
| V2 “periphery receipt 20261013T095049.338744Z passed.” | evidence | receipt + snapshot (the record cites no peripheral declaration) |
| V3 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V4 “The author's counterreview is in §62 of the integration note;” | evidence | validation_scope (“in the integration note”); §62 is in history entry 0 |
| V5 “reviewed before integration by the sixteenth independent review (BECOMING-P42-P43-REVIEW.md), whose treatment is in §62.1;” | evidence | validation_scope (the review file is listed under sources as the review reference; §62.1 is in history entry 0) |
| V6 “the text after that treatment is not yet independently reviewed.” | evidence | validation_scope |
| R0–R1 Ren's words from “Truth exist” and earlier | Ren's words | correspondence (verbatim, both languages) |
| R2 “The AI proposed that the axiom may follow from three claims …, one step short (the AI's words, in the source);” | provenance | correspondence (“(in the source)”) |
| R3 “the sixteenth review corrected this: the result is a decomposition of the axiom, not a reduction.” | provenance + correction | correspondence (“on review, the result is a decomposition of the axiom, not a reduction”); the sixteenth review is named in history entry 0 and in validation_scope |
| R4–R7 the author's reading | reading | correspondence (unchanged) |
| R8 “Super-truth and sub-truth are named from supervaluation (Fine 1975) and subvaluation (Hyde 1997), from prior knowledge;” | source | correspondence (unchanged) |
| R9 “the other names (Boundary, SignificantWithin, BoundaryInvariant, StandpointInvariant, OneCounts) are the AI's, chosen by Ren's naming standard.” | names | correspondence (“the other names are the AI's”; the names are the laws' declarations); “chosen by Ren's naming standard” → standard_boundaries: names-provisional (“Names follow Ren's naming criteria”) |
| N0–N1 | next step | next_delta (unchanged) |
| H0–H1 | premises | hypotheses[0]–[1] (unchanged) |
| X0 | counterexample | counterexamples[0] (unchanged) |
