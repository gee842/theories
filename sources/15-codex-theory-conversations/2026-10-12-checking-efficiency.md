# Ren: why checking takes so long, and cut the repeated work

12 October 2026, Asia/Bangkok. Two exact user messages from the Claude Code conversation in `/Users/ren/theories` (Claude desktop app, session "Checking performance optimization"). Separately labelled AI-authored context follows them. This is not a complete conversation export. Original wording, spelling and spacing are preserved.

## Ren's words

> why does the checking take so long? i know the machine is busy, but i think we are probably doing a lot unnecessary  checks repeatedly

The assistant reported what it measured (below) and proposed four changes: stop the Lean catalogue from scanning saved copies; have the checkers copy into a run folder only what `main` does not already hold; give scratch builds one shared builder that stores passed steps in the checker cache; and, on Ren's side, close idle processes. It also offered to pack git's loose objects without pruning anything.

> yes, all of them. leave world-starter

## Context (AI-authored)

**What was measured** (about 05:00–05:30 local time). Most of the slowness was contention. The load average was 111 at the first reading and later rose to 207 on 12 cores, and swap held 24.4 of 25.6 GB with about 50 MB of RAM free. A process got a few percent of a core: `git status` took 54 s of wall time for 1.3 s of CPU, and a catalogue check was still unfinished after 25 minutes having used 49 s of CPU. Most of the load came from other work on the machine; the Lean and Python checks were a small share of it.

The repository's own repeated work came from one source. Every run of `check_becoming.py` and `check_correction_inquiry.py` wrote a run folder holding a copy of every source in the closure, both checker files, the generated audit drivers and every log, reused or not, and the folders were committed. A core run folder held 413 files: 66 source copies, 113 generated drivers (also `.lean` files) and their logs. By then `becoming-checks/` held 102 runs, 254 MB and 11,019 `.lean` files, and `correction-inquiry-checks/` held 3,176 more. Of the 19,870 `.lean` paths the catalogue indexed, 18,763 were saved copies and 604 were working sources. The catalogue read, hashed and listed every one, so each checker run made it stale. Its 27 MB `lean-index.json`, tracked in git, had to be regenerated and committed again; it changed in 12 commits between 11 and 12 October. Scratch builds also ran outside the cache: one session's tree builder reused passed steps but never stored its own, and per-module audits loaded all of `import Lean` (about 430 MB each).

**What changed.**

- The checkers copy into a run folder only the sources and checker files that `main` does not hold byte for byte. The receipt's `source_commit` names `main`'s commit and lists what was copied; every file keeps its sha256 in the receipt. The run folder keeps the drivers and logs of the steps that ran. A reused step's log stays in the shared cache under the key the receipt now lists (`lean_steps.keys`), with the run that first passed it. This replaces the [earlier note](2026-10-11-unified-head-and-incremental-checks.md) that a reused step's log is retained unchanged in each run folder. What a receipt certifies is unchanged: the axiom report of every declaration is in the receipt itself. `LEAN_TIMEOUT` now applies to the core checker as well.
- The Lean catalogue decides the saved-copy role from the path alone, and neither reads nor lists saved copies. A checker run therefore leaves the catalogue unchanged. Every other entry is as before.
- `scratch_build.py` in the Becoming package builds a session's changed or new modules against this checkout with the checker's command, toolchain and step keys. It reuses passed steps, stores the steps that pass, and audits with the checker's own `#print axioms` driver, so a landing run reuses what scratch already built.
- Folders already written stay as they are; nothing was deleted.

**Verification** (in a scratch worktree, before landing):

- A fully cached run of the core checker passed with 1 step run (`lean --version`) and 230 reused, in 25 s. Its run folder holds 3 files: the receipt, the version log and the edited checker, copied because `main` did not yet hold it.
- The periphery checker passed with 1 step run and 57 reused. It copied the five sources that `main` had changed since the worktree was made, which shows the per-file rule at work.
- The catalogue regenerated in 72 s of wall time (13 s CPU) instead of more than 25 minutes, and `lean-index.json` went from 27 MB to 6.5 MB. Leaving saved copies aside, its 1,113 entries match `main`'s; three development files committed since the last regeneration were added.
- The scratch builder restored all 21 steps of an unchanged module from the cache. With a probe theorem added to that module, it compiled the module and its audit once, and the next build reused them. The checker computes the same keys for those two steps.
- `make research-test` passed, including a new test that the catalogue never opens a saved copy.
