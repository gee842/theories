import Becoming.Readout

/-!
# Projected laws: when a description closes under the law, and what wiring and formation do

For a law of change `next : S → A → S` (a process of the spine by `Assurance.ofMap`) and a
projection `p : S → Q`, a reduced law `reduced : Q → A → Q` **commutes** with it when the
projection of each step is the reduced step of the projection (`Commuting`). This module states,
on the core's processes, traces and `Becoming.Readout`, what `SystemsOrganization` (8 October)
proved on its own `evolve` (which is `List.foldl`) and what the join `ProjectedLawTraces`
(17 October) read through the core (board item F3R, 18 October 2026).

* **A reduced law.** A projection commutes with a reduced law exactly where its step factors
  through the reduced process (`commuting_iff_factors`), and exactly where it carries every trace
  to a trace with the same word (`commuting_iff_traces`); configurations alike under it then go
  alike (`fibre_iff_goAlike`). Given an explicit section, a reduced law exists exactly where the
  fibres are consistent (`reduced_law_exists_iff`); no choice is used. Commuting projections and
  trace-carrying projections compose (`commuting_composes`, `traces_compose`), and two component
  equations of the law carry every trace to a trace of the coupled law (`coupled_trace`). That
  every word is then carried is the core's `Readout.foldl_semiconj`.
* **Same cells, different wiring.** Two copy cells wired straight rest at `(true, false)`, wired
  crossed they do not and return after two steps (`wiring_recurrence`); under the crossed wiring
  configurations alike in their left cell do not go alike (`crossed_left_not_fibre_consistent`,
  `left_not_goAlike`), so no law on the left cell carries it (`no_autonomous_left_law`,
  `left_carries_no_law`).
* **Formation inside one law.** In `organization`, a device whose exchange step becomes
  possible only after an assembly step that draws a spare and fuel: the link inventory is kept
  and fuel never rises (`link_inventory_preserved`, `fuel_does_not_increase`); assembly keeps the
  cell values (`formation_preserves_cell_values`) while it makes exchange possible
  (`exchange_unavailable_before_formation`, `exchange_available_after_formation`), so no process
  on the cell values alone keeps the device's possible futures
  (`parts_only_cannot_preserve_futures`); without fuel or spare no assembly is possible
  (`no_fuel_blocks_formation`, `no_spare_blocks_formation`).

The wiring and the device are supplied countermodels, not definitions or proofs of emergence;
no favourable direction, learning or ethics is derived. Every declaration has an empty axiom
report.
-/

namespace Becoming

open Generative Assurance

universe u v w z

namespace ProjectedLaws

variable {S : Type u} {Q : Type v} {R : Type w} {A : Type z}

/-! ## A reduced law -/

/-- The projection of each step is the reduced step of the projection. -/
def Commuting (next : S → A → S) (reduced : Q → A → Q) (p : S → Q) : Prop :=
  ∀ s a, p (next s a) = reduced (p s) a

/-- Configurations with one projection have successors with one projection. -/
def FibreConsistent (next : S → A → S) (p : S → Q) : Prop :=
  ∀ s t, p s = p t → ∀ a, p (next s a) = p (next t a)

/-- A step of the law: its course is the fold of the law. -/
theorem trace_iff {next : S → A → S} :
    ∀ {s t : S} {word : List A}, Trace (ofMap next) s word t ↔ t = word.foldl next s
  | _, _, [] => ⟨fun path => (trace_nil_iff.mp path).symm, fun same => trace_nil_iff.mpr same.symm⟩
  | _, _, _ :: _ => ⟨fun path => match trace_cons_iff.mp path with
      | ⟨_, step, rest⟩ => (trace_iff.mp rest).trans
          (congrArg (fun x => List.foldl next x _) step),
    fun same => .cons rfl (trace_iff.mpr same)⟩

/-- **A projection commutes with a reduced law exactly where the step factors through it** into
the reduced process. -/
theorem commuting_iff_factors {next : S → A → S} {reduced : Q → A → Q} {p : S → Q} :
    Commuting next reduced p ↔ FactorsThrough (ofMap next) p (ofMap reduced) :=
  ⟨fun commutes s a _ step => (congrArg p step).trans (commutes s a),
   fun factors s a => factors s a (next s a) rfl⟩

/-- **The fibres of a projection are consistent exactly where configurations alike under it go
alike.** -/
theorem fibre_iff_goAlike {next : S → A → S} {p : S → Q} :
    FibreConsistent next p ↔ GoAlike (ofMap next) p :=
  ⟨fun consistent s s' a _ _ same step step' =>
      (congrArg p step).trans ((consistent s s' same a).trans (congrArg p step').symm),
   fun alike s s' same a => alike s s' a (next s a) (next s' a) same rfl rfl⟩

/-- **Given an explicit section, a reduced law exists exactly where the fibres are consistent.**
The section is a representative of each summary, supplied; no choice is used. -/
theorem reduced_law_exists_iff (next : S → A → S) (p : S → Q) (sectionMap : Q → S)
    (back : ∀ q, p (sectionMap q) = q) :
    (∃ reduced : Q → A → Q, Commuting next reduced p) ↔ FibreConsistent next p :=
  ⟨fun ⟨reduced, commutes⟩ s t same a =>
      (commutes s a).trans ((congrArg (fun q => reduced q a) same).trans (commutes t a).symm),
   fun consistent => ⟨fun q a => p (next (sectionMap q) a), fun s a =>
      consistent s (sectionMap (p s)) (back (p s)).symm a⟩⟩

/-- **Commuting projections compose.** -/
theorem commuting_composes {next : S → A → S} {middle : Q → A → Q} {last : R → A → R}
    {p : S → Q} {q : Q → R} (hp : Commuting next middle p) (hq : Commuting middle last q) :
    Commuting next last (fun s => q (p s)) :=
  fun s a => (congrArg q (hp s a)).trans (hq (p s) a)

/-- **A projection commutes with a reduced law exactly where it takes every trace of the process
to a trace of the reduced process** with the same word. -/
theorem commuting_iff_traces {next : S → A → S} {reduced : Q → A → Q} {p : S → Q} :
    Commuting next reduced p ↔
      ∀ s word t, Trace (ofMap next) s word t → Trace (ofMap reduced) (p s) word (p t) :=
  ⟨fun commutes s word _ path =>
     trace_iff.mpr ((congrArg p (trace_iff.mp path)).trans
       (Readout.foldl_semiconj next p reduced commutes word s)),
   fun carries s a => trace_iff.mp (carries s [a] _ (trace_iff.mpr rfl))⟩

/-- **Projections carrying every trace compose.** -/
theorem traces_compose {next : S → A → S} {middle : Q → A → Q} {last : R → A → R}
    {p : S → Q} {q : Q → R}
    (hp : ∀ s word t, Trace (ofMap next) s word t → Trace (ofMap middle) (p s) word (p t))
    (hq : ∀ s word t, Trace (ofMap middle) s word t → Trace (ofMap last) (q s) word (q t)) :
    ∀ s word t, Trace (ofMap next) s word t → Trace (ofMap last) (q (p s)) word (q (p t)) :=
  commuting_iff_traces.mp
    (commuting_composes (commuting_iff_traces.mpr hp) (commuting_iff_traces.mpr hq))

/-- The law of two components, each updated from both. -/
def coupledNext (left : Q → R → A → Q) (right : Q → R → A → R) (state : Q × R) (a : A) : Q × R :=
  (left state.1 state.2 a, right state.1 state.2 a)

/-- **Two component equations of the law carry every trace to a trace of the coupled law**, the
components of each configuration together. -/
theorem coupled_trace {next : S → A → S} (p : S → Q) (q : S → R)
    (left : Q → R → A → Q) (right : Q → R → A → R)
    (hp : ∀ s a, p (next s a) = left (p s) (q s) a)
    (hq : ∀ s a, q (next s a) = right (p s) (q s) a)
    {s t : S} {word : List A} (path : Trace (ofMap next) s word t) :
    Trace (ofMap (coupledNext left right)) (p s, q s) word (p t, q t) :=
  (commuting_iff_traces (p := fun x => (p x, q x)) (reduced := coupledNext left right)).mp
    (fun s a => (congrArg (fun y => (y, q (next s a))) (hp s a)).trans
      (congrArg (fun y => (left (p s) (q s) a, y)) (hq s a))) s word t path

/-! ## Same cells, different wiring -/

/-- A copy cell. -/
def copyCell (input : Bool) : Bool := input

/-- Two copy cells, wired straight or crossed. -/
def routed (crossed : Bool) (state : Bool × Bool) (_ : Unit) : Bool × Bool :=
  if crossed then (copyCell state.2, copyCell state.1) else (copyCell state.1, copyCell state.2)

theorem self_routing_fixed : ∀ s : Bool × Bool, routed false s () = s
  | (_, _) => rfl

theorem cross_routing_two_steps : ∀ s : Bool × Bool, [(), ()].foldl (routed true) s = s
  | (_, _) => rfl

theorem cross_routing_not_fixed : routed true (true, false) () ≠ (true, false) := by decide

/-- **Same cells, different recurrence.** -/
theorem wiring_recurrence :
    Trace (ofMap (routed false)) (true, false) [()] (true, false) ∧
      ¬ Trace (ofMap (routed true)) (true, false) [()] (true, false) ∧
      Trace (ofMap (routed true)) (true, false) [(), ()] (true, false) :=
  ⟨trace_iff.mpr rfl, fun path => cross_routing_not_fixed (trace_iff.mp path).symm,
   trace_iff.mpr rfl⟩

/-- **Under the crossed wiring the left cell's next value is not fixed by the left cell.** -/
theorem crossed_left_not_fibre_consistent : ¬ FibreConsistent (routed true) (fun s => s.1) :=
  fun consistent => Bool.noConfusion (consistent (false, false) (false, true) rfl ())

/-- **No autonomous law of the left cell commutes with the crossed wiring.** -/
theorem no_autonomous_left_law :
    ¬ ∃ reduced : Bool → Unit → Bool, Commuting (routed true) reduced (fun s => s.1) :=
  fun found => crossed_left_not_fibre_consistent
    ((reduced_law_exists_iff (routed true) (fun s => s.1) (fun x => (x, false)) fun _ => rfl).mp
      found)

/-- **Under the crossed wiring, configurations alike in their left cell do not go alike.** -/
theorem left_not_goAlike : ¬ GoAlike (ofMap (routed true)) (fun s => s.1) :=
  fun alike => crossed_left_not_fibre_consistent (fibre_iff_goAlike.mpr alike)

/-- **No determined process on the left cell admits the steps of the crossed wiring read through
it.** -/
theorem left_carries_no_law :
    ¬ ∃ P : Process Bool Unit, Determined P ∧ FactorsThrough (ofMap (routed true)) (fun s => s.1) P :=
  fun found => left_not_goAlike (carries_law_iff.mp found)

/-! ## Formation inside one law -/

/-- Two cells, a link, a spare and fuel. -/
structure Device where
  left : Bool
  right : Bool
  linked : Bool
  spare : Bool
  fuel : Nat
  deriving DecidableEq

/-- Assembly and exchange. -/
inductive Event where
  | assemble
  | exchange
  deriving DecidableEq

def assembled (s : Device) : Device := { s with linked := true, spare := false, fuel := s.fuel - 1 }

def exchanged (s : Device) : Device := { s with left := copyCell s.right, right := copyCell s.left }

/-- Assembly needs the spare and fuel and no link; exchange needs the link. -/
def organization : Process Device Event where
  step s a t := match a with
    | .assemble => s.linked = false ∧ s.spare = true ∧ 0 < s.fuel ∧ t = assembled s
    | .exchange => s.linked = true ∧ t = exchanged s

/-- The cell values. -/
def parts (s : Device) : Bool × Bool := (s.left, s.right)

/-- The link and the spare, counted. -/
def linkInventory (s : Device) : Nat := (if s.linked then 1 else 0) + (if s.spare then 1 else 0)

/-- **Assembly turns the spare into the link; exchange adds nothing.** -/
theorem link_inventory_preserved {s t : Device} {a : Event} (h : organization.step s a t) :
    linkInventory t = linkInventory s := by
  cases a with
  | assemble =>
    obtain ⟨hl, hs, _, rfl⟩ := h
    unfold linkInventory assembled
    rw [hl, hs]
    rfl
  | exchange =>
    obtain ⟨_, rfl⟩ := h
    rfl

/-- **Fuel never rises.** -/
theorem fuel_does_not_increase {s t : Device} {a : Event} (h : organization.step s a t) :
    t.fuel ≤ s.fuel := by
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

theorem formation_step : organization.step raw .assemble formed := ⟨rfl, rfl, by decide, rfl⟩

theorem formation_preserves_cell_values : parts raw = parts formed := rfl

theorem formation_consumes_spare_and_fuel :
    raw.spare = true ∧ formed.spare = false ∧ raw.fuel = 1 ∧ formed.fuel = 0 := by decide

/-- **Formation draws on the spare and the fuel**: every assembly step from the raw device reaches
a device without the spare and without fuel. -/
theorem assembly_draws {t : Device} (step : organization.step raw .assemble t) :
    raw.spare = true ∧ t.spare = false ∧ raw.fuel = 1 ∧ t.fuel = 0 :=
  Eq.subst (motive := fun x => raw.spare = true ∧ x.spare = false ∧ raw.fuel = 1 ∧ x.fuel = 0)
    step.2.2.2.symm formation_consumes_spare_and_fuel

theorem exchange_unavailable_before_formation : ¬ Enabled organization raw .exchange
  | ⟨_, h, _⟩ => Bool.noConfusion h

theorem exchange_available_after_formation : Enabled organization formed .exchange :=
  ⟨exchangedOnce, rfl, rfl⟩

theorem formation_and_recurrence_same_history :
    Trace organization raw [.assemble, .exchange, .exchange] formed :=
  .cons formation_step
    (.cons (show organization.step formed .exchange exchangedOnce from ⟨rfl, rfl⟩)
      (.cons (show organization.step exchangedOnce .exchange formed from ⟨rfl, rfl⟩) (.nil formed)))

/-- **No process on the cell values alone keeps the device's possible futures.** -/
theorem parts_only_cannot_preserve_futures :
    ¬ ∃ summary : Process (Bool × Bool) Event,
      ∀ s word, Feasible organization s word ↔ Feasible summary (parts s) word :=
  fun ⟨summary, h⟩ =>
    have after : Feasible organization formed [.exchange] :=
      ⟨exchangedOnce, .cons ⟨rfl, rfl⟩ (.nil exchangedOnce)⟩
    have before : ¬ Feasible organization raw [.exchange] := fun ⟨t, ht⟩ =>
      exchange_unavailable_before_formation ⟨t, trace_singleton_iff.mp ht⟩
    before ((h raw [.exchange]).mpr
      (Eq.subst (motive := fun x => Feasible summary x [.exchange])
        formation_preserves_cell_values.symm ((h formed [.exchange]).mp after)))

theorem no_fuel_blocks_formation (s : Device) (h : s.fuel = 0) :
    ¬ Enabled organization s .assemble
  | ⟨_, _, _, positive, _⟩ => Nat.lt_irrefl 0 (h ▸ positive)

theorem no_spare_blocks_formation (s : Device) (h : s.spare = false) :
    ¬ Enabled organization s .assemble
  | ⟨_, _, spare, _, _⟩ => Bool.noConfusion (h.symm.trans spare)

end ProjectedLaws

end Becoming
