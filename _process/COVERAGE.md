# Reading coverage and known gaps

What was actually read, by whom, and what was not. Kept honest so that nobody later mistakes "organized" for "fully read".

## Method

Two multi-agent reading passes on 2026-09-03. Each reader was given the brief (`BRIEF.md`), a set of source paths, and the theory template (`THEORY-TEMPLATE.md`), and wrote one synthesis file per theory-part. A first pass of 54 readers was cut short by usage limits after 5 cluster syntheses completed; a second pass of 24 readers, restructured to be cheaper and to write files before returning, covered the rest.

The second pass made two economising decisions that are also coverage limits, recorded below: chat conversations were read as **Ren's turns only**, and Claude Code messages were **keyword-filtered** before reading.

## Coverage by source group

| group | read by | coverage |
|---|---|---|
| `00-early-2021-2022` | main session, by hand | Complete. The Pages bodies were decoded on 2026-09-04 and the full text is in `sources/00-early-2021-2022/recovered-text/`. |
| `01-writings-2025` | pass 1 cluster reader | Complete. |
| `02-wamotopia` | pass 1 cluster reader | Complete. |
| `03-meta-attractor` | pass 1 (2024 precursors + 2025-05 drafts), pass 2 (2025-08 formal, 2025-10 essays, site context) | Complete for what was copied. **Only 6 of the 22+ near-identical draft versions in `~/Downloads` were copied**; the rest are redundant iterations of the same essay and remain in `~/Downloads`. |
| `04-speculative-future` | pass 1 cluster reader | Complete, including files recovered from git history. |
| `05-alignment-and-moloch` | pass 1 cluster reader | Complete. |
| `06-zhishan` | pass 2, two readers (texts; research + writing program) | Complete. |
| `07-shengsheng-buxi` | pass 2, three readers (2026 drafts; 史料 canon; 义理 and formal doctrine) | Substantially complete. The Markov-bridge quantum series (S2–S33) was sampled rather than read line by line, by instruction. Lean source files themselves were not read — only the doctrine and reports about them. |
| `08-jian-wen-language` | pass 2, two readers | Complete. |
| `09-sts-bonfire-yi` | pass 2, two readers | Complete for what was copied. Bonfire's full `docs/` tree (345 files) was not copied; the conceptual layer was. |
| `10-context-runtime-ember` | pass 2, two readers | Complete for what was copied. Context-runtime has 96 spec files upstream; the 15 conceptual ones were copied. |
| `11-human-solutions-museum` | pass 2 cluster reader | Complete. |
| `12-claude-ai-chats` | pass 2, three "voice" readers | **381 of 719 conversations, and within those, only Ren's own turns.** Claude's replies were not read except where Ren quotes or endorses them. The 338 unselected conversations were filtered by length and keyword as logistics/trivia; their titles are listed in `_ALL-719-INDEX.tsv` and can be re-checked. |
| `13-claude-memories` | pass 2 cluster reader | Complete for theory-bearing folders; engineering-only memory folders skimmed, with skips listed in the synthesis. |
| `14-claude-code-prompts` | pass 2, seven "voice" readers | **272 of 731 long messages**, selected by conceptual-keyword density and deduplicated. The unread remainder is predominantly build instructions. |

## Gaps worth closing later

1. **~~The `.pages` documents.~~ Closed 2026-09-04.** These were decoded (a Pages file is a zip of Snappy-compressed protobuf; the decoder is kept at `sources/00-early-2021-2022/recovered-text/decode-pages-iwa.py`). The result corrected an assumption rather than filling a hole: `World of Possibilities` turned out to be one page and no more — a book begun and abandoned — while `proposal.pages` yielded about 10,000 characters of the Metamunity community-infrastructure argument that were genuinely new to the corpus, and `社区.pages` proved to be empty. See that folder's README.

2. **Voice memos and meeting recordings** in `~/Desktop/Voice Memos` and `~/Documents/Zoom` were not touched. The two otter.ai transcripts that were included turned out to be among the most direct statements of the argument in Ren's own voice, which suggests the audio is worth transcribing.
3. **Claude's side of the conversations.** Ideas that were Claude's and that Ren silently accepted will show up in the drafts but not in the "Ren's own words" sections. Where authorship matters for publication, the full conversation files are in `sources/12-claude-ai-chats/`.
4. **The 338 unselected conversations.** Worth a second filter pass if a specific idea seems to be missing its origin.
5. **The Lean proofs themselves.** The corpus records what the SSBX project claims to have proven; the claim-status ledger says roughly 150 `sorry`s remain and at least one axiom. No independent verification was attempted here.
