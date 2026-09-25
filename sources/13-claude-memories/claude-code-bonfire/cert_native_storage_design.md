---
name: cert-native-storage-design
description: Current certificate-at-rest model and the legacy lowering that still remains
metadata:
  node_type: memory
  type: project
  originSessionId: bbd2e490-701e-4287-99dd-c653730f2ce5
---

Grant authority is stored as compiled Certificate data in
`dimensions['core:certificate']`. The compatibility accessor and bucket
builder are in
`packages/core/src/adapters/authority/certificates-at-rest.ts`; a row without a
valid bucket is not interpreted as a certificate.

`mintGrant` in `packages/core/src/authority/service/grants/grants.ts` accepts
`GrantPayload`-shaped input sugar, compiles it with
`compileLegacyGrantPayload`, and passes the certificate to the Runtime
representation boundary, which writes the bucket rather than an authority
payload. Grant disclosure events derive from current certificate state.

Do not claim all legacy lowering is only a parity oracle:
`compileLegacyScope` still has live compatibility uses in delegation resolution
and holding-mint representation paths. The destination is one certificate
model, but that migration is not complete in the current tree.

Old phase ordering, seed/case counts, and pin rituals are superseded by
[[verification-regime-2026-08-14]].
