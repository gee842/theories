import Lean
import D36
open Lean Elab Command

#eval show CommandElabM Unit from do
  let env ← getEnv
  for m in [`D35, `D36] do
    let some index := env.getModuleIdx? m | throwError m!"no module {m}"
    let mut count := 0
    let mut withAx := #[]
    for (n, _) in env.constants.map₁.toList do
      if env.getModuleIdxFor? n == some index then
        count := count + 1
        let axioms ← liftCoreM <| Lean.collectAxioms n
        if axioms.size > 0 then withAx := withAx.push (n, axioms)
    logInfo m!"MODULE {m} CONSTANTS {count} WITH_AXIOMS {withAx.size} {withAx.toList}"
#print axioms Becoming.since
#print axioms Becoming.since_before
#print axioms Becoming.since_succ
#print axioms Becoming.since_mono
#print axioms Becoming.falls_within
#print axioms Becoming.Settles
#print axioms Becoming.Settles.rests
#print axioms Becoming.add_sub_turn
#print axioms Becoming.sub_eq_zero_of_le
#print axioms Becoming.add_sub_of_le
#print axioms Becoming.le_sub_of_add_le
#print axioms Becoming.Tended.decideEq
#print axioms Becoming.Closing.store
#print axioms Becoming.Closing.spare
#print axioms Becoming.Closing.place
#print axioms Becoming.Closing.level
#print axioms Becoming.Closing.exchange
#print axioms Becoming.Closing.web
#print axioms Becoming.Closing.flow
#print axioms Becoming.Closing.span
#print axioms Becoming.Closing.place_pos
#print axioms Becoming.Closing.place_zero
#print axioms Becoming.Closing.total_place
#print axioms Becoming.Closing.still_flows
#print axioms Becoming.Closing.still
#print axioms Becoming.Closing.empty_stays
#print axioms Becoming.Closing.outside_empty
#print axioms Becoming.Closing.idle
#print axioms Becoming.Closing.quiet_same
#print axioms Becoming.Closing.within_span
#print axioms Becoming.Closing.moving_within
#print axioms Becoming.Closing.closed
#print axioms Becoming.Closing.span_distinct
#print axioms Becoming.Closing.busy
#print axioms Becoming.World.length_le_stock
#print axioms Becoming.World.change_within
#print axioms Becoming.World.closingQueue
#print axioms Becoming.World.closingQueue_decided
#print axioms Becoming.World.closingQueue_census
#print axioms Becoming.World.closingQueue_embodied
#print axioms Becoming.World.closingQueue_balanced
#print axioms Becoming.World.closingQueue_acting
#print axioms Becoming.World.closingQueue_taking
#print axioms Becoming.World.closingQueue_stock
#print axioms Becoming.World.closingQueue_dissipative
#print axioms Becoming.World.closingQueue_premised
#print axioms Becoming.World.closingQueue_enclosed
#print axioms Becoming.World.enclosed_counting
#print axioms Becoming.below
#print axioms Becoming.fin_eq
#print axioms Becoming.mem_below
#print axioms Becoming.distinct_below
#print axioms Becoming.total_below
#print axioms Becoming.Queue.reached
#print axioms Becoming.Settles.joins
#print axioms Becoming.Settles.reach
#print axioms Becoming.Closed.size
#print axioms Becoming.Closed.front
#print axioms Becoming.Closed.web
#print axioms Becoming.Closed.flow
#print axioms Becoming.Closed.alive
#print axioms Becoming.Closed.front_val
#print axioms Becoming.Closed.placed
#print axioms Becoming.World.closedQueue
#print axioms Becoming.World.closedQueue_decided
#print axioms Becoming.World.closedQueue_finite
#print axioms Becoming.World.closedQueue_census
#print axioms Becoming.World.closedQueue_counts
#print axioms Becoming.World.closedQueue_premised
#print axioms Becoming.World.finite_counting
