# I4a classification rubric (working document)

Ren, 15 October 2026, chose “Draft the table first” for I4 ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-15-i4-classification-table.md)). The table is read-only. Each row proposes a category; nothing is marked, moved or deleted until Ren decides. Every category is an AI reading.

## Population

Every tracked Lean module whose full module name the spine run does not compile, one row per file stem (598 stems on core receipt 20261015T164401.170999Z: 558 with a live path, 40 only in snapshot folders). `inventory.py`, `connect.py` and `similar.py` compute these signals:
- the run modules each module reaches through imports (core and bridge, inherited, or the foundation only);
- the records citing the module;
- its importers;
- three suggested core modules by shared words.

The suggestions are hints to check by reading, never a classification.

## Categories

| Category | When | Edge recorded |
|---|---|---|
| `joined` | The module already states its results as instances of core laws (it imports `Becoming.*` and proves instance or `*_by_core` theorems), or it is the periphery source that such an instance module reads. | the core declarations instantiated, and the instance module |
| `application` | A concrete construction, model, protocol, example or counterexample. It applies the theory and adds no general law the spine lacks. It stays as it is. | the run modules it builds on, the records citing it, and the core law it exemplifies where checked |
| `earlier-version` | Its main theorem is a special case or an earlier form of a law the spine now states. It must be checked by reading both statements. It is an edge, not a verdict: the module stays. | the spine declarations, with the relation `same`, `spine-generalizes` or `instance` |
| `join-candidate` | A general law the spine does not state: quantified over arbitrary processes, relations or histories, not a fixed construction. | the nearest spine module, and what would be added |
| `artifact` | A review probe, attempt, prototype, landing scratch, executable samples file, audit or driver: evidence of a review or landing. | the module it probes or drives |
| `snapshot` | The file exists only in run, check or development snapshot folders. | the live successor, if one is found under another name |

**Basis.** Each row says how far it was checked:
- `statements read`: the module's main theorems and the spine declarations named were both read;
- `header read`: only the module's header and declaration names were read.

`earlier-version` and `join-candidate` need `statements read`. Otherwise the row is `application` and says what remains to check.

**Where to look on the spine.**
- The core and bridge are in `experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/`.
- The chapter's §9 table lists every module with what it states: `theories/becoming/chapters/THE-THEORY-OF-BECOMING.md`, section “9. 形式脊柱 / The formal spine”.
- Records with their spine aliases are in `theories/becoming/results/records/*.json`; `make research-find QUERY=…` searches them.
- Inherited modules (compiled in the run because the bridge imports them) count as on the spine run, and the bridge reads them. Modules building on them connect through them.

## Row format

One JSON object per line:

```json
{"stem": "…", "path": "…", "category": "…", "spine": ["Becoming.Module.decl", "…"], "relation": "same | spine-generalizes | instance | ",
 "basis": "statements read | header read", "reason_en": "≤ 60 words", "reason_zh": "≤ 75 个汉字"}
```

**Writing.**
- Use structural words.
- Do not use market words (budget, price, cost, pay, credit, profit, …) except as a module's own identifier in backticks.
- Do not quote or attribute anything to Ren.
- Write reasons as readings ("states …", "is a constructed …"), not verdicts on worth.

## Reproducing the table

From the repository root, with `DIR` any scratch folder:

```sh
python3 -B …/integration-i4a/inventory.py DIR/modules.json
python3 -B …/integration-i4a/connect.py DIR
python3 -B …/integration-i4a/similar.py DIR
python3 -B …/integration-i4a/table.py DIR --write
```

`table.py` checks every row and renders `MODULE-CLASSIFICATION.md`. A new spine receipt can add or remove stems; `table.py` then reports the stems without a row, and those rows are read and added before rendering. `themes.json` groups the join candidates (an AI grouping); every join candidate needs exactly one theme.
