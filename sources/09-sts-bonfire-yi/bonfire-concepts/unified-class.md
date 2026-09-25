# Kinds and facets

> Where this page and source-anchored docs disagree, `llms.txt` and the cited
> source files win.

A Kind is a portable semantic family revision. It declares authored state,
gates, ports, presentation, and context-owned facet contributions. A Kind does
not declare a storage shape. The compiler closes the family and records the
logical representation plan in its binding revision.

## Authoring a Kind

Published and portable Kinds require explicit family genesis.

```ts
import {
  defineHandler,
  defineKind,
  defineKindFamily,
  defineKit,
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
  t.object({}),
  async (ctx) => {
    const row = await ctx.read(ctx.target, { kind: Sword.id })
    return { durability: Number(row?.authoredState?.[Sword.id]?.durability ?? 0) }
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

const SwordKit = defineKit('pkg:mycommunity.sword', {
  kinds: [Sword],
  handlerArtifacts: [SwingHandler],
})
```

`rowSchema` governs only authored state. Custody facts such as holder and
lifecycle come from the Custody facet's component row.

## What the compiler closes

For each family the compiler validates and freezes:

- family genesis and all family references;
- Kinds-owned declaration and facet-binding contributions;
- context contributions such as Custody assets, Relations topology/policy,
  Containment acceptance/policy, and Authority instruments;
- the public interface and presentation surfaces;
- a deterministic logical representation plan;
- a binding revision naming the exact semantic revision and representation.

`composes` accepts Kind/family references. It does not select representation.
Representation comes only from decoded facet contributions.

## Cross-facet binding

When one facet affects another, author an explicit `bindFacet.*` value. A
binding identifies the source and target contributions, execution class, and
deciding owner. This keeps overlaps reviewable and makes ambiguous overlaps a
compiler error.

For example, keep the results of `facet.custody.asset(...)` and
`facet.authority.role(...)` in local constants, include both constants in
`facets`, then pass those same frozen values as `custody` and `authority` to
`bindFacet.authoritySubjectFromCustodyHolder(...)`.

The exact builders validate through their owning context codecs and return
deeply frozen artifacts. Refer to the generated TypeScript signature for the
required fields of each builder.

## Kind versus Yi

A Kind is immutable semantic law. A Yi is one stable UID-denoted runtime root carrying
one or more effective Kind bindings.

```ts
const sword = await rt.as(alice.uid).manifest({
  kind: Sword.id,
  contexts: {
    custody: { holder: alice.uid, quantity: '1', units: 'unit' },
  },
  init: { [Sword.id]: { material: 'steel', durability: 100 } },
})
```

Conceptually the read is assembled from normalized owners:

```ts
{
  uid: sword.uid,
  primaryKindBindingId: Sword.bindingId,
  bindings: [Sword.bindingId],
  contexts: {
    custody: { holder: alice.uid, lifecycle: 'active' },
  },
  authoredState: {
    [Sword.id]: { material: 'steel', durability: 100 },
  },
}
```

The Kinds repository owns the committed binding evidence and representation
plan; it is not copied onto each public Yi read. The runtime resolves the
binding identifiers against that plan and never infers components from
optional fields or identifier prefixes.

## Relations

Relations are ordinary Kind families with Relations contributions:

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

Relations owns endpoints, cardinality, and occurrence lifecycle. These facts
are not authored state.

## Kits and evolution

The portable install unit is `PortableKitInstallSourceV3`. It carries family
genesis, contribution bytes, surfaces, aliases, and migrations together. The
server compiles and admits the whole set atomically into the Kinds repository
and the owning context plans.

Redeploying a family creates immutable revisions. Domain binding selection and
rollout decide which revision a Yi uses. A revision change affects identity only
when its canonical semantics change.

See [Yi](yi.md), [Holdings](holdings.md), and the
[kit author guide](../kit-author-guide.md).
