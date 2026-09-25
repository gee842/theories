---
name: Operator metadata + signature seed layer (c27901d, 2026-05-07)
description: New Text/OperatorSignatures.lean (14 seeds) + extended OperatorReadings.lean (precedence/expectedTypes/construction) infrastructure available; WenyanParser does NOT yet use it
type: project
originSessionId: 0e41811f-cbc6-4d9b-b2bf-291360840d4b
---
Commit c27901d (codex/wenyan-polysemy branch, pulled into pensive-meitner-c79a1f worktree 2026-05-07) added a parser-support metadata layer:

- `Text/OperatorSignatures.lean` (new, 89 LOC): `SignatureKind` (7 cases: app/endoComp/propImp/instrument/objectEndo/propUnary/opUnary), `ExactOperatorSignature` struct, `exactSignatureSeed` list of 14 entries for `之/而/以/故/反/復/错/综/互/损/益`. 5 theorems verified by native_decide.
- `Text/OperatorReadings.lean`: `OperatorReading` struct now has `precedence : Nat`, `expectedTypes : List ExpectedType` (14 cases), `construction : ConstructionKind` (12 cases) fields. Helper fns `expectedTypeOfCue` / `precedenceOfCues` / `constructionKindOf` derive these from existing `cues : List ContextCue`. All 193 reading rows now carry metadata.
- `Foundation/Bagua/Cell192.lean`: 2 new theorems `hexCuo_hexZong_comm`, `hexCuoZong_hexCuoZong` (cell-level 错综 group law).
- `Text/OperatorCellMap.lean`: `functionalCompletionRows` now has 9 rows incl. new `exactSignatureSeeds` tracked layer.
- Wenyan CLI binary in this worktree exposes `wenyan signatures` and `wenyan readings <char>` to browse the layer from the terminal.

**Why:** Builds toward parser disambiguation for polysemous CJK glyphs (e.g. `之` as genitive vs anaphora vs path-source). Currently WenyanParser only recognizes `«»` reserved tokens, so this metadata is **not yet wired into parsing** — the wenyan-operators.md follow-up explicitly calls out "后续需让 parser 真正使用这些 metadata".

**How to apply:**
- For parser-disambiguation work in WenyanParser/WenyanParserGeneral, this metadata is the canonical source of precedence and expected-type info — query `allSurfaceReadings` / `coreMultiReadingTable` / `signatureFor?`.
- Don't conflate the 14 signature seeds with full coverage — only `complete` for 14 of 371 catalogue ops; the rest is `pending`.
- This layer is purely additive; does not change existing M1 parser behavior. Existing `«解程»` / `«印程»` continue to work unchanged.
- The full plan including this layer's place in the wenyan-as-language roadmap is at `/Users/ren/.claude/plans/lean-snoopy-elephant.md`.
