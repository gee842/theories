# SDK elegance exploration

> **Status:** living exploration ledger, not an implementation plan.
>
> This document records desired SDK qualities, current friction, candidate
> surfaces, constraints, and unresolved questions. We will keep changing it as
> we explore. Only after the important questions have convincing answers should
> this material be distilled into an implementation plan.
>
> **Baseline reconciliation — 2026-09-02:** Plans 51 and 52 are implemented
> and release-certified in the direct baseline. Their Creation, reference,
> graph-read, View, query-frame, and generation contracts are current truth for
> this exploration, not candidate architecture.

## Purpose

Bonfire already has unusually strong semantic machinery: exact Kind and
installation binding, actor/subject separation, current Authority evaluation,
revocable certificates, context-owned facts, durable Occasion commits, and a
single World-facing product direction. The SDK should make that power feel
small, direct, and natural without weakening or concealing those laws.

The desired experience is object-oriented in the original capability sense:
developers receive meaningful objects, pass them to collaborators, and invoke
the verbs those objects make available. Registry coordinates, transport DTOs,
binding revisions, and Authority envelopes remain exact underneath, but appear
in ordinary code only when they matter.

This exploration builds on
[SDK structural direction](sdk-one-model-direction.md). That document describes
the larger one-model architecture; this one concentrates on elegance,
capability-shaped use, and the amount of code and API vocabulary a developer
must carry.

## How we will use this document

- Record observations before proposing a solution.
- Mark candidate syntax as provisional; an attractive snippet is not yet a
  semantic design.
- Keep security, lifecycle, exactness, and failure behavior beside ergonomic
  proposals rather than treating them as later implementation details.
- Prefer removing concepts from daily use over merely shortening their names.
- Test ideas against typed builders, source-free participants, autonomous
  agents, local tests, and connected Worlds.
- Defer sequencing, migrations, work packages, and release gates to the later
  implementation plan.

## Elegance scorecard

An improvement should be evaluated against all of these, not only line count.

| Quality | Question |
| --- | --- |
| Small vocabulary | How many Bonfire-specific nouns and verbs must ordinary code learn? |
| Local readability | Does code read as objects doing domain actions? |
| Authority visibility | Is it clear what authority is passed, retained, narrowed, or stripped? |
| Exactness | Can a convenience silently float to another install, Kind revision, target, actor, or subject? |
| Progressive disclosure | Can a newcomer succeed without learning the substrate, while an expert can inspect the exact lowering? |
| Type flow | Do authored names and schemas flow through creation, actions, Views, snapshots, and delegation without duplicate declarations? |
| Runtime honesty | Does every typed promise have a corresponding runtime check and portable representation? |
| Failure clarity | Do missing, invisible, denied, ambiguous, stale, exhausted, and unsupported cases remain distinguishable where safe? |
| Capability confinement | Can a handle be passed without unintentionally exposing a broader World, transport, token, or target set? |
| Local/remote parity | Does the same product code retain its meaning in tests, in-process runtimes, and connected Worlds? |
| Mechanical weight | What do imports, generated types, bundle size, round trips, and setup ceremony cost? |

## Current baseline worth preserving

The elegance work should project these existing strengths rather than replace
them:

- `connect()` owns authenticated transport resources and can reach multiple
  Worlds.
- `World` is the actor-bound product and governance root.
- `install(Kit)` is governance and returns an exact bound Kit; `use(Kit)` is a
  read-only exact binding.
- `world.yi(uid)` begins untrusted; exact and family verification are explicit.
- bound Kinds and Yi retain exact installation and binding revision evidence.
- one Yi root and one immutable Creation record are written atomically;
  callers cannot supply or rewrite Creation origin through the SDK create
  input.
- a Yi UID, a principal ID, mutable principal profile/liveness/parentage, exact
  Kind evidence, and immutable Creation are distinct facts and references.
- definitions remain pure; declaring a Kind or Kit does not connect or mutate.
- Authority is evaluated from current evidence, not cached SDK permission.
- actor, beneficiary subject, presenter, target, and Authority evidence remain
  distinct.
- Kind dependency, Yi effective Kind membership, and semantic projected graph
  reach remain distinct. Creation lineage and mutable principal ancestry are
  separately owned lenses over one private bounded traversal kernel.
- Views compile once to one logical operator DAG and execute through a private
  `QueryReadFrame`; neither is public graph state or cached Authority.
- live Views may use the admitted projected traversal capability. Durable
  Views are non-graph and publish through prepare -> build -> activate.
- lifecycle reuse remains a protocol pattern over exact operation attribution
  and Occasion commits, not a universal service, interface, registry, or state
  machine.
- advanced and substrate mechanisms remain available through explicit review
  boundaries rather than `.raw` peers on daily objects.

## Baseline reconciliation: completed Plans 51 and 52

The normative sources are [Plan 51](../yi/51-state-lineage-transition-spine.md),
[Plan 52](../yi/52-compiled-dag-query-planner.md), and their
[implementation ledger](../yi/51-52-implementation-status.md). Both plans
changed the direct baseline. There is no V2 surface, compatibility reader,
dual write/materialization, inferred historical backfill, or migration path to
preserve in the SDK redesign.

### Plan 51 facts the SDK must project

The implemented identity and provenance chain is:

```text
authored Kind
  -> BoundKind.kind + exact binding revision
  -> verified Yi.kind
  -> Yi.ref                         inert UID-only designation
  -> Yi.creation.read()             immutable born-as/origin fact
  -> Yi.creation.lineage(bounds)    bounded projected creator chain
```

These values answer different questions. A newly verified handle may use a
new exact binding, while the Kind recorded at Creation never changes. A
principal rename changes profile, reparenting changes the principal-parent
edge, and extinguishing changes liveness; none changes the Yi UID, existing
Kind evidence, or Creation.

`YiRef` and `PrincipalRef` are intentionally disjoint. `YiRef` contains only a
UID plus its type-only Kind witness. `PrincipalRef` contains only a principal
ID plus its private type-only witness. Neither reference is profile, ancestry,
liveness, Kind evidence, or Authority. The SDK must not introduce a generic
`IdentityRef` or cast between them because a row happens to connect them.

Creation is generated and validated at the Kinds/Runtime boundary. The public
creation command carries authored state, initial context facts, and Activation
bindings, but no creator or complete origin. An Action birth derives its
creator from the exact invoked Yi and authorized binding; a ceremony may carry
one separately owner-selected creator; deferred work restores the original
semantic producer instead of attributing the queue worker. This is why a more
elegant create input may rename or regroup manifestation fields but may never
offer `creator`, `origin`, or a constructible Creation object.

The current daily read is already small:

```ts
const creation = await yi.creation.read()
const lineage = await yi.creation.lineage({ maxDepth: 32 })
```

`lineage()` is bounded, root-first, and closed by `complete`, `redacted`,
`external`, `unavailable`, or `max-depth`. There is no public descendant scan,
generic graph session, exact graph constructor, or traversal mode switch.
Graph reach never authorizes an operation.

### Plan 52 facts the SDK must project

View authoring now has one certified language with two explicit delivery
states:

```ts
const roster = view.materialized('active-members', { /* non-graph plan */ })
const ancestry = view.live('ancestry', {
  /* bounded creation.creator or principal.parent traversal */
})
```

Both lower to one strict portable declaration and one installed logical DAG.
The distinction is a capability law, not stylistic naming:

- materialized authoring cannot express traversal;
- forged traversal-plus-materialized bytes reject at decode and install;
- generation independently rechecks non-graph eligibility before source work;
- live traversal consumes only Runtime's projected graph capability;
- `QueryReadFrame` is private, execution-scoped, non-serializable, and cannot
  be retained or resumed as an SDK session;
- View-level admission never implies source/lens admission, and the complete
  frame is revalidated before disclosure; and
- public cursors seal semantic continuation and exact plan/access/read state,
  never a graph scope, repository cursor, snapshot, or general Authority
  token.

The current public handles are exact and deliberately asymmetric:

```ts
await materialized.page(tie, { limit, cursor })
await materialized.count(tie)       // only when declared
await materialized.has(tie, member) // only when declared

await live.query(root, { limit, cursor, signal })
```

An ergonomic wrapper may make tie/root binding and iteration feel more alike,
but it cannot erase which delivery contract is held. In particular, async
iteration must remain bounded page composition over an exact handle; it cannot
imply an unbounded stream or a durable query object.

Durable View updates use two atomic publication pointers with one permanent
readiness invariant:

```text
prepare exact access candidate
  -> build and publish complete immutable generation
  -> fenced activation rotates the public selection
```

`serve-last-complete` keeps the prior ready selection current during a build;
it is not a reader fallback or dual-read branch. Traversal-bearing Views are
live-only. Graph-backed durable generation remains rejected until a separate
architecture proves owner change positions, invalidation, caller-neutral
admission, rebuild frontiers, and publication semantics.

### Consequences for this exploration

- We optimize the existing `Yi.creation`, `view.live`, `view.materialized`,
  exact View handles, and bounded results; we do not propose parallel SDK
  products for the same semantics.
- “Creation input” below means manifestation input only. Immutable Creation is
  output/provenance owned by Kinds and is never caller-authored.
- A projected traversal result may contain `YiRef` or `PrincipalRef` according
  to its exact edge. It does not return an executable capability by visibility
  alone.
- Any future result-binding or iteration convenience must preserve current
  generation/read stamps, cursor families, cancellation semantics, and
  live-versus-materialized delivery in types and runtime bytes.
- Similar lifecycle or graph-shaped APIs may share naming patterns, but the
  SDK must not manufacture a universal `Lifecycle`, `Graph`, `Parent`,
  `Entity`, or resumable query session.

### Certification inherited by the baseline

The final 2026-09-02 release sequence passed:

- model: 69 PostgreSQL files / 360 assertions;
- unit: 710 files / 5,020 assertions, plus one intentional skip;
- connected PostgreSQL: 56 files / 270 assertions;
- indexed query plans: 3 files / 22 assertions;
- first-party product canaries: 12 files / 73 assertions;
- strict indexed-path performance, packed SDK consumer, and browser
  production build;
- all 23 indexed examples through build and smoke test; and
- documentation hygiene plus `git diff --check`.

The release sequence initially found only stale reviewed documentation
inventory counts and an obsolete protocol number in `llms.txt`. Both were
corrected and their affected artifact gates reran green. These results certify
the direct baseline; they do not pre-certify any ergonomic candidate in this
document.

The original completion handoff reported 1,041 tracked changes and 219
untracked files before commit. Current repository inspection supersedes that
transient state: `main` and `origin/main` now point at commit `1953aa710`
(`feat: complete unified SDK and Yi architecture`), with this exploration
document as the only working-tree modification. Agent token/time accounting is
operational history, not an SDK design constraint, and is not carried into the
decision ledger.

## Improvement ledger

This is the high-level set of areas we currently want to explore. “Important”
means the area deserves a resolved design before planning; it does not imply an
implementation order.

| Area | Current friction | Direction to explore | State |
| --- | --- | --- | --- |
| Object capabilities | Yi handles designate objects but Authority is primarily presented through a broader World access. Passing a handle does not yet have one crisp authority meaning. | Make product handles honest, attenuated object capabilities, with inert references as an explicit authority-stripping form. | Important; active exploration |
| Object-and-verb projection | Typed actions sit under `.actions`; source-free actions are selected separately and invoked with an explicit target. | Put domain verbs on the target object while reserving one framework/meta surface. | Candidate |
| Source-free use | `discover()` exposes catalog, installation, Kind, action, selector, and invocation ceremony. | Provide a pinned dynamic product projection such as `world.open(...)`. | Candidate |
| Authoring ceremony | Family genesis, addresses, handler IDs, schemas, gates, facet policy, portability policy, and Kit aliases can dominate a small Kind. | Generate stable identity once, infer repeated data, provide honest recipes, and keep exact controls progressively accessible. | Needs deeper audit |
| SDK root API size | The default entrypoint contains the daily model but also a large flat export vocabulary. | Establish a daily vocabulary budget and group specialist authoring/tooling concepts without multiplying product models. | Needs usage audit |
| Core public constitution | Core's internal ownership is strict, but its published root and owner-named subpaths mix portable contracts, semantic services, runtime composition, and host operations. SDK, Std, and Server therefore depend on an import topology whose names do not reliably reveal power or runtime weight. | Define one public role/environment law, make the transport-neutral World product execution path canonical in Core, and let SDK and Server project it rather than reimplement it. | Important; active exploration before planning |
| Manifestation input | `create({ state, birth, activations })` is exact, but `birth` now collides with the precise immutable Creation/birth vocabulary from Plan 51 even though this field means initial named facet facts. | Explore an authored-name-first or `facets`-grouped input that keeps authored state, initial owner facts, and Activation distinct and never accepts caller-authored creator/origin. | Open; constrained by implemented Creation |
| Snapshot and provenance shape | `.state`, named facets, `$`, and `yi.creation` are principled but ordinary observation may still feel framework-heavy. | Keep `snapshot.state` canonical, preserve owner-specific facet projections, and make immutable Creation nearby without flattening it into current state. | State decision settled; navigation open |
| Views and queries | `view.live`/`view.materialized`, compiled plans, and exact `query`/`page` handles are implemented; typed and discovered selection plus paging still feel different. | Bind tie/root first and progressively expose bounded iteration while preserving live/materialized types, exact cursors/read stamps, and data-or-ref result defaults. | Execution foundation settled; ergonomics open |
| References and semantic identity | `YiRef`, `PrincipalRef`, verified `Yi.kind`, and immutable born-as evidence are exact but newcomers can easily treat them as one identity concept. | Teach and project the smallest owner-specific path without adding a generic entity/identity reference or conversion. | Baseline fixed; naming/navigation open |
| Authority authoring | Exact action references and target graph selectors are expressive but verbose and separated from target-bound use. | Compose grants from existing action/target capabilities while keeping issuance World-rooted and attenuation explicit. | Important; coupled to OCap |
| Authority-bearing items | Bonfire items can participate in Authority through Custody and Authority facets, while an SDK object reference is a different kind of possession. | Make the relation between passing a handle, transferring an item, holding an item, and presenting its Authority explicit and useful. | Important; active exploration |
| Errors | Strong error identities exist, but product code may still need too much protocol knowledge to recover well. | Define a small product-level recovery grammar with exact details available for inspection. | Needs transcript audit |
| Lifecycle and resources | Connection disposal is explicit; World/Kit/Yi capabilities, remote tokens, principal liveness, Activation, View generations, and Creation have different lifetimes. | Give them a coherent navigation and failure story while retaining separate owner state machines; do not introduce a universal lifecycle interface. | Open; universal abstraction rejected |
| Explainability | Exact lowering and Authority evidence exist in several places. | Give every convenience one nearby explanation path without putting internals in the normal call. | Candidate |
| Type inference | The SDK carries strong exact types, but phase wrappers and exported helper types are visible. | Preserve exact inference while letting most developers name only their domain Kinds and actions. | Needs type-surface audit |
| Testing parity | The testing package returns the production World model, but fixture setup and actor switching add their own vocabulary. | Make tests read like the same capability-passing product code with controlled factories around it. | Open |
| Agents | Agents correctly have no ambient inherited Authority, but tool exposure and delegation can be verbose. | Pass narrowly attenuated product capabilities directly to agents and make onward delegation visible. | Important OCap proof |
| Performance | Catalog scans, verification, and separate binding/action steps may add round trips hidden by an elegant projection. | Measure transcripts and define where safe batching, pinning, and local projection are allowed. | Needs measurement |
| Documentation | Existing documents explain exact machinery well but the shortest golden path is not yet the organizing center. | Teach one small grammar, then reveal why and how it lowers. | Later synthesis |

## First audit findings

The first pass over the current SDK and examples found several opportunities
that are more specific than general “API cleanup”:

- The root currently exposes 144 runtime values and 167 type-only names. Few
  package entrypoints have successfully removed competing object models, but
  they have not yet produced a small autocomplete or learning surface.
- The ten TypeScript files under `docs/examples` that import the daily
  root most often import `defineKindFamily`, `defineKit`, `portable`,
  `defineKind`, `deployKit`, `facet`, `t`, and `public_`. This suggests that
  declaration and release ceremony—not connection—is the dominant public
  vocabulary in examples.
- Kind compilation already rejects collisions among named facets, actions,
  Activations, `$`, and framework names such as `read`, `find`, `get`, and
  `ref`. The SDK therefore already pays much of the governance cost required
  for direct product projection while still putting invocation under
  `.actions`.
- A schema-authored `defineHandler` already carries its exact input schema and
  inferred argument type. `action({ input, run: handler })` nevertheless
  requires the same schema again and hashes both copies to reject drift.
- `BonfireConnection` and the testing fixture are already `AsyncDisposable`.
  A smaller lifecycle transcript may need documentation and naming changes,
  not another connection API.
- The source-free path has exact installed Kind and Action information, but it
  makes callers independently select the Kind and Action and then pass the
  target back to the selected Action.
- `isBonfireError(error)` recognizes the shared cross-realm brand, but its
  public narrowed `AnyBonfireError` shape omits `.code`; practical recovery in
  the error guide is nevertheless almost entirely code-driven.
- Typed and dynamic Views share exact catalog bindings, but callers must learn
  separate materialized `page(tie, ...)` and live `query(root, ...)` shapes
  before they can simply iterate results.
- `Yi` now exposes the small immutable `creation.read()` / bounded
  `creation.lineage()` surface, and live traversal results construct either
  `YiRef` or `PrincipalRef` only after the exact edge discriminant is checked.
- `BoundKindCreateInput.birth` still names initial facet inputs. That spelling
  predates the now-canonical immutable Creation/birth vocabulary and is an API
  clarity issue even though the wire correctly accepts no creator or origin.
- `view.live` and `view.materialized` are already capability-typed authoring
  states over one compiler. The remaining elegance problem is selection,
  iteration, and result flow—not inventing a new query language or unifying
  their execution lifetimes.
- Core's internal structure map is strong, but the public package currently
  has 49 export paths. Its 787-line root exports 248 runtime values and 294
  type-only names and reaches approximately 737 production Core modules plus
  `node:async_hooks` and `node:crypto` through static runtime edges.
- Core owner-named subpaths do not have one predictable meaning:
  `@bonfire/core/views` reaches about 24 Core modules and `activation` 5,
  while `authority` reaches about 628 and `identity` 625. The latter paths
  include runtime composition and Node built-ins as well as owner contracts.
- The local SDK and connected Server currently contain parallel World product
  semantics: `runtime-product.ts` is 860 lines and Server's `world/catalog.ts`
  is 758. Both own the same catalog digest domain, metadata key, exact install
  checks, and catalog/create/verify/invoke/Activation/transfer flows. Behavioral
  parity is tested, but it is not yet structural because the semantic
  implementation sits above Core in two places.

These are early measurements from the current worktree, not stable release
statistics. Repeat the audit after the surrounding SDK rewrite settles.

## Code comparison gallery

The comparisons below are design probes. “Candidate” means “worth testing
against the scorecard,” not “chosen API.” Each candidate is followed by the
semantic concern that could invalidate it.

### 1. Connection and lifecycle: simplify the transcript, not the ontology

Current teaching:

```ts
const connection = await connect({ endpoint, auth: { token } })
try {
  const world = await connection.world('@hearth')
  // ...
} finally {
  await connection.dispose()
}
```

Candidate using the existing API:

```ts
await using bonfire = await connect({ endpoint, auth: { token } })
const hearth = await bonfire.world('@hearth')
```

Potential improvement: teach the connection as “Bonfire access” and use its
existing `AsyncDisposable` contract. `World` remains a separate product root
because one connection can reach several Worlds and owns the shared transport.

Concern: emitted JavaScript/runtime support for explicit resource management
must match the SDK's supported targets. The conventional `try/finally` form
still belongs in compatibility documentation.

Current assessment: likely keep the connection API. This is an example where
renaming or merging roots would create more concepts than it removes.

### 2. Typed use: make the Yi the domain object

Current:

```ts
const notes = await hearth.use(Notes)
const note = await notes.notes.create({ state: { title: 'Hello' } })

await note.actions.rename({ title: 'Welcome' })

const snapshot = await note.read()
console.log(snapshot.state.title)
```

Candidate:

```ts
const notes = await hearth.use(Notes)
const note = await notes.note.create({ title: 'Hello' })

await note.rename({ title: 'Welcome' })

const snapshot = await note.$.read()
console.log(snapshot.title)
```

Potential improvements:

- singular aliases read naturally when they name a Kind factory;
- direct actions make the verified Yi the one domain object;
- `$` protects authored vocabulary from framework growth;
- authored state may project directly onto creation and observation.

Concerns:

- flattening state requires state-field collision checks against facets,
  actions, Activations, and `$`, including raw JSON Schema declarations;
- `snapshot.state` honestly names the owner of authored data, while flattening
  can make context-owned facets and Kind-owned fields look equally stored;
- moving universally understood `read()` under `$` may be less intuitive than
  the collision safety is worth;
- Kit alias plurality is authored product vocabulary and cannot be silently
  singularized by the SDK.

Variants to compare:

```ts
// Conservative: direct actions only.
await note.rename(input)
const title = (await note.read()).state.title

// Framework namespace, state ownership retained.
await note.rename(input)
const title = (await note.$.read()).state.title

// Fully authored-name-first projection.
await note.rename(input)
const title = (await note.$.read()).title
```

### 3. Source-free participation: open a product, do not operate a catalog

Current:

```ts
const catalog = await world.discover({ include: ['creatable'] })
const posts = catalog.kinds.require({ alias: 'posts' })
const post = await posts.create({ state: { text: 'first light' } })

const rename = catalog.actions.require({ name: 'posts.rename' })
await rename.invoke({ target: post, input: { text: 'welcome' } })
```

Candidate:

```ts
const posts = await world.open('first-world-posts')
const post = await posts.post.create({ text: 'first light' })

await post.rename({ text: 'welcome' })
```

Potential improvement: `open()` performs one exact actor-visible installation
selection and projects the same Kit → Kind → Yi grammar used by `use(Kit)`.
`discover()` remains for browsing and tooling, not as a mandatory product-use
step.

Concern: without local or generated types, property names and inputs are
runtime-validated. Proxy magic must not imply static guarantees or make this
surface impossible to reproduce in other language SDKs. A method-based dynamic
variant may be more honest:

```ts
const posts = await world.open('first-world-posts')
const post = await posts.kind('post').create({ text: 'first light' })

await post.action('rename')({ text: 'welcome' })
```

This is more explicit but gives back much of the ceremony. We need to test
whether generated/pulled types should be the answer for long-lived code while
the dynamic projection optimizes exploration and scripting.

### 4. In-process OCap: pass the whole object or one bound action

Current actor-bound pattern:

```ts
const delegated = world.with({ present: certificate })
const delegatedNotes = await delegated.use(Notes)
const note = await delegatedNotes.note.get(noteRef)

await note.actions.rename({ title: 'Allowed' })
```

Candidate object capability:

```ts
const note = await delegatedNotes.note.get(noteRef)

await runWorker(note) // conveys all capabilities exposed by this note handle
```

More strongly attenuated candidate:

```ts
await runRenameWorker(note.rename) // exact target + exact action + evidence
```

The second form is especially OCap-like: a bound action is itself a callable
capability. Extracting it must retain its target and Authority envelope:

```ts
const rename = note.rename
await rename({ title: 'Allowed' })
```

It must not behave like an unbound JavaScript prototype method whose `this`
can be replaced.

Concern: the handle must capture only the intended evidence. Capturing a broad
World credential and relying solely on hidden fields for confinement is not
enough if any method, result, reflection path, or substrate bridge can recover
that broader access.

### 5. Remote OCap: delegate from the capability being narrowed

Current:

```ts
const certificate = await world.authority.grantTo(agent, {
  allow: {
    actions: [notes.note.actions.rename],
    target: {
      containment: { descendantOf: folder, maxDepth: 3 },
    },
    useBudget: 20,
    delegationDepth: 0,
  },
})

const delegated = world.with({ present: certificate })
```

Candidate for one exact target:

```ts
const remoteNote = await note.$.delegate({
  to: agent,
  actions: ['rename'],
  uses: 20,
  expiresIn: '10m',
})
```

Candidate for a changing graph scope:

```ts
const remoteNotes = await notes.note.rename.$.delegate({
  to: agent,
  on: folder.descendants({ depth: 3 }),
  uses: 20,
})
```

Potential improvement: begin with an existing target/action capability and
describe only the attenuation. Exact action references and target interface
coordinates are inferred from the object being narrowed.

Concern: Authority issuance is constitutionally World-rooted. A convenience on
the capability must visibly lower to the World's Authority ceremony rather
than imply that any Yi can mint Authority. Graph selectors also describe a set
of present and future targets, so they are not equivalent to delegating one
target-bound handle.

### 6. Manifestation input: do not let `birth` mean two things

Current exact form:

```ts
const key = await locksmith.keys.create({
  state: { label: 'Front door' },
  birth: {
    ownership: { holder: alice },
    placement: { parent: keyring, slot: 'keyring' },
  },
  activations: {
    behavior: { /* exact provider bindings */ },
  },
})
```

The current field called `birth` contains initial named facet facts. It does
not contain the immutable Kinds-owned Creation record implemented by Plan 51.
That record is generated atomically and read afterward:

```ts
const creation = await key.creation.read()
// creation.bornAs and creation.origin are immutable evaluator-produced facts
```

The overloaded word is now the primary friction. A caller must never be able
to make this compile:

```ts
await locksmith.keys.create({
  state: { label: 'Front door' },
  creator: forgedCreator,
  origin: forgedOrigin,
})
```

One conservative candidate renames the manifestation grouping:

```ts
const key = await locksmith.keys.create({
  state: { label: 'Front door' },
  facets: {
    ownership: { holder: alice },
    placement: { parent: keyring, slot: 'keyring' },
  },
  activations: {
    behavior: { /* exact provider bindings */ },
  },
})
```

Authored-name-first candidate:

```ts
const key = await locksmith.keys.create({
  label: 'Front door',
  ownership: { holder: alice },
  placement: { parent: keyring, slot: 'keyring' },
  activations: {
    behavior: { /* exact provider bindings */ },
  },
})
```

Potential improvement: named facets retain their authored names from
definition through initial manifestation and observation. The API stops using
`birth` for something other than immutable Creation, while simple authored
data may still receive a generated concise input when its names are
unambiguous.

Constraints now fixed by the baseline:

- create returns the verified Yi capability produced by the operation;
- root plus immutable Creation commit atomically or neither appears;
- the SDK input contains no complete Creation, creator, or origin;
- authored state, context-owned initial facts, and Activation bindings remain
  separately validated owner inputs even if generated syntax projects names;
- Activation retains its own lifecycle and is not another facet/state field;
  and
- a rename, reparent, transfer, move, rollout, or Activation change never
  rewrites Creation.

We should test whether the best solution is generated overloads: the concise
shape for unambiguous Kinds and the explicit `state` + `facets` + `activations`
shape when raw schemas or names prevent safe projection. `birth` should remain
reserved for the immutable semantic fact in new SDK vocabulary.

### 7. Views: make selection first, delivery progressively visible

Current materialized View:

```ts
const page = await notes.views.byOwner.page(alice, { limit: 50 })
for (const cell of page.cells) {
  const note = await notes.note.get(cell.member)
  // ...
}
```

Current live View:

```ts
const page = await people.views.ancestry.query(person, { limit: 20 })
for (const visit of page.visits) {
  // ...
}
```

Candidate shared selection grammar:

```ts
const owned = notes.views.byOwner(alice)
const ancestry = people.views.ancestry(person)

for await (const cell of owned) {
  const noteRef = cell.member // inert YiRef, not an opened capability
}

for await (const visit of ancestry) {
  // visit.node is YiRef or PrincipalRef according to the exact edge
}
```

Exact page and read evidence remain available:

```ts
const page = await owned.$.page({ limit: 50 })
page.$.cursor
page.$.readStamp
```

Potential improvement: all Views first bind their declared tie/root and then
behave as bounded result capabilities. Paging is progressive control rather
than the first operation everyone must learn.

The commonality stops at selection and bounded paging. A materialized binding
reads one ready immutable generation. A live binding opens a fresh private
`QueryReadFrame`, independently admits its sources/lens, and supports the
certified `signal` cancellation posture. They should not inherit from one
runtime `ViewSession`, and only declared materialized capabilities expose
`count` or `has`.

Concern: returning an executable `note` would convey more than the current
projection data or inert `YiRef`. Ordinary View results remain data/refs by
default and require `kind.get(ref)` to open a capability under the receiver's
World access. Async iteration must also retain exact plan/selection/generation
or read-stamp identity, sealed cursor expiry and budgets, whole-frame retry,
and cancellation. It cannot suggest an unbounded graph stream, hide a restart,
persist a live traversal, or wrap a private graph continuation.

### 8. Authoring: remove duplicated coordinates, not semantic choices

Current small Action and Kind excerpt:

```ts
const PostFamily = defineKindFamily({
  lineageId: 'klin_...',
  nonce: 'knonce_...',
})

const rename = defineHandler(
  'first-world/post.rename-v1',
  t.object({ text: t.string() }),
  async (ctx) => {
    await ctx.patch(ctx.target, { [ctx.kind]: { text: ctx.args.text } })
  },
)

const Post = defineKind('@first-world.app:post', {
  family: PostFamily,
  state: { text: t.string() },
  actions: {
    rename: action({
      input: t.object({ text: t.string() }),
      allowed: public_,
      run: rename,
    }),
  },
  gates: {
    discover: public_,
    add: bears('core:human'),
    remove: public_,
    mutate: public_,
  },
})
```

Candidate:

```ts
const rename = define.handler(
  families.post.actions.rename,
  t.object({ text: t.string() }),
  async (ctx) => {
    await ctx.state.patch({ text: ctx.args.text })
  },
)

const Post = define.kind(families.post, {
  state: { text: t.string() },
  actions: {
    rename: define.action(rename, { allow: public_ }),
  },
  access: {
    discover: public_,
    create: bears('core:human'),
  },
})
```

Potential improvements:

- committed family/action tokens remove raw genesis and duplicated addresses;
- a typed Handler supplies the Action input schema once;
- the handler context supplies a target-bound state capability instead of
  requiring the exact Kind bucket coordinate for a self patch;
- unchanged safe access laws come from an explicit recipe or a closed default,
  while exceptional gates remain visible.

Concerns:

- stable Handler identity cannot be derived from mutable variable or record
  names;
- omitting `remove` and `mutate` needs a precise, safe default, not wishful
  inference;
- `ctx.state.patch` must be confined to the current target and exact Kind
  contribution and still participate in the Occasion transaction;
- grouping under `define.*` shortens imports but may not reduce how many
  concepts an author must understand;
- process-local and portable behavior must remain visibly different when the
  selected release cannot carry a trusted closure.

### 9. Common facets: name reviewed semantic recipes

Current unit Custody declaration:

```ts
ownership: facet.custody.asset({
  quantity: { kind: 'unit' },
  transfer: 'whole-only',
  extinguish: 'whole-only',
  consolidation: 'preserve-lots',
  holderLoss: 'detach',
  maxUnextinguishedPerHolder: 'unbounded',
})
```

Candidate reviewed recipe:

```ts
ownership: facet.custody.item({
  holderLoss: 'detach',
})
```

Potential improvement: `item()` is a stable semantic recipe that lowers to the
complete exact policy above and is explainable. It is not a bag of implicit
defaults on the general `asset()` constructor.

Concern: recipes can become a second, drifting ontology. Each must be a pure
expansion over one canonical context contract, versioned when its meaning
changes, and inspectable through the same compiler explanation.

### 10. Errors: make the safe recovery path one guard

Current:

```ts
try {
  await note.actions.rename(input)
} catch (error) {
  if (
    error instanceof BonfireRpcError &&
    error.code === 'PermissionDenied'
  ) {
    // ...
  }
}
```

Candidate:

```ts
try {
  await note.rename(input)
} catch (error) {
  if (isBonfireError(error, 'PermissionDenied')) {
    // error is code-narrowed and retains safe structured details
  }
}
```

Potential improvement: extend the cross-realm guard with an optional code and
make the branded error shape include `.code`. Product code should not need to
know whether a denial crossed RPC, came from an in-process Runtime, or was
raised by a local projection.

Concern: retryable transport failures and authentication lifecycle still have
important category-specific data. A single guard should improve narrowing,
not flatten all errors into one recovery policy. Privacy-preserving opacity
also means some denials must intentionally lack a more specific public reason.

### 11. Testing: keep the production World, remove fixture ceremony

Current:

```ts
const fixture = await testWorld('notes')
try {
  await fixture.world.install(Notes)
  const alice = await fixture.actor('alice')
  const world = fixture.as(alice)
  const notes = await world.use(Notes)
  // ...
} finally {
  await fixture.dispose()
}
```

Candidate using current capabilities:

```ts
await using test = await testWorld('notes')
const installed = await test.world.install(Notes)

const alice = await test.actor('alice')
const notes = await test.as(alice).use(Notes)
```

Candidate fixture convenience to explore:

```ts
await using test = await testWorld('notes', { install: [Notes] })
const alice = await test.actor('alice')
const notes = await test.as(alice).use(Notes)
```

Potential improvement: preinstallation removes governance setup from tests
whose subject is product behavior. The explicit install form remains for tests
of governance, release, and Authority.

Concern: fixture convenience must execute the real `World.install()` ceremony
as the founder and expose receipts/failures; it cannot seed an internal Runtime
shortcut that makes tests prove a different product.

### 12. Public imports: infer types and group tools

Current daily root scale in this audit:

```text
144 runtime values
167 type-only exports
```

Candidate golden application import:

```ts
import {
  connect,
  define,
  facet,
  gate,
  t,
} from '@bonfire/sdk'
```

Most application types should be inferred from authored Kinds, Kits, Yi, and
Actions. Exact compiler, release, migration, raw schema, and protocol types can
remain available through explicit specialist entrypoints.

Concern: moving names to many subpaths can reduce autocomplete while making a
real application import several modules and learn the same concepts. The audit
must distinguish a small learning surface, a small bundle, and a small export
count; they are related but not identical goals.

## Six accepted design choices in detail

This section turns six recurring questions into explicit alternatives. The
selected alternatives are accepted design decisions. Their exact syntax,
lowering, compatibility, and implementation mechanics remain exploratory until
the later plan.

### Choice 1: should snapshots flatten `state`?

Current canonical shape:

```ts
const snapshot = await note.read()

snapshot.state.title
snapshot.ownership.holder
snapshot.$.bindingRevisionId
```

#### Option A: keep `state` canonical

```ts
snapshot.state.title
```

Pros:

- preserves the semantic owner: `state` is authored by the Kind, while named
  facets are projections of context-owned facts;
- cannot collide with facet, Action, Activation, or framework names;
- works uniformly with raw JSON Schema, dynamic Kinds, and Kinds whose field
  names are not statically enumerable;
- preserves a coherent fallback for an untyped `Yi<unknown>`, whose visible
  authored state may contain several Kind buckets;
- schema evolution can add a state field without unexpectedly colliding with a
  newly installed facet or action surface;
- serialization and `Object.keys()` have one unsurprising representation.

Cons:

- adds ceremony to the most common read;
- makes a domain object feel like a storage DTO;
- creation and observation repeat a framework partition developers may not
  care about for simple Kinds;
- destructuring is less natural: `const { title } = snapshot.state` rather
  than `const { title } = snapshot`.

#### Option B: flatten typed state fields onto the snapshot

```ts
snapshot.title
snapshot.ownership.holder
snapshot.$.bindingRevisionId
```

Pros:

- the snapshot reads like the authored domain object;
- state, creation input, and handler vocabulary can reuse the same field names;
- TypeScript inference and destructuring are excellent;
- removes one framework noun from daily product code.

Cons:

- state fields can collide with facets, Actions, Activations, `$`, and future
  framework names;
- adding a state field or facet can become a public-surface breaking change
  even when its underlying semantic contract is otherwise compatible;
- raw/dynamic schemas cannot always prove collision safety ahead of time;
- it visually erases the distinction between Kind-authored state and
  context-owned facts;
- an unverified or multiply represented Yi has no single obvious state object
  to flatten;
- typed and dynamic snapshots may acquire different shapes.

#### Option C: expose both forms

```ts
snapshot.title
snapshot.state.title
```

Pros:

- supports migration and lets developers choose brevity or explicitness;
- makes simple examples concise without immediately removing the canonical
  representation.

Cons:

- creates two public representations of the same fact;
- equality, enumeration, serialization, spread, schema validation, and docs
  become confusing;
- every new field needs alias/collision behavior;
- tends to preserve compatibility sugar indefinitely.

#### Option D: keep the snapshot exact, add a state-only read

```ts
const { title } = await note.$.state()
const full = await note.$.read()
```

Pros:

- keeps the full snapshot semantically honest;
- makes the common state-only read concise;
- avoids collision and dual-property problems.

Cons:

- adds another read verb and possible round-trip expectation;
- encourages product code to ignore context-owned facts;
- `state()` can be mistaken for live mutable state rather than an immutable
  observation.

Decision: keep `snapshot.state` as the one canonical representation. Direct
Actions, concise creation, source-free opening, and OCap passing
remove more ceremony with less semantic loss. Test a state-only convenience
only if complete transcripts show `snapshot.state` remains a dominant burden.
Do not expose simultaneous flattened and nested aliases.

### Choice 2: are all verified Yi capabilities?

There are three semantic objects to distinguish:

```text
YiRef<K>       inert UID designation with a type-only expected Kind witness
Yi<K>          verified executable handle
Certificate   durable/exportable Authority evidence
```

#### Option A: every verified `Yi<K>` is an object capability

Obtaining a Yi through a World access attenuates that World to one exact target
and installed interface. Passing the Yi passes its callable authority
in-process.

```ts
const note = await notes.note.get(ref)
await runWorker(note)
```

Pros:

- one executable object model: if an object has a verb, passing the object
  passes the ability to call that verb;
- matches OCap intuition and avoids hidden ambient lookup at every call site;
- the handle can be confined to one target and exact operation set;
- `note.rename` can be an even narrower callable capability;
- `YiRef<K>` becomes the clear authority-stripping form.

Cons:

- code accustomed to treating handles as harmless data may accidentally leak
  authority by returning or caching one;
- `get()` and View hydration become security-sensitive capability-opening
  operations;
- a handle may expose methods that current policy later denies, so developers
  must learn that capability method presence is not a cached allow;
- capturing a broad actor credential behind a narrow object is safe only if
  the implementation prevents every escape or recombination path;
- debugging must show which evidence envelope the handle captured without
  exposing reusable secrets.

#### Option B: verified Yi are inert; only explicitly derived values are capabilities

```ts
const note = await notes.note.get(ref)       // verified executable Yi handle
const editable = await note.$.cap(['rename'])
await runWorker(editable)
```

Pros:

- least-authority passing is visually explicit;
- Values returned from reads and Views are safer by default;
- the exact operation set can be selected at capability derivation;
- accidental leakage of a normal verified object conveys less power.

Cons:

- introduces two Yi-like public models and an extra conversion ceremony;
- if the “inert” Yi can still invoke through ambient World authority, the
  distinction is cosmetic and misleading;
- if it cannot invoke, the ordinary typed object no longer carries its domain
  verbs;
- application code repeatedly asks for capabilities it already has standing
  to use.

#### Option C: one `Yi` type whose authority mode is conditional

```ts
Yi<Note, 'inert'>
Yi<Note, typeof renameAuthority>
```

Pros:

- can model exact attenuation statically;
- makes returned capabilities and inert results distinguishable in types.

Cons:

- authority depends on current graph state, budgets, expiry, and revocation,
  which TypeScript cannot prove;
- authority generics can infect every function signature;
- dynamic source-free use cannot reproduce the same static precision;
- risks presenting a static authorization guarantee the evaluator does not
  make.

Decision: Option A, with a strict meaning. Every executable verified
`Yi<K>` is a target- and interface-bound in-process capability. `YiRef<K>` is
the inert form. `kind.get(ref)` is intentionally a capability-opening
operation under the receiving World access; `kind.ref(uid)` creates only inert
designation. A method remains callable after revocation but its next operation
must fail current evaluation. Avoid authority generics that pretend to prove a
future allow.

This decision is acceptable only if Views and ordinary data results return inert
references by default, and if no Yi exposes its broader World, transport, or
evidence.

### Choice 3: what do Views and Action results convey?

There are three possible output classes:

```text
data       immutable values/projections
reference  inert designation such as YiRef<K>
capability executable Yi/Action/View handle carrying Authority
```

#### Option A: always return data or inert references

Pros:

- visibility never silently becomes operation Authority;
- passing or serializing results is safe by default;
- pagination, caching, replication, and event logs remain ordinary data flows;
- View evaluation does not need to mint certificates or partition budgets;
- callers deliberately open references under their own World access.

Cons:

- every result needs a follow-up `kind.get(ref)` before domain actions;
- bulk Views can cause N+1 verification/opening round trips;
- capability-oriented pipelines feel interrupted by reference plumbing;
- a creation or issuance Action that naturally produces a usable object needs
  special treatment.

#### Option B: always hydrate visible results into capabilities

Pros:

- extremely fluent application code;
- no explicit open step after a View or Action;
- returned objects carry their verbs immediately.

Cons:

- visibility is not Authority and must never be treated as such;
- merely reading a list becomes a capability distribution event;
- the origin and attenuation of each returned capability are unclear;
- page caching or serialization cannot preserve JavaScript capabilities;
- budget, expiry, and revocation behavior becomes expensive and surprising;
- a View might unintentionally convey broader rights than its own read
  operation.

#### Option C: result contracts explicitly declare data, refs, or capabilities

```ts
const byOwner = view.materialized({
  // default
  result: t.ref(Note),
})

const issueNote = action({
  result: t.cap(Note, { actions: ['read', 'rename'] }),
  // exact Authority derivation required
})
```

Pros:

- authority flow becomes part of the installed interface and reviewable
  declaration;
- ordinary Views remain safe while true capability factories are possible;
- generated types distinguish data, refs, and executable objects;
- runtime can reject a claimed capability result without a valid derivation;
- supports Actions that create, delegate, or issue genuinely new capability.

Cons:

- adds authoring vocabulary and compiler/evaluator work;
- capability-result derivation needs an exact semantic owner and attenuation
  proof, not merely a return-type annotation;
- remote and local execution must agree on sturdy-reference encoding;
- careless authors may choose `cap` for convenience unless policy makes it a
  consequential declaration.

Decision: Option C with safe defaults. Views return declared projection
data or inert typed references by default. Ordinary Action results do the same.
Creation is an explicit built-in capability factory and returns the created Yi.
Any other executable capability result must be declared and proven as an
Authority derivation. Do not add a runtime `hydrate: true` flag that changes
the authority class of one declared View.

Initially, avoid capability-returning Views. Use an explicit Action to issue or
delegate capabilities, because paging over a capability-producing View raises
budget, replay, and revocation questions that need a dedicated law.

### Choice 4: how should remote capability tokens be bound?

These properties are composable rather than mutually exclusive:

```text
bearer bound      possession of token is sufficient
audience bound    token works only at a named World/host/service/protocol
presenter bound   token works only when presented by an authenticated principal
```

#### Bearer token

Pros:

- closest remote analogue to an in-process object reference;
- easy to pass through systems that do not share identity infrastructure;
- supports invitation links, bootstrap, and anonymous workflows;
- possession has one simple meaning.

Cons:

- theft from logs, URLs, storage, telemetry, or process memory immediately
  conveys authority;
- replay and uncontrolled copying are intrinsic unless bounded by use count,
  expiry, and revocation;
- audit identifies the token, not necessarily the human/service that used it;
- onward passing is difficult to distinguish from authorized delegation;
- high-value or long-lived bearer tokens are hazardous.

#### Audience-bound token

Pros:

- prevents replay at another World, host, service, or protocol;
- mitigates confused-deputy and cross-environment token substitution;
- still permits intentional transfer among presenters inside the audience;
- composes naturally with either bearer or presenter binding.

Cons:

- audience coordinates and host migration need exact semantics;
- does not stop theft and replay inside the allowed audience;
- overly narrow audience choices can make federation and service composition
  cumbersome.

#### Presenter-bound token

Pros:

- stolen token alone is insufficient without the presenter's authenticated
  identity/key;
- provides strong attribution and matches Bonfire's existing separation of
  subject and presenter;
- onward transfer requires an explicit delegation ceremony;
- well suited to autonomous agents and durable service access.

Cons:

- recipient must already have an identity/authentication channel;
- less convenient for anonymous invitations and bootstrap;
- device/service rotation and multi-presenter teams require delegation or a
  group-presenter law;
- looks less like pure bearer OCap, though it still represents an unforgeable
  attenuated authority reference.

Decision: every remote token is audience-bound at least to its exact
World and protocol/authority root. The secure default is also
presenter-bound. Bearer-within-audience is an explicit restricted mode for
bootstrap/invitation cases and should default to short expiry, very small use
budget, no onward delegation, narrow operations, and strong result/event
membranes.

In-process JavaScript references remain bearer-like: possession of the object
reference conveys its callable authority. Crossing a trust/process boundary is
where presenter and audience binding become important.

### Choice 5: how should dynamic `open()` expose installed names?

#### Option A: dynamic properties, usually via Proxy or constructed objects

```ts
const adventure = await world.open('adventure')
const sword = await adventure.swords.create(input)
await sword.rename(args)
```

Pros:

- shortest and most domain-like surface;
- mirrors a typed bound Kit;
- excellent for REPLs, scripts, and browsing examples;
- runtime catalog aliases remain visible as authored names.

Cons:

- TypeScript cannot distinguish a valid property from a typo without generated
  types; an index signature can make every typo appear valid;
- Proxy behavior around `then`, inspection, symbols, serialization, and
  reserved names is subtle;
- error timing moves from selection to property use;
- harder to reproduce faithfully in languages without dynamic properties;
- dynamic property collisions can complicate `$`, Views, installation
  metadata, and framework evolution.

#### Option B: explicit selector methods

```ts
const adventure = await world.open('adventure')
const swords = adventure.kind('swords')
const sword = await swords.create(input)
await sword.action('rename')(args)
```

Pros:

- honest about runtime-only names;
- typos fail at an explicit selector boundary with good ambiguity errors;
- no Proxy/thenable/reflection traps;
- maps cleanly to other language SDKs;
- framework names and product names occupy separate namespaces.

Cons:

- string selectors and `action(name)` reintroduce ceremony;
- source-free and typed code look different after binding;
- less pleasant for exploratory scripting;
- passing `sword.action('rename')` is OCap-like but less discoverable.

#### Option C: generated/pulled Kit types only

```ts
import { Adventure } from './bonfire.generated.js'

const adventure = await world.use(Adventure)
const sword = await adventure.swords.create(input)
await sword.rename(args)
```

Pros:

- static names, schemas, results, and autocomplete;
- generated registry can pin exact package/install compatibility;
- same object grammar as locally authored Kits;
- typos and many schema errors fail at compile time.

Cons:

- code generation and committed artifacts add setup and update workflow;
- newcomers cannot immediately use an unfamiliar World;
- stale generated contracts need explicit mismatch behavior;
- unsuitable for generic explorers, CLIs, admin tools, and cross-World scripts;
- generated code can become another model if it does not lower to `use(Kit)`.

#### Option D: hybrid dynamic selectors plus generated typed projection

Use methods for honest source-free selection:

```ts
const adventure = await world.open('adventure')
const swords = adventure.kind('swords')
```

Use generated or local Kits for durable application code:

```ts
const adventure = await world.use(Adventure)
const sword = await adventure.swords.create(input)
```

Both paths converge on the same `BoundKind` and `Yi` capability classes after
selection.

Pros:

- dynamic use remains immediate and honest;
- production code gets static safety and direct properties;
- avoids making Proxy magic constitutional;
- preserves one runtime object model after the binding step.

Cons:

- two selection grammars remain;
- documentation must clearly say when to graduate from dynamic to generated;
- source-free examples are somewhat longer than the pure property form.

Decision: Option D. Make method-based dynamic selection the portable,
honest floor. Make local/generated `world.use(Kit)` the elegant typed path for
long-lived code. A JavaScript property convenience may be explored only as a
thin alias over the method-based contract and must not rely on an “all strings
are valid” TypeScript index signature. Avoid Proxy as the only way to use a
dynamic Kit.

### Choice 6: which authoring omissions have safe defaults?

The useful distinction is not “explicit versus concise.” It is whether a value
is mechanically derivable, safely closed, a named reviewed recipe, or a
consequential product choice.

#### Category A: mechanically derivable — omit safely

Examples:

- Action input schema and argument type from a schema-authored Handler;
- Kit handler-artifact collection from exact Actions carried by its Kinds;
- Kind/action addresses from committed family/action identity tokens;
- local action name from its authored record key;
- exact target and binding revision from a bound Action/Yi capability;
- result TypeScript type from the installed/declared result schema.

Pros: removes duplication without choosing policy. Cons: derivation rules and
identity stability must be inspectable; mutable variable names are never a safe
identity source.

Decision: aggressively remove these repetitions.

#### Category B: least-authority/closed behavior — omission can be safe

Candidate defaults:

```text
Kind discover/create/remove/mutate: deny when omitted
Kit/family export: private and artifact export prohibited
certificate onward delegation depth: 0
undeclared result events: none
View page/query size: bounded
incompatible schema evolution: reject
ambiguous installation selection: fail
```

Pros: omission cannot broaden Authority, portability, resource use, or
compatibility. Cons: a forgotten field creates a definition that is safely
inert but may fail only when used; diagnostics must explain the closed default
clearly.

Decision: permit closed defaults where they make partial definitions
useful, but emit excellent compile/explanation output. Do not default public
access.

#### Category C: named reviewed recipes — concise but fully specified

Examples:

```ts
facet.custody.item({ holderLoss: 'detach' })
gate.publicObject()
authority.agentTool({ expiresIn: '10m', uses: 20 })
```

The recipe expands to a complete versioned canonical contract. Its name is a
semantic promise, not a collection of mutable defaults.

Pros: makes common policy readable and consistent. Cons: recipes can drift,
hide surprising consequences, or become a second ontology unless expansion is
pure, versioned, and explainable.

Decision: use recipes for truly common closed bundles; keep the general
constructors exact.

#### Category D: consequential choices — keep explicit

No universal default is safe for:

- public versus member/holder/role Action admission;
- Custody quantity, transfer, partial transfer, extinction, consolidation, and
  holder-loss law on the general asset constructor;
- Containment parent-loss behavior;
- Relation direction, cardinality, activation, and endpoint-loss law;
- principal parenting/reparenting and agency;
- Authority subject/presenter semantics and target graph scope;
- capability-result derivation;
- Activation provider selection, loss response, restart, and rebind policy;
- external effects, settlement, retries, compensation, and idempotency;
- public artifact licensing/export;
- destructive migration intent;
- accepting requested install scopes or floating to a newer installation.

Making these implicit would shorten declarations by moving product decisions
into undocumented framework behavior.

#### Specific gate recommendation to test

Current authoring requires all four Kind gates. A safe concise form could allow
omission to mean deny:

```ts
const Post = define.kind(families.post, {
  state: { text: t.string() },
  access: {
    discover: public_,
    create: bears(Human),
    // update/remove remain denied
  },
})
```

Use a named complete recipe when all operations intentionally share policy:

```ts
access: gate.publicObject()
```

Do not infer Action admission from Kind mutation policy: invoking a semantic
Action and patching authored state are different operations. `allowed` may be
omitted only if the Action becomes closed/deny; a public or holder-authorized
Action must state or inherit an explicit named Action policy.

Accepted authoring-default rule:

1. derive facts already owned by another exact artifact;
2. default omissions closed, never open;
3. introduce versioned recipes for recurring complete policies;
4. keep lifecycle, economic, Authority, portability, and external-effect
   choices explicit.

## Exploration A: capability-carrying product handles

Object capability design is a central direction, not merely shorter method
syntax.

### Candidate semantic split

```ts
note          // executable, authority-carrying product capability
note.$.ref    // inert, serializable designation; carries no authority
```

Passing `note` to another in-process component would intentionally pass the
authority captured by that handle. Passing `note.$.ref` would pass inert UID
designation only. A target handle would privately bind at least:

```ts
{
  world,
  target,
  exactBinding,
  exposedActions,
  actor,
  subject,
  presenter,
  evidence,
}
```

These are semantic fields, not a proposed public DTO. The implementation must
not expose a broader World, transport, credential, or swappable target through
the handle.

The intended feel is:

```ts
const note = await notes.note.create({ title: 'Hello' })

await note.rename({ title: 'Welcome' })
await runWorker(note)       // intentionally conveys this capability in-process

const ref = note.$.ref      // intentionally strips authority
```

### Same-process and cross-process passing

A JavaScript object reference can be an unforgeable in-process capability. It
cannot cross a process or network boundary as the same reference. Remote
passing therefore needs a sealed, attenuated sturdy reference backed by the
Authority system:

```ts
const token = await note.$.delegate({
  to: agent,
  actions: ['rename'],
  uses: 20,
  expiresIn: '10m',
})

const delegatedNote = await hearth.accept(token)
await delegatedNote.rename({ title: 'Delegated edit' })
```

The spelling is provisional. Semantically, export must not serialize a raw
transport credential or the full Authority of the creating World. Acceptance
must recover the exact target, installed interface, action bounds, subject and
presenter law, validity, budget, and parent evidence.

### Authority-bearing items

Bonfire also supports durable items whose Custody or Authority facets affect
standing. That creates three different operations which the SDK must not blur:

1. passing an in-process capability handle;
2. delegating/exporting attenuated Authority to another actor or process;
3. transferring or changing Custody of the durable item itself.

An SDK handle may carry an item or certificate as evidence. Passing the handle
can convey the captured executable capability without claiming that durable
Custody changed. Conversely, transferring the item can change future Authority
even if an old handle still exists; the next protected operation must evaluate
current state and fail when that standing has disappeared.

We should explore whether an Authority-bearing item naturally projects its
verbs as the capability:

```ts
await key.unlock(door)
await passToAgent(key)
```

and how that relates to domain actions on the target:

```ts
await door.unlockWith(key)
```

The choice should follow the semantic owner of the operation and the intended
direction of delegation, not fluent-API aesthetics alone.

### OCap laws to preserve

- A capability fixes its World, target, exact installed interface, and exposed
  operation set.
- A target or operation supplied by the caller cannot replace the bound one.
- Delegation only narrows targets, actions, subject/presenter bounds, validity,
  budgets, result/event membranes, and onward depth.
- An inert reference cannot reconstruct the stripped evidence.
- Revocation, expiry, budget, Custody, Relation, Containment, and other current
  standing are re-evaluated at the protected operation's consistency frontier.
- A cached allow is never Authority.
- Methods return inert data/references unless their declaration deliberately
  returns another capability.
- Capability composition cannot union two authorities accidentally.
- Dynamic method presence is not itself a promise that current policy will
  allow the next call; denial and revocation remain normal runtime outcomes.
- Explainability can reveal why a call is available without exposing reusable
  secrets or broader evidence.

### OCap questions still open

- Does a handle capture all applicable actor standing, only explicitly
  presented evidence, or a server-issued attenuation of current standing?
- How do capability methods behave when standing changes after construction?
- Can one capability intentionally derive another without returning to a broad
  World authority root, and what evaluator proves the attenuation?
- How are use budgets partitioned across multiple delegated handles?
- When an item grants standing through Custody, what exactly does passing its
  SDK handle confer compared with transferring the item?
- Which operations belong on the Authority-bearing item, which belong on the
  protected target, and which deserve an explicitly composed capability?
- Should `$` contain `delegate`, `attenuate`, `explain`, and `ref`, or should
  capability control have another small, collision-free shape?

## Exploration B: one small object-and-verb grammar

The strongest candidate grammar puts authored actions directly on a verified
target and moves SDK mechanics under one reserved surface:

```ts
const notes = await hearth.use(Notes)
const note = await notes.note.create({ title: 'Hello' })

await note.rename({ title: 'Welcome' })
await note.ownership.transferTo(bob)

const snapshot = await note.$.read()
const ref = note.$.ref
```

Candidate roles:

```text
connection.world(name)  -> World capability/factory
world.use(Kit)           -> exact typed Kit capability
world.install(Kit)       -> governance ceremony returning the same shape
world.open(selector)     -> exact dynamic Kit capability
kit.alias                -> exact Kind capability/factory
kind.create(input)       -> exact Yi capability
kind.get(ref)            -> verified Yi capability
yi.domainVerb(input)     -> target-bound Action invocation
yi.namedFacet.verb(...)  -> context-owned operation
yi.creation              -> immutable Kinds-owned provenance reads
yi.$                     -> inert reference, observation, evidence, capability control
```

Questions:

- Are direct action names worth the collision rules they require?
- Is `$` sufficiently natural across JavaScript, TypeScript, generated clients,
  docs, and other future language SDKs?
- Should `read()` remain a universally obvious top-level verb, or is putting it
  under `$` the cleanest way to protect the product namespace?
- Should Kind creation accept authored names directly, and how are ambiguous
  names between state, initial facet facts, and Activation bindings handled
  without exposing or overloading immutable Creation?
- Does a Kind capability expose action selectors for grants without reusing the
  invocation function as a confusing dual-purpose object?

## Exploration C: source-free Worlds without catalog ceremony

The current dynamic path is exact and actor-filtered but makes the developer
navigate catalog structure manually. Explore a pinned projection:

```ts
const adventure = await hearth.open('adventure')
const sword = await adventure.swords.create({ name: 'Traveler blade' })

await sword.rename({ name: 'Road-worn blade' })
```

`open()` must still:

- bind one exact visible installation and catalog revision;
- reject missing or ambiguous names;
- allow exact package/version/install selection;
- validate dynamic input and output with installed schemas;
- keep action-only creation and visibility laws;
- avoid pretending dynamic properties have compile-time types;
- expose discovery/search as a separate deliberate operation when the caller
  genuinely wants to browse rather than open one product.

We should compare `open`, `use`, `discover`, `find`, and `resolve` as vocabulary.
The typed and dynamic paths should converge immediately after binding instead
of maintaining separate object models.

## Exploration D: authoring compression

Current authoring is exact, but a small Note can require raw family genesis,
an address, a Handler identity, repeated input schema, four gates, a detailed
Custody recipe, export policy, and Kit aliases before the product code begins.
Some of this is essential semantics; some is declaration ceremony or an
advanced choice occupying the daily path.

Candidate direction:

```ts
const Note = define.kind(families.note, {
  state: { title: t.string() },
  actions: {
    rename: define.action({
      input: { title: t.string() },
      allow: public_,
      run: handlers.rename,
    }),
  },
})

const Notes = define.kit('notes', { note: Note })
```

This is only a sketch. Exploration should determine:

- which identities can be generated once into a committed registry;
- whether schema repetition between Action and Handler can disappear without
  losing portable validation;
- which gate defaults are safe and semantically honest;
- which facet policies deserve named recipes;
- whether export policy belongs at family creation, Kit export, publication,
  or an advanced release boundary;
- whether `define.*` grouping truly reduces vocabulary or merely hides a large
  namespace behind one import;
- how declarative portable handlers and trusted process handlers remain visibly
  distinct when execution trust matters.

## Exploration E: reads, Views, streams, and returned capabilities

An elegant write path is insufficient. We need one coherent rule for how data
and authority flow out of reads:

- snapshots are immutable observations, not live capabilities;
- references inside snapshots are inert unless explicitly declared otherwise;
- immutable Creation is read through `yi.creation`, remains distinct from
  current snapshot state, and never authorizes from historical provenance;
- Views return declared data, references, or projected values under the
  accepted default; capability-producing Views remain deferred;
- hydration must not accidentally broaden authority;
- materialized `page` reads an exact ready generation, while live `query`
  executes through one private `QueryReadFrame` and may consume only an
  admitted projected traversal capability;
- traversal-bearing Views remain live-only; graph-backed durable generation
  is rejected rather than simulated or silently downgraded;
- paging and streaming cursors remain exact to their plan/access/generation or
  read frontier, and never serialize a query frame or graph scope;
- subscriptions inherit a deliberate Authority envelope and do not become a
  hidden long-lived permission cache;
- action results that return capabilities must declare the authority derivation
  and lifecycle, not simply return a UID typed as a powerful object.

Candidate feel:

```ts
for await (const note of notes.views.byOwner(alice)) {
  await note.rename({ title: normalize(await note.$.read()) })
}
```

This snippet is only valid if the View deliberately returns executable note
capabilities. Otherwise it should return inert references or projections and
require an explicit capability-opening step.

The current baseline chooses the latter for ordinary Views. A realistic
iteration convenience therefore yields cells, projections, `YiRef`, or
`PrincipalRef`; it does not silently turn visible rows into executable `Yi`.

## Exploration F: failure and explanation grammar

Concise calls make failures more important. A developer should be able to
handle the common product outcomes without learning RPC structure:

```ts
try {
  await note.rename(input)
} catch (error) {
  if (isBonfireError(error, 'denied')) { /* ... */ }
  if (isBonfireError(error, 'stale-capability')) { /* ... */ }
  if (isBonfireError(error, 'not-found')) { /* ... */ }
}
```

The exact spelling and taxonomy need auditing. In particular, we should decide
what callers can safely distinguish without creating visibility or Authority
oracles. Explanation should be nearby:

```ts
await note.$.explain('rename')
```

but must report evaluator evidence rather than reverse-engineering decisions in
the SDK.

## Exploration G: API and import budget

Few package entrypoints do not automatically mean a small API. We should audit:

- runtime values exported from `@bonfire/sdk`;
- type-only exports developers must name in ordinary applications;
- concepts used by the golden connected, testing, builder, participant, and
  agent transcripts;
- exports used only by framework internals, release tooling, migration, or
  advanced authoring;
- tree-shaking and browser bundle effects;
- whether namespaces such as `define`, `facet`, `gate`, and `t` reduce learning
  or only rearrange autocomplete;
- whether specialist concepts can move to explicit entrypoints without making
  one ordinary application import several competing models.

A possible budget to test, not yet adopt:

```text
Runtime nouns: connection, World, Kit, Kind, Yi, View, Certificate
Runtime verbs: connect, world, install, use/open, create/get, domain actions
Authoring roots: define, facet, gate, t
Framework surface: $
```

## Exploration H: entrypoints, exposure, dependencies, and navigation

The entrypoint design is the SDK's information architecture. It decides what a
new developer believes Bonfire is, which dependencies enter their program, and
whether greater power is a visible choice or an accidental import.

### Exposure is a ladder plus lanes

One ordered ladder is useful for operational power:

```text
@bonfire/sdk
    product objects and object capabilities
        ↓ explicit escalation
@bonfire/sdk/advanced
    governance and connected control-plane operations
        ↓ explicit escape hatch
@bonfire/sdk/substrate
    transport, protocol, DTO, query, and dynamic-dispatch primitives
```

This is not the whole package map. Authoring, testing, project tooling, and
provider integrations are different activities, not higher rungs of runtime
Authority:

```text
                         operational power
                               │
      product ───────── advanced ───────── substrate
         │
         ├── authoring lane     pure declarations and schemas
         ├── testing lane       production-shaped test Worlds
         ├── tooling lane       init, inspect, pull, check, publish
         └── integration lane   agents and provider adapters
```

Calling everything an “advanced” layer would hide important distinctions. A
Kit author needs more definition vocabulary, but should not receive more
runtime Authority. A test needs an in-memory World, but that implementation
must not enter a production dependency graph. An AI adapter needs its provider
package, but a participant application should not.

The intended conceptual exposure is therefore:

| Surface | Promise | Excludes by default |
| --- | --- | --- |
| `@bonfire/sdk` | Connect, authenticate, open/use products, and work with capabilities | compilers, test runtime, Node built-ins, provider SDKs, raw protocol |
| `@bonfire/sdk/authoring` | Pure Kit/Kind/View/Action declarations | connections, ambient World access, hosting, provider SDKs |
| `@bonfire/sdk/testing` | The same product object model over disposable test Worlds | legacy parallel clients, production transport, hosting internals |
| `@bonfire/sdk/advanced` | Deliberately requested governance and control-plane operations | compiler/host implementation merely for convenience |
| `@bonfire/sdk/substrate` | Raw protocol and infrastructure escape hatches | daily product aliases and authoring conveniences |
| tooling package | Project lifecycle and code generation | application runtime graph |
| provider adapter package | One optional ecosystem integration | unrelated providers and base SDK installs |

The exact subpaths and package names remain provisional. The separation rule is
more important: split at dependency, trust, environment, and lifecycle
boundaries—not merely because two groups contain different nouns.

### What the current entrypoints reveal

An approximate TypeScript source-graph audit, refreshed after the Plans 51/52
direct cut on 2026-09-02, gives the following runtime reach. This is a
dependency signal, not a bundle-size claim; native ESM evaluation, bundler
tree-shaking, conditional exports, and build output can change actual cost.

| Current entrypoint | SDK source modules reached | Important observation |
| --- | ---: | --- |
| root | 112 | Daily runtime and authoring exports reach compiler/computation code |
| authoring definition path | 44 | A definition-only path is already meaningfully smaller |
| `testing` | 127 | Mixes the converged `testWorld` experience with a broad legacy test substrate |
| `advanced` | 116 | Connected governance is coupled to runtime deployment/compiler helpers |
| `substrate` | 69 | Mixes raw client/protocol concerns with product and compiler utilities |
| `agents` | 11 | Small, but reaches `node:crypto` while the entrypoint is marked browser-safe |
| Vercel adapter | 6 | Correctly introduces Vercel/AI peer dependencies only at the adapter source path |
| Mastra adapter | 5 | Correctly introduces Mastra peer dependencies only at the adapter source path |

The root currently exports roughly 144 runtime values and 167 type-only names.
That does not prove they all enter a bundle, but it does show that “one import”
is not yet the same thing as a small public vocabulary or a small runtime
contract.

Current subpaths communicate intent better than they isolate dependencies.
Specific seams to investigate are:

- move pure declaration builders behind a stable authoring entrypoint;
- keep compilation/lowering out of the participant runtime path, possibly by
  build-time tooling or a lazy authoring-only edge;
- make `testing` mean production-shaped `testWorld`, and relocate raw
  `createTestSubstrate` infrastructure to a visibly lower-level testing path;
- separate the small connected `advanced(world)` facade from Node/host/runtime
  deployment machinery;
- make `substrate` a disciplined primitive layer instead of a collection of
  everything too powerful or inconvenient for root;
- verify browser declarations mechanically against source and built-in imports;
- isolate provider peer dependencies at the package boundary, since npm peer
  dependencies are package-wide even when source entrypoints are separate;
- remove daily reliance on side-effectful prototype augmentation. The existing
  handle-augmentation side-effect list is a warning that surface composition is
  not yet fully explicit.

### Target dependency shape

A candidate dependency direction is:

```text
               tiny shared contracts
          identity · errors · addresses · protocol
                   ↗                    ↖
        product runtime              substrate tools
              ↑                           ↑
        advanced facade              host infrastructure

authoring builders ──→ compiler contracts/lowering
testing ─────────────→ product runtime + disposable implementation
CLI/tooling ─────────→ authoring/compiler + project inspection
provider adapter ────→ provider-neutral agent contract + one provider peer
```

Arrows represent allowed dependencies. They are not public inheritance or new
object models. In particular, root and substrate may share a small internal
protocol layer; root should not import the public `substrate` barrel and then
try to hide it.

Candidate dependency laws:

1. Importing `@bonfire/sdk` must not statically load authoring compilation,
   testing, host/runtime deployment, Node built-ins, or AI providers.
2. Type-only exports must remain type-only edges after build.
3. Authoring definitions must be pure and browser-safe. If lowering is heavy,
   it occurs through an authoring/compiler or tooling edge, not participant
   startup.
4. Testing depends on the public product model; production never depends on the
   test implementation.
5. `advanced` is an explicit power import. Whether it is browser-safe depends
   on the final operations it contains and must be declared truthfully.
6. Provider-neutral agent contracts must not import a provider SDK. Each
   adapter introduces exactly its selected provider dependency.
7. Package splitting follows dependency and deployment boundaries. It must not
   create a second identity, error, certificate, capability, or client model.
8. Every public entrypoint receives automated environment, native-ESM import,
   source-reach, and representative bundle-budget checks.

These laws imply likely package-level separation for CLI/host tools and
provider adapters. Candidate names such as `@bonfire/cli`, `@bonfire/agents`,
`@bonfire/agents-vercel`, and `@bonfire/agents-mastra` illustrate the boundary;
they are not accepted names.

### The root should be a starting point, not a catalog

The root needs very few runtime values. A candidate budget is:

```ts
import {
  connect,
  login,
  signup,
  isBonfireError,
} from '@bonfire/sdk'
```

Types such as `World`, `Yi`, `YiRef`, `Snapshot`, and `Certificate` may be
available for annotations, but ordinary code should infer them from returned
objects. A developer should not have to construct or import `BoundKind`,
`DiscoveredAction`, transport clients, or internal handles to do product work.

The root object tree is the main navigation system:

```text
connection
└── world(name)
    ├── open(name) / use(Kit)
    ├── install(Kit)
    ├── authority ...                 explicit World-scoped operations
    └── product
        ├── kind(name)                dynamic path
        ├── namedKind                 generated/local typed path
        ├── views ...
        └── kind
            ├── create(...)
            ├── get(ref)              opens an executable capability
            ├── ref(uid)              creates inert designation
            └── yi
                ├── authored actions
                ├── authored facets
                ├── creation          immutable read/lineage surface
                └── $                 framework/evidence surface
                    ├── ref
                    ├── read()
                    ├── explain(...)
                    └── delegate(...)  exact spelling remains provisional
```

Autocomplete should reveal the next legitimate operation from the capability
already held. Documentation should not compensate for a flat export catalog.
`$` is deliberately the framework surface, not an unbounded `.raw` peer.

### Four ways a developer starts

The first page and `init` experience should ask what the developer is trying to
do. It should not begin with the substrate architecture.

#### 1. Use an existing product

The source-free path gives value immediately:

```ts
import { connect } from '@bonfire/sdk'

await using bonfire = await connect({ endpoint, token })

const world = await bonfire.world('@hearth')
const adventure = await world.open('adventure')
const swords = adventure.kind('swords')
const sword = await swords.create({ name: 'Dawn' })

await sword.action('rename')({ name: 'Daybreak' })
console.log((await sword.$.read()).state)
```

`kind(...)` and `action(...)` are the honest dynamic selectors in this
transcript. Their exact spelling is provisional, but they do not pretend that
runtime-discovered names are statically known properties.

Once a product matters to the project, inspection and generation graduate it
to the typed path:

```sh
bonfire inspect @hearth adventure
bonfire pull @hearth adventure
```

```ts
import { connect } from '@bonfire/sdk'
import { Adventure } from './bonfire.generated.js'

await using bonfire = await connect({ endpoint, token })

const world = await bonfire.world('@hearth')
const adventure = await world.use(Adventure)
const sword = await adventure.swords.create({ name: 'Dawn' })

await sword.rename({ name: 'Daybreak' })
```

The generated Kit pins or validates exact compatibility and describes the same
bound runtime objects. It is not a generated client competing with `World`.
Direct typed Yi actions remain a provisional surface candidate recorded in the
decision ledger.

The mental path is therefore:

```text
connect → browse/open → try dynamically → inspect → pull → use with types
```

Dynamic discovery is not a second-class API. It is the zero-source entrance;
generated/local Kits are the typed graduation.

#### 2. Author a Kit

An author begins in the authoring lane and stays in ordinary product concepts:

```ts
import { define, facet, gate, t } from '@bonfire/sdk/authoring'

export const Notes = define.kit({
  name: 'notes',
  kinds: {
    note: define.kind({
      state: t.object({ title: t.string() }),
      actions: {
        rename: define.action({
          input: t.object({ title: t.string() }),
          gate: gate.authority('rename'),
          handler: ({ input }) => ({ title: input.title }),
        }),
      },
    }),
  },
})
```

The precise authoring grammar is still under exploration. The key entrypoint
property is that importing definitions does not connect, host, or grant
Authority.

Tests should exercise the production-shaped model:

```ts
import { testWorld } from '@bonfire/sdk/testing'
import { Notes } from './notes.js'

await using test = await testWorld()
const notes = await test.world.install(Notes)
const note = await notes.note.create({ title: 'First' })

await note.rename({ title: 'Second' })
expect((await note.$.read()).state.title).toBe('Second')
```

Install, publish, compatibility checking, and generated artifact production
belong to one project tool rather than several disconnected binaries. A
candidate command family is:

```text
bonfire init
bonfire inspect
bonfire pull
bonfire family add
bonfire check
bonfire publish
```

The command set is provisional. The navigation principle is settled enough to
test: the CLI assists the same World/Kit/Kind/Yi model; it does not invent a
configuration-first product model.

#### 3. Build an agent or worker

The application obtains and attenuates capabilities before constructing agent
tools:

```ts
const note = await notes.note.get(noteRef)
const editor = await note.$.delegate({ actions: ['rename'], budget: 3 })

const tools = toolsFrom(editor)
```

The agent receives the smallest capability-shaped input and no ambient World.
A provider adapter is imported only at the integration edge:

```ts
import { toolsFrom } from '@bonfire/agents'
import { vercelTools } from '@bonfire/agents-vercel'
```

This sketch deliberately separates provider-neutral OCap projection from
provider packaging. Whether provider-neutral agent contracts remain an SDK
subpath or become their own package is open; base SDK installation must not
declare or load every supported agent framework.

#### 4. Operate, govern, or host

An operator begins with the same connection and deliberately imports greater
power:

```ts
import { connect } from '@bonfire/sdk'
import { advanced } from '@bonfire/sdk/advanced'

await using bonfire = await connect({ endpoint, token })
const world = await bonfire.world('@hearth')
const control = advanced(world)

await control.installations.inspect('adventure')
```

Raw protocol work descends one further level:

```ts
import { createSubstrateClient } from '@bonfire/sdk/substrate'
```

The visible import is useful in review: it tells the reader that this module is
not ordinary participant code. Hosting and runtime deployment may warrant a
separate Node-only package rather than making all `advanced` usage heavy or
server-only.

### Documentation is part of navigation

The SDK landing page should present four doors:

1. use an existing product;
2. author a Kit;
3. give narrow capabilities to an agent or service;
4. operate or integrate infrastructure.

The primary quickstart should be source-free and useful before code generation.
Its next step is typed graduation, not a rewrite. Each page should state which
entrypoint it inhabits and why a deeper surface is necessary. Basic examples
must not link to `advanced` or `substrate` as routine workarounds.

Navigation also happens at failure time. Typed errors and `$.explain(...)`
should identify whether the next legitimate move is to request Authority,
refresh an exact binding, pull a compatible Kit, or handle disappearance. They
must not reveal information the actor lacks Authority to observe.

### Choices still open in this exploration

- Is a separate `/authoring` import worth the dependency clarity, or should a
  very small pure authoring language remain at root?
- Do `login` and `signup` belong at root, on a connection namespace, or behind
  an auth entrypoint without fragmenting the first transcript?
- Can definitions remain small and pure while compilation/lowering is loaded
  only by tooling or installation?
- Should provider-neutral agent contracts remain `@bonfire/sdk/agents` or form
  a separate package with the provider adapters?
- Should the unified CLI and host/runtime integration be independent packages?
- Is connected `advanced(world)` browser-safe after host tooling is removed?
- Which exact browser, edge, Node, and bundler environments are contractual for
  each entrypoint?
- What is the minimal runtime contract embedded in or imported by a generated
  Kit artifact?
- Where should raw test-substrate construction live after `testing` converges
  on `testWorld`?

We should decide these with complete project transcripts and measured import
graphs, not by minimizing the number of package specifiers in isolated code
samples.

## Exploration I: where the standard library belongs

`@bonfire/std` is not a fourth rung beneath `substrate`, nor part of the SDK's
operational power ladder. It is ordinary, versioned Bonfire content built above
the SDK authoring language:

```text
application Kits ──→ standard Kits and recipes ──→ SDK authoring contracts

participant code ──→ SDK product runtime ──→ exact installed Kit release
```

The two lines meet when a World binds an exact Kit. A participant can use an
already installed standard product without installing or even importing
`@bonfire/std`. Importing a standard definition conveys no Authority. Opening
it with `world.use(...)` is evaluated under the caller's existing World access;
installing it with `world.install(...)` is a separate Authority-bearing act.

“Standard” should promise reviewed vocabulary, exact family continuity,
portable definitions, stable typed aliases, documented policies, and a release
cadence. It must not mean ambient privilege, kernel status, automatic
installation, or permission to bypass the same evaluator used by third-party
Kits.

### What `std` currently combines

The current package contains 99 non-test TypeScript source files and its root
barrel re-exports examples, community, platform, agent, social, package, token,
generator, and Sigil surfaces. It is also currently version `0.0.0` and marked
private, so it is in-repository vocabulary rather than an installable external
standard-library contract. It currently combines at least four roles:

1. reusable Kit and Kind definitions;
2. authoring recipes such as currency, membership, and voucher factories;
3. trusted-process activation and direct `Runtime` installation helpers;
4. first-party products and server application helpers for communities,
   agents, social flows, and package management.

Those roles have different dependency and trust needs. The package imports
`@bonfire/core`, `@bonfire/core/compiler`, `@bonfire/core/runtime`, internal
computation modules, the SDK root, and `@bonfire/sdk/advanced`. Functions such
as `installStdKit(rt)`, `installAgentKit(rt)`, and `installSocialKit(rt)` accept
a raw runtime and deploy through an advanced runtime target. A root value
import can therefore reach compiler, runtime, portability, and Node crypto
paths even when the caller only wanted one small recipe or helper.

There are also visible navigation inconsistencies:

- package documentation recommends `@bonfire/std/tokens`, but the current
  package export map has no `./tokens` entry;
- documentation names `installCommunity`, while the community surface exposes
  several product-specific installers instead;
- the root duplicates the named `community`, `agent`, and `social` subpaths,
  weakening the isolation those paths appear to offer;
- web code already restricts itself to type-only `std` imports to avoid the
  known runtime/browser dependency path;
- SDK testing fixtures import `std` while `std` depends on the SDK, which is a
  boundary inversion even if those fixtures are not part of the daily root.

This is the same “intent without isolation” issue seen in the SDK, but more
pronounced: `std` currently describes a catalog, an authoring library, a host
bootstrap layer, and a particular application stack at once.

### Candidate standard-library contract

The standard library should contain only things that can behave like a
third-party Kit:

- pure, immutable Kit definitions and typed aliases;
- versioned authoring recipes that return pure definitions;
- portable handler artifacts where the portable execution contract permits
  them;
- inert catalog metadata and exact release coordinates;
- no connection, actor, presenter, runtime, storage, or ambient World;
- no installation, activation, registration, or network effect at import.

Trusted process handlers may accompany a standard Kit, but their trust must be
visible. They should live in a host integration artifact or package rather
than changing the meaning of importing the definition. Likewise, community
HTTP/RPC helpers and server boot flows are application or host concerns, not
standard vocabulary.

Candidate dependency laws for every pure `std` subpath:

1. Depend only on the SDK authoring/schema contracts and tiny shared types;
   never on raw `Runtime`, `advanced`, `substrate`, storage, or core internals.
2. Importing any definition is deterministic and side-effect free.
3. No Node built-in enters a browser-safe definition path.
4. Each Kit or coherent recipe domain is importable without evaluating the
   complete catalog.
5. The SDK production graph never depends upward on `std`; SDK test products
   belong in separate fixtures or test-only packages.
6. Standard handles are the same generated/bound Kit, Kind, and Yi objects as
   every other product. Hand-written `*Handle` classes do not form a parallel
   client model.
7. Installation and handler activation are explicit and reviewable at the
   World or host boundary.
8. Standard releases are exact; `std` does not introduce an ambient floating
   “latest” behind `world.use(...)`.

Plans 51 and 52 add four concrete standard-library conformance laws:

- a standard recipe declares Kind dependencies but never turns those
  dependencies into Yi effective Kind memberships unless an explicit
  `composes` edge says so;
- a standard manifestation helper supplies only its owner-specific initial
  facts and never constructs or accepts complete Yi Creation provenance;
- a standard live View may use only the certified projected
  `creation.creator` or `principal.parent` capability and remains live-only;
  a durable standard View is non-graph and follows the ordinary
  prepare/build/activate publication law; and
- standard public result types preserve `YiRef` versus `PrincipalRef` and do
  not replace either with a generic identity/entity reference.

These are ordinary Kit laws, not privileges attached to the `std` publisher.
They should be covered by the same compiler, installer, memory/PostgreSQL, and
packed/browser consumer checks as third-party Kits.

### How a participant uses a standard Kit

No package import is required for source-free use:

```ts
const world = await bonfire.world('@hearth')
const social = await world.open('social')
const request = await social.kind('friend-request').get(requestRef)

await request.action('accept')({})
```

If the project wants checked local vocabulary, it imports one exact standard
Kit descriptor:

```ts
import { Social } from '@bonfire/std/social'

const social = await world.use(Social)
const request = await social.friendRequests.get(requestRef)

await request.accept({})
```

This is the same dynamic-to-typed graduation as any installed product.
`Social` is not a privileged client and does not connect independently.

An authorized operator installs that same definition:

```ts
import { Social } from '@bonfire/std/social'

await world.install(Social)
```

This replaces the daily need to obtain a raw runtime and call a special
standard-library installer:

```ts
// Current host-shaped usage
await installSocialKit(rt)

// Candidate product-shaped usage
await world.install(Social)
```

If `Social` requires trusted host code, installation can report that declared
requirement and the host can activate the reviewed implementation through an
explicit host surface. `world.install(Social)` must never silently register
arbitrary local process code on a remote host.

### How an author uses standard recipes

Recipes help author another Kit; they do not install products themselves:

```ts
import { define } from '@bonfire/sdk/authoring'
import { currency } from '@bonfire/std/custody'

export const Market = define.kit({
  name: 'market',
  kinds: {
    credit: currency({ symbol: 'CR', decimals: 2 }),
  },
})
```

The exact names are provisional. The important property is the dependency
direction: the application owns `Market`; the standard recipe returns a pure,
reviewable declaration and has no runtime installation powers.

### Exposure candidates

A single package with explicit subpaths may be sufficient if every path is a
real dependency island:

```text
@bonfire/std/catalog      inert discovery and release metadata
@bonfire/std/custody      asset recipes
@bonfire/std/social       one typed standard Kit
@bonfire/std/agent        one typed standard Kit
@bonfire/std/sigil        one typed standard Kit
@bonfire/std/community/*  deliberately selected community Kits
```

The root `@bonfire/std` could be metadata-only or omitted as a runtime barrel.
Re-exporting every Kit from root would recreate the current problem. Package
separation is warranted when a domain has a different owner, release cadence,
host dependency, or deployment environment; subpaths are enough when the
boundary is only catalog organization and they remain mechanically isolated.

`community` deserves particular scrutiny. A reusable roster or invitation
recipe may be standard vocabulary, while an entire community operating system,
presets, server reads, founding ceremony, and deployment helpers may be a
first-party product package rather than “the standard library.” Incubator
content should remain opt-in and never be re-exported from a stable root.

### Open `std` decisions

- Which existing definitions are genuine cross-product standards, which are
  reusable recipes, and which are Bonfire first-party applications?
- Should `@bonfire/std` have a runtime root at all, or only a catalog plus
  explicit domain subpaths?
- Can every shipped standard handler be portable, and where do the remaining
  trusted host implementations live?
- Are factories such as `makeCurrency` stable semantic recipes or temporary
  authoring conveniences that should become SDK facet vocabulary?
- Should community, platform, and package-management products have independent
  packages and release cadences?
- What exact release object does a `std` subpath export for `world.use()` and
  `world.install()`?

These decisions should be made by running the participant, author, operator,
browser, and host transcripts for one small standard Kit and one process-backed
Kit. A low source-module count alone cannot prove that the trust boundary is
correct.

## Exploration J: Core as the public dependency constitution

The SDK can be elegant at the call site and still be architecturally expensive
if the Core API below it has the wrong seams. Core decides where semantics are
implemented, which contracts can travel to a browser, which modules receive a
raw Runtime, and whether local and connected behavior share one implementation
or merely try to remain equal through tests.

This is a different audience from the daily SDK. Most application authors
should never import Core. Core's elegance is therefore not measured by whether
a product developer can write one short import. It is measured by whether a
framework maintainer can identify the smallest correct dependency, whether the
import reveals its environment and power, and whether one semantic law has one
implementation owner.

### Strong internal structure does not settle the public API

Core's internal architecture is a strength to preserve. `structure-map.json`
assigns a dependency kernel, fifteen bounded contexts, eight shells, explicit
cross-owner grants, and five protocol monopolies. The structure checker rejects
cycles, unowned production files, internal barrels, unauthorized owner edges,
oversized semantic modules, and duplicate declaration/dispatch/commit/
Authority/View compiler owners.

The package boundary answers another question. It currently publishes 49
entrypoints over approximately 1,017 production modules. The 787-line root is
both described as a kernel contract and tested as the Runtime boot surface. It
exports raw Yi/accessor contracts, messages, Kind and gate vocabulary, package
operations, signing, observability, and `createRuntime`. That is effectively a
portable-contract audience and a Node host audience sharing one barrel.

An approximate static runtime source-graph audit gives this shape:

| Entrypoint | Runtime values | Type-only names | Core modules reached | Node built-ins reached |
| --- | ---: | ---: | ---: | --- |
| root | 248 | 294 | 737 | `node:async_hooks`, `node:crypto` |
| `browser` | 53 | 39 | 29 | none |
| `address` | 17 | 23 | 5 | none |
| `computation` | 12 | 8 | 4 | none |
| `activation` | 14 | 26 | 5 | none |
| `views` | 10 | 19 | 24 | none |
| `compiler` | 128 | 80 | 137 | none |
| `custody` | 6 | 11 | 391 | `node:async_hooks`, `node:crypto` |
| `kinds` | 13 | 6 | 381 | `node:async_hooks`, `node:crypto` |
| `occasion` | 33 | 20 | 504 | `node:async_hooks`, `node:crypto` |
| `composition` | 123 | 151 | 558 | `node:async_hooks`, `node:crypto` |
| `identity` | 97 | 30 | 625 | `node:async_hooks`, `node:crypto` |
| `authority` | 113 | 102 | 628 | `node:async_hooks`, `node:crypto` |
| `runtime` | 36 | 83 | 709 | `node:async_hooks`, `node:crypto` |
| `errors` | 3 | 2 | 2 | none |

“Modules reached” follows runtime imports and re-exports in the TypeScript
source graph. It is not an npm size or bundled-byte measurement; tree-shaking
and conditional loading may reduce shipped code. It is still a useful
architectural measure: it shows what an entrypoint is allowed to know and which
environment assumptions can enter through it.

The important problem is not simply that several numbers are large. It is that
the path name does not predict the role:

- `views` is contracts, codecs, and a small compiler;
- `activation` is similarly contract-oriented;
- `authority` combines certificates and gates with current invocation context,
  World issuance, revocation, issuer epochs, administration, and Runtime
  composition;
- `identity` combines addresses, pure path logic, key operations, creation,
  extinction, reparenting, Runtime projections, and administration;
- `occasion` combines observations and recovery contracts with a Runtime reader
  and the settlement/outbox pump; and
- `yi` sounds like the primitive model but currently exports one Runtime-backed
  readable-row projection plus storage query types.

An owner noun alone therefore cannot tell a consumer whether it is importing a
portable value contract, the semantic service, an ambient execution frame, or
a host operation. Adding more noun-named paths without a role convention would
make the package larger without making it easier to reason about.

### The downstream cost is already visible

A production-source import census shows how the ambiguous root becomes a type
pantry and convenience barrel. Counts below are files; a mixed import may count
once in each column.

| Consumer | Core root runtime imports | Core root type imports | What it reveals |
| --- | ---: | ---: | --- |
| SDK | 4 | 49 | Portable SDK contracts and local Runtime implementation both shop at the same root |
| Std | 32 | 74 | Pure definitions, trusted Handler code, and raw Runtime helpers are not isolated |
| Server | 94 | 91 | A legitimate host consumer still depends on a large flat catalog rather than a cohesive host boundary |
| Web | 0 | 0 | Web uses only `@bonfire/core/browser`, demonstrating that a real environment boundary can stay narrow |

The exact adapter-SPIs are a positive counterexample. A storage or context
adapter can import its named port without receiving the default Runtime. The
compiler, address, errors, Views, and Activation paths also show that one npm
package can provide useful dependency islands; a package split is not required
for every boundary.

Core root breadth affects the downstream SDK in four ways:

1. SDK types are tempted to re-export Core implementation vocabulary because
   it is already convenient and globally available.
2. Runtime-only dependencies can enter code believed to be portable through a
   harmless-looking owner import.
3. Std can accept `Runtime` and call Core services directly, becoming a host
   layer instead of ordinary authored content.
4. Server and local SDK code can each assemble the same operation from low-level
   helpers, so the SDK grammar is only a facade over duplicated semantics.

Shrinking SDK autocomplete without correcting these edges would improve the
front door while retaining the architectural pressure that made it broad.

### The more important issue: World product semantics have two owners

The current local and connected World paths are transport-equivalent but not
structurally single-sourced:

```text
Core primitives and Runtime services
        ├── SDK runtime-product.ts          local World semantics
        └── Server methods/world/catalog.ts connected World semantics
```

The SDK file is 860 lines and the Server file is 758. Both define the same
catalog digest domain and World-Kit metadata key, and both implement exact
installation checks, catalog projection, create, verify, invoke, Activation,
and Custody transfer flows. The Server additionally binds RPC authentication,
presentation, rate limits, and public serialization; the local path binds a
trusted in-process access object. Those are legitimate adapter differences.
Exact Kind matching, product visibility, manifestation, Authority dispatch,
and result semantics are not.

The protocol types also flow upward from `@bonfire/sdk/substrate` into Server.
That makes the consumer SDK partly own the contract by which the host exposes
Core semantics. Tests can detect many divergences, but every new operation or
security correction still has two implementation sites.

The target dependency should be:

```text
                     Core portable product contract
                                  │
                     Core World product execution
                                  │
                 ┌────────────────┴────────────────┐
        SDK local adapter                  Server RPC adapter
                 │                                 │
        SDK product handles             SDK connected transport
```

Core should own one transport-neutral execution boundary for installed World
products. Server should own authentication, framing, admission limits, and
serialization. SDK should own the application-facing World/Kit/Kind/Yi object
projection and local/remote transport adaptation. Neither SDK nor Server should
reimplement the semantic product operation.

One candidate host-side shape is:

```ts
const execution = runtime.worldProducts.bind({
  world: exactWorld,
  actor: authenticatedActor,
  presentation,
  source,
})

await execution.catalog(input)
await execution.create(input)
await execution.invoke(input)
await execution.views.page(input)
```

The names are provisional. This object is not another application `World` or
client model. It is a trusted-process execution capability hidden beneath the
SDK and RPC adapters. Binding fixes World, actor, presenter/evidence, and source
context once; operation inputs cannot substitute them. Every protected call
still evaluates current Authority and current state—binding is not an allow
cache.

An even narrower implementation may construct separate read, mutation,
Authority, View, and governance capabilities and compose them into this private
host facade. The public Core contract should expose the smallest stable service
the two adapters genuinely share, not every internal context service used to
build it.

Current implementation-style code has to assemble that service itself:

```ts
import {
  BonfireError,
  evaluateGate,
  getPathOrUid,
  invokeYi,
  resolveKind,
  type Kind,
  type Runtime,
} from '@bonfire/core'
import { readRuntimeProjectedYiCreation } from '@bonfire/core/composition'
import { readRuntimeDeclaredViewPage } from '@bonfire/core/runtime'
```

The desired implementation dependency is closer to:

```ts
import type { WorldProductExecution } from '@bonfire/core/product'

function localWorldTransport(
  execution: WorldProductExecution,
): WorldOperationTransport {
  return {
    catalog: (input) => execution.catalog(input),
    createInstalled: (input) => execution.create(input),
    invokeInstalled: (input) => execution.invoke(input),
    // transport projection only
  }
}
```

This is not merely fewer imports. Exact selection, Authority, Creation,
visibility, projection, and failure semantics become impossible for local and
connected adapters to implement differently unless they bypass the canonical
service.

### Core needs roles, not a second exposure ladder

SDK's product -> advanced -> substrate ladder describes increasing participant
power. Core needs a host dependency map instead. A candidate convention is:

| Core role | Contract | Allowed consumers |
| --- | --- | --- |
| portable kernel | Small cross-owner identities, brands, and immutable value contracts; no Runtime or Node imports | SDK portable runtime, compiler, tools |
| owner contract API | Owner codecs, declarations, result types, and pure derivations; the owner noun always has this meaning | SDK authoring/runtime, adapters, tools |
| product execution | Canonical transport-neutral installed-World operations over narrow bound access | SDK local/testing adapter, Server RPC adapter |
| Runtime | Default host execution root and lifecycle; Node-capable by declaration | Server, in-process host, controlled testing |
| composition | Service/representation constructors and external host wiring | Runtime and infrastructure integrations |
| adapter SPI | Exact type-first port for one representation responsibility | The corresponding adapter only |
| operations | Explicit privileged administrative workflow | Operator/host tooling |
| testing | Fixtures and behavior probes | Tests only |

Not every bounded context needs every public role. Symmetry is not a reason to
publish an API. If no external adapter or compiler needs a Kinds service, the
service can remain internal even though Kinds has portable contracts.

This convention gives owner-named paths one predictable floor: contracts,
codecs, and pure derivations. Runtime-bound commands must use a path or facade
whose name communicates host execution. `computation/internal` and
`streams/internal` should not be permanent published categories: an API cannot
be both a supported package export and internal. A genuinely required trusted
host surface should receive an honest role name and explicit stability;
otherwise it remains package-private.

### What should the Core root mean?

There are three credible choices:

| Choice | Advantages | Costs |
| --- | --- | --- |
| Node host aggregate | Preserves one convenient Server import and admits that Core is a host package | SDK/Std must ban the root; portable types still need another home; the default import remains a dumping ground |
| Small portable kernel | Gives the default path one environment-safe meaning; shared brands and fundamental value contracts remain easy to name | Requires moving `createRuntime` and many conveniences; needs a hard allowlist to prevent regrowth |
| No general runtime root | Every dependency is role-explicit and accidental reach is minimized | More import paths, weaker discovery, larger direct-cut churn, and pressure to create local convenience barrels |

The provisional preference is a small portable kernel root plus explicit host
paths. `createRuntime`, environment parsing, storage, invocation, issuer
administration, recovery pumps, and composition do not belong in that root.
The exact portable allowlist still needs a symbol-by-symbol downstream audit;
“widely used” is insufficient because wide use may only prove existing
coupling.

A host aggregate may still exist at `@bonfire/core/runtime`. Its breadth is not
itself a defect if its audience, Node requirement, lifecycle, and Authority are
truthful. The mistake is letting that same aggregate serve as the portable
contract pantry for SDK and Std.

### Core should be capability-shaped internally too

OCap elegance at the SDK cannot rest on ambient or oversized implementation
authority below it. Core APIs used across package boundaries should follow the
same discipline:

- constructors receive exact ports or narrow services rather than a raw
  `Runtime` when they need only one responsibility;
- a bound execution object fixes actor, World, exact install/binding, presented
  evidence, and operation family where practical;
- no caller-supplied field can replace a bound target or actor;
- services do not expose their storage, broader Runtime, credential, or
  internal graph/query frame;
- narrowing returns a capability with no path back to the broader one;
- current Authority and liveness are re-evaluated at the operation frontier;
  and
- portable contracts and inert values never become executable merely because
  they were imported from Core.

`Runtime` itself can remain a broad host ownership root. The discipline applies
when code passes part of its power to SDK, Std, adapters, handlers, or plugins.
For example, a standard process Handler needing manifestation should receive a
manifestation capability or Handler context, not the entire Runtime plus a
system caller token.

### Candidate public-Core laws

Before the SDK implementation plan, the Core direction should be able to
satisfy these laws:

1. One Core-owned product execution service implements catalog, exact binding,
   create, verify, invoke, Creation projection, Activation, transfer, Authority,
   and declared View semantics used by both local and connected adapters.
2. Server RPC and SDK local transport adapt context and bytes only; they do not
   own competing semantic implementations.
3. The Core root has one audience and one environment. Under the provisional
   choice it is portable, has no static Node built-in edge, and excludes Runtime
   construction and host operations.
4. An owner-named public path has one defined role. A path cannot quietly mix
   portable contracts, ambient invocation frames, administrative commands, and
   composition roots.
5. SDK participant/browser paths never import Core Runtime, composition,
   operations, `internal`, or Node-dependent owner aggregates.
6. SDK authoring depends only on portable declarations, schema/compiler
   contracts, and lowering; installing or importing a definition grants no
   Runtime capability.
7. Pure Std definitions and recipes have no direct Core dependency. They use
   the SDK authoring contract like third-party Kits.
8. Server is allowed to depend broadly on Runtime and composition, but each
   adapter imports only its exact SPI and portable owner contracts.
9. Published `internal` subpaths are removed or renamed to an honest supported
   host role; package-private internals stay unexported.
10. Type-only edges stay type-only in emitted JavaScript and declaration reach
    cannot pull host-only types into portable consumer builds.
11. Public-surface snapshots are supplemented with environment, allowed-owner,
    source-reach, native ESM import, and representative bundle budgets for every
    entrypoint.
12. Core root never re-exports a symbol solely because Server, SDK, or Std finds
    the shorter import convenient.

### How each downstream developer should navigate Core

- An application or Kit author does not navigate Core; they use SDK or SDK
  authoring.
- An SDK maintainer starts from the portable product contract and canonical
  product execution interface, then projects it into handles. They do not
  assemble Authority, Creation, or View semantics from root helpers.
- A Runtime host starts from `core/runtime`, adding `composition` only for
  custom wiring and `operations/*` only for explicit administration.
- A storage or representation implementer imports one `adapter-spi/*` plus the
  exact portable contracts named by that SPI.
- A browser renderer uses `core/browser` only when the SDK has not already
  projected the needed values.
- A Core contributor uses internal owner modules inside Core under the
  structure map; those paths do not become package exports for convenience.

This keeps Core expert-facing without making it mysterious. Its README should
lead with these jobs and their permitted paths, not a flat inventory of Yi,
Runtime, messages, storage, and helpers.

### Open Core decisions

- What exact symbols form the portable root allowlist, and would an explicit
  `model` or `contracts` path be clearer than a meaningful root?
- Should the shared product operation contract live in Core or in a separate
  tiny protocol package? A separate package is justified only if wire release,
  environment, or ownership really differs.
- How broad should the canonical bound World execution service be? One facade
  aids parity; smaller composed capabilities aid least authority and testing.
- Which current owner APIs can become contract-only without inventing dozens
  of `/contracts` and `/service` paths?
- Which current SDK `runtime-product` and Server World helpers are truly shared
  semantics, and which are legitimate local/RPC adapter policy?
- Can host functions stop accepting all of `Runtime` where an existing
  context-owned service or port is sufficient?
- Which current public `internal` consumers need a supported host API, and
  which should move behind composition or Handler contexts?
- Do we keep one Core package with enforced dependency islands, or do protocol,
  host, or adapter release/deployment boundaries justify a later package split?

Core should be resolved before freezing the SDK plan. Otherwise the plan may
polish handles and imports around an implementation seam that still forces
semantic duplication, environment leakage, and broad downstream authority.

## Transcripts we must optimize

Every candidate should be written and compared as a complete executable
transcript, including cleanup and realistic error handling:

1. connect, open an existing product, read, and act without source;
2. use a typed Kit, create an object, act, read, and pass it to a function;
3. author and install a small portable Kit;
4. grant an exact operation over one target and over a changing graph scope;
5. pass an Authority-bearing item in-process, delegate it remotely, and
   transfer the durable item;
6. give a minimally attenuated capability to an autonomous agent;
7. query a View and deliberately choose projections, inert refs, or returned
   capabilities;
8. handle denial, disappearance, revocation, expiry, budget exhaustion,
   ambiguity, and stale exact bindings;
9. run the same product code through `@bonfire/sdk/testing` and a connected
   World;
10. read immutable Creation and bounded creator lineage without confusing it
    with principal ancestry, current Kind membership, or Authority;
11. inspect the exact View lowering, delivery eligibility, and Authority
    explanation only when needed;
12. drive the same World catalog/create/verify/invoke/View operation through a
    local adapter and Server RPC while proving both invoke one Core semantic
    execution service; and
13. compose a custom Runtime representation from one exact adapter SPI without
    importing the Core root or unrelated context services.

For each transcript, record:

- lines and tokens of application code;
- Bonfire-specific nouns and verbs introduced;
- explicit selectors and repeated identifiers;
- network round trips;
- authority conveyed to every callee;
- exactness and lifecycle boundaries;
- what TypeScript catches;
- what runtime validation catches;
- what a reader is likely to misunderstand.

## Investigation backlog

These are research questions, not ordered implementation tasks.

- Audit all current public SDK exports and their use in non-test consumers.
- Classify every Core root export by actual SDK, Std, Server, adapter, tool, and
  browser consumer; distinguish genuine portable kernel contracts from
  convenience-barrel debt.
- Diff SDK `runtime-product.ts` against Server `methods/world/catalog.ts` and
  extract the exact shared semantic operation set, leaving authentication,
  framing, rate limiting, cancellation, and serialization in their adapters.
- Prototype a transport-neutral, access-bound Core World product execution
  service and test whether it can replace both semantic implementations without
  becoming another application object model.
- Define and mechanically enforce Core entrypoint role, environment, allowed
  consumer, source-reach, and Node-built-in budgets in addition to symbol
  snapshots.
- Audit every published Core `internal` subpath and every function accepting a
  full `Runtime`; identify the narrow supported host capability each real
  external consumer needs.
- Reduce representative examples to semantic transcripts and identify repeated
  ceremony that can be inferred safely.
- Trace the exact current forms of Authority-bearing items through Custody,
  facets, certificate evaluation, and invocation presentation.
- Model an in-process capability handle that cannot expose or recombine its
  broader World transport/evidence.
- Model the remote sturdy-reference encoding using the existing certificate
  and presenter/subject machinery.
- Test capability revocation and current-standing changes after a handle has
  been passed.
- Validate the accepted capability-opening and inert-result defaults across
  create, get, View, Action, discovery, and remote acceptance transcripts.
- Compare `birth`, `facets`, and authored-name-first manifestation inputs while
  proving that no public shape can supply immutable Creation creator/origin.
- Prototype View tie/root binding and async iteration strictly over the current
  exact materialized/live handles, including restart, cancellation, cursor,
  generation, and read-stamp behavior.
- Inventory action/framework/facet name collisions across real Kinds.
- Compare direct actions plus `$` with `.actions`, callable action objects, and
  other collision-free projections.
- Measure catalog/binding/verification round trips for typed and source-free
  paths.
- Audit schema, Handler, gate, family, export-policy, and address repetition in
  authored Kinds.
- Evaluate how the grammar maps to a second language SDK; avoid elegance that
  depends entirely on TypeScript Proxy behavior.
- Define product-level error recovery scenarios and safe opacity boundaries.
- Verify that each convenience has one exact explanation and advanced escape
  path without a daily `.raw` peer.

## Decision ledger

The ledger distinguishes settled intent from provisional designs.

### Recorded intent

- SDK elegance is a dedicated design concern, broader than the existing
  one-model convergence work.
- Object capabilities are an important direction and must be explored as a
  semantic Authority model, not only fluent syntax.
- Core's public dependency and semantic-execution seams are part of SDK
  elegance. They must be resolved before the downstream API plan is frozen.
- We will explore the improvement space before writing an implementation plan.
- This document is the living record for that exploration.

### Constraints carried forward

- Exact installations and binding revisions do not float silently.
- Actor, subject, presenter, target, and evidence do not collapse.
- Current Authority is re-evaluated; cached allows are not permissions.
- Definitions stay pure and substrate power stays explicit.
- Passing an inert reference never silently passes executable Authority.
- Custody transfer and capability passing are distinct operations even when an
  item participates in Authority.

### Implemented baseline constraints — 2026-09-02

- Plans 51 and 52 are implementation-complete and release-certified in the
  direct baseline. There is no V2 API, compatibility path, dual write,
  dual-materialization interval, or migration surface to preserve.
- Every Yi birth atomically writes one root and one immutable Kinds-owned
  Creation record. Public create inputs carry no complete origin or creator.
- Stable Yi UID denotation is separate from mutable principal profile,
  principal liveness, and principal-parent state. `YiRef` and `PrincipalRef`
  remain disjoint inert references.
- Authored/bound/born-as Kind evidence, the Kind dependency graph, and a Yi's
  effective Kind membership are separate facts. A semantic projected graph is
  a bounded read capability, not another membership or state owner.
- Creation lineage and principal ancestry use one private traversal kernel
  through sealed exact and visibility-projected construction. No generic graph
  constructor/session is public.
- Views compile one strict declaration to one logical operator DAG. Live reads
  execute inside one private `QueryReadFrame`; it is neither serializable nor
  a cached permission or resumable query session.
- Live Views may traverse the admitted projected lenses. Traversal makes a
  declaration ineligible for durable generation at authoring, decode/install,
  and generation-build boundaries.
- Durable non-graph Views publish through prepare -> build -> activate, keeping
  the prior ready selection current under `serve-last-complete` until fenced
  activation.
- Lifecycle unification is limited to exact operation/protocol patterns and
  Occasion commit mechanics. Creation, principal state, Activation, Custody,
  Containment, Relations, and View generations keep separate owner laws and
  state machines.

### Accepted design decisions — 2026-09-01

- `Snapshot<K>` keeps `snapshot.state` as the one canonical authored-state
  representation. Named facets and `$` remain siblings; flattened duplicate
  aliases are not added.
- Every executable verified `Yi<K>` is a target- and exact-interface-bound
  in-process object capability. `YiRef<K>` is inert designation, `kind.get(ref)`
  opens a capability under a World access, and `kind.ref(uid)` does not.
- Views and ordinary Actions return declared data or inert typed references by
  default. Creation is an explicit capability factory. Any other executable
  capability result requires a declared and evaluator-proven Authority
  derivation; capability-producing Views are deferred until they have a
  dedicated budget/replay/revocation law.
- Every remote capability token is audience-bound to its exact World and
  Authority/protocol root. The secure default is also presenter-bound.
  Bearer-within-audience is restricted, explicit, short-lived, narrowly scoped,
  budgeted, non-delegating, and membrane-constrained.
- Dynamic `world.open(...)` uses honest method-based runtime selection as its
  portable floor. Local or generated Kits use direct typed properties through
  `world.use(Kit)`. Both paths converge on the same bound Kind and Yi runtime
  objects; Proxy behavior is not constitutional.
- Authoring removes mechanically derivable repetition, permits omissions only
  when they close Authority/portability/resource behavior, uses pure versioned
  recipes for reviewed complete policy bundles, and keeps consequential
  lifecycle, economic, Authority, portability, migration, and external-effect
  choices explicit.

### Provisional candidates

- Direct authored actions on Yi with a reserved `$` framework surface.
- An authored-name-first manifestation shape, or an explicit `facets` group,
  that never exposes immutable Creation origin/creator and keeps state,
  context-owned initial facts, and Activation bindings semantically distinct.
- Tie/root-bound View result objects and bounded async iteration layered over
  the exact existing materialized/live handles without erasing their delivery
  posture.
- Grouped daily authoring roots and a measured root-export budget.
- The exact delegate/export/accept spelling and token representation that
  realizes the accepted remote binding laws.
- A small portable Core root, with Runtime construction and host operations on
  explicit host paths, subject to a symbol-by-symbol consumer audit.
- One Core-owned, access-bound World product execution service used by SDK
  local/testing and Server RPC adapters.
- A public Core role map in which owner-named paths mean portable owner
  contracts/pure derivations, while Runtime, composition, adapter SPI,
  operations, and testing have explicit dependency roles.

### Rejected or not yet justified

- Treating possession of a UID as Authority.
- Serializing a raw connection credential as a remote capability.
- Assuming a durable item changed Custody because an SDK handle was passed.
- Making methods disappear and reappear as current Authority changes.
- Hiding ambiguous installation selection behind an ambient “latest”.
- Adding another App/client/product object model beside World, Kit, Kind, and
  Yi.
- Adding a generic `IdentityRef`, `Entity`, `Graph`, public graph session,
  resumable `QueryReadFrame`, or universal lifecycle service/interface.
- Treating projected graph reach or historical Creation provenance as current
  Authority.
- Accepting caller-authored Yi creator/origin or conflating initial facet facts
  with immutable Creation.
- Materializing a traversal-bearing View or adding a hidden graph-backed
  generation path within the current baseline.
- Treating Core's strong internal structure map or public symbol snapshots as
  sufficient proof that the external entrypoint topology is sound.
- Keeping separate SDK-local and Server-connected implementations of exact
  World product semantics and relying only on parity tests to prevent drift.
- Using the Core root as an unrestricted type pantry or publishing an
  `internal` path as a routine supported integration surface.
- Producing an implementation plan before the capability, authoring, dynamic
  discovery, read-result, failure, and Core execution-boundary questions are
  resolved.

## Next exploration checkpoint

Before planning, we should have at least:

- a defensible answer to every remaining open OCap mechanics question above;
- side-by-side current and candidate versions of the complete transcript set;
- a public-export and authoring-ceremony audit;
- a Core export-role audit and one canonical local/connected World product
  execution prototype;
- transcript and evaluator probes validating the accepted data/reference/
  capability result rule;
- a remote capability encoding grounded in the existing Authority contracts
  and the accepted audience/presenter defaults;
- measured round-trip and bundle/API costs;
- explicit decisions recorded in this ledger, including discarded alternatives
  and why they were rejected.
