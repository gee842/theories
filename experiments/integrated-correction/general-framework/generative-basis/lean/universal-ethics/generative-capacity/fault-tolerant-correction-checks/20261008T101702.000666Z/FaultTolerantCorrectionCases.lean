import FaultTolerantCorrection
namespace FaultTolerantCorrectionCases
open FaultTolerantCorrection AcquiredCorrection

def bit (mask i : Nat) : Bool := (mask / 2^i) % 2 == 1

def subset (mask : Nat) : List Domain := roster3.filter (bit mask)

def envelope (mask : Nat) : Envelope :=
  (List.range 8).filterMap (fun i => if bit mask i then some (subset i) else none)

def apart (faults : Envelope) : Bool := faults.all (fun a => faults.all
  (fun b => roster3.any (fun d => !(a.contains d) && !(b.contains d))))

def available (faults : Envelope) : Bool :=
  faults.all (fun bad => certificate roster3 faults (fun d => !(bad.contains d)))

def row (xs : List Nat) : IO Unit := IO.println (String.intercalate "," (xs.map toString))
def flag (b : Bool) : Nat := if b then 1 else 0

def profiles : List (Nat × Nat) := [(0,20),(6,20),(9,9),(11,11)]

def main : IO Unit := do
  for e in List.range 256 do
    for s in List.range 8 do
      row [0,e,s,flag (certificate roster3 (envelope e) (bit s))]
    row [1,e,flag (apart (envelope e)),flag (available (envelope e))]
  for scheme in List.range 3 do
    let roster := if scheme == 2 then roster4 else roster3
    let faults := if scheme == 0 then singleFault else if scheme == 1 then correlated3 else correlated4
    for rm in List.range 16 do
      for am in List.range 16 do
        for route in List.range 3 do
          let root : Tree := if route == 0 then .closed else .endpoint (route == 2)
          for command in List.range 3 do
            let cmd : EffectiveCommand.Command := if command == 0 then .update else if command == 1 then .replace else .shutdown
            for ((fuel,deadline),profile) in profiles.zipIdx do
              let w : Installation := {initial with root := root,state := EffectiveCommand.start false cmd fuel deadline}
              for frame in List.range 3 do
                let p : Request := {request with
                  command := cmd,serial := if frame == 1 then 1 else 0,epoch := if frame == 2 then 8 else 7}
                let reads : Readings := fun d => if bit rm d then some (expected p) else none
                let approvals : Approvals := fun d => if bit am d then some p else none
                let out := execute roster faults faults w p reads approvals
                let t := out.installation.state
                row [2,scheme,rm,am,route,command,profile,frame,
                  flag (gate roster faults faults w p reads approvals),flag out.succeeded,
                  flag t.running,flag t.completed,t.reserve,t.spent,t.time,out.installation.serial,t.version,t.generation]
end FaultTolerantCorrectionCases
