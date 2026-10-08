import GenerativeCore
import RelationalRenewal

/-! Scratch: RelationalRenewal's single unfolding is the unique infinite run of
a core Process; renewal/consumption are properties of that run's observables. -/
namespace BecomingRun
open Generative

universe u v

/-- Proposed core extension: an infinite execution (already ad hoc in Depletion). -/
structure Run {S : Type u} {A : Type v} (P : Process S A) where
  state : Nat → S
  act : Nat → A
  step : ∀ n, P.step (state n) (act n) (state (n + 1))

/-- The next `k` labels of a run from time `n`. -/
def window {S : Type u} {A : Type v} {P : Process S A} (r : Run P) : Nat → Nat → List A
  | _, 0 => []
  | n, k + 1 => r.act n :: window r (n + 1) k

/-- Every finite window of a run is a core Trace. -/
theorem run_window {S : Type u} {A : Type v} {P : Process S A} (r : Run P) :
    ∀ k n, Trace P (r.state n) (window r n k) (r.state (n + k))
  | 0, n => .nil _
  | k + 1, n => by
    have e : n + 1 + k = n + (k + 1) := (Nat.succ_add n k).trans (Nat.add_succ n k).symm
    exact .cons (r.step n) (e ▸ run_window r k (n + 1))

open RelationalRenewal

def stepLevel (L : Law) (t l : Nat) : Nat :=
  if L.needG ≤ l then (if L.needF ≤ l then l + L.renew + L.contrib t - L.draw t else l + L.renew)
  else (if L.needF ≤ l then l + L.contrib t - L.draw t else l)

/-- The renewal law as a deterministic core process on (time, level). -/
def lawProcess (L : Law) : Process (Nat × Nat) Unit :=
  ⟨fun s _ t => t = (s.1 + 1, stepLevel L s.1 s.2)⟩

def lawRun (L : Law) : Run (lawProcess L) :=
  ⟨fun n => (n, L.level n), fun _ => (), fun _ => rfl⟩

theorem run_unique (L : Law) (r : Run (lawProcess L)) (h0 : r.state 0 = (0, L.start)) :
    ∀ n, r.state n = (n, L.level n)
  | 0 => h0
  | n + 1 => by
    have ih := run_unique L r h0 n
    have st := r.step n
    simp only [lawProcess] at st
    rw [st, ih]
    rfl

/-- The module's unfolding is read off the unique run: `level` is an observable. -/
theorem unfolding_level_is_run_observable (L : Law) (r : Run (lawProcess L))
    (h0 : r.state 0 = (0, L.start)) (t : Nat) (c : Unit) :
    L.unfolding.level t c = (r.state t).2 := by
  rw [run_unique L r h0 t]
  rfl

end BecomingRun

#print axioms BecomingRun.run_window
#print axioms BecomingRun.run_unique
#print axioms BecomingRun.unfolding_level_is_run_observable
