# The platform model — communities as operating systems

> **Historical pre-address-reset proposal.** The social model remains useful
> design context, but its global-root and path spellings are not current API
> guidance. Use the canonical address model and current execution plans under
> [`docs/yi/`](../../yi/README.md) for implementation.

> Status: **owner-approved direction** (revision 2, after design conversation
> 2026-06-12). The implementation-grade companion — every mechanism cited to
> code, adversarially verified — is
> [`docs/plans/consolidation/P3-implementation-notes.md`](../plans/consolidation/P3-implementation-notes.md),
> re-derived against this revision. The proposal owns decisions;
> the notes own mechanisms.

---

## The idea in one paragraph

There is **one container primitive: the group** — a spirit with members.
A **community is a group that has been given an operating system**: its own
path, a rulebook (what a member is, what a moderator may do), a surface
(tabs made of views in layouts), and its own belongings (installed apps,
kits, bots). Everything enters the community through **one consent door**,
whether it came from the marketplace, a preset, or a member's conversation
with an agent. Apps are a sigil frontend plus a small data backend, so
building one is a conversation away — and agents operate the whole OS
through the same roles and ports humans use.

## One primitive, one stamp

- A **group** is a spirit with members. That's the whole primitive.
- A **community** is a group with the OS stamp: it lives at its **own
  path** (`c/gardeners` — not under its founder), carries the deployed
  rulebook (`member` with tiers, `moderator`, `channel`, `post`, `vote`),
  the surface config, and holds its own items. One stamp per tree — the
  community is the tenancy boundary that owns role definitions, installs,
  and the bot roster, so "who owns the wishing pool" is never ambiguous.
- **Sub-groups are just groups inside it** — no second OS. They reuse the
  community's rulebook and render inside its shell (a folder, not a second
  desktop). They are addressable, hold their own channels, and their
  members are a subset of the community's.
- **Defaults minimize config; gates make customization unbounded.** A
  sub-group's join rule defaults to *"community members may join."*
  Customizing it means replacing one gate expression: `holds(season-pass)`
  for a token-gated room, `tier(member, atLeast, steward)` for an elders'
  room, any composition the gate vocabulary can say. Because gates are
  data, the swap can be made from the UI, from the SDK, or **by an agent
  someone asked in chat**.
- **Growing up is built in:** a sub-group that outgrows its home
  **graduates** into its own community — the existing `graduate`
  transition primitive, doing what it was named for.

## The surface: views, layouts, tabs

A flat tab list can't say what Hearth is — chat in the main pane with
witness book, wishes, needs, and presence beside it. So the surface config
is a small tree:

- **Views** are the atomic units: chat, forum, feed, roster, the kit
  panels — and **any sigil**, which is the escape hatch: a view nobody
  shipped is a miniapp someone codes (or asks an agent to code).
- **Layouts** arrange views. v1 ships two: `single`, and `main + sidebar`.
  That covers the launch trio exactly.
- **Tabs** are the named entries in the community's nav.

```
tab "hearth"  → main+sidebar:  chat(#hearth) | witness · wishes · needs · presence
tab "forum"   → single:        post list (sort: top)
tab "arcade"  → single:        sigil (the guessing game)
```

**Launch presets: hearth, discord-like, reddit-like.** A preset is a full
starting config — tabs and layouts, kits to install, bots to propose,
the role family. Choosing one at founding is the entire setup; everything
it configured remains editable afterwards, piece by piece.

## Apps: built by talking

The scenario this is designed around: a member who may not code asks the
community's builder-agent in chat for a guessing game with a leaderboard.

1. **The agent replies with the game, in the thread.** Sigil replies in
   chat are the development loop: people play it inline, ask for changes
   in plain language, the agent posts revisions. In-thread sigils run
   readonly in the sandbox, so iteration is zero-risk.
2. **The backend is a small deployed kind, not a write capability.** The
   game saves scores by invoking ports on its own `game-score` kind —
   schema-validated, member-gated. The app never holds raw write access;
   its ports are its syscalls, and the port gate is the boundary.
3. **Installing goes through the consent door.** The agent bundles sigil +
   kind spec + a manifest of what it needs, and files an install request.
   **Default: a moderator approves** everything that enters the community —
   apps, bots, kits, preset contents. The founder can loosen that, but the
   consent record always exists, *even for the founder's own agent*.
   Install deploys the kind under the community's path, whitelists exactly
   the app's own ports for its sigil, records provenance, and can promote
   the game from a chat message to a tab. Uninstall is the existing
   provenance + revert machinery.
4. **v1 app backends are append-only.** Records in, derived reads out —
   the leaderboard is "max score per player," computed at read, which is
   also the honest way (you store every submission and derive, rather than
   trusting a client that claims only its best counts). Constraints ride
   the gate vocabulary: members-only, one-per-member, rate limits. This
   covers scores, polls, signups, inventories, guest books. **Sandboxed
   user handlers** — communities running their own server-side logic —
   are the explicit *next* milestone, not scoped now: the moment
   "community OS" stops being a metaphor.

## Presets and the marketplace are the same thing

A preset is a distribution image; a marketplace listing is the same bundle,
published. A member's homegrown app is an unpublished marketplace item with
an audience of one community — publishing it later is a flag, not a
rewrite. Bundles may **propose** bots; the founder **consents** at install.
Daemons are added by the owner, never smuggled in.

## Agents are operators, not exceptions

- Agents join through the same door as humans, bear the same member label,
  rank the same tiers, and can hold the moderator role.
- Every config surface is a port, so an agent with the right role can do
  whatever a human with that role can: reconfigure tabs, swap a
  sub-group's join gate, approve an install — usually because someone
  asked in chat.
- **Hero-as-principal holds throughout:** an agent acts as itself, with a
  human at the root of its authority chain; acting *for* a human stays the
  separate, explicit delegation path.

## What this deletes

- `admin: true` booleans and client-invented role ids → deployed roles.
- Kits registered in memory, re-registered each boot, first caller's
  identity baked in globally → durable per-community installs; two
  communities with the same kit are fully isolated.
- Items owned by `sys` (and the "which hearth's witness book?" ambiguity)
  → items owned by the community.
- The flat global Groups list → groups live inside communities.
- Hearth as a 1,363-line bespoke page → Hearth as the first preset.

## Decision register

**Decided (this revision):**

1. **One primitive:** group = spirit + members; community = group + OS
   stamp; sub-groups are plain groups inside; `graduate` is the upgrade
   path.
2. **Communities own their path** (`c/gardeners`), not a slot under their
   founder.
3. **Surface = view / layout / tab tree.** v1 layouts: single,
   main+sidebar. Launch presets: hearth, discord-like, reddit-like.
4. **Sub-group defaults + gate-expression customization** — default join
   is community-members; any gate expression may replace it (token-gated,
   tier-gated, composed); humans, SDK, and agents all edit it through the
   same port.
5. **One consent door** for everything entering a community. Moderator
   approval by default; founder may loosen; the consent record always
   exists.
6. **App model:** sigil frontend + kind backend invoked through its own
   ports; v1 backends are append-only records + derived reads + gate
   constraints; sandboxed user handlers are the named next milestone.
7. **Preset = distro image; marketplace = the same bundle, published.**
   Bots ride bundles as proposals, added only on founder consent.
8. **Agents are first-class operators** via the same roles and ports;
   same join gate as humans by default (restricting is one line per
   community); delegation stays explicit.
9. Roles v1 = fixed family (tiered member + moderator + founder), door
   open for author-defined roles. Votes: up-only, post-level, new/top
   sorts.

**Deliberately deferred:** community transfer / sovereignty mechanics ·
local sub-group roles · comment-level votes and "hot" ranking · plugin
registry as the *only* install path · sandboxed user handlers.

## Why this is solid

Nothing here invents substrate. The gate vocabulary (tiers, holds,
requires-with-directions), durable kind deploys with ownership and
evolution checks, anchored sessions and the message DAG, the sigil sandbox
with per-source whitelists, plugin provenance + revert, and agent runners
all exist on main today — the join loop is already CI-executed end-to-end.
The genuinely new pieces are deliberately few: the shared community root,
the view/layout schema, the install door, the generic app-data backend,
and the chat-to-tab promotion path. The implementation notes pin each one
to code and carry the sequencing against Phase 1.
