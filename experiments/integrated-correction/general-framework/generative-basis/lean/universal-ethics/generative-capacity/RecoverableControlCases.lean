import RecoverableControl
import MediatedControlCases
namespace RecoverableControlCases
open RecoverableControl MediatedControl TemporalInspection EvidenceQualifiedCorrection FaultTolerantCorrection CorrectionReconfiguration FallibleInspection
open MediatedControlCases

def backing : Device → Machine | .ready m => m | .busy r => r.target
def actual : Device → World | .ready m => m.tracked.actual | .busy r => r.actual
def pending : Device → Bool | .ready _ => false | .busy _ => true
def remaining : Device → Nat | .ready _ => 0 | .busy r => r.todo.length+1

def outputs (d : Device) : List Nat :=
  let m := backing d
  let s := m.tracked.installation.state
  [number (pending d),worldNumber (actual d),worldMask m.tracked.possible,s.spent,s.reserve,s.time,
   number s.completed,number s.running,m.tracked.installation.serial,m.generation,m.journal.length,
   remaining d,number (RecoverableControl.use .command d).isNone,number (m.tracked.possible.contains (actual d))]

def inspection (w : World) : List RecoverableControl.Event :=
  (inspectEvents (physical w)).map RecoverableControl.Event.use

def normalOps : List Write := ops.take 9
def replayPrograms : List (List Write) := [[]] ++ normalOps.map (fun a => [a]) ++
  normalOps.flatMap (fun a => normalOps.map (fun b => [a,b]))

def schedule (code : Nat) : List RecoverableControl.Event :=
  (List.range 3).map (fun i => if bit code i then .crash 1 else .tick)

def finish (d : Device) : Bool × Device :=
  RecoverableControl.run ((List.replicate (remaining d) RecoverableControl.Event.tick) ++ [.use .command]) d

def main : IO Unit := do
  for (p,pi) in replayPrograms.zipIdx do
    for (w,wi) in worlds.zipIdx do
      for n in List.range (p.length+1) do
        let intermediate := writes (p.take n) w
        emit [0,pi,wi,n,worldNumber intermediate,worldNumber (writes p intermediate),worldNumber (writes p w)]
  for (old,oi) in worlds.zipIdx do
    for (new,ni) in worlds.zipIdx do
      for code in List.range 8 do
        for fuel in [10,22,23,30] do
          for deadline in [22,30] do
            let es := inspection old ++ [.prepare ⟨0,.steady,targetProgram new⟩] ++ schedule code
            let firstRun := RecoverableControl.run es (.ready (start old fuel deadline))
            let out := finish firstRun.2
            emit ([1,oi,ni,code,fuel,deadline,number firstRun.1,number out.1] ++ outputs out.2)
  for (p,pi) in programs.zipIdx do
    for rights in List.range 4 do
      for generation in List.range 2 do
        let d : Device := .ready (start ⟨.left,some 0⟩ 30 30 ⟨bit rights 0,bit rights 1⟩)
        let out := RecoverableControl.run [.prepare ⟨generation,.steady,p⟩] d
        emit ([2,pi,rights,generation,number out.1] ++ outputs out.2)
  for (old,oi) in worlds.zipIdx do
    for (new,ni) in worlds.zipIdx do
      for count in List.range 3 do
        let es := inspection old ++ [.prepare ⟨0,.steady,targetProgram new⟩] ++ List.replicate count RecoverableControl.Event.tick
        let d := (RecoverableControl.run es (.ready (start old 30 30))).2
        let bad := loseMarker d
        let m := backing bad
        emit ([3,oi,ni,count,number (RecoverableControl.use .command d).isNone,
          number (m.tracked.possible.contains (actual bad)),number (certificate roster4 (pooled describe (models m.tracked.possible)) (fun i => decide (2≤i)))] ++ outputs bad)
end RecoverableControlCases
