import FormativeCapacity

/-! Executable samples for independent graph correspondence, not new theorems. -/
open FormativeCapacity

def treeWord : Tree → String
  | .atom => "A"
  | .socket => "S"
  | .branch l r => "(" ++ treeWord l ++ treeWord r ++ ")"

def bit (b : Bool) : String := if b then "1" else "0"

def stateLine (feed : Feed) (label : String) (s : State) : String :=
  let events := [Event.capture, .commissionClosed, .commissionOpen, .build]
  let enabled := String.join (events.map (fun e => bit (decide (Enabled feed s e))))
  s!"{label};{treeWord s.tree};{s.raw};{s.work};{s.cursor};{bit (s.phase == .building)};{enabled}"

def frontier (feed : Feed) : Nat → List State
  | 0 => [initial]
  | n + 1 => ((frontier feed n).flatMap (children feed)).eraseDups

def checkedRun (feed : Feed) : State → List Event → Option State
  | s, [] => some s
  | s, e :: es => if decide (Enabled feed s e) then checkedRun feed (advance s e) es else none

def main : IO Unit := do
  for mode in List.range 6 do
    let feed := if mode == 5 then constantFeed else finiteFeed mode
    for horizon in List.range 9 do
      for s in frontier feed horizon do
        IO.println (stateLine feed s!"frontier:{mode}:{horizon}" s)
  for n in List.range 13 do
    let word := List.replicate (n+1) Event.capture ++
      [.commissionClosed] ++ List.replicate n .build
    match checkedRun constantFeed initial word with
    | some s => IO.println (stateLine constantFeed s!"batch:{n}" s)
    | none => throw (IO.userError "batch witness disabled")
  for n in List.range 65 do
    let word := [Event.capture, .commissionOpen] ++
      (List.replicate n [Event.capture, .build]).flatten
    match checkedRun constantFeed initial word with
    | some s => IO.println (stateLine constantFeed s!"renew:{n}" s)
    | none => throw (IO.userError "renewal witness disabled")
