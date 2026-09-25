# Runtime

A web dashboard for one server: one passkey login, then a list of apps — a Terminal, an
Editor, a Desktop, a shell on the host itself, and a private Forgejo — that grows every
time you write another one. It is meant to be the primary way of interacting with the
machine, so closing the tab never interrupts anything and the recovery path (host SSH)
is never managed from inside.

**The north star is that adding an app is cheap.** An app is one registry entry plus a
leaf directory; the site block, the TLS, the authorization, the login exchange, the
per-app cookie, the systemd unit, the socket permissions, the deploy and the health probe
are all generated from that entry. `pnpm new-app hello --daemon` takes four seconds and
produces a working app.

```
apps/         shell (the dashboard) · terminal · hello (the scaffolded example)
services/     authd (passkeys, sessions, the only authz decision) · terminald · hello
packages/     registry (the single source of truth) · protocol · app-kit
images/       locally-built platform and workspace containers
infra/        generated: Caddyfiles, Quadlet/systemd units, JSON/INI configs
scripts/      gen · dev · build · new-app · deploy · bootstrap-host · doctor · backup · restore
docs/         architecture · invariants · add-an-app · deploy · recovery · acceptance · mail
```

## Quickstart (local, on a Mac)

Everything below runs against `*.runtime.test` with real TLS and a real passkey — the
same generator, the same authorization, the same exchange as production. Only the
upstreams differ (loopback ports instead of unix sockets).

```sh
brew install caddy tmux code-server forgejo # code-server/Forgejo only for those apps
pnpm install

pnpm gen                                   # writes infra/, prints the /etc/hosts line
sudo sh -c 'cat infra/hosts.line >> /etc/hosts'

pnpm dev                                   # the whole stack, one command
```

The first `pnpm dev` creates Caddy's local CA and prints the one `sudo security
add-trusted-cert …` command that puts it in the system trust store (do that once, then
reload the browser). `caddy trust` itself does **not** work here: the dev Caddyfile runs
with `admin off`, same as production, and `caddy trust` needs the admin API.

Then create the first account — registration is invite-only and always will be, so the
first owner comes from a CLI:

```sh
pnpm --filter ./services/authd exec tsx src/cli.ts bootstrap-user --handle you
```

Open the printed `https://os.runtime.test/register?token=…`, create a passkey, and you
are in. Enrol a second one from the Passkeys page while you are there.

| | |
|---|---|
| `pnpm check` | Biome + TypeScript, everywhere |
| `pnpm test` | vitest — the units with logic in them |
| `pnpm e2e` | Playwright against the real local stack, including Forgejo + Git CLI |
| `pnpm gen` / `pnpm gen:check` | regenerate `infra/`; fail if it drifted from the registry |
| `pnpm new-app <id> [--daemon]` | scaffold an app, register it, generate everything |
| `pnpm build` | production bundles |
| `SERVER=… pnpm run deploy` / `pnpm run doctor` | ship it / check it |

## Documentation

| | |
|---|---|
| [`PLAN.md`](PLAN.md) | the plan: intent, design, phases, acceptance. The source of truth for *why*. |
| [`docs/architecture.md`](docs/architecture.md) | the built system: topology, auth plane, trust boundaries |
| [`docs/invariants.md`](docs/invariants.md) | the sixteen things that may not change, and where each is enforced |
| [`docs/add-an-app.md`](docs/add-an-app.md) | the recipe, and what it measured |
| [`docs/deploy.md`](docs/deploy.md) | first deploy, routine deploy, the two planned restarts |
| [`docs/recovery.md`](docs/recovery.md) | break-glass runbook, including "every passkey is lost" |
| [`docs/git.md`](docs/git.md) | Forgejo web SSO, HTTPS access tokens, Git/LFS CLI, ownership and recovery |
| [`docs/mail.md`](docs/mail.md) | `@datong.to`: where its configuration lives, the DNS inventory, and a symptom→cause table |
| [`docs/acceptance.md`](docs/acceptance.md) | PLAN §17's checklist, honestly scored |
| [`docs/host-target.md`](docs/host-target.md) · [`docs/desktop.md`](docs/desktop.md) | the two apps with arguments attached |

## Status

| phase | | |
|---|---|---|
| P0 | monorepo, registry, generator, local Caddy, shell | done |
| P1 | authd: passkeys, sessions, the silent exchange, the security matrix | done |
| P2 | Terminal: protocol, app-kit, terminald, xterm UI, tmux | done |
| P3a | image, Quadlet, socket chain, mounted delivery, ops scripts | done (server-independent half) |
| **P3b** | **the actual server** | **live; post-reboot workspace relink fix ready to roll out** |
| P4 | Editor (code-server) | done |
| P5 | Host target (the second lifeline) | done |
| P6 | Desktop (Xpra + XFCE) | done |
| P7 | ops hardening, `new-app`, restore rehearsal, docs, acceptance | done |

The complete stack is deployed on the production Ubuntu host and the same generated
system runs locally on a Mac. The 2026-08-20 reboot proved Forgejo recovery but exposed a
workspace-unit relink gap; the image fix and one-command planned rebuild are committed,
with the final post-fix reboot still recorded honestly in `docs/acceptance.md`. `pnpm e2e`
exercises all 65 browser, terminal, editor, security and Forgejo cases through a real
local Caddy.
