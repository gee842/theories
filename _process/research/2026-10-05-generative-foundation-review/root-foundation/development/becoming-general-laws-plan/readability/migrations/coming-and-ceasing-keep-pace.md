# Migration map: coming-and-ceasing-keep-pace

Old record sha256 `a6d68f6db714db3f18da3a2ac8fdbde6b9d1b28276d703c3998763dc64e396e6`; snapshot `_process/architecture/history/a6d68f6db714db3f/coming-and-ceasing-keep-pace.json`.

Labels number the old English sentences and clauses (split at full stops and semicolons outside parentheses): T title, S statement, C claim, L limitations, V validation_scope, R correspondence, N next_delta, H hypotheses, X counterexamples. The Chinese text of each field goes to the same place as its English counterpart; the old Chinese was read alongside, sentence by sentence. Migration under the open-issues plan, stream F; documentary only, with no change of law, premise, status, proof binding or source hash.

Each law was checked against its Lean statement: `ComesToBe`/`CeasesToBe` (`¬ p t ∧ p (t+1)` and its converse), `Web.change_readings`, `persists` (decidable determination), `Web.supported_of`, `over_stretch`, `family_over_stretch`, `fallen_within`, `rising_recurs`, `Web.falls_need_rises`, `falls_not_recurring_from_floor` and `Becoming.Renewal`'s `falls_not_recurring` (never rising from `T` on), `risen_within` and `falling_recurs` (bounded by `B`), `held_over_stretch`, `keep_pace` (at most `as.length`), `coming_recurs_iff`, `Web.activity_over_stretch`, `Web.arising_recurs_iff` and `Web.unceasing_iff` (decided activity; the last with every formation in one list), `Web.standing_recurs_iff` (no decidability hypothesis), `Accretion.*`, `Attrition.*`, and `Web.unceasing_iff_covering` (one list covering the active formations from some step `T` on, decided activity). None is narrower or wider than the old text.

| Old text | Type | New place |
|---|---|---|
| T0 “Coming to be and ceasing to be keep pace” | title | title (unchanged) |
| S0–S1 “In a finite family, coming to be and ceasing to be keep pace; this needs no premise.” | statement | statement (unchanged) |
| C0 “The following holds of every web, with no premise about it.” | law | law 1 (opening sentence) |
| C1 “A determination comes to be across a step … (ComesToBe, CeasesToBe);” | law | law 1 |
| C2 “a formation arising and ceasing, … are this one change, read of activity, dependence and standing (Web.change_readings).” | law | law 1 |
| C3 “A decidable determination that holds and ceases to be at no later step holds on (persists);” | law | law 2 |
| C4 “a formation supported at one step is supported at another … (Web.supported_of).” | law | law 2 |
| C5 “Over any stretch of steps, an amount at the end with everything it fell … (over_stretch, family_over_stretch).” | law | law 3 |
| C6 “No amount falls below zero, … (fallen_within), and members falling at arbitrarily late steps rise at arbitrarily late steps (rising_recurs): in every unfolding, levels of finitely many conditions that keep falling keep rising (Web.falls_need_rises);” | law | law 4 |
| C7 “for one amount this is Becoming.Renewal's law … (falls_not_recurring_from_floor).” | law | law 5 (with `Becoming.falls_not_recurring`, the Renewal law it names, already a declared reference) |
| C8 “With the amounts bounded, … (risen_within), and rising at arbitrarily late steps needs falling at arbitrarily late steps (falling_recurs).” | law | law 6 |
| C9–C11 “A determination counts as zero or one, so both hold of it: … (held_over_stretch); … (keep_pace); and each recurs exactly when the other does (coming_recurs_iff).” | law | law 7 (with `mark`, the zero-or-one count) |
| C12–C14 “Read of activity, given decidable activity: … (Web.activity_over_stretch); … (Web.arising_recurs_iff); and with finitely many formations, some formation arises at arbitrarily late steps (Web.Unceasing) exactly when … (Web.unceasing_iff).” | law | law 8 (the parenthetical “some formation arises at arbitrarily late steps” is the meaning of `Web.Unceasing`, kept by the declaration and by “arising recurs”) |
| C15 “Read of standing, with no premise at all: … (Web.standing_recurs_iff).” | law | law 9 (with `Web.ComesToStand`) |
| C16 “Finiteness does the work: … (Accretion), … (Attrition).” | law + counterexample | law 10; counterexamples[0], [1] (unchanged) |
| C17 “No ethical premise and no Lean axiom is used.” | standard boundary | standard_boundaries: no-ethical-premise |
| L0 “Contains no ethical predicate;” | standard boundary | standard_boundaries: no-evaluation |
| L1 “stated for the reading across discrete steps;” | standard boundary | standard_boundaries: discrete-steps; hypotheses[0] (unchanged) |
| L2 “finite families are given as lists;” | premise | hypotheses[1] (unchanged: “given as a list, possibly with repetition”) |
| L3 “recurring means occurring at arbitrarily late steps and gives no frequency;” | scope | does_not_show[0] |
| L4 “keeping pace is of counts and says neither which formations arise or cease nor why;” | non-implication | does_not_show[1] |
| L5 “decidability is a hypothesis about activity;” | logical commitment | standard_boundaries: decidability; hypotheses[0] (unchanged) |
| L6 “does not show that ceasing is good or bad;” | standard boundary | standard_boundaries: no-evaluation (“evaluates neither arising nor ceasing”) |
| L7 “does not take formal laws for necessity in reality;” | correspondence | does_not_show[2] (in the fuller wording of R8) |
| L8 “the level at which 生生不息 is read and the names are Ren's.” | names + next step | standard_boundaries: names-provisional; next_delta (last item); correspondence (last sentence) |
| V0 “Successful Lean 4.29.1 consolidated check (20261013T094743.528770Z): the 59 theorems of Becoming.Change (recurring_accumulates added in P30, Recurs.accumulates now proved from it) all have empty axiom reports;” | evidence | validation_scope (module and receipt); count → receipt + snapshot; the P30 note → history (migration note) |
| V1 “the same receipt covers the package's 75 modules …” | evidence | receipt + snapshot |
| V2 “The author's counterreview is in §26 of the integration note;” | evidence | validation_scope (“in the integration note”); §26 → history (migration note) |
| V3 “the ninth independent review (BECOMING-P18B-P23-REVIEW.md) accepts its mathematics, and its corrections are handled in §34 …” | evidence | validation_scope; review file stays in references; §34 → history (migration note) |
| V4 “The checker also verifies core purity: …” | evidence (core purity) | validation_scope (one clause); details → receipt + snapshot |
| V5–V6 “The eleventh independent review (BECOMING-P25B-P29-REVIEW.md) accepts its mathematics, … §42 …; those corrections are not yet independently reviewed.” | evidence | validation_scope; review file stays in references; §42 → history (migration note) |
| V7 “This record's local laws (P57–P61) are in the same receipt, with empty axiom reports.” | evidence | validation_scope (“with this record's local laws”); label P57–P61 → history (migration note) |
| R0 “Ren's proposal: counting the whole space, … (2026-10-08-theory-of-becoming-priority).” | correspondence (Ren's proposal) | correspondence (unchanged) |
| R1 “This result gives a set of laws holding of the whole space: …” | correspondence | correspondence (unchanged) |
| R2 “The one the author finds most contentful: …” | correspondence | correspondence (unchanged) |
| R3–R4 “The author reads this as one formal content of Ren's scope … (an AI argument): …” | reading | correspondence (unchanged) |
| R5–R7 “This is a reading of activity, arising and ceasing being names Ren confirmed (…); whether it is the proposal's generative and degenerative is Ren's to choose (Ren wrote ‘…’, …): …; for the reading as relations see Web.renewing_not_consuming.” | reading + Ren's words | correspondence (unchanged; Ren's words verbatim and attributed) |
| R8 “Nor does this decide the level at which 生生不息 is read (Ren's), does not show that ceasing is good or bad, and does not take formal laws for the deductive necessity of the whole for reality;” | next step + standard boundary + correspondence | next_delta (the level at which 生生不息 is read, Ren); standard_boundaries: no-evaluation; does_not_show[2] |
| R9 “the Chinese terms proposed for ceasing and coming to be are the AI's, and names are Ren's.” | names | correspondence (last sentence, unchanged); standard_boundaries: names-provisional |
| N0–N2 “The exact restatement for every world is this record's Web.unceasing_iff_covering (P60), …; finitely many formations in all is not needed; Web.unceasing_iff is its corollary;” | law | law 11; label P60 → history (migration note) |
| N3 “a complete list of the laws holding of the whole space, with models and countermodels of every premise (plan P22, Becoming.Space);” | next step | next_delta; label P22 → history (migration note) |
| N4 “when a fall is, at its own step, a ceasing to stand (P20 proves that under dissipation rising and falling are one exchange, see rising-and-falling-in-one-exchange);” | next step | next_delta (“P20 proves” → “under dissipation rising and falling are one exchange, see …”); label → history (migration note) |
| N5–N6 “versions with frequencies or proportions; readings not across discrete steps;” | next step | next_delta (unchanged) |
| N7 “the level at which 生生不息 is read (Ren).” | next step | next_delta (unchanged) |
| H0 “Commitments of the representation, not premises about the unfolding: …” | premise | hypotheses[0] (unchanged) |
| H1 “The family is finite, given as a list, possibly with repetition; …” | premise | hypotheses[1] (unchanged) |
| X0 “An infinite family: ever new formations arise with none ceasing, … (Accretion).” | counterexample | counterexamples[0] (unchanged) |
| X1 “An infinite family: formations all active at the start cease one after another while nothing arises (Attrition).” | counterexample | counterexamples[1] (unchanged) |
