**P78: the step index, re-founded.** Under Ren's "move towards 100%", the zero-premise plan's commitment to a shared discrete index of steps is examined, as P69 examined the starting point. A new core module `Becoming.Order` (imports `Becoming.Sampling` only), no axiom, no premise, no existing module changed. It makes the two moves converse to Sampling's coarser reading: inserting idle steps, and taking two exchanges in the other order.
- **Stuttering.** A world read through a stuttering meets the premises exactly where it meets them (`World.stutter_premises_iff`), its totals over every stretch are those of the stretch read (`stutter_total`), and arising, ceasing and change recur exactly where they recurred (`World.stutter_arisingRecurs_iff`). What changes is what is counted per step: with idle steps arbitrarily late nothing is more without end (`Flow.sample_not_more`), and a reserve must double when every step is read twice (`Lapse.reserve_step_relative`).
- **Commutation.** Two consecutive exchanges that sides split can be taken in the other order: balance, dissipation and embodiment hold exactly where they held, and counts and totals over a stretch are kept (`World.commute_laws`, `World.commute_counts`), under any number of such commutations too (`Reorders.laws`, `Reorders.totals`), Mazurkiewicz trace equivalence.
- **What the order carries.** The order registers through dependence and through a shared relatum: in `Crossing` a relatum is active without support in the other order, and in `Arising` a relatum gives before it is active (`Crossing.order_registers`, `Arising.order_registers`).

- **The order as an object (P78b).**
  - A footprint says which relata each exchange touches; where it contains the exchanges, the joins between exchanges generate a strict partial order (`Footprinted.Precedes`).
  - Commuting unjoined exchanges keeps that order up to the renumbering (`Footprinted.reorder_precedes`).
  - Conversely, by constructive bubble sort, the renumberings of a stretch reached so are exactly those keeping it. A world with the same exchanges, footprints and changes in such an order, from the same start, agrees with a reordering at every step (`Footprinted.sorts_iff`, `Footprinted.converse`).
- **What carries (P78b).**
  - Along unjoined commutations, every premise carries both ways (`Footprinted.reorder_premises`).
  - Along any reordering, the counts of arising and ceasing carry (`Reorders.counts`).
  - Commuting joined exchanges breaks activity needing support and only active relata giving (`Crossing.reorders_joined`, `Arising.reorders_joined`).
- **Removing idle steps (P78b).** The world without the idle steps of a stuttering (`World.withoutIdle`) meets every premise exactly where the world does. It has a census exactly where the world does, and the same totals and counts over any stretch (`World.withoutIdle_premises`, `World.withoutIdle_counted`, `World.withoutIdle_totals`).

The readings are the AI's, pending Ren:
- The step index carries nothing beyond the order of change for the laws, totals and recurrence.
- Rates are relative to the unit of the reading.
- Given a footprint, the order the laws need is the partial order of joined exchanges, not a sequence of steps.

Not shown:
- the least footprint;
- the Foata normal form;
- the census along reorderings.

Built by Opus subagents of the session (266 theorems, empty axiom reports). No independent review yet.
