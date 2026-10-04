# V6.2 build notes: integrating the eleven merged units

4 October 2026. This pass integrated the merged units for §2–§12 (with S2–S11, X8, X10 and X11) into a V6.2 that builds, and fixed the mechanical problems. Only `src/` was edited; the assembled documents were regenerated from it. The front matter (00_head, 10_s01, d0_symbols, S0, S13–S15, X1, X2) and the registers other than EVIDENCE are still V6.1's. The only edits there were the minimal ones listed in §1, made to keep the build correct.

## 0. Status

| Step | Result |
|---|---|
| `python3 src/assemble_v62.py` | **no problems**: 95 core and 33 supplement declarations; no unknown or duplicate keys, no forward uses, no doubled kind names, no leftover markup, no banned phrases |
| `python3 refs_v62.py` (from `src/`) | THEORY 119, SUPPLEMENT 74, DISCUSSION 92 entries. No citation lacks an entry, no author form differs, and no two entries share a key |
| `python3 xref_v62.py` | Citation coverage passes in both directions for all three documents; 32/32 must-stay items; no named states or firms in core prose. **One failure remains:** guide items 1 (33%) and 9 (33%) fall below the 60% term match with §1.2. Both the guide and §1.2 belong to the front matter, which has not been rewritten yet (phase 2) |
| `python3 checks_v62.py > checks_v62.log` | **169 passed, 0 failed**, in 282 s. All eight of Codex's boundary cases appear and hold. Apart from the timing line, the output is identical to the checks agent's log |
| Kind-word audit (every `Kind {{#key}}` against the key's kind) | Three mismatches fixed (§1). None remain |
| Section references (`§N.M`, `Section N.M`) | Every reference in THEORY, SUPPLEMENT and DISCUSSION resolves to an existing heading. Only LEDGER's historical rows (v6.0 numbers) do not |
| V6.1→V6.2 paragraph preservation (trigram scan, scratch script modelled on `src/preserve_v62.py`) | 486 V6.1 paragraphs of length 12 words or more: 437 kept and 49 rewritten, with **0 unmatched**. The lowest matches are the reorganized parameter tables (§7.1 → S7 matrix) and V6.1 proofs whose results moved (Cor 11.1, Prop 6.8). Each was checked and has a home |

## 1. What I fixed

**Assembler.**
- `src/assemble_v62.py:8`: the docstring now lists the kind `Table` ("numbered in the same section counter: Table 7.1").
- `src/assemble_v62.py:28`: `KINDS` gained `'Table'`.
- `src/assemble_v62.py:66`: the `DOUBLE` regex gained `Table`, so "Table Table 7.1" is caught.

The plan's other kind changes needed no assembler change, since they are declarations in the units. They are all in place: `require` → Table 9.1, `reachable` → Table 11.5, `slowroute` → Proposition 4.13 ("Silent crossing when capture precedes evidence"), `branches` → Proposition 7.2.

**Bibliography tool (`src/refs_v62.py`).** xref imports its keying rule, so the fixes below apply to both.
- **Name pattern (l.17).** `NAME` allows two particles: `(?:{PART} ){0,2}`. Before, "van der Weij et al. 2024" keyed as "der Weij" and could never match its entry.
- **Key rule (l.26–51).** Where one first author has two or more works with three or more authors in the same year, the key takes the second author, and a bare "X et al. YEAR" is then reported as ambiguous. The set `SHARED` is computed from the data (l.222–227) and holds only (Greenblatt, 2024). Before, "Greenblatt, Roger, Krasheninnikov and Krueger 2024" and "Greenblatt, Denison et al. 2024" both matched the AI-control entry silently, and xref did not see it. Year suffixes would have meant editing the citations in five units; the in-text forms already disambiguate as APA does. The docstring (l.8–11) records the rule. `entry_keys` is split into `_parse_entry` plus `entry_keys`, with unchanged behaviour otherwise.
- **D4 block (l.131–219).** Every entry in D4-evidence-notes §(b), "corrections" and "additions", in the verified form (Verification §Corrected and §Confirmed applied), under its legacy handle. It overrides the v6.0 data and NEW. Two consequences:
  - Copeland 2000b keeps its suffix, because Copeland 2000a exists. Konrad 2009 holds both the Kovenock paper and the book.
  - Schelling is split into 1960 (*The Strategy of Conflict*, Harvard UP, †) and 1966. Before, SUPPLEMENT listed *Arms and Influence* twice.
- **Two works not in D4, cited by S11.**
  - Cho, I.-K. and Kreps, D. M. 1987, *QJE* 102(2):179–221.
  - Wald, A. 1945, *Annals of Mathematical Statistics* 16(2):117–186.

  Both records were confirmed on Crossref today, so they are marked † (record).
- **Marks line (l.247).** The reference lists' header now names the register's five forms ("full text", "page", "abstract"; "record", "not retrieved").
- `src/{core,supp,disc}/z9_refs.md` were regenerated.

**Front matter and registers (minimal edits, to keep the build correct).**

| File:line | Before | After | Why |
|---|---|---|---|
| `src/disc/01_X1.md:48` | (Deutsch 1957) | (Deutsch et al. 1957) | xref "author form differs"; the entry is Deutsch et al. (V6.1 had the same defect) |
| `src/supp/00_S0.md:40` | Theorem {{#slowroute}}'s conditions | {{slowroute}}'s conditions | `slowroute` is now a Proposition; printed "Theorem 4.13" |
| `src/supp/14_S14.md:15` | Proposition {{#require}}, R1 | {{require}}, R1 | `require` is now a Table; printed "Proposition 9.1" |
| `src/reg/CHANGELOG.md:21` | (Propositions …, {{#talk}}, {{#require}} and {{#compound}}, … | (Propositions …, {{#talk}} and {{#compound}}, {{require}}, … | same; printed "Propositions …, 9.1" |
| `src/reg/README.md:26` | Section 9 (R8) | Section 9 (R8a, R8b) | R8 is split in Table 9.1 (U09) |
| `src/reg/EVIDENCE.md:259` | EV16 header "(THEORY §7.1, the gain; V5)" | "(THEORY §7.1, the drive; V5)" | plan §8.3 vocabulary (U07) |

**Cross-unit fixes in the merged units** (each flagged by the merging unit as another unit's to make).

| File:line | Before | After | Source |
|---|---|---|---|
| `src/supp/07_S7.md:7` | delegation is {{delegate}}(2) … where $L_e/n>L_c\Delta\psi$ suffices | {{delegate}}(1) | U06: the dominance condition is part (1) of the V6.2 statement; (2) is now "universal delegation is worse" |
| `src/supp/05_S5.md:66` (`zonesillus`) | $A=\epsilon(b-d)-c$, $B=\epsilon(b/(n-1)+d)$, $K=c+n\epsilon d$, "$d=0.2$" | $h_d$ in all four | U06: the harm coefficient of (15) is now $h_d$ |
| `src/supp/05_S5.md:128` (`jointscissors`) | ($b=1$, $c=0.3$, $d=0.2$, $\epsilon=1$) | $h_d=0.2$ | same |
| `src/supp/07_S7.md:87` (P8) | ({{require}}, R8) | ({{require}}, R8a) | U09: R8 is split |
| `src/supp/07_S7.md:119` (loops table, training loop) | R8 | R8a, R8b | same |
| `src/core/70_s7.md:26` (Table 7.1, Alignment-tax lever) | "…internal deployment included, of equal incidence and sanctioned above the gain from evasion; …" | "…internal deployment included, sanctioned above every type's gain from evasion, and of equal incidence for neutrality among those who comply; …" | U06 item 4. Table 9.1's R8b says equal incidence is "not needed to keep a divergence out" (`blind`(2), `nested`(3)), so the old cell contradicted it. The Load row keeps "of equal incidence", because there it prevents the barrier named in its danger column |

**Not changed.** Nothing in any unit's prose beyond the cells above. There were no unknown keys, no forward uses and no doubled kinds left to fix once `Table` was in the assembler; the merges had already resolved them against each other.

## 2. What remains for the integration editor

### 2.1 Mechanical, for the phase-2 owners

- **Front matter (§0, §1, guide, symbols, S0).**
  - §1.2 still has "every forward-looking actor", "manufactures the relative objective" and "decides whether leads compound" (THEORY l.46–47), and item (4)'s "forms blocs" (U05).
  - The guide still uses 宿主, 签名, 闭合于自身, 这个过程是好的, 弱化身 and 强化身 (l.7–17).
  - The guide/§1.2 term match fails for items 1 and 9. Item 9 needs the tiers as merged (U12 item 8).
  - The box wording "rises at least in proportion" / "less than in proportion" (U02) is used in §2's box (l.85). §1.2 item 1 and the guide must use it, not the plan's "rises with the stock's level".
  - §0's last clause should point to §11.2 for counter-performativity (U11 item 6).
  - The symbol table needs:
    - "R1–R8" → "R1–R9 (R3 and R8 in two parts)", if R9 is kept;
    - "C0–C11" → C0–C13 with C3a/b and C9a–d, N1–N4;
    - "Stages 1–5" → "Tracks 1–5";
    - every rename listed in the merge notes (U02 §4.5, U03 §4.3, U04 §4.6, U06 §4.7, U08 §4.10, U11 §4.4).
  - S0 should define the label **[identity: X]**, which units now use for algebraic checks (EC, JX, RH, BI), beside [num: X].
- **S13–S15.**
  - S13 rows: "T_dec set by Λ*"; "p_d = 1−υ(T_dec)"; new interfaces "stocks and stage payoffs", "human capacity and correction", "correction across models", "reflexive gain off parity"; "capacity and the field" → `capdyn`. Rename S13's $F(U,\dots)$, which clashes with the sanction $F$ (U02, U04, U05, U07).
  - S14 rows: `enforce`(5) should cite the $P<v<C$ example; the `opaquecorr` row should cite the summable example $c_{b,t}=1-2^{-(t+1)}$ (U05, U06).
  - S15 still names `checks_v61.log`.
- **Registers.**
  - CLAIMS: D marks on every model rendering the units list (U03 §4.4, U05 §4.5, U06 §4.8, U07 §4.4, U08 §4.4, U12 §4.3); new keys and kinds.
  - LEDGER: the v6.1→v6.2 crosswalk (§4 below); R4, R5, R8 and R9 history; ASTRA; the Meadows reading.
  - TESTS: C3a/b, C9a–d, C12, C13, N4 rows; C8 "the drive"; Test G "discriminates at intermediate $p_d$"; Test Γ's sign; "Stage 1" → "Track 1"; Study 2's corrected failure signature.
  - CHANGELOG: "four conditions" → three plus closure; every renumbering; `signal`(2) corrected; 0.99 → 0.9495/0.9793.
  - README: the reading paths.
- **Checks (`checks_v62.py`; not edited here).**
  - **Block TR is cited but does not exist.** [num: TR] appears three times in THEORY (`signal`, `pausevalue`, `readrule`) and three times in SUPPLEMENT. Port `planning/drafts/U11/A/checks/tr_transition.py` (12 assertions, U11 item 2).
  - Also asked by units and not yet done:
    - DL(e) `nearlock` (`planning/drafts/U06/B/checks/dl_nearlock.py`);
    - the `homeostasis`(2) two-root example in SM or AL;
    - the QS comment "necessary iff liminf" → "if";
    - an S4.2(2)(b) assertion, and the capture-lag range 8–85 printed across s4 E1 (U04 §4.2);
    - a CI check for the multi-type part of `unravel` (U09 §4.9);
    - a check line for `thrrep`'s cutoffs 0.11/0.47/0.95 (U03 §4.10).
  - Legacy-only numbers (v4.4 SV, v4.5 LD/N22/K7, v5 SR/FS/N13/CMP and the S5 dissipation and coverage figures) still run only under `--legacy`. If they are ported, avoid the names FS and SR, which V6.2 uses (U05 §4.7, U08 §4.3, U10 §4.9).
- **EVIDENCE.** Gap 7 should name the analogue base rate that X8 cites (U08 §4.8). EV18's minimum-tax wording should match X10, per D4 J1 (U09 §4.7).

### 2.2 Judgment (not changed here)

1. **Length.** The core is **59,516 words** against the plan's expected 27–30k (V6.1: 30,525). Every section roughly doubled; §9 more than tripled. The Supplement went from 15.6k to 46.0k words and the Discussion from 8.3k to 15.0k. Each unit lists cuts that would lose nothing (U03 §4.11, U05 §4.9, U06 §4.13, U07 §4.12, U08 §4.11, U10 §4.4, U11 §4.10, U12 §4.9). The largest single candidates:
   - §10's `commonfrontn` to S10 (−250);
   - §11's "Where things stand" to X11 (−160);
   - §3.8's multiplicity figures, which appear three times (U03 §4.8).

   One-home duplication across units is the first place to look.
2. **R9 (human decision authority kept)** is a new row of Table 9.1 that the plan does not name. Ren must confirm it; U09 §4.1 has the removal list.
3. **Crux family names.** §8.4's table cites "C1, C3, C9, C12", while §12.3 defines only C3a/C3b and C9a–d. The family names are readable, but the editor should decide whether to write "C3a, C3b" there.
4. **"Four conditions"** survives in §5.3, §9 (R5) and §12.1 item 1 for the four conditions of contestable correction (legible, overrulable, exercised, resourced). This is not Definition 2.1. It is not the banned use, but a reader of the CHANGELOG ("three conditions, not four") may stumble. Naming it once, "the four conditions of contestable correction", would remove the ambiguity.
5. **Claim-box modals** worth a look:
   - §10's claim "can instead make contribution fund…" (existence or hedge?);
   - §7's "racing can be each actor's best response" (existence; probably right).
6. **§6.6 versus §12.1 item 7:** "a positive tax" against "withdrawn where measured zero or negative" (U12 §4.5). These are compatible, but one phrase should be chosen.
7. **§9's [conj] on the readiness rule's exit bias** can now cite `readrule`(1) for the bias (U11 §4.7).
8. **Quotation conventions:** bracketed repairs ("optimiz[es]", "compet[ing]") against verbatim ("it out grows"); "the author" against "Ren"; the [corpus: key] form (U02 §4.7, §4.9; U06 §4.11; U07 §4.5).
9. **Two joint scissors models** are in S5 (U05 §4.8). If outside review should see only one, drop S5's second specification and JX(g).
10. **Uniform placement of side results** (U05 §4.6). `join`, `preventattack`, `nonsum` and `freeze` keep core numbers with statements in S5, while §6, §8 and §10 moved theirs to S-numbers.
11. **Items for Ren**, as the merge notes list them:
    - box wording "at least in proportion";
    - "host"/母体;
    - the rendering of every quoted line marked D;
    - the Meadows reading;
    - R9;
    - S4.2(2)(b)–(c), a new derivation that corrects both memos;
    - the $d^\ast$ estimating body in X10.

## 3. Word counts

Counted by the assembler: a formula counts as one word, and references are excluded.

| Section | V6.1 | V6.2 |
|---|---:|---:|
| front (title, status) | 77 | 77 |
| 0 (not rewritten) | 343 | 343 |
| 1 (not rewritten) | 1,410 | 1,446 |
| 2 | 2,645 | 4,007 |
| 3 | 3,586 | 5,452 |
| 4 | 2,613 | 4,473 |
| 5 | 3,184 | 5,579 |
| 6 | 2,903 | 6,015 |
| 7 | 2,020 | 5,563 |
| 8 | 3,086 | 5,388 |
| 9 | 870 | 3,089 |
| 10 | 3,484 | 6,520 |
| 11 | 2,318 | 5,921 |
| 12 | 1,664 | 5,321 |
| symbols (not rewritten) | 322 | 322 |
| **Core total** | **30,525** | **59,516** |
| Parts III+IV (§8–§12) | — | 26,239 (44%) |
| SUPPLEMENT | 15,639 | 46,029 |
| DISCUSSION | 8,250 | 15,047 |
| 导读 (not rewritten) | — | 1,181 字 |

## 4. Keys against V6.1's keymap (`../v6.1/src/keymap.json`)

**Removed: none.** Every V6.1 key is still declared.

**Added (21).**

| Key | V6.2 | Where |
|---|---|---|
| `twoerrors` | Remark 3.10 | core |
| `humancorr` | Proposition 4.6 | core |
| `detectlink` | Remark 5.5 | core |
| `scissors` | Proposition 5.17 | core |
| `masked` | Remark 6.8 | core |
| `thresholds` | Table 7.1 | core |
| `eqgain` | Remark S2.2 | supplement |
| `delayosc` | Remark S2.3 | supplement |
| `chansign` | Proposition S2.4 | supplement |
| `gammarange` | Remark S2.5 | supplement |
| `growprize` | Proposition S3.2 | supplement |
| `capdyn` | Proposition S4.2 | supplement |
| `jointscissors` | Remark S5.2 | supplement |
| `nearlock` | Remark S6.1 | supplement |
| `boundedopt` | Remark S6.3 | supplement |
| `unravel` | Remark S9.1 | supplement |
| `crosswalk` | Table S9.2 | supplement |
| `readrule` | Remark S11.1 | supplement |
| `dwell` | Proposition S11.2 | supplement |
| `ratchet` | Remark S11.3 | supplement |
| `capturebasin` | Remark S11.4 | supplement |

`gammarange`, `nearlock`, `boundedopt`, `unravel`, `readrule`, `dwell`, `ratchet` and `capturebasin` are Supplement-only keys the plan did not name. The plan allows such keys.

**Moved from the core to the Supplement** (key kept):

| Key | V6.1 | V6.2 |
|---|---|---|
| `bench` | Remark 2.5 | Remark S2.6 |
| `homeostasis` | Proposition 6.11 | Proposition S6.2 |
| `opaquecorr` | Proposition 6.8 | Proposition S6.4 |
| `lyapunov` | Remark 6.10 | Remark S6.5 |
| `survassure` | Proposition 8.3 | Proposition S8.1 |
| `lead` | Remark 8.6 | Remark S8.2 |
| `sprint` | Remark 8.7 | Remark S8.3 |
| `insure` | Remark 8.9 | Remark S8.4 |
| `overhang` | Proposition 8.12 | Proposition S8.5 |
| `commonfront` | Proposition 10.1 | Proposition S10.1 |
| `rivalverify` | Proposition 10.6 | Proposition S10.2 |
| `participate` | Proposition 10.7 | Proposition S10.3 |

**Kind changes:**
- `branches`: Theorem 7.1 → Proposition 7.2.
- `slowroute`: Theorem 4.12 → Proposition 4.13.
- `require`: Proposition 9.1 → Table 9.1.
- `reachable`: Proposition 11.5 → Table 11.5.

**Renumbered in the core** (kind kept):

| Key | V6.1 | V6.2 |
|---|---|---|
| `pathgen` | 2.6 | 2.5 |
| `onegroup` | 3.10 | 3.11 |
| `club` | 3.11 | 3.12 |
| `psi` | 3.12 | 3.13 |
| `countervail` | 4.6 | 4.7 |
| `masking` | 4.7 | 4.8 |
| `alarm` | 4.8 | 4.9 |
| `certificate` | 4.9 | 4.10 |
| `reabsorb` | 4.10 | 4.11 |
| `pausefield` | 4.11 | 4.12 |
| `relpunish` | 5.5 | 5.6 |
| `restraint` | 5.6 | 5.7 |
| `wingives` | 5.7 | 5.8 |
| `preventattack` | 5.8 | 5.9 |
| `racehazard` | 5.9 | 5.10 |
| `nonsum` | 5.10 | 5.11 |
| `tempo` | 5.11 | 5.12 |
| `coverage` | 5.12 | 5.13 |
| `freeze` | 5.13 | 5.14 |
| `enough` | 5.14 | 5.15 |
| `talk` | 5.15 | 5.16 |
| `raceselects` | 7.2 | 7.3 |
| `racepremise` | 7.3 | 7.4 |
| `profile` | 8.4 | 8.3 |
| `durability` | 8.5 | 8.4 |
| `preventown` | 8.8 | 8.5 |
| `assure` | 8.10 | 8.6 |
| `verify` | 8.11 | 8.7 |
| `commonfrontn` | 10.2 | 10.1 |
| `share` | 10.3 | 10.2 |
| `twoorders` | 10.4 | 10.3 |
| `safeguards` | 10.5 | 10.4 |
| `guardian` | 10.8 | 10.5 |
| `fieldlemma` | S4.2 | S4.3 |

The equation keys and numbers (1)–(15) and (S1) are unchanged, so literal "(9)" and "(14)" still point where they did.
