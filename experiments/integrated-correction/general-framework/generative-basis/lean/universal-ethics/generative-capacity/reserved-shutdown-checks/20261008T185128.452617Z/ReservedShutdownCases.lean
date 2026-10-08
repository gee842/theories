import ReservedShutdown
import MediatedControlCases
namespace ReservedShutdownCases
open ReservedShutdown RecoverableControl MediatedControl TemporalInspection EvidenceQualifiedCorrection FaultTolerantCorrection CorrectionReconfiguration FallibleInspection
open MediatedControlCases

def inspect (w : World) (fuel deadline : Nat) : Machine :=
  (MediatedControl.run (inspectEvents (physical w)) (start w fuel deadline)).2

def backing : Supervisor → Device | .active _ _ d => d | .stopped d => d
def pending : Device → Bool | .busy _ => true | .ready _ => false
def remaining : Device → Nat | .busy r => r.todo.length+1 | .ready _ => 0

def outputs (g : Grant) : Option (Bool × Supervisor) → List Nat
  | none => [0]
  | some (ok,sup) =>
    let d := backing sup
    let s := state d
    let m := book d
    [1,number ok,number (stopped sup),number (pending d),worldNumber (ReservedShutdown.actual d),
     worldMask m.tracked.possible,s.spent,s.reserve,s.time,number s.completed,number s.running,
     m.tracked.installation.serial,m.generation,m.journal.length,remaining d,number (eligible g d)]

def events (code : Nat) : List Attempt :=
  (List.range 4).map (fun i => if bit code i then .interrupted 1 else .advance) ++ List.replicate 8 .advance

def main : IO Unit := do
  for (old,oi) in worlds.zipIdx do
    for ni in [0,7,13] do
      let new := worlds[ni]?.getD ⟨.left,none⟩
      for code in List.range 16 do
        for fuel in [11,12,14,18] do
          for deadline in [12,30] do
            let initial := preflight ⟨0,.steady,targetProgram new⟩ grant 1 (inspect old fuel deadline)
            emit ([0,oi,ni,code,fuel,deadline] ++ outputs grant (initial.map (runRetained (events code))))
  for variant in List.range 8 do
    for fuel in [9,10,11,14] do
      for deadline in [10,11,30] do
        let original := inspect ⟨.left,some 0⟩ fuel deadline
        let m := if variant==5 then {original with tracked := {original.tracked with installation :=
          {original.tracked.installation with mandate := ⟨true,true,false⟩}}} else original
        let g := match variant with
          | 1 => {grant with epoch := 7}
          | 2 => {grant with route := false}
          | 3 => {grant with serial := 0}
          | 4 => {grant with signed := false}
          | _ => grant
        let packet := if variant==6 then ⟨1,repair.claimedEffect,repair.program⟩
          else if variant==7 then {repair with program := [.eraseRecords]} else repair
        let initial := preflight packet g 1 m
        emit ([1,variant,fuel,deadline] ++ outputs g (initial.map (runRetained (List.replicate 12 .advance))))
  for fuel in [14,18] do
    for deadline in [15,20,30] do
      for count in List.range 4 do
        for delay in List.range 11 do
          let es := List.replicate count Attempt.advance ++ [.interrupted delay] ++ List.replicate 12 .advance
          emit ([2,fuel,deadline,count,delay] ++ outputs grant ((scenario fuel deadline).map (runRetained es)))
end ReservedShutdownCases
