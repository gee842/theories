# Evaluation of `the-frame.md` and `the-pivot.md`

> Where this page and source-anchored docs disagree, `llms.txt` and the cited source files win.

Status: independent review artifact. This file does not modify or supersede
`docs/concepts/the-frame.md` or `docs/design/the-pivot.md`.

Inputs:

- Direct reading of `docs/concepts/the-frame.md` and `docs/design/the-pivot.md`.
- Targeted verification against `packages/core`, `packages/server`, `packages/sdk`, `packages/std`, and existing docs.
- Three independent sub-agent passes: conceptual coherence, code claim audit, and engineering risk.

No tests were run. This is a design and source-verification review.

## Short Verdict

The direction is probably right, but the documents are not yet safe as an
implementation plan.

The best kernel is:

> A `Yi` is the one addressable bearer of traits, relations, capabilities,
> state, and behavior. Meaning lives in the `kinds[]` a Yi bears. Agency is a
> trait, not the default condition of every Yi. Ports and gates are the common
> interaction and authority surface. Storage remains free to optimize below the
> conceptual seam.

That is elegant and compatible with the strongest parts of the current code:
`Yi` is already one row shape, traits are already close to composed kinds, and
port dispatch already walks `kinds[]`.

The risky part is that the documents also promote a broader `Tie/Moment/Compiler`
frame. That frame may be useful as rationale, but as written it risks turning
the concept doc into a promise about unbuilt machinery. The final product will
be elegant only if the docs are tightened so that implemented truth, desired
direction, and future compiler work are separated.

## What To Keep

### 1. Meaning In The Open

The strongest claim is that meaning should be in `kinds[]`, not in optional
field presence.

Current code already supports this direction in important places:

- `Yi.kinds` is ordered and additive.
- One row can carry both `core:spirit` and `core:holding`.
- Holding subface routing is already marker-based in the storage path.
- Port dispatch resolves behavior through the row's `kinds[]`.

This is the right conceptual center. If the project keeps only one law from
these documents, keep this one.

### 2. Agency Is A Trait

This is the most important correction to a naive actor model.

Every Yi should be addressable. Not every Yi should be active. Initiating
behavior should require an agent-like trait. Receiving a port, holding a
capability, being contained, being transferable, and being a relation target
should be separate traits or roles.

This gives you the original "item carries an agent and behaves like a spirit"
case without making every inert object a possible actor.

### 3. One Interface, Plural Representation

The core desire is sound: authors should declare intent, not hand-pick
marker-vs-edge-vs-special-table representation.

That does not mean storage becomes generic. It means storage optimizations move
below the seam:

- marker queries use `kinds[]` and the GIN path;
- edge queries use holder/referent indexes;
- streams use the dense `yi_message` path;
- collections can use children plus aggregate-at-read.

The frame is strongest when it says "same meaning, multiple representations,"
not when it pretends all representations are already interchangeable.

### 4. Break Forward, With Atomic Phases

The "no compat layer" instinct fits this project, but it only works if each
phase is atomic across core, server, SDK, docs, tests, examples, and public
surface snapshots.

Breaking forward is not the same as deleting half a bridge and leaving the
other half to guess. Each phase needs one clean world, not old and new names
coexisting.

## What Needs Correction

### 1. `Tie` Is Overloaded As A Taught Primitive

`the-pivot.md` says Tie-duality should be rationale, not the daily taught model.
`the-frame.md` still teaches `Yi + Tie` as the irreducible core and folds
traits, messages, port firings, audit events, and standing relations into the
same word.

That is the main conceptual risk.

The frame should teach:

- `Yi`
- `Trait`
- `Role`
- `Port`
- `Gate`
- `Relation` or `Tie` only for relationships between Yis

The deeper "standing relation and moment are dual" idea can live as an
appendix. It is explanatory, but if it becomes the daily model, it risks
replacing the old zoo with a more abstract one.

### 2. The Compiler Is Treated Like A Conceptual Fact

`the-frame.md` makes the deploy-time relation compiler central to the mental
model, but no such compiler exists yet.

That is fine as a direction, but it should be labeled as planned substrate
work. The current implemented reality is:

- marker queries exist;
- holder/referent edge queries exist;
- message table streams exist;
- no author-facing `membership(...)`, `stream(...)`, or relation compiler exists.

The concept doc should not make an unbuilt compiler part of the basic model
until at least one relation has shipped through it.

### 3. "Every Representation Is Rebuildable" Is Too Absolute

The law is desirable, but the document states it as already true for all
materializations.

Current messages are a special table with a same-transaction event dual-write.
That is good engineering. It is not the same as proving every future marker,
edge, stream, collection, CRDT, or feed representation is a pure rebuildable
function of canonical Yi state.

Safer wording:

> Every representation must either be canonical or have a declared canonical
> source and a tested rebuild path. No performance representation may become the
> only place truth exists.

### 4. Phase 1 Is Not "Pure Deletion"

The pivot calls Phase 1 router-independent subtraction. The sequencing is good.
The "pure deletion" framing is too optimistic.

Examples:

- `DimensionRegistry.contributesToFace` is still live discovery machinery.
- `holdingSubFaceFromKinds` has many non-test call sites across core, server,
  and std.
- `Kind` stored fields are read through accessors and face-specific modules.
- Runtime and SDK public APIs still carry `face`, `classId`, and old namespaces.

This can still be the first phase, but it is migration work with tests, not just
cleanup.

### 5. The `Kind` Shrink Needs An Inventory First

The target `Kind = { id, rowSchema, gates, ports, composes, defaults,
lifecycle, triggers }` is appealing, but the current `Kind` also has live fields
that cannot be deleted by assertion:

- `invariants`
- `evolutionPolicy`
- `transientVia`
- `examples`
- `frozen`
- stored class-spec fields such as `face`, `features`, `policy`, `methods`,
  `hooks`, `partySchema`, `issuer`, `referent`, `mutual`, `transferable`,
  `revocable`, and more.

Before shrinking `Kind`, classify every field as one of:

- canonical field;
- trait data;
- port;
- gate;
- lifecycle or trigger;
- storage/index metadata;
- migration-only;
- deleted legacy.

No field should disappear until this classification exists and has tests.

### 6. The Agency Law Is Slightly Too Strong

`the-frame.md` says only a Yi bearing an agency trait can receive ports,
initiate moments, or hold capabilities.

Initiating moments should require agency. Holding a capability should not.
Receiving ports may require `messageable` or `callable`, but not necessarily
full agency.

Suggested split:

- `addressable`: can be referenced;
- `callable` or `messageable`: can receive ports/touches;
- `agent`: can initiate actions;
- `capability`: can be held and used as authority evidence;
- `container`: can carry child/contained Yis.

This keeps roles orthogonal and avoids smuggling subjecthood back into agency.

### 7. The Docs Mix Current Fact And Destination

Both docs should consistently distinguish:

- **Current fact**: already true in code.
- **Violation**: current code contradicts the frame.
- **Destination**: intended end state.
- **Future mechanism**: compiler/planner/stream generalization not yet built.

Right now several destination claims are phrased as if the code already works
that way.

## Is This The Best Way To Go?

Mostly yes, if tightened.

The current codebase already contains the right spine:

- one `Yi` row;
- additive `kinds[]`;
- kind rows as Yis;
- `rt.yi.*` as the runtime root;
- ports and gates over kind membership;
- storage indexes below the surface.

The documents correctly identify the remaining pain: old faces, field-presence
identity, split membership, split port models, and public concepts that do not
match the substrate's best parts.

But the best path is not "implement the frame as written." The best path is:

1. Do a doc-truth pass.
2. Make the concept doc smaller and more conservative.
3. Inventory `Kind` fields.
4. Remove field-presence identity.
5. Normalize face/register vocabulary.
6. Prove membership through one compiler-style relation.
7. Only later consider streams, collections, CRDTs, or a broader relation
   compiler.

## Recommended Route

### Phase 0: Truth Pass

Do not change runtime behavior yet.

- Mark every major claim in `the-frame.md` and `the-pivot.md` as current fact,
  violation, destination, or future mechanism.
- Fix concrete inaccuracies such as `rt.yi.get` vs the actual `rt.yi.read`.
- Remove or soften "already true" language around the compiler and rebuildable
  projections.
- Move Tie/Moment duality into rationale/appendix unless the founder explicitly
  wants it as the daily model.

### Phase 1: Subtractive, But Tested

- Inventory all `Kind` fields.
- Decide the replacement home for each field.
- Replace field-presence identity with declared markers/traits.
- Rename "face_class" registers to "register" in docs and types only when the
  code follows.
- Keep public surface snapshots and docs in lockstep.

### Phase 2: Membership-Only Compiler Proof

Build exactly one relation compiler PoC: membership.

It must prove identical behavior for:

- `join`
- `leave`
- `isMember`
- `members`
- negative auth cases
- marker-backed hot reads
- edge-backed churny writes
- session membership referent checks
- EXPLAIN-backed PG routes

Do not generalize streams here.

### Phase 3: Streams And Collections

Only after membership works should the project consider:

- stream relation APIs over `yi_message`;
- collection relations over children/aggregate reads;
- feed/list/map/CRDT variants.

`yi_message` has transaction, sequence, event, and subscriber-order invariants.
Do not abstract it until those invariants are explicitly part of the compiler
contract.

## Stop Criteria

Stop before shrinking `Kind` if any stored field lacks a replacement category
and migration/backfill test.

Stop before removing field-presence checks if marker-based replacements do not
cover all token/item/relationship projections and SDK result narrowing.

Stop before a compiler if marker and edge representations cannot prove
identical membership behavior and indexed performance.

Stop before stream generalization if it bypasses `storage.messages.append`,
changes dense per-session sequence allocation, changes same-transaction event
dual-write, or changes subscriber ordering.

Stop if a phase introduces an old/new alias layer. Break forward is only good
when the phase lands as one coherent world.

## Continue Criteria

Continue if a change:

- reduces public concepts;
- moves meaning into `kinds[]`;
- preserves existing hot paths;
- keeps storage optimization below the seam;
- updates core/server/SDK/docs/tests together;
- leaves no compatibility shadow.

## Final Judgment

Will following these docs produce something elegant and well engineered?

Yes, if the frame is tightened and implemented in the order above.

No, if the project treats the current wording as already-verified architecture.
The current documents are strong design artifacts, but they overstate some
claims, over-teach Tie/Moment, and make the compiler too central before it
exists.

The final product should be judged by this sentence:

> Can a kit author express capability + container + agent + membership on one
> Yi without special-case branches, while storage still hits the same indexed
> hot paths?

If yes, the direction is working. If not, the project has only renamed the old
faces.
