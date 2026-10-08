import ChanceAdequacy
open ChanceAdequacy

-- Event-level repair example; not a theorem asserting physical feasibility.
example : mass [false, true] (fun _ => 1)
    (repair (fun _ => true) Bool.not (fun h => h)) = 2 := by rfl

-- The general algebra admits an empty domain; it is not a probability law.
example : total ([] : List Bool) (fun _ => 1) = 0 := by rfl
