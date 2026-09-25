# Soundness assessment — 2026-09-07

Status: AI-authored critical assessment; proposed refinements have not yet been endorsed by Ren. No prototype or benchmark was run for this assessment.

This record preserves Ren’s question verbatim and the assistant’s prepared substantive response. It excludes tool execution, internal reasoning, and progress updates. It supplements the [founding conversation](/Users/ren/theories/theories/evolving-community-swarms/context/2026-09-05-conversation.md); that earlier snapshot remains unchanged.

## Ren

is our idea solid?

## Assistant

**My honest answer: it is a solid research direction, with an important scaling claim still unproven.** I was too quick earlier to say “we can build this” without clearly separating a working prototype from the full promise of a community evolving its software for years.

The strongest part is the combination of **local technical responsibility and local social choice**. People can change their tools, try working alternatives, and adopt them for different audiences while preserving shared records. That is a coherent product mechanism.

The weakest part is our explanation of how that remains inexpensive over time.

**Our central assumption currently contains much of the problem we need to solve.**

We have said that agents can work locally when contracts contain everything their neighbors need. That is a useful condition. But we still need a mechanism that:

- Discovers suitable boundaries.
- Detects requirements missing from existing contracts.
- Revises those contracts without routinely involving the whole system.
- Keeps the contracts small enough for agents to understand.

Otherwise, complexity simply moves from the code into the contracts, their maintainers, or a central coordinator.

**A concrete example exposes the difficulty.**

Suppose the community develops this chain:

```text
Event attendance → volunteer badges → voting eligibility
                                  → wallet rewards → game spending
```

Later, members decide attendance must mean verified participation, and ask to correct earlier false check-ins.

That can affect previously awarded badges, election eligibility, and rewards already spent. The event’s data type could remain identical while its meaning changes. Versioning the code does not settle those consequences.

Good architecture can expose the affected relationships and coordinate the change. It cannot make an inherently shared decision purely local. Our theory needs to predict that wider scope **before implementation**, rather than explain every surprise afterward as “another affected dependency.”

**We also need to separate three kinds of scale.**

| Kind of growth | What we currently know |
|---|---|
| More installed, inactive apps | Lazy loading and isolation give us a credible engineering approach. |
| More simultaneously working agents | Benefits depend on task independence and coordination cost. |
| More years of interconnected features and commitments | This is the largest unanswered question. |

A benchmark with a thousand dormant apps would test the first row. It would provide little evidence for the other two.

Recent evidence supports this distinction. A controlled study of agent architectures reports that coordination can help decomposable tasks and hurt sequential ones. That supports testing the swarm against a strong single-agent baseline rather than assuming more agents help. [Scaling-agent study, revised April 2026](https://arxiv.org/abs/2512.08296v3)

There is also substantial overlap with existing work. Cursor describes recursive planning, narrow worker contexts, shared design decisions, and mechanisms for resolving swarm conflicts. That supports feasibility of some ingredients, but means we should be cautious about claiming the tree architecture itself as original. [Cursor’s engineering report](https://cursor.com/blog/agent-swarm-model-economics)

**The distinctive hypothesis worth pursuing is this:**

> For a defined class of community changes, explicit ownership, maintained contracts, durable local context, and scoped adoption can keep the effort of local changes largely independent of unrelated accumulated functionality—while detecting broader changes early.

That is precise enough to challenge experimentally.

I would test it with twenty successive changes to one small community space, including a semantic change like the attendance example, conflicting preferences, a failed migration, and an abandoned app. Compare local agent coordination with a strong baseline using the same modular platform and comparable resources.

Measure accepted behavior, regressions, human effort, agent cost, contract growth, and unexpected expansion of the change’s scope. Separately measure runtime performance. If the later changes require increasingly global understanding, we have found a failure of the proposed mechanism.

The other major risk is economic: **making features can become cheap while maintaining their shared meaning becomes expensive.** Owners, budgets, and retirement are sensible proposed responses, but we have not yet shown that they control that burden.

I think the idea merits a prototype and serious investigation. The next advance should be a concrete mechanism for maintaining boundaries through change, followed by evidence that it works. I’ve saved this assessment in our [theory folder](/Users/ren/theories/theories/evolving-community-swarms/context/2026-09-07-soundness-assessment.md).

## Evidence and interpretation notes

These notes supplement the response; they are not additional user decisions.

- The scaling-agent paper was checked through the arXiv abstract and version record. Version 3, dated 2026-04-08, reports 260 configurations and six benchmarks. The older Google Research summary describes an earlier 180-configuration study; its figures should not be mixed with the revised abstract. No full-paper methods audit or replication was performed. The results concern the studied configurations, not years of community software evolution.
- Cursor’s July 20, 2026 report was read as a first-party engineering account. It describes recursive task decomposition and additional mechanisms for design conflicts, code collisions, and accumulated errors. It is not independent validation of this theory, and the associated code was not inspected here.
- [Anthropic’s compiler experiment](https://www.anthropic.com/engineering/building-c-compiler), published 2026-02-05, reports substantial work designing verification and restructuring tasks to make parallel progress possible, as well as remaining regressions and limitations. This supports treating verification and decomposition as engineering work. Its comparatively specified compiler task does not establish success for changing community meanings.
- Two bounded independent agent critiques were used to identify counterexamples and missing mechanisms. Their agreement is analytical input, not empirical validation.
- Existing sources on information hiding, assume–guarantee reasoning, dynamic loading, and malleable software remain listed in [SOURCES.md](/Users/ren/theories/theories/evolving-community-swarms/SOURCES.md). This was a focused assessment, not a comprehensive novelty search.

## Proposed refinements to the research method

1. Define the class of supported requests and independently assess whether each result fulfills them.
2. Predict the affected modules and contracts before implementation; record scope expansion as an outcome. Do not make the claim unfalsifiable by reclassifying every surprise after the fact.
3. Track contract size, ancestor context, and coordination work alongside worker context. Local-looking workers must not hide unbounded work elsewhere.
4. Separate runtime catalog scale, active agent concurrency, and accumulated semantic dependencies.
5. Compare the same modular host under a strong single-agent or repository-wide-context baseline and local agent coordination with comparable tools and resource budgets. This tests the contribution of coordination without attributing all modular-host benefits to the swarm.
6. Include unforeseen changes to meanings and shared state, not just additive features or inactive packages.
7. Track human clarification, adoption decisions, support, and ownership transfer as costs, rather than counting code generation alone.

These are recommended tests and revisions. The preserved working direction remains in [DECISIONS.md](/Users/ren/theories/theories/evolving-community-swarms/DECISIONS.md); a request for assessment does not itself establish acceptance of this response.
