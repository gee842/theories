# Tokens and certificates

Bonfire separates conserved assets from issued authority.

- Custody owns fungible/unit quantity, holder, transfer, split, consolidation,
  activation, and extinction.
- Authority owns certificates: issuer, subject, presenter, canonical bytes,
  use count, issuer epoch, and revocation.

Declare a balance with `facet.custody.asset(...)` and fungible quantity. Declare
an instrument that authorizes actions with `facet.authority.role(...)`. When a
single Yi intentionally carries both, connect them with `bindFacet.*`.

```ts
const Credits = defineKind('@mycommunity:credits', {
  family: CreditsFamily,
  facets: [facet.custody.asset({
    name: 'mycommunity.credits',
    quantity: { kind: 'fungible', decimalScale: 2 },
    transfer: 'whole-or-partial',
    extinguish: 'whole-or-partial',
    consolidation: 'explicit-merge-same-holder',
    holderLoss: 'cascade',
    maxUnextinguishedPerHolder: 'unbounded',
  })],
})
```

Use `certificate` for Authority instruments. The word `claim` is reserved for
Automation/Settlement work claiming.

See [SDK tokens](../sdk/tokens.md) and [Holdings](holdings.md).
