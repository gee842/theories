# Ren's Theories

Everything Ren has thought, drafted and theorised from 2021 to September 2026, gathered from `~/repos`, `~/writings`, `~/wamo`, `~/meta_attractor`, `~/Downloads`, `~/Desktop`, the claude.ai chat exports and the Claude Code memories and transcripts — organised so the ideas can be connected, tested, taught, and turned into books.

## Start here

| File | What it gives you |
|---|---|
| [MAP.md](MAP.md) | The whole corpus on one page: what the central claim is, how the theories connect, and what to do next. |
| [TIMELINE.md](TIMELINE.md) | How the thinking developed, 2021 to 2026, and where the vocabulary changed. |
| [GLOSSARY.md](GLOSSARY.md) | The canonical terms, bilingual, with their aliases across drafts and where each was coined. |
| [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) | What is unresolved, what contradicts what, and where a hostile reader would attack. |
| [BOOKS.md](BOOKS.md) | The books this material can support, in the order they should be written. |
| [drafts/](drafts/) | New writing built from the corpus. `2026-09-04-one-work/` holds the plan for one essay and one short book on a single spine, its gap list, and the first essay draft. |
| [Evolving community swarms](theories/evolving-community-swarms/README.md) | Exploration opened 2026-09-05: local agent reasoning and a community space that grows into its own software environment. The [updated vision and plan](theories/evolving-community-swarms/next-vision/README.md) aims to surpass existing systems through adaptive boundaries, reusable evidence and sustained learning. Includes the founding context and comparative research. |

New exploration: [Architecture for a living Earth](theories/architecture-for-a-living-earth/README.md), opened 2026-09-13 — branching towers, elevated frameworks, automated construction, circulating materials, and the ecological conditions under which human settlements could support more life.

## The layers

**`theories/<slug>/`** — one folder per theory. `README.md` is the canonical document: the strongest current formulation, the mechanism in prose, every claim with its citation, the genealogy, what earlier versions lost, Ren's own words, the open critiques, and what to read next. The `synthesis-*.md` files beside it are the reading drafts it was built from; they are kept because they carry detail the canonical document compresses.

**`sources/`** — a copy of every source document, grouped by origin and never edited. [SOURCES.md](sources/SOURCES.md) records what came from where, with true dates. The originals stay where they were.

**`_process/`** — how this was built, what it does not cover, and where it was found wrong.
- [BRIEF.md](_process/BRIEF.md) — the orientation given to every reader.
- [COVERAGE.md](_process/COVERAGE.md) — what was actually read, and the honest gaps.
- [CRITIQUE-FINDINGS.md](_process/CRITIQUE-FINDINGS.md) — sixty-nine findings from five independent audits of this folder, twenty of them high severity. Read it before quoting anything from here in public.
- [LOST-ARTIFACTS.md](_process/LOST-ARTIFACTS.md) — finished essays that exist only on claude.ai, and how to get them back.
- [THEORY-DIGEST.md](_process/THEORY-DIGEST.md) — every theory's opening paragraph and status line in one file.
- [THEORY-TEMPLATE.md](_process/THEORY-TEMPLATE.md) — the structure each synthesis follows.
- `reading-notes/` — Ren's own words, extracted from 381 claude.ai conversations and 272 of his Claude Code messages, with one notes file per batch.
- `timeline-raw.tsv` — every source file with its true date.

## Before you quote anything

The audit found that AI-written sentences had been credited to Ren in several places, including the corpus's signature line. Those have been corrected, but the general risk remains: most finished documents here are AI prose written from Ren's ideas, and the boundary is not always marked in the sources themselves. Before publishing a sentence as Ren's, check it against `_process/reading-notes/` or the original conversation. A quotation that survives that check is safe; one that does not may still be a good sentence, but it is not his.

## Conventions

- The originals are untouched; `sources/` is a snapshot taken on 2026-09-03. New material goes into `sources/` with a line in `SOURCES.md`, then into the relevant `theories/<slug>/README.md` — not into a parallel document.
- Chinese and English are equally primary. Terms keep their Chinese form with a gloss on first use.
- Every claim cites a source path. Ren's own words are quoted verbatim and marked; AI-drafted elaborations and AI reviews are labelled as such, because much of this corpus is AI-assisted writing from Ren's ideas and the distinction matters for publication.
- Genealogy is preserved. What an earlier version had and a later one dropped is listed rather than silently merged away — a rule that comes from Ren's own standing complaint about lossy consolidation.

## How this was built

Two multi-agent reading passes over the whole corpus on 2026-09-03: readers covering every source group wrote one synthesis per theory-part, three more assembled the theories that live scattered across the corpus rather than in one folder, and a further pass merged those into the canonical documents and the cross-cutting layer above. Independent critics then went back to the sources looking for content that had been dropped, claims that were not supported, and quotations that had drifted. `_process/COVERAGE.md` records what each pass did and did not read.
