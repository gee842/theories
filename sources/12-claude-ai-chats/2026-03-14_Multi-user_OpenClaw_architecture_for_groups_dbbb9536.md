# Multi-user OpenClaw architecture for groups

created: 2026-03-14T07:50:42.129868Z  uuid: dbbb9536-108e-4725-b285-d9124af95d96  export: old
messages: 8  total_chars: 17305  human_chars: 375

summary: **Conversation Overview**

The conversation focused on deploying OpenClaw for a group rather than a single user, covering multi-user architecture patterns, Telegram group integration with per-topic agent routing, OpenClaw's coding capabilities, and curated reading resources for understanding the system's architecture and design.

On the multi-user deployment question, Claude outlined three architectural patterns: a single agent with per-peer session scoping (`dmScope: "per-peer"`), multiple isolated agents on one gateway with binding-based routing, and fully isolated per-user instances via Clawbake/Kubernetes. Claude recommended starting with Pattern 1 on Telegram or Discord given the person's existing Docker setup, then graduating to Pattern 2 for specialized agents as needed. A security note was raised about credential bleed risk when multiple agents share a runtime.

On Telegram group integration, the person asked specifically about routing different agents to different forum topics. Claude explained that Telegram supergroups with Forum Topics enabled use `message_thread_id` for per-topic routing, but noted that true per-topic `agentId` routing has outstanding bugs. Three practical approaches were outlined: per-topic system prompts and skills with one agent (works today), multiple bots each owning a topic (works today, recommended), and one bot with sub-agent delegation. The multi-bot approach was recommended for its intuitive UX and isolated agent contexts.

On coding, Claude explained that OpenClaw uses Pi as its built-in coding engine with a minimal four-tool design (read, write, edit, bash), running directly via SDK instantiation rather than as a subprocess. OpenClaw can also orchestrate external coding agents like Claude Code or Codex as background processes using `claude --print --permission-mode bypassPermissions` for Claude Code and PTY spawning for interactive agents. The shared filesystem constraint for multi-user coding scenarios was flagged.

For architecture reading, Claude curated seven resources ordered by recommended reading sequence: Bindschaedler's systems-level conceptual piece first, Ronacher's Pi design philosophy piece second, then Paolo's full architecture walkthrough, followed by reference-grade materials including the official docs, DeepWiki code-level detail, a self-documenting Opus 4.6 deep dive, the community OpenClaw Book, and a memory system deep dive.


---
**HUMAN** (2026-03-14T07:50):

I want to build an openclaw for a group instead of just me, what’s the best approach

---
**ASSISTANT** (2026-03-14T07:51):

The user is asking about building an "OpenClaw" for a group rather than just themselves. From their memory context, I know Ren has explored the OpenClaw vs. Claude Code comparison before, focusing on agent architecture efficiency and context window trade-offs. Let me search for past conversations to get more context on what they've discussed about OpenClaw.
```
This block is not supported on your current device yet.
```

Ren has already set up OpenClaw with Docker and explored its architecture. Now they want to make it work for a group, not just themselves. Let me think about the best approaches for this.

OpenClaw is built around Pi (minimal coding agent) with a gateway that connects to messaging platforms. The key question is: how do you make this work for multiple people in a group/community context?

Let me search for more current info on OpenClaw's multi-user capabilities.
```
This block is not supported on your current device yet.
```

Great, I have a lot of context now. Let me synthesize this for Ren's specific situation - they want to build OpenClaw for a group (their community), not just themselves. Given their community-building focus and the Docker setup they already have, I should lay out the main architectural approaches.Good timing to think about this — the OpenClaw ecosystem has matured a lot on the multi-user front since you set up your Docker deployment. There are essentially three architectural patterns, and the right one depends on what "for a group" means for your community.

**Pattern 1: One agent, multiple users (simplest)**

This is the fastest path. You keep your existing single OpenClaw instance but configure it so each group member gets isolated sessions. The key setting is `dmScope: "per-peer"`, which gives each user their own DM session rather than everyone sharing one. Combine this with allowlists on whichever channel your community uses (Telegram, WhatsApp, Discord) to control access. The agent shares one personality/workspace (your SOUL.md, skills, etc.) but conversations are private per person.

This works well if the goal is "give my community access to a shared AI assistant with a shared knowledge base" — like a community concierge that knows your group's context.

**Pattern 2: Multiple isolated agents on one gateway**

OpenClaw's multi-agent routing lets multiple people share one Gateway server while keeping their AI workspaces and data fully isolated. Each agent gets its own workspace with SOUL.md, AGENTS.md, skills, and separate session storage. You define bindings that route specific users or channels to specific agents.

This is the pattern if different members of your group need different agent configurations — say one agent is tuned for hardware sourcing research, another for community coordination, another for writing/editing. The recommended starting configuration for a small team is two to three specialized agents, and you can add new agents at any time without affecting existing ones.

For your Docker setup, this means multiple OpenClaw processes on one server, each with its own config directory and port. On a single server, this keeps costs low and management simple, though it creates a single point of failure.

**Pattern 3: Fully isolated per-user instances (Clawbake / K8s)**

Clawbake is an open-source system that provisions each team member their own isolated OpenClaw instance in Kubernetes, managed through a web dashboard or Slack with a single Helm chart. Each person gets their own namespace, persistent volume, API keys, and network isolation. This is enterprise-grade and probably overkill for your community unless you're handling sensitive data or want to let people fully customize their own agents.

**My recommendation for your situation:**

Given that your community is your competitive advantage and you're already running Docker, I'd start with **Pattern 1 on Telegram or Discord** with `per-peer` session scoping. Here's why:

1. Your community members probably want access to a shared AI brain that understands your group's context (The Fork, hardware sourcing knowledge, 706-style community norms) — not isolated agents
2. You can enrich the shared workspace with your research, documents, and community knowledge in SOUL.md and the skills folder
3. It's one `docker-compose.yml` change from what you already have
4. API costs scale linearly with usage and you control the allowlist

Then if specific people in the group need specialized agents (e.g., a dedicated hardware sourcing agent vs. a writing assistant), you graduate to Pattern 2 by adding agent entries to your config.

One security consideration worth flagging: credential bleed is a real risk when multiple agents share a runtime — secrets loaded into one gateway are accessible to all agents in that process. If any of your group members will have shell access or handle sensitive credentials, separate those into different gateway tiers early.

Want me to draft the config changes to your existing Docker setup for the multi-user pattern, or do you want to think through which channel (Telegram/Discord/WhatsApp) makes most sense for your group first?

---
**HUMAN** (2026-03-14T07:56):

Can I have a telegram group with different channels where different agents respond to each channel

---
**ASSISTANT** (2026-03-14T07:57):

Ren wants to know if they can set up a Telegram group with different channels/topics where different OpenClaw agents respond to each one. Let me search for more specific info on this.
```
This block is not supported on your current device yet.
```

Great, I have a lot of good info on this. Let me synthesize the key findings for Ren.Yes, this is exactly the pattern people are converging on — a Telegram forum supergroup where each topic routes to a different agent. It works, but there's an important caveat about the current state of the feature.

**How it works architecturally**

You create a Telegram supergroup with Forum Topics enabled. Each topic gets a `message_thread_id`. OpenClaw treats each topic as a separate session, and you can set different system prompts, skills, and settings per topic. The config looks like this:

```json5
{
  channels: {
    telegram: {
      groups: {
        "-100123456789": {
          topics: {
            "33": { agentId: "research", systemPrompt: "..." },
            "34": { agentId: "coder", systemPrompt: "..." },
            "35": { agentId: "sourcing", systemPrompt: "..." }
          }
        }
      }
    }
  }
}
```

In practice this means: General topic goes to a main agent, a Research topic gets web search skills, a Dev topic gets code execution tools, and an Alerts topic could be notifications-only with the bot disabled.

**The caveat: per-topic `agentId` routing is still buggy**

Multiple GitHub issues requesting per-topic agent routing were closed as "completed" by AI triage, but the actual feature didn't fully exist — the referenced commits fixed session path resolution, not topic-to-agent routing. A newer issue (#27562) from late February proposes the proper implementation where the session key resolves as `agent:<agentId>:telegram:group:<chatId>:topic:<topicId>`.

So right now you have two reliable approaches:

**Approach A: Per-topic system prompts + skills (works today)**

One agent, but each topic gets different behavior via per-topic `systemPrompt` and `skills` config. Topic entries inherit group settings unless overridden for requireMention, allowFrom, skills, systemPrompt, and enabled. This means your "hardware sourcing" topic can have tools and prompts completely different from your "writing" topic, but they share the same agent workspace and memory.

**Approach B: Multiple bots, one per topic (works today, more setup)**

The approach several people have landed on is multiple Telegram bots (one per agent), each owning a topic in a single forum group. Each bot is a separate OpenClaw agent with its own workspace, SOUL.md, memory, and tools. You create each bot via BotFather, add them all to the group, and configure each to only respond in its designated topic. You configure peer routes with both `kind: "group"` and `kind: "channel"` for the same group ID, because Telegram can report the same group as different peer kinds — a common gotcha.

**Approach C: One bot + sub-agent delegation (more elegant, more complex)**

You talk to one main bot in the group, and it delegates work to sub-agents using `sessions_spawn` in the background, with sub-agents announcing results back into the same thread. This is the cleanest UX but requires more orchestration work.

**For your community, I'd recommend Approach B.** Here's why: your group members will intuitively understand "go to the #hardware-sourcing topic to talk to the sourcing agent" — it maps naturally to how people already use Telegram forum groups. Each agent gets fully isolated context, and you can tune models per agent (Sonnet for casual Q&A topics, Opus for deep research topics) to manage API costs. The setup overhead is just creating extra bots in BotFather and adding agent entries to your config.

One practical tip: for topics where both humans chat and an agent is bound, set `requireMention: true` so the bot only responds when tagged. For agent-dedicated topics, set it to `false` so every message gets a response. This keeps the human conversation natural in mixed topics.

Want me to draft the full config for a specific topic layout you have in mind?

---
**HUMAN** (2026-03-14T08:01):

How do people use openclaw for coding? Does it call Claude code or some cli? Or it just code

---
**ASSISTANT** (2026-03-14T08:02):

Ren is asking about how OpenClaw handles coding tasks - whether it invokes Claude Code, uses some CLI, or does coding itself. From our previous conversation, I know OpenClaw uses Pi as its coding engine, which has a minimal approach with just read/write/edit/bash tools. Let me search for more current info on how OpenClaw handles coding workflows.
```
This block is not supported on your current device yet.
```

Great, I have a comprehensive picture now. Let me synthesize this for Ren.It just codes directly — Pi is the engine, and it's radically minimal. But OpenClaw can also *orchestrate* other coding agents like Claude Code or Codex as subprocesses. So there are actually two layers to understand.

**Layer 1: Pi is the built-in coding brain**

Pi has the shortest system prompt of any coding agent — roughly 200 tokens — and only four tools: read, write, edit, bash. That's it. Mario Zechner's argument is that all frontier models have been RL-trained extensively, so they inherently understand what a coding agent is. The model knows what bash is, knows how files work. If you need ripgrep, run `rg` via bash. If you need to search GitHub, use `gh` via bash.

OpenClaw doesn't spawn Pi as a subprocess — it directly imports and instantiates Pi's AgentSession via the SDK (`createAgentSession()`), then replaces some of Pi's base tools with its own sandboxed versions and layers on OpenClaw-specific tools like messaging, browser, canvas, cron, and channel-specific actions. So when you message your OpenClaw agent "build me a React app," it's Pi's agent loop running with the LLM, reading/writing/editing files and executing bash commands in the workspace directly.

Pi also has an extension system where extensions can persist state into sessions, with built-in hot reloading — the agent can write code, reload, test it, and loop until the extension works. And sessions are trees, so the agent can branch off to fix something without polluting the main context, then rewind back.

**Layer 2: OpenClaw can orchestrate other coding agents**

This is where it gets interesting for heavier coding tasks. OpenClaw has a coding-agent skill that delegates tasks to Codex, Claude Code, or Pi agents via background processes. The pattern is:

- For **Claude Code**: `claude --print --permission-mode bypassPermissions` (no PTY needed)
- For **Codex/Pi/OpenCode**: spawned with `pty:true` since they're interactive terminal apps

The recommended use cases for delegation are building new features/apps, reviewing PRs (spawn in temp dir), refactoring large codebases, or iterative coding that needs file exploration. For simple one-liner fixes, the agent just edits directly.

So you can literally message your OpenClaw bot on Telegram: "spin up Claude Code to refactor the auth module in my project" and it will:

1. Create a git worktree
2. Spawn Claude Code as a background process
3. Monitor progress
4. Report back when done
5. Optionally create a PR

You can even run multiple coding agents in parallel on different issues using git worktrees, each in background mode, then monitor and create PRs after they finish.

**The practical difference for your group setup:**

For a Telegram group with coding topics, the Pi-native approach (Layer 1) is what runs by default — your group members message the agent and it reads/writes/executes in its workspace. If someone in the group needs heavier coding done, they'd ask the agent to spawn a dedicated coding agent (Layer 2) in the background.

The key constraint is that the workspace is per-agent, so if multiple group members are coding through the same agent, they're sharing a filesystem. For isolated coding work per person, you'd want either `per-peer` session scoping or separate agents per developer in the group.

---
**HUMAN** (2026-03-14T08:07):

Need to read something to understand the architecture and design of openclaw, please find me the best

---
**ASSISTANT** (2026-03-14T08:08):

The user wants to find the best resources to understand OpenClaw's architecture and design. Let me search for documentation, blog posts, and technical deep-dives.
```
This block is not supported on your current device yet.
```

Great, I found a lot of good resources. Let me curate the best ones for Ren, organized by depth and focus.Here's my curated reading list, ordered from "start here" to deep cuts:

**1. Start here — the conceptual "why"**

[Decoding OpenClaw: The Surprising Elegance of Two Simple Abstractions](https://binds.ch/blog/openclaw-systems-analysis/) by Laurent Bindschaedler. This frames OpenClaw as a systems problem rather than a prompt engineering problem, arguing the innovation is in composing familiar concepts (event loops, durable state, process isolation) into a coherent runtime for LLM agents. It reduces the whole architecture to two primitives: periodic invocation with session identity, and durable file-based memory with compaction. This is the most intellectually satisfying piece and will resonate with how you think about systems.

**2. The full architecture walkthrough**

[OpenClaw Architecture, Explained](https://ppaolo.substack.com/p/openclaw-system-architecture-overview) by Paolo. Written by someone who went deep into the codebase specifically to understand agent architecture decisions, covering the Gateway, runtime, sessions, tools, plugin system, and multi-channel deployment. Good diagrams, practical focus.

**3. The self-documenting deep dive**

[Reference Architecture: OpenClaw (Opus 4.6 Edition)](https://robotpaper.ai/reference-architecture-openclaw-early-feb-2026-edition-opus-4-6/) — this was generated by an OpenClaw instance running Opus 4.6 that was asked to deep-dive into its own source code. Covers the full message lifecycle, memory layers, session resolution, and tool architecture. The author notes the memory system has held up well across dozens of projects over weeks of use.

**4. Pi specifically — the coding agent underneath**

[Pi: The Minimal Agent Within OpenClaw](https://lucumr.pocoo.org/2026/1/31/pi/) by Armin Ronacher (the Flask creator). He explains why Pi's minimal four-tool design works, the extension system with persisted state and hot reloading, and the tree-based session branching that lets you make side-quests without wasting context. This is the best piece for understanding the design philosophy behind the agent engine you're actually interacting with.

**5. Memory system deep dive**

[Deep Dive: How OpenClaw's Memory System Works](https://snowan.gitbook.io/study-notes/ai-blogs/openclaw-memory-system-deep-dive). Covers the file-first Markdown-driven memory, hybrid search (vector + BM25 fusion), automatic memory flush before compaction, and the sliding-window chunking algorithm. Relevant if you're thinking about how a shared group agent retains knowledge over time.

**6. Reference-grade technical docs**

- [Official architecture docs](https://docs.openclaw.ai/architecture) — covers Gateway, agent loop, network model, session model, workspace structure, multi-agent routing, streaming, and protocol.
- [DeepWiki: Architecture Deep Dive](https://deepwiki.com/openclaw/openclaw/15.1-architecture-deep-dive) — code-level detail on the Gateway control plane, agent execution pipeline, channel monitor implementations, and tool execution infrastructure.
- [OpenClaw Book](https://www.openclawbook.xyz) — a community-generated comprehensive book covering every subsystem chapter by chapter, from Gateway server architecture through Pi agent runtime to the tool system and canvas.

**My suggested reading order for you:** Start with Bindschaedler (#1) for the systems-level mental model, then Ronacher (#4) for the Pi agent philosophy, then the architecture walkthrough (#2) for the full picture. The rest is reference material you'll want when you're actually building the group setup.
