# Research agenda: evolving community swarms

Date: 2026-09-05. AI-drafted from the conversation; exploratory, with no implementation or benchmark results yet.

Start with the [theory overview](README.md). The [preserved conversation](context/2026-09-05-conversation.md) records how the proposal developed and the user's statement of alignment with the direction so far.

## Starting position

The motivating scenario is a community space that begins as a forum and gradually acquires calendars, badges, scheduling, wallets, voting, personal diaries, games, and specialized agents. Members reshape its interfaces and functions until the space becomes something like their operating system and part of their culture.

The agreed direction is to explore how this growth could preserve technical locality, social locality, and continuity. Each module should carry its purpose, contracts, implementation versions, data ownership, verification evidence, maintenance context, and relevant community decisions. A maintainer agent may evolve it while ordinary interactions run through ordinary code. New features should usually create options before creating obligations for everyone.

The central hypothesis is that recursive contracts, bounded dependencies, versioned artifacts, scoped adoption, and persistent maintenance ownership can keep local changes tractable as the system grows. Agreement with this direction does not establish that it works, or authorize building a product yet. The immediate work is to develop the theory and identify discriminating experiments.

## Questions that could change the architecture

### 1. What kind of locality is sufficient?

The original model is a tree such as `A(B(D, E), C(F, G))`: a node knows itself, its parent, its children, and common architectural rules. Two interpretations remain open:

- **Strict tree execution:** every cross-subtree request travels through ancestors and descendants. Parents summarize and mediate dependencies.
- **Hierarchical ownership with supplied connections:** a parent grants a child narrow capabilities whose calls may reach providers outside its subtree. Knowledge and authority remain local, while execution forms a graph.

Compare their mediation cost, discovery cost, failure propagation, and ability to keep reasoning local. If a tree repeatedly routes detailed negotiation through the root, does the decomposition fail, or does the system need richer connections? Define locality in terms of the information and obligations a maintainer needs, rather than just directory structure.

### 2. Can contracts carry enough meaning without becoming the whole program?

Types alone cannot establish compatibility. Contracts may need assumptions, guarantees, effects, state ownership, failures, progress conditions, units, ordering, idempotency, and resource limits. Each parent must establish that it satisfies its children's assumptions and that their composition satisfies its outward promises.

Investigate which properties can be mechanically checked, which need examples or tests, and which require human domain judgment. A shared prompt cannot supply missing domain facts. What happens when a badge rule depends on the meaning of “attendance,” rather than merely an event name? How does a node report an infeasible or underspecified contract upward without reconstructing the entire system?

### 3. How does local discovery support reuse and situational generation?

A resolver should distinguish reuse, configuration, composition, forking, general upgrades, and generation. A view definition may be reused by many instances with different parents and data bindings.

Explore parent-mediated discovery through searchable contract summaries. Measure how much context must cross boundaries to find candidates and verify suitability. Similar descriptions may retrieve useful candidates but cannot prove compatibility. Determine when variants deserve separate maintenance, when they should remain configurations, and how duplicate implementations are recognized without universal agent awareness.

### 4. How do state and shared meaning evolve?

Replacing code while preserving an interface is easier than changing records, domain semantics, or ongoing commitments. Identify who owns migrations, compatibility adapters, and the transition of active sessions. Reverting a code version does not reverse incompatible writes.

Use changes to attendance, wallet reward rules, voting eligibility, and calendar event semantics as cases. Can old and new versions coexist over shared records? When must their adoption be coordinated? What history must remain available after an app is retired? A replacement criterion should cover observable behavior and data obligations, not only successful builds.

### 5. How does the community choose the scope of change?

Personal layouts, group workflows, and community rules have different audiences and consequences. Explore how a request identifies its affected scope, how experiments become usable, and how the relevant audience adopts a version.

The theory should support alternatives over shared data without assuming that every preference can coexist. Conflicting shared commitments still require a social decision. Keep the mechanism for representing authority distinct from any particular governance policy; the conversation did not choose a voting system or prescribe a universal approval workflow.

### 6. Who carries maintenance cost over time?

Cheap creation may produce expensive obligations. Examine ownership transfer, dormant maintainers, abandoned apps, dependency consolidation, retirement, archival access, and reconstruction of an agent's working context. What happens when an app's original sponsor leaves but others depend on it?

Maintenance context must survive individual agent sessions. Resource and maintenance budgets should make ongoing cost attributable without presupposing a billing model. The system needs a way to stop maintaining executable variants while preserving community history.

### 7. How independent are implementation and verification?

An agent can write code and tests that share the same mistaken assumption. Independent review also does not establish correctness merely because agents agree. Explore contract-derived checks, adversarial examples, integration evidence, and bounded repair assignments. Verification should scale with the scope and consequences of the change.

At swarm scale, measure accepted useful changes and rework rather than agent activity. Determine whether verification and integration queues become bottlenecks, and when adding workers ceases to improve delivery.

### 8. What does “does not get slower or harder” mean?

The proposed target is bounded cost for a local interaction or change despite growth in unrelated modules. It does not imply unlimited active computation at constant cost. Investigate demand loading, dormant agents, bounded task queues, selective event subscriptions, resource isolation, and cost attribution by module version.

Define an active dependency set for each interaction. Distinguish cold generation latency, warm loading, ordinary interaction latency, background work, and agent maintenance cost. Likewise distinguish a local layout change from an identity migration that necessarily affects many modules.

## Proposed repeated-evolution experiment

Build a minimal forum, module host, and request-to-experiment process only when moving from theory to a prototype is intended. No stack, deployment model, schedule, or production scope is selected here.

Exercise successive changes rather than presenting isolated generation demonstrations:

1. Add a calendar using the community agent.
2. Add attendance badges through the calendar's published contract.
3. Create competing calendar designs over the same event records and adopt them for different audiences.
4. Add a scheduler that combines existing capabilities.
5. Change a calendar contract and stored representation; exercise compatibility and migration handling.
6. Introduce a broken release; observe containment, diagnosis, replacement, and recovery.
7. Retire an app while retaining access to its records and history.
8. Install hundreds, then thousands, of inactive modules and repeat the original forum measurements.
9. Add overlapping feature requests and concurrent maintainers to test discovery, integration, and maintenance ownership.

Record runtime latency, memory, background activity, dependency fan-out, and interference with core interactions. For each change, record context retrieved, contracts revised, unrelated modules touched, coordination required, integration delays, repairs, and continuing maintenance obligations. Include whether members can understand and adopt alternatives without losing their shared history.

Compare results against module count, active dependency count, and the number of prior changes. Rising effort with genuinely affected dependencies may be expected; rising effort with unrelated accumulated features challenges the central hypothesis. The twentieth change should be at least as revealing as the first generated app.

## Evidence standard

Keep architectural commitments, hypotheses, experiment designs, and observed results separate. Preserve failed decompositions and counterexamples. The theory earns support when repeated evolution remains local under meaningful tests, and must change when hidden dependencies, semantic drift, governance conflicts, or maintenance accumulation defeat that locality.

## Proposed tightening after the 2026-09-07 assessment

The [critical assessment](context/2026-09-07-soundness-assessment.md) recommends making the tests harder to satisfy by construction. These are assistant proposals awaiting further discussion.

- Declare the supported class of changes and predict the affected modules before implementation. Record newly discovered dependencies and scope expansion rather than relabeling every surprise as expected locality.
- Measure contract size and ancestor/reconciler work so bounded worker context cannot conceal growing central complexity.
- Distinguish inactive catalog growth, active agent concurrency, and accumulated semantic dependencies. A dormant-app benchmark does not establish the other two properties.
- Compare local coordination against a strong single-agent or repository-wide-context baseline on the same modular host, using comparable tools, resources, and independent acceptance checks.
- Include the chain attendance → badges → eligibility/rewards → downstream actions, followed by a change in attendance meaning and retroactive corrections. Determine which historical commitments can remain stable and which require coordinated policy or state transitions.
- Track human clarification, adoption decisions, support, and ownership transfer as part of maintenance cost.

The central question is whether the system can discover and maintain compact boundaries through unforeseen changes. Contract sufficiency is a condition to establish, not an already-solved mechanism.

## Proposed focus after comparing harnesses and swarm research

The [2026-09-07 comparison](context/2026-09-07-harness-and-swarm-comparison.md) suggests borrowing execution isolation, delegation, checkpointing, queues, and traces from existing systems. The proposed research object is the protocol that maintains module boundaries and continuing obligations across changes. This remains an assistant recommendation, not an implementation decision.

Specify the transition from a requested change to an affected-contract prediction, candidate implementation, acceptance evidence, adoption decision, state transition, activation, observation, and eventual retirement. Define how incomplete contracts are discovered and repaired, including when a parent must widen its scope or revise the decomposition. Keep durable module responsibility separate from the temporary task graph used for an individual change.

Use the same modular host and execution harness for an ordinary task-oriented coding-team baseline and for the added module-maintenance protocol. Select twenty changes independently of the implementation. Include semantic corrections, conflicting adoption scopes, migration failure, ownership transfer, and retirement. Account for worker and ancestor context, contract growth, human effort, accepted behavior, and continuing maintenance cost. Later ablations could isolate the contribution of curated module context, contract propagation, and adoption support. Test inactive catalogs and active concurrency separately from accumulated semantic dependencies.

Existing systems may support this protocol as extensions. The comparison neither establishes exclusive capability nor proves that the combined approach is original. No experiment has been run.

## Current plan after Ren’s direction to surpass

Ren explicitly asks for an updated vision aimed at surpassing existing systems. The [next-vision package](next-vision/README.md) is now the primary ordered plan. It adds adaptive boundary search, revision-aware change propagation, evidence reuse with validity conditions, learning that transfers, and useful active concurrency as mechanisms to investigate.

The next proposed implementation package tests one semantic change across calendar observations, participation qualification and badges. Later stages add a complete community loop, 200-change competitive comparisons, learning over histories up to 1,000 changes, and active concurrency toward 1,000 workers. See [PLAN.md](next-vision/PLAN.md) for deliverables and [EVALUATION.md](next-vision/EVALUATION.md) for outcome matching, baseline selection, uncertainty rules, and provisional gates.

The ambition to surpass is user-directed; these mechanisms and targets are assistant proposals. Existing work on adaptive agent designs, workflows and context is included as competition. No prototype or comparative result is claimed.
