**P79: the laws of one step are all the laws of one step.** Under Ren's "move towards 100%", completeness in the strong sense, which held for counting only (`tally_iff_counted`), is proved for Locality's laws of one step. A new core module `Becoming.OneStep` (imports `Counting` and `Sampling`), no axiom, no premise, no existing module changed.
- **Exact under each condition.** A pattern (the passages of a family's members, the count of takers, whether something exchanges) is shown by some world exactly when it obeys the law of every step (`OneStep.every_iff`), and on a family balanced on, running down, closed, or both, exactly when it also obeys that condition's law (`OneStep.balance_iff`, `OneStep.runsDown_iff`, `OneStep.closed_iff`, `OneStep.runsDownClosed_iff`); so a property holds of every such step exactly when it holds of every pattern obeying the law (`OneStep.laws`). Across runs on one family the only further law is that what stands after each step stands before the next (`OneStep.Chained`, `OneStep.run_every_iff`).
- **Two laws the spine had not stated.** Something taken has a taker (`Flow.sign_uptake_le_takers`); nothing is taken beyond what stood with what was given (`Flow.BalancesOn.taken_le`). Without the first, the stated laws allow a pattern no world shows (`OneStep.stated_not_realized`); with it they are the whole law for a family running down closed (`OneStep.runsDownClosed_iff_stated`).

- **Givers, capacity and activity (P79b).**
  - Something given has a giver: the givers number at least one wherever anything is given, and at most what is given (`OneStep.Givers`).
  - Running down adds exactly that every giver takes (`Flow.DissipatesOn.renewers_le_takers`).
  - Capacity adds exactly that what is given is at most capacity times the givers (`OneStep.every_capacity_iff`).
  - Activity at the step adds no law (`OneStep.every_active_iff`).
- **Families chosen step by step (P79b).**
  - Where the family may change at each step, no condition, balance and closure join no step to the next (`OneStep.step_every_iff`).
  - Running down joins steps by continuity up to order: at each positive level as many stand after a step as before the next (`OneStep.Continues`, `OneStep.step_runsDown_iff`).
  - This is strictly weaker than following position by position (`OneStep.steps_not_run`, `OneStep.vanishing_steps`).

The readings are the AI's, pending Ren.

Not covered:
- counting active relata (it needs activity decided);
- capacity and activity over runs.

Built by Opus subagents of the session (311 theorems, empty axiom reports). No independent review yet.
