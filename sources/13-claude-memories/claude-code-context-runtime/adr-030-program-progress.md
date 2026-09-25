---
name: adr-030-program-progress
description: "The ADR-030 program ran 2026-08-22/23 and is implemented, awaiting Ren's sign-off: what landed where (engine a483b7a, product c8950ff), the conventions that worked for parallel Opus agents, and what was deliberately left open."
metadata: 
  node_type: memory
  type: project
  originSessionId: f383e451-e38b-455d-a692-42874ac2be2a
  modified: 2026-08-24T09:16:33.079Z
---

Ren's directive 2026-08-22: *"please finish adr 030, use opus as implementor, you can spawn more for
proper parallelism if helps."* Fable orchestrates; Opus agents implement one package each.

**Conventions that worked.** One git worktree per package under the session scratchpad
(`git worktree add <path> -b adr-030/<pkg> main` then `pnpm install --offline --frozen-lockfile`
inside it — 10 s, links resolve to the worktree's own packages), one Postgres database per package
(`createdb -h localhost -p 55432 context_runtime_test_<pkg>`; roles are cluster-global so nothing
else is needed), every test command prefixed with `CONTEXT_RUNTIME_TEST_DATABASE_URL`. Agents never
touch the main checkout; they do not rebase; the orchestrator rebases each branch onto main and
fast-forwards (linear history), then runs typecheck + biome + the full suite on main. Agents write
one acceptance note each (`specs/acceptance/history-core/<pkg>.md`, sign-off box empty) and never
edit ADR-030, decisions.md, terminology.md or CLAUDE.md — the orchestrator folds amendments in.

**Recorded on main (`cbfc2cb`, the ADR's execution-record addendum):** W1's deleted input is the
`exports` maps + the closure walker; every `packages/*` publishes at `0.1.0` lockstep; the host
plugins (provider, gateways, bracket, observer) are the engine's `packages/dsh-host`, not the
product repo's `dsh-product-host`, because Ren's first clause (*everyone can install it*) needs the
engine to publish them; the product repo is `~/repos/context-runtime-product`; U1 is Ren's outward
action.

**Landed:** W1 (`03e6ccf`) — 20 packages publishable, `@context-runtime/testkit` with the DSH
persistence contract vendored at DSH `47f9438`, `bench/publish.test.ts` builds an out-of-tree
consumer from `pnpm pack` tarballs inside `pnpm test`. Findings worth keeping: `files` is near-inert
for single-entry packages (npm always ships `main`); `packages/runtime/test/
publication-conformance-suite.ts` is a third kit-shaped family to fold into the testkit later; all
packages say `UNLICENSED` + `access: public` — Ren must pick a license before any registry push.
`6222be9` — biome skips `.claude` (two stale worktrees with Ren's uncommitted files live there);
the root `test` script defaults the disposable database name.

D4 (`36fcfd6`) — the operation table in `packages/domain/src/operations/table.ts`, reads as a
capability, one `OperationKey` constructor (nine mint sites, not five). D1 (`45865e2`) — the
`departure/1` + `composition.attestation/1` families and the examination ledger in
`packages/{domain,runtime}/src/standing/`, `proj.standing_ledger`, `policy.set_standing`, the pill
split. D1 left the orchestrator a rename: `StandingPolicyRef` in
`packages/domain/src/evidence/refusal.ts` is a third meaning of "standing" (refusal visibility) →
`RefusalVisibilityPolicyRef`, ~15 sites; do it in the final cleanup pass. Main verified green after
D1/D4: 184 files, 1722 tests.

D3 (`8686926`) — `ops.world_holds`, the kernel's three-tier effect gate, `assertWorldHold` shared by
PG/Temporal, `RECONCILED_REF_CLASSES` in the scanner, `workspace.*` effects behind a `WorldAdapter`
port this repo does not implement, real `kill -9` drill. Main green after D3: 190 files, 1762 tests.
**Trap:** `pnpm freeze:migrations -- 001_genesis` failed because pnpm 10 forwards the literal `--`;
fixed in `0255cbf` so both forms work. Integration chains must `cd` per command — a chained
`git merge` after a `cd` into a worktree merges in the worktree, not main.

**Integration debts for the cleanup pass** (each a gate someone could not write alone): the
shared-world accrual end to end (D1 arm (b) over D3's `workspace.checkout{shared}`/`share`
effects — contact point `WORLD_SHARING_TOOLS`); D4's read capability `lint` wired to D1's `lint`
(`LintPort`); the `StandingPolicyRef` → `RefusalVisibilityPolicyRef` rename; the
publication-conformance suite folded into the testkit; one `useOptionalChain` warning in
`packages/product/src/runtime.ts`.

W4 — `~/repos/context-runtime-product` exists (6 commits, no remote, 24 tests): control plane
(scrypt accounts, server-side sessions, orgs, `cp.audit`, provisioning, fixed role pool), runtime
manager (`DSH_HOME` per boundary, `dsh --profile` children, two channel dirs), the router inside the
control plane; a real DSH runtime answered through it with no model key. Engine tarballs are
vendored under `vendor/engine-tarballs/` from `6222be9` — re-vendor when `dsh-host` lands (its
note has the eight-step checklist). Findings: `exports` vs `publishConfig.exports` drift (gate
added on main); `issuePrincipalContextTicket` binds to the app connection's login/pid and cannot
cross a process boundary (W3 must take application identity as data).

D2 — the departure lane (`packages/product/src/gateway/departures.ts`, six `runtime.*` kinds incl.
`unarchive_ref`), `patchFromTrees`/`contestedValue` exported, promotion's labeled door as a
two-occurrence chain (`runtime.promote` then `runtime.promote_theirs`), archived-ref retention
class, `readGuard` on both History drivers. D2 flagged: `packages/domain/src/standing/records.ts`
holds raw NUL bytes (git sees binary — make them `\u0000` escapes in cleanup); a refused reduction
leaves its batch open on the ref (pre-existing, OPEN); the departure lane is not wired into
`ProductRuntime` (no wire carries it yet). Rebase conflicts with D3 were all one shape — D3 renamed
`crossedAsSimulation`→`crossedFromWorld` while D2 added `resolvedTheirs` beside it.

D2 landed at `2f3c7ea` after one fixture fix (its theirs drill contested `workspace/shared`, which D3's
workspace policy no longer merges → `artifacts/shared`). Main green: 194 files, 1785 tests.

W2 landed at `33ba209` — `packages/dsh-host` (the truth-layer provider under DSH's
`PersistenceCoordinator`, all 52 vendored contract titles green over Postgres canon), the
staging plane `ops.session_log_staging`, `sessions/**` merge row, two-plane encoding as two sibling
leaves (`…/env` inline, `…/data` a blob link), real `kill -9`, measured p95s (staged append 47 ms,
per-turn fold 1.2 s at 100k events). Integration: the scanner's class table is D3's
`RECONCILED_REF_CLASSES` with W2's `session` row (reversible only); W2's `openTurnRefs`/
`admitsRecovery` were dropped in favour of D3's intent-based `openEffectTurnRefs`; the
session-ref discovery half of the crash drill waits for W3's bracket (marked OPEN in
`packages/dsh-host/test/crash-recovery.test.ts`).

Integration pass (`7580f38`+`ad2937e`): D1's arm (b) had never fired on real canon (the reader's
`effects` had no implementation) — now gated over Postgres; `lint` wired through the read capability;
`StandingPolicyRef` → `RefusalVisibilityPolicyRef` (38 files, vectors re-derived with a second RFC 8785
implementation); NUL bytes → escapes; D2's open-batch OPEN was a defect — `PublicationBatchPort.abandon`
added; genesis's inert `session.*` allowlist rows removed. NOT done: folding the publication kit
into the testkit is a hard `tsc -b` project-reference cycle (runtime↔testkit) — Ren's call.
W3 (`packages/dsh-host/src/contact/`): attestation observer written into canon, attested-profile
checker (`composition-attestation` coverage dimension, default `unsupported`), `ctx.llm` mediated
port with replay refusal at mount, the bracket joining the session's open turn with approvals and
standing preconditions, git-worktree `WorldAdapter`, tickets with application identity as data,
worker-credential refusal. NOT done: the bracket does not stage a durable `EffectIntentPublication`
(needs `HostReduction.plannedEffects` to carry `PlannedEffect[]`, `MediatedHostPublisher` defer +
complete, and a `world:<id>` grant) so the session-ref crash drill OPEN stays; the model gateway is
not assembled in the composition root (needs a budget/product policy). Also: `coverage.ts` has NUL
bytes too.

W6 landed on the product's `main` (`abf0040`, 42 tests): boundary = user | project, the router names
the acting member, per-boundary quota at the router (kernel ledger for spend, never the gateway),
ledger-labeled shares. **Finding:** DSH has no per-request principal seam — `ConnectionRpcHandler`
is `(endpoint, payload, signal)` (`@deepseek-ai/dsh-client-connection` `lib/types/rpc.d.ts:11`), so
per-member canon attribution is NOT met; gate 13 goes red when upstream widens it. Engine gaps
routed to D15: decision 15's label on `AssimilationRecord`, an operator-side membership API
(`admitBoundaryMember`). Also: the router does not filter upstream's 15 loopback-privileged methods
(not exported upstream) — a `member` can call `credentials.set` on a shared runtime.

W3b landed: the bracket stages a durable intent inside a world it minted (`workspace.checkout` as a
bracketed effect writing `workspace/world`), `HostReduction.plannedEffects` + publisher defer/
complete, the session-ref `kill -9` drill green, the model gateway assembled (`models` empty by
default ⇒ nothing; `budget.limit` required), `readDumpedRows` for `--dump-config`; defect found:
a batch row outlived its turn after `kill -9` mid-bracket — `PostgresPublicationBatchPort.open` now
settles a stranded batch (`settleStrandedBatch`). Engine at 211 files / 1911 tests.

W5 done on product branch `w5` (41 tests): the five `/api` methods, five client surfaces, dsh-compat
drift (one inherited method). **Finding:** a runtime holding only its boundary login cannot compose
the truth layer — `createCanonSessionHost` opens every pool internal-mode (`role=context_runtime_worker`);
the engine's rows ship `disabled: true` in the bundle → W2b (engine: `PostgresStore.connect` with an
injected `mintTicket(identity)`, every pool principal-mode under the boundary login). Also: `UniverseId`
is a ULID (W4 used `universe-<uuid>`); `ops.migrations` records names so an old soft genesis reads as
current — the product drill compares the frozen-manifest digest.

Product `main` = `35b3984` (W5 + W6 by union: schema version 4, 10 files / 59 tests; `w5-prerebase`
tag keeps W5's pre-rebase tip).

D15 landed (`6708199`, 213 files / 1921 tests): `AssimilationRecord.originStanding: StandingSummary`
required, folded at the SOURCE node; `ops.admit_boundary_member`/`revoke_boundary_member` (SECURITY
DEFINER, worker-only, partitioned from the owner door) + `ops.universe_membership_audit`; W6's
expected call gains a fourth argument `boundary: BoundaryAssignment`. Genesis SQL comments must hold
no backticks (the file is one JS template literal).

W2b landed (`3b7910b`, 214 files / 1977 tests — **the engine is complete**): `packages/store/src/
canon-access.ts` (`CanonAccess = {internal} | {principal, principal, tickets, binding?}`,
`openCanonPool`, `createAttestorTicketMinter`), `attestorDatabaseUrl?: never` on the Store, every
pool principal-capable, the 52 DSH contract titles green under a boundary login, genesis grants
caught up to the (already member-write) policies — fifteen ACL lines. Product checklist in w2b.md.

W5c landed on the product's `main` (`82743ee`, 65 tests): the dsh-host rows armed; a real DSH child
process composes the truth layer with only its boundary login + an HTTP-minted ticket; a fold lands
in canon and reads back tenant-scoped. Engine defects found → W2c: `dumpedComposition`/
`readDumpedRows` unexported; `DSH_HOST_BRACKET_PLUGIN` names an unexported subpath;
`ops.dispatch_claims` granted to the worker only (world lane strands under a boundary login).
Also: the engine records no principal column on a canon node (attribution is the perimeter's
`author` + the ticket + universe scoping); `/api` admits one interceptor upstream.

W2c landed (engine `a483b7a`, 216 files / 1981 tests): `ops.dispatch_claims` gets a universe policy +
`SELECT, UPDATE` for the app role (policy load-bearing); exports fixed; product `w5d` → product `main`
`c8950ff` (66 tests) with the world lane under the boundary login.

**CLOSED 2026-08-23.** ADR-030 status: *implemented — awaiting Ren's sign-off* (commit after
`a483b7a`). Program record: `specs/acceptance/history-core/adr-030.md` (rows, numbers, seven items
routed to Ren: license, the publication-kit cycle, U1, loopback-privileged methods, CLAUDE.md rule 1,
the two grant widenings, the stranded-intent OPEN). All disposable worktrees and `context_runtime_test_*`
databases removed; branches `adr-030/*` kept in the engine, `w4..w5d`/`w6` in the product. Nothing
pushed anywhere (no product remote). Previously listed remaining items are all either landed or
recorded as deliberate OPENs in the ADR's closing addendum.

**Post-closure product increments (2026-08-23/24, engine `e84a51b` 218/1994, product `3eb62e7`
15 files/97 tests):** the session tree view v2 (`conversation.view` tab "Lineage": git-graph lanes,
detail pane with per-node explain, Go, Branch-here via `sessions.fork` at the node's boundary seq;
`readSessionTree` on the host), the departure/examination loop end to end (session-aware transplant,
examiner principal, `transplant`/`examine` endpoints + client actions inside the standing badge),
bracketed tools in a shared world (`contact/tool-classes.ts` classification, workspace witness,
approvals for shells), the control-plane `OutboxReconciler` wired behind `RECONCILER_INTERVAL_MS`.
Local OpenRouter set up by hand on runtime `b-09c1da41…` (`llm-pi-ai` settings + user-typed
`.credentials.yaml`); fleet-wide key policy is an offered ~10-line change. Merged branches and
worktrees for these increments removed 2026-08-24.

**UI-coherence program — DONE 2026-08-24** (Ren: *"ui/ux still doesn't feel coherent"* → planned in
`~/.claude/plans/expressive-spinning-hummingbird.md`, implemented by Opus agents, product `main`
`e0cb916`, 18 files / 109 tests): seven surfaces → three (standing display chip · approvals dock ·
Lineage tab); transplant/examine are pure node-action verbs (`node-actions.ts`) surfaced in the tab
(picker bounded `turns.first..boundary.turn` — never `turns.last`, trailing open turns refuse);
one token source `theme.ts` on `--dsw-alias-*`; `watchSession` + pure `foldTick` over
`turnEnds` (tree re-reads when its own session folds; 15 s poll is the backstop); method vocabulary
unchanged (host untouched, 8 endpoints, `dag` has no client caller). Upstream facts verified: no
plugin API to switch view tabs (`setView` private) — hence chip not button; message seats hand down
`messageId` only; no canon event. Acceptance: `docs/acceptance/ui-coherence.md` (browser walkthrough
incl.). **Incident found live**: `ensureWorkspaceRepository`'s `--is-inside-work-tree` probe made
every boundary under `data/` adopt the *product repo itself* as its workspace (fix `5c690ea`:
own-toplevel probe + `GIT_CEILING_DIRECTORIES`; damaged boundary cleaned; the probe had also
written the runtime git identity into the product repo's local config — repaired, but **15 commits
incl. the five UI ones are misattributed** `context-runtime boundary <runtime@context-runtime.invalid>`;
rewrite is Ren's call — nothing pushed, but acceptance notes cite the shas). Known trap: two
full-suite runs red with pre-fix signatures right after the merge — stale vitest transform cache;
`rm -rf node_modules/.vite` and rerun before diagnosing "impossible" failures. Web-deployment gap:
`host.pickDirectory` answers `{path:null}` headless, so Add-workspace is inert — walkthrough seeded
`storages/workspace.json` with the boundary's world-ground path by hand; workspace provisioning (or
composing upstream's `directory-picker-browse`) is open. Chips filed: git-identity hardening,
host-side stale "five endpoints" prose.

Former plan: re-pack tarballs, a product pass to
re-vendor + arm the disabled rows + flip W6's engine-gap lines, the ADR status flip. then W3 (on W2, same package), W5/W6,
the publication-conformance suite folded into the testkit, the StandingPolicyRef rename, ADR status
→ *implemented — awaiting sign-off*, decisions.md/terminology.md updates; CLAUDE.md rule 1 stays
unedited until Ren accepts (his earlier call). See [[r0-reset-progress]], [[adr-030-assurance-model]].
