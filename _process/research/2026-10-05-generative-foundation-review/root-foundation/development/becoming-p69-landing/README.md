# P69 landing package: one unfolding and its readings

Ren, 12 October 2026, asked of the core's first two layers: "is this dualistic?". The AI proposed restating the four splits from `World`, leaving `GenerativeCore` unchanged, and Ren answered "yes, put it on the board and start" ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-relational-starting-point.md); [directive register](../../../../../RESEARCH-DIRECTIVES.md)).

On another branch of the same conversation Ren agreed with one reading: law and history are one unfolding read two ways, the law read off the unfolding rather than set over it. Ren's words were "yes, i do agree with your reading, there are no two realities" ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-no-two-realities.md)). Every other reading is the AI's, pending Ren.

The item is claimed on the [work board](../../../../../BECOMING-WORKBOARD.md) as P69 by the session "Current math core" [1c3084].

| Item | Module | Layer | Imports | Records |
|---|---|---|---|---|
| P69 one relational starting point | `Becoming.Unfolding` | L3 | `Mechanism` (P66), `Space` | process-and-frame-as-readings, configurations-alike-by-relation (F01) |
| P69 bridge section | `Becoming.Bridge` (periphery) | bridge | adds `ExplanatoryBranching` | in configurations-alike-by-relation, if landed |

- **No existing core module changes.** `Unfolding` imports P66's `Becoming.Mechanism`, so this package lands after P64–P68.
- **Bridge change.** The bridge gains one section and one import. That is the integrator's call; see below.

## What it contains

`Becoming.Unfolding` has 67 theorems and 103 declarations by the checker's parser. They fall into five groups:

- **The move within the configuration.** `withMove`, `closedBy`, `unlabelled` and `Fork`.
- **A world's moves as its relata's exchanges.** `Exchange`, the law of exchange, `World.move`, `World.balances_iff_exchange` and `Circulation`.
- **A history and the law it shows.** `Shown`, `exists_law_iff`, and where the correspondence is not an identity: `DeadEnd`, `Splice` and `Run.keepHistory_shown`.
- **Claims as relata.** `Frame.world` and `Frame.novel_iff_arises`.
- **Configurations alike by relation.** `Bisimulation`, `Alike`, `DeterminedAt`, `Twins`, `MakesSense`, and for a determined law `Law.alike_iff_sameFuture`.

The work of two other branches is restated here on this module's definitions and credited in the docstring, records and study:

- **Five groups from "Current math core (fork 2)".** Its [evidence](../becoming-p69-shape-evidence/README.md) gives the dead end, the splice, the kept history, the shared move and `Circulation`.
- **`MakesSense` from "Current math core (fork)".** Its [evidence](../becoming-framing-evidence/README.md) defines it for one determined law; here it covers frames that branch and carry claims.

The framing fork's P70 (`Becoming.Description`) imports this module and builds on its names. It has dropped its own `Law.SameFuture`.

## Verified in scratch

The checks ran against main at ae17922a, with the core's 49 modules taken from the shared cache, plus the P64–P68 package at 413d8543, including its patched `Capture`.

- **The module.** `Unfolding` compiles with no error or warning. All 246 constants it declares, compiler auxiliaries included, have empty axiom reports. It contains no `sorry`, `axiom`, `Classical` or `native_decide`. `by decide` appears only on natural-number literals.
- **The bridge.** The bridge section is `lean/bridge_section.lean`. It was appended to main's `Becoming.Bridge` with `import ExplanatoryBranching`, which brings in 7 inherited modules, each with a passed receipt. Over the bridge's full import closure it compiles with no error or warning, and all 122 constants have empty axiom reports.
- **No name clashes.** A file importing the root, the four P64–P68 modules, `Unfolding` and the bridge compiles.
- **Not yet run.** The consolidated checker has not been run on any of this; that is the landing run.

## Contents

- **`lean/Becoming/Unfolding.lean`.** Copy it to `experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/`.
- **`lean/bridge_section.lean`.** Append it to `Becoming/Bridge.lean` before the final `end Becoming`, and add `import ExplanatoryBranching` after `import CorrectionInfrastructure`.
- **`docs/study/p69_{zh,en}.md`.** The study section and its English summary entry, with placeholders.
- **`docs/chapter.py`.** The chapter edits:
  - §1's opening and a P69 paragraph;
  - item 1 of the theory stated in full;
  - Part I stated whole, sections 一 and 三;
  - §8: the status row, Ren's choices and further proofs;
  - the §9 spine row;
  - the glossary: process, frame, and five new terms.

  Several anchors are lines the P64–P68 package adds.
- **`docs/plan_rows.md`.** The unification plan's row and bullet.
- **`docs/records/*.json`.** The text of the two new records. `configurations-alike-by-relation` carries a `bridge` part, which the records script uses only if the receipt's `Becoming.Bridge` declares `deeper_bisimulation_iff`. P69 advances no existing record's next_delta.
- **Scripts.** `apply_docs.py`, `make_records.py` and `repoint.py`, adapted from P64–P68's. `repoint.py` skips the two new records.

## Landing steps

1. **Modules.** Copy the module, and the bridge section if you take it (below). Add the module to `Becoming.lean` (root) and to `CORE` in `check_becoming.py`, with the edits below.
2. **Checker.** Run the consolidated checker once.
3. **Docs.** Run `python3 -B apply_docs.py ROOT S PLAN_ZH_AFTER PLAN_EN_AFTER`.
   - `S` is P69's study section, the one after P64–P68's.
   - After P64–P68, the plan prefixes are `'| P67 吸引'` and `'- **P67:**'`.
4. **Records.** Run `python3 -B make_records.py ROOT REVIEWED_AT_UTC S`, with `REVIEWED_AT_UTC` written as `2026-10-12T12:00:00+00:00`. Then run `python3 -B repoint.py ROOT BASE`.
5. **Totals and checks.** Update the chapter's section 9 totals and the Lean README with the receipt's counts. Then run `make research-render` and `make research-check`.

### Dry run

The package was dry-run on a copy of ae17922a. On it, the P64–P68 package was applied first by its own scripts, under a stand-in receipt; the copy also held the framing fork's committed evidence. P69 was then applied under a second stand-in receipt, with theorem counts by the checker's parser (`Unfolding` 67, `Bridge` 44).

- **Anchors and records.** Every anchor matched once, and the records script wrote both records with the bridge part.
- **Repoint.** `repoint.py` rewrote the stamps of 73 records.
- **Checks.** `make research-render` and `make research-check` passed with no error and no drift.
- **Links.** The 47 links in the inserted text resolve, anchors included.
- **Without the bridge section.** With main's `Becoming.Bridge` instead, the records script names branching-tests-bisimulation as related only and drops the bridge sentence and reference.

## Root module, checker and Lean README

**`Becoming.lean`.** Add `import Becoming.Unfolding` after `import Becoming.Mechanism`. Then add this docstring bullet after Mechanism's:

```text
* `Becoming.Unfolding` (L3): one unfolding and its readings (P69). The labelled process and the
  frame are readings of a world: read within the configuration the move changes no run and is
  what the law leaves open, and a world's move is its relata's exchange, balance being running by
  the law of exchange; every history is a run of the law it shows, the least one, determined
  exactly where the history is consistent, the correspondence failing to be an identity through
  dead ends and splices and closing where the history is kept; a claim is a relatum and novelty
  is arising; configurations are alike where a bisimulation relates them, pass the same tests,
  and are named sensibly exactly where alike ones are one; determinacy as equality depends on
  names. Ren confirmed the reading of law and history; the other readings are the AI's.
```

**`check_becoming.py`.** Add `"Becoming.Unfolding"` after `"Becoming.Mechanism"` in `CORE`. Add this scope sentence after Mechanism's:

```text
"Unfolding: read with the move inside the configuration a process has the same runs, the law "
"leaving the next move open and determined exactly where it is with moves as labels and one move "
"wherever it steps; with the move formed within by a policy, runs from one configuration agree; "
"a shared move couples the parts of a synchronized product; a world balances exactly where its "
"standings run by the law of exchange with its relata's exchanges as moves, the exchange fixing "
"the standings from a beginning and the standings not fixing the exchange; every history is a "
"run of the law it shows, the least law it is a run of, determined exactly where the history is "
"consistent, a law can have a step and no run, a revisiting history shows a law admitting a run "
"it never took, and a kept history shows a law admitting only it; a frame along a run is a world "
"whose relata are its claims, novelty being arising; configurations are alike where a "
"bisimulation relates them, an equivalence with no quotient, and alike ones pass the same tests; "
"determinacy up to likeness passes along likeness while determinacy as equality depends on names; "
"a description makes sense where it identifies exactly the alike configurations, and then carries "
"a law where the frame is determined up to likeness; under a determined law likeness is the same "
"registered future; under the law of exchange standings are alike exactly where they agree "
"pointwise. "
```

**Lean README.** The row after Mechanism uses the chapter's spine-table description, `SPINE_L3` in `docs/chapter.py`, with an English half from the docstring bullet above. The import sentences gain "`Unfolding` 导入 `Mechanism` 与 `Space`" (L3), with the English to match.

## For the integrator to decide

- **The bridge section.** It adds `import ExplanatoryBranching` to `Becoming.Bridge`, and with it 7 inherited modules that have passed receipts. It proves that `RelationalDynamics`' `Deeper.Bisimulation` (6 October) and `ExplanatoryBranching.Bisimulation` are the core's `Bisimulation`, and that alike configurations pass every branching test.
  - **If you decline it,** change "which `Becoming.Bridge` shows to be this one" in `Unfolding`'s docstring to "which a bridge can show to be this one". The records script then adapts by itself. In the study and chapter text, drop the bridge rows and sentences.
  - **Bridge docstring.** If you take it, a bullet for the bridge docstring could read: "`Deeper.Bisimulation` and `ExplanatoryBranching.Bisimulation` are the core's `Bisimulation` on frames with no claims and with a model's conditions as claims (`deeper_bisimulation_iff`, `branching_bisimulation_iff`); alike configurations pass every branching test (`Alike.same`)."
- **Names that could clash later.**
  - `unlabelled` and Mechanism's `forget` are different: `forget` drops the second part of a move, `unlabelled` drops the whole move.
  - `Exchange` (structure) and `exchange` (process) differ only in case. The record aliases keep only `Becoming.Exchange`, because the register compares aliases without case.
- **The §1 opening.** The chapter's opening "**机制。** 起点是过程" becomes "**起点。** 起点是一个展开", the World-first reading. The integrator decides whether the opening changes before Ren reads it.
