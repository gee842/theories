# Independent reconciliation review

5 October 2026. **Verdict: passed within the declared consolidation scope. No blocking discrepancy found.** Repository files were not modified by this review.

## Preservation and exact editions

- Independently computed hashes and byte lengths for all **2,689 manifest mappings**. Every repository target exists inside the repository and matches its recorded source bytes.
- Confirmed the new-source file set contains exactly **80 files, totaling 1,647,588 bytes**.
- Opened all four omitted delivery ZIPs independently, checked their hashes, enumerated their complete file membership, and verified all **138 members** against both recorded hashes and repository copies.
- Checked all **34 reading-edition source and destination hashes**. Reconstructed each edition from its preserved original using only the recorded Markdown link-target substitutions. Exactly **three files contain seven link adaptations**; every other byte matches. Scientific prose, equations, figures, programs, and saved evidence were not strengthened or otherwise changed by those transformations.
- Reconstructed the three existing documents affected by **ten live-link repairs** from base commit `5f40dc01d6d0a3515dc24f5afbf8beace169635c`. Their current bytes differ only by those recorded replacements.
- `sources/20-codex-theory-sessions-2026-10-05` has **no diff against that base commit**. The earlier snapshots remain unchanged by this consolidation.

## Navigation and provenance

Independently checked the declared **62-document reading scope and 692 local live links** at review time: every target exists, is repository-contained, and is relative rather than an absolute workspace path. Frozen historical source internals and the separately active joint-formation additions are outside that documented live-reading scope. An earlier broader sample of 509 links likewise found no unresolved or outside-repository target.

All **16 workspace entry-point records** match their actual files, text, and hashes. The new repository instructions consistently make repository studies primary while retaining historical exports and original provenance.

Reviewed RESEARCH.md, AGENTS.md, the source-22 README and location map, both new study READMEs, the reconciliation README and verifier, and the tracked navigation changes. They consistently distinguish preservation from scientific validation, source reports from integrated conclusions, ongoing development from completed results, and AI-assisted elaboration from Ren's authorship. I found no newly strengthened scientific claim in the consolidation text. The content-preserving edition checks provide the stronger assurance for the imported study bodies.

The repository's own verifier was inspected and then run without modification; it also passed with **2,689 mappings, 138 archive members, 34 editions, and 692 links across 62 documents**. The independent calculations did not rely on that verifier's hash or transformation implementation.

## Dated-capture qualification

Three external `fo/work/development-02` files changed after the recorded capture: `check_joint_math.py`, `conceptual-review.md`, and `joint-formation-math.md`. Their preserved repository snapshots still match the manifest. This is consistent with the explicitly active separate study and does not indicate failed preservation. This review does not certify those later changes or the newly appearing joint-formation companions.

No scientific experiments were rerun for this organizational review. External URLs, rendered layout, and every historical source link were not verified. Counts describe the review-time state; subsequently added record links may increase the live-link count without changing the preservation result.

Machine-readable independent findings are saved at `/tmp/theories-reconciliation-independent.json`.
