import GenerativeCore

/-!
# Organization, coupled histories and exact projection

The general theorems concern arbitrary deterministic action laws. They identify
when a state description closes under the actual law; they do not assume that
distinguishable components evolve independently. The relational trace bridge
reuses GenerativeCore rather than introducing a second history semantics.

The finite examples are conditional countermodels, not definitions or proofs of
emergence: unchanged local copy operations can give fixed or period-two joint
behavior under different wiring. Actual formation can change available events
inside one unchanged encompassing law. The formation recipe and finite costs
are supplied; no universal favorable direction, learning or ethics is derived.
-/

namespace SystemsOrganization

universe u v w z

variable {S : Type u} {Q : Type v} {R : Type w} {A : Type z}

def evolve (next : S → A → S) : S → List A → S
  | s, [] => s
  | s, a :: rest => evolve next (next s a) rest

def deterministic (next : S → A → S) : Generative.Process S A where
  step s a t := t = next s a

theorem deterministic_trace_iff (next : S → A → S) (s t : S) (word : List A) :
    Generative.Trace (deterministic next) s word t ↔ t = evolve next s word := by
  induction word generalizing s with
  | nil =>
      constructor
      · intro h
        exact (Generative.trace_nil_iff.mp h).symm
      · intro h
        exact Generative.trace_nil_iff.mpr h.symm
  | cons a rest ih =>
      constructor
      · intro h
        obtain ⟨m, hs, ht⟩ := Generative.trace_cons_iff.mp h
        have hm : m = next s a := hs
        subst m
        exact (ih (next s a)).mp ht
      · intro h
        exact .cons rfl ((ih (next s a)).mpr h)

def Commuting (next : S → A → S) (reduced : Q → A → Q) (p : S → Q) : Prop :=
  ∀ s a, p (next s a) = reduced (p s) a

theorem evolve_semiconjugacy {next : S → A → S} {reduced : Q → A → Q}
    {p : S → Q} (h : Commuting next reduced p) (s : S) (word : List A) :
    p (evolve next s word) = evolve reduced (p s) word := by
  induction word generalizing s with
  | nil => rfl
  | cons a rest ih =>
      exact (ih (next s a)).trans
        (congrArg (fun q => evolve reduced q rest) (h s a))

/-- All-word exactness is equivalent to actual one-step commutation, not to
the act of choosing a projection. This quantifies over every initial state. -/
theorem commuting_iff_all_words {next : S → A → S} {reduced : Q → A → Q}
    {p : S → Q} : Commuting next reduced p ↔
      ∀ s word, p (evolve next s word) = evolve reduced (p s) word := by
  constructor
  · exact evolve_semiconjugacy
  · intro h s a
    exact h s [a]

/-- The image endpoint is exact; distinct concrete endpoints need not be
recoverable from a many-to-one summary. -/
theorem projected_trace_exact {next : S → A → S} {reduced : Q → A → Q}
    {p : S → Q} (h : Commuting next reduced p) (s : S) (r : Q) (word : List A) :
    Generative.Trace (deterministic reduced) (p s) word r ↔
      ∃ t, Generative.Trace (deterministic next) s word t ∧ p t = r := by
  apply Generative.projected_trace_iff
  · intro before a after hs
    have heq : after = next before a := hs
    change p after = reduced (p before) a
    exact (congrArg p heq).trans (h before a)
  · intro before a after hs
    have heq : after = reduced (p before) a := hs
    exact ⟨next before a, rfl, (h before a).trans heq.symm⟩

def FibreConsistent (next : S → A → S) (p : S → Q) : Prop :=
  ∀ s t, p s = p t → ∀ a, p (next s a) = p (next t a)

/-- A supplied section is only a representative for each summary state.
Fibre consistency, not that representative choice, makes the reduced law exact.
No choice principle is needed because the section is explicit. -/
theorem reduced_law_exists_iff (next : S → A → S) (p : S → Q)
    (sectionMap : Q → S) (hsection : ∀ q, p (sectionMap q) = q) :
    (∃ reduced : Q → A → Q, Commuting next reduced p) ↔
      FibreConsistent next p := by
  constructor
  · rintro ⟨reduced, h⟩ s t heq a
    exact (h s a).trans ((congrArg (fun q => reduced q a) heq).trans (h t a).symm)
  · intro h
    refine ⟨fun q a => p (next (sectionMap q) a), ?_⟩
    intro s a
    exact h s (sectionMap (p s)) (hsection (p s)).symm a

theorem commuting_composes {next : S → A → S} {middle : Q → A → Q}
    {last : R → A → R} {p : S → Q} {q : Q → R}
    (hp : Commuting next middle p) (hq : Commuting middle last q) :
    Commuting next last (fun s => q (p s)) := by
  intro s a
  exact (congrArg q (hp s a)).trans (hq (p s) a)

def coupledNext (left : Q → R → A → Q) (right : Q → R → A → R)
    (state : Q × R) (a : A) : Q × R :=
  (left state.1 state.2 a, right state.1 state.2 a)

/-- Component updates may depend on both coordinates. Their joint description
preserves the same history when both equations hold for the actual law. -/
theorem coupled_components_preserve_history {next : S → A → S}
    (p : S → Q) (q : S → R) (left : Q → R → A → Q) (right : Q → R → A → R)
    (hp : ∀ s a, p (next s a) = left (p s) (q s) a)
    (hq : ∀ s a, q (next s a) = right (p s) (q s) a)
    (s : S) (word : List A) :
    (p (evolve next s word), q (evolve next s word)) =
      evolve (coupledNext left right) (p s, q s) word := by
  refine evolve_semiconjugacy (p := fun state => (p state, q state)) ?_ s word
  intro before a
  exact Prod.ext (hp before a) (hq before a)

/-! ## Same local rule, different coupling -/

def copyCell (input : Bool) : Bool := input

def routed (crossed : Bool) (state : Bool × Bool) (_ : Unit) : Bool × Bool :=
  if crossed then (copyCell state.2, copyCell state.1)
  else (copyCell state.1, copyCell state.2)

theorem self_routing_fixed (s : Bool × Bool) : routed false s () = s := by
  cases s
  rfl

theorem cross_routing_two_steps (s : Bool × Bool) :
    evolve (routed true) s [(), ()] = s := by
  cases s
  rfl

theorem cross_routing_not_fixed :
    routed true (true, false) () ≠ (true, false) := by
  decide

theorem same_cells_different_collective_recurrence :
    routed false (true, false) () = (true, false) ∧
    routed true (true, false) () ≠ (true, false) ∧
    evolve (routed true) (true, false) [(), ()] = (true, false) := by
  exact ⟨self_routing_fixed _, cross_routing_not_fixed, cross_routing_two_steps _⟩

/-- Dropping the other coordinate makes the next left value ambiguous even
though the complete two-coordinate deterministic law is perfectly defined. -/
theorem crossed_left_not_fibre_consistent :
    ¬ FibreConsistent (routed true) (fun s => s.1) := by
  intro h
  have wrong : false = true := h (false, false) (false, true) rfl ()
  exact Bool.noConfusion wrong

theorem no_autonomous_left_law :
    ¬ ∃ reduced : Bool → Unit → Bool,
      Commuting (routed true) reduced (fun s => s.1) := by
  intro h
  have consistent := (reduced_law_exists_iff (routed true) (fun s => s.1)
    (fun x => (x, false)) (fun _ => rfl)).mp h
  exact crossed_left_not_fibre_consistent consistent

/-! ## Stored arrangement formed inside an unchanged encompassing law -/

structure Device where
  left : Bool
  right : Bool
  linked : Bool
  spare : Bool
  fuel : Nat
  deriving DecidableEq, Repr

inductive Event where
  | assemble
  | exchange
  deriving DecidableEq, Repr

def assembled (s : Device) : Device :=
  { s with linked := true, spare := false, fuel := s.fuel - 1 }

def exchanged (s : Device) : Device :=
  { s with left := copyCell s.right, right := copyCell s.left }

def organization : Generative.Process Device Event where
  step s a t := match a with
    | .assemble => s.linked = false ∧ s.spare = true ∧ 0 < s.fuel ∧ t = assembled s
    | .exchange => s.linked = true ∧ t = exchanged s

def parts (s : Device) : Bool × Bool := (s.left, s.right)

def linkInventory (s : Device) : Nat :=
  (if s.linked then 1 else 0) + (if s.spare then 1 else 0)

/-- Assembly converts the declared spare into a link; exchange adds no part.
This is a finite symbolic inventory, not an identification of physical matter. -/
theorem link_inventory_preserved {s t : Device} {a : Event}
    (h : organization.step s a t) : linkInventory t = linkInventory s := by
  cases a with
  | assemble =>
      obtain ⟨hl, hs, _, rfl⟩ := h
      unfold linkInventory assembled
      rw [hl, hs]
      rfl
  | exchange =>
      obtain ⟨_, rfl⟩ := h
      rfl

/-- Exchange is deliberately cost-free in this structural example; only the
assembly bill is modeled. This is not a sustainability theorem. -/
theorem fuel_does_not_increase {s t : Device} {a : Event}
    (h : organization.step s a t) : t.fuel ≤ s.fuel := by
  cases a with
  | assemble =>
      obtain ⟨_, _, _, rfl⟩ := h
      exact Nat.sub_le _ _
  | exchange =>
      obtain ⟨_, rfl⟩ := h
      exact Nat.le_refl _

def raw : Device := ⟨true, false, false, true, 1⟩
def formed : Device := assembled raw
def exchangedOnce : Device := exchanged formed

theorem formation_step : organization.step raw .assemble formed := by
  exact ⟨rfl, rfl, by decide, rfl⟩

theorem formation_preserves_cell_values : parts raw = parts formed := by
  rfl

theorem formation_consumes_spare_and_fuel :
    raw.spare = true ∧ formed.spare = false ∧ raw.fuel = 1 ∧ formed.fuel = 0 := by
  decide

theorem exchange_unavailable_before_formation :
    ¬ Generative.Enabled organization raw .exchange := by
  rintro ⟨_, h, _⟩
  exact Bool.noConfusion h

theorem exchange_available_after_formation :
    Generative.Enabled organization formed .exchange := by
  exact ⟨exchangedOnce, rfl, rfl⟩

theorem formation_and_recurrence_same_history :
    Generative.Trace organization raw [.assemble, .exchange, .exchange] formed := by
  exact .cons formation_step
    (.cons (show organization.step formed .exchange exchangedOnce from ⟨rfl, rfl⟩)
      (.cons (show organization.step exchangedOnce .exchange formed from ⟨rfl, rfl⟩)
        (.nil formed)))

/-- The observer can retain only the two cell values, but this summary cannot
preserve every future action capability of the formed organization. -/
theorem parts_only_cannot_preserve_futures :
    ¬ ∃ summary : Generative.Process (Bool × Bool) Event,
      ∀ s word, Generative.Feasible organization s word ↔
        Generative.Feasible summary (parts s) word := by
  rintro ⟨summary, h⟩
  have after : Generative.Feasible organization formed [.exchange] :=
    ⟨exchangedOnce, .cons ⟨rfl, rfl⟩ (.nil exchangedOnce)⟩
  have before : ¬ Generative.Feasible organization raw [.exchange] := by
    rintro ⟨t, ht⟩
    exact exchange_unavailable_before_formation
      ⟨t, Generative.trace_singleton_iff.mp ht⟩
  have distinct := Generative.feasible_difference_implies_projection_difference
    h after before
  exact distinct formation_preserves_cell_values.symm

theorem no_fuel_blocks_formation (s : Device) (h : s.fuel = 0) :
    ¬ Generative.Enabled organization s .assemble := by
  rintro ⟨_, _, _, hpositive, _⟩
  rw [h] at hpositive
  exact Nat.lt_irrefl 0 hpositive

theorem no_spare_blocks_formation (s : Device) (h : s.spare = false) :
    ¬ Generative.Enabled organization s .assemble := by
  rintro ⟨_, _, hspare, _, _⟩
  exact Bool.noConfusion (h.symm.trans hspare)

end SystemsOrganization

#print axioms SystemsOrganization.deterministic_trace_iff
#print axioms SystemsOrganization.evolve_semiconjugacy
#print axioms SystemsOrganization.commuting_iff_all_words
#print axioms SystemsOrganization.projected_trace_exact
#print axioms SystemsOrganization.reduced_law_exists_iff
#print axioms SystemsOrganization.commuting_composes
#print axioms SystemsOrganization.coupled_components_preserve_history
#print axioms SystemsOrganization.self_routing_fixed
#print axioms SystemsOrganization.cross_routing_two_steps
#print axioms SystemsOrganization.cross_routing_not_fixed
#print axioms SystemsOrganization.same_cells_different_collective_recurrence
#print axioms SystemsOrganization.crossed_left_not_fibre_consistent
#print axioms SystemsOrganization.no_autonomous_left_law
#print axioms SystemsOrganization.link_inventory_preserved
#print axioms SystemsOrganization.fuel_does_not_increase
#print axioms SystemsOrganization.formation_step
#print axioms SystemsOrganization.formation_preserves_cell_values
#print axioms SystemsOrganization.formation_consumes_spare_and_fuel
#print axioms SystemsOrganization.exchange_unavailable_before_formation
#print axioms SystemsOrganization.exchange_available_after_formation
#print axioms SystemsOrganization.formation_and_recurrence_same_history
#print axioms SystemsOrganization.parts_only_cannot_preserve_futures
#print axioms SystemsOrganization.no_fuel_blocks_formation
#print axioms SystemsOrganization.no_spare_blocks_formation
