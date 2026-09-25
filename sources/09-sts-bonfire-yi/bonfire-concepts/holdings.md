# Holdings

> Where this page and source-anchored docs disagree, `llms.txt` and the cited
> source files win.

A holding is a Yi with a Custody component. The Yi root supplies stable
identity and Kind bindings; Custody owns holder, quantity, units, activation,
transfer, and extinction. Authored fields live separately in `yi_kind_state`.

There is no public storage selector or sentinel composition. A portable Kind
declares a family genesis and a semantic Custody
facet. The compiler validates that contribution and commits its representation
components in the Kind binding revision.

## Declare a unit asset

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
  lineageId: `klin_${'42'.padStart(64, '0')}`,
  nonce: `knonce_${'42'.padStart(64, '0')}`,
})

const SwingHandler = defineHandler(
  '@mycommunity.sword:swing',
  t.object({}),
  async (ctx) => {
    const sword = await ctx.read(ctx.target, { kind: Sword.id })
    return { damage: Number(sword?.authoredState?.[Sword.id]?.damage ?? 1) }
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
  rowSchema: { damage: t.number() },
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

Manifest semantic Custody input at the operation boundary. Only schema-authored
state belongs under the Kind address.

```ts
const sword = await rt.as(alice.uid).manifest({
  kind: Sword.id,
  contexts: {
    custody: { holder: alice.uid, quantity: '1', units: 'unit' },
  },
  init: { [Sword.id]: { damage: 7 } },
})

await rt.as(alice.uid).invoke(sword.uid, 'swing', {})
await rt.as(alice.uid).transfer(sword.uid, { to: bob.uid })
await rt.as(bob.uid).extinguish(sword.uid)
```

Ports belong to the concrete Yi carrying them. Holding a capability does not
project its ports onto the holder.

## Fungible assets

Fungibility is a Custody quantity policy, not a sentinel or a generic payload
field.

```ts
const Points = defineKind('@mycommunity:points', {
  family: PointsFamily,
  facets: [facet.custody.asset({
    name: 'mycommunity.points',
    quantity: { kind: 'fungible', decimalScale: 2 },
    transfer: 'whole-or-partial',
    extinguish: 'whole-or-partial',
    consolidation: 'explicit-merge-same-holder',
    holderLoss: 'cascade',
    maxUnextinguishedPerHolder: 'unbounded',
  })],
  gates: {
    discover: public_,
    add: public_,
    remove: custodyHolder(),
    mutate: custodyHolder(),
  },
})
```

```ts
const balance = await rt.as(alice.uid).manifest({
  kind: Points.id,
  contexts: {
    custody: { holder: alice.uid, quantity: '1250.00', units: 'points' },
  },
})

await rt.as(alice.uid).transfer(balance.uid, {
  to: bob.uid,
  amount: '250.00',
})
```

Custody performs conserved unit arithmetic and journals idempotent transfer
requests. Product code must not reproduce balances in authored state.

## Context ownership

| Fact | Owner | Read projection |
|---|---|---|
| Stable uid, Domain, carried binding, creation/extinction head | Kinds/Yi | universal Yi fields |
| Kind-authored state | Kinds | `authoredState[Kind.id]` |
| Holder, quantity, units, active state | Custody | `contexts.custody` |
| Parent, slot, order | Containment | `contexts.containment` |
| Relation endpoints and occurrence lifecycle | Relations | `contexts.relations` |
| Certificate issuer, subject, presenter, revocation/use state | Authority | `contexts.authority` |
| Canonical path and principal revision | Identity | `contexts.identity` |

The context values above are joined read projections. They are not duplicated
inside authored Kind state.

## Relations and certificates are not holding shapes

Endpoint facts belong to Relations and are declared with
`facet.relations.topology(...)` plus `facet.relations.policy(...)`. Issue,
revocation, presentation, and use-count facts belong to Authority certificates.
Use `certificate` for Authority instruments; reserve `claim` for
Automation/Settlement work claiming.

One Yi may intentionally carry several components. For example, an equipped
key can combine Custody, Containment, and Authority. Declare every facet and an
explicit `bindFacet.*` binding so the compiler records the source contribution,
target contribution, execution class, and deciding owner. Runtime selection
comes only from that committed plan.

## Queries and lifecycle

Use context-owned indexed queries. Explicit substrate tooling can page a
holder's live assets through the Custody holder index:

```ts
const swords = await client.query.holdings()
  .holder(alice.uid)
  .kind(Sword.id)
  .page({ limit: 50 })
```

Placements are read through the Containment page operation rather than a
generic Yi predicate.

Use Custody lifecycle verbs for held assets:

```ts
await rt.as(alice.uid).transfer(sword.uid, { to: bob.uid })
await rt.as(bob.uid).activate(sword.uid)
await rt.as(bob.uid).deactivate(sword.uid)
await rt.as(bob.uid).extinguish(sword.uid)
```

These operations share the Yi's Domain transaction and Occasion commit with
any other compiled components. They do not scan Yi rows to rediscover a
representation.

See [items](../sdk/items.md), [tokens](../sdk/tokens.md), and
[relationships](../sdk/relationships.md) for product-oriented examples.
