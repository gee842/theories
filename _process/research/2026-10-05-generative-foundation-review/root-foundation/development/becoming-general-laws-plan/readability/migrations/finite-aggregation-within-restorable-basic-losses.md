# Migration map: finite-aggregation-within-restorable-basic-losses

Schema 1 → schema 2, 14 October 2026 (Asia/Bangkok), starting from the current law-first record; the [planning draft](../drafts/finite-aggregation-within-restorable-basic-losses.mapping.md) predates the law-first rewrite and served only as a style reference. Old record sha256 `118f5468ef15a9ed1ffa3ea9644de9879940fe3f04d5c44e406f44e4d97e81bf`; exact bytes in [the snapshot](../../../../../../../architecture/history/118f5468ef15a9ed/finite-aggregation-within-restorable-basic-losses.json). [New record](../../../../../../../../theories/becoming/results/records/finite-aggregation-within-restorable-basic-losses.json). Argument: [CROSSED-CLAIMS-ARGUMENT.md](../../../../CROSSED-CLAIMS-ARGUMENT.md) §10–§13.

Each English sentence is listed by field and index (as split by `tools/research/style.sentences`), with its opening words; the long first claim sentence is split into its semicolon clauses (a–g). The Chinese text of each sentence takes the same route as its English counterpart; the old Chinese was read alongside. `L[n]` is `laws[n-1]` counted from 1 as rendered, `H[n]` is `hypotheses[n]`, `DNS[n]` is `does_not_show[n]`, `P[n]` is `progress[n]`, `CE[n]` is `counterexamples[n]`, `VS` is `validation_scope`, `ND` is `next_delta`, all indexed from 0 except laws. Unchanged fields (`id`, `title`, `kind`, `status`, `family`, `canonical_source`, `aliases`, `dependencies`, `related`, `references`, `proof_bindings`, the four earlier `history` entries) are not repeated.

“Labels → history” means the round, section, date or receipt labels are named in this migration’s history note or already in an earlier history entry; the exact sentence stays in the snapshot.

## Claim

| Old | New place |
|---|---|
| claim.0a “On every frame, strict loss matching obeys general laws (Becoming.LossMatching)” | `claim` sentence 1 (“Strict loss matching obeys the laws below on every frame (Becoming.LossMatching)”); `statement` (“strict loss matching laws give its formal content”) |
| claim.0b “a generative extension is a strict loss match by identity, so a commitment making strict matching sufficient for strict priority contains comparison principle C, and not conversely” | L1; “not conversely” is glossed with its witness from §11.3 (the match of A against B₁ is no extension, `a_b1_not_extension`) |
| claim.0c “the commitment is consistent only where matching is asymmetric, and with infinitely many losses …” | L2 (verbatim) |
| claim.0d “with losses listed once, strict matching is a strict order” | L3, with the study’s gloss from §11.3 (`StrictLossMatch.length_lt`: the worse loses strictly more, hence irreflexive and asymmetric) |
| claim.0e “with content read as a class, a strict match exists exactly when …” | L4; the condition “losses listed once” comes from limitations.6, and the one-class case (“within one class, exactly when it loses fewer”, `strictLossMatch_iff_length_of_alike`) is the specialization §11.3 applies to the instance |
| claim.0f “a configuration that loses a support every claim rests on is strictly matched below nothing” | L5, with the theorem’s condition stated as in §11.4 (claims finitely listed; under any content relation) |
| claim.0g “and a claim read at its episode time stays lost when support returns” | L6 second clause; its first clause (`readsAt_iff_settled`) is the companion law stated in §11.1 |
| claim.1 “On these laws FR proposes that, within an independently specified family …” | `claim` sentence 2 (verbatim); `statement` (summary) |
| claim.2 “Where support, burdens and historical conditions persist under scale expansion …” | `claim` sentence 3 (verbatim); `statement` (“where support, burdens and history persist with scale”) |
| claim.3 “This is an additional normative candidate beyond LR’s neighborhood …” | `claim` sentence 4 (verbatim) |
| claim.4 “One repair process is an instance: generated from one start …” | `claim` sentence 5 (“One repair process is an instance (laws 7–9)”); L7 (generation, episodes, counts 3/4/3/2, matches by the counting law); L8 (sufficient matching: one insufficient, three suffice, two against two only a correspondence); L9 (three-access repair disconnecting the backbone) |
| claim.5 “P102 completes two content connections: …” | P[0] (complete-episode domain, anchored at `#complete-episodes-and-relational-remainders`, §12); P[1] (sustained harm, anchored at `#whole-course-comparison-of-sustained-harm`, §13); “P102” → history |

## Limitations (7 sentences)

| Old | New place |
|---|---|
| limitations.0 “P100 treats only the constructed domain where the graver side …; it does not calibrate the preceding arbitrary H.” | DNS[0] (scope); “P100” → “the repair instance”; “the preceding arbitrary H” → “the arbitrary H of FR’s general form” (the H of §10, which “preceding” referred to); label → history |
| limitations.1 “No universal exchange rate, global ranking, minimum sufficient number or final two-against-two verdict follows.” | DNS[1] (merged with limitations.4’s “minimum sufficient number for arbitrary H”) |
| limitations.2 “Consistency with all earlier principles, general FR and zero-substantive-axiom grounding remain open, with no new independent acceptance or empirical calibration.” | DNS[2] (general FR, formal consistency); standard boundary `zero-axiom-target-open`; “no … independent acceptance or empirical calibration” → VS last sentence |
| limitations.3 “This case cannot dismiss CP claims or valid chances outside its warranted scope.” | DNS[3] (verbatim) |
| limitations.4 “P102 completes a scoped account of decomposition and direct whole-course comparison, not a unique natural partition …” | P[0], P[1] (the completed scoped account); DNS[4] (partition, aftereffects); DNS[1] (minimum number for arbitrary H); label → history |
| limitations.5 “Either whole reference may be unavailable; needing an upper bound does not warrant one.” | DNS[5] (verbatim) |
| limitations.6 “The counting law is an exact criterion only where content is read as a class and losses are listed once; …” | DNS[6] (verbatim); its condition also written into L4 |

## Validation scope (9 sentences)

| Old | New place |
|---|---|
| VS.0 “14 October 2026: the current bytes of Becoming.RepairComparison (36 theorems, 65 declaration audits, P100’s original 17 theorems only renamed) and Becoming.LossMatching (34 theorems, 42 declaration audits) are bound to consolidated receipt … (passed: 85 package modules, …; the 86-module core closure compiles from the prelude).” | VS sentence 1 (module counts, empty axiom reports, core closure from the prelude); date, receipt timestamp, package-wide counts and “17 only renamed” → history; the receipt itself stays in `references` and `proof_bindings` |
| VS.1 “Earlier receipts below checked the same statements under the former names, tabulated in plan section 10.” | history (this note, and the rename list of the previous entry); VS sentence 1 (“Frame and GenerativeLossComparison are bound to an earlier receipt”) |
| VS.2 “P96 FR remains a philosophical candidate.” | `claim` sentence 4 (“an additional normative candidate”); `status`; H[3]; label → history |
| VS.3 “P100’s 17 new theorems and 45 source declarations passed the consolidated checker …; 2 changed steps ran and 368 passed steps were reused.” | now within RepairComparison’s 36 theorems and 65 audits (VS sentence 1); the frozen receipt binds Frame and GenerativeLossComparison (VS sentence 1, `proof_bindings`); counts, timestamp and build steps → history |
| VS.4 “Normative sufficiency remains an explicit hypothesis and actual content correspondence is not formally proved.” | first clause: H[5] (SufficientMatching is an explicitly added commitment); second clause: VS sentence 2 (verbatim) |
| VS.5 “Substantive author counterreview adds no independent acceptance; the original eight opportunity theorems and LR review retain their scopes.” | VS last sentence (“Author counterreview; no independent acceptance …”); other results’ scopes → history (and the P96 history entry) |
| VS.6 “All 49 research-infrastructure tests passed; documentary checks certify only record consistency.” | history; the rendered page’s footer states that the page is not a proof receipt |
| VS.7 “P102 adds affirmative philosophical argument, constructed thought cases and author counterreview, directly reusing strict_rejection_transport and strict_improvement_transport without new mathematics, Lean execution, normative axiom or external literature certification.” | VS sentence 3 (“Decomposition and whole-course comparison: philosophical argument and thought cases reusing two transport theorems, without new Lean, normative axiom or external literature certification”); the two theorem names stay in `references`; label → history |
| VS.8 “P100’s 17/45 and historical independent reviews are not recounted as new evidence.” | history |

## Next step (4 sentences)

| Old | New place |
|---|---|
| ND.0 “Complete-episode qualification and the direct whole-course method are complete and not reopened.” | P[0], P[1] (completed connections); “not reopened” (an instruction to later sessions) → history |
| ND.1 “A new numerical threshold for sustained harm requires its specified living/protection courses, …” | ND sentence 1 (stated as the step) |
| ND.2 “General FR, global ranking and zero-substantive-axiom grounding retain their separate scopes.” | DNS[1] (global ranking), DNS[2] (general FR), standard boundary `zero-axiom-target-open` |
| ND.3 “A Hall-type characterization for content not read as a class is an optional further step.” | ND sentence 2 (verbatim) |

## Correspondence (6 sentences)

| Old | New place |
|---|---|
| correspondence.0, .1, .4, .5 | `correspondence` (verbatim) |
| correspondence.2 “P100 first generates the courses through one Process/Run; …” | `correspondence` (“The repair instance first generates …”); label → history |
| correspondence.3 “P102 distinguishes temporal narration, …” | `correspondence` (“The account of decomposition and sustained harm distinguishes …”); label → history |

## Hypotheses and counterexamples

| Old | New place |
|---|---|
| hypotheses.0–3, .5, .7 | H[0]–H[3], H[5], H[7] (unchanged) |
| hypotheses.4 “P100 supplies a repair law, backbone and coverage capacities. …” | H[4] (“The repair instance supplies …”; zh “修复实例的给定修复律 …”) |
| hypotheses.6 “P102 completeness concerns the actual comparison …” | H[6] (“In the account of decomposition and sustained harm, completeness concerns …”; zh “分解与持续损伤说明中的内容完整性 …”) |
| counterexamples.0–3, .5 | CE[0]–CE[3], CE[5] (unchanged) |
| counterexamples.4 “… Filling P100’s recovery gap can supply worsening …” | CE[4] (“Filling the repair instance’s recovery gap …”; zh “修复实例的恢复间隔 …”) |

## Added without new content

- `statement`: a summary of claim.1–claim.3 and claim.0a; the exact wording stays in `claim`.
- `laws[].declarations`: every name is a declaration already listed in `references`; no reference was added.
- `standard_boundaries`: `zero-axiom-target-open` only, replacing the zero-substantive-axiom sentences of limitations.2 and ND.2.
- `progress[].source`: the hashed study `CROSSED-CLAIMS-ARGUMENT.md`, with its existing explicit anchors for §12 and §13.
- `history`: one note for this migration; `text_versions[0]`: the snapshot above.
