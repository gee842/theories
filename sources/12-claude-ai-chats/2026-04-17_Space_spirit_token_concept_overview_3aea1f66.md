# Space spirit token concept overview

created: 2026-04-17T10:33:48.012112Z  uuid: 3aea1f66-6fe4-42e5-a8bc-40e0b7002e59  export: new
messages: 2  total_chars: 3955  human_chars: 83

summary: **Conversation Overview**

The person asked Claude to explain their "Space Spirit Token" idea in full detail for use as context by a Claude Code agent. Claude retrieved relevant prior context from memory and produced a comprehensive technical reference document covering the SST (Spirit/Space/Token) architecture — a capability-based protocol for social systems, agent ecosystems, and miniapp platforms built around three core primitives.

The conversation was entirely technical in nature, focused on producing a standalone markdown file (`SST.md`) that a Claude Code agent could read directly. Claude synthesized the architecture from prior conversations, noting a naming convention clarification: "Sprite" appears in the v0.1 spec and legacy code, while "Spirit" is the preferred public-facing term the person uses conversationally. The document covers the three primitives (Spirit as identity, Space as container, Token as typed relational edge), their recursive loop relationship, capability-first/UCAN-style auth, schema and hook DSL design, lazy cascading lifecycle via bindings, a privacy-first visibility model, the token-as-edge architectural insight, embedded Spirits in Tokens, prototypal inheritance via extension Tokens, a FUSE filesystem mapping where Space=directory and Token=file enabling Unix toolchain compatibility, a worked example using a community system, design discipline warnings against using Tokens as content stores, and open questions for future versions. The document also captures the "mycological composition" pattern where agents wire themselves via local hook files without a central orchestrator.

Claude flagged one open design question directly to the person: whether `token.agents[]` should be a dedicated field (as recommended in prior conversation) or kept inside the payload, noting the agent should not generate code assuming the field exists until that decision is settled. The file was written to `/home/claude/SST.md` and copied to outputs.


---
**HUMAN** (2026-04-17T10:33):

explain my space spirit token idea in full for my claude code agent to have context

---
**ASSISTANT** (2026-04-17T10:36):

  I'm checking my memory for context on what the user means by "space spirit token" — it looks like they're referring to the SST architecture from OpenClaw, an AI agent framework that uses Sprite-Space-Token primitives, though the thought cuts off before I can confirm the exact terminology.
```
This block is not supported on your current device yet.
```

 I'm seeing the naming confusion around this concept — the user has been referring to it as "Space Spirit Token," but the formal spec calls it "Sprite Space Token" or SST, and they want to ensure "spirit" is properly defined in the API design even though it's technically just a special space.
```
This block is not supported on your current device yet.
```

 I've got a solid understanding of the SST architecture now, so I'm ready to write up a clear explanation for the Claude Code agent that covers the fundamentals—what Spirit, Space, and Token represent—along with the naming conventions and how the recursive structure works, plus the key design principles that drive the whole system. I'm settling on "Spirit" as the primary term since that's what the user has been using in recent conversations, though I'll note that the original spec called it "Sprite." Now I need to structure this comprehensive markdown document for the agent—starting with a clear overview, then the three core primitives, the recursive architecture, capability-first design principles, schemas and hooks, the token-as-edge insight, visibility model, filesystem mapping, agent-native properties, a worked example, design decisions, and open questions for future versions.I'll put this together as a context file your Claude Code agent can read directly. Pulling from the v0.1 spec, the FUSE filesystem mapping work, and the architectural decisions you made along the way.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Drop this in your repo as `SST.md` (or `docs/SST.md`, or paste into `CLAUDE.md` if you want it loaded automatically). Sixteen sections, covers everything from the three primitives through the FUSE realization to the convention-layer discipline.

A few notes on the choices I made writing this:

**On naming.** I led with "Spirit" as the public term and flagged "Sprite" as the legacy spec/code name. You went back and forth on this — in the v0.1 spec it was Sprite, but in conversation and later filesystem work you consistently said Spirit. If your agent encounters both in the codebase, this should keep it from getting confused.

**What I left in.** The full design rationale (why three not two or four, why lazy bindings, why traits not inheritance), because an agent making changes needs to know *why* the model is shaped this way to avoid breaking it accidentally. Also the discipline section — that "without conventions this degrades into a schemaless blob store" warning is the single most load-bearing thing for an agent that might generate new schemas casually.

**What I left out.** The full hook DSL operator list and the §16 worked example from the spec doc — those are reference material, not orientation. If your agent needs them, point it at the actual `spec.md`. This file is the "model of the model" that lets an agent reason about the system; the spec is what it consults for exact API shapes.

**One thing worth deciding.** Section 9 introduces `token.agents[]` as a separate field from `token.holder` to distinguish "Spirits with agency within the Token" from "Spirit holding the capability." That was a recommendation in the original conversation, not a settled spec decision. If you've decided to keep them in `payload` instead, edit that section before handing this to an agent — otherwise it'll start writing code assuming the field exists.
