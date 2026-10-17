# U: joining the apart theorems to the base (brief for one batch)

17 October 2026. Ren: "let's first complete the unification", then "finish all before you return". The integrator (the session "Repository completion review and restructure") holds board item **U** and lands everything; you write join modules for one batch of source modules, verify them in scratch, and report. You do not land, commit, run `check_becoming.py`, edit records, or edit any existing file.

## What "apart" means and what a join is

`THEOREM-CONNECTIVITY.py` (in `../../`) classes every spine theorem by whether its statement or proof reaches the base: the Process family (`Generative.Process`, `Generative.Trace`, `Becoming.Frame`, `Becoming.Run`) or the World family (`Becoming.World`, `Becoming.Flow`, `Becoming.Web`). On main, 1,019 of 7,214 spine theorems stand apart; 486 of them are **roots** (used by no other apart theorem). A theorem on the base whose proof uses a root makes that root, and every apart theorem it uses, feed the base.

A **join theorem** states a root's law *of the base*: the source module's vocabulary is read off a run, process, trace, frame, world, flow or web, and the law is then proved through the root. The templates on main are `Becoming/LearnableRuns.lean`, `Becoming/FinerTraces.lean`, `Becoming/ParityReadings.lean`, `Becoming/Runs.lean`, `Becoming/CourseWorlds.lean`, `Becoming/FormedLoops.lean`; the pilot of this item is `pilot/Becoming/SeekingRuns.lean` here. Read at least LearnableRuns and the pilot before writing.

Existing readings to build on (prefer these to new ones):
- a determined law is a process, `Law.process next : Process S Unit`, its run from `s` is `Law.run next s`, and every run of it is its orbit: `Branching.law_run_state`;
- any sequence read along a run: `r.state : Nat → S` for `r : Run P` of any process `P` (a law about every sequence `g : Nat → S` holds of every run's configurations);
- a run read as a world: `Run.world`, `Frame.world`, `Frame.configurations`, `World.run`, `World.run_world` (Runs, Unfolding);
- a history fixes its law: `Shown`, `Shown.run`, and families of histories holding their splices are laws (Unfolding, Histories);
- a course of a law of exchange is a world: `ExchangeLaw.courseWorld`, `ExchangeLaw.courseRun`, `carriedWorld` (Runs);
- likeness: `Alike`, `Bisimulation`, `Law.registered`, `Law.alike_iff_sameFuture`.

## Standard (the integrator will reject joins that miss it)

1. **The base object carries the law.** In each join statement the source vocabulary is read off the base object the statement is about (e.g. `Learning.record (course reg r) t` for a run `r`). Never a base binder the statement does not use, never `(_ : Run P) → X`, never a conjunction bundled only to make roots feed. One theorem may cover several roots only where each part is a law of the same base object.
2. **Exact and no stronger than the Lean.** Prefer `↔` restatements; keep every hypothesis the root needs, stated of the base object. A new reading definition (for example a structure's step as a `Process`) is allowed only where it is the evident reading of that structure, and it should come with the theorem that makes it exact (the run of it is the source's sequence; its traces are the source's courses).
3. **Not every root should be joined.** Classify a root you leave apart, with a one-sentence reason, as:
   - `support`: arithmetic or list lemma, or a statement using only the prelude;
   - `logical-strength`: a statement about LPO, WLPO, LLPO, excluded middle or choice only (if the same strength can be stated of every run or world in a meaningful way, join it instead);
   - `model-witness`: a fact about one constructed model (a counterexample or example structure). Join it only where the model reads naturally as a run or world (then state it so, as the pilot does for `Captured`);
   - `restates`: it restates a theorem already on the base (name it).
4. **Pure core.** Import only spine modules (`Becoming.*`, and `GenerativeCore` through them); no Mathlib. Every declaration must have an **empty axiom report**: no `propext`, `Quot.sound`, `Classical.choice`, `funext`. `simp`, `omega`, `decide` on propositions, `rw` with `propext`-based lemmas and `by_cases` often introduce axioms; term-mode proofs, `match`, `congrArg`, `Eq.subst`, `.trans` do not. The audit tells you. No `sorry`, no warnings (unused variables are warnings: the build counts them as unclean).
5. **Names and prose.** New module names say what they state in the core's vocabulary, ending in `Runs` or `Worlds` (or another structural word) and not colliding with an existing module (`ls` the package `Becoming/` first; `LearnableRuns` already exists). Module docstring in English, like the templates: what the source states, the reading used, then bullets naming the theorems; end with "No ethical predicate, ranking or axiom occurs." if true. Theorem docstrings bold the law. Structural words only: no social, financial or dualist names; no claims about Ren. Put the theorems in a namespace named after the module.
6. **Do not edit any existing file**, in the package or elsewhere. If a source theorem seems wrong or a join needs a lemma inside a source module, write the lemma in your join module, or report it.

## Tools

Package: `/Users/ren/theories/experiments/integrated-correction/general-framework/generative-basis/lean/becoming` (Lean 4.29.1 through elan; the checker's cache already holds every current module, so a build compiles only yours).

- Build and audit (from the package folder): `BECOMING_JOBS=2 python3 -B scratch_build.py TREE` where TREE is your batch folder below; `TREE/Becoming/Foo.lean` is module `Becoming.Foo`. The JSON it prints must show `"unclean": []` and `"with_axioms": {}` for each of your modules. Errors are printed above the JSON.
- Measure (from the repository root `/Users/ren/theories`): `python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/development/u-unification/apart_roots.py TREE/apart.json TREE` — overlays your tree and prints the apart count by module; `TREE/apart.json` lists every apart theorem with `root`, `uses` and `used_by`. The starting list is `apart-before.json` in this folder. Run it after your modules build; it takes about 30 seconds.
- Read a root's statement in its source file (`grep -n "theorem NAME" Becoming/*.lean`).

## Deliverables in your batch folder

1. `Becoming/<Name>.lean`, one or more join modules, building clean.
2. `classification.json`: `{"<theorem>": {"module": "...", "category": "support|logical-strength|model-witness|restates", "reason": "..."}}` for every root of your source modules still apart at the end.
3. `REPORT.md` (short, English): the modules written, the theorems by root covered, the readings used, the apart count for your source modules before → after, anything you think is wrong or misplaced in a source module, and anything the integrator must decide.

Work through your source modules in the order given (most significant first). Aim to join every root that has a meaningful reading on the base; classify the rest. Keep proofs short and through the roots.
