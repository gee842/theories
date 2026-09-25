# Spirit-token design overview

created: 2026-04-20T08:52:43.496080Z  uuid: b20b24d5-428d-4024-ab6b-3ee4f9903e4e  export: new
messages: 2  total_chars: 5478  human_chars: 47


---
**HUMAN** (2026-04-20T08:52):

concisely but completely my spirit-token design

---
**ASSISTANT** (2026-04-20T08:53):

  Ren's asking me to recall his spirit-token design from the SST architecture work—I need to pull up the specifics from our past conversations since my memory only has the high-level overview.
```
This block is not supported on your current device yet.
```

 I need to distill the SST design into something concise but complete—hitting the three core primitives, the recursive loop, and the capability-first auth model without getting bogged down in spec details.# SST — Spirit / Space / Token

A capability-based protocol for social systems and agent ecosystems. Three primitives, one recursive relationship, no ambient authority. Humans and agents share the same API.

## The loop

```
Spirit ──has──▶ Space ──contains──▶ Token ──held by──▶ Spirit
```

- **Spirit** — an identity (human or agent). Structurally a Space with identity metadata (keypair/DID) attached. No fourth primitive.
- **Space** — a container/scope. Holds Tokens. Can nest sub-Spaces.
- **Token** — a typed relational *edge* with a payload. Binds a Spirit's capability into a Space.

Everything else — membership, roles, channels, chats, credentials, agent assignments, miniapp installs, payment auths — is a Token of some schema, held by a Spirit, scoped to a Space.

(Naming: spec/code says "Sprite"; "Spirit" is the public-facing term. Same primitive.)

## Capability-first

Every action requires presenting a Token. No "Alice is admin therefore X" — only "here is a proof chain that authorizes X." UCAN-style. Consequences:

- Agents are first-class — a delegated UCAN is indistinguishable from a human-presented one.
- Delegation = issuing a Token. Sub-delegation = issuing a Token bound to a parent Token.
- Revocation is lazy — revoke parent, dependent Tokens fail resolution. Re-grant reactivates them. No cascading deletes, clean audit trail.
- No central permission table. Authority lives in the proof chains.

## Schemas + hooks

A Schema defines: payload shape, **traits** (string tags consumed by access rules), and **hooks** (declarative rules firing on lifecycle events: issue, transfer, delegate, resolve, revoke). Traits replace inheritance — `admin-role` declares `traits: [community_participant, community_admin]`, so a rule checking `community_participant` accepts both admins and members. No diamond problem, independent lifecycles.

## Token-as-edge (the discipline)

Tokens carry **relationships and pointers**, not content. A `chat` Token says "these Spirits are in a chat together" with payload `{service: "matrix", room_id: "..."}` — actual messages live in the chat backend. Spaces stay lean: a Spirit with 500 connections, 50 credentials, 10 chats has ~600 Tokens, not millions of rows. SST is the graph; implementations hang off the edges.

## Privacy & visibility

Tokens default to holder-only visibility. Discoverability is opt-in via schema declaration. A Spirit's Space is not a public profile.

## Extension (prototypal)

Modeled as a Token of schema `extends`. `706-Shenzhen-Hub` extends `706`; the resolver walks the extension chain when looking up issuable schemas. Sub-communities, regional chapters, persona variants, agent specializations — all without `parent_id` columns anywhere.

## Embedded Spirits in Tokens

A Token's payload can reference a Spirit whose lifecycle is bound to that Token (e.g., an agent attached to a chat dies when the chat is revoked). Lets agents be *granted* like capabilities.

## FUSE realization

SST maps cleanly onto Unix:

| SST | Filesystem |
|---|---|
| Space | Directory |
| Token | File (payload = content, proof chain = xattrs) |
| Spirit | Directory + identity file |
| Issue / Resolve / Transfer / Share / Revoke | `create` / `read`+capcheck / `rename` / `link` / `unlink` |

The FUSE daemon **is** the runtime. Every syscall becomes a protocol op. The Unix toolchain becomes SST-native.

A Spirit on disk:

```
/sst/spirits/agent-7/
├── .identity         # keypair, DID
├── .hooks.yaml       # event → handler (nervous system)
├── .state.json       # persistent state
├── handlers/         # executable hooks (reflexes)
├── tokens/           # held UCANs (capabilities)
├── inbox/  outbox/   # message queues (trigger on file write)
└── workspace/
```

The daemon enforces the capability ceiling — an agent can write any hook it wants, but the daemon refuses to register hooks exceeding the agent's actual UCAN authority. Agents self-modify by rewriting their own files; daemon reloads on change.

## Mycological composition

No central orchestrator. Agent A writes to B's inbox → B's hook fires → writes to C's inbox → C's hook fires. Pipelines emerge from filesystem topology plus each Spirit's *local* hook declarations. Composition by environment, not by wiring.

## Why three (not two, not four)

- **Two** (merge Space and Token): loses cognitive clarity, makes resolution ambiguous.
- **Four** (add token-spaces, schema inheritance): imports OOP complexity into a capability system.
- **Three** with rich relationships (containment, holding, binding, extension): the sweet spot.

## Open at v0.1

Hook DSL expressiveness (declarative now → CEL/WASM later), schema versioning/migration, federated cross-instance resolution, rate limits as first-class hooks, E2EE within Spaces, offline/local-first sync for edge agents, multi-sig governance primitives. And the still-unresolved question of whether `token.agents[]` should be a top-level field or kept inside the payload.
