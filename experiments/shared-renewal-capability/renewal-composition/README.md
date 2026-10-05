# Exact marked-renewal diagnostics

[The derivation](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/REPEATED-RENEWAL-COMPOSITION.md) supplies the general conditioning and approximation arguments. This directory preserves a small exact diagnostic of their event semantics.

`exact_check.py` uses Python's standard-library rational arithmetic. The saved `exact-check.json` checks four explicitly enumerated time/budget outcomes, equal one-cycle answers with different two-cycle continuations, and five finite uniform-error examples. It records its producer hash and the frozen predecessor inputs. It does not propagate the CF model, execute an RNA model, fit data or prove the analytic general theorems.

Run `python3 exact_check.py` to reproduce and replace the saved record. The original run completed successfully on 5 October 2026. Integration edits alone do not justify a scientific rerun.

`mixing_check.py` and `mixing-check.json` separately check a consequence of the preserved Ledoux author-v6 Poisson/multinomial closure at d=1: the sign of mixing for a co-occupancy assay depends on the joint initial field and density. They preserve the primary-PDF hash, 110 finite splitting identities and directed probability enclosures. This is a new model calculation, not an RNA renewal experiment or a reanalysis of the source dye images. Run `python3 mixing_check.py` only when reproducing that calculation.
