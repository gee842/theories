# Agent Note: Manifold product split

Status: implemented

## Problem

The repository carries two products: the agent harness (CLI, headless, SDK, ACP) and the agentic web environment the desktop phases built on top of it. Phase 6 of the [restructuring plan](../../proposed/architecture/2026-08-26-agentic-web-desktop-repository-restructuring.md) adds control-plane weight — OIDC, Postgres, runner supervision, deployment images — that the harness never needs, and the [controlled downstream product fork](../../proposed/architecture/2026-08-24-controlled-downstream-product-fork.md) schedules the product fork at exactly this point. That note chose a same-repository `product/main` branch; the environment now warrants a separate product identity — its own name, repository, configuration, and releases — while continuing to consume harness updates cheaply.

## Decision

Manifold is a new repository and product: the personal web environment that hosts applications, of which the DeepSeek Harness agent is the first. dsh remains the upstream harness, mounted in the manifold repository as a SHA-pinned git submodule whose packages resolve as pnpm workspace members. The change is a global rename plus the smallest structural set that makes the two repositories independent; no seam, loop, event, or storage design changes.

One rule allocates every package and script: **manifold owns it unless dsh's copy is consumable verbatim without structural cost.** Owning means the code lives in the manifold repository under manifold names and manifold maintains it; consuming means importing the submodule copy unchanged. dsh gains no manifold-shaped abstraction: the only upstream changes this plan needs are the dsh-side rewirings that removal forces.

Product identity is total on manifold's side: manifold-owned surfaces — user-visible strings, durable file locations, environment variables, configuration, docs — never name dsh. The embedded harness keeps its own name only where it speaks as itself — its packages, its prompts, the harness-home variable it reads — the way an application keeps its name on the platform that hosts it.

### Repository skeleton

```text
manifold/
├── dsh/                       pinned git submodule; no tracked-file modifications, CI-enforced
│                              (builds emit into dsh/**/lib/ and *.tsbuildinfo, which dsh gitignores)
├── packages/<group>/<pkg>/    same layout conventions as dsh
├── apps/
│   ├── manifold/              product CLI (owned; forked from dsh apps/cli, keeps profile and plugin management)
│   └── web/                   browser frontend build (moved)
├── docs/  .agents/  scripts/
└── pnpm-workspace.yaml        globs: packages/*/*, apps/*, dsh/apps/web, dsh/packages/*/*, dsh/vendor/*, dsh/native/landlock-run(/packages/*)
```

The workspace globs make every dsh package and the vendored Cordis layer resolve from submodule source through `linkWorkspacePackages`, so one Cordis instance serves both trees and pre-release dsh renames surface as compile errors in one workspace. That vendored layer is the project's own maintained Cordis fork (owner decision 2026-08-31): dsh's `vendor/` no longer tracks upstream cordis-js as standing policy — its evolution is logged in the vendor manifest, an upstream sync is an exceptional deliberate act — and manifold edits it upstream-first like the rest of the harness. Hosting the fork in the manifold repository was tried and rejected: TypeScript resolves each file's imports with the compiler options of the project that owns the file, so submodule sources bind `@deepseek-ai/cordis` through dsh's own tsconfig to `dsh/vendor` regardless of manifold's facade, and a second copy splits the `Context` type identity across the workspace; the trap-free escape — manifold-owned mirror tsconfigs over every consumed submodule project — was rejected as standing machinery, and a runtime/type split as a silent divergence trap. The manifold root owns its pnpm config outright rather than mirroring dsh's: `link:` overrides and the path-keyed `allowBuilds` entry are rewritten for the `dsh/` prefix, `dsh/patches/**` is copied, and `scripts/sync-dsh-resolutions.ts` runs on every pin bump to validate patch keys against manifold's resolution and pin the shared dependency closure to the versions dsh's lockfile proved.

### Ownership allocation

The allocation is stated as of the phase-5 tree.

Moved and renamed (`@deepseek-ai/dsh-<x>` → `@manifold/<x>`; dsh deletes the original):

| Current dsh owner | Content |
| --- | --- |
| `packages/space/`, `packages/note/`, `packages/plugin-runtime/`, `packages/automation/` | The environment's domain families, including their `tool-*` Consumers; manifold mounts those tools into dsh agents through its bundles. |
| `packages/client/` (all), `packages/host/`, `packages/api/remotes`, `apps/web` | The browser half, the host half, and the Chat BFF. `api/gateway` stays in dsh: it is transport infrastructure beside `typert` with no spine dependencies, and the retained `runtime-core` bundle mounts it. |
| `packages/bundle/{web-platform, space-shell, app-chat, app-settings, app-notes, personal-plugin-runtime}` | The environment's composition layers. `runtime-core`, `agent-standard`, and `headless` stay dsh bundles; manifold profiles stack the first two. |
| `packages/extensions/{cordis-client-runner, ui-cordis}`, `packages/session-query/session-log-export`, `packages/test-support/client-runtime` | The four packages where dsh imports Client packages; moving them deletes every dsh→client edge, so no dsh package knows manifold. |
| `examples/web-cordis`, `examples/web-schedule`; the `space`, `notes`, `automation`, `plugin-promotion`, and `plugin-target` leaves of `examples/headless-agent` with their snapshot scenarios and fixtures; `vitest.web*.config.ts`, `apps/web/tests`, the web replay lane, aria goldens, the `record-browser-gif` skill | Examples, snapshot lanes, and test infrastructure move with the packages they exercise. Manifold therefore carries the keyless snapshot harness, not only browser e2e; its headless example composes the moved leaves against the retained dsh bundles. |

Owned (manifold maintains its own copy under manifold names; dsh keeps the original for the harness product):

| dsh source | Manifold copy | Why owned |
| --- | --- | --- |
| `util/home-paths` | `@manifold/home-paths` | Owns `$MANIFOLD_HOME` and `~/.manifold`; the identity constants are the package. |
| `boot/app-boot`, `boot/cmdline`, and `packages/boot/app-boot/tests` | `@manifold/app-boot`, `@manifold/cmdline` | Profile discovery, bundle layering, patch composition, and template migration are product composition; manifold's diverges in home, templates, manifest keys, and branding. The forked tests keep the lifecycle coverage the fork would otherwise silently lose. |
| `apps/cli` | `apps/manifold` (bin `manifold`) | The full CLI: profile boot, `manifold plugin` bundle installation against manifold's manifest keys and home, and the shipped agent-preset `config/` root, which only the moved `app-chat` bundle composes today. |
| `settings/settings-file`, `credentials/credentials-local`, `attachment/attachment-local`, `skill/skill-filesystem`, `identity/anonymous-user-id`, `shell/shell-env` | `@manifold/settings-file`, `@manifold/credentials-local`, `@manifold/attachment-local`, `@manifold/skill-filesystem`, `@manifold/user-id`, `@manifold/shell-env` | The user-data provider plane: where settings, credentials, attachments, skills, and the installation id live, and which home variable the environment exports into tool shells. These are Service Providers of dsh-defined seams; consumers bind by service key, so manifold composes its providers in place of dsh's — the provider-swap idiom the seam model exists for. `manifold-shell-env` is a provider of the `ctx.shellEnv` seam that `@deepseek-ai/dsh-shell` defines: it owns the `MANIFOLD_` prefix and the built-in facts under it, contributors keep declaring prefix-relative suffixes, and manifold's `subprocess-local` row sets `managedEnvPrefixes: ['MANIFOLD_', 'DSH_']` so both namespaces are scrubbed out of every child. `manifold-user-id` is a provider of the `ctx.userIdentity` seam; dsh's row lives in `local-machine`, so `manifold-local-machine` swaps it without patching a retained bundle, and one process holds one installation identity. Phase 8 replaces them again with hosted providers, so ownership here is also the staging ground for that work. |
| `bundle/local-machine` | `@manifold/local-machine` | The bundle that mounts the local user-data and execution providers; manifold's mounts the owned provider plane above over the consumed execution providers. |
| `scripts/verify-cordis-config.ts`, `scripts/gen-client-catalog.ts`, `scripts/gen-cordis-inspect-catalog.ts` with the catalog policy they import, the client build environment, the root tsconfig faces and `paths` facade, root pnpm config, and the gates runner | manifold `scripts/` and root configs | All are repository-layout-shaped; a copy that knows the `dsh/` prefix is simpler than parameterizing dsh's for two layouts. |

Everything else is consumed from the submodule unchanged: `vendor/`, the rest of `util/`, `runtime-diagnostics/`, `typert/`, `api/gateway`, `storage/`, the settings, credentials, attachment, skill, and identity Service Definitions, `core/`, `llm/`, `session/`, `interaction/`, `context/`, every capability family's Definitions, execution providers, and tools, `preset/`, `goal/`, `workflow/`, `plan/`, `todo/`, `guard/`, `hooks/`, the `extensions/` host half, the remaining `session-query/`, the remaining `test-support/`, `sdk/`, `acp/`, `workspace/`, `schedule/`, `feedback/`, `jobs/`, and the retained bundles. Dependency direction is manifold→dsh only.

### The manifold home

`$MANIFOLD_HOME` (default `~/.manifold`) is the only durable root a manifold process touches; nothing reads or writes `~/.dsh`.

- Manifold's owned boot resolves `$MANIFOLD_HOME` once through `manifold-home-paths` and points the boot-provided storage, session, and plugin path accessors at it.
- The owned user-data providers place settings, credentials, attachments, skills, and the installation id under it natively, and `manifold-shell-env` exports `MANIFOLD_HOME` into tool shells.
- `manifold-skill-filesystem` resolves every root it scans under the manifold home: no `~/.agents` convention root and no `DSH_AGENTS_HOME` environment root, which the harness home does not move.
- Boot assigns the resolved manifold home as the embedded harness runtime's home (`DSH_HOME`) for the process tree — a stated runtime fact of hosting dsh, not a hidden remap. Consumed packages that resolve the harness home internally — the `agent-presets` user root, the `agent-instructions` global file, the `llm-deepseek` upload index — therefore operate under the manifold home.
- A step-1 audit enumerates every ambient harness-home resolver and confirms each is covered by one of the mechanisms above.

Existing `~/.dsh` data does not migrate; under the pre-release stance manifold starts empty.

#### Owned replacement of a consumed package

Ownership of further consumed packages stays open, one package at a time, under one mechanical test. A fork binds at runtime through the unchanged service key, but its `declare module` merges carry new type identities, so both copies must never enter one TypeScript program: manifold may own a replacement only when no retained package it composes imports the dsh copy by name (or that importer set is owned too), its composition replaces the mounting row — in an owned bundle or by patching a retained bundle's row — and the replaced dsh copy leaves manifold's project references, with the rescope gate asserting nothing manifold-side imports the replaced name.

Under that test today: `agent-instructions` is ownable (no retained code importer; its row patches over `agent-standard`) and stays consumed only to keep AGENTS.md-loading behavior on dsh's churn; `agent-presets` is not (its retained importers are `subagent` and `subagent-in-process-driver`), and manifold instead controls it through the composing row it already owns in `app-chat` — the phase-6 control plane replaces preset machinery with manifold-native per-user composition rather than a fork; `llm-deepseek` is not (nine retained importers across the llm, sdk, session, and subagent surfaces), and a manifold model-provider policy would be a new provider of dsh's llm seam, never a fork of dsh's.

### Naming rules

- Manifold-owned packages carry the `@manifold/<x>` scope (owner decision 2026-08-31, superseding the interim `@deepseek-ai/manifold-<x>` spelling the move batches used; the redundant `manifold-` stem drops with the scope change); directory names, group layout, and `ctx` keys are unchanged. The repositories are hosted at git.datong.to (`ren/manifold`, `ren/deepseek-harness`); manifold's identity carries no deepseek-ai or dsh spelling. The rename follows the [repository naming contract](../../../../dsh/.agents/notes/implemented/architecture/2026-08-11-repository-naming-contract-and-rename-ledger.md): no alias packages, no dual service keys, every reference updated together.
- Product surfaces rename: the `manifold` bin, `$MANIFOLD_HOME`, `MANIFOLD_HOME` in tool shells, profile names, docs titles and product references, and the shell brand package (`ui-brand-official` successor) with the frontend's default document title.
- Manifest keys are product-scoped: manifold-owned bundles declare `manifold.bundle`, manifold profiles `manifold.profile`, moved client packages `manifold.client`. Manifold's owned boot and client tooling read the manifold key and accept the `dsh.*` key on packages dsh publishes; a package carrying both keys fails the load loudly. dsh's vocabulary is untouched.
- Not renamed: `ctx.*` service keys, event names, slot namespaces (`space.*`, `chat.*`), branded id types, `SessionEventMap` and `SESSION_FORMAT_VERSION` (dsh-owned vocabulary), the `@deepseek-ai/cordis*` vendor names (framework scope with no product name; a second copy or rescope would split the single Cordis runtime and type identity both trees must share), and references to dsh where dsh is meant — its packages, bundles, CLI, and the harness-home variable the embedded runtime reads.
- Stored personal plugins survive the rename: dynamic package code cannot import modules and reaches everything through `ctx` services and Remote keys, which do not rename.
- Mechanism: `scripts/rescope-manifold.ts` modeled on [scripts/rescope-vendor.ts](../../../../dsh/scripts/rescope-vendor.ts), with report, `--apply`, and check modes, covering manifests, import specifiers, and cordis config rows. The check runs as a manifold gate in two parts: manifest names and import specifiers are mechanically decided with no allowlist; product references in prose carry an allowlist for genuine dsh references.
- Bilingual docs move with their `.zh.md` and `.i18n.yaml` pairs; renames update both languages and re-record the pair per [docs/AGENTS.md](../../../../dsh/docs/AGENTS.md).

### Structural changes

Two dsh-side seam completions landed upstream as prerequisites of step 3, so the provider-swap model above holds for the whole user-data plane: `ctx.shellEnv` moved into the `dsh-shell` Service Definition with a provider-owned namespace prefix and suffix-declaring contributors, and the anonymous installation id became the `ctx.userIdentity` seam with `dsh-anonymous-user-id` as its provider (recorded in the deepseek-harness repository at `.agents/notes/implemented/architecture/2026-08-30-managed-environment-and-user-identity-seams.md`).

Beyond the moves, forks, and renames above, and the dsh-side rewiring that removal forces (listed in sequencing step 6):

1. Manifold's tsconfig faces map both manifold and submodule packages to `src`, preserving the source-plane rule of [docs/development.md](../../../../dsh/docs/development.md#typescript-project-layout) across the submodule; project references enumerate the consumed submodule packages. A manifold gate asserts every submodule workspace package has a `paths` entry, because a missing entry silently degrades that name to built-`lib` resolution and a duplicate module singleton.
2. Manifold's Host build runs Typert generation over both trees: the moved `api/remotes` Client entry consumes Remote projections that retained dsh Host packages (`goal`, `commands`, `message-feedback`, `file-reference`, `session-reference`, `cordis-host-runner`) emit during Host tsdown, so the build emits into `dsh/**/lib/` — untracked output the read-only rule permits.
3. The cordis catalog splits by output: dsh keeps `gen-cordis-catalog` and the `tool-cordis` host catalog; manifold's owned copies of the client and inspect generators produce the moved client catalogs. The shared policy is forked with them; both halves derive from the vendored Cordis API, which bounds drift.
4. Manifold-owned packages declare no `SessionEventMap` merges and no scoped events, enforced by a manifold gate. dsh's session persistence refuses event types outside its generated `KNOWN_SESSION_EVENT_TYPES` unless marked `ignorable`, and the registration surface for out-of-repo events is deferred in dsh until a consumer exists. Manifold becomes that consumer the first time an environment domain needs a durable session event — expected with the phase 8/9 domains — and landing that surface in dsh is a named prerequisite of that work, not of this split.
5. Manifold CI starts with typecheck, test, build, the owned config verifier, the rescope check, the paths-coverage gate, and an assertion that the submodule contains no tracked-file diff; hygiene and knip exclude the submodule as a standing decision, because dsh's own CI owns those signals for dsh source. Further dsh gates are adopted when their surfaces exist in manifold.

Non-goals: no package regrouping, no `ctx`/slot/event renames, no seam or agent-loop changes, no moves of shared infrastructure, no npm-publishing prerequisite, and no manifold-owned durable session events until the registration surface lands.

### Update procedure

A dsh update is one pin bump on an `upgrade/*` branch: verify the dsh commit, bump the submodule SHA, run `sync-dsh-resolutions`, `pnpm install`, run manifold gates, diff-review the owned forks against their dsh sources, merge; manifold releases record the manifold and dsh SHAs. The forks are the accepted maintenance cost of keeping dsh free of manifold-shaped structure; the diff review is the standing mitigation, and the forked boot tests keep lifecycle regressions loud. Nothing modifies tracked files under `dsh/`; a needed harness change lands in dsh first and the pin advances past it — both checkouts are local, so upstream-first costs minutes. pnpm `patches/` is the bounded escape hatch, each patch carrying the owner, purpose, and retirement condition of the [fork note's inventory](../../proposed/architecture/2026-08-24-controlled-downstream-product-fork.md#integration-patch-inventory).

### Migration sequencing

Each batch is four steps and lands green on both sides: manifold adds the renamed copies and recomposes onto them; dsh rewires its retained consumers; dsh deletes the originals; the pin bumps past the deletion. Renamed copies never collide with submodule names; between steps the submodule originals are unmounted inert source, excluded from manifold hygiene. The green criterion is measured after the deletion: dsh's gates pass with the originals gone, and manifold's pass at the new pin.

1. Land phase 5 in dsh and pin manifold at that commit. Audit ambient harness-home resolvers and assign each to an owned provider or the embedded-runtime home.
2. Bootstrap: repository, submodule, workspace globs, owned root configs and tsconfig faces, CI skeleton, and a skeletal `apps/manifold` entry that boots the current `web` profile through the consumed dsh boot and templates — dsh-flavored scaffolding that step 3 replaces, since `dsh/apps/*` is not a workspace member. Exit: today's product runs from the manifold repository with zero moves.
3. Fork the identity plane: `manifold-home-paths`, `manifold-app-boot`/`-cmdline` with their tests, the user-data provider plane with `manifold-local-machine`, `apps/manifold` with plugin management and the shipped preset root, profile templates, manifest keys, brand package. Owned-provider rows that live in retained bundles — `runtime-core` and `agent-standard` carry some — are replaced through manifold patch layers, the override the bundle layering exists for. Exit: the product runs under `$MANIFOLD_HOME` with no `~/.dsh` access.
4. Move the domain families: `space`, `note`, `plugin-runtime`, `automation`, with the headless-example leaves, snapshot scenarios, and fixtures that exercise them.
5. Move the browser stack: `client`, `host`, `api/remotes`, `apps/web`, the six bundles, the four dsh→client packages, web examples, and test lanes. Product strings on the moved surfaces — the web startup banner, help text, frontend titles, and the shell brand — rebrand to manifold in the same batch as separate re-recording commits (owner ruling 2026-08-31).
6. dsh removal and rewiring: delete the moved packages and the `web` profile; drop the moved leaves from `examples/package.json`; drop the moved tools from `python/sdk-runtime` and `gen-tool-catalog`; remove the `web` template, CLI `web` surface, and their pinned tests and snapshots; re-record the retained headless snapshots; reposition the README: dsh is the agent harness and the flagship runtime inside manifold.
7. Docs pass: moved subsystem pages and Agent Notes, bilingual pairs re-recorded, generated catalogs regenerated on both sides.

Phase 6 of the restructuring plan starts in the manifold repository immediately after step 2 and never touches dsh.

Agent Notes disposition: notes whose subject moves — the space, note, plugin-runtime, automation, client, and web-lane notes — migrate to manifold's `.agents/notes` with their packages, keeping their filenames; a cross-repository reference names the repository and path in prose instead of a relative link. dsh retains every other note. This note and the two it amends are updated in dsh in the same change.

### Supersession audit

This decision supersedes the same-repository choice in the [controlled downstream product fork](../../proposed/architecture/2026-08-24-controlled-downstream-product-fork.md): the source-ownership zones become the repository boundary itself, the integration-patch inventory becomes the pnpm `patches/` inventory, and the upgrade transaction, provenance, and extraction test carry over unchanged; that note's repository-and-branch-roles section is edited in the same change to record the manifold repository in place of `product/main`. In the [restructuring plan](../../proposed/architecture/2026-08-26-agentic-web-desktop-repository-restructuring.md), "create the product fork on `product/main`" in phase 6 becomes "create the manifold repository"; phases 6, 8, and 9 continue there, and the plan's architecture is otherwise unaffected. Notes migrate per the disposition rule above; no other active note's content changes.

## Alternatives considered

**Same-repository `product/main` branch (the fork note as written).** Rejected: control-plane dependencies and deployment machinery would enter the harness repository's gates permanently, and the environment would keep dsh's name, configuration, and release identity.

**Parameterize dsh's boot with a product-identity value instead of owning forks.** Rejected by owner decision: it threads a manifold-shaped abstraction through dsh's boot, home resolution, and profile templates that dsh does not need for itself, trading a bounded fork-maintenance cost manifold pays for a structural constraint dsh carries forever.

**Point dsh's local providers at the manifold home through their Config fields instead of owning providers.** Rejected by owner decision: the user-data plane is product identity, and a manifold whose settings, credentials, skills, and shell environment are configured dsh packages is dsh with overrides, not its own product. Manifold owns its providers of the dsh-defined seams; the composition swap is the seam model's intended use, and phase 8's hosted providers continue the same pattern.

**Consume published `@deepseek-ai/dsh-*` versions instead of a submodule.** Deferred, not rejected: the packages are on npm, but the pre-release stance renames freely, and absorbing that across a publish cycle is the expensive form of every break. The flip after dsh's first stable tag is a lockfile change plus retiring the submodule `paths` facade and project references for declaration-plane resolution, preconditioned on dsh publishing accurate `lib/types` for every consumed package under its built-package invariants.

**Vendor dsh's source into manifold.** Rejected: the sync cost buys only local patch rights that the read-only rule forbids anyway.

**Rename or re-host the vendored Cordis layer under manifold.** Rejected: both trees must share one Cordis runtime and one type identity in one process, and TypeScript binds each submodule file's imports through dsh's own tsconfig to `dsh/vendor`, so a manifold-hosted copy split the `Context` type into two identities (measured at roughly 390 errors across the owned packages); the escapes — mirror tsconfigs over every consumed submodule project, or a runtime/type split — cost standing machinery or silent divergence. The fork is maintained in `dsh/vendor` instead (see the repository-skeleton section), which manifold edits upstream-first.

**Rename dsh's manifest key to a product-neutral name so both products share one vocabulary.** Rejected with the parameterization alternative: it edits dsh for manifold's benefit. Manifold's owned boot reading its own key and accepting dsh's on dsh-published packages keeps each product's vocabulary on its own packages, with the both-keys case failing loudly.

**Keep the environment's packages upstream and make manifold a thin control plane (the fork note's allocation).** Rejected: the environment's iteration would stay gated by harness discipline in dsh's repository, and dsh would keep the web-GUI identity this split removes.

## Consequences

- A clean clone of manifold with one submodule init boots today's web product through `manifold` under `$MANIFOLD_HOME`, and the process reads and writes only under `$MANIFOLD_HOME` — never `~/.dsh`.
- `manifold plugin` installs a bundle into a manifold profile and the bundle joins the layer stack.
- No manifold-owned package name carries the `dsh-` prefix; the rescope check enforces it; dsh builds green with no manifold reference, measured after each batch's deletion step.
- The dsh repository contains no client, host, remotes, space, note, plugin-runtime, automation, or web-profile code; its retained headless snapshots are re-recorded and green; its README states the harness scope.
- One pin bump has been exercised through an `upgrade/*` branch, and it is complete when manifold's gates, composition dumps, and keyless snapshots pass at the new pin with `sync-dsh-resolutions` clean — not when Git reports no conflicts.
- The moved snapshot lanes and aria goldens replay identically under manifold at the split pin; product-string changes from the rename land as deliberate re-recordings, separate from the moves.
- Manifold CI rejects any tracked-file diff under `dsh/`, the paths-coverage gate passes, the no-session-event gate passes, and moved bilingual pairs are re-recorded.

## Risks

- The owned forks (home-paths, boot, CLI, the user-data provider plane, local-machine, layout-shaped scripts) can drift from dsh fixes. The pin-bump diff review and the forked boot tests are the standing mitigations; the cost is accepted in exchange for keeping dsh free of manifold-shaped structure, and the provider plane's divergence is eventually intended — phase 8 replaces it with hosted providers.
- A stranded pin accumulates rename debt. Bumps are pull-based; keep them small and frequent per the fork note's upgrade guidance.
- Two repositories duplicate gate tooling beyond the deliberately owned copies. Manifold starts with the minimal set; a gate needed identically by both repos is promoted into a dsh-published dev package rather than copied a second time.
- Chat UI tracks `SessionEventMap` churn across the boundary. The session-log version mechanism makes dsh's unknown events an explicit decision, and the shared workspace surfaces breaks at compile time; manifold's own durable events are barred until the registration surface lands.
- The split cordis catalogs can drift between repos. Both derive from the vendored Cordis API; the pin-bump review covers the policy forks.
- Between a move batch and its pin bump, inert duplicate sources exist. Batch ordering bounds the window; the standing submodule exclusion from manifold hygiene covers it.
- Resolved 2026-08-31: the scope is `@manifold/*`, applied through the rescope transform.
