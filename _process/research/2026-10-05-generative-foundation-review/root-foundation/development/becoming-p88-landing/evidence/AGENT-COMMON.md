# Common rules for the session's subagents (session "Current math core" [1c3084])

You are helping Ren's Theory of Becoming. Ren's word (12 Oct 2026): "move towards 100%". The item you work on is already claimed on the work board (`/Users/ren/theories/_process/BECOMING-WORKBOARD.md`) in the session's name. Do not edit the board or anything in the repository.

## Where you write
- Write only into your own scratch directory, given in your task.
- Do not edit `/Users/ren/theories`, do not commit, and do not run `check_becoming.py` (the consolidated checker) or `make research-*`. Checker runs go one at a time through the landing queue, and the session runs them.
- Never run `git prune` or delete anything outside your scratch.

## Read first
- `/Users/ren/theories/AGENTS.md`.
- `/Users/ren/theories/theories/becoming/chapters/NONDUAL-METHOD.md`: begin from one relational unfolding; no independent subject, object, owner or value type smuggled in by naming.
- The core modules you build on: `/Users/ren/theories/experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/*.lean`. The root is `Becoming.lean`; the layers and modules are listed in its docstring.

## Pure-core rules
Every new theorem must satisfy all of these; this is enforced at landing:
- **Imports.** Only `Becoming.*` modules (and `GenerativeCore`), no Mathlib, no `Std`; Lean 4.29.1 prelude only.
- **Axioms.** Every axiom report must be EMPTY: no `propext`, `Quot.sound` or `Classical.choice`.
  - Avoid tactics that introduce these: no `simp`, no `omega`, no `decide` except on closed natural-number literals, no `funext`.
  - Avoid `Nat.add_right_cancel` from the prelude; use the core's `add_right_cancel (k)` from `Becoming.Dependence`.
  - Prefer term-mode proofs, `match`, `nomatch`, `.trans`, `congrArg`, `Nat.le_trans`, `Nat.lt_or_ge`, and the core's own lemmas. Read how the existing modules prove things and copy their idiom.
  - No quotients. Keep likeness and identity as relations.
- **Forbidden tokens.** No `sorry`, `axiom`, `Classical` or `native_decide`.
- **Shared definitions.** Build on the core's definitions (`World`, `Flow`, `Web`, `Flow.BalancesOn`, `Flow.RunsDownOn`, `Web.StandingCensus`, `Distinct`, `Covers`, `Listed`, `Sampling`, `Tower`, `Law.orbit`, `Frame`, `Run`, …). Do not set up parallel definitions of anything the core already has. Grep before defining.
- **No trailing primes in declaration names** (`foo'`): the checker's parser drops them. Use a descriptive name.
- **Names.** Precise and formal or scientific: no social, financial or rights words, and no dualist words (subject/object, agent/patient, owner) where a structural word exists.

## Building and auditing
1. Materialize main's core into your own tree once:
   `python3 -B /private/tmp/claude-501/-Users-ren-theories/e2a8824b-beaa-4b8e-9f70-f9716e01002c/scratchpad/ztree.py <your-scratch>/tree`
   It reuses the shared cache and normally compiles nothing.
2. Put your new module at `<your-scratch>/tree/Becoming/<Name>.lean`.
3. Compile and audit it:
   `zsh /private/tmp/claude-501/-Users-ren-theories/e2a8824b-beaa-4b8e-9f70-f9716e01002c/scratchpad/mk.sh <your-scratch>/tree Becoming.<Name>`
   It compiles the module, prints errors, audits the axioms of every constant the module declares (it prints `AXIOMS …` lines for any constant with axioms, then `CONSTANTS n`), and greps for forbidden tokens.
4. Done means: no error, no warning, no `AXIOMS` line, and "no forbidden tokens".

The machine is heavily loaded, so compiles can take minutes. Run long commands with `run_in_background` and wait on them. Do not rebuild the whole core; if you change an existing core module in your tree, rebuild only what depends on it.

## Honesty
- State exactly what is proved, with exact hypotheses.
- Separate theorems from readings; readings are the AI's, pending Ren.
- Where something cannot be proved without a premise or a logical principle, say so. Prove it as a boundary (a witness, or an equivalence with a named principle such as excluded middle or LLPO) rather than hiding it.
- A witness counterexample is a valuable result. Do not overclaim.

## Report
Your final message is your report to the session, not the user. It must include:
1. The scratch path of each Lean file.
2. The mk.sh audit output (the `CONSTANTS n` lines and confirmation that there are no `AXIOMS` lines).
3. A list of the main theorems with their exact Lean statements.
4. What each one means, in plain words.
5. What was not achieved, and why.
6. Any existing core module you would need to change, as a patch in your scratch. Avoid changing existing modules unless it is necessary; new modules are preferred.
7. Suggested result-record ids, with titles in the style of the existing records under `/Users/ren/theories/theories/becoming/results/records/`.
