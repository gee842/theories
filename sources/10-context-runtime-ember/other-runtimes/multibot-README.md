# multibot

Feed it a `.md` spec, get back a working artifact. Three Claude agents coordinate through a local git repo to turn your description into code you can run.

```
python run.py examples/hello-cli.md
# → runs/2026-04-24T00-59-47/hello.py, test_hello.py, full git history
```

---

## How it works

Three specialized agents, one git repo, sequential execution.

```
spec.md
   │
   ▼
┌─────────┐   writes task files      ┌──────────────────────────┐
│ PLANNER │ ───────────────────────▶ │ .multibot/tasks/open/    │
└─────────┘                          │   task-001.md            │
                                     │   task-002.md            │
                                     └──────────────────────────┘
                                                │
                                                ▼  for each task:
                                     ┌──────────────────────────┐
                    on fail,         │  git checkout -b task/N  │
                    feed eval  ┌────▶│  ┌────────────────────┐  │
                    report     │     │  │ IMPLEMENTER writes │  │
                               │     │  │ source files       │  │
                               │     │  └────────────────────┘  │
                               │     │  ┌────────────────────┐  │
                               │     │  │ EVALUATOR runs     │  │
                               │     │  │ commands, writes   │──┼── verdict: pass ──▶ merge to main
                               │     │  │ eval-N.md          │  │
                               │     │  └────────────────────┘  │
                               │     └──────────────────────────┘
                               │                │
                               └────────────────┘ verdict: fail (up to --max-attempts times)
```

**Roles:**

- **Planner** — reads `.multibot/spec.md`, writes 3–7 task files with testable acceptance criteria. Writes no source code.
- **Implementer** — picks one task, writes/edits source files to satisfy its acceptance criteria. Scoped to one task at a time.
- **Evaluator** — can read and run but cannot edit. Executes the acceptance-criteria commands, writes a report with `verdict: pass` or `verdict: fail`.

The orchestrator owns all git state transitions (branches, commits, merges); agents only touch working-tree files.

---

## Install

```
cd multibot
python3 -m venv .venv
.venv/bin/pip install -e .
```

Requirements:
- **Python 3.10+**
- **Claude Code CLI** installed and authenticated (`claude login`) — the SDK shells out to it. No separate `ANTHROPIC_API_KEY` needed.
- **git** on PATH.

---

## Usage

### Basic

```
python run.py path/to/spec.md
```

Creates `./runs/<timestamp>/`, a fresh git repo containing the artifact, the coordination files, and the full decision history.

### Flags

```
python run.py <spec.md> [--out PATH] [--model MODEL] [--max-tasks N] [--max-attempts N]
```

| Flag | Default | What it does |
|---|---|---|
| `--out PATH` | `./runs/<timestamp>/` | Workspace directory |
| `--model MODEL` | `claude-sonnet-4-6` | Claude model for all three roles (also settable via `MULTIBOT_MODEL` env var) |
| `--max-tasks N` | 10 | Cap on tasks executed in one run (planner may produce more; extras are ignored) |
| `--max-attempts N` | 3 | Implement→evaluate retries per task before marking it failed |

Exit code is `0` if no task failed, `1` if any task exhausted retries, `2` if the spec file is missing.

---

## Writing a good spec

The spec is the planner's only input, so be concrete. The example at `examples/hello-cli.md` is a good reference.

**Good spec patterns:**
- State the exact behavior: commands to run, expected outputs, file names.
- Name the language / runtime / allowed dependencies.
- Include tests in the spec — the planner will turn them into acceptance criteria the evaluator actually runs.
- List constraints explicitly (e.g., "standard library only", "single file").

**Bad spec patterns:**
- Vague qualities ("make it clean", "handle edge cases well") — the evaluator can't verify these, so they become noise.
- Broad scopes ("build a web app") — the planner will decompose reasonably but you have no control over what it chooses.

---

## Inspecting a run

Every run leaves a complete audit trail. The workspace is a real git repo:

```
runs/<timestamp>/
├── .git/
├── .multibot/
│   ├── spec.md                       ← your input, copied in
│   ├── tasks/
│   │   ├── open/                     ← planner wrote these; drained during run
│   │   ├── in_progress/              ← currently being worked
│   │   ├── done/      task-001.md    ← merged successfully
│   │   └── failed/    task-003.md    ← exhausted retries
│   └── runs/
│       └── task-001/
│           ├── eval-1.md             ← evaluator report, attempt 1
│           └── eval-2.md             ← attempt 2 (if attempt 1 failed)
└── <source files>                    ← the actual artifact
```

### Useful commands after a run

```bash
cd runs/<timestamp>

# The branching decision history
git log --oneline --all --graph

# What the planner produced
cat .multibot/tasks/done/*.md

# How the evaluator judged each attempt
cat .multibot/runs/*/eval-*.md

# The diff a single task introduced
git show task/task-001
```

Commit message conventions:
- `init:` — workspace scaffold
- `plan:` — planner output
- `start:` — task moved to in_progress
- `impl: <id> attempt <n>` — implementer's changes
- `eval: <id> attempt <n>` — evaluator's report
- `merge:` — approved branch merged into main
- `done:` / `fail:` — task file moved to final state

---

## Cost and time expectations

Based on the `hello-cli.md` example (2 tasks, 1 attempt each, both passed):
- **~3 minutes** wall clock
- **~67 agent turns**
- **~$0.40** on Sonnet 4.6

Rough scaling: cost ≈ `$0.10–0.20 per agent invocation` (planner + one implementer + one evaluator per task, plus another implementer+evaluator per retry). A 5-task spec with no retries is ~$1–1.50. Opus is roughly 5× more expensive.

---

## Customizing

### Different model per role

The SDK wrapper reads `MULTIBOT_MODEL` for all roles. If you want different models for different roles, edit `multibot/orchestrator.py` — the `_run_planner` / `_run_implementer` / `_run_evaluator` functions call `run_agent(...)`, and you can pass a role-specific model by setting the env var before each call, or by extending `run_agent` with a `model` parameter.

### Editing prompts

The role prompts live at `multibot/prompts/{planner,implementer,evaluator}.md`. They're plain markdown, loaded at runtime — edit and re-run with no reinstall needed.

Good reasons to edit:
- Bias the planner toward fewer/more tasks
- Tell the implementer about a project convention (style, testing framework)
- Tighten the evaluator (e.g., require code coverage, reject TODO comments)

### Tools available to each role

In `multibot/orchestrator.py`:
- Planner: `Read`, `Write`, `Bash`
- Implementer: `Read`, `Write`, `Edit`, `Bash`
- Evaluator: `Read`, `Write`, `Bash` (deliberately no `Edit` — it shouldn't fix bugs, only report them)

All run with `permission_mode="bypassPermissions"` so the agents can execute without interactive prompts. The workspace is isolated (its own dir, its own git repo), so the blast radius is contained — but this does mean the agents can run arbitrary shell commands inside the workspace. Inspect the output before running what the agents produced.

---

## Project layout

```
multibot/
├── README.md
├── pyproject.toml
├── run.py                           ← CLI entry
├── examples/
│   └── hello-cli.md
└── multibot/
    ├── __init__.py
    ├── orchestrator.py              ← main loop, git coordination
    ├── agents.py                    ← Claude Agent SDK wrapper (sync over async)
    ├── gitops.py                    ← subprocess wrappers for git
    ├── tasks.py                     ← task file I/O, frontmatter parser
    └── prompts/
        ├── planner.md
        ├── implementer.md
        └── evaluator.md
```

---

## Known limitations

- **Sequential only.** Tasks run one at a time. Parallel execution would require per-task worktrees and merge conflict handling.
- **No cross-task coordination.** The planner is asked for independent tasks; there's no explicit dependency graph. If task N relies on task M's output, the planner must order them, and a mid-sequence failure may cascade.
- **One-shot per agent call.** Each agent invocation is a fresh session — no conversation memory. Prior evaluator feedback is passed to the next implementer attempt as text, via file reference.
- **Trusts the evaluator.** A lenient evaluator will pass bad code. A paranoid one will reject good code. The prompt tries to strike a balance; tune it for your taste.
- **No remote integration.** Everything is local — no GitHub issues/PRs, no CI. That's deliberate for v1 simplicity.
- **No caching.** Every run starts from scratch. If the planner produces similar tasks twice, you pay twice.

---

## Troubleshooting

**`claude` not found** — install Claude Code (`npm install -g @anthropic-ai/claude-code`) and run `claude login`.

**`claude_agent_sdk` import error** — you're probably outside the venv. Use `.venv/bin/python run.py ...` or activate it first.

**Planner produces 0 tasks** — usually means the spec is too vague. Add concrete success criteria and retry.

**Evaluator passes bad output** — the acceptance criteria in the task file weren't specific enough. Edit the spec to be more concrete, or tighten `multibot/prompts/evaluator.md` to be stricter.

**Task stuck in retry loop** — check `.multibot/runs/<task-id>/eval-*.md`. If the evaluator's complaints are wrong, the implementer is being asked to fix a non-problem. Kill the run, edit the task file's acceptance criteria, or edit the evaluator prompt.

**Everything fails fast and weirdly** — check for hooks in your global `~/.claude/settings.json` that might be blocking SDK-spawned subprocesses. Multibot runs the SDK with `bypassPermissions` but user-configured hooks still fire.
