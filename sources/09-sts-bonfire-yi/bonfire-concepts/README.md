# Bonfire

A messaging substrate where humans, bots, groups, and mini-programs are peers.

Bonfire is built on **Yi**: a stable root identity with immutable Kind bindings,
schema-authored state, and normalized components owned by the fifteen bounded
contexts. Identity owns principal coordinates, Custody owns holdings,
Containment owns placements, Relations owns occurrences, and Authority owns
certificates. Joined reads expose those facts under `contexts.*`; Kind-authored
state remains under its Kind address.

Authors use `defineKind` and `defineKindFamily` with semantic `facet.*`
contributions. The compiler closes each family into a deterministic
representation plan, and the runtime executes that plan without field-based
storage inference. Every durable multi-context change commits atomically on the
Domain-scoped Occasion spine.

Bonfire also ships a separate message DAG (`stream`) for high-volume chat, a content-block message envelope, and a sandboxed miniapp runtime (sigils) that ride inside messages.

## Documentation

[`docs/`](docs/README.md) — start here.

- [Overview](docs/overview.md) — what Bonfire is + architecture in one read.
- [Concepts](docs/concepts/) — the mental model (yi, kinds, ports, gates, sessions, messages, federation).
- [Author guide](docs/author-guide.md) — defining kinds, writing handlers, shipping a kit.
- [Kit author guide](docs/kit-author-guide.md) — patterns for shipping a community kit.
- [Glossary](docs/glossary.md) — terminology cheat sheet.
- [SDK](docs/sdk/) — `@bonfire/sdk` quickstart + reference.
- [Sigil](docs/sigil/) — sandboxed miniapps.
- [Hearth](docs/hearth.md) — the reference creator room.
- [Cookbook](docs/cookbook/) — worked recipes from "vanilla capability" to "delegated key with sub-delegation."
- [Examples](docs/examples/) — runnable reference apps.
- [Operations](docs/operations/single-instance.md) — running a Bonfire server.

## Quickstart

```bash
pnpm install
pnpm build
pnpm check:browser
pnpm check:package
pnpm check:release
pnpm test
```

`pnpm build` runs the TypeScript project build. `pnpm check:browser` runs the
reference web app's real Vite browser bundle and catches accidental imports of
Node-only package surfaces. `pnpm check:package` packs `@bonfire/core` and
`@bonfire/sdk`, installs the tarballs into a temporary consumer project,
typechecks public imports, runtime-imports the subpaths, and browser-bundles
the packed client entry. `pnpm check:release` composes the SDK release gate:
repo and SDK type checks, public-surface tests, browser/package checks, and
docs example build/smoke tests.

### Development checks

Use the change-scoped gate for the normal edit/test loop:

```bash
pnpm check:changed -- --dry-run # explain the selected checks
pnpm check:changed             # run related tests and impacted typechecks
pnpm check:module server       # whole module + transitive dependents
PG_URL=postgres:///bonfire_test pnpm check:model # exhaustive persistence gate
```

`check:changed` uses the Git diff, Vitest's reverse dependency graph, and the
workspace package graph. Ordinary leaf changes usually run only related unit
tests. Migrations, PostgreSQL adapters, storage contracts, and shared test
configuration conservatively escalate to connected integration coverage.
`check:release` remains the final merge/release certification gate; a scoped
development check is not a substitute for it.

Run an example:

```bash
pnpm --filter @bonfire/example-hello-bot dev
# { msg: 'hi, world' }
```

Run the dev server + web app:

```bash
pnpm dev
```

## Packages

| Package | Role |
|---|---|
| `@bonfire/core` | Yi substrate, runtime, dispatch, storage interface |
| `@bonfire/sdk` | Authoring surfaces (`defineKind`, `defineHandler`) + isomorphic client + agent runners |
| `@bonfire/std` | Standard kit: the `@bonfire.std.sigil:sigil` held-miniapp kind, token factories (`makeCurrency`, `makeMembership`, `makeVoucher`), community kit (Wishing Pool, Need Wall, Witness Book, Roster, Doorway), transition primitives (`graduate`, `crystallize`, `release`, `compost`, `commemorate`), ambient-tick infrastructure, and the named spirits (Wren, Ember, Sage, Fox, Owl, Heron); experimental tests-only kits live under `community/incubator/` |
| `@bonfire/server` | Postgres storage + WebSocket + HTTP server |
| `@bonfire/chat` | Framework-agnostic chat reducer |
| `@bonfire/chat-ui` | Backend-agnostic React chat primitives (`useChat`, `MessageList`, `Composer`, block-renderer registry) |
| `@bonfire/chat-bonfire` | Bonfire-wired chat surface (`<BonfireChat>`, sigil/question renderers, artifacts pane) |
| `@bonfire/sigil` | Sandboxed miniapp compiler + runtime |
| `@bonfire/sigil-react` | React bindings for sigils |
| `@bonfire/sigil-bonfire` | Host-side SDK bridge for sigils |
| `@bonfire/web` | Reference web UI |

## License

Bonfire is licensed under the MIT License. See [`LICENSE`](LICENSE).

No public git remote is declared yet; package repository metadata will be
added when a public repository exists.
