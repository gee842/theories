import CorrectionReconfiguration
namespace CorrectionReconfigurationCases
open CorrectionReconfiguration FaultTolerantCorrection

def bit (mask i : Nat) : Bool := mask / 2^i % 2 == 1
def subset (n mask : Nat) : List Nat := (List.range n).filter (bit mask)
def formulas : List FaultExpr :=
  let atoms := (List.range 3).map FaultExpr.cause
  let base := atoms ++ (atoms.flatMap (fun a => atoms.flatMap (fun b => [.any a b,.all a b])))
  base ++ base.flatMap (fun e => [.any e (.cause 3),.all e (.cause 3)])
def assignment (n : Nat) : Arrangement :=
  ⟨[0,1,2],fun d => .cause (n / 4^d % 4),[]⟩
def number (b : Bool) : Nat := if b then 1 else 0
def emit (xs : List Nat) : IO Unit := IO.println (String.intercalate "," (xs.map toString))

def main : IO Unit := do
  for (e,i) in formulas.zipIdx do
    for mask in List.range 16 do
      emit [0,i,mask,number (fails e (subset 4 mask))]
  for code in List.range 64 do
    for family in List.range 16 do
      let a := {assignment code with rootFaults := (subset 4 family).map (fun r => [r])}
      for support in List.range 8 do
        emit [1,code,family,support,number (ready a),number (certificate a.roster (envelope a) (bit support))]
      for actual in List.range 16 do
        let roots := subset 4 actual
        let available := certificate a.roster (envelope a) (fun d => !(fails (a.vulnerability d) roots))
        let exposed := (induced a roots).foldl (fun m d => m+2^d) 0
        emit [2,code,family,actual,exposed,number available]
  for (a,scheme) in [separate3,merged3,repaired4,duplicated4].zipIdx do
    for auth in List.range 2 do
      for cost in List.range 4 do
        for depth in List.range 4 do
          for fuel in List.range 21 do
            for deadline in [5,13,20] do
              let old : Managed := ⟨separate3,{initial with state := {initial.state with reserve := fuel,deadline := deadline}}⟩
              let result := reconfigure (auth==1) cost depth a old
              match result with
              | none => emit [3,scheme,auth,cost,depth,fuel,deadline,0,fuel,0,7,0]
              | some next => emit [3,scheme,auth,cost,depth,fuel,deadline,1,next.installation.state.reserve,
                  next.installation.state.spent,next.installation.state.authority,next.installation.serial]
end CorrectionReconfigurationCases
