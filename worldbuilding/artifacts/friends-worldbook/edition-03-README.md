# Worlds we can inhabit

2026-09-07 · **Edition 03: From existing capabilities to shared futures** · A worldbuilding project by Ren, developed with AI.

**Read or share:** [Worlds we can inhabit — third edition](output/pdf/worlds-we-can-inhabit-v3.pdf). Twenty-one illustrated pages, approximately 6.5 MB, with selectable text, bookmarks, embedded text fonts, and clickable source references.

This edition restores the argument that gives the worlds a practical starting point: **existing knowledge and machinery → productive capacity that helps build more capacity → conditional compounding → abundant shared provision and creative means → freedom from compulsory labor → generative civilization-building.** It joins that argument to the meta-level, regenerative materials, and the full range of imagined lives.

## What changed

Ren's [technical-foundation correction](../../archive/007-ren-technical-foundation-and-next-version.txt) identified a missing reason for taking the future seriously. Six opening chapters now explain what is already operating, what AI adds, why productive expansion can compound, how to pursue a working network, and how shared capacity can free people from livelihood coercion. A new production-commons illustration makes the machinery and its proposed social purpose visible.

The strong thesis that present knowledge and AI make full automation an engineering undertaking is represented explicitly. Current deployments and demonstrations are sourced. The book also distinguishes them from the unverified sufficiency of today's models for every required task and the proposed complete autonomous supply network. That distinction defines a concrete construction program rather than treating abundance as an unexplained fictional assumption.

Free association is one freedom made practical by abundant means. The account also explains the systems that make collective creation work: provision, tools, coordination, maintenance, shared knowledge, and learning from consequences. Its aim includes generous lives and ambitious projects, beyond a minimal survival floor.

## Reading path

| Pages | Content |
| --- | --- |
| 1–7 | Existing capabilities, machines making machines, adaptable AI, productive expansion, a practical engineering program, and freedom from compulsory labor. |
| 8–10 | The meta-level: people and worlds forming one another, constructive feedback, and generative principles. |
| 11–15 | Living Garden, Open University, rocket-building Exploration Community, City of Shared Quests, and the elevator experienced as a portal. |
| 16–19 | Regenerative material lives, recoverable transformation, shared consequences, and an invitation to build. |
| 20–21 | Seven technical evidence cases, authorship and source roots, image status, and material references. |

## Theory and evidence

- [From automation to shared abundance](../../foundations/automation-to-shared-abundance.md): the complete new technical and social argument, including the conditional growth model.
- [Updated cooperative-abundance theory](../../../theories/the-fork-and-cooperative-infrastructure/README.md): the wider theory now foregrounds productive recursion and freely created worlds. Its previous version is preserved.
- [Abundance source reading](../../research/2026-09-07-abundance-source-reading.md): directly checked human passages from the older archive, including factories/robots, luxurious necessities, freedom from exploitation, and collective creation.
- [Industrial automation evidence](../../research/2026-09-07-industrial-automation-evidence.md): six primary cases covering robot and equipment production, factory manipulation, industrial logistics, and construction.
- [AI engineering evidence](../../research/2026-09-07-ai-engineering-evidence.md): five primary cases covering physical planning, generalization, deployed tasks, simulation training, and improving productive computation.
- [Generative worldmaking](../../foundations/generative-worldmaking.md) and [material foundation](../../foundations/regenerative-material-civilization.md): the orientation and material continuity that productive power should serve.

The evidence is a bounded reading of company reports and research papers, not an independent industrial audit. The project's own extrapolations and proposed institutions remain identifiable. No doubling time or numerical deployment forecast is assigned.

## Editable sources and verification

- [content-v3.json](content-v3.json): complete copy and technical-reference metadata.
- [build-v3.py](build-v3.py): the PDF layout, diagrams, hyperlinks, and export settings.
- [reader-text-v3.txt](reader-text-v3.txt): text extracted from the delivered PDF.
- [image-placements-v3.json](image-placements-v3.json): page, source file, dimensions, and SHA-256 for each image.
- [qa-report-v3.json](qa-report-v3.json): final file hash, complete-copy verification, source links, fonts, image uniqueness, and page-review record.

Every page received visual review. Independent substantive review checked the new causal argument and source matching. The export contains twenty-one bookmarks, twenty-four link annotations pointing to ten distinct sources, five embedded fonts used for text, and eight image drawing operations with eight unique image hashes. Greek and Chinese text render correctly. No image is placed twice.

## Illustrations

| Page | Source image | Role |
| --- | --- | --- |
| 1 | [Worldmakers' forum](assets-v2/worldmakers-forum.png) | People shaping the shared future. |
| 3 | [Production commons](assets-v3/production-commons.png) | New illustration of robot manufacture, material movement, and factory expansion. |
| 11 | [Garden district](assets/garden-district.png) | Care and ordinary life. |
| 12 | [Open University](assets/open-university.png) | Understanding and embodied learning. |
| 13 | [Exploration Community](assets-v2/exploration-community.png) | A community building rockets. |
| 14 | [Shared quest city](assets-v2/shared-quest-city.png) | Persistent MMORPG-like culture. |
| 15 | [Elevator as portal](assets-v2/elevator-as-portal.png) | Same physical cabin, different experienced worlds. |
| 16 | [Material lives](assets/material-lives.png) | Parts and materials available for further use. |

The new image used one built-in `image_gen` call. Its [exact prompt](assets-v3/production-commons-prompt.txt), [generation metadata](assets-v3/production-commons-metadata.json), and [inspection notes](assets-v3/README.md) are preserved. Earlier [v2 prompts and provenance](assets-v2/README.md), [original prompts](assets/prompts.json), [original metadata](assets/generation-metadata.json), and [garden prompt](assets/garden-district-prompt.txt) remain available. No CLI/API image-generation fallback was used.

All illustrations are raster concepts. They are not evidence of built systems or editable 3D geometry. The production image imagines a commons; the evidence is in the cited operating examples. The portal is perceptual, with conventional physical elevator travel. Original PNGs remain unchanged; the PDF serializes them as high-quality JPEG streams at their original pixel dimensions. Framing occurs in page layout.

## History

- [Edition 01 PDF](output/pdf/worlds-we-can-inhabit.pdf) and [notes](edition-01-README.md): first introduction, ten pages; underrepresented the meta-level and repeated its opening image.
- [Edition 02 PDF](output/pdf/worlds-we-can-inhabit-v2.pdf) and [notes](edition-02-README.md): fifteen pages; restored generative worldmaking and the wider worlds, but did not adequately explain their productive foundation.
- Edition 03 preserves both earlier versions and integrates technical, cultural, material, and lived-world arguments.

## Rebuild

From this folder:

```bash
/Users/ren/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 build-v3.py
```

Requires ReportLab and Pillow. It defaults to the discovered runtime's Noto Serif/Sans fonts and the host's Arial Unicode font for Chinese characters. Elsewhere, pass `--font-dir /path/to/noto-fonts --cjk-font /path/to/compatible.ttf`. Fonts are not copied into the project.

A successful PDF edit-operation marker was recorded before authoring this edition. After changes, render with Poppler, inspect the pages, and refresh reader text and QA for the actual export. The build rejects duplicate source-image hashes. Final verification also inspects image drawing operations in the PDF itself.

The artifact is prepared for Ren to share. It has not been sent to other people or published.
