# Reading notes — Ren's own words, extracted

These files exist because the most valuable material in the corpus is not in the drafts. It is in what Ren typed himself: his messages to Claude on claude.ai between March 2024 and May 2026, and his instructions to Claude Code while building software between 2026-03 and 2026-09. The finished documents are mostly AI prose written from those messages. The messages are the thinking.

## The input files

The input files moved to [`_process/history/2026-09-consolidation/reading-notes-inputs/`](../history/2026-09-consolidation/reading-notes-inputs/) in batch H1 (17 October 2026; receipt `_process/architecture/moves/H1.json`); the table describes them as they were.

| file | what it holds |
|---|---|
| `hb-01.md` … `hb-03.md` | Ren's turns only, from 381 selected claude.ai conversations, in date order. Claude's replies are stripped; where Ren says "yes, exactly" he is endorsing something removed, and the full conversation is named in the heading so it can be opened. 838 KB of his own words. |
| `cb-01.md` … `cb-07.md` | Ren's own messages to Claude Code, filtered for conceptual and design language and deduplicated: 272 of 731 long messages. Mostly build instructions with design philosophy inside them. |

## The output files

`out-hb-*.md` and `out-cb-*.md` are what the readers found. Each has the same shape:

1. An orientation paragraph on what that period or project was about.
2. **Ideas** — every distinct claim, framework, distinction or turn of thought Ren puts forward, numbered, each with a verbatim quote, the date, the conversation or project, and the theory it belongs to. Sixty to two hundred items per batch. Endorsements of Claude's formulations are marked.
3. **Recurring preoccupations** — what he returns to, with the dates showing the arc.
4. **Ideas that appear nowhere else in the corpus** — the most valuable section. These are things the written drafts do not carry, verified against the theory syntheses.
5. **Ren's questions** — the open questions he actually asks, verbatim. Good material for books, because a book is often the answer to a question someone actually asked.
6. **Style and method notes** — how he thinks and corrects.

## How to use them

Grep for a theory slug to find everything tagged to it. Grep for a date to see what he was thinking that week. Read section 4 of each file if you want the fastest route to something in the corpus that has never been written up.

These notes are derived material, not sources: they live under `_process/` rather than `sources/` for that reason. The conversations they were extracted from are in `sources/12-claude-ai-chats/` and the Claude Code messages in `sources/14-claude-code-prompts/`.
