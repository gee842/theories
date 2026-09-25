# Sources and provenance

Established 2026-09-05. AI-authored source notes. These are references consulted during the founding conversation, not a systematic literature review. Links identify the original sources; this folder does not reproduce their full text.

## Primary conversation

- [Local founding archive](context/2026-09-05-conversation.md): five Ren messages, four substantive assistant responses, and earlier visible progress updates, in order. The archive ends at the request to create this folder.
- [Corpus source snapshot](../../sources/15-codex-theory-conversations/2026-09-05-evolving-community-swarms.md): identical founding copy, preserved under the workspace’s sources convention.
- Task ID: `01a07146-7e6d-7093-86bf-f948610c370a`. Original task title at capture: “Design code workflows for swarms”.
- Authorship: Ren’s messages are primary statements of intent and examples. Assistant responses are proposals and synthesis. The final user message explicitly aligns with the direction; it does not establish empirical validation.

## Contract reasoning and decomposition

### David L. Parnas — On the Criteria To Be Used in Decomposing Systems into Modules (1972)

[Paper text hosted by Lafayette College](https://www.cs.lafayette.edu/~gexia/cs301/resources/parnas.html).

Supports decomposition around information hiding and design decisions that can be encapsulated. It supplies a foundation for choosing module boundaries; it does not establish an optimal partitioning algorithm for LLM swarms. The hosted text identifies itself as a digitized copy and warns that transcription accuracy is not guaranteed.

### Pacti — Getting Started

[Official project documentation](https://www.pacti.org/docs/getting_started/).

Explains assumptions and guarantees, composition, refinement, and deriving requirements for missing components. Useful for making the local-to-global reasoning obligation concrete. Its examples and supported formalisms do not prove arbitrary generated software correct or decide unrestricted natural-language behavioral equivalence.

### Ioannis Filippidis and Richard M. Murray — Layering Assume-Guarantee Contracts for Hierarchical System Design (2018)

[Caltech author repository](https://authors.library.caltech.edu/records/r6eba-5m902).

The repository abstract describes hierarchical specification decomposition and hiding variables while preserving realizability under the paper’s formal setting. The abstract and repository record were consulted; the full paper was not reviewed in this discussion. It is a promising next reading, not an already-applied theorem about this proposal.

## Runtime building blocks

### React — lazy

[Official documentation](https://react.dev/reference/react/lazy).

Documents deferring a component’s code loading until first rendering, with loading and failure handling. Supports the feasibility of on-demand loading. It does not supply code generation, general isolation, module governance, or semantic validation.

### webpack — Module Federation

[Official documentation](https://webpack.js.org/concepts/module-federation/).

Describes combining separately built modules into an application and loading remote modules at runtime. It is evidence for an available implementation primitive, not a decision to use webpack or proof of the overall architecture’s performance.

### Visual Studio Code — Activation Events

[Official extension API documentation](https://code.visualstudio.com/api/references/activation-events).

Shows extensions activating in response to relevant events. Supports the adaptive-IDE example’s activation mechanism. Automatic synthesis and verification of new extensions are additional proposed capabilities.

### Codex — Git worktrees

[Official documentation](https://learn.chatgpt.com/docs/environments/git-worktrees).

Consulted for the initial operational discussion about agents working on isolated changes. This reference is historical context for exchange 1. Ren subsequently clarified that the theory should be considered independently of the current harness; Codex worktrees are not a requirement of the proposed system.

## Malleable and community-created software

### Geoffrey Litt, Josh Horowitz, Peter van Hardenberg, Todd Matthews — Malleable Software (June 2025)

[Ink & Switch essay](https://www.inkandswitch.com/essay/malleable-software/).

Articulates software people can reshape at the point of use, compose, and create communally. Closely relevant to the social and product vision. The essay’s vision and prototypes do not establish the complete autonomous, indefinitely evolving swarm proposed here.

### Potluck — Dynamic documents as personal software

[Ink & Switch project essay](https://www.inkandswitch.com/potluck/).

Describes a research prototype for gradually enriching text documents into interactive tools. Useful for thinking about a gentle transition from using a community space to changing it. It does not demonstrate the community’s full wallet/voting/agent ecosystem or long-term bounded maintenance cost.

## Additional sources consulted for the 2026-09-07 assessment

- [Towards a Science of Scaling Agent Systems, arXiv v3](https://arxiv.org/abs/2512.08296v3): abstract and version history checked. Reports task-dependent outcomes from different coordination architectures. The revised abstract, rather than older summary figures, informs the assessment; full methods were not audited.
- [Cursor: Agent swarms and the new model economics](https://cursor.com/blog/agent-swarm-model-economics): first-party report dated July 20, 2026 on recursive coordination and practical failure handling. Relevant prior art and engineering evidence, not independent validation of the community proposal.
- [Anthropic: Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/engineering/building-c-compiler): first-party experiment dated February 5, 2026. Relevant to the work required for verification and useful parallelism; not a test of community evolution.

Interpretive limits and the resulting proposed tests are retained in the [dated assessment](context/2026-09-07-soundness-assessment.md). No numerical result from those sources is represented as a benchmark of this project.

## Harness and swarm comparison — 2026-09-07

The [dated comparison](context/2026-09-07-harness-and-swarm-comparison.md) contains the primary-source links and evidence notes for Codex, Claude Code teams, OpenHands, LangGraph, Cursor, Gas Town, MetaGPT, ChatDev, MacNet, Darwin Gödel Machine, SICA, Webstrates, and Varv. It also updates the scope of reading for the scaling study: selected v3 methods and limitations were inspected in this later comparison, beyond the abstract-level reading recorded above. No results were replicated.

The record distinguishes framework capabilities, design documents with planned features, first-party experiments, papers, and our interpretation. It supports a proposed research focus on contract/state/adoption evolution; it does not establish novelty or comparative performance. Ren’s exact request and the substantive assistant response are preserved there, with an identical [corpus source snapshot](../../sources/15-codex-theory-conversations/2026-09-07-evolving-community-swarms-comparison.md).

## Updated vision — 2026-09-07

The [new source notes](next-vision/SOURCES.md) add primary abstract/version records for ADAS v2, AFlow v4 and ACE v3. They establish precedents for adaptive agent designs, workflow search and evolving context; full methods were not audited in this turn. The [updated-vision context record](context/2026-09-07-updated-vision.md) preserves Ren’s explicit competitive direction and a complete snapshot of the resulting assistant-authored planning package. An identical [corpus snapshot](../../sources/15-codex-theory-conversations/2026-09-07-evolving-community-swarms-next-vision.md) is retained.

## Corpus connections to investigate

The workspace already contains theories about context runtimes, spirit/space/token and Yi, Wamotopia, and cooperative infrastructure. README.md links to them. Only workspace orientation and an initial portion of the context-runtime synthesis were inspected while setting up this folder. No comprehensive comparison or reconciliation has been performed. These connections should be investigated from their original sources before claiming equivalence or lineage.
