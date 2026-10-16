# P86–P88: one landing run

This wrapper joins the prepared [P86](../becoming-p86-landing/LANDING.md), [P87](../becoming-p87-landing/README.md) and [P88](../becoming-p88-landing/LANDING.md) packages without copying or changing their original Lean/evidence. It creates no separate scientific result. Use the [shared kit](../becoming-landing-kit/README.md) with this directory as `RUN`, after P77–P85 (P88 requires P78 Order), before the final rest-name reconciliation.

For a starting study section `S`, the order is **P86 S**, **P87 S+1**, **P88 S+2**. Package keys and record IDs are merged with collision assertions. `record_deltas.py` passes each individual delta its exact section. The combined catalogue entry is written once; substantive chapter edits stay in their respective subject sections.

Run `land_lean.py` once; run the consolidated core checker and periphery checker once in the queue; then classify the inventory, update totals, apply `land_docs.py RUN W S BASE`, `make_records.py RUN W REVIEWED_AT_UTC S` and the guarded repoint/render/check workflow. The actual successful receipts are mandatory. The wrapper adds two P88 records and extends P86/P87/P88 existing records; a repeated wrapper or recheck is not another result.

The three sources have no named-declaration clashes in the preparer's textual scan of the current core and queued P70/P76–P85 sources; all original preservation hashes remain unchanged. This does not replace the integrated Lean build. Existing scratch compilation artifacts are historical evidence only. Claims retain their named conditions and open boundaries in the individual packages.

## Scope review before integration

On 13 October 2026, the independent Codex agent `entropy_ready` compared the three packages' new prose with the inspected source signatures and reported that the stated scopes match:

- P86: exact conditions for meeting requirements, without support implying activity; possible carrying distinct from actual origin; fixed remaining draw with no balancing path distinct from a reference flow whose activity changes.
- P87: the holding reading is supplied, with the declared decidable-equality and census/no-split/no-merge conditions retained where used.
- P88: finite stretches of named exchanges, the stated natural-number-valued complete invariant, and Boolean footprints with decidable equality where the converse uses it.

This is a documentary scope review, not an independent full proof-body audit or a Lean check. The successful consolidated source-bound checks remain necessary. P86's integration header was corrected to match its need-satisfaction theorems, with its original bytes retained at [Feeding.original.lean](../becoming-p86-landing/evidence/Feeding.original.lean); no formal statement or proof changed.
