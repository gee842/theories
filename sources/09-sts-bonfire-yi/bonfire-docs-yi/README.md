# Yi — engineering documents

Current owners:

- [`@bonfire/core` architecture](../../packages/core/ARCHITECTURE.md) defines
  current bounded-context ownership, dependency direction, and structural
  verification.
- [24](24-projection-stance.md) defines explicit declared Views as derived read
  products over one installed logical plan.
- [00](00-direction.md) and [01](01-frame.md) define the direction and
  conceptual frame.

[Plan 49](49-structural-arc/README.md) is complete on the certified
protocol-162 baseline. Its [handoff](49-structural-arc/HANDOFF.md) is the
starting point for subsequent work.

[Plan 50](50-one-world-facing-sdk.md) is complete at protocol 163 and Core/SDK
0.3.0. Its [handoff](50-one-world-facing-sdk/HANDOFF.md) is the certified
starting point for current work.

[Plan 51](51-state-lineage-transition-spine.md) is the active normative work
order for exact Kind evidence and Yi coordinates, immutable Yi Creation
lineage, one live operation coordinate/provenance projection, and one private
typed graph reader over Creation lineage and principal ancestry. The shared
reader cut is accepted in source and its superseded production walkers are
removed; behavioral parity and performance certification remain open. Only
that two-reader publication proof exposes a narrow projected capability to
Plan 52. Creation and principal state otherwise retain independent feature,
transaction, lifecycle, and release gates. There are never separate exact/
projected graph products or sessions. Phase 2 uses one canonical durable
Occasion reference to the Kinds root interpreter; its digest identifies the
interpreter contract, never a Kind binding. Occasion remains the transition
spine; the
[context transition note](../architecture/context-transition-protocol-plan.md)
is a conditional post-Plan 51 extraction proposal, not a completion gate. The
[typed graph fabric](../architecture/typed-graph-fabric-plan.md) is Plan 51's
graph component. Plan 51 wins conflicts and owns integration and release order.

[Plan 52](52-compiled-dag-query-planner.md) is the dependent compiled-query
plan. It first lowers the existing canonical `ViewsDeclaration`; new syntax is
added only for mapped needs. Portable source family identity is closed through
the contribution's exact Kinds semantic slot and committed binding selection;
it is never treated as an installed binding or resolved by ambient latest.
Its implementation is one-way: exact installation resolution -> immutable
logical plan -> pure oracle -> one private `QueryReadFrame` -> adapter
execution -> immutable non-graph generation where declared. That spine adds no
universal query context, permission cache, or second graph session. Exact
install closure, strict installed-plan decoding/recompilation, memory and
PostgreSQL execution, owner-qualified source/Gate admission, aggregate-specific
contributor channels, exact access-plan associations, full generation rebuild,
and the direct `declaredViews.page/count/has` generation reader are present in
source. The callback projection declaration, reader, subscription, and tables
are removed rather than retained as compatibility paths. The mapped live
installed-View product corpus remains empty; `yi.where` does not invent an
installed coordinate.

Internal live traversal is also present in source, but release waits for Plan
51's two-reader projected graph certification. Materialized declarations and
generation code independently reject traversal before work. Owner-qualified
routes remain absent until repeated mapped demand and independent owner-lens
acceptance; incremental maintenance remains absent until measured operators
and stable owner change positions justify it. Neither plan requires a
universal cross-owner lifecycle graph or broad context migration for symmetry.

The shared [Plan 51/52 status ledger](51-52-implementation-status.md) records
volatile implementation and dependency checkpoints separately from those two
normative plans.

[Plan 53](53-lean-core-and-elegant-sdk/README.md) is the active work order
for a lean, role-explicit Core and one elegant SDK: one Core-owned World
product execution service under both the local and connected paths, one
Authority evaluator and presentation lane, a portable Core root with
role-named host paths, a capability-shaped object-and-verb SDK grammar,
compressed authoring over a committed families registry, dependency-island
entrypoints, Server as adapter, and Std as pure content. It opens at protocol
168 / Core-SDK 0.3.0 and completes at protocol 169 / 0.4.0. Its README
carries the shared laws, phase map, and defect ledger; each numbered file is
one self-contained implementation unit.

The route-era addressing Plans [43](archive/43-clean-slate-addressing-and-portability-plan.md)
and [44](archive/44-address-reset-smart-execution-plan.md) are historical. They
do not define current Kind authoring or representation semantics.

Everything in [archive](archive/) is historical. Live code, tests, the current
Core architecture guide, and the current structure map win conflicts with
historical prose.
