/-
LL1 dependency audit (19 October 2026), not part of the core: it imports Lean. Compiled against the
package's modules built by scratch_build.py (Becoming.LeastLoss and Becoming.Continuation), it lists
for each named rest law which whole-number descent its proof reaches, walking the constants of each
proof, and checks that each whole-number restatement in Becoming.LeastLoss has the same Lean type as
the theorem it restates. Output: deps.log beside this file.
-/
import Becoming.LeastLoss
import Becoming.Continuation
import Lean
open Lean Elab Command

partial def closureOf (env : Environment) (root : Name) : NameSet := Id.run do
  let mut seen : NameSet := {}
  let mut todo : Array Name := #[root]
  while h : todo.size > 0 do
    let n := todo.back
    todo := todo.pop
    if seen.contains n then continue
    seen := seen.insert n
    if let some ci := env.find? n then
      let used := ci.type.getUsedConstants ++ (match ci.value? with | some v => v.getUsedConstants | none => #[])
      for m in used do
        if !seen.contains m then todo := todo.push m
  return seen

elab "#rest_deps" : command => do
  let env ← getEnv
  let descents := [`Becoming.falls_not_recurring, `Becoming.falls_not_recurring_from_floor,
    `Becoming.falls_stop_unrefuted]
  let laws := [`Becoming.Flow.fed_from_beyond, `Becoming.Flow.rising_fed_from_beyond,
    `Becoming.Flow.taking_draws_in, `Becoming.Flow.taking_not_recurring_from,
    `Becoming.Flow.Balances.taking_not_recurring, `Becoming.Flow.Dissipative.opens,
    `Becoming.World.rests_unrefuted, `Becoming.World.comes_to_rest_unrefuted,
    `Becoming.World.rests_unrefuted_enclosed, `Becoming.World.rests_unrefuted_around,
    `Becoming.World.Finite.comes_to_rest_unrefuted,
    `Becoming.World.rests_unrefuted_without_refinement,
    `Becoming.World.rests_unrefuted_refinement_counted,
    `Becoming.Flow.change_stops_unrefuted_around, `Becoming.Web.generation_stops_unrefuted]
  for l in laws do
    if (env.find? l).isNone then
      logInfo m!"{l}: NOT FOUND"
      continue
    let c := closureOf env l
    let used := descents.filter c.contains
    logInfo m!"{l}: {used}"
#rest_deps

elab "#same_statements" : command => do
  let env ← getEnv
  let pairs := [(`Becoming.falls_not_recurring, `Becoming.whole_falls_not_recurring),
    (`Becoming.falls_stop_unrefuted, `Becoming.whole_falls_stop_unrefuted),
    (`Becoming.Flow.taking_not_recurring_from, `Becoming.Flow.taking_not_recurring_whole),
    (`Becoming.Flow.takers_within_on, `Becoming.Flow.takers_within_on_whole),
    (`Becoming.Flow.change_stops_unrefuted, `Becoming.Flow.change_stops_unrefuted_whole),
    (`Becoming.World.rests_unrefuted_enclosed, `Becoming.World.rests_unrefuted_enclosed_whole)]
  for (a, b) in pairs do
    match env.find? a, env.find? b with
    | some x, some y => logInfo m!"{a} vs {b}: same statement = {x.type == y.type}"
    | _, _ => logInfo m!"{a} / {b}: NOT FOUND"
#same_statements
