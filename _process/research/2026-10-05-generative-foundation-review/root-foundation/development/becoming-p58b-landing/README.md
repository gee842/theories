# P58b landing kit: exact names for P58's settling lemmas

Provenance for the P58b landing (study §90), kept beside the other landings' kits. Ren, 12 October 2026: “be the
integrator from now on, let's adopt these names for now, as long as the proof has the exact meaning”
([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-integrator-and-names.md)).

- `land_p58b.sh`: the landing run in a scratch worktree (patch, both checkers, spec, documents and records, inventory,
  re-pointed scopes, hash refresh, this kit, generators, checks). Commits nothing.
- `lean_p58b.py`, `wrap_p58b.py`: the six renames, the docstrings and `stop_unrefuted_iff` in Space, Openness and
  Decidedness; then the rewrapping of lengthened lines (three joined lines were fixed by hand before the checker run).
- `p58b_spec.py`: the repoint spec and module counts from the new receipts against HEAD's.
- `p58b_docs.py`: chapter, Lean README, unification plan, inventory name map and the classification of P64–P68's four proof-only theorems, reading entry, study §90 and its English
  block, and the two records.
- `p58b_zero.py`: the zero-premise plan's count of what still uses decidedness, from the regenerated inventory page
  (P64–P68 added four proof-only theorems, classified in `p58b_docs.py`).
- `p58b_refresh.py`: reference hashes for files this landing changed, only where the record was current at HEAD.
- `repoint.py`, `modcounts.py`: the shared validation-scope tools, as used by earlier landings.

AI-authored tooling; the names and the reading of Ren's condition are the AI's, pending Ren.
