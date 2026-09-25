# Authored state and context facts

This page records the normalized storage boundary. For authoring examples, start
with [Holdings](holdings.md).

A held Yi has two distinct kinds of data:

- schema-authored state in `yi_kind_state`, projected as typed authored state;
- Custody-owned facts in `custody_holdings`, projected as
  `contexts.custody`.

Holder, quantity, units, activation, transfer revision, and extinction are
not authored-state fields. Generic mutation operations reject attempts
to write context facts. Use Custody operations instead.

```ts
const row = await rt.yi.read(assetUid, caller)

row?.authoredState[Asset.id]    // authored rowSchema state
row?.contexts?.custody?.holder  // Custody fact
row?.contexts?.custody?.quantity // projected fungible quantity
```

## Declaring quantity and lifecycle

```ts
const Asset = defineKind('@mycommunity:asset', {
  family: AssetFamily,
  facets: [facet.custody.asset({
    name: 'mycommunity.asset',
    quantity: { kind: 'unit' },
    transfer: 'whole-only',
    extinguish: 'whole-only',
    consolidation: 'preserve-lots',
    holderLoss: 'cascade',
    maxUnextinguishedPerHolder: 'unbounded',
  })],
  rowSchema: { label: t.string() },
  gates: {
    discover: public_,
    add: public_,
    remove: custodyHolder(),
    mutate: custodyHolder(),
  },
})
```

Use `quantity: { kind: 'fungible', decimalScale }` for conserved divisible
assets. Transfer and extinction policies determine which whole/partial
operations Custody admits.

## Other context components

Do not place these facts in a Custody or authored-state bucket:

| Fact | Context |
|---|---|
| parent, slot, order, move revision | Containment |
| relation from/to, cardinality, occurrence lifecycle | Relations |
| certificate issuer/subject/presenter, uses, revocation | Authority |
| canonical path, principal coordinates, identity revision | Identity |

Multi-facet Kinds compile these components into one closed representation plan.
Cross-facet effects require an explicit `bindFacet.*` declaration; field
presence is never used to infer the representation.
