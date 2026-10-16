import CorrectionBoundary

/- Parent and children are descriptions of joint operation. A parent label
confers neither independence nor ethical authority. Exact reduced dynamics and
history composition are credited to the existing SystemsOrganization module;
these examples test correction interventions and joint command feasibility. -/
namespace CorrectionParent

structure Children where
  leftStopped : Bool
  rightStopped : Bool
  deriving DecidableEq, Repr

def parentStopped (s : Children) : Bool := s.leftStopped && s.rightStopped

def stopBoth (_ : Children) : Children := ⟨true,true⟩

def stopLeft (s : Children) : Children := { s with leftStopped := true }

theorem parent_summary_exact_for_stop_both (s : Children) :
    parentStopped (stopBoth s) = true := rfl

theorem same_parent_summary_different_local_effect :
    parentStopped ⟨false,false⟩ = parentStopped ⟨false,true⟩ ∧
    parentStopped (stopLeft ⟨false,false⟩) ≠ parentStopped (stopLeft ⟨false,true⟩) := by decide

theorem no_parent_only_law_for_local_stop :
    ¬ ∃ next : Bool → Bool, ∀ s, parentStopped (stopLeft s) = next (parentStopped s) := by
  rintro ⟨next,h⟩
  have h0 := h ⟨false,false⟩
  have h1 := h ⟨false,true⟩
  have bad : false = true := h0.trans h1.symm
  exact Bool.noConfusion bad

theorem retaining_sibling_context_suffices (s : Children) :
    parentStopped (stopLeft s) = s.rightStopped := by simp [parentStopped,stopLeft]

theorem parent_stopped_iff_children (s : Children) :
    parentStopped s = true ↔ s.leftStopped = true ∧ s.rightStopped = true := by
  cases s with | mk a b => cases a <;> cases b <;> decide

theorem child_can_stop_without_parent :
    (Children.mk true false).leftStopped = true ∧ parentStopped ⟨true,false⟩ = false := by decide

-- Differing child decoders are individually correctable but not by one shared
-- bit. A vector interface restores joint feasibility.
def decode (p command : Bool) : Bool := xor command p

theorem each_child_correctable (p : Bool) : ∃ command, decode p command = true := by
  exact ⟨!p,by cases p <;> rfl⟩

theorem one_broadcast_cannot_correct_both :
    ¬ ∃ command, decode false command = true ∧ decode true command = true := by
  rintro ⟨c,h⟩
  exact CorrectionBoundary.opposite_decoders_conflict c true h

theorem separate_commands_correct_both (left right : Bool) :
    decode left (!left) = true ∧ decode right (!right) = true := by
  cases left <;> cases right <;> decide

-- Generic composition needs joint feasibility and an actual outcome bridge.
-- Componentwise existence alone is intentionally not used as that bridge.
theorem joint_correction_from_feasible_commands {I A : Type}
    (available : (I → A) → Prop) (childCorrect : I → A → Prop)
    (parentCorrect : (I → A) → Prop)
    (bridge : ∀ commands, available commands → (∀ i, childCorrect i (commands i)) → parentCorrect commands)
    (joint : ∃ commands, available commands ∧ ∀ i, childCorrect i (commands i)) :
    ∃ commands, available commands ∧ parentCorrect commands := by
  rcases joint with ⟨commands,ha,hc⟩
  exact ⟨commands,ha,bridge commands ha hc⟩

-- Shared support is included in the parent, even when each local controller's
-- translation is correct. It is not inferred from local command acceptance.
def actualDelivery (power p command : Bool) : Option Bool :=
  if power then some (decode p command) else none

theorem shared_power_loss_blocks_correct_children (p : Bool) :
    decode p (!p) = true ∧ actualDelivery false p (!p) = none := by
  cases p <;> decide

theorem parent_support_restores_delivery (p : Bool) :
    actualDelivery true p (!p) = some true := by cases p <;> rfl

-- The full pair is an exact operational parent representation in these laws;
-- conjunction is only a status summary. Neither fact identifies one unique
-- physical or moral boundary for every purpose.
end CorrectionParent
