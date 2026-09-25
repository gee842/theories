# Pi agent architecture and design

created: 2026-04-12T16:39:36.279182Z  uuid: fa34a70e-1a75-4114-b041-03163aedb8bc  export: new
messages: 14  total_chars: 17447  human_chars: 208


---
**HUMAN** (2026-04-12T16:39):

Explain pi agent

---
**ASSISTANT** (2026-04-12T16:39):

The user is asking about "pi agent" - let me search past conversations to see if this refers to something specific we've discussed before.
```
This block is not supported on your current device yet.
```

The user is asking about Pi agent. Based on past conversations, this is the coding engine inside OpenClaw. Let me synthesize what I know.Pi is the coding engine inside OpenClaw, built by Mario Zechner. The core philosophy is radical minimalism — about 200 tokens of system prompt and only four tools: **read, write, edit, bash**.

The argument behind it: frontier models have already been RL-trained extensively on coding tasks, so they inherently know what a coding agent is. You don't need thousands of tokens of instructions telling the model how to use files and terminals. The model already knows. So strip everything away and let it work.

The practical implications are significant. Compared to Claude Code's ~18,000–32,000 tokens of fixed overhead (system prompt, 18 tool definitions, sub-agent prompts, MCP), Pi consumes roughly 600 tokens. On a 200K context window, that means almost all of it goes to your actual code rather than scaffolding.

The tradeoff: Pi has no plan mode, no IDE integration, no confirmation gates (YOLO by default), and no specialized tools — if you need ripgrep, you run `rg` via bash. This makes it more error-prone on edge cases but far more transparent. Every tool call is visible, unlike Claude Code's sub-agents which operate as black boxes.

In OpenClaw's architecture, Pi isn't spawned as a subprocess — it's imported directly via `createAgentSession()`, and OpenClaw replaces some of Pi's base tools with sandboxed versions while layering on messaging, browser, canvas, and cron tools. So when your OpenClaw agent codes, it's Pi's agent loop running underneath.

---
**HUMAN** (2026-04-12T16:43):

Explain pi api

---
**ASSISTANT** (2026-04-12T16:43):

The user is asking about "pi api" - this could refer to Pi's API within OpenClaw, or something else. Let me search past conversations.
```
This block is not supported on your current device yet.
```

The user is asking about "Pi API" - this could mean the API/SDK that Pi exposes for programmatic use. Let me search more specifically.
```
This block is not supported on your current device yet.
```

The search results don't have a specific discussion about "Pi API" as a standalone concept. The user might be asking about Pi's programmatic API - how you use Pi as a library/SDK. Let me search more specifically or just search the web.
```
This block is not supported on your current device yet.
```

Now I have good information about Pi's API/SDK. Let me synthesize this.Pi's API is a layered TypeScript SDK — a monorepo of four packages that stack on each other:

**`pi-ai`** (bottom layer) handles multi-provider LLM communication. It streams completions across Anthropic, OpenAI, and Gemini, and is designed so sessions can contain messages from different providers. It deliberately avoids leaning into provider-specific features that don't transfer.

**`pi-agent-core`** adds the agent loop and tool execution. You define tools as `AgentTool` objects with a name, description, typed parameters (using TypeBox), and an `execute` function. The loop handles sending to the LLM, parsing tool calls, executing them, and streaming responses back.

**`pi-coding-agent`** builds on top with the four built-in coding tools (read, write, edit, bash), session persistence, an extension system with hot reloading, and compaction (automatic history summarization when approaching token limits).

**`pi-tui`** is the terminal UI layer for CLI interfaces.

The key entry point for embedding Pi is `createAgentSession()` from `pi-coding-agent`. OpenClaw wraps the complexity into `runEmbeddedPiAgent`, which handles session management and event handling in a single call. You pass it a session ID, workspace directory, provider/model config, prompt, and a callback for block replies.

You can also hook into lifecycle events — `api.on("context", ...)` lets you rewrite the message array before it hits the LLM, `api.on("session_before_compact", ...)` lets you replace the default compaction with custom summarization, and `api.registerCommand()` adds user-facing commands separate from LLM tools.

The packages are published as `@mariozechner/pi-coding-agent`, `@mariozechner/pi-ai`, `@mariozechner/pi-agent-core`, and `@mariozechner/pi-tui`. You can use any layer independently — build a bare LLM wrapper with just `pi-ai`, or a full coding agent with all four.

---
**HUMAN** (2026-04-12T16:46):

Write a simple agent with full customized system prompt and tui

---
**ASSISTANT** (2026-04-12T16:47):

The user wants me to write a simple agent using Pi's SDK with a custom system prompt and TUI. Let me search for more specific documentation on how to do this.
```
This block is not supported on your current device yet.
```

Let me fetch the actual example files from the Pi monorepo to get the exact API usage.
```
This block is not supported on your current device yet.
```

Now let me get the TUI example too.
```
This block is not supported on your current device yet.
```

Now let me look for the TUI example specifically.
```
This block is not supported on your current device yet.
```

Let me fetch the TUI example from the Nader tutorial to get the actual code.
```
This block is not supported on your current device yet.
```

Let me search for the specific TUI example file.
```
This block is not supported on your current device yet.
```

Now I have enough information to write a comprehensive example. Let me synthesize the two approaches: one using the lower-level pi-tui with custom system prompt, and another using the higher-level InteractiveMode.Now I have enough to give you a solid working example. There are actually two approaches — I'll show both.

**Approach 1: Full InteractiveMode (easiest, gets you Pi's built-in TUI)**

This gives you the complete Pi terminal experience — markdown rendering, editor with autocomplete, session tree, slash commands — with your own system prompt:

```typescript
// agent.ts
import {
  createAgentSessionFromServices,
  createAgentSessionRuntime,
  createAgentSessionServices,
  getAgentDir,
  InteractiveMode,
  SessionManager,
  DefaultResourceLoader,
  type CreateAgentSessionRuntimeFactory,
} from "@mariozechner/pi-coding-agent";

const createRuntime: CreateAgentSessionRuntimeFactory = async ({
  cwd, sessionManager, sessionStartEvent,
}) => {
  const services = await createAgentSessionServices({
    cwd,
    resourceLoader: new DefaultResourceLoader({
      systemPromptOverride: () => `You are Spore, a coordination agent for the 706 network.

You help with:
- Planning events and meetups across Southeast Asia
- Tracking project status across OpenClaw, Nomad OS, and hardware builds
- Drafting bilingual (EN/ZH) communications
- Researching payment rails, manufacturing contacts, and logistics

Be concise. Think in systems. Default to action over analysis.
When writing Chinese, use 简体. When uncertain, say so.`,
      appendSystemPromptOverride: () => [],
    }),
  });

  return {
    ...(await createAgentSessionFromServices({
      services, sessionManager, sessionStartEvent,
    })),
    services,
    diagnostics: services.diagnostics,
  };
};

const runtime = await createAgentSessionRuntime(createRuntime, {
  cwd: process.cwd(),
  agentDir: getAgentDir(),
  sessionManager: SessionManager.create(process.cwd()),
});

const mode = new InteractiveMode(runtime, {
  migratedProviders: [],
  modelFallbackMessage: undefined,
  initialMessage: undefined,
  initialImages: [],
  initialMessages: [],
});

await mode.run();
```

**Approach 2: Manual pi-tui wiring (full control)**

This uses the lower-level TUI components directly, so you control every piece:

```typescript
// custom-tui-agent.ts
import { createAgentSession, DefaultResourceLoader, SessionManager } from "@mariozechner/pi-coding-agent";
import { getModel, streamSimple } from "@mariozechner/pi-ai";
import { TUI, Text, Editor, ProcessTerminal } from "@mariozechner/pi-tui";

const model = getModel("anthropic", "claude-sonnet-4-6");

const loader = new DefaultResourceLoader({
  systemPromptOverride: () => `You are Spore, a coordination agent.
You have access to the filesystem. Be concise. Act, don't theorize.`,
  appendSystemPromptOverride: () => [],
});
await loader.reload();

const { session } = await createAgentSession({
  resourceLoader: loader,
  model,
  thinkingLevel: "off",
  sessionManager: SessionManager.inMemory(),
});

session.agent.streamFn = streamSimple;

// Set up TUI
const terminal = new ProcessTerminal();
const tui = new TUI(terminal);

const header = new Text("🍄 Spore Agent — type your message, Ctrl+C to exit\n");
tui.addChild(header);

const editor = new Editor(tui, {});
tui.addChild(editor);

let streamingText = "";
let responseComponent: Text | null = null;

session.subscribe((event) => {
  if (event.type === "message_update") {
    const e = event.assistantMessageEvent;
    if (e.type === "text_delta") {
      streamingText += e.delta;
      if (!responseComponent) {
        responseComponent = new Text("");
        tui.addChild(responseComponent);
      }
      responseComponent.setText(streamingText);
      tui.requestRender();
    }
  }
  if (event.type === "tool_execution_start") {
    const toolLine = new Text(`⚙ ${event.toolName}`);
    tui.addChild(toolLine);
    tui.requestRender();
  }
  if (event.type === "agent_end") {
    streamingText = "";
    responseComponent = null;
    tui.requestRender();
  }
});

editor.onSubmit = async (text: string) => {
  const userMsg = new Text(`\n> ${text}\n`);
  tui.addChild(userMsg);
  tui.requestRender();
  await session.prompt(text);
};

tui.start();
```

**Setup for both:**

```bash
mkdir spore-agent && cd spore-agent
npm init -y
npm install @mariozechner/pi-ai @mariozechner/pi-agent-core \
  @mariozechner/pi-coding-agent @mariozechner/pi-tui
npm install -D typescript @types/node tsx

export ANTHROPIC_API_KEY=sk-ant-...
npx tsx agent.ts
```

Approach 1 is what I'd recommend for your use case — you get the full Pi TUI (markdown rendering, syntax highlighting, `/model` switching, session persistence, `/tree` navigation) with zero custom UI code, and the `systemPromptOverride` gives you complete control over the agent's identity. Approach 2 is for when you want to build something that doesn't look like Pi at all.

---
**HUMAN** (2026-04-12T16:51):

Are there any good frontend ui?

---
**ASSISTANT** (2026-04-12T16:51):

The user is asking about frontend/web UIs for Pi agents, as opposed to the terminal TUI. Let me search for this.
```
This block is not supported on your current device yet.
```

There's a pi-web-ui package. Let me summarize it.Yes — Pi has a first-party web UI package: **`@mariozechner/pi-web-ui`**.

It's a set of reusable web components built with mini-lit and Tailwind CSS v4, providing a complete chat interface with message history, streaming, tool execution, file attachments (PDF, DOCX, XLSX, PPTX, images), sandboxed artifacts (HTML, SVG, Markdown), IndexedDB storage for sessions/keys/settings, CORS proxy handling, and support for custom providers like Ollama and LM Studio.

The core component is `<agent-interface>`, which you wire to a Pi `Agent` instance:

```typescript
import { Agent } from '@mariozechner/pi-agent-core';
import { getModel } from '@mariozechner/pi-ai';
import { defaultConvertToLlm } from '@mariozechner/pi-web-ui';
import '@mariozechner/pi-web-ui/app.css';

const agent = new Agent({
  initialState: {
    systemPrompt: 'You are Spore.',
    model: getModel('anthropic', 'claude-sonnet-4-6'),
    thinkingLevel: 'off',
    messages: [],
    tools: [],
  },
  convertToLlm: defaultConvertToLlm,
});

const chat = document.createElement('agent-interface');
chat.session = agent;
chat.enableAttachments = true;
chat.enableModelSelector = true;
chat.enableThinkingSelector = true;
```

There's a minimal working example in the repo — clone it, run it with Vite, and it opens at localhost:5173. It uses "Direct Mode" by default, calling AI provider APIs directly from the browser with keys stored in localStorage.

You also get extensibility via custom message renderers (register new message types with custom Lit templates), `convertToLlm` overrides, and the full attachment pipeline for client-side document processing.

For your use case this could be interesting as a Nomad OS or 706 community-facing agent interface — it runs entirely in-browser with no backend required beyond the LLM API keys.

---
**HUMAN** (2026-04-12T16:53):

Nice, can I use it in my application?

---
**ASSISTANT** (2026-04-12T16:53):

The user is asking if they can use pi-web-ui in their own application. This is a practical question about integration. Let me give a direct answer based on what I know.Yes, it's published on npm as a standalone package. Install it alongside the core packages:

```bash
npm install @mariozechner/pi-web-ui @mariozechner/pi-agent-core @mariozechner/pi-ai
```

It's framework-agnostic since it uses web components (Lit-based), so it drops into React, Vue, Svelte, plain HTML — whatever you're building Nomad OS with. The `<agent-interface>` element is just a custom element you mount anywhere in the DOM.

A few practical things to know:

The storage layer (`AppStorage` with `IndexedDBStorageBackend`) handles session persistence, API key management, and settings entirely client-side. You'd set that up once at app init and pass it through. If you want server-side key management instead (so users don't enter their own API keys), you'd override `streamFn` with a function that routes through your backend.

For custom tools — say a "pay via QR" tool for Nomad OS — you'd define them as `AgentTool` objects on the `Agent` instance and register a custom message renderer so the result displays nicely in the chat UI. The artifact system already handles sandboxed HTML/SVG rendering, so if your agent generates a QR code as HTML, it renders inline automatically.

The CORS proxy handling is worth noting — browser-to-LLM-API calls hit CORS issues with some providers. Pi-web-ui has built-in proxy detection and auto-configuration for this, but in production you'd probably want your own proxy or backend relay anyway.

Want me to scaffold a minimal Nomad OS agent frontend with it?

---
**HUMAN** (2026-04-12T16:53):

Oh I mean pi

---
**ASSISTANT** (2026-04-12T16:53):

The user is asking if they can use Pi (the coding agent/SDK) in their application. They're not asking about pi-web-ui specifically - they're asking about Pi itself, whether they can use it as a dependency/library in their own app.

The answer is yes - Pi is designed to be embedded. That's exactly what OpenClaw does. The SDK mode is one of Pi's four modes (interactive, print/JSON, RPC, SDK).Yes, absolutely. That's one of Pi's four operating modes — SDK is explicitly designed for embedding into your own apps. OpenClaw is the proof case; it's built entirely on top of Pi's SDK.

You'd use `@mariozechner/pi-coding-agent` (and whichever sibling packages you need) as npm dependencies, then call `createAgentSession()` to spin up agent instances programmatically. You get full control over the system prompt, tools, session lifecycle, model routing, and event handling — all without forking Pi.

The license is MIT, so there are no restrictions on commercial use either.

---
**HUMAN** (2026-04-12T16:54):

How about sub agents or agent swarm

---
**ASSISTANT** (2026-04-12T16:54):

The user is asking about sub-agents or agent swarms in Pi. Let me search for this - I know from earlier context that Pi deliberately doesn't include sub-agents as a built-in feature, but there are ways to do it.
```
This block is not supported on your current device yet.
```

Great, now I have a clear picture. Pi deliberately doesn't include sub-agents, but there are community extensions that add this capability.Pi deliberately doesn't build sub-agents into core — Mario's position is that they're black boxes with poor observability and context transfer. His take: if you need Pi to spawn itself, just have it run `pi` via bash, optionally inside a tmux session where you can watch everything.

That said, the community has built several options on top of Pi's extension system:

**[pi-side-agents](https://github.com/pasky/pi-side-agents)** — An extension that automates the full tmux/worktree/merge lifecycle. You fire off work with `/agent`, each side agent gets its own tmux window and short-lived git branch with a separate worktree. Side agents can also be spawned and controlled by another agent to orchestrate a flock of subagents. It exposes tools like `agent-start`, `agent-check`, `agent-wait-any`, `agent-send` for programmatic orchestration.

**[pi-agent-teams](https://github.com/tmustier/pi-agent-teams)** — Brings Claude Code-style agent teams to Pi. Shared task list with dependency tracking, auto-claim (idle teammates pick up the next unblocked task), direct messages and broadcast via file-based mailboxes, git worktrees per teammate, and session branching to clone the leader's context into teammates. Has a `/swarm` command where the agent spawns a team and coordinates autonomously.

**[ClawTeam-OpenClaw](https://github.com/win4r/ClawTeam-OpenClaw)** — A fork of ClawTeam adapted for OpenClaw as the default agent. Full swarm orchestration with task management, inter-agent messaging, kanban board (terminal and web UI), and support for mixing different agent backends.

For your OpenClaw/SST architecture, the most interesting path is probably pi-agent-teams since it works at the extension level and maps naturally to the kind of multi-agent coordination you're building — each agent gets isolated context but can communicate through structured channels, which rhymes with your Sprite-Space-Token model.
