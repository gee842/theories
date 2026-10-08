# Fallible structural inspection and actual correction

The [research integration](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/FALLIBLE-INSPECTION-INTEGRATION.md) states the theory, correspondence, source comparison, counterreview and limits.

Run from this directory:

```sh
python3 check_fallible_inspection.py
```

The checker compiles frozen copies with Lean 4.29.1, audits every explicit declaration in [FallibleInspection.lean](FallibleInspection.lean), checks the retained theorem signatures and compares the [finite runner](FallibleInspectionCases.lean) with a separately expressed Python reference. The [receipt](fallible-inspection-verification.json) binds source, compiler, logs and outputs. No prebuilt `.olean` files are trusted.

Current result: **24 new theorems / 41 declaration audits / 18,684 matched records**. Twenty-two declarations have empty axiom dependencies; the rest use only `propext`, `Quot.sound` and `Classical.choice`. Six inherited modules are rebuilt but not counted as new work.

The filter jointly treats each candidate's factual answer and possible witness failures. Missing reports leave alternatives open. A generic theorem characterizes opposite-answer distinguishability for complete transcripts; a separate sufficient theorem permits faulty withholding. Retention composes with the earlier pooled certificate and actual command completion. The executable pays for inspection, keeps the transcript and uses the remaining capacity for the protected command.

The example includes rival models each certified by its own trusted positions, an effective fifth diagnostic witness that can itself fail, an ineffective fifth witness sharing support, missing testimony, underfunded response and deletion of the actual model by an unadmitted joint cause. Factual/fault coverage, faithful received reports outside admitted faults, stable roster and interval, recorder/monitor support and mandate legitimacy remain premises. This is neither distributed consensus nor empirical validation.

The matched records comprise 2,592 transcript/certificate records, 7,560 costed executions, 6,804 executions with exhaustive arbitrary-report assignments on the small rosters and 1,728 paired-fault transcripts. The arbitrary assignments can yield duplicate healthy-overwritten transcripts. This is a same-author reference comparison, not independent acceptance or a count of independent observations.
