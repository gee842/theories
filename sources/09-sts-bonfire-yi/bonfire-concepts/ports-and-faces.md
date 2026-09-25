# Ports and discovery

A port is a typed executable operation declared on a Kind. The Kind's compiled
interface and presentation surfaces determine how clients discover it; runtime
dispatch resolves the exact installed handler artifact.

## Authoring

`defineHandler` returns a deeply frozen artifact with an id, digest, ABI, input
schema, and implementation provenance. `definePort` references that artifact
and declares its gate. `defineKit` carries the exact artifacts referenced by
its Kinds.

Every executable port requires a runtime schema. String-only handler names,
ambient registry lookup, and schema-less executable ports are invalid.

```ts
const SendHandler = defineHandler(
  '@mycommunity.channel:send',
  t.object({ body: t.string() }),
  async (ctx) => ctx.streams.send(ctx.target, ctx.args.body),
)

const SendPort = definePort(SendHandler, { gate: ChannelMemberGate })

const Channel = defineKind('@mycommunity:channel', {
  family: ChannelFamily,
  facets: [ChannelIdentity, ChannelStream, ChannelMembership],
  ports: { send: SendPort },
  presentation: ChannelPresentation,
})
```

## Discovery surfaces

`PortableKitInstallSourceV3` carries exact typed interface and presentation
surface bytes with aliases, parameter slots, descriptions, and explanations.
Callable operations are derived from the referenced ports and their
schema/gate digests. Any semantic surface change changes revision identity.

Discovery reads the target Yi's committed binding revisions and returns only
the operations visible to the caller. It never assembles operations from
optional row fields or runtime-added method bags.

## Runtime dispatch

Each Runtime owns one handler registry and each registration carries its
RuntimeScope token. Duplicate references in one Runtime fail; equal references
in different Runtimes remain isolated. Async `dispose()` removes only the
owning scope's registrations.

Trusted process handlers, installed workflows, sandbox handlers, DSL handlers,
and application handlers use one `PortHandlerContext`, one schema/gate/Authority
envelope, one `BonfireError` identity, and one Occasion transaction. Nested
commands join the active Occasion.

## Local and remote parity

World's local and connected modes expose the same typed transport contract.
Generated relations, Signals, Views, projections, and port operations must be
implemented over the default remote transport if they are advertised.

See [Ports, gates, and certificates](port-gate-grant.md) and the
[kit author guide](../kit-author-guide.md).
