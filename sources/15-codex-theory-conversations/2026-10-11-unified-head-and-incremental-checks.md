# Ren: run only what changed, and merge into one head

11 October 2026, Asia/Bangkok. These are six exact user messages and one choice, from the Claude Code conversation in `/Users/ren/theories` (Claude desktop app, session "CPU waste from redundant runs"). Separately labelled AI-authored context follows them. This is not a complete conversation export. Original wording, spelling and spacing are preserved.

## Ren's words

> is everything run when a change is made? I feel a lot cpu are wasted on this, can you fix it please

> ok, make sure this gets optimized - not changed parts don't need to run, only the one necessary runs, then commit

> oh and it is time to ask other agents to merge in, so we have a unified head, with the same improved new efficient work flow, please archive this elegantly

The assistant asked what "archive" should cover. Ren chose the option "Record it in the repo": a dated source note, a link from the directive register, and the rule on the work board.

> actually i change my mind - let all merge and have a unified head first

> continue

> commit and merge all that's useful, discard what should be removed

## Context (AI-authored)

**What ran.** No hook, schedule or watcher started anything. Each session ran the Lean checkers itself, and every run of `check_becoming.py` and `check_correction_inquiry.py` recompiled and re-audited its whole import closure from scratch, whatever had changed. That was about 175 Lean steps for the core and 47 for the Mathlib bridge, each run taking 2 to 15 minutes, and up to an hour when several sessions checked at once. There were about 160 such runs between 8 and 10 October.

**What changed** (`f73c4011`). Each Lean step (compile, axiom audit, signatures, environment audit, controls, prelude-only compile) is keyed by the toolchain binary, its own bytes and the keys of everything it imports. A module's key therefore covers its whole import closure. A step that passed with the same key is restored from a cache shared by all runs and worktrees (`~/.cache/becoming-lean`), so only changed modules and the modules depending on them run. Each receipt lists the steps run and the steps reused, with the run each reused step came from. `BECOMING_FRESH=1` runs every step. The checker's README documents this. Reuse does not change what a receipt certifies: a reused step passed earlier with the same binary on identical inputs, and its log is retained unchanged.

**Verification** (scratch worktrees, outside the landing queue):

- On `86dabd72` the core checker passed with 26 steps run and 161 reused, about 56 CPU-seconds against about 236 for a fresh run.
- A rerun on unchanged sources ran only `lean --version`. Its module records, axiom reports and 175 logs equal the fresh run's.
- `check_correction_inquiry.py` passed fresh with 47 steps; its rerun ran 1 and reused 46, with identical records and logs.
- Editing one module re-keys exactly the modules whose import closure contains it.

**The landings that followed** reused the cache:

| Landing | Core steps run / reused | Bridge steps run / reused |
|---|---|---|
| P46 | 14 / 173 | 6 / 41 |
| P47 | 58 / 133 | 17 / 31 |
| R6 | 14 / 181 | 6 / 43 |

**One head.** The assistant asked the integrator and the other sessions working in this repository to:

1. commit their work;
2. rebase or merge onto the commit with the cache;
3. hand verified work to the [work board's](../../_process/BECOMING-WORKBOARD.md) landing queue;
4. hold new Lean until the head is unified.

The integrator drove the queue in order:

- Landed: P46, P47 with the P51 docstring fold, R6, and `Becoming.Locality` (P48, with law 2 folded in).
- P49 rebased and took the checker after Locality.
- R5 merged the head, Locality included, into its branch and rechecked.
- Group C is queued with the integrator, and Sampling v2 after it.
- Two claims continued during the hold: the P52 inventory, which writes no Lean, and one further localization (census balance), still being drafted.

One session never received the request: it ran in a different permission mode, and the held message expired.

**What was discarded.** The assistant's two scratch test worktrees were removed; they held only test receipts, whose results are recorded above and in `f73c4011`. The two untracked drafts in the main checkout were set aside outside the repository, so that P49 can land. They were older versions of `REGISTRATION-AND-TESTING-PLAN.md` and of the [registration source note](2026-10-11-wisdom-from-registration.md) (on P49's branch `p47-testing` until it lands), and that branch carries the later versions with nothing lost. Other sessions' scratch worktrees were left to their owners; one of them holds unlanded Lean. Git's suggestion to `git prune` loose objects was not followed.

**Readings.** These are the AI's readings:

- "only the one necessary runs" means steps whose inputs changed, together with everything downstream of them;
- "unified head" means main, with every verified item landed through the one queue;
- "archive" means this note, its register entry and the work-board rule.
