# Final limits review

5 October 2026. Reviewed `outputs/changing-the-interface.md` against `limits-audit.md`, `check_limits.py`, and `limits-checks.json`. No redundant checks rerun.

**Verdict: conditional pass; one initialization clarification is needed.**

The capacity-3 / dwell-4 sufficiency theorem should explicitly start with a **ready coherent interface, not a partially completed rebuild**. Suggested addition to its setup: “The initial interface is coherent and ready to operate; no rebuild is in progress.” The proof and model agent's stated contract use that initialization. Full reserve and phase-start alone would also describe a state with one rebuilding step pending; without the ready-state premise, that pending switch could create an absent interface and leave too little reserve for the required second switch. The alternative entry condition “starting matched with full reserve” should likewise mean ready to operate.

All substantive mathematics otherwise passes:

- The two-step transition and reserve path use intake-before-final-storage-cap accounting consistently.
- The lower reserve threshold is correctly scoped to completing this supplied two-step reconstruction while remaining operational.
- The universal timing obstruction correctly applies to every permitted controller at capacity 3, including foresight, and counts disjoint completed rebuilds between alternating successful conversions. It does not claim the same threshold for larger capacities.
- The statement that exhaustive histories fail at step 14 agrees with the independent reachable-state computation; the analytical 21-step upper bound is accurately described as conservative.
- The fixed-point operator explicitly ranges over nonempty safe beliefs with a common observation. Its iteration, safety objective, unavailable-action convention, and sensor-change treatment match the proof. The finite-model premise requires all environmental history constraints relevant to future successors to be encoded in the state; this is already compatible with the stated model and evidence.
- The report distinguishes perpetually operating a finite supplied repertoire from generating unforeseen capabilities, and changing physical configuration from defeating all fixed algorithms.
- The sensing-only limitation correctly uses the independently varying current processing bit; histories of earlier guesses cannot reveal the next arbitrary bit.
- The physical continuation condition is kept separate from moral desirability and phenomenal experience.

No additional mathematical correction is requested after explicitly adding ready initialization.
