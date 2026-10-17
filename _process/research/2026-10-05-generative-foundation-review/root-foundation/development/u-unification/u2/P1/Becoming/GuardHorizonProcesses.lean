import Becoming.Viability
import CorrectionInfrastructure

/-!
# A guard kept over a horizon: the step relation of `CorrectionInfrastructure` as a process

`CorrectionInfrastructure` states, for a step relation `step : S → A → S → Prop` and a guard
`access : S → Prop`, when a guard can be kept for `n` steps by a choice of moves against every
successor (`Viable`, `Admissible`, `Closed`), and when such a choice can be made from readings of
the configurations (`UniformPolicy`). A step relation of that shape is the step of a process of the
spine, and a deterministic law with free moves `next : S → A → S` is the process
`Viability.disturbed next (fun _ => True)`. This module states those laws of every process.

* **One step of the horizon.** The guard is kept for `n + 1` steps from `s` exactly when `s` is
  within it and some enabled move leads only to configurations keeping it for `n` steps
  (`viable_succ_iff`); a configuration keeping it for any horizon is within it (`viable_guard`).
  A move the process does not enable keeps nothing (`not_enabled_not_admissible`): no vacuous
  universal over absent successors counts.
* **Closed sets and the spine's certificates.** Every configuration of a set within the guard
  from which some enabled move stays in the set keeps the guard at every horizon
  (`closed_viable`). A certificate of the spine's viability law (`Viability.Certificate`) whose
  configurations each have an enabled move is such a set (`certificate_closed`,
  `certificate_viable`), and so is the kernel: where no course leaves the guard and every
  configuration reached has an enabled move, the guard is kept at every horizon
  (`kernel_viable`).
* **Deterministic laws.** Keeping the guard under a deterministic law (`DViable`) is keeping it
  in the law's process (`dViable_iff`), and the course of any choice of moves that stays within
  the guard shows that its start keeps it (`safe_path_viable`). A trace kept within the guard
  (`Kept`) is a trace of the process (`Kept.trace`); a choice of moves stays within the guard over
  `n` steps (`PathSafe`) exactly when its moves (`moves`, ending at `last`) form a trace of the
  law's process kept within the guard (`pathSafe_iff`).
* **Choosing from readings.** A choice of admissible moves made from a reading of the
  configurations keeps the guard one step further from every configuration within it
  (`uniform_viable`), and it survives every finer reading (`uniform_finer`).

Which guard marks what an activity needs is supplied with each application; nothing here says
that a closed set, a certificate or a uniform choice exists. No ethical predicate, ranking or
axiom occurs.
-/

namespace Becoming

open Generative

namespace GuardHorizonProcesses

open CorrectionInfrastructure

variable {S A : Type} (P : Process S A) (guard : S → Prop)

/-! ## One step of the horizon -/

/-- **The guard is kept for `n + 1` steps exactly when the configuration is within it and some
enabled move leads only to configurations keeping it for `n` steps.** -/
theorem viable_succ_iff (n : Nat) (s : S) :
    Viable P.step guard (n + 1) s ↔
      guard s ∧ ∃ a, Enabled P s a ∧ ∀ t, P.step s a t → Viable P.step guard n t :=
  viable_iff_access_and_admissible P.step guard n s

/-- **A configuration keeping the guard for any horizon is within the guard.** -/
theorem viable_guard {n : Nat} {s : S} (kept : Viable P.step guard n s) : guard s :=
  viable_has_current_access P.step guard n s kept

/-- **A move the process does not enable keeps nothing.** -/
theorem not_enabled_not_admissible {n : Nat} {s : S} {a : A} (absent : ¬ Enabled P s a) :
    ¬ Admissible P.step guard n s a :=
  dead_action_not_admissible P.step guard n s a (fun t st => absent ⟨t, st⟩)

/-! ## Closed sets and the spine's certificates -/

/-- **Every configuration of a closed set keeps the guard at every horizon.** -/
theorem closed_viable {K : S → Prop} (closed : Closed P.step guard K) :
    ∀ n s, K s → Viable P.step guard n s :=
  closed_implies_every_finite_horizon P.step guard K closed

/-- **A certificate of the spine's viability law whose configurations each have an enabled move is
closed.** -/
theorem certificate_closed {K : S → Prop} (cert : Viability.Certificate P guard K)
    (live : ∀ s, K s → ∃ a, Enabled P s a) : Closed P.step guard K :=
  fun s held => ⟨cert.within s held,
    match live s held with
    | ⟨a, enabled⟩ => ⟨a, enabled, fun t st => cert.closed s a t st held⟩⟩

/-- **Every configuration of such a certificate keeps the guard at every horizon.** -/
theorem certificate_viable {K : S → Prop} (cert : Viability.Certificate P guard K)
    (live : ∀ s, K s → ∃ a, Enabled P s a) : ∀ n s, K s → Viable P.step guard n s :=
  closed_viable P guard (certificate_closed P guard cert live)

/-- **Where no course leaves the guard and every configuration reached has an enabled move, the
guard is kept at every horizon.** -/
theorem kernel_viable {s : S} (kept : Viability.Kernel P guard s)
    (live : ∀ t, Reach P s t → ∃ a, Enabled P t a) : ∀ n, Viable P.step guard n s :=
  fun n => closed_implies_every_finite_horizon P.step guard (Reach P s)
    (fun t reach => ⟨kept t reach,
      match live t reach with
      | ⟨a, enabled⟩ => ⟨a, enabled, fun _ st => reach.trans (Reach.of_step st)⟩⟩)
    n s (Reach.refl P s)

/-! ## Deterministic laws -/

/-- **Keeping the guard under a deterministic law is keeping it in the law's process.** -/
theorem dViable_iff (next : S → A → S) :
    ∀ n s, DViable next guard n s ↔ Viable (Viability.disturbed next fun _ => True).step guard n s
  | 0, _ => Iff.rfl
  | n + 1, s =>
    ⟨fun ⟨within, a, kept⟩ => ⟨within, a, ⟨next s a, trivial, rfl⟩,
        fun _ ⟨_, lands⟩ => lands ▸ (dViable_iff next n (next s a)).mp kept⟩,
     fun ⟨within, a, _, all⟩ => ⟨within, a, (dViable_iff next n (next s a)).mpr
        (all (next s a) ⟨trivial, rfl⟩)⟩⟩

/-- **The course of a choice of moves that stays within the guard shows that its start keeps the
guard in the law's process.** -/
theorem safe_path_viable (next : S → A → S) (policy : Nat → S → A) (n : Nat) (s : S)
    (safe : PathSafe next guard policy n s) :
    Viable (Viability.disturbed next fun _ => True).step guard n s :=
  (dViable_iff guard next n s).mp (safe_path_is_viable next guard policy n s safe)

/-! ## Courses kept within the guard -/

/-- A trace of a process every configuration of which is within the guard. -/
inductive Kept : S → List A → S → Prop where
  | nil {s : S} : guard s → Kept s [] s
  | cons {s m t : S} {a : A} {as : List A} :
      guard s → P.step s a m → Kept m as t → Kept s (a :: as) t

variable {P guard} in
/-- **A course kept within the guard is a trace of the process.** -/
theorem Kept.trace {s t : S} {as : List A} : Kept P guard s as t → Trace P s as t
  | .nil _ => .nil _
  | .cons _ st rest => .cons st rest.trace

variable {P guard} in
/-- A course kept within the guard begins within it. -/
theorem Kept.start {s t : S} {as : List A} : Kept P guard s as t → guard s
  | .nil within => within
  | .cons within _ _ => within

/-- The moves of a choice of moves over `n` steps under a deterministic law, the choice at each
step depending on the steps left and the configuration. -/
def moves (next : S → A → S) (policy : Nat → S → A) : Nat → S → List A
  | 0, _ => []
  | n + 1, s => policy n s :: moves next policy n (next s (policy n s))

/-- Where those `n` moves end. -/
def last (next : S → A → S) (policy : Nat → S → A) : Nat → S → S
  | 0, s => s
  | n + 1, s => last next policy n (next s (policy n s))

/-- **A choice of moves stays within the guard over `n` steps exactly when its course is a trace of
the law's process kept within the guard.** -/
theorem pathSafe_iff (next : S → A → S) (policy : Nat → S → A) :
    ∀ n s, PathSafe next guard policy n s ↔
      Kept (Viability.disturbed next fun _ => True) guard s (moves next policy n s)
        (last next policy n s)
  | 0, _ => ⟨fun within => .nil within, fun | .nil within => within⟩
  | n + 1, _ =>
    ⟨fun ⟨within, rest⟩ => .cons within ⟨trivial, rfl⟩ ((pathSafe_iff next policy n _).mp rest),
     fun | .cons within ⟨_, rfl⟩ rest => ⟨within, (pathSafe_iff next policy n _).mpr rest⟩⟩

/-! ## Choosing from readings -/

/-- **A choice of admissible moves made from a reading of the configurations keeps the guard one
step further from every configuration within it.** -/
theorem uniform_viable {O : Type} {read : S → O} {n : Nat}
    (uniform : UniformPolicy read (Admissible P.step guard n)) {s : S} (within : guard s) :
    Viable P.step guard (n + 1) s :=
  match uniform with
  | ⟨choice, admissible⟩ =>
    (viable_iff_access_and_admissible P.step guard n s).mpr ⟨within, choice (read s), admissible s⟩

/-- **A choice of admissible moves made from a reading survives every finer reading.** -/
theorem uniform_finer {O R : Type} {coarse : S → O} {fine : S → R} (forget : R → O)
    (compatible : ∀ s, forget (fine s) = coarse s) {n : Nat}
    (uniform : UniformPolicy coarse (Admissible P.step guard n)) :
    UniformPolicy fine (Admissible P.step guard n) :=
  uniform_safety_survives_finer_evidence coarse fine forget compatible _ uniform

end GuardHorizonProcesses

end Becoming
