import MaintenanceBaseline
open MaintenanceBaseline

-- Retirement actually disables the old dependent routes.
example : deliver .left (retire (initial 2 false)) = none ∧
    deliver .parallel (retire (initial 2 false)) = none := by
  exact ⟨rfl, rfl⟩

-- The independent right route remains executable where its physical mode works.
example : deliver .right (retire (initial 2 true)) =
    some ⟨⟨true, 1, true⟩, false, true⟩ := by rfl

-- Completed task records suffice even when the retired current target is empty.
example : ChanceAdequacy.Fulfilled [false, true] (fun _ => true)
    ObservableContinuation.oldWorks (actualDelivery .left 1) := by
  have joined := target_transport_with_completion_gives_bound [false, true]
    (fun _ => 1) (fun _ => true) ObservableContinuation.oldWorks
    (fun mode => !(actualDelivery .left 1 mode)) (fun _ => false)
    (actualDelivery .left 1) (actualDelivery .left 1)
    (by
      intro mode member needed
      exact Or.inl (completed_single_delivery_allows_retirement.2.1 mode member needed))
    (by intro mode member done; exact done)
    (by intro mode member needed; simp [ChanceAdequacy.target] at needed)
    (by decide)
  exact joined.1
