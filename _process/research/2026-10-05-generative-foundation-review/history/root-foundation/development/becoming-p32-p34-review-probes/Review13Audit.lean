import Lean
import Review13
open Lean Elab Command

#eval show CommandElabM Unit from do
  let env ← getEnv
  let some index := env.getModuleIdx? `Review13 | throwError "no module Review13"
  let mut count := 0
  let mut withAx := #[]
  for (n, _) in env.constants.map₁.toList do
    if env.getModuleIdxFor? n == some index then
      count := count + 1
      let axioms ← liftCoreM <| Lean.collectAxioms n
      if axioms.size > 0 then withAx := withAx.push (n, axioms)
  logInfo m!"MODULE Review13 CONSTANTS {count} WITH_AXIOMS {withAx.size} {withAx.toList}"
#print axioms Review13.Balance
#print axioms Review13.tally_balance
#print axioms Review13.tally_le
#print axioms Review13.tally_of_balance
#print axioms Review13.tally_iff
#print axioms Review13.balance_not_tally
#print axioms Review13.ceasing_bound_law
#print axioms Review13.tally_congr
#print axioms Review13.tally_iff_counted
#print axioms Review13.since_le
#print axioms Review13.since_zero_le
#print axioms Review13.settles_zero
#print axioms Review13.settles_iff_zero
#print axioms Review13.same_laws
#print axioms Review13.tended_dissipation_idle
#print axioms Review13.tended_not_binds
#print axioms Review13.ind
#print axioms Review13.ind_split
#print axioms Review13.mark_double
#print axioms Review13.FirstChange.change
#print axioms Review13.FirstChange.since_clear
#print axioms Review13.FirstChange.tally
#print axioms Review13.FirstChange.company
#print axioms Review13.FirstChange.settles
#print axioms Review13.FirstChange.at_first
#print axioms Review13.FirstChange.decide_of_end
#print axioms Review13.SettlesEnds
#print axioms Review13.lpo_of_settlesEnds
#print axioms Review13.FiniteEnds
#print axioms Review13.lpo_of_finiteEnds
#print axioms Review13.OneSwap.change
#print axioms Review13.OneSwap.tally
#print axioms Review13.OneSwap.since_one
#print axioms Review13.OneSwap.settles
#print axioms Review13.OneSwap.world
#print axioms Review13.OneSwap.zero
#print axioms Review13.OneSwap.takes
#print axioms Review13.OneSwap.attained
#print axioms Review13.closed_dissipation_binds
#print axioms Review13.binds_arising
#print axioms Review13.arising_pointwise
#print axioms Review13.binds_adds
#print axioms Nat.add_right_cancel
#print axioms Nat.sub_eq_zero_of_le
#print axioms Nat.add_sub_of_le
#print axioms Nat.le_sub_of_add_le
#print axioms Fin.eq_of_val_eq
#print axioms Nat.sub_add_cancel
#print axioms Nat.le.dest
#print axioms Nat.exists_eq_add_of_le
#print axioms Nat.succ_ne_zero
#print axioms Becoming.add_right_cancel
#print axioms Becoming.le_of_add_le_add_right
#print axioms RelationalRenewal.le_sub_from_add
#print axioms Becoming.le_dest
