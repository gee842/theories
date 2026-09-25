# Bonfire vocabulary — one word per concept

This table governs every identifier, file name, error message, and doc. One
winner per concept; every loser is banned from new code and swept from old.
History (why each loser existed) lives in docs/yi — never in source comments.

| Concept | The word | Banned synonyms | Notes |
|---|---|---|---|
| The one persisted row | **Yi** | spirit-as-row, entity, record | `Yi` is the row type; "row" is fine as a common noun. |
| The one declarable concept | **kind** | class, cls, type | Applies to identifiers (`deployKind`, `kindPolicyOf`), file names, and error text. `Kind` (authored shape), `KindSpec` (permissive authoring input), `KindRecord` (stored form). |
| Effective Kind bindings on a Yi | **bindings / Kinds** | tags, faces, storage selectors | Kinds owns binding membership and the committed representation plan. |
| A Custody component | **holding** | — | A Yi with holder/quantity/lifecycle facts owned by Custody. |
| Authority instrument | **certificate** | token, claim | Issuer/subject/presenter coverage owned by Authority. |
| Invokable held value | **capability** | item | A Custody asset whose Kind exposes ports; invoke the value Yi directly. |
| Directed social fact | **relation occurrence** | edge, relationship | Endpoint and lifecycle facts owned by Relations. |
| Identity principal | **spirit** | actor, subject | An addressable Yi with Identity-owned principal coordinates that can sign and anchor a subtree. Profile state is carried by the `core:profile` binding. |
| Conferred-authority family | **certificate** | grant (as a family name), delegation (as a family name), attestation (for Authority-issued instruments) | The `core:certificate` at-rest IR (docs/yi/45). `capability/` module = the capability algebra over certificates. Individual certificate flavors may still be called grants in product surfaces. Authority-side successors of split attestation modules speak certificate, never attestation. |
| Taking exclusive dispatch of work | **claim** | lease, lock (for work items), reserve | Automation/Settlement verb: a claimant claims durable work (`ClaimedAutomationWork`). Never a synonym for attestation — a claim is taken, an attestation is vouched. |
| Materializing a Yi | **manifest** | spawn, generic create | Typed product/World commands manifest the complete compiled representation; product helpers may say mint when creating a Custody asset. |
| Ending a public lifecycle | **extinguish** | destruction aliases | Public Custody and Yi APIs and read models use `extinguish` / `extinguishedAt`. |
| Substrate core-kind constants | **CORE_KINDS** | CoreKinds, CoreTraits | One bag, one `CoreKindRef` type. |

## Frozen storage names (not vocabulary — data)

Uid prefixes, stored authored-state binding keys, context
projections, and durable Occasion/effect kinds are opaque stored values. They carry no
vocabulary weight and are never renamed by a word sweep — renaming any of them
is a data migration with its own plan. Accessors may use current vocabulary
over frozen fields (for example, `getCustodyInstanceKey` reads Custody's
stored instance identity).

## How to use this table

- New code: winners only, even where the surrounding file still uses a loser.
- Reviews: a banned word in a new identifier is a finding.
- The complete old→new rename map for the 2026-07 sweep is in
  [docs/yi/archive/48-vocabulary-unification.md](yi/archive/48-vocabulary-unification.md).
