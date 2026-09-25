# 0003 — Contract Boundaries and Command/Query Paths

Status: accepted

Date: 2026-08-04

## Context

API, domain, persistence, and UI representations have different change
pressures. Reusing database or domain objects directly as public payloads would
couple those surfaces. Conversely, forcing every read through a rich aggregate
would add work without enforcing a business decision and would scale poorly for
feeds, search, and reporting.

## Decision

- Put runtime-decodable HTTP contracts in a shared `contracts` package consumed
  by API and web.
- Keep public wire representations distinct from domain and database types when
  their responsibilities differ.
- Route commands through application services and pure domain decisions.
- Permit authorized application queries to use direct typed read adapters that
  decode rows and return public read models without aggregate reconstruction.
- Model behavior and expected failures before freezing their public wire
  representations.
- Begin with one database and process; this is a lightweight path distinction,
  not a CQRS framework or separate read store.
- Produce a language-neutral API description so future non-TypeScript
  components need not import repository source code.

## Consequences

Positive:

- Public compatibility is deliberate.
- Reads avoid unnecessary aggregate reconstruction.
- API and web compile against the same contract.
- Future derived read models have a natural seam.

Negative:

- Some mapping and apparently similar types are duplicated.
- Command and query consistency expectations must be explicit.

Constraints:

- Database rows do not cross the adapter boundary.
- Query shortcuts may not bypass authorization or tenant invariants.
- Separate read storage requires a source, update, staleness, and rebuild model.

## Revisit when

- A second protocol needs a shared language-neutral schema strategy.
- Query volume or availability justifies a derived read store.
- Contract generation constrains necessary product behavior.
