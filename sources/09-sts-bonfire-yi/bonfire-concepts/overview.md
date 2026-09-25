# Bonfire overview

Bonfire is a messaging and social substrate built around stable Yi identities,
portable Kind families, explicit context ownership, and transactional
Occasions.

## Core concepts

| Concept | Purpose |
|---|---|
| [Yi](concepts/yi.md) | Stable UID-denoted runtime root and the joined read projection |
| [Kinds and facets](concepts/unified-class.md) | Portable semantic families, authored state, ports, gates, and context contributions |
| [Holdings](concepts/holdings.md) | Custody-owned assets, quantity, transfer, and extinction |
| [Relationships](concepts/relationships.md) | Relations-owned endpoints, lifecycle, affiliation, and cardinality |
| Authority certificates | Issuer/subject/presenter coverage, use, and revocation |
| Containment | Parent, slot, order, capacity, and exclusive moves |
| Identity | Canonical paths, principal coordinates, and identity revision |
| Occasion | One causal/transactional commit across all affected components |

## Authoring

Portable Kinds use explicit family genesis and semantic facets:

```ts
const NoteFamily = defineKindFamily({
  lineageId: `klin_${'61'.padStart(64, '0')}`,
  nonce: `knonce_${'61'.padStart(64, '0')}`,
})

const Note = defineKind('@mycommunity:note', {
  family: NoteFamily,
  facets: [facet.custody.asset({
    name: 'mycommunity.note',
    quantity: { kind: 'unit' },
    transfer: 'whole-only',
    extinguish: 'whole-only',
    consolidation: 'preserve-lots',
    holderLoss: 'cascade',
    maxUnextinguishedPerHolder: 'unbounded',
  })],
  rowSchema: { body: t.string() },
  gates: {
    discover: public_,
    add: public_,
    remove: custodyHolder(),
    mutate: custodyHolder(),
  },
})
```

`composes` references other Kind families; it never chooses storage. A
cross-facet interaction must be declared with `bindFacet.*`.

## Runtime model

The runtime chooses context operations from the committed Kind binding plan.
Each context stores its own canonical facts and joins them onto Yi reads under
`contexts.*`. Schema-authored state appears under `authoredState[Kind.id]`.

Use indexed semantic operations for reads and writes. Holdings transfer through
Custody, placements move through Containment, occurrences change through
Relations, and certificates issue/revoke/use through Authority. These
operations share the Yi's Domain transaction and Occasion commit.

## Next steps

- [Author guide](author-guide.md)
- [Kit author guide](kit-author-guide.md)
- [SDK quickstart](sdk/quickstart.md)
- [Cookbook](cookbook/README.md)
