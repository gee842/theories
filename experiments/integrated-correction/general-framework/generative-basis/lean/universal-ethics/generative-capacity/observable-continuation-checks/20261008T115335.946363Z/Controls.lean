import ObservableContinuation
open ObservableContinuation

-- Paying for a reading with the only unit leaves no unit for the response.
example : AlignmentInquiry.run (interface extension) inspect (initial 1 false) = none := by rfl

-- Instantiate the generic bridge with independently checked actual support.
example : ChanceAdequacy.mass [false, true] (fun _ => 1)
      (ChanceAdequacy.target (fun _ => true) oldWorks) ≤
    ChanceAdequacy.mass [false, true] (fun _ => 1) (support inspect 2) := by
  have joined := selected_execution_gives_continuation_bound
    [false, true] (fun _ => 1) (fun _ => true) oldWorks (support inspect 2)
    (initial 2) (interface extension) (states 2) singlePlans inspect
    funded_observation_realizes_extension.1
    (by intro mode _; cases mode <;> simp [states])
    (by
      intro mode _ _ final _ _
      have actual := (funded_observation_realizes_extension.2.1 mode).2
      simp [support, actual])
    (by decide)
  exact joined.2.2.1
