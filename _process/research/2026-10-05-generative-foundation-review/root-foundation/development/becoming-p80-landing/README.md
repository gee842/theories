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
  (`through_sensitive`, `through_of_observed`). Conversely, every registration a law reads through holds every
  condition the exchange is sensitive to, together with what the formation depends on (`registers_of_sensitive`).
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

`lean/Becoming/Counterfactual.lean` (sha256 `b1510a66…`; 41 theorems, 116 constants) was compiled against a core tree
of main with the P64–P68 modules (`Response`, `Mechanism` byte-identical to main at `bca9695b`). It compiled with no
error and no warning. Every constant it declares has an empty axiom report. It contains no `sorry`, `axiom`,
`Classical`, `native_decide`, `simp` or `omega`. The consolidated checker has not been run on it; that is the landing
run.
