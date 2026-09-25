# Yi

> Where this page and source-anchored docs disagree, `llms.txt` and the cited
> source files win.

Yi is Bonfire's stable runtime root. Its UID is the durable denotation; Kind
evidence, immutable Creation, and mutable context facts remain separately
owned. The normalized model stores the root separately from context-owned
component rows and joins them into one public read.

## Root storage

The `yi` table owns only stable root and coordination fields:

- stable `uid` and Domain;
- primary Kind binding;
- creation and extinction time;
- monotonic sequence/cursor;
- current Occasion head.

Two Kinds-owned tables complete the authored representation:

- `yi_binding_memberships` records every effective Kind binding carried by the
  Yi;
- `yi_kind_state` records schema-validated authored state keyed by Yi and
  binding.

The Kinds-owned `yi_births` table records the exact born-as binding and
immutable origin/optional semantic creator. Root and birth are committed
atomically; later principal rename, reparenting, or extinction never rewrites
that Creation fact.

No context fact is duplicated in authored state.

## Context components

| Component | Owner | Examples |
|---|---|---|
| Identity principal | Identity | canonical path, parent principal, key/profile revision |
| Holding | Custody | holder, quantity, units, active/extinguished lifecycle |
| Placement | Containment | child, parent, slot, order, move revision |
| Relation occurrence | Relations | from/to, lifecycle, pair/from/to cardinality |
| Certificate | Authority | issuer, subject, presenter, uses, revocation revision |

Every local component row references its Yi root. Federation coordinates that
cannot use local foreign keys remain semantic strings.

## Public read shape

```ts
interface Yi {
  uid: string
  domainId: string
  primaryKindBindingId: string
  bindings: ReadonlyArray<string>
  createdAt: string
  extinguishedAt: string | null
  sequence: number
  occasionHeadId: string
  contexts?: {
    identity?: { canonicalPath: string; revision: string; active: boolean }
    custody?: { holder: string; lifecycle: 'active' | 'inactive' | 'extinguished'; quantity?: string; units?: string }
    containment?: { parent: string; lifecycle: 'placed' | 'extinguished'; slot?: string; order?: string }
    relations?: { from: string; to: string; lifecycle: 'inactive' | 'active' | 'extinguished' }
    authority?: { issuer: string; subject: string; presenter?: string; active: boolean }
  }
  authoredState: Readonly<Record<string, unknown>>
}
```

`contexts` is a joined read projection. `authoredState` contains only
schema-validated Kind state. Concrete public SDK types may provide typed
accessors over these fields; they do not fabricate absent components.

## Manifestation

```ts
const yi = await rt.as(alice.uid).manifest({
  kind: Asset.id,
  contexts: {
    custody: { holder: alice.uid, quantity: '1', units: 'unit' },
  },
  init: { [Asset.id]: { label: 'camp key' } },
})
```

The runtime selects operations from the Kind binding's committed logical
representation plan. It does not classify the input from field presence,
identifier prefixes, or composed sentinel Kinds.

Multi-component manifestation shares one Domain transaction and Occasion
commit. If any owner rejects, every component and the root roll back.

## Reading and querying

Use the typed product facade for the selected Kind family and its context
components. Queries use context-owned indexes for Custody holder, placement, relation endpoint,
certificate subject/issuer, Kind binding, and identity path. Product code must
not fall back to full Yi scans or N+1 component hydration.

## Invocation

Ports are resolved from the target Yi's effective Kind bindings. Invoke the Yi
that carries the port:

```ts
await rt.as(alice.uid).invoke(tool.uid, 'use', { target: door.uid })
```

Read visibility and invocation addressability are distinct. A port can be
addressable while its state remains private; the port gate is the permission
boundary. Holding a Yi never copies its ports onto the holder.

## Lifecycle

Context operations own lifecycle facts:

- Custody transfers and extinguishes holdings;
- Containment moves placements;
- Relations activates, deactivates, and extinguishes occurrences;
- Authority issues, consumes, and revokes certificates;
- Runtime/Kinds creates the Yi root and immutable Creation; Identity
  initializes, reparents, renames, and extinguishes principal state.

The Yi root records final extinction and the shared Occasion head. Generic
authored-state patching cannot mutate context lifecycle.

## Kind bindings

A Yi may carry multiple effective bindings. Kinds closes the complete family
set, validates dependency slots and cross-facet bindings, and commits a
deterministic representation plan in `KindBindingRevisionBodyV2`. Runtime
selection reads that plan directly.

See [Kinds and facets](unified-class.md) and [Holdings](holdings.md).
