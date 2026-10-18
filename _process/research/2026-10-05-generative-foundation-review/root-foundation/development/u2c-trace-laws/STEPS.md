# U2c: the two trace laws U2 flagged as possibly vacuous

Board item U2c, 18 October 2026 (AI working notes; the outcome is in study §167 and D43). The check D43 left open: `ProbeRunsInherited.empty_candidates_trace_fails` and the slow-query half of `slow_trace_misses_deadline` stated only that every trace of their query and the response ends without the command achieved.

**Outcome.** Both traces exist, so neither law is vacuous. Each law now states its trace as a first conjunct, proved by `trace_of_final_ne`: the final situation records the query's answer in its receipt, and the start records none. That reduction goes through only because the query is answered: the slow query draws 3 from a reserve of 20 and takes 3 time steps against a deadline of 12 from time 0, the reuse query draws and takes nothing, and the response always answers. No other statement changed, and nothing in Lean used either law.

**Steps.**
1. The board claim, alone (`9f7296c0d`), then a worktree `.claude/worktrees/u2c-trace-laws` on branch `u2c-trace-laws`.
2. `scratch_build.py` built the edited module against the shared cache (21 theorems, 22 declarations, both laws on `propext` only).
3. Checker run `20261018T142457.232756Z` on `08188907c` passed ([log](checker-u2c.log)). The module's doc sentence was then narrowed: the two listed-situation cases state existence by their form, not through `trace_of_final_ne`. The rerun `20261018T145140.478701Z` passed ([log](checker-u2c-b.log)).
4. F1, G3, and L2 with C1 landed first through the landing queue (board rule 5). The branch kept only the source edits, was rebased on main, and the landing run `20261018T164220.815903Z` on `c64053b9c` passed ([log](checker-u2c-c.log)). It ran one step and reused 1,118, and it is the current receipt. All three run folders are kept.
5. `apply_text.py RECEIPT BASE AFTER [EARLIER]` wrote the receipt into the study note and rewrote the chapter's §9 receipt paragraph. Every module's theorem and declaration counts were checked equal to those of the run the chapter named (L2 and C1's), so the count rows stay. `apply_text.py board RECEIPT` moved the board row to the history file and removed U2c's entry from the queue line.
6. `rehash_refs.py` re-pointed the records that `research.py check --changed-since main` reported as drift, each with a history note.
7. `make research-render`, then research-check, research-links (scoped to the changed Markdown) and research-test.
