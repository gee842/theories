import NondualFormation
open NondualCore.Signals

def probeEdges : List (Nat × Nat) :=
  [(0,3),(1,3),(1,4),(2,4),(3,4),(3,3),(4,4)]
def picked (mask bit : Nat) : Bool := (mask / (2 ^ bit)) % 2 == 1
def probeNet (graph activity : Nat) : Net :=
  { edges := ((List.range 7).filter (picked graph)).map (fun i => probeEdges[i]!)
    active := (List.range 5).filter (picked activity) }
def bit (b : Bool) : String := if b then "1" else "0"
def encoded (s : Net) : String :=
  String.intercalate "," (s.edges.map (fun e => toString e.1 ++ ":" ++ toString e.2))
    ++ "|" ++ String.intercalate "," (s.active.map toString)
#eval IO.println ("matrix=" ++ String.intercalate "" ((List.range 128).flatMap
  (fun graph => (List.range 32).flatMap (fun activity =>
    [bit (canPulse (probeNet graph activity) 3), bit (canPulse (probeNet graph activity) 4)]))))
#eval IO.println ("origin=" ++ encoded origin)
#eval IO.println ("formed=" ++ encoded formed)
#eval IO.println ("responded=" ++ encoded responded)
#eval IO.println ("dissolved=" ++ encoded dissolved)
#eval IO.println ("rewired=" ++ encoded rewired)
#eval IO.println ("reresponded=" ++ encoded reresponded)
#eval IO.println ("duplicate=" ++ bit (canPulse ⟨[(0,3),(0,3)], [0]⟩ 3))
#eval IO.println ("self_plus_one=" ++ bit (canPulse ⟨[(3,3),(0,3)], [0,3]⟩ 3))
#eval IO.println ("duplicate_plus_other=" ++ bit (canPulse ⟨[(0,3),(0,3),(1,3)], [0,1]⟩ 3))
