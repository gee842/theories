# Bridge fold: classification data and tools

Working material for [BECOMING-BRIDGE-FOLD.md](../../../history/root-foundation/BECOMING-BRIDGE-FOLD.md), 18 October 2026. Read-only study: nothing here changes Lean, records or receipts.

- [`classification.json`](classification.json): one row for each of the 741 declarations (601 theorems) of the 39 bridge modules: module, line, declaration kind, kind (1, 2, 3) and subkind, whether it reaches a periphery constant, the periphery modules in its statement and in its whole dependency through the bridge, the periphery and core theorems its proof cites, the records naming it in a live field (`history` excluded) and the chapter sections naming it.
- [`periphery-modules.json`](periphery-modules.json): the 67 periphery modules the 39 reach, with theorem counts, how many kind-1 and all bridge declarations reach each, and the live Lean files importing each outside the Becoming package.

## How it was produced

The inputs are main `934f2b43c` (receipt `20261018T093527.497358Z` inputs, unchanged since).

1. `tools/inventory.py` parses the 39 modules named in `check_becoming.py`'s `BRIDGE` list (declaration, namespace, statement and proof text).
2. `tools/BridgeInventoryImports.lean` imports the 39 modules. `scratch_build.py` built it in a scratch tree; all 300 other steps were restored from `~/.cache/becoming-lean`, and only this module and its audit ran. `tools/BridgeMeta.lean`, run with the same Lean (4.29.1) on that tree, writes every constant of the 39 modules with the constants used in its type and its value and the module each comes from.
3. `tools/meta.py` assigns layers: prelude, foundation (`GenerativeCore`, `InquirySufficiency`, `RelationalRenewal`), core (`CORE`), bridge (`BRIDGE`) and periphery (everything else). It then follows each declaration's constants through bridge declarations to the periphery constants it reaches. `tools/feat.py` adds the periphery and core theorems each proof cites, read from the receipt's declaration lists.
4. `tools/cite.py` matches declaration names (the last two components, or the bare name where distinctive) against the records' JSON fields other than `history`, and against the chapter's lines.
5. `tools/classify.py` applies the rules stated in its docstring and in the study's section 2. The kind-2 set, the encodings and the handoffs of the eight bridges are listed by hand after reading the source. The joins are sorted by name pattern and by whether the proof cites a periphery theorem.
6. `tools/tables.py`, `tools/permods.py` and `tools/graph.py` produce the study's tables.

The scripts were run from a scratchpad. Their paths are absolute or relative to that directory, and they are kept as a record of the method, not as a maintained tool.
