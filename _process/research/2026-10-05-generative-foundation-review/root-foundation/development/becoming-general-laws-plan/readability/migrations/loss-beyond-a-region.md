# Migration map: loss-beyond-a-region

Old record sha256 `5b530b0e905ac91b7c06fb4fde564e4a9873079583742d7ff27d45a05ab8083f`; snapshot `_process/architecture/history/5b530b0e905ac91b/loss-beyond-a-region.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses and quotations): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence (the labels align in both languages).

Each law was read against its declarations in `Becoming/Regions.lean` (with `Becoming/Admission.lean` for `Web.Admits`, `Web.Includes` and `Flow.WithheldLevels`, and `Becoming/Standpoints.lean` for `Clearing.fedBy_source`). The laws are the old claim's sentences with the declaration names moved into `declarations`; laws 1 and 4 say “at a step”, as the theorems are stated per step. Law 7 names the dweller where `Clearing.loses_beyond` states that some formation beyond `alongDependence` is lost (`Web.LosesBeyond` is existential): this is exact, because the dweller is the only formation of Clearing outside that region (`alongDependence` holds of the source and the clearer). “From step two on” counts from step zero, as hypotheses[3] says (the theorem's `n + 2`; its docstring counts from one and says “the third step”). No law states more than its declaration.

The validation scope follows the current proof bindings: Regions, Admission and Standpoints are bound to receipt 20261013T094743.528770Z, Continuation to 20261014T141427.442103Z. The old text cited receipt 20261013T221720.428753Z; all three receipts record the same bytes of Regions, Admission and Standpoints (`13b5c507…`, `6e6d134d…`, `bb5bfadd…`), which are the current bytes.

| Old text | Type | New place |
|---|---|---|
| T0 “Loss beyond a region” | title | title (unchanged) |
| S0–S1 “Compared over nested regions of formations, … closes the dweller beyond them.” | statement | statement (unchanged) |
| C0–C1 “Within a region of formations, levels l admit every formation the levels l′ admit there (Web.AdmitsWithin); there is loss beyond the region (Web.LosesBeyond) when …” | law | law 1 (names → declarations; “at a step” added, see above) |
| C2 “Inclusion is admission within the whole at every step (Web.includes_iff_within_whole).” | law | law 2 (first clause) |
| C3–C4 “What holds within a region holds within every region inside it (Web.AdmitsWithin.narrow); what is lost beyond … (Web.LosesBeyond.narrow): the smaller the region, the more lies beyond it.” | law | law 3 (names → declarations) |
| C5 “Nothing lies beyond the whole (Web.not_losesBeyond_whole), and what holds within the whole leaves nothing lost beyond any region (Web.AdmitsWithin.not_losesBeyond).” | law | law 4 (“at a step … at that step” added) |
| C6 “Within one formation, what holds is its own admission by l wherever l′ admits it (Web.admitsWithin_self).” | law | law 5 (name → declarations) |
| C7 “In Clearing the levels without the clearer's part (Clearing.clearerPart) exist (Clearing.withheld, see four-cases-of-a-part).” | law | law 6 (names → declarations); “see four-cases-of-a-part” is the dependency four-cases-of-a-part (unchanged) |
| C8 “The region Clearing.alongDependence is the clearer with the source that feeds the one condition it requires, its resource;” | law | law 6 |
| C9 “it matches the formations Clearing.fedBy_source finds along feeding (checked by inspection, not by a theorem).” | law + superseded evidence status | law 6 (“along feeding only the clearer is fed, and only by the source”, `Clearing.fedBy_source`); the match is now a theorem (L4): the related entry feeding-closure (unchanged) carries it, “alongDependence is exactly the clearer's feeding closure (Clearing.dependenceRegion_iff)”. “Checked by inspection, not by a theorem” stays in the snapshot and in history (the entry that added the record and the P40 entry) |
| C10–C11 “At every step the clearer is active and supported, and within this region …; from step two on, beyond the region, the dweller is admitted without the clearer's part and not with it (Clearing.loses_beyond).” | law (witness) | law 7 (“for any levels l without the clearer's part”, the theorem's hypothesis, made explicit; see above) |
| C12 “So a part can continue at every step and close nothing within its dependence while closing what lies beyond it;” | conclusion | counterexamples[0] (“Continuing does not imply closing nothing: …”, unchanged) and the statement (S1) |
| C13 “with the whole as the region there is no loss beyond to speak of (Web.not_losesBeyond_whole).” | law (duplicate of C5) | law 4 (last clause) |
| C14 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (the hypotheses contain no ethical premise; the bound receipts report empty axiom lists) |
| C15 “P56: inclusion is exactly admission within every region at every step at once (Web.includes_iff_within_every): a region's comparison takes the region as an input, while the whole's takes no boundary as an input.” | law | law 2 (second clause); “P56:” → history (the P56 entries) + snapshot |
| L0 “Regions are parameters of the statement, and nothing here models how a center forms or represents one;” | premise (duplicate of H0) + scope | hypotheses[0] (first clause); does_not_show[0] |
| L1 “the whole is the region of all formations of a web, the represented whole;” | premise (duplicate of H0) | hypotheses[0] (second clause) |
| L2 “most of the level theorems are order properties, and the substance is in the clearer's witness;” | scope | does_not_show[1] (“the theorems on the levels of region”; zh unchanged) |
| L3 “the comparison is of admission at each step, with the rest of the exchange fixed;” | premise (duplicate of H2) | hypotheses[2] |
| L4 “that alongDependence matches the extent derived along feeding, first checked by inspection, is a theorem from P40: it is closed under feeding and is exactly the clearer's feeding closure (Clearing.fedClosed, Clearing.dependenceRegion_iff; see feeding-closure);” | completed connection | related entry feeding-closure (unchanged); the declarations are in `Becoming/Feeding.lean`, which this record does not reference, so they are not stated as a law here; P40 → history (the P40 entry, which names Clearing.dependenceRegion_iff) + snapshot |
| L5 “contains no ethical predicate, does not say which criterion should be followed, and licenses no ending of a part;” | standard boundary + non-implication | standard_boundaries: no-evaluation (“contains no ethical predicate”); does_not_show[2] (the rest) |
| L6 “the reading (self, system, whole) and the names are the AI's, pending Ren.” | reading | standard_boundaries: names-provisional; correspondence (R3 and R8 give the reading and the names as the AI's, pending Ren) |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T221720.428753Z): the 46 theorems of Becoming.Admission and the 26 of Becoming.Regions all have empty axiom reports;” | evidence | validation_scope (current bindings, see above); the counts and the receipt 20261013T221720.428753Z stay in the snapshot and in history (the batch 2 entry) |
| V1 “the same receipt covers the package's 91 modules … and 39 inherited modules …” | evidence (counts) | receipt + snapshot |
| V2 “periphery receipt 20261013T095049.338744Z passed.” | evidence | receipt + history + snapshot (every cited module is a core module) |
| V3 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (“core purity verified”); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V4 “The author's counterreview is in §51 of the integration note;” | evidence | validation_scope (“in the integration note”); §51 stays in history (the entry that added the record) and the snapshot |
| V5 “not yet independently reviewed.” | evidence | validation_scope |
| R0–R8 | Ren's words + readings | correspondence (unchanged) |
| N0 “Dependence over several steps is given by the feeding closure (P40, feeding-closure);” | completed connection | related entry feeding-closure (unchanged; the feeding-closure record gives the closure along feeding, within a step and across steps); P40 → history + snapshot |
| N1 “comparison of regions with dependence step by step and in temporal order;” | next step | next_delta (“Compare regions with dependence step by step and in temporal order”) |
| N2 “a model of how a center forms and represents a region;” | next step | next_delta (“model how a center forms and represents a region”) |
| N3 “whether route (b) suffices is Ren's judgment (closure-verdict-meets-axiom).” | next step | next_delta (“Whether route (b) suffices is Ren's to judge (closure-verdict-meets-axiom).”) |
| H0–H3 | premises | hypotheses[0]–[3] (unchanged) |
| X0–X1 | counterexamples | counterexamples[0]–[1] (unchanged) |

Remaining lint findings: the correspondence is over its length guide (en 1258/1200, zh 578/500). It quotes Ren's passage on levels verbatim (272 characters in each language), without which it is within the guide (en 986, zh 306); the remaining sentences are the author's correction, its formal counterpart and the attributed AI reading. It is kept rather than moved out of the record.
