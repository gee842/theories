---
name: hero-as-principal
description: "Current auth stance: human account bearers act as their subject; delegation is explicit"
metadata:
  node_type: memory
  type: project
  originSessionId: 5741b7cc-3c58-4c34-9e13-cae7425631b2
---

Human account bearers resolve directly to the account subject as `asCaller`;
login does not manufacture or select a default agent. Agents are opt-in beings
created through `agents.create`.

API-key bearers are the distinct delegated path: the key resolves to its holder
as `asCaller` and presents the bonded delegation holding as `actingAs`, which
core validates before substituting the delegation subject.

Do not reintroduce a default-agent login pipeline or ambient human-session
elevation. The former `sessionItemUid`/`core:session_item` detail is obsolete;
the current core session workflow installs `core:channel-read-state` and
`core:conversation-participant` via `ensureSessionKinds`.
