# Claude memory after /clear command

created: 2026-04-21T18:09:34.481299Z  uuid: 52f0395b-35ca-4dbf-a1a1-e8c935f5ab41  export: new
messages: 2  total_chars: 1576  human_chars: 102

summary: **Conversation Overview**

The person asked a brief but practical question about Claude Code's behavior after using the `/clear` command: specifically, whether Claude would know which plan to execute if told to "start" in a new session. Claude explained that `/clear` wipes all conversation context entirely, meaning any plan discussed in a prior session would not be remembered. Claude distinguished between what persists across `/clear` (files on disk, `CLAUDE.md` files, MCP connections and settings) and what does not (conversation history, plans produced in plan mode, and TodoWrite tool lists).

Claude recommended a concrete workflow: before clearing, the person should save any plan to a file (such as `plan.md` or `PLAN.md`), then after clearing, explicitly instruct Claude to read that file and begin execution. Claude also suggested encoding this as a standing instruction in `CLAUDE.md` so that plan outputs are always written to `plan.md` before being presented. The recommendation was framed around the person's apparent working style involving long focused sessions and a preference for delegating work without needing to re-brief Claude each time.


---
**HUMAN** (2026-04-21T18:09):

in claude code, if i do /clear and come back, tell claude to start, will it know which plan to start"?

---
**ASSISTANT** (2026-04-21T18:09):

  The user is asking whether Claude Code would remember a plan after using `/clear` and then saying "start" — essentially testing my self-awareness about context persistence. Since `/clear` wipes the conversation history, I'd have no memory of any previous plan unless it's stored in a persistent file within the project itself, like a plan document or similar artifact.No. `/clear` wipes the conversation context entirely — Claude Code comes back with no memory of the plan you discussed. Saying "start" in a fresh session is ambiguous; it'll either ask you what plan or guess from whatever's on disk.

What persists across `/clear`:
- `CLAUDE.md` files (project + user-level memory)
- Files on disk
- MCP connections, settings, subagents

What doesn't:
- The conversation (including any plan produced in plan mode, unless you exited with "keep plan in context" — and even that dies on `/clear`)
- Todo lists from the TodoWrite tool

So the reliable pattern is: before `/clear`, dump the plan to a file (`plan.md`, `PLAN.md`, or a section in `CLAUDE.md`). Then after `/clear`, say "read plan.md and start executing" or similar. Claude Code will read it and pick up where you left off.

Given how you work — long hyperfocus sessions, wanting to delegate without re-briefing — it's worth making this a habit: every plan-mode output → `plan.md` before clearing. You can even bake it into `CLAUDE.md`: "When producing a plan, always write it to `plan.md` before presenting it."
