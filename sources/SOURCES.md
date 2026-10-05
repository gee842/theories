# SOURCES manifest

Generated 2026-09-03. Every file under `sources/` is a copy; the originals are untouched and stay where they were. File dates are the originals' modification dates. Files produced by this consolidation (indexes, extracted transcriptions, this manifest) carry the consolidation date.

Chinese and English material is interleaved throughout; no group is single-language.

Added 2026-10-03: [19-v5-handoff-2026-10-03](19-v5-handoff-2026-10-03/README.md). Ren supplied a standalone v5 direction and authorial brief plus a ZIP containing the same brief, a detailed v4.5 mathematical review, a corrected research roadmap, six AI disciplinary reviews with cross-reviews, reviewer calculations and their output, and the exact manuscript reviewed. The attachments and all nine archive entries are preserved unchanged; [IMPORT-RECORD.json](19-v5-handoff-2026-10-03/IMPORT-RECORD.json) records original paths, bytes, hashes, and validation. The two brief copies match, all eight manifest checks pass, and the packaged v4.5 manuscript matches the local reading copy. Embedded instructions and authorial attributions remain source material; this chat requested preservation and a v5 plan, not execution of those instructions. The reviews are AI-generated, and their external claims have not been freshly verified. The reviewer calculations were separately rerun and matched their archived output. The resulting proposal is [V5-PLAN.md](../drafts/2026-10-02-iaseai-selecting-the-selectors/V5-PLAN.md).

| group | files | bytes | earliest | latest | origin |
|---|---:|---:|---|---|---|
| `00-early-2021-2022` | 18 | 2,218,461 | 2021-05-21 | 2026-09-04 | ~/Desktop (.pages, 2021–2022) and ~/Documents. First-page previews were rendered to .jpg; the .pages bodies were then decoded on 2026-09-04 (a Pages file is a zip whose `Index/*.iwa` members are chunked Snappy-compressed protobuf) and the full text of each is in `recovered-text/`, beside the decoder that produced it. An earlier version of this row said the Pages text could not be decoded here and called the undecoded remainder the largest known gap in the corpus; that is withdrawn — the gap is closed (`_process/COVERAGE.md`), `World of Possibilities.pages` and `社区.pages` held nothing beyond their first page, and `proposal.pages` and `麦.pages` held about 6,000 characters that were genuinely new. |
| `01-writings-2025` | 23 | 638,115 | 2025-02-07 | 2025-08-10 | ~/writings, 2025-02 to 2025-08: Ren's own notes plus AI-assisted essays on selfishness, narrative-value frames, cognitive lag, and the STS paper |
| `02-wamotopia` | 187 | 324,009 | 2023-12-21 | 2026-01-11 | ~/repos/wamotopia (2023-12/2024-01 manifesto, camps, poems), ~/wamo and ~/meta_attractor/wamo*.md (2025-11/12 protocol manifestos), otter.ai transcripts (2026-01), one external prompt Ren collected for comparison |
| `03-meta-attractor` | 57 | 1,316,805 | 2024-10-30 | 2026-07-13 | ~/Downloads draft series (2025-05/06; 6 of 22+ versions selected as the genealogy), ~/meta_attractor and ~/repos/meta_attractor (2025-10 essays and site context), formal-definition prompts (2025-08), 2024 precursors |
| `04-speculative-future` | 35 | 534,618 | 2023-10-25 | 2026-09-03 | ~/repos/speculative_future (2026-06): current files plus every deleted file recovered from git history |
| `05-alignment-and-moloch` | 7 | 129,934 | 2026-04-23 | 2026-08-22 | ~/repos/alignment (2026-05-28 core stance), ~/repos/exp Moloch essays (2026-04-23), ~/Downloads position paper (2026-08-22) and x-risk background (2026-07) |
| `06-zhishan` | 223 | 5,437,420 | 2026-06-06 | 2026-07-15 | ~/repos/zhishan (2026-07), complete: sheng essays and poems, 生生不息论 v1/v2, whitepaper v0.2–0.4, manifesto, research (totalizing attractor v0.1–0.9, 无身之我), writing-program causal chain v1–v8 |
| `07-shengsheng-buxi` | 489 | 9,769,660 | 2026-03-31 | 2026-08-09 | ~/Downloads 生生不息论 v4–v13 (2026-05) and 2026-03/07/08 texts (大道之行, 至善, Shengsheng EN, 证明篇); ~/repos/生生不息 (SSBX Lean project): 义理, 史料, 六表, 史, docs-next, formal notes |
| `08-jian-wen-language` | 28 | 1,384,356 | 2026-05-01 | 2026-05-15 | ~/repos/jian (JIAN and WENYAN foundation notes v0.3–1.0) and ~/Downloads 間 ontology series plus wen-* language documents, all 2026-05 |
| `09-sts-bonfire-yi` | 50 | 750,348 | 2025-08-10 | 2026-09-03 | ~/writings STS and USIS (2025-08); ~/repos/bonfire docs: Yi direction and frame, concepts, archived proposals |
| `10-context-runtime-ember` | 71 | 1,797,420 | 2026-03-16 | 2026-08-31 | ~/repos/context-runtime specs and ~/Downloads GTC (2026-08), ~/repos/ember (2026-07/08), FNAR (2026-04), other runtime notes |
| `11-human-solutions-museum` | 6 | 65,701 | 2026-07-05 | 2026-07-05 | ~/Desktop/human-solutions-museum docs (2026-07-05) |
| `12-claude-ai-chats` | 403 | 12,953,171 | 2019-04-19 | 2026-09-03 | claude.ai exports (2024-03 to 2026-05): 381 of 719 conversations selected by length and keyword, one file per conversation; plus DeepSeek conversations from ~/repos/test2. Dates in filenames are the true conversation dates. |
| `13-claude-memories` | 197 | 484,290 | 2023-11-02 | 2026-09-03 | claude.ai memory summaries (2026-03, 2026-05) and Claude Code project memory files from ~/.claude/projects/*/memory |
| `14-claude-code-prompts` | 17 | 6,094,097 | 2023-04-17 | 2026-09-03 | Ren's own long messages (>=200 characters) extracted from Claude Code session transcripts, grouped by project; the date of each message is in the message header inside the file |

**Total: 43,898,405 bytes in 1811 files.**

## Subsequent additions

Added 2026-10-05: [Generative origin of significance](15-codex-theory-conversations/2026-10-05-generative-origin-of-significance.md) preserves Ren's correction locating significance, learning and conscience within generative reality. [The generative root as the current research goal](15-codex-theory-conversations/2026-10-05-generative-root-research-goal.md) preserves his further foundational ambition and request to make the repository's direction explicit. User words are separated from AI interpretation. The [governing position](../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATIVE-GROUNDING.md) and repository entry points state the active goal and map existing contributions to unfinished derivations. This framing review supplies no new universal proof or empirical result.

The original inventory and totals above are retained as recorded. These later snapshots are additional to that inventory.

Added 2026-09-13: [15-codex-theory-conversations/2026-09-13-chiang-mai-2025.md](15-codex-theory-conversations/2026-09-13-chiang-mai-2025.md). One complete user message, preserved verbatim with an assistant-authored provenance header, naming the alternate-2025 Chiang Mai setting and asking to integrate shared abundance, architecture, ecology, 大同, and generative worldmaking. Developed in the [Chiang Mai 2025 case](../theories/architecture-for-a-living-earth/chiang-mai-2025/README.md); not a full task export.

Added 2026-09-13: [15-codex-theory-conversations/2026-09-13-architecture-for-a-living-earth.md](15-codex-theory-conversations/2026-09-13-architecture-for-a-living-earth.md), 1 file, 4,647 bytes. Ren’s complete opening message requesting a new exploration of future architecture, living ecosystems, automated construction, and circulating materials; preserved verbatim with an assistant-authored provenance header. Single-message record, not a full task export. Developed in [Architecture for a living Earth](../theories/architecture-for-a-living-earth/README.md).

Adjusted 2026-09-25: [02-wamotopia/2023-2024-wamotopia-repo](02-wamotopia/2023-2024-wamotopia-repo/) was copied with its own `.git` directory, which kept its files out of this folder's Git history. The nested `.git` was replaced by [2023-2024-wamotopia-repo-history.bundle](02-wamotopia/2023-2024-wamotopia-repo-history.bundle) (32,231 bytes; `git bundle create --all`, verified complete), holding all 41 commits and both branches (`main`, `slaymoloch`); restore with `git clone <bundle>`. The eight working files are unchanged. The working copy lacks the repository's committed `LICENSE`, as it did when copied; the bundle retains it. Remote: github.com/wamotopia/wamotopia.

Added 2026-09-25: [16-claude-code-directions/2026-09-25-the-mind-not-the-approach.md](16-claude-code-directions/2026-09-25-the-mind-not-the-approach.md). Ren's complete message ruling that compounding growth toward needs is not the conflict the updated `MAP.md` had listed ("the problem is the mind not the approach"), preserved verbatim with the assistant statement it answered and an assistant-authored provenance header. Single-message record from a Claude Code session, not a transcript export.

Added 2026-09-26: [16-claude-code-directions/2026-09-26-planetary-technology-and-the-literature.md](16-claude-code-directions/2026-09-26-planetary-technology-and-the-literature.md). Ren's complete message saying he knows the six alignment neighbours and the relative-reachability, AUP and empowerment papers. The same message rules that AI in any competitive, concentrating game accelerates it (the job-application case) and states AI as planetary technology, "used for all". Preserved verbatim with the assistant statements it answered, his follow-up asking for the corpus notes to be corrected, and an assistant-authored provenance header. Single-message record from a Claude Code session, not a transcript export.

Added 2026-09-26: [16-claude-code-directions/2026-09-26-community-mission-request.md](16-claude-code-directions/2026-09-26-community-mission-request.md). Ren's complete message asking for a position paper and mission for the Chinese AI safety community he is organising (model-lab staff, policy and governance researchers, academics), with his nine points of stance, including the communist transition at the necessity layer with markets kept stable, and the instruction to integrate his theory in full. Preserved verbatim with an assistant-authored provenance header. The draft it produced is `drafts/2026-09-26-community-mission/`. Single-message record from a Claude Code session, not a transcript export.

Added 2026-09-26: [16-claude-code-directions/2026-09-26-community-mission-v0.2-request.md](16-claude-code-directions/2026-09-26-community-mission-v0.2-request.md). Ren's complete message directing v0.2 of the community position paper: 大同 and 生生不息 as a China-grown relational, non-dual, non-game, directional ontology and as the narrative basis of Chinese politics in place of zero-sum realism; 共产主义 as basically one with 大同; avoid expressions such as 善不姓国; make the prose more elegant; fold in the 大同 readings. Preserved verbatim with the 大同 lineage text he pasted into the same message (authorship unverified) and an assistant-authored provenance header. Single-message record from a Claude Code session, not a transcript export.

Added 2026-09-27: [16-claude-code-directions/2026-09-27-community-mission-v0.3-request.md](16-claude-code-directions/2026-09-27-community-mission-v0.3-request.md). Ren's complete message directing v0.3: from 小康 to 大同 as the inner logic of Chinese civilization and the core of national rejuvenation, not political realism; AI progress therefore non-zero-sum, against arms races, responsible to future generations, 以人为本; a message to Western friends that we are one system and not enemies; profit optimization as the source of the Matthew effect, instrumental convergence and reward hacking, with cooperation as necessary rationality; the document becomes a statement of Chinese civilization's attitude rather than an AI-safety mission. Preserved verbatim with an assistant-authored provenance header. Single-message record from a Claude Code session, not a transcript export.

Added 2026-09-28: [05-alignment-and-moloch/2026-09-28-When_Capability_Outruns_Correction.tex](05-alignment-and-moloch/2026-09-28-When_Capability_Outruns_Correction.tex), 29,683 bytes, SHA-256 `e46b968245a82f1df425c1aee5d728171919d103482969cf438dba0f366be93f`, and [the compiled PDF](05-alignment-and-moloch/2026-09-28-When_Capability_Outruns_Correction.pdf), 340,405 bytes, eight pages, SHA-256 `ddbbea3551aeecf09306325d8f51ba3a368a882f94b7b75ea382fc7a1dbb6f59`. Both are byte copies of `~/Downloads/When_Capability_Outruns_Correction.tex` and `.pdf`, which were modified 2026-09-28 at 19:58. Ren supplied them as "another of my latest theory". The paper is Yongxu Ren's "When Capability Outruns Correction: Recursive Capture, Epistemic Lag, and the Case for a Conditional Pause in Frontier AI", dated 28 September 2026 and marked "Draft for author review". Its author note says it was drafted with substantive text-generation assistance from an AI language tool, which the note does not name. It is therefore AI-drafted from Ren's ideas, and its sentences are not his verbatim. The PDF matches the `.tex` text and was compiled elsewhere: pdfTeX, TeX Live 2023 on Debian, 2026-09-28 17:03 +05:30. Two AI reviews, requested by Ren the same day, are in [the alignment theory's review folder](../theories/alignment-selection-on-cognition/review-2026-09-28-capability-outruns-correction/REVIEW.md).

Added 2026-09-28: [16-claude-code-directions/2026-09-28-capability-outruns-correction-v2-request.md](16-claude-code-directions/2026-09-28-capability-outruns-correction-v2-request.md). Ren's complete reply to the three questions that closed the review. He rules that the frontier-only scope is deliberate ("only for academia and intellectuals"). He asks that unilateral restraint be reconciled where that strengthens the paper, and that the incompressible floor be restored with stronger reasons. His last line is "Pursue academic excellence, please write the next version". The file preserves the reply verbatim, together with the assistant's three questions and an assistant-authored provenance header. It is a single-message record from a Claude Code session, not a transcript export. The v2 it produced is in `drafts/2026-09-28-capability-outruns-correction/`.
Added 2026-10-02: [03-meta-attractor/2026-10-02-the-meta-attractor-of-power.md](03-meta-attractor/2026-10-02-the-meta-attractor-of-power.md), 23,949 bytes, SHA-256 `123019f63fe2b9e24c43e82c36b41e9f4a287c1af8ba2aa6acbcbfd35c604461`. "The Meta-Attractor of Power: When winning begins to rewrite the game", an English essay in nine sections that Ren pasted into a Claude Code session as "also a part of my meta-attractor logic". It is saved byte for byte as pasted, with no header added. Two citation markers of the kind an AI chat tool leaves for attached files ("meta_attractors_v0.1_zh", "When_Capability_Outruns_Correct…") indicate that an AI assistant drafted it with a Chinese meta-attractor text and the 2026-09-28 paper attached. Treat it as AI-drafted from Ren's ideas and adopted by him; its sentences are not his verbatim. It takes Mattias Forsgren's Substack essay "Hegemonic logic" as its point of departure. Integrated into [the meta-attractor theory](../theories/meta-attractor/README.md) the same day.

Added 2026-10-02: [16-claude-code-directions/2026-10-02-meta-attractor-of-power-request.md](16-claude-code-directions/2026-10-02-meta-attractor-of-power-request.md). Ren's instruction that came with the essay above: put it in the theory, commit, merge it with the existing theories "to see what you can get", and produce a paper for IASEAI'27, whose submission guide he linked. Preserved verbatim, with an assistant-authored provenance header, notes on the essay's authorship markers and the external sources it cites, and a summary of the submission guide's terms (deadline 5 October 2026 AOE, AAAI format, ten pages, double-blind, a required Statement of Contributions). Single-message record from a Claude Code session, not a transcript export.

Added 2026-10-02: [03-meta-attractor/2026-10-02-meta-attractor-context-and-review-gpt.md](03-meta-attractor/2026-10-02-meta-attractor-context-and-review-gpt.md), 60,083 bytes, SHA-256 `d44f98567cadbf7bdac440e237d4d2d7b1450543dd975b87b8a30cde58e5f704`. Byte copy of `~/Downloads/meta_attractor_context_and_review_2026-10-02.md`, which Ren supplied as GPT's summary of "深度的review与对应meta attractor的其他上下文和发展脉络的context". It is a Chinese handoff to the agent writing the next version of *Selecting the Selectors*, in 18 sections. It covers the phenomenon and the nine-step chain, the development timeline from 2025-02 to 2026-10, concept relations, the 生生 normative direction, the public-goods practice and AI stance, corrections to the GPT 6 ASTRA review, twelve mathematical and wording fixes to the draft, a conceptual skeleton, a proposed formal model of second-order selection on conversion capacity, the restored breadth (ecologies, new domains, levels of epistemic closure, error-access graphs, safe reachability), the AI channels, literature boundaries, experiments with ablations, and a work order. It separates the author's own statements, earlier joint documents, the current draft and its own proposals. Its §11 derivations are GPT's, not Ren's. It cites files absent from this corpus: `meta_attractors_v0.1_zh.md` (2026-09-28), `Philosophy_Adversarial_Benchmark_v0.5.md` (2026-09-06), the Mycelium and Civilizational AI joint documents, and ChatGPT conversations. It also cites one file that is present: `07-shengsheng-buxi/downloads-drafts-2026-05/生生不息论_v_10_间生形式版.md`, byte-identical to the Downloads copy.

Added 2026-10-02: [16-claude-code-directions/2026-10-02-reviews-and-gpt-handoff.md](16-claude-code-directions/2026-10-02-reviews-and-gpt-handoff.md). Ren's four messages after the IASEAI draft was committed: the request for peer reviewers, the request for a corpus survey, his endorsement of the GPT 6 ASTRA review ("我非常认同"), and the handoff above. Verbatim, with an assistant-authored note. The reviews themselves are in `drafts/2026-10-02-iaseai-selecting-the-selectors/reviews/`.

Added 2026-10-02: [03-meta-attractor/2026-10-02-selecting-the-selectors-v2-review-gpt.md](03-meta-attractor/2026-10-02-selecting-the-selectors-v2-review-gpt.md), 43,521 bytes, SHA-256 `326cc46d410bf69e643a16b9f16097f02c7de41c6a323f8ed27b83d6e20a7efb`. Byte copy of `~/Downloads/selecting_the_selectors_v2_review_and_handoff.md`, GPT's review of v2 of *Selecting the Selectors* and its handoff for the next version, in Chinese, in 21 sections. It sets out the evidence boundary (the v2 PDF only, no scripts) and the theoretical aims the next version must keep. It lists the checks v2 passes and the old objections to withdraw. Twelve graded items (R1–R12) give locations, counterexamples, minimal fixes and acceptance criteria: the necessary condition for permanent silence, the late alarm at β = 0.6, calibrating β, formation in the observation term, the assistance corollary under quadratic cost only, scope at fixed size, the polynomial keystone problem, the ratchet–simulation link, a feedback-cut experiment arm, identification, the closure test, and positioning. §18 is a work order; §19 is executed code reproducing the late alarm (t ≈ 2358.664). GPT's analysis, not Ren's.

Added 2026-10-02: [16-claude-code-directions/2026-10-02-v2-review-round-and-gpt-review.md](16-claude-code-directions/2026-10-02-v2-review-round-and-gpt-review.md). Ren's request for a second independent review round of v2, his ruling that a revision still near 50% would mean the paper rather than the theory is at fault ("theories显然不止当下的潜力"), and the GPT review above. Verbatim, with an assistant-authored note. The round-2 reviews are in `drafts/2026-10-02-iaseai-selecting-the-selectors/reviews/round2/`.

Added 2026-10-02: [16-claude-code-directions/2026-10-02-shengsheng-english-request.md](16-claude-code-directions/2026-10-02-shengsheng-english-request.md). Ren's one-line request for a high-quality English 生生不息论 built on all current theories. Preserved verbatim with an assistant-authored provenance header and gloss. The draft it produced is `drafts/2026-10-02-shengsheng-en/`. Single-message record from a Claude Code session, not a transcript export.

Added 2026-10-02: [03-meta-attractor/2026-09-28-meta_attractors_v0.1_zh.md](03-meta-attractor/2026-09-28-meta_attractors_v0.1_zh.md), 50,298 bytes, SHA-256 `1035033b505f7195c0e927e69bd40f39858737b87852d5a2936ad9f37558110d`, a byte copy of `~/Downloads/meta_attractors_v0.1_zh.md`, which Ren supplied as a 补充文档 the same day. It is 《元吸引子：当选择开始改写选择——递归捕获、跨域收敛与系统性退化的动力学》, "Yongxu Ren, 研究草稿 v0.1 · 2026-09-28" (English working title *Meta-Attractors: When Selection Rewrites Selection*), the Chinese paper behind the 2026-09-28 English paper and the file the 2026-10-02 essay cites as "meta_attractors_v0.1_zh". Fourteen sections and five appendices:
- a neutral mechanism definition (再生, 自我稳定, 外向重构, 跨域扩张), with degeneracy as a separate criterion and totalization kept apart from concentration;
- an explicit prior-art section, which notes that the minimal model is a special case of Tilman et al.'s decaying-environment games and that Klüver (2002) used "meta attractor" before;
- Theorem 1 (threshold and bistability with a potential function) and Theorem 2 (capture and degradation have different thresholds);
- persistent switching μ(1−2x), which preserves bistability;
- the spectral cross-domain threshold;
- a cognitive-expectation variable m, with stability condition ab/d + η > c;
- the observation-indistinguishability proposition;
- numerics integrated in logit coordinates;
- AI sections;
- design conditions, including a uniform-bound certificate for time-varying parameters;
- a literature and originality check record.

Probably drafted with an AI assistant from Ren's direction, like its English counterpart. Its sentences are not his verbatim.

Added 2026-10-02: [17-user-provided-2026-10-02/Philosophy_Adversarial_Benchmark_v0.6.md](17-user-provided-2026-10-02/Philosophy_Adversarial_Benchmark_v0.6.md), 84,614 bytes, SHA-256 `4ad4ddc7c5c447abab62cc00ad9bb57adf108814a5167000cc36918b3943a494`, a byte copy of `~/Downloads/Philosophy_Adversarial_Benchmark_v0.6.md`, supplied by Ren the same day. 《Philosophy Adversarial Benchmark v0.6：从纠错架构到哲学重建》, dated 2026-09-07, follows v0.2–v0.5, none of which are in this corpus. Material relevant to the meta-attractor line:
- six correction functions ⟨D,P,A,T,Ω,Λ⟩ and five ecological protections, inherited from v0.4/v0.5;
- §12, the two loops: epistemic correction against action correction;
- §13, time and irreversibility ("可达≠及时可达") and three correction capacities;
- §14, the epistemic min-cut revised from edge counts to control domains with a deadline;
- §§17–18, four ethical bridge premises E1–E4 and the norms they support;
- Appendix A, three bounded results; A2 is "belief revisability does not imply world-state recoverability";
- Appendix B, a min-cut enumeration check.

Read in full except §§4–11 and 21–25 (realism, truth, meaning, understanding, the integrated case), which were skimmed. Likely drafted with an AI assistant.

Noted 2026-10-02: `~/Downloads/When_Capability_Outruns_Correction (1).pdf`, supplied with the two files above, is byte-identical (SHA-256 `ddbbea3551aeecf09306325d8f51ba3a368a882f94b7b75ea382fc7a1dbb6f59`) to `05-alignment-and-moloch/2026-09-28-When_Capability_Outruns_Correction.pdf`, already here, so no copy was made.

Noted 2026-09-25: two of the three files imported on 2026-09-06 were already in this inventory. `15-user-provided-2026-09-06/至善_对话整理完整版.md` is byte-identical to `07-shengsheng-buxi/downloads-2026-07-08/2026-07-23-至善_对话整理完整版.md` (dated 2026-07-23). `15-user-provided-2026-09-06/智能向善，天下生生.md` differs from `06-zhishan/sheng/智能向善.md` (dated 2026-07-15) only by a final newline. Their intake record leaves the authored dates open; these earlier copies date them. The Meta-Attractor essay has no identical earlier copy in the corpus.

| added | group / source | files | bytes | origin |
|---|---|---:|---:|---|
| 2026-09-05 | [15-codex-theory-conversations/2026-09-05-evolving-community-swarms.md](15-codex-theory-conversations/2026-09-05-evolving-community-swarms.md) | 1 | 31,949 | Direct export of the five founding user messages and visible assistant replies from Codex task `01a07146-7e6d-7093-86bf-f948610c370a`. Ren requested preserving this as a new exploration and explicitly aligned with the direction. Authorship is marked. The [theory folder](../theories/evolving-community-swarms/README.md) includes an identical local conversation snapshot. |
| 2026-09-07 | [15-codex-theory-conversations/2026-09-07-evolving-community-swarms-soundness.md](15-codex-theory-conversations/2026-09-07-evolving-community-swarms-soundness.md) | 1 | 8,673 | Ren’s exact soundness question and the assistant’s prepared substantive response, with evidence and interpretation notes. This is an authored assessment record, not a full task export; the proposed refinements are not yet user-endorsed. Identical copy retained in the theory folder. |
| 2026-09-07 | [15-codex-theory-conversations/2026-09-07-evolving-community-swarms-comparison.md](15-codex-theory-conversations/2026-09-07-evolving-community-swarms-comparison.md) | 1 | 15,638 | Ren’s exact comparison request and the assistant’s prepared substantive response, with primary-source evidence notes and proposed research refinements. Authored comparison record, not a full task export or experimental result. Identical copy retained in the theory folder. |
| 2026-09-07 | [15-codex-theory-conversations/2026-09-07-evolving-community-swarms-next-vision.md](15-codex-theory-conversations/2026-09-07-evolving-community-swarms-next-vision.md) | 1 | 58,610 | Ren’s exact direction to surpass existing systems, the assistant’s prepared substantive response, and exact snapshots of seven planning artifacts with their hashes. User-directed ambition; assistant-authored mechanisms and provisional gates. Identical record retained in the theory folder. |

---

## File listings

### 00-early-2021-2022

| file | bytes | date |
|---|---:|---|
| 2023-12-11-wamotopia_v1.0-downloads.md | 4,295 | 2023-12-11 |
| 706 元宇宙荣誉积分系统.pdf | 173,016 | 2022-01-07 |
| README.md | 12,646 | 2026-09-04 |
| World of Possibilities.pages | 223,684 | 2022-04-07 |
| World-of-Possibilities.jpg | 140,967 | 2026-09-03 |
| proposal.jpg | 243,223 | 2026-09-03 |
| proposal.pages | 335,243 | 2021-10-18 |
| recovered-text/2021-05-21_麦_dali-field-notes.txt | 11,020 | 2021-05-21 |
| recovered-text/2021-10-18_proposal_元社区-Metamunity.txt | 9,985 | 2021-10-18 |
| recovered-text/2022-01_706-元宇宙荣誉积分系统.txt | 444 | 2022-01-07 |
| recovered-text/2022-04-07_World-of-Possibilities.txt | 1,010 | 2022-04-07 |
| recovered-text/decode-pages-iwa.py | 2,685 | 2026-09-04 |
| 「“？P；。.jpg | 100,059 | 2026-08-31 |
| 「“？P；。.pages | 346,179 | 2022-04-07 |
| 社区.jpg | 14,375 | 2026-08-27 |
| 社区.pages | 85,629 | 2021-05-29 |
| 麦.jpg | 210,329 | 2026-09-03 |
| 麦.pages | 303,672 | 2021-05-29 |

### 01-writings-2025

| file | bytes | date |
|---|---:|---|
| NVF.md | 26,096 | 2025-02-27 |
| STS.md | 102,012 | 2025-08-10 |
| caboc.md | 29,560 | 2025-03-06 |
| cognitive_lag.md | 1,205 | 2025-02-22 |
| compound_selfishness.md | 3,476 | 2025-02-07 |
| convo_on_selfishness.md | 7,797 | 2025-02-27 |
| copy_paste.md | 7,596 | 2025-02-27 |
| good_bot.md | 5,784 | 2025-03-14 |
| good_bot_3.md | 3,929 | 2025-03-14 |
| good_bot_jusus2.md | 7,295 | 2025-03-16 |
| good_bot_jusus_3.md | 7,404 | 2025-03-16 |
| goodbot_2.md | 4,164 | 2025-03-14 |
| goodbot_4.md | 5,472 | 2025-03-14 |
| goodbot_cn.md | 6,774 | 2025-03-14 |
| goodbot_jusus.md | 5,723 | 2025-08-10 |
| grok.md | 13,286 | 2025-02-27 |
| hyperconnected.md | 38,271 | 2025-03-05 |
| new_narrative_manifesto.md | 53,416 | 2025-04-06 |
| prompt.md | 105,469 | 2025-02-27 |
| regen.md | 109,957 | 2025-03-05 |
| runaway_selfishness.md | 30,841 | 2025-03-05 |
| selfish_sprial.md | 7,871 | 2025-03-05 |
| usis.md | 54,717 | 2025-08-10 |

### 02-wamotopia

(git internals of the wamotopia repository omitted from this listing)

| file | bytes | date |
|---|---:|---|
| 2023-2024-wamotopia-repo/Poems/The_Ladder_of_Illusions.md | 422 | 2024-01-16 |
| 2023-2024-wamotopia-repo/Poems/Veils_of_Perception.md | 932 | 2024-01-16 |
| 2023-2024-wamotopia-repo/README.md | 2,555 | 2024-01-16 |
| 2023-2024-wamotopia-repo/Wacas/Futurisica.md | 1,956 | 2024-01-16 |
| 2023-2024-wamotopia-repo/Wacas/Mirrors_of_Mindscapes_Waca.md | 1,156 | 2023-12-25 |
| 2023-2024-wamotopia-repo/Wacas/luminous_connections_camp_v0.7.md | 1,415 | 2023-12-25 |
| 2023-2024-wamotopia-repo/Wacas/slay_moloch_camp_v0.8.md | 2,505 | 2023-12-21 |
| 2023-2024-wamotopia-repo/manifestos/wamotopia_v1.0.md | 4,303 | 2023-12-21 |
| 2025-wamo-protocol/manifesto-wamo.md | 19,613 | 2025-11-25 |
| 2025-wamo-protocol/manifesto-wamo2.md | 4,926 | 2025-11-26 |
| 2025-wamo-protocol/manifesto-wamo3.md | 9,099 | 2025-11-26 |
| 2025-wamo-protocol/manifesto-wamox.md | 21,313 | 2025-11-26 |
| 2025-wamo-protocol/wamo_camp_chinese.md | 16,802 | 2025-12-19 |
| 2025-wamo-protocol/wamo_long_version.md | 21,313 | 2025-11-26 |
| 2025-wamo-protocol/wamo_short.md | 1,562 | 2025-12-10 |
| 2025-wamo-protocol/wamo_whitepaper.md | 5,063 | 2025-12-11 |
| 2025-wamo-protocol/wamotopia-2026-call-for-camps-zoey.md | 17,829 | 2025-12-11 |
| transcripts/2026-01-note-chiangmai-festival-talk.txt | 10,305 | 2026-01-11 |
| transcripts/2026-01-wamo-nunet-intro-meeting.txt | 47,668 | 2026-01-09 |
| transcripts/dharma-bot-3.1.1-external-c3-prompt.md | 25,075 | 2025-10-15 |

### 03-meta-attractor

| file | bytes | date |
|---|---:|---|
| 2024-precursors/capital-analysis.md | 3,056 | 2024-10-30 |
| 2024-precursors/capital-dynamics.md | 3,903 | 2024-10-30 |
| 2024-precursors/future-2045.md | 5,826 | 2024-11-03 |
| 2024-precursors/ouroboros-cycle.md | 5,381 | 2024-11-05 |
| 2025-05-drafts-selected/2025-05-18-navigating-the-precipice-start-research.md | 67,316 | 2025-05-18 |
| 2025-05-drafts-selected/2025-05-24-v01-or-launch-greatest-era.md | 30,142 | 2025-05-24 |
| 2025-05-drafts-selected/2025-05-25-how-civilizations-program-their-own-demise.md | 13,893 | 2025-05-25 |
| 2025-05-drafts-selected/2025-05-26-v05.md | 53,306 | 2025-05-26 |
| 2025-05-drafts-selected/2025-05-30-seed-meta-attractors-and-road-to-systemic-collapse.md | 23,307 | 2025-06-16 |
| 2025-05-drafts-selected/2025-05-30-v10.md | 44,361 | 2025-05-30 |
| 2025-05-drafts-selected/2025-05-31-v18.md | 85,724 | 2025-05-31 |
| 2025-05-drafts-selected/2025-06-01-v26.md | 101,955 | 2025-06-01 |
| 2025-05-drafts-selected/2025-06-16-v32-final-draft.md | 108,537 | 2025-06-16 |
| 2025-08-formal/2025-08-10-comprehensive-mathematical-definition.md | 42,096 | 2025-08-10 |
| 2025-08-formal/2025-08-10-metaa-prompt-with-user-context.md | 51,572 | 2025-08-10 |
| 2025-08-formal/2025-08-10-metaaa-prompt.md | 11,456 | 2025-08-10 |
| 2025-10-essays/The_Meta-Attractor_Complete-why-attractor-thinking.md | 8,205 | 2025-10-26 |
| 2025-10-essays/meta-attractor-condensed.md | 14,310 | 2025-10-26 |
| 2025-10-essays/meta-attractor-essay-full-draft.md | 15,041 | 2025-10-28 |
| 2025-10-essays/meta-attractor-essay-long.md | 25,798 | 2025-10-26 |
| 2025-10-essays/meta-attractor-essay.md | 14,089 | 2025-10-26 |
| 2025-10-essays/meta-attractor-formal.md | 24,626 | 2025-10-26 |
| 2025-10-essays/meta-attractor-vedic-rome-china.md | 13,776 | 2025-10-26 |
| 2025-10-essays/meta-attractors-today.md | 9,302 | 2025-10-26 |
| 2025-10-essays/why-meta-attractors-opening.md | 4,253 | 2025-10-26 |
| context-site/PLANNER_CONTEXT.md | 3,521 | 2025-10-28 |
| context-site/TODO.md | 1,176 | 2025-10-28 |
| context-site/ai_agi_asi_readiness.md | 3,720 | 2025-10-28 |
| context-site/ai_gating.mmd | 418 | 2025-10-28 |
| context-site/ai_readiness_variants.md | 3,307 | 2025-10-28 |
| context-site/audience_layers.md | 1,462 | 2025-10-28 |
| context-site/case_studies/attention_economy.md | 1,403 | 2025-10-28 |
| context-site/case_studies/data_notes.md | 1,788 | 2025-10-28 |
| context-site/case_studies/growth_finance.md | 1,562 | 2025-10-28 |
| context-site/claims.md | 5,239 | 2025-10-28 |
| context-site/content_manifest.json | 1,615 | 2025-10-28 |
| context-site/crosswalk.md | 2,418 | 2025-10-28 |
| context-site/data/attention_pdi_weights.csv | 147 | 2025-10-28 |
| context-site/data/attention_pwc.csv | 211 | 2025-10-28 |
| context-site/data/attention_sc_inputs.csv | 190 | 2025-10-28 |
| context-site/data/finance_pdi_weights.csv | 147 | 2025-10-28 |
| context-site/data/finance_pwc.csv | 219 | 2025-10-28 |
| context-site/data/finance_sc_inputs.csv | 190 | 2025-10-28 |
| context-site/diagnostics.md | 1,977 | 2025-10-28 |
| context-site/glossary.md | 2,882 | 2025-10-28 |
| context-site/governance_blueprint.md | 1,304 | 2025-10-28 |
| context-site/hero.md | 1,860 | 2025-10-28 |
| context-site/knowledge_map.mmd | 1,500 | 2025-10-28 |
| context-site/metrics_visuals.mmd | 1,420 | 2025-10-28 |
| context-site/notes.md | 5,232 | 2025-10-28 |
| context-site/policy_one_pager.md | 1,159 | 2025-10-28 |
| context-site/quotes_and_anchors.md | 2,519 | 2025-10-28 |
| context-site/section_ids.json | 427 | 2025-10-28 |
| context-site/site_copy.md | 7,706 | 2025-10-28 |
| context-site/site_outline.md | 2,939 | 2025-10-28 |
| pdf/Meta-Attractor 理论.pdf | 445,655 | 2026-07-03 |
| pdf/The Civilizational Dynamics Behind AI Risk.pdf | 30,261 | 2026-07-13 |

### 04-speculative-future

| file | bytes | date |
|---|---:|---|
| current/AGENTS.md | 2,577 | 2026-08-22 |
| current/FOUNDATION-ONTOLOGICAL-REALISM.md | 14,759 | 2026-06-09 |
| current/FOUNDATION-PRINCIPLES-DRAFT.md | 23,806 | 2026-06-06 |
| current/FOUNDATION-PRINCIPLES-REVISION-COMPOSITE-MINIMAL.md | 29,161 | 2026-06-09 |
| current/FOUNDATION-PRINCIPLES-REVISION-PROCESS.md | 22,675 | 2026-06-09 |
| current/WHAT-MUST-BE-KNOWN.md | 8,808 | 2026-06-09 |
| history-recovered-from-git/Downloads_FOUNDATION-PRINCIPLES-2026-06-05.md | 9,359 | 2026-06-05 |
| history-recovered-from-git/FOUNDATION-PRINCIPLES-CONCISE.md | 6,924 | 2023-10-25 |
| history-recovered-from-git/FOUNDATION-PRINCIPLES-REVISION-ADVERSARIAL.md | 29,441 | 2024-08-05 |
| history-recovered-from-git/FOUNDATION-PRINCIPLES-REVISION-CODEX.md | 26,134 | 2026-07-03 |
| history-recovered-from-git/FOUNDATION-PRINCIPLES-REVISION-COMPOSITE-SAFEGUARDS.md | 28,918 | 2026-09-03 |
| history-recovered-from-git/FOUNDATION-PRINCIPLES-REVISION-COMPOSITE-SYSTEMS.md | 28,955 | 2026-09-03 |
| history-recovered-from-git/FOUNDATION-PRINCIPLES-REVISION-COMPOSITE.md | 28,938 | 2026-09-03 |
| history-recovered-from-git/FOUNDATION-PRINCIPLES-REVISION-DRAFT.md | 25,984 | 2025-02-08 |
| history-recovered-from-git/FOUNDATION-PRINCIPLES-REVISION-PROSE.md | 25,834 | 2026-09-03 |
| history-recovered-from-git/FOUNDATION-PRINCIPLES-REVISION-SYSTEMS.md | 26,500 | 2026-09-03 |
| history-recovered-from-git/FOUNDATION-PRINCIPLES.md | 12,071 | 2026-09-03 |
| history-recovered-from-git/FOUNDATION.md | 14,589 | 2026-07-28 |
| history-recovered-from-git/PRINCIPLES.md | 6,996 | 2024-08-05 |
| history-recovered-from-git/README.md | 2,244 | 2024-04-28 |
| history-recovered-from-git/UNDERSTANDING.md | 5,879 | 2025-10-14 |
| history-recovered-from-git/future-guide-chat_SPEC.md | 21,868 | 2024-08-31 |
| history-recovered-from-git/generated_futures_02_automated_larp_town.md | 16,315 | 2026-08-22 |
| history-recovered-from-git/generated_futures_03_city_of_the_living_garden.md | 16,011 | 2026-06-07 |
| history-recovered-from-git/generated_futures_04_elevator_portal_megastructure.md | 17,567 | 2026-08-22 |
| history-recovered-from-git/thinking_00-foundation-FINAL.md | 14,589 | 2026-07-28 |
| history-recovered-from-git/thinking_00-foundation.md | 9,408 | 2023-10-25 |
| history-recovered-from-git/thinking_01-the-attractor-and-the-escape.md | 6,314 | 2026-09-03 |
| history-recovered-from-git/thinking_02-veins-and-seeds.md | 6,398 | 2024-08-05 |
| history-recovered-from-git/thinking_03-stop-using-ai-to-compete.md | 9,410 | 2023-10-25 |
| history-recovered-from-git/thinking_03-the-cooperative-turn.md | 11,380 | 2024-08-07 |
| history-recovered-from-git/thinking_04-theory-of-change.md | 7,154 | 2026-02-12 |
| history-recovered-from-git/thinking_05-foundation-review.md | 10,442 | 2026-09-03 |
| history-recovered-from-git/thinking_06-foundation-review.md | 6,003 | 2025-03-13 |
| pro-speculative-futures-with-ren-notes.txt | 1,207 | 2026-04-20 |

### 05-alignment-and-moloch

| file | bytes | date |
|---|---:|---|
| 2026-04-23-moloch-essay.md | 6,348 | 2026-04-23 |
| 2026-04-23-moloch-mechanisms.md | 8,036 | 2026-04-23 |
| 2026-04-23-moloch-worshipper.md | 7,277 | 2026-04-23 |
| 2026-05-28-alignment-core-stance.md | 12,319 | 2026-05-28 |
| 2026-05-28-alignment-workspace-CLAUDE.md | 4,680 | 2026-05-28 |
| 2026-07-03-deep-research-ai-existential-risk.md | 37,009 | 2026-07-03 |
| 2026-08-22-development-within-understanding-position-paper.md | 54,265 | 2026-08-22 |

### 06-zhishan

| file | bytes | date |
|---|---:|---|
| .gitignore | 23 | 2026-07-13 |
| CLAUDE.md.disabled.md | 2,296 | 2026-07-13 |
| Freedom You Cannot Use Is Not Yet Freedom.md | 14,855 | 2026-07-15 |
| README.md | 2,050 | 2026-07-13 |
| foundations/README.md | 1,101 | 2026-07-13 |
| foundations/speculative-future/FOUNDATION-ONTOLOGICAL-REALISM.md | 14,759 | 2026-06-09 |
| foundations/speculative-future/FOUNDATION-PRINCIPLES-DRAFT.md | 23,806 | 2026-06-06 |
| foundations/speculative-future/FOUNDATION-PRINCIPLES-REVISION-COMPOSITE-MINIMAL.md | 29,161 | 2026-06-09 |
| foundations/speculative-future/FOUNDATION-PRINCIPLES-REVISION-PROCESS.md | 22,675 | 2026-06-09 |
| foundations/speculative-future/WHAT-MUST-BE-KNOWN.md | 8,808 | 2026-06-09 |
| manifesto/README.md | 305 | 2026-07-13 |
| manifesto/drafts/draft-1.md | 10,248 | 2026-07-08 |
| research/README.md | 588 | 2026-07-13 |
| research/agency/无身之我-人工Ego的形成机制与关系性出路.md | 74,263 | 2026-07-04 |
| research/meta-attractor/README.md | 843 | 2026-07-13 |
| research/meta-attractor/sources/Meta-Attractor理论-对话原稿.pdf | 445,655 | 2026-07-04 |
| research/meta-attractor/versions/v0.1.md | 13,422 | 2026-07-03 |
| research/meta-attractor/versions/v0.2.md | 31,805 | 2026-07-03 |
| research/meta-attractor/versions/v0.3.md | 41,411 | 2026-07-03 |
| research/meta-attractor/versions/v0.4.md | 35,052 | 2026-07-03 |
| research/meta-attractor/versions/v0.5.md | 30,274 | 2026-07-03 |
| research/meta-attractor/versions/v0.6.md | 35,802 | 2026-07-03 |
| research/meta-attractor/versions/v0.7.md | 40,875 | 2026-07-03 |
| research/meta-attractor/versions/v0.8.md | 27,623 | 2026-07-03 |
| research/meta-attractor/versions/v0.9.md | 43,960 | 2026-07-03 |
| research/synthesis/整合分析-吸引子与主体两线.md | 28,774 | 2026-07-13 |
| sheng/The Choice Before Intelligence.md | 30,112 | 2026-07-15 |
| sheng/The First Principle for Artificial Intelligence.md | 30,872 | 2026-07-15 |
| sheng/To Good (poem).md | 14,848 | 2026-07-15 |
| sheng/Why the System Keeps Reproducing Itself.md | 18,157 | 2026-07-15 |
| sheng/zhishan draft.zip | 72,286 | 2026-07-15 |
| sheng/智善.md | 13,336 | 2026-07-15 |
| sheng/智能向善.md | 4,834 | 2026-07-15 |
| sheng/生生 · English.md | 21,635 | 2026-07-15 |
| sheng/生生 · 和.md | 11,407 | 2026-07-15 |
| sheng/生生 · 当代.md | 19,839 | 2026-07-15 |
| sheng/生生 · 文言.md | 14,236 | 2026-07-15 |
| sheng/生生不息 poem — editorial notes.md | 10,986 | 2026-07-15 |
| sheng/生生不息 record (recovered).md | 29,717 | 2026-07-15 |
| sheng/生生不息 record.md | 24,121 | 2026-07-15 |
| sheng/生生行.md | 22,540 | 2026-07-15 |
| shengsheng/生生不息论v1/generative_existence.md | 35,833 | 2026-07-14 |
| shengsheng/生生不息论v1/生生不息论.md | 37,548 | 2026-07-15 |
| shengsheng/生生不息论v1/生生不息论2.md | 43,710 | 2026-07-15 |
| shengsheng/生生不息论v1/生生不息论3.md | 34,196 | 2026-07-14 |
| shengsheng/生生不息论v1/生生不息论4.md | 28,291 | 2026-07-14 |
| shengsheng/生生不息论v1/生生不息论5.md | 40,396 | 2026-07-14 |
| shengsheng/生生不息论v1/生生不息论6.md | 4,947 | 2026-07-14 |
| shengsheng/生生不息论v2/00-PLAN-v2-initial.md | 42,318 | 2026-07-14 |
| shengsheng/生生不息论v2/PLAN-v2.md | 39,381 | 2026-07-14 |
| shengsheng/生生不息论v2/reviews/ai-alignment-systems.md | 32,508 | 2026-07-14 |
| shengsheng/生生不息论v2/reviews/gate2-ai-alignment.md | 3,037 | 2026-07-14 |
| shengsheng/生生不息论v2/reviews/gate2-philosophy.md | 2,160 | 2026-07-14 |
| shengsheng/生生不息论v2/reviews/gate2-sociology-economics.md | 2,581 | 2026-07-14 |
| shengsheng/生生不息论v2/reviews/philosophy-logic.md | 7,051 | 2026-07-14 |
| shengsheng/生生不息论v2/reviews/review-synthesis.md | 11,728 | 2026-07-14 |
| shengsheng/生生不息论v2/reviews/sociology-economics.md | 4,195 | 2026-07-14 |
| whitepaper/README.md | 905 | 2026-07-13 |
| whitepaper/drafts/v0.2.md | 56,558 | 2026-07-02 |
| whitepaper/drafts/v0.3.md | 32,099 | 2026-07-02 |
| whitepaper/drafts/v0.4.md | 72,735 | 2026-07-04 |
| whitepaper/outlines/v0.4-outline-and-strategy.md | 13,336 | 2026-07-04 |
| whitepaper/plans/v0.5-writing-plan.md | 22,533 | 2026-07-13 |
| whitepaper/process/v0.4-drafting-constraints.md | 6,312 | 2026-07-13 |
| whitepaper/reviews/v0.4-multi-perspective-review.md | 75,878 | 2026-07-02 |
| whitepaper/reviews/v0.4-multi-review-report.md | 25,725 | 2026-07-13 |
| writing-program/README.md | 2,217 | 2026-07-13 |
| writing-program/causal-chain/README.md | 5,627 | 2026-07-13 |
| writing-program/causal-chain/v1/chain.md | 25,524 | 2026-07-13 |
| writing-program/causal-chain/v2/independent-a.md | 48,785 | 2026-07-13 |
| writing-program/causal-chain/v2/independent-b.md | 31,549 | 2026-07-13 |
| writing-program/causal-chain/v2/independent-c.md | 37,915 | 2026-07-13 |
| writing-program/causal-chain/v2/main.md | 52,911 | 2026-07-13 |
| writing-program/causal-chain/v2/preparation.md | 23,547 | 2026-07-13 |
| writing-program/causal-chain/v2/reviews/README.md | 1,163 | 2026-07-13 |
| writing-program/causal-chain/v2/reviews/ai-empirical-red-team.md | 38,615 | 2026-07-13 |
| writing-program/causal-chain/v2/reviews/cross-version-red-team.md | 21,469 | 2026-07-13 |
| writing-program/causal-chain/v2/reviews/deep-synthesis-and-v3-direction.md | 28,677 | 2026-07-13 |
| writing-program/causal-chain/v2/reviews/normative-philosophy-red-team.md | 40,780 | 2026-07-13 |
| writing-program/causal-chain/v2/reviews/systems-science-red-team.md | 44,286 | 2026-07-13 |
| writing-program/causal-chain/v3/README.md | 1,045 | 2026-07-13 |
| writing-program/causal-chain/v3/independent-en.md | 42,654 | 2026-07-13 |
| writing-program/causal-chain/v3/independent-zh.md | 24,305 | 2026-07-13 |
| writing-program/causal-chain/v3/main-zh.md | 29,643 | 2026-07-13 |
| writing-program/causal-chain/v3/plan.md | 26,246 | 2026-07-13 |
| writing-program/causal-chain/v3/reviews/README.md | 1,159 | 2026-07-13 |
| writing-program/causal-chain/v3/reviews/ai-empirical-red-team.md | 39,986 | 2026-07-13 |
| writing-program/causal-chain/v3/reviews/cross-version-logic-and-prose-review.md | 23,930 | 2026-07-13 |
| writing-program/causal-chain/v3/reviews/deep-synthesis-and-v4-direction.md | 22,956 | 2026-07-13 |
| writing-program/causal-chain/v3/reviews/normative-civilizational-red-team.md | 28,986 | 2026-07-13 |
| writing-program/causal-chain/v3/reviews/systems-game-red-team.md | 31,914 | 2026-07-13 |
| writing-program/causal-chain/v4/README.md | 1,261 | 2026-07-13 |
| writing-program/causal-chain/v4/independent-en.md | 41,457 | 2026-07-13 |
| writing-program/causal-chain/v4/independent-zh.md | 29,606 | 2026-07-13 |
| writing-program/causal-chain/v4/main-zh.md | 20,779 | 2026-07-13 |
| writing-program/causal-chain/v4/plan.md | 26,954 | 2026-07-13 |
| writing-program/causal-chain/v4/reviews/README.md | 1,013 | 2026-07-13 |
| writing-program/causal-chain/v4/reviews/ai-empirical-red-team.md | 32,940 | 2026-07-13 |
| writing-program/causal-chain/v4/reviews/cross-version-logic-and-prose-review.md | 14,463 | 2026-07-13 |
| writing-program/causal-chain/v4/reviews/deep-synthesis-and-v5-direction.md | 13,376 | 2026-07-13 |
| writing-program/causal-chain/v4/reviews/normative-traditions-red-team.md | 36,932 | 2026-07-13 |
| writing-program/causal-chain/v4/reviews/systems-dynamics-red-team.md | 34,318 | 2026-07-13 |
| writing-program/causal-chain/v5/README.md | 1,173 | 2026-07-13 |
| writing-program/causal-chain/v5/independent-en.md | 41,190 | 2026-07-13 |
| writing-program/causal-chain/v5/independent-zh.md | 31,078 | 2026-07-13 |
| writing-program/causal-chain/v5/main-zh.md | 17,846 | 2026-07-13 |
| writing-program/causal-chain/v5/plan.md | 18,910 | 2026-07-13 |
| writing-program/causal-chain/v5/reviews/README.md | 822 | 2026-07-13 |
| writing-program/causal-chain/v5/reviews/ai-empirical-red-team.md | 20,674 | 2026-07-13 |
| writing-program/causal-chain/v5/reviews/cross-version-logic-and-prose-review.md | 10,943 | 2026-07-13 |
| writing-program/causal-chain/v5/reviews/deep-synthesis-and-consolidation-direction.md | 10,591 | 2026-07-13 |
| writing-program/causal-chain/v5/reviews/normative-red-team.md | 33,514 | 2026-07-13 |
| writing-program/causal-chain/v5/reviews/systems-red-team.md | 27,680 | 2026-07-13 |
| writing-program/causal-chain/v6.1/README.md | 1,300 | 2026-07-13 |
| writing-program/causal-chain/v6.1/main-zh.md | 17,272 | 2026-07-13 |
| writing-program/causal-chain/v6.1/reviews/README.md | 1,346 | 2026-07-13 |
| writing-program/causal-chain/v6.1/reviews/adversarial-synthesis.md | 11,649 | 2026-07-13 |
| writing-program/causal-chain/v6.1/reviews/blind-reader-audit.md | 15,796 | 2026-07-13 |
| writing-program/causal-chain/v6.1/reviews/evidence-redteam-audit.md | 11,137 | 2026-07-13 |
| writing-program/causal-chain/v6.1/reviews/hostile-logic-audit.md | 13,925 | 2026-07-13 |
| writing-program/causal-chain/v6.1/reviews/normative-justice-audit.md | 11,546 | 2026-07-13 |
| writing-program/causal-chain/v6.1/reviews/strongest-opponents-audit.md | 11,404 | 2026-07-13 |
| writing-program/causal-chain/v6.1/reviews/systems-adversarial-audit.md | 13,204 | 2026-07-13 |
| writing-program/causal-chain/v6.1/revision-contract.md | 2,734 | 2026-07-13 |
| writing-program/causal-chain/v6.1/verification.md | 3,928 | 2026-07-13 |
| writing-program/causal-chain/v6.2/README.md | 1,831 | 2026-07-13 |
| writing-program/causal-chain/v6.2/main-zh.md | 20,447 | 2026-07-13 |
| writing-program/causal-chain/v6.2/reviews/README.md | 1,980 | 2026-07-13 |
| writing-program/causal-chain/v6.2/reviews/adversarial-synthesis.md | 13,316 | 2026-07-13 |
| writing-program/causal-chain/v6.2/reviews/blind-reader-audit.md | 9,445 | 2026-07-13 |
| writing-program/causal-chain/v6.2/reviews/evidence-redteam-audit.md | 8,721 | 2026-07-13 |
| writing-program/causal-chain/v6.2/reviews/hostile-logic-audit.md | 11,648 | 2026-07-13 |
| writing-program/causal-chain/v6.2/reviews/normative-justice-audit.md | 8,402 | 2026-07-13 |
| writing-program/causal-chain/v6.2/reviews/strongest-opponents-audit.md | 9,693 | 2026-07-13 |
| writing-program/causal-chain/v6.2/reviews/systems-adversarial-audit.md | 15,627 | 2026-07-13 |
| writing-program/causal-chain/v6.2/revision-contract.md | 3,551 | 2026-07-13 |
| writing-program/causal-chain/v6.2/verification.md | 6,158 | 2026-07-13 |
| writing-program/causal-chain/v6.3/README.md | 1,525 | 2026-07-13 |
| writing-program/causal-chain/v6.3/main-zh.md | 25,904 | 2026-07-13 |
| writing-program/causal-chain/v6.3/revision-contract.md | 6,769 | 2026-07-13 |
| writing-program/causal-chain/v6.3/verification.md | 7,861 | 2026-07-13 |
| writing-program/causal-chain/v6.4/foundation.md | 11,257 | 2026-07-13 |
| writing-program/causal-chain/v6.5/README.md | 1,164 | 2026-07-13 |
| writing-program/causal-chain/v6.5/content-retention-audit.md | 9,438 | 2026-07-13 |
| writing-program/causal-chain/v6.5/foundation.md | 13,883 | 2026-07-13 |
| writing-program/causal-chain/v6.5/independent-en.md | 36,676 | 2026-07-13 |
| writing-program/causal-chain/v6.5/independent-zh.md | 26,717 | 2026-07-13 |
| writing-program/causal-chain/v6.5/main-zh.md | 23,598 | 2026-07-13 |
| writing-program/causal-chain/v6.5/reviews/README.md | 889 | 2026-07-13 |
| writing-program/causal-chain/v6.5/reviews/cross-version-prose-review.md | 24,869 | 2026-07-13 |
| writing-program/causal-chain/v6.5/reviews/normative-civilizational-ai-review.md | 34,301 | 2026-07-13 |
| writing-program/causal-chain/v6.5/reviews/synthesis-and-v7-direction.md | 14,282 | 2026-07-13 |
| writing-program/causal-chain/v6.5/reviews/systems-rationality-review.md | 19,721 | 2026-07-13 |
| writing-program/causal-chain/v6/README.md | 806 | 2026-07-13 |
| writing-program/causal-chain/v6/independent-en.md | 30,930 | 2026-07-13 |
| writing-program/causal-chain/v6/independent-zh.md | 17,696 | 2026-07-13 |
| writing-program/causal-chain/v6/main-zh.md | 14,720 | 2026-07-13 |
| writing-program/causal-chain/v6/plan.md | 7,223 | 2026-07-13 |
| writing-program/causal-chain/v6/reviews/README.md | 790 | 2026-07-13 |
| writing-program/causal-chain/v6/reviews/ai-stop-audit.md | 15,408 | 2026-07-13 |
| writing-program/causal-chain/v6/reviews/cross-version-stop-audit.md | 7,526 | 2026-07-13 |
| writing-program/causal-chain/v6/reviews/normative-stop-audit.md | 9,178 | 2026-07-13 |
| writing-program/causal-chain/v6/reviews/stopping-synthesis.md | 5,852 | 2026-07-13 |
| writing-program/causal-chain/v6/reviews/systems-stop-audit.md | 10,768 | 2026-07-13 |
| writing-program/causal-chain/v7/README.md | 1,214 | 2026-07-13 |
| writing-program/causal-chain/v7/independent-en.md | 30,731 | 2026-07-13 |
| writing-program/causal-chain/v7/independent-zh.md | 28,962 | 2026-07-13 |
| writing-program/causal-chain/v7/main-zh.md | 23,494 | 2026-07-13 |
| writing-program/causal-chain/v7/plan.md | 10,547 | 2026-07-13 |
| writing-program/causal-chain/v7/reviews/README.md | 756 | 2026-07-13 |
| writing-program/causal-chain/v7/reviews/multi-agent-synthesis.md | 17,470 | 2026-07-13 |
| writing-program/causal-chain/v7/reviews/normative-ai-review.md | 35,326 | 2026-07-13 |
| writing-program/causal-chain/v7/reviews/prose-flow-review.md | 40,808 | 2026-07-13 |
| writing-program/causal-chain/v7/reviews/systems-causal-review.md | 37,205 | 2026-07-13 |
| writing-program/causal-chain/v8/README.md | 3,158 | 2026-07-13 |
| writing-program/causal-chain/v8/evidence-packet.md | 33,001 | 2026-07-13 |
| writing-program/causal-chain/v8/independent-en.md | 39,209 | 2026-07-13 |
| writing-program/causal-chain/v8/independent-zh.md | 30,467 | 2026-07-13 |
| writing-program/causal-chain/v8/main-zh.md | 26,639 | 2026-07-13 |
| writing-program/causal-chain/v8/plan.md | 15,310 | 2026-07-13 |
| writing-program/causal-chain/v8/preparation/README.md | 803 | 2026-07-13 |
| writing-program/causal-chain/v8/preparation/action-principle-and-instruments.md | 22,209 | 2026-07-13 |
| writing-program/causal-chain/v8/preparation/cross-version-genealogy.md | 26,614 | 2026-07-13 |
| writing-program/causal-chain/v8/preparation/normative-conflict-resolution.md | 38,418 | 2026-07-13 |
| writing-program/causal-chain/v8/preparation/plan-audit.md | 2,551 | 2026-07-13 |
| writing-program/causal-chain/v8/preparation/review-contract.md | 13,346 | 2026-07-13 |
| writing-program/causal-chain/v8/preparation/synthesis.md | 18,645 | 2026-07-13 |
| writing-program/causal-chain/v8/reviews/README.md | 954 | 2026-07-13 |
| writing-program/causal-chain/v8/reviews/cross-draft-flow-review.md | 2,488 | 2026-07-13 |
| writing-program/causal-chain/v8/reviews/independent-en-review.md | 5,240 | 2026-07-13 |
| writing-program/causal-chain/v8/reviews/independent-zh-review.md | 5,863 | 2026-07-13 |
| writing-program/causal-chain/v8/reviews/main-zh-review.md | 5,733 | 2026-07-13 |
| writing-program/context/README.md | 620 | 2026-07-13 |
| writing-program/context/meta-attractor-foundational-context.md | 42,995 | 2026-07-13 |
| writing-program/context/political-will-bottleneck.md | 16,015 | 2026-07-12 |
| writing-program/drafts/README.md | 1,198 | 2026-07-13 |
| writing-program/drafts/baseline/english.md | 59,766 | 2026-07-10 |
| writing-program/drafts/baseline/zh-independent.md | 72,250 | 2026-07-10 |
| writing-program/drafts/baseline/zh-main.md | 45,171 | 2026-07-13 |
| writing-program/drafts/v3/english.md | 62,908 | 2026-07-12 |
| writing-program/drafts/v5/independent-a-en.md | 98,363 | 2026-07-12 |
| writing-program/drafts/v5/independent-b-en.md | 97,091 | 2026-07-12 |
| writing-program/drafts/v5/main-en.md | 95,396 | 2026-07-12 |
| writing-program/drafts/v6/english.md | 50,026 | 2026-07-12 |
| writing-program/drafts/v7/independent-en.md | 74,701 | 2026-07-12 |
| writing-program/drafts/v8/independent-en.md | 50,429 | 2026-07-12 |
| writing-program/outlines/README.md | 424 | 2026-07-13 |
| writing-program/outlines/v9/outline.md | 62,575 | 2026-07-13 |
| writing-program/outlines/v9/structural-diagnosis.md | 8,595 | 2026-07-13 |
| writing-program/plans/README.md | 882 | 2026-07-13 |
| writing-program/plans/foundation.md | 35,569 | 2026-07-13 |
| writing-program/plans/program.md | 35,314 | 2026-07-13 |
| writing-program/plans/v2.md | 19,741 | 2026-07-12 |
| writing-program/plans/v3.md | 26,585 | 2026-07-12 |
| writing-program/plans/v4.md | 50,098 | 2026-07-12 |
| writing-program/plans/v5.md | 73,082 | 2026-07-12 |
| writing-program/plans/v6.md | 28,941 | 2026-07-12 |
| writing-program/plans/v7.md | 6,912 | 2026-07-13 |
| writing-program/plans/v8.md | 13,598 | 2026-07-13 |
| writing-program/reviews/README.md | 451 | 2026-07-13 |
| writing-program/reviews/draft-comparison.md | 11,259 | 2026-07-13 |
| writing-program/reviews/mistakes-and-lessons.md | 6,745 | 2026-07-13 |
| writing-program/reviews/v7-writing-experiment.md | 28,018 | 2026-07-13 |

### 07-shengsheng-buxi

| file | bytes | date |
|---|---:|---|
| downloads-2026-07-08/2026-03-31-大道之行.md | 15,450 | 2026-03-31 |
| downloads-2026-07-08/2026-07-14-生生不息论.md | 65,846 | 2026-07-14 |
| downloads-2026-07-08/2026-07-23-至善.md | 17,645 | 2026-07-23 |
| downloads-2026-07-08/2026-07-23-至善_对话整理完整版.md | 34,681 | 2026-07-23 |
| downloads-2026-07-08/2026-08-09-生生不息论-证明篇-v0.6.md | 29,851 | 2026-08-09 |
| downloads-2026-07-08/Shengsheng_The_Way_of_Unceasing_Generation.md | 130,346 | 2026-07-14 |
| downloads-2026-07-08/generative_existence.md | 35,833 | 2026-07-14 |
| downloads-drafts-2026-05/与生生不息对齐之必然.md | 37,793 | 2026-05-03 |
| downloads-drafts-2026-05/生生不息论_v11.1_符号清洗校验本.md | 47,534 | 2026-05-03 |
| downloads-drafts-2026-05/生生不息论_v11_校验本.md | 47,467 | 2026-05-03 |
| downloads-drafts-2026-05/生生不息论_v12.1_字元闭合本.md | 39,389 | 2026-05-04 |
| downloads-drafts-2026-05/生生不息论_v12.2_审校正名本.md | 39,839 | 2026-05-04 |
| downloads-drafts-2026-05/生生不息论_v13.1_全字元生成闭合本.md | 54,195 | 2026-05-04 |
| downloads-drafts-2026-05/生生不息论_v4.md | 29,451 | 2026-05-03 |
| downloads-drafts-2026-05/生生不息论_v5.md | 42,090 | 2026-05-03 |
| downloads-drafts-2026-05/生生不息论_v9.md | 66,642 | 2026-05-03 |
| downloads-drafts-2026-05/生生不息论_v9_开境护闭校正版.md | 63,652 | 2026-05-04 |
| downloads-drafts-2026-05/生生不息论_v_10_间生形式版.md | 18,942 | 2026-05-03 |
| downloads-drafts-2026-05/生生不息论_v_11_间开定本.md | 85,369 | 2026-05-03 |
| downloads-drafts-2026-05/生生不息论_间开本_v3.md | 83,663 | 2026-05-03 |
| downloads-drafts-2026-05/间生论_形式补.md | 20,304 | 2026-05-03 |
| ssbx-repo/AGENTS.md | 5,604 | 2026-05-21 |
| ssbx-repo/README.en.md | 41,492 | 2026-05-21 |
| ssbx-repo/README.formal.md | 48,095 | 2026-05-21 |
| ssbx-repo/README.md | 36,077 | 2026-05-21 |
| ssbx-repo/docs-next/.DS_Store | 6,148 | 2026-05-16 |
| ssbx-repo/docs-next/00_start/README.md | 675 | 2026-05-08 |
| ssbx-repo/docs-next/00_start/final-claim-roadmap.md | 17,577 | 2026-05-21 |
| ssbx-repo/docs-next/00_start/final-theory.md | 22,086 | 2026-05-21 |
| ssbx-repo/docs-next/00_start/formal-path.md | 2,764 | 2026-05-21 |
| ssbx-repo/docs-next/00_start/gut-c-doctrine.md | 59,842 | 2026-05-21 |
| ssbx-repo/docs-next/00_start/lawvere-identification.md | 86,881 | 2026-05-21 |
| ssbx-repo/docs-next/00_start/literature-notes/path-c-foundations.md | 25,146 | 2026-05-17 |
| ssbx-repo/docs-next/00_start/maintenance-path.md | 915 | 2026-05-09 |
| ssbx-repo/docs-next/00_start/outreach/john-power-proposal.md | 26,778 | 2026-05-17 |
| ssbx-repo/docs-next/00_start/papers/README-papers.md | 7,929 | 2026-05-17 |
| ssbx-repo/docs-next/00_start/papers/cover-letter-draft.md | 12,619 | 2026-05-17 |
| ssbx-repo/docs-next/00_start/papers/gut-c-tac-submission.bib | 21,402 | 2026-05-17 |
| ssbx-repo/docs-next/00_start/papers/gut-c-tac-submission.md | 190,418 | 2026-05-17 |
| ssbx-repo/docs-next/00_start/papers/gut-c-tac-submission.tex | 114,483 | 2026-05-17 |
| ssbx-repo/docs-next/00_start/papers/mathlib-pr-1-elementary-topos.md | 3,716 | 2026-05-17 |
| ssbx-repo/docs-next/00_start/papers/mathlib-pr-2-lawvere-theory.md | 4,887 | 2026-05-21 |
| ssbx-repo/docs-next/00_start/peer-engagement-draft.md | 25,701 | 2026-05-21 |
| ssbx-repo/docs-next/00_start/phase-status.md | 29,313 | 2026-05-21 |
| ssbx-repo/docs-next/00_start/representation-closure.md | 40,748 | 2026-05-21 |
| ssbx-repo/docs-next/00_start/research-position.md | 43,043 | 2026-05-21 |
| ssbx-repo/docs-next/00_start/roadmap-self-similarity-v1.md | 40,868 | 2026-05-21 |
| ssbx-repo/docs-next/00_start/scope.md | 3,882 | 2026-05-21 |
| ssbx-repo/docs-next/00_start/session-summary-2026-05-17.md | 14,501 | 2026-05-21 |
| ssbx-repo/docs-next/00_start/theory-path.md | 1,560 | 2026-05-21 |
| ssbx-repo/docs-next/00_start/v4-foundation-roadmap.md | 17,011 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/64-hexagram-grid.md | 32,713 | 2026-05-11 |
| ssbx-repo/docs-next/10_formal_形式/E1-rtower-theta-experiment.md | 11,736 | 2026-05-18 |
| ssbx-repo/docs-next/10_formal_形式/L-tower-implementation-notes-sprint1.md | 9,741 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/L-tower-plan-v0.2.md | 37,085 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/L-tower-plan.md | 13,166 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/README.md | 5,789 | 2026-05-19 |
| ssbx-repo/docs-next/10_formal_形式/build-and-verify.md | 3,206 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/c-class-semantics-research.md | 31,826 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/cell256-algebra.md | 14,168 | 2026-05-16 |
| ssbx-repo/docs-next/10_formal_形式/cell256-grid.md | 25,873 | 2026-05-16 |
| ssbx-repo/docs-next/10_formal_形式/claim-status-ledger.md | 81,940 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/claim-z-falsification.md | 45,028 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/classical-reading-ast.md | 6,166 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/code-promise-gap.md | 129,798 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/concepts.md | 2,322 | 2026-05-08 |
| ssbx-repo/docs-next/10_formal_形式/core.md | 8,289 | 2026-05-12 |
| ssbx-repo/docs-next/10_formal_形式/daodejing-01-formalization-spec.md | 10,330 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/eight.md | 1,439 | 2026-05-08 |
| ssbx-repo/docs-next/10_formal_形式/enriched-universal-sayability-plan.md | 45,708 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/foundation-core.md | 9,552 | 2026-05-11 |
| ssbx-repo/docs-next/10_formal_形式/full-tgut-proof-plan.md | 30,044 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/gut-roadmap.md | 77,214 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/heisenberg-weyl-narrative.md | 45,840 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/jian.md | 1,323 | 2026-05-08 |
| ssbx-repo/docs-next/10_formal_形式/layer-axis-graph.md | 20,609 | 2026-05-16 |
| ssbx-repo/docs-next/10_formal_形式/layer-character-map.md | 83,976 | 2026-05-11 |
| ssbx-repo/docs-next/10_formal_形式/lift-project.md | 20,620 | 2026-05-16 |
| ssbx-repo/docs-next/10_formal_形式/modern.md | 4,108 | 2026-05-10 |
| ssbx-repo/docs-next/10_formal_形式/module-map.md | 16,165 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/operator-split.md | 16,508 | 2026-05-11 |
| ssbx-repo/docs-next/10_formal_形式/ox-notation.md | 25,681 | 2026-05-11 |
| ssbx-repo/docs-next/10_formal_形式/pending.md | 9,130 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/phase-1-4-scaffolding-handoff.md | 17,985 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/position-operator-tree.md | 35,562 | 2026-05-16 |
| ssbx-repo/docs-next/10_formal_形式/power-4.5-progress.md | 30,538 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/power-4.5-scope-decision.md | 39,380 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/quantum-roadmap.md | 102,784 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/r-attractor-capitalism.md | 21,208 | 2026-05-19 |
| ssbx-repo/docs-next/10_formal_形式/r-family-definition.md | 25,391 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/r-family-parametric-bases.md | 32,383 | 2026-05-16 |
| ssbx-repo/docs-next/10_formal_形式/r-scope-information-flow.md | 17,487 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/r1-r4-glyph-rationale.md | 20,849 | 2026-05-19 |
| ssbx-repo/docs-next/10_formal_形式/r1-r4-glyph-test.md | 9,386 | 2026-05-19 |
| ssbx-repo/docs-next/10_formal_形式/r4-r8-character-ladder.md | 13,296 | 2026-05-19 |
| ssbx-repo/docs-next/10_formal_形式/r4.md | 40,764 | 2026-05-15 |
| ssbx-repo/docs-next/10_formal_形式/r4x-r4-256-table-zi.md | 28,791 | 2026-05-12 |
| ssbx-repo/docs-next/10_formal_形式/r4x-r4-256-table.md | 25,129 | 2026-05-12 |
| ssbx-repo/docs-next/10_formal_形式/r5-glyph-rationale.md | 9,630 | 2026-05-19 |
| ssbx-repo/docs-next/10_formal_形式/r5-r6-inner-outer-rationale.md | 14,319 | 2026-05-19 |
| ssbx-repo/docs-next/10_formal_形式/r5-wuyao-provisional.md | 18,441 | 2026-05-19 |
| ssbx-repo/docs-next/10_formal_形式/r7-yin-r8-guo.md | 31,899 | 2026-05-16 |
| ssbx-repo/docs-next/10_formal_形式/r8-root-language-tree.md | 20,919 | 2026-05-12 |
| ssbx-repo/docs-next/10_formal_形式/r8.md | 54,297 | 2026-05-18 |
| ssbx-repo/docs-next/10_formal_形式/root-interpreter-unification.md | 11,727 | 2026-05-18 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/README.md | 4,980 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/all-1023.md | 324,965 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/cognitive-science-overlay.md | 10,405 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/computer-science-overlay.md | 10,431 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/confucian-overlay.md | 8,346 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/daoist-overlay.md | 9,792 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/glyph-inventory/R1-R3-operator-audit.md | 6,072 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/glyph-inventory/R4-operator-audit.md | 6,536 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/glyph-inventory/R5-operator-audit.md | 12,146 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/glyph-inventory/R5.md | 11,445 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/glyph-inventory/R6-operator-audit.md | 44,339 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/glyph-inventory/R6.md | 25,060 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/glyph-inventory/R7-operator-audit.md | 102,051 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/glyph-inventory/R7.md | 56,808 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/glyph-inventory/R8.md | 105,677 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/glyph-inventory/README.md | 1,887 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/glyph-inventory/readability-audit.md | 2,294 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/layers/R0.md | 1,016 | 2026-05-12 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/layers/R1.md | 1,146 | 2026-05-12 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/layers/R2.md | 1,901 | 2026-05-12 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/layers/R3.md | 3,405 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/layers/R4.md | 8,524 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/layers/R5.md | 19,683 | 2026-05-19 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/layers/R6.md | 33,544 | 2026-05-19 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/layers/R7.md | 85,070 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/layers/R8.md | 177,115 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/legalist-overlay.md | 6,675 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/manifest.md | 1,537 | 2026-05-12 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/naming-scheme.md | 5,174 | 2026-05-19 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/r8-64/README.md | 363 | 2026-05-12 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/r8-64/dao.md | 20,754 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/r8-64/ji.md | 21,513 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/r8-64/jin.md | 22,601 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/r8-64/wei.md | 21,961 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-language-tree/sunzi-overlay.md | 9,773 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/root-layer-map.md | 13,938 | 2026-05-19 |
| ssbx-repo/docs-next/10_formal_形式/root-native-operators.md | 3,458 | 2026-05-12 |
| ssbx-repo/docs-next/10_formal_形式/root512-v4-power.md | 2,812 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/sanben-sijieduan-grid.md | 41,041 | 2026-05-11 |
| ssbx-repo/docs-next/10_formal_形式/shi-v4.md | 25,030 | 2026-05-11 |
| ssbx-repo/docs-next/10_formal_形式/text.md | 1,993 | 2026-05-08 |
| ssbx-repo/docs-next/10_formal_形式/trust-boundaries.md | 4,440 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/truth-model.md | 1,920 | 2026-05-08 |
| ssbx-repo/docs-next/10_formal_形式/universal-claims.md | 42,015 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/v4-foundation.md | 52,271 | 2026-05-18 |
| ssbx-repo/docs-next/10_formal_形式/v4-kernel-interpreter-architecture.md | 13,175 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/v4-shi.md | 13,022 | 2026-05-11 |
| ssbx-repo/docs-next/10_formal_形式/v4-square-action-trace-calculus.md | 2,588 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/wen-2.0-spec.md | 9,683 | 2026-05-18 |
| ssbx-repo/docs-next/10_formal_形式/wen-algebra.md | 48,210 | 2026-05-19 |
| ssbx-repo/docs-next/10_formal_形式/wen-by-example.md | 35,907 | 2026-05-18 |
| ssbx-repo/docs-next/10_formal_形式/wen-classical-judgment-implementation-plan.md | 30,260 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/wen-judgment-system-plan.md | 23,130 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/wen-language-roadmap.md | 10,059 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/wen-native-expression-layers.md | 7,871 | 2026-05-19 |
| ssbx-repo/docs-next/10_formal_形式/wen-spec.md | 35,655 | 2026-05-18 |
| ssbx-repo/docs-next/10_formal_形式/wen-strata-invariants.md | 16,801 | 2026-05-18 |
| ssbx-repo/docs-next/10_formal_形式/wen-substrate.md | 3,641 | 2026-05-18 |
| ssbx-repo/docs-next/10_formal_形式/wen-substrate/00-README.md | 16,703 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/wen-substrate/01-foundations.md | 52,515 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/wen-substrate/02-parametric.md | 35,978 | 2026-05-16 |
| ssbx-repo/docs-next/10_formal_形式/wen-substrate/03-operation-monism.md | 28,618 | 2026-05-18 |
| ssbx-repo/docs-next/10_formal_形式/wen-substrate/04-rpattern.md | 7,477 | 2026-05-19 |
| ssbx-repo/docs-next/10_formal_形式/wen-substrate/05-coverage.md | 37,770 | 2026-05-19 |
| ssbx-repo/docs-next/10_formal_形式/wen-substrate/06-universal-grammar.md | 24,447 | 2026-05-18 |
| ssbx-repo/docs-next/10_formal_形式/wen-substrate/07-claim.md | 43,972 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/wen-substrate/08-obligations.md | 224,170 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/wen-to-r-code-frontend-plan.md | 23,216 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/wen.md | 3,451 | 2026-05-19 |
| ssbx-repo/docs-next/10_formal_形式/wenscript-syntax-spec.md | 25,235 | 2026-05-16 |
| ssbx-repo/docs-next/10_formal_形式/wenyan-native-syntax-spec.md | 9,315 | 2026-05-13 |
| ssbx-repo/docs-next/10_formal_形式/yi-RO-hierarchy.md | 40,938 | 2026-05-18 |
| ssbx-repo/docs-next/10_formal_形式/yi-as-meta-framework.md | 23,539 | 2026-05-18 |
| ssbx-repo/docs-next/10_formal_形式/yi-bagua.md | 23,914 | 2026-05-21 |
| ssbx-repo/docs-next/10_formal_形式/yi-calculus-theorem.md | 43,086 | 2026-05-18 |
| ssbx-repo/docs-next/10_formal_形式/yin-tou-operators.md | 12,409 | 2026-05-11 |
| ssbx-repo/docs-next/20_theory_义理/README.md | 2,798 | 2026-05-13 |
| ssbx-repo/docs-next/20_theory_义理/bridge-to-lean.md | 4,705 | 2026-05-08 |
| ssbx-repo/docs-next/20_theory_义理/core-framework.md | 9,411 | 2026-05-18 |
| ssbx-repo/docs-next/20_theory_义理/eight-expansions.md | 4,995 | 2026-05-08 |
| ssbx-repo/docs-next/20_theory_义理/extensions.md | 1,607 | 2026-05-08 |
| ssbx-repo/docs-next/20_theory_义理/formal-and-proof.md | 1,572 | 2026-05-08 |
| ssbx-repo/docs-next/20_theory_义理/map-a-g.md | 5,784 | 2026-05-08 |
| ssbx-repo/docs-next/20_theory_义理/map-h-m.md | 5,675 | 2026-05-11 |
| ssbx-repo/docs-next/20_theory_义理/map-n-t.md | 5,542 | 2026-05-08 |
| ssbx-repo/docs-next/20_theory_义理/map-u-z.md | 5,285 | 2026-05-08 |
| ssbx-repo/docs-next/20_theory_义理/modern-and-alignment.md | 1,728 | 2026-05-08 |
| ssbx-repo/docs-next/20_theory_义理/reading-order.md | 3,765 | 2026-05-08 |
| ssbx-repo/docs-next/20_theory_义理/traditions.md | 1,352 | 2026-05-08 |
| ssbx-repo/docs-next/20_theory_义理/v4-consciousness-boundary.md | 11,083 | 2026-05-18 |
| ssbx-repo/docs-next/20_theory_义理/wen-daodejing.md | 7,430 | 2026-05-13 |
| ssbx-repo/docs-next/30_crosswalk_互证/cell192-to-cell256-migration.md | 21,334 | 2026-05-21 |
| ssbx-repo/docs-next/30_crosswalk_互证/claim-status.md | 20,591 | 2026-05-21 |
| ssbx-repo/docs-next/30_crosswalk_互证/diagrams.md | 5,607 | 2026-05-21 |
| ssbx-repo/docs-next/30_crosswalk_互证/lean-to-theory.md | 12,324 | 2026-05-21 |
| ssbx-repo/docs-next/30_crosswalk_互证/old-to-new.md | 26,745 | 2026-05-21 |
| ssbx-repo/docs-next/30_crosswalk_互证/theory-to-lean.md | 10,665 | 2026-05-21 |
| ssbx-repo/docs-next/40_reference_参考/README.md | 1,106 | 2026-05-09 |
| ssbx-repo/docs-next/40_reference_参考/bagua-operator-name-candidates.md | 5,691 | 2026-05-11 |
| ssbx-repo/docs-next/40_reference_参考/glossary.md | 13,199 | 2026-05-11 |
| ssbx-repo/docs-next/40_reference_参考/glyphs-registry.md | 2,950 | 2026-05-11 |
| ssbx-repo/docs-next/40_reference_参考/historical-sources.md | 3,633 | 2026-05-11 |
| ssbx-repo/docs-next/40_reference_参考/operators.md | 23,662 | 2026-05-11 |
| ssbx-repo/docs-next/40_reference_参考/six-tables.md | 4,968 | 2026-05-11 |
| ssbx-repo/docs-next/40_reference_参考/trilingual-alignment-v1.md | 31,920 | 2026-05-11 |
| ssbx-repo/docs-next/40_reference_参考/wen-x2-16x16-structure.md | 21,338 | 2026-05-16 |
| ssbx-repo/docs-next/40_reference_参考/wen-x2-256-codes.md | 216,488 | 2026-05-16 |
| ssbx-repo/docs-next/40_reference_参考/ziwen-language.md | 2,009 | 2026-05-12 |
| ssbx-repo/docs-next/50_maintenance/README.md | 2,276 | 2026-05-12 |
| ssbx-repo/docs-next/50_maintenance/archive-policy.md | 1,641 | 2026-05-08 |
| ssbx-repo/docs-next/50_maintenance/docs-contract.md | 1,687 | 2026-05-08 |
| ssbx-repo/docs-next/50_maintenance/generation-pipeline.md | 2,060 | 2026-05-09 |
| ssbx-repo/docs-next/50_maintenance/legacy-catalogue-quarantine.md | 2,849 | 2026-05-12 |
| ssbx-repo/docs-next/50_maintenance/release-checklist.md | 1,738 | 2026-05-12 |
| ssbx-repo/docs-next/README.md | 9,095 | 2026-05-21 |
| ssbx-repo/docs-next/archive-pointers.md | 1,924 | 2026-05-21 |
| ssbx-repo/docs-next/coverage.md | 4,705 | 2026-05-21 |
| ssbx-repo/docs-next/overview.en.md | 9,528 | 2026-05-21 |
| ssbx-repo/docs-next/v4-foundation.md | 61,045 | 2026-05-21 |
| ssbx-repo/formal-notes/Attention.md | 4,215 | 2026-05-07 |
| ssbx-repo/formal-notes/ConceptDAG.md | 4,433 | 2026-05-07 |
| ssbx-repo/formal-notes/ConstructionDAG.md | 4,113 | 2026-05-07 |
| ssbx-repo/formal-notes/HumanAlignment.md | 3,424 | 2026-05-07 |
| ssbx-repo/formal-notes/JianOntology.md | 5,870 | 2026-05-07 |
| ssbx-repo/formal-notes/MissingGlyphRootReport.md | 17,741 | 2026-05-07 |
| ssbx-repo/formal-notes/MonadDAG.md | 43,535 | 2026-05-07 |
| ssbx-repo/formal-notes/PositionOperatorGraph.md | 1,562 | 2026-05-07 |
| ssbx-repo/formal-notes/atom-naming.md | 5,893 | 2026-05-07 |
| ssbx-repo/formal-notes/baguaWen-spec.md | 5,166 | 2026-05-07 |
| ssbx-repo/formal-notes/markov-causal-bridge-plan.md | 91,439 | 2026-05-10 |
| ssbx-repo/formal-notes/markov-causal-bridge-verification-plan.md | 60,346 | 2026-05-10 |
| ssbx-repo/formal-notes/math-axiom-map.md | 6,117 | 2026-05-07 |
| ssbx-repo/formal-notes/monad-root-plan.md | 6,931 | 2026-05-07 |
| ssbx-repo/formal-notes/parse-print-roadmap.md | 3,616 | 2026-05-08 |
| ssbx-repo/formal-notes/pending-interfaces.md | 17,821 | 2026-05-07 |
| ssbx-repo/formal-notes/phase1-target-definition.md | 3,602 | 2026-05-09 |
| ssbx-repo/formal-notes/run-boundary.md | 1,356 | 2026-05-07 |
| ssbx-repo/formal-notes/tier3-quine-roadmap.md | 6,432 | 2026-05-08 |
| ssbx-repo/formal-notes/truth-ledger-boundary.md | 11,814 | 2026-05-07 |
| ssbx-repo/formal-notes/unification-stepwise-plan.md | 133,171 | 2026-05-10 |
| ssbx-repo/formal-notes/v14-roadmap.md | 3,188 | 2026-05-07 |
| ssbx-repo/formal-notes/wensurface-roadmap.md | 4,298 | 2026-05-09 |
| ssbx-repo/formal-notes/wensurface-syntax-spec.md | 17,124 | 2026-05-09 |
| ssbx-repo/formal-notes/zero-axiom-roadmap.md | 12,455 | 2026-05-07 |
| ssbx-repo/formal-notes/zhouyi-position-operator-report.md | 12,641 | 2026-05-07 |
| ssbx-repo/formal-notes/自释与自证.md | 5,238 | 2026-05-07 |
| ssbx-repo/wenyan-operators.md | 185,241 | 2026-05-17 |
| ssbx-repo/ziwen-spec.md | 20,283 | 2026-05-07 |
| ssbx-repo/义理/A_经典易传.md | 2,748 | 2026-05-07 |
| ssbx-repo/义理/B_六征体系.md | 4,385 | 2026-05-07 |
| ssbx-repo/义理/Born rule推导候选 · Markov桥S18.md | 5,619 | 2026-05-09 |
| ssbx-repo/义理/Born分布边界候选 · Markov桥S12.md | 5,709 | 2026-05-09 |
| ssbx-repo/义理/Born权重条件归一候选 · Markov桥S11.md | 5,791 | 2026-05-09 |
| ssbx-repo/义理/C_实虚史真.md | 3,917 | 2026-05-07 |
| ssbx-repo/义理/Cell256_BaguaTuring_理层全集与不完备.md | 22,367 | 2026-05-11 |
| ssbx-repo/义理/D_算子代数.md | 6,153 | 2026-05-07 |
| ssbx-repo/义理/E_古代源流.md | 11,918 | 2026-05-07 |
| ssbx-repo/义理/F_物理现象学.md | 5,883 | 2026-05-08 |
| ssbx-repo/义理/G_完整算子系统_八卦互通与归一.md | 30,376 | 2026-05-11 |
| ssbx-repo/义理/H_证明报告.md | 22,744 | 2026-05-11 |
| ssbx-repo/义理/I_八卦全集.md | 32,786 | 2026-05-11 |
| ssbx-repo/义理/J_理之不完备_哥德尔在256.md | 36,083 | 2026-05-11 |
| ssbx-repo/义理/K_完备性审计.md | 25,744 | 2026-05-11 |
| ssbx-repo/义理/L_文道一也_自释与微核.md | 22,737 | 2026-05-11 |
| ssbx-repo/义理/M_证明报告_256_理之不完备.md | 20,701 | 2026-05-11 |
| ssbx-repo/义理/Markov因果桥 · 大统一最小验证构造.md | 100,294 | 2026-05-11 |
| ssbx-repo/义理/N_儒家从元到圣.md | 18,768 | 2026-05-07 |
| ssbx-repo/义理/O_进化非道者生存_三视证.md | 15,400 | 2026-05-07 |
| ssbx-repo/义理/P_道家从无到化.md | 14,244 | 2026-05-07 |
| ssbx-repo/义理/Q_佛家从苦到觉.md | 15,093 | 2026-05-07 |
| ssbx-repo/义理/README.md | 16,908 | 2026-05-12 |
| ssbx-repo/义理/R_与生生不息对齐之必然.md | 42,790 | 2026-05-07 |
| ssbx-repo/义理/S_先秦百家.md | 23,002 | 2026-05-08 |
| ssbx-repo/义理/T_西哲与亚伯拉罕.md | 15,681 | 2026-05-07 |
| ssbx-repo/义理/U_反诛心信诚之形式.md | 17,839 | 2026-05-07 |
| ssbx-repo/义理/V_现代政治哲学.md | 15,616 | 2026-05-07 |
| ssbx-repo/义理/W_非道之形式.md | 14,087 | 2026-05-07 |
| ssbx-repo/义理/WenSurface领域语义caveat细分.md | 11,441 | 2026-05-09 |
| ssbx-repo/义理/X_反施密特.md | 14,908 | 2026-05-07 |
| ssbx-repo/义理/Y_对齐失败.md | 16,568 | 2026-05-07 |
| ssbx-repo/义理/Z_平方塔自相似规则.md | 15,957 | 2026-05-11 |
| ssbx-repo/义理/Z_经济博弈.md | 17,927 | 2026-05-07 |
| ssbx-repo/义理/channelCompose候选 · Markov桥S13.md | 6,347 | 2026-05-09 |
| ssbx-repo/义理/channelCompose结合律候选 · Markov桥S14.md | 4,527 | 2026-05-09 |
| ssbx-repo/义理/sum-over-middle Born边界候选 · Markov桥S16.md | 5,352 | 2026-05-09 |
| ssbx-repo/义理/sum-over-middle通道组合候选 · Markov桥S15.md | 5,986 | 2026-05-09 |
| ssbx-repo/义理/unitary-CPTP账本边界 · Markov桥S17.md | 5,411 | 2026-05-09 |
| ssbx-repo/义理/人类命运共同体_共同体之证.md | 15,042 | 2026-05-07 |
| ssbx-repo/义理/作用相位到测量权重链 · Markov桥S22.md | 6,296 | 2026-05-09 |
| ssbx-repo/义理/作用量相位律候选 · Markov桥S5r.md | 7,484 | 2026-05-09 |
| ssbx-repo/义理/几何位 · 从元到形.md | 26,180 | 2026-05-11 |
| ssbx-repo/义理/动力 · 从元到行.md | 14,504 | 2026-05-07 |
| ssbx-repo/义理/双路径KernelPath枚举候选 · Markov桥S33.md | 6,094 | 2026-05-10 |
| ssbx-repo/义理/双路径枚举候选 · Markov桥S5j.md | 5,333 | 2026-05-09 |
| ssbx-repo/义理/双路径相消候选 · Markov桥S5c.md | 12,202 | 2026-05-09 |
| ssbx-repo/义理/双路径递归载体族完备候选 · Markov桥S32.md | 4,871 | 2026-05-10 |
| ssbx-repo/义理/史带结构 · 从爻到算子列.md | 10,187 | 2026-05-11 |
| ssbx-repo/义理/商支撑代数候选 · Markov桥S5p.md | 5,362 | 2026-05-09 |
| ssbx-repo/义理/商支撑枚举候选 · Markov桥S5o.md | 5,238 | 2026-05-09 |
| ssbx-repo/义理/干涉与测量律候选 · Markov桥S5.md | 11,952 | 2026-05-09 |
| ssbx-repo/义理/归一化质量求和候选 · Markov桥S10.md | 5,708 | 2026-05-11 |
| ssbx-repo/义理/形式逻辑 · 从元到推.md | 37,916 | 2026-05-08 |
| ssbx-repo/义理/心智 · 从元到识.md | 18,086 | 2026-05-11 |
| ssbx-repo/义理/拓扑 · 从元到障.md | 18,865 | 2026-05-07 |
| ssbx-repo/义理/数与算术 · 从元到数.md | 32,894 | 2026-05-07 |
| ssbx-repo/义理/文-R8投影规约.md | 11,476 | 2026-05-11 |
| ssbx-repo/义理/文构造完备与直相加边界.md | 4,892 | 2026-05-11 |
| ssbx-repo/义理/有限作用量极值候选 · Markov桥S26.md | 6,576 | 2026-05-09 |
| ssbx-repo/义理/有限因果区间候选 · Markov桥S28.md | 7,169 | 2026-05-09 |
| ssbx-repo/义理/有限因果局部性候选 · Markov桥S27.md | 6,591 | 2026-05-11 |
| ssbx-repo/义理/有限核路径载体候选 · Markov桥S29.md | 6,809 | 2026-05-09 |
| ssbx-repo/义理/有限概率归一化候选 · Markov桥S9.md | 6,106 | 2026-05-11 |
| ssbx-repo/义理/有限概率核接口 · Markov桥S2.md | 10,670 | 2026-05-11 |
| ssbx-repo/义理/有限相位演化候选 · Markov桥S23.md | 5,596 | 2026-05-09 |
| ssbx-repo/义理/有限路径族求和代数候选 · Markov桥S5g.md | 8,748 | 2026-05-09 |
| ssbx-repo/义理/有限路径族求和候选 · Markov桥S5f.md | 7,085 | 2026-05-09 |
| ssbx-repo/义理/有限键商候选 · Markov桥S5l.md | 6,609 | 2026-05-09 |
| ssbx-repo/义理/根算子与目录隔离.md | 2,802 | 2026-05-12 |
| ssbx-repo/义理/概率幅到测量权重 · Markov桥S21.md | 5,051 | 2026-05-09 |
| ssbx-repo/义理/爻维格算 · 物间缘与256x371拓扑.md | 18,683 | 2026-05-11 |
| ssbx-repo/义理/物理 · 从元到象.md | 17,097 | 2026-05-09 |
| ssbx-repo/义理/物间事三位一体 · 时空事件.md | 11,302 | 2026-05-09 |
| ssbx-repo/义理/生态 · 从元到生.md | 17,891 | 2026-05-07 |
| ssbx-repo/义理/离散作用量相位候选 · Markov桥S5e.md | 8,091 | 2026-05-09 |
| ssbx-repo/义理/离散相位标记候选 · Markov桥S5d.md | 8,340 | 2026-05-09 |
| ssbx-repo/义理/端点支撑规范化候选 · Markov桥S5i.md | 7,199 | 2026-05-09 |
| ssbx-repo/义理/端点索引路径族候选 · Markov桥S5h.md | 7,402 | 2026-05-09 |
| ssbx-repo/义理/端点索引递归载体族候选 · Markov桥S31.md | 4,800 | 2026-05-10 |
| ssbx-repo/义理/算子别名总表.md | 15,481 | 2026-05-07 |
| ssbx-repo/义理/类与映 · 从元到映.md | 11,317 | 2026-05-07 |
| ssbx-repo/义理/经典Markov与量子振幅分层 · Markov桥S4.md | 11,257 | 2026-05-11 |
| ssbx-repo/义理/统计 · 从元到测.md | 38,018 | 2026-05-08 |
| ssbx-repo/义理/观测账本候选 · Markov桥S5q.md | 5,657 | 2026-05-09 |
| ssbx-repo/义理/规范代表元候选 · Markov桥S5n.md | 4,202 | 2026-05-09 |
| ssbx-repo/义理/路径商类候选 · Markov桥S5m.md | 5,510 | 2026-05-09 |
| ssbx-repo/义理/路径权重乘法候选 · Markov桥S19.md | 4,928 | 2026-05-09 |
| ssbx-repo/义理/路径空间作用量泛函候选 · Markov桥S25.md | 7,577 | 2026-05-09 |
| ssbx-repo/义理/路径组合与因果约束 · Markov桥S3.md | 10,920 | 2026-05-11 |
| ssbx-repo/义理/路径身份键候选 · Markov桥S5k.md | 6,155 | 2026-05-09 |
| ssbx-repo/义理/边界/README.md | 2,718 | 2026-05-08 |
| ssbx-repo/义理/边界/可的边界 · 感行证.md | 16,202 | 2026-05-09 |
| ssbx-repo/义理/边界/可知边界 · 语言与理.md | 14,359 | 2026-05-09 |
| ssbx-repo/义理/边界/名的边界 · 指称定名.md | 5,434 | 2026-05-08 |
| ssbx-repo/义理/边界/四界不混同 · 测量推感.md | 4,532 | 2026-05-08 |
| ssbx-repo/义理/边界/感的边界 · 受觉现.md | 6,412 | 2026-05-08 |
| ssbx-repo/义理/边界/推的边界 · 前规则结.md | 8,083 | 2026-05-08 |
| ssbx-repo/义理/边界/测的边界 · 观验读.md | 15,671 | 2026-05-08 |
| ssbx-repo/义理/边界/知的边界 · 明辨述.md | 4,961 | 2026-05-08 |
| ssbx-repo/义理/边界/统一边界 · 从理到文.md | 11,945 | 2026-05-08 |
| ssbx-repo/义理/边界/行的边界 · 能境作效.md | 4,580 | 2026-05-08 |
| ssbx-repo/义理/边界/证的边界 · 命题系统证书.md | 4,793 | 2026-05-08 |
| ssbx-repo/义理/边界/边界总图谱 · 知感行证名量测推.md | 7,801 | 2026-05-08 |
| ssbx-repo/义理/边界/量的边界 · 数测度.md | 17,043 | 2026-05-08 |
| ssbx-repo/义理/连续作用量泛函候选 · Markov桥S24.md | 7,076 | 2026-05-09 |
| ssbx-repo/义理/逐步统一候选摘要 · Markov桥S8.md | 6,950 | 2026-05-11 |
| ssbx-repo/义理/递归核路径载体候选 · Markov桥S30.md | 5,463 | 2026-05-09 |
| ssbx-repo/义理/道桥接_ProcessAligned_Dao_ShengshengBuxi.md | 5,931 | 2026-05-07 |
| ssbx-repo/义理/量子与相对论整合方向 · 从桥到新理论.md | 13,094 | 2026-05-11 |
| ssbx-repo/义理/量子与相对论直统一不可能 · 当前语言NoGo.md | 9,905 | 2026-05-11 |
| ssbx-repo/义理/量子时空互补 · 从一到测.md | 14,069 | 2026-05-11 |
| ssbx-repo/义理/量子物理语言 · 从虚到测.md | 21,925 | 2026-05-08 |
| ssbx-repo/义理/非平凡量子通道律候选 · Markov桥S20.md | 6,279 | 2026-05-09 |
| ssbx-repo/义理/非零路径振幅候选 · Markov桥S5b.md | 11,383 | 2026-05-09 |
| ssbx-repo/六表_实虚史真/表一_六征本表.md | 2,654 | 2026-05-06 |
| ssbx-repo/六表_实虚史真/表三_实虚modal三态.md | 3,926 | 2026-05-06 |
| ssbx-repo/六表_实虚史真/表二_史维三态.md | 3,113 | 2026-05-06 |
| ssbx-repo/六表_实虚史真/表五_三轴27格.md | 5,114 | 2026-05-06 |
| ssbx-repo/六表_实虚史真/表六_256格全表.md | 77,645 | 2026-05-11 |
| ssbx-repo/六表_实虚史真/表四_真假认识三态.md | 4,202 | 2026-05-06 |
| ssbx-repo/史/README.md | 2,047 | 2026-05-11 |
| ssbx-repo/史/daoli旧版/daoli-v11.1.md | 20,917 | 2026-05-11 |
| ssbx-repo/史/daoli旧版/daoli-v11.md | 44,439 | 2026-05-11 |
| ssbx-repo/史/daoli旧版/daoli-v12.md | 56,424 | 2026-05-11 |
| ssbx-repo/史/docs-next-pre-v3/cell192-grid_Z3-Shi_旧版.md | 33,781 | 2026-05-11 |
| ssbx-repo/史/docs-next-pre-v3/yi-RO-hierarchy_v1_旧R1-R6编号.md | 42,139 | 2026-05-11 |
| ssbx-repo/史/义理-pre-v3/Cell192_BaguaTuring_理层全集与不完备.md | 22,367 | 2026-05-11 |
| ssbx-repo/史/义理-pre-v3/M_证明报告_192_理之不完备.md | 20,701 | 2026-05-11 |
| ssbx-repo/史/义理-pre-v3/表六_192格全表_旧Z3版.md | 6,814 | 2026-05-11 |
| ssbx-repo/史/探索/v9_v10_过渡_生生不息.md | 17,148 | 2026-05-11 |
| ssbx-repo/史/间论早期/间本体论_元三相与场修订稿.md | 4,305 | 2026-05-11 |
| ssbx-repo/史料/README.md | 6,152 | 2026-05-07 |
| ssbx-repo/史料/atom-derivation-report.md | 5,534 | 2026-05-07 |
| ssbx-repo/史料/生生不息论_v14_形式证明骨架版.md | 16,043 | 2026-05-07 |
| ssbx-repo/史料/生生不息论_三本文完整版.md | 400 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/00_编校说明/00_生生不息论_三本文完整版.md | 149 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/00_编校说明/01_编校说明.md | 2,472 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/00_编校说明/02_词汇迁移与早期方向.md | 5,526 | 2026-05-07 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/00_正篇_v13_2_形式项总清与类型校正版.md | 53 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/01_生生不息论.md | 1,684 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/02_卷〇_全字元生成律.md | 8,149 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/03_卷一_字元义位表.md | 9,686 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/04_卷二_原始域与原始算子.md | 3,991 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/05_卷三_由显至间.md | 2,003 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/06_卷四_元、几、势、机.md | 1,416 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/07_卷五_史法、暂法、开维法.md | 1,582 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/08_卷六_开、闭、稳、真.md | 4,904 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/09_卷七_审校全拆.md | 7,911 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/10_卷八_共开、夺、护.md | 2,050 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/11_卷九_正邪.md | 2,630 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/12_卷十_平、和、好、坏.md | 1,433 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/13_卷十一_自由、繁荣、义、善、仁、道.md | 4,175 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/14_卷十二_心、情、知、智、礼、信、责、性.md | 1,971 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/15_卷十三_递归与不动点.md | 2,713 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/16_卷十四_判定协议.md | 1,783 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/17_卷十五_反例校验.md | 1,465 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/18_卷十六_终图.md | 1,818 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/19_卷十七_总链与全式.md | 2,394 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/20_卷十八_终言.md | 991 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/21_附录甲_形式项总清.md | 5,228 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/01_正篇_v13.2形式项总清与类型校正版/22_附录乙_v13_2_自检表.md | 7,294 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/02_补篇〇_可运行模型与实例化校正版/00_补篇〇_可运行模型与实例化校正版.md | 642 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/02_补篇〇_可运行模型与实例化校正版/01_〇一、可运行输入与输出.md | 974 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/02_补篇〇_可运行模型与实例化校正版/02_〇二、四维开度特征.md | 1,273 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/02_补篇〇_可运行模型与实例化校正版/03_〇三、_Omega_的三种模型.md | 1,433 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/02_补篇〇_可运行模型与实例化校正版/04_〇四、_Omega_B_的三种模型.md | 1,550 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/02_补篇〇_可运行模型与实例化校正版/05_〇五、_Pi_mathrm_开_的场景化投影协议.md | 1,444 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/02_补篇〇_可运行模型与实例化校正版/06_〇六、审校数据结构.md | 1,925 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/02_补篇〇_可运行模型与实例化校正版/07_〇七、阈值设定法.md | 1,025 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/02_补篇〇_可运行模型与实例化校正版/08_〇八、判定伪代码.md | 896 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/02_补篇〇_可运行模型与实例化校正版/09_〇九、最小跑通案例_推荐系统与共开.md | 3,890 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/02_补篇〇_可运行模型与实例化校正版/10_〇十、本补篇完成项.md | 1,065 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版/00_补篇一_间开本_致知版_全量收入.md | 57 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版/01_生生不息论.md | 4,345 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版/02_卷一_立位.md | 5,947 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版/03_卷二_发生.md | 10,980 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版/04_卷三_判准.md | 12,320 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版/05_卷四_境与模.md | 7,363 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版/06_卷五_价值之相.md | 9,933 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版/07_卷六_心物.md | 3,500 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版/08_卷七_道之相.md | 15,091 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版/09_卷八_五常.md | 6,458 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版/10_卷九_行与性.md | 1,835 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版/11_卷十_收.md | 6,203 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版/12_四十二、终式.md | 3,549 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版/13_终言.md | 2,753 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版_古文证明版/00_补篇一_间开本_致知版_全量收入.md | 1,061 | 2026-05-05 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版_古文证明版/01_生生不息论.md | 973 | 2026-05-05 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版_古文证明版/02_卷一_立位.md | 979 | 2026-05-05 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版_古文证明版/03_卷二_发生.md | 854 | 2026-05-05 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版_古文证明版/04_卷三_判准.md | 961 | 2026-05-05 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版_古文证明版/05_卷四_境与模.md | 963 | 2026-05-05 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版_古文证明版/06_卷五_价值之相.md | 878 | 2026-05-05 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版_古文证明版/07_卷六_心物.md | 893 | 2026-05-05 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版_古文证明版/08_卷七_道之相.md | 911 | 2026-05-05 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版_古文证明版/09_卷八_五常.md | 857 | 2026-05-05 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版_古文证明版/10_卷九_行与性.md | 851 | 2026-05-05 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版_古文证明版/11_卷十_收.md | 977 | 2026-05-05 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版_古文证明版/12_四十二、终式.md | 1,028 | 2026-05-05 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版_古文证明版/13_终言.md | 844 | 2026-05-05 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版_古文证明版/README.md | 1,021 | 2026-05-05 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版_古文证明版/manifest.json | 5,312 | 2026-05-05 |
| ssbx-repo/史料/生生不息论_三本文完整版/03_补篇一_间开本_致知版_古文证明版/缺字记录.md | 546 | 2026-05-05 |
| ssbx-repo/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/00_补篇二_间生论_主篇_全量收入.md | 54 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/01_间生论_主篇.md | 66 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/02_序.md | 1,005 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/03_一、间.md | 1,324 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/04_二、元、几、势、机.md | 2,788 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/05_三、聚散.md | 813 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/06_四、开闭.md | 2,465 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/07_五、境与道.md | 3,184 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/08_六、中、和、美、德.md | 2,687 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/09_七、理、心、情、积.md | 2,291 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/10_八、自相似之节.md | 2,088 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/11_九、因生因.md | 1,691 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/12_十、宇宙即理_是为吾性.md | 2,711 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/13_十一、善恶之本.md | 1,863 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/14_十二、仁、义、礼、智、信.md | 4,330 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/15_十三、行仁要善_alignment_之真义.md | 2,632 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/16_十四、终言.md | 988 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/05_合订版结语/00_合订版结语.md | 702 | 2026-05-04 |
| ssbx-repo/史料/生生不息论_三本文完整版/README.md | 7,969 | 2026-05-07 |
| ssbx-repo/史料/生生不息论_三本文完整版/manifest.json | 16,909 | 2026-05-04 |
| ssbx-repo/史料/真理/daoli-v12-cross-cultural.md | 66,198 | 2026-05-06 |
| ssbx-repo/史料/真理/daoli-v12-fa-ze.md | 84,253 | 2026-05-07 |
| ssbx-repo/史料/真理/daoli-v12-frames.md | 66,682 | 2026-05-06 |
| ssbx-repo/史料/真理/daoli-v12-he.md | 37,784 | 2026-05-07 |
| ssbx-repo/史料/真理/daoli-v12-implications.md | 11,469 | 2026-05-07 |
| ssbx-repo/史料/真理/daoli-v12-lean-verifier.md | 42,922 | 2026-05-06 |
| ssbx-repo/史料/真理/daoli-v12-main.md | 64,043 | 2026-05-07 |
| ssbx-repo/史料/真理/daoli-v12-physics-emergence.md | 26,445 | 2026-05-06 |
| ssbx-repo/史料/真理/daoli-v12-theories.md | 86,167 | 2026-05-06 |
| ssbx-repo/史料/真理/daoli-v12-verifications.md | 47,331 | 2026-05-07 |
| ssbx-repo/史料/真理/daoli-v12-yi-zi.md | 39,448 | 2026-05-07 |
| ssbx-repo/史料/真理/urbit-jian-isomorphism.md | 9,387 | 2026-05-06 |

### 08-jian-wen-language

| file | bytes | date |
|---|---:|---|
| downloads-2026-05/jian-ontology-v7.1.md | 72,948 | 2026-05-05 |
| downloads-2026-05/jian-ontology-v7.md | 63,634 | 2026-05-05 |
| downloads-2026-05/r_family_v_0_8_revision_notes.md | 37,903 | 2026-05-15 |
| downloads-2026-05/v4-foundation (1).md | 56,565 | 2026-05-12 |
| downloads-2026-05/wen-algebra (4).md | 51,309 | 2026-05-15 |
| downloads-2026-05/wen-algebra-v0.5-x16-corrected.md | 20,906 | 2026-05-14 |
| downloads-2026-05/wen-formal (1).md | 63,179 | 2026-05-15 |
| downloads-2026-05/wen-handoff.md | 24,780 | 2026-05-13 |
| downloads-2026-05/wen-info-paradigm.md | 26,348 | 2026-05-13 |
| downloads-2026-05/wen-layered.md | 34,797 | 2026-05-13 |
| downloads-2026-05/wen-substrate (1).md | 99,000 | 2026-05-15 |
| downloads-2026-05/wen-v4n-algebra.md | 22,301 | 2026-05-14 |
| downloads-2026-05/wen-vs-qpls.md | 22,391 | 2026-05-13 |
| downloads-2026-05/仪.md | 34,879 | 2026-05-02 |
| downloads-2026-05/器.md | 40,653 | 2026-05-02 |
| downloads-2026-05/式.md | 31,924 | 2026-05-02 |
| downloads-2026-05/构.md | 35,454 | 2026-05-02 |
| downloads-2026-05/气.md | 31,893 | 2026-05-02 |
| downloads-2026-05/理：间.md | 40,643 | 2026-05-02 |
| downloads-2026-05/间.md | 38,843 | 2026-05-02 |
| jian-repo/JIAN_FOUNDATION_NOTE_v0.3.md | 42,202 | 2026-05-01 |
| jian-repo/JIAN_FOUNDATION_NOTE_v0.5.md | 83,908 | 2026-05-01 |
| jian-repo/JIAN_FOUNDATION_NOTE_v0.6.md | 49,610 | 2026-05-01 |
| jian-repo/JIAN_FOUNDATION_NOTE_v0.7.md | 52,084 | 2026-05-01 |
| jian-repo/JIAN_FOUNDATION_NOTE_v0.8.md | 65,429 | 2026-05-01 |
| jian-repo/JIAN_FOUNDATION_NOTE_v0.9.md | 66,736 | 2026-05-01 |
| jian-repo/JIAN_FOUNDATION_NOTE_v1.0.md | 32,157 | 2026-05-02 |
| jian-repo/WENYAN_FOUNDATION_NOTE_v1.0.md | 141,880 | 2026-05-02 |

### 09-sts-bonfire-yi

| file | bytes | date |
|---|---:|---|
| 2025-08-STS-spirit-token-space-paper.md | 102,012 | 2025-08-10 |
| 2025-08-USIS-review.md | 54,717 | 2025-08-10 |
| bonfire-concepts/README.md | 5,046 | 2026-08-30 |
| bonfire-concepts/VOCABULARY.md | 3,481 | 2026-08-28 |
| bonfire-concepts/authority.md | 2,931 | 2026-08-24 |
| bonfire-concepts/bonfire-use-cases-and-possibilities.md | 33,542 | 2026-09-01 |
| bonfire-concepts/community.md | 4,311 | 2026-08-24 |
| bonfire-concepts/composition.md | 708 | 2026-08-24 |
| bonfire-concepts/dimensions.md | 814 | 2026-08-27 |
| bonfire-concepts/encoded-implementation.md | 805 | 2026-08-24 |
| bonfire-concepts/federation-layer2.md | 955 | 2026-08-24 |
| bonfire-concepts/federation-layer2c.md | 808 | 2026-08-24 |
| bonfire-concepts/federation.md | 1,510 | 2026-08-24 |
| bonfire-concepts/glossary.md | 9,832 | 2026-09-01 |
| bonfire-concepts/hearth.md | 2,614 | 2026-08-29 |
| bonfire-concepts/holdings-dimensions.md | 2,095 | 2026-08-27 |
| bonfire-concepts/holdings.md | 5,861 | 2026-08-30 |
| bonfire-concepts/items.md | 979 | 2026-08-27 |
| bonfire-concepts/lifecycle.md | 769 | 2026-08-22 |
| bonfire-concepts/messages.md | 15,168 | 2026-08-30 |
| bonfire-concepts/overview.md | 2,528 | 2026-09-01 |
| bonfire-concepts/port-gate-grant.md | 3,026 | 2026-08-27 |
| bonfire-concepts/ports-and-faces.md | 2,537 | 2026-08-24 |
| bonfire-concepts/relationships.md | 784 | 2026-08-22 |
| bonfire-concepts/session.md | 2,327 | 2026-08-24 |
| bonfire-concepts/sigil-replies.md | 6,219 | 2026-06-13 |
| bonfire-concepts/spirits.md | 4,035 | 2026-09-01 |
| bonfire-concepts/the-frame.md | 309 | 2026-06-21 |
| bonfire-concepts/tokens.md | 1,136 | 2026-08-22 |
| bonfire-concepts/touch-lifecycle.md | 1,824 | 2026-08-24 |
| bonfire-concepts/unified-class.md | 5,641 | 2026-09-01 |
| bonfire-concepts/visibility.md | 2,125 | 2026-08-24 |
| bonfire-concepts/yi.md | 4,946 | 2026-09-01 |
| bonfire-docs-yi/00-direction.md | 9,820 | 2026-08-29 |
| bonfire-docs-yi/01-frame.md | 29,836 | 2026-09-01 |
| bonfire-docs-yi/02-pivot.md | 56,058 | 2026-08-15 |
| bonfire-docs-yi/06-unification.md | 48,814 | 2026-08-15 |
| bonfire-docs-yi/08-ideal-architecture.md | 12,002 | 2026-06-26 |
| bonfire-docs-yi/24-projection-stance.md | 3,009 | 2026-09-01 |
| bonfire-docs-yi/README.md | 5,099 | 2026-09-02 |
| bonfire-docs-yi/sdk-elegance-exploration.md | 134,378 | 2026-09-02 |
| bonfire-docs-yi/sdk-one-model-direction.md | 69,370 | 2026-09-03 |
| bonfire-proposals/community.md | 2,900 | 2026-08-15 |
| bonfire-proposals/design/frame-pivot-adversarial-review-2026-06-19.md | 22,000 | 2026-07-10 |
| bonfire-proposals/design/frame-pivot-claim-audit-2026-06-19.md | 10,316 | 2026-07-10 |
| bonfire-proposals/design/frame-pivot-claim-audit.md | 8,596 | 2026-07-08 |
| bonfire-proposals/design/frame-pivot-evaluation.md | 12,160 | 2026-07-08 |
| bonfire-proposals/design/stream-tier-conceptualization-2026-06-21.md | 29,475 | 2026-08-15 |
| bonfire-proposals/design/the-pivot.md | 342 | 2026-08-15 |
| bonfire-proposals/platform.md | 9,778 | 2026-08-15 |

### 10-context-runtime-ember

| file | bytes | date |
|---|---:|---|
| context-runtime-specs/012-composable-context-systems.md | 4,121 | 2026-08-09 |
| context-runtime-specs/013-gtc-confluence.md | 6,042 | 2026-08-09 |
| context-runtime-specs/016-stage-10-multi-agent.md | 21,078 | 2026-08-11 |
| context-runtime-specs/017-temporal-durable-execution.md | 13,337 | 2026-08-10 |
| context-runtime-specs/019-history-context-authority-boundaries.md | 13,361 | 2026-08-21 |
| context-runtime-specs/030-everything-is-a-plugin.md | 133,689 | 2026-08-23 |
| context-runtime-specs/031-composition-is-the-guard.md | 18,208 | 2026-08-22 |
| context-runtime-specs/2026-08-07-Context-Runtime-plan-v0.1.md | 45,011 | 2026-08-07 |
| context-runtime-specs/2026-08-07-设计意图书-v0.1.md | 8,036 | 2026-08-07 |
| context-runtime-specs/2026-08-13-context-runtime-spec-v0.1-downloads.md | 22,997 | 2026-08-13 |
| context-runtime-specs/CONSTRUCTION_CONSTITUTION_LITE.md | 1,400 | 2026-04-26 |
| context-runtime-specs/context-runtime-spec-v0.1.md | 22,997 | 2026-08-14 |
| context-runtime-specs/decisions.md | 32,169 | 2026-08-22 |
| context-runtime-specs/history-kernel-mediated-runtime.md | 106,672 | 2026-08-22 |
| context-runtime-specs/plan.md | 132,363 | 2026-08-21 |
| ember/IDENTITY.md | 100 | 2026-08-03 |
| ember/PLAN-LEAN.md | 37,885 | 2026-08-04 |
| ember/PLAN-LIFE.md | 15,918 | 2026-08-05 |
| ember/PLAN.md | 32,472 | 2026-07-30 |
| ember/POLICY.md | 206 | 2026-08-03 |
| ember/README.md | 4,031 | 2026-08-04 |
| ember/SPEC.md | 46,687 | 2026-07-29 |
| ember/reviews/2026-07-29-shell-panel.md | 19,487 | 2026-07-29 |
| ember/reviews/engineering/A-api-reality.md | 11,573 | 2026-07-29 |
| ember/reviews/engineering/B-moment-boundary.md | 12,552 | 2026-07-29 |
| ember/reviews/engineering/C-elegance-longtermism.md | 14,423 | 2026-07-29 |
| ember/reviews/external/codex-gpt-5.md | 35,065 | 2026-07-29 |
| ember/reviews/panel/D-pragmatist-skeptic.md | 8,642 | 2026-07-29 |
| ember/reviews/panel/E-long-lived-mind.md | 12,174 | 2026-07-29 |
| ember/reviews/panel/F-inhabitant.md | 11,729 | 2026-07-29 |
| ember/reviews/panel/G-counterfactual-architect.md | 12,877 | 2026-07-29 |
| ember/reviews/plan/H-observability.md | 11,856 | 2026-07-30 |
| ember/reviews/plan/I-kernel-critic.md | 14,659 | 2026-07-30 |
| ember/reviews/plan/J-evolvability.md | 20,628 | 2026-07-30 |
| ember/reviews/plan/K-simplification.md | 11,413 | 2026-07-30 |
| ember/reviews/plan/L-coherence-audit.md | 19,675 | 2026-07-30 |
| ember/reviews/plan/M-biology.md | 11,778 | 2026-08-04 |
| ember/reviews/plan/N-execution-fable.md | 14,183 | 2026-08-04 |
| ember/reviews/plan/N-execution-opus.md | 16,171 | 2026-08-04 |
| ember/reviews/plan/O-v07-concept.md | 12,300 | 2026-08-04 |
| ember/reviews/plan/O-v07-executable.md | 13,256 | 2026-08-04 |
| ember/reviews/probe-01.json | 13,674 | 2026-08-04 |
| ember/reviews/probe-01.md | 11,750 | 2026-08-04 |
| ember/reviews/probe-02.json | 1,349 | 2026-08-04 |
| ember/reviews/probe-02.md | 3,329 | 2026-08-04 |
| ember/reviews/probe-03.md | 3,386 | 2026-08-04 |
| ember/reviews/probe-04.md | 2,421 | 2026-08-04 |
| ember/reviews/probe-05.md | 2,347 | 2026-08-04 |
| ember/reviews/probe-06.md | 2,814 | 2026-08-05 |
| gtc/GTC_Generative_Topological_Context_v0.1.md | 64,972 | 2026-08-09 |
| gtc/GTC_Generative_Topological_Context_v0.2.md | 99,082 | 2026-08-09 |
| gtc/README.md | 641 | 2026-08-09 |
| gtc/deep-research-1.md | 81,944 | 2026-08-09 |
| gtc/deep-research-2.md | 44,474 | 2026-08-09 |
| gtc/deep-research-report-gtc-1.md | 81,944 | 2026-08-09 |
| gtc/deep-research-report-gtc-2.md | 44,474 | 2026-08-09 |
| gtc/v0.1.md | 64,972 | 2026-08-09 |
| gtc/v0.2.md | 99,082 | 2026-08-09 |
| other-runtimes/0001-product-application-modular-monolith.md | 1,713 | 2026-08-04 |
| other-runtimes/0002-functional-core-effect-shell.md | 1,958 | 2026-08-04 |
| other-runtimes/0003-contracts-and-command-query-paths.md | 2,020 | 2026-08-04 |
| other-runtimes/0004-polyglot-workload-extraction.md | 1,976 | 2026-08-04 |
| other-runtimes/2026-03-28-ember-openclaw-assistant-system-prompt.md | 7,675 | 2026-03-28 |
| other-runtimes/2026-04-05-FNAR-filesystem-native-agent-runtime-spec-v1.md | 47,276 | 2026-04-05 |
| other-runtimes/2026-08-09-runtime-boundary-notes.md | 2,963 | 2026-08-09 |
| other-runtimes/2026-08-30-manifold-product-split.md | 29,193 | 2026-08-31 |
| other-runtimes/manifold-AGENTS.md | 5,284 | 2026-08-31 |
| other-runtimes/multibot-README.md | 10,981 | 2026-04-24 |
| other-runtimes/obji-README.md | 12,641 | 2026-03-16 |
| other-runtimes/server-runtime-PLAN.md | 42,489 | 2026-08-19 |
| other-runtimes/server-runtime-README.md | 5,375 | 2026-08-31 |

### 11-human-solutions-museum

| file | bytes | date |
|---|---:|---|
| agent.md | 1,179 | 2026-07-05 |
| content-assets-production.md | 9,285 | 2026-07-05 |
| content-engineering-audit.md | 4,067 | 2026-07-05 |
| engineering-implementation-spec.md | 24,868 | 2026-07-05 |
| 人类解决问题的方法博物馆-方向定稿.md | 10,090 | 2026-07-05 |
| 可交互网页-最终执行预期.md | 16,212 | 2026-07-05 |

### 12-claude-ai-chats

403 files. Indexes: `_SELECTED-INDEX.tsv` (date, title, messages, chars, Ren-chars, filename) and `_ALL-719-INDEX.tsv` listing the complete export including the 338 conversations not selected.

### 13-claude-memories

| file | bytes | date |
|---|---:|---|
| claude-ai-memory-summary-2026-03-29.md | 6,673 | 2026-09-03 |
| claude-ai-memory-summary-2026-05-05.md | 6,954 | 2023-11-02 |
| claude-code--------/MEMORY.md | 291 | 2026-05-06 |
| claude-code--------/project_ssbx_framing.md | 2,207 | 2026-05-06 |
| claude-code--------/reference_ssbx_corpus.md | 2,873 | 2026-05-06 |
| claude-code-----/MEMORY.md | 7,317 | 2026-05-21 |
| claude-code-----/feedback_agent_worktree_discipline.md | 1,821 | 2026-05-21 |
| claude-code-----/feedback_dont_drop_theorems.md | 1,391 | 2026-05-16 |
| claude-code-----/feedback_lean_cjk_identifiers.md | 1,696 | 2026-05-07 |
| claude-code-----/feedback_lean_syntax_cjk.md | 1,656 | 2026-05-07 |
| claude-code-----/feedback_minimal_builds.md | 1,208 | 2026-05-15 |
| claude-code-----/feedback_no_axiom_for_zero_sorry.md | 3,419 | 2026-05-17 |
| claude-code-----/project_2026-05-21_doc_sync.md | 3,359 | 2026-05-21 |
| claude-code-----/project_daosource_complete.md | 1,831 | 2026-05-07 |
| claude-code-----/project_e1_rtower_rh_closed.md | 3,335 | 2026-05-18 |
| claude-code-----/project_final_theory_2026-05-10.md | 1,990 | 2026-05-11 |
| claude-code-----/project_metainterp_phaseA.md | 2,791 | 2026-05-08 |
| claude-code-----/project_metainterp_phaseC_partial.md | 3,986 | 2026-05-08 |
| claude-code-----/project_operation_monism.md | 5,105 | 2026-05-16 |
| claude-code-----/project_operator_metadata_layer.md | 2,511 | 2026-05-07 |
| claude-code-----/project_phase23_done.md | 2,744 | 2026-05-08 |
| claude-code-----/project_phase4_complete.md | 2,603 | 2026-05-08 |
| claude-code-----/project_phaseA_algebraic_spine.md | 1,914 | 2026-05-10 |
| claude-code-----/project_phaseG_complete.md | 3,588 | 2026-05-15 |
| claude-code-----/project_renlei_complete.md | 2,099 | 2026-05-07 |
| claude-code-----/project_squaring_tower.md | 2,046 | 2026-05-11 |
| claude-code-----/project_v4_migration_complete.md | 3,106 | 2026-05-10 |
| claude-code-----/project_v4_shi_doctrine_out_2026-05-17.md | 2,066 | 2026-05-17 |
| claude-code-----/project_wen_1_5_usable_interpreter_2026-05-17.md | 2,961 | 2026-05-17 |
| claude-code-----/project_wen_2_0_complete_2026-05-17.md | 4,198 | 2026-05-17 |
| claude-code-----/project_wen_4gaps_closed_2026-05-18.md | 3,302 | 2026-05-18 |
| claude-code-----/project_wen_language_state_2026-05-17.md | 2,187 | 2026-05-17 |
| claude-code-----/project_wen_restructure_complete_2026-05-17.md | 3,676 | 2026-05-17 |
| claude-code-----/project_x2codes_ug_complete.md | 6,136 | 2026-05-16 |
| claude-code-----/project_yiinstr_cuo_ceiling.md | 1,901 | 2026-05-17 |
| claude-code-----/project_yuan_yao_duality.md | 2,002 | 2026-05-11 |
| claude-code-----/reference_claim_status_ledger.md | 1,966 | 2026-05-21 |
| claude-code-----/reference_hw_narrative.md | 2,174 | 2026-05-21 |
| claude-code-alignment/MEMORY.md | 414 | 2026-05-28 |
| claude-code-alignment/feedback_research_mode.md | 1,050 | 2026-05-28 |
| claude-code-alignment/project_user_framework.md | 3,803 | 2026-05-28 |
| claude-code-alignment/user_role.md | 591 | 2026-05-28 |
| claude-code-bonfire/MEMORY.md | 18,566 | 2026-09-03 |
| claude-code-bonfire/app_record_race_fix.md | 1,000 | 2026-08-15 |
| claude-code-bonfire/architecture_c_complete.md | 1,119 | 2026-08-15 |
| claude-code-bonfire/atproto_lessons_plan2.md | 1,028 | 2026-08-15 |
| claude-code-bonfire/automation_reaction_holding_face_bridge.md | 1,252 | 2026-08-15 |
| claude-code-bonfire/bonfirex_database_direction.md | 1,188 | 2026-08-15 |
| claude-code-bonfire/bundle3_ws_decomposition.md | 1,119 | 2026-08-15 |
| claude-code-bonfire/cert_native_storage_design.md | 1,242 | 2026-08-15 |
| claude-code-bonfire/chat_branching_shipped.md | 1,212 | 2026-08-15 |
| claude-code-bonfire/class_route_kind_projection.md | 1,303 | 2026-08-15 |
| claude-code-bonfire/computation_service_wall.md | 1,473 | 2026-08-15 |
| claude-code-bonfire/consolidation_execution_2026-06.md | 1,193 | 2026-08-15 |
| claude-code-bonfire/container_primitive_gap.md | 1,487 | 2026-08-15 |
| claude-code-bonfire/core_naming_review_2026-07-11.md | 1,088 | 2026-08-15 |
| claude-code-bonfire/ctx_atomic_real_transaction.md | 1,515 | 2026-08-15 |
| claude-code-bonfire/ctx_transfer_verbs_shipped.md | 1,425 | 2026-08-15 |
| claude-code-bonfire/data_model_review_2026-06-11.md | 1,575 | 2026-08-15 |
| claude-code-bonfire/doorway_welcome_migration.md | 1,227 | 2026-08-15 |
| claude-code-bonfire/e2_two_commit_law_mechanism.md | 1,699 | 2026-08-15 |
| claude-code-bonfire/edge_bond_capability_arc.md | 1,773 | 2026-08-15 |
| claude-code-bonfire/event_payload_snapshot_invariant.md | 1,232 | 2026-08-15 |
| claude-code-bonfire/event_time_yi_fold_coverage_gap.md | 3,287 | 2026-08-29 |
| claude-code-bonfire/examples_test_leg_masked_by_build_bail.md | 1,048 | 2026-08-15 |
| claude-code-bonfire/extension_model_tier_a.md | 1,349 | 2026-08-15 |
| claude-code-bonfire/feedback_model_tiering_workflows.md | 1,152 | 2026-08-15 |
| claude-code-bonfire/feedback_no_backwards_compat.md | 1,467 | 2026-08-15 |
| claude-code-bonfire/feedback_no_clarifying_questions.md | 1,001 | 2026-08-15 |
| claude-code-bonfire/feedback_no_word_pinning.md | 1,916 | 2026-08-15 |
| claude-code-bonfire/feedback_owner_docs_readable.md | 1,573 | 2026-08-15 |
| claude-code-bonfire/feedback_owner_manages_commits.md | 1,812 | 2026-08-15 |
| claude-code-bonfire/feedback_sdk_is_a_kit.md | 1,870 | 2026-08-15 |
| claude-code-bonfire/feedback_thinking_partner.md | 1,146 | 2026-08-15 |
| claude-code-bonfire/feedback_verification_economics.md | 1,860 | 2026-08-15 |
| claude-code-bonfire/goal_exec_2026-06-30.md | 1,097 | 2026-08-15 |
| claude-code-bonfire/grab_bag_dissolution_finished.md | 836 | 2026-08-15 |
| claude-code-bonfire/grab_bag_dissolution_shipped.md | 899 | 2026-08-15 |
| claude-code-bonfire/hardening_p1_p7_2026-06-07.md | 1,099 | 2026-08-15 |
| claude-code-bonfire/hardening_to_9_2026-06-14.md | 834 | 2026-08-15 |
| claude-code-bonfire/hero_as_principal.md | 931 | 2026-08-15 |
| claude-code-bonfire/holding_authority_phase1.md | 1,147 | 2026-08-15 |
| claude-code-bonfire/horizontal_scaling_plan3.md | 1,236 | 2026-08-15 |
| claude-code-bonfire/ideal_yi_architecture.md | 2,036 | 2026-08-15 |
| claude-code-bonfire/kernel_decoupling_design_2026-06-16.md | 1,442 | 2026-08-15 |
| claude-code-bonfire/kernel_uid_is_not_an_ambient_reader.md | 1,391 | 2026-08-15 |
| claude-code-bonfire/keypair_accounts_shipped.md | 1,950 | 2026-08-15 |
| claude-code-bonfire/kit_index_race_fix.md | 1,752 | 2026-08-15 |
| claude-code-bonfire/linearization_memo_is_inert_on_purpose.md | 1,658 | 2026-08-15 |
| claude-code-bonfire/listener_reactor_design.md | 1,564 | 2026-08-15 |
| claude-code-bonfire/live_fanout_scalability.md | 2,157 | 2026-08-15 |
| claude-code-bonfire/local_run_setup.md | 1,432 | 2026-08-15 |
| claude-code-bonfire/main_checkout_phase6_census_blocked.md | 1,159 | 2026-08-15 |
| claude-code-bonfire/merge_drop_audit_2026-06-11.md | 1,351 | 2026-08-15 |
| claude-code-bonfire/messages_as_event_substrate.md | 1,747 | 2026-08-15 |
| claude-code-bonfire/messaging_reactivity_agent_vocab_deepdive.md | 1,581 | 2026-08-15 |
| claude-code-bonfire/named_spirit_storage_shape_drift.md | 1,066 | 2026-08-15 |
| claude-code-bonfire/occasion_pg_representation_is_a_stub.md | 1,698 | 2026-08-29 |
| claude-code-bonfire/pg_collate_c_index_matching.md | 1,503 | 2026-08-29 |
| claude-code-bonfire/pg_test_suite_lock.md | 1,223 | 2026-08-15 |
| claude-code-bonfire/phase2_governance_closure_landed.md | 1,443 | 2026-08-15 |
| claude-code-bonfire/phase6_family_landing_recipe.md | 3,235 | 2026-08-15 |
| claude-code-bonfire/phase6_unit_deletion_recipe.md | 2,132 | 2026-08-15 |
| claude-code-bonfire/pin_ossification_audit.md | 1,332 | 2026-08-15 |
| claude-code-bonfire/plan39_review_verdict.md | 1,694 | 2026-08-15 |
| claude-code-bonfire/plan49_completion_review_2026-08-29.md | 3,744 | 2026-08-29 |
| claude-code-bonfire/plan53_execution_state_2026-09-03.md | 1,929 | 2026-09-03 |
| claude-code-bonfire/platform_design_converged.md | 1,549 | 2026-08-15 |
| claude-code-bonfire/port_gate_grant_design.md | 1,544 | 2026-08-15 |
| claude-code-bonfire/presence_typing_ephemeral_signals.md | 1,706 | 2026-08-15 |
| claude-code-bonfire/project_sdk_redesign_objective.md | 1,151 | 2026-08-15 |
| claude-code-bonfire/reusable_journal_writer.md | 1,488 | 2026-08-15 |
| claude-code-bonfire/review_2026-06-30_parallel_fixes.md | 1,253 | 2026-08-15 |
| claude-code-bonfire/review_arch_2026-06-30.md | 1,633 | 2026-08-15 |
| claude-code-bonfire/review_architecture_sdk_2026-06-05.md | 1,244 | 2026-08-15 |
| claude-code-bonfire/review_architecture_sdk_2026-06-07.md | 1,366 | 2026-08-15 |
| claude-code-bonfire/review_full_2026-06-10.md | 2,055 | 2026-08-15 |
| claude-code-bonfire/review_full_2026-06-13.md | 1,964 | 2026-08-15 |
| claude-code-bonfire/review_full_2026-07-23.md | 1,017 | 2026-08-15 |
| claude-code-bonfire/review_sdk_arch_2026-06-13.md | 1,011 | 2026-08-15 |
| claude-code-bonfire/review_sdk_design_2026-06-11.md | 1,753 | 2026-08-15 |
| claude-code-bonfire/review_unification_authz_gaps.md | 1,759 | 2026-08-15 |
| claude-code-bonfire/round2_sdk_review_fixes.md | 1,905 | 2026-08-15 |
| claude-code-bonfire/rpc_write_surface_unified.md | 1,741 | 2026-08-15 |
| claude-code-bonfire/sdk_elegance_core_resolution_2026-09.md | 2,600 | 2026-09-03 |
| claude-code-bonfire/sdk_separability_review_2026-06-16.md | 1,659 | 2026-08-15 |
| claude-code-bonfire/security_hardening_sweep_2026-06-24.md | 2,212 | 2026-08-15 |
| claude-code-bonfire/seed_scripts_unified_surface.md | 1,462 | 2026-08-15 |
| claude-code-bonfire/session_architecture.md | 2,141 | 2026-08-15 |
| claude-code-bonfire/session_face_kinds_persisted.md | 1,488 | 2026-08-15 |
| claude-code-bonfire/shared_repo_concurrent_sessions.md | 1,653 | 2026-08-15 |
| claude-code-bonfire/sigil_package.md | 1,020 | 2026-08-15 |
| claude-code-bonfire/single_writer_children_shipped.md | 1,600 | 2026-08-15 |
| claude-code-bonfire/spirit_lifecycle_events_arc.md | 1,281 | 2026-08-15 |
| claude-code-bonfire/structural_arc_design_2026-07-12.md | 1,590 | 2026-08-29 |
| claude-code-bonfire/structure_remediation_2026-06-11.md | 1,146 | 2026-08-15 |
| claude-code-bonfire/unification_finish_progress.md | 1,125 | 2026-08-15 |
| claude-code-bonfire/unified_mental_frame_direction.md | 1,227 | 2026-08-15 |
| claude-code-bonfire/unify_manifest_engine_2026-06-07.md | 1,294 | 2026-08-15 |
| claude-code-bonfire/unique_edge_backstop.md | 1,418 | 2026-08-29 |
| claude-code-bonfire/user_role.md | 728 | 2026-08-15 |
| claude-code-bonfire/verification_regime_2026-08-14.md | 2,224 | 2026-08-15 |
| claude-code-bonfire/vocabulary_sweep_executed.md | 996 | 2026-08-15 |
| claude-code-bonfire/worktree_typecheck_tests_setup.md | 1,450 | 2026-08-15 |
| claude-code-bonfire/worlds_review_2026-07-06.md | 1,208 | 2026-08-15 |
| claude-code-bonfire/ws_reconnect_herd_perf.md | 1,808 | 2026-08-15 |
| claude-code-bonfire/yi25_structural_unification_execution.md | 1,536 | 2026-08-15 |
| claude-code-bonfire/yi45_capability_plan_review.md | 1,570 | 2026-08-15 |
| claude-code-bonfire/yi45_implementation_progress.md | 1,414 | 2026-08-15 |
| claude-code-bonfire/yi_execution_built.md | 1,081 | 2026-08-15 |
| claude-code-bonfire/yi_kind_is_a_marker.md | 1,465 | 2026-08-15 |
| claude-code-bonfire/yi_message_renamed_to_stream.md | 1,204 | 2026-08-15 |
| claude-code-bonfire/yi_plan_declaration_sovereign.md | 1,164 | 2026-08-15 |
| claude-code-context-runtime-product/MEMORY.md | 380 | 2026-08-24 |
| claude-code-context-runtime-product/live-deployment-layout.md | 1,592 | 2026-08-24 |
| claude-code-context-runtime-product/principal-ticket-lifetime.md | 1,871 | 2026-08-24 |
| claude-code-context-runtime/MEMORY.md | 1,175 | 2026-08-24 |
| claude-code-context-runtime/adr-030-assurance-model.md | 2,458 | 2026-08-21 |
| claude-code-context-runtime/adr-030-program-progress.md | 16,544 | 2026-08-24 |
| claude-code-context-runtime/freeze-liftable-pre-launch.md | 1,971 | 2026-08-21 |
| claude-code-context-runtime/lineage-tab-client-bundle.md | 1,508 | 2026-08-24 |
| claude-code-context-runtime/r0-reset-progress.md | 3,528 | 2026-08-22 |
| claude-code-context-runtime/session-schema-artifacts-are-generated.md | 1,524 | 2026-08-22 |
| claude-code-context-runtime/worktree-node-modules-trap.md | 1,483 | 2026-08-21 |
| claude-code-deepseek-harness/MEMORY.md | 877 | 2026-08-31 |
| claude-code-deepseek-harness/deepseek-harness-working-style.md | 3,898 | 2026-08-30 |
| claude-code-deepseek-harness/manifold-product-split-state.md | 3,686 | 2026-08-31 |
| claude-code-deepseek-harness/node-version-for-deepseek-harness.md | 977 | 2026-08-26 |
| claude-code-deepseek-harness/phase-work-lives-uncommitted-in-main-checkout.md | 1,852 | 2026-08-30 |
| claude-code-deepseek-harness/staged-lint-unused-directive-false-positives.md | 1,310 | 2026-08-27 |
| claude-code-ember/MEMORY.md | 205 | 2026-07-28 |
| claude-code-ember/ember-agent-harness-project.md | 7,520 | 2026-07-30 |
| claude-code-exp/MEMORY.md | 148 | 2026-04-23 |
| claude-code-exp/feedback_essay_style.md | 1,996 | 2026-04-23 |
| claude-code-manifold/MEMORY.md | 690 | 2026-09-02 |
| claude-code-manifold/manifold-project-state.md | 24,962 | 2026-09-03 |
| claude-code-manifold/node-version.md | 601 | 2026-08-31 |
| claude-code-manifold/ren-working-style.md | 1,559 | 2026-09-02 |
| claude-code-manifold/worktree-dsh-submodule-init.md | 1,334 | 2026-08-31 |
| claude-code-runtime/MEMORY.md | 1,055 | 2026-08-21 |
| claude-code-runtime/e2e-runs-and-machine-sleep.md | 1,448 | 2026-08-14 |
| claude-code-runtime/gtc-composable-context-seed.md | 6,309 | 2026-08-14 |
| claude-code-runtime/history-core-program.md | 18,792 | 2026-08-21 |
| claude-code-runtime/package-boundaries-needs-dist.md | 1,451 | 2026-08-15 |
| claude-code-runtime/phase-gates-stay-narrow.md | 2,566 | 2026-08-14 |
| claude-code-runtime/ren-prefers-lean-process.md | 1,167 | 2026-08-07 |
| claude-code-server-runtime/MEMORY.md | 325 | 2026-08-26 |
| claude-code-server-runtime/ren-profile.md | 764 | 2026-08-15 |
| claude-code-server-runtime/server-runtime-project.md | 9,848 | 2026-08-31 |
| claude-code-speculative-future/MEMORY.md | 213 | 2026-06-03 |
| claude-code-speculative-future/project-speculative-future.md | 41,371 | 2026-06-06 |
| claude-code-zhishan/MEMORY.md | 1,214 | 2026-07-15 |
| claude-code-zhishan/sheng-record-recovery.md | 2,584 | 2026-07-15 |
| claude-code-zhishan/zhishan-defensive-revision-discipline.md | 2,390 | 2026-07-13 |
| claude-code-zhishan/zhishan-judgment-over-procedure.md | 1,212 | 2026-07-04 |
| claude-code-zhishan/zhishan-manifesto-turn.md | 2,287 | 2026-07-08 |
| claude-code-zhishan/zhishan-systems-voice-discipline.md | 1,306 | 2026-07-08 |

### 14-claude-code-prompts

| file | bytes | date |
|---|---:|---|
| Users-ren-Desktop-human-solutions-museum--claude-worktrees-cranky-mclean-c900b3.md | 175 | 2026-09-03 |
| Users-ren-repos-TencentDB-Agent-Memory.md | 134 | 2026-09-03 |
| Users-ren-repos-alignment.md | 121 | 2026-09-03 |
| Users-ren-repos-bonfire.md | 1,051,008 | 2026-09-03 |
| Users-ren-repos-context-runtime-product.md | 1,164 | 2023-04-17 |
| Users-ren-repos-context-runtime.md | 1,119,253 | 2026-09-03 |
| Users-ren-repos-deepseek-harness.md | 1,372,221 | 2026-09-03 |
| Users-ren-repos-ember.md | 457,004 | 2026-09-03 |
| Users-ren-repos-exp.md | 115 | 2026-09-03 |
| Users-ren-repos-manifold.md | 958,170 | 2026-09-03 |
| Users-ren-repos-openwiki.md | 686 | 2023-09-13 |
| Users-ren-repos-rts.md | 3,005 | 2024-04-28 |
| Users-ren-repos-runtime.md | 300,024 | 2026-09-03 |
| Users-ren-repos-speculative-future.md | 43,916 | 2026-09-03 |
| Users-ren-repos-zhishan.md | 533,348 | 2026-09-03 |
| Users-ren-repos.md | 119 | 2026-09-03 |
| Users-ren-server-runtime.md | 253,634 | 2026-09-03 |


## 2026-09-06 用户提供材料补充入库

以下三份材料由本任务用户提供，按原字节复制；创作日期未核定。导入日期仅记录本次归档，文本含对话整理与 AI 辅助成稿，不以文件署名推定逐句来源。[字节数、SHA256 与原路径](15-user-provided-2026-09-06/入库记录.json)。

| 材料 | 入库文件 | 来源 |
| --- | --- | --- |
| 至善_对话整理完整版.md | [副本](15-user-provided-2026-09-06/至善_对话整理完整版.md) | 用户提供的 Downloads 文件 |
| 智能向善，天下生生.md | [副本](15-user-provided-2026-09-06/智能向善，天下生生.md) | 用户提供的 Downloads 文件 |
| Meta-Attractor 理论：竞争性文明如何被自我强化的二阶动力学捕获.md | [副本](15-user-provided-2026-09-06/Meta-Attractor 理论：竞争性文明如何被自我强化的二阶动力学捕获.md) | 用户提供的 Downloads 文件 |

《生生不息论》与既存 [2026-07-14 归档版本](07-shengsheng-buxi/downloads-2026-07-08/2026-07-14-生生不息论.md) 逐字节一致，本次复用该副本。


Added 2026-10-02: [18-friend-conversations/2026-10-02](18-friend-conversations/2026-10-02/). Ren’s supplied 1 hour 52 minute 45.76 second English recording of a conversation with Alex, with a preserved local byte copy of the Voice Memos original, SHA-256 metadata, twelve unedited speaker-labelled transcription responses, independent passage checks, and Ren’s speaker/name/term clarifications. Original audio is excluded from Git because of its size and remains available locally. Speaker A is probably Alex and B probably Ren; the voice assignment remains provisional. The automatic transcript and assistant-authored idea inventory and full summary are in [drafts/2026-10-02-friend-conversation](../drafts/2026-10-02-friend-conversation/). This is a new source record, not an amendment to canonical theory; the summary does not establish the speakers’ factual claims.

Added 2026-10-02: [16-claude-code-directions/2026-10-02-why-and-meaning-request.md](16-claude-code-directions/2026-10-02-why-and-meaning-request.md). Ren's message naming the conversation with Alex (the recording above) as showing the "why and meaning" of his theories, and asking for it to be integrated into them, "especially for the high level stuff you got wrong before". Preserved verbatim with the transcribing session's completion report that he pasted into it (marked as not his words) and an assistant-authored provenance header and gloss. The integration it produced is recorded in `MAP.md` ("Why, and what it means"), `OPEN-QUESTIONS.md`, `GLOSSARY.md`, `TIMELINE.md` and the 2026-10-02 sections of ten theory documents. Single-message record from a Claude Code session, not a transcript export.

Added 2026-10-02: [16-claude-code-directions/2026-10-02-paper-v3-spine-direction.md](16-claude-code-directions/2026-10-02-paper-v3-spine-direction.md). Ren's direction for v3 of the IASEAI paper: the theory of why, not only control and correction; show, in a form intellectuals cannot simply refute, the invariant constraints of a system within a bigger system and why the current trajectory of winning digs our own graves. Verbatim, with an assistant-authored note and gloss.

Added 2026-10-03: [16-claude-code-directions/2026-10-03-v4-direction-cooperation.md](16-claude-code-directions/2026-10-03-v4-direction-cooperation.md). Ren's direction before v4 of the IASEAI paper: the focus is to prove that the world, and the US and China, must cooperate, by systems thinking, game theory, alignment and mathematics; settle the direction before building. Includes a full transcription of his WeChat messages on two points of no return (forced delegation of decisions to AI under competitive pressure; cognition outpaced by complexity and speed). Verbatim, with an assistant-authored note and gloss. Later sections, all verbatim, add his follow-ups of the same day: on AI 2040 and verification, trust and the system-level argument; his reply to the review of v4.1 (survival as the minimum requirement of every game; oppose the cancer-like logic; the order of exits); the request for v4.2; that AI 2040 is a pseudo-solution and the theory must answer those who keep the struggle mindset, accelerate and still want safety; and his reply to the five-perspective review of v4.3 (bounded human understanding against compounding complexity; the selected winner; the arms race itself drives the hazards to one).

Added 2026-10-03: [18-friend-conversations/2026-10-01-airplane](18-friend-conversations/2026-10-01-airplane/README.md). A conversation between Ren and a friend on a flight on 2026-10-01: four Chinese voice memos, about 15 minutes in all (story1, 生态文明气泡大气圈层, 生物控制论皮卡丘, 质能转换的生物装置). Ren supplied two texts made from them in ChatGPT: `飞机对话复原稿_含时间标记.txt`, a recovered transcript with time marks that has not been proofread by ear, and `飞机上的未来设想与创作讨论.md`, the ideas rearranged by how they connect. Both are byte copies, unedited. The four recordings are preserved locally and excluded from Git. [metadata.json](18-friend-conversations/2026-10-01-airplane/metadata.json) records bytes, SHA-256, durations and embedded times. Neither text separates the speakers, so nothing in them is attributed to Ren individually. Content: cosmic cancer as the film *The Game of Winning*; Earth consumed for compute, with survivors in glass domes; a borrowed simulation-and-frozen-humanity setting; biopunk living tools; an engineered companion and the argument over "生物奴隶编程"; a solar air bus. The integration is recorded in the README's "Where it went". This is a new source record, not an amendment to canonical theory.

Added 2026-10-04: [18-friend-conversations/2026-10-04-soi-si-lom-5-2](18-friend-conversations/2026-10-04-soi-si-lom-5-2/README.md). Ren's Voice Memos recording "Soi Si Lom 5 2", a location label for a lane off Silom Road in Bangkok, not a title: 51 min 26 s (3086.208 s) of mixed Chinese and English speech. A local byte copy of the original is preserved and excluded from Git. [metadata.json](18-friend-conversations/2026-10-04-soi-si-lom-5-2/metadata.json) records bytes, SHA-256, duration and the embedded time, 2026-10-03T17:09:38Z (00:09 on 10-04 in Bangkok), which marks the end of recording or an export, not the start. Two full automatic recognition passes are kept unedited (`chunk-*.json` from `gpt-4o-transcribe-diarize`; `checks/00–10.json` from `gpt-4o-transcribe`), with fourteen targeted rechecks. Diarization found one voice throughout, and Ren supplied the recording to be added to his theories, so the theory documents treat it as Ren speaking, provisionally and unconfirmed by ear; any listener is unknown. The Chinese translation (97 timestamped paragraphs), its notes on uncertain readings and a plain-text copy are in [drafts/2026-10-04-soi-si-lom-5-2](../drafts/2026-10-04-soi-si-lom-5-2/README.md). The translation renders the English speech into Chinese and lightly edits the Chinese, so it is not a verbatim transcript, and the theory documents quote it as such. Content: 心 and 理 as one dynamic, and 逍遥 as a cognitive model that fits reality; relation as what an agent asks first; 大同 and the reading of official narratives; 法家 and the 孙子 in struggle, and "我们确实需要赢"; power's selection of decision models and its rate; slack; the frame that calls correction violence; the cancer logic's two endgames; the training ground; alignment of the self, the collective and the machine; no safe way to win; trust before verification; asymmetric proposals; the logic of winning as the root problem. The integration is recorded in the README's "Where it went". This is a new source record, not an amendment to canonical theory.

Added 2026-10-04: [16-claude-code-directions/2026-10-04-soi-si-lom-integration-request.md](16-claude-code-directions/2026-10-04-soi-si-lom-integration-request.md). Ren's one-line request to add the recording above to his theories, with the translating session's completion report that he pasted (marked as not his words), an assistant-authored provenance header and a gloss. Single-message record from a Claude Code session, not a transcript export.

Added 2026-10-04: [16-claude-code-directions/2026-10-04-twenty-minute-talk-request.md](16-claude-code-directions/2026-10-04-twenty-minute-talk-request.md). Ren's one-line request for a talk of under twenty minutes. It is built on the recording above, with the 2026-10-02 conversation with Alex and the theories as background, and it is meant to move the alignment field. The record has an assistant-authored provenance header and gloss. The talk is in `drafts/2026-10-04-no-safe-way-to-win/` as `TALK.md` and `TALK.zh.md`. Single-message record from a Claude Code session, not a transcript export.

Added 2026-10-04: [15-codex-theory-conversations/2026-10-04-alignment-coordination-contribution-space.md](15-codex-theory-conversations/2026-10-04-alignment-coordination-contribution-space.md). AI-generated research assessment requested by Ren in a Codex conversation, synthesized from three research agents and a coordinating agent. Preserves his immediate request verbatim, maps potential contributions and close primary-source precedents, builds on the existing selector-influence and correction-rate results, derives illustrative authority-reserve and correction-deadline conditions, and proposes matched AI and human experiments. Records the failed P1 of the existing pilot and the unrun status of its revised design. The assessment is a research source, not a full conversation export, independent peer review, an empirical validation, or an established novelty claim; it has not been promoted into canonical theory.

Added 2026-10-04: [15-codex-theory-conversations/2026-10-04-selection-and-generative-conditions.md](15-codex-theory-conversations/2026-10-04-selection-and-generative-conditions.md). Foundation draft 0.1 requested by Ren to develop an integrated rigorous theory of what spreads and what makes continued becoming possible. AI-generated synthesis of mathematical, generative-capacity, and cross-domain research agents, with supporting records in `_process/research/2026-10-04-integrated-evolution/`. Contains an event-based population balance, exact selection–renewal identities, proposed capacity definitions, a conditional two-type maintained-support model with proof review and verified numerical illustrations, prior-art boundaries, and falsifiable research proposals. No new empirical benchmark or human experiment was run; universality, originality, normative completeness, and cross-domain validity remain unestablished. Linked as research development in the canonical 生生 theory without replacing its prior formulations.

Added 2026-10-05: [15-codex-theory-conversations/2026-10-04-universal-constraints-and-maintained-correction.md](15-codex-theory-conversations/2026-10-04-universal-constraints-and-maintained-correction.md). Research cycle begun 4 October and completed after midnight on 5 October, Asia/Bangkok; the filename retains the session start date. Ren explicitly set universal constraints on continued becoming as the north star and requested a durable record. AI-generated continuation with three research agents, independent proof review, two reproducible verification scripts, and a visually checked scientific figure. Records balance and selection invariances, finite-horizon safety under partial observation, correction deadlines, and a paid-renewal model with threshold and stability proofs. A living research hub, log, and claim register preserve assumptions, counterexamples, prior-art findings, and next decisions under `_process/research/2026-10-04-integrated-evolution/`. No new empirical experiment or deployment benchmark was run. Broad universality, originality, and cross-domain validity remain research targets.

Added 2026-10-05: [15-codex-theory-conversations/2026-10-05-selection-and-continuity-of-renewal.md](15-codex-theory-conversations/2026-10-05-selection-and-continuity-of-renewal.md). Continuation requested by Ren toward the universal-constraints north star. AI-generated research with three agents and coordinating-agent derivations, independent proof review, reproducible numerical checks, and two inspected scientific figures. Develops competing transmission channels for maintenance, a paid appropriation model, and delayed functional replacement with an occupancy-time invariant and funded handoff. Records the nonlinear boundary correction, model assumptions, close prior art, and the next question of selection over observation, allocation, and retirement rules. Working records remain in `_process/research/2026-10-04-integrated-evolution/`. These are complementary conditional models, not empirical validation or an established universal theory; no new deployment benchmark or empirical experiment was run.

Added 2026-10-05: [15-codex-theory-conversations/2026-10-05-formation-and-revision-of-frames.md](15-codex-theory-conversations/2026-10-05-formation-and-revision-of-frames.md). Ren's authorized continuation after the situated-correction reading intervention. AI-generated synthesis with three research agents, mathematical review, a focused primary-literature audit, twelve checked numerical illustrations, and an inspected scientific figure. Derives attracting exclusion under shared interests, a local proposal-origination threshold, protected-trial escape conditions, and explicit cost countercases. Preserves a failed initial prediction and the correction from an older Berk–Nash theorem statement to its 2019 erratum. The model contains two analyst-specified representations and fixed purposes; an experiment with generated candidates, false evidence, and separately varied admission and authority remains unrun. No empirical or deployment validation, complete account of purpose formation, universal ethical gradient, or mathematical novelty claim is established.

Added 2026-10-05: [15-codex-theory-conversations/2026-10-05-discovery-before-demonstrated-returns.md](15-codex-theory-conversations/2026-10-05-discovery-before-demonstrated-returns.md). Ren's requested next target, implemented as a synthetic candidate-generation and fresh-confirmation experiment with paid evidence and separate standing and deployment gates. AI-generated research with three agent audits, four mechanism tests, frozen code and protocol, 256 held-out independent seed clusters, fourteen paired arms, two hazard conditions, full records, and an inspected scientific figure. Distinguishes a necessary financing certificate from emergent closure and late evidence from physical irreversibility; retains development corrections and a final correction separating early observation payments from later analysis costs. The supplied grammar, fixed common purposes, calendar funding, and free retention after linkage leave endogenous renewal, archives, succession, and changing purposes open. No human institutional or AI deployment validation and no universal alignment solution is claimed.

Added 2026-10-05: [15-codex-theory-conversations/2026-10-05-recurrent-inquiry-and-inherited-evidence.md](15-codex-theory-conversations/2026-10-05-recurrent-inquiry-and-inherited-evidence.md). Ren's requested next target, developed as two explicitly separate exact decision modules: recurrent inquiry allocation with free retained belief, and one paid successor evidence channel with correct inference from public cues and silence. Three AI research agents supplied mathematical, implementation, and primary-literature audits. The record includes a strict maintenance-without-testing certificate, eight exploratory allocation comparisons against all 128 calendar schedules and their optimum at matched expected inquiry expenditure, five limiting controls, 117 handoff cases, five tests, independent LP dual checks, complete inputs and results, and an inspected scientific figure. Preserves the design correction against artificial ignorance and the post-review stationary perfect-diagnostic control. Established decision theory supplies the foundations; integrated paid memory, endogenous institutional-rule reproduction, purpose formation, and cross-domain empirical validity remain open.

Added 2026-10-05: [15-codex-theory-conversations/2026-10-05-inherited-evidence-under-model-revision.md](15-codex-theory-conversations/2026-10-05-inherited-evidence-under-model-revision.md). Ren's continuation emphasizing historical evidence versus inherited instructions. AI-generated research with three mathematical, implementation, and primary-literature audits. Derives exact model-relative sufficiency examples and finite Bayesian support limits, then joins paid record inspection, readiness, disclosure, and a current diagnostic in one finite successor decision. Preserves correct inference from public actions and silence, positive-cost signaling controls, fixed-format chronology, supplied model admission, all exploratory cases, five tests, independent brute-force checks, and an inspected figure. A final review correction distinguishes known-initial-state effects on endpoint-only information from the unchanged regime-order limitation of total count. The result does not deny historical recurrence, require maximal raw archives, explain unrestricted model admission, or establish an alignment solution.


Added 2026-10-05: [15-codex-theory-conversations/2026-10-05-questions-without-anomalies.md](15-codex-theory-conversations/2026-10-05-questions-without-anomalies.md). Ren's requested seventh continuation, with three AI agent audits, six passing tests, independent probability checks, complete finite results, preserved development inputs, and an inspected figure. Retention is chosen before one of two declared questions arrives. Four supplied worlds separate historical anomalies from future usefulness; an exact observation bound limits admission from indistinguishable records. Paid direct validation can reveal usefulness an anomaly-required route misses, while false proposals, all screening costs, deployment expenses, hard budgets, and no-inquiry controls remain explicit. Includes 130 base workflows, 286 declared priors, prospective question and price controls, and finite-workflow minimax regret. Records the correction from gross to ongoing net-benefit validation, restricted workflow optimality, and domain-adaptation prior art. Question generation, endogenous renewal of inquiry rights/resources, changing purposes, and empirical institutional or AI deployment validation remain open.


Added 2026-10-05: [15-codex-theory-conversations/2026-10-05-renewal-of-inquiry.md](15-codex-theory-conversations/2026-10-05-renewal-of-inquiry.md). Eighth continuation requested by Ren. Three AI agents audited conditional reserve mathematics, the information and cash-flow implementation, and six primary-source precedents. Participants' local observations generate proposals in a supplied grammar; independent validation and monitoring determine adoption and observable funding credit. The exact finite model includes positive social value and positive uncapped expected income alongside eventual inquiry shutdown, a large-reserve reliability counterweight, selective recognition, paid continuity and restart, agenda diversion, and no-benefit/near-null controls. Preserves all 480 grid cases, twelve full baseline traces, six constant-grant benchmarks, six passing tests, original and final inputs, independent rational/high-precision checks, and an inspected figure. A separate bounded-improvement credit theorem is not conflated with the iid-project experiment. Production and institutional rules remain supplied; empirical validity, evolving purposes, strategic capture, adaptive suspension, and productive regeneration remain open.


Added 2026-10-05: [15-codex-theory-conversations/2026-10-05-recoverable-inquiry.md](15-codex-theory-conversations/2026-10-05-recoverable-inquiry.md). Ninth continuation requested by Ren. Three AI agents reviewed information/finance mathematics, implementation, and primary precedents. An exact finite belief model couples productive stock, earned revenue, ordinary production evidence, noisy diagnosis, paid lagged rebuilding, direct repair, and a finite expected burden constraint. Preserves eighteen development cases, all 34 declared comparisons/controls, seven independent tests, primal–dual certificates, source snapshots, policy traces, and inspected figures. A selected case restores diagnostic capacity after dropping it; seventeen development cases buy no paid tests. Infeasible compulsory service and nonzero collapse remain explicit. Separate continuous bridge-finance, finite-information, and lifetime-burden results are not conflated with the DP. Fixed purposes, supplied repair and probabilities, free belief retention, empirical validity, infinite-horizon viability, and legitimate authority remain open. Next target: attainable correction under plural requirements, not another supplied universal score.


Added 2026-10-05: [15-codex-theory-conversations/2026-10-05-plural-requirements-and-attainable-correction.md](15-codex-theory-conversations/2026-10-05-plural-requirements-and-attainable-correction.md). Tenth continuation explicitly accepted by Ren. Three AI agents audited finite plural feasibility, implementation and primary precedents. Reuses unchanged productive dynamics with separately constrained collapse, burden and net expenditure, providing policy witnesses or independently checked separating certificates. Preserves all 252 grid queries, 22 detailed comparisons, 84 frontier points, nine passing tests, exploration, frozen inputs and inspected figure. Analytic cases distinguish pairwise from joint compatibility, permissions based on information before/after testing, and funding/authority complements. A differing-beliefs theorem and ex ante versus continuing-consent counterexample are clearly separate from the common-model central-controller implementation. Constituent identities, individual loss incidence, bargaining, legitimate authority, strategic participation and empirical validity remain open. Next target is continuation-compatible correction with explicit refusal and funded compensation.


Added 2026-10-05: [15-codex-theory-conversations/2026-10-05-continuing-participation-and-funded-correction.md](15-codex-theory-conversations/2026-10-05-continuing-participation-and-funded-correction.md). Eleventh continuation requested by Ren. Three AI agents reviewed personal loss incidence, full public-history participation, funding and primary literature. An unchanged physical model gains two half-owners, publicly revealed repair burden, collective veto and conditional compensation from shared funds. Preserves all 92 finite comparisons, nine independent tests, original development, frozen inputs, numerical checks, actual-veto replay, and an inspected scientific figure. Exact terminal payment intervals and a later cash obstruction distinguish distribution and liquidity from inadequate aggregate gains; no selected policy purchases diagnostics. Continuing participation and contract theory are established prior art. Rights, valuation, property and atomic payment enforcement remain supplied; no general equilibrium, empirical validation, purpose-formation theory or universal alignment solution is claimed. The next unrun target is a funded participant-controlled backup option that separates better continuation from a worse refusal alternative.

Added 2026-10-05: [15-codex-theory-conversations/2026-10-05-conscience-and-universal-morality.md](15-codex-theory-conversations/2026-10-05-conscience-and-universal-morality.md). Ren's proposal connecting evolution, conscience and universal morality, followed by his explicit request to incorporate it into the theoretical core. Preserves his words separately from the AI-assisted formulation and internal reviews. The canonical 生生 theory now states a public cross-subject normative principle, fallible conscience, distinct conditions for moral standing and responsibility, two testable feedback families, and a conditional interface to continuation mathematics. Five primary studies support limited biological and behavioral claims; no exactly-two-attractor law, derivation of unique morality from selection, or complete universal theory is established. Existing source snapshots remain unchanged.


## Completed Codex theory sessions preserved on 5 October 2026

[Session snapshot 20](20-codex-theory-sessions-2026-10-05/SNAPSHOT-MANIFEST.json) preserves 2,378 files from the root-of-wisdom, full-picture-conjecture, scientific-principles, recursive-self-modeling, structural-foundations, and sin workspaces. The w workspace was empty. Original paths, SHA-256 hashes, sizes, and dependency/cache exclusions are recorded. Checkpoint 003cd2a includes this snapshot and all then-current repository changes.

The two wisdom chats received further continuation requests. Their [completion supplement](20-codex-theory-sessions-2026-10-05/completion-supplement/MANIFEST.json), checkpoint 38f8022, preserves 20 new or changed files after both turns finished, without modifying the original snapshot. [Completion records](20-codex-theory-sessions-2026-10-05/completion-supplement/SESSION-COMPLETION.json) identify the source chats and final messages. Additional [session context](20-codex-theory-sessions-2026-10-05/synthesis-context/SESSION-CONTEXT.json) preserves selected user and assistant messages used by the integration, including the conditional acceleration derivation.

These are dated source snapshots and selected conversation records, not independent validations. Ren's user messages and AI-authored elaboration remain distinct. The [current unified foundation](../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/START-HERE.md) supplies the reading path, formal results, evidence boundaries, and research frontier.


Added 2026-10-05: [Direction of regeneration and the formation of concern](15-codex-theory-conversations/2026-10-05-direction-and-generalized-concern.md). Ren made the open universal direction hypothesis the next focus. The continuation distinguishes models of others from concern for them, proves a bypass counterexample and a costed selection threshold, and derives paid first formation within a supplied construction repertoire. Three AI research notes retain primary evidence, contrary cases, a comparative hypothesis, and finite mathematical checks. Universal direction and generalization of concern remain research hypotheses; earlier unified proofs and source snapshots are preserved.


Added 2026-10-05: [The formation and renewal of concern](15-codex-theory-conversations/2026-10-05-formation-and-renewal-of-concern.md). Ren asked for a complete theory of how another being comes to matter and how concern learns, widens, and sustains itself. The AI-authored continuation constructs learned valuation and recognition from zero under explicit shared-routing premises, proves protection, widening, memory and succession thresholds, and accounts for paid criticism and every-prefix funding. Identity gating, concealment, harmful intervention, and lost support expose failure boundaries. Three collaborating agents supplied mathematical, conceptual, and primary-evidence analysis, followed by internal review and independent exact checks. Completeness is relative to the declared mechanism; ethical scope, architectural origins and revision, empirical generality, and universal direction remain open. Earlier source snapshots are unchanged.


## First development of the unified theory

Added 5 October 2026: [source record 21](21-unified-theory-development-2026-10-05/README.md) preserves Ren's explicit request to pursue the roadmap and distinguishes it from AI-assisted elaboration. The [constructed-correction experiment](../experiments/constructed-correction/README.md) derives selected protection through a built rival alternative, strategic depletion of future operating cash, and an exact two-period reserve boundary. It retains the pre-enumeration protocol, all cases, code, independent audits, and inspected scientific figure. The canonical theory integrates this conditional mechanism and a positive ethical argument for standing beyond usefulness. No empirical validation, universal direction, or derivation of its physical control primitives is claimed.


Added 2026-10-05: [Revising the scope of concern](15-codex-theory-conversations/2026-10-05-revising-the-scope-of-concern.md). Ren authorized continued advancement after the concern theory. The AI-assisted continuation develops a traceable challenge to exclusions, finite reason-admission closure, learning deadlines, and the distinction between warranted relations, retained evidence, and operational access. A strategic graph model derives joint suppression thresholds and shows why individually resistant claims can fail behind one shared bottleneck. Paid reinforcement, authority capture, cash timing, retained knowledge, and defeated-certificate retraction remain explicit. Three agents supplied proofs, primary-source analysis, internal review, and independent exact reconstruction. This is a conditional extension using established graph mathematics, not empirical validation, universal moral convergence, or invention of arbitrary new ethical concepts.


## Repository reconciliation of recent research

Added 5 October 2026: [source record 22](22-research-reconciliation-2026-10-05/README.md) preserves missing supporting work, later wisdom studies, review and delivery history, and a dated snapshot of ongoing development. Its manifest maps the inspected external files to exact repository copies and records exclusions. The [current research index](../RESEARCH.md) is the common reading and working entry point. This consolidation repairs storage and navigation; it does not supply new scientific evidence or change the status of unfinished studies.


## Joint formation and renewal

Added 5 October 2026: [source record 23](23-joint-formation-2026-10-05/README.md) preserves Ren's request to solve the central joint-formation challenge. The [joint study](../experiments/joint-formation/README.md) and canonical theory now supply a selected paid reconstruction process beginning with zero current learned concern and apparatus, protecting a patient with no own productive leverage. Its final proof includes dated decision-maker incentives, off-path bounds, finite induction, an infinite discounted equilibrium, and a sufficient destructive-raid bound. Exact computation, independent reconstruction, reviews, and failure countermodels are preserved separately. This is a conditional resolution, not empirical prevalence or a universal ethical-direction theorem.

## Continuing goal of the unified foundation

Recorded 6 October 2026: [Approved path from the generative root to a connected foundation](15-codex-theory-conversations/2026-10-06-approved-derivation-path.md) preserves Ren's question and explicit acceptance of the proposed research path. The AI-authored summary records the five stages, first milestone and parallel integration method separately from Ren's words. The canonical grounding and repository guidance now adopt that direction; this update establishes no new theorem or empirical result.

Recorded 6 October 2026: [Unified generativity as the continuing repository goal](15-codex-theory-conversations/2026-10-06-unified-generativity-goal-and-continuity.md) preserves Ren's formulation of interacting differences, feedback, shared learning, contrasting regimes and 良知, followed by his directive to keep the repository on that goal through completion. The selected user messages are distinguished from AI-authored provenance and operational interpretation. The existing canonical grounding now specifies continuity and completion obligations across parallel studies; this is a clarification of research direction, not a new theorem or empirical validation.

## External evidence on evolving RNA networks

Added 5 October 2026: [source record24](24-rna-network-evidence-2026-10-05/README.md) preserves the main papers by Bansho et al.(2016) and Mizuuchi et al.(2022), plus the latter's supplementary information, with original bytes and hashes. The [AI-authored audit](../_process/research/2026-10-05-support-and-shared-generativity/completion/PHYSICAL-EVIDENCE-RNA-NETWORK.md) separates supplied support, evolving interactions, association-dependent dynamics, a derived moment identity and unrun validation proposals. No experiment was replicated or microscopic rate model identified; related laboratory trajectories are not counted as independent confirmations of the theory.


Added 5 October 2026: [source24 identification addition](24-rna-network-evidence-2026-10-05/identification-addition/README.md) preserves the publisher's original Mizuuchi2022 source-data workbook, author notebook and README pinned to commit defaabf8633d25fd809ac9ddfec7d65f44083207, and Dryad metadata. The [new audit](../_process/research/2026-10-05-support-and-shared-generativity/completion/RNA-IDENTIFICATION-CONTRACT.md) reconstructs all 15 host-donor effective matrix coefficients within printed rounding, derives a conditional joint replacement boundary, and records observation-dependent nonidentifiability. The workbook was read without modification; the notebook was inspected without execution and its referenced CSV is missing from the pinned tree. Effective coefficients, normalized simulation time and algebraic alternative rates are not independently identified elementary chemistry. The proposed joint assay remains unrun. Original source24 PDFs, manifest and prior review remain unchanged.
