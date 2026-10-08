# Recent theory research: repository and navigation audit

Read-only audit, 5 October 2026. Repository: `/Users/ren/theories`. No repository files changed. The coordinator is concurrently integrating the work, so this records the inspected state and recommendations rather than a claim about the eventual release.

## Conclusion

The recent direction, concern-formation, and revisable-concern packages are already present in full authored research directories and already summarized in the main 生生 theory README. The main deficiency is discoverability and portability, not a need to move or duplicate those packages.

The coordinator's proposed **single root `RESEARCH.md`** is the simplest cross-branch reading index. Root `README.md`, the theory README's current opening, and unified `START-HERE.md` should point to that index. Keep the existing detailed reports, proofs, checks, source records, and experiments at their current paths. Do not build a second competing current-research table inside the unified guide.

An independent scoped link audit inspected 57 current documents and 601 local Markdown links. It found **no missing file targets or broken local anchors** in that scope. Ten links resolve only because this machine has `/Users/ren/theories`; those should become relative links. Fourteen original workspace references are code-quoted review/provenance strings, not broken live links.

## What is already in the repository

| Role | Existing location | Recommended treatment |
|---|---|---|
| Canonical current interpretation and genealogy | `theories/becoming/README.md` | Keep its current summaries and preserved historical formulation; add a concise pointer to root `RESEARCH.md`. |
| Unified foundation, formal core, formation, ethics, and concern–correction interface | `theories/becoming/chapters/` | Keep as the integrated foundation. Link to later branches rather than copy their complete reports into this directory. |
| Direction hypothesis and costed formation | `_process/research/2026-10-05-direction-frontier/` | Existing `EXPLORATION.md`, mathematical/conceptual/literature notes, checks, review, interactive model, and research record remain together. |
| Concern formation, widening, correction, and succession | `_process/research/2026-10-05-concern-theory/` | Existing reading guide, theory, claim register, two formal notes, evidence, reviews, and exact programs/results remain together. |
| Revision of scope and strategic access | `_process/research/2026-10-05-revisable-concern/` | Existing guide, theory, claims, scope/access proofs, provenance/context, reviews, and independent checks remain together. |
| Integration work and review history | `_process/research/2026-10-05-unified-theory/` | Preserve working/review records here. The existing `direction-synthesis.md` is the repository counterpart of the old workspace memo. |
| Earlier inquiry and selection progression | `_process/research/2026-10-04-integrated-evolution/` and relevant `experiments/` packages | Retain their existing index and experiment entry points; the new root index should link into that progression. |
| Completed original session snapshots | `sources/20-codex-theory-sessions-2026-10-05/` | Preserve the original manifest, completion supplement, and session context. Do not rewrite frozen report links or merge later bytes into this snapshot. |
| Authorship record for first unified development | `sources/21-unified-theory-development-2026-10-05/README.md` | Keep its dated scope. It accurately covers the first development and concern interface, not every later branch. |
| Authorship records for later branches | `sources/15-codex-theory-conversations/2026-10-05-direction-and-generalized-concern.md`, `2026-10-05-formation-and-renewal-of-concern.md`, `2026-10-05-revising-the-scope-of-concern.md` | Already catalogued in `sources/SOURCES.md`; retain these records and use them as provenance links. |

The root index should give each branch a question, present status, primary reading link, proof/check link, and provenance link. Labels such as **integrated foundation**, **completed conditional research**, **preserved source report**, and **in progress** will prevent a source archive from being mistaken for a new verification or canonical endorsement.

## Minimal navigation changes

1. **Root `README.md:7`:** point to `RESEARCH.md` as the current map. Its current text names the formation and ethics development but leaves the newer concern and scope-revision chapters several clicks away.
2. **Unified `START-HERE.md`:** add a short current-research paragraph pointing to `../../../RESEARCH.md` and explicitly noting the later scope-revision continuation. Its existing reading list ends at the concern–correction interface.
3. **Unified `SOURCE-MAP.md`:** add the coordinator's proposed S20 for revisable concern and S21 for newly preserved causal/provenance work. S19 already covers concern formation, direction, and the one-period interface. Avoid counting their already saved tests as new runs.
4. **Theory `README.md`:** its current sections already cover direction, concern, formation, and revisable concern. A short index pointer is enough; do not replace or duplicate its large genealogy. The current synthesis status remains authoritative where historical claims differ.
5. **`experiments/README.md`:** add omitted existing experiment entry points, with brief scoped descriptions. Root `README.md:27` should link to this experiment index rather than expose only circular construction as the example.
6. **Root corpus dates:** `README.md:3` still says “2021 to September 2026,” although the current work is dated October. `README.md:48` describes `sources/` as one September 3 snapshot. Update the latter to distinguish the original snapshot from later dated additions, while preserving the rule against editing originals.

At inspection the experiment index listed eight of fifteen experiment directories. Completed-looking directories with a README but no index row are:

- `constructed-correction/`
- `guardian-anarchy/`
- `integrated-correction/`
- `recurrent-inquiry/`
- `revisable-inheritance/`
- `situated-discovery/`

`joint-formation/` had a frozen protocol and timing clarification but no README. Its `model.py`, `study.py`, and `results/` appeared as untracked active work during this audit. Link its protocol as **in progress** until its owning session finishes and supplies its actual release status. This observation is not permission to collect another session's unfinished work into a completed-results claim.

## Ten nonportable live links

All targets exist locally. Replace only the link target strings in these current authored documents, not the source contents they cite.

| File and line | Suggested relative target |
|---|---|
| `theories/becoming/chapters/ETHICAL-FOUNDATION.md:3`, conscience link | `../../../sources/15-codex-theory-conversations/2026-10-05-conscience-and-universal-morality.md` |
| Same file and line, unified-theory link | `THEORY.md` |
| `theories/becoming/chapters/FORMATION-PRIOR-ART.md:11` | `../../../experiments/continuing-participation/README.md` |
| Same file:12 | `../../../sources/15-codex-theory-conversations/2026-10-05-selection-and-continuity-of-renewal.md` |
| Same file:13, formation results | `../../../experiments/integrated-correction/general-framework/gap-resolution/formation-coupled/RESULTS.md` |
| Same file:13, reopening extension | `../../../experiments/integrated-correction/general-framework/gap-resolution/formation-coupled/REOPENING-RESULTS.md` |
| Same file:15 | `../../../sources/15-codex-theory-conversations/2026-10-05-continuing-participation-and-funded-correction.md` |
| `_process/research/2026-10-05-direction-frontier/EXPLORATION.md:29` | `../2026-10-04-integrated-evolution/selection-of-renewal.md` |
| Same file:140, unified theory | `../../../theories/becoming/chapters/THEORY.md` |
| Same file:140, conscience proposal | `../../../sources/15-codex-theory-conversations/2026-10-05-conscience-and-universal-morality.md` |

These root-absolute targets will otherwise be interpreted as website-root paths by a hosted repository and will not work for another local checkout.

## Absolute workspace strings: provenance versus reading links

The scoped `/Users/ren/Documents/Codex/...` occurrences are in:

- Direction `formation-review.md:5–7,163`.
- Concern `RESEARCH-RECORD.md:11` and `conceptual-evidence.md:234–236`.
- Revisable concern `RESEARCH-RECORD.md:13`, `conceptual-evidence.md:195`, and `conceptual-review.md:67–70`.

They record where a review was performed or where a delivered copy existed. They are not live Markdown links and should not be mechanically rewritten as if they were erroneous historical claims. The old `work/direction-synthesis.md` reference has an existing counterpart at `_process/research/2026-10-05-unified-theory/direction-synthesis.md`.

For author-facing `RESEARCH-RECORD.md` destination sentences, a small optional improvement is to provide a relative repository source link and describe the workspace output as an export at the time of release. For preserved review memos, a single note in the current index or reconciliation manifest explaining original workspace paths is sufficient. Do not rewrite every historical reference to create apparent original provenance it did not have.

## Proposed reconciliation archive and repository policy

The coordinator's planned `sources/22-research-reconciliation-2026-10-05/` is appropriate for unique authored material that the hash audit finds absent, including newer root-of-wisdom reports. It should be an append-only reconciliation of sources, not a replacement canonical theory.

Use the manifest to map each original file to either an existing byte-identical repository path, a newly archived path, or an explicit exclusion reason. Preserve exact bytes for selected originals. Cache directories, compiled interpreter artifacts, temporary dependency installations, and mechanically regenerated duplicates do not need to become research history merely because their hashes differ. Conversely, unique authored reports, code, results, declared protocols, and meaningful review records should not disappear simply because a cleaner export exists.

The newly found `conditions-of-generativity`, `renewing-access-to-support`, and `shared-generative-direction` reports should initially be labelled **newly preserved latest source reports** unless their substantive conclusions have been independently integrated and reviewed. Archive inclusion is not evidence of validation or a completed causal bridge.

A concise repo-first `AGENTS.md` can prevent this problem recurring: keep new durable research and its reproducibility records inside the declared repository layers; permit temporary scratch; integrate durable outputs with source provenance and portable links; preserve previous snapshots. It should not require a new parallel research folder per session or retroactive moves of established packages.

## Scope and verification limits

Inspected the repository root and theory entry points; all unified top-level Markdown files; recent direction/concern/revisable-concern packages; current experiment index and entry points; source catalogue and session snapshot layout; three branch source records; and the first unified-development provenance record. A delegated read-only check supplied the 57-document, 601-link result and exact ten-link repair list; the coordinator independently inspected the affected targets and navigation gaps.

This is a navigation and preservation audit. It does not newly verify the theory, all external URLs, frozen source internals, rendered output, or the changing joint-formation experiment. Existing source snapshots and concurrent work were not modified.
