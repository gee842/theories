# AGENTS.md

Manifold is the personal web environment that hosts applications, of which the DeepSeek Harness agent is the first. The harness is an external upstream; manifold pins a slim fork base of it as a SHA-pinned git submodule at `dsh/`, whose packages resolve as pnpm workspace members, and owns a package unless dsh's copy is consumable verbatim.

The split is governed by the Agent Note at [.agents/notes/implemented/architecture/2026-08-30-manifold-product-split.md](.agents/notes/implemented/architecture/2026-08-30-manifold-product-split.md) — repository skeleton, ownership allocation, naming rules, and migration sequencing. Read it before changing structure; this file states only the rules that bind every change.

## Hard rules

- **The submodule is read-only.** Never modify, stage, or commit a tracked file under `dsh/`. Builds may emit into paths dsh gitignores (`dsh/**/lib/`, `*.tsbuildinfo`); nothing else may appear there.
- **dsh is an external upstream, fetch-only.** Nothing is ever pushed to it. The pin targets the slim fork base `manifold-base` at git.datong.to/ren/deepseek-harness: one unmodified upstream commit plus the delta commits [`upstream-patches.yml`](upstream-patches.yml) inventories, each with an owner, exact paths, purpose, and retirement condition. A harness change manifold needs is a new delta commit there and a new inventory entry here; absorbing an upstream update is fetch, rebase the delta series, gates green at the new pin, bump.
- **Dependency direction is manifold→dsh only.** No dsh package may reference manifold.
- **Manifold-owned packages are `@manifold/<x>`.** Directory names, group layout, and `ctx` keys are unchanged from their dsh sources.
- **No renames of dsh vocabulary**: `ctx` service keys, event names, slot namespaces, branded id types, `SessionEventMap`, `SESSION_FORMAT_VERSION`, and the `@deepseek-ai/cordis*` vendor names stay as they are — both trees share one Cordis instance.
- **No manifold-owned `SessionEventMap` merges and no manifold-owned scoped events** until dsh lands the out-of-repo event registration surface.
- Documentation in this repository is English `.md` only; the bilingual pairing rules apply inside `dsh/`, not here. Link a harness file through `dsh/` when the pin carries it, and name the repository and path in prose when it does not.
- **Every non-trivial change carries an Agent Note** in `.agents/notes/`, under the harness's lifecycle, class, and format rules ([conventions](.agents/notes/README.md)).

## Node

The repository needs node `^22.19.0 || >=24.0.0` and pnpm 11. A default system node may be older or unsupported; locally, select the pinned version first:

```sh
export PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH"
```

## Commands

```sh
pnpm install          # pnpm workspaces over packages/*, apps/*, examples, and the dsh/ submodule
pnpm run typecheck    # tsc -b over the manifold faces (builds the consumed dsh projects)
pnpm run test         # manifold-owned tests; dsh's own CI owns dsh signals
pnpm run build        # manifold packages plus the consumed dsh closure, into gitignored dsh/**/lib/
pnpm run test:snapshot   # keyless replay of the runnable leaves under examples/
pnpm run test:web        # keyless browser lane: official client build, real Chromium over real HTTP
pnpm run gates           # every gate below, in order
pnpm run check:doc       # generated catalogs are fresh and every Markdown link resolves
pnpm run check:cordis-config     # the composition files load and name real plugins
pnpm run check:paths-coverage    # every submodule package resolves to source through the paths facade
pnpm run check:rescope           # nothing owned reaches a replaced dsh package
pnpm run check:no-session-events # no owned source declares a SessionEventMap member or a scoped event
pnpm run check:submodule-clean   # fail on any tracked-file change or stray file under dsh/
pnpm run check:dsh-resolutions   # patch keys resolve and the shared closure holds dsh's proven versions
pnpm run check:fork-base         # the pin is the upstream base plus exactly the inventoried delta
pnpm run gen-client-catalog      # rewrite the client slot catalog from source
pnpm run gen-cordis-inspect-catalog  # rewrite the client Cordis API catalog from the Client face
pnpm run gen-tool-catalog        # rewrite docs/tool-catalog.md by booting each tool package
pnpm manifold web                # boot the web profile from source (needs DEEPSEEK_API_KEY)
```

Gates are local scripts under `scripts/`; there is no CI service configured yet. Hygiene and knip exclude the submodule as a standing decision — dsh's own CI owns those signals for dsh source.

## Layout

```text
dsh/          pinned harness fork base (read-only submodule)
apps/         product assemblies; apps/manifold owns the `manifold` bin, apps/web the frontend build
packages/     @manifold/<pkg> workspaces at packages/<group>/<pkg>/
examples/     runnable cordis.yml leaves and their keyless snapshot lanes
docs/         subsystem references, the generated tool catalog, and cookbooks
.agents/      Agent Notes and skills
patches/      pnpm patches, copied from dsh and re-keyed for this workspace
scripts/      owned repository gates, generators, and build orchestration
```
