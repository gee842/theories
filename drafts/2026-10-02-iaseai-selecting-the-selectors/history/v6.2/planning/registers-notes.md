# V6.2 registers: TESTS and CLAIMS

4 October 2026. `src/reg/TESTS.md` and `src/reg/CLAIMS.md` were rewritten for V6.2. No other file in `src/` was touched.

## Build

- Drafted in scratch copies (`/private/tmp/claude-501/v62reg-tc`, then `/private/tmp/claude-501/v62reg-final`).
- The front matter (`00_head`, `10_s01`, `d0_symbols`, `S0`) was installed in `src/` at 14:18, while this work was under way. Its arrival is recorded in `planning/front-notes.md`.
  - The final pass re-copied `src/` with that front matter in place.
  - It re-synced CLAIMS §1 to the installed abstract, and the D list to front-notes §4.
- Final scratch run:
  - `assemble_v62.py`: no problems; 93 core and 35 supplement declarations.
  - `refs_v62.py`, then `assemble_v62.py` again.
  - `xref_v62.py`: **ALL CHECKS PASS**.
- Before installation, only these two files differed from the live `src/`.
- Sizes: TESTS about 10,100 words (source); CLAIMS about 12,700 words.
- **Inventory coverage, checked by script:**
  - every one of the 112 result keys in `keymap.json` appears exactly once in CLAIMS §4;
  - every V6.1 number in its V6.1 column matches `../v6.1/src/keymap.json`.
- **Information from xref, not a failure:**
  - TESTS cites Khan et al. 2024, Kenton et al. 2024 and Zhu 2026, which no document's reference list carries.
  - Khan and Kenton are in `refs_v62.py`'s data; Zhu is EV2's source.
  - V6.1 had the same.

## TESTS: what is new, and the choices made

1. **§1 Cruxes C0–C13.**
   - Each crux's definition and "what a measurement would change" are those of §12.3.
   - C9b–d and C12 had no row in V6.1. Each now has present evidence and a next measurement.
   - The C3a and C9 evidence follows the V6.1 alignment review and X1. Every citation resolves to a document's reference list, except Khan and Kenton.
2. **§2 Normative cruxes.**
   - N1–N4 are kept as separate rows; §12.3 groups N1–N3 in one row.
   - The V6.1 effects are kept.
   - N2 now also says that narrow E1's equilibrium presupposes actors who price in the lock.
3. **§3.1 The robustness matrix.**
   - Rows are the cruxes C0–C13, with C9a–d in one row. Columns are tier 1(a)'s five items.
   - Each cell gives its kind, using §12.1's four kinds (I, L, E, P), with a phrase on why the item stands on that crux in either direction.
   - A "read by column" paragraph covers how the normative cruxes bear: N2 on item 5; N1 on none.
4. **§3.2 Tier 1(b).**
   - Items 6–8 are listed with the crux that withdraws each, what is withdrawn, and what stays.
   - "Favourable" is defined once as "favourable to withdrawal". This settles elegance-notes U12 #3: for item 8 it is the reading unfavourable to the item's hope.
5. **§3.3 Registered conditions.**
   - V6.1's rows are kept and extended: C0, C3b in both directions, C4, C9a in both directions, C10–C13, and C1 with C2.
   - "Stage 1 transparency" became "the shared account of hazards of Track 1" (U11).
6. **§4 Redirect.**
   - V6.1's three outcomes are kept.
   - The persistence-by-profile prediction of §8 is added.
   - So are §7.4's refutations.
7. **§5 Tests.**
   - **Γ**: re-signed. Its observable is the ratio $1+\theta$, rising with provision relative to the stakes and with diffusion (0.58 → 0.81, [num: SP]). The ψ confound and the second identification are added.
   - **G**: discriminates at intermediate $p_d$. The hump at $D>C$ is given with S5's numbers [num: JX].
   - **L**: redesigned to the alignment review's I7 table:
     - third-party, fixed-protocol evaluations, not release notes;
     - divergences coded by cost incidence, with detectability held fixed;
     - difference in differences;
     - the conditional prediction on latent reasoning.
   - **M**: relabelled a remedy test, per Codex.
     - Under present institutions, a favourable outcome is C2 favourable. This keeps the core's use of "Test M" for C2 in §12.1 and §12.3.
     - Under item 6's mandates, the same outcome is the remedy working.
     - The mechanism goes to Test B.
     - The contrary is the remedy failing its stress test (C4).
   - **B**:
     - entry barriers without appropriability are now the discriminating contrary, on positions toward correction keyed to no one that burdens rivals more;
     - the barrier direction of capture is folded into the theory's own prediction, (ii);
     - the spending exponent and the moment are those of S4/S13.
   - **D**: the hysteresis prediction is restored, as fidelity minor 3(b) asked, with Pierson and ordinary reversal as contraries.
   - **I**: adds C13 (dependence on the governed) and succession rules.
   - **H**: absent. A sentence says why (v6.0's T-H became a tier-2 indicator). The symbols table already reads "Tests A–G, I–M and Γ".
8. **§6 Indicators.**
   - §6.1: the tier-2 trigger table, with estimators for each quantity:
     - who estimates it: certified correctors, with misses measured for correlation;
     - from what channels: those that observe actions directly;
     - $T_{\rm dec}$ set by $\Lambda^\ast$;
     - E2's compute-cap rate from EV9, at 2.8× and from 1.5× to 64×;
     - E3's tempo arithmetic.
   - The tempo arithmetic is computed here as an illustration, not a block:
     - with a 7-month doubling: 0.55, 0.30 and 0.09;
     - with a 131-day doubling: 0.38, 0.14 and 0.02.
   - §6.2 covers release: readiness, readrule, dwell and hysteresis, and it points to X11's *Readiness, read today* and *Where things stand*.
   - §6.3: "rates of human overrule" became catch rates of planted errors, in both the coverage paragraph and the E1 paragraph (Ali m11; v6.0 B3).
9. **§8 Research programme.**
   - **Study 2** is rewritten from S4.2 and S13: what the five implementations found, the corrected failure signature, what was done since V6.1 (the dwell of an alternative lineage), and what remains.
   - **New studies:**
     - Study 6, faithful AI in a harmful game: v5.2 B9's two low-cost experiments, which the v6.0 alignment review (minor 9) found unlisted;
     - Study 7, the strategic models for outside review: multiplicity, catch-up, $n\ge3$, the full stochastic game, and the least-value punishment.
   - **The meta-loop toy** is a suggestion, with block ML's numbers. It is described as it is: the present toy uses a logistic response chosen for the toy, so the condition "rebuilt from the paper's own pieces, or dropped" is stated.
   - **Γ calibration template** by channel: compute, algorithms, talent, data and rule support. It gives ranges only where the register has them, plus S2's illustrative thresholds, and states no estimates.
   - **ASTRA** gets one sentence in Study 4: which of its layers V6.2 carries, and which remain (endogenous domains, the ecology of practices).
   - **Within-pool free riding**: computed contributions are added to Study 3 (U10 #11).
10. **§9 Independence.**
    - Family bias, made concrete: the joint models and the meta-loop toy are the family's preferred kind, and the evidence on the tax comes from developers.
    - What Codex checked and found: four errors the family missed. Its eight boundary cases now run in blocks.
    - The full list of V6.2 results for outside review.

## CLAIMS: what is new, and the choices made

1. **§1 Thesis.**
   - Stated as the installed abstract states it, sentence by sentence, with R, A or D provenance.
   - The meaning sentence uses the identity wording, marked as rendering D34.
   - "What is not claimed" mirrors §1.4, including blocs.
2. **§2 Definitions.**
   - Updated to V6.2: three conditions plus the closure; the structural and equilibrium gains; the won share; the two errors; Ψ's three predicates.
   - Capture's two directions; coverage in hazard modes, with the four conditions of contestable correction; the four divergence classes.
   - R1–R9, with R9 pending; E1 narrow and broad; the tiers, with "favourable to withdrawal"; tracks.
3. **§4 Inventory.**
   - 112 results in section order, core and Supplement interleaved.
   - Columns: key, V6.2 number (rendered from the key), V6.1 number, title, tag, proof and check blocks, status and what changed.
   - Titles were supplied for V6.1's untitled in-prose results: wow, unequal, noinside, countervail, join, preventattack, nonsum, freeze, transmit.
4. **§5 Dependency chain.**
   - §5.1: by threshold, the nine rows of Table 7.1. Each row gives where it is shown, its support, its status on the present path, its crux, and what answers it (R rows, G marks, tier items).
   - §5.2: by link, the nine items of §1.2.
5. **§6 Open interfaces.** From the final S13: open, closed and premise interfaces.
6. **§7 Dispositions.**
   - **§7.1**: the synthesis's §二 table, nineteen rows, each with its reviews.
   - **§7.2**: the synthesis's §四 items A–H, where they are not already §7.1 rows, with the review items each answers.
   - **§7.3**: every remaining important item and every remaining minor of each review. These include:
     - Codex on Test M and Test Γ;
     - Adv-F F4–F13;
     - Adv-O I1, I5, I6, Q6 and the minors;
     - Ali minors 1–15;
     - Sys m1–m4.
   - **§7.4**: the synthesis's §五 decisions and §七 outside-review list.
   - **§7.5**: the v6.0 alignment items V6.1 never recorded (B3, B4, minors 3, 4 and 6, plus minor 9). It also corrects "Evidence asymmetries and citation errors": partly repaired at V6.1, with I1–I6 fixed now.
   - **§7.6**: V6.1's own table of the v6.0 reviews, brought forward with what V6.2 changed (no loss).
   - Status words: fixed / narrowed / declined (reason) / open.
   - **Declined, with reasons:**
     - Γ calibration in the core (Adv-O I1);
     - the meta-loop toy in the core (Sys m3);
     - compression to a venue's length now (Adv-F F6, Adv-O I8): narrowed, by Ren's direction;
     - polycentric redesign as a requirement (F5): narrowed.
   - **Open:** Adv-O Q6; T3's floating predicate (cosmetic); the outside-review list.
   - Findings carry V6.1's numbers. The V6.2 column cites by key, and the section's intro says so.
7. **§8 D list.**
   - 42 entries:
     - D1–D35 for §2–§12, S3, S5, S8 and X10;
     - D36–D42 for the front matter and terms;
     - a closing note on three formulations in the theory's own voice that compress his rulings without attributing them to him.
   - Sources: merge-notes U02–U12, elegance-notes, front-notes §4, the X1 verification, and a scan of every `[corpus: …]` and "the author" sentence in the assembled THEORY, SUPPLEMENT and DISCUSSION.
   - **Flagged as attribution uncertain or misattributed:**
     - D9: §3.8's "In the author's words" on the causal-chain drafters' sentence;
     - D30 and D32: §11.1 and §12.2, lines of an AI-drafted prompt Ren pasted;
     - D7: §3.8's quotation marks on the README's paraphrase of "winner justifies all".
8. **§9 Decisions for Ren:**
   1. R9;
   2. the Meadows reading;
   3. "host";
   4. quotation conventions and the three doubtful attributions;
   5. "favoured" or "to continue" (front-notes open issue 3);
   6. "at least in proportion";
   7. the S4.2(2)(b)–(c) derivation;
   8. the $d^\ast$ body;
   9. placement (0.9495; the readiness table; `frontier`).

## Statuses that rest on other agents' files

Several CLAIMS rows say "fixed in LEDGER", "fixed in README" or "CHANGELOG". These follow the instructions of the LEDGER, CHANGELOG and README task in `planning/workflows/v62-front-registers.js`, which runs after this one. That agent should confirm each:
- **LEDGER:**
  - the sentence-level table;
  - reasons for the nine V6.1 withdrawals (two reclassified as restated);
  - LEDGER §5's blanket sentence removed;
  - §7's "S5" misrecord fixed;
  - entry barriers, the hysteresis prediction and Meadows recorded.
- **CHANGELOG:** the "four conditions" departure; the name sentence in §1.4 rather than §0.
- **README:** the alignment reading path (Ali m15).

## Found in passing, for the integration editor (not fixed; outside these files)

1. **DISCUSSION X1, Grieco 1988 entry:** "manufactured by compounding wherever reinvestment's relative return exceeds its common return". Plan §8.3 replaces "manufactures" with "prices standing".
   - The assembler's banned list does not catch this form; it catches "manufactures the relative objective" only.
   - DISCUSSION's other "manufacture", in X10's injection paragraph ("manufacture the certificate failures"), is ordinary usage and needs no change.
2. **THEORY §6.3:** "hidden loyalties … (Davidson, Finnveden and Hadshar 2025)". The report's terms are "singular" and "secret" loyalties (x1-notes, *For the integration editor* item 3); X1 already uses them.
3. **THEORY §3.8, §11.1, §12.2:** "In the author's words" before lines whose authorship the corpus does not settle (D9, D30, D32).
   - **§3.8, Ψ2:** quotation marks on a paraphrase (D7).
   - **§6.4:** "(Turner et al. 2021)" for the bounded-goal case should read "(compare Turner et al. 2021)" (x1-notes item 4).
4. **EVIDENCE gap 7** should name the analogue base rate: the survival and capture of bodies with verification or custody mandates. X8 and TESTS C4 cite gap 7 for it (U08 #8; Adv-O m6).
5. **xref's term list** maps 'host' to 宿主 and 'signatures' to 签名, both now banned in the guide (front-notes open issue 2).
6. **checks:** T3's last line prints "exists iff bias<1/4: True" at the boundary (Math-F m9; s13-notes item 4). Cosmetic.

## Not done

- The registers were not reviewed by a second agent.
- The D list was assembled from the notes and a scan, not by reading every sentence of the companions against the corpus. X1's verification covers the keyed passages.
