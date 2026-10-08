import AcquiredCorrection
namespace AcquiredCorrectionCases
open AcquiredCorrection

def trees : Nat → List Tree
  | 0 => [.closed,.endpoint false,.endpoint true]
  | n+1 => [.closed,.endpoint false,.endpoint true] ++
      (trees n).flatMap (fun l => (trees n).map (fun r => .fork l r))

def flip : Tree → Tree
  | .closed => .closed
  | .endpoint k => .endpoint (!k)
  | .fork l r => .fork (flip l) (flip r)

def addressCode (xs : Address) : Nat := xs.foldl (fun a b => 2*a + if b then 1 else 0) 1

def report (s : Scan) : List Nat :=
  match s.verdict with
  | .pending => [0,0,0,s.spent]
  | .exhausted => [1,0,0,s.spent]
  | .found (path,key) => [2,addressCode path,if key then 1 else 0,s.spent]

def row (xs : List Nat) : IO Unit := IO.println (String.intercalate "," (xs.map toString))

def profiles : List (Nat × Nat) := [(0,0),(4,20),(20,4),(8,8),(10,10),(20,20)]

def main : IO Unit := do
  for (root,i) in (trees 2).zipIdx do
    for fuel in List.range 10 do
      row ([0,i,fuel] ++ report (discover fuel root))
    for command in List.range 3 do
      let cmd : EffectiveCommand.Command := if command == 0 then .update else if command == 1 then .replace else .shutdown
      for ((reserve,deadline),j) in profiles.zipIdx do
        for mutation in List.range 3 do
          let current := if mutation == 0 then root else if mutation == 1 then flip root else .closed
          for auth in List.range 3 do
            let start := EffectiveCommand.start false cmd reserve deadline
            match acquire 7 root start with
            | none => row ([1,i,command,j,mutation,auth,0] ++ [0,1,0,reserve,0,0,0,0])
            | some (scan,paid) =>
              let now := if auth == 0 then paid else if auth == 1 then {paid with authority := 8} else {paid with signed := false}
              let out := match scan.verdict with
                | .found ticket => dispatch current ticket now
                | _ => Delivery.mk now false
              let s := out.state
              row ([1,i,command,j,mutation,auth,1] ++
                [if out.succeeded then 1 else 0,if s.running then 1 else 0,
                if s.completed then 1 else 0,s.reserve,s.spent,s.time,s.version,s.generation])
end AcquiredCorrectionCases
