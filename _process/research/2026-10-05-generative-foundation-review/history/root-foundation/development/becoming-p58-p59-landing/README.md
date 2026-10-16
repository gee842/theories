# P58 + P59 landing: decidedness made local; the imbalance as a relatum, proved equivalent first

Ren, 11 October 2026: “give me more context, but i intuitively feel decidability is too dualist, also proved solutions
and their pro/cons”, then “please” to the AI's three suggestions: decidedness made local (P58), the imbalance relatum
proved equivalent before any adoption (P59), and embodiment not read as a definition
([source](../../../../../../sources/15-codex-theory-conversations/2026-10-11-decidability-local-imbalance-relatum.md);
[zero-premise plan §1.4](../../ZERO-PREMISE-PLAN.md)). Claimed on the [work board](../../../../../BECOMING-WORKBOARD.md)
as P58 and P59 by the session “Universal Metaethical Core”; landed in one checker run after P62, as agreed with the
integrator. The readings are the AI's, pending Ren.

The scripts are kept as provenance of the landing, not as tools: they ran once, in order, from the session's scratch
directory (named in `land_p5859.sh`), the Lean patches copying the two new modules from beside them. What they produced is on main: the two core modules, the in-place edits, the
[inventory page](../../DECIDABILITY-INVENTORY.md) with its Lean tool, study sections, chapter and plan edits, records
and both receipts.

| File | What it did |
|---|---|
| `land_p5859.sh` | The landing sequence: both patches, the core checker, the periphery checker, the inventory page, the spec, documents, records, the hash refresh, generators and checks. Commits nothing. |
| `p58_lean.py` | P58's Lean: settling lemmas in `Becoming.Space` and `Becoming.Openness`; the rest theorems re-proved in place with no decision procedure, names kept (`World.rests_covering`, `World.rests`, `World.comes_to_rest`, `World.Finite.comes_to_rest`, `World.rest_few`, `World.premised_rests`, `World.sample_rests`); the new module `Becoming.Decidedness`; root import and summary; checker lists and scope. |
| `p59_lean.py` | P59's Lean: the new module `Becoming.Imbalance`; root import and summary; checker lists. |
| `p5859_spec.py` | Checks the receipts against HEAD (exactly the two new modules; package and closure each one more per module; which modules changed) and writes the values the documents use. |
| `p5859_docs.py` | Study sections (P58, P59, English summary, totals), chapter, Lean README, reading-catalogue entry, zero-premise plan (b2) and status, unification plan rows. |
| `p58_records.py` | Four records extended (space-and-its-parts, continued-change-needs-openness, map-of-premises, laws-at-coarser-steps), three related links, and the new records counts-exist-where-decided, recurrence-without-decidedness and imbalance-as-relatum, each boundary from a witness (the undecided world; the world meeting every premise but balance). |
| `p5859_refresh.py` | Refreshes a record's reference to a file this landing changed only where the stored hash equals HEAD's; any other drift stops the run. |
| `repoint.py`, `modcounts.py` | Shared with the P54 landing: re-point validation scopes to the new receipts; update module theorem counts in records. |
| `board_p5859.py` | Marks P58, P59 and the queue line landed on the work board (a separate commit). |
| `mock_receipts_5859.py` | Dry runs only: fake receipts with run ids in 2099; never used for the landing. |
