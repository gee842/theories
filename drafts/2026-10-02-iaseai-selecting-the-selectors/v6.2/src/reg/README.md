# Changing the AI Trajectory: The Meta-Attractor of Winning and the Generative Alternative — V6.2

Theory V6.2, 4 October 2026. Drafted by Claude from Ren's direction; every sentence is AI-drafted. One model outside the drafting family (Codex) reviewed V6.1, whose review round this version answers; V6.2 has not yet been reviewed outside the family, and Ren has not yet read it.

## Files

| File | What it is |
|---|---|
| [THEORY.md](THEORY.md) | The core: an English abstract and a Chinese guide, then the argument from mechanism to judgment. Parts I–IV follow the levels of claim: mechanism (§2–§6), diagnosis (§7), responses (§8–§10), transition and judgment (§11–§12). Results are stated with their conditions; proofs are in the Supplement. |
| [SUPPLEMENT.md](SUPPLEMENT.md) | Full statements, proofs and numerics, chapter by chapter (S2 for Section 2, and so on); S0 conventions, shared symbols, renames and maintained assumptions; S13 the interfaces between models; S14 counterexamples; S15 the map of numerical checks. |
| [DISCUSSION.md](DISCUSSION.md) | Lineage and literature, with the author's corpus by key and date (X1); substrates (X2); the alternatives in full, with every path's failure modes (X8); the design in full (X10); the transition in full (X11). |
| [CLAIMS.md](CLAIMS.md) | Thesis; definitions fixed in advance; every result by stable key with its tag and status; the dependency chain by threshold; open interfaces; the disposition of the V6.1 reviews; renderings of Ren's words awaiting his confirmation (§8); decisions for Ren (§9). |
| [EVIDENCE.md](EVIDENCE.md) | Dated sources for each premise of the diagnosis (EV1–EV18), with contrary findings, gaps and corrections. |
| [TESTS.md](TESTS.md) | Cruxes C0–C13 and N1–N4; the judgment set against every crux; conditions registered in advance; tests with rival predictions; indicators for activation and release; the research programme; what needs review outside the drafting family. |
| [LEDGER.md](LEDGER.md) | Where every V6.1 result and sentence now lives; what was restated, corrected, withdrawn or declined, and why; V6.1's losses and unrecorded changes; earlier versions. |
| [LEDGER-v62-sentences.tsv](LEDGER-v62-sentences.tsv) | Every sentence of V6.1's core with its containment in V6.2 and, below 0.4, its disposition. |
| [LEDGER-units.tsv](LEDGER-units.tsv) | Every paragraph of v6.0 with its V6.1 destination (kept from V6.1). |
| [CHANGELOG.md](CHANGELOG.md) | Ren's direction and decisions, what changed and why, deviations from the plan, what is not done. |
| [V6.2-PLAN.md](V6.2-PLAN.md) | The plan this version implements. |
| `checks_v62.py`, `checks_v62.log` | Numerical checks: 41 blocks, 202 assertions, each block labelled independent, identity or derived and keyed to the results it serves (map: SUPPLEMENT S15). |
| `xref_v62.py` | Structure checks: assembly, citations in both directions, must-stay items, the guide against §1.2, no state or firm named in the core. |
| `src/` | Keyed sources and the build (below). |
| `planning/` | Design memos (D1, D2, D4), the notes of every drafting, merge, elegance and build step, the snapshot before the elegance pass, and the workflow scripts. |

## Reading paths

- **Thirty minutes:** the abstract or the Chinese guide; Section 0; Sections 1.2 and 1.4; the claim box at the head of each section; Table 7.1; Section 12, with the cruxes of 12.3.
- **Policy:** Sections 0–1; the claim boxes of Part I, with 4.3 (how fast correction must grow), 4.5 (certificates, keystones and pauses), 5.2 (enforcement) and 5.5 (the scissors); Section 7, with Table 7.1 and 7.2 (what the premise of the race cannot justify); Sections 8–12; TESTS §1 (cruxes), §3 (the judgment against the cruxes) and §6 (indicators); DISCUSSION X10 and X11.
- **Formal:** Section 1.4 and *Symbols and labels*; Supplement S0; each section of Part I with its chapter of the Supplement (S2–S6), then S7–S11 for the results of Parts II–IV; S13 (interfaces), S14 (counterexamples), S15 (checks); `checks_v62.py` with its log; CLAIMS §4–§6; the results held for outside review (TESTS §8, Study 7, and §9).
- **Alignment:** Section 6 and S6, with the four classes of divergence and masked divergences (Remark 6.8), the alignment tax, weak and strong incarnation, and the inner and outer levels of 6.6; 4.3 (delegation erodes the corrector, Proposition 4.6) and 4.4 (masking, and the bound that must come from evidence the model's behaviour controls less directly); 5.3; 8.3(a), technical alignment and AI-assisted correction, with DISCUSSION X8 *Technical alignment and AI-assisted correction*; Table 9.1, rows R8a, R8b and R9; 11.3 (E1, narrow and broad); 12.1, tier 1 (alignment and control research; admission before consequential deployment); DISCUSSION X1 *The alignment literature*; EVIDENCE EV6; cruxes C1, C3a, C3b, C9a–C9d, C12 and N4; Test L.
- **Systems and design:** Sections 2.2 (the levers, channel by channel) and 2.3 (the reflexive closure), with S2; Section 4 with S4 (capacity off its selected level; the field model); Table 7.1 with S7 (the matrix of shared parameters; the four loops, formally); Section 10 with DISCUSSION X10; 11.4 with S11 (dwell, the ratchet); S13.
- **Evidence and international relations:** Section 7 with EVIDENCE; 3.4–3.5 (relative gains and the price of standing); 5.2 (enforcement where power is about to shift); 8.3 with X8; 11.5 with X11's precedents; DISCUSSION X1, *International relations* and *What is absorbed, and what is added*.
- **Readers of V6.1:** LEDGER first (Table L1 for numbers, §4 for what changed in content, §6 for the restored losses); then the V6.2 entry of the CHANGELOG; then the abstract, Section 1.2, Table 7.1 and the sections that changed; CLAIMS §7 for what became of each review finding.

## Rebuilding

Edit the keyed sources in `src/core`, `src/supp`, `src/disc` and `src/reg`, never the assembled files.
- Results are declared as `{{{{!Proposition:key}}}}` (or Definition, Theorem, Lemma, Corollary, Remark, Assumption, Table) and cited as `{{{{key}}}}`, which prints the kind and the number, or `{{{{#key}}}}`, which prints the number alone; never write a kind word before `{{{{key}}}}`. `{{{{>key}}}}` is a forward pointer in the core. Equations are declared as `{{{{!eq:key}}}}` and cited as `{{{{eq:key}}}}`. Supplement declarations are S-numbered. Write `{{{{{{{{` and `}}}}}}}}` for literal double braces.
- Numbers are assigned in order of appearance; keys never change.

From `v6.2/`:

```
python3 src/assemble_v62.py              # assemble; checks keys, forward use, doubled kinds, banned phrases; writes src/keymap.json
(cd src && python3 refs_v62.py)          # after adding or removing a citation: regenerate the reference lists
python3 src/assemble_v62.py              # assemble again with the new lists
python3 xref_v62.py                      # structure checks
python3 checks_v62.py > checks_v62.log   # about 300 s; "python3 checks_v62.py XX YY" runs named blocks; --full adds heavy grids; --legacy re-runs earlier suites
python3 src/sentcheck.py ../v6.1/THEORY.md THEORY.md SUPPLEMENT.md DISCUSSION.md --min 0.4 --all
```

The last command is the sentence-level preservation check behind LEDGER §3 and [LEDGER-v62-sentences.tsv](LEDGER-v62-sentences.tsv); without `--all` it prints only the sentences below the threshold. `src/persub.py` prints words per subsection. `src/preserve_v62.py` is the paragraph check of v6.0 against V6.1 behind `LEDGER-units.tsv`.
