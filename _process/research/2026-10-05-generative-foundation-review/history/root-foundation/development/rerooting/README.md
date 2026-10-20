# Re-rooting the spine: data and tools

Working material for [study section 180](../../BECOMING-RENEWAL-READING.md#180-where-the-spines-import-tree-starts-and-a-plan-to-start-it-at-the-one-unfolding-w-step-1) (board item W, step 1), 18 October 2026. This is a read-only study: nothing here changes Lean, records or receipts.

- [`declarations.json`](declarations.json) has one row for each of the 10,529 declarations of the core closure (the three foundation modules and the 184 core modules, counted as `check_becoming.declarations` counts them). Each row gives the module and kind, `full_lts` (the statement or the proof reaches a constant of `GenerativeCore` or `Becoming.Frame`) and `stmt_lts` (the statement does, followed through definitions but not through theorems' proofs).
- [`module-reach.json`](module-reach.json) has one row per module: declarations, how many are free, proof-only or statement-reaching, the same counts for theorems, and the module's class.
- [`plan-batches.json`](plan-batches.json) is the executable spec of batches W1 and W2. For each batch it lists the new modules with their imports, the declarations each module receives (`moved`), the source modules edited, every changed import line before and after (`import_changes`), the modules whose only change is an import (`import_only`), the compile steps whose inputs change, and the records naming a moved declaration. It also gives W2's module set, which is closed under use.
- [`plan-sim.json`](plan-sim.json) is an earlier pass over W1, with a single run module and no cycle check. It is superseded by `plan-batches.json` and kept as a record.

## How it was produced

Inputs: main `fcf68673f`. The Lean sources are unchanged on `08188907c`.

1. `tools/graph2.py` writes the import graph from the checker's `module_index` and `closure` (327 compile steps).
2. `tools/RerootImports.lean` imports `Becoming`. `scratch_build.py` built it in a scratch tree, restoring all 187 imported steps from `~/.cache/becoming-lean`, so only this module and its audit ran. `tools/RerootMeta.lean`, run with the same Lean (4.29.1) and `LEAN_PATH` set to that tree's `.build`, writes every constant of the foundation and core modules (listed one per line in `RerootModules.txt`, from `FOUNDATION + CORE`), with the constants of its type and its value and the module of each. That output (`reroot-meta.json`, 24,321 constants, 13 MB) is regenerable and not kept.
3. `tools/reach.py` computes both reaches for every declaration of the checker's registry. `tools/mods.py` aggregates them by module. `tools/kinds.py` sorts the free theorems by what their statements mention.
4. `tools/free.py` builds the module graph of the free declarations alone. `tools/pairs2.py` lists the free cross-module uses at the bottom of the chain.
5. `tools/sim.py` computes the base's closure and Unfolding's early readings (`sim.json`, in the scratchpad).
6. `tools/sim3.py` runs both batches and writes `plan-batches.json`. It moves every declaration to its batch's module and trims world-side modules' imports to world-side ones. It then adds the imports each module lacks for a constant it uses, checks the resulting graph for cycles, and reports the depths, the modules still reaching `Frame` and the affected compile steps. `tools/sim2.py` is the earlier pass that wrote `plan-sim.json`.

The scripts ran from a scratchpad and take its path as their argument. They are kept as a record of the method, not as a maintained tool. Rerun them on the rebased tree before W1 lands.

## W2 as implemented (19 October 2026)

W2 was planned again on main `d22626bf0` ([study 180.14](../../BECOMING-RENEWAL-READING.md#18014-w2-as-implemented)), and its kit is in [`w2/`](w2/):

- `tools/w2_plan.py SCRATCH [options]` reads `reroot-meta.json`, the checker's import graph (`graph.json`) and the registry of the current receipt (`registry.json`), and writes `w2-plan.json`: the split modules and their reading targets, the moves, every changed import line, and the modules that lose the labelled process. Its options for this landing are in [`w2/plan-args.txt`](w2/plan-args.txt): `--keep` sends a module's few free-side declarations to a free-side host, `--with` moves a free declaration with the readings that alone use it, and `--put` chooses a reading target.
- [`w2/w2-move.json`](w2/w2-move.json) is the move plan for `tools/move_decls.py`: moves, the new module's header and imports, section headings, source order, and the targets that receive at their end. [`w2/ranges.tsv`](w2/ranges.tsv) holds the declaration ranges from [`w2/RangeDump.lean`](w2/RangeDump.lean) on `d22626bf0`. Dump them again on the landing tree.
- `tools/w2_apply.sh PACKAGE w2-move.json ranges.tsv w2-plan.json` applies the edit: `move_decls.py`, then `apply_imports.py`, then `tidy_scopes.py` (it drops `open Generative` and labelled-process binders where the closure lost them, and removes emptied sections), then `w2_notes.py` (the docstring notes) and `w2_register.py` (the new module in the core list, the scope text and the root).

At landing (19 October 2026, main `8c9359c34`) the plan, the move plan and the ranges were made again on the landing tree: `--new=Becoming.JointPlans` adds an empty module that a `--keep` may host, and five more mixed modules are divided (study 180.14, "Replayed at landing"). The scratch inputs (`reroot-meta.json`, `graph.json`, `registry.json`) are regenerable and not kept. `tools/w2_landing_move.py` extends the move plan to the new moves. After `rebind_w.py`, `tools/w2_alias_bind.py` keeps two aliases elaborated only by the retired `Becoming.Bridge` bound to a receipt that elaborated them, and `tools/repoint_drift_w2.py` re-points the six records whose cited chapter lines W2 rewrote; `tools/readme_imports.py` checks the package README's sentence of direct imports against the import graph.
