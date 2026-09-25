# Declared Views — explicit derived read products (stance, 2026-09-01)

> This decision supersedes the former callback-based projection sidecar. The
> historical architecture review remains in
> [`archive/23-architecture-review-2026-06-30.md`](archive/23-architecture-review-2026-06-30.md).
> [Plan 52](52-compiled-dag-query-planner.md) is the normative implementation
> plan.

## Decision

A declared View is not a primary storage representation. Semantic owners keep
their canonical rows, relations, births, ancestry, visibility, lifecycle, and
change laws. A View is an explicitly authored read product compiled into one
installed logical operator DAG.

The public authoring choice is closed:

- `view.live(...)` executes an installed plan inside one admitted
  `QueryReadFrame`;
- `view.materialized(...)` reads an immutable current generation of an
  installed non-graph plan; and
- a declaration whose compiler-derived requirements include graph traversal is
  live-only and cannot acquire a generation association.

Installation persists one exact chain:

```text
declared access binding
  -> exact installed logical plan
  -> current immutable generation, for materialized non-graph Views only
```

Readers never infer a plan from a name, family, catalog head, source Kind, or
"latest" selection. There is no executable projection callback, compatibility
DTO, fallback reader, dual materializer, or parallel declaration version.

## Ownership and execution

The logical plan owns portable query semantics. Owner-qualified source and
edge capabilities own admission and disclosure. Memory and PostgreSQL own
private physical lowering. The generation builder owns rebuild and atomic
publication of immutable non-graph results.

Live traversal, when released, consumes only Plan 51's admitted projected graph
capability. Views does not receive exact or staged graph access, rebuild owner
adjacency, or create a semantic graph store.

The result contract carries the facts required by the product rather than
reconstructing them in a reader: exact cell identity, tie/item coordinates,
lifecycle, source position, projected value, provenance, contributor law, and
visibility posture.

## Adoption and performance

A View is authored only for a real mapped product. Similar-looking owner reads
remain direct when compiling them would not remove duplication or improve a
measured path.

Materialization is a rebuildable acceleration over the same installed logical
truth, not another semantic model. Incremental maintenance is optional and is
added only for measured operators whose owners expose stable change positions.
Until that evidence exists, full generation rebuild plus an atomic current
pointer is the complete architecture.

Owner-qualified route recipes are likewise optional. They are admitted only
after repeated mapped demand and independent acceptance of every source or edge
lens they expand to. Routes disappear during compilation and never become a
mixed-edge graph or runtime registry.
