# Filesystem-Native Agent Runtime (FNAR)
## Complete Implementation Specification v1.0-draft

**Status:** Implementation-ready draft  
**Audience:** system designers, orchestrator implementers, agent-runtime developers  
**Primary goal:** define a filesystem-native, inspectable, recursively decomposable multi-agent runtime where the filesystem is the canonical source of truth.

---

## 1. What this is

FNAR is a runtime protocol for coordinating agents through the filesystem instead of hidden orchestrator memory.

Each agent works inside a **workspace**. A workspace contains its spec, context, inputs, outputs, logs, communication files, child workspaces, status markers, inherited policy, and locally mounted capabilities. Agents advance work by reading and writing files. Hooks, humans, and automated processes observe **filesystem-visible transitions** and decide what happens next.

The central design claim is:

> large systems can be built by many agents with **bounded local context**, as long as global coherence is maintained through explicit contracts, inheritance, evaluation, and visible state transitions.

This spec is meant to be enough to start implementation.

---

## 2. Design goals

FNAR is designed to:

1. **Minimize per-agent context** so work scales without every agent understanding the whole system.
2. **Keep the filesystem canonical** so ordinary tools like `tree`, `ls`, `cat`, `find`, and `grep` can explain what is happening.
3. **Support recursive decomposition** so a workspace can create child workspaces and delegate bounded tasks.
4. **Keep orchestration inspectable** by representing state, communication, capability exposure, inheritance, and hooks as files and folders.
5. **Allow human interruption and supervision** at configurable checkpoints.
6. **Preserve full auditability and debugging** through append-only event logs and self-explaining marker files.
7. **Prevent silent drift** by defaulting to symlink inheritance and explicit copy-on-divergence.
8. **Treat hooks, tools, and skills uniformly enough** that capability exposure remains legible and policy-governed.

---

## 3. Non-goals

FNAR does **not** require:

- a specific programming language
- a specific watcher backend
- a specific LLM vendor or model
- a specific database
- a specific container runtime
- a specific OS-level permission model
- a specific UI
- a universal sandbox implementation

FNAR also does **not** assume every agent is autonomous. Humans may play protocol roles directly.

---

## 4. Normative language

The keywords **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are used in the RFC sense.

- **MUST / MUST NOT**: required for compliant implementation.
- **SHOULD / SHOULD NOT**: strong default; deviations should be intentional.
- **MAY**: optional.

---

## 5. Core abstractions

### 5.1 Workspace
A directory representing one bounded unit of work.

A workspace is the unit of:
- task scope
- local context
- outputs
- logs
- communication
- child decomposition
- capability exposure
- status

### 5.2 Contract
The explicit local definition of what a workspace must produce and how correctness is judged.

At minimum, the contract includes:
- objective
- deliverables
- input/output interface
- constraints
- non-goals
- evaluation expectations

### 5.3 Transition
A visible filesystem change that reflects state progress and may trigger hooks, humans, or downstream execution.

Examples:
- `.ready.md` appears
- `.finished.md` replaces `.running.md`
- a message file arrives in `comms/inbox/`
- a child workspace is created under `children/`

### 5.4 Hook
An event-triggered filesystem-native capability that can inspect state and react.

A hook MAY:
- approve or reject
- pause or resume
- write messages
- write status files
- spawn agents
- propose new hooks

subject to policy.

### 5.5 Capability
A mounted thing an agent can use.

FNAR recognizes three capability families:
- **tools**: directly invoked operational capabilities
- **skills**: reusable cognitive / behavioral / procedural modules
- **hooks**: event-triggered capabilities

### 5.6 Inheritance
A way to expose shared policies, prompts, hooks, tools, skills, or templates to a workspace.

Default form is a **symlink**.

### 5.7 Divergence
A local copy that replaces or supplements inherited state when local modification is necessary.

Divergence MUST be explicit and recorded.

### 5.8 Lock
A filesystem-visible exclusive write indicator.

### 5.9 Claim
A filesystem-visible advisory ownership indicator.

### 5.10 Message
A persistent markdown document used for questions, answers, warnings, proposals, or escalation between workspaces, agents, hooks, or humans.

---

## 6. High-level mental model

FNAR is best understood as:

- **workspace tree** = decomposition tree
- **status markers** = lifecycle state
- **messages** = bounded communication surface
- **hooks** = event-triggered behavior
- **symlinks** = inherited protocol and capabilities
- **local copies** = explicit divergence
- **logs** = audit trail
- **filesystem watchers** = transition detector
- **agent runner** = process that enters one workspace, acts locally, and exits

The runtime is not the hidden source of truth. The filesystem is.

---

## 7. Canonicality rules

### 7.1 Filesystem canonicality
The canonical runtime state MUST be reconstructable from the filesystem.

That includes:
- workspace existence
- workspace hierarchy
- state markers
- locks and claims
- visible communications
- inheritance links
- local forks
- mounted capabilities
- outputs
- hooks

### 7.2 Derived views
Generated machine-readable views MAY exist, but they are not canonical.

Examples:
- `.meta/manifest.generated.json`
- `.meta/effective-hooks.json`
- `.meta/effective-capabilities.json`

These MUST be treated as derived caches or summaries.

### 7.3 Tree legibility
A compliant implementation SHOULD make the workspace meaningfully inspectable with:
- `tree -a`
- `ls -la`
- `cat`
- `grep`
- `find`

---

## 8. Runtime root layout

A reference root layout:

```text
runtime/
├── hooks/
│   ├── on-workspace-created/
│   ├── on-workspace-ready/
│   ├── on-decomposition-proposed/
│   ├── on-finished/
│   ├── on-message-received/
│   └── on-tool-request/
├── tools/
│   ├── shell/
│   ├── git/
│   ├── tests/
│   └── deploy/
├── skills/
│   ├── decomposition/
│   ├── verification/
│   ├── integration/
│   └── escalation/
├── policies/
│   ├── default/
│   ├── strict-local/
│   ├── supervised/
│   └── privileged/
├── templates/
│   ├── workspace/
│   ├── hook/
│   └── message/
├── docs/
│   ├── protocol.md
│   ├── naming.md
│   ├── state-machine.md
│   └── safety-classes.md
└── tasks/
    └── <root-workspaces>
```

Notes:
- `runtime/tasks/` is the default home for root workspaces, but implementations MAY place root workspaces elsewhere.
- `templates/` SHOULD contain bootstrapping skeletons for compliant workspace and hook creation.

---

## 9. Workspace layout

Every compliant workspace MUST contain this minimum structure:

```text
workspace/
├── spec.md
├── interface.md
├── constraints.md
├── execution.mode.md
├── context/
├── inputs/
├── outputs/
├── logs/
│   ├── worklog.md
│   └── events.jsonl
├── comms/
│   ├── inbox/
│   ├── outbox/
│   └── threads/
├── children/
├── inherited/
├── local/
├── tools/
├── skills/
└── status/
```

Recommended optional directories:

```text
workspace/
├── .meta/
├── approvals/
├── reviews/
├── temp/
└── archive/
```

### 9.1 Purpose of each workspace path

| Path | Purpose |
|---|---|
| `spec.md` | local task description |
| `interface.md` | IO contract and invariants |
| `constraints.md` | local rules and limits |
| `execution.mode.md` | supervision and checkpoint behavior |
| `context/` | local context exposed to the agent |
| `inputs/` | inputs and dependency artifacts |
| `outputs/` | produced outputs |
| `logs/` | human-readable and machine-readable logs |
| `comms/` | messages in and out |
| `children/` | child workspaces |
| `inherited/` | symlinked inherited resources |
| `local/` | local overrides and forks |
| `tools/` | directly mounted tools |
| `skills/` | directly mounted skills |
| `status/` | primary and orthogonal state markers |

---

## 10. Required files and schemas

FNAR uses markdown as its primary human-readable protocol format.

### 10.1 Markdown field grammar
Protocol files SHOULD follow this structure:

```md
# <Document Type>

## Field Name
value

## Another Field
value
```

Multi-value fields SHOULD use bullet lists.

Long explanations SHOULD appear under sections like `## Reason`, `## Notes`, or `## Details`.

### 10.2 `spec.md`
`spec.md` MUST define what the workspace is trying to accomplish.

Required sections:
- `## Task`
- `## Objective`
- `## Deliverables`
- `## Non-Goals`
- `## Dependencies`

Recommended sections:
- `## Background`
- `## Risks`
- `## Open Questions`
- `## Suggested Decomposition`

Reference template:

```md
# Spec

## Task
Implement authentication middleware.

## Objective
Create middleware that validates session tokens and attaches an authenticated session object to the request context.

## Deliverables
- outputs/auth_middleware.ts
- outputs/auth_middleware.test.ts
- outputs/notes.md

## Non-Goals
- token issuance
- user management
- frontend login flow

## Dependencies
- interface.md
- constraints.md
- inputs/session_contract.md

## Background
This module will be composed into the backend request pipeline.

## Open Questions
- What is the expected behavior when the session store is temporarily unavailable?
```

### 10.3 `interface.md`
`interface.md` MUST define the local IO contract.

Required sections:
- `## Inputs`
- `## Outputs`
- `## Invariants`
- `## Failure Semantics`

Recommended sections:
- `## Data Formats`
- `## Performance Expectations`
- `## Compatibility Notes`

### 10.4 `constraints.md`
`constraints.md` MUST define local rules.

Required sections:
- `## Required Rules`
- `## Forbidden Actions`

Recommended sections:
- `## Architectural Rules`
- `## Security Rules`
- `## Performance Limits`
- `## Style Expectations`

### 10.5 `execution.mode.md`
`execution.mode.md` MUST define supervision behavior for the workspace.

Required sections:
- `## Decomposition Review`
- `## Child Spec Review`
- `## Tool Approval`
- `## Integration Review`
- `## Auto Resume`
- `## Human Escalation`

Allowed values SHOULD include:
- `none`
- `optional`
- `required`

Example:

```md
# Execution Mode

## Decomposition Review
required

## Child Spec Review
optional

## Tool Approval
required for deploy and destructive shell

## Integration Review
required

## Auto Resume
true after approval

## Human Escalation
on blocked, rejected, or privileged capability request
```

### 10.6 `logs/worklog.md`
A human-readable progress narrative.

Required behavior:
- MUST exist
- SHOULD be append-oriented
- SHOULD note major steps, assumptions, and blockers

### 10.7 `logs/events.jsonl`
A machine-readable append-only event log.

Each line MUST be valid JSON.

Minimum event fields:
- `ts`
- `event`
- `actor`

Recommended additional fields:
- `workspace`
- `path`
- `from`
- `to`
- `details`

Example:

```json
{"ts":"2026-04-05T11:03:00Z","event":"workspace_started","actor":"implementer-agent","workspace":"task-auth"}
{"ts":"2026-04-05T11:05:14Z","event":"file_written","actor":"implementer-agent","workspace":"task-auth","path":"outputs/auth_middleware.ts"}
{"ts":"2026-04-05T11:07:30Z","event":"state_changed","actor":"implementer-agent","workspace":"task-auth","from":"running","to":"finished"}
```

---

## 11. Status protocol

The workspace lifecycle is represented through marker files in `status/`.

### 11.1 Primary state markers
Exactly one primary state marker SHOULD exist at a time.

Allowed primary markers:
- `.ready.md`
- `.running.md`
- `.blocked.md`
- `.waiting-for-human.md`
- `.finished.md`
- `.failed.md`
- `.verified.md`
- `.rejected.md`
- `.archived.md`

### 11.2 Orthogonal markers
These MAY coexist with a primary state marker:
- `.lock.md`
- `.claim.md`
- `.approval-required.md`
- `.decomposition-proposed.md`
- `.integration-pending.md`
- `.proposed.md`

### 11.3 Marker file schema
All markdown state markers MUST include:
- `## Actor`
- `## Timestamp`
- `## Reason`
- `## Next Step`

Recommended additional sections:
- `## Related Files`
- `## Notes`

Reference template:

```md
# State
running

## Actor
implementer-agent

## Timestamp
2026-04-05T11:03:00Z

## Reason
Implementing middleware from approved child spec.

## Next Step
Write outputs, update worklog, replace this marker with .finished.md when complete.

## Related Files
- spec.md
- interface.md
- outputs/auth_middleware.ts
```

### 11.4 Primary marker replacement rule
When changing primary state:
1. the prior primary marker SHOULD be removed or archived
2. the new primary marker MUST be written
3. the event log SHOULD record the transition

### 11.5 Contradictory state detection
The runtime MUST detect contradictory primary states, such as:
- `.running.md` and `.finished.md`
- `.verified.md` and `.rejected.md`

Contradictions SHOULD be surfaced through:
- `logs/errors.md`
- an event log entry
- or a failure marker

---

## 12. Canonical state machine

### 12.1 States
The canonical primary states are:
- `ready`
- `running`
- `blocked`
- `waiting_for_human`
- `finished`
- `failed`
- `verified`
- `rejected`
- `archived`

### 12.2 Allowed transitions
Recommended allowed transitions:

| From | To |
|---|---|
| ready | running |
| running | blocked |
| running | waiting_for_human |
| running | finished |
| running | failed |
| blocked | waiting_for_human |
| blocked | running |
| waiting_for_human | ready |
| waiting_for_human | running |
| finished | verified |
| finished | rejected |
| rejected | ready |
| rejected | running |
| failed | ready |
| failed | running |
| verified | archived |

### 12.3 Disallowed direct transitions
These SHOULD NOT occur except through explicit override:
- `archived -> *`
- `verified -> running`
- `finished -> running`
- `failed -> verified`

### 12.4 Integration marker
Verification does not automatically mean integration. After verification, a workspace MAY also carry `.integration-pending.md` until parent composition completes.

---

## 13. Locking and claiming

### 13.1 Lock
Exclusive modification is represented by:

```text
status/.lock.md
```

A lock marker MUST include:
- `## Actor`
- `## Timestamp`
- `## Reason`
- `## Release Condition`

### 13.2 Claim
Advisory ownership is represented by:

```text
status/.claim.md
```

A claim SHOULD include the same fields as a lock marker.

### 13.3 Lock semantics
- Another writer MUST NOT modify a locked workspace unless the lock is cleared or explicitly overridden by higher policy.
- Hooks that only observe MAY still inspect a locked workspace.
- The runtime SHOULD prefer one active writer per workspace.

### 13.4 Claim semantics
- A claim is softer than a lock.
- Another actor MAY escalate or override a claim according to policy.
- Claims are primarily for coordination visibility.

---

## 14. Communication protocol

Communication happens through markdown messages.

### 14.1 Communication directories
Each workspace MUST contain:

```text
comms/
├── inbox/
├── outbox/
└── threads/
```

### 14.2 Message types
Allowed message types:
- `question`
- `answer`
- `warning`
- `proposal`
- `handoff`
- `escalation`
- `note`
- `approval_request`
- `approval_response`

### 14.3 Message file naming
Recommended format:

```text
YYYY-MM-DDTHH-MM-SSZ_<type>_<short-subject>.md
```

Example:

```text
2026-04-05T11-10-00Z_question_null-session-behavior.md
```

### 14.4 Message schema
Messages SHOULD start with YAML frontmatter followed by markdown body.

Reference template:

```md
---
type: question
from: task-auth
from_actor: implementer-agent
to: parent
priority: medium
subject: Clarify session store failure behavior
related_files:
  - interface.md
  - outputs/auth_middleware.ts
thread_id: auth-null-store-001
---

The current interface permits either:
1. hard failure
2. anonymous fallback

Please clarify expected behavior when the session store is unavailable.
```

### 14.5 Message routing
Recommended flow:
1. sender writes message in `comms/outbox/`
2. router or watcher copies or links it into recipient `comms/inbox/`
3. recipient responds in its own `comms/outbox/`
4. optional thread consolidation occurs under `threads/`

### 14.6 Message immutability
Sent messages SHOULD be treated as immutable. Corrections SHOULD be new messages or append-only follow-ups.

---

## 15. Decomposition protocol

### 15.1 Initial decision
When a workspace first becomes runnable, the assigned planner / primary agent MUST decide whether the task is:
- atomic enough to execute directly, or
- large / entangled enough to decompose

### 15.2 Decomposition outputs
If decomposition is chosen, the workspace SHOULD produce:
- `decomposition.plan.md`
- child workspaces under `children/`
- appropriate status markers reflecting review or readiness

### 15.3 `decomposition.plan.md` schema
Required sections:
- `## Why Decompose`
- `## Child Workspaces`
- `## Dependencies`
- `## Parallelism`
- `## Risks`

Reference template:

```md
# Decomposition Plan

## Why Decompose
The task mixes implementation, tests, and integration, and would exceed the desired local complexity boundary.

## Child Workspaces
- child-api: implement middleware
- child-tests: write unit tests
- child-notes: document behavior and edge cases

## Dependencies
- child-tests depends on child-api output contract
- child-notes depends on child-api behavior

## Parallelism
child-api and child-notes may proceed in parallel after interface finalization.

## Risks
- unclear null-session semantics
- need parent clarification if session store failure behavior is not fixed in spec
```

### 15.4 Child closure boundary rule
Each child workspace MUST contain enough local specification to proceed without arbitrary hidden context.

Every child SHOULD know:
- what to produce
- how correctness will be judged
- what assumptions are guaranteed
- what is out of scope

### 15.5 Decomposition review
Depending on `execution.mode.md`, the runtime MAY:
- proceed immediately
- write `.decomposition-proposed.md`
- write `.waiting-for-human.md`
- wait for approval before activating child workspaces

---

## 16. Child workspace lifecycle

### 16.1 Child creation
Each child workspace MUST be a compliant workspace.

At creation time it MUST have:
- required files
- required directories
- valid inherited mounts or empty directories where appropriate
- an initial primary state marker, usually `.ready.md` or `.waiting-for-human.md`

### 16.2 Parent-child relationship
The directory structure itself is canonical for parent-child relationship.

Optional derived metadata MAY record lineage, but is not canonical.

### 16.3 No sibling mutation by default
A child workspace MUST NOT directly mutate sibling workspaces unless policy explicitly allows it.

Sibling coordination SHOULD happen through:
- outputs
- parent integration
- messages
- explicit dependency artifacts

---

## 17. Inheritance and divergence

### 17.1 Link by default
Shared resources SHOULD be inherited through symlinks under `inherited/`.

Examples:
- policies
- prompts
- hooks
- tools
- skills
- test harnesses
- templates

Example:

```text
inherited/
├── hooks -> ../../runtime/hooks
├── policy -> ../../runtime/policies/default
└── skills -> ../../runtime/skills
```

### 17.2 Copy on divergence
If local modification is needed, the workspace SHOULD copy the relevant inherited resource into `local/` and modify the local copy.

### 17.3 Fork record
Any local divergence SHOULD be recorded with `.forked-from.md`.

Reference template:

```md
# Fork Record

## Source
../../runtime/policies/default/security.md

## Timestamp
2026-04-05T11:20:00Z

## Actor
planner-agent

## Reason
This migration workspace needs temporary read access to legacy logs that the inherited default policy forbids.
```

### 17.4 Drift visibility
The runtime SHOULD make divergence visible rather than silent. A hook MAY detect and report unexpected or risky drift.

---

## 18. Capability model

FNAR exposes three capability families:
- tools
- skills
- hooks

### 18.1 Mount locations
Capabilities MAY appear in:
- workspace-local override paths
- direct workspace mount paths
- inherited symlinked paths
- runtime global defaults

### 18.2 Recommended resolution precedence
For a capability of the same logical name:
1. `local/`
2. workspace direct mount
3. `inherited/`
4. runtime default

### 18.3 Capability shadowing
A more local capability MAY shadow a more global one, but shadowing SHOULD remain visible through the filesystem.

### 18.4 Control markers
The following control markers are recommended:
- `.disabled`
- `.approval-required.md`
- `.constrained.md`
- `.proposed.md`

### 18.5 Activation rules
A capability is active only if:
- present in scope
- not disabled
- any required approval is satisfied
- allowed by policy

### 18.6 No silent activation
Newly written hooks, tools, or privileged capabilities MUST NOT become silently active unless policy explicitly allows that class of activation.

---

## 19. Tools

### 19.1 Tool purpose
Tools are directly invoked operational capabilities.

Examples:
- shell
- git
- browser
- tests
- deploy

### 19.2 Tool directory example

```text
tools/
└── deploy/
    ├── tool.md
    ├── .approval-required.md
    └── run.sh
```

### 19.3 `tool.md` schema
Recommended sections:
- `## Purpose`
- `## Inputs`
- `## Outputs`
- `## Side Effects`
- `## Safety Class`

---

## 20. Skills

### 20.1 Skill purpose
Skills are reusable cognitive or procedural modules.

Examples:
- decomposition skill
- verification rubric
- integration procedure
- code-style transformation

### 20.2 Skill representation
A skill MAY be represented as:
- a folder containing documents and assets
- a skill spec file
- or other runtime-defined structure

### 20.3 Skill example

```text
skills/
└── verification/
    ├── skill.md
    ├── rubric.md
    └── examples/
```

### 20.4 `skill.md` schema
Recommended sections:
- `## Purpose`
- `## Inputs`
- `## Procedure`
- `## Outputs`
- `## Limits`

---

## 21. Hooks

Hooks are first-class filesystem-native plugins.

### 21.1 Hook locations
Hooks MAY exist in:
- `runtime/hooks/`
- `workspace/inherited/hooks`
- `workspace/local/hooks/`

### 21.2 Event naming
Recommended hook event directories:
- `on-workspace-created`
- `on-workspace-ready`
- `on-decomposition-proposed`
- `on-child-created`
- `on-running`
- `on-blocked`
- `on-waiting-for-human`
- `on-finished`
- `on-failed`
- `on-verified`
- `on-rejected`
- `on-integration-pending`
- `on-message-received`
- `on-tool-request`
- `on-hook-written`
- `on-archive-requested`

### 21.3 Hook folder schema
A minimal hook folder MUST contain:
- `hook.md`
- `trigger.md`
- one primary entrypoint

Allowed entrypoints MAY include:
- `run.sh`
- `run.py`
- `run.ts`
- `run.js`
- `skill/`
- `skill.md`

### 21.4 `hook.md` required sections
- `## Purpose`
- `## Event`
- `## Scope`
- `## Expected Effects`

### 21.5 `trigger.md` required sections
- `## Event`

Recommended sections:
- `## Conditions`
- `## Priority`
- `## Ordering`

### 21.6 Hook priority
Default hook priority SHOULD be `100` if omitted.

Recommended evaluation order for matching hooks:
1. lower numeric priority first
2. lexical folder name as tie-breaker
3. local hooks before inherited hooks
4. inherited hooks before runtime hooks

### 21.7 Hook outcomes
A hook MAY:
- continue
- pause
- reject
- fail
- escalate
- spawn

If a hook writes a pausing or rejecting state marker, lower-priority hooks for the same event SHOULD be skipped unless policy says otherwise.

### 21.8 Hook safety classes
Recommended hook safety classes:
- `observe_only`
- `advisory`
- `state_changing`
- `spawning`
- `privileged`

### 21.9 Agent-authored hooks
Agents MAY write hooks, but new hooks SHOULD default to disabled or proposed state.

Recommended default:

```text
local/hooks/on-finished/custom-verifier/
├── hook.md
├── trigger.md
├── run.sh
├── .disabled
└── .proposed.md
```

### 21.10 Hook example

```text
hooks/
└── on-finished/
    └── verifier/
        ├── hook.md
        ├── trigger.md
        ├── policy.md
        └── run.sh
```

Example `hook.md`:

```md
# Hook
verifier

## Purpose
Validate outputs when a workspace enters finished state.

## Event
on-finished

## Scope
workspace-local or inherited

## Expected Effects
- inspect outputs/
- write status/.verified.md or status/.rejected.md
- append to logs/events.jsonl
```

Example `trigger.md`:

```md
# Trigger

## Event
on-finished

## Conditions
- status/.finished.md exists
- required outputs listed in spec.md exist

## Priority
20
```

---

## 22. Policy model

Policies SHOULD be filesystem-native objects too.

### 22.1 Policy locations
Policies MAY live in:
- `runtime/policies/`
- `workspace/inherited/policy`
- `workspace/local/policy`

### 22.2 Policy scope
Policies MAY govern:
- readable paths
- writable paths
- allowed tools
- allowed skills
- allowed hooks
- approval thresholds
- safety classes
- spawn permissions
- runtime-global modification rights

### 22.3 Policy representation
Policies MAY be a directory of markdown docs and machine-readable companions.

Minimum recommended files:
- `policy.md`
- optional machine-readable companion such as `policy.json`

### 22.4 Privileged changes
Changes that affect runtime-global hooks, tools, or policies SHOULD require approval in all but explicitly experimental profiles.

---

## 23. Human supervision model

Humans are first-class protocol participants, not special out-of-band exceptions.

### 23.1 Human intervention surfaces
Humans MAY intervene by:
- editing workspace files directly
- answering inbox messages
- granting or denying approvals
- removing `.disabled` or `.approval-required.md` markers when authorized
- replacing `.waiting-for-human.md` with a next state marker
- modifying decomposition plans or specs

### 23.2 Checkpoint categories
Recommended supervision checkpoints:
- decomposition review
- child spec review
- privileged tool request
- privileged hook activation
- integration review
- risky policy fork

### 23.3 Human pause representation
If waiting on a human, the workspace SHOULD show:
- `status/.waiting-for-human.md`
- explanatory message or approval request in `comms/`

### 23.4 Auto resume
If `execution.mode.md` allows auto resume, the runtime MAY proceed automatically once the required approval condition becomes satisfied.

---

## 24. Event model

The runtime SHOULD emit stable event names into `logs/events.jsonl`.

Recommended canonical events:

### 24.1 Workspace lifecycle
- `workspace_created`
- `workspace_prepared`
- `workspace_ready`
- `workspace_started`
- `workspace_blocked`
- `workspace_waiting_for_human`
- `workspace_finished`
- `workspace_failed`
- `workspace_verified`
- `workspace_rejected`
- `workspace_archived`

### 24.2 Decomposition
- `decomposition_requested`
- `decomposition_proposed`
- `child_workspace_created`
- `child_workspace_ready`

### 24.3 Capability
- `tool_requested`
- `tool_used`
- `skill_invoked`
- `hook_invoked`
- `hook_written`
- `hook_activated`
- `hook_rejected`

### 24.4 Communication
- `message_sent`
- `message_received`
- `message_answered`
- `message_escalated`

### 24.5 Inheritance and approval
- `inheritance_linked`
- `inheritance_forked`
- `approval_requested`
- `approval_granted`
- `approval_denied`

---

## 25. Activation semantics

### 25.1 Workspace runnable conditions
A workspace is runnable when:
- required files exist
- required directories exist
- a valid `.ready.md` exists or policy permits direct start from another approved state
- no blocking lock or unresolved approval forbids execution

### 25.2 Hook active conditions
A hook is active when:
- present in scope
- not disabled
- approval is satisfied if needed
- trigger matches the event
- conditions in `trigger.md` are satisfied

### 25.3 Tool usable conditions
A tool is usable when:
- mounted in scope
- not disabled
- approval is satisfied if needed
- policy permits it

### 25.4 Skill available conditions
A skill is available when:
- mounted in scope
- not disabled
- policy permits it

---

## 26. Concurrency model

### 26.1 Single-writer preference
The runtime SHOULD prefer one active writer per workspace.

### 26.2 Parallelism strategy
Parallel work SHOULD happen across child workspaces rather than through many writers in one workspace.

### 26.3 Locking discipline
Exclusive writers SHOULD acquire `.lock.md` before major write phases.

### 26.4 Claiming discipline
Long-running advisory ownership MAY use `.claim.md`.

### 26.5 Race detection
The runtime SHOULD detect suspicious concurrent mutation patterns, including:
- rapid lock contention
- contradictory state transitions
- out-of-order marker replacement

---

## 27. Error and protocol violation handling

### 27.1 Examples of protocol violations
- missing required files
- missing required directories
- contradictory primary markers
- active hook with no entrypoint
- capability used before approval
- child workspace missing closure boundary
- local override without visible fork record where policy requires one

### 27.2 Surfacing violations
Violations SHOULD be surfaced visibly through one or more of:
- `logs/errors.md`
- event log entries
- `status/.failed.md`
- escalation message in `comms/`

### 27.3 Recovery
Protocol violations MAY trigger:
- automatic repair hook
- human review pause
- rollback to `ready`
- archival for audit

---

## 28. Archival model

### 28.1 Archivable conditions
A workspace MAY be archived when:
- verified and integrated
- or intentionally frozen after rejection/failure for audit

### 28.2 Archive representation
Archive state is represented by:
- `status/.archived.md`

The runtime MAY additionally make files read-only at the OS layer, but `.archived.md` remains canonical.

### 28.3 Archive contents
An archived workspace SHOULD preserve:
- final status
- outputs
- logs
- comms
- fork records
- hook proposals
- relevant approvals and reviews

---

## 29. Recommended implementation architecture

A practical reference implementation SHOULD separate these concerns:

### 29.1 Filesystem watcher
Watches root paths and emits transitions when relevant files appear, disappear, or change.

Responsibilities:
- monitor workspace creation
- detect status marker changes
- detect incoming messages
- detect new hooks or capability changes
- feed an orchestrator queue

### 29.2 Transition resolver / orchestrator
Consumes detected transitions and decides which hooks, agents, or approvals are relevant.

Responsibilities:
- resolve effective hooks
- enforce ordering and policy
- honor locks and approvals
- spawn agent runs
- write event logs

### 29.3 Agent runner
Executes one agent against one workspace.

Responsibilities:
- load visible local context
- expose allowed tools and skills
- update worklog and event log
- write outputs locally
- replace status markers appropriately

### 29.4 Capability loader
Resolves effective tools, skills, and hooks by precedence.

### 29.5 Policy engine
Determines what reads, writes, spawns, approvals, and privileged changes are allowed.

### 29.6 Message router
Moves or links messages between outboxes and inboxes.

### 29.7 Approval service
Tracks human or policy approval state in filesystem-visible form.

### 29.8 Optional derived-manifest generator
Generates `.meta/` summaries for convenience.

---

## 30. Reference execution flow

This section gives a concrete end-to-end flow.

### 30.1 Root task creation
A human or upstream process creates a compliant root workspace under `runtime/tasks/feature-x/` with:
- required files
- inherited links
- `status/.ready.md`

### 30.2 Detection
Watcher emits `workspace_ready`.

### 30.3 Planning / decomposition
Orchestrator runs planner agent.

Planner either:
- proceeds directly, or
- writes `decomposition.plan.md`, child workspaces, and possibly `.decomposition-proposed.md`

### 30.4 Review
If required by execution mode, human or policy hook edits/approves decomposition.

### 30.5 Child activation
Child workspaces enter `.ready.md` and corresponding implementers are spawned.

### 30.6 Child execution
Each child:
- acquires lock or claim if needed
- writes outputs
- updates worklog and event log
- finishes with `.finished.md`

### 30.7 Verification
`on-finished` verifier hook runs.

It writes either:
- `.verified.md`, or
- `.rejected.md`

### 30.8 Repair loop
Rejected child may go back to `ready` or `running` after repair.

### 30.9 Integration
Parent notices all needed children are verified, writes `.integration-pending.md`, and spawns integrator.

### 30.10 Parent verification and archival
Integrated parent output is verified, then archived when appropriate.

---

## 31. Minimal compliant workspace example

```text
task-auth/
├── spec.md
├── interface.md
├── constraints.md
├── execution.mode.md
├── context/
│   └── selected_context.md
├── inputs/
│   └── session_contract.md
├── outputs/
│   ├── auth_middleware.ts
│   └── auth_middleware.test.ts
├── logs/
│   ├── worklog.md
│   └── events.jsonl
├── comms/
│   ├── inbox/
│   │   └── 2026-04-05T11-15-00Z_answer_null-session-behavior.md
│   ├── outbox/
│   └── threads/
├── children/
├── inherited/
│   ├── hooks -> ../../runtime/hooks
│   ├── policy -> ../../runtime/policies/default
│   └── skills -> ../../runtime/skills
├── local/
│   └── hooks/
│       └── on-finished/
│           └── custom-verifier/
│               ├── hook.md
│               ├── trigger.md
│               ├── run.sh
│               └── .disabled
├── tools/
│   ├── shell/
│   └── tests/
├── skills/
│   └── verification/
└── status/
    ├── .verified.md
    └── .integration-pending.md
```

---

## 32. Recommended profiles

### 32.1 `strict-local`
Use when safety and control matter most.

Defaults:
- no auto-activation of agent-authored hooks
- strong approval gating
- local writes only
- runtime-global changes human approved
- privileged tools heavily gated

### 32.2 `supervised`
Use when humans want structured oversight but not constant micromanagement.

Defaults:
- decomposition review optional or required
- local hooks allowed as proposals
- selected tool approvals required
- auto-resume permitted after approval

### 32.3 `autonomous-safe`
Use for high-velocity execution with visible audit trail.

Defaults:
- most non-privileged work auto-runs
- verification still required
- no silent privileged activation
- strong logging preserved

### 32.4 `experimental`
Use only in prototypes or sandboxed environments.

Defaults:
- looser local hook and capability creation
- more permissive auto-activation
- still filesystem-visible, but lower safety bar

---

## 33. Reference implementation plan

This section is not normative, but it is meant to help you start implementation in a sane order.

### Phase 1: Static protocol and workspace bootstrapping
Build:
- workspace template generator
- marker file writer utilities
- message writer utilities
- event log append utilities
- tree / manifest inspector

Success condition:
- you can create valid workspaces and inspect them manually

### Phase 2: Watcher and transition resolver
Build:
- filesystem watcher
- transition deduplication
- state transition resolver
- event emission into `events.jsonl`

Success condition:
- state marker changes and incoming messages are detected reliably

### Phase 3: Agent runner
Build:
- one workspace-bound agent runner
- capability resolution
- context loading from visible files only
- output writing discipline

Success condition:
- a single agent can take a `.ready.md` workspace to `.finished.md`

### Phase 4: Verification hooks
Build:
- `on-finished` hook loading
- priority ordering
- verifier hook examples
- rejection / repair loop

Success condition:
- a finished workspace gets verified or rejected automatically

### Phase 5: Decomposition and child orchestration
Build:
- planner agent
- child workspace creation
- parent-child dependency tracking
- integration pending flow

Success condition:
- root tasks can decompose into multiple children and complete end-to-end

### Phase 6: Human supervision and approvals
Build:
- approval file conventions
- human review UI or CLI helpers
- pause / resume flows

Success condition:
- humans can edit, approve, and resume using filesystem-visible operations

### Phase 7: Hook authoring and advanced capability control
Build:
- local hook writing
- agent-authored hook proposal flow
- policy-gated activation
- runtime-global safety classes

Success condition:
- hooks are extensible without making orchestration opaque

---

## 34. Suggested internal helper conventions

These are implementation suggestions that make life easier.

### 34.1 Stable workspace IDs
Even though the filesystem path is canonical, it is useful to generate a stable workspace ID and include it in logs.

Recommended derived file:
- `.meta/workspace_id.txt`

### 34.2 Effective capability summaries
Generate derived summaries like:
- `.meta/effective-tools.json`
- `.meta/effective-skills.json`
- `.meta/effective-hooks.json`

These are not canonical, but they help debugging.

### 34.3 Marker replacement helper
Implement a helper that:
1. validates new state
2. archives or removes old primary marker
3. writes new primary marker
4. appends event log entry

### 34.4 Safe write helper
Implement helpers for:
- atomic file writes
- append-only event writes
- temporary file rename strategy

This reduces partial-write corruption.

---

## 35. Security and safety guidance

FNAR is not itself a full security model, but implementations should take these seriously.

### 35.1 Least privilege by default
Agents SHOULD only see and mutate what their workspace and policy expose.

### 35.2 Privileged changes
Changes to runtime-global hooks, tools, skills, or policies SHOULD require approval in non-experimental environments.

### 35.3 Dangerous tools
Destructive tools SHOULD be:
- disabled by default, or
- gated with `.approval-required.md`

Examples:
- deploy
- recursive delete
- production database write

### 35.4 Hook risk
Hooks can change future runtime behavior. Treat agent-authored hooks as higher risk than ordinary output files.

### 35.5 Human-readable explanation requirement
Any risky lock, pause, rejection, or privilege gate SHOULD explain itself in markdown.

---

## 36. Testing strategy

A useful FNAR implementation SHOULD be tested at four levels.

### 36.1 Unit tests
Test:
- status marker validation
- capability resolution
- hook ordering
- message parsing
- fork-record handling

### 36.2 Integration tests
Test:
- workspace from ready to finished
- verification hook execution
- pause / resume
- child decomposition and integration

### 36.3 Concurrency tests
Test:
- lock contention
- duplicate transition detection
- two hooks targeting the same event
- watcher burst behavior

### 36.4 Auditability tests
Test whether a human can reconstruct state from:
- `tree -a`
- marker files
- `events.jsonl`
- fork records
- messages

This last one matters a lot because inspectability is one of the core design goals.

---

## 37. Open design choices you can safely defer

You do **not** need to settle these on day one to start implementation:

- exact machine-readable policy schema
- exact sandbox backend
- whether messages are copied or symlinked during routing
- whether approval state lives in `approvals/` or marker files only
- exact human UI
- exact capability entrypoint language support

Start with the filesystem protocol and a simple orchestrator first.

---

## 38. Protocol checklist for first implementation

Before calling your implementation minimally compliant, verify that it can do all of the following:

- [ ] Create a valid root workspace from template
- [ ] Represent state with marker files in `status/`
- [ ] Append structured event logs to `logs/events.jsonl`
- [ ] Route messages between workspaces through `comms/`
- [ ] Resolve inherited vs local capabilities visibly
- [ ] Detect and reject contradictory primary state markers
- [ ] Run an agent against one workspace only
- [ ] Support planner-driven child workspace creation
- [ ] Load and invoke at least one hook from the filesystem
- [ ] Support at least one human approval checkpoint
- [ ] Represent divergence with visible local copy plus `.forked-from.md`
- [ ] Preserve enough information that `tree -a` plus `cat` explains what happened

---

## 39. Short rationale summary

FNAR is built around a few simple but strong beliefs:

1. **Agents should not need the whole world in context.** They need only the local contract required for correctness.
2. **State should be visible.** If it matters, it should be inspectable as files and folders.
3. **Coordination should be explicit.** Status markers, messages, inheritance, and hooks should not hide in opaque runtime memory.
4. **Humans should remain in the loop when desired.** Review and pause are first-class, not bolted on.
5. **Drift should be visible, not silent.** Symlink inheritance and copy-on-divergence make shared protocol legible.
6. **Complexity should live in composition.** Workspaces, contracts, and verification allow large systems to emerge from bounded local work.

---

## 40. Recommended first implementation scope

If you want the smallest useful FNAR prototype, build this subset first:

- workspace template generator
- status markers + event log helpers
- one watcher
- one orchestrator queue
- one agent runner
- one planner that can optionally decompose
- one verifier hook
- one message router
- one human approval flow

With just that, you already have the core of the system.

---

## 41. Future extensions

These are natural next steps once the base runtime works:

- richer policy schema
- stronger derived manifests
- workspace search and query tooling
- lineage visualization
- branch / merge semantics for workspaces
- OS-user isolation per workspace or per agent
- cryptographic signing of approvals or outputs
- remote workspace replication
- bundle/export format for archived task trees
- deterministic replay tooling from event logs

---

## 42. Final implementation advice

Do **not** start by building the fanciest orchestrator.

Start by making the filesystem protocol real and strict:
- a workspace template
- state markers
- event logs
- child workspace creation
- one verifier hook
- one approval flow

If those are clean, the rest can grow around them.

If those are muddy, the whole system will turn opaque.

The deepest design constraint here is not cleverness. It is **legibility**.

---

## 43. Appendix A: Example `.ready.md`

```md
# State
ready

## Actor
workspace-builder

## Timestamp
2026-04-05T11:00:00Z

## Reason
Workspace has been created with required files and is ready for planner execution.

## Next Step
Spawn planner agent or run decomposition hook.

## Related Files
- spec.md
- interface.md
- constraints.md
- execution.mode.md
```

---

## 44. Appendix B: Example `.blocked.md`

```md
# State
blocked

## Actor
implementer-agent

## Timestamp
2026-04-05T11:12:00Z

## Reason
The expected null-session behavior is ambiguous and affects implementation correctness.

## Next Step
Wait for parent or human response to the related question in comms/inbox/.

## Related Files
- comms/outbox/2026-04-05T11-10-00Z_question_null-session-behavior.md
- interface.md
```

---

## 45. Appendix C: Example `.lock.md`

```md
# Lock
exclusive write lock

## Actor
verifier-hook

## Timestamp
2026-04-05T11:18:00Z

## Reason
Verifying finished outputs before writing verified or rejected marker.

## Release Condition
Remove this lock after verification marker is written.
```

---

## 46. Appendix D: Example `.approval-required.md`

```md
# Approval Required
privileged capability use

## Actor
tool-gate-hook

## Timestamp
2026-04-05T11:25:00Z

## Reason
The requested deploy tool targets a privileged environment.

## Next Step
Human must approve or deny deployment.

## Related Files
- tools/deploy/
- comms/outbox/2026-04-05T11-25-00Z_approval_request_deploy.md
```

---

## 47. Appendix E: Example agent-authored hook proposal

```text
local/hooks/on-finished/custom-style-check/
├── hook.md
├── trigger.md
├── run.sh
├── .disabled
└── .proposed.md
```

Example `.proposed.md`:

```md
# Proposed Hook

## Actor
planner-agent

## Timestamp
2026-04-05T11:30:00Z

## Reason
This task family repeatedly fails style validation. A local post-finish style check hook would catch issues before parent integration.

## Next Step
Human or policy hook may approve activation by removing .disabled if appropriate.
```

---

## 48. Appendix F: Example `tree -a` legibility target

```text
task-auth/
├── spec.md
├── interface.md
├── constraints.md
├── execution.mode.md
├── context/
│   └── selected_context.md
├── inputs/
│   └── session_contract.md
├── outputs/
│   ├── auth_middleware.ts
│   └── auth_middleware.test.ts
├── logs/
│   ├── worklog.md
│   └── events.jsonl
├── comms/
│   ├── inbox/
│   │   └── 2026-04-05T11-15-00Z_answer_null-session-behavior.md
│   ├── outbox/
│   └── threads/
├── children/
├── inherited/
│   ├── hooks -> ../../runtime/hooks
│   ├── policy -> ../../runtime/policies/default
│   └── skills -> ../../runtime/skills
├── local/
│   └── hooks/
│       └── on-finished/
│           └── custom-style-check/
│               ├── hook.md
│               ├── trigger.md
│               ├── run.sh
│               ├── .disabled
│               └── .proposed.md
├── tools/
│   ├── shell/
│   └── tests/
├── skills/
│   └── verification/
└── status/
    ├── .verified.md
    └── .integration-pending.md
```

A human should be able to infer almost everything important from this plus a few `cat` commands.

---

## 49. Closing note

This document is intentionally opinionated. The key bet is that a multi-agent runtime becomes more powerful, safer, and more scalable when its operational truth is visible in the filesystem rather than hidden in an orchestrator's memory.

That is the spine of the whole design.
