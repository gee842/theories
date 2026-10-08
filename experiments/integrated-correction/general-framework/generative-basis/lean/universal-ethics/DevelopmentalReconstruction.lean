import DevelopmentalAssociation

/-!
# Reconstruction through actual sampled descendants

Extends the existing mutable local-division model with an accounted single-cell
transfer. A sample carries its actual developmental state; old bonds are removed
by the declared bottleneck, and subsequent division rebuilds bonds from the
carried state. Material and activity support come from explicit finite reserves.

The transfer requirement, local division law, occurrence of mutation, chosen
cell and supply amounts are supplied experimental/model conditions. The module
does not derive molecular rates, collective natural reproduction, indefinite
renewal, evolutionary stability, or empirical superiority.
-/

namespace DevelopmentalReconstruction

abbrev Culture := DevelopmentalAssociation.State

structure World where
  culture : Culture
  materialReserve : Nat
  supportReserve : Nat
  removedMaterial : Nat
  removedSupport : Nat

def material (w : World) : Nat :=
  w.culture.count + w.culture.precursor + w.materialReserve + w.removedMaterial

def support (w : World) : Nat :=
  w.culture.available + w.culture.spent + w.supportReserve + w.removedSupport

inductive Requirement where
  | anyCell
  | attachedCell
  deriving DecidableEq, Repr

def attached (s : Culture) (p : Nat) : Bool :=
  s.bonds.any (fun edge => edge.1 == p || edge.2 == p)

def eligible (s : Culture) (r : Requirement) (p : Nat) : Bool :=
  decide (p < s.count) && match r with
    | .anyCell => true
    | .attachedCell => attached s p

/-- One actual cell is moved. Every other cell and unused culture stock is
recorded as removed; the new material/support comes from the named reserves.
The selected cell's state is copied into the coordinate convention of position
zero, not chosen again by the investigator for the next generation. -/
def transfer (w : World) (r : Requirement) (p supply work : Nat) : Option World :=
  if eligible w.culture r p = true ∧ p < w.culture.count ∧
      supply ≤ w.materialReserve ∧ work ≤ w.supportReserve then
    some {
      culture := ⟨1, supply, work, 0,
        fun _ => w.culture.retains p, fun _ => w.culture.founder p, []⟩
      materialReserve := w.materialReserve - supply
      supportReserve := w.supportReserve - work
      removedMaterial := w.removedMaterial + (w.culture.count - 1) + w.culture.precursor
      removedSupport := w.removedSupport + w.culture.available + w.culture.spent }
  else none

def develop (w : World) (word : List DevelopmentalAssociation.Event) : Option World :=
  (DevelopmentalAssociation.run word w.culture).map (fun s => { w with culture := s })

theorem transfer_accounts {w t : World} {r : Requirement} {p supply work : Nat}
    (actual : transfer w r p supply work = some t) :
    material t = material w ∧ support t = support w := by
  unfold transfer at actual
  split at actual
  · rename_i enabled
    cases Option.some.inj actual
    dsimp [material, support]
    omega
  · cases actual

theorem transfer_carries_development {w t : World} {r : Requirement} {p supply work : Nat}
    (actual : transfer w r p supply work = some t) :
    t.culture.count = 1 ∧ t.culture.bonds = [] ∧
    t.culture.retains 0 = w.culture.retains p ∧
    t.culture.founder 0 = w.culture.founder p ∧
    t.culture.precursor = supply ∧ t.culture.available = work := by
  unfold transfer at actual
  split at actual
  · cases Option.some.inj actual
    simp
  · cases actual

/-- Existing bond structure is not transferred; its redevelopment follows
from the selected cell's operative state and actual subsequent division. -/
theorem sampled_state_rebuilds_bonds {w t : World} {r : Requirement} {p supply work : Nat}
    {daughter : Culture}
    (sample : transfer w r p supply work = some t)
    (division : DevelopmentalAssociation.divide t.culture 0 = some daughter) :
    daughter.count = 2 ∧
    daughter.retains 1 = w.culture.retains p ∧
    daughter.founder 1 = w.culture.founder p ∧
    daughter.bonds = (if w.culture.retains p then [(0, 1)] else []) := by
  obtain ⟨count, bonds, retained, founder, _, _⟩ := transfer_carries_development sample
  obtain ⟨n, inherited, origin, graph⟩ := DevelopmentalAssociation.division_inherits division
  rw [count] at n inherited origin graph
  rw [retained] at inherited graph
  rw [founder] at origin
  rw [bonds] at graph
  exact ⟨n, inherited, origin, graph⟩

theorem development_accounts {w t : World} {word : List DevelopmentalAssociation.Event}
    (actual : develop w word = some t) :
    material t = material w ∧ support t = support w ∧
    t.culture.available + word.length = w.culture.available := by
  unfold develop at actual
  cases h : DevelopmentalAssociation.run word w.culture with
  | none => simp [h] at actual
  | some s =>
    simp only [h, Option.map_some, Option.some.injEq] at actual
    cases actual
    obtain ⟨mat, sup, count⟩ := DevelopmentalAssociation.core_trace_accounts
      ((DevelopmentalAssociation.run_iff_core_trace _ _ _).mp h)
    dsimp [DevelopmentalAssociation.material] at mat
    dsimp [material, support]
    omega

inductive Event where
  | develop (word : List DevelopmentalAssociation.Event)
  | transfer (requirement : Requirement) (cell supply work : Nat)

def step : Event → World → Option World
  | .develop word, w => develop w word
  | .transfer requirement cell supply work, w => transfer w requirement cell supply work

def run : List Event → World → Option World
  | [], w => some w
  | e :: es, w => (step e w).bind (run es)

def process : Generative.Process World Event where
  step w e t := step e w = some t

theorem run_iff_core_trace (word : List Event) (w t : World) :
    run word w = some t ↔ Generative.Trace process w word t := by
  induction word generalizing w with
  | nil => simp [run, Generative.trace_nil_iff]
  | cons e es ih =>
    rw [Generative.trace_cons_iff]
    change ((step e w).bind (run es) = some t) ↔
      ∃ middle, step e w = some middle ∧ Generative.Trace process middle es t
    cases h : step e w with
    | none => simp
    | some middle => simpa using ih middle

theorem step_accounts {w t : World} {e : Event} (actual : step e w = some t) :
    material t = material w ∧ support t = support w := by
  cases e with
  | develop word => exact (development_accounts actual).1 |> fun mat =>
      ⟨mat, (development_accounts actual).2.1⟩
  | transfer r p supply work => exact transfer_accounts actual

theorem history_accounts (events : List Event) {w t : World}
    (actual : run events w = some t) :
    material t = material w ∧ support t = support w := by
  induction events generalizing w with
  | nil => cases Option.some.inj actual; exact ⟨rfl, rfl⟩
  | cons e es ih =>
    simp only [run] at actual
    cases h : step e w with
    | none => simp [h] at actual
    | some middle =>
      simp only [h, Option.bind_some] at actual
      obtain ⟨m1, s1⟩ := step_accounts h
      obtain ⟨m2, s2⟩ := ih actual
      exact ⟨m2.trans m1, s2.trans s1⟩

/-- Excludes already expended/removed support. A transfer does not create it. -/
def remainingSupport (w : World) : Nat := w.culture.available + w.supportReserve

def workCost : Event → Nat
  | .develop word => word.length
  | .transfer _ _ _ _ => 0

def historyCost (events : List Event) : Nat := (events.map workCost).sum

theorem step_support_bound {w t : World} {e : Event} (actual : step e w = some t) :
    remainingSupport t + workCost e ≤ remainingSupport w := by
  cases e with
  | develop word =>
    obtain ⟨_, _, consumed⟩ := development_accounts actual
    change develop w word = some t at actual
    unfold develop at actual
    cases h : DevelopmentalAssociation.run word w.culture with
    | none => simp [h] at actual
    | some s =>
      simp only [h, Option.map_some, Option.some.injEq] at actual
      cases actual
      dsimp [remainingSupport, workCost] at *
      omega
  | transfer r p supply work =>
    change transfer w r p supply work = some t at actual
    unfold transfer at actual
    split at actual
    · rename_i enabled
      cases Option.some.inj actual
      dsimp [remainingSupport, workCost]
      omega
    · cases actual

theorem history_support_bound (events : List Event) {w t : World}
    (actual : run events w = some t) :
    remainingSupport t + historyCost events ≤ remainingSupport w := by
  induction events generalizing w with
  | nil => cases Option.some.inj actual; simp [historyCost]
  | cons e es ih =>
    simp only [run] at actual
    cases h : step e w with
    | none => simp [h] at actual
    | some middle =>
      simp only [h, Option.bind_some] at actual
      have first := step_support_bound h
      have rest := ih actual
      simp only [historyCost, List.map_cons, List.sum_cons] at *
      omega

/-- A homogeneous developmental state, not genetic identity or common interest. -/
def Retention (s : Culture) (value : Bool) : Prop :=
  ∀ i, i < s.count → s.retains i = value

def NoRevision : DevelopmentalAssociation.Event → Prop
  | .changeRetention _ _ => False
  | _ => True

theorem local_step_preserves_retention {s t : Culture}
    {e : DevelopmentalAssociation.Event} {value : Bool}
    (unchanged : NoRevision e) (carried : Retention s value)
    (actual : DevelopmentalAssociation.step e s = some t) : Retention t value := by
  cases e with
  | divide parent =>
    change DevelopmentalAssociation.divide s parent = some t at actual
    unfold DevelopmentalAssociation.divide at actual
    split at actual
    · rename_i enabled
      cases Option.some.inj actual
      intro i hi
      dsimp at hi ⊢
      split
      · exact carried parent enabled.1
      · exact carried i (by omega)
    · cases actual
  | changeRetention cell value => cases unchanged
  | detach parent child =>
    change DevelopmentalAssociation.detach s parent child = some t at actual
    unfold DevelopmentalAssociation.detach at actual
    split at actual
    · cases Option.some.inj actual; exact carried
    · cases actual
  | aggregate a b =>
    change DevelopmentalAssociation.aggregate s a b = some t at actual
    unfold DevelopmentalAssociation.aggregate at actual
    split at actual
    · cases Option.some.inj actual; exact carried
    · cases actual

theorem local_history_preserves_retention (word : List DevelopmentalAssociation.Event)
    {s t : Culture} {value : Bool}
    (unchanged : ∀ e ∈ word, NoRevision e) (carried : Retention s value)
    (actual : DevelopmentalAssociation.run word s = some t) : Retention t value := by
  induction word generalizing s with
  | nil => cases Option.some.inj actual; exact carried
  | cons e es ih =>
    simp only [DevelopmentalAssociation.run] at actual
    cases h : DevelopmentalAssociation.step e s with
    | none => simp [h] at actual
    | some middle =>
      simp only [h, Option.bind_some] at actual
      exact ih (fun a ha => unchanged a (List.mem_cons_of_mem e ha))
        (local_step_preserves_retention (unchanged e (by simp)) carried h) actual

def PreservesDevelopment : Event → Prop
  | .develop word => ∀ e ∈ word, NoRevision e
  | .transfer _ _ _ _ => True

theorem world_step_preserves_retention {w t : World} {e : Event} {value : Bool}
    (unchanged : PreservesDevelopment e) (carried : Retention w.culture value)
    (actual : step e w = some t) : Retention t.culture value := by
  cases e with
  | develop word =>
    change develop w word = some t at actual
    unfold develop at actual
    cases h : DevelopmentalAssociation.run word w.culture with
    | none => simp [h] at actual
    | some s =>
      simp only [h, Option.map_some, Option.some.injEq] at actual
      cases actual
      exact local_history_preserves_retention word unchanged carried h
  | transfer r p supply work =>
    change transfer w r p supply work = some t at actual
    unfold transfer at actual
    split at actual
    · rename_i enabled
      cases Option.some.inj actual
      intro i _
      exact carried p enabled.2.1
    · cases actual

/-- Arbitrary finite supported development/transfer histories preserve the
acquired state until an operative revision occurs. Persistence has hypotheses. -/
theorem inherited_development_over_generations (events : List Event)
    {w t : World} {value : Bool}
    (unchanged : ∀ e ∈ events, PreservesDevelopment e)
    (carried : Retention w.culture value) (actual : run events w = some t) :
    Retention t.culture value := by
  induction events generalizing w with
  | nil => cases Option.some.inj actual; exact carried
  | cons e es ih =>
    simp only [run] at actual
    cases h : step e w with
    | none => simp [h] at actual
    | some middle =>
      simp only [h, Option.bind_some] at actual
      exact ih (fun a ha => unchanged a (List.mem_cons_of_mem e ha))
        (world_step_preserves_retention (unchanged e (by simp)) carried h) actual

def initial : World := ⟨DevelopmentalAssociation.seed 1, 20, 30, 0, 0⟩

def acquired : World :=
  (develop initial [.changeRetention 0 true, .divide 0]).getD initial

def ordinary : World := (develop initial [.divide 0]).getD initial

theorem acquired_developmental_state : Retention acquired.culture true := by
  intro i hi
  dsimp [acquired, develop, initial, DevelopmentalAssociation.seed,
    DevelopmentalAssociation.run, DevelopmentalAssociation.step,
    DevelopmentalAssociation.changeRetention, DevelopmentalAssociation.divide] at hi ⊢
  split <;> simp_all <;> omega

def cycle (r : Requirement) : List Event :=
  [.transfer r 1 2 3, .develop [.divide 0]]

def observation (w : World) :=
  (DevelopmentalAssociation.observe w.culture,
    w.materialReserve, w.supportReserve, w.removedMaterial, w.removedSupport)

/-- Mutation occurs once. Every later construction uses the selected cell's
inherited retention, with fresh support taken from the finite common account. -/
theorem formed_inherited_reconstruction_history :
    (run ([.develop [.changeRetention 0 true, .divide 0]] ++
      cycle .attachedCell ++ cycle .attachedCell) initial).map observation =
    some ((2, 1, 2, 1, [true, true], [0, 0], [(0, 1)]), 16, 24, 12, 23) := by
  rfl

theorem formation_changes_sampling_under_same_requirement :
    acquired.culture.count = ordinary.culture.count ∧
    (transfer acquired .attachedCell 1 2 3).isSome = true ∧
    (transfer ordinary .attachedCell 1 2 3).isSome = false := by
  decide +kernel

/-- Removing the original attached-cell sampling requirement does not erase
the inherited developmental state. This is persistence, not invasion stability. -/
theorem relaxed_requirement_preserves_reconstruction :
    (run (cycle .anyCell) acquired).map observation =
    some ((2, 1, 2, 1, [true, true], [0, 0], [(0, 1)]), 18, 27, 10, 20) := by
  rfl

/-- An admitted inherited revision really changes subsequent development;
no lifetime identity between acquired form and all descendants is assumed. -/
theorem revised_descendant_changes_next_sampling :
    ((run [.transfer .attachedCell 1 2 3,
      .develop [.changeRetention 0 false, .divide 0]] acquired).map
        (fun w => (w.culture.count, w.culture.bonds,
          (transfer w .attachedCell 1 2 3).isSome,
          (transfer w .anyCell 1 2 3).isSome))) =
    some (2, [], false, true) := by
  decide +kernel

theorem inherited_capacity_still_needs_actual_support :
    (transfer { acquired with materialReserve := 0 } .attachedCell 1 2 3).isSome = false ∧
    (transfer { acquired with supportReserve := 0 } .attachedCell 1 2 3).isSome = false ∧
    (transfer acquired .attachedCell 2 2 3).isSome = false := by
  decide +kernel

/-- Count alone cannot predict this specified response even in two histories
from the same seed. This does not defeat conventional bond-aware models. -/
theorem count_only_sampling_is_inadequate :
    ¬ ∃ predict : Nat → Bool,
      predict acquired.culture.count = (transfer acquired .attachedCell 1 2 3).isSome ∧
      predict ordinary.culture.count = (transfer ordinary .attachedCell 1 2 3).isSome := by
  rintro ⟨predict, left, right⟩
  obtain ⟨same, yes, no⟩ := formation_changes_sampling_under_same_requirement
  rw [same] at left
  have h := left.symm.trans right
  rw [yes, no] at h
  cases h

end DevelopmentalReconstruction
