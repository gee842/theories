# The Frame — Bonfire's canonical conceptual model

> **This is the North Star.** It defines the mental model a developer should
> use to predict Bonfire. Source, tests, and permanent gates remain the final
> authority for implementation status.

Bonfire makes **being, having, doing, and permitting** one composable system:

- **being** is the set of effective Kind bindings a Yi carries;
- **having** is expressed by context-owned holdings, placements, and relation
  occurrences;
- **doing** is expressed by ports backed by exact handler artifacts;
- **permitting** is expressed by gates and Authority certificates.

There is one stable runtime root, **Yi**, but not one universal component table.
Identity, Custody, Containment, Relations, and Authority own the facts in their
domains. Kinds owns semantic family law, effective bindings, and authored
state. Occasion is the single durable commit spine joining their changes.

The author declares meaning with `defineKind`, `defineKindFamily`, semantic
`facet.*` contributions, and explicit `bindFacet.*` interactions. The compiler
closes those declarations into an immutable binding revision and deterministic
logical representation plan. Runtime follows that plan; it never guesses
meaning from names, optional fields, or storage layout.

---

## Table of contents

1. [The frame, conceptually](#1-the-frame-conceptually)
2. [The one runtime root — Yi](#2-the-one-runtime-root--yi)
3. [Connections have semantic owners](#3-connections-have-semantic-owners)
4. [Kinds, families, and contributions](#4-kinds-families-and-contributions)
5. [Ports, handlers, and gates](#5-ports-handlers-and-gates)
6. [Roles are a reading lens](#6-roles-are-a-reading-lens)
7. [Agency is composed through Identity and Authority](#7-agency-is-composed-through-identity-and-authority)
8. [Collective capability](#8-collective-capability)
9. [Kind evolution](#9-kind-evolution)
10. [The compiler seam](#10-the-compiler-seam)
11. [The normalized substrate](#11-the-normalized-substrate)
12. [The non-leak guarantee](#12-the-non-leak-guarantee)
13. [The recut](#13-the-recut)
14. [Worked examples](#14-worked-examples)
15. [The laws](#15-the-laws)
16. [What is not in the frame](#16-what-is-not-in-the-frame)
17. [Addressing and reading a Yi](#17-addressing-and-reading-a-yi)
18. [Working vocabulary](#18-working-vocabulary)
19. [Relationship to the other docs](#19-relationship-to-the-other-docs)

---

## 1. The frame, conceptually

There are three conceptual layers. Product authors work at the declaration
layer. The compiler closes declarations into immutable law. Runtime and storage
materialize that law through context owners.

```text
┌─────────────────────────────────────────────────────────────────────┐
│ DECLARATION                                                         │
│                                                                     │
│  Kind family + Kind revision                                       │
│    ├─ authored row schema                                           │
│    ├─ semantic context contributions                               │
│    ├─ explicit cross-context bindings                              │
│    ├─ ports + exact handler artifacts                              │
│    ├─ gates                                                        │
│    └─ interface + presentation surfaces                            │
└───────────────────────────────┬─────────────────────────────────────┘
                                │ compile and validate
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ KINDS CONTROL PLANE                                                 │
│                                                                     │
│  family genesis → immutable revision → effective binding            │
│                 → closed representation plan                        │
└───────────────────────────────┬─────────────────────────────────────┘
                                │ manifest and operate
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ RUNTIME                                                            │
│                                                                     │
│  Yi root + binding memberships + authored state                     │
│    ├─ Identity principal                                            │
│    ├─ Custody holding                                               │
│    ├─ Containment placement                                         │
│    ├─ Relations occurrence                                          │
│    └─ Authority certificate                                         │
│                                                                     │
│  all durable changes join one Domain-scoped Occasion                │
└─────────────────────────────────────────────────────────────────────┘
```

The compact vocabulary is **Yi, Kind, context contribution, port, gate, and
Occasion**. Roles such as subject, holder, child, issuer, or endpoint describe
how a Yi participates in a context fact; they are not root categories.

## 2. The one runtime root — Yi

A **Yi** (一, “the one”) is a stable, addressable runtime root. People,
agents, groups, spaces, posts, assets, invitations, relation occurrences, and
certificates can all have Yi roots. There is no parallel subject/object root.

The root owns only stable denotation and coordination fields:

- stable `uid` and Domain;
- primary Kind binding;
- creation and extinction timestamps;
- monotonic sequence;
- current Occasion head.

Kinds-owned records complete the authored representation:

- `yi_binding_memberships` records every effective Kind binding carried by the
  Yi;
- `yi_kind_state` records schema-validated authored state keyed by Yi and
  binding.
- `yi_births` records the immutable exact born-as Kind evidence and optional
  semantic creator; it appears atomically with the root.

Context facts do not belong in authored state. A holder is a Custody fact, a
parent and slot are Containment facts, endpoints are Relations facts, and an
issuer or subject is an Authority fact.

A public read is a joined projection, conceptually:

```ts
interface Yi {
  uid: string
  primaryBinding: string | null
  kinds: ReadonlyArray<string> // effective immutable binding memberships
  createdAt: string
  extinguishedAt: string | null
  contexts?: {
    identity?: { canonicalPath: string; revision: string; active: boolean }
    custody?: {
      holder: string
      lifecycle: 'active' | 'inactive' | 'extinguished'
      quantity?: string
      units?: string
    }
    containment?: {
      parent: string
      slot?: string
      order?: string
      lifecycle: 'placed' | 'extinguished'
    }
    relations?: {
      from: string
      to: string
      lifecycle: 'inactive' | 'active' | 'extinguished'
    }
    authority?: {
      issuer: string
      subject: string
      presenter?: string
      active: boolean
      remainingUses?: number
    }
  }
  authoredState: Record<string, unknown> // authored Kind state only
}
```

The projection is convenient, but ownership remains strict. Generic Yi writes
cannot mutate a context component.

## 3. Connections have semantic owners

The conceptual frame still says that Yis become meaningful through
connections, but Plan 49 does not flatten all connections into one runtime
primitive. Each kind of connection has an owner and law of its own.

| Connection | Owner | Canonical facts |
|---|---|---|
| effective Kind binding | Kinds | family, immutable revision, binding membership |
| canonical identity | Identity | principal coordinates, path, revision |
| holding | Custody | holder, asset binding, quantity, units, lifecycle |
| placement | Containment | child, parent, slot, order, lifecycle |
| relation occurrence | Relations | from/to endpoints, cardinality, activation, lifecycle |
| certificate | Authority | issuer, subject, presenter, uses, revocation |

This keeps the original ontological promise without hiding behavioral
differences. “Alice holds a key,” “a key is equipped in a slot,” “Alice is a
member of a group,” and “a certificate permits Alice to moderate” all connect
Yis, but their conservation, cardinality, lifecycle, and authorization laws are
different. The owning context enforces those laws.

Every local component row references its local Yi root. Semantic coordinates
remain strings where federation prevents a local foreign key. Neither case
creates a second universal root.

## 4. Kinds, families, and contributions

A **Kind family** supplies stable, rename-safe genesis. A **Kind revision** is
immutable semantic law for that family. A Yi carries one or more **effective
Kind bindings**, selected for its Domain and committed by Kinds.

Published and portable Kinds require explicit family genesis:

```ts
import {
  defineKind,
  defineKindFamily,
  defineHandler,
  definePort,
  facet,
  custodyHolder,
  public_,
  t,
} from '@bonfire/sdk'

const SwordFamily = defineKindFamily({
  lineageId: `klin_${'17'.padStart(64, '0')}`,
  nonce: `knonce_${'17'.padStart(64, '0')}`,
})

const SwingHandler = defineHandler(
  '@mycommunity.sword:swing',
  t.object({ target: t.string() }),
  async (ctx) => {
    const sword = await ctx.read(ctx.target, { kind: Sword.id })
    return { durability: sword?.authoredState?.[Sword.id]?.durability }
  },
)
const SwingPort = definePort(SwingHandler, { gate: custodyHolder() })

const Sword = defineKind('@mycommunity:sword', {
  family: SwordFamily,
  facets: [facet.custody.asset({
    name: 'mycommunity.sword',
    quantity: { kind: 'unit' },
    transfer: 'whole-only',
    extinguish: 'whole-only',
    consolidation: 'preserve-lots',
    holderLoss: 'cascade',
    maxUnextinguishedPerHolder: 'unbounded',
  })],
  rowSchema: {
    material: t.enum(['iron', 'steel', 'mythril']),
    durability: t.number(),
  },
  gates: {
    discover: public_,
    add: public_,
    remove: custodyHolder(),
    mutate: custodyHolder(),
  },
  ports: { swing: SwingPort },
})
```

The `rowSchema` governs only authored product state. Custody owns holder,
quantity, units, and lifecycle.

Semantic contributions are declared in `facets`. Their builders fill schema
identifiers, decode with the owning context codec, and deeply freeze the
result. Composition accepts Kind or family references; it does not select a
storage representation.

When one contribution affects another, an explicit `bindFacet.*` declaration
names the exact source and target contributions, execution class, and deciding
owner. The compiler rejects a missing endpoint, missing contribution,
incompatible owner, or ambiguous overlap.

## 5. Ports, handlers, and gates

A **port** is a named operation offered by a Kind. A **gate** decides whether a
caller may invoke it. Gates can allow, deny, or explain required authority; they
reason over the caller, target, effective bindings, context facts, and requested
operation.

A port references an exact, deeply frozen handler artifact. The artifact has a
stable identity, digest, ABI, and runtime schema. A Kit carries the artifacts it
is allowed to carry; trusted process artifacts activate only through installed
package provenance. There is no ambient process-global handler lookup.

The Sword declaration above uses the canonical handler-first shape: define the
runtime schema with the handler artifact, pass that exact artifact to
`definePort`, and include the resulting port in the Kind.

All execution classes use one runtime-owned registry, one handler context, one
schema/gate/Authority envelope, and one Occasion transaction. Equal artifact
references in separate runtimes remain isolated. Disposing one runtime removes
only registrations owned by that runtime.

Ports are resolved from the target Yi’s effective Kind bindings. Holding an
asset does not copy its ports onto the holder. If holding, placement, or a
certificate affects authorization, that relationship is declared explicitly
and evaluated by the gate and Authority path.

## 6. Roles are a reading lens

Subject, object, holder, held asset, child, parent, source endpoint, target
endpoint, issuer, subject, presenter, capability, container, and agent are
**roles**, not root types.

The same Yi may simultaneously be:

- a Custody holder in one holding;
- the held asset in another;
- the child of a Containment placement;
- an endpoint of several Relations occurrences;
- the subject of one Authority certificate and issuer of another.

Those roles are read from context components. They are never inferred from an
optional authored field or a hidden category.

## 7. Agency is composed through Identity and Authority

Every Yi is addressable. Acting requires explicit semantic law and runtime
authority:

- an Identity principal supplies canonical principal coordinates and signing
  identity;
- ports define which operations the Yi offers;
- gates define the admission rule;
- Authority certificates carry delegated or scoped permission;
- Custody and Containment can affect permission only through declared
  cross-context bindings.

This keeps four control axes separate:

1. **authored-state authority** — who may change binding-specific product data;
2. **custody** — who holds and may transfer an asset;
3. **signing identity** — which principal witnesses an operation;
4. **operation authority** — which gate and certificate law admits the call.

An equipped key illustrates the separation. Custody records who holds the key;
Containment records whether it occupies the required equipment slot; Authority
records the certificate it activates; the port gate decides the action. Moving,
transferring, extinguishing, or revoking the relevant component removes the
authority immediately without changing the Yi’s root identity.

## 8. Collective capability

A group is an Identity principal with product-specific Kind bindings and
Relations occurrences connecting its members. A group may be the subject of a
scoped Authority certificate just as an individual principal may be.

Collective permission is evaluated through a bounded, explicit path:

```text
member ── Relations membership ──▶ group
group  ── Authority certificate ─▶ resource + operation scope
```

The invariants are:

- **attenuation only** — delegation can narrow, never widen, the issuer’s
  authority;
- **deny precedence** — applicable sanctions and revocation defeat inherited
  allow;
- **eager revocation** — revoking the certificate removes access without
  per-member cleanup;
- **no synthetic membership** — access through the group does not create a
  membership occurrence in the target resource.

Membership cardinality belongs to Relations. Certificate scope and revocation
belong to Authority. The gate consumes both owners’ facts through the declared
authorization path.

## 9. Kind evolution

Family genesis is stable; revisions are immutable and content-addressed. A
Domain selects effective binding revisions through Kinds-owned binding records.

An evolution has several distinct identities:

- semantic contribution changes alter the semantic revision;
- representation-plan changes alter the binding revision;
- interface-surface changes alter interface identity;
- presentation-surface changes alter presentation identity.

The compiler closes the complete family set, dependency slots, context
contributions, cross-context bindings, aliases, and surfaces before admitting a
revision. A rollout changes the selected binding; it does not mutate an old
revision in place.

Portable installation uses `PortableKitInstallSourceV3`. Family genesis,
canonical contribution bytes, exact surfaces, handler artifacts, views,
workflows, migrations, aliases, expected-source inventory, and per-family
export policy travel as one install unit. Export policy is operation-owned
metadata and never influences semantic representation.

## 10. The compiler seam

Authors declare **meaning**, not storage:

```ts
const Friendship = defineKind('@mycommunity:friendship', {
  family: FriendshipFamily,
  facets: [
    facet.relations.topology({
      name: 'mycommunity.friendship',
      direction: 'mutual',
      from: { name: 'friend-a', familyId: PersonFamily.familyId },
      to: { name: 'friend-b', familyId: PersonFamily.familyId },
    }),
    facet.relations.policy({
      name: 'mycommunity.friendship',
      unextinguished: { perPair: 'one', perFrom: 'many', perTo: 'many' },
      activePerTo: 'unbounded',
      activation: 'immediate',
      affiliation: null,
      readVisibility: 'confers',
    }),
  ],
})
```

The compiler decodes the contribution bytes through Relations, validates the
endpoint families and cardinality law, and writes the required Relations
component into the representation plan. Runtime does not inspect the Kind name
or authored payload to rediscover that choice.

A multi-context Kind is manifested through one runtime command. It validates
authored state once, prepares every component named by the committed plan, and
commits the Yi root, binding memberships, authored state, context components,
and exact effects through one Occasion. Partial manifestation is invalid.

> **Law — the compiler seam.** Declaration states what a Kind means. The closed
> representation plan states which owners must materialize it. Runtime executes
> that plan exactly.

## 11. The normalized substrate

One ontology does not imply one data structure. The fresh-database baseline
keeps context stores normalized and separately indexed:

- `yi`, `yi_binding_memberships`, and `yi_kind_state`;
- Identity principals and canonical-path indexes;
- Custody holdings and transfer-request journal;
- Containment placements and move-request journal;
- Relations occurrences and cardinality reservations;
- Authority certificates and issuer epochs;
- Streams in their established dense ordered store;
- Occasion commits, effects, checkpoints, and consumer positions.

Specialized indexes are part of the contract. Holder, placement, relation
endpoint, certificate subject/issuer, Kind binding, identity path, forum order,
and balance reads must use context-owned query ports with cursor pagination.
Product code may not replace those queries with Yi scans, fixed-size fetches,
client-side aggregation, or per-row catalog hydration.

### Occasion is the durable spine

One Domain-scoped Occasion coordinator acquires the logical Domain lock or
transaction, runs transaction-scoped narrow repositories, collects exact
effects, computes the immutable commit, binds every changed Yi root to the
actual commit ID, and commits once.

Nested commands join the active Occasion. An empty Occasion, an effect without
materialized state, or an ordinary durable write outside the coordinator fails
closed. Stream writes, Yi changes, workflows, outbox state, Views, and
multi-Yi effects share the same atomic commit when one operation changes them
together.

Checkpoint plus retained Occasion tail must reconstruct normalized state.
History, watches, Authority frontiers, recovery, restore, erasure propagation,
and safe pruning consume the same commit/effect source.

## 12. The non-leak guarantee

Public operations describe semantic facts and return the same logical shape in
memory and PostgreSQL. Storage-specific choices remain behind owner ports.

The escape path is explicit and ownership-preserving:

1. use generated Kind operations and typed SDK surfaces;
2. use context-owned indexed query operations for cross-row reads;
3. read the joined Yi projection when one stable identity is the anchor;
4. inspect Occasion history for committed change order and effects.

There is no public generic writer beneath these steps. Authored state changes
go through a binding-specific Kinds command. Custody, Containment, Relations,
Identity, and Authority facts change only through their owners.

Local and connected World modes use the same typed transport contract. A
generated relation, Signal, View, projection, or workflow operation is either
implemented over that transport or absent from the advertised surface.

## 13. The recut

The final model replaces several overloaded ideas with explicit owners:

| Former ambiguity | Canonical model |
|---|---|
| runtime category decides subject versus object | one Yi root; roles come from effective bindings and context facts |
| a type label also selects storage | Kind/family semantics compile to an explicit representation plan |
| holder or endpoint duplicated in authored payload | Custody or Relations is the sole owner |
| parent field on the generic root | Containment placement owned by Containment |
| permission encoded as an arbitrary product record | Authority certificate plus gate law |
| connection uniqueness enforced in product code | Relations reservation and indexed cardinality constraint |
| ambient handler name lookup | exact handler artifact in a runtime-owned registry |
| audit appended after mutation | one atomic Occasion commit with exact effects |
| exportability changes Kind meaning | operation-owned family export policy with install provenance |

The result is not a relabeled object hierarchy. It is a smaller root combined
with stronger semantic owners.

## 14. Worked examples

- **A person** is a Yi with an Identity principal contribution and product Kind
  bindings. Its ports and gates define what it can do.
- **A bot** has the same root shape. Its installed workflow and handler
  artifacts determine automated behavior.
- **A plain asset** is a Yi with a Custody component and product-authored state.
  It need not have an Identity principal or ports.
- **An equipped authority key** combines Custody, a child placement in an
  equipment slot, and an Authority certificate through explicit cross-context
  bindings. Moving or transferring it invalidates the permission.
- **A community** is an Identity principal with membership occurrences owned by
  Relations, durable messages owned by Streams, and role certificates owned by
  Authority.
- **A friendship** is a mutual Relations occurrence whose canonical endpoint
  ordering and per-pair reservation enforce one live occurrence under races.
- **A vote** is a Relations occurrence with a per-voter/proposal reservation.
  The product cannot create a second live vote for the same pair.
- **An invitation** is a Relations occurrence plus a one-use Authority
  certificate. Acceptance atomically consumes the certificate, creates one
  membership, and extinguishes the invitation.
- **A reply** is one atomic workflow that creates the relation and durable
  stream content in a single Occasion.
- **An escrow** is an installed Settlement workflow. Custody transfers offered
  assets to an escrow principal, then releases or refunds conserved quantities.
  The escrow occurrence itself is not an asset.
- **A sanction** is explicit Authority deny law with scope, precedence,
  revocation, and explanation.
- **Ephemeral occupancy** is a Signal. It is TTL-bounded and does not become a
  durable placement or relation occurrence.

## 15. The laws

1. **One stable root.** Every addressable runtime entity is a Yi; context
   component tables do not create competing roots.
2. **Meaning is explicit.** A Yi’s meaning comes from effective Kind bindings,
   decoded semantic contributions, and context-owned facts—never identifier
   prefixes or optional-field inference.
3. **Owners are exclusive.** Authored state contains product data only. Each
   context is the sole writer of its semantic facts and lifecycle.
4. **Families are closed.** Portable Kinds have explicit family genesis;
   composition and dependency slots resolve within a complete install set.
5. **Cross-context effects are bound.** Every interaction identifies its source
   contribution, target contribution, execution class, and deciding owner.
6. **Ports and authority are exact.** Executable ports have runtime schemas and
   exact handler artifacts; gates and Authority decide invocation.
7. **Representation is compiled.** Runtime executes a committed logical plan
   and never reconstructs representation from declaration names.
8. **One durable commit spine.** All durable effects of one Domain operation
   commit atomically through Occasion, or none do.
9. **Queries respect ownership.** Cross-row reads use context-owned indexed,
   paginated operations; no generic Yi scan substitutes for them.
10. **Break forward cleanly.** Prelaunch changes do not retain dual writes,
    compatibility aliases, old wire decoders, or detached projections.

## 16. What is not in the frame

Some systems are first-class but do not become generic Yi components:

- **Streams** own canonical, dense-ordered content and reply causality. Their
  writes join Occasion when an operation also changes Yi or context state.
- **Signals** own ephemeral presence, typing, cursors, and occupancy. Signals
  are TTL-bounded and do not assert durable authority or historical truth.
- **Views and projections** own declared, rebuildable read models. Evolution law
  is centralized in Views and shared by SDK preflight and server admission.
- **External effects** use durable outbox/workflow state with idempotency and
  compensation; a database transaction cannot roll back a completed external
  call.
- **Portability** is a privileged operation. Export policy is package metadata,
  not a semantic contribution and not part of a representation plan.
- **Federation and sharding** translate semantic Domain and principal
  coordinates to physical placement. They do not alter the Kind or Yi model.

These are named boundaries, not hidden alternative roots.

## 17. Addressing and reading a Yi

- **Identity** is `uid`: opaque, stable, and never rewritten.
- **Canonical path** is an Identity-owned lookup coordinate, not universal root
  state.
- **Kind membership** is the Yi’s effective immutable binding set.
- **Authored state** is schema-validated and keyed by binding.
- **Context state** is read through typed `contexts.identity`,
  `contexts.custody`, `contexts.containment`, `contexts.relations`, and
  `contexts.authority` projections.
- **History and watch order** come from Occasion commits and effects.

Read visibility and invocation addressability remain distinct. A caller may be
able to invoke a gated operation without receiving private state. The port’s
gate and Authority envelope decide the call; the owner’s read policy decides
the projection.

## 18. Working vocabulary

| Term | Meaning |
|---|---|
| **Yi** | stable UID-denoted runtime and coordination root |
| **Kind family** | stable semantic lineage with explicit genesis |
| **Kind revision** | immutable authored law for one family revision |
| **effective Kind binding** | the exact family revision and closed plan selected for a Yi |
| **context contribution** | decoded semantic law owned by Identity, Custody, Containment, Relations, Authority, or another bounded context |
| **cross-context binding** | explicit law connecting exact source and target contributions |
| **port** | typed operation offered by a Kind |
| **handler artifact** | deeply frozen executable definition named by exact identity, digest, and ABI |
| **gate** | admission and explanation law for an operation |
| **certificate** | Authority-owned record carrying scoped permission and revocation state |
| **Occasion** | immutable atomic commit and exact effect set for a Domain operation |
| **role** | how a Yi participates in a context fact, such as holder, child, endpoint, issuer, or subject |

Semantic product nouns remain useful when accurate: holdings, placements,
relations, capabilities, certificates, attestations, memberships, and
reservations. “Claim” is reserved for Automation or Settlement work claiming.

## 19. Relationship to the other docs

Bonfire is an encoded realization of 间理. The frame makes its reconstruction
law operational: declarations are portable semantic bytes, the compiler closes
them into immutable plans, normalized owners hold canonical facts, and Occasion
records the atomic change.

Continue with:

- [Yi](../concepts/yi.md) for the normalized root and public read shape;
- [Kinds and facets](../concepts/unified-class.md) for authoring and compiler
  closure;
- [Authority](../concepts/authority.md),
  [Holdings](../concepts/holdings.md), and
  [Messages](../concepts/messages.md) for owner-specific behavior;
- [the structural arc](49-structural-arc/README.md) for the Plan 49 constitution
  and execution record.

> **The sentence to remember:** A Yi is the stable identity that carries
> effective Kind bindings; its meaning is explicit in immutable semantic law
> and context-owned facts, and every durable change lands through Occasion.
