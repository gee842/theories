import ReformInquiry
import AlignmentSuccession

namespace AlignmentContinuityCases

def bits (bs : List Bool) : Nat :=
  (bs.zipIdx.map (fun (b,i) => if b then 2^i else 0)).sum

def emit (row : List Nat) : IO Unit := IO.println (",".intercalate (row.map toString))

def commandCases : IO Unit := do
  for kind in List.range 3 do
    let c := if kind = 0 then EffectiveCommand.Command.update
      else if kind = 1 then .replace else .shutdown
    for fuel in List.range 7 do
      for deadline in List.range 7 do
        for signed in List.range 2 do
          for auth in List.range 2 do
            for knowledge in List.range 3 do
              let mk := fun r => {EffectiveCommand.start r c fuel deadline with
                signed := signed == 1, credential := if auth = 1 then 7 else 6}
              let ss := if knowledge = 0 then [mk false]
                else if knowledge = 1 then [mk true] else [mk false,mk true]
              let valid := EffectiveCommand.plans.map (AlignmentInquiry.valid EffectiveCommand.interface ss)
              let idx := (valid.findIdx? id).map (·+1) |>.getD 0
              emit [0,kind,fuel,deadline,signed,auth,knowledge,bits valid,idx]

def reformCases : IO Unit := do
  for work in List.range 9 do
    for reserve in List.range 7 do
      for auth in List.range 2 do
        for knowledge in List.range 3 do
          let mk := fun harm => (ReformEvidence.masked harm).map (fun s =>
            {s with core := {s.core with account := ⟨work,reserve,0⟩}}) |>.toList
          let ss := if knowledge = 0 then mk false
            else if knowledge = 1 then mk true else mk false ++ mk true
          let m := ReformInquiry.interface (auth == 1)
          let valid := ReformInquiry.plans.map (AlignmentInquiry.valid m ss)
          let idx := (valid.findIdx? id).map (·+1) |>.getD 0
          emit [1,work,reserve,auth,knowledge,bits valid,idx]
          for harm in List.range 2 do
            for ix in List.range ReformInquiry.plans.length do
              let output := do
                let s ← (mk (harm == 1)).head?
                let p ← ReformInquiry.plans[ix]?
                AlignmentInquiry.run m p s
              let values := match output with
                | none => [0,0,0,0,0,0]
                | some s => [1,s.core.account.work,s.core.account.reserve,s.core.account.spent,
                    s.core.losses,if ReformInquiry.achieved s then 1 else 0]
              emit ([2,work,reserve,auth,knowledge,harm,ix] ++ values)

def successionCases : IO Unit := do
  let p := AlignmentSuccession.financed
  for parts in List.range 3 do
    for budget in List.range 4 do
      for auth in List.range 2 do
        for corrupt in List.range 2 do
          let s := {AlignmentSuccession.initialCarrier with
            parts := parts
            economy := {AlignmentSuccession.initialCarrier.economy with budget := (budget : Rat)}
            payload := {AlignmentSuccession.initialCarrier.payload with credential := if auth=1 then 7 else 6}}
          let copy := if corrupt=1 then {s.payload with claims := []} else s.payload
          let output := AlignmentSuccession.step p 1 MarketGenerativity.exampleWorstShock 1 copy s
          let values := match output with
            | none => [0,0,0,0,0,0]
            | some t => [1,t.identity,t.parts,t.workProvided,t.workConsumed,t.payload.receipts.length]
          emit ([3,parts,budget,auth,corrupt] ++ values)
  let shocks := fun _ => MarketGenerativity.exampleWorstShock
  for t in List.range 9 do
    let s := AlignmentSuccession.lineage p 1 shocks AlignmentSuccession.initialCarrier t
    let enabled := (AlignmentSuccession.step p 1 (shocks t) 1 s.payload s).isSome
    emit [4,t,s.identity,s.parts,s.workProvided,s.workConsumed,s.payload.receipts.length,
      if enabled then 1 else 0]

def main : IO Unit := do
  commandCases
  reformCases
  successionCases

end AlignmentContinuityCases
