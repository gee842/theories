import FallibleInspection
namespace FallibleInspectionCases
open FallibleInspection EvidenceQualifiedCorrection FaultTolerantCorrection CorrectionReconfiguration

def bit (mask i : Nat) : Bool := mask / 2^i % 2 == 1
def rootsFor (mask : Nat) : List Nat := (List.range 5).filter (bit mask)
def modelsFor (mask : Nat) : List Model :=
  (hypotheses.zipIdx.filter (fun x => bit mask x.2)).map Prod.fst
def number (b : Bool) : Nat := if b then 1 else 0
def modelMask (models : List Model) : Nat :=
  (hypotheses.zipIdx.filter (fun x => models.contains x.1)).foldl (fun n x => n+2^x.2) 0

def reportsFor (code : Nat) : Reports := fun d => match code / 3^d % 3 with
  | 0 => none | 1 => some false | _ => some true

def reportNumber : Option Bool → Nat
  | none => 0 | some false => 1 | some true => 2

def strategy (mode : Nat) : Reports := fun d => match mode with
  | 0 => none | 1 => some false | 2 => some true
  | 3 => some (d%2==0) | _ => some (decide (2≤d))

def execution (extended : Bool) (reports : Reports) (s : Situation) : List Nat := Id.run do
  let result := run extended reports s
  let out := (result.map Audited.situation).getD s
  let transcript := (result.map Audited.transcript).getD []
  return [number result.isSome, modelMask out.candidates,number (achieved out),
    out.installation.state.spent,out.installation.state.reserve,out.installation.state.time,
    out.installation.serial,number out.installation.state.running,transcript.length,
    transcript.foldl (fun acc pair => acc+(reportNumber pair.2)*3^pair.1) 0]

def emit (xs : List Nat) : IO Unit := IO.println (String.intercalate "," (xs.map toString))

def main : IO Unit := do
  for extended in [false,true] do
    for family in List.range 8 do
      for code in List.range (3^(auditRoster extended).length) do
        let reports := reportsFor code
        let models := posterior extended (modelsFor family) reports
        emit [0,number extended,family,code,modelMask models,number (poolReady (pooled describe models)),
          number (certificate (auditRoster extended) (auditFaults extended .left) (fun d => reports d==some true)),
          number (certificate (auditRoster extended) (auditFaults extended .right) (fun d => reports d==some false))]
  for (h,index) in hypotheses.zipIdx do
    for extended in [false,true] do
      for rootMask in [0,1,2,4,8,16,20] do
        for mode in List.range 5 do
          let reports := simulationReports extended h (rootsFor rootMask) (strategy mode)
          for fuel in [0,10,14,15,16,20] do
            for deadline in [15,16,20] do
              for allowed in [false,true] do
                let s := initialSituation h (rootsFor rootMask) fuel deadline hypotheses allowed
                emit ([1,index,number extended,rootMask,mode,fuel,deadline,number allowed] ++ execution extended reports s)
  for extended in [false,true] do
    for (h,index) in hypotheses.zipIdx do
      for rootMask in [0,1,2,4,8,16,20] do
        for code in List.range (3^(auditRoster extended).length) do
          let reports := simulationReports extended h (rootsFor rootMask) (reportsFor code)
          let s := initialSituation h (rootsFor rootMask) 20 20
          emit ([2,number extended,index,rootMask,code] ++ execution extended reports s)
  for a in List.range 8 do
    for b in List.range 8 do
      for code in List.range 27 do
        let reports := reportsFor code
        let roster := [0,1,2]
        emit [3,a,b,code,
          number (explains roster ((List.range 3).filter (bit a)) true reports),
          number (explains roster ((List.range 3).filter (bit b)) false reports),
          number (roster.all (fun d => (reports d).isSome)),
          number (roster.all (fun d => bit a d || bit b d))]
end FallibleInspectionCases
