# Items

An item is usually a unit Custody asset whose Kind declares product state and
ports. It is not a separate runtime row family.

```ts
const UseHandler = defineHandler(
  '@mycommunity.tool:use',
  t.object({}),
  async (ctx) => ({ used: ctx.target }),
)
const UsePort = definePort(UseHandler, { gate: custodyHolder() })

const Tool = defineKind('@mycommunity:tool', {
  family: ToolFamily,
  facets: [ToolCustody],
  rowSchema: { condition: t.number() },
  ports: { use: UsePort },
})

const ToolKit = defineKit('pkg:mycommunity.tool', {
  kinds: [Tool],
  handlerArtifacts: [UseHandler],
})
```

Manifest the holder and quantity through typed `contexts.custody` input and
store only `condition` under the Kind's authored state. Invoke `use` on the
concrete tool Yi. Placement belongs
to Containment, and issued authority belongs to Authority; add those facets and
bindings only when the product needs them.

See [SDK items](../sdk/items.md) and [Holdings](holdings.md).
