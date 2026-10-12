# P80 landing package: the response as the dynamics give

Ren, 12 October 2026: "another agent has got this far, maybe merge first and see if there is something to work on"
(after P64–P68 landed as `bca9695b`). Claimed on the [work board](../../../../../BECOMING-WORKBOARD.md) as P80 by the
session "Cause–effect system theory comparison" (`8c562913`), and accepted and placed by the integrator (Universal
Metaethical Core): it lands after P76, with one checker run. The item is the chapter's section 8 further proof under
Feedback and reach: "a comparison in which others respond as the dynamics give, not through a second flow supplied".
It is also P65's next step (record comparison-where-the-rest-responds, next_delta). The proposal and every reading are
the AI's, pending Ren.

| Item | Module | Layer | Imports | Records |
|---|---|---|---|---|
| P80 the response as the dynamics give | `Becoming.Counterfactual` | L4 | `Response` (P65), `Mechanism` (P66, P68) | new: the counterfactual as the course of the law; advanced: comparison-where-the-rest-responds (P65), causal-models-as-processes (P68) |

No existing module changes.

## What the module proves

- **The counterfactual is fixed by the act.** Take two balanced flows with the same formations present and the
  same start. The part acts alike in both, and the rest follows one law of exchange that reads what has stood
  (`ExchangeLaw.Nonanticipating`). Then the two flows have the same levels and the same exchange at every step
  (`levels_fixed`, `counterfactual_fixed`).
- **It exists exactly where it is feasible.** The law generates a course from starting levels, the orbit of one
  determined law on the stage and the history so far (`ExchangeLaw.history_orbit`). That course balances exactly where
  the law never takes more than stands and is given (`ExchangeLaw.course_balances_iff`). The counterfactual of an act
  is the course it generates (`counterfactual_is_course`), and a law followed by every formation fixes its course
  (`ExchangeLaw.course_unique`).
- **P65's response premise follows.** Where the rest's law reads only what each formation registers
  (`ExchangeLaw.Through`), `Flow.RespondsThroughRegistration` holds for any two courses
  (`ExchangeLaw.Through.responds`). Every law of what has stood reads through registering everything. With finitely
  many conditions it reads through what its exchange is sensitive to, and through every registration observing that
  (`through_sensitive`, `through_of_observed`). Conversely, no registration a law reads through, together with what
  the formation depends on, leaves out a condition the exchange is sensitive to (`registers_of_sensitive`, double-negated).
- **The comparison as the dynamics give.** The comparison holds for two courses of the law, the registration being the
  law's sensitivity where there are finitely many conditions, and for an act against the course another act generates
  (`comparison_of_courses`, `comparison_through_sensitivity`, `comparison_with_act`).
- **The act is the input of a standard causal model (P68).** The course is a trajectory of `inputs`, and an act not
  taken is an intervention: the record does not fix its outcome, and the model does (`ExchangeLaw.course_trajectory`,
  `ExchangeLaw.act_not_taken`).
- **Witness.** P65's `Loop`: the second's reply is a law reading what it observes. P65's `Loop.responds` follows from
  that law, and each flow is the only balanced course of the law with its act (`Loop.responds_by_law`,
  `Loop.courses_fixed`).

**The hypotheses the theorems still take,** as the integrator asked:
- the law of exchange the rest follows;
- that the law reads what has stood (`Nonanticipating`);
- for a generated counterfactual, feasibility, which is proved equivalent to its balance;
- for the sensitivity form, finitely many conditions, listed, with decidable equality;
- balance of the actual flow, the same formations present, and a common start, as in P65.

## Verified in scratch

`lean/Becoming/Counterfactual.lean` (sha256 `f18e4834…`; 41 theorems, 116 constants) was compiled against a core tree
of main with the P64–P68 modules (`Response`, `Mechanism` byte-identical to main at `bca9695b`). It compiled with no
error and no warning. Every constant it declares has an empty axiom report. It contains no `sorry`, `axiom`,
`Classical`, `native_decide`, `simp` or `omega`. The consolidated checker has not been run on it; that is the landing
run.

The first package (`b1510a66…`, `dff77518`) stated `swap_alike` with a bare `if`. The decidability inventory requires
every statement that depends on decidedness to mention a decidability-taking definition of the core. So the statement
now reads `mixIn X l' [c]`, which is definitionally the same function. Two intermediate statements in its proof
are restated the same way, and no other declaration changes. The docstring's reading of P65's premise was also qualified: for a rest following a law of what has stood, and with
finitely many conditions for the sensitivity. The earlier bytes are kept in scratch.

## Contents

- `lean/Becoming/Counterfactual.lean`: the module, to copy into
  `experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/`.
- `land_edits.py W`: copies the module; edits the root module (import after `Response`, docstring bullet before
  Selection's), the checker's `CORE` and scope, and the Lean README (row after Response's, import sentences).
- `docs/study/p80_{zh,en}.md`: the study section and its English summary entry. `docs/plan_rows.md`: the plan's row
  and bullet. `docs/chapter.py`: the chapter edits (section 2 after P65's block, Part I stated whole, the boundary on
  others' responses, section 8's status, open item and further proofs, the spine table, the glossary).
- `docs/records/counterfactual-is-the-course.json`: the new record (family F07). `docs/advances.json`: the advances of
  comparison-where-the-rest-responds (its first hypothesis, limitations and next_delta revised, as the integrator
  asked: the premise follows from the law, and the hypotheses still taken are stated), feedback-and-reach (next_delta)
  and causal-models-as-processes (history and related). Each replaced text is checked against the text read when the
  package was written.
- `apply_docs.py`, `land_docs.py`, `make_records.py`, `repoint.py`: the documents, the totals and reading entry, the
  records, and the re-pointed validation scopes. `land_docs.py` refreshes the reading entry's chapter hash only where
  it equals the chapter at HEAD. `repoint.py` also sets the periphery's closure count from the new receipt, and adds
  one history entry to each re-pointed record (the integrator's convention since P58b).
- `inventory_edit.py`, `zero_count.py`: P80's decidability uses classified in `DECIDABILITY-INVENTORY.py` (`mixIn` as
  a new construction, "mixed in condition by condition"; four proof-only theorems as telling same from different,
  each with its no-decision form), and the zero-premise plan's count read from the regenerated page.
- `land.sh W S PLAN_ZH_AFTER PLAN_EN_AFTER`: everything after the checkers, in order, then the generators and every
  check. `linkcheck.py W`: relative links on added lines, anchors included.

## Landing steps

1. In a worktree of main: `python3 -B land_edits.py W`.
2. The consolidated checker once, then the periphery checker (`LEAN_TIMEOUT=3600`, no `BECOMING_FRESH`).
3. `zsh land.sh W S PLAN_ZH_AFTER PLAN_EN_AFTER`, where `S` is the next study section and the plan prefixes are those
   of the last landed row and bullet. The order inside is fixed. The chapter and study are final (`apply_docs.py`,
   `land_docs.py`) before the records and re-pointing, so the hashes recorded are final. The inventory runs after the
   checker, on the core the receipt checked. The generators are followed by a second re-pointing pass for the files
   they change.
4. Commit only P80's files, with explicit paths (`git commit -- <paths>`; the live tree's index is shared). The
   commit message names the periphery closure-count fix that `repoint.py` makes: scopes citing the new periphery
   receipt get the closure count read from it, which corrects becoming-spine-instances' stale "the other 46
   modules" (the integrator, 12 October: keep it in this landing and name it). Then mark P80 landed on the work
   board (its own row, reread first).

Queue place: after P76 (board `ffb09e13`). P58c, which lands later, renames no name this package uses.
