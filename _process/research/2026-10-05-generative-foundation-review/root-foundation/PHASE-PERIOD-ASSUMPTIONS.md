# Phase-period selection: status of its four premises

7 October 2026. AI-assisted continuation of the [phase-period selection](PHASE-PERIOD-SELECTION.md), at the owner's request to leave no unproved premise and no axiom. It follows the [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md). This round was stopped by the coordinator before any premise was fully discharged. This note records what is proved, what was found, and where to resume.

**Formal status:** one new Lean module, [PhasePeriodUniversal.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/PhasePeriodUniversal.lean). It contains 47 declarations and builds with Lean 4.29.1, with no warnings and every axiom report empty (no `propext`, `Quot.sound` or `Classical.choice`). Run the [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_phase_universal.py) to rebuild the closure; its result is in the [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/phase-universal-verification.json). The module proves reduction lemmas only. **None of the four premises is eliminated yet.** The exploration script [explore_phase_universal.py](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/explore_phase_universal.py) reproduces the computations cited below. It is evidence for the plan, not a proof.

| Premise | Status | Lean names |
|---|---|---|
| 1. Lower bounds checked only for periods 3–8 | **Open, partly reduced.** General reduction lemmas proved. The finite local check and the extraction are designed and computationally confirmed, but not yet in Lean. | `knows_sub`, `knows_transfer`, `iter_formula`, `iter_add`, `add_period_mod`, `succ_mod_mod`, `walk`, `bitAt_walk` |
| 2. Retained cell count `1 + 2n` from the Python source | **Open.** Analysed below; no Lean work this round. | none |
| 3. Start (phase, reading inversion) taken as unsettled | **Open.** Analysed below; no Lean work this round. | none |
| 4. Both contact values required | **Open.** Analysed below; no Lean work this round. | none |

## Premise 1: the lower bound for every period

### What is proved (PhasePeriodUniversal.lean)

- **Fewer candidates never make settling harder** (`knows_sub`). This holds for every pattern, period, value and command count: if `knowsWithin` succeeds on a belief, it succeeds on every sub-collection of that belief.
- **Only what is read nearby matters** (`knows_transfer`). Pair the candidates of two beliefs, possibly over different patterns and periods. Suppose each pair has equal inversions and equal contact values at every phase reached by up to `d` advances. Then both beliefs are settled within `d` commands, or neither is.
- **Arithmetic of the advance without `propext`.** The core lemmas `Nat.mod_eq_of_lt`, `Nat.add_mod_right`, `Nat.mod_mod`, `Nat.mod_add_div` and `List.mem_map` all depend on `propext`. The module re-proves what is needed from the fuel-based definition of `Nat.modCore`: `mod_of_lt`, `modCore_reduce`, `add_period_mod`, `add_periods_mod` and `succ_mod_mod`. The closed form of repeated advance is `iter_formula`: `iter n j x = (x + j) % n`. Composition is `iter_add`.
- **Stretches read forward** (`walk`, `walk_length`, `bitAt_walk`). These give the contact values met by successive advances from a phase.

### What was found by computation

- The bounded claim extends at least to period 16. No non-repeating two-valued pattern of period 1–16 settles both values within 7 commands (script, item 1). Periods 9–16 are new.
- **A finite local check suffices.** Let `u` be any word of 14 contact values. Suppose (a) `u[4] = u[7]` and `u[5] ≠ u[8]` (a defect after a non-defect), or (b) `u[j+3] ≠ u[j]` for every `j < 11` (a defect everywhere), or (c) `u` is constant. Then the local game on `u` loses for some value within 7 commands. The local game has phases 0–6, both inversions, and period 14. All 4106 such words lose (script, item 2). With six local phases or fewer, every defect offset leaves some words that do not lose. So seven phases and the offset 4/5 are needed in this scheme.
- **Kernel cost.** Evaluating the local check with `decide +kernel` on the existing `knowsWithin` took 59 s for one sixteenth of the words (the prefix `0000`), measured on Lean 4.29.1. The full check should take about 16 minutes if split into 16 theorems by four-bit prefix. Peak memory is the risk: two concurrent builds of the existing `PhasePeriodSelection` were killed by the out-of-memory killer at 15 GB.

### The proof plan, and the exact resume point

1. **`factor_knows` (next to write).** Let `0 < n`, `x0 < n`, and `phases + d ≤ L`. Suppose `knowsWithin p n v d (unknownStart n) = true`. Then `knowsWithin (walk p n L x0) L v d (unknownStart phases) = true`. Proof: pair each local candidate `(s, b)` with `(iter n s x0, b)`. The pairs map to `unknownStart phases` on the right (a `localPair` map and its `map … Prod.snd` identity were drafted and then removed with the `sorry`). On the left they form a sub-collection of `unknownStart n`, by `iter_lt`, `member_unknownStart` and `member_unknownStart_inv`, all proved. Apply `knows_sub`, then `knows_transfer`. The related contact values follow from `iter_formula` at period `L` (`s + j < L`), from `bitAt_walk` and from `iter_add`. A draft with `sorry` was written and then removed; only the lemmas above it were kept.
2. **Finite checks.** Decide the following by `decide +kernel`, split by four-bit prefix:
   - `allOf (patterns 14) (fun u => !localDefect u || losesWithin u 14 7 7) = true`.
   - The depth-6 check on three-periodic words of length 9 with three local phases. This is cheap: eight words.
3. **Extraction.** Define `D x := bitAt p (iter n 3 x) != bitAt p x` and case on `allOf (upto n) (fun x => !D x)`.
   - **Some defect and some non-defect.** Walk the orbit from a non-defect `z` to a defect `y`, at `k = y + n - z` steps (`iter_formula`, `add_period_mod`). By a discrete intermediate-value step, some `j` has `¬D(iter j z)` and `D(iter (j+1) z)`. Start the stretch at `iter (4n - 4) (iter j z)`. Then `iter_add` and `add_periods_mod` place the defect at offsets 4/5.
   - **Defect everywhere.** Case (b) at `x0 = 0`.
   - **No defect, and `n % 3 = 0`.** `repeatsEveryThree` holds, using `iter_formula` with `x + 3 < 2n`.
   - **No defect, and `n % 3 ≠ 0`.** Write `n = 3q + r` with `r ∈ {1, 2}` (by induction, without `Nat.div_add_mod`). Then `3(q+1) = n + 1` or `3(2q+1) = 2n + 1`. So `iter n 1` preserves the contact value, the stretch at 0 is constant, and case (c) applies.
4. **General theorems.** These follow:
   - `no_pattern_within_six`.
   - `seven_only_by_repeating_three_general`: for every period, `bothKnowableWithin p p.length 7 = true → repeatsEveryThree p p.length = true`.
   - `at_least_seven_general` and `at_least_eight_unless_repeating`.
   - `three_phase_least_guaranteed_draw_general`, without the bound `pattern.length ≤ 8`.

   The bound for repetitions of `001` is reached through the depth-6 check on their period-3 stretch.

What would change the account: a word meeting (a)–(c) whose local game does not lose. The script found none. Another such outcome would be a non-repeating pattern of period above 16 that settles both values within 7 commands. The local check together with the extraction would rule that out, once both are in Lean.

## Premise 2: the retained cell count `1 + 2n`

**Status: open. No Lean work this round.** Analysis made before the stop:

- **Where it enters.** The count matters only for the repetitions of a three-phase pattern (periods `3m`, `m ≥ 2`), which tie period three at 7 commands. For every other period, once premise 1 is general, the gap of at least one command decides alone. The reason: `7·(K + c₃) < 8·(K + cₙ)` whenever `7·c₃ < K`, with `K ≥ 16386` the native interface amount without the cycle cells. With `c₃ = 7` this holds for every retention of the other period, even zero cells. So premise 2 can be narrowed to the repetitions alone.
- **The count is representation-dependent.** `1 + 2n` is the acquisition source's `Machine.cells` for a one-action table. Other retentions of the same cycle are possible. A phase counter with an output list uses `1 + n` cells. A binary phase register uses `⌈log₂ n⌉` binary cells plus the output law. The diagnosis's belief also holds `2·|belief|` cells (`diagnosis.py`, `Diagnoser.cells`), and that grows with `n` as well.
- **Invariant lower bound to prove.** A deterministic retention whose advance follows a cycle of `n` phases distinguishable by its readings must hold at least `n` distinct configurations. With binary cells this means at least `⌈log₂ n⌉` cells, by pigeonhole. For `n = 3m ≥ 6`, that is at least 3, while 2 binary cells suffice for period 3. So "least retention of period 3 < any retention of period `3m`" holds without the table form. What remains supplied is that a cell holds one binary distinction.
- **Necessity to record.** If the repetition `001001` is retained in no more cells than `001`, it ties (`six_cycle_repetition_ties_in_commands`, existing). Its readings never distinguish phase `q` from `q + 3`, so its reduced organization is the three-cycle itself.

## Premise 3: the unsettled start

**Status: open. No Lean work this round.** Analysis made before the stop:

- **What can be derived natively.** Native readings depend on the phase and on `tau xor sigma` only (`readBit`). The silent commands `a` and `reset` produce no observation. Their completion and every non-phase coordinate depend only on coordinates unrelated to the phase, inversion and reset fault. These are `fuel`, `live`, `workspace` and `capacity`, the inherited native names. So two configurations that differ only in phase, inversion parity or reset fault cannot be told apart by anything the activity retains until it reads. A conduct that is a function of retained coordinates and observations must therefore succeed on the whole class. The image of that class under (phase, parity) is exactly `unknownStart`. Proving these lockstep lemmas is routine.
- **Reset with an unsettled fault does not help, for every period.** Restricted to candidates with `broken = true`, `reset` is the identity, which only uses up a command. By `knows_sub` and `knows_one_more`, any guarantee with `reset` available yields one without it. This is the planned general form of the exploratory Python result in the selection note.
- **What stays supplied.** The beginning holds no observation of phase, parity or reset fault. This is "the meaning of a beginning", as in [STARTING-STOCK.md](STARTING-STOCK.md).
- **Necessity to prove (counterexample in hand).** If the start is settled, the selection fails. With a known phase, the pattern `01` reaches either value within one advance, while `001` needs two. Likewise, with a known intact reset, `reset` followed by at most one advance gives period 2 a guarantee of 2 commands, against 3 for period 3. So three is not selected.

## Premise 4: requiring both contact values

**Status: open. No Lean work this round.** Analysis made before the stop:

- **Derivation available from the native gate.** With an open contact, `arrivalAt (output phase) tau false = (output phase != tau)`. So continuing through arrival needs a phase whose contact value is `!tau`. Readings reveal only `tau xor sigma`, never `tau`. Within any class of starts that readings cannot separate, `(tau, sigma) = (0, s)` and `(1, !s)` both occur. Hence:
  - A read/advance conduct that does not know `tau` cannot guarantee arrival at all: both members of the pair end at the same phase, and exactly one of them arrives.
  - A conduct that has settled `tau`, by the two-probe inquiry of `AcquiredContact`, must settle value `!tau`. Taken over the class, this is both values.

  The equivalence `(∀ tau, knowsWithin p n (!tau) d (unknownStart n)) ↔ bothKnowableWithin p n d` is immediate once these native facts are stated. Probing at a phase whose value is not settled fails for some member of the class. Such a probe is a failed conversion: it dissipates ten units (`failed_conversion_dissipates_quantum`) and enacts two interface draws. This connects to `FormedContactCycle.open_arrival_is_native_pattern`.
- **Necessity to prove (counterexample in hand).** If `tau` were settled before the period is fixed, one value would suffice. Then the constant period-1 pattern equal to `!tau` settles it with zero commands (`knowsWithin [false] 1 false 0 (unknownStart 1) = true` when `tau = true`). That beats period three. For a single value, periods 3–8 also tie at 4 commands (`single_value_does_not_select`, existing).
- **What stays supplied.** The inversion `tau` is a port parameter, never changed by a native command (`execute_retains_parameters`). That it is unsettled at the beginning belongs to the same beginning premise as in premise 3.

## Vocabulary

New names and prose use held, enacted, arrived, dissipated and draw. The binder names in the re-proved `Nat.modCore` lemmas avoid inherited market words. The only remaining occurrence is the core lemma `Nat.div_rec_fuel_lemma`, which is cited, not named here.

## Next unresolved bridge

Resume at premise 1, step 1 (`factor_knows`), then the split finite check, the extraction and the general theorems. After that come premise 4 (the arrival-gate derivation and its single-value counterexample), premise 3 (lockstep indistinguishability and the reset-fault reduction) and premise 2 (pigeonhole lower bound for repetitions). The completion conditions of the unified foundation are not met by this round.
