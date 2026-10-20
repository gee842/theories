# O2 plan: readings verified or refuted in the limit

Board item O2 (claimed 19 October 2026). Lean is written only after O1 lands (board rule 7). This is an AI-written working plan, revised on paper while O1 waits in the queue.

## Question

O1 states what a finite stretch verifies (the open classes) and what it refutes (the closed classes), and splits every reading into its hull and a remainder that no stretch refutes. Two readings are neither open nor closed:

- settling (`Enough.Settles`: from some step on, the configuration does not change);
- recurrence (`Horizon.Sequences.Recurs`).

No finite record verifies or refutes either of them. The next level is convergence. A method guesses yes or no at each horizon from the record so far, and it converges where its guess is the same from some horizon on (identification in the limit: Gold 1967, Putnam 1965, Kelly 1996). Where do settling and recurrence sit at this level?

## Definitions (on the runs of any process)

- `Method P := Nat → Run P → Bool`.
- `ByRecord m := ∀ k r r', r.AgreeUpTo k r' → m k r = m k r'`: the guess at `k` is fixed by the record up to `k`. A guess that reads the step into `k + 1` is shifted by one.
- `Converges m r b := ∃ n, ∀ k, n ≤ k → m k r = b`.
- `YesRecurs m r := ∀ n, ∃ k, n ≤ k ∧ m k r = true`.
- `LimitVerifies m K := ∀ r, K r ↔ Converges m r true`.
- `LimitRefutes m K := ∀ r, K r ↔ YesRecurs m r`. This is the positive form. Kelly's form is "converges to no exactly off `K`", and the two are classically the same. Constructively, `LimitRefutes` gives "converges to no ⇒ outside". The converse step, from "outside" to "converges to no", is law 8.

## Laws

1. **Structure (no premise).** Suppose `m` is fixed by the record.
   - If `m` limit-verifies `K`, then `K` is the union over `n` of `C n` (from `n` on the guess is yes), and each `C n` is closed: a run adhering to `C n` is in it (as `adheres_passes`).
   - If `m` limit-refutes `K`, then `K` is the meet over `n` of the open readings `O n` (some guess yes at or after `n`), each verifiable.

2. **The finite levels lie within the limit levels (no premise).**
   - A reading of tests (`Passes`, closed) is limit-verified and limit-refuted by "no test failed so far".
   - "Some test succeeds" (open) is limit-verified and limit-refuted by "some test succeeded so far".

3. **Meets and joins.**
   - The meet of two limit-verified readings is limit-verified by the conjunction of the guesses.
   - The join of two limit-refuted readings is limit-refuted by the disjunction.
   - The other two combinations use dovetailing. Constructively they reach `¬¬` convergence only: finding where the guess stabilises means deciding, for each earlier witness, whether it ever fails. State the `¬¬` form, and state the outright form under LPO if the proof is short.

4. **Settling.** Configurations must be told apart (`DecidableEq S`). With that, the guess "the step into `k + 1` changed nothing" (shifted) limit-verifies `Enough.Settles` exactly, with no premise.

5. **Settling on the free process** (`Enough.Free.process`: two configurations, every step allowed).
   - Settling is not verifiable: the constant run, continued past any horizon by alternation, does not settle.
   - Settling is not refutable: the alternating run, continued past any horizon by staying, settles.
   - Both settling and its complement are dense.
   - Under Markov's principle, no method fixed by the record limit-refutes settling. The proof is a diagonal: build the run that stays while the method says yes and changes while it says no. If the method converges to yes, the run settles. Without convergence, Markov finds a no after every horizon, so the run changes again and again.
   - Constructively, any method that limit-verifies the complement leaves this run with neither "settles" nor "converges to yes".
   - Reading: settling is what a method can come to say in the limit and never at a finite stretch. That a run changes again and again cannot be said even in the limit. `LastChange.lpo_iff_settles` is the outright decision.

6. **Recurrence** (Boolean sequences).
   - Recurrence is limit-refuted by the last move.
   - Its positive complement, "from some step on every move is false", is limit-verified by the negated move.
   - Under Markov, no method fixed by the record limit-verifies recurrence. The diagonal plays the negation of the guess.
   - Recurrence thus sits where settling's complement sits: refutable in the limit, not verifiable in the limit, and neither at a finite stretch.

7. **Identification.** Suppose a guess of values `Nat → Run P → V`, fixed by the record, converges on each run to `H r`, and `V` has decidable equality. Then each reading `H r = v` is both limit-verified and limit-refuted, by "the guess is `v`". Identification in the limit decides each hypothesis in the limit. `Learnable.Rests` is this identification along an orbit through the map. The record notes the correspondence; there is no instance theorem unless it is short.

8. **The step from outside to "converges to no".** Take the law that every run outside recurrence has, from some step on, only false moves. That law, asked of every Boolean sequence, implies LPO. Witness: the sequence that marks only the first `true` of a given sequence. It has at most one true, so it does not recur, and the step from which its moves are all false decides whether the given sequence is ever true. Reading: saying in the limit that a run has stopped, from the fact that it does not go on, is locating where it stopped.

## Lean notes

- The diagonal runs are defined by recursion on stages. Stage `k + 1` is stage `k` with the move at `k` set from the guess at `k` on stage `k`'s run; the stage runs are the prefix continued by a fixed move. Then:
  - the diagonal run agrees with stage `k` up to `k` (by induction);
  - `ByRecord` moves the guess onto the diagonal run.
- `if` on `Nat.decEq`, with `if_pos` and `if_neg`, has empty axiom reports in earlier core modules; check this on first use.
- Avoid `simp`, `omega` and `Nat` lemmas that use `propext`.

## Joins

- Modules: O1 (`Verification`), `Horizon` (tests, Markov, `Sequences`), `Enough` (`Settles`, `Free`), `LastChange`, `Learnable`.
- Records:
  - what-a-finite-stretch-verifies (its next step);
  - when-the-runs-of-a-process-settle;
  - the-last-change-of-a-run;
  - learnable-through-registration;
  - scientific-inquiry-foundation (inquiry in the limit: a hypothesis can be honest and decidable in the limit while no finite record bears on it).
