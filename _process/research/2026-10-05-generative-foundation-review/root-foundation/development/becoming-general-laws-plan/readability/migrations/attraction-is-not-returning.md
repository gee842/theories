# Migration map: attraction-is-not-returning

Old record sha256 `fb1187b1aa06afad2fc82970b0b4a90ee41d28e119e7494e5b44fdff4780c25d`; snapshot `_process/architecture/history/fb1187b1aa06afad/attraction-is-not-returning.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence.

Each law was read against its declarations in `Becoming/Attraction.lean`, with `Law.orbit`, `Law.process`, `Law.Returns`, `Law.Reachable`, `Law.Merges` and `Law.KeepsPossibilities` in `Becoming/Recurrence.lean` and `Invariant` and `Reach` in `Becoming/Frame.lean`. None states more than the declaration; every condition the Lean takes is kept: the list holding every configuration (laws 7 and 8, as hypotheses[1] says, with `drawn_iff_lost` right to left needing none), decidable equality (laws 6 and 7), the absorbing region and the configuration outside it (law 3), the region the run is in at step n (law 11, `Run.stays`). Symbolic forms in the claim are written in words: `orbit next s (n + k) ≠ s for every k` as “the course is not s at any step from n on”; `Lossless` as “merges nothing” and `KeepsPossibilities` as “keeps every possibility” (`Law.Lossless` is not among this record's references, so law 7 cites `Law.KeepsPossibilities` and the theorems).

| Old text | Type | New place |
|---|---|---|
| T0 “Attraction is not returning” | title | title (unchanged) |
| S0–S3 | statement | statement (unchanged) |
| C0–C4 “Let next : S → S be a determined law on a type S of any kind, with orbit Law.orbit. A region R is absorbing … (Law.Absorbing); s is drawn into R … (Law.DrawnInto); s is drawn … (Law.Drawn); what lies ahead of s … (Law.Ahead).” | definitions | law 1 |
| C5–C7 “What lies ahead is absorbing (…); once the course is in an absorbing region it is in it at every later step (…); s returns exactly where it lies ahead of itself (…).” | laws | law 2 |
| C8 “Lock-in: with R absorbing, ¬ R s and R (orbit next s n), orbit next s (n + k) ≠ s for every k (…), so a drawn configuration never returns (…).” | law | law 3 |
| C9–C10 “The main law, with no premise, no finiteness and no decidability: Drawn next s ↔ ¬ Returns next s (…); an s that does not return is drawn into what lies ahead of it, entering at the first step (…).” | laws | law 4 |
| C11–C13 “The future narrows: …” | laws | law 5 |
| C14–C16 “Merging: …” | laws | law 6 (the period identity a + (a + 1)·b = b + (b + 1)·a kept) |
| C17–C18 “Where a list holds every configuration: being drawn rules out Lossless and KeepsPossibilities (…); with decidable equality, Lossless next ↔ ∀ s, ¬ Drawn next s (…);” | laws | law 7 |
| C19–C20 “Returns next s ↔ ∀ n, Reachable next n s (…), so Drawn next s ↔ ¬ ∀ n, Reachable next n s (…, right to left with no list); every course enters a configuration that returns (…), so …” | laws | law 8 (“There”, i.e. with the list of law 7) |
| C21–C22 “Open witnesses: Drawn Nat.succ 0 ∧ Lossless Nat.succ (…); Drawn Nat.pred 1 ∧ KeepsPossibilities Nat.pred (…).” | laws (witnesses) | law 9; counterexamples[0] (unchanged) |
| C23–C26 “Processes: Absorbing next R ↔ Invariant (Law.process next) R (…); R is absorbing under the move a (AbsorbingUnder); Invariant P R ↔ ∀ a, AbsorbingUnder P R a (…); with R invariant, R t and ¬ R s, ¬ Reach P t s (…);” | laws | law 10 |
| C27–C29 “where a run r is inside an invariant R at step n and outside it at step m, … (Run.locked_in); where every move from step n on keeps R, the run stays in R (Run.stays); … (Run.leaving_needs).” | laws | law 11 (Run.stays with the run in the region at step n, as the declaration's `inside`) |
| C30 “In Ratchet every configuration goes to true: …” | law (witness) | law 12; counterexamples[1] (unchanged) |
| C31–C33 “In Exit the move false keeps the configuration and the move true flips it: …” | law (witness) | law 13; counterexamples[2] (unchanged) |
| C34 “No Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise (the hypotheses hold no ethical premise; the receipts report empty axioms) |
| L0 “The main law is close to definitional: being drawn asks only for some absorbing region, and the region used is the configuration's own course ahead, so it identifies lock-in with not returning and is not an attractor in the classical sense (…);” | scope + correspondence | does_not_show[0] (first part, witness Law.drawnInto_ahead) and does_not_show[1] (second part, kind correspondence, witness Law.Drawn) |
| L1 “the mathematics (eventual periodicity on finite sets, a non-injective map having a point that is not periodic) is reused;” | scope | does_not_show[2] |
| L2 “the main law is here for determined laws only (for every process, necessarily drawn is not returning and possibly drawn allows return: see necessarily-drawn-is-not-returning, P81);” | scope | does_not_show[3] (P81 → the record name, which is the related entry necessarily-drawn-is-not-returning, unchanged; P81 is in history entry 5) |
| L3 “which of two merged configurations is drawn is not chosen, only the double-negation form is stated;” | scope | hypotheses[2] (unchanged, which says the same); law 6 (“both in double-negation form”) |
| L4 “which regions actual unfoldings enter and how deep or wide a basin is are not derived;” | non-implication | does_not_show[4] (“lie outside the theorems”) |
| L5 “escape from beyond the representation is not stated, a determined law having no move or exchange from beyond;” | scope | does_not_show[5] |
| L6 “the witnesses have two configurations;” | scope | does_not_show[6] (“The finite witnesses, Ratchet and Exit, have two configurations”: the open witnesses of law 9 are on the natural numbers) |
| L7 “the links to Capture, Admission and P53 are readings;” | correspondence | does_not_show[7] (P53 → Becoming.Experiment, its module) |
| L8 “the readings are the AI's, pending Ren;” | standard boundary | standard_boundaries: names-provisional; the correspondence keeps “Readings (the AI's, pending Ren)” |
| L9 “contains no ethical predicate;” | standard boundary | standard_boundaries: no-evaluation |
| L10 “not yet independently reviewed.” | evidence | validation_scope (“there is no independent review yet”); next_delta keeps “an independent review” |
| V0 “14 October 2026: the current bytes of Becoming.Attraction are bound to consolidated receipt 20261013T204910.042715Z (passed: …).” | evidence | validation_scope (the binding receipt, without the date; counts in the receipt and the snapshot) |
| V1 “Earlier receipts below checked the same statements under the former names, tabulated in plan section 10.” | evidence (history) | validation_scope (“which checked them under the current names”); the rename table stays in the plan and history entry 23 names it |
| V2 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 47 theorems of Becoming.Attraction …” | evidence | validation_scope (20261013T094743.528770Z binds Becoming.Recurrence and Becoming.Frame, as the proof bindings have it); the count and the list stay in the receipt and the snapshot |
| V3 “the same receipt covers the package's 75 modules …” | evidence (counts) | receipt + snapshot |
| V4 “periphery receipt 20261013T095049.338744Z passed.” | evidence | receipt + snapshot (the record cites no peripheral declaration) |
| V5 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); the closure list and the injEq/propext detail stay in the receipt and the snapshot |
| V6 “The author's counterreview is in §89 of the integration note;” | evidence | validation_scope (“in the integration note”); §89 is in history entry 0 |
| V7 “there is no independent review yet.” | evidence | validation_scope |
| R0 “On 12 October 2026 Ren asked “hows cause–effect system comparing to our theory?” and pasted an account …” | Ren's words | correspondence (verbatim; the date is in history entry 0 and the provenance source) |
| R1 “The AI compared and made five proposals, and Ren answered “Great, let's finish all of them, …”.” | Ren's words | correspondence (verbatim) |
| R2 “This record is the fourth, “attractors and lock-in are merging”, plan item P67.” | provenance + work-item label | correspondence (“This is the fourth, …”); P67 is in history entry 0 |
| R3–R8 readings | reading | correspondence (unchanged) |
| R9 “See §89 of the integration note.” | provenance | history entry 0 (existing: “see §89 of the integration note”) |
| N0 “attraction for processes that are not determined and Captured's rule region as an absorbing region are given by necessarily-drawn-is-not-returning (P81);” | completed connection | history entry 5 (existing: the P81 note that these items are answered); does_not_show[3]; related entry necessarily-drawn-is-not-returning (unchanged) |
| N1–N4 | next steps | next_delta (unchanged wording) |
| H0–H5 | premises | hypotheses[0]–[5] (unchanged) |
| X0–X2 | counterexamples | counterexamples[0]–[2] (unchanged) |
