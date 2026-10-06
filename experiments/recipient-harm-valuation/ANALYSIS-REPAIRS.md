# Implementation repairs and source discrepancies

6 October 2026. The first producer run stopped during the summary cross-check because the CSV uses the literal `NaN` for an undefined percentage. Passing this string to the exact rational parser raised an error. No result file was written or result aggregate displayed. The first implementation and its hash are preserved in [review-history/summary-nan/preservation.json](review-history/summary-nan/preservation.json).

The repair maps empty or `NaN` summary percentages to an explicit unknown value, retaining the raw text in the audit. It does not turn them into zero, alter trial codes, change the protocol, or remove an animal. All trial-derived outcomes and cohort definitions are unchanged. Unknown-percentage agreement is checked separately from numeric rounding agreement.

The final source-summary audit retains every mismatch with the independently reconstructed trial counts. A mismatch is evidence about the released representations; it is not permission to silently repair an original file or change the primary estimator.
