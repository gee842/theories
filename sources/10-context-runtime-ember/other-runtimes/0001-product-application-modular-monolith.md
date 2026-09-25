# 0001 — Product Application Modular Monolith

Status: accepted

Date: 2026-08-04

## Context

The seed must support rapid product iteration, strong internal boundaries, one
transactional source of truth, simple local development, and reliable agent
feedback. Starting with multiple network services would add deployment,
consistency, discovery, observability, and failure complexity before workloads
or ownership justify it.

The architecture must also be honest that some future workloads—such as a
storage engine or high-frequency simulation—may not fit the application
runtime.

## Decision

Begin as a modular monolith:

- One API application.
- One React web application.
- One PostgreSQL database.
- Feature-oriented internal modules.
- One-way dependency rules.
- One composition root for live application capabilities.

The repository is explicitly a product-application platform and control plane,
not a universal data-plane runtime.

## Consequences

Positive:

- Fast local edit/check cycles.
- Ordinary in-process calls and database transactions.
- Easy refactoring while feature boundaries are discovered.
- Lower operational cost.

Negative:

- Internal module discipline must be enforced without network boundaries.
- One deployment shares process-level failure and resource budgets.
- Hot workloads may eventually require extraction.

Deferred:

- Queues, caches, search, microservices, and orchestration platforms.

## Revisit when

- A workload has a measured independent scaling or runtime profile.
- Security or availability requires process isolation.
- Team ownership cannot be supported by module boundaries.
- A component needs independent deployment for a concrete product reason.
