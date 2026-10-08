import MediatedControl
namespace MediatedControlCases
open MediatedControl TemporalInspection EvidenceQualifiedCorrection FaultTolerantCorrection CorrectionReconfiguration FallibleInspection

def bit (mask i : Nat) : Bool := mask / 2^i % 2 == 1
def number (b : Bool) : Nat := if b then 1 else 0
def modelNumber : Model → Nat | .left => 0 | .swapped => 1 | .right => 2
def faultNumber (w : World) : Nat := match w.fault with | none => 0 | some n => n+1
def worldNumber (w : World) : Nat := 6*modelNumber w.model+faultNumber w
def worldMask (xs : List World) : Nat :=
  (worlds.zipIdx.filter (fun p => xs.contains p.1)).foldl (fun n p => n+2^p.2) 0

def family (hs fs : Nat) : List World := worlds.filter (fun w => bit hs (modelNumber w.model) && bit fs (faultNumber w))
def changeNumber : Change → Nat | .steady => 0 | .mobile => 1 | .control => 2 | .reset => 3

def ops : List Write :=
  [.model .left,.model .swapped,.model .right,.fault .clear,.fault .r0,.fault .r1,.fault .r2,.fault .r3,.fault .r4,
   .eraseRecords,.forgePossible [⟨.right,some 2⟩],.replaceInstallation (start ⟨.left,some 0⟩ 30 30).tracked.installation,.grantBoth]
def programs : List (List Write) := [[]] ++ ops.map (fun op => [op]) ++ ops.flatMap (fun a => ops.map (fun b => [a,b]))
def exactPrograms : List (List Write) := [[],[.model .left],[.fault .r4],[.model .right,.fault .r1],
  [.model .left,.model .right],[.fault .r2,.fault .clear],[.model .swapped,.fault .r3,.model .right]]
def targetProgram (w : World) : List Write :=
  [.model w.model,.fault (match w.fault with | none => .clear | some 0 => .r0 | some 1 => .r1 | some 2 => .r2 | some 3 => .r3 | _ => .r4)]

def outputs (events : List MediatedControl.Event) (s : Machine) : List Nat :=
  let result := MediatedControl.run events s
  let out := result.2
  let st := out.tracked.installation.state
  [number result.1,worldNumber out.tracked.actual,worldMask out.tracked.possible,TemporalInspection.mask out.tracked.possible,
   st.spent,st.reserve,st.time,out.tracked.installation.serial,number st.completed,number st.running,
   out.tracked.records.length,number (out.tracked.possible.contains out.tracked.actual),out.generation,out.journal.length,
   (match out.journal.getLast? with | none => 4 | some e => changeNumber e.actualEffect),st.authority,
   number st.signed,number st.issued,number st.delivered,number out.rights.model+2*number out.rights.fault]

def physical (w : World) (d : Domain) : Option Bool :=
  if fails ((auditArrangement true w.model).vulnerability d) (roots w) then some (!diagnostic w.model) else some (diagnostic w.model)
def events (old new : World) : List MediatedControl.Event :=
  inspectEvents (physical old) ++ [.patch ⟨0,.steady,targetProgram new⟩,.command]
def emit (xs : List Nat) : IO Unit := IO.println (String.intercalate "," (xs.map toString))

def main : IO Unit := do
  for (p,pi) in programs.zipIdx do
    for (w,wi) in worlds.zipIdx do
      let out := writes p w
      emit [0,pi,wi,worldNumber out,changeNumber (effect p),number ((successors (effect p) w).contains out)]
  for hs in List.range 8 do
    for fs in List.range 64 do
      for (p,pi) in exactPrograms.zipIdx do
        let old := family hs fs
        emit [1,hs,fs,pi,worldMask (image p old),worldMask (predict (effect p) old)]
  for (p,pi) in programs.zipIdx do
    for rights in List.range 4 do
      for generation in List.range 2 do
        for (claim,ci) in [Change.steady,.mobile,.control,.reset].zipIdx do
          let s := start ⟨.left,some 0⟩ 30 30 ⟨bit rights 0,bit rights 1⟩
          emit ([2,pi,rights,generation,ci] ++ outputs [.patch ⟨generation,claim,p⟩] s)
  for (old,oi) in worlds.zipIdx do
    for (new,ni) in worlds.zipIdx do
      for fuel in [0,4,5,7,8,15,18,19] do
        for rights in List.range 4 do
          emit ([3,oi,ni,fuel,rights] ++ outputs (events old new) (start old fuel 19 ⟨bit rights 0,bit rights 1⟩))
  for (old,oi) in worlds.zipIdx do
    for (new,ni) in worlds.zipIdx do
      for deadline in [8,16,18] do
        emit ([4,oi,ni,deadline] ++ outputs (events old new) (start old 30 deadline))
  for (new,ni) in worlds.zipIdx do
    let m := bypass new previouslyInspected
    emit [5,ni,number (publicView m == publicView previouslyInspected),number (m.tracked.possible.contains m.tracked.actual),
      number (certificate roster4 (pooled describe (models m.tracked.possible)) (fun d => decide (2≤d)))]
  for (old,oi) in worlds.zipIdx do
    for (new,ni) in worlds.zipIdx do
      let p : Packet := ⟨0,.steady,targetProgram new⟩
      emit ([6,oi,ni] ++ outputs [.patch p,.patch p] (start old 30 30))
end MediatedControlCases
