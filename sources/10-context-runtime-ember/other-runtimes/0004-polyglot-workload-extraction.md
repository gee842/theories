# 0004 — Evidence-Driven Polyglot Workload Extraction

Status: accepted

Date: 2026-08-04

## Context

TypeScript and Effect are well suited to product applications, I/O-heavy
services, orchestration, and control planes. They are not assumed to be optimal
for storage-engine internals, hard realtime loops, intensive simulation,
specialized compute, or every future data plane.

Forcing an unsuitable workload into the default runtime would be a form of
lock-in, not architectural consistency. Splitting speculative services early
would create distributed complexity without evidence.

## Decision

- Keep workloads in the modular monolith by default.
- Measure latency, throughput, CPU, memory, I/O, and operational independence.
- Extract only a cohesive workload with a demonstrated driver.
- Allow another language/runtime when it materially fits the workload better.
- Communicate through versioned language-neutral contracts.
- Preserve explicit data ownership, idempotency, consistency, failure, and
  observability semantics across the boundary.
- Retain the TypeScript/Effect application as control plane when appropriate.

## Consequences

Positive:

- The foundation can support products larger than one runtime's sweet spot.
- Runtime choice follows evidence rather than ideology.
- Ordinary features retain monolith simplicity.

Negative:

- A polyglot component increases build, deployment, hiring, debugging, and
  compatibility cost.
- Cross-process operations lose ordinary transactions and require distributed
  failure reasoning.

Required extraction record:

- Measured constraint.
- Contract and owner.
- Source of truth.
- Consistency and delivery semantics.
- Deployment, rollback, and observability plan.
- Exit/removal condition.

## Revisit when

- Operational experience shows a different default boundary.
- A specialized workload returns to a profile the monolith can support.
- Contract or deployment cost outweighs the specialization benefit.
