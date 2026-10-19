import Becoming.CourseWorlds

/-!
# Formed loops: worlds whose loops form within them

`Becoming.Closing` states how loops form: the strengths before a step keep the couplings acting
before it (`strengthsBefore`), the carried amount up to a step reads only those
(`carried_before`), and two witnesses show a loop forming at a step, a self-loop that acts from
step `T` on (`Closing.Onset`) and an exchange that comes to respond to its own level once the level
reaches `θ` (`Closing.Threshold`). `Becoming.CourseWorlds` reads the carrying law's courses as
worlds (`carriedWorld`, `formedWorld`). This module states Closing's laws about those worlds.

* **Up to a step, a formed world is the world its couplings formed before that step carry.** The
  standing of a world whose strengths are read off its own standing (`formedWorld`) at every step
  up to `T` is the standing of the balanced world carried by the couplings it read before `T`
  (`formedWorld_before`, through `Closing.carried_before`): what a world has formed by a step is
  all its course up to that step shows.
* **A loop forming at a step, in a world.** The world of the self-loop acting from `T` on
  (`onsetWorld`) balances, stands at the starting gap up to `T`, doubles at every step from `T`,
  and up to `T` stands as the world of a loop forming at any later step (`onsetWorld_course`).
* **A loop a world reads off its own standing.** In the threshold world (`thresholdWorld`) the
  exchange comes to respond to the level it gives to once the level reaches `θ`. The world
  balances; the loop of the couplings it reads off its own standing forms at step `θ` and not
  before; its standing is `t` up to `θ`, and from `θ` on the standing plus one doubles at every
  step; and up to `θ` its standing is that of the threshold world of every later threshold
  (`thresholdWorld_course`). Which loops form, and when, is read off the world itself.
* **How often a loop couples, in a world.** The world of a self-loop coupling at the steps a
  schedule marks (`scheduleWorld`, from `Becoming.Frequency`) balances and stands at
  `D * (1 + M) ^ a`, `a` the number of marked steps so far; its standing is bounded by a
  polynomial exactly where two to that number is (`scheduleWorld_course`). On the sparse schedule
  `0, 1, 3, 7, …` the coupling recurs, the standing stays polynomial, and no finite order of the
  carried amount is exact (`sparseWorld_course`).

Each witness's own law is cited from its module, not proved again; what this module adds is that
each witness amount is the standing of a balanced world, a run of the law of exchange
(`Becoming.Runs`).

What is not derived: which strengths an actual world reads off its course; a characterization of
when a loop of read strengths forms for every law. The general formation laws of
`Becoming.Closing` (`onLoop_succ_iff`, `forms_by_closing`) hold for every array of strengths and
so for the strengths a world reads; stating them again with the array named after a world would
add only the name. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

section Formed

variable {F C : Type} {cs : List C} {part : F → Bool} {σ : Nat → F → C → Nat}
  {present : Nat → List F} {δ : C → Nat} {κ : (Nat → C → Nat) → Nat → F → C → Nat → C → Nat}

/-- The couplings a formed world reads off its own standing. -/
def formedCouplings (cs : List C) (part : F → Bool) (σ : Nat → F → C → Nat)
    (κ : (Nat → C → Nat) → Nat → F → C → Nat → C → Nat) (present : Nat → List F) (δ : C → Nat) :
    Nat → F → C → Nat → C → Nat :=
  κ fun s d => (formedWorld cs part σ κ present δ).web.level s (.inr d)

/-- **Up to a step, a formed world is the world its couplings formed before that step carry.**
At every step up to `T`, the standing of a world whose strengths are read off its own standing is
the standing of the balanced world carried by the couplings it read before `T`. -/
theorem formedWorld_before (reads : ReadsBefore κ) {T t : Nat} (le : t ≤ T) (c : C) :
    (formedWorld cs part σ κ present δ).web.level t (.inr c) =
        (carriedWorld cs part σ (strengthsBefore T (formedCouplings cs part σ κ present δ))
          present δ).web.level t (.inr c) ∧
      (carriedWorld cs part σ (strengthsBefore T (formedCouplings cs part σ κ present δ))
          present δ).Balanced :=
  ⟨(formedWorld_level reads t c).trans (carried_before t le t (Nat.le_refl t) c).symm,
   carriedWorld_balanced⟩

end Formed

namespace FormedLoops

/-- The world of a self-loop of strength one acting from step `T` on, carrying a starting gap `D`. -/
def onsetWorld (T D : Nat) : World :=
  carriedWorld [()] (fun _ => false) (fun _ _ _ => 0) (Closing.Onset.strengths T) (fun _ => [()])
    (fun _ => D)

/-- The standing of the onset world is what the self-loop carries. -/
theorem onsetWorld_level (T D t : Nat) :
    (onsetWorld T D).web.level t (.inr ()) = Closing.Onset.amount T D t :=
  rfl

/-- **A balanced world whose standing does not show a loop until it forms, and doubles from
then.** The onset world balances, stands at the starting gap up to `T`, doubles at every step from
`T`, and up to `T` stands as the onset world of every later step. -/
theorem onsetWorld_course (T D : Nat) :
    (onsetWorld T D).Balanced ∧
      (∀ t, t ≤ T → (onsetWorld T D).web.level t (.inr ()) = D) ∧
      (∀ r, (onsetWorld T D).web.level (T + r) (.inr ()) = D * 2 ^ r) ∧
      ∀ T', T ≤ T' → ∀ t, t ≤ T →
        (onsetWorld T D).web.level t (.inr ()) = (onsetWorld T' D).web.level t (.inr ()) :=
  ⟨carriedWorld_balanced, Closing.Onset.amount_before, Closing.Onset.amount_after T D,
   fun _ later _ le => Closing.Onset.unforeseen later le⟩

/-- The threshold world: a steady gap of one from the part raises the one condition, and the
exchange outside the part responds to the condition's level once it has reached `θ`. -/
def thresholdWorld (θ : Nat) : World :=
  formedWorld [()] (fun h => h) (fun _ _ _ => 1) (Closing.Threshold.reading θ)
    (fun _ => [true, false]) (fun _ => 0)

/-- The standing of the threshold world is the threshold witness's level. -/
theorem thresholdWorld_level (θ t : Nat) :
    (thresholdWorld θ).web.level t (.inr ()) = Closing.Threshold.level θ t :=
  rfl

/-- The couplings the threshold world reads off its own standing. -/
def readOff (θ : Nat) : Nat → Bool → Unit → Nat → Unit → Nat :=
  Closing.Threshold.reading θ fun s d => (thresholdWorld θ).web.level s (.inr d)

/-- **A loop a world reads off its own standing.** The threshold world balances; the loop of the
couplings it reads off its own standing forms at step `θ` and not before; its standing is `t` up
to `θ`, and from `θ` on the standing plus one doubles at every step; and up to `θ` it stands as the
threshold world of every later threshold. -/
theorem thresholdWorld_course (θ : Nat) :
    (thresholdWorld θ).Balanced ∧
      (OnLoop [()] (fun h => h) (strengthsBefore (θ + 1) (readOff θ)) (fun _ => [true, false]) () ∧
        ¬ OnLoop [()] (fun h => h) (strengthsBefore θ (readOff θ)) (fun _ => [true, false]) ()) ∧
      (∀ t, t ≤ θ → (thresholdWorld θ).web.level t (.inr ()) = t) ∧
      (∀ r, (thresholdWorld θ).web.level (θ + r) (.inr ()) + 1 = (θ + 1) * 2 ^ r) ∧
      ∀ θ', θ ≤ θ' → ∀ t, t ≤ θ →
        (thresholdWorld θ).web.level t (.inr ()) = (thresholdWorld θ').web.level t (.inr ()) :=
  ⟨formedWorld_balanced (Closing.Threshold.reads θ),
   ⟨Closing.Threshold.forms θ, Closing.Threshold.not_formed θ⟩,
   Closing.Threshold.level_before θ, Closing.Threshold.level_after θ,
   fun _ later _ le => Closing.Threshold.unforeseen later le⟩

/-- The world of a self-loop of strength `M` coupling at the steps a schedule marks, carrying a
starting gap `D` (`Becoming.Frequency`). -/
def scheduleWorld (on : Nat → Bool) (M D : Nat) : World :=
  carriedWorld [()] (fun _ => false) (fun _ _ _ => 0) (Frequency.SelfLoop.strengths on M)
    (fun _ => [()]) (fun _ => D)

/-- **The rate is a world's standing.** The schedule world balances and stands at
`D * (1 + M) ^ a`, with `a` the number of marked steps before `t`; with strength and gap positive,
its standing is bounded by a polynomial in the steps exactly where two to that number is. -/
theorem scheduleWorld_course (on : Nat → Bool) (M D : Nat) :
    (scheduleWorld on M D).Balanced ∧
      (∀ t, (scheduleWorld on M D).web.level t (.inr ()) = D * (1 + M) ^ Frequency.count on t) ∧
      (1 ≤ M → 1 ≤ D →
        ((∃ A n, ∀ t, (scheduleWorld on M D).web.level t (.inr ()) ≤ A * (t + 1) ^ n) ↔
          ∃ A n, ∀ t, 2 ^ Frequency.count on t ≤ A * (t + 1) ^ n)) :=
  ⟨carriedWorld_balanced, Frequency.SelfLoop.carried_eq on M D,
   fun strong pos => Frequency.SelfLoop.polynomial_iff on strong pos⟩

/-- **A world whose loop recurs and does not run away.** On the sparse schedule `0, 1, 3, 7, …`,
with strength and gap positive, the schedule world balances, its coupling recurs, its standing is
at most a polynomial in the steps of degree `M`, and every finite order of the carried amount
misses some of its standing at some step. -/
theorem sparseWorld_course {M D : Nat} (strong : 0 < M) (pos : 0 < D) :
    (scheduleWorld Frequency.Sparse.on M D).Balanced ∧
      CouplingRecurs [()] (fun _ => false) (Frequency.SelfLoop.strengths Frequency.Sparse.on M)
        (fun _ => [()]) () () ∧
      (∀ t, (scheduleWorld Frequency.Sparse.on M D).web.level t (.inr ()) ≤
        D * 2 ^ M * (t + 1) ^ (1 * M)) ∧
      ∀ J, ∃ t, carriedWithin [()] (fun _ => false) (fun _ _ _ => 0)
          (Frequency.SelfLoop.strengths Frequency.Sparse.on M) (fun _ => [()]) (fun _ => D) J t () <
        (scheduleWorld Frequency.Sparse.on M D).web.level t (.inr ()) :=
  ⟨carriedWorld_balanced, Frequency.Sparse.recurs strong, Frequency.Sparse.polynomial M D,
   Frequency.Sparse.inexact strong pos⟩

end FormedLoops

end Becoming
