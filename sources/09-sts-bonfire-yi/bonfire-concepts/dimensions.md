# Authored state and context projections

`authoredState[Kind.id]` is the typed read projection of schema-validated state
stored in `yi_kind_state`. Each effective binding owns one state bucket.

Canonical context facts are projected separately:

- `contexts.identity` — path and principal revision;
- `contexts.custody` — holder, quantity, units, and lifecycle;
- `contexts.containment` — parent, slot, and order;
- `contexts.relations` — endpoints and occurrence lifecycle;
- `contexts.authority` — certificate parties and active state.

Generic authored-state mutation accepts only Kind buckets. Use the owning context
operation for transfers, moves, relation lifecycle, certificate revocation, and
Identity changes.

See [Yi](yi.md) and [Authored state and context facts](holdings-authoredState.md).
