# Migration map: alignment-direction-g0-j

Old record sha256 `b50f9d9b48950cdf518a57b8a9669d782a994affc195a2321ead910d72679701`; snapshot `_process/architecture/history/b50f9d9b48950cdf/alignment-direction-g0-j.json`. Schema-2 readability migration (stream M2); documentary only, no claim, premise, status, dependency, related link, proof binding, reference or hash change. G0 and J1–J4 stay explicit in `hypotheses[0]`; normative warrant (the argument), compliance and deployment reliability stay separate items.

| Old text | Type | New place |
|---|---|---|
| claim s1 "With warranted AI correspondence, the practical principles support generative development, correction, transfer and appropriate ending while retaining capability growth's real benefits and losses." | statement of the result | `statement` (verbatim, both languages) |
| hypotheses[0] (inherits G0 and J1–J4; E includes warrant for classifications, protection, undertakings, authority) | premises | `hypotheses[0]` (unchanged) |
| correspondence s1 | correspondence | `correspondence` (unchanged) |
| dependencies[0] (application of practical-judgment-g0-j, with interface) | link | unchanged |
| related[0], related[1] | links | unchanged (see the note below) |
| limitations s1a "The completed result is a direction argument" | status/kind in other words | `kind` argument + `status` reviewed-scoped |
| limitations s1b "it proves neither inevitable compliance" | non-implication (warrant vs compliance) | `does_not_show[0]` |
| limitations s1c "… deployment reliability" | correspondence | `does_not_show[1]` |
| limitations s1d "… nor axiom-free necessity of G0" | scope | `does_not_show[2]` |
| counterexamples[0] (same sentence as limitations, verbatim; a scope boundary with no witnessed case) | duplicate | merged into `does_not_show[0..2]`; `counterexamples` is now `[]`. Its path is the record's `canonical_source`, still hashed. **Judgment for review.** |
| validation_scope s1 "The existing independent review accepts … 46 inherited audits." | evidence | `validation_scope` (verbatim) |
| validation_scope s2 "This turn only registers that evidence." | round narration | `history[0]` ("migrated existing result identity and scope; no new theorem") and the migration history note |
| next_delta s1 | next step | `next_delta` (unchanged) |
| history[0..4] | provenance | `history` (unchanged) |
| overview (title, summary, evidence) | README summary | `overview` (unchanged) |
| study §1 (G0 → comparison → requirements → AI direction; E) | completed connection | `progress[0]` (ALIGNMENT-DIRECTION-INTEGRATION §1) |
| study §3 (constructed AI case: transfer, promised successor, crossed losses) | completed connection | `progress[1]` (§3; Lean names stay in `references`) |

Counts: 7 old sentences or sentence parts outside history, overview and unchanged fields (1 claim, 4 limitation parts, 2 validation_scope) plus 1 duplicate counterexample. Destinations: statement 1, kind/status 1, does_not_show 3 (+1 duplicate merged), validation_scope 1, history 1; progress 2 anchored lines name the integration study's completed sections. Standard boundaries: none cited.

**Note for the integrator (not changed here, `related` is protected):** `related[0].detail` still says “§3's statement that J2 is not implied by G0”, while `history[4]` records that the related details were corrected to “J2 does not follow from C (G0 does not constrain ordering)”. The overview evidence carries the corrected wording; the related detail does not.
