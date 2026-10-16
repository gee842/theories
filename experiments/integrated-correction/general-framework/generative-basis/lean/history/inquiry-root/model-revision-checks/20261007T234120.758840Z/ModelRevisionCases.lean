import ModelRevision

open Generative.ModelRevision

def bit (b : Bool) : String := if b then "true" else "false"
def statusText : Status → String
  | .inadequate => "inadequate"
  | .needsProbe => "needs_probe"
  | .settledOnAvailable => "settled_on_available"

def emitRow (kind : String) (index fuel : Nat) (actual : Law)
    (initial result : State) (available : List Probe) : IO Unit := do
  let correct := result.candidates.all
    (fun r => allProbes.all (fun p => predict r p == actual p))
  let present := !result.candidates.isEmpty
  let oldRetained := result.history.take initial.history.length == initial.history
  if !oldRetained then throw (IO.userError "History overwritten")
  let full := result.history.map Prod.fst == allProbes
  if full && present && !correct then throw (IO.userError "Complete audit retained false prediction")
  IO.println (String.intercalate "," [kind, toString index, toString fuel,
    toString initial.candidates.length, toString result.candidates.length,
    toString result.history.length, statusText (status result available),
    bit present, (if present then bit correct else "not_applicable"), bit full, bit oldRetained])

def main : IO Unit := do
  IO.println "kind,mechanism,budget,initial_candidates,final_candidates,records,status,has_model,all_eight_predictions_correct,all_eight_observed,history_retained"
  let residuals : List Reports := [(false, true), (true, false), (true, true)]
  let mut index := 0
  for term in terms do
    for residual in residuals do
      let actualRepair : Repair := ⟨term, residual⟩
      let actual := predict actualRepair
      let observed := acquire actual (SourceReliance.protocol ++ [discovery])
      let initial := start observed
      for fuel in [0, 1, 2] do
        let result := investigate actual allProbes fuel initial
        if fuel > 0 && status result allProbes != .settledOnAvailable then
          throw (IO.userError "Represented mechanism did not settle after complete audit")
        if fuel == 0 && status result allProbes != .needsProbe then
          throw (IO.userError "Unexamined declared case was concealed")
        emitRow "generated_grammar" index fuel actual initial result allProbes
      index := index + 1
  let inadequate : State := ⟨[exceptionPatch], discoveryHistory⟩
  for fuel in [0, 1, 2] do
    let result := investigate SourceReliance.jointFailure allProbes fuel inadequate
    if fuel > 0 && status result allProbes != .inadequate then
      throw (IO.userError "Missing correct repair was not exposed")
    emitRow "inadequate_grammar" 0 fuel SourceReliance.jointFailure inadequate result allProbes
  let restricted := investigate SourceReliance.jointFailure [discovery] 1 (start discoveryHistory)
  emitRow "restricted_probe_scope" 0 1 SourceReliance.jointFailure
    (start discoveryHistory) restricted [discovery]
