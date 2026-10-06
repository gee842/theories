import NondualCore

namespace NondualCore
open Generative

namespace Signals

/- One carrier type, not separate actors/patients. Nodes and event laws remain
   supplied. Edges are formed; joint support is read from actual edges/activity.
   A pulse toggles its target and carries no ethical or experiential label. -/
structure Net where
  edges : List (Nat × Nat)
  active : List Nat
  deriving DecidableEq, Repr

inductive Event where
  | link (source target : Nat)
  | cut (source target : Nat)
  | pulse (target : Nat)
  deriving DecidableEq, Repr

def sources (s : Net) (target : Nat) : List Nat :=
  (s.edges.filter (fun e => e.2 == target && e.1 != target && s.active.contains e.1)).map Prod.fst

def Support (s : Net) (target source : Nat) : Prop := source ∈ sources s target
instance (s : Net) (target source : Nat) : Decidable (Support s target source) := by
  unfold Support
  infer_instance

def canPulse (s : Net) (target : Nat) : Bool :=
  (sources s target).any (fun a => (sources s target).any (fun b => a != b))

def allowed (s : Net) : Event → Bool
  | .link _ _ | .cut _ _ => true
  | .pulse target => canPulse s target

def advance (s : Net) : Event → Net
  | .link a b => {s with edges := s.edges ++ [(a,b)]}
  | .cut a b => {s with edges := s.edges.filter (fun e => e != (a,b))}
  | .pulse n => {s with active :=
      if s.active.contains n then s.active.filter (fun m => m != n) else n :: s.active}

def process : Process Net Event where
  step s e t := allowed s e = true ∧ t = advance s e

theorem support_iff_active_link (s : Net) (target source : Nat) :
    Support s target source ↔
      (source,target) ∈ s.edges ∧ source ≠ target ∧ source ∈ s.active := by
  simp only [Support,sources,List.mem_map,List.mem_filter]
  constructor
  · rintro ⟨⟨a,b⟩,⟨he,hguard⟩,ha⟩
    have h : (b = target ∧ a ≠ target) ∧ a ∈ s.active := by simpa using hguard
    change a = source at ha
    subst a
    rcases h with ⟨⟨rfl,hne⟩,hact⟩
    exact ⟨he,hne,hact⟩
  · rintro ⟨he,hne,ha⟩
    exact ⟨(source,target),⟨he,by simp [hne,ha]⟩,rfl⟩

theorem pulse_iff_distinct_supports (s : Net) (target : Nat) :
    canPulse s target = true ↔
      ∃ a, Support s target a ∧ ∃ b, Support s target b ∧ a ≠ b := by
  simp [canPulse,Support]

def run : Net → List Event → Net
  | s,[] => s
  | s,e::es => run (advance s e) es

def permitted : Net → List Event → Bool
  | _,[] => true
  | s,e::es => allowed s e && permitted (advance s e) es

theorem permitted_gives_actual_trace (s : Net) (es : List Event)
    (h : permitted s es = true) : Trace process s es (run s es) := by
  induction es generalizing s with
  | nil => exact .nil s
  | cons e es ih =>
    have hh : allowed s e = true ∧ permitted (advance s e) es = true := by simpa [permitted] using h
    exact .cons ⟨hh.1,rfl⟩ (ih _ hh.2)

def origin : Net := ⟨[],[0,1,2]⟩
def formation : List Event := [.link 0 3,.link 1 3,.link 1 4,.link 2 4]
def formed : Net := run origin formation
def response : List Event := [.pulse 3,.pulse 4]
def responded : Net := run formed response
def dissolution : List Event := [.cut 0 3,.cut 1 3,.cut 1 4,.cut 2 4]
def dissolved : Net := run responded dissolution

theorem formation_is_actual : Trace process origin formation formed :=
  permitted_gives_actual_trace _ _ (by decide)

theorem both_responses_are_actual : Trace process formed response responded :=
  permitted_gives_actual_trace _ _ (by decide)

theorem dissolution_is_actual : Trace process responded dissolution dissolved :=
  permitted_gives_actual_trace _ _ (by decide)

theorem composed_formation_response_dissolution :
    Trace process origin (formation ++ response ++ dissolution) dissolved := by
  exact trace_append_iff.mpr ⟨responded,
    trace_append_iff.mpr ⟨formed,formation_is_actual,both_responses_are_actual⟩,
    dissolution_is_actual⟩

theorem distinct_derived_supports_overlap :
    sources formed 3 = [0,1] ∧ sources formed 4 = [1,2] ∧
      Support formed 3 1 ∧ Support formed 4 1 ∧
      ¬ Support formed 3 2 ∧ ¬ Support formed 4 0 := by decide

theorem no_capacity_at_origin : canPulse origin 3 = false ∧ canPulse origin 4 = false := by decide

theorem repeated_same_source_does_not_make_joint_support :
    canPulse ⟨[(0,3),(0,3)], [0]⟩ 3 = false := by decide

theorem each_formed_support_link_is_needed :
    canPulse (advance formed (.cut 0 3)) 3 = false ∧
    canPulse (advance formed (.cut 1 3)) 3 = false ∧
    canPulse (advance formed (.cut 1 4)) 4 = false ∧
    canPulse (advance formed (.cut 2 4)) 4 = false := by decide

theorem response_has_actual_effects :
    ¬ 3 ∈ formed.active ∧ ¬ 4 ∈ formed.active ∧
      3 ∈ responded.active ∧ 4 ∈ responded.active := by decide

theorem dissolution_changes_capacity_preserving_activity :
    responded.active = dissolved.active ∧
      canPulse responded 3 = true ∧ canPulse responded 4 = true ∧
      canPulse dissolved 3 = false ∧ canPulse dissolved 4 = false := by decide

theorem no_activity_only_capacity_report :
    ¬ ∃ read : List Nat → Nat → Prop,
      ∀ s n, read s.active n ↔ canPulse s n = true := by
  rintro ⟨read,hexact⟩
  have hp := (hexact responded 3).mpr (by decide)
  have hs : responded.active = dissolved.active := by decide
  have hn := (hexact dissolved 3).mp (hs ▸ hp)
  have hf : canPulse dissolved 3 = false := by decide
  rw [hf] at hn
  cases hn

/- A formerly affected node becomes an effective source after new coupling.
   This branch starts from the actual responded state, before dissolution. -/
def rewiring : List Event := [.link 3 4,.cut 2 4]
def rewired : Net := run responded rewiring
def reresponded : Net := advance rewired (.pulse 4)

theorem rewiring_and_role_change_are_actual :
    Trace process responded (rewiring ++ [.pulse 4]) reresponded :=
  permitted_gives_actual_trace _ _ (by decide)

theorem affected_node_becomes_effective_contributor :
    ¬ Support formed 4 3 ∧ 3 ∈ responded.active ∧
      sources rewired 4 = [1,3] ∧ Support rewired 4 3 ∧
      canPulse rewired 4 = true ∧
      canPulse (advance rewired (.cut 3 4)) 4 = false ∧
      canPulse {rewired with active := rewired.active.filter (fun n => n != 3)} 4 = false ∧
      4 ∈ rewired.active ∧ ¬ 4 ∈ reresponded.active := by decide

end Signals
end NondualCore

#print axioms NondualCore.Signals.support_iff_active_link
#print axioms NondualCore.Signals.pulse_iff_distinct_supports
#print axioms NondualCore.Signals.permitted_gives_actual_trace
#print axioms NondualCore.Signals.formation_is_actual
#print axioms NondualCore.Signals.both_responses_are_actual
#print axioms NondualCore.Signals.dissolution_is_actual
#print axioms NondualCore.Signals.composed_formation_response_dissolution
#print axioms NondualCore.Signals.distinct_derived_supports_overlap
#print axioms NondualCore.Signals.no_capacity_at_origin
#print axioms NondualCore.Signals.repeated_same_source_does_not_make_joint_support
#print axioms NondualCore.Signals.each_formed_support_link_is_needed
#print axioms NondualCore.Signals.response_has_actual_effects
#print axioms NondualCore.Signals.dissolution_changes_capacity_preserving_activity
#print axioms NondualCore.Signals.no_activity_only_capacity_report
#print axioms NondualCore.Signals.rewiring_and_role_change_are_actual
#print axioms NondualCore.Signals.affected_node_becomes_effective_contributor
