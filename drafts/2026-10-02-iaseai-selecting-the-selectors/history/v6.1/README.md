# Changing the AI Trajectory: The Meta-Attractor of Winning and the Generative Alternative — V6.1

Theory V6.1, 3 October 2026. Drafted by Claude (Opus 5.5) from Ren's direction; not yet reviewed outside the drafting model family; not yet read by Ren.

## Files

| File | What it is |
|---|---|
| [THEORY.md](THEORY.md) | The core: the argument from mechanism to judgment, with a Chinese guide at the head. Parts I–IV follow the levels of claim: mechanism, diagnosis, responses, transition and judgment. Results are stated, not proved. |
| [SUPPLEMENT.md](SUPPLEMENT.md) | Full statements, proofs and numerics, chapter by chapter (S2 for Section 2, and so on); interfaces (S13), counterexamples (S14), the map of numerical checks (S15). |
| [DISCUSSION.md](DISCUSSION.md) | Lineage and literature (X1), substrates (X2), the alternatives in full (X8), the design in full (X10), the transition in full (X11). |
| [CLAIMS.md](CLAIMS.md) | Thesis, definitions fixed in advance, every result by stable key, the dependency chain, open interfaces, disposition of the v6.0 reviews. |
| [EVIDENCE.md](EVIDENCE.md) | Dated sources for each premise of the diagnosis, with contrary findings. |
| [TESTS.md](TESTS.md) | Cruxes, conditions registered in advance and what each would change, tests with rival predictions, indicators, research programme. |
| [LEDGER.md](LEDGER.md), [LEDGER-units.tsv](LEDGER-units.tsv) | Where every v6.0 result and paragraph now lives; content restated, corrected, withdrawn; restored and deleted items. |
| [CHANGELOG.md](CHANGELOG.md) | Decisions and changes. |
| `checks_v61.py`, `checks_v61.log` | Numerical checks by block, keyed to results. |
| `xref_v61.py` | Structure checks. |
| `src/` | Keyed sources and the build: `assemble_v61.py`, `refs_v61.py`, `preserve_v61.py`, `keymap.json`. |

## Reading paths

- **Thirty minutes:** the Chinese guide or Section 0; Section 1.2; the claim box at the head of each section; Sections 12.1 and 12.4.
- **Policy:** Sections 0–1; the claim boxes of Part I with 4.3, 4.5 and 5.2; Sections 6.6 to 12; the cruxes in TESTS.
- **Formal:** Section 1.4; Supplement S0; each section of Part I with its Supplement chapter; S14; `checks_v61.py`.
- **Alignment:** Section 6 and S6; 4.4; 5.3; Section 9 (R8); 11.3 (E1); cruxes C1, C3, C9; Test L.
- **Systems and design:** Sections 2.3, 4, 10 with Discussion X10; 11.4 with S11.
- **Evidence and international relations:** Section 7 with EVIDENCE; 8.3 with X8; 11.5 with X11; X1.
- **Readers of v6.0:** LEDGER first, then Section 1.2 and the sections that changed.

## Rebuilding

Edit the keyed sources in `src/core`, `src/supp`, `src/disc` and `src/reg`, never the assembled files. Results are declared as `{{!Proposition:key}}` and cited as `{{key}}` or `{{#key}}`; numbers are assigned in order of appearance. Then, from `v6.1/`:

```
python3 src/assemble_v61.py
python3 xref_v61.py
python3 checks_v61.py > checks_v61.log
```

After adding citations, run `python3 src/refs_v61.py` from `src/` and assemble again.