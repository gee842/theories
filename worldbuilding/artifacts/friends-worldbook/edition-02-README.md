# Worlds we can inhabit

2026-09-07 · **Edition 02: A generative civilization** · A worldbuilding project by Ren, developed with AI.

**Read or share:** [Worlds we can inhabit — revised illustrated PDF](output/pdf/worlds-we-can-inhabit-v2.pdf). Fifteen portrait pages, approximately 5.7 MB, with selectable text, bookmarks, embedded text fonts, and clickable material references. No account or live service is needed to read it.

This edition begins with the meta-level: how shared understandings, human drives, stories, institutions, tools, and lived environments influence one another. It develops generativity as sustaining conditions from which further life and worlds can arise. Rockets, an inhabited MMORPG culture, and an elevator experienced as a portal now have dedicated illustrations and lived scenes.

## The revision

Ren's [correction](../../archive/006-ren-meta-level-and-worlds.txt) identified two failures in edition 01: the broader meta-level was missing, and the first illustration appeared twice. The revised book changes its organizing argument and uses **seven distinct source illustrations, each placed exactly once**. Its new cover shows inhabitants considering the worlds they could make together.

The [first PDF](output/pdf/worlds-we-can-inhabit.pdf), original copy, layout script, and [edition 01 notes](edition-01-README.md) remain as history. Their earlier layout checks did not establish that the vision had been adequately represented. Ren's [feedback screenshot](feedback/edition-01-duplicate-image.png) is retained alongside the correction.

## Inside edition 02

1. A new cover: collectively imagining the shared world.
2. The meta-level: a civilization that understands it is making a world.
3. Feedback: people, stories, rewards, institutions, and lived conditions.
4. Generative principles, including Ren's verified environmental-generativity quotation.
5. Autonomous productive capacity, secure access, and public knowledge.
6. The Living Garden: care as a way of inhabiting a city.
7. The Open University: understanding and embodied learning as ways of life.
8. The Exploration Community: a shared culture that builds rockets.
9. The City of Shared Quests: an inhabited, coauthored MMORPG-like world.
10. The House of Worlds: a full two-panel elevator passage between experienced realities.
11. Material inheritance: cups, components, and reusable buildings.
12. Recoverable transformation, circulation, and physical expansion.
13. Many worlds sharing one foundation; culture that learns from amplified will.
14. An invitation to imagine lives, cultures, dependencies, and further beginnings.
15. Authorship, primary-source roots, scenario scope, image provenance, and material references.

## Editable sources and checks

- [content-v2.json](content-v2.json): complete final copy, including the source page.
- [build-v2.py](build-v2.py): layout and PDF generation; rejects any repeated source-image hash.
- [reader-text-v2.txt](reader-text-v2.txt): text extracted from the delivered PDF.
- [image-placements-v2.json](image-placements-v2.json): exact page/image mapping, dimensions, and source SHA-256 hashes.
- [qa-report-v2.json](qa-report-v2.json): final export checks and review coverage.

The larger [generative-worldmaking foundation](../../foundations/generative-worldmaking.md) develops the philosophical account. The [bounded reading record](../../research/2026-09-07-meta-level-reading.md) identifies the theory excerpts and original human turns checked; it does not claim that the whole theories corpus was read. The [charter](../../foundations/charter.md) and [possibility map](../../foundations/possibility-map.md) now carry that account into future work.

## Images and their world briefs

| Page | Preserved source image | Development |
| --- | --- | --- |
| 1 | [Worldmakers' forum](assets-v2/worldmakers-forum.png) | New cover; [generative worldmaking](../../foundations/generative-worldmaking.md). |
| 6 | [Garden district](assets/garden-district.png) | Existing concept used once; [Living Garden](../../worlds/01-living-garden.md). |
| 7 | [Open University](assets/open-university.png) | Existing concept used once; [Open University](../../worlds/03-open-university.md). |
| 8 | [Exploration Community](assets-v2/exploration-community.png) | New rocket/community image; [expanded exploration brief](../../worlds/05-exploration-community.md). |
| 9 | [City of Shared Quests](assets-v2/shared-quest-city.png) | New inhabited MMORPG scene; [new world brief](../../worlds/06-city-of-shared-quests.md). |
| 10 | [Elevator as portal](assets-v2/elevator-as-portal.png) | New diptych, shown in full; [expanded House of Worlds](../../worlds/02-house-of-worlds.md). |
| 11 | [Material lives](assets/material-lives.png) | Existing concept used once; [material foundation](../../foundations/regenerative-material-civilization.md). |

The four new images used separate built-in `image_gen` calls. [Exact new prompts](assets-v2/prompts.json), [original output paths and metadata](assets-v2/manifest.json), and [asset review](assets-v2/README.md) are retained. The prior images' [prompts](assets/prompts.json), [metadata](assets/generation-metadata.json), and [garden prompt](assets/garden-district-prompt.txt) remain available. No CLI/API image-generation fallback or external reference image was used for this revision.

These are raster concept illustrations, not constructed places, editable 3D geometry, or engineering demonstrations. They express proposed experiences and architecture. The portal caption distinguishes physical elevator travel from the shared perceptual destination. Source PNGs remain unchanged; only their PDF streams are serialized as high-quality JPEGs at original pixel dimensions. Scene-page framing is a layout choice; the cover and elevator diptych retain their full 3:2 composition.

## Rebuild

From this directory:

```bash
/Users/ren/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 build-v2.py
```

Requires ReportLab and Pillow. The script defaults to the discovered runtime's Noto Serif/Sans fonts and the host's Arial Unicode font for the four Chinese characters. Elsewhere, pass `--font-dir /path/to/noto-fonts --cjk-font /path/to/a/compatible.ttf`. Font files are not copied into this project.

Render the PDF with Poppler after editing; inspect every changed page and confirm unchanged pages match the reviewed rendering. Update extracted reader text and QA records for the actual delivered bytes. A successful PDF edit-operation marker was recorded before authoring this revision.

## Review and next use

Content received an independent review against Ren's current request and checked primary passages. Every page received visual review for framing, text placement, diagrams, legibility, and footer separation. Final checks cover page count, selectable copy, Chinese text, bookmarks, material-reference links, embedded fonts used for text, and seven unique image placements both in the source manifest and actual PDF drawing operations.

This booklet is ready for Ren to share. It has not been sent to other people or published. The illustrations also give the project three concrete next spatial studies: a public spacecraft hall, an inhabited quest street, and an elevator's physical/perceptual passage. The [roadmap](../../process/roadmap.md) keeps those branches available alongside the garden and university.
