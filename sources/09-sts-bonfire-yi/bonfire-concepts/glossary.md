# Bonfire glossary

> **Direction:** for historical vocabulary and migration context, see [docs/yi/archive/05-authoring-and-migration.md §B](yi/archive/05-authoring-and-migration.md) and [01-frame.md §18](yi/01-frame.md). The definitions below describe current implementation terms.

Terminology cheat sheet. Substrate concepts to author-facing names; terms
that no longer exist and what replaced them.

## Substrate primitives

| Term | Definition |
|---|---|
| **Yi** | Stable runtime root denoted by a UID. Its root joins effective Kind bindings, authored state, immutable Creation, and context-owned components. Pronounced "ee" (一 — "the one"). |
| **Kind** | Immutable semantic law: family genesis, authored-state schema, gates, ports, facets, and cross-facet bindings. Stored in the Kinds repository, never as a Yi. |
| **KindRef** | A canonical kind address such as `core:membered`, `@mycommunity:member`, or `~alice.tools:calendar`. |
| **`bindings[]`** | Public projection of the Yi's effective immutable Kind binding memberships. It does not select physical representation. |
| **`authoredState`** | Public projection of schema-validated authored state from `yi_kind_state`, keyed by Kind address. Context facts never live here. |
| **`composes`** | Kind/family references included in semantic family closure; marker strings cannot select representation. |
| **Facet** | Typed contribution owned by Identity, Custody, Containment, Relations, Authority, Streams, or another context. |
| **Touch** | The universal write verb. Every mutation is a touch; every touch emits a `yi.touched` event. |
| **TouchHandle** | Per-touch observability handle: `delivered → responded → reactions`. Returned by `rt.yi.touch` and `rt.yi.actAs` (`manifest` returns the minted `Yi`; `invoke` returns the handler's result). |

## Author-facing surfaces

| Term | Definition |
|---|---|
| **`defineKind`** | Declares one Kind revision from explicit family genesis, typed facets/bindings, authored state, gates, ports, and presentation. |
| **`defineHandler`** | Returns an exact, deeply frozen handler artifact from a ref, runtime schema, and body. It has no ambient registration side effect. |
| **`defineStream`** | Proposed V1.1 declarative server-side feed. No canonical stream-declaration kind or public `defineStream` surface exists in the live SDK yet. |
| **Port** | A named executable operation on a Kind. It has its own gate and references an exact schema-bearing handler artifact. The Runtime evaluates the gate and runs the artifact on allow. |
| **Gate** | An ADT describing who can do what. Pure data. Composable via `and`/`or`/`not`. Returns `allow` / `deny` / `requires` / `requires-any`. |
| **Gate DSL** | The fluent function library (`bears`, `holds`, `within`, `is`, etc.) that builds Gate trees. |
| **Schema DSL (`t.*`)** | The type-as-value builders (`t.string()`, `t.enum()`, etc.) that compile to JSON Schema. |
| **Recipe** | A deterministic `facet.*`, Gate, or policy constructor that compiles into ordinary Kind meaning rather than creating another semantic layer. |
| **Snapshot** | Immutable verified read of one Yi under an exact binding. It exposes authored `state`, named facet faces, and reserved `$` metadata/evidence without duplicating context facts. |

## Authentication and Authority

| Term | Definition |
|---|---|
| **Bearer** | An API key. Substrate maps bearer → subject spirit. Bearer custody = identity. The client never types a uid for itself. |
| **Actor** | The authenticated principal operating the SDK. It remains the actor when a certificate supplies a different subject. |
| **Subject** | The principal for whom an operation is attempted. It equals the actor unless an explicit valid `actFor` ceremony narrows it. |
| **Certificate** | Explicit, attenuated, revocable Authority evidence. Its conjunctive action/resource target and graph-specific selectors are re-evaluated against current state on every operation. |
| **`'self'` literal** | The string `'self'` (or `'me'`) anywhere a uid is expected. SDK passes it through; server rewrites to the authenticated caller's uid. |
| **Frozen kind** | A substrate-seeded Kind whose definition cannot be mutated and whose instances follow kernel-owned lifecycle law. |
| **Graph-scoped selector** | An explicit current-state target over principal-state descendants, Containment descendants, Custody holdings, or Relation neighborhoods. Graphs are never interchangeable and ancestry grants nothing automatically. |
| **WriteWitness** | (V1.1) Federation optimization. A trusted host pre-signs a validation witness; the receiving host skips re-validation if the writer is in its trust pairs. |

## Federation

| Term | Definition |
|---|---|
| **Federation envelope** | Wire format for cross-host Yi propagation. Contains the row, pinned kind versions, recent events, optional WriteWitness, host signature. |
| **Trust pair** | A historical federation proposal for asserting "host A trusts host B for scope X." No canonical trust-pair kind exists in the live runtime. |
| **Unknown-kind quarantine** | When a row arrives with a kind the receiving host doesn't have, fetch the kind from origin; on failure, quarantine the row (don't merge). |
| **Dialect version** | The substrate's wire-format version: `bonfire/v1`. Minor mismatches warn-and-degrade; major mismatches reject. |
| **Closed format registry** | The 9 `bonfire/*` formats every host implements: `uid`, `kind-ref`, `class-ref`, `iso-datetime`, `path`, `url`, `email`, `sha256`, `uint-string`. |

## Concurrency

| Term | Definition |
|---|---|
| **Optimistic concurrency** | Rows carry monotonic sequence state, but the public write API does not currently expose an `expectedSeq` / SDK auto-retry knob. Re-read and re-check inside a handler when a kit needs compare-and-set semantics. |
| **Atomic block** | Handler-side transaction via `ctx.atomic(fn)` inside `defineHandler`: the body runs on a tx-mirror ctx inside ONE storage transaction — every verb on the mirror is all-or-nothing, and a mid-body failure rolls back the rows AND events already written (Postgres `BEGIN`/`COMMIT`; in-memory undo log). Nested `atomic` joins the ambient transaction. Use the `tx` mirror inside the body, not the outer `ctx`. There is no standalone HTTP endpoint for it, and it is not surfaced on the public client `yi.*` object. |
| **Latency class** | Optional `defineHandler` opt (`sync` / `async-bounded`). Stored at registration but not read by dispatch — no behavioral effect today. |
| **Durable checkpoint** | Occasion recovery checkpoint used with a retained tail and protected consumer positions. It is distinct from the public SDK `Snapshot<K>` read value. |

## Time travel + history

| Term | Definition |
|---|---|
| **`atSeq` read** | `rt.yi.read(uid, { atSeq: N })` returns the row's state at sequence N by folding the per-Yi event log from the start (a best-effort replay under Architecture C; the `yi` row is canonical at HEAD). Degrades past the retention horizon: a read below the oldest retained seq throws `BeyondRetentionHorizon` rather than returning a different seq's state. See `rt.yi.retentionHorizon()`. |
| **`rt.yi.explain`** | Returns the gate evaluator's full trace as data — used for "why was this denied?" UX, audit, debugging. |
| **`estimateFoldCost`** | UI cost-awareness primitive. Returns expected events + ms for a time-travel read. |

## Schema evolution

| Term | Definition |
|---|---|
| **Evolution policy** | Per-Kind compatibility mode: `backward` (default; new can read old), `forward` (old can read new), `full` (both), `none` (anything goes). Recorded in the immutable Kind revision at deploy; a redeploy inherits it when omitted, may strengthen it, and may not weaken it (refused with `SchemaIncompatible` — publish a new family instead). |
| **Backward-compatible change** | Adding optional fields, widening enums, lifting constraints. Allowed under `backward` policy. |
| **Breaking change** | Removing required fields, narrowing enums, tightening constraints. Rejected under `backward`; requires deploying a new kind address (for example `@mycommunity:member-v2`). |
| **Schema-version pinning** | Federation envelopes pin to specific kind seqs (`kindUids[]` + `kindSeqs[]`). Receivers validate against the version pinned in the envelope, not the host's current version. |

## Yi UID + principal path

| Term | Definition |
|---|---|
| **uid** | Opaque stable primary key. `<prefix>_<hex>` (e.g. `sp_abc123…`). Never rewritten. |
| **Address** | Canonical human-readable identity or world locator (for example `~alice/post-1` or `@mycommunity/members/alice`). Rewritten on rename/reparent; the uid remains stable. |
| **`core:human`** | Substrate-immutable kind. Once added to a row at signup, never removed. The structural API-key custody marker. |
| **`core:api-keyable`** | Substrate-immutable kind. Carriers can have API keys minted. Mutually exclusive with `core:human` via `add` gate. |
| **`core:sovereign`** | Substrate-immutable tag-kind. Rows carrying it opt out of ancestor authority on their gates. |

## Etymology

- **Yi** (一 / 太极): Chinese for "the one" or "great ultimate." The substrate's
  single primitive. Pronounced "ee."
- **Kind**: A category, type, or sort. The kind a row belongs to determines
  what it is.
- **Touch**: The verb for substrate mutation, borrowed from Whitehead's process
  philosophy. Every event is a "touching" of one Yi by another.
- **Compose**: From "co-position" — putting kinds together. A composing kind
  IS its composed kinds.
- **Bear**: To carry a kind. `caller-bears-kind` = the caller carries this
  binding in their `bindings[]` array.
- **Hold**: To possess a holding row. `caller-holds(kindRef)` = the caller has
  at least one active holding of this kind.
