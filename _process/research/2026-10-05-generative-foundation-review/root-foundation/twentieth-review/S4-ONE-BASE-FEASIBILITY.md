# One base: scratch feasibility of the twentieth review's step 4

20 October 2026. An AI note (board item S4). It records scratch builds only: nothing was landed, and no core file, record, chapter or generated page was changed. The question was whether the definitional part of [step 4](../BECOMING-TWENTIETH-REVIEW.md#programme--推进次序), which the [synthesis §1](../BECOMING-TWENTIETH-REVIEW.md#1-two-bases--两个基底) and lens [A1, A2](A-FOUNDATIONS.md#21-one-base-question-1), [A §3](A-FOUNDATIONS.md#3-the-minimal-base-question-5) and [B1](B-LEAN-REDUNDANCY.md) inferred to be mechanical, is in fact mechanical. The note answers it for three refactors, alone and combined.

**Base.** Lean sources of main `05ed62b00` (the same as `cf65d331e`, the review's commit), 300 modules in the closure of `Becoming`. The combined run-root tree was rebuilt and re-audited at main `1705fe0d8`, after R23 landed (301 modules, 298 audited, 11,680 theorems).

**Method.** Each refactor was an overlay of changed modules, compiled with the checker's Lean, step keys and shared cache. A census driver compiled the whole closure and kept going past failures. A failing module was recompiled with each erroring declaration's body replaced by `sorry`, so that breakage further down was counted too. Sorried builds were never cached. Each break was then fixed by hand and the tree rebuilt until it compiled. Then [`scratch_build.py`](../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/scratch_build.py) audited every module with the checker's `#print axioms` driver. That audit is a working build, not a receipt: the environment audit, the controls and the prelude-only compile run only in the checker. The patches, the driver, the rewrite scripts and the audit reports are kept on the ref `refs/salvage/s4-one-base-scratch` (an orphan commit, folder `s4-one-base/`; not for landing).

## Result

All three refactors work, alone and together. Every declaration's axiom report stays empty, with no warnings. Test 3 is the only one that needs real proof edits, and they are local.

| Test | Change | Breakage before fixes | Fixes needed | Audit |
|---|---|---|---|---|
| 1. `abbrev Web` | `structure Dependence S F C` moved into `World.lean` (with `universe u`); `abbrev Web F C := Dependence Nat F C`; the structure removed from `Dependence.lean` | 1 module (`Counting`), 2 declarations; the other 22 errors were cascades from them | 2 lines | 297 modules, 11,647 theorems, all empty |
| 2. `World` as a history | `WebAt` moved into `World.lean`; `structure World := (Relatum, history : Nat → WebAt Relatum × Exchange Relatum)`; `World.web`, `World.flow`, `World.move` as definitions; constructor `World.of R L W`; `World.webAt`, `Run.world` restated in `Runs` | 92 construction sites in 17 modules (no longer valid as anonymous constructors); after the scripted rewrite, 10 declarations in 2 modules (`Counting` 8, `Order` 2) | 91 sites rewritten by script; about 15 lines by hand | 297 modules, 11,647 theorems, all empty |
| 3. `Law.*` as abbreviations | `Recurrence` imports `Frame`; `Law.process` (from `Labelled`), `Branching.Reachable/KeepsPossibilities/Returns/Lossless/Merges` and four trace lemmas (from `Branching`) moved into `Recurrence`; `Law.Lossless/Merges/Returns/Reachable/KeepsPossibilities` became `abbrev`s at `Law.process next` | 55 declarations in 17 modules (Recurrence 14, Attraction 13, HexagramLaws 5, Branching 3, Pace 3, 1–2 in each of 12 others) | 5 new unfolding lemmas; about 60 one-term wraps; 5 bridges became `Iff.rfl` | 297 modules, 11,652 theorems, all empty |
| 1+2+3 | all three | none beyond the above | none | 297 modules, 11,652 theorems, all empty |
| Run root | as 1+2+3, but `World.history : Run (everyStep (WebAt R) (Exchange R))`, `World.lean` importing `Frame` | **none** beyond 1+2+3 | none | at `1705fe0d8`: 298 modules, 11,680 theorems, all empty |

### 1. `Web` as `Dependence Nat`: works

- **Field access and dot lemmas resolve.** `w.web.level` and every other field access compile unchanged. So do the `Web.*` lemmas called by dot notation (`W.Supported`, `W.Dependent`, `W.saturated`, …). No proof outside `Counting` needed a change in any of the 297 modules.
- **Dependence laws now reach webs.** A probe module confirmed the gain the review expected: for `W : Web F C`, `W.foo` also finds a `Dependence.foo`, because Lean unfolds the reducible head. So a law stated once for `Dependence S` serves webs at `S := Nat`, and `Web.static` with its six equivalences, `Dependence.along` and `World.web_along` can be restated over one record.
- **The one trap.** Structure-update syntax `{ W with active := … }` elaborates to a term whose type is `Dependence Nat …`, not `Web …`. A type ascription `({ … } : Web _ _)` does not change that, because dot notation reads the type of the elaborated term. So `({ … } : Web _ _).Dependent` looks for `Dependence.Dependent` and fails. The fix is the explicit form, `Web.Dependent ({ … } : Web _ _)`. It was needed twice, in `OnceClosedQueue.dependent_any_activity` and `World.relayQueue` (`Counting`). Any later module that dots off a structure-update web meets the same trap.

### 2. `World` as a history of snapshot and exchange: works, mostly by script

- **The `rfl` identities hold unchanged:** `World.run_world`, `Run.world_webAt`, `Run.world_move`, `World.web_along` and `balancedRun_level`. A world is now literally its history, and `w.web` and `w.flow` are its readings along the step index.
- **Construction sites.** The cost is the places that build a world as `⟨R, flow, web⟩`: 80 `: World := ⟨…⟩` bodies and 11 inline `(⟨…⟩ : World)`, in 17 modules (Counting 19, Space 16, Premises 14, Order 11, Openness 5, Standing 6, Resolution 4, Entropy 3, Sampling 3, Reading 2, Transmission 2, and one each in ExchangePremises, HexagramSequences, Labelled, Listing, Persistence and PlaceTransitionNets), plus one named argument in Order. A short script rewrites all of them to `World.of R flow web`. No proof destructured a world into `⟨R, flow, web⟩`, so none broke on that count.
- **Proofs broken after the rewrite: 10.** A concrete world's `.web` is now rebuilt from its history: `(World.of R L W).web` is `⟨fun t => W.level t, …⟩`. That is definitionally `W` but no longer syntactically `W`. A lemma whose web argument is left to unification (`Web.saturated_dependent _`, `Flow.transmits_saturated _`, `Flow.stutter_*_iff` with the web implicit) can no longer solve that argument through the rebuilt record. Naming the web explicitly fixes each one, and no proof was rethought (Counting: the eight `*_binding` theorems of the lossy, relay, saturated-open, ring, exchanging and shedding queues and rings; Order: `stutter_premises_iff` and `Reorders.laws`, whose one anonymous world became `World.of`). A landing could add `@[simp]`-free `rfl` lemmas `World.of_web`/`World.of_flow` for later proofs.

### 3. `Law.*` as abbreviations at `Law.process`: works, but it is not definitional

- **The bodies are not definitionally equal.** The review's "the bridges become `Iff.rfl`" holds only after a proof step. `Law.Lossless next` is `∀ x y, next x = next y → x = y`; `Branching.Lossless (Law.process next)` is `∀ x y a b t, t = next x → t = next y → x = y`. `Law.Returns` is an orbit period, `∃ p, 0 < p ∧ orbit next s p = s`; `Branching.Returns` is a step followed by `Reach`. `Law.Reachable` is an orbit and `Branching.Reachable` a trace of a given length. So every proof that builds or takes apart the orbit form broke: 55 declarations.
- **The fix is uniform.** Five unfolding lemmas in `Recurrence` are the old bridges read the other way: `Law.lossless_iff`, `merges_iff`, `reachable_iff`, `keeps_iff` and `returns_iff`, the orbit forms. Each broken proof then takes `.mp` or `.mpr` of one of them where it destructures or constructs, about 60 one-term edits with no proof rethought. `law_lossless_iff`, `law_merges_iff`, `law_reachable_iff`, `law_keeps_iff` and `law_returns_iff` (Branching) become `Iff.rfl`. Net theorem count: +5.
- **Order and placement.** `Recurrence` must import `Frame`, which W2's rule forbids today ("this module does not import the frame"). The rule is moot once there is one base. `Law.process` and the trace lemmas move down. Their names are unchanged, but 18 records name them and need their module path re-pointed.
- **Not done here.** The point of B1 is the next step: deleting or one-lining the `Law.*` theorems that have a `Branching.*` twin (23 shared last names). That is proof-free work once the abbreviations stand.

## Run root or World root

At the level of the Lean, **they cost the same**. The run-root variant replaces the history function by a `Run` of the process that admits every step (`everyStep (WebAt R) (Exchange R)`, `⟨fun _ _ _ => True⟩`). It compiled with no edit beyond the combined tree. The `rfl` identities still hold (the step proofs agree by proof irrelevance). What differs is outside the proofs:

- **World root** (`World.lean` imports nothing; World is a bare history, `Run` defined separately in `Frame`). It keeps the README's and the checker's present statement that the import tree starts at `World.lean`. A world is then a run by an `rfl` identity, not by its type, so the measure's `families_reach_each_other` still depends on correspondence statements.
- **Run root** (`World.lean` imports `Frame` and `GenerativeCore`; a world's history *is* a run). The two families meet by definition, which is the review's acceptance test. The `SCOPE` text of `check_becoming.py` (which says the tree starts at `Becoming.World` and that no module free of the labelled process imports the frame) and README:20, `Becoming.lean` and §1/§9 must say so. The checker computes its compile order from the imports, so only its text changes. A small redundancy appears: `w.history` (a run of every step) beside `World.run` (the run of the law the world shows, same states and moves). A landing would derive the second from the first.

*Judgment:* the run root. It costs nothing more in proofs. It makes one base a fact of the types rather than of a theorem, and it is the direction lens A argued for ("law read off the unfolding").

## What a landing would take (estimate)

Proof-level work is done in the scratch and is small. The rest is the usual landing work:

| Part | Modules | Work |
|---|---|---|
| Definitions (tests 1–3, run root) | World, Dependence, Runs, Recurrence, Branching, Labelled | as in the patches; docstrings rewritten (World's "imports nothing" and "not the starting point"; Runs' root paragraph; Recurrence's "does not import the frame") |
| Scripted construction rewrite | 17 modules | rerun the script on the landing tree |
| Hand fixes | Counting, Order (test 2); Recurrence, Attraction, Branching and 14 others (test 3) | as in the patches, about 75 short edits in all |
| Records | 124 of 279 records bind an edited source file; 18 name a moved declaration | rebind by the usual tools; re-point the 18 |
| Text | README:20, `Becoming.lean` header, chapter §1/§9, `check_becoming.py` `SCOPE` | the exact relation (this note's run-root sentence) |
| Checks | — | one checker run (all keys change below `World`; a full core build took under 2 minutes here, cache warm for unchanged leaves), connectivity rerun (acceptance: `families_reach_each_other`) |

So the definitional part of step 4 is **one session**, not the several the programme allows for it. The other parts of step 4 are separate: the inversions of G2, folding the companion modules back (A3/B7), the measure's new class (B8/G3), and Interleavings constructing the `World` (G10). These scratch builds do not test them. Only the fold is made possible by this note's result, not shown by it. The programme puts step 4 after step 3 (names). The definitional change does not depend on step 3's renames. It only shares files with it (35 files edited here), so whichever lands second rebases.

## What this does not show

- That the companion modules fold back with no statement change (A3's "about 40 of 59" is still an inference). Nor that `families_reach_each_other` turns true: the measure was not rerun on a scratch tree.
- Anything about the periphery, which was not built. The bridge modules that read `World` or `Web` from outside the core may have their own construction sites.
- That the proofs repaired here are the best ones. Each was repaired with the least change, not rewritten.
