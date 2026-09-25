# Worlds we can inhabit

2026-09-07 · Edition 01 · A worldbuilding project by Ren, developed with AI.

An illustrated introduction for friends who have not read the project. It begins with everyday life, then makes the technical premise, material rights, plural cultures, recovery systems, and disagreements visible. It ends with an invitation to imagine and challenge the world together.

**Share this:** [Worlds we can inhabit - illustrated PDF](output/pdf/worlds-we-can-inhabit.pdf). Ten portrait pages, approximately 3.2 MB, with selectable text, bookmarks, embedded fonts, and three clickable source references. No external account or live service is required to read the PDF. This is the first friend-facing edition; its title and art direction are editorial choices, not new decisions about the world's institutions or geography.

## Inside

1. An invitation to the world.
2. An ordinary day in the Living Garden.
3. The technological premise, durable material claims, and meaningful exit.
4. Open University and many ways to spend a life.
5. House of Worlds and optional shared realities.
6. A cup's successive lives and a simple return loop.
7. Reusable architecture and a material library.
8. A neighborhood disagreement and the consequences of amplified will.
9. Questions for friends and a possible first spatial study.
10. Scope, authorship, and a few material evidence sources.

## Editable sources

- [content.json](content.json): the final cover and interior copy, and source references.
- [build.py](build.py): the page layout, final context page, PDF metadata, image placement, and export settings.
- [reader-text.txt](reader-text.txt): text extracted from the delivered edition for easier reading and reuse.
- [editorial-draft.md](editorial-draft.md): the earlier manuscript; preserved as drafting history, not the final text.
- [qa-report.json](qa-report.json): final checks and export integrity.

The original source messages and project principles remain separate. This booklet is an AI-authored synthesis of Ren's ideas, with no invented quotations attributed to Ren. Relevant sources are the [opening](../../archive/001-ren-opening.txt), [assistant development](../../archive/002-assistant-development.md), [regenerative-material addition](../../archive/004-ren-regenerative-materials.txt), [current request](../../archive/005-ren-friends-artifact-request.txt), [charter](../../foundations/charter.md), [material foundation](../../foundations/regenerative-material-civilization.md), and [bounded materials evidence note](../../research/2026-09-07-material-circulation.md).

## Illustration sources and prompts

Four raster concepts are embedded in the PDF. They depict possible scenes; they are not architectural plans, photographs of built places, or evidence of autonomous operation.

| Image | Origin and generation source |
| --- | --- |
| [Garden district](assets/garden-district.png) | Copied unchanged from the existing [vision overview](../vision-overview/README.md); [original prompt](assets/garden-district-prompt.txt) retained. |
| [House of Worlds](assets/house-of-worlds.png) | Newly generated with the built-in image tool; exact prompt in [prompts.json](assets/prompts.json). |
| [Open University](assets/open-university.png) | Newly generated with the built-in image tool; exact prompt in [prompts.json](assets/prompts.json). |
| [Material lives](assets/material-lives.png) | Newly generated with the built-in image tool; exact prompt in [prompts.json](assets/prompts.json). |

The three new images used independent `image_gen.imagegen` calls, with no reference images and no CLI/API fallback. Their [metadata](assets/generation-metadata.json) and [visual review](assets/visual-review.md) are retained. Source PNGs remain unchanged; the PDF encodes them as high-quality JPEG streams without reducing their pixel dimensions. Framing and cropping occur only in the page layout.

## Rebuild

From this folder, use the bundled Python runtime:

```bash
/Users/ren/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 build.py
```

The script needs ReportLab and Pillow. It defaults to the Noto Serif and Noto Sans fonts in the discovered bundled runtime. For another environment, pass `--font-dir /absolute/path/to/fonts` containing `NotoSerif-Regular.ttf`, `NotoSerif-Italic.ttf`, `NotoSans-Regular.ttf`, and `NotoSans-Bold.ttf`.

After editing, render every PDF page with Poppler and inspect it. Refresh the extracted reader text and QA report for the delivered edition. The initial PDF operation marker was run successfully before authoring this edition.

## Review and limits

All ten pages were visually reviewed for text placement, cropping, spacing, diagram clarity, and footer separation. Export encoding was then reduced for sharing; the five text-only pages rendered identically, and the five illustrated pages were reviewed again. Page count, selectable text, reference links, bookmarks, and embedded font resources were checked. The final edition passed without detected layout defects.

The cup diagram is a proposed service loop. The booklet retains the distinction between scenario assumptions and technical findings, and between reused stock and physical expansion. Images cannot establish reliable automation, safe construction, accessibility, sanitation, ecological performance, or good institutions. Those remain subjects for the project's next studies.
