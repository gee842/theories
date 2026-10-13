# R5 Entropy landing package

Prepared on 13 October 2026 for Ren's authorized takeover and merging of the Claude branches. This is the already completed R5 work, not a new result or further research.

Source: branch `claude/jolly-pike-140c94`, commit `52ff83a4` (full identity and SHA-256 in [provenance.json](provenance.json)). The exact branch source is preserved at [evidence/Entropy.original.lean](evidence/Entropy.original.lean). The landing source differs only by qualifying four colliding list helper names under `EntropyLists`; it retains: **185 theorems, 233 declarations**, importing `Becoming.Resolution` and `Becoming.Recurrence`. Its historical consolidated receipt is `20261011T170859.998618Z`; a new integrated check is required before the current record can claim success. Original prose, record history and proof evidence remain in the branch's Git history. The untracked check folder in the old worktree is retained there.

The package owns only this directory. The preparer has not run Lean or the consolidated checkers, edited canonical records or committed changes. The package-only dry run passed against the current landing tree: all insertions and record construction succeeded, all 233 declarations were bound, reused names resolved, and all three original history entries were retained. That dry run used explicit stand-in receipts and makes no current proof-validation claim. It uses the [shared landing kit](../becoming-landing-kit/kit.py). The integrator can run, with `W` the landing checkout and `S` its next free study section:

```sh
python3 -B "$W/_process/research/2026-10-05-generative-foundation-review/root-foundation/development/becoming-landing-kit/land_lean.py" "$W/_process/research/2026-10-05-generative-foundation-review/root-foundation/development/becoming-entropy-landing" "$W"
```

Then run the consolidated core/periphery checks and inventory. After their fresh receipts cover Entropy, run the kit's `land_docs.py RUN W S BASE`, then `make_records.py RUN W REVIEWED_AT_UTC S`, as for the other packages. `BASE` must identify the reconciled reading-entry source before the chapter edits. The record step also retains R5's historical record entries and inserts its authorization paragraph in the directive register. Use the existing repoint/render/check workflow afterward. If branch ancestry has already introduced that paragraph, reconcile it before running `finish_record.py` rather than adding it twice.

`prepare_package.py` reconstructs the drafts from the retained commit and writes only this package. It records these editorial reconciliations:

- The provisional study section 80, old aggregate counts and unresolved `@PERI@` become landing placeholders; both actual imports are named.
- Exchange-history monotonicity does not need balance; connecting level changes or reversals to the history uses balance. An inherited claim that the history is the *unique* premise-free increasing quantity is removed because the module proves no such uniqueness.
- The checker summary now says that **dissipation**, rather than the first law alone, bounds history by the dissipated amount; it is the loss that does not recur, not the accumulated amount.
- The original result's producer/consumer interfaces, counterexamples, R6 reuse, authored counterreview and open scope remain. No definition body, proof content or public theorem proposition changes. Four generic helper declaration names and their uses are qualified under `EntropyLists` because `Weighted` and `OneStep` occupy the original names; both original and landing hashes are recorded.

The result **decomposes least loss; it does not derive it from fewer hypotheses**. Ren's choice of what “entropy” names, thermodynamic correspondence, coarse-grained entropy, an ordered beginning, and the record as a census relatum remain open at their existing scope. The source uses natural-number amounts at a fixed unit and discrete steps. Merging statements retain their specified determinacy and double-negation limitations. No universal zero-premise foundation or physical second law is claimed by this landing.

Rerun `python3 -B dry_run.py` from this directory to repeat the document/record dry run; it writes only temporary files inside this package and removes them on exit. Land R5 before P58c, so that the later name pass can reconcile imported names and receipt-bound records together.
