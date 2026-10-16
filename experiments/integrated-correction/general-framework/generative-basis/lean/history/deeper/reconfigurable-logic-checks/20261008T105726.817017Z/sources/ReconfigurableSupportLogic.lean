import GenerativeCore

/-! A changing access relation makes previously omitted occupancy relevant.
K supplies the permitted support scope. Redirect, take and release are atomic
steps of one configuration. The target is exact finite-word feasibility, not
all observations, inevitable progress, physical time or ethical priority. -/
namespace Generative.ReconfigurableSupportLogic
universe u v
variable {R : Type u} [DecidableEq R]

structure Configuration (R : Type u) where
  route : R
  busy : R → Bool

inductive Event (R : Type u) where
  | redirect : R → Event R
  | take : Event R
  | release : R → Event R

def setBusy (b : R → Bool) (r : R) (value : Bool) : R → Bool :=
  fun i => if i = r then value else b i

def enabled (K : R → Prop) (s : Configuration R) : Event R → Prop
  | .redirect r => K r
  | .take => K s.route ∧ s.busy s.route = false
  | .release r => K r ∧ s.busy r = true

def after (s : Configuration R) : Event R → Configuration R
  | .redirect r => ⟨r, s.busy⟩
  | .take => ⟨s.route, setBusy s.busy s.route true⟩
  | .release r => ⟨s.route, setBusy s.busy r false⟩

def process (K : R → Prop) : Process (Configuration R) (Event R) where
  step s e t := enabled K s e ∧ t = after s e

def OccupancyAgrees (K : R → Prop) (s t : Configuration R) : Prop :=
  ∀ r, K r → s.busy r = t.busy r

def Agrees (K : R → Prop) (s t : Configuration R) : Prop :=
  s.route = t.route ∧ OccupancyAgrees K s t

def observe (K : R → Prop) (s : Configuration R) : R × ({r // K r} → Bool) :=
  (s.route, fun r => s.busy r.val)

theorem enabled_exact (K : R → Prop) (s : Configuration R) (e : Event R) :
    Enabled (process K) s e ↔ enabled K s e := by
  exact ⟨fun ⟨_, h, _⟩ => h, fun h => ⟨after s e, h, rfl⟩⟩

theorem redirect_readiness (K : R → Prop) (s : Configuration R) (r : R) :
    Enabled (process K) (after s (.redirect r)) .take ↔ K r ∧ s.busy r = false :=
  enabled_exact K _ .take

theorem agrees_symm {K : R → Prop} {s t : Configuration R} (h : Agrees K s t) :
    Agrees K t s := ⟨h.1.symm, fun r hr => (h.2 r hr).symm⟩

theorem observation_iff (K : R → Prop) (s t : Configuration R) :
    observe K s = observe K t ↔ Agrees K s t := by
  constructor
  · intro eq
    refine ⟨congrArg Prod.fst eq, ?_⟩
    intro r hr
    exact congrFun (congrArg Prod.snd eq) ⟨r, hr⟩
  · intro h
    apply Prod.ext h.1
    funext r
    exact h.2 r.val r.property

theorem agrees_enabled {K : R → Prop} {s t : Configuration R}
    (h : Agrees K s t) (e : Event R) : enabled K s e ↔ enabled K t e := by
  cases e with
  | redirect r => exact Iff.rfl
  | take =>
    change (K s.route ∧ s.busy s.route = false) ↔ (K t.route ∧ t.busy t.route = false)
    rw [← h.1]
    exact ⟨fun ⟨hr, free⟩ => ⟨hr, (h.2 _ hr).symm.trans free⟩,
      fun ⟨hr, free⟩ => ⟨hr, (h.2 _ hr).trans free⟩⟩
  | release r =>
    exact ⟨fun ⟨hr, held⟩ => ⟨hr, (h.2 _ hr).symm.trans held⟩,
      fun ⟨hr, held⟩ => ⟨hr, (h.2 _ hr).trans held⟩⟩

theorem agrees_after {K : R → Prop} {s t : Configuration R}
    (h : Agrees K s t) (e : Event R) : Agrees K (after s e) (after t e) := by
  cases e with
  | redirect r => exact ⟨rfl, h.2⟩
  | take =>
    refine ⟨h.1, ?_⟩
    intro r hr
    change setBusy s.busy s.route true r = setBusy t.busy t.route true r
    simp only [setBusy, h.1]
    by_cases eq : r = t.route
    · simp [eq]
    · simp [eq, h.2 r hr]
  | release a =>
    refine ⟨h.1, ?_⟩
    intro r hr
    change setBusy s.busy a false r = setBusy t.busy a false r
    by_cases eq : r = a
    · simp [setBusy, eq]
    · simp [setBusy, eq, h.2 r hr]

theorem match_trace {K : R → Prop} {s last : Configuration R} {word : List (Event R)}
    (history : Trace (process K) s word last) :
    ∀ t, Agrees K s t → ∃ final, Trace (process K) t word final ∧ Agrees K last final := by
  induction history with
  | nil s => intro t h; exact ⟨t, .nil _, h⟩
  | @cons s mid last e word step tail ih =>
    intro t h
    obtain ⟨en, rfl⟩ := step
    obtain ⟨final, rest, related⟩ := ih (after t e) (agrees_after h e)
    exact ⟨final, .cons ⟨(agrees_enabled h e).mp en, rfl⟩ rest, related⟩

theorem agrees_feasible {K : R → Prop} {s t : Configuration R}
    (h : Agrees K s t) (word : List (Event R)) :
    Feasible (process K) s word ↔ Feasible (process K) t word := by
  constructor
  · rintro ⟨last, ht⟩
    obtain ⟨final, trace, _⟩ := match_trace ht t h
    exact ⟨final, trace⟩
  · rintro ⟨last, ht⟩
    obtain ⟨final, trace, _⟩ := match_trace ht s (agrees_symm h)
    exact ⟨final, trace⟩

theorem observation_sufficient {K : R → Prop} {s t : Configuration R}
    (h : observe K s = observe K t) (word : List (Event R)) :
    Feasible (process K) s word ↔ Feasible (process K) t word :=
  agrees_feasible ((observation_iff K s t).mp h) word

def probe (r : R) : List (Event R) := [.redirect r, .take]

theorem probe_exact (K : R → Prop) (s : Configuration R) (r : R) :
    Feasible (process K) s (probe r) ↔ K r ∧ s.busy r = false := by
  constructor
  · rintro ⟨last, history⟩
    obtain ⟨mid, first, tail⟩ := trace_cons_iff.mp history
    obtain ⟨_, rfl⟩ := first
    have take := trace_singleton_iff.mp tail
    exact take.1
  · rintro ⟨hr, free⟩
    exact ⟨after (after s (.redirect r)) .take,
      .cons ⟨hr, rfl⟩ (.cons ⟨⟨hr, free⟩, rfl⟩ (.nil _))⟩

theorem bool_false_iff_eq (a b : Bool) (h : (a = false ↔ b = false)) : a = b := by
  cases a <;> cases b <;> simp_all

theorem probes_determine_occupancy {K : R → Prop} {s t : Configuration R}
    (h : ∀ r, K r → (Feasible (process K) s (probe r) ↔
      Feasible (process K) t (probe r))) : OccupancyAgrees K s t := by
  intro r hr
  apply bool_false_iff_eq
  constructor
  · intro free
    exact ((probe_exact K t r).mp ((h r hr).mp ((probe_exact K s r).mpr ⟨hr, free⟩))).2
  · intro free
    exact ((probe_exact K s r).mp ((h r hr).mpr ((probe_exact K t r).mpr ⟨hr, free⟩))).2

/-- With the current route fixed, agreement on K is both sufficient and
necessary for exact finite-word behavior under the declared reconfigurations. -/
theorem fixed_route_behavior_iff {K : R → Prop} {s t : Configuration R}
    (route : s.route = t.route) :
    (∀ word, Feasible (process K) s word ↔ Feasible (process K) t word) ↔
      OccupancyAgrees K s t := by
  exact ⟨fun h => probes_determine_occupancy (fun r _ => h (probe r)),
    fun h word => agrees_feasible ⟨route, h⟩ word⟩

/-- Any exact representation must separate occupancy distinctions on K.
This says nothing about distinctions outside K or about route minimality. -/
theorem exact_reader_separates {K : R → Prop} {Q : Type v}
    (q : Configuration R → Q) (read : Q → List (Event R) → Prop)
    (correct : ∀ s word, read (q s) word ↔ Feasible (process K) s word)
    {s t : Configuration R} (same : q s = q t) : OccupancyAgrees K s t := by
  apply probes_determine_occupancy
  intro r _
  rw [← correct s, ← correct t, same]

theorem unrestricted_reader_injective {Q : Type v} (root : R)
    (encode : (R → Bool) → Q) (read : Q → List (Event R) → Prop)
    (correct : ∀ busy word, read (encode busy) word ↔
      Feasible (process (fun _ : R => True)) ⟨root, busy⟩ word) :
    Function.Injective encode := by
  intro b c same
  have h : OccupancyAgrees (fun _ : R => True)
      (Configuration.mk root b) (Configuration.mk root c) := by
    apply probes_determine_occupancy
    intro r _
    rw [← correct b, ← correct c, same]
  funext r
  exact h r True.intro

namespace Witness

def allSlots (_ : Bool) : Prop := True
def firstOnly (r : Bool) : Prop := r = false
def clear : Configuration Bool := ⟨false, fun _ => false⟩
def hidden : Configuration Bool := after (after (after clear (.redirect true)) .take) (.redirect false)
def activeView (s : Configuration Bool) := (s.route, s.busy s.route)

theorem hidden_formed :
    Trace (process allSlots) clear [.redirect true, .take, .redirect false] hidden := by
  exact .cons ⟨True.intro, rfl⟩
    (.cons ⟨⟨True.intro, rfl⟩, rfl⟩ (.cons ⟨True.intro, rfl⟩ (.nil _)))

theorem old_observation_same : observe firstOnly clear = observe firstOnly hidden := by
  apply (observation_iff _ _ _).mpr
  refine ⟨rfl, ?_⟩
  intro r hr
  change r = false at hr
  subst r
  rfl

theorem old_workload_exact (word : List (Event Bool)) :
    Feasible (process firstOnly) clear word ↔ Feasible (process firstOnly) hidden word :=
  observation_sufficient old_observation_same word

theorem new_probe_separates :
    Feasible (process allSlots) clear (probe true) ∧
      ¬ Feasible (process allSlots) hidden (probe true) := by
  constructor
  · exact (probe_exact _ _ _).mpr ⟨True.intro, rfl⟩
  · intro h
    have bad := ((probe_exact _ _ _).mp h).2
    cases bad

theorem same_active_view : activeView clear = activeView hidden := rfl

theorem no_old_view_future_reader :
    ¬ ∃ read : (Bool × Bool) → Prop, ∀ s,
      read (activeView s) ↔ Feasible (process allSlots) s (probe true) := by
  rintro ⟨read, correct⟩
  have yes := (correct clear).mpr new_probe_separates.1
  exact new_probe_separates.2 ((correct hidden).mp (same_active_view ▸ yes))

theorem no_blind_redirect_update :
    ¬ ∃ update : (Bool × Bool) → Bool → (Bool × Bool), ∀ s r,
      update (activeView s) r = activeView (after s (.redirect r)) := by
  rintro ⟨update, correct⟩
  have eq : activeView (after clear (.redirect true)) =
      activeView (after hidden (.redirect true)) :=
    (correct clear true).symm.trans ((congrArg (fun x => update x true) same_active_view).trans
      (correct hidden true))
  have bad := congrArg Prod.snd eq
  cases bad

theorem redirect_changes_readiness_only :
    (after hidden (.redirect true)).busy = hidden.busy ∧
      Enabled (process allSlots) hidden .take ∧
      ¬ Enabled (process allSlots) (after hidden (.redirect true)) .take := by
  refine ⟨rfl, ⟨after hidden .take, ⟨True.intro, rfl⟩, rfl⟩, ?_⟩
  intro h
  have bad := ((redirect_readiness allSlots hidden true).mp h).2
  cases bad

/-- A current observation of the new slot suffices to update the active view;
obtaining a trustworthy observation atomically is a separate implementation. -/
theorem refreshed_view (s : Configuration Bool) (r : Bool) :
    (r, s.busy r) = activeView (after s (.redirect r)) := rfl

end Witness
end Generative.ReconfigurableSupportLogic

#print axioms Generative.ReconfigurableSupportLogic.enabled_exact
#print axioms Generative.ReconfigurableSupportLogic.redirect_readiness
#print axioms Generative.ReconfigurableSupportLogic.agrees_symm
#print axioms Generative.ReconfigurableSupportLogic.observation_iff
#print axioms Generative.ReconfigurableSupportLogic.agrees_enabled
#print axioms Generative.ReconfigurableSupportLogic.agrees_after
#print axioms Generative.ReconfigurableSupportLogic.match_trace
#print axioms Generative.ReconfigurableSupportLogic.agrees_feasible
#print axioms Generative.ReconfigurableSupportLogic.observation_sufficient
#print axioms Generative.ReconfigurableSupportLogic.probe_exact
#print axioms Generative.ReconfigurableSupportLogic.bool_false_iff_eq
#print axioms Generative.ReconfigurableSupportLogic.probes_determine_occupancy
#print axioms Generative.ReconfigurableSupportLogic.fixed_route_behavior_iff
#print axioms Generative.ReconfigurableSupportLogic.exact_reader_separates
#print axioms Generative.ReconfigurableSupportLogic.unrestricted_reader_injective
#print axioms Generative.ReconfigurableSupportLogic.Witness.hidden_formed
#print axioms Generative.ReconfigurableSupportLogic.Witness.old_observation_same
#print axioms Generative.ReconfigurableSupportLogic.Witness.old_workload_exact
#print axioms Generative.ReconfigurableSupportLogic.Witness.new_probe_separates
#print axioms Generative.ReconfigurableSupportLogic.Witness.same_active_view
#print axioms Generative.ReconfigurableSupportLogic.Witness.no_old_view_future_reader
#print axioms Generative.ReconfigurableSupportLogic.Witness.no_blind_redirect_update
#print axioms Generative.ReconfigurableSupportLogic.Witness.redirect_changes_readiness_only
#print axioms Generative.ReconfigurableSupportLogic.Witness.refreshed_view
