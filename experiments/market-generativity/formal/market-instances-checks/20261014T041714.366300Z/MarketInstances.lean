import Becoming.Viability
import Becoming.Lasting
import MarketGenerativity
import FiniteSupportObstruction
import PartialRegimeTransition

/-!
# The rational market as an instance of the core's laws (periphery)

The market law of `MarketGenerativity` is rational arithmetic with standard axioms, so its
instances of the pure core's laws are stated here; the core does not import this module.

* **Protected continuation (`Becoming.Viability`).** The operating map is a law of change driven
  by disturbances (`history_eq`), and the guarded market is the core's guarded law with the
  essential floors as guard (`guardedHistory_eq`). Some disturbance is admissible for every
  bound (`worst_admissible`). So, for every parameter set, bound set and start, no admissible
  history ever fails the essential guard exactly when some set of states containing the start
  lies within the essential floors and is closed under every admissible disturbance
  (`never_fails_iff`); the largest such set is the viability kernel. Under `Certificate p b` the
  rectangle `Safe p b` is one such set (`safe_closed`), so `safe_history_never_fails` is an
  instance (`safe_never_fails`), and every safe state lies in the kernel (`safe_within_kernel`).
  The numerical example is an instance (`example_never_fails`).
* **Finite support obstruction (`Becoming.Lasting`, exhaustion).** With a correction strength
  chosen at each step, the market is a law of change (`scheduled`; `run_eq`, `guarded_eq`). On
  a physical pair the share grows at most by `3/2` a step, whose orbit is the share times
  `(3/2)^n` (`orbit_growth`); while that orbit stays at or below `1/6`, a step with a
  nonnegative shock costs the stock one unit above the floor `5`. So a physical start whose
  share times `(3/2)^N` is at most `1/6` and whose stock is below `5 + N` stops within `N`
  steps on every such history: `finite_support_forces_failure` is an instance
  (`forces_failure_instance`).
* **Supported finite transition (`Becoming.Lasting`, ladders).** The cover recurrence is a
  ladder for every correction schedule and every disturbance whose shock is at most the cost
  (`cover_ladder`), so a physical start whose stock covers `N` steps runs within the essential
  floor for its first `N` steps, for every correction strength (`supported_prefix_instance`);
  the prefixes of `supported_finite_transition` and `supported_partial_transition` are its
  cases (`pulse_prefix_instance`, `partial_prefix_instance`). At the worst share the cover is
  exact: the stock alone lasts `n` steps at or above `5` exactly when it is at least the cover
  for `n` steps (`cover_exact`).
* **Partial correction boundary (`Becoming.Lasting`, never reaching).** The regime law is a
  determined law (`path_eq`). Some positive seed never lands exactly when some set closed under
  the law and avoiding landing contains a positive seed (`never_lands_iff`). For
  `0 ≤ b ≤ 3/4`, every positive seed lands exactly when the quality margin at the fixed
  quality `3/8` under the worst influence `1` is nonnegative (`lands_iff_margin`), and exactly
  when no such closed set contains a positive seed (`lands_iff_no_closed`). Above the boundary
  the fixed configuration is such a set by itself (`fixed_point_instance`).

Every declaration may depend on the standard axioms through rational arithmetic only.
-/

namespace Becoming.MarketInstances

open Becoming.Viability MarketGenerativity

/-- The market's history is the core's history of the operating map. -/
theorem history_eq {n : Nat} (p : Parameters n) (s : State n) (d : Nat → Disturbance n) :
    ∀ t, MarketGenerativity.history p s d t = Viability.history (operatingStep p) s d t
  | 0 => rfl
  | t + 1 => congrArg (fun x => operatingStep p x (d t)) (history_eq p s d t)

/-- The market's guarded step is the core's guarded law with the essential floors as guard. -/
theorem guardedStep_eq {n : Nat} (p : Parameters n) (b : Bounds n) (e : Disturbance n) :
    ∀ o, MarketGenerativity.guardedStep p b e o =
      Viability.guardedStep (operatingStep p) (essentialReady p b) e o
  | none => rfl
  | some _ => rfl

/-- The market's guarded history is the core's guarded history. -/
theorem guardedHistory_eq {n : Nat} (p : Parameters n) (b : Bounds n) (s : State n)
    (d : Nat → Disturbance n) :
    ∀ t, MarketGenerativity.guardedHistory p b s d t =
      Viability.guardedHistory (operatingStep p) (essentialReady p b) s d t
  | 0 => rfl
  | t + 1 => (guardedStep_eq p b (d t) _).trans
      (congrArg (Viability.guardedStep (operatingStep p) (essentialReady p b) (d t))
        (guardedHistory_eq p b s d t))

/-- The worst disturbance a bound admits is admissible: some disturbance always is. -/
theorem worst_admissible {n : Nat} (b : Bounds n) : Admissible b ⟨b.epsilon, b.nu⟩ :=
  ⟨Rat.le_refl, fun _ => Rat.le_refl⟩

/-- **For every market law, bound set and start: no admissible history ever fails the essential
guard exactly when some set of states containing the start lies within the essential floors and
is closed under every admissible disturbance.** -/
theorem never_fails_iff {n : Nat} (p : Parameters n) (b : Bounds n) (s : State n) :
    (∀ d : Nat → Disturbance n, (∀ t, Admissible b (d t)) →
        ∀ t, MarketGenerativity.guardedHistory p b s d t =
          some (MarketGenerativity.history p s d t)) ↔
      ∃ K : State n → Prop, K s ∧ (∀ x, K x → essentialReady p b x) ∧
        ∀ x e, Admissible b e → K x → K (operatingStep p x e) :=
  (⟨fun every d admissible t =>
      (guardedHistory_eq p b s d t).symm.trans
        ((every d admissible t).trans (congrArg some (history_eq p s d t))),
    fun every d admissible t =>
      (guardedHistory_eq p b s d t).trans
        ((every d admissible t).trans (congrArg some (history_eq p s d t).symm))⟩ :
      (∀ d : Nat → Disturbance n, (∀ t, Admissible b (d t)) →
          ∀ t, MarketGenerativity.guardedHistory p b s d t =
            some (MarketGenerativity.history p s d t)) ↔
        ∀ d : Nat → Disturbance n, (∀ t, Admissible b (d t)) →
          ∀ t, Viability.guardedHistory (operatingStep p) (essentialReady p b) s d t =
            some (Viability.history (operatingStep p) s d t)).trans
    (guarded_never_fails_iff (worst_admissible b))

/-- **The safe rectangle is a certificate** wherever `Certificate p b` holds: it lies within the
essential floors and every admissible disturbance keeps it. -/
theorem safe_closed {n : Nat} {p : Parameters n} {b : Bounds n} (hc : Certificate p b) :
    (∀ x, Safe p b x → essentialReady p b x) ∧
      ∀ x e, Admissible b e → Safe p b x → Safe p b (operatingStep p x e) :=
  ⟨fun _ safe j _ => safe.supports j, fun x e admitted safe => rectangle_one_step p b x e hc safe admitted⟩

/-- **`safe_history_never_fails` is an instance**: a safe start never fails under any admissible
history. -/
theorem safe_never_fails {n : Nat} {p : Parameters n} {b : Bounds n} {s : State n}
    (hc : Certificate p b) (h0 : Safe p b s) (d : Nat → Disturbance n)
    (admissible : ∀ t, Admissible b (d t)) :
    ∀ t, MarketGenerativity.guardedHistory p b s d t = some (MarketGenerativity.history p s d t) :=
  (never_fails_iff p b s).mpr ⟨Safe p b, h0, safe_closed hc⟩ d admissible

/-- Every safe state lies in the viability kernel of the essential guard. -/
theorem safe_within_kernel {n : Nat} {p : Parameters n} {b : Bounds n} (hc : Certificate p b)
    {s : State n} (h0 : Safe p b s) :
    Kernel (disturbed (operatingStep p) (Admissible b)) (essentialReady p b) s :=
  Certificate.kernel (certificate_disturbed_iff.mpr (safe_closed hc)) h0

/-- The numerical example never fails. -/
theorem example_never_fails (d : Nat → Disturbance 1)
    (admissible : ∀ t, Admissible exampleBounds (d t)) :
    ∀ t, MarketGenerativity.guardedHistory exampleParameters exampleBounds exampleState d t =
      some (MarketGenerativity.history exampleParameters exampleState d t) :=
  safe_never_fails example_certificate example_safe d admissible

/-! ## Finite support obstruction -/

/-- The market law with a correction strength chosen at each step. -/
def scheduled (s : State 1) (a : Rat × Disturbance 1) : State 1 :=
  operatingStep (FiniteSupportObstruction.parameters a.1) s a.2

/-- The essential floor of the example bounds. -/
abbrev floor : State 1 → Prop := essentialReady exampleParameters exampleBounds

theorem floor_of_stock {x : State 1} (h : 5 ≤ x.stock 0) : floor x :=
  fun j _ => match j with
    | ⟨0, _⟩ => h
    | ⟨_ + 1, bound⟩ => absurd bound (by omega)

theorem stock_of_floor {x : State 1} (ready : floor x) : 5 ≤ x.stock 0 := ready 0 rfl

/-- The scheduled run is the core's history of the scheduled law. -/
theorem run_eq (beta : Nat → Rat) (d : Nat → Disturbance 1) (initial : State 1) :
    ∀ n, FiniteSupportObstruction.run beta d initial n =
      Viability.history scheduled initial (fun k => (beta k, d k)) n
  | 0 => rfl
  | n + 1 => congrArg (fun x => scheduled x (beta n, d n)) (run_eq beta d initial n)

/-- The scheduled guarded run is the core's guarded history with the essential floor as
guard. -/
theorem guarded_eq (beta : Nat → Rat) (d : Nat → Disturbance 1) (initial : State 1) :
    ∀ n, FiniteSupportObstruction.guarded beta d initial n =
      Viability.guardedHistory scheduled floor initial (fun k => (beta k, d k)) n
  | 0 => rfl
  | n + 1 => by
    show MarketGenerativity.guardedStep (FiniteSupportObstruction.parameters (beta n)) exampleBounds
        (d n) (FiniteSupportObstruction.guarded beta d initial n) =
      Viability.guardedStep scheduled floor (beta n, d n)
        (Viability.guardedHistory scheduled floor initial (fun k => (beta k, d k)) n)
    rw [guarded_eq beta d initial n]
    cases Viability.guardedHistory scheduled floor initial (fun k => (beta k, d k)) n with
    | none => rfl
    | some _ => rfl

/-- The share's growth bound: a step multiplies the share by at most `3/2`. -/
def growth (v : Rat) : Rat := (3/2) * v

theorem orbit_growth (v : Rat) :
    ∀ n, Law.orbit growth v n = v * RegimeAttraction.radius (3/2) 1 n
  | 0 => by show v = v * 1; grind
  | n + 1 => by
    show (3/2) * Law.orbit growth v n = v * ((3/2) * RegimeAttraction.radius (3/2) 1 n)
    rw [orbit_growth v n]
    grind

/-- **`finite_support_forces_failure` is an instance of exhaustion by bounded growth**: the
share's orbit under `growth` stays at or below `1/6` for `N` steps, each step costs the stock a
unit above the floor `5`, and a stock below `5 + N` is not at level `N`. -/
theorem forces_failure_instance (beta : Nat → Rat) (d : Nat → Disturbance 1)
    (initial : State 1) (N : Nat) (hi : FiniteSupportObstruction.PairPhysical initial)
    (hc : 5 ≤ initial.stock 0) (hd : ∀ n, 0 ≤ (d n).shock 0)
    (hsmall : initial.x * RegimeAttraction.radius (3/2) 1 N ≤ 1/6)
    (hshort : initial.stock 0 < 5 + (N : Rat)) :
    FiniteSupportObstruction.guarded beta d initial N = none := by
  have leaves := Lasting.exhausts (f := scheduled) (adm := fun a => 0 ≤ a.2.shock 0)
    (guard := floor) (rel := fun a b : Rat => a ≤ b) (g := growth)
    (R := FiniteSupportObstruction.PairPhysical) (q := fun x => x.x) (θ := 1/6)
    (level := fun k x => 5 + (k : Rat) ≤ x.stock 0)
    (fun _ _ _ hab hbc => Rat.le_trans hab hbc)
    (fun a b h => by show (3/2) * a ≤ (3/2) * b; grind)
    (fun x a _ hx => FiniteSupportObstruction.next_pair_physical a.1 a.2 x hx)
    (fun x a _ hx => FiniteSupportObstruction.next_share_upper a.1 a.2 x hx)
    (fun x ready => by
      have h5 := stock_of_floor ready
      show 5 + ((0 : Nat) : Rat) ≤ x.stock 0
      grind)
    (fun k x a hx ready admitted small next => by
      have h5 := stock_of_floor ready
      have hr : Law.orbit growth x.x (k + 1) ≤ 1/6 := small
      rw [orbit_growth] at hr
      have hgrow := (RegimeAttraction.radius_growth_lower (3/2) 1
        (by decide +kernel) (by decide +kernel) (k + 1)).1
      have hm := Rat.mul_le_mul_of_nonneg_left hgrow hx.1
      have hxs : x.x ≤ 1/6 := by grind
      have loss := FiniteSupportObstruction.next_support_loss a.1 a.2 x h5 hxs admitted
      have hn : 5 + (k : Rat) ≤
          (operatingStep (FiniteSupportObstruction.parameters a.1) x a.2).stock 0 := next
      show 5 + ((k + 1 : Nat) : Rat) ≤ x.stock 0
      simp only [Rat.natCast_add, Rat.natCast_ofNat]
      grind)
    hi (by show Law.orbit growth initial.x N ≤ 1/6; rw [orbit_growth]; exact hsmall)
    (by show ¬ (5 + (N : Rat) ≤ initial.stock 0); grind) (fun k => (beta k, d k)) hd
  rw [guarded_eq]
  exact (Lasting.guarded_none_iff (floor_of_stock hc)).mpr leaves

/-! ## Supported finite transition -/

/-- The cover family: a physical pair whose stock is at least the cover for `n` more steps. -/
def covered (cost : Rat) (n : Nat) (x : State 1) : Prop :=
  FiniteSupportObstruction.PairPhysical x ∧ RegimeTransition.cover cost n ≤ x.stock 0

/-- A smaller shock leaves at least as much support. -/
theorem support_antitone (stock x shock cost : Rat) (h : shock ≤ cost) :
    supportStep stock (1/10) 2 1 x 0 cost ≤ supportStep stock (1/10) 2 1 x 0 shock := by
  unfold supportStep
  grind

/-- **The cover is a ladder** for the essential floor, for every correction schedule and every
disturbance whose shock is at most the cost. -/
theorem cover_ladder (cost : Rat) (hc : 0 ≤ cost) :
    Lasting.Ladder scheduled (fun a => a.2.shock 0 ≤ cost) floor (covered cost) :=
  ⟨fun k _ held => floor_of_stock (Rat.le_trans (RegimeTransition.cover_floor cost hc k) held.2),
   fun k x a admitted held => ⟨FiniteSupportObstruction.next_pair_physical a.1 a.2 x held.1,
     Rat.le_trans (RegimeTransition.cover_step cost (x.stock 0) x.x k hc held.1.1 held.2)
       (support_antitone (x.stock 0) x.x (a.2.shock 0) cost admitted)⟩⟩

/-- A fixed correction strength is a constant schedule. -/
theorem history_scheduled (b : Rat) (s : State 1) (d : Nat → Disturbance 1) :
    ∀ n, MarketGenerativity.history (FiniteSupportObstruction.parameters b) s d n =
      Viability.history scheduled s (fun k => (b, d k)) n
  | 0 => rfl
  | n + 1 => congrArg (fun x => scheduled x (b, d n)) (history_scheduled b s d n)

theorem guardedHistory_scheduled (b : Rat) (s : State 1) (d : Nat → Disturbance 1) :
    ∀ n, MarketGenerativity.guardedHistory (FiniteSupportObstruction.parameters b) exampleBounds
        s d n = Viability.guardedHistory scheduled floor s (fun k => (b, d k)) n
  | 0 => rfl
  | n + 1 => by
    show MarketGenerativity.guardedStep (FiniteSupportObstruction.parameters b) exampleBounds
        (d n) (MarketGenerativity.guardedHistory (FiniteSupportObstruction.parameters b)
          exampleBounds s d n) =
      Viability.guardedStep scheduled floor (b, d n)
        (Viability.guardedHistory scheduled floor s (fun k => (b, d k)) n)
    rw [guardedHistory_scheduled b s d n]
    cases Viability.guardedHistory scheduled floor s (fun k => (b, d k)) n with
    | none => rfl
    | some _ => rfl

/-- **The supported prefix is an instance of the ladder law**: from a physical start whose stock
covers `N` steps, the pulse runs within the essential floor for its first `N` steps, for every
correction strength `b`. -/
theorem supported_prefix_instance (b cost initial : Rat) (s : RegimeBoundary.OperatingState)
    (N : Nat) (hc : 0 ≤ cost) (hs : RegimeAttraction.physical s)
    (hi : RegimeTransition.cover cost N ≤ initial) :
    ∀ t, t ≤ N →
      MarketGenerativity.guardedHistory (FiniteSupportObstruction.parameters b) exampleBounds
          (RegimeAttraction.lift s initial) (fun _ => RegimeTransition.pulseDisturbance cost) t =
        some (MarketGenerativity.history (FiniteSupportObstruction.parameters b)
          (RegimeAttraction.lift s initial) (fun _ => RegimeTransition.pulseDisturbance cost) t) := by
  have lasts := Lasting.Ladder.lasts (cover_ladder cost hc) N (RegimeAttraction.lift s initial)
    ⟨⟨hs.1, hs.2.1, hs.2.2.1, hs.2.2.2.1⟩, hi⟩
  have within := Lasting.Lasts.histories lasts
    (fun _ => (b, RegimeTransition.pulseDisturbance cost)) (fun _ => Rat.le_refl)
  intro t ht
  rw [guardedHistory_scheduled, history_scheduled]
  exact Lasting.guarded_agrees (fun k hk => within k (Nat.le_trans hk ht))

/-- The prefix of `supported_finite_transition` (`pulse_prefix_executes`) is the case `b = 0`. -/
theorem pulse_prefix_instance (cost initial : Rat) (s : RegimeBoundary.OperatingState) (N : Nat)
    (hc : 0 ≤ cost) (hs : RegimeAttraction.physical s)
    (hi : RegimeTransition.cover cost N ≤ initial) :
    ∀ t, t ≤ N → MarketGenerativity.guardedHistory RegimeTransition.pulseParameters exampleBounds
        (RegimeAttraction.lift s initial) (fun _ => RegimeTransition.pulseDisturbance cost) t =
      some (MarketGenerativity.history RegimeTransition.pulseParameters
        (RegimeAttraction.lift s initial) (fun _ => RegimeTransition.pulseDisturbance cost) t) :=
  supported_prefix_instance 0 cost initial s N hc hs hi

/-- The prefix of `supported_partial_transition` (`partial_prefix_executes`) is the case of
correction strength `b`. -/
theorem partial_prefix_instance (b cost initial : Rat) (s : RegimeBoundary.OperatingState)
    (N : Nat) (hc : 0 ≤ cost) (hs : RegimeAttraction.physical s)
    (hi : RegimeTransition.cover cost N ≤ initial) :
    ∀ t, t ≤ N → MarketGenerativity.guardedHistory (PartialRegimeTransition.partialParameters b)
        exampleBounds (RegimeAttraction.lift s initial)
        (fun _ => RegimeTransition.pulseDisturbance cost) t =
      some (MarketGenerativity.history (PartialRegimeTransition.partialParameters b)
        (RegimeAttraction.lift s initial) (fun _ => RegimeTransition.pulseDisturbance cost) t) :=
  supported_prefix_instance b cost initial s N hc hs hi

/-- The support stock alone at the worst share, which renews nothing. -/
def worstSupport (cost stock : Rat) (_ : Unit) : Rat := supportStep stock (1/10) 2 1 0 0 cost

/-- **The cover is exact at the worst share**: the stock alone lasts `n` steps at or above the
floor `5` exactly when it is at least the cover for `n` steps. The cover family is both a ladder
and necessary. -/
theorem cover_exact (cost : Rat) (hc : 0 ≤ cost) (n : Nat) (stock : Rat) :
    Lasting.Lasts (worstSupport cost) (fun _ => True) (fun x => 5 ≤ x) n stock ↔
      RegimeTransition.cover cost n ≤ stock :=
  Lasting.lasts_iff_of_exact (C := fun k x => RegimeTransition.cover cost k ≤ x)
    ⟨fun k _ held => Rat.le_trans (RegimeTransition.cover_floor cost hc k) held,
     fun k x _ _ held => RegimeTransition.cover_step cost x 0 k hc Rat.le_refl held⟩
    ⟨fun _ held => held,
     fun k x _ next => by
       have h := next () trivial
       have h5 := RegimeTransition.cover_floor cost hc k
       change RegimeTransition.cover cost k ≤ supportStep x (1/10) 2 1 0 0 cost at h
       unfold supportStep at h
       show (10/9) * (RegimeTransition.cover cost k + 1 + cost) ≤ x
       grind⟩ n stock

/-! ## Partial correction boundary -/

/-- The regime law with correction strength `b` is a determined law. -/
theorem path_eq (b : Rat) (s : RegimeBoundary.OperatingState) :
    ∀ n, PartialRegimeTransition.path b s n = Law.orbit (RegimeAttraction.family b) s n
  | 0 => rfl
  | n + 1 => congrArg (RegimeAttraction.family b) (path_eq b s n)

/-- **Some positive seed never lands exactly when some set closed under the regime law and
avoiding landing contains a positive seed.** -/
theorem never_lands_iff (b : Rat) :
    (∃ s, (RegimeAttraction.physical s ∧ 0 < s.1) ∧
        ∀ n, ¬ RegimeTransition.Landing (PartialRegimeTransition.path b s n)) ↔
      ∃ K : RegimeBoundary.OperatingState → Prop,
        (∃ s, (RegimeAttraction.physical s ∧ 0 < s.1) ∧ K s) ∧
        (∀ x, K x → ¬ RegimeTransition.Landing x) ∧
        ∀ x, K x → K (RegimeAttraction.family b x) := by
  constructor
  · intro ⟨s, seeded, avoids⟩
    exact Lasting.some_avoids_iff.mp ⟨s, seeded, fun n => by rw [← path_eq]; exact avoids n⟩
  · intro found
    obtain ⟨s, seeded, avoids⟩ := Lasting.some_avoids_iff.mpr found
    exact ⟨s, seeded, fun n => by rw [path_eq]; exact avoids n⟩

/-- The quality margin at the fixed quality `3/8` under the worst influence `1` is nonnegative
exactly at correction strengths up to `5/12`. -/
theorem margin_iff (b : Rat) : 0 ≤ RegimeBoundary.margin (1/4) b 1 (3/8) ↔ b ≤ 5/12 := by
  unfold RegimeBoundary.margin
  constructor <;> intro h <;> grind

/-- **For `0 ≤ b ≤ 3/4`, every positive seed lands exactly when the quality margin at the fixed
quality is nonnegative.** -/
theorem lands_iff_margin (b : Rat) (hb0 : 0 ≤ b) (hb1 : b ≤ 3/4) :
    (∀ s, RegimeAttraction.physical s → 0 < s.1 →
        ∃ n, RegimeTransition.Landing (PartialRegimeTransition.path b s n)) ↔
      0 ≤ RegimeBoundary.margin (1/4) b 1 (3/8) :=
  (PartialRegimeTransition.exact_universal_landing_boundary b hb0 hb1).trans (margin_iff b).symm

/-- **For `0 ≤ b ≤ 3/4`, every positive seed lands exactly when no set closed under the regime
law and avoiding landing contains a positive seed.** -/
theorem lands_iff_no_closed (b : Rat) (hb0 : 0 ≤ b) (hb1 : b ≤ 3/4) :
    (∀ s, RegimeAttraction.physical s → 0 < s.1 →
        ∃ n, RegimeTransition.Landing (PartialRegimeTransition.path b s n)) ↔
      ¬ ∃ K : RegimeBoundary.OperatingState → Prop,
        (∃ s, (RegimeAttraction.physical s ∧ 0 < s.1) ∧ K s) ∧
        (∀ x, K x → ¬ RegimeTransition.Landing x) ∧
        ∀ x, K x → K (RegimeAttraction.family b x) := by
  constructor
  · intro lands
    apply Lasting.reaches_excludes
    intro s seeded
    obtain ⟨n, hn⟩ := lands s seeded.1 seeded.2
    exact ⟨n, by rw [← path_eq]; exact hn⟩
  · intro none_found
    apply (PartialRegimeTransition.exact_universal_landing_boundary b hb0 hb1).mpr
    by_cases hb : b ≤ 5/12
    · exact hb
    · obtain ⟨s, hs, hx, never⟩ :=
        PartialRegimeTransition.supercritical_positive_fixed_obstruction b (by grind) hb1
      exact absurd ((never_lands_iff b).mp ⟨s, ⟨hs, hx⟩, never⟩) none_found

/-- **Above the boundary the fixed configuration is a closed set avoiding landing by itself**:
for `5/12 < b ≤ 3/4`, `middle b` is a positive physical seed that never lands, an instance of
`fixed_avoids`. -/
theorem fixed_point_instance (b : Rat) (hb : 5/12 < b) (hu : b ≤ 3/4) :
    RegimeAttraction.physical (RegimeAttraction.middle b) ∧ 0 < (RegimeAttraction.middle b).1 ∧
      ∀ n, ¬ RegimeTransition.Landing
        (PartialRegimeTransition.path b (RegimeAttraction.middle b) n) := by
  have hb0 : 0 < b := by grind
  have hd : 0 < 12*b := Rat.mul_pos (by decide +kernel) hb0
  have hdiv : 5/(12*b) < 1 := (Rat.div_lt_iff hd).mpr (by grind)
  refine ⟨(RegimeAttraction.middle_physical_iff b hb0).mpr (by grind), ?_, ?_⟩
  · change 0 < 1-5/(12*b)
    grind
  · intro n
    rw [path_eq]
    apply Lasting.fixed_avoids (RegimeAttraction.middle_fixed b (by grind) hu)
    unfold RegimeTransition.Landing RegimeAttraction.middle
    grind

end Becoming.MarketInstances
