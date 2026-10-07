# Independent review of the finite-window period reduction

7 October 2026. AI-authored counterreview of the general-period continuation of [period selection](PHASE-PERIOD-SELECTION.md). This checks whether the proposed local-language certificate addresses the **same** unknown-phase/unknown-inversion game as `PhasePeriodSelection.knowsWithin`. It supplies a formal implementation premise to the governing ethical programme; it supplies no ethical order or reason to select persistence.

**Assessment:** the mathematical reduction has a coherent route to an arbitrary-period result. Finite-window enumeration is not a bound on cycle length. Its general application still needs the explicit semantic and encoding connections below; computing the finite certificate alone does not prove the original game's arbitrary-period theorem. The review found no counterexample in 1,020 comparisons with the retained solver. Those comparisons are finite corroboration, not a replacement for the connections.

## Exact scope of the reduction

Take a nonempty binary pattern of length `period`, with `period > 0`, and the original starting belief containing **every** phase with both reading inversions. A policy uses only native `advance` and `read` commands and may stop early. Success means every candidate still compatible with its readings is currently at the requested contact value. The target question requires a guarantee for each of the two values, possibly by different policies.

The intended seven-command reduction is justified in these steps:

1. **Remove leading advances only at the full unknown start.** Advance is a permutation of all phases and leaves inversion fixed. Any finite sequence of advances before the first reading therefore leaves the same candidate set. Such a prefix cannot add knowledge or improve a uniform command bound. This argument does not authorize deleting advances after observations have narrowed the belief.
2. **The first read is necessary for a nonconstant pattern.** Before reading, every phase remains possible and both contact values occur, so no stop succeeds uniformly for either requested value. With unknown inversion, either first reading is possible for every initial phase. Conditioning on reading zero leaves exactly inversion equal to the phase's initial contact bit. For the necessary lower-bound direction, it suffices to follow this branch. Its residual budget is at most six; unused budget can be retained as early stopping.
3. **A residual policy sees at most seven positions.** With six commands left, there can be no more than six advances. Encode the initial bit and the next six bits in chronological order, least-significant bit first. The reading at position `p` is `word[p] XOR word[0]` on the normalized branch. The policy's branching and final contact value therefore depend only on this seven-bit word. For periods shorter than seven the encoded words wrap around the pattern; treating all 128 words as the search universe is conservative and does not require all words to be realizable by every cycle.
4. **Stop, advance and read generate success languages.** Stop accepts words whose current bit is the requested value. Advance uses a residual policy at the next position. Read partitions the word universe by the relative observation and takes one residual policy on each part. For the intended recursive calls, `position + residualBudget ≤ 6`; positions outside the seven-bit window are not silently admitted. Taking only maximal languages is legitimate because replacing an accepted language by a superset preserves coverage of the actual cycle's windows. The independent choices for the two read branches justify separately maximizing the restricted languages before their pairwise unions.
5. **Empty beliefs and early stops are retained.** The original `contactKnown` uses a universal test and is true on an empty belief. A read branch impossible for the actual candidate set imposes no requirement to execute it. A policy may stop on that empty branch without changing the other branch's guarantee. The language construction must represent failure on hypothetical words as nonmembership, rather than require its policy to succeed on all 128 words. The semantic module linked below makes the original game's bounded-policy reading explicit.
6. **Complement relates the two targets.** Complementing every word bit exchanges target zero and target one while leaving `word[p] XOR word[0]` unchanged. Thus target-zero success languages are bit-complement images of target-one languages. A cycle satisfying both targets has its entire cyclic-window set inside the intersection of one appropriate language for each target; different windows cannot independently select different global policies.
7. **Pruning cannot remove an actual cyclic window.** A window `w` has a successor `w / 2` or `w / 2 + 64`, and a predecessor `w * 2 % 128` or that value plus one. Every window of a finite nonempty cycle has both witnesses among that same cycle's windows. Simultaneous in/out pruning consequently retains all of them at every round. It need not compute exact strongly connected components: retaining extra graph edges only weakens the exclusion test. Multiple components in a candidate mask are permitted, not silently assumed absent.
8. **The finite output must still be read through the encoding.** An empty joint mask cannot cover a nonempty cyclic-window set. The proposed seven-command output consists of the three windows of repeated `001` and their three complements. Each of those windows has bit zero equal to bit three. General application therefore requires deriving three-step periodicity of the original cyclic word and, with nonconstancy, divisibility of the carrier period by three. This final arithmetic consequence and the concrete Nat-mask membership correspondence must be proved or explicitly marked as remaining work.

The finite search is over local policy languages, not over periods up to some large cutoff. Once all eight connections are proved, its period-independent conclusion can be applied to every admitted finite cycle. Conversely, neither a list of 201 masks nor an empty-axiom proof of equality between computed lists alone supplies those connections.

## Formal contributions and remaining links

[PeriodWindowPruning.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/PeriodWindowPruning.lean) proves the general in/out preservation argument with nine empty axiom reports. It is independent of the moving numerical certificate. The theorem is parameterized by a window encoding, advancement/retreat maps and their two-neighbor adjacency witnesses. It allows arbitrary index and window types, duplicate windows and multiple components. `cyclic_pruning_preserves` handles any finite number of rounds. `early_rounds_preserve_coverage` also permits an early exit: returning an already covering mask is conservative even without an exact fixed-point test.

[PeriodStrategySemantics.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/PeriodStrategySemantics.lean) proves the equivalence between indexed stop/advance/read policies and `knowsWithin` for every belief, including empty beliefs. A direct Lean 4.29.1 check against the full original game module passed all eleven new axiom reports, empty and without warnings; the period-study receipt records the fresh full-closure check separately. This equivalence does not on its own normalize the first read, derive maximal-language coverage, or connect Nat masks to concrete cyclic windows.

The remaining proof links are explicit:

- full-start permutation invariance and removal of any initial advance prefix;
- normalization of a first-read branch to relative observations;
- coverage of every residual bounded policy by the computed maximal-language family, including the bounded-width preconditions of structural mask arithmetic;
- concrete encoding, membership, set inclusion/complement and pruning correspondence for Nat masks;
- the implication from the six allowed local words to the original `repeatsEveryThree` conclusion, retaining nonemptiness and nonconstancy.

These are representational proof obligations. They are not evidence that the independently specified game lacks the proposed lower bound. They also do not authorize claiming the arbitrary-period theorem before those obligations are met.

## Independent correspondence check

[check_period_reduction_review.py](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_period_reduction_review.py) compares the proposed 201 maximal languages with the retained `least_commands` solver. For all 510 binary patterns of lengths one through eight, **including constants**, it checks both requested values at command bound seven. All **1,020 comparisons agree**. Empty/constant cases are therefore not excluded from this finite semantic test.

The [review receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/period-reduction-review.json) preserves the explicit language masks, their provenance and hashes, the checker/solver hashes, per-period comparison counts and any mismatches. The proposed masks are **supplied inputs to this comparison**. This does not count the same enumeration twice as independent evidence of completeness. Its independent content is agreement between finite-window coverage and the pre-existing belief-game solver on the declared domain.

Reproduce from the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_period_reduction_review.py
```

The original solver's receipts, bounded Lean theorems and historical counterexamples remain unchanged. A failure of semantic correspondence, incorrect width bound, omitted possible policy or locally accepted word inconsistent with the claimed three-step conclusion would require revising this reduction. A successful reduction would still be conditional on the original worst-case, both-value inquiry target and its retained-model interpretation.
