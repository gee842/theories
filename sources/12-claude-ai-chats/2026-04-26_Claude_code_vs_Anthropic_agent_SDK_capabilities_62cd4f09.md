# Claude code vs Anthropic agent SDK capabilities

created: 2026-04-26T17:40:27.892318Z  uuid: 62cd4f09-2447-4513-8c79-79d3fc436821  export: new
messages: 4  total_chars: 22739  human_chars: 359


---
**HUMAN** (2026-04-26T17:40):

are there any feature in claude code that you can not get from anthropic agent sdk? can i use code to control as rich as using claude, or even better, with claude doing coding

---
**ASSISTANT** (2026-04-26T17:42):

  The user is asking about the differences between Claude Code and the Agent SDK—specifically what capabilities Claude Code offers that aren't available through the SDK, and whether they can build something equally or more sophisticated using the SDK programmatically. I should check my product knowledge and look up current documentation since both tools are actively evolving. Ren is building OpenClaw and wants to understand what's possible with each approach.
```
This block is not supported on your current device yet.
```

 I need to pull up the documentation for both Claude Code and the Agent SDK to compare their capabilities and understand what features each one offers.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

 I need to check the official documentation to clarify which Claude Code features are only available through the CLI versus the SDK.Let me get the authoritative breakdown from Anthropic's docs on what's CLI-only vs available in the SDK.
```
This block is not supported on your current device yet.
```

 I'm distinguishing between what's available only through the CLI versus what the Agent SDK can access—auto memory with its persistent project directory is strictly CLI-only, and agent teams for coordinating multiple instances appear to be as well.

Beyond those core features, there are several other CLI-specific capabilities: the Python SDK has fewer hook events than TypeScript, slash commands are CLI UI affordances, Plan Mode is an interactive feature tied to the terminal interface, and various integrations like VS Code and JetBrains are specific to Claude Code rather than the SDK itself. The CLI also handles auto-updates and binary distribution, while the SDK requires API key billing since Anthropic restricts third-party developers from offering claude.ai login.

Now looking at what's actually available in both the SDK and Claude Code: the agent loop, all the built-in tools, subagents, skills, CLAUDE.md rules, both filesystem and programmatic hooks, MCP servers, permission controls, context compaction, multi-cloud support, budget controls, and session persistence. The SDK actually has some advantages here—it supports programmatic hooks with callbacks that return structured decisions, in-process custom tools, custom system prompt injection, direct control over messages and streaming, and can be used to build non-coding agents or embed in any application.

For Ren's question about whether they can achieve the same richness programmatically as Claude Code, or even better with Claude doing the coding itself—the answer is yes. The Agent SDK is what powers Claude Code under the hood, so they can build something equally or more capable because they control the entire harness, can implement programmatic hooks that the CLI can't do as cleanly, build any custom UI on top, and compose multiple agents in whatever topology they need. Since Ren is building OpenClaw, they're essentially creating their own version of Claude Code with full control over the architecture.

The real question becomes whether to use the Agent SDK directly or build from scratch, which depends on their specific goals. Let me break down the key differences: Claude Code is a finished product while the Agent SDK is a library—everything Claude Code does is available in the SDK except for some CLI-specific features like auto memory management, agent teams with shared task coordination, the interactive terminal UI with plan mode and slash commands, IDE integrations across VS Code and JetBrains, and Slack integration. The SDK also requires an API key rather than relying on Claude.ai subscription billing.

On the flip side, the SDK offers capabilities beyond Claude Code: programmatic callbacks, in-process custom tools, the ability to build non-coding agents, custom system prompts, direct control over message streaming, and multi-cloud deployment options. For Ren's OpenClaw project specifically, since they're already building their own harness, the Agent SDK essentially serves as a reference implementation—they can either adopt it as a foundation or work directly with the Messages API, but using the SDK gives them the full Claude Code agent loop without reinventing it.

I'm thinking about how to present this clearly for someone technical and bilingual who prefers directness. A compact comparison with maybe one small table showing the gaps, then a straightforward answer to their second question. I should keep the formatting minimal and prose-heavy rather than relying on heavy headers, maybe just a focused list of the CLI-only features since that's really what distinguishes the two.

Drafting the response now: the Agent SDK is essentially the same harness Claude Code runs on, so they get everything except a few CLI-specific UX features. And yes, they can definitely build something more sophisticated on top of it.

The CLI-only features are things like the persistent memory system that stores notes across sessions, agent teams where multiple Claude Code instances coordinate with each other, the interactive UX layer with slash commands and plan mode, the subscription billing tied to claude.ai, and some Python hook events that aren't exposed in the SDK. These are mostly product surfaces rather than core capabilities.

But the SDK actually offers some powerful advantages — structured hook callbacks that can block or transform decisions, custom tools defined directly in application code without needing an MCP server, fine-grained control over the message stream and system prompt, per-session cost caps, and multi-cloud support across different providers. So for the original question, the answer is yes — the SDK is genuinely richer in certain ways.

The real tradeoff is that you're building the user-facing surfaces yourself: no terminal UI, no slash commands, no plan mode unless you implement them. Since OpenClaw is your own harness anyway, you've got two paths forward — either wrap the SDK's `query()` method and agent options into your SST architecture to inherit the loop, tool execution, and hook lifecycle for free, or skip it entirely and build directly on the Messages API for complete control, though you'd lose the built-in plumbing.

For OpenClaw, the key question is whether the SDK's agent loop actually fits what you need for SST, or whether your harness should own that loop entirely. Since the SDK exposes programmatic hooks, custom tools, and message-level control, you can probably stay on it and only drop down to the Messages API when a specific abstraction gets in your way. I'm identifying the source documents for each claim so I can cite them properly—the web fetch gave me one set of results, and the searches provided others. I'll focus on the strongest evidence for the key differences between CLI and SDK capabilities, then write a concise response that's direct and useful for someone building with OpenClaw.Short answer: the Agent SDK is the same harness Claude Code is built on. You get everything except a small set of CLI-only UX features — and you can actually build something richer.

**What's genuinely CLI-only (not available in the Agent SDK):**

- **Auto-memory** — the `~/.claude/projects/<project>/memory/` notes Claude Code persists across interactive sessions. This is explicitly a CLI-only feature that is never loaded by the SDK. (CLAUDE.md and `.claude/rules/*.md` *are* available via `settingSources`.)
- **Agent teams** — multiple Claude Code instances sharing a task list and messaging each other directly. Agent teams are a CLI feature where one session acts as the team lead, coordinating work across independent teammates, and are not directly configured via SDK options. Regular subagents (ephemeral, isolated, return summary to parent) work fine in the SDK.
- **Interactive UX surfaces** — slash commands, plan mode, terminal rendering with live diffs, IDE integrations (VS Code, JetBrains, Xcode), Slack. Product surfaces, not capabilities.
- **Claude.ai subscription billing** — Anthropic does not allow third party developers to offer claude.ai login or rate limits for products built on the Agent SDK; you must use API key authentication.
- **A few hook events in Python only** — SessionStart, SessionEnd, TeammateIdle, and TaskCompleted exist in the TypeScript SDK but not Python.

That's the entire gap.

**What's actually *richer* in the SDK than in Claude Code:**

- **Programmatic hook callbacks** that return structured decisions (`{"decision": "block", "reason": "..."}`, transform, audit). Much more expressive than shell-script filesystem hooks, and they run in-process.
- **In-process custom tools** defined in your application code — no MCP server boundary needed.
- **Direct control over the message stream, system prompt injection, context compaction**, and per-session cost caps via `max_budget_usd`.
- **Multi-cloud out of the box** — Bedrock, Vertex AI, Azure Foundry by env var.
- Build non-coding agents — you're not pinned to coding workflows.

**For your OpenClaw question specifically:** the SDK essentially *is* the reference harness. Two real paths:

1. **Build SST on top of `query()` / `ClaudeAgentOptions`.** You inherit the agent loop, tool execution, context compaction, hook lifecycle, and skills/CLAUDE.md loading. Your Sprite-Space-Token layer sits above it. Fastest to ship; you only own the parts that are actually novel.
2. **Drop to the Messages API directly.** You give up the loop and tool plumbing but own every byte — useful if SST's incremental output / harness semantics diverge enough that the SDK becomes friction rather than scaffolding.

The deciding question is whether the SDK's agent loop matches the loop you want OpenClaw to have. The fact that it exposes programmatic hooks, custom in-process tools, system prompt control, and message-level streaming means you can probably stay on it and only drop down where a specific abstraction actively blocks you.

Sources: [Agent SDK overview](https://platform.claude.com/docs/en/agent-sdk/overview), [Use Claude Code features in the SDK](https://platform.claude.com/docs/en/agent-sdk/claude-code-features).

---
**HUMAN** (2026-04-26T17:50):

how's typing -> enter -> execute -> context management-> next round of typing equivalent claude code in agent sdk? to what extend can they be customized?  how about context management?

---
**ASSISTANT** (2026-04-26T17:52):

  Ren's asking about the mechanics of how the interactive turn loop works in the Agent SDK—specifically how the type-enter-execute-context cycle maps over, how much control they have to customize it, and the details of context management. This is foundational for their OpenClaw harness design, so they need the actual implementation details, not just high-level concepts.

I need to dig into the docs on sessions, the agent loop mechanics, context compaction strategies, streaming input mode as the interactive equivalent, and the lifecycle hooks available—things like `query()` being one-shot versus sessions for multi-turn, session resumption via IDs, the CompactBoundary mechanism, and permission callbacks that let them intercept the flow.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

 I'm diving deeper into how context management and compaction work to understand the mechanisms better.
```
This block is not supported on your current device yet.
```

 I need to pull up the agent loop and context management documentation, specifically the agent-loop page and the compaction details.
```
This block is not supported on your current device yet.
```

 Now I'm pulling together everything to address Ren's question about how the interactive typing-execute loop works in Claude Code versus the Agent SDK, what customization options exist, and how context gets managed across turns.

The core flow maps pretty directly: your input goes through `query()` for single interactions or streaming input mode for more control, the agent's internal loop handles evaluation and tool execution automatically, and context management happens through automatic compaction with `compact_boundary` markers that you can also trigger manually.

Sessions persist state across interactions—either automatically through `ClaudeSDKClient` or by capturing and resuming a `session_id`, with everything stored in the project directory. The key difference from the CLI is that the SDK's inner loop runs continuously without yielding until the model finishes, hits a turn/budget limit, or an `AskUserQuestion` interrupts it.

Every stage of this flow is customizable—streaming input lets you interrupt and inject mid-loop, hooks like `UserPromptSubmit` fire at specific points to inject context, and the execution loop itself can be shaped through various configuration options. ction, archive transcript) — I can manually trigger compaction or do it via prompt, and there's a PreCompact hook that runs before this happens. I'm also considering ToolSearch for loading tool schemas on-demand rather than preloading everything, plus file checkpointing to capture filesystem snapshots.

For output, I need StreamEvent for live deltas, structured outputs, and a Stop hook that fires after completion. On the session side, I can continue from the most recent context, resume by session_id, or fork into a new branch — with optional ephemeral sessions that don't persist. There are commands to list sessions, retrieve messages, rename, and tag them, with session files stored in ~/.claude/projects/<encoded-cwd>/*.jsonl.

Now I'm thinking through context management specifically... I see that persistent rules should live in CLAUDE.md rather than the initial prompt since compaction can drop that content, and I can use subagents for isolated context or ToolSearch for dynamic tool loading when needed. For Ren's OpenClaw SDK, it mirrors Claude Code's flow but through a generator pattern where I yield messages and the query loop handles the interaction cycle.

Now I'm mapping how the SDK's customization works — the Sprite/Space/Token model aligns with execution contexts, tool environments, and data flow, where I can intercept at each stage with typed callbacks instead of shell hooks. Since Ren's asking layered technical questions, I should structure the response clearly while keeping it readable.

I'll use the four-stage frame they introduced and aim for a similar length to my previous answer — comprehensive but focused, with bullets only where they genuinely help (like listing customization options). I need to cite the key facts from the docs.Mapping your four stages to the SDK, then the customization surface for each:

## type → enter

In Claude Code interactive, you type and hit return. In the SDK there are four ways to do this depending on how interactive you need:

- **One-shot:** `query(prompt="...")` — single prompt, runs the loop, returns. No follow-up context.
- **Multi-turn in one process (Python):** `ClaudeSDKClient` as an async context manager. Each call to client.query() automatically continues the same session, with no ID handling required.
- **Multi-turn in one process (TypeScript):** pass `continue: true` on each `query()` call — the SDK picks up the most recent session in the current directory.
- **Streaming input mode (the rich one):** pass an async generator as `prompt`. It allows the agent to operate as a long lived process that takes in user input, handles interruptions, surfaces permission requests, and handles session management. This is what you'd build a chat UI on top of, and what lets you inject images mid-conversation, respond to `AskUserQuestion`, or interrupt the agent.

The TypeScript V2 preview adds `createSession()` with separate `send()`/`stream()` that's closer in feel to Python's client.

## execute

This is the inner agent loop, and the key thing to internalize: **one `query()` call runs as many turns as needed without yielding control to your code**. Within a single query() call, the agent already takes as many turns as it needs, and permission prompts and AskUserQuestion are handled in-loop — they don't end the call.

The cycle inside one call: SystemMessage init → AssistantMessage with tool calls → SDK executes tools → results feed back to Claude → repeat until Claude produces text with no tool calls → AssistantMessage final → ResultMessage. Each round-trip is a "turn." Customization knobs on this loop:

- **`max_turns` / `max_budget_usd`** — hard stops that return error subtypes you can resume from
- **`effort: low|medium|high|max`** — reasoning depth per turn (TypeScript defaults to high, Python defers to model)
- **`permission_mode`** — `default` (callback approves), `acceptEdits` (auto-approve edits), `plan` (no execution, planning only), `dontAsk`, `bypassPermissions`
- **`allowed_tools` / `disallowed_tools`** with rule scoping like `"Bash(npm:*)"` for command-level allow lists
- **`canUseTool` callback** — in-process per-tool approval, can transform inputs before execution
- **Hooks at every lifecycle point** — `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `SubagentStart`/`Stop`, `PreCompact`. Hooks run in your process, return structured `{decision: "block", reason: "..."}` decisions, and don't consume context window
- **Custom in-process tools** — defined in your application, no MCP boundary
- **MCP servers + ToolSearch** — load tool schemas on-demand instead of preloading
- **Subagents** via the `agents` parameter — isolated fresh-context delegations
- **`include_partial_messages`** — token-by-token `StreamEvent` deltas for live UI

So you can customize at the granularity of: which prompts, what reasoning depth, which tools, which inputs to those tools, what to do with results, and when to stop.

## context management

This is where most harness designers get burned, so worth being precise. From the agent loop docs:

The context window does not reset between turns within a session. Everything accumulates: the system prompt, tool definitions, conversation history, tool inputs, and tool outputs. Content that stays the same across turns (system prompt, tool definitions, CLAUDE.md) is automatically prompt cached.

When the window approaches its limit, the SDK automatically compacts the conversation: it summarizes older history to free space, keeping your most recent exchanges and key decisions intact, and emits a SystemMessage with subtype "compact_boundary" in the stream.

The customization surface for context:

- **`setting_sources=["user", "project", "local"]`** — loads CLAUDE.md, `.claude/rules/*.md`, skills, hooks, settings.json. Without this, the SDK runs in isolation mode with only what you pass programmatically.
- **`system_prompt` / `systemPromptModification`** — inject directly without CLAUDE.md, or layer on top of Claude Code's default system prompt.
- **CLAUDE.md is re-injected every request** (then prompt-cached). This is the one critical detail: compaction replaces older messages with a summary, so specific instructions from early in the conversation may not be preserved. Persistent rules belong in CLAUDE.md rather than in the initial prompt, because CLAUDE.md content is re-injected on every request. If you put rules only in the initial prompt, compaction may eat them.
- **`PreCompact` hook** — runs before compaction, receives a `trigger` field (`manual` vs `auto`). Use it to archive the full transcript or inject custom summarization context.
- **Compaction summary instructions in CLAUDE.md** — the compactor reads CLAUDE.md like any other context, so you can include a section telling it what to preserve.
- **Manual `/compact`** — sent as a prompt string, triggers compaction on demand. Slash commands sent this way are SDK inputs, not CLI-only.
- **Subagents for context isolation** — each subagent gets a fresh conversation (no parent message history); only its final response returns to the parent as a tool result. The main agent's context grows by the summary, not the full subtask transcript. This is the most powerful context-management primitive in the SDK.
- **`ToolSearch` / MCP tool search** — load tool schemas on-demand instead of preloading every server's full toolset.
- **`max_thinking_tokens`** — caps extended thinking budget per turn.

## next round of typing

This is sessions. A session is the conversation history the SDK accumulates while your agent works. It contains your prompt, every tool call the agent made, every tool result, and every response. The SDK writes it to disk automatically at `~/.claude/projects/<encoded-cwd>/*.jsonl`.

Three primitives:
- **Continue** — most recent session in current directory, no ID tracking
- **Resume** — pass a captured `session_id`, picks up that specific session
- **Fork** — `fork_session=True` with `resume=id` creates a new branch from history; original stays unchanged. Forking branches the conversation history, not the filesystem — if a forked agent edits files, those changes are real and visible to any session working in the same directory. Pair with file checkpointing if you want filesystem branching too.

`list_sessions()`, `get_session_messages()`, `rename_session()`, `tag_session()` give you full programmatic access to the session store. TypeScript also has `persistSession: false` for stateless ephemeral mode (Python always persists).

## the practical takeaway for OpenClaw

The customization surface is essentially complete: every transition point in your four-stage cycle has a typed callback or option. What the SDK *doesn't* let you customize is the inner agent loop's control flow itself — between turns, you don't get a yield point unless a hook fires, the loop completes, or AskUserQuestion triggers. If your SST design needs the harness to take control mid-loop on its own initiative (not in response to a tool call or user input), you'd need to either drive it through hooks or drop to the Messages API and own the loop yourself.

For the streaming-input pattern with `ClaudeSDKClient` plus `setting_sources=["user", "project", "local"]`, hooks for SST instrumentation, and subagents for context isolation — that's basically a Claude Code-grade interactive harness with your own UI and orchestration on top.

Sources: [How the agent loop works](https://platform.claude.com/docs/en/agent-sdk/agent-loop), [Work with sessions](https://platform.claude.com/docs/en/agent-sdk/sessions), [Streaming Input](https://platform.claude.com/docs/en/agent-sdk/streaming-vs-single-mode).
