# Harnesses, agent teams, and swarm research — 2026-09-07

## Provenance and status

Ren requested the comparison below after asking whether the idea was solid. This is an assistant-authored assessment based on selected primary documentation, project materials, and papers consulted on 2026-09-07. It is not an exhaustive literature review, implementation audit, replication, or claim of priority.

The substantive response below is prepared for the current conversation. Additional evidence notes distinguish reported mechanisms from our inferences. These recommendations are not recorded as new user endorsements. No prototype or benchmark was implemented in this turn.

An identical copy is retained at [the corpus source](/Users/ren/theories/sources/15-codex-theory-conversations/2026-09-07-evolving-community-swarms-comparison.md). Earlier conversation snapshots remain unchanged.

## Ren’s request — verbatim

> think about existing harness and agent team, and other swarm implementations/papers, how's our solution?

## Assistant’s substantive response

**Our proposal is credible, but the comparison narrows where its contribution could be.** Hierarchy, local context, persistence, and self-modification already have strong precedents. Our most interesting question is how those mechanisms can sustain a community’s software through years of changing requirements.

Here is how the closest work compares:

| Existing work | What it already provides | What our proposal needs to add |
|---|---|---|
| **Codex / Claude Code teams** | Delegation with separate contexts; Claude teams also provide peer communication and shared task coordination. [Codex docs](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Claude docs](https://code.claude.com/docs/en/agent-teams) | Persistent responsibility for a module’s meaning, state, and dependents across many tasks. |
| **LangGraph** | Nested subgraphs, boundary schemas, private internal state, and persistent execution. This closely resembles your recursive structure. [Documentation](https://docs.langchain.com/oss/python/langgraph/use-subgraphs) | A protocol for evolving those boundaries and migrating the running application. |
| **Cursor swarms / Gas Town** | Recursive planning and shared design knowledge in Cursor; durable worker identities and recoverable work in Gas Town’s architecture. [Cursor report](https://cursor.com/blog/agent-swarm-model-economics), [Gas Town design](https://github.com/gastownhall/gastown/blob/main/docs/design/architecture.md) | Connect engineering coordination to community adoption, shared records, and continuing maintenance obligations. |
| **MetaGPT / ChatDev** | Structured roles and collaboration artifacts. Current ChatDev also encompasses incremental development and broader orchestration. [MetaGPT paper](https://arxiv.org/html/2308.00352v7), [ChatDev repository](https://github.com/OpenBMB/ChatDev) | Maintain domain boundaries through successive, unforeseen changes. |
| **MacNet** | Graph-organized collaboration with local artifact refinement, supporting the feasibility of limited-context collaboration. [Paper](https://arxiv.org/html/2406.07155v3) | Demonstrate that locality survives accumulated dependencies in a running application. |
| **Darwin Gödel Machine / SICA** | Agents modify their own implementations and evaluate resulting versions. [DGM](https://arxiv.org/html/2505.22954v2), [SICA](https://arxiv.org/html/2504.15228v2) | Evaluate changes against existing users’ commitments, state compatibility, and adoption choices. |
| **Webstrates / Varv** | Collaborative, modifiable software; different interfaces over shared content; declarative mechanisms for changing applications. These are particularly close to our product vision. [Webstrates](https://webstrates.net/project/a-brief-overview/), [Varv](https://varv.projects.cavi.au.dk/) | Integrate agent maintenance, contract evolution, resource limits, and community governance. |

These are possible foundations. The last column describes work our architecture must specify; it does **not** establish that the existing platforms cannot support it.

**The strongest refinement is to make the maintained module the durable unit.**

An agent can wake, work, and disappear. What persists is the module’s:

- Purpose, behavioral contract, and declared dependencies.
- Owned records, version history, and migration obligations.
- Acceptance evidence and relevant community decisions.
- Maintenance owner, resource budget, and adoption scope.

That distinction makes thousands of modules plausible without requiring thousands of continuously running agents. Persistence alone, however, does not ensure that the saved context remains compact or sufficient.

Cursor offers a useful warning: its recursive swarm still needed shared design decisions, reconciliation, and mechanisms for splitting oversized files. A tree did not prevent incompatible interpretations from developing. Our parents will face the same problem unless contracts and escalation rules carry the relevant meaning. [Cursor’s engineering report](https://cursor.com/blog/agent-swarm-model-economics)

**The missing centerpiece is a protocol for changing contracts.** I would organize it around this sequence:

1. Describe the proposed change and its intended audience.
2. Identify changes to behavior, meaning, state, and resource use.
3. Predict affected dependents through declared contracts.
4. Build and check a candidate version.
5. Coordinate necessary adoption and state transitions.
6. Activate, observe, repair, and eventually retire versions.

Consider your community calendar. Changing its layout should remain local. Changing “attendance” from registration to verified participation may affect badges, voting eligibility, and rewards already spent in a game. The system must discover those obligations and determine how historical records are treated. A successful build cannot settle that question.

Our key hypothesis becomes: **most changes can stay local, while changes to shared meaning trigger explicit, proportionate coordination.** Whether that uses strict parent-mediated communication or parent-supplied capabilities remains open.

The evidence also argues against treating agent count as success. A recent scaling study found task-dependent outcomes, but explored counts only up to nine agents; it does not establish thousand-agent or long-term application evolution. [Study, revised version](https://arxiv.org/html/2512.08296v3)

I would test our protocol on the same modular application and execution harness as an ordinary coding-team baseline, using an independently chosen sequence of twenty changes. Measure accepted behavior, human effort, total context—including ancestors—unexpected dependency discoveries, migration failures, and maintenance cost. Test dormant catalog size and active concurrency separately.

**We have a worthwhile architectural hypothesis, with substantial prior art and an unproven central mechanism.** The strongest potential contribution is the integrated handling of contracts, state, and adoption over time. Existing systems give us much of the machinery to investigate it.

I saved the [comparison and source notes](/Users/ren/theories/theories/evolving-community-swarms/context/2026-09-07-harness-and-swarm-comparison.md) and updated the theory’s research agenda.

## Additional evidence and interpretation notes

### Execution and coordination

- **Codex:** Official subagent documentation and the [Agents SDK orchestration guide](https://learn.chatgpt.com/docs/mcp-server) were consulted. Scoped work, handoffs, and traces are useful implementation primitives. This does not select an OpenAI stack or constrain the hypothetical architecture to the present harness.
- **Claude Code:** The reviewed team documentation describes independent contexts, dependencies in shared tasks, direct messaging, and completion hooks. Its current team limitations include no nested teams and limited teammate resumption. [Worktrees](https://code.claude.com/docs/en/worktrees) isolate file edits; file isolation does not establish behavioral compatibility.
- **OpenHands:** [Conversation persistence](https://docs.openhands.dev/sdk/guides/convo-persistence) restores execution context; [workspace architecture](https://docs.openhands.dev/sdk/arch/workspace) abstracts local and remote execution. Existing harnesses therefore should not be described as universally forgetful. A curated module dossier has a different purpose from retaining every event.
- **Gas Town:** The design document distinguishes durable worker identity from ephemeral sessions and describes persistent coordination state. It mixes operational descriptions and planned work; batch/bisect integration is marked in progress or blocked. The document is architectural evidence, not proof that every described feature is shipped.
- **Cursor:** The July 20, 2026 first-party report describes design-document references, reconciliation, and a curated shared guide alongside recursive task decomposition. Its SQL experiment evaluates a specified implementation task. It does not test continuing community adoption or shared-state evolution. No reported throughput or test score is treated as a result for our theory.
- **LangGraph:** Subgraph schemas support encapsulation and separately developed graphs. [Persistence documentation](https://docs.langchain.com/oss/python/langgraph/persistence) also describes checkpoints and cross-thread memory. Checkpoint recovery is distinct from establishing domain correctness after a schema migration; concurrent access to a persistent subagent needs coordination. A graph runtime could host our proposed protocol.

### Collaboration and self-modification papers

- **MetaGPT:** The reviewed arXiv v7 uses structured procedures and artifacts with feedback. Appendix A describes experience-informed role/prompt updates while keeping structured communication interfaces fixed. This supplies a useful contrast with our proposed contract evolution, without implying MetaGPT cannot be extended.
- **ChatDev:** Distinguish the [original ACL 2024 paper](https://aclanthology.org/2024.acl-long.810/) from the current repository. The latter presents ChatDev 2.0 / DevAll and records incremental-development and experience-reuse features. Characterizing current ChatDev as merely a one-shot software factory would be inaccurate.
- **MacNet:** The reviewed v3 defines actors at graph nodes and critics at edges, passing refined artifacts rather than all prior dialogue. Its 64-node complete DAG corresponds to 64 + 64 × 63 / 2 = 2,080 actor/critic assignments—our calculation from its definition. This is not evidence of 2,080 simultaneous processes or persistent product maintainers. Its benchmark findings do not establish years of application evolution.
- **Darwin Gödel Machine:** The reviewed v2 evaluates candidate coding-agent implementations and retains an archive of descendants. The underlying model and evolutionary search loop remain fixed in that version. Archive and evaluation mechanisms are relevant; objectives for community compatibility and adoption would be additional design work.
- **SICA:** The reviewed v2 demonstrates evaluated self-edits to agent code and discusses limitations including path dependence. Evidence that an agent can improve its implementation under benchmark objectives does not establish indefinite improvement or preservation of a community’s changing commitments.

### Malleable software

- **Webstrates:** The official overview describes persistent collaborative documents, transclusion, history, and tools that can themselves be modified. Its asymmetric collaboration is directly relevant to members using different interfaces over shared content. The original paper PDF could not be retrieved in this comparison; the claims here rely on the project overview.
- **Varv:** The CHI 2022 project page describes applications expressed through extensible declarative definitions and separation of logic from interface modality. A restricted representation could make generated changes easier to inspect and check; that is our proposed use, not a demonstrated swarm result.

### Limits of scaling evidence

The revised v3 of *Towards a Science of Scaling Agent Systems* reports 260 configurations across six benchmarks. Selected methods and limitations were inspected in this comparison, extending the earlier assessment’s abstract-level reading. Agent counts reach nine; the coding evaluations use small subsets of 20 instances per coding benchmark. Results are task-dependent and cannot be extrapolated to thousands of persistent modules. No experiments were replicated.

The [Anthropic C compiler report](https://www.anthropic.com/engineering/building-c-compiler), consulted in the preceding assessment, remains another relevant first-party example: verification and partitioning work were central to making parallel agents useful. It does not supply evidence for community-scale longitudinal evolution.

## Proposed architectural interpretation

The candidate contribution is a protocol for maintaining semantic boundaries, authoritative state, and scoped adoption over repeated changes. This is a synthesis and research target, not an established originality claim. No reviewed source establishes the entire combination with sustained low maintenance cost; the review does not establish that no such work exists elsewhere.

Treat the following as independently varying structures:

1. A durable module responsibility hierarchy.
2. A temporary task graph for carrying out a particular change.
3. A reusable artifact/version graph.
4. The application’s runtime capability connections and current view tree.

A task graph can be generated from a module’s change request without duplicating its persistent identity. Multiple workers may implement one module; a worker may later maintain a different module. Shared contracts require explicit owners and affected-dependency discovery. Root/ancestor coordination must be measured rather than hidden outside a worker’s context budget.

Preserve the unresolved strict runtime mediation versus supplied-capability alternative. A framework’s support for graph execution does not decide that theoretical choice.

## Proposed discriminating experiment

Use a common modular host, execution harness, tool access, comparable resource budgets, and independent acceptance criteria. Compare an ordinary task-oriented coding team with the added persistent module and contract-evolution protocol. A single-agent baseline on the same host is also useful. Later ablations could separate the effect of curated maintenance context from contract propagation and adoption machinery.

Select a sequence of twenty changes independently of implementation choices. Include presentation changes, new compositions, competing group variants, revised shared meanings, retroactive corrections, failed state transitions, ownership transfer, and retirement. Predict affected scope before each change and record unexpected expansion. Include the attendance → badges → eligibility/rewards → downstream spending chain.

Record the complete cost: worker and ancestor context, growing contract size, user clarification and adoption effort, acceptance failures, migrations, regressions, latency, and ongoing obligations. Separate catalog growth, concurrent workload, and accumulated semantic coupling. Success on one axis does not establish the others.

These are proposed experiments. They were not run, and no numerical target has been selected by Ren.

