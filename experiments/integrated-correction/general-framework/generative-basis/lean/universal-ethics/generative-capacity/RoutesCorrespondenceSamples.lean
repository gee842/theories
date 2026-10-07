import FormationRoutes

/-! Finite executable correspondence samples, not additional proof claims. -/
open FormationRoutes

def roleWord : Role → String
  | .a => "a"
  | .b => "b"
  | .c => "c"

def treeWord : Tree → String
  | .atom r => roleWord r
  | .join l r => "(" ++ treeWord l ++ treeWord r ++ ")"

def portWord : Port → String
  | .left => "L"
  | .right => "R"

def barWord : Bar → String
  | .absent => "N"
  | .loose => "U"
  | .span p q => portWord p ++ portWord q

def bit (b : Bool) : String := if b then "1" else "0"

def events : List Event := [.receive, .attach, .repair, .startAB, .startBC,
  .finishLeft, .finishRight, .syncLeft, .syncRight]

def permitted (bypass : Bool) (s : State) (e : Event) : Bool :=
  decide (Enabled s e) && (!bypass || !(e == .syncLeft || e == .syncRight))

def stateLine (label : String) (bypass : Bool) (s : State) : String :=
  let source := match s.source with
    | none => "N"
    | some lot => s!"{lot.raw},{lot.work}"
  let pending := match s.pending with
    | none => "N"
    | some t => treeWord t
  let products := String.intercalate "," (s.products.map treeWord)
  let enabled := String.join (events.map (fun e => bit (permitted bypass s e)))
  s!"{label};{source};{s.raw};{s.work};{s.spent};{barWord s.bar};{pending};{products};{enabled}"

def frontier (bypass : Bool) (start : State) : Nat → List State
  | 0 => [start]
  | n + 1 => ((frontier bypass start n).flatMap fun s =>
      (events.filter (permitted bypass s)).map (advance s)).eraseDups

def testFrontiers (label : String) (bypass : Bool) (start : State) (horizons : Nat) : IO Unit := do
  for n in List.range horizons do
    for s in frontier bypass start n do
      IO.println (stateLine s!"{label}:{n}" bypass s)

def main : IO Unit := do
  for raw in List.range 9 do
    for work in List.range 6 do
      for bypass in [false, true] do
        testFrontiers s!"budget:{raw}:{work}:{bit bypass}" bypass (initial raw work) (work + 3)
  -- A prior left product and its spent work remain in all ablation states.
  for work in List.range 4 do
    for bar in [Bar.span .left .right, .loose, .span .left .left, .span .right .left] do
      let start : State := ⟨none, 3, work, 2, bar, none, [leftForm]⟩
      testFrontiers s!"intervention:{work}:{barWord bar}" false start (work + 2)
