import TemporalInspection
namespace TemporalInspectionCases
open TemporalInspection EvidenceQualifiedCorrection FaultTolerantCorrection CorrectionReconfiguration FallibleInspection

def bit (mask i : Nat) : Bool := mask / 2^i % 2 == 1
def number (b : Bool) : Nat := if b then 1 else 0
def modelNumber : Model → Nat | .left => 0 | .swapped => 1 | .right => 2
def faultNumber (w : World) : Nat := match w.fault with | none => 0 | some n => n+1
def worldNumber (w : World) : Nat := 6*modelNumber w.model+faultNumber w
def worldMask (xs : List World) : Nat :=
  (worlds.zipIdx.filter (fun p => xs.contains p.1)).foldl (fun n p => n+2^p.2) 0

def family (hs fs : Nat) : List World := worlds.filter (fun w => bit hs (modelNumber w.model) && bit fs (faultNumber w))
def report (n : Nat) : Option Bool := match n with | 0 => none | 1 => some false | _ => some true

def physical (w : World) (d : Domain) (arbitrary : Option Bool) : Option Bool :=
  if fails ((auditArrangement true w.model).vulnerability d) (roots w) then arbitrary else some (diagnostic w.model)

def outputs (events : List Event) (s : State) : List Nat :=
  let result := runUntilBlocked events s
  let out := result.2
  [number result.1,worldNumber out.actual,worldMask out.possible,TemporalInspection.mask out.possible,
   out.installation.state.spent,out.installation.state.reserve,out.installation.state.time,
   out.installation.serial,number out.installation.state.completed,number out.installation.state.running,
   out.records.length,number (out.possible.contains out.actual),number (auditRun events s).isSome]

def emit (xs : List Nat) : IO Unit := IO.println (String.intercalate "," (xs.map toString))

def main : IO Unit := do
  for hs in List.range 8 do
    for fs in List.range 64 do
      for d in List.range 5 do
        for r in List.range 3 do
          let out := receive (family hs fs) d (report r)
          emit [0,hs,fs,d,r,worldMask out,TemporalInspection.mask out]
  for hs in List.range 8 do
    for fs in List.range 64 do
      for (c,ci) in [Change.steady,.mobile,.control,.reset].zipIdx do
        let out := predict c (family hs fs)
        emit [1,hs,fs,ci,worldMask out,TemporalInspection.mask out]
  for (w,wi) in worlds.zipIdx do
    for code in List.range 243 do
      let rs : Reports := fun d => physical w d (report (code/3^d%3))
      let events := scan rs ++ [.command]
      emit ([2,wi,code] ++ outputs events (TemporalInspection.initial w 16 16))
  for (old,oi) in worlds.zipIdx do
    for (new,ni) in worlds.zipIdx do
      let before : Reports := fun d => physical old d (some (!diagnostic old.model))
      let after : Reports := fun d => physical new d (some (!diagnostic new.model))
      let events := scan before ++ [.move .reset new] ++ scan after ++ [.command]
      for fuel in [0,4,5,6,12,20,22,23] do
        for deadline in [22,23] do
          for permission in List.range 4 do
            let start := {TemporalInspection.initial old fuel deadline with
              inspectionAllowed := bit permission 0
              changeAllowed := bit permission 1}
            emit ([3,oi,ni,fuel,deadline,permission] ++ outputs events start)
  for (h,hi) in hypotheses.zipIdx do
    for code in List.range 216 do
      let events := ([0,2,4].zipIdx.flatMap (fun p =>
        let f := code/6^p.2%6
        let next : World := ⟨h,if f==0 then none else some (f-1)⟩
        [Event.move .mobile next,Event.read p.1 (physical next p.1 (some (!diagnostic h)))])) ++ [.command]
      emit ([4,hi,code] ++ outputs events (TemporalInspection.initial ⟨h,none⟩ 30 30))
end TemporalInspectionCases
