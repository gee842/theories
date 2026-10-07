import ReconfigurableRoutes

/-! Finite executable samples, not additional theorem claims. -/
open FormationRoutes
namespace ReconfigurationSamples

def treeWord : Tree → String
  | .atom .a => "a"
  | .atom .b => "b"
  | .atom .c => "c"
  | .join l r => "(" ++ treeWord l ++ treeWord r ++ ")"

def portWord : Port → String
  | .left => "L"
  | .right => "R"

def barWord : Bar → String
  | .absent => "N"
  | .loose => "U"
  | .span p q => portWord p ++ portWord q

def bit (b : Bool) : String := if b then "1" else "0"

def events : List ReconfigurableRoutes.Event :=
  [.old .receive, .old .attach, .old .repair, .old .startAB, .old .startBC,
   .old .finishLeft, .old .finishRight, .old .syncLeft, .old .syncRight,
   .release, .startAC, .finishZ]

-- mode0 full; mode1 excludes synchronous assembly; mode2 excludes release.
def permitted (mode : Nat) (s : State) (e : ReconfigurableRoutes.Event) : Bool :=
  decide (ReconfigurableRoutes.Enabled s e) &&
  (mode != 1 || !(e == .old .syncLeft || e == .old .syncRight)) &&
  (mode != 2 || e != .release)

def stateLine (label : String) (mode : Nat) (s : State) : String :=
  let source := match s.source with
    | none => "N"
    | some lot => s!"{lot.raw},{lot.work}"
  let pending := match s.pending with
    | none => "N"
    | some t => treeWord t
  let products := String.intercalate "," (s.products.map treeWord)
  let enabled := String.join (events.map (fun e => bit (permitted mode s e)))
  s!"{label};{source};{s.raw};{s.work};{s.spent};{barWord s.bar};{pending};{products};{enabled}"

def next (mode : Nat) (states : List State) : List State :=
  (states.flatMap fun s => (events.filter (permitted mode s)).map
    (ReconfigurableRoutes.advance s)).eraseDups

def testFrontiers (label : String) (mode : Nat) (start : State) (horizons : Nat) : IO Unit := do
  let mut states := [start]
  for n in List.range horizons do
    for s in states do
      IO.println (stateLine s!"{label}:{n}" mode s)
    states := next mode states

end ReconfigurationSamples
open ReconfigurationSamples

def main : IO Unit := do
  for raw in List.range 10 do
    for work in List.range 7 do
      for mode in List.range 3 do
        testFrontiers s!"budget:{raw}:{work}:{mode}" mode (initial raw work) (work+3)
  for rw in [(12,7), (12,8)] do
    for mode in List.range 3 do
      testFrontiers s!"threshold:{rw.1}:{rw.2}:{mode}" mode (initial rw.1 rw.2) (rw.2+3)
  for raw in [2,3,5] do
    for work in List.range 5 do
      for bar in [Bar.span .left .right, .loose, .span .left .left, .span .right .left] do
        for mode in List.range 3 do
          let start : State := ⟨none, raw, work, 3, bar, none, [rightForm,leftForm]⟩
          testFrontiers s!"retained:{raw}:{work}:{barWord bar}:{mode}" mode start (work+2)
  for pending in [dyadAB,dyadBC,ReconfigurableRoutes.dyadAC] do
    for mode in List.range 3 do
      let start : State := ⟨none, 2, 3, 4, .span .left .right, some pending, [leftForm]⟩
      testFrontiers s!"partial:{treeWord pending}:{mode}" mode start 5
