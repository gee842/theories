# Start here

A guide for visitors: what this repository is, where to begin, how its history is kept and how to check the proofs yourself. It extends the map of 17 October 2026; the September corpus map, with the reading of the fifteen folders as strata of one argument and the 2 October "why and meaning" section, is kept verbatim in [history](_process/history/2026-09-consolidation/MAP.md).

## What this is

The working repository of the Theory of Becoming: an account of how anything comes to be, lasts, changes and passes away within one relational unfolding, and of what follows for ethics and for AI alignment. It is developed together by Ren and AI. Claude and Codex sessions, often several at once, draft, prove, review and keep the records; Ren sets the direction, decides the readings of his own terms and writes in his own voice.

Three kinds of statement are kept apart throughout:

- **Laws proved in Lean.** Each holds under the conditions it names, and no axiom is assumed: the core's declarations have empty axiom reports.
- **Readings and judgments.** What the laws mean for people, ethics and AI, labelled as readings, and as AI readings where the AI made them.
- **Open questions.** Including whether the one ethical step the theory states as a condition, that the continuation of anything has significance, can itself be derived.

The footnotes of the README's opening say, sentence by sentence, which kind each claim is. Ren's words are kept verbatim with their source in [`sources/`](sources/README.md) and quoted as provenance, not as the warrant for a claim.

The work is not licensed: [knowledge is a common good](COMMONS.md).

## Where to start

1. [README](README.md): Ren's opening, then the established results.
2. [The Theory of Becoming](theories/becoming/chapters/THE-THEORY-OF-BECOMING.md): the canonical chapter. It is long; begin with [the premise card](theories/becoming/chapters/THE-THEORY-OF-BECOMING.md#0-前提卡--premise-card) and sections 1–6, the theory with no axiom, then the conditional §6.15.
3. [The nondual method](theories/becoming/chapters/NONDUAL-METHOD.md): how the theory is worked.
4. [Results](RESULTS.md): every registered result, each bound to its Lean proof or evidence, and [open questions](OPEN-QUESTIONS.md).
5. [Goals](GOALS.md) and the [directive register](_process/RESEARCH-DIRECTIVES.md): scope and Ren's authorizations.

## How it got here

The ideas began in Ren's writing from 2021 on: the fifteen earlier theory folders below, with their originals in `sources/`. The repository's first commit is from 6 September 2026; the formal theory was built in October 2026, in about 1,400 commits. The history is part of the work, and nothing is deleted:

- **Commits.** `git log` shows each step. Where an instruction of Ren's governed a step, the commit message quotes it.
- **`history/` folders.** Only the latest version of a document stays live. What it replaces moves byte for byte to a sibling `history/` folder, recorded in a manifest under [`_process/architecture/`](_process/architecture/), so earlier versions stay readable and linked.
- **Studies and records.** [`_process/research/`](_process/research/README.md) records each step of the work, failed candidates and counterexamples included; each result's record in `theories/becoming/results/records/` names its premises, evidence and boundary.
- **The work board.** [`_process/BECOMING-WORKBOARD.md`](_process/BECOMING-WORKBOARD.md) shows what each session has claimed and the order in which work lands.

Personal and third-party material (private chats, AI memories and friends' conversations) is not tracked from 19 October 2026 and stays on Ren's machine.

## Check the proofs yourself

The Lean package `Becoming` is in [`experiments/integrated-correction/general-framework/generative-basis/lean/becoming/`](experiments/integrated-correction/general-framework/generative-basis/lean/becoming/README.md). Its core imports nothing outside itself, and every declaration of the core and its bridge has an empty axiom report: no `propext`, `Quot.sound` or `Classical.choice`. The core check needs Lean and Python 3 (standard library only), not Mathlib.

1. Install [elan](https://github.com/leanprover/elan), then the toolchain: `elan toolchain install leanprover/lean4:v4.29.1`.
2. From the repository root, with no cache and the receipt written outside the repository:

   ```bash
   BECOMING_FRESH=1 BECOMING_OUT=/tmp/becoming-run python3 -B experiments/integrated-correction/general-framework/generative-basis/lean/becoming/check_becoming.py
   ```

3. `"status": "passed"` on the last line means that, on your machine, every module compiled, the core's purity held and every audited declaration's axiom report was as recorded.

A fresh run compiles more than a thousand Lean steps and takes a while; `BECOMING_JOBS` sets how many run at once. Without `BECOMING_OUT` the checker writes its receipt into the repository. [Verify it yourself](experiments/integrated-correction/general-framework/generative-basis/lean/becoming/README.md#自行验证--verify-it-yourself) gives the details, and what a passing run does not show (whether the premises hold, whether the readings fit, whether the representation fits the world).

## Top-level layout

| Path | What it holds |
|---|---|
| `theories/becoming/` | The current theory: chapter, kept chapters, records (`results/records/`), generated results pages, `history/` |
| `theories/<folder>/` | The earlier theory folders (below); each now reads as a stratum the Theory of Becoming gathers |
| `experiments/` | Executable research; the Lean package Becoming is under `experiments/integrated-correction/general-framework/generative-basis/lean/becoming/` |
| `_process/` | Studies (`research/`), the work board, directives, workflow, architecture receipts, `history/` |
| `sources/` | Imported originals and Ren's directive records, byte-preserved |
| `drafts/` | Papers and long drafts by date |
| `worldbuilding/` | The constructive half: worlds, atlas, causal engine |
| `tools/research/` | Rendering, checking, moves, evidence store |
| `tools/publishing/` | PDF builders for the exports in `output/` |
| `output/` | Exported PDFs and images |

[REPOSITORY-LAYOUT](_process/REPOSITORY-LAYOUT.md) gives the rules for where new material goes.

## The earlier theory folders

| Folder | In one line |
|---|---|
| [alignment-selection-on-cognition](theories/alignment-selection-on-cognition/README.md) | Selection on axes where winning buys capacity to win remakes the minds it scores |
| [architecture-for-a-living-earth](theories/architecture-for-a-living-earth/README.md) | Working exploration of building and settlement for a living Earth (opened 2026-09-13) |
| [context-as-existence-runtimes](theories/context-as-existence-runtimes/README.md) | "llm is operator, context is existence": the context runtimes and ember |
| [drives-narrative-attractors-and-mind](theories/drives-narrative-attractors-and-mind/README.md) | A mind is what an environment makes of ancient drive systems |
| [evolving-community-swarms](theories/evolving-community-swarms/README.md) | Exploratory design for communities that evolve (opened 2026-09-05) |
| [human-solutions-museum](theories/human-solutions-museum/README.md) | Civilization as an accumulated stock of methods that turn problems into mechanisms |
| [jian-and-wenyan-as-formal-language](theories/jian-and-wenyan-as-formal-language/README.md) | 简 and 文言 as a formal language for theory |
| [keep-the-possibility-space-open](theories/keep-the-possibility-space-open/README.md) | 保持可能性空间打开: that the generating go on |
| [memories-and-working-style](theories/memories-and-working-style/README.md) | The person making the claims, and the salvage yard |
| [meta-attractor](theories/meta-attractor/README.md) | The meta-attractor of winning and common organization |
| [relational-self-and-datong](theories/relational-self-and-datong/README.md) | The self as what a knot of relations is doing; 大同 |
| [selfishness-spiral-and-narrative-value-frames](theories/selfishness-spiral-and-narrative-value-frames/README.md) | Actors act from narrative-value frames, and the spiral they select |
| [spirit-space-token-and-yi-substrate](theories/spirit-space-token-and-yi-substrate/README.md) | Spirits, tokens and spaces; the Yi substrate |
| [the-fork-and-cooperative-infrastructure](theories/the-fork-and-cooperative-infrastructure/README.md) | Cooperative infrastructure (the two-outcome "fork" framing was later rejected by Ren) |
| [wamotopia-and-the-wamo-protocol](theories/wamotopia-and-the-wamo-protocol/README.md) | Technology amplifies the operating logic it runs under; the Wamo Protocol |
| [zhishan-intelligence-must-be-good](theories/zhishan-intelligence-must-be-good/README.md) | 智善: competition that selects survivors hands winners the rule |

The [theory map](theories/becoming/results/THEORY-MAP.md) gives the longer branch-by-branch reading of these folders (a dated reading catalogue).
