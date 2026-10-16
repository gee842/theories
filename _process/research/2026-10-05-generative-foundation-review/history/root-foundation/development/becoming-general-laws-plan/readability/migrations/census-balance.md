# Migration map: census-balance

Old record sha256 `c738317088d545394fb9246bfa472d5c1e6cdc41ca6e274ae0258ee64677703a`; snapshot `_process/architecture/history/c738317088d54539/census-balance.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence. Migration under the open-issues plan, stream F; documentary only, with no change of law, premise, status, proof binding or source hash.

Each law was checked against its Lean statement: `Listed.across` and `Listed.keeps_at` (the kept members, through `marks_le_of_sub`), `Listed.over_stretch`, `Listed.ceasings_within`, `Listed.comings_within`, the three readings `Web.Census.over_stretch` (decided activity), `Web.StandingCensus.over_stretch`, `Web.DependenceCensus.over_stretch` (decided requiring), `Listed.ceasing_iff_shortfall`, `Listed.coming_iff_excess`, and the local forms `balance_over_stretch_on` (balance only at the steps of the stretch), `Listed.across_at` (listings at the step's two ends), `Listed.over_stretch_on`, `*_from` (listing from `T` on). None is narrower or wider than the old text.

| Old text | Type | New place |
|---|---|---|
| T0 “The census balance” | title | title (unchanged) |
| S0–S1 “The list at the end with what ceased is the list at the start with what came; read of recurrence, it is exact.” | statement | statement (unchanged) |
| C0 “Where the members of which a determination holds are listed at each step, each once (Listed), and the determination is decided, across each step the length of the list after it … (Listed.across): the members kept across the step are counted alike on both lists (marks_le_of_sub).” | law | law 1 |
| C1 “So over any stretch the list at the end with what ceased between is the list at the start with what came between (Listed.over_stretch, summed step by step by balance_over_stretch);” | law | law 2 |
| C2 “what ceases is at most what comes and the list at the start, and what comes at most what ceases and the list at the end (Listed.ceasings_within, Listed.comings_within).” | law | law 2 |
| C3 “Read of activity: under a census, …(Web.Census.over_stretch);” | law | law 3 |
| C4 “read of standing: under a census of what stands, … (Web.StandingCensus.over_stretch).” | law | law 3 |
| C5 “Read of dependence: under a census of dependences, … (Web.DependenceCensus.over_stretch).” | law | law 4 |
| C6 “Read of recurrence the balance is exact: ceasing to be recurs exactly when … (Listed.ceasing_iff_shortfall), and coming to be recurs exactly when … (Listed.coming_iff_excess).” | law | law 5 |
| C7 “The census law and the bounded law follow from it (ceasing-needs-arising, bounded-census-keeps-pace).” | law (pointer) | law 5 (second sentence); related (unchanged) |
| C8 “This is the census form of section 26's law of a finite family (held_over_stretch, keep_pace): no fixed finite family is needed, only the list at each step.” | law | law 6 (“section 26's law” → “the law of a finite family … in coming-and-ceasing-keep-pace”) |
| C9 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise |
| L0 “Stated for discrete steps and holders finitely many at each step;” | scope | standard_boundaries: discrete-steps; does_not_show[0] (holders finitely many at each step) |
| L1 “needs decidability (a logical commitment);” | logical commitment | standard_boundaries: decidability; hypotheses[1] (unchanged) |
| L2 “the balance is a count, saying neither which member enters or leaves nor that entering and leaving are causally linked;” | non-implication | does_not_show[1] |
| L3 “evaluates neither arising nor ceasing;” | standard boundary | standard_boundaries: no-evaluation |
| L4 “names are Ren's to choose.” | names | standard_boundaries: names-provisional; next_delta |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 130 theorems of Becoming.Population (new in P28: …; new in P30: …) and the 85 theorems of Becoming.Openness (Web.StandingCensus.over_stretch new in P28) all have empty axiom reports;” | evidence | validation_scope (modules and receipt); counts and the per-round lists of names → receipt + snapshot |
| V1–V2 “the same receipt covers the package's 75 modules …; periphery receipt 20261013T095049.338744Z passed.” | evidence | validation_scope (periphery receipt); counts → receipt + snapshot |
| V3–V4 “The author's counterreview is in §37 and §40 of the integration note; no independent review yet.” | evidence | validation_scope (“two sections of the integration note”); section numbers → history (migration note); “no independent review yet” is superseded within the same old paragraph by V6 |
| V5 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); details → receipt + snapshot |
| V6–V7 “The eleventh independent review (BECOMING-P25B-P29-REVIEW.md) accepts its mathematics, and its corrections are handled in §42 of the integration note; those corrections are not yet independently reviewed.” | evidence | validation_scope; review file stays in references; §42 → history (migration note) |
| V8 “The 44 theorems of Becoming.Locality (P48) also have empty axiom reports.” | evidence | validation_scope (Becoming.Locality); count and label → snapshot |
| V9 “This record's local laws (P50) are in the same receipt, with empty axiom reports.” | evidence | validation_scope (“with this record's local laws”); label → snapshot |
| (references, proof_bindings) Dependence.lean and Generation.lean bound to receipt 20261014T091930.724493Z | evidence | validation_scope now names that receipt, which the proof bindings already used |
| R0–R1 “Section 26's held_over_stretch holds of one fixed finite family; with infinitely many relata there is no such family.” | correspondence | correspondence (“section 26's” → “the finite-family law (held_over_stretch in coming-and-ceasing-keep-pace)”) |
| R2 “This result shows that wherever the holders at each step are finitely many and listed, the same balance holds, and it gives rates: …” | correspondence | correspondence (shortened wording, same content) |
| R3 “The recurrence laws of P26 and P27 follow from it: …” | correspondence | correspondence (“the recurrence laws of P26 and P27” → “the census and bounded laws”, named in law 5) |
| R4–R5 “Before P30 they were proved from the lengths of the lists directly, a second route beside the balance; now there is one route, through the balance (P30).” | round narration | history (migration note) + snapshot; law 5 states that they follow from the balance |
| R6 “The author's reading (an AI argument): …” | reading | correspondence (unchanged) |
| R7–R8 “This is a reading of activity, standing and any determination, arising and ceasing being names Ren confirmed (…); whether it is the proposal's generative and degenerative is Ren's to choose (Ren wrote ‘…’ …).” | reading + Ren's words | correspondence (Ren's words verbatim and attributed; the AI's gloss unchanged) |
| R9 “It evaluates neither arising nor ceasing.” | standard boundary | standard_boundaries: no-evaluation |
| N0 “The exact restatement for every world is this record's balance_over_stretch_on, Listed.across_at, … (P50), the local condition inside the law: balance across each step of the stretch, or what holds listed only at the step's two ends, at each step of the stretch, or at each step from some step on;” | local form appended to next | law 7 (across a step, over a stretch, the three readings); law 8 (from some step on); label P50 → history (migration note) |
| N1 “the two iffs of the recurrence reading stay exact on a listed tail;” | local form | law 8 |
| N2 “balance_over_stretch, Listed.across, … are their corollaries;” | local form | laws 7 and 8 (“the earlier forms are their corollaries”) |
| N3 “names (Ren).” | next step | next_delta |
| N4 “Deriving the recurrence laws from the balance, so that the two routes are one, and the balance read of dependence are given in P30.” | round narration | history (migration note) + snapshot; the content is laws 4 and 5 |
| H0 “Listing: …” | premise | hypotheses[0] (unchanged) |
| H1 “Decidability: …” | premise | hypotheses[1] (unchanged) |
| X0 “Attrition: … Accretion: …” | counterexample | counterexamples[0] (unchanged) |
