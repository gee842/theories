# Relationships

A relationship is a logical Relations occurrence governed by topology and
policy contributions.

```ts
const Friendship = defineKind('@mycommunity:friendship', {
  family: FriendshipFamily,
  facets: [FriendshipTopology, FriendshipPolicy],
  rowSchema: { since: t.iso_datetime() },
})
```

Topology declares direction and the from/to family slots. Policy declares
activation, read visibility, affiliation, and enforceable unextinguished
cardinality per pair/from/to. Relations owns endpoints and lifecycle; authored
state contains only fields such as `since`.

Create and mutate occurrences through Relations operations. Indexed endpoint
queries must not scan Yi rows or infer graph meaning from generic references.

See [SDK relationships](../sdk/relationships.md).
