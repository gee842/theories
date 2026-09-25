# Ports, gates, and certificates

A port is a typed operation declared on a Kind. A gate decides whether a caller
may invoke it. Authority certificates carry durable, revocable authorization
evidence when a gate needs more than structural policy.

## Handler artifacts

`defineHandler` returns a deeply frozen artifact. `definePort` references that
exact artifact and supplies its runtime schema and gate. `defineKit` carries
the exact handler artifacts used by its Kinds.

```ts
const UnlockHandler = defineHandler(
  '@mycommunity.key:unlock',
  t.object({ door: t.string() }),
  async (ctx) => ({ opened: ctx.args.door }),
)

const UnlockPort = definePort(UnlockHandler, { gate: custodyHolder() })

const Key = defineKind('@mycommunity:key', {
  family: KeyFamily,
  facets: [KeyCustody, KeyAuthority, KeyPlaceable],
  bindings: [
    bindFacet.authoritySubjectFromCustodyHolder({
      custody: KeyCustody,
      authority: KeyAuthority,
    }),
    bindFacet.authorityActiveInContainmentSlot({
      authority: KeyAuthority,
      containment: KeyPlaceable,
      slot: 'key',
    }),
  ],
  ports: { unlock: UnlockPort },
})

const KeyKit = defineKit('pkg:mycommunity.key', {
  kinds: [Key],
  handlerArtifacts: [UnlockHandler],
})
```

The compiler validates handler identity/digest/ABI, runtime schemas, referenced
contributions, endpoint and slot artifacts, execution class, and deciding
owner. A string with the same handler name is not an executable artifact.

## Runtime isolation

Each Runtime owns one registry. Equal handler references in different
Runtimes are isolated; duplicate references within one Runtime fail.
Disposal removes only registrations owned by that Runtime scope.

All execution classes use one `PortHandlerContext`, one error contract, one
schema/gate/Authority envelope, and one Occasion transaction. Nested commands
join the active Occasion.

## Cross-facet authority

Possession, relation membership, containment placement, and certificate status
remain facts of their owning contexts. A multi-facet Kind connects them only
through typed `bindFacet.*` contributions. Moving, transferring, extinguishing,
or revoking the key therefore changes authorization in the same atomic commit;
no copied boolean or payload field can drift.

Certificates name issuer, subject, optional presenter, coverage, use policy,
and revocation consistency. Child certificates may only narrow their parent.
One-use policies are enforced by Authority's use counter.

## Discovery and invocation

Interface surfaces are compiled from exact port artifacts and their schema/gate
digests. Aliases, parameter slots, descriptions, and explanations travel in
`PortableKitInstallSourceV3`. A surface change changes its revision identity.

Invoke the concrete Yi that carries the port. Holding it never copies the port
onto the holder. Remote and local Worlds use the same typed transport contract.

See [Authority](authority.md), [Kinds and facets](unified-class.md), and the
[kit author guide](../kit-author-guide.md).
