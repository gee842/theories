# Flexible alternatives to agent-generated UI libraries

created: 2026-03-16T08:49:15.985319Z  uuid: a8a3f22e-4e33-44a4-a908-a27e693d1575  export: old
messages: 4  total_chars: 12471  human_chars: 216

summary: **Conversation Overview**

The person asked Claude to research and explain current paradigms for agent-generated UI (where AI agents dynamically generate user interface components), citing a2ui as a known example they found too rigid. Claude provided a structured overview of the emerging landscape, covering AG-UI/CopilotKit, MCP Apps, Thesys C1/OpenUI, and Open-JSON-UI, explaining how these technologies function as complementary layers rather than competing alternatives. Claude organized them along a spectrum from constrained/declarative approaches (A2UI, Open-JSON-UI) to more open-ended ones (MCP Apps, CopilotKit with custom React components).

The person then asked for a deeper, more practical assessment including real developer experiences and community sentiment. Claude conducted additional web research and synthesized findings into a tiered practical ranking. The most battle-tested options identified were Vercel AI SDK with assistant-ui and CopilotKit with AG-UI, followed by MCP Apps and Thesys C1 as promising but earlier-stage. Claude noted that most available content is vendor-authored rather than independent, flagged specific limitations of each approach (e.g., CopilotKit's backend runtime requirement, Thesys's managed-service lock-in, MCP's historically rough developer experience), and provided tailored recommendations based on the person's apparent context of building AI-embedded hardware products and community infrastructure. Claude closed with a meta-observation that the more interesting design question for edge devices and community platforms may be whether the "agent generates UI" paradigm itself is the right model, versus a lightweight local agent protocol for minimal displays.

Domain-specific terminology used throughout includes: AG-UI, A2UI, MCP (Model Context Protocol), MCP Apps, generative UI, controlled generative UI, declarative UI spec, SSE/WebSockets, Zod schemas, LangGraph, CrewAI, Pydantic AI, A2A (agent-to-agent), and sandboxed iframes.


---
**HUMAN** (2026-03-16T08:49):

find me a few latest paradigms to use agent generate ui, for example, a2ui is such a library, but I feel it is too rigid

---
**ASSISTANT** (2026-03-16T08:50):

The user is asking about latest paradigms/libraries for agent-generated UI (where AI agents dynamically generate UI components). They mention a2ui as an example but find it too rigid. Let me search for current approaches and libraries in this space.
```
This block is not supported on your current device yet.
```

Good, I have a solid picture now. Let me also search for more on the specific alternatives like AG-UI, MCP Apps, Open-JSON-UI, and assistant-ui.
```
This block is not supported on your current device yet.
```

Now let me search for MCP Apps and Open-JSON-UI to complete the picture.
```
This block is not supported on your current device yet.
```

Now I have a comprehensive picture. Let me also quickly search for Thesys/Crayon and assistant-ui to round things out.
```
This block is not supported on your current device yet.
```

Now I have a comprehensive picture of the landscape. Let me synthesize this for Ren.Great question, Ren. This space has exploded recently — there's now a clear emerging stack with distinct layers. Here's how the current paradigms break down, roughly from "most constrained" to "most open-ended":

**1. CopilotKit + AG-UI (Agent-User Interaction Protocol)**

AG-UI is an open, event-based protocol from CopilotKit that standardizes how AI agent backends connect to user-facing frontends. Think of it as the **transport/runtime layer** — it doesn't define *what* the UI looks like, it defines how agent state, UI intents, and user interactions flow bidirectionally in real-time over SSE/WebSockets/HTTP. It complements MCP (agent-to-tool) and A2A (agent-to-agent) by handling the agent-to-user connection specifically. CopilotKit builds on this with React hooks like `useFrontendTool` where you pre-register components and the agent picks which to render. This is the **"controlled generative UI"** pattern — you own the components, the agent just orchestrates them. Much more flexible than A2UI because you're writing real React, not working within a JSON schema.

**2. MCP Apps (the official MCP extension)**

MCP Apps let tools return rich, interactive interfaces instead of plain text — dashboards, forms, visualizations — that render directly in the conversation via sandboxed iframes. This is now the **first official MCP extension**, co-developed by Anthropic, OpenAI, and the MCP-UI community. Tools declare a `ui://` resource, and the host renders it as interactive HTML inside a sandboxed iframe with bidirectional data flow via JSON-RPC postMessage. The key advantage: build an MCP App once and it works across Claude, ChatGPT, VS Code Copilot, Goose, and other compliant hosts. This is the **most open-ended** approach — you ship actual HTML/JS/CSS, not a constrained schema. It's basically "embed a mini web app in the chat."

**3. Thesys C1 / OpenUI**

Thesys offers a managed generative UI API where the LLM generates interactive interfaces at runtime — cards, tables, forms, charts — tailored to each user and situation. They recently open-sourced **OpenUI**, a compact rendering spec that replaces verbose JSON with a more code-like format to reduce tokens and improve reliability. The approach: you call their API, the LLM outputs structured UI specs, their renderer (Crayon component library) handles the rest. Their Agent Builder lets you build AI agents that respond with UI instead of text. This is the fastest path from zero to working demo, but it's a managed service with its own opinions.

**4. Open-JSON-UI**

This is an open standardization of OpenAI's internal declarative generative UI schema. It sits alongside A2UI as a "declarative" spec — agent outputs structured JSON describing cards/lists/forms, the frontend interprets and renders it. Less rigid than A2UI's JSONL format, and more closely aligned with how OpenAI's own products handle it.

**How they relate (the emerging stack)**

These aren't competing technologies — they're layers. AG-UI handles the runtime streaming/state sync, A2UI or Open-JSON-UI provide the declarative UI spec, MCP Apps provide HTML templates for tools, and MCP handles the tool layer underneath.

Given your frustration with A2UI's rigidity, the most interesting directions for you are probably:

- **MCP Apps** if you want maximum freedom (you're writing real HTML/JS) and cross-platform portability across Claude/ChatGPT/etc.
- **CopilotKit + AG-UI** if you're building a React app and want the agent to orchestrate your own custom components with real-time streaming
- **Thesys OpenUI** if you want the fastest prototyping path with a managed service

The philosophical split is between "agent emits a structured schema, client renders natively" (A2UI, Open-JSON-UI) vs. "agent emits actual executable UI" (MCP Apps, CopilotKit controlled pattern). The latter gives you far more expressiveness at the cost of more security concerns (hence the sandboxed iframes in MCP Apps).

---
**HUMAN** (2026-03-16T08:53):

what is the best/practical approaches? how's people's experience with them? do a research for me

---
**ASSISTANT** (2026-03-16T08:55):

The user wants a deeper dive into practical experiences, real-world usage, and community sentiment around these generative UI approaches. Let me do more targeted research.
```
This block is not supported on your current device yet.
```

Let me search for more practical developer experiences and comparisons.
```
This block is not supported on your current device yet.
```

Let me search for more real developer experiences, Reddit/HN discussions, and practical comparisons.
```
This block is not supported on your current device yet.
```

Let me search for more hands-on developer experiences, Reddit discussions, and community feedback about these tools.
```
This block is not supported on your current device yet.
```

Let me search for more critical/honest takes and community discussions.
```
This block is not supported on your current device yet.
```

Now I have enough information to give Ren a comprehensive, practical assessment. Let me synthesize the key findings.OK Ren, here's my synthesis after digging through a lot of material. I'll cut through the marketing and give you the practical landscape.

---

## The Real Picture

The honest truth is that most of the content out there is written by the framework authors themselves (CopilotKit's blog is 90% of the AG-UI discourse, Thesys writes most of the OpenUI content, etc.), so genuine independent developer feedback is thin. That said, here's what I can piece together:

### Tier 1: Most battle-tested and practical right now

**Vercel AI SDK + assistant-ui** — This is the quiet workhorse that most production apps are actually built on. The Vercel AI SDK has over 20 million monthly downloads, and assistant-ui (YC W25) has become the most popular UI library for AI chat with 50k+ monthly downloads. The generative UI approach here is straightforward: you define tools with Zod schemas, and each tool maps to a React component that renders when the LLM calls it. Tool results render as custom React components instead of generic tool displays — you get loading states, streaming partial results, and error handling built in. This is the "controlled" pattern and it just works. The tradeoff: you pre-define every UI component. The agent picks which to show, but can't invent new ones.

**CopilotKit + AG-UI** — This is the most ambitious framework and has real traction. AG-UI crossed 9,000 GitHub stars and hit 120,000 weekly installs, with CopilotKit surpassing 2 million agent-user interactions per week. It has first-party integrations with LangGraph, CrewAI, Pydantic AI, and Microsoft Agent Framework. The key differentiator: it supports all three generative UI patterns (controlled, declarative, open-ended) through a single protocol, and there's now a Kotlin SDK for native mobile (Android/iOS/JVM) too. The practical concern: CopilotKit currently assumes agents run in a backend via `runtimeUrl`, so a fully frontend-only setup isn't straightforward — developers have been asking for client-side-only AG-UI support without the CopilotKit backend runtime.

### Tier 2: Promising but earlier-stage or more specialized

**MCP Apps** — This is conceptually the most exciting and has the strongest institutional backing (Anthropic + OpenAI + community). Tools can now return interactive HTML that renders directly in conversation — dashboards, forms, visualizations — as the first official MCP extension. It's supported by Claude, Claude Desktop, VS Code Copilot, Goose, and ChatGPT. But the developer experience still has rough edges. MCP in general has a reputation problem — cryptic error messages, complex setup with node/uv, and limited testing options. The developer experience really matters, and historically the standards that win aren't necessarily the strongest technically — they're the easiest to use. If MCP has a reputation problem right now, it's because many people met it in its worst form: huge always-on tool catalogs, flaky servers, and awkward client UX. MCP Apps specifically is better than raw MCP in this regard — you're writing HTML that gets sandboxed in iframes — but it's still young. Best for: building tools that need to work across Claude/ChatGPT/VS Code without per-host code.

**Thesys C1 / OpenUI** — The fastest path from zero to working demo. Developers report getting up and running in minutes — uploading inventory, configuring goals, and having a functional agent with interactive UI. OpenUI Lang is up to 67% more token-efficient than equivalent JSON formats — they benchmarked against Vercel and their own C1 JSON format across seven scenarios. The catch: it's a managed API (you call their endpoint instead of OpenAI/Anthropic directly), and the model outputs structured UI specs rather than code — if you ask it to build a portfolio, it gives you the interface without underlying code, because they view LLM-generated code as unreliable. This philosophy means you can't extract and own what it generates. Also, one developer asked pointedly: "So what's the end goal of thesys? Just generate UI-based answers so users can interact with it?" — which gets at the philosophical limit.

**A2UI (Google)** — You already know this one feels rigid, and you're right. It's at v0.8 with early client libraries for Flutter, Web Components, and Angular. The sweet spot is cross-platform portability — the same JSONL spec renders natively on web, mobile, and desktop. In practice, implementing A2UI involves putting JSON examples directly in the system prompt so the LLM learns the envelope format — it's template-heavy and the agent can't easily go beyond the predefined component set. Best for: multi-platform A2A (agent-to-agent) flows where a remote sub-agent needs to send UI to a host app in a safe, framework-agnostic way.

### My practical recommendation for your situation

Given that you're building AI-embedded hardware products and community infrastructure — not a typical SaaS dashboard — here's how I'd think about it:

**If you need an agent chat interface in a web/mobile app** → Start with **Vercel AI SDK** (or CopilotKit if you want more agentic features like shared state and human-in-the-loop). These are the most production-proven.

**If you're building tools that need to surface UI inside Claude/ChatGPT/VS Code** → **MCP Apps** is the right bet despite the DX roughness, because the cross-host portability is uniquely valuable.

**If you want maximum flexibility and don't mind complexity** → CopilotKit as the runtime + whatever UI spec (A2UI for declarative, MCP Apps for open-ended) fits the use case. CopilotKit thinks the future is composable: an agent might use MCP to call tools, A2UI to describe UI, and AG-UI to push updates to the frontend.

**If you want rapid prototyping** → Thesys C1 to validate concepts fast, then migrate to something you own.

The real meta-insight: the model intelligence has become a commodity — the real competitive advantage lies in the SDKs and protocols that connect that brain to the real world. For your hardware + community work, the interesting question isn't which framework to use, it's whether the "agent generates UI" paradigm itself is the right model for edge devices and community platforms, or whether you need something more like a local agent that speaks a lightweight protocol to a minimal display. That's a different design space than what any of these frameworks are optimizing for.
