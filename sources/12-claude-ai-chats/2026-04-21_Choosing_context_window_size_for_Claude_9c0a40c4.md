# Choosing context window size for Claude

created: 2026-04-21T18:13:49.017297Z  uuid: 9c0a40c4-75dd-4bff-884f-92fe8285b293  export: new
messages: 2  total_chars: 2344  human_chars: 54

summary: **Conversation Overview**

The person asked a brief, technical question about Claude Code context window settings, specifically whether to use 1M or 20k context (likely a typo for 200k). Claude clarified the intended comparison and provided guidance on when each context size is appropriate. The conversation touched on pricing parity between the two options, attention quality tradeoffs, and specific use cases that justify the larger context window.

Claude's recommendation was to default to 200k for typical daily coding sessions, noting that most sessions peak well below that limit before compaction occurs, and that stale early-turn context in very long sessions can degrade output quality. The 1M context window was recommended for scenarios requiring simultaneous visibility into large codebases, heavy tool-call accumulation during complex multi-step operations, or situations where manually cherry-picking file references becomes a bottleneck. Claude also noted a project called OpenClaw as an example use case where 1M context could pay off when needing to hold multiple architectural layers in view simultaneously. Switching syntax was provided: `/model opus[1m]` or `/model sonnet[1m]` to enable, and `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` to disable.


---
**HUMAN** (2026-04-21T18:13):

should i use 1m context or 20k context in claude code?

---
**ASSISTANT** (2026-04-21T18:14):

  The user is asking about Claude Code's context window options, so I should look into what I know about Anthropic's product specifications to give them accurate information.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

 The user probably meant 200k context, not 20k — that's likely a typo. Given their setup with OpenClaw and complex codebases, I should clarify the main tradeoffs: 1M context has the same per-token pricing as 200k now, and it's most valuable for fitting entire large codebases in a single request or maintaining long document references where exact citations matter.Assuming you mean 200k (the standard) vs 1M — short answer: default to 200k, reach for 1M when you specifically need it.

The pricing is the same per token either way now, so it's not a cost question. The real question is what actually helps the work:

**Use 1M when:**
- Loading a large codebase or many files in a single request where you'd otherwise be manually cherry-picking what to @-include
- Sessions doing heavy tool-call accumulation (Datadog searches, repeated file reads, multi-agent orchestration) where compaction would kick in and you'd lose the intermediate reasoning
- You need exact-quote fidelity across a large document

**Stick with 200k when:**
- Normal daily coding sessions — most peak at 80–120k before compacting anyway, so 1M is wasted
- Long conversations where you'd actually benefit from a `/clear` and fresh start. Stale early-turn context often hurts more than it helps; the model wastes attention on exploration that's no longer relevant
- You care about attention quality on a focused task — needle-in-haystack retrieval degrades somewhat at the tail end of very long contexts

For OpenClaw-scale work specifically: I'd expect 1M to pay off when you want Claude to see the SST primitives, hooks, schema layer, and a feature you're implementing simultaneously — that's the "load the types alongside the component, stop micro-managing @-includes" case. For iterative SST design conversations and day-to-day coding, 200k + `/clear` discipline is probably sharper.

To switch in-session: `/model opus[1m]` or `/model sonnet[1m]`. To disable 1M entirely: `CLAUDE_CODE_DISABLE_1M_CONTEXT=1`.
