---
name: keypair-accounts-shipped
description: "Native ed25519 keypair signup/login is on main; current routes, credential split, starvation marker, recovery, and PoW"
metadata:
  node_type: memory
  type: project
  originSessionId: ea0da350-3970-4231-8240-d98f951fdbfd
---

Native keypair accounts are on main. `packages/server/src/server/routes/key.ts` serves `POST /auth/key/nonce` and `/auth/key/verify`: the browser signs a single-use, origin-bound challenge with an ed25519 key; `lookupOrCreateAccountByKey` creates on first sight and logs in on later sightings. `key_credentials` is part of `packages/server/migrations/001_init.sql`.

The login key is **not** the Yi's identity key. The account is a normal anonymous human Yi with its own substrate identity keypair; the client's public login key exists only in `key_credentials`. This preserves server-side event signing while keeping signup free of email, phone, or username.

Fresh self-signups bear `core:new-account`, whose authority pre-guard denies `spirit.create`. `packages/server/src/auth/account-lifecycle.ts` removes that marker after recovery binding; `/auth/key/provision` is sys-admin-only and creates an already-vouched account. Adaptive proof-of-work lives in `packages/server/src/auth/pow.ts` and is off unless `BONFIRE_KEY_POW` enables it.

Operational gotchas:

- Client and server must construct the same canonical sign-in message and origin or signature verification fails.
- The web implementation uses `@noble/curves/ed25519` directly; importing the Node-oriented `@bonfire/core` runtime barrel into the browser bundle is unsafe.
- Marker add/remove calls act as `kernel.uid`, the account's structural ancestor; a bearer cannot remove its own probation marker.

The old branch-only status, migration number, `sys/new-account` id, seed-count checklist, and public-snapshot regeneration ritual are obsolete. Verification work follows [[verification-regime-2026-08-14]].
