# P80b: the counterfactual as P69's unfolding (verified in scratch)

The P80↔`Unfolding` instances, left by the integrator to whichever of P69 and P80 landed second (P69 landed
`da8f75a7`). `Becoming/Counterfactual.lean` here is the P80 module with `import Becoming.Unfolding` and one section
added; no existing statement changes. Built with `scratch_build.py` against main at `da8f75a7`: 46 theorems, 72
declarations, every axiom report empty, no error or warning. Whether it lands with P80 or right after it is the
integrator's call.

- `ExchangeLaw.world`, `ExchangeLaw.world_balances_iff`, `ExchangeLaw.world_exchange_iff`, `ExchangeLaw.worldRun`: over
  one kind of relatum the course is a P69 `World`. It balances, and so runs by the law of exchange, exactly where the
  course is feasible.
- `Run.beyond_shown_iff` (any determined law): a law steps beyond what a run of it shows (`Shown`) exactly where it
  steps at all and the run never takes that move there.
- `ExchangeLaw.counterfactual_beyond_shown`: the course's history is `Consistent`. An act has a step of the standard
  model beyond what the history shows exactly where the history never takes it there: what the law adds to the
  history is exactly its counterfactuals.
- `ExchangeLaw.policy`, `ExchangeLaw.closedBy_course`: with the part's act formed by a law of what has stood, a run of
  P69's `closedBy` from the start is the course that act generates, so two such runs agree (`closedBy_runs_agree`).

The readings are the AI's, pending Ren. The counterfactual is a world, and a law's step beyond its history is not a
second history (Ren at P69: "there are no two realities"). With the act formed within the unfolding, the part acting
otherwise is a law of the part otherwise.
