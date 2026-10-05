# Combined-foundation evidence

5 October 2026. This package contains the new combined-process theorem, finite implementation, exact results, independent checks, comparative-text analysis, and read-only source snapshots. The user-facing reports are delivered separately in the task's `outputs/` directory.

## Reproduce

Use Python 3 and its standard library, from this extracted directory:

```sh
python3 implementation/verify.py
python3 implementation/independent_oracle.py
python3 independent_graph_check.py
python3 cognitive_scope_audit.py
python3 implementation-review-check.py
```

The first command recreates the eight full reachable graphs and producer results. The second independently derives baseline transitions from closed-form period equations without importing the model or producer verifier. The third reads the exported graphs without importing either implementation and recomputes payments, event semantics, and recurrence by a different graph algorithm. The last two inspect the implementation against additional assertions; they disclose their dependence on model imports. Reproduced JSON and report files should match the saved files byte for byte.

`MANIFEST.json` records the SHA-256 of every evidence payload except itself. `source-manifest.json` separately identifies the seven read-only upstream snapshots. Upstream absolute paths are provenance, not required runtime dependencies. No source repository build or modification is needed. Generated `__pycache__` directories are excluded.

## Interpretation

The baseline is a finite synthetic process, with 486 states and 506 transitions. Its six actual events recur on all paths while protection and all payment prefixes hold. The other seven conditions expose failures of the declared mechanisms. This is exact verification of the model, not empirical verification of every domain named by the broad theory.

`combined-process-proof.md` supplies the general arbitrary-state theorem and composition conditions. `implementation-proof-review.md` and `model-scope-review.md` record independent agent reviews and adopted precision repairs. `tradition-integration.md` and `tradition-source-ledger.md` describe the sources' contributions and preserve their differences. `scope-contract.md` records the intended work before the combined model results.

The maintained programme and checker are actual state transmitted through paid handoffs. The phase scheduler, calibration technology, finite grammar and productive auxiliary apparatus remain supplied premises. The public criterion does not change when the actor's evaluator changes. “Competent handoff” denotes actual retained skill/checker transmission; it does not make a corrupted sensor trustworthy. All reviewers and implementations are AI-assisted, not independent human replications or a proof-assistant certification.
