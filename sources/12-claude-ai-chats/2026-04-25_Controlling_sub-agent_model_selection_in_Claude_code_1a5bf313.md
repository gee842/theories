# Controlling sub-agent model selection in Claude code

created: 2026-04-25T10:36:39.832216Z  uuid: 1a5bf313-8ed1-42a4-bc78-c81d7e544351  export: new
messages: 2  total_chars: 4169  human_chars: 194


---
**HUMAN** (2026-04-25T10:36):

when my claude code spawn sub agents, it uses smaller model for complex task occasionally, can i tell it which one to trigger or do this in settings? these are agents provided by the claude code

---
**ASSISTANT** (2026-04-25T10:37):

  The user is asking about Claude Code's subagent behavior—specifically whether they can control which model gets used when Claude Code spawns subagents for complex tasks. I need to check the product self-knowledge documentation to see what's documented about model selection and subagent configuration.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

 I need to look more closely at the documentation for the built-in agents that Claude Code provides—specifically the Explore, Plan, and general-purpose ones—since that's what the user is asking about.
```
This block is not supported on your current device yet.
```

 Now I'm seeing the specific model assignments for each built-in subagent—Explore uses Haiku for speed, Plan and General-purpose inherit from the main conversation, statusline-setup runs on Sonnet, and Claude Code Guide uses Haiku. The user is realizing that subagents like Explore are deliberately using Haiku for tasks they expected might need more capability.

I can outline the control mechanisms: setting the `CLAUDE_CODE_SUBAGENT_MODEL` environment variable overrides all subagent models globally and takes highest precedence, though it's a blunt approach that forces every subagent to use that model. Alternatively, Ren could disable the built-in Explore subagent and create a custom version with a different model assignment, or rely on the resolution order where the environment variable takes priority, followed by per-invocation parameters, the subagent's own model definition, and finally the main conversation's model.Yes, you have a few levers, but the built-in agents (Explore, Plan, general-purpose, statusline-setup, Claude Code Guide) have hardcoded model assignments that you can't edit directly — you can only override them globally or replace them.

**What's actually happening:** Built-in subagent models are fixed at:
- **Explore** → always Haiku (this is probably what you're seeing — it's intentionally locked to Haiku for fast read-only codebase searches)
- **Plan** → inherits main conversation model
- **General-purpose** → inherits main conversation model
- **statusline-setup** → Sonnet
- **Claude Code Guide** → Haiku

So if Claude is delegating a task you consider complex to Explore, it's getting Haiku no matter what your `/model` is set to.

**Your options, in order of bluntness:**

1. **`CLAUDE_CODE_SUBAGENT_MODEL` env var** — this is the global hammer. It overrides every subagent's model regardless of what's in their definition. Set it to `claude-opus-4-7`, `sonnet`, etc. The resolution order is: this env var → per-invocation parameter → subagent's `model` frontmatter → main conversation's model. Downside: it forces *all* subagents onto that model, including Explore where Haiku is genuinely the right call for cheap fanout.

2. **Steer in your prompt** — if you say "use the general-purpose subagent to do X" rather than letting Claude pick, general-purpose inherits your main model. This dodges Explore entirely.

3. **Disable the built-in and replace it** — add `"deny": ["Agent(Explore)"]` to your `permissions` settings, then drop a custom subagent into `~/.claude/agents/` or `.claude/agents/` with the same role but `model: opus` (or `inherit`) in the frontmatter. This is the surgical answer if you only want one specific built-in rerouted.

4. **CLAUDE.md routing rules** — you can't change which model the built-ins use this way, but you *can* nudge Claude to prefer your custom agents over the built-ins for certain task shapes by writing routing rules into your CLAUDE.md.

For your OpenClaw harness work, option 3 is probably the cleanest pattern — keeps the rest of the system intact and lets you encode the model choice declaratively in the agent definition rather than as a session-wide env var.

Source: https://code.claude.com/docs/en/sub-agents
