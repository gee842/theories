# Migration map: theory-of-becoming-foundation

Schema 1 → schema 2, 14 October 2026 (Asia/Bangkok). Old record sha256 `5d90f904859febd0e2c9a1f4102e87b18e63c54ffa1174a2270edafea36af485`; exact bytes in [the snapshot](../../../../../../../architecture/history/5d90f904859febd0/theory-of-becoming-foundation.json). [New record](../../../../../../../../theories/becoming/results/records/theory-of-becoming-foundation.json).

Each English sentence is listed; its Chinese counterpart follows the same route. Unchanged fields (`title`, `hypotheses`, `correspondence`, `counterexamples`, `dependencies`, `related`, `references`, `history`) are not repeated.

| Old text | Type | New place |
|---|---|---|
| claim.0 “Establish the deductive necessity of the Theory of Becoming as a whole without added substantive axioms; explain generativity within its manifold, with persistence, … evaluation within the same relational unfolding.” | target | `statement` (prefixed “Target:”; “without added substantive axioms” written “with zero added substantive axioms” so the lead is positive; zh verbatim) |
| limitations.0 “The existing checked results do not yet supply the deduction of the whole claim.” | non-implication (“yet” restates status) | `does_not_show[0]`; “yet” → `status: open` |
| limitations.1 “Failure of a particular generative mode is not by itself a counterexample to Becoming.” | target scope | `not_required[0]` (“Not every becoming need be generative”, the chapter’s wording of the same scope) |
| limitations.2 “Ren’s necessity claim is retained without installing it as an axiom; no impossibility claim is made.” | scope | `does_not_show[2]` |
| validation_scope.0 “Retains finite-history coherence, the operational-order assessment and the 27-theorem restricted control calculation.” | evidence + completed connections | `validation_scope` sentence 1; `progress[0]` (coherence), `[1]` (operational order), `[2]` (control calculation) |
| validation_scope.1 “Section 19 reconciles the completion audit with the whole/manifold scope and assesses the direct passage from inclusion to relational constitution, with primary Hegel passages and author counterreview.” | completed connections + evidence | `progress[3]` (whole/manifold), `progress[4]` (inclusion → relation, Hegel); “primary Hegel passages and author counterreview” → `validation_scope` sentence 2; “Section 19” → `history` (migration note) |
| validation_scope.2 “No new mathematical proof; the full zero-substantive-axiom target remains open.” | evidence + status | `validation_scope` (“This record adds no mathematical proof”); “remains open” → `status: open` |
| validation_scope.3 “The completion audit now cites the Becoming spine’s checked laws, parts and countermodels (P19–P22) as evidence for each row, without discharging the whole deduction.” | completed connection | `progress[5]`; `validation_scope` sentence 1; “(P19–P22)” → `history` |
| next_delta.0 “Establish the passage from determinate articulation to the actual relational constitution of the whole, with its inferential warrant.” | next step | `next_delta` (first clause) |
| next_delta.1 “The Becoming spine now states laws … seven … eight …; what remains is the warrant that every becoming is so representable and that the whole is relationally constituted, not only consistently stated.” | completed connection + next step | first half → `progress[5]`; “what remains …” → `next_delta` (after the colon) |
| next_delta.2 “Particular mechanisms explain modes within Becoming; neither inclusive naming nor universalizing one generative mode supplies the whole deduction.” | non-implication | `does_not_show[1]` |

Progress sources (all hashed references already in the record): `GROUNDING-INFERENCE-AND-PRESENTATION.md` §16–§19 anchors; `BECOMING-FOUNDATION.md#whole-and-manifold` and `#5-completion-audit-and-next-central-inference`. Progress lines 1–3 also draw on the dependency details of `becoming-context-coherence` and `control-coherence-loss` and on the history entries of 9 October (sections 17–18), which stay unchanged.

Destination counts (11 old sentences; a sentence split across fields counts once per field): statement 1; progress 4; does_not_show 3; not_required 1; validation_scope 4; next_delta 2; status 2. Labels (Section 19, P19–P22) are named in the migration history note and kept in the snapshot.

Judgment for review: limitations.1 is typed as target scope (`not_required`) rather than a non-implication, following the chapter (“It must not require every becoming to be generative”). No standard boundary is cited: none of the shared sentences restates a sentence of this record exactly.
