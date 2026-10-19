# Common brief for the twentieth review (whole-theory review: completion, unification, coherence, elegance, redundancy)

Repository: /Users/ren/theories (git, branch main at 121ff8042). It holds "the Theory of Becoming": one relational unfolding as the starting point (no separate entities first), a pure Lean core (package `Becoming`, empty axiom reports, imports only Lean's Init) plus prose chapters, result records and studies. Ren's direction for this review: "our direction is an elegant, unified theory". The target is one unified, complete, enclosed, zero-axiom theory; ethics is conditional on the continuation condition (§6.15), asserted nowhere.

Key paths (repository-relative):
- AGENTS.md (working rules; read it first, it is short and defines the method: one relational unfolding first, nondual method, names structural, Ren's words are provenance not authority)
- theories/becoming/chapters/THE-THEORY-OF-BECOMING.md (canonical chapter, ~1,950 lines; outline: In one sentence; stated in full; §0 premise card; §1 Becoming; §2 organization/renewal/evolution; §3 knowing; §4 collective; §5 evaluation; §6.1–6.15 significance; "stated whole"; §7 alignment; §8 open programme; §9 formal spine; §10 glossary; §11 earlier chapters)
- theories/becoming/chapters/NONDUAL-METHOD.md, theories/becoming/OPENING.md (Ren's voice; do not propose rewriting his voice, only flag)
- core Lean: experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/*.lean (297 modules, ~166k lines), its README.md (layers), Becoming.lean (import list), check_becoming.py
- result records: theories/becoming/results/records/*.md|json (≈279 records), theories/becoming/results/*.md (generated pages)
- studies: _process/research/2026-10-05-generative-foundation-review/root-foundation/ (the study, DELEGATED-CHOICES.md = decision register D1–D57, REVIEWS.md, BECOMING-NINETEENTH-REVIEW.md = the last review)
- theorem connectivity measure (theorem-level dependency classes on the current head 831fcaf73): _process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY.json (keys: base, families_reach_each_other, classes, apart_roots_by_category, apart_by_module, components, theorems → class per theorem, statements_on_both_by_module, ...) and THEOREM-CONNECTIVITY.md (method). Notable: two base families (Process: Generative.Process/Trace, Becoming.Frame/Run; World: Becoming.World/Flow/Web) and "families_reach_each_other" is all False; 66 components; 495 theorems "apart" of 11,647.
- work board: _process/BECOMING-WORKBOARD.md; layout rules: _process/REPOSITORY-LAYOUT.md; GOALS.md; RESULTS.md; OPEN-QUESTIONS.md

The nineteenth review (BECOMING-NINETEENTH-REVIEW.md) already checked prose against Lean for many sections, and session R21 is applying its fix list right now. Do NOT repeat those findings (read its Summary and fix list to know them). This review is at a different altitude: the theory as a whole. Sentence-level accuracy errors count only when they matter for the whole.

Rules:
- READ-ONLY. Do not edit, create, move or delete any file in /Users/ren/theories, do not commit, do not run `git` commands that write (checkout, stash, worktree add, etc.), do not run lake/lean builds or the checkers (CPU is shared with landing sessions). You may run read-only scripts (python, grep, git log/show/grep) and write scratch files ONLY under your output directory.
- Use the existing data (THEOREM-CONNECTIVITY.json, record JSON, lean-index data in theories/becoming/results/data/) before writing new scripts. Parsing Lean source with regex for declaration names, namespaces and statements is fine.
- Be concrete: every finding cites path:line (or module/declaration names) and the evidence. Quantify where you can (counts, sizes).
- Separate what you verified from what you infer. Mark judgments of elegance as judgments and argue them.
- The theory's own method is the yardstick: one relational unfolding first; one notion, one name; structural (not dualist/social/financial) names; a weaker model omitting a relation is not a refutation; only the latest, most informative version stays live; a wrapper, recheck, rename or repeated acceptance is not a result.
- For each problem, propose the unified/elegant form concretely (what merges into what, what becomes a corollary/instance of what, what moves to history), its cost (docs only / Lean rename / Lean proof work), and what it would gain. Also say what is already good and should be kept (briefly).

Output: write your full report as Markdown to the file named in your task (the lens files beside this brief), structured as:
  1. Summary (≤ 12 lines: the 3–6 most important points)
  2. Findings table(s): id (your prefix + number), severity (major / moderate / minor), where, finding, evidence, proposal, cost
  3. What is sound and should be kept
  4. What you could not check
Then reply with a ≤ 300-word summary plus the path of the report. Severity "major" means it affects whether the theory is one elegant, unified whole.
