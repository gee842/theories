# Exact checks for paid allocation control

The [theory note](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/ALLOCATION-CONTROL.md) proves a useful paid construction episode in a modified version of the shared-renewal reaction framework. The old regulator model and its failed numerical comparisons are unchanged.

[exact_check.py](exact_check.py) and [exact-check.json](exact-check.json) check one finite witness chosen algebraically from a sufficient parameter hierarchy. They use Python's exact rational arithmetic, with no parameter search or trajectory simulation. Running the script overwrites only its result JSON beside the script; the original model is not imported or modified.

The checks cover reaction hazards along the paid success and unregulated failure routes, material/work increments, relevant post-assembly hazards, the finite-rate hierarchy, a rational finite-deadline bound, the common reliability separation and the early-time generator derivatives. The general proof is in the note, rather than inferred from one checked case.

From the common supported preparation with no regulator, the modified gate's joint fresh-capture probability by time 3 is at least 2209/18432, while the absent arm's is at most 6769/110592. The event requires capture machinery and the other catalyst to be present at the first fresh capture. It does not require that they remain until time 3. The gate initially performs worse for this same event, with cubic coefficient -kappa*a*g/3; a later crossover is therefore necessary within the stated class.

The [independent review](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/ALLOCATION-REVIEW.md) records proof checks and the accepted limits. This is a conditional reaction-law theorem, not identified chemistry, a benefit of fuel-responsive switching, a full capability ordering or proof of architecture selection.
