# Working in the theory repository

Rewritten 17 October 2026 with Ren's approval ([previous text](_process/history/2026-10-17-instructions/AGENTS.md)); revised the same day for Ren's directive that his words are provenance ([before](_process/history/2026-10-17-instructions/AGENTS-before-ren-words-directive.md)).

## Start here

Read [README](README.md) → [the canonical chapter](theories/becoming/chapters/THE-THEORY-OF-BECOMING.md) → [the nondual method](theories/becoming/chapters/NONDUAL-METHOD.md) → [the records](RESULTS.md). [GOALS](GOALS.md) gives scope and authorization; [the work board](_process/BECOMING-WORKBOARD.md) holds claims. Ren's applicable instructions govern scope; another session's objective is not automatically yours. The [directive register](_process/RESEARCH-DIRECTIVES.md) curates retained authorizations from `sources/15-*` and `sources/16-*`; it is incomplete, so read the source record when an authorization matters.

## Begin with one relational unfolding

Ren: “我们首先考虑一元，关系的本体” ([source](sources/15-codex-theory-conversations/2026-10-08-monist-relational-ontology-first.md)). The primary ontology and starting point are one and relational: first how relations in the one unfolding form, persist and change, then how actor, patient, knowing, evaluation, capacity and responsibility differentiate within it. Each analytic distinction (subject/object, action/condition, fact/value) states its relational basis, scope and omissions; no name or formal variable smuggles in an independent ontology. Reconstruct a framing that presupposes separate entities first; a closing remark does not fix it.

Read both before foundational analysis, formalization or criticism. Preserve differentiated relationships, real losses and genuine counterexamples. A supplied local law is not thereby external to reality. A relationship a representation omits is not an explanatory failure: freely toggled predicates in a weaker model do not refute the full account. Nonduality is a method requirement, not a proof of the ontology or of ethical necessity.

Joint activity starts from actual relations, not opposed interests, bargaining, who wins more or a fixed common utility: study how the whole relation's change supports, enriches or damages 生生, not a distribution among independent value owners. The [common-problem reminder](sources/15-codex-theory-conversations/2026-10-08-collective-destructive-attractors.md#common-problem-solving-and-awareness) keeps real conflict and difference.

## Scope and current status

**First priority: the Theory of Becoming** ([Ren](sources/15-codex-theory-conversations/2026-10-08-theory-of-becoming-priority.md), [scope](GOALS.md#theory-of-becoming)): the whole unfolding, generation, maintenance, transformation, degeneration and disappearance, not assumed good; life, evolution and evaluation unfold through the relations it forms. Zero premises first: the strongest claim without axiom ([Ren](sources/15-codex-theory-conversations/2026-10-10-zero-axiom-part-and-names.md)), toward one unified, complete, enclosed, zero-axiom theory ([Ren](sources/15-codex-theory-conversations/2026-10-11-one-unified-theory-together.md)). Do not shrink "zero axiom" to "no ethical axiom", nor take a law admitting every outcome as explaining actual regularities. A local result does not complete a stronger universal or uniqueness claim.

**The theory asserts no ethical axiom.** The continuation condition (`Unrestricted`: for anything, its continuation into the future has significance) is the condition of [§6.15](theories/becoming/chapters/THE-THEORY-OF-BECOMING.md#615-若任何东西的延续都有意义--if-the-continuation-of-anything-has-significance); living significance and the other ethical results are theorems under it, and its warrant and necessity are open. Completed conditional results, including the conditional alignment route, keep their scope and are not reopened by demanding an axiom-free start. State conditions, comparison or responsibility commitments and corollaries openly; hide no weight or obligation in a definition. 生生 names life in the whole and its continuing generation ([source](sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md)); generation and degeneration do not overlap, so "generative" never means any new organization. Retired labels (G0, Part I/II, the one axiom) are explained once, in the chapter's glossary; live text uses the current terms.

Normative warrant, recognition, motivation, compliance and implemented preservation stay distinct; direction, continuing capacity, per-step monotonic growth and scalar maximization are different claims. Connect work to the inference it advances, state supplied premises and what would change the account, and build on completed mechanisms rather than historical "next step" passages. Weigh argument, counter-review and source assessment before choosing the next connection.

**Ren's words are provenance, not authority** ([Ren, 17 October](sources/15-codex-theory-conversations/2026-10-17-ren-words-not-authority.md)): “My words should not hinder the most significant direction, and we are pushing the frontier, not my frontier.” Keep Ren's words verbatim in `sources/` and wherever quoted, with their source; never present them as the warrant for a claim. Live text follows the strongest direction the work supports and revises or drops directives that the work has outgrown; where Ren's words seem unreasonable, say so and keep a note ([Ren](sources/15-codex-theory-conversations/2026-10-15-situational-and-the-whole-core.md)).

## Proof and naming

- New formal results go on [the Becoming spine](theories/becoming/chapters/THE-THEORY-OF-BECOMING.md#9-形式脊柱--the-formal-spine); extend it rather than build another model. Earlier modules keep their scope and connect by instance or equivalence theorems.
- [Pure core](sources/15-codex-theory-conversations/2026-10-09-pure-core.md): it imports nothing outside itself, every source declaration has an empty axiom report, and it compiles from Lean's prelude (`check_becoming.py` enforces this). The periphery may use any tool.
- Every new proof claim needs Lean and an actual check, with exact hypotheses, correspondence and dependency audits; metadata, hand arguments and finite numerics do not replace it. Claims say exactly what the Lean proves. Historical results keep their scope; no retrospective audit by default.
- Keep premises, scoped proofs, empirical support, philosophical warrant and conjecture distinct; encoding a desired verdict does not justify its premises.
- Names are structural and exact: formal, scientific and systems words, not dualist, limited-scope, social or financial ones ([Ren](sources/15-codex-theory-conversations/2026-10-10-zero-axiom-part-and-names.md)). A module joined to the spine, its instance module and its record take the core's vocabulary; the original file keeps path and bytes (board rule 8). A name is adopted only where the statement means exactly that.

## Coordination

- Claim on the board before new Lean or a new result. Do not reprove another session's item; give overlapping verified work to its owner. One integrator decides order, shared definitions and merges; build on its definitions and land through the queue.
- Unified head first ([Ren](sources/15-codex-theory-conversations/2026-10-11-unified-head-and-incremental-checks.md)): land or hand over verified work before new Lean. Checkers reuse passed steps; `BECOMING_FRESH=1` only when needed.
- Inspect `git status` first. Commit only owned paths, always `git commit -m … -- <paths>`, unless Ren asks for a whole-repository checkpoint. Never commit in the shared checkout mid-merge. Never `git prune`, `gc --prune`, `git clean` or delete data.
- Re-read a shared record or page before editing; keep distinct claims in separate records. Never move an active workspace or overwrite another session's study.

## Records and generated pages

Follow [RESULT-WORKFLOW](_process/RESULT-WORKFLOW.md): `make research-find QUERY=…` first; in the existing study state reused IDs, delta, premises, evidence, boundary and output→input connection. A wrapper, recheck, rename or repeated acceptance is not another result. Records govern migrated summaries only; contradictory evidence outranks a label. Corrections keep completed results, failed candidates and counterexamples.

Generated pages (README, RESULTS, GOALS, RESEARCH, ROADMAP, OPEN-QUESTIONS, DEPENDENCIES, indexes) are never hand-edited; reconcile and preserve prose others added before regenerating. Run `make research-render`, `research-check`, `research-links`, and `research-test` after infrastructure changes. Never refresh a source hash to silence a failure. Rerun scientific checks only when substantive change, dependencies or open concerns call for it.

**Ren's own voice.** The body of [OPENING](theories/becoming/OPENING.md) is written in Ren's first person and the [generativity chain](theories/becoming/results/GENERATIVITY-CHAIN.md) is his curated argument: propose changes to them rather than rewriting his voice (the chain changes through the maintenance record it links; its historical evidence is never silently refreshed). Everything AI-written around them, including OPENING's footnotes, goal records and this file, follows the current theory.

## Layout, history and language

[REPOSITORY-LAYOUT](_process/REPOSITORY-LAYOUT.md) says where things go: arguments in `theories/`, studies in `_process/research/`, executable research in `experiments/`, originals in `sources/`, tools in `tools/research/`. Reuse the relevant study; no new dated workspace for the same work.

- **Only the latest, most informative version stays live** ([Ren, 17 October](sources/15-codex-theory-conversations/2026-10-17-restructure-go-and-language-separation.md)). Superseded material moves to a sibling `history/` with `research.py move` (`--plan` first), which writes the manifest; never keep copies beside live files. Verify links and preservation hashes after a move. Preserve original bytes and provenance; label reading editions and record their link changes. Frozen copies and repeated reviews are evidence, not results. Import no dependency installs, caches or redundant exports.
- **Language** ([Ren, 17 October](sources/15-codex-theory-conversations/2026-10-17-restructure-go-and-language-separation.md)): each live document is in one language, or English plus a Chinese edition `NAME.zh.md`; new documents do not interleave languages; full translation is not required. Ren's quoted words stay in their original language; record JSON may carry one or both. Always distinguish Ren's words from AI elaboration.
- Repository-relative links in documents, absolute paths in messages. Save unique scratch work into the repository before delivery; exports are snapshots, not editing places.
