# Migration map: continuing-self-fed-from-beyond

Old record sha256 `55de6e2d567deed9568749b8003c4f8613e52cbfd794b2c4e4ae071fc09aa3d6`; snapshot `_process/architecture/history/55de6e2d567deed9/continuing-self-fed-from-beyond.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses and quotations): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence (the labels align in both languages).

Each law was read against its declarations in `Becoming/Continuation.lean` (with `Becoming/Dissipation.lean` for `Flow.Inward`, `Flow.Around`, `Flow.Dissipative`, `Flow.taking_draws_in`, `Flow.rising_draws_in` and `Lone.lone`, `Becoming/Roles.lean` for `Web.generation_draws_in`, and `Becoming/Flow.lean` for `Flow.BalancesOn` and `Flow.Balances.on`). The laws are the old claim's sentences with the declaration names moved into `declarations`. Law 3 says “formations take from it at arbitrarily late steps” for C4's “taking from it recurs”, as `Flow.fed_from_beyond` states its hypothesis (`∀ N, ∃ t, N ≤ t ∧ 0 < L.takers ds t`). Law 5 says “every family without repetition closed across each step”, as the local forms take dissipation only of families that are `Distinct` and `ClosedAt` the step. No law states more than its declaration; the conclusions keep their constructive form (“cannot from any step on be fed from nothing beyond it”), which hypotheses[3] explains.

The validation scope follows the current proof bindings: Continuation is bound to receipt 20261014T141427.442103Z, Dissipation, Roles, Flow and Succession to 20261013T094743.528770Z. The old text cited receipt 20261013T221720.428753Z for Continuation; the current Continuation bytes are those of the bound receipt.

| Old text | Type | New place |
|---|---|---|
| T0 “A continuing family is fed from beyond” | title | title (unchanged) |
| S0–S1 | statement | statement (unchanged) |
| C0–C1 “Across the step from t, something is conveyed from c to d when … (Flow.Conveys); a family ds is fed from beyond across the step when … (Flow.FedFromBeyond).” | law | law 1 (names → declarations; “a family ds” → “a family”) |
| C2–C3 “A step at which the family is fed from beyond is not inward (Flow.not_inward_of_fed); with equality decided, … (Flow.inward_of_not_fed), so the two are exact opposites (Flow.inward_iff_not_fed), and whatever refutes … (Flow.fed_of_not_inward).” | law | law 2 (names → declarations) |
| C4 “So under balance and dissipation a finite family without repetition, enclosed around from some step on, cannot … whether taking from it recurs (Flow.fed_from_beyond, from taking_draws_in), its members rise at arbitrarily late steps (Flow.rising_fed_from_beyond, from rising_draws_in), or, read with one kind of relatum, embodied members arise at arbitrarily late steps (Web.generation_fed_from_beyond, from Web.generation_draws_in).” | law | laws 3 (taking and rising; “from taking_draws_in” → “by the draw-in laws”) and 4 (read with one kind of relatum) |
| C5–C6 “Being fed is needed, and no source condition need recur: in Lone, … (Lone.lone) … (Lone.fed, Lone.each_fuel_once, Lone.fed_not_recurring); the one source does all the conveying.” | law (witness) | law 6 (names → declarations); counterexamples[0] (unchanged) |
| C7 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (the hypotheses contain no ethical premise; the bound receipts report empty axiom lists) |
| L0 “Stated for discrete steps, natural-number amounts and finite families;” | standard boundary + premise | standard_boundaries: discrete-steps; hypotheses[4] (new item: “Discrete steps, natural-number amounts and finite families.”) |
| L1 “needs balance, dissipation, enclosure and decided equality;” | premise (duplicate) | hypotheses[0]–[2] |
| L2 “the conclusion is a constructive negation and exhibits no step at which the family is fed;” | premise (duplicate of H3) | hypotheses[3] |
| L3 “says only that what lies beyond must be counted, not that it ought to be, and contains no ethical predicate;” | non-implication + standard boundary | does_not_show[0]; standard_boundaries: no-evaluation |
| L4 “says neither which formation conveys nor whether the source is living;” | non-implication | does_not_show[1] |
| L5 “in Lone the one source does all the conveying, and in Successive no source formation recurs while each source is still needed at its own step;” | witness (duplicate) | counterexamples[0] and [1] (unchanged); law 6 (“the one source does all the conveying”); correspondence R7 |
| L6 “the names are the AI's wording, for Ren to choose (Conveys, FedFromBeyond and others).” | names | standard_boundaries: names-provisional |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T221720.428753Z): the 52 theorems of Becoming.Continuation all have empty axiom reports;” | evidence | validation_scope (current bindings, see above); the count and the receipt id stay in the snapshot |
| V1 “the same receipt covers the package's 91 modules … and 39 inherited modules …” | evidence (counts) | receipt + snapshot |
| V2 “periphery receipt 20261013T095049.338744Z passed.” | evidence | receipt + history + snapshot (every cited module is a core module) |
| V3 “The author's counterreview is in §47 of the integration note;” | evidence | validation_scope (“in the integration note”); §47 stays in history (the entry that added the record) and the snapshot |
| V4 “the independent review (CONTINUATION-GROUNDING-REVIEW.md) accepts its Lean, and its corrections are handled in §47.1–47.4 of the integration note.” | evidence | validation_scope (“the independent review accepts its Lean, and its corrections are handled in the integration note”); the review file is the record's `review` reference; §47.1–47.4 stays in history (the W8 entry) and the snapshot |
| V5 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (“core purity verified”); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V6 “This record's local laws (P57–P61) are in the same receipt, with empty axiom reports.” | evidence | validation_scope (“the local forms included”); P57–P61 → history (the P57 entry) + snapshot |
| R0–R7 | Ren's words + readings | correspondence (unchanged) |
| N0 “The exact restatement for every world is this record's Flow.fed_from_beyond_from, rising_fed_from_beyond_from (P57), the local condition inside the law: from some step on: the family balanced on and enclosed around, and the families closed across each step dissipated on;” | completed result | law 5 (names → declarations; “the families closed across each step” → “every family without repetition closed across each step”, see above); P57 → history + snapshot |
| N1 “Flow.fed_from_beyond, rising_fed_from_beyond are their corollaries;” | completed result | law 5 (“the forms under balance and dissipation everywhere are their corollaries”); dependency laws-of-one-step (unchanged) |
| N2 “the reading where what is conveyed comes from a living source;” | next step | next_delta (“Read the case where what is conveyed comes from a living source”) |
| N3 “the witness in which no source formation recurs is given (Successive.relay);” | completed item | counterexamples[1] (unchanged; it states the Successive witness, Successive.relay); its addition is in history (the P85 entry) |
| N4 “the removable form, the same world still fed at every step with one source formation taken away (taking a formation away changes the levels, so that is another flow, and the world-level form is its place);” | next step | next_delta (“give the removable form, …”; the parenthesis reordered: “that is another flow, since taking a formation away changes the levels; the world-level form is its place”) |
| N5 “whole-run and world-level forms;” | next step | next_delta (“give whole-run and world-level forms”) |
| N6 “whether conveyance counts as a formed relation (Ren).” | next step | next_delta (“Whether conveyance counts as a formed relation is Ren's to judge.”) |
| H0–H3 | premises | hypotheses[0]–[3] (unchanged) |
| X0–X2 | counterexamples | counterexamples[0]–[2] (unchanged) |

Remaining lint findings: none expected beyond the generated-page notice of the focused check; the correspondence is within its length guide (en 991/1200, zh 423/500).
