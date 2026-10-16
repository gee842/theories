# Point-in-time audit of scattered theory work

Read-only audit at **2026-10-05T16:51:33.244488**, repository HEAD `5f40dc01d6d0a3515dc24f5afbf8beace169635c`. Full machine-readable inventory: `/tmp/theories-scatter-audit.json`.

**82 unique missing byte contents, totaling 2,382,307 bytes, should be preserved from this snapshot.** This includes four original ZIP containers (759,657 bytes); their member contents are otherwise present in the tracked repository or inspected loose files. The other **78 unique contents total 1,622,650 bytes**. Missing means absent from the current tracked working-tree files, not a claim about every historical Git blob or semantic novelty.

The scan compared **2,693 external files / 1,519 unique contents** with **7,179 tracked paths**, using SHA-256 and byte size. No read errors or file changes during individual reads were detected. Other chats are active: this is a dated snapshot, not a guarantee that their files will remain unchanged. Verify the source hash immediately before import, retain the actual imported hash, and flag any changed source.

| Workspace | Inspected files | Exact tracked matches | Unique missing | Missing bytes |
|---|---:|---:|---:|---:|
| causal-foundations | 13 | 3 | 10 | 100,908 |
| fo | 257 | 212 | 45 | 1,412,712 |
| full-picture-conjecture | 482 | 482 | 0 | 0 |
| recursive-self-modeling | 400 | 400 | 0 | 0 |
| root-of-wisdom | 598 | 571 | 27 | 868,687 |
| scientific-principles | 160 | 160 | 0 | 0 |
| sin | 663 | 663 | 0 | 0 |
| structural-foundations | 119 | 119 | 0 | 0 |
| task visualization | 1 | 1 | 0 | 0 |

## What to preserve and index

- **Causal foundations:** all 13 source files deserve a direct reading index, but only its 10 `work/` files add missing bytes (100,908 bytes). Its three outputs already exist exactly inside earlier root-of-wisdom/cross-session snapshots. The missing material is the research log, conceptual and formal audits, verification scripts, and results.
- **Root of wisdom:** 27 missing files (868,687 bytes) cover the three newer studies `conditions-of-generativity`, `renewing-access-to-support`, and `shared-generative-direction`: prose, mathematics, numerical evidence, SVG/PNG figures, checks, scripts, and preservation manifests. Include each study's corresponding `work/` verification as well as its outputs.
- **This unification workspace (`fo`):** 45 missing contents (1,412,712 bytes). The genuinely recent research includes eight files in `work/development-02/`, including joint-formation mathematics, prior art, conceptual review, obstruction analysis, and independent verification. Additional missing bytes include development-01 internal review/tool variants and original export versions with different links or historical content. Preserve those versions as provenance rather than treating every export as a new theory.
- **Task visualization:** `protection-and-evasion.html` is already preserved exactly at `_process/research/2026-10-05-direction-frontier/protection-and-evasion.html` (SHA-256 `2cc5366509306ffbb79eca91ca155f5f829c05c504db705bb6a8814080939002`, 6,335 bytes). No new copy is needed for completeness; index its existing path.

The JSON contains every inspected absolute path, SHA-256, byte size, exact tracked matches, deduplicated content groups, preferred missing-source path, archive member hashes, and exclusions with reasons. The root task can import each missing hash once and preserve all original-path mappings.

## Duplicate exports and existing preservation

All inspected substantive bytes in **full-picture-conjecture, recursive-self-modeling, scientific-principles, sin, and structural-foundations** already have exact tracked counterparts. Their export/reproduction directories should be mapped, not blindly recopied.

Within `fo/outputs`, `concern-theory` has 17/18 files already represented, `revisable-concern` 27/28, and `direction-of-regeneration` 13/14; the lone unmatched file in each is delivery metadata. `unified-theory` has 9/19 and `unified-theory-development-01` 61/73 exact matches; their unmatched versions are historical/portable export variants and should retain provenance. All four unmatched ZIP files contain no member content unique to the archive.

- `2026-10-05/recursive-self-modeling/outputs/recursive-self-modeling-research.zip` has 4 member versions not present as loose files, but the complete archive itself is byte-identical to a tracked repository file. Members: `claims.md`, `decisions-and-next-test.md`, `research.md`, `sources.md`.

## Deliberate exclusions and scope

Excluded installed dependencies and reproducible caches, not research evidence. In particular:

- `2026-10-05/full-picture-conjecture/work/access-study/plot-libraries`
- `2026-10-05/root-of-wisdom/work/endogenous-renewal/mpl-cache`
- `2026-10-05/root-of-wisdom/work/renewing-access/mpl-cache`
- `2026-10-05/root-of-wisdom/work/conditions-of-generativity/mpl-cache`
- `2026-10-05/scientific-principles/work/integrated-inquiry/plot-deps`
- `2026-10-05/scientific-principles/work/integrated-inquiry/mpl-cache`
- `2026-10-05/recursive-self-modeling/work/plot-env`
- `2026-10-05/fo/work/development-01/mpl-cache`

All `__pycache__`, standalone `.pyc`/`.pyo`, `.DS_Store`, and analogous cache paths are also excluded; the complete 34-path exclusion list is in JSON. Downloaded primary-reference PDFs, reproducible experiment traces, numerical arrays, output figures, and evidence archives were retained in the comparison. The 55 MB inherited-evidence JSONL and 23 MB compressed inquiry traces are already tracked, so their size is not a reason to discard them.

`i-x20` and `w` were empty. `2026-10-04/p` is unrelated worldbuilding and excluded from the final inventory. The repository currently has active untracked `experiments/joint-formation/` work; it was not used to claim tracked preservation and must not be overwritten or deleted. The root task is responsible for committing that live work at its chosen checkpoint.

No repository or original workspace file was modified by this audit.
