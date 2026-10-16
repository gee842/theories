# Migration map: conditional-foundation-assessment

Old record sha256 `f6f1a702917ff753e310311cda444bb9766a1c95a39b6000ebfbd35719af7fa7`; snapshot `_process/architecture/history/f6f1a702917ff753/conditional-foundation-assessment.json`. Schema-2 readability migration (stream M2); documentary only, no claim, premise, status, related link, reference or hash change.

| Old text | Type | New place |
|---|---|---|
| claim s1 "The existing review assesses the candidate as meeting its original five completion conditions under explicit local laws and normative premises." | statement of the assessment | `statement` (verbatim, both languages) |
| hypotheses[0] | premise | `hypotheses[0]` (unchanged) |
| correspondence s1 "distinguishes joined histories, conditional transport and separate realizations; it is not a proof that every model is one realized world" | correspondence | `correspondence` (unchanged) |
| limitations s1a "It establishes neither universal empirical truth …" | correspondence | `does_not_show[0]` (correspondence) |
| limitations s1b "… exclusive metaphysical necessity, general moral reliability …" | non-implication | `does_not_show[1]` (non-implication) |
| limitations s1c "… nor completed governance" | scope | `does_not_show[2]` (scope) |
| counterexamples[0] (same sentence as limitations, verbatim; a scope boundary with no witnessed case) | duplicate | merged into `does_not_show[0..2]`; `counterexamples` is now `[]` (schema 2 accepts `does_not_show` in its place). Its source path is the record's `canonical_source`, still a hashed reference. **Judgment for review.** |
| related[0], related[1] (axiom-free normative target; core's exclusive necessity) | links to other records | `related` (unchanged) |
| validation_scope s1–s2 | evidence | `validation_scope` (unchanged) |
| next_delta s1 | next step | `next_delta` (unchanged) |
| history[0], history[1] | provenance | `history` (unchanged) |
| overview (title, summary, evidence) | README summary | `overview` (unchanged) |
| claim "The existing review …" (what that review is) | anchored connection | `progress[0]` (FIXED-FINISH-LINE-AUDIT §15, five conditions judged satisfied at stated scope) and `progress[1]` (FOUNDATION-ROOT-ACCEPTANCE, positive requirement-by-requirement verification; internal AI challenges, not external peer review) |

Counts: 9 old sentences or sentence parts outside history, overview and the unchanged related details (1 claim, 3 limitation parts, 1 duplicate counterexample, 1 correspondence, 2 validation_scope, 1 next_delta). Destinations: statement 1, does_not_show 3 (+1 duplicate merged), correspondence 1, validation_scope 2, next_delta 1; progress 2 new anchored lines that name the existing reviews the claim refers to. Standard boundaries: none cited.
