# SDK structural direction — one World-facing language, explicit semantic graphs

> **Status:** conceptual north star built on the certified protocol-162 / Plan
> 49 baseline and revised after auditing the current SDK, Authority, package
> and Kind dependency machinery, lifecycle gaps, Cordis's core lifecycle, and
> an independent second-pass review of the ideal public SDK surface.
> This is deliberately not an implementation plan. Target-language examples
> are sketches; exact spelling is provisional until the public grammar is
> ratified.

## Executive direction

Bonfire should present one product language from definition through execution:

```text
Bonfire connection
└── World Yi
    ├── implicit primary DefinitionNamespace
    ├── exact PackageInstalls and Kind binding environments
    ├── generated typed product surfaces
    ├── World-scoped Authority and control plane
    └── ordinary Yi interpreted in that World

Kit source
├── Kinds
│   ├── authored state
│   ├── named facets
│   ├── actions
│   ├── optional activation behaviors and requirements
│   └── governed transitions
├── Views
└── exports and portable implementation artifacts
```

Concepts learned during definition should retain their names during creation,
reading, invocation, querying, testing, explanation, and evolution. The World,
typed client, raw Yi handle, product namespaces, facets, presets, and substrate
APIs must stop behaving like competing application models.

The important correction to the earlier direction is:

> **One product language does not mean one generic graph.**

Definition dependencies, install locks, semantic relationships, activation
requirements, activation ownership, and Authority delegation have different
meanings and lifecycle owners. Elegance comes from naming and composing them
consistently, not flattening them into `capability`, `parent`, or `dependsOn`.

This is not a Core rewrite. Preserve the compiler and contexts as the single
semantic authority, preserve Occasion as the durable commit spine, preserve
exact package and Kind locks, and preserve the modern Authority certificate
engine. The SDK-facing hierarchy may be substantially reshaped, and a real
Activation model is still missing beneath it.

## Current truth

The codebase is not back at zero, and Plan 49 was not wasted. Important parts
of the destination already exist:

- facets are real, typed, exact authoring contracts;
- Views, typed Relations, Streams, Signals, and generated Kit namespaces are
  materially present;
- Kind-family identity, revision closure, binding revisions, rollout, and
  exact dependency slots are deep and rigorous;
- package installation has exact pins, provenance, uninstall protection,
  stale-plan checks, and cycle rejection;
- manifestation plans and Occasion now form the certified atomic and recovery
  baseline;
- package installation activates exact Handler and workflow artifacts, and
  connected acceptance runs through the public remote SDK;
- the modern issued Authority certificate already represents subject,
  presenter, parent chain, structured coverage, validity, revocation epoch,
  attenuation, transfer policy, caveats, and consistency evidence;
- agents already have no privileged class or ambient Authority by design.

What is not finished or converged:

- World, `defineBonfireApp`, typed clients, broad clients, product facades, and
  raw handles remain overlapping object models;
- local and connected World bootstrapping do not yet agree on one canonical
  World composition;
- current `World.kind()` is async and deploys immediately, so it cannot be the
  pure definition language;
- `world.app` names a namespace boundary as though it were an application;
- `Capability` is overloaded across facets, permission evidence, held Yi,
  protocol discovery, and service injection;
- typed generation exists but does not yet become the ordinary World surface;
- current `YiHandle.as(kind)` adds typed methods locally without verifying the
  installed binding, so its target meaning is `unsafeAssume`, not `expect`;
- a general Yi-to-Yi activation requirement and reconciliation lifecycle does
  not exist;
- some context lifecycle declarations are not yet closed by execution;
- two Authority certificate/product lanes remain visible;
- delegated invocation does not yet preserve the full actor/subject/evidence
  envelope through every nested call;
- the certified Plan 49 substrate has not yet been projected into one coherent
  World-facing SDK.

In particular, current context behavior is not one universal dependency law:

| Current relationship | Current lifecycle truth |
| --- | --- |
| Identity parent to child | Strong, transactional subtree lifecycle and governance ancestry. |
| Custody holder to holding | Holder-loss policy exists; transfer does not imply child transfer. |
| Containment parent to placement | `reject`, `detach`, and `cascade` are declared, but parent-extinction execution is not fully composed. |
| Relation occurrence to endpoints | Endpoint liveness affects reads; no complete endpoint-loss transition law exists. |
| Kind to dependent Kind | Exact revision closure and rollout are strong. |
| Package to dependency | Exact install pins and uninstall blockers are strong. |
| Workflow to target/operation | Exact installed artifacts and references execute through the package lifecycle; a general provider-degraded lifecycle is still absent. |
| Yi to executable provider Yi | No general durable activation requirement/reconciler exists. |

The direction must build on this certified substrate rather than reopening it,
and must not claim instance Activation is solved by package activation, facets,
or Views.

### Audited anchors

The current-state claims above are grounded in the present
[facet authoring surface](../../packages/sdk/src/authoring/facets.ts),
[typed-client generator](../../packages/sdk/src/client/typed-client.ts), and
[World façade](../../packages/sdk/src/world/world.ts). Exact package lifecycle
is represented by the
[package install contracts](../../packages/core/src/packages/contracts/manifest.ts).

The Authority direction builds on the modern
[issued certificate](../../packages/core/src/authority/contracts/certificate-issued.ts),
[delegation algebra](../../packages/core/src/authority/service/certificates/issued-certificate.ts),
and
[parent-chain evaluation](../../packages/core/src/authority/service/decisions/authority-role-evaluation.ts),
including the existing
[no-ambient-authority agent seal](../../packages/core/src/authority/service/principals/tests-agent-no-ambient-authority.test.ts).
The lifecycle gaps are visible in Containment's
[declared parent-loss contract](../../packages/core/src/containment/contracts/placeable.ts),
the Relations
[occurrence lifecycle](../../packages/core/src/relations/service/lifecycle.ts),
and the certified
[Plan 49 handoff](../yi/49-structural-arc/HANDOFF.md).

## The Bonfire-native root

A canonical World root is a real Yi bearing `core:world`, with a stable UID and
an exact root address. It may bear additional Kinds under the same composition
laws as other Yi.

A Bonfire connection is the transport and authenticated-actor root for
reaching several Worlds; it is not another product ontology:

```ts
const bonfire = await connect({ endpoint, auth })

const hearth = await bonfire.world('@hearth')
const forest = await bonfire.world('@forest')
```

`hearth` and `forest` are distinct World Yi handles, installations, namespace
sets, governance scopes, and Authority scopes. The connection may reuse
transport and identity credentials, but it does not merge their graphs or
invent one global App above them.

World is nevertheless not a ninth kernel noun or a universal storage
container:

- **World** is the product, governance, naming, installation, portability, and
  exit scope.
- **Domain** is the atomic commit and total-order boundary.
- **Shard** is physical placement.
- **Containment** is an authored relationship with its own lifecycle laws.
- **RuntimeContext** is an ephemeral host activation environment, not a Yi and
  not a namespace.

Consequently, one World may use many Domains, World-wide operations are not
automatically atomic, and World participation is never inferred from arbitrary
Containment or Relation ancestry.

An Occasion has one semantic Domain and one ordered head. Runtime
`participantDomainIds` may predeclare coordination/fencing needed by a
ceremony, but they do not merge Domain heads or create portable cross-Domain
atomicity. Cross-Domain product change remains an explicit promise, workflow,
or settlement with visible completion law.

### The constitutional bootstrap exception

The World is a Yi, but installing Kinds is already World-scoped. Therefore a
small constitutional ceremony must create the `core:world` root and its
primary DefinitionNamespace before ordinary installation can occur. This is a
real bootstrap boundary and should be named, tested, and kept small.

After bootstrap, product behavior on the World should come from normal Kind
composition. Community governance may be composed onto the World; it must not
replace World identity. Local, test, and connected modes must verify the same
canonical `core:world` root instead of relying on different first-binding
conventions.

### Three meanings of “a World has a Kind”

The SDK must keep these statements distinct:

| Statement | Exact meaning |
| --- | --- |
| The World **bears** a Kind | The World Yi itself carries that binding and gains its state/facets. |
| The World **governs** a Kind | A PackageInstall has established exact binding revisions in a World-scoped `KindBindingEnvironment`. |
| A Yi **bears the governed Kind** | An instance selected that installed binding and materialized its representation. |

Installing Key does not make the World root a Key. A Key participating in the
World need not be contained by the World root. This distinction must survive
the SDK, typed snapshots, explanation, and migration tooling.

## The namespace boundary, without “App”

The separate namespace Yi is an excellent boundary. Its name should describe
what it owns.

Call the architectural concept a **DefinitionNamespace**. The public advanced
API may simply say `Namespace` because its location under an explicit
`advanced(world).namespaces` surface supplies the qualifier:

- it durably owns world-authored address names and namespace Authority;
- it records namespace controller and provenance;
- it provides a stable address boundary for locally defined Kinds, Relations,
  projections, and other address-bearing declarations;
- it is created by the World bootstrap or an explicit advanced ceremony.

It is not:

- an App or second application root;
- a Kit definition;
- a package installation or install receipt;
- a binding environment;
- a runtime dependency container;
- a Group, community, or subworld;
- the catalog of everything usable in the World;
- a Kit's pure export aliases, a package publisher namespace, or the aliases
  sealed into a Kind interface revision.

The primary namespace should be implicit in ordinary product code. Pure source
does not call a connected World:

```ts
const Key = defineKind(families.key, { /* ... */ })
const Locksmith = defineKit('locksmith', { kinds: { keys: Key } })
```

Publication or installation qualifies those local names in the selected
World namespace.

Advanced code may address it honestly and plurally:

```ts
import { advanced } from '@bonfire/sdk/advanced'

const namespaces = advanced(hearth).namespaces

namespaces.main
await namespaces.create('economy', { /* governance */ })
```

`main` is a reasonable neutral primary alias, but exact address punctuation
must be ratified against canonical address rules rather than guessed in this
document. Illustratively, the conceptual structure is:

```text
@hearth                     World Yi
@hearth.<main>              primary DefinitionNamespace Yi
@hearth.<main>:key          world-authored Kind
@hearth.<channels>          package-created definition namespace, if declared
@hearth+<channels-install>  durable install/provenance record
@hearth/groups/raiders      Group Yi
```

The current concepts should separate accordingly:

| Current name | Direction |
| --- | --- |
| `WorldApp` / `world.app` | `DefinitionNamespaceRef` / explicit advanced namespace access. |
| `defineBonfireApp` | Removed from the product model. Explicit Kit records supply public aliases; transport schemas are generated internally, not authored as another root. |
| `createTypedClient` | Generator machinery behind a World-bound Kit surface. |
| `communities.deployApp` | A high-level World publish/install ceremony plus an exact advanced namespace deployment operation. |
| logical `appId` | A deployment/source identity, not namespace identity. |

## Minimal, non-overloaded vocabulary

The daily model should center on existing concepts and introduce new nouns only
where the semantic gap is real.

### World

The distinguished Yi and product/governance scope in which installations are
bound and operations are interpreted. `World` always means the real durable
World Yi as reached through one authenticated actor-bound connection. There is
no pure `WorldDefinition`; reproducible bootstrap may use an advanced
deployment plan, but that plan is never accepted where a runtime World is
expected. Actor binding belongs to the access handle/invocation, not to durable
state on the World Yi.

### DefinitionNamespace

The advanced durable owner of declaration names. It is normally implicit.

### Kit

A pure local composition of Kinds, View exports, actions/Handlers, workflows,
transitions, migrations, and product aliases. Publication turns it into a
Package release; Packages owns release dependencies, requested consent,
resolution locks, provenance, and installation lifecycle. A Kit is not an
installation or running container.

### Kind

The stable public identity and vocabulary of a class of Yi. `KindFamilyId` is
the rename-stable identity. A pure descriptor, portable revision, interface
revision, installed binding revision, and World-bound access are distinct
artifacts, but they preserve one public Kind identity and vocabulary instead
of becoming unrelated wrapper models.

Raw family genesis coordinates are an exact/advanced concern. Ordinary
authoring uses a generated, committed registry. An explicit tooling ceremony
such as `bonfire family add key` writes the token once:

```ts
const Key = defineKind(families.key, {
  // ...
})
```

`families.key` carries the stable declaration identity needed by
`defineKind`; authors do not repeat the local name and raw genesis coordinates
inside every definition. Tooling preserves it across variable, file, Kit
alias, and namespace-address renames. It never derives family identity from a
mutable address or generates a nonce at module evaluation time.
`defineKindFamily({ lineageId, nonce })` remains advanced migration/testing
machinery, not ordinary product authoring.

### Facet

A named semantic contribution owned by one Bonfire context. A facet contributes
that context's canonical contracts and exact interaction points; the Kind and
compiler compose the complete birth, state, action, event, and interface
surface. Product recipes may make common facets concise without inventing a
parallel `Capability` ontology.

### Action

A humane verb with typed input, authorization, execution identity, and
effects. Invocation lowers to the constitutional port/Handler protocol. Only
durable mutations commit through Occasion; reads, Signals, and external effects
retain their own completion laws.

### View

An explicitly declared, authorized, rebuildable read model or access path.
Today its portable semantic identity is hosted by an explicit Kind-family
facet contribution; Package/World installation binds and catalogs it, while a
Kit supplies its product alias. A future standalone Kit-owned View would need
its own portable revision and migration law rather than an SDK-only shortcut.

### ActivationRequirement

A named condition that one activation behavior needs from an exact provider
endpoint while it is active. It is usually authored with `requires(...)`.
Requirement controls readiness; it does not imply
ownership, containment, transfer, or Authority.

### Activation

One executable behavior contributed to a Yi. Its durable `ActivationSlot`
records desire and exact bindings; each ephemeral `ActivationGeneration` is a
leased live realization. A Yi may have zero, one, or several slots. Yi
identity, slot, and generation are different lifetimes.

### Certificate

`grant` and `delegate` are operations. A certificate is the exact durable
result/evidence and parent-chain coordinate. There is no second durable Grant
noun unless a future ceremony genuinely governs several certificates as one
artifact. A certificate is not a facet, service, held object, or server
feature.

`Gate`, `Domain`, `Occasion`, `Handler`, revision, certificate, and exact
binding identity remain visible when their decisions matter. Repository,
registry, route, shard, and raw protocol vocabulary remain advanced.

## One language, several explicitly owned graphs

This graph map is the conceptual center of the direction.

| Graph | Question it answers | Semantic owner | Change/loss law | Cycles | Grants Authority? |
| --- | --- | --- | --- | --- | --- |
| Kind/revision dependency | Which definitions and interface revisions give this Kind meaning? | Kinds/compiler | Exact closure, cohorts, rollout, migration. | Only by explicit compiler cohort law. | No. |
| Package/install dependency | Which exact releases and artifacts must be installed together? | Packages | Exact lock update, uninstall protection, replacement provenance. | Hard cycles reject unless the package model explicitly supports a closed cohort. | No. |
| Identity ancestry | Where is this Yi structurally rooted and governed? | Identity | Reparent/extinction laws and subtree locking. | Reject. | No implicit operation right. |
| Custody/Containment/Relation | Who holds it, where is it placed, or how is it related? | Owning context | Context-specific transfer, move, endpoint, and extinction policies. | Context-specific. | Only through explicit Authority bindings. |
| Activation requirement | What exact provider endpoint must be available for this behavior to run? | New Activation bounded context | Wait, stop, restart, or explicit rebind against an exact endpoint. | Required graph rejects cycles against one serialized graph revision. | No. |
| Activation generation ownership | Which live effects and child generations are cleaned up together? | Computation `RuntimeScope`, fenced by an Activation generation | Reverse dependency-order teardown inside one live scope; crash recovery is idempotent/best-effort. | Forest/acyclic ownership. | No. |
| Authority standing/certificate | Which actor may exercise which operation for which subject over which resources? | Authority | Closed intrinsic standing or issued certificate; attenuation, expiry, epoch/revocation, consistency, and parent-chain evaluation. | Certificate derivation rejects cycles. | Yes. |

No row in this table may be inferred from another merely because the same two
Yi appear in both:

```text
A contains B        ≠ A owns B
A created B         ≠ B may use A's grants
A depends on T      ≠ A may invoke T
A may invoke T      ≠ T is available
A owns generation B ≠ extinguishing A extinguishes Yi B
```

The SDK should share names, types, explanations, and transitions across these
graphs while keeping their evaluators distinct.

## The ideal public SDK shape

The daily surface has one object model:

| Shape | Role | What it is not |
| --- | --- | --- |
| Bonfire connection | Transport and authenticated actor root for reaching Worlds. | An App or global semantic container. |
| `World` | The real World Yi plus its actor-bound product/control surface. | A pure definition or deployment blueprint. |
| `Kit` | Pure composition whose record keys define the product namespace. | A client, install receipt, or running container. |
| `Kind` | Stable pure declaration identity and vocabulary. | A World-specific registration token. |
| World-bound Kit/Kind access | Exact installed access, such as `locksmith.keys`. | A new Feature ontology. |
| `Yi<K>` | One verified handle carrying the named faces of `K`. | A parallel model beside a raw Yi object. |
| `Snapshot<K>` | One immutable typed observation using the same state/facet names. | A bag of `data`, `dimensions`, and context DTOs. |
| `YiRef<K>` | A locator plus expected stable Kind identity. | Proof that the target exists or is visible now. |
| `Certificate` | Exact Authority evidence returned by grant/delegate verbs. | A generic Capability object. |

`Facet`, `Action`, and `View` are declaration vocabulary. Activation and
ActivationRequirement appear only for Kinds that declare live behavior.
Ordinary code should not learn App, TypedClient, WorldKindRef, TypedKind,
Feature, durable Grant, semantic Preset, or raw Port as peer product nouns.
Presets remain ordinary functions that return declaration fragments; Ports and
Handlers remain visible only when exact execution detail matters.

The default import should contain the entire daily language:

```ts
import {
  action,
  connect,
  defineKind,
  defineKit,
  facet,
  t,
  view,
} from '@bonfire/sdk'

import { families } from './bonfire.families.js'
```

Separate package paths control operational weight, not meaning. Testing uses
the same World/Kit/Kind/Yi types; advanced and substrate imports expose exact
mechanisms without adding `.raw` peers to daily objects.

The unavoidable runtime phases preserve one identity rather than inventing
unrelated wrappers:

```text
Key (pure Kind) ───────────── stable Kind identity ───────────────┐
        │                                                         │
Locksmith.kinds.keys ── publish/install ──> locksmith.keys        │
                                             exact bound access   │
                                                      │           │
world.yi(uid).expect(locksmith.keys) ─────────────> Yi<Key> ─> Snapshot<Key>
```

The public identity laws are:

```ts
locksmith.keys.kind === Key
key.kind === Key
key.ref.kind === Key
```

`BoundKit<K>` and `BoundKind<K>` may exist as TypeScript phase types, but
developers interact with “the Locksmith Kit in Hearth” and “the Key Kind in
that installation,” not a second client ontology.

## One end-to-end product model

### Pure definition with named facets

```ts
const ownership = facet.custody.asset({
  quantity: 'unit',
  transfer: 'whole',
  holderLoss: 'detach',
})

const placement = facet.containment.placeable({
  slots: ['keyring'],
  parentLoss: 'detach',
})

const access = facet.authority.role({
  subject: ownership.holder,
  activeWhen: placement.in('keyring'),
  ownerTransfer: 'reissue',
  extinguish: 'revoke',
})

const Key = defineKind(families.key, {
  state: {
    label: t.string(),
  },

  facets: {
    ownership,
    placement,
    access,
  },

  actions: {
    unlock: action({
      input: { door: t.ref(Door) },
      allowed: ownership.holder,
      run: handlers.unlock,
    }),
  },
})
```

The facet recipes above are pure, deterministic constructors over existing
context contracts. They do not create another representation or evaluator.
Common `facet.*` recipes belong on the daily surface; exact contribution and
`bindFacet.*` mechanics remain advanced.

Named facet values are typed references. `access` refers to the exact ownership
and placement contributions that give it meaning. Several facets may coexist;
interaction exists only through an exact reference or aggregate law.
The `facets` record key is the one public name reused in birth input, snapshot,
runtime face, events, bindings, and explanation; a recipe should not require a
second duplicate name. Multiple contributions from one context are legal only
when that context declares their composition law. Ambiguous operations,
duplicate semantic names, and surface collisions reject at compilation—never
last-write-wins.

### Kit definition and explicit View ownership

```ts
const KeysByHolder = view({
  from: Key,
  by: {
    holder: ownership.holder,
  },
  item: Key.ref,
  order: ['createdAt', 'uid'],
  access: ownership.holder,
})

const Locksmith = defineKit('locksmith', {
  kinds: {
    keys: Key,
    doors: Door,
    keyrings: Keyring,
  },

  views: {
    keysByHolder: KeysByHolder,
  },
})
```

Aliases are explicit. They never come from transitive dependency names or
ambient package state.

In the current semantic model, `view(...)` must lower to an explicit View
declaration contribution on its designated Kind family; the Kit key only
exports that portable identity. It must not become an SDK-only Kit query with
no revision or migration owner.

The Kit's record keys are its product namespace and survive unchanged through
generated types, installation, creation, Views, tests, and explanations.
Reserved framework keys should be few and fixed—for example `installation`,
`views`, `streams`, `signals`, `workflows`, `activations`, and `explain`—and
compilation rejects collisions instead of silently renaming user exports.

### Publication, installation, and binding

```ts
const bonfire = await connect({ endpoint, auth })
const hearth = await bonfire.world('@hearth')

const locksmith = await hearth.install(Locksmith)
```

`install()` is the one durable product ceremony and returns the World-bound Kit
directly. It never returns a receipt that requires an immediate second
`use(...)` call:

```text
Kit source
→ Package release
→ Resolution lock
→ PackageInstall
→ KindBindingEnvironment and exact binding revisions
→ BoundKit<typeof Locksmith>
```

Distributed software installs a verified Package release and exact resolution
lock. A local source Kit may be accepted only when `install()` creates an
immutable private release and a real PackageInstall through the same chain.
If a development path skips that law, it must be honestly named `deploy()` and
remain advanced. There is no ambient `latest`.

`locksmith` is the Locksmith Kit bound immutably to one World and exact
installation. Its `BoundKit<typeof Locksmith>` type retains the
PackageInstall, resolution lock, namespace, binding environment, and exact
binding revisions for explanation and advanced control. It is not another
World, App, Yi, Authority scope, or client engine.

`use()` is the read-only reconnect path:

```ts
const locksmith = await hearth.use(Locksmith)
```

It succeeds only when exactly one active compatible installation exists. A
missing installation fails as missing; ambiguity fails with the candidate
installation IDs. Exact selection repeats the Kit for its static contract and
adds only the durable selector:

```ts
const locksmith = await hearth.use(Locksmith, {
  installation: installId,
})
```

Package replacement or rollout may yield a new bound value; an existing value
never silently changes binding underneath its handles.

### Creation, reading, acting, and querying

```ts
const key = await locksmith.keys.create({
  state: { label: 'Front door' },

  birth: {
    ownership: { holder: alice },
    placement: { parent: keyring, slot: 'keyring' },
  },
})

const snapshot = await key.read()

snapshot.state.label
snapshot.ownership.holder
snapshot.placement.parent
snapshot.meta.observation

await key.ownership.transferTo(bob)
await key.placement.moveTo(backpack, { slot: 'keys' })
await key.actions.unlock({ door })

const page = await locksmith.views
  .keysByHolder({ holder: alice })
  .page({ limit: 50 })
```

Birth input and handle faces are derived from the same named facets. Creation
returns a verified typed handle. Views use the same contribution references.
Context operations stay beside the context-owned facet instead of reappearing
as unrelated top-level client namespaces.

`Action` is the sole daily verb abstraction. Compilation lowers it to one
exact Port declaration, Handler/Computation artifact, interface revision, and
bound invocation. `key.actions.unlock` invokes it;
`locksmith.keys.actions.unlock` is the same bound descriptor when Authority or
explanation needs an exact selector. Raw Port dispatch is substrate-only.
An inline JavaScript body is never advertised as portable unless the selected
Package tier, release artifact, and execution trust policy can actually carry
it; otherwise `run` names a sealed Handler/Computation artifact.

The snapshot is immutable and repeats the definition's names. Authored state,
context-owned facts, and observation/binding evidence have one obvious place;
the product surface does not expose competing `WorldRow`, `data`,
`dataByKind`, `authoredState`, and `contexts` shapes. Exact substrate material
is grouped under one reserved metadata face or available from the substrate
import.

Each View declares one output shape. Reference output is the default;
hydration, projection fields, or aggregates belong in the declaration and
therefore change the generated output type. Runtime flags such as
`itemShape: 'ref' | 'structured'` must not turn one View into several APIs.

### Reference and verification

```ts
const ref = locksmith.keys.ref(uid)
const key = await locksmith.keys.get(uid)
const maybeKey = await locksmith.keys.find(uid)
const key = await hearth.yi(uid).expect(locksmith.keys)
```

`hearth.yi(uid)` means “interpret this Yi in this World.”
`expect(locksmith.keys)` verifies the exact installed binding selected by the
bound Kit. `expect(Key)` may exist only when it is clearly documented as
family/interface compatibility rather than exact binding verification. Neither
asserts ownership or structural containment.

The unverified value is `Yi<unknown>` with only stable UID denotation and
verification operations. It is not a raw protocol client wearing a shorter
name; dynamic dispatch and substrate row access require the substrate import.

Compatibility is better given a different verb:

```ts
const compatible = await hearth.yi(uid).expectFamily(Key)
```

`get()` and `read()` throw the same opaque not-found result for an absent or
invisible Yi; `find()` returns `null`. This prevents visibility probing while
keeping optional lookup explicit. Substrate reads may retain raw nullable
behavior.

Unchecked assertions must identify themselves:

```ts
const key = hearth.yi(uid).unsafeAssume(locksmith.keys)
```

### Testing

```ts
const test = await testWorld({
  root: '@hearth-test',
  install: [Locksmith],
})

const alice = await test.actor('alice')
const hearth = test.as(alice)
const locksmith = await hearth.use(Locksmith)
const key = await locksmith.keys.create({
  state: { label: 'Front door' },
  birth: { ownership: { holder: alice } },
})

await key.ownership.transferTo(await test.actor('bob'))
```

Tests use the same World, Kit, Kind, facet names, requirement slots,
certificate operations, Views, and Actions. Only facilities and controlled
actor binding differ.
Authority belongs to an authenticated actor-bound World/invocation, not to a
durable Yi handle, so production code has no `key.as(...)` impersonation
escape. `test.as(alice)` is a test-controller ceremony and returns the exact
production `World` type; actor switching is not a method on that World.

## Activation: the missing Yi dependency lifecycle

Cordis is a useful reference for a small process-local activation law:

- a behavior waits until required providers are present;
- provider loss deactivates dependents;
- restoration permits reactivation;
- every listener, timer, registration, resource, and child activation belongs
  to one effect owner;
- partial setup failure disposes what was already acquired;
- definition and mounted instance are different things.

Bonfire should adopt those invariants, not Cordis's ontology. Cordis is trusted,
in-process, transient, dynamically resolved, and not a permission or durable
event system. A Cordis fiber is not a Yi; a Cordis service namespace is not a
DefinitionNamespace; isolation is not security; a disposer cannot compensate
for committed Occasion history.

Activation needs an explicit semantic owner. A new **Activation bounded
context** owns durable slots, requirement edges, graph revisions, desired
state, observed phase, generation claims, leases, and reconciliation
decisions. Computation owns the process-local `RuntimeScope` and the effects
acquired by one generation. Packages still activate installed code artifacts;
that is not the same lifecycle as activating behavior on an individual Yi.

### Activation belongs to executable behavior, not to every Yi

A Yi is durable identity. An Activation is one reversible live behavior
contributed to it: an agent loop, scheduler, subscription, adapter, or active
workflow realization.

- data-only facets normally create no Activation;
- one Yi may have several independent Activations;
- failure of one behavior does not make the entire Yi nonexistent;
- Yi extinction terminally retires its Activations, but stopping an Activation
  never extinguishes the Yi;
- a requirement should attach to the smallest affected behavior, not globally
  disable a multi-facet Yi without reason.

### Minimal authored shape

The common case can remain small:

```ts
const research = activation({
  requires: {
    search: requires(SearchTool.actions.search, {
      availability: SearchTool.activation.active,
      onUnavailable: 'wait',
    }),
    metrics: optional(Metrics.actions.record),
  },

  start: handlers.startResearch,
})

const ResearchAgent = defineKind(families.researchAgent, {
  activations: {
    research,
  },
})
```

Creation binds exact provider Yi:

```ts
const agent = await workshop.researchAgents.create({
  birth: {
    research: {
      search: searchTool,
      metrics,
    },
  },
})
```

The portable declaration names the required endpoint contract. Birth binds
that slot to one exact provider Yi, installed interface revision, and endpoint;
the binding is durable rather than rediscovered by type or string at runtime.

The Handler receives typed providers and a generation-fenced effect scope:

```ts
const startResearch = handler(async (ctx) => {
  await ctx.scope.acquire('task-subscription', () =>
    subscribeToTasks(ctx.self),
  )

  await ctx.use.search({ query: '...' })
})
```

`acquire` claims generation ownership before setup begins and does not let the
resource escape until cleanup is registered; setup failure drains anything
already registered. A bare `effect(await subscribe())` cannot provide that
partial-setup guarantee.

The exact syntax may be simplified, but the same slot name—`search`—must be
used during definition, binding, execution, status, explanation, and rebinding.
Runtime control stays under the authored behavior name:

```ts
await agent.activations.research.read()
await agent.activations.research.stop()
await agent.activations.research.start()
```

Kinds without authored live behavior expose no Activation surface.

### Durable desired state and observed phase

Do not persist one misleading global Yi lifecycle. Each Activation records:

```ts
type DesiredActivation = 'running' | 'stopped' | 'retired'

type ActivationPhase =
  | 'stopped'
  | 'waiting'
  | 'starting'
  | 'active'
  | 'stopping'
  | 'failed'
  | 'retired'
```

Desired and observed state must remain separate. Restoring a provider must not
restart behavior its owner intentionally stopped.

`waiting` is reversible and carries a structured cause such as missing
provider, inactive provider, incompatible interface, unavailable Authority,
or unavailable owner lease. `failed` is reserved for invalid configuration
(including a rejected cycle) or behavior/setup failure.

### State laws

1. An Activation publishes `active` only after setup and every resource
   acquisition is owned by its generation scope.
2. Before teardown, it unpublishes availability and fences its generation.
3. Dependents stop before providers; providers start before dependents.
4. Every start gets a new generation, a fenced owner claim, and a host lease.
5. Late work from an old generation cannot commit.
6. Each live scope attempts each registered disposer at most once, in reverse
   dependency order; one cleanup failure does not skip later cleanup.
7. Setup registers effect ownership before resources escape, enabling rollback
   of partial setup.
8. Cleanup releases process-local effects only. Durable mutation, migration,
   compensation, and history remain explicit Occasion/workflow operations.
9. Missing required providers produce `waiting`, not semantic Yi extinction.
10. Optional requirements never determine activation readiness.
11. Crash recovery guarantees generation fencing and idempotent takeover, not
    exactly-once external cleanup. External resources require idempotent leases
    or cleanup plus orphan diagnostics.
12. Slot, requirement, and binding changes use compare-and-swap against one
    serialized Activation graph revision; takeover cannot race an older owner.

### What happens when provider B changes?

“B changed” must be decomposed into exact semantic events:

| Change to B | Effect on dependent Activation A |
| --- | --- |
| Ordinary authored/display state changed | No lifecycle change unless a named availability predicate depends on it. Observe the Occasion normally. |
| A declared availability predicate became false | Fence and stop A, then enter `waiting` under the declared loss policy. |
| B became unavailable but remains the same exact provider | Stop A; restoration may start a fresh generation. |
| B's compatible implementation revision is governed through rollout | Preflight, fence, and restart only under the exact rollout/compatibility law. |
| B loses the required interface or moves to an incompatible revision | Stop A and remain `waiting: interface-incompatible`. |
| Authority to invoke B is revoked | Invocation fails immediately; reconciliation moves A to `waiting: authority-unavailable` if Authority is a declared readiness condition. |
| B is extinguished | The fixed binding remains visibly broken. A does not silently choose a new Yi. |
| A different compatible B appears | Nothing happens until an authorized, Occasion-committed rebind selects it. |
| B's holder, parent, placement, or relation changes | Only the owning Custody, Identity, Containment, Relation, or explicit Authority binding law decides the consequence. |

Provider replacement is never ambient discovery of “latest.” A rebind validates
the exact target/interface, updates the durable edge, fences the old
generation, stops, recomputes readiness, and starts if admitted.

### Observed requirements and generation ownership

An observed requirement means A uses B but does not own it. Stopping A has no
effect on B, and many consumers may share B.

Generation ownership means one `RuntimeScope` owns a child generation and its
process-local effects. Disposing the owner includes the child generation in
teardown. It still does not extinguish the child's Yi or grant Authority.

Requirement edges determine start/stop order. Runtime ownership determines
which live units belong to one cleanup closure. Keep the required dependency
graph acyclic and the generation-ownership graph a forest.

### Durable and distributed law

Cordis cleanup assumes one process. Bonfire needs durable coordination:

- persist each `ActivationSlot`, desired state, exact endpoint bindings,
  serialized graph revision, generation claims, leases, and meaningful
  lifecycle Occasions;
- derive observed phase from current generation/lease and history rather than
  trusting stale process memory;
- allow only one host to own a generation;
- reject stale-generation commits even if a zombie process continues;
- rebuild process-local effects after crash from durable declarations and
  checkpoints;
- store long-running agent state through Occasion, Streams, or explicit
  checkpoints, not in fiber memory;
- use strong same-Domain epoch checks where available;
- for cross-Domain providers, declare consistency/freshness and treat expired
  dependency evidence as unavailable;
- bound fan-out, retries, backoff, and reconciliation work when one provider
  has many dependents.

Hard runtime requirement cycles should reject against one graph revision at
planning or binding time. Optional edges may break a cycle. A future atomic
activation cohort must be an explicit construct, not a set of consumers
silently waiting forever.

## Authority and autonomous agents

The permission graph should be a productized convergence of the modern issued
Authority certificate system, not a new generic graph engine.

The existing engine already has the right semantic core:

- distinct issuer, authority root, subject, and presenter;
- exact action/port and resource coverage;
- validity windows and issuer revocation epochs;
- parent certificate chains with cycle/depth safety;
- narrowing-only attenuation and transfer policy;
- audience, expiry, use-budget, result-redaction, and event caveats;
- same-Domain and freshness/consistency evidence;
- current parent-chain evaluation and decision evidence.

It still needs one important coverage correction: a list of resource selectors
currently behaves disjunctively. The target model needs a **conjunctive target
descriptor** so “this Tool Yi through this exact installed interface revision”
cannot accidentally mean “this Yi or anything with this revision.”

The SDK should retire or lower the older certificate/capability lane into this
one model. `client.capabilities` should not remain the permission noun while
facets and protocol features also use “capability.” Product code should use
`authority`, grant/delegate verbs, and `certificates`.

### Non-inheritance laws

These laws are absolute:

1. Identity ancestry conveys structural lifecycle/governance, never ambient
   permission to invoke arbitrary operations.
2. Containment conveys placement, never permission by itself.
3. Custody and Relations provide Authority standing only through an explicit
   Authority facet binding.
4. Agent creation and creator/child relationships convey no grants.
5. The only transitive edge for **issued** Authority is
   `certificate.parent`. Closed intrinsic self, root, or Custody standing starts
   at its context-owned evaluator; it neither inherits nor fabricates a parent
   certificate.
6. Every invocation re-evaluates current evidence; a cached `allow` is never
   Authority.

The ideal Gate API must split `identityAncestor`, `containmentAncestor`, and
exact standing predicates. It must not expose an ambiguous generic
`ancestor()` that merges structural and spatial parentage.

### If A grants Alice the right to use Tool T

- The grant covers exact World, Tool resource/interface revision, ports or
  actions, subject/presenter, validity, and caveats.
- Alice's children receive nothing automatically.
- Alice may derive a certificate for child C only when attenuation, transfer,
  recipient, depth, and budget laws all permit it.
- C's effective Authority is the intersection of its complete current parent
  chain, never a copy of Alice's ambient identity.
- Parent expiry, revocation, or invalidation denies descendants at the
  certificate's declared consistency level.
- Tool availability remains a separate Activation requirement.

### Two distinct delegation ceremonies

Authority operations are rooted in the authenticated actor-bound World, not
hung off the target Yi or a freely chosen identity object. `hearth.authority`
below is a request/control face; it is not state stored on the World Yi. The
product surface must distinguish:

```ts
await hearth.authority.grantTo(agent, {
  // subject = agent; presenter = agent
  allow: {
    action: workshop.searchTools.actions.search,
    target: {
      yi: searchTool,
      interface: workshop.searchTools.interfaces.tool,
    },
  },
  /* bounds */
})

await hearth.authority.actFor(agent, {
  // subject = alice; presenter = agent
  allow: {
    action: workshop.searchTools.actions.search,
    target: {
      yi: searchTool,
      interface: workshop.searchTools.interfaces.tool,
    },
  },
  /* bounds */
})
```

`grantTo` lets the agent act for itself. `actFor` lets the agent present a
bounded right on Alice's behalf. Changing presenter and changing beneficiary
are not the same transfer. In tests, `test.as(alice)` creates this actor-bound
World under an explicit test-only ceremony; an arbitrary `alice.authority` or
`key.as(alice)` API would make impersonation look like object navigation.

Certificate presentation derives a new immutable actor-bound World access:

```ts
const delegatedHearth = await hearth.with({
  present: [certificate],
})
```

The authenticated actor remains unchanged; only the presented certificate
evidence and resulting subject envelope differ. Bound Kits and Yi handles
derived from `delegatedHearth` inherit that exact envelope. Presentation does
not live on an individual handle, and no operation mutates the Authority
context of an existing World/Kit/Yi value.

### Safe autonomous-agent defaults

An autonomous child agent should start with:

- no inherited grants;
- no onward delegation (`remainingDepth: 0`);
- exact World, Tool revision/interface, operations, and resources;
- short expiry and a bounded use budget;
- recipient/presenter bound to that agent;
- explicit result-redaction and event allow-list membranes;
- current Authority checks for irreversible, economic, or administrative work;
- human approval continuations where policy requires them;
- a complete audit and explanation path.

If an agent may create subagents, opt in with a positive delegation depth,
strict descendant/named-recipient bounds, and narrower grants. A mechanical
chain safety ceiling is not a product delegation policy.

Use budgets must be conserved across siblings by partition/escrow: deriving a
child reserves part of the parent's remaining pool, each protected operation
commits consumption idempotently, and expiry/revocation can release unused
reservation under explicit law. Issuing many children each with the parent's
maximum is not attenuation. Monetary or computational cost limits should not
enter the certificate grammar until one context owns metering, reservation,
settlement, and dispute semantics.

An Activation that runs autonomously stores an exact execution Authority
envelope on its durable slot: actor/subject, the admitted intrinsic-standing
mode or certificate references, consistency requirements, and permitted
service role if any. Starting a new generation re-evaluates that envelope. A
host process contributes no ambient Authority merely because it holds the
lease.

### Preserve the invocation Authority envelope

Do not collapse a delegated call into one `effectiveCaller`. The full envelope
must survive Handler entry, nested invocation, Occasion attribution, and
explanation:

```ts
interface InvocationAuthority {
  actor: PrincipalRef       // authenticated presenter
  subject: PrincipalRef     // beneficiary
  certificates: CertificateRef[]
  decision: AuthorityDecisionEvidence
}
```

Handlers receive `ctx.actor`, `ctx.subject`, and `ctx.authority`. Nested
`ctx.invoke` preserves or narrows the inbound envelope; it can never upgrade
the beneficiary into an ambient caller. Exercising a Kit/service's own
Authority requires a separate, scoped, audited ceremony. Service Authority is
not unioned with inbound Authority and is never tried as an implicit fallback.
This is the primary confused-deputy correctness boundary for autonomous
agents.

### Remaining Authority laws to settle

- Add first-class delegation depth and recipient/subject/presenter bounds.
- Make resource, action, caveat, and transfer narrowing available on the
  product surface, not only in exact Core contracts.
- Replace disjunctive resource selection with conjunctive target matching for
  exact Yi, Kind/interface revision, Domain, and any scoped relation facts.
- Define whether reparenting changes live authority-root validity. Either root
  ancestry is immutable provenance or reparenting advances a topology/issuer
  epoch; it cannot remain ambiguous.
- Complete containment-scope and relation-scope materialization only through
  explicit Authority facet bindings.
- Bind certificates to Tool interface/revision meaning so an upgrade cannot broaden
  an old grant silently.
- Persist the exact execution Authority envelope for autonomous Activation
  slots and define the audited service-Authority ceremony.
- Keep human approval as a real Gate/continuation protocol, not a decorative
  caveat.
- Treat execution isolation separately: a certificate constrains Bonfire
  operations, not arbitrary JavaScript, CPU, memory, filesystem, or network
  access.

## Context lifecycle and transfer remain context-owned

Activation does not replace existing semantic lifecycles.

- Identity decides subtree reparenting and extinction.
- Custody decides holding transfer and holder-loss behavior.
- Containment decides movement and placement-edge loss.
- Relations decide occurrence activation and endpoint loss.
- Kinds decide revision rollout and representation migration.
- Packages decide installation, replacement, and uninstall.
- Authority decides grant derivation and invalidation.

The direction must close declared-but-unexecuted laws before presenting them as
SDK promises. In particular, Containment parent-extinction and Relation
endpoint-loss need complete executable semantics, and package/namespace/World
extinction must be composed with install retirement.

### Parent transfer and children

Transferring a container does not silently transfer children. Custody and
Containment remain independent unless an explicit aggregate law connects them.

Closed laws may include:

```ts
contents.independent()
contents.requireEmpty()
contents.bundle()
contents.cascade({ depth, thirdParty: 'reject' })
```

`bundle` means effective ownership derives from the aggregate and should avoid
duplicating child holdings. `cascade` means independently held descendants are
transferred through a bounded, authorized plan.

Complex transfer must be previewable:

```ts
const plan = await chest.ownership.previewTransferTo(bob)

plan.affectedChildren
plan.blockers
plan.domains
plan.execution

await plan.commit()
```

The explanation states whether execution is same-Domain atomic or a real
cross-Domain workflow/settlement. It must account for concurrent moves,
non-transferable children, third-party holdings, partial failure, and topology
fencing.

### Governed evolution, not a generic Kind-attach verb

Do not collapse semantically different changes:

| Operation | Meaning |
| --- | --- |
| `attach` | Add representation-free vocabulary/behavior when target admission permits it. |
| `materialize` | Add missing context-owned representation to the same Yi through a full birth ceremony. |
| `wrap` | Create a new Yi representing a bounded right or claim over the original. |
| `convert` | Migrate/supersede semantic identity under a declared transition. |

These remain advanced target concepts until each has an owner, admission law,
rollback/settlement class, Occasion shape, and removal law. The SDK must not
fake materialization by calling an internal Kind-membership path.

Adding a Tool Kind or compatible interface may make an existing fixed provider
eligible to satisfy a waiting ActivationRequirement after a governed
representation transition. It never grants Authority, silently rebinds
consumers, or makes the Yi exchangeable without Custody materialization.

## Progressive disclosure without a model cliff

The intended public ladder is conceptual, not a commitment to exact package
paths:

```text
@bonfire/sdk
  connection, World, pure Kind/Kit/Action/View authoring, schemas,
  common facet recipes, world-bound Kits, typed Yi, Certificates, errors

@bonfire/sdk/testing
  The same World/Kit/Kind model in a controlled runtime

@bonfire/sdk/advanced
  exact facets/bindings, namespace management, package/binding/revision and
  certificate control, compilation and deployment tools

@bonfire/sdk/substrate
  raw protocol, dynamic dispatch, DTOs, RPC and infrastructure operations

@bonfire/sdk/agents/*
  optional external runtime adapters, not a second Bonfire object model
```

The generated typed-client machinery should project onto
`world.install(Kit)` and `world.use(Kit)`. `defineBonfireApp`,
`createTypedClient`, `TypedBonfireClient`, `WorldKindRef`, `WorldRow`, and the
broad product client become compatibility/internal machinery, not peer public
models.

Daily World and Kit values expose no `.raw` peer. Opening substrate power is an
explicit import and therefore a visible review boundary:

```ts
import { openSubstrate } from '@bonfire/sdk/substrate'

const substrate = openSubstrate(hearth)
```

A World-bound Kit exposes explicit aliases, not Feature objects:

```text
locksmith.keys
locksmith.doors
locksmith.views
locksmith.transitions
```

A typed Yi exposes only verified faces:

```text
key.read()
key.ownership
key.placement
key.actions
key.activations
```

## Explainability is part of minimalism

A small surface must expose its exact lowering and decision evidence:

```ts
explain(Key)
explain(Locksmith)
await agent.activations.research.explain()
await hearth.authority.explain(certificate)
await chest.ownership.previewTransferTo(bob)
```

For an invocation, one explanation should preserve the graph boundaries:

```text
Why is this action available?
├── World and exact Kit installation
├── installed Kind/action binding
├── activation requirement
│   ├── exact provider Yi and interface revision
│   └── current phase, generation, lease, and consistency
├── authenticated actor and beneficiary subject
├── effective certificate parent chain
│   ├── operation/resource intersection
│   ├── validity, budget, depth, recipient, and membranes
│   └── revocation/consistency evidence
├── current Gate and context facts
└── Domain/Occasion or workflow/settlement execution class
```

Explanation is not another evaluator. It is structured evidence emitted by
the same compiler, context, Activation, Authority, and execution decisions.

## Conceptual movements and why

This is an order of architectural understanding, not a task breakdown.

### 1. Ratify vocabulary and graph ownership

Move from overloaded App/Capability/parent/dependency language to World,
DefinitionNamespace, Kit, Kind, Facet, Action, View, ActivationRequirement,
Activation, and Certificate.

**Why:** lifecycle and permission cannot be safe or intuitive while the same
word means composition, availability, possession, and authorization.

### 2. Converge on one World-facing product surface

Keep the connection as the transport root for several Worlds and make each
World the real actor-bound Yi root—never a pure definition. Start pure
authoring at Kind/Action/View/Kit; project existing generated types onto
`install()`/`use()`, exact Kit aliases, verified Yi, and immutable snapshots.
Make `install()` return the bound Kit and reserve `use()` for read-only
reconnection.

**Why:** this removes App, TypedClient, WorldKindRef, WorldRow, and unchecked
handle translation without discarding the typed-client and View machinery that
already works.

### 3. Finish existing semantic lifecycle promises

Hold the certified Plan 49 Occasion/manifestation/recovery spine fixed, then
close the context-owned loss laws still only declared or partial for
Containment, Relations, packages, and World/namespace retirement.

**Why:** a new Activation coordinator cannot safely orchestrate lifecycle laws
that are only comments or partial projections.

### 4. Introduce Activation as the one new lifecycle concept

Add per-behavior exact requirements, durable desired state, observed phase,
generations, leases, effect ownership, reconciliation, cycle/fan-out policy,
and explicit rebinding.

**Why:** this is the unresolved gap between durable Yi semantics and live
agents/tools/workflows. Cordis supplies the minimal local law; Occasion,
revisions, Domain, and leases make it Bonfire-correct.

### 5. Converge and productize Authority

Make the modern certificate chain the sole semantic permission model; preserve
the invocation envelope; split `grantTo` from `actFor`; add delegation depth,
recipient bounds, conserved budgets, complete narrowing, and Tool revision
stability.

**Why:** autonomous agents require explicit, attenuated, current Authority—not
ancestry inheritance or an ambient effective caller.

### 6. Admit governed evolution only after owners are complete

Expose attach/materialize/wrap/convert only as distinct, context-owned
transitions with complete admission, representation, Authority, rollback, and
history laws.

**Why:** dynamic Kind membership must not become a shortcut around Custody,
Containment, Authority, or revision invariants.

### 7. Demote substrate mechanics and enforce the public ladder

Keep the whole daily language on `@bonfire/sdk`, move exact namespace/package/
binding/certificate mechanics to `advanced`, and require an explicit substrate
import for raw protocol access. Project current broad clients behind World and
bound Kit values, maintain one executable quickstart, and type-check public
examples.

**Why:** minimalism is durable only when documentation, generated types, and
runtime behavior cannot drift apart.

## Assumptions corrected by this direction

| Assumption | Correct direction |
| --- | --- |
| App is the runtime root | World is the product/governance root; a bound Kit is a typed projection. |
| `world.app` is another product root | It is a durable DefinitionNamespace boundary and should be named/hidden accordingly. |
| Pure authoring should start from `WorldDefinition` or `world.kind()` | World always means the real connected Yi; pure authoring starts with Kind, Action, View, and Kit. |
| A separate TypedClient is the normal generated surface | Generated types project directly onto `world.install/use(Kit)`, bound Kit aliases, and verified Yi. |
| `YiHandle.as(kind)` verifies Kind membership | Verification is async `expect(boundKind)`; unchecked narrowing is visibly `unsafeAssume`. |
| Install returns a receipt that must be bound again | `install()` returns the exact World-bound Kit; `use()` only reconnects to existing installation state. |
| One model means one graph | One language coordinates several explicitly owned graphs. |
| `Capability` can name every useful contribution | Facet, Action, ActivationRequirement, Certificate, held Yi, protocol support, and process-local provider remain distinct. |
| A Kind is literally one artifact at every phase | It has one stable public identity/vocabulary across distinct definition, revision, binding, and bound-access artifacts. |
| A World needs no special bootstrap | `core:world` and the primary namespace require a small constitutional creation ceremony. |
| A View is just a Kit/World-owned query helper | Today a View's portable semantics are an explicit Kind-family facet contribution; Kit aliases it and Package/World installation binds and catalogs it. |
| A Yi dependency is a Kind dependency | Definition closure and instance Activation requirements are separate. |
| Provider state change always restarts consumers | Only declared availability/interface/epoch inputs affect Activation. |
| Compatible replacement may be selected automatically | Exact provider rebind or rollout is governed and explicit. |
| Fiber disposal equals Yi extinction | Activation teardown releases live effects; contexts own durable Yi lifecycle. |
| Parent/creator implies permission inheritance | Only an explicit certificate-parent edge derives Authority. |
| Authority to invoke implies availability | Certificate evaluation and ActivationRequirement readiness are independent checks. |
| Service isolation is a security boundary | Runtime provider selection and execution sandboxing are distinct from Authority. |
| Parent transfer implies child transfer | Custody and Containment are independent unless an aggregate law connects them. |
| Adding a Kind makes an object transferable | Context-bearing representation requires governed materialization/conversion. |
| Handler cleanup can undo durable work | Disposers release local effects; durable compensation uses Occasion/workflow law. |

## Structural laws for the target

1. **World is the product root and always a real Yi.** Host, connection,
   World, Domain, namespace, deployment plan, and install remain distinct
   roots/coordinates; there is no pure WorldDefinition.
2. **The namespace boundary is real and accurately named.** Ordinary code uses
   it implicitly; advanced code can govern it explicitly.
3. **One concept keeps one name.** Definition, birth, read, Action, View,
   ActivationRequirement, certificate selection, test, and explanation reuse
   the same authored names.
4. **One stable Kind identity crosses explicit phases.** Pure definition,
   portable revision, installed binding, and bound access never become
   competing public ontologies.
5. **Definitions are pure.** Declaration never installs, connects, or mutates
   a World.
6. **Core remains the semantic authority.** Product recipes lower exactly to
   existing compiler/context contracts.
7. **Facts have one owner.** Authored state never duplicates normalized
   context facts.
8. **Graphs do not infer one another.** Dependency, ownership, containment,
   and Authority require exact edges.
9. **Yi identity and Activation are distinct.** Stopping behavior never
   extinguishes durable identity.
10. **Every live effect has one activation-generation owner.** Live disposal
    attempts are bounded and once-only; crash recovery fences stale work and
    uses idempotent external cleanup rather than promising the impossible.
11. **Provider selection is exact.** Replacement requires governed rollout or
    rebind; there is no ambient latest.
12. **Authority is explicit and current.** Agent creation, ancestry, and
    containment grant nothing; certificate derivation is the only transitive
    path for issued Authority, alongside closed intrinsic standing.
13. **Actor and subject never collapse.** The complete Authority envelope
    survives nested execution and audit.
14. **Consequential policy is explicit.** Loss, transfer, delegation,
    budgets, consistency, Domain, and settlement are never guessed.
15. **Every public promise executes.** A declarative option affects enforced
    behavior or compilation rejects it.
16. **Advanced is accessible but not ambient.** Exact mechanisms remain
    available without defining daily product work.
17. **Convenience is explainable.** Generated semantics and every decision can
   be inspected through evidence from the actual evaluator.
18. **Binding and Authority context are immutable.** `install()` returns one
    exact bound Kit, `use()` reads existing state, and presenting a certificate
    derives a new actor-bound World rather than mutating existing handles.
19. **Snapshots repeat authored names.** State, named facet facts, and one
    reserved evidence face replace competing row/DTO shapes.

## Acceptance scenarios for the direction

These are architectural tests, not merely documentation questions.

### Surface and World

- One canonical connected quickstart uses World, Kit, Kind, typed creation,
  View, Action, and certificate issuance without a raw/substrate escape.
- The same definitions and names run locally, in tests, and through public
  transport.
- `install(Kit)` returns the bound Kit directly; `use(Kit)` is read-only and
  rejects missing or ambiguous installation selection.
- Multiple installations require exact selection and produce distinct typed
  projections without creating extra roots.
- No public App, TypedClient, Feature, WorldKindRef, or WorldRow model remains;
  namespace and substrate access require explicit advanced imports.
- A pure Kind keeps the same identity through bound access, verified Yi,
  reference, snapshot, Authority selector, test, and explanation.
- `expect(boundKind)` verifies exact installation membership,
  `expectFamily(Kind)` checks compatibility, and `unsafeAssume` is the only
  unchecked narrowing.
- Snapshot state and facet facts reuse authored names, while `get/read` versus
  `find` have one consistent absence law.
- `test.as(actor)` returns the production World type; production values expose
  no impersonation method.

### Activation

- A dependent created before its provider is `waiting`, not failed or
  extinguished.
- Provider arrival admits at most one live generation for the affected
  behavior under the current graph revision.
- Provider loss fences and stops only affected behaviors; unrelated facets and
  Activations remain available.
- Every registered local effect is disposed at most once by its live scope;
  crash recovery fences stale generations and diagnoses orphans.
- Restoration starts a fresh generation idempotently.
- Ordinary provider data changes do not restart dependents.
- An incompatible upgrade or different provider never silently rebinds.
- A hard requirement cycle rejects with its path.
- Stale generations cannot commit after stop/replacement.
- Same-Domain and cross-Domain dependency freshness follow their declared
  consistency laws.
- One provider loss with many dependents remains within fan-out/retry budgets.

### Authority and agents

- A child or autonomous agent receives no creator-held grant automatically.
- `grantTo` and `actFor` produce observably different subject/presenter
  evidence.
- An explicitly attenuated agent invokes only the selected Tool operation and
  resources.
- Nested calls cannot escape the presented certificate envelope.
- Widening, unauthorized recipient changes, and excess delegation depth reject.
- Parent revocation/expiry denies every descendant at the declared freshness
  level.
- Sibling derivations cannot multiply a conserved use/cost budget.
- Result redaction and event allow-lists hold over remote transport.
- Tool upgrade cannot broaden the meaning of an existing grant.
- `explain()` shows the actor, subject, parent chain, effective intersection,
  current evidence, and exact denial cause.

### Semantic lifecycle and evolution

- Containment parent-extinction policy executes exactly as declared.
- Relation endpoint loss has an explicit state transition and no hidden
  multiplicity leak.
- Package/namespace/World retirement cannot leave live-looking unusable
  installations without an explicit state.
- Parent transfer behavior is explicit, previewable, and Domain-aware.
- Representation-bearing evolution cannot occur through raw Kind attachment.
- Activation loss never bypasses the owning context's durable lifecycle law.

## What this direction is not

It does not pursue:

- a generic property bag or active-record object model;
- one universal parent, dependency, capability, or lifecycle graph;
- a second App ontology layered over World;
- a Cordis fiber as durable Yi identity;
- string service lookup, proxy injection, or invisible provider substitution;
- permission inheritance from Identity, Containment, creation, or ownership;
- service/provider isolation presented as security sandboxing;
- automatic parent/child ownership coupling;
- arbitrary dynamic transformation of any Yi into any other representation;
- a second compiler, Gate evaluator, lifecycle truth, or permission engine;
- an elegant declaration that the runtime cannot execute and explain.

## Final test

The direction is coherent when a developer can answer, without changing
mental models:

- Which World and exact installation am I using?
- Which DefinitionNamespace owns this declaration, when I need to know?
- What is this Kind, and which named facets give it meaning?
- What must I provide to create it, and what typed handle comes back?
- Which Views and actions are installed?
- Which exact provider does this Activation require, and why is it waiting or
  active?
- What will happen if that provider's data, interface, availability, Authority,
  or identity changes?
- Who is the authenticated actor, who is the beneficiary, and which current
  certificate chain permits this operation?
- Why does a child agent have exactly these grants and no others?
- Which context owns transfer, parent loss, endpoint loss, extinction, or
  representation evolution?
- Which Domain/Occasion or workflow/settlement executes the operation?
- How do I inspect the exact lowering and decision evidence?
- How do I test the same semantics locally and remotely?

The intended result is concise:

> **World is the product root. DefinitionNamespace owns names. Kit is pure
> composition. Kind and named facets preserve the product vocabulary. Exact
> installations bind that vocabulary to a World. Activation controls live
> readiness. Authority certificates control use. Contexts control durable
> lifecycle. Occasion records durable change. None of these silently becomes
> another.**
