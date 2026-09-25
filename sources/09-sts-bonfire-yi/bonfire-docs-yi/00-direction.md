# Yi — The Engineering Direction

> **Status: committed direction.** This is no longer an "ideal" or a hypothesis. It is the engineering
> target the codebase is built toward. The conceptual model that realizes it is [`01-frame.md`](01-frame.md);
> the decisions + route are [`02-pivot.md`](archive/02-pivot.md); the architecture is [`03-architecture.md`](archive/03-architecture.md);
> the phased, parallelized plan with verifiable tasks is [`04-execution-plan.md`](archive/04-execution-plan.md).

---

## The direction

**Yi makes _being_, _having_, _doing_, and _permitting_ one composable substrate.**

Most systems choose one center:

- Actor systems center on message-passing actors.
- ECS / game engines center on entities with components.
- Graph DBs center on relations.
- Object-capability systems center on possession of authority.
- Social platforms center on accounts, groups, posts, feeds, and permissions.
- Blockchains center on ownership and verifiable state.

**Yi combines these without making one of them the hidden "real" model.** The distinctive thing:

> **A Yi can become subject, object, capability, actor, container, member, tool, or policy-holder through
> composed Kinds and context-owned state _without changing its root identity_.**

Concrete examples:

- A **sword** is an item, but can also hold an agent, expose ports, grant abilities, track history, and act
  under gates.
- A **community** is a container, but also a subject that owns capabilities, delegates moderation, runs
  agents, and publishes streams.
- A **membership** is not just an ACL row; it is a Yi whose Relations occurrence and composed facets can
  carry scope, expiry, role, audit, revocation, and behavior.
- A **Kind family** is immutable governed law, so it can be versioned, migrated, composed, installed, and
  inspected without pretending that law is another Yi root.
- A **capability** is not an external permission bit; it is something you can hold, lend, attenuate, revoke,
  explain, and invoke.
- An **agent** is not a bolted-on bot account; it is a Yi whose effective Kind bindings, Identity principal,
  and Authority state permit it to act.

The best version is **not** "everything is one table." It is:

> **Everything is one kind of meaningful thing, while storage, indexes, fan-out, presence, messages, feeds,
> and moderation can be specialized where scale demands it.**

That is the rare part. Most systems either get conceptual elegance and lose operational reality, or get
operational reality and hard-code the product concepts. **Yi keeps both.**

---

## How the four verbs map to the compiled model

The direction is organized around four questions (see [`01-frame.md`](01-frame.md)). Kind authors answer
them with composed Kinds, semantic facets, ports, and gates; the compiler closes those declarations into an
immutable binding revision and representation plan.

| Verb | Primitive | Meaning |
|---|---|---|
| **being** | an effective **Kind binding** | the composed semantic law a Yi carries (projected as `bindings[]`) |
| **having** | a context-owned **component** | what Custody holds, Containment places, or Relations connects |
| **doing** | a **port** — its firing is a *moment* | what it can do |
| **permitting** | a **gate** plus Authority contributions | who may cause it, and which certificates or policies justify that decision |

`Yi` is the one runtime noun. Its root joins effective Kind bindings and schema-validated authored state
with normalized components owned by Identity, Custody, Containment, Relations, Authority, and the other
bounded contexts. Positions such as subject, object, holder, child, parent, and relation endpoint belong to
those context components; they are never storage categories disguised as Kinds. **Agency is explicit**:
every Yi is addressable, while acting requires the appropriate Identity and Authority state.

---

## The seven enablements — as verifiable goals

These are what the direction enables that most systems do not handle elegantly. Each is restated as a
**verifiable acceptance goal** (G1–G7 measure capabilities; **G8** measures the cognitive budget the whole
pivot exists to protect). The execution plan ([`04-execution-plan.md`](archive/04-execution-plan.md))
schedules the work; these goals are how we know it is done. An enablement is *not* "achieved" until its
acceptance test passes with automated tests.

### G1 — Item-as-agent
**The item _itself_ can be active** — not "spawn a bot linked to an item."
**Verify:** one Yi carrying the item, Identity, and agent Kind bindings plus ports **signs its own action,
receives a trigger, and fires a gated port — with tests** — while Custody remains the sole owner of its
holder state.
Custody (who writes), signing (the witness/`identity`), gate-authorization (may it fire), and holder-transfer
remain four separate axes. An item delegating to a separate agent Yi is allowed only as a **delegation**
pattern, never as the meaning of an active item.

### G2 — Capability-carrying objects
Objects grant **real authority** by being held, equipped, joined, delegated, or activated.
**Verify:** a capability Yi whose compiled facets bind Custody or Containment state to an Authority
certificate authorizes the holder while it is held or equipped. Moving, transferring, extinguishing, or
revoking the relevant context component denies the next invocation. Tests cover grant, attenuation,
revocation, discovery, and invocation without copying the capability's ports onto the holder.

### G3 — Kinds as live governed law
A Kind is not just schema: its family has genesis, semantic contributions, owner policy, evolution,
migrations, ports, presentation, and export policy. It is authored through `defineKind` and
`defineKindFamily`, compiled as immutable Kinds-owned law, and installed with its exact Kit artifacts.
**Verify:** installing a family commits its canonical contributions, surfaces, handler artifacts, aliases,
migrations, and export policy together. A semantic change produces a new immutable binding revision;
declared evolution governs upgrades, while incompatible law forks to a new family identity.

### G4 — Unified product composition
Community, channel, role, inventory, quest, API key, bot, plugin, post, and session are **specialized Yi
patterns**, not separate app-specific concepts first.
**Verify:** each composes from Kind/family references and typed context facets rather than product-specific
storage branches. Acceptance scenario: a 100-person community with channels, conditional Authority
certificates, plugins, and miniapps is built from Relations membership, Streams, Custody, and Authority
contributions, with the closed representation plan selected by the compiler rather than hand-picked at
runtime.

### G5 — Explainable authority
"Why can Alice do this?" traces through held item, group membership, delegated capability, port gate, role,
and policy as **one graph of cause**.
**Verify:** a single `explain(caller, target, port)` returns one connected trace spanning all of those
sources — not a per-port gate tree beside scattered imperative `auth.ts` branches and ad-hoc traversals.

### G6 — Agents inside the permission world
Agents do **not** escape the model. They act only through held capabilities, scoped delegation, and auditable
ports.
**Verify:** an agent has no privileged class and no backdoor; every action is a gated port invocation under a
held capability or scoped delegation, and every durable action is part of one auditable Occasion commit.
Tests assert no ambient authority.

### G7 — Social + programmable world in one substrate
Discord-like communities, MMORPG-like items/roles, Bluesky-like identity/views, and actor-like message
dispatch **share primitives without being the same storage path**.
**Verify:** these surfaces are all expressed as Yi roots, composed Kind bindings, semantic context
contributions, ports, and gates over one ontology. Their normalized Custody, Containment, Relations,
Authority, Streams, and View representations remain context-owned and index-backed — proven by the
integration scenario in G4 plus a performance bar on the hot paths.

### G8 — The cognitive budget
The pivot's whole reason for being is **the fewest concepts a developer must hold** (the least-cognitive-
resistance frame). G1–G7 measure *capabilities*; G8 measures *the budget itself* — so the program cannot win
on features while the concept count silently regrows.
**Verify:** phase-neutral CI gates pin the measurable proxies — the single Kind authoring front door, one
dispatch lane, one Occasion commit spine, context-owned storage, and the absence of alternate representation
classifiers — across Core, Server, SDK, and Std. Product patterns such as sessions must compile from the same
family references and semantic contributions as every other Yi. The held-concept count is defended by
executable structure and public-surface checks, not asserted by prose.

---

## The two halves the direction must keep together

1. **Conceptual elegance** — one kind of meaningful thing; the four questions; no hidden center. Owned by
   [`01-frame.md`](01-frame.md).
2. **Operational reality** — storage, indexes, fan-out, presence, messages, feeds, and moderation specialized
   below a seam, with the index-backed hot paths preserved. Owned by [`03-architecture.md`](archive/03-architecture.md)
   and built per [`04-execution-plan.md`](archive/04-execution-plan.md).

The failure mode to avoid is **rhetorical victory before engineering closure**: if a doc says "the item
itself acts," the first milestone must make it literally true in witness resolution, trigger dispatch, ports,
and tests (G1). Every enablement above carries an automated acceptance test; none is "done" on prose.
