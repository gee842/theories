# Spirits

> Where this page and source-anchored docs disagree, `llms.txt` and the cited
> source files win.

A spirit is an addressable agent: a Yi whose effective Kind binding includes
an Identity principal contribution. People, bots, groups, channels, and
sessions are common product nouns for spirits; they are not separate storage
representations.

## Yi denotation, principal state, and containment

The facts are deliberately separate:

- Kinds owns the stable Yi `uid`, exact root binding, and immutable Creation;
- the existing `Identity` code module owns mutable principal profile,
  liveness, canonical path, parent edge, and their revisions; and
- Containment owns placement.

Code that retains a reference should retain the `uid`. Path lookup resolves
through the indexed `identity_principals` repository.

Containment is independent of Identity. A placement records child, parent,
slot, order, lifecycle, and CAS revision in `containment_placements`. Moving a
spirit updates that component; it does not rewrite authored Kind state or
infer the Yi's representation from fields.

## Authoring an addressable Kind

Portable Kinds declare explicit family genesis and an Identity facet:

```ts
import {
  defineKind,
  defineKindFamily,
  defineHandler,
  defineKit,
  definePort,
  facet,
  public_,
  t,
} from '@bonfire/sdk'

const GreetHandler = defineHandler(
  '@mycommunity.greeter:greet',
  t.object({ name: t.string() }),
  async (ctx) => ({ message: `hello, ${ctx.args.name}` }),
)
const GreetPort = definePort(GreetHandler, { gate: public_ })

const Greeter = defineKind('@mycommunity:greeter', {
  family: defineKindFamily({
    lineageId: `klin_${'17'.padStart(64, '0')}`,
    nonce: `knonce_${'17'.padStart(64, '0')}`,
  }),
  facets: [facet.identity.principal({
    name: 'mycommunity.greeter',
    agency: 'initiate',
    keyCapability: 'ed25519-v1',
    recoveryStrategies: [],
  })],
  rowSchema: { greeting: t.string() },
  gates: {
    discover: public_,
    add: public_,
    remove: public_,
    mutate: public_,
  },
  ports: { greet: GreetPort },
})

const GreeterKit = defineKit('pkg:mycommunity.greeter', {
  kinds: [Greeter],
  handlerArtifacts: [GreetHandler],
})
```

The compiler validates the Identity contribution, closes the family, and
records the resulting components in `KindBindingRevisionBodyV2`. Runtime
manifestation follows that committed plan; it never infers an Identity
component from `composes` or optional fields.

## Runtime representation

The Yi root carries its stable UID denotation, primary binding, sequence, and
Occasion head. Its immutable birth is the Kinds-owned Creation record.
Principal profile, liveness, and parent facts live in the existing Identity
repository. Schema-validated authored values live in `yi_kind_state`, keyed by
Yi and binding, and appear in the public authored-state projection.

```ts
const greeter = await rt.as(alice.uid).manifest({
  kind: Greeter.id,
  contexts: {
    identity: { parent: alice.uid, displayName: 'g1' },
  },
  init: { [Greeter.id]: { greeting: 'hello' } },
})
```

If the Kind also declares Custody, Containment, Relations, Authority, Streams,
or other facets, those owners write their own component repositories in the
same Domain transaction and Occasion commit.

## Ports and lifecycle

Ports resolve from the Yi's effective immutable bindings. Their handlers read
authored state through the Yi projection and use context services for semantic
facts such as holder, placement, relation endpoints, or certificate status.

Runtime and Kinds atomically establish the Yi root plus immutable Creation;
Identity may initialize sibling principal state in that same Occasion. After
birth, Identity reparents, renames, or extinguishes the principal without
rewriting the Yi UID, Kind evidence, or Creation. Other contexts own their own
lifecycle operations; generic state patches cannot change them.

See [Yi](yi.md), [Kinds and facets](unified-class.md), and the executable
[hello-bot example](../examples/hello-bot/index.ts).
