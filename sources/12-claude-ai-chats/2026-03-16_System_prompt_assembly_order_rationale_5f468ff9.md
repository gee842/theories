# System prompt assembly order rationale

created: 2026-03-16T10:06:21.470101Z  uuid: 5f468ff9-a44d-49a7-878b-1d9f9d769f58  export: old
messages: 8  total_chars: 13956  human_chars: 975

summary: **Conversation Overview**

The person is working on a project called OpenClaw, an agent framework that dynamically assembles system prompts from multiple sources at runtime. The conversation focused on understanding the design rationale behind OpenClaw's specific system prompt component ordering, which follows an infrastructure-to-identity gradient: tooling, safety, skills, self-update instructions, workspace info, documentation pointers, datetime, reply tags, heartbeat contract, and runtime metadata — followed by a project context boundary, then AGENTS.md, SOUL.md, TOOLS.md, IDENTITY.md, USER.md, and HEARTBEAT.md.

Claude initially analyzed the ordering as reflecting a deliberate infrastructure-first philosophy, contrasting it with the conventional identity-first convention common in most system prompts. The person pushed back, noting that most system prompts they've encountered start with identity, prompting a more nuanced discussion of the tradeoffs between both approaches. Claude acknowledged that OpenClaw's ordering may be partly accidental, reflecting code architecture rather than pure prompt engineering theory. When the person asked for Claude's intuition on whether ordering actually matters, Claude offered that recency bias and conflict resolution are the real mechanisms at play, and that clarity of section separation likely matters more than ordering itself.

The person then asked Claude to look up actual research on the topic. Claude used web search tools and surfaced the "Lost in the Middle" research (Liu et al., 2024) and related MIT findings, which identified a U-shaped attention curve where beginning and end positions receive significantly more attention weight than middle positions — with accuracy drops exceeding 30% for content in the middle of long contexts. Claude also surfaced Anthropic's own documentation guidance recommending that longform data be placed at the top of prompts. The synthesis was that OpenClaw's ordering aligns reasonably well with the research: large structured reference material (tools, safety) benefits from primacy, while behaviorally relevant instructions (USER.md, HEARTBEAT.md) benefit from recency. The conventional identity-first pattern was characterized as a human readability preference rather than an architecturally optimal choice.


---
**HUMAN** (2026-03-16T10:06):

OpenClaw builds a custom system prompt for every agent run. This is not a static string — it's assembled from multiple sources:

```
System Prompt = 
    Tooling (available tools + descriptions)
  + Safety (guardrails)
  + Skills (available skill list with file paths)
  + Self-Update instructions
  + Workspace info
  + Documentation pointers
  + Current Date & Time (timezone-aware)
  + Reply Tags
  + Heartbeat contract
  + Runtime metadata (host/OS/model/thinking level)
  + ── Project Context ──
  + AGENTS.md (operating instructions)
  + SOUL.md (persona/tone)
  + TOOLS.md (local tool notes)
  + IDENTITY.md (agent name/vibe)
  + USER.md (user profile)
  + HEARTBEAT.md (periodic task checklist)

My question is, why this order?
```

---
**ASSISTANT** (2026-03-16T10:06):

Ren is asking about the ordering of components in OpenClaw's system prompt assembly. This is a design question about prompt engineering architecture. Let me think about why this specific ordering matters.

The ordering goes from most generic/infrastructure to most specific/personal:

1. Tooling, Safety, Skills, Self-Update, Workspace, Docs, DateTime, Reply Tags, Heartbeat, Runtime — these are all **system infrastructure**
2. Then Project Context boundary
3. AGENTS.md, SOUL.md, TOOLS.md, IDENTITY.md, USER.md, HEARTBEAT.md — these are **persona/project-specific**

This ordering pattern reflects several prompt engineering principles. Let me think through them.Great question — and it's one where the answer is partly principled prompt engineering, partly practical artifact of how LLM attention works.

The ordering follows a **infrastructure → context → identity → user** gradient, and there are real reasons for each layer's position:

**Generic system stuff first (Tooling → Runtime metadata)**

This is the "operating system" layer. By front-loading tool definitions, safety guardrails, and runtime metadata, you establish the agent's *capabilities and constraints* before it knows who it is or what it's doing. This matters because:

- Tool schemas need to be parsed reliably — putting them early and cleanly reduces the chance they get "contaminated" by persona bleed from later sections.
- Safety guardrails placed early act as a baseline frame. The model processes them before encountering any persona instructions that might create tension with those guardrails. It's harder for a SOUL.md to override safety if safety was established first as foundational context.
- DateTime and runtime metadata are factual anchors — they ground the model in reality before it starts roleplaying.

**The "Project Context" boundary marker**

That separator is doing real work. It signals to the model: "everything above was infrastructure you operate *on top of*; everything below is configuration you operate *within*." It's a cognitive frame shift.

**AGENTS.md → SOUL.md → TOOLS.md → IDENTITY.md → USER.md → HEARTBEAT.md**

This inner ordering goes from **behavioral rules → personality → capabilities → name/vibe → who you're talking to → what to do periodically**. The logic:

- **AGENTS.md first** among the project files because operating instructions are the most "law-like" — they constrain everything that follows. Think of it as the constitution before the personality.
- **SOUL.md second** because persona/tone should color how the agent executes its operating instructions, but shouldn't override them. Recency bias in transformers means later content has *slightly* more influence on generation style — but AGENTS.md being right before SOUL.md means they're both in a high-attention zone while SOUL.md gets the stylistic "last word" between the two.
- **IDENTITY.md after SOUL.md** is interesting — it separates *how you behave* from *what you're called*. Name/vibe is surface; soul is deeper. You want the model to internalize tone before it gets a label.
- **USER.md near the end** is the classic prompt engineering move: put the most *variable* and *conversation-specific* context closest to where generation begins. The model's attention to the user profile benefits from proximity to the actual conversation turns that follow.
- **HEARTBEAT.md last** because it's a periodic checklist — it's the thing the agent should "glance at" most readily during execution, so recency helps. It's the sticky note on the monitor.

**The meta-principle**

The whole thing mirrors how you'd brief a human operator: "Here are your tools. Here are the rules. Here's the mission context. Here's who you are. Here's who you're talking to. Here's your checklist." You don't start with "your name is Jarvis" and then explain what a wrench is.

There's also a practical concern: if the system prompt gets truncated (hitting context limits), you want the *infrastructure* to survive even if the personality gets clipped — a tool-capable but personality-less agent is more useful than a charming agent that can't call functions.

Does this match what you've been seeing in practice with your deployments, or are you noticing cases where the ordering creates problems?

---
**HUMAN** (2026-03-16T10:18):

hmm... i feel a lot system prompt starts with who you are and built from there

---
**ASSISTANT** (2026-03-16T10:18):

Ren is making a good observation — most system prompts DO start with identity/persona ("You are a helpful assistant named X...") and build outward from there. OpenClaw's approach inverts this. Let me think about why both approaches exist and what the tradeoffs are.Yeah, you're right — the conventional pattern is almost always identity-first:

> "You are Claude, an AI assistant made by Anthropic. You are helpful, harmless, and honest. You have access to the following tools..."

That's the dominant paradigm. OpenClaw's ordering is actually the unusual one, and it's worth asking whether it's *deliberately* inverted or just an accident of how the prompt got assembled incrementally.

**The case for identity-first (the standard approach)**

The logic is straightforward: give the model a "self" to anchor on, then everything else is interpreted *through* that self. It mirrors how humans process instructions — "who am I?" comes before "what do I do?" You establish a frame of reference, and all subsequent information gets filtered through it. If I tell you "you're a cautious security auditor" before listing your tools, you'll read the tool list differently than if I said "you're a creative hacker."

This works well because transformers build up contextual representations cumulatively — early tokens shape how later tokens are attended to. Identity-first means tool descriptions, rules, and user context all get "colored" by the persona.

**The case for what OpenClaw does**

Infrastructure-first treats the agent more like a *runtime being configured* than a *character being briefed*. The implicit philosophy is: tools and constraints are objective facts about the environment, and identity is just one more configuration layer loaded on top. It's more... mechanical. More like booting an OS than waking up a person.

**The honest answer though**

I'd guess OpenClaw's ordering is at least partly accidental — a product of how the assembly code grew organically. Tooling gets injected by the framework layer, safety by another module, project files get appended last because they're loaded from disk. The order might reflect *code architecture* more than *prompt engineering theory*.

Have you tried shuffling the sections to test whether it actually matters for your agents' behavior?

---
**HUMAN** (2026-03-16T10:20):

i have not, but since you are the llm, what is your intuition?

---
**ASSISTANT** (2026-03-16T10:20):

The user is asking me to introspect on how prompt ordering actually affects my processing. This is a genuinely interesting question and I should be honest about what I can and can't know about my own internals.Honestly? I think it matters less than either camp argues, but in specific ways that are real.

**The stuff that genuinely doesn't matter much:**

Whether tools come before or after identity — I'm not "reading" the system prompt sequentially the way a human reads a document. Attention is bidirectional within the context. By the time I'm generating tokens, I've attended to the entire prompt. The SOUL.md can "see" the tools section regardless of where it sits. So the idea that earlier content creates an interpretive lens for later content — that's more of a human cognition metaphor than how transformers actually work.

**The stuff that does matter:**

Recency bias is real. Content closer to the actual conversation turns gets slightly more attention weight during generation. So USER.md and HEARTBEAT.md being last in OpenClaw's ordering is probably genuinely helpful — those are the things you want most active in the agent's "working memory" during a response.

The other thing that's real: when instructions *conflict*, position can act as a tiebreaker. If AGENTS.md says "be concise" and SOUL.md says "be verbose and expressive," whichever one sits closer to generation has a slight edge. So the ordering becomes a *priority system for conflicts*, not a reading order.

**My actual intuition:**

The single biggest factor isn't ordering — it's **clarity and separation**. The fact that OpenClaw uses distinct named files with clear boundaries (AGENTS.md, SOUL.md, etc.) probably does more for agent quality than where those files sit in the prompt. When instructions are muddled together in one big blob, I struggle more than when they're cleanly delineated, regardless of order.

If I were designing it, I'd probably keep tools and safety early (they're long and structured — keeping them away from the conversation boundary reduces noise), and keep the most *behaviorally relevant* stuff late. Which is... roughly what OpenClaw already does.

The identity-first convention is mostly a readability choice for the humans writing the prompts. I don't think I care.

---
**HUMAN** (2026-03-16T10:25):

alright, good answer but not satisfied. can you look up and see if anyone has done the research?

---
**ASSISTANT** (2026-03-16T10:26):

The user wants me to search for actual research on system prompt ordering effects on LLM performance.
```
This block is not supported on your current device yet.
```

Good results but mostly about general prompt sensitivity, not specifically about ordering of sections within system prompts. Let me search more specifically.
```
This block is not supported on your current device yet.
```

Good, now I have solid research to draw from. The key finding is the "Lost in the Middle" phenomenon. Let me also search for anything specifically about system prompt section ordering.
```
This block is not supported on your current device yet.
```

Now I have a good picture. The key research is the "Lost in the Middle" paper by Liu et al. (2024), and Anthropic's own guidance to put longform data at the top. Let me synthesize this.Okay, so the research picture is actually pretty clear, and it corrects some of what I said earlier.

**The big finding: "Lost in the Middle" (Liu et al., 2024)**

This is the most directly relevant research. When you plot accuracy against document position, the curve forms a U shape — high at the edges, low in the middle. This holds regardless of document order randomization. Performance drops of over 30% were measured on multi-document QA when the answer document was at position 10 out of 20, compared to position 1 or 20.

MIT researchers in 2025 identified the architectural cause: tokens at the beginning of the context get attended to by every subsequent token, while a token in the middle is only visible to tokens that come after it, meaning earlier tokens accumulate more attention weight simply because they have more opportunities to be attended to. On top of that, RoPE introduces a distance-based decay where tokens far apart have reduced attention scores — middle tokens are too far from the beginning to benefit from primacy and too far from the end to benefit from recency.

**What this means for system prompt ordering:**

The practical implication is that position isn't just a tiebreaker — it creates a genuine attention gradient. The beginning and end of your context are "prime real estate," and the middle is a dead zone.

So for OpenClaw's architecture, the question becomes: what should occupy the privileged positions?

**Anthropic's own guidance is interesting here.** Their docs recommend: put longform data at the top — place your long documents and inputs near the top of your prompt, above your query, instructions, and examples. This is the opposite of identity-first! Anthropic is saying: put the bulky reference material (tools, docs) early where it benefits from primacy effects, and put the actionable instructions closer to the conversation where they benefit from recency.

Which is... basically what OpenClaw does.

**The honest synthesis:**

The research confirms that ordering matters more than I initially suggested, but in a specific way. It's not about "interpretive framing" (identity colors how you read tools) — that was my human-cognition metaphor leaking in. It's about **attention allocation**. The U-curve means:

- **Beginning**: high attention — good for large structured reference material (tool schemas, safety rules) that needs to be reliably parsed
- **Middle**: attention dead zone — put whatever you can afford to have slightly degraded access to
- **End**: high attention — good for the most behaviorally relevant instructions (user profile, heartbeat, persona) that should most strongly influence generation

OpenClaw's ordering actually aligns with this better than the "You are X" convention. Putting identity first wastes the primacy position on a sentence or two, when that position would be better used for the large tool/safety blocks that need reliable parsing. And by putting USER.md and HEARTBEAT.md last, OpenClaw gives them the recency advantage right before conversation turns begin.

The conventional identity-first approach probably persists because it feels natural to humans writing prompts, not because it's optimal for the architecture processing them. Nobody had proven it mattered until the lost-in-the-middle research came along.
