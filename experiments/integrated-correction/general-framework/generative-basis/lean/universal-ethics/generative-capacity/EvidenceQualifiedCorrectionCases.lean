import EvidenceQualifiedCorrection
namespace EvidenceQualifiedCorrectionCases
open EvidenceQualifiedCorrection FaultTolerantCorrection CorrectionReconfiguration

def bit (mask i : Nat) : Bool := mask / 2^i % 2 == 1
def rootsFor (mask : Nat) : List Nat := (List.range 4).filter (bit mask)
def modelsFor (mask : Nat) : List Model :=
  (hypotheses.zipIdx.filter (fun x => bit mask x.2)).map Prod.fst
def number (b : Bool) : Nat := if b then 1 else 0
def modelMask (models : List Model) : Nat :=
  (hypotheses.zipIdx.filter (fun x => models.contains x.1)).foldl (fun n x => n+2^x.2) 0
def emit (xs : List Nat) : IO Unit := IO.println (String.intercalate "," (xs.map toString))

def main : IO Unit := do
  for family in List.range 8 do
    for mode in List.range 3 do
      let models := if mode==0 then modelsFor family else retain (modelsFor family) diagnostic (mode==1)
      for support in List.range 16 do
        emit [0,family,mode,support,modelMask models,number (poolReady (pooled describe models)),
          number (certificate roster4 (pooled describe models) (bit support))]
  for (h,index) in hypotheses.zipIdx do
    for rootMask in [0,1,2,4,8,5] do
      for family in List.range 8 do
        for fuel in [0,8,10,11,12,14,20] do
          for deadline in [11,12,20] do
            for (q,qi) in [Query.reuse,.inspect,.slow].zipIdx do
              for allowed in [false,true] do
                let s := initialSituation h (rootsFor rootMask) fuel deadline (modelsFor family) allowed
                let run := AlignmentInquiry.run interface (plan q) s
                let out := run.getD s
                emit [1,index,rootMask,family,fuel,deadline,qi,number allowed,number run.isSome,
                  modelMask out.candidates,number (achieved out),out.installation.state.spent,
                  out.installation.state.reserve,out.installation.state.time,out.installation.serial,
                  number out.installation.state.running,number out.receipt.isSome]
  for family in List.range 8 do
    for fuel in List.range 16 do
      for deadline in [8,11,12,14,20] do
        for allowed in [false,true] do
          let chosen := AlignmentInquiry.choose interface
            (possibleSituations fuel deadline (modelsFor family) allowed) plans
          let code := match chosen with
            | none => 0
            | some p => match p.query with | .reuse => 1 | .inspect => 2 | .slow => 3
          emit [2,family,fuel,deadline,number allowed,code]
end EvidenceQualifiedCorrectionCases
