import Becoming.Viability
import MarketGenerativity

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

end Becoming.MarketInstances
