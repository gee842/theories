import SelectiveRevision

open Generative.SelectiveRevision

def boolText (b : Bool) : String := if b then "true" else "false"
def reportText : Option Bool → String
  | none => "none"
  | some b => boolText b
def groundText : Ground → String
  | .empty => "empty"
  | .supported => "supported"
  | .conflict => "conflict"
def choiceText : Choice → String
  | .check => "check"
  | .select => "select"
  | .decline => "decline"

def main : IO Unit := do
  IO.println "reversed,first_content,second_content,first_usable,second_usable,purpose,intervention,judgment,ground,choice,conventional_equal"
  let bits := [false, true]
  let reports := [none, some false, some true]
  let interventions : List (String × List Event) :=
    [("baseline", []), ("receive_first_false", [.receive false false]),
     ("receive_first_true", [.receive false true]),
     ("receive_second_false", [.receive true false]),
     ("receive_second_true", [.receive true true]),
     ("withdraw_first", [.withdraw false]), ("withdraw_second", [.withdraw true]),
     ("purpose_false", [.setPurpose false]), ("purpose_true", [.setPurpose true])]
  for r in bits do
    for a in reports do
      for b in reports do
        for u in bits do
          for v in bits do
            for g in bits do
              for (label, events) in interventions do
                let s := run events (prepared r a b u v g)
                let result := outcome s
                let equal := conventional s == result
                if !equal then throw (IO.userError "Implementation disagreement")
                IO.println (String.intercalate ","
                  [boolText r, reportText a, reportText b, boolText u, boolText v,
                   boolText g, label, reportText result.judgment,
                   groundText result.ground, choiceText result.choice, boolText equal])
