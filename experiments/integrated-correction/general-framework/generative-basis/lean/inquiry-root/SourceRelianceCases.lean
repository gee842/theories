import SourceReliance

open Generative.SourceReliance

def bit (b : Bool) : String := if b then "true" else "false"
def answerText : Option Bool → String
  | none => "none"
  | some b => bit b

def main : IO Unit := do
  IO.println "copies,shared,reversed,stage,envelope,target,local_fault,common_fault,candidates,answer,covered,assertion_correct"
  let stages : List (String × List Probe) :=
    [("baseline", [baseline]), ("local", [baseline, localProbe]), ("full", protocol)]
  let envelopes := [("clean", clean), ("local_uncertain", localUncertain), ("all", allFaults)]
  for r in repertoire do
    for reversed in [false, true] do
      for (stage, probes) in stages do
        let routes := learn repertoire (acquire r reversed probes)
        for (envelope, faults) in envelopes do
          for target in [false, true] do
            for f in allFaults do
              let result := rely routes faults (emit r ⟨target, f.1, f.2⟩)
              let covered := faults.contains f
              let correct := result.map (fun b => b == target)
              if covered && correct == some false then
                throw (IO.userError "Covered-world correctness failed")
              IO.println (String.intercalate ","
                [bit r.copiesFirst, bit r.sharesDisturbance, bit reversed, stage,
                 envelope, bit target, bit f.1, bit f.2, toString routes.length,
                 answerText result, bit covered, answerText correct])
