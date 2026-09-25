# 0002 — Functional Core and Effect Application Shell

Status: accepted

Date: 2026-08-04

## Context

The seed should make refactoring compiler-guided, keep expected failures
explicit, and provide a consistent model for resources, concurrency, retries,
and observability. At the same time, coupling every business value and pure
calculation to one runtime would weaken simplicity and future adaptability.

## Decision

Use:

- Pure TypeScript domain values and decisions with no Effect runtime import.
- Effect application services for dependencies, expected failures, resources,
  async/concurrent operations, and observability.
- Effect adapters and platform integrations at external boundaries.
- Layer assembly only at composition roots and named bootstrap modules.
- Conventional React components by default, with Effect contained in client or
  boundary modules unless a demonstrated frontend need justifies expansion.

Static typing is not treated as proof of all runtime or product correctness.
External values are decoded and risk-based tests cover what types cannot prove.

## Consequences

Positive:

- Domain behavior is easy to reason about and test.
- Dependencies and expected failures remain visible in application types.
- Resource and concurrency policy uses one coherent runtime.
- Pure business rules remain portable.

Negative:

- Mapping is required between pure domain results and Effect errors.
- Contributors must learn a focused Effect vocabulary.
- Application code has a strategic dependency on Effect.

Constraints:

- Do not wrap pure functions in Effect merely for consistency.
- Do not expose Effect service/layer types in language-neutral contracts.
- Quarantine unsafe vendor interop in adapters.

## Revisit when

- Effect prevents rather than improves ordinary feature delivery.
- Upgrade or runtime costs exceed the value of its unified model.
- A separate component has requirements better served by another runtime.
