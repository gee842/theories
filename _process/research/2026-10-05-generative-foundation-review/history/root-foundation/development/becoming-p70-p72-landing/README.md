# P70–P72 landing package: what a description keeps and loses, a registration within what it registers, contextual registration

Ren, 12 October 2026, asked what the framing loses ("wave/particle, 道可道非常道"), what makes a split make sense and "what makes a pair, a pair?". After the AI's answer Ren said "push the frontier, as far as possible". Ren then asked the AI to dig deeper into the pair. Ren also corrected the AI's reading of 道可道: "i was speculating there is a "truth", but when we model it, projection is the limitation … i also speculate the full "truth" can be derived, situationally, including the cognition/controller part". To the AI's test of that speculation Ren answered "keep prove to the deepest, i agree with your last reply(just saw), be smart, resolve and connect things elegantly. and for the open questions, if they need to be answered to move forward, answer them" ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-framing-and-pairs.md); [directive register](../../../../../RESEARCH-DIRECTIVES.md)). Every reading in this package is the AI's, pending Ren. Ren agreed with the reply that contained them.

The items are claimed on the [work board](../../../../../BECOMING-WORKBOARD.md) by the session "Current math core (fork)" [b79a26]. P72q was written and checked by "Cause–effect system theory comparison" [d00a85], the owner of P64–P68, and is placed here with P72.

| Item | Module | Layer | Imports | Records (F01) |
|---|---|---|---|---|
| P70 what a description keeps and loses | `Becoming.Description` | L4 after P73 (L3 otherwise) | `Unfolding` (P69), `Diagonal`, `Context`, and `Learning` (P73) once patched | separation-loses-the-relation, the-split-that-makes-sense |
| P71 a registration within what it registers | `Becoming.Diagonal` | L2 | `Recurrence` | registration-within-what-it-registers |
| P72 contextual registration | `Becoming.Context` | L2 | `Frame` | contextual-registration |
| P72q quantum realization of the Mermin–Peres square | `Becoming.Quantum` | L2 | `Context` | in contextual-registration |

No existing module changes, and none of the four modules adds a premise.

## What it contains

- **`Becoming.Description`** (51 theorems by the checker's parser; 53 with the Learning patch).
  - **Separation loses exactly the relation.** `separation_faithful_iff`, `separation_surplus`, `whole_not_in_pairs`. On Specker's pairs, parity is a whole its pairs do not give back (`evenBoxes_not_determined`).
  - **A relation forms, lasts and ends in the joint law.** `copy_relates`, `relation_persists`, `forgetting_unrelates`, `coupling_relates_and_unrelates`.
  - **The split that makes sense, under a determined law.** `Law.makesSense_of_law`, `Law.now_makesSense_iff_goAlike`, `Law.part_makesSense_iff_step`, `Law.adaptive_makesSense_iff`. Position and velocity form a pair (`Motion`).
  - **States read off a registered history.** `SameAhead`, `alike_moments_iff`, `finitely_many_states_iff`, `Law.Returns.states`. The two-valued denial has exactly two states (`Denial.two_states`).
- **`Becoming.Diagonal`** (26 theorems).
  - **The diagonal.** `gap_unsaid` and `claims_incomplete`; `Frame.self_incomplete` lives in namespace `Becoming.Frame`.
  - **Completeness exactly where nothing differs.** `complete_iff_alike`, with `fixed_of_complete`.
  - **Completing is an unfolding.** `Unfolds` with `never_returns` and `unheld`; one exists (`unfolding_open`).
  - **The liar as a rhythm.** `revision_never_rests`, `denial_returns`.
- **`Becoming.Context`** (28 theorems).
  - **Gluing.** `Contextual.glues_iff_agree`.
  - **Context-free claims as a commitment of the representation.** `Contextual.fitsFree_iff`, `Contextual.indexed_fits`, `Contextual.no_free_frame`.
  - **Wholes and their parts.** `glued_of_whole`, `restrict_local`, `no_whole`.
  - **Witnesses.** Specker's three boxes and the Mermin–Peres square.
- **`Becoming.Quantum`** (37 theorems by the parser; 43 by its author's count). The nine two-qubit observables as integer matrices, their line products, and `no_context_free_values`.

**Reviews.** "Cause–effect system theory comparison" reviewed all three modules twice and found no errors:

- **First review** (Description 6af48ab0, Diagonal c98eb6a8, Context a655aa36). It proposed the one-step forms, injectivity only on what occurs, and `no_free_frame` needing one configuration.
- **Second review** (10d7b043, e14821d9, 349fbc63, read against the first). It found four wording points: `no_whole`'s condition, `Unfolds.incomplete`, the step index behind the law of moments, and "repeats from some moment on".

Every suggestion is adopted and credited in the study sections.

## Verified in scratch

Checked with `becoming/scratch_build.py` against main's core at a64ff7db, with P69's `Unfolding` (46c3d049…):

- `Diagonal` (1a1d3ecb…), `Context` (c454da2d…), `Quantum` (5bfd7529…) and `Description` (dc0d80e6…) compile with no error or warning.
- Every source declaration has an empty axiom report. The generated `injEq` lemmas of `Contextual.mk`, `Square.Line.row` and `Square.Line.column` depend on `propext`, and the checker allows and lists them.
- There is no `sorry`, `axiom`, `Classical` or `native_decide`.
- **With the Learning patch.** `lean/learning_patch.py` applied to `Description`, built with P73's `Learning.lean` (a73c889e…): `Description` has 53 theorems and empty axiom reports.
- **Not yet run.** The consolidated checker has not run on any of this; that is the landing run.

**Quantum's names.** The checker's declaration parser drops a trailing prime: it reads `neg'` as `neg`, and the audit then fails with an unknown constant. So the landing copy of `Quantum` renames four helpers:

| Old | New |
|---|---|
| `neg'` | `negAt` |
| `zero_mul'` | `int_zero_mul` |
| `zero_add'` | `int_zero_add` |
| `neg_one_mul'` | `int_neg_one_mul` |

Statements are unchanged, and the owner agreed. The owner's evidence copy in `../becoming-p72q-quantum/` is unchanged. No core module on main uses a primed name.

## Contents

- **`lean/Becoming/{Description,Diagonal,Context,Quantum}.lean`.** Copy them to `experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/`.
- **`lean/learning_patch.py`.** Apply it to the copied `Description.lean` when P73's `Becoming.Learning` is on main. This is the integrator's order: P69, then P73, then P70–P72.
  - **What it changes.** `Description` then imports `Learning`. `Law.goAlike_process_iff` becomes the instance of Learning's identical `goAlike_iff_lumped`, written independently; its name and statement are kept. It also adds `lasso_iff_sameAhead` and `finitely_many_states_iff_lasso`.
  - **Who writes the identities.** The second to land writes them, as agreed with P73's owner.
- **`docs/study/p7{0,1,2}_{zh,en}.md`.** The three study sections and their English summary entries, with placeholders.
- **`docs/chapter.py`.** The chapter edits:
  - in §1, what makes a pair a pair;
  - in §3, the split that makes sense, a registration within what it registers, and contextual registration;
  - item 9 of the theory stated in full;
  - Part I stated whole, sections 一 and 三;
  - in §8, the status row, Ren's choices and further proofs;
  - the §9 spine rows;
  - the glossary.

  Several anchors are lines the P69 package adds.
- **`docs/learning.py`.** Text that depends on whether P73 landed first: the layer, the imports, the identities, and where the spine row goes.
- **`docs/plan_rows.md`.** The unification plan's three rows and bullets.
- **`docs/records/*.json`.** The text of the four new records.
- **Scripts.** `apply_docs.py`, `make_records.py`, `repoint.py` (which skips the four new records) and `root_edits.py`.

## Landing steps

In queue order, after P69 and P73, with one checker run:

1. **Modules.** Copy the four modules, then run `python3 -B lean/learning_patch.py <checkout>/…/Becoming/Description.lean` if P73 is on main. Then run `python3 -B root_edits.py ROOT core`.
2. **Checker.** Run the consolidated checker once. Then run `check_correction_inquiry.py`, which imports the root.
3. **Docs.** Run `python3 -B apply_docs.py ROOT S PLAN_ZH_AFTER PLAN_EN_AFTER`.
   - `S` is the next free study section: P70 takes `S`, P71 `S+1`, P72 `S+2`.
   - The plan prefixes are those of the row and bullet that land just before: P73's, or P69's if P73 has not landed.
4. **Records.** Run `python3 -B make_records.py ROOT REVIEWED_AT_UTC S`, then `python3 -B repoint.py ROOT BASE`, then `python3 -B root_edits.py ROOT readmes`.
5. **Totals and checks.** Update the chapter's §9 totals and the Lean README's verification totals with the receipt's counts. Then run `make research-render` and `make research-check`.
6. **Commit and board.** Commit only these changes, and mark the board.

## For the integrator to decide

**Context-free claims as a commitment of the representation.** The core's `Frame` reads claims as context-free by type. P72 proves when that fits:

- exactly where the registrations glue at every configuration;
- the frame indexed by context always fits;
- quantum registrations do not glue.

The proposal is to list "context-free claims" in ZERO-PREMISE-PLAN §1.2 beside discrete steps, natural-number amounts, the shared index and relata listed once. P72 is the condition under which that commitment fits. Ren decides whether it is listed.

## Codex takeover landing, 13 October 2026

Landed from the preserved package after P73–P75. The four source modules and the Learning instance patch passed the consolidated checker (core receipt `20261013T084405.661795Z`) and CorrectionInquiry (receipt `20261013T084521.070057Z`). The package now covers 3,114 theorems and 4,559 declaration audits; every source declaration in the pure core has an empty axiom report. These packages add 144 theorems. Study sections 94–96, four canonical records, chapter, catalogue and inventory are reconciled. The two new proof-only equality uses in Diagonal are classified explicitly. Research render/check passed; the five existing generativity-chain errors remain an independent historical maintenance issue.

This integration reuses the package's two recorded reviews; it does not claim a fresh independent mathematical review. The representation choices and empirical correspondence boundaries above remain open. The original package and scratch evidence remain preserved.
