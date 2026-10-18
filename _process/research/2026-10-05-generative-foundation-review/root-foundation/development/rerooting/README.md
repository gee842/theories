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
