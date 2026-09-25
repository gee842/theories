# ember

Ember is a small, replayable harness for a digital life. A being is an immutable
Git lineage plus a disposable operational face. Every moment—birth, waking,
dream, approval resolution, audit, revision, and end—uses one transaction:

```text
lease → recover → perceive → attend → think → rule → act → settle → commit → CAS
```

The implementation follows [PLAN-LEAN.md](PLAN-LEAN.md), which is shipped. Its
center is four operations: journal facts, reduce events, apply exact tree edits,
and commit/CAS. [PLAN-LIFE.md](PLAN-LIFE.md) is the next phase. A being is a folder that
travels a DAG; the folder exists, and the being cannot yet see the graph it
lives in, nor does anything call `next()`.

## Try it

Ember requires Python 3.12+. Git objects are read and written in-process
through libgit2; the `git` binary is optional and used only for bundles.

```sh
uv sync --extra dev --extra litellm
uv run ember init ./world.git
uv run ember birth main -w ./world.git --words "hello"
uv run ember say main "remember today" -w ./world.git
uv run ember status main -w ./world.git
uv run ember fold main -w ./world.git
```

The CLI uses the deterministic fake model unless a provider is named. The
production adapter is LiteLLM, so the model id carries its provider:

```sh
ANTHROPIC_API_KEY=... uv run ember wake main -w ./world.git --provider litellm
```

`--provider anthropic` selects the direct reference adapter, kept because it is
the only transport that sees true per-block boundaries and so is the oracle that
measures what normalization costs.

For applications, construct `World`, then call `Runtime.advance(being, mode,
input)`. Program revisions use `Runtime.revise`; every revision pins the prior
head before it applies an exact `TreePatch`.

## What is durable

- Git commits and refs are the committed source of truth.
- Provider grammar never reaches the record: adapters translate into one neutral
  part vocabulary, so a lineage stays readable when the provider changes.
- Before commit, a synced transaction directory outside the face is truth.
- Provider content blocks close into that journal before normalization into one
  authoritative thought.
- An act and its immutable ruling are durable before dispatch.
- A lost post-effect CAS is pinned and quarantined until a no-effect two-parent
  reconciliation records it.
- `stream/` is append-only. Derived `present/`, `states/`, and the operational
  face are reconstructed and verified from facts plus historical programs.

The default reader is experiential. It cannot disclose raw streams, thoughts,
provider requests, or blobs. A forensic read first commits an audit moment.

## Security boundary

Tree-local programs are trusted and authority-gated. A fresh `python -I -S`
process isolates historical versions and failures, but it is not a hostile-code
sandbox. Workspace tools use descriptor-relative, no-follow filesystem access.
Unrestricted shell is intentionally absent. Direct Git/filesystem access outside
Ember cannot be audited without a future OS boundary.

Local filesystem locks are the v1 concurrency boundary. Shared/NFS worlds are
unsupported. `ember init` records the detected Git/fsync posture and currently
claims process-crash durability only; power-loss durability stays false until a
filesystem is explicitly qualified.

## Development

```sh
uv run ruff check ember tests scripts
uv run pytest -q
uv run python scripts/update_format_manifest.py
uv run python scripts/count_lines.py
uv run python scripts/benchmark_replay.py
uv run python scripts/benchmark_moments.py --moments 150 --verify
```

`benchmark_moments.py` is the standing scaling gate: it lives a real being and
fails if late moments cost more than early ones. Every test builds a small
lineage, so without it a cost that grows with age is invisible.

Checked golden artifacts include the semantic format/commit vectors and a Git
bundle created entirely by the runtime. The bundle is replayed and awakened by
the current body in the test suite.
